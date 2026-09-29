# Editör görevi (onarım): Hello Kitty, onarım partisi 28

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar28.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0049 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0049
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'defter', fiil 'doyurmak', sıfat 'pembe'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: babası resmi anlamadı çünkü turtada elma yoktu | turtanın üstüne kırmızı elmalar çizip yeniden gösterdi
@tohum: hello_kitty-0049
Bir sabah Hello Kitty ile babası evde resim oyunu oynuyordu. Hello Kitty pembe defterine en sevdiği elmalı turtayı çizdi. Ama resimde hiç elma yoktu, bu yüzden babası resmin ne olduğunu anlamadı. "Bu bir şapka mı?" diye sordu babası. Hello Kitty bu komik soruya çok güldü. Hemen kırmızı bir kalem aldı. Turtanın üstüne üç küçük elma çizdi. Defteri babasına yeniden gösterdi. "Bu bir elmalı turta!" dedi babası sevinçle. Sonra resmi yiyormuş gibi yaptı ve karnını tuttu. "Bu resim beni çok doyurdu, kızım," dedi babası. Hello Kitty çok sevindi, çünkü babası çizdiği turtayı sonunda anlamıştı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "turtanın üstüne kırmızı elmalar çizip"
   - Cümle 0 (plan satırı): «babası resmi anlamadı çünkü turtada elma yoktu | turtanın üstüne kırmızı elmalar çizip yeniden gösterdi»
   - Açıklama: Planda elmaları çizdiği söyleniyor ama gövdede bu eylem yazılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0049` birebir aynı, ardından `@onarim: e0bd7edda847a3efda7be099238ee23080782be0`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0069 (deneme 5 -> 6)

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
@plan: kedinin başı çok büyüktü ve köfte için yer kalmadı | büyük çizgileri silip daha küçük bir baş çizdi
@tohum: hello_kitty-0069
@degisim: düşünceli -> küçük
Parkta, yolun kenarında yumuşak bir toprak vardı. Hello Kitty toprağa köfte yiyen bir kedi çiziyordu. Ama kedinin başını çok büyük çizmişti ve köfte için yer kalmadı. Hello Kitty resmi yeni arkadaşlarına gösterecekti ve kediyi köftesiz bırakmak istemedi. Toprağa baktı ve biraz düşündü. Sonra büyük çizgileri eliyle sildi. Bu kez daha küçük, yuvarlak bir baş çizdi. Şimdi toprakta köfte için de yer vardı. Hello Kitty başa iki göz, uzun bıyıklar ve iki sivri kulak ekledi. En son kedinin önüne bir köfte çizdi. Hello Kitty çok sevindi, çünkü resimdeki kedinin artık köftesi vardı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Parkta, yolun kenarında yumuşak"
   - Cümle 1: «Parkta, yolun kenarında yumuşak bir toprak vardı.»
   - Açıklama: Güvenli kullanım satırına aykırı olarak Hello Kitty yanında büyük olmadan yol kenarında tek başına oynuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty resmi yeni arkadaşlarına gösterecekti"
   - Cümle 4: «Hello Kitty resmi yeni arkadaşlarına gösterecekti ve kediyi köftesiz bırakmak istemedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "resmi yeni arkadaşlarına gösterecekti"
   - Cümle 4: «Hello Kitty resmi yeni arkadaşlarına gösterecekti ve kediyi köftesiz bırakmak istemedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0069` birebir aynı, `@degisim: düşünceli -> küçük` (tutuyorsan), ardından `@onarim: 63f4e40bb3a767af5fb232ab9782447b5e5fe5ae`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0078 (deneme 5 -> 6)

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
@plan: babası sırayı unutuyor ve topu hep kendisi tutuyordu | babasına sırayla atmayı önerdi
@tohum: hello_kitty-0078
@degisim: enerjik -> hızlı
Bir sabah Hello Kitty babasıyla parkta, fıskiyenin yanında top oynuyordu. Ama babası sırayı hep unutuyordu. Topu havaya atıyor ve hızlı hızlı yine kendisi tutuyordu. Hello Kitty'ye hiç sıra gelmedi. Babası topu tuttu ve Hello Kitty'nin yanına koştu. Hello Kitty onu gülümseyerek karşıladı. "Baba, iki arkadaş gibi sırayla atalım, şimdi sıra bende," dedi Hello Kitty. "Haklısın, unuttum!" dedi babası ve topu ona verdi. Hello Kitty topu babasına attı ve babası onu tuttu. Sonra babası topu yavaşça Hello Kitty'ye geri attı. Hello Kitty onu iki eliyle yakaladı. Hello Kitty çok sevindi, çünkü artık sıra ikisine de geliyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babası topu tuttu ve Hello Kitty'nin yanına koştu"
   - Cümle 5: «Babası topu tuttu ve Hello Kitty'nin yanına koştu.»
   - Açıklama: Babanın Hello Kitty'nin yanına koşması sebepsiz ve olay akışından çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0078` birebir aynı, `@degisim: enerjik -> hızlı` (tutuyorsan), ardından `@onarim: a3cc658bb5e854b38e5110e4101c1bfdde66d373`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0079 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: mutfaktan bilinmeyen bir ses geldi | kurabiye kitabının durduğu tezgaha baktı ve sesi buldu
