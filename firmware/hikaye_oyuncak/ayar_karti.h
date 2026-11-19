// Ayar kartının telefona dönük yüzü: NDEF Wi-Fi kaydı. Telefon karta dokununca oyuncağın ayar ağına bağlanır.
//
// Ayar modu açılınca oyuncak, standdaki ayar kartına o oturumun ağ adını ve şifresini yazar (her oturumda yeni şifre).
// Kart kaldırılıp telefonun arkasına dokundurulunca Android "Ağa bağlanılsın mı?" diye sorar: NFC Forum Type 2
// etiketinde bir NDEF mesajı, tek kayıt, MIME "application/vnd.wfa.wsc" (Wi-Fi Simple Configuration, "Configuration
// Token": Credential = ağ adı, WPA2-Kişisel, AES, şifre). Bağlanınca ayar sayfası kendiliğinden açılır (captive
// portal). iPhone bu kaydı kendiliğinden işlemez: ağ adı ve şifre yine sesli söylenir.
//
// Etiket belleği (NTAG213/215; kullanıcı belleği sayfa 4'ten başlar):
//   sayfa 4..       TLV alanı: 03 L <NDEF mesajı> FE, sonu 00 (telefonlar bunu okur)
//   sayfa 36..37    oyuncağın kendi kaydı (etiket.h: "EKO" + sürüm + nfc_no + CRC). NDEF sonlandırıcısından (FE)
//                   sonra durduğu için telefonlar görmez.
// Figür etiketlerinde kayıt sayfa 4'tedir (etiket.h). Oyuncak sayfa 4'te kayıt yerine NDEF TLV'si (03) görürse kaydı
// sayfa 36'dan okur (nfc.h nfc_etiket_no). Yazma sırası (nfc.h nfc_ayar_karti_yaz): önce sayfa 36-37, sonra sayfa 4'ten
// başlayarak TLV alanı. Yazma hangi sayfada kesilirse kesilsin kart ayar kartı olarak tanınır: 4'e yazılmadan önce
// eski kayıt (sayfa 4-5) durur, 4 yazıldıktan sonra sayfa 36'daki kayıt okunur.
//
// Saf C: tools/urun_test.c dener; tools/ndef_test.py aynı baytları bağımsız bir NDEF çözücüyle (ndeflib) okur.
#pragma once
#include <stdint.h>
#include <string.h>

#define AYAR_KARTI_EK_SAYFA 36   // oyuncağın kaydı (ETIKET_BAYT = 2 sayfa) NDEF'ten sonra burada
#define AYAR_KARTI_TLV_MAKS ((AYAR_KARTI_EK_SAYFA - 4) * 4)  // sayfa 4..35: 128 bayt
#define NDEF_TLV 0x03
#define NDEF_SON 0xFE

static const char WSC_MIME[] = "application/vnd.wfa.wsc";

// WSC özniteliği (tür ve uzunluk 2'şer bayt, büyük uçlu). Döner: yazılan bayt (yer yoksa -1).
static inline int wsc_oznitelik(uint8_t *out, int kap, uint16_t tur, const void *veri, int n) {
  if (n < 0 || 4 + n > kap) return -1;
  out[0] = (uint8_t)(tur >> 8);
  out[1] = (uint8_t)tur;
  out[2] = (uint8_t)(n >> 8);
  out[3] = (uint8_t)n;
  if (n) memcpy(out + 4, veri, (size_t)n);
  return 4 + n;
}

// Wi-Fi Simple Configuration yükü (Configuration Token): Version 1.0, Credential {Network Index 1, SSID,
// Authentication Type WPA2-Personal, Encryption Type AES, Network Key, MAC Address}, Vendor Extension (WFA, Version2
// 2.0). Döner: yük uzunluğu (sığmazsa -1).
static inline int wsc_yuk(const char *ssid, const char *sifre, const uint8_t mac[6], uint8_t *out, int kap) {
  uint8_t kim[96];
  int k = 0, r;
  const uint8_t idx = 1, auth[2] = {0x00, 0x20}, enc[2] = {0x00, 0x08};
  int ns = (int)strlen(ssid), nk = (int)strlen(sifre);
  if (ns < 1 || ns > 32 || nk < 8 || nk > 63) return -1;
#define WSC_EKLE(t, v, n) do { r = wsc_oznitelik(kim + k, (int)sizeof kim - k, (t), (v), (n)); if (r < 0) return -1; k += r; } while (0)
  WSC_EKLE(0x1026, &idx, 1);          // Network Index
  WSC_EKLE(0x1045, ssid, ns);         // SSID
  WSC_EKLE(0x1003, auth, 2);          // Authentication Type: WPA2-Personal
  WSC_EKLE(0x100F, enc, 2);           // Encryption Type: AES
  WSC_EKLE(0x1027, sifre, nk);        // Network Key
  WSC_EKLE(0x1020, mac, 6);           // MAC Address (erişim noktası)
#undef WSC_EKLE
  int n = 0;
  const uint8_t surum = 0x10, satici[6] = {0x00, 0x37, 0x2A, 0x00, 0x01, 0x20};  // WFA: Version2 = 2.0
  if ((r = wsc_oznitelik(out + n, kap - n, 0x104A, &surum, 1)) < 0) return -1;  // Version
  n += r;
  if ((r = wsc_oznitelik(out + n, kap - n, 0x100E, kim, k)) < 0) return -1;     // Credential
  n += r;
  if ((r = wsc_oznitelik(out + n, kap - n, 0x1049, satici, 6)) < 0) return -1;  // Vendor Extension
  return n + r;
}

// Ayar kartının sayfa 4'ten başlayan TLV alanı: 03 L <NDEF kaydı> FE + 00 dolgu (4'ün katı). NDEF mesajı tek kayıt:
// başlık D2 (MB ME SR, TNF 2 = MIME türü), tür uzunluğu, yük uzunluğu (1 bayt), tür, yük.
// Döner: yazılacak bayt (4'ün katı; AYAR_KARTI_TLV_MAKS'ı aşarsa -1).
static inline int ayar_karti_tlv(const char *ssid, const char *sifre, const uint8_t mac[6], uint8_t *out, int kap) {
  uint8_t yuk[160];
  int ny = wsc_yuk(ssid, sifre, mac, yuk, (int)sizeof yuk);
  int nt = (int)sizeof WSC_MIME - 1;
  if (ny < 0 || ny > 255) return -1;
  int nk = 3 + nt + ny;                       // NDEF kaydı
  int n = 2 + nk + 1;                         // TLV + sonlandırıcı
  int dolgu = (4 - n % 4) % 4;
  if (n + dolgu > AYAR_KARTI_TLV_MAKS || n + dolgu > kap || nk > 254) return -1;
  uint8_t *p = out;
  *p++ = NDEF_TLV;
  *p++ = (uint8_t)nk;
  *p++ = 0xD2;
  *p++ = (uint8_t)nt;
  *p++ = (uint8_t)ny;
  memcpy(p, WSC_MIME, (size_t)nt);
  p += nt;
  memcpy(p, yuk, (size_t)ny);
  p += ny;
  *p++ = NDEF_SON;
  for (int i = 0; i < dolgu; i++) *p++ = 0;
  return (int)(p - out);
}
