"""Vocoder'ı (mel -> dalga) GAN ile eğit. Yarıda kesilirse aynı komutla kaldığı yerden devam eder.

1. aşama:  python ses/egit_vocoder.py                       (gerçek mel'den; akustik modelden bağımsız)
2. aşama:  python ses/egit_vocoder.py --gta --adim N        (akustik modelin kendi mel'iyle ince ayar; akustik
           eğitim bittikten sonra. Kartta akustiğin çıktısı gireceği için bulanıklığı/çınlamayı azaltır.)
Örnekler: ses_calisma/vocoder/ornek/ (v*: gerçek mel'den, t*: metinden, akustik model varsa).
"""
import argparse
import os
import sys
import time

import numpy as np
import soundfile as sf
import torch
import torch.nn.functional as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kuant import kart_boyutu, kuantize  # noqa: E402
from model import AyirtEdici, Vocoder, parametre  # noqa: E402
from ortak import HOP, KOK, SR, Mel, cihaz  # noqa: E402
from sentezle import ORNEK_CUMLELER, akustik_yukle, seslendir  # noqa: E402
from veri import Kare, akustik_birlestir, liste, uzunluklar, yukle  # noqa: E402

BOS_MEL = -11.5129


def gta_birlestir(orn):
    dicts = [o for o, _ in orn]
    bas = torch.tensor([b for _, b in orn])
    t = max(len(o["dalga"]) for o in dicts)
    dalga = torch.zeros(len(dicts), t)
    for i, o in enumerate(dicts):
        dalga[i, : len(o["dalga"])] = torch.from_numpy(o["dalga"].astype(np.float32) / 32767)
    return akustik_birlestir(dicts), bas, dalga


def ad_kaybi(gercek, sahte):
    return sum(torch.mean((1 - r) ** 2) + torch.mean(g ** 2) for (r, _), (g, _) in zip(gercek, sahte))


