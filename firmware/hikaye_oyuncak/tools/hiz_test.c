// hiz.h'nin q4f çekirdeği, llm.h'nin matvec_q8_range'i ile bit bit aynı logit'i veriyor mu?
// Derle:  cc -O2 -I.. -o /tmp/hiz_test hiz_test.c -lm
// Çalıştır: /tmp/hiz_test ../../../modeller/c2ft_plan/model.bin
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LLM_INT8_ACT 1
#include "../generated/llm.h"
#include "../hiz.h"

static double simdi(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }

int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "kullanım: %s model.bin\n", argv[0]); return 2; }
  FILE *f = fopen(argv[1], "rb");
  if (!f) { perror("model.bin"); return 2; }
  fseek(f, 0, SEEK_END); long n = ftell(f); fseek(f, 0, SEEK_SET);
  uint8_t *img = malloc(n);
  if (fread(img, 1, n, f) != (size_t)n) return 2;
  fclose(f);
  Model m;
  if (llm_load(img, &m)) { fprintf(stderr, "model okunamadı\n"); return 2; }
  const QT *h = &m.out_head;
  printf("head: %d x %d, grup %d (%d grup/satır)\n", h->rows, h->cols, h->group, h->n_groups);

  Q4F q = {h->codes, NULL, h->rows, h->cols, h->group, h->n_groups, h->row_bytes, false};
  float *sc = malloc(sizeof(float) * h->rows * h->n_groups);
  for (size_t i = 0; i < (size_t)h->rows * h->n_groups; i++) sc[i] = half2float(h->scales[i]);
  q.scale = sc;

  float *x = malloc(sizeof(float) * h->cols), *y0 = malloc(sizeof(float) * h->rows),
        *y1 = malloc(sizeof(float) * h->rows);
  int8_t xq[LLM_Q8_MAX_INPUT];
  int32_t gs[256];
  srand(7);
  int fark = 0;
  double t_eski = 0, t_yeni = 0;
  for (int deneme = 0; deneme < 20; deneme++) {
    for (int i = 0; i < h->cols; i++) x[i] = ((float)rand() / RAND_MAX - 0.5f) * (1 + deneme);
    float xs;
    quantize_act(x, h->cols, xq, &xs);
    double t0 = simdi();
    matvec_q8_range(h, xq, xs, y0, 0, h->rows);
    double t1 = simdi();
    q4f_grup_toplam(xq, h->cols, h->group, gs);
    q4f_range(&q, xq, gs, xs, y1, 0, h->rows);
    double t2 = simdi();
    t_eski += t1 - t0; t_yeni += t2 - t1;
    for (int r = 0; r < h->rows; r++)
      if (memcmp(&y0[r], &y1[r], 4)) fark++;
  }
  printf("farklı logit: %d / %d\n", fark, 20 * h->rows);
  printf("bilgisayarda süre: eski %.2f ms, yeni %.2f ms (x%.1f)\n", t_eski / 20 * 1e3, t_yeni / 20 * 1e3,
         t_eski / t_yeni);
  return fark ? 1 : 0;
}
