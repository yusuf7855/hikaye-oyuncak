# Deney sonuçları

Plan: [OLAY_ORGUSU_PLANI.md](OLAY_ORGUSU_PLANI.md). Test seti: `degerlendirme/uret.py test_seti()` (36 vaka: 24 tek
figür + 12 ikili), K=8 aday, temp 0.5, top-k 40, rep 1.1; seçici `sec.py`. Hakemler: kol başına 2 bağımsız rubrik
hakemi (`RUBRIK.md`, S1-S3 olay örgüsü soruları) + kör ikili tercih (`IKILI.md`; metni iki kolda aynı olan vakalar
hakeme gitmez).

## E0 — örnekleme ayarları (model: c2ara = v1 önizleme, ön-eğitim 6000 adım + 1500 adım ince ayar)

| Kol | Rubrik (10) | S1 sorun var / S2 sonda çözülüyor / S3 olaylar bağlı | mantıksız olay/hikâye | İkili tercih (tabana karşı) | Karar |
|---|---|---|---|---|---|
| c2ara (taban) | 4.86 | %64 / %46 / %50 | 1.35 | — | — |
| c2ara_P: başlık tekrar penceresinde değil (`-P`) | 4.69 | %72 / %40 / %51 | 1.31 | 5/16 (Kaybetti) | **reddedildi** |
| c2ara_N: gövdede satır sonu yasak (`-N`) | 4.76 | %65 / %51 / %56 | 1.49 | 5/8 (Eşit) | **benimsendi** (eşit + bekçiler sağlam; paragraf kırılması %5.6 → %0) |
| E: istem başında `<|endoftext|>` | — | — | — | NLL: −0.0069 nat/token, %95 GA [0.0047, 0.0090] | **benimsendi** (`prompt_idler(eot=True)`) |

- Hakem uyumu yüksek: puan farkı ort. 0.44–0.61, S1 %92–100.
- Otomatik ölçüler (en iyi 8'den seçilen): üç kolda da 36/36 kuralları geçiyor, uydurma kelime %0, 36/36 biten;
  seçicinin kuralları bu modelde doymuş, ayrımı hakemler yapıyor.
- En sık kusurlar (tabanda, vaka): mantıksız olay 28.5, bozuk dil 25.5, karakter karışıklığı 17, tekrar 8.5.
- Karşılaştırma: eski C1 + ince ayar (tam ön-eğitim) 4.94 almıştı; v1 ön-eğitimin dörtte biriyle 4.86.
