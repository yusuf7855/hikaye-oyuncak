# Ön kayıt sayfası ve talep testi

> Panelist incelemesinin en büyük eleştirisi: "Bütün doğrulamalar gelecek zamanda." Hem hızlandırma programına
> kabul (ölçüt 4: ön hazırlık) hem Aşama 2 paneli (ticarileşme potansiyeli) için **gerçek talep kanıtı** gerekiyor.
> Bu belge, şimdiden başlatılabilecek en ucuz testi anlatıyor:
>
> - basit bir ön kayıt sayfası (`on_kayit/index.html`),
> - bir Google Formu,
> - ebeveyn topluluklarında paylaşım.

## Ölçülecekler ve hedefler

| Gösterge | Hedef | Ne işe yarar |
|---|---|---|
| Ön kayıt sayısı | 300 (hızlandırma başvurusuna kadar), 1.000 (Aşama 2'ye kadar) | Pazar ilgisi; iş fikri dokümanı §5 ve AGY 112 §1.4, §2.1 |
| "Bu fiyata alırım" oranı (2.499 / 2.999 TL KDV dahil, A/B) | ≥ %20 | Fiyat doğrulaması; AGY 112 §2.3 (plan fiyatı 2.999 TL; 2.499 TL düşük fiyat seçeneği) |
| Kaparo bırakan oranı (ileride, iadeli 100 TL) | ≥ %5 | Gerçek ödeme niyeti |
| Görüşmeye/pilota gönüllü | ≥ 50 aile | Pilot ve etik kurul başvurusu için havuz |
| Anaokulu niyet mektubu | ≥ 3 | İşbirlikleri (AGY 112 §3.4) |
| Kayıt başına maliyet (reklam kullanılırsa) | ≤ 40 TL | CAC varsayımı (≤450 TL) |

## Nasıl yapılır? (1–2 günlük iş)

1. **Google Formu** oluşturun (soruları aşağıda). Formu kopyalayıp ikinci bir form yapın: iki form aynı, yalnız
   6. sorudaki fiyat farklı (A: 2.499 TL, B: 2.999 TL). İki formun "yanıtları topla" bağlantısını alın.
2. **Ön kayıt sayfası:** `on_kayit/index.html` hazır.
   - Dosyanın sonundaki `FORM_A` ve `FORM_B` değerlerine iki formun bağlantısını yazın.
   - Örnek sesler hazır: `ornek1.mp3` (Bulut bahçede, 32 sn) ve `ornek2.mp3` (Keloğlan şatoda, 40 sn). Bunları
     ürün modeli c3ft_urun13 yazdı (5 aday + seçici, kartla aynı) ve kartın sesi okudu (kartta olduğu gibi
     4/8 bit kuantize). Metinler `ornek1.txt`, `ornek2.txt`; hiç düzeltilmedi. 11 hikâyeden en düzgün ikisi
     seçildi; sayfada bu söylenmez ama "deneme sürümü" ve "bazen tuhaf cümle çıkabilir" uyarıları vardır.
   - Demo videosu çekilince bağlantısını `VIDEO` değişkenine yazın (boşken video satırı görünmez).
   - Sayfayı ücretsiz yayınlayın: GitHub Pages ya da Netlify. Hangisini isterseniz kurulumu yaparım.
3. **A/B fiyat testi.** Sayfa her ziyaretçiye rastgele bir fiyat gösterir (2.499 ya da 2.999 TL) ve düğmeler o
   fiyatın formuna gider; aynı tarayıcı hep aynı fiyatı görür. Belirli bir fiyatı göstermek için bağlantının
   sonuna `?fiyat=2499` ya da `?fiyat=2999` ekleyin (ör. reklamda iki ayrı bağlantı). Hangi fiyatın daha çok
   kayıt getirdiğini iki formun yanıt sayısından okursunuz.
4. **Paylaşım.**
   - Anne-baba WhatsApp ve Facebook grupları.
   - Okul öncesi öğretmeni ve çocuk gelişimci Instagram hesapları (ücretsiz deneme cihazı karşılığı).
   - Kendi çevreniz.
   - Bütçe varsa Instagram reklamı: 3 mesajla A/B testi (gizlilik / ekransız / her gece yeni masal).
5. **Haftalık kayıt.** Sayıları her hafta bir tabloya yazın (tarih, kayıt, fiyat seçenekleri, kanal). Bu tablo,
   başvuruda "yaptığımız doğrulama" bölümünün kanıtıdır.

## Google Formu soruları

1. E-posta adresiniz (zorunlu; ürün çıkınca haber vermek için)
2. Kaç yaşında çocuğunuz var? (0–2 / 3–4 / 5–6 / 7+; çoklu seçim)
3. Hangi şehirde yaşıyorsunuz?
4. Çocuğunuz şu an hikâye/masalı en çok nereden dinliyor? (siz okuyorsunuz / tablet-telefon / sesli kitap
   uygulaması / sesli oyuncak / diğer)
5. Sizin için en önemli üç özellik? (internete bağlanmaması / her seferinde yeni hikâye / Türkçe ve yerel
   karakterler / ekransız olması / abonelik olmaması / uyku modu / fiyat)
6. Eko'yu **[2.499 / 2.999] TL**'ye satın almayı düşünür müsünüz? (kesinlikle / muhtemelen / emin değilim /
   muhtemelen hayır / kesinlikle hayır)
7. Size göre bu ürün için uygun fiyat nedir? (serbest)
8. Hangi karakterleri istersiniz? (Keloğlan / Nasreddin Hoca / Pinokyo / Pamuk Prenses / Alaaddin / hayvan
   karakterler / robot-uzay / diğer)
9. 4 haftalık ücretsiz denemeye (pilot) katılmak ister misiniz? (evet / hayır)
10. Çocuğunuzun gittiği anaokulu bu ürünü denemek ister mi, bize bağlantı verebilir misiniz? (isteğe bağlı)
11. (Fiyat seçeneği, formun kendisinden anlaşılır: A formu = 2.499, B formu = 2.999.)
12. Onay: "Aydınlatma metnini okudum; e-posta adresimin ürün duyurusu için saklanmasını kabul ediyorum."
    (zorunlu)

## KVKK aydınlatma metni (kısa, forma eklenecek)

> **Kişisel verilerin işlenmesi hakkında:** Bu formda verdiğiniz e-posta adresi ve yanıtlar, [AD SOYAD] ([İL])
> tarafından yalnız Eko ürününün geliştirilmesi, ürün çıktığında size haber verilmesi ve isteğiniz halinde pilot
> çalışmaya davet edilmeniz amacıyla, 6698 sayılı KVKK md. 5/1 (açık rıza) kapsamında işlenir.
>
> - Verileriniz yurt içinde ve yurt dışında bulunan form hizmeti (Google) sunucularında saklanır; üçüncü
>   kişilerle paylaşılmaz.
> - En geç ürün satışa çıktıktan 6 ay sonra silinir.
> - KVKK md. 11'deki haklarınızı (bilgi talebi, düzeltme, silme vb.) [E-POSTA] adresine yazarak
>   kullanabilirsiniz.
> - Çocuğunuza ait hiçbir kişisel veri istenmez.

Not: Google Formları verileri yurt dışında saklayabilir. Bu yüzden açık rıza alın; bunun yerine yurt içi bir form
hizmeti de kullanılabilir. Bu metin hukuki görüş değildir.
