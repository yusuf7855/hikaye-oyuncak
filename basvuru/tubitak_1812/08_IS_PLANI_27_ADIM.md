# Hızlandırma programının 27 iş planı bileşeni: Eko için taslak cevaplar

> TÜBİTAK'ın Aşama 1 kılavuzu (`resmi/1812_Asama_1_Kilavuz.pdf`, bölüm 3.2), hızlandırma programı sonunda
> girişimcinin şu 27 soruyu cevaplamış olmasını bekliyor. 7 modülün haftalık görevleri bunlara göre kurulu.
> Aşağıda her biri için bugünkü taslak cevap ve AGY 112'deki yeri var. **[DOĞRULA]** işaretli olanlar programda
> müşteriyle test edilmesi gerekenler.

## Modül 1 — Müşteri ve pazar

1. **İş tanımı.** Eko; 3–6 yaş çocuklara her seferinde yeni bir Türkçe hikâye yazıp kendi sesiyle okuyan,
   internete bağlanmayan, figürlü bir hikâye oyuncağı. Sektör: eğitici oyuncak / tüketici elektroniği, cihaz içi
   yapay zekâ. → AGY 112 §1.1
2. **Problem/ihtiyaç.** Ebeveyn: ekransız ama çeşitli içerik; çocuk verisinin korunması; her gece yeni masal
   uydurmanın zorluğu. Ölçülebilir hali: haftalık hikâye dinleme sıklığı, "çocuk sıkıldı" beyanı, ekran süresi.
   **[DOĞRULA: 30+ ebeveyn görüşmesi]** → §1.3
3. **Pazar segmentasyonu.**
   - (a) kentli orta-üst gelirli, ekran kaygılı ebeveynler;
   - (b) hediye alıcılar (büyükanne-büyükbaba);
   - (c) özel anaokulu ve kreşler;
   - (d) yurt dışındaki Türkçe konuşan aileler;
   - (e) belediye çocuk kütüphaneleri.

   → §1.2
4. **Odak pazar.** (a) segmenti, İstanbul–Ankara–İzmir'de, çevrimiçi satın alan ebeveynler.
   - Erişilebilir: Instagram ve ebeveyn toplulukları.
   - Ödeme isteği yüksek: lisanslı konuşan peluşa 4.700+ TL ödeniyor.
   - Rakip baskısı düşük: Türkçe cihaz içi ürün yok.

   **[DOĞRULA: ön kayıt dağılımı]**
5. **Persona ve kullanıcı yaşam döngüsü.**
   - *Persona — "Elif, 34, İstanbul":* pazarlamacı, 4 yaşında oğlu var. Akşam 20.30'da yorgun; oğlu her gece
     "bir masal daha" istiyor. Tableti kısıtlamak istiyor ama alternatif bulamıyor. Instagram'da çocuk gelişimi
     hesaplarını takip ediyor, Trendyol'dan alışveriş yapıyor. "Yapay zekâ" deyince merak ediyor ama verinin
     nereye gittiğinden kaygılanıyor.
   - *Kullanıcı — "Can, 4":* Keloğlan'ı ve Bip robotu seviyor. Okuma bilmiyor; figürü standa koymayı ve "bir
     daha!" demeyi seviyor.
   - *Yaşam döngüsü:* farkındalık (Instagram/ebeveyn grubu) → örnek ses dinleme → ön sipariş ya da satın alma →
     kutu açılışı (kurulum yok) → ilk hafta günlük kullanım → uyku rutinine girmesi (Ay Dede) → yeni figür
     isteği (ek paket) → tavsiye.
   - Kritik anlar: uyku öncesi, araba yolculuğu, hasta günler, hafta sonu sabahları.
6. **Rakip analizi ve satın alma kriterleri.** Rakipler: Toniebox, Yoto, Storypod, Miko, Curio, Elaves Sunny,
   sabit masallı yerli oyuncaklar (→ §1.5).

   Satın alma kriterleri (öncelik sırası tahmini):

   1. güvenlik ve gizlilik,
   2. eğiticilik / yaşa uygunluk,
   3. fiyat,
   4. çocuğun ilgisinin sürmesi,
   5. kullanım kolaylığı,
   6. yorumlar.

   **[DOĞRULA: anket sıralaması]**
