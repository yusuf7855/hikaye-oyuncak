"""KWS eğitimi: (1) float + BN, (2) BN katlama + etkinlik ölçeği kalibrasyonu + QAT (kartın int8 hesabıyla).

  .venv/bin/python ses/kws/egit.py [--adim 8000] [--qat-adim 2000] [--is 2] [--parcacik 2]
Çıktı: ses_kws_veri/calisma/{float.pt, qat.pt, egitim.log}. Yarıda kalırsa --devam ile son kayıttan sürer.
Sonra: degerlendir.py (eşik seçimi + sınama) -> disa_aktar.py (kws_model.h) -> tools/kws_test.py.
"""
import argparse
import math
import os
import sys
import time

import numpy as np
import torch
import torch.nn.functional as F

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
sys.path.insert(0, BURASI)
import ortak as O  # noqa: E402
import veri as V  # noqa: E402

HAM = os.path.join(KOK, "ses_kws_veri", "ham")
CALISMA = os.path.join(KOK, "ses_kws_veri", "calisma")
EGITIM_GRUPLARI = ["poz_egitim", "neg_egitim", "cumle_egitim"]
ISINMA = 25  # ilk 0,5 sn'lik kareler kayba girmez (geçmiş yok)
SINIF_AGIRLIK = torch.tensor([1.0, 1.0] + [2.0] * (O.SINIF_SAYISI - 2))


class Akis(torch.utils.data.IterableDataset):
    def __init__(self, havuz, toplu, tohum, ekler=None):
        self.havuz, self.toplu, self.tohum = havuz, toplu, tohum
        self.ekler = ekler or []

    def __iter__(self):
        wi = torch.utils.data.get_worker_info()
        rng = np.random.default_rng([self.tohum, wi.id if wi else 0, int(time.time() * 1000) % 100000])
        sahne = V.Sahne(self.havuz)
        while True:
            xs, ls = [], []
            for _ in range(self.toplu):
                x, l = sahne.uret(rng)
                while not np.isfinite(x).all():
                    x, l = sahne.uret(rng)
                xs.append(x)
                ls.append(l)
            yield torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ls))


def maske_uygula(f, rng):
    """Hafif SpecAugment: frekans bandı maskesi (öznitelik q*S ölçeğinde, -8 = en düşük)."""
    B = f.shape[0]
    for b in range(B):
        if rng.random() < 0.4:
            w = rng.integers(1, 6)
            a = rng.integers(0, O.NMEL - w)
            f[b, a:a + w] = -8.0
    return f


def kayip(net, on, x, l, rng=None):
    f = on(x)
    if rng is not None:
        f = maske_uygula(f, rng)
    z = net(f)  # (B, C, T)
    l = l.clone()
    l[:, :ISINMA] = V.YOK
    return F.cross_entropy(z, l, weight=SINIF_AGIRLIK, ignore_index=V.YOK), z, l


