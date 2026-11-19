"""icerik.py + finans.py -> doldurulmuş başvuru dosyaları (../cikti/).

Gerekenler: pypdf, python-docx, openpyxl; pandoc ve LibreOffice (soffice) Word->PDF için.
  python3 -m venv /tmp/v && /tmp/v/bin/pip install pypdf python-docx openpyxl
  /tmp/v/bin/python doldur.py
Üretilenler:
  cikti/AGY112_Is_Plani_Eko_DOLDURULMUS.pdf   resmi form, alanlar dolu (Adobe Acrobat Reader ile açın)
  cikti/AGY112_Is_Plani_Eko.docx / .pdf       aynı içerik, okunur/yazdırılır kopya
  ../02_IS_PLANI_AGY112.md                     kopyala-yapıştır için
  cikti/Tahmini_Maliyet_Formlari_Eko.docx      M011–M030 doldurulmuş
  cikti/Eko_Finansal_Model.xlsx                varsayımlar, projeksiyon, başa baş, bütçe, BOM
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(BURASI)
CIKTI = os.path.join(KOK, "cikti")
RESMI = os.path.join(KOK, "resmi")
sys.path.insert(0, BURASI)
import icerik  # noqa: E402
import finans  # noqa: E402

BASLIKLAR = {
    "1_1_urun_tanimi": "1.1 Ürün Tanımı",
    "1_2_musteri_tanimi": "1.2 Müşteri Tanımı",
    "1_3_musteri_ihtiyaclari": "1.3 Müşteri İhtiyaçları",
    "1_4_pazar_buyuklugu": "1.4 Pazar Büyüklüğü",
    "1_5_rekabet_durumu": "1.5 Rekabet Durumu",
    "1_6_rekabet_stratejisi": "1.6 Rekabet Stratejisi",
    "1_7_engelleyici_faktorler": "1.7 Engelleyici Faktörler",
    "1_8_sosyal_fayda": "1.8 Sosyal Fayda",
    "2_1_deger_onerisi": "2.1 Değer Önerisi",
    "2_2_teknolojik_rekabet": "2.2 Teknolojik Rekabet",
    "2_3_urun_fiyati": "2.3 Ürün Fiyatı",
    "2_4_urun_maliyeti": "2.4 Ürün Maliyeti",
    "2_6_fikri_mulkiyet_haklari": "2.6 Fikri Mülkiyet Hakları",
    "2_7_regulasyonlar": "2.7 Regülasyonlar",
    "3_1_ekip_deneyim": "3.1 Ekip ve Deneyim",
    "3_2_ortaklik_yapisi": "3.2 Ortaklık Yapısı",
    "3_3_is_paylasimi": "3.3 İş Paylaşımı",
    "3_4_isbirlikleri": "3.4 İşbirlikleri",
    "3_5_misyon_degerler": "3.5 Ekibin Misyonu ve Değerleri",
    "4_1_is_modeli": "4.1 İş Modeli",
    "4_2_musteriye_erisim": "4.2 Müşteriye Erişim",
    "4_5_yatirimci_iliskisi": "4.5 Yatırımcı İlişkileri",
}
SIRA = ["1_1_urun_tanimi", "1_2_musteri_tanimi", "1_3_musteri_ihtiyaclari", "1_4_pazar_buyuklugu",
        "1_5_rekabet_durumu", "1_6_rekabet_stratejisi", "1_7_engelleyici_faktorler", "1_8_sosyal_fayda",
        "2_1_deger_onerisi", "2_2_teknolojik_rekabet", "2_3_urun_fiyati", "2_4_urun_maliyeti", "TEKNIK",
        "2_6_fikri_mulkiyet_haklari", "2_7_regulasyonlar", "3_1_ekip_deneyim", "3_2_ortaklik_yapisi",
        "3_3_is_paylasimi", "3_4_isbirlikleri", "3_5_misyon_degerler", "4_1_is_modeli", "4_2_musteriye_erisim",
        "KRITIK", "BASABAS", "4_5_yatirimci_iliskisi", "RISK"]
BOLUM = {"1_1_urun_tanimi": "1 Pazar Fırsatı", "2_1_deger_onerisi": "2 Ürün ve Teknoloji",
         "3_1_ekip_deneyim": "3 Ekip", "4_1_is_modeli": "4 İş Modeli ve Finansal Öngörüler",
         "RISK": "5 Risk Yönetimi"}

# AGY 112 PDF tablo alanları (sayfa düzeninden çıkarıldı: satır satır, soldan sağa)
TEKNIK_HUCRE = [["fill_1_5", "fill_2_4", "fill_3", "fill_4"], ["fill_5", "fill_6", "fill_7", "fill_8"],
                ["fill_9", "fill_10", "fill_11", "fill_12"], ["fill_13", "fill_14", "fill_15", "fill_16"],
                ["fill_17", "fill_18", "fill_19", "fill_20"], ["fill_21", "fill_22", "fill_23", "fill_24"],
                ["fill_25", "fill_26", "fill_27", "fill_28"], ["fill_29", "fill_30", "fill_31", "fill_32"]]
KRITIK_HUCRE = [["fill_1_9", "fill_2_7", "fill_3_2"], ["fill_4_2", "fill_5_2", "fill_6_2"],
                ["fill_7_2", "fill_8_2", "fill_9_2"], ["fill_10_2", "fill_11_2", "fill_12_2"],
                ["fill_13_2", "fill_14_2", "fill_15_2"], ["fill_16_2", "fill_17_2", "fill_18_2"],
                ["fill_19_2", "fill_20_2", "fill_21_2"], ["fill_22_2", "fill_23_2", "fill_24_2"],
                ["fill_25_2", "fill_26_2", "fill_27_2"], ["fill_28_2", "fill_29_2", "fill_30_2"],
                ["fill_31_2", "fill_32_2", "fill_33"], ["fill_34_2", "fill_35_2", "fill_36"],
                ["fill_37", "fill_38", "fill_39"], ["fill_40", "fill_41", "fill_42"],
                ["fill_43", "fill_44", "fill_45"], ["fill_46", "fill_47", "fill_48"]]


def tl(x, ondalik=0):
    s = f"{x:,.{ondalik}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s


def denetle():
    sorun = []
    for k, v in icerik.ALANLAR.items():
        n = len(v)
        if n > 3000:
            sorun.append(f"{k}: {n} karakter (> 3000)")
        print(f"  {k:32s} {n:5d} karakter")
    assert len(icerik.KRITIK_ADIMLAR) <= len(KRITIK_HUCRE)
    assert len(icerik.TEKNIK_DURUM) <= len(TEKNIK_HUCRE)
    if sorun:
        sys.exit("Karakter sınırı aşıldı:\n" + "\n".join(sorun))


def pdf_doldur(bb):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import NameObject, BooleanObject, TextStringObject
    r = PdfReader(os.path.join(RESMI, "1812_agy_112_pdf_form_v1.2.pdf"))
    w = PdfWriter()
    w.append(r)
    deger = dict(icerik.ALANLAR)
    for satir, hucre in zip(icerik.TEKNIK_DURUM, TEKNIK_HUCRE):
        for v, h in zip(satir, hucre):
            deger[h] = v
    for satir, hucre in zip(icerik.KRITIK_ADIMLAR, KRITIK_HUCRE):
        for v, h in zip(satir, hucre):
            deger[h] = v
    deger.update({
        "4_4_1_urun_adedi": str(bb["adet"]), "satisfiyati": str(bb["fiyat"]),
        "4_4_1_satis_gelirleri": str(bb["satis"]), "4_4_1_diger_gelirler": str(bb["diger_gelir"]),
        "4_4_1_toplam_gelir": str(bb["toplam_gelir"]),
        "4_4_2_personel_maliyeti": str(bb["personel"]), "4_4_2_malzeme_maliyeti": str(bb["malzeme"]),
        "4_4_2_enerji_maliyeti": str(bb["enerji"]), "4_4_2_dagitim_maliyeti": str(bb["dagitim"]),
        "4_4_2_diger_degisken": str(bb["diger_degisken"]), "birimurunmaliyeti": str(bb["birim"]),
        "4_4_3_makine_techizat": str(bb["makine"]), "4_4_3_amortisman": "0", "4_4_3_kira_giderleri": str(bb["kira"]),
        "4_4_3_diger_sabit_maliyet": str(bb["diger_sabit"]), "toplamsabitmaliyet": str(bb["toplam_sabit"]),
        "karmarji": str(bb["marj"]), "basabasurunadedi": str(bb["basabas"]),
    })
    for i, (tanim, onlem, ol, etki, b) in enumerate(icerik.RISKLER, 1):
        deger[f"risk_tanim_{i}"] = tanim
        deger[f"ÖnlemlerRow{i}"] = onlem
        deger[f"risk_b_plani_{i}"] = b
        deger[f"risk_olasilik_{i}"] = ol
        deger[f"risk_etki_{i}"] = etki
    alanlar = set(r.get_fields().keys())
    eksik = [k for k in deger if k not in alanlar]
    assert not eksik, eksik
    # Uzun metin alanlarında yazı boyutu otomatik olsun (form 8 pt sabit; 3000 karakter kutuya sığmıyor)
    for sayfa in w.pages:
        for a in sayfa.get("/Annots", []) or []:
            a = a.get_object()
            ad = a.get("/T")
            if ad in icerik.ALANLAR:
                a[NameObject("/DA")] = TextStringObject("/Helv 0 Tf 0 g")
        w.update_page_form_field_values(sayfa, {k: v for k, v in deger.items()}, auto_regenerate=False)
    w._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)
    yol = os.path.join(CIKTI, "AGY112_Is_Plani_Eko_DOLDURULMUS.pdf")
    with open(yol, "wb") as f:
        w.write(f)
    # geri oku ve doğrula
    r2 = PdfReader(yol)
    f2 = r2.get_fields()
    bos = [k for k in deger if (f2[k].get("/V") or "") != deger[k]]
    assert not bos, bos[:5]
    print("PDF:", yol, len(deger), "alan dolduruldu")
    duzlestir(deger)


SAYI_ALANLARI = {"4_4_1_urun_adedi", "satisfiyati", "4_4_1_satis_gelirleri", "4_4_1_diger_gelirler",
                 "4_4_1_toplam_gelir", "4_4_2_personel_maliyeti", "4_4_2_malzeme_maliyeti", "4_4_2_enerji_maliyeti",
                 "4_4_2_dagitim_maliyeti", "4_4_2_diger_degisken", "birimurunmaliyeti", "4_4_3_makine_techizat",
                 "4_4_3_amortisman", "4_4_3_kira_giderleri", "4_4_3_diger_sabit_maliyet", "toplamsabitmaliyet",
                 "karmarji", "basabasurunadedi"}
ADET_ALANLARI = {"4_4_1_urun_adedi", "basabasurunadedi"}


def duzlestir(deger):
    """Formun düzleştirilmiş kopyası: alan metinleri Türkçe karakterli bir yazı tipiyle sayfaya çizilir.
    Formun yazı tipi (Helvetica) ğ, ş, ı, İ, Ğ, Ş içermediği için bazı PDF görüntüleyiciler alanlardaki Türkçe
    harfleri göstermiyor; bu kopya her görüntüleyicide ve çıktıda aynı görünür (alanlar düzenlenemez)."""
    import io
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.utils import simpleSplit
    yt = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    if not os.path.exists(yt):
        yt = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    pdfmetrics.registerFont(TTFont("TR", yt))
    r = PdfReader(os.path.join(RESMI, "1812_agy_112_pdf_form_v1.2.pdf"))
    w = PdfWriter()
    for sayfa in r.pages:
        gen, yuk = float(sayfa.mediabox.width), float(sayfa.mediabox.height)
        tampon = io.BytesIO()
        c = canvas.Canvas(tampon, pagesize=(gen, yuk))
        for a in sayfa.get("/Annots", []) or []:
            a = a.get_object()
            ad = a.get("/T")
            if ad is None and "/Parent" in a:
                ad = a["/Parent"].get_object().get("/T")
            if ad not in deger:
                continue
            x0, y0, x1, y1 = [float(v) for v in a["/Rect"]]
            v = deger[ad]
            if ad in SAYI_ALANLARI:
                v = tl(float(v)) + ("" if ad in ADET_ALANLARI else " TL")
            pay = 2.0
            gw, gh = x1 - x0 - 2 * pay, y1 - y0 - 2 * pay
            cok_satir = ad in icerik.ALANLAR or (y1 - y0) > 25
            if cok_satir:
                for boy in [9, 8.5, 8, 7.5, 7, 6.8, 6.5, 6.2, 6, 5.8, 5.5, 5.2, 5, 4.8, 4.5]:
                    satirlar = []
                    for par in v.split("\n"):
                        satirlar += simpleSplit(par, "TR", boy, gw) or [""]
                    if len(satirlar) * boy * 1.15 <= gh:
                        break
                c.setFont("TR", boy)
                yy = y1 - pay - boy
                for s in satirlar:
                    if yy < y0:
                        break
                    c.drawString(x0 + pay, yy, s)
                    yy -= boy * 1.15
            else:
                boy = 6.5
                while boy > 3.5 and pdfmetrics.stringWidth(v, "TR", boy) > gw:
                    boy -= 0.25
                c.setFont("TR", boy)
                c.drawString(x0 + pay, y0 + (y1 - y0 - boy) / 2 + 1, v)
        c.showPage()
        c.save()
        tampon.seek(0)
        ust = PdfReader(tampon).pages[0]
        yeni = w.add_page(sayfa)
        yeni.merge_page(ust)
        if "/Annots" in yeni:
            del yeni["/Annots"]
    yol = os.path.join(CIKTI, "AGY112_Is_Plani_Eko_DUZ_okuma_yazdirma.pdf")
    with open(yol, "wb") as f:
        w.write(f)
    print("PDF (düz):", yol)


def markdown(bb, oz):
    s = [f"# AGY 112 – İş Planı: {icerik.IS_FIKRI_ADI}", "",
         "> TÜBİTAK 1812 BiGG Yatırım, Aşama 2 iş planı formunun (AGY 112, v1.2) bütün alanları. Bu dosya "
         "`hazirla/icerik.py` ve `hazirla/finans.py`'den üretilir (`hazirla/doldur.py`); elle değiştirmeyin, "
         "kaynağı değiştirip yeniden üretin. Köşeli parantezli büyük harfli yerler ([AD SOYAD] gibi) sizin "
         "dolduracağınız kişisel bilgilerdir. [V] varsayım, [T] tahmin demektir.", "",
         f"**Tematik alan:** {icerik.TEMATIK_ALAN}", ""]
    for k in SIRA:
        if k in BOLUM:
            s += [f"## {BOLUM[k]}", ""]
        if k == "TEKNIK":
            s += ["### 2.5 Tekniğin Bilinen Durumu", "",
                  "| Buluş başlığı | Başvuru numarası | Proje çıktılarıyla ilişkisi | Proje çıktısının özgün yönleri |",
                  "|---|---|---|---|"]
            s += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in icerik.TEKNIK_DURUM]
            s += ["", "Patentler Google Patents'te doğrulandı (EP3092043B2: Tonies GmbH, başvuru 9.1.2015; "
                  "US10960320B2: Boxine GmbH; EP4282503A1: Tonies GmbH, başvuru 25.5.2022). Cihaz içinde üretilen hikâyeye yönelik bir patente rastlanmadı; "
                  "patent vekiliyle profesyonel tarama İP5'te planlıdır.", ""]
            continue
        if k == "KRITIK":
            s += ["### 4.3 Kritik İş Adımları", "", "| İş tanımı | Öngörülen gerçekleşme tarihi | "
                  "Doğrulanabilir başarım ölçütleri |", "|---|---|---|"]
            s += [f"| {a} | {b} | {c} |" for a, b, c in icerik.KRITIK_ADIMLAR]
            s += [""]
            continue
        if k == "BASABAS":
            s += ["### 4.4 Başa Baş Noktası Analizi (proje süresi 18 ay + 5 yıl; sabit 2026 fiyatları, KDV hariç)", "",
                  "| Tablo 4.4-1 Gelirler | |", "|---|---:|",
                  f"| Satılan ürün adedi | {tl(bb['adet'])} |", f"| Birim satış fiyatı | {tl(bb['fiyat'])} TL |",
                  f"| Satış gelirleri | {tl(bb['satis'])} TL |",
                  f"| Diğer gelirler (ek figür paketleri: {tl(bb['ek_paket'])} paket × 374 TL) | {tl(bb['diger_gelir'])} TL |",
                  f"| **Toplam gelirler** | **{tl(bb['toplam_gelir'])} TL** |", "",
                  "| Tablo 4.4-2 Değişken maliyetler (birim) | |", "|---|---:|",
                  f"| Personel (montaj, test, flaş yazma) | {tl(bb['personel'])} TL |",
                  f"| Malzeme (ağırlıklı ortalama; 1.000 adette 1.050 → 10.000+ adette ≈675 TL) | {tl(bb['malzeme'])} TL |",
                  f"| Enerji | {tl(bb['enerji'])} TL |",
                  f"| Dağıtım (kanal karışımı: komisyon/indirim + kargo + ödeme) | {tl(bb['dagitim'])} TL |",
                  f"| Diğer değişken (garanti/iade karşılığı ≈%3) | {tl(bb['diger_degisken'])} TL |",
                  f"| **Birim ürün maliyeti** | **{tl(bb['birim'])} TL** |", "",
                  "| Tablo 4.4-3 Sabit maliyetler (toplam) | |", "|---|---:|",
                  f"| Makine ve teçhizat (kalıplar, test düzenekleri, laboratuvar ekipmanı) | {tl(bb['makine'])} TL |",
                  "| Bina amortismanı | 0 TL |",
                  f"| Kira (kuluçka/teknopark ofisi ve atölye) | {tl(bb['kira'])} TL |",
                  f"| Diğer sabit maliyetler (personel, pazarlama, belgelendirme, genel yönetim, Ar-Ge; ek paketlerin değişken maliyeti dahil) | {tl(bb['diger_sabit'])} TL |",
                  f"| **Toplam sabit maliyet** | **{tl(bb['toplam_sabit'])} TL** |", "",
                  "| Tablo 4.4-4 Başa baş analizi | |", "|---|---:|",
                  f"| Kâr marjı (birim satış fiyatı − birim ürün maliyeti) | {tl(bb['marj'])} TL |",
                  f"| Satılan ürün adedi olarak başa baş noktası | {tl(bb['basabas'])} set |", ""]
            dk = bb["diger_sabit_kalemler"]
            s += ["**Varsayımlar:** "
                  f"Satış adetleri yıllara göre {', '.join(tl(a) for a in finans.ADET)} (Y0 = 18 aylık proje dönemi). "
                  "Birim fiyat 2.999 TL (KDV dahil) başlangıç setinin KDV hariç karşılığıdır; ön satıştaki erken alım "
                  "indirimi pazarlama giderine dahildir. Kur 1 USD = 50 TL. Diğer sabit maliyetlerin dağılımı: "
                  f"personel {tl(dk['personel'])} TL, pazarlama {tl(dk['pazarlama'])} TL, belgelendirme "
                  f"{tl(dk['belgelendirme'])} TL, genel yönetim {tl(dk['genel_yonetim'])} TL, Ar-Ge ve proje "
                  f"hizmetleri {tl(dk['arge_ve_proje_hizmetleri'])} TL, ek paketlerin değişken maliyeti "
                  f"{tl(dk['ek_paket_degisken'])} TL. Başa baş adedi, 6,5 yılın bütün sabit giderlerini tek "
                  "kalemde topladığı için kümülatif satışın sonuna yakın çıkar; yıllık bazda FAVÖK ticarileşmenin "
                  "2. yılında pozitife döner, kümülatif FAVÖK 3. yılda artıya geçer (bkz. Eko_Finansal_Model.xlsx).", ""]
            s += ["| Yıl | Adet | Ciro (M TL) | Değişken (M TL) | Sabit (M TL) | FAVÖK (M TL) | Dönem sonu kasa (M TL) |",
                  "|---|---:|---:|---:|---:|---:|---:|"]
            for r in oz["yillar"]:
                s.append(f"| {r['yil']} | {tl(r['adet'])} | {tl(r['ciro']/1e6, 2)} | {tl(r['degisken']/1e6, 2)} | "
                         f"{tl(r['sabit']/1e6, 2)} | {tl(r['favok']/1e6, 2)} | {tl(r['kasa_sonu']/1e6, 2)} |")
            s += ["", "Kasa, finansmanı içerir: Y0'da BİGG Fonu 1,35 M TL + devam yatırımı 1,35 M TL; Y1 başında "
                  "tohum turu (BiGG+ ve eş yatırım) ≈12 M TL [V]. İşletme sermayesi cironun %15'i.", ""]
            continue
        if k == "RISK":
            s += ["### 5.1 Projenin Yürütülmesi Sırasında Karşılaşılabilecek Riskler ve Alınacak Önlemler", "",
                  "| Risk tanımı | Önlemler | Olasılık | Etki | B planı |", "|---|---|---|---|---|"]
            s += [f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in icerik.RISKLER]
            s += ["", "**Ayrıntı (formun hücreleri kısa olduğu için):**", "", icerik.RISK_AYRINTI, ""]
            continue
        metin = icerik.ALANLAR[k]
        s += [f"### {BASLIKLAR[k]}", "", f"*({len(metin)} / 3000 karakter)*", "", metin.replace("\n", "\n\n").replace("\n\n\n\n", "\n\n"), ""]
    yol = os.path.join(KOK, "02_IS_PLANI_AGY112.md")
    open(yol, "w", encoding="utf-8").write("\n".join(s))
    print("MD:", yol)
    return yol


def word_pdf(md_yol, ad):
    docx = os.path.join(CIKTI, ad + ".docx")
    subprocess.run(["pandoc", md_yol, "-o", docx], check=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", CIKTI, docx], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("DOCX/PDF:", docx)


def maliyet_formu():
    import docx
    kaynak = os.path.join(CIKTI, "_maliyet_kaynak.docx")
    if not os.path.exists(kaynak):
        subprocess.run(["soffice", "--headless", "--convert-to", "docx", "--outdir", CIKTI,
                        os.path.join(RESMI, "1812_Tahmini_Maliyet_Formlari.doc")], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.move(os.path.join(CIKTI, "1812_Tahmini_Maliyet_Formlari.docx"), kaynak)
    d = docx.Document(kaynak)
    B = finans.BUTCE
    bt = finans.butce_toplam()
    T = d.tables

    def yaz(tablo, satir, sutunlar, degerler):
        hucreler = tablo.rows[satir].cells
        for c, v in zip(sutunlar, degerler):
            hucreler[c].text = str(v)

    def bos_satir_ekle(tablo, gereken, ilk):
        while len(tablo.rows) - ilk < gereken:
            yeni = __import__("copy").deepcopy(tablo.rows[ilk]._tr)
            tablo.rows[ilk]._tr.addnext(yeni)

    # M011 personel: satır 0 iş fikri adı, 1 iş paketi, 2 başlık, 3.. veri
    t = T[0]
    t.rows[0].cells[2].text = icerik.IS_FIKRI_ADI
    t.rows[1].cells[2].text = "İP1–İP5 (tüm iş paketleri)"
    for i, (ad, gorev, unvan, oran, ay, aylik) in enumerate(B["personel"]):
        yaz(t, 3 + i, [0, 3, 6, 7, 8, 9, 10], [ad, gorev, unvan, f"{oran:.1f}", ay, tl(aylik), tl(oran * ay * aylik)])
    t.rows[-1].cells[-1].text = tl(bt["personel"])
    # M012 seyahat
    t = T[1]
    t.rows[0].cells[1].text = "İP5 Ticarileşme / İP3 Donanım"
    for i, r in enumerate(B["seyahat"]):
        yaz(t, 2 + i, range(6), [r[0], r[1], r[2], r[3], r[4], tl(r[5])])
    t.rows[-1].cells[-1].text = tl(bt["seyahat"])
    # M013 alet/teçhizat
    t = T[2]
    t.rows[0].cells[3].text = "İP2 Kart yazılımı ve doğrulama / İP3 Donanım"
    for i, (ad, adet, kap, tek, amac, kul, usd, tlb) in enumerate(B["alet"]):
        yaz(t, 3 + i, [1, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [ad, adet, kap, tek, amac, "X" if kul == "Ar-Ge" else "", "" if kul == "Ar-Ge" else "X", tl(usd),
             tl(tlb), tl(adet * tlb)])
    t.rows[-1].cells[-1].text = tl(bt["alet"])
    # M015 hizmet
    t = T[3]
    t.rows[0].cells[1].text = "İP1, İP3, İP4, İP5"
    bos_satir_ekle(t, len(B["hizmet"]) + 1, 2)
    for i, (kim, acik, iliski, tutar) in enumerate(B["hizmet"]):
        yaz(t, 2 + i, [0, 2, 3, 4], [kim, acik, iliski, tl(tutar)])
    t.rows[-1].cells[-1].text = tl(bt["hizmet"])
    # M016 malzeme
    t = T[4]
    t.rows[0].cells[2].text = "İP1 Pilot / İP2 Doğrulama / İP3 Donanım"
    for i, (ad, kul, mik, ger, usd, tlb, top) in enumerate(B["malzeme"]):
        yaz(t, 2 + i, range(8), [i + 1, ad, kul, mik, ger, tl(usd), tl(tlb), tl(top)])
    t.rows[-1].cells[-1].text = tl(bt["malzeme"])
    # M030 dönemsel
    t = T[5]
    t.rows[0].cells[0].text = "İş Fikri Adı: " + icerik.IS_FIKRI_ADI
    for c, v in zip([1, 2, 3, 4], ["2028", "2028", "2029", "2029"]):
        t.rows[1].cells[c].text = v
    etiketler = [t.rows[i].cells[0].text.strip() for i in range(len(t.rows))]
    satir_no = {"personel": "Personel", "seyahat": "Seyahat", "alet": "Alet/Teçhizat",
                "hizmet": "Danışmanlık/Hizmet", "malzeme": "Malzeme"}
    for k, et in satir_no.items():
        i = next(j for j, e in enumerate(etiketler) if e.startswith(et))
        dn = bt["donem"][k]
        yaz(t, i, [1, 2, 3, 4, 5, 6], [tl(dn[0]), tl(dn[1]), tl(dn[2]), "–", tl(bt[k]),
                                       f"%{100 * bt[k] / bt['toplam']:.1f}".replace(".", ",")])
    top = [sum(bt["donem"][k][j] for k in bt["donem"]) for j in range(3)]
    i = next(j for j, e in enumerate(etiketler) if e.startswith("TOPLAM MAL"))
    yaz(t, i, [1, 2, 3, 4, 5, 6], [tl(top[0]), tl(top[1]), tl(top[2]), "–", tl(bt["toplam"]), "%100"])
    i = next(j for j, e in enumerate(etiketler) if e.startswith("BİRİKİMLİ"))
    yaz(t, i, [1, 2, 3, 4, 5], [tl(top[0]), tl(top[0] + top[1]), tl(sum(top)), "–", tl(bt["toplam"])])
    t.rows[1].cells[0].text = "Maliyet Kalemi (dönemler: 2028-I Oca–Haz, 2028-II Tem–Ara, 2029-I Oca–Haz)"
    yol = os.path.join(CIKTI, "Tahmini_Maliyet_Formlari_Eko.docx")
    d.save(yol)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", CIKTI, yol], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Maliyet formu:", yol, [t.rows[i].cells[0].text for i in range(3, len(t.rows))])


def excel(oz):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    wb = Workbook()
    kalin = Font(bold=True)
    dolgu = PatternFill("solid", fgColor="DDEBF7")

    def sayfa(ad, basliklar, satirlar, genislik=None):
        ws = wb.create_sheet(ad)
        ws.append(basliklar)
        for c in ws[1]:
            c.font = kalin
            c.fill = dolgu
            c.alignment = Alignment(wrap_text=True, vertical="top")
        for r in satirlar:
            ws.append(r)
        for i, g in enumerate(genislik or [], 1):
            ws.column_dimensions[chr(64 + i)].width = g
        return ws

    wb.remove(wb.active)
    v = oz["varsayim"]
    sayfa("Varsayımlar", ["Varsayım", "Değer", "Not"], [
        ["Kur (TL/USD)", v["kur"], "Kasım 2026 varsayımı"],
        ["Başlangıç seti fiyatı (KDV hariç)", v["fiyat"], "2.999 TL KDV dahil"],
        ["Ek figür paketi fiyatı (KDV hariç)", v["ek_paket_fiyat"], "449 TL KDV dahil, 3 figür"],
        ["Ek paket / cihaz", v["ek_paket_orani"], "ortalama"],
        ["TÜBİTAK BİGG Fonu yatırımı", v["bigg"], "%3 pay (2026-2 çağrısı)"],
        ["Devam yatırımı (şartlı)", v["bigg_devam"], "ilk dönem raporundan sonra; fon payı toplam ≤ %5"],
        ["Tohum turu (Y1)", v["tohum"], "BiGG+ ≤ 8 M TL (≤ %10) + eş yatırımcı"],
        ["İşletme sermayesi / ciro", v["isletme_sermayesi"], "stok + alacak"],
        ["Ortalama kişi maliyeti (Y1+, aylık)", v["kisi_aylik"], "işveren maliyeti, sabit 2026 TL"],
        ["Kanal karışımı", "40/40/20", "pazaryeri / kendi web / kurum-perakende"],
    ] + [[k, round(x), "dağıtım maliyetine katkı (TL/cihaz)"] for k, x in oz["kanal"].items()], [42, 16, 50])
    sutun = ["Kalem"] + [r["yil"] for r in oz["yillar"]] + ["Toplam"]
    alan = [("Satılan set", "adet"), ("Ek figür paketi", "ek_paket"), ("Ekip (kişi)", "ekip"),
            ("Ciro (TL)", "ciro"), ("  cihaz", "gelir_cihaz"), ("  ek paket", "gelir_paket"),
            ("Birim değişken maliyet (TL/set)", "birim_degisken"), ("Değişken maliyet (TL)", "degisken"),
            ("Brüt katkı (TL)", "brut_katki"), ("Personel (TL)", "personel"),
            ("Makine/teçhizat/kalıp (TL)", "makine"), ("Kira (TL)", "kira"), ("Pazarlama (TL)", "pazarlama"),
            ("Belgelendirme (TL)", "belgelendirme"), ("Genel yönetim (TL)", "genel_yonetim"),
            ("Ar-Ge ve proje hizmetleri (TL)", "arge"), ("Sabit gider toplamı (TL)", "sabit"),
            ("FAVÖK (TL)", "favok"), ("İşletme sermayesi (TL)", "isletme_sermayesi"),
            ("Finansman girişi (TL)", "finansman"), ("Dönem sonu kasa (TL)", "kasa_sonu")]
    toplanmaz = {"birim_degisken", "ekip", "isletme_sermayesi", "kasa_sonu"}
    satirlar = []
    for et, k in alan:
        vals = [round(r[k]) for r in oz["yillar"]]
        satirlar.append([et] + vals + ([""] if k in toplanmaz else [sum(vals)]))
    ws = sayfa("Projeksiyon", sutun, satirlar, [34, 16, 16, 16, 16, 16, 16, 18])
    for row in ws.iter_rows(min_row=2):
        for c in row[1:]:
            c.number_format = "#,##0"
    bb = oz["basa_bas"]
    sayfa("Başa baş (AGY 4.4)", ["Kalem", "Değer (TL / adet)"], [
        ["Satılan ürün adedi", bb["adet"]], ["Birim satış fiyatı", bb["fiyat"]], ["Satış gelirleri", bb["satis"]],
        ["Diğer gelirler (ek paketler)", bb["diger_gelir"]], ["Toplam gelirler", bb["toplam_gelir"]],
        ["Personel (birim)", bb["personel"]], ["Malzeme (birim, ağırlıklı)", bb["malzeme"]],
        ["Enerji (birim)", bb["enerji"]], ["Dağıtım (birim)", bb["dagitim"]], ["Diğer değişken (birim)", bb["diger_degisken"]],
        ["Birim ürün maliyeti", bb["birim"]], ["Makine ve teçhizat", bb["makine"]], ["Bina amortismanı", 0],
        ["Kira", bb["kira"]], ["Diğer sabit", bb["diger_sabit"]], ["Toplam sabit maliyet", bb["toplam_sabit"]],
        ["Kâr marjı (birim)", bb["marj"]], ["Başa baş noktası (adet)", bb["basabas"]],
    ], [40, 20])
    be = oz["birim_ekonomisi"]
    sayfa("Birim ekonomisi", ["Gösterge", "Değer", "Not"], [
        ["Cihaz katkı payı (TL)", be["katki_cihaz"], "2.499 − birim değişken maliyet (Y3)"],
        ["Ek paket katkı payı (TL)", be["katki_paket"], "374 − 70 malzeme − 90 dağıtım"],
        ["Müşteri yaşam boyu değeri, LTV (TL)", be["ltv"], be["not_"]],
        ["Hedef müşteri edinme maliyeti, CAC (TL)", be["cac"], "karma: organik + performans pazarlaması"],
        ["LTV / CAC", be["ltv_cac"], "≥ 3 hedeflenir; pilot ve ön satışla ölçülecek"],
    ], [38, 14, 50])
    bt = oz["butce"]
    rows = []
    for k, ad in [("personel", "Personel (M011)"), ("seyahat", "Seyahat (M012)"),
                  ("alet", "Alet/Teçhizat/Yazılım (M013)"), ("hizmet", "Hizmet alımı (M015)"),
                  ("malzeme", "Malzeme (M016)")]:
        rows.append([ad] + bt["donem"][k] + [bt[k], round(100 * bt[k] / bt["toplam"], 1)])
    rows.append(["TOPLAM"] + [sum(bt["donem"][k][j] for k in bt["donem"]) for j in range(3)] + [bt["toplam"], 100])
    sayfa("Proje bütçesi (1812)", ["Maliyet kalemi"] + finans.DONEMLER + ["Toplam (TL)", "Pay (%)"], rows,
          [32, 14, 14, 14, 16, 10])
    yol = os.path.join(CIKTI, "Eko_Finansal_Model.xlsx")
    wb.save(yol)
    print("Excel:", yol)


def main():
    os.makedirs(CIKTI, exist_ok=True)
    finans.main()
    oz = json.load(open(os.path.join(CIKTI, "finans_ozet.json"), encoding="utf-8"))
    print("Karakter denetimi:")
    denetle()
    pdf_doldur(oz["basa_bas"])
    md = markdown(oz["basa_bas"], oz)
    word_pdf(md, "AGY112_Is_Plani_Eko")
    maliyet_formu()
    excel(oz)


if __name__ == "__main__":
    main()
