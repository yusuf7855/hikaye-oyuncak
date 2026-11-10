// Üretildi: tools/basliklar.py (data/figur_donanim.json, sürüm 3). Donanım figürü d (0..DONANIM_N-1):
// etiketteki nfc_no, halka rengi, mod (hikâye / uyku = ninni) ve modeldeki figür numarası
// (istemler.h FIGUR_*; -1: model bu figürü bilmiyor, yerleşik metin okunur).
#pragma once
#include <stdint.h>
#define DONANIM_N 14
#define DONANIM_SURUM 3
#define AYAR_KARTI_NFC 200
enum { MOD_HIKAYE = 0, MOD_UYKU = 1 };
static const char *const DONANIM_KIMLIK[14] = {
  "keloglan", "gece", "pamuk_prenses", "pinokyo", "alaaddin", "nasreddin_hoca", "bulut", "zipzip", "tontis",
  "bilge_baykus", "ejderha_yavrusu", "tek_boynuzlu_at", "bip", "fistik"
};
static const char *const DONANIM_AD[14] = {
  "Kelo\xc4\x9flan", "Ay Dede", "Pamuk Prenses", "Pinokyo", "Alaaddin", "Nasreddin Hoca", "Bulut", "Z\xc4\xb1pz\xc4\xb1p",
  "Tonti\xc5\x9f", "Bilge Bayku\xc5\x9f", "Ejderha Yavrusu", "Tek Boynuzlu At", "Bip", "F\xc4\xb1st\xc4\xb1k"
};
static const uint16_t DONANIM_NFC[14] = {
  4, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
};
static const uint8_t DONANIM_RENK[42] = {
  126, 211, 33, 59, 63, 216, 255, 90, 122, 232, 163, 61, 138, 79, 255, 46, 158, 91, 255, 255, 255, 255, 158, 199,
  126, 211, 33, 181, 121, 58, 31, 181, 176, 199, 125, 255, 59, 130, 246, 156, 163, 175
};
static const uint8_t DONANIM_MOD[14] = {
  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
};
static const int8_t DONANIM_MODEL[14] = {
  0, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
};
static const uint8_t AYAR_KARTI_RENK[3] = {
  0, 229, 200
};
