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
