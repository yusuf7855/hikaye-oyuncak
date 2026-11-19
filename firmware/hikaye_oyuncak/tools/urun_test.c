// Ürün parçalarının bilgisayarda denemesi (saf C başlıklar): saat ve zamanlı işler (saat.h: gün/dakika, alarm penceresi,
// gün doğumu, yatma, gece kilidi, saat ayarlanınca hemen çalmama), alarm sesi (alarm_ses.h: ADPCM, CRC, başlık),
// ayar kartı (ayar_karti.h + nfc.h: NDEF yazma, sayfa 36 kaydı, yarıda kesilen yazma), mesaj ve sayılar (ayarlar.h,
// selam.h), etiket kaydı (etiket.h: kodla/çöz/CRC, bozulmalar),
// taslak NFC sürücüsünde etiket belleğine yazma + doğrulama (nfc.h, NFC_OKUYUCU 0), selamlama ekleri (selam.h:
// donanım figürlerinin hepsi, üründen çıkan eski figürlerin adları, adsız, ninni), ayar formu doğrulaması (ayarlar.h),
// halka durumları ve sınırları (halka.h), müzik kutusu (muzik_kutusu.h), donanım figürü tablosu
// (generated/figur_donanim.h: üründen çıkan figürler yok, yerlesik.h).
// Derle:  cc -O2 -Wall -o /tmp/urun_test firmware/hikaye_oyuncak/tools/urun_test.c -lm
// Çalıştır: /tmp/urun_test   (çıkış kodu 0: hepsi geçti)
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NFC_OKUYUCU 0
#define HALKA_LED_MA 20
#include "../etiket.h"
#include "../nfc.h"
#include "../selam.h"
#include "../ayarlar.h"
#include "../halka.h"
#include "../muzik_kutusu.h"
#include "../generated/figur_donanim.h"
#include "../yerlesik.h"
#include "../saat.h"
#include "../alarm_ses.h"
#include <math.h>

static int hata = 0;
// Donanım tablosunda kimliği k olan figür (yoksa -1)
static int donanim_kimlik(const char *k) {
  for (int d = 0; d < DONANIM_N; d++)
    if (!strcmp(DONANIM_KIMLIK[d], k)) return d;
  return -1;
}
#define DENE(k, ...)                                                                                    \
  do {                                                                                                  \
    if (!(k)) { printf("HATA (satır %d): ", __LINE__); printf(__VA_ARGS__); printf("\n"); hata++; }      \
  } while (0)

// ---- etiket ----
static void etiket_denemesi(void) {
  DENE(etiket_crc16((const uint8_t *)"123456789", 9) == 0x29B1, "CRC-16/CCITT-FALSE denetim değeri");
  for (int no = 1; no <= 300; no++) {
    uint8_t k[ETIKET_BAYT];
    etiket_kodla(no, k);
    DENE(etiket_coz(k) == no, "%d kodla/çöz", no);
    DENE(!memcmp(k, "EKO", 3) && k[3] == ETIKET_SURUM, "sihir/sürüm");
    for (int b = 0; b < ETIKET_BAYT * 8; b++) {  // her tek bit bozulması yakalanır
      uint8_t z[ETIKET_BAYT];
      memcpy(z, k, sizeof z);
      z[b / 8] ^= (uint8_t)(1 << (b % 8));
      DENE(etiket_coz(z) != no, "%d: bit %d bozulması yakalanmadı", no, b);
    }
  }
  uint8_t bos[ETIKET_BAYT] = {0x03, 0x00, 0xFE, 0x00, 0, 0, 0, 0}, ff[ETIKET_BAYT];
  memset(ff, 0xFF, sizeof ff);
  DENE(etiket_coz(bos) == -1 && etiket_coz(ff) == -1, "boş NTAG / silinmiş bellek kayıt sayıldı");
  uint8_t k[ETIKET_BAYT];
  etiket_kodla(ETIKET_AYAR_NO, k);
  k[3] = 2;  // bilinmeyen sürüm
  DENE(etiket_coz(k) == -1, "bilinmeyen sürüm kabul edildi");
  uint8_t sifir[ETIKET_BAYT];
  etiket_kodla(0, sifir);
  DENE(etiket_coz(sifir) == -1, "nfc_no 0 kabul edildi");
}

// ---- taslak sürücüde tanıtma: yaz, geri oku, doğrula ----
static void nfc_denemesi(void) {
  const uint8_t uid[7] = {0x04, 0x51, 0x62, 0x73, 0x84, 0x95, 0xA6};
  bool kayit;
  nfc_sahte_koy_bos(uid, 7, true);
  uint8_t u[10];
  DENE(nfc_uid_oku(u, sizeof u) == 7 && !memcmp(u, uid, 7), "UID");
  DENE(nfc_etiket_no(u, 7, &kayit) == -1 && !kayit, "boş etiket bir figür sayıldı");
  DENE(nfc_kayit_yaz(3, uid, 7) == NFC_YAZ_TAMAM, "boş etikete yazılamadı");
  DENE(nfc_etiket_no(u, 7, &kayit) == 3 && kayit, "yazılan kayıt okunmadı");
  DENE(!memcmp(nfc_sahte.bellek + 12, "\xE1\x10\x12\x00", 4), "yetenek kabı (sayfa 3) bozuldu");
  DENE(nfc_kayit_yaz(ETIKET_AYAR_NO, uid, 7) == NFC_YAZ_TAMAM && nfc_etiket_no(u, 7, NULL) == ETIKET_AYAR_NO,
       "üzerine yazma (ayar kartı)");
  const uint8_t baska[7] = {0x04, 1, 2, 3, 4, 5, 6};
  DENE(nfc_kayit_yaz(5, baska, 7) == NFC_YAZ_ETIKET_YOK, "başka etiket beklenirken yazıldı");
  nfc_sahte.kilitli = true;
  DENE(nfc_kayit_yaz(5, uid, 7) == NFC_YAZ_OLMADI && nfc_etiket_no(u, 7, NULL) == ETIKET_AYAR_NO, "kilitli etiket");
  nfc_sahte.kilitli = false;
  // NTAG olmayan (MIFARE Classic) etiket: yazılamaz; UID tablosundaysa oradan
  const uint8_t klasik[4] = {0x04, 0xA1, 0xB2, 0xC3};
  nfc_sahte_koy_bos(klasik, 4, false);
  DENE(nfc_kayit_yaz(2, klasik, 4) == NFC_YAZ_NTAG_DEGIL, "Classic'e yazıldı");
  DENE(nfc_etiket_no(klasik, 4, &kayit) == 4 && !kayit, "UID tablosu (Keloğlan)");
  nfc_sahte_koy_no(12);
  DENE(nfc_uid_oku(u, sizeof u) == 7 && nfc_etiket_no(u, 7, NULL) == 12, "programlanmış gece figürü");
  nfc_sahte_kaldir();
  DENE(nfc_uid_oku(u, sizeof u) == 0, "kalkan etiket görüldü");
}

