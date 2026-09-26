"""mp3 -> 16 kHz dalga + log-mel + sembol dizisi; eğitim/doğrulama listeleri.

Kullanım: python ses/hazirla.py --veri ses_veri [--is 4]
Yazar: ses_veri/hazir/<kimlik>.npz (dalga int16, mel float16 [80, kare], f0 float16 [kare] Hz, metin int16), ses_veri/egitim.txt,
ses_veri/uzunluk.tsv,
ses_veri/dogrulama.txt (kimlikler; doğrulama 100 cümle). Yarıda kalırsa devam eder.
"""
import argparse
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import soundfile as sf
import torch
from scipy.signal import resample_poly

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import HOP, SR, Mel, f0_cikar  # noqa: E402
from metin import kodla  # noqa: E402

_mel = None


def kirp(x, esik_db=-40, pay=0.05):
    """Baştaki ve sondaki sessizliği at (50 ms pay bırak)."""
    pencere = int(0.02 * SR)
    n = len(x) // pencere
    if n < 3:
        return x
    enerji = 20 * np.log10(np.sqrt((x[: n * pencere].reshape(n, pencere) ** 2).mean(1)) + 1e-9)
    tepe = enerji.max()
    ses = np.where(enerji > tepe + esik_db)[0]
    if len(ses) == 0:
        return x
    b = max(0, ses[0] * pencere - int(pay * SR))
    e = min(len(x), (ses[-1] + 1) * pencere + int(pay * SR))
    return x[b:e]


def isle(arg):
    global _mel
    kimlik, metin, veri = arg
    hedef = os.path.join(veri, "hazir", kimlik + ".npz")
    if os.path.exists(hedef):
        try:
            with np.load(hedef) as z:
                if "f0" in z.files:
                    return kimlik, (z["mel"].shape[1], len(z["metin"]))
        except Exception:
            pass
    mp3 = os.path.join(veri, "mp3", kimlik + ".mp3")
    if not os.path.exists(mp3):
        return kimlik, None
    try:
        x, sr = sf.read(mp3, dtype="float32")
    except Exception:
        return kimlik, None
    if x.ndim > 1:
        x = x.mean(1)
    if sr != SR:
        from math import gcd
        g = gcd(SR, sr)
        x = resample_poly(x, SR // g, sr // g).astype(np.float32)
    x = kirp(x)
    x = x / (np.abs(x).max() + 1e-6) * 0.95
    x = x[: len(x) // HOP * HOP]
    if _mel is None:
        torch.set_num_threads(1)
        _mel = Mel()
    with torch.no_grad():
        m = _mel(torch.from_numpy(x)[None])[0].numpy()
    f0 = f0_cikar(x)
    ids = np.array(kodla(metin), dtype=np.int16)
    if len(ids) == 0 or m.shape[1] < len(ids) + 2:  # hizalama için kare >= sembol olmalı
        return kimlik, None
    tmp = hedef + ".tmp.npz"
    np.savez(tmp, dalga=(x * 32767).astype(np.int16), mel=m.astype(np.float16), f0=f0.astype(np.float16),
             metin=ids)
    os.replace(tmp, hedef)
    return kimlik, (m.shape[1], len(ids))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--veri", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                   "ses_veri"))
    ap.add_argument("--is", dest="is_", type=int, default=4)
    a = ap.parse_args()
    os.makedirs(os.path.join(a.veri, "hazir"), exist_ok=True)
    satirlar = [l.rstrip("\n").split("\t", 1) for l in open(os.path.join(a.veri, "metin.tsv"), encoding="utf-8")]
    isler = [(k, m, a.veri) for k, m in satirlar]
    iyi, uz = [], []
    with ProcessPoolExecutor(a.is_) as ex:
        for i, (k, ok) in enumerate(ex.map(isle, isler, chunksize=32)):
            if ok:
                iyi.append(k)
                uz.append(f"{k}\t{ok[0]}\t{ok[1]}")
            if (i + 1) % 1000 == 0:
                print(f"{i + 1} / {len(isler)}", flush=True)
    open(os.path.join(a.veri, "uzunluk.tsv"), "w").write("\n".join(uz) + "\n")   # kimlik, kare, sembol
    dog = set(iyi[:100])
    open(os.path.join(a.veri, "dogrulama.txt"), "w").write("\n".join(k for k in iyi if k in dog) + "\n")
    open(os.path.join(a.veri, "egitim.txt"), "w").write("\n".join(k for k in iyi if k not in dog) + "\n")
    print(f"hazır: {len(iyi)} / {len(isler)} (eğitim {len(iyi) - len(dog)}, doğrulama {len(dog)})")


if __name__ == "__main__":
    main()
