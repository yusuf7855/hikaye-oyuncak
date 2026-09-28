// ses.h'nin çıkarımı PyTorch'la (kartın ağırlıklarıyla) aynı mı? ses/disa_aktar.py'nin altın örnekleriyle karşılaştırır.
// Derle:    cc -O2 -I.. -o /tmp/ses_test ses_test.c -lm
// Çalıştır: /tmp/ses_test ses.bin ses_altin.bin [MMAC/s ...]
// Sürücü (model oluşturur, dışa aktarır, derler, çalıştırır): python firmware/hikaye_oyuncak/tools/ses_test.py
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "../ses.h"

static double simdi(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }

static uint8_t *dosya_oku(const char *yol, size_t *n) {
  FILE *f = fopen(yol, "rb");
  if (!f) { perror(yol); exit(2); }
  fseek(f, 0, SEEK_END); *n = (size_t)ftell(f); fseek(f, 0, SEEK_SET);
  uint8_t *b = (uint8_t *)malloc(*n + 1);
  if (fread(b, 1, *n, f) != *n) { perror(yol); exit(2); }
  fclose(f);
  b[*n] = 0;
  return b;
}

static const uint8_t *rp;
static uint32_t u32(void) { uint32_t v; memcpy(&v, rp, 4); rp += 4; return v; }

// kancalar
typedef struct {
  int *sure; int n_sure;
  float *mel; int n_mel;       // kare
  float *dalga; long n_dalga;
  long n_pcm;
  int16_t *pcm;
} Topla;
static void k_sure(void *k, const int *s, int n) { Topla *t = (Topla *)k; memcpy(t->sure, s, n * sizeof(int)); t->n_sure = n; }
static void k_mel(void *k, const float *m, int n) { Topla *t = (Topla *)k; memcpy(t->mel + (size_t)t->n_mel * 80, m, (size_t)n * 80 * 4); t->n_mel += n; }
static void k_dalga(void *k, const float *x, int n) { Topla *t = (Topla *)k; memcpy(t->dalga + t->n_dalga, x, n * 4); t->n_dalga += n; }
static void k_pcm(void *k, const int16_t *p, int n) { Topla *t = (Topla *)k; if (t->pcm) memcpy(t->pcm + t->n_pcm, p, n * 2); t->n_pcm += n; }

// iki "çekirdek"i sırayla çalıştıran sahte paralel (bölme ve işçi tamponlarını sınar)
static void sahte_paralel(SesIs is, void *arg, int n) { is(arg, n / 2, n, 0); is(arg, 0, n / 2, 1); }

static void fark(const float *a, const float *b, long n, double *en, double *ref) {
  *en = 0; *ref = 0;
  for (long i = 0; i < n; i++) {
    double d = fabs((double)a[i] - b[i]);
    if (d > *en) *en = d;
    if (fabs(b[i]) > *ref) *ref = fabs(b[i]);
  }
}

