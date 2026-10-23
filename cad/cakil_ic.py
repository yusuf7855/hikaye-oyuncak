"""Çakıl stand: dış kabuk (seçenek 3: çukurda figür yuvası, zemin kabuğun kendisi) ve iç yerleşim, iki NFC seçeneği.

    python cad/cakil_ic.py            # RC522 ve PN5180: çarpışma denetimi, önizleme PNG, STL (cad/stl_cakil/<nfc>/)

Ölçüler TAHMİN (ürün sahibi, 16 Ekim 2026: "tahminle başlayalım"); parça ölçüleri PARCA sözlüğünde, gerçekleri
ölçülünce yalnız orası değişir. Koordinat: z yukarı (z=0 taban), +y ÖN (logo), -y ARKA (anahtar solda).

Güç (ürün sahibi, 21 Ekim 2026): USB-C, 18650 ve TP4056 kalktı; 4'lü AA pil yatağı tabandaki PİL KUTUSUNDA, alttan
vidalı kapakla açılır. Piller -> anahtar (KCD11) -> 5 V düzenleyici -> ESP32, ses kartı, halka.

Yerleşim (alttan üste):
  taban plakası (vidalı, 4 ayak) + alttan açılan pil kapağı | pil kutusu (ortada; 4xAA yatağı ters durur, sırtı
  kutunun tavanına bantlı) | hoparlör Ø50 önde dik (ses ön ızgaradan) | kutunun tavanında: MAX98357A (sağ),
  5 V düzenleyici (sol) | açma-kapama (sol yan duvar) | ESP32-S3 (arkada, kutunun üstünde, TERS: pinler yukarı, J1 öne,
  jumper'lar üstten takılır) | NFC okuyucu (anten figürün tam altında) | LED halka (Ø55/Ø70) | figür zemini (kabuk) |
  mikrofon (üstte, arkada delik).
"""
import math
import os
import sys

import numpy as np
import trimesh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import manifold3d as m3  # noqa: E402
from geometri import M, CS, kutu, silindir, dondur, xz_den_y_ye, xy_prizma, aynala_x, yazi_duz, yuvarlak_dikdortgen, trimesh_e, vida_cubugu, cokgen  # noqa: E402

KOK = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(KOK, "font", "Fredoka.ttf")
SEG = 160

# ---------------------------------------------------------------- dış form (çakıl, süperelips)
R, H = 60.0, 56.0
ZC, B, N = 21.0, 45.0, 2.8
DUVAR = 2.4
TABAN_KAL = 2.4
# figür yuvası (seçenek 3)
# Ürün sahibi (16 Ekim 2026, seçenek A): 16'lı halka çukurun DIŞINDA, üst yüzün altındaki tavanda; bunun için çukur
# halkanın iç boşluğuna (Ø31,75) girer -> figür tabanı Ø28 (NTAG213 Ø25 sığar). Işık figür üstündeyken de görünür.
# Ürün sahibi (20 Ekim 2026, ilk baskıdan sonra): LED halkası iç Ø55 / dış Ø70; çukurun dış duvarı halkanın iç çapına
# SIKI geçer (Ø54,9), çukurun içi Ø52,5, figür tabanı Ø52 (NTAG213 Ø25 rahat sığar).
FIGUR_TABAN_D = 52.0
YUVA_R = FIGUR_TABAN_D / 2 + 0.25
CUKUR_DERIN = 5.0        # figür tabanının oturduğu yüz = H - 5
# Ürün sahibi (16 Ekim 2026): ayrı yarı saydam parça yok, her şey PLA/PETG. Figürün oturduğu zemin kabuğun parçası;
# zeminin altında, LED'lerin tam üstünde halka biçimli oyuk: zemin orada ISIK_KAL kalır, beyaz PLA'dan ışık geçer.
YUVA_DUVAR = 1.2         # çukurun kabuk içine sarkan duvarı: dış Ø54,9 -> halkanın iç Ø55'ine sıkı geçer, halkayı ortalar
ZEMIN_KAL = 1.6          # figür zemini kalınlığı (altında NFC okuyucu)
ISIK_KAL = 0.6           # LED'lerin üstünde kalan zemin (0,6 mm beyaz PLA ışığı geçirir; renkli PLA'da delik açılabilir)
ISIK_YARIK = (36, 1.6)   # ürün sahibi: çukurun LED şeridine bakan DİKEY iç duvarı şerit şerit açık -> 24 dikey pencere,
                         # 1,6 mm geniş; ışık yandan çukurun içine vurur (üst yüz kapalı kalır)
ISIK_R = (28.05, 34.6)   # ışık oyuğu: LED'ler (5x5 mm, r ≈ 31) halka tavana yaslanınca bu oyuğun içine girer
CANAK_GOVDE_R = YUVA_R + YUVA_DUVAR   # çukurun dış yarıçapı (tutucu plaka da bu kadar)
YAZI, YAZI_BOY, YAZI_Z = "eco ai", 13.0, 44.5   # logo hoparlör ızgarasının üstünde

# ---------------------------------------------------------------- parçalar (TAHMİN; ölçülünce düzelt)
PARCA = {
    "hoparlor": (50.0, 22.0),
    "hoparlor_miknatis_r": 20.7,         # arkadaki mıknatıs yarıçapı (ürün sahibi: eyer yarıçapı 21 = 20,7 + 0,3 pay)            # 4 Ω 3 W YUVARLAK: Ø50, derinlik (mıknatıs dahil) tahmin
    "pil_4aa": (62.5, 58.0, 15.5),       # 4'lü AA yatağı, 4 pil yan yana: en (pillere dik, x), boy (pil ekseni, y),
                                         # yükseklik; TAHMİN, ölç (yaygın yatak 62-63 x 57-58 x 15-16)
    "duzenleyici": (11.5, 15.5, 6.0),    # 5 V düzenleyici (Pololu S9V11F5 11,4 x 15,2; pinlerle ~6 mm)
    "max98357": (19.0, 18.0, 10.0),      # vida klemensi lehimliyse ~10 mm
    "esp32": (57.2, 28.5, 1.6),          # ESP32-S3 DevKit (ürün sahibinin STEP'i, cad/parca_stl/): kart en, boy, kalınlık
    "kcd11": (15.0, 20.0, 18.5, 2.0, 1.6),   # yuvarlak: panel deliği Ø, arkadaki gövde+uçlar derinliği, flanş Ø, flanş
                                             # kalınlığı, panel kalınlığı (tırnaklar ~1-2 mm panele oturur); TAHMİN, ölç
    "inmp441": (14.0, 14.0, 3.0),
    "halka": (55.0, 70.0, 1.6),          # NeoPixel halka (ürün sahibi ölçtü): iç Ø, dış Ø, kart kalınlığı
    "halka_led": (5.0, 1.6),             # WS2812B 5050: en, yükseklik (kartın üstünde, r ≈ 31)
    "rc522": (60.0, 40.0, 1.6, 3.0),     # en, boy, PCB, alt bileşen yüksekliği
    "pn5180": (70.0, 39.0, 1.6, 3.0),
}
# NFC antenin kart üzerindeki merkezi (kart merkezine göre x, y): figürün tam altına getirilir
ANTEN_GERCEK = {"rc522": ((-5.0, 0.0), (38.0, 34.0)), "pn5180": ((15.0, 0.0), (37.0, 37.0))}  # (merkez, en x boy), tahmin
ANTEN_KAYMA = {"rc522": (-5.0, 0.0),    # RC522: 8'li pin sırası kısa kenarda (+x, kartın raylara girdiği uç: kablo
                                        # erişimi kolay); anten öteki yana ~5 mm kaymış (tahmin)
               "pn5180": (10.0, 0.0)}   # PN5180: anten kartın bir ucunda (~39x39; merkezi kart merkezinden ~15 mm);
                                        # kabuğun eğrisine sığsın diye 10 mm kaydırıldı: anten merkezi figürden 5 mm yanda

# ---------------------------------------------------------------- yerleşim (merkez x, y; alt z)
# Hoparlör (yuvarlak Ø50) önde DİK durur, çocuğa bakar: ses ön duvardaki ızgaradan çıkar. Taban plakasındaki beşiğe oturur,
# kabuğun içinden inen bir "ses yakası" ızgaraya yönlendirir.
HOP_ZC = TABAN_KAL + PARCA["hoparlor"][0] / 2 + 0.6   # merkez yüksekliği


def _hop_on_y():
    """Hoparlörün ön yüzü: Ø50 çember her noktasında kabuğun içinde kalacak en ön y."""
    r = PARCA["hoparlor"][0] / 2
    return min(math.sqrt(max(0.0, (ic_r(HOP_ZC + r * math.sin(t)) - 0.6) ** 2 - (r * math.cos(t)) ** 2))
               for t in np.linspace(0, 2 * math.pi, 120, endpoint=False))
