"""Anahtar sözcük (KWS) eğitim/sınama verisini Supertonic 3 ile sentezler ve çocuk sesine benzetir (internetsiz).

Gerçek çocuk kaydı yokken yapay veri:
  * Supertonic 3 sesleri (F1–F5, M1–M5) ve aralarındaki rastgele karışımlar (stil vektörleri harmanlanır).
    Eğitim: F1 F2 F3 F5 M1 M2 M3 M4 (+karışımları); SINAMA yalnız GÖRÜLMEMİŞ F4 ve M5 (+karışımları).
  * Hız 0,75–1,3, noktalama (".", "!", "?", "...") ile tonlama çeşitliliği, yazımla yanlış söyleyiş ("Melhaba").
  * WORLD vokoderiyle çocuk sesi: perde 230–400 Hz'e (+3..+15 yarım ton), formantlar 1,08–1,45 kat yukarı,
    tonlama abartısı, zaman esnetme 0,85–1,35; %8 fısıltı (perdesiz), %8 bağırma (yüksek perde).
Çıktı: <cikti>/<grup>_<parça>.pkl (her biri 100 öğe; FLAC baytları + konuşma başı/sonu). Yarıda kalırsa sürer.

Kullanım (ayrı ortam: /tmp/st_venv; pip install supertonic soundfile scipy pyworld):
  /tmp/st_venv/bin/python ses/kws/sentezle.py --model-dizini <supertonic assets> [--is 2] [--grup poz_egitim ...]
"""
import argparse
import glob
import io
import os
import pickle
import random
import re
import sys
import time
from multiprocessing import Pool

import numpy as np

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
sys.path.insert(0, BURASI)
import ifadeler as IF  # noqa: E402

SR = 16000
EGITIM_SESLERI = ["F1", "F2", "F3", "F5", "M1", "M2", "M3", "M4"]
SINAMA_SESLERI = ["F4", "M5"]
PARCA = 100


# ---------------------------------------------------------------- metinler
def cumleler(surum):
    out, gor = [], set()
    for f in sorted(glob.glob(os.path.join(KOK, "data", surum, "*.txt"))):
        if os.path.basename(f) in ("izin.txt", "gecen.txt"):
            continue
        for satir in open(f, encoding="utf-8"):
            satir = satir.strip()
            if not satir or satir.startswith(("###", "@", "#")) or re.match(r"^(Sorun|Çözüm|Karakter|Yer|Yan):", satir):
                continue
            for c in re.split(r'(?:(?<=[.!?])|(?<=[.!?]["”]))\s+(?=["“A-ZÇĞİÖŞÜ])', satir):
                c = c.strip()
                if 15 <= len(c) <= 120 and c not in gor:
                    gor.add(c)
                    out.append(c)
    return out


def sozcukler(cs):
    yasak = {IF._kucuk(w) for k, v in list(IF.POZITIF.items()) + list(IF.SENTEZ_EK.items())
             for p in v["egitim"] + v["deneme"]
             for w in p.replace(",", "").split()} | {"eko", "merhaba"}
    s = set()
    for c in cs:
        for w in re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîû']+", c):
            w = w.split("'")[0]
            if len(w) >= 3 and IF._kucuk(w) not in yasak:
                s.add(w[0].upper() + w[1:] if w[0].isupper() else w)
    return sorted(s)


def noktala(rng, metin, sinif):
    m = metin.rstrip(".!?")
    r = rng.random()
    if sinif == "UYANDIRMA" or sinif in IF.POZITIF or sinif in IF.SENTEZ_EK:
        son = rng.choice(["", ".", "!", "!", "?", "...", "!!"]) if r < 0.9 else ","
    else:
        son = rng.choice(["", ".", "!", "?"]) if not metin[-1:] in ".!?" else metin[-1]
    if rng.random() < 0.1:
        m = m.lower() if not m.startswith("İ") else m
    return m + son


