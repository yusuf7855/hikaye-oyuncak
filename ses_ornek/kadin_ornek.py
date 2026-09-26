"""Kadın sesi örnekleri (Microsoft Emel, çevrimiçi servis; yalnız dinleme amaçlı).

4_kadin_tam.wav: tam cümlelerle doğal okuma (karta sığmaz; karşılaştırma).
5_kadin_hece.wav: aynı sesin heceleri tek tek alınıp birleştirilmiş hâli (karta sığan yöntem).
"""
import asyncio, io, os, re, sys, wave
import numpy as np
import soundfile as sf
import edge_tts

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hece_ornek import METIN, SR, heceler, yeniden_ornekle, kirp, yaz  # noqa: E402

SES = "tr-TR-EmelNeural"


async def sentez(metin, hiz="+0%"):
    veri = b""
    async for p in edge_tts.Communicate(metin, SES, rate=hiz).stream():
        if p["type"] == "audio":
            veri += p["data"]
    x, sr = sf.read(io.BytesIO(veri), dtype="float32")
    if x.ndim > 1:
        x = x.mean(1)
    return yeniden_ornekle(x, sr)


async def main():
    yaz("4_kadin_tam.wav", await sentez(METIN))
    birim, parcalar = {}, []
    for cumle in re.split(r"(?<=[.,!?])\s+", METIN):
        for kelime in re.findall(r"[\wçğıöşüÇĞİÖŞÜ']+", cumle):
            for h in heceler(kelime.replace("'", "")):
                if h not in birim:
                    birim[h] = kirp(await sentez(h, hiz="+60%"), esik=0.03)
                parcalar.append(("h", h))
            parcalar.append(("b", 0.03))
        parcalar.append(("b", 0.28 if cumle.endswith(".") else 0.15))
    cikti, xf = [], int(0.012 * SR)
    for tur, d in parcalar:
        if tur == "b":
            cikti.append(np.zeros(int(d * SR), np.float32)); continue
        u = birim[d].copy()
        if cikti and len(cikti[-1]) > xf and len(u) > xf:
            r = np.linspace(0, 1, xf, dtype=np.float32)
            cikti[-1][-xf:] = cikti[-1][-xf:] * (1 - r) + u[:xf] * r
            u = u[xf:]
        cikti.append(u)
    x = np.concatenate(cikti)
    yaz("5_kadin_hece.wav", x / (np.abs(x).max() + 1e-6) * 0.9)


asyncio.run(main())
