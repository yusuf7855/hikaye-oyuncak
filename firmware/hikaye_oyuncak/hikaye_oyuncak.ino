// Hikâye Oyuncağı — kart testi (ESP32-S3 N16R8).
//
// Model flash'taki "model" bölümünde (0x110000), çekirdek açılışta PSRAM'e int8 olarak kopyalanır; head (tied
// gömme) 4-bit olarak flash'ta kalır: C2'de çekirdek + head int8 + float KV 8 MB PSRAM'e sığmıyor. Bağlam 224
// token (hikâye + plan + başlık ≈ 190). Örnekleme bilgisayardaki gen/uret.py ile aynı (runtime/ornekle.h):
// sıcaklık 0.5, top-k 40, tekrar cezası 1.1, plan modu, gövdede satır sonu yasağı, seçilmeyen figür isimleri yasak.
//
// Seri monitör (115200): "1 3" = 1. figür, 3. yer | "1,5 3" = iki figür | "r" = rastgele | "?" = liste |
// "b" = hız testi (head'in üç yolu, token başına ms dökümü).
// Sona aday sayısı: "1 3 4" = 4 aday üret, seçiciyle en iyisini yaz (puanla()). Aday sayısı yoksa (1) canlı
// yazar. Kart her hikâyeden sonra token/s ve süreyi yazar.
// Seçici: SECICI_TAM 1 (varsayılan) = secici.h, sec.py puanla'nın birebir C kopyası (hakemlerin gördüğü E5b/olay2
// seçicisi; generated/sozluk.h ~290 KB flash); 0 = eski hafif seçici (puanla_hafif, yalnız token sayımı).
// SECICI_GUVENLIK 1 (varsayılan): çocuğa uygun olmayan içerik cezası da açık (sec.py: ürün yolunda her zaman açık).
//
// Ses (ses.h): flash'taki "ses" bölümünde ses.bin varsa hikâye kartta seslendirilir; MAX98357A'ya I2S (BCLK 4,
// LRC 5, DIN 6; 16 kHz, 16 bit, mono -> iki kanala aynı örnek). Konuşurken kart üstündeki RGB LED yeşil.
// "s <metin>" = metni oku | "o" = üretilen hikâyeyi otomatik okuma aç/kapa (ses modeli varsa açık başlar).
// Bölüm ya da ses.bin yoksa her şey eskisi gibi çalışır, konuşma kapalıdır.

#include "esp_partition.h"
#include "esp_heap_caps.h"
#include "esp_timer.h"
#include "esp_random.h"

#define LLM_INT8_ACT 1
#define LLM_PROFILE 1
#define LLM_PROFILE_NOW() esp_timer_get_time()
#include "generated/llm.h"
#include "hiz.h"
#define ORNEKLE_RASTGELE() ((double)esp_random() / 4294967295.0)
#include "generated/ornekle.h"
#include "generated/vocab.h"
#include "generated/istemler.h"
#ifndef SECICI_TAM
#define SECICI_TAM 1
#endif
#ifndef SECICI_GUVENLIK
#define SECICI_GUVENLIK 1
#endif
#if SECICI_TAM
#include "secici.h"
#endif
#include <ESP_I2S.h>
#include <freertos/stream_buffer.h>
#include "ses.h"

static const int BAGLAM = 224;       // KV önbelleği: 10 katman x 224 x 160 x 4 B x 2 = 2.9 MB
static const int N_URET = 240;       // en fazla bu kadar token (plan + gövde)
static const float SICAKLIK = 0.5f, TEKRAR = 1.1f;
static const int TOP_K = 40;

// Arduino fonksiyon prototiplerini dosyanın başına ekler; Aday onlardan önce tanımlı olmalı.
struct Aday { int n, n_plan; float lp; bool bitti, plan_bozuk; };

Model model;
Scratch s;
static bool ses_var = false, ses_oku = false;   // ses modeli yüklü mü, hikâye okunsun mu
static size_t psram_used = 0;

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

