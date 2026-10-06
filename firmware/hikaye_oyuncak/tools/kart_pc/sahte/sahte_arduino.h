// Sahte Arduino/ESP32 ortamı: hikaye_oyuncak.ino bilgisayarda derlenip çalışsın (tools/kart_pc/kart_pc.cpp).
// Yalnız çizimin kullandığı kadarı: Serial (stdout/stdin), String, delay, esp_timer, esp_random, heap_caps (PSRAM
// ve SRAM sınırlı ve sayılır: KART_PSRAM / KART_SRAM bayt), esp_partition (partitions.csv'den; "model" ve "ses"
// bölümlerinin içeriği KART_MODEL / KART_SES dosyalarından, kalanı 0xFF), FreeRTOS görevleri (kurulamaz: tek
// çekirdek yolu), I2S ve akış tamponu (boş).
#pragma once
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <time.h>
#include <string>

// ---- zaman, rastgele ----
static inline int64_t esp_timer_get_time(void) {
  struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t);
  return (int64_t)t.tv_sec * 1000000 + t.tv_nsec / 1000;
}
static inline uint32_t esp_random(void) {  // rand()'dan bağımsız (örnekleyici rand() kullanır)
  static uint32_t x = 2463534242u;
  x ^= x << 13; x ^= x >> 17; x ^= x << 5;
  return x;
}
static inline void delay(uint32_t) {}

// ---- bellek ----
#define MALLOC_CAP_SPIRAM (1 << 10)
#define MALLOC_CAP_INTERNAL (1 << 11)
#define MALLOC_CAP_8BIT (1 << 2)
static size_t sahte_psram_sinir = 0, sahte_psram_dolu = 0, sahte_sram_sinir = 0, sahte_sram_dolu = 0;
static void sahte_bellek_kur(void) {
  const char *p = getenv("KART_PSRAM"), *s = getenv("KART_SRAM");
  sahte_psram_sinir = p ? strtoul(p, NULL, 0) : 8315000;  // docs/ESP32_BUTCE.md: kullanılabilir ≈8 315 000 B
  sahte_sram_sinir = s ? strtoul(s, NULL, 0) : 300000;
}
static inline void *heap_caps_malloc(size_t n, uint32_t caps) {
  if (!sahte_psram_sinir) sahte_bellek_kur();
  size_t *dolu = (caps & MALLOC_CAP_SPIRAM) ? &sahte_psram_dolu : &sahte_sram_dolu;
  size_t sinir = (caps & MALLOC_CAP_SPIRAM) ? sahte_psram_sinir : sahte_sram_sinir;
  size_t yuvarla = (n + 15) & ~(size_t)15;  // ayırıcı başlığı/hizası yerine kaba pay
  if (*dolu + yuvarla > sinir) return NULL;
  void *r = malloc(n ? n : 1);
  if (r) *dolu += yuvarla;
  return r;
}
static inline size_t heap_caps_get_free_size(uint32_t caps) {
  if (!sahte_psram_sinir) sahte_bellek_kur();
  return (caps & MALLOC_CAP_SPIRAM) ? sahte_psram_sinir - sahte_psram_dolu : sahte_sram_sinir - sahte_sram_dolu;
}

// ---- bölümler ----
typedef int esp_err_t;
#define ESP_OK 0
typedef enum { ESP_PARTITION_TYPE_APP = 0, ESP_PARTITION_TYPE_DATA = 1 } esp_partition_type_t;
typedef int esp_partition_subtype_t;
typedef int esp_partition_mmap_memory_t;
#define ESP_PARTITION_MMAP_DATA 0
typedef uint32_t esp_partition_mmap_handle_t;
typedef struct { char label[32]; int subtype; uint32_t address, size; } esp_partition_t;
static const esp_partition_t *esp_partition_find_first(esp_partition_type_t, esp_partition_subtype_t alt,
                                                       const char *label) {
  static esp_partition_t bolum[8];
  static int n = -1;
  if (n < 0) {  // partitions.csv: ad, tür, alt tür, adres, boyut
    n = 0;
    const char *yol = getenv("KART_BOLUMLER");
    FILE *f = fopen(yol ? yol : "partitions.csv", "r");
    if (!f) { perror("partitions.csv (KART_BOLUMLER)"); exit(2); }
    char satir[256];
    while (n < 8 && fgets(satir, sizeof satir, f)) {
      if (satir[0] == '#') continue;
      char ad[32], tur[32], at[32];
      unsigned adres, boy;
      if (sscanf(satir, " %31[^, ] , %31[^, ] , %31[^, ] , %x , %x", ad, tur, at, &adres, &boy) != 5) continue;
      esp_partition_t *b = &bolum[n++];
      snprintf(b->label, sizeof b->label, "%s", ad);
      b->subtype = (int)strtol(at, NULL, 0);
      b->address = adres; b->size = boy;
    }
    fclose(f);
  }
  for (int i = 0; i < n; i++)
    if (!strcmp(bolum[i].label, label) && bolum[i].subtype == alt) return &bolum[i];
  return NULL;
}
static inline esp_err_t esp_partition_mmap(const esp_partition_t *p, size_t ofs, size_t boy, int, const void **out,
                                           esp_partition_mmap_handle_t *) {
  const char *env = !strcmp(p->label, "model") ? "KART_MODEL" : !strcmp(p->label, "ses") ? "KART_SES" : NULL;
  uint8_t *b = (uint8_t *)malloc(boy);
  memset(b, 0xFF, boy);
  const char *yol = env ? getenv(env) : NULL;
  if (yol) {
    FILE *f = fopen(yol, "rb");
    if (!f) { perror(yol); exit(2); }
    size_t n = fread(b, 1, boy, f);
    if (fgetc(f) != EOF) { fprintf(stderr, "%s: dosya %s bölümüne sığmıyor (%zu B)\n", yol, p->label, boy); exit(2); }
    (void)n;
    fclose(f);
  }
  *out = b + ofs;
  return ESP_OK;
}

