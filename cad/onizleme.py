"""Önizleme PNG'leri (matplotlib, ekran kartı/OpenGL gerekmez) -> cad/onizleme/."""
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import PathPatch  # noqa: E402
from matplotlib.path import Path  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

import parametreler as P  # noqa: E402
import parcalar as pc  # noqa: E402
from geometri import trimesh_e  # noqa: E402

KOK = os.path.dirname(os.path.abspath(__file__))
CIKTI = os.path.join(KOK, "onizleme")

RENK = {
    "govde_alt": "#d9dde3",
    "ust_kapak": "#b8c4d6",
    "difuzor_halka": "#fff7d6",
    "rc522_tutucu": "#7a8aa0",
    "figur_taban": "#ff8fb8",
}
ZARF_RENK = "#3a7d44"
ISIK = np.array([0.35, -0.45, 0.82])
ISIK = ISIK / np.linalg.norm(ISIK)


def _poly(mesh, renk, alfa=1.0, kamera=None, isik=None):
    v = mesh.vertices[mesh.faces]
    n = mesh.face_normals
    if kamera is not None:            # arka yüz ayıklama: ressam algoritmasının hatalarını büyük ölçüde giderir
        on = n @ kamera > 0
        v, n = v[on], n[on]
    L = ISIK if isik is None else isik
    k = 0.35 + 0.65 * np.clip(n @ L, 0, 1)
    c = np.array(matplotlib.colors.to_rgb(renk))
    fc = np.clip(c[None, :] * k[:, None], 0, 1)
    fc = np.concatenate([fc, np.full((len(fc), 1), alfa)], axis=1)
    return v, fc


def sahne(ogeler, dosya, elev=24, azim=58, baslik=None, boyut=(8, 6.5), zoom=1.0):
    """ogeler: [(manifold, renk, alfa)]"""
    tum_v, tum_c = [], []
    e, a = np.radians(elev), np.radians(azim)
    kamera = np.array([np.cos(e) * np.cos(a), np.cos(e) * np.sin(a), np.sin(e)])
    isik = kamera + np.array([0.45 * np.cos(a + 1.2), 0.45 * np.sin(a + 1.2), 0.5 * np.sign(elev)])
    isik = isik / np.linalg.norm(isik)
    for man, renk, alfa in ogeler:
        if man.is_empty():
            continue
        tm = trimesh_e(man.refine_to_length(12.0))   # uzun ince üçgenleri böl (derinlik sıralaması için)
        v, c = _poly(tm, renk, alfa, kamera, isik)
        tum_v.append(v)
        tum_c.append(c)
    V = np.concatenate(tum_v)
    C = np.concatenate(tum_c)
    fig = plt.figure(figsize=boyut, dpi=130)
    ax = fig.add_subplot(111, projection="3d")
    pcoll = Poly3DCollection(V, facecolors=C, edgecolors="none", linewidths=0)
    ax.add_collection3d(pcoll)
    lo = V.reshape(-1, 3).min(0)
    hi = V.reshape(-1, 3).max(0)
    mid = (lo + hi) / 2
    r = (hi - lo).max() / 2 / zoom
    ax.set_xlim(mid[0] - r, mid[0] + r)
    ax.set_ylim(mid[1] - r, mid[1] + r)
    ax.set_zlim(mid[2] - r, mid[2] + r)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    if baslik:
        ax.set_title(baslik, fontsize=11)
    fig.subplots_adjust(0, 0, 1, 0.95)
    fig.savefig(os.path.join(CIKTI, dosya))
    plt.close(fig)


def kesit_x(man, x=0.0):
    """x = sabit düzlemde kesit; (y, z) düzleminde çokgen listesi."""
    r = man.translate([-x, 0, 0]).rotate([0, -90, 0])      # yeni z = eski x, yeni x = -eski z
    cs = r.slice(0.0)
    out = []
    for p in cs.to_polygons():
        p = np.asarray(p)
        out.append(np.column_stack([p[:, 1], -p[:, 0]]))
    return out


def kesit_z(man, z):
    return [np.asarray(p) for p in man.slice(z).to_polygons()]


def poligon_ciz(ax, polys, renk, kenar="k", lw=0.6, hatch=None, alfa=1.0, z=1):
    if not polys:
        return
    verts, codes = [], []
    for p in polys:
        verts += list(p) + [p[0]]
        codes += [Path.MOVETO] + [Path.LINETO] * (len(p) - 1) + [Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=renk, edgecolor=kenar, lw=lw, hatch=hatch,
                           alpha=alfa, zorder=z))


def yerlestir(parca):
    return {ad: m.translate(list(o)) for ad, (m, o) in parca.items()}


