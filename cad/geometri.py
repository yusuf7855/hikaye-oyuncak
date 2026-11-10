"""Küçük geometri yardımcıları (manifold3d üstüne)."""
import math

import numpy as np
import manifold3d as m3
import trimesh

from parametreler import SEG_BUYUK, SEG_KUCUK

M = m3.Manifold
CS = m3.CrossSection


def kutu(x0, x1, y0, y1, z0, z1):
    return M.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])


def silindir(r, z0, z1, x=0.0, y=0.0, seg=None, r2=None):
    if seg is None:
        seg = SEG_BUYUK if r > 15 else SEG_KUCUK
    r2 = r if r2 is None else r2
    return M.cylinder(z1 - z0, r, r2, circular_segments=seg).translate([x, y, z0])


def silindir_y(r, y0, y1, x=0.0, z=0.0, seg=None):
    """Ekseni y boyunca silindir."""
    c = silindir(r, 0, y1 - y0, seg=seg)          # z boyunca
    return c.rotate([-90, 0, 0]).translate([x, y0, z])   # z -> +y


def halka(r_ic, r_dis, z0, z1, seg=SEG_BUYUK):
    return silindir(r_dis, z0, z1, seg=seg) - silindir(r_ic, z0 - 1, z1 + 1, seg=seg)


def cokgen(pts):
    """Saat yönünün tersine (pozitif alan) yönlendirilmiş çokgen."""
    a = np.asarray(pts, dtype=float)
    x, y = a[:, 0], a[:, 1]
    alan = 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)
    return a if alan > 0 else a[::-1].copy()


def dondur(profil, seg=SEG_BUYUK):
    """(r, z) profil çokgeni z ekseni etrafında döndürülür."""
    return CS([cokgen(profil)]).revolve(seg)


def yay(cx, cy, r, a0, a1, n=8):
    """(cx,cy) merkezli yay noktaları, açı derece."""
    return [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
            for a in np.linspace(a0, a1, n)]


def yuvarlak_dikdortgen(w, h, r):
    r = min(r, w / 2 - 1e-3, h / 2 - 1e-3)
    return CS.square([w - 2 * r, h - 2 * r], center=True).offset(r, m3.JoinType.Round, 2.0, 24)


def xz_den_y_ye(cs, y0, y1, x=0.0, z=0.0):
    """x-z düzlemindeki 2B şekli y0..y1 arasında uzatır (merkezi (x, z))."""
    e = cs.extrude(y1 - y0)                 # z boyunca, 2B (u,v)
    # (u, v, w) -> (u, w, v): önce x ekseni etrafında -90 (v->z? ) dönüş
    e = e.rotate([90, 0, 0])                # (u, v, w) -> (u, -w, v)
    return e.translate([x, y1, z])


def xy_prizma(cs, z0, z1):
    """x-y düzlemindeki 2B şekli z0..z1 arasında uzatır."""
    return cs.extrude(z1 - z0).translate([0, 0, z0])


def aynala_x(man):
    """x -> -x (yz düzlemine göre ayna)."""
    return man.mirror([1, 0, 0])


def acida(man, aci):
    return man.rotate([0, 0, aci])


def kutup(r, aci):
    a = math.radians(aci)
    return r * math.cos(a), r * math.sin(a)


def govde_kutusu_radyal(r0, r1, genislik, z0, z1, aci):
    """Radyal doğrultuda (r0..r1) kutu, aci yönünde."""
    b = kutu(r0, r1, -genislik / 2, genislik / 2, z0, z1)
    return acida(b, aci)


def trimesh_e(man):
    mg = man.to_mesh()
    v = np.asarray(mg.vert_properties)[:, :3]
    f = np.asarray(mg.tri_verts)
    return trimesh.Trimesh(vertices=v, faces=f, process=True)


def kesisim_hacmi(a, b):
    return (a ^ b).volume()


# ---------------------------------------------------------------- yazı
_FONT_CACHE = {}


def _font(path):
    from matplotlib.font_manager import FontProperties
    if path not in _FONT_CACHE:
        _FONT_CACHE[path] = FontProperties(fname=path)
    return _FONT_CACHE[path]


def yazi_duz(metin, boy, font_path, merkez=True, ayna=False):
    """Düz yazı 2B kesiti (mm). Taban çizgisi y=0; merkez=True ise x'te ortalanır."""
    from matplotlib.textpath import TextPath
    tp = TextPath((0, 0), metin, size=boy, prop=_font(font_path))
    polys = [np.asarray(p) for p in tp.to_polygons(closed_only=True) if len(p) >= 3]
    cs = CS(polys, m3.FillRule.EvenOdd)
    if merkez:
        b = cs.bounds()
        cs = cs.translate([-(b[0] + b[2]) / 2, -(b[1] + b[3]) / 2])
    if ayna:
        cs = cs.mirror([1, 0])
    return cs.offset(0.03, m3.JoinType.Round, 2.0, 8).simplify(0.005)


