# Editör görevi (onarım): Doru, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Doru | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar41.txt --ad urun_v2`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Onarılacak hikâyeler

### Hikâye 1: tohum doru-0148 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0148
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'karnabahar', fiil 'savrulmak', sıfat 'tüylü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: en küçük at uçan tohumlara yetişemedi çünkü boyu kısaydı | çiçeği salladı ve tohumlar alçaktan uçtu
@tohum: doru-0148
@degisim: karnabahar -> çiçek
Dağda Doru ile Alaca tüylü çiçeklerin yanında oynuyordu. Rüzgarda savrulan tohumları burunlarıyla yakalamaya çalışıyorlardı. Ama Alaca çok küçüktü ve uçan tohumlara boyu yetmiyordu. Doru üç tohum tuttu, Alaca ise hiç tutamadı. Alaca üzüldü ve oyunu bırakmak istedi. Doru ona yardım etmek için en büyük çiçeğin yanına gitti. Başını eğdi ve çiçeği yavaşça salladı. Tohumlar bu kez alçaktan, tam Alaca'nın önünden uçtu. Alaca zıpladı ve bir tohumu burnuyla yakaladı. Sonra bir tane daha tuttu ve sevinçle güldü. Doru bundan sonra oyunlarda tohumları Alaca için hep aşağıdan uçururdu.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hep aşağıdan uçururdu"
   - Cümle 11: «Doru bundan sonra oyunlarda tohumları Alaca için hep aşağıdan uçururdu.»
   - Açıklama: Anlatım -dı'lı geçmişten geniş zamanın hikayesine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0148` birebir aynı, `@degisim: karnabahar -> çiçek` (tutuyorsan), ardından `@onarim: 5a22b44c7c9db9a85b90f508f8e0f5c07ad0f3b5`, sonra gövde.

### Hikâye 2: tohum doru-0150 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0150
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'ağaç', fiil 'dalgalanmak', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: kuru bir dal ufak bir ağacın üstüne düşmüştü | dalı dişleriyle çekti ve ağacı kurtardı
@tohum: doru-0150
Doru ormanda yürüyordu ve rüzgarda yapraklar dalgalanıyordu. Birden Doru ufak bir ağaç gördü. Büyük ve kuru bir dal onun üstüne düşmüştü. Ufak ağacın ince gövdesi dalın altında yere eğilmişti. Doru ağaca hemen yardım etmek istedi. Önce dalın ucunu dişleriyle sıkıca tuttu. Sonra geri geri yürüdü ve dalı yavaşça çekti. Kuru dal ağacın üstünden kaydı ve yere düştü. Ufak ağaç yeniden doğruldu. Şimdi onun yaprakları da rüzgarda sallanıyordu. Doru ağaca baktı ve çok sevindi. Sonra ağacın yanındaki taze çimenleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "rüzgarda yapraklar dalgalanıyordu"
   - Cümle 1: «Doru ormanda yürüyordu ve rüzgarda yapraklar dalgalanıyordu.»
   - Açıklama: Yapraklar dalgalanmaz, sallanır; fiil öznesine uymuyor.
   - Açıklama: Yapraklar dalgalanmaz; 'sallanıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0150` birebir aynı, ardından `@onarim: 97c0be6aeb0733b6f5d0a073322d4c4529fb4057`, sonra gövde.

