// Kalıcı ürün ayarları (ayar sayfasından değişir, Preferences/NVS'te durur) ve form doğrulaması.
//
// Ayar sayfası (ayar_sayfa.h) alanları: ad, okunus, ses_maks, uyku_dk, parlaklik, cekilince, nefes, arka_goster,
// muzik; saat ve zamanlı işler (saat.h): alarm_acik, alarm_saat ("07:00"), alarm_gunler (bit 0 pazartesi),
// alarm_gunes (dk), alarm_tur, alarm_mesaj, yatma_acik, yatma_saat, kilit, sabah_saat. Form ayar_form_uygula() ile
// önce bütünüyle doğrulanır, hepsi geçerliyse uygulanır (yarım ayar kaydedilmez). Saf C: tools/urun_test.c dener;
// .ino NVS'e yazar.
#pragma once
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "saat.h"

#define AYAR_AD_HARF 20        // çocuğun adı en çok bu kadar harf (boşluk dahil)
#define AYAR_AD_BAYT 64        // UTF-8 (Türkçe harf 2 bayt)
#define AYAR_MESAJ_HARF 120    // alarm mesajı ve sürpriz mesaj en çok bu kadar karakter
#define AYAR_MESAJ_BAYT 256

// Alarmda ne çalar: Eko'nun sesi (günaydın + ad + mesaj), müzik kutusu ezgisi, yüklenen ses (alarm_ses.h). Müzik ve
// yüklenen seste de günaydın + mesaj bir kez söylenir. Yüklenen ses yoksa müzik kutusu çalar.
enum { ALARM_SES = 0, ALARM_MUZIK = 1, ALARM_YUKLENEN = 2 };
static const char *const ALARM_TUR_AD[3] = {"Eko'nun sesi", "müzik kutusu", "yüklenen ses"};

enum { CEKILINCE_CUMLE = 0, CEKILINCE_HEMEN = 1, CEKILINCE_BITIR = 2 };

typedef struct {
  char ad[AYAR_AD_BAYT];  // çocuğun adı ("" yok)
  char okunus[AYAR_AD_BAYT];  // adın okunuşu (ör. Jasmine -> Yasmin); "" ise ad okunur
  uint8_t ses_maks;       // en yüksek ses seviyesi 1..7
  uint8_t uyku_dk;        // uyku zamanlayıcısı 10 / 20 / 30 dk (gece figürü: ninniler bu kadar sürer, sonra kapanır)
  uint8_t parlaklik;      // halka parlaklığı 0..100 (% HALKA_PARLAKLIK_SINIR; 0 halka kapalı)
  uint8_t cekilince;      // oyuncak çekilince: CEKILINCE_*
  uint8_t nefes;          // boşta sönük beyaz nefes (0: halka boşta kapalı)
  uint8_t arka_goster;    // arka planda hikâye hazırlanırken sönük dönen nokta
  uint8_t muzik;          // ninni modunda çok kısık müzik kutusu
  SaatAyar zaman;         // alarm, yatma vakti, gece kilidi (saat.h)
  uint8_t alarm_tur;      // ALARM_*
  char alarm_mesaj[AYAR_MESAJ_BAYT];  // alarmda günaydından sonra söylenir ("" yok)
  int16_t tz_dk;          // telefonun saat dilimi (dakika, UTC'ye eklenir; Türkiye +180)
} Ayarlar;

static const char *const CEKILINCE_AD[3] = {"cümle sonunda dur", "hemen dur", "hikâyeyi bitir"};

static inline void ayar_varsayilan(Ayarlar *a) {
  memset(a, 0, sizeof *a);
  a->ses_maks = 7;
  a->uyku_dk = 20;
  a->parlaklik = 60;
  a->cekilince = CEKILINCE_CUMLE;
  a->nefes = 1;
  a->arka_goster = 1;
  a->muzik = 1;
  saat_varsayilan(&a->zaman);
  a->alarm_tur = ALARM_SES;
  a->tz_dk = 180;
}

