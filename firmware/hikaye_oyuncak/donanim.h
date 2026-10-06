// Donanım ve ürün ayarları: bütün pin numaraları ve davranış sabitleri burada (README "Bağlantılar").
// Pin seçimi (ESP32-S3-DevKitC-1 N16R8): 26-32 flash, 33-37 sekizli PSRAM, 19/20 USB, 43/44 UART0, 0/3/45/46
// açılış ayar uçları, 38/48 kart üstü RGB LED: bunlara bağlanmaz. 1-21 RTC GPIO'dur (hafif uykudan uyandırabilir).
#pragma once

// ---- I2S hoparlör (MAX98357A) ----
#define I2S_BCLK_PIN 4
#define I2S_LRC_PIN 5
#define I2S_DIN_PIN 6
#define AMP_SD_PIN -1          // MAX98357A SD ucu bu GPIO'ya bağlıysa konuşmazken LOW (yükselteç uyur); -1 bağlı değil

// ---- düğmeler: GPIO ile GND arasında, iç pull-up (basılı = LOW) ----
#define DUGME_FIGUR_PIN 7
#define DUGME_YER_PIN 15
#define DUGME_OYNAT_PIN 16

// ---- LED: kart üstü RGB LED (RGB_BUILTIN) kullanılır; ayrıca tek renkli LED istenirse (aktif HIGH) ----
#define DURUM_LED_PIN -1
#define LED_PARLAKLIK 40       // RGB LED en yüksek parlaklık (0-255); göz almasın, akım az olsun

// ---- NFC/RFID figür okuyucu (nfc.h): 0 yok | 1 RC522 (SPI, MFRC522 kütüphanesi) | 2 PN532 (I2C, Adafruit_PN532) ----
#ifndef NFC_OKUYUCU
#define NFC_OKUYUCU 0
#endif
#define NFC_SPI_SCK 12
#define NFC_SPI_MISO 13
#define NFC_SPI_MOSI 11
#define NFC_SPI_SS 10
#define NFC_RST_PIN 9
#define NFC_I2C_SDA 8
#define NFC_I2C_SCL 18
#define NFC_IRQ_PIN 17          // PN532 IRQ
#define NFC_OYNAT 1            // tanınan figür okuyucuya konunca hikâye de başlasın (0: yalnız figür seçilir)

// ---- hikâye kuyruğu (kuyruk.h) ----
#ifndef KUYRUK_K
#define KUYRUK_K 16            // kuyruğa hazırlanan hikâyede aday sayısı (ürün önerisi, degerlendirme/urun_secim)
#endif
#ifndef KUYRUK_FIGUR_BASI
#define KUYRUK_FIGUR_BASI 3    // figür başına hazır tutulan hikâye (11 x 3 = 33 <= 48 yuva)
#endif
#ifndef ARKA_BEKLE_MS
#define ARKA_BEKLE_MS 5000     // son düğme/komuttan bu kadar sonra arka planda üretime başlanır
#endif

// ---- güç ----
#ifndef UYKU_ACIK
#define UYKU_ACIK 1            // boşta ve üretecek iş yokken hafif uyku
#endif
#ifndef UYKU_BEKLE_MS
#define UYKU_BEKLE_MS 30000    // son etkinlikten bu kadar sonra uyunur
#endif
#define UYKU_DILIM_MS 10000    // bir uyku en çok bu kadar (sonra uyanıp kuyruğa ve seri porta bakar)
#define SES_SEVIYE_N 8         // ses seviyeleri 0..7
#define SES_SEVIYE_VARSAYILAN 6
#define BEKCI_SN 30            // görev bekçisi (task watchdog): ana döngü bu kadar beslenmezse kart yeniden başlar
