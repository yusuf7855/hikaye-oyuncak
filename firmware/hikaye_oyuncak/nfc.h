// NFC/RFID figür okuyucu arayüzü: figürün tabanındaki etiketin UID'si -> figür numarası (NFC_TABLO).
//
//   nfc_kur()           okuyucuyu başlatır; okuyucu yoksa ya da NFC_OKUYUCU 0 ise false
//   nfc_uid_oku(u, k)   alandaki etiketin UID'si: bayt sayısı (4/7/10) ya da 0 (etiket yok)
//   nfc_figur(u, n)     NFC_TABLO'dan figür (0..N_FIGUR-1) ya da -1 (bilinmeyen etiket)
//
// NFC_OKUYUCU (donanim.h): 0 = taslak (okuyucu yok; seri porttan "n 04A1B2C3" ile etiket denenir), 1 = RC522 (SPI,
// "MFRC522" kütüphanesi), 2 = PN532 (I2C, "Adafruit PN532" kütüphanesi). 1 ve 2 kartta denenmedi (taslak sürücü).
// Etiket UID'leri: okuyucuya bilinmeyen etiket konunca seri porta "bilinmeyen etiket: 04A1B2C3" yazılır; onu
// figürüyle birlikte NFC_TABLO'ya ekleyin.
#pragma once
#include <stdint.h>
#include <string.h>

typedef struct {
  uint8_t uid[10];
  uint8_t n;
  int8_t figur;  // 0: Niloya ... 10: Hello Kitty (istemler.h FIGUR_AD sırası)
} NfcEtiket;

static const NfcEtiket NFC_TABLO[] = {
    // örnek UID'ler (kendi etiketlerinizinkini yazın)
    {{0x04, 0xA1, 0xB2, 0xC3}, 4, 0},                    // Niloya
    {{0x04, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66}, 7, 7},  // Elsa (7 baytlık NTAG UID örneği)
};

static int nfc_figur(const uint8_t *uid, int n) {
  for (size_t i = 0; i < sizeof NFC_TABLO / sizeof NFC_TABLO[0]; i++)
    if (NFC_TABLO[i].n == n && !memcmp(NFC_TABLO[i].uid, uid, (size_t)n)) return NFC_TABLO[i].figur;
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
static int nfc_uid_oku(uint8_t *uid, int kap) {
  // Etiket alanda kaldıkça her seferinde okunabilsin: WUPA (IsNewCardPresent yalnız yeni kartı görür)
  byte atqa[2], boy = sizeof atqa;
  if (nfc_rc522.PICC_WakeupA(atqa, &boy) != MFRC522::STATUS_OK || !nfc_rc522.PICC_ReadCardSerial()) return 0;
  int n = nfc_rc522.uid.size < kap ? nfc_rc522.uid.size : kap;
  memcpy(uid, nfc_rc522.uid.uidByte, n);
  nfc_rc522.PICC_HaltA();
  return n;
}
#elif NFC_OKUYUCU == 2
#include <Wire.h>
#include <Adafruit_PN532.h>
static Adafruit_PN532 nfc_pn532(NFC_IRQ_PIN, NFC_RST_PIN, &Wire);
static bool nfc_kur(void) {
  Wire.begin(NFC_I2C_SDA, NFC_I2C_SCL);
  nfc_pn532.begin();
  if (!nfc_pn532.getFirmwareVersion()) return false;
  nfc_pn532.SAMConfig();
  return true;
}
static int nfc_uid_oku(uint8_t *uid, int kap) {
  uint8_t u[10], n = 0;
  if (!nfc_pn532.readPassiveTargetID(PN532_MIFARE_ISO14443A, u, &n, 30)) return 0;  // en çok 30 ms bekler
  if (n > kap) n = (uint8_t)kap;
  memcpy(uid, u, n);
  return n;
}
#else  // taslak: okuyucu yok
static bool nfc_kur(void) { return false; }
static int nfc_uid_oku(uint8_t *, int) { return 0; }
#endif
