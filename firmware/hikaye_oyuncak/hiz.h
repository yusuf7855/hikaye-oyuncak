// Hız: 4-bit head için hızlı çekirdek ve head'in PSRAM'e taşınması.
//
// Kartta ölçülen hız 1,6 token/s idi. Çekirdek katmanlar int8 ve iki çekirdekte çalışıyor, ama head
// (16 384 satır x 160) 4-bit olduğu için matvec_par onu tek çekirdekte, eleman başına nibble ayıklayan ve
// grup başına half2float çağıran yavaş yoldan (matvec_q8_range) geçiriyordu. Head bir token'daki en büyük
// matris (2,6 M çarpma; çekirdeğin tamamı ~3 M).
//
// Burada:
//  1) q4f: aynı aritmetik, daha az iş. Bayt başına iki nibble birlikte açılır; "-8" her eleman yerine grup
//     başına bir kez düşülür: sum((c-8)*x) = sum(c*x) - 8*sum(x). Grup toplamları tamsayıda birebir aynı,
//     float birikim sırası da aynı: logit'ler matvec_q8_range ile bit bit eşit (tools/hiz_test.c doğrular).
//  2) Grup ölçekleri bir kez float'a çevrilir (head için 16 384 x 5 x 4 B = 320 KB PSRAM).
//  3) Kodlar (1,3 MB) yer varsa flash'tan PSRAM'e kopyalanır; flash önbelleği yerine PSRAM'den okunur.
//  4) matvec_par head'i de iki çekirdeğe böler.
#pragma once
#include <stdint.h>
#include <string.h>

typedef struct {
  const uint8_t *codes;   // rows * row_bytes (flash ya da PSRAM)
  const float *scale;     // rows * n_groups
  int rows, cols, group, n_groups, row_bytes;
  bool psram;             // kodlar PSRAM'de mi
} Q4F;

// Aktivasyonun grup toplamları (x_q int8): her matvec başında bir kez.
static inline void q4f_grup_toplam(const int8_t *xq, int cols, int group, int32_t *gs) {
  int ng = (cols + group - 1) / group;
  for (int gi = 0; gi < ng; gi++) {
    int b = gi * group, e = b + group;
    if (e > cols) e = cols;
    int32_t s = 0;
    for (int j = b; j < e; j++) s += xq[j];
    gs[gi] = s;
  }
}

#if defined(__GNUC__)
__attribute__((noinline))
#endif
static void q4f_range(const Q4F *t, const int8_t *xq, const int32_t *gs, float x_scale, float *y, int r0,
                      int r1) {
  const int g = t->group, ng = t->n_groups, cols = t->cols, rb = t->row_bytes;
  for (int r = r0; r < r1; r++) {
    const uint8_t *row = t->codes + (size_t)r * rb;
    const float *sc = t->scale + (size_t)r * ng;
    float acc = 0.f;
    for (int gi = 0; gi < ng; gi++) {
      int b = gi * g, e = b + g;
      if (e > cols) e = cols;
      int32_t s = 0;
      int j = b;
      if (!(b & 1)) {  // grup çift sütunda başlar (C2/C3: 160, 192 ve grup 32/64): bayt bayt
        const uint8_t *p = row + (b >> 1);
        for (; j + 1 < e; j += 2, p++) {
          uint8_t v = *p;
          s += (int32_t)(v & 0xF) * xq[j] + (int32_t)(v >> 4) * xq[j + 1];
        }
      }
      for (; j < e; j++) {  // tek sütun artığı (genel durum)
        uint8_t v = row[j >> 1];
        s += (int32_t)((j & 1) ? (v >> 4) : (v & 0xF)) * xq[j];
      }
      s -= 8 * gs[gi];
      acc += (float)s * sc[gi];
    }
    y[r] = acc * x_scale;
  }
}