def yazi_yay(metin, boy, font_path, r_taban, orta_aci=90.0):
    """Çember yayı üzerinde yazı: harflerin üstü merkeze bakar, yay orta_aci'da ortalanır.
    orta_aci=90 (ön) için yazı, standın önünde duran kişiye düz okunur (soldan sağa)."""
    from matplotlib.textpath import TextPath, text_to_path
    fp = _font(font_path)
    font = text_to_path._get_font(fp)
    font.set_size(text_to_path.FONT_SCALE, text_to_path.DPI)
    glyphs = text_to_path.get_glyphs_with_font(font, metin, return_new_glyphs_only=False)[0]
    olcek = boy / text_to_path.FONT_SCALE
    xs = [g[1] * olcek for g in glyphs]
    son = TextPath((0, 0), metin[-1], size=boy, prop=fp).get_extents()
    toplam = xs[-1] + son.x1
    aci_toplam = toplam / r_taban            # radyan
    a0 = math.radians(orta_aci) - aci_toplam / 2
    sonuc = CS()
    for ch, x in zip(metin, xs):
        if ch.isspace():
            continue
        tp = TextPath((0, 0), ch, size=boy, prop=fp)
        polys = [np.asarray(p) for p in tp.to_polygons(closed_only=True) if len(p) >= 3]
        if not polys:
            continue
        g = CS(polys, m3.FillRule.EvenOdd)
        th = a0 + x / r_taban                 # harfin sol taban noktasının açısı
        # yerel X -> teğet (artan açı), yerel Y -> merkeze doğru: dönüş = th + 90°
        g = g.rotate(math.degrees(th) + 90.0).translate([r_taban * math.cos(th), r_taban * math.sin(th)])
        sonuc = sonuc + g
    # Ş/ç gibi harflerde çengel gövdeye noktada değer: 0,03 mm şişirme tek parça yapar
    # (yoksa STL'de "tek noktadan değen" su geçirmez olmayan köşe oluşur)
    return sonuc.offset(0.03, m3.JoinType.Round, 2.0, 8).simplify(0.005)


def yildiz(cx, cy, r_dis, r_ic, n=5, aci0=90.0):
    pts = []
    for i in range(2 * n):
        r = r_dis if i % 2 == 0 else r_ic
        a = math.radians(aci0 + i * 180.0 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return CS([cokgen(pts)])


def hilal(cx, cy, r, kayma, r2=None, aci=0.0):
    """Hilal: r çemberinden, kayma kadar ötelenmiş r2 çemberi çıkarılır."""
    r2 = r * 0.85 if r2 is None else r2
    a = math.radians(aci)
    c1 = CS.circle(r, 64).translate([cx, cy])
    c2 = CS.circle(r2, 64).translate([cx + kayma * math.cos(a), cy + kayma * math.sin(a)])
    return c1 - c2


# ---------------------------------------------------------------- vida dişi
def vida_cubugu(r_kok, derinlik, adim, ust_gen, alt_gen, z0, z1, n_aci=96):
    """Dişli çubuk (tek ağızlı, sağ el): eksene dik kesit r(φ) = kök + yamuk diş profili, adım başına 360° burularak
    z0..z1 uzatılır; sarmal, z0'dan bağımsız olarak hep aynıdır (aynı adımla üretilen dişi/erkek parçalar eşleşir).
    Kesit: kök yarıçapı r_kok, tepe r_kok + derinlik; diş tepede ust_gen, kökte alt_gen geniş (eksen yönünde)."""
    def r_a(a):
        da = abs(a - adim / 2)
        if da <= ust_gen / 2:
            return r_kok + derinlik
        if da <= alt_gen / 2:
            return r_kok + derinlik * (alt_gen / 2 - da) / ((alt_gen - ust_gen) / 2)
        return r_kok
    pts = []
    for k in range(n_aci):
        fi = 2 * math.pi * k / n_aci
        a = (z0 - adim * fi / (2 * math.pi)) % adim       # z0 yüksekliğindeki kesit
        r = r_a(a)
        pts.append((r * math.cos(fi), r * math.sin(fi)))
    h = z1 - z0
    kat = max(4, int(math.ceil(h / adim * n_aci / 2)))
    return CS([np.asarray(pts)]).extrude(h, kat, 360.0 * h / adim).translate([0, 0, z0])
