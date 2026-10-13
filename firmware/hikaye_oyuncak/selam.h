// Oyuncağın söylediği kalıp cümleler: selamlama (doğru Türkçe tamlayan/iyelik ekiyle), ninni selamı, veda, ayar
// şifresi.
//
//   selam_iyelik("Niloya") -> "Niloya'nın" | "Keloğlan" -> "Keloğlan'ın" | "Doru" -> "Doru'nun" | "Örümcek Adam" ->
//   "Örümcek Adam'ın" (çok sözcüklü adda son sözcük) | "Hello Kitty" -> "Hello Kitty'nin" | "Chase" -> "Chase'in"
//
// Kural: özel ad + kesme işareti + ek; ek son ünlüye uyar (büyük ünlü uyumu: a ı -> ın, e i -> in, o u -> un,
// ö ü -> ün); ad ünlüyle bitiyorsa araya kaynaştırma "n" girer (nın/nin/nun/nün). Yabancı adlarda okunuş esas:
// sözcük sonundaki ünsüzden sonra gelen "y" i okunur (Kitty -> "Kitti" -> 'nin); okunuşu yazılışından ayrılan adlar
// SELAM_ISTISNA tablosundadır (Chase "Çeys" okunur -> 'in). Saf C: tools/urun_test.c 11 figürü ve adsız durumu dener.
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

// "Merhaba Emre, şimdi sana Niloya'nın hikâyesini okuyacağım." (cocuk boş ya da NULL: "Merhaba, şimdi sana ...")
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