// Değerleri sınırlarına çeker (NVS'ten bozuk/eski değer gelirse)
static inline void ayar_duzelt(Ayarlar *a) {
  a->ad[AYAR_AD_BAYT - 1] = 0;
  if (a->ses_maks < 1 || a->ses_maks > 7) a->ses_maks = 7;
  if (a->uyku_dk != 10 && a->uyku_dk != 20 && a->uyku_dk != 30) a->uyku_dk = 20;
  if (a->parlaklik > 100) a->parlaklik = 100;
  if (a->cekilince > CEKILINCE_BITIR) a->cekilince = CEKILINCE_CUMLE;
  a->nefes = a->nefes != 0;
  a->arka_goster = a->arka_goster != 0;
  a->muzik = a->muzik != 0;
  a->okunus[AYAR_AD_BAYT - 1] = 0;
  saat_duzelt(&a->zaman);
  if (a->alarm_tur > ALARM_YUKLENEN) a->alarm_tur = ALARM_SES;
  a->alarm_mesaj[AYAR_MESAJ_BAYT - 1] = 0;
  if (a->tz_dk < -720 || a->tz_dk > 840) a->tz_dk = 180;
}

// Ad için izinli harfler: İngiliz alfabesi + Türkçe harfler (ç ğ ı i ö ş ü, şapkalı â î û), büyük ve küçük
static inline int ad_harf_mi(uint32_t c) {
  if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) return 1;
  switch (c) {
    case 0xE7: case 0xC7: case 0x11F: case 0x11E: case 0x131: case 0x130: case 0xF6: case 0xD6:
    case 0x15F: case 0x15E: case 0xFC: case 0xDC: case 0xE2: case 0xC2: case 0xEE: case 0xCE: case 0xFB: case 0xDB:
      return 1;
  }
  return 0;
}

enum { AD_TAMAM = 0, AD_UZUN = -1, AD_HARF = -2 };

// Adı temizler (baş/son boşluk atılır, aradaki boşluklar teke iner) ve doğrular. out en az AYAR_AD_BAYT.
// Döner: AD_TAMAM | AD_UZUN (20 harften uzun) | AD_HARF (harf ve boşluk dışında karakter ya da bozuk UTF-8).
static inline int ad_temizle(const char *girdi, char *out) {
  const unsigned char *p = (const unsigned char *)girdi;
  int n = 0, harf = 0, bosluk = 0;
  out[0] = 0;
  while (*p) {
    if (*p == ' ' || *p == '\t') { bosluk = 1; p++; continue; }
    const unsigned char *bas = p;
    uint32_t c = *p++;
    int k = 0;
    if (c >= 0xF0) return AD_HARF;
    if (c >= 0xE0) { c &= 0x0F; k = 2; }
    else if (c >= 0xC0) { c &= 0x1F; k = 1; }
    else if (c >= 0x80) return AD_HARF;
    for (int i = 0; i < k; i++) {
      if ((*p & 0xC0) != 0x80) return AD_HARF;
      c = (c << 6) | (*p++ & 0x3F);
    }
    if (!ad_harf_mi(c)) return AD_HARF;
    if (bosluk && harf) {
      if (++harf > AYAR_AD_HARF || n + 1 >= AYAR_AD_BAYT) return AD_UZUN;
      out[n++] = ' ';
    }
    bosluk = 0;
    if (++harf > AYAR_AD_HARF || n + (int)(p - bas) >= AYAR_AD_BAYT) return AD_UZUN;
    memcpy(out + n, bas, (size_t)(p - bas));
    n += (int)(p - bas);
    out[n] = 0;
  }
  return AD_TAMAM;
}

