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

## İyileştirme döngüsü

Hedef: hakem puanı ≥7/10, olay örgüsü soruları ≥%90, bariz hatalar nadir; kullanıcının hedef örneği
docs/HIKAYE_ANALIZI.md sonunda. Üst üste 3 tur iyileşme olmazsa dur.

### Tur 1 — E4: ince ayarda oyuncak payı %15 → %32 (c2ft_e4; genel veri 8M → 4M token, gerisi E3 ile aynı)

| Kol | Rubrik | S1 / S2 / S3 | Genel ikili (v4 + yeni seçiciye karşı) | Karar |
|---|---|---|---|---|
| v4 (c2ft_plan) | 4.89 | %90 / %76 / %78 | — | en iyi kalıyor |
| E4 (c2ft_e4) | 4.74 | %81 / %68 / %69 | 84/165 (%51: test 19/36, doğrulama 65/129) | **benimsenmedi** |

- Oyuncak doğrulama kaybı 2.4257 → 2.4154 (küçük iyileşme), ama hakemlerde fark yok. Veri karışımı sınır değil.
- Kurallar ile hakem puanı arasındaki ilişki zayıf: 468 hakemli hikâyede korelasyon 0.33; kurallara hiç takılmayan
  hikâyelerin ortalaması 4.96, yalnız %21'i ≥7. "Her hikâye en az hedef seviyede" için daha iyi bir kalite ölçer
  gerekiyor. Kol dışı çapraz doğrulamada kurallar + log-olasılık + modelin son gizli durumunun ortalaması (160 boyut)
  üstüne ridge: korelasyon 0.55. Tur 2 bu "öğrenen seçici".

### Tur 2 — öğrenen seçici (degerlendirme/odul.py; model v4)

- 480 yeni etiket: v4'ün doğrulama havuzundan (129 vaka, vaka başına en çok 4 aday) tek rubrik hakemiyle; önceki
  504 etiketle toplam 984. Özellik: -(kural cezası), gövde uzunluğu, C motorundan (gen -H -G) son gizli durumun gövde
  ortalaması (160). Ridge.
- Kol-dışı korelasyon: öğrenen 0.545, yalnız kurallar 0.43. Ama asıl iş olan **aynı vakanın adayları arasında
  sıralamada** fark yok: 5 katlı (vakaya göre) çapraz doğrulamada çift doğruluğu öğrenen 0.647, eski seçici
  (kurallar + 2·log-olasılık) 0.673, ikisi birden 0.686; seçilen adayın hakem ortalaması 4.06 / 4.09 / 4.16.
  **Benimsenmedi** (gürültü düzeyinde fark; kartta ek iş).
- Asıl bulgu: 4 adaydan **en iyisi bile ortalama 5.12** (rastgele 3.38, eski seçici 4.09). Seçici tavana yakın; hedef
  seviye (≥7, kullanıcının örneği ~9) için üretimin kendisi iyileşmeli. Seçim yolu tükendi.

### Tur 3 — üretimi değiştirmeden iyileştirme: hazır plan ve düşük sıcaklık (model v4)

| Karşılaştırma | n | Genel ikili (yeni kolun payı) | Karar |
|---|---|---|---|
| Hazır (gerçek hikâyeden) plan vs modelin kendi planı, doğrulama vakaları | 128 | 60 (%47) | benimsenmedi |
| Sıcaklık 0.35 vs 0.5, test seti | 36 | 18 (%50) | benimsenmedi |

- Hazır plan kartta "plan bankası" (önceden yazılmış iyi Sorun/Çözüm listesi) olacaktı; iyi plan verilince bile hikâye
  iyileşmiyor: sınır plan değil, planı tutarlı bir hikâyeye dökme becerisi.

### Durum: 3 tur üst üste iyileşme yok (durma kuralı)