// ---- iki çekirdekli matvec: çekirdek katmanlar int8, head 4-bit (hiz.h q4f) ----
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
static void matvec_par(const QT *t, const float *x, float *y) {
  static int8_t xq[LLM_Q8_MAX_INPUT];
  float xs;
  if (!iki_cekirdek || t->w8 == NULL || t->rows < 128) { MATVEC(t, x, y); return; }
  quantize_act(x, t->cols, xq, &xs);
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

static int istem_onbellek_k = -1;   // KV'sinde istemi hazır tutulan (seçim, yer); -1 yok
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
  istem_logit = (float *)heap_caps_malloc((size_t)model.out_vocab * 4, MALLOC_CAP_SPIRAM);  // yoksa önbelleksiz
  s.kcache = (float *)ps_or_die((size_t)L * S * D * 4, "kcache");
  s.vcache = (float *)ps_or_die((size_t)L * S * D * 4, "vcache");
}

static void yaz(int tok) {
  if (tok < 0 || tok >= VOCAB_N) return;
  Serial.write(VOCAB_BLOB + VOCAB_OFF[tok], VOCAB_OFF[tok + 1] - VOCAB_OFF[tok]);
}

static void liste() {
  Serial.println("\nFigürler:");
  for (int i = 0; i < N_FIGUR; i++) Serial.printf("  %2d  %s\n", i + 1, FIGUR_AD[i]);
  Serial.println("Yerler:");
  for (int i = 0; i < N_YER; i++) Serial.printf("  %2d  %s\n", i + 1, YER_AD[i]);
  Serial.println("Örnek: \"10 1\" (Alev, orman) | \"1,3 4\" (Pamuk ve Karabaş, park) | \"r\" (rastgele)");
  Serial.println("Sona aday sayısı (en çok 16) eklenirse en iyisi seçilir: \"10 1 8\" (8 aday). Aday yoksa canlı yazar.");
  Serial.printf("Ses: \"s <metin>\" metni okur | \"o\" hikâyeyi okuma %s (şu an %s)\n\n",
                ses_var ? "aç/kapa" : "(ses modeli yok)", ses_var && ses_oku ? "açık" : "kapalı");
}

// figür indeksleri (0'dan) -> seçim numarası; bulunamazsa -1
static int secim_bul(int a, int b) {
  for (int i = 0; i < N_SECIM; i++) {
    if (b < 0 && SECIM_A[i] == a && SECIM_B[i] == -1) return i;
    if (b >= 0 && ((SECIM_A[i] == a && SECIM_B[i] == b) || (SECIM_A[i] == b && SECIM_B[i] == a))) return i;
  }
  return -1;
}

static int yasak[128], govde_yasak[2], idx[TOP_K];
static double olas[TOP_K];
static int16_t aday_tok[N_URET], en_tok[N_URET];

// Bir aday üretir: aday_tok'a plan + gövde token'ları (EOT hariç). canli: token'lar üretildikçe seriye yazılır.
static int64_t ornek_us = 0;  // örnekleme (top-k, ceza) süresi

static Aday aday_uret(int sec, int yer, bool canli) {
  int ny = YASAK_OFF[sec + 1] - YASAK_OFF[sec];
  if (ny > 128) ny = 128;
  for (int i = 0; i < ny; i++) yasak[i] = YASAK_ID[YASAK_OFF[sec] + i];
  govde_yasak[0] = GOVDE_YASAK[0]; govde_yasak[1] = GOVDE_YASAK[1];
  OrnAyar ayar = {SICAKLIK, TOP_K, TEKRAR, yasak, ny, govde_yasak, 2, idx, olas};
  OrnDurum st; orn_sifirla(&st);
  int k = sec * N_YER + yer, pos = 0, tok = 0;
  // İstem her adayda aynı: bir kez işlenir. Sonraki adaylar yalnız istemden sonraki KV konumlarına yazdığından
  // istemin KV'si bozulmaz; istem sonundaki logit'ler saklanıp geri yüklenir (sonuç bit bit aynı, ~%10 hız).
  bool hazir = istem_onbellek_k == k && istem_logit;
  for (int i = ISTEM_OFF[k]; i < ISTEM_OFF[k + 1]; i++) {  // istem tekrar penceresine girer (gen.c varsayılanı)
    tok = ISTEM_ID[i];
    orn_ekle(&st, tok);
    if (hazir) pos++;
    else llm_forward(&model, tok, pos++, &s);
  }
  if (hazir) memcpy(s.logits, istem_logit, (size_t)model.out_vocab * sizeof(float));
  else if (istem_logit) { memcpy(istem_logit, s.logits, (size_t)model.out_vocab * sizeof(float)); istem_onbellek_k = k; }
  orn_plan_baslat(&st, NL_ID);
  Aday a = {0, 0, 0.f, false, false};
  double lp = 0; int n_lp = 0;
  if (canli) Serial.print("Sorun:");
  for (int step = 0; step < N_URET && pos < model.c.seq_len; step++) {
    bool govdede = st.govde;
    int64_t to = esp_timer_get_time();
    tok = orn_adim(&ayar, &st, s.logits, model.out_vocab);
    ornek_us += esp_timer_get_time() - to;
    if (govdede) { lp += orn_logp(s.logits, model.out_vocab, tok); n_lp++; }  // gövdenin güveni (gen -l ile aynı)
    if (tok == EOT_ID) { a.bitti = true; break; }
    aday_tok[a.n++] = tok;
    if (!govdede) a.n_plan = a.n;
    if (canli) yaz(tok);
    if (st.plan_bozuk) { a.plan_bozuk = true; break; }
    llm_forward(&model, tok, pos++, &s);
    if ((step & 7) == 0) delay(0);
  }
  a.lp = n_lp ? (float)(lp / n_lp) : -99.f;
  return a;
}

