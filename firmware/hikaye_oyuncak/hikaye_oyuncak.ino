// Hikâye Oyuncağı (ESP32-S3 N16R8): ürün yazılımı + seri monitör test komutları.
//
// Model: c3ft_karma (C3: d192 L12 F512 P56, V16384; model.bin 10 331 252 B), flash'taki "model" bölümünde
// (0x1D0000). Figürler data/urun_kartlari.json'daki 11 ürün figürü ve kart yerleri; üretim bilgisayardaki
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
// Ürün: kuyruğa önceden hazırlanan hikâyede K=5 (KUYRUK_K); hazır yoksa canlı okuma (yazdıkça okur, seçici yok).
// Kart her hikâyeden sonra token/s ve süreyi yazar.
//
// Ses (ses.h): flash'taki "ses" bölümünde ses.bin varsa hikâye kartta seslendirilir; MAX98357A'ya I2S (BCLK 4,
// LRC 5, DIN 6; 16 kHz, 16 bit, mono -> iki kanala aynı örnek). Konuşurken kart üstündeki RGB LED yeşil.
// "s <metin>" = metni oku | "o" = üretilen hikâyeyi otomatik okuma aç/kapa (ses modeli varsa açık başlar).
// Bölüm ya da ses.bin yoksa her şey eskisi gibi çalışır, konuşma kapalıdır (düğmelere bip ile yanıt verilir).
//
// Ürün (docs/URUN_TANIMI.md; README "6. Oyuncak olarak"): düğme yok. Pinler ve sabitler donanim.h'de.
// - Stand (NFC, nfc.h; RC522): hikâye yalnız standdaki oyuncağın hikâyesidir. Oyuncak etiketi kayıtlıdır (etiket.h:
//   sihir + sürüm + nfc_no + CRC, NTAG sayfa 4-5); kayıt yoksa UID tablosu. İlk kez konan oyuncak "tanınır" (NVS).
//   Kondu -> halka figür renginde dolar -> selamlama ("Merhaba Emre, şimdi sana Niloya'nın hikâyesini okuyacağım.",
//   selam.h) -> en eski hazır hikâye; hazır yoksa canlı okuma (canli_oku: selam çalarken model yazmaya başlar, her
//   cümle biter bitmez okunur; yerler kendiliğinden döner). Çekilince cümle sonunda durur
//   (ayar). nfc_no 200 = ayar kartı: Wi-Fi erişim noktası + ayar sayfası (ayar_sayfa.h, ayarlar.h).
// - Gece figürü (Ay Dede, mod "uyku"): ninni modu: yavaş, alçak, kısık okuma (ses.h hiz/perde_kaydir/kazanc), uzun
//   cümle araları, isteğe bağlı müzik kutusu (muzik_kutusu.h), gece mavisi yıldızlı halka; uyku zamanlayıcısı dolunca
//   halka 60 sn'de söner, mikrofon/yükselteç/halka kapanır. Metin: 100 sabit ninni (yerlesik.h, ninniler.txt),
//   sırayla; model bu figürde hiç çalışmaz.
// - Sesli komut (INMP441 I2S1 -> kws.h): "Merhaba Eko" + dur / devam / başka / bir daha / sesini aç / sesini kıs.
//   Hiçbir komut figür seçmez.
// - Halka (halka.h; NeoPixel GPIO18, RMT): bütün durumlar; ayrı düşük öncelikli görev.
// - Hikâye kuyruğu (kuyruk.h, flash'ta "kuyruk" bölümü): ilk açılıştan boştayken bütün figürler için (standa konmuş
//   olanlar önce; ARKA_HEPSI) K=5 aday + seçici, en iyisi saklanır; yuvalar figürlere bölünür. Açılıştan açılışa kalır.
// - Güç: uyku modunda hafif uyku; yazılımla ses seviyesi; görev bekçisi her token'da beslenir.
// Seri komutlar (geliştirme): "8" = Elsa (standı atlar) | "8 4" | "8 4 K" = her zaman K adayla üret (test) | "k" kuyruk,
// "k+"/"k-", "k sil" | "v+"/"v-"/"v N" ses | "w dur" sesli komut taklidi | "n" stand, "n koy 3" / "n kaldir" taslak
// okuyucuda etiket | "a" ayar modu | "sahip" tanınmış oyuncaklar | "h" halka | "u" hafif uyku denemesi.

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
#include "esp_mac.h"
#include <Preferences.h>
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include "donanim.h"
#include "olaylar.h"
#if DUGME_ACIK
#include "dugmeler.h"
#endif
#include "kuyruk.h"
#include "nfc.h"
#include "halka.h"
#include "selam.h"
#include "ayarlar.h"
#include "kws.h"
#include "muzik_kutusu.h"
#include "generated/figur_donanim.h"
#include "yerlesik.h"
#include "ayar_sayfa.h"

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

// Arduino fonksiyon prototiplerini dosyanın başına ekler; Aday onlardan önce tanımlı olmalı (imzalarda yalnız
// başlıklardaki ve burada tanımlı türler).
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
  Serial.println("Ürün: oyuncağı standa koyun (taslak okuyucuda \"n koy 8\" = Elsa, \"n koy 12\" = Ay Dede, \"n kaldir\").");
  Serial.println("Geliştirme: \"8 4\" (Elsa, şato) | \"8\" (Elsa, sürpriz yer): hazır varsa hemen, yoksa canlı.");
  Serial.println("Sona aday sayısı (en çok 16) eklenirse her zaman üretilir, en iyisi seçilir: \"8 4 8\" (8 aday).");
  Serial.println("(ürün: kuyrukta önceden hazırlanan hikâye K=5; hazır yoksa canlı okuma: yazdıkça okur)");
  Serial.printf("Ses: \"s <metin>\" metni okur | \"o\" hikâyeyi okuma %s (şu an %s) | \"v+\" \"v-\" \"v N\" ses seviyesi\n",
                ses_var ? "aç/kapa" : "(ses modeli yok)", ses_var && ses_oku ? "açık" : "kapalı");
  Serial.println("Kuyruk: \"k\" durum | \"k+\" \"k-\" arka plan üretimi aç/kapa | \"k sil\" hazırları sil");
  Serial.println("Sesli komut taklidi: \"w uyandirma\" \"w dur\" \"w devam\" \"w baska\" \"w bir_daha\" \"w sesi_ac\""
                 " \"w sesi_kis\" | \"n\" stand | \"a\" ayar modu | \"sahip\" | \"h\" halka | \"u\" uyku denemesi\n");
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
static void (*govde_tok)(int tok) = NULL;  // canlı okuma: gövde token'ı üretildikçe (EOT hariç)

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
    if (govdede && govde_tok) govde_tok(tok);
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

// ---- durum: ayarlar, standdaki oyuncak, son okunan içerik, uyku ve ayar modları ----
// Donanım figürü d (generated/figur_donanim.h: etiketteki nfc_no, halka rengi, mod) -> model figürü DONANIM_MODEL[d]
// (istemler.h; -1: model bilmiyor, yerleşik metin). Tanınmış (sahip olunan) figürler sahip_maske'de (bit d).
static_assert(DONANIM_N <= 32, "sahip maskesi 32 bit");
static Ayarlar ay;
static uint32_t sahip_maske = 0;
static bool llm_var = false;
#if DUGME_ACIK
static int secili_f = 0, secili_j = -1;      // geliştirme: düğmeler
#endif
static int16_t son_tok[N_URET];              // son model hikâyesi (plan + gövde)
static int son_n = 0, son_plan = 0, son_f = -1, son_j = -1;
static int son_d = -1, son_yerlesik = -1;    // son okunan içeriğin donanım figürü; yerleşik metin no (-1: model)
static int yerlesik_sira[DONANIM_N];         // yerleşik listelerde sıradaki metin
static uint8_t canli_yer[N_FIGUR];           // canlı üretimde figürün sıradaki yeri (yerler döner)
static struct { bool var; int d, cumle; } durak;   // "Dur" ile duran okuma: figür, kaldığı cümle
// Stand: alandaki etiket (nfc_tara her NFC_YOKLA_MS'de günceller)
static struct { bool dolu; uint8_t uid[10]; int uid_n, no, d; uint32_t gordu_ms; } stand;
// Uyku (gece figürü): ninniler -> zamanlayıcı dolunca halka ve müzik 60 s'de söner -> kapalı (mikrofon, yükselteç,
// halka kapalı; stand yoklanır, yeni oyuncak konunca uyanır)
enum { UYKU_YOK, UYKU_NINNI, UYKU_SONUYOR, UYKU_KAPALI };
static const char *const UYKU_AD[4] = {"yok", "ninni", "sönüyor", "kapalı"};
static struct { int durum; uint32_t bitis_ms, sonme_ms; } uyku;
// Ayar modu (ayar kartı standda): Wi-Fi erişim noktası + ayar sayfası
enum { TANIT_YOK, TANIT_BEKLE, TANIT_SONUC };
static struct {
  bool acik, tanit_oldu, kapat_iste, tanit_tamam;
  uint32_t bas_ms, bos_ms, tanit_ms;
  int tanit, tanit_no;
  char mesaj[128];
} ayr;
static uint32_t son_etkinlik_ms = 0;          // son olay / seri komut
static bool uretim_serbest = false;          // geliştirme (seri "8 4"): standda oyuncak olmasa da üret
static bool ayar_kirli = false;

static int donanim_bul(int no) {
  for (int d = 0; d < DONANIM_N; d++)
    if (DONANIM_NFC[d] == no) return d;
  return -1;
}
static int model_donanim(int f) {  // model figürünün donanım figürü (yoksa -1)
  for (int d = 0; d < DONANIM_N; d++)
    if (DONANIM_MODEL[d] == f) return d;
  return -1;
}
// Tanınmış donanım figürlerinin model figürleri (arka plan yalnız bunlar için üretir)
static uint32_t model_maske() {
  uint32_t m = 0;
  for (int d = 0; d < DONANIM_N; d++)
    if (((sahip_maske >> d) & 1) && DONANIM_MODEL[d] >= 0) m |= 1u << DONANIM_MODEL[d];
  return m;
}

// ---- halka (NeoPixel, HALKA_PIN): halka.h durumdan kareye, RMT ile yollanır; kartta ayrı görev 30 kare/s ----
static Halka halka;
static portMUX_TYPE halka_kilit = portMUX_INITIALIZER_UNLOCKED;
static bool halka_var = false, halka_gorevi_var = false, halka_karanlik = false;
static uint8_t halka_kare[HALKA_MAKS][3];
static rmt_data_t halka_bit[HALKA_LED_SAYISI * 24];
static uint32_t halka_son_ms = 0, halka_bitti_ms = 0;
static bool acilis_bekliyor = true;           // açılış gökkuşağı bitince halka_bosta()
static volatile uint8_t konusma_seviye = 0;   // çalınan sesin yüksekliği 0..255 (okurken halka dalgalanır)
static char halka_son_durum[48];
#ifndef HALKA_DURUM_DEGISTI  // bilgisayardaki deneme: durum değişince döküm
#define HALKA_DURUM_DEGISTI(metin)
#endif

