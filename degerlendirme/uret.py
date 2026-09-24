"""Sabit test setinden hikâye üret (hakemlere verilecek).

Kullanım: python degerlendirme/uret.py <model_dizini> <çıktı_adı> [--aday K] [--temp 0.5] [--rep 1.1]
                                      [--baslik eski|tema] [--pencere tum|govde] [--satir-yasak] [--eot-on]
  --aday K: her vaka için K aday üret, seçici (sec.py) ile en iyisini al (cihazdaki önceden-üret+filtrele akışı).
  --baslik tema: i. vakaya TEMALAR[(7*i) % 20] verilir, başlık "... | Tema: T" olur.
  --pencere govde: istem token'ları tekrar cezası penceresine girmez (gen -P).
  --satir-yasak: gövdede yalnız satır sonundan oluşan token'lar yasak (gen -N).
  --eot-on: istemin başına <|endoftext|> (eğitimde her hikâye bir öncekinin EOT'sinden sonra gelir).
Çıktı: degerlendirme/<çıktı_adı>/hikayeler.json  [{id, figurler, yer, (tema), baslik, metin, token}]
       <model_dizini>/adaylar_<çıktı_adı>.json    bütün adaylar [{vaka, j, kim, yer, tema, metin, n, lp, bitti}]
       (ayarları yanındaki ayar_adaylar_<çıktı_adı>.json'da; aynı ayarla üretilmiş adaylar yeniden üretilmez)
Test seti: 24 tek figür (12 figür × 2 yer) + 12 ikili; seed'ler sabit, sonuçlar tekrarlanabilir.
GEN ortam değişkeni başka bir gen derlemesini gösterebilir (varsayılan: depo kökündeki ./gen).
"""
import argparse, functools, hashlib, json, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, SIRA, TEMALAR, baslangic, prompt_idler, yasak_idler  # noqa: E402

YERLER = ["orman", "deniz", "ev", "park", "sato", "dag"]
GEN = os.environ.get("GEN", os.path.join(ROOT, "gen"))


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


def vaka_temasi(i, baslik="eski"):
    """--baslik tema: 36 vaka 20 temanın hepsini kapsar (7 ile 20 aralarında asal)."""
    return TEMALAR[(7 * i) % 20] if baslik == "tema" else None


def satir_idleri(tok):
    """Yalnızca boşluk ve satır sonundan oluşan token'lar (C2'de Ċ=199, ĠĊ=9491): --satir-yasak bunları yasaklar."""
    return [i for i in range(tok.get_vocab_size()) if "\n" in (s := tok.decode([i])) and not s.strip()]


@functools.lru_cache(maxsize=None)
def gen_kullanim():
    """gen'in kullanım satırı: hangi seçenekleri bildiği (eski derleme -P, -N, -e bilmez)."""
    return subprocess.run([GEN], capture_output=True, text=True).stderr


def uret(model_dir, kimlikler, yer, seed, temp, rep, tok, n=240, tema=None, eot=False, govde=False, satir=None):
    """govde: gen -P; satir: gövdede yasak token id'leri (gen -N). Döner: (başlık, metin, n, ort_logp, bitti)."""
    prompt = baslangic(kimlikler, yer, ilk_cumle=False, tema=tema)
    ids = prompt_idler(tok, kimlikler, yer, tema=tema, eot=eot)
    ban = yasak_idler(tok, kimlikler)
    son = tok.token_to_id("<|endoftext|>")
    ek = (["-P"] if govde else []) + (["-N", ",".join(map(str, satir))] if satir else [])
    # -e: EOT'den sonrası zaten atılıyor; gen orada durur, önceki token'lar aynı kalır (yalnız daha hızlı)
    ek += ["-e", str(son)] if son is not None and "[-e " in gen_kullanim() else []
    out = subprocess.run([GEN, os.path.join(model_dir, "model.bin"), str(n), str(temp), "40",
                          str(seed), str(rep), "-b", ",".join(map(str, ban)), *ek, "-l", *map(str, ids)],
                         capture_output=True, text=True).stdout.split("\n")
    pairs = [(int(a), float(b)) for a, b in (l.split() for l in out if l.strip())]
    toks = [t for t, _ in pairs]
    bitti = son in toks
    if bitti:
        pairs = pairs[:toks.index(son)]
    lp = sum(l for _, l in pairs) / max(1, len(pairs))
    return prompt, tok.decode([t for t, _ in pairs]).strip(), len(pairs), lp, bitti


