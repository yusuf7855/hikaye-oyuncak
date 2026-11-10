# Claude Code istemi: halka ve NFC denemesi (Mac, ESP32-S3 USB ile bağlı)

Bu dosyanın tamamını Claude Code'a ver ("bu dosyayı oku ve uygula" ya da içeriği yapıştır).

---

Sen ürün sahibinin Mac'indeki Claude Code'sun. Benimle **Türkçe**, kısa ve sade konuş. Görevin: ESP32-S3 kartına
deneme kodlarını derleyip yüklemek, seri çıktıyı okumak ve sorun varsa bulup düzeltmek. Halkayı ve kartın
ışıklarını sen göremezsin: ne gördüğümü bana sor.

## Donanım
- Kart: **ESP32-S3-DevKitC-1 N16R8** (16 MB flash, 8 MB PSRAM). Mac'e çipin kendi USB ucundan bağlı:
  port `/dev/cu.usbmodem1101` (değişebilir: `ls /dev/cu.usbmodem*`). esptool bu portu "USB-Serial/JTAG" görüyor.
- Arduino IDE kurulu, ESP32 çekirdeği **esp32:esp32 3.3.12** zaten kurulu (`~/Library/Arduino15`).
- Önceki denemede yükleme başarılı oldu ama **seri monitörde hiçbir şey çıkmadı ve halka yanmadı**. Büyük olasılıkla
  "USB CDC On Boot" kapalıydı (o zaman `Serial` çipin USB ucuna değil UART0'a gider). Ayrıca yüklenen taslağın adı
  "RenkliLed" idi; aşağıdaki kodun yüklendiğinden emin değilim.

## Araç
- `arduino-cli` kullan (yoksa `brew install arduino-cli`; Homebrew yoksa Arduino IDE'nin içindekini bul ya da bana sor).
  Aynı veri klasörünü kullanır, çekirdeği yeniden indirmen gerekmez (`arduino-cli core list` ile bak).
- Kart ayarı (FQBN), USB CDC açık:
  `esp32:esp32:esp32s3:FlashSize=16M,PSRAM=opi,CDCOnBoot=cdc,USBMode=hwcdc`
- Derle ve yükle:
  `arduino-cli compile --upload -p /dev/cu.usbmodem1101 -b <FQBN> <taslak klasörü>`
  Yükleme bağlanamazsa: bana "BOOT'u basılı tut, RST'ye bas, BOOT'u bırak" dedirt, sonra tekrar dene; bitince RST.
- Seri çıktıyı oku (115200): `pip3 install pyserial` ve kısa bir Python betiğiyle portu aç, 15-20 s oku, ekrana bas;
  komut göndermek için satır sonuyla yaz (`s\n` gibi). Port açılınca kart yeniden başlayabilir, normaldir.
  Hiç çıktı yoksa: CDCOnBoot ayarını, kartın indirme kipinde kalıp kalmadığını (RST'ye bastır) denetle.
- Taslak klasörünün adı `.ino` dosyasının adıyla aynı olmalı (`halka_deneme/halka_deneme.ino`). Kodlar aşağıda; depo
  (`github.com/yusuf7855/hikaye-oyuncak`, `firmware/denemeler/`) elindeyse oradakiler de aynıdır.

## Sıra
1. **Halka** (`halka_deneme`). Bağlantı: halka **DI** -> 330 Ω -> **GPIO18**; halka **DO boş**; halka 5V -> kartın
   **5V** ucu; halka GND -> kartın **GND** ucu (ortak toprak şart). Seviye çevirici deneme için şart değil.
   Beklenen seri çıktı: `== Halka denemesi (GPIO18) ==`, `RMT hazir`, sonra renk adları. Halka kırmızı, yeşil, mavi,
   beyaz yanıp gökkuşağı dönmeli. Bana ne gördüğümü sor. Renk sırası tutmuyorsa halka RGB'dir (kod GRB yolluyor):
   kodu düzelt. Sonra `s` gönder ve bana halkada yanan **son numarayı** sor: o, **LED sayısı**dır.
   Halka hiç yanmıyorsa: kabloları bana tek tek denetlet (DI/DO karışması en sık hata), 5V ucunda gerilim var mı
   (ölçü aleti varsa), GND ortak mı; 330 Ω'u kaldırıp doğrudan dene; son çare GPIO18 yerine başka uç (ör. 21) dene
   ve kodda `HALKA_PIN`'i değiştir (ana üründe pin 18 kalır, bunu bana not et).
2. **RC522** (`nfc_rc522_deneme`). `arduino-cli lib install MFRC522`. Bağlantı: 3.3V -> **3V3** (5V'A DEĞİL), GND,
   SCK 12, MISO 13, MOSI 11, SDA 10, RST 9, IRQ boş. Beklenen: `RC522 bulundu, surum 0x..`. Etiketi koydurup
   çıktıyı oku; boş NTAG etiketlere figür kaydı yazmak için `y <numara>` (1 Niloya ... 12 Ay Dede, 200 ayar kartı).
   Okuma oranını ("yoklamalarin x/y'unda") stand kapağının üstünden de denet.
3. **PN5180** (`nfc_pn5180_deneme`, kütüphanesiz; sürücüyü NXP veri sayfasından yazdım, **hiç denenmedi**). Bağlantı:
   5V -> **5V**, 3.3V -> **3V3**, GND, SCK 12, MISO 13, MOSI 11, NSS 10, RST 9, **BUSY -> GPIO8**; IRQ/GPIO/AUX/REQ boş.
   Beklenen: `PN5180 bulundu: urun x.y ...`, etiket konunca UID. Çalışmazsa sürücüyü düzelt (BUSY el sıkışması,
   EEPROM adresleri 0x10/0x12/0x14, RF_STATUS bitleri 24-26, RX_IRQ = IRQ_STATUS bit 0); gerekirse karşılaştırma için
   ATrappmann/PN5180-Library ya da tueddy/PN5180-Library'nin ISO14443 kodlarına bak.

## Sonunda bana
- Halkanın LED sayısı ve renk sırası (GRB/RGB), iki okuyucunun bulunup bulunmadığı, etiket okuma oranları, kısa özet.
- Kodda değişiklik yaptıysan ne değiştiğini söyle. Depo bu bilgisayardaysa: değişiklikleri `firmware/denemeler/`
  altına koy, Türkçe commit mesajıyla `claude/wonderful-pasteur-x7seiq` dalına it; ana yazılımda halka LED sayısı
  `firmware/hikaye_oyuncak/donanim.h` -> `HALKA_LED_SAYISI` (şu an 16) ve README/URUN_TANIMI'ndeki "16 LED" geçen
  yerler. Ana yazılımı kendi başına karta yükleme; önce bana sor.

---

## Kod: `halka_deneme/halka_deneme.ino`

```cpp
// NeoPixel halka denemesi (ESP32-S3; ana yazılımdan bağımsız, kütüphane gerekmez: çekirdeğin RMT'si).
//
// Bağlantı (docs/URUN_TANIMI.md): halka DIN <- 330 Ω <- 74AHCT1G125 çıkışı; çevirici girişi GPIO18, OE -> GND,
// VCC 5 V. Halka 5 V ve GND'den beslenir, girişte 1000 µF. Çevirici yoksa DIN doğrudan GPIO18'e (330 Ω ile) de
// çoğu halkada çalışır.
//
// Seri monitör 115200 (satır sonu: "Yeni satır"). Açılışta renk sırası denenir, sonra gökkuşağı döner. Komutlar:
//   s        sayım: LED'ler tek tek yanar, numarası yazılır; halkada yanan son numara = LED sayısı
//   n 24     LED sayısını ayarla (en çok 64)
//   p 10     parlaklık %, 1..40 (USB'den beslerken 20'yi geçme)
//   r        renk sırası: kırmızı, yeşil, mavi, beyaz (1'er s)
//   g        gökkuşağı (dönen)
//   b        beyaz nefes
//   f        figür renkleri sırayla (ürünün halka renkleri)
//   0        söndür
#include <Arduino.h>

#define HALKA_PIN 18
#define MAKS 64

static int n_led = 16, parlak = 10, kip = 'g';
static uint8_t kare[MAKS][3];
static rmt_data_t bitler[MAKS * 24];
static bool rmt_var = false;

static void gonder() {
  if (!rmt_var) return;
  for (int i = 0; i < MAKS; i++) {
    const uint8_t grb[3] = {kare[i][1], kare[i][0], kare[i][2]};  // WS2812: önce yeşil
    for (int c = 0; c < 3; c++)
      for (int b = 0; b < 8; b++) {
        rmt_data_t *r = &bitler[(i * 3 + c) * 8 + b];
        bool bir = (grb[c] >> (7 - b)) & 1;
        r->level0 = 1; r->duration0 = bir ? 8 : 4;   // 10 MHz: 1 = 0,8/0,4 µs, 0 = 0,4/0,8 µs
        r->level1 = 0; r->duration1 = bir ? 4 : 8;
      }
  }
  // Her zaman 64 LED yollanır: fazlası halkada yoksa zararsız, sayımda gerçek sayıyı bulmayı sağlar
  rmtWrite(HALKA_PIN, bitler, MAKS * 24, RMT_WAIT_FOR_EVER);
}

static void boya(int i, uint8_t r, uint8_t g, uint8_t b) {
  if (i < 0 || i >= MAKS) return;
  kare[i][0] = (uint8_t)(r * parlak / 100);
  kare[i][1] = (uint8_t)(g * parlak / 100);
  kare[i][2] = (uint8_t)(b * parlak / 100);
}
static void hepsi(uint8_t r, uint8_t g, uint8_t b) {
  memset(kare, 0, sizeof kare);
  for (int i = 0; i < n_led; i++) boya(i, r, g, b);
  gonder();
}
static void renk_tekerlek(int h, uint8_t *r, uint8_t *g, uint8_t *b) {  // h 0..767
  h %= 768;
  if (h < 256) { *r = 255 - h; *g = h; *b = 0; }
  else if (h < 512) { h -= 256; *r = 0; *g = 255 - h; *b = h; }
  else { h -= 512; *r = h; *g = 0; *b = 255 - h; }
}

// data/figur_donanim.json'daki halka renkleri
static const struct { const char *ad; uint8_t r, g, b; } FIGUR[] = {
    {"Niloya (pembe)", 0xFF, 0x6F, 0xA8},  {"Masa (mor)", 0xB4, 0x5C, 0xFF},     {"Pepee (turuncu)", 0xFF, 0x8A, 0x1F},
    {"Keloglan (yesil)", 0x7E, 0xD3, 0x21}, {"Doru (kahverengi)", 0xC9, 0x80, 0x2E}, {"Hayri (sari)", 0xFF, 0xC2, 0x1A},
    {"Sakir (altin)", 0xFF, 0xE4, 0x5C},    {"Elsa (buz mavisi)", 0x7F, 0xDB, 0xFF}, {"Chase (lacivert)", 0x25, 0x63, 0xFF},
    {"Orumcek Adam (kirmizi)", 0xE8, 0x20, 0x2E}, {"Hello Kitty (beyaz)", 0xFF, 0xFF, 0xFF},
    {"Ay Dede (gece mavisi)", 0x3B, 0x3F, 0xD8},
};

static void renk_sirasi() {
  const char *ad[4] = {"KIRMIZI", "YESIL", "MAVI", "BEYAZ"};
  const uint8_t rgb[4][3] = {{255, 0, 0}, {0, 255, 0}, {0, 0, 255}, {255, 255, 255}};
  for (int k = 0; k < 4; k++) {
    Serial.printf("  simdi %s olmali\n", ad[k]);
    hepsi(rgb[k][0], rgb[k][1], rgb[k][2]);
    delay(1000);
  }
  Serial.println("  Renkler yazilanla ayni degilse halka GRB degil (RGB): bana yaz.");
}

static void sayim() {
  Serial.println("Sayim: LED'ler tek tek yesil yanar (ilki kirmizi). Halkada yanan SON numara = LED sayisi.");
  memset(kare, 0, sizeof kare);
  for (int i = 0; i < MAKS; i++) {
    boya(i, i == 0 ? 255 : 0, i == 0 ? 0 : 255, 0);
    gonder();
    Serial.printf("  LED %d\n", i + 1);
    delay(i < 8 ? 400 : 250);
    if (Serial.available()) break;
  }
  Serial.println("Sayim bitti. Ornek: halkada 24'te durduysa \"n 24\" yaz.");
}

static void komut(String s) {
  s.trim();
  if (!s.length()) return;
  char c = s[0];
  int v = s.length() > 1 ? s.substring(1).toInt() : 0;
  if (c == 'n' && v > 0) { n_led = v > MAKS ? MAKS : v; Serial.printf("LED sayisi %d\n", n_led); }
  else if (c == 'p' && v > 0) { parlak = v > 40 ? 40 : v; Serial.printf("parlaklik %%%d\n", parlak); }
  else if (c == 's') { sayim(); kip = '0'; }
  else if (c == 'r') { renk_sirasi(); kip = 'g'; }
  else if (strchr("gbf0", c)) kip = c;
  else Serial.println("komutlar: s sayim | n 24 | p 10 | r renkler | g gokkusagi | b nefes | f figurler | 0 sondur");
  if (kip == '0') hepsi(0, 0, 0);
}

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n== Halka denemesi (GPIO18) ==");
  rmt_var = rmtInit(HALKA_PIN, RMT_TX_MODE, RMT_MEM_NUM_BLOCKS_1, 10000000);
  Serial.println(rmt_var ? "RMT hazir" : "RMT BASLAMADI (cekirdek esp32 3.x mi?)");
  hepsi(0, 0, 0);
  Serial.printf("LED sayisi %d (degistir: n 24), parlaklik %%%d\n", n_led, parlak);
  renk_sirasi();
  Serial.println("komutlar: s sayim | n 24 | p 10 | r renkler | g gokkusagi | b nefes | f figurler | 0 sondur");
}

void loop() {
  if (Serial.available()) komut(Serial.readStringUntil('\n'));
  uint32_t t = millis();
  if (kip == 'g') {
    memset(kare, 0, sizeof kare);
    for (int i = 0; i < n_led; i++) {
      uint8_t r, g, b;
      renk_tekerlek(i * 768 / n_led + t / 4, &r, &g, &b);
      boya(i, r, g, b);
    }
    gonder();
  } else if (kip == 'b') {
    float k = 0.5f - 0.5f * cosf(t * 2 * PI / 4000.0f);
    uint8_t v = (uint8_t)(20 + 235 * k);
    hepsi(v, v, v);
  } else if (kip == 'f') {
    static int son = -1;
    int i = (t / 2000) % (sizeof FIGUR / sizeof FIGUR[0]);
    if (i != son) {
      son = i;
      Serial.printf("  %s\n", FIGUR[i].ad);
      hepsi(FIGUR[i].r, FIGUR[i].g, FIGUR[i].b);
    }
  }
  delay(33);
}
```

## Kod: `nfc_rc522_deneme/nfc_rc522_deneme.ino`

```cpp
// RC522 NFC okuyucu denemesi (ESP32-S3; ana yazılımdan bağımsız). Kütüphane: MFRC522 (GithubCommunity, 1.4.x).
//
// Bağlantı (docs/URUN_TANIMI.md): 3.3V -> 3V3 (5 V'A BAĞLAMA), GND, SCK 12, MISO 13, MOSI 11, SDA(SS) 10, RST 9,
// IRQ boş.
//
// Seri monitör 115200 (satır sonu: "Yeni satır"). Etiket konunca UID'si, türü ve (NTAG ise) figür kaydı yazılır;
// kaldırınca kaç saniye durduğu ve yoklamaların kaçında görüldüğü yazılır (stand kapağının içinden okuma sağlam mı).
// Komutlar:
//   y 3      standdaki NTAG etikete figür 3'ün kaydını yaz (Pepee; numaralar aşağıda, ayar kartı 200)
//   g        anten kazancı: en yüksek <-> varsayılan (okuma mesafesini dener)
#include <SPI.h>
#include <MFRC522.h>

#define NFC_SCK 12
#define NFC_MISO 13
#define NFC_MOSI 11
#define NFC_SS 10
#define NFC_RST 9
#define YOKLA_MS 250
#define KALKTI_MS 1000

static MFRC522 rc(NFC_SS, NFC_RST);

// data/figur_donanim.json (nfc_no -> ad)
static const char *figur_adi(int no) {
  static const char *AD[] = {"?", "Niloya", "Masa", "Pepee", "Keloglan", "Doru", "Hayri", "Sakir", "Elsa",
                             "Chase", "Orumcek Adam", "Hello Kitty", "Ay Dede (ninni)"};
  if (no == 200) return "Ayar karti";
  return no > 0 && no <= 12 ? AD[no] : "bilinmeyen numara";
}

// Kayıt (firmware/hikaye_oyuncak/etiket.h): sayfa 4-5 = "EKO", sürüm 1, nfc_no (2 B), CRC-16/CCITT-FALSE (2 B)
static uint16_t crc16(const uint8_t *p, int n) {
  uint16_t c = 0xFFFF;
  while (n--) {
    c ^= (uint16_t)(*p++) << 8;
    for (int k = 0; k < 8; k++) c = (c & 0x8000) ? (uint16_t)((c << 1) ^ 0x1021) : (uint16_t)(c << 1);
  }
  return c;
}
static int kayit_coz(const uint8_t *k) {
  if (k[0] != 'E' || k[1] != 'K' || k[2] != 'O' || k[3] != 1) return -1;
  if (crc16(k, 6) != (uint16_t)(k[6] | (k[7] << 8))) return -1;
  return k[4] | (k[5] << 8);
}
static void kayit_kodla(int no, uint8_t *k) {
  k[0] = 'E'; k[1] = 'K'; k[2] = 'O'; k[3] = 1;
  k[4] = no & 0xFF; k[5] = (no >> 8) & 0xFF;
  uint16_t c = crc16(k, 6);
  k[6] = c & 0xFF; k[7] = c >> 8;
}

static bool sec() {  // WUPA: alanda duran etiket her yoklamada yeniden seçilir
  byte atqa[2], boy = sizeof atqa;
  return rc.PICC_WakeupA(atqa, &boy) == MFRC522::STATUS_OK && rc.PICC_ReadCardSerial();
}
static void uid_yaz() {
  for (byte i = 0; i < rc.uid.size; i++) Serial.printf("%02X", rc.uid.uidByte[i]);
}

static bool var = false;
static uint8_t son_uid[10], son_n = 0;
static uint32_t ilk_ms = 0, son_gorulme = 0, yokla = 0;
static uint32_t yoklama = 0, gorulen = 0, kayip = 0;  // etiket dururken: yoklama, görüldüğü, son görülmeden beri ıska

static void etiket_geldi() {
  MFRC522::PICC_Type tur = MFRC522::PICC_GetType(rc.uid.sak);
  Serial.print("\nETIKET GELDI  UID ");
  uid_yaz();
  Serial.printf("  (%d bayt)  tur: %s\n", rc.uid.size, (const char *)MFRC522::PICC_GetTypeName(tur));
  if (tur != MFRC522::PICC_TYPE_MIFARE_UL) {
    Serial.println("  NTAG degil (or. kitle gelen MIFARE kart/anahtarlik): kayit yazilamaz, yalniz UID okunur.");
    return;
  }
  byte b[18], boy = sizeof b;
  if (rc.MIFARE_Read(3, b, &boy) != MFRC522::STATUS_OK) {  // sayfa 3-6: yetenek kabı + kayıt
    Serial.println("  bellek okunamadi (etiket kenarda olabilir)");
    return;
  }
  const char *model = b[2] == 0x12 ? "NTAG213" : b[2] == 0x3E ? "NTAG215" : b[2] == 0x6D ? "NTAG216" : "Ultralight/baska";
  int no = kayit_coz(b + 4);
  Serial.printf("  %s  sayfa 4-5: %02X %02X %02X %02X %02X %02X %02X %02X\n", model, b[4], b[5], b[6], b[7], b[8],
                b[9], b[10], b[11]);
  if (no > 0) Serial.printf("  KAYIT: figur %d = %s\n", no, figur_adi(no));
  else Serial.println("  kayit yok (bos etiket). Yazmak icin: y <numara>");
}

static void kayit_yaz(int no) {
  if (!sec()) { Serial.println("standda etiket yok"); return; }
  if (MFRC522::PICC_GetType(rc.uid.sak) != MFRC522::PICC_TYPE_MIFARE_UL) {
    Serial.println("bu etiket NTAG degil, yazilamaz");
    rc.PICC_HaltA();
    return;
  }
  uint8_t k[8];
  kayit_kodla(no, k);
  bool ok = rc.MIFARE_Ultralight_Write(4, k, 4) == MFRC522::STATUS_OK &&
            rc.MIFARE_Ultralight_Write(5, k + 4, 4) == MFRC522::STATUS_OK;
  byte b[18], boy = sizeof b;
  ok = ok && rc.MIFARE_Read(4, b, &boy) == MFRC522::STATUS_OK && !memcmp(b, k, 8);
  rc.PICC_HaltA();
  Serial.printf(ok ? "YAZILDI ve dogrulandi: figur %d = %s\n" : "YAZILAMADI (figur %d = %s); etiketi ortala, tekrar dene\n",
                no, figur_adi(no));
  var = false;  // bir sonraki yoklamada yeniden okunup gösterilir
}

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n== RC522 denemesi (SCK 12, MISO 13, MOSI 11, SDA 10, RST 9) ==");
  SPI.begin(NFC_SCK, NFC_MISO, NFC_MOSI, NFC_SS);
  rc.PCD_Init();
  delay(10);
  byte v = rc.PCD_ReadRegister(MFRC522::VersionReg);
  if (v == 0x00 || v == 0xFF) {
    Serial.printf("RC522 BULUNAMADI (surum 0x%02X). Kablolari ve 3,3 V'u denetle; sonra RST dugmesine bas.\n", v);
  } else {
    Serial.printf("RC522 bulundu, surum 0x%02X (%s)\n", v,
                  v == 0x91 ? "v1.0" : v == 0x92 ? "v2.0" : v == 0x88 || v == 0x18 || v == 0x12 ? "kopya yonga, calisir" : "?");
    rc.PCD_DumpVersionToSerial();
  }
  Serial.println("Figur numaralari: 1 Niloya, 2 Masa, 3 Pepee, 4 Keloglan, 5 Doru, 6 Hayri, 7 Sakir, 8 Elsa, 9 Chase,");
  Serial.println("  10 Orumcek Adam, 11 Hello Kitty, 12 Ay Dede, 200 ayar karti.  Komutlar: y <numara> | g");
}

void loop() {
  if (Serial.available()) {
    String s = Serial.readStringUntil('\n');
    s.trim();
    if (s.startsWith("y")) {
      int no = s.substring(1).toInt();
      if (no > 0) kayit_yaz(no);
      else Serial.println("ornek: y 3");
    } else if (s == "g") {
      bool en = rc.PCD_GetAntennaGain() != MFRC522::RxGain_max;
      rc.PCD_SetAntennaGain(en ? MFRC522::RxGain_max : MFRC522::RxGain_33dB);
      Serial.println(en ? "anten kazanci: EN YUKSEK (48 dB)" : "anten kazanci: varsayilan (33 dB)");
    }
  }
  uint32_t t = millis();
  if (t - yokla < YOKLA_MS) return;
  yokla = t;
  if (sec()) {
    bool ayni = rc.uid.size == son_n && !memcmp(rc.uid.uidByte, son_uid, son_n);
    if (!var || !ayni) {
      memcpy(son_uid, rc.uid.uidByte, rc.uid.size);
      son_n = rc.uid.size;
      var = true;
      ilk_ms = t;
      yoklama = gorulen = kayip = 0;
      etiket_geldi();
    }
    yoklama += kayip + 1;
    gorulen++;
    kayip = 0;
    son_gorulme = t;
    rc.PICC_HaltA();
  } else if (var) {
    kayip++;
    if (t - son_gorulme > KALKTI_MS) {
      Serial.printf("ETIKET KALKTI  %.1f s durdu, yoklamalarin %lu/%lu'unda goruldu\n", (son_gorulme - ilk_ms) / 1000.0f,
                    (unsigned long)gorulen, (unsigned long)yoklama);
      var = false;
    }
  }
}
```

## Kod: `nfc_pn5180_deneme/nfc_pn5180_deneme.ino`

```cpp
// PN5180 NFC okuyucu denemesi (ESP32-S3; ana yazılımdan bağımsız, kütüphane gerekmez: küçük sürücü aşağıda).
// Yalnız okur (ISO14443A: UID, NTAG figür kaydı). Etikete kayıt yazmak için RC522 denemesini kullan.
//
// Bağlantı: PN5180 kartında İKİ besleme var: 5V -> DevKit 5V (anten vericisi), 3.3V -> 3V3 (mantık), GND.
//   SCK 12, MISO 13, MOSI 11, NSS 10, RST 9 (RC522 ile aynı uçlar), BUSY -> GPIO8 (yeni uç). IRQ, GPIO, AUX, REQ boş.
//
// Seri monitör 115200. Etiket konunca UID, tür ve (NTAG ise) figür kaydı yazılır; kaldırınca kaç saniye durduğu ve
// yoklamaların kaçında görüldüğü yazılır (stand kapağının içinden okuma sağlam mı).
#include <SPI.h>

#define NFC_SCK 12
#define NFC_MISO 13
#define NFC_MOSI 11
#define PN_NSS 10
#define PN_RST 9
#define PN_BUSY 8
#define YOKLA_MS 250
#define KALKTI_MS 1000

// PN5180 komutları ve yazmaçları (NXP PN5180 veri sayfası)
enum { K_YAZ = 0x00, K_OR = 0x01, K_AND = 0x02, K_OKU = 0x04, K_EEPROM = 0x07, K_GONDER = 0x09, K_AL = 0x0A,
       K_RF_AYAR = 0x11, K_RF_AC = 0x16, K_RF_KAPA = 0x17 };
enum { R_SYSTEM_CONFIG = 0x00, R_IRQ_STATUS = 0x02, R_IRQ_CLEAR = 0x03, R_CRC_RX = 0x12, R_RX_STATUS = 0x13,
       R_CRC_TX = 0x19, R_RF_STATUS = 0x1D };

static const SPISettings PN_SPI(2000000, MSBFIRST, SPI_MODE0);
static bool busy_hatasi = false;

static bool busy_bekle(int seviye, uint32_t ms) {
  uint32_t t = millis();
  while (digitalRead(PN_BUSY) != seviye)
    if (millis() - t > ms) { busy_hatasi = true; return false; }
  return true;
}
// Bir komut çerçevesi yolla, isteğe bağlı yanıt çerçevesi al (BUSY el sıkışması: veri sayfası 11.4)
static bool pn_komut(const uint8_t *gonder, int gn, uint8_t *al = nullptr, int an = 0) {
  if (!busy_bekle(LOW, 100)) return false;
  SPI.beginTransaction(PN_SPI);
  digitalWrite(PN_NSS, LOW);
  delayMicroseconds(20);
  for (int i = 0; i < gn; i++) SPI.transfer(gonder[i]);
  bool ok = busy_bekle(HIGH, 20);
  digitalWrite(PN_NSS, HIGH);
  ok = busy_bekle(LOW, 100) && ok;
  if (ok && an) {
    digitalWrite(PN_NSS, LOW);
    delayMicroseconds(20);
    for (int i = 0; i < an; i++) al[i] = SPI.transfer(0xFF);
    ok = busy_bekle(HIGH, 20);
    digitalWrite(PN_NSS, HIGH);
    ok = busy_bekle(LOW, 100) && ok;
  }
  SPI.endTransaction();
  return ok;
}
static bool yaz(uint8_t komut, uint8_t r, uint32_t v) {
  uint8_t b[6] = {komut, r, (uint8_t)v, (uint8_t)(v >> 8), (uint8_t)(v >> 16), (uint8_t)(v >> 24)};
  return pn_komut(b, 6);
}
static bool oku(uint8_t r, uint32_t *v) {
  uint8_t b[2] = {K_OKU, r}, a[4];
  if (!pn_komut(b, 2, a, 4)) return false;
  *v = a[0] | (a[1] << 8) | (a[2] << 16) | ((uint32_t)a[3] << 24);
  return true;
}
// Etikete veri yolla (son baytın geçerli bit sayısı: 0 = 8) ve en çok ms içinde n baytlık yanıtı al; döner: alınan
static int aktar(const uint8_t *v, int n, uint8_t son_bit, uint8_t *yanit, int beklenen, uint32_t ms = 10) {
  uint32_t d;
  if (!yaz(K_AND, R_SYSTEM_CONFIG, 0xFFFFFFF8) || !yaz(K_OR, R_SYSTEM_CONFIG, 0x00000003)) return -1;  // boşta -> alıp-ver
  if (!oku(R_RF_STATUS, &d) || ((d >> 24) & 7) != 1) return -1;  // alıp-ver durumu: göndermeyi bekliyor
  yaz(K_YAZ, R_IRQ_CLEAR, 0xFFFFFFFF);
  uint8_t b[24] = {K_GONDER, son_bit};
  memcpy(b + 2, v, n);
  if (!pn_komut(b, n + 2)) return -1;
  uint32_t t = millis();
  do {
    d = 0;
    if (oku(R_IRQ_STATUS, &d) && (d & 1)) break;  // RX_IRQ: yanıt geldi
  } while (millis() - t < ms);
  if (!(d & 1)) return 0;
  oku(R_RX_STATUS, &d);
  int gelen = d & 0x1FF;
  if (gelen < beklenen) return gelen;
  uint8_t k[2] = {K_AL, 0x00};
  return pn_komut(k, 2, yanit, beklenen) ? beklenen : -1;
}
static void crc(bool acik) {
  if (acik) { yaz(K_OR, R_CRC_RX, 1); yaz(K_OR, R_CRC_TX, 1); }
  else { yaz(K_AND, R_CRC_RX, 0xFFFFFFFE); yaz(K_AND, R_CRC_TX, 0xFFFFFFFE); }
}

// ISO14443A etkinleştirme (REQA, çakışma önleme, seçme; 4 ya da 7 baytlık UID). Döner: UID uzunluğu ya da 0
static int etkinlestir(uint8_t *uid, uint8_t *sak) {
  uint8_t atqa[2], c[7], s[1];
  yaz(K_AND, R_SYSTEM_CONFIG, 0xFFFFFFBF);  // Crypto1 kapalı
  crc(false);
  c[0] = 0x26;  // REQA, 7 bit
  if (aktar(c, 1, 7, atqa, 2) != 2) return 0;
  int n = 0;
  for (int duzey = 0; duzey < 2; duzey++) {
    uint8_t sel = duzey ? 0x95 : 0x93, a[5];
    crc(false);
    c[0] = sel; c[1] = 0x20;
    if (aktar(c, 2, 0, a, 5) != 5) return 0;
    if ((a[0] ^ a[1] ^ a[2] ^ a[3]) != a[4]) return 0;  // BCC tutmuyor
    crc(true);
    c[0] = sel; c[1] = 0x70;
    memcpy(c + 2, a, 5);
    if (aktar(c, 7, 0, s, 1) != 1) return 0;
    *sak = s[0];
    if (s[0] & 0x04) {            // UID sürüyor: ilk bayt 0x88 (CT), 3 bayt UID
      if (a[0] != 0x88) return 0;
      memcpy(uid + n, a + 1, 3);
      n += 3;
    } else {
      memcpy(uid + n, a, 4);
      return n + 4;
    }
  }
  return 0;
}

static bool pn_kur() {
  pinMode(PN_NSS, OUTPUT);
  digitalWrite(PN_NSS, HIGH);
  pinMode(PN_BUSY, INPUT);
  pinMode(PN_RST, OUTPUT);
  digitalWrite(PN_RST, LOW);
  delay(10);
  digitalWrite(PN_RST, HIGH);
  delay(50);
  SPI.begin(NFC_SCK, NFC_MISO, NFC_MOSI, PN_NSS);
  uint8_t k[3] = {K_EEPROM, 0x10, 6}, e[6];
  busy_hatasi = false;
  if (!pn_komut(k, 3, e, 6)) {
    Serial.println(busy_hatasi ? "PN5180 YANIT VERMIYOR: BUSY (GPIO8), RST (9), 3,3 V ve 5 V baglantilarini denetle"
                               : "PN5180 YANIT VERMIYOR");
    return false;
  }
  // EEPROM 0x10 ürün, 0x12 yazılım, 0x14 EEPROM sürümü (her biri 2 bayt: küçük, büyük)
  if ((e[0] == 0xFF && e[1] == 0xFF) || (e[0] == 0 && e[1] == 0)) {
    Serial.printf("PN5180 surumu okunamadi (%02X %02X): MISO/MOSI/SCK kablolari?\n", e[0], e[1]);
    return false;
  }
  Serial.printf("PN5180 bulundu: urun %d.%d, yazilim %d.%d, EEPROM %d.%d\n", e[1], e[0], e[3], e[2], e[5], e[4]);
  return true;
}

// data/figur_donanim.json (nfc_no -> ad)
static const char *figur_adi(int no) {
  static const char *AD[] = {"?", "Niloya", "Masa", "Pepee", "Keloglan", "Doru", "Hayri", "Sakir", "Elsa",
                             "Chase", "Orumcek Adam", "Hello Kitty", "Ay Dede (ninni)"};
  if (no == 200) return "Ayar karti";
  return no > 0 && no <= 12 ? AD[no] : "bilinmeyen numara";
}
// Kayıt (firmware/hikaye_oyuncak/etiket.h): sayfa 4-5 = "EKO", sürüm 1, nfc_no (2 B), CRC-16/CCITT-FALSE (2 B)
static int kayit_coz(const uint8_t *k) {
  if (k[0] != 'E' || k[1] != 'K' || k[2] != 'O' || k[3] != 1) return -1;
  uint16_t c = 0xFFFF;
  for (int i = 0; i < 6; i++) {
    c ^= (uint16_t)k[i] << 8;
    for (int j = 0; j < 8; j++) c = (c & 0x8000) ? (uint16_t)((c << 1) ^ 0x1021) : (uint16_t)(c << 1);
  }
  return c == (uint16_t)(k[6] | (k[7] << 8)) ? (k[4] | (k[5] << 8)) : -1;
}

static bool hazir = false, var = false;
static uint8_t son_uid[10], son_n = 0;
static uint32_t ilk_ms = 0, son_gorulme = 0, yokla = 0;
static uint32_t yoklama = 0, gorulen = 0, kayip = 0;  // etiket dururken: yoklama, görüldüğü, son görülmeden beri ıska

static void etiket_geldi(const uint8_t *uid, int n, uint8_t sak) {
  Serial.print("\nETIKET GELDI  UID ");
  for (int i = 0; i < n; i++) Serial.printf("%02X", uid[i]);
  Serial.printf("  (%d bayt)  SAK %02X\n", n, sak);
  if (sak != 0x00) {
    Serial.println(sak == 0x08 || sak == 0x18 ? "  MIFARE Classic (kitle gelen kart/anahtarlik): yalniz UID okunur."
                                              : "  NTAG degil: yalniz UID okunur.");
    return;
  }
  uint8_t c[2] = {0x30, 3}, b[16];  // READ sayfa 3-6: yetenek kabı + kayıt
  if (aktar(c, 2, 0, b, 16) != 16) {
    Serial.println("  bellek okunamadi (etiket kenarda olabilir)");
    return;
  }
  const char *model = b[2] == 0x12 ? "NTAG213" : b[2] == 0x3E ? "NTAG215" : b[2] == 0x6D ? "NTAG216" : "Ultralight/baska";
  int no = kayit_coz(b + 4);
  Serial.printf("  %s  sayfa 4-5: %02X %02X %02X %02X %02X %02X %02X %02X\n", model, b[4], b[5], b[6], b[7], b[8],
                b[9], b[10], b[11]);
  if (no > 0) Serial.printf("  KAYIT: figur %d = %s\n", no, figur_adi(no));
  else Serial.println("  kayit yok (bos etiket; RC522 denemesiyle \"y <numara>\" yazilir)");
}

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n== PN5180 denemesi (SCK 12, MISO 13, MOSI 11, NSS 10, RST 9, BUSY 8; 5V + 3V3) ==");
  hazir = pn_kur();
  if (!hazir) Serial.println("Duzeltip karttaki RST dugmesine bas.");
}

void loop() {
  uint32_t t = millis();
  if (!hazir || t - yokla < YOKLA_MS) return;
  yokla = t;
  // Her yoklamada alan açılır, etiket aranır, alan kapanır (etiket her seferinde baştan uyanır; az akım)
  uint8_t rf[3] = {K_RF_AYAR, 0x00, 0x80};  // ISO14443A 106 kbit/s
  uint8_t ac[2] = {K_RF_AC, 0x00}, kapa[2] = {K_RF_KAPA, 0x00};
  uint8_t uid[10], sak = 0;
  int n = 0;
  if (pn_komut(rf, 3) && pn_komut(ac, 2)) {
    delay(5);  // etiket güç alsın
    n = etkinlestir(uid, &sak);
    if (n) {
      bool ayni = n == son_n && !memcmp(uid, son_uid, n);
      if (!var || !ayni) {
        memcpy(son_uid, uid, n);
        son_n = n;
        var = true;
        ilk_ms = t;
        yoklama = gorulen = kayip = 0;
        etiket_geldi(uid, n, sak);
      }
      yoklama += kayip + 1;
      gorulen++;
      kayip = 0;
      son_gorulme = t;
    }
  }
  pn_komut(kapa, 2);
  if (!n && var) {
    kayip++;
    if (t - son_gorulme > KALKTI_MS) {
      Serial.printf("ETIKET KALKTI  %.1f s durdu, yoklamalarin %lu/%lu'unda goruldu\n", (son_gorulme - ilk_ms) / 1000.0f,
                    (unsigned long)gorulen, (unsigned long)yoklama);
      var = false;
    }
  }
  if (busy_hatasi) {
    Serial.println("BUSY zaman asimi: baglanti koptu mu? (BUSY GPIO8)");
    busy_hatasi = false;
  }
}
```
