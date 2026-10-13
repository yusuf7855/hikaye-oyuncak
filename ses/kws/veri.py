"""KWS eğitim sahneleri: sentezlenmiş kliplerden (sentezle.py) her adımda yeni, karışık ses + kare etiketleri.

Sahne (4 sn): arka plan (beyaz/pembe/kahverengi gürültü, vantilatör uğultusu, mutfak tıkırtısı, müzik, uzak TV
konuşması) + %50 hoparlörden gelen hikâye sesi (küçük hoparlör benzetimi, SNR -10..25 dB) + ön planda 0–3 olay
(anahtar ifade / "Merhaba Eko" + komut / karışan sözcük / cümle), oda yankısı, mikrofon renklendirmesi, kazanç,
kırpılma, int16'ya yuvarlama.

Kare etiketleri (saniyede 50 kare, kare zamanı = pencerenin SONU):
  anahtar ifade [bas, son]: [bas, son-0.05) yok sayılır (-100), [son-0.05, son+0.30] sınıf, (son+0.30, son+0.60]
  yok sayılır; olumsuz konuşma: [bas, son+0.40] KONUSMA (komut sözcüğüyle başlıyorsa içi yok sayılır);
  geri kalan ARKA. Sonraki olay öncekinin kuyruğunu ezer ("Merhaba Eko" + "dur" -> önce UYANDIRMA, sonra DUR).
"""
import glob
import io
import os
import pickle
import zlib

import numpy as np
from scipy.signal import butter, fftconvolve, resample_poly, sosfilt

import ifadeler as IF
import ortak as O

SR = O.SR
YOK = -100


# ------------------------------------------------------------------ klip havuzu
class Klip:
    __slots__ = ("x", "bas", "son", "sinif", "metin", "tur", "ozel")

    def __init__(self, x, bas, son, sinif, metin, tur, ozel):
        self.x, self.bas, self.son, self.sinif, self.metin, self.tur, self.ozel = x, bas, son, sinif, metin, tur, ozel


def _dev_mi(kimlik, oran=0.05):
    return (zlib.crc32(kimlik.encode()) % 1000) < oran * 1000


def havuz_yukle(dizin, gruplar, bolum=None):
    """bolum: None (hepsi), 'egitim' (dev hariç), 'dev' (yalnız %5 dev)."""
    import soundfile as sf
    poz = {s: [] for s in IF.POZITIF}
    neg, cumle = [], []
    for g in gruplar:
        for yol in sorted(glob.glob(os.path.join(dizin, f"{g}_*.pkl"))):
            with open(yol, "rb") as fh:
                ogeler = pickle.load(fh)
            for o in ogeler:
                if bolum is not None and _dev_mi(o["kimlik"]) != (bolum == "dev"):
                    continue
                if o["sinif"] in IF.SENTEZ_EK and not g.endswith("_sinama") and zlib.crc32(o["kimlik"].encode()) % 10 >= 3:
                    continue  # eski UYKU ifadeleri: olumsuz havuzu boğmasın diye %30'u
                for v in o["varyant"]:
                    x, _ = sf.read(io.BytesIO(v["flac"]), dtype="int16")
                    ozel = "fisilti" if v.get("fisilti") else ("bagirma" if v.get("bagirma") else "")
                    k = Klip(x, v["bas"], v["son"], o["sinif"], o["metin"], v["tur"], ozel)
                    if o["sinif"] in poz:
                        poz[o["sinif"]].append(k)
                    elif g.startswith("cumle"):
                        cumle.append(k)
                    else:
                        neg.append(k)
    return dict(poz=poz, neg=neg, cumle=cumle)


def havuz_ozet(h):
    return ", ".join(f"{s}:{len(v)}" for s, v in h["poz"].items()) + f", neg:{len(h['neg'])}, cumle:{len(h['cumle'])}"


# ------------------------------------------------------------------ sesler ve bozucular
def db(x):
    return 10 ** (x / 20)


def rms(x):
    x = np.asarray(x, np.float64)
    return float(np.sqrt(np.mean(x ** 2) + 1e-12)) if x.size else 0.0