# Pil kutusu: 4xAA yatağı ters durur (açık yüzü aşağıda, kapağa bakar), sırtı kutunun tavanına ince çift taraflı
# bantla yapışır; piller alttan takılır. Kapak taban plakasıyla aynı hizada: solda iki dil plakadaki yuvalara girer,
# sağda tek M3 havşa vida (plakadaki ısıl gömme somuna). Kutunun duvarı kapağın kenarına basar (kapak içeri kaçmaz).
PIL_Y = -11.4                        # kutunun ortası: arka köşeleri kabuğa, ön duvarı hoparlöre değmez
PIL_PAY = 0.4                        # yatak ile kutu arası (her yanda)
PIL_DUVAR = 2.4                      # kutu duvarı; iç 1,2 mm'si kapağın kenarına basar
PIL_KAPAK_KENAR = 1.2                # kapak boşluktan her yanda bu kadar geniş
PIL_BANT = 0.5                       # yatağın sırtı ile tavan arası (çift taraflı bant)
PIL_TAVAN = 1.6
PIL_KAPAK_KOSE = 4.0
PIL_IC = (PARCA["pil_4aa"][0] / 2 + PIL_PAY, PARCA["pil_4aa"][1] / 2 + PIL_PAY)   # boşluğun yarı eni, yarı boyu
Z_PIL_TAVAN = TABAN_KAL + 0.3 + PARCA["pil_4aa"][2] + PIL_BANT                       # boşluğun üstü
Z_PIL_UST = Z_PIL_TAVAN + PIL_TAVAN                                                  # tavanın üstü
PIL_KAPAK_XE = PIL_IC[0] + PIL_KAPAK_KENAR                                           # kapağın yarı eni
PIL_DIL_Y = (PIL_Y - 18.0, PIL_Y + 18.0)                                             # soldaki iki dil
PIL_VIDA_XY = (PIL_KAPAK_XE + 4.5, PIL_Y)                                            # sağdaki vida
AMP_XY = (19.0, 2.0)                 # MAX98357A: kutunun tavanında, sağ önde (hoparlöre yakın)
DUZ_XY = (-19.0, 2.0)                # 5 V düzenleyici: tavanda, sol önde (anahtara yakın)
ANAHTAR_ACI, ANAHTAR_Z = 155.0, 28.0 # sol yan duvar; pil kutusunun üstüne çıktı
# ESP32-S3: ürün sahibi "jumper takmama uygun yer kalsın". Kart TERS takılır (bileşenler aşağı, pinler yukarı): dişi
# jumper'lar üst kabuk açıkken yukarıdan takılır. Kart arkada, pil kutusunun tavanının üstünde; uzun kenarı x boyunca,
# USB-C uçları +x, anten -x. Kullanılan bütün uçlar J1 sırasında: J1 öne (okuyucuya) bakar, arka sıraya (J3) jumper
# takılmaz (kabuğun eğrisine yer kalmaz). Kod yüklemek için taban açılır, USB-C ESP32'nin kendi ucuna takılır.
ESP_XY = (0.0, -32.7)                # kartın ortası: köşeleri kabuğun alt ağzından geçmeli (GECIS_R)
ESP_Z = Z_PIL_UST + 0.6 + 3.4        # bileşen yüzü (aşağı bakar; bileşenler 3,4 mm); kartın arka yüzü ESP_Z + 1,6
JUMPER_BOY = 14.0 + 2.0              # dişi jumper gövdesi (14) + kablonun bükülme payı (üstte okuyucu; kabloyu yana yatır)
ESP_STL = os.path.join(KOK, "parca_stl", "esp32s3_devkit.stl")   # STEP'ten: kart x ±28,6, y ±14,25, z 0..1,6 (pinler -z)
MIKROFON = False                     # ürün sahibi (16 Ekim 2026): mikrofon şimdilik yok (sonra eklenecek; yeri ayrılı)
MIK_XY = (0.0, -40.8)                # yuvarlak INMP441 kartı (Ø14), figür çukuru ile kabuk kenarı arasında
UST_ACILAR = (38.0, 142.0, 218.0, 322.0)    # halka/NFC tutucu direkleri (ürün sahibi, 21 Ekim 2026: öndeki ikisi
                                            # hoparlörden uzaklaştı; okuyucunun köşelerine de değmez)
# Tutucu vidasız, pimli (ürün sahibi, 21 Ekim 2026): kabuğun direklerinin ucunda Ø5 pim, tutucunun tablasındaki deliğe
# (3 ezilen kaburga, sıkı geçme) girer. Pim uzun: tutucu tasarımdan birkaç mm aşağıda kalsa da tutar.
PIM_R, PIM_BOY = 2.5, 10.0
TABLA_R = 4.6                        # tutucudaki pim tablası
VIDA_ACILAR = (0.0, 180.0, 210.0, 330.0)    # taban vidaları (pil kutusu ve ESP32'nin dışında)
VIDA_R = 50.0
UST_DIREK_R = 41.0                   # halka/NFC tutucusunu taşıyan, kabuğun üstünden inen direkler
# Kedi kulakları (ürün sahibi, 23 Ekim 2026; cad/kulaklar.py): ayrı basılır, kabuğun omzundaki iki yuvaya dilleriyle
# takılır. Yuvalar kabukta; içte her yuvanın altında dili saran bir kaide.
KULAK = True
KULAK_ACILAR = (45.0, 135.0)         # sağ ön ve sol ön omuz (önden bakınca figürü kapatmaz, yıldızlara değmez)
KULAK_Z = 53.5                       # kulağın oturduğu omuz noktası (r ≈ 50)
KULAK_EGIM, KULAK_GOM = 4.0, 3.0     # geriye yatıklık (°), tabanın yüzeye gömülmesi
KULAK_DIL = ((-5.0,), 8.0, (-1.0, 3.0), (-7.0, 6.0))   # dil x'i (sağ kulak; solda aynası), eni, y aralığı (ön yüz +3),
                                                       # z aralığı (yerel). Dil kulağın içe (üst yüze) yakın yarısında:
                                                       # dış yarıda omuz dikleşir, dil ve yuva dışarıdan görünürdü
AYAK = (10.0, 1.0)                   # silikon ayak yuvası Ø, derinlik
AYAKLAR = ((0.0, 40.0), (-45.0, 10.0), (45.0, 10.0), (0.0, -49.0))   # pil kapağının dışında


def dis_r(z):
    u = abs(z - ZC) / B
    return R * max(0.0, 1 - u ** N) ** (1 / N)


def kulak_yon(aci):
    return 90 + (aci - 90) * 0.45    # kulak öne bakar, biraz dışa açık


def kulak_yer(m, aci, geri=False):
    """Kulağın yerel koordinatından (taban z=0, xz düzlemi, ön yüz +y) kabuktaki yerine; geri=True: tersi."""
    r = dis_r(KULAK_Z)
    x, y = 0.98 * r * math.cos(math.radians(aci)), 0.98 * r * math.sin(math.radians(aci))
    if geri:
        return m.translate([-x, -y, -KULAK_Z]).rotate([0, 0, -(kulak_yon(aci) - 90)]).rotate([KULAK_EGIM, 0, 0]).translate([0, 0, KULAK_GOM])
    return m.translate([0, 0, -KULAK_GOM]).rotate([-KULAK_EGIM, 0, 0]).rotate([0, 0, kulak_yon(aci) - 90]).translate([x, y, KULAK_Z])


def kulak_dilleri(aci, pay=0.0, uzat=0.0):
    """Kulağın iki dili kabuktaki yerinde (pay: her yanda büyütme, uzat: aşağı/yukarı uzatma; yuva için)."""
    xs, en, (y0, y1), (z0, z1) = KULAK_DIL
    s = 1.0 if math.cos(math.radians(aci)) > 0 else -1.0
    d = M()
    for xc in (s * x for x in xs):
        d = d + kutu(xc - en / 2 - pay, xc + en / 2 + pay, y0 - pay, y1 + pay, z0 - pay - uzat, z1 + uzat)
    return kulak_yer(d, aci)


def ic_r(z):
    return dis_r(z) - DUVAR


def profil(ofs=0.0, z0=0.0, z1=H):
    pts = [(0, z0)]
    for z in np.linspace(z0, z1, 70):
        pts.append((max(0.5, dis_r(z) + ofs), z))
    pts.append((0, z1))
    return pts


