// KWS: kartta Türkçe uyandırma sözcüğü ("Merhaba Eko") ve çocuk komutları (docs/URUN_TANIMI.md).
// Uyku sesli komut değil (gece figürü); "Uykum geldi" / "İyi geceler" olumsuz örnek olarak eğitildi.
//
// Giriş: INMP441'den 16 kHz mono int16 PCM, istenen boyda parçalarla (kws_isle her parçayla çağrılır).
// Çıkış: olay (KWS_*). Komutlar yalnız "Merhaba Eko"dan sonraki KWS_PENCERE_MS (~4 sn) içinde verilir; yumuşatma,
// eşik, tekrar engeli (debounce) ve bekleme süreleri içeride. Bir parçada birden çok olay olursa sıraya alınır,
// sonraki çağrılarda (gerekirse n = 0 ile) sırayla döner.
//
// Hesap (ses/kws/ortak.py ile aynı; tools/kws_test.py karşılaştırır):
//   öznitelik: 512 örnek Hann pencere, 320 örnek adım (saniyede 50 kare), 512 FFT, 40 mel (100–7800 Hz),
//              ln(mel + 1e-6) -> int8   (float; PC'deki numpy'dan yalnız yuvarlama farkı olabilir)
//   ağ:        nedensel genişletilmiş TCN, int8 ağırlık / int8 etkinlik / int32 toplam, tamsayı yeniden ölçekleme
//              (PyTorch int8 başvurusuyla bit bit aynı). Her karede yalnız yeni kare hesaplanır.
//   son işlem: softmax, KWS_YUMUSAT karelik ortalama, eşikler, bekleme süreleri.
// Ağırlıklar generated/kws_model.h'de (ses/kws/disa_aktar.py yazar), flash'ta sabit dizi; RAM ~12 KB.
//
// Kullanım:
//   if (!kws_kur()) { hata }
//   int olay = kws_isle(pcm, n);   // 16 kHz int16; olay != KWS_YOK ise işle
//
// Başlık dosyası hem C (tools/kws_test.c) hem C++ (.ino) olarak derlenir.
#pragma once
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#ifdef KWS_MODEL_BASLIK
#include KWS_MODEL_BASLIK   // denemelerde başka model başlığı (tools/kws_test.py)
#else
#include "generated/kws_model.h"
#endif

enum {
  KWS_YOK = 0,
  KWS_UYANDIRMA,
  KWS_DUR,
  KWS_DEVAM,
  KWS_BASKA,
  KWS_BIR_DAHA,
  KWS_SESI_AC,
  KWS_SESI_KIS
};

#if defined(__GNUC__)
#define KWS_API static __attribute__((unused))
#else
#define KWS_API static
#endif

// Son işlem ayarları (derlemeden önce tanımlanarak değiştirilebilir; varsayılanlar kws_model.h'de, eğitimde seçilen)
#ifndef KWS_ESIK_UYAN
#define KWS_ESIK_UYAN KWS_M_ESIK_UYAN        // "Merhaba Eko" olasılık eşiği (yumuşatılmış)
#endif
#ifndef KWS_ESIK_KOMUT
#define KWS_ESIK_KOMUT KWS_M_ESIK_KOMUT      // komut olasılık eşiği
#endif
#ifndef KWS_YUMUSAT
#define KWS_YUMUSAT KWS_M_YUMUSAT            // ortalaması alınan kare (20 ms)
#endif
#ifndef KWS_PENCERE_MS
#define KWS_PENCERE_MS 4000                  // uyandırmadan sonra komut beklenen süre
#endif
#ifndef KWS_UYAN_BEKLE_MS
#define KWS_UYAN_BEKLE_MS 1500               // iki uyandırma arası en az
#endif
#ifndef KWS_KOMUT_BEKLE_MS
#define KWS_KOMUT_BEKLE_MS 600               // komuttan sonra yeni komut için en az
#endif
#ifndef KWS_KOMUT_GECIKME_MS
#define KWS_KOMUT_GECIKME_MS 100             // uyandırmadan hemen sonra komut sayılmayan süre
#endif

#define KWS_KARE_MS (1000 * KWS_ADIM / 16000)
#define KWS_SIRA 8

