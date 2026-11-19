# Özgeçmiş taslağı (hızlandırma programı başvurusu için)

> **Neden gerekli?** PRODİS kılavuzuna göre İş Fikri Formu'nda girişimci "özgeçmiş formunu indirip doldurur ve
> PDF olarak ekler"; ekip üyelerinin özgeçmişleri de "Ekler" bölümüne PDF olarak yüklenir
> (`resmi/BiGG_1_Asama_PRODIS_Kilavuzu.pdf`, bölüm 1.2).
>
> **Resmi form nerede?** Form PRODİS'in içinde, girişten sonra indiriliyor; dışarıda yayımlanmış bir kopyası yok.
> Aşağıdaki taslak, bu tür formların olağan bölümlerine göre hazırlandı. Formu indirince metinleri ilgili
> kutulara taşıyın. Form farklı bir bölüm sorarsa bana gösterin, uyarlarım.
>
> **Köşeli parantezli yerleri siz doldurun.** Kişisel bilgileri ben bilmiyorum, uydurmadım.

## Dürüstlük notu (önce okuyun)

Panel ve hızlandırıcı, özgeçmişteki her teknik iddiayı sorabilir. Eko'nun yazılımı, model eğitimi ve
belgelerinin büyük kısmı **yapay zekâ kodlama asistanlarıyla** (Claude Code) yapıldı. Bunu saklamayın; doğru
anlatılırsa güçlü bir yandır: "Tek kişiyle, yapay zekâ araçlarını yöneterek 4 ayda çalışan bir prototip çıkardım."
Ama şunları kendi cümlelerinizle anlatabilmelisiniz:

- model neden 5,7 M parametrede kaldı (16 MB flash / 8 MB PSRAM sınırı),
- kaliteyi nasıl ölçtünüz (kör ikili kıyas; hakemler yapay zekâydı, insan hakemli test pilotta),
- ses neden Emel / edge-tts değil de VoxCPM2 (ticari lisans),
- kartta hangi parçalar çalışıyor, hangileri henüz denenmedi (gerçek kart denemesi yapılmadı).

Sunumdan önce bu dört soruyu yüksek sesle cevaplamayı deneyin. `06_SUNUM_METNI.md`'deki "sık sorulan sorular"
bölümü de bunun için.

## A. Proje yürütücüsü (siz)

### 1. Kişisel bilgiler

