// Ses: kartta Türkçe metinden 16 kHz sese (ses/model.py'deki Akustik + Vocoder'ın C çıkarımı).
//
// Ağırlıklar flash'taki "ses" bölümünde (ses/disa_aktar.py'nin yazdığı ses.bin), yerinde okunur; RAM'e kopyalanmaz.
//   Akustik: 4 bit, 32'lik gruplar, fp16 ölçek | Vocoder: 8 bit, satır başına float ölçek | küçükler fp16.
// Hesap PyTorch'la aynı (Akustik.uret, hiz=1; Vocoder.forward): ağırlık satırı kuant.q_agirlik'teki gibi
// q * ölçek olarak float'a açılır, etkinlikler float. Fark yalnız toplama sırasından (tools/ses_test.c ölçer).
//
// Akış: metin -> semboller -> kodlayıcı + tahminci (cümlenin tamamı, <= SES_MAX_SEMBOL) -> süreler ->
// çözücü -> mel -> vocoder -> iSTFT -> PCM. Çözücü ve vocoder kare kare akar: her ConvNeXt katmanı yalnız
// kendi alıcı alanı kadar (k/2 kare) geçmiş tutar, SES_PARCA karelik parçalarla ilerler. Böylece tekrar hesap
// yok, bellek cümle uzunluğundan bağımsız, ses ilk parçadan sonra (~0,6 s ses) çıkmaya başlar.
// Noktasal katmanlar (pw1/pw2/çıkış) SES_ALT kare birlikte hesaplanır: her ağırlık satırı flash'tan bir kez
// okunup SES_ALT karede kullanılır.
//
// Kullanım:
//   Ses s; if (ses_yukle(&s, img, boyut, ayirici)) { hata: ses_hata }
//   s.paralel = ...;                       // istenirse iki çekirdek (NULL: tek)
//   ses_cumle(&s, "Bir varmış bir yokmuş.", cb, kul);   // cb(kul, int16 *pcm, n) parça parça çağrılır
//   ses_metin(&s, hikaye, cb, kul, 250);   // cümlelere böler, aralara 250 ms sessizlik
//
// Başlık dosyası hem C (tools/ses_test.c) hem C++ (.ino) olarak derlenir.
#pragma once
#include <math.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef ESP_PLATFORM
#include "esp_heap_caps.h"
#endif

#ifndef SES_PARCA
#define SES_PARCA 16        // akışta bir adımda çözücüye giren kare (0,26 s ses)
#endif
#ifndef SES_ALT
#define SES_ALT 16          // noktasal katmanlarda birlikte işlenen kare
#endif
#ifndef SES_MAX_SEMBOL
#define SES_MAX_SEMBOL 128  // tek seferde sentezlenen en uzun sembol dizisi (uzunlar boşluk/virgülden bölünür)
#endif
#ifndef SES_MAX_KOD
#define SES_MAX_KOD 1024    // ses_cumle'nin tek cümlede okuduğu en çok sembol
#endif
#define SES_MAX_BLOK 12
#define SES_PCM_N 1024
#define SES_PI 3.14159265358979323846
#if defined(__GNUC__)
#define SES_API static __attribute__((unused))
#else
#define SES_API static
#endif

enum { SES_F32 = 0, SES_F16 = 1, SES_Q4 = 2, SES_Q8 = 3 };

// sicak = 1: sık okunan küçük tampon (kartta dahili SRAM tercih edilir), 0: büyük tampon (PSRAM olabilir)
typedef void *(*SesAyir)(size_t n, int sicak);
// İş bölme: is(arg, bas, son, isci) [0, n) aralığını parçalara bölerek çağrılır; isci 0 ya da 1 (her işçinin kendi
// tamponu var). paralel NULL ise tek parça (isci 0).
typedef void (*SesIs)(void *arg, int bas, int son, int isci);
typedef void (*SesParalel)(SesIs is, void *arg, int n);
typedef void (*SesPcm)(void *kul, const int16_t *pcm, int n);

typedef struct {
  uint8_t tip;
  int satir, sutun, grup, n_grup, satir_bayt;
  const uint8_t *kod;   // q4: satir x satir_bayt (çift sütun alt nibble, q+8) | q8: int8 | f16/f32: değerler
  const void *olcek;    // q4: fp16 [satir x n_grup] | q8: float [satir]
} SesT;

typedef struct {
  int d, k, h;
  SesT dw_w, dw_b, ln_g, ln_b, pw1_w, pw1_b, pw2_w, pw2_b, gamma;
} SesBlok;

// Akış katmanı: girişin [bas, son) kareleri buf'ta; cikan'dan önceki çıkışlar verildi.
typedef struct {
  int tip;              // 0: ConvNeXt bloğu, 1: vocoder girişi (Conv1d n_mel->d, k) + ln0
  const SesBlok *b;
  int d_in, d_out, r, kap;
  float *buf;
  int bas, son, cikan;
} SesAkis;

typedef struct Ses {
  int n_sembol, n_mel, n_fft, hop, sr, grup;
  int ad, n_kod, k_kod, n_coz, k_coz, genis, d_tah, n_tah, k_tah;
  int vd, n_vblok, vgenis, vk, vk_giris;
  SesT gomme, tah_giris_w, tah_giris_b, tah_ln_g, tah_ln_b, tah_cikis_w, tah_cikis_b;
  SesT perde_w, perde_b, enerji_w, enerji_b, coz_ln_g, coz_ln_b, cikis_w, cikis_b;
  SesT v_giris_w, v_giris_b, v_ln0_g, v_ln0_b, v_ln1_g, v_ln1_b, v_cikis_w, v_cikis_b;
  SesBlok kod[SES_MAX_BLOK], tah[SES_MAX_BLOK], coz[SES_MAX_BLOK], vblok[SES_MAX_BLOK];
  float istat[4];
  // ayarlar (yüklemeden sonra değiştirilebilir)
  float hiz;            // > 1 yavaş (Akustik.uret hiz)
  float perde_kaydir;   // yarım ton
  SesParalel paralel;
  // çalışma alanı
  float *ex, *alan, *tahmin, *pA, *pB, *z, *hid, *u, *col, *dwt, *satir[2];
  int *sure, *kod_buf;
  SesAkis akis[2 * SES_MAX_BLOK + 1];
  int n_akis, kmax;
  float *fre, *fim, *pen, *pen2, *ola, *tc, *ts;
  int16_t *ters, *pcm;
  // iSTFT durumu
  int T, ola_bas, n_pcm;
  long n_ornek;
  SesPcm cb;
  void *cb_kul;
  // deneme kancaları (NULL olabilir)
  void (*kanca_sure)(void *kul, const int *sure, int n);
  void (*kanca_mel)(void *kul, const float *mel, int n_kare);        // [n_kare x n_mel]
  void (*kanca_dalga)(void *kul, const float *x, int n);             // kırpılmamış float
  void *kanca_kul;
  size_t bellek_buyuk, bellek_sicak;   // ayrılan tamponlar (bayt)
  double mac;           // son sentezdeki çarpma sayısı (tahmini süre için)
} Ses;

