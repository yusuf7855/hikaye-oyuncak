// Hikâye Oyuncağı (ESP32-S3 N16R8): ürün yazılımı + seri monitör test komutları.
//
// Model: c3ft_karma (C3: d192 L12 F512 P56, V16384; model.bin 10 331 252 B), flash'taki "model" bölümünde
// (0x110000). Figürler data/urun_kartlari.json'daki 11 ürün figürü ve kart yerleri; üretim bilgisayardaki
// degerlendirme/urun_uret.py ile aynı (runtime/ornekle.h + runtime/isim_suzgec.h, generated/ altına kopya):
// istem <|endoftext|> + "Karakter: F | Yer: Y\nSorun:" (Yan alanı yok), plan modu, sıcaklık 0.5, top-k 40, tekrar
// cezası 1.1, istem tekrar penceresine girmez (gen -P), gövdede satır sonu yasağı (gen -N), isim süzgeci (gen -Y:
// başka figürlerin ve yanlarının adları üretilemez), en çok 230 token. Seçici secici.h = urun_uret.puanla.
//
// Bellek (PSRAM): KV önbelleği float, bağlam 224 (C3: 12 x 224 x 192 x 4 B x 2 = 4.13 MB) + logits. Çekirdek
// katmanlar sığarsa int8 (C2), sığmazsa dosyadaki gibi 4-bit (C3: 2.85 MB kod + 0.23 MB float ölçek) PSRAM'e
// kopyalanır; head (bağlı gömme) 4-bit flash'ta kalır (yer varsa PSRAM'e kopyalanır). Hepsi aynı int8 aktivasyon
// aritmetiği (llm.h matvec_q8 ile bit bit aynı; hiz.h).
//
// Seri monitör (115200): "3 1" = 3. figür, kendi 1. yeri | "r" = rastgele | "?" = liste |
// "b" = hız testi (head'in üç yolu, token başına ms dökümü).
// Sona aday sayısı: "3 1 4" = 4 aday üret, seçiciyle en iyisini yaz. Aday sayısı yoksa (1) canlı yazar.
// Ürün önerisi: kuyruğa önceden hazırlanan hikâyede K=16, canlı beklenen hikâyede K=4-8.
// Kart her hikâyeden sonra token/s ve süreyi yazar.
//
// Ses (ses.h): flash'taki "ses" bölümünde ses.bin varsa hikâye kartta seslendirilir; MAX98357A'ya I2S (BCLK 4,
// LRC 5, DIN 6; 16 kHz, 16 bit, mono -> iki kanala aynı örnek). Konuşurken kart üstündeki RGB LED yeşil.
// "s <metin>" = metni oku | "o" = üretilen hikâyeyi otomatik okuma aç/kapa (ses modeli varsa açık başlar).
// Bölüm ya da ses.bin yoksa her şey eskisi gibi çalışır, konuşma kapalıdır (düğmelere bip ile yanıt verilir).
//
// Ürün (README "6. Oyuncak olarak"): pinler ve sabitler donanim.h'de.
// - Hikâye kuyruğu (kuyruk.h, flash'ta "kuyruk" bölümü): oyuncak boştayken her figür x yer için K=16 aday üretip
//   seçiciyle en iyisini saklar (figür başına KUYRUK_FIGUR_BASI). Çocuk hikâye isteyince hazır olan hemen okunur,
//   tüketilir, yerine boşta yenisi üretilir. Hazır yoksa canlı (K=1). Açılıştan açılışa kalır.
// - Düğmeler (dugmeler.h): FİGÜR / YER / OYNAT, uzun basışlar, OYNAT + FİGÜR/YER ses aç/kıs; RGB LED durumu.
//   NFC figür okuyucu arayüzü nfc.h (NFC_OKUYUCU; varsayılan taslak, "n <uid>" ile denenir).
// - Güç: boşta ve üretecek iş yokken hafif uyku (düğme uyandırır); yazılımla ses seviyesi. Görev bekçisi
//   (task watchdog) uzun üretimde her token'da beslenir.
// Seri komutlar (yenileri): "8" = Elsa, sürpriz yer | "8 4" = hazır varsa hemen, yoksa canlı | "8 4 K" = her zaman
// K adayla üret (test) | "k" kuyruk durumu, "k+"/"k-" arka plan üretimi aç/kapa, "k sil" | "v+"/"v-"/"v N" ses |
// "t f|F|y|Y|o|O|+|-|a" düğme taklidi | "n 04A1B2C3" NFC etiketi taklidi | "u" 10 s hafif uyku denemesi.

#include "esp_partition.h"
#include "esp_heap_caps.h"
#include "esp_timer.h"
#include "esp_random.h"
#include "esp_task_wdt.h"
#include "esp_sleep.h"
#include "esp_system.h"
#include "driver/gpio.h"
#if !ARDUINO_USB_CDC_ON_BOOT
#include "driver/uart.h"
#endif
#include <Preferences.h>
#include "donanim.h"
#include "kuyruk.h"
#include "dugmeler.h"
#include "nfc.h"

#define LLM_INT8_ACT 1
#define LLM_PROFILE 1
#define LLM_PROFILE_NOW() esp_timer_get_time()
#include "generated/llm.h"
#include "hiz.h"
#ifndef ORNEKLE_RASTGELE  // bilgisayardaki denemede (tools/kart_pc) gen'in rand()'ı verilir
#define ORNEKLE_RASTGELE() ((double)esp_random() / 4294967295.0)
#endif
#include "generated/ornekle.h"
#include "generated/isim_suzgec.h"
#include "generated/vocab.h"
#include "generated/istemler.h"
#include "secici.h"
#include <ESP_I2S.h>
#include <freertos/stream_buffer.h>
#include "ses.h"

static const int BAGLAM = 224;       // KV önbelleği konumu (istem ~15 + plan + gövde; en uzun gözlenen ~191)
static const int N_URET = 230;       // en fazla bu kadar token (plan + gövde; urun_uret.aday_uret n=230)
static const float SICAKLIK = 0.5f, TEKRAR = 1.1f;
static const int TOP_K = 40;
static const size_t SES_PAY = 640 * 1024;  // ses.h'nin PSRAM'i (~450 KB) + çalma tamponu, int8 çekirdek kararında

// Bilgisayardaki deneme (tools/kart_pc) için kancalar: aday başında (tohum) ve puanlandıktan sonra (döküm).
#ifndef ADAY_BASI
#define ADAY_BASI(j)
#endif
#ifndef ADAY_SONU
#define ADAY_SONU(j, a, puan)
#endif
#ifndef KUYRUK_YAZILDI  // arka plan hikâyesi kuyruğa yazıldı (yuva y; -1 yazılamadı)
#define KUYRUK_YAZILDI(y, f, j, K, puan, tok, n, n_plan)
#endif
#ifndef HAZIR_CALINDI   // hazır (ya da yarım iş) hikâye çalındı
#define HAZIR_CALINDI(f, j, tok, n)
#endif

// Arduino fonksiyon prototiplerini dosyanın başına ekler; Aday onlardan önce tanımlı olmalı.
struct Aday { int n, n_plan; double lp; bool bitti, plan_bozuk, iptal; };

Model model;
Scratch s;
static bool ses_var = false, ses_oku = false;   // ses modeli yüklü mü, hikâye okunsun mu
static size_t psram_used = 0;
static uint32_t model_fp = 0;                   // model.bin parmak izi (kuyruk imzası)

// Görev bekçisi (task watchdog): ana döngü (loopTask) BEKCI_SN saniye beslenmezse kart yeniden başlar. Uzun üretim
// (K=16 aday ~15 dk) her token'da, konuşma her ses parçasında besler.
static bool bekci_var = false;
static void bekci_kur() {
  esp_task_wdt_config_t c;
  memset(&c, 0, sizeof c);
  c.timeout_ms = BEKCI_SN * 1000;
  c.idle_core_mask = 1 << 0;  // Arduino varsayılanı: 0. çekirdeğin boşta görevi de izlenir
  c.trigger_panic = true;
  if (esp_task_wdt_reconfigure(&c) != ESP_OK && esp_task_wdt_init(&c) != ESP_OK) {
    Serial.println("UYARI: görev bekçisi kurulamadı");
    return;
  }
  esp_err_t e = esp_task_wdt_add(NULL);
  bekci_var = e == ESP_OK || e == ESP_ERR_INVALID_ARG;  // INVALID_ARG: zaten ekli
}
static void bekci_besle() { if (bekci_var) esp_task_wdt_reset(); }

