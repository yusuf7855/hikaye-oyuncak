// Sahte Arduino/ESP32 ortamı: hikaye_oyuncak.ino bilgisayarda derlenip çalışsın (tools/kart_pc/kart_pc.cpp).
// Yalnız çizimin kullandığı kadarı: Serial (stdout/stdin), String, delay, esp_timer, esp_random, heap_caps (PSRAM
// ve SRAM sınırlı ve sayılır: KART_PSRAM / KART_SRAM bayt), esp_partition (partitions.csv'den; "model" ve "ses"
// bölümlerinin içeriği KART_MODEL / KART_SES dosyalarından, kalanı 0xFF), FreeRTOS görevleri (kurulamaz: tek
// çekirdek yolu), I2S ve akış tamponu (boş).
// Ürün parçaları için: sahte zaman (delay ve hafif uyku saati ileri alır: sahte_zaman_ek_us), GPIO (sahte_pin[],
// pull-up'lı düğmeler 1 başlar), RGB LED (sahte_led), yazılabilir bölüm ("kuyruk": NOR flash gibi, yazma yalnız
// 1 -> 0, silme 4 KB; KART_KUYRUK dosyasına her değişiklikte yazılır = açılıştan açılışa kalır), hafif uyku (GPIO
// uyandırması sahte_pin'den; stderr'e "UYKU"), görev bekçisi (sayılır), esp_reset_reason (KART_SIFIRLAMA),
// Preferences (bellekte; KART_NVS dosyası verilirse ona yazılır).
#pragma once
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <time.h>
#include <string>

