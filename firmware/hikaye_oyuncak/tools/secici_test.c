// secici.h'yi bilgisayarda çalıştırır (tools/secici_karsilastir.py'nin C tarafı).
// Derleme: cc -O2 -o secici_test firmware/hikaye_oyuncak/tools/secici_test.c
// Girdi (stdin), aday başına: "n_fig f0 [f1] yer bitti lp guvenlik metin_bayt plan_bayt\n" + metin + plan
// (plan_bayt < 0: plan yok). Çıktı: aday başına bir satır: "puan c0 c1 ... c21" (secici_kural, SK_* sırası).
// "-a" ile yalnız kural adlarını yazar.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../secici.h"

int main(int argc, char **argv) {
  if (argc > 1 && !strcmp(argv[1], "-a")) {
    for (int i = 0; i < SK_N; i++) printf("%s%c", SECICI_KURAL_AD[i], i + 1 < SK_N ? ' ' : '\n');
    return 0;
  }
  static char metin[1 << 16], plan[1 << 14];
  int nf;
  while (scanf("%d", &nf) == 1) {
    int fig[2] = {0, 0}, yer, bitti, guv, mn, pn;
    double lp;
    for (int i = 0; i < nf && i < 2; i++)
      if (scanf("%d", &fig[i]) != 1) return 1;
    if (scanf("%d %d %lf %d %d %d", &yer, &bitti, &lp, &guv, &mn, &pn) != 6) return 1;
    getchar();  // satır sonu
    if (mn < 0 || mn >= (int)sizeof metin || pn >= (int)sizeof plan) return 2;
    if (fread(metin, 1, mn, stdin) != (size_t)mn) return 3;
    if (pn > 0 && fread(plan, 1, pn, stdin) != (size_t)pn) return 3;
    double p = secici_puanla(metin, mn, pn >= 0 ? plan : NULL, pn < 0 ? 0 : pn, fig, nf, yer, bitti, lp, guv);
    printf("%.6f", p);
    for (int i = 0; i < SK_N; i++) printf(" %g", secici_kural[i]);
    putchar('\n');
  }
  return 0;
}
