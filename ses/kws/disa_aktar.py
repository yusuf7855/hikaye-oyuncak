"""Eğitilmiş KWS modelini kartın başlığına yazar: firmware/hikaye_oyuncak/generated/kws_model.h

  .venv/bin/python ses/kws/disa_aktar.py --model ses_kws_veri/calisma/qat.pt [--cikti ...]
  .venv/bin/python ses/kws/disa_aktar.py --rastgele      # eğitilmemiş yer tutucu (yalnız derleme denemesi için)

Kayıt (qat.pt) BN'si katlanmış ve etkinlik ölçekleri kalibre edilmiş KWSNet'tir (egit.py yazar); son işlem
eşikleri de kayıttadır (degerlendir.py seçer). Ayrıca <cikti dizini>/../tools için gerek yok: kws_test.py aynı
tamsayı modelini ortak.tamsayi_model ile kendisi kurar.
"""
import argparse
import os
import sys

import numpy as np
import torch

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(os.path.dirname(BURASI))
sys.path.insert(0, BURASI)
import ortak as O  # noqa: E402

VARSAYILAN = os.path.join(KOK, "firmware", "hikaye_oyuncak", "generated", "kws_model.h")


def _dizi(ad, tur, v, satir=24):
    v = np.asarray(v).ravel()
    if tur == "float":
        el = [repr(float(np.float32(x))) + "f" for x in v]
    else:
        el = [str(int(x)) for x in v]
    govde = ",\n".join("  " + ", ".join(el[i: i + satir]) for i in range(0, len(el), satir))
    return f"static const {tur} {ad}[{len(v)}] = {{\n{govde}\n}};\n"


def yukle(yol):
    k = torch.load(yol, map_location="cpu", weights_only=False)
    net = O.KWSNet(**k.get("yapi", {}))
    net.katla()
    net.load_state_dict(k["model"])
    return net, k


def baslik_yaz(net, son, cikti, aciklama=""):
    tm = O.tamsayi_model(net)
    L = tm["katmanlar"]
    C = net.giris.conv.out_channels
    nb = len(net.bloklar)
    gen = [b.d for b in net.bloklar]
    bant = O.mel_bantlari()
    ofs, w = [], []
    for bas, ww in bant:
        ofs.append(len(w))
        w.extend(ww.tolist())
    gecmis = sum((O.K - 1) * d + 1 for d in gen) * C
    agirlik = sum(l["w"].numel() for l in L) + tm["cikis"]["w"].numel()
    bayt = agirlik + 4 * (sum(l["b"].numel() * 2 for l in L) + tm["cikis"]["b"].numel()) + nb + 4 * len(w)
    s = []
    s.append("// Otomatik üretildi: ses/kws/disa_aktar.py. ELLE DEĞİŞTİRMEYİN.\n")
    s.append(f"// {aciklama}\n")
    s.append(f"// Ağırlık: {agirlik} int8 (~{bayt / 1024:.1f} KB toplam flash). Geçmiş tamponu: {gecmis} bayt.\n")
    s.append("#pragma once\n#include <stdint.h>\n\n")
    d = dict(KWS_SURUM=1, KWS_NMEL=O.NMEL, KWS_KANAL=C, KWS_NBLOK=nb, KWS_K=O.K, KWS_NSINIF=net.cikis.out_channels,
             KWS_PENCERE=O.PENCERE, KWS_ADIM=O.ADIM, KWS_NFFT=O.NFFT, KWS_GECMIS_TOPLAM=gecmis,
             KWS_M_YUMUSAT=int(son["yumusat"]))
    for a, v in d.items():
        s.append(f"#define {a} {v}\n")
    s.append(f"#define KWS_GENISLEME_DIZI {{{', '.join(map(str, gen))}}}\n")
    s.append(f"#define KWS_EPS {O.EPS!r}f\n#define KWS_LN_ALT {O.LN_ALT!r}f\n#define KWS_LN_ADIM {O.LN_ADIM!r}f\n")
    s.append(f"#define KWS_CIKIS_OLCEK {repr(float(np.float32(tm['cikis']['olcek'])))}f\n")
    s.append(f"#define KWS_M_ESIK_UYAN {float(son['esik_uyan'])!r}f\n#define KWS_M_ESIK_KOMUT {float(son['esik_komut'])!r}f\n\n")
    s.append(_dizi("kws_mel_bas", "uint16_t", [b for b, _ in bant]))
    s.append(_dizi("kws_mel_n", "uint16_t", [len(ww) for _, ww in bant]))
    s.append(_dizi("kws_mel_ofs", "uint16_t", ofs))
    s.append(_dizi("kws_mel_w", "float", w, 8))
    s.append(_dizi("kws_w0", "int8_t", L[0]["w"].numpy(), 40))
    s.append(_dizi("kws_b0", "int32_t", L[0]["b"].numpy(), 16))
    s.append(_dizi("kws_m0", "int32_t", L[0]["m"].numpy(), 12))
    s.append(_dizi("kws_s0", "int8_t", L[0]["s"].numpy(), 32))
    s.append(_dizi("kws_wb", "int8_t", torch.stack([l["w"] for l in L[1:]]).numpy(), 40))
    s.append(_dizi("kws_bb", "int32_t", torch.stack([l["b"] for l in L[1:]]).numpy(), 16))
    s.append(_dizi("kws_mb", "int32_t", torch.stack([l["m"] for l in L[1:]]).numpy(), 12))
    s.append(_dizi("kws_sb", "int8_t", torch.stack([l["s"] for l in L[1:]]).numpy(), 32))
    s.append(_dizi("kws_mh", "int32_t", [l["mh"] for l in L[1:]]))
    s.append(_dizi("kws_mc", "int32_t", [l["mc"] for l in L[1:]]))
    s.append(_dizi("kws_wc", "int8_t", tm["cikis"]["w"].numpy(), 32))
    s.append(_dizi("kws_bc", "int32_t", tm["cikis"]["b"].numpy(), 16))
    os.makedirs(os.path.dirname(cikti), exist_ok=True)
    with open(cikti, "w", encoding="utf-8") as f:
        f.write("".join(s))
    for l in L:
        assert int(l["s"].min()) >= 1 and int(l["s"].max()) <= 62
        assert int(l["m"].max()) < 2 ** 31
    return dict(agirlik=agirlik, bayt=bayt, gecmis=gecmis)


