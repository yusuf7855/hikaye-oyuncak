// kuyruk.h'nin bilgisayarda denemesi: bellekte NOR flash taklidi (yazma yalnız 1 -> 0, silme 4 KB, yazma sınırıyla
// güç kesilmesi). Denenen: çöp dolu bölüm, doldurma politikası (figür başına hedef, yerlerin dönmesi), yeniden
// başlatmada aynen okuma, en eskisinin önce çalınması, tüketme, CRC bozulması, imza değişimi, kap sınırı, her
// noktada güç kesilmesi (yarım yazılan hikâye hiç görünmez, eskiler bozulmaz), aşınma dengesi.
// Derle:  cc -O2 -Wall -o /tmp/kuyruk_test firmware/hikaye_oyuncak/tools/kuyruk_test.c
// Çalıştır: /tmp/kuyruk_test   (çıkış kodu 0: hepsi geçti)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../kuyruk.h"

#define YUVA 48
#define BOYUT (YUVA * KUYRUK_SEKTOR)
static uint8_t flash[BOYUT];
static long yazma_butce = -1;           // >= 0: bu kadar bayt daha yazılır, sonra "güç kesilir"
static int sil_sayisi[YUVA];

static int f_oku(void *kul, uint32_t ofs, void *b, uint32_t n) {
  (void)kul;
  if (ofs + n > BOYUT) return 1;
  memcpy(b, flash + ofs, n);
  return 0;
}
static int f_yaz(void *kul, uint32_t ofs, const void *b, uint32_t n) {
  (void)kul;
  if (ofs + n > BOYUT) return 1;
  for (uint32_t i = 0; i < n; i++) {
    if (yazma_butce == 0) return 0;  // güç kesildi: yazma tutmaz (sürücü hata da bildiremez)
    if (yazma_butce > 0) yazma_butce--;
    flash[ofs + i] &= ((const uint8_t *)b)[i];
  }
  return 0;
}
static int f_sil(void *kul, uint32_t ofs, uint32_t n) {
  (void)kul;
  if (ofs % KUYRUK_SEKTOR || n % KUYRUK_SEKTOR || ofs + n > BOYUT) return 1;
  if (yazma_butce == 0) return 0;
  memset(flash + ofs, 0xFF, n);
  sil_sayisi[ofs / KUYRUK_SEKTOR]++;
  return 0;
}
static const KuyrukFlash FL = {NULL, f_oku, f_yaz, f_sil, BOYUT};

// istemler.h'deki 11 figürün yer sayıları
static const int8_t YER_N[11] = {4, 3, 4, 4, 3, 4, 4, 4, 5, 3, 3};

static int hata = 0;
#define DENE(k, ...)                                                    \
  do {                                                                  \
    if (!(k)) { printf("HATA (satır %d): ", __LINE__); printf(__VA_ARGS__); printf("\n"); hata++; } \
  } while (0)

// Hikâye içeriği sıradan türetilir: okunanın doğruluğu sıradan denetlenir
static int hikaye_kur(uint32_t sira, int16_t *t) {
  int n = 40 + (int)(sira * 7919u % 190);
  for (int i = 0; i < n; i++) t[i] = (int16_t)((sira * 31u + (uint32_t)i * 17u) % 16384u);
  return n;
}
static int hikaye_dogru(const KuyrukBaslik *b, const int16_t *t) {
  int16_t bek[KUYRUK_TOK_MAKS];
  int n = hikaye_kur(b->sira, bek);
  return b->n == n && b->n_plan == n / 5 && !memcmp(t, bek, (size_t)n * 2) && b->puan == -(float)b->sira / 8;
}
static int uret_yaz(Kuyruk *q, int f, int j) {
  int16_t t[KUYRUK_TOK_MAKS];
  int n = hikaye_kur(q->son_sira + 1, t);
  return kuyruk_yaz(q, f, j, 16, -(float)(q->son_sira + 1) / 8, t, n, n / 5);
}
// Bütün hazır yuvaları okuyup içeriği denetler; döner: hazır sayısı
static int hepsini_denetle(Kuyruk *q) {
  int n = 0;
  for (int i = 0; i < q->n_yuva; i++) {
    if (q->y[i].durum != KY_HAZIR) continue;
    KuyrukBaslik b;
    int16_t t[KUYRUK_TOK_MAKS];
    int k = kuyruk_oku(q, i, &b, t, KUYRUK_TOK_MAKS);
    DENE(k > 0 && hikaye_dogru(&b, t), "yuva %d içeriği yanlış (sıra %u)", i, (unsigned)b.sira);
    n++;
  }
  return n;
}
// Politika döngüsü: kuyruk dolana kadar sonraki işi üretir; döner: yazılan
static int doldur(Kuyruk *q, int basi) {
  int f, j, n = 0;
  while (kuyruk_sonraki(q, basi, 11, YER_N, &f, &j)) {
    DENE(uret_yaz(q, f, j) >= 0, "yazılamadı");
    if (++n > 1000) { DENE(0, "doldurma bitmiyor"); break; }
  }
  return n;
}

