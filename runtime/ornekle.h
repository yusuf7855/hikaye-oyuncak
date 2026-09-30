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
// Plan modu (gen.c -S): istem "…\nSorun:" ile biter, model önce plan satırlarını ("<sorun>\nÇözüm: <çözüm>"),
// sonra iki satır sonu (nl nl) ve gövdeyi yazar. d.govde = 1 yerine orn_plan_baslat(&d, nl) çağrılır; her
// orn_adim'dan sonra d.govde (gövde başladı mı) ve d.plan_bozuk (ORNEKLE_PLAN_SINIR token'da gövdeye
// varılamadı: üretim durmalı, aday atılır) okunur. Plan token'ları tekrar penceresine hiç girmez; gövde
// başlarken pencere planın başındaki hâlindedir (istem token'ları, istem pencereye eklenmişse).
// Gövde yasakları (govde_yasak) plan boyunca uygulanmaz: planın kendi satır sonları gerekli.
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
#ifndef ORNEKLE_PLAN_SINIR
#define ORNEKLE_PLAN_SINIR 48         /* plan modu: gövdeye varmadan en fazla bu kadar token (nl nl dahil) */
#endif
#ifndef ORNEKLE_SUZGEC_DENEME
#define ORNEKLE_SUZGEC_DENEME 64      /* süzgeç açıkken bir adımda en fazla bu kadar token reddedilir */
#endif
#define ORNEKLE_YASAK_LOGIT (-1e30f)

typedef struct {
  float sicaklik;                  /* <= 0: greedy (argmax) */
  int top_k;                       /* >= 1; idx ve p en az bu kadar eleman */
  float tekrar;                    /* CTRL tekrar cezası; <= 1 kapalı */
  const int *yasak; int n_yasak;   /* her zaman yasak (gen.c -b) */
  const int *govde_yasak; int n_govde_yasak;  /* yalnızca hikâye gövdesinde yasak (gen.c -N) */
  int *idx; double *p;             /* çağıranın karalama alanı: top_k'şar eleman */
  /* İsteğe bağlı süzgeç (NULL: kapalı, çıktı eskisiyle aynı). Seçilen token'ı reddederse (0 döner) o token'ın
   * logit'i yasaklanır ve yeniden seçilir: kalan token'lar arasından örneklemeyle aynı dağılım. Tek token'la
   * yasaklanamayan çok parçalı isimler için (gen.c -Y, isim_suzgec.h). */
  int (*suzgec)(void *baglam, int tok); void *suzgec_baglam;
} OrnAyar;

typedef struct {
  int son[ORNEKLE_PENCERE];        /* tekrar penceresi (halka tampon) */
  int yaz, dolu;                   /* sıradaki yuva, dolu yuva sayısı */
  int govde;                       /* 1: hikâye gövdesi örnekleniyor, govde_yasak etkin */
  int plan_nl;                     /* plan modu: satır sonu token'ı (gen.c -S); < 0: plan modu kapalı */
  int plan_n;                      /* plan modunda gövdeden önce üretilen token sayısı */
  int onceki_nl;                   /* plan modunda son token plan_nl miydi */
  int plan_bozuk;                  /* 1: ORNEKLE_PLAN_SINIR token'da gövdeye varılamadı */
} OrnDurum;

static inline void orn_sifirla(OrnDurum *d) {
  d->yaz = 0; d->dolu = 0; d->govde = 0;
  d->plan_nl = -1; d->plan_n = 0; d->onceki_nl = 0; d->plan_bozuk = 0;
}

/* Plan modunu açar (istem "\nSorun:" ile bittikten sonra, ilk örneklemeden önce). Gövde, üretilen ilk
 * nl nl çiftinden sonraki token'la başlar. */
static inline void orn_plan_baslat(OrnDurum *d, int nl) {
  d->govde = 0; d->plan_nl = nl; d->plan_n = 0; d->onceki_nl = 0; d->plan_bozuk = 0;
}

/* Pencereyi boşaltır, gövde bayrağına dokunmaz (ör. gövde başlarken başlığı da pencereden atmak için). */
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

/* Plan modunda gövde başlamadan seçilen bir token'ı işler: ikinci ardışık nl gövdeyi başlatır (pencere
 * planın başındaki hâlinde kalır, çünkü plan token'ları ona hiç eklenmedi); ORNEKLE_PLAN_SINIR token'da
 * gövdeye varılamadıysa plan_bozuk. */
static inline void orn_plan_izle(OrnDurum *d, int tok) {
  d->plan_n++;
  if (tok == d->plan_nl && d->onceki_nl) { d->govde = 1; return; }
  d->onceki_nl = tok == d->plan_nl;
  if (d->plan_n >= ORNEKLE_PLAN_SINIR) d->plan_bozuk = 1;
}

/* Bir token seçer: tekrar cezası, yasaklar (gövdedeyse gövde yasakları da) logits'e yerinde
 * uygulanır, seçilen token pencereye eklenir (plan modunda gövde başlamadan seçilenler eklenmez). */
static inline int orn_adim(const OrnAyar *a, OrnDurum *d, float *lg, int V) {
  orn_tekrar_cezasi(lg, V, d, a->tekrar);
  orn_yasakla(lg, V, a->yasak, a->n_yasak);
  if (d->govde) orn_yasakla(lg, V, a->govde_yasak, a->n_govde_yasak);
  int tok = orn_sec(lg, V, a->sicaklik, a->top_k, a->idx, a->p);
  if (a->suzgec)  /* reddedilen token yasaklanır, yeniden seçilir; hepsi reddedilirse sonuncusu kalır */
    for (int deneme = 0; deneme < ORNEKLE_SUZGEC_DENEME && !a->suzgec(a->suzgec_baglam, tok); deneme++) {
      lg[tok] = ORNEKLE_YASAK_LOGIT;
      tok = orn_sec(lg, V, a->sicaklik, a->top_k, a->idx, a->p);
    }
  if (d->plan_nl >= 0 && !d->govde) orn_plan_izle(d, tok);
  else orn_ekle(d, tok);
  return tok;
}

#endif