def uretec_kaybi(gercek, sahte):
    adv = sum(torch.mean((1 - g) ** 2) for g, _ in sahte)
    fm = 0.0
    for (_, oz_r), (_, oz_g) in zip(gercek, sahte):
        for r, g in zip(oz_r, oz_g):
            fm = fm + torch.mean(torch.abs(r.detach() - g))
    return adv, fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--veri", default=os.path.join(KOK, "ses_veri"))
    ap.add_argument("--cikti", default=os.path.join(KOK, "ses_calisma", "vocoder"))
    ap.add_argument("--adim", type=int, default=600000)
    ap.add_argument("--toplu", type=int, default=16)
    ap.add_argument("--parca", type=int, default=16384, help="örnek (HOP'un katı)")
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--sadece-mel", type=int, default=5000, help="ilk adımlarda yalnız mel kaybı (hızlı başlangıç)")
    ap.add_argument("--qat-adim", type=int, default=10000)
    ap.add_argument("--gta", action="store_true")
    ap.add_argument("--akustik", default=None)
    ap.add_argument("--baslangic", default=None, help="yeni eğitime bu kayıttaki ağırlıklarla başla (GTA için)")
    ap.add_argument("--kayit-her", type=int, default=1000)
    ap.add_argument("--ornek-her", type=int, default=10000)
    ap.add_argument("--is", dest="is_", type=int, default=2)
    ap.add_argument("--cihaz", default=None)
    a = ap.parse_args()
    assert a.parca % HOP == 0
    cih = torch.device(a.cihaz) if a.cihaz else cihaz()
    os.makedirs(os.path.join(a.cikti, "ornek"), exist_ok=True)
    son = os.path.join(a.cikti, "son.pt")

    kare = a.parca // HOP
    uz = uzunluklar(a.veri)
    egitim = [k for k in liste(a.veri, "egitim") if k in uz and uz[k][0] > kare + 2]
    dogrulama = [k for k in liste(a.veri, "dogrulama") if k in uz][:3]
    G, D = Vocoder(), AyirtEdici()
    opt_g = torch.optim.AdamW(G.parameters(), lr=a.lr, betas=(0.8, 0.99), weight_decay=0.01)
    opt_d = torch.optim.AdamW(D.parameters(), lr=a.lr, betas=(0.8, 0.99), weight_decay=0.01)
    adim = 0
    if os.path.exists(son):
        k = torch.load(son, map_location="cpu", weights_only=False)
        G.load_state_dict(k["model"])
        D.load_state_dict(k["ad"])
        opt_g.load_state_dict(k["opt_g"])
        opt_d.load_state_dict(k["opt_d"])
        adim = k["adim"]
        print(f"devam: adım {adim}", flush=True)
    elif a.baslangic:
        k = torch.load(a.baslangic, map_location="cpu", weights_only=False)
        G.load_state_dict(k["model"])
        D.load_state_dict(k["ad"])
        print(f"başlangıç: {a.baslangic} (adım {k['adim']})", flush=True)
    G.to(cih)
    D.to(cih)
    for opt in (opt_g, opt_d):
        for g in opt.state.values():
            for kk, v in g.items():
                if torch.is_tensor(v):
                    g[kk] = v.to(cih)
    mel_f = Mel().to(cih)
    ak = None
    if a.gta:
        ak = akustik_yukle(a.akustik, cih)
        if ak is None:
            sys.exit("--gta için akustik model gerekli (ses_calisma/akustik/son.pt)")
        for p in ak.parameters():
            p.requires_grad_(False)
    print(f"cihaz {cih}, {len(egitim)} cümle, vocoder {parametre(G):.2f} M (kartta {kart_boyutu(G, 8) / 1e6:.2f} MB), "
          f"ayırt edici {parametre(D):.1f} M{', GTA' if a.gta else ''}", flush=True)

    ds = Kare(a.veri, egitim, a.parca, HOP, gta=a.gta)
    yukleyici = torch.utils.data.DataLoader(ds, batch_size=a.toplu, shuffle=True, num_workers=a.is_,
                                            drop_last=True, persistent_workers=a.is_ > 0,
                                            collate_fn=gta_birlestir if a.gta else None)

    def lr(s):
        return a.lr * (0.999997 ** s)

    t0, ort = time.time(), {}
    while adim < a.adim:
        for toplu in yukleyici:
            if adim >= a.adim:
                break
            if a.gta:
                (metin, m_uz, mel_tam, k_uz, f0), bas, dalga = toplu
                with torch.no_grad():
                    o = ak(metin.to(cih), m_uz.to(cih), mel_tam.to(cih), k_uz.to(cih), f0.to(cih))
                    mt = o["mel"].masked_fill(o["k_maske"][:, None] == 0, BOS_MEL)
                mel = torch.stack([mt[i, :, b: b + kare + 1] for i, b in enumerate(bas.tolist())])
                y = torch.stack([dalga[i, b * HOP: b * HOP + a.parca] for i, b in enumerate(bas.tolist())]).to(cih)
            else:
                y = toplu.to(cih)
                with torch.no_grad():
                    mel = mel_f(y)
            for g in opt_g.param_groups + opt_d.param_groups:
                g["lr"] = lr(adim)
            gan = adim >= a.sadece_mel
            qat = adim >= a.adim - a.qat_adim
            with kuantize(G, 8) if qat else _bos():
                y_g = G(mel)
                if gan:
                    opt_d.zero_grad(set_to_none=True)
                    l_d = ad_kaybi(D(y), D(y_g.detach()))
                    l_d.backward()
                    torch.nn.utils.clip_grad_norm_(D.parameters(), 10.0)
                    opt_d.step()
                opt_g.zero_grad(set_to_none=True)
                l_mel = F.l1_loss(mel_f(y_g), mel_f(y))
                if gan:
                    adv, fm = uretec_kaybi(D(y), D(y_g))
                    l_g = 45 * l_mel + adv + 2 * fm
                else:
                    adv = fm = torch.zeros(())
                    l_g = 45 * l_mel
                l_g.backward()
            if not torch.isfinite(l_g):
                print(f"adım {adim}: kayıp sonsuz, atlandı", flush=True)
                adim += 1
                continue
            torch.nn.utils.clip_grad_norm_(G.parameters(), 10.0)
            opt_g.step()
            adim += 1
            d = dict(mel=l_mel.item(), adv=float(adv.detach()), fm=float(fm.detach()), ad=l_d.item() if gan else 0.0)
            for kk, v in d.items():
                ort[kk] = ort.get(kk, 0) + v
            if adim % 100 == 0:
                s = " ".join(f"{kk} {v / 100:.4f}" for kk, v in ort.items())
                print(f"adım {adim} | {s} | lr {lr(adim):.2e}{' | QAT' if qat else ''} | "
                      f"{(time.time() - t0) / 100:.2f} s/adım", flush=True)
                ort, t0 = {}, time.time()
            if adim % a.kayit_her == 0 or adim == a.adim:
                torch.save({"model": G.state_dict(), "ad": D.state_dict(), "opt_g": opt_g.state_dict(),
                            "opt_d": opt_d.state_dict(), "adim": adim}, son + ".tmp")
                os.replace(son + ".tmp", son)
            if adim % a.ornek_her == 0 or adim == a.adim:
                ornek_yaz(G, a, cih, adim, dogrulama, qat)
                t0 = time.time()
    print("bitti", flush=True)


class _bos:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


@torch.no_grad()
def ornek_yaz(G, a, cih, adim, dogrulama, qat):
    G.eval()
    for i, k in enumerate(dogrulama):
        mel = torch.from_numpy(yukle(a.veri, k)["mel"].astype(np.float32))[None].to(cih)
        with kuantize(G, 8) if qat else _bos():
            x = G(mel)[0].clamp(-1, 1).cpu().numpy()
        sf.write(os.path.join(a.cikti, "ornek", f"v{adim:07d}_{i}.wav"), x, SR)
    ak = akustik_yukle(a.akustik, cih)
    if ak is not None:
        for i, c in enumerate(ORNEK_CUMLELER):
            sf.write(os.path.join(a.cikti, "ornek", f"t{adim:07d}_{i}.wav"), seslendir(c, ak, G, kuant=qat), SR)
    print(f"== adım {adim}: örnekler yazıldı ({a.cikti}/ornek)", flush=True)
    G.train()


if __name__ == "__main__":
    main()
