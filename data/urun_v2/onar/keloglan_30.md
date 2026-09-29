# Editör görevi (onarım): Keloğlan, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0099 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0099
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kristal', fiil 'yarışmak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: dedenin bilyeleri torbanın deliğinden düşmüştü | bilyelerini saydı ve dedeyle eşit paylaştı
@tohum: keloglan-0099
Şatonun büyük bahçesinde Keloğlan ile Bilgecan Dede bilye yarışı yapacaktı. Keloğlan'ın torbası kristal bilye doluydu ama Dede'nin torbası boştu. Dede'nin bilyeleri yolda torbanın deliğinden düşmüştü. Keloğlan torbasını açtı ve bilyeleri çimenlere döktü. Onları tek tek saydı ve dürüst bir şekilde ikiye ayırdı. Altı bilye Keloğlan'a, altı bilye de Dede'ye kaldı. Sonra ikisi bilyelerini taş yolda yuvarladı ve yarıştı. Bazen Keloğlan kazandı, bazen de Dede kazandı. Bilgecan Dede her yarışta güldü ve ellerini çırptı. Keloğlan çok mutluydu, çünkü paylaşınca oyun daha güzel olmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst bir şekilde ikiye ayırdı"
   - Cümle 5: «Onları tek tek saydı ve dürüst bir şekilde ikiye ayırdı.»
   - Açıklama: Eşit bölmek için 'dürüst' yanlış kelime; 'eşit' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dürüst bir şekilde ikiye ayırdı"
   - Cümle 5: «Onları tek tek saydı ve dürüst bir şekilde ikiye ayırdı.»
   - Açıklama: 'Dürüst bir şekilde' soyut bir ifade ve burada 'eşit' anlamında yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0099` birebir aynı, ardından `@onarim: 5e8c7a51b44e0fcc31f350e2380d1ca6fc08094d`, sonra gövde.

### Hikâye 2: tohum keloglan-0102 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0102
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'reçel', fiil 'vedalaşmak', sıfat 'dürüst'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: tepede rüzgarla garip bir ıslık sesi geldi | sesi dikkatle dinledi ve boş kavanozu buldu
@tohum: keloglan-0102
@degisim: vedalaşmak -> dinlemek
Keloğlan ile anası tepede reçelli ekmek yiyordu. Birden rüzgarla birlikte ince bir ıslık sesi geldi. Keloğlan bu sesi çok merak etti. "Bu ses nereden geliyor, Keloğlan?" diye sordu anası. Keloğlan dürüst bir cevap verdi. "Bilmiyorum, anneciğim, ama bulacağım," dedi Keloğlan. Önce taşların arkasına baktı ama hiçbir şey göremedi. Sonra gözlerini kapadı ve sesi dikkatle dinledi. Ses çok yakından, yanlarındaki taşın üstünden geliyordu. Orada az önce bitirdikleri reçelin boş kavanozu duruyordu. Rüzgar kavanozun ağzından esti ve yine ıslık sesi geldi. Keloğlan güldü ve kavanozu anasına gösterdi. "Anneciğim, sesi buldum, ses bu boş kavanozdan geliyor!" dedi Keloğlan sevinçle.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir cevap verdi"
   - Cümle 5: «Keloğlan dürüst bir cevap verdi.»
   - Açıklama: Tohumdaki dürüstlük sorunu çözmede işe yaramıyor, çözüm merak ve dikkatli dinlemeyle geliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Rüzgar kavanozun ağzından esti"
   - Cümle 11: «Rüzgar kavanozun ağzından esti ve yine ıslık sesi geldi.»
   - Açıklama: Rüzgar kavanozun ağzından değil ağzının üstünden eser; fiil yeri yanlış anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0102` birebir aynı, `@degisim: vedalaşmak -> dinlemek` (tutuyorsan), ardından `@onarim: 896b4ab6e5b91dae2932a246b6022b5087f0c04f`, sonra gövde.