HOP_YF = _hop_on_y()                         # hoparlörün ön yüzü (y)
GECIS_R = ic_r(1.2) - 0.4                    # kabuğun alt ağzı: taban plakasındaki her şey bunun içinde kalmalı
Z_CANAK_TABAN = H - CUKUR_DERIN              # figür tabanının oturduğu yüz
Z_HALKA_UST = H - DUVAR                      # halka kartı üst yüzün altına (tavana) yaslanır, LED'ler oyukta
Z_HALKA_ALT = Z_HALKA_UST - PARCA["halka"][2]
TUTUCU_KAL = 2.0
Z_MIK = H - DUVAR - 3.0 - 1.2                # mikrofon kartı (deliğe bakar, üstte 1,2 mm conta payı)
Z_TUTUCU_ALT = Z_HALKA_ALT - TUTUCU_KAL      # halka tutucu plakası (halkayı tavana bastırır)
Z_OKUYUCU_UST = Z_CANAK_TABAN - ZEMIN_KAL - 0.3   # NFC okuyucunun anten yüzü: çukur zemininin hemen altı




def esp_yerine(m):
    """ESP32 STEP koordinatından (bileşenler +z, pinler -z; J1 +y, USB-C -x) standdaki ters yerine: y ekseni etrafında
    180° (J1 önde kalır, USB-C +x'e döner)."""
    return m.rotate([0, 180, 0]).translate([ESP_XY[0], ESP_XY[1], ESP_Z + PARCA["esp32"][2]])


def esp_stl():
    """Ürün sahibinin ESP32-S3 modeli standdaki yerinde (yalnız görsel; denetim kutu zarflarla)."""
    m = trimesh.load(ESP_STL)
    m.apply_transform(trimesh.transformations.rotation_matrix(math.pi, [0, 1, 0]))
    m.apply_translation([ESP_XY[0], ESP_XY[1], ESP_Z + PARCA["esp32"][2]])
    return m


def anahtar_yer():
    """KCD11 (anahtar ekseni yerel +x, z = ANAHTAR_Z): (flanş oturma düzlemi x, panelin iç yüzü x).
    Dış gövde eğri; flanş düz oturmalı: flanşın değdiği dairenin gövdeye en içte değdiği yerden düz bir oturma yüzü
    açılır (gövdeye en fazla birkaç onda mm gömülür, dışa hiçbir şey eklenmez). Panel içten düz ve PARCA kalınlığında."""
    dd, derin, fd, fk, pk = PARCA["kcd11"]
    r = fd / 2 + 0.3
    x_otur = min(math.sqrt(dis_r(ANAHTAR_Z + r * math.sin(u)) ** 2 - (r * math.cos(u)) ** 2)
                 for u in np.linspace(0, 2 * math.pi, 72, endpoint=False))
    return x_otur, x_otur - pk


def pil_kapak_cs(pay=0.0):
    """Pil kapağının dış çizgisi (xy, yuvarlak köşeli); pay: her yanda büyütme (plakadaki delik için)."""
    w, d = 2 * PIL_KAPAK_XE + 2 * pay, 2 * (PIL_IC[1] + PIL_KAPAK_KENAR) + 2 * pay
    return yuvarlak_dikdortgen(w, d, PIL_KAPAK_KOSE + pay).translate([0, PIL_Y])


def pil_dil(pay=0.0):
    """Kapağın solundaki iki dil (plakadaki yuvalara girer): üstü düz, altı 45° pahlı (desteksiz basılır, kapak
    plakaya oturunca dilin pahı yuvanın pahına dayanır, kapak aşağı düşmez)."""
    x0 = -PIL_KAPAK_XE
    kesit = CS([cokgen([(x0 + 0.5, -pay), (x0 + 0.5, 2.2 + pay), (x0 - 2.4 - pay, 2.2 + pay), (x0 - 2.4 - pay, 1.2 - pay),
                        (x0 - 1.2 - pay, -pay)])])
    d = None
    for yd in PIL_DIL_Y:
        e = xz_den_y_ye(kesit, yd - 4.0 - pay, yd + 4.0 + pay)
        d = e if d is None else d + e
    return d


def pil_kapagi(yazi_ile=True):
    """Pil kapağı (yerinde, z 0..TABAN_KAL): plaka + soldaki iki dil + sağda vida tablası (M3 havşa); dış yüzde yazı
    (yazi_ile=False: yazı oyulmaz, renkli baskıda kakma olur)."""
    k = xy_prizma(pil_kapak_cs(), 0, TABAN_KAL)
    # dilin karşısındaki alt kenar pahı: kapak eğik takılırken plakanın kenarına takılmaz
    k = k - xz_den_y_ye(CS([cokgen([(-PIL_KAPAK_XE - 1, -1), (-PIL_KAPAK_XE + 2.0, -1), (-PIL_KAPAK_XE - 1, 2.0)])]), -80, 80)
    k = k + pil_dil()
    xv, yv = PIL_VIDA_XY
    k = k + kutu(PIL_KAPAK_XE - 1.0, xv + 4.5, yv - 6.0, yv + 6.0, 0, 1.8)
    k = k - silindir(1.7, -1, 5, x=xv, y=yv, seg=24) - silindir(3.2, -0.01, 1.5, x=xv, y=yv, seg=32, r2=1.7)
    return k - xy_prizma(pil_kapak_yazi(), -1, 0.6) if yazi_ile else k


def pil_kapak_yazi():
    """Kapağın dış yüzündeki yazı (2B, ayna: alttan okunur)."""
    return (yazi_duz("4 x AA", 8.0, FONT, ayna=True).translate([0, PIL_Y + 6])
            + yazi_duz("1,5 V", 6.0, FONT, ayna=True).translate([0, PIL_Y - 8]))


def pil_bosluklari():
    """Taban plakasından çıkarılan: pil boşluğu, kapak deliği, dil yuvaları, vida tablası cebi ve tırnak çentiği,
    ısıl gömme somun deliği, tavandaki kablo delikleri."""
    xi, yi = PIL_IC
    b = kutu(-xi, xi, PIL_Y - yi, PIL_Y + yi, -1, Z_PIL_TAVAN)
    b = b + xy_prizma(pil_kapak_cs(0.25), -1, TABAN_KAL)
    b = b + pil_dil(0.25)
    xv, yv = PIL_VIDA_XY
    b = b + kutu(PIL_KAPAK_XE - 1.0, xv + 4.8, yv - 6.3, yv + 6.3, -1, 1.85)               # vida tablası cebi
    b = b + kutu(xv + 4.8 - 0.01, xv + 7.0, yv - 4.0, yv + 4.0, -1, 1.0)                    # tırnak çentiği (kapağı açmak)
    b = b + silindir(2.0, 1.8, 1.8 + 5.9, x=xv, y=yv, seg=24) + silindir(1.6, 1.8, 10.3, x=xv, y=yv, seg=24)  # Ø4 somun
    for x in (-20.0, 20.0):                                                                  # yatağın kabloları
        b = b + kutu(x - 5, x + 5, PIL_Y + yi - 5.0, PIL_Y + yi - 0.5, Z_PIL_TAVAN - 1, Z_PIL_UST + 1)
    return b


def gorunmez():
    return M()