// ---- zaman, rastgele ----
static int64_t sahte_zaman_ek_us = 0;  // delay() ve hafif uyku saati ileri alır (gerçekte beklemeden)
static inline int64_t esp_timer_get_time(void) {
  struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t);
  return (int64_t)t.tv_sec * 1000000 + t.tv_nsec / 1000 + sahte_zaman_ek_us;
}
static inline uint32_t millis(void) { return (uint32_t)(esp_timer_get_time() / 1000); }
static inline uint32_t esp_random(void) {  // rand()'dan bağımsız (örnekleyici rand() kullanır)
  static uint32_t x = 2463534242u;
  x ^= x << 13; x ^= x >> 17; x ^= x << 5;
  return x;
}
static inline void delay(uint32_t ms) { sahte_zaman_ek_us += (int64_t)ms * 1000; }

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
#define ESP_FAIL -1
#define ESP_ERR_INVALID_ARG 0x102
#define ESP_ERR_INVALID_STATE 0x103
typedef enum { ESP_PARTITION_TYPE_APP = 0, ESP_PARTITION_TYPE_DATA = 1 } esp_partition_type_t;
typedef int esp_partition_subtype_t;
typedef int esp_partition_mmap_memory_t;
#define ESP_PARTITION_MMAP_DATA 0
typedef uint32_t esp_partition_mmap_handle_t;
typedef struct { char label[32]; int subtype; uint32_t address, size; } esp_partition_t;
static esp_partition_t sahte_bolum[8];
static uint8_t *sahte_bolum_veri[8];  // yazılabilir bölümlerin içeriği (kuyruk)
static const esp_partition_t *esp_partition_find_first(esp_partition_type_t, esp_partition_subtype_t alt,
                                                       const char *label) {
  esp_partition_t *bolum = sahte_bolum;
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
// Yazılabilir bölüm (kuyruk): içerik KART_KUYRUK dosyasından (yoksa 0xFF), her yazma/silmede dosyaya geri yazılır.
// KART_FLASH_KES=N: N bayt yazıldıktan sonra yazmalar tutmaz (güç kesilmesi taklidi).
static long sahte_flash_yazilan = 0, sahte_flash_sil_n = 0;
static uint8_t *sahte_bolum_ac(const esp_partition_t *p) {
  int i = (int)(p - sahte_bolum);
  if (!sahte_bolum_veri[i]) {
    uint8_t *b = (uint8_t *)malloc(p->size);
    memset(b, 0xFF, p->size);
    const char *yol = getenv("KART_KUYRUK");
    FILE *f = yol ? fopen(yol, "rb") : NULL;
    if (f) { size_t n = fread(b, 1, p->size, f); (void)n; fclose(f); }
    sahte_bolum_veri[i] = b;
  }
  return sahte_bolum_veri[i];
}
static void sahte_bolum_kaydet(const esp_partition_t *p) {
  const char *yol = getenv("KART_KUYRUK");
  if (!yol) return;
  FILE *f = fopen(yol, "wb");
  if (!f) { perror(yol); exit(2); }
  fwrite(sahte_bolum_ac(p), 1, p->size, f);
  fclose(f);
}
static inline esp_err_t esp_partition_read(const esp_partition_t *p, size_t ofs, void *buf, size_t n) {
  if (ofs + n > p->size) return ESP_ERR_INVALID_ARG;
  memcpy(buf, sahte_bolum_ac(p) + ofs, n);
  return ESP_OK;
}
static inline esp_err_t esp_partition_write(const esp_partition_t *p, size_t ofs, const void *buf, size_t n) {
  if (ofs + n > p->size) return ESP_ERR_INVALID_ARG;
  const char *kes = getenv("KART_FLASH_KES");
  uint8_t *b = sahte_bolum_ac(p);
  for (size_t i = 0; i < n; i++, sahte_flash_yazilan++) {
    if (kes && sahte_flash_yazilan >= atol(kes)) break;
    b[ofs + i] &= ((const uint8_t *)buf)[i];  // NOR flash: yalnız 1 -> 0
  }
  sahte_bolum_kaydet(p);
  return ESP_OK;
}
static inline esp_err_t esp_partition_erase_range(const esp_partition_t *p, size_t ofs, size_t n) {
  if (ofs % 4096 || n % 4096 || ofs + n > p->size) return ESP_ERR_INVALID_ARG;
  memset(sahte_bolum_ac(p) + ofs, 0xFF, n);
  sahte_flash_sil_n += (long)(n / 4096);
  sahte_bolum_kaydet(p);
  return ESP_OK;
}

// ---- FreeRTOS (görev kurulamaz: çizim tek çekirdek yoluna düşer) ----
typedef void *TaskHandle_t;
typedef int BaseType_t;
#define pdPASS 1
#define pdFAIL 0
#define pdTRUE 1
#define portMAX_DELAY 0xFFFFFFFFu
// Görevler kurulamaz (çizim tek çekirdek yoluna, düğmeleri ana döngüde örneklemeye düşer); yalnız çalma görevi
// "kurulmuş" sayılır ama çalışmaz: akış tamponu her şeyi kabul edip atar (ses yolu bilgisayarda da koşsun).
static inline BaseType_t xTaskCreatePinnedToCore(void (*)(void *), const char *ad, uint32_t, void *, int,
                                                 TaskHandle_t *, int) { return !strcmp(ad, "cal") ? pdPASS : pdFAIL; }
static inline TaskHandle_t xTaskGetCurrentTaskHandle(void) { return NULL; }
static inline uint32_t ulTaskNotifyTake(BaseType_t, uint32_t) { return 1; }
static inline void xTaskNotifyGive(TaskHandle_t) {}
typedef void *StreamBufferHandle_t;
typedef struct { int x; } StaticStreamBuffer_t;
static inline StreamBufferHandle_t xStreamBufferCreateStatic(size_t, size_t, uint8_t *b, StaticStreamBuffer_t *) { return b; }
static inline size_t xStreamBufferReceive(StreamBufferHandle_t, void *, size_t, uint32_t) { return 0; }
static inline size_t xStreamBufferSend(StreamBufferHandle_t, const void *, size_t n, uint32_t) { return n; }
static inline int xStreamBufferIsEmpty(StreamBufferHandle_t) { return 1; }
#define pdMS_TO_TICKS(ms) (ms)
static inline void vTaskDelay(uint32_t t) { delay(t); }

// ---- GPIO, LED ----
#define LOW 0
#define HIGH 1
#define INPUT 0x01
#define OUTPUT 0x03
#define INPUT_PULLUP 0x05
static int sahte_pin[64] = {0};
static bool sahte_pin_kuruldu = false;
static inline void sahte_pin_kur(void) {
  if (sahte_pin_kuruldu) return;
  for (int i = 0; i < 64; i++) sahte_pin[i] = 1;  // pull-up: basılı değil
  sahte_pin_kuruldu = true;
}
static inline void pinMode(int, int) { sahte_pin_kur(); }
// Zamanlı seviye değişimi (kart_pc "#pin_sonra P V MS"): üretim sürerken düğmeye basmak için
static struct { int pin, deger; int64_t us; } sahte_zamanli[16];
static int sahte_zamanli_n = 0;
static inline void sahte_zamanli_uygula(void) {  // vakti gelenler zaman sırasıyla
  int64_t simdi = esp_timer_get_time();
  for (;;) {
    int en = -1;
    for (int i = 0; i < sahte_zamanli_n; i++)
      if (sahte_zamanli[i].us <= simdi && (en < 0 || sahte_zamanli[i].us < sahte_zamanli[en].us)) en = i;
    if (en < 0) return;
    sahte_pin[sahte_zamanli[en].pin] = sahte_zamanli[en].deger;
    for (int i = en + 1; i < sahte_zamanli_n; i++) sahte_zamanli[i - 1] = sahte_zamanli[i];
    sahte_zamanli_n--;
  }
}
static inline int digitalRead(int p) {
  sahte_pin_kur();
  sahte_zamanli_uygula();
  return (p >= 0 && p < 64) ? sahte_pin[p] : 1;
}
static inline void digitalWrite(int p, int v) { sahte_pin_kur(); if (p >= 0 && p < 64) sahte_pin[p] = v; }
#define ESP_ARDUINO_VERSION_MAJOR 3
#define RGB_BUILTIN 48
static uint8_t sahte_led[3];
static inline void rgbLedWrite(int, uint8_t r, uint8_t g, uint8_t b) { sahte_led[0] = r; sahte_led[1] = g; sahte_led[2] = b; }

// ---- görev bekçisi ----
typedef struct { uint32_t timeout_ms, idle_core_mask; bool trigger_panic; } esp_task_wdt_config_t;
static long sahte_bekci_besle = 0;
static inline esp_err_t esp_task_wdt_reconfigure(const esp_task_wdt_config_t *) { return ESP_OK; }
static inline esp_err_t esp_task_wdt_init(const esp_task_wdt_config_t *) { return ESP_OK; }
static inline esp_err_t esp_task_wdt_add(TaskHandle_t) { return ESP_OK; }
static inline esp_err_t esp_task_wdt_reset(void) { sahte_bekci_besle++; return ESP_OK; }

// ---- yeniden başlama sebebi ----
typedef enum {
  ESP_RST_UNKNOWN, ESP_RST_POWERON, ESP_RST_EXT, ESP_RST_SW, ESP_RST_PANIC, ESP_RST_INT_WDT, ESP_RST_TASK_WDT,
  ESP_RST_WDT, ESP_RST_DEEPSLEEP, ESP_RST_BROWNOUT, ESP_RST_SDIO
} esp_reset_reason_t;
static inline esp_reset_reason_t esp_reset_reason(void) {
  const char *e = getenv("KART_SIFIRLAMA");
  return e ? (esp_reset_reason_t)atoi(e) : ESP_RST_POWERON;
}

// ---- hafif uyku ----
typedef int gpio_num_t;
#define GPIO_INTR_LOW_LEVEL 4
#define UART_NUM_0 0
typedef enum { ESP_SLEEP_WAKEUP_UNDEFINED = 0, ESP_SLEEP_WAKEUP_TIMER = 4, ESP_SLEEP_WAKEUP_GPIO = 7 } esp_sleep_wakeup_cause_t;
static uint64_t sahte_uyku_sure_us = 0;
static bool sahte_uyandir[64];
static esp_sleep_wakeup_cause_t sahte_uyanma = ESP_SLEEP_WAKEUP_UNDEFINED;
static int sahte_uyku_n = 0;
static inline esp_err_t esp_sleep_enable_timer_wakeup(uint64_t us) { sahte_uyku_sure_us = us; return ESP_OK; }
static inline esp_err_t gpio_wakeup_enable(gpio_num_t p, int) { if (p >= 0 && p < 64) sahte_uyandir[p] = true; return ESP_OK; }
static inline esp_err_t gpio_wakeup_disable(gpio_num_t p) { if (p >= 0 && p < 64) sahte_uyandir[p] = false; return ESP_OK; }
static inline esp_err_t esp_sleep_enable_gpio_wakeup(void) { return ESP_OK; }
static inline esp_err_t uart_set_wakeup_threshold(int, int) { return ESP_OK; }
static inline esp_err_t esp_sleep_enable_uart_wakeup(int) { return ESP_OK; }
static inline esp_err_t esp_light_sleep_start(void) {
  sahte_pin_kur();
  sahte_uyku_n++;
  int64_t bas = esp_timer_get_time(), son = bas + (int64_t)sahte_uyku_sure_us;
  for (int p = 0; p < 64; p++)
    if (sahte_uyandir[p] && sahte_pin[p] == 0) {
      sahte_uyanma = ESP_SLEEP_WAKEUP_GPIO;
      fprintf(stderr, "UYKU 0 ms (GPIO %d)\n", p);
      return ESP_OK;
    }
  for (int i = 0; i < sahte_zamanli_n; i++)  // uyku sırasında zamanlı basış: o anda uyan
    if (sahte_zamanli[i].deger == 0 && sahte_uyandir[sahte_zamanli[i].pin] && sahte_zamanli[i].us < son)
      son = sahte_zamanli[i].us < bas ? bas : sahte_zamanli[i].us, sahte_uyanma = ESP_SLEEP_WAKEUP_GPIO;
  if (son < bas + (int64_t)sahte_uyku_sure_us) {
    sahte_zaman_ek_us += son - bas;
    fprintf(stderr, "UYKU %lld ms (GPIO)\n", (long long)((son - bas) / 1000));
    return ESP_OK;
  }
  sahte_zaman_ek_us += (int64_t)sahte_uyku_sure_us;
  sahte_uyanma = ESP_SLEEP_WAKEUP_TIMER;
  fprintf(stderr, "UYKU %llu ms\n", (unsigned long long)(sahte_uyku_sure_us / 1000));
  return ESP_OK;
}
static inline esp_sleep_wakeup_cause_t esp_sleep_get_wakeup_cause(void) { return sahte_uyanma; }

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
  char operator[](size_t i) const { return i < s.size() ? s[i] : 0; }
  bool startsWith(const char *x) const { return s.compare(0, strlen(x), x) == 0; }
  const char *c_str() const { return s.c_str(); }
};
struct SahteSerial {
  std::string girdi;  // kart_pc.cpp doldurur
  void begin(int) {}
  void flush() { fflush(stdout); }
  explicit operator bool() const { return true; }
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

// ---- Preferences (NVS): bellekte; KART_NVS dosyası verilirse "anahtar değer" satırları olarak ona yazılır ----
#include <map>
struct Preferences {
  std::map<std::string, long> m;
  bool begin(const char *, bool) {
    const char *yol = getenv("KART_NVS");
    FILE *f = yol ? fopen(yol, "r") : NULL;
    if (f) {
      char k[64]; long v;
      while (fscanf(f, "%63s %ld", k, &v) == 2) m[k] = v;
      fclose(f);
    }
    return true;
  }
  void kaydet() {
    const char *yol = getenv("KART_NVS");
    FILE *f = yol ? fopen(yol, "w") : NULL;
    if (!f) return;
    for (auto &kv : m) fprintf(f, "%s %ld\n", kv.first.c_str(), kv.second);
    fclose(f);
  }
  long al(const char *k, long v) { auto i = m.find(k); return i == m.end() ? v : i->second; }
  void koy(const char *k, long v) { m[k] = v; kaydet(); }
  uint8_t getUChar(const char *k, uint8_t v) { return (uint8_t)al(k, v); }
  int8_t getChar(const char *k, int8_t v) { return (int8_t)al(k, v); }
  bool getBool(const char *k, bool v) { return al(k, v) != 0; }
  size_t putUChar(const char *k, uint8_t v) { koy(k, v); return 1; }
  size_t putChar(const char *k, int8_t v) { koy(k, v); return 1; }
  size_t putBool(const char *k, bool v) { koy(k, v); return 1; }
};
