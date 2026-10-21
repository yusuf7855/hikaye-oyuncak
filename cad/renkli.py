"""Çok renkli baskı dosyaları (Bambu Lab P2S Combo / AMS, 4 renk): her parçanın renk bölgeleri ayrı gövdeler.

    python cad/renkli.py     # stl_cakil/renkli_bambu/: parça başına .3mf + renk başına STL; onizleme/renkli_*.png

Renkler (AMS yuvası = Bambu Studio'daki filament numarası):
  1 beyaz   2 turkuaz   3 sarı   4 mor
  kabuk     : beyaz gövde (LED'lerin üstündeki 0,6 mm ışık halkası BEYAZ kalmalı), turkuaz "eco ai" logosu ve çukur
              zemini, sarı çukur kenarı + "güneş" halkası, üstte 6 büyük mor yıldız
  taban     : beyaz plaka; alt yüzde, pil kapağının önünde turkuaz "eco ai" (alttan okunur)
  pil kapağı: beyaz; dış yüzde turkuaz "4 x AA / 1,5 V"
  tutucu    : beyaz (LED ışığını yansıtır); montajda görünen yüzünde turkuaz "ÖN" ve ok
  figür     : turkuaz jeton, üst yüzde sarı halka (11 adet, tek tablada)
  ayar kartı: mor jeton ve topuz, topuzun tepesinde beyaz çark, jetonun üstünde sarı halka
Kakmaların çoğu baskının ilk/son 3 katmanında (az renk değişimi); kabuğun logosu dikey duvarda olduğu için logo
boyunca her katmanda renk değişir (atık kulesi / prime tower açık kalmalı).
"""
import math
import os
import sys
import uuid
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cakil_ic as C  # noqa: E402
from geometri import CS, cokgen, silindir, dondur, xz_den_y_ye, yazi_duz, yildiz  # noqa: E402

KAKMA = 0.6
RENKLER = [("1_beyaz", "beyaz", "#F4F1EA"), ("2_turkuaz", "turkuaz", "#1FB5B0"),
           ("3_sari", "sarı", "#F6C33B"), ("4_mor", "mor", "#7A4FD0")]
RENK_NO = {k: i + 1 for i, (k, _, _) in enumerate(RENKLER)}
YILDIZ_ACI = 60.0                   # önde ortada yıldız yok, logonun iki yanında birer tane (simetrik)
YILDIZ_R, YILDIZ_BOY, YILDIZ_ADET = 48.1, 6.8, 6     # ürün sahibi (21 Ekim 2026): büyük, üstten bakınca güneş halkası (r 38,2) ile
                                                    # dış kenar (r ≈ 58) arasında ortalı; kabuğun yüzünü (omzu) izler
TABLA = 256.0                       # P2S tablası 256 x 256


def _bol(g, renkli, taban_renk="1_beyaz"):
    """renkli: {renk: bölge}; bölgeler g ile kesilir, kalan taban rengi olur. Parçalar birbirine değmez."""
    out = {}
    kalan = g
    for k, m in renkli.items():
        p = m ^ g
        kalan = kalan - p
        out[k] = p
    out[taban_renk] = kalan
    return {k: v for k, v in out.items() if not v.is_empty()}


def _yildizlar(r, boy, adet, aci0=90.0):
    s = None
    for i in range(adet):
        a = aci0 + 360.0 * i / adet
        y = yildiz(r * math.cos(math.radians(a)), r * math.sin(math.radians(a)), boy, boy * 0.45, aci0=a)
        s = y if s is None else s + y
    return s


def _halka(r0, r1, z0, z1):
    return silindir(r1, z0, z1, seg=C.SEG) - silindir(r0, z0 - 1, z1 + 1, seg=C.SEG)


