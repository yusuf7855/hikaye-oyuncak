// Sahte DNS sunucusu (bilgisayarda deneme): yalnız durum.
#pragma once
#include "WiFi.h"
enum class DNSReplyCode { NoError = 0 };
struct DNSServer {
  bool acik = false;
  void setErrorReplyCode(DNSReplyCode) {}
  bool start(uint16_t, const char *ad, IPAddress) { acik = true; fprintf(stderr, "DNS %s\n", ad); return true; }
  void stop() { acik = false; }
  void processNextRequest() {}
};
