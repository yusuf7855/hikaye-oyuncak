"""Çakıl stand: dış kabuk (seçenek 3: çukurda figür yuvası, zemin kabuğun kendisi) ve iç yerleşim, iki NFC seçeneği.

    python cad/cakil_ic.py            # RC522 ve PN5180: çarpışma denetimi, önizleme PNG, STL (cad/stl_cakil/<nfc>/)

Ölçüler TAHMİN (ürün sahibi, 16 Ekim 2026: "tahminle başlayalım"); parça ölçüleri PARCA sözlüğünde, gerçekleri
ölçülünce yalnız orası değişir. Koordinat: z yukarı (z=0 taban), +y ÖN (logo), -y ARKA (USB-C, anahtar).

Yerleşim (alttan üste):
  taban plakası (vidalı, 4 ayak, hoparlör ızgarası) | hoparlör 50x50 AŞAĞI bakar (önde; ses tabandan ve ayak
  boşluğundan çıkar: 55 mm yükseklikte dik 50x50 hoparlör sığmıyor) | 18650 yatağı (ortada, x boyunca) |
  TP4056 (arka orta, USB-C arka duvarda) | MAX98357A (sağ ön) | açma-kapama (sol yan duvar) |
  ESP32-S3 (arkada, TERS: pinler yukarı, jumper'lar üstten takılır) | NFC okuyucu (anten figürün tam altında) | 16'lı halka | figür zemini (kabuk) |
  mikrofon (üstte, arkada delik).
"""
import math
import os
import sys

import numpy as np
import trimesh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import manifold3d as m3  # noqa: E402
from geometri import M, CS, kutu, silindir, dondur, xz_den_y_ye, yazi_duz, yuvarlak_dikdortgen, trimesh_e  # noqa: E402

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
FIGUR_TABAN_D = 28.0
YUVA_R = FIGUR_TABAN_D / 2 + 0.3
CUKUR_DERIN = 5.0        # figür tabanının oturduğu yüz = H - 5
# Ürün sahibi (16 Ekim 2026): ayrı yarı saydam parça yok, her şey PLA/PETG. Figürün oturduğu zemin kabuğun parçası;
# zeminin altında, LED'lerin tam üstünde halka biçimli oyuk: zemin orada ISIK_KAL kalır, beyaz PLA'dan ışık geçer.
YUVA_DUVAR = 1.2         # çukurun kabuk içine sarkan duvarı (halkanın iç boşluğundan geçer: r 15,5 < 15,9)
ZEMIN_KAL = 1.6          # figür zemini kalınlığı (altında NFC okuyucu)
ISIK_KAL = 0.6           # LED'lerin üstünde kalan zemin (0,6 mm beyaz PLA ışığı geçirir; renkli PLA'da delik açılabilir)
ISIK_YARIK = (24, 1.6)   # ürün sahibi: çukurun LED şeridine bakan DİKEY iç duvarı şerit şerit açık -> 24 dikey pencere,
                         # 1,6 mm geniş; ışık yandan çukurun içine vurur (üst yüz kapalı kalır)
ISIK_R = (16.2, 22.0)    # ışık oyuğu: LED'ler (5x5 mm, r ≈ 19) halka tavana yaslanınca bu oyuğun içine girer
CANAK_GOVDE_R = YUVA_R + YUVA_DUVAR   # çukurun dış yarıçapı (tutucu plaka da bu kadar)
YAZI, YAZI_BOY, YAZI_Z = "eco ai", 13.0, 44.5   # logo hoparlör ızgarasının üstünde

