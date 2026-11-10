# Keloğlan: son model c3ft_v5 – ürün modeli c3ft_karma (kör ikili kıyas)

Keloğlan, eski ürün modelinin de bildiği tek ürün figürü. `urun_kiyas_v5`'te Keloğlan'da ara model v5a son
modelin önündeydi (16 vakada 10–6, anlamlı değil); son modelin şu anki ürün modelinden geri olmadığını
doğrulamak için ayrı kıyas.

- 48 vaka: `urun_uret.py <model> m<ad>.json --figur keloglan --aday 8 --tekrar-vaka 12` (4 yer × 12 tohum);
  c3ft_v5 = `hf_c3ft_v5`, c3ft_karma = `modeller/c3ft_karma` (üründeki model).
- Seçici puanı: v5 −2,051 (38 cezasız) – karma −2,123 (37 cezasız); ikisinde de yanlış isim, bozuk plan,
  bitmemiş hikâye yok.
- 1 parti × 2 hakem (IKILI_GENEL.md, IKILI.md); A/B sırası rastgele (tohum 8484, A=v5 25/48), anahtar hakemlik
  süresince klasör dışındaydı (`anahtar.json` sonradan kondu).

| Hakem | v5 | karma | eşit | p (tek yönlü işaret testi, v5 > karma) |
|---|---|---|---|---|
| Genel kalite | 34 | 14 | 0 | 0,003 |
| Olay örgüsü | 29 | 15 | 4 | 0,024 |

**Sonuç:** son model Keloğlan'da da ürün modelini açık farkla geçiyor; yeni figür verisi Keloğlan'ı bozmadı.
