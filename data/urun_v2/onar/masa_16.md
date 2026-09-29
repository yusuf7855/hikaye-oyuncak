# Editör görevi (onarım): Maşa, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0055 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0055
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kapı', fiil 'söylemek', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: ormanda kapı sesine benzeyen bir ses duydu | ağaçlara vurup sesi yapan kuru dalı buldu
@tohum: masa-0055
Ormandaki patikada Maşa şarkı söyleyerek yürüyordu. Birden tak tak diye garip bir ses duydu. Maşa şarkıyı bıraktı ve sesin nereden geldiğini çok merak etti. Bu ses bir kapı sesine benziyordu. Maşa sesi bulmak için ağaçlara vurmayı denedi. İlk ağaçtan çok küçük bir ses çıktı. Geniş bir ağaca vurunca aynı ses çıktı. Maşa bu ağacın yukarısına baktı. Rüzgar kuru bir dalı sallıyordu ve dal gövdeye çarpıyordu. Garip ses işte bu daldan geliyordu. Maşa sesi bulduğu için sevinçle zıpladı. Maşa bundan sonra bir ses duyunca önce etrafına dikkatle baktı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden tak tak diye garip bir ses duydu"
   - Cümle 2: «Birden tak tak diye garip bir ses duydu.»
   - Açıklama: Garip bir ses duymak yalnız bir merak; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa sesi bulmak için ağaçlara vurmayı denedi"
   - Cümle 5: «Maşa sesi bulmak için ağaçlara vurmayı denedi.»
   - Açıklama: Ağaçlara vurmak sesin kaynağını aramaya doğrudan yönelmiyor; ses dalın rüzgarla çarpmasından geliyor.
   - Açıklama: Sesin kaynağını bulmak için ağaçlara vurmak sebebe yönelmiyor; sesi dinleyip etrafa bakmak gerekirdi.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "vurunca aynı ses çıktı"
   - Cümle 7: «Geniş bir ağaca vurunca aynı ses çıktı.»
   - Açıklama: 'Aynı ses' ilk ağacın sesini mi garip sesi mi gösteriyor belli değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bu ağacın yukarısına baktı"
   - Cümle 8: «Maşa bu ağacın yukarısına baktı.»
   - Açıklama: 'Ağacın yukarısına' bozuk bir kullanım; 'ağacın tepesine' olmalı.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bir ses duyunca önce etrafına dikkatle baktı"
   - Cümle 12: «Maşa bundan sonra bir ses duyunca önce etrafına dikkatle baktı.»
   - Açıklama: Ders yaşanan olaydan çıkmıyor; Maşa etrafına bakarak değil ağaçlara vurarak sesi buldu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0055` birebir aynı, ardından `@onarim: 1bcdc75f02b42149a85b614316d19997865077a5`, sonra gövde.

### Hikâye 2: tohum masa-0056 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0056
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yağ', fiil 'sakinleşmek', sıfat 'sabırsız'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: yaprakların arasından gelen sesi merak etti | sakinleşti ve yere elma koyunca kirpiyi gördü
@tohum: masa-0056
@degisim: yağ -> elma
Maşa ormanda elinde bir elmayla yürüyordu. Birden yaprakların arasından hışır hışır bir ses geldi. Maşa bu sesi çok merak etti. Maşa çok sabırsızdı ve hemen sesin geldiği yere koştu. Ama ses kesildi ve hiçbir şey kıpırdamadı. Maşa biraz bekledi ve sakinleşti. Sonra elmasını yere koymayı denedi. Yavaşça geri çekildi ve sessizce oturdu. Az sonra yaprakların arasından küçük bir burun çıktı. Ardından dikenli bir kirpi göründü. Kirpi elmayı kokladı ve mutlu mutlu yemeye başladı. Maşa çok sevindi, çünkü sesi yapan kirpiyi sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elmasını yere koymayı denedi"
   - Cümle 7: «Sonra elmasını yere koymayı denedi.»
   - Açıklama: Maşa elmayı doğrudan koyuyor; 'denedi' fiili burada yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0056` birebir aynı, `@degisim: yağ -> elma` (tutuyorsan), ardından `@onarim: 9608f62afffa6afac842ad210771fd74b28b326e`, sonra gövde.