# ---------------------------------------------------------------- parçalar (TAHMİN; ölçülünce düzelt)
PARCA = {
    "hoparlor": (50.0, 22.0),
    "hoparlor_miknatis_r": 20.7,         # arkadaki mıknatıs yarıçapı (ürün sahibi: eyer yarıçapı 21 = 20,7 + 0,3 pay)            # 4 Ω 3 W YUVARLAK: Ø50, derinlik (mıknatıs dahil) tahmin
    "pil_yatagi": (77.0, 21.0, 19.0),    # 18650 tekli yatak
    "tp4056": (17.3, 28.0, 1.0),         # TP4056 Type-C HW-373 (ürün sahibinin STL'si, cad/parca_stl/): en, boy, kart
    "tp4056_usb": (9.8, 3.0, 6.9, 1.5),  # USB-C dişi: en, yükseklik, boy, kart kenarından taşma (STL'den)
    "max98357": (19.0, 18.0, 10.0),      # vida klemensi lehimliyse ~10 mm
    "esp32": (57.2, 28.5, 1.6),          # ESP32-S3 DevKit (ürün sahibinin STEP'i, cad/parca_stl/): kart en, boy, kalınlık
    "kcd11": (15.0, 20.0, 18.5, 2.0, 1.6),   # yuvarlak: panel deliği Ø, arkadaki gövde+uçlar derinliği, flanş Ø, flanş
                                             # kalınlığı, panel kalınlığı (tırnaklar ~1-2 mm panele oturur); TAHMİN, ölç
    "inmp441": (14.0, 14.0, 3.0),
    "halka": (31.75, 44.5, 1.6),         # NeoPixel 16'lı: iç Ø, dış Ø, kart kalınlığı
    "halka_led": (5.0, 1.6),             # WS2812B 5050: en, yükseklik (kartın üstünde, r ≈ 19)
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
PIL_Y = -4.0                         # pil yatağı (önce TP4056'ya, sonra arkadaki ESP32'ye yer açmak için öne alındı)
TP_X = 0.0                           # USB-C arkanın tam ortasında (gövde eğrisine en iyi oturduğu yer)
AMP_XY = (37.0, 18.5)                # sağ önde, pil ile hoparlör arasındaki köşe
ANAHTAR_ACI, ANAHTAR_Z = 155.0, 17.0 # sol yan duvar (arka ESP32'ye kaldı)
USB_Z_ALT = TABAN_KAL + 6.5          # TP4056 kartının alt yüzü: gövdenin dik kısmına çıkar ki USB-C yüzeyle hizalansın
USB_ZC = USB_Z_ALT + 1.0 + 1.5       # USB-C dişinin ekseni (kart 1,0 + dişi 3,0 / 2)
# ESP32-S3: ürün sahibi "jumper takmama uygun yer kalsın". Kart TERS takılır (bileşenler aşağı, pinler yukarı): dişi
# jumper'lar üst kabuk açıkken yukarıdan takılır. Kart arkada, TP4056'nın üstünde; uzun kenarı x boyunca, USB-C uçları -x.
ESP_XY = (0.0, -32.5)                # kartın ortası
ESP_Z = 18.0                         # bileşen yüzü (aşağı bakar); kartın arka yüzü ESP_Z + 1,6, pin uçları ESP_Z + 9,7
JUMPER_BOY = 14.0 + 4.0              # dişi jumper gövdesi (14) + kablonun bükülme payı
ESP_STL = os.path.join(KOK, "parca_stl", "esp32s3_devkit.stl")   # STEP'ten: kart x ±28,6, y ±14,25, z 0..1,6 (pinler -z)
PIL_BAG_X = 22.0                     # pil yatağını tabana sıkan iki kablo bağının yeri (x = ±22)
MIKROFON = False                     # ürün sahibi (16 Ekim 2026): mikrofon şimdilik yok (sonra eklenecek; yeri ayrılı)
MIK_XY = (0.0, -40.8)                # yuvarlak INMP441 kartı (Ø14), figür çukuru ile kabuk kenarı arasında
UST_ACILAR = (45.0, 135.0, 225.0, 315.0)    # halka/NFC tutucu direkleri
VIDA_ACILAR = (0.0, 180.0, 230.0, 330.0)    # taban vidaları (hoparlör, pil, TP4056, ESP32 arasında)
VIDA_R = 50.0
UST_DIREK_R = 41.0                   # halka/NFC tutucusunu taşıyan, kabuğun üstünden inen direkler
AYAK = (10.0, 1.0, 38.0)             # silikon ayak yuvası Ø, derinlik, yarıçap


def dis_r(z):
    u = abs(z - ZC) / B
    return R * max(0.0, 1 - u ** N) ** (1 / N)


def ic_r(z):
    return dis_r(z) - DUVAR


def profil(ofs=0.0, z0=0.0, z1=H):
    pts = [(0, z0)]
    for z in np.linspace(z0, z1, 70):
        pts.append((max(0.5, dis_r(z) + ofs), z))
    pts.append((0, z1))
    return pts


HOP_YF = _hop_on_y()                         # hoparlörün ön yüzü (y)
Z_CANAK_TABAN = H - CUKUR_DERIN              # figür tabanının oturduğu yüz
Z_HALKA_UST = H - DUVAR                      # halka kartı üst yüzün altına (tavana) yaslanır, LED'ler oyukta
Z_HALKA_ALT = Z_HALKA_UST - PARCA["halka"][2]
TUTUCU_KAL = 2.0
Z_MIK = H - DUVAR - 3.0 - 1.2                # mikrofon kartı (deliğe bakar, üstte 1,2 mm conta payı)
Z_TUTUCU_ALT = Z_HALKA_ALT - TUTUCU_KAL      # halka tutucu plakası (halkayı tavana bastırır)
Z_OKUYUCU_UST = Z_CANAK_TABAN - ZEMIN_KAL - 0.3   # NFC okuyucunun anten yüzü: çukur zemininin hemen altı


TP_STL = os.path.join(KOK, "parca_stl", "tp4056_hw373_usbc.stl")   # STL: kart x -20..8 (USB-C x-), y -5,3..12, z 0..1


def tp_stl():
    """Ürün sahibinin TP4056 STL'si standdaki yerinde (yalnız görsel; denetim kutu zarflarla)."""
    m = trimesh.load(TP_STL)
    m.apply_transform(trimesh.transformations.rotation_matrix(math.pi / 2, [0, 0, 1]))   # (x, y) -> (-y, x): USB-C y-
    b = m.bounds
    y_plaka, y_usb, y_kart = tp_konum()
    m.apply_translation([TP_X - (b[0][0] + b[1][0]) / 2, y_usb - b[0][1], USB_Z_ALT - b[0][2]])
    return m


def esp_yerine(m):
    """ESP32 STEP koordinatından (bileşenler +z, pinler -z) standdaki ters yerine: x ekseni etrafında 180°."""
    return m.rotate([180, 0, 0]).translate([ESP_XY[0], ESP_XY[1], ESP_Z + PARCA["esp32"][2]])


def esp_stl():
    """Ürün sahibinin ESP32-S3 modeli standdaki yerinde (yalnız görsel; denetim kutu zarflarla)."""
    m = trimesh.load(ESP_STL)
    m.apply_transform(trimesh.transformations.rotation_matrix(math.pi, [1, 0, 0]))
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


def tp_konum():
    """TP4056: (duvarın inceltilmiş iç yüzü y, USB-C ön yüzü y, kartın ön kenarı y).
    Ürün sahibi: USB-C dış yüzle 0'a 0, ama DIŞ GÖVDE BOZULMAZ. USB-C'nin düz ön yüzü, dört köşesinin hiçbiri eğri
    dış yüzü aşmayacak en arka yere konur (ortası yüzeyden en çok birkaç onda bir mm içeride); duvar içeriden
    inceltilir, kart kenarı bu iç yüze dayanır."""
    uw, uh, ul, ut = PARCA["tp4056_usb"]
    y_usb = max(-math.sqrt(dis_r(USB_ZC + dz) ** 2 - (TP_X + dx) ** 2)
                for dx in (-uw / 2, 0.0, uw / 2) for dz in (-uh / 2, 0.0, uh / 2)) + 0.05
    y_kart = y_usb + ut
    return y_kart - 0.1, y_usb, y_kart


def usb_cukurluk():
    """USB-C ön yüzünün ortasının dış yüzeyden içeride kaldığı mesafe (mm)."""
    return tp_konum()[1] + math.sqrt(dis_r(USB_ZC) ** 2 - TP_X ** 2)


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
    w, d, h = PARCA["pil_yatagi"]
    z["18650 yatağı"] = kutu(-w / 2, w / 2, PIL_Y - d / 2, PIL_Y + d / 2, TABAN_KAL, TABAN_KAL + h)
    w, d, t = PARCA["tp4056"]
    uw, uh, ul, ut = PARCA["tp4056_usb"]
    y_plaka, y_usb, y_kart = tp_konum()
    z["TP4056 Type-C"] = (kutu(TP_X - w / 2, TP_X + w / 2, y_kart, y_kart + d, USB_Z_ALT, USB_Z_ALT + t)
                          + kutu(TP_X - w / 2 + 1.0, TP_X + w / 2 - 1.0, y_kart + 1.0, y_kart + d - 1.0, USB_Z_ALT + t, USB_Z_ALT + t + 1.3)
                          + xz_den_y_ye(yuvarlak_dikdortgen(uw, uh, 1.3), y_usb, y_usb + ul, x=TP_X, z=USB_ZC))   # USB-C dişi (köşeleri yuvarlak)
    w, d, h = PARCA["max98357"]
    z["MAX98357A"] = kutu(AMP_XY[0] - w / 2, AMP_XY[0] + w / 2, AMP_XY[1] - d / 2, AMP_XY[1] + d / 2,
                          TABAN_KAL + 1, TABAN_KAL + 1 + h)
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
    j = None
    for s in (-1, 1):
        e = e + kutu(-27.2, 27.5, min(s * 12.2, s * 13.4), max(s * 12.2, s * 13.4), 1.6, 3.1)
        e = e + kutu(-27.7, 28.2, min(s * 11.5, s * 14.0), max(s * 11.5, s * 14.0), -2.5, 0)
        jj = kutu(-28.0, 28.3, min(s * 11.3, s * 14.3), max(s * 11.3, s * 14.3), -2.5 - JUMPER_BOY, -2.5)
        j = jj if j is None else j + jj
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
    # tutucu direkleri (üstten iner, M2,5 pilot)
    for aci in UST_ACILAR:
        x, y = UST_DIREK_R * math.cos(math.radians(aci)), UST_DIREK_R * math.sin(math.radians(aci))
        z0 = Z_TUTUCU_ALT + TUTUCU_KAL   # direk tutucu plakanın üstünde biter (plaka altından vidalanır)
        g = g + silindir(3.5, z0, H - DUVAR + 0.5, x=x, y=y, seg=32)
    for aci in UST_ACILAR:   # M2,5 sac vidası kılavuz deliği: tavanın içine 3 mm (üst yüzde 1 mm et kalır)
        x, y = UST_DIREK_R * math.cos(math.radians(aci)), UST_DIREK_R * math.sin(math.radians(aci))
        g = g - silindir(1.05, Z_TUTUCU_ALT + TUTUCU_KAL - 1, H - 1.0, x=x, y=y, seg=24)
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
    # arka: USB-C (fiş gövdesi için 12,5 x 7,5) ve anahtar (Ø15)
    # USB-C 0'a 0 (dış gövde aynen kalır; deliğin çevresi kapalı, dışta yalnız USB-C deliği görünür): içte duvar
    # inceltilir; kart kabuğa bağlı iki yan kızağa içeriden kayarak takılır (USB-C deliğe girer), taban plakası kapanınca
    # altındaki kaide ve arkadaki dayanak kartı yerinde kilitler
    y_ic, y_usb, y_kart = tp_konum()
    uw, uh, ul, ut = PARCA["tp4056_usb"]
    w_k, d_k, t_k = PARCA["tp4056"]
    g = g - kutu(TP_X - w_k / 2 - 0.6, TP_X + w_k / 2 + 0.6, y_ic, y_usb + 9, USB_Z_ALT - 0.6, USB_ZC + uh / 2 + 1.2)   # iç cep
    g = g - xz_den_y_ye(yuvarlak_dikdortgen(uw + 0.3, uh + 0.3, 1.5), -80, y_usb + 9, x=TP_X, z=USB_ZC)
    x0, x1, zu = TP_X - w_k / 2, TP_X + w_k / 2, USB_Z_ALT + t_k
    kz = None
    for s, xk in ((-1, x0), (1, x1)):
        dis_x, ic_x = xk + s * 1.6, xk - s * 0.8     # kızak duvarı kartın 0,15 mm dışında; dudaklar kart kenarına 0,8 mm biner
        f = kutu(min(xk + s * 0.15, dis_x), max(xk + s * 0.15, dis_x), y_ic - 4, y_kart + 14, USB_Z_ALT - 1.4, zu + 1.4)
        f = f + kutu(min(dis_x, ic_x), max(dis_x, ic_x), y_ic - 4, y_kart + 14, USB_Z_ALT - 1.4, USB_Z_ALT - 0.15)   # alt dudak
        f = f + kutu(min(dis_x, ic_x), max(dis_x, ic_x), y_ic - 4, y_kart + 14, zu + 0.15, zu + 1.4)                 # üst dudak
        kz = f if kz is None else kz + f
    g = g + (kz ^ dondur(profil(-0.5), SEG))
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
        p = p + kol + silindir(4.0, zt - 1.5, zt + TUTUCU_KAL, x=x, y=y, seg=32)   # vida tablası 3,5 mm (M2,5 x 6)
        p = p - silindir(1.4, zt - 3, zt + 5, x=x, y=y, seg=24)
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
    return p


TABAN_OZ = ("vida", "ayak", "pil", "hoparlor", "tp4056", "esp32", "amfi")


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
        eyer = kutu(-18, 18, yf - hdr + 3, yf - hdr + 7, TABAN_KAL - 0.01, HOP_ZC - 9)
        t = t + (eyer - silindir(PARCA["hoparlor_miknatis_r"] + 0.3, -5, 80, seg=96).rotate([-90, 0, 0]).translate([0, -10, HOP_ZC]))
        for x in (-hd / 2 - 1.5, hd / 2 - 1.0):
            t = t - kutu(x, x + 2.5, yf - 10, yf - 6, -1, TABAN_KAL + 1)
    # pil yatağı cebi (1,5 mm duvar, 3 mm yüksek) + iki kablo bağı yarığı (yatak cırt/kablo bağıyla tabana sıkılır)
    w, d, h = PARCA["pil_yatagi"]
    if "pil" in oz:
        t = t + (kutu(-w / 2 - 1.5, w / 2 + 1.5, PIL_Y - d / 2 - 1.5, PIL_Y + d / 2 + 1.5, TABAN_KAL, TABAN_KAL + 3)
                 - kutu(-w / 2 - 0.3, w / 2 + 0.3, PIL_Y - d / 2 - 0.3, PIL_Y + d / 2 + 0.3, TABAN_KAL - 1, TABAN_KAL + 4))
        for x in (-PIL_BAG_X, PIL_BAG_X):
            for y in (PIL_Y - d / 2 - 2.0, PIL_Y + d / 2 + 0.6):
                t = t - kutu(x - 2.0, x + 2.0, y, y + 2.6, -1, TABAN_KAL + 4)
    # TP4056: kart kabuktaki kızaklarda durur; tabanda altında kaide (kartı kızağın ortasında tutar) ve arkada dayanak
    # (fiş takılırken kart içeri kaçmaz)
    w, d, tk = PARCA["tp4056"]
    y_plaka, y_usb, y_kart = tp_konum()
    x0, x1, y0, y1 = TP_X - w / 2, TP_X + w / 2, y_kart, y_kart + d
    zu = USB_Z_ALT + tk
    tp = kutu(x0 + 1.2, x1 - 1.2, y0 - 3, y1 - 3, TABAN_KAL - 0.01, USB_Z_ALT)
    tp = tp + kutu(x0 + 1, x1 - 1, y1 + 0.2, y1 + 1.6, TABAN_KAL - 0.01, zu + 1.0)
    if "tp4056" in oz:
        t = t + tp
    w, d, h = PARCA["max98357"]
    if "amfi" in oz:
        t = t + (kutu(AMP_XY[0] - w / 2 - 1.2, AMP_XY[0] + w / 2 + 1.2, AMP_XY[1] - d / 2 - 1.2, AMP_XY[1] + d / 2 + 1.2, TABAN_KAL, TABAN_KAL + 2.5)
                 - kutu(AMP_XY[0] - w / 2 - 0.2, AMP_XY[0] + w / 2 + 0.2, AMP_XY[1] - d / 2 - 0.2, AMP_XY[1] + d / 2 + 0.2, TABAN_KAL - 1, TABAN_KAL + 4))
    # ESP32 yuvası (ters kart): iki uzun kenarda kanal (iç kiriş kartı pin sıralarının hemen içinden taşır, dış duvar
    # yandan tutar; aradaki boşluk pin lehimlerine), USB-C ucunda iki köşe kancası (kart altına kayar), anten ucunda
    # esnek tırnak (bastırınca kartın modül ucuna oturur) ve modül ucunun altında destek
    if "esp32" in oz:
        xc, yc, ze = ESP_XY[0], ESP_XY[1], ESP_Z
        za = ze + PARCA["esp32"][2]
        def yb(a, b, s):
            return min(yc + s * a, yc + s * b), max(yc + s * a, yc + s * b)
        for s in (-1, 1):
            parcalar = ((-28.5, 28.5),) if s > 0 else ((-28.5, -11.5), (11.5, 28.5))   # arka kanalın altından TP4056 geçer
            for xa, xb in parcalar:
                t = t + kutu(xc + xa, xc + xb, *yb(10.7, 15.4, s), TABAN_KAL - 0.01, ze - 1.8)
            if s < 0:
                t = t + kutu(xc - 11.6, xc + 11.6, *yb(10.7, 15.4, s), 13.5, ze - 1.8)        # TP4056'nın üstünden köprü
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
    # ayak yuvaları
    for aci in ((90.0, 210.0, 330.0) if "ayak" in oz else ()):
        x, y = AYAK[2] * math.cos(math.radians(aci)), AYAK[2] * math.sin(math.radians(aci))
        t = t - silindir(AYAK[0] / 2 + 0.2, -1, AYAK[1], x=x, y=y, seg=32)
    for x, y in (((0, -42), (-44, 14), (44, 14)) if "ayak" in oz else ()):
        t = t - silindir(AYAK[0] / 2 + 0.2, -1, AYAK[1], x=x, y=y, seg=32)
    ic = dondur(profil(-DUVAR - 0.3, 1.0, H - DUVAR), SEG)
    t = (t ^ kutu(-70, 70, -70, 70, -1, 1.2)) + (t ^ ic)
    return t


def figur_taban(topuz=False):
    """Figür tabanı (jeton) Ø28: figür üstüne yapıştırılır; altta NTAG213 Ø25 etiket cebi (etiket çukur zeminine değer).
    topuz=True: ayar kartı (üstte tutma topuzu)."""
    r, h = FIGUR_TABAN_D / 2, CUKUR_DERIN
    b = dondur([(0, 0), (r - 0.3, 0), (r, 0.3), (r, h - 1.0), (r - 1.0, h), (0, h)], SEG)
    b = b - silindir(12.8, -1, 0.4, seg=SEG)                       # etiket cebi (alt yüz, 0,4 mm)
    if topuz:
        b = b + dondur([(0, h - 0.5), (10.0, h - 0.5), (10.0, h + 9.0), (8.5, h + 11.0), (6.0, h + 12.0), (0, h + 12.0)], SEG)
    return b


# ---------------------------------------------------------------- denetim
def denetle(nfc):
    z = zarflar(nfc)
    bosluk = dondur(profil(-DUVAR, TABAN_KAL, H - DUVAR), SEG) + (
        silindir(ISIK_R[1], H - DUVAR - 0.5, H - ISIK_KAL, seg=SEG) - silindir(ISIK_R[0], H - DUVAR - 1, H, seg=SEG)) + (
        kutu(TP_X - 6, TP_X + 6, tp_konum()[1] - 0.01, tp_konum()[2] + 1, USB_Z_ALT, USB_ZC + 2)) + (
        kutu(TP_X - PARCA["tp4056"][0] / 2 - 0.6, TP_X + PARCA["tp4056"][0] / 2 + 0.6, tp_konum()[0], tp_konum()[1] + 9,
             TABAN_KAL, USB_ZC + 3))  # ışık oyuğu, USB-C deliği ve duvardaki kart cebi
    fd = PARCA["kcd11"][2]
    bosluk = bosluk + silindir(fd / 2 + 0.3, anahtar_yer()[1] - 6, 80, seg=96).rotate([0, 90, 0]).translate(
        [0, 0, ANAHTAR_Z]).rotate([0, 0, ANAHTAR_ACI])   # anahtarın deliği; flanş ve tuş dışta
    yapi = {"kabuk": kabuk(), "tutucu": tutucu(nfc), "taban": taban(), "figur": figur_taban().translate([0, 0, Z_CANAK_TABAN])}
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
    ys = list(yapi)
    for i in range(len(ys)):
        for j in range(i + 1, len(ys)):
            v = (yapi[ys[i]] ^ yapi[ys[j]]).volume()
            if v > 0.5:
                sorun.append(f"{ys[i]} ile {ys[j]} (basılan parçalar) çakışıyor ({v:.0f} mm³)")
    # NFC: etiket ile anten arası
    mesafe = (Z_CANAK_TABAN + 0.4) - Z_OKUYUCU_UST
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
    ("3_halka_nfc_tutucu", "tutucu", "ters: halkanın bastığı düz yüz tablada, raylar yukarı"),
    ("4_figur_taban", "figur", "ters: düz üst yüz tablada, etiket cebi yukarı; 11 figür için 11 adet"),
    ("5_ayar_karti", "ayar", "alt yüz tablada, topuz yukarı (kenar/brim önerilir); 1 adet"),
)


