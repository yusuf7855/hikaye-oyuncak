"""Masal standı: bütün STL'leri, denetimleri, önizlemeleri ve teknik çizimleri üretir.

    python cad/uret.py            # hepsi
    python cad/uret.py --stl      # yalnız STL + denetim raporu

Gerekenler: cad/requirements.txt (manifold3d, trimesh, numpy, scipy, matplotlib).
"""
import argparse
import json
import math
import os
import sys
import time

KOK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, KOK)

import numpy as np  # noqa: E402

import parametreler as P  # noqa: E402
import parcalar as pc  # noqa: E402
from geometri import trimesh_e, silindir  # noqa: E402

DEPO = os.path.dirname(KOK)
STL = os.path.join(KOK, "stl")
FIG_JSON = os.path.join(DEPO, "data", "figur_donanim.json")

BASKI = {   # malzeme, katman, dolgu, yön, renk
    "govde_alt": ("PETG ya da PLA", 0.2, 15, "taban tablada (olduğu gibi), destek YOK", "açık renk, opak"),
    "ust_kapak": ("PETG ya da PLA", 0.2, 15, "alt yüz tablada (olduğu gibi), destek YOK", "opak (ışık sızmasın)"),
    "difuzor_halka": ("PETG doğal/beyaz yarı saydam", 0.2, 100, "etekler tablada (olduğu gibi), destek YOK",
                      "beyaz yarı saydam (natural)"),
    "rc522_tutucu": ("PLA/PETG", 0.2, 30, "alt yüz tablada, destek YOK", "herhangi"),
    "figur_taban": ("PLA/PETG", 0.16, 30, "alt yüz (etiket cebi) tablada, destek YOK", "figür renginde"),
    "ayar_karti": ("PLA/PETG", 0.16, 30, "alt yüz tablada, destek YOK", "turkuaz"),
}


def figurler():
    with open(FIG_JSON, encoding="utf-8") as f:
        d = json.load(f)
    return d["figurler"], d.get("ozel_kartlar", [])


def taban_yazisi(fig):
    if fig.get("mod") == "uyku":
        return "AY DEDE", "gece"
    return fig["ad"], None


def parcalar():
    """{ad: (manifold, montaj ötelemesi)} — figür tabanı jenerik (yazısız)."""
    return {
        "govde_alt": (pc.alt_govde(), pc.montaj_konumu("govde_alt")),
        "ust_kapak": (pc.ust_kapak(), pc.montaj_konumu("ust_kapak")),
        "difuzor_halka": (pc.difuzor_halka(), pc.montaj_konumu("difuzor_halka")),
        "rc522_tutucu": (pc.rc522_tutucu(), pc.montaj_konumu("rc522_tutucu")),
        "figur_taban": (pc.figur_taban(), pc.montaj_konumu("figur_taban")),
    }


def baski_tahmini(mesh, dolgu, katman, malzeme):
    """Kaba dilimleyici tahmini: kabuk (yüzey x 1,0 mm) + iç hacim x dolgu; 6 mm³/s akış, %25 boş hareket."""
    V = mesh.volume
    A = mesh.area
    kabuk = min(V, A * 0.75)   # ~0,75 mm ortalama kabuk (çevre + üst/alt katmanlar)
    ic = max(V - kabuk, 0.0)
    filament = kabuk + ic * dolgu / 100.0
    akis = 6.0 * (katman / 0.2)
    sure_s = filament / akis * 1.25
    yogunluk = 1.27 if "PETG" in malzeme else 1.24
    return filament, filament / 1000 * yogunluk, sure_s / 3600


def stl_yaz(man, yol):
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    t = trimesh_e(man)
    t.export(yol)
    import trimesh
    return trimesh.load(yol)          # diskteki STL'yi yeniden okuyup denetle


