// Seçici: aday hikâyeleri puanlar, kart en yüksek puanlıyı okur.
//  - secici_urun_puanla (kartın kullandığı): degerlendirme/urun_uret.py puanla()'nın birebir C kopyası (ürün
//    figürleri, data/urun_kartlari.json): sec.py kuralları + ISIM_KELIME muafiyeti + kadro_cezalari + takinti_cezasi
//    + yer + güvenlik + 2 × ortalama log-olasılık. Tablolar generated/istemler.h'de (tools/basliklar.py).
//  - secici_puanla (SECICI_ESKI 1 ile): degerlendirme/sec.py puanla(), eski hayvan kataloğu (baslangic.KAR; 0 Pamuk ..
//    11 Can); yalnız eski aday havuzlarının eşitlik testi için.
//
// Girdi: gövdenin çözülmüş UTF-8 metni (Python'a giden metin gibi baştan/sondan kırpılmış), plan metni
// ("Sorun: ...\nÇözüm: ..."; NULL ise plan kuralı yok), figür, yer (0 orman, 1 deniz, 2 ev, 3 park, 4 şato, 5 dağ;
// < 0: yer kuralı yok), bitti, ortalama lp.
// Bellek ayırmaz: bütün çalışma alanı sabit statik diziler (~24 KB, SECICI_MAKS = 2048 harf; daha uzun metin
// kırpılır). Yeniden girişli değil (tek görevden çağrılır).
//
// Python'la eşitlik: düzenli ifadeler elle, Python re'nin geri izleme sırası ve findall/finditer'in üst üste
// binmeyen tarama kuralıyla yazıldı; \b ve \w Python'daki gibi Unicode (Latin/Yunan/Kiril'de birebir, öteki
// yazılarda yaklaşık). kucuk() = sec.kucuk (I -> ı, İ -> i, sonra küçük harf). Dilimler (metin[a:b]) ayrı
// dizgeymiş gibi: sınır denetimi dilim kenarında dizge başı/sonu sayılır. Doğrulama: tools/secici_test.c +
// tools/secici_karsilastir.py (--urun: ürün aday havuzlarının bütün adayları; eski: c2ft_plan havuzları).
//
// Derleme anahtarları: SECICI_SOZLUK (1: uydurma-kelime kuralı, generated/sozluk.h ~290 KB flash; 0: kural yok),
// SECICI_URUN (1: ürün seçicisi, generated/istemler.h gerekir), SECICI_ESKI (1: eski sec.py seçicisi).
#pragma once
#include <stdint.h>
#include <string.h>

#ifndef SECICI_SOZLUK
#define SECICI_SOZLUK 1
#endif
#if SECICI_SOZLUK
#include "generated/sozluk.h"
#endif
#ifndef SECICI_ESKI
#define SECICI_ESKI 0
#endif
#ifndef SECICI_MAKS
#define SECICI_MAKS 2048        // gövde (harf); 240 token ≈ en çok ~1000 harf
#endif
#define SECICI_PLAN_MAKS 1024
#define SECICI_CUMLE (SECICI_MAKS / 2 + 2)
#define SECICI_KELIME (SECICI_MAKS / 2 + 2)

// Son puanlamanın kural kural cezaları (tanı ve test için).
enum {
  SK_AZ_ISIM, SK_KENDINE, SK_SONDA_YOK, SK_ISIM_VE_ISIM, SK_YENI_HAYVAN, SK_KONUSMACI, SK_YANLIS_ISIM,
  SK_TEKRAR_CUMLE, SK_YARIM, SK_KISA, SK_UYDURMA_KELIME, SK_TEKRAR_IFADE,
  SK_IKI_TANITIM, SK_KENDI_KENDINE, SK_BASKASI, SK_UYDURMA_AD, SK_OZELLIK, SK_KEKEME, SK_DERS, SK_PLAN,
  SK_YER, SK_GUVENLIK,
  SK_KENDINE_SESLENME, SK_KADRO_TEKRAR, SK_YAN_KENDI_KENDINE, SK_KARTTA_OLMAYAN, SK_TAKINTI, SK_GOVDE_YOK,  // ürün
  SK_N
};
static const char *const SECICI_KURAL_AD[SK_N] = {
  "az_isim", "kendine", "sonda_yok", "isim_ve_isim", "yeni_hayvan", "konusmaci", "yanlis_isim",
  "tekrar_cumle", "yarim", "kisa", "uydurma_kelime", "tekrar_ifade",
  "iki_tanitim", "kendi_kendine", "baskasi", "uydurma_ad", "ozellik", "kekeme", "ders", "plan",
  "yer", "guvenlik",
  "kendine_seslenme", "kadro_tekrar", "yan_kendi_kendine", "kartta_olmayan_ad", "takinti", "govde_yok"};
static double secici_kural[SK_N];

// ---- veri (baslangic.py / sec.py ile aynı) ----
#if SECICI_ESKI
static const char *const SC_ISIM[12] = {"Pamuk", "Tekir", "Karabaş", "Bal", "Kızıl", "Cikcik", "Tosbi", "Paytak",
                                        "Dino", "Alev", "Elif", "Can"};
static const char *const SC_TUR[12] = {"tavşan", "kedi", "köpek", "ayı", "tilki", "kuş", "kaplumbağa", "penguen",
                                       "dinozor", "ejderha", "kız", "oğlan"};
static const char *const SC_YABANCI[] = {"Lily", "Tim", "Tom", "Sara", "Sue", "Max", "Lucy", "Anna", "Jack", "Mia",
                                         "Sam", "Timmy", "Bob", "Jane", "Spot", "Fluffy", "Amy", "Zeynep", "Ali",
                                         "Ayşe", "Mehmet", "Ahmet", "Boncuk", "Mert", "Defne", "Kerem", "Emir",
                                         "Zıpzıp"};
#endif
static const char *const SC_HAYVAN[] = {"kuş", "sincap", "yengeç", "fare", "tavşan", "kedi", "köpek", "ayı", "tilki",
                                        "kurbağa", "balık", "kelebek", "karınca", "baykuş", "kaplumbağa", "penguen",
                                        "dinozor", "ejderha", "aslan", "inek", "koyun", "tavuk", "ördek", "yunus",
                                        "maymun", "zürafa", "kirpi", "salyangoz", "uğur böceği"};
static const char *const SC_IKILEME[] = {
  "paytak", "yavaş", "tek", "üzgün", "adım", "mutlu", "sık", "pırıl", "uzun", "ağır", "mışıl", "hızlı", "tekrar",
  "sakin", "için", "teker", "güle", "tıklım", "tatlı", "çekingen", "ürkek", "tir", "birer", "utana", "parıl", "seve",
  "araya", "şırıl", "beyaz", "rahat", "yudum", "dilim", "ışıl", "geri", "hüzünlü", "pır", "uğraşa", "kaşık", "derin",
  "kova", "kızgın", "usul", "sıkı", "azar", "sesli", "hayran", "köşe", "halsiz", "düşünceli", "tuhaf", "bol",
  "didik", "küskün", "sallaya", "diz", "suçlu", "tane", "güzel", "dalgın", "ara", "kat", "ağaç", "yorgun", "koşa",
  "neşeli", "sevinçli", "minik", "küçük"};
static const char *const SC_KUS[] = {"kuş", "cikcik", "baykuş", "serçe", "güvercin", "ördek", "tavuk", "martı",
                                     "leylek", "keklik", "papağan", "horoz", "civciv", "kartal", "karga", "bülbül",
                                     "kırlangıç", "penguen", "paytak"};  // + "kaz\b"
static const char *const SC_KUYRUK[] = {"köpe", "karabaş", "kedi", "tekir", "tilki", "kızıl", "sincap", "kuzu", "keçi",
                                        "alev", "ejderha", "dino", "dinozor"};
