"""Teknik çizimler (A3, ölçek 1:1) -> cad/teknik_cizim.svg/.pdf ve cad/patlatilmis_montaj.svg/.pdf.

Bütün ölçüler parametreler.py'den ve parçaların kendisinden (kesitler manifold dilimleme ile) gelir:
parametre değişince çizim de değişir.
"""
import math
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import parametreler as P  # noqa: E402
import parcalar as pc  # noqa: E402
from onizleme import kesit_x, kesit_z, poligon_ciz, yerlestir, RENK  # noqa: E402

KOK = os.path.dirname(os.path.abspath(__file__))
A3 = (420.0, 297.0)
matplotlib.rcParams["svg.fonttype"] = "path"
matplotlib.rcParams["hatch.linewidth"] = 0.3


def sayfa():
    fig = plt.figure(figsize=(A3[0] / 25.4, A3[1] / 25.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, A3[0])
    ax.set_ylim(0, A3[1])
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(plt.Rectangle((10, 10), A3[0] - 20, A3[1] - 20, fill=False, lw=0.8))
    return fig, ax


def ok(ax, p0, p1, lw=0.35):
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="<|-|>", lw=lw, shrinkA=0, shrinkB=0,
                                                      mutation_scale=5, color="k"))


def olcu_yatay(ax, x0, x1, y, metin, ust=True, uz=(None, None), fs=5.5):
    """x0..x1 arası yatay ölçü, y yüksekliğinde; uz: uzatma çizgilerinin başladığı y'ler."""
    for x, yb in zip((x0, x1), uz):
        if yb is not None:
            ax.plot([x, x], [yb, y + (1.5 if y > yb else -1.5)], lw=0.25, color="k")
    ok(ax, (x0, y), (x1, y))
    ax.text((x0 + x1) / 2, y + (0.8 if ust else -0.8), metin, ha="center", va="bottom" if ust else "top",
            fontsize=fs)


def olcu_dikey(ax, y0, y1, x, metin, sag=True, uz=(None, None), fs=5.5):
    for y, xb in zip((y0, y1), uz):
        if xb is not None:
            ax.plot([xb, x + (1.5 if x > xb else -1.5)], [y, y], lw=0.25, color="k")
    ok(ax, (x, y0), (x, y1))
    ax.text(x + (0.8 if sag else -0.8), (y0 + y1) / 2, metin, ha="left" if sag else "right", va="center",
            fontsize=fs, rotation=90)


def cember(ax, cx, cy, r, ls="-", lw=0.4, renk="k"):
    t = np.linspace(0, 2 * np.pi, 361)
    ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), ls=ls, lw=lw, color=renk)


def cap_olcu(ax, cx, cy, r, aci, metin, metin_yer, fs=5.0):
    a = math.radians(aci)
    p = (cx + r * math.cos(a), cy + r * math.sin(a))
    ax.annotate(metin, xy=p, xytext=metin_yer, fontsize=fs, ha="left", va="center",
                arrowprops=dict(arrowstyle="-|>", lw=0.3, mutation_scale=5, color="k"))


def baslik_blok(ax, baslik, alt):
    x0, y0 = A3[0] - 150, 10
    ax.add_patch(plt.Rectangle((x0, y0), 140, 24, fill=False, lw=0.6))
    ax.plot([x0, x0 + 140], [y0 + 12, y0 + 12], lw=0.4, color="k")
    ax.text(x0 + 3, y0 + 18, baslik, fontsize=9, va="center", weight="bold")
    ax.text(x0 + 3, y0 + 6, alt, fontsize=5.5, va="center")


