"""Ürün modeli (c3ft_urun*) için hikâye üretimi: figür kartlarına bağlı istem, isim süzgeci, K aday + seçici.

Eski üretim yolu (uret.py, sec.py, web, firmware) data/karakterler.json'daki hayvan oyuncaklara bağlı; ürün modeli ise
data/urun_kartlari.json'daki çizgi film figürleriyle (data/urun_v2) eğitildi. Bu araç aynı gen ikilisini ve aynı
örnekleme ayarlarını (sıcaklık 0.5, top-k 40, tekrar 1.1, plan modu, gövdede satır sonu yasağı) ürün figürleriyle
kullanır:
  - istem eğitim dizgisiyle aynı biçimde: <|endoftext|> + 'Karakter: F | Yer: Y[ | Yan: X]\\nSorun:' (urun_kayit.dizgi)
  - isim süzgeci (gen -Y, runtime/isim_suzgec.h): başka figürlerin ve onların adlı yan karakterlerinin adları,
    çok parçalı olsalar da üretilemez; figürün kendi kadrosu serbesttir
  - K aday üretilir, seçici (sec.py kuralları + ürün adları) en iyisini alır

Kullanım:
  python degerlendirme/urun_uret.py <model_dizini> <cikti.json> [--aday K] [--suzgec/--suzgecsiz] [--yan]
                                    [--figur niloya,pepee] [--tekrar-vaka 1] [--temp 0.5]
Çıktı: [{figur, yer, yan, seed, plan, metin, puan, cezalar, yanlis_isim, bitti, plan_bozuk, adaylar: [...]}]
Vakalar: her figürün kart yerleri (figür × yer), seed'ler sabit (tekrarlanabilir).
"""
import argparse, json, os, random, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, YABANCI  # noqa: E402
import sec  # noqa: E402

GEN = os.environ.get("GEN", os.path.join(ROOT, "gen"))
KARTLAR = {k["kimlik"]: k for k in json.load(open(os.path.join(ROOT, "data", "urun_kartlari.json"),
                                                    encoding="utf-8"))["kartlar"]}
# ürün modelinin verisi olan figürler (data/urun_v2/<kimlik>.txt)
FIGURLER = [k for k in KARTLAR if os.path.exists(os.path.join(ROOT, "data", "urun_v2", f"{k}.txt"))]
NL, SATIR_YASAK, EOT = 199, [199, 9491], 0
BOZUK_LP = -99.0


def figur_adlari(kimlik):
    """Figürün kendi adı ve adlı yanlarının büyük harfli yüzey biçimleri (rol yanları: 'Anne', 'Dede' hariç;
    onlar her figürde geçebilir). Çok kelimeli adın ayırt edici kelimeleri de eklenir ('Basri Amca' -> 'Basri')."""
    k = KARTLAR[kimlik]
    adlar = {k["ad"]["deger"]}
    for y in k["yanlar"]:
        if y.get("tip") != "adli":
            continue
        for s in y["yuzey_bicimleri"] + [y["kisa_ad"]]:
            if s[:1].isupper():
                adlar.add(s)
    for a in list(adlar):
        parca = re.split(r"[ \-]", a)
        if len(parca) > 1:
            adlar.update(p for p in parca if p not in {"Amca", "Dede", "Adam", "Koca", "Fil", "Hello", "Ayı", "Örümcek"} and len(p) > 2)
    return adlar


def kadro_disi(kimlik):
    """Bu figürün hikâyesinde geçmemesi gereken adlar: diğer bütün figürler ve adlı yanları, eğitim verisindeki
    yabancı adlar. Figürün kendi kadrosundaki adlar (ör. Elsa için Anna) hiçbir zaman yasak değil."""
    izinli = figur_adlari(kimlik)
    tum = set(YABANCI) | {k["isim"] for k in KAR.values()}  # eski oyuncak adları (genel veride ve eski ince ayarda)
    for k in FIGURLER:
        tum |= figur_adlari(k)
    return sorted(a for a in tum - izinli if not any(a in i.split() for i in izinli) and a not in ("Ayı", "Örümcek"))


def _bayt_haritasi():
    """ByteLevel BPE: token karakteri -> bayt (GPT-2 bytes_to_unicode'un tersi)."""
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs, n = bs[:], 0
    for b in range(256):
        if b not in bs:
            bs.append(b); cs.append(256 + n); n += 1
    return {chr(c): b for b, c in zip(bs, cs)}


