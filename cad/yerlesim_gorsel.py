"""Montaj rehberi görseli: her parçanın nereye geldiği (numaralı).

    python cad/yerlesim_gorsel.py     # cad/onizleme/yerlesim_rehberi.png (RC522 ile)
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon, Circle  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
import dis_konsept as K  # noqa: E402
from geometri import kutu  # noqa: E402

# (no, ad, zarf/yapı anahtarı, renk, modül)
PARCALAR = [
    (1, "Dış kabuk (eco ai)", "kabuk", "#EFE6D8", "üst"),
    (2, "NeoPixel halka (Ø55/Ø70)", "NeoPixel 16", "#ff4fa3", "üst"),
    (3, "Halka + NFC tutucu", "tutucu", "#c9b07a", "üst"),
    (4, "NFC okuyucu (RC522 / PN5180)", "RC522 okuyucu", "#1f6f3f", "üst"),
    (5, "5 V düzenleyici (kutunun üstünde)", "5 V düzenleyici", "#2d6cdf", "alt"),
    (6, "KCD11 açma-kapama (sol yan)", "KCD11 anahtar", "#222222", "üst"),
    (7, "Taban plakası (alt kapak)", "taban", "#E3D5BF", "alt"),
    (8, "4'lü AA yatağı (pil kutusunda)", "4xAA yatağı", "#4a4a52", "alt"),
    (9, "Hoparlör Ø50 (öne bakar)", "hoparlör (önden)", "#6b7280", "alt"),
    (10, "ESP32-S3 (ters, pinler yukarı)", "ESP32-S3", "#111111", "alt"),
    (11, "MAX98357A ses kartı", "MAX98357A", "#7b3fbf", "alt"),
    (12, "Figür tabanı Ø52 (çukurda)", "figur", "#1FB5B0", "üst"),
    (13, "Pil kapağı (alttan, M3 vida)", "pil_kapagi", "#d9c6ad", "alt"),
]


def golge(man):
    """Üstten izdüşüm çokgenleri."""
    return [np.asarray(p) for p in man.project().to_polygons()]


def plan_ciz(ax, parcalar, z, yapi, ayna=False, baslik=""):
    s = -1.0 if ayna else 1.0
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(C.dis_r(C.ZC) * np.cos(th), C.dis_r(C.ZC) * np.sin(th), color="#8a7a66", lw=1.6)
    for no, ad, k, renk, _ in parcalar:
        man = yapi.get(k) if k in yapi else z.get(k)
        if man is None:
            continue
        alfa = 0.35 if k in ("kabuk", "taban", "tutucu") else 0.75
        for p in golge(man):
            ax.add_patch(Polygon(np.c_[s * p[:, 0], p[:, 1]], closed=True, fc=renk, ec="#333", lw=0.5, alpha=alfa))
        b = man.bounding_box()
        cx, cy = (b[0] + b[3]) / 2, (b[1] + b[4]) / 2
        yer = {"kabuk": (-46, 40), "taban": (-48, -30), "tutucu": (26, 22), "NeoPixel 16": (0, 21.0)}.get(k, (cx, cy))
        ax.add_patch(Circle((s * yer[0], yer[1]), 4.2, fc="white", ec="#222", lw=1.2, zorder=5))
        ax.text(s * yer[0], yer[1], str(no), ha="center", va="center", fontsize=10, fontweight="bold", zorder=6)
    ax.text(0, C.dis_r(C.ZC) + 3, "ÖN (logo)", ha="center", fontsize=10, fontweight="bold")
    ax.text(0, -C.dis_r(C.ZC) - 7, "ARKA", ha="center", fontsize=10, fontweight="bold")
    ax.text(s * (C.dis_r(C.ZC) + 2), 0, "SAĞ" if s > 0 else "SAĞ", ha="left" if s > 0 else "right", va="center", fontsize=9)
    ax.text(-s * (C.dis_r(C.ZC) + 2), 0, "SOL", ha="right" if s > 0 else "left", va="center", fontsize=9)
    ax.set_xlim(-70, 70); ax.set_ylim(-70, 68); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(baslik, fontsize=12)


def main():
    z, yapi, sorun, mesafe = C.denetle("rc522")
    fig = plt.figure(figsize=(22, 13), dpi=100)
    gs = fig.add_gridspec(2, 3, width_ratios=[1.25, 1, 1])
    # 1) patlatılmış 3B
    ax = fig.add_subplot(gs[:, 0], projection="3d")
    kaydir = {"kabuk": 82, "NeoPixel 16": 36, "tutucu": 26, "RC522 okuyucu": 16, "KCD11 anahtar": 82,
              "figur": 104, "pil_kapagi": -16}
    ls = []
    yarim = kutu(-80, 0, -80, 80, -5, 80)
    etiket = []
    for no, ad, k, renk, _ in PARCALAR:
        man = yapi.get(k) if k in yapi else z.get(k)
        dz = kaydir.get(k, 0)
        if k == "kabuk":
            man = man ^ yarim
        if k == "ESP32-S3":
            ls.append((C.esp_stl(), renk, False))
        else:
            ls.append((man.translate([0, 0, dz]), renk, k == "NeoPixel 16"))
        b = man.bounding_box()
        if k == "taban":
            etiket.append((no, -52, -20, 4))
        else:
            etiket.append((no, (b[0] + b[3]) / 2, (b[1] + b[4]) / 2, b[5] + dz))
    elev, azim = 16, 32
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    for no, x, y, zz in etiket:
        ax.text(x, y, zz + 3, str(no), fontsize=11, fontweight="bold", ha="center",
                bbox=dict(boxstyle="circle,pad=0.25", fc="white", ec="#222"))
    ax.set_xlim(-62, 62); ax.set_ylim(-62, 62); ax.set_zlim(-5, 150)
    ax.set_box_aspect((1, 1, 1.35))
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Patlatılmış görünüş: yukarıdan aşağı takılma sırası\n(kabuk yarım kesik, içi görünsün)", fontsize=13)
    # 2) alt kapak üstten
    ax2 = fig.add_subplot(gs[0, 1])
    alt = [p for p in PARCALAR if p[4] == "alt"]
    plan_ciz(ax2, [p for p in alt if p[2] != "pil_kapagi"], z, yapi,
             baslik="ALT KAPAK — üstten bakış\n(pil kutusu; üstünde ESP32, ses kartı, düzenleyici; önde hoparlör)")
    for p in golge(z["jumper payı"]):
        ax2.add_patch(Polygon(p, closed=True, fc="#e8a33d", ec="none", alpha=0.25))
    ax2.text(-27, -54, "turuncu: jumper kablolar\n(ESP32 pinleri, yukarı)", fontsize=8, color="#a8650a")
    for aci in C.VIDA_ACILAR:
        x, y = C.VIDA_R * math.cos(math.radians(aci)), C.VIDA_R * math.sin(math.radians(aci))
        ax2.add_patch(Circle((x, y), 1.7, fc="#555", ec="none"))
    ax2.text(62, -62, "● M3 vida (4)", fontsize=8, ha="right")
    # 3) üst kabuk alttan (ters çevrilmiş)
    ax3 = fig.add_subplot(gs[0, 2])
    ust = [p for p in PARCALAR if p[4] == "üst" and p[2] != "figur"]
    plan_ciz(ax3, ust, z, yapi, ayna=True, baslik="ÜST KABUK — ters çevrilmiş, alttan bakış\n(halka, tutucu, NFC, anahtar kabukta)")
    for aci in C.UST_ACILAR:
        x, y = C.UST_DIREK_R * math.cos(math.radians(aci)), C.UST_DIREK_R * math.sin(math.radians(aci))
        ax3.add_patch(Circle((-x, y), 1.4, fc="#555", ec="none"))
    ax3.text(-68, -62, "● pim (4): tutucu kabuğun\ndireklerine geçer (vidasız)", fontsize=8, ha="left")
    # 4) yan kesit
    ax4 = fig.add_subplot(gs[1, 1:])
    for no, ad, k, renk, _ in PARCALAR:
        man = yapi.get(k) if k in yapi else z.get(k)
        cs = man.rotate([0, -90, 0]).slice(0.0)
        for poly in cs.to_polygons():
            pp = np.asarray(poly)
            ax4.add_patch(Polygon(np.c_[pp[:, 1], -pp[:, 0]], closed=True, fc=renk, ec="#333", lw=0.6,
                                  alpha=0.55 if k in ("kabuk", "taban", "tutucu") else 0.9))
    cs = z["jumper payı"].rotate([0, -90, 0]).slice(0.0)
    for poly in cs.to_polygons():
        pp = np.asarray(poly)
        ax4.add_patch(Polygon(np.c_[pp[:, 1], -pp[:, 0]], closed=True, fc="#e8a33d", ec="none", alpha=0.3))
    yerler = {1: (-52, 48), 2: (22, 55), 3: (24, 49), 4: (-6, 46), 7: (-48, 1.2), 8: (-4, 10), 13: (8, -1.5),
              9: (37, 30), 10: (-32, 25), 12: (0, 53.5)}
    for no, (y, zz) in yerler.items():
        ax4.add_patch(Circle((y, zz), 2.6, fc="white", ec="#222", lw=1.1, zorder=5))
        ax4.text(y, zz, str(no), ha="center", va="center", fontsize=9, fontweight="bold", zorder=6)
    ax4.text(-45, 30, "jumper\nboşluğu", fontsize=8, color="#a8650a", ha="center")
    ax4.set_xlim(-66, 66); ax4.set_ylim(-3, 60); ax4.set_aspect("equal"); ax4.grid(alpha=.2)
    ax4.set_xlabel("← ARKA                         y (mm)                         ÖN (logo) →")
    ax4.set_ylabel("z (mm)")
    ax4.set_title("Ortadan yan kesit (x = 0): parçaların yüksekliği", fontsize=12)
    # lejant
    metin = "\n".join(f"{no:>2}. {ad}" for no, ad, *_ in PARCALAR)
    fig.text(0.005, 0.02, metin, fontsize=10.5, family="monospace", va="bottom",
             bbox=dict(fc="white", ec="#999", boxstyle="round,pad=0.5"))
    fig.suptitle("Hikâye Oyuncağı standı — her parça nereye gelir", fontsize=18, fontweight="bold")
    plt.tight_layout(rect=(0, 0, 1, 0.96))
    yol = os.path.join(C.KOK, "onizleme", "yerlesim_rehberi.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


if __name__ == "__main__":
    print(main())
