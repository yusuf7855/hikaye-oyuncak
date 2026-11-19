// Sahte WebServer (bilgisayarda deneme): yollar kaydedilir; kart_pc "#http GET /durum" ya da
// "#http POST /kaydet ad=Emre&ses_maks=5" istek taklidi yapar (gövde application/x-www-form-urlencoded, % çözülür),
// yanıt sahte_yanit'ta.
#pragma once
#include "WiFi.h"
#include <functional>
#include <vector>
enum HTTPMethod { HTTP_ANY = 0, HTTP_GET = 1, HTTP_POST = 3 };
enum HTTPUploadStatus { UPLOAD_FILE_START, UPLOAD_FILE_WRITE, UPLOAD_FILE_END, UPLOAD_FILE_ABORTED };
#define HTTP_UPLOAD_BUFLEN 1436
struct HTTPUpload {
  HTTPUploadStatus status;
  String filename, name, type;
  size_t totalSize, currentSize;
  uint8_t buf[HTTP_UPLOAD_BUFLEN];
};
struct WebServer {
  typedef std::function<void(void)> THandlerFunction;
  struct Yol { std::string yol; int yontem; THandlerFunction fn, yukle; };
  HTTPUpload yuklenen;
  std::vector<Yol> yollar;
  THandlerFunction bulunamadi;
  std::map<std::string, std::string> args;
  bool acik = false;
  int yanit_kod = 0;
  std::string yanit_tur, yanit, konum;
  explicit WebServer(int) {}
  void on(const char *y, int yontem, THandlerFunction fn) { yollar.push_back({y, yontem, fn, nullptr}); }
  void on(const char *y, int yontem, THandlerFunction fn, THandlerFunction ufn) { yollar.push_back({y, yontem, fn, ufn}); }
  void on(const char *y, THandlerFunction fn) { yollar.push_back({y, HTTP_ANY, fn, nullptr}); }
  HTTPUpload &upload() { return yuklenen; }
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
  // Dosya yükleme taklidi (çok parçalı form): veri HTTP_UPLOAD_BUFLEN'lik parçalarla yükleme işleyicisine, sonra
  // yolun işleyicisine; kes > 0 ise o kadar bayttan sonra yükleme yarıda kesilir (ABORTED). Döner yanıt kodu.
  int sahte_yukle(const char *yol, const std::string &veri, const char *dosya_adi, long kes = 0) {
    yanit_kod = 0; yanit.clear(); konum.clear(); args.clear();
    if (!acik) return 0;
    for (auto &r : yollar) {
      if (r.yol != yol || !r.yukle) continue;
      yuklenen.filename = String(dosya_adi);
      yuklenen.totalSize = 0;
      yuklenen.currentSize = 0;
      yuklenen.status = UPLOAD_FILE_START;
      r.yukle();
      for (size_t i = 0; i < veri.size(); i += HTTP_UPLOAD_BUFLEN) {
        if (kes > 0 && (long)i >= kes) { yuklenen.status = UPLOAD_FILE_ABORTED; r.yukle(); return yanit_kod; }
        size_t k = veri.size() - i < HTTP_UPLOAD_BUFLEN ? veri.size() - i : HTTP_UPLOAD_BUFLEN;
        memcpy(yuklenen.buf, veri.data() + i, k);
        yuklenen.currentSize = k;
        yuklenen.totalSize += k;
        yuklenen.status = UPLOAD_FILE_WRITE;
        r.yukle();
      }
      yuklenen.status = UPLOAD_FILE_END;
      yuklenen.currentSize = 0;
      r.yukle();
      r.fn();
      return yanit_kod;
    }
    if (bulunamadi) bulunamadi();
    return yanit_kod;
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
