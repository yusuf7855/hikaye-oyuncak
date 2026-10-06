// hikaye_oyuncak.ino'yu bilgisayarda sahte ESP32 başlıklarıyla (sahte/) derleyip çalıştırır: kartın üretim yolu
// (istem, isim süzgeci, plan modu, örnekleme, seçici) aynen koşar; tek fark çift çekirdek yerine tek çekirdek (aynı
// sayılar) ve rastgeleliğin gen'deki gibi rand() olması.
// Derleme (tools/kart_pc_karsilastir.py yapar):
//   g++ -O2 -Itools/kart_pc/sahte -o kart_pc tools/kart_pc/kart_pc.cpp
// Çalıştırma: KART_MODEL=hf_c3ft_karma/model.bin KART_BOLUMLER=partitions.csv ./kart_pc < komutlar
//   stdin satırları seri monitöre yazılmış gibi loop()'a gider; "#tohum N" satırı sonraki hikâyenin aday j'sini
//   srand(N + j) ile başlatır (urun_uret: seed + j). Her aday stderr'e:
//   "ADAY j n n_plan bitti plan_bozuk lp puan tok1 tok2 ..." (aday_tok: plan + gövde, gövdedeki EOT hariç).
#include "sahte_arduino.h"

static int kart_tohum = 0;
#define ORNEKLE_RASTGELE() ((double)rand() / RAND_MAX)
#define ADAY_BASI(j) srand(kart_tohum + (j))
#define ADAY_SONU(j, a, p)                                                                                   \
  do {                                                                                                       \
    fprintf(stderr, "ADAY %d %d %d %d %d %.17g %.17g", (j), (a).n, (a).n_plan, (int)(a).bitti,                \
            (int)(a).plan_bozuk, (a).lp, (p));                                                               \
    for (int i_ = 0; i_ < (a).n; i_++) fprintf(stderr, " %d", aday_tok[i_]);                                  \
    fputc('\n', stderr);                                                                                     \
  } while (0)
#include "../../hikaye_oyuncak.ino"

int main() {
  setvbuf(stdout, NULL, _IOLBF, 0);
  setup();
  fprintf(stderr, "PSRAM %zu / %zu B, SRAM %zu B\n", sahte_psram_dolu, sahte_psram_sinir, sahte_sram_dolu);
  char satir[1024];
  while (fgets(satir, sizeof satir, stdin)) {
    if (!strncmp(satir, "#tohum ", 7)) { kart_tohum = atoi(satir + 7); continue; }
    Serial.girdi += satir;
    while (Serial.available()) loop();
  }
  return 0;
}