// ---- ayar kartı: NDEF Wi-Fi + sayfa 36 kaydı; yazma hangi sayfada kesilirse kesilsin kart tanınır ----
static void ayar_karti_denemesi(void) {
  const uint8_t uid[7] = {0x04, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22}, mac[6] = {0x24, 0xA1, 0x60, 0x12, 0x3F, 0x7A};
  uint8_t u[10], t[AYAR_KARTI_TLV_MAKS];
  int nt = ayar_karti_tlv("Masalci-Ayar-3F7A", "48201937", mac, t, sizeof t);
  DENE(nt > 0 && nt % 4 == 0 && nt <= AYAR_KARTI_TLV_MAKS && t[0] == NDEF_TLV && t[2] == 0xD2, "TLV (%d)", nt);
  DENE(ayar_karti_tlv("Masalci-Ayar-3F7A", "1234567", mac, t, sizeof t) < 0, "7 haneli şifre kabul edildi");
  nfc_sahte_koy_no(ETIKET_AYAR_NO);
  nfc_uid_oku(u, sizeof u);
  const uint8_t *ku = nfc_sahte.uid;
  DENE(nfc_ayar_karti_yaz(ETIKET_AYAR_NO, "Masalci-Ayar-3F7A", "48201937", mac, ku, 7) == NFC_YAZ_TAMAM, "ayar kartına yazılamadı");
  DENE(nfc_sahte.bellek[16] == NDEF_TLV && !memcmp(nfc_sahte.bellek + 16, t, (size_t)nt), "sayfa 4'te NDEF yok");
  DENE(nfc_etiket_no(u, 7, NULL) == ETIKET_AYAR_NO, "NDEF düzenindeki ayar kartı tanınmadı");
  DENE(!memcmp(nfc_sahte.bellek + 12, "\xE1\x10\x12\x00", 4), "yetenek kabı bozuldu");
  // yarıda kesilen yazma: eski düzenden (sayfa 4-5 kayıt) başlayıp k sayfa yazıldıktan sonra kesilir
  int sayfalar = ETIKET_BAYT / 4 + nt / 4;
  for (int k = 0; k <= sayfalar; k++) {
    nfc_sahte_koy_no(ETIKET_AYAR_NO);
    uint8_t son[NFC_SAHTE_SAYFA * 4];
    nfc_ayar_karti_yaz(ETIKET_AYAR_NO, "Masalci-Ayar-3F7A", "48201937", mac, nfc_sahte.uid, 7);
    memcpy(son, nfc_sahte.bellek, sizeof son);
    nfc_sahte_koy_no(ETIKET_AYAR_NO);
    // ilk k yazma (sırası: sayfa 36, 37, sonra 4, 5, ...) uygulanmış bellek
    for (int y = 0; y < k; y++) {
      int sayfa = y < 2 ? AYAR_KARTI_EK_SAYFA + y : ETIKET_SAYFA + (y - 2);
      memcpy(nfc_sahte.bellek + sayfa * 4, son + sayfa * 4, 4);
    }
    DENE(nfc_etiket_no(u, 7, NULL) == ETIKET_AYAR_NO, "yazma %d. sayfada kesilince kart tanınmadı", k);
  }
  (void)uid;
  // figür etiketi (eski düzen) hâlâ sayfa 4'ten
  nfc_sahte_koy_no(13);
  DENE(nfc_etiket_no(u, 7, NULL) == 13, "figür etiketi");
  nfc_sahte_kaldir();
}

