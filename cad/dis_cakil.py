"""Seçilen dış form "A — Çakıl" + yükseltilmiş figür platformu (ışık dışarı taşsın) -> cad/onizleme/cakil_*.png

Ürün sahibi (16 Ekim 2026): figürün konduğu yuvarlak kısım gövdeden biraz yukarıda kalmalı; içerideki 16'lı
NeoPixel halkanın ışığı dışarı yansımalı. İki yol:
  1 "bilezik": gövdeyle platform arasında yarı saydam beyaz bir bilezik (8 mm). Halka platformun altında,
               bileziğin içinde; ışık bileziğin her yanından dışarı parlar, figür üstündeyken de görünür.
  2 "yüzen"  : platform gövdenin üstünde 6 mm boşlukla "yüzer" (ortada gizli ayak). Halka platformun altına
               ters (aşağı bakan) takılır; ışık gövdenin üst yüzüne vurup yansır: platformun altından hale.
Gündüz ve gece (ışık yanıyor) görünüşü, ayrıca ışık yolunu ve NFC mesafesini gösteren kesit.

    python cad/dis_cakil.py
"""
import math
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon, FancyArrowPatch, Rectangle  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geometri import CS, dondur, silindir, xz_den_y_ye, yazi_duz, yildiz, yuvarlak_dikdortgen  # noqa: E402
import dis_konsept as K  # noqa: E402

CIKTI = K.CIKTI
SEG = 160
H_GOVDE = 50.0       # gövdenin üst düz yüzü
R_UST = 44.0         # gövde üst düz alanının yarıçapı (süperelips kesimi)
PLATFORM_R = 37.5    # platform (figür tablası) dış yarıçapı
PLATFORM_KAL = 3.0
YUVA_R = 31.6        # figür tabanı Ø62 + pay
YUVA_DERIN = 2.2
BILEZIK_R = (33.0, 36.0)
BILEZIK_H = 8.0
YUZEN_BOSLUK = 6.0
CUKUR_DERIN = 6.0    # "cukur": figür tabanının oturduğu derinlik
CUKUR_KENAR_R = 38.0 # çanağın üstteki ışık kenarı (r 31,6..38)
AYAK_R = 13.5        # gizli ayak halkanın iç boşluğundan (r 15,9) geçer
HALKA = (31.75 / 2, 44.5 / 2, 3.5)   # NeoPixel 16'lı: iç r, dış r, kalınlık


def profil_govde():
    zc, b, n, R = 18.0, 40.0, 2.8, 60.0
    pts = [(0, 0)]
    for z in np.linspace(0, H_GOVDE, 60):
        u = abs(z - zc) / b
        pts.append((R * max(0.0, 1 - u ** n) ** (1 / n), z))
    r0 = pts[1][0]
    pts.insert(1, (r0 - 2.0, 0))
    pts[2] = (r0, 2.0)
    pts.append((0, H_GOVDE))
    return pts