static const char *ses_hata = "";

// ---------------------------------------------------------------- metin -> semboller (ses/metin.py ile aynı)
// Semboller: 0 '_', 1 ' ', 2.. ",.!?\"-:;", 10.. "abcçdefgğhıijklmnoöprsştuüvyzâîû"
static const uint16_t SES_HARF[32] = {'a', 'b', 'c', 0xE7, 'd', 'e', 'f', 'g', 0x11F, 'h', 0x131, 'i', 'j', 'k',
                                      'l', 'm', 'n', 'o', 0xF6, 'p', 'r', 's', 0x15F, 't', 'u', 0xFC, 'v', 'y',
                                      'z', 0xE2, 0xEE, 0xFB};

static int ses_sembol_id(uint32_t c) {
  static const char NOK[] = ",.!?\"-:;";
  if (c == '_') return 0;
  if (c == ' ') return 1;
  for (int i = 0; i < 8; i++) if (c == (uint32_t)(unsigned char)NOK[i]) return 2 + i;
  for (int i = 0; i < 32; i++) if (c == SES_HARF[i]) return 10 + i;
  return -1;
}

// Python kucult(): I -> ı, İ -> i, sonra str.lower(). Yalnız sembol kümesine düşen dönüşümler gerekli
// (başka her şey zaten boşluğa gider); liste bütün Unicode taranarak çıkarıldı.
static uint32_t ses_kucult(uint32_t c) {
  if (c == 'I') return 0x131;
  if (c == 0x130) return 'i';
  if (c >= 'A' && c <= 'Z') return c + 32;
  switch (c) {
    case 0xC2: return 0xE2;   case 0xC7: return 0xE7;   case 0xCE: return 0xEE;   case 0xD6: return 0xF6;
    case 0xDB: return 0xFB;   case 0xDC: return 0xFC;   case 0x11E: return 0x11F; case 0x15E: return 0x15F;
    case 0x212A: return 'k';  // Kelvin işareti
  }
  return c;
}

// UTF-8'den bir kod noktası; bozuk bayt -> 0xFFFD (bilinmeyen: boşluk olur)
static uint32_t ses_utf8(const unsigned char **p, const unsigned char *son) {
  const unsigned char *s = *p;
  uint32_t c = *s++;
  int n = 0;
  if (c < 0x80) n = 0;
  else if ((c & 0xE0) == 0xC0) { c &= 0x1F; n = 1; }
  else if ((c & 0xF0) == 0xE0) { c &= 0x0F; n = 2; }
  else if ((c & 0xF8) == 0xF0) { c &= 0x07; n = 3; }
  else { *p = s; return 0xFFFD; }
  for (int i = 0; i < n; i++) {
    if (s >= son || (*s & 0xC0) != 0x80) { *p = s; return 0xFFFD; }
    c = (c << 6) | (*s++ & 0x3F);
  }
  *p = s;
  return c;
}

// metin.py temizle() + kodla(): küçük harf, tırnak/üç nokta/uzun tire dönüşümü, kesme işareti silinir,
// bilinmeyen -> boşluk, boşluklar teke iner, baştan/sondan kırpılır. Döner: sembol sayısı (en çok kap).
SES_API int metin_kodla_n(const char *metin, size_t bayt, int *ids, int kap) {
  const unsigned char *p = (const unsigned char *)metin, *son = p + bayt;
  int n = 0, bosluk = 0;
  while (p < son && n < kap) {
    uint32_t c = ses_kucult(ses_utf8(&p, son));
    if (c == 0x201C || c == 0x201D) c = '"';
    else if (c == 0x2026) c = '.';
    else if (c == 0x2014) c = '-';
    else if (c == 0x2019 || c == '\'') continue;   // ’ -> ' -> silinir
    int id = c == ' ' ? -1 : ses_sembol_id(c);
    if (id < 0) { bosluk = 1; continue; }
    if (bosluk && n > 0) {
      ids[n++] = 1;
      if (n >= kap) break;
    }
    bosluk = 0;
    ids[n++] = id;
  }
  return n;
}
SES_API int metin_kodla(const char *metin, int *ids, int kap) { return metin_kodla_n(metin, strlen(metin), ids, kap); }

// ---------------------------------------------------------------- tensörler
static inline float ses_f16(uint16_t h) {
  uint32_t sign = (uint32_t)(h & 0x8000) << 16, e = (h >> 10) & 0x1F, m = h & 0x3FF, f;
  if (e == 0) {
    if (m == 0) f = sign;
    else {
      e = 127 - 15 + 1;
      while (!(m & 0x400)) { m <<= 1; e--; }
      m &= 0x3FF;
      f = sign | (e << 23) | (m << 13);
    }
  } else if (e == 31) f = sign | 0x7F800000u | (m << 13);
  else f = sign | ((e - 15 + 127) << 23) | (m << 13);
  float r;
  memcpy(&r, &f, 4);
  return r;
}

static inline float ses_v(const SesT *t, int i) {
  if (t->tip == SES_F16) return ses_f16(((const uint16_t *)t->kod)[i]);
  return ((const float *)t->kod)[i];
}

// Ağırlık satırı r -> w[sutun] float (kuant.q_agirlik'in değeri: q * ölçek, tek çarpma, PyTorch'la bit bit aynı).
static void ses_satir_ac(const SesT *t, int r, float *w) {
  int cols = t->sutun;
  if (t->tip == SES_Q4) {
    const uint8_t *p = t->kod + (size_t)r * t->satir_bayt;
    const uint16_t *sc = (const uint16_t *)t->olcek + (size_t)r * t->n_grup;
    int g = t->grup;
    for (int gi = 0, j = 0; gi < t->n_grup; gi++) {
      float s = ses_f16(sc[gi]);
      int e = j + g;
      if (!(j & 1) && !(g & 1)) {  // çift başlangıç, çift grup: bayt bayt
        for (; j < e; j += 2) {
          uint8_t v = p[j >> 1];
          w[j] = (float)((int)(v & 15) - 8) * s;
          w[j + 1] = (float)((int)(v >> 4) - 8) * s;
        }
      } else {
        for (; j < e; j++) {
          uint8_t v = p[j >> 1];
          w[j] = (float)((int)((j & 1) ? (v >> 4) : (v & 15)) - 8) * s;
        }
      }
    }
  } else if (t->tip == SES_Q8) {
    const int8_t *p = (const int8_t *)t->kod + (size_t)r * cols;
    float s = ((const float *)t->olcek)[r];
    for (int j = 0; j < cols; j++) w[j] = (float)p[j] * s;
  } else {
    for (int j = 0; j < cols; j++) w[j] = ses_v(t, r * cols + j);
  }
}

