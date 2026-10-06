# Pazar, hukuk ve maliyet araştırması: internetsiz Türkçe hikâye oyuncağı

> 6 Ekim 2026. Web araştırmasıyla hazırlandı. Teknik rakamlar depodaki `docs/ESP32_BUTCE.md`,
> `docs/SES_ARASTIRMASI.md` ve `degerlendirme/urun_kiyas_karma/OZET.md` belgelerinden alındı.
>
> **İşaretler:** **[D]** kaynağıyla doğrulanmış bilgi. **[T]** tahmin ya da yorum (gerekçesi yazılı).
> **[?]** doğrulanamadı, kontrol edilmesi gerekiyor. Kur için **1 USD ≈ 49 TL** alındı (1 Ekim 2026,
> [hisse.net](https://www.hisse.net/haber/dolar-ve-euro-bugun-ne-kadar-kac-tl-1-ekim-guncel-doviz-kurlari-99449)).
> Bu belge hukuki görüş değildir. Lisans ve uygunluk kararlarından önce fikrî mülkiyet avukatına ve akredite
> bir test laboratuvarına danışılmalıdır.

---

## Yönetici özeti

1. **Lisanslı karakterlerle satış bugünkü haliyle yapılamaz.** Demodaki 11 figürün 10'u başka şirketlere ait:
   Niloya (Kaynak Licensing), Pepee (Düşyeri), Kral Şakir (Grafi2000), Hayri / Rafadan Tayfa ve Doru (TRT ortak
   yapımları), Maşa (Animaccord), Elsa ve Örümcek Adam (Disney/Marvel), Hello Kitty (Sanrio), Chase (Spin Master).
   Bu figürlerin adını, kişiliğini ya da dünyasını kullanarak yeni hikâye üretmek **işleme eser** sayılır. Ürünü bu
   adlarla pazarlamak da **marka kullanımıdır**. İkisi de hak sahibinin izni olmadan yapılamaz. Tek istisna
   **Keloğlan**: halk masalı figürü olarak serbest kullanılabilir, ama TRT çizgi filmindeki tasarım ve yan karakterler
   kullanılamaz. Bu karakterler yalnızca kapalı Ar-Ge demosunda kalmalı; kampanya, fuar ve satışta yer almamalı.
2. **Önerilen yol:** İlk ürünü **kendi özgün karakterlerimiz ve halk figürleriyle** (Keloğlan, Nasreddin Hoca,
   Dede Korkut, Karagöz ile Hacivat, hayvan masalları) çıkarmak. Ürün tutunursa, ikinci adımda tek bir yerli marka
   için lisans görüşülür (Kaynak/Niloya ya da TRT). Tipik telif payı toptan satış fiyatının **%8–12'si**, buna ek
   olarak asgari garanti ödemesi istenir **[T]**.
3. **Rakipler iki gruba ayrılıyor.** (a) **Kartlı ya da figürlü ses oynatıcılar:** Toniebox (2025 cirosu 630 M€),
   Yoto, Storypod. Bunlar hazır içerik çalar, LLM kullanmaz. (b) **Bulut LLM'li yapay zekâ oyuncakları:** Miko,
   Curio, FoloToy, Fawn, Bondu. Bu ikinci grup 2025–2026'da arka arkaya skandallarla anıldı: FoloToy'un OpenAI
   erişimi kesildi, Bondu'da yaklaşık 50 bin çocuk sohbeti açıkta kaldı, Moxie sunucular kapanınca çalışmaz oldu,
   Mattel ile OpenAI ürünlerini erteledi. "**Her seferinde yeni hikâye yazan ama hiç veri göndermeyen**" ürün bu iki
   grubun arasındaki boşluğa denk geliyor.
4. **Pazar:** Türkiye oyuncak pazarı yaklaşık **1 milyar USD** ve %85'i ithal **[D]**. E-ticaret hacmi 2025'te
   4,57 trilyon TL'ye ulaştı **[D]**. Trendyol'un oyuncak komisyonu yaklaşık **%18** **[D]**. Yerli, ekransız ve
   yapay zekâlı ses cihazı alanında ciddi bir rakip **Elaves Sunny** (0–5 yaş, CES ödüllü, ABD odaklı) **[D]**.
5. **Birim maliyet (BOM, montaj dahil) [T]:** 1.000 adetlik üretimde **≈17–22 USD**. Kalıp ve sertifika payı
   eklenince **≈30–45 USD**. 10.000 adette **≈12–15 USD**, Türkiye'ye teslim maliyeti **≈18–23 USD**.
6. **Önerilen raf fiyatı [T]:** **2.499–3.499 TL** (KDV dahil, 2–3 karakter jetonuyla), ek karakter paketi
   349–499 TL. Karşılaştırma için konuşan lisanslı Pepee peluşları 4.700–9.999 TL **[D]**. 10 bin adet ölçeğinde
   Trendyol üzerinden brüt katkı birim başına ≈730–925 TL çıkar (net satışın ≈%30–37'si). 1.000 adette ancak başa baş noktasına gelinir.
7. **En büyük ürün riski hikâye kalitesi.** Rubrik puanı **4,51/10** ve "mantık ve dil kusurları hâlâ hemen her
   hikâyede var" (`OZET.md`). Satışa çıkmadan önce kalite eşiği tanımlanmalı, ebeveynlerle kör testte ölçülmeli
   ve en kötü durum için içerik güvenliği garanti altına alınmalı.
8. **Uygunluk:** CE kapsamında EN 71-1/2/3 ve EN IEC 62115 gerekiyor. NFC okuyucu ya da BLE kullanıldığı için
   **RED (Telsiz Ekipmanları) de devreye girer**: 13,56 MHz okuyucu da bir verici sayılır. Bunlara ek olarak pil
   (IEC 62133, UN 38.3), RoHS, AEEE ve atık pil kayıtları gerekir. Ses dosyası için "yapay zekâ ile üretilmiştir"
   ibaresi zorunlu. Veri toplanmaması KVKK ve GDPR açısından büyük bir avantaj.

---

## 1. Rakipler ve benzer ürünler

### 1.1 Dünya: kartlı ya da figürlü ses oynatıcılar (LLM yok)

| Ürün | Fiyat | İş modeli | Bulut LLM | Not |
|---|---|---|---|---|
| **Toniebox 2** (tonies SE, DE) | 119,99 € / 139,99 USD'den başlayan başlangıç setleri **[D]** | Tonie figürü başına içerik (≈15 £), Tonieplay oyunları | Yok. Kurulum için Wi-Fi gerekir, sonra çevrimdışı çalışır | 2025 cirosu **630 M€** (+%31), Toniebox kategorisi 161 M€ **[D]** ([basın bülteni](https://tonies.mynewsdesk.com/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442746), [Yahoo](https://tech.yahoo.com/audio/articles/toniebox-2-everything-know-screen-163912590.html)). 10 yılda ≈12 M cihaz ve 150 M figür satıldı **[D]** ([theSun/AFP](https://thesun.my/news/world-news/parents-turn-to-audio-toys-to-cut-kids-screen-time/)). 2024'te İngiltere'de 1.000 kullanıcıyla **yapay zekâ hikâye üreticisi** denedi, ama üretim bulutta yapılıyor **[D]** ([tonies](https://tonies.mynewsdesk.com/pressreleases/tonies-r-explores-ai-based-content-generator-in-a-test-with-up-to-1000-users-3276746)). |
| **Yoto Player / Mini 4. nesil** (UK) | Player 119,99 £ / 149,99 USD, Mini 89,99 £ / 109,99 USD **[D]** | Kart başına içerik, Yoto Club aboneliği (ayda ≈8–10 £), boş "Make Your Own" kartlar (10'lusu 25 USD) | Yok. 64 GB depo, çevrimdışı dinleme | 2024 cirosu ≈95 M £ **[D]** ([Tom's Guide](https://www.tomsguide.com/audio/yoto-player-4th-gen-unveiled-with-green-button-playlist-feature-and-theres-a-new-yoto-mini-player-too), [TechAdvisor](https://www.techadvisor.com/article/722040/yoto-player-review-audio-content-for-kids.html), [theSun](https://thesun.my/news/world-news/parents-turn-to-audio-toys-to-cut-kids-screen-time/)) |
| **Storypod** (US) | 99,99 USD, başlangıç seti 75 USD **[D]** | Örgü "Craftie" figürleri ve RFID, lisanslı içerik (Gruffalo vb.) | Yok | Figür ve RFID modeli bize en yakın donanım örneği ([TTPM](https://ttpm.com/products/storypod-the-magical-storyteller-audio-characters-trivia-cards-and-book/)) |

**Ders:** Bu kategorinin parası cihazdan değil **figür ya da kart satışından** geliyor. Tonies 150 M figür satmış.
Bizim jeton ya da figür modelimiz bu düzeni kopyalayabilir; tek fark içeriğin cihazda üretilmesi.

### 1.2 Dünya: yapay zekâ oyuncakları (bulut LLM)

| Ürün | Fiyat | Model | Olay ya da tartışma |
|---|---|---|---|
| **Miko 3** (Hindistan/ABD) | 199–299 USD, **Miko Max** aboneliği ayda 15 USD ya da yılda 99 USD **[D]** ([miko.ai](https://miko.ai/products/miko-3), [App Store](https://apps.apple.com/app/id1588895826)) | Bulut yapay zekâ ve lisanslı Disney içeriği | Abonelik olmadan içeriğin büyük kısmı kapalı |
| **Curio Grem / Grok / Gabbo** (ABD) | 99 USD, 60 gün "Curio Plus" dahil **[D]** ([Axios](https://www.axios.com/2023/12/14/grimes-chat-gpt-artificial-intelligence-toy), [Freethink](https://www.freethink.com/robots-ai/ai-toy-grok)) | OpenAI GPT ve uygulama | Ses kaydı ve transkript bulutta tutuluyor |
| **FoloToy Kumma** (Singapur/Çin) | ≈99 USD **[?]** | OpenAI API | PIRG raporunda cinsel içerik ve bıçak tarifi verdi. **OpenAI geliştiricinin erişimini kesti**, ürün geçici olarak satıştan çekildi (Kasım 2025) **[D]** ([Notebookcheck](https://www.notebookcheck.net/ChuckyGPT-AI-teddy-bear-for-toddlers-gives-dangerous-answers-OpenAI-blocks-it.1166685.0.html), [WALB/PIRG](https://www.walb.com/2025/12/12/consumer-safety-report-warns-disturbing-responses-ai-powered-toys/), [ekonomim](https://www.ekonomim.com/gundem/skandal-oyuncak-yapay-zekali-ayi-raflardan-cekildi-haberi-855867)) |
| **Bondu** (ABD) | – | Bulut LLM | Ocak 2026'da herhangi bir Gmail hesabıyla girilebilen bir konsolda **≈50.000 çocuk sohbeti** (ad, doğum tarihi, aile bilgileri) açıkta kaldı **[D]** ([Malwarebytes](https://www.malwarebytes.com/blog/news/2026/02/an-ai-plush-toy-exposed-thousands-of-private-chats-with-children), [OECD AI](https://oecd.ai/en/incidents/2026-01-29-5f44)) |
| **Moxie** (Embodied, ABD) | 799 USD (çıkışta 1.500) **[D]** | Tamamen bulut | Şirket Kasım 2024'te kapandı, **sunucular 30 Ocak 2025'te kapatılınca robotlar çalışmaz oldu**. Daha sonra gönüllüler OpenMoxie ile kısmen canlandırdı **[D]** ([PIRG](https://pirg.org/articles/moxie-robot-open-source/)) |
| **Fawn Friends** | 399 USD + ayda 30 USD **[D]** ([letsdatascience](https://letsdatascience.com/news/fawn-friends-plushie-uses-ai-to-model-friendship-c1f9ead9)) | Bulut | "Yapay arkadaşlık" etiği tartışması |
| **Mattel + OpenAI** | – | – | Ortaklık Haziran 2025'te duyuruldu. İlk ürün 2025'te çıkmadı, "daha büyük yaş ve aileler" hedefleniyor, çünkü OpenAI API 13 yaş altını desteklemiyor **[D]** ([Axios](https://www.axios.com/2025/12/15/mattel-openai-toys-kids), [PIRG](https://pirg.org/media-center/statement-mattel-openai-delay-ai-product-launch-as-senators-demand-transparency-from-toy-companies/)) |
| **Poe the AI Story Bear** (Skyrocket) | – | OpenAI, hikâye uygulamada üretilip ayıya aktarılıyor | Mikrofon yok, ama yine de uygulama ve bulut gerekiyor ([CO/AI](https://getcoai.com/news/ai-powered-toy-bear-can-tell-stories-in-over-30-languages)) |

**Çevrimdışı emsal:** Hindistan'da 8 yaşında bir çocuğun ESP32 üzerinde TinyStories ile yaptığı internetsiz hikâye
cihazı haberlere çıktı **[D]** ([Analytics Insight](https://www.analyticsinsight.net/news/8-year-old-builds-rs-760-ai-device-that-works-offline)).
Yani fikir teknik olarak yeni değil. **Ticari olarak Türkçe yapılmış bir örneği ise bulamadık [?]**.

### 1.3 Türkiye

| Ürün | Fiyat (TL) | Not |
|---|---|---|
| **Elaves Sunny** (yerli, Elaves Eğitim ve Teknoloji) | Belirtilmemiş **[?]** | 0–5 yaş, ekransız, "salla-dinle-oyna", internetsiz de çalışıyor. Yapay zekâ içerik üretiminde **arka planda** kullanılıyor, çocukla doğrudan konuşmuyor. CES inovasyon ödülü var, ABD'de 100 bin adet hedefliyor **[D]** ([Ekonomist, 4 Tem 2026](https://www.ekonomist.com.tr/makale/ekransiz-ogrenmeyle-globale-acilacak-75916), [Posta](https://www.posta.com.tr/yazarlar/murat-gulderen/ekran-bagimliligini-bitiren-cihaz-2989545)). **En yakın yerli rakip.** |
| Lisanslı konuşan Pepee peluşları (Trendyol) | 4.700 ve 9.999 TL **[D]** ([Trendyol arama](https://www.trendyol.com/pepee-x-b792)) | Sabit kayıtlı replikler. Lisanslı ses oyuncağının raftaki fiyatını gösteren iyi bir çıpa. |
| Niloya bebek ve figürleri | Figür ≈400 TL, bebek < 2.000 TL'den başlıyor **[D]** ([akakce](https://www.akakce.com/et-bebek/niloya.html)) | |
| "Türkçe konuşan, masal anlatan" robotlar (Astro vb.) | ≈1.550–1.600 TL **[D]** ([idefix](https://www.idefix.com/turkce-konusan-sesli-isikli-muzikli-4-farkli-sarki-3-farkli-masal-soyleyebilen-yuruyen-oyuncak-robot-p-28830482)) | 3 sabit masal, düşük kalite. Fiyat tabanını gösteriyor. |
| Eilik masaüstü yapay zekâ robotu (Trendyol) | 10.999 TL **[D]** ([Sözcü](https://www.sozcu.com.tr/yapay-zeka-destekli-konusan-oyuncaklar-piyasaya-cikiyor-p13077)) | Üst segment |
| Miko 3, Toniebox, Yoto | Resmî Türkiye distribütörü bulunamadı. Trendyol'da yurt dışı satıcı ilanları var **[?]** | Kurla çevrilmiş fiyatlar: Yoto Mini ≈5.400 TL, Toniebox 2 ≈6.800 TL **[T]** |

---

## 2. Pazar büyüklüğü ve trendler

- **Türkiye oyuncak pazarı ≈1 milyar USD.** Bunun ≈700 M USD'si ithal, ≈200 M USD'si yerli üretim, ihracat ≈100 M
  USD. Pazar %85 ithalata bağımlı, ithalatın %82,5'i Çin'den **[D]** (TOYDER Başkanı Raşit Akar,
  [Bloomberg HT](https://www.bloomberght.com/turkiye-oyuncak-pazari-1-milyar-lirayi-asti-1180261),
  [Sözcü](https://www.sozcu.com.tr/oyuncaklara-test-darbesi-wp2023047)). Yıl tam olarak belirtilmemiş,
  2024–2025 dönemi olarak okunmalı.
- **E-ticaret:** 2025 hacmi **4,57 trilyon TL** (+%52,2), perakende e-ticaret 2,46 trilyon TL **[D]**
  ([Ticaret Bakanlığı / Alomaliye](https://www.alomaliye.com/2026/05/12/turkiyede-e-ticaret-hacmi-2025te-4-6-trilyon-liraya-ulasti/)).
  Oyuncak alt kırılımı yayımlanmıyor.
- **Pazaryeri maliyeti:** Trendyol oyuncak komisyonu **≈%18** **[D]**
  ([ideasoft](https://www.ideasoft.com.tr/trendyol-komisyon-oranlari/)). Buna kargo, iade ve reklam eklenince
  satış maliyeti brüt cironun **%25–30'unu** bulur **[T]**.
- **Dünyada ses oyuncakları:** Tonies 630 M€ ve Yoto ≈95 M £ (2024). İki şirket de %30'un üstünde büyüyor. Büyümeyi
  ebeveynlerin "ekran süresi" kaygısı sürüklüyor **[D]**
  ([theSun/AFP](https://thesun.my/news/world-news/parents-turn-to-audio-toys-to-cut-kids-screen-time/)).
- **Yapay zekâ oyuncakları:** Küresel "AI smart toy" pazarının yıllık yaklaşık %14,6 büyümesi bekleniyor
  (2024–2030). Çin'de AI oyuncak pazarının 2025'te 24,6 milyar yuan (≈3,5 milyar USD), 2030'da 85 milyar yuan
  olacağı tahmin ediliyor **[D, ama danışmanlık şirketi tahmini]**
  ([Lucintel](https://lucintel.com/ai-smart-toy-market.aspx), [tech.az/AskCI](https://tech.az/en/posts/china-s-ai-toy-market-projected-to-hit-12b-by-2030-6404)).
- **Türkiye'de fiyat bantları [T]** (yukarıdaki ilanlardan çıkarıldı):
  - giriş seviyesi elektronik ve sesli oyuncak: 800–1.600 TL,
  - lisanslı konuşan peluş: 4.700–10.000 TL,
  - ithal ses oynatıcı: 5.000–7.000 TL,
  - yapay zekâ robotu: 10.000 TL ve üstü.

  **2.500–3.500 TL bandı boş görünüyor.** Bu banttaki ürün hem "ithal ses kutusundan ucuz" hem de "sabit masallı
  oyuncaktan çok daha zengin" diye konumlanabilir.
- **İthalat engeli:** Oyuncaklar "riskli ürün" grubunda yer alıyor. Posta ve hızlı kargoyla basitleştirilmiş beyan
  kullanılamıyor, her parti için TAREKS denetimi gerekiyor **[D]**
  ([Corpenza](https://corpenza.com/2026-cinden-turkiyeye-ithalat-rehberi),
  [SGS](https://www.sgs.com/news/2026/01/safeguards-00426-turkey-publishes-import-controls-for-toys-and-other-consumer-goods)).
  2026'nın ilk yarısındaki denetimlerde oyuncak grubunda uygunsuz ürün oranı %4 çıktı **[D]**. Çin menşeli 9503
  GTİP'li ürünlerde ilave gümrük vergisinin güncel oranını gümrük müşavirine teyit ettirmek gerekiyor **[?]**.

---

## 3. Hukuk ve uygunluk

### 3.1 Karakter lisansı (en kritik konu)

**Neden izin gerekiyor? [T, genel hukuk bilgisi, avukat teyidi gerekli]**

- **Çizgi karakterler FSEK kapsamında eser.** Görünüş, kişilik ve adın bütünü korunuyor.
- **Karakterle yeni hikâye üretmek işleme eserdir.** İşleme hakkı (FSEK md. 21) hak sahibine ait; izinsiz işleme
  hukuki ve cezai sorumluluk doğurur (FSEK md. 71).
- **Karakter adları genellikle sınıf 9, 16, 28 ve 41'de marka olarak tescilli.** Ürünü "Niloya hikâyeleri anlatır"
  diye pazarlamak ya da ambalaja Elsa yazmak SMK kapsamında marka ihlalidir.
- **Görsel şart değil.** Ekran ya da figür kullanılmasa bile, yalnızca ad ve kişilikle "Pepee'li yeni hikâye"
  satmak da risklidir.
- **Uluslararası markalar pazaryerlerini sıkı takip ediyor.** Disney ve Marvel, ABD'de yüzlerce satıcıya tek davada
  ("Schedule A") ihtiyati tedbir ve hesap dondurma kararı aldırıyor **[D]**
  ([Vondran](https://www.vondranlegal.com/disney-ip-defense)). Trendyol ve Hepsiburada da hak sahibi şikâyetiyle
  ilanı kaldırıyor **[T]**.

**Kime başvurulur?**

| Figür | Hak sahibi ya da lisans muhatabı | Durum |
|---|---|---|
| **Niloya** | **Kaynak Licensing Company (KLC)**: dünya genelinde tek yayın ve lisans-ürünlendirme hak sahibi. Yapımcı Bee & Bird Animation **[D]** | Oyuncak lisansı daha önce Play And Learn Toys'a 3 yıllığına verilmişti, LC Waikiki ile giyim anlaşması var **[D]** ([Licensing Intl.](https://licensinginternational.org/news/klc-appoints-toy-licensee-for-niloya/), [License Global](https://www.licenseglobal.com/toys-games/kaynak-finds-niloya-toy-partner)). **Yerli lisans için en gerçekçi muhatap.** |
| **Pepee** | **Düşyeri** (Ayşe Şule Bilgiç ve ortakları) **[D]** ([Wikipedia](https://en.wikipedia.org/wiki/Pepee)) | Düşyeri, TRT'den bağımsız bir yapımcı (2013'te TRT ile sözleşme yenilenmemişti, [Sözcü](https://www.sozcu.com.tr/pepee-issiz-kaldi-wp390133)). Düşyeri doğrudan aranmalı. |
| **Kral Şakir** | **Grafi2000** (Varol Yaşaroğlu), Cartoon Network Türkiye için üretiliyor **[D]** ([İstiklal](https://www.istiklal.com.tr/kultur-sanat/cizgi-karakter-kral-sakirin-tasarimcisi-amacim-dunyada-markalasmak-743322h)) | Güçlü bir lisans programı var. Yayın tarafında Warner Bros. Discovery hakları da olabilir **[?]** |
| **Hayri (Rafadan Tayfa)** | **TRT ve ISF Studios ortak yapımı** **[D]** ([Wikipedia](https://en.wikipedia.org/wiki/Rafadan_Tayfa)) | TRT, 2018'de Rafadan Tayfa dahil 11 TRT Çocuk karakteri için Adel Kalemcilik'e oyuncak ve kırtasiye lisansı verdi **[D]** ([Marketing Türkiye](https://marketingturkiye.com.tr/?p=48241)). Yani TRT doğrudan lisans veriyor. Başvurunun hangi birime yapılacağı web'de bulunamadı; TRT kurumsal iletişim ya da ticari işler birimine yazılmalı **[?]** |
| **Doru** | **TRT ortak yapımı** (yapımcı tarafında Alper Afşin Özdemir adı geçiyor) **[D]** ([haber7](https://www.haber7.com/medya/haber/3348172-trt-ortak-yapimi-doru-macera-adasi-30-agustosta-vizyona-girecek)) | Lisans hakkının TRT'de mi yapımcıda mı olduğu sözleşmeye bağlı **[?]** |
| **Maşa** | **Animaccord** (Kıbrıs). Türkiye ajanı **Lisans A.Ş.** **[D]** ([Animaccord](https://animaccord.com/news/consumer-products/new-consumer-products-are-in-the-spotlight-in-turkey.html), [Toybook](https://toybook.com/animaccord-inks-new-licensing-agents-for-masha-and-the-bear)) | |
| **Hello Kitty** | **Sanrio**. Türkiye ajanı Max Licensing; World Space Licensing de Türkiye'de Hello Kitty projeleri yürütüyor **[D]** ([License Global](https://www.licenseglobal.com/licensing-resources/istanbul-says-hello-kitty-and-happy-birthday), [License Global](https://www.licenseglobal.com/location-based-entertainment/world-space-licensing-launches-immersive-hello-kitty-experience-in-turkey)) | |
| **Elsa, Örümcek Adam** | **Disney** (Marvel) | Küçük bir girişimin yapay zekâ ile serbest hikâye ürettiği bir ürüne Disney'in lisans vermesi **pratikte beklenmemeli [T]**: içerik kontrolü, marka güvenliği ve asgari garanti engelleri var. |
| **Chase (PAW Patrol)** | **Spin Master** | Türkiye ajanı doğrulanamadı **[?]**. Disney'e benzer şekilde zor **[T]**. |
| **Keloğlan** | **Halk masalı, anonim** | Aşağıya bakınız. |

**Lisansın tipik koşulları [T, sektör kaynaklarından]:**

- Telif payı, lisans sahibinin toptan (net) satış fiyatı üzerinden **%5–15**. Eğlence ve karakter mülklerinde
  ortalama ≈**%9,7**, A sınıfı markalarda %20'nin üstüne çıkabiliyor **[D, ABD verisi]**
  ([License Global](https://www.licenseglobal.com/trends-insights/royalty-rights),
  [UpCounsel](https://upcounsel.com/toy-licensing-agreements)).
- **Asgari garanti (MG)** isteniyor ve genellikle %25–50'si peşin ödeniyor.
- Süre 2–3 yıl, toprak "Türkiye" ile sınırlı, kategori ("elektronik ve ses oyuncağı") dar tanımlanıyor.
- Her ürün ve her içerik için **onay süreci** var. Bu bizim için kritik bir nokta: içerik cihazda sınırsız
  üretildiği için tek tek onaylanamaz. Lisans verenin "her hikâyeyi önceden göremiyoruz" itirazına karşı içerik
  kuralları (kapalı dünya, yasak kelime listesi, karakter kartı) ve örnek bir hikâye setiyle denetim önerilmeli.
  Depodaki "kapalı dünya" ve karakter kartı kuralları (`docs/KUSURSUZ_VERI.md`) bu konuda iyi bir başlangıç.
- Türkiye'de yerli bir marka için MG'nin **birkaç yüz bin TL** düzeyinde olmasını bekliyoruz **[T]**. Görüşmeden
  önce bilinemez.

**Keloğlan'ın durumu:**

- **Masal figürü olarak Keloğlan** anonim halk edebiyatına ait. Belirli bir yazarı olmadığından FSEK korumasına
  girmez ve serbestçe kullanılabilir **[T]**.
- **TRT'nin "Keloğlan Masalları" çizgi filmi** (2008–2016, TRT Çocuk ile Anameks/Animax) ise ayrı bir eser
  **[D]** ([Marmara Üniv.](https://kutuphane.marmara.edu.tr/dosya/kutuphane/form-files/382//1584008399.pdf),
  [memurlar.net](https://www.memurlar.net/haber/754964/feto-nun-caillou-su-keloglan-i-zarar-ettirdi.html)).
  Bu dizinin **karakter tasarımı**, dizide yaratılan yan karakterler (ör. **Bilgecan Dede**) ve görselleri TRT ile
  yapımcıya ait.
- **Karar:** Keloğlan kullanılabilir, ama kendi çizimimizle, masal geleneğindeki yan figürlerle (anası, padişah,
  dev, cadı) ve TRT'yi çağrıştırmayan bir ambalajla.
- Ayrıca "Keloğlan" adının **sınıf 28'de (oyuncak) marka olarak tescilli olup olmadığına** TÜRKPATENT
  veritabanında bakılmalı **[?]**. Tescilli ise ürün adı farklı tutulup Keloğlan yalnızca hikâye içinde
  kullanılmalı.
- Aynı mantık **Nasreddin Hoca, Dede Korkut, Karagöz ile Hacivat, Köroğlu ve Tepegöz** için de geçerli. Bunların
  da yalnızca belirli bir modern uyarlamasının tasarımı korumalı.

**Pratik sonuç:**

1. Ürün **v1'i özgün karakterlerle** (ör. bir kedi, bir kaplumbağa, bir bulut) ve **halk figürleriyle** çıkmalı.
   Kendi karakterlerimiz için **TÜRKPATENT'e marka başvurusu** (sınıf 9, 16, 28, 41) yapılmalı.
2. Lisanslı figürler **halka açık demo, kampanya videosu, fuar ve Trendyol görsellerinde kullanılmamalı.**
3. Modelin eğitim verisinde lisanslı karakter adları var. Ürün modeli **özgün karakterlerle yeniden ince ayardan
   geçirilmeli** ve lisanslı adlar isim süzgecinde yasaklanmalı. Depodaki veri hattı (`urun_v3` hafif hat ile
   10 bin hikâye) bunu yaklaşık aynı maliyetle yapabilir.
4. Lisans görüşmesi (Kaynak/Niloya ya da TRT) ilk satış verisi elde olunca açılmalı. Gösterilecek kanıt: "X bin
   adet sattık, veri toplamıyoruz, içerik kurallarımız şunlar."

### 3.2 Oyuncak güvenliği ve CE (Türkiye ve AB)

| Konu | Gereklilik | Not |
|---|---|---|
| **Oyuncak Güvenliği Yönetmeliği** (2009/48/AT uyumu, RG 4.10.2016/29847) | CE işareti, teknik dosya, AB/AT uygunluk beyanı, Türkçe uyarılar, üretici ya da ithalatçı adresi **[D]** ([Alomaliye](https://alomaliye.com/2016/10/04/oyuncak-guvenligi-yonetmeligi/)) | Piyasa gözetimini **Ticaret Bakanlığı** yapıyor; usulsüz CE kullanımı ürünün toplatılmasına kadar gidebilir **[D]** ([Ticaret Bak.](https://ticaret.gov.tr/haberler/ce-isaretini-oyuncaga-usulsuz-i̇listirenlere-siki-takip)). TSE belgesi zorunlu değil, CE ve akredite laboratuvar raporları esas. |
| **EN 71-1 / -2 / -3** | Mekanik ve fiziksel güvenlik, yanıcılık, ağır metal göçü | 3–6 yaş ürünü olsa da küçük parça (jeton, figür) riski 36 ay altı için değerlendirilmeli. "0–3 yaş için uygun değildir" uyarısı ancak ürün gerçekten 3 yaş altına yönelik değilse kullanılabilir. |
| **EN IEC 62115** (elektrikli oyuncaklar) | Pil bölmesi vidası **tutsak (captive)** olmalı. Küçük parça silindirine sığan pillere alet kullanmadan erişilememeli. Şarjlı piller **IEC 62133** uyumlu olmalı **[D]** ([QIMA](https://blog.qima.com/lab-testing/guide-to-en-iec-62115-standard), [STC](https://stc.group/en/media/detail/1410)) | Li-ion hücre için ayrıca UN 38.3 taşıma testi ve MSDS gerekir. |
| **RED** (Türkiye'de BTK'nın Telsiz Ekipmanları Yönetmeliği) | **NFC okuyucu (13,56 MHz) ya da BLE varsa EMC ve LVD yerine RED uygulanır.** Gerekli testler: EN 300 330 (NFC), EN 300 328 (BLE), EN 301 489-1/-3/-17, EN 62479 | **Önemli:** Wi-Fi kapalı olsa bile NFC okuyucu bir telsiz vericisidir **[T, laboratuvar teyidi gerekli]**. |
| **RED siber güvenlik** (DA 2022/30, 1.8.2025'ten itibaren, EN 18031) | 3.3(e) maddesi **kişisel veri işleyebilen telsizli oyuncakları** internet bağlantısı olmasa da kapsar **[D/T]** ([BSI](https://www.bsigroup.com/siteassets/pdf/en/products-and-services/bsi_radio_equipment_directive-cybersecurity_faq_flyer_a4_241014.pdf)) | **Tasarım önerisi:** Cihaz çocuk adı, ses ya da kullanım kaydı tutmasın. Böylece kapsam dışı kalma argümanı güçlenir. BLE ile güncelleme yapılacaksa imzalı firmware ve eşleşme güvenliği gerekir. |
| **AB Siber Dayanıklılık Yasası (CRA)** | Veri bağlantılı ürünlerde tam uygulama 11.12.2027 **[T]** | AB'ye ihracat planı varsa yol haritasına alınmalı. |
| **Yeni AB Oyuncak Güvenliği Tüzüğü 2025/2509** | 12.12.2025'te yayımlandı, **1.8.2030'da uygulanmaya başlıyor**. **Dijital Ürün Pasaportu (QR)**, yeni uyarı formatı, daha sıkı kimyasal kurallar getiriyor **[D]** ([Eurofins](https://www.eurofins.com/toys-hardlines/resources/articles/a-quick-overview-of-the-new-eu-toy-safety-regulation-eu-20252509/)) | Türkiye'nin de uyumlaştırması beklenir **[T]**. |
| **RoHS ve REACH** | Bileşen RoHS beyanları, plastikte SVHC | |
| **Pil Tüzüğü 2023/1542** (AB) | 18.2.2027'den itibaren taşınabilir pillerin **son kullanıcı tarafından çıkarılıp değiştirilebilmesi** gerekiyor **[D]** ([ComplianceGate](https://www.compliancegate.com/removable-and-replaceable-battery-requirements-european-union/)) | AB satışı için vidalı, değiştirilebilir pil bölmesi tasarlanmalı. Bu, EN 62115'in tutsak vida şartıyla uyumlu. |
| **AEEE ve atık pil** (Türkiye) | Üretici ya da ithalatçı olarak AEEE ve TAP kayıtları | |
| **TAREKS** (Çin'den bitmiş ürün getirilirse) | Her parti için ürün güvenliği denetimi **[D]** | Türkiye'de son montaj yapılırsa bitmiş oyuncak ithal edilmemiş olur, yalnızca bileşenler ithal edilir. |
| **6502 sayılı Kanun ve garanti** | Türkçe kullanım kılavuzu, 2 yıl garanti, tanıtma-kullanma kılavuzu | |

**Laboratuvar maliyeti [T]:** Türkiye ya da Shenzhen'de EN 71 (1-2-3) için ≈1.500–3.000 USD, EN 62115 ve RED
(NFC/BLE) için ≈4.000–8.000 USD, pil testleri için ≈1.000–2.000 USD. Toplam **≈7–13 bin USD**. Teklif
alınmalıdır.

### 3.3 Veri koruma ve yapay zekâ şeffaflığı

- **KVKK ve GDPR:** Cihazda mikrofon, ağ bağlantısı ya da kayıt yoksa **kişisel veri işlenmez**. Bu durumda
  aydınlatma metni ve açık rıza yükü, VERBİS kaydı ve veri ihlali riski ortadan kalkar. KVKK 2026'yı çocuk
  verilerine ayırdı ve "akıllı cihazlar" uyarıları yayımladı **[D]**
  ([Cumhuriyet](https://www.cumhuriyet.com.tr/turkiye/kvkk-den-cocuklarin-kisisel-verileri-icin-uyari-gizlilik-ve-guvenlik-ayarlarini-duzenleyiniz-2431879),
  [Alomaliye](https://www.alomaliye.com/2026/09/30/akilli-cihaz-kullanicilarina-10-temel-oneri/)).
  Bu bir pazarlama avantajı. **İlke olarak çocuk adının bile cihaza yazılmaması** önerilir. Gerekirse ad, jetona
  bağlı bir takma ad olarak tutulmalı.
- **Seslendirme sanatçısı:** Difon kaydı yapılacak sanatçıdan **yazılı hak devri ve KVKK açık rızası** alınmalı
  (`SES_ARASTIRMASI.md`).
- **Yapay zekâ beyanı:**
  - Supertonic lisansı ambalajda ya da kılavuzda "Bu oyuncaktaki ses yapay zekâ ile üretilmiştir" ibaresini
    **zorunlu kılıyor** (Ek A(e)).
  - AB Yapay Zekâ Yasası **Madde 50** 2 Ağustos 2026'dan beri uygulanıyor. Yapay ses ve metin üreten sistemlerin
    sağlayıcıları, çıktının yapay olduğunu teknik olarak mümkün olduğu ölçüde işaretlemek zorunda **[D]**
    ([Sidley](https://datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026/),
    [artificialintelligenceact.eu](https://artificialintelligenceact.eu/transparency-rules-article-50/)).
  - Türkiye'de bağlayıcı bir yapay zekâ yasası henüz yok **[T]**. Ambalajda ve açılış anonsunda "hikâyeleri yapay
    zekâ yazar, sesi yapay zekâ ile üretilmiştir" demek hem uyumlu hem güven verici.

---

## 4. Malzeme listesi (BOM) ve birim maliyet

Kaynaklı fiyatlar **[D]**:

- ESP32-S3-WROOM-1-N16R8 LCSC'de 1.300 adet ve üstü için **3,68 USD**
  ([Lion Circuits / LCSC](https://lioncircuits.com/parts/ESP32-S3-WROOM-1-N16R8)).
- MAX98357A LCSC'de ≈**0,46 USD** ([findchips](https://origin-www.findchips.com/search/max98357aete%2Bt)).
- MFRC522 klonu LCSC'de 1.000 adet ve üstü için **0,30 USD** ([LCSC](https://www.lcsc.com/product-image/C54946590.html)).
- NTAG213 PVC kart 1.000 adet ve üstü için ≈**0,34 USD**.
- PCBA ve kalıp aralıkları için [Seeed](https://www.seeed.cc/post/how-to-find-a-good-low-volume-pcb-assembly-manufacturer)
  ve [Formlabs](https://formlabs.com/latam/blog/injection-molding-cost/) kullanıldı.

Geri kalan kalemler tahmindir **[T]**.

Not: Geliştirme kartı (DevKitC, 5–8 USD) yerine üretimde **modül** doğrudan kendi kartımıza lehimlenir.

| Kalem | 1.000 adet (USD) | 10.000 adet (USD) |
|---|---:|---:|
| ESP32-S3-WROOM-1-N16R8 modülü | 3,7–4,2 | 3,2–3,6 |
| I2S amfi (MAX98357A; yerine NS4168 kullanılırsa ≈0,2) | 0,5–1,0 | 0,3–0,5 |
| Hoparlör, 40 mm 3 W | 0,5–0,9 | 0,4–0,6 |
| Li-ion hücre 1.200–2.000 mAh, koruma devresi dahil (IEC 62133 ve UN 38.3 belgeli) | 1,5–2,5 | 1,1–1,6 |
| Şarj entegresi, USB-C, LDO, koruma | 0,4–0,7 | 0,3–0,4 |
| NFC okuyucu IC ve PCB anteni (MFRC522/FM175xx) | 0,4–0,8 | 0,3–0,5 |
| Butonlar, LED, ses ayarı, pasifler | 0,4–0,7 | 0,3–0,4 |
| PCB (2–4 katman) | 0,6–1,2 | 0,3–0,5 |
| SMT montaj, test ve 14 MB flash yazma | 1,5–2,5 | 0,6–1,0 |
| Plastik kasa (enjeksiyon parçası) ve kumaş ya da ses ızgarası | 1,2–2,0 | 0,8–1,2 |
| 3 karakter jetonu (NTAG213 ve baskılı ya da kalıp figür) | 1,0–3,0 | 0,6–1,5 |
| Kutu, kılavuz, USB kablosu | 1,2–2,0 | 0,8–1,2 |
| Son montaj, QC, %3 fire | 1,0–1,5 | 0,5–0,8 |
| **Değişken maliyet (fabrika çıkışı)** | **≈14–23** | **≈9,5–14** |
| Kalıp (alüminyum 3–6 bin USD; çelik 8–20 bin USD) / adet | 3–6 | 0,8–2 |
| Sertifika (≈7–13 bin USD) / adet | 7–13 | 0,7–1,3 |
| Navlun, gümrük, TAREKS, depo (≈%10–15) | 2–3 | 1,2–2 |
| **Türkiye'ye teslim tam maliyet** | **≈26–45** | **≈12–19** |

Notlar:

- Lisanslı karakter kullanılırsa toptan fiyatın ≈%10'u kadar telif payı ve asgari garanti eklenir. 10 bin adette
  bu birim başına ≈+2,5–4 USD eder **[T]**.
- **Üretim yeri seçenekleri:**
  - **Shenzhen anahtar teslim** (PCBA, kasa ve paketleme tek fabrikada) en ucuz seçenek. Bitmiş oyuncak olarak
    ithal edileceği için her partide TAREKS denetimi ve gümrük vergisi var.
  - **Melez model:** Shenzhen'de PCBA (ya da JLCPCB/PCBWay'de küçük seri), Türkiye'de kasa ve son montaj.
    Örneğin Çayırova, Manisa ve Bursa'daki oyuncak ve plastik üreticileri kullanılabilir. Bu modelin avantajları:
    "Yerli Üretim" etiketi (TRT'nin "Yerli Kahraman Yerli Üretim" söylemine uyar), KOSGEB/TÜBİTAK teşvikleri,
    ve bitmiş oyuncak ithalatı olmadığı için TAREKS gerekmemesi. Dezavantajı Türkiye'de kalıp ve işçiliğin
    %20–40 daha pahalı olabilmesi **[T]**.
  - Türkiye'de tam PCBA da mümkün (İstanbul ve Ankara'da EMS firmaları var), ama 1.000 adette birim maliyet daha
    yüksek olur **[T]**.

**Fiyat ve marj (10 bin adet, Trendyol) [T]:**

| | TL |
|---|---:|
| Raf fiyatı (KDV dahil) | 2.999 |
| KDV (%20) | −500 |
| Net satış | 2.499 |
| Trendyol komisyonu (%18, KDV dahil fiyattan) | −540 |
| Kargo, iade, reklam (≈%10) | −300 |
| **Markaya kalan** | **≈1.660 (≈34 USD)** |
| Teslim maliyeti (≈15–19 USD) | ≈735–930 |
| **Brüt katkı** | **≈730–925 TL (marka cirosunun ≈%44–56'sı, net satışın ≈%30–37'si)** |

- 1.000 adette teslim maliyeti 26–45 USD (1.275–2.200 TL) olduğu için ilk parti **başa baş ya da hafif zararla**
  satılır. Bu yüzden ilk partiyi **ön satışla** (kitle fonlama) finanse etmek mantıklı.
- Önerilen fiyatlar:
  - **2.499 TL:** 2 jetonlu giriş seti.
  - **2.999–3.499 TL:** 4 jetonlu set.
  - **349–499 TL:** 3 figürlü ek paket. Ek paketin maliyeti ≈1–2 USD olduğu için **yüksek marjlı tekrar gelir**
    sağlar ve abonelik gerektirmez. Ancak yeni karakterlerin modelde tanınması için firmware ve model güncellemesi
    gerekebilir (bkz. §5).

---

## 5. Cihaz içi (internetsiz) yaklaşım: artılar ve riskler

**Farklılaştırıcılar**

1. **Gizlilik tasarım gereği sağlanıyor.** Mikrofon yok, ağ yok, kayıt yok, dolayısıyla Bondu tipi bir veri
   sızıntısı olamaz. Ebeveyne verilecek mesaj tek cümle: "**Çocuğunuzun sesi ve bilgisi hiçbir yere gitmez.**"
2. **Abonelik yok, sunucu yok.** Şirket kapansa bile cihaz çalışmaya devam eder (Moxie'nin tersi). Bulut LLM
   maliyeti olmadığı için birim başına sürekli gider sıfır.
3. **Her yerde çalışır:** arabada, köyde, uçakta. Wi-Fi kurulumu yok, ebeveyn uygulaması yok.
4. **Her seferinde yeni hikâye üretir.** Yoto ve Tonies sabit içerik çalarken bu cihaz her seferinde farklı bir
   hikâye anlatır; bu sabit içerikli rakiplere karşı somut bir üstünlük.
5. **Türkçe ve yerel kültür.** Büyük rakiplerin Türkçe yatırımı yok. Keloğlan, Nasreddin Hoca ve Anadolu
   mekânları büyük rakiplerin kolayca taklit edemeyeceği bir alan.
6. **Güvenlik denetlenebilir.** Kapalı kelime dağarcığı (V=16384), yasak listesi, Bloom süzgeci ve aday seçici
   cihazda çalışıyor, bir bulut modelinin "uzun sohbette kontrolden çıkması" sorunu yok.

**Riskler ve sınırlar**

1. **Hikâye kalitesi.** Rubrik ortalaması 4,51/10. Mantık ve dil kusurları neredeyse her hikâyede var, ajanların
   yazdığı hikâyeler ise ≈9,7 alıyor (`OZET.md`). Ebeveyn tek bir saçma ya da uygunsuz hikâyeyi sosyal medyada
   paylaşabilir. **Satıştan önce yapılması gerekenler:**
   - ebeveynlerle kör bir test yapıp kabul eşiğini belirlemek (ör. "hikâyelerin %90'ı anlaşılır ve tutarlı"),
   - kötü hikâyeyi sessizce atan bir seçici ve kuyruk,
   - çok kısıtlı bir dünya (az yer, az nesne).
2. **Hız.** Yaklaşık 3,7 token/s, yani bir hikâye ≈36 saniyede yazılıyor (C3 tahmini). Kuyrukta önceden hazırlanan
   hikâyeler bekleme süresini gizliyor, ama ilk açılışta ve yeni bir figür×yer ikilisinde beklenebilir. Bekleme
   anında bir müzik ya da "hikâye düşünülüyor" anonsu çalınabilir.
3. **Ses kalitesi.** Difon ve TD-PSOLA sentezi nöral TTS kadar doğal değil. Çocuk gelişimcisi ve ebeveyn testiyle
   kabul edilebilirlik ölçülmeli.
4. **Etkileşim sınırlı.** Çocuk soru soramıyor. Bu bir güvenlik avantajı, ama "konuşan oyuncak" bekleyen
   ebeveynde hayal kırıklığı yaratabilir. Pazarlamada "**dinleme oyuncağı**" olarak konumlanmalı.
5. **Yeni karakter eklemek zor.** Model karakter bilgisini eğitimle öğreniyor. Yeni figür paketleri için USB ya da
   BLE ile model güncellemesi gerekiyor. Alternatif olarak **jetonda karakter kartı** (NTAG216, 888 B) taşınabilir,
   ama modelin bu kartı genellemesi henüz denenmedi **[T]**.
6. **Bulut rakipleri hızla ucuzluyor.** 2026'da Çin'de 30–50 USD'lik bulut AI peluşları yaygın **[T]**. Gizlilik
   avantajı ancak net anlatılırsa fiyat farkını haklı çıkarır.

---

## 6. Türkiye'ye çıkış önerileri

**Hedef kitle ve mesaj**

- **Birincil:** 3–6 yaş çocuğu olan, ekran süresinden kaygılı, şehirli ve orta ile üst gelir grubundaki
  ebeveynler (özellikle anneler).
  - Mesaj: "**Ekransız, internetsiz, her gece yeni bir Türkçe masal.**"
  - Kanıt: veri toplamama, abonelik olmaması, yerli üretim.
- **İkincil:** Özel anaokulları ve kreşler (≈"hikâye köşesi" kullanımı), çocuk kütüphaneleri, belediye çocuk
  merkezleri. Paket önerisi: 5 cihaz ve 20 jetonluk bir **okul öncesi seti**. MEB'in okul öncesi programındaki
  "dil etkinlikleri" ile ilişkilendirilebilir.
- **Hediye pazarı:** 23 Nisan, yılbaşı, karne ve bayram dönemleri. Türkiye'de oyuncak satışı bu dönemlerde
  yoğunlaşır **[T]**.

**Kanallar**

1. **Kitle fonlama ve ön satış:**
   - **Kickstarter'da Türkiye'den proje açılamıyor.** Uygun 25 ülke arasında Türkiye yok, bunun için ABD, İngiltere
     ya da bir AB ülkesinde şirket gerekir **[D]**
     ([Kickstarter](https://help.kickstarter.com/hc/en-us/articles/115005128014)).
   - Türkiye için **Fongogo** (≈90 bin üye; ödüllü, bağışlı, paylı ve borçlu modeller) ya da Arıkovanı
     kullanılabilir **[D]** ([Bloomberg HT](https://www.bloomberght.com/fongogo-iki-girisime-kitle-fonlamasi-yontemiyle-fon-topladi-2308455)).
     Gerçekçi hedef 300–800 ön sipariş **[T]**. Yerli kampanyalarda toplanan tutarlar genellikle yüz binlerce TL
     düzeyinde (ör. SOYL-GEL 175 bin TL).
   - Kendi sitemizden kaparolu ön sipariş de bir seçenek.
2. **Trendyol ve Hepsiburada:** Ana hacim kanalı. Ürün sayfasında 30 saniyelik hikâye ses örnekleri olmalı. Trendyol
   Mağaza ve "Yerli Üretim" rozetleri kullanılmalı.
3. **Kendi web sitesi:** Doğrudan satışta komisyon yok, ek paket satışı ve garanti kaydı (kişisel veri
   istemeden) yapılabilir.
4. **Fiziksel perakende (ikinci yıl):** Toyzz Shop, D&R, idefix ve kitapçılar. Raf marjı %35–50 olduğu için fiyat
   yapısı buna göre kurulmalı **[T]**.
5. **İçerik pazarlaması:** Çocuk gelişimci ve okul öncesi öğretmeni Instagram hesapları, "uyku öncesi rutin"
   videoları, ebeveyn forumları. Ayrıca veri sızıntısı haberlerine karşı "veri toplamayan oyuncak" hikâyesi basına
   anlatılabilir.
6. **Destekler:** KOSGEB Ar-Ge ve İnovasyon, TÜBİTAK 1512 BiGG, Ticaret Bakanlığı **Turquality** (ihracat aşamasında).

**Yol haritası (öneri) [T]**

| Dönem | İş | Çıktı ve karar noktası |
|---|---|---|
| **0–2. ay** | Avukatla lisans ve marka analizi. Özgün 4–6 karakter ve halk figürü seti. Modelin bu setle yeniden ince ayarı, lisanslı adların isim süzgecine eklenmesi. TÜRKPATENT marka başvurusu. | Lisanssız ürün modeli, rubrik ≥6/10 hedefi |
| **1–3. ay** | **EVT prototipi:** kendi kartımız (modül, amfi, NFC, Li-ion), 3D baskı kasa, 10 adet. Hız ve ses kartta ölçülür. | Ölçülmüş token/s, pil süresi (≥8 saat hedef) |
| **3–4. ay** | **Ebeveyn ve çocuk pilotu:** 30–50 aile, 3–5 anaokulu, 4 hafta. Kör kalite testi, kullanım günlüğü (yalnızca anket). | "Saçma ya da uygunsuz hikâye" oranı, tekrar kullanım, ödeme isteği (fiyat testi) |
| **4–6. ay** | **DVT:** kasa tasarımı, alüminyum kalıp, 100 adet. Laboratuvarda ön uygunluk testi (EN 62115, RED). Pil tedarikçisinden IEC 62133 ve UN 38.3 belgeleri. | Test raporu taslağı |
| **5–7. ay** | **Fongogo kampanyası** (özgün karakterlerle). Lisanslı karakterler hiçbir yerde yer almaz. | Ön sipariş sayısı (300+ ise devam) |
| **6–8. ay** | **Sertifikasyon:** EN 71-1/2/3, EN IEC 62115, RED (EN 300 330 / 300 328 / 301 489), RoHS. Teknik dosya, uygunluk beyanı, Türkçe kılavuz, AEEE ve TAP kayıtları. | CE işaretli ürün |
| **8–10. ay** | **PVT ve ilk parti 500–1.000 adet.** Kampanya teslimatı, ardından Trendyol ve web satışı. | İade oranı (< %5), puan (≥ 4,3) |
| **10–12. ay** | Ek figür paketleri. **Lisans görüşmesi** (Kaynak/Niloya ya da TRT) satış verisiyle. 10 bin adetlik üretim kararı. | Lisans teklifi, MG ve telif payı |
| **12. ay ve sonrası** | AB'ye açılma: Pil Tüzüğü ve CRA uyumu. Yurt dışındaki Türkçe konuşan aileler (Almanya, Hollanda) niş ama değerli bir pazar. | |

**Hemen yapılacak 5 iş**

1. Lisanslı figürleri hiçbir **dış** sunumda kullanmamak. Demo videolarını özgün karakterlerle yeniden çekmek.
2. Fikrî mülkiyet avukatından yazılı görüş almak: Keloğlan, halk figürleri ve marka araması.
3. Özgün karakter kartlarını yazmak ve modeli onlarla yeniden ince ayardan geçirmek.
4. Akredite bir laboratuvardan (TÜV, SGS, Intertek, Bureau Veritas, Türk Loydu) **NFC ve BLE dahil** test teklifi
   almak.
5. 30 ailelik kör kalite testini tasarlamak. Ürünün kaderini bu test belirleyecek.

---

### Kaynakça (ek)

- Tonies 2025 sonuçları: https://www.mynewsdesk.com/uk/tonies/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442747
- Toniebox 2 ve Tonieplay: https://www.spielwarenmesse.de/en/mag/toy-market-news/tonies-unveils-toniebox-2-tonieplay-gaming-platform-and-my-first-tonies-for-toddlers/
- Yoto 4. nesil: https://www.expressandstar.com/recommended/yoto-player-4th-gen-yoto-player-4th-generation-yoto-mini-4th-gen-yoto-mini-4th-generation-new-yoto-player-new-yoto-mini-yoto-4th-gen-9045551
- OpenAI'nin FoloToy erişimini kesmesi: https://www.folio3.ai/ai-pulse/openai-suspends-toymaker-ai-teddy-bear-inappropriate-advice-children
- Mattel ve OpenAI erteleme haberi: https://www.shopifreaks.com/mattel-delays-openai-toy-launch-amid-safety-scrutiny/
- Niloya ve Kaynak Licensing: https://www.licenseglobal.com/entertainment/niloya-heads-turkey
- Kral Şakir ve Grafi2000: https://ecchorights.com/series/king-shakir_
- Masha, Türkiye ajanı: https://www.licenseglobal.com/licensing-resources/masha-and-bear-paws-new-agents
- Oyuncak ithal denetimi: https://www.mevzuat.net/legislation/item/29873.aspx
- EN 18031 ve RED: https://iotsecurityfoundation.org/wp-content/uploads/2025/09/EUROPEAN-UNION-RADIO-EQUIPMENT-DIRECTIVE-EU-RED-EXECUTIVE-BRIEF.pdf
- AB Oyuncak Tüzüğü 2025/2509: https://www.cps.bureauveritas.com/newsroom/eu-toy-safety-regulation-20252509-published
- E-ticaret 2025: https://www.ekonomigazetesi.com/ekonomi/e-ticaret-hacmi-46-trilyon-tlye-yaklasti-74639
