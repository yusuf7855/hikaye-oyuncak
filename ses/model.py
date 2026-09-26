"""Ses modelleri: metin -> mel (Akustik, FastPitch benzeri) ve mel -> dalga (Vocoder, Vocos benzeri).

Hepsi tek tip blokla kurulu (ConvNeXt: derinlemesine evrişim + LayerNorm + iki doğrusal katman), böylece kartta
tek bir çekirdek yazmak yeter. Dikkat (attention) ve özyineleme yok: çıkarım maliyeti kare başına sabit.

Boyutlar kartın boş flash'ına göre seçildi (LLM'den sonra ~4,4 MB kalıyor):
  Akustik ~2,6 M parametre, kartta 4 bit (32'lik gruplar)  ~1,45 MB
  Vocoder ~2,8 M parametre, kartta 8 bit (satır başına ölçek) ~2,8 MB
Kartta hesap: ~260 M çarpma / saniye ses (gerçek zamandan hızlı).

Kalite için:
- Perde (f0) ve enerji harf başına tahmin edilip modele verilir (tonlama; FastPitch).
- Hizalama dışarıdan gelmez; eğitimde hizalayıcı + MAS ile öğrenilir (RAD-TTS). Hizalayıcı karta gitmez.
- Vocoder GAN ile (çok periyotlu + çok çözünürlüklü ayırt ediciler) eğitilir, sonra akustik modelin kendi
  çıktısıyla ince ayar yapılır (GTA).
"""
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from metin import N_SEMBOL
from ortak import N_FFT, N_MEL, Istft, Stft, beta_binom_onsel, mas