### Hikâye 3: tohum keloglan-0103 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Bilgecan Dede
@tohum: keloglan-0103
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'lale', fiil 'zıplamak', sıfat 'mor'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | Bilgecan Dede
@plan: hediye edilecek mor lale karanlık köşede kapalı kalmıştı | dededen öğrenip saksıyı güneşli pencereye taşıdı
@tohum: keloglan-0103
Bir sabah Bilgecan Dede, Keloğlan'a bir oyuncak yapıp evine getirdi. Keloğlan da ona mor bir lale vermek istedi. Ama saksıdaki lale kapalıydı, çünkü karanlık bir köşede duruyordu. "Dede, laleler neden kapalı kalır?" diye sordu Keloğlan. "Laleler güneşi sever, ışıkta açılır," dedi Bilgecan Dede. Keloğlan bunu öğrenince saksıyı güneşli pencerenin önüne taşıdı. Biraz bekledi ve lale yavaş yavaş açıldı. Keloğlan sevinçle yerinde zıpladı. Sonra saksıyı Dede'ye uzattı. "Bu mor lale senin için, Dede!" dedi Keloğlan. "Çok teşekkür ederim, Keloğlan, bu çok güzel bir sürpriz!" dedi Bilgecan Dede.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bir oyuncak yapıp evine getirdi"
   - Cümle 1: «Bir sabah Bilgecan Dede, Keloğlan'a bir oyuncak yapıp evine getirdi.»
   - Açıklama: 'Evine' kelimesinin Dede'nin mi Keloğlan'ın mı evini gösterdiği belli değil.
   - Açıklama: 'evine' kimin evini gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0103` birebir aynı, ardından `@onarim: 1e02d210433b3dfef82855310a81458f28bca5e8`, sonra gövde.

### Hikâye 4: tohum keloglan-0104 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0104
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'anahtar', fiil 'acıkmak', sıfat 'uslu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: ikisi de anahtarı saklamak istedi ve oyun durdu | doğruyu söyledi ve sırayı arkadaşına verdi
@tohum: keloglan-0104
@degisim: acıkmak -> saymak
Tepede serin bir rüzgar esiyordu. Keloğlan ile Balkız eski bir anahtarla saklama oyunu oynuyordu. Ama ikisi de anahtarı saklamak istedi ve oyun durdu. Keloğlan biraz düşündü. Az önce anahtarı kendisi saklamıştı. Keloğlan dürüst davrandı ve anahtarı Balkız'a verdi. "Az önce ben sakladım, şimdi sıra sende, Balkız," dedi Keloğlan. Balkız gülümsedi ve anahtarı bir taşın altına koydu. Keloğlan gözlerini kapadı, uslu durdu ve ona kadar saydı. Sonra taşların altına tek tek baktı ve anahtarı buldu. "Şimdi sıra sende, Keloğlan," dedi Balkız. İkisi de çok sevindi, çünkü sırayla oynayınca oyun yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Az önce ben sakladım"
   - Cümle 7: «"Az önce ben sakladım, şimdi sıra sende, Balkız," dedi Keloğlan.»
   - Açıklama: Beşinci cümlede anlatılan bilgi replikte gereksizce aynen tekrarlanıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Balkız gülümsedi ve anahtarı bir taşın altına koydu"
   - Cümle 8: «Balkız gülümsedi ve anahtarı bir taşın altına koydu.»
   - Açıklama: Balkız anahtarı Keloğlan gözlerini kapamadan saklıyor, yani Keloğlan saklanan yeri görmüş olmalı; olay sırası saklama oyunuyla çelişiyor.
   - Açıklama: Balkız anahtarı Keloğlan gözlerini kapamadan saklıyor, yani saklama oyunu mantıksız işliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0104` birebir aynı, `@degisim: acıkmak -> saymak` (tutuyorsan), ardından `@onarim: 54465b99a3f7d7d7837a5d87612de33544614c7a`, sonra gövde.

### Hikâye 5: tohum keloglan-0105 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0105
- yer: dağ (Köyün yakınındaki tepe.)
- tema: kaybolan eşya
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'damga', fiil 'inmek', sıfat 'peynirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: rüzgar esti ve torba yokuştan aşağı yuvarlandı | bir taş yuvarlayıp peşinden indi ve torbayı buldu
@tohum: keloglan-0105
@degisim: damga -> torba
Dağda güneşli bir gündü. Keloğlan peynirli ekmeğinin olduğu torbayı bir kayanın yanına koydu. Birden sert bir rüzgar esti ve torba yokuştan aşağı yuvarlandı. Keloğlan etrafa baktı ama torbayı göremedi. Torbanın nereye gittiğini öğrenmek istedi. Yerden yuvarlak bir taş aldı ve kayanın yanından bıraktı. Taş da yuvarlandı ve büyük bir çalının dibinde durdu. Keloğlan taşın peşinden yavaş yavaş indi. Çalının arkasına baktı ve torbasını orada buldu. Keloğlan çalının yanına oturdu ve peynirli ekmeğini mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sert bir rüzgar esti ve torba yokuştan aşağı yuvarlandı"
   - Cümle 3: «Birden sert bir rüzgar esti ve torba yokuştan aşağı yuvarlandı.»
   - Açıklama: İçinde ekmek olan bir torbanın rüzgarla yokuştan yuvarlanması ve Keloğlan'ın onu gözden kaçırması akla pek yatkın değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "torba yokuştan aşağı yuvarlandı"
   - Cümle 3: «Birden sert bir rüzgar esti ve torba yokuştan aşağı yuvarlandı.»
   - Açıklama: Rüzgarın içinde ekmek olan bir torbayı yokuştan yuvarlaması akla pek yatkın değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Torbanın nereye gittiğini öğrenmek istedi"
   - Cümle 5: «Torbanın nereye gittiğini öğrenmek istedi.»
   - Açıklama: Kartın 'yeni şeyler öğrenmeyi sever' özelliği yalnız 'bulmak' anlamında bir fiil olarak geçiyor, işe yarar biçimde kullanılmıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Yerden yuvarlak bir taş aldı ve kayanın yanından bıraktı"
   - Cümle 6: «Yerden yuvarlak bir taş aldı ve kayanın yanından bıraktı.»
   - Açıklama: Yokuştan aşağı taş yuvarlamak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Yokuştan aşağı taş yuvarlamak çocuğun taklit edince başkasını yaralayabileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0105` birebir aynı, `@degisim: damga -> torba` (tutuyorsan), ardından `@onarim: ac0d207696b10dd7862e4cb37e1bd2b4afdda127`, sonra gövde.

### Hikâye 6: tohum keloglan-0106 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0106
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'biber', fiil 'üzülmek', sıfat 'bozuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: yol bozuktu ve top ağaçların arasında kayboldu | düşen bir biberin peşinden gidip topu buldu
@tohum: keloglan-0106
Bir sabah Keloğlan ormanda bir sepet biber taşıyordu. Kırmızı topunu da sepetin üstüne koymuştu. Yol çok bozuktu ve top zıplayıp büyük ağaçların arasında kayboldu. Keloğlan çok üzüldü ve topu aramaya başladı. Ama topu hiçbir yerde göremedi. Keloğlan biraz sakardı ve eğilince sepeti elinden düşürdü. Biberler yere döküldü. Bir biber yuvarlandı ve büyük bir ağacın köküne kadar gitti. Keloğlan biberi almak için ağaca yürüdü. Kökün arkasında kırmızı topunu gördü. Topu ve bütün biberleri sepete geri koydu. Keloğlan çok sevindi, çünkü kırmızı topunu yine bulmuştu.
```