// Bir kare: hesapla (kilit altında, ~20 µs), WS2812 bitlerine çevir (GRB, 10 MHz RMT: 1 = 0,8/0,4 µs, 0 = 0,4/0,8 µs)
static void halka_tik_(uint32_t ms) {
  char d[48];
  portENTER_CRITICAL(&halka_kilit);
  halka.ses = konusma_seviye;
  halka_ciz(&halka, ms, halka_kare);
  halka_durum_metni(&halka, d, sizeof d);
  portEXIT_CRITICAL(&halka_kilit);
  halka_son_ms = ms;
  if (strcmp(d, halka_son_durum)) {
    snprintf(halka_son_durum, sizeof halka_son_durum, "%s", d);
    HALKA_DURUM_DEGISTI(d);
  }
  if (!halka_var) return;
  bool karanlik = true;
  for (int i = 0; i < HALKA_LED_SAYISI; i++) karanlik &= !(halka_kare[i][0] | halka_kare[i][1] | halka_kare[i][2]);
  if (karanlik && halka_karanlik) return;  // sönük halka bir kez yollanır (uykuda boşuna RMT yok)
  halka_karanlik = karanlik;
  for (int i = 0; i < HALKA_LED_SAYISI; i++) {
    const uint8_t grb[3] = {halka_kare[i][1], halka_kare[i][0], halka_kare[i][2]};
    for (int c = 0; c < 3; c++)
      for (int b = 0; b < 8; b++) {
        rmt_data_t *r = &halka_bit[(i * 3 + c) * 8 + b];
        bool bir = (grb[c] >> (7 - b)) & 1;
        r->level0 = 1; r->duration0 = bir ? 8 : 4;
        r->level1 = 0; r->duration1 = bir ? 4 : 8;
      }
  }
  rmtWrite(HALKA_PIN, halka_bit, HALKA_LED_SAYISI * 24, RMT_WAIT_FOR_EVER);
}
static void halka_gorevi(void *) {
  for (;;) {
    halka_tik_(millis());
    vTaskDelay(pdMS_TO_TICKS(1000 / HALKA_FPS));
  }
}
// Görev yoksa (bilgisayardaki deneme) ana döngüden
static void halka_tik() {
  if (!halka_gorevi_var && millis() - halka_son_ms >= 1000 / HALKA_FPS) halka_tik_(millis());
}
static void halka_durum(int taban) {
  acilis_bekliyor = false;  // açılış gökkuşağının yerine başka durum geldi
  portENTER_CRITICAL(&halka_kilit);
  halka_taban(&halka, taban, millis());
  portEXIT_CRITICAL(&halka_kilit);
  halka_tik();
}
static void halka_figur(int d) {
  portENTER_CRITICAL(&halka_kilit);
  halka_renk(&halka, &DONANIM_RENK[3 * d]);
  portEXIT_CRITICAL(&halka_kilit);
}
static void halka_ustte(int ust, uint32_t sure) {
  portENTER_CRITICAL(&halka_kilit);
  halka_ust(&halka, ust, millis(), sure);
  portEXIT_CRITICAL(&halka_kilit);
  halka_tik();
}
static void halka_ilerle(int pay, int payda) {
  portENTER_CRITICAL(&halka_kilit);
  halka_ilerleme(&halka, pay, payda);
  portEXIT_CRITICAL(&halka_kilit);
  halka_tik();
}
static void halka_ayarla() {  // ayardaki parlaklık ve boşta nefes
  portENTER_CRITICAL(&halka_kilit);
  halka.parlaklik = ay.parlaklik;
  halka.nefes = ay.nefes;
  portEXIT_CRITICAL(&halka_kilit);
}
static void halka_baslat() {
  halka_kur(&halka, HALKA_LED_SAYISI, HALKA_PARLAKLIK_SINIR, HALKA_AKIM_SINIR_MA);
  halka_ayarla();
  halka_var = rmtInit(HALKA_PIN, RMT_TX_MODE, RMT_MEM_NUM_BLOCKS_2, 10000000);
  if (!halka_var) Serial.println("UYARI: halka (RMT) kurulamadı");
  halka_taban(&halka, HT_ACILIS, millis());
  // düşük öncelik (loopTask ile aynı, 1. çekirdek): kare hesabı ~0,1 ms, RMT yollaması DMA'sız ama bekler (CPU boş)
  halka_gorevi_var = xTaskCreatePinnedToCore(halka_gorevi, "halka", 3072, NULL, 1, NULL, 1) == pdPASS;
}

// ---- olaylar: stand (NFC, nfc.h), sesli komut (KWS, mikrofon görevi), geliştirme düğmeleri, seri taklit ----
static OlayHalka ana_halka;         // ana döngünün kendi olayları (stand, seri "w")
static OlayHalka kws_halka;         // mikrofon görevi yazar
static bool nfc_var = false;
static uint32_t nfc_son_ms = 0;
static uint32_t dinle_bitis = 0;    // "Merhaba Eko"dan sonraki komut penceresinin sonu (0: dinlemiyor)
#ifndef SAHTE_ZAMANLI  // bilgisayardaki deneme: zamanı gelen taklit satırları
#define SAHTE_ZAMANLI()
#endif

static const char *kws_ad(int e) {
  static const char *const AD[] = {"yok", "uyandırma", "dur", "devam", "başka", "bir daha", "sesi aç", "sesi kıs"};
  return e >= 0 && e < (int)(sizeof AD / sizeof AD[0]) ? AD[e] : "?";
}

#if DUGME_ACIK
static Dugmeler dg;
static const int DUGME_PIN[DUGME_N] = {DUGME_FIGUR_PIN, DUGME_YER_PIN, DUGME_OYNAT_PIN};
static bool dugme_gorevi_var = false;
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
#endif

static void uid_yaz(const uint8_t *u, int n) {
  for (int i = 0; i < n; i++) Serial.printf("%02X", u[i]);
}

// Standı yoklar: yeni etiket konunca kaydını okuyup bir kez olay verir; etiket NFC_KALKTI_MS görünmezse kalkmıştır.
static void nfc_tara() {
  uint8_t u[10];
  int n = nfc_uid_oku(u, sizeof u);
  uint32_t simdi = millis();
  if (n <= 0) {
    if (stand.dolu && simdi - stand.gordu_ms > NFC_KALKTI_MS) {
      stand.dolu = false;
      halka_ekle(&ana_halka, OLAY_STAND_KALKTI, stand.no);
    }
    return;
  }
  stand.gordu_ms = simdi;
  if (stand.dolu && n == stand.uid_n && !memcmp(u, stand.uid, n)) return;
  if (stand.dolu) halka_ekle(&ana_halka, OLAY_STAND_KALKTI, stand.no);  // kalkışı görülmeden başka etiket
  bool kayit = false;
  int no = -1;
  for (int k = 0; k < 3 && no < 0; k++) no = nfc_etiket_no(u, n, &kayit);  // okuma bozulursa iki kez daha
  stand.dolu = true;
  memcpy(stand.uid, u, n);
  stand.uid_n = n;
  stand.no = no;
  stand.d = donanim_bul(no);
  Serial.print("(stand: etiket ");
  uid_yaz(u, n);
  if (no < 0) {
    Serial.println(")\nbilinmeyen etiket (ayar sayfasında \"oyuncak tanıt\" ile yazın ya da nfc.h NFC_TABLO'ya ekleyin)");
    halka_ekle(&ana_halka, OLAY_STAND_BILINMEYEN, 0);
    return;
  }
  Serial.printf(", nfc_no %d%s)\n", no, kayit ? "" : " UID tablosundan");
  halka_ekle(&ana_halka, OLAY_STAND_KONDU, no);
}

static void dinle_bitir(bool anlasildi);
static void olaylari_topla() {
  SAHTE_ZAMANLI();
#if DUGME_ACIK
  if (!dugme_gorevi_var) dugme_tara();
#endif
  if (nfc_var && millis() - nfc_son_ms >= NFC_YOKLA_MS) { nfc_son_ms = millis(); nfc_tara(); }
  if (dinle_bitis && (int32_t)(millis() - dinle_bitis) >= 0) dinle_bitir(false);  // komut gelmedi
  halka_tik();
}
static bool olay_bak_(Olay *o) {
  if (halka_bak(&ana_halka, o) || halka_bak(&kws_halka, o)) return true;
#if DUGME_ACIK
  if (halka_bak(&dg.h, o)) return true;
#endif
  return false;
}
static bool olay_al_(Olay *o) {
  if (halka_al(&ana_halka, o) || halka_al(&kws_halka, o)) return true;
#if DUGME_ACIK
  if (halka_al(&dg.h, o)) return true;
#endif
  return false;
}
static bool olay_var() { olaylari_topla(); return olay_bak_(NULL); }
static bool durdur_istendi() { return olay_var() || Serial.available() > 0; }

// ---- ses: metinden konuşma (ses.h), I2S0 hoparlör, ses seviyesi, müzik kutusu ----
static const int I2S_BCLK = I2S_BCLK_PIN, I2S_LRC = I2S_LRC_PIN, I2S_DIN = I2S_DIN_PIN;
// Çalma tamponu: canlı okumada CANLI_TAMPON_SN saniye (PSRAM'de yer varsa; model sonraki cümleyi yazarken önceki
// çalar), öteki okumalarda cal_sinir = 1 s doldurulur ("Dur" denince kalınan cümle çalınan cümle olsun).
static int cal_bayt = 32000, cal_sinir = 32000, cal_sinir_1sn = 32000;
static volatile uint32_t cal_alinan = 0;  // çalıcının tampondan aldığı bayt (atılanlar dahil)
static uint32_t cal_gonderilen = 0;       // pcm_yaz'ın tampona yazdığı bayt
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
static volatile int32_t cal_kazanc = 256;   // Q8; çalıcı uygular: ses aç/kıs okurken hemen duyulur
static uint16_t kisma_dinle = 256;          // "Merhaba Eko"dan sonra komut duyulsun diye konuşma kısılır
static MuzikKutusu muzik;
static volatile bool muzik_acik = false;
static volatile uint16_t muzik_seviye = 0;  // 0..256 (ninni sonunda söner)
// Okuma tarzı (donanım figürünün modu): ninni yavaş, alçak, kısık, uzun aralı
static const struct { float hiz, perde, kazanc; int ara_ms; } SES_STIL[2] = {{1.f, 0.f, 1.f, 250},
                                                                              {1.f / 0.75f, -2.f, 0.6f, 900}};
static int stil_ara_ms = 250;
static void ses_stili(int mod) {
  if (mod < 0 || mod > 1) mod = 0;
  ses.hiz = SES_STIL[mod].hiz;
  ses.perde_kaydir = SES_STIL[mod].perde;
  ses.kazanc = SES_STIL[mod].kazanc;
  stil_ara_ms = SES_STIL[mod].ara_ms;
}
static void kazanc_guncelle() { cal_kazanc = (int32_t)SES_KAZANC[ses_seviye] * kisma_dinle / 256; }