# ---------------------------------------------------------------------------------------------
def teknik_cizim(parca):
    yer = yerlestir(parca)
    fig, ax = sayfa()
    # ===================== ÜST GÖRÜNÜŞ (1:1), merkez
    cx, cy = 80.0, 212.0
    ax.text(14, 281, "ÜST GÖRÜNÜŞ (kapak + difüzör; kesik çizgi: gizli)  ölçek 1:1", fontsize=6.5,
            weight="bold")
    kap = yer["ust_kapak"]
    poligon_ciz(ax, [q + [cx, cy] for q in kesit_z(kap, P.H_ALT + P.KAPAK_KAL - 0.5)], RENK["ust_kapak"], lw=0.4)
    poligon_ciz(ax, [q + [cx, cy] for q in kesit_z(kap, P.H_ALT + P.YUVA_TABAN_KAL + 0.5)], "#9fb0c8", lw=0.3,
                alfa=0.5)
    poligon_ciz(ax, [q + [cx, cy] for q in kesit_z(yer["difuzor_halka"],
                                                       P.H_ALT + P.LED_UST + P.ISIK_BOSLUGU + P.DIF_KAL / 2)],
                RENK["difuzor_halka"], lw=0.4, z=3)
    cember(ax, cx, cy, P.R_DIS, lw=0.6)
    cember(ax, cx, cy, P.HALKA_DIS_D / 2, ls="--", lw=0.3)
    cember(ax, cx, cy, P.HALKA_IC_D / 2, ls="--", lw=0.3)
    # eksenler
    ax.plot([cx - 70, cx + 70], [cy, cy], lw=0.25, ls="-.", color="k")
    ax.plot([cx, cx], [cy - 70, cy + 70], lw=0.25, ls="-.", color="k")
    ax.text(cx, cy + P.R_DIS + 1.2, "ÖN (çocuk, hoparlör)", ha="center", fontsize=5, va="bottom")
    ax.text(cx, cy - P.R_DIS - 1.2, "ARKA (USB-C, mikrofon)", ha="center", fontsize=5, va="top")
    # gizli: vidalar, ayaklar, RC522
    for a in P.VIDA_ACILAR:
        x, y = P.VIDA_R * math.cos(math.radians(a)), P.VIDA_R * math.sin(math.radians(a))
        cember(ax, cx + x, cy + y, P.INSERT_D / 2, ls="--", lw=0.3)
        cember(ax, cx + x, cy + y, P.VIDA_HAVSA_D / 2, ls=":", lw=0.3)
        ax.text(cx + x * 1.12, cy + y * 1.12, f"V{a:.0f}°", fontsize=4.5, ha="center", va="center")
    for a in P.AYAK_ACILAR:
        x, y = P.AYAK_R * math.cos(math.radians(a)), P.AYAK_R * math.sin(math.radians(a))
        cember(ax, cx + x, cy + y, P.AYAK_D / 2, ls=":", lw=0.3, renk="#555")
    L, W = P.RC522
    x0 = -P.RC522_ANTEN_KAYMA - L / 2
    ax.add_patch(plt.Rectangle((cx + x0, cy - W / 2), L, W, fill=False, ls="--", lw=0.3))
    ax.text(cx + x0 + 1, cy - W / 2 + 1, "RC522 (altta)", fontsize=4.5)
    for x, y in P.RC_VIDALAR:
        cember(ax, cx + x, cy + y, P.RC_VIDA_PILOT / 2, ls="--", lw=0.3)
    # USB ve mikrofon
    ax.add_patch(plt.Rectangle((cx - P.USBC_AGIZ[0] / 2, cy - P.R_DIS - 1.2), P.USBC_AGIZ[0], 2.4, fill=True,
                               color="k"))
    mx, my = P.R_DIS * math.cos(math.radians(P.MIK_ACI)), P.R_DIS * math.sin(math.radians(P.MIK_ACI))
    ax.plot(cx + mx, cy + my, "ko", ms=1.5)
    ax.annotate(f"mikrofon deliği Ø{P.MIK_DELIK:.0f} ({P.MIK_ACI:.0f}°, z={P.MIK_Z:.0f})", xy=(cx + mx, cy + my),
                xytext=(148, 160), fontsize=5, arrowprops=dict(arrowstyle="-", lw=0.3))
    ax.annotate(f"USB-C (180° arka, z={P.USBC_Z:.0f})", xy=(cx, cy - P.R_DIS), xytext=(148, 153),
                fontsize=5, arrowprops=dict(arrowstyle="-", lw=0.3))
    # çaplar
    cap_olcu(ax, cx, cy, P.R_DIS, 45, f"Ø{P.D_DIS:.0f} dış", (148, 268))
    cap_olcu(ax, cx, cy, P.YUVA_R, 20, f"Ø{2 * P.YUVA_R:.1f} figür yuvası\n(taban Ø{P.TABAN_D:.0f})", (148, 258))
    cap_olcu(ax, cx, cy, P.KANAL_UST_R_DIS - P.DIF_PAY, 10, f"difüzör Ø{2 * (P.KANAL_UST_R_IC + P.DIF_PAY):.1f}/"
             f"Ø{2 * (P.KANAL_UST_R_DIS - P.DIF_PAY):.1f}", (148, 247))
    cap_olcu(ax, cx, cy, P.HALKA_DIS_D / 2, -5, f"halka Ø{P.HALKA_IC_D:.0f}/Ø{P.HALKA_DIS_D:.0f}\n"
             f"(kanal Ø{2 * P.KANAL_R_IC:.1f}/Ø{2 * P.KANAL_R_DIS:.1f})", (148, 236))
    cap_olcu(ax, cx, cy, P.VIDA_R, -30, f"vida çemberi Ø{2 * P.VIDA_R:.0f}:\n3×M3 (0°,135°,225°)", (148, 172))
    ax.text(cx - P.ANAHTAR_G / 2 - 1, cy - P.YUVA_R + 4.5, "kama", fontsize=4.5, ha="right")

    # ===================== KESİT A–A (x=0), 1:1
    ox, oy = 300.0, 196.0      # y=0 , z=0 noktası
    ax.text(ox - 64, oy + 85, "KESİT A–A (x = 0, yandan; sol = arka, sağ = ön)  ölçek 1:1", fontsize=7,
            weight="bold")
    for ad, m in yer.items():
        polys = [p + [ox, oy] for p in kesit_x(m)]
        poligon_ciz(ax, polys, RENK[ad], lw=0.35, hatch="////" if ad not in ("difuzor_halka",) else None, z=2)
    zarf = pc.zarflar()
    for zad, zm in zarf.items():
        polys = [p + [ox, oy] for p in kesit_x(zm)]
        poligon_ciz(ax, polys, "#bfe3c5", kenar="#2e6b38", lw=0.3, z=3)
    H_top = P.H_ALT + P.LED_UST + P.ISIK_BOSLUGU + P.DIF_KAL
    # ölçüler
    olcu_yatay(ax, ox - P.R_DIS, ox + P.R_DIS, oy - 8, f"Ø{P.D_DIS:.0f}", ust=False, uz=(oy, oy))
    olcu_dikey(ax, oy, oy + H_top, ox - P.R_DIS - 22, f"{H_top:.1f} toplam", sag=False, uz=(None, None))
    olcu_dikey(ax, oy, oy + P.H_ALT, ox - P.R_DIS - 13, f"{P.H_ALT:.0f} gövde", sag=False, uz=(ox - P.R_DIS, None))
    olcu_dikey(ax, oy + P.H_ALT, oy + P.H_ALT + P.KAPAK_KAL, ox + P.R_DIS + 4, f"{P.KAPAK_KAL:.0f} kapak",
               uz=(ox + P.R_DIS, ox + P.R_DIS))
    olcu_dikey(ax, oy + P.H_ALT, oy + H_top, ox + P.R_DIS + 13, f"{H_top - P.H_ALT:.1f}",
               uz=(None, ox + 53.4))
    olcu_dikey(ax, oy, oy + P.HOP_Z, ox + P.R_DIS + 4, f"{P.HOP_Z:.0f} hop. ekseni",
               uz=(None, ox + P.R_DIS))
    olcu_dikey(ax, oy, oy + P.USBC_Z, ox - P.R_DIS - 5, f"{P.USBC_Z:.0f} USB-C", sag=False,
               uz=(None, ox - P.R_DIS))
    # yuva ayrıntısı
    ax.annotate(f"yuva tabanı {P.YUVA_TABAN_KAL} mm (NFC)\nyuva derinliği {P.KAPAK_KAL - P.YUVA_TABAN_KAL:.1f}",
                xy=(ox + 5, oy + P.H_ALT + 0.9), xytext=(ox - 40, oy + 72), fontsize=5,
                arrowprops=dict(arrowstyle="-|>", lw=0.3, mutation_scale=5))
    ax.annotate(f"ışık boşluğu {P.ISIK_BOSLUGU:.0f} mm\ndifüzör {P.DIF_KAL} mm",
                xy=(ox + 48.5, oy + P.H_ALT + 8), xytext=(ox + 30, oy + 75), fontsize=5,
                arrowprops=dict(arrowstyle="-|>", lw=0.3, mutation_scale=5))
    ax.annotate("NFC: etiket→anten ≈3,6 mm", xy=(ox, oy + P.H_ALT - 0.8), xytext=(ox - 20, oy + 30), fontsize=5,
                arrowprops=dict(arrowstyle="-|>", lw=0.3, mutation_scale=5))
    ax.annotate("ızgara (yarık 1,6)", xy=(ox + P.R_DIS - 1, oy + P.HOP_Z), xytext=(ox + 30, oy - 20),
                fontsize=5, arrowprops=dict(arrowstyle="-|>", lw=0.3, mutation_scale=5))
    ax.annotate("derin havşa + M3x10 (gizli)", xy=(ox - 1, oy + 2), xytext=(ox - 60, oy - 20), fontsize=5,
                arrowprops=dict(arrowstyle="-", lw=0.3))

    # ===================== KESİT B–B (z = 15, yerleşim), 1:1
    bx, by = 80.0, 76.0
    zb = 15.0
    ax.text(148, by + 50, f"KESİT B–B\n(z = {zb:.0f}, üstten;\nalt gövde yerleşimi)\nölçek 1:1", fontsize=6.5,
            weight="bold", va="top")
    poligon_ciz(ax, [q + [bx, by] for q in kesit_z(yer["govde_alt"], zb)], RENK["govde_alt"], lw=0.35,
                hatch="////")
    etiket = {
        "Taşıyıcı pertinaks 5x7": "taşıyıcı 50×70",
        "ESP32-S3-DevKitC-1 (+headerlar)": "ESP32-S3",
        "Seviye çevirici + 1000 µF + klemensler": "74AHCT1G125\n1000µF",
        "MAX98357A PCB": "", "MAX98357A bileşen/klemens": "MAX98357A",
        "Hoparlör Ø40x20": "hoparlör Ø40", "USB-C kartı": "USB-C", "INMP441 kartı": "",
    }
    for zad, zm in zarf.items():
        if zad not in etiket:
            continue
        b = zm.bounding_box()
        # izdüşüm kutusu (üstten)
        ax.add_patch(plt.Rectangle((b[0] + bx, b[1] + by), b[3] - b[0], b[4] - b[1], fill=True,
                                   facecolor="#bfe3c5", edgecolor="#2e6b38", lw=0.3, alpha=0.6, zorder=3))
        if etiket[zad]:
            ax.text(bx + (b[0] + b[3]) / 2, by + (b[1] + b[4]) / 2, etiket[zad], fontsize=4.5, ha="center",
                    va="center", zorder=4)
    mx, my = 60 * math.cos(math.radians(P.MIK_ACI)), 60 * math.sin(math.radians(P.MIK_ACI))
    ax.text(bx + mx - 6, by + my + 6, "INMP441\n(z=36)", fontsize=4.5, ha="center")
    cember(ax, bx, by, P.R_DIS, lw=0.5)
    # taşıyıcı ölçüleri
    tx0 = P.TASIYICI_MERKEZ[0] - P.TASIYICI[0] / 2
    ty0 = P.TASIYICI_MERKEZ[1] - P.TASIYICI[1] / 2
    olcu_yatay(ax, bx + tx0, bx + tx0 + P.TASIYICI[0], by + ty0 - 4, f"{P.TASIYICI[0]:.0f}", ust=False)
    olcu_dikey(ax, by + ty0, by + ty0 + P.TASIYICI[1], bx + tx0 - 4, f"{P.TASIYICI[1]:.0f}", sag=False)

    # ===================== parça listesi
    lx, ly = 190.0, 140.0
    ax.text(lx, ly, "PARÇA LİSTESİ (basılanlar: cad/stl/; elektronik: docs/DONANIM.md)", fontsize=7,
            weight="bold")
    satirlar = [
        ("1", "govde_alt.stl", "alt gövde, PETG/PLA", "1"),
        ("2", "ust_kapak.stl", "üst kapak (yuva + halka kanalı), opak", "1"),
        ("3", "difuzor_halka.stl", "difüzör, beyaz yarı saydam PETG", "1"),
        ("4", "rc522_tutucu.stl", "RC522 tutucu çerçeve", "1"),
        ("5", "figurler/<kimlik>.stl", "figür tabanı (12 adlı) / figur_taban.stl yazısız", "figür başına 1"),
        ("6", "ayar_karti.stl", "ayar kartı tabanı (topuzlu, AYAR)", "1"),
        ("7", "ESP32-S3-DevKitC-1 N16R8", "taşıyıcıda dişi headerlara takılı", "1"),
        ("8", "5×7 cm delikli pertinaks", "4 köşe kenetli kızakta", "1"),
        ("9", "MAX98357A + 40 mm 4 Ω 3 W hoparlör", "dikey kızak / ön bölme, köpük conta", "1+1"),
        ("10", "INMP441", "arka iç ped, 1 mm köpük conta", "1"),
        ("11", "RC522 (bileşen yüzü aşağı)", "tutucu ile kapağa 4×M2,5x8 sac vidası", "1"),
        ("12", "NeoPixel halka Ø104/Ø90", "kanalda, kablo arkadan aşağı", "1"),
        ("13", "USB-C kartı (5,1 kΩ CC)", "arka platform, epoksi + kablo bağı", "1"),
        ("14", "M3 ısıl gömme somun M3×5,7 + M3×10 vida", "kapak–gövde", "3+3"),
        ("15", "Silikon ayak Ø12,7×3,5", "tabandaki yuvalara", "3"),
        ("16", "NTAG213 Ø25 etiket", "taban altındaki 0,4 mm cebe", "figür başına 1"),
    ]
    for i, (no, ad, aciklama, adet) in enumerate(satirlar):
        y = ly - 6 - i * 5.3
        ax.text(lx, y, no, fontsize=5.5)
        ax.text(lx + 7, y, ad, fontsize=5.5)
        ax.text(lx + 72, y, aciklama, fontsize=5.5)
        ax.text(lx + 175, y, adet, fontsize=5.5)
        ax.plot([lx, lx + 205], [y - 1.4, y - 1.4], lw=0.15, color="#888")
    notlar = [
        "Genel tolerans ±0,2. Boşluklar: yuva–taban 0,4 radyal; halka kanalı 0,4 radyal; dil–oluk 0,2; kartlar 0,25–0,3.",
        "Kenarlar: alt dış pah 3×45°, kapak üst R3. Vidalar alttan, derin havşada gizli.",
        "Ölçüler mm. Bu çizim cad/uret.py ile parametreler.py'den üretilir; elle düzenlemeyin.",
    ]
    for i, n in enumerate(notlar):
        ax.text(lx, 46 - i * 4.5, n, fontsize=5)
    baslik_blok(ax, "MASAL STANDI — teknik çizim", f"A3 · ölçek 1:1 · Ø{P.D_DIS:.0f} × {H_top:.1f} mm · "
                "hikaye-oyuncak/cad · sayfa 1/2")
    for uz in ("svg", "pdf"):
        fig.savefig(os.path.join(KOK, f"teknik_cizim.{uz}"))
    plt.close(fig)


