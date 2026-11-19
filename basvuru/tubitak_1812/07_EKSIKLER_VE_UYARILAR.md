# Eksik bilgiler ve kritik uyarılar

> Bu listedeki **kırmızı (🔴)** maddeler başvuruyu doğrudan engelleyebilir. Hızlandırma programına başvurmadan önce
> hepsini kontrol edin.

## 🔴 Uygunluk: bunlar sağlanmazsa başvuru yapılamaz

1. **Üniversite öğrencisi ya da mezunu olmak.** Girişimci, hızlandırma programına başvurduğu tarihte bir
   üniversitenin ön lisans, lisans, yüksek lisans ya da doktora programına kayıtlı öğrenci ya da mezun olmalı.
   PRODİS bilgiyi YÖK'ten çeker. Yurt dışı diploma için YÖK denklik belgesi gerekir.
   - Siz bu koşulu sağlamıyorsanız: ekipte koşulu sağlayan bir kişi **proje yürütücüsü (girişimci)** olur.
     Yürütücü sonradan değiştirilemez ve şirkette tam zamanlı çalışmak zorundadır.
2. **Hiçbir şirkette ortak olmamak.** Hızlandırma programına **kabul edildiğiniz tarihte** hiçbir sermaye
   şirketinde (Ltd., A.Ş.) ve **şahıs işletmesinde** (serbest meslek, e-ticaret şahıs şirketi dahil) ortak ya da
   sahip olmamalısınız. Borsada işlem gören hisseler ve kitle fonlamasıyla alınan paylar sayılmaz.
   - **Eko için şimdiden şirket kurmayın.** Şirket, Mükemmeliyet Mührü'nden sonra TÜBİTAK'ın istediği biçimde
     (anonim şirket) kurulur.
   - Varsa şahıs işletmenizi programa kabulden önce kapatın.
3. **Daha önce destek almamış olmak.** Sanayi ve Teknoloji Bakanlığı Teknogirişim Sermayesi Desteği ya da
   TÜBİTAK 1512/1812 Aşama 2 desteği almış kişiler başvuramaz.
4. **Tam zamanlı çalışma ve rekabet yasağı.** Yatırımdan sonra proje yürütücüsü ve yönetici ortaklar:
   - yalnız şirket için çalışır; başka işte çalışamaz, danışmanlık veremez;
   - pay sahipliği bittikten sonra 2 yıl rakip bir işte çalışamaz.

   Bugün bir işte çalışıyorsanız, şirket kuruluşundan önce ayrılmanız gerekir. Tek istisna, üniversitede öğretim
   elemanı olarak çalışmaktır.
5. **Fikri mülkiyetin şirkete devri.** Kod, modeller, veri ve tasarımlar yatırım öncesinde bedelsiz olarak
   şirkete devredilir. Depodaki her şeyin sizin ya da açık kaynak lisansla kullanılabilir olduğundan emin olun
   (aşağıdaki 🟠 maddelere bakın).

## 🟠 Fikri mülkiyet: başvurudan önce düzeltilmesi önerilenler

1. **Keloğlan'ın yan karakterleri.** `data/urun_figurleri.json`'da Keloğlan'ın yanındakiler arasında
   **Bilgecan Dede**, **Balkız** ve **Karakaçan** var. Pazar araştırmamız (`docs/PAZAR_ARASTIRMASI.md`
   §3.1) Bilgecan Dede'nin TRT'nin *Keloğlan Masalları* çizgi filmine ait bir karakter olduğunu belirtiyor.
   Diğer ikisi de aynı diziden olabilir.
   - Öneri: bu adları masal geleneğindeki anonim figürlerle değiştirin (anası, padişah, dev, eşeği) ve Keloğlan
     verisini/modelini güncelleyin. Hızlıca yapabilirim.
2. **Eğitim verisinde lisanslı karakterler.** Modeller, üründen çıkarılan lisanslı karakterlerin (Niloya, Elsa
   vb.) hikâyeleriyle de eğitildi. Bu adlar isim süzgeciyle engelleniyor ve ürün bu karakterlerle hikâye
   anlatmıyor. Yine de yatırım öncesi incelemede soru gelebilir.
   - Avukata sorun.
   - Gerekirse model yalnız lisanssız veriyle yeniden eğitilebilir. Bulutta ≈6 saat sürer; kör kıyasla kalite
     kaybı ölçülür.
3. **Yapay zekâ ile üretilen eğitim verisi.** Hikâyelerin büyük kısmı yapay zekâ ajanlarıyla yazıldı. Kullanılan
   hizmetin koşulları çıktının ticari kullanımına izin veriyor. Bunu doğrulayıp iş planı ekindeki "üçüncü taraf
   lisans envanteri"ne yazın.
