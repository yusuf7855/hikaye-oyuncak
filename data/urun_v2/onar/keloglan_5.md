# Editör görevi (onarım): Keloğlan, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar5.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0001 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0001
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'yiyecek', fiil 'basmak', sıfat 'dar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: rüzgar yiyecek kabını banktan düşürüp uzağa yuvarladı | sesi dinledi ve kabı dar bir yerde buldu
@tohum: keloglan-0001
Rüzgar sert esiyordu. Keloğlan büyük taş sarayın bahçesinde yiyecek kabını arıyordu. Rüzgar kabı banktan düşürmüş ve otların üstünde uzağa yuvarlamıştı. Kabın içinde Keloğlan'ın ekmeği vardı. Birden yüksek kapının yanından ince bir ses geldi. Keloğlan sesi dikkatle dinleyip kabın yerini öğrenmek istedi. Yumuşak otlara basarak kapıya doğru yürüdü. Kapının dibinde iki taşın arasında dar bir yer vardı. Yiyecek kabı orada sıkışmıştı. Rüzgar esince kap taşlara çarpıyordu. Ses buradan geliyordu! Keloğlan kabı dar yerden yavaşça çekip aldı. Sonra banka oturdu ve ekmeğini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kabın yerini öğrenmek istedi"
   - Cümle 6: «Keloğlan sesi dikkatle dinleyip kabın yerini öğrenmek istedi.»
   - Açıklama: Tohumdaki 'yeni şeyler öğrenmeyi sever' özelliği yalnız kelime olarak geçiyor; kabı bulmak yeni bir şey öğrenmek değil, özellik işe yarar biçimde kullanılmıyor.
   - Açıklama: Kart özelliği yeni şeyler öğrenmeyi sevmek; burada 'öğrenmek' yalnız kaybolan kabın yerini bulmak anlamında geçiyor, özellik karttaki gibi kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0001` birebir aynı, ardından `@onarim: faf4631b065be192a5fc0147ee56eceee3f6ab2f`, sonra gövde.

### Hikâye 2: tohum keloglan-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0006
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: paylaşmak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'jöle', fiil 'çoğalmak', sıfat 'yırtık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: tek jöle vardı ve annesine hiç kalmadı | annesinden kesmeyi öğrendi ve jöleyi paylaştı
@tohum: keloglan-0006
@degisim: yırtık -> kırmızı
Bir sabah Keloğlan ile anası evde kırmızı bir jöle yaptı. Kap küçüktü, bu yüzden tek bir jöle çıktı. Anası jöleyi Keloğlan'a verdi ama kendine hiç kalmadı. Keloğlan jöleyi annesiyle paylaşmak istedi. "Anneciğim, bunu nasıl keserim?" diye sordu Keloğlan. "Kaşıkla önce ortadan, sonra yandan kes," dedi anası. Keloğlan bunu hemen öğrendi. Kaşık jöleye girince jöle titredi ve Keloğlan güldü. Parçalar çoğaldı ve tabakta dört küçük kare oldu. Keloğlan iki kareyi annesine verdi. Anası bir kare yedi ve gülümsedi. "Seninle yemek çok güzel, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "kırmızı bir jöle yaptı"
   - Cümle 1: «Bir sabah Keloğlan ile anası evde kırmızı bir jöle yaptı.»
   - Açıklama: Jöle çağdaş bir yiyecek; kartın tohum yasak kategorileri notundaki masal köyü dünyasına uymuyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "evde kırmızı bir jöle yaptı"
   - Cümle 1: «Bir sabah Keloğlan ile anası evde kırmızı bir jöle yaptı.»
   - Açıklama: Jöle, kartın tohum_yasak_kategoriler notundaki masal köyü dünyasına uymayan çağdaş bir yiyecek; kapalı dünyada yeri belirsiz.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Parçalar çoğaldı ve tabakta"
   - Cümle 9: «Parçalar çoğaldı ve tabakta dört küçük kare oldu.»
   - Açıklama: Parçalar kendiliğinden çoğalmaz; jöle kesilerek bölündü.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0006` birebir aynı, `@degisim: yırtık -> kırmızı` (tutuyorsan), ardından `@onarim: 529825ea2fc1210f8363a31099a3ab84a3f8befa`, sonra gövde.