// Sıcak tamponlar (SES_ALT kare etkinlik, FFT) dahili SRAM'e, SES_SRAM_PAY bırakarak (Wi-Fi ayar modu için); gerisi
// PSRAM.
static void *ses_ayir(size_t n, int sicak) {
  void *p = NULL;
  if (sicak && heap_caps_get_free_size(MALLOC_CAP_INTERNAL) > n + SES_SRAM_PAY)
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

// MAX98357A SD ucu: konuşmazken yükselteç kapalı (boşta ~2-3 mA, hışırtı yok)
static void amp(bool acik) {
#if AMP_SD_PIN >= 0
  digitalWrite(AMP_SD_PIN, acik ? HIGH : LOW);
  if (acik) delay(5);
#else
  (void)acik;
#endif
}

// Çalma görevi: tampondan I2S'e (i2s.write DMA dolunca bekler). Kazanç burada uygulanır (anında etkili); ninni
// modunda müzik kutusu karıştırılır, konuşma yokken de (cümle aralarında) müzik sürer. Sesin yüksekliği halkaya.
static void calici(void *) {
  static int16_t buf[256];
  for (;;) {
    size_t n = xStreamBufferReceive(cal_akim, buf, sizeof buf, muzik_acik ? 0 : portMAX_DELAY);
    cal_alinan += (uint32_t)n;
    int k = cal_sustur ? 0 : (int)(n / 2);
    if (!k) {
      if (!muzik_acik) continue;
      k = 256;  // yalnız müzik: 16 ms
      memset(buf, 0, sizeof buf);
    }
    const int32_t g = cal_kazanc;
    uint32_t top = 0;
    for (int i = 0; i < k; i++) {
      int32_t v = ((int32_t)buf[i] * g) / 256;
      buf[i] = (int16_t)(v > 32767 ? 32767 : v < -32768 ? -32768 : v);
      top += (uint32_t)(v < 0 ? -v : v);
    }
    uint32_t sv = top / (uint32_t)k / 24;
    konusma_seviye = (uint8_t)(sv > 255 ? 255 : sv);
    if (muzik_acik) mk_karistir(&muzik, buf, k, (int)(muzik_seviye * (g > 256 ? 256 : g) / 256));
    i2s.write((const uint8_t *)buf, (size_t)k * 2);
  }
}

enum { KES_YOK = 0, KES_HEMEN = 1, KES_CUMLE = 2 };
static int okuma_denetle_(bool uretim);
static int okuma_denetle() { return okuma_denetle_(false); }

// Sentezin PCM'i çalma tamponuna. Okurken olaylara bakılır: "Dur", başka oyuncak, oyuncak çekildi ("hemen dur"
// ayarı) ya da seri porta bir şey gelirse konuşma hemen susar (tampondaki ses atılır).
static void pcm_yaz(void *, const int16_t *pcm, int n) {
  if (konusma_kesildi) return;
  if (konusma_kesilebilir && okuma_denetle() == KES_HEMEN) { konusma_kesildi = true; cal_sustur = true; return; }
#ifndef ESP_PLATFORM
  if (n > 0) {  // bilgisayarda çalıcı çalışmaz: halka için yükseklik burada
    uint32_t top = 0;
    for (int i = 0; i < n; i++) top += (uint32_t)(pcm[i] < 0 ? -pcm[i] : pcm[i]);
    uint32_t sv = top / (uint32_t)n / 24;
    konusma_seviye = (uint8_t)(sv > 255 ? 255 : sv);
  }
#endif
  int64_t t0 = esp_timer_get_time();
  const uint8_t *p = (const uint8_t *)pcm;
  size_t kalan = (size_t)n * 2;
  while (kalan) {
    size_t dolu = xStreamBufferBytesAvailable(cal_akim), bos = dolu < (size_t)cal_sinir ? cal_sinir - dolu : 0;
    if (!bos) { delay(5); continue; }  // sınır kadar dolu: çalınmayı bekle
    size_t y = xStreamBufferSend(cal_akim, p, kalan < bos ? kalan : bos, portMAX_DELAY);
    p += y; kalan -= y; cal_gonderilen += (uint32_t)y;
  }
  cal_bekleme_us += esp_timer_get_time() - t0;
  bekci_besle();
}

// Tampon boşalsın, DMA'da kalan (6 x 240 örnek = 90 ms) çalınsın
static void cal_bitir() {
  while (!xStreamBufferIsEmpty(cal_akim)) delay(10);
  delay(120);
  cal_sustur = false;
}

// Ses modeli yokken okuma süresi taklidi (bilgisayardaki deneme: SESSIZ_MS_HARF); arada olaylara bakılır
static void sessiz_bekle(int ms) {
  while (ms > 0 && !konusma_kesildi) {
    int k = ms < 100 ? ms : 100;
    delay(k);
    ms -= k;
    konusma_seviye = (uint8_t)(100 + (ms / 100 % 3) * 60);
    if (konusma_kesilebilir && okuma_denetle() == KES_HEMEN) konusma_kesildi = true;
  }
}

// Metni cümle cümle okur (ses.h ses_cumle_sonu ile bölünür; ilk cümle hesaplanırken çalmaya başlar). bas: başlanan
// cümle (duraklatılan okuma kaldığı yerden), ilerleme: halka okunan cümle oranını gösterir, ara_ms: cümle arası.
// Olaylar okuma_denetle'de: hemen kesme (cümle ortasında) ya da cümle sonunda durma. Döner: kesildiği cümle (bu cümle
// baştan okunur); hepsi okunduysa cümle sayısı (okuma_n).
#define CUMLE_MAKS 64
static int okuma_n = 0;
static bool okuma_ortada = false;  // son okuma cümle ortasında kesildi
static int metin_oku(const char *metin, int bas, bool ilerleme, int ara_ms) {
  static const char *cb[CUMLE_MAKS], *ce[CUMLE_MAKS];
  int n = 0;
  for (const char *p = metin; *p;) {
    const char *s = ses_cumle_sonu(p);
    if (ses_harfli(p, s)) {
      if (n == CUMLE_MAKS) { ce[n - 1] = s; }  // sığmayan cümleler sonuncuya eklenir
      else { cb[n] = p; ce[n] = s; n++; }
    }
    p = s;
  }
  okuma_n = n;
  if (bas >= n) return n;
  const bool sesli = ses_var && ses_oku;
  if (!hoparlor_var && !(SESSIZ_MS_HARF > 0)) {  // hoparlör yok: yalnız seri porta
    if (ilerleme) halka_ilerle(n, n);
    return n;
  }
  amp(true);
  cal_bekleme_us = 0;
  konusma_kesildi = false;
  konusma_kesilebilir = true;
  cal_sustur = false;
  int64_t t0 = esp_timer_get_time();
  long ornek = 0;
  int i = bas;
  for (; i < n; i++) {
    if (ilerleme) halka_ilerle(i, n);
    if (i > bas && ara_ms > 0) {
      if (sesli) ses_sessizlik(&ses, ara_ms, pcm_yaz, NULL);
      else if (SESSIZ_MS_HARF > 0) sessiz_bekle(ara_ms);
    }
    if (konusma_kesildi || okuma_denetle() != KES_YOK) break;
    if (sesli) {
      long r = ses_cumle_n(&ses, cb[i], (size_t)(ce[i] - cb[i]), pcm_yaz, NULL);
      if (r < 0) { Serial.printf("ses hatası: %s\n", ses_hata); break; }
      ornek += r;
    } else if (SESSIZ_MS_HARF > 0) {
      sessiz_bekle((int)(ce[i] - cb[i]) * SESSIZ_MS_HARF);
    }
    if (konusma_kesildi) break;
  }
  if (ilerleme && i >= n) halka_ilerle(n, n);
  bool kesildi = konusma_kesildi;
  okuma_ortada = kesildi && i < n;
  konusma_kesilebilir = false;
  if (sesli && !kesildi) ses_sessizlik(&ses, 150, pcm_yaz, NULL);  // DMA'da kalan son parça sussun
  cal_bitir();
  konusma_kesildi = false;
  konusma_seviye = 0;
  if (!muzik_acik) amp(false);
  if (sesli && ornek > 0) {
    float hesap = (esp_timer_get_time() - t0 - cal_bekleme_us) / 1e6f, sure = ornek / (float)ses.sr;
    Serial.printf("[ses: %.1f s konuşma, %.1f s hesap = %.2f s hesap / s ses%s]\n", sure, hesap,
                  sure > 0 ? hesap / sure : 0.f, i < n ? "; durduruldu" : "");
  }
  return i;
}
static bool konus(const char *metin) {
  Serial.printf("[%s]\n", metin);
  return metin_oku(metin, 0, false, 250) >= okuma_n;
}

// Kısa ton (ses modeli olmasa da hoparlör varsa): ses seviyesi onayı. Kesilmez.
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
  if (!muzik_acik) amp(false);
}

