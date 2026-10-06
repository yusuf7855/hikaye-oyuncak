# İlk prototip: parça listesi ve kurulum (masa üstü, lehimsiz)

Amaç: kartı bilgisayarsız bir oyuncak gibi denemek. Çocuk FİGÜR düğmesiyle figürü, YER düğmesiyle yeri seçer,
OYNAT'a basar; kart hazır hikâyeyi hemen okur (boştayken arka planda yenilerini hazırlar). Bağlantı ayrıntıları
`firmware/hikaye_oyuncak/README.md` bölüm 5–6'da; pinler tek yerde: `firmware/hikaye_oyuncak/donanim.h`.

## Parça listesi

Türkiye'de elektronik satan sitelerde (ör. Robotistan, Direnc.net, Robotzade, Trendyol) şu adlarla aranır.
Fiyat yazmadım: kurla hızlı değişiyor.

| Adet | Parça | Arama adı / not |
|---|---|---|
| 1 | ESP32-S3 geliştirme kartı **N16R8** | "ESP32-S3-DevKitC-1 N16R8" (16 MB flash, 8 MB PSRAM şart; N8R2 vb. olmaz) |
| 1 | I2S ses yükselteci | "MAX98357A I2S amplifikatör" |
| 1 | Hoparlör 4–8 Ω, 2–3 W | 40–50 mm, kablolu |
| 3 | Basmalı düğme | "12 mm tact switch" ya da büyük renkli "arcade buton" (çocuk için daha iyi) |
| 1 | Breadboard + jumper kablo | erkek-erkek ve erkek-dişi |
| 1 | USB-C kablo (veri destekli) | yükleme ve güç |
| İsteğe bağlı | 470–1000 µF kondansatör | yükseltecin 5V–GND'sine, ses sırasında yeniden başlamayı önler |
| İsteğe bağlı | NFC okuyucu | "RC522 RFID modülü" + "NTAG213 etiket" (figür jetonları için; sürücü yazıldı, kartta denenmedi) |
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
| FİGÜR düğmesi | GPIO7 ↔ GND |
| YER düğmesi | GPIO15 ↔ GND |
| OYNAT düğmesi | GPIO16 ↔ GND |

Düğmelere direnç gerekmez (iç pull-up). Kart üstündeki RGB LED durumu gösterir.

## Sıra

1. Kartı yalnız USB ile bağlayıp yazılımı ve `modeller/c3ft_karma/model.bin`'i yükle (README bölüm 2–3).
   Seri monitörde `fp=00ea3e55` ve `?` ile figür listesi → `1 1` ile bir hikâye → `b` ile hız testi.
2. Ses modeli hazır olunca `ses.bin`'i 0xBB0000'e yükle; MAX98357A ve hoparlörü bağla; `s Merhaba` ile dene.
3. Düğmeleri bağla. İlk gece kartı USB'de açık bırak: kuyruk dolsun (figür başına 3 hikâye, tahmini 5–6 saat).
4. Sabah OYNAT'a bas: hikâye beklemeden başlamalı.

Seri monitör çıktısını (açılış satırları, `b` sonucu, hız/profil satırı) Claude'a gönder; hız gerçek kartta ilk kez
ölçülecek.
