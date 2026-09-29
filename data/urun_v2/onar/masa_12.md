# Editör görevi (onarım): Maşa, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
@plan: <sorun> | <çözüm>
@tohum: <aynı tohum kimliği>
@degisim: <eski> -> <yeni>      (yalnız özgün blokta varsa ve tutuyorsan)
@onarim: <özgün bloğun sha1'i; her hikâyede verilir>
<gövde>
```

- **Yalnız bulguların gösterdiği yeri düzelt** ve tutarlılık için değişmesi gerekeni (ör. çözüm değiştiyse plan
  satırı, silinen nesnenin sonraki anılışı). Öteki cümleler olduğu gibi kalır.
- **Tohumu ve hikâyeyi koru:** figür, yer, yan, tema, açılış, kapanış türü, diyalog, özellik ve tohum kelimeleri
  (isim, fiil, sıfat) aynı kalır; sorun ve çözüm aynı kalır. Tohum kelimelerinden en çok biri değişebilir ve
  `@degisim` satırına yazılır (özgün bloktaki değişim sayılır).
- Gövde 70-100 kelime, her cümle en çok 12 kelime, tek paragraf.
- Bir bulgu sana yanlış görünse bile o cümleyi daha basit ve açık biçimde yeniden söyle: hakem orada takıldı,
  okuyan çocuk da takılabilir. İşaretlenen kelimeyi ya da yapıyı tekrarlama.
- Görevi **YENİDEN YAZ** olan hikâyede (M3: çekirdek önemsiz ya da saçma) hikâyeyi aynı tohumdan baştan yaz:
  çocuğun önemseyeceği, sebebi ilk 3 cümlede söylenen bir sorun ve figürün 1-2 adımlık çözümü; başlık, tohum
  kimliği ve `@onarim` satırı yine verilir.
- Onarılmış metin özgünden farklı olmalıdır (aynı metin aynı kayıttır ve reddedilir).
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar12.txt --ad urun_v2`
  İşaretlenen hikâyede EN ÇOK 1 yerel düzeltme yap ve kontrolü bir kez daha koş. Yine geçmeyen hikâyenin bütün
  bloğunu (başlık dahil) dosyadan sil; zorlama. Geçen hikâyeye dokunma (her değişiklik bir yama sayılır).

## Yazım kılavuzu

# Ürün hikayesi yazım kılavuzu

Bu hikayeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini eğitecek. Her hikaye bir tohumdan yazılır.
Yanında figürün kaynaklı kartı (data/urun_kartlari.json) ve sade sözlük (data/sade_sozluk_sik.txt) vardır.
Kart kapalı dünyadır: kartta yazmayan hiçbir şey hikayeye girmez.

1. **Uzunluk.** Gövde 70-100 kelime. Her cümle en çok 12 kelime, çoğu 5-9 kelime. Tek paragraf.
2. **Tek sahne, tek zaman.** Hikaye tohumdaki yerde başlar ve biter. 'ertesi', '... gün/hafta sonra',
   'akşama/sabaha kadar', 'bütün gün', 'o gece', 'günlerce', 'her sabah' gibi zaman atlamaları yok.
   Bekleme sahnenin içinde olur.
3. **Tek sorun, açık hedef.** Figürün açık ve küçük bir hedefi vardır (uçurtmayı yükseltmek, sesin nereden
   geldiğini bulmak) ve hikaye bu hedefe ulaşınca tatmin edici biçimde biter; 'hiçbir şey olmayan' hikaye yok.
   Hedef çocuğun önemseyeceği bir şeydir (bir arkadaşı sevindirmek, kaybolan oyuncağı bulmak, bozulan oyunu
   kurtarmak); rüzgarın yaprakları dağıtması gibi önemsiz ya da 'kurdele hamurun içine düştü' gibi saçma olay yok.
   Sorun ilk 3 cümlede sebebiyle birlikte söylenir ('Top çalıya takıldı.'). Sorun çoğunlukla dışarıdan gelir
   (hava, takılan top, merak uyandıran bir ses); figürün kendi hatası yalnız özür temasında sorundur. Sorunu figür
   kendisi 1-2 adımda çözer; yardım istemek de figürün çözümüdür. Yan karakter en fazla yardım eder.