@torch.no_grad()
def rastgele_net(tohum=0):
    """Eğitilmemiş ama ölçekleri kalibre edilmiş model (derleme ve C/PyTorch eşitlik denemeleri için)."""
    torch.manual_seed(tohum)
    net = O.KWSNet()
    for m in net.modules():
        if isinstance(m, torch.nn.BatchNorm1d):
            m.running_mean.normal_(0, 0.3)
            m.running_var.uniform_(0.5, 2.0)
            m.weight.data.uniform_(0.5, 1.5)
            m.bias.data.normal_(0, 0.3)
    net.eval()
    net.katla()
    net.cikis.bias.data.normal_(0, 0.5)
    on = O.Oznitelik()
    g = torch.Generator().manual_seed(tohum)
    x = torch.randn(4, 16000 * 3, generator=g) * torch.logspace(-3, -0.7, 4)[:, None]
    net.kalibrasyon(True)
    for _ in range(3):
        net(on(x))
    net.kalibrasyon(False)
    net.qat_ac(True)
    return net


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=None)
    ap.add_argument("--rastgele", action="store_true")
    ap.add_argument("--cikti", default=VARSAYILAN)
    a = ap.parse_args()
    if a.rastgele:
        net = rastgele_net()
        son = dict(esik_uyan=0.6, esik_komut=0.5, yumusat=4)
        acik = "YER TUTUCU: eğitilmemiş rastgele model (yalnız derleme). Gerçek model: ses/kws/README.md"
    else:
        net, k = yukle(a.model)
        net.qat_ac(True)
        son = k.get("son_islem", dict(esik_uyan=0.6, esik_komut=0.5, yumusat=4))
        acik = f"Model: {os.path.basename(a.model)}; {k.get('aciklama', '')}"
    r = baslik_yaz(net.eval(), son, a.cikti, acik)
    print(f"{a.cikti}: {r['agirlik']} int8 ağırlık, ~{r['bayt'] / 1024:.1f} KB flash, geçmiş {r['gecmis']} B")


if __name__ == "__main__":
    main()