// ---- saat ve zamanlı işler ----
static int64_t yerel(int y, int ay, int g, int sa, int dk, int sn) {  // yerel tarih -> yerel saniye (UTC gibi)
  static const int G[12] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
  int64_t gun = (int64_t)(y - 1970) * 365 + (y - 1969) / 4 + G[ay - 1] + (g - 1) + (ay > 2 && y % 4 == 0);
  return gun * 86400 + sa * 3600 + dk * 60 + sn;
}
static void saat_denemesi(void) {
  DENE(saat_hafta_gunu(saat_gun(yerel(2026, 11, 23, 12, 0, 0))) == 0, "23 Kasım 2026 pazartesi");
  DENE(saat_hafta_gunu(saat_gun(yerel(2026, 11, 29, 0, 0, 0))) == 6, "29 Kasım 2026 pazar");
  DENE(saat_hafta_gunu(saat_gun(yerel(1970, 1, 1, 0, 0, 0))) == 3, "1 Ocak 1970 perşembe");
  DENE(saat_gun_dakika(yerel(2026, 11, 23, 7, 5, 59)) == 7 * 60 + 5, "dakika");
  uint8_t sa, dk;
  DENE(saat_coz("07:05", &sa, &dk) && sa == 7 && dk == 5 && saat_coz("7:05", &sa, &dk) && sa == 7, "saat_coz");
  DENE(!saat_coz("24:00", &sa, &dk) && !saat_coz("07:60", &sa, &dk) && !saat_coz("07:5", &sa, &dk) &&
       !saat_coz("07:05x", &sa, &dk) && !saat_coz("", &sa, &dk), "geçersiz saat kabul edildi");
  SaatAyar a;
  saat_varsayilan(&a);
  a.alarm_acik = 1; a.alarm_saat = 7; a.alarm_dk = 0; a.alarm_gunler = SAAT_HAFTA_ICI; a.alarm_gunes = 10;
  SaatDurum d = {-1, -1};
  int b = -1, alarm = 0, gunes = 0, son_binde = -1, artiyor = 1;
  for (int64_t t = yerel(2026, 11, 23, 6, 40, 0); t < yerel(2026, 11, 23, 7, 30, 0); t++) {  // pazartesi, her saniye
    int o = saat_olay(&a, &d, t, &b);
    if (o == SAAT_ALARM) { alarm++; DENE(t == yerel(2026, 11, 23, 7, 0, 0), "alarm anı"); }
    if (o == SAAT_GUNES) {
      gunes++;
      if (b < son_binde) artiyor = 0;
      son_binde = b;
      DENE(t >= yerel(2026, 11, 23, 6, 50, 0) && t < yerel(2026, 11, 23, 7, 0, 0), "gün doğumu penceresi");
    }
  }
  DENE(alarm == 1 && gunes == 600 && artiyor && son_binde >= 998, "alarm bir kez (%d), gün doğumu 10 dk (%d s)", alarm, gunes);
  d.alarm_son = d.yatma_son = -1;
  alarm = 0;
  for (int64_t t = yerel(2026, 11, 28, 6, 0, 0); t < yerel(2026, 11, 28, 8, 0, 0); t += 30)  // cumartesi
    alarm += saat_olay(&a, &d, t, &b) != SAAT_YOK;
  DENE(alarm == 0, "hafta sonu alarm/gün doğumu");
  // meşgulken kaçan alarm: pencere içinde (07:09) çalar, sonra (07:10) çalmaz
  d.alarm_son = -1;
  DENE(saat_olay(&a, &d, yerel(2026, 11, 24, 7, 9, 30), &b) == SAAT_ALARM, "pencere içinde geç alarm");
  d.alarm_son = -1;
  DENE(saat_olay(&a, &d, yerel(2026, 11, 24, 7, 10, 0), &b) != SAAT_ALARM, "pencere dışında alarm");
  // saat 07:03'te ayarlandı: o günün alarmı hemen çalmaz; ertesi gün çalar
  saat_durum_kur(&a, &d, yerel(2026, 11, 24, 7, 3, 0));
  DENE(saat_olay(&a, &d, yerel(2026, 11, 24, 7, 3, 1), &b) == SAAT_YOK, "saat ayarlanınca alarm hemen çaldı");
  DENE(saat_olay(&a, &d, yerel(2026, 11, 25, 7, 0, 0), &b) == SAAT_ALARM, "ertesi gün alarm");
  // gece yarısına yakın alarm (00:05, gün doğumu 15 dk önceki günden başlar; gün: alarmın günü)
  a.alarm_saat = 0; a.alarm_dk = 5; a.alarm_gunes = 15; a.alarm_gunler = 1;  // yalnız pazartesi
  d.alarm_son = -1;
  DENE(saat_olay(&a, &d, yerel(2026, 11, 22, 23, 55, 0), &b) == SAAT_GUNES, "gece yarısını aşan gün doğumu");
  DENE(saat_olay(&a, &d, yerel(2026, 11, 23, 0, 5, 0), &b) == SAAT_ALARM, "00:05 alarmı");
  // yatma hatırlatması ve gece kilidi (21:00 - 07:00, gece yarısını aşar)
  saat_varsayilan(&a);
  a.yatma_acik = 1; a.yatma_saat = 21; a.yatma_dk = 0; a.kilit = 1; a.sabah_saat = 7; a.sabah_dk = 0;
  d.alarm_son = d.yatma_son = -1;
  int yatma = 0;
  for (int64_t t = yerel(2026, 11, 23, 20, 0, 0); t < yerel(2026, 11, 23, 23, 0, 0); t += 10)
    yatma += saat_olay(&a, &d, t, &b) == SAAT_YATMA;
  DENE(yatma == 1, "yatma hatırlatması bir kez (%d)", yatma);
  DENE(saat_gece_mi(&a, yerel(2026, 11, 23, 21, 0, 0)) && saat_gece_mi(&a, yerel(2026, 11, 24, 3, 0, 0)) &&
       !saat_gece_mi(&a, yerel(2026, 11, 24, 7, 0, 0)) && !saat_gece_mi(&a, yerel(2026, 11, 23, 20, 59, 59)), "gece kilidi");
  a.kilit = 0;
  DENE(!saat_gece_mi(&a, yerel(2026, 11, 23, 23, 0, 0)), "kilit kapalıyken gece");
  a.kilit = 1; a.yatma_saat = 13; a.yatma_dk = 0; a.sabah_saat = 15; a.sabah_dk = 0;  // gün içinde (öğle uykusu)
  DENE(saat_gece_mi(&a, yerel(2026, 11, 23, 14, 0, 0)) && !saat_gece_mi(&a, yerel(2026, 11, 23, 16, 0, 0)), "öğle kilidi");
}

