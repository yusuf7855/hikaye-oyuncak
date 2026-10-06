# Ses: kartta çalışacak Türkçe kadın sesi

Hedef: Supertonic 3 F2 kadın sesine olabildiğince yakın, tamamen kartta (ESP32-S3) çalışan bir ses modeli.
Ürün hikâyelerinden 25 bin cümlenin Supertonic okuması öğretmen olarak kullanılır (`veri_uret_st.py`); küçük model onu
taklit etmeyi öğrenir. Önceki öğretmen Emel (edge-tts, `veri_uret.py`) Microsoft koşulları yüzünden satılan üründe
kullanılamaz; yalnız eski deneme için duruyor. Supertonic lisansı (Open RAIL-M) ticari kullanıma açık; koşullar
`docs/SES_ARASTIRMASI.md` ve `veri_uret_st.py` başında.

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

## Çalıştırma (Colab Pro, önerilen)

`ses/colab_egitim.ipynb` defterini Colab'da açın, önce veriyi CPU çalışma zamanında hazırlayın, sonra L4 GPU seçin, hücreleri sırayla çalıştırın.
Kayıtlar Drive'daki `hikaye_ses/` klasörüne gider; oturum koparsa bütün hücreleri yeniden çalıştırmak yeter.

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
- `disa_aktar.py`: eğitilmiş modelleri karta aktarır (`ses.bin`, ~4,34 MB; akustik 4 bit, vocoder 8 bit) ve C
  çıkarımını (`firmware/hikaye_oyuncak/ses.h`) sınamak için altın örnekler yazar. Kart adımları:
  `firmware/hikaye_oyuncak/README.md` (5. Ses).
