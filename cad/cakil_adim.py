"""Çakıl stand: parçaları TEK TEK yerleştirme adımları (ürün sahibi onayladıkça sıradaki) -> cad/onizleme/adim_<n>_<ad>.png

    python cad/cakil_adim.py 1        # 1. adım: boş gövde + 16'lı halka
Her görsel: solda gövdenin sağ yarısı kesik 3B görünüş, sağda tam ortadan yan kesit (ölçülü).
Ölçüler ve yerler cad/cakil_ic.py'den (tek kaynak).
"""
import math
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
import dis_konsept as K  # noqa: E402
from geometri import kutu  # noqa: E402

ADIMLAR = [
    ("halka", "16'lı NeoPixel halka", ["NeoPixel 16"], ["tutucu"]),
    ("nfc", "NFC okuyucu (RC522 / PN5180)", ["RC522 okuyucu"], []),
    ("hoparlor", "Hoparlör 50x50", ["hoparlör (aşağı bakar)"], ["taban"]),
    ("pil", "18650 pil yatağı", ["18650 yatağı"], []),
    ("esp32", "ESP32-S3", ["ESP32-S3 (rafta)"], ["raf"]),
    ("tp4056", "TP4056 + USB-C", ["TP4056 Type-C"], []),
    ("anahtar", "Açma-kapama anahtarı", ["KCD11 anahtar"], []),
    ("amfi", "MAX98357A", ["MAX98357A"], []),
    ("mikrofon", "INMP441 mikrofon", ["INMP441 mikrofon"], []),
]


def kesit_ciz(ax, man, renk, ec, alfa=1.0):
    if man is None or man.is_empty():
        return
    cs = man.rotate([0, -90, 0]).slice(0.0)       # x = 0 düzlemi: (u, v) = (-z, y)
    for poly in cs.to_polygons():
        p = np.asarray(poly)
        ax.add_patch(Polygon(np.c_[p[:, 1], -p[:, 0]], closed=True, fc=renk, ec=ec, lw=1.0, alpha=alfa))


