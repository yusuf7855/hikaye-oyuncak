"""Sabit test setinden hikâye üret (hakemlere verilecek).

Kullanım: python degerlendirme/uret.py <model_dizini> <çıktı_adı> [--aday K] [--temp 0.5] [--rep 1.1]
                                      [--baslik eski|tema|plan] [--pencere tum|govde] [--satir-yasak] [--eot-on]
                                      [--plan-kosul model|oracle] [--dogrulama <dogrulama.json>]
  --aday K: her vaka için K aday üret, seçici (sec.py) ile en iyisini al (cihazdaki önceden-üret+filtrele akışı).
  --baslik tema: i. vakaya TEMALAR[(7*i) % 20] verilir, başlık "... | Tema: T" olur.
  --baslik plan (E3, temasız): istem "Karakter: X | Yer: Y\nSorun:" ile biter, model önce planı ("<sorun>\nÇözüm:
      <çözüm>"), sonra Ċ Ċ ve gövdeyi yazar (gen -S 199). Çıktı ilk Ċ Ċ'den bölünür: 'plan' ("Sorun: S\nÇözüm: Ç")
      ve gövde ('metin'; n, lp ve bitti yalnız gövdeden). Gövdesi olmayan aday (gen stderr'de plan_bozuk ya da boş
      gövde) adaylarda plan_bozuk=true, metin="", bitti=false, lp=-99 kalır: seçici onu almaz.
  --plan-kosul oracle: planı model yazmaz, doğrulama hikâyesinin gerçek planı istemde verilir (üst sınır; --baslik
      plan ve --dogrulama ister, test setinin etiketi yok). Verilen plan tekrar penceresine girmez (gen -W), model
      modundaki gibi: (b) ile (c) aynı örnekleyiciyle karşılaştırılır.
  --dogrulama D: 36 vakalık test seti yerine D'deki (prepare_ft2 --plan'ın dogrulama.json'u) planlı hikâyelerin
      (turler, yer) ikilileri; D'de plan alanı yoksa hepsi. Seed'ler aynı kuralla (1000·i+j, i vaka sırası).
  --pencere govde: istem token'ları tekrar cezası penceresine girmez (gen -P).
  --satir-yasak: gövdede yalnız satır sonundan oluşan token'lar yasak (gen -N).
  --eot-on: istemin başına <|endoftext|> (eğitimde her hikâye bir öncekinin EOT'sinden sonra gelir).
Çıktı: degerlendirme/<çıktı_adı>/hikayeler.json  [{id, figurler, yer, (tema), baslik, metin, token}]
       <model_dizini>/adaylar_<çıktı_adı>.json    bütün adaylar [{vaka, j, kim, yer, tema, metin, n, lp, bitti}]
       plan modunda ikisine de plan (ve plan_bozuk), --dogrulama'da hikaye_id eklenir; hakem.py/ikili.py planı
       hakeme göndermez (yalnız metin/başlık alanları).
       (ayarları yanındaki ayar_adaylar_<çıktı_adı>.json'da; aynı ayarla üretilmiş adaylar yeniden üretilmez)
Test seti: 24 tek figür (12 figür × 2 yer) + 12 ikili; seed'ler sabit, sonuçlar tekrarlanabilir.
GEN ortam değişkeni başka bir gen derlemesini gösterebilir (varsayılan: depo kökündeki ./gen).
"""
import argparse, functools, hashlib, json, os, random, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, SIRA, TEMALAR, YER, baslangic, prompt_idler, yasak_idler  # noqa: E402

YERLER = ["orman", "deniz", "ev", "park", "sato", "dag"]
GEN = os.environ.get("GEN", os.path.join(ROOT, "gen"))
BOZUK_LP = -99.0  # gövdesi olmayan planlı adayın lp'si: seçici (sec.puanla) onu hiçbir gövdeli adaya tercih etmez


def test_seti():
    rng = random.Random(2024)
    vakalar = []
    for i, k in enumerate(SIRA):
        vakalar.append(([k], YERLER[i % 6]))
        vakalar.append(([k], YERLER[(i + 3) % 6]))
    ciftler = [(a, b) for i, a in enumerate(SIRA) for b in SIRA[i + 1:]]
    for a, b in rng.sample(ciftler, 12):
        vakalar.append(([a, b], rng.choice(YERLER)))
    return vakalar