def stl_yaz(nfc, yapi):
    """Baskıya hazır STL'ler (her parça baskı yönünde, tablada) + montajlı tüm model."""
    d = os.path.join(KOK, "stl_cakil", nfc)
    os.makedirs(d, exist_ok=True)
    for eski in os.listdir(d):
        if eski.endswith(".stl"):
            os.remove(os.path.join(d, eski))
    baski = {"kabuk": yapi["kabuk"].rotate([180, 0, 0]), "taban": yapi["taban"],
             "tutucu": yapi["tutucu"].rotate([180, 0, 0]), "figur": figur_taban().rotate([180, 0, 0]), "ayar": figur_taban(topuz=True)}
    for dosya, ad, _ in BASKI:
        _tm(_tablaya(baski[ad])).export(os.path.join(d, f"{dosya}.stl"))
    # tüm hali: basılan parçalar yerinde (tek dosya, ayrı gövdeler)
    tum = [yapi["kabuk"], yapi["tutucu"], yapi["taban"], yapi["figur"]]
    trimesh.util.concatenate([_tm(m) for m in tum]).export(os.path.join(d, f"0_tum_stand_{nfc}_montajli.stl"))
    # elektronikle birlikte (yalnız bakmak için): ESP32 ve TP4056 gerçek modelleri, ötekiler kutu zarf
    z = zarflar(nfc)
    el = [_tm(m) for m in tum] + [tp_stl(), esp_stl()]
    el += [_tm(e) for ad, e in z.items() if ad not in ("TP4056 Type-C", "ESP32-S3", "jumper payı")]
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
RENK_PARCA = {"hoparlör (önden)": "#555b66", "18650 yatağı": "#2f2f33", "TP4056 Type-C": "#2d6cdf",
              "MAX98357A": "#7b3fbf", "KCD11 anahtar": "#111111", "ESP32-S3": "#1d1d1d", "jumper payı": "#e8a33d",
              "INMP441 mikrofon": "#3a7d44", "NeoPixel 16": "#ff4fa3", "RC522 okuyucu": "#1f6f3f",
              "PN5180 okuyucu": "#1f4f8f"}
