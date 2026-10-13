// Sahte ESP32 başlığı (bilgisayarda deneme): sabit MAC.
#pragma once
#include <stdint.h>
#define ESP_MAC_WIFI_SOFTAP 1
static inline int esp_read_mac(uint8_t *mac, int) {
  static const uint8_t M[6] = {0x24, 0x0A, 0xC4, 0x12, 0xAB, 0xCD};
  for (int i = 0; i < 6; i++) mac[i] = M[i];
  return 0;
}
