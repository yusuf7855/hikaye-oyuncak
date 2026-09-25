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

## R — tam ön-eğitim (24 000 adım) + sabit bölme + blok EOT; R-temiz — aynısı, denetimde bozuk 289 hikâye çıkarılmış

| Kol | Rubrik | S1 / S2 / S3 | mantıksız olay/hikâye | İkili tercih | Karar |
|---|---|---|---|---|---|
| c2ara_NE (v1, ön-eğitim 6000 adım) | 4.74 | %83 / %62 / %71 | 1.22 | — | — |
| c2ft_NE (R) | 4.58 | %88 / %71 / %82 | 1.35 | v1'e karşı 21.25/36 (Eşit, p=0.20) | **yeni taban** |
| c2ft_temiz_NE (R-temiz) | 4.33 | %86 / %54 / %69 | 1.75 | R'ye karşı 12.75/36 (**Kaybetti**) | reddedildi |

- Tam ön-eğitim olay örgüsü sorularını belirgin yükseltti (S2 %62→%71, S3 %71→%82); toplam puan ve ikili tercih
  anlamlı fark göstermedi. Bozuk dil en sık kusur olarak kaldı (32.5/36 vaka).
- Bozuk hikâyeleri çıkarmak (%12 veri) sonucu kötüleştirdi; iki ikili hakemin uyumu %92. Her kol tek eğitim koşusu,
  farkın bir kısmı eğitim rastlantısallığı olabilir. Bozukların yarısı güvenlik içerikliydi (yaralanma, boğulma,
  derin su); bunlar artık seçicide ele alınıyor: `sec.GUVENLIK` + `puanla(guvenlik=True)` (arayüzde/kartta her zaman
  açık, −4 ceza). R'nin 288 adayından 10'unda bu kelimeler var; seçilen 36 hikâyede 0 (v1'de 3/36).
- Sonraki: E2 (hizalı pencereler) ve E3 (önce plan) R'nin ayarlarıyla (bütün veri) eğitiliyor.

## E2 — hikâyeye hizalı eğitim pencereleri (c2ft_hiz) ve E3 — model önce Sorun/Çözüm planı yazar (c2ft_plan)

Taban: R (c2ft_NE). E3 modeli iki biçimde ölçüldü: planlı (b) ve plansız başlıkla (a).

| Kol | Rubrik | S1 / S2 / S3 | mantıksız olay/hikâye | İkili tercih (R'ye karşı) | Karar |
|---|---|---|---|---|---|
| c2ft_NE (R) | 4.58 | %88 / %71 / %82 | 1.35 | — | — |
| c2ft_hiz (E2) | 4.85 | %78 / %61 / %69 | 1.18 | 15/36 (Eşit, R önde) | benimsenmedi (olay örgüsü soruları düştü) |
| c2ft_plan (E3, planlı) | **4.89** | **%90 / %76** / %78 | 1.35 | **21/36** (Eşit, p=0.20) | **şimdilik en iyi: v4** |
| c2ft_plan_a (E3 modeli, plansız) | 4.46 | %85 / %61 / %72 | 1.40 | 11.5/36 (Kaybetti) | plan modu zorunlu |

- E3: planların %100'ü doğru biçimde (plan_bozuk 0/36), hikâyelerin %86'sı kendi planına uyuyor. Doğru plan vs aynı
  temadan başka bir hikâyenin planı: hikâyenin ilk üçte birinde ΔNLL 0.146 nat/token, son üçte birinde yalnızca 0.0075
  — model sorunu plandan kuruyor ama çözüm/son plana zayıf bağlı. Planın kart maliyeti ~20-30 token (~5 sn).
- Planın başarı eşiği (ikili ≥24/36) tutmadı; E3 "Eşit" bandında ama ölçülen her şeyde en iyi ya da eşit en iyi.
- Genel tablo: hiçbir deney belirleyici bir sıçrama vermedi (bütün modeller 4.3–4.9/10). README'deki bulgu duruyor:
  eğitim verisi 9.8/10, model ~4.9/10; sınır 3M çekirdekli modelin kapasitesi. 36 vakada ~0.3 puanlık farklar
  gürültü içinde.

## E5b — 50 hikâye analizinden olay örgüsü kuralları (yalnız seçici; model v4 aynı)

Ayrıntı: docs/HIKAYE_ANALIZI.md. Yeni kurallar: iki kez tanıtma, kendi kendine, başkasının figür adıyla tanıtması,
uydurma karakter adı, özellik karışması, kekeme tekrar, ders olaydan kopuk, plan bozuk; güvenliğe kan ve yara eklendi.
Eğitim verisinde tetiklenme ~%2, v4'ün 50 hikâyesinde %40.

| Karşılaştırma (yalnız seçimi değişen vakalar) | n | Olay örgüsü (IKILI.md) | Genel kalite (IKILI_GENEL.md) |
|---|---|---|---|
| tüm kurallar vs eski seçici | 63 | 34.25 (%54) | 39 (%62, p=0.038) |
| son kurallar (plan uyumu çıkarıldı) vs eski seçici | 49 | 25.75/43 (%60) | **32 (%65, p=0.022)** |

- Plan-hikâye kelime uyumu kuralları seçimi kötüleştirdi (genel hakemde %23 / %47); çıkarıldı.
- **Benimsendi:** arayüzde açık. `sec.puanla(..., plan=...)` artık planı da alıyor.