# ---------------------------------------------------------------------------------------------
def patlatilmis(parca):
    yer = yerlestir(parca)
    zarf = pc.zarflar()
    fig, ax = sayfa()
    ox, oy = 110.0, 22.0
    ax.text(25, 280, "PATLATILMIŞ MONTAJ (kesit A–A, x = 0; sol = arka, sağ = ön)  ölçek 1:1", fontsize=8,
            weight="bold")
    katlar = [  # (ad/zarflar, z ötelemesi, balon no, etiket)
        (["govde_alt"], 0, "1", "alt gövde"),
        (["Taşıyıcı pertinaks 5x7", "ESP32-S3-DevKitC-1 (+headerlar)", "ESP32 anten çıkıntısı",
          "Seviye çevirici + 1000 µF + klemensler", "Hoparlör Ø40x20", "USB-C kartı",
          "MAX98357A PCB", "MAX98357A bileşen/klemens", "Pertinaks altı lehim/kablo"], 0, "7–9, 13", "elektronik"),
        (["RC522 PCB", "RC522 bileşenleri (alt)", "rc522_tutucu"], 45, "4, 11", "RC522 + tutucu"),
        (["ust_kapak"], 85, "2", "üst kapak"),
        (["NeoPixel halka Ø104/Ø90"], 112, "12", "NeoPixel halka"),
        (["difuzor_halka"], 135, "3", "difüzör"),
        (["figur_taban", "NTAG213 Ø25"], 168, "5, 16", "figür tabanı + NTAG213"),
    ]
    for adlar, dz, no, et in katlar:
        ymax = None
        for ad in adlar:
            if ad in yer:
                m = yer[ad]
                renk, kenar, hatch = RENK[ad], "k", ("////" if ad != "difuzor_halka" else None)
            else:
                m = zarf[ad]
                renk, kenar, hatch = "#bfe3c5", "#2e6b38", None
            polys = [p + [ox, oy + dz] for p in kesit_x(m)]
            poligon_ciz(ax, polys, renk, kenar=kenar, lw=0.35, hatch=hatch, z=2)
            b = m.bounding_box()
            ymax = b[5] if ymax is None else max(ymax, b[5])
        # balon
        bx_, by_ = ox + 80, oy + dz + (20.0 if et == "elektronik" else ymax - 4)
        ax.add_patch(plt.Circle((bx_ + 9, by_), 4.2, fill=False, lw=0.5))
        ax.text(bx_ + 9, by_, no, fontsize=5, ha="center", va="center")
        ax.text(bx_ + 15, by_, et, fontsize=6, va="center")
        ax.plot([ox + 62, bx_ + 4.8], [by_, by_], lw=0.3, color="k")
    # montaj ekseni
    ax.plot([ox, ox], [oy - 5, oy + 230], lw=0.3, ls="-.", color="k")
    sira = [
        "MONTAJ SIRASI",
        "1  Alt gövdeye 3 silikon ayak; USB-C kartını platforma epoksiyle yapıştır, kabloyu kablo bağıyla sabitle.",
        "2  Hoparlörü (1 mm köpük conta ile) üstten ön bölmeye kaydır, arkaya 3 mm köpük; 4 nokta silikon.",
        "3  MAX98357A'yı dikey kızağa üstten kaydır (klemens aşağıda, hoparlör kablosu bağlı).",
        "4  INMP441'i conta + kart olarak arka pede üstten kaydır (delikli yüz duvara).",
        "5  Taşıyıcı pertinaksı 4 köşe kenetine bastır; DevKit'i dişi headerlara tak.",
        "6  Kapağın 3 deliğine M3 ısıl gömme somunları havya ile göm (230 °C).",
        "7  RC522'yi (bileşen yüzü aşağı) tutucuya koy, tutucuyu 4×M2,5x8 ile kapağa vidala.",
        "8  Halkayı kanala koy (kablo arkadaki yarıktan aşağı), 1000 µF + 330 Ω halka ucunda.",
        "9  Difüzörü bastır (tırnak oturur; kalıcı için 3 nokta şeffaf silikon).",
        "10 Kabloları tak, testleri yap (docs/DONANIM.md), kapağı dil–oluk ile oturt,",
        "   alttan 3×M3x10 ile vidala. Figür tabanlarına NTAG213 yapıştır, figürleri üste yapıştır.",
    ]
    for i, s in enumerate(sira):
        ax.text(245, 270 - i * 6.0, s, fontsize=6 if i else 7, weight="bold" if i == 0 else None)
    png = os.path.join(KOK, "onizleme", "montaj_patlatilmis.png")
    if os.path.exists(png):
        img = plt.imread(png)
        h, w = img.shape[:2]
        gen = 130.0
        ax.imshow(img, extent=(255, 255 + gen, 36, 36 + gen * h / w), zorder=1)
        ax.set_xlim(0, A3[0])
        ax.set_ylim(0, A3[1])
    baslik_blok(ax, "MASAL STANDI — patlatılmış montaj", "A3 · ölçek 1:1 · balon numaraları = teknik çizim "
                "parça listesi · sayfa 2/2")
    for uz in ("svg", "pdf"):
        fig.savefig(os.path.join(KOK, f"patlatilmis_montaj.{uz}"))
    plt.close(fig)


def hepsi(parca):
    teknik_cizim(parca)
    patlatilmis(parca)