4. **Figür görünür ve etkin.** Figürün adı ilk 2 cümlede ve sonda geçer. Hikaye onun gözünden anlatılır.
5. **Yan karakter ve kapalı dünya.** Yalnız başlıktaki Yan alanında yazan karakterler bulunur; kartta yazan kısa
   adla ve karttaki ilişkiyle (Niloya'nın ağabeyi Murat'tır; Mete, Murat'ın arkadaşıdır). Başka ad, canlı, rol ya
   da aile üyesi yok; bebek, robot, dev, biri gibi kelimeler karakter olamaz, yalnız cansız anlamda geçer ('oyuncak
   robot', 'bir sürü yaprak'). Arka plandaki çoğul canlılar ('kuşlar') konuşmaz ve olaya katılmaz. Kartta 'konuşmaz'
   yazan karakter konuşmaz. Kartta olmayan ev, eşya ya da yetenek uydurulmaz. Yer, kartın o yer için verdiği
   tarife uyar.
6. **Figür özelliği.** Yalnız tohumdaki özellik kullanılır: bir kez, olayda işe yarar biçimde ve kartın 'güvenli
   özellik kullanımı' satırına uygun. Özellikler sıralanmaz, betimlenmez. Slogan ve kalıp replik yok.
7. **Sade kelime.** Kelimeler sade_sozluk_sik.txt'den seçilir; en çok 2 liste dışı kelime. Deyim, mecaz, soyut
   kavram ve şapkalı harf yok ('keşfetmek' değil 'bulmak'; 'top gibi' benzetmesi serbest); 'hâlâ' yerine 'yine'
   ya da 'daha' yazılır. Tohumdaki isim, fiil ve sıfat geçer;
   biri listeden başka bir kelimeyle değiştirilebilir ve değişiklik kayda yazılır.
8. **Dil.** Anlatım -dı'lı geçmiş zamanda ('yürüdü', 'bakıyordu', 'takılmıştı'). Her replikte konuşan bellidir
   ('dedi Niloya'); hitaptan önce virgül konur ('Sıra sende, Niloya'). Kimse kendi kendine konuşmaz ya da kendine adıyla seslenmez. Plan satırları da aynı dil ve
   yazım kurallarına uyar; cihazda model planı kendisi yazıyor.
9. **Son.** Son 1-2 cümle hikayeyi kapatır: sorunun çözüldüğü görünür ve son cümle sıcak, doyurucu bir kapanış
   verir ('İkisi oyunlarına mutlu mutlu devam etti.'). Hikaye hiçbir zaman çıplak bir eylemle ya da durgun bir
   resimle bitmez; okur 'sonra ne oldu?' diye sormaz. Son, tohumdaki kapanış türüyle yazılır: duygu, sonuç, replik ya
   da ders; 'çünkü' ile açıklama yalnız 'duygu' türünde kullanılır. Son güvenlidir. Korku, yaralanma, hastalık ve
   taklit edilince tehlikeli davranış (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç) yok.
10. **Biçim ve öz-denetim.** Her hikaye dört parçadır:
    `### Figür | yer | yan` / `@plan: sorun | çözüm` / `@tohum: id` / gövde.
    Başlık tohumdaki figür, yer ve yan alanlarının birebir kopyasıdır. Planda sorun ve çözüm her biri 3-9 küçük
    harfli kelimedir, özel ad yoktur. Yazdıktan sonra her hikaye HAKEM_M.md, HAKEM_D.md ve HAKEM_K.md madde
    listelerine karşı cümle cümle okunur (çelişki, sebepsiz nesne, ikinci sorun, özne-fiil uyumu, tekrar, kart
    dışı eşya, taklit edilince tehlikeli davranış) ve kusur bulunursa kontrolden önce düzeltilir. Sonra
    `veri_hakem.py kontrol` koşulur. İşaretli hikayede en çok
    1 yerel düzeltme yapılır; yine geçmezse hikaye boş bırakılır, zorlanmaz.

**Kural bütçesi.** Bu kılavuz tek sayfa ve 10 maddedir. Yeni bir kusur türü kılavuza değil koda ya da hakem
listesine eklenir. Kılavuza yeni madde ancak bir madde çıkarılarak girer. Kötü örnek konmaz.

**Tohum alanları (tanım, kural değil).** Açılış türü: figür adı / zaman ('Bir sabah') / yer / ses-hava;
'<Ad> adında ... yaşardı' bir açılış türü değildir. Kapanış türü: *duygu* (figürün ya da karakterlerin yaşanan
olaya bağlı hissi; 'çünkü' kullanılabilir: 'Tosbi çok sevindi, çünkü sesin nereden geldiğini bulmuştu.'),
*sonuç* (ardından mutlulukla ne yaptıkları ya da olayın sonucu: 'oyunlarına mutlu mutlu devam ettiler'),
*replik* (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle gelmez), *ders* (olaya
bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir: 'Niloya bundan sonra zorda kalınca büyüklerinden yardım
istedi.'). Diyalog 'yok' ise hikayede replik yoktur. Temalar tek sahneye uyarlanmıştır: merak edip bulmak (bir
ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar); eğlenceli ya da komik bir oyun ve oyunda küçük bir
aksilik; figür başkasına yardım eder (hasta ya da yaralı hayvan değil); aynı sahnede küçük bir kutlama ya da
sürpriz hazırlamak; doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef; hayali
oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef; kaybolan eşya; yeni bir şeyi denemek; bir şey
yapmak; yağmur ya da kar günü; sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil);
yeni arkadaş (ilk adımı figür atar); ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek;
yalnız yağmurun dinmesi değil); paylaşmak; yardım istemek (çözüm figürün yardım istemesidir); özür dilemek (figürün
kendi hatası yalnız bu temada olur); sırayla oynamak.