// Mesaj (alarm mesajı, sürpriz mesaj): harfler (ad gibi), rakamlar, boşluk ve . , ! ? ' - : ; noktalama. Telefon
// klavyelerinin kıvrık tırnakları (‘ ’ “ ”) düz kesme işaretine, üç nokta (…) "..."ya çevrilir; boşluklar teke iner.
// Döner: AD_TAMAM | AD_UZUN (AYAR_MESAJ_HARF'ten uzun) | AD_HARF (izinsiz karakter). out en az AYAR_MESAJ_BAYT.
static inline int mesaj_temizle(const char *girdi, char *out) {
  const unsigned char *p = (const unsigned char *)girdi;
  int n = 0, harf = 0, bosluk = 0;
  out[0] = 0;
  while (*p) {
    if (*p == ' ' || *p == '\t' || *p == '\n' || *p == '\r') { bosluk = 1; p++; continue; }
    const unsigned char *bas = p;
    uint32_t c = *p++;
    int k = 0;
    if (c >= 0xF0) return AD_HARF;
    if (c >= 0xE0) { c &= 0x0F; k = 2; }
    else if (c >= 0xC0) { c &= 0x1F; k = 1; }
    else if (c >= 0x80) return AD_HARF;
    for (int i = 0; i < k; i++) {
      if ((*p & 0xC0) != 0x80) return AD_HARF;
      c = (c << 6) | (*p++ & 0x3F);
    }
    const char *yerine = NULL;
    if (c == 0x2018 || c == 0x2019 || c == 0x201C || c == 0x201D) yerine = "'";
    else if (c == 0x2026) yerine = "...";
    else if (!ad_harf_mi(c) && !(c >= '0' && c <= '9') && !strchr(".,!?'-:;", (int)c)) return AD_HARF;
    int uz = yerine ? (int)strlen(yerine) : (int)(p - bas);
    if (bosluk && harf) {
      if (++harf > AYAR_MESAJ_HARF || n + 1 >= AYAR_MESAJ_BAYT) return AD_UZUN;
      out[n++] = ' ';
    }
    bosluk = 0;
    harf += yerine ? uz : 1;
    if (harf > AYAR_MESAJ_HARF || n + uz >= AYAR_MESAJ_BAYT) return AD_UZUN;
    memcpy(out + n, yerine ? (const void *)yerine : (const void *)bas, (size_t)uz);
    n += uz;
    out[n] = 0;
  }
  return AD_TAMAM;
}

// Sayı alanı: yalnız rakam; döner 1 geçerli
static inline int ayar_sayi(const char *s, int *v) {
  if (!s || !*s || strlen(s) > 4) return 0;
  for (const char *p = s; *p; p++) if (*p < '0' || *p > '9') return 0;
  *v = atoi(s);
  return 1;
}

// Form alanı okuyucu: ada göre değer (yoksa NULL)
typedef const char *(*AyarAlan)(void *kul, const char *ad);