def dogrulama_seti(yol):
    """--dogrulama: prepare_ft2'nin dogrulama.json'undan vakalar [(kim, yer, bilgi)]; bilgi = {hikaye_id, tema, plan}.
    Dosyada plan alanı (sorun) varsa yalnız planlı hikâyeler (plan = (sorun, çözüm)), yoksa hepsi (plan = None)."""
    tur = {k["tur"]: k["kimlik"] for k in KAR.values()}
    yer = {y["ad"]: y["kimlik"] for y in YER.values()}
    hik = json.load(open(yol, encoding="utf-8"))
    planli = any("sorun" in h for h in hik)
    vakalar = []
    for h in hik:
        p = (h["sorun"], h["cozum"]) if h.get("sorun") and h.get("cozum") else None
        if planli and p is None:
            continue
        vakalar.append((sorted((tur[t] for t in h["turler"]), key=SIRA.index), yer[h["yer"]],
                        {"hikaye_id": h["id"], "tema": h.get("tema"), "plan": p}))
    return vakalar


def vakalar(dogrulama=None):
    """[(kim, yer, bilgi)]: test seti (bilgi None) ya da --dogrulama hikâyeleri."""
    return dogrulama_seti(dogrulama) if dogrulama else [(k, y, None) for k, y in test_seti()]


def vaka_temasi(i, baslik="eski"):
    """--baslik tema: 36 vaka 20 temanın hepsini kapsar (7 ile 20 aralarında asal)."""
    return TEMALAR[(7 * i) % 20] if baslik == "tema" else None


def satir_idleri(tok):
    """Yalnızca boşluk ve satır sonundan oluşan token'lar (C2'de Ċ=199, ĠĊ=9491): --satir-yasak bunları yasaklar."""
    return [i for i in range(tok.get_vocab_size()) if "\n" in (s := tok.decode([i])) and not s.strip()]


def satir_sonu(tok):
    """Tek satır sonu token'ı (C2'de Ċ = 199): plan modunda gövde ilk Ċ Ċ'den sonra başlar (gen -S)."""
    nl = tok.encode("a\n").ids[-1]
    assert tok.decode([nl]) == "\n", "tokenizer'da tek başına satır sonu token'ı yok"
    return nl


def plan_metni(sorun, cozum):
    return f"Sorun: {sorun}\nÇözüm: {cozum}"


def plan_bol(plan):
    """'plan' alanı -> (sorun, çözüm); biçim "Sorun: S\nÇözüm: Ç" değilse None."""
    m = re.fullmatch(r"Sorun:[ \t]*([^\n]*?)\s*\nÇözüm:[ \t]*([^\n]*?)\s*", plan or "")
    return (m.group(1), m.group(2)) if m and m.group(1) and m.group(2) else None


@functools.lru_cache(maxsize=None)
def gen_kullanim():
    """gen'in kullanım satırı: hangi seçenekleri bildiği (eski derleme -P, -N, -e bilmez)."""
    return subprocess.run([GEN], capture_output=True, text=True).stderr


def _gen(model_dir, ids, ban, seed, temp, rep, tok, n, govde, satir, plan_nl=None, pencere_k=None):
    """gen'i bir kez çağırır. Döner: ([(token, logp)], stderr). plan_nl: gen -S (plan modu); pencere_k: gen -W
    (istemin yalnız ilk k token'ı tekrar penceresine girer)."""
    son = tok.token_to_id("<|endoftext|>")
    ek = (["-P"] if govde else []) + (["-N", ",".join(map(str, satir))] if satir else [])
    # -e: EOT'den sonrası zaten atılıyor; gen orada durur, önceki token'lar aynı kalır (yalnız daha hızlı)
    ek += ["-e", str(son)] if son is not None and "[-e " in gen_kullanim() else []
    ek += ["-S", str(plan_nl)] if plan_nl is not None else []
    ek += ["-W", str(pencere_k)] if pencere_k is not None else []
    r = subprocess.run([GEN, os.path.join(model_dir, "model.bin"), str(n), str(temp), "40",
                        str(seed), str(rep), "-b", ",".join(map(str, ban)), *ek, "-l", *map(str, ids)],
                       capture_output=True, text=True)
    return [(int(a), float(b)) for a, b in (l.split() for l in r.stdout.split("\n") if l.strip())], r.stderr


def _eot_kes(pairs, son):
    """(EOT'ye kadarki çiftler, EOT üretildi mi)."""
    toks = [t for t, _ in pairs]
    return (pairs[:toks.index(son)], True) if son in toks else (pairs, False)


