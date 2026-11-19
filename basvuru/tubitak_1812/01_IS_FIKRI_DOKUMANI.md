# İş Fikri Dokümanı (Aşama 1 – Hızlandırma Programı Başvurusu)

> **Nasıl kullanılır:** PRODİS'te başvurduğunuz hızlandırma programının "İş Fikri Başvurusu Dokümanı" Word
> şablonunu indirin. Her programın şablonu biraz farklıdır; aşağıdaki bölümleri şablondaki karşılık gelen
> başlıklara yapıştırın, sonra PDF olarak kaydedip PRODİS'e yükleyin. Bölümler, uygulayıcı kuruluşun puanladığı
> dört ölçüte göre düzenlendi; her ölçütten **en az 7/10** almak gerekiyor:
> (1) iş fikrinin içeriği ve niteliği, (2) ürünün pazar durumu, (3) ekibin yetkinliği ve uyumu,
> (4) ön hazırlık çalışmalarının yeterliliği.
>
> Köşeli parantezli büyük harfli yerleri ([AD SOYAD] gibi) siz doldurun. **İş fikri adı PRODİS'te sonradan
> değiştirilemez.**

**İş fikri adı:** Eko: İnternetsiz Çalışan, Cihaz İçi Yapay Zekâlı Türkçe Hikâye Oyuncağı

**Tematik alan:** İletişim ve Sayısal Dönüşüm — Yapay Zekâ (yan alanlar: Ses/Görüntü/Metin İşleme, Eğitim,
Elektronik Sistemler)

**Girişimci:** [AD SOYAD], [ÜNİVERSİTE / BÖLÜM / ÖĞRENCİ ya da MEZUN], [İL], [TELEFON], [E-POSTA]

---

## 1. Özet (en fazla 1 paragraf)

Eko, 3–6 yaş çocuklar için internete hiç bağlanmadan çalışan, her seferinde yeni bir Türkçe hikâye yazıp kendi
sesiyle okuyan bir hikâye oyuncağıdır. Çocuk sevdiği figürü (Keloğlan, Nasreddin Hoca, Pinokyo ya da Bulut kedi,
Zıpzıp tavşan gibi özgün karakterlerimiz) standa koyar; Eko figürü tanır ve o figürün dünyasında geçen, daha önce
hiç anlatılmamış bir hikâye okur. Bütün yapay zekâ (dil modeli, konuşma sentezi, "Merhaba Eko" sesli komutları)
tek bir ESP32-S3 mikrodenetleyicide çalışır. Hiçbir veri göndermez, abonelik ve sunucu gerektirmez. Bugün çalışan
yazılım ve eğitilmiş modellerle TRL 4 düzeyindeyiz. Hızlandırma programında ebeveyn ve okul doğrulaması yapıp
yatırıma hazır iş planını tamamlamayı hedefliyoruz.

## 2. İş fikrinin içeriği ve niteliği (ölçüt 1)

**Problem.** Ebeveynler çocukları için ekransız ama zengin içerik arıyor. Mevcut ses kutuları (Toniebox, Yoto)
her figür için hep aynı kaydı çalar; çocuk birkaç dinlemede sıkılır, yeni içerik için yeni figür almak gerekir.
Bulut yapay zekâlı oyuncaklar (Miko, Curio, FoloToy, Bondu) ise çocuğun sesini ve bilgisini sunuculara gönderir.
2025–2026'da bu ürünlerde uygunsuz yanıtlar oldu, on binlerce çocuk sohbeti açığa çıktı, sunucusu kapanan
oyuncaklar (Moxie) çalışmaz oldu. Türkçe içerik ise her iki grupta da yok denecek kadar az.

**Çözüm.** Eko, hikâyeyi cihazın içinde üretir:

- **Türkçe dil modeli:** ≈19,9 M parametre (5,7 M çekirdek + flaşta duran sözcük tablosu), 10,3 MB, 4 bit. Önce kısa bir "Sorun/Çözüm" planı,
  sonra hikâye yazar. 28.493 özgün çocuk hikâyesiyle eğitildi.
- **Konuşma sentezi:** Karta özel, 4,3 MB. Ticari kullanıma açık bir öğretmen sesten (VoxCPM2, Apache-2.0)
  damıtıldı. Gece modunda yavaş ve kısık okur.
- **Uyandırma sözcüğü ve komutlar:** ≈110 KB'lık model. "Merhaba Eko" + "dur, devam, başka, bir daha, sesini
  aç/kıs" komutlarını tanır; mikrofon cihaz dışına hiçbir şey göndermez.
- **İçerik güvenliği:**
  - Her figürün kapalı bir dünyası (yerler, yan karakterler, girmeyecek öğeler) var.
  - İsim süzgeci başka figürlerin adını yazdırmaz.
  - Her hikâye için 5 aday üretilir; bir seçici en iyisini seçer.
  - Boştayken hikâyeler önceden yazılıp kuyrukta saklanır, oyuncak konunca beklemeden okunur.
