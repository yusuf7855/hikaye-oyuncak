# Editör görevi (onarım): Hello Kitty, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar35.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0113 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0113
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'toz', fiil 'geçmek', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: kuru otlar hemen kırıldı | ağaç gölgesinde yumuşak yeşil otlarla bileklik ördü
@tohum: hello_kitty-0113
Bir sabah Hello Kitty ormandaki kamp yerindeydi. İlk kez yeni arkadaşlarına vermek için otlardan bileklik yapmayı denedi. Ama yerdeki otlar kuru ve toz doluydu, hemen kırıldı. Hello Kitty kırık otlara baktı ve biraz düşündü. Sonra tozlu yoldan geçti ve yakındaki bir ağacın gölgesine gitti. Orada yumuşak ve yeşil otlar vardı. Hello Kitty birkaç yeşil otu nazikçe kopardı. Otları yavaş yavaş birbirine ördü. Yeşil otlar hiç kırılmadı. Sonunda küçük ve güzel bir bileklik oldu. Hello Kitty çok sevindi, çünkü ilk bilekliğini kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlarına vermek için"
   - Cümle 2: «İlk kez yeni arkadaşlarına vermek için otlardan bileklik yapmayı denedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor; arkadaşlar olaya hiç girmiyor ve özellik sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız amaç olarak anılıyor, hikayenin sorununda ya da çözümünde işe yaramıyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hello Kitty çok sevindi, çünkü ilk bilekliğini kendisi yapmıştı"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü ilk bilekliğini kendisi yapmıştı.»
   - Açıklama: Bileklik yeni arkadaşlara verilmek için yapılıyordu ama hikaye bu hedefe dönmeden, bileklik hiç verilmeden bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0113` birebir aynı, ardından `@onarim: 2f42f208cacdd7f818e2607dc33393cc79b586d5`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0116 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0116
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'muffin', fiil 'boşalmak', sıfat 'temkinli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: rüzgar kutuyu devirdi ve kurabiyeler çimene döküldü | elindeki son kurabiyeyi ikiye bölüp annesiyle paylaştı
@tohum: hello_kitty-0116
@degisim: muffin -> kutu
Parkta ağaçların gölgesinde bir piknik örtüsü vardı. Hello Kitty ile annesi evde birlikte yaptıkları kurabiyeleri getirmişti. Ama rüzgar örtüyü kaldırdı ve kurabiye kutusu devrildi. Kutu boşaldı ve kurabiyeler yere döküldü. Bir tek kurabiye Hello Kitty'nin elinde kalmıştı. "Yere düşen kurabiyeleri yiyemeyiz," dedi temkinli annesi ve onları topladı. Annesi daha hiç kurabiye yememişti. Hello Kitty son kurabiyeyi yavaşça ikiye kırdı. "Al, anneciğim, bu yarısı senin," dedi Hello Kitty. "Teşekkürler, tatlım," dedi annesi ve kurabiyeyi yedi. Hello Kitty çok mutlu oldu, çünkü son kurabiyeyi annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi temkinli annesi"
   - Cümle 6: «"Yere düşen kurabiyeleri yiyemeyiz," dedi temkinli annesi ve onları topladı.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Temkinli' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty son kurabiyeyi yavaşça ikiye kırdı"
   - Cümle 8: «Hello Kitty son kurabiyeyi yavaşça ikiye kırdı.»
   - Açıklama: Sorun dökülen kurabiyeler iken çözüm bu sebebe yönelmiyor, sonradan eklenen annenin hiç yememiş olmasına cevap veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0116` birebir aynı, `@degisim: muffin -> kutu` (tutuyorsan), ardından `@onarim: 73fca1ffd90eaf28a22fc004c208095d7f879217`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0117 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0117
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'su', fiil 'tatmak', sıfat 'konuşkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesi çok susamıştı ama şişesinde su kalmamıştı | kendi dolu şişesini annesine verdi
@tohum: hello_kitty-0117
Ormandaki kamp yerinde sıcak bir gündü. Hello Kitty ile annesi küçük bir yürüyüşten yeni dönmüştü. Annesi çok susamıştı, ama şişesi bomboştu. "Suyum bitti, kızım," dedi annesi. Konuşkan Hello Kitty yürürken çok konuşmuştu. Bu yüzden kendi suyunu hiç içmemişti. Hello Kitty her şeyini arkadaşlarıyla paylaşırdı. Şimdi de dolu şişesini hemen annesine uzattı. "Al, anneciğim, benimki dolu," dedi Hello Kitty. Annesi serin suyu tattı ve gülümsedi. "Çok güzel, teşekkür ederim," dedi annesi. Sonra ikisi ağaçların gölgesinde oturup dinlendi. Hello Kitty çok sevindi, çünkü annesine yardım edebilmişti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Konuşkan Hello Kitty yürürken"
   - Cümle 5: «Konuşkan Hello Kitty yürürken çok konuşmuştu.»
   - Açıklama: Kartın özellikler alanında olmayan konuşkanlık ikinci bir huy olarak ekleniyor.
   - Açıklama: Tohumdaki özellik arkadaş/iyilik; kartın özellikler alanında olmayan konuşkanlık ikinci bir özellik olarak ekleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty her şeyini arkadaşlarıyla paylaşırdı"
   - Cümle 7: «Hello Kitty her şeyini arkadaşlarıyla paylaşırdı.»
   - Açıklama: Tohum özelliği yeni arkadaş edinmeyi sevmek iken paylaşma olarak değiştirilmiş.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Annesi serin suyu tattı"
   - Cümle 10: «Annesi serin suyu tattı ve gülümsedi.»
   - Açıklama: Çok susamış biri suyu tatmaz, içer; fiil anlama uymuyor.
   - Açıklama: Susamış anne suyu içer; 'tattı' fiili burada yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0117` birebir aynı, ardından `@onarim: 56edfac238b8dae751f8bf98985855c993b3b458`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0118 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0118
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'yüzük', fiil 'inmek', sıfat 'heyecanlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: ikizinin büyük yüzüğü yokuştan aşağı yuvarlandı | ikizinin elini tuttu, yokuştan indi ve yüzüğü buldu
@tohum: hello_kitty-0118
Ormandaki kamp yerinde Hello Kitty ile Mimi yaprak topluyordu. Mimi'nin parmağında yeni ve büyük bir yüzük vardı. Birden yüzük parmağından kaydı ve küçük bir yokuştan aşağı yuvarlandı. Mimi çok üzüldü ama bir şey demedi. Hello Kitty ikizinin üzgün yüzünü gördü. Hemen arkadaşına elini uzattı. "Gel, Mimi, birlikte arayalım," dedi Hello Kitty. İkisi el ele yavaşça yokuştan indi. Aşağıda bir sürü sarı yaprak vardı. Hello Kitty yaprakları tek tek kaldırdı. Sonunda bir yaprağın altında parlayan yüzüğü buldu. Mimi onu sevinçle aldı ve heyecanlı bir sesle teşekkür etti. Hello Kitty bundan sonra ikizi üzülünce hemen yanına gitti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hemen arkadaşına elini uzattı"
   - Cümle 6: «Hemen arkadaşına elini uzattı.»
   - Açıklama: Mimi ikizi olarak tanıtıldı; 'arkadaşına' yanlış kelime.
   - Açıklama: Bir önceki cümlede ikizi olan Mimi için 'arkadaş' kelimesi yanlış anlamda kullanılmış.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hemen arkadaşına elini uzattı"
   - Cümle 6: «Hemen arkadaşına elini uzattı.»
   - Açıklama: Mimi bir cümle önce ve planda ikiz olarak anılıyor ama burada arkadaş deniyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi el ele yavaşça yokuştan indi"
   - Cümle 8: «İkisi el ele yavaşça yokuştan indi.»
   - Açıklama: Güvenli kullanım satırına aykırı olarak iki küçük çocuk bir büyük olmadan ormanda yokuştan aşağı iniyor.
4. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "bundan sonra ikizi üzülünce hemen yanına gitti"
   - Cümle 13: «Hello Kitty bundan sonra ikizi üzülünce hemen yanına gitti.»
   - Açıklama: 'Bundan sonra' ile anlatılan alışkanlık için geniş zamanlı geçmiş ('giderdi') gerekirken tek seferlik -dı kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0118` birebir aynı, ardından `@onarim: 5218a11c1c8223922bd421d63734eba64dd3fd18`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0119
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kadife', fiil 'açmak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: tebeşir kesesi sıkı bir düğümle bağlıydı | düğüme dikkatle baktı ve yavaşça açtı
@tohum: hello_kitty-0119
Bir sabah Hello Kitty parkta yeni bir şey denemek istedi. İlk kez tebeşirle parkın yoluna resim çizecekti. Ama kadife kese sıkı bir düğümle bağlıydı. Hello Kitty ipi hızlı hızlı çekti. Düğüm daha da sıkıştı. Hello Kitty durdu ve düğüme dikkatle baktı. Sonra ipin ucunu buldu ve düğümü yavaşça açtı. Kese renkli tebeşirlerle doluydu. Hello Kitty yere büyük bir güneş çizdi. Güneşin yanına, yeni arkadaşlarla oynamak için bir seksek çizdi. Resim çok güzel oldu. Hello Kitty bundan sonra düğümleri acele etmeden açtı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlarla oynamak için bir seksek çizdi"
   - Cümle 10: «Güneşin yanına, yeni arkadaşlarla oynamak için bir seksek çizdi.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlarla oynamak için"
   - Cümle 10: «Güneşin yanına, yeni arkadaşlarla oynamak için bir seksek çizdi.»
   - Açıklama: Arkadaş özelliği düğüm sorununun çözümünde işe yaramıyor, yalnız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0119` birebir aynı, ardından `@onarim: 282c05aefac8b046910f1c1d00e73603186393fd`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0121 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0121
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'menekşe', fiil 'giymek', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: çimenlerde küçük sarı parçalar vardı | parçaları tanıdı ve delik cebini buldu
@tohum: hello_kitty-0121
Hello Kitty parkta çiçeklerin arasında yürüyordu. Üstüne yeni ve esnek bir yelek giymişti. Birden menekşelerin yanında küçük sarı parçalar gördü. Parçalar çimenlerde arkasına doğru uzun bir çizgi yapıyordu. Hello Kitty bu izi çok merak etti. Eğildi ve bir parçayı yakından kokladı. Bu, onun sabah yaptığı yıldız kurabiyelerin bir parçasıydı! Hemen cebine baktı. Cep çok dolmuştu ve altı yırtılmıştı. Parçalar yürürken oradan tek tek düşmüştü. Hello Kitty kendi izini bulduğu için güldü. Hello Kitty bundan sonra yiyeceklerini cebine değil, küçük bir kutuya koydu.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çimenlerde küçük sarı parçalar vardı"
   - Cümle 0 (plan satırı): «çimenlerde küçük sarı parçalar vardı | parçaları tanıdı ve delik cebini buldu»
   - Açıklama: Çimende parçalar olması çocuğun önemseyeceği bir sorun değil, merak edilen bir iz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni ve esnek bir yelek"
   - Cümle 2: «Üstüne yeni ve esnek bir yelek giymişti.»
   - Açıklama: 'Esnek' kelimesi 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden menekşelerin yanında küçük sarı parçalar gördü.»
   - Açıklama: İlk üç cümlede bir sorun söylenmiyor; yalnız çimende parçalar görülüyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden menekşelerin yanında küçük sarı parçalar gördü"
   - Cümle 3: «Birden menekşelerin yanında küçük sarı parçalar gördü.»
   - Açıklama: Çimendeki sarı parçalar çocuğun önemseyeceği açık bir sorun değil; asıl kayıp olan kurabiyeler de hiç geri alınmıyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çimenlerde arkasına doğru uzun"
   - Cümle 4: «Parçalar çimenlerde arkasına doğru uzun bir çizgi yapıyordu.»
   - Açıklama: 'Arkasına' zamirinin kimi ya da neyi gösterdiği belli değil.
   - Açıklama: 'Arkasına' zamirinin kimin arkasını gösterdiği belli değil.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yaptığı yıldız kurabiyelerin bir parçasıydı"
   - Cümle 7: «Bu, onun sabah yaptığı yıldız kurabiyelerin bir parçasıydı!»
   - Açıklama: Tamlama eki eksik; 'yıldız kurabiyelerinin' olmalı.
   - Açıklama: Tamlama eki eksik; 'yıldız kurabiyelerinin bir parçası' olmalı.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Parçalar yürürken oradan"
   - Cümle 10: «Parçalar yürürken oradan tek tek düşmüştü.»
   - Açıklama: 'Yürürken' parçalara bağlanıyor; parçalar yürümez, 'Hello Kitty yürürken' olmalı.
   - Açıklama: 'Yürürken' fiili öznesi olan parçalara uymuyor; yürüyen Hello Kitty.
8. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 12: «Hello Kitty bundan sonra yiyeceklerini cebine değil, küçük bir kutuya koydu.»
   - Açıklama: Kurabiyeler geri gelmiyor ve cep onarılmıyor; açık bir hedefe doyurucu biçimde ulaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0121` birebir aynı, ardından `@onarim: d0539a3ca84e259e8545060be2c64e6bbdcb0996`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0122 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0122
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: sırayla oynamak
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'pankek', fiil 'ayrılmak', sıfat 'şirin'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: tek bir top vardı ve kardeşi oyundan ayrıldı | ilk sırayı kardeşine verdi ve sırayla oynadılar
@tohum: hello_kitty-0122
@degisim: pankek -> top
Hello Kitty ile Mimi ormandaki kamp yerinde top oynuyordu. Topu şirin bir sepetin içine atıyorlardı. Ama bir tek top vardı ve ikisi de hep atmak istiyordu. Mimi utangaçtı, bir şey demedi ve oyundan ayrıldı. Bir ağacın altına oturdu ve topa baktı. Hello Kitty kardeşinin yanına gitti. Topu Mimi'nin eline verdi. "İlk sıra sende, en iyi arkadaşım, sonra ben atarım," dedi Hello Kitty. Mimi topu attı ve top sepete girdi. "Sıra sende, Hello Kitty!" dedi Mimi sevinçle. Hello Kitty de attı ve top sepetin içine düştü. İki kardeş sırayla atış yapıp oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "İlk sıra sende, en iyi arkadaşım"
   - Cümle 8: «"İlk sıra sende, en iyi arkadaşım, sonra ben atarım," dedi Hello Kitty.»
   - Açıklama: Hello Kitty kardeşine 'en iyi arkadaşım' diye sesleniyor; hitap kişiye uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en iyi arkadaşım, sonra ben"
   - Cümle 8: «"İlk sıra sende, en iyi arkadaşım, sonra ben atarım," dedi Hello Kitty.»
   - Açıklama: Hello Kitty kardeşi Mimi'ye 'en iyi arkadaşım' diye sesleniyor; kelime ilişkiye uymuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşım, sonra ben"
   - Cümle 8: «"İlk sıra sende, en iyi arkadaşım, sonra ben atarım," dedi Hello Kitty.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği yalnız kelime olarak geçiyor, işe yarar biçimde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşım"
   - Cümle 8: «"İlk sıra sende, en iyi arkadaşım, sonra ben atarım," dedi Hello Kitty.»
   - Açıklama: Tohumdaki 'yeni arkadaşlar edinme' özelliği yalnız hitap sözü olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0122` birebir aynı, `@degisim: pankek -> top` (tutuyorsan), ardından `@onarim: c7694c4b387a7e39df66dd7c44b64f05364d9414`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0123
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'önlük', fiil 'mırıldanmak', sıfat 'yalnız'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası tatlı kutusunu nereye koyduğunu unutmuştu | kokuyu izleyip kutuyu ağacın arkasında buldu
@tohum: hello_kitty-0123
Ormanda rüzgar hafifçe esiyordu. Hello Kitty'nin babası kamp yerinde önlüğüyle piknik sofrasını hazırlıyordu. Ama tatlı kutusunu nereye koyduğunu unutmuştu. Babası bir şarkı mırıldanarak her yere baktı. Hello Kitty babasının kutuyu yalnız aradığını gördü ve yanına koştu. Hello Kitty en çok elmalı turtayı severdi ve kokusunu hemen tanırdı. Burnunu havaya kaldırdı ve güzel kokuyu izledi. Koku büyük bir ağacın arkasından geliyordu. Kutu orada, serin gölgede duruyordu. Babası onu sabah oraya kendisi koymuştu. Hello Kitty kutuyu iki eliyle sofraya getirdi. Babası güldü ve önlüğünü komik bir şekilde salladı. Sonra baba kız sofraya oturdu ve pikniğe mutlu mutlu başladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir şarkı mırıldanarak"
   - Cümle 4: «Babası bir şarkı mırıldanarak her yere baktı.»
   - Açıklama: 'Mırıldanmak' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0123` birebir aynı, ardından `@onarim: 854ebe5564490face6ac6929f4b829ca1172f171`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0124 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: çamurda yuvarlak ve dalgalı bir iz vardı | izin tabaktan kaldığını buldu
