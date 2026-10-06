# Hikâye Oyuncağı — kart testi (ESP32-S3 N16R8)

Bu yazılım, eğittiğimiz ürün modelini **kartın kendisinde** çalıştırır: 11 çizgi film figüründen birini ve onun
kartındaki yerlerden birini seri monitörden seçersiniz, kart önce planı (Sorun/Çözüm), sonra hikâyeyi yazar ve hızını
(token/s) gösterir. İnternet, SD kart ya da bilgisayar
gerekmez; bilgisayar yalnızca yükleme ve ekranı okumak için. Ses modeli (`ses.bin`) ve bir MAX98357A hoparlör
kartı takılıysa hikâyeyi yazdıktan sonra kartın kendisinde sesli okur (bkz. **5. Ses**).

Şu an yüklenecek model: **c3ft_karma** (`modeller/c3ft_karma/model.bin`, 10,3 MB; C3: d192, 12 katman, FFN 512, PLE 56,
V16384) — ürün modeli (10 bin hikâyeli karma veri; kör kıyasta 1030s2'yi geçti, `degerlendirme/urun_kiyas_karma`).
Figürler ve yerleri `data/urun_kartlari.json`'dan; üretim ve seçim bilgisayardaki `degerlendirme/urun_uret.py` ile
aynıdır (istem, isim süzgeci, plan modu, seçici; bkz. **Geliştirici notları**).

> `model.bin` depoda (ZIP'te de var): `modeller/c3ft_karma/model.bin` (SHA-256 `modeller/SHA256SUMS`'ta). Tokenizer C2
> ile aynıdır (`modeller/c2_tokenizer.json`).

## Gerekenler

- ESP32-S3-DevKitC-1 **N16R8** (16 MB flash, 8 MB PSRAM) ve USB kablosu
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
   | Partition Scheme | **Custom** (çizim klasöründeki `partitions.csv`: uygulama 1 MB, model 0x110000, ses 0xBB0000; eskisiyle aynı) |
   | CPU Frequency | 240MHz |
   | USB CDC On Boot | **Enabled** (kartın "USB" yazan girişini kullanıyorsanız); "COM/UART" girişinde **Disabled** |
   | Erase All Flash Before Sketch Upload | **Disabled** (açık olursa model silinir) |
   | Port | kartın portu (Windows'ta COM3, COM5 gibi) |

3. **Upload** (→) düğmesine basın. Derleme birkaç dakika sürebilir.

## 3. Model dosyalarını yükleyin (bir kez; model değişince tekrar)

Flash düzeni (`partitions.csv`):

| Bölüm | Adres | Boyut | İçerik |
|---|---|---|---|
| factory (uygulama) | 0x10000 | 1 MB | Arduino'nun yüklediği yazılım |
| model | **0x110000** | 0xAA0000 (10,6 MB) | LLM `model.bin`: C3 c3ft_karma 10 331 252 B (0x9DA474), pay 809 868 B |
| ses | **0xBB0000** | 0x440000 (4,25 MB) | ses modeli `ses.bin` (~4,34 MB; `ses/disa_aktar.py` üretir) |

Kart takılıyken, depo klasöründe bir komut penceresi açıp (portu kendinizinkiyle değiştirin):

```bash
# Windows
python -m esptool --chip esp32s3 --port COM5 --baud 921600 write_flash 0x110000 modeller\c3ft_karma\model.bin 0xBB0000 ses.bin
# Mac / Linux
python3 -m esptool --chip esp32s3 --port /dev/ttyACM0 --baud 921600 write_flash 0x110000 modeller/c3ft_karma/model.bin 0xBB0000 ses.bin
```

`ses.bin` henüz yoksa komuttan `0xBB0000 ses.bin` kısmını çıkarın: kart konuşmadan eskisi gibi çalışır. Yalnız ses
modelini değiştirmek için: `... write_flash 0xBB0000 ses.bin`.

Yükleme ~1–1,5 dakika sürer. Kart yükleme modundan çıkmazsa **RST** düğmesine basın.
(Sıra önemli değil: yazılım ve modeller flash'ın farklı yerlerine yazılır.) Bölüm tablosu C2'dekiyle aynı: eski
model yüklü bir kartta yalnız yazılımı ve yeni `model.bin`'i (aynı adres, 0x110000) yüklemek yeter; `ses.bin`'e
dokunmak gerekmez. Yazılım ile model birlikte değişti: eski yazılım yeni modelle (ya da tersi) çalışmaz.

## 4. Deneyin

**Tools → Serial Monitor**, hız **115200**, satır sonu **Newline**. Kart açılışta şuna benzer yazar:

```
=== Hikâye Oyuncağı — kart testi ===
model: V=16384 D=192 L=12 H=4 F=512 P=56 bağlam=224
PSRAM: KV + logits 4.06 MB, süzgeç 0.12 MB, çekirdek 4-bit 2.93 MB (int8 5.65 MB gerekirdi)
head: 4-bit hızlı yol, kodlar flash'ta (1.50 MB)
PSRAM toplam (LLM): 7.25 MB
model.bin: 10331252 B, parmak izi fp=00ea3e55
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
| `8 4` | Elsa, şato — hikâye canlı yazılır |
| `1 2` | Niloya, dağ |
| `8 4 8` | 8 aday üretir (en çok 16), seçiciyle en iyisini yazar (daha yavaş, daha iyi) |
| `r` | rastgele figür ve onun yerlerinden biri |
| `?` | figür ve yer listesi |
| `b` | hız testi: head'in üç yolunu ölçer, token başına ms dökümünü yazar, en hızlısını seçer |

Aday sayısı yazılmazsa 1'dir (canlı). Ürün önerisi: oyuncak hikâyeleri boşta kuyruğa hazırlarken **K=16**, çocuk
beklerken üretiliyorsa **K=4–8** (`degerlendirme/urun_secim`). Figürün hikâyesinde başka figürlerin ve onların
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
| SD, GAIN | boş (varsayılan: iki kanalın ortalaması, 9 dB) |

Ses 16 kHz, 16 bit, mono; I2S'te iki kanala da aynı örnek gönderilir (SD ayarı ne olursa olsun duyulur).
Konuşurken kart üstündeki RGB LED yeşil yanar.

`ses.bin` yüklüyse açılışta `ses: akustik d=192 ... | hikâyeyi okuma: açık` satırı görünür. C3 ile LLM'den sonra
PSRAM'de ≈0,7 MB kalır; ses için ≈0,5 MB yeter. Komutlar:

| Yazılan | Anlamı |
|---|---|
| `s Bir varmış bir yokmuş.` | yazılan metni okur |
| `o` | üretilen hikâyeyi otomatik okumayı aç/kapa (ses modeli varsa açık başlar) |

Hikâye cümle cümle okunur: ilk cümle hesaplanırken çalmaya başlar, sonraki cümle çalarken hesaplanır. Okurken seri
monitöre bir şey yazıp gönderirseniz cümle sonunda durur. Her okumadan sonra
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

## Sorun giderme

| Belirti | Çözüm |
|---|---|
| `model bölümü yok` | Partition Scheme **Custom** seçilmemiş; seçip yazılımı yeniden yükleyin. |
| `model okunamadı` | model.bin yüklenmemiş ya da yanlış adrese yüklenmiş: 3. adım, adres **0x110000**. |
| `HATA: PSRAM ayrılamadı` | PSRAM ayarı **OPI PSRAM** değil. |
| `HATA: tokenizer/model uyuşmuyor` ya da anlamsız metin | Eski model (C2) ya da yanlış dosya yüklü: `fp=00ea3e55` olmalı. |
| `çekirdek flash'ta 4-bit (PSRAM yetmedi, yavaş)` ya da `UYARI: isim süzgeci için PSRAM yok` | PSRAM eksik görünüyor; açılış çıktısını bana gönderin. |
| `ses bölümü yok` | Yeni `partitions.csv` ile yazılım yeniden yüklenmemiş (Partition Scheme **Custom**). |
| `ses: ses.bin değil (sihir): konuşma kapalı` | ses.bin yüklenmemiş ya da yanlış adrese: 3. adım, adres **0xBB0000**. |
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
