// Düğmeler: üç düğmenin (FİGÜR, YER, OYNAT) sekme süzgeci, kısa/uzun basış ve ikili basışlar -> olay halkası.
//
// dugme_adim() saf bir durum makinesidir: her örneklemede (kartta 10 ms'de bir, ayrı görevde) üç düğmenin basılı
// olup olmadığını ve zamanı (ms) alır, olayları halkaya ekler; olay_al() ana döngüden okur (tek üretici, tek
// tüketici). Donanıma bağımlı değildir: tools/dugme_test.c bilgisayarda dener.
//
//   FİGÜR kısa: sonraki figür          | FİGÜR uzun (bırakınca): önceki figür
//   YER kısa:   sonraki yer            | YER uzun: yer "sürpriz" (rastgele)
//   OYNAT kısa: hikâye / dur           | OYNAT uzun: son hikâyeyi yeniden oku
//   OYNAT basılıyken FİGÜR: ses aç, YER: ses kıs (OYNAT'ın kendi olayı bastırılır)
//   FİGÜR + YER birlikte DUGME_IKILI_MS: arka plan üretimi aç/kapa
// Uzun basış bırakınca verilir (basılı tutarken başka düğmeyle ikili basışa dönüşebilsin diye).
#pragma once
#include <stdbool.h>
#include <stdint.h>

#ifndef DUGME_SEKME_MS
#define DUGME_SEKME_MS 30     // seviye bu kadar kararlı kalmalı (sekme süzgeci)
#endif
#ifndef DUGME_UZUN_MS
#define DUGME_UZUN_MS 800     // bundan uzun basış "uzun"
#endif
#ifndef DUGME_IKILI_MS
#define DUGME_IKILI_MS 3000   // FİGÜR + YER birlikte bu kadar: arka plan aç/kapa
#endif

enum { DUGME_FIGUR = 0, DUGME_YER = 1, DUGME_OYNAT = 2, DUGME_N = 3 };

typedef enum {
  OLAY_YOK = 0,
  OLAY_FIGUR, OLAY_FIGUR_UZUN,
  OLAY_YER, OLAY_YER_UZUN,
  OLAY_OYNAT, OLAY_OYNAT_UZUN,
  OLAY_SES_ARTI, OLAY_SES_EKSI,
  OLAY_ARKA,        // arka plan üretimi aç/kapa
  OLAY_NFC,         // deger: figür (nfc.h)
} OlayTur;

static const char *const OLAY_AD[] = {"yok", "figür", "figür uzun", "yer", "yer uzun", "oynat", "oynat uzun",
                                      "ses +", "ses -", "arka plan", "nfc"};

typedef struct { uint8_t tur; int8_t deger; } Olay;

typedef struct {
  bool ham, basili;      // son okunan seviye, süzülmüş durum
  uint32_t ham_ms;       // ham seviyenin değiştiği an
  uint32_t bas_ms;       // basışın başladığı an
  bool sustur;           // bu basış ikili basışa harcandı: kendi olayı verilmez
} DugmeDurum;

// Olay halkası: tek üretici, tek tüketici (kilitsiz). Düğme görevi ve ana döngü ayrı halkalara yazar.
#define OLAY_HALKA 16
typedef struct {
  Olay o[OLAY_HALKA];
  volatile uint8_t yaz, oku;
} OlayHalka;

static void halka_ekle(OlayHalka *h, uint8_t tur, int8_t deger) {
  uint8_t y = h->yaz, s = (uint8_t)((y + 1) % OLAY_HALKA);
  if (s == h->oku) return;  // halka dolu: olay düşer
  h->o[y].tur = tur;
  h->o[y].deger = deger;
  __sync_synchronize();
  h->yaz = s;
}

static bool halka_bak(const OlayHalka *h, Olay *o) {
  if (h->oku == h->yaz) return false;
  if (o) *o = h->o[h->oku];
  return true;
}

static bool halka_al(OlayHalka *h, Olay *o) {
  if (!halka_bak(h, o)) return false;
  __sync_synchronize();
  h->oku = (uint8_t)((h->oku + 1) % OLAY_HALKA);
  return true;
}

typedef struct {
  DugmeDurum d[DUGME_N];
  bool ikili_verildi;
  uint32_t ikili_ms;
  OlayHalka h;
} Dugmeler;

// Bir örnekleme: basili[i] düğme i'nin şu anki ham seviyesi (true: basılı), ms şimdiki zaman (taşma güvenli).
static void dugme_adim(Dugmeler *g, const bool basili[DUGME_N], uint32_t ms) {
  for (int i = 0; i < DUGME_N; i++) {
    DugmeDurum *d = &g->d[i];
    if (basili[i] != d->ham) { d->ham = basili[i]; d->ham_ms = ms; }
    if (d->ham == d->basili || (uint32_t)(ms - d->ham_ms) < DUGME_SEKME_MS) continue;
    d->basili = d->ham;
    if (d->basili) {  // basış başladı
      d->bas_ms = ms;
      d->sustur = false;
      if (i != DUGME_OYNAT && g->d[DUGME_OYNAT].basili) {  // OYNAT basılıyken: ses aç/kıs
        halka_ekle(&g->h, i == DUGME_FIGUR ? OLAY_SES_ARTI : OLAY_SES_EKSI, 0);
        d->sustur = g->d[DUGME_OYNAT].sustur = true;
      } else if (i != DUGME_OYNAT && g->d[DUGME_FIGUR].basili && g->d[DUGME_YER].basili) {  // FİGÜR + YER
        g->d[DUGME_FIGUR].sustur = g->d[DUGME_YER].sustur = true;
        g->ikili_verildi = false;
        g->ikili_ms = ms;
      }
    } else {          // bırakıldı
      if (!d->sustur) {
        bool uzun = (uint32_t)(ms - d->bas_ms) >= DUGME_UZUN_MS;
        uint8_t tur = i == DUGME_FIGUR ? (uzun ? OLAY_FIGUR_UZUN : OLAY_FIGUR)
                    : i == DUGME_YER   ? (uzun ? OLAY_YER_UZUN : OLAY_YER)
                                       : (uzun ? OLAY_OYNAT_UZUN : OLAY_OYNAT);
        halka_ekle(&g->h, tur, 0);
      }
      d->sustur = false;
    }
  }
  if (g->d[DUGME_FIGUR].basili && g->d[DUGME_YER].basili && g->d[DUGME_FIGUR].sustur && g->d[DUGME_YER].sustur &&
      !g->ikili_verildi && (uint32_t)(ms - g->ikili_ms) >= DUGME_IKILI_MS) {
    halka_ekle(&g->h, OLAY_ARKA, 0);
    g->ikili_verildi = true;
  }
}

// Herhangi bir düğme basılı mı (süzülmüş)
static bool dugme_basili(const Dugmeler *g) {
  for (int i = 0; i < DUGME_N; i++)
    if (g->d[i].basili || g->d[i].ham) return true;
  return false;
}
