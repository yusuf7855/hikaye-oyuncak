# Editör görevi (onarım): Hello Kitty, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hello Kitty | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar22.txt --ad urun_v2`
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

## Kart: Hello Kitty (kaynaklı, kapalı dünya)

- Ad: Hello Kitty (okunuş: helo kiti; kesme eki okunuşa uyar)
- Kimlik: Hello Kitty, ailesiyle birlikte bir evde yaşayan, kırmızı kurdeleli, beyaz ve iyi kalpli bir kedidir.
- Tür: kedi
- Güvenli özellik kullanımı: Kurabiye ve turta bir büyükle birlikte yapılır; fırını ve sıcak tepsiyi annesi ya da babası tutar. Kimse yabancıyla bir yere gitmez; kimse tek başına uzağa gitmez.
- Özellikler:
  - arkadaş: Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır. (örnek biçimler: arkadaş, arkadaşlar, arkadaşıyla)
  - kurabiye: Kurabiye yapmayı çok sever. (örnek biçimler: kurabiye, kurabiyeler, kurabiyeleri)
  - turta: En çok elmalı turtayı sever. (örnek biçimler: turta, turtayı, turtası)
- Yerler:
  - park: Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.
  - orman: Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.
  - ev: Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Mimi: Hello Kitty'nin ikiz kız kardeşi ve en iyi arkadaşı; utangaçtır ve sarı kurdele takar. Tür: kedi; konuşur. Yüzey biçimleri: Mimi, kardeş, kardeşi, ikiz, ikizi
  - annesi: Hello Kitty'nin annesi; çok iyi yemek yapar, elmalı turtası çok güzeldir. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
  - babası: Hello Kitty'nin babası; güvenilir ve komiktir, bazen bir şeyi unutur. Tür: baba; konuşur. Yüzey biçimleri: baba, babası, babacığım, Baba
- Dünya kuralları:
  - Hello Kitty, Mimi, annesi ve babası konuşur. Hikayede Hello Kitty'nin ağzından söz edilmez.
  - Mimi, Hello Kitty'nin ikiz kız kardeşidir; ablası ya da kuzeni değildir. Mimi sarı kurdele takar.
  - Hikaye evde, parkta ya da ormanda tek sahnede geçer; Londra'ya ya da başka bir şehre yolculuk yoktur.
  - Hello Kitty bir marka ya da satılan bir eşya olarak anılmaz; mağaza ve alışveriş yoktur.
- Yasak adlar: Dear Daniel, Daniel, Charmmy Kitty, Charmmy, Sugar, Ichigoman, Mimmy, Kitty White, George, Mary, Anthony, Margaret, Joey, Judy, Tippy, Thomas, Tracy, Rorry, My Melody
- Yasak: Marka, mağaza, alışveriş, uçak ya da trenle şehir yolculuğu ve zamanda yolculuk hikayeye girmez.
- İzinli dünya kelimeleri: kurdele, kurabiye, turta, piknik, kamp

## Onarılacak hikâyeler

