"""Hazır figür STL'sinin altına vidalı NFC kapaklı tabanı ekler (internetten bulunan lisanssız figürler için).

    python cad/figur_tabanla.py FIGUR.stl --ad "Kırmızı Başlıklı Kız" --no 13 [--boy 55] [--kes 2] [--dondur 90 0 0]

  --boy     figürün tabandan yukarı yüksekliği (mm); verilmezse STL'nin kendi ölçüsü (mm sayılır)
  --kes     figürün kendi kaidesi varsa alttan kesilecek kalınlık (mm)
  --dondur  STL yatık geldiyse x y z ekseni etrafında derece (önce x, sonra y, sonra z)

Çıktı: cad/stl_cakil/figurler/<no>_<ad>.stl (figür + taban tek parça, dik basılır; yanında adlı kapak).
Figür, ayaklarının değdiği yerin ortası tabanın ortasına gelecek biçimde konur ve tabana
0,6 mm gömülür. Ağ kapalı değilse onarılır; onarılamazsa figür ve taban ayrı gövde olarak yazılır (yapıştırılır).
"""
import argparse
import math
import os
import sys

import numpy as np
import trimesh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
import manifold3d as m3  # noqa: E402
from geometri import kutu  # noqa: E402

CIKTI = os.path.join(C.KOK, "stl_cakil", "figurler")
TR = str.maketrans("çğıöşüÇĞİÖŞÜ ", "cgiosuCGIOSU_")


def manifolda(t):
    t = t.copy()
    t.merge_vertices()
    t.update_faces(t.nondegenerate_faces())
    t.update_faces(t.unique_faces())
    t.remove_unreferenced_vertices()
    if not t.is_watertight:
        trimesh.repair.fill_holes(t)
    trimesh.repair.fix_normals(t)
    m = m3.Manifold(m3.Mesh(vert_properties=np.asarray(t.vertices, np.float32), tri_verts=np.asarray(t.faces, np.uint32)))
    if m.is_empty() or m.status() != m3.Error.NoError:
        return None
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stl")
    ap.add_argument("--ad", required=True)
    ap.add_argument("--no", type=int, required=True)
    ap.add_argument("--boy", type=float, default=None)
    ap.add_argument("--kes", type=float, default=0.0)
    ap.add_argument("--dondur", type=float, nargs=3, default=(0.0, 0.0, 0.0))
    a = ap.parse_args()

    t = trimesh.load(a.stl, force="mesh")
    for eksen, aci in zip(([1, 0, 0], [0, 1, 0], [0, 0, 1]), a.dondur):
        if aci:
            t.apply_transform(trimesh.transformations.rotation_matrix(math.radians(aci), eksen))
    if a.boy:
        t.apply_scale(a.boy / (t.extents[2] - a.kes) if a.kes else a.boy / t.extents[2])
    t.apply_translation([0, 0, -t.bounds[0][2]])
    m = manifolda(t)
    if m is not None and a.kes > 0:
        m = (m ^ kutu(-500, 500, -500, 500, a.kes, 1000)).translate([0, 0, -a.kes])
    # ayakların değdiği yer (alttan 1,5 mm dilim) -> tabanın ortası
    if m is not None:
        poly = [np.asarray(p) for p in m.slice(0.75).to_polygons()]
    else:
        poly = [t.vertices[t.vertices[:, 2] < 1.5][:, :2]]
    pts = np.concatenate([p for p in poly if len(p)]) if poly else np.zeros((1, 2))
    cx, cy = (pts.min(0) + pts.max(0)) / 2
    gomme = 0.6
    taban = C.figur_taban()
    if m is not None:
        govde = taban + m.translate([-cx, -cy, C.FIGUR_BOY - gomme])
        tek = True
    else:
        t.apply_translation([-cx, -cy, C.FIGUR_BOY - gomme])
        govde = None
        tek = False
    kapak = C.figur_kapak(a.ad.replace("i", "İ").replace("ı", "I").upper(), a.no)
    kb = kapak.bounding_box()
    os.makedirs(CIKTI, exist_ok=True)
    ad_dosya = f"{a.no:02d}_{a.ad.translate(TR).lower()}"
    yol = os.path.join(CIKTI, ad_dosya + ".stl")
    if tek:
        gb = govde.bounding_box()
        parca = [C._tm(govde), C._tm(kapak.translate([gb[3] + 4 - kb[0], 0, 0]))]
    else:
        tb = C._tm(taban)
        parca = [t, tb, C._tm(kapak.translate([t.bounds[1][0] + 4 - kb[0], 0, 0]))]
    trimesh.util.concatenate(parca).export(yol)
    sonuc = trimesh.load(yol)
    if tek:
        mm = m.translate([-cx, -cy, C.FIGUR_BOY - gomme])
        temas = mm.slice(C.FIGUR_BOY + 0.3).area()
        boy = mm.bounding_box()[5] - C.FIGUR_BOY
    else:
        temas, boy = 0.0, t.extents[2] - gomme
    print(f"{yol}\n  figür tabanın üstünde {boy:.1f} mm, tabana değen alan {temas:.0f} mm², tek parça: {tek}, "
          f"su geçirmez: {sonuc.is_watertight}")
    if tek and temas < 30:
        print("  UYARI: figürün tabana değdiği alan küçük; kopmasın diye --kes ile kendi kaidesini bırakmayı ya da "
              "yapıştırmayı düşünün.")
    return yol


if __name__ == "__main__":
    main()