**İyi örnekler** (kullanıcı yetkisiyle seçildi; farklı figür ve farklı kapanış türü; ikisi de `veri_hakem.py kontrol`dan
geçer):

Tohum: deniz, yan balık, özellik sabır, kelimeler taş/toplamak/renkli, tema merak edip bulmak, açılış yer,
kapanış duygu.

```
### Tosbi | deniz | balık
@plan: sığ sudan bilinmeyen bir ses geldi | sabırla bekledi ve sesi yapan balığı gördü
@tohum: tosbi-9001
Deniz kıyısında serin bir sabahtı. Tosbi kumda renkli taşlar topluyordu. Birden sığ sudan garip bir ses geldi. Tosbi bu sesi çok merak etti. Suyun kenarına yavaşça yürüdü ve baktı. Ama suda hiçbir şey göremedi. Tosbi acele etmedi ve sabırla bekledi. Sonunda küçük bir balık sudan zıpladı ve suya geri düştü. "Bu sesi sen mi yapıyorsun?" diye sordu Tosbi. "Evet, bu benim zıplama oyunum," dedi balık. Balık üç kez daha zıpladı ve Tosbi hepsini saydı. Tosbi çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

Tohum: park, yan Murat, özellik soru, kelimeler uçurtma/bağlamak/uzun, tema yardım istemek, açılış figür adı,
kapanış replik.

```
### Niloya | park | Murat
@plan: uçurtma ağaçların üstüne çıkamadı çünkü ipi kısaydı | ağabeyinden ip isteyip iki ipi bağladı
@tohum: niloya-9001
Niloya ile Murat parkta sarı bir uçurtma uçuruyordu. Ama uçurtma ağaçların üstüne çıkamadı çünkü ipi çok kısaydı. Niloya ipe baktı ve biraz düşündü. "Murat, çantada başka ip var mı?" diye sordu Niloya. Murat çantasına baktı ve uzun bir ip buldu. İpi hemen Niloya'ya verdi. Niloya iki ipi sıkıca birbirine bağladı. Sonra ipi yavaş yavaş bıraktı. Rüzgar esti ve uçurtma yükseldi. Sarı uçurtma ağaçların üstüne çıktı. Murat sevinçle ellerini çırptı. Niloya ipi iki eliyle tuttu ve güldü. "Teşekkürler, Murat, uçurtmamız artık en yüksekte!" dedi Niloya.
```

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0035
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'şeker', fiil 'çıkmak', sıfat 'büyük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: elma içi boş büyük bir kütüğe düştü | uzun bir dalla elmayı itip kütükten çıkardı
@tohum: masa-0035
@degisim: şeker -> elma
Rüzgar ağaçların arasında hafif hafif esiyordu. Maşa ile Koca Ayı patikada üzgün bir kirpi gördü. Kirpi elmasını içi boş büyük bir kütüğe düşürmüştü. Kirpi kısa bacaklarıyla elmaya ulaşamıyordu. "Üzülme, kirpi, ben sana yardım ederim!" dedi Maşa. Maşa önce kolunu kütüğe uzattı. Ama elma çok içerideydi. Koca Ayı yerden uzun bir dal aldı ve Maşa'ya verdi. Maşa dalla elmayı yavaşça itmeyi denedi. Kırmızı elma kütüğün öbür ucundan dışarı çıktı. Kirpi elmaya koştu ve burnuyla ona dokundu. Koca Ayı gülümseyip başını salladı. "Al bakalım, kirpi, şimdi afiyetle yiyebilirsin!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Koca Ayı yerden uzun bir dal aldı"
   - Cümle 8: «Koca Ayı yerden uzun bir dal aldı ve Maşa'ya verdi.»
   - Açıklama: Çözümün asıl aracını yan karakter bulup veriyor, Maşa yalnız uyguluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0035` birebir aynı, `@degisim: şeker -> elma` (tutuyorsan), ardından `@onarim: c8d8cf9f70bd48a017aaa89ba9a6f55f8570d791`, sonra gövde.

