"""Kartın hafif seçicisinin (firmware/hikaye_oyuncak/hikaye_oyuncak.ino, SECICI_TAM 0 yolu: puanla_hafif) Python
kopyası: aynı aday havuzundan kartın seçeceği hikâyeyi seçer; hakemler tam seçiciyle (sec.puanla, c2ft_plan_olay2)
karşılaştırabilsin diye.

Kullanım: python degerlendirme/kart_secici.py <adaylar_<ad>.json> <çıktı_adı> [--tokenizer T] [--kiyas <ad>]
  örn.  python degerlendirme/kart_secici.py hf_c2ft_plan/adaylar_c2ft_plan.json kart_sec --kiyas c2ft_plan_olay2
        python degerlendirme/kart_secici.py hf_c2ft_plan/adaylar_c2ft_plan_dog.json kart_sec_dog \\
               --kiyas c2ft_plan_dog_olay2
Kurallar (kartla birebir): puan = 2 × lp; bitmemiş −2; gövde < 60 token −2; her figür için adının token'ı
(ISIM_ID: " Pamuk" gibi tek token, tools/basliklar.py ile aynı) gövdede 2'den az −3, gövdenin son %40'ında
(i ≥ int(n × 0.6f), float32) yok −3; plan bozuk elenir. Eşitlikte ilk aday (kart: p > en_p).
Kartta isim sayımı üretilen token'lar üzerindedir; havuzda token yok, gövde metni tokenizer ile yeniden kodlanır
(kanonik olmayan bölme ya da strip edilen boşluk token'ı: aday'ların ~%8'inde uzunluk ±1-3 farklı; gövde
uzunluğu ve %60 sınırı için havuzdaki n, yani kartın üretilen token sayısı kullanılır). Kartın lp'si EOT token'ının
log-olasılığını da ortalamaya katar, havuzunki katmaz (küçük fark; havuz lp'si kullanılır).
Çıktı: degerlendirme/<çıktı_adı>/hikayeler.json (uret.py ile aynı biçim).
"""
import argparse
import json
import os
import sys

import numpy as np
from tokenizers import Tokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from baslangic import KAR, baslangic  # noqa: E402


def isim_idleri(tok):
    """tools/basliklar.py'deki ISIM_ID: figür kimliği -> ' <isim>' tek token id'si."""
    ids = {}
    for k in KAR:
        e = tok.encode(" " + KAR[k]["isim"]).ids
        assert len(e) == 1, (KAR[k]["isim"], e)
        ids[k] = e[0]
    return ids


def kart_puanla(aday, kimlikler, toklar, isim_id):
    """hikaye_oyuncak.ino puanla_hafif(): toklar = gövde token id'leri."""
    if aday.get("plan_bozuk") or not aday["metin"]:
        return -1e9
    lp = np.float32(aday["lp"])
    p = np.float32(2.0) * lp - np.float32(0.0 if aday["bitti"] else 2.0)
    govde = aday["n"]  # kartta üretilen gövde token sayısı (yeniden kodlanan uzunluk ±1-3 farklı olabilir)
    son = int(np.float32(govde) * np.float32(0.6))
    if govde < 60:
        p -= np.float32(2.0)
    for k in kimlikler:
        say = sum(t == isim_id[k] for t in toklar)
        sonda = sum(t == isim_id[k] for t in toklar[son:])
        if say < 2:
            p -= np.float32(3.0)
        if not sonda:
            p -= np.float32(3.0)
    return float(p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("adaylar")
    ap.add_argument("ad")
    ap.add_argument("--tokenizer", default=None, help="varsayılan: adaylar dosyasının dizinindeki tokenizer.json")
    ap.add_argument("--kiyas", default=None, help="seçimi karşılaştırılacak kol (degerlendirme/<ad>/hikayeler.json)")
    a = ap.parse_args()
    tok = Tokenizer.from_file(a.tokenizer or os.path.join(os.path.dirname(os.path.abspath(a.adaylar)), "tokenizer.json"))
    isim_id = isim_idleri(tok)
    vakalar = {}
    for h in json.load(open(a.adaylar, encoding="utf-8")):
        vakalar.setdefault(h["vaka"], []).append(h)
    sonuc, farkli_n = [], 0
    for i in sorted(vakalar):
        adaylar = sorted(vakalar[i], key=lambda h: h["j"])
        en, en_p = None, -1e30
        for h in adaylar:
            toklar = tok.encode(h["metin"]).ids if h["metin"] else []
            farkli_n += bool(h["metin"]) and len(toklar) != h["n"]
            p = kart_puanla(h, h["kim"], toklar, isim_id)
            if p > en_p:
                en, en_p = h, p
        kim, yer = en["kim"], en["yer"]
        sonuc.append({"id": i, "figurler": [KAR[k]["isim"] + " (" + KAR[k]["tur"] + ")" for k in kim],
                      "yer": yer, **({"tema": en["tema"]} if en["tema"] else {}),
                      "baslik": baslangic(kim, yer, ilk_cumle=False, tema=en["tema"]).strip(), "metin": en["metin"],
                      "token": en["n"], **{k: en[k] for k in ("plan", "plan_bozuk", "hikaye_id") if k in en}})
    os.makedirs(os.path.join(HERE, a.ad), exist_ok=True)
    json.dump(sonuc, open(os.path.join(HERE, a.ad, "hikayeler.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{a.ad}/hikayeler.json "
          f"(yeniden kodlanan uzunluğu n'den farklı aday: {farkli_n})")
    if a.kiyas:
        ref = {h["id"]: h for h in json.load(open(os.path.join(HERE, a.kiyas, "hikayeler.json"), encoding="utf-8"))}
        fark = [h["id"] for h in sonuc if h["metin"].strip() != ref[h["id"]]["metin"].strip()]
        print(f"{a.kiyas} ile farklı seçim: {len(fark)}/{len(sonuc)} vaka {fark}")


if __name__ == "__main__":
    main()
