"""Eko finans modeli: proje bütçesi (1812 Aşama 2), 6,5 yıllık projeksiyon, başa baş, birim ekonomisi.

Bütün tutarlar sabit 2026 fiyatlarıyla, KDV hariç TL. "V" = varsayım. Kur: 1 USD = 50 TL (V).
Yıl düzeni: Y0 = Aşama 2 proje dönemi (18 ay, Ocak 2028 – Haziran 2029), Y1..Y5 = ticarileşmenin 1.–5. yılı
(Temmuz–Haziran). AGY 112 tablo 4.4 "proje süresi + 5 yıl" toplamını ister: Y0..Y5.

Çalıştır: python finans.py  ->  ../cikti/finans_ozet.json (+ doldur.py Excel'i yazar)
"""
import json
import os

BURASI = os.path.dirname(os.path.abspath(__file__))
CIKTI = os.path.join(os.path.dirname(BURASI), "cikti")

KUR = 50.0
YILLAR = ["Y0 (Oca 2028–Haz 2029, proje)", "Y1 (Tem 2029–Haz 2030)", "Y2 (2030–31)", "Y3 (2031–32)",
          "Y4 (2032–33)", "Y5 (2033–34)"]
KISA = ["Y0", "Y1", "Y2", "Y3", "Y4", "Y5"]

# --- Satış varsayımları (V) ---
ADET = [1000, 4000, 9000, 16000, 24000, 32000]          # başlangıç seti (kurum setleri dahil, cihaz adedi)
FIYAT = 2499                                             # KDV hariç liste (2.999 TL KDV dahil)
EK_PAKET_ORANI = 0.8                                     # satılan cihaz başına ek figür paketi
EK_PAKET_FIYAT = 374                                     # KDV hariç (449 TL KDV dahil)
EK_PAKET_MALZEME = 70
EK_PAKET_DAGITIM = 90

# --- Birim değişken maliyet (TL/cihaz) ---
MALZEME = [1050, 860, 770, 720, 690, 675]                # ölçekle düşen BOM + kasa + figür + ambalaj
PERSONEL_BIRIM = 60                                      # montaj, test, flaş yazma
ENERJI_BIRIM = 5
DAGITIM_BIRIM = 507                                      # kanal karışımı: %40 pazaryeri, %40 web, %20 kurum/perakende
DIGER_BIRIM = 75                                         # garanti/iade karşılığı ≈%3

# Kanal maliyeti ayrıntısı (dağıtım = komisyon/indirim + kargo + ödeme ücreti), TL/cihaz
KANAL = {
    "Pazaryeri (%40): komisyon %18 × 2.999 + kargo 90": 0.4 * (0.18 * 2999 + 90),
    "Kendi web (%40): ödeme ücreti %3 × 2.999 + kargo 90": 0.4 * (0.03 * 2999 + 90),
    "Kurum/perakende (%20): %35 indirim × 2.499 + lojistik 40": 0.2 * (0.35 * 2499 + 40),
}

# --- Sabit giderler (TL/yıl) ---
PROJE_PERSONEL = 18 * 40500                              # Y0: proje yürütücüsü, 18 adam-ay (asgari ücret işveren maliyeti)
EKIP = [1, 4, 7, 10, 13, 16]                             # Y1+ çalışan sayısı (kurucular dahil)
KISI_AYLIK = 65000                                       # ortalama işveren maliyeti (Y1+)
PERSONEL = [PROJE_PERSONEL] + [EKIP[i] * 12 * KISI_AYLIK for i in range(1, 6)]
HIZMET_Y0 = 393000                                       # proje bütçesindeki hizmet alımları
SEYAHAT_Y0 = 20000
ALET_Y0 = 58000
MALZEME_PROTOTIP_Y0 = 150000
MAKINE = [700000 + 200000 + ALET_Y0, 0, 400000, 0, 500000, 0]   # kalıplar, test düzenekleri, lab ekipmanı
KIRA = [18 * 6000, 12 * 20000, 12 * 30000, 12 * 40000, 12 * 50000, 12 * 60000]
PAZARLAMA = [250000, 1600000, 3200000, 5200000, 7200000, 9000000]
BELGELENDIRME = [450000, 0, 300000, 400000, 200000, 200000]     # Y0: tam CE/RED (ön tarama proje bütçesinde)
GENEL_YONETIM = [0, 300000, 450000, 600000, 750000, 900000]
ARGE_EK = [MALZEME_PROTOTIP_Y0 + HIZMET_Y0 + SEYAHAT_Y0, 300000, 600000, 800000, 800000, 800000]