// Y[i*ys + r] = b[r] + sum_c W[r][c] * X[i*xs + c], i < n (gelu: sonuca GELU; iki çekirdeğe bölünsün diye burada). Satır başına bir açma, dört kare birlikte
// (her karenin toplama sırası tek kare yoluyla aynı: sonuç bit bit aynı).
typedef struct {
  const SesT *w, *b;
  const float *X;
  int n, xs, ys, gelu;
  float *Y;
  float *const *satir;
} SesMatIs;

static inline float ses_gelu(float x) { return 0.5f * x * (1.f + erff(x * 0.70710678118654752f)); }

static void ses_mat_is(void *arg, int r0, int r1, int isci) {
  const SesMatIs *a = (const SesMatIs *)arg;
  float *wr = a->satir[isci];
  const int cols = a->w->sutun, n = a->n, xs = a->xs, ys = a->ys;
  for (int r = r0; r < r1; r++) {
    ses_satir_ac(a->w, r, wr);
    float bb = a->b ? ses_v(a->b, r) : 0.f;
    int i = 0;
    for (; i + 4 <= n; i += 4) {
      const float *x0 = a->X + (size_t)i * xs, *x1 = x0 + xs, *x2 = x1 + xs, *x3 = x2 + xs;
      float s0 = 0.f, s1 = 0.f, s2 = 0.f, s3 = 0.f;
      for (int c = 0; c < cols; c++) {
        float w = wr[c];
        s0 += w * x0[c]; s1 += w * x1[c]; s2 += w * x2[c]; s3 += w * x3[c];
      }
      float *y = a->Y + (size_t)i * ys + r;
      y[0] = s0 + bb; y[ys] = s1 + bb; y[2 * ys] = s2 + bb; y[3 * ys] = s3 + bb;
      if (a->gelu) { y[0] = ses_gelu(y[0]); y[ys] = ses_gelu(y[ys]); y[2 * ys] = ses_gelu(y[2 * ys]); y[3 * ys] = ses_gelu(y[3 * ys]); }
    }
    for (; i < n; i++) {
      const float *x = a->X + (size_t)i * xs;
      float s = 0.f;
      for (int c = 0; c < cols; c++) s += wr[c] * x[c];
      a->Y[(size_t)i * ys + r] = a->gelu ? ses_gelu(s + bb) : s + bb;
    }
  }
}

static void ses_mat_g(Ses *s, const SesT *w, const SesT *b, const float *X, int n, int xs, float *Y, int ys, int gelu) {
  if (n <= 0) return;
  SesMatIs a = {w, b, X, n, xs, ys, gelu, Y, s->satir};
  s->mac += (double)n * w->satir * w->sutun;
  if (s->paralel && w->satir >= 16) s->paralel(ses_mat_is, &a, w->satir);
  else ses_mat_is(&a, 0, w->satir, 0);
}
static void ses_mat(Ses *s, const SesT *w, const SesT *b, const float *X, int n, int xs, float *Y, int ys) {
  ses_mat_g(s, w, b, X, n, xs, Y, ys, 0);
}

static void ses_ln(float *x, int d, const SesT *g, const SesT *b) {
  float m = 0.f;
  for (int i = 0; i < d; i++) m += x[i];
  m /= d;
  float v = 0.f;
  for (int i = 0; i < d; i++) { float t = x[i] - m; v += t * t; }
  v /= d;
  float r = 1.f / sqrtf(v + 1e-5f);
  for (int i = 0; i < d; i++) x[i] = (x[i] - m) * r * ses_v(g, i) + ses_v(b, i);
}

// ConvNeXt: x satır i = kare x_bas+i (gerekli kareler mevcut; [0, T) dışı sıfır). Çıkış kareleri [t0, t1)
// -> out satır t-t0. out = x + gamma * pw2(gelu(pw1(LN(dw(x))))).
static void ses_blok(Ses *s, const SesBlok *b, const float *x, int x_bas, int T, int t0, int t1, float *out) {
  const int d = b->d, k = b->k, r = k / 2, h = b->h;
  float *wk = s->satir[0];
  for (int c = 0; c < d; c++) {        // derinlemesine ağırlıklar [j][c] düzeninde
    ses_satir_ac(&b->dw_w, c, wk);
    for (int j = 0; j < k; j++) s->dwt[j * d + c] = wk[j];
  }
  for (int a = t0; a < t1; a += SES_ALT) {
    int n = t1 - a < SES_ALT ? t1 - a : SES_ALT;
    for (int i = 0; i < n; i++) {
      float *z = s->z + (size_t)i * d;
      for (int c = 0; c < d; c++) z[c] = 0.f;
      for (int j = 0; j < k; j++) {
        int t = a + i - r + j;
        if (t < 0 || t >= T) continue;
        const float *xr = x + (size_t)(t - x_bas) * d, *w = s->dwt + j * d;
        for (int c = 0; c < d; c++) z[c] += w[c] * xr[c];
      }
      for (int c = 0; c < d; c++) z[c] += ses_v(&b->dw_b, c);
      ses_ln(z, d, &b->ln_g, &b->ln_b);
    }
    s->mac += (double)n * d * k;
    ses_mat_g(s, &b->pw1_w, &b->pw1_b, s->z, n, d, s->hid, h, 1);
    ses_mat(s, &b->pw2_w, &b->pw2_b, s->hid, n, h, s->u, d);
    for (int i = 0; i < n; i++) {
      const float *xr = x + (size_t)(a + i - x_bas) * d, *u = s->u + (size_t)i * d;
      float *o = out + (size_t)(a + i - t0) * d;
      for (int c = 0; c < d; c++) o[c] = xr[c] + ses_v(&b->gamma, c) * u[c];
    }
  }
}