### Hikâye 2: tohum masa-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0037
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'fıskiye', fiil 'güvenmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: top ağaca çarpıp iki taşın arasına düştü | dalın ucuna reçel sürdü ve topu çıkardı
@tohum: masa-0037
@degisim: fıskiye -> top
Maşa ormanda piknik yapıyor ve küçük sarı topuyla oynuyordu. Topu havaya atıyor ve yakalıyordu. Ama top bir ağaca çarptı ve iki taşın arasına düştü. Taşların arası çok dardı ve Maşa topa yetişemedi. Maşa piknik sepetindeki tatlı reçele baktı. Sarı top çok hafifti ve Maşa buna güvendi. Uzun bir dalın ucuna biraz reçel sürdü. Dalı taşların arasına uzattı ve top reçele yapıştı. Maşa dalı yavaşça çekti ve top dışarı çıktı. Top yapış yapış olmuştu. Maşa güldü ve onu otlara silip temizledi. Maşa bundan sonra topuyla ağaçlardan uzakta, açık bir yerde oynadı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa buna güvendi"
   - Cümle 6: «Sarı top çok hafifti ve Maşa buna güvendi.»
   - Açıklama: 'Güvenmek' fiili burada topun hafifliğine uygun anlamda kullanılmamış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa buna güvendi"
   - Cümle 6: «Sarı top çok hafifti ve Maşa buna güvendi.»
   - Açıklama: 'Buna güvendi' soyut bir anlatım; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Bir duruma güvenmek soyut bir anlatım, küçük çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Uzun bir dalın ucuna biraz reçel sürdü"
   - Cümle 7: «Uzun bir dalın ucuna biraz reçel sürdü.»
   - Açıklama: Karttaki özellik reçeli çok sevmek; reçel burada yalnız yapıştırıcı olarak kullanılıyor, sevgi gösterilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0037` birebir aynı, `@degisim: fıskiye -> top` (tutuyorsan), ardından `@onarim: 3733c8d8d813be72436dfcfd9023c17bfbda5a68`, sonra gövde.

### Hikâye 3: tohum masa-0038 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0038
- yer: dağ (Ormanın yanındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bilezik', fiil 'dağılmak', sıfat 'değişik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: elmalar tepeden aşağı yuvarlandı ve dağıldı | reçelli bir ekmek yapıp kirpiye verdi
@tohum: masa-0038
@degisim: bilezik -> sepet
Tepede güneş parlıyordu. Maşa, Koca Ayı ve kirpi çimenlerde elmalarla piknik yapıyordu. Ama elmalar tepeden aşağı yuvarlandı ve ormana doğru dağıldı. Kirpi elmaları çok severdi ve üzgün üzgün başını eğdi. "Üzülme, kirpi, sana güzel bir şey vereceğim!" dedi Maşa. Maşa hemen piknik sepetini açtı. Sepette Maşa'nın en sevdiği değişik bir reçel vardı: elma reçeli. Maşa bir ekmeğe bu reçelden bol bol sürdü. Koca Ayı ekmeği alıp kirpiye verdi. Kirpi ekmeği kokladı ve mutlu mutlu yemeye başladı. Koca Ayı da gülümsedi. Maşa çok sevindi, çünkü küçük kirpi yine mutluydu.
```

**Hakem bulguları (8):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "reçelli bir ekmek yapıp kirpiye verdi"
   - Cümle 0 (plan satırı): «elmalar tepeden aşağı yuvarlandı ve dağıldı | reçelli bir ekmek yapıp kirpiye verdi»
   - Açıklama: Planda Maşa ekmeği veriyor ama gövdede Koca Ayı veriyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama elmalar tepeden aşağı yuvarlandı"
   - Cümle 3: «Ama elmalar tepeden aşağı yuvarlandı ve ormana doğru dağıldı.»
   - Açıklama: Elmaların neden yuvarlandığı söylenmiyor.
   - Açıklama: Elmaların neden yuvarlandığı hiç söylenmiyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kirpi elmaları çok severdi ve üzgün"
   - Cümle 4: «Kirpi elmaları çok severdi ve üzgün üzgün başını eğdi.»
   - Açıklama: Sorun elmaların dağılmasından kirpinin üzgünlüğüne kayıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en sevdiği değişik bir reçel"
   - Cümle 7: «Sepette Maşa'nın en sevdiği değişik bir reçel vardı: elma reçeli.»
   - Açıklama: 'Değişik' kelimesi burada anlamsız ve yanlış kullanılmış.
   - Açıklama: 'Değişik' kelimesi burada anlamsız ve 'en sevdiği' ile çelişiyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa bir ekmeğe bu reçelden"
   - Cümle 8: «Maşa bir ekmeğe bu reçelden bol bol sürdü.»
   - Açıklama: Reçelli ekmek elmaların yuvarlanması sorununa yönelmiyor; elmalar hiç toplanmıyor.
   - Açıklama: Çözüm dağılan elmalara yönelmiyor, elmalar hiç toplanmıyor.
6. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "Koca Ayı ekmeği alıp kirpiye verdi"
   - Cümle 9: «Koca Ayı ekmeği alıp kirpiye verdi.»
   - Açıklama: Plan ekmeği Maşa'nın verdiğini söylüyor ama gövdede Koca Ayı veriyor.
7. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Koca Ayı ekmeği alıp kirpiye verdi"
   - Cümle 9: «Koca Ayı ekmeği alıp kirpiye verdi.»
   - Açıklama: Ekmeği kirpiye figür değil Koca Ayı veriyor.