### Hikâye 3: tohum masa-0057 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0057
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yosun', fiil 'içmek', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: sincap saklanan reçel kavanozunun üstüne yosun koydu | sincabın taşıdığı yosunu izleyip kavanozu buldu
@tohum: masa-0057
@degisim: içmek -> saklamak
Maşa tepede Koca Ayı ve sincapla bir arama oyunu oynuyordu. Koca Ayı, Maşa'nın özel reçel kavanozunu bir taşın arkasına sakladı. Ama sincap oyuna katıldı ve kavanozun üstünü yosunla örttü. Maşa taşların arkasına baktı ama kavanozu göremedi. Sonra sincabın ağzında biraz yosun gördü. Sincap yosunu büyük bir taşın yanına bıraktı. Maşa hemen o taşa koştu ve yosunları kaldırdı. Reçel kavanozu tam oradaydı! "Buldum, sincap, sen çok komiksin!" dedi Maşa. Koca Ayı güldü ve ellerini çırptı. Sincap da kuyruğunu salladı. Maşa çok sevindi, çünkü sevdiği reçeli oyunun sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama sincap oyuna katıldı"
   - Cümle 3: «Ama sincap oyuna katıldı ve kavanozun üstünü yosunla örttü.»
   - Açıklama: Sincap ilk cümlede zaten oyunda tanıtılmışken yeniden oyuna katılıyor gibi tanıtılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sincap yosunu büyük bir taşın yanına bıraktı"
   - Cümle 6: «Sincap yosunu büyük bir taşın yanına bıraktı.»
   - Açıklama: Sincabın yosunu tam kavanozun yanına getirmesi çözümü sebepsizce getiriyor ve Maşa'nın kendi aramasının yerini alıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0057` birebir aynı, `@degisim: içmek -> saklamak` (tutuyorsan), ardından `@onarim: 23ff175e499aa3b634ba7d28407ad6d1558067b9`, sonra gövde.

### Hikâye 4: tohum masa-0058 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0058
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'basamak', fiil 'şişirmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: parmakları reçelli olunca balon elinden kaydı | parmaklarını otlara silip balonu yeniden şişirdi
@tohum: masa-0058
@degisim: düzenli -> sıkı
Güneş parlıyordu. Maşa tepede reçelli ekmeğini bitirdi ve kırmızı bir balon şişirdi. Ama balonu bağlarken reçelli parmakları kaydı ve balon kaçtı. Balon komik bir sesle tepede sağa sola uçtu. Sonra söndü ve taş bir basamağın üstüne düştü. Maşa buna çok güldü. Sonra parmaklarını yumuşak otlara sildi. Balonu yeniden şişirdi ve ucuna sıkı bir düğüm attı. Bu kez balon hiç kaçmadı. Maşa balonu havaya attı ve yakaladı. Maşa balonuyla tepede mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "reçelli parmakları kaydı ve balon kaçtı"
   - Cümle 3: «Ama balonu bağlarken reçelli parmakları kaydı ve balon kaçtı.»
   - Açıklama: Tohumdaki reçel özelliği iki kez geçiyor ve çözümde işe yaramıyor, yalnız sorunu doğuruyor.
   - Açıklama: Tohumdaki reçel özelliği işe yarar biçimde değil, yalnız sorunun nedeni olarak kullanılıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Maşa buna çok güldü"
   - Cümle 6: «Maşa buna çok güldü.»
   - Açıklama: Balonun kaçması Maşa'yı üzmüyor, güldürüyor; sorun çocuğun önemseyeceği bir sorun gibi kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0058` birebir aynı, `@degisim: düzenli -> sıkı` (tutuyorsan), ardından `@onarim: 428db962412592ec32a55bc6a944b4ebbeda2053`, sonra gövde.