# ---------------------------------------------------------------- zarflar (çarpışma denetimi için)
def zarflar(nfc):
    z = {}
    hd, hdr = PARCA["hoparlor"]
    yf = HOP_YF
    # ön çerçeve Ø50 (5 mm) + sepet Ø50 -> Ø32 (8 mm) + mıknatıs Ø32 (kalan); hepsi tahmin
    mr = PARCA["hoparlor_miknatis_r"]
    hop = (silindir(hd / 2, hdr - 5, hdr, seg=96) + silindir(mr, hdr - 13, hdr - 5, seg=96, r2=hd / 2)
           + silindir(mr, 0, hdr - 13, seg=64))
    z["hoparlör (önden)"] = hop.rotate([-90, 0, 0]).translate([0, yf - hdr, HOP_ZC])
    w, d, h = PARCA["pil_4aa"]
    z["4xAA yatağı"] = kutu(-w / 2, w / 2, PIL_Y - d / 2, PIL_Y + d / 2, TABAN_KAL + 0.3, TABAN_KAL + 0.3 + h)
    w, d, h = PARCA["duzenleyici"]
    z["5 V düzenleyici"] = kutu(DUZ_XY[0] - w / 2, DUZ_XY[0] + w / 2, DUZ_XY[1] - d / 2, DUZ_XY[1] + d / 2,
                                Z_PIL_UST + 1, Z_PIL_UST + 1 + h)
    w, d, h = PARCA["max98357"]
    z["MAX98357A"] = kutu(AMP_XY[0] - w / 2, AMP_XY[0] + w / 2, AMP_XY[1] - d / 2, AMP_XY[1] + d / 2,
                          Z_PIL_UST + 1, Z_PIL_UST + 1 + h)
    dd, derin, fd, fk, pk = PARCA["kcd11"]
    x_otur, x_ic = anahtar_yer()
    k = (silindir(dd / 2 - 0.3, x_ic - derin, x_otur, seg=48)                  # gövde + uçlar (delikten geçer)
         + silindir(fd / 2, x_otur, x_otur + fk, seg=48)                       # flanş (dışta, oturma yüzünde)
         + silindir(dd / 2 - 1.5, x_otur + fk, x_otur + fk + 3.0, seg=48))     # basma tuşu
    k = k.rotate([0, 90, 0]).translate([0, 0, ANAHTAR_Z]).rotate([0, 0, ANAHTAR_ACI])
    z["KCD11 anahtar"] = k
    # ESP32 (STEP ölçüleri): kart, üst bileşenler (USB-C'ler dahil), modülün kart dışına taşan anten ucu, pin lehimleri,
    # başlık plastiği; pinler jumper payının içinde
    e = (kutu(-28.6, 28.6, -14.25, 14.25, 0, 1.6) + kutu(-28.6, 28.6, -10.45, 10.45, 1.6, 5.0)
         + kutu(28.5, 35.3, -9.0, 9.0, 1.6, 2.4))
    for s in (-1, 1):
        e = e + kutu(-27.2, 27.5, min(s * 12.2, s * 13.4), max(s * 12.2, s * 13.4), 1.6, 3.1)
        e = e + kutu(-27.7, 28.2, min(s * 11.5, s * 14.0), max(s * 11.5, s * 14.0), -2.5, 0)
    e = e + kutu(-27.5, 28.0, -13.4, -12.1, -8.1, -2.5)                                # J3 pin uçları (jumper yok)
    j = kutu(-28.0, 28.3, 11.3, 14.3, -2.5 - JUMPER_BOY, -2.5)                          # J1 jumper'ları
    z["ESP32-S3"] = esp_yerine(e)
    z["jumper payı"] = esp_yerine(j)
    w, d, h = PARCA["inmp441"]
    if MIKROFON:
        z["INMP441 mikrofon"] = silindir(w / 2, Z_MIK, Z_MIK + h, x=MIK_XY[0], y=MIK_XY[1], seg=32)
    ri, rd, kal = PARCA["halka"]
    lw, lh = PARCA["halka_led"]
    rl = (ri + rd) / 4
    z["NeoPixel 16"] = (silindir(rd / 2, Z_HALKA_ALT, Z_HALKA_UST, seg=96) - silindir(ri / 2, Z_HALKA_ALT - 1, Z_HALKA_UST + 1, seg=96)
                        + (silindir(rl + lw / 2, Z_HALKA_UST, Z_HALKA_UST + lh, seg=96)
                           - silindir(rl - lw / 2, Z_HALKA_UST - 1, Z_HALKA_UST + lh + 1, seg=96)))
    w, d, pcb, alt = PARCA[nfc]
    cx, cy = -ANTEN_KAYMA[nfc][0], -ANTEN_KAYMA[nfc][1]
    z[f"{nfc.upper()} okuyucu"] = (kutu(cx - w / 2, cx + w / 2, cy - d / 2, cy + d / 2, Z_OKUYUCU_UST - pcb, Z_OKUYUCU_UST)
                                   + kutu(cx - w / 2 + 2.5, cx + w / 2 - 2.5, cy - d / 2 + 2.5, cy + d / 2 - 2.5,
                                          Z_OKUYUCU_UST - pcb - alt, Z_OKUYUCU_UST - pcb))
    return z


# ---------------------------------------------------------------- basılacak parçalar
def kabuk():
    dis = dondur(profil(), SEG)
    ic = dondur(profil(-DUVAR, -1.0, H - DUVAR), SEG)
    g = dis - ic
    # logo (kabarık)
    dis12 = dondur(profil(1.2), SEG)
    g = g + ((xz_den_y_ye(yazi_duz(YAZI, YAZI_BOY, FONT, ayna=True), 0, 80, x=0, z=YAZI_Z) ^ dis12) - dondur(profil(-0.8), SEG))
    # figür çukuru: zemin ve duvar kabuğun parçası; zeminin altında LED'lerin üstünde ışık oyuğu
    g = g + silindir(CANAK_GOVDE_R, Z_CANAK_TABAN - ZEMIN_KAL, H - DUVAR + 0.01, seg=SEG)
    g = g - silindir(YUVA_R, Z_CANAK_TABAN, H + 1, seg=SEG)
    g = g - (silindir(ISIK_R[1], H - DUVAR - 1, H - ISIK_KAL, seg=SEG)
             - silindir(ISIK_R[0], H - DUVAR - 2, H, seg=SEG))   # tavandaki ışık oyuğu (çukurun çevresinde)
    n, gen = ISIK_YARIK   # çukur duvarında dikey pencereler: ışık oyuğundan (LED'ler) çukurun içine; üstte 0,6 mm dudak kalır
    for i in range(n):
        g = g - kutu(YUVA_R - 0.5, ISIK_R[0] + 0.5, -gen / 2, gen / 2, H - DUVAR - 0.2, H - ISIK_KAL).rotate([0, 0, 360.0 * (i + 0.5) / n])
    # tutucu direkleri (üstten iner) ve uçlarında pim (tutucunun tablasına geçer; ucu pahlı)
    for aci in UST_ACILAR:
        x, y = UST_DIREK_R * math.cos(math.radians(aci)), UST_DIREK_R * math.sin(math.radians(aci))
        z0 = Z_TUTUCU_ALT + TUTUCU_KAL   # direk tutucu plakanın üstünde biter
        g = g + silindir(3.8, z0, H - DUVAR + 0.5, x=x, y=y, seg=32)
        g = g + silindir(PIM_R, z0 - PIM_BOY + 0.8, z0 + 0.01, x=x, y=y, seg=32)
        g = g + silindir(PIM_R - 0.8, z0 - PIM_BOY, z0 - PIM_BOY + 0.8, x=x, y=y, seg=32, r2=PIM_R)
    # taban vida kolonları (duvara yapışık, alttan M3 ısıl gömme somun)
    for aci in VIDA_ACILAR:
        x, y = VIDA_R * math.cos(math.radians(aci)), VIDA_R * math.sin(math.radians(aci))
        kol = silindir(4.5, TABAN_KAL, 14.0, x=x, y=y, seg=32) + kutu(-2.2, 2.2, 0, 8, TABAN_KAL, 14.0).rotate([0, 0, aci - 90]).translate([x, y, 0])
        g = g + ((kol ^ dondur(profil(-0.5), SEG)) - silindir(2.0, TABAN_KAL - 1, TABAN_KAL + 6.5, x=x, y=y, seg=24))
    # ön: hoparlör ızgarası (logonun altında, Ø2,4 delikler) + içte ses yakası (hoparlörün önünden duvara boru)
    hd, hdr = PARCA["hoparlor"]
    izgara = CS()
    for i in range(-6, 7):
        for j in range(-6, 7):
            x, zz = i * 4.4 + (2.2 if j % 2 else 0.0), j * 3.8
            if x * x + zz * zz < (hd / 2 - 5) ** 2 and HOP_ZC + zz < YAZI_Z - YAZI_BOY / 2 - 1.5 and HOP_ZC + zz > TABAN_KAL + 5:
                izgara = izgara + CS.circle(1.2, 20).translate([x, zz])
    g = g - xz_den_y_ye(izgara, 40, 75, x=0, z=HOP_ZC)
    yaka = (silindir(hd / 2 - 1.0, 0, 30, seg=96) - silindir(hd / 2 - 3.0, -1, 31, seg=96)).rotate([-90, 0, 0]).translate([0, HOP_YF + 2.0, HOP_ZC])
    g = g + (yaka ^ dondur(profil(-1.0), SEG) ^ kutu(-40, 40, -70, 70, TABAN_KAL + 1.0, H))
    # anahtar: Ø delik + flanşın düz oturma yüzü (dışta, gövdeye gömülü) + içte düz panel (tırnaklar için)
    dd, derin, fd, fk, pk = PARCA["kcd11"]
    x_otur, x_ic = anahtar_yer()
    oyuk = (silindir(dd / 2 + 0.1, x_ic - 5, 80, seg=64) + silindir(fd / 2 + 0.3, x_otur, 80, seg=96)
            + silindir(fd / 2 + 1.5, x_ic - 6, x_ic, seg=96))
    g = g - oyuk.rotate([0, 90, 0]).translate([0, 0, ANAHTAR_Z]).rotate([0, 0, ANAHTAR_ACI])
    # mikrofon deliği ve cebi (MIKROFON açılınca)
    if MIKROFON:
        g = g - silindir(0.8, H - 6, H + 1, x=MIK_XY[0], y=MIK_XY[1], seg=16)
        r = PARCA["inmp441"][0] / 2 + 0.3
        cep = (silindir(r + 1.2, Z_MIK + 1.5, H - DUVAR + 0.01, seg=32) - silindir(r, Z_MIK, H, seg=32)).translate([MIK_XY[0], MIK_XY[1], 0])
        g = g + (cep ^ dondur(profil(-0.6), SEG))
    # kedi kulağı yuvaları: içte dili saran kaide (dış yüzden taşmaz), sonra dilin yuvası
    if KULAK:
        xs, en, (y0, y1), (z0, z1) = KULAK_DIL
        for aci in KULAK_ACILAR:
            kaide = M()
            for xc in ((1.0 if math.cos(math.radians(aci)) > 0 else -1.0) * x for x in xs):
                kaide = kaide + kutu(xc - en / 2 - 2.2, xc + en / 2 + 2.2, y0 - 2.2, y1 + 2.2, z0 - 2.5, KULAK_GOM)
            g = g + (kulak_yer(kaide, aci) ^ dondur(profil(-0.4), SEG))
            g = g - kulak_dilleri(aci, pay=0.2, uzat=1.0)
    # kabuğun alt kenarında taban plakası için 1,2 mm oturma basamağı
    g = g - silindir(ic_r(1.0) + 0.6, -1, 1.2, seg=SEG)
    return g