// Hafif seçici (sec.py'nin kartta ucuz alt kümesi): 2 x ortalama log-olasılık, bitmemiş hikâye -2, figür adı
// gövdede 2'den az -3, son %40'ta yok -3, çok kısa (<60 token) -2, plan bozuk elenir.
// Bilgisayardaki kopyası: degerlendirme/kart_secici.py.
static float puanla_hafif(const Aday &a, int sec) {
  if (a.plan_bozuk) return -1e9f;
  float p = 2.f * a.lp - (a.bitti ? 0.f : 2.f);
  int govde = a.n - a.n_plan, son = a.n_plan + (int)(govde * 0.6f);
  if (govde < 60) p -= 2.f;
  for (int f = 0; f < 2; f++) {
    int fig = f == 0 ? SECIM_A[sec] : SECIM_B[sec];
    if (fig < 0) continue;
    int say = 0, sonda = 0;
    for (int i = a.n_plan; i < a.n; i++) if (aday_tok[i] == ISIM_ID[fig]) { say++; if (i >= son) sonda++; }
    if (say < 2) p -= 3.f;
    if (!sonda) p -= 3.f;
  }
  return p;
}

#if SECICI_TAM
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

// Tam seçici (secici.h = sec.puanla): gövde metni uret.py'deki gibi çözülüp kırpılır (.strip()), plan "Sorun:" +
// plan token'ları. Plan bozuk ya da gövde boşsa elenir (uret.py: plan_bozuk).
static char govde_buf[4096], plan_buf[1024];
static inline bool ascii_bosluk(char c) { return c == ' ' || (c >= '\t' && c <= '\r'); }
static float puanla_tam(const Aday &a, int sec, int yer) {
  if (a.plan_bozuk) return -1e9f;
  int gn = coz_ekle(aday_tok + a.n_plan, a.n - a.n_plan, govde_buf, 0, sizeof govde_buf);
  int bas = 0;
  while (bas < gn && ascii_bosluk(govde_buf[bas])) bas++;
  while (gn > bas && ascii_bosluk(govde_buf[gn - 1])) gn--;
  if (gn == bas) return -1e9f;
  memcpy(plan_buf, "Sorun:", 6);
  int pn = coz_ekle(aday_tok, a.n_plan, plan_buf, 6, sizeof plan_buf);
  int fig[2], nf = 0;
  fig[nf++] = SECIM_A[sec];
  if (SECIM_B[sec] >= 0) fig[nf++] = SECIM_B[sec];
  return (float)secici_puanla(govde_buf + bas, gn - bas, plan_buf, pn, fig, nf, yer, a.bitti, a.lp, SECICI_GUVENLIK);
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
#endif

static float puanla(const Aday &a, int sec, int yer) {
#if SECICI_TAM
  return puanla_tam(a, sec, yer);
#else
  (void)yer;
  return puanla_hafif(a, sec);
#endif
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
    int tok = 0;
    while (pos < 48) {  // açgözlü: en olası token (örnekleme ölçüme girmesin)
      int b = 0;
      for (int v = 1; v < model.out_vocab; v++) if (s.logits[v] > s.logits[b]) b = v;
      tok = b;
      llm_forward(&model, tok, pos++, &s);
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

// ---- ses: metinden konuşma (ses.h), I2S hoparlör, LED ----
static const int I2S_BCLK = 4, I2S_LRC = 5, I2S_DIN = 6;
static const int CAL_BAYT = 32000;      // çalma tamponu: 1 s ses (16 kHz x 2 B)
static Ses ses;
static I2SClass i2s;
static StreamBufferHandle_t cal_akim = NULL;
static StaticStreamBuffer_t cal_yapi;
static int64_t cal_bekleme_us = 0;      // sentez, çalma tamponu dolu diye bu kadar bekledi (hesap süresinden düşülür)
static char oku_buf[4096];

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

static void led(bool acik) {
#ifdef RGB_BUILTIN
#if defined(ESP_ARDUINO_VERSION_MAJOR) && ESP_ARDUINO_VERSION_MAJOR >= 3
  rgbLedWrite(RGB_BUILTIN, 0, acik ? 255 : 0, 0);
#else
  neopixelWrite(RGB_BUILTIN, 0, acik ? 255 : 0, 0);
#endif
#else
  (void)acik;
#endif
}

// Çalma görevi: tampondan I2S'e (i2s.write DMA dolunca bekler). Sentez bu arada sonraki parçayı hesaplar.
static void calici(void *) {
  static int16_t buf[256];
  for (;;) {
    size_t n = xStreamBufferReceive(cal_akim, buf, sizeof buf, portMAX_DELAY);
    if (n) i2s.write((const uint8_t *)buf, n);
  }
}

static void pcm_yaz(void *, const int16_t *pcm, int n) {
  const uint8_t *p = (const uint8_t *)pcm;
  size_t kalan = (size_t)n * 2;
  int64_t t0 = esp_timer_get_time();
  while (kalan) {
    size_t k = xStreamBufferSend(cal_akim, p, kalan, portMAX_DELAY);
    p += k; kalan -= k;
  }
  cal_bekleme_us += esp_timer_get_time() - t0;
}

static int ses_dur(void *) { return Serial.available() > 0; }  // seri porttan bir şey gelirse cümle arasında dur

// Metni cümle cümle seslendirir (ilk cümle sentezlenirken çalmaya başlar); bitince çalmanın bitmesini bekler.
static void konus(const char *metin) {
  if (!ses_var) { Serial.println("konuşma kapalı (ses bölümü ya da ses.bin yok)"); return; }
  led(true);
  cal_bekleme_us = 0;
  int64_t t0 = esp_timer_get_time();
  long n = ses_metin(&ses, metin, pcm_yaz, NULL, 250, ses_dur);
  float hesap = (esp_timer_get_time() - t0 - cal_bekleme_us) / 1e6f, sure = n > 0 ? n / (float)ses.sr : 0.f;
  ses_sessizlik(&ses, 150, pcm_yaz, NULL);  // DMA'da kalan son parça sussun
  while (!xStreamBufferIsEmpty(cal_akim)) delay(10);
  delay(120);                               // DMA (6 x 240 örnek = 90 ms) boşalsın
  led(false);
  if (n < 0) Serial.printf("ses hatası: %s\n", ses_hata);
  else Serial.printf("[ses: %.1f s konuşma, %.1f s hesap = %.2f s hesap / s ses]\n", sure, hesap,
                     sure > 0 ? hesap / sure : 0.f);
}

// Açılışta: "ses" bölümü (alt tip 0x41) ve ses.bin varsa modeli, I2S'i ve çalma görevini kurar.
static void ses_kur() {
  const esp_partition_t *part = esp_partition_find_first(ESP_PARTITION_TYPE_DATA,
                                                         (esp_partition_subtype_t)0x41, "ses");
  if (!part) { Serial.println("ses bölümü yok (eski partitions.csv): konuşma kapalı"); return; }
  const void *base;
  esp_partition_mmap_handle_t h;
  if (esp_partition_mmap(part, 0, part->size, ESP_PARTITION_MMAP_DATA, &base, &h) != ESP_OK) {
    Serial.println("ses: mmap başarısız: konuşma kapalı"); return;
  }
  if (ses_yukle(&ses, (const uint8_t *)base, part->size, ses_ayir)) {
    Serial.printf("ses: %s: konuşma kapalı (ses.bin 0x%X adresine yüklendi mi?)\n", ses_hata, (unsigned)part->address);
    return;
  }
  ses.paralel = ses_paralel;
  uint8_t *depo = (uint8_t *)ps(CAL_BAYT + 1);
  if (!depo) depo = (uint8_t *)heap_caps_malloc(CAL_BAYT + 1, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
  if (!depo) { Serial.println("ses: çalma tamponu ayrılamadı: konuşma kapalı"); return; }
  cal_akim = xStreamBufferCreateStatic(CAL_BAYT, 1, depo, &cal_yapi);
  i2s.setPins(I2S_BCLK, I2S_LRC, I2S_DIN);
  if (!i2s.begin(I2S_MODE_STD, ses.sr, I2S_DATA_BIT_WIDTH_16BIT, I2S_SLOT_MODE_MONO, I2S_STD_SLOT_BOTH)) {
    Serial.println("ses: I2S başlatılamadı: konuşma kapalı"); return;
  }
  if (xTaskCreatePinnedToCore(calici, "cal", 4096, NULL, 5, NULL, 0) != pdPASS) {
    Serial.println("ses: çalma görevi kurulamadı: konuşma kapalı"); return;
  }
  ses_var = ses_oku = true;
  led(false);
  Serial.printf("ses: akustik d=%d (%d+%d+%d blok), vocoder d=%d (%d blok) | bellek %.0f KB PSRAM + %.0f KB SRAM | "
                "I2S BCLK %d LRC %d DIN %d | hikâyeyi okuma: açık (\"o\" ile kapat)\n",
                ses.ad, ses.n_kod, ses.n_tah, ses.n_coz, ses.vd, ses.n_vblok, ses.bellek_buyuk / 1024.0,
                ses.bellek_sicak / 1024.0, I2S_BCLK, I2S_LRC, I2S_DIN);
}

// Gövde token'larını (plan hariç) metne çevirip okur
static void hikaye_oku(const int16_t *t, int n) {
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
  konus(oku_buf);
}

static void hikaye(int sec, int yer, int K) {
  Serial.printf("\n=== %s", FIGUR_AD[SECIM_A[sec]]);
  if (SECIM_B[sec] >= 0) Serial.printf(" + %s", FIGUR_AD[SECIM_B[sec]]);
  Serial.printf(" | %s | %d aday ===\n", YER_AD[yer], K);
  int64_t t0 = esp_timer_get_time();
  llm_profile_reset(&s); ornek_us = 0;
  int toplam = 0, en_n = 0, en_plan = 0; float en_p = -1e30f;
  for (int j = 0; j < K; j++) {
    Aday a = aday_uret(sec, yer, K == 1);
    // Tek adayda plan bozulursa (plan satırı yerine hikâye başlarsa) en çok iki kez yeniden dene.
    for (int tekrar = 0; K == 1 && a.plan_bozuk && tekrar < 2; tekrar++) {
      toplam += a.n;
      Serial.println("\n(plan bozuk, yeniden deniyorum)");
      a = aday_uret(sec, yer, true);
    }
    toplam += a.n + (a.bitti ? 1 : 0);
    float p = puanla(a, sec, yer);
    if (K > 1) {
      Serial.printf("aday %d/%d: %d token, güven %.3f, %s -> puan %.2f", j + 1, K, a.n, a.lp,
                    a.plan_bozuk ? "plan bozuk" : a.bitti ? "bitti" : "yarım", p);
#if SECICI_TAM
      if (!a.plan_bozuk) kural_yaz();
#endif
      Serial.println();
    }
    if (p > en_p) { en_p = p; en_n = a.n; en_plan = a.n_plan; memcpy(en_tok, aday_tok, a.n * sizeof(int16_t)); }
  }
  if (K > 1) {
    Serial.print("\nSorun:");
    for (int i = 0; i < en_n; i++) yaz(en_tok[i]);
  }
  float sn = (esp_timer_get_time() - t0) / 1e6f;
  Serial.printf("\n\n--- %d aday, toplam %d token %.1f s = %.2f token/s ---\n", K, toplam, sn, toplam / sn);
  profil_yaz();
  if (ses_var && ses_oku && en_n > en_plan) hikaye_oku(en_tok + en_plan, en_n - en_plan);
  Serial.println("Yeni hikâye için figür ve yer yazın (\"?\" liste).");
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
  if (model.c.seq_len > BAGLAM) model.c.seq_len = BAGLAM;  // RoPE konumdan hesaplanır; S yalnız KV adımı
  Cfg *c = &model.c;
  Serial.printf("model: V=%d D=%d L=%d H=%d F=%d P=%d bağlam=%d\n", model.out_vocab, c->dim, c->n_layers,
                c->n_heads, c->ffn, c->ple_dim, c->seq_len);
  if (VOCAB_N != model.out_vocab) {
    Serial.printf("HATA: tokenizer/model uyuşmuyor: vocab.h %d, model %d\n", VOCAB_N, model.out_vocab);
    return false;
  }
  alloc_scratch();
  int want = llm_core_stage_count(&model);
  int staged = llm_stage_core_int8_alloc(&model, ps);
  if (staged != want) { Serial.printf("HATA: çekirdek %d/%d tensör PSRAM'e kopyalandı\n", staged, want); while (1) delay(1000); }
  Serial.printf("PSRAM: çekirdek int8 + KV + logits = %.2f MB; head 4-bit flash'ta\n", psram_used / 1048576.0);

  model.layer_matvec = matvec_par;
  model.head_matvec = head_par;
  head_hazirla();
  {
    const uint8_t *img = (const uint8_t *)base;
    uint32_t fp = 2166136261u;
    for (size_t i = 0; i < model.image_bytes; i++) { fp ^= img[i]; fp *= 16777619u; }
    Serial.printf("model.bin: %u B, parmak izi fp=%08x\n", (unsigned)model.image_bytes, fp);
  }
  Serial.printf("boş: SRAM %.0f KB | PSRAM %.2f MB\n", heap_caps_get_free_size(MALLOC_CAP_INTERNAL) / 1024.0,
                heap_caps_get_free_size(MALLOC_CAP_SPIRAM) / 1048576.0);
  return true;
}

static bool llm_var = false;

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n=== Hikâye Oyuncağı — kart testi ===");
  main_h = xTaskGetCurrentTaskHandle();
  iki_cekirdek = xTaskCreatePinnedToCore(worker_main, "mv", 4096, NULL, 2, &worker_h, 0) == pdPASS;
  llm_var = llm_kur();
  ses_kur();  // LLM'den sonra: LLM'in PSRAM yerleşimi (head kopyası) eskisi gibi kalsın, ses kalanı kullanır
  if (ses_var)
    Serial.printf("boş (ses sonrası): SRAM %.0f KB | PSRAM %.2f MB\n", heap_caps_get_free_size(MALLOC_CAP_INTERNAL) / 1024.0,
                  heap_caps_get_free_size(MALLOC_CAP_SPIRAM) / 1048576.0);
  liste();
}

void loop() {
  if (!Serial.available()) { delay(20); return; }
  String g = Serial.readStringUntil('\n');
  g.trim();
  if (g.length() == 0) return;
  if (g == "?") { liste(); return; }
  if (g == "o" || g == "O") {
    if (!ses_var) { Serial.println("konuşma kapalı (ses bölümü ya da ses.bin yok)"); return; }
    ses_oku = !ses_oku;
    Serial.printf("hikâyeyi okuma: %s\n", ses_oku ? "açık" : "kapalı");
    return;
  }
  if (g.startsWith("s ") || g.startsWith("S ")) { konus(g.c_str() + 2); return; }
  if (!llm_var) { Serial.println("LLM modeli yok: yalnız \"s <metin>\" çalışır."); return; }
  if (g == "b" || g == "B") { hiz_testi(); return; }
  int sec = -1, yer = -1, K = 1;
  if (g == "r" || g == "R") {
    sec = esp_random() % N_SECIM;
    yer = esp_random() % N_YER;
  } else {
    int a = -1, b = -1, y = -1, k = 1;
    if (sscanf(g.c_str(), "%d,%d %d %d", &a, &b, &y, &k) >= 3) sec = secim_bul(a - 1, b - 1);
    else if (sscanf(g.c_str(), "%d %d %d", &a, &y, &k) >= 2) sec = secim_bul(a - 1, -1);
    yer = y - 1;
    K = k < 1 ? 1 : k > 16 ? 16 : k;
  }
  if (sec < 0 || yer < 0 || yer >= N_YER) { Serial.println("Anlaşılmadı. Örnek: \"10 1\" ya da \"1,3 4\". \"?\" liste."); return; }
  hikaye(sec, yer, K);
}