// Vocoder girişi: Conv1d(n_mel -> vd, k, dolgu k/2) + ln0. Ağırlık satırı [giriş][k] düzeninde.
static void ses_vgiris(Ses *s, const float *x, int x_bas, int T, int t0, int t1, float *out) {
  const int ci = s->n_mel, k = s->vk_giris, r = k / 2, d = s->vd;
  for (int a = t0; a < t1; a += SES_ALT) {
    int n = t1 - a < SES_ALT ? t1 - a : SES_ALT;
    for (int i = 0; i < n; i++) {
      float *col = s->col + (size_t)i * ci * k;
      for (int j = 0; j < k; j++) {
        int t = a + i - r + j;
        const float *xr = (t < 0 || t >= T) ? NULL : x + (size_t)(t - x_bas) * ci;
        for (int c = 0; c < ci; c++) col[c * k + j] = xr ? xr[c] : 0.f;
      }
    }
    float *o = out + (size_t)(a - t0) * d;
    ses_mat(s, &s->v_giris_w, &s->v_giris_b, s->col, n, ci * k, o, d);
    for (int i = 0; i < n; i++) ses_ln(o + (size_t)i * d, d, &s->v_ln0_g, &s->v_ln0_b);
  }
}

// Akış katmanına n yeni kare verir; hesaplanabilen çıkış karelerini out'a yazar, sayısını döner (-1: hata).
// Tampon 2r + SES_PARCA kare tutar; daha fazlası gelirse (akışın sonunda) parça parça işlenir.
static int ses_akis_it(Ses *s, SesAkis *a, const float *in, int n, int T, float *out) {
  int top = 0;
  do {
    int k = a->kap - (a->son - a->bas);
    if (k > n) k = n;
    if (k <= 0 && n > 0) { ses_hata = "akış tamponu taştı"; return -1; }
    memcpy(a->buf + (size_t)(a->son - a->bas) * a->d_in, in, (size_t)k * a->d_in * sizeof(float));
    a->son += k; in += (size_t)k * a->d_in; n -= k;
    int hedef = a->son >= T ? T : a->son - a->r;
    if (hedef > a->cikan) {
      float *o = out + (size_t)top * a->d_out;
      if (a->tip == 0) ses_blok(s, a->b, a->buf, a->bas, T, a->cikan, hedef, o);
      else ses_vgiris(s, a->buf, a->bas, T, a->cikan, hedef, o);
      top += hedef - a->cikan;
      a->cikan = hedef;
    }
    int yeni = a->cikan - a->r;
    if (yeni > a->bas) {
      memmove(a->buf, a->buf + (size_t)(yeni - a->bas) * a->d_in, (size_t)(a->son - yeni) * a->d_in * sizeof(float));
      a->bas = yeni;
    }
  } while (n > 0);
  return top;
}

// ---------------------------------------------------------------- iSTFT (ortak.Istft: hann, center, w² bölme)
static void ses_ifft(const Ses *s, float *re, float *im) {  // karmaşık, e^{+i}, ölçeksiz
  const int N = s->n_fft;
  for (int i = 0; i < N; i++) {
    int j = s->ters[i];
    if (i < j) {
      float t = re[i]; re[i] = re[j]; re[j] = t;
      t = im[i]; im[i] = im[j]; im[j] = t;
    }
  }
  for (int len = 2; len <= N; len <<= 1) {
    int yarim = len >> 1, adim = N / len;
    for (int i = 0; i < N; i += len)
      for (int j = 0; j < yarim; j++) {
        float wr = s->tc[j * adim], wi = s->ts[j * adim];
        int p = i + j, q = p + yarim;
        float vr = re[q] * wr - im[q] * wi, vi = re[q] * wi + im[q] * wr;
        re[q] = re[p] - vr; im[q] = im[p] - vi;
        re[p] += vr; im[p] += vi;
      }
  }
}

static void ses_pcm_bosalt(Ses *s) {
  if (s->n_pcm && s->cb) s->cb(s->cb_kul, s->pcm, s->n_pcm);
  s->n_pcm = 0;
}

static void ses_ornek_ver(Ses *s, const float *x, int n) {
  if (s->kanca_dalga) s->kanca_dalga(s->kanca_kul, x, n);
  for (int i = 0; i < n; i++) {
    float v = x[i] > 1.f ? 1.f : x[i] < -1.f ? -1.f : x[i];
    s->pcm[s->n_pcm++] = (int16_t)lrintf(v * 32767.f);
    if (s->n_pcm == SES_PCM_N) ses_pcm_bosalt(s);
  }
  s->n_ornek += n;
}

// ola[0..n) örneklerini (kırpılmamış konum ola_bas+i) zarfa bölüp verir; kırpma: [N/2, N/2 + (T-1)*hop)
static void ses_ola_ver(Ses *s, int n) {
  const int N = s->n_fft, hop = s->hop, bas = N / 2, son = N / 2 + (s->T - 1) * hop;
  float tmp[64];
  int m = 0;
  for (int i = 0; i < n; i++) {
    int idx = s->ola_bas + i;
    if (idx < bas || idx >= son) continue;
    int f0 = idx >= N ? (idx - N) / hop + 1 : 0, f1 = idx / hop < s->T - 1 ? idx / hop : s->T - 1;
    float z = 0.f;
    for (int f = f0; f <= f1; f++) z += s->pen2[idx - f * hop];
    tmp[m++] = s->ola[i] / (z > 1e-8f ? z : 1e-8f);
    if (m == 64) { ses_ornek_ver(s, tmp, m); m = 0; }
  }
  if (m) ses_ornek_ver(s, tmp, m);
}

// Bir karenin çıktısı x[N_FFT+2] (log genlik | faz) -> dalga, üst üste ekle, biten hop örneği ver.
static void ses_istft_kare(Ses *s, const float *x) {
  const int N = s->n_fft, F = N / 2 + 1, hop = s->hop;
  float *re = s->fre, *im = s->fim;
  for (int k = 0; k < F; k++) {
    float lg = x[k], g = expf(lg > 6.f ? 6.f : lg), fz = x[F + k];
    re[k] = g * cosf(fz);
    im[k] = g * sinf(fz);
  }
  im[0] = 0.f; im[N / 2] = 0.f;
  for (int k = 1; k < N / 2; k++) { re[N - k] = re[k]; im[N - k] = -im[k]; }
  ses_ifft(s, re, im);
  const float olc = 1.f / N;
  for (int n = 0; n < N; n++) s->ola[n] += s->pen[n] * olc * re[n];
  ses_ola_ver(s, hop);
  memmove(s->ola, s->ola + hop, (N - hop) * sizeof(float));
  memset(s->ola + N - hop, 0, hop * sizeof(float));
  s->ola_bas += hop;
}

