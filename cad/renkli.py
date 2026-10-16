"""Çok renkli kabuk (Bambu Lab P2S Combo / AMS, 4 renk): renk bölgeleri ayrı gövdeler.

    python cad/renkli.py     # stl_cakil/renkli_bambu/: kabuk_renkli_bambu.3mf + renk başına STL; onizleme/renkli_kabuk.png

Renkler (AMS yuvası = Bambu Studio'daki filament numarası):
  1 beyaz   : gövde; LED'lerin üstündeki 0,6 mm ışık halkası BEYAZ kalmalı (ışık geçer)
  2 turkuaz : "eco ai" logosu (kabarık harfler + duvara 1,3 mm gömülü kökü), çukurun zemini (üst 0,6 mm)
  3 sarı    : çukurun kenarı ve ışık halkasının dışındaki "güneş" halkası (üst yüzde 0,6 mm kakma)
  4 mor     : üst yüzde 6 yıldız (0,6 mm kakma)
Üst yüz ve çukur zemini kakmaları ters baskıda ilk katmanlardadır (az renk değişimi); logo dikey duvarda olduğundan
logonun boyunca her katmanda renk değişir (atık kule/prime tower açık kalmalı).
"""
import math
import os
import sys
import uuid
import zipfile

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
from geometri import silindir, dondur, xz_den_y_ye, yazi_duz, yildiz  # noqa: E402

KAKMA = 0.6
RENKLER = [("1_beyaz", "beyaz", "#F4F1EA"), ("2_turkuaz", "turkuaz", "#1FB5B0"),
           ("3_sari", "sarı", "#F6C33B"), ("4_mor", "mor", "#7A4FD0")]
YILDIZ_R, YILDIZ_BOY, YILDIZ_ADET = 34.0, 5.2, 6


def bolgeler():
    """Kullanım konumunda (z yukarı) renk bölgeleri: {renk: manifold}; birbirine değmez, toplamı kabuk."""
    g = C.kabuk()
    H, seg = C.H, C.SEG
    ust = lambda r0, r1: silindir(r1, H - KAKMA, H + 1, seg=seg) - silindir(r0, H - KAKMA - 1, H + 2, seg=seg)  # noqa: E731
    logo = (xz_den_y_ye(yazi_duz(C.YAZI, C.YAZI_BOY, C.FONT, ayna=True), 0, 80, x=0, z=C.YAZI_Z)
            ^ dondur(C.profil(1.2), seg)) - dondur(C.profil(-1.3), seg)   # harf kökü duvara 1,3 mm (kabuktaki 0,8 ve ses yakasının 1,0 sınırlarıyla çakışmasın)
    zemin = silindir(C.YUVA_R + 0.01, C.Z_CANAK_TABAN - KAKMA, C.Z_CANAK_TABAN + 0.01, seg=seg)
    turkuaz = (logo + zemin) ^ g
    sari = (ust(C.YUVA_R - 0.01, C.ISIK_R[0] - 0.4) + ust(C.ISIK_R[1] + 0.6, C.ISIK_R[1] + 3.6)) ^ g
    yild = None
    for i in range(YILDIZ_ADET):
        a = math.radians(90 + 360.0 * i / YILDIZ_ADET)
        s = yildiz(YILDIZ_R * math.cos(a), YILDIZ_R * math.sin(a), YILDIZ_BOY, YILDIZ_BOY * 0.45, aci0=90 + 360.0 * i / YILDIZ_ADET)
        yild = s if yild is None else yild + s
    mor = yild.extrude(KAKMA + 1).translate([0, 0, H - KAKMA]) ^ g
    beyaz = g - turkuaz - sari - mor
    return {"1_beyaz": beyaz, "2_turkuaz": turkuaz, "3_sari": sari, "4_mor": mor}


def baski_konumu(b):
    """Kabukla aynı: ters (üst yüz tablada), x-y ortada, z = 0'dan."""
    ters = {k: m.rotate([180, 0, 0]) for k, m in b.items()}
    hepsi = None
    for m in ters.values():
        hepsi = m if hepsi is None else hepsi + m
    bb = hepsi.bounding_box()
    t = [-(bb[0] + bb[3]) / 2, -(bb[1] + bb[4]) / 2, -bb[2]]
    return {k: m.translate(t) for k, m in ters.items()}


def temiz(man):
    """Boole işlemlerinin bıraktığı hacimsiz kırıntıları at (dilimleyici uyarı vermesin)."""
    import trimesh
    t = C._tm(man)
    t.merge_vertices()
    parca = [p for p in t.split(only_watertight=False) if abs(p.volume) > 0.01]
    return trimesh.util.concatenate(parca)


def _mesh_xml(oid, t):
    v, f = t.vertices, t.faces
    vs = "".join(f'<vertex x="{a:.4f}" y="{b:.4f}" z="{c:.4f}"/>' for a, b, c in v)
    ts = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in f)
    return (f'<object id="{oid}" p:UUID="{uuid.uuid4()}" type="model"><mesh><vertices>{vs}</vertices>'
            f'<triangles>{ts}</triangles></mesh></object>'), len(f)


