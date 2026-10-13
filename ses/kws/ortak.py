"""KWS ortak parçaları: öznitelik (log-mel), model (nedensel genişletilmiş TCN), int8 başvuru çıkarımı, son işlem.

Kartla birebir: firmware/hikaye_oyuncak/kws.h aynı hesabı yapar (tools/kws_test.py karşılaştırır).

Öznitelik: 16 kHz, 512 örnek pencere (32 ms, Hann), 320 örnek adım (20 ms, saniyede 50 kare), 512 FFT güç
spektrumu, 40 mel bandı (100–7800 Hz, HTK), ln(mel + 1e-6), 0..255'e nicemlenip -128 kaydırılır (int8).

Model (akış: her kare için yalnız yeni kare hesaplanır, katman başına (k-1)*d karelik geçmiş tutulur):
  giriş int8 40 -> nedensel conv k3 d1 -> ReLU (C kanal)
  -> 8 artık blok: nedensel conv k3 (genişleme 1,2,4,8,16,32,1,2) -> ReLU, + girişi (artık toplam)
  -> 1x1 conv -> 9 sınıf (logit): ARKA, KONUSMA, UYANDIRMA, DUR, DEVAM, BASKA, BIR_DAHA, SESI_AC, SESI_KIS
  Alıcı alan 1 + 2*(1+1+2+4+8+16+32+1+2) = 135 kare = 2,7 s.

Nicemleme: ağırlıklar int8 (kanal başına simetrik; çıkış katmanı tek ölçek), bias int32, etkinlikler 0..127 (ReLU
sonrası, tensör başına ölçek). Yeniden ölçekleme tamsayı: (acc * m + 2^(s-1)) >> s (int64). Artık toplam:
(h*mh + c*mc + 2^15) >> 16 (int32). Hepsi C ile bit bit aynı.
"""
import math

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

SR = 16000
PENCERE = 512
ADIM = 320
NFFT = 512
NMEL = 40
FMIN, FMAX = 100.0, 7800.0
EPS = 1e-6
LN_ALT = -13.8
LN_ADIM = 0.0935
S_GIRIS = 1.0 / 16.0          # ağ girişi = q * S_GIRIS
KARE_HZ = SR // ADIM          # 50

SINIF_SAYISI = 9
KANAL = 64
GENISLEME = [1, 2, 4, 8, 16, 32, 1, 2]
K = 3


def alici_alan():
    return 1 + (K - 1) * (1 + sum(GENISLEME))


# ------------------------------------------------------------------ öznitelik
def hann():
    n = np.arange(PENCERE)
    return (0.5 - 0.5 * np.cos(2 * np.pi * n / PENCERE)).astype(np.float32)


def _hz2mel(f):
    return 2595.0 * np.log10(1.0 + f / 700.0)


def _mel2hz(m):
    return 700.0 * (10 ** (m / 2595.0) - 1.0)


def mel_matrisi():
    """(NFFT//2+1, NMEL) üçgen süzgeçler (tepe 1)."""
    nb = NFFT // 2 + 1
    fr = np.arange(nb) * SR / NFFT
    m = np.linspace(_hz2mel(FMIN), _hz2mel(FMAX), NMEL + 2)
    hz = _mel2hz(m)
    W = np.zeros((nb, NMEL), np.float32)
    for j in range(NMEL):
        a, b, c = hz[j], hz[j + 1], hz[j + 2]
        sol = (fr - a) / (b - a)
        sag = (c - fr) / (c - b)
        W[:, j] = np.maximum(0, np.minimum(sol, sag))
    return W


_W = mel_matrisi()
_H = hann()


def mel_bantlari():
    """C için seyrek gösterim: her bant için (ilk kutu, ağırlıklar)."""
    out = []
    for j in range(NMEL):
        nz = np.nonzero(_W[:, j])[0]
        out.append((int(nz[0]), _W[nz[0]: nz[-1] + 1, j].astype(np.float32)))
    return out


