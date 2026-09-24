// Örnekleyici: tekrar cezası, yasaklı token maskesi, top-k + sıcaklık seçimi, log-olasılık.
// PC'deki gen.c ile ESP32 firmware'i aynı kodu kullanır. Düz C99; token başına malloc yok:
// tekrar penceresi OrnDurum içinde sabit bir halka tampon, top-k karalama alanını çağıran verir.
//
// Kullanım (her token için):
//   OrnAyar a = {sicaklik, top_k, tekrar, yasak, n_yasak, govde_yasak, n_govde_yasak, idx, p};
//   OrnDurum d; orn_sifirla(&d);
//   for (istem token'ı t) { if (istem_pencereye) orn_ekle(&d, t); llm_forward(...); }
//   d.govde = 1;                               // istem başlığın tamamını taşıyorsa gövde hemen başlar
//   int tok = orn_adim(&a, &d, logits, V);     // ceza ve yasaklar logits'e yerinde uygulanır
//
// Rastgelelik ORNEKLE_RASTGELE() ile gelir, varsayılanı rand(); firmware kendi üretecini tanımlayabilir.
#ifndef ORNEKLE_H
#define ORNEKLE_H
#include <math.h>

#ifndef ORNEKLE_PENCERE
#define ORNEKLE_PENCERE 64            /* tekrar cezasının baktığı son token sayısı */
#endif
#ifndef ORNEKLE_RASTGELE
#include <stdlib.h>
#define ORNEKLE_RASTGELE() ((double)rand() / RAND_MAX)   /* [0, 1] aralığında */
#endif
#define ORNEKLE_YASAK_LOGIT (-1e30f)

typedef struct {
  float sicaklik;                  /* <= 0: greedy (argmax) */
  int top_k;                       /* >= 1; idx ve p en az bu kadar eleman */
  float tekrar;                    /* CTRL tekrar cezası; <= 1 kapalı */
  const int *yasak; int n_yasak;   /* her zaman yasak (gen.c -b) */
  const int *govde_yasak; int n_govde_yasak;  /* yalnızca hikâye gövdesinde yasak (gen.c -N) */
  int *idx; double *p;             /* çağıranın karalama alanı: top_k'şar eleman */
} OrnAyar;

typedef struct {
  int son[ORNEKLE_PENCERE];        /* tekrar penceresi (halka tampon) */
  int yaz, dolu;                   /* sıradaki yuva, dolu yuva sayısı */
  int govde;                       /* 1: hikâye gövdesi örnekleniyor, govde_yasak etkin */
} OrnDurum;

static inline void orn_sifirla(OrnDurum *d) { d->yaz = 0; d->dolu = 0; d->govde = 0; }

/* Pencereyi boşaltır, gövde bayrağına dokunmaz (ör. plan bitip gövde başlarken). */
static inline void orn_pencere_sifirla(OrnDurum *d) { d->yaz = 0; d->dolu = 0; }

static inline void orn_ekle(OrnDurum *d, int tok) {
  d->son[d->yaz] = tok;
  d->yaz = (d->yaz + 1) % ORNEKLE_PENCERE;
  if (d->dolu < ORNEKLE_PENCERE) d->dolu++;
}

/* CTRL tarzı ceza: pozitif logit küçülür, negatif olan daha da düşer. Pencerede geçen her farklı
 * token bir kez cezalanır, geçtiği kadar değil. Pencere tam doluyken tek geçiş: ~2K karşılaştırma. */
static inline void orn_tekrar_cezasi(float *lg, int V, const OrnDurum *d, float tekrar) {
  if (!(tekrar > 1.f)) return;
  for (int i = 0; i < d->dolu; i++) {
    int t = d->son[i], ayni = 0;
    for (int j = 0; j < i && !ayni; j++) ayni = d->son[j] == t;
    if (ayni || t < 0 || t >= V) continue;
    lg[t] = lg[t] > 0 ? lg[t] / tekrar : lg[t] * tekrar;
  }
}

static inline void orn_yasakla(float *lg, int V, const int *ids, int n) {
  for (int i = 0; i < n; i++) if (ids[i] >= 0 && ids[i] < V) lg[ids[i]] = ORNEKLE_YASAK_LOGIT;
}

/* sicaklik <= 0 ise argmax; yoksa en yüksek k logit arasından exp((l - max) / sicaklik) ağırlığıyla.
 * idx ve p en az k elemanlı karalama alanı. Eşitlikte küçük id önce gelir. */
static inline int orn_sec(const float *lg, int V, float sicaklik, int k, int *idx, double *p) {
  int best = 0; for (int v = 1; v < V; v++) if (lg[v] > lg[best]) best = v;
  if (sicaklik <= 0) return best;
  if (k < 1) k = 1;
  int n = 0;
  for (int v = 0; v < V; v++) {          // top-k, eklemeli sıralama
    int j = n < k ? n++ : k;
    if (j == k && lg[v] <= lg[idx[k - 1]]) continue;
    if (j == k) j = k - 1;
    while (j > 0 && lg[idx[j - 1]] < lg[v]) { idx[j] = idx[j - 1]; j--; }
    idx[j] = v;
  }
  double sum = 0;
  for (int i = 0; i < n; i++) sum += p[i] = exp((lg[idx[i]] - lg[best]) / sicaklik);
  double r = ORNEKLE_RASTGELE() * sum; int out = idx[n - 1];
  for (int i = 0; i < n; i++) if ((r -= p[i]) <= 0) { out = idx[i]; break; }
  return out;
}

/* log softmax(lg)[tok]. orn_adim'dan sonra çağrılırsa ceza ve yasaklar dahil (gen.c -l böyle). */
static inline double orn_logp(const float *lg, int V, int tok) {
  float mx = lg[0]; for (int v = 1; v < V; v++) if (lg[v] > mx) mx = lg[v];
  double z = 0; for (int v = 0; v < V; v++) z += exp(lg[v] - mx);
  return lg[tok] - mx - log(z);
}

/* Bir token seçer: tekrar cezası, yasaklar (gövdedeyse gövde yasakları da) logits'e yerinde
 * uygulanır, seçilen token pencereye eklenir. */
static inline int orn_adim(const OrnAyar *a, OrnDurum *d, float *lg, int V) {
  orn_tekrar_cezasi(lg, V, d, a->tekrar);
  orn_yasakla(lg, V, a->yasak, a->n_yasak);
  if (d->govde) orn_yasakla(lg, V, a->govde_yasak, a->n_govde_yasak);
  int tok = orn_sec(lg, V, a->sicaklik, a->top_k, a->idx, a->p);
  orn_ekle(d, tok);
  return tok;
}

#endif