@tohum: hello_kitty-0124
@degisim: kanepe -> örtü
Parkta çimenler ıslak ve çamurluydu. Hello Kitty annesiyle ağacın altında, bir örtünün üstünde oturuyordu. Birden çamurda yuvarlak ve büyük bir iz gördü. İzin kenarları küçük dalgalar gibiydi. "Anne, bunu ne yaptı?" diye sordu Hello Kitty. "Bil bakalım," dedi annesi gülerek. Hello Kitty örtüye baktı. Orada en sevdiği elmalı turtanın tabağı duruyordu. Tabağın kenarı da dalgalıydı! Hello Kitty tabağı kaldırdı ve kenarını izin yanına tuttu. İkisi aynıydı. "Tabağı önce çamura koydun!" dedi Hello Kitty. "Evet, sonra örtüye taşıdım," dedi annesi. "Anneciğim, bu bilmece beni çok eğlendirdi!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği elmalı turtanın tabağı"
   - Cümle 8: «Orada en sevdiği elmalı turtanın tabağı duruyordu.»
   - Açıklama: Tohumdaki turta sevgisi yalnız anılıyor, iz bilmecesinin çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Tabağı önce çamura koydun"
   - Cümle 12: «"Tabağı önce çamura koydun!" dedi Hello Kitty.»
   - Açıklama: Annenin turta tabağını çamura koyması akla yatkın değil ve çamurdaki iz çocuğun önemseyeceği gerçek bir sorun değil.
   - Açıklama: Annenin turta tabağını önce çamura koyması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0124` birebir aynı, `@degisim: kanepe -> örtü` (tutuyorsan), ardından `@onarim: 3f30f6691082703fb4f7bd56f81a50c561016935`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0125 (deneme 2 -> 3)

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
Bir sabah Hello Kitty parka kırmızı topacını getirdi. Onu çimenlerin üstünde hızla çevirdi. Ama topaç yumuşak çimenlerde hemen durdu ve devrildi. Hello Kitty bir daha denedi. Topaç bu kez tuhaf bir şekilde sallandı ve yine yere düştü. Onun için düz ve sert bir yer gerekiyordu. Hello Kitty çantasına baktı. İçinde evde yaptığı kurabiyelerin kutusu vardı. Kutunun kapağı düz ve sertti. Hello Kitty kapağı çimenin üstüne koydu. Topacı onun ortasında çevirdi. Kırmızı topaç bu kez uzun uzun döndü. Sevinçle ellerini çırptı. Sonra Hello Kitty orada mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty parka kırmızı topacını getirdi"
   - Cümle 1: «Bir sabah Hello Kitty parka kırmızı topacını getirdi.»
   - Açıklama: Küçük çocuk parka tek başına gidip orada büyüksüz oynuyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun için düz ve sert"
   - Cümle 6: «Onun için düz ve sert bir yer gerekiyordu.»
   - Açıklama: 'Onun' topacı mı Hello Kitty'yi mi gösteriyor belli değil ve 'bu yüzden' anlamıyla da okunabiliyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sevinçle ellerini çırptı"
   - Cümle 13: «Sevinçle ellerini çırptı.»
   - Açıklama: Öznesiz cümlede son özne topaç olduğu için ellerini kimin çırptığı belli değil.
   - Açıklama: Özne yazılmamış; önceki cümlenin öznesi topaç olduğu için kimin el çırptığı belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0125` birebir aynı, ardından `@onarim: 4ec09ce8d3e7ce4fe8c28ec2988116a160567f7f`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0126 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0126
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'marul', fiil 'serinlemek', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: yakın bir çalının altından hışır hışır bir ses geldi | çalıya gidip sesi yapan küçük kediyi buldu
@tohum: hello_kitty-0126
Bir sabah parkta hava çok sıcaktı. Hello Kitty ağacın gölgesinde marullu sandviçini yiyordu. Birden yakın bir çalının altından hışır hışır bir ses geldi. Hello Kitty bu sesi çok merak etti. Çalıya yavaşça gitti ve eğilip baktı. Gölgede küçük bir kedi serinliyordu. Kedi kuru yapraklarla oynarken o ses çıkıyordu. Hello Kitty yeni arkadaşlar edinmeyi çok severdi. Hemen kediye sandviçinden bir parça ekmek verdi. Kedi ekmeği yedi ve Hello Kitty'nin yanına oturdu. İkisi gölgede birlikte dinlendi. Hello Kitty bundan sonra parka gelirken yanına bir sandviç daha aldı.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakın bir çalının altından hışır hışır bir ses geldi"
   - Cümle 3: «Birden yakın bir çalının altından hışır hışır bir ses geldi.»
   - Açıklama: Bir sesin merak edilmesi gerçek bir sorun değil; ortada çözülmesi gereken bir dert yok.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Gölgede küçük bir kedi serinliyordu"
   - Cümle 6: «Gölgede küçük bir kedi serinliyordu.»
   - Açıklama: Başlıktaki Yan alanı boş ama kartın yanlar bölümünde olmayan bir kedi olaya katılıyor.
   - Açıklama: Başlığın Yan alanı boş olduğu hâlde kartın yanlar bölümünde olmayan bir kedi olaya katılıyor.
   - Açıklama: Başlıkta yan yok ama olaya katılan bir kedi karakteri ekleniyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Gölgede küçük bir kedi serinliyordu"
   - Cümle 6: «Gölgede küçük bir kedi serinliyordu.»
   - Açıklama: Kartta hayvan arkadaş yok; kart dışı bir hayvan karakter eklenmiş.
   - Açıklama: Kartta hayvan arkadaşları yok; kapalı dünyaya yeni bir hayvan karakter ekleniyor.
   - Açıklama: Kartın yanlar bölümünde hayvan arkadaş yok; kararlar hayvan arkadaşlarını dışlıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni arkadaşlar edinmeyi"
   - Cümle 8: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: 'Arkadaş edinmek' soyut bir anlatım ve 'edinmek' küçük çocuğun bilmediği bir kelime.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 8: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: 'Arkadaş edinmek' soyut bir ifade ve 3 yaşındaki çocuk için zor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen kediye sandviçinden bir parça ekmek verdi"
   - Cümle 9: «Hemen kediye sandviçinden bir parça ekmek verdi.»
   - Açıklama: Tanımadığı sokak hayvanına yaklaşıp yiyecek vermek taklit edilince tehlikeli.
   - Açıklama: Tanımadığı bir hayvana yaklaşıp yiyecek vermek çocuğun taklit edebileceği tehlikeli bir davranış.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen kediye sandviçinden bir parça"
   - Cümle 9: «Hemen kediye sandviçinden bir parça ekmek verdi.»
   - Açıklama: Çocuğun tanımadığı bir sokak hayvanına yaklaşıp elle yem vermesi taklit edilince tehlikeli olabilir.
8. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hello Kitty bundan sonra parka gelirken yanına bir sandviç daha aldı"
   - Cümle 12: «Hello Kitty bundan sonra parka gelirken yanına bir sandviç daha aldı.»
   - Açıklama: Son cümle olaydan çıkan bir ders değil, sonraki günlere atlayan bir eylem.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0126` birebir aynı, ardından `@onarim: 1ac8c8c58974bf7ba47634e292b36417ed45017e`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0127 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0127
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'pirinç', fiil 'keşfetmek', sıfat 'kolay'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: tatlı kutusu yüksek raftaydı ve önünde pirinç torbası vardı | babasından yardım istedi ve babası kutuyu indirdi
@tohum: hello_kitty-0127
@degisim: keşfetmek -> bulmak
Hello Kitty mutfakta en sevdiği elmalı turtayı arıyordu. Sonunda kutusunu en üst rafta buldu. Ama raf çok yüksekti ve kutunun önünde büyük bir pirinç torbası vardı. Hello Kitty uzandı, ama rafa yetişemedi. Babası o sırada salonda oturuyordu. "Babacığım, bana yardım eder misin?" diye sordu Hello Kitty. Babası hemen mutfağa geldi. "Tabii, bu benim için çok kolay," dedi babası. Önce ağır pirinç torbasını kenara çekti. Sonra kutuyu indirdi ve masaya koydu. Babası iki tabak getirdi ve komik bir yüz yaptı. Hello Kitty kahkahayla güldü. "Teşekkürler, babacığım, şimdi birlikte yiyelim!" dedi Hello Kitty.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonunda kutusunu en üst rafta buldu"
   - Cümle 2: «Sonunda kutusunu en üst rafta buldu.»
   - Açıklama: Kutunun önünde büyük bir pirinç torbası varken Hello Kitty'nin kutuyu aşağıdan görüp bulması çelişkili.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve komik bir yüz yaptı"
   - Cümle 11: «Babası iki tabak getirdi ve komik bir yüz yaptı.»
   - Açıklama: 'Yüz yapmak' doğal bir kullanım değil; 'komik bir surat yaptı' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babası iki tabak getirdi ve komik bir yüz yaptı"
   - Cümle 11: «Babası iki tabak getirdi ve komik bir yüz yaptı.»
   - Açıklama: Komik yüz sorunla ilgisiz, olaydan çıkmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0127` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 9bb47ce1a736a3b60a4313cf4a3c0ad91314445d`, sonra gövde.
