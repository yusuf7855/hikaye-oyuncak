# Sunum metni: komisyon ve panel sunumu (10 slayt, ≈5 dakika)

> Hızlandırma programı değerlendirme komisyonu, program sonu iş planı sunumu ve gerekirse TÜBİTAK paneli için.
> Komisyon sunumları genellikle 5 dakika + soru-cevap. Her slaytta **tek mesaj**, az yazı, bol görsel. Demo
> videosunu 2. slayda koyun. `cikti/Eko_Sunum.pptx` (ve PDF kopyası) bu metinden üretildi (`hazirla/sunum.js`);
> konuşma notları slaytların içinde. Demo videosunu 2. slayttaki alana, kişisel bilgileri [AD SOYAD] yerlerine ekleyin.

## Slayt 1 — Açılış

**Eko** — internetsiz, cihaz içi yapay zekâlı Türkçe hikâye oyuncağı.

*"Her gece yeni bir masal. Çocuğunuzun sesi hiçbir yere gitmez."*

[AD SOYAD], kurucu · [hızlandırma programı adı] · [tarih]

**Konuşma (15 sn):** "Merhaba, ben [ad]. Eko'yu anlatacağım: çocuklara her seferinde yeni bir Türkçe hikâye
anlatan, ama internete hiç bağlanmayan bir oyuncak."

## Slayt 2 — Demo (video, 30–45 sn)

Figür standa konur → halka figürün renginde dolar → "Merhaba, şimdi sana Keloğlan'ın hikâyesini okuyacağım" →
hikâye. Ardından "Merhaba Eko, başka" → yeni hikâye.

**Konuşma:** "Gördüğünüz her şey bu küçük kartın içinde oluyor. Hikâyeyi yazan model de, okuyan ses de, sesli
komutu duyan model de. İnternet yok, uygulama yok, abonelik yok."

### Demo videosu çekim planı (gerçek kartta, kart denemesinden sonra)

Videonun işi "bu gerçekten cihazda çalışıyor" demek. Komisyon kurgu şüphesine karşı şunları görmek ister:

1. **Kesintisiz tek çekim** (telefon sabit, ≈60 sn). Hikâyenin ortası hızlandırılacaksa ekranda "2× hızlı"
   yazsın; kesme yapmayın.
2. **İnternet yok kanıtı:** çekimin başında evdeki modemin kapalı olduğunu ya da kartın Wi-Fi'sının kapalı
   olduğunu gösterin (seri monitördeki açılış satırı da olur).
3. **Aynı figür, iki farklı hikâye:** Keloğlan'ı koyun, hikâye başlasın; "Merhaba Eko, başka" deyin, yeni hikâye
   başlasın. "Her seferinde yeni" iddiasının kanıtı bu.
4. **Kartın boyu:** son 5 saniyede standın altını açıp ESP32 kartını parmak yanında gösterin.
5. Ses net olsun: telefonu hoparlöre ≈50 cm yakın tutun, odada başka ses olmasın.
6. Videoya altyazı olarak hikâyenin metnini koymak isterseniz seri monitör çıktısını kullanın; metni
   **düzeltmeyin**.

Figür konduktan sonra hikâyenin ilk cümlesinin ne kadar sürede başladığı kartta henüz ölçülmedi. Ürün
tanımına göre bu arada Eko selam verir ve halkada figür renginde bir nokta yavaşça döner
(`docs/URUN_TANIMI.md`, halka tablosu). Bekleme uzunsa saklamayın; komisyonun ilk sorularından biri olur.
Kart denemesinde bu süreyi ve hızı (`b` komutu) ölçüp sunuma yazın.

## Slayt 3 — Problem

- Ebeveynler ekransız içerik istiyor, ama mevcut ses kutuları **hep aynı kaydı** çalıyor; çocuk sıkılıyor.
- Bulut yapay zekâlı oyuncaklar **çocuğun sesini sunucuya gönderiyor**:
  - FoloToy'un erişimi uygunsuz yanıtlar yüzünden kesildi (2025);
  - Bondu'da ≈50 bin çocuk sohbeti açıkta kaldı (2026);
  - Moxie, sunucusu kapanınca çalışmaz oldu.