# ---------------------------------------------------------------- parçalar (kullanım konumunda, z yukarı)
def kabuk_renk():
    g = C.kabuk()
    H, seg = C.H, C.SEG
    logo = (xz_den_y_ye(yazi_duz(C.YAZI, C.YAZI_BOY, C.FONT, ayna=True), 0, 80, x=0, z=C.YAZI_Z)
            ^ dondur(C.profil(1.2), seg)) - dondur(C.profil(-1.3), seg)   # harf kökü 1,3 mm (0,8 / 1,0 sınırlarına değmesin)
    zemin = silindir(C.YUVA_R + 0.01, C.Z_CANAK_TABAN - KAKMA, C.Z_CANAK_TABAN + 0.01, seg=seg)
    sari = _halka(C.YUVA_R - 0.01, C.ISIK_R[0] - 0.4, H - KAKMA, H + 1) + _halka(C.ISIK_R[1] + 0.6, C.ISIK_R[1] + 3.6, H - KAKMA, H + 1)
    deri = dondur(C.profil(1.0, 0.0, H + 1.0), seg) - dondur(C.profil(-KAKMA, 0.0, H - KAKMA), seg)   # yüzeyin 0,6 mm'lik derisi (üst yüz dahil)
    mor = _yildizlar(YILDIZ_R, YILDIZ_BOY, YILDIZ_ADET, aci0=YILDIZ_ACI).extrude(30).translate([0, 0, H - 25]) ^ deri
    return _bol(g, {"2_turkuaz": logo + zemin, "3_sari": sari, "4_mor": mor})


def taban_renk():
    """Alt yüz (tablada): alttan bakınca okunur (ayna)."""
    g = C.taban()
    alt = lambda cs: cs.extrude(KAKMA + 1).translate([0, 0, -1])   # noqa: E731
    yazi = alt(yazi_duz(C.YAZI, 8.0, C.FONT, ayna=True).translate([0, 28.5]))   # ortası pil kapağı: yazı önde
    return _bol(g, {"2_turkuaz": yazi})


def pil_kapagi_renk():
    g = C.pil_kapagi(yazi_ile=False)
    return _bol(g, {"2_turkuaz": C.pil_kapak_yazi().extrude(KAKMA + 1).translate([0, 0, -1])})


def tutucu_renk(nfc):
    """Montajda (kabuk ters dururken) görünen yüz plakanın alt yüzü: orada "ÖN" ve öne bakan ok (ayna: alttan okunur)."""
    g = C.tutucu(nfc)
    zt = C.Z_TUTUCU_ALT
    # plakanın yan tarafında (raylardan uzak): "ÖN" ve üstünde öne (+y) bakan ok
    xm = -(C.CANAK_GOVDE_R + C.PARCA["halka"][1] / 2 + 2.9) / 2        # plaka halkasının ortası (Ø70 halkayla büyüdü)
    on = yazi_duz("ÖN", 3.4, C.FONT, ayna=True).translate([xm, -1.4])
    ok = CS([cokgen([(xm - 1.8, 1.6), (xm + 1.8, 1.6), (xm, 5.0)])])
    sekil = (on + ok).extrude(KAKMA + 1).translate([0, 0, zt - 1])
    return _bol(g, {"2_turkuaz": sekil})


def figur_renk():
    g = C.figur_taban()
    h = C.FIGUR_BOY
    return _bol(g, {"3_sari": _halka(C.FIGUR_TABAN_D / 2 - 3.6, C.FIGUR_TABAN_D / 2 - 1.4, h - KAKMA, h + 1)}, taban_renk="2_turkuaz")


def ay_renk():
    """Ay Dede: turkuaz taban, sarı hilal ay."""
    from geometri import kutu
    g = C.ay_dede()
    return _bol(g, {"3_sari": kutu(-40, 40, -40, 40, C.FIGUR_BOY, 90)}, taban_renk="2_turkuaz")