### Hikâye 1: tohum hello_kitty-0045 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0045
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'lale', fiil 'planlamak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: ince sap büküldü ve hamurdan lale devrildi | kalın bir sap yapıp çiçeği tepsiye dik koydu
@tohum: hello_kitty-0045
@degisim: planlamak -> hatırlamak
Hello Kitty mutfakta oyun hamuruyla oynuyordu. İlk kez hamurdan dik duran bir lale yapmayı denedi. Ama ince sap büküldü ve lale devrildi. Çiçek, yapraklar ve sap birbirine yapıştı ve karmakarışık oldu. Hello Kitty hamura baktı ve biraz düşündü. Kalın kurabiyelerin hep sağlam durduğunu hatırladı. Hamuru yeniden ayırdı. Bu kez kalın bir sap yaptı ve tepsiye dik koydu. Sapın yanına iki yaprak, en üste de kırmızı bir çiçek taktı. Lale tepside güzelce durdu ve hiç düşmedi. Hello Kitty çok sevindi ve bundan sonra hep kalın sap yaptı.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "sap birbirine yapıştı ve karmakarışık oldu"
   - Cümle 4: «Çiçek, yapraklar ve sap birbirine yapıştı ve karmakarışık oldu.»
   - Açıklama: Devrilen laleye ek olarak hamurun karmakarışık olması ikinci bir sorun ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0045` birebir aynı, `@degisim: planlamak -> hatırlamak` (tutuyorsan), ardından `@onarim: 977bd1fa7c4703d0c1f0d572f004e99899f0e956`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0048 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0048
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'tuz', fiil 'dökmek', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: hamur çok suluydu ve yapışıyordu | hamura un ve tuz döktü ve yoğurdu
@tohum: hello_kitty-0048
Evde, kahverengi mutfak masasında Hello Kitty ile annesi tuz hamuru yapıyordu. Hello Kitty hamurdan küçük bir kedi yapmak istedi. Ama hamur çok suluydu ve ellerine yapışıyordu. Hello Kitty arkadaşlarına olduğu gibi annesine de hep kibar davranırdı. "Anne, lütfen biraz un ve tuz alabilir miyim?" diye sordu Hello Kitty. Annesi unu ve tuzu ona uzattı. Hello Kitty hamura bir kaşık un ve biraz tuz döktü. Sonra hamuru güzelce yoğurdu. Hamur artık ellerine yapışmadı. Hello Kitty küçük bir kedi yaptı. Annesi kediyi görünce gülümsedi. Hello Kitty çok sevindi, çünkü kedisi tam istediği gibi olmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına olduğu gibi annesine de hep kibar davranırdı"
   - Cümle 4: «Hello Kitty arkadaşlarına olduğu gibi annesine de hep kibar davranırdı.»
   - Açıklama: Tohumdaki arkadaş özelliği karttaki gibi işe yarar biçimde kullanılmıyor, yalnız bir huy cümlesi olarak sayılıyor ve sorunu çözmüyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarına olduğu gibi annesine"
   - Cümle 4: «Hello Kitty arkadaşlarına olduğu gibi annesine de hep kibar davranırdı.»
   - Açıklama: Tohumdaki arkadaş/iyi davranma özelliği yalnız bir huy cümlesi olarak söyleniyor, sorunun çözümüne (hamura un eklemek) iş görmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0048` birebir aynı, ardından `@onarim: ce51c579b3df90e073abc3cf4dd48fea22b7d969`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0053 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0053
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kavanoz', fiil 'bırakmak', sıfat 'utangaç'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: top kavanoza çarptı ve kavanoz yuvarlandı, kayboldu | yerdeki izin peşinden gidip kavanozu buldu
@tohum: hello_kitty-0053
Hello Kitty ile Mimi parkta top oynuyordu. Hello Kitty evde yaptığı kurabiyelerin kavanozunu örtüye bırakmıştı. Birden Mimi'nin attığı top kavanoza çarptı. Kavanoz yere düştü, yuvarlandı ve çiçeklerin arasında kayboldu. "Kurabiyeler nereye gitti?" diye sordu utangaç Mimi yavaşça. Hello Kitty yere dikkatle baktı. Çimenlerde ince, uzun bir iz vardı. İki kardeş izin peşinden yürüdü. İz, büyük bir çiçeğin arkasında bitti. Kavanoz orada, kapağı kapalı duruyordu. Hello Kitty kavanozu aldı ve içine baktı. Kavanoz da kurabiyeler de sağlamdı. "Bak, Mimi, kurabiyelerimiz burada!" dedi Hello Kitty. İki kardeş çok sevindi, çünkü kurabiyelerini yeniden bulmuşlardı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty evde yaptığı kurabiyelerin kavanozunu"
   - Cümle 2: «Hello Kitty evde yaptığı kurabiyelerin kavanozunu örtüye bırakmıştı.»
   - Açıklama: Kurabiye yapma özelliği yalnız eşya olarak anılıyor; çözüm izi takip etmekten geliyor, özellik işe yaramıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "yuvarlandı ve çiçeklerin arasında kayboldu"
   - Cümle 4: «Kavanoz yere düştü, yuvarlandı ve çiçeklerin arasında kayboldu.»
   - Açıklama: Kavanozun kaybolması sorunu ilk üç cümlede değil, dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0053` birebir aynı, ardından `@onarim: f42bf0200947787c00982366c78add673d389401`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0067 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0067
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'ayna', fiil 'kopmak', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: aynanın ipi koptu ve ayna çimenlere düştü | turtanın üstündeki garip ışığı izleyip aynayı buldu
@tohum: hello_kitty-0067
Parkta ağaçların gölgesi serindi. Hello Kitty çimenlerde en sevdiği elmalı turtayı yiyordu. Birden çantasına bağlı küçük aynanın ipi koptu ve ayna düştü. Hello Kitty üzüldü ve çevresine baktı. Ama aynayı göremedi. Hello Kitty aynanın güneşte parladığını biliyordu. Bu yüzden çimenlerde parlak bir şey aradı. Sonra turtasının üstünde garip, sarı bir ışık gördü. Hello Kitty ışığın geldiği yere baktı. Çimenlerin arasında küçük ayna parlıyordu. Güneş aynadan turtaya yansıyordu. Hello Kitty aynayı aldı ve ipin iki ucunu bağladı. Sonra Hello Kitty turtasını mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük aynanın ipi koptu"
   - Cümle 3: «Birden çantasına bağlı küçük aynanın ipi koptu ve ayna düştü.»
   - Açıklama: İpin neden koptuğu söylenmiyor; sorun sebepsiz başlıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Güneş aynadan turtaya yansıyordu"
   - Cümle 11: «Güneş aynadan turtaya yansıyordu.»
   - Açıklama: Güneş yansımaz, güneşin ışığı yansır; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0067` birebir aynı, ardından `@onarim: 4aed137ca0d96220f889915f36c0b7c26e65c67f`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0069 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0069
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'köfte', fiil 'çizmek', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: çizdiği baş çok büyüktü ve toprağa sığmadı | büyük çizgileri silip daha küçük bir baş çizdi
@tohum: hello_kitty-0069
@degisim: düşünceli -> küçük
Parkta, yolun kenarında yumuşak bir toprak vardı. Hello Kitty bir dalla toprağa komik bir kedi resmi çiziyordu. Ama resimdeki başı çok büyük çizmişti ve toprak yetmedi. Başın yarısı çimenlerin üstünde kaldı ve hiç görünmedi. Hello Kitty toprağa baktı ve biraz düşündü. Sonra büyük çizgileri eliyle sildi. Bu kez daha küçük, yuvarlak bir baş çizdi. Küçük baş toprağa tam sığdı. Hello Kitty resme iki göz ve uzun bıyıklar ekledi. Kedinin burnunu da köfte gibi kocaman ve yuvarlak yaptı. Hello Kitty buna kahkahayla güldü. En sona iki sivri kulak koydu. Hello Kitty çok sevindi, çünkü resmi arkadaşlarını da güldürecekti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "burnunu da köfte gibi kocaman"
   - Cümle 10: «Kedinin burnunu da köfte gibi kocaman ve yuvarlak yaptı.»
   - Açıklama: Benzetme kullanılmış; mecazlı anlatımdan kaçınılmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "resmi arkadaşlarını da güldürecekti"
   - Cümle 13: «Hello Kitty çok sevindi, çünkü resmi arkadaşlarını da güldürecekti.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız sonda anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son cümlede anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0069` birebir aynı, `@degisim: düşünceli -> küçük` (tutuyorsan), ardından `@onarim: d07f4ef7b341397c264d755ba0eb7f755e655ad8`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0071 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0071
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: sırayla oynamak
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yonca', fiil 'eğlenmek', sıfat 'sadık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: iki kardeş boş sepeti aynı anda istedi | sırayla oynamayı önerdi ve sırayla yonca buldular
@tohum: hello_kitty-0071
@degisim: sadık -> boş
Rüzgar ağaçların arasında yavaşça esiyordu. Hello Kitty ve Mimi kamp yerinde elmalı turtayı bitirdi. İkisi yonca toplamak için boş sepeti aynı anda istedi ve oyun durdu. Hello Kitty biraz düşündü. "Mimi, sırayla oynayalım, önce sen bul," dedi Hello Kitty. Mimi çimenlere baktı ve küçük bir yonca buldu. Onu sepete koydu ve sepeti Hello Kitty'ye uzattı. Sonra Hello Kitty de yeşil bir yonca buldu. "Şimdi sıra yine sende, Mimi," dedi Hello Kitty. Sepet yavaş yavaş yeşil yapraklarla doldu. İkisi gülerek eğlendi. İki kardeş çok sevindi, çünkü sırayla oynayınca ikisi de yonca bulmuştu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ve Mimi kamp yerinde"
   - Cümle 2: «Hello Kitty ve Mimi kamp yerinde elmalı turtayı bitirdi.»
   - Açıklama: İki küçük kardeş ormandaki kamp yerinde büyük olmadan yalnız; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kamp yerinde elmalı turtayı bitirdi"
   - Cümle 2: «Hello Kitty ve Mimi kamp yerinde elmalı turtayı bitirdi.»
   - Açıklama: Tohumdaki turta özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki turta özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kamp yerinde elmalı turtayı bitirdi"
   - Cümle 2: «Hello Kitty ve Mimi kamp yerinde elmalı turtayı bitirdi.»
   - Açıklama: Elmalı turta olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Turta olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0071` birebir aynı, `@degisim: sadık -> boş` (tutuyorsan), ardından `@onarim: bcad36146bc88778cb4debd240a1fc6448783fb3`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0072 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0072
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'içecek', fiil 'yuvarlamak', sıfat 'rahat'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: oyun hamuru çok sertti ve kurabiyeler kırılıyordu | hamuru elleri arasında yuvarladı ve yumuşattı
@tohum: hello_kitty-0072
Dışarıda yağmur tıp tıp yağıyordu. Hello Kitty evde ilk kez oyun hamuruyla kurabiye yapmak istedi. Ama hamur çok sertti ve kurabiyeler hep kırılıyordu. Hello Kitty hamura baktı ve biraz düşündü. Sonra hamuru iki elinin arasında uzun uzun yuvarladı. Hamur ısındı ve yavaş yavaş yumuşadı. Hello Kitty küçük toplar yaptı ve hepsini düz bastırdı. Artık hiçbir kurabiye kırılmadı. Hello Kitty yuvarlak kurabiyeleri bir tabağa dizdi. Yanına da bir bardak içecek koydu. Sonra rahat koltuğuna oturdu. Hello Kitty hamur kurabiyeleriyle çay oyununa mutlu mutlu başladı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ilk kez oyun hamuruyla kurabiye yapmak"
   - Cümle 2: «Hello Kitty evde ilk kez oyun hamuruyla kurabiye yapmak istedi.»
   - Açıklama: Kartın özellikler alanındaki kurabiye yapma sevgisi gerçek kurabiye yerine oyun hamuru oyuncağına çevrilmiş, özellik karttaki gibi kullanılmamış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra rahat koltuğuna oturdu"
   - Cümle 11: «Sonra rahat koltuğuna oturdu.»
   - Açıklama: Koltuğa oturma olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0072` birebir aynı, ardından `@onarim: ad8be0c91fdea1ebf575176af09a018279d843fd`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0074 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0074
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'portakal', fiil 'katılmak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: son turta dilimi kaldı ama annesi hiç yememişti | turtayı ikiye bölüp büyük parçayı annesine verdi
@tohum: hello_kitty-0074
@degisim: katılmak -> bölmek
Ormanın kamp yerinde kuşlar ötüyordu. Hello Kitty sepetten son elmalı turta dilimini çıkardı. Sepette bir de portakal vardı. Ama annesi daha hiç turta yememişti, çünkü dilimleri hep Hello Kitty'ye vermişti. Hello Kitty turtaya baktı ve biraz düşündü. Sonra onu elleriyle ikiye böldü. Büyük parçayı annesine uzattı. Annesi gülümsedi ve sepetteki portakalı aldı. Portakalı soydu ve yarısını Hello Kitty'ye verdi. Önlerinde meyveli, küçük bir sofra oldu. İkisi turtayı ve portakalı ağaçların gölgesinde birlikte yedi. Hello Kitty çok mutlu oldu, çünkü en sevdiği turtayı annesiyle paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama annesi daha hiç turta yememişti"
   - Cümle 4: «Ama annesi daha hiç turta yememişti, çünkü dilimleri hep Hello Kitty'ye vermişti.»
   - Açıklama: Sorun (annenin hiç turta yememiş olması) ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0074` birebir aynı, `@degisim: katılmak -> bölmek` (tutuyorsan), ardından `@onarim: 4521e1ad486adedae28939d38f3fd8dcfb527bdf`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0075 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0075
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'mermer', fiil 'eşleştirmek', sıfat 'büyük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: babası elmaları nereye koyduğunu unuttu | çantayı hatırladı ve elmaları tezgahta buldu
@tohum: hello_kitty-0075
@degisim: eşleştirmek -> hatırlamak
Hello Kitty babasıyla mutfakta turta yapmak istedi. En çok elmalı turtayı severdi ama babası elmaları nereye koyduğunu unutmuştu. Babası dolabı açtı ama elmalar orada yoktu. "Kızım, bana yardım eder misin?" diye sordu babası. Hello Kitty biraz düşündü ve hatırladı. "Baba, eve büyük bir çantayla geldin, belki elmalar oradadır," dedi Hello Kitty. Sonra etrafına baktı. Büyük çanta mermer tezgahın üstünde duruyordu. Hello Kitty çantayı açtı ve içinde kırmızı elmaları buldu. Babası güldü ve elmaları yıkamaya başladı. "Teşekkürler, kızım, elmaları sen buldun!" dedi babası.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Babası dolabı açtı ama"
   - Cümle 3: «Babası dolabı açtı ama elmalar orada yoktu.»
   - Açıklama: Art arda iki cümlede aynı 'ama' kalıbı gereksizce tekrarlanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çanta mermer tezgahın üstünde"
   - Cümle 8: «Büyük çanta mermer tezgahın üstünde duruyordu.»
   - Açıklama: 'Mermer' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0075` birebir aynı, `@degisim: eşleştirmek -> hatırlamak` (tutuyorsan), ardından `@onarim: f86a57e2c2a87ddf0952740afe7c1116e1f3f9e7`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0078
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fıskiye', fiil 'karşılamak', sıfat 'enerjik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası sırayı unutuyor ve topu hep kendisi atıyordu | kızmadan babasına sırayla atmayı önerdi
@tohum: hello_kitty-0078
@degisim: fıskiye -> çimen
Bir sabah babası parka elinde bir topla geldi. Hello Kitty onu çimenlerde sevinçle karşıladı. Ama enerjik babası sırayı unutuyor ve topu hep kendisi atıyordu. Hello Kitty'ye hiç sıra gelmedi. Hello Kitty kızmadı, çünkü herkese bir arkadaş gibi iyi davranırdı. "Baba, sırayla atalım, şimdi sıra bende," dedi Hello Kitty. "Haklısın, unuttum!" dedi babası ve güldü. Babası topu ona verdi. Hello Kitty topu yukarı attı ve babası koşup tuttu. Sonra babası "Hop!" diye bağırdı ve topu yavaşça geri attı. Hello Kitty onu iki eliyle yakaladı. İkisi uzun süre neşeyle oynadı. Hello Kitty çok sevindi, çünkü artık sıra ikisine de geliyordu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bir sabah babası parka"
   - Cümle 1: «Bir sabah babası parka elinde bir topla geldi.»
   - Açıklama: Hikaye 'babası' ile açılıyor; kimin babası olduğu henüz belli değil.
   - Açıklama: Hikayenin ilk cümlesinde 'babası' kimin babası olduğu henüz belli değilken kullanılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama enerjik babası sırayı"
   - Cümle 3: «Ama enerjik babası sırayı unutuyor ve topu hep kendisi atıyordu.»
   - Açıklama: 'Enerjik' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Enerjik' 3 yaşındaki bir çocuğun bilmeyeceği yabancı kökenli soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0078` birebir aynı, `@degisim: fıskiye -> çimen` (tutuyorsan), ardından `@onarim: 898163414532639a5e89633839e92f5675c81460`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0079 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0079
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kitap', fiil 'kucaklamak', sıfat 'dağınık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: mutfaktan bilinmeyen bir ses geldi | kurabiye kitabının yerine bakıp sayfaları çeviren rüzgarı buldu
@tohum: hello_kitty-0079
Mutfağın penceresinden serin bir rüzgar esiyordu. Hello Kitty odasında otururken mutfaktan hışır hışır bir ses duydu. Hello Kitty bu sesi çok merak etti, çünkü mutfakta kimse yoktu. Yavaşça mutfağa yürüdü. Masada dağınık kaşıklar ve kaplar vardı. Hello Kitty onların arasına baktı ama ses oradan gelmiyordu. Hello Kitty kurabiye yaparken hep en sevdiği kitaba bakardı. O kitap pencerenin önündeki tezgahta dururdu. Hello Kitty hemen tezgaha baktı. Rüzgar kitabın sayfalarını tek tek çeviriyordu. Ses buradan geliyordu. Hello Kitty pencereyi kapattı ve kitabı sıkıca kucakladı. Hello Kitty çok sevindi, çünkü sesi bulmuş ve kitabını korumuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurabiye kitabının yerine bakıp"
   - Cümle 0 (plan satırı): «mutfaktan bilinmeyen bir ses geldi | kurabiye kitabının yerine bakıp sayfaları çeviren rüzgarı buldu»
   - Açıklama: 'Yerine' hem 'kitabın durduğu yere' hem 'kitap yerine' diye okunabiliyor; anlam belirsiz.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "mutfakta kimse yoktu"
   - Cümle 3: «Hello Kitty bu sesi çok merak etti, çünkü mutfakta kimse yoktu.»
   - Açıklama: Boş mutfaktan gelen bilinmeyen ses küçük bir çocuğu korkutabilecek bir öğe.
   - Açıklama: Boş mutfaktan gelen bilinmeyen ses küçük bir çocuğu korkutabilir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty kurabiye yaparken hep en sevdiği kitaba bakardı"
   - Cümle 7: «Hello Kitty kurabiye yaparken hep en sevdiği kitaba bakardı.»
   - Açıklama: Kitap sesle bağlantı kurulmadan sebepsizce akla geliyor ve çözümü getiriyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty pencereyi kapattı"
   - Cümle 12: «Hello Kitty pencereyi kapattı ve kitabı sıkıca kucakladı.»
   - Açıklama: 'Hello Kitty' adı neredeyse her cümlede gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0079` birebir aynı, ardından `@onarim: a05213d1a7d21697386cbe74622de2c1ca53a1c8`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0080 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0080
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'masa', fiil 'karıştırmak', sıfat 'bembeyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: babasının beyaz boyası bitti ve karlar boş kaldı | kendi beyaz boyasını babasıyla paylaştı
@tohum: hello_kitty-0080
Dışarıda kar sessizce yağıyordu. Hello Kitty ve babası masada karlı bir resim yapıyordu. Ama babasının beyaz boyası bitmişti ve resmindeki karlar boş kaldı. "Eyvah, bende hiç beyaz kalmadı," dedi babası. Hello Kitty herkese iyi davranırdı. Kendi beyaz boyasını hemen babasının önüne koydu. "Baba, bunu birlikte kullanalım," dedi Hello Kitty. Babası fırçasını suya batırdı ve boyayla karıştırdı. Sonra kağıttaki karları bembeyaz yaptı. "Teşekkürler, kızım, sen çok iyi bir arkadaşsın," dedi babası. Hello Kitty gülümsedi. İkisi resimlerini yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "beyaz boyası bitti ve karlar boş kaldı"
   - Cümle 0 (plan satırı): «babasının beyaz boyası bitti ve karlar boş kaldı | kendi beyaz boyasını babasıyla paylaştı»
   - Açıklama: Karlar boş kalmaz; boyanmamış kalan kar yerleri kastediliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "resmindeki karlar boş kaldı"
   - Cümle 3: «Ama babasının beyaz boyası bitmişti ve resmindeki karlar boş kaldı.»
   - Açıklama: Karlar boş kalmaz; 'karlar boyanmadan kaldı' gibi olmalı.
   - Açıklama: Karlar boş kalmaz; boyanmamış yerler kastediliyor, kelime yanlış anlamda.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve karlar boş kaldı"
   - Cümle 3: «Ama babasının beyaz boyası bitmişti ve resmindeki karlar boş kaldı.»
   - Açıklama: Karlar boş kalmaz; resimde boyanmamış kalan yerler kastediliyor, kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0080` birebir aynı, ardından `@onarim: 65e2690424bfe8bd78efdee54b198f48e0359261`, sonra gövde.