def tutucu(nfc):
    """Halka + NFC tutucu: halkayı tavana bastırır (ortası çukura açık), altından inen raylar okuyucuyu çukur zemininin
    hemen altında tutar; 4 kolla kabuğun direklerine vidalanır."""
    zt = Z_TUTUCU_ALT
    w, d, pcb, alt = PARCA[nfc]
    cx, cy = -ANTEN_KAYMA[nfc][0], -ANTEN_KAYMA[nfc][1]
    ri, rd, kal = PARCA["halka"]
    p = silindir(rd / 2 + 2.5, zt, zt + TUTUCU_KAL, seg=SEG)
    for aci in UST_ACILAR:
        x, y = UST_DIREK_R * math.cos(math.radians(aci)), UST_DIREK_R * math.sin(math.radians(aci))
        kol = kutu(0, UST_DIREK_R, -4, 4, zt, zt + TUTUCU_KAL).rotate([0, 0, aci])
        p = p + kol + silindir(TABLA_R, zt - 1.5, zt + TUTUCU_KAL, x=x, y=y, seg=32)   # pim tablası 3,5 mm
        delik = silindir(PIM_R + 0.25, zt - 3, zt + 5, x=x, y=y, seg=32) \
            + silindir(PIM_R + 0.25, zt + TUTUCU_KAL - 0.6, zt + TUTUCU_KAL + 0.01, x=x, y=y, seg=32, r2=PIM_R + 0.85)   # giriş pahı
        p = p - delik
        for k in range(3):   # ezilen kaburgalar: pim (Ø5) ile 0,12 mm sıkı geçme; kırılmaz, ezilir
            p = p + kutu(PIM_R - 0.12, PIM_R + 0.4, -0.4, 0.4, zt - 1.5, zt + TUTUCU_KAL - 0.6).rotate([0, 0, 120 * k + aci]).translate([x, y, 0])
    p = p - silindir(CANAK_GOVDE_R + 0.4, zt - 1, zt + 5, seg=SEG)            # çukur geçer
    # halkayı tavandaki ışık oyuğuna giren LED'ler ortalar (bilezik gerekmez: plakanın üst yüzü düz, ters basılır);
    # arkada halkanın kablo lehimleri için plakadan geçen çentik
    p = p - kutu(-3.5, 3.5, -rd / 2 - 5, -rd / 2 + 4.5, zt - 1, zt + TUTUCU_KAL + 1)
    # okuyucu rayları: plakanın altından iner, kart uzun kenarlarından kayarak girer
    z_alt = Z_OKUYUCU_UST - pcb - 1.6
    for s in (-1, 1):
        y_ic = cy + s * (d / 2 + 0.3)
        ray = kutu(cx - w / 2 + 6, cx + w / 2 - 6, min(y_ic, y_ic + s * 2.0), max(y_ic, y_ic + s * 2.0), z_alt, zt + 0.01)
        y_d = cy + s * (d / 2 - 1.2)
        dudak = kutu(cx - w / 2 + 6, cx + w / 2 - 6, min(y_d, y_ic), max(y_d, y_ic), z_alt, Z_OKUYUCU_UST - pcb - 0.2)
        ust = kutu(cx - w / 2 + 6, cx + w / 2 - 6, min(y_d, y_ic + s * 2.0), max(y_d, y_ic + s * 2.0), Z_OKUYUCU_UST + 0.2, zt + 0.01)
        p = p + ray + dudak + (ust - silindir(CANAK_GOVDE_R + 0.4, zt - 9, zt + 5, seg=SEG))
    # çukur (Ø54,9) büyüyünce rayların üstü çukurun zemin gövdesine girer: zemin altına kadar kesilir
    p = p - silindir(CANAK_GOVDE_R + 0.4, Z_CANAK_TABAN - ZEMIN_KAL - 0.2, H, seg=SEG)
    return p


TABAN_OZ = ("vida", "ayak", "pil", "hoparlor", "esp32", "amfi")