### Hikâye 3: tohum keloglan-0007 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0007
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kartopu', fiil 'kaplamak', sıfat 'düzenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: kartopu pasta için çok küçüktü | düşen topu karda iterek büyüttü
@tohum: keloglan-0007
Keloğlan dağda Bilgecan Dede'ye kardan bir pasta yapmak istedi. Kar bütün tepeyi kaplamıştı ve Dede ağacın altında kitap okuyordu. Ama Keloğlan'ın kartopu çok küçüktü, pasta için büyük bir top gerekiyordu. Keloğlan biraz sakardı ve kartopu elinden düştü. Top karda yuvarlandı ve üstüne kar yapıştı. Keloğlan bunu görünce güldü ve topu karda itti. Top büyüdü ve kocaman bir pasta oldu. Keloğlan pastanın üstüne düzenli bir sırayla küçük taşlar dizdi. "Dede, bak, sana bir sürprizim var!" dedi Keloğlan. Bilgecan Dede kitabını kapattı ve pastayı gördü. "Ne güzel bir pasta, çok teşekkür ederim, Keloğlan!" dedi Bilgecan Dede.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve"
   - Cümle 4: «Keloğlan biraz sakardı ve kartopu elinden düştü.»
   - Açıklama: 'Sakar' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kartopu elinden düştü"
   - Cümle 4: «Keloğlan biraz sakardı ve kartopu elinden düştü.»
   - Açıklama: Çözüm Keloğlan'ın düşünmesinden değil, topun rastlantıyla elinden düşmesinden çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve kartopu elinden düştü"
   - Cümle 4: «Keloğlan biraz sakardı ve kartopu elinden düştü.»
   - Açıklama: Çözüm figürün düşüncesinden değil, sebepsiz bir kazadan doğuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0007` birebir aynı, ardından `@onarim: 3611fa6c24b55503e214646166bb91fd092aea1c`, sonra gövde.

### Hikâye 4: tohum keloglan-0011 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0011
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tarak', fiil 'yeşillenmek', sıfat 'nazik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: dedenin tahta tarağı cebinden düşüp kayboldu | yere dikkatle bakıp tarağı buldu ve geri verdi
@tohum: keloglan-0011
Keloğlan ormanda Bilgecan Dede ile yürüyordu. Büyük ağaçlar yeni yeşillenmişti. Bilgecan Dede'nin tahta tarağı cebinden düşüp kaybolmuştu. "Tarak cebimde yok!" dedi Bilgecan Dede. "Ben bulurum!" dedi Keloğlan. Yavaşça geri yürüdü ve yere dikkatle baktı. Yolun kenarında uzun otlar vardı. Keloğlan otların arasını tek tek aradı. Sonunda tarağı bir ağacın dibinde buldu. Tarak çok güzeldi ve Keloğlan onu beğendi. Ama Keloğlan dürüst davrandı ve tarağı Bilgecan Dede'ye götürdü. "İşte tarağını buldum!" dedi Keloğlan. Bilgecan Dede nazik bir sesle teşekkür etti. Sonra Keloğlan ile Bilgecan Dede ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yolun kenarında uzun otlar vardı"
   - Cümle 7: «Yolun kenarında uzun otlar vardı.»
   - Açıklama: Otlar aranacak yer olarak kuruluyor ama tarak otlarda değil bir ağacın dibinde bulunuyor, kurulan ayrıntı işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0011` birebir aynı, ardından `@onarim: 08525f122646bf34b2fe0d9968ae5b7287dfa262`, sonra gövde.

