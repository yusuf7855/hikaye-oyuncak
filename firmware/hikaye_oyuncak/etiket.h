// Figür etiketinin kaydı: NTAG213/215 kullanıcı belleğinin ilk iki sayfası (sayfa 4-5, 8 bayt).
//
//   [0..3)  sihir "EKO"
//   [3]     sürüm (ETIKET_SURUM)
//   [4..6)  nfc_no, küçük uçlu (data/figur_donanim.json: figür 1.., ayar kartı 200; numara asla yeniden kullanılmaz)
//   [6..8)  CRC-16/CCITT-FALSE (çokterim 0x1021, başlangıç 0xFFFF) [0..6) üzerinden, küçük uçlu
//
// Sayfa 0-3 (UID, kilit, yetenek kabı) dokunulmaz. Fabrikadan gelen NTAG'da sayfa 4'te boş NDEF TLV (03 00 FE) durur:
// kayıt onun üzerine yazılır (etiket artık telefona NDEF göstermez; ürün için gerekmez). Okuma: nfc.h etiketi görünce
// sayfa 4'ten 16 bayt okur (READ komutu 4 sayfa verir); kayıt yoksa ya da bozuksa UID tablosuna düşülür.
// Yazma ("oyuncak tanıt"): iki sayfa yazılır, geri okunup karşılaştırılır. Saf C: tools/urun_test.c dener.
#pragma once
#include <stdint.h>
#include <string.h>

#define ETIKET_SAYFA 4         // kaydın ilk sayfası
#define ETIKET_BAYT 8          // kayıt uzunluğu (2 sayfa)
#define ETIKET_SURUM 1
#define ETIKET_AYAR_NO 200     // ayar kartı (data/figur_donanim.json ozel_kartlar)

static const uint8_t ETIKET_SIHIR[3] = {'E', 'K', 'O'};

static inline uint16_t etiket_crc16(const uint8_t *p, int n) {
  uint16_t c = 0xFFFF;
  while (n--) {
    c ^= (uint16_t)(*p++) << 8;
    for (int k = 0; k < 8; k++) c = (c & 0x8000) ? (uint16_t)((c << 1) ^ 0x1021) : (uint16_t)(c << 1);
  }
  return c;
}

static inline void etiket_kodla(int nfc_no, uint8_t out[ETIKET_BAYT]) {
  memcpy(out, ETIKET_SIHIR, 3);
  out[3] = ETIKET_SURUM;
  out[4] = (uint8_t)(nfc_no & 0xFF);
  out[5] = (uint8_t)((nfc_no >> 8) & 0xFF);
  uint16_t c = etiket_crc16(out, 6);
  out[6] = (uint8_t)(c & 0xFF);
  out[7] = (uint8_t)(c >> 8);
}

// Döner: nfc_no (1..65535) ya da -1 (sihir yok / sürüm tanınmıyor / CRC tutmuyor / numara 0)
static inline int etiket_coz(const uint8_t in[ETIKET_BAYT]) {
  if (memcmp(in, ETIKET_SIHIR, 3) || in[3] != ETIKET_SURUM) return -1;
  if (etiket_crc16(in, 6) != (uint16_t)(in[6] | (in[7] << 8))) return -1;
  int no = in[4] | (in[5] << 8);
  return no ? no : -1;
}
