// Üretildi: tools/basliklar.py (data/figur_donanim.json, sürüm 2). Donanım figürü d (0..DONANIM_N-1):
// etiketteki nfc_no, halka rengi, mod (hikâye / uyku = ninni) ve modeldeki figür numarası
// (istemler.h FIGUR_*; -1: model bu figürü bilmiyor, yerleşik metin okunur).
#pragma once
#include <stdint.h>
#define DONANIM_N 12
#define DONANIM_SURUM 2
#define AYAR_KARTI_NFC 200
enum { MOD_HIKAYE = 0, MOD_UYKU = 1 };
static const char *const DONANIM_KIMLIK[12] = {
  "niloya", "masa", "pepee", "keloglan", "doru", "hayri", "sakir", "elsa", "chase", "orumcek_adam", "hello_kitty",
  "gece"
};
static const char *const DONANIM_AD[12] = {
  "Niloya", "Ma\xc5\x9f" "a", "Pepee", "Kelo\xc4\x9flan", "Doru", "Hayri", "\xc5\x9e" "akir", "Elsa", "Chase",
  "\xc3\x96r\xc3\xbcmcek Adam", "Hello Kitty", "Ay Dede"
};
static const uint16_t DONANIM_NFC[12] = {
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
};
static const uint8_t DONANIM_RENK[36] = {
  255, 111, 168, 180, 92, 255, 255, 138, 31, 126, 211, 33, 201, 128, 46, 255, 194, 26, 255, 228, 92, 127, 219, 255,
  37, 99, 255, 232, 32, 46, 255, 255, 255, 59, 63, 216
};
static const uint8_t DONANIM_MOD[12] = {
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
};
static const int8_t DONANIM_MODEL[12] = {
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1
};
static const uint8_t AYAR_KARTI_RENK[3] = {
  0, 229, 200
};
