# Editör görevi (onarım): Hello Kitty, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0001 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0001
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kova', fiil 'koşturmak', sıfat 'faydalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: kova çok hafifti ve top düşünce devrildi | kovanın içine taş koyup onu ağır yaptı
@tohum: hello_kitty-0001
@degisim: faydalı -> küçük
Parkta serin ve güneşli bir sabahtı. Hello Kitty ağaçların gölgesinde topu kırmızı kovaya atıyordu. Ama kova çok hafifti ve top içine düşünce kova devrildi. Top da çimenlerde biraz yuvarlandı. Hello Kitty topun arkasından koşturdu ve onu geri aldı. Bu oyunla parkta yeni arkadaşlar bulmak istiyordu. Kovayı ağır yapmak için ağacın altından üç küçük taş topladı. Taşları kovanın içine koydu. Hello Kitty topu yine attı. Top kovaya düştü ve kova hiç devrilmedi. Hello Kitty sevinçle zıpladı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "parkta yeni arkadaşlar bulmak istiyordu"
   - Cümle 6: «Bu oyunla parkta yeni arkadaşlar bulmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız istek olarak anılıyor, hikayede hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu oyunla parkta yeni arkadaşlar bulmak istiyordu"
   - Cümle 6: «Bu oyunla parkta yeni arkadaşlar bulmak istiyordu.»
   - Açıklama: Yeni arkadaş bulma isteği kuruluyor ama hikayede hiç kullanılmıyor.
   - Açıklama: Yeni arkadaş bulma hedefi kuruluyor ama hikayede hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0001` birebir aynı, `@degisim: faydalı -> küçük` (tutuyorsan), ardından `@onarim: e0754a0f32e3e71faa459b8f311f7d7e4bacff13`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0004 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0004
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'zil', fiil 'ölçmek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: ağaçların arasından zil gibi ince bir ses geldi | sesin peşinden gitti ve dalda çarpışan kaşıkları buldu
@tohum: hello_kitty-0004
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Annesi ılık sütü ölçtü ve iki bardağa koydu. Birden ağaçların arasından zil gibi ince bir ses geldi. Hello Kitty bunu çok merak etti. "Anne, bu ses nereden geliyor?" diye sordu Hello Kitty. "Gel, birlikte bakalım," dedi annesi. İkisi çadırın arkasına yürüdü. Hello Kitty orada yeni bir arkadaş olabilir diye düşündü. "Merhaba!" diye seslendi Hello Kitty. Kimse cevap vermedi ama ses yine geldi. Hello Kitty yukarı baktı. Alçak bir dalda, kurusun diye asılan iki kaşık vardı. Rüzgar esince kaşıklar birbirine çarpıyordu. İkisi de çok güldü, çünkü sesi iki kaşık yapıyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi ılık sütü ölçtü ve iki bardağa koydu"
   - Cümle 2: «Annesi ılık sütü ölçtü ve iki bardağa koydu.»
   - Açıklama: Süt ve bardaklar kuruluyor ama olayda hiç kullanılmıyor.
   - Açıklama: Süt kurulup bir daha kullanılmıyor; işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0004` birebir aynı, ardından `@onarim: 8e3d5984d8775f0f407b2a77123d29320e5b603e`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0008 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0008
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'perde', fiil 'çekmek', sıfat 'biberli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: ip gergin değildi ve perde çimenlere düştü | ipi çekip sıkı bir düğümle ağaca yeniden bağladı
@tohum: hello_kitty-0008
@degisim: biberli -> renkli
Bir sabah Hello Kitty parkta kukla oyunu oynamak istedi. İki ağacın arasına bir ip bağladı ve ipe renkli bir perde astı. Ama ip gergin değildi ve perde hemen çimenlere düştü. Hello Kitty bu oyunla parkta yeni arkadaşlar bulmak istiyordu. İpi iki eliyle çekti ve gerdi. Sonra ipin ucunu sıkı bir düğümle ağaca yeniden bağladı. Perdeyi tekrar astı ve bu kez perde düşmedi. Hello Kitty perdenin arkasına geçti ve kukla oyununa başladı. Hello Kitty çok sevindi, çünkü perde artık hiç düşmüyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "parkta yeni arkadaşlar bulmak istiyordu"
   - Cümle 4: «Hello Kitty bu oyunla parkta yeni arkadaşlar bulmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, hikayede hiçbir işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız istek olarak anılıyor, hikayede hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlar bulmak istiyordu"
   - Cümle 4: «Hello Kitty bu oyunla parkta yeni arkadaşlar bulmak istiyordu.»
   - Açıklama: Yeni arkadaş bulma hedefi kuruluyor ama hikayede hiç arkadaş gelmiyor ve bu ayrıntı kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty bu oyunla parkta yeni arkadaşlar bulmak istiyordu"
   - Cümle 4: «Hello Kitty bu oyunla parkta yeni arkadaşlar bulmak istiyordu.»
   - Açıklama: Yeni arkadaş bulma hedefi kurulup hiç kullanılmıyor, hikayede tek arkadaş belirmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0008` birebir aynı, `@degisim: biberli -> renkli` (tutuyorsan), ardından `@onarim: af4ed90f055b44d780e649b2591b0585c7c330e8`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0009 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0009
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'testi', fiil 'oturmak', sıfat 'hareketli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: kütük sallanıyordu çünkü yer düz değildi | düz bir yer buldu ve kütüğü babasıyla oraya yuvarladı
@tohum: hello_kitty-0009
@degisim: hareketli -> düz
Ormandaki kamp yerinde Hello Kitty'nin babası çadırı kurup yorulmuştu. Babası su testisini aldı ve bir kütüğe oturmak istedi. Ama kütük sallandı, çünkü yer düz değildi. "Bu kütük hiç durmuyor, kızım!" dedi babası ve güldü. Hello Kitty hemen babasına yardım etmek istedi. Etrafa baktı ve ağaçların arasında düz bir yer buldu. "Baba, kütüğü buraya getirelim," dedi Hello Kitty. Hello Kitty ile babası kütüğü birlikte oraya yuvarladı. Kütük artık hiç sallanmıyordu. "Teşekkürler, kızım, sen benim en iyi kamp arkadaşımsın," dedi babası. Sonra ikisi kütükte yan yana oturup testiden mutlu mutlu su içti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen benim en iyi kamp arkadaşımsın"
   - Cümle 10: «"Teşekkürler, kızım, sen benim en iyi kamp arkadaşımsın," dedi babası.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği işe yarar biçimde kullanılmıyor, yalnız babanın sözünde kelime olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0009` birebir aynı, `@degisim: hareketli -> düz` (tutuyorsan), ardından `@onarim: 81d7e2128301bbebb34f4e0768c5223fe6321442`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0012
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kıyafet', fiil 'yaratmak', sıfat 'taze'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: iki kardeş de tek kıyafeti aynı anda giymek istedi | sırayla giymeyi önerdi ve önce kardeşine verdi
@tohum: hello_kitty-0012
Ağaçların arasında hafif bir rüzgar esiyordu. Hello Kitty ile Mimi parkta çimenlere oturmuştu. Sepette tek bir oyun kıyafeti vardı ve ikisi de onu giymek istedi. Kıyafeti iki ucundan birden tuttular. Hello Kitty biraz düşündü ve sırayla giymeyi önerdi. Kıyafeti önce kardeşine verdi. Kendisi de sepetten taze elmalı turtayı çıkardı. En sevdiği turtadan bir dilim yerken Mimi'yi izledi. Mimi kıyafeti giyip yeni bir oyun yarattı. Kollarını açtı ve çimenlerde uçar gibi koştu. Sonra sıra Hello Kitty'ye geldi. O da çiçeklerin arasında dans etti. İki kardeş turtayı da kıyafeti de paylaşarak mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sepetten taze elmalı turtayı çıkardı"
   - Cümle 7: «Kendisi de sepetten taze elmalı turtayı çıkardı.»
   - Açıklama: Tohumdaki turta özelliği sorunun çözümünde işe yaramıyor ve üç kez tekrarlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepetten taze elmalı turtayı çıkardı"
   - Cümle 7: «Kendisi de sepetten taze elmalı turtayı çıkardı.»
   - Açıklama: Turta sebepsiz beliriyor, kıyafet sorununa katkısı yok ve sonda paylaşıldığı söylense de paylaşılmıyor.
   - Açıklama: Turta sorunla ilgisiz bir ayrıntı olarak araya giriyor ve olaydan çıkmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "En sevdiği turtadan bir dilim yerken"
   - Cümle 8: «En sevdiği turtadan bir dilim yerken Mimi'yi izledi.»
   - Açıklama: Tohumdaki turta özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak ekleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir oyun yarattı"
   - Cümle 9: «Mimi kıyafeti giyip yeni bir oyun yarattı.»
   - Açıklama: 'oyun yarattı' soyut ve çocuğun bilmeyeceği bir kullanım.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çimenlerde uçar gibi koştu"
   - Cümle 10: «Kollarını açtı ve çimenlerde uçar gibi koştu.»
   - Açıklama: 'Uçar gibi koştu' mecazlı bir benzetme; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'uçar gibi' benzetmesi mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0012` birebir aynı, ardından `@onarim: a766c670731f3c13fa098d952f6c6860e896bfbd`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0013
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fırça', fiil 'yollamak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesinin fırçası çok kalındı | kendi incecik fırçasını annesine yolladı
@tohum: hello_kitty-0013
Hello Kitty ile annesi parkta düz taşları boyuyordu. Annesi taşına küçük bir kedi yaptı. Ama kalın fırçasıyla kedinin ince bıyıklarını yapamadı. "Bu fırça çok kalın," dedi annesi. Hello Kitty kendi fırçasına baktı. Onun bir de incecik bir fırçası vardı. "Anne, bu fırçayı sana yolluyorum!" dedi Hello Kitty. Fırçayı örtünün üstünden annesine doğru yuvarladı. Annesi fırçayı aldı ve bıyıkları tek tek çizdi. Taşın üstündeki kedi artık çok tatlı görünüyordu. "Teşekkürler, sen harika bir arkadaşsın," dedi annesi. Hello Kitty çok mutlu oldu, çünkü fırçası annesinin kedisini tamamlamıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu fırçayı sana yolluyorum"
   - Cümle 7: «"Anne, bu fırçayı sana yolluyorum!" dedi Hello Kitty.»
   - Açıklama: Yan yanda oturan birine fırça vermek için 'yollamak' uygun değil; 'veriyorum' olmalı.
   - Açıklama: Yanındaki kişiye yuvarlanan fırça için 'yollamak' uygun değil; 'veriyorum' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Fırçayı örtünün üstünden annesine doğru yuvarladı"
   - Cümle 8: «Fırçayı örtünün üstünden annesine doğru yuvarladı.»
   - Açıklama: Örtü sebepsiz beliriyor ve fırçayı elden vermek yerine yuvarlamak olaydan çıkmayan tuhaf bir eylem.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "harika bir arkadaşsın"
   - Cümle 11: «"Teşekkürler, sen harika bir arkadaşsın," dedi annesi.»
   - Açıklama: Anne kızına 'arkadaş' diyor; kelime ilişkiye uymuyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen harika bir arkadaşsın"
   - Cümle 11: «"Teşekkürler, sen harika bir arkadaşsın," dedi annesi.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, yalnız kelime olarak anneye söyletiliyor.
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, yalnız annesinin sözünde kelime olarak geçiyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fırçası annesinin kedisini tamamlamıştı"
   - Cümle 12: «Hello Kitty çok mutlu oldu, çünkü fırçası annesinin kedisini tamamlamıştı.»
   - Açıklama: Fırça kediyi tamamlamaz; özneye uygun olmayan fiil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0013` birebir aynı, ardından `@onarim: cbaf5e791c7e654cd999a259dcf1a33488e8c9ab`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0014 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0014
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'karnabahar', fiil 'uzaklaşmak', sıfat 'sabunlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar esince köpük balonları hemen uzaklaştı | ağacın gölgesine geçti ve çubuğu yavaşça salladı
@tohum: hello_kitty-0014
Bir sabah Hello Kitty parkta köpük balonu yapıyordu. Çubuğu sabunlu suya batırdı ve havada salladı. Ama rüzgar esince balonlar hemen ondan uzaklaştı. Hello Kitty büyük bir balon yapmak istiyordu. Küçük balonlar çiçeklerin üstünde bir bir patladı. Hello Kitty etrafına baktı ve gölgeli bir ağaç gördü. Ağacın altına geçti, orada rüzgar yoktu. Bu kez çubuğu çok yavaş salladı. Çubuğun ucunda kocaman bir balon büyüdü. Sonra ona küçük balonlar yapıştı. Balon tıpkı bir karnabahara benzedi! Hello Kitty güldü ve balona arkadaşça el salladı. Hello Kitty çok sevindi, çünkü rüzgarsız gölgede istediği balonu yapmıştı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esince balonlar hemen ondan uzaklaştı"
   - Cümle 3: «Ama rüzgar esince balonlar hemen ondan uzaklaştı.»
   - Açıklama: Balonların uçup gitmesi doğal olduğu gibi büyük balon yapma hedefinin önünde de bir engel değil, sebep ile hedef bağlanmıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ağacın altına geçti, orada rüzgar yoktu"
   - Cümle 7: «Ağacın altına geçti, orada rüzgar yoktu.»
   - Açıklama: Ağacın gölgesi rüzgarı kesmez; çözüm sebebe akla yatkın biçimde yönelmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra ona küçük balonlar yapıştı"
   - Cümle 10: «Sonra ona küçük balonlar yapıştı.»
   - Açıklama: Rüzgarsız gölgede balona yapışan küçük balonlar ve karnabahar benzetmesi sebepsiz beliriyor ve olaya hizmet etmiyor.
   - Açıklama: Küçük balonlar sebepsiz beliriyor; Hello Kitty yalnız tek büyük balon yapmıştı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "balona arkadaşça el salladı"
   - Cümle 12: «Hello Kitty güldü ve balona arkadaşça el salladı.»
   - Açıklama: 'Arkadaşça' soyut bir kelime ve cansız balona arkadaşça el sallamak mecazlı bir kullanım.
   - Açıklama: 'Arkadaşça' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "balona arkadaşça el salladı"
   - Cümle 12: «Hello Kitty güldü ve balona arkadaşça el salladı.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız bir süs kelimesi olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, yalnız kelime olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0014` birebir aynı, ardından `@onarim: eabec67e8296e2401d613e34b33c2e71897176f9`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0015 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0015
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'para', fiil 'gezdirmek', sıfat 'devasa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kardeşinin kurdelesi başının arkasında bir dala takıldı | kurdeleyi daldan yavaşça çıkardı ve yine bağladı
@tohum: hello_kitty-0015
@degisim: para -> dal
Bir sabah Hello Kitty, Mimi'yi ormandaki kamp yerinde gezdiriyordu. İkisi devasa bir ağacın altından geçti. Birden Mimi'nin sarı kurdelesi alçak bir dala takıldı. Mimi kurdeleyi göremedi, çünkü kurdele başının arkasındaydı. Mimi kurdelesini çok seviyordu ve üzüldü. Hello Kitty en iyi arkadaşına hemen yardım etti. Mimi'nin arkasına geçti ve dala baktı. Kurdele dalın ucuna dolanmıştı. Hello Kitty kurdeleyi daldan yavaşça çözdü. Sonra onu Mimi'nin başına güzelce bağladı. Kurdele hiç bozulmamıştı. Mimi sevinçle gülümsedi ve kardeşine sarıldı. İki kardeş kamp yerini gezmeye mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Mimi'yi ormandaki kamp yerinde gezdiriyordu"
   - Cümle 1: «Bir sabah Hello Kitty, Mimi'yi ormandaki kamp yerinde gezdiriyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; iki çocuk ormanda büyüksüz geziyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İkisi devasa bir ağacın"
   - Cümle 2: «İkisi devasa bir ağacın altından geçti.»
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
   - Açıklama: 'Devasa' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşına hemen yardım"
   - Cümle 6: «Hello Kitty en iyi arkadaşına hemen yardım etti.»
   - Açıklama: Mimi kardeşi olduğu halde 'en iyi arkadaşı' denmesi kimin kastedildiğini belirsizleştiriyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hello Kitty en iyi arkadaşına hemen yardım etti"
   - Cümle 6: «Hello Kitty en iyi arkadaşına hemen yardım etti.»
   - Açıklama: Mimi kardeş olarak anılıyor; 'en iyi arkadaşına' kimi gösterdiğini belirsizleştiriyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Mimi sevinçle gülümsedi ve kardeşine sarıldı"
   - Cümle 12: «Mimi sevinçle gülümsedi ve kardeşine sarıldı.»
   - Açıklama: Mimi önce Hello Kitty'nin en iyi arkadaşı, sonra kardeşi olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0015` birebir aynı, `@degisim: para -> dal` (tutuyorsan), ardından `@onarim: f12867637500e9e37dddb2c6b85d71d58e711ba8`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0016 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0016
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mercan', fiil 'giydirmek', sıfat 'kirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babasının elleri kirliydi ve temiz kazağını giyemedi | kazağı babasına kendisi giydirdi
@tohum: hello_kitty-0016
@degisim: mercan -> kazak
Bir sabah ormandaki kamp yerinde serin bir rüzgar esti. Hello Kitty'nin babası kazağını giymek istedi. Ama çadırı kurarken elleri çok kirli olmuştu. "Temiz kazağı kirletmek istemiyorum," dedi babası. Hello Kitty babasına yardım etmek istedi. "Baba, kollarını kaldır!" dedi Hello Kitty. Babası güldü ve kollarını yukarı uzattı. Hello Kitty kazağı babasına dikkatle giydirdi. Sonra kolları tek tek aşağı çekti. Kazak tertemiz kaldı. "Teşekkürler, kızım, şimdi çok iyiyim!" dedi babası. "Ellerini yıka, sonra birlikte yaptığımız kurabiyeleri yiyelim!" dedi Hello Kitty. Hello Kitty bundan sonra kampta babasına hep yardım etti.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Temiz kazağı kirletmek istemiyorum"
   - Cümle 4: «"Temiz kazağı kirletmek istemiyorum," dedi babası.»
   - Açıklama: Babası ellerini yıkayarak sorunu hemen çözebilir, sonda da el yıkama öneriliyor; sorun yapay kalıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kazağı babasına dikkatle giydirdi"
   - Cümle 8: «Hello Kitty kazağı babasına dikkatle giydirdi.»
   - Açıklama: Sebep kirli eller ama çözüm elleri temizlemiyor; eller yıkanmak yerine sonraya bırakılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra kolları tek tek"
   - Cümle 9: «Sonra kolları tek tek aşağı çekti.»
   - Açıklama: 'Kolları' babanın kollarını mı kazağın kollarını mı gösterdiği belli değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra kolları tek tek aşağı çekti"
   - Cümle 9: «Sonra kolları tek tek aşağı çekti.»
   - Açıklama: 'Kolları' kazağın kollarını mı babanın kollarını mı gösteriyor belli değil.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra kolları tek tek aşağı çekti"
   - Cümle 9: «Sonra kolları tek tek aşağı çekti.»
   - Açıklama: Kirli eller kolların içinden geçtiği halde kazağın tertemiz kaldığı söyleniyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kazak tertemiz kaldı"
   - Cümle 10: «Kazak tertemiz kaldı.»
   - Açıklama: Kazak giyilirken kirli eller kollardan geçmek zorunda olduğu halde kazağın temiz kaldığı söyleniyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "birlikte yaptığımız kurabiyeleri yiyelim"
   - Cümle 12: «"Ellerini yıka, sonra birlikte yaptığımız kurabiyeleri yiyelim!" dedi Hello Kitty.»
   - Açıklama: Tohumdaki kurabiye özelliği hikayede işe yarar biçimde kullanılmıyor, yalnız sonda anılıyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "birlikte yaptığımız kurabiyeleri yiyelim"
   - Cümle 12: «"Ellerini yıka, sonra birlikte yaptığımız kurabiyeleri yiyelim!" dedi Hello Kitty.»
   - Açıklama: Kurabiyeler sebepsiz beliriyor ve olaya hiçbir katkısı yok.
   - Açıklama: Kurabiyeler hikayede kurulmadan sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0016` birebir aynı, `@degisim: mercan -> kazak` (tutuyorsan), ardından `@onarim: 4b3095fc07b260e00d5d52604b42007bae240224`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0017 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0017
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'klasör', fiil 'bitmek', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: yolda küçük kurabiye parçaları bir iz yapmıştı | izin sonuna yürüdü ve sepetin altındaki deliği buldu
@tohum: hello_kitty-0017
@degisim: klasör -> delik
Hello Kitty annesiyle parkta piknik yapıyordu. Birden yolda küçük parçalar gördü. Parçalar bir iz gibi çimenlere doğru uzanıyordu. "Anne, bu iz nereden geliyor?" diye sordu Hello Kitty. "Gel, izin sonunu birlikte bulalım," dedi annesi. Hello Kitty eğildi ve yerdeki parçalara baktı. Bunlar, evde annesiyle yaptığı yıldız kurabiyelerdendi. İz, ağacın altındaki kıpkırmızı sepetin yanında bitti. Hello Kitty sepeti kaldırıp altına baktı. Sepetin altında küçük bir delik vardı! Kurabiye parçaları yolda bu delikten dökülmüştü. "Bu deliği evde birlikte onarırız," dedi annesi. Hello Kitty çok sevindi, çünkü izin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yolda küçük kurabiye parçaları bir iz yapmıştı"
   - Cümle 0 (plan satırı): «yolda küçük kurabiye parçaları bir iz yapmıştı | izin sonuna yürüdü ve sepetin altındaki deliği buldu»
   - Açıklama: Yolda bir iz görmek gerçek bir sorun değil; asıl sorun olan delikli sepet ise hikayede çözülmüyor.
   - Açıklama: Yerde bir iz görmek bir sorun değil, merak konusu; asıl sorun olan kurabiyelerin dökülmesi sorun olarak kurulmuyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Gel, izin sonunu birlikte bulalım"
   - Cümle 5: «"Gel, izin sonunu birlikte bulalım," dedi annesi.»
   - Açıklama: Çözüm fikrini figür değil annesi veriyor; Hello Kitty yalnız onu izliyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu deliği evde birlikte onarırız"
   - Cümle 12: «"Bu deliği evde birlikte onarırız," dedi annesi.»
   - Açıklama: Sebep olan delik yalnız bulunuyor, çözüm ona yönelmiyor ve onarım sonraya bırakılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0017` birebir aynı, `@degisim: klasör -> delik` (tutuyorsan), ardından `@onarim: e293200c48a53da1273ba13692103dd61ce644c9`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0018 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0018
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'ot', fiil 'dokunmak', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: turtanın yuvarlak kapağı çok sıkıydı | babasından yardım istedi ve babası kapağı çevirdi
@tohum: hello_kitty-0018
Hello Kitty babasıyla parkta, yumuşak otların üstünde oturuyordu. Yanlarında en sevdiği elmalı turtanın kabı vardı. Ama kabın yuvarlak kapağı çok sıkıydı ve açılmadı. Hello Kitty kapağı iki eliyle çevirdi. Kapak hiç kıpırdamadı. "Baba, bu kapağı açmama yardım eder misin?" diye sordu Hello Kitty. "Tabii, kızım," dedi babası. Babası kabı sıkıca tuttu ve kapağı güçlü bir şekilde çevirdi. Kapak hemen açıldı. Turtanın güzel kokusu otların üstüne yayıldı. Hello Kitty sevinçle babasının koluna dokundu. "Teşekkürler, babacığım," dedi Hello Kitty. İkisi turtayı birlikte yedi. Hello Kitty bundan sonra sıkı bir kapak görünce babasından yardım istedi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "turtanın yuvarlak kapağı çok"
   - Cümle 0 (plan satırı): «turtanın yuvarlak kapağı çok sıkıydı | babasından yardım istedi ve babası kapağı çevirdi»
   - Açıklama: Turtanın kapağı olmaz; kapak turtanın kabına aittir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "turtanın yuvarlak kapağı çok sıkıydı"
   - Cümle 0 (plan satırı): «turtanın yuvarlak kapağı çok sıkıydı | babasından yardım istedi ve babası kapağı çevirdi»
   - Açıklama: Turtanın kapağı olmaz; kapak turtanın kabına ait.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0018` birebir aynı, ardından `@onarim: c28fbbe67b2dbb6bb2156b6afb425cdbab261818`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0019 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0019
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'fener', fiil 'oturtmak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: çantanın kapağı açık kaldı ve kurabiye kutusu düştü | fenerle çadırın içine baktı ve kutuyu buldu
@tohum: hello_kitty-0019
Ağaçlarda kuşlar ötüyordu. Hello Kitty kamp yerinde çantasını açtı ama kurabiye kutusu yoktu. Çantanın kapağı açık kalmıştı ve kutu bir yere düşmüştü. Kutuda evde yaptığı yıldız kurabiyeler vardı. Hello Kitty kütüğün yanına ve ağaçların dibine baktı. Kutu orada da yoktu. Sonra çadırın karanlık köşesinde gizemli bir şekil gördü. Hello Kitty girişteki feneri alıp açtı ve içeri tuttu. Işıkta şekil belli oldu: bu, onun kurabiye kutusuydu! Hello Kitty çantayı çadırdan alırken kutu içeri düşmüştü. Hello Kitty kutuyu çıkardı ve kütüğün üstüne oturttu. Kapağı açtı, kurabiyelerin hepsi yerindeydi. Hello Kitty yıldız kurabiyelerden birini aldı ve mutlu mutlu yedi.
```