@torch.no_grad()
def dev_olc(net, on, dev_toplu):
    net.eval()
    dogru = np.zeros(O.SINIF_SAYISI)
    say = np.zeros(O.SINIF_SAYISI)
    top = 0.0
    for x, l in dev_toplu:
        k, z, l2 = kayip(net, on, x, l)
        top += k.item()
        p = z.argmax(1)
        for c in range(O.SINIF_SAYISI):
            m = l2 == c
            say[c] += m.sum().item()
            dogru[c] += (p[m] == c).sum().item()
    net.train()
    return top / len(dev_toplu), dogru / np.maximum(say, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--adim", type=int, default=8000)
    ap.add_argument("--qat-adim", type=int, default=2000)
    ap.add_argument("--toplu", type=int, default=48)
    ap.add_argument("--lr", type=float, default=3e-3)
    ap.add_argument("--is", dest="is_", type=int, default=2, help="sahne üreten işçi süreç")
    ap.add_argument("--parcacik", type=int, default=2, help="torch iş parçacığı")
    ap.add_argument("--devam", action="store_true")
    ap.add_argument("--yalniz-qat", action="store_true", help="float.pt'den QAT aşamasına geç")
    ap.add_argument("--tohum", type=int, default=0)
    ap.add_argument("--baslangic", default=None, help="float ağırlıkları bu kayıttan başlat (tam çizelge yeniden)")
    a = ap.parse_args()
    torch.set_num_threads(a.parcacik)
    torch.manual_seed(a.tohum)
    os.makedirs(CALISMA, exist_ok=True)
    gunluk = open(os.path.join(CALISMA, "egitim.log"), "a", encoding="utf-8")

    def yaz(*s):
        m = " ".join(str(x) for x in s)
        print(m, flush=True)
        gunluk.write(m + "\n")
        gunluk.flush()

    t0 = time.time()
    havuz = V.havuz_yukle(HAM, EGITIM_GRUPLARI, "egitim")
    dev = V.havuz_yukle(HAM, EGITIM_GRUPLARI, "dev")
    yaz(f"havuz ({time.time() - t0:.0f} sn): {V.havuz_ozet(havuz)} | dev: {V.havuz_ozet(dev)}")
    drng = np.random.default_rng(123)
    ds = V.Sahne(dev)
    dev_toplu = []
    for _ in range(8):
        xs, ls = zip(*[ds.uret(drng) for _ in range(32)])
        dev_toplu.append((torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ls))))

    on = O.Oznitelik()
    net = O.KWSNet()
    yaz(f"parametre: {sum(p.numel() for p in net.parameters())}, alıcı alan {O.alici_alan()} kare")
    yukleyici = torch.utils.data.DataLoader(Akis(havuz, a.toplu, a.tohum), batch_size=None, num_workers=a.is_,
                                            persistent_workers=a.is_ > 0, prefetch_factor=4 if a.is_ else None)
    akis = iter(yukleyici)
    rng = np.random.default_rng(a.tohum)
    float_yol = os.path.join(CALISMA, "float.pt")

    # ---------------- aşama 1: float
    bas = 0
    opt = torch.optim.AdamW(net.parameters(), lr=a.lr, weight_decay=1e-3)
    if (a.devam or a.yalniz_qat) and os.path.exists(float_yol):
        k = torch.load(float_yol, map_location="cpu", weights_only=False)
        net.load_state_dict(k["model"])
        if "opt" in k:
            opt.load_state_dict(k["opt"])
        bas = k["adim"]
        yaz(f"float kaydından devam: adım {bas}")
    if a.baslangic:
        net.load_state_dict(torch.load(a.baslangic, map_location="cpu", weights_only=False)["model"])
        yaz(f"başlangıç ağırlıkları: {a.baslangic}")
    if a.yalniz_qat:
        bas = a.adim
    net.train()
    en_iyi = 1e9
    ort = None
    for adim in range(bas, a.adim):
        lr = a.lr * min(1.0, (adim + 1) / 300) * 0.5 * (1 + math.cos(math.pi * adim / a.adim))
        for g in opt.param_groups:
            g["lr"] = lr
        x, l = next(akis)
        k, _, _ = kayip(net, on, x, l, rng)
        opt.zero_grad()
        k.backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(), 5.0)
        opt.step()
        ort = k.item() if ort is None else 0.98 * ort + 0.02 * k.item()
        if (adim + 1) % 100 == 0:
            yaz(f"adım {adim + 1} kayıp {ort:.4f} lr {lr:.2e} ({time.time() - t0:.0f} sn)")
        if (adim + 1) % 1000 == 0 or adim + 1 == a.adim:
            dk, da = dev_olc(net, on, dev_toplu)
            yaz(f"  dev kayıp {dk:.4f} | doğruluk " + " ".join(f"{s}:{v:.3f}" for s, v in zip(V.IF.SINIFLAR, da)))
            torch.save(dict(model=net.state_dict(), opt=opt.state_dict(), adim=adim + 1, dev=dk), float_yol)
            if dk < en_iyi:
                en_iyi = dk
                torch.save(dict(model=net.state_dict(), adim=adim + 1, dev=dk), os.path.join(CALISMA, "float_en_iyi.pt"))

    # ---------------- aşama 2: katla + kalibre + QAT
    k = torch.load(os.path.join(CALISMA, "float_en_iyi.pt") if os.path.exists(os.path.join(CALISMA, "float_en_iyi.pt"))
                   else float_yol, map_location="cpu", weights_only=False)
    net.load_state_dict(k["model"])
    yaz(f"QAT: float adım {k['adim']} (dev {k['dev']:.4f}) ağırlıklarıyla")
    net.eval()
    net.katla()
    net.kalibrasyon(True)
    with torch.no_grad():
        for _ in range(20):
            x, l = next(akis)
            net(on(x))
    net.kalibrasyon(False)
    net.qat_ac(True)
    dk, da = dev_olc(net, on, dev_toplu)
    yaz(f"  QAT öncesi (int8 benzetim) dev kayıp {dk:.4f} | " + " ".join(f"{s}:{v:.3f}" for s, v in zip(V.IF.SINIFLAR, da)))
    net.train()
    opt = torch.optim.AdamW([p for n, p in net.named_parameters()], lr=a.lr * 0.1, weight_decay=0.0)
    for adim in range(a.qat_adim):
        lr = a.lr * 0.1 * 0.5 * (1 + math.cos(math.pi * adim / a.qat_adim))
        for g in opt.param_groups:
            g["lr"] = lr
        x, l = next(akis)
        kk, _, _ = kayip(net, on, x, l, rng)
        opt.zero_grad()
        kk.backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(), 5.0)
        opt.step()
        ort = 0.98 * ort + 0.02 * kk.item() if ort else kk.item()
        if (adim + 1) % 100 == 0:
            yaz(f"qat adım {adim + 1} kayıp {ort:.4f} ({time.time() - t0:.0f} sn)")
    dk, da = dev_olc(net, on, dev_toplu)
    yaz(f"  QAT sonrası dev kayıp {dk:.4f} | " + " ".join(f"{s}:{v:.3f}" for s, v in zip(V.IF.SINIFLAR, da)))
    torch.save(dict(model=net.state_dict(), yapi={}, son_islem=dict(esik_uyan=0.6, esik_komut=0.5, yumusat=4),
                    aciklama=f"float {k['adim']} + QAT {a.qat_adim} adım"), os.path.join(CALISMA, "qat.pt"))
    yaz("kaydedildi:", os.path.join(CALISMA, "qat.pt"))


if __name__ == "__main__":
    main()
