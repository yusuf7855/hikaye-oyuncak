// Saat ve zamanlı işler: sabah alarmı (günler, gün doğumu ışığı), akşam yatma vakti hatırlatması, gece kilidi
// (yatma vaktinden sabah saatine kadar yalnız ninni).
//
// Oyuncakta pil destekli saat yok: saat, ayar sayfası her açıldığında telefondan alınır (UTC saniye + telefonun saat
// dilimi) ve oyuncak açık kaldıkça kendi zamanlayıcısıyla ilerler. Piller çıkarılınca saat kaybolur; zamanlı işler
// ayar sayfası yeniden açılana kadar çalışmaz. (Hafif uykuda iç RC saati dakikalar mertebesinde kayabilir; ürün
// kartı için 32,768 kHz kristal ya da pilli saat modülü: docs/DONANIM.md "Saat".)
//
// Bütün hesap "yerel saniye" (UTC saniye + saat dilimi) üzerinden, tamsayıyla. 1 Ocak 1970 perşembe. Haftanın günü
// 0 = pazartesi .. 6 = pazar; alarm günleri bit maskesi (bit 0 pazartesi). Saf C: tools/urun_test.c dener.
#pragma once
#include <stdint.h>
#include <stdio.h>

#define SAAT_ALARM_PENCERE_DK 10  // alarm anı geçmiş olsa da (oyuncak o an meşgulse) bu kadar dakika içinde çalar
#define SAAT_YATMA_PENCERE_DK 30  // yatma hatırlatması (o an okuma sürüyorsa) bu kadar dakika içinde söylenir
#define SAAT_GUNES_MAKS_DK 30
#define SAAT_HER_GUN 0x7F
#define SAAT_HAFTA_ICI 0x1F

typedef struct {
  uint8_t alarm_acik, alarm_saat, alarm_dk, alarm_gunler;  // gunler: bit 0 pazartesi .. bit 6 pazar
  uint8_t alarm_gunes;                     // gün doğumu ışığı: alarmdan kaç dakika önce başlar (0: yok)
  uint8_t yatma_acik, yatma_saat, yatma_dk;  // akşam hatırlatması (her gün)
  uint8_t kilit;                           // gece kilidi: yatma vaktinden sabaha yalnız ninni
  uint8_t sabah_saat, sabah_dk;            // gece kilidinin bittiği saat
} SaatAyar;

// Bir kez çalan işlerin son çalındığı an (yerel dakika; aynı alarm iki kez çalmasın)
typedef struct { int64_t alarm_son, yatma_son; } SaatDurum;

enum { SAAT_YOK = 0, SAAT_GUNES = 1, SAAT_ALARM = 2, SAAT_YATMA = 3 };

static const char *const SAAT_GUN_KISA[7] = {"Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"};

static inline void saat_varsayilan(SaatAyar *a) {
  a->alarm_acik = 0; a->alarm_saat = 7; a->alarm_dk = 0; a->alarm_gunler = SAAT_HAFTA_ICI; a->alarm_gunes = 10;
  a->yatma_acik = 0; a->yatma_saat = 20; a->yatma_dk = 30;
  a->kilit = 0; a->sabah_saat = 7; a->sabah_dk = 0;
}

static inline void saat_duzelt(SaatAyar *a) {
  a->alarm_acik = a->alarm_acik != 0;
  if (a->alarm_saat > 23) a->alarm_saat = 7;
  if (a->alarm_dk > 59) a->alarm_dk = 0;
  a->alarm_gunler &= SAAT_HER_GUN;
  if (a->alarm_gunes > SAAT_GUNES_MAKS_DK) a->alarm_gunes = 10;
  a->yatma_acik = a->yatma_acik != 0;
  if (a->yatma_saat > 23) a->yatma_saat = 20;
  if (a->yatma_dk > 59) a->yatma_dk = 30;
  a->kilit = a->kilit != 0;
  if (a->sabah_saat > 23) a->sabah_saat = 7;
  if (a->sabah_dk > 59) a->sabah_dk = 0;
}

static inline int64_t saat_bol(int64_t a, int64_t b) { return a >= 0 ? a / b : -((-a + b - 1) / b); }  // aşağı yuvarlar
static inline int64_t saat_gun(int64_t yerel_s) { return saat_bol(yerel_s, 86400); }
static inline int saat_gun_dakika(int64_t yerel_s) { return (int)(saat_bol(yerel_s, 60) - saat_gun(yerel_s) * 1440); }
static inline int saat_hafta_gunu(int64_t gun) { return (int)(((gun + 3) % 7 + 7) % 7); }  // 0 pazartesi

