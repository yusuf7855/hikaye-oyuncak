# Editör görevi (onarım): Hello Kitty, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0035 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0035
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'sebze', fiil 'karışmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: ıslak boyalar birbirine karıştı ve resim bozuldu | yeni kağıtta sebzeleri birbirinden uzağa boyadı
@tohum: hello_kitty-0035
Parkta, ağaçların gölgesinde Hello Kitty yeni arkadaşlarına resim boyuyordu. Kağıda kırmızı bir domates ile turuncu bir havuç boyadı. Ama iki sebze çok yakındı ve ıslak boyalar birbirine karıştı. Kağıtta yalnız büyük bir leke kaldı. Hello Kitty lekeli resme baktı ve çok mutsuz oldu. Biraz düşündü ve yeni bir kağıt aldı. Önce domatesi kağıdın bir köşesine boyadı. Sonra havucu öbür köşeye, çok uzağa boyadı. Bu kez boyalar birbirine hiç değmedi. Kırmızı domates ve turuncu havuç kağıtta güzelce duruyordu. Hello Kitty çok sevindi, çünkü artık güzel bir hediyesi vardı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşlarına resim boyuyordu"
   - Cümle 1: «Parkta, ağaçların gölgesinde Hello Kitty yeni arkadaşlarına resim boyuyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız resmin gerekçesi olarak anılıyor, çözümde işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kırmızı bir domates ile turuncu bir havuç boyadı"
   - Cümle 2: «Kağıda kırmızı bir domates ile turuncu bir havuç boyadı.»
   - Açıklama: Domatesin resmi yapılır; 'domates boyadı' domatesin kendisini boyamak anlamına gelir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0035` birebir aynı, ardından `@onarim: 819de21490394f91e1b6eb9261652c99c94a3fca`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0037 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0037
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'ip', fiil 'tartmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: ipler arkadaydı ve önlüğü bağlayamadı | ipleri iki yandan öne çekip önde bağladı
@tohum: hello_kitty-0037
Dışarıda soğuk bir rüzgar esiyordu. Hello Kitty yemek oyununda en sevdiği elmalı turta için elma tartacaktı. Ama önlüğünü bağlayamadı, çünkü ipleri arkadaydı. Arkasını hiç göremiyordu. Biraz düşündü ve ipleri iki yandan öne çekti. İpler çok uzundu ve önde buluştu. Hello Kitty iki ipi sıkıca bağladı. Sonra küçük terazide üç kırmızı elmayı tarttı. Elmaları büyük bir kaseye tek tek koydu. Hello Kitty çok mutluydu, çünkü önlüğünü tek başına bağlamış ve oyuna başlamıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dışarıda soğuk bir rüzgar esiyordu"
   - Cümle 1: «Dışarıda soğuk bir rüzgar esiyordu.»
   - Açıklama: Hikaye evin içinde geçerken dışarıdaki rüzgar yeri kurmuyor ve olayda hiçbir işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği elmalı turta için"
   - Cümle 2: «Hello Kitty yemek oyununda en sevdiği elmalı turta için elma tartacaktı.»
   - Açıklama: Tohumdaki turta özelliği yalnız bahane olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0037` birebir aynı, ardından `@onarim: a29116bb6c51f8d30865b655a3c520f4a1390e3e`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0038 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0038
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'hediye', fiil 'yürümek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: eski sepetin sapı koptu ve annesi üzüldü | kurdelesini çıkarıp sapı sepete bağladı
@tohum: hello_kitty-0038
Parkta çimenlerin üstünde güneş parlıyordu. Hello Kitty annesiyle ağaçların gölgesine doğru yürüyordu. Annesinin elindeki piknik sepeti çok eskiydi ve sapı birden koptu. Bu sepet, annesinin çok sevdiği bir hediyeydi. Annesi sepete baktı ve üzüldü. Hello Kitty, arkadaşlarının kopan oyuncaklarını hep kurdeleyle düzeltirdi. Hemen kırmızı kurdelesini çıkardı. Sonra onunla sapı sepete sıkıca bağladı. Annesi sepeti yavaşça kaldırdı. Sap yerinde kaldı ve sepet düşmedi. Annesi gülümsedi ve kızına sarıldı. Sonra Hello Kitty ile annesi gölgede mutlu mutlu piknik yaptı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarının kopan oyuncaklarını hep kurdeleyle düzeltirdi"
   - Cümle 6: «Hello Kitty, arkadaşlarının kopan oyuncaklarını hep kurdeleyle düzeltirdi.»
   - Açıklama: Tohumdaki arkadaş özelliği karttaki gibi yeni arkadaş edinme ya da iyi davranma olarak değil, kartta olmayan bir oyuncak onarma alışkanlığı olarak kullanılıyor.
   - Açıklama: Kartın 'yeni arkadaşlar edinmeyi sever' özelliği yerine kartta olmayan bir onarma alışkanlığı gerekçe olarak ekleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty, arkadaşlarının kopan oyuncaklarını hep kurdeleyle düzeltirdi"
   - Cümle 6: «Hello Kitty, arkadaşlarının kopan oyuncaklarını hep kurdeleyle düzeltirdi.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, arkadaşlar yalnız arka plan bilgisi olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0038` birebir aynı, ardından `@onarim: f23025a85467f0884d2299676d4c08f4f55ac831`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0039 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0039
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'meşe', fiil 'katmak', sıfat 'umutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: hafif sepet her atışta yere devriliyordu | kurabiye kutusunu sepetin dibine koydu
@tohum: hello_kitty-0039
@degisim: umutlu -> ağır
Hello Kitty ile Mimi, bir kutu kurabiyeyle büyük meşe ağacının altına oturmuştu. İkisi küçük bir topu sepete atma oyunu oynuyordu. Ama sepet çok hafifti ve her atışta yere devriliyordu. Top çimenlere kaçtı ve Mimi güldü. "Sepet yine düştü, Hello Kitty!" dedi Mimi. Hello Kitty biraz düşündü. Sonra evde yaptığı kurabiyelerin ağır kutusunu aldı. Hello Kitty kutuyu sepetin dibine koydu ve ağırlık kattı. Mimi topu yeniden sepete attı. Top içine düştü ve bu kez sepet hiç kıpırdamadı. "Oldu, Hello Kitty!" dedi Mimi sevinçle. İkisi sırayla atmaya devam etti. Hello Kitty bundan sonra hafif bir sepete hep ağır bir şey koydu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "koydu ve ağırlık kattı"
   - Cümle 8: «Hello Kitty kutuyu sepetin dibine koydu ve ağırlık kattı.»
   - Açıklama: 'Ağırlık katmak' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Ağırlık katmak' kalıplaşmış, soyut bir anlatım; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0039` birebir aynı, `@degisim: umutlu -> ağır` (tutuyorsan), ardından `@onarim: b91a7e06e3f3b9a2ae6a0d4e6e5f36c8ee920fe6`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0044 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0044
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kalıp', fiil 'esnemek', sıfat 'sakar'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: ekmek çok kalındı ve kalıp ekmeği kesemedi | ekmeği ikiye ayırıp ince parçaya kalıbı bastırdı
@tohum: hello_kitty-0044
@degisim: sakar -> ince
Ormanda, kamp yerinde Hello Kitty'nin annesi esnedi ve dinlenmek için uzandı. Hello Kitty annesine kalıpla kalp şeklinde bir sandviç yapmak istedi. Ama ekmek çok kalındı ve kalıp ekmeği kesemedi. Hello Kitty arkadaşlarına sandviç yaparken kalın ekmeği hep ikiye ayırırdı. Şimdi de ekmeği yavaşça ikiye böldü. İnce parçaya kalıbı iki eliyle bastırdı. Bu kez güzel bir kalp çıktı. Hello Kitty üç kalp daha yaptı ve hepsini bir tabağa dizdi. "Anne, sana bir sürprizim var!" dedi Hello Kitty. Annesi tabağı görünce güldü. "Çok teşekkürler, kızım!" dedi annesi. Sonra ikisi sandviçleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarına sandviç yaparken kalın ekmeği hep ikiye ayırırdı"
   - Cümle 4: «Hello Kitty arkadaşlarına sandviç yaparken kalın ekmeği hep ikiye ayırırdı.»
   - Açıklama: Kartın 'yeni arkadaşlar edinmeyi sever' özelliği kullanılmıyor; arkadaş kökü yalnız kartta olmayan bir alışkanlığın gerekçesi olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0044` birebir aynı, `@degisim: sakar -> ince` (tutuyorsan), ardından `@onarim: 8c668f2951b0b24772f9d9d436b3266c7634f357`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0045 (deneme 4 -> 5)

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
@plan: ince sap büküldü ve hamurdan lale devrildi | kalın bir sap yapıp çiçeği tepsiye düz koydu
@tohum: hello_kitty-0045
@degisim: planlamak -> hatırlamak
Hello Kitty mutfakta oyun hamuruyla oynuyordu. İlk kez hamurdan bir lale yapmayı denedi. Ama lale ayakta durunca ince sap büküldü ve lale devrildi. Çiçek, yapraklar ve sap birbirine yapıştı ve karmakarışık oldu. Hello Kitty hamura baktı ve biraz düşündü. Kurabiyelerin tepside hep düz durduğunu hatırladı. Hamuru yeniden ayırdı. Bu kez kalın bir sapı tepsiye düz koydu. Yanına iki yaprak, en üste de kırmızı bir çiçek yerleştirdi. Lale tepside güzelce durdu ve hiç düşmedi. Hello Kitty bundan sonra hamur lalelerini hep düz yaptı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "lale ayakta durunca"
   - Cümle 3: «Ama lale ayakta durunca ince sap büküldü ve lale devrildi.»
   - Açıklama: Hamurdan lale için 'ayakta durmak' öznesine uygun değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu kez kalın bir sapı tepsiye düz koydu"
   - Cümle 8: «Bu kez kalın bir sapı tepsiye düz koydu.»
   - Açıklama: Lalenin ayakta durma hedefi çözülmüyor, laleyi yatırarak sorundan kaçılıyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hello Kitty bundan sonra hamur lalelerini hep düz yaptı"
   - Cümle 11: «Hello Kitty bundan sonra hamur lalelerini hep düz yaptı.»
   - Açıklama: Ayakta duran lale hedefi bırakılıp lale yatırılarak sorun atlatılıyor ve hikaye sevinç ya da sıcak bir kapanış olmadan bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0045` birebir aynı, `@degisim: planlamak -> hatırlamak` (tutuyorsan), ardından `@onarim: 066c3910f9a496c067bf572c7b2c040f26ee44f6`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0046 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0046
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'turşu', fiil 'soğumak', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: kavanozun kapağı çok sıkıydı | babasından yardım istedi ve kapak açıldı
@tohum: hello_kitty-0046
@degisim: soğumak -> paylaşmak
Hello Kitty babasıyla parkta, ağacın gölgesinde piknik yapıyordu. Örtünün üstünde çıtır patatesler ve bir kavanoz turşu vardı. Hello Kitty turşu almak istedi ama kavanozun kapağı çok sıkıydı. İki eliyle çevirdi ama kapak hiç dönmedi. "Baba, lütfen bu kapağı açar mısın?" diye sordu Hello Kitty. Babası kapağı bir kez çevirdi ve kavanoz hemen açıldı. "Teşekkürler, babacığım!" dedi Hello Kitty. Arkadaşlarına yaptığı gibi, ilk turşuyu babasına uzattı. Hello Kitty ile babası turşu ve patatesleri mutlu mutlu paylaştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Arkadaşlarına yaptığı gibi, ilk turşuyu"
   - Cümle 8: «Arkadaşlarına yaptığı gibi, ilk turşuyu babasına uzattı.»
   - Açıklama: Sahnede olmayan arkadaşlara yapılan alışkanlığa gönderme soyut ve çocuk için anlaşılmaz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Arkadaşlarına yaptığı gibi, ilk turşuyu babasına uzattı"
   - Cümle 8: «Arkadaşlarına yaptığı gibi, ilk turşuyu babasına uzattı.»
   - Açıklama: Tohumdaki arkadaş özelliği sorun çözüldükten sonra eklenmiş, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0046` birebir aynı, `@degisim: soğumak -> paylaşmak` (tutuyorsan), ardından `@onarim: 611f930be65dfeb68d84a589d1221b222dc8aa47`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0048 (deneme 4 -> 5)

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
Evde, kahverengi mutfak masasında Hello Kitty ile annesi tuz hamuru yapıyordu. Hello Kitty yeni arkadaşına hamurdan bir kedi hediye etmek istedi. Ama hamur çok suluydu ve ellerine yapışıyordu. "Anne, biraz un ve tuz alabilir miyim?" diye sordu Hello Kitty. Annesi unu ve tuzu ona uzattı. Hello Kitty hamura bir kaşık un ve biraz tuz döktü. Sonra hamuru güzelce yoğurdu. Hamur artık ellerine yapışmadı. Hello Kitty küçük bir kedi yaptı. Annesi kediyi görünce gülümsedi. Hello Kitty çok sevindi, çünkü hediyesi tam istediği gibi olmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşına hamurdan bir kedi hediye etmek istedi"
   - Cümle 2: «Hello Kitty yeni arkadaşına hamurdan bir kedi hediye etmek istedi.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız bir amaç olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0048` birebir aynı, ardından `@onarim: caa429e7422ef0243c37e44b9feee3bae79f54bb`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0052 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0052
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'yatak', fiil 'girmek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: küçük sarı tabak yataktan düşüp kaybolmuştu | yatağın altına girdi ve tabağı buldu
@tohum: hello_kitty-0052
Bir sabah Hello Kitty odasında yemek oyunu oynuyordu. Oyun hamurundan dört küçük kurabiye yaptı. Ama yatağın üstünde yalnız üç tabak vardı, küçük sarı tabak eksikti. Hello Kitty yere eğildi ve yatağın altına girdi. Küçük tabak yataktan kaymış ve oraya düşmüştü. Hello Kitty tabağı aldı ve yatağın altından çıktı. Onu öteki tabakların yanına bıraktı. Artık dört tabak da yan yanaydı. Hello Kitty her tabağa bir kurabiye koydu. Sonra yemek oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yere eğildi ve yatağın altına girdi"
   - Cümle 4: «Hello Kitty yere eğildi ve yatağın altına girdi.»
   - Açıklama: Hello Kitty tabağın nerede olduğuna dair hiçbir ipucu olmadan doğrudan yatağın altına giriyor; çözüm sebepsiz geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0052` birebir aynı, ardından `@onarim: 4c4588637532e64f3c519d3aba9869ae9efea509`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0053 (deneme 3 -> 4)

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
@plan: top kavanoza çarptı ve kavanoz çimenlerde kayboldu | yerdeki izin peşinden gidip kavanozu buldu
@tohum: hello_kitty-0053
Hello Kitty ile Mimi parkta top oynuyordu. Hello Kitty evde yaptığı kurabiyelerin kavanozunu örtüye bırakmıştı. Birden Mimi'nin attığı top kavanoza çarptı ve kavanoz çimenlerde dönerek kayboldu. "Kurabiyeler nereye gitti?" diye sordu utangaç Mimi yavaşça. Hello Kitty yere dikkatle baktı. Çimenlerde ince, uzun bir iz vardı. İki kardeş izin peşinden yürüdü. İz, çiçeklerin arasında bitti. Kavanoz orada, kapağı kapalı duruyordu. Hello Kitty kavanozu aldı ve içine baktı. Kavanoz da kurabiyeler de sağlamdı. "Bak, Mimi, kurabiyelerimiz burada!" dedi Hello Kitty. İki kardeş çok sevindi, çünkü kurabiyelerini yeniden bulmuşlardı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kavanoz çimenlerde dönerek kayboldu"
   - Cümle 3: «Birden Mimi'nin attığı top kavanoza çarptı ve kavanoz çimenlerde dönerek kayboldu.»
   - Açıklama: Örtüdeki bir kavanozun topa çarpınca çimenlerde yuvarlanıp gözden kaybolması akla pek yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0053` birebir aynı, ardından `@onarim: 926b80de686446218d5d11168573c95e85b50b68`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0056 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0056
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kolye', fiil 'affetmek', sıfat 'hareketsiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesinin kolyesi düştü çünkü kilidi açılmıştı | dikkatle aradı ve kolyeyi kurabiye sepetinde buldu
@tohum: hello_kitty-0056
@degisim: affetmek -> aramak
Bir sabah Hello Kitty annesiyle parkta piknik yapıyordu. İkisi evde birlikte yaptıkları kurabiyeleri yiyordu. Birden annesinin kolyesi boynundan düştü, çünkü kilidi açılmıştı. "Kolyemi bulamıyorum, kızım," dedi annesi üzgün bir sesle. "Üzülme, anne, ben ararım," dedi Hello Kitty. Hello Kitty önce bir an hareketsiz durdu ve etrafa dikkatle baktı. Sonra kurabiye sepetinde parlayan bir şey gördü. Kolye kurabiyelerin arasına düşmüştü. Hello Kitty kolyeyi aldı ve annesine verdi. "Teşekkür ederim, canım kızım," dedi annesi ve ona sarıldı. Hello Kitty bundan sonra kaybolan şeyleri önce yakında arardı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kaybolan şeyleri önce yakında arardı"
   - Cümle 11: «Hello Kitty bundan sonra kaybolan şeyleri önce yakında arardı.»
   - Açıklama: 'Yakında' burada 'az sonra' anlamına da okunabiliyor; 'yakınlarda' ya da 'yanında' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "önce yakında arardı"
   - Cümle 11: «Hello Kitty bundan sonra kaybolan şeyleri önce yakında arardı.»
   - Açıklama: 'Yakında' çocuk için 'az sonra' anlamında okunur; 'yakınlarda' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0056` birebir aynı, `@degisim: affetmek -> aramak` (tutuyorsan), ardından `@onarim: 74c23e77cfe3ab7b694b0d5b9c6b799006792f7a`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0060 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0060
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'yağ', fiil 'yavaşlamak', sıfat 'kısa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesi yavaşladı, çünkü çantası çok ağırdı | yağ şişesini kendi çantasına aldı
@tohum: hello_kitty-0060
Hello Kitty annesiyle ormandaki kamp yerine yürüyordu. Yol kısaydı ama annesi yavaşladı, çünkü çantası çok ağırdı. Çantada ekmek ve büyük bir şişe yağ vardı. Hello Kitty'nin kendi çantası ise boştu. "Anne, yağ şişesini ben taşıyayım," dedi Hello Kitty. Annesi durdu ve çantasını açtı. Hello Kitty yağ şişesini kendi çantasına koydu. Annesinin çantası artık daha hafifti. İkisi yan yana hızlı adımlarla yürüdü. Biraz sonra kamp yerine vardılar. Hello Kitty annesinin elini tuttu. "Teşekkür ederim, kızım, sen çok iyi bir yol arkadaşısın!" dedi annesi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen çok iyi bir yol arkadaşısın"
   - Cümle 12: «"Teşekkür ederim, kızım, sen çok iyi bir yol arkadaşısın!" dedi annesi.»
   - Açıklama: Tohumdaki arkadaş özelliği karttaki yeni arkadaş edinme anlamında değil, yalnız 'yol arkadaşı' söz oyunu olarak geçiyor.
   - Açıklama: Kartın 'yeni arkadaşlar edinmeyi sever' özelliği kullanılmıyor; kök yalnız annenin son repliğinde 'yol arkadaşı' sözü olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0060` birebir aynı, ardından `@onarim: 2140cdcc87c413f1856d347be717c12d389bc69a`, sonra gövde.