### Hikâye 3: tohum doru-0151 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0151
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'basamak', fiil 'tutunmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: yağmur başladı ve yelesi ıslandı | hızla koşup sık dalların altına girdi
@tohum: doru-0151
@degisim: basamak -> damla
Doru ormanın kenarındaki açıklıkta çimen yiyordu. Birden kara bulutlar geldi ve yağmur yağmaya başladı. Doru'nun yelesi hemen ıslandı. Kuru kalmak için büyük ağaçların altına gitmeliydi. Ama ağaçlar biraz uzaktaydı. Doru açık ve düz çimenlerin üstünde hızla koştu. Kısa sürede ağaçların altına vardı. Orada dallar sık ve karışıktı. Dallara yeşil bir sarmaşık tutunuyordu. Damlalar bu dalların arasından aşağı inemiyordu. Doru başını iki kez salladı ve yelesi biraz kurudu. Sonra kuru yerde yağmurun sesini mutlu mutlu dinledi. Doru bundan sonra yağmur başlayınca hemen sık dalların altına koştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dallara yeşil bir sarmaşık tutunuyordu"
   - Cümle 9: «Dallara yeşil bir sarmaşık tutunuyordu.»
   - Açıklama: Sarmaşık işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
   - Açıklama: Sarmaşık kuruluyor ama olayda hiçbir işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yağmur başlayınca hemen sık dalların altına koştu"
   - Cümle 13: «Doru bundan sonra yağmur başlayınca hemen sık dalların altına koştu.»
   - Açıklama: Kara bulutlu yağmurda ağaç altına sığınmak örnek bir davranış olarak veriliyor; fırtınada taklit edilince tehlikeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0151` birebir aynı, `@degisim: basamak -> damla` (tutuyorsan), ardından `@onarim: 69b0fbdb37c5e18eaa67f27936b18c8fe6a9a442`, sonra gövde.

### Hikâye 4: tohum doru-0152 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0152
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bağcık', fiil 'tamamlamak', sıfat 'kaygan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: susamıştı ve uzaktan bir su sesi geldi | hızla koşup sesi buldu ve kütüğün içindeki suyu içti
@tohum: doru-0152
@degisim: bağcık -> kütük
Doru annesiyle dağda çimen yiyordu. Çok susamıştı, ama yakında su yoktu. Birden uzaktan "şıp, şıp" diye bir ses geldi. Doru bu sesi çok merak etti. "Anne, bu bir su sesi mi?" diye sordu Doru. "Olabilir, git bak," dedi annesi. Doru açık ve düz çimenlerde hızla koştu. Sesin geldiği yerde yüksek bir kayadan su damlıyordu. Damlalar eski bir kütüğün içine düşüyordu. Kütüğün içi serin suyla dolmuştu. Yanındaki taşlar ıslak ve kaygandı. Doru onlara basmadı ve çimenin üstünden suyu içti. Annesi de yemeğini tamamladı ve Doru'nun yanına geldi. Doru çok sevindi, çünkü hem sesi hem de suyu bulmuştu.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: ""Olabilir, git bak," dedi annesi"
   - Cümle 6: «"Olabilir, git bak," dedi annesi.»
   - Açıklama: Anne yavrusunu bilinmeyen bir sesin peşine tek başına gönderiyor; çocuk bunu ebeveynden uzaklaşma olarak taklit edebilir.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yanındaki taşlar ıslak"
   - Cümle 11: «Yanındaki taşlar ıslak ve kaygandı.»
   - Açıklama: 'Yanındaki' ifadesinin kütüğü mü Doru'yu mu gösterdiği belli değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanındaki taşlar ıslak ve kaygandı"
   - Cümle 11: «Yanındaki taşlar ıslak ve kaygandı.»
   - Açıklama: Kaygan taşlar bir tehlike gibi kuruluyor ama olayda hiçbir işlev görmüyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çimenin üstünden suyu içti"
   - Cümle 12: «Doru onlara basmadı ve çimenin üstünden suyu içti.»
   - Açıklama: Eski bir kütükte birikmiş suyu içmek çocuğun taklit edebileceği güvensiz bir davranış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çimenin üstünden suyu içti"
   - Cümle 12: «Doru onlara basmadı ve çimenin üstünden suyu içti.»
   - Açıklama: Su çimenin üstünden içilmez; 'çimenin üstünde durup kütükten içti' anlamı bozuk kurulmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0152` birebir aynı, `@degisim: bağcık -> kütük` (tutuyorsan), ardından `@onarim: c2d8741b35bb2d8e377a1054cdfd55c89c3ebf46`, sonra gövde.

