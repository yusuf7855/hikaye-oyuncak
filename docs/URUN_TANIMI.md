# Ürün tanımı (ürün sahibinin kararları, 13 Ekim 2026) — bütün ajanlar için ortak

Yalnız Türkçe. İnternetsiz. Düğme YOK.

## Etkileşim
- Uyandırma sözcüğü: tek ve sabit: **"Merhaba Eko"** (çocuk söyleyişleri de tanınmalı: "Melhaba Eko", "Meraba Eko", "Merhaba Ekoo", "Eko!" tek başına DEĞİL — yanlış uyanmayı azaltmak için iki sözcük gerekli).
- Sesli komutlar ÇOCUĞA göre (3–6 yaş, kısa, doğal söyleyişler), yalnız uyandırmadan sonraki ~4 sn içinde:
  | Olay | Çocuğun diyebileceği |
  |---|---|
  | DUR | "Dur", "Dursun", "Sus" |
  | DEVAM | "Devam", "Devam et", "Hadi" |
  | BASKA | "Başka", "Başka masal", "Bunu sevmedim" (aynı oyuncağın başka hikâyesi) |
  | BIR_DAHA | "Bir daha", "Yine", "Tekrar" (son hikâyeyi baştan) |
  | SESI_AC | "Sesini aç", "Yüksek", "Duyamıyorum" |
  | SESI_KIS | "Sesini kıs", "Çok yüksek", "Yavaş konuş" |
- Uyku sesli komutla DEĞİL, gece figürüyle açılır (aşağıda "Uyku modu").
- Hiçbir komut karakter SEÇEMEZ. Hikâye yalnız standa konan oyuncağın hikâyesidir. Standda oyuncak yoksa hikâye okunmaz. Standa hiç konmamış oyuncağın hikâyesi hiç yazılmaz ve okunmaz (kart yalnız "tanınmış" oyuncaklar için arka planda hikâye hazırlar).
- Selamlama: "Merhaba Emre, şimdi sana Pamuk'un hikâyesini okuyacağım." (ad yoksa "Merhaba, şimdi sana ..."). Ek uyumu doğru olmalı (Niloya'nın, Maşa'nın, Keloğlan'ın, Örümcek Adam'ın, Hello Kitty'nin, Chase'in ...).
- Ayarlar: "Ayar kartı" (NFC, nfc_no 200) standa konunca kart kendi Wi-Fi erişim noktasını açar; telefonda ayar sayfası kendiliğinden açılır (captive portal). Ayarlar: çocuğun adı, en yüksek ses, uyku zamanlayıcısı (10/20/30 dk), halka parlaklığı, oyuncak çekilince ne olsun, oyuncak tanıt (NFC etiketine figür yazma), hikâyeleri sil. Wi-Fi yalnız ayar modunda açık; internet hiç kullanılmaz.
- Figür listesi ve halka renkleri: `data/figur_donanim.json` (nfc_no + renk). NFC etiketine figür numarası yazılır (NTAG213 kullanıcı belleği, sayfa 4+: sihir + sürüm + nfc_no + CRC).

## Uyku modu: gece figürü ("Ay Dede", nfc_no 12)
- Standa gece figürü konunca oyuncak **ninni moduna** geçer: ninni ve uyku masalı okur. Bu figür bir hikâye karakteri değil, bir mod figürüdür (bir geceyi temsil eder: ay, yıldızlar).
- **Metin tarzı değişir:** ninni gibi ritimli, tekrarlı, yumuşak dizeler ("Uyusun da büyüsün, ninni...") ve çok sakin kısa uyku masalları (ay, yıldızlar, uyuyan hayvanlar; sorun yok ya da çok küçük; son: herkes uyur). Hikâye modeli bu tarz için ayrı veriyle eğitilir (istemde "Karakter: Ay Dede" + tür alanı). Veri: `data/urun_v4` gece metinleri (kart `gece`, yazım kılavuzu `degerlendirme/KILAVUZ_GECE.md`); tür alanı plan satırının ilk kelimesidir (`Sorun: ninni, ...` ya da `Sorun: masal, ...`), kart istemi `...\nSorun: ninni,` ile türü seçer. Ninni dizeleri tek satırdadır, her dize noktayla biter: ses modeli noktada uzun, virgülde kısa durur. Model gece verisiyle eğitilene dek `urun_uret.GECE_MODELDE = False` (kart bu figürde yerleşik metin okur).
- **Ses tonu değişir:** kartın ses modeli daha yavaş (≈%75 hız), daha alçak perde (≈−2 yarım ton), daha kısık ve cümle aralarında daha uzun duraklarla okur; isteğe bağlı çok kısık bir müzik kutusu melodisi (kartta sentezlenir, dosya gerekmez). Gerçek şarkı (melodili ninni) bu ses modeliyle mümkün değil: "ninni okur", söylemez.
- **Halka:** gece mavisi, yıldız gibi rastgele yavaş parıldayan birkaç LED; okuma bitince 60 sn'de söner; ardından oyuncak uyku zamanlayıcısıyla kapanır.
- Selamlama: "İyi geceler Emre, şimdi sana bir ninni söyleyeceğim." (ad yoksa "İyi geceler, ...").

