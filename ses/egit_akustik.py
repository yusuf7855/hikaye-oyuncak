"""Akustik modeli (metin -> mel) eğit. Yarıda kesilirse aynı komutla kaldığı yerden devam eder.

  python ses/egit_akustik.py                    # varsayılanlar: ses_veri -> ses_calisma/akustik
Her --ornek-her adımda ses_calisma/akustik/ornek/ altına örnek wav (vocoder varsa onunla, yoksa Griffin-Lim)
ve doğrulama kaybı yazılır. Son --qat-adim adım kartın 4 bitlik ağırlıklarıyla eğitilir.
"""
import argparse
import math
import os
import sys
import time

import numpy as np
import soundfile as sf
import torch
import torch.nn.functional as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kuant import kart_boyutu, kuantize  # noqa: E402
from model import Akustik, ileri_toplam_kaybi, parametre  # noqa: E402
from ortak import KOK, SR, cihaz  # noqa: E402
from sentezle import ORNEK_CUMLELER, seslendir, vocoder_yukle  # noqa: E402
from veri import AkustikVeri, Kumeler, akustik_birlestir, liste, uzunluklar, yukle  # noqa: E402


def istatistik(veri, kimlikler, n=400):
    lf0, en = [], []
    for k in kimlikler[:n]:
        o = yukle(veri, k)
        f = o["f0"].astype(np.float32)
        lf0.append(np.log(f[f > 0]))
        en.append(o["mel"].astype(np.float32).mean(0))
    lf0, en = np.concatenate(lf0), np.concatenate(en)
    return torch.tensor([lf0.mean(), lf0.std(), en.mean(), en.std()], dtype=torch.float32)