def isler(grup, seed):
    """[(kimlik, metin, sinif, ses_tanimi, hiz, adim, cocuk_sayisi)] — deterministik."""
    rng = random.Random(seed)
    sinama = grup.endswith("_sinama")
    sesler = SINAMA_SESLERI if sinama else EGITIM_SESLERI
    out = []

    def ses():
        if rng.random() < 0.3:
            return [(rng.choice(sesler), 1.0)]
        k = rng.choice([2, 2, 3]) if len(sesler) > 2 else 2
        sec = rng.sample(sesler, k)
        w = np.random.default_rng(rng.randrange(1 << 30)).dirichlet([0.7] * k)
        return [(s, float(x)) for s, x in zip(sec, w)]

    def ekle(metin, sinif, cocuk, hiz=None):
        out.append((f"{grup}_{len(out):06d}", metin, sinif, ses(),
                    hiz if hiz else round(rng.uniform(0.75, 1.3), 3), rng.choice([3, 4, 5, 6]), cocuk))

    if grup.startswith("poz"):
        for sinif, d in list(IF.POZITIF.items()) + list(IF.SENTEZ_EK.items()):
            liste = d["deneme" if sinama else "egitim"]
            n = (3000 if sinif == "UYANDIRMA" else 1300) if not sinama else (400 if sinif == "UYANDIRMA" else 150)
            for i in range(n):
                ekle(noktala(rng, liste[i % len(liste)], sinif), sinif, 2)
    elif grup.startswith("neg"):
        cs = cumleler("urun_v3" if sinama else "urun_v2")
        sz = sozcukler(cs)
        if sinama:
            egit = set(sozcukler(cumleler("urun_v2")))
            sz = [w for w in sz if w not in egit]
        rng.shuffle(sz)
        tekrar = (4, 2, 300) if sinama else (25, 10, 1500)
        for m in IF.KARISAN * tekrar[0]:
            ekle(noktala(rng, m, "KONUSMA"), "KONUSMA", 1)
        for m in IF.GUNLUK * tekrar[1]:
            ekle(m, "KONUSMA", 1)
        for w in sz[: tekrar[2]]:
            ekle(noktala(rng, w, "KONUSMA"), "KONUSMA", 1)
    elif grup.startswith("cumle"):
        cs = cumleler("urun_v3" if sinama else "urun_v2")
        rng.shuffle(cs)
        for c in cs[: 1000 if sinama else 2500]:
            ekle(c, "KONUSMA", 1 if rng.random() < 0.4 else 0, hiz=round(rng.uniform(0.85, 1.2), 3))
    rng.shuffle(out)
    return out


# ---------------------------------------------------------------- ses işleme
def kirp(x, esik_db=38.0, pay=0.08):
    h = SR // 100
    n = len(x) // h
    if n < 3:
        return x, 0, len(x)
    e = 10 * np.log10(np.mean(x[: n * h].reshape(n, h) ** 2, axis=1) + 1e-10)
    ust = e.max()
    ix = np.where(e > ust - esik_db)[0]
    a, b = ix[0] * h, (ix[-1] + 1) * h
    p = int(pay * SR)
    a0, b0 = max(0, a - p), min(len(x), b + p)
    return x[a0:b0], a - a0, b - a0


def cocuklastir(x, rng):
    """WORLD ile çocuk sesi benzetimi. Döner: (ses, parametreler)."""
    import pyworld as pw
    xd = x.astype(np.float64)
    fp = 5.0
    f0, t = pw.dio(xd, SR, frame_period=fp, f0_floor=60, f0_ceil=600)
    f0 = pw.stonemask(xd, f0, t, SR)
    sp = pw.cheaptrick(xd, f0, t, SR)
    ap = pw.d4c(xd, f0, t, SR)
    v = f0 > 0
    med = float(np.median(f0[v])) if v.any() else 200.0
    kip = rng.random()
    hedef = rng.uniform(230, 400) if kip > 0.08 else rng.uniform(340, 460)  # son durum: bağırma
    oran = float(np.clip(hedef / med, 2 ** (3 / 12), 2 ** (15 / 12)))
    abart = rng.uniform(1.0, 1.5)
    lf = np.log(np.maximum(f0, 1e-3))
    f0n = np.where(v, np.exp(np.log(med * oran) + (lf - np.log(med)) * abart), 0.0)
    erkek = med < 165
    alfa = rng.uniform(1.25, 1.45) if erkek else rng.uniform(1.08, 1.28)
    nb = sp.shape[1]
    kaynak = np.minimum(np.arange(nb) / alfa, nb - 1)
    sp2 = np.empty_like(sp)
    ap2 = np.empty_like(ap)
    for i in range(sp.shape[0]):
        sp2[i] = np.interp(kaynak, np.arange(nb), sp[i])
        ap2[i] = np.interp(kaynak, np.arange(nb), ap[i])
    sp2 = np.maximum(sp2, 1e-16)
    esne = rng.uniform(0.85, 1.35)
    fisilti = kip < 0.08
    if fisilti:
        f0n[:] = 0.0
        ap2[:] = 1.0
    y = pw.synthesize(np.ascontiguousarray(f0n), np.ascontiguousarray(sp2), np.ascontiguousarray(ap2), SR, fp * esne)
    y = y.astype(np.float32)
    y /= np.abs(y).max() + 1e-6
    return y * 0.9, dict(perde=round(med * oran, 1), alfa=round(alfa, 3), esne=round(esne, 3),
                         fisilti=fisilti, bagirma=(0.08 <= kip < 0.16))