// ---------------------------------------------------------------- yükleme
static int ses_tensor(const uint8_t *img, size_t boyut, const char *ad, SesT *t, int satir, int sutun) {
  uint32_t n, taban;
  memcpy(&n, img + 12, 4);
  for (uint32_t i = 0; i < n; i++) {
    const uint8_t *e = img + 144 + 64 * i;
    if (strncmp((const char *)e, ad, 40) != 0) continue;
    uint32_t v[5];
    memcpy(v, e + 44, 20);
    t->tip = e[40];
    t->satir = (int)v[0]; t->sutun = (int)v[1]; t->grup = (int)v[2];
    t->kod = img + v[3];
    t->olcek = v[4] ? (const void *)(img + v[4]) : NULL;
    t->n_grup = t->tip == SES_Q4 ? t->sutun / t->grup : 1;
    t->satir_bayt = t->tip == SES_Q4 ? (t->sutun + 1) / 2 : t->sutun;
    taban = v[3];
    if (taban >= boyut || (satir >= 0 && t->satir * t->sutun != satir * sutun) ||
        (satir >= 0 && t->tip >= SES_Q4 && (t->satir != satir || t->sutun != sutun))) {
      ses_hata = "tensör boyutu uyuşmuyor";
      return -1;
    }
    if (satir >= 0) { t->satir = satir; t->sutun = sutun; }
    return 0;
  }
  ses_hata = "tensör yok";
  return -1;
}

static int ses_blok_bul(const uint8_t *img, size_t boyut, const char *onek, int d, int k, int h, SesBlok *b) {
  char ad[48];
  b->d = d; b->k = k; b->h = h;
  struct { const char *son; SesT *t; int satir, sutun; } l[] = {
      {"dw.weight", &b->dw_w, d, k}, {"dw.bias", &b->dw_b, 1, d}, {"ln.weight", &b->ln_g, 1, d},
      {"ln.bias", &b->ln_b, 1, d}, {"pw1.weight", &b->pw1_w, h, d}, {"pw1.bias", &b->pw1_b, 1, h},
      {"pw2.weight", &b->pw2_w, d, h}, {"pw2.bias", &b->pw2_b, 1, d}, {"gamma", &b->gamma, 1, d}};
  for (unsigned i = 0; i < sizeof l / sizeof l[0]; i++) {
    snprintf(ad, sizeof ad, "%s%s", onek, l[i].son);
    if (ses_tensor(img, boyut, ad, l[i].t, l[i].satir, l[i].sutun)) return -1;
  }
  return 0;
}

static void *ses_ay(struct Ses *s, SesAyir ayir, size_t n, int sicak);
static void *ses_varsayilan_ayir(size_t n, int sicak) {
#ifdef ESP_PLATFORM
  void *p = sicak ? heap_caps_malloc(n, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT) : NULL;
  return p ? p : heap_caps_malloc(n, MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT);
#else
  (void)sicak;
  return malloc(n);
#endif
}

static void *ses_ay(struct Ses *s, SesAyir ayir, size_t n, int sicak) {
  void *p = ayir(n, sicak);
  if (p) { if (sicak) s->bellek_sicak += n; else s->bellek_buyuk += n; }
  return p;
}

