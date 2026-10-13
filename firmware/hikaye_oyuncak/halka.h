// Stand halkası (NeoPixel, WS2812B uyumlu): durumdan kareye. Donanımsız saf C; sürücü (.ino) kareyi RMT ile yollar.
//
// Halkanın bir "taban" durumu (uzun süren: boşta, okuma, uyku ...) ve üstüne gelen kısa bir "üst" durumu (dinliyorum,
// komut anlaşıldı/anlaşılmadı, ses düzeyi) vardır; üst durum süresi dolunca taban görünür. halka_ciz() zamana (ms)
// göre kareyi hesaplar: ana döngüden ya da ayrı düşük öncelikli görevden çağrılabilir (LLM ve ses beklemez).
// Davranışlar (docs/URUN_TANIMI.md "Halka"):
//   açılış      gökkuşağı tek tur, sonra söner (sonra boşta)
//   boşta       çok sönük nefes alan beyaz (nefes ayarı kapalıysa sönük)
//   dolma       figür renginde halka 0,6 s'de dolar, dolu kalır
//   okuma       figür renginde; okunan cümle oranı kadar LED dolu, kalanı sönük; parlaklık konuşma sesiyle dalgalanır
//   hazırlık    hazır hikâye yokken canlı yazılıyor: figür renginde dönen nokta
//   arka plan   arka planda hikâye hazırlanıyor: çok sönük, yavaş dönen figür rengi nokta
//   oyuncak     oyuncak standda, boşta: figür renginde sönük, yavaş nefes
//   gece        ninni modu (gece figürü): gece mavisi, yavaş parıldayan rastgele "yıldızlar"; sönme başlatılınca
//               60 s'de yavaşça söner
//   ayar        turkuaz nefes
//   hata        kırmızı yanıp sönme
//   üst: dinle  beyaz dönen nokta | onay: kısa yeşil yanıp sönme | anlaşılmadı: kısa turuncu | ses: 0..maks beyaz LED
// Parlaklık: her kanal x HALKA tavanı (%25) x ayar (%0..100); toplam akım tahmini sınırı (600 mA) aşarsa kare kısılır.
#pragma once
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define HALKA_MAKS 64
#ifndef HALKA_LED_MA
#define HALKA_LED_MA 20        // LED başına kanal başına tam parlaklık akımı (mA)
#endif

enum { HT_KAPALI, HT_ACILIS, HT_BOSTA, HT_DOLMA, HT_OKUMA, HT_HAZIRLA, HT_ARKA, HT_GECE, HT_AYAR, HT_HATA, HT_OYUNCAK,
       HT_N };
enum { HU_YOK, HU_DINLE, HU_ONAY, HU_ANLASILMADI, HU_SES, HU_N };
static const char *const HT_AD[HT_N] = {"kapali", "acilis", "bosta", "dolma", "okuma", "hazirlik", "arka", "gece",
                                        "ayar", "hata", "oyuncak"};
static const char *const HU_AD[HU_N] = {"-", "dinle", "onay", "anlasilmadi", "ses"};

#define HALKA_ACILIS_MS 1500   // gökkuşağı turu
#define HALKA_ACILIS_SON_MS 400 // ardından sönme
#define HALKA_DOLMA_MS 600
#define HALKA_ONAY_MS 480      // iki kısa yanıp sönme
#define HALKA_SES_MS 2000
#define HALKA_SONME_MS 60000

typedef struct {
  int n;                     // LED sayısı
  uint8_t taban, ust;
  uint32_t taban_ms, ust_ms, ust_sure;
  uint8_t renk[3];           // figür rengi (dolma, okuma, hazırlık, arka plan)
  uint16_t pay, payda;       // okuma ilerlemesi: okunan / toplam cümle
  uint8_t ses;               // konuşma sesi 0..255 (okurken dalgalanma)
  uint8_t duzey, maks;       // ses düzeyi göstergesi
  uint8_t sinir;             // tavan, % (HALKA_PARLAKLIK_SINIR)
  uint8_t parlaklik;         // ayar, % (0: halka kapalı)
  uint16_t akim_sinir;       // mA
  uint8_t nefes;             // boşta nefes açık mı
  uint32_t sonme_ms;         // gece: sönmenin başladığı an (0 yok)
  uint16_t akim_ma;          // son karenin akım tahmini (kısılmış)
} Halka;

static inline void halka_kur(Halka *h, int n, int sinir, int akim_sinir) {
  memset(h, 0, sizeof *h);
  h->n = n < 1 ? 1 : n > HALKA_MAKS ? HALKA_MAKS : n;
  h->sinir = (uint8_t)sinir;
  h->akim_sinir = (uint16_t)akim_sinir;
  h->parlaklik = 100;
  h->nefes = 1;
  h->payda = 1;
}