def flac(x):
    import soundfile as sf
    b = io.BytesIO()
    sf.write(b, np.clip(x, -1, 1), SR, format="FLAC", subtype="PCM_16")
    return b.getvalue()


_tts = None
_stiller = {}


def _kur(model_dizini):
    global _tts
    from supertonic import TTS
    _tts = TTS(model_dir=model_dizini, auto_download=False, intra_op_num_threads=1, inter_op_num_threads=1)
    for n in EGITIM_SESLERI + SINAMA_SESLERI:
        _stiller[n] = _tts.get_voice_style(n)


def _parca(arg):
    from math import gcd
    from scipy.signal import resample_poly
    from supertonic.core import Style
    yol, isler_ = arg
    out = []
    t0 = time.time()
    for kimlik, metin, sinif, ses, hiz, adim, cocuk in isler_:
        rng = random.Random(kimlik)
        np.random.seed(rng.randrange(1 << 30))
        ttl = sum(w * _stiller[s].ttl for s, w in ses).astype(np.float32)
        dp = sum(w * _stiller[s].dp for s, w in ses).astype(np.float32)
        try:
            wav, dur = _tts.model([metin], Style(ttl, dp), total_step=adim, speed=hiz, lang="tr")
        except Exception as e:  # noqa: BLE001
            print("başarısız:", kimlik, metin, e, file=sys.stderr, flush=True)
            continue
        sr = _tts.sample_rate
        x = wav[0, : int(dur[0] * sr)].astype(np.float32)
        g = gcd(SR, sr)
        x = resample_poly(x, SR // g, sr // g).astype(np.float32)
        x /= np.abs(x).max() + 1e-6
        x, a, b = kirp(x * 0.9)
        varyant = [dict(tur="yetiskin", flac=flac(x), bas=a, son=b)]
        for _ in range(cocuk):
            try:
                y, p = cocuklastir(x, rng)
            except Exception as e:  # noqa: BLE001
                print("world başarısız:", kimlik, e, file=sys.stderr, flush=True)
                continue
            y, a2, b2 = kirp(y)
            varyant.append(dict(tur="cocuk", flac=flac(y), bas=a2, son=b2, **p))
        out.append(dict(kimlik=kimlik, metin=metin, sinif=sinif, ses=ses, hiz=hiz, adim=adim, varyant=varyant))
    tmp = yol + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(out, f)
    os.replace(tmp, yol)
    return yol, len(out), time.time() - t0


GRUPLAR = ["poz_egitim", "neg_egitim", "poz_sinama", "neg_sinama", "cumle_egitim", "cumle_sinama"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cikti", default=os.path.join(KOK, "ses_kws_veri", "ham"))
    ap.add_argument("--model-dizini", required=True)
    ap.add_argument("--is", dest="is_", type=int, default=2)
    ap.add_argument("--grup", nargs="*", default=GRUPLAR)
    a = ap.parse_args()
    os.makedirs(a.cikti, exist_ok=True)
    gorev = []
    for gi, g in enumerate(a.grup):
        js = isler(g, 1000 + GRUPLAR.index(g))
        for k in range(0, len(js), PARCA):
            yol = os.path.join(a.cikti, f"{g}_{k // PARCA:03d}.pkl")
            if not os.path.exists(yol):
                gorev.append((yol, js[k: k + PARCA]))
        print(f"{g}: {len(js)} öğe", flush=True)
    print(f"yapılacak parça: {len(gorev)}", flush=True)
    t0 = time.time()
    with Pool(a.is_, initializer=_kur, initargs=(a.model_dizini,)) as p:
        for i, (yol, n, dt) in enumerate(p.imap(_parca, gorev), 1):
            print(f"[{i}/{len(gorev)}] {os.path.basename(yol)} {n} öğe {dt:.0f} sn (toplam {time.time() - t0:.0f} sn)",
                  flush=True)


if __name__ == "__main__":
    main()