// Döner 0; hata: -1 (ses_hata). img flash'ta (mmap) ya da RAM'de kalmalı. ayir NULL: heap_caps / malloc.
// Tamponlar bir kez ayrılır (serbest bırakılmaz); varsayılan boyutlarda ~470 KB büyük (PSRAM olabilir) +
// ~210 KB sıcak (dahili SRAM tercih). Miktar: s->bellek_buyuk / s->bellek_sicak.
SES_API int ses_yukle(Ses *s, const uint8_t *img, size_t boyut, SesAyir ayir) {
  memset(s, 0, sizeof *s);
  s->hiz = 1.f;
  if (!ayir) ayir = ses_varsayilan_ayir;
  uint32_t sihir, surum, n;
  if (!img || boyut < 144) { ses_hata = "ses.bin yok"; return -1; }
  memcpy(&sihir, img, 4); memcpy(&surum, img + 4, 4); memcpy(&n, img + 12, 4);
  if (sihir != 0x31534553u) { ses_hata = "ses.bin değil (sihir)"; return -1; }
  if (surum != 1) { ses_hata = "ses.bin sürümü desteklenmiyor"; return -1; }
  if (144 + 64 * (size_t)n > boyut) { ses_hata = "ses.bin kısa"; return -1; }
  int32_t A[32];
  memcpy(A, img + 16, sizeof A);
  s->n_sembol = A[0]; s->n_mel = A[1]; s->n_fft = A[2]; s->hop = A[3]; s->sr = A[4];
  s->ad = A[5]; s->n_kod = A[6]; s->k_kod = A[7]; s->n_coz = A[8]; s->k_coz = A[9]; s->genis = A[10];
  s->d_tah = A[11]; s->n_tah = A[12]; s->k_tah = A[13];
  s->vd = A[14]; s->n_vblok = A[15]; s->vgenis = A[16]; s->vk = A[17]; s->vk_giris = A[18]; s->grup = A[19];
  if (s->n_sembol != 42 || s->n_kod > SES_MAX_BLOK || s->n_coz > SES_MAX_BLOK || s->n_tah > SES_MAX_BLOK ||
      s->n_vblok > SES_MAX_BLOK || (s->n_fft & (s->n_fft - 1)) || s->n_fft > 4096 || s->hop <= 0 ||
      s->n_fft % s->hop) {
    ses_hata = "desteklenmeyen ayar";
    return -1;
  }
  const int ad = s->ad, dt = s->d_tah, vd = s->vd, M = s->n_mel;
  char on[32];
  struct { const char *ad; SesT *t; int satir, sutun; } l[] = {
      {"a.gomme.weight", &s->gomme, s->n_sembol, ad},
      {"a.tah_giris.weight", &s->tah_giris_w, dt, ad}, {"a.tah_giris.bias", &s->tah_giris_b, 1, dt},
      {"a.tah_ln.weight", &s->tah_ln_g, 1, dt}, {"a.tah_ln.bias", &s->tah_ln_b, 1, dt},
      {"a.tah_cikis.weight", &s->tah_cikis_w, 3, dt}, {"a.tah_cikis.bias", &s->tah_cikis_b, 1, 3},
      {"a.perde_gomme.weight", &s->perde_w, ad, 3}, {"a.perde_gomme.bias", &s->perde_b, 1, ad},
      {"a.enerji_gomme.weight", &s->enerji_w, ad, 3}, {"a.enerji_gomme.bias", &s->enerji_b, 1, ad},
      {"a.coz_ln.weight", &s->coz_ln_g, 1, ad}, {"a.coz_ln.bias", &s->coz_ln_b, 1, ad},
      {"a.cikis.weight", &s->cikis_w, M, ad}, {"a.cikis.bias", &s->cikis_b, 1, M},
      {"v.giris.weight", &s->v_giris_w, vd, M * s->vk_giris}, {"v.giris.bias", &s->v_giris_b, 1, vd},
      {"v.ln0.weight", &s->v_ln0_g, 1, vd}, {"v.ln0.bias", &s->v_ln0_b, 1, vd},
      {"v.ln1.weight", &s->v_ln1_g, 1, vd}, {"v.ln1.bias", &s->v_ln1_b, 1, vd},
      {"v.cikis.weight", &s->v_cikis_w, s->n_fft + 2, vd}, {"v.cikis.bias", &s->v_cikis_b, 1, s->n_fft + 2}};
  for (unsigned i = 0; i < sizeof l / sizeof l[0]; i++)
    if (ses_tensor(img, boyut, l[i].ad, l[i].t, l[i].satir, l[i].sutun)) return -1;
  SesT ist;
  if (ses_tensor(img, boyut, "a.istat", &ist, 1, 4)) return -1;
  for (int i = 0; i < 4; i++) s->istat[i] = ses_v(&ist, i);
  for (int i = 0; i < s->n_kod; i++) {
    snprintf(on, sizeof on, "a.kod.%d.", i);
    if (ses_blok_bul(img, boyut, on, ad, s->k_kod, s->genis * ad, &s->kod[i])) return -1;
  }
  for (int i = 0; i < s->n_tah; i++) {
    snprintf(on, sizeof on, "a.tah.%d.", i);
    if (ses_blok_bul(img, boyut, on, dt, s->k_tah, s->genis * dt, &s->tah[i])) return -1;
  }
  for (int i = 0; i < s->n_coz; i++) {
    snprintf(on, sizeof on, "a.coz.%d.", i);
    if (ses_blok_bul(img, boyut, on, ad, s->k_coz, s->genis * ad, &s->coz[i])) return -1;
  }
  for (int i = 0; i < s->n_vblok; i++) {
    snprintf(on, sizeof on, "v.bloklar.%d.", i);
    if (ses_blok_bul(img, boyut, on, vd, s->vk, s->vgenis * vd, &s->vblok[i])) return -1;
  }

  // akış katmanları: çözücü blokları, vocoder girişi, vocoder blokları
  // (akış tamponları ve kodlayıcının geçici tamponları aynı alanı paylaşır: ikisi aynı anda kullanılmaz)
  int toplam_r = s->n_coz * (s->k_coz / 2) + s->vk_giris / 2 + s->n_vblok * (s->vk / 2);
  size_t akis_n = 0;
  s->kmax = SES_PARCA + toplam_r;   // bir adımda bir katmandan çıkabilecek en çok kare (akış sonunda)
  s->n_akis = 0;
  for (int i = 0; i < s->n_coz + 1 + s->n_vblok; i++) {
    SesAkis *a = &s->akis[s->n_akis++];
    if (i < s->n_coz) { a->tip = 0; a->b = &s->coz[i]; a->d_in = a->d_out = ad; }
    else if (i == s->n_coz) { a->tip = 1; a->b = NULL; a->d_in = M; a->d_out = vd; }
    else { a->tip = 0; a->b = &s->vblok[i - s->n_coz - 1]; a->d_in = a->d_out = vd; }
    a->r = (a->tip == 1 ? s->vk_giris : a->b->k) / 2;
    a->kap = 2 * a->r + SES_PARCA;
    akis_n += (size_t)a->kap * a->d_in;
  }
  {
    int dm = ad > vd ? ad : vd;
    if (dt > dm) dm = dt;
    if (M > dm) dm = M;
    int de = ad > dt ? ad : dt;
    int hm = s->genis * dm > s->vgenis * vd ? s->genis * dm : s->vgenis * vd;
    int um = dm > s->n_fft + 2 ? dm : s->n_fft + 2;
    int cm = hm > M * s->vk_giris ? hm : M * s->vk_giris;
    int km = s->k_kod > s->k_coz ? s->k_kod : s->k_coz;
    if (s->k_tah > km) km = s->k_tah;
    if (s->vk > km) km = s->vk;
    if (cm < km) cm = km;
    const size_t F = sizeof(float), N = s->n_fft;
    size_t alan_n = (size_t)SES_MAX_SEMBOL * (de + dt);
    if (akis_n > alan_n) alan_n = akis_n;
    s->ex = (float *)ses_ay(s, ayir, SES_MAX_SEMBOL * de * F, 0);
    s->alan = (float *)ses_ay(s, ayir, alan_n * F, 0);
    if (!s->alan) goto yer_yok;
    for (int i = 0, o = 0; i < s->n_akis; i++) {
      s->akis[i].buf = s->alan + o;
      o += s->akis[i].kap * s->akis[i].d_in;
    }
    s->tahmin = (float *)ses_ay(s, ayir, SES_MAX_SEMBOL * 3 * F, 0);
    s->sure = (int *)ses_ay(s, ayir, SES_MAX_SEMBOL * sizeof(int), 0);
    s->kod_buf = (int *)ses_ay(s, ayir, SES_MAX_KOD * sizeof(int), 0);
    s->pA = (float *)ses_ay(s, ayir, (size_t)s->kmax * dm * F, 0);
    s->pB = (float *)ses_ay(s, ayir, (size_t)s->kmax * dm * F, 0);
    s->z = (float *)ses_ay(s, ayir, SES_ALT * dm * F, 1);
    s->hid = (float *)ses_ay(s, ayir, SES_ALT * hm * F, 1);
    s->u = (float *)ses_ay(s, ayir, SES_ALT * um * F, 1);
    s->col = (float *)ses_ay(s, ayir, SES_ALT * M * s->vk_giris * F, 1);
    s->dwt = (float *)ses_ay(s, ayir, km * dm * F, 1);
    s->satir[0] = (float *)ses_ay(s, ayir, cm * F, 1);
    s->satir[1] = (float *)ses_ay(s, ayir, cm * F, 1);
    s->fre = (float *)ses_ay(s, ayir, N * F, 1);
    s->fim = (float *)ses_ay(s, ayir, N * F, 1);
    s->pen = (float *)ses_ay(s, ayir, N * F, 1);
    s->pen2 = (float *)ses_ay(s, ayir, N * F, 1);
    s->ola = (float *)ses_ay(s, ayir, N * F, 1);
    s->tc = (float *)ses_ay(s, ayir, N / 2 * F, 1);
    s->ts = (float *)ses_ay(s, ayir, N / 2 * F, 1);
    s->ters = (int16_t *)ses_ay(s, ayir, N * sizeof(int16_t), 1);
    s->pcm = (int16_t *)ses_ay(s, ayir, SES_PCM_N * sizeof(int16_t), 1);
    if (!s->ex || !s->tahmin || !s->sure || !s->kod_buf || !s->pA || !s->pB || !s->z ||
        !s->hid || !s->u || !s->col || !s->dwt || !s->satir[0] || !s->satir[1] || !s->fre || !s->fim ||
        !s->pen || !s->pen2 || !s->ola || !s->tc || !s->ts || !s->ters || !s->pcm)
      goto yer_yok;
    for (size_t i = 0; i < N; i++) {  // torch.hann_window (periyodik), float64'te hesaplanıp float'a
      double w = 0.5 - 0.5 * cos(2.0 * SES_PI * (double)i / (double)N);
      s->pen[i] = (float)w;
      s->pen2[i] = (float)(w * w);
    }
    for (size_t i = 0; i < N / 2; i++) {
      s->tc[i] = (float)cos(2.0 * SES_PI * (double)i / (double)N);
      s->ts[i] = (float)sin(2.0 * SES_PI * (double)i / (double)N);
    }
    int lg = 0;
    while ((1u << lg) < N) lg++;
    for (size_t i = 0; i < N; i++) {
      int r = 0;
      for (int b = 0; b < lg; b++) if (i & (1u << b)) r |= 1 << (lg - 1 - b);
      s->ters[i] = (int16_t)r;
    }
  }
  return 0;
yer_yok:
  ses_hata = "bellek ayrılamadı";
  return -1;
}