### Hikâye 5: tohum masa-0060 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0060
- yer: dağ (Ormanın yanındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'gül', fiil 'uzanmak', sıfat 'yapışkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: güller birbirine bağlı değildi ve taç dağıldı | gülleri uzun otlarla birbirine bağladı
@tohum: masa-0060
@degisim: yapışkan -> kırmızı
Tepede Koca Ayı çimlerin üstüne uzanmış uyuyordu. Maşa ile kirpi ona tepedeki güllerden bir taç yapmak istedi. Ama güller birbirine bağlı değildi ve taç hemen dağıldı. Kirpi yerdeki güllerden birini burnuyla Maşa'ya itti. Maşa biraz düşündü. Sonra gülleri uzun otlarla birbirine bağlamayı denedi. Otlar gülleri sıkıca tuttu ve taç artık bozulmadı. Maşa kırmızı tacı yavaşça Koca Ayı'nın başına koydu. Koca Ayı uyandı ve tacına dokundu. Sonra kocaman gülümsedi ve Maşa'ya sarıldı. Kirpi de mutlu mutlu tacı kokladı. "Sürpriz, Koca Ayı! Bu taç senin için!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kirpi yerdeki güllerden birini burnuyla Maşa'ya itti"
   - Cümle 4: «Kirpi yerdeki güllerden birini burnuyla Maşa'ya itti.»
   - Açıklama: Kirpinin gül itmesi çözüme bağlanmayan işlevsiz bir ayrıntı.
   - Açıklama: Kirpinin gülü itmesi çözüme bir katkı yapmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0060` birebir aynı, `@degisim: yapışkan -> kırmızı` (tutuyorsan), ardından `@onarim: 42f338a1e7bab4c96b8278fb6c344b81d3804221`, sonra gövde.

### Hikâye 6: tohum masa-0062 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0062
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'külah', fiil 'çırpmak', sıfat 'yamuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: tanımadığı sincap utandı ve yaprakların arasına saklandı | yapraktan külah yapıp içine fındık koydu
@tohum: masa-0062
Maşa ormanda kavanozundan reçel yiyerek yürüyordu. Bir ağacın dalında daha önce görmediği bir sincap gördü. Sincap onu görünce utandı ve yaprakların arasına saklandı. "Merhaba, sincap, benimle arkadaş olur musun?" diye sordu Maşa. Sonra ona reçelini uzattı. Ama sincap reçeli kokladı ve başını çevirdi. Maşa etrafına baktı ve yerde fındıklar gördü. Büyük bir yapraktan yamuk bir külah yaptı. Külahı fındıkla doldurdu ve ağacın dibine koydu. Sincap hemen aşağı indi ve bir fındık aldı. Sonra Maşa'nın yanına geldi ve kuyruğunu salladı. Maşa sevinçle ellerini yavaşça çırptı. Maşa çok mutluydu, çünkü yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sincap reçeli kokladı ve başını çevirdi"
   - Cümle 6: «Ama sincap reçeli kokladı ve başını çevirdi.»
   - Açıklama: Tohumdaki reçel özelliği işe yaramıyor; sorunu fındık çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0062` birebir aynı, ardından `@onarim: 45275f0083f8808031b91095f2ab1b2a1359c080`, sonra gövde.

### Hikâye 7: tohum masa-0063 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0063
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'şemsiye', fiil 'ayırmak', sıfat 'pahalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: yağmur başladı ve açık kavanozlara su damladı | kuzeninden şemsiye isteyip dükkanın yanına dikti
@tohum: masa-0063
Bir sabah Maşa ile kuzeni Daşa ormanda dükkan oyunu oynuyordu. Maşa bir kütüğün üstüne üç kavanoz reçel dizdi. Ama birden yağmur başladı ve açık kavanozlara su damladı. "Reçellerim ıslanıyor!" dedi Maşa. Daşa şehirden şemsiyesini getirmişti. "Daşa, şemsiyeni bize verir misin?" diye sordu Maşa. Daşa hemen verdi. Maşa şemsiyeyi açtı ve kütüğün yanına dikti. Artık kavanozlar hiç ıslanmadı. Maşa en güzel kavanozu Daşa için ayırdı. "Bu reçel pahalı mı?" diye sordu Daşa gülerek. "Hayır, Daşa, sana hediye!" dedi Maşa. Maşa ile Daşa çok sevindi, çünkü dükkanları yağmurda da açık kalmıştı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "üç kavanoz reçel dizdi"
   - Cümle 2: «Maşa bir kütüğün üstüne üç kavanoz reçel dizdi.»
   - Açıklama: Tohumdaki reçel özelliği birçok cümlede tekrar ediliyor ve Maşa'nın reçeli sevmesi çözümde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Daşa şehirden şemsiyesini getirmişti"
   - Cümle 5: «Daşa şehirden şemsiyesini getirmişti.»
   - Açıklama: Şemsiye önceden kurulmadan, tam gerektiği anda çözümü getirmek için beliriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Bu reçel pahalı mı?""
   - Cümle 11: «"Bu reçel pahalı mı?" diye sordu Daşa gülerek.»
   - Açıklama: Fiyat kavramı olan 'pahalı' 3 yaşındaki bir çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0063` birebir aynı, ardından `@onarim: f15cb7cf2969206bb4cdaaa2308c598e63ba86d8`, sonra gövde.