def bayraklar(ap):
    """uret.py ve otomatik.py'nin ortak üretim bayrakları; hiçbiri verilmezse davranış eskisiyle aynı."""
    ap.add_argument("--baslik", choices=["eski", "tema"], default="eski",
                    help="tema: i. vakaya TEMALAR[(7*i)%%20], başlık '... | Tema: T'")
    ap.add_argument("--pencere", choices=["tum", "govde"], default="tum",
                    help="govde: istem token'ları tekrar cezası penceresine girmez (gen -P)")
    ap.add_argument("--satir-yasak", action="store_true", help="gövdede satır sonu token'ları yasak (gen -N)")
    ap.add_argument("--eot-on", action="store_true", help="istemin başına <|endoftext|>")


def _sha(yol):
    return hashlib.sha256(open(yol, "rb").read()).hexdigest()[:16] if os.path.exists(yol) else None


def _istem_ozeti(tok, baslik, eot_on, satir):
    """Vakaların gen girdileri (istem, yasak, satır yasağı): baslangic.py ya da tokenizer değişirse havuz eskir."""
    girdi = [[prompt_idler(tok, kim, yer, tema=vaka_temasi(i, baslik), eot=eot_on), yasak_idler(tok, kim)]
             for i, (kim, yer) in enumerate(test_seti())]
    return hashlib.sha256(json.dumps([girdi, satir]).encode()).hexdigest()[:16]


def aday_havuzu(model_dir, ad, K, temp, rep, tok, baslik="eski", pencere="tum", satir_yasak=False, eot_on=False):
    """Her vaka için K aday (seed 1000·i+j). <model_dir>/adaylar_<ad>.json'a yazılır; aynı ayarlarla (model,
    gen, istemler, temp, rep, bayraklar) üretilmiş bir havuz varsa yalnızca eksik adaylar üretilir.
    Döner: vaka başına aday listesi [{vaka, j, kim, yer, tema, metin, n, lp, bitti}]."""
    yol = os.path.join(model_dir, f"adaylar_{ad}.json")
    ayar_yol = os.path.join(model_dir, f"ayar_adaylar_{ad}.json")
    satir = satir_idleri(tok) if satir_yasak else None
    ayar = {"model": _sha(os.path.join(model_dir, "model.bin")), "gen": _sha(GEN),
            "istem": _istem_ozeti(tok, baslik, eot_on, satir), "temp": temp, "rep": rep, "top_k": 40, "n": 240,
            "baslik": baslik, "pencere": pencere, "satir_yasak": satir_yasak, "eot_on": eot_on}
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
    havuz, yeni = [], 0
    for i, (kim, yer) in enumerate(test_seti()):
        tema = vaka_temasi(i, baslik)
        adaylar = []
        for j in range(K):
            h = eski.get((i, j))
            if h is None or h["kim"] != kim or h["yer"] != yer or h["tema"] != tema:
                _, metin, n, lp, bitti = uret(model_dir, kim, yer, 1000 * i + j, temp, rep, tok, tema=tema,
                                              eot=eot_on, govde=pencere == "govde", satir=satir)
                h = {"vaka": i, "j": j, "kim": kim, "yer": yer, "tema": tema, "metin": metin, "n": n, "lp": lp,
                     "bitti": bitti}
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
    bayraklar(ap)
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    sonuc = []
    if a.aday > 1:
        sys.path.insert(0, HERE)
        from sec import puanla  # noqa: E402
    havuz = aday_havuzu(a.model_dir, a.ad, a.aday, a.temp, a.rep, tok, a.baslik, a.pencere, a.satir_yasak,
                        a.eot_on)
    for i, (kim, yer) in enumerate(test_seti()):
        adaylar = havuz[i]
        h = (max(adaylar, key=lambda x: puanla(x["metin"], kim, x["lp"], x["n"], yer, x["bitti"]))
             if a.aday > 1 else adaylar[0])
        tema = h["tema"]
        sonuc.append({"id": i, "figurler": [KAR[k]["isim"] + " (" + KAR[k]["tur"] + ")" for k in kim],
                      "yer": yer, **({"tema": tema} if tema else {}),
                      "baslik": baslangic(kim, yer, ilk_cumle=False, tema=tema).strip(), "metin": h["metin"],
                      "token": h["n"]})
    os.makedirs(os.path.join(HERE, a.ad), exist_ok=True)
    json.dump(sonuc, open(os.path.join(HERE, a.ad, "hikayeler.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{a.ad}/hikayeler.json")


if __name__ == "__main__":
    main()