### Hikâye 5: tohum keloglan-0012 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0012
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'karnabahar', fiil 'yardımlaşmak', sıfat 'utangaç'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: yaprakların altında ne olduğu belli değildi | annesiyle yaprakları açıp karnabaharı buldu
@tohum: keloglan-0012
@degisim: utangaç -> beyaz
Keloğlan evde masanın üstünde yapraklara sarılı büyük bir şey gördü. Yapraklar çok sıkıydı ve içi hiç görünmüyordu. Keloğlan içinde ne olduğunu çok merak etti. "Anneciğim, bu yaprakların altında ne var?" diye sordu Keloğlan. "Gel, yardımlaşıp birlikte açalım," dedi anası. Anası onu tuttu, Keloğlan da yaprakları tek tek çekti. Keloğlan biraz sakardı ve büyük bir yaprağı yere düşürdü. O yaprağın altından beyaz, yuvarlak bir şey göründü. "Bu bir karnabahar, akşam yemeğimiz," dedi anası. Keloğlan beyaz karnabahara dokundu ve çok sevindi. "Yardımın için teşekkürler, Keloğlan," dedi anası. "Seninle bulmak çok eğlenceliydi, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yaprakların altında ne olduğu belli değildi"
   - Cümle 0 (plan satırı): «yaprakların altında ne olduğu belli değildi | annesiyle yaprakları açıp karnabaharı buldu»
   - Açıklama: Sorun yalnız bir merak; çocuğun önemseyeceği gerçek bir sorun yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Keloğlan içinde ne olduğunu çok merak etti"
   - Cümle 3: «Keloğlan içinde ne olduğunu çok merak etti.»
   - Açıklama: Sorun yalnız bir merak; masadaki paketin içini bilmemek çocuğun önemseyeceği bir güçlük değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Anası onu tuttu"
   - Cümle 6: «Anası onu tuttu, Keloğlan da yaprakları tek tek çekti.»
   - Açıklama: 'Onu' zamiri Keloğlan'ı mı karnabaharı mı gösteriyor belli değil.
   - Açıklama: 'onu' zamirinin Keloğlan'ı mı yoksa yapraklı şeyi mi gösterdiği belli değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Anası onu tuttu"
   - Cümle 6: «Anası onu tuttu, Keloğlan da yaprakları tek tek çekti.»
   - Açıklama: Ananın Keloğlan'ı neden tuttuğu belli değil; ayrıntı işlevsiz ve sebepsiz.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve büyük bir yaprağı yere düşürdü"
   - Cümle 7: «Keloğlan biraz sakardı ve büyük bir yaprağı yere düşürdü.»
   - Açıklama: Sakarlık çözüme bir şey katmıyor ve karnabaharı tesadüfen ortaya çıkarıyor.
   - Açıklama: Çözüm, sakarlıkla bir yaprağın düşmesiyle tesadüfen geliyor.
6. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu bir karnabahar, akşam yemeğimiz"
   - Cümle 9: «"Bu bir karnabahar, akşam yemeğimiz," dedi anası.»
   - Açıklama: Anne içindekini zaten biliyor; sorun yalnız yapay bir merak, gerçek bir sebebi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0012` birebir aynı, `@degisim: utangaç -> beyaz` (tutuyorsan), ardından `@onarim: 901c0784fc7cf807ebe23e26c9422d9377c6d825`, sonra gövde.

### Hikâye 6: tohum keloglan-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0013
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'askı', fiil 'dökmek', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepede ince bir sesin nereden geldiği belli değildi | ağaca bakıp sesin şişeden geldiğini buldu
@tohum: keloglan-0013
Tepede serin bir rüzgar esiyordu. Keloğlan bir kayanın yanında oturmuş dinleniyordu. Birden ağaçtan ince bir ses geldi. Keloğlan bu sesi çok merak etti. Önce kayaların arkasına baktı ama bir şey bulamadı. Sonra ağaca yürüdü ve askıda asılı çantasına baktı. Çantada su şişesi vardı ve rüzgar şişenin ağzına esiyordu. İnce ses şişeden geliyordu. Şişenin üstünde işaretli çizgiler vardı. Keloğlan suyun birazını ilk çizgiye kadar yere döktü. Rüzgar yine esti ve bu kez kalın bir ses çıktı. Keloğlan böylece az suyla sesin kalın olduğunu öğrendi. Sonra şişeyle ince ve kalın sesler çıkarmaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "askıda asılı çantasına baktı"
   - Cümle 6: «Sonra ağaca yürüdü ve askıda asılı çantasına baktı.»
   - Açıklama: 'Askıda' ile 'asılı' aynı şeyi söylüyor; gereksiz tekrar.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şişenin üstünde işaretli çizgiler vardı"
   - Cümle 9: «Şişenin üstünde işaretli çizgiler vardı.»
   - Açıklama: Sorun çözüldükten sonra sebepsiz beliren çizgiler plana bağlı olmayan yeni bir deneye yol açıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keloğlan suyun birazını ilk çizgiye kadar"
   - Cümle 10: «Keloğlan suyun birazını ilk çizgiye kadar yere döktü.»
   - Açıklama: Sesin kaynağı bulunduktan sonra ses kalınlığı deneyi olan ikinci bir olay başlıyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "az suyla sesin kalın olduğunu öğrendi"
   - Cümle 12: «Keloğlan böylece az suyla sesin kalın olduğunu öğrendi.»
   - Açıklama: Cümle bozuk kurulmuş; 'su azalınca sesin kalınlaştığını' anlamı eksik eklerle verilmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0013` birebir aynı, ardından `@onarim: 6a3f2bec91836ef66e08417b6a31e52882d5e48a`, sonra gövde.

### Hikâye 7: tohum keloglan-0014 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0014
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'küpe', fiil 'giyinmek', sıfat 'kalın'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: çalıda sallanan pembe şeylerin ne olduğu belli değildi | yakından bakıp onların çiçek olduğunu buldu
@tohum: keloglan-0014
Bir sabah Keloğlan ile Bilgecan Dede tepeye çıktı. Hava soğuktu, bu yüzden ikisi de kalın giyinmişti. Keloğlan bir çalıda sallanan pembe, küçük şeyler gördü. Bunların ne olduğunu çok merak etti. "Dede, bunlar meyve mi?" diye sordu Keloğlan. "Yakından bak, belki sen bulursun," dedi Bilgecan Dede. Keloğlan eğildi ve dikkatle baktı. "Bunlar çiçek, yaprakları var!" dedi Keloğlan. "Evet, adı küpe çiçeği, çünkü küpe gibi sallanır," dedi Bilgecan Dede. Keloğlan yere düşmüş bir çiçeği aldı ve kulağına taktı. Bilgecan Dede bunu görünce güldü. "Teşekkürler, Dede, bugün yeni bir çiçek öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bu yüzden ikisi de kalın giyinmişti"
   - Cümle 2: «Hava soğuktu, bu yüzden ikisi de kalın giyinmişti.»
   - Açıklama: Kalın giyinme ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0014` birebir aynı, ardından `@onarim: e8bf8d428afce5abb47af7492545172870043ef1`, sonra gövde.

### Hikâye 8: tohum keloglan-0016 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0016
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'testi', fiil 'oynamak', sıfat 'minik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: top ağacın dibinde dar bir deliğe düştü | arkadaşından yardım isteyip deliğe su döktü
@tohum: keloglan-0016
Ormanda büyük ağaçların altında Keloğlan ile Balkız top oynuyordu. Yanlarında içmek için su dolu bir testi vardı. Birden minik top yuvarlandı ve ağacın dibinde dar bir deliğe düştü. Keloğlan eğilip baktı ama deliğe eli sığmadı. "Balkız, bana yardım eder misin?" diye sordu Keloğlan. Balkız testiyi gösterdi. "Deliğe su dök, top yukarı çıkar," dedi Balkız. Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü. İkisi de buna güldü. Keloğlan bu kez testiyi yavaşça deliğe eğdi. Minik top suyla yukarı çıktı ve Keloğlan onu aldı. Keloğlan çok sevindi, çünkü yardım istemek topunu geri getirmişti.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Deliğe su dök, top yukarı çıkar"
   - Cümle 7: «"Deliğe su dök, top yukarı çıkar," dedi Balkız.»
   - Açıklama: Çözüm fikrini Balkız buluyor; Keloğlan yalnız onun dediğini uyguluyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yardım istemek topunu geri getirmişti"
   - Cümle 12: «Keloğlan çok sevindi, çünkü yardım istemek topunu geri getirmişti.»
   - Açıklama: Soyut 'yardım istemek' eylemi topu getiren özne gibi mecazlı kullanılmış.
   - Açıklama: Soyut 'yardım istemek' özne olarak topu getiriyor; mecazlı ve somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0016` birebir aynı, ardından `@onarim: b8422857f02fea55cd3884e120a27f979d7cfa49`, sonra gövde.

