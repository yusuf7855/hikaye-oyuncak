"""Ses modeli: ortak ayarlar, mel hesabı, veri okuma, hizalama (MAS).

Ses 16 kHz mono. Mel: 80 kanal, n_fft 1024, pencere 1024, adım 256 (saniyede 62,5 kare), 0-8000 Hz, log.
Kartta da aynı sayılar kullanılacak (vocoder'ın iSTFT'si aynı n_fft/adımla).
"""
import math
import os

import numpy as np
import torch

SR = 16000
N_FFT = 1024
HOP = 256
WIN = 1024
N_MEL = 80
FMIN, FMAX = 0.0, 8000.0
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cihaz():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def _hz2mel(f):  # Slaney (librosa varsayılanı)
    f = np.asarray(f, dtype=np.float64)
    m = f / (200.0 / 3)
    ust = f >= 1000.0
    m[ust] = 15.0 + np.log(f[ust] / 1000.0) / (np.log(6.4) / 27.0)
    return m


def _mel2hz(m):
    m = np.asarray(m, dtype=np.float64)
    f = m * (200.0 / 3)
    ust = m >= 15.0
    f[ust] = 1000.0 * np.exp((np.log(6.4) / 27.0) * (m[ust] - 15.0))
    return f


def mel_filtre():
    """[N_MEL, N_FFT/2+1] Slaney normalizasyonlu üçgen filtreler (librosa.filters.mel ile aynı)."""
    fft_f = np.linspace(0, SR / 2, N_FFT // 2 + 1)
    mel_f = _mel2hz(np.linspace(_hz2mel(np.array([FMIN]))[0], _hz2mel(np.array([FMAX]))[0], N_MEL + 2))
    fdiff = np.diff(mel_f)
    ramps = mel_f[:, None] - fft_f[None, :]
    w = np.zeros((N_MEL, len(fft_f)))
    for i in range(N_MEL):
        lower = -ramps[i] / fdiff[i]
        upper = ramps[i + 2] / fdiff[i + 1]
        w[i] = np.maximum(0, np.minimum(lower, upper))
    w *= (2.0 / (mel_f[2:N_MEL + 2] - mel_f[:N_MEL]))[:, None]
    return torch.tensor(w, dtype=torch.float32)


def _dft(n_fft):
    n = torch.arange(n_fft, dtype=torch.float64)
    k = torch.arange(n_fft // 2 + 1, dtype=torch.float64)
    a = 2 * math.pi * k[:, None] * n[None] / n_fft
    return torch.cos(a), torch.sin(a)                      # [F, n_fft]


class Stft(torch.nn.Module):
    """torch.stft(center=True, reflect, hann) ile aynı, ama evrişimle: MPS dahil her cihazda çalışır.
    x [B, T] -> (gerçel, sanal) [B, F, kare]."""

    def __init__(self, n_fft=N_FFT, hop=HOP):
        super().__init__()
        self.n_fft, self.hop = n_fft, hop
        c, s = _dft(n_fft)
        w = torch.hann_window(n_fft, dtype=torch.float64)
        self.register_buffer("taban", torch.cat([c * w, -s * w])[:, None].float(), persistent=False)

    def forward(self, x):
        x = torch.nn.functional.pad(x[:, None], (self.n_fft // 2, self.n_fft // 2), mode="reflect")
        y = torch.nn.functional.conv1d(x, self.taban, stride=self.hop)
        f = self.n_fft // 2 + 1
        return y[:, :f], y[:, f:]


class Istft(torch.nn.Module):
    """torch.istft(center=True, hann) ile aynı, evrişimle. (gerçel, sanal) [B, F, kare] -> dalga [B, (kare-1)*HOP]."""

    def __init__(self, n_fft=N_FFT, hop=HOP):
        super().__init__()
        self.n_fft, self.hop = n_fft, hop
        c, s = _dft(n_fft)
        kat = torch.full((n_fft // 2 + 1, 1), 2.0, dtype=torch.float64)
        kat[0] = kat[-1] = 1.0
        w = torch.hann_window(n_fft, dtype=torch.float64)
        self.register_buffer("taban", (torch.cat([c * kat, -s * kat]) / n_fft * w)[:, None].float(),
                             persistent=False)
        self.register_buffer("w2", (w * w)[None, None].float(), persistent=False)

    def forward(self, re, im):
        t = re.shape[-1]
        y = torch.nn.functional.conv_transpose1d(torch.cat([re, im], 1), self.taban, stride=self.hop)
        zarf = torch.nn.functional.conv_transpose1d(torch.ones(1, 1, t, device=re.device), self.w2, stride=self.hop)
        y = y / zarf.clamp_min(1e-8)
        p = self.n_fft // 2
        return y[:, 0, p:-p]


class Mel(torch.nn.Module):
    """Dalga [B, T] -> log-mel [B, N_MEL, kare]. Kare sayısı = T // HOP + 1 (merkezli STFT)."""

    def __init__(self):
        super().__init__()
        self.stft = Stft()
        self.register_buffer("filtre", mel_filtre(), persistent=False)

    def genlik(self, x):
        re, im = self.stft(x)
        return torch.sqrt((re * re + im * im).clamp_min(1e-12))

    def forward(self, x):
        return torch.log(torch.clamp(self.filtre @ self.genlik(x), min=1e-5))


def f0_cikar(x, fmin=70.0, fmax=450.0, esik=0.5):
    """Basit özilinti perde takibi (temiz, tek konuşmacı sentetik ses için yeterli).
    x: float dalga -> f0 [kare] Hz (sessiz/ötümsüz = 0). Kareler Mel ile aynı (merkezli, adım HOP)."""
    xp = np.pad(x, (N_FFT // 2, N_FFT // 2), mode="reflect")
    n = 1 + (len(xp) - N_FFT) // HOP
    idx = np.arange(N_FFT)[None] + HOP * np.arange(n)[:, None]
    fr = xp[idx]
    fr = fr - fr.mean(1, keepdims=True)
    w = np.hanning(N_FFT)
    fw = fr * w
    spek = np.fft.rfft(fw, 2 * N_FFT)
    ac = np.fft.irfft(np.abs(spek) ** 2)[:, :N_FFT]
    wac = np.fft.irfft(np.abs(np.fft.rfft(w, 2 * N_FFT)) ** 2)[:N_FFT]
    ac = ac / np.maximum(wac[None], 1e-9)                      # pencere sönümünü düzelt
    ac = ac / np.maximum(ac[:, :1], 1e-9)
    lmin, lmax = int(SR / fmax), int(SR / fmin)
    ara = ac[:, lmin:lmax]
    enb = ara.max(1)
    # oktav hatasına karşı: en büyüğün %90'ına ulaşan ilk tepe
    iyi = ara >= 0.9 * enb[:, None]
    lag = lmin + iyi.argmax(1)
    # o bölgedeki yerel tepeye kay
    for _ in range(3):
        sag = np.minimum(lag + 1, N_FFT - 1)
        lag = np.where(ac[np.arange(n), sag] > ac[np.arange(n), lag], sag, lag)
    # parabolik ince ayar
    a, b, c = ac[np.arange(n), lag - 1], ac[np.arange(n), lag], ac[np.arange(n), np.minimum(lag + 1, N_FFT - 1)]
    pay = a - 2 * b + c
    kayma = np.where(np.abs(pay) > 1e-9, 0.5 * (a - c) / np.where(np.abs(pay) > 1e-9, pay, 1), 0)
    f0 = SR / (lag + np.clip(kayma, -1, 1))
    enerji = np.sqrt((fr ** 2).mean(1))
    ses = (enb > esik) & (enerji > 0.02 * enerji.max())
    f0 = np.where(ses, f0, 0.0)
    # tek karelik sıçramaları temizle (3'lü medyan, yalnız ötümlü komşular arasında)
    if n >= 3:
        m = np.median(np.stack([np.r_[f0[:1], f0[:-1]], f0, np.r_[f0[1:], f0[-1:]]]), 0)
        f0 = np.where((f0 > 0) & (m > 0), m, f0)
    return f0.astype(np.float32)


def mas(log_p):
    """Tekdüze hizalama arama (Glow-TTS): log_p [metin N, kare T] -> her karenin metin indeksi, süreler [N].

    En yüksek toplam log-olasılıklı, soldan sağa, atlamasız yol. Numpy ile kare üzerinde döngü (T ~ 300)."""
    n, t = log_p.shape
    q = np.full((n, t), -np.inf, dtype=np.float64)
    q[0, 0] = log_p[0, 0]
    for j in range(1, t):
        kal = q[:, j - 1]
        gec = np.concatenate([[-np.inf], q[:-1, j - 1]])
        q[:, j] = np.maximum(kal, gec) + log_p[:, j]
    yol = np.zeros(t, dtype=np.int64)
    i = n - 1
    for j in range(t - 1, -1, -1):
        yol[j] = i
        if j > 0 and i > 0 and (i == j or q[i - 1, j - 1] > q[i, j - 1]):
            i -= 1
    sure = np.bincount(yol, minlength=n)
    return sure


def beta_binom_onsel(n, t, olcek=1.0):
    """Hizalamaya köşegen önseli (RAD-TTS): [t, n] log-olasılık."""
    from scipy.special import betaln, gammaln

    k = np.arange(n)
    out = np.zeros((t, n))
    for j in range(1, t + 1):
        a, b = olcek * j, olcek * (t + 1 - j)
        out[j - 1] = gammaln(n) - gammaln(k + 1) - gammaln(n - k) + betaln(k + a, n - 1 - k + b) - betaln(a, b)
    return out.astype(np.float32)
