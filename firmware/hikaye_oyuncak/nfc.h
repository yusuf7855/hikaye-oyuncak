// NFC stand okuyucusu: standdaki etiketin UID'si ve kaydı (etiket.h: sihir + sürüm + nfc_no + CRC, NTAG sayfa 4-5).
//
// Sürücü arayüzü (her okuyucu için aynı):
//   nfc_kur()                okuyucuyu başlatır; yoksa false
//   nfc_uid_oku(u, kap)      alandaki etiketin UID'si: bayt sayısı (4/7/10) ya da 0 (etiket yok)
//   nfc_oku16(sayfa, b)      sayfa..sayfa+3 (16 B) okur (NTAG READ); 0 tamam
//   nfc_sayfa_yaz(sayfa, b)  bir sayfa (4 B) yazar (NTAG WRITE); 0 tamam
// Ortak:
//   nfc_etiket_no(u, n)      etiketin nfc_no'su: önce kayıt (sayfa 4), yoksa UID tablosu (NFC_TABLO); yoksa -1
//   nfc_kayit_yaz(no, u, n)  "oyuncak tanıt": UID'si u olan etikete kaydı yazar, geri okuyup doğrular
//
// NFC_OKUYUCU (donanim.h): 1 = RC522 (ürün; SPI, "MFRC522" kütüphanesi), 2 = PN532 (aynı SPI uçlarında; modülün
// anahtarları SPI'ye alınır; "Adafruit PN532" kütüphanesi), 0 = taslak: okuyucu yok, alan bellekte taklit edilir
// (seri porttan "n koy 3", "n koy bos", "n koy uid 04A1B2C3", "n kaldir"; bilgisayarda tools/kart_pc "#etiket ...",
// etiket belleği dosyada da durabilir). 1 ve 2 kartta denenmedi.
// Kaydı olmayan etiket (ör. RC522 kitindeki MIFARE Classic kart) UID'siyle NFC_TABLO'da aranır: bilinmeyen etiket
// konunca seri porta "bilinmeyen etiket: 04A1B2C3" yazılır.
#pragma once
#include <stdint.h>
#include <string.h>
#include "etiket.h"

typedef struct {
  uint8_t uid[10];
  uint8_t n;
  uint16_t nfc_no;  // data/figur_donanim.json: figür 1.., ayar kartı 200
} NfcEtiket;

static const NfcEtiket NFC_TABLO[] = {
    // örnek UID'ler (kayıt yazılamayan etiketler için; kendi etiketlerinizinkini yazın)
    {{0x04, 0xA1, 0xB2, 0xC3}, 4, 1},                    // Niloya
    {{0x04, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66}, 7, 8},  // Elsa (7 baytlık NTAG UID örneği)
};

static int nfc_tablo_no(const uint8_t *uid, int n) {
  for (size_t i = 0; i < sizeof NFC_TABLO / sizeof NFC_TABLO[0]; i++)
    if (NFC_TABLO[i].n == n && !memcmp(NFC_TABLO[i].uid, uid, (size_t)n)) return NFC_TABLO[i].nfc_no;
  return -1;
}