static inline void halka_taban(Halka *h, int durum, uint32_t ms) {
  if (h->taban == durum && durum != HT_DOLMA && durum != HT_ACILIS) return;
  h->taban = (uint8_t)durum;
  h->taban_ms = ms;
  if (durum != HT_GECE) h->sonme_ms = 0;
}
static inline void halka_ust(Halka *h, int ust, uint32_t ms, uint32_t sure) {
  h->ust = (uint8_t)ust;
  h->ust_ms = ms;
  h->ust_sure = sure;
}
static inline void halka_renk(Halka *h, const uint8_t rgb[3]) { memcpy(h->renk, rgb, 3); }
static inline void halka_ilerleme(Halka *h, int pay, int payda) {
  h->payda = (uint16_t)(payda < 1 ? 1 : payda);
  h->pay = (uint16_t)(pay < 0 ? 0 : pay > h->payda ? h->payda : pay);
}

// Okuma ilerlemesinde dolu LED sayısı
static inline int halka_dolu(const Halka *h) { return h->n * h->pay / h->payda; }

// Sözde rastgele (yıldızlar): durumsuz karıştırıcı, kare zamandan hesaplanır (bilgisayarda ve kartta aynı)
static inline uint32_t halka_karistir(uint32_t x) {
  x ^= x >> 16; x *= 0x7feb352du; x ^= x >> 15; x *= 0x846ca68bu; x ^= x >> 16;
  return x;
}

static inline void halka_hsv(float hue, uint8_t out[3]) {  // hue 0..1, tam doygun, tam parlak
  float x = hue * 6.f;
  int i = (int)x % 6;
  float f = x - floorf(x);
  uint8_t q = (uint8_t)(255 * (1 - f)), t = (uint8_t)(255 * f);
  const uint8_t r[6] = {255, q, 0, 0, t, 255}, g[6] = {t, 255, 255, q, 0, 0}, b[6] = {0, 0, t, 255, 255, q};
  out[0] = r[i]; out[1] = g[i]; out[2] = b[i];
}

static inline void halka_koy(uint8_t k[3], const uint8_t c[3], float f) {
  if (f < 0) f = 0;
  if (f > 1) f = 1;
  for (int i = 0; i < 3; i++) k[i] = (uint8_t)(c[i] * f + 0.5f);
}

// Dönen nokta: baş tam, kuyrukta azalan
static inline void halka_nokta(const Halka *h, uint8_t (*k)[3], const uint8_t c[3], float tur, float bas, float zemin) {
  int n = h->n, b = ((int)(tur * n) % n + n) % n;
  for (int i = 0; i < n; i++) halka_koy(k[i], c, zemin);
  static const float KUYRUK[4] = {1.f, .45f, .2f, .08f};
  for (int j = 0; j < 4 && j < n; j++) halka_koy(k[(b - j + n) % n], c, bas * KUYRUK[j] > zemin ? bas * KUYRUK[j] : zemin);
}

