// Sahte Wi-Fi (bilgisayarda deneme): erişim noktası açılıp kapanır, stderr'e "WIFI ..." satırları.
// KART_WIFI_HATA=1: softAP başarısız.
#pragma once
#include "sahte_arduino.h"
#define WIFI_OFF 0
#define WIFI_AP 2
struct IPAddress {
  uint8_t b[4];
  IPAddress(int a = 0, int c = 0, int d = 0, int e = 0) { b[0] = (uint8_t)a; b[1] = (uint8_t)c; b[2] = (uint8_t)d; b[3] = (uint8_t)e; }
};
struct SahteWiFi {
  int kip = WIFI_OFF;
  bool ap = false;
  std::string ssid, sifre;
  bool mode(int k) { kip = k; fprintf(stderr, "WIFI kip %d\n", k); return true; }
  bool softAPConfig(IPAddress, IPAddress, IPAddress) { return true; }
  bool softAP(const char *s, const char *p, int kanal = 1, int gizli = 0, int en_cok = 4) {
    const char *h = getenv("KART_WIFI_HATA");
    if (h && *h == '1') return false;
    if (kip != WIFI_AP || !p || strlen(p) < 8) return false;  // WPA2: şifre en az 8
    ap = true; ssid = s; sifre = p;
    fprintf(stderr, "WIFI ap %s %s kanal %d gizli %d en_cok %d\n", s, p, kanal, gizli, en_cok);
    return true;
  }
  bool softAPdisconnect(bool) { ap = false; fprintf(stderr, "WIFI ap kapandi\n"); return true; }
  IPAddress softAPIP() { return IPAddress(192, 168, 4, 1); }
};
static SahteWiFi WiFi;
