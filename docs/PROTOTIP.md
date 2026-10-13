# İlk prototip: parça listesi ve kurulum (masa üstü, lehimsiz)

Amaç: kartı bilgisayarsız bir oyuncak gibi denemek (ürün tanımı `docs/URUN_TANIMI.md`: düğme yok). Çocuk figürü
NFC standına koyar; kart selamlar ve hazır hikâyeyi hemen okur (boştayken arka planda yenilerini hazırlar); "Merhaba
Eko" ile sesli komut; halka durumu gösterir. Bağlantı ayrıntıları
`firmware/hikaye_oyuncak/README.md` bölüm 5–6'da; pinler tek yerde: `firmware/hikaye_oyuncak/donanim.h`.

## Parça listesi

Türkiye'de elektronik satan sitelerde (ör. Robotistan, Direnc.net, Robotzade, Trendyol) şu adlarla aranır.
Fiyat yazmadım: kurla hızlı değişiyor.

| Adet | Parça | Arama adı / not |
|---|---|---|
| 1 | ESP32-S3 geliştirme kartı **N16R8** | "ESP32-S3-DevKitC-1 N16R8" (16 MB flash, 8 MB PSRAM şart; N8R2 vb. olmaz) |
| 1 | I2S ses yükselteci | "MAX98357A I2S amplifikatör" |
| 1 | Hoparlör 4–8 Ω, 2–3 W | 40–50 mm, kablolu |
| 1 | I2S mikrofon | "INMP441 I2S mikrofon modülü" |
| 1 | NeoPixel halka | WS2812B halka (dış Ø104 mm hedef; LED sayısı `HALKA_LED_SAYISI`) + 74AHCT1G125 seviye çevirici + 330 Ω + 1000 µF |
| 1 | Breadboard + jumper kablo | erkek-erkek ve erkek-dişi |
| 1 | USB-C kablo (veri destekli) | yükleme ve güç |
| İsteğe bağlı | 470–1000 µF kondansatör | yükseltecin 5V–GND'sine, ses sırasında yeniden başlamayı önler |
| 1 | NFC okuyucu | "RC522 RFID modülü" + "NTAG213 etiket" (figür tabanları ve ayar kartı; sürücü yazıldı, kartta denenmedi) |
| Sonra | Pil | 1S Li-ion + şarj modülü (TP4056 korumalı) + 5V yükseltici; ilk denemede USB yeterli |

## Bağlantı (README'deki tablo)

| Parça ucu | ESP32-S3 |
|---|---|
| MAX98357A VIN | 5V |
| MAX98357A GND | GND |
| MAX98357A BCLK | GPIO4 |
| MAX98357A LRC | GPIO5 |
| MAX98357A DIN | GPIO6 |
| Hoparlör | MAX98357A'nın + ve − uçları |
| MAX98357A SD | GPIO7 |
| INMP441 SCK / WS / SD (L/R → GND, VDD 3V3) | GPIO15 / 16 / 17 |
| RC522 SCK / MISO / MOSI / SDA / RST (3V3) | GPIO12 / 13 / 11 / 10 / 9 |
| Halka DIN (seviye çevirici + 330 Ω üzerinden; halka 5V) | GPIO18 |

Pin haritası kesindir (`docs/URUN_TANIMI.md`); kart üstündeki RGB LED kullanılmaz.

## Sıra

1. Kartı yalnız USB ile bağlayıp yazılımı ve `modeller/c3ft_karma/model.bin`'i **0x1D0000**'e yükle (README bölüm 2–3).
   Seri monitörde `fp=00ea3e55` ve `?` ile figür listesi → `1 1` ile bir hikâye → `b` ile hız testi.
2. Ses modeli hazır olunca `ses.bin`'i 0xBB0000'e yükle; MAX98357A ve hoparlörü bağla; `s Merhaba` ile dene.
3. RC522, mikrofon ve halkayı bağla. Ayar kartını ve figür etiketlerini ayar sayfasından "oyuncak tanıt" ile yaz
   (README 6). Her figürü bir kez standa koy (tanınsın); ilk gece kartı USB'de açık bırak: tanınan figürlerin
   kuyruğu dolsun.
4. Sabah figürü standa koy: selamdan sonra hikâye beklemeden başlamalı.

Seri monitör çıktısını (açılış satırları, `b` sonucu, hız/profil satırı) Claude'a gönder; hız gerçek kartta ilk kez
ölçülecek.