// ---- alarm sesi: ADPCM, CRC, başlık ----
static void alarm_ses_denemesi(void) {
  DENE(alarm_crc32(0, (const uint8_t *)"123456789", 9) == 0xCBF43926u, "CRC-32 denetim değeri");
  enum { N = 8000 };
  static int16_t x[N], y[N], z[2 * N], z2[2 * N];
  static uint8_t v[N / 2];
  for (int i = 0; i < N; i++) x[i] = (int16_t)(12000 * sin(2 * M_PI * 440 * i / 8000.0) * exp(-i / 4000.0));
  Adpcm s = {0, 0}, c = {0, 0};
  adpcm_kodla(&s, x, N, v);
  adpcm_coz(&c, v, N, y);
  double se = 0, sx = 0;
  for (int i = 0; i < N; i++) { double e = y[i] - x[i]; se += e * e; sx += (double)x[i] * x[i]; }
  DENE(10 * log10(sx / se) > 20, "ADPCM SNR %.1f dB", 10 * log10(sx / se));
  int16_t o1 = 0, o2 = 0;
  alarm_ses_iki_kat(&o1, y, N, z);
  for (int i = 0; i < N; i += 100) alarm_ses_iki_kat(&o2, y + i, N - i < 100 ? N - i : 100, z2 + 2 * i);
  DENE(!memcmp(z, z2, sizeof z) && z[1] == y[0] && z[3] == y[1] && z[2] == (y[0] + y[1]) / 2, "16 kHz'e çıkarma");
  int16_t uc[3] = {32767, -32768, 32767};
  uint8_t uv[2];
  Adpcm us = {0, 0};
  adpcm_kodla(&us, uc, 3, uv);  // uçlar taşmaz
  DENE(us.tahmin >= -32768 && us.tahmin <= 32767 && us.indeks >= 0 && us.indeks <= 88, "ADPCM uç değerler");
  AlarmSesBaslik b;
  memset(&b, 0, sizeof b);
  b.sihir = ALARM_SES_SIHIR; b.surum = ALARM_SES_SURUM; b.sr = ALARM_SES_SR; b.n = N;
  strcpy(b.ad, "deneme");
  DENE(alarm_ses_baslik_gecerli(&b, 0xB000), "geçerli başlık");
  b.n = ALARM_SES_ORNEK_MAKS + 1;
  DENE(!alarm_ses_baslik_gecerli(&b, 0xB000), "uzun ses kabul edildi");
  b.n = 0x20000;
  DENE(!alarm_ses_baslik_gecerli(&b, 0xB000), "bölüme sığmayan ses");
  b.n = N; b.sr = 16000;
  DENE(!alarm_ses_baslik_gecerli(&b, 0xB000), "yanlış örnek hızı");
  b.sr = ALARM_SES_SR;
  memset(b.ad, 'a', sizeof b.ad);
  DENE(!alarm_ses_baslik_gecerli(&b, 0xB000), "NUL'süz ad");
  DENE(ALARM_SES_BASLIK + ALARM_SES_ORNEK_MAKS / 2 <= 0xB000, "en uzun ses alarm bölümüne sığmıyor");
}

// ---- mesaj, sayılar, yeni konuşma kalıpları ----
typedef struct { const char *k, *v; } KV;
static const char *kv_al(void *kul, const char *ad) {
  for (const KV *p = (const KV *)kul; p->k; p++) if (!strcmp(p->k, ad)) return p->v;
  return NULL;
}
static void mesaj_denemesi(void) {
  char o[AYAR_MESAJ_BAYT], b[1024];
  DENE(mesaj_temizle("  Bugün   2 kurabiye var!  ", o) == AD_TAMAM && !strcmp(o, "Bugün 2 kurabiye var!"), "mesaj: %s", o);
  DENE(mesaj_temizle("Saat 8\xE2\x80\x99" "de \xE2\x80\x9C" "\xC3\xA7\xC4\xB1" "k\xE2\x80\x9D\xE2\x80\xA6", o) == AD_TAMAM &&
       !strcmp(o, "Saat 8'de '\xC3\xA7\xC4\xB1" "k'..."), "kıvrık tırnak / üç nokta: %s", o);
  DENE(mesaj_temizle("<b>", o) == AD_HARF && mesaj_temizle("a\"b", o) == AD_HARF && mesaj_temizle("a\\b", o) == AD_HARF,
       "izinsiz karakter kabul edildi");
  char uzun[200];
  memset(uzun, 'a', 121);
  uzun[121] = 0;
  DENE(mesaj_temizle(uzun, o) == AD_UZUN, "121 karakter kabul edildi");
  uzun[120] = 0;
  DENE(mesaj_temizle(uzun, o) == AD_TAMAM, "120 karakter reddedildi");
  sayi_yazi(0, b, sizeof b);
  DENE(!strcmp(b, "sıfır"), "0: %s", b);
  sayi_yazi(1234567, b, sizeof b);
  DENE(!strcmp(b, "bir milyon iki yüz otuz dört bin beş yüz altmış yedi"), "1234567: %s", b);
  sayi_yazi(1000, b, sizeof b);
  DENE(!strcmp(b, "bin"), "1000: %s", b);
  sayi_yazi(100, b, sizeof b);
  DENE(!strcmp(b, "yüz"), "100: %s", b);
  sayi_yazi(2019, b, sizeof b);
  DENE(!strcmp(b, "iki bin on dokuz"), "2019: %s", b);
  sayilari_yaz("Saat 07:30'da 3 kek, 8'de çık", b, sizeof b);
  DENE(!strcmp(b, "Saat yedi otuzda üç kek, sekizde çık"), "sayilari_yaz: %s", b);
  sayilari_yaz("Kod 12345678901", b, sizeof b);
  DENE(!strcmp(b, "Kod bir, iki, üç, dört, beş, altı, yedi, sekiz, dokuz, sıfır, bir"), "uzun dizi: %s", b);
  alarm_metni("Emre", "Bugün 2 kurabiye var!", b, sizeof b);
  DENE(!strcmp(b, "Günaydın Emre! Kalkma vakti geldi. Bugün iki kurabiye var!"), "alarm: %s", b);
  alarm_metni("", "", b, sizeof b);
  DENE(!strcmp(b, "Günaydın! Kalkma vakti geldi."), "adsız alarm: %s", b);
  surpriz_metni("Emre", "Seni seviyorum", b, sizeof b);
  DENE(!strcmp(b, "Emre, sana bir mesaj var: Seni seviyorum"), "sürpriz: %s", b);
  for (int c = 0; c < 6; c++) {
    selam_metni_cesit(c, "Emre", "Keloğlan", b, sizeof b);
    DENE(strstr(b, "Emre") && strstr(b, "Keloğlan"), "selam çeşidi %d: %s", c, b);
  }
  selam_metni_cesit(0, "Emre", "Keloğlan", b, sizeof b);
  DENE(!strcmp(b, "Merhaba Emre, şimdi sana Keloğlan'ın hikâyesini okuyacağım."), "ilk selam değişti: %s", b);
  selam_metni_cesit(1, NULL, "Bip", b, sizeof b);
  DENE(!strcmp(b, "Bak kim geldi: Bip! Dinlemeye hazır mısın?"), "adsız selam 1: %s", b);
  // form: yeni alanlar
  Ayarlar a;
  ayar_varsayilan(&a);
  char h[160];
  KV F[] = {{"alarm_acik", "1"}, {"alarm_saat", "06:45"}, {"alarm_gunler", "65"},
                                       {"alarm_gunes", "15"}, {"alarm_tur", "2"}, {"okunus", "Yasmin"},
                                       {"alarm_mesaj", "Kalk bakalım!"}, {"yatma_acik", "1"}, {"yatma_saat", "20:15"},
                                       {"kilit", "1"}, {"sabah_saat", "06:30"}, {NULL, NULL}};
  DENE(ayar_form_uygula(&a, kv_al, F, h, sizeof h) == 0, "yeni alanlar: %s", h);
  DENE(a.zaman.alarm_acik && a.zaman.alarm_saat == 6 && a.zaman.alarm_dk == 45 && a.zaman.alarm_gunler == 65 &&
       a.zaman.alarm_gunes == 15 && a.alarm_tur == ALARM_YUKLENEN && !strcmp(a.okunus, "Yasmin") &&
       !strcmp(a.alarm_mesaj, "Kalk bakalım!") && a.zaman.yatma_saat == 20 && a.zaman.yatma_dk == 15 && a.zaman.kilit &&
       a.zaman.sabah_saat == 6 && a.zaman.sabah_dk == 30, "yeni alanlar uygulanmadı");
  char j[1024];
  ayar_json(&a, j, sizeof j);
  DENE(strstr(j, "\"alarm_saat\":\"06:45\"") && strstr(j, "\"okunus\":\"Yasmin\"") && strstr(j, "\"tz_dk\":180"), "json: %s", j);
  KV G1[] = {{"alarm_gunes", "45"}, {NULL, NULL}}, G2[] = {{"alarm_tur", "3"}, {NULL, NULL}},
     G3[] = {{"okunus", "Ya5min"}, {NULL, NULL}};
  Ayarlar e = a;
  DENE(ayar_form_uygula(&a, kv_al, G1, h, sizeof h) < 0 && ayar_form_uygula(&a, kv_al, G2, h, sizeof h) < 0 &&
       ayar_form_uygula(&a, kv_al, G3, h, sizeof h) < 0 && !memcmp(&a, &e, sizeof a), "geçersiz yeni alanlar");
}

