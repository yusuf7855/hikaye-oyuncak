# KWS: "Merhaba Eko" ve çocuk komutları (kartta, internetsiz)

Kart (ESP32-S3) mikrofonu sürekli dinler; "Merhaba Eko" duyunca ~4 sn komut bekler (`docs/URUN_TANIMI.md`).
Uyku sesli komut değil (gece figürü); "Uykum geldi", "İyi geceler" olumsuz örnek olarak eğitildi.

| Olay (`kws.h`) | Çocuğun diyebileceği (eğitimde ayrıca çocuk söyleyişleri: "Melhaba", "Dul", "Tekral" ...) |
|---|---|
| `KWS_UYANDIRMA` | "Merhaba Eko", "Melhaba Eko", "Meraba Eko", "Merhaba Ekoo" ("Eko" tek başına UYANDIRMAZ) |
| `KWS_DUR` | "Dur", "Dursun", "Sus" |
| `KWS_DEVAM` | "Devam", "Devam et", "Hadi" |
| `KWS_BASKA` | "Başka", "Başka masal", "Bunu sevmedim" |
| `KWS_BIR_DAHA` | "Bir daha", "Yine", "Tekrar" |
| `KWS_SESI_AC` | "Sesini aç", "Yüksek", "Duyamıyorum" |
| `KWS_SESI_KIS` | "Sesini kıs", "Çok yüksek", "Yavaş konuş" |

Arayüz: `firmware/hikaye_oyuncak/kws.h` — `bool kws_kur(void); int kws_isle(const int16_t *pcm, int n);`
(16 kHz mono int16, istenen parça boyu; komutlar yalnız uyandırmadan sonraki 4 sn'de; yumuşatma, eşik, bekleme
içeride). Ağırlıklar `firmware/hikaye_oyuncak/generated/kws_model.h` (`disa_aktar.py` yazar).

## Model ve kart bütçesi

- Öznitelik: 32 ms Hann pencere, 20 ms adım (saniyede 50 kare), 512 FFT, 40 log-mel (100–7800 Hz), int8.
- Ağ: nedensel genişletilmiş TCN — giriş conv (40→64, k3) + 8 artık blok (64→64, k3, genişleme 1,2,4,8,16,32,1,2)
  + 1×1 çıkış (9 sınıf: ARKA, KONUSMA, 7 olay). Alıcı alan 135 kare = 2,7 sn. Akışta her karede yalnız yeni kare
  hesaplanır (katman başına (k-1)·d karelik halka tampon), pencereyi baştan hesaplamak yok.
- int8 ağırlık (kanal başına ölçek), int8 etkinlik, int32 toplam, tamsayı yeniden ölçekleme: PyTorch tamsayı
  başvurusuyla **bit bit aynı** (`tools/kws_test.py`). Öznitelik float (FFT); PC ile fark yuvarlama sınırında, ölçülen 0.
- Boyut: 106 560 int8 ağırlık, başlıkla birlikte ~110 KB flash. RAM: ~21 KB (geçmiş 9 KB + FFT/pencere tamponları).
- İşlem: 106,6 K çarpma-toplama/kare × 50 = **5,3 M MAC/s** + FFT/mel ~1,5 MFLOP/s. Xtensa LX7'de düz C ile
  ~3 çevrim/MAC varsayımıyla bir 240 MHz çekirdeğin **~%7–10'u** (kartta ölçülmedi).
- Eğitim: QAT (BN katlanır, etkinlik ölçekleri kalibre edilir, sonra kartın int8 hesabıyla eğitim sürer).

## Veri (gerçek kayıt yok → yapay)

`sentezle.py`: Supertonic 3 (Open RAIL-M), 10 ses ve karışımları. **Eğitim: F1 F2 F3 F5 M1 M2 M3 M4; sınama yalnız
görülmemiş F4, M5.** Çocuk benzetimi WORLD vokoderiyle (perde 230–400 Hz, formant ×1,08–1,45, tonlama abartısı,
zaman esnetme, %8 fısıltı, %8 bağırma) + yazımla yanlış söyleyiş ("Melhaba Ekko", "Dul", "Tekral"). Olumsuzlar: karışan
sözcükler ("Merhaba", "Eko", "Merhaba Ece", "Ekmek", "Susadım", "Bunu sevdim", "İyi günler" ...), günlük cümleler,
hikâye sözcükleri ve cümleleri (`data/urun_v2`; sınamada `urun_v3`).
`veri.py`: her adımda yeni 4 sn sahne — ev gürültüleri, oda yankısı, mikrofon renklendirme, kırpılma ve **kartın kendi
hoparlöründen hikâye sesi** (küçük hoparlör benzetimi, çocuk sesine göre -10..+25 dB).
Uzun konuşma içindeki komut sözcükleri komut değildir: model kendi başına (önünde sessizlik ya da "Merhaba Eko" olan)
kısa ifadeleri öğrenir.