def kelime_basi_mi(ad):
    """Ad, sözlükteki daha uzun bir kelimenin başı mı ("Tim" -> "timsah", "Sara" -> "saray")? Öyleyse süzgeç onu
    yalnızca kelime bittiğinde reddeder (isim_suzgec.h '$')."""
    k = sec.kucuk(ad)
    return sec.SOZLUK is not None and any(w != k and w.startswith(k) for w in sec.SOZLUK)


def suzgec_dosyasi(tok, adlar, yol):
    """gen -Y dosyası: V, her token'ın baytları (hex), yasaklı adlar (kelime başı olabilenler '$' ile)."""
    harita = _bayt_haritasi()
    V = tok.get_vocab_size()
    with open(yol, "w", encoding="utf-8") as f:
        f.write(f"{V}\n")
        for i in range(V):
            s = tok.id_to_token(i) or ""
            f.write(bytes(harita[c] for c in s if c in harita).hex() + "\n")
        for a in adlar:
            f.write(a + ("$" if kelime_basi_mi(a) else "") + "\n")
    return yol


def istem(tok, figur_ad, yer, yan):
    bas = f"Karakter: {figur_ad} | Yer: {yer}" + (f" | Yan: {yan}" if yan else "") + "\nSorun:"
    return [EOT] + tok.encode(bas).ids


def aday_uret(model, tok, ids, seed, temp, suzgec=None, n=230):
    cmd = [GEN, os.path.join(model, "model.bin"), str(n), str(temp), "40", str(seed), "1.1",
           "-S", str(NL), "-P", "-N", ",".join(map(str, SATIR_YASAK)), "-l"]
    if suzgec:
        cmd += ["-Y", suzgec]
    r = subprocess.run(cmd + [str(i) for i in ids], capture_output=True, text=True, check=True)
    satir = [s.split() for s in r.stdout.splitlines() if s.strip()]
    toks, lps = [int(a) for a, _ in satir], [float(b) for _, b in satir]
    govde_bas = next((i + 1 for i in range(1, len(toks)) if toks[i] == NL and toks[i - 1] == NL), None)
    if govde_bas is None:
        return {"plan": tok.decode(toks), "metin": "", "bitti": False, "plan_bozuk": True, "lp": BOZUK_LP, "n": 0}
    govde, glp = toks[govde_bas:], lps[govde_bas:]
    bitti = EOT in govde
    if bitti:
        k = govde.index(EOT); govde, glp = govde[:k], glp[:k]
    plan = "Sorun:" + tok.decode(toks[:govde_bas - 2])
    return {"plan": plan.strip(), "metin": tok.decode(govde).strip(), "bitti": bitti, "plan_bozuk": False,
            "lp": sum(glp) / max(1, len(glp)), "n": len(govde)}


YER_ANAHTAR = {"dağ": "dag", "şato": "sato"}


def yanlis_isimler(metin, kimlik):
    yasak = kadro_disi(kimlik)
    return sorted(a for a in yasak if re.search(rf"(?<![\wçğıöşüÇĞİÖŞÜ]){re.escape(a)}(?![a-zçğıöşüâîû])", metin))