static void *ps(size_t n) {
  void *p = heap_caps_malloc(n, MALLOC_CAP_SPIRAM);
  if (p) psram_used += n;
  return p;
}
static void *ps_or_die(size_t n, const char *what) {
  void *p = ps(n);
  if (!p) { Serial.printf("HATA: PSRAM ayrılamadı: %s (%u B)\n", what, (unsigned)n); while (1) delay(1000); }
  return p;
}
static void *sram_or_die(size_t n, const char *what) {
  void *p = heap_caps_malloc(n, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
  if (!p) { Serial.printf("HATA: SRAM ayrılamadı: %s (%u B)\n", what, (unsigned)n); while (1) delay(1000); }
  return p;
}

// ---- iki çekirdekli matvec: çekirdek katmanlar int8 ya da 4-bit (hiz.h q4f), head 4-bit (q4f) ----
static TaskHandle_t worker_h, main_h;
static SesIs job_fn = NULL;        // ses.h işi (NULL değilse)
static void *job_arg;
static const QT *job_t;
static const Q4F *job_q;           // NULL: int8 işi
static const int8_t *job_xq;
static const int32_t *job_gs;
static float job_xs;
static float *job_y;
static int job_split;
static void worker_main(void *) {
  for (;;) {
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    if (job_fn) job_fn(job_arg, 0, job_split, 1);
    else if (job_q) q4f_range(job_q, job_xq, job_gs, job_xs, job_y, 0, job_split);
    else matvec_i8_range(job_t, job_xq, job_xs, job_y, 0, job_split);
    xTaskNotifyGive(main_h);
  }
}
static bool iki_cekirdek = false;
// Çekirdek tensör: w8 != NULL int8 (PSRAM) | scale8 != NULL ve w8 == NULL: 4-bit kodlar PSRAM'de, ölçekler float
// (q4f) | ikisi de NULL: flash'ta 4-bit (MATVEC). Üç yol da matvec_q8 ile bit bit aynı sonucu verir.
static void matvec_par(const QT *t, const float *x, float *y) {
  static int8_t xq[LLM_Q8_MAX_INPUT];
  static int32_t gs[64];
  static Q4F q;
  float xs;
  if (t->w8 == NULL && (t->scale8 == NULL || t->n_groups > 64)) { MATVEC(t, x, y); return; }
  quantize_act(x, t->cols, xq, &xs);
  if (t->w8 == NULL) {
    q = {t->codes, t->scale8, t->rows, t->cols, t->group, t->n_groups, t->row_bytes, true};
    q4f_grup_toplam(xq, t->cols, t->group, gs);
    if (!iki_cekirdek || t->rows < 128) { q4f_range(&q, xq, gs, xs, y, 0, t->rows); return; }
    job_fn = NULL; job_q = &q; job_xq = xq; job_gs = gs; job_xs = xs; job_y = y; job_split = t->rows / 2;
    xTaskNotifyGive(worker_h);
    q4f_range(&q, xq, gs, xs, y, job_split, t->rows);
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    return;
  }
  if (!iki_cekirdek || t->rows < 128) { matvec_i8_range(t, xq, xs, y, 0, t->rows); return; }
  job_fn = NULL; job_q = NULL; job_t = t; job_xq = xq; job_xs = xs; job_y = y; job_split = t->rows / 2;
  xTaskNotifyGive(worker_h);
  matvec_i8_range(t, xq, xs, y, job_split, t->rows);
  ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
}

// Head: 0 = eski yol (tek çekirdek, matvec_q8_range, flash) | 1 = q4f iki çekirdek, kodlar flash'ta |
// 2 = q4f iki çekirdek, kodlar PSRAM'de. Açılışta en hızlısı (2, yer yoksa 1) seçilir; "b" üçünü ölçer.
static Q4F head_flash, head_psram;
static int head_mod = 0;
static void head_par(const QT *t, const float *x, float *y) {
  static int8_t xq[LLM_Q8_MAX_INPUT];
  static int32_t gs[64];
  if (head_mod == 0) { MATVEC(t, x, y); return; }
  const Q4F *q = (head_mod == 2 && head_psram.codes) ? &head_psram : &head_flash;
  float xs;
  quantize_act(x, t->cols, xq, &xs);
  q4f_grup_toplam(xq, t->cols, t->group, gs);
  if (!iki_cekirdek) { q4f_range(q, xq, gs, xs, y, 0, t->rows); return; }
  job_fn = NULL; job_q = q; job_xq = xq; job_gs = gs; job_xs = xs; job_y = y; job_split = t->rows / 2;
  xTaskNotifyGive(worker_h);
  q4f_range(q, xq, gs, xs, y, job_split, t->rows);
  ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
}

// Head için float ölçekler (her zaman) ve PSRAM'de kod kopyası (yer varsa; 512 KB pay bırakılır).
static void head_hazirla() {
  const QT *h = &model.out_head;
  size_t ns = (size_t)h->rows * h->n_groups;
  float *sc = (float *)ps(ns * sizeof(float));
  if (!sc || h->n_groups > 64) { Serial.println("head: hızlı yol kurulamadı, eski yol"); head_mod = 0; return; }
  for (size_t i = 0; i < ns; i++) sc[i] = half2float(h->scales[i]);
  head_flash = {h->codes, sc, h->rows, h->cols, h->group, h->n_groups, h->row_bytes, false};
  head_psram = head_flash; head_psram.codes = NULL;
  size_t nb = (size_t)h->rows * h->row_bytes;
  if (heap_caps_get_free_size(MALLOC_CAP_SPIRAM) > nb + 512 * 1024) {
    uint8_t *c = (uint8_t *)ps(nb);
    if (c) { memcpy(c, h->codes, nb); head_psram.codes = c; head_psram.psram = true; }
  }
  head_mod = head_psram.codes ? 2 : 1;
  Serial.printf("head: 4-bit hızlı yol, kodlar %s (%.2f MB)\n", head_mod == 2 ? "PSRAM'de" : "flash'ta", nb / 1048576.0);
}

static const char *HEAD_AD[] = {"eski (tek çekirdek, flash)", "yeni, flash", "yeni, PSRAM"};

// ---- çekirdek katmanların PSRAM'e kopyası (llm_stage_core_int8_alloc ile aynı tensörler) ----
static int cekirdek_tensorleri(QT **t) {
  int n = 0;
  t[n++] = &model.ple_model_proj;
  for (int l = 0; l < model.c.n_layers; l++) {
    t[n++] = &model.qkv[l]; t[n++] = &model.attn_proj[l]; t[n++] = &model.gate[l]; t[n++] = &model.up[l];
    t[n++] = &model.down[l]; t[n++] = &model.ple_gate[l]; t[n++] = &model.ple_proj[l];
  }
  return n;
}
static size_t q4_kod_bayt(const QT *t) { return ((size_t)t->rows * t->row_bytes + 3) & ~(size_t)3; }
static size_t q4_bayt(const QT *t) { return q4_kod_bayt(t) + (size_t)t->rows * t->n_groups * sizeof(float); }
// 4-bit kodları PSRAM'e kopyalar, ölçekleri float'a çevirir (bir ayırma: kodlar + ölçekler). Döner: kopyalanan.
static int cekirdek_4bit_psram(QT **t, int n) {
  int k = 0;
  for (int i = 0; i < n; i++) {
    uint8_t *b = (uint8_t *)ps(q4_bayt(t[i]));
    if (!b) break;
    memcpy(b, t[i]->codes, (size_t)t[i]->rows * t[i]->row_bytes);
    float *sc = (float *)(b + q4_kod_bayt(t[i]));
    for (size_t g = 0; g < (size_t)t[i]->rows * t[i]->n_groups; g++) sc[g] = half2float(t[i]->scales[g]);
    t[i]->codes = b; t[i]->scale8 = sc;
    k++;
  }
  return k;
}

// ---- isim süzgeci: token baytları (vocab.h; gen -Y dosyasından farklı olan özel token'lar istemler.h'de) ----
static const char **suz_bayt = NULL;
static int *suz_uzun = NULL;
static IsimSuzgec suz;
static bool suzgec_kur() {
  suz_bayt = (const char **)ps(VOCAB_N * sizeof(char *));
  suz_uzun = (int *)ps(VOCAB_N * sizeof(int));
  if (!suz_bayt || !suz_uzun) { suz_bayt = NULL; return false; }
  for (int i = 0; i < VOCAB_N; i++) {
    suz_bayt[i] = (const char *)VOCAB_BLOB + VOCAB_OFF[i];
    suz_uzun[i] = (int)(VOCAB_OFF[i + 1] - VOCAB_OFF[i]);
  }
  for (int o = 0; o < SUZGEC_OZEL_N; o++) {
    suz_bayt[SUZGEC_OZEL_ID[o]] = SUZGEC_OZEL_BAYT[o];
    suz_uzun[SUZGEC_OZEL_ID[o]] = (int)strlen(SUZGEC_OZEL_BAYT[o]);
  }
  return true;
}

static int istem_onbellek_k = -1;   // KV'sinde istemi hazır tutulan (figür, yer); -1 yok
static float *istem_logit = NULL;   // o istemin son token'ından sonraki logit'ler (PSRAM)

static void alloc_scratch() {
  Cfg *c = &model.c;
  int D = c->dim, L = c->n_layers, P = c->ple_dim, F = c->ffn, S = c->seq_len;
  s.x = (float *)sram_or_die(D * 4, "x");
  s.h = (float *)sram_or_die((F > D ? F : D) * 4, "h");
  s.qkv = (float *)sram_or_die(3 * D * 4, "qkv");
  s.att = (float *)sram_or_die(D * 4, "att");
  s.g1 = (float *)sram_or_die(F * 4, "g1");
  s.g2 = (float *)sram_or_die((P > F ? P : F) * 4, "g2");
  s.ple = (float *)sram_or_die(L * P * 4, "ple");
  s.tmpP = (float *)sram_or_die(L * P * 4, "tmpP");
  s.trow = (float *)sram_or_die(L * P * 4, "trow");
  s.scores = (float *)sram_or_die(S * 4, "scores");
  s.logits = (float *)ps_or_die((size_t)model.out_vocab * 4, "logits");
  istem_logit = (float *)ps((size_t)model.out_vocab * 4);  // yoksa önbelleksiz
  s.kcache = (float *)ps_or_die((size_t)L * S * D * 4, "kcache");
  s.vcache = (float *)ps_or_die((size_t)L * S * D * 4, "vcache");
}

static void yaz(int tok) {
  if (tok < 0 || tok >= VOCAB_N) return;
  Serial.write(VOCAB_BLOB + VOCAB_OFF[tok], VOCAB_OFF[tok + 1] - VOCAB_OFF[tok]);
}

static void liste() {
  Serial.println("\nFigürler ve yerleri:");
  for (int f = 0; f < N_FIGUR; f++) {
    int harf = 0;
    for (const char *p = FIGUR_AD[f]; *p; p++) harf += (*p & 0xC0) != 0x80;
    Serial.printf("  %2d  %s%*s", f + 1, FIGUR_AD[f], harf < 13 ? 13 - harf : 0, "");
    for (int j = 0; j < FIGUR_YER_N[f]; j++) Serial.printf("  %d %s", j + 1, YER_AD[FIGUR_YER[f * YER_MAKS + j]]);
    Serial.println();
  }
  Serial.println("Örnek: \"8 4\" (Elsa, şato) | \"8\" (Elsa, sürpriz yer) | \"r\" (rastgele figür)");
  Serial.println("Hazır (kuyrukta) hikâye varsa hemen okunur, yoksa canlı yazılır.");
  Serial.println("Sona aday sayısı (en çok 16) eklenirse her zaman üretilir, en iyisi seçilir: \"8 4 8\" (8 aday).");
  Serial.println("(ürün önerisi: kuyrukta önceden hazırlanan hikâye K=16, beklenen hikâye K=4-8)");
  Serial.printf("Ses: \"s <metin>\" metni okur | \"o\" hikâyeyi okuma %s (şu an %s) | \"v+\" \"v-\" \"v N\" ses seviyesi\n",
                ses_var ? "aç/kapa" : "(ses modeli yok)", ses_var && ses_oku ? "açık" : "kapalı");
  Serial.println("Kuyruk: \"k\" durum | \"k+\" \"k-\" arka plan üretimi aç/kapa | \"k sil\" hazırları sil");
  Serial.println("Düğme taklidi: \"t f\" figür, \"t y\" yer, \"t o\" oynat (büyük harf: uzun basış), \"t +\" \"t -\" ses,"
                 " \"t a\" arka plan | \"n 04A1B2C3\" NFC etiketi | \"u\" uyku denemesi\n");
}

static int govde_yasak[2], idx[TOP_K];
static double olas[TOP_K];
static int16_t aday_tok[N_URET], en_tok[N_URET];

// gen -l log-olasılığı "%.4f" ile yazar, urun_uret.aday_uret onu okur: ortalama aynı sayılardan alınsın
static double lp4(double x) {
  char b[32];
  snprintf(b, sizeof b, "%.4f", x);
  return strtod(b, NULL);
}

// Python 3.12+ sum()'ı (Neumaier telafili toplam): urun_uret'in sum(glp) / len(glp) ortalaması bit bit aynı çıksın
struct PyToplam {
  double t = 0.0, c = 0.0;
  void ekle(double x) {
    double y = t + x;
    c += fabs(t) >= fabs(x) ? (t - y) + x : (x - y) + t;
    t = y;
  }
  double deger() const { return (c != 0.0 && isfinite(c)) ? t + c : t; }
};

// Bir aday üretir (urun_uret.aday_uret): aday_tok'a plan + gövde token'ları (gövdedeki EOT hariç).
// canli: token'lar üretildikçe seriye yazılır. uretim_kes verilmişse her token'dan önce sorulur: true dönerse aday
// yarıda bırakılır (Aday.iptal; KV'de istem dışında bir şey saklanmadığından sonraki aday baştan başlar).
static int64_t ornek_us = 0;  // örnekleme (top-k, ceza, süzgeç) süresi
static bool (*uretim_kes)() = NULL;

static Aday aday_uret(int f, int j, bool canli) {
  govde_yasak[0] = GOVDE_YASAK[0]; govde_yasak[1] = GOVDE_YASAK[1];
  OrnAyar ayar = {SICAKLIK, TOP_K, TEKRAR, NULL, 0, govde_yasak, 2, idx, olas, NULL, NULL};
  if (suz_bayt) {  // gen -Y: figürün kadro dışı adları
    int a0 = SUZGEC_AD_OFF[f];
    isim_suzgec_kur(&suz, suz_bayt, suz_uzun, VOCAB_N, SUZGEC_AD + a0, SUZGEC_AD_UZUN + a0, SUZGEC_AD_OFF[f + 1] - a0);
    ayar.suzgec = isim_suzgec_uygun; ayar.suzgec_baglam = &suz;
  }
  OrnDurum st; orn_sifirla(&st);
  int k = f * YER_MAKS + j, pos = 0, tok = 0;
  Aday a = {0, 0, 0.0, false, false, false};
  // İstem her adayda aynı: bir kez işlenir. Sonraki adaylar yalnız istemden sonraki KV konumlarına yazdığından
  // istemin KV'si bozulmaz; istem sonundaki logit'ler saklanıp geri yüklenir (sonuç bit bit aynı, ~%10 hız).
  bool hazir = istem_onbellek_k == k && istem_logit;
  if (!hazir) istem_onbellek_k = -1;  // istem yarıda kesilirse önceki istemin KV'si yarı yarıya ezilmiş olur
  for (int i = ISTEM_OFF[k]; i < ISTEM_OFF[k + 1]; i++) {  // istem tekrar penceresine girmez (gen -P)
    tok = ISTEM_ID[i];
    if (suz_bayt) isim_suzgec_ekle(&suz, tok);             // süzgeç istemi de görür (gen -Y)
    if (hazir) { pos++; continue; }
    if (uretim_kes && uretim_kes()) { a.iptal = true; return a; }
    llm_forward(&model, tok, pos++, &s);
    bekci_besle();
  }
  if (hazir) memcpy(s.logits, istem_logit, (size_t)model.out_vocab * sizeof(float));
  else if (istem_logit) { memcpy(istem_logit, s.logits, (size_t)model.out_vocab * sizeof(float)); istem_onbellek_k = k; }
  orn_plan_baslat(&st, NL_ID);
  PyToplam lp; int n_lp = 0;
  if (canli) Serial.print("Sorun:");
  for (int step = 0; step < N_URET && pos < model.c.seq_len; step++) {
    if (uretim_kes && uretim_kes()) { a.iptal = true; break; }  // düğme / seri: aday yarıda (sonuç kullanılmaz)
    bool govdede = st.govde;
    int64_t to = esp_timer_get_time();
    tok = orn_adim(&ayar, &st, s.logits, model.out_vocab);
    if (suz_bayt) isim_suzgec_ekle(&suz, tok);
    ornek_us += esp_timer_get_time() - to;
    if (govdede) {
      if (tok == EOT_ID) { a.bitti = true; break; }        // gövde biter (plandaki EOT gen'de olduğu gibi geçer)
      lp.ekle(lp4(orn_logp(s.logits, model.out_vocab, tok))); n_lp++;  // gövdenin güveni (gen -l ile aynı)
    }
    aday_tok[a.n++] = tok;
    if (!govdede) a.n_plan = a.n;
    if (canli) yaz(tok);
    if (st.plan_bozuk) break;
    llm_forward(&model, tok, pos++, &s);
    bekci_besle();
    if ((step & 7) == 0) delay(0);
  }
  a.plan_bozuk = !st.govde;  // gövdeye (plan sonrası "nl nl") varılamadı: urun_uret plan_bozuk
  a.lp = n_lp ? lp.deger() / n_lp : 0.0;
  return a;
}

// token'ların ham UTF-8 baytlarını buf'a ekler (VOCAB_BLOB); döner: yeni uzunluk (cap'te kesilir)
static int coz_ekle(const int16_t *t, int n, char *buf, int len, int cap) {
  for (int i = 0; i < n; i++) {
    int tok = t[i];
    if (tok < 0 || tok >= VOCAB_N) continue;
    int b = VOCAB_OFF[tok], e = VOCAB_OFF[tok + 1];
    if (len + (e - b) > cap) break;
    memcpy(buf + len, VOCAB_BLOB + b, e - b);
    len += e - b;
  }
  return len;
}

// Python str.strip()'in boşlukları (sc_bosluk): p'deki (bas) ya da p'den önceki (son) boşluk harfinin bayt sayısı
static int bosluk_bayt(const unsigned char *p, int kalan, bool son) {
  for (int L = 1; L <= 3 && L <= kalan; L++) {
    const unsigned char *c = son ? p - L : p;
    uint32_t h = 0;
    if (L == 1 && c[0] < 0x80) h = c[0];
    else if (L == 2 && c[0] == 0xC2 && (c[1] & 0xC0) == 0x80) h = c[1];
    else if (L == 3 && (c[0] & 0xF0) == 0xE0 && (c[1] & 0xC0) == 0x80 && (c[2] & 0xC0) == 0x80)
      h = ((c[0] & 15) << 12) | ((c[1] & 63) << 6) | (c[2] & 63);
    else continue;
    return sc_bosluk(h) ? L : 0;
  }
  return 0;
}

// Seçici (secici.h = urun_uret.puanla): gövde metni urun_uret.aday_uret'teki gibi çözülüp kırpılır (.strip()), plan
// "Sorun:" + plan token'ları (son "nl nl" hariç). Plan bozuksa -99 (urun_uret: "gövde yok").
static char govde_buf[4096], plan_buf[1024];
static double puanla(const Aday &a, int f, int j) {
  if (a.plan_bozuk) { for (int i = 0; i < SK_N; i++) secici_kural[i] = 0; secici_kural[SK_GOVDE_YOK] = 99; return -99.0; }
  int gn = coz_ekle(aday_tok + a.n_plan, a.n - a.n_plan, govde_buf, 0, sizeof govde_buf), bas = 0, L;
  const unsigned char *g = (const unsigned char *)govde_buf;
  while (bas < gn && (L = bosluk_bayt(g + bas, gn - bas, false))) bas += L;
  while (gn > bas && (L = bosluk_bayt(g + gn, gn - bas, true))) gn -= L;
  memcpy(plan_buf, "Sorun:", 6);
  int pn = coz_ekle(aday_tok, a.n_plan - 2, plan_buf, 6, sizeof plan_buf);
  while (pn > 6 && (L = bosluk_bayt((const unsigned char *)plan_buf + pn, pn - 6, true))) pn -= L;
  return secici_urun_puanla(govde_buf + bas, gn - bas, plan_buf, pn, f, FIGUR_YER[f * YER_MAKS + j], a.bitti, a.lp);
}

// Son puanlanan adayın sıfır olmayan kural cezaları: " (sonda_yok 3, plan 2)"
static void kural_yaz() {
  bool ilk = true;
  for (int i = 0; i < SK_N; i++) {
    if (secici_kural[i] == 0) continue;
    Serial.printf("%s%s %.1f", ilk ? " (" : ", ", SECICI_KURAL_AD[i], secici_kural[i]);
    ilk = false;
  }
  if (!ilk) Serial.print(")");
}

// Token başına ms: girdi, dikkat, FFN, PLE, head (llm.h LLM_PROFILE) ve örnekleme.
static void profil_yaz() {
  uint32_t n = s.profile.calls ? s.profile.calls : 1;
  double gir = s.profile.input_us / 1e3 / n, att = s.profile.attn_us / 1e3 / n, ffn = s.profile.ffn_us / 1e3 / n,
         ple = s.profile.ple_us / 1e3 / n, head = s.profile.head_us / 1e3 / n, orn = ornek_us / 1e3 / n;
  double top = gir + att + ffn + ple + head + orn;
  Serial.printf("profil (ms/token, %u adım): girdi %.1f | dikkat %.1f | FFN %.1f | PLE %.1f | head %.1f | örnekleme %.1f"
                " | toplam %.1f (%.2f token/s) | head: %s\n",
                (unsigned)s.profile.calls, gir, att, ffn, ple, head, orn, top, 1000.0 / top, HEAD_AD[head_mod]);
}

// "b": aynı istemle 48 adım, head'in üç yolu için ayrı ayrı ölçer; en hızlısını seçili bırakır.
static void hiz_testi() {
  istem_onbellek_k = -1;  // test KV'yi başka istemle doldurur
  int secilen = head_mod, en = head_mod;
  double en_ms = 1e30;
  for (int mod = 0; mod < 3; mod++) {
    if (mod == 2 && !head_psram.codes) continue;
    head_mod = mod;
    llm_profile_reset(&s); ornek_us = 0;
    int k = 0, pos = 0;
    int64_t t0 = esp_timer_get_time();
    for (int i = ISTEM_OFF[k]; i < ISTEM_OFF[k + 1] && pos < 48; i++) llm_forward(&model, ISTEM_ID[i], pos++, &s);
    bekci_besle();
    int tok = 0;
    while (pos < 48) {  // açgözlü: en olası token (örnekleme ölçüme girmesin)
      int b = 0;
      for (int v = 1; v < model.out_vocab; v++) if (s.logits[v] > s.logits[b]) b = v;
      tok = b;
      llm_forward(&model, tok, pos++, &s);
      bekci_besle();
    }
    double ms = (esp_timer_get_time() - t0) / 1e3 / pos;
    Serial.printf("head %-28s %.1f ms/token = %.2f token/s\n", HEAD_AD[mod], ms, 1000.0 / ms);
    profil_yaz();
    if (ms < en_ms) { en_ms = ms; en = mod; }
    delay(0);
  }
  head_mod = en;
  Serial.printf("seçilen head yolu: %s (önceki: %s)\n\n", HEAD_AD[head_mod], HEAD_AD[secilen]);
}

// ---- durum: seçili figür/yer, son okunan hikâye ----
static int secili_f = 0, secili_j = -1;      // düğmelerle seçilen figür ve figürün yeri (-1: sürpriz)
static int16_t son_tok[N_URET];              // son okunan hikâye (OYNAT uzun: yeniden oku)
static int son_n = 0, son_plan = 0, son_f = -1, son_j = -1;

// ---- olaylar: düğmeler (dugmeler.h; kartta ayrı görevde 10 ms'de bir örneklenir), NFC (nfc.h), seri taklit ----
static Dugmeler dg;                 // düğme görevi üretir, ana döngü tüketir
static OlayHalka ana_halka;         // ana döngünün kendi olayları (NFC, "t" komutu)
static const int DUGME_PIN[DUGME_N] = {DUGME_FIGUR_PIN, DUGME_YER_PIN, DUGME_OYNAT_PIN};
static bool dugme_gorevi_var = false, nfc_var = false;
static uint32_t nfc_son_ms = 0, nfc_gordu_ms = 0;
static uint8_t nfc_son_uid[10];
static int nfc_son_n = 0;

static void dugme_tara() {
  bool b[DUGME_N];
  for (int i = 0; i < DUGME_N; i++) b[i] = DUGME_PIN[i] >= 0 && digitalRead(DUGME_PIN[i]) == LOW;
  dugme_adim(&dg, b, millis());
}
static void dugme_gorevi(void *) {
  for (;;) {
    dugme_tara();
    vTaskDelay(pdMS_TO_TICKS(10));
  }
}

static void uid_yaz(const uint8_t *u, int n) {
  for (int i = 0; i < n; i++) Serial.printf("%02X", u[i]);
}

// Okunan (ya da "n" komutuyla verilen) etiket: tablodaysa figür olayı
static void nfc_etiket(const uint8_t *u, int n) {
  int f = nfc_figur(u, n);
  if (f < 0 || f >= N_FIGUR) {
    Serial.print("bilinmeyen etiket: ");
    uid_yaz(u, n);
    Serial.println(" (nfc.h NFC_TABLO'ya figürüyle ekleyin)");
    return;
  }
  halka_ekle(&ana_halka, OLAY_NFC, (int8_t)f);
}

// Okuyucuyu yoklar: yeni etiket konunca bir kez olay verir; etiket 1,5 s görünmezse kalkmış sayılır.
static void nfc_tara() {
  uint8_t u[10];
  int n = nfc_uid_oku(u, sizeof u);
  uint32_t simdi = millis();
  if (n <= 0) {
    if (nfc_son_n && simdi - nfc_gordu_ms > 1500) nfc_son_n = 0;
    return;
  }
  nfc_gordu_ms = simdi;
  if (n == nfc_son_n && !memcmp(u, nfc_son_uid, n)) return;
  memcpy(nfc_son_uid, u, n);
  nfc_son_n = n;
  nfc_etiket(u, n);
}

// Düğme görevi yoksa (bilgisayardaki deneme) düğmeleri burada örnekler; NFC'yi 250 ms'de bir yoklar.
static void olaylari_topla() {
  if (!dugme_gorevi_var) dugme_tara();
  if (nfc_var && millis() - nfc_son_ms >= 250) { nfc_son_ms = millis(); nfc_tara(); }
}
static bool olay_bak_(Olay *o) { return halka_bak(&ana_halka, o) || halka_bak(&dg.h, o); }
static bool olay_al_(Olay *o) { return halka_al(&ana_halka, o) || halka_al(&dg.h, o); }
static bool olay_var() { olaylari_topla(); return olay_bak_(NULL); }
// Konuşmayı ya da canlı üretimi durduran OYNAT basışı "dur" demektir: ardından yeni hikâye başlatmasın.
static void oynat_olayini_yut() {
  Olay o;
  if (olay_bak_(&o) && o.tur == OLAY_OYNAT) olay_al_(&o);
}
static bool durdur_istendi() { return olay_var() || Serial.available() > 0; }
static bool canli_kes() { return olay_var(); }  // canlı hikâye ve "f j K" testi: yalnız düğme/NFC keser

// ---- LED (kart üstü RGB; DURUM_LED_PIN varsa o da) ----
enum { LED_KAPALI, LED_KONUSMA, LED_CANLI, LED_ARKA, LED_HATA, LED_TAMAM };
static uint8_t led_rgb[3] = {1, 1, 1};  // ilk yazım gönderilsin
static void led_renk(uint8_t r, uint8_t g, uint8_t b) {
  if (led_rgb[0] == r && led_rgb[1] == g && led_rgb[2] == b) return;
  led_rgb[0] = r; led_rgb[1] = g; led_rgb[2] = b;
#ifdef RGB_BUILTIN
#if defined(ESP_ARDUINO_VERSION_MAJOR) && ESP_ARDUINO_VERSION_MAJOR >= 3
  rgbLedWrite(RGB_BUILTIN, r, g, b);
#else
  neopixelWrite(RGB_BUILTIN, r, g, b);
#endif
#endif
#if DURUM_LED_PIN >= 0
  digitalWrite(DURUM_LED_PIN, (r | g | b) ? HIGH : LOW);
#endif
}
static void led(int durum) {
  const uint8_t L = LED_PARLAKLIK;
  switch (durum) {
    case LED_KONUSMA: led_renk(0, L, 0); break;            // yeşil: konuşuyor
    case LED_CANLI: led_renk(L, L / 2, 0); break;          // turuncu: çocuk beklerken canlı üretiyor
    case LED_ARKA: led_renk(0, 0, L / 8 + 1); break;       // loş mavi: boşta kuyruğa üretiyor
    case LED_HATA: led_renk(L, 0, 0); break;               // kırmızı: model yok / hata
    case LED_TAMAM: led_renk(L / 2, L / 2, L / 2); break;  // beyaz: düğme alındı
    default: led_renk(0, 0, 0);
  }
}
static void led_yanip(int durum, int kez) {
  for (int i = 0; i < kez; i++) {
    led(durum); delay(120);
    led(LED_KAPALI); delay(120);
  }
}

// ---- ses: metinden konuşma (ses.h), I2S hoparlör, ses seviyesi ----
static const int I2S_BCLK = I2S_BCLK_PIN, I2S_LRC = I2S_LRC_PIN, I2S_DIN = I2S_DIN_PIN;
static const int CAL_BAYT = 32000;      // çalma tamponu: 1 s ses (16 kHz x 2 B)
static const int SES_SR = 16000;        // ses.bin yoksa da (bip için) I2S bu hızda
static Ses ses;
static I2SClass i2s;
static bool ses_model_var = false, hoparlor_var = false;
static StreamBufferHandle_t cal_akim = NULL;
static StaticStreamBuffer_t cal_yapi;
static int64_t cal_bekleme_us = 0;      // sentez, çalma tamponu dolu diye bu kadar bekledi (hesap süresinden düşülür)
static char oku_buf[4096];
static volatile bool cal_sustur = false;                   // çalıcı tampondakini atsın (konuşma kesildi)
static bool konusma_kesildi = false, konusma_kesilebilir = false;
static int ses_seviye = SES_SEVIYE_VARSAYILAN;
static_assert(SES_SEVIYE_N == 8, "SES_KAZANC tablosu 8 seviye");
static const int16_t SES_KAZANC[SES_SEVIYE_N] = {32, 45, 64, 90, 128, 181, 256, 362};  // Q8 (256 = 1), ~3 dB adım

// Sıcak tamponlar (SES_ALT kare etkinlik, FFT) dahili SRAM'e, 48 KB pay bırakarak; gerisi PSRAM.
static void *ses_ayir(size_t n, int sicak) {
  void *p = NULL;
  if (sicak && heap_caps_get_free_size(MALLOC_CAP_INTERNAL) > n + 48 * 1024)
    p = heap_caps_malloc(n, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
  if (!p) p = ps(n);
  return p;
}

// ses.h'nin matris işlerini iki çekirdeğe böler (LLM ile aynı işçi görevi; ikisi aynı anda çalışmaz)
static void ses_paralel(SesIs is, void *arg, int n) {
  if (!iki_cekirdek || n < 32) { is(arg, 0, n, 0); return; }
  job_fn = is; job_arg = arg; job_split = n / 2;
  xTaskNotifyGive(worker_h);
  is(arg, job_split, n, 0);
  ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
  job_fn = NULL;
}

// MAX98357A SD ucu bağlıysa: konuşmazken yükselteç kapalı (boşta ~2-3 mA, hışırtı yok)
static void amp(bool acik) {
#if AMP_SD_PIN >= 0
  digitalWrite(AMP_SD_PIN, acik ? HIGH : LOW);
  if (acik) delay(5);
#else
  (void)acik;
#endif
}

// Çalma görevi: tampondan I2S'e (i2s.write DMA dolunca bekler). Sentez bu arada sonraki parçayı hesaplar.
static void calici(void *) {
  static int16_t buf[256];
  for (;;) {
    size_t n = xStreamBufferReceive(cal_akim, buf, sizeof buf, portMAX_DELAY);
    if (n && !cal_sustur) i2s.write((const uint8_t *)buf, n);
  }
}

// Sentezin PCM'i: ses seviyesiyle ölçeklenip (doyumlu) çalma tamponuna. Düğmeye basılır ya da seri porta bir şey
// gelirse konuşma hemen susar (tampondaki ses atılır; sentez cümle sonunda durur).
static void pcm_yaz(void *, const int16_t *pcm, int n) {
  if (konusma_kesildi) return;
  if (konusma_kesilebilir && durdur_istendi()) { konusma_kesildi = true; cal_sustur = true; return; }
  static int16_t buf[256];
  const int32_t g = SES_KAZANC[ses_seviye];
  int64_t t0 = esp_timer_get_time();
  while (n > 0) {
    int k = n < 256 ? n : 256;
    for (int i = 0; i < k; i++) {
      int32_t v = ((int32_t)pcm[i] * g) / 256;
      buf[i] = (int16_t)(v > 32767 ? 32767 : v < -32768 ? -32768 : v);
    }
    const uint8_t *p = (const uint8_t *)buf;
    size_t kalan = (size_t)k * 2;
    while (kalan) {
      size_t y = xStreamBufferSend(cal_akim, p, kalan, portMAX_DELAY);
      p += y; kalan -= y;
    }
    pcm += k; n -= k;
  }
  cal_bekleme_us += esp_timer_get_time() - t0;
  bekci_besle();
}

static int ses_dur(void *) {  // cümle aralarında: durdurulsun mu
  if (!konusma_kesildi && konusma_kesilebilir && durdur_istendi()) { konusma_kesildi = true; cal_sustur = true; }
  return konusma_kesildi;
}

// Tampon boşalsın, DMA'da kalan (6 x 240 örnek = 90 ms) çalınsın
static void cal_bitir() {
  while (!xStreamBufferIsEmpty(cal_akim)) delay(10);
  delay(120);
  cal_sustur = false;
}

// Metni cümle cümle seslendirir (ilk cümle sentezlenirken çalmaya başlar); bitince çalmanın bitmesini bekler.
// rapor: "[ses: ...]" satırı yazılsın. Döner: sonuna kadar okundu (düğme/seri ile kesilmedi).
static bool konus_(const char *metin, bool rapor) {
  if (!ses_var) { if (rapor) Serial.println("konuşma kapalı (ses bölümü ya da ses.bin yok)"); return false; }
  amp(true);
  led(LED_KONUSMA);
  cal_bekleme_us = 0;
  konusma_kesildi = false;
  konusma_kesilebilir = true;
  int64_t t0 = esp_timer_get_time();
  long n = ses_metin(&ses, metin, pcm_yaz, NULL, 250, ses_dur);
  float hesap = (esp_timer_get_time() - t0 - cal_bekleme_us) / 1e6f, sure = n > 0 ? n / (float)ses.sr : 0.f;
  bool kesildi = konusma_kesildi;
  konusma_kesilebilir = false;
  if (!kesildi) ses_sessizlik(&ses, 150, pcm_yaz, NULL);  // DMA'da kalan son parça sussun
  cal_bitir();
  konusma_kesildi = false;
  led(LED_KAPALI);
  amp(false);
  if (n < 0) Serial.printf("ses hatası: %s\n", ses_hata);
  else if (rapor)
    Serial.printf("[ses: %.1f s konuşma, %.1f s hesap = %.2f s hesap / s ses%s]\n", sure, hesap,
                  sure > 0 ? hesap / sure : 0.f, kesildi ? "; durduruldu" : "");
  return !kesildi && n >= 0;
}
static void konus(const char *metin) { konus_(metin, true); }

// Kısa ton (ses modeli olmasa da hoparlör varsa): düğme onayı, ses seviyesi, hata. Kesilmez.
static void bip(int hz, int ms) {
  if (!hoparlor_var) return;
  amp(true);
  static int16_t b[256];
  int n = SES_SR * ms / 1000, kenar = SES_SR / 200;  // 5 ms yumuşak giriş/çıkış (tık sesi olmasın)
  for (int i = 0; i < n;) {
    int k = n - i < 256 ? n - i : 256;
    for (int t = 0; t < k; t++) {
      int u = i + t, z = u < kenar ? u : n - 1 - u < kenar ? n - 1 - u : kenar;
      b[t] = (int16_t)(6000.f * z / kenar * sinf(6.2831853f * hz * u / SES_SR));
    }
    pcm_yaz(NULL, b, k);
    i += k;
  }
  memset(b, 0, sizeof b);
  for (int i = 0; i < SES_SR * 60 / 1000; i += 256) pcm_yaz(NULL, b, 256);
  cal_bitir();
  amp(false);
}

// Kısa duyuru (figür / yer adı): ses modeli varsa söyler, yoksa bip
static void duyur(const char *metin) {
  Serial.printf("[%s]\n", metin);
  if (ses_var) konus_(metin, false);
  else bip(880, 70);
}

// I2S, çalma tamponu ve çalma görevi (ses.bin olmasa da: bip)
static void hoparlor_kur(int sr) {
  uint8_t *depo = (uint8_t *)ps(CAL_BAYT + 1);
  if (!depo) depo = (uint8_t *)heap_caps_malloc(CAL_BAYT + 1, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
  if (!depo) { Serial.println("ses: çalma tamponu ayrılamadı: konuşma kapalı"); return; }
  cal_akim = xStreamBufferCreateStatic(CAL_BAYT, 1, depo, &cal_yapi);
  i2s.setPins(I2S_BCLK, I2S_LRC, I2S_DIN);
  if (!i2s.begin(I2S_MODE_STD, sr, I2S_DATA_BIT_WIDTH_16BIT, I2S_SLOT_MODE_MONO, I2S_STD_SLOT_BOTH)) {
    Serial.println("ses: I2S başlatılamadı: konuşma kapalı"); return;
  }
  if (xTaskCreatePinnedToCore(calici, "cal", 4096, NULL, 5, NULL, 0) != pdPASS) {
    Serial.println("ses: çalma görevi kurulamadı: konuşma kapalı"); return;
  }
  hoparlor_var = true;
}

// Açılışta: "ses" bölümü (alt tip 0x41) ve ses.bin varsa modeli; her durumda I2S'i ve çalma görevini kurar.
static void ses_kur() {
  const esp_partition_t *part = esp_partition_find_first(ESP_PARTITION_TYPE_DATA,
                                                         (esp_partition_subtype_t)0x41, "ses");
  const void *base;
  esp_partition_mmap_handle_t h;
  if (!part) Serial.println("ses bölümü yok (eski partitions.csv): konuşma kapalı");
  else if (esp_partition_mmap(part, 0, part->size, ESP_PARTITION_MMAP_DATA, &base, &h) != ESP_OK)
    Serial.println("ses: mmap başarısız: konuşma kapalı");
  else if (ses_yukle(&ses, (const uint8_t *)base, part->size, ses_ayir))
    Serial.printf("ses: %s: konuşma kapalı (ses.bin 0x%X adresine yüklendi mi?)\n", ses_hata, (unsigned)part->address);
  else {
    ses.paralel = ses_paralel;
    ses_model_var = true;
  }
  hoparlor_kur(ses_model_var ? ses.sr : SES_SR);
  ses_var = ses_oku = ses_model_var && hoparlor_var;
  led(LED_KAPALI);
  if (ses_var)
    Serial.printf("ses: akustik d=%d (%d+%d+%d blok), vocoder d=%d (%d blok) | bellek %.0f KB PSRAM + %.0f KB SRAM | "
                  "I2S BCLK %d LRC %d DIN %d | hikâyeyi okuma: açık (\"o\" ile kapat)\n",
                  ses.ad, ses.n_kod, ses.n_tah, ses.n_coz, ses.vd, ses.n_vblok, ses.bellek_buyuk / 1024.0,
                  ses.bellek_sicak / 1024.0, I2S_BCLK, I2S_LRC, I2S_DIN);
  else if (hoparlor_var)
    Serial.printf("hoparlör: açık, yalnız bip (I2S BCLK %d LRC %d DIN %d); hikâyeler seri porta yazılır\n",
                  I2S_BCLK, I2S_LRC, I2S_DIN);
}

// Gövde token'larını (plan hariç) metne çevirip okur. Döner: sonuna kadar okundu.
static bool hikaye_oku(const int16_t *t, int n) {
  int len = 0;
  for (int i = 0; i < n; i++) {
    int tok = t[i];
    if (tok < 0 || tok >= VOCAB_N) continue;
    int b = VOCAB_OFF[tok], e = VOCAB_OFF[tok + 1];
    if (len + (e - b) >= (int)sizeof oku_buf) break;
    memcpy(oku_buf + len, VOCAB_BLOB + b, e - b);
    len += e - b;
  }
  oku_buf[len] = 0;
  return konus_(oku_buf, true);
}

static void son_hikaye_sakla(const int16_t *t, int n, int n_plan, int f, int j) {
  memcpy(son_tok, t, n * sizeof(int16_t));
  son_n = n; son_plan = n_plan; son_f = f; son_j = j;
}

// f figür, j figürün kart yeri (0'dan), K aday: urun_uret.main'in bir vakası (en yüksek puanlı aday; eşitlikte ilki).
// Düğmeye basılırsa (ya da NFC) yarıda kesilir. Döner: hikâye üretildi.
static bool hikaye(int f, int j, int K) {
  Serial.printf("\n=== %s | %s | %d aday ===\n", FIGUR_AD[f], YER_AD[FIGUR_YER[f * YER_MAKS + j]], K);
  int64_t t0 = esp_timer_get_time();
  llm_profile_reset(&s); ornek_us = 0;
  int toplam = 0, en_n = 0, en_plan = 0; double en_p = -1e30;
  bool kesildi = false;
  led(LED_CANLI);
  uretim_kes = canli_kes;
  for (int jj = 0; jj < K; jj++) {
    ADAY_BASI(jj);
    Aday a = aday_uret(f, j, K == 1);
    // Tek adayda plan bozulursa (plan satırı yerine hikâye başlarsa) en çok iki kez yeniden dene.
    for (int tekrar = 0; K == 1 && a.plan_bozuk && !a.iptal && tekrar < 2; tekrar++) {
      toplam += a.n;
      Serial.println("\n(plan bozuk, yeniden deniyorum)");
      a = aday_uret(f, j, true);
    }
    if (a.iptal) { kesildi = true; break; }
    toplam += a.n + (a.bitti ? 1 : 0);
    double p = puanla(a, f, j);
    ADAY_SONU(jj, a, p);
    if (K > 1) {
      Serial.printf("aday %d/%d: %d token, güven %.3f, %s -> puan %.2f", jj + 1, K, a.n, a.lp,
                    a.plan_bozuk ? "plan bozuk" : a.bitti ? "bitti" : "yarım", p);
      if (!a.plan_bozuk) kural_yaz();
      Serial.println();
    }
    if (p > en_p) { en_p = p; en_n = a.n; en_plan = a.n_plan; memcpy(en_tok, aday_tok, a.n * sizeof(int16_t)); }
  }
  uretim_kes = NULL;
  led(LED_KAPALI);
  if (kesildi) {
    Serial.println("\n(durduruldu)");
    oynat_olayini_yut();
    return false;
  }
  if (K > 1) {
    Serial.print("\nSorun:");
    for (int i = 0; i < en_n; i++) yaz(en_tok[i]);
  }
  float sn = (esp_timer_get_time() - t0) / 1e6f;
  Serial.printf("\n\n--- %d aday, toplam %d token %.1f s = %.2f token/s ---\n", K, toplam, sn, toplam / sn);
  profil_yaz();
  son_hikaye_sakla(en_tok, en_n, en_plan, f, j);
  if (ses_var && ses_oku && en_n > en_plan && !hikaye_oku(en_tok + en_plan, en_n - en_plan)) oynat_olayini_yut();
  Serial.println("Yeni hikâye için figür ve yer yazın (\"?\" liste).");
  return true;
}

// LLM'i kurar; model yoksa false (konuşma yine çalışabilir)
static bool llm_kur() {
  const esp_partition_t *part = esp_partition_find_first(ESP_PARTITION_TYPE_DATA,
                                                         (esp_partition_subtype_t)0x40, "model");
  if (!part) { Serial.println("model bölümü yok (partitions.csv?)"); return false; }
  const void *base;
  esp_partition_mmap_handle_t h;
  if (esp_partition_mmap(part, 0, part->size, ESP_PARTITION_MMAP_DATA, &base, &h) != ESP_OK) {
    Serial.println("mmap başarısız"); return false;
  }
  if (llm_load((const uint8_t *)base, &model)) { Serial.println("model okunamadı (model.bin yüklendi mi?)"); return false; }
  if (model.image_bytes > part->size) { Serial.println("HATA: model.bin bölümden büyük"); return false; }
  if (model.c.seq_len > BAGLAM) model.c.seq_len = BAGLAM;  // RoPE konumdan hesaplanır; S yalnız KV adımı
  Cfg *c = &model.c;
  Serial.printf("model: V=%d D=%d L=%d H=%d F=%d P=%d bağlam=%d\n", model.out_vocab, c->dim, c->n_layers,
                c->n_heads, c->ffn, c->ple_dim, c->seq_len);
  if (VOCAB_N != model.out_vocab) {
    Serial.printf("HATA: tokenizer/model uyuşmuyor: vocab.h %d, model %d\n", VOCAB_N, model.out_vocab);
    return false;
  }
  alloc_scratch();
  size_t kv = psram_used;
  if (!suzgec_kur()) Serial.println("UYARI: isim süzgeci için PSRAM yok: başka figürlerin adları engellenmiyor");
  // Çekirdek: int8 sığarsa (ses ve head ölçekleri için pay bırakarak) int8, yoksa 4-bit PSRAM'de, o da yoksa flash.
  QT *t[1 + 7 * LLM_MAX_LAYERS];
  int n = cekirdek_tensorleri(t);
  size_t i8 = 0, q4 = 0, bos = heap_caps_get_free_size(MALLOC_CAP_SPIRAM);
  for (int i = 0; i < n; i++) { i8 += llm_stage_int8_bytes(t[i]); q4 += q4_bayt(t[i]); }
  size_t head_olcek = (size_t)model.out_head.rows * model.out_head.n_groups * sizeof(float);
  const char *yol;
  if (bos > i8 + head_olcek + SES_PAY) {
    int staged = llm_stage_core_int8_alloc(&model, ps);
    if (staged != n) { Serial.printf("HATA: çekirdek %d/%d tensör PSRAM'e kopyalandı\n", staged, n); while (1) delay(1000); }
    yol = "int8";
  } else if (bos > q4 + head_olcek) {
    int k = cekirdek_4bit_psram(t, n);
    if (k != n) Serial.printf("UYARI: çekirdek %d/%d tensör PSRAM'de, kalanı flash'ta (yavaş)\n", k, n);
    yol = "4-bit";
  } else {
    yol = "flash'ta 4-bit (PSRAM yetmedi, yavaş)";
  }
  size_t suz_b = suz_bayt ? VOCAB_N * (sizeof(char *) + sizeof(int)) : 0;
  Serial.printf("PSRAM: KV + logits %.2f MB, süzgeç %.2f MB, çekirdek %s %.2f MB (int8 %.2f MB gerekirdi)\n",
                kv / 1048576.0, suz_b / 1048576.0, yol, (psram_used - kv - suz_b) / 1048576.0, i8 / 1048576.0);

  model.layer_matvec = matvec_par;
  model.head_matvec = head_par;
  head_hazirla();
  Serial.printf("PSRAM toplam (LLM): %.2f MB\n", psram_used / 1048576.0);
  {
    const uint8_t *img = (const uint8_t *)base;
    uint32_t fp = 2166136261u;
    for (size_t i = 0; i < model.image_bytes; i++) { fp ^= img[i]; fp *= 16777619u; }
    Serial.printf("model.bin: %u B, parmak izi fp=%08x\n", (unsigned)model.image_bytes, (unsigned)fp);
    model_fp = fp;
  }
  Serial.printf("boş: SRAM %.0f KB | PSRAM %.2f MB\n", heap_caps_get_free_size(MALLOC_CAP_INTERNAL) / 1024.0,
                heap_caps_get_free_size(MALLOC_CAP_SPIRAM) / 1048576.0);
  return true;
}

static bool llm_var = false;

// ---- hikâye kuyruğu (kuyruk.h): flash'taki "kuyruk" bölümü (alt tip 0x42) ----
static Kuyruk kq;
static bool kuyruk_var = false, arka_acik = true;
static int arka_yazilan = 0;                 // bu açılışta kuyruğa yazılan hikâye
static int kf_oku(void *kul, uint32_t ofs, void *b, uint32_t n) {
  return esp_partition_read((const esp_partition_t *)kul, ofs, b, n) != ESP_OK;
}
static int kf_yaz(void *kul, uint32_t ofs, const void *b, uint32_t n) {
  return esp_partition_write((const esp_partition_t *)kul, ofs, b, n) != ESP_OK;
}
static int kf_sil(void *kul, uint32_t ofs, uint32_t n) {
  return esp_partition_erase_range((const esp_partition_t *)kul, ofs, n) != ESP_OK;
}

// Açılışta: bölümü tarar. İmza = model parmak izi + istem ve yer tabloları: model ya da kartlar değişince eski
// hikâyeler geçersiz sayılır (yuvaları yeniden kullanılır).
static void kuyruk_hazirla() {
  const esp_partition_t *part = esp_partition_find_first(ESP_PARTITION_TYPE_DATA,
                                                         (esp_partition_subtype_t)0x42, "kuyruk");
  if (!part) { Serial.println("kuyruk bölümü yok (eski partitions.csv): hazır hikâye yok, hep canlı üretilir"); return; }
  if (!llm_var) return;
  uint32_t imza = kuyruk_fnv(model_fp, ISTEM_ID, sizeof ISTEM_ID);
  imza = kuyruk_fnv(imza, FIGUR_YER, sizeof FIGUR_YER);
  KuyrukFlash fl = {(void *)part, kf_oku, kf_yaz, kf_sil, part->size};
  int n = kuyruk_kur(&kq, &fl, imza);
  if (n < 0) { Serial.println("kuyruk bölümü çok küçük: hazır hikâye yok"); return; }
  kuyruk_var = true;
  Serial.printf("kuyruk: %d yuva (0x%X @ 0x%X), hazır %d hikâye | hedef figür başına %d, K=%d | arka plan %s\n",
                kq.n_yuva, (unsigned)part->size, (unsigned)part->address, n, KUYRUK_FIGUR_BASI, KUYRUK_K,
                arka_acik ? "açık" : "kapalı");
}

static void kuyruk_durum() {
  if (!kuyruk_var) { Serial.println("kuyruk yok (bölüm ya da model yok)"); return; }
  Serial.printf("kuyruk: hazır %d / %d yuva (hedef figür başına %d, K=%d) | arka plan %s | bu açılışta %d yazıldı\n",
                kuyruk_say(&kq, -1, -1), kq.n_yuva, KUYRUK_FIGUR_BASI, KUYRUK_K, arka_acik ? "açık" : "kapalı",
                arka_yazilan);
  for (int f = 0; f < N_FIGUR; f++) {
    Serial.printf("  %2d %-14s %d:", f + 1, FIGUR_AD[f], kuyruk_say(&kq, f, -1));
    for (int j = 0; j < FIGUR_YER_N[f]; j++) {
      int n = kuyruk_say(&kq, f, j);
      if (n) Serial.printf(" %s %d", YER_AD[FIGUR_YER[f * YER_MAKS + j]], n);
    }
    Serial.println();
  }
}

// ---- arka plan üretimi: boşta, kuyruktaki eksik (figür, yer) için K aday + seçici, en iyisi flash'a ----
// İş aday aday ilerler: düğmeye basılır ya da seri porta bir şey gelirse o aday bırakılır (biten adaylar ve en
// iyisi RAM'de kalır), çocuk hikâyesini dinledikten sonra iş kaldığı adaydan sürer.
static struct {
  bool aktif;
  int f, j, K, sonraki, toplam, en_n, en_plan;
  double en_p;
  int64_t us;
} arka;
static int16_t arka_tok[N_URET];

static bool arka_kes() { return durdur_istendi(); }

// Döner: bir aday üretildi (ya da yarıda kesildi); false: yapılacak iş yok
static bool arka_adim() {
  if (!llm_var || !kuyruk_var || !arka_acik) return false;
  if (!arka.aktif) {
    int f, j;
    if (!kuyruk_sonraki(&kq, KUYRUK_FIGUR_BASI, N_FIGUR, FIGUR_YER_N, &f, &j)) return false;
    arka.aktif = true; arka.f = f; arka.j = j; arka.K = KUYRUK_K; arka.sonraki = 0; arka.toplam = 0;
    arka.en_p = -1e30; arka.en_n = arka.en_plan = 0; arka.us = 0;
    Serial.printf("[kuyruk] %s | %s: %d aday üretiliyor (düğme ya da seri komut keser)\n", FIGUR_AD[f],
                  YER_AD[FIGUR_YER[f * YER_MAKS + j]], arka.K);
  }
  led(LED_ARKA);
  int64_t t0 = esp_timer_get_time();
  uretim_kes = arka_kes;
  ADAY_BASI(arka.sonraki);
  Aday a = aday_uret(arka.f, arka.j, false);
  uretim_kes = NULL;
  led(LED_KAPALI);
  if (a.iptal) return true;  // kullanıcı geldi: bu aday sonra baştan
  arka.us += esp_timer_get_time() - t0;
  double p = puanla(a, arka.f, arka.j);
  ADAY_SONU(arka.sonraki, a, p);
  arka.toplam += a.n + (a.bitti ? 1 : 0);
  if (p > arka.en_p) {
    arka.en_p = p; arka.en_n = a.n; arka.en_plan = a.n_plan;
    memcpy(arka_tok, aday_tok, a.n * sizeof(int16_t));
  }
  arka.sonraki++;
  if (arka.sonraki < arka.K) return true;
  arka.aktif = false;
  const char *fa = FIGUR_AD[arka.f], *ya = YER_AD[FIGUR_YER[arka.f * YER_MAKS + arka.j]];
  if (arka.en_p <= -99) { Serial.printf("[kuyruk] %s | %s: bütün adayların planı bozuk, yeniden denenecek\n", fa, ya); return true; }
  int y = kuyruk_yaz(&kq, arka.f, arka.j, arka.K, (float)arka.en_p, arka_tok, arka.en_n, arka.en_plan);
  KUYRUK_YAZILDI(y, arka.f, arka.j, arka.K, (float)arka.en_p, arka_tok, arka.en_n, arka.en_plan);
  if (y < 0) {
    Serial.println("[kuyruk] HATA: flash'a yazılamadı; arka plan üretimi kapatıldı");
    arka_acik = false;
    return true;
  }
  arka_yazilan++;
  float sn = arka.us / 1e6f;
  Serial.printf("[kuyruk] %s | %s: %d aday, puan %.2f -> yuva %d | hazır: %s %d, toplam %d (%.0f s, %.2f token/s)\n",
                fa, ya, arka.K, arka.en_p, y, fa, kuyruk_say(&kq, arka.f, -1), kuyruk_say(&kq, -1, -1), sn,
                sn > 0 ? arka.toplam / sn : 0.f);
  return true;
}

// Bilgisayardaki deneme (tools/kart_pc "#bosta") için: arka planda yapılacak iş kaldı mı
static bool arka_is_var() {
  int f, j;
  return llm_var && kuyruk_var && arka_acik && (arka.aktif || kuyruk_sonraki(&kq, KUYRUK_FIGUR_BASI, N_FIGUR, FIGUR_YER_N, &f, &j));
}

// ---- hikâye isteği: hazır varsa hemen, yoksa yarım kalmış arka plan işinin en iyisi, o da yoksa canlı (K=1) ----
static bool hazir_oku(int f, int j, const char *kaynak) {
  Serial.printf("\n=== %s | %s | %s ===\n", FIGUR_AD[f], YER_AD[FIGUR_YER[f * YER_MAKS + j]], kaynak);
  HAZIR_CALINDI(f, j, son_tok, son_n);
  Serial.print("Sorun:");
  for (int i = 0; i < son_n; i++) yaz(son_tok[i]);
  Serial.println("\n");
  bool tamam = true;
  if (ses_var && ses_oku && son_n > son_plan) tamam = hikaye_oku(son_tok + son_plan, son_n - son_plan);
  if (!tamam) oynat_olayini_yut();
  return tamam;
}

// j < 0: figürün herhangi bir yeri (sürpriz)
static void hikaye_anlat(int f, int j) {
  char kaynak[96];
  for (int y; kuyruk_var && (y = kuyruk_bul(&kq, f, j)) >= 0;) {
    KuyrukBaslik b;
    int n = kuyruk_oku(&kq, y, &b, son_tok, N_URET);
    if (n <= 0) { Serial.printf("kuyruk: yuva %d bozuk, atlandı\n", y); continue; }
    kuyruk_tuket(&kq, y);
    son_n = n; son_plan = b.n_plan; son_f = f; son_j = b.yer;
    snprintf(kaynak, sizeof kaynak, "hazır hikâye (%d aday, puan %.2f; %s için %d hazır kaldı)", b.K, b.puan,
             FIGUR_AD[f], kuyruk_say(&kq, f, -1));
    hazir_oku(f, b.yer, kaynak);
    return;
  }
  if (arka.aktif && arka.f == f && (j < 0 || arka.j == j) && arka.sonraki > 0 && arka.en_p > -99) {
    son_hikaye_sakla(arka_tok, arka.en_n, arka.en_plan, f, arka.j);
    snprintf(kaynak, sizeof kaynak, "yarım kuyruk işinden (%d/%d aday, puan %.2f)", arka.sonraki, arka.K, arka.en_p);
    arka.aktif = false;  // bu (figür, yer) için iş baştan
    hazir_oku(f, son_j, kaynak);
    return;
  }
  if (!llm_var) { Serial.println("LLM modeli yok: hikâye üretilemiyor."); led_yanip(LED_HATA, 3); bip(220, 300); return; }
  hikaye(f, j >= 0 ? j : (int)(esp_random() % FIGUR_YER_N[f]), 1);
}

static void son_hikayeyi_oku() {
  if (son_n <= 0) { Serial.println("henüz okunmuş hikâye yok"); bip(330, 150); return; }
  hazir_oku(son_f, son_j, "son hikâye, yeniden");
}

// ---- ayarlar (NVS, Preferences): ses seviyesi, seçili figür/yer, arka plan; boşta yazılır ----
static Preferences ayar;
static bool ayar_acik = false, ayar_kirli = false;
static uint32_t son_etkinlik_ms = 0;          // son düğme / seri komut / NFC

static void ayar_yukle() {
  ayar_acik = ayar.begin("hikaye", false);
  if (!ayar_acik) return;
  ses_seviye = ayar.getUChar("ses", SES_SEVIYE_VARSAYILAN);
  secili_f = ayar.getUChar("figur", 0);
  secili_j = ayar.getChar("yer", -1);
  arka_acik = ayar.getBool("arka", true);
  if (ses_seviye < 0 || ses_seviye >= SES_SEVIYE_N) ses_seviye = SES_SEVIYE_VARSAYILAN;
  if (secili_f < 0 || secili_f >= N_FIGUR) secili_f = 0;
  if (secili_j < -1 || secili_j >= FIGUR_YER_N[secili_f]) secili_j = -1;
}
static void ayar_kaydet() {  // konuşma ya da üretim sırasında flash'a yazılmasın: boşta, 2 s sonra
  if (!ayar_acik || !ayar_kirli || millis() - son_etkinlik_ms < 2000) return;
  ayar.putUChar("ses", (uint8_t)ses_seviye);
  ayar.putUChar("figur", (uint8_t)secili_f);
  ayar.putChar("yer", (int8_t)secili_j);
  ayar.putBool("arka", arka_acik);
  ayar_kirli = false;
}

static const char *secili_yer_ad() { return secili_j < 0 ? "sürpriz yer" : YER_AD[FIGUR_YER[secili_f * YER_MAKS + secili_j]]; }

static void ses_seviye_ayarla(int v) {
  ses_seviye = v < 0 ? 0 : v >= SES_SEVIYE_N ? SES_SEVIYE_N - 1 : v;
  ayar_kirli = true;
  Serial.printf("ses seviyesi %d/%d (kazanç %.2f)\n", ses_seviye, SES_SEVIYE_N - 1, SES_KAZANC[ses_seviye] / 256.0);
  bip(660, 120);
}

// ---- düğme / NFC olayları ----
static void olay_isle(const Olay &o) {
  Serial.printf("(düğme: %s)\n", OLAY_AD[o.tur]);
  switch (o.tur) {
    case OLAY_FIGUR:
    case OLAY_FIGUR_UZUN:
    case OLAY_NFC:
      secili_f = o.tur == OLAY_NFC ? o.deger : (secili_f + (o.tur == OLAY_FIGUR ? 1 : N_FIGUR - 1)) % N_FIGUR;
      secili_j = -1;
      ayar_kirli = true;
      Serial.printf("figür: %d %s (%d hazır hikâye)\n", secili_f + 1, FIGUR_AD[secili_f],
                    kuyruk_var ? kuyruk_say(&kq, secili_f, -1) : 0);
      duyur(FIGUR_AD[secili_f]);
      if (o.tur == OLAY_NFC && NFC_OYNAT && !olay_var()) hikaye_anlat(secili_f, -1);
      break;
    case OLAY_YER:
    case OLAY_YER_UZUN:
      secili_j = o.tur == OLAY_YER_UZUN || secili_j + 1 >= FIGUR_YER_N[secili_f] ? -1 : secili_j + 1;
      ayar_kirli = true;
      Serial.printf("yer: %s (%s)\n", secili_yer_ad(), FIGUR_AD[secili_f]);
      duyur(secili_yer_ad());
      break;
    case OLAY_OYNAT: hikaye_anlat(secili_f, secili_j); break;
    case OLAY_OYNAT_UZUN: son_hikayeyi_oku(); break;
    case OLAY_SES_ARTI: ses_seviye_ayarla(ses_seviye + 1); break;
    case OLAY_SES_EKSI: ses_seviye_ayarla(ses_seviye - 1); break;
    case OLAY_ARKA:
      arka_acik = !arka_acik;
      ayar_kirli = true;
      Serial.printf("arka plan üretimi: %s\n", arka_acik ? "açık" : "kapalı");
      led_yanip(arka_acik ? LED_ARKA : LED_HATA, 2);
      bip(arka_acik ? 880 : 440, 150);
      break;
  }
}

// ---- güç: hafif uyku ----
static int uyku_sayisi = 0;
static int64_t uyku_us = 0;

// USB CDC'de bilgisayar portu açıkken uyunmaz (hafif uykuda USB bağlantısı kopar)
static bool seri_bagli() {
#if ARDUINO_USB_CDC_ON_BOOT
  return (bool)Serial;
#else
  return false;
#endif
}

// Hafif uyku: CPU durur, PSRAM ve RAM korunur (model yeniden yüklenmez). Düğme (LOW) ya da süre uyandırır; UART
// girişinde (CDC kapalıyken) seri porttan gelen ilk karakterler uyandırır ama kaybolur.
static void hafif_uyku(uint32_t ms) {
  led(LED_KAPALI);
  amp(false);
  Serial.flush();
  esp_sleep_enable_timer_wakeup((uint64_t)ms * 1000);
  for (int i = 0; i < DUGME_N; i++)
    if (DUGME_PIN[i] >= 0) gpio_wakeup_enable((gpio_num_t)DUGME_PIN[i], GPIO_INTR_LOW_LEVEL);
  esp_sleep_enable_gpio_wakeup();
#if !ARDUINO_USB_CDC_ON_BOOT
  uart_set_wakeup_threshold(UART_NUM_0, 3);
  esp_sleep_enable_uart_wakeup(UART_NUM_0);
#endif
  int64_t t0 = esp_timer_get_time();
  esp_light_sleep_start();
  uyku_us += esp_timer_get_time() - t0;
  uyku_sayisi++;
  for (int i = 0; i < DUGME_N; i++)
    if (DUGME_PIN[i] >= 0) gpio_wakeup_disable((gpio_num_t)DUGME_PIN[i]);
}

// Boşta: üretecek iş yoksa ve UYKU_BEKLE_MS geçtiyse uyu, yoksa kısa bekle
static void bosta_bekle() {
  if (UYKU_ACIK && millis() - son_etkinlik_ms >= UYKU_BEKLE_MS && !dugme_basili(&dg) && !seri_bagli() &&
      !Serial.available())
    hafif_uyku(UYKU_DILIM_MS);
  else
    delay(20);
}

// ---- seri komutlar ----
static void seri_komut(String g) {
  if (g == "?") { liste(); return; }
  if (g == "o" || g == "O") {
    if (!ses_var) { Serial.println("konuşma kapalı (ses bölümü ya da ses.bin yok)"); return; }
    ses_oku = !ses_oku;
    Serial.printf("hikâyeyi okuma: %s\n", ses_oku ? "açık" : "kapalı");
    return;
  }
  if (g.startsWith("s ") || g.startsWith("S ")) { konus(g.c_str() + 2); return; }
  if (g == "v" || g.startsWith("v+") || g.startsWith("v-") || g.startsWith("v ")) {
    const char *p = g.c_str() + 1;
    if (*p == '+') ses_seviye_ayarla(ses_seviye + 1);
    else if (*p == '-') ses_seviye_ayarla(ses_seviye - 1);
    else if (*p == ' ') ses_seviye_ayarla(atoi(p + 1));
    else Serial.printf("ses seviyesi %d/%d\n", ses_seviye, SES_SEVIYE_N - 1);
    return;
  }
  if (g.startsWith("t ") && g.length() >= 3) {  // düğme taklidi
    static const char HARF[] = "fFyYoO+-a";
    static const uint8_t TUR[] = {OLAY_FIGUR, OLAY_FIGUR_UZUN, OLAY_YER, OLAY_YER_UZUN, OLAY_OYNAT, OLAY_OYNAT_UZUN,
                                  OLAY_SES_ARTI, OLAY_SES_EKSI, OLAY_ARKA};
    const char *h = strchr(HARF, g.c_str()[2]);
    if (!h || !*h) { Serial.println("t f|F|y|Y|o|O|+|-|a (küçük: kısa, büyük: uzun basış)"); return; }
    halka_ekle(&ana_halka, TUR[h - HARF], 0);
    return;
  }
  if (g.startsWith("n ")) {  // NFC etiketi taklidi: "n 04A1B2C3"
    uint8_t u[10];
    int n = 0;
    for (const char *p = g.c_str() + 2; n < 10 && p[0] && p[1];) {
      if (*p == ' ' || *p == ':') { p++; continue; }
      unsigned v;
      if (sscanf(p, "%2x", &v) != 1) break;
      u[n++] = (uint8_t)v;
      p += 2;
    }
    if (n) nfc_etiket(u, n);
    else Serial.println("örnek: n 04A1B2C3");
    return;
  }
  if (g == "u") {
    Serial.println("10 s hafif uyku (düğme uyandırır)...");
    int64_t t0 = esp_timer_get_time();
    hafif_uyku(10000);
    Serial.printf("uyandı: %.1f s (sebep %d)\n", (esp_timer_get_time() - t0) / 1e6, (int)esp_sleep_get_wakeup_cause());
    return;
  }
  if (g == "k") { kuyruk_durum(); return; }
  if (g == "k+" || g == "k-") {
    arka_acik = g == "k+";
    ayar_kirli = true;
    Serial.printf("arka plan üretimi: %s\n", arka_acik ? "açık" : "kapalı");
    return;
  }
  if (g == "k sil") {
    if (!kuyruk_var) { Serial.println("kuyruk yok"); return; }
    arka.aktif = false;
    Serial.printf("kuyruk: %d hazır hikâye silindi (boşta yeniden üretilir)\n", kuyruk_temizle(&kq));
    return;
  }
  if (!llm_var) { Serial.println("LLM modeli yok: yalnız \"s <metin>\" çalışır."); return; }
  if (g == "b" || g == "B") { hiz_testi(); return; }
  if (g == "r" || g == "R") { hikaye_anlat((int)(esp_random() % N_FIGUR), -1); return; }
  int a = -1, y = -1, k = 1;
  int n = sscanf(g.c_str(), "%d %d %d", &a, &y, &k);
  int f = a - 1, j = n >= 2 ? y - 1 : -1;
  if (n < 1 || f < 0 || f >= N_FIGUR || (n >= 2 && (j < 0 || j >= FIGUR_YER_N[f]))) {
    Serial.println("Anlaşılmadı. Örnek: \"8 4\" (figür no, o figürün yer no) ya da \"8 4 8\" (8 aday). \"?\" liste.");
    return;
  }
  if (n >= 3) hikaye(f, j, k < 1 ? 1 : k > 16 ? 16 : k);  // aday sayısı verildi: her zaman üret (test)
  else hikaye_anlat(f, j);                               // hazır varsa hemen
}

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n=== Hikâye Oyuncağı ===");
  bekci_kur();
  esp_reset_reason_t neden = esp_reset_reason();
  ayar_yukle();
  if (neden == ESP_RST_BROWNOUT) {
    Serial.println("UYARI: güç düşmesiyle (brownout) yeniden başladı: güç kaynağı/kablo zayıf ya da hoparlör çok "
                   "akım çekiyor (README \"Güç\"). Bu açılışta ses kısıldı.");
    if (ses_seviye > 4) ses_seviye = 4;
  } else if (neden == ESP_RST_TASK_WDT || neden == ESP_RST_INT_WDT || neden == ESP_RST_WDT || neden == ESP_RST_PANIC) {
    Serial.printf("UYARI: önceki çalışma hatayla bitti (yeniden başlama sebebi %d); bu satırı bana gönderin\n", (int)neden);
  }
  for (int i = 0; i < DUGME_N; i++)
    if (DUGME_PIN[i] >= 0) pinMode(DUGME_PIN[i], INPUT_PULLUP);
#if AMP_SD_PIN >= 0
  pinMode(AMP_SD_PIN, OUTPUT);
  digitalWrite(AMP_SD_PIN, LOW);
#endif
#if DURUM_LED_PIN >= 0
  pinMode(DURUM_LED_PIN, OUTPUT);
#endif
  main_h = xTaskGetCurrentTaskHandle();
  iki_cekirdek = xTaskCreatePinnedToCore(worker_main, "mv", 4096, NULL, 2, &worker_h, 0) == pdPASS;
  llm_var = llm_kur();
  ses_kur();  // LLM'den sonra: LLM'in PSRAM yerleşimi (head kopyası) eskisi gibi kalsın, ses kalanı kullanır
  if (ses_var)
    Serial.printf("boş (ses sonrası): SRAM %.0f KB | PSRAM %.2f MB\n", heap_caps_get_free_size(MALLOC_CAP_INTERNAL) / 1024.0,
                  heap_caps_get_free_size(MALLOC_CAP_SPIRAM) / 1048576.0);
  kuyruk_hazirla();
  nfc_var = nfc_kur();
  dugme_gorevi_var = xTaskCreatePinnedToCore(dugme_gorevi, "dugme", 3072, NULL, 3, NULL, 1) == pdPASS;
  Serial.printf("düğmeler: FİGÜR %d, YER %d, OYNAT %d | NFC: %s | uyku: %s | ses seviyesi %d/%d | bekçi %d s%s\n",
                DUGME_FIGUR_PIN, DUGME_YER_PIN, DUGME_OYNAT_PIN,
                nfc_var ? "var" : NFC_OKUYUCU ? "okuyucu bulunamadı" : "yok (\"n <uid>\" ile denenir)",
                UYKU_ACIK ? "açık" : "kapalı", ses_seviye, SES_SEVIYE_N - 1, BEKCI_SN, bekci_var ? "" : " (kurulamadı)");
  Serial.printf("seçili: %s, %s\n", FIGUR_AD[secili_f], secili_yer_ad());
  liste();
  if (!llm_var) led_yanip(LED_HATA, 3);
  son_etkinlik_ms = millis();
}

void loop() {
  bekci_besle();
  olaylari_topla();
  if (Serial.available()) {
    String g = Serial.readStringUntil('\n');
    g.trim();
    if (g.length()) seri_komut(g);
    son_etkinlik_ms = millis();
    return;
  }
  Olay o;
  if (olay_al_(&o)) {
    led(LED_TAMAM);
    olay_isle(o);
    led(LED_KAPALI);
    son_etkinlik_ms = millis();
    return;
  }
  if (millis() - son_etkinlik_ms >= ARKA_BEKLE_MS && arka_adim()) return;
  ayar_kaydet();
  bosta_bekle();
}
