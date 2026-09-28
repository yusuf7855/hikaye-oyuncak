# Hikâye Oyuncağı — kart testi (ESP32-S3 N16R8)

Bu yazılım, eğittiğimiz modeli **kartın kendisinde** çalıştırır: figür ve yeri seri monitörden seçersiniz, kart
önce planı (Sorun/Çözüm), sonra hikâyeyi yazar ve hızını (token/s) gösterir. İnternet, SD kart ya da bilgisayar
gerekmez; bilgisayar yalnızca yükleme ve ekranı okumak için.

Şu an yüklenecek model: **v4** (`modeller/c2ft_plan/model.bin`, 11,1 MB) — Hikâye Atölyesi'ndeki en iyi model.
Büyük model (C3) hazır olunca aynı yazılımla, yalnız model dosyası değiştirilerek denenecek.

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
   | Partition Scheme | **Custom** (çizim klasöründeki `partitions.csv`: uygulama 1 MB, model bölümü 0x110000) |
   | CPU Frequency | 240MHz |
   | USB CDC On Boot | **Enabled** (kartın "USB" yazan girişini kullanıyorsanız); "COM/UART" girişinde **Disabled** |
   | Erase All Flash Before Sketch Upload | **Disabled** (açık olursa model silinir) |
   | Port | kartın portu (Windows'ta COM3, COM5 gibi) |

3. **Upload** (→) düğmesine basın. Derleme birkaç dakika sürebilir.

## 3. Model dosyasını yükleyin (bir kez; model değişince tekrar)

Kart takılıyken, depo klasöründe bir komut penceresi açıp (portu kendinizinkiyle değiştirin):

```bash
# Windows
python -m esptool --chip esp32s3 --port COM5 --baud 921600 write_flash 0x110000 modeller\c2ft_plan\model.bin
# Mac / Linux
python3 -m esptool --chip esp32s3 --port /dev/ttyACM0 --baud 921600 write_flash 0x110000 modeller/c2ft_plan/model.bin
```

Yükleme ~1 dakika sürer. Kart yükleme modundan çıkmazsa **RST** düğmesine basın.
(Sıra önemli değil: yazılım ve model flash'ın farklı yerlerine yazılır.)

## 4. Deneyin

**Tools → Serial Monitor**, hız **115200**, satır sonu **Newline**. Kart açılışta şuna benzer yazar:

```
=== Hikâye Oyuncağı — kart testi ===
model: V=16384 D=160 L=10 H=4 F=320 P=96 bağlam=224
PSRAM: çekirdek int8 + KV + logits = 5.81 MB; head 4-bit flash'ta
model.bin: 11105372 B, parmak izi fp=3900f74e
```

`model.bin` satırındaki **fp=3900f74e** doğru model yüklendiğini gösterir. Sonra yazın:

| Yazılan | Anlamı |
|---|---|
| `10 1` | Alev (ejderha), orman — hikâye canlı yazılır |
| `1,3 4` | Pamuk ve Karabaş, park |
| `10 1 8` | 8 aday üretir (en çok 16), seçiciyle en iyisini yazar (daha yavaş, daha iyi) |
| `r` | rastgele figür ve yer |
| `?` | figür ve yer listesi |
| `b` | hız testi: head'in üç yolunu ölçer, token başına ms dökümünü yazar, en hızlısını seçer |

Her hikâyenin sonunda `token/s` ve bir **profil** satırı yazar: token başına ms olarak girdi, dikkat, FFN, PLE,
head ve örnekleme. **Bu satırları, `b` çıktısını ve birkaç hikâyeyi bana gönderin.**

### Hız (ilk ölçüm ve düzeltme)

İlk kart denemesi 1,6 token/s verdi (hikâye başına 80–110 s). Neden: head (16 384 satır, 4-bit, flash'ta) tek
çekirdekte ve eleman başına nibble ayıklayan yavaş yoldan hesaplanıyordu; çekirdek katmanlar ise int8 ve iki
çekirdekteydi. Şimdi (`hiz.h`):
- head için hızlı 4-bit çekirdek (bayt başına iki nibble, "-8" grup başına bir kez; sonuçlar eski yolla bit bit
  aynı, `tools/hiz_test.c`),
- head iki çekirdeğe bölünür,
- yer varsa head kodları (1,3 MB) açılışta PSRAM'e kopyalanır.
Açılışta `head: 4-bit hızlı yol, kodlar PSRAM'de` satırı görünür. `b` komutu eski ve yeni yolları karşılaştırır.

## Sorun giderme

| Belirti | Çözüm |
|---|---|
| `model bölümü yok` | Partition Scheme **Custom** seçilmemiş; seçip yazılımı yeniden yükleyin. |
| `model okunamadı` | model.bin yüklenmemiş ya da yanlış adrese yüklenmiş: 3. adım, adres **0x110000**. |
| `HATA: PSRAM ayrılamadı` | PSRAM ayarı **OPI PSRAM** değil. |
| Seri monitör boş | USB CDC On Boot ayarı kullandığınız USB girişine uymuyor; değiştirip yeniden yükleyin. |
| Türkçe harfler bozuk | Seri monitör UTF-8 göstermiyor olabilir; Arduino IDE 2 gösterir. |

## Geliştirici notları

- `generated/` klasörü `tools/basliklar.py` ile üretilir (tokenizer tablosu, 78 seçim × 6 yer istemi, yasaklı
  isimler, `runtime/llm.h` ve `runtime/ornekle.h` kopyaları). Değiştirdikten sonra:
  `python firmware/hikaye_oyuncak/tools/basliklar.py`
- Bellek: çekirdek int8 PSRAM'de, head 4-bit flash'ta, KV önbelleği float 224 konum → PSRAM ≈5.8 MB (8 MB'ın).
- Örnekleme bilgisayardaki `gen`/`degerlendirme/uret.py` ile aynıdır (plan modu, sıcaklık 0.5, top-k 40, tekrar
  1.1, gövdede satır sonu yasağı). Aynı yazılım bilgisayarda sahte ESP32 başlıklarıyla derlenip denendi.
- Tek adayda plan bozulursa (plan yerine hikâye başlarsa) iki kez yeniden denenir.
- Seçici: `secici.h`, `degerlendirme/sec.py` puanla'nın birebir C kopyası (hakemlerin gördüğü E5b/olay2 seçicisi:
  kural + olay + plan + yer cezaları, uydurma-kelime sözlüğü, güvenlik). Aday satırında sıfır olmayan kural
  cezaları parantez içinde yazılır. Eski hafif seçici (güven, bitiş, figür adı sayımı) `#define SECICI_TAM 0` ile;
  güvenlik cezası `SECICI_GUVENLIK` (varsayılan 1). Sözlük `generated/sozluk.h` (~290 KB flash;
  `tools/sozluk_paketle.py` ile `degerlendirme/sozluk.pkl`'den üretilir). Eşitlik testi (bütün havuz adayları +
  bozulmuş sentetik adaylar, puan ve kural kural):
  `python firmware/hikaye_oyuncak/tools/secici_karsilastir.py --guvenlik --sentetik 5000`
