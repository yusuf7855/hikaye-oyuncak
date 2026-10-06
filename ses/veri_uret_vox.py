"""Ses modeli için öğretmen verisi: ürün hikâyelerinin cümlelerini VoxCPM2 ile, seçilen kadın sesiyle seslendirir.

Ses: `ses/referans_ses.mp3` (VoxCPM2'nin metin tarifinden tasarladığı kadın sesi; ürün sahibi dinleyip seçti). Tasarlanan
ses her çalıştırmada değişir; bu yüzden her cümle o kayıt referans alınarak üretilir (ses klonlama): 25 bin cümlede aynı
ses. Gerçek bir kişinin sesi değildir. VoxCPM2 Apache-2.0: ticari kullanım ve çıktıyla model eğitmek serbest. Ambalajda
"ses yapay zekâ ile üretilmiştir" notu yine önerilir.

GPU gerekir (Colab L4). Cümleler veri_uret_st.cumleler ile aynı (ürün hikâyeleri, sabit sıra).

  pip install voxcpm soundfile
  python ses/veri_uret_vox.py --cikti ses_veri --adet 25000
Yazar: <cikti>/metin.tsv, <cikti>/mp3/<kimlik>.mp3 (16 kHz mono); ses/hazirla.py --veri <cikti> ile aynen işlenir.
Yarıda kalırsa aynı komutla devam eder.
"""
import argparse
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from veri_uret_st import KOK, SR, cumleler  # noqa: E402

REFERANS = os.path.join(KOK, "ses", "referans_ses.mp3")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cikti", default=os.path.join(KOK, "ses_veri"))
    ap.add_argument("--adet", type=int, default=25000)
    ap.add_argument("--referans", default=REFERANS)
    ap.add_argument("--referans-metin", default=None,
                    help="referans kaydın tam metni verilirse 'tam klonlama' (daha benzer ses) kullanılır")
    ap.add_argument("--adim", type=int, default=10, help="inference_timesteps")
    ap.add_argument("--cfg", type=float, default=2.0)
    a = ap.parse_args()

    import numpy as np
    import soundfile as sf
    from scipy.signal import resample_poly
    from voxcpm import VoxCPM
    from math import gcd

    os.makedirs(os.path.join(a.cikti, "mp3"), exist_ok=True)
    tsv = os.path.join(a.cikti, "metin.tsv")
    if os.path.exists(tsv):
        secim = [l.rstrip("\n").split("\t", 1) for l in open(tsv, encoding="utf-8")]
    else:
        cs = cumleler()
        random.Random(1).shuffle(cs)
        secim = [(f"s{i:06d}", c) for i, c in enumerate(cs[: a.adet])]
        with open(tsv, "w", encoding="utf-8") as f:
            f.writelines(f"{k}\t{c}\n" for k, c in secim)
        print(f"{len(cs)} tekrarsız cümle; {len(secim)} seçildi -> {tsv}", flush=True)
    kalan = [(k, c) for k, c in secim if not os.path.exists(os.path.join(a.cikti, "mp3", k + ".mp3"))]
    print(f"seslendirilecek: {len(kalan)} / {len(secim)}", flush=True)
    if not kalan:
        return

    model = VoxCPM.from_pretrained("openbmb/VoxCPM2", load_denoiser=False)
    sr = model.tts_model.sample_rate
    g = gcd(SR, sr)
    ek = dict(reference_wav_path=a.referans)
    if a.referans_metin:
        ek.update(prompt_wav_path=a.referans, prompt_text=a.referans_metin)
    for i, (k, c) in enumerate(kalan, 1):
        yol = os.path.join(a.cikti, "mp3", k + ".mp3")
        try:
            wav = model.generate(text=c, cfg_value=a.cfg, inference_timesteps=a.adim,
                                 seed=int(k[1:]) if k[1:].isdigit() else 0, **ek)
            x = np.asarray(wav, dtype=np.float32).ravel()
            if sr != SR:
                x = resample_poly(x, SR // g, sr // g).astype(np.float32)
            x = x / (np.abs(x).max() + 1e-6) * 0.95
            sf.write(yol + ".tmp.mp3", x, SR, format="MP3")
            os.replace(yol + ".tmp.mp3", yol)
        except Exception as e:  # noqa: BLE001
            print("başarısız:", k, e, file=sys.stderr, flush=True)
        if i % 250 == 0:
            print(f"{i} / {len(kalan)}", flush=True)


if __name__ == "__main__":
    main()