- En iyi sistem: **v4 (c2ft_plan) + E5b seçici** (rubrik ~4.9, olay örgüsü %90/%76/%78).
- Denenip tükenen yollar: veri karışımı (E4), öğrenen seçici (Tur 2), hazır plan ve sıcaklık (Tur 3); daha önce
  tema başlığı (E1), temiz veri (R-temiz), hizalı pencereler (E2). Seçici tavana yakın: 4 adayın en iyisi ~5.1.
- Kalan büyük yol, modelin kapasitesi: çekirdeği büyütmek (kart bütçesinin yeniden düzenlenmesi + ön-eğitimin
  baştan yapılması) ya da daha çok bellekli bir kart. Kullanıcı kararı bekleniyor.

## Tur 4 hazırlığı — büyük model (C3) ve v4 verisi

- **C3** (docs/ESP32_BUTCE.md "C3"): aynı kart (N16R8) için çekirdek 3.0M → 5.7M (d192 L12 F512 P56). Ön-eğitim
  `egit_c3.sh`, 24 000 adım. Aynı adımda doğrulama kaybı C2'den düşük (9 500. adım: 2.399 / 2.442).
- **v4 verisi** (data/oyuncak_v4, KILAVUZ.md): kullanıcının 10/10 örneğinin tarzında, 50 hikâye analizinden çıkan
  kurallarla yazılmış 1104 hikâye (72/72 tek figür-yer × 8, 66/66 ikili × 8), planlarıyla. Denetim (kontrol.py:
  v3 kuralları + seçicinin olay kuralları + güvenlik) 1104/1104. Rubrik hakemi (40 rastgele hikâye): **9.88/10**,
  S1/S2/S3 %100. İnce ayardaki oyuncak hikâyesi 2102 → 3206.
- Zincir (`zincir_c3.sh`): C3 + v2/v3/v4 ince ayar (4000 adım, plan) → ölçüm; ardından ayrıştırma için C2 + v4.

## Tur 4 — C3 ince ayar (c3ft_v5)

- Model: C3 ön-eğitim (val 2.146) + v2/v3/v4 + ilk popüler karakter partisi, 5000 adım, plan modu. Kalan hakem-dışı
  hikâye listesi o an 29 kimlikti (popüler paketlerin çoğu henüz yazılmamış/hakemlenmemişti). Son doğrulama 2.38.
  model.bin 10.3 MB (bölüme sığıyor), C motoru PyTorch ile birebir.
- Seçim: E5b kural seçici, 8 aday. Kurallar: en iyi 8'de 34/36 temiz, 36/36 biten, plan bozuk 0.

| Ölçüm | c3ft_v5 | Taban (v4 + E5b) |
|---|---|---|
| Rubrik (36 test × 2 hakem) | 4.06 | 4.89 (eski hakemler; aynı hakemle ölçülmedi) |
| Genel ikili, test | 18/36 (%50) | — |
| Genel ikili, doğrulama | 74/129 (%57, p≈0.06) | — |
| Genel ikili, toplam | 92/165 (%56) | — |

- Karar: **benimsenmedi** (anlamlı üstünlük yok; rubrik düşük). v4 kartta kalır. Model `modeller/c3ft_v5`.
- Neden beklenen: bu ince ayar, kılavuzdaki yeni kurallar ve hakem–düzeltme döngüsünden geçmiş veri gelmeden
  yapıldı.

## Veri — popüler karakterler (hakem–düzeltme döngüsü)

- 12 karakter (Elsa, Peppa, Bluey, Chase, Pepee, Niloya, Maşa, Örümcek Adam, Gabby, Stitch, Moana, Dora) × 2 paket ×
  48 = **1152 hikâye**. Her hikâye sıkı veri hakemine (HAKEM_VERI.md) girdi, 10 almayanlar en çok iki kez
  düzeltildi (DUZELTICI.md). Sonuç: **1063 tam puan (%92)**; kalan 89 hikâye eğitimden çıkarıldı.