// ---- selam ----
static void selam_denemesi(void) {
  // donanım figürlerinin hepsi (kimliğe göre: tablo sırası değişse de) ve beklenen ekleri
  static const char *const BEK[][2] = {
      {"keloglan", "Keloğlan'ın"},           {"gece", "Ay Dede'nin"},          {"pamuk_prenses", "Pamuk Prenses'in"},
      {"pinokyo", "Pinokyo'nun"},            {"alaaddin", "Alaaddin'in"},      {"nasreddin_hoca", "Nasreddin Hoca'nın"},
      {"bulut", "Bulut'un"},                 {"zipzip", "Zıpzıp'ın"},          {"tontis", "Tontiş'in"},
      {"bilge_baykus", "Bilge Baykuş'un"},   {"ejderha_yavrusu", "Ejderha Yavrusu'nun"},
      {"tek_boynuzlu_at", "Tek Boynuzlu At'ın"}, {"bip", "Bip'in"},        {"fistik", "Fıstık'ın"}};
  char b[160];
  for (int d = 0; d < DONANIM_N; d++) {
    const char *bek = NULL;
    for (size_t i = 0; i < sizeof BEK / sizeof BEK[0]; i++)
      if (!strcmp(BEK[i][0], DONANIM_KIMLIK[d])) bek = BEK[i][1];
    DENE(bek != NULL, "%s için beklenen selam eki yazılmamış", DONANIM_KIMLIK[d]);
    if (!bek) continue;
    selam_iyelik(DONANIM_AD[d], b, sizeof b);
    DENE(!strcmp(b, bek), "%s -> %s (beklenen %s)", DONANIM_AD[d], b, bek);
  }
  // üründen çıkan (lisanslı) figürlerin adları: kural denemesi olarak kalır (yabancı adda "y", Chase istisnası)
  static const char *const DIGER[][2] = {{"Niloya", "Niloya'nın"},     {"Maşa", "Maşa'nın"},     {"Pepee", "Pepee'nin"},
                                        {"Doru", "Doru'nun"},         {"Hayri", "Hayri'nin"},   {"Şakir", "Şakir'in"},
                                        {"Elsa", "Elsa'nın"},         {"Chase", "Chase'in"},    {"Örümcek Adam", "Örümcek Adam'ın"},
                                        {"Hello Kitty", "Hello Kitty'nin"},
                                        {"Pamuk", "Pamuk'un"}, {"Gülüş", "Gülüş'ün"}, {"Ömür", "Ömür'ün"},
                                        {"Ali", "Ali'nin"},     {"Ayşe", "Ayşe'nin"}, {"Arı", "Arı'nın"},
                                        {"Kuzu", "Kuzu'nun"},   {"Örtü", "Örtü'nün"}, {"Mary", "Mary'nin"},
                                        {"Tony", "Tony'nin"},   {"Kral Şakir", "Kral Şakir'in"},
                                        {"BALIK", "BALIK'ın"},  {"Iğdır", "Iğdır'ın"}, {"İnek", "İnek'in"}};
  for (size_t i = 0; i < sizeof DIGER / sizeof DIGER[0]; i++) {
    selam_iyelik(DIGER[i][0], b, sizeof b);
    DENE(!strcmp(b, DIGER[i][1]), "%s -> %s (beklenen %s)", DIGER[i][0], b, DIGER[i][1]);
  }
  selam_metni("Emre", "Pamuk", b, sizeof b);
  DENE(!strcmp(b, "Merhaba Emre, şimdi sana Pamuk'un hikâyesini okuyacağım."), "selam: %s", b);
  selam_metni("", "Hello Kitty", b, sizeof b);
  DENE(!strcmp(b, "Merhaba, şimdi sana Hello Kitty'nin hikâyesini okuyacağım."), "adsız selam: %s", b);
  selam_metni(NULL, "Örümcek Adam", b, sizeof b);
  DENE(!strcmp(b, "Merhaba, şimdi sana Örümcek Adam'ın hikâyesini okuyacağım."), "adsız selam: %s", b);
  ninni_selam_metni("Emre", b, sizeof b);
  DENE(!strcmp(b, "İyi geceler Emre, şimdi sana bir ninni söyleyeceğim."), "ninni selamı: %s", b);
  ninni_selam_metni("", b, sizeof b);
  DENE(!strcmp(b, "İyi geceler, şimdi sana bir ninni söyleyeceğim."), "adsız ninni selamı: %s", b);
  rakam_metni("4729", b, sizeof b);
  DENE(!strcmp(b, "dört, yedi, iki, dokuz"), "rakamlar: %s", b);
}

