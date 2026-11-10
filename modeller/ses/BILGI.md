# Ses Modeli Bilgileri

## Tarihler
- Veri üretimi: Ekim 2026
- Akustik eğitimi: Ekim 2026
- Vocoder eğitimi: Ekim-Kasım 2026
- GTA ince ayar: Kasım 2026

## Veri
- **Cümle/mp3 sayısı:** 25.000
- **Referans ses:** `ses/referans_ses.mp3` (VoxCPM2, Apache-2.0 lisansı)

## Eğitim
- **Akustik:** 150.000 adım
- **Vocoder:** 600.000 adım
- **GTA:** +50.000 adım (toplam 650.000)
  - Komut: `python ses/egit_vocoder.py --gta --adim 650000 --is 0`
  - Checkpoint: `ses_calisma/vocoder/son.pt` üstünde

## Son Kayıp Değerleri
**Akustik (150.000 adım):**
- mel: 0.3467, sure: 0.0544, perde: 0.3294, enerji: 0.0934, ctc: 0.6701, bin: 0.0976
- Doğrulama mel L1: 0.3949 (4-bit: 0.3814)

**Vocoder GTA (650.000 adım):**
- mel: 0.1721, adv: 3.5923, fm: 4.1758, ad: 2.9077

## Çıktı
- **ses.bin boyutu:** 4.344.208 bayt (4,14 MiB)
- **SHA-256:** `575fa75733db3145220c4803d5a330774a88c9a05d03d792a8f3b0fd47278ca4`
- **Limit:** 4.390.912 bayt - SIĞIYOR (112 KB boş)

## Notlar
- `ses_test.py` PC'de çalışmadı (C derleyicisi yok, WSL'de torch yok)
- Ürün sahibinin yorumu: "şimdilik iyi, idare eder"

## Dosyalar
- `ses.bin` - Kuantize edilmiş model (firmware için)
- `ses_altin.bin` - Test cümleleri için altın referans
- `akustik.pt` - Akustik model ağırlıkları (sadece üretici)
- `vocoder.pt` - Vocoder ağırlıkları (sadece üretici)
- `vocoder_ayirt_fp16.pt` - Ayırt edici ağırlıkları (fp16)
- `deneme.wav` - Örnek sentez çıktısı
- `gunluk/` - Eğitim günlükleri