def hepsi(parca, figs, ozel):
    os.makedirs(CIKTI, exist_ok=True)
    yer = yerlestir(parca)
    zarf = pc.zarflar()
    # 1) montaj, izometrik (önden-sağdan)
    sahne([(m, RENK[ad], 1.0) for ad, m in yer.items()], "montaj_izometrik.png", elev=26, azim=62,
          baslik="Masal standı — montaj (Ø128 x 57 mm), önden")
    sahne([(m, RENK[ad], 1.0) for ad, m in yer.items()], "montaj_arka.png", elev=22, azim=-110,
          baslik="Arkadan: USB-C güç girişi ve mikrofon deliği")
    # 2) patlatılmış
    ac = {"govde_alt": 0, "rc522_tutucu": 22, "ust_kapak": 45, "difuzor_halka": 80, "figur_taban": 105}
    og = [(m.translate([0, 0, ac[ad]]), RENK[ad], 1.0) for ad, m in yer.items()]
    for zad, zm in zarf.items():
        dz = 0
        if zad.startswith("RC522"):
            dz = ac["rc522_tutucu"]
        elif zad.startswith("NeoPixel"):
            dz = 62
        elif zad.startswith("NTAG"):
            dz = 93
        og.append((zm.translate([0, 0, dz]), ZARF_RENK if not zad.startswith("NeoPixel") else "#333333", 1.0))
    sahne(og, "montaj_patlatilmis.png", elev=18, azim=62, baslik="Patlatılmış montaj (yeşil: elektronik)",
          boyut=(8, 9.5), zoom=1.05)
    # 3) içi: kapaksız gövde + elektronik
    og = [(yer["govde_alt"], RENK["govde_alt"], 1.0)]
    for zad, zm in zarf.items():
        if zad.startswith(("RC522", "NeoPixel", "NTAG")):
            continue
        og.append((zm, ZARF_RENK, 1.0))
    sahne(og, "govde_ic_yerlesim.png", elev=55, azim=70, baslik="Alt gövde içi: yerleşim (yeşil: elektronik zarfları)")
    # 4) kesit A-A (x=0)
    fig, ax = plt.subplots(figsize=(11, 5), dpi=140)
    for ad, m in yer.items():
        poligon_ciz(ax, kesit_x(m), RENK[ad], hatch="////" if ad != "difuzor_halka" else None, z=2)
    for zad, zm in zarf.items():
        poligon_ciz(ax, kesit_x(zm), "#9fd7a8", kenar="#2e6b38", alfa=0.9, z=3)
    ax.set_aspect("equal")
    ax.set_xlim(-70, 70)
    ax.set_ylim(-5, 62)
    ax.set_xlabel("y (mm)  ← arka (USB-C)          ön (hoparlör) →")
    ax.set_ylabel("z (mm)")
    ax.grid(alpha=0.3)
    ax.set_title("Kesit A–A (x = 0): taban, kartlar, RC522, halka, difüzör, kapak, figür tabanı")
    fig.tight_layout()
    fig.savefig(os.path.join(CIKTI, "montaj_kesit.png"))
    plt.close(fig)
    # 5) parçalar tek tek
    sahne([(parca["govde_alt"][0], RENK["govde_alt"], 1.0)], "parca_govde_alt.png", elev=52, azim=70,
          baslik="govde_alt.stl")
    sahne([(parca["govde_alt"][0], RENK["govde_alt"], 1.0)], "parca_govde_alt_alt.png", elev=-50, azim=70,
          baslik="govde_alt.stl — alttan (ayak yuvaları, gizli vida havşaları, havalandırma)")
    sahne([(parca["ust_kapak"][0], RENK["ust_kapak"], 1.0)], "parca_ust_kapak.png", elev=40, azim=65,
          baslik="ust_kapak.stl — üstten (yuva, kama, halka kanalı)")
    sahne([(parca["ust_kapak"][0], RENK["ust_kapak"], 1.0)], "parca_ust_kapak_alt.png", elev=-45, azim=65,
          baslik="ust_kapak.stl — alttan (dil oluğu, insert ve RC522 vida delikleri)")
    sahne([(parca["difuzor_halka"][0], "#e8e2c8", 1.0)], "parca_difuzor_halka.png", elev=35, azim=60,
          baslik="difuzor_halka.stl", zoom=1.0)
    sahne([(parca["rc522_tutucu"][0], RENK["rc522_tutucu"], 1.0)], "parca_rc522_tutucu.png", elev=45, azim=60,
          baslik="rc522_tutucu.stl")
    sahne([(parca["figur_taban"][0], RENK["figur_taban"], 1.0)], "parca_figur_taban_alt.png", elev=-50, azim=60,
          baslik="figur_taban.stl — alttan (NTAG213 cebi, kama oluğu)")
    # 6) figür tabanları (üst yüz kesiti z = h - 0,3: kazıma yazılar boşluk olarak görünür)
    import json  # noqa
    n = len(figs) + len(ozel)
    sut = 4
    sat = (n + sut - 1) // sut
    fig, axs = plt.subplots(sat, sut, figsize=(sut * 3.2, sat * 3.4), dpi=120)
    axs = np.atleast_1d(axs).ravel()
    from uret import taban_yazisi
    ogeler = []
    for f in figs:
        y, mo = taban_yazisi(f)
        ogeler.append((f"{f['kimlik']}.stl (No {f['nfc_no']})", pc.figur_taban(y, f["nfc_no"], motif=mo), f["renk"]))
    for o in ozel:
        ogeler.append((f"ayar_karti.stl (No {o['nfc_no']})", pc.figur_taban("AYAR", o["nfc_no"], topuz=True), o["renk"]))
    for ax, (ad, m, renk) in zip(axs, ogeler):
        polys = [-q for q in kesit_z(m, P.TABAN_H - 0.3)]   # 180° çevir: ön aşağıda, yazı düz okunur
        poligon_ciz(ax, polys, renk, kenar="#333", lw=0.5)
        ax.set_aspect("equal")
        ax.set_xlim(-33, 33)
        ax.set_ylim(-33, 33)
        ax.set_title(ad, fontsize=9)
        ax.axis("off")
    for ax in axs[len(ogeler):]:
        ax.axis("off")
    fig.suptitle("Figür tabanları — üstten (ön aşağıda; yazı öne okunur, kama oluğu arkada)", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(CIKTI, "figur_tabanlari.png"))
    plt.close(fig)