def oznitelik_np(pcm16):
    """int16 dizisi -> (kare, 40) int8. Akış: kare i, örnek [i*ADIM, i*ADIM+PENCERE). (C ile aynı tanım)"""
    x = np.asarray(pcm16, np.float32) / 32768.0
    n = 0 if len(x) < PENCERE else 1 + (len(x) - PENCERE) // ADIM
    if n == 0:
        return np.zeros((0, NMEL), np.int8)
    idx = np.arange(PENCERE)[None, :] + ADIM * np.arange(n)[:, None]
    fr = x[idx] * _H[None, :]
    X = np.fft.rfft(fr.astype(np.float32), n=NFFT, axis=1)
    P = (X.real.astype(np.float32) ** 2 + X.imag.astype(np.float32) ** 2).astype(np.float32)
    mel = P @ _W
    lm = np.log(mel + np.float32(EPS)).astype(np.float32)
    q = np.floor((lm - np.float32(LN_ALT)) / np.float32(LN_ADIM) + np.float32(0.5))
    return (np.clip(q, 0, 255) - 128).astype(np.int8)


class Oznitelik(nn.Module):
    """Eğitimde toplu öznitelik (torch). Çıkış: (B, 40, T) float = q * S_GIRIS (nicemlenmiş, kartla aynı tanım)."""

    def __init__(self):
        super().__init__()
        self.register_buffer("w", torch.from_numpy(_W))
        self.register_buffer("h", torch.from_numpy(_H))

    def forward(self, x):  # x: (B, N) float, [-1, 1] (int16/32768)
        fr = x.unfold(1, PENCERE, ADIM) * self.h
        X = torch.fft.rfft(fr, n=NFFT)
        P = X.real ** 2 + X.imag ** 2
        lm = torch.log(P @ self.w + EPS)
        q = torch.clamp(torch.floor((lm - LN_ALT) / LN_ADIM + 0.5), 0, 255) - 128
        return q.transpose(1, 2) * S_GIRIS


# ------------------------------------------------------------------ model
def _fq_agirlik(w, kanal_basina=True):
    if kanal_basina:
        s = w.detach().abs().amax(dim=tuple(range(1, w.dim())), keepdim=True).clamp_min(1e-8) / 127.0
    else:
        s = w.detach().abs().max().clamp_min(1e-8) / 127.0
    q = torch.clamp(torch.round(w / s), -127, 127) * s
    return w + (q - w).detach()


class FQ(nn.Module):
    """Etkinlik sahte nicemleme 0..127 (ReLU sonrası). Ölçek kalibrasyonda üstel ortalama ile, sonra sabit."""

    def __init__(self):
        super().__init__()
        self.register_buffer("olcek", torch.tensor(0.0))
        self.acik = False
        self.kalibre = False

    def forward(self, x):
        if self.kalibre:
            m = torch.quantile(x.detach().flatten()[::7].float(), 0.9999) / 127.0
            self.olcek.copy_(m if self.olcek == 0 else 0.9 * self.olcek + 0.1 * m)
        if not self.acik:
            return x
        s = self.olcek
        q = torch.clamp(torch.round(x / s), 0, 127) * s
        return x + (q - x).detach()


class NedenselConv(nn.Module):
    def __init__(self, cin, cout, k, d, bn=True):
        super().__init__()
        self.k, self.d = k, d
        self.conv = nn.Conv1d(cin, cout, k, dilation=d, bias=not bn)
        self.bn = nn.BatchNorm1d(cout) if bn else None
        self.qat = False

    def katla(self):
        """BN'yi conv'a katla (QAT ve dışa aktarım öncesi)."""
        if self.bn is None:
            return
        bn = self.bn
        s = bn.weight / torch.sqrt(bn.running_var + bn.eps)
        w = self.conv.weight * s[:, None, None]
        b = bn.bias - bn.running_mean * s
        conv = nn.Conv1d(self.conv.in_channels, self.conv.out_channels, self.k, dilation=self.d, bias=True)
        conv.weight.data.copy_(w.detach())
        conv.bias.data.copy_(b.detach())
        self.conv = conv
        self.bn = None

    def forward(self, x):
        x = F.pad(x, ((self.k - 1) * self.d, 0))
        w = _fq_agirlik(self.conv.weight) if self.qat else self.conv.weight
        y = F.conv1d(x, w, self.conv.bias, dilation=self.d)
        return self.bn(y) if self.bn is not None else y