typedef struct {
  // öznitelik
  int16_t pcm[KWS_PENCERE];
  int dolu;
  float re[KWS_NFFT], im[KWS_NFFT];
  float cos_t[KWS_NFFT / 2], sin_t[KWS_NFFT / 2];
  uint16_t ters[KWS_NFFT];
  float pencere[KWS_PENCERE];
  // ağ geçmişi: katman l girişinin son (K-1)*d+1 karesi, halka
  int8_t g0[KWS_K][KWS_NMEL];
  int8_t gb[KWS_GECMIS_TOPLAM];
  int konum[KWS_NBLOK + 1];
  int8_t h[KWS_KANAL], c[KWS_KANAL];
  // çıkış
  int32_t logit[KWS_NSINIF];
  float olas[KWS_NSINIF];
  float yum[KWS_YUMUSAT][KWS_NSINIF];
  long kare;
  long son_uyan, pencere_son, komut_engel;
  int sira[KWS_SIRA], sira_bas, sira_n;
} KwsDurum;

static KwsDurum kws_d;

static const int kws_gen[KWS_NBLOK] = KWS_GENISLEME_DIZI;

static inline int32_t kws_rq(int32_t acc, int32_t m, int s) {
  return (int32_t)(((int64_t)acc * m + ((int64_t)1 << (s - 1))) >> s);
}

static inline int32_t kws_sinir(int32_t v, int32_t a, int32_t b) { return v < a ? a : (v > b ? b : v); }

static inline int32_t kws_nokta(const int8_t *w, const int8_t *x, int n) {
  int32_t a = 0;
  for (int i = 0; i < n; i++) a += (int32_t)w[i] * (int32_t)x[i];
  return a;
}

KWS_API void kws_sifirla(void) {
  memset(kws_d.g0, 0, sizeof(kws_d.g0));
  memset(kws_d.gb, 0, sizeof(kws_d.gb));
  memset(kws_d.konum, 0, sizeof(kws_d.konum));
  memset(kws_d.yum, 0, sizeof(kws_d.yum));
  kws_d.dolu = 0;
  kws_d.kare = 0;
  kws_d.son_uyan = -1000000;
  kws_d.pencere_son = -1;
  kws_d.komut_engel = -1;
  kws_d.sira_bas = kws_d.sira_n = 0;
}

KWS_API bool kws_kur(void) {
  int n = KWS_NFFT, b = 0;
  while ((1 << b) < n) b++;
  for (int i = 0; i < n; i++) {
    int r = 0;
    for (int j = 0; j < b; j++) r |= ((i >> j) & 1) << (b - 1 - j);
    kws_d.ters[i] = (uint16_t)r;
  }
  for (int i = 0; i < n / 2; i++) {
    kws_d.cos_t[i] = (float)cos(2.0 * 3.14159265358979323846 * i / n);
    kws_d.sin_t[i] = (float)-sin(2.0 * 3.14159265358979323846 * i / n);
  }
  for (int i = 0; i < KWS_PENCERE; i++)
    kws_d.pencere[i] = (float)(0.5 - 0.5 * cos(2.0 * 3.14159265358979323846 * i / KWS_PENCERE));
  kws_sifirla();
  return KWS_SURUM == 1;
}

// 512 karmaşık FFT (radix-2, yerinde)
static void kws_fft(float *re, float *im) {
  const int n = KWS_NFFT;
  for (int i = 0; i < n; i++) {
    int j = kws_d.ters[i];
    if (j > i) {
      float t = re[i]; re[i] = re[j]; re[j] = t;
      t = im[i]; im[i] = im[j]; im[j] = t;
    }
  }
  for (int boy = 2; boy <= n; boy <<= 1) {
    int yarim = boy >> 1, adim = n / boy;
    for (int i = 0; i < n; i += boy) {
      for (int j = 0; j < yarim; j++) {
        float wr = kws_d.cos_t[j * adim], wi = kws_d.sin_t[j * adim];
        float xr = re[i + j + yarim], xi = im[i + j + yarim];
        float tr = xr * wr - xi * wi, ti = xr * wi + xi * wr;
        re[i + j + yarim] = re[i + j] - tr;
        im[i + j + yarim] = im[i + j] - ti;
        re[i + j] += tr;
        im[i + j] += ti;
      }
    }
  }
}