### Hikâye 9: tohum keloglan-0018 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0018
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'vanilya', fiil 'küçülmek', sıfat 'sıkı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: üç kurabiye ikisine eşit gelmedi | evde bir kurabiye yediğini söyleyip ikisini annesine verdi
@tohum: keloglan-0018
@degisim: küçülmek -> bölmek
Keloğlan ile anası dağda bir kayanın üstüne oturdu. Anası sıkı bağlı çantasını açtı ve üç vanilyalı kurabiye çıkardı. Ama üç kurabiyeyi ikiye eşit bölmek zordu. "Sen iki tane ye, Keloğlan," dedi anası. Keloğlan dürüst bir çocuktu ve başını iki yana salladı. "Hayır, anneciğim, ben evde bir kurabiye yedim," dedi Keloğlan. Sonra iki kurabiyeyi annesine verdi ve kendisi bir tane aldı. Böylece ikisi de iki kurabiye yemiş oldu. Kurabiyeler çok güzel vanilya kokuyordu. Anası kurabiyelerini yedi ve Keloğlan'a sarıldı. "Çok teşekkürler, Keloğlan, seninle burada olmak çok güzel!" dedi anası.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ikisine eşit gelmedi"
   - Cümle 0 (plan satırı): «üç kurabiye ikisine eşit gelmedi | evde bir kurabiye yediğini söyleyip ikisini annesine verdi»
   - Açıklama: Kurabiye 'eşit gelmez'; 'ikiye eşit bölünmedi' gibi doğru bir fiil gerekir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sıkı bağlı çantasını açtı"
   - Cümle 2: «Anası sıkı bağlı çantasını açtı ve üç vanilyalı kurabiye çıkardı.»
   - Açıklama: Çantanın sıkı bağlı olması bir zorluk kuracakmış gibi veriliyor ama hiç kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ben evde bir kurabiye yedim"
   - Cümle 6: «"Hayır, anneciğim, ben evde bir kurabiye yedim," dedi Keloğlan.»
   - Açıklama: Dürüstlük özelliği, annesine fazla kurabiye bırakmak için söylenmiş olabilecek doğrulanmayan bir iddiaya bağlanıyor ve karttaki gibi işe yarar biçimde kullanılmıyor.
4. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "ikisi de iki kurabiye yemiş oldu"
   - Cümle 8: «Böylece ikisi de iki kurabiye yemiş oldu.»
   - Açıklama: Anlatımda '-miş oldu' kalıbı kullanılıyor; düz -dı'lı geçmiş zaman değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0018` birebir aynı, `@degisim: küçülmek -> bölmek` (tutuyorsan), ardından `@onarim: aa99669384d45806b96e6496d197bd31ec247d6f`, sonra gövde.