// ---- ayarlar ----
typedef struct { const char *ad[12], *deger[12]; int n; } Form;
static const char *form_al(void *kul, const char *ad) {
  Form *f = (Form *)kul;
  for (int i = 0; i < f->n; i++) if (!strcmp(f->ad[i], ad)) return f->deger[i];
  return NULL;
}
static int form(Ayarlar *a, char *h, const char *ad, const char *deger) {
  Form f = {{ad}, {deger}, 1};
  return ayar_form_uygula(a, form_al, &f, h, 128);
}
static void ayar_denemesi(void) {
  Ayarlar a;
  char h[128], o[AYAR_AD_BAYT];
  ayar_varsayilan(&a);
  DENE(a.ses_maks == 7 && a.uyku_dk == 20 && a.cekilince == CEKILINCE_CUMLE && a.nefes && a.muzik, "varsayılan");
  DENE(ad_temizle("  Çağrı   Şeyma ", o) == AD_TAMAM && !strcmp(o, "Çağrı Şeyma"), "Türkçe ad: '%s'", o);
  DENE(ad_temizle("İĞÜŞÖÇığüşöçâîû", o) == AD_TAMAM, "Türkçe harfler");
  DENE(ad_temizle("Abcdefghijklmnoprstu", o) == AD_TAMAM, "20 harf");
  DENE(ad_temizle("Abcdefghijklmnoprstuv", o) == AD_UZUN, "21 harf");
  DENE(ad_temizle("Ğğğğğğğğğğğğğğğğğğğğ", o) == AD_TAMAM, "20 Türkçe harf (40 bayt)");
  DENE(ad_temizle("Ali Veli Can Deniz Ece", o) == AD_UZUN, "boşluk dahil 22");
  DENE(ad_temizle("Emre1", o) == AD_HARF && ad_temizle("Em<re>", o) == AD_HARF && ad_temizle("Emre\"", o) == AD_HARF,
       "harf olmayan");
  DENE(ad_temizle("Ali\xC3", o) == AD_HARF && ad_temizle("\xF0\x9F\x98\x80", o) == AD_HARF, "bozuk UTF-8 / emoji");
  DENE(ad_temizle("", o) == AD_TAMAM && !o[0] && ad_temizle("   ", o) == AD_TAMAM && !o[0], "boş ad");
  Form f = {{"ad", "ses_maks", "uyku_dk", "parlaklik", "cekilince", "nefes", "arka_goster", "muzik"},
            {"Emre", "5", "30", "40", "1", "0", "0", "0"}, 8};
  DENE(ayar_form_uygula(&a, form_al, &f, h, sizeof h) == 0, "geçerli form: %s", h);
  DENE(!strcmp(a.ad, "Emre") && a.ses_maks == 5 && a.uyku_dk == 30 && a.parlaklik == 40 &&
       a.cekilince == CEKILINCE_HEMEN && !a.nefes && !a.arka_goster && !a.muzik, "form uygulanmadı");
  Ayarlar once = a;
  DENE(form(&a, h, "ses_maks", "8") && form(&a, h, "ses_maks", "0") && form(&a, h, "ses_maks", "x"), "ses sınırı");
  DENE(form(&a, h, "uyku_dk", "15") && form(&a, h, "parlaklik", "101") && form(&a, h, "cekilince", "3") &&
       form(&a, h, "nefes", "2") && form(&a, h, "parlaklik", "-1") && form(&a, h, "ad", "Emre!"), "geçersizler");
  DENE(!memcmp(&a, &once, sizeof a), "geçersiz form ayarı değiştirdi");
  Form g = {{"ad", "ses_maks"}, {"Zeynep", "9"}, 2};  // biri geçersizse hiçbiri uygulanmaz
  DENE(ayar_form_uygula(&a, form_al, &g, h, sizeof h) && !strcmp(a.ad, "Emre"), "yarım uygulama");
  DENE(strstr(h, "1 ile 7") != NULL, "hata metni: %s", h);
  char j[256];
  ayar_json(&a, j, sizeof j);
  DENE(strstr(j, "\"ad\":\"Emre\"") && strstr(j, "\"uyku_dk\":30") && strstr(j, "\"muzik\":0"), "json: %s", j);
  Ayarlar bozuk;
  memset(&bozuk, 0xEE, sizeof bozuk);
  ayar_duzelt(&bozuk);
  DENE(bozuk.ses_maks == 7 && bozuk.uyku_dk == 20 && bozuk.parlaklik == 100 && bozuk.cekilince == 0, "düzeltme");
}