def uret(model_dir, kimlikler, yer, seed, temp, rep, tok, n=240, tema=None, eot=False, govde=False, satir=None):
    """govde: gen -P; satir: gövdede yasak token id'leri (gen -N). Döner: (başlık, metin, n, ort_logp, bitti)."""
    prompt = baslangic(kimlikler, yer, ilk_cumle=False, tema=tema)
    ids = prompt_idler(tok, kimlikler, yer, tema=tema, eot=eot)
    pairs, _ = _gen(model_dir, ids, yasak_idler(tok, kimlikler), seed, temp, rep, tok, n, govde, satir)
    pairs, bitti = _eot_kes(pairs, tok.token_to_id("<|endoftext|>"))
    lp = sum(l for _, l in pairs) / max(1, len(pairs))
    return prompt, tok.decode([t for t, _ in pairs]).strip(), len(pairs), lp, bitti


def uret_plan(model_dir, kimlikler, yer, seed, temp, rep, tok, n=240, eot=False, govde=False, satir=None,
              oracle=None):
    """Plan modu (--baslik plan, temasız). oracle=(sorun, çözüm): gerçek plan istemde (gen -W: plan tekrar penceresine
    girmez), gövde hemen başlar; yoksa model planı yazar (gen -S Ċ) ve çıktı ilk Ċ Ċ'den bölünür. n, lp ve bitti
    yalnız gövdeden.
    Döner: {metin, n, lp, bitti, plan, plan_bozuk}; gövde yoksa metin="", bitti=False, lp=BOZUK_LP."""
    son = tok.token_to_id("<|endoftext|>")
    ban = yasak_idler(tok, kimlikler)
    if oracle is not None:
        ids = prompt_idler(tok, kimlikler, yer, eot=eot, plan_metni=oracle)
        # Verilen plan tekrar penceresine girmez (gen -W): gövde başlarken pencere, model planı kendisi yazdığındaki
        # (gen -S) gibi yalnız "…\nSorun:" istemini tutar; böylece (c) ile (b) aynı örnekleyiciyle karşılaştırılır.
        bas = prompt_idler(tok, kimlikler, yer, eot=eot, plan=True)
        assert ids[:len(bas)] == bas, (kimlikler, yer, oracle)
        govde_ciftleri, _ = _gen(model_dir, ids, ban, seed, temp, rep, tok, n, govde, satir, pencere_k=len(bas))
        plan, bozuk = plan_metni(*oracle), False
    else:
        nl = satir_sonu(tok)
        ids = prompt_idler(tok, kimlikler, yer, eot=eot, plan=True)
        pairs, err = _gen(model_dir, ids, ban, seed, temp, rep, tok, n, govde, satir, plan_nl=nl)
        toks = [t for t, _ in pairs]
        k = next((k for k in range(len(toks) - 1) if toks[k] == nl and toks[k + 1] == nl), None)
        plan_ciftleri = pairs if k is None else pairs[:k]
        govde_ciftleri = [] if k is None else pairs[k + 2:]
        plan = ("Sorun:" + tok.decode([t for t, _ in _eot_kes(plan_ciftleri, son)[0]])).rstrip()
        bozuk = k is None or "plan_bozuk" in err.split()
    govde_ciftleri, bitti = _eot_kes(govde_ciftleri, son)
    metin = tok.decode([t for t, _ in govde_ciftleri]).strip()
    if bozuk or not metin:
        return {"metin": "", "n": 0, "lp": BOZUK_LP, "bitti": False, "plan": plan, "plan_bozuk": oracle is None}
    lp = sum(l for _, l in govde_ciftleri) / len(govde_ciftleri)
    return {"metin": metin, "n": len(govde_ciftleri), "lp": lp, "bitti": bitti, "plan": plan, "plan_bozuk": False}


def bayraklar(ap):
    """uret.py ve otomatik.py'nin ortak üretim bayrakları; hiçbiri verilmezse davranış eskisiyle aynı."""
    ap.add_argument("--baslik", choices=["eski", "tema", "plan"], default="eski",
                    help="tema: i. vakaya TEMALAR[(7*i)%%20], başlık '... | Tema: T'; plan: model önce planı yazar "
                         "(temasız, gen -S)")
    ap.add_argument("--pencere", choices=["tum", "govde"], default="tum",
                    help="govde: istem token'ları tekrar cezası penceresine girmez (gen -P)")
    ap.add_argument("--satir-yasak", action="store_true", help="gövdede satır sonu token'ları yasak (gen -N)")
    ap.add_argument("--eot-on", action="store_true", help="istemin başına <|endoftext|>")
    ap.add_argument("--plan-kosul", choices=["model", "oracle"], default="model",
                    help="--baslik plan: model planı kendisi yazar; oracle: doğrulama hikâyesinin gerçek planı "
                         "istemde (--dogrulama ister)")
    ap.add_argument("--dogrulama", default=None,
                    help="test seti yerine bu dogrulama.json'un planlı hikâyelerinin (turler, yer) ikilileri")


