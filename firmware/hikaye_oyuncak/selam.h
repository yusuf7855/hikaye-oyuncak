// Oyuncağın söylediği kalıp cümleler: selamlama (doğru Türkçe tamlayan/iyelik ekiyle; SELAM_CESIT çeşit, sırayla),
// ninni selamı, veda, ayar şifresi, alarm (günaydın + mesaj), yatma vakti, gece kilidi, sürpriz mesaj, ad denemesi.
// Ebeveynin yazdığı mesajlardaki rakamlar sözcüğe çevrilir (sayilari_yaz: "8'de" -> "sekizde", "07:30" -> "yedi
// otuz"); ses modeli rakam okumaz.
//
//   selam_iyelik("Keloğlan") -> "Keloğlan'ın" | "Pinokyo" -> "Pinokyo'nun" | "Bulut" -> "Bulut'un" |
//   "Tek Boynuzlu At" -> "Tek Boynuzlu At'ın" (çok sözcüklü adda son sözcük) | "Hello Kitty" -> "Hello Kitty'nin" |
//   "Chase" -> "Chase'in"
//
// Kural: özel ad + kesme işareti + ek; ek son ünlüye uyar (büyük ünlü uyumu: a ı -> ın, e i -> in, o u -> un,
// ö ü -> ün); ad ünlüyle bitiyorsa araya kaynaştırma "n" girer (nın/nin/nun/nün). Yabancı adlarda okunuş esas:
// sözcük sonundaki ünsüzden sonra gelen "y" i okunur (Kitty -> "Kitti" -> 'nin); okunuşu yazılışından ayrılan adlar
// SELAM_ISTISNA tablosundadır (Chase "Çeys" okunur -> 'in). Saf C: tools/urun_test.c donanım figürlerinin hepsini,
// üründen çıkan eski figürlerin adlarını ve adsız durumu dener.
#pragma once
#include <stdint.h>
#include <stdio.h>
#include <string.h>

typedef struct { const char *sozcuk, *ek; } SelamIstisna;
static const SelamIstisna SELAM_ISTISNA[] = {
    {"Chase", "'in"},   // Çeys
};

static uint32_t selam_utf8(const unsigned char **p) {
  const unsigned char *s = *p;
  uint32_t c = *s++;
  int n = 0;
  if (c >= 0xF0) { c &= 0x07; n = 3; }
  else if (c >= 0xE0) { c &= 0x0F; n = 2; }
  else if (c >= 0xC0) { c &= 0x1F; n = 1; }
  for (int i = 0; i < n && (*s & 0xC0) == 0x80; i++) c = (c << 6) | (*s++ & 0x3F);
  *p = s;
  return c;
}

// Ünlü sınıfı: 0 ünsüz | 1 kalın düz (a ı â) | 2 ince düz (e i î) | 3 kalın yuvarlak (o u û) | 4 ince yuvarlak (ö ü)
static int selam_unlu(uint32_t c) {
  switch (c) {
    case 'a': case 'A': case 0xE2: case 0xC2: case 0x131: case 'I': return 1;
    case 'e': case 'E': case 'i': case 0x130: case 0xEE: case 0xCE: return 2;
    case 'o': case 'O': case 'u': case 'U': case 0xFB: case 0xDB: return 3;
    case 0xF6: case 0xD6: case 0xFC: case 0xDC: return 4;
  }
  return 0;
}

// Adın tamlayan eki (kesme işaretiyle): "'nın" ... Döner: ek (durağan dizge).
static const char *selam_ek(const char *ad) {
  static const char *const EK[2][5] = {{"'in", "'ın", "'in", "'un", "'ün"}, {"'nin", "'nın", "'nin", "'nun", "'nün"}};
  const char *son = ad + strlen(ad), *bas;
  while (son > ad && son[-1] == ' ') son--;
  for (bas = son; bas > ad && bas[-1] != ' '; bas--) {}
  for (size_t i = 0; i < sizeof SELAM_ISTISNA / sizeof SELAM_ISTISNA[0]; i++)
    if ((size_t)(son - bas) == strlen(SELAM_ISTISNA[i].sozcuk) && !memcmp(bas, SELAM_ISTISNA[i].sozcuk, son - bas))
      return SELAM_ISTISNA[i].ek;
  int sinif = 0, sonda = 0;  // son ünlünün sınıfı, ad ünlüyle mi bitiyor
  uint32_t onceki = 0;
  for (const unsigned char *p = (const unsigned char *)bas; p < (const unsigned char *)son;) {
    uint32_t c = selam_utf8(&p);
    int u = selam_unlu(c);
    if (u) sinif = u;
    sonda = u != 0;
    if ((c == 'y' || c == 'Y') && p >= (const unsigned char *)son && onceki && !selam_unlu(onceki)) {
      sinif = 2;  // yabancı adda sondaki "y" = i (Kitty, Teddy)
      sonda = 1;
    }
    onceki = c;
  }
  return EK[sonda][sinif];
}