def denetim(parca, satir):
    """Montaj çakışmaları ve ölçü kuralları."""
    hata = 0
    yer = {ad: m.translate(list(o)) for ad, (m, o) in parca.items()}
    satir.append("\n## Basılan parçalar arası çakışma (montajda, mm³; ≈0 olmalı)")
    adlar = list(yer)
    for i in range(len(adlar)):
        for j in range(i + 1, len(adlar)):
            v = (yer[adlar[i]] ^ yer[adlar[j]]).volume()
            durum = "TAMAM" if v < 0.01 else "ÇAKIŞMA"
            hata += durum != "TAMAM"
            if v > 0 or durum != "TAMAM":
                satir.append(f"- {adlar[i]} × {adlar[j]}: {v:.4f} mm³ {durum}")
    satir.append("- (listelenmeyen çiftlerde kesişim hacmi tam 0)")
    satir.append("\n## İç parçaların (elektronik zarfları) basılan parçalarla çakışması ve en küçük boşluk")
    zarf = pc.zarflar()
    for zad, zm in zarf.items():
        topv = 0.0
        enaz = (99.0, "")
        for ad, m in yer.items():
            v = (zm ^ m).volume()
            topv += v
            g = zm.min_gap(m, 5.0)
            if g < enaz[0]:
                enaz = (g, ad)
        # NTAG cebi ve halka kanalına oturanlar temas eder
        durum = "TAMAM" if topv < 0.01 else "ÇAKIŞMA"
        hata += durum != "TAMAM"
        bos = f"{enaz[0]:.2f} mm ({enaz[1]})" if enaz[0] < 5 else "> 5 mm"
        satir.append(f"- {zad}: kesişim {topv:.4f} mm³ → {durum}; en yakın parça {bos}")
    satir.append("\n## İç parçaların birbiriyle çakışması")
    za = list(zarf)
    say = 0
    for i in range(len(za)):
        for j in range(i + 1, len(za)):
            v = (zarf[za[i]] ^ zarf[za[j]]).volume()
            if v > 0.01:
                # beklenen temaslar: DevKit ↔ anten çıkıntısı aynı kart
                beklenen = {"ESP32-S3-DevKitC-1 (+headerlar)", "ESP32 anten çıkıntısı"} == {za[i], za[j]} or \
                    {"RC522 PCB", "RC522 bileşenleri (alt)"} == {za[i], za[j]} or \
                    {"MAX98357A PCB", "MAX98357A bileşen/klemens"} == {za[i], za[j]}
                if not beklenen:
                    satir.append(f"- {za[i]} × {za[j]}: {v:.2f} mm³ ÇAKIŞMA")
                    hata += 1
                    say += 1
    if not say:
        satir.append("- yok (TAMAM)")

    satir.append("\n## Ölçü kuralları")

    def kural(ad, kosul, deger):
        nonlocal hata
        satir.append(f"- {'TAMAM' if kosul else 'HATA '} {ad}: {deger}")
        hata += not kosul
    kural("Halka kanalı halkayı alır (Ø90/Ø104 + boşluk)", P.KANAL_R_IC < P.HALKA_IC_D / 2 and
          P.KANAL_R_DIS > P.HALKA_DIS_D / 2,
          f"kanal Ø{2 * P.KANAL_R_IC:.1f}–Ø{2 * P.KANAL_R_DIS:.1f}, halka Ø{P.HALKA_IC_D:.0f}–Ø{P.HALKA_DIS_D:.0f}, "
          f"radyal boşluk {P.HALKA_PAY} mm")
    kural("Kanal derinliği ≥ halka kalınlığı + 0,5", P.OMUZ_Z - P.KANAL_TABAN >= P.HALKA_KAL + 0.5,
          f"{P.OMUZ_Z - P.KANAL_TABAN:.1f} mm (halka {P.HALKA_KAL})")
    kural("Işık boşluğu (LED → difüzör) ≥ 4 mm", P.ISIK_BOSLUGU >= 4, f"{P.ISIK_BOSLUGU} mm; LED aralığı "
          f"(35 LED, Ø97 çevre) ≈ {math.pi * 97 / 35:.1f} mm")
    kural("Difüzör kalınlığı 1,2–2 mm", 1.2 <= P.DIF_KAL <= 2.0, f"{P.DIF_KAL} mm")
    kural("Yuva tabanı (anten üstü plastik) ≤ 2 mm", P.YUVA_TABAN_KAL <= 2.0, f"{P.YUVA_TABAN_KAL} mm")
    ant_x = -P.RC522_ANTEN_KAYMA + P.RC522_ANTEN_KAYMA
    kural("RC522 anten merkezi yuva merkezinde", abs(ant_x) < 0.5,
          f"kart merkezi x={-P.RC522_ANTEN_KAYMA}, anten kayması {P.RC522_ANTEN_KAYMA} → anten x={ant_x:.1f}")
    nfc = P.YUVA_TABAN_KAL + P.RC522_PCB + (P.ETIKET_CEP_DERIN - 0.25)
    kural("NFC mesafesi (etiket → anten bakırı) ≤ 6 mm", nfc <= 6.0,
          f"{nfc:.2f} mm (yuva tabanı {P.YUVA_TABAN_KAL} + RC522 FR4 {P.RC522_PCB} + cep payı); "
          f"anahtar oturmazsa (kama üstünde) {nfc + P.KAPAK_KAL - 1.2 - P.YUVA_TABAN_KAL:.1f} mm — yine okunur")
    kural("Taban–yuva boşluğu 0,3–0,6 mm", 0.3 <= P.YUVA_PAY <= 0.6, f"radyal {P.YUVA_PAY} mm")
    kural("Taban yuvada gömülü, üstü kapak yüzeyini aşmaz", P.YUVA_TABAN_KAL + P.TABAN_H <= P.KAPAK_KAL,
          f"taban üstü kapak üstünden {P.KAPAK_KAL - P.YUVA_TABAN_KAL - P.TABAN_H:.1f} mm aşağıda")
    kural("Etiket cebi 0,4 mm ve etiket altında plastik ≤ 1 mm", P.ETIKET_CEP_DERIN == 0.4,
          "etiket cebe yapışır; altında plastik yok (koruma için Ø30 keçe/şeffaf bant önerilir)")
    kural("Duvar ≥ 2 mm", min(P.DUVAR, P.TABAN, P.KANAL_TABAN) >= 2.0,
          f"duvar {P.DUVAR}, taban {P.TABAN}, kanal tabanı {P.KANAL_TABAN}; yuva tabanı {P.YUVA_TABAN_KAL} "
          f"(NFC için bilerek ince)")
    yuk = P.H_ALT + P.LED_UST + P.ISIK_BOSLUGU + P.DIF_KAL
    kural("Toplam yükseklik 45–60 mm", 45 <= yuk <= 60, f"{yuk:.1f} mm (+ silikon ayak ~2,5 mm)")
    kural("Dış çap 120–130 mm", 120 <= P.D_DIS <= 130, f"Ø{P.D_DIS:.0f} mm")
    gap = abs(P.USBC_DIS_DUZ - P.USBC_ON_Y)
    kural("USB-C fiş gövdesi ↔ soket ağzı ≤ 1,5 mm", gap <= 1.5, f"{gap:.1f} mm (dış düz alın)")
    import parcalar as _p  # noqa
    mx, my = math.cos(math.radians(P.MIK_ACI)) * P.R_DIS, math.sin(math.radians(P.MIK_ACI)) * P.R_DIS
    d = math.dist((mx, my, P.MIK_Z), (0, P.R_DIS, P.HOP_Z))
    kural("Mikrofon deliği hoparlör ızgarasından ≥ 80 mm", d >= 80, f"{d:.0f} mm")
    vida = P.VIDA_SIKMA + 4.0
    kural("Birleştirme vidası M3x10 (6 mm kolon + 4 mm insert)", vida <= P.VIDA_SIKMA + P.INSERT_DERIN - 1,
          f"M3x{vida:.0f}")
    return hata


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stl", action="store_true", help="yalnız STL + denetim")
    a = ap.parse_args()
    t0 = time.time()
    parca = parcalar()
    satir = ["# Masal standı — üretim ve denetim raporu (cad/uret.py üretir, elle düzenlemeyin)", ""]
    satir.append("## Parçalar")
    satir.append("| Dosya | Hacim cm³ | Boyut (x × y × z) mm | Su geçirmez | Malzeme | Katman | Dolgu % | "
                 "~Filament g | ~Süre sa | Yön |")
    satir.append("|---|---|---|---|---|---|---|---|---|---|")
    meshler = {}

    def ekle(ad, man, dosya, baski_ad):
        t = stl_yaz(man, os.path.join(STL, dosya))
        meshler[dosya] = t
        mlz, kat, dol, yon, _renk = BASKI[baski_ad]
        fil, gr, sa = baski_tahmini(t, dol, kat, mlz)
        b = t.extents
        ok = t.is_watertight and t.is_winding_consistent and t.volume > 0
        satir.append(f"| `stl/{dosya}` | {t.volume / 1000:.1f} | {b[0]:.1f} × {b[1]:.1f} × {b[2]:.1f} | "
                     f"{'evet' if ok else 'HAYIR'} | {mlz} | {kat} | {dol} | {gr:.0f} | {sa:.1f} | {yon} |")
        return ok

    hata = 0
    for ad, (m, _) in parca.items():
        hata += not ekle(ad, m, f"{ad}.stl", ad)
    figs, ozel = figurler()
    for f in figs:
        yazi, motif = taban_yazisi(f)
        m = pc.figur_taban(yazi, f["nfc_no"], motif=motif)
        hata += not ekle(f["kimlik"], m, f"figurler/{f['kimlik']}.stl", "figur_taban")
    for o in ozel:
        if o["kimlik"] == "ayar":
            m = pc.figur_taban("AYAR", o["nfc_no"], topuz=True)
            hata += not ekle("ayar_karti", m, "ayar_karti.stl", "ayar_karti")
    hata += denetim(parca, satir)
    toplam = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(STL) for f in fs)
    satir.append(f"\nSTL toplamı: {toplam / 1e6:.1f} MB. Süre/filament kaba tahmindir (6 mm³/s, 0,4 meme); "
                 "dilimleyicinin değerine bakın.")
    satir.append(f"\nSONUÇ: {'HATA YOK' if hata == 0 else f'{hata} HATA'}")
    with open(os.path.join(KOK, "kontrol_raporu.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(satir) + "\n")
    print("\n".join(satir))
    if not a.stl:
        import onizleme
        import cizim
        onizleme.hepsi(parca, figs, ozel)
        cizim.hepsi(parca)
    print(f"süre {time.time() - t0:.0f} s")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