# --- Finansman (V) ---
BIGG = 1350000                                           # TÜBİTAK BİGG Fonu, %3 pay (2026-2 çağrısı tutarı)
BIGG_DEVAM = 1350000                                     # ilk dönem raporu sonrası devam yatırımı (tetikleyici şartlı)
TOHUM = 12000000                                         # Y1 başı: BiGG+ (≤8 M TL, ≤%10) + eş yatırımcı ≈4 M TL
ISLETME_SERMAYESI_ORANI = 0.15                           # stok + alacak, ciro payı


def hesapla():
    y = []
    kasa = 0.0
    onceki_ns = 0.0
    for i in range(6):
        adet = ADET[i]
        paket = round(adet * EK_PAKET_ORANI)
        gelir_cihaz = adet * FIYAT
        gelir_paket = paket * EK_PAKET_FIYAT
        birim = MALZEME[i] + PERSONEL_BIRIM + ENERJI_BIRIM + DAGITIM_BIRIM + DIGER_BIRIM
        degisken = adet * birim + paket * (EK_PAKET_MALZEME + EK_PAKET_DAGITIM)
        sabit = (PERSONEL[i] + MAKINE[i] + KIRA[i] + PAZARLAMA[i] + BELGELENDIRME[i] + GENEL_YONETIM[i]
                 + ARGE_EK[i])
        ciro = gelir_cihaz + gelir_paket
        favok = ciro - degisken - sabit
        ns = ISLETME_SERMAYESI_ORANI * ciro
        finansman = (BIGG + BIGG_DEVAM if i == 0 else 0) + (TOHUM if i == 1 else 0)
        kasa += favok - (ns - onceki_ns) + finansman
        onceki_ns = ns
        y.append(dict(yil=YILLAR[i], kisa=KISA[i], adet=adet, ek_paket=paket, ciro=ciro, gelir_cihaz=gelir_cihaz,
                      gelir_paket=gelir_paket, birim_degisken=birim, degisken=degisken,
                      brut_katki=ciro - degisken, personel=PERSONEL[i], makine=MAKINE[i], kira=KIRA[i],
                      pazarlama=PAZARLAMA[i], belgelendirme=BELGELENDIRME[i], genel_yonetim=GENEL_YONETIM[i],
                      arge=ARGE_EK[i], sabit=sabit, favok=favok, isletme_sermayesi=ns, finansman=finansman,
                      kasa_sonu=kasa, ekip=EKIP[i]))
    return y


def basa_bas(y):
    """AGY 112 tablo 4.4: proje süresi + 5 yıl toplamları."""
    toplam_adet = sum(r["adet"] for r in y)
    malzeme_ort = sum(r["adet"] * MALZEME[i] for i, r in enumerate(y)) / toplam_adet
    paket = sum(r["ek_paket"] for r in y)
    satis = toplam_adet * FIYAT
    diger_gelir = paket * EK_PAKET_FIYAT
    birim = malzeme_ort + PERSONEL_BIRIM + ENERJI_BIRIM + DAGITIM_BIRIM + DIGER_BIRIM
    makine = sum(MAKINE)
    kira = sum(KIRA)
    paket_degisken = paket * (EK_PAKET_MALZEME + EK_PAKET_DAGITIM)
    diger_sabit = sum(PERSONEL) + sum(PAZARLAMA) + sum(BELGELENDIRME) + sum(GENEL_YONETIM) + sum(ARGE_EK) \
        + paket_degisken
    toplam_sabit = makine + kira + diger_sabit
    marj = FIYAT - birim
    return dict(adet=toplam_adet, fiyat=FIYAT, satis=satis, diger_gelir=diger_gelir, toplam_gelir=satis + diger_gelir,
                personel=PERSONEL_BIRIM, malzeme=round(malzeme_ort), enerji=ENERJI_BIRIM, dagitim=DAGITIM_BIRIM,
                diger_degisken=DIGER_BIRIM, birim=round(birim), makine=makine, amortisman=0, kira=kira,
                diger_sabit=round(diger_sabit), toplam_sabit=round(toplam_sabit), marj=round(marj),
                basabas=round(toplam_sabit / marj), paket_degisken=paket_degisken, ek_paket=paket,
                diger_sabit_kalemler=dict(personel=sum(PERSONEL), pazarlama=sum(PAZARLAMA),
                                          belgelendirme=sum(BELGELENDIRME), genel_yonetim=sum(GENEL_YONETIM),
                                          arge_ve_proje_hizmetleri=sum(ARGE_EK), ek_paket_degisken=paket_degisken))


