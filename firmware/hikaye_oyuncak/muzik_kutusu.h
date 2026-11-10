// Müzik kutusu: ninni modunda konuşmanın altında çok kısık çalan, kartta sentezlenen melodi (dosya gerekmez).
//
// Her nota bir müzik kutusu dişi gibi: temel sinüs + 2. ve 3. harmonik, sert başlangıç, üstel sönüm. Melodi
// "Dandini dandini dastana" havasında, geleneksel (anonim) bir ninni ezgisi; döngü halinde çalar. Sentez tamsayı
// fazla (sinüs tablosu) yapılır: bilgisayarda ve kartta aynı örnekler (tools/urun_test.c). mk_karistir() verilen
// PCM'e ekler (doyumlu); seviye 0..256 (256 = MK_TEPE).
#pragma once
#include <math.h>
#include <stdint.h>
#include <string.h>

#define MK_SR 16000
#define MK_TEPE 900            // tam seviyede tepe genlik (int16; konuşma tepesi ~20000: ≈ -27 dB)
#define MK_SONUM_MS 700        // genlik bu sürede 1/e'ye iner

// Nota: MIDI numarası (0: sus) ve süresi (sekizlik birim)
typedef struct { uint8_t nota, sure; } MkNota;
static const MkNota MK_EZGI[] = {
    {72, 2}, {74, 2}, {76, 4}, {76, 2}, {74, 2}, {72, 4}, {74, 2}, {76, 2}, {77, 2}, {76, 2}, {74, 8},
    {72, 2}, {74, 2}, {76, 4}, {79, 2}, {77, 2}, {76, 4}, {74, 2}, {72, 2}, {74, 2}, {71, 2}, {72, 8}, {0, 8},
};
#define MK_SEKIZLIK_MS 300

typedef struct {
  int nota, kalan;          // çalan nota, notanın kalan örneği
  uint32_t faz, adim;       // Q32 faz
  int32_t zarf;             // Q15 genlik zarfı
  int32_t sonum;            // Q15 örnek başına çarpan
  int16_t sin_t[256];
} MuzikKutusu;

static inline void mk_kur(MuzikKutusu *m) {
  memset(m, 0, sizeof *m);
  for (int i = 0; i < 256; i++) m->sin_t[i] = (int16_t)lrint(32767.0 * sin(6.283185307179586 * i / 256));
  m->sonum = (int32_t)lrint(32768.0 * exp(-1000.0 / (MK_SONUM_MS * (double)MK_SR)));
  m->nota = -1;
}

static inline void mk_nota_bas(MuzikKutusu *m) {
  m->nota = (m->nota + 1) % (int)(sizeof MK_EZGI / sizeof MK_EZGI[0]);
  const MkNota *n = &MK_EZGI[m->nota];
  m->kalan = MK_SR * MK_SEKIZLIK_MS / 1000 * n->sure;
  if (n->nota) {
    double hz = 440.0 * pow(2.0, (n->nota - 69) / 12.0);
    m->adim = (uint32_t)(hz / MK_SR * 4294967296.0);
    m->faz = 0;
    m->zarf = 32767;
  }
}

static inline int16_t mk_ornek(MuzikKutusu *m) {
  if (m->kalan <= 0) mk_nota_bas(m);
  m->kalan--;
  m->faz += m->adim;
  int32_t s = m->sin_t[m->faz >> 24] + (m->sin_t[(uint8_t)((m->faz >> 24) * 2)] >> 2) +
              (m->sin_t[(uint8_t)((m->faz >> 24) * 3)] >> 3);  // 1 + 1/4 + 1/8
  int32_t v = (int32_t)(((int64_t)s * m->zarf) >> 15);
  m->zarf = (int32_t)(((int64_t)m->zarf * m->sonum) >> 15);
  return (int16_t)(v * MK_TEPE / 45000);  // 1.375 x 32767 ≈ 45000 -> tepe MK_TEPE
}

// pcm'e müziği ekler; seviye 0..256
static inline void mk_karistir(MuzikKutusu *m, int16_t *pcm, int n, int seviye) {
  for (int i = 0; i < n; i++) {
    int32_t v = pcm[i] + mk_ornek(m) * seviye / 256;
    pcm[i] = (int16_t)(v > 32767 ? 32767 : v < -32768 ? -32768 : v);
  }
}
