"""Gerçek çocuk kayıtlarıyla KWS ince ayarı (KAYIT.md'deki düzen). Yapay veri de karışık kalır (unutmasın diye).

  .venv/bin/python ses/kws/ince_ayar.py --kayit kws_kayit/ [--adim 3000] [--sinama-aile A07 A13 A18]
Kayıt düzeni (KAYIT.md):
  kws_kayit/<aile>/<cocuk>/<SINIF>/<herhangi>.wav    SINIF: UYANDIRMA DUR DEVAM BASKA BIR_DAHA SESI_AC SESI_KIS
                                                      KONUSMA (karışan sözcükler, serbest konuşma)
  kws_kayit/<aile>/ARKA/<herhangi>.wav               kartın hoparlöründen hikâye okunurken / evde boş oda (uzun)
Her wav tek bir söyleyiş (ARKA hariç); başta/sonda sessizlik olabilir (enerjiyle kırpılır). 16 kHz değilse çevrilir.
Sınama: --sinama-aile ile verilen aileler (yoksa ailelerin ~%20'si) eğitimde hiç kullanılmaz; sonuçta o
ailelerin kayıtlarıyla uyanma / komut doğruluğu basılır. Çıktı: ses_kws_veri/calisma/ince.pt -> degerlendir.py
--model ... --yaz -> disa_aktar.py --model ... -> tools/kws_test.py --model ...
"""
import argparse
import glob
import math
import os
import sys
import time
import zlib

import numpy as np
import torch

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
sys.path.insert(0, BURASI)
import degerlendir as G  # noqa: E402
import disa_aktar as D  # noqa: E402
import egit as E  # noqa: E402
import ifadeler as IF  # noqa: E402
import ortak as O  # noqa: E402
import veri as V  # noqa: E402

SR = O.SR


