# Ses: kartta çalışacak Türkçe kadın sesi

Hedef: Emel (edge-tts) sesine olabildiğince yakın, tamamen kartta (ESP32-S3) çalışan bir ses modeli.
Emel'in 25 bin cümlelik okuması öğretmen olarak kullanılır; küçük model onu taklit etmeyi öğrenir.

## Yapı

| Parça | Görev | Boyut | Kartta |
|---|---|---|---|
| Akustik (FastPitch benzeri) | harfler → mel (+ süre, perde, enerji tahmini) | 2,6 M | 4 bit, ~1,49 MB |
| Vocoder (Vocos benzeri) | mel → 16 kHz ses (STFT genlik+faz, iSTFT) | 2,8 M | 8 bit, ~2,84 MB |

Toplam ~4,33 MB. LLM'den sonra flash'ta ~4,49 MB boş kaldığından boyutlar buna göre en büyük seçildi.
Kartta ~260 M çarpma / saniye ses; gerçek zamandan hızlı çalışması beklenir.

Kaliteyi artıran seçimler:
- Tonlama: perde ve enerji harf başına tahmin edilip modele verilir (düz okumayı engeller).
- Hizalama dışarıdan gelmez; eğitimde öğrenilir (RAD-TTS hizalayıcısı + MAS). Hizalayıcı karta gitmez.
- Vocoder GAN ile eğitilir (çok periyotlu + çok çözünürlüklü ayırt ediciler), sonra akustik modelin
  kendi çıktısıyla ince ayar yapılır (GTA). Bu adım bulanıklığı ve çınlamayı azaltır.
- Son adımlar kartın 4/8 bit ağırlıklarıyla eğitilir (QAT): kartta sıkıştırınca kalite düşmez.

## Çalıştırma (Mac M3)

```bash
python3 -m venv .venv && .venv/bin/pip install -r ses/requirements.txt
./ses/calistir.sh            # veri -> hazırlık -> akustik -> vocoder -> GTA (günler sürer, devam edebilir)
```

Aşamalar tek tek de çalışır: `./ses/calistir.sh akustik`. Yarıda kalırsa aynı komut kaldığı yerden sürer.
Aynı anda tek eğitim çalıştırın (8 GB bellek).

İlerleme: `tail -f ses_calisma/akustik.log` (veya `vocoder.log`, `gta.log`).
Örnek sesler: `ses_calisma/akustik/ornek/` (vocoder yokken Griffin-Lim ile, kaba), `ses_calisma/vocoder/ornek/`.

Deneme: `.venv/bin/python ses/sentezle.py --metin "Bir varmış bir yokmuş." --cikti deneme.wav [--kuant]`

## Dosyalar

- `metin.py`: Türkçe metin → harf sembolleri (kartta C'ye aynen taşınacak kadar basit)
- `veri_uret.py`: `metin.tsv`deki 25 bin cümleyi Emel sesiyle indirir
- `hazirla.py`: mp3 → 16 kHz, log-mel, perde (f0), uzunluk listesi
- `ortak.py`: ses ayarları, STFT/iSTFT/mel (evrişimle, MPS'te de çalışır), perde takibi, MAS
- `model.py`: modeller; `kuant.py`: kart kuantizasyonu; `veri.py`: veri okuma
- `egit_akustik.py`, `egit_vocoder.py`, `sentezle.py`, `calistir.sh`