static const char *const SC_BALON[] = {"alev", "ejderha", "sabun"};
static const char *const SC_BURUN[] = {"tekir", "kedi", "karabaş", "köpe"};
static const char *const SC_DERS[] = {"anladı", "öğrendi", "fark etti", "anlamıştı", "öğrenmişti"};
// sec.DERS_KANIT: değer, sonra kanıt kelimeleri (NULL ile biter); (?:...) açılımları elle.
static const char *const SC_KANIT[] = {
  "paylaş", "paylaş", "verdi", "verme", "uzattı", "böl", "ikiye", "yarısı", "ikram", "ayırdı", "birlikte yedi",
  "birlikte oyna", "birlikte kullan", "sıra", 0,
  "kıskan", "kıskan", "imren", "kendisi de", "kendisini de", "kendisinin de", "yalnız kal", "onu da", "başkasıyla",
  "yeni arkada", "yeni bir arkada", 0,
  "dürüst", "dürüst", "doğruyu", "itiraf", "kırdı", "kırıl", "devir", "özür", "sakla", "yalan", "suç", 0,
  "sabır", "sabır", "sabırl", "bekle", "sıra", "yavaş", "acele", "tekrar dene", "denedi", 0,
  "dikkat", "dikkat", "düştü", "devir", "kırıl", "kaybol", "çarp", "takıl", "kaydı", "kayıp", 0,
  "özür", "özür", "kırdı", "kırıl", "devir", "çarp", "üzdü", "bozdu", 0,
  "cesar", "cesar", "cesur", "kork", "çekin", "utan", 0,
  "yardım", "yardım", "kurtar", "çıkar", "kaldır", "taşı", "destek", "uzan", "birlikte", "getir", "göster", "düzelt",
  "topla", 0,
  0};
static const char *const SC_YER_DENIZ[] = {"deniz", "kumsal", "sahil", "kıyı"};
static const char *const SC_EV_EK[] = {"de", "e", "in", "i", "den", "imiz", ""};
static const char *const SC_DAG_EK[] = {"ğ", "ğı", "ğa", "ğda", "ğın"};
static const char *const SC_GUVEN_ON[] = {"incit", "yaral", "kanıyor", "kanama", "acıyor", "derin su", "tehlike",
                                          "yara band", "canı acı"};

#define SC_SAY(a) ((int)(sizeof(a) / sizeof((a)[0])))

