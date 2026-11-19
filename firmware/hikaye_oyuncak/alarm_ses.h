// Yüklenen alarm sesi: flash'taki "alarm" bölümünde (partitions.csv, data alt tip 0x43, 44 KB: ses bölümünün
// boşalan sonu) tek bir kısa ses.
//
// Ayar sayfası, telefonda seçilen ses dosyasını (mp3, m4a, wav ...) tarayıcıda çözer, tek kanala ve 8 kHz'e indirir,
// en çok ALARM_SES_SN saniyesini alır, tepe değerini düzler ve IMA ADPCM'e (4 bit/örnek, 4 KB/s) çevirir; oyuncağa
// başlık + veri olarak yükler (ayar_sayfa.h, aynı kodlayıcının JavaScript'i). Oyuncak çalarken çözer ve 16 kHz'e
// (doğrusal ara değerle) çıkarır.
//
//   [0..64)   AlarmSesBaslik (sihir "EKAL", sürüm, örnek hızı, örnek sayısı, verinin CRC-32'si, dosya adı)
//   [64..)    IMA ADPCM: örnek başına 4 bit, baytın düşük yarısı önce; başlangıç tahmini 0, adım indeksi 0
//
// Kodlayıcı ve çözücü tamsayıdır: C, JavaScript ve Python aynı baytları üretir (tools/urun_test.c, tools/alarm_ses_test.py).
#pragma once
#include <stdint.h>
#include <string.h>

#define ALARM_SES_SIHIR 0x4C414B45u  // "EKAL" (küçük uçlu)
#define ALARM_SES_SURUM 1
#define ALARM_SES_SR 8000
#define ALARM_SES_SN 10
#define ALARM_SES_BASLIK 64
#define ALARM_SES_ORNEK_MAKS (ALARM_SES_SR * ALARM_SES_SN)

typedef struct {
  uint32_t sihir;
  uint16_t surum, sr;
  uint32_t n;          // örnek sayısı
  uint32_t crc;        // CRC-32 (IEEE) veri baytları ((n + 1) / 2) üzerinden
  char ad[48];         // gösterilecek ad (UTF-8, NUL ile biter)
} AlarmSesBaslik;
typedef char alarm_ses_baslik_64[sizeof(AlarmSesBaslik) == ALARM_SES_BASLIK ? 1 : -1];

static const int16_t ADPCM_ADIM[89] = {
    7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66, 73, 80, 88, 97, 107,
    118, 130, 143, 157, 173, 190, 209, 230, 253, 279, 307, 337, 371, 408, 449, 494, 544, 598, 658, 724, 796, 876, 963,
    1060, 1166, 1282, 1411, 1552, 1707, 1878, 2066, 2272, 2499, 2749, 3024, 3327, 3660, 4026, 4428, 4871, 5358, 5894,
    6484, 7132, 7845, 8630, 9493, 10442, 11487, 12635, 13899, 15289, 16818, 18500, 20350, 22385, 24623, 27086, 29794,
    32767};
static const int8_t ADPCM_INDEKS[16] = {-1, -1, -1, -1, 2, 4, 6, 8, -1, -1, -1, -1, 2, 4, 6, 8};

typedef struct { int32_t tahmin; int32_t indeks; } Adpcm;

static inline int16_t adpcm_coz1(Adpcm *s, int nib) {
  int32_t adim = ADPCM_ADIM[s->indeks], fark = adim >> 3;
  if (nib & 4) fark += adim;
  if (nib & 2) fark += adim >> 1;
  if (nib & 1) fark += adim >> 2;
  s->tahmin += (nib & 8) ? -fark : fark;
  if (s->tahmin > 32767) s->tahmin = 32767;
  if (s->tahmin < -32768) s->tahmin = -32768;
  s->indeks += ADPCM_INDEKS[nib & 15];
  if (s->indeks < 0) s->indeks = 0;
  if (s->indeks > 88) s->indeks = 88;
  return (int16_t)s->tahmin;
}

static inline int adpcm_kodla1(Adpcm *s, int16_t x) {
  int32_t adim = ADPCM_ADIM[s->indeks], fark = (int32_t)x - s->tahmin;
  int nib = 0;
  if (fark < 0) { nib = 8; fark = -fark; }
  if (fark >= adim) { nib |= 4; fark -= adim; }
  adim >>= 1;
  if (fark >= adim) { nib |= 2; fark -= adim; }
  adim >>= 1;
  if (fark >= adim) nib |= 1;
  adpcm_coz1(s, nib);  // kodlayıcı, çözücünün göreceği tahminle sürer
  return nib;
}

// n örneği kodlar; out (n + 1) / 2 bayt
static inline void adpcm_kodla(Adpcm *s, const int16_t *x, int n, uint8_t *out) {
  for (int i = 0; i < n; i++) {
    int nib = adpcm_kodla1(s, x[i]);
    if (i & 1) out[i >> 1] |= (uint8_t)(nib << 4);
    else out[i >> 1] = (uint8_t)nib;
  }
}

// Bayttan n örnek çözer (n çift olmalı, son parça hariç: bayt sınırında kalınır)
static inline void adpcm_coz(Adpcm *s, const uint8_t *in, int n, int16_t *out) {
  for (int i = 0; i < n; i++) out[i] = adpcm_coz1(s, (in[i >> 1] >> ((i & 1) * 4)) & 15);
}

static inline uint32_t alarm_crc32(uint32_t c, const uint8_t *p, int n) {
  c = ~c;
  while (n--) {
    c ^= *p++;
    for (int k = 0; k < 8; k++) c = (c >> 1) ^ (0xEDB88320u & (0u - (c & 1)));
  }
  return ~c;
}

static inline int alarm_ses_veri_bayt(uint32_t n) { return (int)((n + 1) / 2); }

// Başlık geçerli mi (bölüm boyutuna sığıyor mu)? CRC'yi denetlemez (veri okunmadan). Döner 1 geçerli.
static inline int alarm_ses_baslik_gecerli(const AlarmSesBaslik *b, uint32_t bolum) {
  if (b->sihir != ALARM_SES_SIHIR || b->surum != ALARM_SES_SURUM || b->sr != ALARM_SES_SR) return 0;
  if (b->n == 0 || b->n > ALARM_SES_ORNEK_MAKS) return 0;
  if ((uint32_t)ALARM_SES_BASLIK + (uint32_t)alarm_ses_veri_bayt(b->n) > bolum) return 0;
  return memchr(b->ad, 0, sizeof b->ad) != NULL;
}

// 8 kHz -> 16 kHz (doğrusal ara değer, parça parça): her örnek x için önce (önceki + x) / 2, sonra x. out 2n örnek.
static inline void alarm_ses_iki_kat(int16_t *onceki, const int16_t *in, int n, int16_t *out) {
  int16_t p = *onceki;
  for (int i = 0; i < n; i++) {
    out[2 * i] = (int16_t)(((int32_t)p + in[i]) / 2);
    out[2 * i + 1] = in[i];
    p = in[i];
  }
  *onceki = p;
}
