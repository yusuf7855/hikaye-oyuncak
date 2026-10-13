// kws.h'nin çıkarımı PyTorch int8 başvurusuyla (ses/kws/ortak.py) aynı mı? tools/kws_test.py sürer.
// Derle:    cc -O2 -I.. [-DKWS_MODEL_BASLIK='"/yol/kws_model.h"'] -o /tmp/kws_test kws_test.c -lm
// Çalıştır: /tmp/kws_test ses.pcm oznitelik.i8 cikti_dizini [tohum]
//   ses.pcm      : 16 kHz int16 ham ses; rastgele boylu parçalarla kws_isle'ye verilir (akış sınırlarını zorlar)
//   oznitelik.i8 : PC'nin (numpy) int8 öznitelikleri; ağ yalnız bunlarla da çalıştırılır (bit bit eşitlik)
// Yazar: <dizin>/c_oznitelik.i8, c_logit.i32 (uçtan uca), c_ag_logit.i32 (yalnız ağ), c_olay.txt (kare olay),
//        c_olay_parca.txt (büyük/küçük rastgele parçalarla olay sırası)
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "../kws.h"

static double simdi(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }

static void *oku(const char *yol, size_t *n) {
  FILE *f = fopen(yol, "rb");
  if (!f) { perror(yol); exit(2); }
  fseek(f, 0, SEEK_END); *n = (size_t)ftell(f); fseek(f, 0, SEEK_SET);
  void *b = malloc(*n + 1);
  if (fread(b, 1, *n, f) != *n) { perror(yol); exit(2); }
  fclose(f);
  return b;
}

static FILE *ac(const char *dizin, const char *ad) {
  char yol[1024];
  snprintf(yol, sizeof yol, "%s/%s", dizin, ad);
  FILE *f = fopen(yol, "wb");
  if (!f) { perror(yol); exit(2); }
  return f;
}

int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "kullanım: %s ses.pcm oznitelik.i8 dizin [tohum]\n", argv[0]); return 2; }
  size_t nb, nq;
  int16_t *pcm = (int16_t *)oku(argv[1], &nb);
  int8_t *qpc = (int8_t *)oku(argv[2], &nq);
  long n = (long)(nb / 2);
  unsigned tohum = argc > 4 ? (unsigned)atoi(argv[4]) : 1u;
  srand(tohum);
  if (!kws_kur()) { fprintf(stderr, "kws_kur başarısız\n"); return 1; }

  // 1) uçtan uca, kare kare: örnekler rastgele boylu ama kare sınırını aşmayan parçalarla verilir; her karenin logiti
  //    ve olayı (kare numarasıyla) yazılır
  FILE *fq = ac(argv[3], "c_oznitelik.i8"), *fl = ac(argv[3], "c_logit.i32"), *fo = ac(argv[3], "c_olay.txt");
  long kare = 0, olay_n = 0;
  double t0 = simdi();
  for (long i = 0; i < n;) {
    int al = (rand() % 5 == 0) ? 1 + rand() % 7 : 1 + rand() % 400;
    int gerek = KWS_PENCERE - kws_d.dolu;
    if (al > gerek) al = gerek;
    if (al > n - i) al = (int)(n - i);
    long once = kws_d.kare;
    int olay = kws_isle(pcm + i, al);
    i += al;
    if (kws_d.kare != once) { fwrite(kws_d.logit, 4, KWS_NSINIF, fl); kare++; }
    while (olay != KWS_YOK) {
      fprintf(fo, "%ld %d\n", kws_d.kare - 1, olay);
      olay_n++;
      olay = kws_isle(NULL, 0);
    }
  }
  double t1 = simdi();
  fclose(fl); fclose(fo);

  // 1b) aynı ses, sınırsız rastgele parçalar (1..4000 örnek): olay sırası aynı olmalı (kare numarası yazılmaz)
  kws_sifirla();
  FILE *fs = ac(argv[3], "c_olay_parca.txt");
  for (long i = 0; i < n;) {
    int al = (rand() % 3 == 0) ? 1 + rand() % 50 : 1 + rand() % 4000;
    if (al > n - i) al = (int)(n - i);
    int olay = kws_isle(pcm + i, al);
    i += al;
    while (olay != KWS_YOK) { fprintf(fs, "%d\n", olay); olay = kws_isle(NULL, 0); }
  }
  fclose(fs);

  // 2) öznitelikler ayrıca (aynı akış tanımıyla, toplu)
  kws_sifirla();
  for (long f = 0; (long)f * KWS_ADIM + KWS_PENCERE <= n; f++) {
    int8_t q[KWS_NMEL];
    memcpy(kws_d.pcm, pcm + (long)f * KWS_ADIM, KWS_PENCERE * sizeof(int16_t));
    kws_oznitelik(q);
    fwrite(q, 1, KWS_NMEL, fq);
  }
  fclose(fq);

  // 3) yalnız ağ: PC özniteliğiyle (bit bit karşılaştırma için)
  kws_sifirla();
  FILE *fa = ac(argv[3], "c_ag_logit.i32");
  long nk = (long)(nq / KWS_NMEL);
  double t2 = simdi();
  for (long f = 0; f < nk; f++) {
    kws_ag_adim(qpc + f * KWS_NMEL);
    fwrite(kws_d.logit, 4, KWS_NSINIF, fa);
  }
  double t3 = simdi();
  fclose(fa);
  printf("kare %ld, olay %ld, uçtan uca %.1f kare/s (gerçek zaman x%.0f), yalnız ağ %.1f kare/s\n", kare, olay_n,
         kare / (t1 - t0), kare / (t1 - t0) / 50.0, nk / (t3 - t2));
  return 0;
}
