"""Metinden ses: python ses/sentezle.py --metin "Bir varmış bir yokmuş." --cikti deneme.wav

--akustik / --vocoder verilmezse ses_calisma/ altındaki son kayıtlar kullanılır. Vocoder yoksa kaba bir
Griffin-Lim ile dinlenir (yalnız akustik modelin gidişatını görmek için; asıl kalite vocoder'la).
--kuant: kartta olacağı gibi (akustik 4 bit, vocoder 8 bit) yuvarlanmış ağırlıklarla üretir.
"""
import argparse
import os
import sys

import numpy as np
import soundfile as sf
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kuant import kuantize  # noqa: E402
from metin import kodla  # noqa: E402
from model import Akustik, Vocoder  # noqa: E402
from ortak import KOK, SR, Istft, Stft, cihaz, mel_filtre  # noqa: E402

CALISMA = os.path.join(KOK, "ses_calisma")
ORNEK_CUMLELER = [
    "Bir varmış bir yokmuş, ormanın kenarında küçük bir tavşan yaşarmış.",
    "\"Yardım eder misin?\" diye sordu karınca. Tavşan hemen koştu.",
    "Güneş batarken bütün arkadaşlar ağacın altında toplandı ve birlikte güldüler!",
]


def akustik_yukle(yol=None, cih="cpu"):
    yol = yol or os.path.join(CALISMA, "akustik", "son.pt")
    if not os.path.exists(yol):
        return None
    k = torch.load(yol, map_location="cpu", weights_only=False)
    m = Akustik(**k.get("yapi", {}))
    m.load_state_dict(k["model"])
    return m.to(cih).eval()


def vocoder_yukle(yol=None, cih="cpu"):
    yol = yol or os.path.join(CALISMA, "vocoder", "son.pt")
    if not os.path.exists(yol):
        return None
    k = torch.load(yol, map_location="cpu", weights_only=False)
    m = Vocoder(**k.get("yapi", {}))
    m.load_state_dict(k["model"])
    return m.to(cih).eval()


@torch.no_grad()
def griffin_lim(mel, adim=48):
    """log-mel [80, T] -> dalga (kaba)."""
    fb = mel_filtre()
    g = torch.linalg.lstsq(fb.T @ fb + 1e-3 * torch.eye(fb.shape[1]), fb.T @ torch.exp(mel)).solution.clamp_min(0)
    g = g ** 1.2
    stft, istft = Stft(), Istft()
    faz = torch.rand_like(g) * 2 * np.pi
    re, im = g * torch.cos(faz), g * torch.sin(faz)
    for _ in range(adim):
        x = istft(re[None], im[None])
        r, i = stft(x)
        n = torch.sqrt(r * r + i * i).clamp_min(1e-8)
        re, im = g * r[0] / n[0], g * i[0] / n[0]
    x = istft(re[None], im[None])[0]
    return (x / x.abs().max().clamp_min(1e-4) * 0.9).numpy()


@torch.no_grad()
def seslendir(metin, akustik, vocoder=None, hiz=1.0, kuant=False):
    cih = next(akustik.parameters()).device
    ids = torch.tensor([kodla(metin)], device=cih)
    if kuant:
        with kuantize(akustik, 4):
            mel = akustik.uret(ids, hiz=hiz)
    else:
        mel = akustik.uret(ids, hiz=hiz)
    if vocoder is None:
        return griffin_lim(mel[0].float().cpu())
    mel = mel.to(next(vocoder.parameters()).device)
    if kuant:
        with kuantize(vocoder, 8):
            x = vocoder(mel)[0]
    else:
        x = vocoder(mel)[0]
    return x.clamp(-1, 1).float().cpu().numpy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metin", default=None)
    ap.add_argument("--dosya", default=None, help="her satır bir cümle")
    ap.add_argument("--cikti", default="deneme.wav")
    ap.add_argument("--akustik", default=None)
    ap.add_argument("--vocoder", default=None)
    ap.add_argument("--hiz", type=float, default=1.0)
    ap.add_argument("--kuant", action="store_true")
    a = ap.parse_args()
    cih = cihaz()
    ak = akustik_yukle(a.akustik, cih)
    if ak is None:
        sys.exit("akustik model yok (ses_calisma/akustik/son.pt)")
    vo = vocoder_yukle(a.vocoder, cih)
    if a.dosya:
        cumleler = [s.strip() for s in open(a.dosya, encoding="utf-8") if s.strip()]
    else:
        cumleler = [a.metin] if a.metin else ORNEK_CUMLELER
    parcalar = []
    for c in cumleler:
        parcalar += [seslendir(c, ak, vo, a.hiz, a.kuant), np.zeros(int(0.35 * SR), dtype=np.float32)]
    sf.write(a.cikti, np.concatenate(parcalar), SR)
    print(f"yazıldı: {a.cikti}" + ("" if vo else " (vocoder yok: Griffin-Lim, kaba)"))


if __name__ == "__main__":
    main()