- **Türkçe içerik yok denecek kadar az.**

**Konuşma:** "Anne-babalar iki kötü seçenek arasında kalıyor: ya sıkıcı, ya riskli."

## Slayt 4 — Çözüm ve nasıl çalışıyor

Tek mikrodenetleyici (ESP32-S3; 16 MB flash, 8 MB PSRAM) üzerinde üç model:

1. Türkçe dil modeli: ≈19,9 M parametre (5,7 M çekirdek), 10,3 MB. Önce plan, sonra hikâye yazar.
2. Konuşma sentezi: 4,3 MB, kadın sesi, gece modu.
3. "Merhaba Eko" ve 6 komut: 110 KB.

Güvenlik katmanları:

- figür kartıyla kapalı dünya,
- isim süzgeci,
- 5 aday + seçici,
- önceden hazırlanan hikâye kuyruğu.

## Slayt 5 — Kanıt (bugüne kadar)

- **28.493** hikâyeyle eğitim. Kalite **kör kıyaslarla** ölçüldü (yapay zekâ hakemli; insan hakemli test pilotta):
  - son model ara modeli 102–78 ve 99–73 yendi;
  - Keloğlan'da önceki ürün modelini 34–14 yendi.
- Kart yazılımı PC referansıyla **birebir aynı** (52/52 aday; seçicide 872/872).
- Ses: C çıkarımı = PyTorch (SNR ≥ 79 dB).
- 13 figür (5 halk/masal figürü + 8 özgün karakter) ve 100 halk ninnisi.
- TRL 4 → hedef TRL 8 (CE belgeli, pilotta doğrulanmış ürün).

## Slayt 6 — Pazar

| Pazar | Büyüklük |
|---|---|
| Türkiye 3–6 yaş (2028) | ≈3,9 milyon çocuk, ≈3,3 milyon hane; toplam pazar ≈8,2 milyar TL (KDV hariç) |
| Hedef segment (kentli, orta-üst gelir) | ≈1 milyon hane, ≈2,5 milyar TL |
| Ek segmentler | okul öncesi kurumlar, yurt dışındaki Türk aileler |
| Dünya | tonies 630 M€ (+%31), Yoto 95 M£ |

Kategori ekran kaygısıyla büyüyor.

## Slayt 7 — Rakipler

| | Eko | Toniebox/Yoto | Miko/Curio | Yerli sabit masallı |
|---|---|---|---|---|
| Yeni hikâye | ✔ | ✘ | ✔ | ✘ |
| İnternetsiz | ✔ | ~ | ✘ | ✔ |
| Veri göndermez | ✔ | ~ | ✘ | ✔ |
| Abonelik yok | ✔ | ~ | ✘ | ✔ |
| Türkçe | ✔ | ✘ | ~ | ✔ |
| Fiyat | 2.999 TL | 5.400–6.800 TL | ≈10.000 TL+ | ≈1.600 TL |

## Slayt 8 — İş modeli ve finans

- Başlangıç seti **2.999 TL** · ek figür paketi **449 TL** · okul öncesi seti (5 cihaz).
- Birim katkı payı ≈**1.140 TL** (%46). Sunucu maliyeti yok. LTV/CAC ≈2,9.
- Kanallar:
  1. ön kayıt ve kitle fonlama (600+ set),
  2. web ve pazaryerleri,
  3. anaokulları,
  4. perakende,
  5. yurt dışı.
- Projeksiyon:
  - satış: proje döneminde 1.000 set → 5. yılda 32.000 set; 6,5 yılda 86.000 set;
  - FAVÖK 2. ticari yılda pozitif.

## Slayt 9 — 18 aylık plan ve 1.350.000 TL'nin kullanımı

| Ay | Kilometre taşı |
|---|---|
| 1–2 | Şirket, fikri mülkiyet devri, kartta hız/ses/pil ölçümleri ve optimizasyon |
| 3–4 | Kendi devre kartımız (EVT), marka/tasarım başvurusu |
| 5–7 | 60 cihazlık pilot serisi; 30–50 aile + 3–5 anaokulu pilotu (etik kurul onayı önceden) |
| 8–9 | DVT, ön uygunluk testi |
| 12 | Kitle fonlama (≥600 ön sipariş) |
| 15–17 | CE/RED belgeleri, ilk 1.000 set |
| 18 | Satış |