// I2S0, çalma tamponu ve çalma görevi (ses.bin olmasa da: bip)
static void hoparlor_kur(int sr) {
  cal_sinir_1sn = cal_sinir = sr * 2;
  uint8_t *depo = NULL;
  size_t buyuk = (size_t)sr * 2 * CANLI_TAMPON_SN, pay = 256 * 1024;  // LLM ve ses kurulduktan sonra: kalan PSRAM
  if (heap_caps_get_free_size(MALLOC_CAP_SPIRAM) > buyuk + pay && (depo = (uint8_t *)ps(buyuk + 1))) cal_bayt = (int)buyuk;
  if (!depo) { cal_bayt = cal_sinir; depo = (uint8_t *)ps(cal_bayt + 1); }
  if (!depo) depo = (uint8_t *)heap_caps_malloc(cal_bayt + 1, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
  if (!depo) { Serial.println("ses: çalma tamponu ayrılamadı: konuşma kapalı"); return; }
  cal_akim = xStreamBufferCreateStatic(cal_bayt, 1, depo, &cal_yapi);
  Serial.printf("ses: çalma tamponu %.1f s%s\n", cal_bayt / (2.f * sr),
                cal_bayt > cal_sinir ? " (canlı okuma: yazarken okur)" : " (PSRAM az: canlı okumada cümle araları uzar)");
  i2s.setPins(I2S_BCLK, I2S_LRC, I2S_DIN);
  if (!i2s.begin(I2S_MODE_STD, sr, I2S_DATA_BIT_WIDTH_16BIT, I2S_SLOT_MODE_MONO, I2S_STD_SLOT_BOTH)) {
    Serial.println("ses: I2S başlatılamadı: konuşma kapalı"); return;
  }
  if (xTaskCreatePinnedToCore(calici, "cal", 4096, NULL, 5, NULL, 0) != pdPASS) {
    Serial.println("ses: çalma görevi kurulamadı: konuşma kapalı"); return;
  }
  hoparlor_var = true;
  mk_kur(&muzik);
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
  kazanc_guncelle();
  if (ses_var)
    Serial.printf("ses: akustik d=%d (%d+%d+%d blok), vocoder d=%d (%d blok) | bellek %.0f KB PSRAM + %.0f KB SRAM | "
                  "I2S0 BCLK %d LRC %d DIN %d SD %d\n",
                  ses.ad, ses.n_kod, ses.n_tah, ses.n_coz, ses.vd, ses.n_vblok, ses.bellek_buyuk / 1024.0,
                  ses.bellek_sicak / 1024.0, I2S_BCLK, I2S_LRC, I2S_DIN, AMP_SD_PIN);
  else if (hoparlor_var)
    Serial.printf("hoparlör: açık, yalnız bip (I2S0 BCLK %d LRC %d DIN %d); hikâyeler seri porta yazılır\n",
                  I2S_BCLK, I2S_LRC, I2S_DIN);
}

// ---- mikrofon (INMP441, I2S1) ve sesli komut (kws.h) ----
#if MIK_ACIK
static I2SClass mik;
static bool kws_var = false;
#endif
static volatile bool mik_iste = false, mik_acik = false;
#if MIK_ACIK
// Mikrofon görevi: I2S1'den 32 bitlik örnekleri okur, 16 bite indirir (DC atılır), kws_isle'ye verir; olayları
// kws_halka'ya yazar. Açma/kapama yalnız bu görevde (mik_iste): uyku modunda saat durur, INMP441 uyur.
static void mik_gorevi(void *) {
  static int32_t ham[320];
  static int16_t pcm[320];
  int32_t dc = 0;  // Q8
  for (;;) {
    if (mik_iste != mik_acik) {
      if (mik_iste) {
        mik.setPins(MIK_SCK_PIN, MIK_WS_PIN, -1, MIK_SD_PIN);
        mik_acik = mik.begin(I2S_MODE_STD, 16000, I2S_DATA_BIT_WIDTH_32BIT, I2S_SLOT_MODE_MONO, I2S_STD_SLOT_LEFT);
        if (!mik_acik) mik_iste = false;
        kws_sifirla();
      } else {
        mik.end();
        mik_acik = false;
      }
    }
    if (!mik_acik) { vTaskDelay(pdMS_TO_TICKS(50)); continue; }
    size_t b = mik.readBytes((char *)ham, sizeof ham);
    int n = (int)(b / 4);
    for (int i = 0; i < n; i++) {
      int32_t v = ham[i] >> MIK_KAYDIRMA;
      dc += (v * 256 - dc) / 1024;
      v -= dc / 256;
      pcm[i] = (int16_t)(v > 32767 ? 32767 : v < -32768 ? -32768 : v);
    }
    for (int e = kws_isle(pcm, n); e != KWS_YOK; e = kws_isle(pcm, 0)) halka_ekle(&kws_halka, OLAY_SESLI, e);
  }
}
#endif

// ---- hikâye üretimi (LLM) ----
static void son_hikaye_sakla(const int16_t *t, int n, int n_plan, int f, int j) {
  memcpy(son_tok, t, n * sizeof(int16_t));
  son_n = n; son_plan = n_plan; son_f = f; son_j = j;
  son_yerlesik = -1;
}

static bool canli_kes() { return okuma_denetle_(true) != KES_YOK; }  // canlı üretim: oyuncak kalktı, komut ...

// f model figürü, j figürün kart yeri (0'dan), K aday: urun_uret.main'in bir vakası (en yüksek puanlı aday; eşitlikte
// ilki). Standdan oyuncak kalkar ya da komut gelirse yarıda kesilir. Döner: hikâye üretildi (son_* doldu).
static bool hikaye(int f, int j, int K) {
  Serial.printf("\n=== %s | %s | %d aday ===\n", FIGUR_AD[f], YER_AD[FIGUR_YER[f * YER_MAKS + j]], K);
  int64_t t0 = esp_timer_get_time();
  llm_profile_reset(&s); ornek_us = 0;
  int toplam = 0, en_n = 0, en_plan = 0; double en_p = -1e30;
  bool kesildi = false;
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
  if (kesildi) {
    Serial.println("\n(durduruldu)");
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
// Arka planın yazdığı model figürleri: ARKA_HEPSI ise ilk açılıştan bütün figürler (tanınmışlar önce), değilse yalnız
// tanınmışlar. Figür başına hedef hazır hikâye: yuvalar bu figürlere bölünür.
static uint32_t arka_maske() { return ARKA_HEPSI ? (N_FIGUR >= 32 ? 0xFFFFFFFFu : (1u << N_FIGUR) - 1) : model_maske(); }
static int arka_hedef() { return kuyruk_hedef(&kq, arka_maske(), N_FIGUR, KUYRUK_FIGUR_MAKS, KUYRUK_PAY); }

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
  Serial.printf("kuyruk: %d yuva (0x%X @ 0x%X), hazır %d hikâye | figür başına %d (en çok %d), K=%d | "
                "arka plan %s\n", kq.n_yuva, (unsigned)part->size, (unsigned)part->address, n, arka_hedef(),
                KUYRUK_FIGUR_MAKS, KUYRUK_K, arka_acik ? "açık" : "kapalı");
}

static void sahip_yaz() {
  Serial.print("tanınmış oyuncaklar:");
  bool hic = true;
  for (int d = 0; d < DONANIM_N; d++)
    if ((sahip_maske >> d) & 1) { Serial.printf(" %s", DONANIM_AD[d]); hic = false; }
  Serial.println(hic ? " (yok: standa konan oyuncak tanınır)" : "");
}

static void kuyruk_durum() {
  sahip_yaz();
  if (!kuyruk_var) { Serial.println("kuyruk yok (bölüm ya da model yok)"); return; }
  Serial.printf("kuyruk: hazır %d / %d yuva (figür başına %d, K=%d) | arka plan %s | bu açılışta %d yazıldı\n",
                kuyruk_say(&kq, -1, -1), kq.n_yuva, arka_hedef(), KUYRUK_K, arka_acik ? "açık" : "kapalı",
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

// ---- arka plan üretimi: boşta, eksik (figür, yer) (tanınmışlar önce; arka_maske): K aday + seçici, en iyisi flash'a ----
// İş aday aday ilerler: bir olay (oyuncak kondu, sesli komut) ya da seri komut gelirse o aday bırakılır (biten adaylar
// ve en iyisi RAM'de kalır), çocuk hikâyesini dinledikten sonra iş kaldığı adaydan sürer.
static struct {
  bool aktif;
  int f, j, K, sonraki, toplam, en_n, en_plan;
  double en_p;
  int64_t us;
} arka;
static int16_t arka_tok[N_URET];
static void halka_bosta();

static bool arka_kes() { return durdur_istendi(); }

// Döner: bir aday üretildi (ya da yarıda kesildi); false: yapılacak iş yok
static bool arka_adim() {
  if (!llm_var || !kuyruk_var || !arka_acik || ayr.acik) return false;
  uint32_t mm = arka_maske();
  int hedef = arka_hedef();
  if (arka.aktif && !((mm >> arka.f) & 1)) arka.aktif = false;  // figür unutuldu (ayar sayfası)
  if (!arka.aktif) {
    int f, j;
    // önce tanınmış (standa konmuş) figürler, boş yuva varken; sonra ötekiler
    bool bos = kuyruk_say(&kq, -1, -1) < kq.n_yuva;
    if (!(bos && model_maske() != mm && kuyruk_sonraki_sahip(&kq, hedef, N_FIGUR, FIGUR_YER_N, model_maske(), &f, &j)) &&
        !kuyruk_sonraki_sahip(&kq, hedef, N_FIGUR, FIGUR_YER_N, mm, &f, &j))
      return false;
    arka.aktif = true; arka.f = f; arka.j = j; arka.K = KUYRUK_K; arka.sonraki = 0; arka.toplam = 0;
    arka.en_p = -1e30; arka.en_n = arka.en_plan = 0; arka.us = 0;
    Serial.printf("[kuyruk] %s | %s: %d aday üretiliyor (olay ya da seri komut keser)\n", FIGUR_AD[f],
                  YER_AD[FIGUR_YER[f * YER_MAKS + j]], arka.K);
  }
  if (ay.arka_goster && uyku.durum != UYKU_KAPALI) {
    int d = model_donanim(arka.f);
    if (d >= 0) halka_figur(d);
    halka_durum(HT_ARKA);
  }
  int64_t t0 = esp_timer_get_time();
  uretim_kes = arka_kes;
  ADAY_BASI(arka.sonraki);
  Aday a = aday_uret(arka.f, arka.j, false);
  uretim_kes = NULL;
  if (ay.arka_goster) halka_bosta();
  if (a.iptal) return true;  // çocuk geldi: bu aday sonra baştan
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
  int y = kuyruk_yer_ac(&kq, mm, hedef) < 0 ? -1
          : kuyruk_yaz(&kq, arka.f, arka.j, arka.K, (float)arka.en_p, arka_tok, arka.en_n, arka.en_plan);
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
  return llm_var && kuyruk_var && arka_acik && !ayr.acik &&
         (arka.aktif || kuyruk_sonraki_sahip(&kq, arka_hedef(), N_FIGUR, FIGUR_YER_N, arka_maske(), &f, &j));
}

// ---- içerik: donanım figürünün okunacak metni ----
static const YerlesikListe *yerlesik_liste(int d) {
  for (size_t i = 0; i < sizeof YERLESIK / sizeof YERLESIK[0]; i++)
    if (!strcmp(YERLESIK[i].kimlik, DONANIM_KIMLIK[d])) return &YERLESIK[i];
  return NULL;
}

static void hikaye_yaz(int f, int j, const char *kaynak) {
  Serial.printf("\n=== %s | %s | %s ===\nSorun:", FIGUR_AD[f], YER_AD[FIGUR_YER[f * YER_MAKS + j]], kaynak);
  for (int i = 0; i < son_n; i++) yaz(son_tok[i]);
  Serial.println("\n");
}

// d figürü için içerik: model figürüyse hazır (kuyruk; j >= 0 ise o yerin) > yarım arka plan işinin en iyisi >
// canlı okuma (canli_oku: yazdıkça okur; yer sırayla döner); modelde yoksa yerleşik metin (yerlesik.h, sırayla).
// Döner: ICERIK_HAZIR (son_* ya da yerleşik metin dolu), ICERIK_CANLI (canli_f / canli_j), ICERIK_YOK.
enum { ICERIK_YOK, ICERIK_HAZIR, ICERIK_CANLI };
static int canli_f = -1, canli_j = -1;
static int icerik_hazirla(int d, int j) {
  char kaynak[96];
  int f = DONANIM_MODEL[d];
  if (f < 0) {
    const YerlesikListe *L = yerlesik_liste(d);
    if (!L || L->n <= 0) { Serial.printf("%s için içerik yok (model bilmiyor, yerleşik metin yok)\n", DONANIM_AD[d]); return ICERIK_YOK; }
    son_yerlesik = yerlesik_sira[d] % L->n;
    yerlesik_sira[d]++;
    son_d = d;
    Serial.printf("\n=== %s | yerleşik metin %d/%d ===\n%s\n\n", DONANIM_AD[d], son_yerlesik + 1, L->n, L->metin[son_yerlesik]);
    return ICERIK_HAZIR;
  }
  for (int y; kuyruk_var && (y = kuyruk_bul(&kq, f, j)) >= 0;) {
    KuyrukBaslik b;
    int n = kuyruk_oku(&kq, y, &b, son_tok, N_URET);
    if (n <= 0) { Serial.printf("kuyruk: yuva %d bozuk, atlandı\n", y); continue; }
    kuyruk_tuket(&kq, y);
    son_n = n; son_plan = b.n_plan; son_f = f; son_j = b.yer; son_d = d; son_yerlesik = -1;
    snprintf(kaynak, sizeof kaynak, "hazır hikâye (%d aday, puan %.2f; %s için %d hazır kaldı)", b.K, b.puan,
             FIGUR_AD[f], kuyruk_say(&kq, f, -1));
    HAZIR_CALINDI(f, son_j, son_tok, son_n);
    hikaye_yaz(f, son_j, kaynak);
    return ICERIK_HAZIR;
  }
  if (arka.aktif && arka.f == f && (j < 0 || arka.j == j) && arka.sonraki > 0 && arka.en_p > -99) {
    son_hikaye_sakla(arka_tok, arka.en_n, arka.en_plan, f, arka.j);
    son_d = d;
    snprintf(kaynak, sizeof kaynak, "yarım kuyruk işinden (%d/%d aday, puan %.2f)", arka.sonraki, arka.K, arka.en_p);
    arka.aktif = false;  // bu (figür, yer) için iş baştan
    HAZIR_CALINDI(f, son_j, son_tok, son_n);
    hikaye_yaz(f, son_j, kaynak);
    return ICERIK_HAZIR;
  }
  if (!llm_var) { Serial.println("LLM modeli yok: hikâye üretilemiyor."); halka_durum(HT_HATA); return ICERIK_YOK; }
  canli_f = f;
  canli_j = j < 0 ? canli_yer[f]++ % FIGUR_YER_N[f] : j;
  return ICERIK_CANLI;
}

// Son içeriğin okunacak metni oku_buf'a (model hikâyesinde plan hariç gövde)
static void icerik_metni() {
  if (son_yerlesik >= 0) {
    const YerlesikListe *L = yerlesik_liste(son_d);
    snprintf(oku_buf, sizeof oku_buf, "%s", L ? L->metin[son_yerlesik % L->n] : "");
    return;
  }
  int len = 0;
  for (int i = son_plan; i < son_n; i++) {
    int tok = son_tok[i];
    if (tok < 0 || tok >= VOCAB_N) continue;
    int b = VOCAB_OFF[tok], e = VOCAB_OFF[tok + 1];
    if (len + (e - b) >= (int)sizeof oku_buf) break;
    memcpy(oku_buf + len, VOCAB_BLOB + b, e - b);
    len += e - b;
  }
  oku_buf[len] = 0;
}

// ---- uyku (gece figürü) ----
static void uyku_baslat() {
  uyku.durum = UYKU_NINNI;
  uyku.bitis_ms = millis() + ay.uyku_dk * 60000UL;
  if (ay.muzik && hoparlor_var) {
    mk_kur(&muzik);
    muzik_seviye = 256;
    muzik_acik = true;
    amp(true);
  }
  Serial.printf("(uyku modu: ninniler %d dk, müzik kutusu %s)\n", ay.uyku_dk, muzik_acik ? "açık" : "kapalı");
}
static void uyku_son() {  // zamanlayıcı doldu, okunan ninni bitti: halka ve müzik 60 s'de söner
  uyku.durum = UYKU_SONUYOR;
  uyku.sonme_ms = millis();
  portENTER_CRITICAL(&halka_kilit);
  halka_taban(&halka, HT_GECE, millis());
  halka.sonme_ms = uyku.sonme_ms ? uyku.sonme_ms : 1;
  portEXIT_CRITICAL(&halka_kilit);
  Serial.println("(uyku: zamanlayıcı doldu; halka ve müzik 60 sn'de sönüyor)");
}
static void uyku_kapat() {  // mikrofon, yükselteç, müzik ve halka kapanır; stand yoklanmaya devam eder
  muzik_acik = false;
  muzik_seviye = 0;
  amp(false);
  mik_iste = false;
  uyku.durum = UYKU_KAPALI;
  halka_durum(HT_KAPALI);
  Serial.println("(uyku: kapandı; mikrofon, yükselteç ve halka kapalı. Uyandırmak için standa bir oyuncak koyun)");
}
static void uyku_uyan() {
  if (uyku.durum == UYKU_YOK) return;
  if (uyku.durum == UYKU_KAPALI) Serial.println("(uyku: uyandı)");
  muzik_acik = false;
  muzik_seviye = 0;
#if MIK_ACIK
  if (kws_var) mik_iste = true;
#endif
  uyku.durum = UYKU_YOK;
}

// Halkanın boştaki durumu: ayar > uyku > hata (model yok) > standda oyuncak > boşta
static void halka_bosta() {
  halka_bitti_ms = 0;
  if (ayr.acik) halka_durum(HT_AYAR);
  else if (uyku.durum == UYKU_KAPALI) halka_durum(HT_KAPALI);
  else if (uyku.durum == UYKU_SONUYOR) {}  // gece sönmesi sürüyor
  else if (uyku.durum == UYKU_NINNI) halka_durum(HT_GECE);
  else if (!llm_var) halka_durum(HT_HATA);
  else if (stand.dolu && stand.d >= 0) { halka_figur(stand.d); halka_durum(HT_OYUNCAK); }
  else halka_durum(HT_BOSTA);
}

// ---- canlı okuma: hazır hikâye yokken model yazdıkça cümle cümle okunur (bitmesi beklenmez, seçici yok) ----
// Selam büyük çalma tamponuna yazılır, model planı yazarken çalar. Gövdenin her cümlesi biter bitmez seslendirilip
// tampona eklenir; model sonraki cümleyi yazarken önceki çalar. "Dur": anlatım susar, hikâye sessizce tamamlanır
// (sonra "Devam" kaldığı cümleden sürer); "Devam" susmuşken gelirse anlatım hemen kaldığı cümleden sürer. Oyuncak
// kalkar, başka oyuncak konur ya da "Başka" / "Bir daha" denirse üretim bırakılır (olay ana döngüde işlenir).
#define CANLI_TAHMIN 16  // halka ilerlemesi için tahmini cümle sayısı (gerçeği hikâye bitince belli olur)
static bool sesli_yerinde_mi(int e);
static void sesli_yerinde(int e);
static struct {
  bool sesli, okunur, sustu, iptal;
  int n, yazilan, okunan, dur, bas, len;  // n: bulunan cümle; yazilan: tampona yazılan; dur: susulan cümle
  int cb[CUMLE_MAKS], ce[CUMLE_MAKS];     // cümlelerin oku_buf'taki başı / sonu
  uint32_t son[CUMLE_MAKS];               // cümlenin çalma tamponunda bittiği bayt (cal_gonderilen)
} cn;

static int canli_calan() {  // çalınmakta olan cümle (hepsi çalındıysa sıradaki)
  if (!cn.sesli) return cn.okunan;
  uint32_t a = cal_alinan;
  for (int i = 0; i < cn.yazilan; i++)
    if ((int32_t)(cn.son[i] - a) > 0) return i;
  return cn.yazilan;
}
static void canli_sustur() {
  cn.dur = canli_calan();
  cn.sustu = true; konusma_kesildi = true; cal_sustur = true;
  Serial.printf("\n(dur: %d. cümlede sustu; hikâye sessizce tamamlanıyor)\n", cn.dur + 1);
}
// Okuma bir olayla kesildi: "Dur" ise sus ve sessizce tamamla (false); değilse üretimi bırak (true)
static bool canli_kesinti() {
  Olay o;
  if (olay_bak_(&o) && o.tur == OLAY_SESLI && o.deger == KWS_DUR) {
    olay_al_(&o);
    Serial.println("(sesli komut: dur)");
    dinle_bitir(true);
    canli_sustur();
    return false;
  }
  cn.iptal = true; konusma_kesildi = true; cal_sustur = true;
  return true;
}
static void canli_cumle_oku(int i, int b, int e) {
  cn.okunan = i;
  if (i == 0 || i == cn.dur) halka_durum(HT_OKUMA);
  halka_ilerle(i, i + 2 > CANLI_TAHMIN ? i + 2 : CANLI_TAHMIN);
  if (cn.sesli) {
    if (i > 0) ses_sessizlik(&ses, stil_ara_ms, pcm_yaz, NULL);
    if (!konusma_kesildi) {
      long r = ses_cumle_n(&ses, oku_buf + b, (size_t)(e - b), pcm_yaz, NULL);
      if (r < 0) Serial.printf("ses hatası: %s\n", ses_hata);
    }
  } else if (SESSIZ_MS_HARF > 0) {
    if (i > 0) sessiz_bekle(stil_ara_ms);
    if (!konusma_kesildi) sessiz_bekle((e - b) * SESSIZ_MS_HARF);
  }
  if (!konusma_kesildi) { cn.son[i] = cal_gonderilen; if (cn.yazilan < i + 1) cn.yazilan = i + 1; }
  else if (!cn.sustu && !cn.iptal) canli_kesinti();
}
// oku_buf'ta biten cümleleri ayırıp okur (metin_oku ile aynı bölme: ses_cumle_sonu, ses_harfli). son: metin bitti
static void canli_bol(bool son) {
  for (;;) {
    const char *p = oku_buf + cn.bas;
    if (!*p) return;
    const char *s = ses_cumle_sonu(p);
    if (!*s && !son) return;  // cümle sonu henüz belli değil (sonraki token kapanış tırnağı olabilir)
    if (ses_harfli(p, s)) {
      int i;
      if (cn.n < CUMLE_MAKS) { i = cn.n++; cn.cb[i] = (int)(p - oku_buf); }
      else i = CUMLE_MAKS - 1;  // sığmayanlar sonuncuya eklenir (metin_oku gibi)
      cn.ce[i] = (int)(s - oku_buf);
      if (cn.okunur && !cn.sustu && !cn.iptal) canli_cumle_oku(i, (int)(p - oku_buf), (int)(s - oku_buf));
    }
    cn.bas = (int)(s - oku_buf);
  }
}
static void canli_govde(int tok) {
  if (tok < 0 || tok >= VOCAB_N) return;
  int b = VOCAB_OFF[tok], e = VOCAB_OFF[tok + 1];
  if (cn.len + (e - b) >= (int)sizeof oku_buf) return;
  memcpy(oku_buf + cn.len, VOCAB_BLOB + b, e - b);
  cn.len += e - b;
  oku_buf[cn.len] = 0;
  canli_bol(false);
}
static void canli_devam() {  // susmuşken "Devam": kalınan cümleden yeniden
  Serial.printf("\n(devam: %d. cümleden)\n", cn.dur + 1);
  while (!xStreamBufferIsEmpty(cal_akim)) delay(10);
  cal_sustur = false; konusma_kesildi = false; cn.sustu = false;
  int m = cn.n < CUMLE_MAKS ? cn.n : CUMLE_MAKS;
  for (int i = cn.dur; i < m && !konusma_kesildi && !cn.iptal; i++) canli_cumle_oku(i, cn.cb[i], cn.ce[i]);
}
// Üretim sırasında (her token'dan önce) olaylar
static bool canli_okuma_kes() {
  if (cn.iptal) return true;
  if (!cn.sustu) return okuma_denetle_(true) != KES_YOK && canli_kesinti();
  olaylari_topla();  // susmuş: hikâye sessizce tamamlanıyor
  Olay o;
  while (olay_bak_(&o)) {
    if (o.tur == OLAY_SESLI && o.deger == KWS_DEVAM) {
      olay_al_(&o);
      Serial.println("(sesli komut: devam)");
      dinle_bitir(true);
      canli_devam();
      return cn.iptal;
    }
    if (o.tur == OLAY_SESLI && (o.deger == KWS_DUR || sesli_yerinde_mi(o.deger))) {
      olay_al_(&o);
      Serial.printf("(sesli komut: %s)\n", kws_ad(o.deger));
      if (o.deger == KWS_DUR) dinle_bitir(true);
      else sesli_yerinde(o.deger);
      continue;
    }
    if (o.tur == OLAY_STAND_BILINMEYEN) { olay_al_(&o); continue; }
    cn.iptal = true;  // başka / bir daha, oyuncak kalktı ya da değişti
    return true;
  }
  return false;
}

// d donanım figürü, f model figürü, j yer; onsoz: önce okunacak selam (NULL olabilir). Döner: kesildiği cümle (hepsi
// okunduysa okuma_n); -1: üretim bırakıldı (hikâye yok, olay ana döngüde).
static int canli_oku(int d, int f, int j, const char *onsoz) {
  memset(&cn, 0, sizeof cn);
  cn.sesli = ses_var && ses_oku;
  cn.okunur = hoparlor_var || SESSIZ_MS_HARF > 0;
  oku_buf[0] = 0;
  halka_figur(d);
  ses_stili(MOD_HIKAYE);
  cal_sinir = cal_bayt;  // büyük tampon: yazarken çalsın
  if (cn.okunur) {
    amp(true);
    cal_bekleme_us = 0; konusma_kesildi = false; konusma_kesilebilir = true; cal_sustur = false;
  }
  if (onsoz) {  // selam: tampona; model planı yazarken çalar
    halka_ilerle(0, 1);
    halka_durum(HT_OKUMA);
    for (const char *p = onsoz; *p && cn.okunur && !konusma_kesildi;) {
      const char *q = ses_cumle_sonu(p);
      if (ses_harfli(p, q)) {
        if (cn.sesli) ses_cumle_n(&ses, p, (size_t)(q - p), pcm_yaz, NULL);
        else sessiz_bekle((int)(q - p) * SESSIZ_MS_HARF);
      }
      p = q;
    }
    if (konusma_kesildi) cn.iptal = true;  // selam kesildi: olay ana döngüde
  }
  Aday a = {0, 0, 0.0, false, false, true};
  if (!cn.iptal) {
    halka_durum(HT_HAZIRLA);
    Serial.printf("\n=== %s | %s | canlı okuma (yazdıkça) ===\n", FIGUR_AD[f], YER_AD[FIGUR_YER[f * YER_MAKS + j]]);
    int64_t t0 = esp_timer_get_time();
    llm_profile_reset(&s); ornek_us = 0;
    ADAY_BASI(0);
    for (int tekrar = 0;; tekrar++) {
      uretim_kes = canli_okuma_kes; govde_tok = canli_govde;
      a = aday_uret(f, j, true);
      uretim_kes = NULL; govde_tok = NULL;
      if (a.iptal || cn.iptal || !a.plan_bozuk || tekrar == 2) break;
      Serial.println("\n(plan bozuk, yeniden deniyorum)");  // gövde hiç başlamadı: okunan bir şey yok
    }
    if (!a.iptal && !cn.iptal) {
      canli_bol(true);  // son cümle
      float sn = (esp_timer_get_time() - t0) / 1e6f;
      Serial.printf("\n\n--- canlı: %d token %.1f s = %.2f token/s ---\n", a.n, sn, sn > 0 ? a.n / sn : 0.f);
    }
  }
  bool iptal = a.iptal || cn.iptal || a.plan_bozuk;
  if (!iptal) {
    son_hikaye_sakla(aday_tok, a.n, a.n_plan, f, j);
    son_d = d;
    while (cn.okunur && !konusma_kesildi && !xStreamBufferIsEmpty(cal_akim)) {  // kalan cümleler çalarken olaylar
      if (okuma_denetle_(true) != KES_YOK && canli_kesinti()) break;
      delay(20);
    }
  } else {
    Serial.println("\n(durduruldu)");
  }
  int m = cn.n < CUMLE_MAKS ? cn.n : CUMLE_MAKS;
  int k = iptal ? -1 : cn.sustu ? cn.dur : konusma_kesildi ? canli_calan() : m;
  if (k >= 0 && k >= m) halka_ilerle(m, m);
  okuma_n = m;
  okuma_ortada = k >= 0 && k < m;
  if (cn.okunur) {
    if (cn.sesli && !konusma_kesildi) ses_sessizlik(&ses, 150, pcm_yaz, NULL);
    cal_bitir();
    konusma_kesildi = false;
    konusma_kesilebilir = false;
    konusma_seviye = 0;
    if (!muzik_acik) amp(false);
  }
  cal_sinir = cal_sinir_1sn;
  return k;
}

// ---- okuma: oyuncağın içeriği (yeni / son içerik baştan / duran okuma kaldığı cümleden) ----
// onsoz: içerikten önce okunacak selam (NULL olabilir). Hazır içerik yoksa canlı okuma (selam da onun içinde).
enum { OYNA_YENI, OYNA_TEKRAR, OYNA_DEVAM };
static void oyna_(int d, int mod, int j, const char *onsoz) {
  for (;;) {
    int bas = 0, r = ICERIK_HAZIR;
    if (mod == OYNA_DEVAM && durak.var && durak.d == d && son_d == d) {
      bas = durak.cumle;
      Serial.printf("(devam: %d. cümleden)\n", bas + 1);
    } else if (mod == OYNA_TEKRAR && son_d == d && (son_yerlesik >= 0 || son_n > 0)) {
      Serial.println("(bir daha: baştan)");
    } else if ((r = icerik_hazirla(d, j)) == ICERIK_YOK) {
      halka_ustte(HU_ANLASILMADI, HALKA_ONAY_MS);
      halka_bosta();
      return;
    }
    durak.var = false;
    bool gece = DONANIM_MOD[d] == MOD_UYKU;
    halka_figur(d);
    int k;
    if (r == ICERIK_CANLI) {
      k = canli_oku(d, canli_f, canli_j, onsoz);
      onsoz = NULL;
      if (k < 0) { halka_bosta(); return; }  // üretim bırakıldı: sebebi (kalktı, komut) ana döngüde
    } else {
      halka_ilerle(bas, 1);
      halka_durum(gece ? HT_GECE : HT_OKUMA);
      ses_stili(DONANIM_MOD[d]);
      if (onsoz) {
        bool tamam = metin_oku(onsoz, 0, false, stil_ara_ms) >= okuma_n;
        onsoz = NULL;
        if (!tamam) {  // selam kesildi: hazır içerik kaybolmasın ("Devam" ya da "Bir daha" okur)
          ses_stili(MOD_HIKAYE);
          durak.var = son_d == d; durak.d = d; durak.cumle = 0;
          return;
        }
      }
      icerik_metni();
      k = metin_oku(oku_buf, bas, !gece, stil_ara_ms);
      ses_stili(MOD_HIKAYE);
    }
    int n = okuma_n;
    Serial.printf("(okuma: %d/%d cümle%s)\n", k, n, k < n ? (okuma_ortada ? ", durdu, cümle ortasında" : ", durdu") : "");
    if (k < n) {  // durdu: sebebi (dur, başka, oyuncak kalktı ...) ana döngü işler
      durak.var = true; durak.d = d; durak.cumle = k;
      return;
    }
    if (gece && uyku.durum == UYKU_NINNI) {
      if (!(stand.dolu && stand.d == d)) { uyku_uyan(); halka_bosta(); return; }  // gece figürü kalktı (bitir ayarı)
      if ((int32_t)(millis() - uyku.bitis_ms) < 0) { mod = OYNA_YENI; continue; }  // zamanlayıcı sürüyor: sıradaki
      uyku_son();
      return;
    }
    halka_bitti_ms = millis() | 1;  // ilerleme dolu kalır, 3 s sonra boşta
    return;
  }
}
static void oyna(int d, int mod) { oyna_(d, mod, -1, NULL); }

// ---- ayarlar (NVS, Preferences) ----
static Preferences prefs;
static bool prefs_acik = false;

static void ayar_uygula() {
  ayar_duzelt(&ay);
  if (ses_seviye > ay.ses_maks) ses_seviye = ay.ses_maks;
  kazanc_guncelle();
  halka_ayarla();
}
static void ayar_yukle() {
  ayar_varsayilan(&ay);
  prefs_acik = prefs.begin("hikaye", false);
  if (!prefs_acik) return;
  ses_seviye = prefs.getUChar("ses", SES_SEVIYE_VARSAYILAN);
  String ad = prefs.getString("ad", "");
  char t[AYAR_AD_BAYT];
  if (ad_temizle(ad.c_str(), t) == AD_TAMAM) snprintf(ay.ad, sizeof ay.ad, "%s", t);
  ay.ses_maks = prefs.getUChar("ses_maks", ay.ses_maks);
  ay.uyku_dk = prefs.getUChar("uyku_dk", ay.uyku_dk);
  ay.parlaklik = prefs.getUChar("parlak", ay.parlaklik);
  ay.cekilince = prefs.getUChar("cekil", ay.cekilince);
  ay.nefes = prefs.getUChar("nefes", ay.nefes);
  ay.arka_goster = prefs.getUChar("arka_gos", ay.arka_goster);
  ay.muzik = prefs.getUChar("muzik", ay.muzik);
  sahip_maske = prefs.getUInt("sahip", 0) & ((1u << DONANIM_N) - 1);
  arka_acik = prefs.getBool("arka", true);
  if (ses_seviye < 0 || ses_seviye >= SES_SEVIYE_N) ses_seviye = SES_SEVIYE_VARSAYILAN;
  ayar_uygula();
}
static void ayar_kaydet_simdi() {
  ayar_kirli = false;
  if (!prefs_acik) return;
  prefs.putUChar("ses", (uint8_t)ses_seviye);
  prefs.putString("ad", ay.ad);
  prefs.putUChar("ses_maks", ay.ses_maks);
  prefs.putUChar("uyku_dk", ay.uyku_dk);
  prefs.putUChar("parlak", ay.parlaklik);
  prefs.putUChar("cekil", ay.cekilince);
  prefs.putUChar("nefes", ay.nefes);
  prefs.putUChar("arka_gos", ay.arka_goster);
  prefs.putUChar("muzik", ay.muzik);
  prefs.putUInt("sahip", sahip_maske);
  prefs.putBool("arka", arka_acik);
}
static void ayar_kaydet() {  // konuşma ya da üretim sırasında flash'a yazılmasın: boşta, 2 s sonra
  if (ayar_kirli && millis() - son_etkinlik_ms >= 2000) ayar_kaydet_simdi();
}
// Oyuncak standa ilk kez kondu: tanınır (kalıcı); arka plan artık onun için de hikâye hazırlar
static void sahip_ekle(int d) {
  if ((sahip_maske >> d) & 1) return;
  sahip_maske |= 1u << d;
  ayar_kaydet_simdi();
  Serial.printf("(yeni oyuncak tanındı: %s%s)\n", DONANIM_AD[d],
                DONANIM_MODEL[d] >= 0 ? "; boşta onun hikâyeleri hazırlanacak" : "; yerleşik metinleri var");
}

// ---- ses düzeyi, dinleme penceresi ----
static void ses_degistir(int yon) {
  int v = ses_seviye + yon;
  ses_seviye = v < 0 ? 0 : v > ay.ses_maks ? ay.ses_maks : v;
  ayar_kirli = true;
  kazanc_guncelle();
  portENTER_CRITICAL(&halka_kilit);
  halka.duzey = (uint8_t)ses_seviye;
  halka.maks = (uint8_t)(SES_SEVIYE_N - 1);
  portEXIT_CRITICAL(&halka_kilit);
  halka_ustte(HU_SES, HALKA_SES_MS);
  Serial.printf("ses seviyesi %d/%d (en çok %d; kazanç %.2f)\n", ses_seviye, SES_SEVIYE_N - 1, ay.ses_maks,
                SES_KAZANC[ses_seviye] / 256.0);
}
static void dinle_bitir(bool anlasildi) {
  if (!dinle_bitis) return;
  dinle_bitis = 0;
  kisma_dinle = 256;
  kazanc_guncelle();
  halka_ustte(anlasildi ? HU_ONAY : HU_ANLASILMADI, HALKA_ONAY_MS);
  if (!anlasildi) Serial.println("(sesli komut: anlaşılmadı)");
}
// Okurken (ve üretirken) olduğu yerde işlenen komutlar: uyandırma (dinliyorum: konuşma kısılır), ses aç/kıs, devam
static bool sesli_yerinde_mi(int e) { return e == KWS_UYANDIRMA || e == KWS_SESI_AC || e == KWS_SESI_KIS || e == KWS_DEVAM; }
static void sesli_yerinde(int e) {
  if (e == KWS_UYANDIRMA) {
    dinle_bitis = (millis() + DINLE_MS) | 1;
    kisma_dinle = 90;  // ~-9 dB: çocuğun komutu duyulsun
    kazanc_guncelle();
    halka_ustte(HU_DINLE, DINLE_MS);
  } else if (e == KWS_SESI_AC || e == KWS_SESI_KIS) {
    dinle_bitis = 0;
    kisma_dinle = 256;
    ses_degistir(e == KWS_SESI_AC ? 1 : -1);
  } else {
    dinle_bitir(true);
  }
}

// Okuma ve canlı üretim sırasında olaylara bakar. Yerinde işlenenler tüketilir; durduranlar sırada kalır, ana döngü
// okuma bittikten sonra işler. Döner: KES_YOK | KES_HEMEN | KES_CUMLE (oyuncak çekildi, "cümle sonunda dur" ayarı).
// uretim: canlı üretim (oyuncak çekilince her zaman durur; seri giriş kesmez: "f j K" denemesi).
static int okuma_denetle_(bool uretim) {
  olaylari_topla();
  Olay o;
  while (olay_bak_(&o)) {
    if (o.tur == OLAY_SESLI) {
      if (!sesli_yerinde_mi(o.deger)) return KES_HEMEN;  // dur, başka, bir daha
      olay_al_(&o);
      Serial.printf("(sesli komut: %s)\n", kws_ad(o.deger));
      sesli_yerinde(o.deger);
      continue;
    }
    if (o.tur == OLAY_STAND_KALKTI) {
      if (uretim || ay.cekilince == CEKILINCE_HEMEN) return KES_HEMEN;
      if (ay.cekilince == CEKILINCE_CUMLE) return KES_CUMLE;
      olay_al_(&o);
      Serial.println("(oyuncak kalktı: okuma bitirilecek)");
      continue;
    }
    if (o.tur == OLAY_STAND_BILINMEYEN) { olay_al_(&o); continue; }
    return KES_HEMEN;  // başka oyuncak / ayar kartı kondu, düğme
  }
  if (!uretim && Serial.available()) return KES_HEMEN;
  return KES_YOK;
}

// ---- ayar modu: ayar kartı standa konunca Wi-Fi erişim noktası (WPA2, her açılışta yeni 8 haneli şifre: oyuncak
// sesli söyler), DNS her adı karta yönlendirir (telefonda ayar sayfası kendiliğinden açılır), ayar sayfası ----
static WebServer web(80);
static DNSServer dns;
static char ayar_sifre[9], ayar_ssid[33];
static bool web_kuruldu = false;

static void web_json(int kod, const char *govde) { web.send(kod, "application/json; charset=utf-8", govde); }
static void web_yonlendir() {
  web.sendHeader("Location", "http://192.168.4.1/", true);
  web.send(302, "text/plain", "");
}
static const char *web_alan(void *, const char *ad) {
  static String s;
  if (!web.hasArg(ad)) return NULL;
  s = web.arg(ad);
  return s.c_str();
}
static void web_sayfa() { web.send(200, "text/html; charset=utf-8", AYAR_SAYFA); }
static void web_durum() {
  static char b[2560];
  int n = snprintf(b, sizeof b, "{\"ayar\":{");
  n += ayar_json(&ay, b + n, sizeof b - n);
  long kalan = (long)(AYAR_SURE_MS - (millis() - ayr.bas_ms)) / 1000;
  n += snprintf(b + n, sizeof b - n, "},\"kalan_sn\":%ld,\"ses_maks_ust\":%d,\"figurler\":[", kalan < 0 ? 0 : kalan,
                SES_SEVIYE_N - 1);
  for (int d = 0; d < DONANIM_N && n < (int)sizeof b - 200; d++) {
    int f = DONANIM_MODEL[d];
    n += snprintf(b + n, sizeof b - n, "%s{\"no\":%d,\"ad\":\"%s\",\"sahip\":%d,\"hazir\":%d,\"gece\":%d}", d ? "," : "",
                  DONANIM_NFC[d], DONANIM_AD[d], (int)((sahip_maske >> d) & 1),
                  f >= 0 && kuyruk_var ? kuyruk_say(&kq, f, -1) : -1, DONANIM_MOD[d] == MOD_UYKU);
  }
  snprintf(b + n, sizeof b - n, "],\"ayar_karti\":%d,\"tanit\":{\"durum\":%d,\"no\":%d,\"tamam\":%d,\"mesaj\":\"%s\"}}",
           AYAR_KARTI_NFC, ayr.tanit, ayr.tanit_no, ayr.tanit_tamam, ayr.mesaj);
  web_json(200, b);
}
static void web_kaydet() {
  char h[128], b[192];
  if (ayar_form_uygula(&ay, web_alan, NULL, h, sizeof h)) {
    snprintf(b, sizeof b, "{\"tamam\":false,\"hata\":\"%s\"}", h);
    web_json(400, b);
    return;
  }
  ayar_uygula();
  ayar_kaydet_simdi();
  Serial.printf("[ayar] kaydedildi: ad \"%s\", en yüksek ses %d, uyku %d dk, parlaklık %d, çekilince %s, nefes %d, "
                "hazırlık ışığı %d, müzik %d\n", ay.ad, ay.ses_maks, ay.uyku_dk, ay.parlaklik, CEKILINCE_AD[ay.cekilince],
                ay.nefes, ay.arka_goster, ay.muzik);
  web_json(200, "{\"tamam\":true}");
}
static void web_tanit() {
  int no = 0;
  if (!web.hasArg("no") || !ayar_sayi(web.arg("no").c_str(), &no) || (donanim_bul(no) < 0 && no != AYAR_KARTI_NFC)) {
    web_json(400, "{\"tamam\":false,\"hata\":\"Figür seçin.\"}");
    return;
  }
  ayr.tanit = TANIT_BEKLE;
  ayr.tanit_no = no;
  ayr.tanit_ms = millis();
  ayr.tanit_oldu = true;
  ayr.tanit_tamam = false;
  snprintf(ayr.mesaj, sizeof ayr.mesaj, "Ayar kartını kaldırın, figürün tabanını standa koyun (60 sn).");
  Serial.printf("[ayar] oyuncak tanıt: nfc_no %d bekleniyor\n", no);
  web_json(200, "{\"tamam\":true}");
}
static void web_sil() {
  bool unut = web.hasArg("unut") && web.arg("unut") == "1";
  int n = kuyruk_var ? kuyruk_temizle(&kq) : 0;
  arka.aktif = false;
  if (unut) { sahip_maske = 0; ayar_kaydet_simdi(); }
  Serial.printf("[ayar] hikâyeler silindi: %d hazır hikâye%s\n", n, unut ? "; tanınmış oyuncaklar unutuldu" : "");
  char b[64];
  snprintf(b, sizeof b, "{\"tamam\":true,\"silinen\":%d}", n);
  web_json(200, b);
}
static void web_bitir() {
  web_json(200, "{\"tamam\":true}");
  ayr.kapat_iste = true;
}
static void web_kur() {
  if (web_kuruldu) return;
  web.on("/", HTTP_GET, web_sayfa);
  web.on("/durum", HTTP_GET, web_durum);
  web.on("/kaydet", HTTP_POST, web_kaydet);
  web.on("/tanit", HTTP_POST, web_tanit);
  web.on("/sil", HTTP_POST, web_sil);
  web.on("/bitir", HTTP_POST, web_bitir);
  // telefonların "internet var mı" denemeleri: sayfaya yönlendir (captive portal penceresi açılır)
  static const char *const YOKLAMA[] = {"/generate_204", "/gen_204", "/hotspot-detect.html", "/library/test/success.html",
                                        "/connecttest.txt", "/ncsi.txt", "/redirect", "/canonical.html", "/fwlink"};
  for (size_t i = 0; i < sizeof YOKLAMA / sizeof YOKLAMA[0]; i++) web.on(YOKLAMA[i], web_yonlendir);
  web.onNotFound(web_yonlendir);
  web_kuruldu = true;
}

static void ayar_modu_ac() {
  if (ayr.acik) return;
  memset(&ayr, 0, sizeof ayr);
  ayr.acik = true;
  ayr.bas_ms = ayr.bos_ms = millis();
  durak.var = false;
  for (int i = 0; i < 8; i++) ayar_sifre[i] = (char)('0' + esp_random() % 10);
  ayar_sifre[8] = 0;
  uint8_t mac[6] = {0};
  esp_read_mac(mac, ESP_MAC_WIFI_SOFTAP);
  snprintf(ayar_ssid, sizeof ayar_ssid, "%s%02X%02X", AYAR_SSID_ONEK, mac[4], mac[5]);
  halka_durum(HT_AYAR);
  Serial.printf("[ayar modu] boş SRAM %u B, PSRAM %u B\n", (unsigned)heap_caps_get_free_size(MALLOC_CAP_INTERNAL),
                (unsigned)heap_caps_get_free_size(MALLOC_CAP_SPIRAM));
  WiFi.mode(WIFI_AP);
  IPAddress ip(192, 168, 4, 1), ag(255, 255, 255, 0);
  WiFi.softAPConfig(ip, ip, ag);
  if (!WiFi.softAP(ayar_ssid, ayar_sifre, 1, 0, 2)) {  // WPA2-PSK, kanal 1, görünür, en çok 2 bağlantı
    Serial.println("[ayar modu] HATA: Wi-Fi erişim noktası açılamadı");
    WiFi.mode(WIFI_OFF);
    ayr.acik = false;
    halka_durum(HT_HATA);
    konus("Ayar modu açılamadı.");
    return;
  }
  dns.setErrorReplyCode(DNSReplyCode::NoError);
  dns.start(53, "*", ip);
  web_kur();
  web.begin();
  Serial.printf("[ayar modu] Wi-Fi: %s | şifre: %s | sayfa: http://192.168.4.1 | en çok %lu dk\n", ayar_ssid,
                ayar_sifre, AYAR_SURE_MS / 60000);
  char r[128], m[400];
  rakam_metni(ayar_sifre, r, sizeof r);
  snprintf(m, sizeof m, "Ayar modu açık. Telefonunla Masalcı Ayar ağına bağlan. Şifre: %s. Tekrar ediyorum: %s.", r, r);
  konus(m);
}

static void ayar_modu_kapat(const char *neden) {
  web.stop();
  dns.stop();
  WiFi.softAPdisconnect(true);
  WiFi.mode(WIFI_OFF);
  ayr.acik = false;
  ayar_kaydet_simdi();
  Serial.printf("[ayar modu kapandı: %s]\n", neden);
  halka_bosta();
  konus("Ayarlar kaydedildi.");
  son_etkinlik_ms = millis();
}

// Standdaki etikete tanıtılan figürü yazar, doğrular
static void tanit_yaz() {
  int r = nfc_kayit_yaz(ayr.tanit_no, stand.uid, stand.uid_n);
  int d = donanim_bul(ayr.tanit_no);
  const char *ad = d >= 0 ? DONANIM_AD[d] : "ayar kartı";
  char m[128];
  ayr.tanit = TANIT_SONUC;
  ayr.tanit_tamam = r == NFC_YAZ_TAMAM;
  if (ayr.tanit_tamam) {
    stand.no = ayr.tanit_no;
    stand.d = d;
    if (d >= 0) sahip_ekle(d);
    snprintf(ayr.mesaj, sizeof ayr.mesaj, "Tamam: bu etiket artık %s.", ad);
    snprintf(m, sizeof m, "Tamam, bu artık %s.", ad);
    halka_ustte(HU_ONAY, HALKA_ONAY_MS);
  } else {
    snprintf(ayr.mesaj, sizeof ayr.mesaj, "Etiket yazılamadı: %s.", NFC_YAZ_AD[-r]);
    snprintf(m, sizeof m, "Etiket yazılamadı.");
    halka_ustte(HU_ANLASILMADI, HALKA_ONAY_MS);
  }
  Serial.printf("[ayar] oyuncak tanıt: %s\n", ayr.mesaj);
  konus(m);
}

// Ayar modunda ana döngü: sayfa istekleri, standdaki etiket ("oyuncak tanıt"), süreler
static void ayar_dongu() {
  dns.processNextRequest();
  web.handleClient();
  uint32_t simdi = millis();
  Olay o;
  while (ayr.acik && olay_al_(&o)) {
    if (o.tur == OLAY_STAND_KONDU || o.tur == OLAY_STAND_BILINMEYEN) {
      bool ayar_karti = o.tur == OLAY_STAND_KONDU && o.deger == AYAR_KARTI_NFC;
      if (ayr.tanit == TANIT_BEKLE && (!ayar_karti || ayr.tanit_no == AYAR_KARTI_NFC)) tanit_yaz();
    } else if (o.tur == OLAY_STAND_KALKTI && !ayr.tanit_oldu) {
      ayar_modu_kapat("ayar kartı kaldırıldı");
      return;
    }  // sesli komutlar ve düğmeler ayar modunda yok sayılır
  }
  if (ayr.tanit == TANIT_BEKLE && simdi - ayr.tanit_ms > AYAR_TANIT_MS) {
    ayr.tanit = TANIT_SONUC;
    ayr.tanit_tamam = false;
    snprintf(ayr.mesaj, sizeof ayr.mesaj, "Süre doldu: standa etiket konmadı.");
  }
  if (stand.dolu || ayr.tanit == TANIT_BEKLE) ayr.bos_ms = simdi;
  if (ayr.kapat_iste) ayar_modu_kapat("sayfadan bitirildi");
  else if (simdi - ayr.bas_ms >= AYAR_SURE_MS) ayar_modu_kapat("10 dakika doldu");
  else if (ayr.tanit_oldu && simdi - ayr.bos_ms >= AYAR_BOS_KAPAT_MS) ayar_modu_kapat("stand 1 dakikadır boş");
}

// ---- olaylar (okuma dışında, ana döngüde) ----
static void bekle_olayli(uint32_t ms) {  // halka dolarken: olaylar toplanır, oyuncak kalkarsa erken biter
  uint32_t bas = millis();
  while (millis() - bas < ms && stand.dolu) {
    delay(10);
    olaylari_topla();
  }
}

static void stand_kondu(int no) {
  uyku_uyan();
  if (no == AYAR_KARTI_NFC) { ayar_modu_ac(); return; }
  int d = donanim_bul(no);
  if (d < 0) {
    Serial.printf("nfc_no %d bu yazılımda tanımlı değil (data/figur_donanim.json)\n", no);
    halka_ustte(HU_ANLASILMADI, HALKA_ONAY_MS);
    return;
  }
  sahip_ekle(d);
  durak.var = false;
  Serial.printf("\n[oyuncak: %s]\n", DONANIM_AD[d]);
  halka_figur(d);
  halka_durum(HT_DOLMA);
  bekle_olayli(HALKA_DOLMA_MS);
  if (!stand.dolu || stand.no != no) return;  // dolarken kalktı
  bool gece = DONANIM_MOD[d] == MOD_UYKU;
  if (gece) uyku_baslat();
  static char s[256];
  if (gece) ninni_selam_metni(ay.ad, s, sizeof s);
  else selam_metni(ay.ad, DONANIM_AD[d], s, sizeof s);
  Serial.printf("[%s]\n", s);
  oyna_(d, OYNA_YENI, -1, s);  // selam + içerik (hazır yoksa selam çalarken model yazmaya başlar)
}

static void stand_kalkti() {
  Serial.println("(oyuncak kalktı)");
  durak.var = false;
  if (uyku.durum == UYKU_NINNI || uyku.durum == UYKU_SONUYOR) { uyku_uyan(); amp(false); }
  halka_bosta();
}

static void sesli_isle(int e) {
  Serial.printf("(sesli komut: %s)\n", kws_ad(e));
  if (e == KWS_UYANDIRMA || e == KWS_SESI_AC || e == KWS_SESI_KIS) {
    sesli_yerinde(e);
    if (e != KWS_UYANDIRMA && !muzik_acik) bip(660, 80);
    return;
  }
  bool dinliyordu = dinle_bitis != 0;
  dinle_bitir(true);
  int d = stand.dolu ? stand.d : -1;
  if (e == KWS_DUR) {  // okuma zaten durdu (kaldığı yer saklandı) ya da okunan yok
    if (!dinliyordu) halka_ustte(HU_ONAY, HALKA_ONAY_MS);
    return;
  }
  if (e != KWS_DEVAM && e != KWS_BASKA && e != KWS_BIR_DAHA) {
    halka_ustte(HU_ANLASILMADI, HALKA_ONAY_MS);
    return;
  }
  if (d < 0) {  // standda oyuncak yok: hikâye okunmaz
    halka_ustte(HU_ANLASILMADI, HALKA_ONAY_MS);
    konus("Önce bir oyuncağını standa koy.");
    halka_bosta();
    return;
  }
  if (!dinliyordu) halka_ustte(HU_ONAY, HALKA_ONAY_MS);
  oyna(d, e == KWS_DEVAM ? OYNA_DEVAM : e == KWS_BASKA ? OYNA_YENI : OYNA_TEKRAR);
}

static void olay_isle(const Olay &o) {
  switch (o.tur) {
    case OLAY_STAND_KONDU: stand_kondu(o.deger); break;
    case OLAY_STAND_BILINMEYEN: halka_ustte(HU_ANLASILMADI, HALKA_ONAY_MS); break;
    case OLAY_STAND_KALKTI: stand_kalkti(); break;
    case OLAY_SESLI: sesli_isle(o.deger); break;
#if DUGME_ACIK
    // geliştirme düğmeleri: figür / yer seçimi standı ve tanınmışlığı atlar
    case OLAY_FIGUR:
    case OLAY_FIGUR_UZUN:
      secili_f = (secili_f + (o.tur == OLAY_FIGUR ? 1 : N_FIGUR - 1)) % N_FIGUR;
      secili_j = -1;
      Serial.printf("(düğme) figür: %d %s\n", secili_f + 1, FIGUR_AD[secili_f]);
      break;
    case OLAY_YER:
    case OLAY_YER_UZUN:
      secili_j = o.tur == OLAY_YER_UZUN || secili_j + 1 >= FIGUR_YER_N[secili_f] ? -1 : secili_j + 1;
      Serial.printf("(düğme) yer: %s\n", secili_j < 0 ? "sürpriz" : YER_AD[FIGUR_YER[secili_f * YER_MAKS + secili_j]]);
      break;
    case OLAY_OYNAT: { int d = model_donanim(secili_f); if (d >= 0) oyna_(d, OYNA_YENI, secili_j, NULL); break; }
    case OLAY_OYNAT_UZUN: if (son_d >= 0) oyna(son_d, OYNA_TEKRAR); break;
    case OLAY_SES_ARTI: ses_degistir(1); break;
    case OLAY_SES_EKSI: ses_degistir(-1); break;
    case OLAY_ARKA:
      arka_acik = !arka_acik;
      ayar_kirli = true;
      Serial.printf("arka plan üretimi: %s\n", arka_acik ? "açık" : "kapalı");
      break;
#endif
    default: break;
  }
}

// Ana döngünün süreleri: okuma bitince halka, ninni zamanlayıcısı, gece sönmesi, açılış
static void zamanlayicilar() {
  uint32_t s = millis();
  if (acilis_bekliyor && halka.taban != HT_ACILIS) { acilis_bekliyor = false; halka_bosta(); }
  if (halka_bitti_ms && s - halka_bitti_ms >= 3000) halka_bosta();
  if (uyku.durum == UYKU_NINNI && (int32_t)(s - uyku.bitis_ms) >= 0) uyku_son();
  if (uyku.durum == UYKU_SONUYOR) {
    uint32_t e = s - uyku.sonme_ms;
    muzik_seviye = (uint16_t)(e >= UYKU_SONME_MS ? 0 : 256 - 256 * e / UYKU_SONME_MS);
    if (e >= UYKU_SONME_MS) uyku_kapat();
  }
}

// ---- güç: hafif uyku (yalnız uyku modunda: mikrofon kapalı; stand UYKU_DILIM_MS'de bir yoklanır) ----
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

// Hafif uyku: CPU durur, PSRAM ve RAM korunur (model yeniden yüklenmez). Süre uyandırır; UART girişinde (CDC
// kapalıyken) seri porttan gelen ilk karakterler uyandırır ama kaybolur.
static void hafif_uyku(uint32_t ms) {
  Serial.flush();
  esp_sleep_enable_timer_wakeup((uint64_t)ms * 1000);
#if !ARDUINO_USB_CDC_ON_BOOT
  uart_set_wakeup_threshold(UART_NUM_0, 3);
  esp_sleep_enable_uart_wakeup(UART_NUM_0);
#endif
  int64_t t0 = esp_timer_get_time();
  esp_light_sleep_start();
  uyku_us += esp_timer_get_time() - t0;
  uyku_sayisi++;
}

static void bosta_bekle() {
  if (uyku.durum == UYKU_KAPALI && !seri_bagli() && !Serial.available()) hafif_uyku(UYKU_DILIM_MS);
  else delay(20);
}

// ---- seri komutlar (geliştirme; ürün yalnız stand ve sesle kullanılır) ----
static int kws_olay_bul(const char *ad) {
  static const char *const AD[] = {"", "uyandirma", "dur", "devam", "baska", "bir_daha", "sesi_ac", "sesi_kis"};
  for (int i = 1; i < (int)(sizeof AD / sizeof AD[0]); i++)
    if (!strcmp(ad, AD[i])) return i;
  return -1;
}
static int onaltilik(const char *p, uint8_t *u, int kap) {
  int n = 0;
  while (n < kap && p[0] && p[1]) {
    if (*p == ' ' || *p == ':') { p++; continue; }
    unsigned v;
    if (sscanf(p, "%2x", &v) != 1) break;
    u[n++] = (uint8_t)v;
    p += 2;
  }
  return n;
}

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
    if (*p == '+') ses_degistir(1);
    else if (*p == '-') ses_degistir(-1);
    else if (*p == ' ') ses_degistir(atoi(p + 1) - ses_seviye);
    else Serial.printf("ses seviyesi %d/%d (en çok %d)\n", ses_seviye, SES_SEVIYE_N - 1, ay.ses_maks);
    return;
  }
  if (g.startsWith("w ")) {  // sesli komut taklidi: "w uyandirma", "w dur", "w devam", "w baska", "w bir_daha" ...
    int e = kws_olay_bul(g.c_str() + 2);
    if (e < 0) { Serial.println("w uyandirma|dur|devam|baska|bir_daha|sesi_ac|sesi_kis"); return; }
    halka_ekle(&ana_halka, OLAY_SESLI, e);
    return;
  }
  if (g == "n") {
    Serial.printf("NFC: %s | stand %s", NFC_AD, stand.dolu ? "dolu: " : "boş\n");
    if (stand.dolu) {
      uid_yaz(stand.uid, stand.uid_n);
      Serial.printf(" nfc_no %d (%s)\n", stand.no, stand.d >= 0 ? DONANIM_AD[stand.d] : stand.no == AYAR_KARTI_NFC ? "ayar kartı" : "?");
    }
    return;
  }
#if NFC_OKUYUCU == 0
  if (g.startsWith("n ")) {  // taslak okuyucu: alandaki etiket
    const char *p = g.c_str() + 2;
    uint8_t u[10];
    if (!strncmp(p, "koy uid ", 8)) {
      int n = onaltilik(p + 8, u, 7);
      if (n) nfc_sahte_koy_bos(u, n, false);
    } else if (!strncmp(p, "koy bos", 7)) {
      int n = onaltilik(p + 7, u, 7);
      static const uint8_t VARSAYILAN[7] = {0x04, 0xB0, 0x5E, 0x11, 0x22, 0x33, 0x80};
      nfc_sahte_koy_bos(n == 7 ? u : VARSAYILAN, 7, true);
    } else if (!strncmp(p, "koy ", 4)) {
      nfc_sahte_koy_no(atoi(p + 4));
    } else if (!strcmp(p, "kaldir")) {
      nfc_sahte_kaldir();
    } else if (!strcmp(p, "kilitle")) {
      nfc_sahte.kilitli = !nfc_sahte.kilitli;
    } else {
      Serial.println("n koy <nfc_no> | n koy bos [UID] | n koy uid <UID> | n kaldir | n kilitle");
    }
    return;
  }
#endif
  if (g == "a") { ayar_modu_ac(); return; }
  if (g == "a kapat") { if (ayr.acik) ayar_modu_kapat("seri komut"); return; }
  if (g == "sahip" || g.startsWith("sahip ")) {  // tanınmış oyuncaklar: "sahip hepsi|yok|+3|-3" (nfc_no)
    const char *p = g.c_str() + 5;
    while (*p == ' ') p++;
    int d;
    if (!strcmp(p, "hepsi")) sahip_maske = (1u << DONANIM_N) - 1;
    else if (!strcmp(p, "yok")) sahip_maske = 0;
    else if ((*p == '+' || *p == '-') && (d = donanim_bul(atoi(p + 1))) >= 0)
      sahip_maske = *p == '+' ? sahip_maske | 1u << d : sahip_maske & ~(1u << d);
    if (*p) ayar_kaydet_simdi();
    sahip_yaz();
    return;
  }
  if (g == "h") {
    Serial.printf("halka: %s | %d LED, tavan %%%d, ayar %%%d, akım ~%d mA | uyku: %s\n", halka_son_durum,
                  HALKA_LED_SAYISI, HALKA_PARLAKLIK_SINIR, ay.parlaklik, halka.akim_ma, UYKU_AD[uyku.durum]);
    return;
  }
#if DUGME_ACIK
  if (g.startsWith("t ") && g.length() >= 3) {  // düğme taklidi
    static const char HARF[] = "fFyYoO+-a";
    static const uint8_t TUR[] = {OLAY_FIGUR, OLAY_FIGUR_UZUN, OLAY_YER, OLAY_YER_UZUN, OLAY_OYNAT, OLAY_OYNAT_UZUN,
                                  OLAY_SES_ARTI, OLAY_SES_EKSI, OLAY_ARKA};
    const char *h = strchr(HARF, g.c_str()[2]);
    if (!h || !*h) { Serial.println("t f|F|y|Y|o|O|+|-|a (küçük: kısa, büyük: uzun basış)"); return; }
    halka_ekle(&ana_halka, TUR[h - HARF], 0);
    return;
  }
#endif
  if (g == "u") {
    Serial.println("10 s hafif uyku...");
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
  int a = -1, y = -1, k = 1;
  int n = sscanf(g.c_str(), "%d %d %d", &a, &y, &k);
  int f = a - 1, j = n >= 2 ? y - 1 : -1;
  if (n < 1 || f < 0 || f >= N_FIGUR || (n >= 2 && (j < 0 || j >= FIGUR_YER_N[f]))) {
    Serial.println("Anlaşılmadı. Örnek: \"8 4\" (figür no, o figürün yer no) ya da \"8 4 8\" (8 aday). \"?\" liste.");
    return;
  }
  uretim_serbest = true;  // geliştirme: standda oyuncak olmasa da üretilir
  int d = model_donanim(f);
  if (n >= 3) {  // aday sayısı verildi: her zaman üret (test), sonra oku
    if (hikaye(f, j, k < 1 ? 1 : k > 16 ? 16 : k) && d >= 0) { son_d = d; oyna(d, OYNA_TEKRAR); }
    Serial.println("Yeni hikâye için figür ve yer yazın (\"?\" liste).");
  } else if (d >= 0) {
    oyna_(d, OYNA_YENI, j, NULL);  // hazır varsa hemen
  }
  uretim_serbest = false;
}

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n=== Hikâye Oyuncağı ===");
  bekci_kur();
  esp_reset_reason_t neden = esp_reset_reason();
#if AMP_SD_PIN >= 0
  pinMode(AMP_SD_PIN, OUTPUT);
  digitalWrite(AMP_SD_PIN, LOW);
#endif
  ayar_yukle();
  halka_baslat();  // açılış gökkuşağı (model yüklenirken)
  if (neden == ESP_RST_BROWNOUT) {
    Serial.println("UYARI: güç düşmesiyle (brownout) yeniden başladı: güç kaynağı/kablo zayıf ya da hoparlör çok "
                   "akım çekiyor (README \"Güç\"). Bu açılışta ses kısıldı.");
    if (ses_seviye > 4) ses_seviye = 4;
  } else if (neden == ESP_RST_TASK_WDT || neden == ESP_RST_INT_WDT || neden == ESP_RST_WDT || neden == ESP_RST_PANIC) {
    Serial.printf("UYARI: önceki çalışma hatayla bitti (yeniden başlama sebebi %d); bu satırı bana gönderin\n", (int)neden);
  }
  main_h = xTaskGetCurrentTaskHandle();
  iki_cekirdek = xTaskCreatePinnedToCore(worker_main, "mv", 4096, NULL, 2, &worker_h, 0) == pdPASS;
  llm_var = llm_kur();
  ses_kur();  // LLM'den sonra: LLM'in PSRAM yerleşimi (head kopyası) eskisi gibi kalsın, ses kalanı kullanır
  kuyruk_hazirla();
  nfc_var = nfc_kur();
#if MIK_ACIK
  kws_var = kws_kur();
  if (kws_var && xTaskCreatePinnedToCore(mik_gorevi, "mik", 6144, NULL, 3, NULL, 0) == pdPASS) mik_iste = true;
#endif
#if DUGME_ACIK
  for (int i = 0; i < DUGME_N; i++)
    if (DUGME_PIN[i] >= 0) pinMode(DUGME_PIN[i], INPUT_PULLUP);
  dugme_gorevi_var = xTaskCreatePinnedToCore(dugme_gorevi, "dugme", 3072, NULL, 3, NULL, 1) == pdPASS;
#endif
  Serial.printf("boş: SRAM %.0f KB | PSRAM %.2f MB\n", heap_caps_get_free_size(MALLOC_CAP_INTERNAL) / 1024.0,
                heap_caps_get_free_size(MALLOC_CAP_SPIRAM) / 1048576.0);
  Serial.printf("stand NFC: %s%s | mikrofon: %s | halka: %d LED, GPIO %d%s | ses seviyesi %d/%d (en çok %d) | "
                "bekçi %d s%s\n", NFC_AD, nfc_var ? "" : " BULUNAMADI", mik_iste ? "açık (Merhaba Eko)" : "kapalı",
                HALKA_LED_SAYISI, HALKA_PIN, halka_var ? "" : " (RMT yok)", ses_seviye, SES_SEVIYE_N - 1, ay.ses_maks,
                BEKCI_SN, bekci_var ? "" : " (kurulamadı)");
  Serial.printf("ayarlar: ad \"%s\", uyku %d dk, parlaklık %d, çekilince %s, müzik kutusu %s\n", ay.ad, ay.uyku_dk,
                ay.parlaklik, CEKILINCE_AD[ay.cekilince], ay.muzik ? "açık" : "kapalı");
  sahip_yaz();
  liste();
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
  if (ayr.acik) { ayar_dongu(); delay(2); return; }
  zamanlayicilar();
  Olay o;
  if (olay_al_(&o)) {
    olay_isle(o);
    son_etkinlik_ms = millis();
    return;
  }
  if (millis() - son_etkinlik_ms >= ARKA_BEKLE_MS && arka_adim()) return;
  ayar_kaydet();
  bosta_bekle();
}
