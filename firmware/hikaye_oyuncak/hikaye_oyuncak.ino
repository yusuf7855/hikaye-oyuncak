// Hikâye Oyuncağı — kart testi (ESP32-S3 N16R8).
//
// Model flash'taki "model" bölümünde (0x110000), çekirdek açılışta PSRAM'e int8 olarak kopyalanır; head (tied
// gömme) 4-bit olarak flash'ta kalır: C2'de çekirdek + head int8 + float KV 8 MB PSRAM'e sığmıyor. Bağlam 224
// token (hikâye + plan + başlık ≈ 190). Örnekleme bilgisayardaki gen/uret.py ile aynı (runtime/ornekle.h):
// sıcaklık 0.5, top-k 40, tekrar cezası 1.1, plan modu, gövdede satır sonu yasağı, seçilmeyen figür isimleri yasak.
//
// Seri monitör (115200): "1 3" = 1. figür, 3. yer | "1,5 3" = iki figür | "r" = rastgele | "?" = liste.
// Sona aday sayısı: "1 3 4" = 4 aday üret, hafif seçiciyle en iyisini yaz (puanla()). Aday sayısı yoksa (1) canlı
// yazar. Kart her hikâyeden sonra token/s ve süreyi yazar.

#include "esp_partition.h"
#include "esp_heap_caps.h"
#include "esp_timer.h"
#include "esp_random.h"

#define LLM_INT8_ACT 1
#define LLM_PROFILE 1
#define LLM_PROFILE_NOW() esp_timer_get_time()
#include "generated/llm.h"
#define ORNEKLE_RASTGELE() ((double)esp_random() / 4294967295.0)
#include "generated/ornekle.h"
#include "generated/vocab.h"
#include "generated/istemler.h"

static const int BAGLAM = 224;       // KV önbelleği: 10 katman x 224 x 160 x 4 B x 2 = 2.9 MB
static const int N_URET = 240;       // en fazla bu kadar token (plan + gövde)
static const float SICAKLIK = 0.5f, TEKRAR = 1.1f;
static const int TOP_K = 40;

Model model;
Scratch s;
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

// ---- iki çekirdekli int8 matvec (esp32_tinystories ile aynı) ----
static TaskHandle_t worker_h, main_h;
static const QT *job_t;
static const int8_t *job_xq;
static float job_xs;
static float *job_y;
static int job_split;
static void worker_main(void *) {
  for (;;) {
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    matvec_i8_range(job_t, job_xq, job_xs, job_y, 0, job_split);
    xTaskNotifyGive(main_h);
  }
}
static void matvec_par(const QT *t, const float *x, float *y) {
  static int8_t xq[LLM_Q8_MAX_INPUT];
  float xs;
  if (t->w8 == NULL || t->rows < 128) { MATVEC(t, x, y); return; }
  quantize_act(x, t->cols, xq, &xs);
  job_t = t; job_xq = xq; job_xs = xs; job_y = y; job_split = t->rows / 2;
  xTaskNotifyGive(worker_h);
  matvec_i8_range(t, xq, xs, y, job_split, t->rows);
  ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
}

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
  Serial.println("Sona aday sayısı eklenirse en iyisi seçilir: \"10 1 4\" (4 aday). Aday yoksa canlı yazar.\n");
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

struct Aday { int n, n_plan; float lp; bool bitti, plan_bozuk; };