### Hikâye 5: tohum doru-0154 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0154
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fide', fiil 'köpürmek', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: yola kalın bir dal düşmüştü ve küçük at geçemedi | dalı iterek yolun kenarına yuvarladı
@tohum: doru-0154
@degisim: fide -> dal
Doru Alaca'ya dağda güzel bir su göstermek istiyordu. Bu, Alaca için küçük bir sürpriz olacaktı. Ama yola kalın bir dal düşmüştü ve Alaca onun üstünden geçemedi. "Doru, bu dal benim için çok yüksek," dedi Alaca. Doru ona yardım etmek için dalı burnuyla itti. Dal yolun kenarına yuvarlandı. Alaca kolayca geçti. Az sonra ikisi suyun yanına vardı. Su taşların arasında beyaz beyaz köpürüyordu. "Sürpriz, Alaca!" dedi Doru sevecen bir sesle. "Çok güzel, teşekkürler, Doru!" dedi Alaca. Alaca sevinçle zıpladı. Doru çok mutlu oldu, çünkü sürprizi Alaca'yı sevindirmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Doru sevecen bir sesle"
   - Cümle 10: «"Sürpriz, Alaca!" dedi Doru sevecen bir sesle.»
   - Açıklama: 'Sevecen' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Sevecen' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0154` birebir aynı, `@degisim: fide -> dal` (tutuyorsan), ardından `@onarim: 80306473d7fa21e1a2efd56599d864af71a7f690`, sonra gövde.

### Hikâye 6: tohum doru-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0156
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'sis', fiil 'konmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sisin içinde küçük renkli şeyler kıpırdıyordu | cesaretle çalıya yaklaştı ve kelebekleri gördü
@tohum: doru-0156
Ormanda sabah sisi vardı ve ağaçlar zor görünüyordu. Doru biraz ileride, bir çalının üstünde küçük renkli şeyler gördü. Renkli şeyler kıpırdıyordu, ama sis yüzünden ne olduklarını anlayamadı. Doru önce yerinde durdu. Sonra cesaretle çalıya doğru birkaç adım attı. Çalı sarı çiçeklerle doluydu. Beyaz ve mavi oynak kelebekler çiçeklere konuyor ve yeniden uçuyordu. Sisin içinde gördüğü renkli şeyler bu kelebeklerdi. Doru çalının yanında durdu ve onları uzun uzun izledi. Doru çok mutlu oldu, çünkü renkli şeylerin ne olduğunu bulmuştu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Renkli şeyler kıpırdıyordu, ama sis yüzünden ne olduklarını anlayamadı"
   - Cümle 3: «Renkli şeyler kıpırdıyordu, ama sis yüzünden ne olduklarını anlayamadı.»
   - Açıklama: İkinci yan cümlenin öznesi Doru olmalı ama cümlede özne 'renkli şeyler' olarak kalıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ama sis yüzünden ne olduklarını anlayamadı"
   - Cümle 3: «Renkli şeyler kıpırdıyordu, ama sis yüzünden ne olduklarını anlayamadı.»
   - Açıklama: 'anlayamadı' fiilinin öznesi cümlede 'renkli şeyler' gibi duruyor; Doru adı geçmediği için özne belirsiz.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "renkli şeylerin ne olduğunu"
   - Cümle 10: «Doru çok mutlu oldu, çünkü renkli şeylerin ne olduğunu bulmuştu.»
   - Açıklama: 'Renkli şeyler' ifadesi kısa hikayede beş kez gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0156` birebir aynı, ardından `@onarim: e54f10e29b977bb4fe4c4c72576c7e5a80d88d44`, sonra gövde.

### Hikâye 7: tohum doru-0157 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0157
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kaya', fiil 'uyumak', sıfat 'sakin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: kelebekler uçabilirdi ve annesi uzakta uyuyordu | hızla koşup annesini uyandırdı ve kelebekleri gösterdi
@tohum: doru-0157
Bir sabah yağmur yeni dinmişti ve dağ çok sakindi. Doru büyük bir kayanın yanında çimen yiyordu. Birden kayanın üstüne mavi kelebekler kondu. Doru onları annesine göstermek istedi, ama kelebekler her an uçabilirdi. Annesi biraz uzakta, çimenlerin üstünde uyuyordu. Doru açık ve düz çimenlerde hızla koştu. "Anne, uyan, kayada mavi kelebekler var!" dedi Doru. Annesi gözlerini açtı ve Doru'yla kayaya yürüdü. Kelebekler daha oradaydı. "Ne güzel, Doru!" dedi annesi. Sonra ikisi yan yana durdu ve onları mutlu mutlu izledi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kelebekler uçabilirdi ve annesi"
   - Cümle 0 (plan satırı): «kelebekler uçabilirdi ve annesi uzakta uyuyordu | hızla koşup annesini uyandırdı ve kelebekleri gösterdi»
   - Açıklama: Plan satırında 'uçabilirdi' uçup gitme anlamını vermiyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Birden kayanın üstüne mavi kelebekler kondu"
   - Cümle 3: «Birden kayanın üstüne mavi kelebekler kondu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, konarak sorunu başlatıp olaya katılıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "üstüne mavi kelebekler kondu"
   - Cümle 3: «Birden kayanın üstüne mavi kelebekler kondu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun merkezinde olaya katılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kelebekler her an uçabilirdi"
   - Cümle 4: «Doru onları annesine göstermek istedi, ama kelebekler her an uçabilirdi.»
   - Açıklama: 'Uçabilirdi' kaçıp gitme anlamında yanlış; 'uçup gidebilirdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0157` birebir aynı, ardından `@onarim: 5f04ec02290668345e4980a6b664cbf9843974c2`, sonra gövde.

