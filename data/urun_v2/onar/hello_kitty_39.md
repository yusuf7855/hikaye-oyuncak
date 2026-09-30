# Editör görevi (onarım): Hello Kitty, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0032 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0032
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'damla', fiil 'almak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: ikisi de davula aynı anda vurdu | kardeşiyle sırayla davul çaldı
@tohum: hello_kitty-0032
@degisim: damla -> davul
Bir sabah Hello Kitty ile Mimi parkta elmalı turtayla piknik yapıyordu. Mimi yanında oyuncak bir davul getirmişti. İkisi de aynı anda davula vurdu ve çok gürültülü bir ses çıktı. Hello Kitty durdu ve düşündü. "Sırayla çalalım mı? Bekleyen de turta yesin," dedi Hello Kitty. "Olur, ama önce sen çal," dedi Mimi. Hello Kitty davula beş kez vurdu, Mimi de bu sırada turta yedi. Sonra Hello Kitty davulu Mimi'ye verdi ve "Sıra sende, Mimi," dedi. Mimi çalarken Hello Kitty en sevdiği turtadan bir dilim aldı. Şimdi davulun sesi güzel ve neşeliydi. Hello Kitty bundan sonra Mimi ile hep sırayla oynadı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "aynı anda davula vurdu ve çok gürültülü bir ses çıktı"
   - Cümle 3: «İkisi de aynı anda davula vurdu ve çok gürültülü bir ses çıktı.»
   - Açıklama: Oyuncak davulun bir an gürültülü çalması çocuğun önemseyeceği gerçek bir sorun gibi durmuyor; olay önemsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0032` birebir aynı, `@degisim: damla -> davul` (tutuyorsan), ardından `@onarim: e3e73cdc806c52c8c044c40a4256f2d04d720a84`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0101 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0101
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'güneş', fiil 'yazmak', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: kuru yapraklar yüzünden hiç elma göremedi | ağacın altındaki yaprakları itti ve elmaları buldu
@tohum: hello_kitty-0101
@degisim: yazmak -> saymak
Hello Kitty güneşli bir sabah ormandaki kamp yerindeydi. En sevdiği elmalı turta için sepetini elmayla doldurmak istiyordu. Ama hiçbir yerde elma göremedi, çünkü yerde bir sürü kuru yaprak vardı. Kamp yerinde büyük bir elma ağacı vardı. Ama dallarında hiç elma kalmamıştı. Hello Kitty elmaların yere düşmüş olabileceğini düşündü. Ağacın altına gitti ve yaprakları elleriyle yavaşça kenara itti. Altında kırmızı elmalar vardı! Hello Kitty onları tek tek saydı ve sepetine koydu. Tam beş tane vardı ve sepet doldu. Hello Kitty sevinçli bir yüzle sepetini kamp yerine taşıdı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sevinçli bir yüzle sepetini kamp yerine taşıdı"
   - Cümle 11: «Hello Kitty sevinçli bir yüzle sepetini kamp yerine taşıdı.»
   - Açıklama: Hello Kitty ve elma ağacı zaten kamp yerinde olduğu halde sepeti kamp yerine taşıması çelişkili.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sepetini kamp yerine taşıdı"
   - Cümle 11: «Hello Kitty sevinçli bir yüzle sepetini kamp yerine taşıdı.»
   - Açıklama: Elma ağacı zaten kamp yerindeydi, bu yüzden sepeti kamp yerine taşımak çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0101` birebir aynı, `@degisim: yazmak -> saymak` (tutuyorsan), ardından `@onarim: 9115c178ed29840270d904e42292759be81e5fe6`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0102 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0102
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'taç', fiil 'çiğnemek', sıfat 'akıllı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesi hep baktığı için sürpriz gizli kalmıyordu | annesine elma verdi ve gizlice taç yaptı
@tohum: hello_kitty-0102
Bir sabah Hello Kitty ile annesi parkta piknik yapıyordu. Hello Kitty annesine sürpriz bir çiçek tacı yapmak istedi. Ama annesi hep ona bakıyordu ve sürpriz gizli kalmıyordu. Hello Kitty en güzel elmayı iyi bir arkadaş gibi annesine uzattı. "Anne, gözlerini kapat ve bu elmayı ye," dedi Hello Kitty. Annesi gözlerini kapattı ve elmayı çiğnedi. Hello Kitty yerdeki beyaz çiçekleri topladı. Çiçekleri birbirine bağladı ve bir taç yaptı. Tacı annesine taktı. "Şimdi gözlerini açabilirsin," dedi Hello Kitty. Annesi tacı görünce kızına sarıldı. "Sen çok akıllı bir kızsın," dedi annesi. Hello Kitty çok mutlu oldu, çünkü sürprizini gizli tutmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iyi bir arkadaş gibi annesine uzattı"
   - Cümle 4: «Hello Kitty en güzel elmayı iyi bir arkadaş gibi annesine uzattı.»
   - Açıklama: 'İyi bir arkadaş gibi' benzetmesi soyut ve anneye yönelik olduğu için yersiz.
   - Açıklama: Anneye 'arkadaş gibi' benzetmesi yersiz ve soyut.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "iyi bir arkadaş gibi annesine uzattı"
   - Cümle 4: «Hello Kitty en güzel elmayı iyi bir arkadaş gibi annesine uzattı.»
   - Açıklama: Tohumdaki arkadaş özelliği annesine karşı bir benzetmeyle zorla sokulmuş, işe yarar biçimde kullanılmamış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en güzel elmayı iyi bir arkadaş gibi annesine uzattı"
   - Cümle 4: «Hello Kitty en güzel elmayı iyi bir arkadaş gibi annesine uzattı.»
   - Açıklama: Sürprizi gizleyen şey gözlerin kapanması; elma çözümde işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0102` birebir aynı, ardından `@onarim: e20665c63e49ddf4bc86d42fe3f605dcf9b70dc0`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0104 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0104
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'tutkal', fiil 'toplanmak', sıfat 'zeki'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası turtanın hangi kutuda olduğunu unuttu | kutuları tek tek kokladı ve turtayı buldu
@tohum: hello_kitty-0104
@degisim: toplanmak -> koklamak
Hello Kitty babasıyla parkta bir kutu oyunu oynuyordu. Babası üç kutunun üstüne tutkalla aynı yıldızları yapıştırdı. Sonra kutulara peynir, ekmek ve turta koydu. Kutuları karıştırdı ve turtanın yerini unuttu. "Eyvah, turta hangi kutuda?" dedi babası ve başını kaşıdı. Hello Kitty en sevdiği elmalı turtanın kokusunu çok iyi biliyordu. Kutuları tek tek kokladı. İlk kutu peynir, ikinci kutu ekmek kokuyordu. Üçüncü kutu elmalı turta kokuyordu! Hello Kitty kapağı açtı. "Buldum, baba, turta burada!" dedi Hello Kitty. "Sen çok zekisin, kızım!" dedi babası ve güldü. Hello Kitty çok sevindi, çünkü turtayı kokusundan bulmuştu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Sonra kutulara peynir, ekmek ve turta koydu.»
   - Açıklama: Sorun ancak 4. cümlede ortaya çıkıyor, ilk 3 cümlede söylenmiyor.
   - Açıklama: Turtanın yerinin unutulması sorunu ilk 3 cümlede değil 4. cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "turtanın yerini unuttu"
   - Cümle 4: «Kutuları karıştırdı ve turtanın yerini unuttu.»
   - Açıklama: Kutuların kapakları açılabildiği için turtanın yerini unutmak gerçek bir sorun değil ve koklama çözümü gereksiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0104` birebir aynı, `@degisim: toplanmak -> koklamak` (tutuyorsan), ardından `@onarim: e32a92a4d5e7957da11bdbfe7f688e248744671e`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0106 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0106
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fotoğraf', fiil 'toplamak', sıfat 'boş'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: rüzgar bir fotoğrafı uçurdu ve duvarda yer boş kaldı | sesi dinledi ve yatağın altında fotoğrafı buldu
@tohum: hello_kitty-0106
Hello Kitty ile Mimi odada fotoğrafları toplayıp duvara asıyordu. Açık pencereden rüzgar esti ve bir fotoğraf uçup kayboldu. Duvarda bir yer boş kaldı. Kaybolan fotoğraf Mimi'nin en sevdiği fotoğraftı ve Mimi çok üzüldü. Hello Kitty en iyi arkadaşı Mimi'ye yardım etmek istedi. Odada durdu ve dikkatle dinledi. Yatağın yanından hışır hışır bir ses geliyordu. Hello Kitty yatağın altına eğilip baktı. Kayıp fotoğraf oradaydı ve rüzgar onu sallıyordu. "Buldum, Mimi, fotoğrafın burada!" dedi Hello Kitty. "Teşekkürler, sesi rüzgar yapıyormuş," dedi Mimi utangaç bir sesle. Hello Kitty fotoğrafı duvarda boş kalan yere astı. Sonra ikisi fotoğraflara bakıp mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Kaybolan fotoğraf Mimi'nin en sevdiği fotoğraftı"
   - Cümle 4: «Kaybolan fotoğraf Mimi'nin en sevdiği fotoğraftı ve Mimi çok üzüldü.»
   - Açıklama: Aynı cümlede 'fotoğraf' gereksiz yere tekrarlanıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı Mimi'ye"
   - Cümle 5: «Hello Kitty en iyi arkadaşı Mimi'ye yardım etmek istedi.»
   - Açıklama: Mimi zaten tanıtılmışken 'en iyi arkadaşı' diye yeniden tanıtılıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedi Mimi utangaç bir sesle"
   - Cümle 11: «"Teşekkürler, sesi rüzgar yapıyormuş," dedi Mimi utangaç bir sesle.»
   - Açıklama: 'Utangaç' teşekkür ve sevinç anına uymuyor; kelime yerinde değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dedi Mimi utangaç bir sesle"
   - Cümle 11: «"Teşekkürler, sesi rüzgar yapıyormuş," dedi Mimi utangaç bir sesle.»
   - Açıklama: Kimse sesin kaynağını sormamışken Mimi'nin sesi rüzgarın yaptığını söylemesi ve utangaçlığı olaydan çıkmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sesi rüzgar yapıyormuş," dedi Mimi utangaç bir sesle"
   - Cümle 11: «"Teşekkürler, sesi rüzgar yapıyormuş," dedi Mimi utangaç bir sesle.»
   - Açıklama: Mimi'nin utangaç tepkisi ve rüzgar açıklaması olaydan çıkmıyor, sebepsiz ve işlevsiz bir replik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0106` birebir aynı, ardından `@onarim: 0413478b354d601e9f03a195d623a158951a965c`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0108 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0108
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kızartma', fiil 'eğmek', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: çamur kurabiyeleri kalıp olmadığı için yamuk oluyordu | ince bir dalı eğdi ve yuvarlak bir kalıp yaptı
@tohum: hello_kitty-0108
@degisim: kızartma -> kalıp
Ormandaki kamp yerinde yumuşak bir çamur vardı. Hello Kitty kampta mutfak oyunu oynuyordu ve çamurdan kurabiyeler yapıyordu. Ama yuvarlak bir kalıbı yoktu ve hepsi yamuk oluyordu. Hello Kitty evde kurabiye yaparken kullandığı kalıbı hatırladı. Yerden ince ve yumuşak bir dal aldı. Dalı yavaşça eğdi ve bir halka yaptı. Uçlarını uzun bir otla sıkıca bağladı. Böylece yeni bir kalıbı oldu. Onu çamura bastırdı ve yuvarlak bir kurabiye çıktı. Sonra aynı biçimde birkaç kurabiye daha yaptı. Hepsini büyük bir yaprağın üstüne güzelce dizdi. Hello Kitty mutfak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kampta mutfak oyunu oynuyordu"
   - Cümle 2: «Hello Kitty kampta mutfak oyunu oynuyordu ve çamurdan kurabiyeler yapıyordu.»
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylerken Hello Kitty ormandaki kamp yerinde büyük olmadan yalnız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0108` birebir aynı, `@degisim: kızartma -> kalıp` (tutuyorsan), ardından `@onarim: d75fbc0a95fc7736a06613500b98016dac607b34`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0109 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0109
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'waffle', fiil 'miyavlamak', sıfat 'kilitli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kardeşi kek kutusunu evde unuttu | kurabiyelerini ikiye ayırdı ve yarısını kardeşine verdi
@tohum: hello_kitty-0109
@degisim: waffle -> kek
Bir sabah Hello Kitty ile Mimi ormanda piknik yapıyordu. İkisi de çok acıkmıştı. Ama Mimi kek kutusunu evde unutmuştu. Mimi boş sepetine baktı ve üzgün üzgün başını eğdi. Hello Kitty evde yaptığı kurabiyeleri küçük bir kutuda getirmişti. Kutu kilitliydi, bu yüzden kurabiyeler yolda hiç dökülmemişti. Hello Kitty anahtarla kutuyu açtı ve kurabiyeleri ikiye ayırdı. Yarısını hemen Mimi'ye verdi. Mimi ilk ısırıkta sevinçle güldü ve şakayla miyavladı. İkisi yan yana oturup kurabiyeleri birlikte yedi. Hello Kitty çok sevindi, çünkü kardeşi artık aç değildi.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutu kilitliydi, bu yüzden kurabiyeler yolda hiç dökülmemişti"
   - Cümle 6: «Kutu kilitliydi, bu yüzden kurabiyeler yolda hiç dökülmemişti.»
   - Açıklama: Kilitli kutu ve anahtar işlevsiz bir ayrıntı; kilidin dökülmeyi önlemesi de sebep olarak tutarsız.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutu kilitliydi, bu yüzden kurabiyeler"
   - Cümle 6: «Kutu kilitliydi, bu yüzden kurabiyeler yolda hiç dökülmemişti.»
   - Açıklama: Kilitli kutu ve anahtar işlevsiz bir ayrıntı olarak kuruluyor ve olaya hiçbir katkı yapmıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sevinçle güldü ve şakayla miyavladı"
   - Cümle 9: «Mimi ilk ısırıkta sevinçle güldü ve şakayla miyavladı.»
   - Açıklama: 'Şakayla miyavlamak' anlamsız bir kullanım; kelime fiile uymuyor.
   - Açıklama: 'Şakayla miyavlamak' anlamca uygunsuz, kelime yanlış kullanılmış.
4. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "şakayla miyavladı"
   - Cümle 9: «Mimi ilk ısırıkta sevinçle güldü ve şakayla miyavladı.»
   - Açıklama: Kartta Mimi konuşan bir kedi kız olarak geçer; dizideki karakter gibi konuşmak yerine hayvan gibi miyavlaması figür dünyasına yanlış bilgi katıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0109` birebir aynı, `@degisim: waffle -> kek` (tutuyorsan), ardından `@onarim: 761e2226837e26c4a0862f98e36b02b04e7b6358`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0112 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0112
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'tabure', fiil 'köpürmek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: rüzgar tabureye serilen örtüyü uçurdu | ağır turta tabağını örtünün ortasına koydu
@tohum: hello_kitty-0112
@degisim: sabırlı -> beyaz
Rüzgar hızlı hızlı esiyordu. Hello Kitty ormandaki kamp yerindeydi ve turta yiyecekti. Tabureye beyaz bir örtü serdi, ama rüzgar örtüyü uçurdu. Hello Kitty örtüyü yerden aldı ve tekrar serdi, ama elleri kirlendi. Rüzgar örtüyü bir kez daha havaya kaldırdı. Hello Kitty örtünün düzgün durmasını istiyordu. Birden sepetindeki elmalı turtayı düşündü. Turtanın tabağı büyük ve ağırdı. Hello Kitty turtanın tabağını örtünün tam ortasına koydu. Rüzgar yine esti ama örtü artık uçmadı. Sonra kirli ellerini sabunla yıkadı ve sabun köpürdü. Hello Kitty bir dilim turta aldı ve mutlu mutlu yedi. Hello Kitty bundan sonra rüzgarlı günlerde örtünün üstüne ağır bir şey koydu.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerindeydi"
   - Cümle 2: «Hello Kitty ormandaki kamp yerindeydi ve turta yiyecekti.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda yetişkinsiz yalnız.
   - Açıklama: Güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmediğini söylerken Hello Kitty yanında büyük olmadan ormanda tek başına.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "serdi, ama elleri kirlendi"
   - Cümle 4: «Hello Kitty örtüyü yerden aldı ve tekrar serdi, ama elleri kirlendi.»
   - Açıklama: 'Ama' bağlacı karşıtlık olmayan iki olayı bağlıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "ama elleri kirlendi"
   - Cümle 4: «Hello Kitty örtüyü yerden aldı ve tekrar serdi, ama elleri kirlendi.»
   - Açıklama: Uçan örtünün yanında ellerin kirlenmesi ikinci bir sorun olarak ekleniyor.
   - Açıklama: Uçan örtünün yanında kirlenen eller ikinci bir sorun olarak ekleniyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kirli ellerini sabunla yıkadı ve sabun köpürdü"
   - Cümle 11: «Sonra kirli ellerini sabunla yıkadı ve sabun köpürdü.»
   - Açıklama: Ormandaki kamp yerinde sabun sebepsizce beliriyor ve bu olay ana sorunla ilgisiz.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra kirli ellerini sabunla yıkadı ve sabun köpürdü"
   - Cümle 11: «Sonra kirli ellerini sabunla yıkadı ve sabun köpürdü.»
   - Açıklama: Ormandaki kamp yerinde sabun sebepsiz beliriyor ve asıl olaya bağlı değil.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra rüzgarlı günlerde örtünün üstüne ağır bir şey koydu"
   - Cümle 13: «Hello Kitty bundan sonra rüzgarlı günlerde örtünün üstüne ağır bir şey koydu.»
   - Açıklama: 'Bundan sonra ... günlerde' alışkanlık bildirir; fiil 'koyardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0112` birebir aynı, `@degisim: sabırlı -> beyaz` (tutuyorsan), ardından `@onarim: a43f8bc2bd1d5bb0b6404dd96527d788e1072cb9`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0113 (deneme 3 -> 4)

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
Bir sabah Hello Kitty ormandaki kamp yerindeydi. Yeni arkadaşlara vermek için ilk kez otlardan bileklik yapmayı denedi. Ama yerdeki otlar kuru ve toz doluydu, hemen kırıldı. Hello Kitty kırık otlara baktı ve biraz düşündü. Sonra tozlu yoldan geçti ve yakındaki bir ağacın gölgesine gitti. Orada yumuşak ve yeşil otlar vardı. Hello Kitty birkaç yeşil otu nazikçe kopardı. Otları yavaş yavaş birbirine ördü. Yeşil otlar hiç kırılmadı. Sonunda küçük ve güzel bir bileklik oldu. Hello Kitty çok sevindi, çünkü artık yeni arkadaşlara verecek bir hediyesi vardı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra tozlu yoldan geçti"
   - Cümle 5: «Sonra tozlu yoldan geçti ve yakındaki bir ağacın gölgesine gitti.»
   - Açıklama: Güvenli kullanım satırına aykırı olarak Hello Kitty ormanda yalnız başına yoldan geçip başka yere gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0113` birebir aynı, ardından `@onarim: 3e22c2cccea36d30159689f61fdd68917ed115b7`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0116 (deneme 3 -> 4)

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
@plan: rüzgar kutuyu devirdi ve kurabiyeler yere döküldü | elindeki son kurabiyeyi ikiye kırıp annesiyle paylaştı
@tohum: hello_kitty-0116
@degisim: temkinli -> dikkatli
Parkta ağaçların gölgesinde bir piknik örtüsü vardı. Hello Kitty ile annesi evde birlikte yaptıkları kurabiyeleri ve muffinleri getirmişti. Ama rüzgar örtüyü kaldırdı ve kutu devrildi. Kutu boşaldı ve kurabiyelerle muffinler yere döküldü. Dikkatli annesi hepsini hemen topladı. "Bunları yiyemeyiz," dedi annesi. Artık ikisine yalnız Hello Kitty'nin elindeki kurabiye kalmıştı. Hello Kitty son kurabiyeyi yavaşça ikiye kırdı. "Al, anneciğim, bu yarısı senin," dedi Hello Kitty. "Teşekkürler, tatlım," dedi annesi ve kurabiyeyi yedi. Hello Kitty çok mutlu oldu, çünkü son kurabiyeyi annesiyle paylaşmıştı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurabiyeleri ve muffinleri getirmişti"
   - Cümle 2: «Hello Kitty ile annesi evde birlikte yaptıkları kurabiyeleri ve muffinleri getirmişti.»
   - Açıklama: 'Muffin' yabancı bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Muffin' yabancı bir kelime; 3 yaşındaki bir çocuk bilmeyebilir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Artık ikisine yalnız Hello Kitty'nin elindeki kurabiye kalmıştı"
   - Cümle 7: «Artık ikisine yalnız Hello Kitty'nin elindeki kurabiye kalmıştı.»
   - Açıklama: Bütün kurabiyeler dökülmüşken Hello Kitty'nin elinde sebepsizce bir kurabiye beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yalnız Hello Kitty'nin elindeki kurabiye kalmıştı"
   - Cümle 7: «Artık ikisine yalnız Hello Kitty'nin elindeki kurabiye kalmıştı.»
   - Açıklama: Hello Kitty'nin elindeki kurabiye önceden kurulmadan sebepsiz beliriyor ve çözümü getiriyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty son kurabiyeyi yavaşça ikiye kırdı"
   - Cümle 8: «Hello Kitty son kurabiyeyi yavaşça ikiye kırdı.»
   - Açıklama: Tohumdaki özellik kurabiye yapmayı sevmek; çözüm paylaşmaya dayanıyor ve özellik işe yarar biçimde kullanılmıyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bu yarısı senin"
   - Cümle 9: «"Al, anneciğim, bu yarısı senin," dedi Hello Kitty.»
   - Açıklama: 'Bu yarısı' dilbilgisel değil; 'bunun yarısı senin' ya da 'yarısı senin' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0116` birebir aynı, `@degisim: temkinli -> dikkatli` (tutuyorsan), ardından `@onarim: b38ad04958f431f2a37287b697f3bde8eb08095f`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0117 (deneme 3 -> 4)

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
@plan: annesi çok susamıştı ama suyu bitmişti | kendi dolu şişesini annesine verdi
@tohum: hello_kitty-0117
@degisim: konuşkan -> dolu
Ormandaki kamp yerinde sıcak bir gündü. Hello Kitty ile annesi küçük bir yürüyüşten yeni dönmüştü. Annesi çok susamıştı, ama şişesi bomboştu. "Suyum bitti, kızım," dedi annesi. Hello Kitty'nin şişesi ise daha doluydu. Hello Kitty arkadaşlarına da annesine de hep iyi davranırdı. Şişesini hemen ona uzattı. "Al, anneciğim, bu su senin," dedi Hello Kitty. Annesi serin suyu içti ve gülümsedi. "Çok güzel, teşekkür ederim," dedi annesi. Hello Kitty de sudan biraz tattı. Sonra ikisi ağaçların gölgesinde oturup dinlendi. Hello Kitty çok sevindi, çünkü annesine yardım edebilmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şişesi ise daha doluydu"
   - Cümle 5: «Hello Kitty'nin şişesi ise daha doluydu.»
   - Açıklama: 'Daha doluydu' 'hâlâ dolu' anlamında yanlış kullanılmış; 'daha fazla dolu' diye anlaşılıyor.
   - Açıklama: 'Daha' burada 'hâlâ' anlamında belirsiz, 'daha fazla dolu' diye de anlaşılıyor; 'hâlâ doluydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0117` birebir aynı, `@degisim: konuşkan -> dolu` (tutuyorsan), ardından `@onarim: d37d0b3d4039b312b4582ee13acbb41a28d84533`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0118 (deneme 3 -> 4)

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
@plan: ikizinin büyük yüzüğü küçük bir çukura yuvarlandı | ikizinin elini tuttu, çukura indi ve yüzüğü buldu
@tohum: hello_kitty-0118
Ormandaki kamp yerinde Hello Kitty ile Mimi yaprak topluyordu. Mimi'nin parmağında büyük bir yüzük vardı. Birden yüzük parmağından kaydı ve küçük bir çukura yuvarlandı. Mimi çok üzüldü ama bir şey demedi. Hello Kitty ikizinin üzgün yüzünü gördü. Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı. Hemen Mimi'ye elini uzattı. "Gel, Mimi, birlikte arayalım," dedi Hello Kitty. İkisi el ele yavaşça çukura indi. Aşağıda bir sürü sarı yaprak vardı. Hello Kitty yaprakları tek tek kaldırdı. Sonunda bir yaprağın altında parlayan yüzüğü buldu. Mimi onu sevinçle aldı ve heyecanlı bir sesle teşekkür etti. Birlikte bakınca kayıp yüzük hemen bulundu.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi el ele yavaşça çukura indi"
   - Cümle 9: «İkisi el ele yavaşça çukura indi.»
   - Açıklama: Çocukların yetişkinsiz bir çukura inmesi taklit edilince tehlikeli olabilir.
   - Açıklama: İki küçük çocuk büyük olmadan ormanda bir çukura iniyor; bu taklit edilince tehlikeli bir davranış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayıp yüzük hemen bulundu"
   - Cümle 14: «Birlikte bakınca kayıp yüzük hemen bulundu.»
   - Açıklama: 'Hemen' yanlış; yüzük yapraklar tek tek kaldırıldıktan sonra 'sonunda' bulundu.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kayıp yüzük hemen bulundu"
   - Cümle 14: «Birlikte bakınca kayıp yüzük hemen bulundu.»
   - Açıklama: Yüzük yapraklar tek tek kaldırılıp sonunda bulunmuşken son cümle hemen bulunduğunu söyleyerek çelişiyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Birlikte bakınca kayıp yüzük hemen bulundu"
   - Cümle 14: «Birlikte bakınca kayıp yüzük hemen bulundu.»
   - Açıklama: Son cümle olayı düzce özetliyor ve önceki 'Sonunda' ile çelişen, sıcaklığı olmayan bir kapanış veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0118` birebir aynı, ardından `@onarim: f6ed2e90f17b68b09c5072a200440c8896a67030`, sonra gövde.