def birim_ekonomisi():
    katkı_cihaz = FIYAT - (MALZEME[3] + PERSONEL_BIRIM + ENERJI_BIRIM + DAGITIM_BIRIM + DIGER_BIRIM)
    katkı_paket = EK_PAKET_FIYAT - EK_PAKET_MALZEME - EK_PAKET_DAGITIM
    ltv = katkı_cihaz + EK_PAKET_ORANI * katkı_paket
    cac = 450
    return dict(katki_cihaz=katkı_cihaz, katki_paket=katkı_paket, ltv=round(ltv), cac=cac,
                ltv_cac=round(ltv / cac, 1), not_="Y3 malzeme maliyetiyle; LTV = cihaz katkısı + 0,8 ek paket katkısı")


# --- 1812 Aşama 2 proje bütçesi (1.350.000 TL), Tahmini Maliyet Formları ile aynı ---
DONEMLER = ["2028-I", "2028-II", "2029-I"]
BUTCE = {
    "personel": [
        # (ad, görev, ünvan, adam/ay oranı, ay, aylık maliyet)
        ("[AD SOYAD]", "Proje yürütücüsü; İP1, İP2, İP5", "Genel Müdür / Kurucu", 1.0, 18, 40500),
    ],
    "seyahat": [
        ("[AD SOYAD]", "Genel Müdür", "Oyuncak ve çocuk ürünleri fuarı (İstanbul), EMS/kalıp üreticisi ziyaretleri",
         "Tedarikçi seçimi, kanal ve kurum görüşmeleri", "İstanbul, Bursa, Kocaeli", 20000),
    ],
    "alet": [
        # (ad, adet, kapasite, teknik özellik, kullanım amacı, ar-ge/üretim, usd, tl)
        ("Dijital osiloskop + mantık analizörü", 1, "4 kanal, 100 MHz", "1 GS/s; 16 kanal LA",
         "I2S ses, NFC ve güç hattı ölçümü", "Ar-Ge", 500, 25000),
        ("FDM 3B yazıcı", 1, "≥ 250 mm", "çok renkli, PLA/PETG",
         "Kasa ve figür prototipleri", "Ar-Ge", 500, 25000),
        ("Ayarlı güç kaynağı + akım ölçer", 1, "0–30 V, 5 A", "mA çözünürlüklü akım ölçümü",
         "Pil ömrü ve tüketim ölçümü", "Ar-Ge", 160, 8000),
    ],
    "hizmet": [
        ("Akredite test laboratuvarı", "EN IEC 62115 ve RED (EN 300 330/301 489) ön uygunluk taraması",
         "İP4: belgelendirme riskinin erken azaltılması", 90000),
        ("PCB tasarım ve DFM danışmanlığı", "EVT/DVT devre kartı tasarım incelemesi, üretilebilirlik",
         "İP3: kendi devre kartımız", 90000),
        ("Endüstriyel tasarımcı", "Stand kasası ve 6 özgün figürün üretime uygun tasarımı",
         "İP3: kasa ve figür", 60000),
        ("Patent ve marka vekili", "Marka (4 sınıf), tasarım tescili, faydalı model araştırma ve başvurusu",
         "İP5: fikri mülkiyet", 55000),
        ("Çocuk gelişimi uzmanı + etik kurul", "İçerik kuralları danışmanlığı, pilot tasarımı, etik kurul",
         "İP1/İP5: pilot ve içerik güvenliği", 35000),
        ("Mali müşavir ve şirket kuruluşu", "18 ay muhasebe (2.000 TL/ay) + noter/tescil/KEP",
         "Şirket yönetimi", 63000),
    ],
    "malzeme": [
        # (ad, kullanım, miktar, gerekçe, usd, tl birim, toplam)
        ("EVT devre kartı (PCB + montaj + bileşen)", "İP3: ilk kendi kartımız", "30 adet",
         "Tasarım doğrulama, 10 kart pil/hız testi", 30, 1500, 45000),
        ("DVT seti (kart + kasa + 4 figür + NFC)", "İP3/İP1: pilot cihazları", "60 adet",
         "30–50 aile + 3–5 okul pilotu", 24, 1200, 72000),
        ("Pilot figür ve NFC etiketleri", "Pilot ailelere ek figürler", "60 set",
         "Her aileye 13 figürden 6'sı", 6, 300, 18000),
        ("Geliştirme kartları ve bileşenler", "İP2: test ve yedek", "1 lot",
         "ESP32-S3 DevKit, mikrofon, hoparlör, halka", 300, 15000, 15000),
    ],
}
# dönemsel dağılım oranları (2028-I, 2028-II, 2029-I)
DAGILIM = {
    "personel": [1 / 3, 1 / 3, 1 / 3],
    "seyahat": [0.25, 0.5, 0.25],
    "alet": [1.0, 0.0, 0.0],
    "hizmet": [0.35, 0.45, 0.20],
    "malzeme": [0.40, 0.55, 0.05],
}


