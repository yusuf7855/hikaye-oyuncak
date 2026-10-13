"""Masal standı — bütün ölçüler (mm) tek yerde.

Koordinatlar (montaj): z yukarı, z=0 alt gövdenin taban yüzü; merkez (0,0) standın ekseni.
+y = ÖN (çocuğun oturduğu taraf, hoparlör ızgarası), -y = ARKA (USB-C güç girişi, mikrofon deliği).
Açılar x ekseninden saat yönünün tersine (0° = sağ, 90° = ön, 270° = arka).

Kaynaklarla doğrulanan ölçüler docs/DONANIM.md "Parça ölçüleri" tablosunda; doğrulanamayanlar
(RC522 anten merkezi, kopya kartların ölçü farkları) burada DOĞRULANMADI diye işaretli ve
tutucu/kızak tasarımıyla tolere edilir (delik konumu tahmin edilmez).
"""

# ---------------------------------------------------------------- genel
D_DIS = 128.0            # dış çap
R_DIS = D_DIS / 2
DUVAR = 2.5              # alt gövde yan duvarı
TABAN = 2.5              # alt gövde tabanı
R_IC = R_DIS - DUVAR     # 61.5 iç yarıçap
H_ALT = 45.0             # alt gövde yüksekliği (taban yüzünden duvar üstüne = kapak alt yüzü)
ALT_PAH = 3.0            # alt dış kenarda 45° pah (çocuk güvenliği; desteksiz basılır)
DIL_KAL = 1.2            # duvar üstündeki merkezleme dili (kalınlık)
DIL_Y = 2.0              # dil yüksekliği
OLUK_PAY = 0.2           # dil–oluk boşluğu (her yan)

# ---------------------------------------------------------------- birleştirme vidaları (alttan, gizli)
VIDA_R = 57.0            # vida ekseni yarıçapı
VIDA_ACILAR = (0.0, 135.0, 225.0)   # 3 vida (ön hoparlörü ve arka USB'yi serbest bırakır)
KOLON_D = 8.0            # alt gövdedeki vida kolonu
VIDA_DELIK = 3.4         # M3 geçiş deliği
VIDA_HAVSA_D = 6.6       # M3 silindir başlı vida başı + tornavida için derin havşa (Ø)
VIDA_SIKMA = 6.0         # kolonun üstte sıkılan dolu kısmı (vida M3x10)
INSERT_D = 4.0           # kapakta M3 ısıl gömme somun deliği (M3 x 5,7 mm insert için Ø4,0)
INSERT_DERIN = 6.0

# ---------------------------------------------------------------- ayaklar
AYAK_D = 13.0            # yapışkanlı silikon ayak yuvası (Ø12,7 x 3,5 mm ayak)
AYAK_DERIN = 1.0
AYAK_R = 50.0
AYAK_ACILAR = (90.0, 210.0, 330.0)  # 3 ayak: sallanmaz

