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
//   "#pin P V"   GPIO P'nin seviyesi (geliştirme düğmeleri, -DDUGME_ACIK=1: 0 basılı, 1 bırakılmış)
//   "#pin_sonra P V MS"  MS sonra (gerçek + sahte saat) GPIO P = V
//   "#bekle MS"  sahte saat MS ilerleyene kadar loop() boşta döner (düğme örneklemesi, arka plan, uyku)
//   "#bosta [N]" arka plan üretimi: kuyruğa N hikâye yazılana ya da yapılacak iş kalmayana kadar loop()
//   "#durum"     stderr'e "DURUM hazır yuva uyku bekçi silme sahip_maske uyku_durumu ayar_acik" yazar
// KART_KUYRUK=dosya: kuyruk bölümü bu dosyada kalır (yeniden çalıştırmak = kartı yeniden başlatmak).
// Ürün denemesi (stand, sesli komut, halka, ayar modu; NFC taslak okuyucu, okuma süresi SESSIZ_MS_HARF ile taklit):
//   "#etiket koy N"          standa nfc_no'su N olan (kayıtlı) etiket | "#etiket koy bos [UID]" boş NTAG213 |
//   "#etiket koy uid UID"    NTAG olmayan (yalnız UID) etiket | "#etiket dosya YOL" etiket belleği dosyadan (yoksa boş
//                            NTAG), yazmalar dosyaya geri yazılır | "#etiket kaldir" | "#etiket kilitle" |
//   "#etiket dok"            stderr'e "ETIKET uid sayfa4..7 (onaltılık)"
//   "#w OLAY"                sesli komut (uyandirma, dur, devam, baska, bir_daha, sesi_ac, sesi_kis)
//   "#sonra MS SATIR"        MS sonra (saatle) SATIR'ı uygula (okuma/üretim sürerken etiket kaldırmak, komut vermek)
//   "#http GET|POST /yol [gövde]"  ayar sayfası isteği; stderr'e "HTTP kod gövde"
//   "#halka"                 stderr'e "HALKA durum | r,g,b ..." (RMT bitlerinden çözülen son kare)
// Her halka durumu değişiminde stderr'e "HALKA_D durum". KART_SAAT=sahte ile saat yalnız taklitle ilerler.
#define SESSIZ_MS_HARF 40
#define NFC_OKUYUCU 0
static void sahte_etiket_kaydet();
#define NFC_SAHTE_YAZILDI() sahte_etiket_kaydet()
static void sahte_zamanli_satirlar();
#define SAHTE_ZAMANLI() sahte_zamanli_satirlar()
#define HALKA_DURUM_DEGISTI(metin) fprintf(stderr, "HALKA_D %s\n", (metin))
#include "sahte_arduino.h"
#include <string>
#include <vector>

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

// ---- etiket belleği dosyası ----
static std::string etiket_dosya;
static void sahte_etiket_kaydet() {
  if (etiket_dosya.empty()) return;
  FILE *f = fopen(etiket_dosya.c_str(), "wb");
  if (!f) return;
  fputc(nfc_sahte.uid_n, f);
  fwrite(nfc_sahte.uid, 1, 7, f);
  fwrite(nfc_sahte.bellek, 1, sizeof nfc_sahte.bellek, f);
  fclose(f);
}
static int onaltilik_(const char *p, uint8_t *u, int kap) { return onaltilik(p, u, kap); }

static bool harness_satir(const char *satir);
static struct Zamanli { int64_t us; std::string satir; } zamanli[32];
static int zamanli_n = 0;
static bool zamanli_isleniyor = false;
static void sahte_zamanli_satirlar() {
  if (zamanli_isleniyor) return;
  zamanli_isleniyor = true;
  for (;;) {
    int en = -1;
    int64_t simdi = esp_timer_get_time();
    for (int i = 0; i < zamanli_n; i++)
      if (zamanli[i].us <= simdi && (en < 0 || zamanli[i].us < zamanli[en].us)) en = i;
    if (en < 0) break;
    std::string s = zamanli[en].satir;
    for (int i = en + 1; i < zamanli_n; i++) zamanli[i - 1] = zamanli[i];
    zamanli_n--;
    fprintf(stderr, "ZAMANLI %s\n", s.c_str());
    harness_satir(s.c_str());
  }
  zamanli_isleniyor = false;
}