def butce_toplam():
    t = {}
    t["personel"] = sum(r[3] * r[4] * r[5] for r in BUTCE["personel"])
    t["seyahat"] = sum(r[5] for r in BUTCE["seyahat"])
    t["alet"] = sum(r[1] * r[7] for r in BUTCE["alet"])
    t["hizmet"] = sum(r[3] for r in BUTCE["hizmet"])
    t["malzeme"] = sum(r[6] for r in BUTCE["malzeme"])
    t["toplam"] = sum(t.values())
    t["donem"] = {k: [round(t[k] * p) for p in DAGILIM[k]] for k in DAGILIM}
    return t


def main():
    os.makedirs(CIKTI, exist_ok=True)
    y = hesapla()
    bb = basa_bas(y)
    be = birim_ekonomisi()
    bt = butce_toplam()
    assert bt["toplam"] == 1350000, bt["toplam"]
    ozet = dict(yillar=y, basa_bas=bb, birim_ekonomisi=be, butce=bt, kanal=KANAL,
                varsayim=dict(kur=KUR, fiyat=FIYAT, ek_paket_orani=EK_PAKET_ORANI, ek_paket_fiyat=EK_PAKET_FIYAT,
                              bigg=BIGG, bigg_devam=BIGG_DEVAM, tohum=TOHUM, isletme_sermayesi=ISLETME_SERMAYESI_ORANI,
                              kisi_aylik=KISI_AYLIK))
    json.dump(ozet, open(os.path.join(CIKTI, "finans_ozet.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    for r in y:
        print(f"{r['kisa']}: adet {r['adet']:>6} ciro {r['ciro']/1e6:6.2f} M  değişken {r['degisken']/1e6:6.2f} M  "
              f"sabit {r['sabit']/1e6:6.2f} M  FAVÖK {r['favok']/1e6:6.2f} M  kasa {r['kasa_sonu']/1e6:6.2f} M")
    print("başa baş:", {k: v for k, v in bb.items() if k != 'diger_sabit_kalemler'})
    print("birim ekonomisi:", be)
    print("kanal:", {k: round(v) for k, v in KANAL.items()}, round(sum(KANAL.values())))
    print("bütçe:", {k: v for k, v in bt.items() if k != 'donem'}, bt["donem"])


if __name__ == "__main__":
    main()