@tohum: hello_kitty-0079
Mutfağın penceresinden serin bir rüzgar esiyordu. Hello Kitty odasında otururken mutfaktan hışır hışır bir ses duydu. Bu sesi çok merak etti. Yavaşça mutfağa yürüdü. Ses, kağıttan geliyor gibiydi. Hello Kitty kurabiye yaparken hep bir kitaba bakardı. O kitap pencerenin önündeki tezgahta dururdu. Hemen tezgaha baktı. Rüzgar kitabın sayfalarını tek tek çeviriyordu. Ses buradan geliyordu. Hello Kitty pencereyi kapattı ve dağınık sayfaları düzeltti. Sonra kitabı sıkıca kucakladı. Hello Kitty çok sevindi, çünkü sesi bulmuş ve kitabını korumuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar kitabın sayfalarını tek tek çeviriyordu"
   - Cümle 9: «Rüzgar kitabın sayfalarını tek tek çeviriyordu.»
   - Açıklama: Rüzgarın sayfaları çevirmesi çocuğun önemseyeceği gerçek bir sorun değil; sesi bulup pencereyi kapatınca olay bitiyor.
   - Açıklama: Sorun rüzgarın sayfa çevirmesinden çıkan önemsiz bir ses; pencere kapanınca bitiyor ve çocuk için gerçek bir sorun kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve dağınık sayfaları düzeltti"
   - Cümle 11: «Hello Kitty pencereyi kapattı ve dağınık sayfaları düzeltti.»
   - Açıklama: Rüzgar sayfaları yalnız çevirmişti; kitabın sayfaları dağınık olmaz, kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0079` birebir aynı, ardından `@onarim: e7316e4f32bbf1485ae2f4c958184022bcd763fe`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0084 (deneme 4 -> 5)

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
@plan: piyanonun tuşlarına küçük bir dal sıkıştı | piyanoyu ters çevirip salladı ve dalı düşürdü
@tohum: hello_kitty-0084
@degisim: gülüşmek -> gülmek
Ormanda rüzgar yavaşça esiyordu. Hello Kitty kamp yerinde yeni arkadaşlar edinmek için bir şarkı hazırlıyordu. Ama ağaçtan küçük bir dal düştü ve rengarenk piyanosunun tuşlarına sıkıştı. Piyano artık güzel ses vermiyordu. Hello Kitty tuşlara dikkatle baktı ve dalı gördü. Piyanoyu yavaşça ters çevirdi ve biraz salladı. Küçük dal çimenlere düştü. Piyano yeniden güzel ses verdi. Hello Kitty şarkısını baştan sona çaldı ve neşeyle güldü. Hello Kitty çok mutluydu, çünkü şarkısı artık hazırdı.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde yeni arkadaşlar"
   - Cümle 2: «Hello Kitty kamp yerinde yeni arkadaşlar edinmek için bir şarkı hazırlıyordu.»
   - Açıklama: Hello Kitty ormandaki kamp yerinde yanında hiçbir büyük olmadan tek başına; güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde"
   - Cümle 2: «Hello Kitty kamp yerinde yeni arkadaşlar edinmek için bir şarkı hazırlıyordu.»
   - Açıklama: Güvenli kullanım satırına aykırı olarak Hello Kitty ormandaki kamp yerinde yanında bir büyük olmadan tek başına.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni arkadaşlar edinmek için"
   - Cümle 2: «Hello Kitty kamp yerinde yeni arkadaşlar edinmek için bir şarkı hazırlıyordu.»
   - Açıklama: 'Edinmek' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Edinmek' 3 yaşındaki çocuğun bilmediği soyut bir fiil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlar edinmek için bir şarkı hazırlıyordu"
   - Cümle 2: «Hello Kitty kamp yerinde yeni arkadaşlar edinmek için bir şarkı hazırlıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlar edinmek için bir şarkı hazırlıyordu"
   - Cümle 2: «Hello Kitty kamp yerinde yeni arkadaşlar edinmek için bir şarkı hazırlıyordu.»
   - Açıklama: Yeni arkadaş edinme amacı kuruluyor ama hikayede hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0084` birebir aynı, `@degisim: gülüşmek -> gülmek` (tutuyorsan), ardından `@onarim: 9fcc647444258ac62e46362e87dbe0c03c35004d`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0088 (deneme 3 -> 4)

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
@plan: rüzgar yapbozun son parçasını uçurdu | turta tabağını kaldırıp parçayı altında buldu
@tohum: hello_kitty-0088
Hello Kitty ormandaki kamp yerinde annesiyle yapboz yapıyordu. Yanlarında annesinin yaptığı elmalı turta duruyordu. Ama birden rüzgar esti ve yapbozun son parçası uçtu. Annesi yerinden kalktı ve eteğini salladı. Parça eteğinden düşmedi. Hello Kitty kararlıydı, yapbozu bitirmek istiyordu. Hello Kitty yapbozun yanındaki turta tabağına baktı. "Anne, belki parça tabağın altına kaydı," dedi Hello Kitty. Tabağı yavaşça kaldırdı ve altında küçük parçayı gördü. Hello Kitty parçayı hemen yerine koydu. "Anne, yapboz bitti, şimdi turta zamanı!" dedi Hello Kitty sevinçle.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi yerinden kalktı ve eteğini salladı"
   - Cümle 4: «Annesi yerinden kalktı ve eteğini salladı.»
   - Açıklama: Annenin eteğini sallaması sebepsiz ve işlevsiz bir ara olay; parçanın eteğe düştüğüne dair hiçbir ipucu yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kararlıydı, yapbozu bitirmek"
   - Cümle 6: «Hello Kitty kararlıydı, yapbozu bitirmek istiyordu.»
   - Açıklama: Tohumdaki özellik turta; kararlılık ikinci bir özellik olarak ekleniyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "belki parça tabağın altına kaydı"
   - Cümle 8: «"Anne, belki parça tabağın altına kaydı," dedi Hello Kitty.»
   - Açıklama: Parça rüzgarla uçtuğu söyleniyor ama yerinde duran tabağın altından çıkıyor; bu akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0088` birebir aynı, ardından `@onarim: f5c208cbf5e065c9203ea0f8d4fa0af685707cc8`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0089 (deneme 3 -> 4)

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
Parkta Hello Kitty ile babası küplerle bir kule yapıyordu. Yanlarında evde birlikte yaptıkları kurabiyelerle dolu bir sepet vardı. Ama ikisi aynı anda küp koyunca kule yıkıldı. Babası bir an sustu, sonra güldü. "Böyle olmuyor, Hello Kitty," dedi babası. Hello Kitty sepetten bir kurabiye çıkardı. "Önce sen koy, sonra kurabiyeyi bana ver," dedi Hello Kitty. Bu çok basit bir oyundu. Babası küpünü koydu ve kurabiyeyi Hello Kitty'ye verdi. Hello Kitty de küpünü koydu ve kurabiyeyi geri uzattı. Kule yavaş yavaş yükseldi ve bu kez hiç yıkılmadı. Sonra kurabiyeyi ikiye böldüler ve oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurabiyeyi sıra işareti yapıp"
   - Cümle 0 (plan satırı): «ikisi aynı anda küp koyunca kule yıkıldı | kurabiyeyi sıra işareti yapıp sırayla küp koydular»
   - Açıklama: Plandaki 'sıra işareti' soyut bir ifade; 3 yaşındaki çocuk için anlaşılır değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0089` birebir aynı, ardından `@onarim: ae4afbbbeca30de83d67b7f758c47402e274d76a`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0095 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0095
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mısır', fiil 'duymak', sıfat 'yumuşacık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: rüzgar kurabiye kutusunu masadan düşürdü | çalıdan gelen sesi izleyip kutuyu buldu
@tohum: hello_kitty-0095
@degisim: mısır -> kutu
Rüzgar sert esiyordu. Hello Kitty babasıyla ormandaki kamp yerindeydi. Birden rüzgar masadaki kurabiye kutusunu yere düşürdü. Hello Kitty etrafa baktı ama kutuyu göremedi ve üzüldü. Kutuda evde yaptığı kurabiyeler vardı. Sonra yakındaki bir çalıdan hışır hışır bir ses duydu. "Baba, bu ses ne, birlikte bakalım mı?" diye sordu Hello Kitty. Babası başını salladı ve ikisi çalıya yürüdü. Kutu çalının dibindeydi ve yapraklara sürtünüyordu. Sesi yapan kutuydu! Kutu yumuşacık çimenlere düştüğü için kurabiyeler kırılmamıştı. Hello Kitty en büyük kurabiyeyi babasına verdi. "Çok güzel olmuş, teşekkürler," dedi babası. İkisi masaya döndü ve kurabiyeleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve yapraklara sürtünüyordu"
   - Cümle 9: «Kutu çalının dibindeydi ve yapraklara sürtünüyordu.»
   - Açıklama: 'Sürtünmek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0095` birebir aynı, `@degisim: mısır -> kutu` (tutuyorsan), ardından `@onarim: 4cb49591c0a748c38c5d9d722d6ffacde7b21897`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0097 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0097
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'biftek', fiil 'düzeltmek', sıfat 'oynak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: çadırdan tık tık diye bir ses geldi | kardeşiyle sesi arayıp oynak direği düzeltti
@tohum: hello_kitty-0097
@degisim: biftek -> direk
Ormandaki kamp yerinde Hello Kitty ile Mimi ailece çadırın önünde oturuyordu. Birden çadırdan tık tık diye bir ses geldi. Hello Kitty sesin nereden geldiğini çok merak etti. Mimi ise biraz çekindi ve yerinden kalkmadı. Hello Kitty kardeşinin elini tuttu. "Gel, Mimi, belki orada yeni bir arkadaş var," dedi Hello Kitty. Mimi başını salladı ve onunla yürüdü. İkisi çadırın arkasına gitti. Orada çadırın direği oynaktı ve rüzgarda bir taşa vuruyordu. Hello Kitty direği toprağa sıkıca bastırdı ve düzeltti. Ses hemen kesildi. Hello Kitty çok sevindi, çünkü sesi kardeşi Mimi ile bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mimi ailece çadırın önünde"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty ile Mimi ailece çadırın önünde oturuyordu.»
   - Açıklama: Sahnede yalnız iki kardeş varken 'ailece' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: İki kardeş için 'ailece' kelimesi yerinde kullanılmamış.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden çadırdan tık tık diye bir ses geldi"
   - Cümle 2: «Birden çadırdan tık tık diye bir ses geldi.»
   - Açıklama: Ormanda kaynağı bilinmeyen ve Mimi'yi çekindiren bir ses küçük çocuk için korkutucu olabilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi ise biraz çekindi"
   - Cümle 4: «Mimi ise biraz çekindi ve yerinden kalkmadı.»
   - Açıklama: 'Çekinmek' soyut bir kelime; 3 yaşındaki çocuk bilmez.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "belki orada yeni bir arkadaş var"
   - Cümle 6: «"Gel, Mimi, belki orada yeni bir arkadaş var," dedi Hello Kitty.»
   - Açıklama: Çocuklar büyük olmadan bilinmeyen bir sesin kaynağına, orada bir yabancı olabileceğini düşünerek gidiyor; güvenli kullanım satırı yabancıyla gitmeyi yasaklıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0097` birebir aynı, `@degisim: biftek -> direk` (tutuyorsan), ardından `@onarim: 22fd3de7c9be89128bfcc2ff719e5b4430b32759`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0099 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0099
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'eldiven', fiil 'çekilmek', sıfat 'yeşil'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: eldiven büyük olduğu için top içinden düşüyordu | eldiveni çıkarıp topu elleriyle yakaladı
@tohum: hello_kitty-0099
Bir sabah Hello Kitty babasıyla parkta top yakalama oyunu oynuyordu. Babası ona büyük, yeşil bir eldiven vermişti. Ama eldiven çok büyüktü ve top her seferinde içinden düşüyordu. Babası gülümsedi ve birkaç adım geri çekildi. Top yine eldivenden kaydı ve çimenlere yuvarlandı. Hello Kitty biraz düşündü. Evde en sevdiği elmalı turtanın tabağını hep iki eliyle taşırdı. Sonra eldiveni çıkardı ve ellerini tabak tutar gibi açtı. Babası topu yavaşça attı. Hello Kitty topu sıkıca yakaladı. Babası sevinçle ellerini çırptı. Hello Kitty çok sevindi, çünkü sonunda topu yakalamıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babası gülümsedi ve birkaç adım geri çekildi"
   - Cümle 4: «Babası gülümsedi ve birkaç adım geri çekildi.»
   - Açıklama: Babanın geri çekilmesi sebepsiz ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0099` birebir aynı, ardından `@onarim: a4c6201d354027eafd1e8fa17a0e410b0f4c74f6`, sonra gövde.