### Hikâye 8: tohum doru-0161 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0161
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: bir şey yapmak
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'sebze', fiil 'okşamak', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: yakındaki yapraklar ıslak ve yapışkandı | alçak ağacın üstünden atlayıp kuru yaprak buldu
@tohum: doru-0161
@degisim: sebze -> yaprak
Bir sabah Doru ormanda büyük bir yaprak yığını yapmak istedi. Doru yaprakların içinde yuvarlanmayı çok severdi. Ama yağmur yeni dinmişti ve yakındaki yapraklar ıslaktı. Islak yapraklar yapışkandı ve Doru'nun tüylerine yapışıyordu. Kuru yapraklar yere düşmüş alçak bir ağacın arkasındaydı. Doru daha önce hiçbir ağacın üstünden atlamamıştı. Ama Doru cesurdu. Biraz geri gitti, koştu ve alçak ağacın üstünden atladı. Orada bir sürü kuru ve sarı yaprak vardı. Doru yaprakları ayaklarıyla bir yere topladı ve büyük bir yığın yaptı. Yığını burnuyla okşadı; yapraklar çok yumuşaktı. Sonra Doru yığının içinde mutlu mutlu yuvarlandı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kuru yapraklar yere düşmüş alçak bir ağacın arkasındaydı"
   - Cümle 5: «Kuru yapraklar yere düşmüş alçak bir ağacın arkasındaydı.»
   - Açıklama: Yağmur yeni dinmişken devrik ağacın arkasındaki yaprakların kuru olması hikayenin kendi kurduğu durumla çelişiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "koştu ve alçak ağacın üstünden atladı"
   - Cümle 8: «Biraz geri gitti, koştu ve alçak ağacın üstünden atladı.»
   - Açıklama: Güvenli özellik kullanımı satırı yalnız açık ve düz yerde koşmayı izin veriyor; engelin üstünden atlamak taklit edilince tehlikeli.
   - Açıklama: Cesaret, daha önce hiç denenmemiş bir engelin üstünden atlamak olarak gösteriliyor; güvenli kullanım satırı hızı yalnız açık ve düz yerde koşarken gösterir ve bu davranış taklit edilince tehlikelidir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0161` birebir aynı, `@degisim: sebze -> yaprak` (tutuyorsan), ardından `@onarim: 9aac364cd29137da213dc7267bbbcf043ea597b4`, sonra gövde.

### Hikâye 9: tohum doru-0162 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0162
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çiçek', fiil 'eğmek', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: acıkmıştı ama tozlu yolda hiç çimen yoktu | kokuya doğru hızla koşup çiçekli bir açıklık buldu
@tohum: doru-0162
Rüzgar hafif hafif esiyordu. Doru ormanın tozlu yolunda yürüyordu ve çok acıkmıştı. Ama yolda hiç taze çimen yoktu. Birden rüzgar güzel bir koku getirdi. Doru bu kokunun nereden geldiğini çok merak etti. Yol düz ve açıktı. Doru hızla koştu ve kokunun geldiği yere vardı. Orada ağaçların arasında küçük bir açıklık vardı. Açıklık sarı ve beyaz çiçeklerle doluydu. Koku bu çiçeklerden geliyordu. Çiçeklerin arasında taze çimenler de vardı. Doru başını eğdi ve çimenleri yedi. Sonra karnı doydu ve çiçeklerin yanında mutlu mutlu dinlendi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden rüzgar güzel bir koku getirdi"
   - Cümle 4: «Birden rüzgar güzel bir koku getirdi.»
   - Açıklama: Çözüm Doru'nun bir fikrinden değil rüzgarın tesadüfen getirdiği kokudan geliyor ve çimen de şans eseri çiçeklerin arasında çıkıyor.
   - Açıklama: Çözüm şans eseri gelen bir çiçek kokusuyla sebepsizce geliyor; çimen bulunması kokudan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0162` birebir aynı, ardından `@onarim: e3e173355639dd7d972e797842be25b0dffbcaa4`, sonra gövde.