def taban(oz=TABAN_OZ):
    """Taban plakası; oz: eklenecek tutucular (adım adım gösterim için alt küme verilebilir)."""
    r = ic_r(1.0) + 0.4
    t = silindir(r, 0, 1.2, seg=SEG) + silindir(ic_r(TABAN_KAL) - 0.3, 1.2, TABAN_KAL, seg=SEG)
    # vida delikleri (M3 havşa)
    for aci in VIDA_ACILAR:
        x, y = VIDA_R * math.cos(math.radians(aci)), VIDA_R * math.sin(math.radians(aci))
        # M3 havşa başlı vida: Ø6 baş alt yüzden başlayan 90° koniye gömülür (yüzle aynı hizada)
        t = t - silindir(1.7, -1, 5, x=x, y=y, seg=24) - silindir(3.3, -0.01, 1.6, x=x, y=y, seg=32, r2=1.7) \
            - silindir(3.3, -1, 0.0, x=x, y=y, seg=32)
    # hoparlör beşiği: önde alt yarım çember (Ø50 kenarı oturur) + önünde dudak (öne kaymaz), arkada eyer; kablo bağı yarığı
    if "hoparlor" in oz:
        hd, hdr = PARCA["hoparlor"]
        yf = HOP_YF
        for y0, y1, ric in ((yf - 4.6, yf + 0.01, hd / 2 + 0.3), (yf + 0.01, yf + 1.6, hd / 2 - 2.5)):
            besik = kutu(-hd / 2 - 3, hd / 2 + 3, y0, y1, TABAN_KAL - 0.01, HOP_ZC - 6)
            besik = besik - silindir(ric, -5, 80, seg=96).rotate([-90, 0, 0]).translate([0, -10, HOP_ZC])
            t = t + besik
        # eyer: ürün sahibi (20 Ekim 2026) bir eyer daha istemişti (y ≈ 15); 21 Ekim'de pil kutusu oraya geldi, ikinci
        # eyer kalktı (kutunun ön duvarı hoparlörün 5 mm arkasında)
        eyer_merkez = yf - hdr + 5
        for ym in (eyer_merkez,):
            eyer = kutu(-18, 18, ym - 2, ym + 2, TABAN_KAL - 0.01, HOP_ZC - 9)
            t = t + (eyer - silindir(PARCA["hoparlor_miknatis_r"] + 0.3, -5, 80, seg=96).rotate([-90, 0, 0]).translate([0, -10, HOP_ZC]))
        for x in (-hd / 2 - 1.5, hd / 2 - 1.0):
            t = t - kutu(x, x + 2.5, yf - 10, yf - 6, -1, TABAN_KAL + 1)
    # pil kutusu: duvarlar + tavan (boşluk, kapak deliği ve yuvalar en sonda çıkarılır); sağda kapak vidasının kolonu
    if "pil" in oz:
        xo, yo = PIL_IC[0] + PIL_DUVAR, PIL_IC[1] + PIL_DUVAR
        t = t + kutu(-xo, xo, PIL_Y - yo, PIL_Y + yo, TABAN_KAL - 0.01, Z_PIL_UST)
        t = t + silindir(4.2, 1.0, 11.0, x=PIL_VIDA_XY[0], y=PIL_VIDA_XY[1], seg=32)
        # 5 V düzenleyici: tavanda alçak çerçeve (çift taraflı bantla yapışır)
        w, d, h = PARCA["duzenleyici"]
        t = t + (kutu(DUZ_XY[0] - w / 2 - 1.2, DUZ_XY[0] + w / 2 + 1.2, DUZ_XY[1] - d / 2 - 1.2, DUZ_XY[1] + d / 2 + 1.2, Z_PIL_UST - 0.01, Z_PIL_UST + 2.0)
                 - kutu(DUZ_XY[0] - w / 2 - 0.2, DUZ_XY[0] + w / 2 + 0.2, DUZ_XY[1] - d / 2 - 0.2, DUZ_XY[1] + d / 2 + 0.2, Z_PIL_UST, Z_PIL_UST + 3))
    w, d, h = PARCA["max98357"]
    if "amfi" in oz:
        t = t + (kutu(AMP_XY[0] - w / 2 - 1.2, AMP_XY[0] + w / 2 + 1.2, AMP_XY[1] - d / 2 - 1.2, AMP_XY[1] + d / 2 + 1.2, Z_PIL_UST - 0.01, Z_PIL_UST + 2.5)
                 - kutu(AMP_XY[0] - w / 2 - 0.2, AMP_XY[0] + w / 2 + 0.2, AMP_XY[1] - d / 2 - 0.2, AMP_XY[1] + d / 2 + 0.2, Z_PIL_UST, Z_PIL_UST + 4))
    # ESP32 yuvası (ters kart): iki uzun kenarda kanal (iç kiriş kartı pin sıralarının hemen içinden taşır, dış duvar
    # yandan tutar; aradaki boşluk pin lehimlerine), USB-C ucunda iki köşe kancası (kart altına kayar), anten ucunda
    # esnek tırnak (bastırınca kartın modül ucuna oturur) ve modül ucunun altında destek
    if "esp32" in oz:
        t0, t = t, M()
        xc, yc, ze = 0.0, ESP_XY[1], ESP_Z   # x'te 0'da kurulur, sonra aynalanır (USB-C +x)
        za = ze + PARCA["esp32"][2]
        def yb(a, b, s):
            return min(yc + s * a, yc + s * b), max(yc + s * a, yc + s * b)
        for s in (-1, 1):
            t = t + kutu(xc - 28.5, xc + 28.5, *yb(10.7, 15.4, s), TABAN_KAL - 0.01, ze - 1.8)  # ön kanal kutunun tavanında durur
            t = t + kutu(xc - 28.5, xc + 28.5, *yb(10.7, 11.9, s), ze - 1.9, ze)             # iç kiriş (kartı taşır)
            t = t + kutu(xc - 28.5, xc + 28.5, *yb(14.4, 15.4, s), ze - 1.9, za + 0.5)       # dış duvar
            # USB-C ucu: köşe kancası (USB-C fişleri |dy| < 12,1'den geçer)
            t = t + kutu(xc - 30.2, xc - 28.45, *yb(12.6, 15.4, s), TABAN_KAL - 0.01, ze)
            t = t + kutu(xc - 30.2, xc - 28.75, *yb(12.6, 15.4, s), ze - 0.01, za + 0.9)
            t = t + kutu(xc - 28.75, xc - 27.95, *yb(12.6, 14.2, s), za + 0.1, za + 0.9)
        # anten ucu: modülün altında destek + esnek tırnak (vida direğinden uzak tarafta)
        t = t + kutu(xc + 29.5, xc + 33.5, yc + 1.5, yc + 7.5, TABAN_KAL - 0.01, ze - 0.9)
        t = t + kutu(xc + 35.6, xc + 36.8, yc + 1.5, yc + 7.5, TABAN_KAL - 0.01, ze + 1.0)
        t = t + kutu(xc + 34.6, xc + 35.65, yc + 1.5, yc + 7.5, ze + 0.1, ze + 1.0)
        t = t0 + aynala_x(t)
    # ayak yuvaları
    for x, y in (AYAKLAR if "ayak" in oz else ()):
        t = t - silindir(AYAK[0] / 2 + 0.2, -1, AYAK[1], x=x, y=y, seg=32)
    ic = dondur(profil(-DUVAR - 0.3, 1.0, H - DUVAR), SEG)
    # kabuk alttan indirilirken her şey kabuğun en dar ağzından (z ≈ 1,2) geçmeli: plakanın üstündekiler GECIS_R içinde
    # (ilk baskı, 21 Ekim 2026: hoparlör beşiğinin sağ kolu kabuğun alt kenarına takılıyordu)
    t = (t ^ kutu(-70, 70, -70, 70, -1, 1.2)) + (t ^ ic ^ silindir(GECIS_R, 1.0, H, seg=SEG))
    if "pil" in oz:
        t = t - pil_bosluklari()
    return t


# ---------------------------------------------------------------- figür tabanı + vidalı NFC kapağı
# Ürün sahibi (19 Ekim 2026): figürün altında şişe kapağı gibi dönerek takılan, içinde NFC etiketi olan kapak.
# Taban Ø28 x 8 (5 mm çukurda, 3 mm üstte); altta M24 x 2 benzeri yamuk diş, 1,5 tur. Kapak bir fincan: Ø20 NTAG213
# yapışkan etiket fincanın tabanına yapışır (zeminden 1 mm yukarıda), alt yüzde bozuk para yarığı ve figür adı.
FIGUR_BOY = 8.0
VIDA_ADIM, VIDA_KOK_R, VIDA_DERIN = 2.0, 14.0, 1.0     # erkek diş: kök Ø28, tepe Ø30 (taban Ø52'ye büyüyünce)
VIDA_UST, VIDA_ALT = 0.3, 1.45                         # diş kesiti: tepe ve kök genişliği (60° yanak)
VIDA_PAY = 0.35                                        # yarıçapta ve yanakta boşluk (FDM)
KAPAK_BOY, KAPAK_TABAN = 5.0, 1.0
ETIKET_CAP = 25.0                                      # NTAG213 Ø25 (standart boy)


def figur_taban(topuz=False):
    """Figür tabanı Ø28 x 8: üst yüz düz (figür yapıştırılır), altta kapağın vidalandığı dişli oyuk.
    topuz=True: ayar kartı (üstte tutma topuzu)."""
    r, h = FIGUR_TABAN_D / 2, FIGUR_BOY
    b = dondur([(0, 0), (r - 0.3, 0), (r, 0.3), (r, h - 0.8), (r - 0.8, h), (0, h)], SEG)
    rb = VIDA_KOK_R + VIDA_PAY
    ust = VIDA_UST + 0.5                                # yanakta 0,25 boşluk; yanak açısı erkek dişle aynı
    oyuk = vida_cubugu(rb, VIDA_DERIN, VIDA_ADIM, ust, ust + (VIDA_ALT - VIDA_UST), -1.0, KAPAK_BOY + 0.2)
    oyuk = oyuk + dondur([(0, -1), (rb + 1.3, -1), (rb + 1.3, 0), (rb, 1.3), (0, 1.3)], SEG)        # giriş pahı
    b = b - oyuk
    if topuz:
        b = b + dondur([(0, h - 0.5), (10.0, h - 0.5), (10.0, h + 9.0), (8.5, h + 11.0), (6.0, h + 12.0), (0, h + 12.0)], SEG)
    return b


def figur_kapak(ad=None, no=None):
    """Vidalı NFC kapağı (fincan): dış diş, içte Ø20 etiket yeri; alt yüzde bozuk para yarığı, ad ve numara (ayna:
    alttan okunur). Fincanın tabanı tablada basılır."""
    g = vida_cubugu(VIDA_KOK_R, VIDA_DERIN, VIDA_ADIM, VIDA_UST, VIDA_ALT, 0.0, KAPAK_BOY)
    g = g - (silindir(VIDA_KOK_R + 5, -1, 0.6, seg=SEG) - silindir(VIDA_KOK_R + VIDA_DERIN, -1, 0.6, seg=SEG, r2=VIDA_KOK_R + VIDA_DERIN - 0.6))  # alt pah
    g = g - silindir(ETIKET_CAP / 2 + 0.2, KAPAK_TABAN, KAPAK_BOY + 1, seg=SEG)
    g = g - kutu(-6.5, 6.5, -0.75, 0.75, -1, 0.5)                                # bozuk para / tornavida yarığı
    for metin, yy, boy in ((ad, -7.6, 3.0), (f"No {no}" if no is not None else None, 7.4, 2.8)):
        if not metin:
            continue
        cs = yazi_duz(metin, boy, FONT, ayna=True)
        b = cs.bounds()
        en = b[2] - b[0]
        if en > 20.0:
            cs = cs.scale([20.0 / en, 20.0 / en])
        g = g - cs.translate([0, yy]).extrude(1.4).translate([0, 0, -1])        # 0,4 mm kazıma
    return g