def wav_oku(yol):
    import soundfile as sf
    from math import gcd
    from scipy.signal import resample_poly
    x, sr = sf.read(yol, dtype="float32", always_2d=True)
    x = x.mean(axis=1)
    if sr != SR:
        g = gcd(SR, sr)
        x = resample_poly(x, SR // g, sr // g).astype(np.float32)
    return x


def kayitlari_yukle(kok):
    """-> {aile: dict(poz={sinif: [Klip]}, neg=[Klip], arka=[int16])}"""
    sys.path.insert(0, BURASI)
    from sentezle import kirp
    aileler = {}
    for aile in sorted(os.listdir(kok)):
        ad = os.path.join(kok, aile)
        if not os.path.isdir(ad):
            continue
        h = dict(poz={s: [] for s in IF.POZITIF}, neg=[], arka=[], cumle=[])
        for yol in glob.glob(os.path.join(ad, "**", "*.wav"), recursive=True):
            parca = os.path.relpath(yol, ad).split(os.sep)
            sinif = "ARKA" if parca[0] == "ARKA" else (parca[1] if len(parca) >= 3 else None)
            x = wav_oku(yol)
            if sinif == "ARKA":
                h["arka"].append(np.clip(np.round(x * 32767), -32768, 32767).astype(np.int16))
                continue
            if sinif not in IF.POZITIF and sinif != "KONUSMA":
                print("atlandı (sınıf klasörü tanınmadı):", yol)
                continue
            y, a, b = kirp(x / (np.abs(x).max() + 1e-6) * 0.9)
            k = V.Klip(np.round(y * 32767).astype(np.int16), a, b, sinif, os.path.basename(yol), "gercek", "")
            (h["poz"][sinif] if sinif in IF.POZITIF else h["neg"]).append(k)
        aileler[aile] = h
    return aileler


def birlestir(*hs, tekrar=1):
    out = dict(poz={s: [] for s in IF.POZITIF}, neg=[], cumle=[], arka=[])
    for h, t in hs:
        for s in IF.POZITIF:
            out["poz"][s] += h["poz"].get(s, []) * t
        out["neg"] += h.get("neg", []) * t
        out["cumle"] += h.get("cumle", [])
        out["arka"] += h.get("arka", [])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kayit", required=True)
    ap.add_argument("--model", default=os.path.join(E.CALISMA, "qat.pt"))
    ap.add_argument("--cikti", default=os.path.join(E.CALISMA, "ince.pt"))
    ap.add_argument("--adim", type=int, default=3000)
    ap.add_argument("--toplu", type=int, default=48)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--gercek-tekrar", type=int, default=8, help="gerçek klipler havuzda kaç kez yer alsın")
    ap.add_argument("--sinama-aile", nargs="*", default=None)
    ap.add_argument("--is", dest="is_", type=int, default=2)
    a = ap.parse_args()
    torch.set_num_threads(2)
    aileler = kayitlari_yukle(a.kayit)
    if not aileler:
        sys.exit("kayıt bulunamadı: " + a.kayit)
    sinama = a.sinama_aile if a.sinama_aile is not None else [f for f in aileler if zlib.crc32(f.encode()) % 5 == 0]
    egitim = [f for f in aileler if f not in sinama]
    print(f"aileler: eğitim {len(egitim)}, sınama {len(sinama)} ({', '.join(sinama)})")
    gercek = birlestir(*[(aileler[f], 1) for f in egitim])
    yapay = V.havuz_yukle(E.HAM, E.EGITIM_GRUPLARI, "egitim")
    havuz = birlestir((yapay, 1), (gercek, a.gercek_tekrar))
    print("havuz:", V.havuz_ozet(havuz), "| gerçek arka plan:", len(havuz["arka"]))

    net, kayit = D.yukle(a.model)
    net.qat_ac(True)
    on = O.Oznitelik()
    yk = torch.utils.data.DataLoader(E.Akis(havuz, a.toplu, 7), batch_size=None, num_workers=a.is_,
                                     persistent_workers=a.is_ > 0)
    akis = iter(yk)
    rng = np.random.default_rng(7)
    opt = torch.optim.AdamW(net.parameters(), lr=a.lr, weight_decay=0.0)
    net.train()
    t0, ort = time.time(), None
    for adim in range(a.adim):
        for g in opt.param_groups:
            g["lr"] = a.lr * 0.5 * (1 + math.cos(math.pi * adim / a.adim))
        x, l = next(akis)
        k, _, _ = E.kayip(net, on, x, l, rng)
        opt.zero_grad()
        k.backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(), 5.0)
        opt.step()
        ort = k.item() if ort is None else 0.98 * ort + 0.02 * k.item()
        if (adim + 1) % 100 == 0:
            print(f"adım {adim + 1} kayıp {ort:.4f} ({time.time() - t0:.0f} sn)", flush=True)
    kayit["model"] = net.state_dict()
    kayit["aciklama"] = kayit.get("aciklama", "") + f" + gerçek kayıt ince ayarı ({len(egitim)} aile, {a.adim} adım)"
    torch.save(kayit, a.cikti)
    print("kaydedildi:", a.cikti)

    # sınama aileleri: her söyleyiş sessiz oda + hafif gürültüyle akışa konur, kartın son işlemiyle ölçülür
    if sinama:
        tm = O.tamsayi_model(net.eval())
        son = kayit.get("son_islem", dict(esik_uyan=0.6, esik_komut=0.5, yumusat=4))
        si = O.SonIslem(son["esik_uyan"], son["esik_komut"], son["yumusat"])
        h = birlestir(*[(aileler[f], 1) for f in sinama])
        h["cumle"] = yapay["cumle"]
        for kosul in ["sessiz", "hikaye_10"] if any(k.tur != "cocuk" for k in yapay["cumle"]) else ["sessiz"]:
            pcm, dg = G.olumlu_akis(h, kosul, sum(len(v) for v in h["poz"].values()), 900,
                                    [k for k in yapay["cumle"] if k.tur != "cocuk"])
            oz = G.ozet_olumlu(G.olumlu_olc(si.olaylar(G.olasiliklar(tm, pcm)), dg))
            print(f"sınama aileleri, {kosul}: " + ", ".join(f"{k}={v:.3f}" if isinstance(v, float) else f"{k}={v}"
                                                         for k, v in oz.items()))
        if h["neg"]:
            pcm, _ = G.olumsuz_akis(h, "dogal", 901)
            ev = si.olaylar(G.olasiliklar(tm, pcm))
            print(f"sınama aileleri, KONUSMA kayıtları: {sum(1 for _, o in ev if o == 1)} yanlış uyanma "
                  f"({len(pcm) / SR / 60:.1f} dk)")


if __name__ == "__main__":
    main()