def yaz_3mf(yol, parcalar, ad="kabuk_renkli"):
    """Bambu Studio proje biçimi (3MF + production uzantısı): tek nesne, renk başına bir parça; her parçanın filament
    numarası Metadata/model_settings.config'te. Bambu Studio açınca parçalar AMS 1-4'e atanmış gelir."""
    NS = ('xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
          'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
          'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"')
    alt, comps, parts = [], [], []
    ana_id = len(parcalar) + 1
    for i, (dosya, renk_ad, extr, man) in enumerate(parcalar, start=1):
        x, ntri = _mesh_xml(i, man)
        alt.append(x)
        comps.append(f'<component p:path="/3D/Objects/object_1.model" objectid="{i}" p:UUID="{uuid.uuid4()}" '
                     f'transform="1 0 0 0 1 0 0 0 1 0 0 0"/>')
        parts.append(f'    <part id="{i}" subtype="normal_part">\n'
                     f'      <metadata key="name" value="{dosya}"/>\n'
                     f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
                     f'      <metadata key="extruder" value="{extr}"/>\n'
                     f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
                     f'    </part>\n')
    obj_model = (f'<?xml version="1.0" encoding="UTF-8"?>\n<model unit="millimeter" xml:lang="en-US" {NS} '
                 f'requiredextensions="p"><metadata name="BambuStudio:3mfVersion">1</metadata><resources>'
                 + "".join(alt) + '</resources><build/></model>')
    ana = (f'<?xml version="1.0" encoding="UTF-8"?>\n<model unit="millimeter" xml:lang="en-US" {NS} requiredextensions="p">\n'
           f' <metadata name="Application">BambuStudio-01.10.00.00</metadata>\n'
           f' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
           f' <metadata name="Title">{ad}</metadata>\n'
           f' <resources>\n  <object id="{ana_id}" p:UUID="{uuid.uuid4()}" type="model">\n   <components>'
           + "".join(comps) + '</components>\n  </object>\n </resources>\n'
           f' <build p:UUID="{uuid.uuid4()}">\n  <item objectid="{ana_id}" p:UUID="{uuid.uuid4()}" '
           f'transform="1 0 0 0 1 0 0 0 1 128 128 0"/>\n </build>\n</model>\n')
    ayar = ('<?xml version="1.0" encoding="UTF-8"?>\n<config>\n'
            f'  <object id="{ana_id}">\n    <metadata key="name" value="{ad}"/>\n    <metadata key="extruder" value="1"/>\n'
            + "".join(parts) + '  </object>\n'
            '  <plate>\n    <metadata key="plater_id" value="1"/>\n    <metadata key="plater_name" value=""/>\n'
            '    <metadata key="locked" value="false"/>\n'
            f'    <model_instance>\n      <metadata key="object_id" value="{ana_id}"/>\n'
            '      <metadata key="instance_id" value="0"/>\n      <metadata key="identify_id" value="101"/>\n'
            '    </model_instance>\n  </plate>\n'
            '  <assemble>\n'
            f'   <assemble_item object_id="{ana_id}" instance_id="0" transform="1 0 0 0 1 0 0 0 1 128 128 0" offset="0 0 0" />\n'
            '  </assemble>\n</config>\n')
    tip = ('<?xml version="1.0" encoding="UTF-8"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
           '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
           '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>'
           '<Default Extension="config" ContentType="text/xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>'
            '</Relationships>')
    model_rels = ('<?xml version="1.0" encoding="UTF-8"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                  '<Relationship Target="/3D/Objects/object_1.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>'
                  '</Relationships>')
    with zipfile.ZipFile(yol, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", tip)
        z.writestr("_rels/.rels", rels)
        z.writestr("3D/3dmodel.model", ana)
        z.writestr("3D/_rels/3dmodel.model.rels", model_rels)
        z.writestr("3D/Objects/object_1.model", obj_model)
        z.writestr("Metadata/model_settings.config", ayar)
    return yol


def onizle(b):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import dis_konsept as K
    renk = {k: c for k, _, c in RENKLER}
    fig = plt.figure(figsize=(16, 7.5), dpi=110)
    for i, (elev, azim, bas) in enumerate(((22, 90, "Önden: turkuaz logo"), (62, 60, "Üstten: çukur, ışık halkası (beyaz), güneş halkası, yıldızlar"))):
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, [(m, renk[k], False) for k, m in b.items()], [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-62, 62); ax.set_ylim(-62, 62); ax.set_zlim(-30, 90)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(bas, fontsize=12)
    fig.suptitle("Renkli kabuk (Bambu P2S + AMS): 1 beyaz, 2 turkuaz, 3 sarı, 4 mor", fontsize=14)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", "renkli_kabuk.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def main():
    import trimesh
    b = bolgeler()
    toplam = sum(m.volume() for m in b.values())
    print("hacim: kabuk", round(C.kabuk().volume()), "parçalar toplamı", round(toplam),
          {k: round(m.volume()) for k, m in b.items()})
    d = os.path.join(C.KOK, "stl_cakil", "renkli_bambu")
    os.makedirs(d, exist_ok=True)
    bk = baski_konumu(b)
    tm = {k: temiz(m) for k, m in bk.items()}
    for k, m in tm.items():
        m.export(os.path.join(d, f"kabuk_{k}.stl"))
    parcalar = [(f"kabuk_{k}", ad, i + 1, tm[k]) for i, (k, ad, _) in enumerate(RENKLER)]
    print(yaz_3mf(os.path.join(d, "kabuk_renkli_bambu.3mf"), parcalar))
    print(onizle(b))
    for k, m in bk.items():
        t = trimesh.load(os.path.join(d, f"kabuk_{k}.stl"))
        print(k, "su geçirmez" if t.is_watertight else "AÇIK", "gövde", len(t.split(only_watertight=False)))


if __name__ == "__main__":
    main()