def renkli_gurultu(rng, n, us):
    """us: 0 beyaz, 1 pembe, 2 kahverengi (spektrum 1/f^us)."""
    X = np.fft.rfft(rng.standard_normal(n))
    f = np.maximum(np.arange(len(X)), 1.0)
    y = np.fft.irfft(X / f ** (us / 2), n)
    return (y / (rms(y) + 1e-9)).astype(np.float32)


def _sos(tur, f, sira=2):
    f = np.clip(np.asarray(f, float), 20, SR / 2 - 100)
    return butter(sira, f, btype=tur, fs=SR, output="sos")


def suzgec(x, tur, f, sira=2):
    return sosfilt(_sos(tur, f, sira), x).astype(np.float32)


def vantilator(rng, n):
    t = np.arange(n) / SR
    f0 = rng.choice([50.0, 60.0, rng.uniform(80, 200)])
    hum = sum(rng.uniform(0.1, 1) * np.sin(2 * np.pi * f0 * k * t + rng.uniform(0, 6)) for k in range(1, 6))
    g = suzgec(renkli_gurultu(rng, n, 1), "lowpass", rng.uniform(800, 4000))
    y = g + hum * rng.uniform(0.0, 0.5)
    return (y / rms(y)).astype(np.float32)


def tikirti(rng, n):
    y = np.zeros(n, np.float32)
    for _ in range(rng.integers(2, 12)):
        L = int(rng.uniform(0.01, 0.15) * SR)
        a = rng.integers(0, max(1, n - L))
        e = np.exp(-np.arange(L) / (L * rng.uniform(0.05, 0.4)))
        b = suzgec(rng.standard_normal(L).astype(np.float32), "bandpass",
                   sorted([rng.uniform(300, 2000), rng.uniform(2500, 7500)]))
        y[a:a + L] += b * e * rng.uniform(0.2, 1.0)
    return (y / (rms(y) + 1e-9)).astype(np.float32)


def muzik(rng, n):
    t = np.arange(n) / SR
    y = np.zeros(n, np.float32)
    nota = rng.uniform(0.15, 0.6)
    for s in np.arange(0, n / SR, nota):
        a, b = int(s * SR), int(min(n, (s + nota * rng.uniform(0.6, 1.2)) * SR))
        f = 220 * 2 ** (rng.integers(-12, 18) / 12)
        tt = t[a:b] - t[a]
        zarf = np.exp(-tt * rng.uniform(1, 8))
        y[a:b] += sum(np.sin(2 * np.pi * f * k * tt) / k ** rng.uniform(1, 2) for k in range(1, 5)) * zarf
    return (y / (rms(y) + 1e-9)).astype(np.float32)


def yanki(rng, kisa=False, rt=None):
    if rt is None:
        rt = rng.uniform(0.05, 0.25) if kisa else rng.uniform(0.1, 0.8)
    L = int(min(rt * 1.1, 0.6) * SR) + 1
    t = np.arange(L) / SR
    h = rng.standard_normal(L) * np.exp(-6.9 * t / rt)
    h = suzgec(h.astype(np.float32), "lowpass", rng.uniform(3000, 7500))
    h *= db(-rng.uniform(0, 15) if rt < 0.9 else -rng.uniform(-3, 3)) / (np.sqrt(np.sum(h ** 2)) + 1e-9)
    gecikme = int(rng.uniform(0, 0.004) * SR)
    h = np.concatenate([np.zeros(gecikme, np.float32), h])
    h[0] += 1.0
    return h.astype(np.float32)


def hoparlor(rng, x):
    """Kartın küçük hoparlörü (MAX98357A + ~3 W hoparlör) -> mikrofon: dar bant, hafif doyum, kısa yankı."""
    y = suzgec(x, "highpass", rng.uniform(150, 450))
    y = suzgec(y, "lowpass", rng.uniform(5000, 7800))
    s = rng.uniform(1, 4)
    y = np.tanh(s * y / (np.abs(y).max() + 1e-9)) / s
    y = fftconvolve(y, yanki(rng, kisa=True))[: len(x)]
    return y.astype(np.float32)