// Formu doğrular; hepsi geçerliyse a'ya uygular. Döner: 0 tamam; değilse -1 ve hata'ya Türkçe açıklama.
// Gönderilmeyen alan değişmez.
static inline int ayar_form_uygula(Ayarlar *a, AyarAlan al, void *kul, char *hata, int kap) {
  Ayarlar y = *a;
  const char *s;
  int v;
  hata[0] = 0;
  if ((s = al(kul, "ad"))) {
    int r = ad_temizle(s, y.ad);
    if (r == AD_UZUN) { snprintf(hata, (size_t)kap, "Ad en çok %d harf olabilir.", AYAR_AD_HARF); return -1; }
    if (r == AD_HARF) { snprintf(hata, (size_t)kap, "Adda yalnız harf (Türkçe harfler dahil) ve boşluk olabilir."); return -1; }
  }
  if ((s = al(kul, "okunus"))) {
    int r = ad_temizle(s, y.okunus);
    if (r == AD_UZUN) { snprintf(hata, (size_t)kap, "Okunuş en çok %d harf olabilir.", AYAR_AD_HARF); return -1; }
    if (r == AD_HARF) { snprintf(hata, (size_t)kap, "Okunuşta yalnız harf ve boşluk olabilir."); return -1; }
  }
  if ((s = al(kul, "ses_maks"))) {
    if (!ayar_sayi(s, &v) || v < 1 || v > 7) { snprintf(hata, (size_t)kap, "En yüksek ses 1 ile 7 arasında olmalı."); return -1; }
    y.ses_maks = (uint8_t)v;
  }
  if ((s = al(kul, "uyku_dk"))) {
    if (!ayar_sayi(s, &v) || (v != 10 && v != 20 && v != 30)) { snprintf(hata, (size_t)kap, "Uyku zamanlayıcısı 10, 20 ya da 30 dakika olmalı."); return -1; }
    y.uyku_dk = (uint8_t)v;
  }
  if ((s = al(kul, "parlaklik"))) {
    if (!ayar_sayi(s, &v) || v > 100) { snprintf(hata, (size_t)kap, "Halka parlaklığı 0 ile 100 arasında olmalı."); return -1; }
    y.parlaklik = (uint8_t)v;
  }
  if ((s = al(kul, "cekilince"))) {
    if (!ayar_sayi(s, &v) || v > CEKILINCE_BITIR) { snprintf(hata, (size_t)kap, "Oyuncak çekilince seçeneği geçersiz."); return -1; }
    y.cekilince = (uint8_t)v;
  }
  if ((s = al(kul, "nefes"))) {
    if (!ayar_sayi(s, &v) || v > 1) { snprintf(hata, (size_t)kap, "Boşta ışık seçeneği geçersiz."); return -1; }
    y.nefes = (uint8_t)v;
  }
  if ((s = al(kul, "arka_goster"))) {
    if (!ayar_sayi(s, &v) || v > 1) { snprintf(hata, (size_t)kap, "Hazırlık ışığı seçeneği geçersiz."); return -1; }
    y.arka_goster = (uint8_t)v;
  }
  if ((s = al(kul, "muzik"))) {
    if (!ayar_sayi(s, &v) || v > 1) { snprintf(hata, (size_t)kap, "Müzik kutusu seçeneği geçersiz."); return -1; }
    y.muzik = (uint8_t)v;
  }
  // saat ve zamanlı işler
  if ((s = al(kul, "alarm_acik"))) {
    if (!ayar_sayi(s, &v) || v > 1) { snprintf(hata, (size_t)kap, "Alarm seçeneği geçersiz."); return -1; }
    y.zaman.alarm_acik = (uint8_t)v;
  }
  if ((s = al(kul, "alarm_saat")) && !saat_coz(s, &y.zaman.alarm_saat, &y.zaman.alarm_dk)) {
    snprintf(hata, (size_t)kap, "Alarm saati SS:DD biçiminde olmalı (ör. 07:00)."); return -1;
  }
  if ((s = al(kul, "alarm_gunler"))) {
    if (!ayar_sayi(s, &v) || v > SAAT_HER_GUN) { snprintf(hata, (size_t)kap, "Alarm günleri geçersiz."); return -1; }
    y.zaman.alarm_gunler = (uint8_t)v;
  }
  if ((s = al(kul, "alarm_gunes"))) {
    if (!ayar_sayi(s, &v) || v > SAAT_GUNES_MAKS_DK) { snprintf(hata, (size_t)kap, "Gün doğumu ışığı 0 ile %d dakika arasında olmalı.", SAAT_GUNES_MAKS_DK); return -1; }
    y.zaman.alarm_gunes = (uint8_t)v;
  }
  if ((s = al(kul, "alarm_tur"))) {
    if (!ayar_sayi(s, &v) || v > ALARM_YUKLENEN) { snprintf(hata, (size_t)kap, "Alarm sesi seçeneği geçersiz."); return -1; }
    y.alarm_tur = (uint8_t)v;
  }
  if ((s = al(kul, "alarm_mesaj"))) {
    int r = mesaj_temizle(s, y.alarm_mesaj);
    if (r == AD_UZUN) { snprintf(hata, (size_t)kap, "Alarm mesajı en çok %d karakter olabilir.", AYAR_MESAJ_HARF); return -1; }
    if (r == AD_HARF) { snprintf(hata, (size_t)kap, "Alarm mesajında yalnız harf, rakam, boşluk ve . , ! ? ' - : ; olabilir."); return -1; }
  }
  if (y.zaman.alarm_acik && !y.zaman.alarm_gunler) { snprintf(hata, (size_t)kap, "Alarm için en az bir gün seçin."); return -1; }
  if ((s = al(kul, "yatma_acik"))) {
    if (!ayar_sayi(s, &v) || v > 1) { snprintf(hata, (size_t)kap, "Yatma vakti seçeneği geçersiz."); return -1; }
    y.zaman.yatma_acik = (uint8_t)v;
  }
  if ((s = al(kul, "yatma_saat")) && !saat_coz(s, &y.zaman.yatma_saat, &y.zaman.yatma_dk)) {
    snprintf(hata, (size_t)kap, "Yatma vakti SS:DD biçiminde olmalı (ör. 20:30)."); return -1;
  }
  if ((s = al(kul, "kilit"))) {
    if (!ayar_sayi(s, &v) || v > 1) { snprintf(hata, (size_t)kap, "Gece kilidi seçeneği geçersiz."); return -1; }
    y.zaman.kilit = (uint8_t)v;
  }
  if ((s = al(kul, "sabah_saat")) && !saat_coz(s, &y.zaman.sabah_saat, &y.zaman.sabah_dk)) {
    snprintf(hata, (size_t)kap, "Sabah saati SS:DD biçiminde olmalı (ör. 07:00)."); return -1;
  }
  if (y.zaman.kilit && y.zaman.yatma_saat == y.zaman.sabah_saat && y.zaman.yatma_dk == y.zaman.sabah_dk) {
    snprintf(hata, (size_t)kap, "Gece kilidi için yatma vakti ile sabah saati farklı olmalı."); return -1;
  }
  *a = y;
  return 0;
}