// ad + ek; döner: yazılan uzunluk (kap'a sığmazsa kesilir)
static int selam_iyelik(const char *ad, char *out, int kap) {
  int n = snprintf(out, (size_t)kap, "%s%s", ad, selam_ek(ad));
  return n < kap ? n : kap - 1;
}

// "Merhaba Emre, şimdi sana Keloğlan'ın hikâyesini okuyacağım." (cocuk boş ya da NULL: "Merhaba, şimdi sana ...")
static int selam_metni(const char *cocuk, const char *figur, char *out, int kap) {
  char iy[96];
  selam_iyelik(figur, iy, sizeof iy);
  int n = (cocuk && *cocuk) ? snprintf(out, (size_t)kap, "Merhaba %s, şimdi sana %s hikâyesini okuyacağım.", cocuk, iy)
                            : snprintf(out, (size_t)kap, "Merhaba, şimdi sana %s hikâyesini okuyacağım.", iy);
  return n < kap ? n : kap - 1;
}

// Ninni modu (gece figürü): "İyi geceler Emre, şimdi sana bir ninni söyleyeceğim."
static int ninni_selam_metni(const char *cocuk, char *out, int kap) {
  int n = (cocuk && *cocuk) ? snprintf(out, (size_t)kap, "İyi geceler %s, şimdi sana bir ninni söyleyeceğim.", cocuk)
                            : snprintf(out, (size_t)kap, "İyi geceler, şimdi sana bir ninni söyleyeceğim.");
  return n < kap ? n : kap - 1;
}

static int veda_metni(const char *cocuk, char *out, int kap) {
  int n = (cocuk && *cocuk) ? snprintf(out, (size_t)kap, "İyi geceler %s, tatlı rüyalar.", cocuk)
                            : snprintf(out, (size_t)kap, "İyi geceler, tatlı rüyalar.");
  return n < kap ? n : kap - 1;
}

// Rakamları okunacak sözcüklere çevirir ("47" -> "dört, yedi"); ses modeli rakam okumaz.
static int rakam_metni(const char *rakamlar, char *out, int kap) {
  static const char *const AD[10] = {"sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"};
  int n = 0;
  if (kap > 0) out[0] = 0;
  for (const char *p = rakamlar; *p; p++) {
    if (*p < '0' || *p > '9') continue;
    int k = snprintf(out + n, (size_t)(kap - n), "%s%s", n ? ", " : "", AD[*p - '0']);
    if (k < 0 || n + k >= kap) break;
    n += k;
  }
  return n;
}

// ---- selam çeşitleri: 0 her açılışta ilk selam (eski selam), sonra sırayla ----
#define SELAM_CESIT 3
static int selam_metni_cesit(int cesit, const char *cocuk, const char *figur, char *out, int kap) {
  int ad = cocuk && *cocuk;
  int n;
  switch (((cesit % SELAM_CESIT) + SELAM_CESIT) % SELAM_CESIT) {
    case 1:
      n = ad ? snprintf(out, (size_t)kap, "%s, bak kim geldi: %s! Dinlemeye hazır mısın?", cocuk, figur)
             : snprintf(out, (size_t)kap, "Bak kim geldi: %s! Dinlemeye hazır mısın?", figur);
      break;
    case 2:
      n = ad ? snprintf(out, (size_t)kap, "Hoş geldin %s! %s yeni bir maceraya çıkıyor.", cocuk, figur)
             : snprintf(out, (size_t)kap, "Hoş geldin! %s yeni bir maceraya çıkıyor.", figur);
      break;
    default:
      return selam_metni(cocuk, figur, out, kap);
  }
  return n < kap ? n : kap - 1;
}