def kayiplar(model, toplu, cih, adim, a):
    metin, m_uz, mel, k_uz, f0 = [t.to(cih) for t in toplu]
    o = model(metin, m_uz, mel, k_uz, f0)
    km, mm = o["k_maske"], o["m_maske"]
    l_mel = ((o["mel"] - mel).abs() * km[:, None]).sum() / (km.sum() * mel.shape[1])
    hedef_sure = torch.log1p(o["sure"].float())
    l_sure = (((o["tah"][..., 0] - hedef_sure) ** 2) * mm).sum() / mm.sum()
    pv = o["perde_var"] * mm
    l_perde = (((o["tah"][..., 1] - o["perde"]) ** 2) * pv).sum() / pv.sum().clamp_min(1)
    l_enerji = (((o["tah"][..., 2] - o["enerji"]) ** 2) * mm).sum() / mm.sum()
    l_ctc = ileri_toplam_kaybi(o["logp"], m_uz, k_uz)
    l_bin = -(o["logp"] * o["A"]).sum() / o["A"].sum()
    w_bin = min(1.0, max(0.0, (adim - a.bin_bas) / 4000))
    top = l_mel + 0.1 * (l_sure + l_perde + l_enerji) + l_ctc + w_bin * l_bin
    return top, dict(mel=l_mel.item(), sure=l_sure.item(), perde=l_perde.item(), enerji=l_enerji.item(),
                     ctc=l_ctc.item(), bin=l_bin.item())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--veri", default=os.path.join(KOK, "ses_veri"))
    ap.add_argument("--cikti", default=os.path.join(KOK, "ses_calisma", "akustik"))
    ap.add_argument("--adim", type=int, default=150000)
    ap.add_argument("--toplu", type=int, default=16)
    ap.add_argument("--kare-siniri", type=int, default=8000, help="toplu iş başına en çok mel karesi")
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--isinma", type=int, default=2000)
    ap.add_argument("--bin-bas", type=int, default=5000)
    ap.add_argument("--qat-adim", type=int, default=15000)
    ap.add_argument("--kayit-her", type=int, default=1000)
    ap.add_argument("--ornek-her", type=int, default=5000)
    ap.add_argument("--is", dest="is_", type=int, default=2)
    ap.add_argument("--cihaz", default=None)
    a = ap.parse_args()
    cih = torch.device(a.cihaz) if a.cihaz else cihaz()
    os.makedirs(os.path.join(a.cikti, "ornek"), exist_ok=True)
    son = os.path.join(a.cikti, "son.pt")

    uz = uzunluklar(a.veri)
    egitim = [k for k in liste(a.veri, "egitim") if k in uz]
    dogrulama = [k for k in liste(a.veri, "dogrulama") if k in uz]
    model = Akustik()
    opt = torch.optim.AdamW(model.parameters(), lr=a.lr, betas=(0.9, 0.98), weight_decay=0.01)
    adim = 0
    if os.path.exists(son):
        k = torch.load(son, map_location="cpu", weights_only=False)
        model.load_state_dict(k["model"])
        opt.load_state_dict(k["opt"])
        adim = k["adim"]
        print(f"devam: adım {adim}", flush=True)
    else:
        model.istat.copy_(istatistik(a.veri, egitim))
        print("istatistik (logf0 ort/std, enerji ort/std):", model.istat.tolist(), flush=True)
    model.to(cih)
    for g in opt.state.values():
        for kk, v in g.items():
            if torch.is_tensor(v):
                g[kk] = v.to(cih)
    print(f"cihaz {cih}, eğitim {len(egitim)} / doğrulama {len(dogrulama)} cümle, "
          f"model {parametre(model, ('hiz.',)):.2f} M (+ hizalayıcı), kartta {kart_boyutu(model, 4) / 1e6:.2f} MB",
          flush=True)

    ornekleyici = Kumeler(egitim, uz, a.toplu, a.kare_siniri, tohum=adim)
    yukleyici = torch.utils.data.DataLoader(AkustikVeri(a.veri), batch_sampler=ornekleyici,
                                            collate_fn=akustik_birlestir, num_workers=a.is_,
                                            persistent_workers=a.is_ > 0)
    dog_toplu = [akustik_birlestir([yukle(a.veri, k) for k in dogrulama[i:i + 8]])
                 for i in range(0, min(len(dogrulama), 64), 8)]

    def lr(s):
        if s < a.isinma:
            return a.lr * (s + 1) / a.isinma
        p = min(1.0, (s - a.isinma) / max(1, a.adim - a.isinma))
        return a.lr * (0.05 + 0.95 * 0.5 * (1 + math.cos(math.pi * p)))

    t0, ort = time.time(), {}
    model.train()
    while adim < a.adim:
        for toplu in yukleyici:
            if adim >= a.adim:
                break
            for g in opt.param_groups:
                g["lr"] = lr(adim)
            qat = adim >= a.adim - a.qat_adim
            opt.zero_grad(set_to_none=True)
            if qat:
                with kuantize(model, 4):
                    top, d = kayiplar(model, toplu, cih, adim, a)
                    top.backward()
            else:
                top, d = kayiplar(model, toplu, cih, adim, a)
                top.backward()
            if not torch.isfinite(top):
                print(f"adım {adim}: kayıp sonsuz, atlandı", flush=True)
                opt.zero_grad(set_to_none=True)
                adim += 1
                continue
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            adim += 1
            for kk, v in d.items():
                ort[kk] = ort.get(kk, 0) + v
            if adim % 100 == 0:
                s = " ".join(f"{kk} {v / 100:.4f}" for kk, v in ort.items())
                print(f"adım {adim} | {s} | lr {lr(adim):.2e}{' | QAT' if qat else ''} | "
                      f"{(time.time() - t0) / 100:.2f} s/adım", flush=True)
                ort, t0 = {}, time.time()
            if adim % a.kayit_her == 0 or adim == a.adim:
                torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "adim": adim}, son + ".tmp")
                os.replace(son + ".tmp", son)
            if adim % a.ornek_her == 0 or adim == a.adim:
                ornek_yaz(model, dog_toplu, cih, adim, a)
                t0 = time.time()
    print("bitti", flush=True)


@torch.no_grad()
def ornek_yaz(model, dog_toplu, cih, adim, a):
    model.eval()
    top = 0.0
    for toplu in dog_toplu:
        _, d = kayiplar(model, toplu, cih, adim, a)
        top += d["mel"]
    with kuantize(model, 4):
        topq = sum(kayiplar(model, t, cih, adim, a)[1]["mel"] for t in dog_toplu)
    vo = vocoder_yukle(None, cih)
    for i, c in enumerate(ORNEK_CUMLELER):
        x = seslendir(c, model, vo, kuant=adim >= a.adim - a.qat_adim)
        sf.write(os.path.join(a.cikti, "ornek", f"a{adim:07d}_{i}.wav"), x, SR)
    n = max(1, len(dog_toplu))
    print(f"== adım {adim} doğrulama mel L1 {top / n:.4f} (kartta 4 bit: {topq / n:.4f}); örnekler "
          f"{'vocoder' if vo else 'Griffin-Lim'} ile yazıldı", flush=True)
    model.train()


if __name__ == "__main__":
    main()