// Bir kare (RGB, kısılmış). Süresi dolan üst durumu ve biten açılışı da ilerletir.
static inline void halka_ciz(Halka *h, uint32_t ms, uint8_t (*k)[3]) {
  static const uint8_t BEYAZ[3] = {255, 255, 255}, YESIL[3] = {0, 255, 40}, TURUNCU[3] = {255, 110, 0},
                       KIRMIZI[3] = {255, 0, 0}, YILDIZ[3] = {200, 210, 255}, TURKUAZ[3] = {0, 229, 200};
  const float PI2 = 6.2831853f;
  int n = h->n;
  uint32_t t = ms - h->taban_ms;
  if (h->taban == HT_ACILIS && t >= HALKA_ACILIS_MS + HALKA_ACILIS_SON_MS) { halka_taban(h, HT_BOSTA, ms); t = 0; }
  if (h->ust != HU_YOK && ms - h->ust_ms >= h->ust_sure) h->ust = HU_YOK;
  memset(k, 0, (size_t)n * 3);
  switch (h->taban) {
    case HT_ACILIS: {
      float f = t < HALKA_ACILIS_MS ? 1.f : 1.f - (float)(t - HALKA_ACILIS_MS) / HALKA_ACILIS_SON_MS;
      int yanan = t < HALKA_ACILIS_MS ? (int)((int64_t)n * t / HALKA_ACILIS_MS) + 1 : n;
      for (int i = 0; i < yanan && i < n; i++) { uint8_t c[3]; halka_hsv((float)i / n, c); halka_koy(k[i], c, f); }
      break;
    }
    case HT_BOSTA:
      if (h->nefes)
        for (int i = 0; i < n; i++) halka_koy(k[i], BEYAZ, .04f + .08f * (.5f - .5f * cosf(PI2 * (float)(t % 4000) / 4000.f)));
      break;
    case HT_DOLMA: {
      int dolu = t >= HALKA_DOLMA_MS ? n : (int)((int64_t)n * t / HALKA_DOLMA_MS) + 1;
      for (int i = 0; i < dolu && i < n; i++) halka_koy(k[i], h->renk, 1.f);
      break;
    }
    case HT_OKUMA: {
      int dolu = halka_dolu(h);
      float m = .8f + .2f * h->ses / 255.f;
      for (int i = 0; i < n; i++) halka_koy(k[i], h->renk, i < dolu ? m : .12f);
      break;
    }
    case HT_HAZIRLA: halka_nokta(h, k, h->renk, (float)(t % 1500) / 1500.f, 1.f, .08f); break;
    case HT_ARKA: halka_nokta(h, k, h->renk, (float)(t % 8000) / 8000.f, .15f, 0.f); break;
    case HT_GECE: {  // gece mavisi zemin + yıldızlar: her LED kendi dönemiyle (3-6 s), dönemlerin ~üçte birinde parlar
      float f = 1.f;
      if (h->sonme_ms) {
        uint32_t s = ms - h->sonme_ms;
        f = s >= HALKA_SONME_MS ? 0.f : 1.f - (float)s / HALKA_SONME_MS;
      }
      for (int i = 0; i < n; i++) {
        uint32_t d = 3000 + halka_karistir((uint32_t)i * 7919u) % 3000, tur = (ms + halka_karistir((uint32_t)i)) / d;
        float y = 0.f;
        if (halka_karistir((uint32_t)i * 131u + tur * 2654435761u) % 3 == 0) {
          float x = (float)((ms + halka_karistir((uint32_t)i)) % d) / d;  // 0..1: yavaşça yanıp söner
          y = .5f - .5f * cosf(PI2 * x);
        }
        uint8_t c[3];
        for (int j = 0; j < 3; j++) c[j] = (uint8_t)(h->renk[j] * .2f * (1.f - y) + YILDIZ[j] * .7f * y);
        halka_koy(k[i], c, f);
      }
      break;
    }
    case HT_OYUNCAK:
      for (int i = 0; i < n; i++) halka_koy(k[i], h->renk, .1f + .06f * (.5f - .5f * cosf(PI2 * (float)(t % 5000) / 5000.f)));
      break;
    case HT_AYAR:
      for (int i = 0; i < n; i++) halka_koy(k[i], TURKUAZ, .25f + .75f * (.5f - .5f * cosf(PI2 * (float)(t % 2500) / 2500.f)));
      break;
    case HT_HATA:
      if ((t / 400) % 2 == 0) for (int i = 0; i < n; i++) halka_koy(k[i], KIRMIZI, 1.f);
      break;
    default: break;
  }
  uint32_t u = ms - h->ust_ms;
  switch (h->ust) {
    case HU_DINLE: {
      for (int i = 0; i < n; i++) for (int c = 0; c < 3; c++) k[i][c] = (uint8_t)(k[i][c] * 3 / 10);
      int b = (int)((int64_t)n * (u % 1200) / 1200);
      static const float KY[3] = {1.f, .4f, .15f};
      for (int j = 0; j < 3 && j < n; j++) halka_koy(k[(b - j + n) % n], BEYAZ, KY[j]);
      break;
    }
    case HU_ONAY:
    case HU_ANLASILMADI:
      for (int i = 0; i < n; i++) halka_koy(k[i], h->ust == HU_ONAY ? YESIL : TURUNCU, (u / 120) % 2 == 0 ? 1.f : 0.f);
      break;
    case HU_SES: {
      int dolu = h->maks ? (n * h->duzey + h->maks / 2) / h->maks : 0;
      for (int i = 0; i < n; i++) halka_koy(k[i], BEYAZ, i < dolu ? 1.f : 0.f);
      break;
    }
    default: break;
  }
  // parlaklık tavanı x ayar, sonra akım sınırı
  uint32_t carpan = (uint32_t)h->sinir * h->parlaklik;  // 0..10000
  uint32_t toplam = 0;
  for (int i = 0; i < n; i++)
    for (int c = 0; c < 3; c++) {
      uint32_t v = (k[i][c] * carpan + 5000) / 10000;
      if (k[i][c] && !v && carpan) v = 1;  // çok sönükler tamamen sönmesin
      k[i][c] = (uint8_t)v;
      toplam += v;
    }
  uint32_t akim = toplam * HALKA_LED_MA / 255;
  if (akim > h->akim_sinir && akim) {
    for (int i = 0; i < n; i++)
      for (int c = 0; c < 3; c++) k[i][c] = (uint8_t)(k[i][c] * h->akim_sinir / akim);
    akim = h->akim_sinir;
  }
  h->akim_ma = (uint16_t)akim;
}

// Testler ve döküm için: "okuma 3/35" gibi kısa durum
static inline int halka_durum_metni(const Halka *h, char *out, int kap) {
  if (h->taban == HT_OKUMA)
    return snprintf(out, (size_t)kap, "%s %d/%d %s", HT_AD[h->taban], halka_dolu(h), h->n, HU_AD[h->ust]);
  return snprintf(out, (size_t)kap, "%s %s", HT_AD[h->taban], HU_AD[h->ust]);
}
