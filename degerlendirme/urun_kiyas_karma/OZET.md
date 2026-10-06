# 10 bin hikâyeli model (c3ft_karma) – 1030 hikâyeli model (c3ft_urun1030s2): kör ikili kıyas

- **c3ft_karma:** urun_v2 hakemli 1030 + urun_v3 hafif hat (yazar + kod kontrolü, hakemsiz) 9567 hikâye = 10 597.
  `IZIN=data/urun_karma/izin.txt TEKRAR=2 GENEL=4000000 STEPS=6000 zincir_urun.sh`, en iyi adım 5999, val 2,015.
- **c3ft_urun1030s2:** 1030 hakemli hikâye, 2000 adım, val 2,553 (aynı 41 hikâyelik doğrulama bölmesi).
- Model boyutu aynı (c3, model.bin 10,3 MB); ESP32-S3 N16R8 bütçesi değişmedi.

Aynı 164 vaka (41 figür×yer × 4 tohum), ikisi de 8 aday + isim süzgeci + kadro/takıntı seçicisi
(`urun_uret.py --aday 8 --tekrar-vaka 4`). 1030s2 çıktıları `urun_kiyas_740_1030/buyuk_164/m1030.json` (= `m1030s2.json`).
4 parti × 2 hakem (IKILI_GENEL.md, IKILI.md); A/B sırası rastgele, anahtar hakemlik süresince klasör dışındaydı.

| Hakem | karma | 1030s2 | eşit | p (işaret testi) |
|---|---|---|---|---|
| Genel kalite | **127** | 37 | 0 | <0,001 |
| Olay örgüsü | **112** | 41 | 11 | <0,001 |

Seçici puanı: karma −2,05 (164 vaka, 133 cezasız) – 1030s2 ≈ −2,34.

Sonuç: 10 kat alan içi veri, seçimle düzelmeyen olay örgüsü tutarlılığını belirgin biçimde iyileştirdi (740→1030'daki
%40 artışın aksine). Hakemsiz hafif hat yeterli; tüm hikâyeleri hakemlerden geçirmeye gerek görülmedi.
Ürün modeli önerisi: c3ft_karma (+ isim süzgeci + K aday seçici).

## Rubrik puanı (RUBRIK.md, 10 üzerinden)

41 vaka (her figür×yer için ilk tohum), iki modelin seçilmiş hikâyeleri karışık sırada, 2 hakem (`rubrik/`).

| Model | Ortalama | Dağılım | karakter karışık | tekrar |
|---|---|---|---|---|
| 1030s2 | 3,17 | 1–6 | 13/41 | 10 |
| **karma** | **4,51** | 2–7 | 2/41 | 16 |

İki hakem de aynı yönde (hakem 1: 2,77 → 4,26; hakem 2: 3,63 → 4,73). Karakter karışıklığı neredeyse bitti; mantık ve
dil kusurları hâlâ hemen her hikâyede var (yazar ajanlarının hikâyeleri ~9,7).