8. **C5** (K merceği) — Son güvenli ve sorun çözülmüş ('sıcaklık' aranmaz).
   - Alıntı: "çünkü küçük kirpi yine mutluydu"
   - Cümle 12: «Maşa çok sevindi, çünkü küçük kirpi yine mutluydu.»
   - Açıklama: Plandaki sorun olan tepeden yuvarlanıp dağılan elmalar hiç toplanmıyor, sorun çözülmeden son veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0038` birebir aynı, `@degisim: bilezik -> sepet` (tutuyorsan), ardından `@onarim: 25947348b6eee58bed10a1169812822fdd0ce9dd`, sonra gövde.

### Hikâye 4: tohum masa-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0039
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'koni', fiil 'yıkamak', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çamur oyunu yüzünden elleri çamur içindeydi | yağmur suyunu kovada toplayıp ellerini yıkadı
@tohum: masa-0039
@degisim: koni -> kova
Maşa bulutlu bir günde ormanda kovasıyla çamurdan pasta yapıyordu. Hafif bir yağmur yağıyordu. Birden karnı acıktı ve sepetindeki en sevdiği reçelli ekmeği yemek istedi. Ama çamur oyunu yüzünden elleri çamur içindeydi. Maşa önce ellerini otlara sildi, ama çamur çıkmadı. Sonra boş kovasını yağmurun altına koydu. Kovada biraz yağmur suyu birikti. Maşa bu suyla ellerini yıkadı ve çamur hemen çıktı. Sonra büyük bir ağacın altına oturdu. Ekmeğini afiyetle yedi. Maşa çok mutluydu, çünkü elleri temizdi ve karnı doymuştu.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden karnı acıktı ve sepetindeki en sevdiği reçelli ekmeği yemek istedi.»
   - Açıklama: Asıl sorun olan çamurlu eller ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "elleri çamur içindeydi"
   - Cümle 4: «Ama çamur oyunu yüzünden elleri çamur içindeydi.»
   - Açıklama: Asıl sorun olan çamurlu eller ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa önce ellerini otlara sildi"
   - Cümle 5: «Maşa önce ellerini otlara sildi, ama çamur çıkmadı.»
   - Açıklama: Çözüm başarısız bir denemeden sonra kova kurup su biriktirmeye dolanıyor, oysa eller doğrudan yağmurda yıkanabilirdi.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra boş kovasını yağmurun altına koydu"
   - Cümle 6: «Sonra boş kovasını yağmurun altına koydu.»
   - Açıklama: Kova çamurdan pasta yapmak için kullanılıyordu ama birden boş ve temiz suya uygun gibi anlatılıyor.
   - Açıklama: Maşa kovasıyla çamurdan pasta yapıyordu ama kova birden boş olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0039` birebir aynı, `@degisim: koni -> kova` (tutuyorsan), ardından `@onarim: db4338ad58d6cd402491bcf89e78592a4d5bb7b9`, sonra gövde.

### Hikâye 5: tohum masa-0040 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Daşa
@tohum: masa-0040
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boncuk', fiil 'kavuşmak', sıfat 'uyanık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Daşa
@plan: koşarken kutu elinden düştü ve boncuklar döküldü | özür diledi ve boncukları tek tek topladı
@tohum: masa-0040
@degisim: uyanık -> renkli
Rüzgar tepede hafif hafif esiyordu. Daşa çimenlere oturmuş, kolye yapmak için Maşa'yı bekliyordu. Maşa boncuk kutusuyla koşarak geldi, ama kutu elinden düştü. Renkli boncuklar çimenlerin arasına döküldü. Daşa çok üzüldü. "Özür dilerim, Daşa, hepsini hemen toplayacağım," dedi Maşa. Maşa çimenlere eğildi ve boncukları tek tek toplamayı denedi. Daşa da kutuyu açık tuttu. Sonunda bütün boncuklar kutudaydı. Daşa boncuklarına yine kavuştu ve gülümsedi. "Teşekkürler, Maşa, hadi kolyeyi birlikte yapalım," dedi Daşa. Maşa çok sevindi, çünkü kuzeni yine gülüyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "boncuklarına yine kavuştu"
   - Cümle 10: «Daşa boncuklarına yine kavuştu ve gülümsedi.»
   - Açıklama: 'Kavuşmak' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Daşa boncuklarına yine kavuştu"
   - Cümle 10: «Daşa boncuklarına yine kavuştu ve gülümsedi.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0040` birebir aynı, `@degisim: uyanık -> renkli` (tutuyorsan), ardından `@onarim: ecc6fe2f67e7640dbe9006a7399c3f576748516b`, sonra gövde.

### Hikâye 6: tohum masa-0041 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0041
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'filiz', fiil 'somurtmak', sıfat 'yağmurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: ıslak top kaydı ve dikenli çalının altına girdi | kirpiden yardım istedi ve kirpi topu dışarı itti
@tohum: masa-0041
@degisim: filiz -> top
Tepede hava yağmurluydu. Maşa kırmızı topunu çimenlerde zıplatıyordu. Islak top elinden kaydı ve dikenli bir çalının altına girdi. Maşa eğildi ama dikenler yüzünden topu alamadı. Sonra yerden bir dal aldı ve topu itmeyi denedi. Ama dal çok kısaydı. Maşa yere oturdu ve somurttu. O sırada çalının yanından küçük bir kirpi geçti. "Kirpi, topumu bana getirir misin?" diye sordu Maşa. Kirpi başını salladı ve çalının altına koştu. Burnuyla topu itip dışarı yuvarladı. Maşa topunu aldı ve kirpiye teşekkür etti. Maşa bundan sonra yapamadığı işlerde arkadaşlarından yardım istedi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "topu itmeyi denedi"
   - Cümle 5: «Sonra yerden bir dal aldı ve topu itmeyi denedi.»
   - Açıklama: Tohumdaki deneme özelliği işe yaramıyor; sorunu Maşa'nın denemesi değil kirpi çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0041` birebir aynı, `@degisim: filiz -> top` (tutuyorsan), ardından `@onarim: 625a1fed9a9ad0d1b7a1ef19ee495df88d027223`, sonra gövde.