int main(void) {
  Kuyruk q;
  // 1. eski bölümden kalma çöp (ör. eski model baytları): hazır yok, ilk yazmalar çalışır
  srand(1);
  for (int i = 0; i < BOYUT; i++) flash[i] = (uint8_t)rand();
  DENE(kuyruk_kur(&q, &FL, 0x1234) == 0, "çöpte hazır hikâye görüldü");
  DENE(q.n_yuva == YUVA, "yuva sayısı %d", q.n_yuva);

  // 2. doldurma politikası: figür başına 3 -> 33 hikâye, her figürde 3 ayrı yer (Niloya: 4 yerin 3'ü)
  DENE(doldur(&q, 3) == 33, "33 hikâye bekleniyordu");
  for (int f = 0; f < 11; f++) {
    DENE(kuyruk_say(&q, f, -1) == 3, "figür %d: %d", f, kuyruk_say(&q, f, -1));
    for (int j = 0; j < YER_N[f]; j++) DENE(kuyruk_say(&q, f, j) <= 1, "figür %d yer %d: aynı yer iki kez", f, j);
  }

  // 3. yeniden başlatma: aynı 33 hikâye, içerik aynen
  DENE(kuyruk_kur(&q, &FL, 0x1234) == 33, "yeniden başlatmada hazır %d", kuyruk_say(&q, -1, -1));
  DENE(hepsini_denetle(&q) == 33, "denetim");

  // 4. en eskisi önce çalınır; tüketilen yeniden başlatmada da tüketilmiş; boşalan figür önce dolar
  int y = kuyruk_bul(&q, 7, -1);
  uint32_t en_eski = 0xFFFFFFFFu;
  for (int i = 0; i < q.n_yuva; i++)
    if (q.y[i].durum == KY_HAZIR && q.y[i].figur == 7 && q.y[i].sira < en_eski) en_eski = q.y[i].sira;
  DENE(y >= 0 && q.y[y].sira == en_eski, "en eski bulunmadı");
  int yer_tuketilen = q.y[y].yer;
  DENE(kuyruk_tuket(&q, y) == 0, "tüketilemedi");
  DENE(kuyruk_tuket(&q, y) != 0, "iki kez tüketildi");
  DENE(kuyruk_kur(&q, &FL, 0x1234) == 32, "tüketme kalıcı değil");
  int f, j;
  DENE(kuyruk_sonraki(&q, 3, 11, YER_N, &f, &j) && f == 7, "boşalan figür (Elsa) önce dolmalı: %d", f);
  DENE(j == yer_tuketilen || kuyruk_say(&q, 7, j) == 0, "boşalan yer seçilmeli");
  DENE(kuyruk_bul(&q, 7, yer_tuketilen) < 0 || kuyruk_say(&q, 7, yer_tuketilen) > 0, "bul/say tutarsız");
  DENE(uret_yaz(&q, f, j) >= 0, "yeniden dolmadı");
  DENE(kuyruk_kur(&q, &FL, 0x1234) == 33, "33'e dönmedi");

  // 5. CRC: token alanında bir bit bozulursa o yuva yok sayılır, okuma 0 döner
  y = kuyruk_bul(&q, 2, -1);
  flash[(size_t)y * KUYRUK_SEKTOR + KUYRUK_BASLIK + 10] ^= 0x04;
  {
    KuyrukBaslik b;
    int16_t t[KUYRUK_TOK_MAKS];
    DENE(kuyruk_oku(&q, y, &b, t, KUYRUK_TOK_MAKS) == 0, "bozuk yuva okundu");
    DENE(q.y[y].durum == KY_BOS, "bozuk yuva boş sayılmadı");
    DENE(kuyruk_kur(&q, &FL, 0x1234) == 32, "bozuk yuva açılışta sayıldı");
    // 6. kap sınırı: hikâye kap'a sığmıyorsa okunmaz
    int z = kuyruk_bul(&q, 3, -1);
    DENE(kuyruk_oku(&q, z, &b, t, 10) == 0, "kap aşıldı");
  }
  DENE(doldur(&q, 3) == 2, "bozuk ve kap denemesindeki yuvalar yeniden dolmalı");

  // 7. imza değişti (yeni model): eskiler geçersiz, yuvalar yeniden kullanılır
  DENE(kuyruk_kur(&q, &FL, 0x9999) == 0, "eski imzalı hikâye görüldü");
  DENE(doldur(&q, 3) == 33, "yeni imzayla doldurma");
  DENE(kuyruk_kur(&q, &FL, 0x9999) == 33 && hepsini_denetle(&q) == 33, "yeni imzayla yeniden başlatma");

  // 8. güç kesilmesi: yazmanın her noktasında (silme dahil) kes, yeniden başlat; yarım hikâye görünmemeli,
  //    eskiler aynen kalmalı; tüketme yazısı yarıda kesilse de yuva ya hazır ya tüketilmiş olmalı
  int deneme = 0, yeni_gorunen = 0;
  for (int tur = 0; tur < 400; tur++) {
    kuyruk_kur(&q, &FL, 0x9999);
    int onceki = kuyruk_say(&q, -1, -1);
    // bir hikâye tüket (yer açılsın), gerekirse yarıda kes
    int tf = tur % 11, ty = kuyruk_bul(&q, tf, -1);
    if (ty >= 0) {
      yazma_butce = (tur % 3 == 0) ? (tur / 3) % 5 : -1;
      kuyruk_tuket(&q, ty);
      yazma_butce = -1;
      kuyruk_kur(&q, &FL, 0x9999);
      int simdi = kuyruk_say(&q, -1, -1);
      DENE(simdi == onceki || simdi == onceki - 1, "tüketme kesilince sayı %d -> %d", onceki, simdi);
      onceki = simdi;
    }
    if (!kuyruk_sonraki(&q, 3, 11, YER_N, &f, &j)) continue;
    int16_t t[KUYRUK_TOK_MAKS];
    int n = hikaye_kur(q.son_sira + 1, t);
    long tam = (long)n * 2 + 24 + 4;
    yazma_butce = rand() % 4 == 0 ? -1 : rand() % (tam + 1);  // dörtte biri kesilmeden biter
    int r = kuyruk_yaz(&q, f, j, 16, -(float)(q.son_sira + 1) / 8, t, n, n / 5);
    yazma_butce = -1;
    (void)r;
    kuyruk_kur(&q, &FL, 0x9999);
    int sonra = hepsini_denetle(&q);
    DENE(sonra == onceki || sonra == onceki + 1, "kesilmeden sonra hazır %d (önce %d)", sonra, onceki);
    yeni_gorunen += sonra == onceki + 1;
    deneme++;
  }
  DENE(yeni_gorunen > 0 && yeni_gorunen < deneme, "kesme denemesi anlamsız (%d/%d)", yeni_gorunen, deneme);
  printf("güç kesilmesi: %d deneme, %d tamamlanan, hepsi tutarlı\n", deneme, yeni_gorunen);

  // 9. aşınma: 3000 kez çal + yeniden üret; sektörler dengeli silinir
  memset(flash, 0xFF, sizeof flash);
  memset(sil_sayisi, 0, sizeof sil_sayisi);
  kuyruk_kur(&q, &FL, 0x77);
  doldur(&q, 3);
  for (int tur = 0; tur < 3000; tur++) {
    int tf = (tur * 7) % 11, ty = kuyruk_bul(&q, tf, -1);
    if (ty >= 0) kuyruk_tuket(&q, ty);
    doldur(&q, 3);
  }
  int en_az = 1 << 30, en_cok = 0, toplam = 0;
  for (int i = 0; i < YUVA; i++) {
    en_az = sil_sayisi[i] < en_az ? sil_sayisi[i] : en_az;
    en_cok = sil_sayisi[i] > en_cok ? sil_sayisi[i] : en_cok;
    toplam += sil_sayisi[i];
  }
  DENE(en_cok - en_az <= 2, "aşınma dengesiz: en az %d, en çok %d", en_az, en_cok);
  DENE(kuyruk_kur(&q, &FL, 0x77) == 33 && hepsini_denetle(&q) == 33, "aşınma sonrası");
  printf("aşınma: %d silme, sektör başına %d-%d\n", toplam, en_az, en_cok);

  // 10. kuyruk tamamen dolu (figür başına hedef yuvalardan fazla): yer kalmayınca yazma -1, sonraki 0
  memset(flash, 0xFF, sizeof flash);
  kuyruk_kur(&q, &FL, 0x55);
  DENE(doldur(&q, 10) == YUVA, "48 yuva dolmalı");
  DENE(uret_yaz(&q, 0, 0) == -1, "dolu kuyruğa yazıldı");
  DENE(kuyruk_temizle(&q) == YUVA && kuyruk_kur(&q, &FL, 0x55) == 0, "temizle");

  printf(hata ? "kuyruk_test: %d HATA\n" : "kuyruk_test: hepsi geçti\n", hata);
  return hata != 0;
}
