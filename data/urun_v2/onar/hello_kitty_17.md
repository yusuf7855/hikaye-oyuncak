# Editör görevi (onarım): Hello Kitty, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0022 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0022
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'cetvel', fiil 'denemek', sıfat 'özel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: tabakta iki kardeşe tek bir kurabiye kaldı | kurabiyeyi cetvelle tam ortadan ikiye böldü
@tohum: hello_kitty-0022
@degisim: denemek -> yemek
Evin mutfağında Hello Kitty ile Mimi masadaki tabağa baktı. Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı. İkisi de onu yemek istiyordu, ama tabakta başka kurabiye yoktu. Mimi sessizce tabağa baktı. "Mimi, bu kurabiyeyi seninle paylaşmak istiyorum," dedi Hello Kitty. "İki parça aynı büyüklükte olur mu?" diye sordu Mimi. Hello Kitty kurabiye yaparken hamuru hep cetvelle keserdi. Çekmeceden bir cetvel aldı. Cetveli kurabiyenin tam ortasına koydu. Sonra kurabiyeyi cetvelin kenarından yavaşça ikiye kırdı. İki parça tam aynı boydaydı. Hello Kitty bir parçayı Mimi'ye verdi. İki kardeş yan yana oturdu ve parçalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Mimi sessizce tabağa baktı"
   - Cümle 4: «Mimi sessizce tabağa baktı.»
   - Açıklama: İlk cümlede ikisi de tabağa bakmıştı; aynı bilgi gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0022` birebir aynı, `@degisim: denemek -> yemek` (tutuyorsan), ardından `@onarim: 2f8d36e2cb189bfef5774def25b4609595455c20`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0024 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0024
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'böğürtlen', fiil 'koparmak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: kırmızı böğürtlenler çok sertti ve daldan çıkmıyordu | annesine sordu ve siyah yumuşak olanları kopardı
@tohum: hello_kitty-0024
@degisim: pürüzsüz -> düz
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Annesi evden böğürtlen dalları getirmişti. Hello Kitty ilk kez böğürtlenleri daldan koparmayı denedi. Ama kırmızı böğürtlenler çok sertti ve daldan çıkmıyordu. Hello Kitty böğürtlenleri annesinin elmalı turtasına koymak istiyordu. Yaprakların arasında siyah ve yumuşak böğürtlenler de vardı. "Anne, siyah olanları koparabilir miyim?" diye sordu Hello Kitty. "Evet, siyah olanlar daha tatlı," dedi annesi. Hello Kitty siyah böğürtlenleri hafifçe çekti ve kolayca kopardı. Böğürtlenleri turtanın üstüne düz bir sıra olarak dizdi. "Turtamız çok güzel oldu!" dedi annesi. İkisi gölgeye oturdu ve Hello Kitty'nin en sevdiği turtayı mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi evden böğürtlen dalları getirmişti"
   - Cümle 2: «Annesi evden böğürtlen dalları getirmişti.»
   - Açıklama: Ormandaki kampa evden böğürtlen dalı getirilmesi sebepsiz ve akla yatkın değil.
   - Açıklama: Ormandaki kamp yerine böğürtlen dallarının evden getirilmesi sebepsiz ve akla yatkın değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kırmızı böğürtlenler çok sertti"
   - Cümle 4: «Ama kırmızı böğürtlenler çok sertti ve daldan çıkmıyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Böğürtlenleri turtanın üstüne düz"
   - Cümle 10: «Böğürtlenleri turtanın üstüne düz bir sıra olarak dizdi.»
   - Açıklama: Turta ormanda hiç kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0024` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: 4af762a9f9fc8cbed101c15a0742f6a5ac687cd4`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0033 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0033
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'ay', fiil 'üzülmek', sıfat 'sıcacık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: çizdiği ay yuvarlak olmadı ve çok üzüldü | annesinden yardım isteyip bardağın çevresini çizdi
@tohum: hello_kitty-0033
Hello Kitty pencerenin önünde oturmuş, gökyüzündeki aya bakıyordu. Yeni arkadaşı için bir ay resmi yapmak istiyordu. Ama çizdiği ay yuvarlak olmadı, çünkü eli hep kayıyordu. Hello Kitty resme baktı ve çok üzüldü. Annesi de odadaydı. "Anne, ay yuvarlak olmuyor, bana yardım eder misin?" diye sordu Hello Kitty. Annesi gülümsedi ve ona bir bardak verdi. "Bardağı kağıda koy ve çevresini çiz," dedi annesi. Hello Kitty bardağı kağıda koydu ve kalemle etrafından yavaşça çizdi. Kağıtta kocaman, yuvarlak bir ay vardı. Hello Kitty sevindi, çünkü ay resmi artık çok güzeldi. Annesine sıcacık sarıldı. Hello Kitty bundan sonra bir şeyi yapamayınca annesinden yardım istedi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşı için bir ay resmi"
   - Cümle 2: «Yeni arkadaşı için bir ay resmi yapmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir gerekçe olarak anılıyor, sorunun çözümünde işe yaramıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kalemle etrafından yavaşça çizdi"
   - Cümle 9: «Hello Kitty bardağı kağıda koydu ve kalemle etrafından yavaşça çizdi.»
   - Açıklama: 'Etrafından çizdi' bozuk; 'etrafını çizdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0033` birebir aynı, ardından `@onarim: 90cf87054627dab88fb10b97dfd02c4d4da14ca9`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0034 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0034
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'eşarp', fiil 'özlemek', sıfat 'buzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası yanındaydı ve her şeyi görüyordu | babasının gözlerini eşarpla kapattı ve kurabiyeleri dizdi
@tohum: hello_kitty-0034
Ormanda ağaçların dalları buzluydu. Hello Kitty kamp yerinde babasına bir sürpriz hazırlamak istedi. Ama babası hemen yanında oturuyordu ve her şeyi görüyordu. "Kurabiyeleri çok özledim," dedi babası. Hello Kitty'nin çantasında kurabiyeler, boynunda da pembe bir eşarp vardı. "Baba, bu eşarpla gözlerini bağlayayım mı?" diye sordu Hello Kitty. Babası gülerek başını salladı. Hello Kitty eşarbı babasının gözlerine yavaşça bağladı. Sonra kurabiyeleri çantadan çıkarıp kütüğün üstüne dizdi. En sonunda eşarbı çözdü. Babası kurabiyeleri görünce çok şaşırdı. "Bu çok güzel bir sürpriz, kızım!" dedi babası. "Afiyet olsun, babacığım!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty'nin çantasında kurabiyeler"
   - Cümle 5: «Hello Kitty'nin çantasında kurabiyeler, boynunda da pembe bir eşarp vardı.»
   - Açıklama: Özellikler alanı kurabiye yapmayı sevmesini söylüyor; hikayede kurabiye yapılmıyor, yalnız çantadan çıkarılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0034` birebir aynı, ardından `@onarim: 120f418b9087a42db8fcbb3c4bb9a66f530e99a4`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0035 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar tabağı devirdi ve sebzelerden yapılan yüz bozuldu | tabağı ağacın dibine koyup yüzü yeniden yaptı
@tohum: hello_kitty-0035
Parkta, evin yakınındaki ağaçların gölgesinde Hello Kitty piknik yapıyordu. Kağıt tabağına sebzelerle gülen bir yüz yapmıştı. Ama birden rüzgar esti ve hafif tabak çimenlere devrildi. Sebzeler birbirine karıştı ve yüz bozuldu. Hello Kitty buna biraz mutsuz oldu. Önce tabağı ağacın dibine, rüzgarın gelmediği yere koydu. Sonra sebzeleri tek tek topladı. İki havuç dilimi yüzün gözleri oldu. Bir domates dilimi de ağız oldu. İki salatalık parçasını da kulak diye yukarıya dizdi. Rüzgar yine esti ama tabak artık kıpırdamadı. Hello Kitty çok sevindi, çünkü gülen yüzü yeni arkadaşlarına gösterebilecekti.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty piknik yapıyordu"
   - Cümle 1: «Parkta, evin yakınındaki ağaçların gölgesinde Hello Kitty piknik yapıyordu.»
   - Açıklama: Hello Kitty parkta yanında hiçbir büyük olmadan tek başına piknik yapıyor; güvenli kullanım satırı tek başına gitmeyi yasaklıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve hafif tabak çimenlere devrildi"
   - Cümle 3: «Ama birden rüzgar esti ve hafif tabak çimenlere devrildi.»
   - Açıklama: Rüzgar tabağı deviriyor, toplanıp yeniden diziliyor; örnekteki önemsiz dağıldı-topladı olayına benziyor.
   - Açıklama: Rüzgarın dağıttığı sebzeleri toplayıp yeniden dizmek önemsiz bir 'dağıldı, topladı, bitti' sorunudur.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hello Kitty buna biraz mutsuz oldu"
   - Cümle 5: «Hello Kitty buna biraz mutsuz oldu.»
   - Açıklama: 'Buna mutsuz oldu' yapısı dilbilgisel değil; 'buna üzüldü' olmalı.
   - Açıklama: 'Buna mutsuz oldu' dilbilgisel değil; 'buna biraz üzüldü' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "gülen yüzü yeni arkadaşlarına gösterebilecekti"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü gülen yüzü yeni arkadaşlarına gösterebilecekti.»
   - Açıklama: Özellikler alanındaki arkadaş özelliği yalnız son cümlede anılıyor ve sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız son cümlede anılıyor, çözümde işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "gülen yüzü yeni arkadaşlarına gösterebilecekti"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü gülen yüzü yeni arkadaşlarına gösterebilecekti.»
   - Açıklama: Yeni arkadaşlar hikayede hiç yokken son cümlede sebepsizce beliriyor.
   - Açıklama: Yeni arkadaşlar hikayede hiç kurulmadan son cümlede sebepsizce beliriyor.
   - Açıklama: Hikayede hiç olmayan yeni arkadaşlar son cümlede sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0035` birebir aynı, ardından `@onarim: 78a9c62e794a99ac5208987fb80754ea9f9ee537`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0037 (deneme 4 -> 5)

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
Dışarıda soğuk bir rüzgar esiyordu. Hello Kitty yemek oyununda en sevdiği elmalı turta için elma tartacaktı. Ama önlüğünü bağlayamadı, çünkü ipleri arkadaydı. Hello Kitty arkasındaki ipleri hiç göremiyordu. Hello Kitty biraz düşündü ve ipleri iki yandan öne çekti. İpler uzundu ve önde buluştu. Hello Kitty iki ipi sıkıca bağladı. Sonra terazide üç kırmızı elmayı tarttı. Elmaları büyük bir kaseye tek tek koydu. Hello Kitty çok mutluydu, çünkü önlüğünü tek başına bağlamış ve oyuna başlamıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty biraz düşündü"
   - Cümle 5: «Hello Kitty biraz düşündü ve ipleri iki yandan öne çekti.»
   - Açıklama: Art arda cümlelerde 'Hello Kitty' adı gereksiz yere tekrarlanıyor.
   - Açıklama: Art arda üç cümle 'Hello Kitty' adıyla başlıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0037` birebir aynı, ardından `@onarim: dc5b59304ed3012dc563409f2c4bffbcb7b3f7d2`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0038 (deneme 4 -> 5)

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
Parkta çimenlerin üstünde güneş parlıyordu. Hello Kitty annesiyle ağaçların gölgesine doğru yürüyordu. Annesinin elindeki piknik sepeti çok eskiydi ve sapı birden koptu. Bu sepet, annesinin çok sevdiği bir hediyeydi. Annesi sepete baktı ve üzüldü. Hello Kitty arkadaşlarına hep iyi davranırdı ve annesine hemen yardım etmek istedi. Kırmızı kurdelesini çıkardı. Sonra kurdeleyle sapı sepete sıkıca bağladı. Annesi sepeti yavaşça kaldırdı. Sap yerinde kaldı ve sepet düşmedi. Annesi gülümsedi ve kızına sarıldı. Sonra Hello Kitty ile annesi gölgede mutlu mutlu piknik yaptı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına hep iyi davranırdı"
   - Cümle 6: «Hello Kitty arkadaşlarına hep iyi davranırdı ve annesine hemen yardım etmek istedi.»
   - Açıklama: Özellikler alanındaki arkadaş özelliği annesine yardım sahnesine etiket gibi eklenmiş, sorunun çözümünde işe yaramıyor.
   - Açıklama: Arkadaş özelliği kullanılmak yerine huy olarak söyleniyor ve anneye uygulanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0038` birebir aynı, ardından `@onarim: ec87c49b7320d050cb72fcf4c36b15b92e00caf1`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0039 (deneme 4 -> 5)

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
Hello Kitty ile Mimi, bir kutu kurabiyeyle büyük meşe ağacının altına oturmuştu. İkisi küçük bir topu sepete atma oyunu oynuyordu. Ama sepet çok hafifti ve her atışta yere devriliyordu. Top çimenlere kaçtı ve Mimi güldü. "Sepet yine düştü, Hello Kitty!" dedi Mimi. Hello Kitty biraz düşündü. Sonra evde yaptığı kurabiyelerin ağır kutusunu oyuna kattı. Kutuyu sepetin dibine yerleştirdi. Mimi topu yeniden sepete attı. Top içine düştü ve bu kez sepet hiç kıpırdamadı. "Oldu, Hello Kitty!" dedi Mimi sevinçle. İkisi sırayla atmaya devam etti. Hello Kitty bundan sonra hafif bir sepete hep ağır bir şey koydu.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kurabiye kutusunu sepetin dibine koydu"
   - Cümle 0 (plan satırı): «hafif sepet her atışta yere devriliyordu | kurabiye kutusunu sepetin dibine koydu»
   - Açıklama: Plan kutuyu figürün koyduğunu söylüyor ama gövdede kutuyu Mimi yerleştiriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurabiyelerin ağır kutusunu oyuna kattı"
   - Cümle 7: «Sonra evde yaptığı kurabiyelerin ağır kutusunu oyuna kattı.»
   - Açıklama: 'Oyuna kattı' soyut bir anlatım; 3 yaşındaki çocuk için 'sepete koydu' gibi somut olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0039` birebir aynı, `@degisim: umutlu -> ağır` (tutuyorsan), ardından `@onarim: 645b5656217be3c7228500dd64694b597b11a809`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0042 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0042
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'zincir', fiil 'homurdanmak', sıfat 'sarı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: koşarken ikizinin kağıt zincirini kopardı | özür dileyip kopan halkaları yapıştırdı
@tohum: hello_kitty-0042
Yağmur cama tık tık vuruyordu. Hello Kitty odada koşarak oynuyordu. Ama yerdeki sarı kağıt zincire bastı ve zincir koptu. Zinciri yapan Mimi, kopan halkalara bakıp homurdandı. Hello Kitty hemen durdu ve ikizinin yanına oturdu. "Özür dilerim, Mimi, zincirini hemen düzelteyim," dedi Hello Kitty. Mimi ona yapıştırıcıyı uzattı. Hello Kitty kopan halkaları dikkatle birbirine yapıştırdı. Zincir yine uzun ve sağlam oldu. "Teşekkürler, şimdi daha da güzel," dedi Mimi. Sonra Hello Kitty en sevdiği elmalı turtayı ikiziyle paylaştı. Hello Kitty çok sevindi, çünkü ikizi yeniden gülüyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Hello Kitty en sevdiği elmalı turtayı ikiziyle paylaştı"
   - Cümle 11: «Sonra Hello Kitty en sevdiği elmalı turtayı ikiziyle paylaştı.»
   - Açıklama: Tohumdaki turta özelliği sorunun çözümüne katkı vermeden sona eklenmiş, işe yarar biçimde kullanılmamış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği elmalı turtayı ikiziyle paylaştı"
   - Cümle 11: «Sonra Hello Kitty en sevdiği elmalı turtayı ikiziyle paylaştı.»
   - Açıklama: Tohumdaki turta özelliği sorun çözüldükten sonra eklenmiş, çözüme hiçbir katkısı yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği elmalı turtayı ikiziyle paylaştı"
   - Cümle 11: «Sonra Hello Kitty en sevdiği elmalı turtayı ikiziyle paylaştı.»
   - Açıklama: Elmalı turta daha önce hiç kurulmadan sebepsizce beliriyor.
   - Açıklama: Elmalı turta daha önce kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0042` birebir aynı, ardından `@onarim: 85014c756b7185c74191dc40155dc672ed91f09f`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0044 (deneme 4 -> 5)

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
Ormanda, kamp yerinde Hello Kitty'nin annesi esnedi ve dinlenmek için uzandı. Hello Kitty arkadaşlarına hep iyi davranırdı ve annesine bir sürpriz yapmak istedi. Kalıpla kalp şeklinde bir sandviç yapacaktı. Ama ekmek çok kalındı ve kalıp ekmeği kesemedi. Hello Kitty ekmeğe baktı ve düşündü. Sonra ekmeği yavaşça ikiye ayırdı. İnce parçaya kalıbı iki eliyle bastırdı. Bu kez güzel bir kalp çıktı. Hello Kitty üç kalp daha yaptı ve hepsini bir tabağa dizdi. "Anne, sana bir sürprizim var!" dedi Hello Kitty. Annesi tabağı görünce güldü. "Çok teşekkürler, kızım!" dedi annesi. Sonra ikisi sandviçleri mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına hep iyi davranırdı"
   - Cümle 2: «Hello Kitty arkadaşlarına hep iyi davranırdı ve annesine bir sürpriz yapmak istedi.»
   - Açıklama: Özellikler alanındaki arkadaş özelliği annesine sürpriz sahnesine etiket gibi eklenmiş, çözümde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty arkadaşlarına hep iyi davranırdı"
   - Cümle 2: «Hello Kitty arkadaşlarına hep iyi davranırdı ve annesine bir sürpriz yapmak istedi.»
   - Açıklama: Arkadaşlara iyi davranma ayrıntısı hikayede hiçbir işe yaramıyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ekmek çok kalındı"
   - Cümle 4: «Ama ekmek çok kalındı ve kalıp ekmeği kesemedi.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0044` birebir aynı, `@degisim: sakar -> ince` (tutuyorsan), ardından `@onarim: 573c692a1e96b993df5df5ab5f819df1554cc88c`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0045 (deneme 3 -> 4)

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
Hello Kitty mutfakta oyun hamuruyla oynuyordu. İlk kez lale gibi bir kurabiye yapmayı denedi. Ama lale ayakta durunca ince sap büküldü ve lale devrildi. Çiçek, yapraklar ve sap birbirine yapıştı ve karmakarışık oldu. Hello Kitty hamura baktı ve biraz düşündü. Kurabiyelerin tepside hep düz durduğunu hatırladı. Hamuru yeniden ayırdı. Bu kez kalın bir sapı tepsiye düz koydu. Yanına iki yaprak, en üste de kırmızı bir çiçek yerleştirdi. Lale tepside güzelce durdu ve hiç düşmedi. Hello Kitty bundan sonra hamur lalelerini hep düz yaptı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İlk kez lale gibi bir kurabiye yapmayı denedi"
   - Cümle 2: «İlk kez lale gibi bir kurabiye yapmayı denedi.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde kurabiye büyüksüz yapılıyor ve oyun hamuru kurabiyeyle karıştırılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "lale gibi bir kurabiye yapmayı denedi"
   - Cümle 2: «İlk kez lale gibi bir kurabiye yapmayı denedi.»
   - Açıklama: Oyun hamurundan yapılan şekle 'kurabiye' denmesi kelimeyi yanlış anlamda kullanıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "lale gibi bir kurabiye yapmayı denedi"
   - Cümle 2: «İlk kez lale gibi bir kurabiye yapmayı denedi.»
   - Açıklama: Hello Kitty oyun hamuruyla oynarken kurabiye yaptığı söyleniyor; oyun hamurundan kurabiye olmaz, bu bir çelişkidir.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İlk kez lale gibi bir kurabiye yapmayı denedi"
   - Cümle 2: «İlk kez lale gibi bir kurabiye yapmayı denedi.»
   - Açıklama: Hello Kitty oyun hamuruyla oynarken kurabiye yaptığı söyleniyor; oyun hamuru ile kurabiye çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0045` birebir aynı, `@degisim: planlamak -> hatırlamak` (tutuyorsan), ardından `@onarim: 83d76d9ef42fefdc76c5a0a6929c66c4411da987`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0046 (deneme 3 -> 4)

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
Hello Kitty babasıyla parkta, ağacın gölgesinde piknik yapıyordu. Örtünün üstünde çıtır patatesler ve bir kavanoz turşu vardı. Hello Kitty turşu almak istedi ama kavanozun kapağı çok sıkıydı. İki eliyle çevirdi ama kapak hiç dönmedi. "Baba, lütfen bu kapağı açar mısın?" diye sordu Hello Kitty. Babası kapağı bir kez çevirdi ve kavanoz hemen açıldı. "Teşekkürler, babacığım!" dedi Hello Kitty. Hello Kitty arkadaşlarına hep iyi davranırdı, babasına da önce bir turşu uzattı. Hello Kitty ile babası turşu ve patatesleri mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty arkadaşlarına hep iyi davranırdı, babasına da"
   - Cümle 8: «Hello Kitty arkadaşlarına hep iyi davranırdı, babasına da önce bir turşu uzattı.»
   - Açıklama: Arkadaşlara iyi davranmak babaya turşu uzatmaya yanlış bağlanmış; bağlaç anlamca uymuyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty arkadaşlarına hep"
   - Cümle 8: «Hello Kitty arkadaşlarına hep iyi davranırdı, babasına da önce bir turşu uzattı.»
   - Açıklama: 'Hello Kitty' adı art arda cümlelerde gereksiz yere tekrarlanıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "dedi Hello Kitty. Hello Kitty arkadaşlarına"
   - Cümle 8: «Hello Kitty arkadaşlarına hep iyi davranırdı, babasına da önce bir turşu uzattı.»
   - Açıklama: Ad art arda cümlelerde gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0046` birebir aynı, `@degisim: soğumak -> paylaşmak` (tutuyorsan), ardından `@onarim: 290011633d6746073ad5aa10c2560a57592c994b`, sonra gövde.