def ay_dede():
    """Ay Dede (gece figürü, telifsiz halk figürü): taban + üstünde uyuyan hilal ay."""
    z0 = FIGUR_BOY - 0.5
    ay = (CS.circle(15.0, 96).translate([0, 15.0]) - CS.circle(12.6, 96).translate([6.2, 17.2]))
    ay = ay + CS.square([10.0, 3.0]).translate([-6.0, 0.0])                     # tabana oturan ayak
    govde = xz_den_y_ye(ay, -3.5, 3.5, x=0.0, z=0.0)
    # kapalı (uyuyan) göz ve gülümseme: hilalin iki yüzüne 0,6 mm kazıma
    import numpy as np
    def yay_seridi(cx, cz, r, a0, a1, kal=0.8):
        dis = [(cx + (r + kal / 2) * math.cos(a), cz + (r + kal / 2) * math.sin(a)) for a in np.linspace(a0, a1, 16)]
        ic = [(cx + (r - kal / 2) * math.cos(a), cz + (r - kal / 2) * math.sin(a)) for a in np.linspace(a1, a0, 16)]
        return CS([np.asarray(dis + ic)])
    yuz = yay_seridi(-4.5, 21.0, 2.2, math.radians(200), math.radians(340)) + \
          yay_seridi(-3.0, 11.5, 3.0, math.radians(200), math.radians(320))
    for y0 in (-3.6, 2.9):
        govde = govde - xz_den_y_ye(yuz, y0, y0 + 0.7, x=0.0, z=0.0)
    return figur_taban() + govde.scale([1.5, 1.4, 1.5]).translate([0, 0, z0])      # Ø52 tabana göre büyük


# ---------------------------------------------------------------- denetim
def denetle(nfc):
    z = zarflar(nfc)
    bosluk = dondur(profil(-DUVAR, TABAN_KAL, H - DUVAR), SEG) + (
        silindir(ISIK_R[1], H - DUVAR - 0.5, H - ISIK_KAL, seg=SEG) - silindir(ISIK_R[0], H - DUVAR - 1, H, seg=SEG))  # ışık oyuğu
    fd = PARCA["kcd11"][2]
    bosluk = bosluk + silindir(fd / 2 + 0.3, anahtar_yer()[1] - 6, 80, seg=96).rotate([0, 90, 0]).translate(
        [0, 0, ANAHTAR_Z]).rotate([0, 0, ANAHTAR_ACI])   # anahtarın deliği; flanş ve tuş dışta
    yapi = {"kabuk": kabuk(), "tutucu": tutucu(nfc), "taban": taban(), "pil_kapagi": pil_kapagi(),
            "figur": (figur_taban() + figur_kapak()).translate([0, 0, Z_CANAK_TABAN])}
    sorun = []
    for ad, e in z.items():
        disari = (e - bosluk).volume()
        if disari > 1.0:
            sorun.append(f"{ad}: gövdenin dışına taşıyor ({disari:.0f} mm³)")
    adlar = list(z)
    for i in range(len(adlar)):
        for j in range(i + 1, len(adlar)):
            if {adlar[i], adlar[j]} == {"ESP32-S3", "jumper payı"}:
                continue  # pinler jumper'ların içinde
            v = (z[adlar[i]] ^ z[adlar[j]]).volume()
            if v > 0.5:
                sorun.append(f"{adlar[i]} ile {adlar[j]} çakışıyor ({v:.0f} mm³)")
    for ad, e in z.items():
        for yad, y in yapi.items():
            v = (e ^ y).volume()
            if v > 1.0:
                sorun.append(f"{ad} ile {yad} çakışıyor ({v:.0f} mm³)")
    pimler = M()
    for aci in UST_ACILAR:   # pim ile tablanın kaburgaları kasıtlı olarak sıkı geçer
        pimler = pimler + silindir(PIM_R + 0.05, 0, H, x=UST_DIREK_R * math.cos(math.radians(aci)),
                                   y=UST_DIREK_R * math.sin(math.radians(aci)), seg=32)
    ys = list(yapi)
    for i in range(len(ys)):
        for j in range(i + 1, len(ys)):
            v = ((yapi[ys[i]] ^ yapi[ys[j]]) - pimler).volume()
            if v > 0.5:
                sorun.append(f"{ys[i]} ile {ys[j]} (basılan parçalar) çakışıyor ({v:.0f} mm³)")
    # kabuk alt modülün üstüne indirilirken: alt modüldeki parçalar kabuğun ağzından geçer mi, taban kabuğa sürter mi
    gecis = silindir(GECIS_R + 0.01, -1, H, seg=SEG)
    for ad in ("hoparlör (önden)", "4xAA yatağı", "5 V düzenleyici", "MAX98357A", "ESP32-S3"):
        v = (z[ad] - gecis).volume()
        if v > 0.5:
            sorun.append(f"{ad}: kabuk takılırken alt ağza çarpar ({v:.0f} mm³)")
    for dz in (1.0, 3.0, 6.0, 10.0, 15.0, 20.0, 30.0):
        v = (yapi["taban"].translate([0, 0, -dz]) ^ yapi["kabuk"]).volume()
        if v > 0.5:
            sorun.append(f"taban {dz:.0f} mm aşağıdayken kabuğa sürtüyor ({v:.0f} mm³)")
            break
    # NFC: etiket ile anten arası
    mesafe = (Z_CANAK_TABAN + KAPAK_TABAN) - Z_OKUYUCU_UST     # etiket kapağın tabanında
    return z, yapi, sorun, mesafe


def _tm(m):
    mg = m.to_mesh()
    return trimesh.Trimesh(np.asarray(mg.vert_properties)[:, :3], np.asarray(mg.tri_verts), process=False)


def _tablaya(m):
    """Baskı tablasına: x-y ortada, en alt z = 0."""
    b = m.bounding_box()
    return m.translate([-(b[0] + b[3]) / 2, -(b[1] + b[4]) / 2, -b[2]])


BASKI = (  # (dosya, parça, baskı yönü açıklaması)
    ("1_kabuk", "kabuk", "ters: üst yüz (figür çukuru) tablada"),
    ("2_taban_plakasi", "taban", "düz alt yüz tablada"),
    ("2b_pil_kapagi", "pil_kapagi", "dış yüz (yazılı) tablada"),
    ("3_halka_nfc_tutucu", "tutucu", "ters: halkanın bastığı düz yüz tablada, raylar yukarı"),
    ("4_figur_taban", "figur", "ters: düz üst yüz tablada, dişli oyuk yukarı; figür başına 1 (adlı kapaklarla figurler/ klasöründe)"),
    ("4b_figur_kapagi", "kapak", "alt yüz tablada; Ø20 NFC etiketi içine yapışır, tabana vidalanır"),
    ("5_ayar_karti", "ayar", "alt yüz tablada, topuz yukarı; 1 adet (+ 1 kapak)"),
)


def stl_yaz(nfc, yapi):
    """Baskıya hazır STL'ler (her parça baskı yönünde, tablada) + montajlı tüm model."""
    d = os.path.join(KOK, "stl_cakil", nfc)
    os.makedirs(d, exist_ok=True)
    for eski in os.listdir(d):
        if eski.endswith(".stl"):
            os.remove(os.path.join(d, eski))
    baski = {"kabuk": yapi["kabuk"].rotate([180, 0, 0]), "taban": yapi["taban"], "pil_kapagi": yapi["pil_kapagi"],
             "tutucu": yapi["tutucu"].rotate([180, 0, 0]), "figur": figur_taban().rotate([180, 0, 0]), "kapak": figur_kapak(), "ayar": figur_taban(topuz=True)}
    for dosya, ad, _ in BASKI:
        _tm(_tablaya(baski[ad])).export(os.path.join(d, f"{dosya}.stl"))
    # tüm hali: basılan parçalar yerinde (tek dosya, ayrı gövdeler)
    tum = [yapi["kabuk"], yapi["tutucu"], yapi["taban"], yapi["pil_kapagi"], yapi["figur"]]
    trimesh.util.concatenate([_tm(m) for m in tum]).export(os.path.join(d, f"0_tum_stand_{nfc}_montajli.stl"))
    # elektronikle birlikte (yalnız bakmak için): ESP32 gerçek modeli, ötekiler kutu zarf
    z = zarflar(nfc)
    el = [_tm(m) for m in tum] + [esp_stl()]
    el += [_tm(e) for ad, e in z.items() if ad not in ("ESP32-S3", "jumper payı")]
    trimesh.util.concatenate(el).export(os.path.join(d, f"0_tum_stand_{nfc}_elektronikli_GORSEL.stl"))
    return d


if __name__ == "__main__":
    for nfc in ("rc522", "pn5180"):
        z, yapi, sorun, mesafe = denetle(nfc)
        print(f"== {nfc}: {len(sorun)} sorun; etiket-anten ≈ {mesafe:.1f} mm")
        for s in sorun:
            print("  ", s)
        if "--stl" in sys.argv:
            print("  STL:", stl_yaz(nfc, yapi))