#if NFC_OKUYUCU == 1
#include <SPI.h>
#include <MFRC522.h>
static MFRC522 nfc_rc522(NFC_SPI_SS, NFC_RST_PIN);
static bool nfc_kur(void) {
  SPI.begin(NFC_SPI_SCK, NFC_SPI_MISO, NFC_SPI_MOSI, NFC_SPI_SS);
  nfc_rc522.PCD_Init();
  byte v = nfc_rc522.PCD_ReadRegister(MFRC522::VersionReg);
  return v != 0x00 && v != 0xFF;
}
// Etiketi uyandırıp seçer (WUPA: etiket alanda kaldıkça HALT'tan da uyanır; IsNewCardPresent yalnız yeni kartı görür)
static bool nfc_sec(void) {
  byte atqa[2], boy = sizeof atqa;
  return nfc_rc522.PICC_WakeupA(atqa, &boy) == MFRC522::STATUS_OK && nfc_rc522.PICC_ReadCardSerial();
}
static int nfc_uid_oku(uint8_t *uid, int kap) {
  if (!nfc_sec()) return 0;
  int n = nfc_rc522.uid.size < kap ? nfc_rc522.uid.size : kap;
  memcpy(uid, nfc_rc522.uid.uidByte, n);
  nfc_rc522.PICC_HaltA();
  return n;
}
static int nfc_oku16(int sayfa, uint8_t *out) {
  if (!nfc_sec()) return -1;
  if (MFRC522::PICC_GetType(nfc_rc522.uid.sak) != MFRC522::PICC_TYPE_MIFARE_UL) { nfc_rc522.PICC_HaltA(); return -2; }
  byte b[18], boy = sizeof b;
  MFRC522::StatusCode d = nfc_rc522.MIFARE_Read((byte)sayfa, b, &boy);
  nfc_rc522.PICC_HaltA();
  if (d != MFRC522::STATUS_OK) return -1;
  memcpy(out, b, 16);
  return 0;
}
static int nfc_sayfa_yaz(int sayfa, const uint8_t *in) {
  if (!nfc_sec()) return -1;
  if (MFRC522::PICC_GetType(nfc_rc522.uid.sak) != MFRC522::PICC_TYPE_MIFARE_UL) { nfc_rc522.PICC_HaltA(); return -2; }
  byte b[4];
  memcpy(b, in, 4);
  MFRC522::StatusCode d = nfc_rc522.MIFARE_Ultralight_Write((byte)sayfa, b, 4);
  nfc_rc522.PICC_HaltA();
  return d == MFRC522::STATUS_OK ? 0 : -1;
}
static const char *NFC_AD = "RC522";
#elif NFC_OKUYUCU == 2
#include <SPI.h>
#include <Adafruit_PN532.h>
static Adafruit_PN532 nfc_pn532(NFC_SPI_SS, &SPI);
static bool nfc_kur(void) {
  pinMode(NFC_RST_PIN, OUTPUT);  // PN532 RSTPDN: yüksek = çalışır
  digitalWrite(NFC_RST_PIN, LOW);
  delay(5);
  digitalWrite(NFC_RST_PIN, HIGH);
  delay(10);
  SPI.begin(NFC_SPI_SCK, NFC_SPI_MISO, NFC_SPI_MOSI, NFC_SPI_SS);  // kütüphanenin SPI.begin()'i bunu değiştirmez
  if (!nfc_pn532.begin() || !nfc_pn532.getFirmwareVersion()) return false;
  nfc_pn532.SAMConfig();
  return true;
}
static uint8_t nfc_pn_uid_n = 0;
static bool nfc_sec(uint8_t *u = NULL) {
  uint8_t b[10];
  nfc_pn_uid_n = 0;
  return nfc_pn532.readPassiveTargetID(PN532_MIFARE_ISO14443A, u ? u : b, &nfc_pn_uid_n, 30);  // en çok 30 ms
}
static int nfc_uid_oku(uint8_t *uid, int kap) {
  uint8_t u[10];
  if (!nfc_sec(u)) return 0;
  int n = nfc_pn_uid_n < kap ? nfc_pn_uid_n : kap;
  memcpy(uid, u, n);
  return n;
}
static int nfc_oku16(int sayfa, uint8_t *out) {
  if (!nfc_sec() || nfc_pn_uid_n != 7) return -2;  // NTAG: 7 baytlık UID
  for (int p = 0; p < 4; p++)
    if (!nfc_pn532.ntag2xx_ReadPage((uint8_t)(sayfa + p), out + 4 * p)) return -1;
  return 0;
}
static int nfc_sayfa_yaz(int sayfa, const uint8_t *in) {
  if (!nfc_sec() || nfc_pn_uid_n != 7) return -2;
  uint8_t b[4];
  memcpy(b, in, 4);
  return nfc_pn532.ntag2xx_WritePage((uint8_t)sayfa, b) ? 0 : -1;
}
static const char *NFC_AD = "PN532";
#else  // taslak: okuyucu yok, alandaki etiket bellekte taklit edilir (NTAG213: 45 sayfa)
#define NFC_SAHTE_SAYFA 45
typedef struct {
  bool alanda, ntag, kilitli;
  uint8_t uid[7], uid_n;
  uint8_t bellek[NFC_SAHTE_SAYFA * 4];
} NfcSahte;
static NfcSahte nfc_sahte;
#ifndef NFC_SAHTE_YAZILDI
#define NFC_SAHTE_YAZILDI()  // bilgisayardaki deneme: etiket belleği dosyaya geri yazılır
#endif
// Fabrikadan çıkmış boş NTAG213 (ntag false: NTAG olmayan etiket, ör. MIFARE Classic: yalnız UID okunur)
static void nfc_sahte_koy_bos(const uint8_t *uid, int n, bool ntag) {
  memset(&nfc_sahte, 0, sizeof nfc_sahte);
  nfc_sahte.uid_n = (uint8_t)(n > 7 ? 7 : n);
  memcpy(nfc_sahte.uid, uid, nfc_sahte.uid_n);
  memcpy(nfc_sahte.bellek, uid, nfc_sahte.uid_n < 8 ? nfc_sahte.uid_n : 8);
  static const uint8_t CC[4] = {0xE1, 0x10, 0x12, 0x00}, TLV[4] = {0x03, 0x00, 0xFE, 0x00};
  memcpy(nfc_sahte.bellek + 12, CC, 4);
  memcpy(nfc_sahte.bellek + 16, TLV, 4);
  nfc_sahte.ntag = ntag;
  nfc_sahte.alanda = true;
}
// Programlanmış figür etiketi (UID nfc_no'dan türetilir)
static void nfc_sahte_koy_no(int no) {
  const uint8_t uid[7] = {0x04, 0xEC, 0x0A, (uint8_t)(no >> 8), (uint8_t)no, 0x5A, 0x80};
  nfc_sahte_koy_bos(uid, 7, true);
  etiket_kodla(no, nfc_sahte.bellek + ETIKET_SAYFA * 4);
}
static void nfc_sahte_kaldir(void) { nfc_sahte.alanda = false; }
static bool nfc_kur(void) { return true; }
static int nfc_uid_oku(uint8_t *uid, int kap) {
  if (!nfc_sahte.alanda) return 0;
  int n = nfc_sahte.uid_n < kap ? nfc_sahte.uid_n : kap;
  memcpy(uid, nfc_sahte.uid, n);
  return n;
}
static int nfc_oku16(int sayfa, uint8_t *out) {
  if (!nfc_sahte.alanda) return -1;
  if (!nfc_sahte.ntag) return -2;
  for (int i = 0; i < 16; i++) out[i] = nfc_sahte.bellek[((sayfa * 4 + i) % (NFC_SAHTE_SAYFA * 4))];
  return 0;
}
static int nfc_sayfa_yaz(int sayfa, const uint8_t *in) {
  if (!nfc_sahte.alanda) return -1;
  if (!nfc_sahte.ntag) return -2;
  if (nfc_sahte.kilitli || sayfa < 4 || sayfa >= NFC_SAHTE_SAYFA - 5) return -1;  // kilitli ya da kullanıcı belleği dışı
  memcpy(nfc_sahte.bellek + sayfa * 4, in, 4);
  NFC_SAHTE_YAZILDI();
  return 0;
}
static const char *NFC_AD = "taslak (okuyucu yok)";
#endif