RENK_YAPI = {"kabuk": "#F6E7D2", "tutucu": "#c9c2b8", "taban": "#E8DCCB"}


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
              (yapi["taban"], RENK_YAPI["taban"], False),
              (yapi["tutucu"], RENK_YAPI["tutucu"], False)]
        ls += [(e, RENK_PARCA.get(ad, "#444"), ad in ("NeoPixel 16", "jumper payı")) for ad, e in z.items()]
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        elev, azim = 18, 20
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-55, 55); ax.set_ylim(-55, 55); ax.set_zlim(-20, 75)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(f"{nfc.upper()} — iç yerleşim (sağ yarı kesik)", fontsize=14)
    fig.suptitle("Çakıl stand, iç yerleşim: alt katta hoparlör (önden), 18650, TP4056, MAX98357A; arkada ters ESP32-S3; "
                 "üstte NFC okuyucu, 16'lı halka, figür zemini (ışık oyuğu)", fontsize=11)
    plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0)
    fig.savefig(os.path.join(cikti, "cakil_ic_kesit3b.png")); plt.close(fig)
    # 2) üstten yerleşim planı (katlar)
    fig, axs = plt.subplots(1, 3, figsize=(19, 6.6), dpi=110)
    katlar = [("Alt kat (taban plakası, z 2–22)", ["hoparlör (önden)", "18650 yatağı", "TP4056 Type-C", "MAX98357A", "KCD11 anahtar"]),
              ("Orta kat (z 15–40): ters ESP32-S3 + jumper payı", ["ESP32-S3", "jumper payı", "18650 yatağı"]),
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
                ax.annotate("USB-C", (TP_X, -dis_r(6)), (TP_X + 6, -dis_r(6) - 4), fontsize=8, arrowprops=dict(arrowstyle="->"))
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
    for ad in ("hoparlör (önden)", "18650 yatağı", "TP4056 Type-C", "MAX98357A"):
        ls.append((z[ad].translate([0, 0, -20]), RENK_PARCA[ad], False))
    elev, azim = 16, 60
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_zlim(-45, 250)
    ax.set_box_aspect((1, 1, 2.3))
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Patlatılmış görünüş (RC522): kabuk, halka, tutucu, okuyucu, alt kat (ESP32 dahil), taban", fontsize=10)
    fig.savefig(os.path.join(cikti, "cakil_ic_patlatilmis.png")); plt.close(fig)
    print("önizleme:", cikti)


if __name__ == "__main__" and "--onizle" in sys.argv:
    onizle()
