// Sahte WebServer (bilgisayarda deneme): yollar kaydedilir; kart_pc "#http GET /durum" ya da
// "#http POST /kaydet ad=Emre&ses_maks=5" istek taklidi yapar (gövde application/x-www-form-urlencoded, % çözülür),
// yanıt sahte_yanit'ta.
#pragma once
#include "WiFi.h"
#include <functional>
#include <vector>
enum HTTPMethod { HTTP_ANY = 0, HTTP_GET = 1, HTTP_POST = 3 };
struct WebServer {
  typedef std::function<void(void)> THandlerFunction;
  struct Yol { std::string yol; int yontem; THandlerFunction fn; };
  std::vector<Yol> yollar;
  THandlerFunction bulunamadi;
  std::map<std::string, std::string> args;
  bool acik = false;
  int yanit_kod = 0;
  std::string yanit_tur, yanit, konum;
  explicit WebServer(int) {}
  void on(const char *y, int yontem, THandlerFunction fn) { yollar.push_back({y, yontem, fn}); }
  void on(const char *y, THandlerFunction fn) { yollar.push_back({y, HTTP_ANY, fn}); }
  void onNotFound(THandlerFunction fn) { bulunamadi = fn; }
  void begin() { acik = true; }
  void stop() { acik = false; }
  void handleClient() {}
  bool hasArg(const char *a) { return args.count(a) > 0; }
  String arg(const char *a) { auto i = args.find(a); return i == args.end() ? String("") : String(i->second); }
  void sendHeader(const char *ad, const char *deger, bool) { if (!strcmp(ad, "Location")) konum = deger; }
  void send(int kod, const char *tur, const char *govde) { yanit_kod = kod; yanit_tur = tur; yanit = govde; }
  static std::string coz(const std::string &x) {
    std::string r;
    for (size_t i = 0; i < x.size(); i++) {
      if (x[i] == '+') r += ' ';
      else if (x[i] == '%' && i + 2 < x.size()) { unsigned b; sscanf(x.c_str() + i + 1, "%2x", &b); r += (char)b; i += 2; }
      else r += x[i];
    }
    return r;
  }
  // İstek taklidi: döner yanıt kodu (0: sunucu kapalı)
  int sahte_istek(const char *yontem, const char *yol, const char *govde) {
    yanit_kod = 0; yanit.clear(); konum.clear(); args.clear();
    if (!acik) return 0;
    std::string g = govde ? govde : "";
    for (size_t b = 0; b < g.size();) {
      size_t e = g.find('&', b);
      if (e == std::string::npos) e = g.size();
      std::string p = g.substr(b, e - b);
      size_t q = p.find('=');
      if (q != std::string::npos) args[coz(p.substr(0, q))] = coz(p.substr(q + 1));
      b = e + 1;
    }
    int y = !strcmp(yontem, "POST") ? HTTP_POST : HTTP_GET;
    for (auto &r : yollar)
      if (r.yol == yol && (r.yontem == HTTP_ANY || r.yontem == y)) { r.fn(); return yanit_kod; }
    if (bulunamadi) bulunamadi();
    return yanit_kod;
  }
};
