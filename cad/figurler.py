"""Figür tabanları: her figür için vidalı NFC kapaklı taban (baskıya hazır, figür başına tek dosya).

    python cad/figurler.py      # cad/stl_cakil/figurler/*.stl + cad/onizleme/figurler.png

Figür listesi data/figur_donanim.json'dan (nfc_no kartın etikete yazdığı numaradır). Her dosyada iki parça yan yana:
  taban (ters: düz üst yüz tablada, dişli oyuk yukarı) + kapak (alt yüzü tablada; altında figür adı ve numarası).
Ay Dede (gece) tabanı üstünde hilal ayla tek parça (dik basılır); ayar kartı topuzlu taban (dik basılır).
Lisanslı karakterlerin kendisi (Niloya, Elsa ...) çizilmez: hazır oyuncak figür tabanın düz üst yüzüne yapıştırılır.
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402

DEPO = os.path.dirname(C.KOK)
CIKTI = os.path.join(C.KOK, "stl_cakil", "figurler")


def figur_listesi():
    with open(os.path.join(DEPO, "data", "figur_donanim.json"), encoding="utf-8") as f:
        d = json.load(f)
    return d["figurler"], d.get("ozel_kartlar", [])


def tabla(parcalar, bosluk=5.0):
    """[(manifold, ters_mi)] -> aralarında bosluk mm kalacak biçimde yan yana, z = 0'dan başlayan tek manifold."""
    out, x = None, 0.0
    for m, ters in parcalar:
        m = m.rotate([180, 0, 0]) if ters else m
        b = m.bounding_box()
        m = m.translate([x - b[0], -(b[1] + b[4]) / 2, -b[2]])
        x += (b[3] - b[0]) + bosluk
        out = m if out is None else out + m
    return out


def uret():
    os.makedirs(CIKTI, exist_ok=True)
    for eski in os.listdir(CIKTI):
        if eski.endswith(".stl"):
            os.remove(os.path.join(CIKTI, eski))
    figs, ozel = figur_listesi()
    taban = C.figur_taban()
    dosyalar = []
    for f in figs:
        no, ad = f["nfc_no"], f["ad"]
        kapak = C.figur_kapak(ad.replace("i", "İ").replace("ı", "I").upper(), no)
        if f.get("mod") == "uyku":
            govde = (C.ay_dede(), False)
        else:
            govde = (taban, True)
        m = tabla([govde, (kapak, False)])
        yol = os.path.join(CIKTI, f"{no:02d}_{f['kimlik']}.stl")
        C._tm(m).export(yol)
        dosyalar.append((yol, ad, no))
    for o in ozel:
        if o["kimlik"] == "ayar":
            m = tabla([(C.figur_taban(topuz=True), False), (C.figur_kapak("AYAR", o["nfc_no"]), False)])
            yol = os.path.join(CIKTI, f"{o['nfc_no']}_ayar_karti.stl")
            C._tm(m).export(yol)
            dosyalar.append((yol, "Ayar kartı", o["nfc_no"]))
    C._tm(tabla([(taban, True)])).export(os.path.join(CIKTI, "bos_figur_taban.stl"))
    C._tm(tabla([(C.figur_kapak(), False)])).export(os.path.join(CIKTI, "bos_kapak.stl"))
    return dosyalar


