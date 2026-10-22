"""Kabuğa takılan tema parçaları (kedi / ayı / tavşan kulağı, dinozor dikenleri): konsept görseli.

    python cad/kulaklar.py     # cad/onizleme/kabuk_temalar.png

Kabuk ters (üst yüz tablada) basıldığı için kulaklar kabuğa basılmaz: ayrı basılır, kabuğun omzundaki deliklere
pimle takılır (tema değiştirilebilir). Bu dosya şimdilik yalnız biçimleri ve yerleri gösterir.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
from geometri import CS, M, cokgen, xz_den_y_ye  # noqa: E402
import manifold3d as m3  # noqa: E402


def yuzey(aci, z):
    """Kabuğun dış yüzünde (açı, z) noktası ve o noktada yüzeyin eğimi (derece, 0 = dik duvar)."""
    r = C.dis_r(z)
    egim = math.degrees(math.atan2(C.dis_r(z - 0.5) - C.dis_r(z + 0.5), 1.0))
    return r * math.cos(math.radians(aci)), r * math.sin(math.radians(aci)), egim


def _yuvarla(cs, r):
    return cs.offset(-r, m3.JoinType.Round, 2.0, 16).offset(r, m3.JoinType.Round, 2.0, 16)


def _yerlestir(govde, aci, z, egim_ek=0.0, gom=3.0, yon=None):
    """Yerel parça (taban z=0'da, xz düzleminde, ön yüzü +y) kabuğun omzunda (açı, z) noktasına; ön yüzü yon
    açısına bakar (verilmezse dışa), tabanı yüzeye gömülü."""
    x, y, eg = yuzey(aci, z)
    yon = aci if yon is None else yon
    g = govde.translate([0, 0, -gom]).rotate([-egim_ek, 0, 0])
    return g.rotate([0, 0, yon - 90]).translate([x * 0.98, y * 0.98, z])


def kulak(bicim):
    """(gövde, iç kakma) yerel koordinatta. Kalınlık y boyunca 6 mm (ön yüz +y)."""
    if bicim == "kedi":
        dis = _yuvarla(CS([cokgen([(-15, 0), (15, 0), (3, 27)])]), 2.8)
        ic = _yuvarla(CS([cokgen([(-9.5, 4.5), (9.5, 4.5), (2.2, 20)])]), 1.5)
    elif bicim == "ayi":
        dis = CS.circle(14, 64).translate([0, 7]) ^ CS.square([40, 40]).translate([-20, 0])
        ic = CS.circle(8.5, 48).translate([0, 7.5]) ^ CS.square([40, 40]).translate([-20, 3.0])
    else:  # tavşan
        dis = CS.circle(1, 64).scale([9, 22]).translate([0, 20])
        ic = CS.circle(1, 48).scale([5.0, 16]).translate([0, 22])
    govde = xz_den_y_ye(dis, -3.0, 3.0)
    kakma = xz_den_y_ye(ic, 2.2, 3.01)
    return govde, kakma


def diken(boy):
    dis = _yuvarla(CS([cokgen([(-boy * 0.55, 0), (boy * 0.55, 0), (0, boy)])]), 1.6)
    return xz_den_y_ye(dis, -2.5, 2.5)


def tema(ad):
    """(gövdeler, kakmalar) kabuğun üstünde yerinde."""
    g, k = M(), M()
    if ad in ("kedi", "ayi", "tavsan"):
        z = C.H - 2.5                       # omuz (r ≈ 50): üst yüzdeki yıldızlara değmez
        for aci in (45.0, 135.0):          # yanlarda: figürü önden kapatmaz
            gv, kk = kulak(ad)
            ek = 10.0 if ad == "tavsan" else 4.0
            yon = 90 + (aci - 90) * 0.45       # kulaklar öne bakar, biraz dışa açık
            g = g + _yerlestir(gv, aci, z, ek, yon=yon)
            k = k + _yerlestir(kk, aci, z, ek, yon=yon)
    elif ad == "dinozor":   # arkada, soldan sağa omuz boyunca dikenler (büyükten küçüğe)
        for aci, boy in ((200, 11), (225, 15), (250, 18), (275, 18), (300, 15), (325, 11)):
            g = g + _yerlestir(diken(boy).rotate([0, 0, 90]), aci, C.H - 2.5, yon=aci + 90)
    return g, k


def konsept():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import dis_konsept as K
    import renkli as R
    b = R.kabuk_renk()
    renk = {k: c for k, _, c in R.RENKLER}
    temalar = [("kedi", "Kedi kulakları", "#F4F1EA", "#ff8fb8"), ("ayi", "Ayı kulakları", "#c98a4b", "#f2d0a8"),
               ("tavsan", "Tavşan kulakları", "#F4F1EA", "#ff8fb8"), ("dinozor", "Dinozor dikenleri", "#7ED321", None)]
    fig = plt.figure(figsize=(18, 14), dpi=100)
    for i, (ad, bas, rg, ri) in enumerate(temalar):
        g, k = tema(ad)
        ax = fig.add_subplot(2, 2, i + 1, projection="3d")
        elev, azim = (18, 90) if ad != "dinozor" else (22, 235)
        e, a = math.radians(elev), math.radians(azim)
        ls = [(m, renk[kk], False) for kk, m in b.items()] + [(g, rg, False)]
        if ri:
            ls.append((k, ri, False))
        K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-62, 62); ax.set_ylim(-62, 62); ax.set_zlim(-5, 90); ax.set_box_aspect((1, 1, 0.78)); ax.set_axis_off()
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(bas + (" (arkadan)" if ad == "dinozor" else ""), fontsize=14)
    fig.suptitle("Kabuk temaları (konsept): parçalar ayrı basılır, kabuğun omzundaki deliklere pimle takılır", fontsize=15,
                 fontweight="bold")
    plt.subplots_adjust(left=0, right=1, top=0.92, bottom=0, wspace=0, hspace=0.05)
    yol = os.path.join(C.KOK, "onizleme", "kabuk_temalar.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


if __name__ == "__main__":
    print(konsept())
