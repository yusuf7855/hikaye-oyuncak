# Editör görevi (onarım): Hello Kitty, onarım partisi 46

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar46.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar46.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0124 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0124
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kanepe', fiil 'eğlendirmek', sıfat 'çamurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesi sürprizini ağacın arkasına sakladı | turtanın kokusunu tanıdı ve sepeti buldu
@tohum: hello_kitty-0124
@degisim: kanepe -> örtü
Parkta çimenler ıslak ve çamurluydu. Hello Kitty annesiyle ağacın altında, bir örtünün üstünde oturuyordu. "Sana bir sürpriz getirdim, ama onu sakladım," dedi annesi. Hello Kitty sürprizi çok merak etti. Birden tatlı bir koku duydu. Hello Kitty en çok elmalı turtayı severdi ve bu kokuyu hemen tanıdı. Koku yakındaki başka bir ağaçtan geliyordu. Hello Kitty o ağaca yavaşça yürüdü. Ağacın arkasında küçük bir sepet duruyordu. Sepetin içinde bir elmalı turta vardı! "Buldum, anne!" dedi Hello Kitty. Annesi güldü ve turtayı örtüye getirdi. "Anneciğim, bu oyun beni çok eğlendirdi!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Parkta çimenler ıslak ve çamurluydu"
   - Cümle 1: «Parkta çimenler ıslak ve çamurluydu.»
   - Açıklama: Islak ve çamurlu çimen işe yarayacakmış gibi kuruluyor ama hikayede hiç kullanılmıyor.
   - Açıklama: Islak ve çamurlu çimenler işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0124` birebir aynı, `@degisim: kanepe -> örtü` (tutuyorsan), ardından `@onarim: 295d4993cbc93a126d33a5bc2739eae9510a3a53`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0125 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0125
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'topaç', fiil 'durmak', sıfat 'tuhaf'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: topaç yumuşak çimenlerde hemen durdu | düz bir kapağı yere koyup topacı üstünde çevirdi
@tohum: hello_kitty-0125
Bir sabah Hello Kitty evin yakınındaki parkta kırmızı topacıyla oynuyordu. Onu çimenlerin üstünde hızla çevirdi. Ama topaç yumuşak çimenlerde hemen durdu ve devrildi. Hello Kitty bir daha denedi. Topaç bu kez tuhaf bir şekilde sallandı ve yine durdu. Topacın dönmesi için düz ve sert bir yer gerekiyordu. Hello Kitty çantasına baktı. İçinde evde yapılan kurabiyelerin kutusu vardı. Kutunun kapağı düz ve sertti. Hello Kitty kapağı çimenin üstüne koydu. Topacı onun ortasında çevirdi. Kırmızı topaç bu kez uzun uzun döndü. Hello Kitty sevinçle ellerini çırptı. Sonra orada mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "evde yapılan kurabiyelerin kutusu"
   - Cümle 8: «İçinde evde yapılan kurabiyelerin kutusu vardı.»
   - Açıklama: Kurabiye yapmayı sevme özelliği kullanılmıyor; yalnız kurabiye kutusunun kapağı işe yarıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0125` birebir aynı, ardından `@onarim: 17e2026db649b7d264cc3435eee353c30d6f53ed`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0135 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0135
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'bambu', fiil 'atlamak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: rüzgar çok gürültülü olduğu için geri gelen sesi duyamadı | rüzgarın durmasını bekledi ve yeniden seslendi
@tohum: hello_kitty-0135
@degisim: bambu -> rüzgar
Rüzgar ormanda hızlı hızlı esiyordu. Kamp yerinde annesi, Hello Kitty'ye ormanda sesin geri geldiğini söyledi. Hello Kitty seslendi, ama rüzgar yüzünden geri gelen sesi duyamadı. "Anne, rüzgar durunca yine seslenirim," dedi Hello Kitty. Rüzgar durmadı, Hello Kitty de yerinde iki kez atladı. "Sabırsız olma, kızım, rüzgar birazdan durur," dedi annesi. Hello Kitty yerine oturdu ve bekledi. Biraz sonra rüzgar durdu ve orman sessiz oldu. "Benimle arkadaş olur musun?" diye seslendi Hello Kitty. Uzaktan "Olur musun?" diye bir ses geri geldi. Annesi güldü ve kızına sarıldı. Hello Kitty çok sevindi, çünkü sesinin geri geldiğini sonunda duymuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Rüzgar durmadı, Hello Kitty de yerinde iki kez atladı"
   - Cümle 5: «Rüzgar durmadı, Hello Kitty de yerinde iki kez atladı.»
   - Açıklama: İki yan cümle 'de' ile anlamsız biçimde bağlanmış; rüzgarın durmamasıyla Hello Kitty'nin atlaması arasında 'de'nin kurduğu ilişki yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Benimle arkadaş olur musun?"
   - Cümle 9: «"Benimle arkadaş olur musun?" diye seslendi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız seslenilen söz olarak geçiyor, sorunun çözümünde işe yaramıyor (kartın özellikler alanı).

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0135` birebir aynı, `@degisim: bambu -> rüzgar` (tutuyorsan), ardından `@onarim: 019e86e088f88ef4709b46cec4e534aef35f670c`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0137 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0137
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çamaşır', fiil 'şakalaşmak', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: koşarken kardeşinin çamaşırlarını yere düşürdü | özür diledi ve çamaşırları kardeşiyle yeniden katladı
@tohum: hello_kitty-0137
@degisim: şakalaşmak -> oynamak
Dışarıda yağmur yağıyordu. Hello Kitty ile ikizi Mimi evde oyun oynuyordu. Hello Kitty koşarken Mimi'nin katladığı çamaşırlara çarptı ve hepsi yere düştü. Mimi yerdeki çamaşırlara baktı ve çok üzüldü. Hello Kitty hemen durdu ve kardeşinin yanına gitti. En iyi arkadaşının üzülmesini istemedi ve ondan özür diledi. Sonra Mimi'ye sıkıca sarıldı. Hello Kitty yumuşak havluları yerden tek tek topladı. Mimi de ona yardım etti. İkisi birlikte bütün çamaşırları yeniden katladı ve sepete koydu. Mimi gülümsedi ve Hello Kitty'nin elini tuttu. Hello Kitty bundan sonra evde koşarken etrafına dikkat etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "En iyi arkadaşının üzülmesini istemedi"
   - Cümle 6: «En iyi arkadaşının üzülmesini istemedi ve ondan özür diledi.»
   - Açıklama: İkiz kardeş olarak tanıtılan Mimi'ye birden 'en iyi arkadaşı' deniyor ve kimin kastedildiği karışıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "En iyi arkadaşının üzülmesini"
   - Cümle 6: «En iyi arkadaşının üzülmesini istemedi ve ondan özür diledi.»
   - Açıklama: İkiz kardeş Mimi birden 'en iyi arkadaşı' diye anılıyor; kimi gösterdiği karışıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0137` birebir aynı, `@degisim: şakalaşmak -> oynamak` (tutuyorsan), ardından `@onarim: 9d3a780e50f0ac91a88b8d4dfe6ca53362a0c8c2`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0139 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0139
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'limon', fiil 'üflemek', sıfat 'hafif'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: resmin üstüne küçük sarı şeyler düşüyordu | çiçekleri üfledi ve güneşli bir yere oturdu
@tohum: hello_kitty-0139
Hello Kitty parkta bir ağacın gölgesinde oturuyordu. Yeni arkadaşlarına hediye olarak resim çiziyordu. Ama resmin üstüne küçük sarı şeyler düşüyordu. Hello Kitty bunların ne olduğunu çok merak etti. Bir tanesini eline aldı. O sarı şey çok hafif ve yumuşaktı. Sonra başını kaldırıp ağaca baktı. Dallarda limon sarısı küçük çiçekler vardı. Rüzgar esince çiçekler dallardan resmin üstüne düşüyordu. Hello Kitty resmin temiz kalmasını çok istedi. Çiçekleri resmin üstünden yavaşça üfledi. Sonra çimenlerde güneşli bir yere oturdu. Artık resmin üstüne hiç çiçek düşmedi. Hello Kitty resmini çizmeye mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına hediye olarak"
   - Cümle 2: «Yeni arkadaşlarına hediye olarak resim çiziyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "resmin üstüne küçük sarı şeyler düşüyordu"
   - Cümle 3: «Ama resmin üstüne küçük sarı şeyler düşüyordu.»
   - Açıklama: Resme hafif çiçeklerin düşmesi üflenip biten önemsiz bir olay; çocuğun önemseyeceği bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0139` birebir aynı, ardından `@onarim: 7210fa54f0bbdbc50d82a57b3e46ba249e1d4a27`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0140 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0140
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'süpürge', fiil 'yarışmak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: oyunda elmalı turta yapacaktı ama elması yoktu | kozalakları toplayıp taşın üstüne dizdi
@tohum: hello_kitty-0140
@degisim: yarışmak -> toplamak
Rüzgar ağaçların arasında yavaş yavaş esiyordu. Hello Kitty ailece kamp yapıyordu ve çadırın yanında yemek oyunu oynuyordu. Oyunda sağlıklı bir elmalı turta yapacaktı, ama hiç elması yoktu. Hello Kitty etrafına baktı ve yerde yuvarlak kozalaklar gördü. Kozalaklar küçük elmalara benziyordu. Kuru bir dalı süpürge gibi kullandı ve kozalakları bir yere topladı. Sonra kozalakları düz bir taşın üstüne daire şeklinde dizdi. Taşın üstünde yuvarlak bir kozalak turtası oldu. Hello Kitty turtasına baktı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty ailece kamp yapıyordu"
   - Cümle 2: «Hello Kitty ailece kamp yapıyordu ve çadırın yanında yemek oyunu oynuyordu.»
   - Açıklama: 'Ailece' çoğul özne ister; tekil özneyle 'ailesiyle' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0140` birebir aynı, `@degisim: yarışmak -> toplamak` (tutuyorsan), ardından `@onarim: 0341e44ab6392739977d79f7f3b9a89c4560ccc0`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0142 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0142
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'bant', fiil 'paylaşmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: koşarken kardeşinin uçurtmasına bastı ve yırttı | özür diledi ve kutunun bandıyla yırtık yeri yapıştırdı
@tohum: hello_kitty-0142
@degisim: düzenli -> yapışkan
Hello Kitty ile Mimi parkta uçurtma uçurmaya hazırlanıyordu. Çimenlerin üstünde, evde ailece yaptıkları kurabiyelerin kutusu duruyordu. Hello Kitty koşarken Mimi'nin kağıt uçurtmasına bastı ve uçurtma yırtıldı. Mimi yırtık uçurtmaya baktı ve çok üzüldü. Hello Kitty hemen kardeşinin yanına oturdu ve ondan özür diledi. Sonra kurabiye kutusuna baktı. Kutunun kapağında yapışkan bir bant vardı. Hello Kitty bandı kapaktan yavaşça çekip aldı. Yırtık yeri bu bantla dikkatlice yapıştırdı. Rüzgar esince uçurtma yükseldi. Mimi sevindi ve Hello Kitty'ye sarıldı. Sonra ikisi kurabiyeleri paylaştı ve uçurtmayı mutlu mutlu uçurdu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra kurabiye kutusuna baktı"
   - Cümle 6: «Sonra kurabiye kutusuna baktı.»
   - Açıklama: Tohum özelliği kurabiye yapmayı sevmek; kurabiye yalnız bandı veren kutu olarak geçiyor, özellik işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0142` birebir aynı, `@degisim: düzenli -> yapışkan` (tutuyorsan), ardından `@onarim: 08d1ea296b70268f86f43f83e33ce77a8bfc8dea`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0144 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0144
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'pul', fiil 'ovmak', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: cam ıslaktı ve kar görünmüyordu | camı parmağıyla ovdu ve kara baktı
@tohum: hello_kitty-0144
@degisim: güvenli -> ıslak
Dışarıda sessizce kar yağıyordu. Hello Kitty kar tanesi şeklinde kurabiyeler yapmak istiyordu. Ama mutfak çok sıcaktı ve pencerenin camı ıslaktı. Hello Kitty camın arkasındaki kar tanelerini hiç göremedi. Camı parmağıyla yavaşça ovdu. Camda küçük, temiz bir yer açıldı. Sonra oradan dışarıya yakından baktı. Camın dışına küçük kar taneleri pul gibi yapışmıştı. Hepsi küçük yıldızlara benziyordu. Hello Kitty onların şeklini iyice gördü ve çok sevindi. Hello Kitty bundan sonra ıslak camı hep parmağıyla sildi.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kar tanesi şeklinde kurabiyeler yapmak istiyordu"
   - Cümle 2: «Hello Kitty kar tanesi şeklinde kurabiyeler yapmak istiyordu.»
   - Açıklama: Tohumdaki kurabiye özelliği yalnız anılıyor, hikayede kurabiye yapılmıyor ve sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kurabiye özelliği yalnız istek olarak anılıyor, sorunun çözümünde hiç kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kar tanesi şeklinde kurabiyeler yapmak istiyordu"
   - Cümle 2: «Hello Kitty kar tanesi şeklinde kurabiyeler yapmak istiyordu.»
   - Açıklama: Kurabiye yapma isteği kuruluyor ama hikayede bir daha kullanılmıyor ve karı görmekle bağı söylenmiyor.
   - Açıklama: Kurabiye isteği kuruluyor ama hikayede hiç kullanılmıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ama mutfak çok sıcaktı"
   - Cümle 3: «Ama mutfak çok sıcaktı ve pencerenin camı ıslaktı.»
   - Açıklama: Hello Kitty büyüksüz sıcak mutfakta; güvenli kullanım satırı kurabiyenin bir büyükle yapıldığını söyler.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kar taneleri pul gibi"
   - Cümle 8: «Camın dışına küçük kar taneleri pul gibi yapışmıştı.»
   - Açıklama: 'Pul gibi' benzetmesi ve 'pul' kelimesi 3 yaşındaki bir çocuk için bilinmeyen, mecazlı bir anlatım.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kar taneleri pul gibi yapışmıştı"
   - Cümle 8: «Camın dışına küçük kar taneleri pul gibi yapışmıştı.»
   - Açıklama: 'Pul gibi' benzetmesi 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Pul gibi' benzetmesi 3 yaşındaki çocuğun bilmeyeceği bir kelimeye dayanıyor.
6. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hello Kitty bundan sonra ıslak camı hep parmağıyla sildi"
   - Cümle 11: «Hello Kitty bundan sonra ıslak camı hep parmağıyla sildi.»
   - Açıklama: Hikayenin açtığı kurabiye hedefine hiç dönülmüyor, son bu hedefe ulaşmadan kapanıyor.
   - Açıklama: Kurulan kurabiye hedefine dönülmüyor ve son cümle sıcak bir kapanış vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0144` birebir aynı, `@degisim: güvenli -> ıslak` (tutuyorsan), ardından `@onarim: e8660388e7f30f62e2e4268d6459822c5371d7c0`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0148 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0148
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'tost', fiil 'yapıştırmak', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: tabaktaki kurabiye birden kayboldu | tostu kaldırıp altına yapışan kurabiyeyi buldu
@tohum: hello_kitty-0148
Ormandaki kamp yerinde Hello Kitty ailece çadırın önünde oturuyordu. Turuncu tabağında ballı bir tost ve yıldız şeklinde bir kurabiye vardı. Kurabiyeyi evde ailece yapmışlardı. Tostunu biraz yedi ve geri koydu, ama sonra kurabiyeyi göremedi. Hello Kitty kurabiyenin nereye gittiğini çok merak etti. Önce tabağın yanına ve otların arasına baktı. Kurabiye orada da yoktu. Sonra tostu eline aldı ve altına baktı. Tostun altından küçük bir yıldız ucu görünüyordu. Bal, kurabiyeyi tostun altına yapıştırmıştı. Kurabiyeyi yavaşça çekip aldı. Hello Kitty çok sevindi, çünkü kurabiyesini bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty ailece çadırın önünde oturuyordu"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty ailece çadırın önünde oturuyordu.»
   - Açıklama: 'Ailece' tekil özne Hello Kitty ile uyumsuz; 'Hello Kitty ailesiyle' olmalı.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Hello Kitty ailece çadırın önünde oturuyordu"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty ailece çadırın önünde oturuyordu.»
   - Açıklama: Başlıktaki Yan alanı boş olduğu hâlde aile üyeleri sahnede bulunuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kurabiyeyi evde ailece yapmışlardı"
   - Cümle 3: «Kurabiyeyi evde ailece yapmışlardı.»
   - Açıklama: Kurabiyenin evde ailece yapılması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama sonra kurabiyeyi göremedi"
   - Cümle 4: «Tostunu biraz yedi ve geri koydu, ama sonra kurabiyeyi göremedi.»
   - Açıklama: Kurabiyenin kaybolması ancak 4. cümlede söyleniyor, ilk 3 cümlede sorun yok.
   - Açıklama: Kurabiyenin kaybolması sorunu ilk 3 cümlede değil 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0148` birebir aynı, ardından `@onarim: 519adbf7320fc88400503851e969708b7422b83e`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0152 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0152
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'köpük', fiil 'serpmek', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: hava bulutluydu ve gökkuşağı yoktu | güneş çıkınca havaya su serpti ve gökkuşağı gördü
@tohum: hello_kitty-0152
@degisim: köpük -> su
Bir sabah Hello Kitty ormanda ailece kamp yapıyordu. Yeni arkadaşlarına bir gökkuşağı resmi çizmek istiyordu. Ama hava bulutluydu ve gökyüzünde hiç gökkuşağı yoktu. Hello Kitty bir süre gökyüzüne baktı ve bekledi. Sonunda bulutların arasından güneş çıktı. Gökkuşağı için güneş ve su damlaları gerekiyordu. Hello Kitty su şişesini aldı ve suyu avucuna döktü. Sonra suyu havaya serpti. Su damlalarının arasında küçük bir gökkuşağı göründü. Hello Kitty onun renklerine dikkatle baktı. Sonra kağıdına renkli bir gökkuşağı çizdi. Hello Kitty bitmiş resmine bakıp mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına bir gökkuşağı resmi"
   - Cümle 2: «Yeni arkadaşlarına bir gökkuşağı resmi çizmek istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız amaç olarak anılıyor, çözümde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama hava bulutluydu ve gökyüzünde hiç gökkuşağı yoktu"
   - Cümle 3: «Ama hava bulutluydu ve gökyüzünde hiç gökkuşağı yoktu.»
   - Açıklama: Gökkuşağı resmi çizmek için gökte gökkuşağı görmek gerekmez; sorun akla yatkın değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty bir süre gökyüzüne baktı ve bekledi"
   - Cümle 4: «Hello Kitty bir süre gökyüzüne baktı ve bekledi.»
   - Açıklama: Çözüm bulutlu hava sebebine yönelmiyor; figür yalnız bekliyor ve havanın açılması şansa bırakılıyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonunda bulutların arasından güneş çıktı"
   - Cümle 5: «Sonunda bulutların arasından güneş çıktı.»
   - Açıklama: Sorunun sebebi olan bulutlar Hello Kitty'nin bir eylemiyle değil, kendiliğinden kalkıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonunda bulutların arasından güneş çıktı"
   - Cümle 5: «Sonunda bulutların arasından güneş çıktı.»
   - Açıklama: Çözüm için gereken güneş figürün eylemi olmadan kendiliğinden gelip çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0152` birebir aynı, `@degisim: köpük -> su` (tutuyorsan), ardından `@onarim: 3ac458318c73130c4bfab98768d62a3247daebbe`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0154 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0154
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'üzüm', fiil 'ulaşmak', sıfat 'berrak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: top yüksek bir dala takıldı | annesinden yardım istedi ve topu geri aldı
@tohum: hello_kitty-0154
@degisim: berrak -> güneşli
Hello Kitty parkta top oynuyordu. Topu ona yeni bir arkadaşı vermişti. Hava güneşli ve sıcaktı. Ama top yükseğe zıpladı ve bir ağacın dalına takıldı. Hello Kitty zıpladı, ama topa ulaşamadı. Annesi yakında, ağacın gölgesinde üzüm yiyordu. Hello Kitty annesinin yanına gitti ve yardım istedi. Annesi kalktı ve uzun koluyla topu daldan aldı. Hello Kitty annesine sarıldı ve teşekkür etti. Sonra annesini de oyuna çağırdı. İkisi birlikte top oynadı. Hello Kitty çok mutluydu, çünkü topu geri almıştı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Topu ona yeni bir arkadaşı vermişti"
   - Cümle 2: «Topu ona yeni bir arkadaşı vermişti.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir kez anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız arka plan bilgisi olarak geçiyor, olayda işe yaramıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Topu ona yeni bir arkadaşı vermişti"
   - Cümle 2: «Topu ona yeni bir arkadaşı vermişti.»
   - Açıklama: Kartın yanlar bölümünde olmayan bir arkadaş karakter hikayeye giriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Topu ona yeni bir arkadaşı vermişti"
   - Cümle 2: «Topu ona yeni bir arkadaşı vermişti.»
   - Açıklama: Topu veren yeni arkadaş işe yarayacakmış gibi kuruluyor ama hikayede hiç kullanılmıyor.
   - Açıklama: Topu veren yeni arkadaş bir daha geçmiyor ve olayda işlevi yok.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama top yükseğe zıpladı ve bir ağacın dalına takıldı.»
   - Açıklama: Topun dala takılması sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0154` birebir aynı, `@degisim: berrak -> güneşli` (tutuyorsan), ardından `@onarim: 6cd9587e9828fbece29223f7f3ac5cf6683b8367`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0156 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0156
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'havlu', fiil 'kurulanmak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: yukarıdan su damladı ve başı ıslandı | suyun yapraklardan geldiğini buldu ve turtayı güneşe taşıdı
@tohum: hello_kitty-0156
@degisim: hazırlıklı -> yumuşak
Bir sabah Hello Kitty babasıyla parkta piknik yapıyordu. İkisi ağacın gölgesinde oturuyordu ve önlerinde elmalı bir turta vardı. Birden yukarıdan su damladı ve Hello Kitty'nin başı ıslandı. Ama gökyüzünde hiç bulut yoktu. Hello Kitty bu suyun nereden geldiğini bilmek istedi. Başını kaldırdı ve ağacın dallarına baktı. Yapraklar sabahki yağmurdan ıslaktı. Rüzgar esince onlardan aşağı su dökülüyordu. "Baba, su ağaçtan geliyor!" dedi Hello Kitty. Sonra en sevdiği turtayı ıslanmasın diye güneşli çimenlere taşıdı. Babası sepetten yumuşak bir havlu çıkardı ve kızına verdi. Hello Kitty havluyla güzelce kurulandı. Çok sevindi, çünkü suyun nereden geldiğini bulmuş ve turtasını kurtarmıştı.
```

**Hakem bulguları (3):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sonra en sevdiği turtayı ıslanmasın diye güneşli çimenlere taşıdı"
   - Cümle 10: «Sonra en sevdiği turtayı ıslanmasın diye güneşli çimenlere taşıdı.»
   - Açıklama: Suyun kaynağını bulma sorununun yanına turtayı kurtarma diye ikinci bir sorun ekleniyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra en sevdiği turtayı ıslanmasın diye güneşli çimenlere taşıdı"
   - Cümle 10: «Sonra en sevdiği turtayı ıslanmasın diye güneşli çimenlere taşıdı.»
   - Açıklama: Sorun Hello Kitty'nin başının ıslanması iken çözüm turtayı taşımaya yöneliyor ve kurulanma babanın havlusuyla oluyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babası sepetten yumuşak bir havlu çıkardı"
   - Cümle 11: «Babası sepetten yumuşak bir havlu çıkardı ve kızına verdi.»
   - Açıklama: Daha önce kurulmamış sepet ve havlu, ıslak başı kurutma çözümünü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0156` birebir aynı, `@degisim: hazırlıklı -> yumuşak` (tutuyorsan), ardından `@onarim: 4a0c8080a54c27c393f556172844ddbb48165ea4`, sonra gövde.
