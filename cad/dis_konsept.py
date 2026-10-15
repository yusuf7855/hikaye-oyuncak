"""Standın dış görünüş konseptleri (yalnız dış kabuk; iç yuvalar sonra) -> cad/onizleme/dis_konsept_*.png

Üç form aynı ölçü kabuğuna oturur (Ø120 mm taban, ~55 mm yükseklik; içine 18650 yatağı, 50x50 hoparlör, ESP32,
RC522/PN5180 ve 16'lı halka sığacak hacim):
  A "çakıl"  : yumuşak, en geniş yeri altta, büyük üst yuvarlatma
  B "kubbe"  : yukarı doğru daralan, hafif kubbeli üst, yanında ay ve yıldız kabartması
  C "pasta"  : iki katlı, katlar arasında ince oluk
Ortak: üstte figür yuvası (Ø63) beyaz yarı saydam bir "çanak" (ayrı parça, beyaz PETG): altındaki 16'lı halka
yandığında çanağın tabanı ve figürün çevresindeki kenarı (hale) parlar. Yuvanın önünde kabartma "eco ai" yazısı,
önde yıldız desenli hoparlör ızgarası, arkada açma-kapama anahtarı (Ø15) ve USB-C şarj girişi.

    python cad/dis_konsept.py            # üç konseptin önizlemesi
"""
import math
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geometri import M, CS, dondur, silindir, xz_den_y_ye, yazi_duz, yildiz, hilal, trimesh_e, yuvarlak_dikdortgen  # noqa: E402

KOK = os.path.dirname(os.path.abspath(__file__))
CIKTI = os.path.join(KOK, "onizleme")
FONT = os.path.join(KOK, "font", "Fredoka.ttf")   # SIL Open Font License (Google Fonts)
SEG = 160

R = 60.0            # en geniş yarıçap
H = 55.0            # toplam yükseklik
YUVA_R = 31.6       # figür tabanı Ø62 + pay
YUVA_DERIN = 6.0
CANAK_R = 34.0      # yarı saydam çanağın dış yarıçapı (hale: YUVA_R..CANAK_R)
YAZI = "eco ai"
YAZI_BOY = 15.0


def _yuvarlak(p0, merkez, r, a0, a1, n=24):
    return [(merkez[0] + r * math.cos(math.radians(a)), merkez[1] + r * math.sin(math.radians(a)))
            for a in np.linspace(a0, a1, n)]


def profil_cakil():
    """Çakıl taşı: süperelips (r yarı ekseni 60, z yarı ekseni 42, merkez z=20), altı ve üstü düz kesilir."""
    zc, b, n = 20.0, 42.0, 2.8
    pts = [(0, 0)]
    for z in np.linspace(0, H, 60):
        u = abs(z - zc) / b
        pts.append((R * max(0.0, 1 - u ** n) ** (1 / n), z))
    r0 = pts[1][0]
    pts.insert(1, (r0 - 2.0, 0))       # alt kenarda küçük pah
    pts[2] = (r0, 2.0)
    pts.append((0, H))
    return pts


def profil_kubbe():
    """Kubbe: taban r=60, üst r=50'ye daralır; üst hafif kubbe (kenarda H-3, ortada H)."""
    pts = [(0, 0), (57, 0)]
    pts += _yuvarlak(None, (57, 3), 3, -90, 0, 8)[1:]
    for z in np.linspace(4, H - 9, 12):
        pts.append((60 - 9 * ((z - 3) / (H - 12)) ** 1.6, z))
    r_son, z_son = pts[-1]
    pts += [(r_son - 5 + 5 * math.cos(a), z_son + 5 * math.sin(a)) for a in np.linspace(0.15, math.pi / 2, 10)]
    r2, z2 = pts[-1]
    for r in np.linspace(r2 - 1, 0, 20):
        pts.append((r, z2 + (H - z2) * (1 - (r / r2) ** 2)))
    return pts


