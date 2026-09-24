"""Sabit test setinden hikâye üret (hakemlere verilecek).

Kullanım: python degerlendirme/uret.py <model_dizini> <çıktı_adı> [--aday K] [--temp 0.5] [--rep 1.1]
  --aday K: her vaka için K aday üret, seçici (sec.py) ile en iyisini al (cihazdaki önceden-üret+filtrele akışı).
Çıktı: degerlendirme/<çıktı_adı>/hikayeler.json  [{id, figurler, yer, baslik, metin}]
Test seti: 24 tek figür (12 figür × 2 yer) + 12 ikili; seed'ler sabit, sonuçlar tekrarlanabilir.
"""
import argparse, json, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, SIRA, baslangic, prompt_idler, yasak_idler  # noqa: E402

YERLER = ["orman", "deniz", "ev", "park", "sato", "dag"]


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


def uret(model_dir, kimlikler, yer, seed, temp, rep, tok, n=240):
    prompt = baslangic(kimlikler, yer, ilk_cumle=False)
    ids = prompt_idler(tok, kimlikler, yer)
    ban = yasak_idler(tok, kimlikler)
    out = subprocess.run([os.path.join(ROOT, "gen"), os.path.join(model_dir, "model.bin"), str(n), str(temp), "40",
                          str(seed), str(rep), "-b", ",".join(map(str, ban)), "-l", *map(str, ids)],
                         capture_output=True, text=True).stdout.split("\n")
    pairs = [(int(a), float(b)) for a, b in (l.split() for l in out if l.strip())]
    eot = tok.token_to_id("<|endoftext|>")
    toks = [t for t, _ in pairs]
    bitti = eot in toks
    if bitti:
        pairs = pairs[:toks.index(eot)]
    lp = sum(l for _, l in pairs) / max(1, len(pairs))
    return prompt, tok.decode([t for t, _ in pairs]).strip(), len(pairs), lp, bitti


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("ad")
    ap.add_argument("--aday", type=int, default=1)
    ap.add_argument("--temp", type=float, default=0.5)
    ap.add_argument("--rep", type=float, default=1.1)
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    sonuc = []
    if a.aday > 1:
        sys.path.insert(0, HERE)
        from sec import puanla  # noqa: E402
    for i, (kim, yer) in enumerate(test_seti()):
        adaylar = [uret(a.model_dir, kim, yer, 1000 * i + j, a.temp, a.rep, tok) for j in range(a.aday)]
        prompt, metin, n, lp, _ = (max(adaylar, key=lambda x: puanla(x[1], kim, x[3], x[2], yer, x[4]))
                                   if a.aday > 1 else adaylar[0])
        sonuc.append({"id": i, "figurler": [KAR[k]["isim"] + " (" + KAR[k]["tur"] + ")" for k in kim],
                      "yer": yer, "baslik": prompt.strip(), "metin": metin, "token": n})
    os.makedirs(os.path.join(HERE, a.ad), exist_ok=True)
    json.dump(sonuc, open(os.path.join(HERE, a.ad, "hikayeler.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{a.ad}/hikayeler.json")


if __name__ == "__main__":
    main()
