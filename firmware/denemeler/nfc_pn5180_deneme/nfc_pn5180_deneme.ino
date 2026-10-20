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
