// Donanım ve ürün ayarları: bütün pin numaraları ve davranış sabitleri burada (README "Bağlantılar").
// Pin haritası docs/URUN_TANIMI.md'deki kesin tablodur (ESP32-S3-DevKitC-1 N16R8); değişirse bütün belgeler birlikte.
// Kullanılmayan uçlar: 0, 3, 45, 46 (açılış), 19/20 (USB), 26-37 (flash/PSRAM), 43/44 (UART), 38/48 (kart üstü RGB
// LED: kullanılmaz). 1-21 RTC GPIO'dur.
#pragma once

// ---- I2S0: hoparlör yükselteci (MAX98357A) ----
#define I2S_BCLK_PIN 4
#define I2S_LRC_PIN 5
#define I2S_DIN_PIN 6
#define AMP_SD_PIN 7           // MAX98357A SD: konuşmazken LOW (yükselteç uyur); -1 bağlı değil

// ---- I2S1: mikrofon (INMP441; L/R -> GND: sol kanal) ----
#define MIK_SCK_PIN 15
#define MIK_WS_PIN 16
#define MIK_SD_PIN 17
#ifndef MIK_KAYDIRMA
#define MIK_KAYDIRMA 14        // 32 bitlik örnek >> bu kadar = 16 bit (INMP441 24 bit; 14: +6 dB kazanç)
#endif
#ifndef MIK_ACIK
#define MIK_ACIK 1             // 0: mikrofon ve sesli komut yok (yalnız stand)
#endif

// ---- NFC okuyucu (nfc.h): 0 taslak (okuyucu yok; seri porttan "n koy 3") | 1 RC522 (ürün) | 2 PN532 (SPI) ----
#ifndef NFC_OKUYUCU
#define NFC_OKUYUCU 1
#endif
#define NFC_SPI_SCK 12
#define NFC_SPI_MISO 13
#define NFC_SPI_MOSI 11
#define NFC_SPI_SS 10
#define NFC_RST_PIN 9
#define NFC_YOKLA_MS 250       // stand bu aralıkla yoklanır
#define NFC_KALKTI_MS 1000     // etiket bu kadar görünmezse oyuncak kalkmış sayılır

// ---- NeoPixel halka (WS2812B uyumlu; 74AHCT1G125 seviye çevirici + 330 Ω, girişte 1000 µF) ----
#define HALKA_PIN 18
#ifndef HALKA_LED_SAYISI
#define HALKA_LED_SAYISI 35    // ürün sahibince doğrulanacak; yazılım bu sayıdan bağımsız
#endif
#ifndef HALKA_PARLAKLIK_SINIR
#define HALKA_PARLAKLIK_SINIR 25   // % (yazılımdaki tavan; ayardaki parlaklık bunun yüzdesidir)
#endif
#ifndef HALKA_AKIM_SINIR_MA
#define HALKA_AKIM_SINIR_MA 600    // toplam halka akımı tahmini bunu aşarsa kare kısılır
#endif
#define HALKA_LED_MA 20        // LED başına renk kanalı başına tam parlaklık akımı (WS2812B ~20 mA)
#define HALKA_FPS 30

// ---- düğmeler (yalnız geliştirme: ürün düğmesizdir) ----
#ifndef DUGME_ACIK
#define DUGME_ACIK 0           // 1: üç düğme (dugmeler.h) geliştirme için; pinler aşağıda (boş uçlar)
#endif
#define DUGME_FIGUR_PIN 1
#define DUGME_YER_PIN 2
#define DUGME_OYNAT_PIN 14

// ---- hikâye kuyruğu (kuyruk.h) ----
#ifndef KUYRUK_K
#define KUYRUK_K 16            // kuyruğa hazırlanan hikâyede aday sayısı (ürün önerisi, degerlendirme/urun_secim)
#endif
#if defined(KUYRUK_FIGUR_BASI) && !defined(KUYRUK_FIGUR_MAKS)
#define KUYRUK_FIGUR_MAKS KUYRUK_FIGUR_BASI   // eski ad
#endif
#ifndef KUYRUK_FIGUR_MAKS
#define KUYRUK_FIGUR_MAKS 6    // tanınmış figür başına en çok hazır hikâye (yuvalar tanınmış figürlere bölünür)
#endif
#ifndef KUYRUK_PAY
#define KUYRUK_PAY 2           // yuva payı: hedef = min(MAKS, (yuva - PAY) / tanınmış figür)
#endif
#ifndef ARKA_BEKLE_MS
#define ARKA_BEKLE_MS 5000     // son etkinlikten bu kadar sonra arka planda üretime başlanır
#endif

// ---- ayar modu (Wi-Fi erişim noktası, yalnız ayar kartı standdayken) ----
#define AYAR_SURE_MS (10UL * 60 * 1000)   // en çok 10 dakika açık
#define AYAR_TANIT_MS 60000    // "oyuncak tanıt": etiket bu kadar beklenir
#define AYAR_BOS_KAPAT_MS 60000 // tanıtmadan sonra stand bu kadar boş kalırsa ayar modu kapanır
#define AYAR_SSID_ONEK "Masalci-Ayar-"

// ---- güç, ses ----
#define UYKU_DILIM_MS 400      // uyku modunda (mikrofon kapalı) hafif uyku dilimi; aralarda stand yoklanır
#define SES_SEVIYE_N 8         // ses seviyeleri 0..7
#define SES_SEVIYE_VARSAYILAN 5
#define BEKCI_SN 30            // görev bekçisi (task watchdog): ana döngü bu kadar beslenmezse kart yeniden başlar
#ifndef SES_SRAM_PAY
#define SES_SRAM_PAY (96 * 1024)  // ses.h sıcak tamponları dahili SRAM'e bu kadar pay bırakarak (Wi-Fi'ye yer)
#endif
#ifndef SESSIZ_MS_HARF
#define SESSIZ_MS_HARF 0       // ses modeli yokken cümle başına harf x bu kadar ms "okunur" (kart_pc: zaman taklidi)
#endif
#define DINLE_MS 4500          // "Merhaba Eko"dan sonra komut penceresi (KWS 4 s; halka bu kadar dinler)
#define UYKU_SONME_MS 60000    // uyku modunda okuma bitince halka bu sürede söner