- **Ninni modu:** Ay Dede figürüyle 100 anonim halk ninnisi.

**Yenilikçi yön.**

1. Üç yapay zekâ modeli (dil, ses, ses tanıma) 16 MB flash ve 8 MB PSRAM'li tek bir mikrodenetleyicide
   birlikte çalışıyor.
2. Türkçeye özgü veri üretim ve hakem süreci, kör ikili kıyas yöntemiyle ölçülen kalite.
3. Gizlilik tasarımdan geliyor: ağ yok, kayıt yok.

Türkçe, ticari ve ses sentezi + içerik güvenliğiyle bütünleşik bir örnek bulamadık. Açık kaynakta İngilizce
TinyStories demoları var.

**Yapılabilirlik kanıtı.**

- Kart yazılımı PC'de ESP32 başlıklarıyla derlenip referans üretimle karşılaştırıldı: 52/52 aday ve seçicide
  872/872 birebir aynı.
- Ses modelinin C çıkarımı PyTorch ile aynı sonucu veriyor (SNR ≥ 79 dB).
- Eklenen her veri setiyle kalite kör kıyasta anlamlı olarak arttı (hakemler yapay zekâ; insan hakemli kör test
  pilotta yapılacak):
  - son model ara modeli 180 vakada 102–78 (genel) ve 99–73 (olay örgüsü) yendi;
  - Keloğlan'da önceki ürün modelini 48 vakada 34–14 ve 29–15 yendi.

## 3. Ürün ve hizmetin pazar durumu (ölçüt 2)

**Hedef müşteri.**

- 3–6 yaş çocuğu olan, kentli, orta ve üst-orta gelirli, ekran süresinden kaygılı ebeveynler.
- Hediye alıcılar (büyükanne-büyükbabalar).
- Özel anaokulları ve kreşler.
- Yurt dışındaki Türkçe konuşan aileler.

**Pazar büyüklüğü.**

- Türkiye'de 2028'de ≈3,8–3,9 milyon 3–6 yaş çocuk ve ≈3,3 milyon hane (TÜİK doğum verilerinden türetildi).
  KDV hariç 2.499 TL'lik setle bu, ≈8,2 milyar TL'lik bir toplam pazar; her yıl ≈0,93 milyon yeni çocuk bu yaşa
  girer (≈2,3 milyar TL).
- Ulaşılabilir pazar (kentli, orta-üst gelir, ≈%30): ≈1,0 milyon hane, ≈2,5 milyar TL. Ek olarak MEB'e bağlı ≈17,6
  bin anaokulu ve özel kreşler.
- Dünyada ekransız ses oyuncakları hızla büyüyor: tonies 2025'te 630 M€ ciro yaptı (+%31), Yoto ≈95 M£.
- Türkiye oyuncak pazarı ≈1 milyar USD ve %85'i ithal.

**Rakipler ve konum.**

| | Eko | Toniebox / Yoto | Miko / Curio (bulut) | Yerli sabit masallı oyuncak |
|---|---|---|---|---|
| Her seferinde yeni hikâye | Var (cihazda) | Yok | Var (bulutta) | Yok |
| İnternetsiz | Tamamen | Kurulumdan sonra | Yok | Var |
| Veri gönderimi | Yok | Hesap/kullanım | Ses ve sohbet | Yok |
| Abonelik | Yok | Kart/figür, kulüp | ≈15 USD/ay | Yok |
| Türkçe | Ana dil | Çok az | Zayıf | 3–5 masal |
| Fiyat | 2.999 TL | 5.400–6.800 TL | ≈10.000 TL + abonelik | ≈1.600 TL |

En yakın yerli rakip **Elaves Sunny**: ekransız, 0–5 yaş, ABD odaklı; yapay zekâyı içerik hazırlamada arka planda
kullanıyor, cihazda hikâye üretmiyor.

**İş modeli.**

- Başlangıç seti: 2.999 TL; cihaz + 3 figür + Ay Dede.
- Ek figür paketleri: 449 TL; abonelik yok, tekrar eden gelir.
- Okul öncesi kurum seti: 5 cihaz.
- Kanallar: kendi web sitemiz, Trendyol/Hepsiburada, kitle fonlama (ön satış), ikinci yılda perakende.
- Birim katkı payı ≈1.140 TL (KDV hariç, %46).
- Sunucu maliyeti olmadığı için satılan cihaz başına sürekli gider sıfır.

## 4. Proje ekibinin yetkinliği ve uyumu (ölçüt 3)

**[AD SOYAD] — kurucu, teknik lider.** [ÜNİVERSİTE, BÖLÜM, ÖĞRENCİ/MEZUN]. Eko'nun bugünkü sürümünü uçtan uca
geliştirdi ve yönetti:

