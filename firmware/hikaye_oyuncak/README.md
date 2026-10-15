# Hikâye Oyuncağı — kart yazılımı (ESP32-S3 N16R8)

Bu yazılım, eğittiğimiz ürün modelini **kartın kendisinde** çalıştırır: 11 çizgi film figüründen birini ve onun
kartındaki yerlerden birini seçersiniz, kart önce planı (Sorun/Çözüm), sonra hikâyeyi yazar ve hızını (token/s)
gösterir. İnternet, SD kart ya da bilgisayar gerekmez. Ses modeli (`ses.bin`) ve bir MAX98357A hoparlör kartı
takılıysa hikâyeyi kartın kendisinde sesli okur (bkz. **5. Ses**).

İki türlü kullanılır:
- **Oyuncak olarak** (bilgisayarsız, bkz. **6**; ürün tanımı `docs/URUN_TANIMI.md`): düğme yok. Çocuk figürünü NFC
  standına koyar; kart selamlar ve **o figürün** hikâyesini okur, standın halkası (NeoPixel) durumu gösterir. Sesli
  komutlar "Merhaba Eko" ile (dur, devam, başka, bir daha, sesini aç/kıs). Gece figürü "Ay Dede" ninni modunu açar;
  "ayar kartı" telefondan ayar sayfasını (Wi-Fi) açar. Kart boştayken **standa konmuş** figürler için hikâyeleri
  önceden hazırlayıp flash'a saklar (hikâye kuyruğu, 16 aday + seçici).
- **Seri monitörden** (bilgisayarla deneme, bkz. **4**): test komutları çalışır (geliştirme içindir).

