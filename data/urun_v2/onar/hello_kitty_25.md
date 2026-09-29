# Editör görevi (onarım): Hello Kitty, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar25.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0090 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0090
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'başörtüsü', fiil 'koymak', sıfat 'sakin'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: başörtüsünü sormadan alınca kardeşi üzüldü | özür dileyip başörtüsünü geri verdi ve turtasını paylaştı
@tohum: hello_kitty-0090
Hello Kitty parkta Mimi ile piknik yapıyordu. Mimi'nin yanında sarı bir başörtüsü duruyordu. Hello Kitty onu sormadan aldı ve başına bağlayıp koşmaya başladı. Mimi bir şey demedi ama çok üzüldü. Hello Kitty bunu görünce hemen durdu. Kardeşinin yanına gidip oturdu. "Özür dilerim, Mimi, sana sormadan aldım," dedi Hello Kitty. Başörtüsünü güzelce katladı ve Mimi'nin kucağına koydu. Sonra sepetten en sevdiği elmalı turtayı çıkardı. En büyük dilimi Mimi'ye verdi. Mimi sakin bir sesle, "Teşekkür ederim," dedi. Hello Kitty çok sevindi, çünkü Mimi yeniden gülümsüyordu.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra sepetten en sevdiği elmalı turtayı çıkardı"
   - Cümle 9: «Sonra sepetten en sevdiği elmalı turtayı çıkardı.»
   - Açıklama: Özür ve iade sorunu çözmüşken turta paylaşımı üçüncü bir adım ekliyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra sepetten en sevdiği elmalı turtayı"
   - Cümle 9: «Sonra sepetten en sevdiği elmalı turtayı çıkardı.»
   - Açıklama: Çözüm özür, başörtüsünü geri verme ve turta paylaşma olarak iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0090` birebir aynı, ardından `@onarim: 5cfd43656e709fecb2d051d657e6502df636dccc`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0091 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0091
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yıldız', fiil 'güldürmek', sıfat 'kuru'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: parkta tatlı bir koku geldi | kokuyu tanıyıp babasının çantasında turtayı buldu
@tohum: hello_kitty-0091
Bir öğleden sonra Hello Kitty babasıyla parkta kuru yaprak topluyordu. Birden tatlı bir koku geldi. Hello Kitty bu kokunun nereden geldiğini çok merak etti. Babası burnunu havaya kaldırdı ve komik sesler çıkararak kokladı. Bu, Hello Kitty'yi çok güldürdü. Hello Kitty de gözlerini kapadı ve derin derin kokladı. Gelen koku, en sevdiği elmalı turtanın kokusuydu! Hello Kitty kokunun geldiği yere yürüdü ve babasının çantasını açtı. Çantada üstünde hamurdan yıldızlar olan bir turta vardı. "Baba, bu turta nereden geldi?" diye sordu Hello Kitty. "Onu sana getirdim ama söylemeyi unuttum," dedi babası. Sonra ikisi ağacın gölgesine oturdu ve turtayı mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden tatlı bir koku geldi"
   - Cümle 2: «Birden tatlı bir koku geldi.»
   - Açıklama: Tatlı bir kokunun gelmesi çocuğun önemseyeceği bir sorun değil; hikayede gerçek bir sorun yok.
   - Açıklama: Tatlı bir koku gerçek bir sorun değil, yalnız merak; çözülecek bir dert yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "komik sesler çıkararak kokladı"
   - Cümle 4: «Babası burnunu havaya kaldırdı ve komik sesler çıkararak kokladı.»
   - Açıklama: Turtayı kendisi getiren babanın kokuyu arar gibi koklaması işlevsiz ve olaydan çıkmayan bir ayrıntı.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Gelen koku, en sevdiği elmalı turtanın kokusuydu"
   - Cümle 7: «Gelen koku, en sevdiği elmalı turtanın kokusuydu!»
   - Açıklama: 'Koku' ve 'gelmek' art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0091` birebir aynı, ardından `@onarim: 432dabacfa55f9548c2a80cbb8fc75e5a0e91909`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0092 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0092
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'inci', fiil 'korunmak', sıfat 'işaretli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: inciler ıslak çimenlere döküldü | özür diledi ve incileri toplayıp annesine bileklik yaptı
@tohum: hello_kitty-0092
@degisim: işaretli -> ıslak
Yağmur çadırın üstüne tıp tıp yağıyordu. Hello Kitty annesiyle çadırın içinde yağmurdan korunuyordu. Annesi bileklik yapmak için küçük bir kaba beyaz inciler koymuştu. Hello Kitty zıplayarak oynarken kaba çarptı. Bütün inciler çadırın kapısından ıslak çimenlere döküldü. Annesi incilere baktı ve bir şey demedi. "Özür dilerim, anne, dikkat etmedim," dedi Hello Kitty. Hemen eğildi ve incileri tek tek topladı. Hepsini bir bezle kuruladı ve kaba geri koydu. Sonra incileri bir ipe dizdi ve güzel bir bileklik yaptı. "Bu arkadaşlık bilekliği senin, anne," dedi Hello Kitty. Annesi bilekliği taktı ve ona sarıldı. Sonra ikisi yağmurun sesini dinleyerek mutlu mutlu oyun oynadı.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Bütün inciler çadırın kapısından ıslak çimenlere döküldü"
   - Cümle 5: «Bütün inciler çadırın kapısından ıslak çimenlere döküldü.»
   - Açıklama: Sorun ilk üç cümlede değil, beşinci cümlede ortaya çıkıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 5: «Bütün inciler çadırın kapısından ıslak çimenlere döküldü.»
   - Açıklama: Sorun (incilerin dökülmesi) ilk 3 cümlede değil ancak 5. cümlede söyleniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hepsini bir bezle kuruladı ve kaba geri koydu"
   - Cümle 9: «Hepsini bir bezle kuruladı ve kaba geri koydu.»
   - Açıklama: Çözüm toplama, kurulama, ipe dizme ve bileklik yapma gibi ikiden fazla adıma yayılıyor.
   - Açıklama: Çözüm toplama, kurulama, geri koyma, ipe dizme ve bileklik yapma gibi ikiden fazla adıma yayılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu arkadaşlık bilekliği senin"
   - Cümle 11: «"Bu arkadaşlık bilekliği senin, anne," dedi Hello Kitty.»
   - Açıklama: Anneye verilen bileklik için 'arkadaşlık bilekliği' anlamca uymuyor.
   - Açıklama: Anneye verilen bileklik 'arkadaşlık bilekliği' diye yanlış anlamda adlandırılıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu arkadaşlık bilekliği senin"
   - Cümle 11: «"Bu arkadaşlık bilekliği senin, anne," dedi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız bir bileklik adında geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0092` birebir aynı, `@degisim: işaretli -> ıslak` (tutuyorsan), ardından `@onarim: c9c289648f313b833c468e5ec919038815fe4630`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0093 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0093
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'salatalık', fiil 'anlamak', sıfat 'sevecen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesi takıldı ve salatalıklar yere yuvarlandı | salatalıkları topladı ve sepeti annesiyle birlikte taşıdı
@tohum: hello_kitty-0093
Bir sabah Hello Kitty annesiyle ormanda kamp yerine yürüyordu. Annesinin kolunda ağır bir piknik sepeti vardı. Annesi bir köke takıldı ve salatalıklar sepetten yere yuvarlandı. Annesinin öbür elinde bir şişe su vardı ve iki eli de doluydu. Hello Kitty bunu hemen anladı. Salatalıkları tek tek topladı ve sepete geri koydu. "Anne, iki arkadaş gibi sepeti birlikte taşıyalım," dedi Hello Kitty. Sepeti annesiyle birlikte iki yandan tuttu. İkisi sepeti kamp yerine kadar kolayca taşıdı. Annesi ona sevecen bir yüzle baktı ve teşekkür etti. Hello Kitty bundan sonra dolu elleri görünce hemen yardıma koştu.
```