### Hikâye 10: tohum doru-0163 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0163
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'nilüfer', fiil 'ışıldamak', sıfat 'çevik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: yanlışlıkla arkadaşının bulduğu papatyayı yedi | cesaretle onun yanına gidip özür diledi
@tohum: doru-0163
@degisim: nilüfer -> papatya
Doru ile Alaca ormanın güneşli bir yerinde oynuyordu. Alaca güneşte ışıldayan beyaz bir papatya buldu. Ama Doru bakmadan papatyayı çimenle birlikte yedi. Alaca çok üzüldü. Çevik Alaca hemen yakındaki büyük bir ağacın altına koştu. Doru o zaman papatyayı yediğini anladı. Biraz utandı ama cesaretle Alaca'nın yanına gitti. Doru başını eğdi ve Alaca'dan özür diledi. Alaca başını Doru'nun boynuna dayadı. Sonra ikisi birlikte güneşli yere döndü. Orada yeni papatyalar buldular. Doru ile Alaca papatyaların yanında mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güneşte ışıldayan beyaz"
   - Cümle 2: «Alaca güneşte ışıldayan beyaz bir papatya buldu.»
   - Açıklama: 'Işıldayan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çevik Alaca hemen yakındaki"
   - Cümle 5: «Çevik Alaca hemen yakındaki büyük bir ağacın altına koştu.»
   - Açıklama: 'Çevik' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime ve burada gereksiz bir sıfat.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Çevik Alaca hemen yakındaki"
   - Cümle 5: «Çevik Alaca hemen yakındaki büyük bir ağacın altına koştu.»
   - Açıklama: Kartın Alaca için yanlar ilişkisinde çeviklik diye bir özellik yok; karta dayanmayan bilgi ekleniyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çevik Alaca hemen yakındaki büyük bir ağacın altına koştu"
   - Cümle 5: «Çevik Alaca hemen yakındaki büyük bir ağacın altına koştu.»
   - Açıklama: Alaca'nın ağacın altına koşması sebepsiz ve olayda hiçbir işe yaramıyor.
   - Açıklama: Alaca'nın ağacın altına koşması Doru'nun papatyayı yediğini anlamasına sebep olmuyor; olaylar birbirinden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0163` birebir aynı, `@degisim: nilüfer -> papatya` (tutuyorsan), ardından `@onarim: dfbb0877ceaedae9a646953850e86f7684c1c0ee`, sonra gövde.

### Hikâye 11: tohum doru-0164 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0164
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kar', fiil 'şaşırtmak', sıfat 'faydalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kar yağmıştı ve çimenleri kapatmıştı | ayaklarıyla karı itip çimenleri açtı
@tohum: doru-0164
@degisim: faydalı -> bembeyaz
Parkın her tarafı bembeyazdı. Sabah yağan kar Doru'yu çok şaşırttı. Ama kar bütün çimenleri kapatmıştı ve yiyecek bir şey görünmüyordu. Doru sürüdeki atlara yardım etmek istedi. Ön ayaklarıyla karı iki yana itti. Karın altından yeşil çimenler çıktı. Doru biraz ileri yürüdü ve karı yine itti. Sonra bir yer daha açtı. Az sonra parkta geniş, yeşil bir yer oldu. Artık yemek için bol bol çimen vardı. Doru çok sevindi, çünkü herkese yetecek kadar çimen açmıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru sürüdeki atlara yardım etmek istedi"
   - Cümle 4: «Doru sürüdeki atlara yardım etmek istedi.»
   - Açıklama: Sürüdeki atlar sebepsiz beliriyor ve hikayede hiç görünmüyor.
   - Açıklama: Sürü ve atlar daha önce hiç kurulmadan sebepsiz beliriyor ve hikayede bir daha görünmüyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "herkese yetecek kadar çimen açmıştı"
   - Cümle 11: «Doru çok sevindi, çünkü herkese yetecek kadar çimen açmıştı.»
   - Açıklama: 'Çimen açmak' yanlış anlamda; çimen açılmaz, karın altından çıkarılır (plandaki 'çimenleri açtı' da aynı sorunu taşır).
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "herkese yetecek kadar çimen açmıştı"
   - Cümle 11: «Doru çok sevindi, çünkü herkese yetecek kadar çimen açmıştı.»
   - Açıklama: Hedef sürüye yardım etmek ama atlar hiç gelmiyor ve çimeni yedikleri görülmüyor, hedefe ulaşıldığı gösterilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0164` birebir aynı, `@degisim: faydalı -> bembeyaz` (tutuyorsan), ardından `@onarim: 466c832830ac51c574897d36dcee0c3004974d0e`, sonra gövde.