// Bir karenin int8 özniteliği (kws_d.pcm'deki 512 örnekten)
KWS_API void kws_oznitelik(int8_t *q) {
  for (int i = 0; i < KWS_NFFT; i++) {
    kws_d.re[i] = i < KWS_PENCERE ? ((float)kws_d.pcm[i] / 32768.0f) * kws_d.pencere[i] : 0.0f;
    kws_d.im[i] = 0.0f;
  }
  kws_fft(kws_d.re, kws_d.im);
  for (int k = 0; k <= KWS_NFFT / 2; k++) kws_d.re[k] = kws_d.re[k] * kws_d.re[k] + kws_d.im[k] * kws_d.im[k];
  for (int j = 0; j < KWS_NMEL; j++) {
    const float *w = kws_mel_w + kws_mel_ofs[j];
    const float *p = kws_d.re + kws_mel_bas[j];
    float s = 0.0f;
    for (int i = 0; i < kws_mel_n[j]; i++) s += w[i] * p[i];
    float lm = logf(s + KWS_EPS);
    float v = floorf((lm - KWS_LN_ALT) / KWS_LN_ADIM + 0.5f);
    if (v < 0.0f) v = 0.0f;
    if (v > 255.0f) v = 255.0f;
    q[j] = (int8_t)((int)v - 128);
  }
}

// Ağın bir adımı: q (int8 öznitelik) -> kws_d.logit (int32)
KWS_API void kws_ag_adim(const int8_t *q) {
  // giriş katmanı (d = 1): geçmiş halka K kare
  int p0 = kws_d.konum[0];
  memcpy(kws_d.g0[p0], q, KWS_NMEL);
  kws_d.konum[0] = (p0 + 1) % KWS_K;
  for (int o = 0; o < KWS_KANAL; o++) {
    int32_t acc = kws_b0[o];
    for (int k = 0; k < KWS_K; k++) {
      int f = (p0 - (KWS_K - 1 - k) + KWS_K) % KWS_K;
      acc += kws_nokta(kws_w0 + ((size_t)o * KWS_K + k) * KWS_NMEL, kws_d.g0[f], KWS_NMEL);
    }
    kws_d.h[o] = (int8_t)kws_sinir(kws_rq(acc, kws_m0[o], kws_s0[o]), 0, 127);
  }
  // artık bloklar
  int8_t *gecmis = kws_d.gb;
  for (int l = 0; l < KWS_NBLOK; l++) {
    int d = kws_gen[l], uz = (KWS_K - 1) * d + 1;
    int p = kws_d.konum[l + 1];
    memcpy(gecmis + (size_t)p * KWS_KANAL, kws_d.h, KWS_KANAL);
    kws_d.konum[l + 1] = (p + 1) % uz;
    const int8_t *W = kws_wb + (size_t)l * KWS_KANAL * KWS_K * KWS_KANAL;
    const int32_t *B = kws_bb + l * KWS_KANAL;
    const int32_t *M = kws_mb + l * KWS_KANAL;
    const int8_t *S = kws_sb + l * KWS_KANAL;
    for (int o = 0; o < KWS_KANAL; o++) {
      int32_t acc = B[o];
      for (int k = 0; k < KWS_K; k++) {
        int f = (p - (KWS_K - 1 - k) * d + uz * KWS_K) % uz;
        acc += kws_nokta(W + ((size_t)o * KWS_K + k) * KWS_KANAL, gecmis + (size_t)f * KWS_KANAL, KWS_KANAL);
      }
      kws_d.c[o] = (int8_t)kws_sinir(kws_rq(acc, M[o], S[o]), 0, 127);
    }
    for (int o = 0; o < KWS_KANAL; o++) {
      int32_t v = ((int32_t)kws_d.h[o] * kws_mh[l] + (int32_t)kws_d.c[o] * kws_mc[l] + (1 << 15)) >> 16;
      kws_d.h[o] = (int8_t)kws_sinir(v, 0, 127);
    }
    gecmis += (size_t)uz * KWS_KANAL;
  }
  for (int o = 0; o < KWS_NSINIF; o++)
    kws_d.logit[o] = kws_bc[o] + kws_nokta(kws_wc + (size_t)o * KWS_KANAL, kws_d.h, KWS_KANAL);
}