| Alan | Bilgi |
|---|---|
| Ad Soyad | [AD SOYAD] |
| Doğum yılı | [YIL] |
| İl | [İL] |
| Telefon | [TELEFON] |
| E-posta | [E-POSTA] (PRODİS'teki adresle aynı olsun) |
| Web / GitHub / LinkedIn | [BAĞLANTI] (Eko deposu herkese açık değilse yazmayın ya da yalnız demo videosunu verin) |

### 2. Eğitim

| Derece | Üniversite | Bölüm | Başlangıç–bitiş | Not ortalaması |
|---|---|---|---|---|
| [Lisans / Ön lisans / Yüksek lisans] | [ÜNİVERSİTE] | [BÖLÜM] | [YIL–YIL ya da "devam ediyor"] | [GNO] |

Bitirme projesi ya da tez konusu Eko'yla ilgiliyse (gömülü sistemler, yapay zekâ, çocuk gelişimi) bir satırla
ekleyin.

### 3. İş deneyimi

| Kurum | Görev | Tarihler | Kısa açıklama |
|---|---|---|---|
| [KURUM] | [GÖREV] | [AY/YIL–AY/YIL] | [1–2 cümle; yazılım, elektronik, ürün, satış deneyimi öne çıksın] |

> Hatırlatma: Mükemmeliyet Mührü'nden sonra **tam zamanlı** çalışmanız gerekir. Bugün bir işte çalışıyorsanız
> bunu yazın; şirket kuruluşundan önce ayrılacağınızı başvuruda belirtin (`07_EKSIKLER_VE_UYARILAR.md`, madde 4).

### 4. Girişimcilik geçmişi ve ortaklıklar

- Şu an ortağı olduğum şirket: **Yok.** (Şahıs işletmesi dahil; kabul tarihinde de olmamalı.)
- Daha önce aldığım kamu girişimcilik desteği: **Yok** [doğruysa]. (1512/1812 Aşama 2, Teknogirişim
  Sermayesi alanlar başvuramaz.)
- Önceki girişim denemeleri: [VARSA kısa yazın; yoksa "Yok"].

### 5. Proje deneyimi: Eko (Temmuz 2026 – bugün)

**Eko — internetsiz, cihaz içi yapay zekâlı Türkçe hikâye oyuncağı.** Fikir sahibi, ürün ve teknik lider.

- Tek bir ESP32-S3 mikrodenetleyicide (16 MB flash, 8 MB PSRAM) üç yapay zekâ modelini bir arada çalışacak
  şekilde tasarladı:
  - her seferinde yeni hikâye yazan Türkçe dil modeli (5,7 M çekirdek parametre, 4 bit, 10,3 MB),
  - kadın sesiyle okuyan konuşma sentezi modeli (4,3 MB),
  - "Merhaba Eko" uyandırma sözcüğü modeli (≈110 KB).
- 3–6 yaş için 28.493 hikâyelik Türkçe eğitim verisi hazırlattı. Veriyi figür kartları (karakter, yer, kurallar),
  yaşa uygunluk kuralları ve isim süzgeciyle denetledi.
- Kaliteyi kör ikili kıyaslarla ölçtü: son model bir önceki modeli 102–78 ve 99–73 yendi. Hakemler yapay
  zekâydı; insan hakemli test pilotta yapılacak.
- Ses modelini RTX 4090'lı iş istasyonunda eğitti: 25 bin cümlelik veri, ticari kullanıma açık VoxCPM2
  (Apache-2.0) sesinden üretildi. Karttaki C kodu ile PyTorch çıktısının birebir aynı olduğunu doğruladı
  (dalga SNR ≥ 79 dB).
- Kart yazılımını C ile yazdırdı (NFC figür tanıma, ışık halkası, uyku modu, ayar kartı). Bilgisayarda sahte
  donanım başlıklarıyla doğruladı: kart kodu Python referansıyla aynı çıktıyı veriyor.
  **Gerçek kartta deneme henüz yapılmadı.**
- Stand ve figürlerin 3B tasarımlarını hazırladı (`cad/`).
- Yapay zekâ kodlama asistanlarını yöneterek tek kişiyle ≈1.200 kayıtlık (commit) bir geliştirme süreci yürüttü.
- Bu başvurunun iş planını, finansal modelini, etik kurul ve pilot planını hazırladı (`basvuru/tubitak_1812/`).

### 6. Teknik yetkinlikler

Doğru olanları bırakın, olmayanları silin, eksikleri ekleyin:

- Python, PyTorch (model eğitimi ve değerlendirme)
- C / gömülü yazılım (ESP32, Arduino çatısı)
- Küçük dil modelleri, konuşma sentezi, kuantizasyon
- Git, Linux, GPU ile eğitim
- 3B tasarım ve baskı
- Yapay zekâ destekli yazılım geliştirme (kodlama asistanlarıyla)
- [DİĞER]

### 7. Yabancı dil

| Dil | Düzey | Belge (varsa) |
|---|---|---|
| İngilizce | [başlangıç / orta / ileri] | [YDS / IELTS / TOEFL puanı] |

### 8. Ödüller, yarışmalar, sertifikalar

- [VARSA yazın.]

> 1 Ocak 2021'den beri TÜBİTAK'ın düzenlediği ya da paydaşı olduğu bir yarışmada 1., 2. veya 3. olmak
> (mansiyon ve katılım belgesi sayılmaz) iş planına **+5 puan** getirir; belge en geç Aşama 2 değerlendirmesinin
> son gününe kadar verilir (2026-2 çağrı duyurusu). Takvim uyarsa değerlendirin: TÜBİTAK 2242 (öğrenciyseniz)
> ya da TÜBİTAK'ın paydaşı olduğu TEKNOFEST yarışmaları. Hangi yarışmanın sayıldığını başvurmadan önce
> bigg@tubitak.gov.tr'ye sorun.

### 9. Yayın, patent, açık kaynak

- [VARSA yazın.] Eko için patent başvurusu yok; ayırt edici teknik yöntem fikri mülkiyet bölümünde anlatıldı
  (`02_IS_PLANI_AGY112.md`).

### 10. Referanslar

- [AD SOYAD, unvan, kurum, telefon / e-posta] — iki kişi yeterli (hoca, eski yönetici).

## B. Ekip üyeleri ve danışmanlar

Her ekip üyesi ve danışman için aynı formu doldurun. AGY 112 §3.1'de iki tamamlayıcı ekip rolü önerildi:

### B1. Kurucu ortak / donanım ve üretim sorumlusu (aranıyor)

Aranan özgeçmiş: elektrik-elektronik ya da mekatronik mühendisi; PCB tasarımı, EMC/RED (CE) uyumu, seri üretim
(EMS, kalıp) deneyimi. Bulunursa:

- Ad Soyad, eğitim, deneyim: [DOLDUR]
- Eko'daki görevi: kart tasarımı (prototipten seri üretime), pil ve güç yönetimi, CE testleri, üretici seçimi.
- Hisse / emek karşılığı: [KARARLAŞTIRIN; ortaklık sözleşmesi şirket kuruluşunda yapılır].

### B2. Danışman: çocuk gelişimi / okul öncesi eğitim uzmanı (aranıyor)

- Ad Soyad, unvan, kurum: [DOLDUR]
- Görevi: hikâye kurallarının yaşa uygunluğu, pilot çalışmanın (etik kurul) yürütülmesi, öğretmen formu.
- Yazılı danışmanlık taahhüdü alın (bir sayfalık niyet mektubu yeterli). Etik kurul başvurusunda sorumlu
  araştırmacı genellikle bir öğretim üyesi olmalıdır (`05_ETIK_KURUL_VE_PILOT.md`).

## Yükleme notları

- Her özgeçmiş ayrı PDF (ör. `Ozgecmis_AD_SOYAD.pdf`); 2 sayfayı geçmesin.
- Word kopyası: `cikti/10_Ozgecmis_Taslagi.docx`. Resmi formu indirince metinleri oraya taşıyın.