## Çalıştırma

```bash
# 1) veri (~2,5 saat, 2 çekirdek; ~1,1 GB ses_kws_veri/ham, depoya girmez)
python3 -m venv /tmp/st_venv && /tmp/st_venv/bin/pip install supertonic soundfile scipy pyworld
/tmp/st_venv/bin/python ses/kws/sentezle.py --model-dizini <supertonic assets dizini> --is 2
# 2) eğitim (float + QAT) -> ses_kws_veri/calisma/qat.pt
.venv/bin/python ses/kws/egit.py --adim 8000 --qat-adim 2000
# 3) eşik seçimi (dev) + sınama raporu (görülmemiş sesler)
.venv/bin/python ses/kws/degerlendir.py --model ses_kws_veri/calisma/qat.pt --yaz
# 4) kart başlığı + C = PyTorch denemesi
.venv/bin/python ses/kws/disa_aktar.py --model ses_kws_veri/calisma/qat.pt
.venv/bin/python firmware/hikaye_oyuncak/tools/kws_test.py --model ses_kws_veri/calisma/qat.pt
```

Gerçek çocuk kaydı ve ince ayar: [`KAYIT.md`](KAYIT.md), `ince_ayar.py`.

## Sonuçlar (14 Ekim 2026, yalnız YAPAY veri; gerçek çocuk sesiyle ölçülmedi)

Model: `ses_kws_veri/calisma/qat.pt` (float 8000 + 6000 + 8000 adım, QAT 2000; ~3 saat CPU). Eşikler dev akışında
seçildi (doğal konuşma + hikâye sesinde saatte ≤ 0,5 yanlış uyanma, karışan ifadelerde ≤ %5): uyanma 0,93,
komut 0,50, yumuşatma 5 kare. Sınama: görülmemiş sesler (F4, M5), görülmemiş söyleyişler, görülmemiş hikâye
metni; kartın int8 hesabıyla (C ile bit bit aynı). Koşul başına 160 deneme.

| koşul | uyanma | komut doğru (uyanınca) | uçtan uca |
|---|---|---|---|
| sessiz oda | 0,969 | 0,923 | 0,893 |
| ev gürültüsü 10 dB | 0,969 | 0,847 | 0,820 |
| ev gürültüsü 5 dB | 0,894 | 0,835 | 0,748 |
| hoparlörden hikâye, çocuk sesi 10 dB üstte | 0,906 | 0,845 | 0,775 |
| hoparlörden hikâye, eşit düzey (0 dB) | **0,600** | 0,690 | 0,415 |
| güçlü yankı (RT60 0,9–1,2 sn, eğitimde yok) | 0,925 | 0,855 | 0,777 |
| süpürge 5 dB (eğitimde yok) | 0,794 | 0,726 | 0,590 |

- Yanlış uyanma: hikâye okuması 0,8 saat 0; doğal konuşma 1,2 saat 0; gürültü 0,5 saat 0; konuşma + hikâye 1,2 saat
  1 → toplam ~3,7 saatte 1 (≈0,27/saat; ölçüm süresi kısa, güven aralığı geniş).
- Karışan ifadeler ("Merhaba", "Eko", "Merhaba Ece", "Ekmek" ...): 752 söyleyişin %1,6'sı uyandırdı; en kötüsü
  tek başına "Meraba" (5/8) ve "Melhaba" (2/8) — çocuk "Meraba ... Eko" derken araya uzun duraklama koyarsa iki
  sözcük de tek tek gelir; bu sınır gerçek kayıtla ayarlanmalı.
- Komutlar (uyanınca, tüm koşullar): DUR 0,87, DEVAM 0,87, BASKA 0,76 (DUR ile karışıyor), BIR_DAHA 0,84,
  SESI_AC 0,76 (DUR/SESI_KIS ile), SESI_KIS 0,86. Boş pencerede (çocuk komut söylemeden) yanlış komut %0–5.
- Ses türüne göre uyanma: çocuk benzetimi 0,89, bağırma 0,95, fısıltı 0,90, yetişkin 0,80.
- Eşik tablosu (sınama, tüm koşullar): 0,80 → uyanma 0,93 / 1,9 yanlış uyanma saatte; 0,93 → 0,87 / 0,27;
  0,97 → 0,81 / 0.

**Bilinen zayıflık:** hoparlörden gelen hikâye sesi çocuğun sesi kadar yüksekse uyanma %60'a düşer. Kart, çaldığı
sesi bildiği için yankı giderme (çalınan PCM'i başvuru alan NLMS) ya da "Merhaba Eko" algılanınca değil ama
okurken ses düzeyini sınırlamak en büyük kazancı verir; ayrıca gerçek kayıt ve kartın kendi mikrofonuyla ince ayar.
