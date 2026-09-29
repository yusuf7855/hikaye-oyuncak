# Editör görevi (onarım): Hello Kitty, onarım partisi 24

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar24.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar24.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0053 (deneme 5 -> 6)

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
@plan: top kavanoza çarptı ve kavanoz çiçeklerin arasında kayboldu | parçaların peşinden gidip kavanozu buldu
@tohum: hello_kitty-0053
Hello Kitty ile Mimi parkta top oynuyordu. Hello Kitty kendi yaptığı kurabiyelerin kavanozunu örtüye bırakmıştı. Birden Mimi'nin attığı top kavanoza çarptı ve kavanoz çiçeklerin arasında kayboldu. "Kurabiyeler nereye gitti?" diye sordu utangaç Mimi. Hello Kitty yere dikkatle baktı. Çimenlerde küçük, sarı parçalar vardı. Hello Kitty onları hemen tanıdı, çünkü o kurabiyeleri kendisi yapmıştı. İki kardeş parçaların peşinden yürüdü. Parçalar büyük bir çiçeğin arkasında bitti. Kavanoz orada, kapağı açık duruyordu. Hello Kitty kavanozu aldı ve içine baktı. Kurabiyelerin çoğu sağlamdı. "Bak, Mimi, kurabiyelerimiz burada!" dedi Hello Kitty. İki kardeş çok sevindi, çünkü kurabiyelerini yeniden bulmuşlardı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kavanoz çiçeklerin arasında kayboldu"
   - Cümle 3: «Birden Mimi'nin attığı top kavanoza çarptı ve kavanoz çiçeklerin arasında kayboldu.»
   - Açıklama: Topun çarptığı kavanozun iz bırakarak çiçeklerin arkasına kadar gidip kaybolması akla yatkın değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "o kurabiyeleri kendisi yapmıştı"
   - Cümle 7: «Hello Kitty onları hemen tanıdı, çünkü o kurabiyeleri kendisi yapmıştı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kurabiye bir büyükle birlikte yapılır, burada Hello Kitty tek başına yapmış.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "o kurabiyeleri kendisi yapmıştı"
   - Cümle 7: «Hello Kitty onları hemen tanıdı, çünkü o kurabiyeleri kendisi yapmıştı.»
   - Açıklama: Kurabiyeleri Hello Kitty'nin kendisinin yaptığı 2. cümlede zaten söylenmişti; bilgi gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0053` birebir aynı, ardından `@onarim: 7e157eea4e9f8e6242317d6dafc384ddb7eaabd2`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0069 (deneme 3 -> 4)

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
Parkta, yolun kenarında yumuşak bir toprak vardı. Hello Kitty arkadaşlarını güldürmek için bir dalla toprağa komik bir kedi çiziyordu. Ama resimdeki başı çok büyük çizmişti ve toprak yetmedi. Başın yarısı çimenlerin üstünde kaldı ve hiç görünmedi. Hello Kitty toprağa baktı ve biraz düşündü. Sonra büyük çizgileri eliyle sildi. Bu kez daha küçük, yuvarlak bir baş çizdi. Küçük baş toprağa tam sığdı. Hello Kitty resme iki göz ve uzun bıyıklar ekledi. En sona iki sivri kulak koydu. Kedi acıkmasın diye önüne bir de köfte çizdi. Hello Kitty çok sevindi, çünkü kedisi tam istediği gibi olmuştu.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarını güldürmek için"
   - Cümle 2: «Hello Kitty arkadaşlarını güldürmek için bir dalla toprağa komik bir kedi çiziyordu.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği yalnız amaç olarak anılıyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarını güldürmek için"
   - Cümle 2: «Hello Kitty arkadaşlarını güldürmek için bir dalla toprağa komik bir kedi çiziyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Hello Kitty arkadaşlarını güldürmek için"
   - Cümle 2: «Hello Kitty arkadaşlarını güldürmek için bir dalla toprağa komik bir kedi çiziyordu.»
   - Açıklama: Kartın yanlar alanında Mimi, annesi ve babası dışında arkadaş yok; kararlar hayvan arkadaşlarının kartta olmadığını söyler.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "arkadaşlarını güldürmek için"
   - Cümle 2: «Hello Kitty arkadaşlarını güldürmek için bir dalla toprağa komik bir kedi çiziyordu.»
   - Açıklama: Kurulan hedef arkadaşları güldürmek ama arkadaşlar hiç görünmüyor ve bu hedefe dönülmüyor.
   - Açıklama: Hikayenin hedefi arkadaşları güldürmek olarak kuruluyor ama arkadaşlar hiç görünmüyor ve bu hedefe dönülmüyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki sivri kulak koydu"
   - Cümle 10: «En sona iki sivri kulak koydu.»
   - Açıklama: Resme kulak konmaz, çizilir; 'koydu' fiili çizme eylemine uymuyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "önüne bir de köfte çizdi"
   - Cümle 11: «Kedi acıkmasın diye önüne bir de köfte çizdi.»
   - Açıklama: Köfte sebepsiz ekleniyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Köfte sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0069` birebir aynı, `@degisim: düşünceli -> küçük` (tutuyorsan), ardından `@onarim: e7f150805614303aa29915b368f14e48f7c2784b`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0071 (deneme 3 -> 4)

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
Rüzgar ağaçların arasında yavaşça esiyordu. Hello Kitty ve Mimi ailece geldikleri kamp yerindeydi. İkisi yonca toplamak için boş sepeti aynı anda istedi ve oyun durdu. Hello Kitty biraz düşündü. Az önce elmalı turtayı da dilim dilim, sırayla yemişlerdi. "Mimi, sırayla oynayalım, önce sen bul," dedi Hello Kitty. Mimi çimenlere baktı ve küçük bir yonca buldu. Onu sepete koydu ve sepeti Hello Kitty'ye uzattı. Sonra Hello Kitty de yeşil bir yonca buldu. "Şimdi sıra yine sende, Mimi," dedi Hello Kitty. Sepet yavaş yavaş yeşil yapraklarla doldu. İkisi gülerek eğlendi. İki kardeş çok sevindi, çünkü sırayla oynayınca ikisi de yonca bulmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Az önce elmalı turtayı da dilim dilim"
   - Cümle 5: «Az önce elmalı turtayı da dilim dilim, sırayla yemişlerdi.»
   - Açıklama: Tohumdaki turta özelliği yalnız geçmişte olmuş bir anı olarak anılıyor, çözümde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Az önce elmalı turtayı da dilim dilim, sırayla yemişlerdi"
   - Cümle 5: «Az önce elmalı turtayı da dilim dilim, sırayla yemişlerdi.»
   - Açıklama: Tohumdaki elmalı turta sevgisi çözümde işe yaramıyor, turta yalnız anı olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0071` birebir aynı, `@degisim: sadık -> boş` (tutuyorsan), ardından `@onarim: 0b8fb20c876462dabd181263a6c0a4ca457e87db`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0072 (deneme 3 -> 4)

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
Dışarıda yağmur tıp tıp yağıyordu. Hello Kitty evde ilk kez oyun hamuruyla kurabiye yapmak istedi. Ama hamur çok sertti ve kurabiyeler hep kırılıyordu. Hello Kitty hamura baktı ve biraz düşündü. Gerçek kurabiye yaparken hamuru hep elleriyle ısıtırdı. Sonra hamuru iki elinin arasında uzun uzun yuvarladı. Hamur ısındı ve yavaş yavaş yumuşadı. Hello Kitty küçük toplar yaptı ve hepsini düz bastırdı. Artık hiçbir kurabiye kırılmadı. Hello Kitty yuvarlak kurabiyeleri bir tabağa dizdi. Yanına da bir bardak içecek koydu. Sonra masaya rahatça oturdu ve çay oyununa mutlu mutlu başladı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanına da bir bardak içecek koydu"
   - Cümle 11: «Yanına da bir bardak içecek koydu.»
   - Açıklama: İçecek ve çay oyunu hiç kurulmadan sonda sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0072` birebir aynı, ardından `@onarim: a4a3f73987be28603a08cfc1b1dda2f29cde4460`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0075 (deneme 3 -> 4)

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
Hello Kitty babasıyla mutfakta turta yapmak istedi. En çok elmalı turtayı severdi ama babası elmaları nereye koyduğunu unutmuştu. Babası dolaba baktı ve elmaları orada bulamadı. "Kızım, bana yardım eder misin?" diye sordu babası. Hello Kitty biraz düşündü ve hatırladı. "Baba, eve büyük bir çantayla geldin, belki elmalar oradadır," dedi Hello Kitty. Sonra etrafına baktı. Büyük çanta, mermer taştan yapılmış tezgahın üstündeydi. Hello Kitty çantayı açtı ve içinde kırmızı elmaları buldu. Babası güldü ve elmaları yıkamaya başladı. "Teşekkürler, kızım, elmaları sen buldun!" dedi babası.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "mermer taştan yapılmış tezgahın"
   - Cümle 8: «Büyük çanta, mermer taştan yapılmış tezgahın üstündeydi.»
   - Açıklama: Tezgahın mermer olması hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0075` birebir aynı, `@degisim: eşleştirmek -> hatırlamak` (tutuyorsan), ardından `@onarim: a4f825b68634f6d44712ba81250689c38779b63d`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0078 (deneme 3 -> 4)

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
Bir sabah Hello Kitty'nin babası parka elinde bir topla geldi. Hello Kitty onu çimenlerde sevinçle karşıladı. Ama babası çok enerjikti, sırayı unutuyor ve topu hep kendisi atıyordu. Hello Kitty'ye hiç sıra gelmedi. Hello Kitty kızmadı, çünkü herkese bir arkadaş gibi iyi davranırdı. "Baba, sırayla atalım, şimdi sıra bende," dedi Hello Kitty. "Haklısın, unuttum!" dedi babası ve güldü. Babası topu ona verdi. Hello Kitty topu yukarı attı ve babası koşup tuttu. Sonra babası "Hop!" diye bağırdı ve topu yavaşça geri attı. Hello Kitty onu iki eliyle yakaladı. İkisi neşeyle oynadı. Hello Kitty çok sevindi, çünkü artık sıra ikisine de geliyordu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty onu çimenlerde sevinçle karşıladı"
   - Cümle 2: «Hello Kitty onu çimenlerde sevinçle karşıladı.»
   - Açıklama: Güvenli kullanım satırına aykırı olarak Hello Kitty babası gelmeden parkta tek başına bekliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "babası çok enerjikti"
   - Cümle 3: «Ama babası çok enerjikti, sırayı unutuyor ve topu hep kendisi atıyordu.»
   - Açıklama: 'Enerjik' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Enerjik' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sırayı unutuyor ve topu hep kendisi atıyordu"
   - Cümle 3: «Ama babası çok enerjikti, sırayı unutuyor ve topu hep kendisi atıyordu.»
   - Açıklama: İki kişilik top oyununda babanın topu hep kendisinin nasıl attığı belirsiz ve sorunun sebebi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0078` birebir aynı, `@degisim: fıskiye -> çimen` (tutuyorsan), ardından `@onarim: e229239e29b73895c33cd10fca04b24f4175283b`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0079 (deneme 3 -> 4)

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
@plan: mutfaktan bilinmeyen bir ses geldi | kurabiye kitabının durduğu tezgaha bakıp rüzgarı buldu
@tohum: hello_kitty-0079
Mutfağın penceresinden serin bir rüzgar esiyordu. Hello Kitty odasında otururken mutfaktan hışır hışır bir ses duydu. Bu sesi çok merak etti. Yavaşça mutfağa yürüdü. Masada dağınık kaşıklar ve kaplar vardı. Onların arasına baktı ama ses oradan gelmiyordu. Ses, kağıttan geliyor gibiydi. Hello Kitty kurabiye yaparken hep bir kitaba bakardı. O kitap pencerenin önündeki tezgahta dururdu. Hemen tezgaha baktı. Rüzgar kitabın sayfalarını tek tek çeviriyordu. Ses buradan geliyordu. Pencereyi kapattı ve kitabı sıkıca kucakladı. Hello Kitty çok sevindi, çünkü sesi bulmuş ve kitabını korumuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bakıp rüzgarı buldu"
   - Cümle 0 (plan satırı): «mutfaktan bilinmeyen bir ses geldi | kurabiye kitabının durduğu tezgaha bakıp rüzgarı buldu»
   - Açıklama: Rüzgar bulunan bir şey değil; fiil nesnesine uymuyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Onların arasına baktı ama ses oradan gelmiyordu"
   - Cümle 6: «Onların arasına baktı ama ses oradan gelmiyordu.»
   - Açıklama: Çözüm önce sebebe değil masadaki kaplara yöneliyor ve fazladan bir arama adımı ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0079` birebir aynı, ardından `@onarim: f61bbc55a9c8f4885afcdcf94e2dd7640eb9cf8d`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0080 (deneme 2 -> 3)

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
@plan: babasının beyaz boyası bitti ve karları yapamadı | kendi beyaz boyasını babasıyla paylaştı
@tohum: hello_kitty-0080
Dışarıda kar sessizce yağıyordu. Hello Kitty ve babası masada karlı bir resim yapıyordu. Ama babasının beyaz boyası bitmişti ve karları yapamadı. "Eyvah, bende hiç beyaz kalmadı," dedi babası. Hello Kitty herkese iyi davranırdı. Kendi beyaz boyasını hemen babasının önüne koydu. "Baba, bunu birlikte kullanalım," dedi Hello Kitty. Babası fırçasını suya batırdı ve boyayla karıştırdı. Sonra kağıttaki karları bembeyaz yaptı. "Teşekkürler, kızım, sen çok iyi bir arkadaşsın," dedi babası. Hello Kitty gülümsedi. İkisi resimlerini yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "babasının beyaz boyası bitti ve karları yapamadı"
   - Cümle 0 (plan satırı): «babasının beyaz boyası bitti ve karları yapamadı | kendi beyaz boyasını babasıyla paylaştı»
   - Açıklama: Planda da özne uyumsuzluğu var; karları yapamayan boya değil baba.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "beyaz boyası bitmişti ve karları yapamadı"
   - Cümle 3: «Ama babasının beyaz boyası bitmişti ve karları yapamadı.»
   - Açıklama: Bağlı iki yüklemin öznesi farklı; 'boya' bitmiş ama 'yapamadı'nın öznesi baba, cümle uyumsuz.
   - Açıklama: İki yüklemin öznesi farklı; 'yapamadı' fiilinin öznesi boya gibi duruyor, 'babası karları yapamadı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0080` birebir aynı, ardından `@onarim: b91e8356b01f37d43cfae8471c0b1ccf151a1181`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0084 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0084
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'piyano', fiil 'gülüşmek', sıfat 'rengarenk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: piyanoya küçük bir dal sıkıştı ve ses çıkmadı | piyanoyu ters çevirip salladı ve dalı düşürdü
@tohum: hello_kitty-0084
@degisim: gülüşmek -> gülmek
Ormanda rüzgar yavaşça esiyordu. Hello Kitty çadırın önünde rengarenk piyanosunu çalıyordu. Ama piyanonun sesi birden kesildi, çünkü tuşların arasına küçük bir dal sıkışmıştı. Oyuncak arkadaşlarını da önüne koymuştu. Yeni arkadaşlarını çok severdi ve onlara bir şarkı çalmak istiyordu. Piyanoyu yavaşça ters çevirdi ve biraz salladı. Küçük dal çimenlere düştü. Piyano yeniden ses verdi. Hello Kitty komik bir şarkı çaldı ve çok güldü. Hello Kitty çok mutluydu, çünkü arkadaşlarına yeniden şarkı çalabiliyordu.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty çadırın önünde"
   - Cümle 2: «Hello Kitty çadırın önünde rengarenk piyanosunu çalıyordu.»
   - Açıklama: Hello Kitty ormandaki çadırda tek başına; güvenli özellik kullanımı alanı kimsenin tek başına uzağa gitmediğini söylüyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tuşların arasına küçük bir dal sıkışmıştı"
   - Cümle 3: «Ama piyanonun sesi birden kesildi, çünkü tuşların arasına küçük bir dal sıkışmıştı.»
   - Açıklama: Dalın çalarken tuşlara nasıl sıkıştığı söylenmiyor ve tek bir dalın bütün sesi kesmesi akla yatkın değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yeni arkadaşlarını çok severdi"
   - Cümle 5: «Yeni arkadaşlarını çok severdi ve onlara bir şarkı çalmak istiyordu.»
   - Açıklama: Önce 'oyuncak arkadaşları' olarak anılan grup 'yeni arkadaşları' diye yeniden tanıtılıyor ve aynı kişiler mi belli değil.
   - Açıklama: 'Yeni arkadaşlarını' ifadesinin önceki cümledeki oyuncak arkadaşları mı yoksa başka kişileri mi gösterdiği belli değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarını çok severdi"
   - Cümle 5: «Yeni arkadaşlarını çok severdi ve onlara bir şarkı çalmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği oyuncaklara dönüşmüş ve sorunun çözümünde hiçbir işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği oyuncaklara yakıştırılarak yalnız söyleniyor, kartın özellikler alanındaki gibi çözümde işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yeni arkadaşlarını çok severdi"
   - Cümle 5: «Yeni arkadaşlarını çok severdi ve onlara bir şarkı çalmak istiyordu.»
   - Açıklama: Oyuncak arkadaşlar sorundan sonra sebepsiz beliriyor ve 'yeni arkadaşlar' olarak tutarsız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0084` birebir aynı, `@degisim: gülüşmek -> gülmek` (tutuyorsan), ardından `@onarim: c167514d8a3d030e177ac8794ff047c70136c66a`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0086 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0086
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'boncuk', fiil 'buluşmak', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: şeker boncuklar kuru kurabiyelere yapışmadı | kurabiyelere önce biraz bal sürdü
@tohum: hello_kitty-0086
@degisim: buluşmak -> yapışmak
Kuşlar ağaçlarda cıvıl cıvıl ötüyordu. Hello Kitty ve Mimi parkta, ağaçların gölgesinde kurabiye süslüyordu. Ama renkli şeker boncuklar yapışmadı, çünkü kurabiyeler çok kuruydu. "Boncuklar hep düşüyor," dedi Mimi. Hello Kitty kurabiye yapmayı çok severdi ve sepete baktı. Sepette, ekmekler için getirdikleri bal saklıydı. "Önce biraz bal sürelim, Mimi," dedi Hello Kitty. Kaşıkla her kurabiyeye bal sürdü. Sonra renkli boncukları üstüne koydu. Boncuklar bala yapıştı ve hiç düşmedi. Mimi bir kurabiye aldı ve gülümsedi. "Teşekkürler, Hello Kitty, kurabiyeler çok güzel oldu!" dedi Mimi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kurabiye yapmayı çok severdi ve sepete baktı"
   - Cümle 5: «Hello Kitty kurabiye yapmayı çok severdi ve sepete baktı.»
   - Açıklama: Geniş zamanlı alışkanlık cümlesi ilgisiz bir eylemle 've' ile bozuk biçimde bağlanmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0086` birebir aynı, `@degisim: buluşmak -> yapışmak` (tutuyorsan), ardından `@onarim: 5f770a0b0410fceecc67dd79c52f1cd60df18832`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0088 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0088
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yapboz', fiil 'kalkmak', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: yapbozun son parçası birden kayboldu | turtadan dilim almak için tabağı kaldırıp parçayı buldu
@tohum: hello_kitty-0088
Hello Kitty ormandaki kamp yerinde annesiyle yapboz yapıyordu. Yanlarında annesinin yaptığı elmalı turta duruyordu. Ama yapbozun son parçası bir anda kayboldu. Annesi yerinden kalktı ve eteğini salladı. Parça oradan da düşmedi. "Belki çimenlerin arasındadır," dedi annesi. İkisi yere eğildi ve her yere baktı. Hello Kitty kararlıydı, yapbozu bitirmek istiyordu. Sonra en sevdiği turtadan bir dilim almak için tabağı kaldırdı. Tabağın altında küçük parçayı gördü. Parça oraya kaymıştı. Hello Kitty parçayı hemen yerine koydu ve yapboz bitti. "Anne, yapboz bitti, şimdi turta zamanı!" dedi Hello Kitty sevinçle.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Parça oradan da düşmedi"
   - Cümle 5: «Parça oradan da düşmedi.»
   - Açıklama: 'da' bağlacı önceki bir durumu varsayıyor ama öncesinde parçanın bir yerden düşmediği söylenmedi, cümle anlamca kusurlu.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "en sevdiği turtadan bir dilim almak için tabağı kaldırdı"
   - Cümle 9: «Sonra en sevdiği turtadan bir dilim almak için tabağı kaldırdı.»
   - Açıklama: Parça aramaya yönelik bir adımla değil, turta almak için rastlantıyla bulunuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra en sevdiği turtadan bir dilim almak için tabağı kaldırdı"
   - Cümle 9: «Sonra en sevdiği turtadan bir dilim almak için tabağı kaldırdı.»
   - Açıklama: Parça aranarak değil turta almak isterken tesadüfen bulunuyor; çözüm sebebe yönelmiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği turtadan bir dilim almak için tabağı kaldırdı"
   - Cümle 9: «Sonra en sevdiği turtadan bir dilim almak için tabağı kaldırdı.»
   - Açıklama: Çözümü sebepsiz bir rastlantı getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0088` birebir aynı, ardından `@onarim: bb4e73aa007e8f52286f9602384d24296fd6861c`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0089
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'küp', fiil 'susmak', sıfat 'basit'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: ikisi aynı anda küp koyunca kule yıkıldı | kurabiyeyi sıra işareti yapıp sırayla küp koydular
@tohum: hello_kitty-0089
Parkta ağaçların gölgesinde Hello Kitty ile babası küp oyunu oynuyordu. İkisi küpleri üst üste koyup bir kule yapıyordu. Ama ikisi aynı anda küp koyunca kule yıkıldı. Babası bir an sustu, sonra güldü. "Böyle olmuyor, Hello Kitty," dedi babası. Hello Kitty sepetten evde kendi yaptığı bir kurabiyeyi çıkardı. "Önce sen koy, sonra kurabiyeyi bana ver," dedi Hello Kitty. Bu çok basit bir oyundu. Babası küpünü koydu ve kurabiyeyi Hello Kitty'ye verdi. Hello Kitty de küpünü koydu ve kurabiyeyi geri uzattı. Kule yavaş yavaş yükseldi ve bu kez hiç yıkılmadı. Sonra kurabiyeyi ikiye böldüler ve oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "evde kendi yaptığı bir kurabiyeyi"
   - Cümle 6: «Hello Kitty sepetten evde kendi yaptığı bir kurabiyeyi çıkardı.»
   - Açıklama: Güvenli kullanım satırına göre kurabiye bir büyükle yapılır; burada Hello Kitty kurabiyeyi kendi yapmış gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0089` birebir aynı, ardından `@onarim: 671019b9f6a2f542ec89502935bba62b7e1dda20`, sonra gövde.