// ---------------------------------------------------------------- sentez
// ids[0..n) (n <= SES_MAX_SEMBOL) -> ses; PCM cb'ye akar. Döner: örnek sayısı (<0 hata).
SES_API long ses_sentez(Ses *s, const int *ids, int n, SesPcm cb, void *kul) {
  if (n <= 0) return 0;
  if (n > SES_MAX_SEMBOL) { ses_hata = "cümle çok uzun"; return -1; }
  const int ad = s->ad, dt = s->d_tah, M = s->n_mel;
  s->cb = cb; s->cb_kul = kul; s->n_pcm = 0; s->n_ornek = 0; s->mac = 0;
  // gömme + kodlayıcı (x = ex; geçici tamponlar akış alanında: y [N x de], q [N x d_tah])
  float *x = s->ex, *y = s->alan;
  for (int i = 0; i < n; i++) {
    int id = ids[i] >= 0 && ids[i] < s->n_sembol ? ids[i] : 0;
    ses_satir_ac(&s->gomme, id, x + (size_t)i * ad);
  }
  for (int b = 0; b < s->n_kod; b++) {
    ses_blok(s, &s->kod[b], x, 0, n, 0, n, y);
    float *t = x; x = y; y = t;
  }
  if (x != s->ex) { memcpy(s->ex, x, (size_t)n * ad * sizeof(float)); y = x; x = s->ex; }
  // tahminci (x kodlayıcı çıkışı; y ve q boş)
  float *p = y, *q = s->alan + (size_t)SES_MAX_SEMBOL * (ad > dt ? ad : dt);
  ses_mat(s, &s->tah_giris_w, &s->tah_giris_b, x, n, ad, p, dt);
  for (int b = 0; b < s->n_tah; b++) {
    ses_blok(s, &s->tah[b], p, 0, n, 0, n, q);
    float *t = p; p = q; q = t;
  }
  for (int i = 0; i < n; i++) ses_ln(p + (size_t)i * dt, dt, &s->tah_ln_g, &s->tah_ln_b);
  ses_mat(s, &s->tah_cikis_w, &s->tah_cikis_b, p, n, dt, s->tahmin, 3);
  long T = 0;
  float kay = s->perde_kaydir != 0.f ? s->perde_kaydir * 0.69314718f / 12.f / s->istat[1] : 0.f;
  for (int i = 0; i < n; i++) {
    float e = (expf(s->tahmin[i * 3]) - 1.f) * s->hiz;
    if (!(e < 2000.f)) e = 2000.f;
    int d = (int)rintf(e);
    s->sure[i] = d < 1 ? 1 : d;
    T += s->sure[i];
    if (kay != 0.f) s->tahmin[i * 3 + 1] += kay;
  }
  if (s->kanca_sure) s->kanca_sure(s->kanca_kul, s->sure, n);
  // koşullama: h = (x + perde_gomme(perde)) + enerji_gomme(enerji), x'in yerine
  float *h = x;
  float wp[3], we[3];
  for (int c = 0; c < ad; c++) {
    ses_satir_ac(&s->perde_w, c, wp);
    ses_satir_ac(&s->enerji_w, c, we);
    float bp = ses_v(&s->perde_b, c), be = ses_v(&s->enerji_b, c);
    for (int i = 0; i < n; i++) {
      float a = 0.f, e = 0.f;
      for (int j = 0; j < 3; j++) {
        int t = i - 1 + j;
        if (t < 0 || t >= n) continue;
        a += wp[j] * s->tahmin[t * 3 + 1];
        e += we[j] * s->tahmin[t * 3 + 2];
      }
      h[(size_t)i * ad + c] = x[(size_t)i * ad + c] + (a + bp) + (e + be);
    }
  }
  // çözücü + vocoder akışı
  s->T = (int)T; s->ola_bas = 0;
  memset(s->ola, 0, s->n_fft * sizeof(float));
  for (int i = 0; i < s->n_akis; i++) { s->akis[i].bas = s->akis[i].son = s->akis[i].cikan = 0; }
  int f = 0, sym = 0, kalan = s->sure[0];
  while (f < s->T) {
    int m = s->T - f < SES_PARCA ? s->T - f : SES_PARCA;
    for (int j = 0; j < m; j++) {  // uzunluk düzenleme
      memcpy(s->pA + (size_t)j * ad, h + (size_t)sym * ad, ad * sizeof(float));
      if (--kalan == 0 && sym + 1 < n) kalan = s->sure[++sym];
    }
    f += m;
    float *cur = s->pA, *nxt = s->pB, *t;
    int ai = 0;
    for (; ai < s->n_coz; ai++) {
      m = ses_akis_it(s, &s->akis[ai], cur, m, s->T, nxt);
      if (m < 0) return -1;
      t = cur; cur = nxt; nxt = t;
    }
    if (m == 0) continue;
    for (int a = 0; a < m; a += SES_ALT) {  // coz_ln + çıkış -> mel
      int k = m - a < SES_ALT ? m - a : SES_ALT;
      for (int i = 0; i < k; i++) {
        memcpy(s->z + (size_t)i * ad, cur + (size_t)(a + i) * ad, ad * sizeof(float));
        ses_ln(s->z + (size_t)i * ad, ad, &s->coz_ln_g, &s->coz_ln_b);
      }
      ses_mat(s, &s->cikis_w, &s->cikis_b, s->z, k, ad, nxt + (size_t)a * M, M);
    }
    if (s->kanca_mel) s->kanca_mel(s->kanca_kul, nxt, m);
    t = cur; cur = nxt; nxt = t;
    for (; ai < s->n_akis; ai++) {
      m = ses_akis_it(s, &s->akis[ai], cur, m, s->T, nxt);
      if (m < 0) return -1;
      t = cur; cur = nxt; nxt = t;
    }
    for (int a = 0; a < m; a += SES_ALT) {  // ln1 + çıkış -> genlik/faz -> iSTFT
      int k = m - a < SES_ALT ? m - a : SES_ALT;
      for (int i = 0; i < k; i++) {
        memcpy(s->z + (size_t)i * s->vd, cur + (size_t)(a + i) * s->vd, s->vd * sizeof(float));
        ses_ln(s->z + (size_t)i * s->vd, s->vd, &s->v_ln1_g, &s->v_ln1_b);
      }
      ses_mat(s, &s->v_cikis_w, &s->v_cikis_b, s->z, k, s->vd, s->u, s->n_fft + 2);
      for (int i = 0; i < k; i++) ses_istft_kare(s, s->u + (size_t)i * (s->n_fft + 2));
    }
  }
  ses_ola_ver(s, s->n_fft - s->hop);  // son karenin kalan örnekleri
  ses_pcm_bosalt(s);
  return s->n_ornek;
}

