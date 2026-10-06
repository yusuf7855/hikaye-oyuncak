// dugmeler.h'nin bilgisayarda denemesi: 10 ms'de bir örnekleme ile sekme süzgeci, kısa/uzun basış, OYNAT + FİGÜR/YER
// (ses aç/kıs), FİGÜR + YER (arka plan), halka taşması, millis taşması.
// Derle:  cc -O2 -Wall -o /tmp/dugme_test firmware/hikaye_oyuncak/tools/dugme_test.c
// Çalıştır: /tmp/dugme_test   (çıkış kodu 0: hepsi geçti)
#include <stdio.h>
#include <string.h>

#include "../dugmeler.h"

static Dugmeler g;
static bool seviye[DUGME_N];
static uint32_t simdi;
static int hata = 0;

static void sifirla(uint32_t t0) {
  memset(&g, 0, sizeof g);
  memset(seviye, 0, sizeof seviye);
  simdi = t0;
}
static void bekle(int ms) {  // 10 ms'de bir örnekle
  for (int t = 0; t < ms; t += 10) {
    dugme_adim(&g, seviye, simdi);
    simdi += 10;
  }
}
static void bas(int d) { seviye[d] = true; }
static void birak(int d) { seviye[d] = false; }
// Halkadaki olayları beklenenle karşılaştırır (OLAY_YOK ile biten dizi)
static void bekle_olaylar(int satir, const uint8_t *bek) {
  Olay o;
  int i = 0;
  while (halka_al(&g.h, &o)) {
    if (bek[i] != o.tur) { printf("HATA (satır %d): %d. olay %s, beklenen %s\n", satir, i, OLAY_AD[o.tur], OLAY_AD[bek[i]]); hata++; return; }
    i++;
  }
  if (bek[i] != OLAY_YOK) { printf("HATA (satır %d): %d. olay gelmedi (%s)\n", satir, i, OLAY_AD[bek[i]]); hata++; }
}
#define OLAYLAR(...)                                        \
  do {                                                      \
    const uint8_t b_[] = {__VA_ARGS__, OLAY_YOK};           \
    bekle_olaylar(__LINE__, b_);                            \
  } while (0)
#define OLAY_YOK_BEKLE()                                    \
  do {                                                      \
    const uint8_t b_[] = {OLAY_YOK};                        \
    bekle_olaylar(__LINE__, b_);                            \
  } while (0)

static void dene(uint32_t t0) {
  // kısa basış: bırakınca bir olay
  sifirla(t0);
  bas(DUGME_FIGUR); bekle(120);
  OLAY_YOK_BEKLE();
  birak(DUGME_FIGUR); bekle(60);
  OLAYLAR(OLAY_FIGUR);

  // sekme: 10 ms'de bir açılıp kapanan kontak (süzgeçten kısa) olay vermez; sonra kararlı basış tek olay
  sifirla(t0);
  for (int i = 0; i < 6; i++) { seviye[DUGME_YER] = i & 1; bekle(10); }
  birak(DUGME_YER); bekle(60);
  OLAY_YOK_BEKLE();
  bas(DUGME_YER); bekle(20); birak(DUGME_YER); bekle(10); bas(DUGME_YER); bekle(200);
  for (int i = 0; i < 4; i++) { seviye[DUGME_YER] = i & 1; bekle(10); }
  birak(DUGME_YER); bekle(60);
  OLAYLAR(OLAY_YER);

  // uzun basış: bırakınca uzun olay
  sifirla(t0);
  bas(DUGME_OYNAT); bekle(1200);
  OLAY_YOK_BEKLE();
  birak(DUGME_OYNAT); bekle(60);
  OLAYLAR(OLAY_OYNAT_UZUN);
  bas(DUGME_FIGUR); bekle(900); birak(DUGME_FIGUR); bekle(60);
  OLAYLAR(OLAY_FIGUR_UZUN);
  bas(DUGME_YER); bekle(300); birak(DUGME_YER); bekle(60);
  OLAYLAR(OLAY_YER);

  // OYNAT basılıyken FİGÜR iki kez, YER bir kez: ses +, +, -; OYNAT bırakılınca (uzun olsa da) kendi olayı yok
  sifirla(t0);
  bas(DUGME_OYNAT); bekle(200);
  bas(DUGME_FIGUR); bekle(100); birak(DUGME_FIGUR); bekle(100);
  bas(DUGME_FIGUR); bekle(100); birak(DUGME_FIGUR); bekle(1000);
  bas(DUGME_YER); bekle(100); birak(DUGME_YER); bekle(100);
  birak(DUGME_OYNAT); bekle(60);
  OLAYLAR(OLAY_SES_ARTI, OLAY_SES_ARTI, OLAY_SES_EKSI);
  bas(DUGME_OYNAT); bekle(100); birak(DUGME_OYNAT); bekle(60);  // sonra OYNAT yine normal
  OLAYLAR(OLAY_OYNAT);

  // FİGÜR + YER birlikte 3,5 s: bir kez arka plan; tek tek olayları yok
  sifirla(t0);
  bas(DUGME_FIGUR); bekle(200); bas(DUGME_YER); bekle(3500);
  birak(DUGME_FIGUR); bekle(50); birak(DUGME_YER); bekle(60);
  OLAYLAR(OLAY_ARKA);
  // kısa ikili basış: hiçbir şey
  bas(DUGME_YER); bekle(100); bas(DUGME_FIGUR); bekle(500); birak(DUGME_YER); birak(DUGME_FIGUR); bekle(60);
  OLAY_YOK_BEKLE();
  bas(DUGME_FIGUR); bekle(100); birak(DUGME_FIGUR); bekle(60);
  OLAYLAR(OLAY_FIGUR);

  // halka taşması: 40 basış, en çok OLAY_HALKA - 1 olay kalır, hepsi FİGÜR
  sifirla(t0);
  for (int i = 0; i < 40; i++) { bas(DUGME_FIGUR); bekle(60); birak(DUGME_FIGUR); bekle(60); }
  Olay o;
  int n = 0;
  while (halka_al(&g.h, &o)) { n++; if (o.tur != OLAY_FIGUR) { printf("HATA: taşmada yanlış olay\n"); hata++; } }
  if (n != OLAY_HALKA - 1) { printf("HATA: taşmada %d olay\n", n); hata++; }
  // basılı mı
  sifirla(t0);
  bas(DUGME_YER); bekle(50);
  if (!dugme_basili(&g)) { printf("HATA: basılı görünmüyor\n"); hata++; }
  birak(DUGME_YER); bekle(50);
  if (dugme_basili(&g)) { printf("HATA: bırakıldı görünmüyor\n"); hata++; }
}

int main(void) {
  dene(1000);
  dene(0xFFFFFF00u);  // millis taşması (49,7 gün) basışların ortasında
  // elle eklenen olaylar (ana döngünün halkası)
  OlayHalka h;
  memset(&h, 0, sizeof h);
  halka_ekle(&h, OLAY_NFC, 7);
  Olay o;
  if (!halka_bak(&h, &o) || o.tur != OLAY_NFC || o.deger != 7 || !halka_al(&h, &o) || halka_bak(&h, NULL)) {
    printf("HATA: NFC olayı\n");
    hata++;
  }
  printf(hata ? "dugme_test: %d HATA\n" : "dugme_test: hepsi geçti\n", hata);
  return hata != 0;
}
