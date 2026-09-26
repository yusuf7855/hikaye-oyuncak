"""Hazır sesle ses örnekleri: espeak-ng, Piper (bilgisayar kalitesi) ve kartta olabilecek hece birleştirme.

Kullanım: /tmp/ttsenv/bin/python ses_ornek/hece_ornek.py /tmp/tts/tr_TR-dfki-medium.onnx
Çıktı: ses_ornek/1_espeak.wav, 2_piper_tam.wav, 3_hece_birlestirme.wav (16 kHz, kartta çalınacak biçim)
"""
import io, os, re, subprocess, sys, wave
import numpy as np
from piper import PiperVoice
from piper.config import SynthesisConfig

HERE = os.path.dirname(os.path.abspath(__file__))
METIN = ("Ormanın kenarında Alev adında küçük ve sevimli bir ejderha yaşardı. Ateş yerine ağzından rengarenk "
         "baloncuklar üflerdi. Bir gün küçük bir karınca ağır bir yaprağı taşımaya çalışıyordu ama başaramıyordu. "
         "Yardım eder misin, diye sordu karınca. Elbette, yardım ederim, dedi Alev. İkisi birlikte yaprağı "
         "karıncanın yuvasına taşıdılar. Karınca çok mutlu oldu ve Alev'e teşekkür etti.")
SR = 16000
UNLU = set("aeıioöuüâîû")


def heceler(kelime):
    """Türkçe heceleme: her hecede bir ünlü; ünlüler arasındaki ünsüzlerin sonuncusu sonraki heceye geçer."""
    k = kelime.lower()
    ui = [i for i, c in enumerate(k) if c in UNLU]
    if not ui:
        return [k] if k else []
    sinir = [0]
    for a, b in zip(ui, ui[1:]):
        ara = b - a - 1                      # iki ünlü arasındaki ünsüz sayısı
        sinir.append(b if ara == 0 else b - 1)
    sinir.append(len(k))
    return [k[sinir[i]:sinir[i + 1]] for i in range(len(sinir) - 1)]


def yeniden_ornekle(x, sr_in):
    if sr_in == SR:
        return x
    n = int(len(x) * SR / sr_in)
    return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)


def sentezle(ses, metin, hiz=1.0):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        ses.synthesize_wav(metin, w, syn_config=SynthesisConfig(length_scale=hiz))
    buf.seek(0)
    with wave.open(buf) as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    return yeniden_ornekle(x, sr)


def kirp(x, esik=0.02):
    idx = np.where(np.abs(x) > esik)[0]
    if len(idx) == 0:
        return x[:0]
    return x[max(0, idx[0] - 80): idx[-1] + 80]


def yaz(ad, x):
    x = np.clip(x, -1, 1)
    with wave.open(os.path.join(HERE, ad), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())
    print(ad, f"{len(x) / SR:.1f} s")


def main():
    ses = PiperVoice.load(sys.argv[1])
    # 1) espeak-ng
    wav = subprocess.run(["espeak-ng", "-v", "tr", "-s", "150", "--stdout", METIN], capture_output=True).stdout
    with wave.open(io.BytesIO(wav)) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        yaz("1_espeak.wav", yeniden_ornekle(x, w.getframerate()))
    # 2) Piper, tam cümle (bilgisayar/telefon kalitesi; karta sığmaz)
    yaz("2_piper_tam.wav", sentezle(ses, METIN))
    # 3) Hece birleştirme: her hece bir kez sentezlenir (kartta saklanacak birimler), metin bunlardan kurulur
    birim = {}
    parcalar = []
    for cumle in re.split(r"(?<=[.,!?])\s+", METIN):
        for kelime in re.findall(r"[\wçğıöşüÇĞİÖŞÜ']+", cumle):
            for h in heceler(kelime.replace("'", "")):
                if h not in birim:
                    birim[h] = kirp(sentezle(ses, h, hiz=0.55), esik=0.03)  # tek başına hece yavaş söylenir: hızlandır
                parcalar.append(("h", h))
            parcalar.append(("bosluk", 0.03))
        parcalar.append(("bosluk", 0.28 if cumle.endswith(".") else 0.15))
    cikti, xf = [], int(0.012 * SR)            # 12 ms geçişle birleştir
    for tur, d in parcalar:
        if tur == "bosluk":
            cikti.append(np.zeros(int(d * SR), np.float32)); continue
        u = birim[d].copy()
        if cikti and len(cikti[-1]) > xf and len(u) > xf:
            onceki = cikti[-1]
            rampa = np.linspace(0, 1, xf, dtype=np.float32)
            onceki[-xf:] = onceki[-xf:] * (1 - rampa) + u[:xf] * rampa
            u = u[xf:]
        cikti.append(u)
    x = np.concatenate(cikti)
    yaz("3_hece_birlestirme.wav", x / (np.abs(x).max() + 1e-6) * 0.9)
    toplam = sum(len(v) for v in birim.values())
    print(f"{len(birim)} farklı hece, {toplam / SR:.1f} s ses; 4-bit ADPCM ile ~{toplam * 0.5 / 1024:.0f} KB")


if __name__ == "__main__":
    main()
