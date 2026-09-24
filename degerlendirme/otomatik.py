"""Hakemsiz hızlı ölçüm: sabit 36 vakalık test setinde kural cezaları ve uydurma kelime oranı.

Kullanım: python degerlendirme/otomatik.py <model_dizini> [--aday 8] [--temp 0.5] [--rep 1.1]
Her vaka için K aday üretilir (uret.py ile aynı seed'ler), seçici (sec.py) en iyisini alır; ölçümler hem
ilk adaydan (seçicisiz model) hem seçilenden raporlanır. Hakem puanının yerini tutmaz ama sürümleri
birkaç dakikada, aynı ölçüyle karşılaştırır. Çıktı: <model_dizini>/otomatik.json
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tokenizers import Tokenizer  # noqa: E402
from sec import SOZLUK, cezalar, kucuk, puanla, yer_cezasi  # noqa: E402
from uret import test_seti, uret  # noqa: E402


TURLER = ["yeterince yok", "sonda yok", "kendine gönderme", " ve ", "sonradan beliren", "aynı konuşmacı",
          "yanlış isim", "tekrarlanan cümle", "yarım son", "çok kısa", "uydurma kelime", "tekrar eden ifade",
          "yer kayması"]


def olc(hikayeler):
    n = len(hikayeler)
    kelime = bilinmeyen = 0
    temiz = bitti = 0
    ceza_top = 0.0
    turler = {}
    for h in hikayeler:
        c = cezalar(h["metin"], h["kim"], h["n"], bitti=h["bitti"])
        yc = yer_cezasi(h["metin"], h["yer"])
        ceza_top += sum(p for p, _ in c) + yc
        temiz += not c and not yc
        bitti += h["bitti"]
        for _, ad in c + ([(yc, "yer kayması")] if yc else []):
            tur = next((t for t in TURLER if t in ad), ad)
            turler[tur] = turler.get(tur, 0) + 1
        if SOZLUK is not None:
            w = re.findall(r"[a-zçğıöşüâîû]+", kucuk(h["metin"]))
            kelime += len(w)
            bilinmeyen += sum(x not in SOZLUK for x in w)
    return {
        "kurallari_gecen": f"{temiz}/{n}",
        "ort_ceza": round(ceza_top / n, 2),
        "biten": f"{bitti}/{n}",
        "uydurma_kelime_%": round(100 * bilinmeyen / max(1, kelime), 2) if SOZLUK is not None else None,
        "ort_token": round(sum(h["n"] for h in hikayeler) / n, 1),
        "ceza_turleri": dict(sorted(turler.items(), key=lambda x: -x[1])),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("--aday", type=int, default=8)
    ap.add_argument("--temp", type=float, default=0.5)
    ap.add_argument("--rep", type=float, default=1.1)
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    ilk, secilen = [], []
    for i, (kim, yer) in enumerate(test_seti()):
        adaylar = []
        for j in range(a.aday):
            _, metin, n, lp, bitti = uret(a.model_dir, kim, yer, 1000 * i + j, a.temp, a.rep, tok)
            adaylar.append({"kim": kim, "yer": yer, "metin": metin, "n": n, "lp": lp, "bitti": bitti})
        ilk.append(adaylar[0])
        secilen.append(max(adaylar, key=lambda h: puanla(h["metin"], kim, h["lp"], h["n"], yer, h["bitti"])))
    sonuc = {"ayar": vars(a), "seçicisiz": olc(ilk), f"en_iyi_{a.aday}": olc(secilen)}
    json.dump(sonuc, open(os.path.join(a.model_dir, "otomatik.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(sonuc, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
