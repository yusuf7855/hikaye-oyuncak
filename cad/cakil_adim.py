"""Çakıl stand: parçaları TEK TEK yerleştirme adımları (ürün sahibi onayladıkça sıradaki) -> cad/onizleme/adim_<n>_<ad>.png

    python cad/cakil_adim.py 1        # 1. adım: boş gövde + LED halka
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

ADIMLAR = [  # (ad, başlık, parçalar, yapılar, taban plakasındaki tutucular)
    ("halka", "NeoPixel halka (iç Ø55, dış Ø70)", ["NeoPixel 16"], ["tutucu"], ()),
    ("nfc", "NFC okuyucu (RC522 / PN5180)", ["RC522 okuyucu"], [], ()),
    ("pil", "Pil kutusu: 4'lü AA, alttan vidalı kapak", ["4xAA yatağı"], ["taban", "pil_kapagi"], ("vida", "ayak", "pil")),
    ("hoparlor", "Hoparlör Ø50 (önden)", ["hoparlör (önden)"], [], ("hoparlor",)),
    ("duzenleyici", "5 V düzenleyici (pil kutusunun tavanında)", ["5 V düzenleyici"], [], ()),
    ("esp32", "ESP32-S3 (ters, jumper'lar üstten)", ["ESP32-S3", "jumper payı"], [], ("esp32",)),
    ("anahtar", "Açma-kapama anahtarı", ["KCD11 anahtar"], [], ()),
    ("amfi", "MAX98357A", ["MAX98357A"], [], ("amfi",)),
]


def kesit_ciz(ax, man, renk, ec, alfa=1.0):
    if man is None or man.is_empty():
        return
    cs = man.rotate([0, -90, 0]).slice(0.0)       # x = 0 düzlemi: (u, v) = (-z, y)
    for poly in cs.to_polygons():
        p = np.asarray(poly)
        ax.add_patch(Polygon(np.c_[p[:, 1], -p[:, 0]], closed=True, fc=renk, ec=ec, lw=1.0, alpha=alfa))


def adim_gorsel(n, notlar=(), nfc="rc522"):
    ad, baslik, parcalar, yapilar, _ = ADIMLAR[n - 1]
    oku = f"{nfc.upper()} okuyucu"
    parcalar = [oku if p == "RC522 okuyucu" else p for p in parcalar]
    z, yapi, sorun, mesafe = C.denetle(nfc)
    yapi = dict(yapi, taban=C.taban(tuple(o for a in ADIMLAR[:n] for o in a[4])))
    onceki_p = [oku if p == "RC522 okuyucu" else p for a in ADIMLAR[:n - 1] for p in a[2]]
    onceki_y = [y for a in ADIMLAR[:n - 1] for y in a[3]]
    fig = plt.figure(figsize=(17, 7.6), dpi=110)
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    yarim = kutu(-80, 0, -80, 80, -5, 80)
    ls = [(yapi["kabuk"] ^ yarim, C.RENK_YAPI["kabuk"], False)]
    ls += [(yapi[y], "#d8d2c8", False) for y in onceki_y]
    ls += [(z[p], "#9a9a9a", False) for p in onceki_p]
    ls += [(yapi[y], "#ffd27a", False) for y in yapilar]
    gercek = {"ESP32-S3": C.esp_stl}
    ls += [(gercek[p]() if p in gercek else z[p], C.RENK_PARCA.get(p, "#e33"), p in ("NeoPixel 16", "jumper payı")) for p in parcalar]
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
    ax2.set_xlabel("y (mm)   ← ARKA                 ÖN (logo) →"); ax2.set_ylabel("z (mm)")
    ax2.set_title("Ortadan yan kesit (x = 0)", fontsize=12)
    fig.suptitle(f"Adım {n}/{len(ADIMLAR)}: {baslik}" + (f" — {nfc.upper()}" if n >= 2 else ""), fontsize=15)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", f"adim_{n}_{ad}" + (f"_{nfc}" if n == 2 else "") + ".png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def ust_gorunus():
    """Çukur yakından: (1) bir pencereden geçen yan kesit, ışık yolu; (2) çukurun iç duvarı açılmış (gündüz / gece)."""
    from matplotlib.patches import Rectangle, FancyArrowPatch
    z, yapi, sorun, mesafe = C.denetle("rc522")
    n, gen = C.ISIK_YARIK
    aci = 360.0 / n * 0.5
    fig, axs = plt.subplots(1, 2, figsize=(16, 6.4), dpi=110, gridspec_kw={"width_ratios": [1, 1.5]})
    ax = axs[0]
    for man, fc, ec in ((yapi["kabuk"], C.RENK_YAPI["kabuk"], "#8a7a66"), (yapi["tutucu"], "#ffd27a", "#b08a30"),
                        (z["NeoPixel 16"], "#ff4fa3", "k")):
        cs = man.rotate([0, 0, -aci]).rotate([90, 0, 0]).slice(0.0)   # pencerenin ortasından geçen düşey kesit (x, z)
        for poly in cs.to_polygons():
            pp = np.asarray(poly)
            ax.add_patch(Polygon(np.c_[pp[:, 0], -pp[:, 1]], closed=True, fc=fc, ec=ec, lw=1))
    for y0 in (C.H - 1.2, C.H - 1.9):
        ax.add_patch(FancyArrowPatch((18.5, y0), (5, y0 - 2.5), arrowstyle="-|>", mutation_scale=14, color="#ff4fa3", lw=1.6))
    ax.text(2, C.H + 1.2, "figür çukuru", fontsize=10)
    ax.text(16, C.H - 7.5, "LED halka\n(LED'ler oyukta)", fontsize=9, color="#b0306f")
    ax.annotate("dikey pencere", xy=(15.0, C.H - 1.6), xytext=(4, C.H - 9), fontsize=10, arrowprops=dict(arrowstyle="->"))
    ax.set_xlim(0, 30); ax.set_ylim(C.H - 12, C.H + 3); ax.set_aspect("equal"); ax.grid(alpha=.25)
    ax.set_title("Bir pencereden geçen kesit (mm): ışık yandan çukura", fontsize=12)
    ax = axs[1]
    cevre = 2 * math.pi * C.YUVA_R
    z0, z1 = C.Z_CANAK_TABAN, C.H
    for gece, yoff in ((False, 0.0), (True, -(z1 - z0) - 2.5)):
        ax.add_patch(Rectangle((0, z0 + yoff), cevre, z1 - z0, fc="#3a3530" if gece else "#F6E7D2", ec="#8a7a66"))
        for i in range(n):
            x = cevre * (i + 0.5) / n
            ax.add_patch(Rectangle((x - gen / 2, C.H - C.DUVAR - 0.2 + yoff), gen, C.DUVAR + 0.2 - C.ISIK_KAL,
                                   fc="#ff4fa3" if gece else "#6b5f52", ec="none"))
        ax.text(cevre + 1.5, z0 + yoff + 1.5, "gece" if gece else "gündüz", fontsize=11)
    ax.set_xlim(-2, cevre + 14); ax.set_ylim(z0 - (z1 - z0) - 4, z1 + 1.5); ax.set_aspect("equal")
    ax.set_yticks([]); ax.set_xlabel("çukurun iç duvarı boyunca (mm, açılmış)")
    ax.set_title(f"Çukurun iç duvarı açılmış: {n} dikey pencere ({gen} mm), üstte 0,6 mm dudak", fontsize=12)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", "adim_1_ust.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def taban_plan(n):
    """Taban plakası üstten: bu adıma kadar konan parçalar, boş kalan alan."""
    from matplotlib.patches import Rectangle
    z, yapi, sorun, mesafe = C.denetle("rc522")
    oz = tuple(o for a in ADIMLAR[:n] for o in a[4])
    tb = C.taban(oz)
    fig, ax = plt.subplots(figsize=(8.6, 8.6), dpi=110)
    from matplotlib.path import Path
    from matplotlib.patches import PathPatch
    cs = tb.slice(1.8)
    verts, codes = [], []
    for poly in cs.to_polygons():
        pp = np.asarray(poly)
        verts += list(pp) + [pp[0]]
        codes += [Path.MOVETO] + [Path.LINETO] * (len(pp) - 1) + [Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), fc="#E8DCCB", ec="#8a7a66", lw=0.8))
    ust = tb.slice(C.TABAN_KAL + 1.5)
    for poly in ust.to_polygons():
        pp = np.asarray(poly)
        ax.add_patch(Polygon(pp, closed=True, fc="#c9b89c", ec="#7a6a55", lw=0.8))
    parca = [p for a in ADIMLAR[:n] for p in a[2] if p in ("4xAA yatağı", "hoparlör (önden)", "5 V düzenleyici", "ESP32-S3", "MAX98357A")]
    for p in parca:
        b = z[p].bounding_box()
        ax.add_patch(Rectangle((b[0], b[1]), b[3] - b[0], b[4] - b[1], fc=C.RENK_PARCA[p] + "88", ec=C.RENK_PARCA[p], lw=2))
        ax.text((b[0] + b[3]) / 2, (b[1] + b[4]) / 2, p, ha="center", va="center", fontsize=10, color="white")
    for x in (-20.0, 20.0):
        ax.annotate("yatağın kablo deliği", xy=(x, C.PIL_Y + C.PIL_IC[1] - 2.5), xytext=(x - 14, C.PIL_Y + C.PIL_IC[1] + 9), fontsize=8,
                    arrowprops=dict(arrowstyle="->"))
    if n < 4:
        ax.text(0, 40, "ön yarı: hoparlör (sonraki adım)", ha="center", fontsize=10, color="#777")
    if n < 6:
        ax.text(0, -50, "arka: ESP32 kutunun üstünde (sonraki adım)", ha="center", fontsize=9, color="#777")
    ax.text(0, 57, "ÖN (logo)", ha="center"); ax.text(0, -60, "ARKA", ha="center")
    ax.set_xlim(-62, 62); ax.set_ylim(-63, 62); ax.set_aspect("equal"); ax.grid(alpha=.25)
    ax.set_title(f"Adım {n}: taban plakası üstten (koyu: tutucu duvarlar)", fontsize=12)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", f"adim_{n}_taban_plan.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def montaj_gorsel():
    """İki modül: üst (kabuk + halka + tutucu + NFC + mikrofon + anahtar) ve alt kapak (pil kutusu, hoparlör, ESP32,
    düzenleyici, amfi)."""
    z, yapi, sorun, mesafe = C.denetle("rc522")
    fig = plt.figure(figsize=(10, 12), dpi=110)
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    yuk = 55.0
    yarim = kutu(-80, 0, -80, 80, -5, 80)
    ls = [((yapi["kabuk"] ^ yarim).translate([0, 0, yuk]), C.RENK_YAPI["kabuk"], False),
          (yapi["tutucu"].translate([0, 0, yuk]), "#ffd27a", False),
          (z["NeoPixel 16"].translate([0, 0, yuk]), "#ff4fa3", True),
          (z["RC522 okuyucu"].translate([0, 0, yuk]), C.RENK_PARCA["RC522 okuyucu"], False),
          (C.taban(), "#E8DCCB", False), (yapi["pil_kapagi"].translate([0, 0, -12]), C.RENK_YAPI["pil_kapagi"], False)]
    for p in ("hoparlör (önden)", "ESP32-S3", "5 V düzenleyici", "MAX98357A"):
        ls.append((z[p], C.RENK_PARCA[p], False))
    etiket = {"hoparlör (önden)": "HOPARLÖR Ø50\n(önden)", "ESP32-S3": "ESP32-S3 (ters)"}
    for p, yazi in etiket.items():
        b = z[p].bounding_box()
        ax.text((b[0] + b[3]) / 2, (b[1] + b[4]) / 2, b[5] + 3, yazi, fontsize=9, ha="center", color="#222",
                bbox=dict(fc="white", ec="none", alpha=.75))
    for aci in C.VIDA_ACILAR:
        x, y = C.VIDA_R * math.cos(math.radians(aci)), C.VIDA_R * math.sin(math.radians(aci))
        ls.append((C.silindir(1.5, -14, -4, x=x, y=y, seg=16) + C.silindir(2.8, -16, -14, x=x, y=y, seg=16), "#555", False))
    elev, azim = 14, 30
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_zlim(-20, 115)
    ax.set_box_aspect((1, 1, 1.15))
    ax.view_init(elev=elev, azim=azim)
    ax.text2D(0.02, 0.86, "ÜST MODÜL (kabuk)\n• LED halka + tutucu plaka (4 direğe vidalı)\n• NFC okuyucu (raylarda)\n"
              "• açma-kapama anahtarı (sol yan duvarda)", transform=ax.transAxes, fontsize=10,
              bbox=dict(fc="white", ec="#b08a30"))
    ax.text2D(0.02, 0.30, "ALT KAPAK\n• pil kutusu: 4'lü AA, alttan vidalı pil kapağı\n• hoparlör Ø50 (önde, dik)\n"
              "• kutunun üstünde: ESP32-S3 (ters; jumper'lar üstten),\n  MAX98357A, 5 V düzenleyici", transform=ax.transAxes, fontsize=10,
              bbox=dict(fc="white", ec="#8a7a66"))
    ax.text2D(0.62, 0.10, "4 x M3 vida alttan\n(kabukta ısıl gömme somun)", transform=ax.transAxes, fontsize=10)
    ax.set_title("Montaj: iki modül ayrı kurulur, kablolar soketle takılır, kabuk alt kapağın üstüne iner", fontsize=11)
    yol = os.path.join(C.KOK, "onizleme", "montaj_iki_modul.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def dis_on():
    """Dışarıdan önden ve yandan: logo, hoparlör ızgarası."""
    k = C.kabuk()
    fig = plt.figure(figsize=(15, 7), dpi=110)
    for i, (elev, azim, bas) in enumerate(((12, 90, "Önden: logo ve hoparlör ızgarası"), (22, 50, "Önden-yandan"))):
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, [(k, C.RENK_YAPI["kabuk"], False)], [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-55, 55); ax.set_ylim(-55, 55); ax.set_zlim(-20, 70)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(bas, fontsize=13)
    plt.subplots_adjust(left=0, right=1, top=0.92, bottom=0, wspace=0)
    yol = os.path.join(C.KOK, "onizleme", "adim_4_dis_on.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def pil_yakin():
    """Pil kutusu yakından: alttan görünüş (kapak, dil yuvaları, vida, ayaklar), kutunun ortasından iki kesit."""
    z, yapi, sorun, mesafe = C.denetle("rc522")
    tb, kp = yapi["taban"], yapi["pil_kapagi"]
    fig = plt.figure(figsize=(21, 7.4), dpi=110)
    ax = fig.add_subplot(1, 3, 1, projection="3d")
    ls = [(tb, "#E8DCCB", False), (kp.translate([0, 0, -8]), C.RENK_YAPI["pil_kapagi"], False)]
    elev, azim = -55, -70
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-55, 55); ax.set_ylim(-55, 55); ax.set_zlim(-30, 30)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Alttan: pil kapağı (8 mm aşağıda gösterildi); solda iki dil, sağda vida", fontsize=11)
    renkler = ((tb, "#E8DCCB", "#8a7a66"), (kp, C.RENK_YAPI["pil_kapagi"], "#7a5a30"), (z["4xAA yatağı"], "#555", "k"),
               (z["ESP32-S3"], "#3a3a3a", "k"), (z["MAX98357A"], C.RENK_PARCA["MAX98357A"], "k"),
               (z["5 V düzenleyici"], C.RENK_PARCA["5 V düzenleyici"], "k"), (yapi["kabuk"], C.RENK_YAPI["kabuk"], "#8a7a66"))
    ax2 = fig.add_subplot(1, 3, 2)
    yk = C.PIL_DIL_Y[1]
    for man, fc, ec in renkler:
        cs = man.translate([0, -yk, 0]).rotate([-90, 0, 0]).slice(0.0)
        for poly in cs.to_polygons():
            pp = np.asarray(poly)
            ax2.add_patch(Polygon(pp, closed=True, fc=fc, ec=ec, lw=1))
    xe = C.PIL_KAPAK_XE
    ax2.annotate("dil plakadaki yuvaya girer", xy=(-xe - 1.5, 1.6), xytext=(-62, 12), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax2.annotate("4 pil (yatak ters: açık yüzü kapağa)", xy=(0, 10), xytext=(-40, 30), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax2.annotate("tavan: yatağın sırtı bantla yapışır", xy=(10, C.Z_PIL_TAVAN + 0.8), xytext=(-25, 42), fontsize=9,
                 arrowprops=dict(arrowstyle="->"))
    ax2.annotate("duvar kapağın kenarına basar", xy=(xe - 0.6, C.TABAN_KAL + 0.2), xytext=(5, -8), fontsize=9,
                 arrowprops=dict(arrowstyle="->"))
    ax2.set_xlim(-64, 64); ax2.set_ylim(-12, 48); ax2.set_aspect("equal"); ax2.grid(alpha=.25)
    ax2.set_xlabel("x (mm)  ← SOL        SAĞ →"); ax2.set_title("Soldaki dilden geçen enine kesit", fontsize=12)
    ax3 = fig.add_subplot(1, 3, 3)
    xv, yv = C.PIL_VIDA_XY
    for man, fc, ec in renkler[:3] + renkler[6:]:
        cs = man.translate([0, -yv, 0]).rotate([-90, 0, 0]).slice(0.0)
        for poly in cs.to_polygons():
            pp = np.asarray(poly)
            ax3.add_patch(Polygon(pp, closed=True, fc=fc, ec=ec, lw=1))
    ax3.add_patch(Polygon([(xv - 3.0, 0), (xv + 3.0, 0), (xv + 1.5, 1.5), (xv + 1.5, 8.0), (xv - 1.5, 8.0), (xv - 1.5, 1.5)],
                          closed=True, fc="#9aa3ad", ec="k", lw=1))
    ax3.annotate("M3 x 8 havşa vida", xy=(xv + 2.0, 0.6), xytext=(xv - 2, -9), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax3.annotate("M3 ısıl gömme somun\n(alttan takılır)", xy=(xv + 1.8, 5.0), xytext=(xv - 14, 24), fontsize=9,
                 arrowprops=dict(arrowstyle="->"))
    ax3.annotate("tırnak çentiği: kapağı\nburadan kaldır", xy=(xv + 6.0, 0.4), xytext=(xv - 4, 14), fontsize=9,
                 arrowprops=dict(arrowstyle="->"))
    ax3.set_xlim(xv - 22, xv + 14); ax3.set_ylim(-12, 30); ax3.set_aspect("equal"); ax3.grid(alpha=.25)
    ax3.set_xlabel("x (mm)"); ax3.set_title("Sağdaki vidadan geçen enine kesit", fontsize=12)
    fig.suptitle("Adım 3: pil kutusu — kapak taban plakasıyla aynı hizada, açmak için tornavida gerekir", fontsize=14)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", "adim_3_pil_yakin.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def esp_yakin():
    """ESP32 yuvası yakından: üstten (jumper'lar), USB-C ucundan kesit, uzunlamasına kesit."""
    z, yapi, sorun, mesafe = C.denetle("rc522")
    tb = C.taban()
    k = yapi["kabuk"]
    xc, yc = C.ESP_XY
    fig = plt.figure(figsize=(21, 7.4), dpi=110)
    ax = fig.add_subplot(1, 3, 1, projection="3d")
    kirp = kutu(-45, 45, -62, -10, -2, 50)
    ls = [(tb ^ kirp, "#E8DCCB", False), (C.esp_stl(), "#2b2b2b", False), (z["jumper payı"], "#e8a33d", True)]
    elev, azim = 32, -62
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-42, 42); ax.set_ylim(-74, 10); ax.set_zlim(-5, 45)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Pil kutusunun üstünde ters ESP32; turuncu: J1 jumper'ları için boş alan", fontsize=11)
    for i, (xk, baslik) in enumerate(((xc, "Kartın ortasından enine kesit"), (xc + 29.4, "USB-C ucundan enine kesit (köşe kancaları)"))):
        ax2 = fig.add_subplot(1, 3, 2 + i)
        for man, fc, ec in ((k, C.RENK_YAPI["kabuk"], "#8a7a66"), (tb, "#E8DCCB", "#8a7a66"), (z["ESP32-S3"], "#3a3a3a", "k"),
                            (z["jumper payı"], "#e8a33d55", "#c07a10"), (z["4xAA yatağı"], "#555", "k")):
            cs = man.translate([-xk, 0, 0]).rotate([0, -90, 0]).slice(0.0)
            for poly in cs.to_polygons():
                pp = np.asarray(poly)
                ax2.add_patch(Polygon(np.c_[pp[:, 1], -pp[:, 0]], closed=True, fc=fc, ec=ec, lw=1))
        if i == 0:
            ax2.annotate("J1 jumper'ları\n(14 mm + büküm)", xy=(yc + 12.8, C.ESP_Z + 14), xytext=(yc - 14, C.ESP_Z + 15), fontsize=9,
                         arrowprops=dict(arrowstyle="->"))
            ax2.annotate("pil kutusunun tavanı", xy=(yc + 8, C.Z_PIL_UST - 0.8), xytext=(yc + 5, 4), fontsize=9,
                         arrowprops=dict(arrowstyle="->"))
            ax2.annotate("iç kiriş: kartı pin\nsırasının içinden taşır", xy=(yc + 11.3, C.ESP_Z - 0.5), xytext=(yc + 6, C.ESP_Z - 14), fontsize=9,
                         arrowprops=dict(arrowstyle="->"))
            ax2.annotate("bileşenler aşağı bakar", xy=(yc, C.ESP_Z - 2), xytext=(yc - 12, C.ESP_Z + 8), fontsize=9,
                         arrowprops=dict(arrowstyle="->"))
        else:
            ax2.annotate("köşe kancası: kartın ucu\naltına kayar", xy=(yc - 13.5, C.ESP_Z + 2.0), xytext=(yc - 30, C.ESP_Z + 18), fontsize=9,
                         arrowprops=dict(arrowstyle="->"))
            ax2.annotate("ortası açık: USB-C fişi takılır\n(kod yüklemek için, taban açıkken)", xy=(yc, C.ESP_Z - 1.6), xytext=(yc - 6, C.ESP_Z + 10),
                         fontsize=9, arrowprops=dict(arrowstyle="->"))
        ax2.set_xlim(yc - 30, yc + 30); ax2.set_ylim(-2, 50); ax2.set_aspect("equal"); ax2.grid(alpha=.25)
        ax2.set_xlabel("y (mm)  ← ARKA        ÖN →"); ax2.set_title(baslik, fontsize=12)
    fig.suptitle("Adım 6: ESP32-S3 — pil kutusunun üstünde ters yatar, J1 öne bakar, jumper'lar yukarıdan; anten ucunda tırnak", fontsize=14)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", "adim_6_esp32_yakin.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def anahtar_yakin():
    """Açma-kapama: dışarıdan görünüş ve anahtar ekseninden kesit (flanş oturma yüzü, içte düz panel)."""
    z, yapi, sorun, mesafe = C.denetle("rc522")
    k = yapi["kabuk"]
    a = C.ANAHTAR_ACI
    dd, derin, fd, fk, pk = C.PARCA["kcd11"]
    x_otur, x_ic = C.anahtar_yer()
    fig = plt.figure(figsize=(18, 7.4), dpi=110)
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ar = math.radians(a)
    kirp = kutu(-90, 90, -90, 90, -2, 60).rotate([0, 0, 0])
    ls = [(k ^ kirp, C.RENK_YAPI["kabuk"], False), (z["KCD11 anahtar"], "#111111", False)]
    elev, azim = 8, a
    e, aa = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(aa), math.cos(e) * math.sin(aa), math.sin(e)])
    cx, cy = 58 * math.cos(ar), 58 * math.sin(ar)
    ax.set_xlim(cx - 32, cx + 32); ax.set_ylim(cy - 32, cy + 32); ax.set_zlim(-14, 50)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Sol yandan: anahtar gövdenin dik yerinde (yerden 17 mm)", fontsize=12)
    ax2 = fig.add_subplot(1, 2, 2)
    for man, fc, ec in ((k, C.RENK_YAPI["kabuk"], "#8a7a66"), (C.taban(), "#E8DCCB", "#8a7a66"), (z["KCD11 anahtar"], "#3a3a3a", "k")):
        cs = man.rotate([0, 0, -a]).rotate([-90, 0, 0]).slice(0.0)
        for poly in cs.to_polygons():
            pp = np.asarray(poly)
            ax2.add_patch(Polygon(pp, closed=True, fc=fc, ec=ec, lw=1))
    ax2.annotate(f"flanş (Ø{fd:.1f}) düz oturma yüzünde;\nyüzey ortada {C.dis_r(C.ANAHTAR_Z) - x_otur:.1f} mm gömülü, dışa ek yok",
                 xy=(x_otur + fk / 2, C.ANAHTAR_Z + fd / 2 - 0.5), xytext=(x_otur - 14, C.ANAHTAR_Z + 20), fontsize=9,
                 arrowprops=dict(arrowstyle="->"))
    ax2.annotate(f"içte düz panel {pk:.1f} mm:\nyan tırnaklar buraya kenetlenir", xy=(x_ic, C.ANAHTAR_Z - dd / 2 - 1),
                 xytext=(x_ic - 26, C.ANAHTAR_Z - 18), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax2.annotate(f"gövde + uçlar (~{derin:.0f} mm, tahmin)", xy=(x_ic - derin / 2, C.ANAHTAR_Z), xytext=(x_ic - 30, C.ANAHTAR_Z + 9),
                 fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax2.set_xlim(x_otur - 34, x_otur + 10); ax2.set_ylim(-2, 42); ax2.set_aspect("equal"); ax2.grid(alpha=.25)
    ax2.set_xlabel("anahtar ekseni boyunca (mm, merkezden)  → DIŞ"); ax2.set_ylabel("z (mm)")
    ax2.set_title("Anahtarın ekseninden kesit", fontsize=12)
    fig.suptitle(f"Adım 7: KCD11 açma-kapama — sol yan duvar ({a:.0f}°), Ø{dd:.0f} delik; ölçüler tahmin, anahtar gelince ölçülecek", fontsize=14)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", "adim_7_anahtar_yakin.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def nfc_plan():
    """Üstten: iki okuyucunun yeri, anten bölgesi, figür etiketi (Ø25), çukur, halka, direkler, raylar."""
    from matplotlib.patches import Rectangle, Circle
    fig, axs = plt.subplots(1, 2, figsize=(15, 7.4), dpi=110)
    th = np.linspace(0, 2 * np.pi, 200)
    for ax, nfc in zip(axs, ("rc522", "pn5180")):
        w, d, pcb, alt = C.PARCA[nfc]
        cx, cy = -C.ANTEN_KAYMA[nfc][0], -C.ANTEN_KAYMA[nfc][1]
        r_ic = C.ic_r(C.Z_OKUYUCU_UST)
        ax.plot(r_ic * np.cos(th), r_ic * np.sin(th), color="#8a7a66", lw=1.5, label="gövde iç duvarı (bu yükseklikte)")
        ax.add_patch(Rectangle((cx - w / 2, cy - d / 2), w, d, fc="#1f6f3f33" if nfc == "rc522" else "#1f4f8f33",
                               ec="#1f6f3f" if nfc == "rc522" else "#1f4f8f", lw=2))
        (ax_, ay_), (aw, ah) = C.ANTEN_GERCEK[nfc]
        ax.add_patch(Rectangle((cx + ax_ - aw / 2, cy + ay_ - ah / 2), aw, ah, fc="none", ec="#d08000", lw=1.5, ls="--"))
        ax.text(cx + ax_ - aw / 2 + 1, cy + ay_ + ah / 2 - 3, "anten bölgesi (tahmin)", fontsize=8, color="#d08000")
        ax.text(cx + w / 2 - 2, cy, "pinler", rotation=90, va="center", ha="right", fontsize=8) if nfc == "rc522" else \
            ax.text(cx - w / 2 + 2, cy, "pinler / elektronik", rotation=90, va="center", ha="left", fontsize=8)
        ri, rd, k = C.PARCA["halka"]
        for r in (ri / 2, rd / 2):
            ax.plot(r * np.cos(th), r * np.sin(th), color="#ff4fa3", lw=1.5)
        ax.add_patch(Circle((0, 0), C.YUVA_R, fc="none", ec="#8a7a66", lw=1.2, ls=":"))
        ax.add_patch(Circle((0, 0), 12.5, fc="#2060ff33", ec="#2060ff", lw=1.5))
        ax.text(0, 0, "etiket\nØ25", ha="center", va="center", fontsize=9, color="#2060ff")
        for aci in C.UST_ACILAR:
            x, y = C.UST_DIREK_R * math.cos(math.radians(aci)), C.UST_DIREK_R * math.sin(math.radians(aci))
            ax.add_patch(Circle((x, y), 3.5, fc="#ffd27a", ec="#b08a30"))
        for s in (-1, 1):
            y_ic = cy + s * (d / 2 + 0.3)
            ax.add_patch(Rectangle((cx - w / 2 + 6, min(y_ic, y_ic + s * 2)), w - 12, 2, fc="#ffd27a", ec="#b08a30"))
        ax.annotate("kart bu yönden\nraylara kayar", xy=(cx + w / 2, cy), xytext=(cx + w / 2 + 3, cy + 22), fontsize=9,
                    arrowprops=dict(arrowstyle="<-", lw=1.5))
        ax.text(cx, cy - d / 2 - 4, f"{nfc.upper()} {w:.0f} x {d:.0f} mm", ha="center", fontsize=10)
        ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_aspect("equal"); ax.grid(alpha=.25)
        ax.set_title(f"{nfc.upper()}: anten figür etiketinin altında, etiket–anten ≈ {C.denetle(nfc)[3]:.1f} mm", fontsize=12)
        ax.text(0, 56, "ÖN", ha="center"); ax.text(0, -59, "ARKA", ha="center")
    fig.suptitle("Adım 2/9: NFC okuyucu — üstten (sarı: tutucu direkleri ve raylar, pembe: halka, mavi: figürdeki etiket)",
                 fontsize=12)
    plt.tight_layout(rect=(0, 0, 1, 0.95))
    yol = os.path.join(C.KOK, "onizleme", "adim_2_nfc_ustten.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "montaj":
        print(montaj_gorsel())
        sys.exit(0)
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    notlar = {
        1: [(-19, C.Z_HALKA_UST - 0.8, "LED halka çukurun ÇEVRESİNDE, tavana yaslı, çukura sıkı geçer;\nLED'ler tavandaki ışık oyuğuna girer", -60, 22),
            (-15.4, C.H - 1.6, "çukurun dikey duvarı şerit şerit açık:\nLED ışığı yandan çukura girer", 16, 31),
            (24, C.Z_TUTUCU_ALT + 1, "tutucu plaka halkayı alttan tavana bastırır\n(4 direğe M2,5 vida); ortası çukura açık", 6, 8),
            (-8, C.Z_CANAK_TABAN, f"figür çukuru Ø{2 * C.YUVA_R:.1f} (figür tabanı Ø{C.FIGUR_TABAN_D:.0f}), halkanın ortasından geçer", -55, 62)],
        2: [(0, C.Z_OKUYUCU_UST - 0.8, "NFC okuyucu: anten yüzü çukur zemininin 0,3 mm altında", -60, 30),
            (0, C.Z_CANAK_TABAN + 0.4, f"figür etiketi -> anten ≈ {(C.Z_CANAK_TABAN + 0.4) - C.Z_OKUYUCU_UST:.1f} mm", 8, 62),
            (-21, C.Z_OKUYUCU_UST - 2.5, "tutucunun rayları (kart kayarak girer)", -62, 18)],
        3: [(0, C.TABAN_KAL + 9, "4 x AA yatağı (62,5 x 58 x 15,5, tahmin):\nters durur, piller alttan takılır", -62, 40),
            (0, C.Z_PIL_TAVAN + 0.8, "kutunun tavanı (yatağın sırtı bantla yapışır)", 2, 30),
            (0, 1.2, "pil kapağı (taban plakasıyla aynı hizada)", 10, -2)],
        4: [(0, C.HOP_ZC + 12, "hoparlör Ø50, dik, öne bakar\n(ön çerçeve + mıknatıs, tahmin)", -62, 44),
            (C.HOP_YF + 6, C.HOP_ZC + 20, "ses yakası: hoparlörden ızgaraya boru", 2, 60),
            (C.HOP_YF + 9, C.HOP_ZC - 6, "ön duvarda ızgara", 20, 12),
            (C.HOP_YF - 2, C.TABAN_KAL + 2, "beşik (taban plakasında)", -10, 4)],
        5: [(C.DUZ_XY[1], C.Z_PIL_UST + 3, "5 V düzenleyici (sol, kesitin arkasında):\npil -> anahtar -> düzenleyici -> 5 V", -62, 40)],
        6: [(C.ESP_XY[1], C.ESP_Z + 0.8, "ESP32-S3 TERS: bileşenler aşağı, pinler yukarı", 0, 46),
            (C.ESP_XY[1] - 12.8, C.ESP_Z + 20, "jumper payı: dişi jumper (14 mm)\n+ kablo bükümü, yukarıdan takılır", -64, 52),
            (C.ESP_XY[1] + 13, C.ESP_Z - 2, "kanal: iç kiriş kartı taşır, dış duvar yandan tutar;\nöndeki kanal pil kutusunun tavanında", -10, 6)],
    }.get(n, [])
    if n == 2:
        for nfc in ("rc522", "pn5180"):
            print(adim_gorsel(n, notlar, nfc))
        print(nfc_plan())
    else:
        print(adim_gorsel(n, notlar))
    if n == 1:
        print(ust_gorunus())
    if n >= 3:
        print(taban_plan(n))
    if n == 4:
        print(dis_on())
    if n == 3:
        print(pil_yakin())
    if n == 6:
        print(esp_yakin())
    if n == 7:
        print(anahtar_yakin())