### Hikâye 12: tohum doru-0165 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0165
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'leke', fiil 'beğenmek', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: kozalak yoldan çıktı ve çalılara doğru yuvarlandı | düz yolda hızla koşup kozalağı durdurdu
@tohum: doru-0165
@degisim: leke -> kozalak
Doru ile Kırat ormanda kozalak oyunu oynuyordu. Kozalağı sırayla burunlarıyla itiyorlardı. Sıra Kırat'a geldi. Kırat biraz uykuluydu ve kozalağa bakmadan itti. Kozalak yoldan çıktı ve sık çalılara doğru yuvarlandı. Çalıların arasında onu bir daha bulamazlardı. Doru hemen düz yolda hızla koştu. Kozalağı çalıların hemen önünde yakaladı ve ayağıyla durdurdu. Sonra onu burnuyla Kırat'a geri itti. Kırat bu kez kozalağı yavaşça itti. Kırat oyunu çok beğendi ve başını salladı. İkisi sırayla oynamaya devam etti. Doru çok sevindi, çünkü kozalak kaybolmamıştı ve oyunları sürüyordu.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Sıra Kırat'a geldi.»
   - Açıklama: İlk üç cümlede sorun yok; kozalak ancak 5. cümlede yoldan çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0165` birebir aynı, `@degisim: leke -> kozalak` (tutuyorsan), ardından `@onarim: 0b8574993db935ad6770c4a115cfc7d966cb934a`, sonra gövde.