// ---- FreeRTOS (görev kurulamaz: çizim tek çekirdek yoluna düşer) ----
typedef void *TaskHandle_t;
typedef int BaseType_t;
#define pdPASS 1
#define pdFAIL 0
#define pdTRUE 1
#define portMAX_DELAY 0xFFFFFFFFu
static inline BaseType_t xTaskCreatePinnedToCore(void (*)(void *), const char *, uint32_t, void *, int, TaskHandle_t *,
                                                 int) { return pdFAIL; }
static inline TaskHandle_t xTaskGetCurrentTaskHandle(void) { return NULL; }
static inline uint32_t ulTaskNotifyTake(BaseType_t, uint32_t) { return 1; }
static inline void xTaskNotifyGive(TaskHandle_t) {}
typedef void *StreamBufferHandle_t;
typedef struct { int x; } StaticStreamBuffer_t;
static inline StreamBufferHandle_t xStreamBufferCreateStatic(size_t, size_t, uint8_t *b, StaticStreamBuffer_t *) { return b; }
static inline size_t xStreamBufferReceive(StreamBufferHandle_t, void *, size_t, uint32_t) { return 0; }
static inline size_t xStreamBufferSend(StreamBufferHandle_t, const void *, size_t n, uint32_t) { return n; }
static inline int xStreamBufferIsEmpty(StreamBufferHandle_t) { return 1; }

// ---- I2S ----
#define I2S_MODE_STD 0
#define I2S_DATA_BIT_WIDTH_16BIT 16
#define I2S_SLOT_MODE_MONO 1
#define I2S_STD_SLOT_BOTH 3
struct I2SClass {
  void setPins(int, int, int) {}
  bool begin(int, int, int, int, int) { return true; }
  size_t write(const uint8_t *, size_t n) { return n; }
};

// ---- String, Serial ----
struct String {
  std::string s;
  String(const std::string &x = "") : s(x) {}
  void trim() {
    size_t a = s.find_first_not_of(" \t\r\n"), b = s.find_last_not_of(" \t\r\n");
    s = a == std::string::npos ? "" : s.substr(a, b - a + 1);
  }
  size_t length() const { return s.size(); }
  bool operator==(const char *x) const { return s == x; }
  bool startsWith(const char *x) const { return s.compare(0, strlen(x), x) == 0; }
  const char *c_str() const { return s.c_str(); }
};
struct SahteSerial {
  std::string girdi;  // kart_pc.cpp doldurur
  void begin(int) {}
  int available() { return (int)girdi.size(); }
  String readStringUntil(char c) {
    size_t i = girdi.find(c);
    std::string r = girdi.substr(0, i);
    girdi.erase(0, i == std::string::npos ? girdi.size() : i + 1);
    return String(r);
  }
  size_t write(const void *b, size_t n) { return fwrite(b, 1, n, stdout); }
  void print(const char *x) { fputs(x, stdout); }
  void println(const char *x = "") { fputs(x, stdout); fputc('\n', stdout); }
  int printf(const char *f, ...) __attribute__((format(printf, 2, 3))) {
    va_list a; va_start(a, f); int r = vprintf(f, a); va_end(a); return r;
  }
};
static SahteSerial Serial;