### Hikâye 10: tohum keloglan-0019 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0019
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çember', fiil 'eğlenmek', sıfat 'uykulu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: odunları tutan eski ip koptu ve odunlar döküldü | odunları toplayıp çemberin içine dizdi
@tohum: keloglan-0019
Bir sabah Keloğlan ormanda tahta çemberini yuvarlayıp eğleniyordu. Uykulu eşeği Karakaçan da sırtında odunlarla yanında yürüyordu. Birden odunları tutan eski ip koptu ve odunlar yere döküldü. Karakaçan durdu ve üzgün üzgün başını eğdi. Keloğlan odunları tek tek topladı. Yük ağırdı ama Keloğlan dürüst bir çocuktu ve hiç durmadı. Sonra odunları çemberin içine sıkıca dizdi. Çember bütün odunları bir arada tuttu. Keloğlan yükü eşeğinin sırtına dikkatle koydu. "Artık odunlar düşmez, Karakaçan," dedi Keloğlan. Karakaçan esnedi, başını salladı ve yavaşça yürüdü. Keloğlan bundan sonra yola çıkmadan önce ipleri hep kontrol etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve hiç durmadı"
   - Cümle 6: «Yük ağırdı ama Keloğlan dürüst bir çocuktu ve hiç durmadı.»
   - Açıklama: Ağır yükü bırakmadan çalışmak dürüstlükle ilgili değil; 'dürüst' kelimesi yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Yük ağırdı ama Keloğlan dürüst bir çocuktu ve hiç durmadı.»
   - Açıklama: Dürüstlük ağır yükü taşımaya devam etmekle ilgili değil; özellik kelimesi yanlış anlamda kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve hiç durmadı"
   - Cümle 6: «Yük ağırdı ama Keloğlan dürüst bir çocuktu ve hiç durmadı.»
   - Açıklama: Tohumdaki dürüstlük özelliği işe yarar biçimde kullanılmıyor; dürüst kelimesi yalnız azmi anlatmak için yanlış yerde geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Yük ağırdı ama Keloğlan dürüst bir çocuktu ve hiç durmadı.»
   - Açıklama: Dürüstlük odun taşıma olayıyla ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve hiç durmadı"
   - Cümle 6: «Yük ağırdı ama Keloğlan dürüst bir çocuktu ve hiç durmadı.»
   - Açıklama: Dürüst olmak yorulmadan çalışmayı açıklamıyor; sebep-sonuç bağı kopuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0019` birebir aynı, ardından `@onarim: edefd2849d9b3b69b6108d84928b964e1e0adb3d`, sonra gövde.

### Hikâye 11: tohum keloglan-0020 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0020
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kaktüs', fiil 'koparmak', sıfat 'yağmurlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: küçük yaprak gemisi suda batıyordu | büyük bir yaprak koparıp kenarlarını kıvırdı
@tohum: keloglan-0020
@degisim: kaktüs -> yaprak
Bir sabah ormanda hava yağmurluydu ve yerde küçük bir su yolu vardı. Keloğlan ile Bilgecan Dede bu suda yaprak gemisi yarışı yapıyordu. Ama Keloğlan'ın gemisi hep batıyordu, çünkü yaprağı çok küçüktü. "Dede, benim gemim neden batıyor?" diye sordu Keloğlan. "Büyük bir yaprak al ve kenarlarını kıvır," dedi Bilgecan Dede. Keloğlan daldan geniş bir yaprak kopardı ve kenarlarını kıvırdı. Yeni gemi suda batmadı ve hızla yüzdü. Ama gemi suda döndü ve Dede'nin ayağına çarptı. İkisi de buna çok güldü. Sonra iki gemi yan yana yüzdü. "Teşekkürler, Dede, yüzen bir gemi yapmayı öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama gemi suda döndü ve Dede'nin ayağına çarptı"
   - Cümle 8: «Ama gemi suda döndü ve Dede'nin ayağına çarptı.»
   - Açıklama: Çözümden sonra sorunla ilgisiz, işlevsiz bir yan olay ekleniyor.
   - Açıklama: Çözümden sonra 'Ama' ile yeni bir aksilik kuruluyor ama hiçbir sonuca bağlanmayan işlevsiz bir olay olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0020` birebir aynı, `@degisim: kaktüs -> yaprak` (tutuyorsan), ardından `@onarim: 80d67049115b31f7696e917df16c91a0be9e0b34`, sonra gövde.
