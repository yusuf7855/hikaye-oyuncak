// hikaye_oyuncak.ino'yu bilgisayarda sahte ESP32 başlıklarıyla (sahte/) derleyip çalıştırır: kartın üretim yolu
// (istem, isim süzgeci, plan modu, örnekleme, seçici) aynen koşar; tek fark çift çekirdek yerine tek çekirdek (aynı
// sayılar) ve rastgeleliğin gen'deki gibi rand() olması.
// Derleme (tools/kart_pc_karsilastir.py yapar):
//   g++ -O2 -Itools/kart_pc/sahte -o kart_pc tools/kart_pc/kart_pc.cpp
// Çalıştırma: KART_MODEL=hf_c3ft_karma/model.bin KART_BOLUMLER=partitions.csv ./kart_pc < komutlar
//   stdin satırları seri monitöre yazılmış gibi loop()'a gider; "#tohum N" satırı sonraki hikâyenin aday j'sini
//   srand(N + j) ile başlatır (urun_uret: seed + j). Her aday stderr'e:
//   "ADAY j n n_plan bitti plan_bozuk lp puan tok1 tok2 ..." (aday_tok: plan + gövde, gövdedeki EOT hariç).
//   Kuyruğa yazılan hikâye: "KUYRUK yuva f j K puan n n_plan tok ..."; hazır hikâye çalınınca: "CALINDI f j n tok ...".
// Ürün denemesi için ek satırlar (stdin):
//   "#pin P V"   GPIO P'nin seviyesi (düğme: 0 basılı, 1 bırakılmış)
//   "#pin_sonra P V MS"  MS sonra (gerçek + sahte saat) GPIO P = V: üretim ya da konuşma sürerken düğmeye basmak için
//   "#bekle MS"  sahte saat MS ilerleyene kadar loop() boşta döner (düğme örneklemesi, arka plan, uyku)
//   "#bosta [N]" arka plan üretimi: kuyruğa N hikâye yazılana ya da yapılacak iş kalmayana kadar loop()
//   "#durum"     stderr'e "DURUM hazır yuva uyku bekçi silme" yazar
// KART_KUYRUK=dosya: kuyruk bölümü bu dosyada kalır (yeniden çalıştırmak = kartı yeniden başlatmak).
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
#define KUYRUK_YAZILDI(y, f, j, K, puan, tok, n, n_plan)                                                    \
  do {                                                                                                       \
    fprintf(stderr, "KUYRUK %d %d %d %d %.17g %d %d", (y), (f), (j), (K), (double)(puan), (n), (n_plan));     \
    for (int i_ = 0; i_ < (n); i_++) fprintf(stderr, " %d", (tok)[i_]);                                       \
    fputc('\n', stderr);                                                                                     \
  } while (0)
#define HAZIR_CALINDI(f, j, tok, n)                                                                          \
  do {                                                                                                       \
    fprintf(stderr, "CALINDI %d %d %d", (f), (j), (n));                                                     \
    for (int i_ = 0; i_ < (n); i_++) fprintf(stderr, " %d", (tok)[i_]);                                       \
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
    if (!strncmp(satir, "#pin ", 5)) {
      int p = 0, v = 1;
      sscanf(satir + 5, "%d %d", &p, &v);
      digitalWrite(p, v);
      continue;
    }
    if (!strncmp(satir, "#pin_sonra ", 11)) {
      int p = 0, v = 1, ms = 0;
      sscanf(satir + 11, "%d %d %d", &p, &v, &ms);
      if (sahte_zamanli_n < 16) sahte_zamanli[sahte_zamanli_n++] = {p, v, esp_timer_get_time() + (int64_t)ms * 1000};
      continue;
    }
    if (!strncmp(satir, "#bekle ", 7)) {
      int64_t son = esp_timer_get_time() + (int64_t)atol(satir + 7) * 1000;
      while (esp_timer_get_time() < son) loop();
      continue;
    }
    if (!strncmp(satir, "#bosta", 6)) {
      int n = atoi(satir + 6), bas = arka_yazilan;
      for (long i = 0; i < 10000000 && arka_is_var() && (n <= 0 || arka_yazilan - bas < n); i++) loop();
      fprintf(stderr, "BOSTA %d\n", arka_yazilan - bas);
      continue;
    }
    if (!strncmp(satir, "#durum", 6)) {
      fprintf(stderr, "DURUM %d %d %d %ld %ld\n", kuyruk_var ? kuyruk_say(&kq, -1, -1) : -1, kq.n_yuva, sahte_uyku_n,
              sahte_bekci_besle, sahte_flash_sil_n);
      continue;
    }
    Serial.girdi += satir;
    while (Serial.available()) loop();
  }
  return 0;
}