class KWSNet(nn.Module):
    def __init__(self, kanal=KANAL, genisleme=GENISLEME, nsinif=SINIF_SAYISI):
        super().__init__()
        self.giris = NedenselConv(NMEL, kanal, K, 1)
        self.fq0 = FQ()
        self.bloklar = nn.ModuleList([NedenselConv(kanal, kanal, K, d) for d in genisleme])
        self.fq_c = nn.ModuleList([FQ() for _ in genisleme])
        self.fq_t = nn.ModuleList([FQ() for _ in genisleme])
        self.cikis = nn.Conv1d(kanal, nsinif, 1)
        self.qat = False

    def katla(self):
        self.giris.katla()
        for b in self.bloklar:
            b.katla()

    def qat_ac(self, acik=True):
        self.qat = acik
        for m in self.modules():
            if isinstance(m, NedenselConv):
                m.qat = acik
            if isinstance(m, FQ):
                m.acik = acik

    def kalibrasyon(self, acik):
        for m in self.modules():
            if isinstance(m, FQ):
                m.kalibre = acik

    def forward(self, x):  # x: (B, 40, T) -> (B, nsinif, T)
        h = self.fq0(F.relu(self.giris(x)))
        for b, fc, ft in zip(self.bloklar, self.fq_c, self.fq_t):
            h = ft(h + fc(F.relu(b(h))))
        w = _fq_agirlik(self.cikis.weight, kanal_basina=False) if self.qat else self.cikis.weight
        return F.conv1d(h, w, self.cikis.bias)


# ------------------------------------------------------------------ tamsayı (int8) dışa aktarım ve başvuru
def _carpan(r):
    """r > 0 gerçek sayıyı m * 2^-s ile yaz (2^30 <= m < 2^31)."""
    if r <= 0:
        return 0, 31
    e = math.floor(math.log2(r))
    s = 30 - e
    m = int(round(r * 2.0 ** s))
    if m >= 2 ** 31:
        m //= 2
        s -= 1
    assert 1 <= s <= 62, (r, s)
    return m, s


@torch.no_grad()
def tamsayi_model(net):
    """Katlanmış + kalibre edilmiş KWSNet -> tamsayı parametreler sözlüğü (C'ye yazılacak olanlar)."""
    def wq(w, kanal_basina=True):
        if kanal_basina:
            s = w.abs().amax(dim=(1, 2)).clamp_min(1e-8) / 127.0
            q = torch.clamp(torch.round(w / s[:, None, None]), -127, 127)
        else:
            s = w.abs().max().clamp_min(1e-8) / 127.0
            q = torch.clamp(torch.round(w / s), -127, 127)
            s = s.expand(w.shape[0])
        return q.to(torch.int8), s.double()

    katmanlar = []
    s_in = S_GIRIS
    convs = [(net.giris, net.fq0.olcek.item(), None)] + [
        (b, fc.olcek.item(), ft.olcek.item()) for b, fc, ft in zip(net.bloklar, net.fq_c, net.fq_t)]
    for conv, s_c, s_t in convs:
        q, sw = wq(conv.conv.weight.double())
        b = torch.round(conv.conv.bias.double() / (sw * s_in)).to(torch.int64)
        mm = [_carpan(float(sw[o] * s_in / s_c)) for o in range(q.shape[0])]
        L = dict(w=q.permute(0, 2, 1).contiguous(),  # (cout, k, cin)
                 b=b.to(torch.int32), m=torch.tensor([a for a, _ in mm], dtype=torch.int64),
                 s=torch.tensor([c for _, c in mm], dtype=torch.int64), d=conv.d, k=conv.k, s_c=s_c)
        if s_t is not None:  # artık toplam: çıkış = (h*mh + c*mc + 2^15) >> 16
            L["mh"] = int(round(s_in / s_t * 65536))
            L["mc"] = int(round(s_c / s_t * 65536))
            L["s_t"] = s_t
            s_in = s_t
        else:
            s_in = s_c
        katmanlar.append(L)
    q, sw = wq(net.cikis.weight.double(), kanal_basina=False)
    b = torch.round(net.cikis.bias.double() / (sw * s_in)).to(torch.int64)
    cikis = dict(w=q[:, :, 0].contiguous(), b=b.to(torch.int32), olcek=float(sw[0] * s_in))
    return dict(katmanlar=katmanlar, cikis=cikis)


