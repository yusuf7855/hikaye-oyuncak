"""Ses modeli için öğretmen verisi: ürün hikâyelerinin cümlelerini Supertonic 3 kadın sesiyle seslendirir (internetsiz).

Emel (edge-tts) yerine: Microsoft koşulları çıktısıyla model eğitip ürüne koymaya kapalı; Supertonic 3 ağırlıkları
BigScience Open RAIL-M (ticari serbest, çıktı üzerinde hak iddiası yok; docs/SES_ARASTIRMASI.md). Koşullar: ambalajda
"ses yapay zekâ ile üretilmiştir" notu, Supertone/Supertonic markası pazarlamada kullanılmaz, bu veriyle eğitilen ses
modeli türev sayılır: lisanstaki kullanım kısıtları son kullanıcı sözleşmesine taşınmalı.

Cümleler ürün verisinden (data/urun_v2, data/urun_v3): kartta okunacak figür adları ve sözcükler eğitimde geçer.

Kurulum (ayrı ortam, bir kez ~400 MB model indirir): python -m venv st && st/bin/pip install supertonic soundfile
Kullanım:
  st/bin/python ses/veri_uret_st.py --cikti ses_veri_st --adet 25000 [--ses F2] [--is 4]
Yazar: <cikti>/metin.tsv (kimlik<TAB>metin), <cikti>/mp3/<kimlik>.mp3 (16 kHz mono). ses/hazirla.py --veri <cikti>
ile aynen işlenir. Yarıda kalırsa aynı komutla devam eder.
"""
import argparse
import glob
import os
import random
import re
import sys
from multiprocessing import Pool

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = 16000


def cumleler():
    gor, out = set(), []
    for f in sorted(glob.glob(os.path.join(KOK, "data", "urun_v[23]", "*.txt"))):
        if os.path.basename(f) in ("izin.txt", "gecen.txt"):
            continue
        for satir in open(f, encoding="utf-8"):
            satir = satir.strip()
            if not satir or satir.startswith(("###", "@", "#")) or re.match(r"^(Sorun|Çözüm|Karakter|Yer|Yan):", satir):
                continue
            for c in re.split(r'(?:(?<=[.!?])|(?<=[.!?]["”]))\s+(?=["“A-ZÇĞİÖŞÜ])', satir):
                c = c.strip()
                if 12 <= len(c) <= 180 and c not in gor:
                    gor.add(c)
                    out.append(c)
    return out


_tts = _stil = None


def _kur(model_dizini, ses):
    global _tts, _stil
    import onnxruntime as ort
    from supertonic import TTS, config
    # Paket varsayılanı yalnız CPU; ekran kartı varsa (Colab GPU + onnxruntime-gpu) önce onu dene (listeyi yerinde değiştir:
    # yükleyici aynı listeyi kullanır).
    if "CUDAExecutionProvider" in ort.get_available_providers() and "CUDAExecutionProvider" not in config.DEFAULT_ONNX_PROVIDERS:
        config.DEFAULT_ONNX_PROVIDERS.insert(0, "CUDAExecutionProvider")
    kw = dict(auto_download=True, intra_op_num_threads=1, inter_op_num_threads=1)
    if model_dizini:
        kw["model_dir"] = model_dizini
    _tts = TTS(**kw)
    _stil = _tts.get_voice_style(voice_name=ses)


def _seslendir(is_):
    import numpy as np
    import soundfile as sf
    from scipy.signal import resample_poly
    kimlik, metin, yol = is_
    try:
        wav, _ = _tts.synthesize(metin, voice_style=_stil, lang="tr", total_steps=8)
        x = np.asarray(wav, dtype=np.float32).ravel()
        sr = _tts.sample_rate if hasattr(_tts, "sample_rate") else 44100
        if sr != SR:
            from math import gcd
            g = gcd(SR, sr)
            x = resample_poly(x, SR // g, sr // g).astype(np.float32)
        x = x / (np.abs(x).max() + 1e-6) * 0.95
        tmp = yol + ".tmp.mp3"
        sf.write(tmp, x, SR, format="MP3")
        os.replace(tmp, yol)
        return True
    except Exception as e:  # noqa: BLE001
        print("başarısız:", kimlik, e, file=sys.stderr, flush=True)
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cikti", default=os.path.join(KOK, "ses_veri_st"))
    ap.add_argument("--adet", type=int, default=25000)
    ap.add_argument("--ses", default="F2", help="Supertonic sesi: F2 (parlak, genç) ya da F5 (daha pes)")
    ap.add_argument("--model-dizini", default=None)
    ap.add_argument("--is", dest="is_", type=int, default=4)
    a = ap.parse_args()
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
    kalan = [(k, c, os.path.join(a.cikti, "mp3", k + ".mp3")) for k, c in secim
             if not os.path.exists(os.path.join(a.cikti, "mp3", k + ".mp3"))]
    print(f"seslendirilecek: {len(kalan)} / {len(secim)} (ses {a.ses})", flush=True)
    with Pool(a.is_, initializer=_kur, initargs=(a.model_dizini, a.ses)) as p:
        for i, _ in enumerate(p.imap_unordered(_seslendir, kalan, chunksize=8), 1):
            if i % 500 == 0:
                print(f"{i} / {len(kalan)}", flush=True)


if __name__ == "__main__":
    main()