def _sha(yol):
    return hashlib.sha256(open(yol, "rb").read()).hexdigest()[:16] if os.path.exists(yol) else None


def vaka_temasi_(i, bilgi, baslik):
    """--dogrulama'da --baslik tema hikâyenin kendi temasını verir; yoksa vaka_temasi."""
    return bilgi["tema"] if bilgi is not None and baslik == "tema" else vaka_temasi(i, baslik)


def istem(tok, i, kim, yer, bilgi, baslik="eski", eot_on=False, plan_kosul="model"):
    """i. vakanın istem token'ları (gen'e giden)."""
    if baslik == "plan":
        if plan_kosul == "oracle":
            return prompt_idler(tok, kim, yer, eot=eot_on, plan_metni=bilgi["plan"])
        return prompt_idler(tok, kim, yer, eot=eot_on, plan=True)
    return prompt_idler(tok, kim, yer, tema=vaka_temasi_(i, bilgi, baslik), eot=eot_on)


def _istem_ozeti(tok, baslik, eot_on, satir, plan_kosul="model", dogrulama=None):
    """Vakaların gen girdileri (istem, yasak, satır yasağı): baslangic.py ya da tokenizer değişirse havuz eskir."""
    girdi = [[istem(tok, i, kim, yer, bilgi, baslik, eot_on, plan_kosul), yasak_idler(tok, kim)]
             for i, (kim, yer, bilgi) in enumerate(vakalar(dogrulama))]
    ek = ([satir_sonu(tok)] if plan_kosul == "model" else ["W"]) if baslik == "plan" else []  # gen -S / gen -W
    return hashlib.sha256(json.dumps([girdi, satir] + ek).encode()).hexdigest()[:16]


