"""SD kart yöntemi: her kelime ayrı ayrı doğal kadın sesiyle kaydedilir, hikâye kelimelerden kurulur.

Her kelimenin iki sürümü saklanır: cümle ortası ("kelime," tonu) ve cümle sonu ("kelime." tonu).
Çıktı: 6_kadin_kelime.wav (16 kHz). Ses: Microsoft Emel (edge-tts).
"""
import asyncio, os, re, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hece_ornek import METIN, SR, kirp, yaz  # noqa: E402
from kadin_ornek import sentez  # noqa: E402


async def main():
    birim, cikti = {}, []
    for cumle in re.split(r"(?<=[.,!?])\s+", METIN):
        kelimeler = re.findall(r"[\wçğıöşüÇĞİÖŞÜ']+", cumle)
        son_nokta = cumle.endswith((".", "!", "?"))
        for i, k in enumerate(kelimeler):
            son = i == len(kelimeler) - 1
            anahtar = (k.lower(), son and son_nokta)
            if anahtar not in birim:
                metin = k + ("." if anahtar[1] else ",")
                birim[anahtar] = kirp(await sentez(metin, hiz="+5%"), esik=0.01)
            cikti.append(birim[anahtar])
            if not son:
                cikti.append(np.zeros(int(0.045 * SR), np.float32))
        cikti.append(np.zeros(int((0.35 if son_nokta else 0.18) * SR), np.float32))
    x = np.concatenate(cikti)
    yaz("6_kadin_kelime.wav", x / (np.abs(x).max() + 1e-6) * 0.9)
    toplam = sum(len(v) for v in birim.values()) / SR
    print(f"{len(birim)} kelime sürümü, {toplam:.1f} s ses; kelime başına ~{toplam / len(birim):.2f} s")


asyncio.run(main())