class ConvNeXt(nn.Module):
    """x [B, C, T] -> x + gamma * pw2(gelu(pw1(LN(dw(x))))). maske [B, 1, T] (dolgu 0)."""

    def __init__(self, d, k=7, genis=3, olcek=0.1):
        super().__init__()
        self.dw = nn.Conv1d(d, d, k, padding=k // 2, groups=d)
        self.ln = nn.LayerNorm(d)
        self.pw1 = nn.Linear(d, d * genis)
        self.pw2 = nn.Linear(d * genis, d)
        self.gamma = nn.Parameter(torch.full((d,), olcek))

    def forward(self, x, maske=None):
        if maske is not None:
            x = x * maske
        y = self.dw(x).transpose(1, 2)
        y = self.pw2(F.gelu(self.pw1(self.ln(y))))
        x = x + (self.gamma * y).transpose(1, 2)
        return x * maske if maske is not None else x


def uzunluk_maskesi(uz, t):
    return (torch.arange(t, device=uz.device)[None] < uz[:, None]).float()


def hizalama_matrisi(sure, t):
    """sure [B, N] (kare) -> A [B, T, N], A[b, j, i] = 1 ise j. kare i. harfe ait."""
    bit = torch.cumsum(sure.float(), 1)          # (MPS eski sürümlerde int64 cumsum yok)
    bas = bit - sure
    j = torch.arange(t, device=sure.device)[None, :, None]
    return ((j >= bas[:, None, :]) & (j < bit[:, None, :])).float()


# ---------------------------------------------------------------- hizalayıcı (yalnız eğitimde)
class Hizalayici(nn.Module):
    """RAD-TTS/FastPitch hizalayıcısı: harf gömmeleri ve mel kodlanır, uzaklıktan yumuşak hizalama."""

    def __init__(self, d_metin, d_att=80, sicaklik=0.0005):
        super().__init__()
        self.sicaklik = sicaklik
        self.anahtar = nn.Sequential(nn.Conv1d(d_metin, d_metin * 2, 3, padding=1), nn.ReLU(),
                                     nn.Conv1d(d_metin * 2, d_att, 1))
        self.sorgu = nn.Sequential(nn.Conv1d(N_MEL, N_MEL * 2, 3, padding=1), nn.ReLU(),
                                   nn.Conv1d(N_MEL * 2, N_MEL, 1), nn.ReLU(), nn.Conv1d(N_MEL, d_att, 1))

    def forward(self, gomme, mel, m_maske, log_onsel):
        k = self.anahtar(gomme)                                     # [B, A, N]
        q = self.sorgu(mel)                                         # [B, A, T]
        uzak = (q * q).sum(1)[:, :, None] + (k * k).sum(1)[:, None, :] - 2 * torch.bmm(q.transpose(1, 2), k)
        logp = F.log_softmax(-self.sicaklik * uzak, dim=-1) + log_onsel
        logp = logp.masked_fill(m_maske[:, None, :] == 0, -1e4)
        return F.log_softmax(logp, dim=-1)                          # [B, T, N]


def ileri_toplam_kaybi(logp, metin_uz, mel_uz, bos=-1.0):
    """Tüm tekdüze hizalamaların toplam olasılığı (CTC ile). MPS'te CTC yok: CPU'da."""
    lp_hepsi = logp.float().cpu()
    kayip = 0.0
    for b in range(lp_hepsi.shape[0]):
        n, t = int(metin_uz[b]), int(mel_uz[b])
        lp = F.pad(lp_hepsi[b, :t, :n], (1, 0), value=bos)
        lp = F.log_softmax(lp, dim=-1)
        hedef = torch.arange(1, n + 1)[None]
        kayip = kayip + F.ctc_loss(lp[:, None], hedef, torch.tensor([t]), torch.tensor([n]), zero_infinity=True)
    return (kayip / lp_hepsi.shape[0]).to(logp.device)


def sert_sureler(logp, metin_uz, mel_uz):
    lp = logp.detach().float().cpu().numpy()
    sure = np.zeros((lp.shape[0], lp.shape[2]), dtype=np.int64)
    for b in range(lp.shape[0]):
        n, t = int(metin_uz[b]), int(mel_uz[b])
        sure[b, :n] = mas(lp[b, :t, :n].T)
    return torch.from_numpy(sure).to(logp.device)


def log_onseller(metin_uz, mel_uz, n_max, t_max):
    out = np.zeros((len(metin_uz), t_max, n_max), dtype=np.float32)
    for b, (n, t) in enumerate(zip(metin_uz.tolist(), mel_uz.tolist())):
        out[b, :t, :n] = beta_binom_onsel(n, t)
    return torch.from_numpy(out)


def harf_ortalamasi(deger, gecerli, A):
    """Kare değerlerini [B, T] harf başına ortalar (yalnız geçerli karelerle). -> (ortalama [B, N], var [B, N])."""
    top = torch.bmm((deger * gecerli)[:, None], A)[:, 0]
    say = torch.bmm(gecerli[:, None], A)[:, 0]
    return top / say.clamp_min(1), (say > 0).float()


# ---------------------------------------------------------------- akustik model
class Akustik(nn.Module):
    def __init__(self, d=192, n_kod=4, n_coz=6, d_tah=128, n_tah=3):
        super().__init__()
        self.gomme = nn.Embedding(N_SEMBOL, d, padding_idx=0)
        self.kod = nn.ModuleList([ConvNeXt(d, k=5) for _ in range(n_kod)])
        # ortak tahminci gövdesi: süre (log 1+kare), perde (normalize log f0), enerji (normalize)
        self.tah_giris = nn.Linear(d, d_tah)
        self.tah = nn.ModuleList([ConvNeXt(d_tah, k=3) for _ in range(n_tah)])
        self.tah_ln = nn.LayerNorm(d_tah)
        self.tah_cikis = nn.Linear(d_tah, 3)
        self.perde_gomme = nn.Conv1d(1, d, 3, padding=1)
        self.enerji_gomme = nn.Conv1d(1, d, 3, padding=1)
        self.coz = nn.ModuleList([ConvNeXt(d, k=7) for _ in range(n_coz)])
        self.coz_ln = nn.LayerNorm(d)
        self.cikis = nn.Linear(d, N_MEL)
        self.hiz = Hizalayici(d)
        # veri istatistikleri (eğitim başında hesaplanıp yazılır; karta da gider)
        self.register_buffer("istat", torch.tensor([5.3, 0.2, -5.0, 1.5]))  # logf0 ort/std, enerji ort/std

    def kart_parametreleri(self):
        return {k: v for k, v in self.state_dict().items() if not k.startswith("hiz.")}

    def kodla(self, metin, maske):
        e = self.gomme(metin).transpose(1, 2)
        x = e
        for b in self.kod:
            x = b(x, maske[:, None])
        return x, e

    def tahmin(self, x, maske):
        y = self.tah_giris(x.transpose(1, 2)).transpose(1, 2)
        for b in self.tah:
            y = b(y, maske[:, None])
        return self.tah_cikis(self.tah_ln(y.transpose(1, 2))) * maske[:, :, None]   # [B, N, 3]

    def kosullu(self, x, perde, enerji):
        return x + self.perde_gomme(perde[:, None]) + self.enerji_gomme(enerji[:, None])

    def coz_mel(self, h, maske):
        for b in self.coz:
            h = b(h, maske[:, None])
        return self.cikis(self.coz_ln(h.transpose(1, 2))).transpose(1, 2)   # [B, N_MEL, T]

    def forward(self, metin, metin_uz, mel, mel_uz, f0):
        """Eğitim (öğretmen zorlamalı). f0 [B, T] Hz (0 = ötümsüz)."""
        n, t = metin.shape[1], mel.shape[2]
        m_maske = uzunluk_maskesi(metin_uz, n)
        k_maske = uzunluk_maskesi(mel_uz, t)
        x, e = self.kodla(metin, m_maske)
        log_onsel = log_onseller(metin_uz, mel_uz, n, t).to(mel.device)
        logp = self.hiz(e, mel, m_maske, log_onsel)
        sure = sert_sureler(logp, metin_uz, mel_uz)
        A = hizalama_matrisi(sure, t)                                    # [B, T, N]
        s = self.istat
        ses = (f0 > 0).float() * k_maske
        lf0 = (torch.log(f0.clamp_min(1.0)) - s[0]) / s[1]
        perde, perde_var = harf_ortalamasi(lf0, ses, A)
        en = (mel.mean(1) - s[2]) / s[3]
        enerji, _ = harf_ortalamasi(en, k_maske, A)
        tah = self.tahmin(x, m_maske)
        h = self.kosullu(x, perde, enerji) * m_maske[:, None]
        H = torch.bmm(h, A.transpose(1, 2))                              # [B, C, T]
        mel_t = self.coz_mel(H, k_maske)
        return dict(mel=mel_t, tah=tah, sure=sure, perde=perde, perde_var=perde_var, enerji=enerji,
                    logp=logp, A=A, m_maske=m_maske, k_maske=k_maske)

    @torch.no_grad()
    def uret(self, metin, hiz=1.0, perde_kaydir=0.0, perde_olcek=1.0):
        """metin [1, N] -> mel [1, N_MEL, T]. hiz > 1 yavaş okur. perde_kaydir: yarım ton."""
        m_maske = torch.ones(metin.shape, device=metin.device)
        x, _ = self.kodla(metin, m_maske)
        tah = self.tahmin(x, m_maske)
        sure = torch.clamp(torch.round((torch.exp(tah[..., 0]) - 1) * hiz), min=1).long()
        perde = tah[..., 1] * perde_olcek + perde_kaydir * np.log(2) / 12 / float(self.istat[1])
        h = self.kosullu(x, perde, tah[..., 2])
        t = int(sure.sum())
        H = torch.bmm(h, hizalama_matrisi(sure, t).transpose(1, 2))
        return self.coz_mel(H, torch.ones(1, t, device=metin.device))


# ---------------------------------------------------------------- vocoder (Vocos benzeri)
class Vocoder(nn.Module):
    """mel [B, 80, T] -> dalga [B, (T-1)*HOP]. Kare başına STFT genliği ve fazı tahmin edilir, iSTFT ile dalga."""

    def __init__(self, d=256, n_blok=6, genis=3):
        super().__init__()
        self.giris = nn.Conv1d(N_MEL, d, 7, padding=3)
        self.ln0 = nn.LayerNorm(d)
        self.bloklar = nn.ModuleList([ConvNeXt(d, k=7, genis=genis, olcek=1.0 / n_blok) for _ in range(n_blok)])
        self.ln1 = nn.LayerNorm(d)
        self.cikis = nn.Linear(d, N_FFT + 2)
        self.istft = Istft()

    def kart_parametreleri(self):
        return self.state_dict()

    def forward(self, mel):
        x = self.giris(mel)
        x = self.ln0(x.transpose(1, 2)).transpose(1, 2)
        for b in self.bloklar:
            x = b(x)
        x = self.cikis(self.ln1(x.transpose(1, 2))).transpose(1, 2)   # [B, N_FFT+2, T]
        lg, faz = x.chunk(2, dim=1)
        g = torch.exp(lg.clamp(max=6.0))
        return self.istft(g * torch.cos(faz), g * torch.sin(faz))


# ---------------------------------------------------------------- ayırt ediciler (yalnız vocoder eğitiminde)
wn = nn.utils.parametrizations.weight_norm


class PeriyotAD(nn.Module):
    def __init__(self, p):
        super().__init__()
        self.p = p
        ch = [1, 32, 128, 256, 512, 512]
        self.katman = nn.ModuleList([wn(nn.Conv2d(ch[i], ch[i + 1], (5, 1), (3 if i < 4 else 1, 1), padding=(2, 0)))
                                     for i in range(5)])
        self.son = wn(nn.Conv2d(512, 1, (3, 1), padding=(1, 0)))

    def forward(self, x):
        b, t = x.shape
        if t % self.p:
            x = F.pad(x, (0, self.p - t % self.p), mode="reflect")
        x = x.view(b, 1, -1, self.p)
        oz = []
        for k in self.katman:
            x = F.leaky_relu(k(x), 0.1)
            oz.append(x)
        x = self.son(x)
        oz.append(x)
        return x.flatten(1), oz


class CozunurlukAD(nn.Module):
    def __init__(self, n_fft):
        super().__init__()
        self.stft = Stft(n_fft, n_fft // 4)
        self.katman = nn.ModuleList([
            wn(nn.Conv2d(1, 32, (3, 9), padding=(1, 4))),
            wn(nn.Conv2d(32, 32, (3, 9), stride=(1, 2), padding=(1, 4))),
            wn(nn.Conv2d(32, 32, (3, 9), stride=(1, 2), padding=(1, 4))),
            wn(nn.Conv2d(32, 32, (3, 9), stride=(1, 2), padding=(1, 4))),
            wn(nn.Conv2d(32, 32, (3, 3), padding=(1, 1)))])
        self.son = wn(nn.Conv2d(32, 1, (3, 3), padding=(1, 1)))

    def forward(self, x):
        re, im = self.stft(x)
        x = torch.sqrt((re * re + im * im).clamp_min(1e-9)) ** 0.3       # sıkıştırılmış genlik
        x = x[:, None].transpose(2, 3)                                    # [B, 1, T, F]
        oz = []
        for k in self.katman:
            x = F.leaky_relu(k(x), 0.1)
            oz.append(x)
        x = self.son(x)
        oz.append(x)
        return x.flatten(1), oz


class AyirtEdici(nn.Module):
    def __init__(self):
        super().__init__()
        self.hepsi = nn.ModuleList([PeriyotAD(p) for p in (2, 3, 5, 7, 11)] +
                                   [CozunurlukAD(n) for n in (512, 1024, 2048)])

    def forward(self, x):
        return [d(x) for d in self.hepsi]


def parametre(m, haric=()):
    return sum(p.numel() for k, p in m.named_parameters() if not any(k.startswith(h) for h in haric)) / 1e6