def govde_parcalari(yol):
    pf = profil_govde()
    govde = dondur(pf, SEG)
    # logo ve hoparlör (konsept A ile aynı yer)
    dis = dondur([(p[0] + 1.2, p[1]) for p in pf] + [(0, 0)], SEG)
    yazi = (xz_den_y_ye(yazi_duz(K.YAZI, K.YAZI_BOY, K.FONT, ayna=True), 0, 80, x=0, z=33.0) ^ dis) - govde
    izgara = yildiz(0, 0, 5.5, 2.4)
    for k, (rr, n, d) in enumerate(((9.0, 9, 2.4), (14.0, 14, 2.4))):
        for i in range(n):
            a = 2 * math.pi * (i + 0.5 * k) / n
            izgara = izgara + CS.circle(d / 2, 24).translate([rr * math.cos(a), rr * math.sin(a)])
    govde = govde - xz_den_y_ye(izgara, 40, 70, x=0, z=15.0)
    govde = govde - xz_den_y_ye(CS.circle(7.5, 48), -70, -40, x=-18, z=22)
    govde = govde - xz_den_y_ye(yuvarlak_dikdortgen(9.6, 3.8, 1.6), -70, -40, x=14, z=9)
    govde = govde - silindir(0.9, H_GOVDE - 15, H_GOVDE + 5, x=0, y=-41.5, seg=16)
    z0 = H_GOVDE
    if yol == "cukur":
        # figür yuvası gövdeye gömülü; yuvayı yarı saydam beyaz bir çanak oluşturur, üstte geniş ışık kenarı
        cz = z0 - CUKUR_DERIN
        govde = govde - silindir(CUKUR_KENAR_R + 0.2, cz - 2.5, z0 + 1, seg=SEG)
        isik = (silindir(CUKUR_KENAR_R, cz - 2.0, z0, seg=SEG) - silindir(YUVA_R, cz, z0 + 1, seg=SEG))
        pz = cz - PLATFORM_KAL + YUVA_DERIN   # figur_taban() tabanı çanağın tabanına oturtsun
        return govde, yazi, isik, None, None, pz
    if yol == "bilezik":
        govde = govde - silindir(BILEZIK_R[1] + 0.2, z0 - 1.5, z0 + 1, seg=SEG)  # bilezik 1,5 mm gömülür
        isik = (silindir(BILEZIK_R[1], z0 - 1.5, z0 + BILEZIK_H, seg=SEG)
                - silindir(BILEZIK_R[0], z0 - 2, z0 + BILEZIK_H + 1, seg=SEG))
        pz = z0 + BILEZIK_H
        ayak = None
    else:
        pz = z0 + YUZEN_BOSLUK
        ayak = silindir(AYAK_R, z0 - 1, pz, seg=SEG)  # gizli ayak (gölgede)
        # ışığın vurduğu yüz: gövde üstünde hafif çanak (yansıtıcı halka bölgesi), parlak beyaz boya/ek
        isik = silindir(PLATFORM_R + 4.0, z0 - 0.6, z0 + 0.02, seg=SEG) - silindir(AYAK_R + 0.3, z0 - 1, z0 + 1, seg=SEG)
        govde = govde - silindir(PLATFORM_R + 4.2, z0 - 0.6, z0 + 1, seg=SEG) + silindir(AYAK_R + 0.3, z0 - 0.6, z0, seg=SEG)
    platform = silindir(PLATFORM_R, pz, pz + PLATFORM_KAL, seg=SEG) - silindir(YUVA_R, pz + PLATFORM_KAL - YUVA_DERIN, pz + 5, seg=SEG)
    # platformun üst kenarı hafif pahlı
    pah = silindir(PLATFORM_R + 1, pz + PLATFORM_KAL - 0.8, pz + PLATFORM_KAL + 1, seg=SEG) - \
        silindir(PLATFORM_R - 0.8, pz + PLATFORM_KAL - 0.8, pz + PLATFORM_KAL + 2, seg=SEG, r2=PLATFORM_R + 1.2)
    platform = platform - pah
    return govde, yazi, isik, platform, ayak, pz


def figur_taban(pz):
    """Figür tabanı (Ø62 jeton) ve üstünde basit bir figür silüeti (yalnız ölçek için)."""
    z = pz + PLATFORM_KAL - YUVA_DERIN
    taban = silindir(31.0, z, z + 6, seg=SEG)
    govde = silindir(13.0, z + 6, z + 40, seg=64, r2=10.0) + silindir(11.0, z + 40, z + 60, seg=64)
    return taban, govde


def gorsel():
    os.makedirs(CIKTI, exist_ok=True)
    yollar = (("1 — Işık bileziği", "bilezik"), ("2 — Yüzen platform", "yuzen"), ("3 — Çukur + ışık kenarı", "cukur"))
    parcalar = {ad: govde_parcalari(ad) for _, ad in yollar}
    for mod in ("gunduz", "gece", "figurlu"):
        fig = plt.figure(figsize=(19, 6.6), dpi=110,
                         facecolor="#0E1430" if mod == "gece" else "white")
        for i, (baslik, ad) in enumerate(yollar):
            govde, yazi, isik, platform, ayak, pz = parcalar[ad]
            if mod == "gece":
                ls = [(govde, "#3a3530", False), (yazi, "#5a3a20", False), (isik, "#FF8FC8", True),
                      (platform, "#3a3530", False), (ayak, "#FF8FC8", True)]
            else:
                ls = [(govde, "#F6E7D2", False), (yazi, "#F2A65A", False),
                      (isik, "#FFFFFF" if mod == "gunduz" else "#FFB3D9", mod != "gunduz"),
                      (platform, "#F6E7D2", False), (ayak, "#E8DCCB", False)]
            if mod == "figurlu":
                t, g = figur_taban(pz)
                ls += [(t, "#FF6FA8", False), (g, "#FF9CC4", False)]
            ax = fig.add_subplot(1, 3, i + 1, projection="3d")
            ax.set_facecolor(fig.get_facecolor())
            elev, azim = 22, 90
            e, a = math.radians(elev), math.radians(azim)
            K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
            ax.set_zlim(-18, 78 if mod == "figurlu" else 72)
            ax.view_init(elev=elev, azim=azim)
            ax.set_title(baslik, fontsize=15, color="white" if mod == "gece" else "black")
        fig.suptitle({"gunduz": "Çakıl + yükseltilmiş figür platformu (gündüz)",
                      "gece": "Gece: 16'lı halka yanıyor (örnek renk: Niloya pembesi)",
                      "figurlu": "Figür üstündeyken: ışık platformun altından/yanından görünmeye devam eder"}[mod],
                     fontsize=13, color="white" if mod == "gece" else "black")
        plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0)
        yol = os.path.join(CIKTI, f"cakil_{mod}.png")
        fig.savefig(yol, facecolor=fig.get_facecolor())
        plt.close(fig)
        print(yol)
    kesit()