def puanla(a, kimlik, yer):
    """sec.py kuralları, ürün figürünün adıyla. İsim kuralları ürün adlarına göre: kadro dışı ad = 'yanlış isim'."""
    if a["plan_bozuk"] or not a["metin"]:
        return -99.0, [(99, "gövde yok")]
    ad = KARTLAR[kimlik]["ad"]["deger"]
    eski = sec.TUM_ISIM
    sec.TUM_ISIM = set().union(*(figur_adlari(k) for k in FIGURLER))  # uydurma ad kuralı ürün adlarıyla
    try:
        # sec.cezalar KAR kimliği ister; ad tabanlı kuralları doğrudan kurarız
        c = []
        metin = a["metin"]
        if len(re.findall(rf"\b{ad}\b", metin)) < 2:
            c.append((3, f"{ad} hikâyede yeterince yok"))
        if not re.search(rf"\b{ad}\b", metin[int(len(metin) * 0.6):]):
            c.append((3, f"{ad} sonda yok"))
        if re.search(rf"\b{ad}\b\s+(?:ve|ile)\s+{ad}\b", metin):
            c.append((3, f"'{ad} ve {ad}'"))
        yanlis = yanlis_isimler(metin, kimlik)
        if yanlis:
            c.append((2, f"yanlış isim {yanlis}"))
        cumleler = [s.strip() for s in re.split(r"(?<=[.!?])\s+", metin) if s.strip()]
        if len(cumleler) != len(set(cumleler)):
            c.append((1, "tekrarlanan cümle"))
        if not metin.rstrip().endswith((".", "!", '"', "”")) or not a["bitti"]:
            c.append((2, "yarım son"))
        if len(metin.split()) < 50:
            c.append((2, "çok kısa"))
        kelimeler = re.findall(r"[a-zçğıöşüâîû]+", sec.kucuk(metin))
        if sec.SOZLUK is not None:
            bilinmeyen = [w for w in kelimeler if w not in sec.SOZLUK]
            if bilinmeyen:
                c.append((1.5 * len(bilinmeyen), f"uydurma kelime {bilinmeyen[:4]}"))
        uclu = [tuple(kelimeler[i:i + 3]) for i in range(len(kelimeler) - 2)]
        tekrar = len(uclu) - len(set(uclu))
        if tekrar > 2:
            c.append((0.5 * (tekrar - 2), f"tekrar eden ifade x{tekrar}"))
        c += sec.olay_cezalari(metin, [ad], a["plan"])
        y = YER_ANAHTAR.get(yer, yer)
        if y in sec.YER_KELIME and sec.yer_cezasi(metin, y):
            c.append((1.5, "yer tutmuyor"))
        if (g := sec.guvenlik_cezasi(metin)):
            c.append(g)
    finally:
        sec.TUM_ISIM = eski
    return -sum(p for p, _ in c) + 2 * a["lp"], c


def vakalar(figurler, tekrar=1, yan=False):
    rng = random.Random(2026)
    out = []
    for f in figurler:
        yanlar = [y["kisa_ad"] for y in KARTLAR[f]["yanlar"]]
        for yer in [y["etiket"] for y in KARTLAR[f]["yerler"]]:
            for r in range(tekrar):
                out.append({"figur": f, "yer": yer, "yan": rng.choice(yanlar) if yan and yanlar else None,
                            "seed": 1000 * len(out) + 7})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model")
    ap.add_argument("cikti")
    ap.add_argument("--aday", type=int, default=1)
    ap.add_argument("--suzgecsiz", action="store_true")
    ap.add_argument("--yan", action="store_true", help="istemde Yan alanı (kart yanlarından biri)")
    ap.add_argument("--figur", default=",".join(FIGURLER))
    ap.add_argument("--tekrar-vaka", type=int, default=1)
    ap.add_argument("--temp", type=float, default=0.5)
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model, "tokenizer.json"))
    gecici = os.path.join(os.path.dirname(os.path.abspath(a.cikti)) or ".", ".suzgec")
    os.makedirs(gecici, exist_ok=True)
    sonuc = []
    for v in vakalar(a.figur.split(","), a.tekrar_vaka, a.yan):
        k = KARTLAR[v["figur"]]
        suz = None if a.suzgecsiz else suzgec_dosyasi(tok, kadro_disi(v["figur"]),
                                                          os.path.join(gecici, f"{v['figur']}.txt"))
        ids = istem(tok, k["ad"]["deger"], v["yer"], v["yan"])
        adaylar = []
        for j in range(a.aday):
            c = aday_uret(a.model, tok, ids, v["seed"] + j, a.temp, suz)
            c["puan"], c["cezalar"] = puanla(c, v["figur"], v["yer"])
            c["yanlis_isim"] = yanlis_isimler(c["metin"], v["figur"])
            adaylar.append(c)
        en = max(adaylar, key=lambda c: c["puan"])
        sonuc.append({**v, **{x: en[x] for x in ("plan", "metin", "puan", "cezalar", "yanlis_isim", "bitti", "plan_bozuk")},
                      "adaylar": adaylar})
        print(f"{v['figur']:12s} {v['yer']:6s} puan {en['puan']:6.2f}  yanlış {en['yanlis_isim']}", file=sys.stderr)
    json.dump(sonuc, open(a.cikti, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n = len(sonuc)
    print(json.dumps({
        "vaka": n,
        "ort_puan": round(sum(s["puan"] for s in sonuc) / n, 3),
        "yanlis_isim_orani": round(sum(1 for s in sonuc if s["yanlis_isim"]) / n, 3),
        "plan_bozuk": sum(1 for s in sonuc if s["plan_bozuk"]),
        "bitmemis": sum(1 for s in sonuc if not s["bitti"]),
        "cezasiz": sum(1 for s in sonuc if not s["cezalar"]),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