# ---------------------------------------------------------------- kapak
KAPAK_KAL = 8.0          # kapak kalınlığı (montajda z = H_ALT .. H_ALT+8)
KAPAK_UST_YUVARLAK = 3.0 # üst dış kenar yuvarlatma yarıçapı
KAPAK_ALT_PAH = 0.6
# figür yuvası (oturak)
YUVA_TABAN_KAL = 1.8     # yuva tabanı = NFC anteni üstündeki plastik (≤ 2 mm)
TABAN_D = 62.0           # figür tabanı (jeton) çapı
TABAN_H = 6.0            # figür tabanı yüksekliği
YUVA_PAY = 0.4           # yuva–taban radyal boşluk
YUVA_R = TABAN_D / 2 + YUVA_PAY      # 31.4
YUVA_PAH = 1.2           # yuva ağzı pahı (kolay oturma)
ANAHTAR_G = 6.0          # yuvadaki kama (arka, 270°) genişliği
ANAHTAR_DERIN = 3.0      # kamanın yuva duvarından içeri çıkıntısı
ANAHTAR_PAY = 0.4        # tabandaki kama oluğu boşluğu (her yan)
ANAHTAR_VAR = True       # küçük çocuklar için False: taban her yönde oturur
# NeoPixel halka kanalı (halka: dış Ø104, iç Ø90, kalınlık 3,5 — URUN_TANIMI.md)
HALKA_DIS_D = 104.0
HALKA_IC_D = 90.0
HALKA_KAL = 3.5
HALKA_PAY = 0.4          # radyal boşluk (her yan)
KANAL_TABAN = 2.0        # kanal tabanı kalınlığı
KANAL_R_IC = HALKA_IC_D / 2 - HALKA_PAY    # 44.6
KANAL_R_DIS = HALKA_DIS_D / 2 + HALKA_PAY  # 52.4
LED_UST = KANAL_TABAN + HALKA_KAL          # 5.5 (kapak koordinatı)
OMUZ_Z = 6.3             # difüzör eteklerinin oturduğu omuz (LED üstünden 0,8 mm yukarıda)
OMUZ_G = 1.2             # omuz genişliği
KANAL_UST_R_IC = KANAL_R_IC - OMUZ_G       # 43.4
KANAL_UST_R_DIS = KANAL_R_DIS + OMUZ_G     # 53.6
KILIT_OLUK_Z = (6.75, 7.35)  # difüzör tırnağı oluğu (dış duvarda)
KILIT_OLUK_DERIN = 0.4
HALKA_KABLO_ACI = 270.0  # halka kablosu geçişi (arka)
# RC522 tutucu vida pilotları (M2,5 x 8 sac vidası)
RC_VIDA_PILOT = 2.0
RC_VIDA_DERIN = 6.0

# ---------------------------------------------------------------- difüzör halka
ISIK_BOSLUGU = 5.0       # LED üstü → difüzör alt yüzü (eşit ışık için ≥ LED aralığının ~yarısı)
DIF_KAL = 1.8            # difüzör üst plakası (beyaz/doğal PETG, 1,2–2 mm)
DIF_ETEK = 1.2           # etek kalınlığı
DIF_PAY = 0.2            # etek–kanal duvarı boşluğu
DIF_TIRNAK = 0.4         # dış etekteki çevresel tırnak (oluğa oturur)

# ---------------------------------------------------------------- figür tabanı (jeton)
ETIKET_D = 25.0          # NTAG213 Ø25 mm etiket (0,2–0,3 mm)
ETIKET_CEP_D = 25.6
ETIKET_CEP_DERIN = 0.4
TABAN_ALT_PAH = 0.8
TABAN_UST_PAH = 1.5
YAPISTIRMA_D = 20.0      # üstte yapıştırma çukuru
YAPISTIRMA_DERIN = 0.8
def _yazi_fontu():
    """matplotlib'in içindeki DejaVu Sans Bold: her işletim sisteminde aynı, Türkçe harfleri var."""
    import os
    import matplotlib
    return os.path.join(matplotlib.get_data_path(), "fonts", "ttf", "DejaVuSans-Bold.ttf")


YAZI_FONT = _yazi_fontu()
YAZI_BOY = 5.5           # font boyu (büyük harf ≈ 4 mm)
YAZI_DERIN = 0.6         # kazıma derinliği
YAZI_R = 27.0            # yazı taban çizgisi yarıçapı (harflerin üstü merkeze bakar, öne okunur)
ALT_YAZI_BOY = 4.0
AYAR_TOPUZ_D = 22.0      # ayar kartında tutma topuzu
AYAR_TOPUZ_H = 14.0

# ---------------------------------------------------------------- hoparlör (ön, yandan yayan)
HOPARLOR_D = 40.0        # 40 mm 4 Ω 3 W (Adafruit 3968: Ø40 x 20; PUI AS04004PR-R: Ø40 x 18,3)
HOPARLOR_DERIN = 20.0    # gövde derinliği (≤ 21 mm sığar; arka dayanakta 3 mm köpük payı)
HOP_YUZ_Y = 56.0         # hoparlör ön yüzünün dayandığı düz bölme düzlemi
HOP_Z = TABAN + 0.5 + HOPARLOR_D / 2       # 23.0 merkez yüksekliği
IZGARA_D = 33.0          # ızgara yarık alanı çapı
IZGARA_YARIK = 1.6       # yarık genişliği (parmak girmez)
IZGARA_ADIM = 3.4
ON_ODA_D = 35.0          # hoparlör önündeki hava odası