// ---- halka ----
static uint8_t kare[HALKA_MAKS][3];
static int yanan(int n) {
  int k = 0;
  for (int i = 0; i < n; i++) k += kare[i][0] || kare[i][1] || kare[i][2];
  return k;
}
static int en_parlak(int n) {
  int m = 0;
  for (int i = 0; i < n; i++) for (int c = 0; c < 3; c++) m = kare[i][c] > m ? kare[i][c] : m;
  return m;
}
static void halka_denemesi(void) {
  Halka h;
  const int N = 35;
  halka_kur(&h, N, 25, 600);
  const int pp = donanim_kimlik("pamuk_prenses");
  DENE(pp >= 0, "Pamuk Prenses donanım tablosunda yok");
  const uint8_t *nil = &DONANIM_RENK[3 * (pp >= 0 ? pp : 0)];  // figür rengi (Pamuk Prenses: kırmızı-pembe)
  // açılış: gökkuşağı (farklı renkler), sonra boşta
  halka_taban(&h, HT_ACILIS, 1000);
  halka_ciz(&h, 1000 + HALKA_ACILIS_MS - 1, kare);
  DENE(yanan(N) == N && kare[0][0] > kare[0][2] && kare[N / 2][2] > kare[N / 2][0], "gökkuşağı");
  halka_ciz(&h, 1000 + HALKA_ACILIS_MS + HALKA_ACILIS_SON_MS + 10, kare);
  DENE(h.taban == HT_BOSTA, "açılıştan sonra boşta değil");
  // boşta nefes: çok sönük beyaz; nefes kapalıysa sönük
  halka_ciz(&h, 10000, kare);
  DENE(yanan(N) == N && en_parlak(N) <= 64 * 13 / 100 + 1 && kare[0][0] == kare[0][1], "nefes");
  h.nefes = 0;
  halka_ciz(&h, 10000, kare);
  DENE(yanan(N) == 0, "nefes kapalı");
  // dolma: 0,6 s'de dolar, figür renginde
  halka_renk(&h, nil);
  halka_taban(&h, HT_DOLMA, 20000);
  halka_ciz(&h, 20000 + HALKA_DOLMA_MS / 2, kare);
  int yari = yanan(N);
  halka_ciz(&h, 20000 + HALKA_DOLMA_MS, kare);
  DENE(yari > N / 3 && yari < 2 * N / 3 && yanan(N) == N, "dolma %d", yari);
  DENE(kare[0][0] == (nil[0] * 25 + 50) / 100 && kare[0][1] == (nil[1] * 25 + 50) / 100, "tavan %%25: %d %d", kare[0][0],
       kare[0][1]);
  // okuma: 3/10 cümle -> 10 LED dolu, kalanı sönük
  halka_taban(&h, HT_OKUMA, 30000);
  halka_ilerleme(&h, 3, 10);
  halka_ciz(&h, 30000, kare);
  DENE(halka_dolu(&h) == 10 && kare[9][0] > 3 * kare[10][0] && kare[10][0] > 0, "ilerleme");
  int sessiz = kare[0][0];
  h.ses = 255;
  halka_ciz(&h, 30000, kare);
  DENE(kare[0][0] > sessiz, "konuşma sesiyle dalgalanma");
  halka_ilerleme(&h, 10, 10);
  halka_ciz(&h, 30000, kare);
  DENE(halka_dolu(&h) == N, "bitti: hepsi dolu");
  // üst durumlar: dinle (beyaz nokta), onay (yeşil), anlaşılmadı (turuncu), ses (0..maks), süreleri dolunca biter
  halka_ust(&h, HU_DINLE, 40000, 4500);
  halka_ciz(&h, 40000, kare);
  DENE(kare[0][0] == kare[0][1] && kare[0][1] == kare[0][2] && kare[0][0] > kare[5][0], "dinle: beyaz nokta");
  halka_ust(&h, HU_ONAY, 41000, HALKA_ONAY_MS);
  halka_ciz(&h, 41000, kare);
  DENE(kare[0][1] > kare[0][0] && yanan(N) == N, "onay yeşil");
  halka_ciz(&h, 41000 + 130, kare);
  DENE(yanan(N) == 0, "onay yanıp sönmüyor");
  halka_ciz(&h, 41000 + HALKA_ONAY_MS + 1, kare);
  DENE(h.ust == HU_YOK && h.taban == HT_OKUMA, "onay bitmedi");
  halka_ust(&h, HU_ANLASILMADI, 42000, HALKA_ONAY_MS);
  halka_ciz(&h, 42000, kare);
  DENE(kare[0][0] > kare[0][1] && kare[0][1] > kare[0][2], "anlaşılmadı turuncu");
  h.duzey = 3; h.maks = 7;
  halka_ust(&h, HU_SES, 43000, HALKA_SES_MS);
  halka_ciz(&h, 43000, kare);
  DENE(yanan(N) == (N * 3 + 3) / 7, "ses göstergesi %d", yanan(N));
  halka_ciz(&h, 43000 + HALKA_SES_MS, kare);
  DENE(h.ust == HU_YOK, "ses göstergesi 2 s'de bitmedi");
  // gece: gece mavisi zemin + parlayan yıldızlar; sönme 60 s
  const int gd = donanim_kimlik("gece");
  DENE(gd >= 0, "gece figürü donanım tablosunda yok");
  halka_renk(&h, &DONANIM_RENK[3 * (gd >= 0 ? gd : 0)]);
  halka_taban(&h, HT_GECE, 50000);
  int yildiz_en = 0, zemin_mavi = 1;
  for (uint32_t t = 50000; t < 70000; t += 250) {
    halka_ciz(&h, t, kare);
    for (int i = 0; i < N; i++) {
      if (kare[i][2] < kare[i][0]) zemin_mavi = 0;
      yildiz_en = kare[i][0] > yildiz_en ? kare[i][0] : yildiz_en;
    }
  }
  DENE(zemin_mavi && yildiz_en > 20, "gece: mavi zemin, yıldızlar (%d)", yildiz_en);
  h.sonme_ms = 80000;
  halka_ciz(&h, 80000 + 30000, kare);
  int yarim = en_parlak(N);
  halka_ciz(&h, 80000 + HALKA_SONME_MS, kare);
  DENE(yarim > 0 && yanan(N) == 0, "gece sönmesi");
  // hata: kırmızı yanıp sönme; ayar: turkuaz
  halka_taban(&h, HT_HATA, 90000);
  halka_ciz(&h, 90000, kare);
  DENE(kare[0][0] > 0 && !kare[0][1] && !kare[0][2], "hata kırmızı");
  halka_ciz(&h, 90400, kare);
  DENE(yanan(N) == 0, "hata yanıp sönmüyor");
  halka_taban(&h, HT_AYAR, 91000);
  halka_ciz(&h, 91000 + 1250, kare);
  DENE(!kare[0][0] && kare[0][1] > kare[0][2] && kare[0][2] > 0, "ayar turkuaz");
  // parlaklık ayarı ve akım sınırı: beyaz tam halka (ses göstergesi maks) %25'te 35 LED ≈ 527 mA
  halka_ust(&h, HU_SES, 92000, 2000);
  h.duzey = h.maks = 7;
  halka_ciz(&h, 92000, kare);
  DENE(en_parlak(N) == 64 && h.akim_ma <= 600, "beyaz tam: %d, %d mA", en_parlak(N), h.akim_ma);
  h.parlaklik = 50;
  halka_ciz(&h, 92000, kare);
  DENE(en_parlak(N) == 32, "parlaklık %%50: %d", en_parlak(N));
  h.parlaklik = 0;
  halka_ciz(&h, 92000, kare);
  DENE(yanan(N) == 0, "parlaklık 0: kapalı");
  Halka g;
  halka_kur(&g, 60, 100, 600);  // tavan %100, 60 LED beyaz: 60 x 60 mA = 3,6 A -> 600 mA'e kısılmalı
  g.duzey = g.maks = 1;
  halka_ust(&g, HU_SES, 0, 2000);
  halka_ciz(&g, 0, kare);
  int top = 0;
  for (int i = 0; i < 60; i++) top += kare[i][0] + kare[i][1] + kare[i][2];
  DENE(g.akim_ma <= 600 && top * HALKA_LED_MA / 255 <= 600, "akım sınırı: %d mA", top * HALKA_LED_MA / 255);
}

