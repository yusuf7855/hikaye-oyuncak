"""Çakıl stand parçalarını STEP olarak yazar (tek renkli tasarım, yıldızsız).

    python cad/step_yaz.py      # cad/step_cakil/: parça başına .step + montaj (tüm parçalar yerinde)

cakil_ic.py'deki aynı tasarım kodu, geometri.py yerine geometri_occ.py (OpenCASCADE) ile çalıştırılır: çıktı gerçek
B-rep katıdır (kavisli dış yüz düzgün B-spline, delikler gerçek silindir). Fusion 360 / SolidWorks / FreeCAD /
Onshape'te düzenlenebilir katı olarak açılır. Koordinat: mm, z yukarı, parçalar montajdaki yerinde (+y ön/logo,
-y arka/USB-C); ayar kartı kendi yerinde (z = 0).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geometri_occ  # noqa: E402
sys.modules["geometri"] = geometri_occ        # cakil_ic aynı kodla OCC katıları üretsin
import cakil_ic as C  # noqa: E402

from OCP.BRepCheck import BRepCheck_Analyzer  # noqa: E402
from OCP.STEPCAFControl import STEPCAFControl_Writer  # noqa: E402
from OCP.STEPControl import STEPControl_AsIs  # noqa: E402
from OCP.TDocStd import TDocStd_Document  # noqa: E402
from OCP.TCollection import TCollection_ExtendedString, TCollection_AsciiString  # noqa: E402
from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ColorType  # noqa: E402
from OCP.TDataStd import TDataStd_Name  # noqa: E402
from OCP.Quantity import Quantity_Color, Quantity_TypeOfColor  # noqa: E402
from OCP.Interface import Interface_Static  # noqa: E402

RENK = {"kabuk": (0.96, 0.94, 0.90), "taban_plakasi": (0.91, 0.86, 0.80), "halka_nfc_tutucu": (0.79, 0.76, 0.72),
        "figur_taban": (0.12, 0.71, 0.69), "figur_kapagi": (0.96, 0.76, 0.23),
        "ay_dede": (0.96, 0.76, 0.23), "ayar_karti": (0.48, 0.31, 0.82)}


def step_yaz(yol, parcalar):
    """parcalar: [(ad, OCC şekli)] -> adları ve renkleriyle tek STEP (AP214)."""
    doc = TDocStd_Document(TCollection_ExtendedString("XmlOcaf"))
    st = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    ct = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
    for ad, sh in parcalar:
        lab = st.AddShape(sh, False)
        TDataStd_Name.Set_s(lab, TCollection_ExtendedString(ad))
        r, g, b = RENK.get(ad.replace("_rc522", "").replace("_pn5180", ""), (0.8, 0.8, 0.8))
        ct.SetColor(lab, Quantity_Color(r, g, b, Quantity_TypeOfColor.Quantity_TOC_RGB), XCAFDoc_ColorType.XCAFDoc_ColorSurf)
    Interface_Static.SetCVal_s("write.step.unit", "MM")
    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    w = STEPCAFControl_Writer()
    w.SetNameMode(True)
    w.SetColorMode(True)
    w.Transfer(doc, STEPControl_AsIs)
    w.Write(TCollection_AsciiString(yol).ToCString())
    return yol


def main():
    d = os.path.join(C.KOK, "step_cakil")
    os.makedirs(d, exist_ok=True)
    for eski in os.listdir(d):
        if eski.endswith(".step"):
            os.remove(os.path.join(d, eski))
    parca = {"kabuk": C.kabuk(), "taban_plakasi": C.taban(),
             "halka_nfc_tutucu_rc522": C.tutucu("rc522"), "halka_nfc_tutucu_pn5180": C.tutucu("pn5180"),
             }   # figür tabanları (vida dişli) STL olarak: cad/stl_cakil/figurler/ (dişli sarmal OCC'de çok yavaş)
    for ad, m in parca.items():
        print(f"{ad}: hacim {m.volume():.0f} mm³, geçerli katı: {BRepCheck_Analyzer(m.sh).IsValid()}", flush=True)
        step_yaz(os.path.join(d, f"{ad}.step"), [(ad, m.sh)])
    for nfc in ("rc522", "pn5180"):
        adlar = ["kabuk", "taban_plakasi", f"halka_nfc_tutucu_{nfc}"]
        print(step_yaz(os.path.join(d, f"0_montaj_{nfc}.step"), [(a, parca[a].sh) for a in adlar]))


if __name__ == "__main__":
    main()