// Bir aday üretir: aday_tok'a plan + gövde token'ları (EOT hariç). canli: token'lar üretildikçe seriye yazılır.
static Aday aday_uret(int sec, int yer, bool canli) {
  int ny = YASAK_OFF[sec + 1] - YASAK_OFF[sec];
  if (ny > 128) ny = 128;
  for (int i = 0; i < ny; i++) yasak[i] = YASAK_ID[YASAK_OFF[sec] + i];
  govde_yasak[0] = GOVDE_YASAK[0]; govde_yasak[1] = GOVDE_YASAK[1];
  OrnAyar ayar = {SICAKLIK, TOP_K, TEKRAR, yasak, ny, govde_yasak, 2, idx, olas};
  OrnDurum st; orn_sifirla(&st);
  int k = sec * N_YER + yer, pos = 0, tok = 0;
  for (int i = ISTEM_OFF[k]; i < ISTEM_OFF[k + 1]; i++) {  // istem tekrar penceresine girer (gen.c varsayılanı)
    tok = ISTEM_ID[i];
    orn_ekle(&st, tok);
    llm_forward(&model, tok, pos++, &s);
  }
  orn_plan_baslat(&st, NL_ID);
  Aday a = {0, 0, 0.f, false, false};
  double lp = 0; int n_lp = 0;
  if (canli) Serial.print("Sorun:");
  for (int step = 0; step < N_URET && pos < model.c.seq_len; step++) {
    bool govdede = st.govde;
    tok = orn_adim(&ayar, &st, s.logits, model.out_vocab);
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
static float puanla(const Aday &a, int sec) {
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

static void hikaye(int sec, int yer, int K) {
  Serial.printf("\n=== %s", FIGUR_AD[SECIM_A[sec]]);
  if (SECIM_B[sec] >= 0) Serial.printf(" + %s", FIGUR_AD[SECIM_B[sec]]);
  Serial.printf(" | %s | %d aday ===\n", YER_AD[yer], K);
  int64_t t0 = esp_timer_get_time();
  int toplam = 0, en_n = 0; float en_p = -1e30f;
  for (int j = 0; j < K; j++) {
    Aday a = aday_uret(sec, yer, K == 1);
    toplam += a.n + (a.bitti ? 1 : 0);
    float p = puanla(a, sec);
    if (K > 1) Serial.printf("aday %d/%d: %d token, güven %.3f, %s -> puan %.2f\n", j + 1, K, a.n, a.lp,
                             a.plan_bozuk ? "plan bozuk" : a.bitti ? "bitti" : "yarım", p);
    if (p > en_p) { en_p = p; en_n = a.n; memcpy(en_tok, aday_tok, a.n * sizeof(int16_t)); }
  }
  if (K > 1) {
    Serial.print("\nSorun:");
    for (int i = 0; i < en_n; i++) yaz(en_tok[i]);
  }
  float sn = (esp_timer_get_time() - t0) / 1e6f;
  Serial.printf("\n\n--- %d aday, toplam %d token %.1f s = %.2f token/s ---\n", K, toplam, sn, toplam / sn);
  Serial.println("Yeni hikâye için figür ve yer yazın (\"?\" liste).");
}

void setup() {
  Serial.begin(115200);
  delay(1500);
  Serial.println("\n=== Hikâye Oyuncağı — kart testi ===");
  const esp_partition_t *part = esp_partition_find_first(ESP_PARTITION_TYPE_DATA,
                                                         (esp_partition_subtype_t)0x40, "model");
  if (!part) { Serial.println("model bölümü yok (partitions.csv?)"); return; }
  const void *base;
  esp_partition_mmap_handle_t h;
  if (esp_partition_mmap(part, 0, part->size, ESP_PARTITION_MMAP_DATA, &base, &h) != ESP_OK) {
    Serial.println("mmap başarısız"); return;
  }
  if (llm_load((const uint8_t *)base, &model)) { Serial.println("model okunamadı (model.bin yüklendi mi?)"); return; }
  if (model.c.seq_len > BAGLAM) model.c.seq_len = BAGLAM;  // RoPE konumdan hesaplanır; S yalnız KV adımı
  Cfg *c = &model.c;
  Serial.printf("model: V=%d D=%d L=%d H=%d F=%d P=%d bağlam=%d\n", model.out_vocab, c->dim, c->n_layers,
                c->n_heads, c->ffn, c->ple_dim, c->seq_len);
  if (VOCAB_N != model.out_vocab) {
    Serial.printf("HATA: tokenizer/model uyuşmuyor: vocab.h %d, model %d\n", VOCAB_N, model.out_vocab);
    return;
  }
  alloc_scratch();
  int want = llm_core_stage_count(&model);
  int staged = llm_stage_core_int8_alloc(&model, ps);
  if (staged != want) { Serial.printf("HATA: çekirdek %d/%d tensör PSRAM'e kopyalandı\n", staged, want); while (1) delay(1000); }
  Serial.printf("PSRAM: çekirdek int8 + KV + logits = %.2f MB; head 4-bit flash'ta\n", psram_used / 1048576.0);

  main_h = xTaskGetCurrentTaskHandle();
  if (xTaskCreatePinnedToCore(worker_main, "mv", 4096, NULL, 2, &worker_h, 0) == pdPASS) {
    model.layer_matvec = matvec_par;
    model.head_matvec = matvec_par;
  }
  {
    const uint8_t *img = (const uint8_t *)base;
    uint32_t fp = 2166136261u;
    for (size_t i = 0; i < model.image_bytes; i++) { fp ^= img[i]; fp *= 16777619u; }
    Serial.printf("model.bin: %u B, parmak izi fp=%08x\n", (unsigned)model.image_bytes, fp);
  }
  Serial.printf("boş: SRAM %.0f KB | PSRAM %.2f MB\n", heap_caps_get_free_size(MALLOC_CAP_INTERNAL) / 1024.0,
                heap_caps_get_free_size(MALLOC_CAP_SPIRAM) / 1048576.0);
  liste();
}

void loop() {
  if (!Serial.available()) { delay(20); return; }
  String g = Serial.readStringUntil('\n');
  g.trim();
  if (g.length() == 0) return;
  if (g == "?") { liste(); return; }
  int sec = -1, yer = -1, K = 1;
  if (g == "r" || g == "R") {
    sec = esp_random() % N_SECIM;
    yer = esp_random() % N_YER;
  } else {
    int a = -1, b = -1, y = -1, k = 1;
    if (sscanf(g.c_str(), "%d,%d %d %d", &a, &b, &y, &k) >= 3) sec = secim_bul(a - 1, b - 1);
    else if (sscanf(g.c_str(), "%d %d %d", &a, &y, &k) >= 2) sec = secim_bul(a - 1, -1);
    yer = y - 1;
    K = k < 1 ? 1 : k > 8 ? 8 : k;
  }
  if (sec < 0 || yer < 0 || yer >= N_YER) { Serial.println("Anlaşılmadı. Örnek: \"10 1\" ya da \"1,3 4\". \"?\" liste."); return; }
  hikaye(sec, yer, K);
}
