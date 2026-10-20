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
