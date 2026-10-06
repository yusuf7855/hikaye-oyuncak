// İsim süzgeci: seçilmeyen figürlerin ve yan karakterlerin adlarını üretimde engeller (ornekle.h OrnAyar.suzgec).
// Figür adları tokenizer'da çok parçaya bölünür (" Olaf" = " O" + "laf", " Niloya" = " N" + "il" + "oya"); ilk
// parçayı yasaklamak O/N ile başlayan her kelimeyi yasaklar. Bu yüzden karar metin üzerinde verilir: son üretilen
// baytlara aday token eklenince yasaklı bir ad bir kelime başında tamamlanıyorsa aday reddedilir; örnekleyici
// kalan token'lardan yeniden seçer ("Orman", "Nil" serbest; "Olaf", "Niloya'ya" değil).
// Adı bir kelimenin başı olabilen adlar ("Tim" -> "Timsah", "Anna" -> "Annane", "Sara" -> "Saray") sonlarında '$' ile
// verilir: bunlar yalnızca ardından harf olmayan bir bayt geldiğinde (kelime bittiğinde) reddedilir. Böyle bir ad
// bazen yazılabilir (ad tek başına biten token'la gelirse); seçici onu ayrıca cezalandırır.
// Düz C99, malloc yok: token baytları ve adlar çağıranın belleğinde, durum sabit boyutlu.
//
// Kullanım:
//   IsimSuzgec s; isim_suzgec_kur(&s, tok_bayt, tok_uzun, V, adlar, ad_uzun, n_ad);
//   ayar.suzgec = isim_suzgec_uygun; ayar.suzgec_baglam = &s;
//   her kabul edilen token'dan sonra (istem dahil): isim_suzgec_ekle(&s, tok);
#ifndef ISIM_SUZGEC_H
#define ISIM_SUZGEC_H
#include <string.h>

#ifndef ISIM_SUZGEC_KUYRUK
#define ISIM_SUZGEC_KUYRUK 48         /* tutulan son bayt sayısı; en uzun addan uzun olmalı */
#endif

typedef struct {
  const char *const *tok_bayt; const int *tok_uzun; int V;  /* token -> UTF-8 baytları */
  const char *const *ad; const int *ad_uzun; int n_ad;        /* yasaklı adlar (UTF-8, büyük harfle) */
  char kuyruk[ISIM_SUZGEC_KUYRUK]; int n;                      /* son üretilen baytlar */
  int bas_sinir;                                               /* kuyruğun başı kelime sınırı mı (metin başı) */
} IsimSuzgec;

static inline void isim_suzgec_kur(IsimSuzgec *s, const char *const *tok_bayt, const int *tok_uzun, int V,
                                   const char *const *ad, const int *ad_uzun, int n_ad) {
  s->tok_bayt = tok_bayt; s->tok_uzun = tok_uzun; s->V = V;
  s->ad = ad; s->ad_uzun = ad_uzun; s->n_ad = n_ad; s->n = 0; s->bas_sinir = 1;
}

/* Harf ya da rakam: ASCII harf/rakam ya da UTF-8 çok baytlı bir harfin baytı (ç, ş, ğ, ı, ö, ü, İ ...). 0xE2 ile
 * başlayan üç baytlık karakterler (’ “ ” – …) noktalamadır: onların baytları harf sayılmaz. */
static inline int isim_suzgec_harf(unsigned char c) {
  return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9') || (c >= 0x80 && c != 0xE2);
}

/* b[i]'den hemen önceki karakter harf mi (i > 0). Önceki bayt bir devam baytıysa (0x80-0xBF) karakterin baş
 * baytına bakılır: "’" (E2 80 99) harf değil, "ş" (C5 9F) harf. */
static inline int isim_suzgec_once_harf(const char *b, int i) {
  int j = i - 1;
  while (j > 0 && ((unsigned char)b[j] & 0xC0) == 0x80) j--;
  return isim_suzgec_harf((unsigned char)b[j]);
}

/* Kabul edilen token'ın baytlarını kuyruğa ekler. */
static inline void isim_suzgec_ekle(IsimSuzgec *s, int tok) {
  if (tok < 0 || tok >= s->V) return;
  const char *b = s->tok_bayt[tok]; int u = s->tok_uzun[tok];
  for (int i = 0; i < u; i++) {
    if (s->n == ISIM_SUZGEC_KUYRUK) {  // en eski baytı at; baş artık metin başı değil
      memmove(s->kuyruk, s->kuyruk + 1, ISIM_SUZGEC_KUYRUK - 1); s->n--; s->bas_sinir = 0;
    }
    s->kuyruk[s->n++] = b[i];
  }
}

/* 1: tok kuyruğa eklenebilir; 0: eklenirse yeni baytlarla biten ya da onlara taşan bir kelime başında yasaklı
 * bir ad tamamlanıyor. */
static inline int isim_suzgec_uygun(void *baglam, int tok) {
  IsimSuzgec *s = (IsimSuzgec *)baglam;
  if (tok < 0 || tok >= s->V || s->n_ad == 0) return 1;
  const char *b = s->tok_bayt[tok]; int u = s->tok_uzun[tok];
  if (u == 0) return 1;
  char tam[ISIM_SUZGEC_KUYRUK + 64];
  if (u > 64) u = 64;
  memcpy(tam, s->kuyruk, s->n); memcpy(tam + s->n, b, u);
  int L = s->n + u;
  for (int a = 0; a < s->n_ad; a++) {
    int al = s->ad_uzun[a], son_sart = al > 0 && s->ad[a][al - 1] == '$';
    if (son_sart) al--;  /* '$': ad bittikten sonra harf olmayan bir bayt da gerekir */
    if (al == 0 || al + son_sart > L) continue;
    // adın bitişi yeni baytların içinde olmalı: başlangıç p, p + al > s->n
    int p0 = s->n - al + 1; if (p0 < 0) p0 = 0;
    if (son_sart) { p0 = s->n - al; if (p0 < 0) p0 = 0; }  /* bitiş baytı yeni baytların içinde olmalı */
    for (int p = p0; p + al + son_sart <= L; p++) {
      if (memcmp(tam + p, s->ad[a], al) != 0) continue;
      if (son_sart && isim_suzgec_harf((unsigned char)tam[p + al])) continue;
      int sinir = p == 0 ? s->bas_sinir : !isim_suzgec_once_harf(tam, p);
      if (sinir) return 0;
    }
  }
  return 1;
}

#endif