- İlk turda hakemin en sık reddettikleri kılavuza eklendi (zaman kayması -mıştı, güçlü arkadaşın "yapamıyorum"
  demesi, sonradan beliren karakter, dünyanın kuralları: Elsa'nın dünyasında hayvanlar konuşmaz vb.). Sonra yazılan
  paketlerde ilk tur geçme oranı arttı (ör. Niloya 35 → 40/48, Örümcek Adam 16 → 29/48).

## Tur 5 — C3 + tüm tam puanlı popüler hikâyeler (c3ft_v6)

- `zincir_c3c.sh`: C3 ön-eğitimden, 5000 adım; eğitim dışı: hakemde 10 almayanlar + hakemlenmemiş v5 dosyaları
  (`data/egitim_haric.txt`, 384 kimlik). Oyuncak hikâyesi 3698 → 4353.
- Sonuç (c3ft_v6, E5b seçici, 8 aday): son doğrulama 2.34 (v5: 2.38); kurallar en iyi 8'de 35/36.

| Ölçüm | c3ft_v6 | Taban (v4 + E5b) |
|---|---|---|
| Rubrik, aynı 4 hakem ikisini birlikte puanladı (36 test × 2) | 4.38 | 4.42 |
| Genel ikili, test | 19/36 (%53) | 17 |
| Genel ikili, doğrulama | 75/129 (%58) | 54 |
| Genel ikili, toplam | 94/165 (%57, tek yönlü p≈0.04) | 71 |

- Yorum: 12 temel figürde C3 ancak sınırda önde (ikili hakem), rubrikte eşit. Ek olarak popüler karakterleri
  (Elsa, Chase…) bilen tek model bu; v4 onları hiç görmedi. Kartta hız C3'te daha düşük (tahmin ~3.7 token/s).
- Mutlak seviye hâlâ düşük: rubrik ~4.4/10 (hedef 8–9). Veri tarafı 10/10 düzeyine geldi (1063 popüler + v4);
  kalan fark modelin kapasitesinden.

## Tur 6 — Uzun ön eğitim (c3u) + aynı ince ayar (c3ft_v7)

- Neden: C3 ön eğitiminde doğrulama kaybı hâlâ düşüyordu (Türkçe TinyStories'te ~1,8 dönem). `zincir_c3u.sh`:
  C3'ten 48 bin adım daha (lr 6e-4), sonra Tur 5 ile aynı ince ayar (5000 adım, aynı veri ve eğitim dışı liste).
- Ön eğitim iyileşti: doğrulama 2,1467 → **2,0517** (`modeller/c3u`, yalnız ağırlıklar).
- İnce ayardan sonra geriledi: son doğrulama 2,462 (v6: 2,341), eğitim 1,83 (v6: 2,02); aşırı uyum işareti.
  Kurallar en iyi 8'de 32/36 (v6: 35/36), plan sorun uyumu %84,0 (v6: %90,8).

| Ölçüm | c3ft_v7 | Taban (v4 + E5b) |
|---|---|---|
| Rubrik, aynı 4 hakem ikisini birlikte puanladı (36 test × 2) | 3,82 | 4,35 |
| Genel ikili, test | 16/36 (%44) | 20 |
| Genel ikili, doğrulama | 57/129 (%44) | 72 |

- Karar: **benimsenmedi**. Model `modeller/c3ft_v7`; kartta v4 kalır. (Taban modelin Tur 5 puanları
  `degerlendirme/c2ft_plan_olay2/tur5_v6/` altında.)
- Yorum: dil modeli olarak daha iyi temel, hikâyeye iyi aktarılmadı. Daha güçlü temelle aynı 5000 adım ve
  aynı öğrenme hızı fazla gelmiş olabilir. Sıradaki deneme adayı: c3u'dan daha kısa / düşük öğrenme hızlı ince
  ayar (ör. 2000–3000 adım, lr yarıya), doğrulama kaybının en düşük olduğu adımda durmak.