def aday_havuzu(model_dir, ad, K, temp, rep, tok, baslik="eski", pencere="tum", satir_yasak=False, eot_on=False,
                plan_kosul="model", dogrulama=None):
    """Her vaka için K aday (seed 1000·i+j). <model_dir>/adaylar_<ad>.json'a yazılır; aynı ayarlarla (model,
    gen, istemler, temp, rep, bayraklar) üretilmiş bir havuz varsa yalnızca eksik adaylar üretilir.
    Döner: vaka başına aday listesi [{vaka, j, kim, yer, tema, metin, n, lp, bitti}] (plan modunda + plan,
    plan_bozuk; --dogrulama'da + hikaye_id). Vakaların sırası vakalar(dogrulama) ile aynı."""
    if plan_kosul == "oracle" and (baslik != "plan" or not dogrulama):
        raise SystemExit("--plan-kosul oracle, --baslik plan ve --dogrulama <dogrulama.json> ister "
                         "(36 vakalık test setinin plan etiketi yok)")
    vk = vakalar(dogrulama)
    if plan_kosul == "oracle" and any(b["plan"] is None for _, _, b in vk):
        raise SystemExit(f"{dogrulama}: plan alanı yok (prepare_ft2 --plan ile yeniden yazılmalı)")
    yol = os.path.join(model_dir, f"adaylar_{ad}.json")
    ayar_yol = os.path.join(model_dir, f"ayar_adaylar_{ad}.json")
    satir = satir_idleri(tok) if satir_yasak else None
    ayar = {"model": _sha(os.path.join(model_dir, "model.bin")), "gen": _sha(GEN),
            "istem": _istem_ozeti(tok, baslik, eot_on, satir, plan_kosul, dogrulama), "temp": temp, "rep": rep,
            "top_k": 40, "n": 240, "baslik": baslik, "pencere": pencere, "satir_yasak": satir_yasak,
            "eot_on": eot_on}
    # yeni ayarlar yalnız varsayılan değilse yazılır: eski havuzların ayar dosyası geçerli kalır
    if plan_kosul != "model":
        ayar["plan_kosul"] = plan_kosul
    if dogrulama:
        ayar["dogrulama"] = _sha(dogrulama)
    eski = {}
    if os.path.exists(yol) and os.path.exists(ayar_yol):
        onceki = json.load(open(ayar_yol, encoding="utf-8"))
        if onceki == ayar:
            eski = {(h["vaka"], h["j"]): h for h in json.load(open(yol, encoding="utf-8"))}
        else:
            fark = sorted(k for k in ayar if onceki.get(k) != ayar[k])
            print(f"{yol}: ayarlar farklı ({', '.join(fark)}), adaylar yeniden üretiliyor", file=sys.stderr)
    if (pencere == "govde" or satir_yasak) and "-P" not in gen_kullanim():
        raise SystemExit(f"{GEN} -P/-N bilmiyor (eski derleme): rm gen && cc -O3 -o gen runtime/host_verify/gen.c -lm")
    if baslik == "plan" and plan_kosul == "model" and "[-S " not in gen_kullanim():
        raise SystemExit(f"{GEN} -S bilmiyor (eski derleme): rm gen && cc -O3 -o gen runtime/host_verify/gen.c -lm")
    if baslik == "plan" and plan_kosul == "oracle" and "[-W " not in gen_kullanim():
        raise SystemExit(f"{GEN} -W bilmiyor (eski derleme): rm gen && cc -O3 -o gen runtime/host_verify/gen.c -lm")
    havuz, yeni = [], 0
    for i, (kim, yer, bilgi) in enumerate(vk):
        tema = vaka_temasi_(i, bilgi, baslik)
        adaylar = []
        for j in range(K):
            h = eski.get((i, j))
            if h is None or h["kim"] != kim or h["yer"] != yer or h["tema"] != tema:
                if baslik == "plan":
                    h = {"vaka": i, "j": j, "kim": kim, "yer": yer, "tema": tema,
                         **uret_plan(model_dir, kim, yer, 1000 * i + j, temp, rep, tok, eot=eot_on,
                                     govde=pencere == "govde", satir=satir,
                                     oracle=bilgi["plan"] if plan_kosul == "oracle" else None)}
                else:
                    _, metin, n, lp, bitti = uret(model_dir, kim, yer, 1000 * i + j, temp, rep, tok, tema=tema,
                                                  eot=eot_on, govde=pencere == "govde", satir=satir)
                    h = {"vaka": i, "j": j, "kim": kim, "yer": yer, "tema": tema, "metin": metin, "n": n,
                         "lp": lp, "bitti": bitti}
                if bilgi is not None:
                    h["hikaye_id"] = bilgi["hikaye_id"]
                eski[(i, j)] = h
                yeni += 1
            adaylar.append(h)
        havuz.append(adaylar)
    if yeni:
        json.dump([eski[k] for k in sorted(eski)], open(yol, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        json.dump(ayar, open(ayar_yol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{yol}: {sum(map(len, havuz))} aday, {yeni} yeni üretildi", file=sys.stderr)
    return havuz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("ad")
    ap.add_argument("--aday", type=int, default=1)
    ap.add_argument("--temp", type=float, default=0.5)
    ap.add_argument("--rep", type=float, default=1.1)
    ap.add_argument("--havuz", default=None,
                    help="aday havuzu adı (varsayılan: ad); başka bir kolun adaylarını yeni seçiciyle yeniden seçmek için")
    bayraklar(ap)
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    sonuc = []
    if a.aday > 1:
        sys.path.insert(0, HERE)
        from sec import puanla  # noqa: E402
    havuz = aday_havuzu(a.model_dir, a.havuz or a.ad, a.aday, a.temp, a.rep, tok, a.baslik, a.pencere, a.satir_yasak,
                        a.eot_on, a.plan_kosul, a.dogrulama)
    for i, (kim, yer, _) in enumerate(vakalar(a.dogrulama)):
        adaylar = havuz[i]
        h = (max(adaylar, key=lambda x: puanla(x["metin"], kim, x["lp"], x["n"], yer, x["bitti"], plan=x.get("plan")))
             if a.aday > 1 else adaylar[0])
        tema = h["tema"]
        sonuc.append({"id": i, "figurler": [KAR[k]["isim"] + " (" + KAR[k]["tur"] + ")" for k in kim],
                      "yer": yer, **({"tema": tema} if tema else {}),
                      "baslik": baslangic(kim, yer, ilk_cumle=False, tema=tema).strip(), "metin": h["metin"],
                      "token": h["n"], **{k: h[k] for k in ("plan", "plan_bozuk", "hikaye_id") if k in h}})
    os.makedirs(os.path.join(HERE, a.ad), exist_ok=True)
    json.dump(sonuc, open(os.path.join(HERE, a.ad, "hikayeler.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{a.ad}/hikayeler.json")


if __name__ == "__main__":
    main()