def profil_pasta():
    """İki katlı: alt kat r=60 (z 0..30), oluk, üst kat r=50 (z 31..H), yumuşak kenarlar."""
    pts = [(0, 0), (57, 0)]
    pts += _yuvarlak(None, (57, 3), 3, -90, 0, 8)[1:]
    pts += [(60, 26)]
    pts += _yuvarlak(None, (56, 26), 4, 0, 90, 10)[1:]         # alt katın üst kenarı
    pts += [(52, 30), (52, 30.0), (51.0, 31.5)]                 # oluk
    pts += [(50, 32)]
    pts += _yuvarlak(None, (44, H - 6), 6, 0, 90, 12)
    pts += [(0, H)]
    return pts


def ust_z(profil, r):
    """Profilin r yarıçapındaki üst yüz yüksekliği (yaklaşık; üst kenarlar için)."""
    ust = [(pr, pz) for pr, pz in profil if pz > H * 0.6]
    ust.sort()
    rs = [p[0] for p in ust]
    zs = [p[1] for p in ust]
    return float(np.interp(r, rs, zs))


def kabuk(profil, ad):
    govde = dondur(profil, SEG)
    zu = ust_z(profil, 0)
    # figür yuvası + çanak (ayrı parça): kabukta Ø68 delik, çanak içinde Ø63 yuva
    delik = silindir(CANAK_R + 0.2, zu - YUVA_DERIN - 3, zu + 5, seg=SEG)
    govde = govde - delik
    canak = (silindir(CANAK_R, zu - YUVA_DERIN - 2.0, zu, seg=SEG)
             - silindir(YUVA_R, zu - YUVA_DERIN, zu + 1, seg=SEG))
    canak = canak + (silindir(YUVA_R + 1.2, zu - YUVA_DERIN - 2.0, zu - YUVA_DERIN, seg=SEG))
    # ön yüzde kabartma "eco ai" logosu (yan duvarın eğimini izler, 1,2 mm kabarık)
    z_yazi = {"cakil": 37.0, "kubbe": 36.0, "pasta": 41.5}[ad]
    yazi = yazi_duz(YAZI, YAZI_BOY, FONT, ayna=True)  # +y önden bakınca x ters görünür
    dis = dondur([(p[0] + 1.2, p[1]) for p in profil] + [(0, 0)], SEG)
    yazi3 = (xz_den_y_ye(yazi, 0, 80, x=0, z=z_yazi) ^ dis) - dondur(profil, SEG)
    # ön hoparlör ızgarası: ortada yıldız, çevresinde iki halka yuvarlak delik
    z_h = {"cakil": 17.0, "kubbe": 16.0, "pasta": 14.0}[ad]
    izgara = yildiz(0, 0, 5.5, 2.4)
    for k, (rr, n, d) in enumerate(((9.0, 9, 2.4), (14.0, 14, 2.4))):
        for i in range(n):
            a = 2 * math.pi * (i + 0.5 * k) / n
            izgara = izgara + CS.circle(d / 2, 24).translate([rr * math.cos(a), rr * math.sin(a)])
    govde = govde - xz_den_y_ye(izgara, 40, 70, x=0, z=z_h)
    # arka: açma-kapama anahtarı (Ø15) ve USB-C (9,5 x 3,6)
    govde = govde - xz_den_y_ye(CS.circle(7.5, 48), -70, -40, x=-18, z=22)
    govde = govde - xz_den_y_ye(yuvarlak_dikdortgen(9.6, 3.8, 1.6), -70, -40, x=14, z=9)
    # mikrofon deliği (üst, arka)
    govde = govde - silindir(0.9, zu - 20, zu + 5, x=0, y=-(CANAK_R + 6), seg=16)
    sus = None
    if ad == "kubbe":  # yanda ay ve yıldızlar kabartması (sol ön)
        motif = hilal(0, 0, 7.0, 3.2, aci=20) + yildiz(11, 5, 3.0, 1.3) + yildiz(8, -6, 2.2, 1.0)
        m3d = xz_den_y_ye(motif.mirror([1, 0]), 0, 80, x=0, z=0)
        m3d = m3d.rotate([0, 0, 42]).translate([0, 0, 22])
        dis = dondur([(p[0] + 0.9, p[1]) for p in profil] + [(0, 0)], SEG)
        sus = (m3d ^ dis) - dondur(profil, SEG)
    return govde, canak, yazi3, sus