7. **TAM.**
   - TAM: Türkiye ≈3,3 milyon hane × 2.499 TL (KDV hariç) ≈ 8,2 milyar TL; her yıl ≈0,93 milyon yeni çocuk
     (≈2,3 milyar TL).
   - SAM: ≈1,0 milyon hane, ≈2,5 milyar TL.
   - SOM (6,5 yıl): 86.000 set.
   - Komşu segmentler: kurumlar, diaspora, başka diller.

   → §1.4

## Modül 2 — Değer önerisi ve ürün

8. **Ürün/çözüm.** Stand cihazı (hoparlör, ışık halkası, NFC okuyucu, mikrofon) + figürler + Ay Dede + ayar kartı.
   Cihaz içi dil modeli, ses sentezi ve sesli komut. → §1.1, §2.1
9. **Değer önerisi ve özellik–fayda.** "Ekransız, internetsiz, her seferinde yeni bir Türkçe masal; çocuğunuzun
   sesi hiçbir yere gitmez." Özellik–fayda eşleşmesi §2.1'de. Sayısallaştırma:
   - sınırsız yeni hikâye (rakiplerde figür başına 1 kayıt),
   - 0 bayt veri gönderimi,
   - 0 TL abonelik,
   - rakip ses kutularından ≈%45–55 ucuz.
10. **MVP (minimum işlevsel ürün).** 3D baskı kasa + ESP32-S3 geliştirme kartı + hoparlör + NFC + 6 figür.
    Hikâye anlatma, "başka/dur/devam" komutları, Ay Dede ninni modu. Işık halkası ve ayar kartı isteğe bağlı.
    Bütün yazılım parçaları hazır; kart üzerinde uçtan uca test bekliyor.
11. **Talep testi.**
    - Ön kayıt sayfası: 30 sn demo videosu, 3 örnek hikâye sesi, "veri toplamayan oyuncak" anlatımı. Hedef
      1.000 kayıt.
    - İki fiyatla A/B testi (2.499 / 2.999 TL) ve 100 TL iadeli kaparo. Başarı ölçütü: kaparo oranı ≥%20.
    - Anaokulu görüşmeleri: 10 görüşme, ≥3 niyet mektubu.

    **[YAPILACAK]**

## Modül 3 — Teknoloji ve fikri mülkiyet

12. **TRL analizi (bugün → proje sonu).**

    | Bileşen | Bugün | Kanıt | Hedef (18. ay) |
    |---|---|---|---|
    | Türkçe dil modeli | TRL 4 | 28.493 hikâyeyle eğitim, yapay zekâ hakemli kör kıyaslar, golden testi (C = PyTorch); insan hakemli test yok | TRL 7 (pilot), 8 (ürün) |
    | Kart yazılımı (seçici, kuyruk, NFC, halka, ayar) | TRL 4 | PC'de sahte ESP32 başlıklarıyla birebir aynı çıktı (52/52, 872/872), ürün akışı testleri | TRL 7–8 |
    | Konuşma sentezi | TRL 4 | C çıkarımı = PyTorch (SNR ≥ 79 dB); gerçek zamanlılık kartta ölçülmedi | TRL 7–8 |
    | "Merhaba Eko" ve komutlar | TRL 3–4 | Sentetik ve çocuk benzetimi seslerle: uyanma %87–93, saatte 0,3–1,9 yanlış uyanma; gerçek çocuk sesiyle denenmedi | TRL 6–7 (pilotta ebeveyn beyanıyla) |
    | Donanım (kart, kasa, figür) | TRL 3 | Parça listesi, pin haritası, CAD çizimleri; masa üstü kurulum | TRL 8 (CE belgeli DVT/PVT) |
    | **Bütün sistem** | **TRL 4** | | **TRL 8** |

    Teknik riskler:

    - ses sentezinin kartta gerçek zamanlı olması;
    - hoparlör çalarken uyanma oranının düşmesi (bilinen zayıflık: aynı yükseklikte %60);
    - pil ömrü;
    - EMC/RED uyumu.
