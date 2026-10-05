# 740 / 1030 hikâyeli ürün modelleri: kör ikili kıyas

41 vaka (11 figür × kart yerleri), her model 8 aday + isim süzgeci (`degerlendirme/urun_uret.py --aday 8`), seçici en iyiyi alır.
İki bağımsız hakem: genel kalite (IKILI_GENEL.md) ve olay örgüsü (IKILI.md). Sıra rastgele, anahtar `anahtar*.json`.

| Tur | Kıyas | Genel kalite (740 / 1030 / eşit) | Olay örgüsü (740 / 1030 / eşit) |
|---|---|---|---|
| 1 | 740 (2000 adım) – 1030 (6000'lik koşunun 1000. adımı, val 2,664) | 25 / 16 / 0 (p=0,21) | 23 / 12 / 6 (p=0,09) |
| 2 | 740 (2000 adım, val 2,660) – 1030 (2000 adım, val 2,553) | 26 / 15 / 0 (p=0,12) | 18 / 12 / 11 (p=0,36) |

Doğrulama kaybı 1030'da belirgin düşük, ama hakemler iki turda da 740'ı biraz öne koydu; hiçbir fark anlamlı değil (işaret testi, eşitler hariç).
Seçici puanı ikisinde aynı (−2,33 / −2,34). Hakemlerin en sık gerekçeleri iki tarafta da: karakterin kendine davranması, tanıtılmamış adlar, kekeme tekrar.

## Seçici kuralları (kendine hitap, kartta olmayan ad, takıntılı tekrar)

Aynı 8 adaydan yeni seçici (`urun_uret.kadro_cezalari`, `takinti_cezasi`) ile eskisinin farklı seçtiği vakalar (82 vakanın 16'sı),
kör ikili. Anahtar `secici_tur*/anahtar.json`.

| Tur | Kural sürümü | Genel kalite (yeni / eski / eşit) | Olay örgüsü (yeni / eski / eşit) |
|---|---|---|---|
| 1 | ilk taslak | 11 / 5 / 0 | 7 / 9 / 0 |
| 2 | son (yanlış alarm %2,3) | 12 / 4 / 0 (p≈0,08) | 7 / 7 / 2 |

Kurallar hedefledikleri karakter hatalarını (genel kalite) iyileştiriyor, olay örgüsüne etkisi yok.