def ciz(ax, parcalar, kamera):
    kam = np.array(kamera, float); kam /= np.linalg.norm(kam)
    isik = np.array([0.3, 0.55, 0.78]); isik /= np.linalg.norm(isik)
    hepsi_v, hepsi_c = [], []
    for man, renk, parla in parcalar:
        if man is None or man.is_empty():
            continue
        m = trimesh_e(man)
        v = m.vertices[m.faces]
        n = m.face_normals
        on = n @ kam > -0.05
        v, n = v[on], n[on]
        k = (0.42 + 0.58 * np.clip(n @ isik, 0, 1)) if not parla else (0.88 + 0.12 * np.clip(n @ isik, 0, 1))
        c = np.array(matplotlib.colors.to_rgb(renk))
        hepsi_v.append(v)
        hepsi_c.append(np.clip(c[None, :] * k[:, None], 0, 1))
    v = np.concatenate(hepsi_v)
    c = np.concatenate(hepsi_c)
    pc = Poly3DCollection(v, facecolors=c, edgecolors="none", linewidths=0)
    ax.add_collection3d(pc)
    ax.set_xlim(-52, 52); ax.set_ylim(-52, 52); ax.set_zlim(-18, 72)
    ax.set_box_aspect((1, 1, 0.93))
    ax.set_axis_off()


KONSEPTLER = [
    ("A — Çakıl", "cakil", profil_cakil, "#F6E7D2", "#F2A65A"),
    ("B — Kubbe (ay ve yıldızlar)", "kubbe", profil_kubbe, "#DCE8F5", "#3B3FD8"),
    ("C — Pasta (iki katlı)", "pasta", profil_pasta, "#FBE3EA", "#E8607E"),
]


def main():
    os.makedirs(CIKTI, exist_ok=True)
    sonuc = []
    for baslik, ad, pf, govde_renk, yazi_renk in KONSEPTLER:
        govde, canak, yazi, sus = kabuk(pf(), ad)
        sonuc.append((baslik, ad, [(govde, govde_renk, False), (canak, "#FFF6C9", True), (yazi, yazi_renk, False),
                                   (sus, yazi_renk, False)]))
    # önden (çocuğun gördüğü), arkadan ve üstten
    for gorunum, elev, azim in (("on", 24, 90), ("arka", 22, -90), ("ust", 70, 90)):
        fig = plt.figure(figsize=(18, 6.6), dpi=110)
        for i, (baslik, ad, parcalar) in enumerate(sonuc):
            ax = fig.add_subplot(1, 3, i + 1, projection="3d")
            e, a = math.radians(elev), math.radians(azim)
            kam = [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)]
            ciz(ax, parcalar, kam)
            ax.view_init(elev=elev, azim=azim)
            ax.set_title(baslik, fontsize=15, pad=0)
        fig.suptitle({"on": "Dış konseptler — önden (Ø120 × 55 mm; çanak: yarı saydam beyaz, altında 16'lı halka)",
                      "arka": "Dış konseptler — arkadan (açma-kapama anahtarı, USB-C şarj)",
                      "ust": "Dış konseptler — üstten (figür yuvası, hale, eco ai)"}[gorunum], fontsize=13)
        plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0)
        yol = os.path.join(CIKTI, f"dis_konsept_{gorunum}.png")
        fig.savefig(yol)
        plt.close(fig)
        print(yol)


if __name__ == "__main__":
    main()
