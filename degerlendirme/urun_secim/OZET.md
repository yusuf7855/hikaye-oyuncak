# Ürün modeli (c3ft_urun1030s2) için seçim deneyleri

## Tavan: 41 vaka × 8 aday, rubrik hakemi (RUBRIK.md, 10 puan)

| Seçim | Seçilen hikâyenin ortalaması |
|---|---|
| Rastgele aday | 2,89 |
| Modelin log-olasılığı | 3,34 |
| Kural seçici (`urun_uret.puanla`) | 3,85 |
| Öğrenen seçici (ridge: kurallar + lp + uzunluk + gizli durum ortalaması, vakaya göre 5 katlı CV) | 3,76–3,83 |
| Tavan (8 adayın hakeme göre en iyisi) | 5,20 |

- Uzunluk hakem puanıyla −0,46 ilişkili (kusur başına düşen rubrik). Uzunluk cezası CV'de 3,85 → 4,02; rubrik yan etkisi olabileceği için eklenmedi.
- Seçilen ile en iyi arasındaki fark: karakter karışıklığı (16/41 ile 2/41) ve net sorun (s1 %61 / %78).
- K'ya göre (alt küme benzetimi, kural seçici): K=1 2,88 · 2 3,32 · 4 3,73 · 8 4,02; tavan 2,88 · 3,75 · 4,56 · 5,20.

## Konuşma kuralları (kendi sorusunu cevaplama, yarım "X ile", tanıtılmamış "ikisi") — benimsenmedi

Kurallar 8 adaylık rubrik notlarından türetildi; ayrı veride (164 vakalık büyük kıyasın adayları, 16 değişen seçim) kör ikili:
genel 9/7, olay 6/8 (yeni/eski). Gürültü düzeyi; kod geri alındı. Kayıtlar `konusma_kurallari/`.

## 16 aday – 8 aday (aynı seçici; ilk 8 aday aynı seed'ler)

41 vakanın 18'inde seçim değişti. Kör ikili (16 / 8 / eşit):

| Hakem | Sonuç |
|---|---|
| Genel kalite 1 | 11 / 7 / 0 |
| Genel kalite 2 | 11 / 7 / 0 |
| Olay örgüsü 1 | 8 / 9 / 1 |
| Olay örgüsü 2 | 8 / 7 / 3 |

16 aday genel kalitede küçük ve tutarlı bir kazanç veriyor (iki hakem de 11/7), olay örgüsünde fark yok. Anlamlı değil (n=18).
