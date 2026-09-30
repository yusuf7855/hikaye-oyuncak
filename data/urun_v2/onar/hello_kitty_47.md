# Editör görevi (onarım): Hello Kitty, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar47.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0157 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0157
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'paket', fiil 'ıslanmak', sıfat 'zarif'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: suya zıpladı ve babasının pantolonu ıslandı | özür diledi ve babasını güneşli bir yere götürdü
@tohum: hello_kitty-0157
@degisim: zarif -> süslü
Parkta, çimenlerin arasında küçük bir su çukuru vardı. Hello Kitty koşarak geldi ve hızla çukura zıpladı. Su her yana sıçradı ve babasının pantolonu ıslandı. Babası elinde süslü bir paket tutuyordu. İçinde evde birlikte yaptıkları kurabiyeler vardı. Hello Kitty babasının pantolonuna baktı ve üzüldü. "Özür dilerim, babacığım," dedi Hello Kitty. Sonra babasının elinden tuttu ve onu güneşli bir yere götürdü. İkisi orada oturdu ve Hello Kitty paketi açtı. Kurabiyeleri birlikte yediler. Güneşte ıslak pantolon yavaş yavaş kurudu. Babası kızına sarıldı. "Teşekkürler, Hello Kitty, bu kurabiyeler çok güzel olmuş!" dedi babası.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babası elinde süslü bir paket tutuyordu"
   - Cümle 4: «Babası elinde süslü bir paket tutuyordu.»
   - Açıklama: Kurabiye paketi sorunla ilgisiz olarak araya giriyor ve son sıcak kapanışı ıslak pantolon yerine kurabiyelere kaydırıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "İçinde evde birlikte yaptıkları kurabiyeler"
   - Cümle 5: «İçinde evde birlikte yaptıkları kurabiyeler vardı.»
   - Açıklama: Tohumdaki kurabiye yapma özelliği sorunun çözümünde işe yaramıyor, yalnız yenen bir yiyecek olarak geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "İçinde evde birlikte yaptıkları kurabiyeler vardı"
   - Cümle 5: «İçinde evde birlikte yaptıkları kurabiyeler vardı.»
   - Açıklama: Tohumdaki kurabiye özelliği sorunun çözümüne (özür ve kurutma) katılmıyor, yan öğe olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0157` birebir aynı, `@degisim: zarif -> süslü` (tutuyorsan), ardından `@onarim: 3f77361d98c77e43eb1963cc325a14412f023123`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0160 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0160
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'tabak', fiil 'gıdıklamak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesi yanındaydı ve sürprizi görebilirdi | annesinden gözlerini kapatmasını istedi ve kurabiyeleri dizdi
@tohum: hello_kitty-0160
@degisim: yardımsever -> mutlu
Hello Kitty annesiyle parkta, ağacın gölgesinde oturuyordu. Bugün annesinin doğum günüydü ve Hello Kitty ona sürpriz hazırlamak istedi. Ama annesi hemen yanındaydı ve her şeyi görecekti. "Anneciğim, gözlerini kapatıp yüze kadar sayar mısın?" diye sordu Hello Kitty. Annesi gülümsedi ve iki eliyle yüzünü kapattı. Hello Kitty sepetten büyük bir tabak çıkardı. Evde annesiyle yaptıkları kurabiyeleri tabağa bir kalp şeklinde dizdi. "Yüz!" dedi annesi ve ellerini indirdi. Tabakta kurabiyelerden kocaman bir kalp vardı. Annesi kızına sarıldı ve onu gıdıkladı. Hello Kitty neşeyle güldü. "Mutlu yıllar, anneciğim!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Evde annesiyle yaptıkları kurabiyeleri"
   - Cümle 7: «Evde annesiyle yaptıkları kurabiyeleri tabağa bir kalp şeklinde dizdi.»
   - Açıklama: Kurabiyeler annesiyle birlikte yapıldığı için annesinden gizlenen sürpriz kendi içinde çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0160` birebir aynı, `@degisim: yardımsever -> mutlu` (tutuyorsan), ardından `@onarim: d05dd33dc5015f43d32f3d23f7a858a20a61eb68`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0165 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0165
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kabak', fiil 'sektirmek', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: kutu çok hafifti ve top çarpınca devrildi | kutunun dibine ağır bir kabak koydu
@tohum: hello_kitty-0165
Bir sabah Hello Kitty evde yeni arkadaşlarıyla oynamak için bir oyun yapıyordu. Oyunda top yere sekip büyük bir kutunun içine düşecekti. Ama kutu çok hafifti ve top çarpınca hemen devrildi. Hello Kitty kutuyu kaldırdı ve biraz düşündü. Kutunun ağır olması için içine bir şey koymalıydı. Mutfaktaki sepette büyük, turuncu bir kabak vardı. Hello Kitty kabağı iki eliyle taşıdı ve kutunun dibine koydu. Sonra topu güçlü bir şekilde yere sektirdi. Top zıpladı ve kutunun içine düştü. Kutu bu kez hiç kıpırdamadı. Oyun artık hazırdı. Hello Kitty bundan sonra hafif kutuların dibine hep ağır bir şey koydu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "için bir oyun yapıyordu"
   - Cümle 1: «Bir sabah Hello Kitty evde yeni arkadaşlarıyla oynamak için bir oyun yapıyordu.»
   - Açıklama: Oyun yapılmaz, kurulur ya da hazırlanır; 'bir oyun kuruyordu' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlarıyla oynamak için"
   - Cümle 1: «Bir sabah Hello Kitty evde yeni arkadaşlarıyla oynamak için bir oyun yapıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bahane olarak anılıyor, çözümde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "evde yeni arkadaşlarıyla oynamak"
   - Cümle 1: «Bir sabah Hello Kitty evde yeni arkadaşlarıyla oynamak için bir oyun yapıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız açılışta anılıyor, sorunun çözümünde işe yaramıyor (kartın özellikler alanı).
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "yeni arkadaşlarıyla oynamak için"
   - Cümle 1: «Bir sabah Hello Kitty evde yeni arkadaşlarıyla oynamak için bir oyun yapıyordu.»
   - Açıklama: Kartın yanlar bölümünde ve kararlarda Mimi, anne ve baba dışında arkadaş yok; kartta olmayan arkadaşlar ekleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlarıyla oynamak için bir oyun"
   - Cümle 1: «Bir sabah Hello Kitty evde yeni arkadaşlarıyla oynamak için bir oyun yapıyordu.»
   - Açıklama: Yeni arkadaşlar oyunun amacı olarak kuruluyor ama hikayede hiç görünmüyor ve işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0165` birebir aynı, ardından `@onarim: 7c9d3b1ef8368960500dc235e4eb68ab6dcea85c`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0168 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0168
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'börek', fiil 'durdurmak', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgarla örtünün ucu kalktı ve turta kaydı | tabağı durdurdu ve örtünün ucuna oturdu
@tohum: hello_kitty-0168
@degisim: ferah -> serin
Parkta, ağaçların gölgesinde serin bir rüzgar esiyordu. Hello Kitty örtünün üstünde oturmuş, böreğini yiyordu. Birden rüzgarla örtünün ucu kalktı ve turta tabağı çimenlere doğru kaydı. Tabakta en sevdiği elmalı turta vardı. Hello Kitty böreğini bıraktı ve tabağı iki eliyle tuttu ve durdurdu. Sonra örtünün kalkan ucuna geçip oturdu. Rüzgar yine esti ama örtü bu kez hiç kalkmadı. Hello Kitty tabağı yanına, örtünün ortasına koydu. Turta tabakta yerinde duruyordu. Hello Kitty böreğini bitirdi ve elmalı turtasını mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "böreğini bıraktı ve tabağı iki eliyle tuttu ve durdurdu"
   - Cümle 5: «Hello Kitty böreğini bıraktı ve tabağı iki eliyle tuttu ve durdurdu.»
   - Açıklama: Aynı cümlede 've' bağlacı gereksiz yere iki kez tekrarlanıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "tabağı iki eliyle tuttu ve durdurdu"
   - Cümle 5: «Hello Kitty böreğini bıraktı ve tabağı iki eliyle tuttu ve durdurdu.»
   - Açıklama: Aynı cümlede 've' gereksizce iki kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0168` birebir aynı, `@degisim: ferah -> serin` (tutuyorsan), ardından `@onarim: 73d9c34117c9a36b21a39331e86fc527af450d41`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0169 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0169
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'brokoli', fiil 'kutlamak', sıfat 'çilekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: güneşte beyaz kağıda bakmak çok zordu | ağaçların gölgesine oturup bulutların resmini çizdi
@tohum: hello_kitty-0169
@degisim: kutlamak -> çizmek
Hello Kitty parkta çimenlere uzanmış, bulutlara bakıyordu. Bir bulut brokoliye, bir bulut da çilekli bir pastaya benziyordu. Hello Kitty bu bulutları çizmek istedi ama parlak güneşte kağıda bakamadı. Hello Kitty etrafına baktı ve büyük bir ağaç gördü. Kağıdını ve boyalarını alıp ağacın gölgesine oturdu. Gölgede kağıt artık parlamıyordu. Hello Kitty önce yeşil boyayla brokoliye benzeyen bulutu çizdi. Sonra pembe boyayla pastaya benzeyen bulutu çizdi. Pastanın üstüne küçük kırmızı çilekler de ekledi. Resim bitince kağıdı iki eliyle tuttu ve baktı. Hello Kitty çok sevindi, çünkü arkadaşlarına göstereceği resim artık hazırdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çünkü arkadaşlarına göstereceği resim"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü arkadaşlarına göstereceği resim artık hazırdı.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son cümlede anılıyor ve olayda işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son cümlede anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0169` birebir aynı, `@degisim: kutlamak -> çizmek` (tutuyorsan), ardından `@onarim: 13ee1e0e69f80f259dbce1e11ce9efc44aef6cf5`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0170 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0170
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fide', fiil 'uyanmak', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: top küçük bitkilerin arasına yuvarlandı | bitkilere dikkat ederek yürüdü ve topu aldı
@tohum: hello_kitty-0170
@degisim: uyanmak -> yürümek
Bir sabah Hello Kitty parkta topuyla yakalama oyunu oynuyordu. Topu yere atıyor ve havada yakalamaya çalışıyordu. Ama top yere çarptı ve küçük bitkilerin arasına yuvarlandı. Bu küçük bitkiler yeni dikilmiş fidelerdi ve kolay eğiliyordu. Hello Kitty bitkilerin arasında dar bir yol gördü. Parmaklarının ucunda bu yoldan yavaşça yürüdü. Topu iki bitkinin arasından dikkatle aldı. Sonra aynı yoldan geri döndü. Bitkilerin hepsi yine dimdik duruyordu. Çimenler top oyunu için mükemmel bir yerdi. Hello Kitty bundan sonra arkadaşlarıyla hep bitkilerden uzakta, çimenlerde oynadı.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "top yere çarptı ve küçük bitkilerin arasına yuvarlandı"
   - Cümle 3: «Ama top yere çarptı ve küçük bitkilerin arasına yuvarlandı.»
   - Açıklama: Top yuvarlanıyor, alınıyor ve bitiyor; sorun çocuğun önemseyeceği bir gerilim taşımıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni dikilmiş fidelerdi"
   - Cümle 4: «Bu küçük bitkiler yeni dikilmiş fidelerdi ve kolay eğiliyordu.»
   - Açıklama: 'Fide' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Fide' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Parmaklarının ucunda bu yoldan"
   - Cümle 6: «Parmaklarının ucunda bu yoldan yavaşça yürüdü.»
   - Açıklama: Kalıp bozuk; 'parmaklarının ucuna basarak' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hep bitkilerden uzakta"
   - Cümle 11: «Hello Kitty bundan sonra arkadaşlarıyla hep bitkilerden uzakta, çimenlerde oynadı.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son cümlede geçiyor, sorunun çözümünde işe yaramıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bundan sonra arkadaşlarıyla hep bitkilerden"
   - Cümle 11: «Hello Kitty bundan sonra arkadaşlarıyla hep bitkilerden uzakta, çimenlerde oynadı.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son cümlede anılıyor, sorunun çözümünde işe yaramıyor.
6. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "bundan sonra arkadaşlarıyla hep"
   - Cümle 11: «Hello Kitty bundan sonra arkadaşlarıyla hep bitkilerden uzakta, çimenlerde oynadı.»
   - Açıklama: Çoğul arkadaşlar arka planda kalmıyor, Hello Kitty ile birlikte oynayarak olaya katılıyor.
7. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bundan sonra arkadaşlarıyla hep"
   - Cümle 11: «Hello Kitty bundan sonra arkadaşlarıyla hep bitkilerden uzakta, çimenlerde oynadı.»
   - Açıklama: Kartın yanlar bölümünde Mimi, annesi ve babası dışında arkadaş karakterler yok.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bundan sonra arkadaşlarıyla hep bitkilerden uzakta"
   - Cümle 11: «Hello Kitty bundan sonra arkadaşlarıyla hep bitkilerden uzakta, çimenlerde oynadı.»
   - Açıklama: Hello Kitty tek başına oynarken arkadaşlar son cümlede sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0170` birebir aynı, `@degisim: uyanmak -> yürümek` (tutuyorsan), ardından `@onarim: df1ec06098c3a3988ad9b582bcd62eccbc0416aa`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0172 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0172
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'halat', fiil 'gezinmek', sıfat 'zor'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: parkta bir ses duydu ve nereden geldiğini merak etti | ağaçların arasında gezindi ve sesi yapan salıncağı buldu
@tohum: hello_kitty-0172
Parkta rüzgarlı bir sabah Hello Kitty çimenlerde yürüyordu. Birden bir yerden tuhaf bir ses geldi. Hello Kitty sesin nereden geldiğini çok merak etti. Ağaçların arasında yavaş yavaş gezindi. Ağaçlar çok fazlaydı ve sesi bulmak zordu. Hello Kitty her ağacın yanında durdu ve dinledi. Ses en büyük ağaçtan geliyordu. Bu ağacın dalına kalın bir halat bağlıydı. Ucunda tahtadan bir salıncak vardı. Rüzgar salıncağı sallıyordu ve dal gıcırdıyordu. Hello Kitty sesi bulduğu için güldü. Salıncağı arkadaşlarına göstermek için yanında mutlu mutlu bekledi.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden bir yerden tuhaf bir ses geldi"
   - Cümle 2: «Birden bir yerden tuhaf bir ses geldi.»
   - Açıklama: Sorun yalnız bir sesi merak etmek; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sesin nereden geldiğini çok merak etti"
   - Cümle 3: «Hello Kitty sesin nereden geldiğini çok merak etti.»
   - Açıklama: Sorun yalnız merak; çocuğun önemseyeceği gerçek bir sorun yok.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ağaçların arasında yavaş yavaş gezindi"
   - Cümle 4: «Ağaçların arasında yavaş yavaş gezindi.»
   - Açıklama: Hello Kitty tek başına tuhaf bir sesin peşinden ağaçların arasına gidiyor; güvenli kullanım satırı tek başına uzağa gitmeyi yasaklar.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ağaçlar çok fazlaydı ve"
   - Cümle 5: «Ağaçlar çok fazlaydı ve sesi bulmak zordu.»
   - Açıklama: 'Ağaçlar çok fazlaydı' doğal değil; 'Çok ağaç vardı' olmalı.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Salıncağı arkadaşlarına göstermek için"
   - Cümle 12: «Salıncağı arkadaşlarına göstermek için yanında mutlu mutlu bekledi.»
   - Açıklama: Tohumdaki arkadaş özelliği sorunun çözümünde işe yaramıyor, yalnız sonda anılıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Salıncağı arkadaşlarına göstermek için"
   - Cümle 12: «Salıncağı arkadaşlarına göstermek için yanında mutlu mutlu bekledi.»
   - Açıklama: Hikayede hiç olmayan arkadaşlar sebepsizce beliriyor.
   - Açıklama: Hikayede hiç olmayan arkadaşlar son cümlede sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0172` birebir aynı, ardından `@onarim: 5ef966d18719ab54798e95233bed4d378f04b99f`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0173 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0173
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yorgan', fiil 'yırtılmak', sıfat 'ilginç'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası elmalı turtayı nereye koyduğunu unuttu | kokusunu tanıdı ve turtanın kutusunu ağacın arkasında buldu
@tohum: hello_kitty-0173
@degisim: yorgan -> örtü
Bir sabah Hello Kitty ile babası parkta bir örtünün üstünde oturuyordu. Babası sepete baktı ama elmalı turtayı bulamadı. Turtayı nereye koyduğunu unutmuştu. "Turta nerede, hiç bilmiyorum," dedi babası. Hello Kitty havayı kokladı ve ilginç, tatlı bir koku aldı. Bu, en sevdiği elmalı turtanın kokusuydu. Hello Kitty kokunun geldiği yere doğru yürüdü. Büyük bir ağacın arkasında bir kutu duruyordu. Kutunun kağıdı biraz yırtılmıştı ve koku oradan geliyordu. "Baba, turta burada!" diye seslendi Hello Kitty. "Onu serin kalsın diye gölgeye koydum," dedi babası. Hello Kitty kutuyu babasıyla birlikte örtünün üstüne taşıdı. Babası çok sevindi, çünkü Hello Kitty turtayı bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ilginç, tatlı bir koku"
   - Cümle 5: «Hello Kitty havayı kokladı ve ilginç, tatlı bir koku aldı.»
   - Açıklama: 'İlginç' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0173` birebir aynı, `@degisim: yorgan -> örtü` (tutuyorsan), ardından `@onarim: f7aaec6198c52109b46d0b184067ad4ccd917139`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0174 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0174
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'sos', fiil 'saklanmak', sıfat 'uslu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: sos kavanozunun kapağı çok sıkıydı ve açılmadı | kardeşinden yardım istedi ve kapağı birlikte açtılar
@tohum: hello_kitty-0174
@degisim: saklanmak -> tutmak
Hello Kitty ile Mimi ormandaki kamp yerinde sandviç yapıyordu. Hello Kitty sandviçlere domates sosu koymak istedi. Ama sos kavanozunun kapağı çok sıkıydı ve açılmadı. Hello Kitty kapağı çevirdi ama kapak hiç dönmedi. Mimi örtünün üstünde uslu uslu oturmuş, bekliyordu. "Mimi, bana yardım eder misin?" diye sordu Hello Kitty. "Tabii, kavanozu ben tutarım," dedi Mimi. Mimi kavanozu iki eliyle sıkıca tuttu. Hello Kitty de kapağı bütün gücüyle çevirdi. Kapak sonunda açıldı. Hello Kitty sandviçlere biraz sos sürdü ve birini Mimi'ye verdi. Hello Kitty çok sevindi, çünkü en iyi arkadaşı olan kardeşiyle kapağı açmıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kapağı çevirdi ama kapak hiç dönmedi"
   - Cümle 4: «Hello Kitty kapağı çevirdi ama kapak hiç dönmedi.»
   - Açıklama: Kapak dönmediyse 'çevirdi' yanlış; 'çevirmeye çalıştı' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı olan kardeşiyle"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü en iyi arkadaşı olan kardeşiyle kapağı açmıştı.»
   - Açıklama: Adıyla tanıtılmış Mimi sonda yeniden 'en iyi arkadaşı olan kardeşi' diye tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşı olan kardeşiyle"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü en iyi arkadaşı olan kardeşiyle kapağı açmıştı.»
   - Açıklama: Tohumdaki arkadaş özelliği çözümde kullanılmıyor, yalnız son cümlede etiket olarak anılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşı olan kardeşiyle kapağı açmıştı"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü en iyi arkadaşı olan kardeşiyle kapağı açmıştı.»
   - Açıklama: Tohumdaki arkadaş özelliği sorunu çözmede işe yaramıyor, yalnız son cümlede anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0174` birebir aynı, `@degisim: saklanmak -> tutmak` (tutuyorsan), ardından `@onarim: 3f68504cc952c9bf9ac3819e357461b164554d12`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0175 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0175
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'tartı', fiil 'dönmek', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: simsiyah bulutlar geldi ve resim ıslanabilirdi | kağıtları ve boyaları çadırın içine taşıdı
@tohum: hello_kitty-0175
@degisim: tartı -> çadır
Hello Kitty kamp yerinde çadırın önünde oturuyordu. Yeni arkadaşlarına vermek için bir orman resmi yapıyordu. Birden arkasına döndü ve ağaçların üstünde simsiyah bulutlar gördü. Yağmur yağarsa resim ıslanırdı. Hello Kitty kağıtlarını ve boyalarını hemen topladı. Hepsini çadırın içine taşıdı. Sonra kendisi de çadıra girdi ve kapısını kapattı. Biraz sonra yağmur damlaları çadırın üstüne düşmeye başladı. Hello Kitty resmine baktı. Resim yine kuruydu. Hello Kitty yağmurun sesini dinledi ve resmini çadırda mutlu mutlu bitirdi.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde çadırın önünde oturuyordu"
   - Cümle 1: «Hello Kitty kamp yerinde çadırın önünde oturuyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez ama Hello Kitty ormanda yalnız.
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda yalnız.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına vermek için"
   - Cümle 2: «Yeni arkadaşlarına vermek için bir orman resmi yapıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "ağaçların üstünde simsiyah bulutlar gördü"
   - Cümle 3: «Birden arkasına döndü ve ağaçların üstünde simsiyah bulutlar gördü.»
   - Açıklama: Ormanda yalnız bir çocuğun üstüne gelen simsiyah bulutlar küçük çocukları korkutabilir.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yağmur yağarsa resim ıslanırdı"
   - Cümle 4: «Yağmur yağarsa resim ıslanırdı.»
   - Açıklama: Resmin ıslanma tehlikesi ancak 4. cümlede açıkça söyleniyor; ilk üç cümlede yalnız bulutlar görülüyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Resim yine kuruydu"
   - Cümle 10: «Resim yine kuruydu.»
   - Açıklama: 'Yine' yanlış anlamda kullanılmış; 'hâlâ kuruydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0175` birebir aynı, `@degisim: tartı -> çadır` (tutuyorsan), ardından `@onarim: eb7590d6586f51694eaf0df4aa921bfa6b1be1ff`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0177 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0177
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: kaybolan eşya
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çatal', fiil 'düzenlemek', sıfat 'sıkı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: rüzgar kardeşinin hafif çatalını uçurdu ve çatal kayboldu | kardeşine iyi davranıp çatalı çiçeklerin arasında buldu
@tohum: hello_kitty-0177
Parkta güçlü bir rüzgar esiyordu. Hello Kitty ağacın gölgesinde piknik tabaklarını düzenledi. Ama rüzgar Mimi'nin hafif plastik çatalını uçurdu ve çatal kayboldu. Mimi çimenlere baktı ama çatalını göremedi. Mimi çok utangaçtı ve üzgün üzgün sustu. Hello Kitty Mimi'nin yanına oturdu ve arkadaşça elini tuttu. "Üzülme, Mimi, çatalını birlikte bulalım," dedi Hello Kitty. Mimi biraz rahatladı ve çiçekleri gösterdi. "Çatal o tarafa düştü," dedi Mimi. Hello Kitty çiçeklerin arasına eğildi. Küçük çatal bir yaprağın altındaydı. Hello Kitty çatalı alıp kardeşine verdi. Mimi çatalını sıkı sıkı tuttu ve güldü. İki kardeş yeniden oturdu ve mutlu mutlu piknik yaptı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşça elini tuttu"
   - Cümle 6: «Hello Kitty Mimi'nin yanına oturdu ve arkadaşça elini tuttu.»
   - Açıklama: Mimi kardeşidir; 'arkadaşça' kelimesi bu ilişkiye uymuyor ve kimin elinin tutulduğu da belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0177` birebir aynı, ardından `@onarim: 7661244aa5059889c7e57d6c0624561d47519e3c`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0178 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0178
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yeni bir şeyi denemek
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'askı', fiil 'uyutmak', sıfat 'benekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: yeni meyveyi tatmak istemedi çünkü kabuğu benekliydi | armudu en sevdiği turtanın üstüne koyup tattı
@tohum: hello_kitty-0178
@degisim: uyutmak -> tatmak
Hello Kitty babasıyla parkta piknik yapıyordu. Babası piknik çantasını askısından tuttu ve ağacın gölgesine koydu. Çantadan benekli bir armut çıkardı ama Hello Kitty tatmak istemedi. Daha önce hiç armut yememişti ve benekler ona garip geldi. "Biraz dene, çok tatlıdır," dedi babası. Hello Kitty çantaya baktı ve elmalı turtayı gördü. "Baba, armudu turtamın üstüne koyar mısın?" diye sordu Hello Kitty. Babası armudu küçük parçalara kesti ve turtanın üstüne dizdi. Hello Kitty turtayı ısırdı. Tatlı armut ile elma birlikte çok güzeldi. "Armut da çok lezzetliymiş!" dedi Hello Kitty. Hello Kitty çok sevindi, çünkü yeni bir meyveyi denemişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "piknik çantasını askısından tuttu"
   - Cümle 2: «Babası piknik çantasını askısından tuttu ve ağacın gölgesine koydu.»
   - Açıklama: Çantanın askısından tutulması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0178` birebir aynı, `@degisim: uyutmak -> tatmak` (tutuyorsan), ardından `@onarim: 708878f6ce3c6ef9325c4d696d8359fe9ed3631d`, sonra gövde.