def onizle():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    import dis_konsept as K
    figs, _ = figur_listesi()
    taban, kapak = C.figur_taban(), C.figur_kapak("NİLOYA", 1)
    fig = plt.figure(figsize=(20, 11), dpi=100)
    # 1) taban + kapak ayrı (patlatılmış), alttan eğik
    ax = fig.add_subplot(2, 3, 1, projection="3d")
    e, a = math.radians(-30), math.radians(35)
    K.ciz(ax, [(taban.translate([0, 0, 14]), "#1FB5B0", False), (kapak.translate([0, 0, -2]), "#F6C33B", False)],
          [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-18, 18); ax.set_ylim(-18, 18); ax.set_zlim(-8, 28); ax.view_init(-30, 35)
    ax.set_title("Taban (turkuaz) ve vidalı kapak (sarı)\nalttan bakış: kapak tabana şişe kapağı gibi döner", fontsize=11)
    # 2) kapak alttan: ad, numara, para yarığı
    ax = fig.add_subplot(2, 3, 2)
    for p in kapak.slice(0.2).to_polygons():
        p = np.asarray(p)
        ax.add_patch(Polygon(np.c_[-p[:, 0], p[:, 1]], closed=True, fc="#F6C33B", ec="#8a6a10", lw=0.6))
    ax.set_xlim(-16, 16); ax.set_ylim(-16, 16); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("Kapağın alt yüzü (alttan bakınca okunur):\nbozuk para yarığı, figür adı, NFC numarası", fontsize=11)
    # 3) kesit: standın çukurunda, kapak takılı, etiket
    ax = fig.add_subplot(2, 3, 3)
    z, yapi, sorun, mesafe = C.denetle("rc522")
    for man, fc, ec in ((yapi["kabuk"], "#F6E7D2", "#8a7a66"), (taban.translate([0, 0, C.Z_CANAK_TABAN]), "#1FB5B0", "#0b6f6b"),
                        (kapak.translate([0, 0, C.Z_CANAK_TABAN]), "#F6C33B", "#8a6a10"), (z["RC522 okuyucu"], "#1f6f3f", "k"),
                        (z["NeoPixel 16"], "#ff4fa3", "k")):
        cs = man.rotate([0, -90, 0]).slice(0.0)
        for p in cs.to_polygons():
            p = np.asarray(p)
            ax.add_patch(Polygon(np.c_[p[:, 1], -p[:, 0]], closed=True, fc=fc, ec=ec, lw=0.6))
    ze = C.Z_CANAK_TABAN + C.KAPAK_TABAN
    ax.plot([-C.ETIKET_CAP / 2, C.ETIKET_CAP / 2], [ze + 0.15, ze + 0.15], color="#d40000", lw=3)
    ax.annotate(f"Ø{C.ETIKET_CAP:.0f} NFC etiketi\n(antene {mesafe:.1f} mm)", xy=(6, ze + 0.2), xytext=(8, 34), fontsize=10,
                arrowprops=dict(arrowstyle="->"))
    ax.set_xlim(-30, 30); ax.set_ylim(36, 66); ax.set_aspect("equal"); ax.grid(alpha=.2)
    ax.set_title("Standda: taban çukura oturur, etiket antenin hemen üstünde", fontsize=11)
    # 4) tüm figür dosyaları (tablada)
    ax = fig.add_subplot(2, 3, (4, 6))
    ax.axis("off")
    satir = [f"{f['nfc_no']:>3}  {f['ad']:<14} {f['nfc_no']:02d}_{f['kimlik']}.stl" + ("   (Ay Dede: hilal ay tabanla tek parça)" if f.get("mod") == "uyku" else "")
             for f in figs] + ["200  Ayar kartı     200_ayar_karti.stl   (topuzlu taban)"]
    ax.text(0.0, 1.0, "No   Figür          Dosya (taban + adlı kapak, tablada yan yana)\n" + "\n".join(satir), family="monospace",
            fontsize=12, va="top")
    ay = C.ay_dede()
    ax2 = fig.add_axes([0.70, 0.04, 0.27, 0.42], projection="3d")
    e, a = math.radians(15), math.radians(60)
    K.ciz(ax2, [(ay, "#F6C33B", False)], [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax2.set_xlim(-20, 20); ax2.set_ylim(-20, 20); ax2.set_zlim(0, 42); ax2.view_init(15, 60)
    ax2.set_title("Ay Dede (gece figürü)", fontsize=11)
    fig.suptitle("Figür tabanları: Ø52 taban + şişe kapağı gibi vidalanan NFC kapağı (Ø25 etiket)", fontsize=16, fontweight="bold")
    yol = os.path.join(C.KOK, "onizleme", "figurler.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


if __name__ == "__main__":
    import trimesh
    for yol, ad, no in uret():
        t = trimesh.load(yol)
        print(f"{no:>3} {ad:<14} {os.path.basename(yol):<26} {'su geçirmez' if t.is_watertight else 'AÇIK'}  "
              f"{len(t.split(only_watertight=False))} parça  {t.extents.round(1)}")
    print(onizle())