def ayar_renk():
    g = C.figur_taban(topuz=True)
    h = C.FIGUR_BOY
    tepe = h + 12.0
    dis = []
    for i in range(16):   # 8 dişli çark
        a = math.radians(i * 22.5)
        r = 5.4 if i % 2 == 0 else 4.2
        for da in (-0.17, 0.17):
            dis.append((r * math.cos(a + da), r * math.sin(a + da)))
    cark = (CS([cokgen(dis)]) - CS.circle(1.7, 32)).extrude(KAKMA + 1).translate([0, 0, tepe - KAKMA])
    return _bol(g, {"1_beyaz": cark, "3_sari": _halka(C.FIGUR_TABAN_D / 2 - 3.6, C.FIGUR_TABAN_D / 2 - 1.4, h - KAKMA, h + 0.01)}, taban_renk="4_mor")


# ---------------------------------------------------------------- baskı konumu, dosyalar
def baski_konumu(b, ters):
    """Parçanın STL'deki baskı yönü: ters=True ise x ekseni etrafında 180°; x-y ortada, z = 0'dan."""
    d = {k: (m.rotate([180, 0, 0]) if ters else m) for k, m in b.items()}
    hepsi = None
    for m in d.values():
        hepsi = m if hepsi is None else hepsi + m
    bb = hepsi.bounding_box()
    t = [-(bb[0] + bb[3]) / 2, -(bb[1] + bb[4]) / 2, -bb[2]]
    return {k: m.translate(t) for k, m in d.items()}


def temiz(man):
    """Boole işlemlerinin bıraktığı hacimsiz kırıntıları at (dilimleyici uyarı vermesin)."""
    import trimesh
    t = C._tm(man)
    t.merge_vertices()
    parca = [p for p in t.split(only_watertight=False) if abs(p.volume) > 0.01]
    return trimesh.util.concatenate(parca)


def _mesh_xml(oid, t):
    vs = "".join(f'<vertex x="{a:.4f}" y="{b:.4f}" z="{c:.4f}"/>' for a, b, c in t.vertices)
    ts = "".join(f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in t.faces)
    return (f'<object id="{oid}" p:UUID="{uuid.uuid4()}" type="model"><mesh><vertices>{vs}</vertices>'
            f'<triangles>{ts}</triangles></mesh></object>')


def yaz_3mf(yol, nesneler):
    """Bambu Studio proje biçimi (3MF + production uzantısı). nesneler: [(ad, [(parça adı, filament no, trimesh)], (x, y))];
    her nesne tek tablada, renk başına bir parça; filament numaraları Metadata/model_settings.config'te."""
    NS = ('xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
          'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
          'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"')
    alt, kaynak, build, ayar_n, ornek, montaj = [], [], [], [], [], []
    oid = 0
    ana_idler = []
    for ad, parcalar, (x, y) in nesneler:
        comps, parts = [], []
        for pad, extr, tm in parcalar:
            oid += 1
            alt.append(_mesh_xml(oid, tm))
            comps.append(f'<component p:path="/3D/Objects/object_1.model" objectid="{oid}" p:UUID="{uuid.uuid4()}" '
                         f'transform="1 0 0 0 1 0 0 0 1 0 0 0"/>')
            parts.append(f'    <part id="{oid}" subtype="normal_part">\n      <metadata key="name" value="{pad}"/>\n'
                         f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
                         f'      <metadata key="extruder" value="{extr}"/>\n'
                         f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
                         f'    </part>\n')
        ana_idler.append((ad, comps, parts, x, y))
    for n, (ad, comps, parts, x, y) in enumerate(ana_idler):
        aid = oid + 1 + n
        tr = f"1 0 0 0 1 0 0 0 1 {x:.3f} {y:.3f} 0"
        kaynak.append(f'  <object id="{aid}" p:UUID="{uuid.uuid4()}" type="model">\n   <components>' + "".join(comps)
                      + '</components>\n  </object>\n')
        build.append(f'  <item objectid="{aid}" p:UUID="{uuid.uuid4()}" transform="{tr}"/>\n')
        ayar_n.append(f'  <object id="{aid}">\n    <metadata key="name" value="{ad}"/>\n    <metadata key="extruder" value="1"/>\n'
                      + "".join(parts) + '  </object>\n')
        ornek.append(f'    <model_instance>\n      <metadata key="object_id" value="{aid}"/>\n'
                     f'      <metadata key="instance_id" value="0"/>\n      <metadata key="identify_id" value="{101 + n}"/>\n'
                     '    </model_instance>\n')
        montaj.append(f'   <assemble_item object_id="{aid}" instance_id="0" transform="{tr}" offset="0 0 0" />\n')
    obj_model = (f'<?xml version="1.0" encoding="UTF-8"?>\n<model unit="millimeter" xml:lang="en-US" {NS} '
                 f'requiredextensions="p"><metadata name="BambuStudio:3mfVersion">1</metadata><resources>'
                 + "".join(alt) + '</resources><build/></model>')
    ana = (f'<?xml version="1.0" encoding="UTF-8"?>\n<model unit="millimeter" xml:lang="en-US" {NS} requiredextensions="p">\n'
           ' <metadata name="Application">BambuStudio-01.10.00.00</metadata>\n'
           ' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
           f' <metadata name="Title">{os.path.splitext(os.path.basename(yol))[0]}</metadata>\n'
           ' <resources>\n' + "".join(kaynak) + ' </resources>\n'
           f' <build p:UUID="{uuid.uuid4()}">\n' + "".join(build) + ' </build>\n</model>\n')
    ayar = ('<?xml version="1.0" encoding="UTF-8"?>\n<config>\n' + "".join(ayar_n)
            + '  <plate>\n    <metadata key="plater_id" value="1"/>\n    <metadata key="plater_name" value=""/>\n'
            '    <metadata key="locked" value="false"/>\n' + "".join(ornek) + '  </plate>\n'
            '  <assemble>\n' + "".join(montaj) + '  </assemble>\n</config>\n')
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