static bool harness_satir(const char *satir) {
  if (!strncmp(satir, "#etiket ", 8)) {
    const char *p = satir + 8;
    uint8_t u[10];
    if (!strncmp(p, "koy uid ", 8)) nfc_sahte_koy_bos(u, onaltilik_(p + 8, u, 7), false);
    else if (!strncmp(p, "koy bos", 7)) {
      static const uint8_t V[7] = {0x04, 0xB0, 0x5E, 0x11, 0x22, 0x33, 0x80};
      int n = onaltilik_(p + 7, u, 7);
      nfc_sahte_koy_bos(n == 7 ? u : V, 7, true);
    } else if (!strncmp(p, "koy ", 4)) nfc_sahte_koy_no(atoi(p + 4));
    else if (!strncmp(p, "dosya ", 6)) {
      etiket_dosya = p + 6;
      while (!etiket_dosya.empty() && (etiket_dosya.back() == '\n' || etiket_dosya.back() == ' ')) etiket_dosya.pop_back();
      FILE *f = fopen(etiket_dosya.c_str(), "rb");
      if (f) {
        uint8_t n = (uint8_t)fgetc(f), uid[7];
        size_t r = fread(uid, 1, 7, f);
        nfc_sahte_koy_bos(uid, n, true);
        r += fread(nfc_sahte.bellek, 1, sizeof nfc_sahte.bellek, f);
        (void)r;
        fclose(f);
      } else {
        static const uint8_t V[7] = {0x04, 0xD0, 0x55, 0x66, 0x77, 0x88, 0x81};
        nfc_sahte_koy_bos(V, 7, true);
        sahte_etiket_kaydet();
      }
    } else if (!strncmp(p, "kaldir", 6)) nfc_sahte_kaldir();
    else if (!strncmp(p, "kilitle", 7)) nfc_sahte.kilitli = true;
    else if (!strncmp(p, "dok", 3)) {
      fprintf(stderr, "ETIKET %d ", nfc_sahte.alanda);
      for (int i = 0; i < nfc_sahte.uid_n; i++) fprintf(stderr, "%02X", nfc_sahte.uid[i]);
      fprintf(stderr, " ");
      for (int i = 16; i < 32; i++) fprintf(stderr, "%02X", nfc_sahte.bellek[i]);
      fprintf(stderr, "\n");
    }
    return true;
  }
  if (!strncmp(satir, "#w ", 3)) {
    char ad[32] = "";
    sscanf(satir + 3, "%31s", ad);
    int e = kws_olay_bul(ad);
    if (e > 0) halka_ekle(&ana_halka, OLAY_SESLI, e);
    else fprintf(stderr, "bilinmeyen sesli olay: %s\n", ad);
    return true;
  }
  if (!strncmp(satir, "#sonra ", 7)) {
    char *son;
    long ms = strtol(satir + 7, &son, 10);
    while (*son == ' ') son++;
    std::string s = son;
    while (!s.empty() && s.back() == '\n') s.pop_back();
    if (zamanli_n < 32) zamanli[zamanli_n++] = {esp_timer_get_time() + (int64_t)ms * 1000, s};
    return true;
  }
  if (!strncmp(satir, "#http ", 6)) {
    char yontem[8] = "", yol[128] = "";
    int k = 0;
    sscanf(satir + 6, "%7s %127s %n", yontem, yol, &k);
    std::string govde = k ? satir + 6 + k : "";
    while (!govde.empty() && govde.back() == '\n') govde.pop_back();
    int kod = web.sahte_istek(yontem, yol, govde.c_str());
    std::string y = web.yanit_tur.find("html") != std::string::npos ? "<html " + std::to_string(web.yanit.size()) + " B>"
                                                                     : web.yanit;
    fprintf(stderr, "HTTP %d %s%s%s\n", kod, y.c_str(), web.konum.empty() ? "" : " -> ", web.konum.c_str());
    return true;
  }
  if (!strncmp(satir, "#halka", 6)) {
    halka_tik_(millis());
    fprintf(stderr, "HALKA %s | %d mA | rmt %ld kare, %d hata |", halka_son_durum, halka.akim_ma, sahte_rmt_kare,
            sahte_rmt_hata);
    for (int i = 0; i < sahte_rmt_n; i++)
      fprintf(stderr, " %d,%d,%d", sahte_rmt_rgb[i][0], sahte_rmt_rgb[i][1], sahte_rmt_rgb[i][2]);
    fprintf(stderr, "\n");
    return true;
  }
  return false;
}

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
      fprintf(stderr, "DURUM %d %d %d %ld %ld %u %d %d\n", kuyruk_var ? kuyruk_say(&kq, -1, -1) : -1, kq.n_yuva,
              sahte_uyku_n, sahte_bekci_besle, sahte_flash_sil_n, (unsigned)sahip_maske, uyku.durum, (int)ayr.acik);
      continue;
    }
    if (harness_satir(satir)) continue;
    Serial.girdi += satir;
    while (Serial.available()) loop();
  }
  return 0;
}