// ---- müzik kutusu ----
static void muzik_denemesi(void) {
  MuzikKutusu m;
  mk_kur(&m);
  static int16_t b[MK_SR * 4];
  memset(b, 0, sizeof b);
  mk_karistir(&m, b, MK_SR * 4, 256);
  int en = 0, sifir_gecis = 0;
  for (int i = 0; i < MK_SR * 4; i++) {
    int v = abs(b[i]);
    en = v > en ? v : en;
    sifir_gecis += i && ((b[i] >= 0) != (b[i - 1] >= 0));
  }
  DENE(en > MK_TEPE / 2 && en <= MK_TEPE + 1, "tepe %d (beklenen <= %d)", en, MK_TEPE);
  DENE(sifir_gecis > 4 * 2 * 400, "ses yok gibi (%d sıfır geçişi)", sifir_gecis);
  int16_t k[1000];
  memset(k, 0, sizeof k);
  mk_kur(&m);
  mk_karistir(&m, k, 1000, 0);
  int sus = 1;
  for (int i = 0; i < 1000; i++) sus &= k[i] == 0;
  DENE(sus, "seviye 0'da ses var");
  for (int i = 0; i < 1000; i++) k[i] = 32000;
  mk_kur(&m);
  mk_karistir(&m, k, 1000, 256);
  int doyum = 1;
  for (int i = 0; i < 1000; i++) doyum &= k[i] >= 31000;
  DENE(doyum, "doyum (taşma)");
}

// ---- donanım figürleri ve yerleşik metinler ----
static void donanim_denemesi(void) {
  int gece = -1, hikaye = 0;
  for (int d = 0; d < DONANIM_N; d++) {
    DENE(d == 0 || DONANIM_NFC[d] > DONANIM_NFC[d - 1], "nfc_no sırası (artan, tekrarsız)");
    if (DONANIM_MOD[d] == MOD_UYKU) gece = d;
    if (DONANIM_MOD[d] == MOD_HIKAYE) {
      hikaye++;
      DENE(DONANIM_MODEL[d] >= 0, "%s: hikâye figürü modelde yok", DONANIM_KIMLIK[d]);
      for (int e = 0; e < d; e++) DENE(DONANIM_MODEL[e] != DONANIM_MODEL[d], "model figürü iki kez");
    }
  }
  DENE(gece >= 0 && !strcmp(DONANIM_KIMLIK[gece], "gece") && DONANIM_NFC[gece] == 12, "gece figürü");
  // 26 Ekim 2026: lisanslı figürler üründen çıktı (data/figur_donanim.json 'cikarildi'): tabloda ne kimlikleri ne
  // numaraları var; Keloğlan (4) kalır, yeni 12 figür 13-24 (numaralar asla yeniden kullanılmaz)
  static const char *const CIKAN[] = {"niloya", "masa", "pepee", "doru", "hayri", "sakir", "elsa", "chase",
                                      "orumcek_adam", "hello_kitty"};
  for (size_t i = 0; i < sizeof CIKAN / sizeof CIKAN[0]; i++) DENE(donanim_kimlik(CIKAN[i]) < 0, "%s tabloda", CIKAN[i]);
  for (int d = 0; d < DONANIM_N; d++)
    DENE(DONANIM_NFC[d] == 4 || DONANIM_NFC[d] >= 12, "%s: çıkarılan figürün numarası (%d)", DONANIM_KIMLIK[d],
         DONANIM_NFC[d]);
  DENE(hikaye == 13 && DONANIM_N == 14 && DONANIM_NFC[DONANIM_N - 1] == 24, "13 hikâye figürü + Ay Dede (%d)", hikaye);
  DENE(donanim_kimlik("keloglan") >= 0 && DONANIM_NFC[donanim_kimlik("keloglan")] == 4, "Keloğlan 4");
  int yerlesik_var = 0;
  for (size_t i = 0; i < sizeof YERLESIK / sizeof YERLESIK[0]; i++)
    if (!strcmp(YERLESIK[i].kimlik, "gece") && YERLESIK[i].n == 100) yerlesik_var = 1;
  DENE(DONANIM_MODEL[gece] < 0 && yerlesik_var, "gece figürü 100 sabit ninniyi okumalı (model değil)");
  for (int d = 0; d < DONANIM_N; d++) DENE(DONANIM_NFC[d] != AYAR_KARTI_NFC, "ayar kartı numarası çakışıyor");
}

int main(void) {
  etiket_denemesi();
  nfc_denemesi();
  ayar_karti_denemesi();
  saat_denemesi();
  alarm_ses_denemesi();
  mesaj_denemesi();
  selam_denemesi();
  ayar_denemesi();
  halka_denemesi();
  muzik_denemesi();
  donanim_denemesi();
  printf(hata ? "urun_test: %d HATA\n" : "urun_test: hepsi geçti\n", hata);
  return hata != 0;
}
