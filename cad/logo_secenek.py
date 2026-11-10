"""\"eco ai\" yazısı seçenekleri (2B, standın önü): python cad/logo_secenek.py -> cad/onizleme/logo_secenekleri.png"""
import sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath, TextToPath
import manifold3d as m3
import cakil_ic as C
from geometri import CS, yildiz
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "font") + "/"   # OFL fontlar (google/fonts)
FONT = {"sniglet": F + "Sniglet-ExtraBold.ttf", "modak": F + "Modak-Regular.ttf", "lilita": F + "LilitaOne-Regular.ttf",
        "rammetto": F + "RammettoOne-Regular.ttf", "bubble": F + "BubblegumSans-Regular.ttf", "fredoka": C.FONT}
T, SA, MO, BE = "#1FB5B0", "#F6C33B", "#7A4FD0", "#F4F1EA"
t2p = TextToPath()

def harf(ch, font, boy):
    tp = TextPath((0, 0), ch, size=boy, prop=FontProperties(fname=font))
    polys = [np.asarray(p) for p in tp.to_polygons(closed_only=True) if len(p) >= 3]
    return CS(polys, m3.FillRule.EvenOdd) if polys else CS()

def genislik(s, font, boy):
    w, h, d = t2p.get_text_width_height_descent(s, FontProperties(fname=font, size=boy), ismath=False)
    return w

def dizi(metin, font, boy, aralik=0.0):
    """[(ch, cs)] harf harf, ortalanmış (x), taban y=0."""
    out = []
    for i, ch in enumerate(metin):
        if ch == " ":
            continue
        x = genislik(metin[:i], font, boy) + aralik * i if i else 0.0
        out.append((ch, harf(ch, font, boy).translate([x, 0])))
    tum = None
    for _, c in out:
        tum = c if tum is None else tum + c
    b = tum.bounds()
    dx, dy = -(b[0] + b[2]) / 2, -(b[1] + b[3]) / 2
    return [(ch, c.translate([dx, dy])) for ch, c in out]

def ciz(ax, cs, renk, ec="none", lw=0, z=3):
    verts, codes = [], []
    for p in cs.to_polygons():
        p = np.asarray(p)
        if len(p) < 3: continue
        verts += list(p) + [p[0]]; codes += [Path.MOVETO] + [Path.LINETO] * (len(p) - 1) + [Path.CLOSEPOLY]
    if verts:
        ax.add_patch(PathPatch(Path(verts, codes), fc=renk, ec=ec, lw=lw, zorder=z))

def kontur(cs, d):
    return cs.offset(d, m3.JoinType.Round, 2.0, 16) - cs

def gulen_o(r):
    """o harfi yerine gülen yüz: halka + iki göz + gülümseme."""
    yuz = CS.circle(r, 48) - CS.circle(r - 1.6, 48)
    goz = CS.circle(0.75, 16).translate([-r * 0.35, r * 0.2]) + CS.circle(0.75, 16).translate([r * 0.35, r * 0.2])
    t = np.linspace(math.radians(200), math.radians(340), 20)
    agiz_dis = [(r * 0.55 * math.cos(a), r * 0.55 * math.sin(a)) for a in t]
    agiz_ic = [(r * 0.35 * math.cos(a), r * 0.35 * math.sin(a) + 0.3) for a in t[::-1]]
    agiz = CS([np.array(agiz_dis + agiz_ic)]).offset(0.25, m3.JoinType.Round, 2.0, 8)
    return yuz, goz + agiz