def kesit():
    """Yan kesit (x = 0 düzlemi, sağ yarı): ışık yolu, halka, NFC okuyucu, etiket mesafesi."""
    fig, axs = plt.subplots(1, 3, figsize=(20, 6.2), dpi=110)
    pf = profil_govde()
    for ax, ad, baslik in ((axs[0], "bilezik", "1 — Işık bileziği"), (axs[1], "yuzen", "2 — Yüzen platform"),
                           (axs[2], "cukur", "3 — Çukur + ışık kenarı")):
        z0 = H_GOVDE
        dis = [(r, z) for r, z in pf]
        ax.add_patch(Polygon(dis, closed=True, fc="#F6E7D2", ec="#8a7a66", lw=1.2))
        ax.add_patch(Polygon([(r - 2.4, z) for r, z in dis if r > 3 and 2 < z < z0 - 2.4] + [(0, z0 - 2.4), (0, 2.4)],
                             closed=True, fc="white", ec="#c8b9a5", lw=0.8))
        if ad == "cukur":
            cz = z0 - CUKUR_DERIN
            ax.add_patch(Rectangle((0, z0 - 2.4), CUKUR_KENAR_R + 0.2, 2.4, fc="white", ec="none"))
            ax.add_patch(Polygon([(0, cz - 2), (CUKUR_KENAR_R, cz - 2), (CUKUR_KENAR_R, z0), (YUVA_R, z0),
                                  (YUVA_R, cz), (0, cz)], closed=True, fc="#FFE3F1", ec="#e080b0", lw=1.2))
            halka_z = cz - 2 - 3.6
            ax.add_patch(Rectangle((HALKA[0], halka_z), HALKA[1] - HALKA[0], 1.6, fc="#333", ec="k"))
            ax.add_patch(Rectangle((HALKA[0] + 1, halka_z + 1.6), 5, 1.2, fc="#ff4fa3", ec="none"))
            for x2, y2 in ((10, cz + 6), (34, z0 + 6), (44, z0 + 4)):
                ax.add_patch(FancyArrowPatch((19, halka_z + 2.6), (x2, y2), arrowstyle="-|>", mutation_scale=12,
                                             color="#ff4fa3", lw=1.3))
            ax.text(39, z0 + 2.5, "ışık kenarı (r 31,6–38)", fontsize=9, color="#b0306f")
            ax.text(33, cz - 6, "yarı saydam çanak\n(beyaz PETG)", fontsize=9, color="#b0306f")
            tz = cz
            ax.add_patch(Rectangle((0, tz), 31.0, 6, fc="#FF9CC4", ec="#c0507c", lw=1))
            ax.add_patch(Rectangle((0, tz + 0.4), 12.5, 0.4, fc="#2060ff", ec="none"))
            ax.text(1, tz + 7.2, "figür tabanı (Ø62); NFC etiketi altta", fontsize=9)
            nfc_z = halka_z - 4.0
            ax.add_patch(Rectangle((0, nfc_z), 30, 1.6, fc="#1f6f3f", ec="k"))
            ax.text(1, nfc_z - 3.2, "NFC okuyucu (RC522 / PN5180)", fontsize=9, color="#1f6f3f")
            mes = tz + 0.4 - (nfc_z + 1.6)
            ax.annotate("", xy=(5, nfc_z + 1.6), xytext=(5, tz + 0.4), arrowprops=dict(arrowstyle="<->", color="#2060ff"))
            ax.text(6, (nfc_z + tz) / 2, f"etiket–anten ≈ {mes:.0f} mm", fontsize=9, color="#2060ff")
            ax.set_xlim(0, 66); ax.set_ylim(-2, z0 + 16)
            ax.set_aspect("equal"); ax.grid(alpha=.25)
            ax.set_title(baslik + " — yan kesit (sağ yarı, mm)", fontsize=12)
            continue
        if ad == "bilezik":
            pz = z0 + BILEZIK_H
            ax.add_patch(Rectangle((BILEZIK_R[0], z0 - 1.5), BILEZIK_R[1] - BILEZIK_R[0], BILEZIK_H + 1.5,
                                   fc="#FFE3F1", ec="#e080b0", lw=1.2))
            halka_z = pz - 4.2                # halka platformun altında, yukarı bakar
            ax.add_patch(Rectangle((HALKA[0], halka_z), HALKA[1] - HALKA[0], HALKA[2] - 2, fc="#333", ec="k"))
            ax.add_patch(Rectangle((HALKA[0] + 2.5, halka_z + 1.5), 5, 1.6, fc="#ff4fa3", ec="none"))
            for aci in (0, 20, -20):
                ax.add_patch(FancyArrowPatch((25, halka_z + 2), (50, halka_z + 2 + 25 * math.tan(math.radians(aci))),
                                             arrowstyle="-|>", mutation_scale=12, color="#ff4fa3", lw=1.4))
            nfc_z = z0 - 6.0
            ax.text(41, z0 + 3.5, "yarı saydam\nbilezik (beyaz PETG)", fontsize=9, color="#b0306f")
        else:
            pz = z0 + YUZEN_BOSLUK
            ax.add_patch(Rectangle((0, z0), AYAK_R, YUZEN_BOSLUK, fc="#E8DCCB", ec="#8a7a66", lw=1))
            halka_z = pz - 1.6                # halka platformun altında, aşağı bakar
            ax.add_patch(Rectangle((HALKA[0], halka_z), HALKA[1] - HALKA[0], 1.6, fc="#333", ec="k"))
            for x2 in (40, 47, 54):
                ax.add_patch(FancyArrowPatch((19.0, halka_z), (x2 - 8, z0 + 0.3), arrowstyle="-", color="#ff4fa3", lw=1.2))
                ax.add_patch(FancyArrowPatch((x2 - 8, z0 + 0.3), (x2 + 4, z0 + 7), arrowstyle="-|>",
                                             mutation_scale=12, color="#ff4fa3", lw=1.2))
            nfc_z = z0 - 6.0
            ax.text(40, z0 - 5, "ışık gövdenin üstüne\nvurup yansır (hale)", fontsize=9, color="#b0306f")
            ax.text(2, z0 + 1.2, "gizli ayak", fontsize=8)
        # platform + yuva + figür tabanı
        ax.add_patch(Polygon([(0, pz), (PLATFORM_R, pz), (PLATFORM_R, pz + PLATFORM_KAL - 0.8),
                              (PLATFORM_R - 0.8, pz + PLATFORM_KAL), (YUVA_R, pz + PLATFORM_KAL),
                              (YUVA_R, pz + PLATFORM_KAL - YUVA_DERIN), (0, pz + PLATFORM_KAL - YUVA_DERIN)],
                             closed=True, fc="#F6E7D2", ec="#8a7a66", lw=1.2))
        tz = pz + PLATFORM_KAL - YUVA_DERIN
        ax.add_patch(Rectangle((0, tz), 31.0, 6, fc="#FF9CC4", ec="#c0507c", lw=1))
        ax.add_patch(Rectangle((0, tz + 0.4), 12.5, 0.4, fc="#2060ff", ec="none"))
        ax.text(1, tz + 7.2, "figür tabanı (Ø62); NFC etiketi altta", fontsize=9)
        # NFC okuyucu (gövdenin içinde, üst duvarın altında)
        ax.add_patch(Rectangle((0, nfc_z), 30, 1.6, fc="#1f6f3f", ec="k"))
        ax.text(1, nfc_z - 3.2, "NFC okuyucu (RC522 / PN5180)", fontsize=9, color="#1f6f3f")
        mes = tz + 0.4 - (nfc_z + 1.6)
        ax.annotate("", xy=(5, nfc_z + 1.6), xytext=(5, tz + 0.4), arrowprops=dict(arrowstyle="<->", color="#2060ff"))
        ax.text(6, (nfc_z + tz) / 2, f"etiket–anten ≈ {mes:.0f} mm", fontsize=9, color="#2060ff")
        ax.set_xlim(0, 66); ax.set_ylim(-2, pz + 16)
        ax.set_aspect("equal"); ax.grid(alpha=.25)
        ax.set_title(baslik + " — yan kesit (sağ yarı, mm)", fontsize=12)
    plt.tight_layout()
    yol = os.path.join(CIKTI, "cakil_kesit.png")
    fig.savefig(yol)
    plt.close(fig)
    print(yol)


if __name__ == "__main__":
    gorsel()