**Hakem bulguları (7):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde çantasını açtı"
   - Cümle 2: «Hello Kitty kamp yerinde çantasını açtı ama kurabiye kutusu yoktu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormandaki kamp yerinde büyüksüz yalnız.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çantasını açtı ama kurabiye kutusu yoktu"
   - Cümle 2: «Hello Kitty kamp yerinde çantasını açtı ama kurabiye kutusu yoktu.»
   - Açıklama: Hello Kitty çantasını açıyor ama hemen ardından çantanın kapağının açık kaldığı söyleniyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yıldız kurabiyeler vardı"
   - Cümle 4: «Kutuda evde yaptığı yıldız kurabiyeler vardı.»
   - Açıklama: Tamlama eki eksik; 'yıldız kurabiyeleri' olmalı.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yaptığı yıldız kurabiyeler vardı"
   - Cümle 4: «Kutuda evde yaptığı yıldız kurabiyeler vardı.»
   - Açıklama: Tamlama eki eksik; 'yıldız kurabiyeleri' olmalı.
5. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "çadırın karanlık köşesinde gizemli bir şekil"
   - Cümle 7: «Sonra çadırın karanlık köşesinde gizemli bir şekil gördü.»
   - Açıklama: Karanlık köşede gizemli şekil küçük çocuk için korkutucu bir öğedir.
   - Açıklama: Karanlık köşede gizemli bir şekil küçük çocuk için korkutucu bir öğe.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gizemli bir şekil gördü"
   - Cümle 7: «Sonra çadırın karanlık köşesinde gizemli bir şekil gördü.»
   - Açıklama: 'Gizemli' 3 yaşındaki çocuk için soyut bir kelime.
   - Açıklama: 'Gizemli' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kütüğün üstüne oturttu"
   - Cümle 11: «Hello Kitty kutuyu çıkardı ve kütüğün üstüne oturttu.»
   - Açıklama: Kutu için 'oturtmak' uygun değil; 'koydu' olmalı.
   - Açıklama: Kutu oturtulmaz; 'koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0019` birebir aynı, ardından `@onarim: 03dab3a422ca77c66cf8317c674d0f391a69b249`, sonra gövde.