int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "kullanım: %s ses.bin ses_altin.bin [MMAC/s ...]\n", argv[0]); return 2; }
  size_t nb, na;
  uint8_t *img = dosya_oku(argv[1], &nb), *alt = dosya_oku(argv[2], &na);
  Ses s;
  if (ses_yukle(&s, img, nb, NULL)) { fprintf(stderr, "ses_yukle: %s\n", ses_hata); return 2; }
  printf("ses.bin %zu B | akustik d=%d kod=%d coz=%d tah=%d | vocoder d=%d blok=%d | SES_PARCA=%d SES_ALT=%d "
         "SES_MAX_SEMBOL=%d | bellek: büyük %.0f KB + sıcak %.0f KB\n", nb, s.ad, s.n_kod, s.n_coz, s.d_tah, s.vd,
         s.n_vblok, SES_PARCA, SES_ALT, SES_MAX_SEMBOL, s.bellek_buyuk / 1024.0, s.bellek_sicak / 1024.0);
  rp = alt;
  if (memcmp(rp, "SESA", 4)) { fprintf(stderr, "altın dosyası değil\n"); return 2; }
  rp += 4;
  int n_ornek = (int)u32(), hata = 0, n_metin = 0, metin_hata = 0;
  double top_sn = 0, top_ses = 0, top_mac = 0, en_mel_rel = 0, en_dalga_rel = 0;
  for (int e = 0; e < n_ornek; e++) {
    uint32_t mb = u32();
    const char *metin = (const char *)rp; rp += mb;
    uint32_t n = u32();
    const int32_t *ids = (const int32_t *)rp; rp += 4 * n;
    int benim[4096];
    int m = metin_kodla_n(metin, mb, benim, 4096);
    n_metin++;
    int ayni = m == (int)n;
    for (uint32_t i = 0; ayni && i < n; i++) ayni = benim[i] == ids[i];
    if (!ayni) {
      metin_hata++;
      printf("METİN FARKLI: \"%.*s\" C %d sembol, Python %u\n", (int)mb, metin, m, n);
    }
    if (!u32()) continue;
    uint32_t T = u32();
    const int32_t *sure = (const int32_t *)rp; rp += 4 * n;
    const float *mel = (const float *)rp; rp += 4 * (size_t)T * 80;
    uint32_t ns = u32();
    const float *dalga = (const float *)rp; rp += 4 * (size_t)ns;

    Topla t;
    memset(&t, 0, sizeof t);
    t.sure = (int *)malloc(n * sizeof(int));
    t.mel = (float *)malloc((size_t)(T + 64) * 80 * 4);
    t.dalga = (float *)malloc((ns + 4096) * 4);
    t.pcm = (int16_t *)malloc((ns + 4096) * 2);
    s.kanca_sure = k_sure; s.kanca_mel = k_mel; s.kanca_dalga = k_dalga; s.kanca_kul = &t;
    s.paralel = NULL;
    double t0 = simdi();
    long r = ses_sentez(&s, benim, m, k_pcm, &t);
    double sn = simdi() - t0;
    if (r < 0) { printf("ses_sentez hata: %s\n", ses_hata); return 1; }
    int sure_ayni = t.n_sure == (int)n, sure_fark = 0;
    for (uint32_t i = 0; i < n && i < (uint32_t)t.n_sure; i++) if (t.sure[i] != sure[i]) { sure_ayni = 0; sure_fark++; }
    double mel_en, mel_ref, d_en, d_ref;
    int boy_ok = t.n_mel == (int)T && t.n_dalga == (long)ns && t.n_pcm == (long)ns;
    fark(t.mel, mel, boy_ok ? (long)T * 80 : 0, &mel_en, &mel_ref);
    fark(t.dalga, dalga, boy_ok ? (long)ns : 0, &d_en, &d_ref);
    double mel_rel = mel_en / (mel_ref > 0 ? mel_ref : 1), d_rel = d_en / (d_ref > 0 ? d_ref : 1);
    if (mel_rel > en_mel_rel) en_mel_rel = mel_rel;
    if (d_rel > en_dalga_rel) en_dalga_rel = d_rel;
    // int16 yolu: ses_ornek_ver'deki dönüşümle aynı mı
    int pcm_fark = 0;
    for (uint32_t i = 0; boy_ok && i < ns; i++) {
      float v = t.dalga[i] > 1.f ? 1.f : t.dalga[i] < -1.f ? -1.f : t.dalga[i];
      if (t.pcm[i] != (int16_t)lrintf(v * 32767.f)) pcm_fark++;
    }
    // iki işçili bölme bit bit aynı mı
    Topla t2;
    memset(&t2, 0, sizeof t2);
    t2.sure = (int *)malloc(n * sizeof(int));
    t2.mel = (float *)malloc((size_t)(T + 64) * 80 * 4);
    t2.dalga = (float *)malloc((ns + 4096) * 4);
    s.kanca_kul = &t2;
    s.paralel = sahte_paralel;
    ses_sentez(&s, benim, m, k_pcm, &t2);
    s.paralel = NULL;
    int par_ayni = t2.n_dalga == t.n_dalga && !memcmp(t2.dalga, t.dalga, t.n_dalga * 4) &&
                   !memcmp(t2.mel, t.mel, (size_t)t.n_mel * 80 * 4);
    double ses_sn = ns / (double)s.sr;
    top_sn += sn; top_ses += ses_sn; top_mac += s.mac;
    printf("[%d] %u sembol, %u kare, %.2f s ses | süreler %s | mel en büyük fark %.2e (|ref| %.2f, göreli %.1e) | "
           "dalga %.2e (|ref| %.3f, göreli %.1e) | pcm %s | 2 işçi %s | %.3f s, %.1f M çarpma\n",
           e, n, T, ses_sn, sure_ayni ? "AYNI" : "FARKLI", mel_en, mel_ref, mel_rel, d_en, d_ref, d_rel,
           pcm_fark ? "FARKLI" : "aynı", par_ayni ? "bit bit aynı" : "FARKLI", sn, s.mac / 1e6);
    if (!boy_ok) printf("    uzunluk farklı: mel %d/%u, dalga %ld/%u, pcm %ld\n", t.n_mel, T, t.n_dalga, ns, t.n_pcm);
    if (!sure_ayni) printf("    %d süre farklı\n", sure_fark);
    if (!sure_ayni || !boy_ok || mel_rel > 1e-3 || d_rel > 1e-3 || pcm_fark > 2 || !par_ayni) hata++;
    free(t.sure); free(t.mel); free(t.dalga); free(t.pcm); free(t2.sure); free(t2.mel); free(t2.dalga);
  }
  // cümle bölme (ses_metin) ve uzun cümle (SES_MAX_SEMBOL üstü: boşluktan bölünür)
  {
    Topla t;
    memset(&t, 0, sizeof t);
    s.kanca_sure = NULL; s.kanca_mel = NULL; s.kanca_dalga = NULL;
    const char *c1 = "Ali koştu.", *c2 = " \"Dur!\" dedi… ", *c3 = "\nSonra   güldüler";
    long a1 = ses_cumle(&s, c1, k_pcm, &t), a2 = ses_cumle(&s, c2, k_pcm, &t), a3 = ses_cumle(&s, c3, k_pcm, &t);
    char birlesik[256];
    snprintf(birlesik, sizeof birlesik, "%s%s%s", c1, c2, c3);
    t.n_pcm = 0;
    long b = ses_metin(&s, birlesik, k_pcm, &t, 250, NULL);
    long bek = a1 + a2 + a3 + 2 * (s.sr / 4);
    printf("ses_metin: 3 cümle %ld örnek (beklenen %ld, geri çağrı toplamı %ld) %s\n", b + 2 * (s.sr / 4), bek, t.n_pcm,
           t.n_pcm == bek ? "aynı" : "FARKLI");
    if (t.n_pcm != bek) hata++;
    char uzun[2048] = "";
    for (int i = 0; i < 30; i++) strcat(uzun, "küçük tavşan koştu ve ");
    strcat(uzun, "durdu.");
    int ids[4096];
    int nu = metin_kodla(uzun, ids, 4096);
    t.n_pcm = 0;
    double t0 = simdi();
    long r = ses_cumle(&s, uzun, k_pcm, &t);
    printf("uzun cümle: %d sembol (> %d, bölünerek) -> %ld örnek, %.2f s\n", nu, SES_MAX_SEMBOL, r, simdi() - t0);
    if (r <= 0 || t.n_pcm != r) hata++;
  }
  printf("metin: %d/%d aynı | en büyük göreli fark: mel %.1e, dalga %.1e\n", n_metin - metin_hata, n_metin,
         en_mel_rel, en_dalga_rel);
  if (top_ses > 0) {
    double mac_sn = top_mac / top_ses;
    printf("bilgisayar (tek çekirdek, -O2): %.3f s hesap / s ses | %.1f M çarpma / s ses\n", top_sn / top_ses, mac_sn / 1e6);
    int n_hiz = argc > 3 ? argc - 3 : 3;
    double varsay[3] = {200, 300, 400};
    for (int i = 0; i < n_hiz; i++) {
      double h = argc > 3 ? atof(argv[3 + i]) : varsay[i];
      printf("ESP32-S3 tahmini @ %.0f MMAC/s: %.2f s hesap / s ses\n", h, mac_sn / (h * 1e6));
    }
  }
  if (hata || metin_hata) { printf("BAŞARISIZ: %d ses, %d metin\n", hata, metin_hata); return 1; }
  printf("TAMAM\n");
  return 0;
}