**Hakem bulguları (5):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "eğilince sepeti elinden düşürdü"
   - Cümle 6: «Keloğlan biraz sakardı ve eğilince sepeti elinden düşürdü.»
   - Açıklama: Topu Keloğlan'ın bir çabası değil, sakarlıkla düşen biberin tesadüfü buluyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "eğilince sepeti elinden düşürdü"
   - Cümle 6: «Keloğlan biraz sakardı ve eğilince sepeti elinden düşürdü.»
   - Açıklama: Çözüm kaybolma sebebine yönelmiyor, bir kaza sonucu kendiliğinden geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve eğilince sepeti elinden düşürdü"
   - Cümle 6: «Keloğlan biraz sakardı ve eğilince sepeti elinden düşürdü.»
   - Açıklama: Çözüm sebepsiz bir sakarlıkla tesadüfen getiriliyor.
   - Açıklama: Sepetin düşmesi olaylardan çıkmıyor ve çözümü sebepsizce getiriyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bir biber yuvarlandı ve büyük bir ağacın köküne kadar gitti"
   - Cümle 8: «Bir biber yuvarlandı ve büyük bir ağacın köküne kadar gitti.»
   - Açıklama: Topu Keloğlan'ın çabası değil tesadüfen yuvarlanan bir biber buluyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bir biber yuvarlandı ve büyük bir ağacın köküne kadar gitti"
   - Cümle 8: «Bir biber yuvarlandı ve büyük bir ağacın köküne kadar gitti.»
   - Açıklama: Çözüm sorunun sebebine yönelmiyor; top rastlantıyla bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0106` birebir aynı, ardından `@onarim: a39936092d7e666112ddfbbdb904101efcc3792e`, sonra gövde.

### Hikâye 7: tohum keloglan-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0108
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'boru', fiil 'sulamak', sıfat 'düzgün'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: kovayı alırken suyu eşeğin sırtına döktü | eşeğinden özür diledi ve ıslak sırtını sildi
@tohum: keloglan-0108
@degisim: boru -> kova
Bir sabah Keloğlan ile eşeği Karakaçan ormanda fidan suluyordu. Karakaçan sırtında iki kova su taşıyordu. Keloğlan bir kovayı alırken sakarlık etti ve su eşeğin sırtına döküldü. Karakaçan başını öbür yana çevirdi. Keloğlan hemen onun yanına gitti. "Özür dilerim, Karakaçan, suyu sana dökmek istemedim," dedi Keloğlan. Sonra onun ıslak sırtını eliyle sildi. Karakaçan başını salladı ve Keloğlan'a yaklaştı. Keloğlan öbür kovayı bu kez iki eliyle düzgün tuttu. İkisi ağaçların altındaki bütün fidanları mutlu mutlu suladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "alırken sakarlık etti ve"
   - Cümle 3: «Keloğlan bir kovayı alırken sakarlık etti ve su eşeğin sırtına döküldü.»
   - Açıklama: 'Sakarlık etmek' soyut bir kalıp; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Keloğlan hemen onun yanına gitti"
   - Cümle 5: «Keloğlan hemen onun yanına gitti.»
   - Açıklama: Keloğlan kovayı eşeğin sırtından alırken zaten yanındaydı, sonra yanına gitmesi çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0108` birebir aynı, `@degisim: boru -> kova` (tutuyorsan), ardından `@onarim: 8da8d57c6d8b254176328681067f32ba84932bbf`, sonra gövde.