static void kws_sira_ekle(int olay) {
  if (kws_d.sira_n < KWS_SIRA) {
    kws_d.sira[(kws_d.sira_bas + kws_d.sira_n) % KWS_SIRA] = olay;
    kws_d.sira_n++;
  }
}

// Son işlem: bir kare olasılıklarından olay (ses/kws/ortak.py SonIslem ile aynı)
static void kws_karar(void) {
  float en = (float)kws_d.logit[0] * KWS_CIKIS_OLCEK, top = 0.0f;
  for (int i = 1; i < KWS_NSINIF; i++) {
    float v = (float)kws_d.logit[i] * KWS_CIKIS_OLCEK;
    if (v > en) en = v;
  }
  for (int i = 0; i < KWS_NSINIF; i++) {
    kws_d.olas[i] = expf((float)kws_d.logit[i] * KWS_CIKIS_OLCEK - en);
    top += kws_d.olas[i];
  }
  for (int i = 0; i < KWS_NSINIF; i++) kws_d.olas[i] /= top;
  long t = kws_d.kare;
  memcpy(kws_d.yum[t % KWS_YUMUSAT], kws_d.olas, sizeof(kws_d.olas));
  if (t + 1 < KWS_YUMUSAT) return;
  float p[KWS_NSINIF];
  for (int i = 0; i < KWS_NSINIF; i++) {
    float s = 0.0f;
    for (int j = 0; j < KWS_YUMUSAT; j++) s += kws_d.yum[j][i];
    p[i] = s / (float)KWS_YUMUSAT;
  }
  const long pencere = KWS_PENCERE_MS / KWS_KARE_MS, ub = KWS_UYAN_BEKLE_MS / KWS_KARE_MS;
  const long kb = KWS_KOMUT_BEKLE_MS / KWS_KARE_MS, kg = KWS_KOMUT_GECIKME_MS / KWS_KARE_MS;
  if (p[2] >= KWS_ESIK_UYAN && t - kws_d.son_uyan >= ub) {
    kws_sira_ekle(KWS_UYANDIRMA);
    kws_d.son_uyan = t;
    kws_d.pencere_son = t + pencere;
    kws_d.komut_engel = t + kg;
    return;
  }
  if (t <= kws_d.pencere_son && t >= kws_d.komut_engel) {
    int c = 3;
    for (int i = 4; i < KWS_NSINIF; i++)
      if (p[i] > p[c]) c = i;
    if (p[c] >= KWS_ESIK_KOMUT) {
      kws_sira_ekle(c - 1);
      kws_d.pencere_son = -1;
      kws_d.komut_engel = t + kb;
    }
  }
}

static int kws_sira_al(void) {
  if (!kws_d.sira_n) return KWS_YOK;
  int o = kws_d.sira[kws_d.sira_bas];
  kws_d.sira_bas = (kws_d.sira_bas + 1) % KWS_SIRA;
  kws_d.sira_n--;
  return o;
}

// 16 kHz int16 PCM parçası işle; olay ya da KWS_YOK döner.
KWS_API int kws_isle(const int16_t *pcm, int n) {
  int8_t q[KWS_NMEL];
  for (int i = 0; i < n;) {
    int al = KWS_PENCERE - kws_d.dolu;
    if (al > n - i) al = n - i;
    memcpy(kws_d.pcm + kws_d.dolu, pcm + i, (size_t)al * sizeof(int16_t));
    kws_d.dolu += al;
    i += al;
    if (kws_d.dolu == KWS_PENCERE) {
      kws_oznitelik(q);
      kws_ag_adim(q);
      kws_karar();
      kws_d.kare++;
      memmove(kws_d.pcm, kws_d.pcm + KWS_ADIM, (size_t)(KWS_PENCERE - KWS_ADIM) * sizeof(int16_t));
      kws_d.dolu = KWS_PENCERE - KWS_ADIM;
    }
  }
  return kws_sira_al();
}

// Tanı: son karenin olasılıkları (KWS_NSINIF: ARKA, KONUSMA, UYANDIRMA, DUR, DEVAM, BASKA, BIR_DAHA, SESI_AC, SESI_KIS)
KWS_API const float *kws_olasiliklar(void) { return kws_d.olas; }