// Etiketin nfc_no'su: kayıt, yoksa UID tablosu; ikisi de yoksa -1. kayit_var: kayıttan mı okundu.
static int nfc_etiket_no(const uint8_t *uid, int n, bool *kayit_var) {
  uint8_t b[16];
  int no = nfc_oku16(ETIKET_SAYFA, b) == 0 ? etiket_coz(b) : -1;
  if (kayit_var) *kayit_var = no > 0;
  return no > 0 ? no : nfc_tablo_no(uid, n);
}

enum { NFC_YAZ_TAMAM = 0, NFC_YAZ_ETIKET_YOK = -1, NFC_YAZ_OLMADI = -2, NFC_YAZ_DOGRULANMADI = -3, NFC_YAZ_NTAG_DEGIL = -4 };
static const char *const NFC_YAZ_AD[5] = {"tamam", "etiket yok ya da değişti", "yazılamadı (kilitli?)",
                                          "doğrulanamadı", "NTAG213/215 değil"};

// "Oyuncak tanıt": UID'si uid olan etikete no'yu yazar, geri okuyup karşılaştırır.
static int nfc_kayit_yaz(int no, const uint8_t *uid, int n) {
  uint8_t u[10], k[ETIKET_BAYT], b[16];
  if (nfc_uid_oku(u, sizeof u) != n || memcmp(u, uid, (size_t)n)) return NFC_YAZ_ETIKET_YOK;
  etiket_kodla(no, k);
  for (int p = 0; p < ETIKET_BAYT / 4; p++) {
    int r = nfc_sayfa_yaz(ETIKET_SAYFA + p, k + 4 * p);
    if (r == -2) return NFC_YAZ_NTAG_DEGIL;
    if (r) return NFC_YAZ_OLMADI;
  }
  if (nfc_oku16(ETIKET_SAYFA, b) || memcmp(b, k, ETIKET_BAYT) || etiket_coz(b) != no) return NFC_YAZ_DOGRULANMADI;
  return NFC_YAZ_TAMAM;
}