// "07:05" -> saat, dakika. Döner 1 geçerli.
static inline int saat_coz(const char *s, uint8_t *sa, uint8_t *dk) {
  if (!s || !(s[0] >= '0' && s[0] <= '9')) return 0;
  int h = 0, m = 0, i = 0;
  while (s[i] >= '0' && s[i] <= '9' && i < 2) h = h * 10 + (s[i++] - '0');
  if (s[i++] != ':') return 0;
  if (!(s[i] >= '0' && s[i] <= '9' && s[i + 1] >= '0' && s[i + 1] <= '9') || s[i + 2]) return 0;
  m = (s[i] - '0') * 10 + (s[i + 1] - '0');
  if (h > 23 || m > 59) return 0;
  *sa = (uint8_t)h;
  *dk = (uint8_t)m;
  return 1;
}

// Alarmın t anına (yerel dakika) en yakın uygun çalış anları: gün g'deki alarm (o gün seçiliyse). -1: yok.
static inline int64_t saat_alarm_ani(const SaatAyar *a, int64_t gun) {
  if (!a->alarm_acik || !((a->alarm_gunler >> saat_hafta_gunu(gun)) & 1)) return -1;
  return gun * 1440 + a->alarm_saat * 60 + a->alarm_dk;
}

// Şimdi ne yapılmalı? Her saniye çağrılır. Alarm ve yatma hatırlatması kendi penceresinde bir kez döner
// (d günceller). SAAT_GUNES: gün doğumu sürüyor, *binde = ilerleme 0..999.
static inline int saat_olay(const SaatAyar *a, SaatDurum *d, int64_t yerel_s, int *binde) {
  int64_t dk = saat_bol(yerel_s, 60), gun = saat_gun(yerel_s);
  int gunes = 0;
  for (int64_t g = gun - 1; g <= gun + 1; g++) {
    int64_t t = saat_alarm_ani(a, g);
    if (t < 0) continue;
    if (dk >= t && dk < t + SAAT_ALARM_PENCERE_DK && d->alarm_son != t) { d->alarm_son = t; return SAAT_ALARM; }
    if (a->alarm_gunes && dk >= t - a->alarm_gunes && dk < t && d->alarm_son != t) {
      int64_t sure = (int64_t)a->alarm_gunes * 60, gecen = yerel_s - (t - a->alarm_gunes) * 60;
      if (binde) *binde = (int)(gecen * 1000 / sure);
      gunes = 1;
    }
  }
  if (a->yatma_acik) {
    for (int64_t g = gun - 1; g <= gun; g++) {
      int64_t t = g * 1440 + a->yatma_saat * 60 + a->yatma_dk;
      if (dk >= t && dk < t + SAAT_YATMA_PENCERE_DK && d->yatma_son != t) { d->yatma_son = t; return SAAT_YATMA; }
    }
  }
  return gunes ? SAAT_GUNES : SAAT_YOK;
}

// Saat ya da ayar yeni değişti: penceresi şu an açık olan alarm/hatırlatma "çalındı" sayılır (saat 07:03'te ayarlanınca
// 07:00 alarmı hemen çalmasın). Gün doğumu sürüyorsa sürer.
static inline void saat_durum_kur(const SaatAyar *a, SaatDurum *d, int64_t yerel_s) {
  int64_t dk = saat_bol(yerel_s, 60), gun = saat_gun(yerel_s);
  d->alarm_son = d->yatma_son = -1;
  for (int64_t g = gun - 1; g <= gun + 1; g++) {
    int64_t t = saat_alarm_ani(a, g);
    if (t >= 0 && dk >= t && dk < t + SAAT_ALARM_PENCERE_DK) d->alarm_son = t;
  }
  for (int64_t g = gun - 1; g <= gun; g++) {
    int64_t t = g * 1440 + a->yatma_saat * 60 + a->yatma_dk;
    if (a->yatma_acik && dk >= t && dk < t + SAAT_YATMA_PENCERE_DK) d->yatma_son = t;
  }
}

// Gece kilidi şu an etkin mi (yatma vakti <= saat < sabah; gece yarısını aşabilir)
static inline int saat_gece_mi(const SaatAyar *a, int64_t yerel_s) {
  if (!a->kilit) return 0;
  int m = saat_gun_dakika(yerel_s), bas = a->yatma_saat * 60 + a->yatma_dk, son = a->sabah_saat * 60 + a->sabah_dk;
  if (bas == son) return 0;
  return bas < son ? (m >= bas && m < son) : (m >= bas || m < son);
}

// "07:05"
static inline int saat_yaz(int sa, int dk, char *out, int kap) { return snprintf(out, (size_t)kap, "%02d:%02d", sa, dk); }
