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

## E1 — başlıkta tema (c2ara_tema; taban c2ara_NE = c2ara + satır yasağı + EOT öneki)

| Kol | Rubrik | S1 / S2 / S3 | mantıksız olay/hikâye | İkili tercih | Karar |
|---|---|---|---|---|---|
| c2ara_NE (taban) | 4.74 | %83 / %62 / %71 | 1.22 | 24/36 | — |
| c2ara_tema_NE | 4.17 | %85 / %51 / %60 | 2.18 | **12/36 (Kaybetti)** | **reddedildi** (varsayılan olmadı) |

- Mekanizma çalışıyor: doğru temayla ikinci yarının NLL'i 0.030 nat/token düşük (GA [0.026, 0.035]; plasebo, temayı
  hiç görmemiş c2ara'da 0.002). Ama hikâyelerin yalnızca %33'ü istenen temaya uyuyor (tema NB), farklı tema 12/20.
- Hakemler temalıyı açıkça daha mantıksız buldu (iki ikili hakemin uyumu %86). Tema başına (n=1-2, yalnızca işaret):
  uyku vakti 1.5, hatadan öğrenmek 1.8, kaybolan bir şeyi bulmak 2.8 … doğayı korumak 6.2, yeni arkadaş edinmek 7.0.
  Yorum: temasız model kendi kolay olay örgüsünü seçiyor; tema onu henüz yazamadığı örgülere zorluyor ve parçalar
  karışıyor ("dedi taş", topu kaybeden kişi değişiyor).
- Yan bulgu: yeni varsayılanlar (satır yasağı + EOT öneki) tabanda olay örgüsü sorularını belirgin yükseltti
  (E0 tabanı %64/%46/%50 → %83/%62/%71; farklı hakemler, dikkatli yorumlanmalı).
- Sonraki: R tabanı temasız başlıkla (+ sabit bölme, blok EOT). Tema, tam ön-eğitimli modelde ve/veya yalnız "kolay"
  temalardan oluşan bir desteyle yeniden denenebilir. E3 (model önce kendi planını yazar) temaya bağlı değil.