# ---------------------------------------------------------------- önizleme
RENK_PARCA = {"hoparlör (önden)": "#555b66", "4xAA yatağı": "#2f2f33", "5 V düzenleyici": "#2d6cdf",
              "MAX98357A": "#7b3fbf", "KCD11 anahtar": "#111111", "ESP32-S3": "#1d1d1d", "jumper payı": "#e8a33d",
              "INMP441 mikrofon": "#3a7d44", "NeoPixel 16": "#ff4fa3", "RC522 okuyucu": "#1f6f3f",
              "PN5180 okuyucu": "#1f4f8f"}
RENK_YAPI = {"kabuk": "#F6E7D2", "tutucu": "#c9c2b8", "taban": "#E8DCCB", "pil_kapagi": "#d9c6ad"}


def onizle():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon as Pg
    import dis_konsept as K
    cikti = os.path.join(KOK, "onizleme")
    sonuc = {nfc: denetle(nfc) for nfc in ("rc522", "pn5180")}
    # 1) yarım kesit: kabuğun x>0 yarısı kaldırılmış, içerisi görünür
    fig = plt.figure(figsize=(17, 7.5), dpi=110)
    for i, nfc in enumerate(("rc522", "pn5180")):
        z, yapi, sorun, mesafe = sonuc[nfc]
        yarim = kutu(-80, 0, -80, 80, -5, 80)
        ls = [(yapi["kabuk"] ^ yarim, RENK_YAPI["kabuk"], False),
              (yapi["taban"], RENK_YAPI["taban"], False), (yapi["pil_kapagi"], RENK_YAPI["pil_kapagi"], False),
              (yapi["tutucu"], RENK_YAPI["tutucu"], False)]
        ls += [(e, RENK_PARCA.get(ad, "#444"), ad in ("NeoPixel 16", "jumper payı")) for ad, e in z.items()]
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        elev, azim = 18, 20
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-55, 55); ax.set_ylim(-55, 55); ax.set_zlim(-20, 75)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(f"{nfc.upper()} — iç yerleşim (sağ yarı kesik)", fontsize=14)
    fig.suptitle("Çakıl stand, iç yerleşim: altta pil kutusu (4xAA, alttan kapaklı) ve önde hoparlör; kutunun üstünde "
                 "MAX98357A, 5 V düzenleyici, ters ESP32-S3; üstte NFC okuyucu, LED halka, figür zemini", fontsize=11)
    plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0)
    fig.savefig(os.path.join(cikti, "cakil_ic_kesit3b.png")); plt.close(fig)
    # 2) üstten yerleşim planı (katlar)
    fig, axs = plt.subplots(1, 3, figsize=(19, 6.6), dpi=110)
    katlar = [("Alt kat (z 0–21): pil kutusu, hoparlör", ["hoparlör (önden)", "4xAA yatağı"]),
              ("Orta kat (z 21–46): kutunun üstü", ["ESP32-S3", "jumper payı", "MAX98357A", "5 V düzenleyici", "KCD11 anahtar"]),
              ("Üst kat (z 37–54): RC522 / PN5180", ["RC522 okuyucu", "PN5180 okuyucu", "NeoPixel 16", "INMP441 mikrofon"])]
    th = np.linspace(0, 2 * np.pi, 200)
    for ax, (baslik, adlar) in zip(axs, katlar):
        ax.plot(dis_r(ZC) * np.cos(th), dis_r(ZC) * np.sin(th), color="#8a7a66", lw=1.5)
        ax.plot(ic_r(TABAN_KAL) * np.cos(th), ic_r(TABAN_KAL) * np.sin(th), color="#c8b9a5", lw=1, ls="--")
        ax.plot(YUVA_R * np.cos(th), YUVA_R * np.sin(th), color="#e080b0", lw=1, ls=":")
        for nfc in ("rc522", "pn5180"):
            z = sonuc[nfc][0]
            for ad in adlar:
                if ad not in z or (ad.endswith("okuyucu") and not ad.lower().startswith(nfc)):
                    continue
                b = z[ad].bounding_box()
                ls = "--" if nfc == "pn5180" and ad.startswith("PN") else "-"
                if ad == "NeoPixel 16":
                    for rr in (PARCA["halka"][0] / 2, PARCA["halka"][1] / 2):
                        ax.plot(rr * np.cos(th), rr * np.sin(th), color=RENK_PARCA[ad], lw=2)
                    continue
                if ad == "INMP441 mikrofon":
                    ax.add_patch(plt.Circle(MIK_XY, PARCA["inmp441"][0] / 2, fc="#3a7d4455", ec=RENK_PARCA[ad]))
                    ax.text(MIK_XY[0], MIK_XY[1], "mik", ha="center", va="center", fontsize=8)
                    continue
                if ad == "KCD11 anahtar":
                    a = math.radians(ANAHTAR_ACI); r1, r0 = ic_r(ANAHTAR_Z), ic_r(ANAHTAR_Z) - PARCA["kcd11"][1]
                    ax.plot([r0 * math.cos(a), r1 * math.cos(a)], [r0 * math.sin(a), r1 * math.sin(a)], color="k", lw=9, alpha=.6)
                    ax.text(r0 * math.cos(a) - 3, r0 * math.sin(a) + 3, "anahtar", fontsize=8)
                    continue
                ax.add_patch(Pg([(b[0], b[1]), (b[3], b[1]), (b[3], b[4]), (b[0], b[4])], closed=True,
                                fc=RENK_PARCA.get(ad, "#888") + "55", ec=RENK_PARCA.get(ad, "#888"), lw=1.5, ls=ls))
                ax.text((b[0] + b[3]) / 2, (b[1] + b[4]) / 2, ad.replace(" (aşağı bakar)", "\n(aşağı bakar)").replace(" (rafta)", ""),
                        ha="center", va="center", fontsize=8)
            if nfc == "rc522" and adlar is katlar[0][1]:
                xk = PIL_KAPAK_XE
                yk0, yk1 = PIL_Y - PIL_IC[1] - PIL_KAPAK_KENAR, PIL_Y + PIL_IC[1] + PIL_KAPAK_KENAR
                ax.plot([-xk, xk, xk, -xk, -xk], [yk0, yk0, yk1, yk1, yk0], color="#b07a2a", lw=1.2, ls="--")
                ax.text(0, yk0 - 4, "pil kapağı (alttan)", ha="center", fontsize=8, color="#b07a2a")
        ax.text(0, dis_r(ZC) + 2, "ÖN (logo)", ha="center", fontsize=9)
        ax.text(0, -dis_r(ZC) - 6, "ARKA", ha="center", fontsize=9)
        ax.set_xlim(-66, 66); ax.set_ylim(-68, 66); ax.set_aspect("equal"); ax.grid(alpha=.25)
        ax.set_title(baslik, fontsize=12)
    axs[2].text(-64, 58, "düz çizgi: RC522 (60x40)\nkesikli: PN5180 (70x39)\nikisinde de anten figürün altında", fontsize=8)
    plt.tight_layout()
    fig.savefig(os.path.join(cikti, "cakil_ic_plan.png")); plt.close(fig)
    # 3) patlatılmış görünüş (RC522)
    z, yapi, sorun, mesafe = sonuc["rc522"]
    fig = plt.figure(figsize=(8, 14), dpi=110)
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    ls = [(yapi["kabuk"].translate([0, 0, 135]), RENK_YAPI["kabuk"], False),
          (yapi["tutucu"].translate([0, 0, 50]), RENK_YAPI["tutucu"], False),
          (z["NeoPixel 16"].translate([0, 0, 64]), RENK_PARCA["NeoPixel 16"], True),
          (z["RC522 okuyucu"].translate([0, 0, 36]), RENK_PARCA["RC522 okuyucu"], False),
          (z["ESP32-S3"].translate([0, 0, -40]), RENK_PARCA["ESP32-S3"], False),
          (yapi["taban"].translate([0, 0, -40]), RENK_YAPI["taban"], False)]
    ls.append((yapi["pil_kapagi"].translate([0, 0, -60]), RENK_YAPI["pil_kapagi"], False))
    for ad in ("hoparlör (önden)", "4xAA yatağı", "5 V düzenleyici", "MAX98357A"):
        ls.append((z[ad].translate([0, 0, -20]), RENK_PARCA[ad], False))
    elev, azim = 16, 60
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_zlim(-65, 250)
    ax.set_box_aspect((1, 1, 2.3))
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Patlatılmış görünüş (RC522): kabuk, halka, tutucu, okuyucu, alt kat (ESP32 dahil), taban", fontsize=10)
    fig.savefig(os.path.join(cikti, "cakil_ic_patlatilmis.png")); plt.close(fig)
    print("önizleme:", cikti)


if __name__ == "__main__" and "--onizle" in sys.argv:
    onizle()