def onizle(parcalar):
    """parcalar: [(başlık, {renk: manifold (kullanım konumunda)}, elev, azim)]"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import dis_konsept as K
    renk = {k: c for k, _, c in RENKLER}
    sutun = (len(parcalar) + 1) // 2
    fig = plt.figure(figsize=(6 * sutun, 11), dpi=100)
    for i, (bas, b, elev, azim) in enumerate(parcalar):
        ax = fig.add_subplot(2, sutun, i + 1, projection="3d")
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, [(m, renk[k], False) for k, m in b.items()], [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        hepsi = None
        for m in b.values():
            hepsi = m if hepsi is None else hepsi + m
        bb = hepsi.bounding_box()
        s = max(bb[3] - bb[0], bb[4] - bb[1], bb[5] - bb[2]) / 2 + 1
        c = [(bb[0] + bb[3]) / 2, (bb[1] + bb[4]) / 2, (bb[2] + bb[5]) / 2]
        ax.set_xlim(c[0] - s, c[0] + s); ax.set_ylim(c[1] - s, c[1] + s); ax.set_zlim(c[2] - s, c[2] + s)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(bas, fontsize=11)
    fig.suptitle("Renkli parçalar (Bambu P2S + AMS): 1 beyaz, 2 turkuaz, 3 sarı, 4 mor", fontsize=15)
    plt.tight_layout()
    yol = os.path.join(C.KOK, "onizleme", "renkli_parcalar.png")
    fig.savefig(yol)
    plt.close(fig)
    return yol


def main():
    import trimesh
    d = os.path.join(C.KOK, "stl_cakil", "renkli_bambu")
    os.makedirs(d, exist_ok=True)
    for eski in os.listdir(d):
        if eski.endswith((".stl", ".3mf")):
            os.remove(os.path.join(d, eski))
    # (dosya adı, renk bölgeleri, baskıda ters mi, tablada adet)
    isler = [("1_kabuk", kabuk_renk(), True, 1), ("2_taban_plakasi", taban_renk(), False, 1),
             ("2b_pil_kapagi", pil_kapagi_renk(), False, 1),
             ("3_halka_nfc_tutucu_rc522", tutucu_renk("rc522"), True, 1),
             ("3_halka_nfc_tutucu_pn5180", tutucu_renk("pn5180"), True, 1)]
    figur, ayar = figur_renk(), ayar_renk()
    hata = 0
    for ad, b, ters, _ in isler + [("4_figur_taban", figur, True, 11), ("5_ayar_karti", ayar, False, 1)]:
        hacim = sum(m.volume() for m in b.values())
        bk = baski_konumu(b, ters)
        tm = {k: temiz(m) for k, m in bk.items()}
        for k, m in tm.items():
            m.export(os.path.join(d, f"{ad}_{k}.stl"))
            t = trimesh.load(os.path.join(d, f"{ad}_{k}.stl"))
            if not t.is_watertight:
                hata += 1
                print("  AÇIK:", ad, k)
        parcalar = [(f"{ad}_{k}", RENK_NO[k], tm[k]) for k in RENK_NO if k in tm]
        if ad == "4_figur_taban":   # tüm figür tabanları, Ay Dede, ayar kartı ve adlı kapaklar aynı tablada
            import figurler as F
            def renkli_parca(b, ters, ad_):
                bk_ = baski_konumu(b, ters)
                return [(f"{ad_}_{k}", RENK_NO[k], temiz(bk_[k])) for k in RENK_NO if k in bk_]
            figs, ozel = F.figur_listesi()
            ap = renkli_parca(ayar, False, "ayar_karti")
            ay = renkli_parca(ay_renk(), False, "ay_dede")
            nes = []
            for f in figs:
                nes.append((f"{f['nfc_no']:02d}_{f['kimlik']}", ay if f.get("mod") == "uyku" else parcalar))
            nes.append(("200_ayar_karti", ap))
            for f in figs + [o for o in ozel if o["kimlik"] == "ayar"]:
                ad_k = "AYAR" if f["kimlik"] == "ayar" else f["ad"].replace("i", "İ").replace("ı", "I").upper()
                kp = baski_konumu({"3_sari": C.figur_kapak(ad_k, f["nfc_no"])}, False)
                nes.append((f"kapak_{f['nfc_no']:02d}_{f['kimlik']}", [(f"kapak_{f['kimlik']}", 3, temiz(kp["3_sari"]))]))
            tabanlar = [n for n in nes if not n[0].startswith("kapak_")]
            kapaklar = [n for n in nes if n[0].startswith("kapak_")]
            yer = [(TABLA / 2 + (i % 4 - 1.5) * 58, TABLA / 2 + (1.5 - i // 4) * 58) for i in range(len(tabanlar))]
            print(yaz_3mf(os.path.join(d, "4a_figur_tabanlari_ay_dede_ayar_karti.3mf"),
                          [(a, p, xy) for (a, p), xy in zip(tabanlar, yer)]))
            yer = [(TABLA / 2 + (i % 5 - 2) * 38, TABLA / 2 + (1 - i // 5) * 38) for i in range(len(kapaklar))]
            print(yaz_3mf(os.path.join(d, "4b_nfc_kapaklari.3mf"), [(a, p, xy) for (a, p), xy in zip(kapaklar, yer)]))
        elif ad != "5_ayar_karti":
            print(yaz_3mf(os.path.join(d, f"{ad}.3mf"), [(ad, parcalar, (TABLA / 2, TABLA / 2))]))
        print(f"  {ad}: hacim {hacim:.0f} mm³;", {k: round(m.volume()) for k, m in b.items()})
    print(onizle([("1) kabuk", isler[0][1], 30, 70), ("2) taban plakası (alttan)", isler[1][1], -55, 90),
                  ("3) tutucu (montajda görünen alt yüzü)", isler[3][1], -60, 90), ("2b) pil kapağı (alttan)", isler[2][1], -60, 90),
                  ("4) figür tabanı", figur, 40, 60), ("5) ayar kartı", ayar, 35, 60),
                  ("1) kabuk önden", isler[0][1], 15, 90)]))
    print("açık (su geçirmeyen) dosya:", hata)


if __name__ == "__main__":
    main()