## Halka (NeoPixel, WS2812B uyumlu) — standın üstünde, figürün çevresinde
- Ölçü: dış Ø104 mm, iç Ø90 mm, kalınlık 3,5 mm. LED sayısı ürün sahibince doğrulanacak; yazılımda tek sabit `HALKA_LED_SAYISI` (varsayılan 35), tasarımda LED sayısından bağımsız.
- 5 V beslenir; veri hattı 3,3 V → 5 V seviye çevirici (74AHCT1G125) + 330 Ω seri direnç; halka girişinde 1000 µF kondansatör. Yazılımda parlaklık üst sınırı (varsayılan %25) ve toplam akım sınırı (≤ 600 mA).
- Davranışlar:
  | Durum | Halka |
  |---|---|
  | Açılış | Gökkuşağı tek tur, sonra söner |
  | Boşta, oyuncak yok | Çok sönük "nefes alan" beyaz (ya da kapalı, ayardan) |
  | Oyuncak kondu | Figürün rengiyle halkanın dolması (≈0,6 sn) |
  | Selamlama / okuma | Figür renginde; ilerleme: hikâyenin okunan kısmı kadar LED dolu, kalan sönük (cümle cümle ilerler) |
  | Konuşma sesi | Okurken parlaklık sesin yüksekliğiyle hafifçe dalgalanır |
  | "Merhaba Eko" duyuldu | Beyaz dönen nokta = dinliyorum |
  | Komut anlaşıldı | Kısa yeşil yanıp sönme; anlaşılmadı: kısa turuncu |
  | Ses aç/kıs | Halka ses düzeyini gösterir (0..maks dolu LED, beyaz), 2 sn sonra eski haline döner |
  | Arka planda hikâye hazırlanıyor | Çok sönük, yavaş dönen figür rengi noktası (ayardan kapatılabilir) |
  | Uyku modu (gece figürü) | Gece mavisi, yavaş parıldayan yıldızlar, okuma bitince 60 sn'de söner |
  | Ayar modu | Turkuaz nefes |
  | Hata (model yok vb.) | Kırmızı yanıp sönme |

## Pin haritası (ESP32-S3-DevKitC-1 N16R8) — kesin, değiştirilecekse bütün belgeler birlikte
| Parça | Sinyal | GPIO |
|---|---|---|
| MAX98357A hoparlör yükselteci (I2S0) | BCLK / LRC / DIN / SD | 4 / 5 / 6 / 7 |
| INMP441 mikrofon (I2S1) | SCK / WS / SD (L/R → GND) | 15 / 16 / 17 |
| RC522 NFC okuyucu (SPI, 3,3 V) | SCK / MISO / MOSI / SDA(SS) / RST | 12 / 13 / 11 / 10 / 9 |
| NeoPixel halka | DIN (seviye çevirici üzerinden) | 18 |
| Kart üstü RGB LED | kullanılmaz | 48 (ya da 38) |
Kullanılmayacak uçlar: 0, 3, 45, 46 (açılış), 19/20 (USB), 26–37 (flash/PSRAM), 43/44 (UART).
Güç: USB-C 5 V / 2 A adaptör (standın arkasındaki USB-C girişi), pil yok (ilk sürüm).
