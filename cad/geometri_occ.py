"""geometri.py'nin OpenCASCADE (OCP) karşılığı: aynı adlar, aynı koordinatlar; çıktı gerçek B-rep katı.

cakil_ic.py'yi değiştirmeden STEP üretmek için kullanılır (step_yaz.py bu modülü 'geometri' yerine yükler):
kutu, silindir (koni dahil), dondur (çok noktalı profil -> düzgün B-spline yüzey), xz_den_y_ye (2B şekil -> prizma)
ve +, -, ^, translate, rotate (manifold3d ile aynı Euler sırası: önce x, sonra y, sonra z).
2B şekiller (yazı, yuvarlak dikdörtgen, daire) manifold3d CrossSection olarak kalır, prizmaya çevrilirken OCC olur.
"""
import math

import numpy as np

import geometri as _g
from geometri import CS, cokgen, yazi_duz, yuvarlak_dikdortgen, yildiz, yay  # noqa: F401  (2B: aynen)

from OCP.gp import gp_Pnt, gp_Vec, gp_Ax1, gp_Ax2, gp_Dir, gp_Trsf
from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone, \
    BRepPrimAPI_MakeRevol, BRepPrimAPI_MakePrism
from OCP.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut, BRepAlgoAPI_Common
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform, BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeFace, \
    BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCP.GeomAPI import GeomAPI_PointsToBSpline
from OCP.collections import Array1_gp_Pnt as TColgp_Array1OfPnt
from OCP.GeomAbs import GeomAbs_C2
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SOLID, TopAbs_SHELL


class O:
    """OCC şekli; None = boş."""

    def __init__(self, sh=None):
        self.sh = sh

    def is_empty(self):
        if self.sh is None:
            return True
        return not TopExp_Explorer(self.sh, TopAbs_SOLID).More()

    def __add__(self, o):
        if self.is_empty():
            return o
        if o.is_empty():
            return self
        return O(BRepAlgoAPI_Fuse(self.sh, o.sh).Shape())

    def __sub__(self, o):
        if self.is_empty() or o.is_empty():
            return self
        return O(BRepAlgoAPI_Cut(self.sh, o.sh).Shape())

    def __xor__(self, o):
        if self.is_empty() or o.is_empty():
            return O()
        return O(BRepAlgoAPI_Common(self.sh, o.sh).Shape())

    def _tr(self, t):
        if self.sh is None:
            return self
        return O(BRepBuilderAPI_Transform(self.sh, t, True).Shape())

    def translate(self, v):
        t = gp_Trsf()
        t.SetTranslation(gp_Vec(*map(float, v)))
        return self._tr(t)

    def rotate(self, a):
        """manifold3d ile aynı: önce x, sonra y, sonra z ekseni etrafında (derece)."""
        top = gp_Trsf()
        for eksen, aci in ((gp_Dir(0, 0, 1), a[2]), (gp_Dir(0, 1, 0), a[1]), (gp_Dir(1, 0, 0), a[0])):
            if aci:
                r = gp_Trsf()
                r.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), eksen), math.radians(aci))
                top.Multiply(r)      # top = top * r  (r önce uygulanır): Rz * Ry * Rx
        return self._tr(top)

    def volume(self):
        if self.is_empty():
            return 0.0
        p = GProp_GProps()
        BRepGProp.VolumeProperties_s(self.sh, p)
        return p.Mass()

    def bounding_box(self):
        b = Bnd_Box()
        BRepBndLib.Add_s(self.sh, b)
        return b.Get()


M = O


def kutu(x0, x1, y0, y1, z0, z1):
    return O(BRepPrimAPI_MakeBox(gp_Pnt(x0, y0, z0), gp_Pnt(x1, y1, z1)).Shape())


def silindir(r, z0, z1, x=0.0, y=0.0, seg=None, r2=None):
    ax = gp_Ax2(gp_Pnt(x, y, z0), gp_Dir(0, 0, 1))
    h = z1 - z0
    if r2 is None or abs(r2 - r) < 1e-9:
        return O(BRepPrimAPI_MakeCylinder(ax, r, h).Shape())
    return O(BRepPrimAPI_MakeCone(ax, r, r2, h).Shape())


def silindir_y(r, y0, y1, x=0.0, z=0.0, seg=None):
    return silindir(r, 0, y1 - y0).rotate([-90, 0, 0]).translate([x, y0, z])


def halka(r_ic, r_dis, z0, z1, seg=None):
    return silindir(r_dis, z0, z1) - silindir(r_ic, z0 - 1, z1 + 1)


def _yuz(pts3):
    p = BRepBuilderAPI_MakePolygon()
    for q in pts3:
        p.Add(gp_Pnt(*q))
    p.Close()
    return BRepBuilderAPI_MakeFace(p.Wire(), True).Face()