### Hikâye 7: tohum masa-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0042
- yer: dağ (Ormanın yanındaki tepe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'nane', fiil 'tanıştırmak', sıfat 'neşeli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: sincap kuzeni tanımadığı için ağacın arkasına saklandı | fındıkları sincapla paylaştı ve sincap yanlarına geldi
@tohum: masa-0042
@degisim: nane -> fındık
Neşeli bir rüzgar esiyordu. Maşa, kuzeni Daşa'yı tepedeki sincapla tanıştırmak istiyordu. Ama sincap Daşa'yı tanımadığı için ağacın arkasına saklandı. Maşa önce sincaba el sallamayı denedi ama sincap çıkmadı. Sonra Maşa cebinden bir avuç fındık aldı. "Daşa, fındıkları sincapla paylaşalım mı?" diye sordu Maşa. "Evet, bence çok sevinir," dedi Daşa. İkisi onları ağacın dibine koydu. Sincap yavaşça çıktı ve bir tanesini aldı. Sonra Daşa'nın yanına gelip ona baktı. "Merhaba, sincap," dedi Daşa gülümseyerek. Maşa, Daşa ve sincap fındıkları birlikte mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Neşeli bir rüzgar esiyordu"
   - Cümle 1: «Neşeli bir rüzgar esiyordu.»
   - Açıklama: Rüzgar neşeli olamaz; kişileştirme mecazı küçük çocuğa uygun değil.
   - Açıklama: Rüzgar neşeli olmaz; mecaz 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0042` birebir aynı, `@degisim: nane -> fındık` (tutuyorsan), ardından `@onarim: 7937967cfe0609af47264fa1b518bef030b27b40`, sonra gövde.

### Hikâye 8: tohum masa-0043 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0043
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'güneş', fiil 'çalıştırmak', sıfat 'resimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: bahçeden bilinmeyen bir müzik sesi geldi | sesin geldiği yere gitti ve resimli kutuyu buldu
@tohum: masa-0043
Maşa güneşli bir sabah Koca Ayı'nın bahçesine geldi. Birden ince bir müzik sesi duydu. Maşa bu sesin nereden geldiğini çok merak etti. Önce havuçların arasına baktı ama orada hiçbir şey yoktu. Sonra sesin ağaç evin arkasından geldiğini anladı. Maşa oraya koştu ve Koca Ayı'yı gördü. Koca Ayı'nın elinde resimli küçük bir kutu vardı. Müzik bu kutudan geliyordu. Şarkı bitince Koca Ayı kutuyu Maşa'ya uzattı. Maşa kutunun kolunu çevirmeyi denedi. Böylece kutuyu kendisi çalıştırdı ve şarkı yeniden başladı. "Demek bu güzel müzik senin kutundan geliyormuş, Koca Ayı!" dedi Maşa. Sonra Maşa ile Koca Ayı bahçede mutlu mutlu dans etti.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden ince bir müzik sesi duydu"
   - Cümle 2: «Birden ince bir müzik sesi duydu.»
   - Açıklama: Bilinmeyen bir müzik sesi gerçek bir sorun değil; ses zaten Koca Ayı'nın kutusundan geliyor ve ortada çözülecek bir dert yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Maşa bu sesin nereden geldiğini çok merak etti"
   - Cümle 3: «Maşa bu sesin nereden geldiğini çok merak etti.»
   - Açıklama: Sorun yalnız bir meraktır; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce havuçların arasına baktı"
   - Cümle 4: «Önce havuçların arasına baktı ama orada hiçbir şey yoktu.»
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor; boşa giden bir arama adımı ve sebepsiz bir anlama adımı var.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Böylece kutuyu kendisi çalıştırdı"
   - Cümle 11: «Böylece kutuyu kendisi çalıştırdı ve şarkı yeniden başladı.»
   - Açıklama: 'Böylece' yalnızca denemeye bağlanıyor; denemek başarmak anlamına gelmediği için bağlaç yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0043` birebir aynı, ardından `@onarim: 8fe8445f1ea529e715eabb1c6741475377cd1c9c`, sonra gövde.

### Hikâye 9: tohum masa-0044 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap
@tohum: masa-0044
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bulmaca', fiil 'kokmak', sıfat 'dürüst'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | sincap
@plan: sincap bulmacanın son parçasını alıp ağaca kaçtı | kavanozu açıp sincaba bir kaşık reçel verdi
@tohum: masa-0044
@degisim: dürüst -> tatlı
Maşa bahçede sincapla resimli bir bulmaca yapıyordu. Sincap parçaları burnuyla itiyor, Maşa da onları yerlerine koyuyordu. Birden sincap son parçayı fındık sandı ve ağaca kaçtı. "Sincap, o fındık değil, bir bulmaca parçası!" dedi Maşa gülerek. Ama sincap dalda oturup parçayı sıkıca tuttu. Maşa ağacın altında biraz düşündü. Sonra evden tatlı çilek reçelini getirdi. Kavanozu açınca reçel çok güzel koktu. Maşa en sevdiği reçelden bir kaşık aldı ve sincaba uzattı. Sincap kokuyu aldı ve hemen aşağı indi. Parçayı Maşa'nın önüne bıraktı ve reçeli yaladı. Maşa son parçayı yerine taktı. Maşa çok sevindi, çünkü bulmacaları sonunda tamamlanmıştı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü bulmacaları sonunda tamamlanmıştı"
   - Cümle 13: «Maşa çok sevindi, çünkü bulmacaları sonunda tamamlanmıştı.»
   - Açıklama: 'Bulmacaları' tek bulmaca için çoğul gibi okunuyor; 'bulmaca sonunda tamamlanmıştı' olmalı.
   - Açıklama: Tek bulmaca ve tekil özne varken 'bulmacaları' eki uyumsuz; 'bulmacası' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0044` birebir aynı, `@degisim: dürüst -> tatlı` (tutuyorsan), ardından `@onarim: 0cd5fd8af1634d693f1f3d5f009b565b9e48627a`, sonra gövde.

### Hikâye 10: tohum masa-0046 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0046
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bisküvi', fiil 'koşuşturmak', sıfat 'vanilyalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi yaprakların altında uyuduğu için pikniğe gelemedi | sessizce bekledi ve reçelin kokusu kirpiyi uyandırdı
@tohum: masa-0046
Maşa ormanda Koca Ayı ile piknik yapıyordu. Sepette vanilyalı bisküvi ve reçel vardı. Ama kirpi arkadaşları yaprakların altında uyuyordu. Maşa onunla birlikte yemek istiyordu. Beklerken ağaçların arasında koşuşturdu. Koca Ayı parmağını ağzına götürdü. Maşa hemen durdu ve sessizce oturdu. Reçeli çok sevdiği için kavanozun kapağını açtı. Güzel koku yapraklara kadar gitti. Kirpi burnunu oynattı ve dışarı çıktı. "Günaydın, kirpi, seni bekledik!" dedi Maşa. Maşa her bisküviye reçel sürdü ve herkese birer tane verdi. Maşa çok sevindi, çünkü beklediği arkadaşı sonunda uyanmıştı.
```

**Hakem bulguları (8):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ama kirpi arkadaşları yaprakların"
   - Cümle 3: «Ama kirpi arkadaşları yaprakların altında uyuyordu.»
   - Açıklama: Tek kirpi için çoğul 'arkadaşları' kullanılmış; 'kirpi arkadaşı' olmalı.
   - Açıklama: 'Kirpi arkadaşları' çoğul da okunabiliyor ve sonraki tekil 'onunla' ile uyumsuz; 'kirpi arkadaşı' olmalı.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Ama kirpi arkadaşları yaprakların altında uyuyordu"
   - Cümle 3: «Ama kirpi arkadaşları yaprakların altında uyuyordu.»
   - Açıklama: Çoğul 'arkadaşları' olaya katılan birden çok canlı olarak okunabiliyor; kartta tek isimsiz kirpi yanı var.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Maşa onunla birlikte yemek"
   - Cümle 4: «Maşa onunla birlikte yemek istiyordu.»
   - Açıklama: Tekil 'onunla' zamiri çoğul 'arkadaşları' ile uyuşmuyor, kimi gösterdiği belirsiz.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Koca Ayı parmağını ağzına götürdü"
   - Cümle 6: «Koca Ayı parmağını ağzına götürdü.»
   - Açıklama: Amaç kirpiyi uyandırmakken sessiz olmaları isteniyor; hedefle eylem çelişiyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Reçeli çok sevdiği için kavanozun kapağını açtı"
   - Cümle 8: «Reçeli çok sevdiği için kavanozun kapağını açtı.»
   - Açıklama: Maşa kavanozu kirpiyi uyandırmak için değil reçeli sevdiği için açıyor; çözüm sebebe bilinçli yönelmiyor.
   - Açıklama: Maşa kirpiyi uyandırmak için değil reçeli sevdiği için kapağı açıyor; çözüm sebebe bilerek yönelmiyor.
   - Açıklama: Maşa kavanozu kirpiyi uyandırmak için değil kendi isteğiyle açıyor; çözüm sebebe bilerek yönelmiyor, tesadüfen geliyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Reçeli çok sevdiği için kavanozun kapağını açtı"
   - Cümle 8: «Reçeli çok sevdiği için kavanozun kapağını açtı.»
   - Açıklama: Çözüm tesadüfen, sebepsizce geliyor ve koşuşturma ayrıntısı olaya bağlanmıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Güzel koku yapraklara kadar gitti"
   - Cümle 9: «Güzel koku yapraklara kadar gitti.»
   - Açıklama: Kirpiyi uyandıran koku tesadüfen geliyor ve çözümü sebepsizce getiriyor.
8. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Maşa çok sevindi, çünkü"
   - Cümle 13: «Maşa çok sevindi, çünkü beklediği arkadaşı sonunda uyanmıştı.»
   - Açıklama: Art arda üç cümlede 'Maşa' adı gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0046` birebir aynı, ardından `@onarim: 4bdabc6e0b4631801a9cbd73d87622b1724daf00`, sonra gövde.

### Hikâye 11: tohum masa-0047 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Daşa
@tohum: masa-0047
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kereviz', fiil 'soğumak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Daşa
@plan: içecek güneşte kaldığı için ılık olmuştu | şişeyi soğuk sulu kovaya koyup gölgede bekledi
@tohum: masa-0047
@degisim: kereviz -> şişe
Hava çok sıcaktı. Maşa, kuzeni Daşa için bahçede çilek reçelinden bir içecek hazırlamıştı. Ama şişe güneşte kaldığı için içecek ılık olmuştu. Maşa evden bir kova soğuk su getirdi. Şişeyi kovaya koydu ve kovayı ağacın gölgesine taşıdı. Maşa beklerken şişeye birkaç kez dokundu. Sonunda içecek iyice soğudu. Tam o sırada bahçe kapısından Daşa geldi. "Sürpriz, Daşa, bu içecek senin için!" dedi Maşa. Daşa bir yudum aldı ve gülümsedi. "Çok güzel olmuş, teşekkür ederim, Maşa," dedi Daşa. Konuşkan Maşa şişeyi nasıl soğuttuğunu kuzenine anlattı. Maşa ile Daşa ağacın altında oturup içeceklerini mutlu mutlu içti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Konuşkan Maşa şişeyi nasıl"
   - Cümle 12: «Konuşkan Maşa şişeyi nasıl soğuttuğunu kuzenine anlattı.»
   - Açıklama: Tohumdaki özellik reçel sevgisi; kartın özellikler alanında olmayan konuşkanlık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0047` birebir aynı, `@degisim: kereviz -> şişe` (tutuyorsan), ardından `@onarim: 86956b5eb18cdd38666fb1204c8a832bd4642412`, sonra gövde.

### Hikâye 12: tohum masa-0048 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0048
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'zil', fiil 'değişmek', sıfat 'cesur'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: kozalak ipe çarptı ve zil yaprakların arasına düştü | yaprakları karıştırıp zilin sesini duydu ve buldu
@tohum: masa-0048
@degisim: cesur -> küçük
Maşa ormanda alçak bir dala küçük bir zil asmıştı. Zile kozalak atıyor, zil her seferinde çın diye çalıyordu. Ama bir kozalak ipe çarptı ve zil yerdeki yaprakların arasına düştü. Maşa yapraklara uzun uzun baktı ama zili göremedi. Sonra yaprakları ayağıyla karıştırmayı denedi. Yaprakların altından bir ses geldi. Zilin sesi orada biraz değişmişti ama Maşa onu hemen tanıdı. Maşa sese doğru eğildi ve zili buldu. Zili yeniden dala sıkıca bağladı. Biraz geri çekildi ve bir kozalak daha attı. Kozalak zile değdi ve zil yine çaldı. Maşa kozalak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Zilin sesi orada biraz değişmişti"
   - Cümle 7: «Zilin sesi orada biraz değişmişti ama Maşa onu hemen tanıdı.»
   - Açıklama: Sesin değişmesi hiçbir işe yaramayan, sebepsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0048` birebir aynı, `@degisim: cesur -> küçük` (tutuyorsan), ardından `@onarim: a0bd513ef8417caa2d21360668445fd7439ec4b0`, sonra gövde.