def secenekler():
    s = []
    # 1 renkli harfler
    d = dizi("eco ai", FONT["sniglet"], 15, aralik=1.2)
    s.append(("1) Renkli harfler", [(c, [T, SA, MO, T, SA][i]) for i, (_, c) in enumerate(d)], []))
    # 2 baloncuk + kontur
    d = dizi("eco ai", FONT["modak"], 17, aralik=1.6)
    tum = None
    for _, c in d:
        tum = c if tum is None else tum + c
    s.append(("2) Baloncuk harfler (sarı, mor kenar)", [(kontur(tum, 1.1), MO), (tum, SA)], []))
    # 3 zıplayan harfler
    d = dizi("eco ai", FONT["lilita"], 15, aralik=0.8)
    renk = [MO, T, SA, MO, T]; aci = [-10, 6, -6, 9, -4]; dy = [0.8, -0.8, 1.0, -0.6, 0.6]
    out = []
    for i, (ch, c) in enumerate(d):
        b = c.bounds(); cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        out.append((c.translate([-cx, -cy]).rotate(aci[i]).translate([cx, cy + dy[i]]), renk[i]))
    s.append(("3) Zıplayan harfler", out, []))
    # 4 gülen o, yıldız noktalı i
    d = dizi("eco ai", FONT["lilita"], 15, aralik=0.8)
    out = []
    for i, (ch, c) in enumerate(d):
        b = c.bounds(); cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        if i == 2:  # o
            r = (b[3] - b[1]) / 2 + 0.6
            yuz, ifade = gulen_o(r)
            out += [(yuz.translate([cx, cy]), SA), (ifade.translate([cx, cy]), SA)]
        elif ch == "i":
            govde = c ^ CS.square([40, b[1] + (b[3] - b[1]) * 0.66 - (b[1] - 1)]).translate([b[0] - 5, b[1] - 1])
            out += [(govde, T), (yildiz(cx, b[3] - 0.6, 3.2, 1.4, aci0=90), MO)]
        else:
            out.append((c, T))
    s.append(("4) Gülen o, yıldız noktalı i", out, []))
    # 5 gülümseyen yay
    d = dizi("eco ai", FONT["rammetto"], 12.5)
    out = []
    renk = [T, SA, MO, T, SA]
    xs = [((c.bounds()[0] + c.bounds()[2]) / 2) for _, c in d]
    R = 55.0
    for i, (ch, c) in enumerate(d):
        b = c.bounds(); cx = (b[0] + b[2]) / 2
        a = math.asin(max(-1, min(1, cx / R)))
        out.append((c.translate([-cx, 0]).rotate(math.degrees(a)).translate([R * math.sin(a), R - R * math.cos(a) - 1.5]), renk[i]))
    s.append(("5) Gülümseyen yay", out, []))
    # 6 yıldızlı
    d = dizi("eco ai", FONT["bubble"], 17)
    out = [(c, T) for _, c in d]
    yild = [(yildiz(x, y, r, r * 0.45, aci0=90), [SA, MO][k % 2]) for k, (x, y, r) in
            enumerate(((-27, 7, 2.2), (-22, -7.5, 1.6), (25, 7.5, 2.4), (28.5, -4, 1.6), (0.5, 9.5, 1.5)))]
    s.append(("6) Yıldızlar arasında", out + yild, []))
    return s

def on_silüet(ax):
    zs = np.linspace(0, C.H, 120)
    xs = [C.dis_r(z) for z in zs]
    ax.fill_betweenx(zs - C.YAZI_Z, [-x for x in xs], xs, color=BE, ec="#b9ad9c", lw=1.2, zorder=1)
    hd = C.PARCA["hoparlor"][0]
    for i in range(-6, 7):
        for j in range(-6, 7):
            x, zz = i * 4.4 + (2.2 if j % 2 else 0.0), j * 3.8
            if x * x + zz * zz < (hd / 2 - 5) ** 2 and C.HOP_ZC + zz < C.YAZI_Z - C.YAZI_BOY / 2 - 1.5 and C.HOP_ZC + zz > C.TABAN_KAL + 5:
                ax.add_patch(Circle((x, C.HOP_ZC + zz - C.YAZI_Z), 1.2, fc="#d8cfc2", ec="none", zorder=2))

fig, axs = plt.subplots(2, 3, figsize=(19, 11.5), dpi=105)
for ax, (bas, parcalar, _) in zip(axs.ravel(), secenekler()):
    on_silüet(ax)
    for cs, renk in parcalar:
        ciz(ax, cs, renk)
    ax.set_xlim(-62, 62); ax.set_ylim(-C.YAZI_Z - 2, C.H - C.YAZI_Z + 3); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(bas, fontsize=15)
fig.suptitle("\"eco ai\" yazısı için seçenekler (standın önü; renkler AMS'teki 4 renk)", fontsize=17, fontweight="bold")
plt.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(os.path.join(C.KOK, "onizleme", "logo_secenekleri.png")); print("ok")