# ---------------------------------------------------------------- mikrofon (arka üst, hoparlörden uzak)
MIK_ACI = 250.0
MIK_Z = 36.0
MIK_PCB_D = 14.5         # INMP441 yuvarlak kart ~Ø14 (DOĞRULANMADI: üreticiye göre 14–15 mm)
MIK_YUVA_BOSLUK = 3.0    # conta (1 mm köpük) + PCB (1,0–1,6) yuvası
MIK_DELIK = 1.0          # akustik delik
MIK_YUZ_GERI = 2.0       # düz ped yüzü iç duvardan bu kadar içeride
MIK_CONTA_D = 7.0        # conta yuvası çapı
MIK_CONTA_DERIN = 0.5

# ---------------------------------------------------------------- USB-C güç girişi (arka orta)
USBC_KART_G = 20.4       # Adafruit 4090: 20,4 x 14,2 x 5,0 mm
USBC_KART_D = 14.2
USBC_KART_H = 5.0        # PCB dahil toplam
USBC_PCB = 1.6
USBC_AGIZ = (9.6, 4.2)   # duvardaki açıklık (soket ağzı 8,94 x 3,26 + pay)
USBC_Z = 10.0            # soket merkezi yüksekliği
USBC_ON_Y = -62.3        # kartın ön kenarı / soket ağzı (duvar içine düz cep)
USBC_DIS_DUZ = -63.6     # dış yüzde düz alın (fiş gövdesi buraya dayanır)

# ---------------------------------------------------------------- taşıyıcı kart (ESP32 + seviye çevirici)
TASIYICI = (50.0, 70.0)  # 5x7 cm çift yüzlü delikli pertinaks (x, y)
TASIYICI_MERKEZ = (0.0, -7.0)
TASIYICI_PCB = 1.6
TASIYICI_Z = TABAN + 4.5 # pertinaks alt yüzü (altında lehim + kablo payı)
TASIYICI_PAY = 0.3
DEVKIT = (25.4, 62.74)   # ESP32-S3-DevKitC-1 PCB (Espressif PCB çizimi), anten modülü ~7 mm taşar
DEVKIT_ANTEN_TASMA = 7.0
DEVKIT_X = -10.0         # kartın x merkezi (taşıyıcının sol yarısı)
DEVKIT_Y_ON = 27.74      # USB ucu öne bakar (antende metal yok: anten arkada duvara yakın)
DISI_HEADER_H = 8.5

# ---------------------------------------------------------------- MAX98357A (dikey kızak, sağ ön)
AMP_KART = (17.8, 19.4)  # Adafruit 3006: 19,4 x 17,8 x 3 mm (17,8 kenar yatay)
AMP_X = 38.0             # PCB düzleminin x konumu
AMP_Y0 = 9.5             # kartın arka kenarı
AMP_TABAN_Z = TABAN + 9.0  # kart alt kenarı (altta hoparlör vida klemensine kablo payı)
AMP_PAY = 0.25

# ---------------------------------------------------------------- RC522 (kapağın altında, tutucuyla)
RC522 = (60.0, 39.5)     # mavi RC522 modülü ~60 x 39,5 mm (delik konumları yayımlanmamış)
RC522_PCB = 1.6
RC522_PAY = 0.3
RC522_ANTEN_KAYMA = 10.0 # anten merkezinin kart merkezinden uzak uca kayması (DOĞRULANMADI; kartla ölç)
RC_TUT_DUVAR = 2.4
RC_TUT_DUDAK = 1.5       # kartın uzun kenarlarının altındaki dudak
RC_TUT_ALT = 1.4         # dudak kalınlığı
RC_VIDALAR = ((-30.0, 25.5), (-30.0, -25.5), (24.0, 26.0), (24.0, -26.0))

# ---------------------------------------------------------------- çizim/örgü
SEG_BUYUK = 192
SEG_KUCUK = 40