def mikrofon(rng, x):
    y = suzgec(x, "highpass", rng.uniform(40, 200))
    if rng.random() < 0.5:
        y = suzgec(y, "lowpass", rng.uniform(5000, 7900))
    if rng.random() < 0.5:  # eğim: tiz ya da pes vurgusu
        a = rng.uniform(-0.6, 0.6)
        y = y + a * suzgec(y, "highpass", rng.uniform(1500, 4000))
    return y.astype(np.float32)


def hiz_boz(rng, x):
    r = rng.uniform(0.88, 1.12)
    return resample_poly(x, 100, int(round(100 * r))).astype(np.float32), r


# ------------------------------------------------------------------ sahne
class Sahne:
    def __init__(self, havuz, sure_s=4.0, p_poz=0.45, p_negatif=0.33, p_uyan_neg=0.07, p_sizinti=0.5):
        self.h = havuz
        self.N = int(sure_s * SR)
        self.T = 1 + (self.N - O.PENCERE) // O.ADIM
        self.p = (p_poz, p_negatif, p_uyan_neg)
        self.p_siz = p_sizinti
        self.siniflar = list(IF.POZITIF)
        nk = len(self.siniflar) - 1
        w = np.array([0.30] + [0.70 / nk] * nk)
        self.sinif_w = w / w.sum()
        self.kare_t = (np.arange(self.T) * O.ADIM + O.PENCERE) / SR

    # -- olay seçimi
    def _poz(self, rng, sinif):
        L = self.h["poz"][sinif]
        k = L[rng.integers(len(L))]
        if k.tur != "cocuk" and rng.random() < 0.5:  # ~%80 çocuk benzetimi, ~%20 yetişkin
            k = L[rng.integers(len(L))]
        return k

    def _neg(self, rng):
        r = rng.random()
        if r < 0.7 or not self.h["cumle"]:
            return self.h["neg"][rng.integers(len(self.h["neg"]))]
        return self.h["cumle"][rng.integers(len(self.h["cumle"]))]

    def _klip_ses(self, rng, k):
        x = k.x.astype(np.float32) / 32768.0
        bas, son = k.bas, k.son
        if rng.random() < 0.3:
            x, r = hiz_boz(rng, x)
            bas, son = int(bas / r), int(son / r)
        g = db(rng.uniform(-42, -12)) / (rms(x[bas:son]) + 1e-9)
        if k.ozel == "fisilti":
            g *= db(-rng.uniform(0, 8))
        if k.ozel == "bagirma" or rng.random() < 0.05:
            g *= db(rng.uniform(4, 12))
        return x * g, bas, min(son, len(x))

    def _arka(self, rng, n):
        y = np.zeros(n, np.float32)
        tur = rng.integers(0, 4)
        g = renkli_gurultu(rng, n, tur) if tur < 3 else vantilator(rng, n)
        y += g * db(rng.uniform(-85, -40))
        if rng.random() < 0.3:
            ek = [tikirti, muzik][rng.integers(2)](rng, n)
            y += ek * db(rng.uniform(-60, -25))
        if rng.random() < 0.12 and self.h["cumle"]:  # uzak TV / başka odadaki konuşma
            y += self._konusma_akisi(rng, n, kisa=False) * db(rng.uniform(-55, -30))
        return y

    def _konusma_akisi(self, rng, n, kisa=True):
        y = np.zeros(n, np.float32)
        t = int(rng.uniform(-2.0, 0.5) * SR)
        while t < n:
            k = self.h["cumle"][rng.integers(len(self.h["cumle"]))]
            x = k.x.astype(np.float32) / 32768.0
            x /= rms(x[k.bas:k.son]) + 1e-9
            a, b = max(t, 0), min(n, t + len(x))
            if b > a:
                y[a:b] += x[a - t: b - t]
            t += len(x) + int(rng.uniform(0.1, 0.7) * SR)
        if not kisa:
            y = fftconvolve(y, yanki(rng))[:n].astype(np.float32)
            y = suzgec(y, "lowpass", rng.uniform(2500, 6000))
        return y / (rms(y) + 1e-9)

    def uret(self, rng):
        N, T = self.N, self.T
        lab = np.zeros(T, np.int64)  # ARKA
        on = np.zeros(N, np.float32)
        olaylar = []  # (bas_s, son_s, sinif_no, komutla_baslar)
        r = rng.random()
        p_poz, p_neg, p_un = self.p
        plan = []
        if r < p_poz:
            s = self.siniflar[rng.choice(len(self.siniflar), p=self.sinif_w)]
            if s != "UYANDIRMA" and rng.random() < 0.4:
                plan = [("UYANDIRMA", rng.uniform(0.05, 1.0)), (s, 0)]
            else:
                plan = [(s, 0)]
            if rng.random() < 0.2:
                plan = [("NEG", rng.uniform(0.3, 1.0))] + plan
        elif r < p_poz + p_neg:
            plan = [("NEG", rng.uniform(0.2, 1.2)) for _ in range(rng.integers(1, 4))]
        elif r < p_poz + p_neg + p_un:
            plan = [("UYANDIRMA", rng.uniform(0.1, 1.0)), ("NEG", 0)]
        # olayları sondan başa yerleştir
        sesler = []
        for ad, ara in plan:
            k = self._neg(rng) if ad == "NEG" else self._poz(rng, ad)
            x, a, b = self._klip_ses(rng, k)
            sesler.append((ad, ara, k, x, a, b))
        if sesler:
            son_t = rng.uniform(1.3, 3.95) if sesler[-1][0] != "NEG" else rng.uniform(0.8, 4.5)
            t_son = int(son_t * SR)
            yer = []
            for i in range(len(sesler) - 1, -1, -1):
                ad, _, k, x, a, b = sesler[i]
                b0 = t_son - b
                yer.append((ad, k, x, a, b, b0))
                if i > 0:
                    t_son = b0 + a - int(sesler[i - 1][1] * SR)
            for ad, k, x, a, b, b0 in reversed(yer):
                i0, i1 = max(0, b0), min(N, b0 + len(x))
                if i1 <= i0:
                    continue
                on[i0:i1] += x[i0 - b0: i1 - b0]
                sn = IF.SINIF_NO[k.sinif] if ad != "NEG" else 1
                olaylar.append(((b0 + a) / SR, (b0 + b) / SR, sn, ad == "NEG" and IF.komutla_baslar(k.metin)))
            if rng.random() < 0.6:
                on = fftconvolve(on, yanki(rng))[:N].astype(np.float32)
        # arka plan ve sızıntı
        arka = self._arka(rng, N)
        y = on + arka
        gercek = self.h.get("arka") or []
        if gercek and rng.random() < 0.5:  # gerçek kayıt: kartın kendi hoparlöründen hikâye / ev sesi (ince_ayar.py)
            g = gercek[rng.integers(len(gercek))]
            a0 = rng.integers(0, max(1, len(g) - N))
            seg = g[a0:a0 + N].astype(np.float32) / 32768.0
            seg = np.pad(seg, (0, N - len(seg)))
            y = y + seg * db(rng.uniform(-6, 6))
        elif rng.random() < self.p_siz and self.h["cumle"]:
            s = hoparlor(rng, self._konusma_akisi(rng, N))
            if olaylar:
                ref = max([rms(on[max(0, int(o[0] * SR)): max(0, int(o[1] * SR)) + 1]) for o in olaylar] + [1e-4])
                s *= ref * db(-rng.uniform(-10, 25))
            else:
                s *= db(rng.uniform(-45, -8))
            y = y + s
        y = mikrofon(rng, y)
        if rng.random() < 0.15:
            y *= db(rng.uniform(-12, 12))
        y += rng.standard_normal(N).astype(np.float32) * db(rng.uniform(-95, -75))
        if rng.random() < 0.08:
            y *= db(rng.uniform(1, 8)) / (np.abs(y).max() + 1e-9)
        y = np.clip(np.round(y * 32767), -32768, 32767) / 32768.0
        # etiketler
        kt = self.kare_t
        for bas, son, sn, ic_yok in olaylar:
            if sn >= 2:
                lab[(kt >= bas) & (kt < son - 0.05)] = YOK
                lab[(kt >= son - 0.05) & (kt <= son + 0.30)] = sn
                lab[(kt > son + 0.30) & (kt <= son + 0.60)] = YOK
            else:
                lab[(kt >= bas) & (kt <= son + 0.40)] = 1
                if ic_yok:
                    lab[(kt >= bas) & (kt < son - 0.05)] = YOK
        return y.astype(np.float32), lab