def _rq(acc, m, s):
    """(acc * m + 2^(s-1)) >> s, kanal başına (acc: (C, T) int64)."""
    return (acc * m[:, None] + (torch.ones_like(m) << (s - 1))[:, None]) >> s[:, None]


@torch.no_grad()
def tamsayi_ileri(tm, q):
    """Tamsayı başvuru çıkarımı. q: (T, 40) int8 (numpy ya da torch) -> (T, nsinif) int32 logit (acc)."""
    x = torch.as_tensor(np.asarray(q)).to(torch.int64).T.contiguous()  # (40, T)
    h = x
    for L in tm["katmanlar"]:
        w = L["w"].permute(0, 2, 1).double()      # (cout, cin, k)
        hp = F.pad(h.double()[None], ((L["k"] - 1) * L["d"], 0))
        acc = F.conv1d(hp, w, dilation=L["d"])[0].round().to(torch.int64) + L["b"].to(torch.int64)[:, None]
        c = torch.clamp(_rq(acc, L["m"], L["s"]), 0, 127)
        if "mh" in L:
            h = torch.clamp((h * L["mh"] + c * L["mc"] + (1 << 15)) >> 16, 0, 127)
        else:
            h = c
    w = tm["cikis"]["w"].double()
    acc = (w @ h.double()).round().to(torch.int64) + tm["cikis"]["b"].to(torch.int64)[:, None]
    return acc.T.contiguous().to(torch.int32)


# ------------------------------------------------------------------ son işlem (kws.h ile aynı)
class SonIslem:
    """Kare olasılıklarından olaylara. Varsayılanlar kws.h'deki KWS_* sabitleriyle aynı tutulur (disa_aktar yazar)."""

    def __init__(self, esik_uyan=0.6, esik_komut=0.5, yumusat=4, pencere_s=4.0, uyan_bekle_s=1.5,
                 komut_bekle_s=0.6, komut_gecikme_s=0.1, kapali_komut=False):
        self.eu, self.ek, self.n = esik_uyan, esik_komut, yumusat
        self.pencere = int(pencere_s * KARE_HZ)
        self.ub, self.kb, self.kg = int(uyan_bekle_s * KARE_HZ), int(komut_bekle_s * KARE_HZ), int(komut_gecikme_s * KARE_HZ)
        self.kapali_komut = kapali_komut  # True: komutları uyandırmasız da ver (yalnız ölçüm için)

    def olaylar(self, olas):
        """olas: (T, nsinif) olasılık. Döner: [(kare, olay)] olay = 1..7 (KWS_*)."""
        T, C = olas.shape
        out = []
        tampon = np.zeros((self.n, C), np.float64)
        son_uyan = -10 ** 9
        pencere_son = -1
        komut_engel = -1
        for t in range(T):
            tampon[t % self.n] = olas[t]
            if t + 1 < self.n:
                continue
            p = tampon.mean(axis=0)
            if p[2] >= self.eu and t - son_uyan >= self.ub:
                out.append((t, 1))
                son_uyan = t
                pencere_son = t + self.pencere
                komut_engel = t + self.kg
                continue
            if (t <= pencere_son or self.kapali_komut) and t >= komut_engel:
                c = int(np.argmax(p[3:])) + 3
                if p[c] >= self.ek:
                    out.append((t, c - 1))
                    pencere_son = -1
                    komut_engel = t + self.kb
        return out