def dondur(profil, seg=None):
    """(r, z) profil z ekseni etrafında döner. Çok noktalı (>12) profilde eksen dışındaki eğri tek B-spline olur
    (düzgün yüzey); az noktalıda kenarlar doğru parçası (koni/silindir/düzlem yüzleri)."""
    pts = [(float(r), float(z)) for r, z in profil]
    w = BRepBuilderAPI_MakeWire()
    if len(pts) > 12:
        egri = [p for p in pts if p[0] > 1e-9]
        arr = TColgp_Array1OfPnt(1, len(egri))
        for i, (r, z) in enumerate(egri, start=1):
            arr.SetValue(i, gp_Pnt(r, 0, z))
        sp = GeomAPI_PointsToBSpline(arr, 3, 8, GeomAbs_C2, 1e-4).Curve()   # C2, ölçü 1e-4 mm içinde
        a0, a1 = gp_Pnt(0, 0, egri[0][1]), gp_Pnt(0, 0, egri[-1][1])
        w.Add(BRepBuilderAPI_MakeEdge(a0, gp_Pnt(egri[0][0], 0, egri[0][1])).Edge())
        w.Add(BRepBuilderAPI_MakeEdge(sp).Edge())
        w.Add(BRepBuilderAPI_MakeEdge(gp_Pnt(egri[-1][0], 0, egri[-1][1]), a1).Edge())
        w.Add(BRepBuilderAPI_MakeEdge(a1, a0).Edge())
        yuz = BRepBuilderAPI_MakeFace(w.Wire(), True).Face()
    else:
        yuz = _yuz([(r, 0.0, z) for r, z in cokgen(pts)])
    return O(BRepPrimAPI_MakeRevol(yuz, gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), 2 * math.pi).Shape())


def _alan(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)


def cs_prizma(cs, h):
    """2B CrossSection -> z = 0..h prizma (dış konturlar birleşir, delikler çıkar)."""
    dis, delik = O(), O()
    for p in cs.to_polygons():
        p = np.asarray(p, dtype=float)
        if len(p) < 3 or abs(_alan(p)) < 1e-6:
            continue
        f = _yuz([(a, b, 0.0) for a, b in (p if _alan(p) > 0 else p[::-1])])
        pr = O(BRepPrimAPI_MakePrism(f, gp_Vec(0, 0, h)).Shape())
        if _alan(p) > 0:
            dis = dis + pr
        else:
            delik = delik + pr
    return dis - delik


def xz_den_y_ye(cs, y0, y1, x=0.0, z=0.0):
    """geometri.xz_den_y_ye ile aynı eşleme: (u, v) -> (x + u, y, z + v), y0..y1."""
    return cs_prizma(cs, y1 - y0).rotate([90, 0, 0]).translate([x, y1, z])


def trimesh_e(man):   # kullanılmaz (uyumluluk)
    raise NotImplementedError


def kesisim_hacmi(a, b):
    return (a ^ b).volume()


__all__ = [n for n in dir(_g) if not n.startswith("_")]


def vida_cubugu(*args, **kw):
    """Dişli çubuk: manifold3d ile üretilen ağ (çok küçük düz yüzlü) OCC katısına çevrilir; diş sarmalı için OCC'de
    düzgün yüzey kurmak yerine ağ yeterli (STEP'te dişler ince yüzlü görünür, ölçüler aynıdır)."""
    import os
    import tempfile
    from OCP.StlAPI import StlAPI_Reader
    from OCP.TopoDS import TopoDS_Shape, TopoDS
    from OCP.BRepBuilderAPI import BRepBuilderAPI_Sewing, BRepBuilderAPI_MakeSolid
    from OCP.ShapeFix import ShapeFix_Solid
    from OCP.ShapeUpgrade import ShapeUpgrade_UnifySameDomain
    m = _g.vida_cubugu(*args, **kw)
    with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as f:
        yol = f.name
    _g.trimesh_e(m).export(yol)
    sh = TopoDS_Shape()
    StlAPI_Reader().Read(sh, yol)
    os.remove(yol)
    sew = BRepBuilderAPI_Sewing(1e-4)
    sew.Add(sh)
    sew.Perform()
    ms = BRepBuilderAPI_MakeSolid()
    ex = TopExp_Explorer(sew.SewedShape(), TopAbs_SHELL)
    while ex.More():
        ms.Add(TopoDS.Shell(ex.Current()))
        ex.Next()
    fx = ShapeFix_Solid(ms.Solid())
    fx.Perform()
    u = ShapeUpgrade_UnifySameDomain(fx.Solid(), True, True, True)
    u.Build()
    return O(u.Shape())
