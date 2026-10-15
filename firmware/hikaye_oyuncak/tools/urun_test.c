// Ürün parçalarının bilgisayarda denemesi (saf C başlıklar): etiket kaydı (etiket.h: kodla/çöz/CRC, bozulmalar),
// taslak NFC sürücüsünde etiket belleğine yazma + doğrulama (nfc.h, NFC_OKUYUCU 0), selamlama ekleri (selam.h: 11
// figür + adsız + ninni), ayar formu doğrulaması (ayarlar.h), halka durumları ve sınırları (halka.h), müzik kutusu
// (muzik_kutusu.h), donanım figürü tablosu (generated/figur_donanim.h, yerlesik.h).
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

static int hata = 0;
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
  DENE(nfc_etiket_no(klasik, 4, &kayit) == 1 && !kayit, "UID tablosu (Niloya)");
  nfc_sahte_koy_no(12);
  DENE(nfc_uid_oku(u, sizeof u) == 7 && nfc_etiket_no(u, 7, NULL) == 12, "programlanmış gece figürü");
  nfc_sahte_kaldir();
  DENE(nfc_uid_oku(u, sizeof u) == 0, "kalkan etiket görüldü");
}

// ---- selam ----
static void selam_denemesi(void) {
  static const char *const BEK[DONANIM_N] = {"Niloya'nın", "Maşa'nın", "Pepee'nin", "Keloğlan'ın", "Doru'nun",
                                             "Hayri'nin", "Şakir'in", "Elsa'nın", "Chase'in", "Örümcek Adam'ın",
                                             "Hello Kitty'nin", "Ay Dede'nin"};
  char b[160];
  for (int d = 0; d < DONANIM_N; d++) {
    selam_iyelik(DONANIM_AD[d], b, sizeof b);
    DENE(!strcmp(b, BEK[d]), "%s -> %s (beklenen %s)", DONANIM_AD[d], b, BEK[d]);
  }
  static const char *const DIGER[][2] = {{"Pamuk", "Pamuk'un"}, {"Gülüş", "Gülüş'ün"}, {"Ömür", "Ömür'ün"},
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
  const uint8_t *nil = &DONANIM_RENK[0];
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
  DENE(kare[0][0] == (255 * 25 + 50) / 100 && kare[0][1] == (111 * 25 + 50) / 100, "tavan %%25: %d %d", kare[0][0], kare[0][1]);
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
  halka_renk(&h, &DONANIM_RENK[3 * 11]);
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
  int gece = -1;
  for (int d = 0; d < DONANIM_N; d++) {
    DENE(DONANIM_NFC[d] == d + 1, "nfc_no sırası");
    if (DONANIM_MOD[d] == MOD_UYKU) gece = d;
  }
  DENE(gece == 11 && !strcmp(DONANIM_KIMLIK[gece], "gece") && DONANIM_NFC[gece] == 12, "gece figürü");
  int yerlesik_var = 0;
  for (size_t i = 0; i < sizeof YERLESIK / sizeof YERLESIK[0]; i++)
    if (!strcmp(YERLESIK[i].kimlik, "gece") && YERLESIK[i].n == 100) yerlesik_var = 1;
  DENE(DONANIM_MODEL[gece] < 0 && yerlesik_var, "gece figürü 100 sabit ninniyi okumalı (model değil)");
  for (int d = 0; d < DONANIM_N; d++) DENE(DONANIM_NFC[d] != AYAR_KARTI_NFC, "ayar kartı numarası çakışıyor");
}

int main(void) {
  etiket_denemesi();
  nfc_denemesi();
  selam_denemesi();
  ayar_denemesi();
  halka_denemesi();
  muzik_denemesi();
  donanim_denemesi();
  printf(hata ? "urun_test: %d HATA\n" : "urun_test: hepsi geçti\n", hata);
  return hata != 0;
}