4. **Açık kaynak lisansları.** Envanteri iş planı ekinde verin:
   - cihaz içi çıkarım motorunun temeli: MIT lisanslı proje (lisans metni ve atıf korunmalı);
   - TinyStories Türkçe: CDLA-Sharing-1.0;
   - VoxCPM2: Apache-2.0;
   - Supertonic: Open RAIL-M. Ambalajda "ses yapay zekâ ile üretilmiştir" ibaresi zorunlu.
5. **Marka araştırması.**
   - "Eko" çok yaygın bir sözcük; tescil zor olabilir. TÜRKPATENT'te 9, 16, 28 ve 41. sınıflarda arayın.
     Gerekirse "Eko Masal", "Merhaba Eko" gibi birleşik bir ad kullanın.
   - Özgün karakter adlarını da arayın: Zıpzıp, Tontiş, Bip, Fıstık, Bulut.
   - Siz projeye "Eco AI" diyorsunuz; başvuruda tek bir yazım seçin (Türkçe ürün için "Eko" önerilir).

## 🟡 Başvuruyu güçlendirecekler

1. **Gerçek kartta çalışan bir demo videosu.** Bugün yazılım PC'de doğrulandı, ama kartta henüz denenmedi.
   Değerlendirme komisyonu için en güçlü kanıt, figür konunca Eko'nun hikâye anlattığı 1 dakikalık bir videodur.
   Başvurudan önce çekin.
2. **Ekip.** Tek kişilik başvurular "ekip yetkinliği" ölçütünde zayıf kalabilir (eşik 7/10).
   - Donanım/üretim bilen bir kurucu ortak bulun ya da en az bir danışmandan yazılı taahhüt alın.
   - Bir çocuk gelişimi uzmanından da danışmanlık taahhüdü alın.
3. **Talep kanıtı.** Basit bir ön kayıt sayfası, 20–30 ebeveyn görüşmesi, 1–2 anaokulundan niyet mektubu.
4. **Ek puan fırsatları (Aşama 2).**
   - TÜBİTAK'ın düzenlediği ya da paydaşı olduğu bir yarışmada 1.–3.lük **+5 puan** getirir. Örnek: TÜBİTAK'ın
     paydaşı olduğu TEKNOFEST yarışmaları; uygunluğunu doğrulayın.
   - ARDEB proje yürütücülüğü +3 puan getirir.
5. **Etik kurul.** Ebeveyn anketi ve çocuklu ailelerle pilot için etik kurul onayının Aşama 2 başvurusundan önce
   alınması ya da ayrıntılı planlanması isteniyor (bkz. `05_ETIK_KURUL_VE_PILOT.md`).

## Sizin dolduracağınız bilgiler (yer tutucular)

| Yer tutucu | Nerede | Not |
|---|---|---|
| [AD SOYAD], T.C. kimlik no, adres, telefon, e-posta | PRODİS kaydı, iş fikri dokümanı, AGY 112 §3.1–3.3, maliyet formu M011 | PRODİS'e e-Devlet ile girilir |
| [ÜNİVERSİTE, BÖLÜM, ÖĞRENCİ/MEZUN] | İş fikri dokümanı §4, AGY 112 §3.1 | Uygunluk koşulu 1 |
| Deneyim, projeler, yarışmalar | AGY 112 §3.1 | Kısa ve somut |
| Kurucu ortak (varsa) ve pay oranları | AGY 112 §3.2 (Seçenek A ya da B) | Kurucu ortak da uygunluk koşullarını sağlamalı |
| Danışman adları ve unvanları | AGY 112 §3.1, §3.3, §3.4 | Niyet mektubu ekleyin |
| İşbirliği yapılacak kurumlar | AGY 112 §3.4 | Anaokulları, üniversite (etik kurul), EMS |
| Hızlandırma programı adı | AGY 112 §3.4 | Kabul edildiğiniz program |
| Logo | AGY 112 §2.6 | Varsa ekleyin |
| [DOĞRULA] işaretli cümleler | AGY 112 §2.6, §3.2 | Üniversitede patent hakkınız yok; daha önce destek almadınız |

## Rakamlar hakkında

- Bütün pazar ve satış rakamları **varsayımdır**. Kaynaklar `docs/PAZAR_ARASTIRMASI.md`'de ve iş planında
  belirtildi.
- Hızlandırma programında ön kayıt, anket ve pilotla güncellenmeleri bekleniyor.
- Finans modelini değiştirmek için `hazirla/finans.py`'deki sayıları düzenleyip `hazirla/doldur.py`'yi yeniden
  çalıştırın; bütün belgeler birlikte güncellenir.