def adim_gorsel(n, notlar=()):
    ad, baslik, parcalar, yapilar = ADIMLAR[n - 1]
    z, yapi, sorun, mesafe = C.denetle("rc522")
    onceki_p = [p for a in ADIMLAR[:n - 1] for p in a[2]]
    onceki_y = [y for a in ADIMLAR[:n - 1] for y in a[3]]
    fig = plt.figure(figsize=(17, 7.6), dpi=110)
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    yarim = kutu(-80, 0, -80, 80, -5, 80)
    ls = [(yapi["kabuk"] ^ yarim, C.RENK_YAPI["kabuk"], False)]
    ls += [(yapi[y], "#d8d2c8", False) for y in onceki_y]
    ls += [(z[p], "#9a9a9a", False) for p in onceki_p]
    ls += [(yapi[y], "#ffd27a", False) for y in yapilar]
    ls += [(z[p], C.RENK_PARCA.get(p, "#e33"), p == "NeoPixel 16") for p in parcalar]
    elev, azim = 22, 25
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-50, 50); ax.set_ylim(-50, 50); ax.set_zlim(-12, 70)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Sağ yarı kesik (yeni parça renkli, öncekiler gri)", fontsize=12)
    ax2 = fig.add_subplot(1, 2, 2)
    kesit_ciz(ax2, yapi["kabuk"], C.RENK_YAPI["kabuk"], "#8a7a66")
    for y in onceki_y:
        kesit_ciz(ax2, yapi[y], "#e6e1d9", "#999")
    for p in onceki_p:
        kesit_ciz(ax2, z[p], "#bdbdbd", "#777")
    for y in yapilar:
        kesit_ciz(ax2, yapi[y], "#ffd27a", "#b08a30")
    for p in parcalar:
        kesit_ciz(ax2, z[p], C.RENK_PARCA.get(p, "#e33"), "k")
    for x, yy, metin, tx, ty in notlar:
        ax2.annotate(metin, xy=(x, yy), xytext=(tx, ty), fontsize=9, arrowprops=dict(arrowstyle="->", color="#444"))
    ax2.set_xlim(-66, 66); ax2.set_ylim(-4, 64); ax2.set_aspect("equal"); ax2.grid(alpha=.25)
    ax2.set_xlabel("y (mm)   ← ARKA (USB-C)                 ÖN (logo) →"); ax2.set_ylabel("z (mm)")
    ax2.set_title("Ortadan yan kesit (x = 0)", fontsize=12)
    fig.suptitle(f"Adım {n}/{len(ADIMLAR)}: {baslik}", fontsize=15)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", f"adim_{n}_{ad}.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def ust_gorunus():
    """Üstten bakış: gündüz (yarıklar) ve gece (halka yanıyor: yarıklardan ışık)."""
    from matplotlib.path import Path
    from matplotlib.patches import PathPatch
    k = C.kabuk()
    cs = k.slice(C.H - 0.2)
    fig, axs = plt.subplots(1, 2, figsize=(14, 7), dpi=110)
    for ax, gece in zip(axs, (False, True)):
        ax.set_facecolor("#0E1430" if gece else "white")
        if gece:
            th = np.linspace(0, 2 * np.pi, 200)
            for r, a in ((C.ISIK_R[1] + 2, .25), (C.ISIK_R[1], .6)):
                ax.fill(r * np.cos(th), r * np.sin(th), color="#ff4fa3", alpha=a, lw=0)
        verts, codes = [], []
        for poly in cs.to_polygons():
            p = np.asarray(poly)
            verts += list(p) + [p[0]]
            codes += [Path.MOVETO] + [Path.LINETO] * (len(p) - 1) + [Path.CLOSEPOLY]
        ax.add_patch(PathPatch(Path(verts, codes), fc="#3a3530" if gece else "#F6E7D2", ec="#8a7a66", lw=0.6))
        ax.add_patch(plt.Circle((0, 0), C.YUVA_R + 1.7, fc="#3a3530" if gece else "#F6E7D2", ec="none"))  # ağız pahı
        ax.add_patch(plt.Circle((0, 0), C.YUVA_R, fc="#2a2622" if gece else "#e9dcc6", ec="#8a7a66"))
        ax.set_xlim(-48, 48); ax.set_ylim(-48, 48); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title("Gece: halka yanıyor (örnek: Niloya pembesi)" if gece else "Gündüz: figür çukuru ve ışık yarıkları",
                     color="black", fontsize=13)
    fig.patch.set_facecolor("white")
    fig.suptitle(f"Üstten: {C.ISIK_YARIK[0]} ışınsal yarık ({C.ISIK_YARIK[1]} mm), LED'lerin tam üstünde; ortada figür çukuru Ø{2 * C.YUVA_R:.1f}",
                 fontsize=12)
    plt.tight_layout(rect=(0, 0, 1, 0.94))
    yol = os.path.join(C.KOK, "onizleme", "adim_1_ust.png")
    fig.savefig(yol, facecolor="white")
    plt.close(fig)
    return yol


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    notlar = {
        1: [(-19, C.Z_HALKA_UST - 0.8, "16'lı halka çukurun ÇEVRESİNDE, tavana yaslı;\nLED'ler tavandaki ışık oyuğuna girer", -60, 22),
            (19, C.Z_HALKA_UST + 1.2, "LED'lerin üstü şerit şerit açık:\n32 ışınsal yarık (1,2 mm)", 16, 31),
            (24, C.Z_TUTUCU_ALT + 1, "tutucu plaka halkayı alttan tavana bastırır\n(4 direğe M2,5 vida); ortası çukura açık", 6, 8),
            (-8, C.Z_CANAK_TABAN, f"figür çukuru Ø{2 * C.YUVA_R:.1f} (figür tabanı Ø{C.FIGUR_TABAN_D:.0f}), halkanın ortasından geçer", -55, 62)],
    }.get(n, [])
    print(adim_gorsel(n, notlar))
    if n == 1:
        print(ust_gorunus())