- veri seti ve hakem süreçleri,
- dil modelinin eğitimi ve değerlendirmesi,
- ESP32 kart yazılımı,
- donanım entegrasyonu (NFC, ses, ışık halkası),
- konuşma sentezi ve uyandırma modelleri.

[DENEYİM, PROJELER, YARIŞMALAR, BURSLAR EKLEYİN.]

**[AD SOYAD ya da "aranıyor"] — kurucu ortak, donanım ve üretim.** [Elektrik-elektronik / mekatronik mühendisi;
PCB, EMC ve seri üretim deneyimi.]

**Danışmanlar:**

- çocuk gelişimi / okul öncesi eğitim uzmanı [AD SOYAD, UNVAN],
- pazarlama ve e-ticaret danışmanı [AD SOYAD].

**Ekibin uyumu:** [Birlikte çalışma geçmişi, iş bölümü.] Kurucu, girişime tam zamanlı katılmayı ve Yatırım ve
Pay Sahipleri Sözleşmesi'ndeki çalışma taahhüdünü kabul eder.

> Öneri: Ekip ölçütünden 7+ almak için başvurudan önce en az bir donanım/üretim yetkinliği olan kurucu ortak ya da
> yazılı taahhüt veren bir danışman bulun (bkz. `07_EKSIKLER_VE_UYARILAR.md`).

## 5. Ön hazırlık çalışmalarının yeterliliği (ölçüt 4)

**Yapılanlar (Kasım 2026):**

- Pazar, hukuk ve maliyet araştırması: rakipler, fiyat bantları, CE/RED gereklilikleri, karakter lisansı,
  malzeme listesi ve birim maliyet. Lisanslı karakterler bu araştırma sonucunda üründen çıkarıldı.
- Ürün tanımı: etkileşim, sesli komutlar, uyku modu, ayar kartı, ışık halkası davranışları.
- 13 figürün içerik kuralları (figür kartları) ve 28.493 hikâyelik eğitim verisi.
- Eğitilmiş modeller: dil, ses, uyandırma sözcüğü. Kör kıyas raporları.
- Kart yazılımı ve PC'de birebir doğrulama.
- 3B kasa ve figür tasarımları (CAD).
- Masa üstü prototip parça listesi.
- Bu iş fikri dokümanı ve taslak iş planı (AGY 112), 18 aylık bütçe ve 6,5 yıllık finansal model.

**Hızlandırma programında yapılacak doğrulama:**

1. 30+ ebeveyn ve 10 anaokulu yöneticisiyle problem ve çözüm görüşmeleri.
2. Ön kayıt sayfası (hedef 1.000 kayıt) ve iki fiyatla A/B testi (2.499 / 2.999 TL), kaparo ile niyet ölçümü.
3. Etik kurul başvurusu ve 30–50 ailelik pilotun tasarımı.
4. Kartta uçtan uca prototip: hız, pil süresi ve ses kalitesinin ölçülmesi.
5. Patent/marka ön araştırması (TÜRKPATENT, Espacenet).

## 6. Tahmini bütçe ve takvim

**Aşama 2 (18 ay, TÜBİTAK BİGG Fonu 1.350.000 TL yatırımı, %3 pay):**

| Kalem | Tutar (TL) | Pay |
|---|---:|---:|
| Personel (proje yürütücüsü, 18 adam-ay) | 729.000 | %54 |
| Hizmet alımları (test laboratuvarı ön tarama, PCB/DFM, endüstriyel tasarım, patent/marka, çocuk gelişimi + etik kurul, mali müşavir) | 393.000 | %29 |
| Malzeme (EVT 30 kart, DVT 60 cihaz, pilot figürleri) | 150.000 | %11 |
| Alet/teçhizat (osiloskop, 3B yazıcı, güç kaynağı) | 58.000 | %4 |
| Seyahat (fuar, üretici ziyaretleri) | 20.000 | %2 |
| **Toplam** | **1.350.000** | **%100** |

Kalıp (≈700 bin TL), tam CE/RED belgelendirmesi (≈450 bin TL) ve ilk üretim partisi şu kaynaklarla karşılanacak:

- ön satış (kitle fonlama, hedef 600+ set),
- ilk dönem raporundan sonra devam yatırımı talebi (≤1.350.000 TL),
- teknopark vergi istisnaları. Aynı iş planının giderleri için başka kamu hibesi kullanılmaz; kullanılırsa
  TÜBİTAK'a beyan edilir ve destekten mahsup edilir.

**Takvim (hedef):**

| Dönem | İş |
|---|---|
| Aralık 2026 – Haziran 2027 | Hızlandırma programı |
| 26 Temmuz – 13 Ağustos 2027 | 2027-2 tohum öncesi yatırım çağrısına iş planı başvurusu |
| Ocak 2028 | Destek başlangıcı |
| Haziran 2029 | İlk 1.000 setin satışı |
