# Hikâye Oyuncağı: ESP32-S3 N16R8 bütçesi ve uygulama planı (sürüm 2, incelemeler işlendi)

> **Notlar (24 Eylül 2026, sonradan eklendi)**
> - Risk tablosundaki "15,34 s/adım, ≈75,9 saat kalıyor" ölçümü, ön-eğitim başka işlerle aynı anda
>   çalışırken alınmış. Tek başına hız 0,85 s/adım; kalan ≈17 800 adım ≈4,2 saat.
> - Tema başlığı (olay örgüsü planı E1, `| Tema: <tema>`) başlığı 6–10 token uzatır. Gözlenen en uzun bağlam
>   209 → ≈218 olur; S=224'te pay ≈6 token kalır. Tema benimsenirse S=256'ya dönmek +102 400 B PSRAM ister
>   (PSRAM payı 787 832 B'a sığar); karar E1 sonucuna göre verilecek.
> - Bu belge, `degerlendirme` araçlarıyla aynı oturumda çok ajanlı bir inceleme (4 inceleyici, 2 denetçi) ile
>   üretildi; kaynak hesaplar scratch dizinindeydi ve depoya alınmadı. Rakamlar kartta ölçülene kadar tahmindir.

# C3 — aynı kart için büyütülmüş model (25 Eylül 2026)

> Kart: ESP32-S3-DevKitC-1 **N16R8** (16 MB flash, 8 MB PSRAM). Kullanıcı ayrıca NFC okuyucu ve belki BLE ekleyecek.
> Neden: 3 iyileştirme turu (docs/DENEYLER.md) C2'nin kapasite sınırında olduğunu gösterdi.

| | C2 (aşağıdaki plan) | **C3** |
|---|---|---|
| Yapı | d160 L10 F320 P96 H4 | **d192 L12 F512 P56 H4** (head_dim 48) |
| Çekirdek parametre | 3.03 M | **5.70 M** (×1.9) |
| PLE tablosu | 15.7 M | 11.0 M |
| `model.bin` (bölüm 0xAA0000 = 11 141 120 B) | 11 105 372 B | **10 331 252 B** (pay 810 KB) |
| Çekirdek + head PSRAM'de | int8, 7.53 MB | **4-bit (dosyadaki gibi), 7.11 MB** (pay ≈1.27 MB) |
| KV önbelleği (bf16, S=224) | 1.43 MB | 2.06 MB (tabloya dahil) |
| MAC/token (çekirdek + head) | 5.64 M | 8.84 M (×1.57) |
| Hız (merkez tahmin, int8 → 4-bit açma dahil) | 5.8 token/s | ≈3.7 token/s, hikâye ≈36 s |

- Boyutlar dışa aktarma biçimiyle hesaplandı ve 250. adımın ara kaydıyla doğrulandı (model.bin tam 10 331 252 B;
  C motoru ve tarayıcı motoru PyTorch'la birebir: `gen_verify` PASS, JS ilk-5 token aynı).
- **Çekirdek 4-bit PSRAM'de:** int8 açılımı (11.3 MB) PSRAM'e sığmıyor. Matvec 4-bit grup-128 ağırlıkları doğrudan
  okur (llm.h zaten böyle). PSRAM bant genişliği ~80 MB/s ile token başına ≈4.5 MB okuma ≈56 ms.
- **Yavaşlık kullanıcıyı beklettirmez:** hikâyeler kuyrukta önceden hazırlanır (tek figür × yer × 3 hikâye ≈ 54 KB,
  token id'si olarak; 256 KB kuyruk bölümü ≈1000 hikâye). Hazır hikâye yoksa canlı anlatım: model 3.7 token/s yazar,
  ses ≈2.5 token/s okur, anlatım takılmaz.
- **NFC + BLE payı:** NFC okuyucu (PN532/RC522, I2C/SPI) kodu onlarca KB, SRAM'de birkaç KB. BLE (NimBLE) uygulama
  bölümünde ≈300–500 KB ve dahili SRAM'de ≈50–70 KB; uygulama bölümü 0x180000 (1.5 MB, şimdiki tahmin 0.64–0.88 MB)
  ve SRAM payı (185 KB) buna yeter. Wi-Fi gerekmez (açılırsa SRAM payı ayrıca hesaplanmalı).
- Ön-eğitim: `egit_c3.sh` (24 000 adım, bu makinede ≈1.0 s/adım, ≈6.7 saat); ince ayar ince_ayar_c2.sh ile
  `BAZ=runs/ple-c3-s0.pt` ve C3 boyut bayraklarıyla.

---

## 0. Karar

Dil modeli, ses verisi ve kodun hepsi kartta. LM flash ve PSRAM'de, ses flash'ta, kod flash'ta duruyor. SD kart ya da ağ kullanılmıyor.

**Dil modeli (LM)**
- C2 aynen kalıyor: V=16384, D=160, L=10, H=4, F=320, P=96, 4-bit g128.
- `model.bin` 11.105.372 B. Bu boyut yalnızca yapılandırmaya bağlı, eğitim bitince değişmiyor.
- Yeniden eğitim yok. Değişiklikler yalnızca firmware tarafında:
  - KV önbelleği bf16,
  - bağlam S=224,
  - çekirdek ve head int8 olarak PSRAM'de,
  - prefill sırasında head atlanıyor,
  - istemin KV'si K aday arasında paylaşılıyor.

**Ses**
- Kadın seslendirme sanatçısıyla kaydedilmiş 1050 difon, 16 kHz IMA-ADPCM.
- Kendi yazacağımız MIT lisanslı TD-PSOLA motoru. Taban F0 228,6 Hz, periyot tam 70 örnek.
- C'ye taşınmış kural tabanlı Türkçe G2P ve ezgi.
- 84 kalıp ve en sık 1000 kelime, Opus 16 kbps. Çözücü: libopus 1.5.2, sabit nokta, yalnızca çözücü, Arduino'ya kaynak olarak ekleniyor.
- `ses` bölümü toplamı 2.915.777 B.

**Çıkarılanlar**
- Nöral TTS kolu askıya alındı. Nedenleri: flash'a sığmıyor, gerçek zaman oranı (RTF) 1'in çok üstünde, eğitim için GPU yok.
- Polly çıkarıldı (AWS Service Terms madde 50.5).

**Paylar**

| Kaynak | Pay |
|---|---|
| Flash, model bölümü | 35.748 B |
| Flash, ses bölümü | 754.239 B |
| Flash, uygulama | 637.771–875.312 B |
| PSRAM | 787.832 B |
| Dahili SRAM | 185.246 B |

**Hız**

| | ms/token | token/s | 1 hikâye | K=4 |
|---|---:|---:|---:|---:|
| Merkez tahmin | 172,2 | 5,81 | 23,4 s | 90,6 s |
| Kötümser | 241,3 | 4,14 | 32,8 s | 126,9 s |

---

## 1. İnceleme düzeltmeleri

### Uygulananlar

1. **Nöral kol flash'a sığmıyor.** "Kelime bankasının yerine sığar" iddiası yanlış, 259.477 B taşıyor. Düzeltilmiş paketle kelime bankası çıksa bile en fazla ≈1,95 MB ağırlık sığar. Kol askıya alındı. (hesap B1, fizibilite A1)
2. **Nöral kolun SRAM ve SIMD yerleşimi bütçede yoktu.** Ağırlıklar flash ya da PSRAM'deyken skaler yol geçerli ve RTF 8–18 oluyor. Hikâye önceden seslendirilemiyor, çünkü hangi figür durumunun okunacağı bilinmiyor. Kabul şartına "RTF < 1, akışlı" eklendi. Ayrıca int8 "heart" sesi korelasyon eşiğini geçemiyor (0,951 < 0,98), GPU yok, sanoTTS'in Arduino paketi GPL-3.0 ve espeak fonemleri kullanıyor. (hesap B2, fizibilite A2 ve B)
3. **Sahte heap testinin SRAM bütçesi** 304.772 B olmalı: 301.056 + 21.128 − seçici bss 14.340 − ISR IRAM 3.072. (hesap B3)
4. **SRAM tablosuna eklenenler:** üretim görevi yığını 8.192 B, üç görev bloğu (TCB) 1.050 B, I2S ISR IRAM ≈3.072 B. (hesap B4)
5. **Opus çözücü durumu SRAM'e zorlanıyor.** `heap_caps_malloc(opus_decoder_get_size(1), MALLOC_CAP_INTERNAL)` ve ardından `opus_decoder_init`. Host'ta ölçülen boyut 17.860 B (sabit nokta), bütçe 18.432 B (26.000 değil). micro-opus 120 KB'lık "pseudostack" ayırdığı için reddedildi. (hesap B5, fizibilite A5)
6. **`deploy.sh` yazmadan önce boyut denetliyor:** model ≤ 0xAA0000, ses ≤ 0x380000, uygulama ≤ 0x180000. (hesap B6)
7. **Token sayıları başlığı ve EOT'yi içeriyor.** (hesap B7, fizibilite B)
   - Yalnızca hikâye ≈123 token, yani ≈1,26 token/kelime.
   - Gözlenen en uzun bağlam 13 + 196 = 209. S=224'e göre pay 15 token.
   - En uzun hikâye 35,5 s + 1,03 s.
   - V8192 kazancı %8,6 değil %12,9.
   - Akış modunda başlama gecikmesi 2,8 s.
8. **PSRAM ayırma sırası:** head → k → v → 71 çekirdek parçası → logits → TTS halkası. Hepsi kütüphaneler başlatılmadan önce ayrılıyor. (hesap B8)
9. **Kuyruk sektör silme:** `src/kuyruk.c:35` sektörü yazma anında siliyor, bu düzeltilecek. DMA'nın garanti ettiği süre 7 × 480 = 210 ms. (hesap B9)
10. **Ses paketine eklenenler** (hesap B10, fizibilite B):
    - difon sesli/sessiz bayrakları 8.194 B,
    - kelime ve kalıp bayrakları 44.448 B,
    - metin anahtarları 8.192 B,
    - son blok dolgusu 69.300 B,
    - başlıkta Opus çözücü gecikme ofseti.
11. **Küçük düzeltmeler:** head matvec `llm.h:552–553`'te. TTS CPU yükü en fazla %6,13. (hesap B11, ilk yarısı)
12. **Polly çıkarıldı.** AWS Service Terms madde 50.1 ve 50.5 nedeniyle. (fizibilite A3)
13. **Opus kod boyutu ölçüldü:** 76.026 B (-Os) ile 116.003 B (-O3) arası. Firmware 697.552–935.093 B oluyor. (fizibilite A4)
14. **Opus Arduino'ya kaynak olarak ekleniyor.** esp_audio_codec yalnızca ESP-IDF bileşeni olduğu için seçilmedi. (fizibilite A6)
15. **Dikkati iki çekirdeğe bölmek** −10 ile −14 ms değil, −3 ile −6 ms kazandırır (kuramsal üst sınır −8,3). (fizibilite A7)
16. **Stüdyodan önce pilot kayıtla devam/dur dinleme testi yapılıyor.** Toplam perde çarpanı [0,80; 1,35] ile sınırlanıyor, çünkü soru ezgisi ile kuş karakterinin birleşimi 1,63 kat, yani ≈375 Hz ediyordu. (fizibilite A8)
17. **Fizibilite B'deki diğer maddeler:**
    - F0 tabanı 228,6 Hz, periyot tam 70 örnek.
    - K=1 akış modunda denetim cümle cümle yapılıyor: yasak ve Bloom denetimi, gerekirse KV geri sarılıyor.
    - CER eşiği göreli: sanatçının doğal kaydına göre.
    - `ple_gate` dual-core eşiği (`.ino:101`, `rows < 128`) 96'ya indirilebilir, ≈−4 ms. İsteğe bağlı, kartta ölçülerek.

### Reddedilenler ve kısmen kabul edilenler

- **hesap B11, "OrnekDurum 280 B, TOPK_MAX 64": reddedildi.** Bu değerler scratch'teki `src/ornekle.c`'ye ait. Plan depodaki `runtime/ornekle.h`'ı kullanıyor: `OrnDurum` 268 B (host'ta `sizeof` ile ölçüldü, 32-bit'te de aynı), idx ve p çağıranın alanı (top_k 40 ile 160 + 320 B). 748 B'lık satır olduğu gibi kalıyor. Scratch'teki `src/ornekle.c` kullanılmayacak.
- **fizibilite C, "I2S DMA 240 ms dayanır": garanti değer olarak reddedildi.** DMA bir tanımlayıcıyı çalarken önceden doldurulabilecek alan en fazla 7 tanımlayıcı, yani 210 ms. Tasarımda 210 ms kullanılıyor.
- **fizibilite A2, SIMD ile RTF 2,0–3,8: reddedildi.** Bu verim yalnızca ağırlıklar dahili SRAM'deyken geçerli, oysa ≥1,5 MB ağırlık oraya sığmıyor. Skaler yolun RTF'si 8–18.
- **fizibilite B, "bf16 −12 ile −14 ms, ≈166 ms/token": merkez tahmine alınmadı**, çünkü ölçülmedi. 172,2 ms korunuyor, bu kazanç yalnızca olası iyileşme olarak not ediliyor.
- **fizibilite B, "V8192 kazancı ≈%12 (141,2 ms)":** plandaki 139,9 ms tabanıyla %12,9 kullanıldı. Fark önemsiz, karar değişmiyor.

---

## 2. Bütçe tablosu

### 2a. Flash (16 MiB = 16.777.216 B)

| Bölüm | Tür | Ofset | Boyut | Bayt | İçerik | Kullanılan | Pay |
|---|---|---|---|---:|---|---:|---:|
| bootloader + bölüm tablosu | – | 0x0 / 0x8000 | 0x9000 | 36.864 | – | – | – |
| nvs | data/nvs | 0x9000 | 0x6000 | 24.576 | ayarlar, figürler, sayaçlar | < 1.024 | > 23.552 |
| (hiza boşluğu) | – | 0xF000 | 0x1000 | 4.096 | – | – | – |
| factory | app | 0x10000 | 0x180000 | 1.572.864 | firmware + libopus | 697.552–935.093 | 637.771–875.312 (%40,5–55,7) |
| model | data 0x40 | 0x190000 | 0xAA0000 | 11.141.120 | C2 `model.bin` | 11.105.372 | 35.748 (%0,32) |
| ses | data | 0xC30000 | 0x380000 | 3.670.016 | ses paketi | 2.915.777 | 754.239 (%20,6) |
| kuyruk | data | 0xFB0000 | 0x40000 | 262.144 | 512 yuva × 512 B, halka | 504 geçerli hikâye | – |
| coredump | data/coredump | 0xFF0000 | 0x10000 | 65.536 | çökme dökümü | – | – |

- **Toplam:** 65.536 + 1.572.864 + 11.141.120 + 3.670.016 + 262.144 + 65.536 = **16.777.216 B**, tam 16 MiB.
- **Adres zinciri:** 0x10000 → 0x190000 → 0xC30000 → 0xFB0000 → 0xFF0000 → 0x1000000.
- **factory:** 621.526–819.090 B (detok 142.297, Bloom 91.407, başlık tablosu 13.754, yasak 179 dahil; hepsi `const`, flash'ta) + libopus 76.026 (-Os) ile 116.003 B (-O3) arası.

**ses ayrıntısı**

| Kalem | Hesap | Bayt |
|---|---|---:|
| Difon | ADPCM 142,5 s × 8.000 = 1.140.000; blok başlığı 35.625; son blok dolgusu (132 B) 1050 × 66 = 69.300; indeks 12.600; sesli/sessiz bayrakları 142,5 × 230 × 2 bit = 8.194 | 1.265.719 |
| 84 kalıp (Opus) | 420.000 + çerçeve uzunlukları 10.500 + indeks 672 | 431.172 |
| 1000 kelime (Opus) | 1.126.000 + 28.150 + 8.000 | 1.162.150 |
| Kelime ve kalıp sesli/sessiz bayrakları | 773 s × 230 × 2 bit | 44.448 |
| Kelime ve kalıp metin anahtarları | – | 8.192 |
| Başlık, sürüm, CRC, vurgu istisnaları, Opus gecikme ofseti | – | 4.096 |
| **Toplam** | | **2.915.777** |

**MMU sayfaları** (64 KiB): PSRAM 128 + model 170 + ses 56 + uygulama 17 (935.093 → 15 sayfa, IROM/DROM ayrımı için +2) = **371 / 512**. Pay 141 sayfa.

### 2b. PSRAM

Kullanılabilir alan ≈8.315.000 B (hesap incelemesi: 8.317.586 ± 5.243).

Ayırma sırası: head → k → v → çekirdek → logits → TTS halkası. Hepsi NFC, I2S ve Opus başlatılmadan önce ayrılıyor. Arduino'da 4 KB'ın üstündeki `malloc`'lar PSRAM'e düşüyor (`CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL=4096`); bunlar 64 KiB'lık yedekten karşılanıyor.

| Tampon | Hesap | Bayt |
|---|---|---:|
| head int8 (bağlı `tok_emb`) | 16.384 × 160 + 16.384 × 8 | 2.752.512 |
| kcache bf16 | 10 × 224 × 160 × 2 | 716.800 |
| vcache bf16 | aynı | 716.800 |
| Çekirdek int8 (71 parça, her biri ≤ 161.280) | 10 × 300.288 + 161.280 | 3.164.160 |
| logits | 16.384 × 4 | 65.536 |
| **LM ara toplamı** | | **7.415.808** |
| TTS'ten I2S'e PCM halkası | 1 s × 16.000 × 2 | 32.000 |
| Fonem ve ezgi listesi | 1.024 × 8 | 8.192 |
| Aday token tamponları | 8 × 224 × 2 | 3.584 |
| Seçilen metin ve akış cümle tamponu | – | 2.048 |
| Kütüphane `malloc`'ları için yedek (> 4 KB) | – | 65.536 |
| **Toplam** | | **7.527.168** |
| **Pay** | | **787.832 (%9,5)** |

Bugünkü firmware fp32 KV ve S=256 ile 9.259.008 B istiyor ve açılışta `ps_or_die("staged head")` satırında duruyor (`esp32_tinystories.ino:222`).

### 2c. Dahili SRAM

Upstream, LLM ayırmalarından (21.128 B dinamik + 8.192 B statik `xq`) sonra 301.056 B boş ölçmüş.

| Kalem | Bayt |
|---|---:|
| LLM toplamı: scratch 19.456 + norm vektörleri 20.224 + statik `xq` 8.192 (upstream'e göre +18.552) | 47.872 |
| **LLM sonrası boş** | **282.504** |
| I2S DMA (8 × 480 × 2 B + tanımlayıcılar) | 7.776 |
| I2S ISR, IRAM (`CONFIG_I2S_ISR_IRAM_SAFE`), tahmin 2–4 KB | 3.072 |
| TTS görev yığını (libopus `VAR_ARRAYS`) | 32.768 |
| Opus çözücü durumu, `MALLOC_CAP_INTERNAL` (ölçülen 17.860) | 18.432 |
| Üretim görevi yığını | 8.192 |
| Görev blokları (TTS, üretim, NFC): 3 × 350 | 1.050 |
| PSOLA tamponları | 3.200 |
| NFC görevi ve I2C | 5.120 |
| Seçici bss | 14.340 |
| Örnekleyici: `OrnDurum` 268 + idx 160 + p 320 | 748 |
| Kuyruk yazma tamponu | 512 |
| Güç, düğme, LED | 2.048 |
| **Ek toplam** | **97.258** |
| **Pay** | **185.246** |

- Host'taki sahte heap testinin bütçesi: 322.184 − 14.340 − 3.072 = **304.772 B**. Test sonunda beklenen boş alan 185.246 B.
- İsteğe bağlı: logits SRAM'e taşınırsa pay 119.710 B'a iner, karşılığında 1–3 ms/token kazanılır.

---

## 3. Seçilen LM yapılandırması ve hız

### Yapılandırma
- C2, S=224, KV bf16 (en yakın çifte yuvarlama). Host'ta ölçülen ΔCE −0,0002.
- int8 aktivasyon, çift çekirdekli matvec.
- `max_new` = 210. S=224'e ulaşıp EOT gelmezse aday son tam cümlede kesilir, seçici bunu cezalandırır.

**V8192'ye kesmek reddedildi**
- Kazancı: hikâye 22,4 s'den 19,5 s'ye iner (−%12,9); PSRAM'de 1,38 MB, flash'ta 4,75 MB açar.
- Yeniden eğitim gerektiriyor; C2 eğitimi zaten ≈76 saat sürüyor.
- Bütçe V8192 olmadan da payla sığıyor.

### Hız
- Sabit kısım 148,7 ms + KV 0,265 ms/girdi + örnekleme 3,0 ms.
- **Üretim:** 172,2 ms/token, 5,81 token/s (130 token varsayımı; gerçek ortalama ≈123, yani %5 kötümser).
- **Prefill:** 12 × 85,9 = 1,03 s.

| | Merkez | Kötümser (× 1,401) |
|---|---:|---:|
| 1 aday | 23,4 s | 32,8 s |
| Sonraki adaylar (KV'nin 0..11 satırı paylaşılıyor) | her biri 22,4 s | – |
| K=4 | 90,6 s | 126,9 s |
| K=8 | 180,1 s | 252,4 s |
| En uzun gözlenen (196 token): ort. 181,0 ms/token × 196 + prefill | 36,5 s | – |

**Konuşma ile karşılaştırma**
- Konuşma süresi: 97,7 kelime, 107 kelime/dk ile 54,8 s. Bu sürede 2,4 aday üretilebilir.
- TTS en fazla %6,13 CPU alıyor.

**Bir gece şarjda (8 saat)**
- K=4 ile 317 hikâye; kötümser 226.
- Kuyruk 504 yuva.

**K=1 akış modu**
- Başlama gecikmesi: 1,03 + 8,2 kelime × 1,26 × 0,1722 = **2,8 s**. 2,5 s'lik tanıtım kalıbı bunun çoğunu örtüyor.
- Üretim hızı 4,61 kelime/s, konuşma 1,78 kelime/s: 2,6 kat pay (kötümserde 1,85 kat).
- Her cümle seslendirilmeden önce yasak kelime ve Bloom denetiminden geçiyor. Başarısız olursa KV cümle başına geri sarılıyor ve en fazla 3 kez yeniden örnekleniyor. Yine olmazsa hikâye bir kapanış kalıbıyla bitiriliyor.

**Olası iyileşmeler (ölçülmedi, merkez tahmine katılmadı)**
- bf16'nın gerçek kazancı büyük çıkarsa ≈166 ms.
- Dikkati iki çekirdeğe bölmek: −3 ile −6 ms.
- `ple_gate` eşiğini 96'ya indirmek: ≈−4 ms.
- logits SRAM'e: −1 ile −3 ms.

---

## 4. Seçilen ses yaklaşımı

**Kayıt**
- 25–35 yaş, sıcak tonlu, çocuğa uygun bir kadın seslendirme sanatçısı.
- İçerik: 1050 difon logatomu, 1000 kelime, 84 kalıp. Hepsi tek düze perdeyle okunuyor.
- Kayıtlar çevrimdışı olarak tam 70 örneklik periyoda (228,6 Hz) getiriliyor.
- Sözleşme: tüm hakların devri, TTS ve sentetik ses kullanımı için açık izin, KVKK açık rızası.

**Sentez**
- TD-PSOLA, örtük (sabit periyotlu) perde işaretleri ve sesli/sessiz bayrakları ile. CPU yükü ≈%0,13.
- Opus SILK çözme %2–6.
- Kelime ve kalıplar da PSOLA'dan geçiyor. Opus çözücü gecikmesi paket başlığındaki ofsetle hizalanıyor.

**Ezgi**
- `tr_pho.py` kuralları C'ye taşınıyor.
- Hız 105–115 kelime/dk.
- Karakter perdesi ±%15 (kuş +%15, ayı −%10).
- Soru ezgisi dahil toplam perde çarpanı [0,80; 1,35] aralığında, yani 183–309 Hz.

**Kalite kapısı (stüdyo rezervasyonundan önce)**
- Pilot kayıt: ≈100 difon ve 20 kelime.
- Kendi motorumuzla 10 cümle seslendirilir, gerçek 3 W hoparlörden kör panelde dinletilir. Karşılaştırma: Piper dfki ve sanatçının kendi doğal okuması.
- Devam şartları:
  - panelin en az %60'ı bizim sesi dfki'ye tercih etmeli,
  - CER(TTS) − CER(doğal okuma) ≤ 3 puan.
- Kapı geçilemezse: kelime ve kalıp katmanı büyütülür (500 kelime ek ≈0,58 MB; paya sığar) ve ezgi katsayıları yeniden ayarlanır.

**Ürüne girmeyecekler**
- Piper dfki: erkek ses, NC lisans.
- MBROLA tr2: lisansı satılan ürüne izin vermiyor; motoru AGPL.
- espeak-ng: GPLv3.
- Polly: AWS Service Terms 50.5.
- sanoTTS Arduino paketi: GPL.
- micro-opus: 120 KB pseudostack.
- esp_audio_codec: yalnızca ESP-IDF bileşeni.

**Nöral kol (askıda)**
- Yeniden açılması için hepsi gerekli:
  - ağırlık ≤ 1,95 MB,
  - kartta ölçülmüş RTF < 1 ve akışlı çalışma,
  - çalışma alanı SRAM payına sığmalı,
  - kendi fonem kümemizle eğitilmiş olmalı,
  - GPU erişimi,
  - int8 korelasyonu ≥ 0,98,
  - kör A/B testini kazanmalı.

---

## 5. Uygulama adımları (sırayla)

### Aşama A: LM ve üretim döngüsü

1. **`/home/user/hikaye-oyuncak/runtime/llm.h`**
   - `LLM_KV_BF16` bayrağı ve `llm_kv_t`.
   - Satır 493–494'teki `memcpy` → `llm_kv_put()` (en yakın çifte yuvarlama).
   - Dikkat döngüsündeki okumalar → `(uint32_t)h << 16`.
   - `llm_forward_ex(m, tok, pos, s, want_logits)`: satır 552–553'teki head matvec atlanabiliyor. `llm_forward` eski imzayla kalıyor.
2. **Host kapıları:** `runtime/host_verify/verify.c` (bayraksız, golden birebir), `staging_verify.c` (`-DLLM_INT8_ACT=1 -DLLM_KV_BF16=1`), `ppl.c` (|ΔCE| ≤ 0,001 nat). Başlangıç için scratch'teki `ppl_kv.c` kullanılabilir.
3. **Örnekleyici:** `/home/user/hikaye-oyuncak/runtime/ornekle.h` (depoya eklenir) ve `runtime/host_verify/gen.c`.
   - `orn_logp` eklenir.
   - K aday döngüsü, istem KV'si paylaşılarak.
   - S=224'te kesme kuralı.
   - K=1 akış modu: cümle denetimi ve KV geri sarma.
4. **Seçici:** `runtime/secici.h` (scratch'teki `src/secici.c` ve `katalog.c`'den) ve `runtime/host_verify/secici_verify.c`.
5. **Tablolar:** `/home/user/hikaye-oyuncak/firmware/esp32_tinystories/tools/gen_tables.py` (scratch'teki sürümden) şu dosyaları üretir: `detok.h` 142.297, `basliklar.h` 13.754, `yasak.h` 179, `bloom.h` 91.407 B. Bunlar U+FFFD hatasını düzeltiyor. `generate_vocab.py` emekliye ayrılır.

### Aşama B: firmware iskeleti

6. **`/home/user/hikaye-oyuncak/firmware/hikaye_oyuncak/partitions.csv`:** 2a'daki tablo.
7. **`/home/user/hikaye-oyuncak/scripts/deploy.sh`:** yeni `hikaye` türü.
   - `PART_OFFSET=0x190000`, `APP_MAX_BYTES=1572864`.
   - `ses.bin` 0xC30000'e yazılır. Kuyruk bölümü yalnızca ilk kurulumda silinir.
   - Satır 310'daki `write_flash`'tan önce boyut kontrolü; sınır aşılırsa iptal.
   - libopus için `--build-property` ile `-I` yolları ve bayraklar (scratch'teki `opus/build.sh`'tan).
   - Kapılar: verify, staging-bf16, ppl-bf16, secici, detok, tts.
   - `/home/user/hikaye-oyuncak/tests/test_deploy.py`: büyük model reddi testi eklenir.
8. **`firmware/hikaye_oyuncak/hikaye_oyuncak.ino`** (`esp32_tinystories.ino`'dan türetilir)
   - `seq_len` 224 ile sınırlanır; KV `L*S*D*sizeof(llm_kv_t)`.
   - PSRAM ayırma sırası 2b'deki gibi, kütüphaneler başlatılmadan önce.
   - PSRAM payı 256 KB'ın altındaysa FATAL.
   - Üretim görevi: 8 KB yığın, K aday → seçici → kuyruk.
   - `ses` bölümü mmap edilir (56 sayfa).
   - İsteğe bağlı: `ple_gate` eşiği (satır 101) 96'ya indirilir, kartta ölçülerek.
9. **`firmware/hikaye_oyuncak/kuyruk.h`** (scratch'teki `src/kuyruk.c`'den)
   - `kuyruk_yaz` sektör silmez. `kuyruk_on_sil()` yalnızca sessizken çağrılır ve en az bir silinmiş sektörü hazır tutar.
   - Konuşurken yalnızca 512 B programlama yapılır (≤ 6 ms, DMA'nın 210 ms'lik payının çok altında).
10. **`pn532.h` (I2C 0x24) ve I2S:** 16 kHz, mono, 16-bit, `dma_desc_num` 8, `dma_frame_num` 480, MAX98357A'yı SD_MODE ile kapatma. GPIO35–37'ye dokunulmaz (octal PSRAM).

### Aşama C: ses

11. **`runtime/tts/tr_g2p.h`:** `tr_pho.py`'nin C portu. F0 228,6 Hz, toplam perde çarpanı [0,80; 1,35].
12. **`runtime/tts/adpcm.h`:** IMA çözücü.
13. **`runtime/tts/psola.h`:** 70 örneklik örtük perde işaretleri ve sesli/sessiz bayrakları.
14. **`runtime/tts/ses_paket.h`** ve **`/home/user/hikaye-oyuncak/tools/ses_paketle.py`:**
    - Kayıtlar periyoda getirilir.
    - Bayraklar, metin anahtarları, blok dolgusu ve Opus gecikme ofseti pakete yazılır.
15. **`firmware/hikaye_oyuncak/src/opus/`:** libopus 1.5.2, sabit nokta, yalnızca çözücü, BSD-3. `VAR_ARRAYS` ile; durum `MALLOC_CAP_INTERNAL` + `opus_decoder_init(st, 16000, 1)`.
16. **`runtime/host_verify/tts_render.c`:** cihazdaki C koduyla WAV üretir, `post.py` hoparlör süzgeci uygulanır. Pilot kayıtla kalite kapısı (bölüm 4), sonra stüdyo kaydı.
17. **`/home/user/hikaye-oyuncak/README.md`:** satır 102, 245, 281–282, 303–304 ve 375'teki "SD kart" ve "Piper dfki" ifadeleri düzeltilir; Polly ve nöral kol ürün dışı olarak yazılır.

### Aşama D: yalnızca geri dönüş gerekirse

18. **3-bit PLE tablosu:** `/home/user/hikaye-oyuncak/research/tinystories/export.py` ve `llm.h` (`LLM_FLAG_TABLE_NBIT`, başlıkta `table_bits`). Tahminen ≈60 satır C, ≈40 satır Python.

---

## 6. Host'ta doğrulama

- **Golden, staging-bf16 ve ppl kapıları:** `hf_c2tmp/model.bin` ile şimdi; son checkpoint gelince tekrar.
- **KV paylaşımı:** pos 12'den yeniden başlatılan aday, sıfırdan prefill+üretimle aynı tohumda birebir aynı token dizisini vermeli. KV geri sarıp yeniden örnekleme de taze bir koşuyla birebir aynı olmalı.
- **`orn_logp`:** tam `expf` sonucuyla fark < 1e-3.
- **Seçici:** 3.414 vakada `sec.py` ile aynı puan.
- **Detok ve yasak tablosu:**
  - 2364 hikâyede detok(encode(metin)) == metin baytları.
  - 78 yasak kombinasyonunun hepsinde `yasak_idler()` ile aynı sonuç.
- **Bellek simülasyonu:** sahte `heap_caps_malloc` ile PSRAM 8.315.000 B ve dahili heap 304.772 B. Tüm ayırmalar başarılı olmalı; kalan PSRAM 787.832 ± 1 KB, kalan SRAM 185.246 ± 4 KB olmalı.
- **xtensa link haritası (upstream'e göre):**
  - Tablolar `.flash.rodata`'da olmalı.
  - `.dram0.bss/.data` artışı ≤ 15 KB, `.iram0.text` artışı ≤ 4 KB.
  - Uygulama ≤ 935.093 B.
  - Opus çözme çağrı zinciri `-fstack-usage` ile < 28 KB.
- **Bölümler ve deploy:** `gen_esp32part.py` doğrulaması; `test_deploy.py` büyük dosyaları reddetmeli.
- **Kuyruk:** RAM'de taklit edilen flash üzerinde güç kesme fuzz testi; konuşurken hiç silme çağrısı olmamalı.
- **G2P:** 28.208 cümle ve 2364 hikâyede fonem, süre ve F0 listeleri Python ile aynı olmalı.
- **ADPCM:** Python kodlayıcısıyla bit düzeyinde aynı.
- **PSOLA:** ölçülen F0 hedefin ±%5 içinde, toplam çarpan sınırı uygulanıyor.
- **Ses paketi:** paketle/oku gidiş-dönüş, ayrıştırıcı fuzz testi, Opus gecikme ofseti.
- **Kelime bankası kapsaması:** 2364 hikâyede ölçülüp raporlanır.
- **TTS kalitesi:** göreli CER ve dinleme paneli (bölüm 4).

**Kartta ilk gün ölçülecekler:**
- gerçek ms/token (`LLM_PROFILE`),
- gerçek boş PSRAM ve SRAM,
- iki çekirdek aynı anda erişirken PSRAM bant genişliği,
- `expf` çevrim maliyeti,
- int8 hazırlama süresi,
- Opus'un gerçek CPU payı ve TTS yığınının en yüksek kullanımı,
- flash yazımı sırasında I2S kesintisi,
- hoparlörden duyulan kalite.

---

## 7. Riskler ve geri dönüşler

| Risk | Geri dönüş |
|---|---|
| Difon sesi mekanik ya da "kaba" kalır (en büyük risk) | Stüdyodan önce pilot kapısı. Kelime ve kalıp katmanı büyütülür (+500 kelime ≈0,58 MB), ezgi ayarlanır. Nöral kol yalnızca bölüm 4'teki şartlarla. |
| PSRAM yetmez | KV int8 −645.120 B; S=192 −204.800 B; head int4 −1.376.252 B (+20 ile +40 ms). |
| Hız 241 ms'den kötü çıkar | K=2 ile 63,8 s. Dikkati iki çekirdeğe bölmek −3 ile −6 ms, `ple_gate` ≈−4 ms, logits SRAM'e −1 ile −3 ms. Son çare V8192 (−%12,9, yeniden eğitim gerekir). |
| Model bölümünde pay yalnızca 35.748 B | `deploy.sh` boyut kontrolü; 3-bit tablo flash'ta 1,74 MB açar. |
| Bağlamda pay 15 token | S=224'te son tam cümlede kesme; gerekirse S=256 (+102.400 B PSRAM). |
| Ses verisi büyür | Pay 754.239 B. 22,05 kHz difon +470 KB ile yine sığar. Opus başarısız olursa yalnızca ADPCM: 2,60 MB. |
| Opus'u Arduino'ya eklemek | Kaynak olarak ekleme ve `--build-property`. Alternatif: pschatzmann/codec-opus. |
| Flash yazımı önbelleği kapatır | Sektör yalnızca sessizken silinir; konuşurken ≤ 6 ms programlama, 210 ms DMA payı var. |
| bf16 kalitesi erken checkpoint'te ölçüldü | Son checkpoint'te ppl kapısı tekrarlanır (≤ 0,001 nat). |
| Derin uykuda PSRAM içeriği kaybolur | Şarjda hafif uyku. Uyanışta yeniden hazırlama 0,3–0,5 s (kartta ölçülecek). |
| Lisans | Yalnızca sanatçı sözleşmesi ve KVKK rızası. Üründe tr2, dfki, GPL kod ve Polly yok; libopus BSD-3. |
| Eğitim takvimi | `runs/ple-c2-s0.progress.json`: adım 6180/24000, 15,34 s/adım, devam ettirilirse ≈75,9 saat kalıyor. PID 4351 hâlâ durdurulmuş (Tl). Firmware işi bundan bağımsız, çünkü `model.bin` boyutu sabit. |

**Kaynak dosyalar**
- Scratch: `/tmp/claude-0/-home-user-hikaye-oyuncak/51a50a87-4e4c-59c8-8b0c-5316b89b1551/scratchpad/esp32/`
  - `src/secici.c`, `src/kuyruk.c`, `gen_tables.py`, `ppl_kv.c`, `llm_kv.h`, `tr_pho.py`
  - `opus/build.sh`, `opus/hsize.c`
  - `denetim/arit.py`
- Depo: `/home/user/hikaye-oyuncak/runtime/llm.h`, `/home/user/hikaye-oyuncak/runtime/ornekle.h`, `/home/user/hikaye-oyuncak/firmware/esp32_tinystories/esp32_tinystories.ino`, `/home/user/hikaye-oyuncak/scripts/deploy.sh`