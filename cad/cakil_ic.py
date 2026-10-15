"""Çakıl stand: dış kabuk (seçenek 3: çukurda figür yuvası, zemin kabuğun kendisi) ve iç yerleşim, iki NFC seçeneği.

    python cad/cakil_ic.py            # RC522 ve PN5180: çarpışma denetimi, önizleme PNG, STL (cad/stl_cakil/<nfc>/)

Ölçüler TAHMİN (ürün sahibi, 16 Ekim 2026: "tahminle başlayalım"); parça ölçüleri PARCA sözlüğünde, gerçekleri
ölçülünce yalnız orası değişir. Koordinat: z yukarı (z=0 taban), +y ÖN (logo), -y ARKA (USB-C, anahtar).

Yerleşim (alttan üste):
  taban plakası (vidalı, 4 ayak, hoparlör ızgarası) | hoparlör 50x50 AŞAĞI bakar (önde; ses tabandan ve ayak
  boşluğundan çıkar: 55 mm yükseklikte dik 50x50 hoparlör sığmıyor) | 18650 yatağı (ortada, x boyunca) |
  TP4056 (arka orta, USB-C arka duvarda) | MAX98357A (arka sağ) | açma-kapama (arka sol duvar) |
  ESP32-S3 rafı (pilin üstünde) | NFC okuyucu (anten figürün tam altında) | 16'lı halka | figür zemini (kabuk) |
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
ISIK_R = (16.2, 22.0)    # ışık oyuğu: LED'ler (5x5 mm, r ≈ 19) halka tavana yaslanınca bu oyuğun içine girer
CANAK_GOVDE_R = YUVA_R + YUVA_DUVAR   # çukurun dış yarıçapı (tutucu plaka da bu kadar)
YAZI, YAZI_BOY, YAZI_Z = "eco ai", 15.0, 37.0

# ---------------------------------------------------------------- parçalar (TAHMİN; ölçülünce düzelt)
PARCA = {
    "hoparlor": (50.0, 50.0, 20.0),      # 4 Ω 3 W, 50x50, derinlik tahmin
    "pil_yatagi": (77.0, 21.0, 19.0),    # 18650 tekli yatak
    "tp4056": (17.0, 26.0, 1.6),         # Type-C, korumalı; USB-C 9 x 3,2 (y- ucunda)
    "max98357": (19.0, 18.0, 10.0),      # vida klemensi lehimliyse ~10 mm
    "esp32": (69.0, 25.5, 9.0),          # DevKitC-1 N16R8 (başlıksız: alt + üst bileşenler)
    "kcd11": (15.0, 20.0),               # Ø15 panel deliği, arkada ~20 mm derinlik
    "inmp441": (14.0, 14.0, 3.0),
    "halka": (31.75, 44.5, 1.6),         # NeoPixel 16'lı: iç Ø, dış Ø, kart kalınlığı
    "halka_led": (5.0, 1.6),             # WS2812B 5050: en, yükseklik (kartın üstünde, r ≈ 19)
    "rc522": (60.0, 40.0, 1.6, 3.0),     # en, boy, PCB, alt bileşen yüksekliği
    "pn5180": (70.0, 39.0, 1.6, 3.0),
}
# NFC antenin kart üzerindeki merkezi (kart merkezine göre x, y): figürün tam altına getirilir
ANTEN_KAYMA = {"rc522": (0.0, 4.0),     # RC522: başlık (pin) kenarı arkada, anten öne kaymış (tahmin)
               "pn5180": (10.0, 0.0)}   # PN5180: anten kartın bir ucunda (~39x39; merkezi kart merkezinden ~15 mm);
                                        # kabuğun eğrisine sığsın diye 10 mm kaydırıldı: anten merkezi figürden 5 mm yanda

# ---------------------------------------------------------------- yerleşim (merkez x, y; alt z)
HOP_Y = 23.0
PIL_Y = -15.0
TP_X = -4.0
AMP_XY = (17.0, -36.0)
ANAHTAR_ACI, ANAHTAR_Z = 250.0, 17.0
USB_Z_ALT = TABAN_KAL + 1.0          # TP4056 1 mm destek üstünde
RAF_Z = 22.8                         # ESP32 rafı (hoparlörün üstü 22,4, pil yatağının 21,4)
RAF_KAL = 1.6
RAF_BACAK_X = 42.5                   # raf bacakları pil yatağının (x ±38,5) dışında
MIK_XY = (0.0, -40.8)                # yuvarlak INMP441 kartı (Ø14), figür çukuru ile kabuk kenarı arasında
UST_ACILAR = (45.0, 135.0, 225.0, 315.0)    # halka/NFC tutucu direkleri
VIDA_ACILAR = (0.0, 180.0, 230.0, 315.0)    # taban vidaları (hoparlör, pil, TP4056, anahtar arasında)
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


Z_CANAK_TABAN = H - CUKUR_DERIN              # figür tabanının oturduğu yüz
Z_HALKA_UST = H - DUVAR                      # halka kartı üst yüzün altına (tavana) yaslanır, LED'ler oyukta
Z_HALKA_ALT = Z_HALKA_UST - PARCA["halka"][2]
TUTUCU_KAL = 2.0
Z_MIK = H - DUVAR - 3.0 - 1.2                # mikrofon kartı (deliğe bakar, üstte 1,2 mm conta payı)
Z_TUTUCU_ALT = Z_HALKA_ALT - TUTUCU_KAL      # halka tutucu plakası (halkayı tavana bastırır)
Z_OKUYUCU_UST = Z_CANAK_TABAN - ZEMIN_KAL - 0.3   # NFC okuyucunun anten yüzü: çukur zemininin hemen altı


def gorunmez():
    return M()


# ---------------------------------------------------------------- zarflar (çarpışma denetimi için)
def zarflar(nfc):
    z = {}
    w, d, h = PARCA["hoparlor"]
    z["hoparlör (aşağı bakar)"] = kutu(-w / 2, w / 2, HOP_Y - d / 2, HOP_Y + d / 2, TABAN_KAL, TABAN_KAL + h)
    w, d, h = PARCA["pil_yatagi"]
    z["18650 yatağı"] = kutu(-w / 2, w / 2, PIL_Y - d / 2, PIL_Y + d / 2, TABAN_KAL, TABAN_KAL + h)
    w, d, t = PARCA["tp4056"]
    y_uc = -(math.sqrt(max(0.0, ic_r(USB_Z_ALT) ** 2 - (abs(TP_X) + w / 2) ** 2))) + 0.6
    z["TP4056 Type-C"] = kutu(TP_X - w / 2, TP_X + w / 2, y_uc, y_uc + d, USB_Z_ALT, USB_Z_ALT + t + 3.4)
    w, d, h = PARCA["max98357"]
    z["MAX98357A"] = kutu(AMP_XY[0] - w / 2, AMP_XY[0] + w / 2, AMP_XY[1] - d / 2, AMP_XY[1] + d / 2,
                          TABAN_KAL + 1, TABAN_KAL + 1 + h)
    dd, derin = PARCA["kcd11"]
    a = math.radians(ANAHTAR_ACI)
    r_duvar = ic_r(ANAHTAR_Z)
    k = silindir(dd / 2 - 0.5, 0, derin, seg=48).rotate([0, 90, 0])   # +x boyunca
    k = k.translate([r_duvar - derin, 0, ANAHTAR_Z]).rotate([0, 0, ANAHTAR_ACI])
    z["KCD11 anahtar"] = k
    w, d, h = PARCA["esp32"]
    z["ESP32-S3 (rafta)"] = kutu(-w / 2, w / 2, PIL_Y - d / 2, PIL_Y + d / 2, RAF_Z + RAF_KAL, RAF_Z + RAF_KAL + h)
    w, d, h = PARCA["inmp441"]
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
    g = g - (silindir(YUVA_R + 0.8, H - 0.8, H + 0.01, seg=SEG, r2=YUVA_R + 1.6) - silindir(0.1, H - 2, H + 2, seg=8))  # ağız pahı
    # tutucu direkleri (üstten iner, M2,5 pilot)
    for aci in UST_ACILAR:
        x, y = UST_DIREK_R * math.cos(math.radians(aci)), UST_DIREK_R * math.sin(math.radians(aci))
        g = g + (silindir(3.5, Z_TUTUCU_ALT, H - DUVAR + 0.5, x=x, y=y, seg=32) - silindir(1.05, Z_TUTUCU_ALT - 1, Z_TUTUCU_ALT + 7, x=x, y=y, seg=24))
    # taban vida kolonları (duvara yapışık, alttan M3 ısıl gömme somun)
    for aci in VIDA_ACILAR:
        x, y = VIDA_R * math.cos(math.radians(aci)), VIDA_R * math.sin(math.radians(aci))
        kol = silindir(4.5, TABAN_KAL, 14.0, x=x, y=y, seg=32) + kutu(-2.2, 2.2, 0, 8, TABAN_KAL, 14.0).rotate([0, 0, aci - 90]).translate([x, y, 0])
        g = g + ((kol ^ dondur(profil(-0.5), SEG)) - silindir(2.0, TABAN_KAL - 1, TABAN_KAL + 6.5, x=x, y=y, seg=24))
    # arka: USB-C (fiş gövdesi için 12,5 x 7,5) ve anahtar (Ø15)
    usb_z = USB_Z_ALT + PARCA["tp4056"][2] + 1.6
    g = g - xz_den_y_ye(yuvarlak_dikdortgen(12.5, 7.5, 3.0), -70, -40, x=TP_X, z=usb_z)
    a = ANAHTAR_ACI
    g = g - silindir(PARCA["kcd11"][0] / 2 + 0.1, 0, 30, seg=48).rotate([0, 90, 0]).translate([45, 0, ANAHTAR_Z]).rotate([0, 0, a])
    # mikrofon deliği ve cebi
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
        p = p + kol + silindir(4.0, zt, zt + TUTUCU_KAL, x=x, y=y, seg=32)
        p = p - silindir(1.4, zt - 1, zt + 5, x=x, y=y, seg=24)
    p = p - silindir(CANAK_GOVDE_R + 0.4, zt - 1, zt + 5, seg=SEG)            # çukur geçer
    # halka bileziği (ortalar) ve kablo çentiği (arkada)
    p = p + (silindir(rd / 2 + 1.7, zt + TUTUCU_KAL, zt + TUTUCU_KAL + 1.5, seg=96) - silindir(rd / 2 + 0.3, zt, zt + 9, seg=96))
    p = p - kutu(-3, 3, -rd / 2 - 3, -rd / 2 + 2, zt + TUTUCU_KAL - 0.01, zt + TUTUCU_KAL + 2)
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


def taban():
    r = ic_r(1.0) + 0.4
    t = silindir(r, 0, 1.2, seg=SEG) + silindir(ic_r(TABAN_KAL) - 0.3, 1.2, TABAN_KAL, seg=SEG)
    # vida delikleri (M3 havşa)
    for aci in VIDA_ACILAR:
        x, y = VIDA_R * math.cos(math.radians(aci)), VIDA_R * math.sin(math.radians(aci))
        t = t - silindir(1.7, -1, 5, x=x, y=y, seg=24) - silindir(3.3, -1, 0.0, x=x, y=y, seg=24, r2=1.7).translate([0, 0, 1.6])
    # hoparlör ızgarası (yıldızlar) ve köşe tutucular
    for i in range(-3, 4):
        for j in range(-3, 4):
            x, y = i * 6.0, HOP_Y + j * 6.0 + (3.0 if i % 2 else 0.0)
            if x * x + (y - HOP_Y) ** 2 < 19.5 ** 2:
                t = t - silindir(1.4, -1, 5, x=x, y=y, seg=16)
    w, d, h = PARCA["hoparlor"]
    for sx in (-1, 1):
        for sy in (-1, 1):
            x0, y0 = sx * (w / 2 + 0.3), HOP_Y + sy * (d / 2 + 0.3)
            l = kutu(min(x0, x0 + sx * 2), max(x0, x0 + sx * 2), min(y0 - sy * 6, y0 + sy * 2), max(y0 - sy * 6, y0 + sy * 2), TABAN_KAL, TABAN_KAL + 6)
            l = l + kutu(min(x0 - sx * 6, x0 + sx * 2), max(x0 - sx * 6, x0 + sx * 2), min(y0, y0 + sy * 2), max(y0, y0 + sy * 2), TABAN_KAL, TABAN_KAL + 6)
            t = t + l
    # pil yatağı cebi (1,5 mm duvar), TP4056 kızağı, amfi tablası
    w, d, h = PARCA["pil_yatagi"]
    t = t + (kutu(-w / 2 - 1.5, w / 2 + 1.5, PIL_Y - d / 2 - 1.5, PIL_Y + d / 2 + 1.5, TABAN_KAL, TABAN_KAL + 3)
             - kutu(-w / 2 - 0.3, w / 2 + 0.3, PIL_Y - d / 2 - 0.3, PIL_Y + d / 2 + 0.3, TABAN_KAL - 1, TABAN_KAL + 4))
    zf = zarflar("rc522")
    b = zf["TP4056 Type-C"].bounding_box()
    t = t + kutu(b[0] - 1.6, b[0] - 0.2, b[1] + 4, b[4] - 2, TABAN_KAL, USB_Z_ALT + 2.4)
    t = t + kutu(b[3] + 0.2, b[3] + 1.6, b[1] + 4, b[4] - 2, TABAN_KAL, USB_Z_ALT + 2.4)
    # iç uçta ayrı dayanak yok: pil yatağı cebinin arka duvarı dayanak (fiş takılırken kart içeri itilir)
    t = t + kutu(b[0] + 3, b[3] - 3, b[1] + 6, b[4] - 4, TABAN_KAL, USB_Z_ALT)
    w, d, h = PARCA["max98357"]
    t = t + (kutu(AMP_XY[0] - w / 2 - 1.2, AMP_XY[0] + w / 2 + 1.2, AMP_XY[1] - d / 2 - 1.2, AMP_XY[1] + d / 2 + 1.2, TABAN_KAL, TABAN_KAL + 2.5)
             - kutu(AMP_XY[0] - w / 2 - 0.2, AMP_XY[0] + w / 2 + 0.2, AMP_XY[1] - d / 2 - 0.2, AMP_XY[1] + d / 2 + 0.2, TABAN_KAL - 1, TABAN_KAL + 4))
    # ESP32 rafının bacakları (pil yatağının iki ucunda)
    w, d, h = PARCA["esp32"]
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = sx * RAF_BACAK_X, PIL_Y + sy * (d / 2 - 1)
            t = t + silindir(2.6, TABAN_KAL, RAF_Z, x=x, y=y, seg=24) - silindir(1.05, RAF_Z - 6, RAF_Z + 1, x=x, y=y, seg=16)
    # ayak yuvaları
    for aci in (90.0, 210.0, 330.0):
        x, y = AYAK[2] * math.cos(math.radians(aci)), AYAK[2] * math.sin(math.radians(aci))
        if abs(x) < 26 and abs(y - HOP_Y) < 26:
            continue
        t = t - silindir(AYAK[0] / 2 + 0.2, -1, AYAK[1], x=x, y=y, seg=32)
    for x, y in ((0, -42), (-44, 14), (44, 14)):
        t = t - silindir(AYAK[0] / 2 + 0.2, -1, AYAK[1], x=x, y=y, seg=32)
    ic = dondur(profil(-DUVAR - 0.3, 1.0, H - DUVAR), SEG)
    return (t ^ kutu(-70, 70, -70, 70, -1, 1.2)) + (t ^ ic)


def raf():
    w, d, h = PARCA["esp32"]
    r = kutu(-RAF_BACAK_X - 3.5, RAF_BACAK_X + 3.5, PIL_Y - d / 2 - 1.5, PIL_Y + d / 2 + 1.5, RAF_Z, RAF_Z + RAF_KAL)
    r = r + (kutu(-w / 2 - 1.2, w / 2 + 1.2, PIL_Y - d / 2 - 1.2, PIL_Y + d / 2 + 1.2, RAF_Z + RAF_KAL, RAF_Z + RAF_KAL + 2.0)
             - kutu(-w / 2 - 0.2, w / 2 + 0.2, PIL_Y - d / 2 - 0.2, PIL_Y + d / 2 + 0.2, RAF_Z, RAF_Z + 5))
    r = r - kutu(w / 2 - 6, w / 2 + 3, PIL_Y - 5, PIL_Y + 5, RAF_Z + RAF_KAL - 0.01, RAF_Z + 6)   # USB-C ucu açık
    r = r - kutu(-20, 20, PIL_Y - 6, PIL_Y + 6, RAF_Z - 1, RAF_Z + 3)                             # kablo geçişi
    for sx in (-1, 1):
        for sy in (-1, 1):
            r = r - silindir(1.4, RAF_Z - 1, RAF_Z + 3, x=sx * RAF_BACAK_X, y=PIL_Y + sy * (d / 2 - 1), seg=16)
    return r


# ---------------------------------------------------------------- denetim
def denetle(nfc):
    z = zarflar(nfc)
    bosluk = dondur(profil(-DUVAR, TABAN_KAL, H - DUVAR), SEG) + (
        silindir(ISIK_R[1], H - DUVAR - 0.5, H - ISIK_KAL, seg=SEG) - silindir(ISIK_R[0], H - DUVAR - 1, H, seg=SEG))  # ışık oyuğu
    yapi = {"kabuk": kabuk(), "tutucu": tutucu(nfc), "taban": taban(), "raf": raf()}
    sorun = []
    for ad, e in z.items():
        if ad == "KCD11 anahtar":
            continue  # kabuğun duvarından geçer
        disari = (e - bosluk).volume()
        if disari > 1.0:
            sorun.append(f"{ad}: gövdenin dışına taşıyor ({disari:.0f} mm³)")
    adlar = list(z)
    for i in range(len(adlar)):
        for j in range(i + 1, len(adlar)):
            v = (z[adlar[i]] ^ z[adlar[j]]).volume()
            if v > 0.5:
                sorun.append(f"{adlar[i]} ile {adlar[j]} çakışıyor ({v:.0f} mm³)")
    for ad, e in z.items():
        for yad, y in yapi.items():
            if ad == "KCD11 anahtar" and yad == "kabuk":
                continue
            v = (e ^ y).volume()
            if v > 1.0:
                sorun.append(f"{ad} ile {yad} çakışıyor ({v:.0f} mm³)")
    # NFC: etiket ile anten arası
    mesafe = (Z_CANAK_TABAN + 0.4) - Z_OKUYUCU_UST
    return z, yapi, sorun, mesafe


def stl_yaz(nfc, yapi):
    d = os.path.join(KOK, "stl_cakil", nfc)
    os.makedirs(d, exist_ok=True)
    for ad, m in (("kabuk", yapi["kabuk"].rotate([180, 0, 0])),
                  ("halka_nfc_tutucu", yapi["tutucu"]), ("taban_plakasi", yapi["taban"]), ("esp32_rafi", yapi["raf"])):
        dosya = os.path.join(d, f"{ad}.stl".replace("ı", "i"))
        mg = m.to_mesh()
        trimesh.Trimesh(np.asarray(mg.vert_properties)[:, :3], np.asarray(mg.tri_verts), process=False).export(dosya)
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
RENK_PARCA = {"hoparlör (aşağı bakar)": "#555b66", "18650 yatağı": "#2f2f33", "TP4056 Type-C": "#2d6cdf",
              "MAX98357A": "#7b3fbf", "KCD11 anahtar": "#111111", "ESP32-S3 (rafta)": "#1d1d1d",
              "INMP441 mikrofon": "#3a7d44", "NeoPixel 16": "#ff4fa3", "RC522 okuyucu": "#1f6f3f",
              "PN5180 okuyucu": "#1f4f8f"}
RENK_YAPI = {"kabuk": "#F6E7D2", "tutucu": "#c9c2b8", "taban": "#E8DCCB", "raf": "#c9c2b8"}


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
              (yapi["taban"], RENK_YAPI["taban"], False), (yapi["raf"], RENK_YAPI["raf"], False),
              (yapi["tutucu"], RENK_YAPI["tutucu"], False)]
        ls += [(e, RENK_PARCA.get(ad, "#444"), ad == "NeoPixel 16") for ad, e in z.items()]
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        elev, azim = 18, 20
        e, a = math.radians(elev), math.radians(azim)
        K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
        ax.set_xlim(-55, 55); ax.set_ylim(-55, 55); ax.set_zlim(-20, 75)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(f"{nfc.upper()} — iç yerleşim (sağ yarı kesik)", fontsize=14)
    fig.suptitle("Çakıl stand, iç yerleşim: alt katta hoparlör (aşağı bakar), 18650, TP4056, MAX98357A; rafta ESP32-S3; "
                 "üstte NFC okuyucu, 16'lı halka, figür zemini (ışık oyuğu)", fontsize=11)
    plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0, wspace=0)
    fig.savefig(os.path.join(cikti, "cakil_ic_kesit3b.png")); plt.close(fig)
    # 2) üstten yerleşim planı (katlar)
    fig, axs = plt.subplots(1, 3, figsize=(19, 6.6), dpi=110)
    katlar = [("Alt kat (taban plakası, z 2–22)", ["hoparlör (aşağı bakar)", "18650 yatağı", "TP4056 Type-C", "MAX98357A", "KCD11 anahtar"]),
              ("Orta kat (raf, z 23–34)", ["ESP32-S3 (rafta)"]),
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
          (yapi["raf"].translate([0, 0, 14]), RENK_YAPI["raf"], False),
          (z["ESP32-S3 (rafta)"].translate([0, 0, 18]), RENK_PARCA["ESP32-S3 (rafta)"], False),
          (yapi["taban"].translate([0, 0, -40]), RENK_YAPI["taban"], False)]
    for ad in ("hoparlör (aşağı bakar)", "18650 yatağı", "TP4056 Type-C", "MAX98357A"):
        ls.append((z[ad].translate([0, 0, -20]), RENK_PARCA[ad], False))
    elev, azim = 16, 60
    e, a = math.radians(elev), math.radians(azim)
    K.ciz(ax, ls, [math.cos(e) * math.cos(a), math.cos(e) * math.sin(a), math.sin(e)])
    ax.set_xlim(-60, 60); ax.set_ylim(-60, 60); ax.set_zlim(-45, 250)
    ax.set_box_aspect((1, 1, 2.3))
    ax.view_init(elev=elev, azim=azim)
    ax.set_title("Patlatılmış görünüş (RC522): kabuk, halka, tutucu, okuyucu, ESP32 rafı, alt kat, taban", fontsize=10)
    fig.savefig(os.path.join(cikti, "cakil_ic_patlatilmis.png")); plt.close(fig)
    print("önizleme:", cikti)


if __name__ == "__main__" and "--onizle" in sys.argv:
    onizle()
