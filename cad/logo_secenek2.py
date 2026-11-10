"""\"eco ai\" yazısı, ikinci tur seçenekler (2B, standın önü): python cad/logo_secenek2.py -> onizleme/logo_secenekleri2.png"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle  # noqa: E402
import manifold3d as m3  # noqa: E402
import cakil_ic as C  # noqa: E402
from geometri import CS, cokgen, yildiz, yuvarlak_dikdortgen  # noqa: E402
from logo_secenek import FONT, dizi, ciz, T, SA, MO, BE  # noqa: E402

R = m3.JoinType.Round


def birlesik(d):
    tum = None
    for _, c in d:
        tum = c if tum is None else tum + c
    return tum


def merkez(c):
    b = c.bounds()
    return (b[0] + b[2]) / 2, (b[1] + b[3]) / 2


def pati(cx, cy, s=1.0):
    """Kedi patisi: büyük yastık + 4 parmak."""
    p = CS.circle(1.7 * s, 32).scale([1.15, 0.95]).translate([cx, cy - 0.9 * s])
    for dx, dy, r in ((-1.9, 0.9, 0.75), (-0.7, 1.85, 0.75), (0.7, 1.85, 0.75), (1.9, 0.9, 0.75)):
        p = p + CS.circle(r * s, 20).translate([cx + dx * s, cy + dy * s])
    return p


def yay_serit(r_ic, r_dis, a0, a1, sy=1.0, n=60):
    t = np.linspace(math.radians(a0), math.radians(a1), n)
    dis = [(r_dis * math.cos(a), r_dis * math.sin(a) * sy) for a in t]
    ic = [(r_ic * math.cos(a), r_ic * math.sin(a) * sy) for a in t[::-1]]
    return CS([cokgen(dis + ic)]).offset(0.0, R, 2.0, 8)


def cizgi(pts, w):
    """Kalınlığı w olan yuvarlak uçlu çizgi."""
    p = None
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        L = math.hypot(x1 - x0, y1 - y0)
        s = yuvarlak_dikdortgen(L + w, w, w / 2).rotate(math.degrees(math.atan2(y1 - y0, x1 - x0))).translate([(x0 + x1) / 2, (y0 + y1) / 2])
        p = s if p is None else p + s
    return p


BANT = (31.0, 7.2)   # yazının sığması gereken alan: x ±31, y ±7,2 (altında ızgara, üstünde omuz kıvrılır)


def secenekler():
    s = []
    # A) rozet: turkuaz hap içinde beyaz (oyuk) harfler, sarı kenar, uçlarda yıldız
    d = dizi("eco ai", FONT["lilita"], 9.6, aralik=0.6)
    yazi = birlesik(d)
    hap = yuvarlak_dikdortgen(57, 12.2, 6.1)
    kenar = yuvarlak_dikdortgen(60, 14.4, 7.2) - hap
    yild = yildiz(-22.6, 0, 2.7, 1.15, aci0=90) + yildiz(22.6, 0, 2.7, 1.15, aci0=90)
    s.append(("A) Rozet", [(kenar, SA), (hap - yazi.offset(0.4, R, 2.0, 8) - yild.offset(0.5, R, 2.0, 8), T), (yild, SA)]))
    # B) bulut: mor bulut, beyaz harfler, sarı güneş bulutun arkasından
    d = dizi("eco ai", FONT["sniglet"], 9.0, aralik=0.8)
    yazi = birlesik(d).translate([0, -1.6])
    bulut = (CS.circle(6.2, 48).translate([-11, 0.4]) + CS.circle(7.2, 48).translate([1, 1.3]) + CS.circle(5.6, 48).translate([12, 0.2])
             + CS.circle(4.4, 40).translate([-21, -2.6]) + CS.circle(4.4, 40).translate([21.5, -2.6])
             + yuvarlak_dikdortgen(48, 8.2, 4.1).translate([0, -2.9]))
    gunes = CS.circle(3.3, 32).translate([-24.5, 3.6])
    isin = None
    for k in range(7):
        a = math.radians(90 + k * 32)
        r_ = cizgi([(-24.5 + 4.5 * math.cos(a), 3.6 + 4.5 * math.sin(a)), (-24.5 + 6.0 * math.cos(a), 3.6 + 6.0 * math.sin(a))], 0.9)
        isin = r_ if isin is None else isin + r_
    isin = isin ^ CS.square([80, 20]).translate([-40, -7.2])
    bulut_k = bulut - yazi.offset(0.4, R, 2.0, 8)
    s.append(("B) Bulut ve güneş", [((gunes + isin) - bulut.offset(0.7, R, 2.0, 8), SA), (bulut_k, MO)]))
    # C) gökkuşağı: yassı iki şerit (sarı, turkuaz) yazının arkasında, mor harfler beyaz boşlukla ayrılır
    d = dizi("eco ai", FONT["lilita"], 10.0, aralik=0.6)
    yazi = birlesik(d).translate([0, -2.0])
    yay = [(yay_serit(25.0, 27.4, 0, 180, 0.42), SA), (yay_serit(27.9, 30.3, 0, 180, 0.42), T)]
    yay = [(c.translate([0, -6.3]) - yazi.offset(0.8, R, 2.0, 8), r) for c, r in yay]
    yil = [(yildiz(x, y, r, r * 0.42, aci0=90), MO) for x, y, r in ((-30.5, -4.5, 1.8), (30.5, -4.5, 1.8))]
    s.append(("C) Gökkuşağı", yay + [(yazi, MO)] + yil))
    # D) oyuncak blokları: her harf yuvarlak köşeli kare blokta, harf oyuk (beyaz); sarı blokta harf mor
    out = []
    renk = [T, MO, SA, T, MO]
    x = -29.2
    for i, ch in enumerate("ecoai"):
        if i == 3:
            x += 2.4
        blok = yuvarlak_dikdortgen(10.4, 10.4, 2.4)
        h = dizi(ch, FONT["lilita"], 9.0)[0][1]
        cx, cy = merkez(h)
        h = h.translate([-cx, -cy])
        aci = [-6, 4, -3, 5, -5][i]
        dy = [0.6, -0.5, 0.8, -0.4, 0.5][i]
        yer = lambda m: m.rotate(aci).translate([x + 5.2, dy])  # noqa: E731
        if renk[i] == SA:
            out += [(yer(blok - h.offset(0.35, R, 2.0, 8)), SA), (yer(h), MO)]
        else:
            out.append((yer(blok - h), renk[i]))
        x += 11.2
    s.append(("D) Oyuncak blokları", out))
    # E) kedi: turkuaz harfler, iki yanda bıyıklar, i'nin noktası pati (kedi kulaklarıyla takım)
    d = dizi("eco ai", FONT["lilita"], 11.0, aralik=0.7)
    out = []
    for i, (ch, c) in enumerate(d):
        c = c.translate([0, -1.0])
        if ch == "i":
            b = c.bounds()
            govde = c ^ CS.square([30, (b[3] - b[1]) * 0.66 + 1]).translate([b[0] - 5, b[1] - 1])
            out += [(govde, T), (pati((b[0] + b[2]) / 2, b[3] - 0.6, 0.85), MO)]
        else:
            out.append((c, T))
    for sg in (-1, 1):
        for dy, eg in ((2.0, 0.10), (-0.4, 0.0), (-2.8, -0.10)):
            x0, x1 = sg * 22.5, sg * 30.5
            out.append((cizgi([(x0, dy), ((x0 + x1) / 2, dy + 0.8 + eg * 8), (x1, dy + eg * 20)], 0.9), MO))
    s.append(("E) Kedi bıyıkları ve pati", out))
    # F) gölgeli pop: sarı şişkin harfler, mor gölge, turkuaz parıltılar
    d = dizi("eco ai", FONT["sniglet"], 12.0, aralik=1.0)
    yazi = birlesik(d).translate([-0.6, 0.6])
    golge = yazi.translate([1.2, -1.2]) - yazi
    pir = [(yildiz(x, y, r, r * 0.38, n=4, aci0=90), T) for x, y, r in ((-27.0, 3.8, 2.4), (27.5, -3.5, 2.0), (28.5, 4.5, 1.4))]
    s.append(("F) Gölgeli pop yazı", [(golge, MO), (yazi, SA)] + pir))
    return s


def on_ust(ax):
    zs = np.linspace(20, C.H, 80)
    xs = [C.dis_r(z) for z in zs]
    ax.fill_betweenx(zs - C.YAZI_Z, [-x for x in xs], xs, color=BE, ec="#b9ad9c", lw=1.2, zorder=1)
    hd = C.PARCA["hoparlor"][0]
    for i in range(-6, 7):
        for j in range(-6, 7):
            x, zz = i * 4.4 + (2.2 if j % 2 else 0.0), j * 3.8
            if x * x + zz * zz < (hd / 2 - 5) ** 2 and C.HOP_ZC + zz < C.YAZI_Z - C.YAZI_BOY / 2 - 1.5 and C.HOP_ZC + zz > C.TABAN_KAL + 5:
                ax.add_patch(Circle((x, C.HOP_ZC + zz - C.YAZI_Z), 1.2, fc="#d8cfc2", ec="none", zorder=2))


if __name__ == "__main__":
    fig, axs = plt.subplots(3, 2, figsize=(17, 16), dpi=100)
    for ax, (bas, parcalar) in zip(axs.ravel(), secenekler()):
        on_ust(ax)
        for cs, renk in parcalar:
            ciz(ax, cs, renk)
        ax.plot([-BANT[0], BANT[0], BANT[0], -BANT[0], -BANT[0]], [-BANT[1], -BANT[1], BANT[1], BANT[1], -BANT[1]],
                color="#cccccc", lw=0.6, ls=":", zorder=0)
        ax.set_xlim(-50, 50); ax.set_ylim(-14, C.H - C.YAZI_Z + 2); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(bas, fontsize=17, fontweight="bold")
    fig.suptitle("\"eco ai\" — yeni seçenekler (standın önünün üst kısmı, gerçek ölçek; beyaz kısımlar kabuğun kendi rengi)",
                 fontsize=15)
    plt.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(os.path.join(C.KOK, "onizleme", "logo_secenekleri2.png"))
    print("ok")