Bütçe dağılımı: personel %54, hizmet alımı %29, malzeme %11, teçhizat %4, seyahat %2. Kalıp ve tam belgelendirme
ön satış ve devam yatırımıyla karşılanır.

## Slayt 10 — Ekip ve istek

- [AD SOYAD] — kurucu, teknik lider (yapay zekâ, gömülü yazılım).
- [AD SOYAD / aranıyor] — donanım ve üretim.
- Danışmanlar: çocuk gelişimi, pazarlama.
- **İstek:** [Hızlandırma programına kabul / TÜBİTAK BİGG Fonu tohum öncesi yatırımı]. Sonrasında BiGG+ tohum
  turu.
- Kapanış cümlesi: *"Yapay zekâyı çocuklara, verilerini almadan ulaştırmak istiyoruz."*

---

## Sık sorulabilecek sorular ve kısa cevaplar

- **"Küçük model saçmalarsa?"** 5 aday üretilir, seçici en iyisini seçer. Başka figür adları süzgeçle
  engellenir; her figürün kapalı bir dünyası var. Kalite veriyle artıyor ve kör kıyasla ölçülüyor. Bugünkü
  kıyaslarda hakemler yapay zekâ; pilotta ebeveynlerle insan hakemli kör test yapıp kabul eşiğini (≥%90 uygun)
  doğrulayacağız. Hikâyeler kısa: ortalama ≈75 sözcük, ≈45–60 sn.
- **"Hız yeterli mi?"** Hikâyeler boştayken önceden yazılıp kuyrukta saklanıyor; oyuncak konunca bekleme yok. Hazır
  hikâye yoksa cihaz yazarken okuyor. Hız ilk gerçek kart testinde ölçülecek. Ses sentezinin optimizasyonu
  planlı.
- **"Neden bulut değil?"** Gizlilik, güvenlik, sıfır işletme maliyeti ve şirket kapansa da çalışan ürün. Bu,
  ebeveynin en büyük kaygısına doğrudan cevap.
- **"Büyükler (tonies) yaparsa?"** Türkçe pazar onlar için küçük. Cihaz içi model ayrı bir uzmanlık istiyor.
  Bizim veri setimiz, hakem sürecimiz ve figür ekosistemimiz var. Önce pazara çıkıp kurumlarla ilişki
  kuracağız.
- **"Lisanslı karakterler?"** Bilinçli olarak çıkardık: halk figürleri ve kendi karakterlerimiz. Satış verisiyle
  yerli marka sahipleriyle lisans görüşeceğiz.
- **"Fikri mülkiyet kimde?"** Kod, modeller, veri ve tasarımlar kurucuda. Şirket kurulunca bedelsiz devredilecek.
  Açık kaynak bileşenler (MIT, Apache-2.0, CDLA) ticari kullanıma uygun ve envanteri hazır.

## 1 dakikalık tanıtım (asansör konuşması)

"3–6 yaşındaki çocuğu olan her ebeveyn iki şey istiyor: çocuk ekrandan uzak dursun ve her gece yeni bir masal
dinlesin. Bugünkü ses oyuncakları hep aynı kaydı çalıyor; yapay zekâlı oyuncaklar ise çocuğun sesini sunuculara
gönderiyor. Bu yüzden skandallar yaşandı. Eko, bu ikisinin arasındaki boşluğu dolduruyor. Çocuk sevdiği figürü
Eko'nun standına koyuyor, Eko o figürle her seferinde yeni bir Türkçe hikâye yazıp kendi sesiyle okuyor. Bütün
yapay zekâ, avuç içi kadar bir kartın içinde çalışıyor: internet yok, kayıt yok, abonelik yok. Modelimizi 28 bin
özgün hikâyeyle eğittik, kaliteyi kör testlerle ölçtük. Şimdi ailelerle pilotu yapıp ürünü CE belgeli olarak
satışa çıkarmak istiyoruz. Eko'yu 2.999 TL'ye, ithal rakiplerinin yarı fiyatına satacağız."