// ---- rakamlar sözcüğe ----
// 0..999 999 999 arası sayı: "iki yüz otuz dört bin beş yüz"; döner uzunluk
static int sayi_yazi(long v, char *out, int kap) {
  static const char *const BIR[10] = {"", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"};
  static const char *const ON[10] = {"", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"};
  int n = 0;
  if (kap > 0) out[0] = 0;
  if (v == 0) return snprintf(out, (size_t)kap, "sıfır");
#define SY_EKLE(x) do { int k_ = snprintf(out + n, (size_t)(kap - n), "%s%s", n ? " " : "", (x)); if (k_ < 0 || n + k_ >= kap) return n; n += k_; } while (0)
  static const char *const BOLUK[3] = {"milyon", "bin", ""};
  long b[3] = {v / 1000000 % 1000, v / 1000 % 1000, v % 1000};
  for (int i = 0; i < 3; i++) {
    long u = b[i];
    if (!u) continue;
    int y = (int)(u / 100), o = (int)(u / 10 % 10), r = (int)(u % 10);
    if (y > 1) SY_EKLE(BIR[y]);
    if (y) SY_EKLE("yüz");
    if (o) SY_EKLE(ON[o]);
    if (r && !(i == 1 && u == 1)) SY_EKLE(BIR[r]);  // "bin", "bir bin" değil
    if (*BOLUK[i]) SY_EKLE(BOLUK[i]);
  }
#undef SY_EKLE
  return n;
}

// Metindeki rakam dizilerini sözcüğe çevirir: "8'de" -> "sekizde" (sayıdan sonraki kesme işareti düşer), "07:30" ->
// "yedi otuz", 9 haneden uzun diziler tek tek okunur. Döner uzunluk.
static int sayilari_yaz(const char *in, char *out, int kap) {
  int n = 0;
  if (kap > 0) out[0] = 0;
  for (const char *p = in; *p && n < kap - 1;) {
    if (*p >= '0' && *p <= '9') {
      const char *b = p;
      while (*p >= '0' && *p <= '9') p++;
      char sayi[160];
      if (p - b <= 9) {
        long v = 0;
        for (const char *q = b; q < p; q++) v = v * 10 + (*q - '0');
        sayi_yazi(v, sayi, sizeof sayi);
      } else {
        char r[16];
        int k = 0;
        for (const char *q = b; q < p && k < 15; q++) r[k++] = *q;
        r[k] = 0;
        rakam_metni(r, sayi, sizeof sayi);
      }
      int k = snprintf(out + n, (size_t)(kap - n), "%s", sayi);
      if (k < 0 || n + k >= kap) break;
      n += k;
      if (*p == '\'' && ((p[1] >= 'a' && p[1] <= 'z') || (unsigned char)p[1] >= 0x80)) p++;  // "8'de" -> "sekizde"
      if (*p == ':' && p[1] >= '0' && p[1] <= '9') { out[n++] = ' '; p++; }                  // "07:30"
      continue;
    }
    out[n++] = *p++;
  }
  out[n < kap ? n : kap - 1] = 0;
  return n;
}

// ---- alarm, yatma vakti, gece kilidi, sürpriz mesaj, ad denemesi ----
static int alarm_metni(const char *cocuk, const char *mesaj, char *out, int kap) {
  char m[512];
  m[0] = 0;
  if (mesaj && *mesaj) sayilari_yaz(mesaj, m, sizeof m);
  int n = (cocuk && *cocuk) ? snprintf(out, (size_t)kap, "Günaydın %s! Kalkma vakti geldi.%s%s", cocuk, *m ? " " : "", m)
                            : snprintf(out, (size_t)kap, "Günaydın! Kalkma vakti geldi.%s%s", *m ? " " : "", m);
  return n < kap ? n : kap - 1;
}

static int yatma_metni(const char *cocuk, char *out, int kap) {
  int n = (cocuk && *cocuk)
              ? snprintf(out, (size_t)kap, "%s, uyku vakti geldi. Ay Dede'yi standa koyarsan sana ninni söylerim.", cocuk)
              : snprintf(out, (size_t)kap, "Uyku vakti geldi. Ay Dede'yi standa koyarsan sana ninni söylerim.");
  return n < kap ? n : kap - 1;
}

static int gece_kilit_metni(const char *cocuk, char *out, int kap) {
  int n = (cocuk && *cocuk)
              ? snprintf(out, (size_t)kap, "%s, şimdi uyku vakti. Hikâyeler sabah devam edecek. İstersen Ay Dede'yi koy, "
                                           "sana ninni söyleyeyim.", cocuk)
              : snprintf(out, (size_t)kap, "Şimdi uyku vakti. Hikâyeler sabah devam edecek. İstersen Ay Dede'yi koy, "
                                           "sana ninni söyleyeyim.");
  return n < kap ? n : kap - 1;
}

static int surpriz_metni(const char *cocuk, const char *mesaj, char *out, int kap) {
  char m[512];
  sayilari_yaz(mesaj ? mesaj : "", m, sizeof m);
  int n = (cocuk && *cocuk) ? snprintf(out, (size_t)kap, "%s, sana bir mesaj var: %s", cocuk, m)
                            : snprintf(out, (size_t)kap, "Sana bir mesaj var: %s", m);
  return n < kap ? n : kap - 1;
}

static int ad_dene_metni(const char *cocuk, char *out, int kap) {
  int n = (cocuk && *cocuk) ? snprintf(out, (size_t)kap, "Merhaba %s! Adını doğru söylüyor muyum?", cocuk)
                            : snprintf(out, (size_t)kap, "Merhaba! Henüz bir ad yazılmadı.");
  return n < kap ? n : kap - 1;
}