// Ayarların JSON'u (ad ve okunuş yalnız harf ve boşluk, mesaj ayrıca . , ! ? ' - : ; içerir: kaçış gerekmez)
static inline int ayar_json(const Ayarlar *a, char *out, int kap) {
  const SaatAyar *z = &a->zaman;
  return snprintf(out, (size_t)kap,
                  "\"ad\":\"%s\",\"okunus\":\"%s\",\"ses_maks\":%d,\"uyku_dk\":%d,\"parlaklik\":%d,\"cekilince\":%d,"
                  "\"nefes\":%d,\"arka_goster\":%d,\"muzik\":%d,\"alarm_acik\":%d,\"alarm_saat\":\"%02d:%02d\","
                  "\"alarm_gunler\":%d,\"alarm_gunes\":%d,\"alarm_tur\":%d,\"alarm_mesaj\":\"%s\",\"yatma_acik\":%d,"
                  "\"yatma_saat\":\"%02d:%02d\",\"kilit\":%d,\"sabah_saat\":\"%02d:%02d\",\"tz_dk\":%d",
                  a->ad, a->okunus, a->ses_maks, a->uyku_dk, a->parlaklik, a->cekilince, a->nefes, a->arka_goster,
                  a->muzik, z->alarm_acik, z->alarm_saat, z->alarm_dk, z->alarm_gunler, z->alarm_gunes, a->alarm_tur,
                  a->alarm_mesaj, z->yatma_acik, z->yatma_saat, z->yatma_dk, z->kilit, z->sabah_saat, z->sabah_dk,
                  a->tz_dk);
}