**Hakem bulguları (9):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "salatalıklar sepetten yere yuvarlandı"
   - Cümle 3: «Annesi bir köke takıldı ve salatalıklar sepetten yere yuvarlandı.»
   - Açıklama: Yere dökülen salatalıklar toplanıp bitiyor; sorun önemsiz ve kendiliğinden kapanan bir olay.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "iki eli de doluydu"
   - Cümle 4: «Annesinin öbür elinde bir şişe su vardı ve iki eli de doluydu.»
   - Açıklama: Dökülen salatalıkların yanına dolu eller ve ağır sepet taşıma diye ikinci bir sorun ekleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iki arkadaş gibi sepeti"
   - Cümle 7: «"Anne, iki arkadaş gibi sepeti birlikte taşıyalım," dedi Hello Kitty.»
   - Açıklama: Benzetme ve mecazlı anlatım küçük çocuğa uygun değil.
   - Açıklama: Benzetme gereksiz ve soyut; anne ile çocuk için 'iki arkadaş gibi' küçük çocuğa uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "iki arkadaş gibi sepeti birlikte taşıyalım"
   - Cümle 7: «"Anne, iki arkadaş gibi sepeti birlikte taşıyalım," dedi Hello Kitty.»
   - Açıklama: Karttaki özellik yeni arkadaşlar edinmek; anneyle 'arkadaş gibi' benzetmesi özelliği işe yarar biçimde kullanmıyor, yalnız kelimeyi yerleştiriyor.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "sepeti birlikte taşıyalım"
   - Cümle 7: «"Anne, iki arkadaş gibi sepeti birlikte taşıyalım," dedi Hello Kitty.»
   - Açıklama: Salatalıklar toplandıktan sonra ağır sepeti taşıma diye ikinci bir sorun çözülüyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ona sevecen bir yüzle"
   - Cümle 10: «Annesi ona sevecen bir yüzle baktı ve teşekkür etti.»
   - Açıklama: 'Sevecen' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sevecen bir yüzle baktı"
   - Cümle 10: «Annesi ona sevecen bir yüzle baktı ve teşekkür etti.»
   - Açıklama: 'Sevecen bir yüzle' soyut bir ifade ve 3 yaşındaki çocuk için anlaşılır değil.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dolu elleri görünce hemen yardıma koştu"
   - Cümle 11: «Hello Kitty bundan sonra dolu elleri görünce hemen yardıma koştu.»
   - Açıklama: 'Dolu elleri görmek' ve 'yardıma koşmak' deyimsel, mecazlı anlatım.
9. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dolu elleri görünce hemen"
   - Cümle 11: «Hello Kitty bundan sonra dolu elleri görünce hemen yardıma koştu.»
   - Açıklama: 'Dolu elleri görmek' mecazlı bir anlatım; somut bir kişi belirtilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0093` birebir aynı, ardından `@onarim: 32118868a043494add4b665bdf4c799f2bed6084`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0094 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0094
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'yağmur', fiil 'esmek', sıfat 'çekingen'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: koşarken kardeşinin oyun kurabiyelerine bastı | özür diledi ve ona yeni kurabiyeler yaptı
@tohum: hello_kitty-0094
Ormanda serin bir rüzgar esiyordu. Yağmurdan sonra Hello Kitty ile Mimi kamp yerinde topraktan oyun kurabiyeleri yapıyordu. Hello Kitty yaprak almak için bakmadan koştu ve Mimi'nin kurabiyelerine bastı. Çekingen Mimi hiçbir şey söylemedi ama çok üzüldü. Hello Kitty bunu gördü ve hemen durdu. "Özür dilerim, Mimi, bakmadan koştum," dedi Hello Kitty. Sonra ıslak topraktan yeni kurabiyeler yaptı. Hepsinin üstüne küçük birer çiçek taktı ve Mimi'ye verdi. Mimi gülümsedi ve kurabiyeyi en öne koydu. İkisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "topraktan oyun kurabiyeleri yapıyordu"
   - Cümle 2: «Yağmurdan sonra Hello Kitty ile Mimi kamp yerinde topraktan oyun kurabiyeleri yapıyordu.»
   - Açıklama: Karttaki özellik kurabiye yapmayı (pişirmeyi) sevmek; hikayede topraktan oyun kurabiyesine çevrilmiş ve karttaki gibi kullanılmamış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çekingen Mimi hiçbir şey"
   - Cümle 4: «Çekingen Mimi hiçbir şey söylemedi ama çok üzüldü.»
   - Açıklama: 'Çekingen' 3 yaşındaki çocuk için soyut bir kelime.
3. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ona yeni kurabiyeler yaptı"
   - Cümle 7: «Sonra ıslak topraktan yeni kurabiyeler yaptı.»
   - Açıklama: Gövdede Hello Kitty yeni kurabiye yapmıyor, yalnız çiçek takıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük birer çiçek taktı"
   - Cümle 8: «Hepsinin üstüne küçük birer çiçek taktı ve Mimi'ye verdi.»
   - Açıklama: Kurabiyeye çiçek takılmaz, konur; fiil nesneye uymuyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kurabiyeyi en öne koydu"
   - Cümle 9: «Mimi gülümsedi ve kurabiyeyi en öne koydu.»
   - Açıklama: Birden çok kurabiye yapılmışken tekil 'kurabiyeyi' hangisini gösterdiği ve 'en öne' neyin önü olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0094` birebir aynı, ardından `@onarim: 3f93c00611f981b8f8349925869d44bd922c76e5`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0095 (deneme 1 -> 2)

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
@plan: ağaçların arkasından garip bir ses geldi | kurabiye kırıntılarını izleyip babasını buldu
@tohum: hello_kitty-0095
@degisim: mısır -> kutu
Ağaçların arkasından kıtır kıtır bir ses geliyordu. Hello Kitty kamp yerinde bu sesi duydu ve çok merak etti. Hemen kurabiye kutusuna baktı. Kutu açıktı ve yerde küçük kırıntılar vardı. Bu kırıntılar onun evde yaptığı yıldız kurabiyelerdendi. Hello Kitty kırıntıların peşinden yakındaki büyük ağaca yürüdü. Ağacın arkasında babası yumuşacık çimenlere oturmuştu. Ağzı kurabiyeyle doluydu. "Baba, bu ses senden mi geliyordu?" diye sordu Hello Kitty. "Evet, kurabiyelerin çok güzel, hepsi kıtır kıtır," dedi babası. Sonra en büyük kurabiyeyi Hello Kitty'ye uzattı. İkisi ağacın altında kurabiyeleri paylaştı ve mutlu mutlu güldü.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hemen kurabiye kutusuna baktı"
   - Cümle 3: «Hemen kurabiye kutusuna baktı.»
   - Açıklama: Sesi duyan Hello Kitty'nin neden kurabiye kutusuna baktığı sebepsiz; ipucu olaydan çıkmıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kırıntıların peşinden yakındaki büyük ağaca yürüdü"
   - Cümle 6: «Hello Kitty kırıntıların peşinden yakındaki büyük ağaca yürüdü.»
   - Açıklama: Hello Kitty ormanda bilinmeyen bir sesin peşinden tek başına gidiyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kırıntıların peşinden yakındaki büyük ağaca yürüdü"
   - Cümle 6: «Hello Kitty kırıntıların peşinden yakındaki büyük ağaca yürüdü.»
   - Açıklama: Hello Kitty ormanda garip bir sesin peşinden tek başına ağaçların arkasına gidiyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0095` birebir aynı, `@degisim: mısır -> kutu` (tutuyorsan), ardından `@onarim: a114ea7b15aaf605f535f484b917f192ce2fdf2a`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0096 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0096
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kese', fiil 'öğrenmek', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: rüzgar esince kurabiye kulesi yıkıldı | büyük kurabiyeleri alta ve küçük olanları üste dizdi
@tohum: hello_kitty-0096
@degisim: gizli -> küçük
Ormandaki kamp yerinde Hello Kitty mutfak oyunu oynuyordu. Yanındaki kesede kurabiyeler vardı ve onlarla bir kütüğün üstünde kule yaptı. Ama rüzgar esti ve kule hemen yıkıldı. Hello Kitty kurabiyelere dikkatle baktı. Onları evde kendisi yapmıştı, kimi büyük, kimi küçüktü. Küçük kurabiyeleri en alta koymuştu. Hello Kitty bu kez en büyük kurabiyeyi en alta koydu. Onun üstüne daha küçük kurabiyeleri sırayla dizdi. En küçük kurabiye en üste çıktı. Rüzgar yine esti ama kule bu kez yıkılmadı. Sonra ellerini çırptı ve kuleye baktı. Hello Kitty çok sevindi, çünkü sağlam bir kule yapmayı öğrenmişti.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ormandaki kamp yerinde Hello Kitty mutfak oyunu oynuyordu"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty mutfak oyunu oynuyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormandaki kamp yerinde büyüksüz yalnız.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ormandaki kamp yerinde Hello Kitty"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty mutfak oyunu oynuyordu.»
   - Açıklama: Hello Kitty ormanda yanında büyük olmadan tek başına; güvenli özellik kullanımı alanı tek başına uzağa gitmeyi yasaklıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yanındaki kesede kurabiyeler vardı"
   - Cümle 2: «Yanındaki kesede kurabiyeler vardı ve onlarla bir kütüğün üstünde kule yaptı.»
   - Açıklama: 'Kese' kelimesi 3 yaşındaki çocuğun bileceği bir kelime değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Onları evde kendisi yapmıştı"
   - Cümle 5: «Onları evde kendisi yapmıştı, kimi büyük, kimi küçüktü.»
   - Açıklama: Güvenli kullanım satırına göre kurabiye bir büyükle birlikte yapılır; burada Hello Kitty kurabiyeleri kendisi yapmış.
   - Açıklama: Güvenli özellik kullanımı alanına göre kurabiye bir büyükle birlikte yapılır, burada tek başına yapılmış.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Onları evde kendisi yapmıştı"
   - Cümle 5: «Onları evde kendisi yapmıştı, kimi büyük, kimi küçüktü.»
   - Açıklama: Tohumdaki kurabiye yapma özelliği karttaki gibi kullanılmıyor; kurabiyeler yalnız kule yapmak için malzeme.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0096` birebir aynı, `@degisim: gizli -> küçük` (tutuyorsan), ardından `@onarim: 661d9590d00b393c8a4031592090a0918dfda822`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0097 (deneme 1 -> 2)

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
Ormandaki kamp yerinde Hello Kitty ile Mimi çadırın önünde oturuyordu. Birden çadırdan tık tık diye bir ses geldi. Hello Kitty sesin nereden geldiğini çok merak etti. Utangaç Mimi ise yerinden kalkmadı. Hello Kitty kardeşinin elini tuttu. "Gel, iki arkadaş birlikte bakalım," dedi Hello Kitty. Mimi başını salladı ve onunla yürüdü. İkisi çadırın arkasına gitti. Orada çadırın direği oynaktı ve rüzgarda bir taşa vuruyordu. Hello Kitty direği toprağa sıkıca bastırdı ve düzeltti. Ses hemen kesildi. Hello Kitty çok sevindi, çünkü sesi Mimi ile birlikte bulmuşlardı.
```

**Hakem bulguları (6):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Utangaç Mimi ise yerinden kalkmadı"
   - Cümle 4: «Utangaç Mimi ise yerinden kalkmadı.»
   - Açıklama: Sesin sebebini bulma sorununun yanına Mimi'nin utangaçlığı ikinci bir sorun olarak ekleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki arkadaş birlikte bakalım"
   - Cümle 6: «"Gel, iki arkadaş birlikte bakalım," dedi Hello Kitty.»
   - Açıklama: Hello Kitty kardeşiyle konuşurken kendilerine 'iki arkadaş' diyor; kelime yanlış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Gel, iki arkadaş birlikte"
   - Cümle 6: «"Gel, iki arkadaş birlikte bakalım," dedi Hello Kitty.»
   - Açıklama: Mimi kardeşi olduğu halde 'iki arkadaş' deniyor; kelime yanlış anlamda.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "iki arkadaş birlikte bakalım"
   - Cümle 6: «"Gel, iki arkadaş birlikte bakalım," dedi Hello Kitty.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği yalnız kardeşe söylenen bir sözde geçiyor ve çözüme katkı vermiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Gel, iki arkadaş birlikte bakalım"
   - Cümle 6: «"Gel, iki arkadaş birlikte bakalım," dedi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir söz olarak geçiyor, sorunu çözen direği düzeltmek; özellik işe yarar biçimde kullanılmıyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Gel, iki arkadaş birlikte bakalım"
   - Cümle 6: «"Gel, iki arkadaş birlikte bakalım," dedi Hello Kitty.»
   - Açıklama: Mimi kardeşi olarak anılırken Hello Kitty ona iki arkadaş diye sesleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0097` birebir aynı, `@degisim: biftek -> direk` (tutuyorsan), ardından `@onarim: e39dee67b1691cb77ac29e04f6bbadf717ac013c`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0099 (deneme 1 -> 2)

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
@plan: eldiven büyük olduğu için top içinden düşüyordu | turtanın son dilimini yiyip boş tabakla topu yakaladı
@tohum: hello_kitty-0099
Bir sabah Hello Kitty babasıyla parkta top yakalama oyunu oynuyordu. Babası ona büyük, yeşil bir eldiven vermişti. Ama eldiven çok büyüktü ve top her seferinde içinden düşüyordu. Babası güldü ve birkaç adım geri çekildi. "Bir daha deneyelim," dedi babası. Top yine eldivenden kaydı ve çimenlere yuvarlandı. Hello Kitty piknik örtüsüne baktı. Orada en sevdiği elmalı turtanın son dilimi duruyordu. Dilimi afiyetle yedi ve boş tabağı iki eliyle tuttu. Babası topu yavaşça attı. Top tabağın tam ortasına düştü ve orada kaldı. Babası sevinçle ellerini çırptı. Hello Kitty çok sevindi, çünkü sonunda topu yakalamıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği elmalı turtanın son dilimi"
   - Cümle 8: «Orada en sevdiği elmalı turtanın son dilimi duruyordu.»
   - Açıklama: Turta ve tabak çözümü sebepsizce getiriyor; turtayı yemek sorunla ilgisiz.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "boş tabağı iki eliyle tuttu"
   - Cümle 9: «Dilimi afiyetle yedi ve boş tabağı iki eliyle tuttu.»
   - Açıklama: Sorunun sebebi büyük eldiven ama çözüm eldivene değil, sebepsiz bir tabağa yöneliyor.
   - Açıklama: Sorunun sebebi büyük eldiven ama çözüm eldivene yönelmiyor, ilgisiz bir tabakla sorunu atlıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dilimi afiyetle yedi ve boş tabağı"
   - Cümle 9: «Dilimi afiyetle yedi ve boş tabağı iki eliyle tuttu.»
   - Açıklama: Turta dilimini yemek sorunla ilgisiz bir ayrıntı ve tabak çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0099` birebir aynı, ardından `@onarim: d5970923aff73070a48f1256bdac4a3cf539bb02`, sonra gövde.
