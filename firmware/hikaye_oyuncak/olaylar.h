// Olaylar: stand (NFC), sesli komut (KWS), geliştirme düğmeleri (DUGME_ACIK) ve seri taklit -> olay halkası.
//
// Olay halkası tek üretici, tek tüketici ve kilitsizdir: her kaynak (düğme görevi, mikrofon görevi, ana döngü) kendi
// halkasına yazar, ana döngü hepsini okur. Donanıma bağımlı değildir (tools/dugme_test.c, tools/urun_test.c).
#pragma once
#include <stdbool.h>
#include <stdint.h>

typedef enum {
  OLAY_YOK = 0,
  // geliştirme düğmeleri (dugmeler.h)
  OLAY_FIGUR, OLAY_FIGUR_UZUN,
  OLAY_YER, OLAY_YER_UZUN,
  OLAY_OYNAT, OLAY_OYNAT_UZUN,
  OLAY_SES_ARTI, OLAY_SES_EKSI,
  OLAY_ARKA,            // arka plan üretimi aç/kapa
  // ürün
  OLAY_STAND_KONDU,     // deger: etiketin nfc_no'su (figür 1..; 200 ayar kartı)
  OLAY_STAND_BILINMEYEN,// standa kaydı ve tablo karşılığı olmayan etiket kondu (boş etiket)
  OLAY_STAND_KALKTI,    // standdaki etiket kalktı
  OLAY_SESLI,           // deger: KWS olayı (kws.h)
} OlayTur;

static const char *const OLAY_AD[] = {"yok", "figür", "figür uzun", "yer", "yer uzun", "oynat", "oynat uzun",
                                      "ses +", "ses -", "arka plan", "stand: kondu", "stand: bilinmeyen etiket",
                                      "stand: kalktı", "sesli komut"};

typedef struct { uint8_t tur; int16_t deger; } Olay;

#define OLAY_HALKA 16
typedef struct {
  Olay o[OLAY_HALKA];
  volatile uint8_t yaz, oku;
} OlayHalka;

static inline void halka_ekle(OlayHalka *h, uint8_t tur, int deger) {
  uint8_t y = h->yaz, s = (uint8_t)((y + 1) % OLAY_HALKA);
  if (s == h->oku) return;  // halka dolu: olay düşer
  h->o[y].tur = tur;
  h->o[y].deger = (int16_t)deger;
  __sync_synchronize();
  h->yaz = s;
}

static inline bool halka_bak(const OlayHalka *h, Olay *o) {
  if (h->oku == h->yaz) return false;
  if (o) *o = h->o[h->oku];
  return true;
}

static inline bool halka_al(OlayHalka *h, Olay *o) {
  if (!halka_bak(h, o)) return false;
  __sync_synchronize();
  h->oku = (uint8_t)((h->oku + 1) % OLAY_HALKA);
  return true;
}
