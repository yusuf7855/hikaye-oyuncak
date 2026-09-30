# Editör görevi (onarım): Hello Kitty, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0032 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Bir sabah Hello Kitty ile Mimi parkta elmalı turtayla piknik yapıyordu. Mimi yanında oyuncak bir davul getirmişti. İkisi de aynı anda davula vurdu ve çok gürültülü bir ses çıktı. Hello Kitty durdu ve düşündü. "Sırayla çalalım mı, Mimi? Bekleyen de turta yesin," dedi Hello Kitty. "Olur, ama önce sen çal," dedi Mimi. Hello Kitty davula beş kez vurdu, Mimi de bu sırada turta yedi. Sonra Hello Kitty davulu Mimi'ye verdi ve "Sıra sende, Mimi," dedi. Mimi çalarken Hello Kitty en sevdiği turtadan bir dilim aldı. Şimdi davulun sesi güzel ve neşeliydi. Hello Kitty bundan sonra Mimi ile hep sırayla oynadı.
```

**Hakem bulguları (1):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Sırayla çalalım mı, Mimi?"
   - Cümle 5: «"Sırayla çalalım mı, Mimi?»
   - Açıklama: Mimi kendine adıyla sesleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0032` birebir aynı, `@degisim: damla -> davul` (tutuyorsan), ardından `@onarim: 78923f0f4bcdd0f35dea5919403f77e426f5812c`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0098 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0098
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'çubuk', fiil 'gelmek', sıfat 'hızlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: koşarken masaya çarptı ve kurabiyeler döküldü | özür diledi ve annesiyle yeni kurabiye yaptı
@tohum: hello_kitty-0098
Yağmur cama tıp tıp vuruyordu. Hello Kitty mutfağa çok hızlı koşarak geldi. Masaya çarptı ve annesinin çubuk kurabiyeleri yere döküldü. Hepsi yerde kırılmıştı. Hello Kitty çok üzüldü. "Özür dilerim, anneciğim, yenilerini birlikte yapalım mı?" dedi Hello Kitty. Annesi gülümsedi ve başını salladı. Hello Kitty annesiyle birlikte yeni bir hamur yoğurdu. Sonra hamurdan ince uzun çubuklar yaptı. Annesi tepsiyi fırına koydu. Biraz sonra mutfak tatlı bir kokuyla doldu. Annesi sıcak tepsiyi dikkatle çıkardı. "Teşekkürler, anne, yeni kurabiyeler çok güzel oldu!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "mutfağa çok hızlı koşarak geldi"
   - Cümle 2: «Hello Kitty mutfağa çok hızlı koşarak geldi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde mutfakta hızla koşup masaya çarpılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0098` birebir aynı, ardından `@onarim: 6b65181284c6421df3b9a2d375a866aa636ef7d5`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0100 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0100
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yapıştırıcı', fiil 'tamamlanmak', sıfat 'harika'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kardeşini kutlamak için hiç hediyesi yoktu | kağıt ve yapıştırıcıyla bir turta yaptı
@tohum: hello_kitty-0100
Bir sabah Hello Kitty ile Mimi, aileleriyle ormanda kamp yapıyordu. Mimi sarı kurdelesini ilk kez kendisi bağlamıştı. Hello Kitty buna küçük bir kutlama yapmak istedi, ama hiç hediyesi yoktu. Sepette yalnız renkli kağıtlar ve bir yapıştırıcı vardı. Hello Kitty onlarla en sevdiği elmalı turtayı kağıttan yapmaya başladı. Önce kahverengi bir kağıdı yuvarlak yırttı. Üstüne kırmızı kağıtlardan küçük elmalar yapıştırdı. Böylece turta tamamlandı. Hello Kitty onu Mimi'ye uzattı. "Bu turta senin için, Mimi!" dedi Hello Kitty. Mimi utangaç bir yüzle gülümsedi. "Bu harika bir sürpriz!" dedi Mimi. Hello Kitty bundan sonra küçük bir kutlama için hep kağıttan turta yaptı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mimi, aileleriyle ormanda kamp"
   - Cümle 1: «Bir sabah Hello Kitty ile Mimi, aileleriyle ormanda kamp yapıyordu.»
   - Açıklama: İkiz kardeşlerin ailesi tektir; 'ailesiyle' olmalı.
   - Açıklama: Hello Kitty ile Mimi kardeş olduğu için 'aileleriyle' yanlış; 'ailesiyle' olmalı.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hello Kitty bundan sonra küçük bir kutlama için hep kağıttan turta yaptı"
   - Cümle 13: «Hello Kitty bundan sonra küçük bir kutlama için hep kağıttan turta yaptı.»
   - Açıklama: Son cümle olaydan çıkan bir ders değil, gelecekteki bir alışkanlığa zaman atlaması yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0100` birebir aynı, ardından `@onarim: 4c9134519c8ebb1abf64643ba35b8fcfb04b5c98`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0101 (deneme 2 -> 3)

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
@plan: kuru yapraklar yüzünden hiç elma göremedi | elmanın kokusunu tanıdı ve elmaları buldu
@tohum: hello_kitty-0101
@degisim: yazmak -> saymak
Hello Kitty güneşli bir sabah ormandaki kamp yerindeydi. Elindeki sepeti turta için elmayla doldurmak istiyordu. Ama hiçbir yerde elma göremedi, çünkü kuru yapraklar yeri örtmüştü. Hello Kitty elmalı turtayı çok sevdiği için elma kokusunu iyi biliyordu. Havayı kokladı ve yakında elma olduğunu anladı. Kokunun geldiği yere doğru yürüdü. Kamp yerinin yanındaki büyük bir ağacın dibine geldi. Yaprakları elleriyle yavaşça kenara itti. Altında kırmızı elmalar vardı! Hello Kitty onları tek tek saydı ve sepetine koydu. Tam beş tane vardı ve sepet doldu. Hello Kitty sevinçli bir yüzle sepetini kamp yerine taşıdı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "elma kokusunu iyi biliyordu"
   - Cümle 4: «Hello Kitty elmalı turtayı çok sevdiği için elma kokusunu iyi biliyordu.»
   - Açıklama: Özellik elmalı turtayı sevmek; kartta olmayan bir koku alma yeteneğine dönüştürülüyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kokunun geldiği yere doğru yürüdü"
   - Cümle 6: «Kokunun geldiği yere doğru yürüdü.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde figür ormanda tek başına kokuyu izleyip yerden yiyecek topluyor.
   - Açıklama: Kartın güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmediğini söylüyor, ama Hello Kitty ormanda yanında büyük olmadan kokuyu izleyerek yürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0101` birebir aynı, `@degisim: yazmak -> saymak` (tutuyorsan), ardından `@onarim: e67a27dd25a267fb92cd7473cc605e09ae431653`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0102 (deneme 2 -> 3)

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
Bir sabah Hello Kitty ile annesi parkta piknik yapıyordu. Hello Kitty annesine sürpriz bir çiçek tacı yapmak istedi. Ama annesi hep ona bakıyordu ve sürpriz gizli kalmıyordu. Hello Kitty arkadaşlarıyla oynadığı göz kapatma oyununu hatırladı. En güzel elmayı annesine uzattı. "Anne, gözlerini kapat ve bu elmayı ye," dedi Hello Kitty. Annesi gözlerini kapattı ve elmayı çiğnedi. Hello Kitty yerdeki beyaz çiçekleri topladı. Çiçekleri birbirine bağladı ve bir taç yaptı. Tacı annesine taktı. "Şimdi gözlerini açabilirsin," dedi Hello Kitty. Annesi tacı görünce kızına sarıldı. "Sen çok akıllı bir kızsın," dedi annesi. Hello Kitty çok mutlu oldu, çünkü sürprizini gizli tutmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarıyla oynadığı göz kapatma"
   - Cümle 4: «Hello Kitty arkadaşlarıyla oynadığı göz kapatma oyununu hatırladı.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anı olarak anılıyor, yeni arkadaş edinme ya da iyilik olarak işe yaramıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "arkadaşlarıyla oynadığı göz kapatma"
   - Cümle 4: «Hello Kitty arkadaşlarıyla oynadığı göz kapatma oyununu hatırladı.»
   - Açıklama: Kartın yanlar bölümünde Hello Kitty'nin arkadaşları yok; kartta olmayan karakterler anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0102` birebir aynı, ardından `@onarim: e6d76ea8642e9fb6a67937506ffdc490603c1470`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0104 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Hello Kitty babasıyla parkta bir kutu oyunu oynuyordu. Babası üç kutunun üstüne tutkalla aynı yıldızları yapıştırdı. Sonra turtayı bir kutuya koydu, hepsini karıştırdı ve yerini unuttu. "Eyvah, turta hangi kutuda?" dedi babası ve başını kaşıdı. Hello Kitty en sevdiği elmalı turtanın kokusunu çok iyi biliyordu. Kutuları tek tek kokladı. İlk kutu peynir, ikinci kutu ekmek kokuyordu. Üçüncü kutu elmalı turta kokuyordu! Hello Kitty kapağı açtı. "Buldum, baba, turta burada!" dedi Hello Kitty. "Sen çok zekisin, kızım!" dedi babası ve güldü. Hello Kitty çok sevindi, çünkü turtayı kokusundan bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İlk kutu peynir, ikinci kutu ekmek kokuyordu"
   - Cümle 7: «İlk kutu peynir, ikinci kutu ekmek kokuyordu.»
   - Açıklama: Peynir ve ekmek kutuları hiç kurulmadan beliriyor; babası yalnız turtayı bir kutuya koymuştu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0104` birebir aynı, `@degisim: toplanmak -> koklamak` (tutuyorsan), ardından `@onarim: d77617be4c535dbd54442da43bce4d3eb3547eae`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0105 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0105
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'erik', fiil 'örmek', sıfat 'sert'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: turtanın yanından tık tık diye bir ses geldi | kutuya baktı ve sesi yapan erikleri buldu
@tohum: hello_kitty-0105
@degisim: örmek -> oturmak
Parkta tık tık diye garip bir ses geliyordu. Hello Kitty annesiyle bir ağacın gölgesinde oturuyordu. Hello Kitty bu sesin nereden geldiğini çok merak etti. Ses, en sevdiği elmalı turtanın yanından geliyordu. Hello Kitty hemen turtanın kutusuna baktı. Kapağın üstünde küçük yeşil bir erik vardı. Tam o sırada yukarıdan bir erik daha düştü. Kapağa çarptı ve tık diye ses çıkardı. "Anne, ses erik ağacından geliyor!" dedi Hello Kitty. Annesi düşen meyveyi eline aldı ve sıktı. "Bunlar çok sert, rüzgar onları düşürüyor," dedi annesi. Sonra Hello Kitty ile annesi turtayı mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Parkta tık tık diye garip bir ses geliyordu"
   - Cümle 1: «Parkta tık tık diye garip bir ses geliyordu.»
   - Açıklama: Sorun yalnız merak edilen önemsiz bir ses; kimseye ya da turtaya bir zarar yok ve sesin kaynağına bakınca hikaye bitiyor.
   - Açıklama: Sorun yalnızca merak uyandıran bir ses; çözülmesi gereken, çocuğun önemseyeceği gerçek bir sorun yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği elmalı turtanın yanından geliyordu"
   - Cümle 4: «Ses, en sevdiği elmalı turtanın yanından geliyordu.»
   - Açıklama: Tohumdaki turta özelliği yalnız sesin yerini gösteren bir süs olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0105` birebir aynı, `@degisim: örmek -> oturmak` (tutuyorsan), ardından `@onarim: c74303f3a9d97375f89c6c66812fa2cd6af04970`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0106 (deneme 2 -> 3)

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
@plan: bir fotoğraf kayıptı ve duvarda yer boş kaldı | sesi merak edip yatağın altında fotoğrafı buldu
@tohum: hello_kitty-0106
Hello Kitty ile Mimi odada fotoğrafları toplayıp duvara asıyordu. Duvarda bir yer boş kaldı, çünkü bir fotoğraf kayıptı. O sırada yatağın altından küçük bir ses geldi. Hello Kitty sesi çok merak etti ve yatağın altına baktı. Orada kayıp fotoğraf vardı. Açık pencereden gelen rüzgar onu hışır hışır sallıyordu. Hello Kitty fotoğrafı eline aldı. Fotoğrafta Hello Kitty, parkta yeni tanıştığı arkadaşlarıyla gülüyordu. "Buldum, Mimi, bu benim en sevdiğim fotoğraf!" dedi Hello Kitty. "Sesi rüzgar yapıyormuş," dedi Mimi utangaç bir sesle. Hello Kitty fotoğrafı duvarda boş kalan yere astı. Sonra ikisi fotoğraflara bakıp mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çünkü bir fotoğraf kayıptı"
   - Cümle 2: «Duvarda bir yer boş kaldı, çünkü bir fotoğraf kayıptı.»
   - Açıklama: Fotoğrafın neden kaybolduğu söylenmiyor; sorunun sebebi yok.
   - Açıklama: Fotoğrafın neden kaybolduğu ve yatağın altına nasıl gittiği söylenmiyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "yatağın altından küçük bir ses geldi"
   - Cümle 3: «O sırada yatağın altından küçük bir ses geldi.»
   - Açıklama: Yatağın altından gelen gizemli ses küçük çocuk için korkutucu olabilir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada yatağın altından küçük bir ses geldi"
   - Cümle 3: «O sırada yatağın altından küçük bir ses geldi.»
   - Açıklama: Çözüm figürün bir eyleminden değil, tam o anda tesadüfen gelen bir sesten çıkıyor.
   - Açıklama: Çözümü tesadüfen beliren bir ses getiriyor; figür fotoğrafı aramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty sesi çok merak etti"
   - Cümle 4: «Hello Kitty sesi çok merak etti ve yatağın altına baktı.»
   - Açıklama: Tohumdaki özellik arkadaş edinmek; sorunu merak çözüyor, yani ikinci bir özellik ekleniyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "parkta yeni tanıştığı arkadaşlarıyla gülüyordu"
   - Cümle 8: «Fotoğrafta Hello Kitty, parkta yeni tanıştığı arkadaşlarıyla gülüyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız fotoğrafta anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0106` birebir aynı, ardından `@onarim: c499abd8c14e553051c3fc27c58edbf422a59ed2`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0107 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0107
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kilit', fiil 'boyamak', sıfat 'temiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası yemeğini evde unuttu ve acıktı | en sevdiği turtayı ikiye böldü ve babasıyla paylaştı
@tohum: hello_kitty-0107
Ağaçlarda kuşlar ötüyordu. Hello Kitty babasıyla parkta resim boyuyordu. Acıkınca babası çantasına baktı ama yemeği yoktu. Kapının kilidine bakarken onu evde, masanın üstünde unutmuştu. Hello Kitty'nin çantasında en sevdiği elmalı turta vardı. Önce ikisi boyalı ellerini temiz bir bezle sildi. Sonra Hello Kitty turtayı ikiye böldü. Büyük parçayı babasına uzattı. "Buyur, babacığım, bu parça senin," dedi Hello Kitty. Babası bir ısırık aldı ve gülümsedi. "Çok teşekkürler, kızım, bu çok güzel!" dedi babası. "Ben de seninle yemeyi çok sevdim, baba!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kapının kilidine bakarken onu evde"
   - Cümle 4: «Kapının kilidine bakarken onu evde, masanın üstünde unutmuştu.»
   - Açıklama: 'Onu' zamirinin yemeği mi kilidi mi gösterdiği belli değil; cümle karışık.
   - Açıklama: Cümlenin öznesi eksik ve 'onu' zamirinin neyi gösterdiği açık değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kapının kilidine bakarken onu evde"
   - Cümle 4: «Kapının kilidine bakarken onu evde, masanın üstünde unutmuştu.»
   - Açıklama: Kilide bakma ayrıntısı hiçbir işe yaramıyor ve olayla bağlantısız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0107` birebir aynı, ardından `@onarim: a746da4dc6bc500bc86e812a92c96006b60d4d43`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0108 (deneme 2 -> 3)

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
Ormandaki kamp yerinde yumuşak bir çamur vardı. Hello Kitty orada mutfak oyunu oynuyordu ve çamurdan kurabiyeler yapıyordu. Ama yuvarlak bir kalıbı yoktu ve hepsi yamuk oluyordu. Hello Kitty evde kurabiye yaparken kullandığı kalıbı hatırladı. Yerden ince ve yumuşak bir dal aldı. Dalı yavaşça eğdi ve bir halka yaptı. Uçlarını uzun bir otla sıkıca bağladı. Böylece yeni bir kalıbı oldu. Onu çamura bastırdı ve yuvarlak bir kurabiye çıktı. Sonra aynı biçimde birkaç kurabiye daha yaptı. Hepsini büyük bir yaprağın üstüne güzelce dizdi. Hello Kitty mutfak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty orada mutfak oyunu oynuyordu"
   - Cümle 2: «Hello Kitty orada mutfak oyunu oynuyordu ve çamurdan kurabiyeler yapıyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormanda yalnız oynuyor.
   - Açıklama: Güvenli özellik kullanımı satırına aykırı olarak Hello Kitty ormandaki kamp yerinde yalnız oynuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0108` birebir aynı, `@degisim: kızartma -> kalıp` (tutuyorsan), ardından `@onarim: 9eb4a9542f6cb8470eb4147ab295f388a8350067`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0109 (deneme 2 -> 3)

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
Bir sabah Hello Kitty ile Mimi, aileleriyle ormanda piknik yapıyordu. İkisi de çok acıkmıştı. Ama Mimi kek kutusunu evde unutmuştu. Mimi boş sepetine baktı ve üzgün üzgün başını eğdi. Hello Kitty evde yaptığı kurabiyeleri kilitli bir kutuda getirmişti. Hello Kitty kutuyu açtı ve kurabiyeleri ikiye ayırdı. Yarısını hemen Mimi'ye verdi. Mimi ilk ısırıkta sevinçle miyavladı ve güldü. İkisi yan yana oturup kurabiyeleri birlikte yedi. Hello Kitty çok sevindi, çünkü kardeşi artık aç değildi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurabiyeleri kilitli bir kutuda"
   - Cümle 5: «Hello Kitty evde yaptığı kurabiyeleri kilitli bir kutuda getirmişti.»
   - Açıklama: Piknik kutusu için 'kilitli' yanlış anlamda kullanılmış; kutu anahtarsız açılıyor, 'kapaklı' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kurabiyeleri kilitli bir kutuda getirmişti"
   - Cümle 5: «Hello Kitty evde yaptığı kurabiyeleri kilitli bir kutuda getirmişti.»
   - Açıklama: Kutunun kilitli olduğu önemliymiş gibi kuruluyor ama hiçbir işe yaramıyor, kutu hemen açılıyor.
   - Açıklama: Kutunun kilitli olduğu söyleniyor ama bu hiçbir işe yaramıyor, kutu hemen açılıyor.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "ilk ısırıkta sevinçle miyavladı"
   - Cümle 8: «Mimi ilk ısırıkta sevinçle miyavladı ve güldü.»
   - Açıklama: Kart türü notuna göre Mimi kedi biçiminde bir kızdır ve dizide konuşur; miyavlaması diziyi bilen çocuğa yanlış gelir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0109` birebir aynı, `@degisim: waffle -> kek` (tutuyorsan), ardından `@onarim: 6ce9961625f4052a19e28b58d7dae12bc560b291`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0112 (deneme 2 -> 3)

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
Rüzgar ağaçların arasından hızlı hızlı esiyordu. Hello Kitty ormandaki kamp yerinde turta yiyecekti. Tabureye beyaz bir örtü serdi, ama rüzgar örtüyü uçurdu. Hello Kitty örtüyü yerden aldı ve tekrar serdi. Rüzgar örtüyü bir kez daha havaya kaldırdı. Hello Kitty örtünün düzgün durmasını istiyordu. Birden sepetindeki elmalı turtayı düşündü. Turtanın tabağı büyük ve ağırdı. Hello Kitty turtanın tabağını örtünün tam ortasına koydu. Rüzgar yine esti ama örtü artık uçmadı. Sonra ellerini sabunlu suyla yıkadı ve sabun köpürdü. Hello Kitty bir dilim turta aldı ve mutlu mutlu yedi. Hello Kitty bundan sonra rüzgarlı günlerde örtünün üstüne ağır bir şey koydu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde turta yiyecekti"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde turta yiyecekti.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına aykırı olarak Hello Kitty ormanda tek başına bulunuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra ellerini sabunlu suyla yıkadı ve sabun köpürdü"
   - Cümle 11: «Sonra ellerini sabunlu suyla yıkadı ve sabun köpürdü.»
   - Açıklama: Sabunlu su sebepsizce beliriyor ve olayda hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ellerini sabunlu suyla yıkadı ve sabun köpürdü"
   - Cümle 11: «Sonra ellerini sabunlu suyla yıkadı ve sabun köpürdü.»
   - Açıklama: El yıkama ve sabun olayla ilgisiz, sebepsiz ve işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0112` birebir aynı, `@degisim: sabırlı -> beyaz` (tutuyorsan), ardından `@onarim: 45154cc47c23ce943243b076563b266141367e71`, sonra gövde.