Şu an yüklenecek model: **c3ft_karma** (`modeller/c3ft_karma/model.bin`, 10,3 MB; C3: d192, 12 katman, FFN 512, PLE 56,
V16384) — ürün modeli (10 bin hikâyeli karma veri; kör kıyasta 1030s2'yi geçti, `degerlendirme/urun_kiyas_karma`).
Figürler ve yerleri `data/urun_kartlari.json`'dan; üretim ve seçim bilgisayardaki `degerlendirme/urun_uret.py` ile
aynıdır (istem, isim süzgeci, plan modu, seçici; bkz. **Geliştirici notları**).

> `model.bin` depoda (ZIP'te de var): `modeller/c3ft_karma/model.bin` (SHA-256 `modeller/SHA256SUMS`'ta). Tokenizer C2
> ile aynıdır (`modeller/c2_tokenizer.json`).

## Gerekenler

- ESP32-S3-DevKitC-1 **N16R8** (16 MB flash, 8 MB PSRAM) ve USB kablosu
- Ürün parçaları (bağlantılar **6**): MAX98357A + hoparlör, INMP441 mikrofon, RC522 NFC okuyucu + NTAG213/215
  etiketler (figür tabanları, ayar kartı), WS2812B halka + 74AHCT1G125 + 330 Ω + 1000 µF, 5 V 2 A USB-C adaptör
- [Arduino IDE 2](https://www.arduino.cc/en/software) (Windows, Mac ya da Linux)
- Python 3 (model dosyasını yüklemek için `esptool`): `pip install esptool`
- Bu depo: GitHub'da `yusuf7855/hikaye-oyuncak`, dal `claude/wonderful-pasteur-x7seiq` → **Code → Download ZIP**
  (ya da `git clone -b claude/wonderful-pasteur-x7seiq https://github.com/yusuf7855/hikaye-oyuncak.git`)

## 1. Arduino IDE'yi hazırlayın (bir kez)

1. **File → Preferences → Additional boards manager URLs** alanına ekleyin:
   `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
2. **Tools → Board → Boards Manager**: "esp32" arayın, **esp32 by Espressif Systems** (3.x) kurun.

## 2. Yazılımı yükleyin

1. Arduino IDE'de `firmware/hikaye_oyuncak/hikaye_oyuncak.ino` dosyasını açın.
2. **Tools** menüsünde şunları seçin:

   | Ayar | Değer |
   |---|---|
   | Board | **ESP32S3 Dev Module** |
   | Flash Size | **16MB (128Mb)** |
   | PSRAM | **OPI PSRAM** |
   | Partition Scheme | **Custom** (çizim klasöründeki `partitions.csv`: uygulama 1,75 MB, model **0x1D0000**, ses 0xBB0000, kuyruk 0xFE0000) |
   | CPU Frequency | 240MHz |
   | USB CDC On Boot | **Enabled** (kartın "USB" yazan girişini kullanıyorsanız); "COM/UART" girişinde **Disabled** |
   | Erase All Flash Before Sketch Upload | **Disabled** (açık olursa model silinir) |
   | Port | kartın portu (Windows'ta COM3, COM5 gibi) |

3. **Library Manager**'dan **MFRC522** kütüphanesini (GithubCommunity, 1.4.x) kurun (NFC okuyucu RC522).
4. **Upload** (→) düğmesine basın. Derleme birkaç dakika sürebilir. (Bilgisayarda Arduino çekirdeği 3.3.12 ile
   derlendi: uygulama 1 690 224 B, 1,75 MB bölümün %92'si; statik RAM 153 820 B.)

## 3. Model dosyalarını yükleyin (bir kez; model değişince tekrar)

Flash düzeni (`partitions.csv`):

| Bölüm | Adres | Boyut | İçerik |
|---|---|---|---|
| nvs | 0x9000 | 20 KB | ayarlar: ad, ses, uyku, halka, çekilince, müzik, tanınmış oyuncaklar |
| factory (uygulama) | 0x10000 | 0x1C0000 (1,75 MB) | Arduino'nun yüklediği yazılım (1 690 224 B, %92) |
| model | **0x1D0000** | 0x9E0000 (9,9 MB) | LLM `model.bin`: C3 c3ft_karma 10 331 252 B (0x9DA474), pay 23 436 B |
| ses | **0xBB0000** | 0x430000 (4,19 MB) | ses modeli `ses.bin` (4 344 208 B; pay 46 704 B; `ses/disa_aktar.py` üretir) |
| kuyruk | 0xFE0000 | 0x20000 (128 KB) | hazır hikâyeler: 32 yuva × 4 KB (yazılım kendisi doldurur; yüklenecek dosya yok) |

> **Ekim 2026 (ayar modu) değişikliği — model yeniden yüklenmeli:** Wi-Fi + WebServer uygulamayı ~0,6 MB büyüttü
> (1 MB'a sığmaz). Uygulama 1,75 MB oldu; model bölümü `model.bin`'in boyuna indirildi ve **0x110000'dan 0x1D0000'e
> kaydı**. Modeli 0x110000'da tutmak mümkün değildi: uygulama hep 0x10000'dan başlayıp modelden önce durduğu için
> 0x110000'daki model uygulamayı 1 MB'ta tutar (uygulamayı modelden sonraya koymak da sığmıyor: 16 MB'ta model
> 9,9 + ses 4,2 + uygulama 1,75 MB). **ses adresi değişmedi** (bölüm 64 KB kısaldı, ses.bin yine sığar). Kuyruk
> flash'ın sonuna taşındı ve 32 yuvaya indi (yalnız tanınmış figürler için doldurulduğundan yeter); coredump bölümü
> kaldırıldı (yer yok; çökmede yalnız seri porttaki döküm kalır). Eski bir kartta: yazılımı (Partition Scheme
> **Custom**) ve `model.bin`'i **0x1D0000**'e yeniden yükleyin; `ses.bin`'e dokunmak gerekmez.

Kart takılıyken, depo klasöründe bir komut penceresi açıp (portu kendinizinkiyle değiştirin):

```bash
# Windows
python -m esptool --chip esp32s3 --port COM5 --baud 921600 write_flash 0x1D0000 modeller\c3ft_karma\model.bin 0xBB0000 ses.bin
# Mac / Linux
python3 -m esptool --chip esp32s3 --port /dev/ttyACM0 --baud 921600 write_flash 0x1D0000 modeller/c3ft_karma/model.bin 0xBB0000 ses.bin
```

`ses.bin` henüz yoksa komuttan `0xBB0000 ses.bin` kısmını çıkarın: kart konuşmadan çalışır (hikâyeler seri porta
yazılır). Yalnız ses modelini değiştirmek için: `... write_flash 0xBB0000 ses.bin`.

Yükleme ~1–1,5 dakika sürer. Kart yükleme modundan çıkmazsa **RST** düğmesine basın. (Sıra önemli değil: yazılım ve
modeller flash'ın farklı yerlerine yazılır.) Yazılım ile model birlikte değişti: eski yazılım yeni modelle (ya da
tersi) çalışmaz. Model değişince kuyruktaki eski hikâyeler kendiliğinden geçersiz sayılır (imza: modelin parmak izi +
istem tablosu) ve yeniden üretilir. Kuyruğu elle boşaltmak için ayar sayfasında "Hikâyeleri sil", seri monitörde
`k sil` ya da `python -m esptool --chip esp32s3 --port COM5 erase_region 0xFE0000 0x20000`.

## 4. Deneyin

**Tools → Serial Monitor**, hız **115200**, satır sonu **Newline**. Kart açılışta şuna benzer yazar:

```
=== Hikâye Oyuncağı ===
model: V=16384 D=192 L=12 H=4 F=512 P=56 bağlam=224
PSRAM: KV + logits 4.06 MB, süzgeç 0.12 MB, çekirdek 4-bit 2.93 MB (int8 5.65 MB gerekirdi)
head: 4-bit hızlı yol, kodlar flash'ta (1.50 MB)
PSRAM toplam (LLM): 7.25 MB
model.bin: 10331252 B, parmak izi fp=00ea3e55
...
kuyruk: 32 yuva (0x20000 @ 0xFE0000), hazır 0 hikâye | figür başına 2 (en çok 6), K=5 | arka plan açık
stand NFC: RC522 | mikrofon: açık (Merhaba Eko) | halka: 35 LED, GPIO 18 | ses seviyesi 5/7 (en çok 7) | bekçi 30 s
ayarlar: ad "", uyku 20 dk, parlaklık 60, çekilince cümle sonunda dur, müzik kutusu açık
tanınmış oyuncaklar: (yok: standa konan oyuncak tanınır)
```

`model.bin` satırındaki **fp=00ea3e55** doğru model yüklendiğini gösterir. Figür ve yer numaraları (`?` listeler):

| No | Figür | Yerleri |
|---|---|---|
| 1 | Niloya | 1 orman, 2 dağ, 3 ev, 4 park |
| 2 | Maşa | 1 orman, 2 dağ, 3 ev |
| 3 | Pepee | 1 orman, 2 deniz, 3 park, 4 ev |
| 4 | Keloğlan | 1 orman, 2 dağ, 3 ev, 4 şato |
| 5 | Doru | 1 dağ, 2 orman, 3 park |
| 6 | Hayri | 1 deniz, 2 orman, 3 park, 4 ev |
| 7 | Şakir | 1 deniz, 2 orman, 3 park, 4 ev |
| 8 | Elsa | 1 dağ, 2 orman, 3 deniz, 4 şato |
| 9 | Chase | 1 dağ, 2 deniz, 3 orman, 4 park, 5 ev |
| 10 | Örümcek Adam | 1 deniz, 2 park, 3 ev |
| 11 | Hello Kitty | 1 park, 2 orman, 3 ev |

Yer numarası figürün kendi listesindendir (her figür yalnız kartındaki yerlerde eğitildi). Sonra yazın:

| Yazılan | Anlamı |
|---|---|
| `8 4` | Elsa, şato — kuyrukta hazır Elsa/şato hikâyesi varsa hemen okunur, yoksa canlı yazılır (standı ve tanınmışlığı atlar: geliştirme) |
| `8` | Elsa, herhangi bir yer — en eski hazır hikâye, yoksa sıradaki yerinde canlı |
| `1 2` | Niloya, dağ |
| `8 4 8` | **her zaman** 8 aday üretir (en çok 16), seçiciyle en iyisini yazar ve okur (test; kuyruğa bakmaz) |
| `8 4 1` | her zaman canlı |
| `?` | figür ve yer listesi |
| `b` | hız testi: head'in üç yolunu ölçer, token başına ms dökümünü yazar, en hızlısını seçer |
| `k` | tanınmış oyuncaklar ve kuyruk durumu: figür figür hazır hikâye sayısı ve yerleri |
| `k+` / `k-` | boşta arka plan üretimini aç / kapat (kalıcı) |
| `k sil` | hazır hikâyelerin hepsini sil (boşta yeniden üretilir) |
| `v+` / `v-` / `v 3` | ses seviyesi (0–7, en çok ayardaki sınır) |
| `n` | standdaki etiket (UID, nfc_no) |
| `n koy 8` / `n koy 12` / `n koy 200` / `n koy bos` / `n koy uid 04A1B2C3` / `n kaldir` | yalnız taslak okuyucuda (`NFC_OKUYUCU 0`): standa etiket koyma taklidi (Elsa, Ay Dede, ayar kartı, boş NTAG, kayıtsız etiket) |
| `w uyandirma` `w dur` `w devam` `w baska` `w bir_daha` `w sesi_ac` `w sesi_kis` | sesli komut taklidi |
| `a` / `a kapat` | ayar modunu aç / kapat (ayar kartı yerine) |
| `sahip` / `sahip +8` / `sahip -8` / `sahip hepsi` / `sahip yok` | tanınmış oyuncaklar (nfc_no ile) |
| `h` | halkanın durumu, akım tahmini |
| `s Merhaba` / `o` | metni oku / hikâyeyi sesli okumayı aç-kapa |
| `u` | 10 s hafif uyku denemesi (akım ölçmek için; USB seri bağlantısı kopabilir) |

Aday sayısı yazılmazsa kuyruk önce denenir, hazır yoksa **canlı okuma**: model yazdıkça her cümle biter bitmez okunur
(seçici yok, bitmesi beklenmez). Boşta (son komuttan 5 s sonra; ilk açılıştan itibaren) kart kuyruğu bütün figürler
için doldurmaya başlar (standa konmuş olanlar önce) ve seri porta `[kuyruk] Elsa | şato: 5 aday, puan -2.13 -> yuva 5
...` gibi satırlar yazar; seri monitöre bir şey yazınca o aday bırakılır ve komutunuz hemen çalışır (iş sonra kaldığı
adaydan sürer). Testte bunu istemezseniz `k-`. Ürün: kuyruğa hazırlarken **K=5** aday, en iyisi (ürün sahibinin
kararı, 15 Ekim 2026). Figürün hikâyesinde başka figürlerin ve onların
yanlarının adları (ör. Elsa'da "Niloya", "Şila") isim süzgeciyle hiç yazılamaz; figürün kendi kadrosu (Elsa için
Anna, Olaf, Kristoff, Sven) serbesttir.

Her hikâyenin sonunda `token/s` ve bir **profil** satırı yazar: token başına ms olarak girdi, dikkat, FFN, PLE,
head ve örnekleme. **Bu satırları, `b` çıktısını ve birkaç hikâyeyi bana gönderin.**

### Hız (ilk ölçüm ve düzeltme)

İlk kart denemesi (C2) 1,6 token/s verdi (hikâye başına 80–110 s). Neden: head (16 384 satır, 4-bit, flash'ta) tek
çekirdekte ve eleman başına nibble ayıklayan yavaş yoldan hesaplanıyordu; çekirdek katmanlar ise int8 ve iki
çekirdekteydi. Şimdi (`hiz.h`):
- head için hızlı 4-bit çekirdek (bayt başına iki nibble, "-8" grup başına bir kez; sonuçlar eski yolla bit bit
  aynı, `tools/hiz_test.c`),
- head iki çekirdeğe bölünür,
- yer varsa head kodları (1,3 MB) açılışta PSRAM'e kopyalanır.
Açılışta `head: 4-bit hızlı yol, kodlar PSRAM'de` satırı görünür. `b` komutu eski ve yeni yolları karşılaştırır.
- Çok adayda istem (~15 token) bir kez işlenir: sonraki adaylar istemin KV'sini ve son logit'lerini yeniden kullanır
  (sonuç aynı, aday başına ~%10 daha az hesap).

**C3 (c3ft_karma) ile:** çekirdek C2'nin ~1,9 katı (5,7 M parametre), int8 açılımı (5,65 MB) float KV ile (4,13 MB)
8 MB PSRAM'e sığmaz. Bu yüzden çekirdek dosyadaki gibi **4-bit** olarak PSRAM'e kopyalanır (2,93 MB, ölçekler float)
ve hiz.h'nin hızlı 4-bit yolu (q4f) iki çekirdekte çalışır; sonuçlar int8 yolla bit bit aynı. Head (1,5 MB) flash'ta
kalır (PSRAM'de yer yok). Açılışta `çekirdek 4-bit` yazar. Beklenen hız ≈3–4 token/s (docs/ESP32_BUTCE.md C3 tahmini
3,7; ölçülmedi): K=8 aday ≈5–7 dakika. **İlk ölçümde `b` çıktısını ve birkaç hikâyenin profil satırını gönderin.**

## 5. Ses (hikâyeyi sesli okuma)

**Bağlantı** (MAX98357A I2S yükselteç kartı, 4–8 Ω hoparlör):

| MAX98357A | ESP32-S3 |
|---|---|
| VIN | 5V (ya da 3V3; 5V daha yüksek ses) |
| GND | GND |
| BCLK | GPIO4 |
| LRC | GPIO5 |
| DIN | GPIO6 |
| SD | GPIO7 (konuşmazken LOW: yükselteç uyur; HIGH'da iki kanalın ortalaması) |
| GAIN | boş (9 dB) |

Ses 16 kHz, 16 bit, mono; I2S'te iki kanala da aynı örnek gönderilir (SD ayarı ne olursa olsun duyulur).
Konuşurken standın halkası okunan kısmı gösterir (bkz. 6. Halka).

`ses.bin` yüklüyse açılışta `ses: akustik d=192 ... | hikâyeyi okuma: açık` satırı görünür. C3 ile LLM'den sonra
PSRAM'de ≈0,7 MB kalır; ses için ≈0,5 MB yeter. Komutlar:

| Yazılan | Anlamı |
|---|---|
| `s Bir varmış bir yokmuş.` | yazılan metni okur |
| `o` | üretilen hikâyeyi otomatik okumayı aç/kapa (ses modeli varsa açık başlar) |

Hikâye cümle cümle okunur: ilk cümle hesaplanırken çalmaya başlar, sonraki cümle çalarken hesaplanır. Okurken seri
monitöre bir şey yazıp gönderirseniz (ya da "Merhaba Eko, dur" denirse, oyuncak çekilirse: ayara göre) ses susar. Her okumadan sonra
`[ses: X s konuşma, Y s hesap = Z s hesap / s ses]` yazılır: **Z 1'den küçükse gerçek zamandan hızlıdır**; bu satırı
bana gönderin.

**ses.bin üretmek** (eğitim bitince, depo klasöründe):

```bash
python ses/disa_aktar.py --akustik ses_calisma/akustik/son.pt --vocoder ses_calisma/vocoder_gta/son.pt \
    --cikti ses.bin --altin ses_altin.bin
```

(GTA ince ayarı yoksa `ses_calisma/vocoder/son.pt`.) Boyutu ve bölüme sığdığını yazar. Kartın C kodunun aynı modelle
PyTorch'la aynı sonucu verdiğini bilgisayarda denemek için:
`python firmware/hikaye_oyuncak/tools/ses_test.py --akustik ses_calisma/akustik/son.pt --vocoder ses_calisma/vocoder_gta/son.pt`

## 6. Oyuncak olarak (bilgisayarsız)

Ürün tanımı: `docs/URUN_TANIMI.md` (bağlayıcı). **Düğme yok.** Çocuk oyuncağını standa koyar; kart o oyuncağın
hikâyesini okur. Sesli komutlar "Merhaba Eko" ile. Ayarlar ebeveynin "ayar kartı"yla telefondan.

### Bağlantılar (pin haritası, kesin)

Pinlerin hepsi `donanim.h`'de; değişirse `docs/URUN_TANIMI.md` ve bu tablo birlikte değişir.

| Parça | Sinyal | ESP32-S3 GPIO | Not |
|---|---|---|---|
| MAX98357A hoparlör yükselteci (I2S0) | BCLK / LRC / DIN / SD | 4 / 5 / 6 / 7 | VIN 5V, GND; SD: konuşmazken LOW (yükselteç uyur) |
| INMP441 mikrofon (I2S1) | SCK / WS / SD | 15 / 16 / 17 | VDD 3V3, GND, **L/R → GND** (sol kanal) |
| RC522 NFC okuyucu (SPI, **3,3 V**) | SCK / MISO / MOSI / SDA(SS) / RST | 12 / 13 / 11 / 10 / 9 | IRQ boş; 5 V'a bağlamayın |
| NeoPixel halka (WS2812B) | DIN | 18 | 74AHCT1G125 seviye çevirici (3,3 → 5 V) + 330 Ω seri direnç; halka girişinde 1000 µF; halka 5 V'tan beslenir |
| Kart üstü RGB LED | — | 48 (38) | kullanılmaz |

Kullanılmayan uçlar: 0, 3, 45, 46 (açılış), 19/20 (USB), 26–37 (flash/PSRAM), 43/44 (UART). Güç: USB-C 5 V / 2 A
adaptör. PN532 okuyucu da kullanılabilir (`NFC_OKUYUCU 2`): aynı SPI uçlarına, modülün anahtarları SPI'ye alınarak
(RSTPDN → GPIO9). Geliştirme için düğmeler `DUGME_ACIK 1` ile açılır (FİGÜR 1, YER 2, OYNAT 14; GND'ye).

Gereken Arduino kütüphanesi: **MFRC522** (GithubCommunity, 1.4.x) — Library Manager'dan. PN532 için ayrıca
**Adafruit PN532** (+ Adafruit BusIO). Wi-Fi, WebServer, DNSServer, ESP_I2S, RMT çekirdekle gelir; halka için ayrı
kütüphane yok (çekirdeğin `rmtInit`/`rmtWrite`'ı; Adafruit_NeoPixel gerekmez).

### Kullanım

| Ne olur | Oyuncak ne yapar |
|---|---|
| Oyuncak standa kondu | Halka figürün renginde dolar (0,6 sn) → "Merhaba Emre, şimdi sana Niloya'nın hikâyesini okuyacağım." → en eski hazır hikâye hemen okunur. Hazır yoksa **canlı okuma**: selam çalarken model yazmaya başlar, her cümle biter bitmez okunur (beklemek yok, aday seçimi yok). Figürün yerleri kendiliğinden döner. |
| İlk açılış / boşta | Kart boştayken bütün figürler için hikâye hazırlar (her biri 5 aday, en iyisi; standa konmuş oyuncaklar önce). Okunan hikâye her zaman standdaki oyuncağınkidir. |
| Canlı okurken "Dur" | Anlatım susar, hikâye sessizce tamamlanır; "Devam" kaldığı cümleden sürer. |
| Oyuncak standdan alındı | Ayara göre: cümle bitince durur (varsayılan) / hemen durur / hikâyeyi bitirir. |
| Standda oyuncak yok | Hikâye okunmaz; "başka", "bir daha", "devam" denirse "Önce bir oyuncağını standa koy." |
| Ay Dede (gece figürü) kondu | Ninni modu (aşağıda). |
| Ayar kartı kondu | Ayar modu (aşağıda). |

**Sesli komutlar** — önce "Merhaba Eko" (halka: beyaz dönen nokta, okuma kısılır), sonra ~4 sn içinde:

| Komut | Çocuğun diyebileceği | Ne olur |
|---|---|---|
| DUR | "Dur", "Dursun", "Sus" | Okuma hemen durur; kaldığı cümle saklanır |
| DEVAM | "Devam", "Devam et", "Hadi" | Duran okuma kaldığı cümleden sürer; duran yoksa aynı oyuncağın yeni hikâyesi |
| BAŞKA | "Başka", "Başka masal", "Bunu sevmedim" | Aynı oyuncağın başka hikâyesi |
| BİR DAHA | "Bir daha", "Yine", "Tekrar" | Son hikâye baştan |
| SESİ AÇ / KIS | "Sesini aç" ... / "Sesini kıs" ... | Bir seviye (okuma durmaz); halka 2 sn ses düzeyini gösterir |

Hiçbir komut figür seçmez. Anlaşılan komut: kısa yeşil; "Merhaba Eko"dan sonra komut gelmezse kısa turuncu.
Mikrofon INMP441, I2S1 16 kHz; tanıma `kws.h` (ayrı geliştirme, `tools/kws_test.py`). Seri monitörden taklit:
`w uyandirma`, `w dur`, `w devam`, `w baska`, `w bir_daha`, `w sesi_ac`, `w sesi_kis`.

### Halka

| Durum | Halka |
|---|---|
| Açılış | Gökkuşağı tek tur, sonra söner |
| Boşta, oyuncak yok | Çok sönük nefes alan beyaz (ayardan kapatılabilir) |
| Oyuncak kondu | Figürün rengiyle 0,6 sn'de dolar (renkler `data/figur_donanim.json`) |
| Selamlama / okuma | Figür renginde; okunan cümle oranı kadar LED dolu, kalanı sönük; parlaklık konuşma sesiyle hafifçe dalgalanır |
| Canlı hikâye yazılıyor | Figür renginde dönen nokta |
| Okuma bitti, oyuncak standda | 3 sn dolu, sonra figür renginde çok sönük nefes |
| "Merhaba Eko" duyuldu | Beyaz dönen nokta (dinliyorum) |
| Komut anlaşıldı / anlaşılmadı | Kısa yeşil / kısa turuncu yanıp sönme |
| Ses aç/kıs | 0..7 düzeyi kadar beyaz LED, 2 sn |
| Arka planda hikâye hazırlanıyor | Çok sönük, yavaş dönen figür rengi nokta (ayardan kapatılabilir) |
| Ninni modu (Ay Dede) | Gece mavisi, yavaş parıldayan yıldızlar; zamanlayıcı dolunca 60 sn'de söner |
| Ayar modu | Turkuaz nefes |
| Hata (model yok, Wi-Fi açılamadı) | Kırmızı yanıp sönme |

LED sayısı `HALKA_LED_SAYISI` (varsayılan 35; ürün sahibi doğrulayacak). Parlaklık tavanı `HALKA_PARLAKLIK_SINIR`
(%25), ayardaki parlaklık bu tavanın yüzdesidir; kare başına akım tahmini (kanal başına 20 mA × değer/255)
`HALKA_AKIM_SINIR_MA`'yı (600 mA) aşarsa kare kısılır (%25'te 35 beyaz LED ≈ 527 mA). Kareler ayrı, düşük
öncelikli bir görevde 30 kare/s hesaplanır ve RMT ile (10 MHz, GRB) yollanır: LLM ve ses beklemez.

### Ninni modu: gece figürü "Ay Dede" (nfc_no 12)

- Selam: "İyi geceler Emre, şimdi sana bir ninni söyleyeceğim." Sonra ninniler art arda okunur: **yavaş** (%75 hız),
  **alçak** (−2 yarım ton), **kısık** (×0,6) ve cümle aralarında 0,9 sn (ses.h `hiz`, `perde_kaydir`, `kazanc`;
  varsayılanlarla ses eskisiyle bayt bayt aynı).
- İsteğe bağlı çok kısık **müzik kutusu** (kartta sentezlenir, `muzik_kutusu.h`; ayardan kapatılır).
- **Uyku zamanlayıcısı** (ayar: 10/20/30 dk) dolunca okunan ninni bitirilir; halka ve müzik **60 sn'de söner**; sonra
  mikrofon, yükselteç ve halka kapanır, kart hafif uykuda standı yoklar. Standa (yeniden) bir oyuncak konunca uyanır.
  Ay Dede erken alınırsa ninni modu biter.
- İçerik: hikâye modeli "gece" figürünü henüz bilmiyor; ninniler kartta gömülü (`yerlesik.h`, 8 kısa metin, sırayla).
  Model bu figürle eğitilip `tools/basliklar.py` yeniden çalıştırılınca `generated/figur_donanim.h`'de
  `DONANIM_MODEL` değişir ve Ay Dede kendiliğinden kuyruk/üretim yoluna geçer (kod değişmez).

### Ayar kartı ve ayar modu

Ayar kartı = kaydında **nfc_no 200** yazan etiket. Standa konunca:

1. Halka turkuaz nefes alır; kart Wi-Fi erişim noktası açar: ad **`Masalci-Ayar-XXXX`** (XXXX: kartın MAC'inin son
   iki baytı), **WPA2**, şifre her açılışta yeni **8 haneli** sayı; oyuncak şifreyi **sesli iki kez söyler** (seri
   porta da yazar).
2. Telefon ağa bağlanınca ayar sayfası kendiliğinden açılır (DNS her adı karta yönlendirir; açılmazsa tarayıcıda
   `http://192.168.4.1`). İnternet hiç kullanılmaz.
3. Sayfada: çocuğun adı (en çok 20 harf, yalnız harf ve boşluk; Türkçe harfler), en yüksek ses (1–7), uyku
   zamanlayıcısı (10/20/30 dk), halka parlaklığı, boşta nefes ışığı, hazırlık ışığı, ninnide müzik kutusu, oyuncak
   alınınca ne olsun, **oyuncak tanıt**, **hikâyeleri sil** (isteğe bağlı: tanınan oyuncakları da unut). Doğrulama
   kartta (`ayarlar.h`); geçersiz form hiç uygulanmaz. Ayarlar NVS'te (Preferences) kalır.
4. Wi-Fi yalnız ayar modunda açıktır; kapanır: ayar kartı alınınca, sayfadan "Bitir"le ya da **10 dakika** sonra
   ("oyuncak tanıt" kullanıldıysa kart alınması beklenen bir adımdır: o zaman stand 1 dk boş kalınca kapanır). Ayar
   modunda arka plan üretimi ve sesli komutlar durur.

**Neden açık ağ değil, WPA2 + söylenen şifre?** Ayar sayfası çocuğun adını gösterir ve değiştirir, etiket yazar,
hikâyeleri siler. Açık ağda o 10 dakika içinde yakındaki herhangi biri (komşu, okul servisi) bağlanabilir ve trafik
(çocuğun adı) şifresiz geçer. WPA2 trafiği şifreler; şifrenin her seferinde yeni olması ve **yalnız oyuncağın
yanındakinin duyacağı şekilde söylenmesi**, ayar kartına ve oyuncağa fiziksel olarak erişen yetişkini (kartı
standa koyan kişi) yetkili sayar; etikete/kutuya basılı sabit şifre gerekmez, kaybolmaz, kopyalanamaz. En çok 2
bağlantı, 10 dakika sınırı ve kartın çekilmesiyle kapanma açık kalma süresini kısaltır. Bedeli: ebeveyn 8 rakam
yazar (yılda birkaç kez).

### Oyuncak tanıtma (figür etiketlerini programlamak)

Figür tabanındaki NTAG213/215 etiketin kullanıcı belleğine (sayfa 4–5) 8 baytlık kayıt yazılır (`etiket.h`):
`"EKO"` + sürüm (1) + nfc_no (2 bayt) + CRC-16/CCITT. Kart her yeni etikette kaydı okur; kayıt yoksa ya da bozuksa
UID tablosuna (`nfc.h NFC_TABLO`) düşer; o da yoksa "bilinmeyen etiket" (kısa turuncu).

1. Ayar kartını standa koyun, telefondan ayar sayfasını açın.
2. "Oyuncak tanıt"ta figürü seçin (yedek ayar kartı yazmak için "Ayar kartı"), **Etikete yaz**.
3. Ayar kartını alın, yeni figürü (ya da boş etiketi) 60 sn içinde standa koyun. Kart yazar, geri okuyup doğrular;
   sayfada ve sesle sonucu söyler ("Tamam, bu artık Niloya."). Figür tanınmış sayılır.

NFC numaraları ve renkler `data/figur_donanim.json`'da (sürüm 2: 11 figür + Ay Dede 12; ayar kartı 200). Numara
asla yeniden kullanılmaz. RC522 kitindeki MIFARE Classic kartlar NTAG değildir: onlara kayıt yazılamaz (UID
tablosuyla kullanılabilir).

### Hikâye kuyruğu

- Boşta (son olaydan 5 s sonra) kart, **tanınmış** figürlerden hazır hikâyesi en az olanı seçip sıradaki yeri için
  **16 aday** üretir, seçiciyle en iyisini flash'a yazar. 32 yuva tanınmış figürlere bölünür: figür başına
  `min(6, (32 − 2) / tanınmış figür sayısı)` (tek figür 6, 11 figür 2). Yeni figür tanınınca hedef düşer; yer
  gerekirse fazlası olan figürün en eski hikâyesi bırakılır.
- Oyuncak konunca o figürün **en eski** hazır hikâyesi hemen okunur ve tüketilir; yerine boşta yenisi üretilir. Hazır
  yoksa yarım kalmış bir kuyruk işinin o ana kadarki en iyisi, o da yoksa canlı (K=1).
- Üretim aday aday ilerler; oyuncak konunca (ya da sesli komut, seri komut) o aday bırakılır, iş sonra sürer. Yazma
  güç kesilmesine dayanıklıdır, yuvalar sırayla döner (aşınma dengesi).

### Güç

- **Hafif uyku** yalnız ninni modunun sonunda (mikrofon kapalı): 0,4 s dilimler, aralarda stand yoklanır. Normalde
  mikrofon "Merhaba Eko"yu dinlediği için kart uyumaz. USB seri monitör bağlıyken uyunmaz.
- **Ses seviyesi:** yazılımla 8 seviye (~3 dB), en yüksek seviye ayardan sınırlanır; sesli komutla ya da `v+` `v-`.
- **Güç düşmesi (brownout):** LLM + PSRAM + flash ≈ 250–350 mA, hoparlör tepe 0,5–1 A, halka en çok 600 mA (yazılım
  sınırı). 5 V 2 A adaptör kullanın; MAX98357A ve halka girişine 470–1000 µF. Açılışta `UYARI: güç düşmesiyle` görülürse
  ses o açılışta 4'e iner.
- **Görev bekçisi:** ana döngü 30 s beslenmezse kart yeniden başlar (uzun üretimde her token'da beslenir).

## Sorun giderme

| Belirti | Çözüm |
|---|---|
| `model bölümü yok` | Partition Scheme **Custom** seçilmemiş; seçip yazılımı yeniden yükleyin. |
| `model okunamadı` | model.bin yüklenmemiş ya da yanlış adrese yüklenmiş: 3. adım, adres **0x1D0000** (Ekim 2026'dan önce 0x110000'dı: yeniden yükleyin). |
| `HATA: PSRAM ayrılamadı` | PSRAM ayarı **OPI PSRAM** değil. |
| `HATA: tokenizer/model uyuşmuyor` ya da anlamsız metin | Eski model (C2) ya da yanlış dosya yüklü: `fp=00ea3e55` olmalı. |
| `çekirdek flash'ta 4-bit (PSRAM yetmedi, yavaş)` ya da `UYARI: isim süzgeci için PSRAM yok` | PSRAM eksik görünüyor; açılış çıktısını bana gönderin. |
| `ses bölümü yok` | Yeni `partitions.csv` ile yazılım yeniden yüklenmemiş (Partition Scheme **Custom**). |
| `kuyruk bölümü yok` | Aynı: Partition Scheme **Custom** ve bu klasördeki `partitions.csv` ile yeniden yükleyin. Kart yine çalışır, hikâyeler hep canlı yazılır. |
| `stand NFC: RC522 BULUNAMADI` | RC522 kabloları (SCK 12, MISO 13, MOSI 11, SDA 10, RST 9), **3,3 V** besleme; MFRC522 kütüphanesi. Seri monitörde `n` standı gösterir. |
| Oyuncak konunca bir şey olmuyor | Seri monitörde `(stand: etiket ...)` satırı var mı? `bilinmeyen etiket` ise etiketi ayar sayfasından "oyuncak tanıt" ile yazın. Etiket okuyucuya 1–3 cm yakın olmalı. |
| "Merhaba Eko" duyulmuyor | INMP441: SCK 15, WS 16, SD 17, **L/R GND'ye**, 3V3. Açılışta `mikrofon: açık` yazmalı. Seri monitörde `w uyandirma` ile tepkiyi deneyin. |
| Halka yanmıyor ya da renkler karışık | DIN GPIO18 → seviye çevirici (74AHCT1G125) → 330 Ω → halka DIN; halka 5 V ve GND ortak; `HALKA_LED_SAYISI` doğru mu? Seri monitörde `h`. |
| Ayar ağı görünmüyor | Ayar kartı standda mı (`(stand: ... nfc_no 200)`)? `[ayar modu] Wi-Fi: Masalci-Ayar-...` satırı ve şifre seri portta da yazar. `HATA: Wi-Fi erişim noktası açılamadı` ise açılıştaki boş SRAM satırını bana gönderin. |
| Ayar sayfası kendiliğinden açılmıyor | Tarayıcıda `http://192.168.4.1` yazın (bazı telefonlar "internet yok" diye ağdan çıkar: "bağlı kal" deyin). |
| Kart kendi kendine yeniden başlıyor | Açılıştaki `UYARI` satırına bakın: brownout ise güç (bkz. **6 → Güç**), değilse satırı bana gönderin. |
| `ses: ses.bin değil (sihir): konuşma kapalı` | ses.bin yüklenmemiş ya da yanlış adrese: 3. adım, adres **0xBB0000**. |
| `hoparlör: açık, yalnız bip` | ses.bin yok ya da yanlış adreste; hikâyeler seri porta yazılır. |
| `ses: bellek ayrılamadı` | PSRAM/SRAM yetmedi (C3'te LLM'den sonra ≈0,7 MB PSRAM kalır); bana açılış çıktısını gönderin (`SES_MAX_SEMBOL`, `SES_PARCA` küçültülebilir). |
| Ses yok ama `[ses: ...]` satırı geliyor | Kablolar: BCLK 4, LRC 5, DIN 6, GND ortak; hoparlör MAX98357A'nın + ve − ucunda. |
| Seri monitör boş | USB CDC On Boot ayarı kullandığınız USB girişine uymuyor; değiştirip yeniden yükleyin. |
| Türkçe harfler bozuk | Seri monitör UTF-8 göstermiyor olabilir; Arduino IDE 2 gösterir. |

## Geliştirici notları

- `generated/` klasörü `tools/basliklar.py` ile üretilir: `vocab.h` (tokenizer tablosu), `istemler.h` (11 figür,
  41 figür × yer istemi, figür başına isim süzgeci adları, seçici tabloları) ve `runtime/llm.h`, `runtime/ornekle.h`,
  `runtime/isim_suzgec.h` kopyaları. Kaynak her zaman `degerlendirme/urun_uret.py` (KARTLAR/FIGURLER, istem,
  kadro_disi + KELIME_BASI, figur_adlari, ISIM_KELIME, TAKINTI_HARIC). Kartlar ya da urun_uret değişince:
  `python firmware/hikaye_oyuncak/tools/basliklar.py` (varsayılan tokenizer `hf_c3ft_karma/tokenizer.json`).
- Üretim = `urun_uret.aday_uret` (gen ile aynı ayarlar): istem `<|endoftext|>Karakter: F | Yer: Y\nSorun:` (Yan alanı
  yok, ürün varsayılanı), plan modu (gen -S 199), istem tekrar penceresine girmez (gen -P), gövdede satır sonu
  yasağı (gen -N 199,9491), sıcaklık 0.5, top-k 40, tekrar 1.1, en çok 230 token. İsim süzgeci (gen -Y,
  `isim_suzgec.h`): figür başına `suzgec_dosyasi`'nın ad listesi (`$` = kelime başı olabilen ad), istem token'ları da
  süzgece verilir; token baytları vocab.h'den (gen -Y dosyasında `<|endoftext|>` metniyle yazıldığı için o token
  istemler.h'de ayrıca), dizi açılışta PSRAM'de (128 KB). Gövdenin ortalama lp'si gen -l'nin 4 basamaklı değerlerinden
  ve Python 3.12 `sum()`'ı gibi telafili toplamla alınır: puanlar urun_uret'le birebir.
- Seçici: `secici.h` `secici_urun_puanla`, `urun_uret.puanla`'nın birebir C kopyası (sec.py kuralları + ISIM_KELIME
  muafiyeti + kadro_cezalari: kendine seslenme, "X X", yanların kendi kendine, kartta olmayan ad + takinti_cezasi +
  yer + güvenlik). Aday satırında sıfır olmayan kural cezaları parantez içinde yazılır. Sözlük `generated/sozluk.h`
  (~290 KB flash; `tools/sozluk_paketle.py` ile `degerlendirme/sozluk.pkl`'den). Eşitlik testi (c3ft_karma, 1030s2,
  1030, 740 kıyaslarının bütün adayları = 5248 + bozulmuş sentetik adaylar; puan 1e-9, kural kural ve seçim):
  `python firmware/hikaye_oyuncak/tools/secici_karsilastir.py --urun --sentetik 5000` → uyuşmazlık 0
  (`tests/test_kart_secici.py` da koşar). Eski hayvan kataloğunun seçicisi `-DSECICI_ESKI=1` ile duruyor
  (`secici_karsilastir.py` argümansız onu dener).
- Bilgisayarda kart: `tools/kart_pc/` (sahte ESP32 başlıkları, `kart_pc.cpp` çizimi olduğu gibi içerir; PSRAM
  8 315 000 B ile sınırlı ve sayılır, bölümler `partitions.csv`'den). Kartın üretim yolu ile urun_uret'in aynı vakada
  aynı hikâyeleri ve aynı seçimi verdiğini doğrular:
  `python firmware/hikaye_oyuncak/tools/kart_pc_karsilastir.py --hepsi --aday 8` (41 vaka × 8 aday: plan, metin, lp,
  puan ve seçim birebir). Kart int8 aktivasyon kullanır (`LLM_INT8_ACT`, hız için); depodaki `./gen` float
  aktivasyonla derlendiğinden karşılaştırma gen.c'nin `-DLLM_INT8_ACT` kopyasıyla yapılır (araç derler; `--float`
  ./gen ile farkı bilgi olarak yazar). Bilinen farklar: kartın bağlamı 224 (urun_uret 256; istem + plan + gövde
  230'u aşan hikâyelerde kart erken keser, karma adaylarında en uzunu ~191), kartta rastgelelik `esp_random`
  (bilgisayardaki seed'ler yok), tek adayda (K=1) plan bozulursa kart iki kez yeniden dener.
- Bellek (C3): KV float 224 konum 4,13 MB + logits 0,13 MB + süzgeç 0,13 MB + çekirdek 4-bit 2,93 MB + head ölçekleri
  0,13 MB = 7,25 MB PSRAM (8 MB'ın); head 4-bit flash'ta. C2 modeli yüklenirse çekirdek eskisi gibi int8'e açılır.
- Ses: `ses.h` (tek başlık, C/C++), `ses/model.py`'deki Akustik.uret + Vocoder'ın birebir C çıkarımı. Ağırlıklar flash'ta
  yerinde okunur (akustik 4 bit/32'lik grup, vocoder 8 bit/satır, `kuant.q_agirlik` ile aynı açma). Çözücü ve vocoder
  kare kare akar (her katman k/2 kare geçmiş tutar; tekrar hesap yok, bellek cümle uzunluğundan bağımsız): ~450 KB
  PSRAM + ~200 KB SRAM. Matris işleri LLM'in işçi göreviyle iki çekirdeğe bölünür. Metin -> sembol `ses/metin.py` ile
  aynı. Eşitlik testi (rastgele model kurar, dışa aktarır, C ile PyTorch'u karşılaştırır; süreler birebir, mel ve dalga
  ~1e-6 göreli fark): `python firmware/hikaye_oyuncak/tools/ses_test.py`
- Ürün parçaları: `donanim.h` (pinler, sabitler), `olaylar.h` (olay halkası: stand, sesli komut, düğme), `kuyruk.h`
  (flash kuyruğu: 4 KB yuva = 32 B başlık [sihir, imza, sıra, figür, yer, K, n, n_plan, puan, CRC-32, tüketildi] +
  int16 token'lar; yazma sırası sil → token → başlık → en son sihir; tüketme silmeden 4 bayt 0; tanınmış figürler:
  `kuyruk_hedef`, `kuyruk_sonraki_sahip`, `kuyruk_yer_ac`), `etiket.h` (NFC kaydı), `nfc.h` (RC522 / PN532 / taslak
  sürücü: UID, 16 B okuma, sayfa yazma; kayıt okuma + UID tablosu; tanıtma: yaz + geri oku), `selam.h` (selamlama,
  Türkçe tamlayan eki, ninni selamı, şifreyi rakam rakam), `ayarlar.h` (ayarlar, form doğrulaması, JSON),
  `ayar_sayfa.h` (gömülü sayfa), `halka.h` (durumdan kareye; tavan ve akım sınırı), `muzik_kutusu.h`, `yerlesik.h`
  (modelin bilmediği figürlerin metinleri), `generated/figur_donanim.h` (`tools/basliklar.py`, `--donanim` yalnız bunu
  yazar), `kws.h` + `generated/kws_model.h` (sesli komut; ayrı geliştirme), `dugmeler.h` (yalnız `DUGME_ACIK 1`).
  Üretim yolu (`aday_uret`) değişmedi: `kart_pc_karsilastir.py` (11 vaka × 4 aday) uyuşmazlık 0.
- Görevler: ana döngü (1. çekirdek, LLM + ses sentezi), LLM/ses işçisi (0. çekirdek, öncelik 2), çalıcı (0, 5:
  I2S0'a yazar, kazancı uygular, müzik kutusunu karıştırır), mikrofon (0, 3: I2S1 → `kws_isle` → olay halkası),
  halka (1, 1: 30 kare/s, RMT). Okurken olaylara `okuma_denetle` bakar: ses aç/kıs, "Merhaba Eko", devam yerinde
  işlenir; dur/başka/bir daha ve oyuncak çekilmesi okumayı (ayara göre hemen ya da cümle sonunda) keser, ana döngü
  sonra işler.
- Denemeler (hepsi `tests/test_kart_kuyruk.py` ile pytest'te):
  - `tools/kuyruk_test.c` (NOR flash taklidi: çöp dolu bölüm, doldurma politikası, yeniden başlatma, en eskinin önce
    çalınması, CRC, imza, her noktada güç kesilmesi, aşınma, tanınmış figürlere bölme ve yer açma),
  - `tools/dugme_test.c` (sekme, kısa/uzun, ikili basış, millis taşması),
  - `tools/urun_test.c` (etiket kaydı ve her tek bit bozulması, taslak sürücüde tanıtma/kilitli/NTAG olmayan etiket,
    11 figür + adsız + ninni selamı, ad doğrulaması ve form, halka durumları/tavan/akım sınırı, müzik kutusu,
    donanım tablosu): `cc -O2 -o /tmp/urun_test tools/urun_test.c -lm && /tmp/urun_test`,
  - `python tools/kuyruk_test.py [--urun]` (çizimin kendisi kart_pc'de: doldur → yeniden başlat → çal → kalıcılık →
    bozulma → arka planda oyuncak konması, canlı üretimde oyuncak çekilmesi; `--urun` ilk işleri urun_uret ile de
    üretir),
  - `python tools/urun_akis_test.py` (ürün akışı: tanınma, selam, halka sırası ve RMT karesi, çekilince 3 ayar,
    sesli komutlar, UID tablosu, gece figürü ve kapanma, ayar kartı: Wi-Fi/şifre, captive, form, tanıt, sil,
    kalıcılık, kapanmalar).
  - Ses stili: `ses.h`'nin `hiz`/`perde_kaydir`/`kazanc` varsayılanlarıyla PCM, önceki ses.h ile bayt bayt aynı
    (gerçek ses.bin ile denendi); `tools/ses_test.py` (C ↔ PyTorch) geçiyor.
- kart_pc ek satırları: `#bekle MS`, `#bosta [N]`, `#durum`, `#etiket koy N | koy bos | koy uid UID | dosya YOL |
  kaldir | kilitle | dok`, `#w OLAY`, `#sonra MS SATIR`, `#http GET|POST /yol [gövde]`, `#halka` (RMT bitlerinden
  çözülen kare), her halka durum değişiminde `HALKA_D`; `KART_SAAT=sahte` (belirli saat: delay + her okumada 50 µs),
  `KART_KUYRUK`, `KART_NVS`, `KART_SIFIRLAMA`, `KART_FLASH_KES`, `KART_WIFI_HATA`. Geliştirme düğmeleri:
  `-DDUGME_ACIK=1` ile `#pin P V`, `#pin_sonra P V MS`.
- Gerçek derleme (Arduino çekirdeği 3.3.12, ESP32S3 Dev Module, OPI PSRAM, 16 MB, Custom, USB CDC açık): uygulama
  1 690 224 B (1,75 MB bölümün %92'si; Wi-Fi + WebServer + DNSServer ≈ +605 KB, sesli komut modeli ≈ +100 KB),
  statik RAM 153 820 B (eski 100 448 B; Wi-Fi ~25 KB, KWS ~20 KB, halka RMT tamponu 3,4 KB).
  Öteki derlemeler: `NFC_OKUYUCU 2` (PN532) 1 723 552 B; `NFC_OKUYUCU 0` + `DUGME_ACIK 1` 1 683 984 B; USB CDC kapalı
  (UART) + `MIK_ACIK 0` 1 577 776 B. Hepsi uyarısız. Kartta henüz denenmedi (RC522/PN532 sürücüleri, I2S1 mikrofon,
  RMT halka, Wi-Fi'nin LLM + ses yüklüyken açılıp açılamadığı: açılıştaki "boş: SRAM/PSRAM" ve ayar modundaki
  "[ayar modu] boş SRAM" satırlarını gönderin).
