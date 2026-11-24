# Yeni model c3ft_v6 (33 924 hikâye) – ürün modeli c3ft_urun13 kör kıyası (hakemlik bekliyor)

Not: Ekim 2026'daki eski `degerlendirme/c3ft_v6` deneyiyle ilgisi yok; ad çakışması yüzünden bu klasör `urun_kiyas_v6`.

- **c3ft_v6:** urun_v2 1030 + urun_v3 9567 + urun_v4 5922 + urun_v5 11 974 + urun_v6 5431 (neden-sonuç ve mantık
  odaklı yeni hafif hat verisi) = 33 924 hikâye (`birlestir urun_karma5 urun_v3 urun_v4 urun_v5 urun_v6 --gecesiz`).
  `TAG=c3ft_v6 IZIN=data/urun_karma5/izin.txt ... STEPS=16500 bash zincir_urun.sh` (bulutta CPU, ~1,33 s/adım;
  aynı ~3,7 tur). En iyi adım 15 500, val **1,8843** (c3ft_urun13 = c3ft_v5: 1,8877). Golden testi geçti
  (C = PyTorch). model.bin 10,33 MB (boyut aynı). Günlük `logs/zincir_c3ft_v6.log`.

Aynı 180 vaka (13 ürün figürü × yerler × 4 tohum), ikisi de `urun_uret.py <model> <çıktı> --aday 8 --tekrar-vaka 4`:

| Model | ort. seçici puanı | cezasız | yanlış isim | bozuk plan | bitmemiş |
|---|---|---|---|---|---|
| c3ft_v6 (`mv6.json`) | −1,872 | 164/180 | 0 | 0 | 0 |
| c3ft_urun13 (`mu13.json`) | −2,011 | 157/180 | 0 | 0 | 0 |

(c3ft_urun13 sonucu `urun_kiyas_v5/mv5.json` ile aynı: üretim belirlenimci.)

Hakemlik: 4 parti × 45 vaka × 2 hakem (IKILI_GENEL.md, IKILI.md), `hakem/parti_*.json`. A/B sırası rastgele
(tohum 7373, A konumunda v6 97/180); anahtar hakemlik bitene kadar bu klasörün dışında durur.
Seçici puanı kalite ölçüsü değildir; karar kör kıyasla verilir.