13. **Teknik doğrulama planı.**

    | Test | Ölçüt | Ne zaman |
    |---|---|---|
    | Kartta hikâye üretim hızı | ≥3,5 token/s, hikâye ≤40 sn; kuyruklu kullanımda bekleme ≤2 sn | Ay 1–2 |
    | Ses sentezi gerçek zamanlılık | Hesap süresi / ses süresi ≤1,0 (iki çekirdek) | Ay 1–3 |
    | Pil ömrü ve tüketim | Kartta ölçüm; 4×AA ile hesap ≈2–3 saat okuma (kart 5 V'ta ≈0,5–0,9 A). Hedef: ≥3 saat okuma ya da USB-C güç girişi | Ay 1–3 (EVT) |
    | Uyanma sözcüğü ve komutlar | Çocuk sesinde uyanma ≥%85 (ebeveyn beyanı), yanlış uyanma ≤0,5/saat | Pilot, ay 5–7 |
    | NFC figür tanıma | ≥%99 ilk denemede | EVT, ay 4 |
    | İçerik kalitesi | Uygunsuz < %1, anlaşılır ≥%90 (kör ebeveyn testi) | Pilot |
    | EMC/RED ve EN 62115 ön tarama | Akredite laboratuvardan geçer raporu | DVT, ay 9 |
    | Düşme ve küçük parça (EN 71-1) | Ön test geçer | DVT, ay 9 |
14. **Fikri mülkiyet stratejisi.**
    - Marka: "Eko" ve karakter adları, sınıf 9/16/28/41, önce Türkiye.
    - Tasarım tescili: stand ve özgün figürler.
    - Faydalı model araştırması: figür tanımalı, cihaz içi üretim ve kuyruk sistemi.
    - Ticari sır: veri üretim ve hakem süreçleri.
    - Yazılım telifi (FSEK).
    - Coğrafya: Türkiye, sonra AB (EUIPO marka).

    → §2.6
15. **Özgünlük ve teknik farklılaşma.** Üç modelin tek mikrodenetleyicide birlikte çalışması; Türkçe veri seti ve
    kör kıyas yöntemi; bit düzeyinde doğrulanmış güvenlik süzgeçleri. Açık kaynak demolar İngilizce ve yalnız
    metin. → §2.2

## Modül 4 — Müşteri kazanımı

16. **Satış kanalları.**
    1. Kendi web sitemiz: marj yüksek, veri istemeyen garanti kaydı.
    2. Pazaryerleri: hacim; %18 komisyon.
    3. Kitle fonlama (Fongogo): ön satış.
    4. Kurum satışı: anaokulları.
    5. Perakende zincirleri (2. yıl): raf marjı %35–50.
    6. Amazon.de (3. yıl).

    → §4.2
17. **Pazara giriş stratejisi.** Ön kayıt topluluğu → pilot referansları → kitle fonlama (Aralık 2028, yılbaşı
    dönemi) → teslimattan sonra pazaryeri ve web (23 Nisan ve karne kampanyaları). Mesaj: "Ekransız, internetsiz,
    her gece yeni bir masal."
18. **Müşteri kazanımı deneyleri.**

    - Instagram reklamlarında üç mesajla A/B testi:
      1. gizlilik,
      2. ekransız,
      3. yeni hikâye.

      Ölçüt: tıklama ve kayıt oranı.
    - Çocuk gelişimci işbirliğinde kayıt başına maliyet.
    - Anaokulu demo günü dönüşümü.
    - Hedef: kayıt başına maliyet ≤40 TL, kayıttan satışa dönüşüm ≥%10. Buradan CAC ≤450 TL hesaplanır.

    **[YAPILACAK]**

## Modül 5 — İş modeli ve finans

19. **Gelir modeli ve fiyat.** Cihaz satışı (2.999 TL), ek figür paketleri (449 TL), kurum seti (12.000 TL),
    ileride teknoloji lisansı. Abonelik yok. → §2.3, §4.1
20. **LTV, CAC, LTV/CAC.**
    - Cihaz katkı payı ≈1.142 TL.
    - Ek paket katkı payı ≈214 TL × 0,8 paket.
    - LTV ≈1.313 TL.
    - Hedef CAC ≤450 TL.
    - LTV/CAC ≈2,9. Hedef ≥3: paket bağlanma oranını ve organik payı artırarak.

    → `cikti/Eko_Finansal_Model.xlsx`, "Birim ekonomisi" sayfası
21. **Üç yıllık finansal projeksiyon** (sabit 2026 TL, KDV hariç; ayrıntı Excel "Projeksiyon" sayfası):

    | | Y0 (18 ay, proje) | Y1 | Y2 | Y3 |
    |---|---:|---:|---:|---:|
    | Satılan set | 1.000 | 4.000 | 9.000 | 16.000 |
    | Ciro (M TL) | 2,80 | 11,19 | 25,18 | 44,77 |
    | Brüt katkı (M TL) | 0,97 | 4,65 | 11,28 | 20,85 |
    | Sabit gider (M TL) | 3,06 | 5,56 | 10,77 | 15,28 |
    | FAVÖK (M TL) | −2,08 | −0,91 | 0,51 | 5,57 |
    | Dönem sonu kasa (M TL) | 0,20 | 6,03 | 4,44 | 7,07 |
    | Ekip (kişi) | 1 | 4 | 7 | 10 |

    Kasa şu finansmanı içerir:
    - Y0: BİGG 1,35 M + devam yatırımı 1,35 M;
    - Y1: tohum turu ≈8 M (BiGG+ ≈5 M + eş yatırımcı ≈3 M).

    Kötümser senaryo (satış −%40, devam yatırımı yok): Excel'deki "Kötümser senaryo" sayfası ve AGY 112 §4.4.

## Modül 6 — Operasyon ve ölçeklenme

22. **18 aylık yol haritası ve finansal ihtiyaç.** Kritik iş adımları: AGY 112 §4.3. Finansal ihtiyaç:
    - Proje bütçesi: 1.350.000 TL. Personel 729 bin, hizmet 393 bin, malzeme 150 bin, teçhizat 58 bin,
      seyahat 20 bin.
    - Ek ihtiyaç ≈1,6 M TL: kalıp 0,7 M, tam belgelendirme 0,45 M, ilk parti çalışma sermayesi, kampanya.
      Ön satış ve devam yatırımıyla karşılanacak.
23. **Fonlama stratejisi.**
    1. BİGG Fonu 1,35 M TL (%3).
    2. Ön satış ≈1,5 M TL.
    3. Devam yatırımı ≤1,35 M TL (tetikleyici: ≥600 ön sipariş ya da kurumsal sipariş).
    4. Teknopark vergi istisnaları. KOSGEB ya da TÜBİTAK 1507 yalnız bu iş planından ayrı yeni projeler
       için; aynı giderler için başka kamu hibesi alınırsa beyan edilir ve mahsup edilir.
    5. BiGG+ tohum (≤8 M TL, ≤%10) + melek/GSYF eş yatırımı ≈4 M TL (ticarileşmenin 1. yılı).
    6. A serisi (3.–4. yıl).

    → §4.5
24. **Ekip yapısı ve danışma kurulu.**
    - Bugün: kurucu (yapay zekâ, gömülü yazılım).
    - Eksik yetkinlikler:
      - donanım/üretim (kurucu ortak),
      - çocuk gelişimi (danışman),
      - pazarlama/e-ticaret (danışman),
      - hukuk/fikri mülkiyet (vekil).
    - Y1'de 4 kişi: +gömülü/yapay zekâ mühendisi, +operasyon ve müşteri ilişkileri.
    - Danışma kurulu hedefi: 1 çocuk gelişimi akademisyeni, 1 oyuncak sektörü yöneticisi, 1 donanım girişimcisi.

    → §3
25. **Yasal düzenlemeler ve uyum.** CE (EN 71-1/2/3, EN IEC 62115), RED (NFC, Wi-Fi ayar modu), RoHS/REACH,
    AEEE/TAP, KVKK (veri işlenmiyor), AB Yapay Zekâ Yasası md. 50 şeffaflığı, etik kurul. → §2.7
26. **Uluslararasılaşma.**
    - 3. yıl: Almanya, Hollanda ve Avusturya'daki Türk diasporası (Amazon.de, dernekler, hafta sonu okulları).
    - 4.–5. yıl: yeni dil sürümleri. Önce Azerbaycan Türkçesi, sonra İngilizce ve Almanca. Teknoloji dile
      bağlı değil; her dil için veri, model ve ses yeniden eğitilir.
    - AB uyumu: Pil Tüzüğü (2027), CRA (2027), yeni Oyuncak Tüzüğü (2030).

## Modül 7 — Etki ve vizyon

27. **Etki, değişim teorisi, SKA.**
    - Değişim teorisi: ekransız, güvenli, yeni içerik → çocuk dinlemeye ve hayal etmeye yönelir; ebeveyn ekran
      süresini azaltır → dil ve dinleme becerileri, aile içi hikâye konuşmaları artar; çocuk verisi korunur.
    - Göstergeler:
      - ulaşılan çocuk ve kurum sayısı;
      - ebeveyn beyanıyla ekran süresinde azalma;
      - haftalık dinleme sıklığı;
      - toplanan çocuk verisi (hedef: 0 bayt).
    - SKA 4.2, 8, 9, 10, 12, 16.2.

    → §1.8