// Bir cümle: metin -> ses. SES_MAX_SEMBOL'den uzunsa son boşluk/virgülden bölünür. Döner: örnek sayısı.
SES_API long ses_cumle_n(Ses *s, const char *metin, size_t bayt, SesPcm cb, void *kul) {
  int n = metin_kodla_n(metin, bayt, s->kod_buf, SES_MAX_KOD), bas = 0;
  long top = 0;
  while (bas < n) {
    int son = n;
    if (son - bas > SES_MAX_SEMBOL) {
      son = bas + SES_MAX_SEMBOL;
      int b = son;
      while (b > bas + SES_MAX_SEMBOL / 2 && s->kod_buf[b - 1] != 1 && s->kod_buf[b - 1] != 2) b--;
      if (b > bas + SES_MAX_SEMBOL / 2) son = b;
    }
    int e = son;
    while (e > bas && s->kod_buf[e - 1] == 1) e--;  // sondaki boşluk
    long r = ses_sentez(s, s->kod_buf + bas, e - bas, cb, kul);
    if (r < 0) return r;
    top += r;
    bas = son;
    while (bas < n && s->kod_buf[bas] == 1) bas++;
  }
  return top;
}
SES_API long ses_cumle(Ses *s, const char *metin, SesPcm cb, void *kul) {
  return ses_cumle_n(s, metin, strlen(metin), cb, kul);
}

SES_API void ses_sessizlik(Ses *s, int ms, SesPcm cb, void *kul) {
  s->cb = cb; s->cb_kul = kul; s->n_pcm = 0;
  int n = (int)((long)s->sr * ms / 1000);
  while (n > 0) {
    int k = n < SES_PCM_N ? n : SES_PCM_N;
    memset(s->pcm, 0, k * sizeof(int16_t));
    if (cb) cb(kul, s->pcm, k);
    n -= k;
  }
}

// Metni cümlelere böler (. ! ? … ve satır sonu; ardından gelen tırnak/ayraçlar cümleye dahil; sonrası küçük
// harfle sürüyorsa bölmez: "Dur!" dedi.), her cümleyi
// seslendirir, aralara ara_ms sessizlik koyar. dur() 1 dönerse (NULL olabilir) cümle aralarında durur.
SES_API long ses_metin(Ses *s, const char *metin, SesPcm cb, void *kul, int ara_ms, int (*dur)(void *kul)) {
  const char *p = metin, *bas = metin;
  long top = 0;
  int ilk = 1;
  for (;;) {
    char c = *p;
    int son = c == 0 || c == '\n' || c == '.' || c == '!' || c == '?' ||
              ((unsigned char)c == 0xE2 && (unsigned char)p[1] == 0x80 && (unsigned char)p[2] == 0xA6);
    if (!son) { p++; continue; }
    if (c) {  // noktalama dizisi ve kapanış tırnakları cümlede kalsın
      for (;;) {
        unsigned char u = (unsigned char)*p;
        if (u == '.' || u == '!' || u == '?' || u == '"' || u == '\'' || u == ')') p++;
        else if (u == 0xE2 && (unsigned char)p[1] == 0x80 &&
                 ((unsigned char)p[2] == 0xA6 || (unsigned char)p[2] == 0x9D || (unsigned char)p[2] == 0x99))
          p += 3;
        else break;
      }
      if (*p == '\n') p++;
      else {  // ardından küçük harfle devam ediyorsa ("Dur!" dedi) cümle bitmemiş
        const unsigned char *q = (const unsigned char *)p;
        while (*q == ' ' || *q == '\t') q++;
        if (*q) {
          int L = 1;
          while (L < 4 && q[L]) L++;
          uint32_t c2 = ses_utf8(&q, q + L);
          if (ses_kucult(c2) == c2 && ses_sembol_id(c2) >= 10) continue;
        }
      }
    }
    int harf = 0;
    for (const char *q = bas; q < p; q++)
      if (((unsigned char)*q >= 'A' && (unsigned char)*q <= 'z') || (unsigned char)*q >= 0xC0) { harf = 1; break; }
    if (harf) {
      if (!ilk && ara_ms > 0) ses_sessizlik(s, ara_ms, cb, kul);
      if (dur && dur(kul)) return top;
      long r = ses_cumle_n(s, bas, (size_t)(p - bas), cb, kul);
      if (r < 0) return r;
      top += r;
      ilk = 0;
    }
    if (!*p) break;
    bas = p;
  }
  return top;
}