// ---- karakter sınıfları ----
static inline int sc_bosluk(uint32_t c) {  // Python str.isspace / \s
  return (c >= 9 && c <= 13) || (c >= 28 && c <= 32) || c == 0x85 || c == 0xA0 || c == 0x1680 ||
         (c >= 0x2000 && c <= 0x200A) || c == 0x2028 || c == 0x2029 || c == 0x202F || c == 0x205F || c == 0x3000;
}
static inline int sc_kelime(uint32_t c) {  // Python \w (Unicode; Latin/Yunan/Kiril birebir, ötesi yaklaşık)
  if (c < 128) return (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || c == '_';
  if (c < 0x100)
    return c == 0xAA || c == 0xB2 || c == 0xB3 || c == 0xB5 || c == 0xB9 || c == 0xBA || (c >= 0xBC && c <= 0xBE) ||
           (c >= 0xC0 && c != 0xD7 && c != 0xF7);
  if (c < 0x2B0) return 1;
  if (c < 0x370) return 0;
  if (c < 0x530) return !(c == 0x375 || c == 0x37E || c == 0x384 || c == 0x385 || c == 0x387 || c == 0x3F6 ||
                          (c >= 0x482 && c <= 0x489));
  if (c < 0x2000) return 1;
  if (c >= 0x3040 && c < 0xD800) return 1;
  return 0;
}
static inline int sc_buyuk(uint32_t c) {  // [A-ZÇĞİÖŞÜ]
  return (c >= 'A' && c <= 'Z') || c == 0xC7 || c == 0x11E || c == 0x130 || c == 0xD6 || c == 0x15E || c == 0xDC;
}
static inline int sc_kh(uint32_t c) {  // [a-zçğıöşü]
  return (c >= 'a' && c <= 'z') || c == 0xE7 || c == 0x11F || c == 0x131 || c == 0xF6 || c == 0x15F || c == 0xFC;
}
static inline int sc_sh(uint32_t c) { return sc_kh(c) || c == 0xE2 || c == 0xEE || c == 0xFB; }  // [a-zçğıöşüâîû]
static inline int sc_kesme(uint32_t c) { return c == '\'' || c == 0x2019; }                       // ['’]
static inline uint16_t sc_kucuk(uint16_t c) {  // sec.kucuk: I -> ı, İ -> i, sonra str.lower()
  if (c == 'I') return 0x131;
  if (c == 0x130) return 'i';
  if (c < 128) return (c >= 'A' && c <= 'Z') ? c + 32 : c;
  if (c >= 0xC0 && c <= 0xDE && c != 0xD7) return c + 32;
  if (c >= 0x100 && c <= 0x137 && !(c & 1)) return c + 1;
  if (c >= 0x139 && c <= 0x148 && (c & 1)) return c + 1;
  if (c >= 0x14A && c <= 0x177 && !(c & 1)) return c + 1;
  if (c == 0x178) return 0xFF;
  if (c >= 0x179 && c <= 0x17E && (c & 1)) return c + 1;
  if (c >= 0x391 && c <= 0x3A9 && c != 0x3A2) return c + 32;
  if (c >= 0x410 && c <= 0x42F) return c + 32;
  if (c >= 0x400 && c <= 0x40F) return c + 80;
  return c;
}

// UTF-8 -> UTF-16 harfleri (BMP dışı ve bozuk bayt U+FFFD; harf sayısı Python len() ile aynı). Döner: harf sayısı.
static int sc_coz(const char *s, int n, uint16_t *out, int cap) {
  const uint8_t *b = (const uint8_t *)s;
  int k = 0, i = 0;
  while (i < n && k < cap) {
    uint32_t c = b[i];
    int L = c < 0x80 ? 1 : (c & 0xE0) == 0xC0 ? 2 : (c & 0xF0) == 0xE0 ? 3 : (c & 0xF8) == 0xF0 ? 4 : 0;
    int ok = L > 0 && i + L <= n;
    for (int t = 1; ok && t < L; t++) ok = (b[i + t] & 0xC0) == 0x80;
    if (!ok) { out[k++] = 0xFFFD; i++; continue; }
    if (L == 2) c = ((c & 31) << 6) | (b[i + 1] & 63);
    else if (L == 3) c = ((c & 15) << 12) | ((b[i + 1] & 63) << 6) | (b[i + 2] & 63);
    else if (L == 4) c = 0xFFFD;
    out[k++] = (uint16_t)c;
    i += L;
  }
  return k;
}
static uint32_t sc_harf(const char **p) {  // güvenilir UTF-8 sabitinden bir harf
  const uint8_t *s = (const uint8_t *)*p;
  uint32_t c = s[0];
  if (c >= 0xE0) { c = ((c & 15) << 12) | ((s[1] & 63) << 6) | (s[2] & 63); *p += 3; }
  else if (c >= 0xC0) { c = ((c & 31) << 6) | (s[1] & 63); *p += 2; }
  else *p += 1;
  return c;
}

// ---- düzenli ifade yapı taşları (s[bas..son) bir Python dizgesi gibi) ----
static inline int sc_sinir(const uint16_t *s, int bas, int son, int i) {  // \b
  int a = i > bas && sc_kelime(s[i - 1]), b = i < son && sc_kelime(s[i]);
  return a != b;
}
static int sc_esle(const uint16_t *s, int i, int son, const char *lit) {  // s[i..] lit ile başlıyorsa uzunluğu, yoksa -1
  int b = i;
  while (*lit) {
    uint32_t c = sc_harf(&lit);
    if (i >= son || s[i] != c) return -1;
    i++;
  }
  return i - b;
}
static int sc_esit(const uint16_t *s, int i, int j, const char *lit) { return sc_esle(s, i, j, lit) == j - i; }
// \blit(\b)? eşleşme sayısı (en çok en_cok'a kadar sayar)
static int sc_say(const uint16_t *s, int bas, int son, const char *lit, int sinir_son, int en_cok) {
  int say = 0;
  for (int i = bas; i < son; i++) {
    if (!sc_sinir(s, bas, son, i)) continue;
    int L = sc_esle(s, i, son, lit);
    if (L < 0 || (sinir_son && !sc_sinir(s, bas, son, i + L))) continue;
    if (++say >= en_cok) return say;
    i += L - 1;
  }
  return say;
}
static int sc_var(const uint16_t *s, int bas, int son, const char *lit) { return sc_say(s, bas, son, lit, 0, 1) > 0; }
static int sc_icerir(const uint16_t *s, int bas, int son, const char *lit) {  // sınırsız alt dizge
  for (int i = bas; i < son; i++)
    if (sc_esle(s, i, son, lit) >= 0) return 1;
  return 0;
}
static int sc_hangi(const uint16_t *s, int bas, int son, const char *const *l, int n) {  // \b(?:a|b|...)
  for (int t = 0; t < n; t++)
    if (sc_var(s, bas, son, l[t])) return 1;
  return 0;
}
// (?:diye \w+|dedi|sordu)\s+ : sonraki konum ya da -1 (arkasından gelenin başarısı seçeneği değiştirmez)
static int sc_fiil(const uint16_t *m, int j, int n) {
  int t = -1, L;
  if ((L = sc_esle(m, j, n, "diye ")) > 0 && j + L < n && sc_kelime(m[j + L])) {
    t = j + L;
    while (t < n && sc_kelime(m[t])) t++;
    if (t >= n || !sc_bosluk(m[t])) t = -1;
  }
  if (t < 0 && (L = sc_esle(m, j, n, "dedi")) > 0 && j + L < n && sc_bosluk(m[j + L])) t = j + L;
  if (t < 0 && (L = sc_esle(m, j, n, "sordu")) > 0 && j + L < n && sc_bosluk(m[j + L])) t = j + L;
  if (t < 0) return -1;
  while (t < n && sc_bosluk(m[t])) t++;
  return t;
}
static int sc_aralik_esit(const uint16_t *s, int a, int b, int c, int d) {
  return b - a == d - c && !memcmp(s + a, s + c, (size_t)(b - a) * sizeof(uint16_t));
}
// ---- sözlük (generated/sozluk.h) ----
#if SECICI_SOZLUK
static uint16_t sc_alfabe[35];
static int sc_alfabe_hazir = 0;
static int sc_sozluk_kiyas(const uint8_t *a, int la, const uint8_t *b, int lb) {
  int n = la < lb ? la : lb;
  for (int i = 0; i < n; i++)
    if (a[i] != b[i]) return a[i] < b[i] ? -1 : 1;
  return la == lb ? 0 : la < lb ? -1 : 1;
}
static int secici_sozlukte(const uint16_t *w, int L) {
  uint8_t q[SOZLUK_UZUN + 1], b[SOZLUK_UZUN + 1];
  if (!sc_alfabe_hazir) {
    const char *p = SOZLUK_ALFABE;
    for (int i = 0; i < 35; i++) sc_alfabe[i] = (uint16_t)sc_harf(&p);
    sc_alfabe_hazir = 1;
  }
  if (L > SOZLUK_UZUN) return 0;
  for (int i = 0; i < L; i++) {
    int k = 0;
    while (k < 35 && sc_alfabe[k] != w[i]) k++;
    if (k == 35) return 0;
    q[i] = (uint8_t)(k + 1);
  }
  int lo = 0, hi = SOZLUK_N_BLOK - 1, bl = -1;
  while (lo <= hi) {  // son blok başı <= sorgu
    int orta = (lo + hi) / 2, lb = 0;
    const uint8_t *v = SOZLUK_VERI + SOZLUK_BLOK[orta] + 1;
    do { b[lb++] = *v & 0x7F; } while (!(*v++ & 0x80));
    int c = sc_sozluk_kiyas(b, lb, q, L);
    if (c == 0) return 1;
    if (c < 0) { bl = orta; lo = orta + 1; } else hi = orta - 1;
  }
  if (bl < 0) return 0;
  const uint8_t *v = SOZLUK_VERI + SOZLUK_BLOK[bl];
  for (int t = 0; t < SOZLUK_BLOK_BOY && bl * SOZLUK_BLOK_BOY + t < SOZLUK_N; t++) {
    int lb = *v++;
    do { b[lb++] = *v & 0x7F; } while (!(*v++ & 0x80));
    int c = sc_sozluk_kiyas(b, lb, q, L);
    if (c == 0) return 1;
    if (c > 0) return 0;
  }
  return 0;
}
#endif

// ---- çalışma alanı ----
static uint16_t sc_m[SECICI_MAKS], sc_k[SECICI_MAKS], sc_g[SECICI_MAKS], sc_p[SECICI_PLAN_MAKS];
static int16_t sc_cb[SECICI_CUMLE], sc_cs[SECICI_CUMLE];  // re.split(r"(?<=[.!?])\s+") parçaları [cb, cs)
static int16_t sc_wb[SECICI_KELIME], sc_wl[SECICI_KELIME], sc_wid[SECICI_KELIME];

static int sc_bol(const uint16_t *m, int n) {
  int k = 0, bas = 0, i = 1;
  while (i < n) {
    if ((m[i - 1] == '.' || m[i - 1] == '!' || m[i - 1] == '?') && sc_bosluk(m[i])) {
      int j = i;
      while (j < n && sc_bosluk(m[j])) j++;
      sc_cb[k] = (int16_t)bas; sc_cs[k] = (int16_t)i; k++;
      bas = j; i = j + 1;
    } else i++;
  }
  sc_cb[k] = (int16_t)bas; sc_cs[k] = (int16_t)n; k++;
  return k;
}
static int sc_dolu(const uint16_t *m, int a, int b) {  // s.strip() boş değil
  for (int i = a; i < b; i++)
    if (!sc_bosluk(m[i])) return 1;
  return 0;
}

// sec.plan_cezasi: re.fullmatch(r"Sorun:[ \t]*([^\n]*?)\s*\nÇözüm:[ \t]*([^\n]*?)\s*") ve iki grup dolu değilse bozuk.
static int sc_plan_bozuk(const uint16_t *p, int n) {
  int L = sc_esle(p, 0, n, "Sorun:");
  if (L < 0) return 1;
  int f = L;
  while (f < n && p[f] != '\n') f++;  // grup 1'de satır sonu olamaz: ilk \n boşluk kısmında
  if (f >= n) return 1;
  int r = f;
  while (r < n && sc_bosluk(p[r])) r++;
  if (p[r - 1] != '\n') return 1;
  int C = sc_esle(p, r, n, "Çözüm:");
  if (C < 0) return 1;
  int t = r + C, e = n;
  while (e > t && sc_bosluk(p[e - 1])) e--;
  if (e == t) return 1;  // grup 2 boş
  for (int i = t; i < e; i++)
    if (p[i] == '\n') return 1;
  return !sc_dolu(p, L, f);  // grup 1 boş
}

// sec.olay_cezalari'nın "kendi kendine" deseni, s = m[a..b) bir cümle:
// ^(?:[A-ZÇĞİÖŞÜ]\w*\s+){0,2}N\b(?!['’])(.*?)\bN['’](?:y?[ıiuü]|y?[ae]|n?[ıiuü]n|n[ıiuü]n|[dt][ae]n?|l[ae])\b
// Döner: eşleşme varsa 1 ve grup 1 [*g0, *g1).
static int sc_ek_isim(const uint16_t *m, int b, int u) {  // u: kesme işaretinden sonrası
#define SC_V(c) ((c) == 0x131 || (c) == 'i' || (c) == 'u' || (c) == 0xFC)
#define SC_AE(c) ((c) == 'a' || (c) == 'e')
#define SC_AT(i) ((i) < b ? m[i] : 0)
#define SC_BITIS(e) ((e) >= b || !sc_kelime(m[e]))
  uint16_t c0 = SC_AT(u), c1 = SC_AT(u + 1), c2 = SC_AT(u + 2);
  if (c0 == 'y' && SC_V(c1) && SC_BITIS(u + 2)) return 1;
  if (SC_V(c0) && SC_BITIS(u + 1)) return 1;
  if (c0 == 'y' && SC_AE(c1) && SC_BITIS(u + 2)) return 1;
  if (SC_AE(c0) && SC_BITIS(u + 1)) return 1;
  if (c0 == 'n' && SC_V(c1) && c2 == 'n' && SC_BITIS(u + 3)) return 1;
  if (SC_V(c0) && c1 == 'n' && SC_BITIS(u + 2)) return 1;
  if ((c0 == 'd' || c0 == 't') && SC_AE(c1) && (SC_BITIS(u + 2) || (c2 == 'n' && SC_BITIS(u + 3)))) return 1;
  if (c0 == 'l' && SC_AE(c1) && SC_BITIS(u + 2)) return 1;
  return 0;
#undef SC_V
#undef SC_AE
#undef SC_AT
#undef SC_BITIS
}
static int sc_kendi_kendine(const uint16_t *m, int a, int b, const char *isim, int *g0, int *g1) {
  for (int r = 2; r >= 0; r--) {
    int p = a, ok = 1;
    for (int t = 0; t < r && ok; t++) {
      if (!(p < b && sc_buyuk(m[p]))) { ok = 0; break; }
      p++;
      while (p < b && sc_kelime(m[p])) p++;
      if (!(p < b && sc_bosluk(m[p]))) { ok = 0; break; }
      while (p < b && sc_bosluk(m[p])) p++;
    }
    if (!ok) continue;
    int L = sc_esle(m, p, b, isim);
    if (L < 0) continue;
    int q = p + L;
    if (!sc_sinir(m, a, b, q) || (q < b && sc_kesme(m[q]))) continue;
    for (int e = q; e < b; e++) {  // tembel (.*?): '.' satır sonunu almaz
      if (e > q && m[e - 1] == '\n') break;
      if (!sc_sinir(m, a, b, e)) continue;
      int L2 = sc_esle(m, e, b, isim);
      if (L2 < 0 || e + L2 >= b || !sc_kesme(m[e + L2])) continue;
      if (sc_ek_isim(m, b, e + L2 + 1)) { *g0 = q; *g1 = e; return 1; }
    }
  }
  return 0;
}

// ---- kekeme tekrar (kucuk metinde) ----
static inline int sc_kos(const uint16_t *k, int i, int n) {  // [a-zçğıöşü]+ koşusunun sonu
  while (i < n && sc_kh(k[i])) i++;
  return i;
}
static int sc_ikileme(const uint16_t *k, int a, int b) {
  for (int t = 0; t < SC_SAY(SC_IKILEME); t++)
    if (sc_esit(k, a, b, SC_IKILEME[t])) return 1;
  return 0;
}
// k[i..) " " + k[a..b) ile başlıyor ve arkasında [a-zçğıöşü] yok mu (tekrarları say kadar)
static int sc_tekrar_sonu(const uint16_t *k, int n, int i, int a, int b, int say) {
  int L = b - a;
  for (int t = 0; t < say; t++) {
    if (i >= n || k[i] != ' ' || i + 1 + L > n || memcmp(k + i + 1, k + a, (size_t)L * 2)) return -1;
    i += 1 + L;
  }
  return (i < n && sc_kh(k[i])) ? -1 : i;
}
static int sc_kekeme(const uint16_t *k, int n) {  // 0 yok, 1 yalnız ikili, 2 üçlü ya da öbek
  int uc = 0, iki = 0, obek = 0;
  for (int i = 0; i < n;) {  // (?<![L])([L]+) \1 \1(?![L]), "paytak" hariç
    if ((i == 0 || !sc_kh(k[i - 1])) && sc_kh(k[i])) {
      int e = sc_kos(k, i, n), s = sc_tekrar_sonu(k, n, e, i, e, 2);
      if (s >= 0) { if (!sc_esit(k, i, e, "paytak")) uc = 1; i = s; continue; }
    }
    i++;
  }
  for (int i = 0; i < n;) {  // (?<![L])([L]+) \1(?![L]), IKILEME hariç
    if ((i == 0 || !sc_kh(k[i - 1])) && sc_kh(k[i])) {
      int e = sc_kos(k, i, n), s = sc_tekrar_sonu(k, n, e, i, e, 1);
      if (s >= 0) { if (!sc_ikileme(k, i, e)) iki = 1; i = s; continue; }
    }
    i++;
  }
  for (int i = 0; i < n;) {  // (?<![L])([L]+(?: [L]+){1,3})(?:,| ve)? \1(?![L]), ilk kelime IKILEME değilse
    int s = -1, e0 = 0;
    if ((i == 0 || !sc_kh(k[i - 1])) && sc_kh(k[i])) {
      int son[4], r = 0;
      son[0] = e0 = sc_kos(k, i, n);
      while (r < 3 && son[r] + 1 < n && k[son[r]] == ' ' && sc_kh(k[son[r] + 1])) { son[r + 1] = sc_kos(k, son[r] + 1, n); r++; }
      for (; r >= 1 && s < 0; r--) {
        int e = son[r];
        if (e < n && k[e] == ',') s = sc_tekrar_sonu(k, n, e + 1, i, e, 1);
        if (s < 0 && sc_esle(k, e, n, " ve") > 0) s = sc_tekrar_sonu(k, n, e + 3, i, e, 1);
        if (s < 0) s = sc_tekrar_sonu(k, n, e, i, e, 1);
      }
    }
    if (s >= 0) { if (!sc_ikileme(k, i, e0)) obek = 1; i = s; } else i++;
  }
  return (uc || obek) ? 2 : iki ? 1 : 0;
}

// ---- yer kelimeleri (sec.YER_KELIME) ----
static int sc_yer_say(const uint16_t *k, int bas, int son, int yer) {
  static const char *const tek[6] = {"orman", 0, 0, "park", "şato", 0};
  if (tek[yer]) return sc_say(k, bas, son, tek[yer], 0, 1 << 30);
  int say = 0;
  for (int i = bas; i < son; i++) {
    if (!sc_sinir(k, bas, son, i)) continue;
    int ok = 0;
    if (yer == 1) {
      for (int t = 0; t < 4 && !ok; t++) ok = sc_esle(k, i, son, SC_YER_DENIZ[t]) > 0;
    } else if (yer == 2) {
      if (sc_esle(k, i, son, "ev") > 0)
        for (int t = 0; t < SC_SAY(SC_EV_EK) && !ok; t++) {
          int L = sc_esle(k, i + 2, son, SC_EV_EK[t]);
          ok = L >= 0 && sc_sinir(k, bas, son, i + 2 + L);
        }
    } else if (sc_esle(k, i, son, "da") > 0) {
      for (int t = 0; t < 5 && !ok; t++) {
        int L = sc_esle(k, i + 2, son, SC_DAG_EK[t]);
        ok = L >= 0 && sc_sinir(k, bas, son, i + 2 + L);
      }
    }
    say += ok;
  }
  return say;
}

// ---- güvenlik (sec.GUVENLIK, kucuk metinde) ----
static int sc_guvenlik(const uint16_t *k, int n) {
  for (int i = 0; i < n; i++) {
    if (i > 0 && sc_kh(k[i - 1])) continue;
    for (int t = 0; t < SC_SAY(SC_GUVEN_ON); t++)
      if (sc_esle(k, i, n, SC_GUVEN_ON[t]) > 0) return 1;
    if (sc_esle(k, i, n, "boğul") > 0 && !(i >= 13 && sc_esle(k, i - 13, n, "gözyaşlarına ") > 0)) return 1;
    if (sc_esle(k, i, n, "kan") > 0) {
      if (!(i + 3 < n && sc_kh(k[i + 3]))) return 1;
      if (sc_esle(k, i + 3, n, "lar") > 0 && !(i + 6 < n && sc_kh(k[i + 6]))) return 1;
    }
    if (sc_esle(k, i, n, "diz") > 0) {
      int j = i + 3;
      while (j < n && sc_kelime(k[j])) j++;
      if (sc_esle(k, j, n, " kana") > 0) return 1;
    }
    if (sc_esle(k, i, n, "yara") > 0) {
      static const char *const ek[4] = {"", "sı", "lar", "ları"};
      for (int t = 0; t < 4; t++) {
        int L = sc_esle(k, i + 4, n, ek[t]);
        if (L >= 0 && !(i + 4 + L < n && sc_kh(k[i + 4 + L]))) return 1;
      }
    }
  }
  return 0;
}

// ---- sec.olay_cezalari parçaları (eski ve ürün seçicisi ortak; m metin, k kucuk(m), cümleler sc_cb/sc_cs [0, ncd)) ----
static int sc_bol_dolu(const uint16_t *m, int n) {  // boş olmayan parçalar (kırpılmamış), sc_cb/sc_cs başına
  int nc = sc_bol(m, n), ncd = 0;
  for (int i = 0; i < nc; i++)
    if (sc_dolu(m, sc_cb[i], sc_cs[i])) { sc_cb[ncd] = sc_cb[i]; sc_cs[ncd] = sc_cs[i]; ncd++; }
  return ncd;
}
static int sc_iki_tanitim(const uint16_t *m, int n, const char *N) {  // len(re.findall(rf"\b{N} adında")) > 1
  int say = 0;
  for (int i = 0; i < n; i++) {
    if (!sc_sinir(m, 0, n, i)) continue;
    int L = sc_esle(m, i, n, N);
    if (L > 0 && sc_esle(m, i + L, n, " adında") > 0) { say++; i += L; }
  }
  return say > 1;
}
static int sc_kendi_kendine_var(const uint16_t *m, const uint16_t *k, int ncd, const char *N) {
  for (int s = 0; s < ncd; s++) {
    int g0, g1;
    if (!sc_kendi_kendine(m, sc_cb[s], sc_cs[s], N, &g0, &g1)) continue;
    int engel = 0;
    for (int i = g0; i < g1 && !engel; i++)
      engel = m[i] == '"' || m[i] == 0x201C || m[i] == 0x201D || m[i] == ':' ||
              (sc_buyuk(m[i]) && sc_sinir(m, g0, g1, i));
    for (int h = 0; h < SC_SAY(SC_HAYVAN) && !engel; h++) engel = sc_var(k, g0, g1, SC_HAYVAN[h]);
    if (!engel) return 1;
  }
  return 0;
}
// \b(?:[Bb]en de|[Bb]enim adım|[Aa]dım) N\b[^"”]*["”]\s*(?:diye \w+|dedi|sordu)\s+(?!N\b)[a-zçğıöşü]
static int sc_baskasi(const uint16_t *m, int n, const char *N) {
  static const char *const giris[6] = {"Ben de", "ben de", "Benim adım", "benim adım", "Adım", "adım"};
  for (int i = 0; i < n; i++) {
    if (!sc_sinir(m, 0, n, i)) continue;
    for (int t = 0; t < 6; t++) {
      int L = sc_esle(m, i, n, giris[t]);
      if (L < 0) continue;
      int j = i + L;
      if (!(j < n && m[j] == ' ')) continue;
      int L2 = sc_esle(m, ++j, n, N);
      if (L2 < 0 || !sc_sinir(m, 0, n, j + L2)) continue;
      j += L2;
      while (j < n && m[j] != '"' && m[j] != 0x201D) j++;
      if (j >= n) continue;
      j++;
      while (j < n && sc_bosluk(m[j])) j++;
      j = sc_fiil(m, j, n);
      if (j < 0 || j >= n) continue;
      int L3 = sc_esle(m, j, n, N);
      if (L3 > 0 && sc_sinir(m, 0, n, j + L3)) continue;
      if (sc_kh(m[j])) return 1;
    }
  }
  return 0;
}
static int sc_listede(const uint16_t *m, int a, int b, const char *const *l, int n) {  // m[a..b) listede mi
  for (int t = 0; t < n; t++)
    if (sc_esit(m, a, b, l[t])) return 1;
  return 0;
}
// uydurma karakter adı: kesme işaretli büyük harfli kelime TUM_ISIM'de değilse (tum: sec.TUM_ISIM)
static int sc_uydurma_ad(const uint16_t *m, int n, const char *const *tum, int n_tum) {
  for (int i = 1; i < n; i++) {  // (?<![.!?"“] )(?<!^)\b([Büyük][küçük]+)['’]
    if (i >= 2 && m[i - 1] == ' ' &&
        (m[i - 2] == '.' || m[i - 2] == '!' || m[i - 2] == '?' || m[i - 2] == '"' || m[i - 2] == 0x201C)) continue;
    if (sc_kelime(m[i - 1]) || !sc_buyuk(m[i]) || !(i + 1 < n && sc_kh(m[i + 1]))) continue;
    int e = sc_kos(m, i + 1, n);
    if (e < n && sc_kesme(m[e]) && !sc_listede(m, i, e, tum, n_tum)) return 1;
  }
  for (int i = 0; i < n; i++) {  // (?:^|[.!?]\s+)([Büyük][küçük]+)['’]
    int p = -1;
    if (i == 0 && sc_buyuk(m[0])) p = 0;
    else if ((m[i] == '.' || m[i] == '!' || m[i] == '?') && i + 1 < n && sc_bosluk(m[i + 1])) {
      p = i + 1;
      while (p < n && sc_bosluk(m[p])) p++;
    }
    if (p < 0 || p + 1 >= n || !sc_buyuk(m[p]) || !sc_kh(m[p + 1])) continue;
    int e = sc_kos(m, p + 1, n);
    if (e < n && sc_kesme(m[e]) && !sc_listede(m, p, e, tum, n_tum)) return 1;
  }
  return 0;
}
static double sc_ozellik(const uint16_t *k, int n) {  // özellik karışması (sec.OZELLIK)
  double c = 0;
  if (sc_var(k, 0, n, "gaga") && !sc_hangi(k, 0, n, SC_KUS, SC_SAY(SC_KUS)) && !sc_say(k, 0, n, "kaz", 1, 1)) c += 2;
  if (sc_icerir(k, 0, n, "kuyruğunu salla") && !sc_hangi(k, 0, n, SC_KUYRUK, SC_SAY(SC_KUYRUK))) c += 2;
  if (sc_icerir(k, 0, n, "baloncuk") && !sc_hangi(k, 0, n, SC_BALON, SC_SAY(SC_BALON))) c += 2;
  if (sc_icerir(k, 0, n, "burnunu sok") && !sc_hangi(k, 0, n, SC_BURUN, SC_SAY(SC_BURUN))) c += 2;
  if ((sc_icerir(k, 0, n, "kabuğunu çıkar") || sc_icerir(k, 0, n, "kabuğunu bırak") ||
       sc_icerir(k, 0, n, "kabuğunu at")) && n > 0)  // izin deseni "$^" yalnız boş metinde eşleşir
    c += 2;
  return c;
}
static int sc_ders(const uint16_t *k, int ncd) {  // ders olaydan kopuk: son 3 cümlede ders, gövdede o değerin olayı yok
  int bas = ncd - 3 > 3 ? ncd - 3 : 3;
  for (int i = bas; i < ncd; i++) {
    int a = sc_cb[i], b = sc_cs[i], ders = 0;
    for (int t = 0; t < SC_SAY(SC_DERS) && !ders; t++) ders = sc_icerir(k, a, b, SC_DERS[t]);
    if (!ders) continue;
    int gn = 0;
    for (int s = 0; s < i; s++) {
      if (s) sc_g[gn++] = ' ';
      for (int t = sc_cb[s]; t < sc_cs[s] && gn < SECICI_MAKS; t++) sc_g[gn++] = k[t];
    }
    int yok = 0;
    for (const char *const *v = SC_KANIT; *v && !yok; v++) {  // değer, kanıtlar..., 0
      int ic = sc_icerir(k, a, b, *v++), kanit = 0;
      for (; *v; v++)
        if (ic && !kanit) kanit = sc_icerir(sc_g, 0, gn, *v);
      yok = ic && !kanit;
    }
    if (yok) return 1;
  }
  return 0;
}
// [a-zçğıöşüâîû]+ kelimeleri (k = kucuk metin) sc_wb/sc_wl'ye; döner: kelime sayısı
static int sc_kelimeler(const uint16_t *k, int n) {
  int nw = 0;
  for (int i = 0; i < n;) {
    if (sc_sh(k[i])) {
      int e = i;
      while (e < n && sc_sh(k[e])) e++;
      sc_wb[nw] = (int16_t)i; sc_wl[nw] = (int16_t)(e - i); nw++;
      i = e;
    } else i++;
  }
  return nw;
}
static int sc_tekrar_cumle(const uint16_t *m, int nc) {  // kırpılmış parçalar arasında aynısı var mı
  for (int i = 0; i < nc; i++) {
    int a = sc_cb[i], b = sc_cs[i];
    while (a < b && sc_bosluk(m[a])) a++;
    while (b > a && sc_bosluk(m[b - 1])) b--;
    if (a == b) continue;
    for (int j = 0; j < i; j++) {
      int a2 = sc_cb[j], b2 = sc_cs[j];
      while (a2 < b2 && sc_bosluk(m[a2])) a2++;
      while (b2 > a2 && sc_bosluk(m[b2 - 1])) b2--;
      if (a2 < b2 && sc_aralik_esit(m, a, b, a2, b2)) return 1;
    }
  }
  return 0;
}
static int sc_tekrar_uclu(const uint16_t *k, int nw) {  // len(uclu) - len(set(uclu))
  for (int w = 0; w < nw; w++) {
    int id = w;
    for (int v = 0; v < w; v++)
      if (sc_wid[v] == v && sc_aralik_esit(k, sc_wb[v], sc_wb[v] + sc_wl[v], sc_wb[w], sc_wb[w] + sc_wl[w])) { id = v; break; }
    sc_wid[w] = (int16_t)id;
  }
  int tekrar = 0;
  for (int i = 0; i + 2 < nw; i++)
    for (int j = 0; j < i; j++)
      if (sc_wid[j] == sc_wid[i] && sc_wid[j + 1] == sc_wid[i + 1] && sc_wid[j + 2] == sc_wid[i + 2]) { tekrar++; break; }
  return tekrar;
}
static void sc_son_kurallar(const uint16_t *m, int n, int bitti, double *c) {  // yarım son, çok kısa
  int e = n;
  while (e > 0 && sc_bosluk(m[e - 1])) e--;
  int iyi = e > 0 && (m[e - 1] == '.' || m[e - 1] == '!' || m[e - 1] == '"' || m[e - 1] == 0x201D);
  if (!iyi || !bitti) c[SK_YARIM] = 2;
  int kelime = 0;
  for (int i = 0; i < n; i++) kelime += !sc_bosluk(m[i]) && (i == 0 || sc_bosluk(m[i - 1]));
  if (kelime < 50) c[SK_KISA] = 2;
}
static int sc_yer_kaymasi(const uint16_t *k, int n, int yer) {  // sec.yer_cezasi
  int kendi = sc_yer_say(k, 0, n, yer), baska = 0;
  for (int y = 0; y < 6; y++) {
    if (y == yer) continue;
    int s = sc_yer_say(k, n / 2, n, y);
    if (s > baska) baska = s;
  }
  return kendi == 0 || baska > kendi;
}

#if SECICI_ESKI
// sec.puanla(metin, kimlikler, ort_logp=lp, yer=yer, bitti=bitti, guvenlik=guvenlik, plan=plan): eski hayvan
// kataloğu (baslangic.KAR). Kart artık ürün seçicisini (secici_urun_puanla) kullanır; bu yol yalnız eski havuzların
// eşitlik testi için (tools/secici_karsilastir.py, -DSECICI_ESKI=1).
static double secici_puanla(const char *metin, int metin_n, const char *plan, int plan_n, const int *fig, int n_fig,
                            int yer, int bitti, double lp, int guvenlik) {
  uint16_t *m = sc_m, *k = sc_k;
  int n = sc_coz(metin, metin_n, m, SECICI_MAKS);
  for (int i = 0; i < n; i++) k[i] = sc_kucuk(m[i]);
  double *c = secici_kural;
  for (int i = 0; i < SK_N; i++) c[i] = 0;

  // --- cezalar ---
  int son40 = (int)(n * 0.6);
  for (int f = 0; f < n_fig; f++) {
    const char *N = SC_ISIM[fig[f]];
    if (sc_say(m, 0, n, N, 1, 2) < 2) c[SK_AZ_ISIM] += 3;
    int kendine = 0, ve = 0;
    for (int i = 0; i < n && !(kendine && ve); i++) {  // \bN\b,?\s+N['’]  ve  \bN\b\s+ve\s+N\b
      if (!sc_sinir(m, 0, n, i)) continue;
      int L = sc_esle(m, i, n, N);
      if (L < 0 || !sc_sinir(m, 0, n, i + L)) continue;
      int j = i + L;
      if (j < n && m[j] == ',') j++;
      if (j < n && sc_bosluk(m[j])) {
        while (j < n && sc_bosluk(m[j])) j++;
        int L2 = sc_esle(m, j, n, N);
        if (L2 > 0 && j + L2 < n && sc_kesme(m[j + L2])) kendine = 1;
      }
      j = i + L;
      if (j < n && sc_bosluk(m[j])) {
        while (j < n && sc_bosluk(m[j])) j++;
        if (sc_esle(m, j, n, "ve") > 0 && j + 2 < n && sc_bosluk(m[j + 2])) {
          j += 2;
          while (j < n && sc_bosluk(m[j])) j++;
          int L2 = sc_esle(m, j, n, N);
          if (L2 > 0 && sc_sinir(m, 0, n, j + L2)) ve = 1;
        }
      }
    }
    if (kendine) c[SK_KENDINE] += 2;
    if (!sc_say(m, son40, n, N, 1, 1)) c[SK_SONDA_YOK] += 3;
    if (ve) c[SK_ISIM_VE_ISIM] += 3;
  }
  int yari = n / 2, yeni = 0;
  for (int h = 0; h < SC_SAY(SC_HAYVAN); h++) {
    if (!sc_var(k, yari, n, SC_HAYVAN[h]) || sc_var(k, 0, yari, SC_HAYVAN[h])) continue;
    int tur = 0;
    for (int f = 0; f < n_fig; f++) tur |= !strcmp(SC_TUR[fig[f]], SC_HAYVAN[h]);
    yeni += !tur;
  }
  c[SK_YENI_HAYVAN] = 1.5 * yeni;
  {  // konuşmacı: ["”]\s*(?:diye \w+|dedi|sordu)\s+([A-ZÇĞİÖŞÜa-zçğıöşü]+), art arda aynı
    int oa = -1, ob = -1;
    for (int i = 0; i < n;) {
      if (m[i] == '"' || m[i] == 0x201D) {
        int j = i + 1;
        while (j < n && sc_bosluk(m[j])) j++;
        j = sc_fiil(m, j, n);
        if (j >= 0 && j < n && (sc_buyuk(m[j]) || sc_kh(m[j]))) {
          int e = j;
          while (e < n && (sc_buyuk(m[e]) || sc_kh(m[e]))) e++;
          if (oa >= 0 && sc_aralik_esit(m, oa, ob, j, e)) c[SK_KONUSMACI] = 1;
          oa = j; ob = e; i = e;
          continue;
        }
      }
      i++;
    }
  }
  {  // yanlış isim: BUYUK.findall ∩ (başka figür adları ∪ YABANCI)
    int yanlis = 0;
    for (int i = 0; i < n && !yanlis;) {
      if (sc_buyuk(m[i]) && i + 1 < n && sc_kh(m[i + 1])) {
        int e = sc_kos(m, i + 1, n);
        for (int f = 0; f < 12 && !yanlis; f++) {
          int secili = 0;
          for (int g = 0; g < n_fig; g++) secili |= fig[g] == f;
          if (!secili && sc_esit(m, i, e, SC_ISIM[f])) yanlis = 1;
        }
        for (int t = 0; t < SC_SAY(SC_YABANCI) && !yanlis; t++) yanlis = sc_esit(m, i, e, SC_YABANCI[t]);
        i = e;
      } else i++;
    }
    if (yanlis) c[SK_YANLIS_ISIM] = 2;
  }
  int nc = sc_bol(m, n);
  if (sc_tekrar_cumle(m, nc)) c[SK_TEKRAR_CUMLE] = 1;
  sc_son_kurallar(m, n, bitti, c);
  int nw = sc_kelimeler(k, n);
#if SECICI_SOZLUK
  {
    int bilinmeyen = 0;
    for (int w = 0; w < nw; w++) bilinmeyen += !secici_sozlukte(k + sc_wb[w], sc_wl[w]);
    c[SK_UYDURMA_KELIME] = 1.5 * bilinmeyen;
  }
#endif
  int tekrar = sc_tekrar_uclu(k, nw);
  if (tekrar > 2) c[SK_TEKRAR_IFADE] = 0.5 * (tekrar - 2);

  // --- olay_cezalari ---
  int ncd = sc_bol_dolu(m, n);
  for (int f = 0; f < n_fig; f++) {
    const char *N = SC_ISIM[fig[f]];
    if (sc_iki_tanitim(m, n, N)) c[SK_IKI_TANITIM] += 3;
    if (sc_kendi_kendine_var(m, k, ncd, N)) c[SK_KENDI_KENDINE] += 2;
    if (sc_baskasi(m, n, N)) c[SK_BASKASI] += 2;
  }
  if (sc_uydurma_ad(m, n, SC_ISIM, 12)) c[SK_UYDURMA_AD] = 2;
  c[SK_OZELLIK] = sc_ozellik(k, n);
  c[SK_KEKEME] = sc_kekeme(k, n);
  if (sc_ders(k, ncd)) c[SK_DERS] = 1.5;
  if (plan) {
    int pn = sc_coz(plan, plan_n, sc_p, SECICI_PLAN_MAKS);
    if (sc_plan_bozuk(sc_p, pn)) c[SK_PLAN] = 2;
  }
  if (yer >= 0 && yer < 6 && sc_yer_kaymasi(k, n, yer)) c[SK_YER] = 1.5;
  if (guvenlik && sc_guvenlik(k, n)) c[SK_GUVENLIK] = 4;
  double ceza = 0;
  for (int i = 0; i < SK_N; i++) ceza += c[i];
  return -ceza + 2 * lp;
}
#endif  // SECICI_ESKI

// ======================= ürün seçicisi: degerlendirme/urun_uret.py puanla() =======================
// Figür f = generated/istemler.h sırası (urun_uret.FIGURLER), yer = genel yer (0 orman, 1 deniz, 2 ev, 3 park,
// 4 şato, 5 dağ; urun_uret.YER_ANAHTAR ile sec.YER_KELIME anahtarı). sec.py kurallarından farkı (urun_uret.puanla):
// figür adları ürün kartlarından, 'kendine gönderme', 'sonradan beliren karakter' ve 'aynı konuşmacı' kuralları yok,
// "X ve|ile X", yanlış isim = kadro dışı ad (önünde harf, ardında küçük harf yok), uydurma kelimede ürün adlarının
// kelimeleri (ISIM_KELIME) muaf, uydurma karakter adında TUM_ISIM ürün adları; ek olarak kadro_cezalari
// (kendine seslenme, 'X X', yanların kendi kendine, kartta olmayan ad) ve takinti_cezasi. Güvenlik her zaman açık.
#ifndef SECICI_URUN
#define SECICI_URUN 1
#endif
#if SECICI_URUN
#include "generated/istemler.h"

// ad '$' ile biterse (isim süzgeci biçimi) '$' sayılmaz: s[i..] ile eşleşen harf sayısı ya da -1
static int sc_esle_ad(const uint16_t *s, int i, int son, const char *lit) {
  int b = i;
  while (*lit && *lit != '$') {
    uint32_t c = sc_harf(&lit);
    if (i >= son || s[i] != c) return -1;
    i++;
  }
  return i - b;
}
static int sc_aralik_var(const uint16_t *s, int bas, int son, int a, int b) {  // \b s[a..b) \b, s[bas..son) içinde
  int L = b - a;
  for (int i = bas; i + L <= son; i++)
    if (sc_sinir(s, bas, son, i) && !memcmp(s + i, s + a, (size_t)L * 2) && sc_sinir(s, bas, son, i + L)) return 1;
  return 0;
}
// \bN\b\s+(?:ve|ile)\s+N\b (bir_bosluk 0) ya da kadro_cezalari'nın \bN\s+N\b|\bN\b,?\s+(?:ve|ile)\s+N\b (1)
static int sc_ad_ad(const uint16_t *m, int n, const char *N, int kadro) {
  for (int i = 0; i < n; i++) {
    if (!sc_sinir(m, 0, n, i)) continue;
    int L = sc_esle(m, i, n, N);
    if (L < 0) continue;
    int j = i + L;
    if (kadro && j < n && sc_bosluk(m[j])) {  // \bN\s+N\b
      int t = j;
      while (t < n && sc_bosluk(m[t])) t++;
      int L2 = sc_esle(m, t, n, N);
      if (L2 > 0 && sc_sinir(m, 0, n, t + L2)) return 1;
    }
    if (!sc_sinir(m, 0, n, j)) continue;
    if (kadro && j < n && m[j] == ',') j++;
    if (!(j < n && sc_bosluk(m[j]))) continue;
    while (j < n && sc_bosluk(m[j])) j++;
    int V = sc_esle(m, j, n, "ve");
    if (!(V > 0 && j + V < n && sc_bosluk(m[j + V]))) V = sc_esle(m, j, n, "ile");
    if (!(V > 0 && j + V < n && sc_bosluk(m[j + V]))) continue;
    j += V;
    while (j < n && sc_bosluk(m[j])) j++;
    int L2 = sc_esle(m, j, n, N);
    if (L2 > 0 && sc_sinir(m, 0, n, j + L2)) return 1;
  }
  return 0;
}
static inline int sc_kelime_tire(uint32_t c) { return sc_kelime(c) || c == '-'; }  // [\w\-]
// urun_uret.KONUSMA: ["“]([^"“”]+)["”]\s*(?:diye\s+)?(?:dedi|...|söyledi)\s+([Büyük][\w\-]+(?:\s[Büyük][\w\-]+)?)
// finditer: konuşan kadrodaysa ve sözde kendi adı geçiyorsa 1.
static int sc_kendine_seslenme(const uint16_t *m, int n, int f) {
  static const char *const fiil[8] = {"dedi", "sordu", "seslendi", "bağırdı", "fısıldadı", "cevap verdi",
                                      "karşılık verdi", "söyledi"};
  for (int i = 0; i < n;) {
    int son = -1, p = 0, q = 0, j = i + 1;
    if (m[i] == '"' || m[i] == 0x201C) {
      while (j < n && m[j] != '"' && m[j] != 0x201C && m[j] != 0x201D) j++;
      if (j > i + 1 && j < n && m[j] != 0x201C) {
        int t = j + 1;
        while (t < n && sc_bosluk(m[t])) t++;
        int D = sc_esle(m, t, n, "diye");
        if (D > 0 && t + D < n && sc_bosluk(m[t + D])) {
          t += D;
          while (t < n && sc_bosluk(m[t])) t++;
        }
        int F = -1;
        for (int v = 0; v < 8 && F < 0; v++) {
          F = sc_esle(m, t, n, fiil[v]);
          if (F > 0 && !(t + F < n && sc_bosluk(m[t + F]))) F = -1;
        }
        if (F > 0) {
          p = t + F;
          while (p < n && sc_bosluk(m[p])) p++;
          if (p + 1 < n && sc_buyuk(m[p]) && sc_kelime_tire(m[p + 1])) {
            q = p + 1;
            while (q < n && sc_kelime_tire(m[q])) q++;
            if (q + 2 < n && sc_bosluk(m[q]) && sc_buyuk(m[q + 1]) && sc_kelime_tire(m[q + 2])) {
              q += 2;
              while (q < n && sc_kelime_tire(m[q])) q++;
            }
            son = q;
          }
        }
      }
    }
    if (son < 0) { i++; continue; }
    for (int t = URUN_KADRO_OFF[f]; t < URUN_KADRO_OFF[f + 1]; t++)
      if (sc_esit(m, p, q, URUN_KADRO[t])) {
        if (sc_aralik_var(m, i + 1, j, p, q)) return 1;
        break;
      }
    i = son;
  }
  return 0;
}
// urun_uret.sozlukte_kok: w ya da en az 4 harfli bir ön eki sözlükte (w = kucuk)
static int sc_sozlukte_kok(const uint16_t *w, int L) {
#if SECICI_SOZLUK
  if (secici_sozlukte(w, L)) return 1;
  for (int i = L - 1; i > 3; i--)
    if (secici_sozlukte(w, i)) return 1;
#else
  (void)w; (void)L;
#endif
  return 0;
}
// kadro_cezalari'nın "kartta olmayan ad" kuralı: farklı bilinmeyen ad sayısı (en çok 3'e kadar sayılır)
static int sc_kartta_olmayan(const uint16_t *m, const uint16_t *k, int n, int f) {
  int ub[3], ul[3], u = 0;
  for (int i = 0; i < n && u < 3;) {  // (?<![\w])([Büyük][a-zçğıöşüâîû]+(?:-[A-Z][a-z]+)?)
    if (!((i == 0 || !sc_kelime(m[i - 1])) && sc_buyuk(m[i]) && i + 1 < n && sc_sh(m[i + 1]))) { i++; continue; }
    int e = i + 1;
    while (e < n && sc_sh(m[e])) e++;
    if (e + 2 < n && m[e] == '-' && m[e + 1] >= 'A' && m[e + 1] <= 'Z' && m[e + 2] >= 'a' && m[e + 2] <= 'z') {
      e += 3;
      while (e < n && m[e] >= 'a' && m[e] <= 'z') e++;
    }
    int b = i;
    i = e;
    int izinli = 0;
    for (int t = URUN_IZINLI_OFF[f]; t < URUN_IZINLI_OFF[f + 1] && !izinli; t++) {
      if (sc_esit(m, b, e, URUN_IZINLI[t])) izinli = 1;
      else if (sc_esle(m, b, e, URUN_IZINLI[t]) > 2) izinli = 1;  // w.startswith(i), len(i) > 2
    }
    if (izinli || sc_listede(m, b, e, URUN_TUM_AD, URUN_TUM_AD_N)) continue;
    int o = b - 1;
    while (o >= 0 && sc_bosluk(m[o])) o--;
    int cumle_basi = o < 0 || m[o] == '.' || m[o] == '!' || m[o] == '?' || m[o] == '"' || m[o] == 0x201C ||
                     m[o] == 0x201D || m[o] == ':';
    int ekli = e < n && sc_kesme(m[e]);
    if (cumle_basi && !ekli && SECICI_SOZLUK && sc_sozlukte_kok(k + b, e - b)) continue;
    int yeni = 1;
    for (int t = 0; t < u && yeni; t++) yeni = !sc_aralik_esit(m, ub[t], ub[t] + ul[t], b, e);
    if (yeni) { ub[u] = b; ul[u] = e - b; u++; }
  }
  return u;
}
// urun_uret.takinti_cezasi: 4+ harfli kelimelerin ilk 5 harfi 9+ kez (ad kelimeleri ve TAKINTI_HARIC hariç);
// döner: sum(n - 8). Kelimeler sc_wb/sc_wl'de (k üzerinde).
static int sc_takinti(const uint16_t *k, int nw, int f) {
  int top = 0;
  for (int w = 0; w < nw; w++) {
    sc_wid[w] = -1;
    if (sc_wl[w] < 4) continue;
    int a = sc_wb[w], L = sc_wl[w] < 5 ? sc_wl[w] : 5;
    if (sc_listede(k, a, a + L, URUN_TAKINTI_AD + URUN_TAKINTI_AD_OFF[f],
                   URUN_TAKINTI_AD_OFF[f + 1] - URUN_TAKINTI_AD_OFF[f]) ||
        sc_listede(k, a, a + L, URUN_TAKINTI_HARIC, URUN_TAKINTI_HARIC_N)) continue;
    int id = w;
    for (int v = 0; v < w; v++) {
      if (sc_wid[v] != v) continue;
      int Lv = sc_wl[v] < 5 ? sc_wl[v] : 5;
      if (sc_aralik_esit(k, sc_wb[v], sc_wb[v] + Lv, a, a + L)) { id = v; break; }
    }
    sc_wid[w] = (int16_t)id;
  }
  for (int w = 0; w < nw; w++) {
    if (sc_wid[w] != w) continue;
    int say = 0;
    for (int v = w; v < nw; v++) say += sc_wid[v] == w;
    if (say >= 9) top += say - 8;
  }
  return top;
}

// urun_uret.puanla(a, kimlik, yer): metin = a["metin"] (çözülmüş ve kırpılmış gövde), plan = a["plan"]
// ("Sorun: ...\nÇözüm: ..."; NULL: plan kuralı yok), f figür, yer genel yer (< 0: yer kuralı yok), lp a["lp"].
// Gövde boşsa -99 (plan bozuk adayı çağıran eler: puan -99).
static double secici_urun_puanla(const char *metin, int metin_n, const char *plan, int plan_n, int f, int yer,
                                 int bitti, double lp) {
  uint16_t *m = sc_m, *k = sc_k;
  double *c = secici_kural;
  for (int i = 0; i < SK_N; i++) c[i] = 0;
  if (metin_n <= 0) { c[SK_GOVDE_YOK] = 99; return -99.0; }
  int n = sc_coz(metin, metin_n, m, SECICI_MAKS);
  for (int i = 0; i < n; i++) k[i] = sc_kucuk(m[i]);
  const char *ad = FIGUR_AD[f];

  if (sc_say(m, 0, n, ad, 1, 2) < 2) c[SK_AZ_ISIM] = 3;
  if (!sc_say(m, (int)(n * 0.6), n, ad, 1, 1)) c[SK_SONDA_YOK] = 3;
  if (sc_ad_ad(m, n, ad, 0)) c[SK_ISIM_VE_ISIM] = 3;
  {  // yanlis_isimler: kadro dışı ad, (?<![\w])ad(?![a-zçğıöşüâîû])
    int yanlis = 0;
    for (int t = SUZGEC_AD_OFF[f]; t < SUZGEC_AD_OFF[f + 1] && !yanlis; t++)
      for (int i = 0; i < n && !yanlis; i++) {
        if (i > 0 && sc_kelime(m[i - 1])) continue;
        int L = sc_esle_ad(m, i, n, SUZGEC_AD[t]);
        if (L > 0 && !(i + L < n && sc_sh(m[i + L]))) yanlis = 1;
      }
    if (yanlis) c[SK_YANLIS_ISIM] = 2;
  }
  int nc = sc_bol(m, n);
  if (sc_tekrar_cumle(m, nc)) c[SK_TEKRAR_CUMLE] = 1;
  sc_son_kurallar(m, n, bitti, c);
  int nw = sc_kelimeler(k, n);
#if SECICI_SOZLUK
  {
    int bilinmeyen = 0;
    for (int w = 0; w < nw; w++)
      bilinmeyen += !secici_sozlukte(k + sc_wb[w], sc_wl[w]) &&
                    !sc_listede(k, sc_wb[w], sc_wb[w] + sc_wl[w], URUN_ISIM_KELIME, URUN_ISIM_KELIME_N);
    c[SK_UYDURMA_KELIME] = 1.5 * bilinmeyen;
  }
#endif
  int tekrar = sc_tekrar_uclu(k, nw);
  if (tekrar > 2) c[SK_TEKRAR_IFADE] = 0.5 * (tekrar - 2);

  // olay_cezalari(metin, [ad], plan), sec.TUM_ISIM = ürün adları
  int ncd = sc_bol_dolu(m, n);
  if (sc_iki_tanitim(m, n, ad)) c[SK_IKI_TANITIM] = 3;
  if (sc_kendi_kendine_var(m, k, ncd, ad)) c[SK_KENDI_KENDINE] = 2;
  if (sc_baskasi(m, n, ad)) c[SK_BASKASI] = 2;
  if (sc_uydurma_ad(m, n, URUN_TUM_ISIM, URUN_TUM_ISIM_N)) c[SK_UYDURMA_AD] = 2;
  c[SK_OZELLIK] = sc_ozellik(k, n);
  c[SK_KEKEME] = sc_kekeme(k, n);
  if (sc_ders(k, ncd)) c[SK_DERS] = 1.5;
  if (plan) {
    int pn = sc_coz(plan, plan_n, sc_p, SECICI_PLAN_MAKS);
    if (sc_plan_bozuk(sc_p, pn)) c[SK_PLAN] = 2;
  }

  // kadro_cezalari
  if (sc_kendine_seslenme(m, n, f)) c[SK_KENDINE_SESLENME] = 3;
  {
    int gecen = 0, tekrar_ad = 0;
    for (int t = URUN_KADRO_OFF[f]; t < URUN_KADRO_OFF[f + 1]; t++) {
      if (!sc_say(m, 0, n, URUN_KADRO[t], 1, 1)) continue;
      gecen++;
      if (!tekrar_ad && sc_ad_ad(m, n, URUN_KADRO[t], 1)) tekrar_ad = 1;
    }
    if (tekrar_ad) c[SK_KADRO_TEKRAR] = 3;
    if (gecen > 1)  // figürün kendi adı olay kurallarında; burada adlı yanlar
      for (int t = URUN_KADRO_OFF[f]; t < URUN_KADRO_OFF[f + 1]; t++)
        if (strcmp(URUN_KADRO[t], ad) && sc_say(m, 0, n, URUN_KADRO[t], 1, 1) &&
            sc_kendi_kendine_var(m, k, ncd, URUN_KADRO[t]))
          c[SK_YAN_KENDI_KENDINE] += 2;
  }
  {
    int u = sc_kartta_olmayan(m, k, n, f);
    if (u) c[SK_KARTTA_OLMAYAN] = 2 * u < 6 ? 2 * u : 6;
  }
  {
    int t = sc_takinti(k, nw, f);
    if (t) c[SK_TAKINTI] = 0.5 * t;
  }
  if (yer >= 0 && yer < 6 && sc_yer_kaymasi(k, n, yer)) c[SK_YER] = 1.5;
  if (sc_guvenlik(k, n)) c[SK_GUVENLIK] = 4;
  double ceza = 0;
  for (int i = 0; i < SK_N; i++) ceza += c[i];
  return -ceza + 2 * lp;
}
#endif  // SECICI_URUN
