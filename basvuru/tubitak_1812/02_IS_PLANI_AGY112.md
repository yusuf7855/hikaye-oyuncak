# AGY 112 – İş Planı: Eko: İnternetsiz Çalışan, Cihaz İçi Yapay Zekâlı Türkçe Hikâye Oyuncağı

> TÜBİTAK 1812 BiGG Yatırım, Aşama 2 iş planı formunun (AGY 112, v1.2) bütün alanları. Bu dosya `hazirla/icerik.py` ve `hazirla/finans.py`'den üretilir (`hazirla/doldur.py`); elle değiştirmeyin, kaynağı değiştirip yeniden üretin. Köşeli parantezli büyük harfli yerler ([AD SOYAD] gibi) sizin dolduracağınız kişisel bilgilerdir. [V] varsayım, [T] tahmin demektir.

**Tematik alan:** 1.4 İletişim ve Sayısal Dönüşüm — Yapay Zekâ (yan alanlar: Ses/Görüntü/Metin İşleme, Eğitim, Elektronik Sistemler)

## 1 Pazar Fırsatı

### 1.1 Ürün Tanımı

*(2626 / 3000 karakter)*

Eko, 3–6 yaş çocuklar için internete hiç bağlanmadan çalışan, her seferinde yeni bir Türkçe hikâye yazıp kendi sesiyle okuyan bir hikâye oyuncağıdır. Çocuk sevdiği figürü (Keloğlan, Nasreddin Hoca, Pinokyo, kendi tasarımımız Bulut kedi, Zıpzıp tavşan, Bip robot vb.) Eko'nun standına koyar; cihaz figürü NFC ile tanır, çocuğu adıyla selamlar ve o figürün dünyasında geçen, daha önce hiç anlatılmamış bir hikâye okur. "Merhaba Eko, başka masal" gibi kısa sesli komutlarla durdurulur, sürdürülür, yenisi istenir. Gece figürü (Ay Dede) konunca yavaş ve kısık sesle ninni moduna geçer.

Yenilik, bütün yapay zekânın 16 MB flash ve 8 MB PSRAM'li tek bir ESP32-S3 mikrodenetleyicide çalışmasıdır: (1) Türkçe dil modeli (≈19,9 M parametre: 5,7 M çekirdek + flaşta duran sözcük tablosu; 4 bit, 10,3 MB) hikâyeyi önce "Sorun/Çözüm" planı, sonra metin olarak yazar; (2) kendi eğittiğimiz 4,3 MB'lık konuşma sentezi modeli metni kadın sesiyle okur; (3) ~110 KB'lık uyandırma sözcüğü ve komut modeli mikrofonu cihaz içinde dinler. İsim süzgeci (başka figür adlarını yazamaz), kapalı sözcük dağarcığı, yasaklı içerik kuralları ve 5 aday arasından en iyisini seçen bir seçici cihazda çalışır; boşta kalan zamanda hazır hikâyeler üretilip kuyrukta saklanır, oyuncak konunca beklemeden okunur. Hikâyeler 3–6 yaşa göre kısadır (ortalama ≈75 sözcük, ≈45–60 sn); uyku öncesinde art arda birkaç hikâye dinlenir.

Çözdüğü problem: Ebeveynler çocukları için ekransız ama zengin içerik arıyor. Mevcut ses kutuları (Toniebox, Yoto) her figür için hep aynı kaydı çalar; çocuk birkaç dinlemede sıkılır. Bulut yapay zekâlı oyuncaklar (Miko, FoloToy, Bondu) ise çocuğun sesini ve bilgisini sunuculara gönderir; 2025–2026'da uygunsuz yanıt verme ve on binlerce çocuk sohbetinin açığa çıkması gibi olaylar yaşandı, sunucusu kapanan ürünler çalışmaz oldu (Moxie). Eko hiçbir veri göndermez, abonelik ve sunucu gerektirmez, şirket kapansa da çalışmaya devam eder; Türkçe ve yerel masal kültürüyle tasarlanmıştır.

Bugünkü durum (Kasım 2026; yazılım ve modeller TRL 4, donanım TRL 3): Dil modeli 28.493 hikâyeyle eğitildi; yapay zekâ hakemli kör kıyaslarda önceki sürümleri anlamlı farkla geçti. Kart yazılımının PC'de ESP32 başlıklarıyla birebir aynı çıktıyı verdiği doğrulandı (52/52 aday, seçicide 872/872). Ses modeli eğitildi; C çıkarımı PyTorch ile aynı sonucu veriyor (SNR ≥ 79 dB). Gerçek kartta uçtan uca deneme: [TARİH — başvurudan önce yapılacak; ölçülen hız, ses ve tüketim buraya]. Proje sonunda (18 ay) hedef: kendi devre kartımız, kasa ve figürleriyle CE belgeli, 30–50 ailelik pilotta doğrulanmış ve ilk 1.000 adedi satışa çıkmış ürün (TRL 8).

### 1.2 Müşteri Tanımı

*(1969 / 3000 karakter)*

Birincil müşteri (satın alan): 3–6 yaşında çocuğu olan, kentte yaşayan, orta ve üst-orta gelirli ebeveynler; çoğunlukla 28–42 yaş, üniversite mezunu, çalışan anne ve babalar. Satın alma kararını çoğunlukla anne verir ya da başlatır [T]. Bu ebeveynler çocuklarının ekran süresinden kaygılı, okul öncesi gelişime önem veren, Instagram'daki çocuk gelişimi ve "ekransız oyun" hesaplarını takip eden, oyuncak ve kitabı çoğunlukla Trendyol, Hepsiburada ve kitap/oyuncak zincirlerinden alan kişilerdir. Uyku öncesi masal okuma rutinleri vardır, ama yorgunluk ve zaman baskısı nedeniyle bunu her gece sürdüremediklerini söylerler. Yapay zekâya merakla ama temkinle bakarlar: çocuk verisinin toplanması ve uygunsuz içerik en büyük kaygılarıdır.

Kullanıcı (dinleyen): 3–6 yaş çocuk. Okuma bilmez, ekranı yoktur; figürle oynamayı, aynı karakterle yeni maceralar dinlemeyi ve "bir daha!" demeyi sever. Kısa sesli komutları kullanabilir; düğme ve uygulama kullanamaz.

İkincil müşteriler:

• Hediye alıcılar: büyükanne-büyükbabalar, akrabalar; 23 Nisan, yılbaşı, doğum günü ve bayramlarda alışveriş yapar, "eğitici ve güvenli" ürünü tercih eder.

• Kurumlar: özel anaokulları, kreşler, belediye çocuk kütüphaneleri ve oyun evleri. "Hikâye köşesi" ve dil etkinlikleri için 5 cihaz + figürlü okul öncesi seti; satın alma kararını kurum müdürü ve okul öncesi öğretmeni verir, fiyat ve güvenlik belgesine (CE) bakar.

• Yurt dışındaki Türkçe konuşan aileler (Almanya, Hollanda, Avusturya vb.): çocuğunun Türkçesini korumak isteyen, Türkçe içerik bulmakta zorlanan ebeveynler. Niş ama ödeme isteği yüksek bir segment [T].

Satın alma alışkanlıkları: Fiyat, güvenlik, eğiticilik ve yorumlar belirleyici; 2.500–3.500 TL bandındaki ürünlerde ebeveynler ürün videosu, örnek ses ve diğer ebeveyn yorumlarını inceliyor. Oyuncak alımı yılbaşı, 23 Nisan, karne ve bayram dönemlerinde yoğunlaşır [T]. Bu profil, hızlandırma programında 30+ ebeveyn görüşmesi ve ön kayıt sayfası ile doğrulanacaktır.

### 1.3 Müşteri İhtiyaçları

*(2260 / 3000 karakter)*

Görüşmelerde ve pazar araştırmamızda öne çıkan ihtiyaçlar ve bugün nasıl karşılandıkları:

1. Ekransız, zengin içerik: Ebeveynler tablet ve telefon süresini azaltmak istiyor. Bugün sesli kitap uygulamaları (ekrana bağlı telefon gerekir), CD/sesli masal oyuncakları (3–5 sabit masal) ve ithal ses kutuları (Toniebox ≈6.800 TL, Yoto Mini ≈5.400 TL; Türkiye'de resmî dağıtım yok, Türkçe içerik çok az) kullanılıyor.

2. Her seferinde yeni hikâye: Çocuk aynı karakteri sever ama aynı kaydı birkaç kez dinledikten sonra sıkılır; ebeveyn her gece yeni masal uydurmakta zorlanır. Mevcut ürünlerin hepsi sabit kayıt çalar; yeni içerik için yeni figür ya da kart satın almak gerekir.

3. Güvenlik ve gizlilik: Ebeveynler çocuğun sesinin, adının ve konuşmalarının bir sunucuya gitmesini istemiyor. Bulut yapay zekâlı oyuncaklar bu ihtiyacı karşılamıyor: FoloToy'un uygunsuz yanıtlar nedeniyle API erişimi kesildi (2025), Bondu'da ≈50 bin çocuk sohbeti açıkta kaldı (2026), Moxie sunucusu kapanınca çalışmaz oldu. KVKK 2026'yı çocuk verilerinin korunması yılı ilan etti.

4. Yaşa uygun, korkutmayan içerik: Klasik masallardaki şiddet ve korku öğeleri (kötü kraliçe, zehirli elma, kurt) 3–6 yaş için uygun bulunmuyor. Eko'nun figür kartları bu öğeleri dışarıda bırakır, hikâyeler yardımlaşma, paylaşma, merak ve özür gibi değerler etrafında kurulur.

5. Türkçe ve kültürel aidiyet: Yurt içinde ve özellikle yurt dışında yaşayan aileler çocuklarının Türkçe dinlemesini, Keloğlan ve Nasreddin Hoca gibi yerel figürleri tanımasını istiyor. Küresel ürünlerin Türkçe içeriği yok denecek kadar az.

6. Kolay kullanım ve kesintisiz çalışma: Wi-Fi kurulumu, uygulama, hesap ve abonelik istemeyen; arabada, köyde, uçakta da çalışan bir ürün. Abonelikli ürünler (Miko Max ayda 15 USD) ebeveynde "sürekli ödeme" kaygısı yaratıyor.

7. Uyku rutini: Uyku öncesi sakinleştirici bir ses; Eko'nun Ay Dede figürü yavaş ve kısık sesle 100 anonim halk ninnisini okur, zamanlayıcıyla kapanır.

Hiçbir mevcut ürün bu yedi ihtiyacı birlikte karşılamıyor; en yakın ürünler ya içerik çeşitliliğinden (ses kutuları) ya da gizlilikten (bulut yapay zekâ) ödün veriyor. Bu ihtiyaçların sıralaması ve ödeme isteği hızlandırma programında ebeveyn görüşmeleri, anket ve ön kayıt sayfasıyla ölçülecektir.

### 1.4 Pazar Büyüklüğü

*(2264 / 3000 karakter)*

Toplam pazar (TAM, Türkiye): TÜİK doğum verilerine göre (2022: ≈1,04 milyon, 2023: 958 bin, 2024: 937.559) 2028'de 3–6 yaş arasında ≈3,8–3,9 milyon çocuk olacak [T]. Bu çocukların yaşadığı ≈3,3 milyon hane, KDV hariç 2.499 TL'lik başlangıç setiyle bir kerelik ≈8,2 milyar TL'lik bir cihaz pazarı demektir; her yıl ≈0,93 milyon yeni çocuk bu yaşa girer (yıllık ≈2,3 milyar TL). Türkiye oyuncak pazarı ≈1 milyar USD ve %85'i ithaldir (TOYDER).

Ulaşılabilir pazar (SAM): Kentli, orta ve üst gelirli, ekran süresine duyarlı aileler hanelerin ≈%30'u kabul edildiğinde ≈1,0 milyon hane ve ≈2,5 milyar TL [V]. Buna MEB'e bağlı ≈17,6 bin anaokulu (2024–25; okul öncesi öğrencilerin %18,8'i özel kurumlarda) ve Aile ve Sosyal Hizmetler Bakanlığı'na bağlı özel kreşler (5 cihazlık set, 12.000 TL) ile yurt dışındaki Türkçe konuşan ailelerin 3–6 yaş çocukları (yalnız Almanya'da ≈3 milyon Türkiye kökenli kişi; ≈100 bin çocuk [T]) eklenir.

Elde edilebilir pazar (SOM, 5 yıl): Proje süresinde 1.000 set, ticarileşmenin 1.–5. yıllarında sırasıyla 4.000, 9.000, 16.000, 24.000 ve 32.000 set; toplam 86.000 set, SAM'ın ≈%8'i [V]. Ek figür paketleriyle birlikte 6,5 yılda KDV hariç ≈240 milyon TL ciro (sabit 2026 fiyatlarıyla).

Büyüme eğilimleri: Ekransız ses oyuncakları dünyada hızla büyüyor: tonies 2025 cirosu 630 milyon € (+%31), Yoto 2024'te ≈95 milyon £; iki şirket de %30'un üstünde büyüyor ve büyümeyi ebeveynlerin ekran süresi kaygısı sürüklüyor. Küresel yapay zekâlı akıllı oyuncak pazarının 2024–2030 arasında yıllık ≈%14,6 büyümesi bekleniyor (Lucintel); Çin'de yapay zekâ oyuncak pazarı 2025'te ≈3,5 milyar USD. Türkiye'de e-ticaret 2025'te 4,57 trilyon TL'ye ulaştı (+%52). Buna karşın doğum sayısındaki düşüş (yılda ≈%2–4) Türkiye'deki çocuk sayısını yavaşça azaltıyor; bu yüzden ikinci aşamada yurt dışı Türk diasporası ve aynı teknolojiyle başka dillere (Azerbaycan Türkçesi, İngilizce, Almanca) açılma planlanıyor. Teknoloji dile bağlı değil: yalnız veri ve ses modeli yeniden eğitilir.

Kaynak ve doğrulama: Rakamlar TÜİK, TOYDER, Ticaret Bakanlığı, tonies ve Yoto açıklamalarından alındı; segment payları ve satış adetleri varsayımdır. Hızlandırma programında ebeveyn anketi, ön kayıt sayfası (hedef 1.000 kayıt) ve 30–50 ailelik pilotla güncellenecektir.

### 1.5 Rekabet Durumu

*(2383 / 3000 karakter)*

Pazar üç gruba ayrılıyor; hiçbiri "her seferinde yeni hikâye + hiç veri göndermeme + Türkçe" üçlüsünü bir arada sunmuyor.

1. Figürlü/kartlı ses oynatıcılar (hazır kayıt, yapay zekâ yok):

• tonies (Almanya): Toniebox 2, 119,99 €'dan; 10 yılda ≈12 milyon cihaz, 150 milyon figür sattı; 2025 cirosu 630 M€. Figür başına sabit içerik. Patentleri: EP3092043B2, US10960320B2 (figürle oynatma). Türkiye'de resmî dağıtım ve Türkçe içerik yok. 2024'te bulutta yapay zekâ hikâye üretimini 1.000 kullanıcıyla denedi.

• Yoto (İngiltere): Player 119,99 £, Mini 89,99 £; kartla içerik, aylık kulüp aboneliği; 2024 cirosu ≈95 M£.

• Storypod (ABD): 99,99 USD; RFID'li örgü figürler.

Konum: Pazar lideri, güçlü marka ve içerik kütüphanesi; zayıf yanı içerik tekrarı ve Türkçe yokluğu. Ayrıca Çin'de 30–50 USD'lik bulut yapay zekâlı peluşlar hızla yaygınlaşıyor [T]; fiyat baskısı yaratabilir.

2. Bulut yapay zekâlı oyuncaklar:

• Miko 3 (Hindistan/ABD): 199–299 USD + ayda 15 USD abonelik.

• Curio Grem/Grok (ABD): 99 USD, OpenAI tabanlı, kayıtlar bulutta.

• FoloToy Kumma: uygunsuz yanıtlar nedeniyle OpenAI erişimi kesildi (2025).

• Bondu: ≈50 bin çocuk sohbeti açığa çıktı (2026). Moxie: 799 USD, sunucu kapanınca çalışmaz oldu.

• Mattel–OpenAI ortaklığı: 13 yaş altı kısıtı nedeniyle ertelendi.

Konum: Etkileşimli ve çok dilli; gizlilik, güvenlik ve sürekli maliyet sorunları büyüyor, düzenleyici baskı artıyor (AB Yapay Zekâ Yasası md. 50, KVKK çocuk verileri uyarıları).

3. Türkiye'deki ürünler:

• Elaves Sunny (yerli): 0–5 yaş, ekransız, internetsiz de çalışıyor; yapay zekâ içerik üretiminde arka planda kullanılıyor, cihazda yeni hikâye üretmiyor; CES ödüllü, ABD odaklı. En yakın yerli rakip.

• Lisanslı konuşan peluşlar (Pepee vb.): 4.700–9.999 TL, sabit replikler.

• "Masal anlatan" robotlar: ≈1.550 TL, 3 sabit masal, düşük kalite.

• Eilik vb. masaüstü robotlar: ≈11.000 TL, üst segment.

Fiyat bantları: 800–1.600 TL sabit içerikli sesli oyuncaklar; 4.700–10.000 TL lisanslı konuşan peluş; 5.000–7.000 TL ithal ses kutusu; 10.000 TL+ robot. 2.500–3.500 TL bandı boş görünüyor; Eko bu banda konumlanıyor.

Cihaz içi (internetsiz) hikâye üretimi: Açık kaynakta ESP32 üzerinde İngilizce TinyStories demoları var (ör. Hindistan'da 8 yaşında bir çocuğun projesi, MIT lisanslı 28,9 M parametreli PLE demosu); ticari, Türkçe, ses sentezi ve içerik güvenliğiyle bütünleşik bir ürün bulamadık.

### 1.6 Rekabet Stratejisi

*(2596 / 3000 karakter)*

1. Konumlandırma — "dinleme oyuncağı": Eko'yu sohbet robotu değil, "her gece yeni bir Türkçe masal anlatan, hiçbir veri göndermeyen" bir dinleme oyuncağı olarak konumlandırıyoruz. Tek cümlelik vaat: "Ekransız, internetsiz, her seferinde yeni bir masal; çocuğunuzun sesi hiçbir yere gitmez."

2. Farklılaşma ekseni: (a) içerik çeşitliliği: ses kutularına karşı sınırsız yeni hikâye; (b) gizlilik ve süreklilik: bulut oyuncaklara karşı sıfır veri, sıfır abonelik, sunucusuz çalışma; (c) Türkçe ve yerel kültür: büyük rakiplerin kolay taklit edemeyeceği veri, karakter kartları ve ses.

3. Fiyat: 2.999 TL başlangıç seti (cihaz + 3 figür + Ay Dede); ithal ses kutularından ucuz, sabit masallı oyuncaklardan çok daha zengin. Ek figür paketleri (3 figür, 449 TL) tekrar eden gelir sağlar; abonelik yoktur.

4. Pazara giriş (ilk 18 ay): (i) Hızlandırma programında ön kayıt sayfası ve ebeveyn toplulukları; (ii) 30–50 aile ve 3–5 anaokuluyla pilot, ebeveyn videoları ve çocuk gelişimci görüşleri; (iii) Fongogo/kendi sitemizde ön satış kampanyası (hedef 600+ set); (iv) ilk teslimatlardan sonra Trendyol, Hepsiburada ve kendi web sitemiz.

5. Tutunma ve savunma: (a) Ürün bütünlüğü ve hız: Veri seti tek başına kalıcı bir engel değildir (yapay zekâyla üretildi; benzer yöntemle üretilebilir). Asıl birikim; verinin, modelin, seçicinin, süzgeçlerin ve sesin 16 MB'lık cihaz kısıtına göre birlikte ayarlanması ve bunun ölçüm altyapısıdır. Önce pazara çıkmak ve kurum ilişkileri bu avantajı korur. (b) Teknik derinlik: 16 MB flaşa sığan dil modeli + ses sentezi + uyandırma sözcüğünün tek mikrodenetleyicide birlikte çalışması; bit düzeyinde doğrulanmış C çıkarımı. (c) Marka ve karakterler: Bulut, Zıpzıp, Bip gibi özgün karakterlerin marka ve tasarım tescili; okul öncesi kurumlarla ilişkiler. (d) Güven: "veri toplamayan oyuncak" sertifikasyonu ve bağımsız güvenlik raporu.

6. Kanal stratejisi: İlk yıl doğrudan satış (web + pazaryeri) ve kurumsal okul öncesi seti; ikinci yıl oyuncak/kitap zincirleri (Toyzz Shop, D&R, idefix); üçüncü yıldan itibaren yurt dışındaki Türk diasporası (Almanya, Hollanda) için Amazon.de ve dernek/okul işbirlikleri.

7. Rakip tepkisine karşı: tonies ya da bulut oyuncakların Türkçe cihaz içi üretime geçmesi beklenmez; Türkçe pazar küçük ve cihaz içi model ayrı bir uzmanlık ister. Yerli bir rakibin benzer ürün çıkarması durumunda hız (önce pazara çıkmak), kurum ilişkileri ve figür ekosistemi (ek paketler) tutundurucu olacaktır. Lisanslı yerli karakterler (Niloya, TRT karakterleri) için görüşmeler, satış verisi oluştuktan sonra (ticarileşmenin 1. yılı) açılacaktır.

### 1.7 Engelleyici Faktörler

*(2676 / 3000 karakter)*

1. Hikâye kalitesi ve içerik güvenliği: Küçük modelin ara sıra mantık ya da dil hatası yapması ebeveyn güvenini zedeleyebilir. Önlem: her hikâye için 5 aday üretip seçiciyle en iyisini saklamak, isim süzgeci, kapalı sözcük dağarcığı ve figür kartlarıyla kapalı dünya; veri artırımı (kalitenin veriyle arttığı kör kıyaslarla gösterildi); 30–50 ailelik kör pilotla kabul eşiği ("hikâyelerin ≥%90'ı anlaşılır ve uygun") tanımlanması; satıştan önce bağımsız içerik denetimi.

2. Cihaz üzerindeki hız ve pil: Hikâye yazımı ≈3,7 token/s (≈36 sn/hikâye; 5 adaylı kuyruk hikâyesi ≈3 dk, boşta) tahmin ediliyor; kart 5 V'ta ≈0,5–0,9 A çektiği için 4 × AA ile hesapla yalnız ≈2–3 saat okuma çıkıyor; ses sentezinin gerçek zamanlı olup olmadığı kartta ölçülecek. Önlem: boştayken önceden hikâye üreten kuyruk (oyuncak konunca bekleme yok), iki çekirdekli işleme, ESP32-S3 SIMD komutlarıyla vocoder optimizasyonu; gerekirse daha hafif vocoder; boşta hikâye üretiminin yalnız adaptöre takılıyken yapılması, EVT'de USB-C güç girişi ve şarjlı pil seçeneği.

3. Belgelendirme ve uygunluk: CE için EN 71-1/2/3, EN IEC 62115 ve NFC okuyucu nedeniyle RED (EN 300 330, EN 301 489) testleri; pil ve RoHS beyanları; AEEE/TAP kayıtları. Maliyet ≈7–13 bin USD ve süre 2–3 ay. Önlem: tasarımın baştan bu standartlara göre yapılması (vidalı pil kapağı, küçük parça kontrolü), DVT aşamasında ön uygunluk taraması, akredite laboratuvarla erken görüşme.

4. Fikri mülkiyet ve karakter hakları: Lisanslı karakterler üründen çıkarıldı; Keloğlan, Nasreddin Hoca, Pinokyo, Pamuk Prenses ve Alaaddin halk/kamu malı masal figürleri, diğerleri özgün. Risk: modern uyarlamaların (ör. TRT çizgi filmi, Disney tasarımları) tasarım ve yan karakterlerine benzerlik. Önlem: kendi çizimlerimiz, yan karakterlerin gözden geçirilmesi, avukat görüşü, TÜRKPATENT marka ve tasarım araştırması.

5. Üretim ve tedarik: ESP32-S3 modülü ve bileşenlerde fiyat/kur dalgalanması; kalıp yatırımı; oyuncakta TAREKS denetimi. Önlem: Türkiye'de son montaj (bitmiş oyuncak ithal edilmez), ikinci kaynaklı bileşenler, ilk partide 3B baskı/alüminyum kalıp.

6. Finansman ve nakit: İlk partinin üretimi ve stok ihtiyacı. Önlem: ön satış (kitle fonlama) ile ilk partiyi finanse etmek; ilk dönem raporuyla devam yatırımı başvurusu; kalıp ve belgelendirmenin gerekirse ilk partiden sonraya kaydırılması. Aynı iş planının giderleri için başka kamu hibesi kullanılmaz (1812 taahhütnamesi: kullanılırsa beyan edilir ve mahsup edilir).

7. Pazar kabulü: Ebeveynlerin "yapay zekâ" kelimesine temkinli yaklaşması. Önlem: iletişimde "internetsiz, veri toplamayan" vurgusu, çocuk gelişimci görüşleri, ücretsiz deneme sesi örnekleri ve iade garantisi.

### 1.8 Sosyal Fayda

*(2447 / 3000 karakter)*

• Ekran süresinin azalması ve okuma alışkanlığı: Eko, okul öncesi çocuğa ekransız, dinlemeye dayalı bir içerik sunar. Dinlenen hikâyeler sözcük dağarcığını ve dinleme-anlama becerisini destekler; ebeveyn-çocuk arasında hikâye üzerine konuşmayı teşvik eder.

• Çocukların gizliliği ve güvenliği: Ürün tasarım gereği kişisel veri toplamaz, ağ bağlantısı yoktur (Wi-Fi yalnız ebeveynin ayar kartıyla açtığı yerel ayar sayfası içindir, internet hiç kullanılmaz). Bulut yapay zekâ oyuncaklarındaki veri sızıntısı ve uygunsuz yanıt risklerine karşı güvenli bir alternatif oluşturur; KVKK'nın çocuk verileri vurgusuyla uyumludur.

• Türkçe ve kültürel miras: Keloğlan, Nasreddin Hoca gibi halk figürleri ve 100 anonim halk ninnisi, yeni kuşaklara aktarılır. Yurt dışındaki Türk ailelerin çocuklarının Türkçesini korumasına katkı sağlar.

• Erişilebilirlik: İnternet ve abonelik gerektirmediği için kırsal bölgelerde, internet erişimi kısıtlı hanelerde ve afet bölgelerinde de çalışır. Okuma güçlüğü ya da görme engeli olan çocuklar ve ebeveynler için sesli içerik sağlar. Kurumsal setler, kreş ve belediye çocuk kütüphanelerinde hikâye etkinliklerini zenginleştirir.

• Yerli teknoloji ve nitelikli istihdam: Cihaz içi yapay zekâ (dil modeli, konuşma sentezi, ses tanıma) alanında yerli bilgi birikimi oluşturur; yazılım, elektronik ve tasarım alanında nitelikli istihdam yaratır. Son montajın Türkiye'de yapılması ithalata bağımlı (%85) oyuncak sektöründe yerli üretime katkıdır.

• Çevre: Sunucu ve bulut işlemi olmadığı için kullanım boyunca veri merkezi enerjisi harcanmaz; ürün düşük güçlü mikrodenetleyiciyle çalışır. Pil bölmesi değiştirilebilir, cihaz uzun ömürlüdür (abonelik ya da sunucu kapanınca çöpe gitmez).

Birleşmiş Milletler Sürdürülebilir Kalkınma Amaçlarına katkı:

• SKA 4 – Nitelikli Eğitim (4.2: okul öncesi gelişim ve eğitime erişim),

• SKA 9 – Sanayi, Yenilikçilik ve Altyapı (yerli yapay zekâ ve elektronik ürün geliştirme),

• SKA 8 – İnsana Yakışır İş ve Ekonomik Büyüme (nitelikli istihdam),

• SKA 10 – Eşitsizliklerin Azaltılması (internetsiz, aboneliksiz erişim),

• SKA 12 – Sorumlu Üretim ve Tüketim (uzun ömürlü, sunucuya bağımlı olmayan ürün),

• SKA 16 – Barış, Adalet ve Güçlü Kurumlar (16.2 kapsamında çocukların çevrimiçi risklerden korunmasına katkı).

Etki göstergeleri: ulaşılan çocuk sayısı, kurum sayısı, ebeveyn anketinde ekran süresinde azalma ve dinleme alışkanlığı beyanı, toplanan veri miktarı (hedef: sıfır).

## 2 Ürün ve Teknoloji

### 2.1 Değer Önerisi

*(2468 / 3000 karakter)*

Özellik → müşteri gereksinimi eşleştirmesi:

• Cihaz içi Türkçe dil modeli (her seferinde yeni hikâye) → "çocuk sıkılmasın, her gece yeni masal". Her istekte yeniden yazılan hikâye; çeşitlilik ve tekrar oranı pilotta ölçülecek. Ölçüt: ebeveyn pilotunda haftalık kullanım sıklığı ve "çocuk sıkıldı" beyanı.

• İnternetsiz ve veri toplamayan mimari → "çocuğumun sesi ve bilgisi bir yere gitmesin". Mikrofon yalnız cihaz içinde uyandırma sözcüğü ve 6 komut için dinler, kayıt tutulmaz; ağ bağlantısı yoktur. Ölçüt: bağımsız güvenlik incelemesi (ağ trafiği yok, kayıt yok).

• İçerik güvenliği katmanları (figür kartı, kapalı dünya, isim süzgeci, yasaklı öğeler, 5 aday + seçici) → "korkutucu ya da uygunsuz içerik olmasın". Ölçüt: pilotta "uygunsuz/korkutucu hikâye" oranı (hedef < %1) ve "anlaşılır, tutarlı hikâye" oranı (hedef ≥ %90).

• Figürlü etkileşim ve sesli komutlar (düğme yok) → "3 yaşındaki çocuk da tek başına kullanabilsin". Figür standa konunca hikâye başlar; "Dur, devam, başka, bir daha, sesini aç/kıs".

• Ninni modu (Ay Dede) → "uyku rutini". Yavaş, alçak sesle 100 halk ninnisi, uyku zamanlayıcısı.

• Abonelik ve uygulama yok, pille çalışır → "kurulum ve sürekli ödeme derdi olmasın". Kutudan çıkar çıkmaz çalışır; ayarlar (çocuğun adı, ses, uyku süresi) ayar kartıyla telefondan yapılır.

• Türkçe ve yerel figürler → "kültürümüzü tanısın". Keloğlan, Nasreddin Hoca ve özgün Türk karakterleri.

Doğrulama çalışmaları (yapılan):

• Kalite: Hikâye modeli 6 kez yeniden eğitildi; her sürüm kör ikili kıyasla (hangi modelin yazdığı gizli; iki ayrı yapay zekâ hakemi: genel kalite ve olay örgüsü; 8 aday + seçici, kartta 5 aday) ölçüldü. Son model, ara modeli 180 vakada 102–78 ve 99–73; Keloğlan'da önceki ürün modelini 48 vakada 34–14 ve 29–15 yendi (işaret testi p < 0,05). 10 puanlık rubrikte önceki ürün modeli 3,17'den 4,51'e çıkmıştı (yapay zekâ hakemli); son model insan hakemli kör testle ölçülecek.

• Teknik: Kart yazılımı, PC'de sahte ESP32 başlıklarıyla derlenip referans Python üretimiyle bit bit karşılaştırıldı (52/52 aday, seçicide 872/872 eşleşme). Ses modelinin C çıkarımı PyTorch ile karşılaştırıldı (SNR ≥ 79 dB). Uyandırma modeli görülmemiş seslerde %87–93 uyanma, saatte 0,3–1,9 yanlış uyanma.

Doğrulama çalışmaları (planlanan, hızlandırma ve Aşama 2): 30+ ebeveyn görüşmesi; ön kayıt sayfası (hedef 1.000 kayıt, fiyat testi); 30–50 aile ve 3–5 anaokuluyla 4 haftalık pilot (etik kurul onaylı), kör kalite testi ve kullanım anketi.

### 2.2 Teknolojik Rekabet

*(2338 / 3000 karakter)*

Müşteri gereksinimine göre karşılaştırma (Eko / ses kutusu: Toniebox-Yoto / bulut yapay zekâ oyuncağı: Miko-Curio / sabit masallı yerli oyuncak):

• Her seferinde yeni hikâye: Eko VAR (cihazda üretim) / YOK (sabit kayıt) / VAR (bulutta) / YOK.

• İnternetsiz çalışma: Eko TAMAMEN / kurulum için Wi-Fi, sonra çevrimdışı / YOK (sürekli bağlantı) / VAR.

• Kişisel veri gönderimi: Eko YOK / hesap ve kullanım verisi / ses ve konuşma kaydı buluta gider / YOK.

• Abonelik: Eko YOK / içerik için kart-figür satın alma, Yoto Club aboneliği / ayda ≈15 USD / YOK.

• İçerik güvenliği: Eko kapalı dünya + süzgeç + seçici, cihazda denetlenebilir / hazır kayıt, güvenli / genel amaçlı LLM, uygunsuz yanıt olayları / güvenli ama sınırlı.

• Türkçe içerik: Eko ANA DİL / çok az / makine çevirisi düzeyinde / var ama 3–5 masal.

• Sunucu kapanırsa: Eko çalışmaya devam eder / büyük ölçüde çalışır / çalışmaz (Moxie örneği) / çalışır.

• Fiyat: Eko 2.999 TL / ≈5.400–6.800 TL / ≈10.000 TL + abonelik / ≈1.600 TL.

Teknik farklılaşma (rakiplerin kolayca kopyalayamayacağı kısım):

1. Bütün zincir tek mikrodenetleyicide: 10,3 MB'lık 4 bit dil modeli flash'ta (Per-Layer Embeddings: sözcük tablosu flash'ta, çekirdek PSRAM'de), 4,3 MB ses modeli, 110 KB uyandırma modeli 16 MB flash ve 8 MB PSRAM'e birlikte sığıyor. Model büyütülmeden kalite veriyle artırıldı.

2. Türkçeye özgü veri ve süreç: 28.493 çocuk hikâyesi (figür kartlarıyla yönlendirilen yapay zekâ yazarlarıyla üretildi; kod kurallarıyla ve yapay zekâ hakemleriyle denetlendi), kapalı dünya kuralları ve kör ikili kıyas yöntemi. Kalitenin veri hacmiyle arttığı ölçüldü (10 kat veri olay örgüsünü düzeltti).

3. Güvenlik mühendisliği: Başka figür adlarını yazmayı engelleyen isim süzgeci ve uydurma ad/sözcük kurallarıyla çalışan seçici, PC referansıyla bit düzeyinde aynı çalışıyor; davranış öngörülebilir ve test edilebilir.

4. Ses: Ticari kullanıma açık (Apache-2.0) bir öğretmen sesten damıtılmış, karta özel 4 bit akustik + 8 bit vocoder; gece modu için hız, perde ve duraklama ayarı.

Doğrulama: Rakip karşılaştırması masa başı incelemeye (ürün sayfaları, basın, PIRG ve Malwarebytes raporları) dayanıyor. Hızlandırma programında 10+ ebeveynle "Eko vs. ses kutusu" karşılaştırmalı dinleme testi ve satın alma karar kriterleri anketi yapılacak; pilotta kullanım sıklığı ve sıkılma beyanı ölçülecek.

### 2.3 Ürün Fiyatı

*(1909 / 3000 karakter)*

Başlangıç seti: 2.999 TL (KDV dahil; KDV hariç 2.499 TL). İçerik: Eko cihazı (stand, hoparlör, ışık halkası), 3 figür (Keloğlan + 2 seçmeli) ve Ay Dede gece figürü, ayar kartı. Pil dahil değil (4 × AA).

Ek figür paketi: 449 TL (KDV dahil; 3 figür). Okul öncesi kurum seti: 5 cihaz + 13 figürün tamamı, 12.000 TL (KDV hariç) [V].

Varsayımlar:

1. Fiyat bantları: Türkiye'de sabit içerikli sesli oyuncaklar 800–1.600 TL, lisanslı konuşan peluşlar 4.700–9.999 TL, ithal ses kutuları ≈5.400–6.800 TL (Yoto Mini, Toniebox 2; kurla çevrilmiş), yapay zekâ robotları 10.000 TL üstü. 2.500–3.500 TL bandı boş; Eko "ithal ses kutusundan ucuz, sabit masallı oyuncaktan çok daha zengin" konumda.

2. Kanal: Ağırlıklı ortalama kanal karışımı %40 pazaryeri (≈%18 komisyon), %40 kendi web sitemiz, %20 kurum ve perakende (≈%35 indirim). Birim başına ortalama kanal/dağıtım maliyeti ≈507 TL (başa baş analizinde "dağıtım maliyeti" olarak gösterildi).

3. Ek paket bağlanma oranı: satılan her cihaz başına ortalama 0,8 ek paket [V].

4. Fiyatlar sabit 2026 fiyatlarıyla verildi; enflasyon etkisi fiyat ve maliyete birlikte yansıtılacağı için reel marjın korunduğu varsayıldı.

5. İlk 600 set kitle fonlama/ön satışta %15–20 erken alım indirimiyle (≈2.499 TL KDV dahil) satılacak.

Doğrulama çalışmaları:

• Yapılan: Trendyol, Hepsiburada, idefix ve üretici sitelerinde rakip fiyat taraması (Ekim 2026, docs/PAZAR_ARASTIRMASI.md).

• Planlanan (hızlandırma programı): (a) Van Westendorp fiyat duyarlılığı anketi (≥150 ebeveyn); (b) ön kayıt sayfasında iki fiyat seçeneğiyle A/B testi (2.499 / 2.999 TL), kaparo ile niyet ölçümü; (c) 10 anaokulu müdürüyle kurum seti fiyat görüşmesi; (d) pilot ailelerinde "bu ürünü bu fiyata alır mıydınız" ve önerilen fiyat sorusu.

• Karar kuralı: Ön kayıtların ≥%20'si 2.999 TL seçeneğinde kaparo bırakırsa fiyat korunur; aksi halde 2.499 TL'ye inilip set içeriği (figür sayısı) yeniden düzenlenir.

### 2.4 Ürün Maliyeti

*(2012 / 3000 karakter)*

Tahmini birim maliyet (başlangıç seti, fabrika çıkışı malzeme + montaj; 1 USD ≈ 50 TL [V]):

1.000 adet ölçeğinde ≈21 USD ≈ 1.050 TL; 10.000 adet ölçeğinde ≈13,5 USD ≈ 675 TL.

Kalemler (1.000 / 10.000 adet, USD): ESP32-S3-WROOM-1-N16R8 modülü 3,9 / 3,3 (LCSC 3,68 USD, 1.300+ adet); I2S yükselteç 0,6 / 0,4; hoparlör 0,7 / 0,5; I2S mikrofon 0,8 / 0,5; NFC okuyucu IC + PCB anteni 0,5 / 0,35 (MFRC522 klonu 0,30 USD); 16 LED'li ışık halkası ve seviye çevirici 1,0 / 0,6; 5 V düşürür-yükseltir regülatör, pil yuvası, anahtar 1,2 / 0,8; pasif bileşenler 0,5 / 0,3; PCB 0,9 / 0,4; SMT montaj, test ve flaş yazma 2,0 / 0,9; stand kasası ve hoparlör ızgarası 1,6 / 1,0; 4 figür (kalıp/baskı + NTAG213 etiketi) 2,8 / 1,6; ayar kartı, kutu, kılavuz 1,6 / 1,0; son montaj, kalite kontrol, %3 fire 1,2 / 0,6; navlun ve gümrük (bileşen ithalatı) 1,4 / 0,7.

Başa baş analizinde kullanılan ağırlıklı ortalama birim değişken maliyet (6,5 yıl): malzeme 710 TL, personel (montaj/test) 60 TL, enerji 5 TL, dağıtım 507 TL, diğer (garanti/iade karşılığı ≈%3) 75 TL; toplam ≈1.357 TL.

Sabit maliyetler (birim maliyete dahil edilmedi, başa baş analizinde ayrı): kalıplar (alüminyum, stand + figürler) ≈700 bin TL, CE/RED belgelendirme ≈450 bin TL, test ve programlama düzenekleri ≈200 bin TL.

Varsayımlar ve doğrulama:

• Yapılan: Ana bileşen fiyatları LCSC ve tedarikçi listelerinden alındı; PCBA ve kalıp aralıkları üretici yayınlarından derlendi (docs/PAZAR_ARASTIRMASI.md, Ekim 2026). Masa üstü prototipin bileşenleri Türkiye'deki elektronik satıcılarından temin edilebiliyor.

• Planlanan: EVT kartı (kendi PCB'miz) için JLCPCB/PCBWay ve iki yerli EMS firmasından teklif; figür ve kasa için 3B baskı ve alüminyum kalıp teklifleri (Türkiye'de 2, Shenzhen'de 1 üretici); DVT'de 60 adetlik seri ile gerçek montaj süresi ve fire ölçümü.

• Hedef: 10.000 adet ölçeğinde birim malzeme maliyetinin ≤ 700 TL'de kalması. Kur artışına karşı fiyatlar dönemsel güncellenecek; ESP32 için ikinci kaynak (farklı modül üreticisi) araştırılacak.

### 2.5 Tekniğin Bilinen Durumu

| Buluş başlığı | Başvuru numarası | Proje çıktılarıyla ilişkisi | Proje çıktısının özgün yönleri |
|---|---|---|---|
| Spielzeug (Tonies/Toniebox) | EP3092043B2 | Figür konunca ses dosyası çalar | Eko kayıt çalmaz, hikâyeyi üretir |
| Toy (Boxine/Toniebox) | US10960320B2 | Figürle oynatma, sensör | Cihaz içi LLM + TTS + KWS |
| Müzik/hikâye oyuncağı (Tonies) | EP4282503A1 | Oyuncakla kayıtlı hikâye çalma | İnternetsiz, veri göndermez |

Patentler Google Patents'te doğrulandı (EP3092043B2: Tonies GmbH, başvuru 9.1.2015; US10960320B2: Boxine GmbH; EP4282503A1: Tonies GmbH, başvuru 25.5.2022). Cihaz içinde üretilen hikâyeye yönelik bir patente rastlanmadı; patent vekiliyle profesyonel tarama İP5'te planlıdır.

### 2.6 Fikri Mülkiyet Hakları

*(2527 / 3000 karakter)*

Mevcut fikri mülkiyet ve şirkete aktarımı: Kart yazılımı (C), eğitim/değerlendirme kodu (Python), eğitilmiş modeller (hikâye, ses, uyandırma), 28.493 hikâyelik veri seti, figür kartları, 100 ninnilik derleme ve CAD dosyaları kurucunun özel Git deposunda sürüm geçmişiyle kayıtlıdır. Mükemmeliyet Mührü sonrasında şirket kuruluşuyla birlikte bedelsiz fikri mülkiyet devir sözleşmesi imzalanacak, depo şirkete taşınacaktır. Kurucunun bir yükseköğretim kurumunda patent ya da başka hak sahipliği yoktur [DOĞRULA].

Açık kaynak ve üçüncü taraf: Çıkarım motorunun temeli (ESP32'de PLE mimarili dil modeli çıkarımı) MIT lisanslı bir projedir; lisans ve atıf korunur. Eko'ya özgü olanlar: Türkçe model ve veri hattı, isim süzgeci, aday seçici, hikâye kuyruğu, konuşma sentezi ve uyandırma motorları, NFC/ışık/ayar yazılımı, figür kartları ve tasarımlar. Ön eğitim verisi TinyStories Türkçe (CDLA-Sharing-1.0; eğitilmiş model "sonuç" sayılır). Ses: VoxCPM2 (Apache-2.0) ile üretilen sentetik veri [REFERANS SESİN KAYNAĞI VE HAKKI: DOĞRULA]; uyandırma verisinde Supertonic (Open RAIL-M). Eğitim hikâyeleri yapay zekâ yazarlarıyla üretildi; hizmet koşulları ticari kullanıma izin veriyor. Yapay zekâ çıktısı FSEK'te eser sayılmayabileceği için veri seti veri tabanı yapımcısı hakkı ve ticari sır olarak korunacak. Lisans envanteri ekte verilecek.

Korunma planı: (1) Marka: "Eko" ve logo ile özgün karakter adları için TÜRKPATENT'e 9, 16, 28, 41. sınıflarda başvuru; "Eko" yaygın bir sözcük olduğundan ön araştırma yapılacak, gerekirse birleşik marka ("Eko Masal" vb.). (2) Endüstriyel tasarım: stand ve özgün figürler. (3) Faydalı model: "figür tanımalı, cihazda önceden hikâye üretip kuyrukta saklayan ve canlı yazarken okuyan oyuncak" ve "ad süzgeçli aday seçimi" için patent vekiliyle araştırma (Espacenet: A63H33, G06F40/56) ve uygun bulunursa başvuru. (4) Ticari sır: veri üretim süreci, kurallar ve eğitim tarifleri; çalışan ve danışmanlarla gizlilik ve buluş devri sözleşmeleri.

Faaliyet serbestliği: tonies'in figürle oynatma patentleri (EP3092043B2, US10960320B2, EP4282503A1) incelenecek; Eko'nun kayıt oynatmak yerine hikâyeyi cihazda üretmesi patent vekiliyle değerlendirilecek. Halk masalı figürlerinin modern uyarlamalarına (TRT çizgi filmi, Disney) ait tasarım ve yan karakterler kullanılmayacak; Keloğlan kartındaki dizi kaynaklı yan karakterler anonim masal figürleriyle değiştirilecek.

Marka ve logo: Çalışma adı "Eko" (uyandırma sözcüğü "Merhaba Eko"); logo hızlandırma programında tasarlanacak [LOGO HAZIRSA EKLE].

### 2.7 Regülasyonlar

*(2585 / 3000 karakter)*

1. Oyuncak Güvenliği Yönetmeliği (2009/48/AT uyumlu, RG 4.10.2016/29847): CE işareti, teknik dosya, uygunluk beyanı, Türkçe uyarılar. Standartlar: EN 71-1 (mekanik/fiziksel; figürlerin küçük parça testi), EN 71-2 (yanıcılık), EN 71-3 (ağır metal göçü). Piyasa gözetimi Ticaret Bakanlığı'ndadır.

2. Elektrikli oyuncaklar: EN IEC 62115 (pil bölmesi tutsak vidalı, alet olmadan açılmaz; yüzey sıcaklığı). Eko 4 × AA pil ile çalışır; şarjlı Li-ion pil olmadığından IEC 62133 ve UN 38.3 yükü yoktur (EVT'de şarjlı pil seçilirse eklenir).

3. Telsiz Ekipmanları Yönetmeliği (RED, BTK): NFC okuyucu (13,56 MHz) ve ayar modundaki Wi-Fi nedeniyle EN 300 330, EN 300 328, EN 301 489-1/-3/-17, EN 62479 testleri. RED siber güvenlik maddesi (EN 18031, 1.8.2025'ten itibaren): cihaz internete bağlanmaz, ama ebeveynin isteğe bağlı girdiği çocuk adını yerel olarak saklar; bu nedenle 3(3)(e) kapsamı laboratuvarla değerlendirilecek; ayar Wi-Fi'ı için şifreli, kısa süreli ve yerel erişim, imzalı yazılım güncellemesi.

4. RoHS, REACH, AEEE ve Atık Pil (TAP) kayıtları; 6502 sayılı Kanun kapsamında 2 yıl garanti ve Türkçe kullanım kılavuzu.

5. Kişisel verilerin korunması (KVKK/GDPR): Cihaz ses kaydı tutmaz, veri göndermez; çocuğun adı yalnız cihazda, ebeveynin isteğiyle saklanır ve tek dokunuşla silinir. Şirket hiçbir kullanıcı verisine erişmez; ad yalnız cihazda kalır; web sitesi ve ön satış için aydınlatma metni hazırlanacak.

6. Yapay zekâ şeffaflığı: AB Yapay Zekâ Yasası md. 50 (2 Ağustos 2026'dan itibaren) yapay ses ve metin üreten sistemlerde çıktının yapay olduğunun belirtilmesini istiyor. Ambalajda ve kılavuzda "Hikâyeleri yapay zekâ yazar, ses yapay zekâ ile üretilmiştir" ibaresi; Supertonic/VoxCPM2 lisans koşulları da bu bildirimi gerektiriyor.

7. Pilot çalışma ve etik: Ebeveyn anketleri, görüşmeler ve çocuklu ailelerle kullanım gözlemi için hızlandırma programı sırasında (2027 bahar) üniversite etik kuruluna başvurulacak, onay belgesi iş planı başvurusuna eklenecek; ebeveyn onam formu, çocuk sesinin kaydedilmemesi, anonim veri.

8. İthalat ve ihracat: Bitmiş oyuncak ithalatında TAREKS denetimi gerektiği için son montaj Türkiye'de yapılacak; AB'ye satışta Pil Tüzüğü 2023/1542 (değiştirilebilir pil, 2027), CRA (2027) ve yeni AB Oyuncak Güvenliği Tüzüğü 2025/2509 (dijital ürün pasaportu, 2030) yol haritasına alınacak.

Uyum planı: Tasarım DVT aşamasında akredite bir laboratuvarda (TÜV, SGS, Intertek, Türk Loydu vb.) ön uygunluk taramasından geçirilecek; seri üretim öncesi tam test ve teknik dosya. Belgelendirme bütçesi ve takvimi kritik iş adımlarında yer almaktadır.

## 3 Ekip

### 3.1 Ekip ve Deneyim

*(1845 / 3000 karakter)*

[BU BÖLÜM KİŞİSEL BİLGİLERLE DOLDURULACAK — aşağıdaki yapı ve örnek metin kullanılabilir.]

Proje yürütücüsü ve kurucu — [AD SOYAD] ([ÜNİVERSİTE, BÖLÜM, MEZUNİYET YILI / ÖĞRENCİLİK DURUMU]): Ürünün fikir sahibi ve teknik lideri. Eko'nun bugünkü sürümünü uçtan uca geliştirdi ve yönetti: Türkçe hikâye veri setinin (28.493 hikâye) ve hakem süreçlerinin kurulması, 5,7 M parametreli dil modelinin eğitimi ve kör kıyaslarla değerlendirilmesi, ESP32-S3 kart yazılımı (C), NFC/ses/ışık donanım entegrasyonu, karta özel konuşma sentezi modelinin RTX 4090'lı iş istasyonunda eğitilmesi ve uyandırma sözcüğü modeli. Yapay zekâ destekli geliştirme araçlarını etkin kullanarak küçük ekiple hızlı ilerleme deneyimine sahip. [ÖNCEKİ İŞ/PROJE DENEYİMİ, YARIŞMA, SERTİFİKA EKLEYİN.]

Önerilen ekip tamamlayıcıları (hızlandırma programında netleşecek):

• Kurucu ortak / donanım ve üretim sorumlusu — [AD SOYAD] ([ELEKTRİK-ELEKTRONİK / MEKATRONİK MÜHENDİSİ]): PCB tasarımı, EMC/RED uyumu, seri üretim (EMS, kalıp) deneyimi. Aranıyor [DOLDUR ya da "aranıyor" yaz].

• Danışman — çocuk gelişimi / okul öncesi eğitim uzmanı ([AD SOYAD, UNVAN]): içerik güvenliği kuralları, yaşa uygunluk ve pilot çalışmanın tasarımı.

• Danışman — pazarlama ve e-ticaret ([AD SOYAD]): oyuncak/çocuk ürünü pazarlaması, pazaryeri ve kitle fonlama deneyimi.

Birlikte çalışma geçmişi: [VARSA YAZIN: ör. ortak proje, aynı bölüm, önceki işyeri.]

Kanıtlanabilir çıktılar (ekte sunulabilir): masa üstü prototip (gerçek kartta deneme [TARİH]), PC'de doğrulanmış kart yazılımı, eğitim ve değerlendirme günlükleri, kör kıyas raporları, örnek hikâye ve ses kayıtları, 3B kasa ve figür tasarımları.

Not: Panel ölçütlerinde "ekip yetkinliği ve uyumu" ayrı puanlanır; tek kişilik başvurularda donanım/üretim yetkinliğinin bir kurucu ortak ya da yazılı taahhütlü danışmanla tamamlanması önerilir.

### 3.2 Ortaklık Yapısı

*(1699 / 3000 karakter)*

[ORTAKLIK YAPISI ÜRÜN SAHİBİNİN KARARIYLA KESİNLEŞTİRİLECEK — aşağıdaki iki seçenekten biri seçilmeli.]

Seçenek A (tek kurucu): Şirket, Türkiye'de yerleşik anonim şirket olarak kurulacaktır. TÜBİTAK BİGG Fonu'nun %3 payı dışında kalan payların tamamı (%97) proje yürütücüsü [AD SOYAD]'a aittir. İleride ekibe katılacak kilit çalışanlar için %5–10'luk bir çalışan pay havuzu, BİGG Fonu'nun yazılı izniyle ve Yatırım ve Pay Sahipleri Sözleşmesi'ndeki devir sınırları (ilk 4 yıl kuruluş sermayesinin %20'si) gözetilerek oluşturulabilir.

Seçenek B (iki kurucu): Proje yürütücüsü [AD SOYAD] %[65–75], kurucu ortak [AD SOYAD] (donanım ve üretim) %[22–32], TÜBİTAK BİGG Fonu %3. Payların hakkaniyete dayalı kazanılması (vesting) için kurucular arası sözleşme imzalanacak.

Kilit kişiler ve yükümlülükler: Proje yürütücüsü ve (varsa) kurucu ortak, Yatırım ve Pay Sahipleri Sözleşmesi'ndeki çalışma taahhüdü ve rekabet yasağı kapsamında, pay sahibi oldukları sürece yalnız şirket için çalışacak, başka bir firmada çalışmayacak ve danışmanlık vermeyecektir; pay sahipliği sona erdikten sonra 2 yıl rakip bir işletmede çalışmayacaktır. Yasaktan muaf girişimci statüsü (pay ≤ %20, yürütücü ya da yönetici olmama) yalnız danışman konumundaki küçük ortaklar için kullanılacaktır.

Uygunluk beyanı: Proje yürütücüsü ve kurucu ortaklar, hızlandırma programına kabul tarihi itibarıyla hiçbir sermaye şirketinde ya da şahıs işletmesinde ortak değildir; daha önce Teknogirişim Sermayesi Desteği, TÜBİTAK 1512 ya da 1812 Aşama 2 desteği almamışlardır [DOĞRULA].

Sermaye: Şirket 250.000 TL sermaye ile kurulacak; BİGG Fonu yatırımı nominal sermaye + emisyon primi olarak aktarılacaktır (Fon Yatırım Kılavuzu'na göre).

### 3.3 İş Paylaşımı

*(2018 / 3000 karakter)*

Proje süresi 18 aydır (destek başlangıcı hedefi 1 Ocak 2028; 2027-2 tohum öncesi yatırım çağrısı).

[AD SOYAD] — Proje yürütücüsü, Genel Müdür (CEO) ve teknik lider; 18 ay, tam zamanlı (1,0 adam/ay):

• İP1 Ürün ve yapay zekâ: hikâye modelinin yeni verilerle iyileştirilmesi, kalite ve güvenlik süzgeçleri, cihaz üzerinde hız optimizasyonu (dil modeli ve ses).

• İP2 Kart yazılımı ve doğrulama: gerçek kartta uçtan uca testler, güç tüketimi, güncelleme mekanizması.

• İP5 Ticarileşme: yatırımcı ve kurum ilişkileri, kitle fonlama kampanyası, fiyat ve kanal kararları; TÜBİTAK dönem raporları.

• Şirket yönetimi: bütçe, satın alma, sözleşmeler.

[AD SOYAD / ARANIYOR] — Donanım ve üretim sorumlusu (CTO-donanım); 1.–18. ay [tam/yarı zamanlı]:

• İP3 Donanım: EVT ve DVT devre kartı tasarımı, EMC/RED ön uyumu, kasa ve figür üretim tasarımı, EMS ve kalıp tedarikçileriyle çalışma, üretim test düzeneği.

• İP4 Belgelendirme: laboratuvar seçimi, ön uygunluk taraması, teknik dosya.

(Proje bütçesinde personel olarak yalnız proje yürütücüsü var. Donanım iş paketleri bütçedeki hizmet alımlarıyla yürütülür: PCB/DFM danışmanlığı 90.000 TL, endüstriyel tasarım 60.000 TL, test laboratuvarı 90.000 TL. Kurucu ortak katılırsa maaşı devam yatırımı ve ön satış gelirinden karşılanır, bütçe revize edilir.)

Danışmanlar (yarı zamanlı, sözleşmeli):

• Çocuk gelişimi uzmanı [AD SOYAD]: içerik kuralları, pilotun yürütülmesi ve değerlendirmesi (4.–8. ay, ayda ≈1 gün; etik kurul onayı hızlandırma programında alınır).

• Pazarlama danışmanı [AD SOYAD]: marka konumlandırma, kitle fonlama ve pazaryeri (8.–18. ay, ayda ≈2 gün).

• Mali müşavir: şirket muhasebesi (1.–18. ay).

• Patent ve marka vekili: marka, tasarım ve faydalı model başvuruları (1.–6. ay).

Karar verme: Teknik ve ürün kararları proje yürütücüsünde; donanım kararları donanım sorumlusuyla ortak; bütçe ve ortaklık kararları yönetim kurulunda (kurucular). Haftalık ilerleme toplantısı ve aylık kilometre taşı değerlendirmesi; altı ayda bir TÜBİTAK dönem raporu (AGY 312).

### 3.4 İşbirlikleri

*(1841 / 3000 karakter)*

Planlanan işbirlikleri (görüşmeler hızlandırma programında başlatılacak; kesinleşenler [KESİNLEŞTİ] olarak işaretlenecek):

• Uygulayıcı kuruluş / hızlandırma programı [PROGRAM ADI]: mentorluk, iş kliniği, yatırımcı ağı, kuluçka ofisi ve teknopark imkânları; Aşama 2 başvurusunda iş planı onayı.

• Üniversite (etik kurul ve çocuk gelişimi bölümü) [ÜNİVERSİTE ADI]: pilot çalışmanın etik kurul onayı, çocuk gelişimi öğretim üyesinin içerik ve yaşa uygunluk danışmanlığı, öğrencilerle gözlem çalışması. Rol: kısa zamanlı danışman.

• Özel anaokulları ve kreşler (3–5 kurum) [KURUM ADLARI]: 4 haftalık pilot; öğretmen geri bildirimi; kurum seti tasarımı. Rol: test ortağı, ilk kurumsal müşteri adayı.

• Pilot aileler (30–50 aile): ön kayıt sayfası ve ebeveyn topluluklarından gönüllü; ücretsiz cihaz karşılığında 4 hafta kullanım ve anonim anket.

• Elektronik üretim (EMS) firması [FİRMA ADI; ör. İstanbul/Ankara'da EMS üreticileri ya da JLCPCB/PCBWay]: EVT/DVT kart montajı, seri üretim teklifi, flaş yazma ve test.

• Plastik/kalıp ve oyuncak üreticisi [FİRMA ADI; ör. Çayırova, Bursa, Manisa bölgesi]: stand kasası ve figür kalıbı, son montaj.

• Akredite test laboratuvarı [TÜV / SGS / Intertek / Türk Loydu]: EN 71, EN IEC 62115 ve RED ön uygunluk ile belgelendirme.

• Patent ve marka vekili [AD SOYAD]: marka, tasarım, faydalı model ve faaliyet serbestliği araştırması.

• Kitle fonlama platformu (Fongogo) ve pazaryerleri (Trendyol, Hepsiburada): lansman ve satış.

• İleride lisans görüşmesi (ticarileşmenin 1. yılı): yerli karakter hak sahipleri (Kaynak Licensing/Niloya, TRT Çocuk) — satış verisi ve içerik güvenliği kurallarıyla.

Bu kişi ve kuruluşların deneyimleri ve görevleri, niyet mektupları alındıkça iş planına eklenecektir. Niyet mektubu hedefi: en az 3 anaokulu, 1 üniversite (etik kurul/çocuk gelişimi), 1 EMS firması.

### 3.5 Ekibin Misyonu ve Değerleri

*(1781 / 3000 karakter)*

Misyon: Her çocuğun, internete ve ekrana bağlı kalmadan, güvenli ve kendi dilinde, her seferinde yeni bir hikâyeyle hayal gücünü geliştirebilmesini sağlamak. Yapay zekâyı çocuk verisini toplamadan, ebeveynin güvenebileceği şekilde çocuklara ulaştıran ilk yerli şirket olmak.

Vizyon: Cihaz içi yapay zekâ ile çalışan, gizliliği tasarımdan gelen çocuk ürünlerinde Türkiye'den çıkan küresel bir marka olmak; Eko'yu önce Türkçe, ardından başka dillerde milyonlarca çocuğun uyku öncesi arkadaşı yapmak.

Ortak değerler ve günlük karşılıkları:

1. Önce çocuk: Her kararda çocuğun güvenliği ve iyiliği önce gelir. Bir özellik çocuk için risk taşıyorsa ticari faydası olsa da eklenmez (ör. bulut bağlantısı, ses kaydı, reklam).

2. Gizlilik tasarımdan gelir: Veri toplamamak bir pazarlama vaadi değil, mimari bir karardır. Ürün, sunucumuz kapansa da çalışır.

3. Ölçerek karar veririz: Kaliteyi kör kıyasla, fiyatı testle, talebi ön kayıtla ölçeriz; doğrulama kaybı ya da sezgi tek başına karar vermez. Bu ilke ürünün bugüne kadarki gelişiminde de uygulandı.

4. Dürüstlük ve şeffaflık: Ebeveyne ürünün yapay zekâ kullandığını açıkça söyleriz; sınırlarını (ör. hikâyelerin bazen basit kalması) gizlemeyiz. Yatırımcıya ve TÜBİTAK'a ilerlemeyi olduğu gibi raporlarız.

5. Kültüre saygı: Türkçeyi ve halk kültürünü özenle kullanırız; başkalarının fikri mülkiyetine saygı gösteririz (lisanslı karakterleri izinsiz kullanmayız).

6. Sade ve sorumlu üretim: Uzun ömürlü, onarılabilir, aboneliksiz ürün; gereksiz özellik ve atık üretmeyiz.

Ekibin girişime bağlılığı: Kurucular Yatırım ve Pay Sahipleri Sözleşmesi'ndeki tam zamanlı çalışma taahhüdünü kabul eder; ürün bugüne kadar kurucunun öz kaynaklarıyla geliştirildi; yazılım ve modeller PC'de doğrulandı, kart üzerinde deneme aşamasına getirildi.

## 4 İş Modeli ve Finansal Öngörüler

### 4.1 İş Modeli

*(2552 / 3000 karakter)*

Gelir kaynakları ve iş modelleri:

1. Cihaz satışı (B2C, firmadan tüketiciye) — ana gelir: Eko başlangıç seti 2.999 TL (KDV dahil). Kanallar: kendi web sitemiz, pazaryerleri (Trendyol, Hepsiburada, Amazon.com.tr), ikinci yıldan itibaren oyuncak ve kitap zincirleri. Ön satış: kitle fonlama (Fongogo) ve kaparolu ön sipariş; ilk üretim partisini ön satış finanse eder.

2. Ek figür paketleri (tekrar eden gelir, abonelik yok): 3 figürlük paketler 449 TL (KDV dahil). Lansmanda başlangıç setinde olmayan 10 figür 3 paket halinde satılır (model bu figürleri zaten tanır). Yeni figürler yılda 1–2 paket: model yeniden eğitilir ve ebeveynin telefonundan, cihazın yerel ayar sayfasıyla yüklenir (internet gerekmez; bu güncelleme yolu Aşama 2'de geliştirilecek). Malzeme maliyeti düşük (≈60–80 TL), marj yüksek. Hedef: cihaz başına ortalama 0,8 paket.

3. Kurumsal satış (B2B, firmadan kuruma): Okul öncesi seti (5 cihaz + 13 figür + öğretmen rehberi), 12.000 TL (KDV hariç). Müşteriler özel anaokulları, kreşler, belediye çocuk kütüphaneleri, çocuk hastaneleri oyun odaları. Doğrudan satış ve eğitim fuarları.

4. Yurt dışı satış (3. yıldan itibaren): Almanya, Hollanda, Avusturya'daki Türkçe konuşan aileler için Amazon.de ve Türk dernekleri/hafta sonu okulları; ardından başka dillerde sürümler (İngilizce, Almanca, Azerbaycan Türkçesi). Teknoloji dile bağlı değil: yeni dil için veri, model ve ses yeniden eğitilir.

5. Lisans ve ortak marka (ileride, 2.–3. yıl): (a) Yerli karakter sahipleriyle (Niloya, TRT karakterleri) lisanslı figür paketleri — telif payı ödeyerek; (b) Eko'nun cihaz içi hikâye ve ses teknolojisinin başka oyuncak/kitap üreticilerine lisanslanması (B2B teknoloji lisansı, adet başı ücret).

Gelir kalemlerinin beklenen payı (5. yıl, [V]): cihaz satışı ≈%85, ek figür paketleri ≈%10, kurumsal setler ≈%5 (kurum setleri cihaz adedine dahil edildi); teknoloji lisansı ve yurt dışı satış ek potansiyel olarak tutuldu.

Maliyet yapısı: Birim değişken maliyet ≈1.357 TL (malzeme, montaj, kanal/dağıtım, garanti); sabit giderler personel, ofis, pazarlama, belgelendirme ve kalıp. Sunucu/bulut maliyeti yoktur; şirket için satılan cihaz başına sürekli işletme gideri yoktur (kullanıcı için yalnız pil). Bu, bulut yapay zekâ oyuncaklarına göre yapısal bir maliyet avantajıdır.

Birim ekonomisi (KDV hariç): liste fiyatı 2.499 TL − birim değişken maliyet 1.357 TL = ≈1.142 TL katkı payı (%46); ek paket başına ≈214 TL katkı payı. Müşteri yaşam boyu değeri (cihaz + 0,8 ek paket) ≈1.300 TL, hedef müşteri edinme maliyeti ≤450 TL (LTV/CAC ≈2,9).

### 4.2 Müşteriye Erişim

*(2154 / 3000 karakter)*

1. Ön kayıt sayfası ve topluluk (hızlandırma programı – Aşama 2'nin 1.–9. ayı): Ürün videosu, örnek hikâye sesleri ve "veri toplamayan oyuncak" anlatımıyla ön kayıt sayfası; hedef 1.000 kayıt. Ebeveyn toplulukları (Facebook/WhatsApp anne grupları), çocuk gelişimci ve okul öncesi öğretmeni Instagram hesaplarıyla işbirliği (ücretsiz cihaz + içerik). Bu kanal hem talep testi hem kitle fonlama kitlesi olarak kullanılacak.

2. Pilot ve referanslar (6.–8. ay): 30–50 aile ve 3–5 anaokulu; izinli ebeveyn yorumları ve video referansları, çocuk gelişimi uzmanı görüşü.

3. Kitle fonlama ve ön satış (10.–12. ay): Fongogo'da ödüllü kampanya (hedef 600+ set, ≈1,5 milyon TL); kendi sitemizde kaparolu ön sipariş. Kampanya; basın bülteni (teknoloji ve ebeveyn medyası), "veri sızıntısı" haberlerine karşı "veri toplamayan oyuncak" hikâyesi ve teknopark/TÜBİTAK haberleriyle desteklenecek.

4. Kendi web sitemiz (ön sipariş 10. aydan; teslimat ve satış 17.–18. aydan itibaren): Komisyonsuz doğrudan satış, ek paketlerin satışı, kişisel veri istemeyen garanti kaydı. Performans pazarlaması (Instagram/YouTube, uyku rutini ve ekransız oyun içerikleri); hedef müşteri edinme maliyeti (CAC) ≤ 450 TL.

5. Pazaryerleri (18. aydan itibaren, CE belgesi ve ilk üretimden sonra): Trendyol, Hepsiburada, Amazon.com.tr; 30 saniyelik ses örnekli ürün sayfaları, "Yerli Üretim" rozeti; yılbaşı, 23 Nisan ve karne dönemi kampanyaları. Komisyon (≈%18) fiyatlamada hesaba katıldı.

6. Kurumsal satış (kurum ön siparişleri 12. aydan, teslimat 18. aydan): Özel anaokulu ve kreş zincirlerine doğrudan ziyaret, okul öncesi eğitim fuarları, belediye çocuk kütüphaneleri; pilot okullar referans. Öğretmen rehberi ve kurum faturası.

7. Fiziksel perakende (ticarileşmenin 2. yılı): Toyzz Shop, D&R, idefix, kitapçılar; raf marjı (%35–50) için ayrı fiyat yapısı; mağaza içi "dinle" demo standı.

8. Yurt dışı (ticarileşmenin 3. yılı): Amazon.de, Avrupa'daki Türk dernekleri ve hafta sonu Türkçe okulları; diaspora medyası.

Ölçütler: ön kayıt dönüşümü (≥ %20 kaparo), kampanya hedefi, CAC, iade oranı (< %5), pazaryeri puanı (≥ 4,3), tekrar alım (ek paket bağlanma oranı ≥ 0,5 ilk yıl).

### 4.3 Kritik İş Adımları

| İş tanımı | Öngörülen gerçekleşme tarihi | Doğrulanabilir başarım ölçütleri |
|---|---|---|
| Şirket kuruluşu, İP devri | Ocak 2028 | Tescil, devir sözleşmesi |
| Kartta hız/ses/pil optimizasyonu | Şubat 2028 | Ses gerçek zamanlı, tüketim ölçüldü |
| Marka/tasarım başvurusu | Mart 2028 | TÜRKPATENT başvuru no |
| EVT kartı (30 adet) | Mart 2028 | NFC ≥ %99, ölçüm raporu |
| Pilot serisi (60 cihaz) | Mayıs 2028 | 60 cihaz teslim |
| Pilot (30–50 aile, 3–5 okul) | Temmuz 2028 | ≥ %90 uygun hikâye |
| DVT ve ön uygunluk testi | Eylül 2028 | Ön uygunluk raporu |
| Kitle fonlama kampanyası | Aralık 2028 | ≥ 600 ön sipariş |
| CE/RED belgelendirme | Mart 2029 | Test raporları, DoC |
| İlk üretim partisi | Mayıs 2029 | 1.000 set, fire < %3 |
| Teslimat, web ve pazaryeri | Haziran 2029 | İade < %5, puan ≥ 4,3 |
| Okul öncesi kurum seti | Eylül 2029 | ≥ 20 kurum müşterisi |
| İlk yeni figür paketi | Aralık 2029 | Yerel güncelleme çalışıyor |
| Yurt dışı (Amazon.de) | Eylül 2031 | ≥ 2.000 set/yıl |
| Yıllık 30.000+ set | Haziran 2034 | Kümülatif 86.000 set |

### 4.4 Başa Baş Noktası Analizi (proje süresi 18 ay + 5 yıl; sabit 2026 fiyatları, KDV hariç)

| Tablo 4.4-1 Gelirler | |
|---|---:|
| Satılan ürün adedi | 86.000 |
| Birim satış fiyatı | 2.499 TL |
| Satış gelirleri | 214.914.000 TL |
| Diğer gelirler (ek figür paketleri: 68.800 paket × 374 TL) | 25.731.200 TL |
| **Toplam gelirler** | **240.645.200 TL** |

| Tablo 4.4-2 Değişken maliyetler (birim) | |
|---|---:|
| Personel (montaj, test, flaş yazma) | 60 TL |
| Malzeme (ağırlıklı ortalama; 1.000 adette 1.050 → 10.000+ adette ≈675 TL) | 710 TL |
| Enerji | 5 TL |
| Dağıtım (kanal karışımı: komisyon/indirim + kargo + ödeme) | 507 TL |
| Diğer değişken (garanti/iade karşılığı ≈%3) | 75 TL |
| **Birim ürün maliyeti** | **1.357 TL** |

| Tablo 4.4-3 Sabit maliyetler (toplam) | |
|---|---:|
| Makine ve teçhizat (kalıplar, test düzenekleri, laboratuvar ekipmanı) | 1.858.000 TL |
| Bina amortismanı | 0 TL |
| Kira (kuluçka/teknopark ofisi ve atölye) | 2.508.000 TL |
| Diğer sabit maliyetler (personel, pazarlama, belgelendirme, genel yönetim, Ar-Ge; ek paketlerin değişken maliyeti dahil) | 85.600.000 TL |
| **Toplam sabit maliyet** | **89.966.000 TL** |

| Tablo 4.4-4 Başa baş analizi | |
|---|---:|
| Kâr marjı (birim satış fiyatı − birim ürün maliyeti) | 1.142 TL |
| Satılan ürün adedi olarak başa baş noktası | 78.779 set |

**Varsayımlar:** Satış adetleri yıllara göre 1.000, 4.000, 9.000, 16.000, 24.000, 32.000 (Y0 = 18 aylık proje dönemi). Birim fiyat 2.999 TL (KDV dahil) başlangıç setinin KDV hariç karşılığıdır; ön satıştaki erken alım indirimi pazarlama giderine dahildir. Kur 1 USD = 50 TL. Diğer sabit maliyetlerin dağılımı: personel 39.729.000 TL, pazarlama 26.450.000 TL, belgelendirme 1.550.000 TL, genel yönetim 3.000.000 TL, Ar-Ge ve proje hizmetleri 3.863.000 TL, ek paketlerin değişken maliyeti 11.008.000 TL. Başa baş adedi, 6,5 yılın bütün sabit giderlerini tek kalemde topladığı için kümülatif satışın sonuna yakın çıkar; yıllık bazda FAVÖK ticarileşmenin 2. yılında pozitife döner, kümülatif FAVÖK 3. yılda artıya geçer (bkz. Eko_Finansal_Model.xlsx).

| Yıl | Adet | Ciro (M TL) | Değişken (M TL) | Sabit (M TL) | FAVÖK (M TL) | Dönem sonu kasa (M TL) |
|---|---:|---:|---:|---:|---:|---:|
| Y0 (Oca 2028–Haz 2029, proje) | 1.000 | 2,80 | 1,82 | 3,06 | -2,08 | 0,20 |
| Y1 (Tem 2029–Haz 2030) | 4.000 | 11,19 | 6,54 | 5,56 | -0,91 | 6,03 |
| Y2 (2030–31) | 9.000 | 25,18 | 13,90 | 10,77 | 0,51 | 4,44 |
| Y3 (2031–32) | 16.000 | 44,77 | 23,92 | 15,28 | 5,57 | 7,07 |
| Y4 (2032–33) | 24.000 | 67,16 | 35,16 | 20,19 | 11,81 | 15,52 |
| Y5 (2033–34) | 32.000 | 89,54 | 46,40 | 24,10 | 19,04 | 31,21 |

Kasa, finansmanı içerir: Y0'da BİGG Fonu 1,35 M TL + devam yatırımı 1,35 M TL; Y1 başında tohum turu (BiGG+ ≈5 M TL ve eş yatırım ≈3 M TL) ≈8 M TL [V]. İşletme sermayesi cironun %15'i.

**Başa başın iki ek görünümü:** (a) Ek paket katkısı birim kâra eklenirse (cihaz başına 0,8 paket × 214 TL) başa baş ≈60.126 set olur. (b) Yıllık bakıldığında FAVÖK ticarileşmenin 2. yılında (9.000 set) pozitife döner; kümülatif FAVÖK 3. yılda artıya geçer.

**Kötümser senaryo** (satışlar %40 düşük, devam yatırımı yok, tohum turu 5 M TL; ekip, pazarlama ve diğer sabit giderler Y1'den itibaren %40 küçültülür, kalıp Y1'e ertelenir):

| Yıl | Adet | FAVÖK (M TL) | Dönem sonu kasa (M TL) |
|---|---:|---:|---:|
| Y0 | 600 | -1,77 | -0,68 |
| Y1 | 2.400 | -1,24 | 2,32 |
| Y2 | 5.400 | 0,03 | 1,09 |
| Y3 | 9.600 | 3,18 | 2,51 |
| Y4 | 14.400 | 6,80 | 7,30 |
| Y5 | 19.200 | 11,35 | 16,63 |

Kötümser senaryoda proje döneminin sonunda ≈0,7 M TL açık oluşur. Bu açık ön sipariş kaparoları, ilk partinin 600 setle sınırlanması ve belgelendirmenin parçalara bölünmesiyle kapatılır. FAVÖK 2. yılda başa başa gelir.

### 4.5 Yatırımcı İlişkileri

*(2410 / 3000 karakter)*

Yatırımcı ilişkileri yaklaşımı: Şeffaflık ve düzenli bilgilendirme. TÜBİTAK BİGG Fonu ve ileride katılacak yatırımcılara aylık kısa ilerleme notu (kilometre taşları, nakit durumu, satış ve kalite göstergeleri), altı ayda bir TÜBİTAK dönem raporu (AGY 312) ile uyumlu ayrıntılı rapor; yıllık genel kurul ve denetlenmiş mali tablolar. Önemli sapmalar ve riskler (ör. belgelendirme gecikmesi, kur etkisi) gerçekleştiği anda bildirilir. Pay devri ve yeni yatırım turlarında Yatırım ve Pay Sahipleri Sözleşmesi'ndeki izin ve bilgi hakları gözetilir.

Finansman yol haritası:

1. Tohum öncesi (Aşama 2): TÜBİTAK BİGG Fonu 1.350.000 TL (%3 pay). İlk dönem raporundan sonra tetikleyici koşullar (kitle fonlamada ≥600 ön sipariş, kurumsal sipariş, seri üretime geçiş) belgelenerek ≤1.350.000 TL devam yatırımı talebi (fon payı toplamda ≤ %5).

2. Ön satış geliri: Kitle fonlama ve kaparolu ön sipariş (≈1,5 milyon TL hedef) ilk üretim partisinin malzeme ve kalıp giderlerini karşılar; hisse seyreltmesi olmadan çalışma sermayesi.

3. Teşvikler ve sonraki projeler: Teknopark vergi istisnaları; bu iş planından ayrı yeni projeler (yeni dil ve ürün sürümleri) için ileride KOSGEB Ar-Ge ve İnovasyon ya da TÜBİTAK 1507. Bu iş planının giderleri için başka kamu hibesi kullanılmaz; kullanılırsa TÜBİTAK'a beyan edilir ve mahsup edilir.

4. Tohum turu (Aşama 3, ticarileşmenin 1. yılı): BiGG+ tohum yatırım çağrısı (2026-1 çağrısında üst sınır 8 milyon TL, fon payı ≤ %10) ve melek yatırımcı/girişim sermayesi eş yatırımıyla toplam ≈8 milyon TL [V] (BiGG+ ≈5 M TL, ≤ %10 pay; eş yatırımcı ≈3 M TL; değerleme o günkü satış verisine göre); seri üretim (10.000 adet ölçeği), stok, pazarlama ve yurt dışı açılım için.

5. A serisi (3.–4. yıl): Çok dilli ürün ve teknoloji lisansı için oyuncak/eğitim teknolojisi odaklı girişim sermayesi fonları ya da stratejik yatırımcı (oyuncak üreticisi, yayınevi).

Çıkış stratejisi öngörüleri: (a) Stratejik satın alma: küresel ses oyuncağı şirketleri (tonies, Yoto), oyuncak üreticileri ya da eğitim teknolojisi şirketleri için cihaz içi, gizlilik odaklı yapay zekâ teknolojisi ve Türkçe pazar erişimi değerli bir satın alma hedefi; (b) Sonraki turlarda erken yatırımcıların paylarının yeni yatırımcılara devri (ikincil satış); (c) Uzun vadede, ölçek yakalanırsa halka arz (Borsa İstanbul GİP). BİGG Fonu'nun 12 yıllık süresi ve 6 yıllık yatırım dönemi, çıkış planlamasında dikkate alınacaktır.

## 5 Risk Yönetimi

### 5.1 Projenin Yürütülmesi Sırasında Karşılaşılabilecek Riskler ve Alınacak Önlemler

| Risk tanımı | Önlemler | Olasılık | Etki | B planı |
|---|---|---|---|---|
| Hikâye kalitesi ebeveyni tatmin etmez | 5 aday+seçici, veri artırımı, kör pilot | Orta | Yüksek | Hazır hikâye kütüphanesi + seçici eşiği |
| Ses sentezi kartta gerçek zamanlı değil | SIMD optimizasyon, iki çekirdek | Orta | Orta | Hafif vocoder ya da ses önbelleği |
| Pil ömrü kısa (4×AA ≈2–3 saat) | Tüketim ölçümü, boşta üretim sınırı | Yüksek | Orta | USB-C güç girişi / şarjlı pil |
| CE/RED belgelendirmede gecikme | Erken ön tarama, uyumlu tasarım | Orta | Yüksek | İkinci laboratuvar, takvime 2 ay pay |
| Kitle fonlama hedefi tutmaz | Ön kayıt ≥1.000, pilot referansı | Orta | Yüksek | Kurumsal satış ve küçük parti üretim |
| Tek kişilik ekip, kilit kişi riski | Kurucu ortak, yazılı danışman taahhüdü | Orta | Yüksek | Hizmet alımı; devam yatırımıyla işe alım |

**Ayrıntı (formun hücreleri kısa olduğu için):**

1. **Hikâye kalitesi ebeveyni tatmin etmez** (olasılık orta, etki yüksek). Önlem: 5 aday üretip seçiciyle en iyisini saklama; isim süzgeci ve kapalı dünya; veri artırımı (kalite veriyle artıyor); pilotta insan hakemli kör kalite testi ve kabul eşiği. B planı: Her figür için önceden üretilmiş, denetimden geçmiş hikâyelerden oluşan bir başlangıç kütüphanesi kuyrukta hazır tutulur; seçici eşiği yükseltilir, eşiği geçemeyen hikâye okunmaz.
2. **Ses sentezi kartta gerçek zamanlı değil** (orta/orta). PC ölçümüne göre ESP32-S3'te saniyelik ses için 0,7–1,4 sn hesap tahmin ediliyor. Önlem: ESP32-S3 vektör (SIMD) komutlarıyla vocoder, iki çekirdekte paralel işlem. B planı: Daha hafif vocoder ya da hikâyenin sesinin boşta önceden sentezlenip önbellekte tutulması.
3. **Pil ömrü kısa** (yüksek/orta). Kart 5 V'ta ≈0,5–0,9 A çekiyor; 4 × AA ile hesapla ≈2–3 saat okuma çıkıyor ve mikrofon sürekli dinlediği için kart derin uykuya giremiyor. Önlem: kartta tüketim ölçümü, halka parlaklığı ve ses düzeyi sınırı, boşta hikâye üretimini yalnız adaptörde yapma, okuma bitince uyku. B planı: USB-C güç girişi (adaptörle sürekli çalışma) ya da şarjlı pil paketi (IEC 62133 ve UN 38.3 testleri eklenir).
4. **CE/RED belgelendirmede gecikme ya da başarısızlık** (orta/yüksek). Önlem: Standartlara uygun tasarım (vidalı pil kapağı, NFC anten uyumu), DVT'de ön uygunluk taraması. B planı: İkinci akredite laboratuvar; takvime 2 ay tampon; gerekirse Wi-Fi ayar modu yerine NFC-yalnız ayar.
5. **Kitle fonlama hedefi tutmaz** (orta/yüksek). Önlem: Kampanya öncesi ≥1.000 ön kayıt, pilot referansları, basın. B planı: Kurumsal satış (anaokulları) ve 300 adetlik küçük parti; alüminyum kalıp ya da 3B baskı ile düşük yatırım; devam yatırımı.
6. **Tek kişilik ekip, kilit kişi riski** (orta/yüksek). Önlem: Hızlandırma programında donanım/üretim kurucu ortağı ve yazılı taahhütlü danışmanlar; kod, veri ve süreçlerin belgelenmesi. B planı: Bütçedeki hizmet alımları; devam yatırımıyla donanım mühendisi işe alımı.
7. **Bileşen fiyatı ve kur artışı** (yüksek/orta; tabloda yer kalmadı). Önlem: ESP32 modülü için ikinci kaynak, ön satışta fiyat sabitleme, toplu alım. B planı: Set içeriği ve fiyatın dönemsel güncellenmesi.
8. **Marka ya da karakter tasarımına hukuki itiraz** (düşük/orta). Önlem: Avukat görüşü, TÜRKPATENT araştırması, Keloğlan kartındaki dizi kaynaklı yan karakterlerin değiştirilmesi. B planı: Ürün ya da karakter adının değiştirilmesi.
