# Editör görevi (onarım): Hello Kitty, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0048 (deneme 3 -> 4)

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
Evde, kahverengi mutfak masasında Hello Kitty ile annesi tuz hamuru yapıyordu. Hello Kitty yeni arkadaşlarına hamurdan komik bir kedi yapmak istedi. Ama hamur çok suluydu ve ellerine yapışıyordu. "Anne, biraz un ve tuz alabilir miyim?" diye sordu Hello Kitty. Annesi unu ve tuzu ona uzattı. Hello Kitty hamura bir kaşık un ve biraz tuz döktü. Sonra hamuru güzelce yoğurdu. Hamur artık ellerine yapışmadı. Hello Kitty küçük bir kedi yaptı. Annesi kediyi görünce gülümsedi. Hello Kitty çok sevindi, çünkü hamur kedisi tam istediği gibi olmuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşlarına hamurdan komik"
   - Cümle 2: «Hello Kitty yeni arkadaşlarına hamurdan komik bir kedi yapmak istedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, çözümde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlarına hamurdan komik bir kedi"
   - Cümle 2: «Hello Kitty yeni arkadaşlarına hamurdan komik bir kedi yapmak istedi.»
   - Açıklama: Kedinin yeni arkadaşlar için yapıldığı kuruluyor ama arkadaşlar bir daha hiç geçmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlarına hamurdan komik bir kedi yapmak istedi"
   - Cümle 2: «Hello Kitty yeni arkadaşlarına hamurdan komik bir kedi yapmak istedi.»
   - Açıklama: Kedinin yeni arkadaşlar için yapılacağı kuruluyor ama arkadaşlar hikayede hiç işe karışmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0048` birebir aynı, ardından `@onarim: 0134e9e1b6766c5e3aafe3291f51df02caf3c32e`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0050 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0050
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'şişe', fiil 'buruşturmak', sıfat 'küçücük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: rüzgar şişeyi devirdi ve kurabiyeler ıslandı | kapalı kutudaki kuru kurabiyeleri kardeşiyle paylaştı
@tohum: hello_kitty-0050
Ormanda sert bir rüzgar esiyordu. Hello Kitty ile Mimi ailece geldikleri kamp yerinde piknik yapıyordu. Birden rüzgar yerdeki su şişesini devirdi. Su, Mimi'nin kağıt üstündeki kurabiyelerine döküldü. Mimi ıslak kağıdı buruşturdu ve üzgünce başını eğdi. Hello Kitty ikizinin yanına oturdu. Çantasından küçücük bir kutu çıkardı. Kutuda evde yaptığı kurabiyeler vardı. Kutunun kapağı sıkıydı, bu yüzden hepsi kuruydu. "Bunlar ikimize de yeter, Mimi," dedi Hello Kitty. Kurabiyelerin yarısını kardeşine verdi. "Çok teşekkür ederim," dedi Mimi sevinçle. Hello Kitty ile Mimi bundan sonra kurabiyeleri hep kapalı bir kutuda taşıdı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden rüzgar yerdeki su şişesini devirdi.»
   - Açıklama: İlk üç cümlede yalnız şişenin devrildiği söyleniyor; asıl sorun olan kurabiyelerin ıslanması ancak 4. cümlede geliyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kurabiyelerin yarısını kardeşine verdi"
   - Cümle 11: «Kurabiyelerin yarısını kardeşine verdi.»
   - Açıklama: Çözüm ıslanan kurabiyelere ya da devrilen şişeye yönelmiyor, yalnız başka kurabiyelerle yerine koyuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0050` birebir aynı, ardından `@onarim: 42ebd7ea9668edd9f2e983162a238c466b009aff`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0052 (deneme 2 -> 3)

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
Bir sabah Hello Kitty odasında yemek oyunu oynuyordu. Oyun hamurundan dört küçük kurabiye yaptı. Ama yatağın üstünde yalnız üç tabak vardı, küçük sarı tabak eksikti. Hello Kitty yastığın arkasına ve battaniyenin altına baktı. Tabak orada da yoktu. Sonra yere eğildi ve yatağın altına girdi. Küçük tabak yataktan kaymış ve oraya düşmüştü. Hello Kitty tabağı aldı ve yatağın altından çıktı. Onu öteki tabakların yanına bıraktı. Artık dört tabak da yan yanaydı. Hello Kitty her tabağa bir kurabiye koydu. Sonra yemek oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "yastığın arkasına ve battaniyenin altına baktı"
   - Cümle 4: «Hello Kitty yastığın arkasına ve battaniyenin altına baktı.»
   - Açıklama: Çözüm birkaç yere bakma denemesinden sonra geliyor ve iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0052` birebir aynı, ardından `@onarim: ffb6f7e5b124e269a178e03359a403b15e85a3c1`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0053 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kavanozun yanından bilinmeyen bir ses geldi | sessizce bekledi ve sesi yapan kozalağı gördü
@tohum: hello_kitty-0053
Hello Kitty ile Mimi parkta bir ağacın gölgesinde piknik yapıyordu. Hello Kitty kurabiye kavanozunu ağacın dibine bıraktı. Birden kavanozun yanından tık diye bir ses geldi. "Bu ses ne, Hello Kitty?" diye sordu utangaç Mimi yavaşça. "Bilmiyorum, hadi sessizce bekleyelim," dedi Hello Kitty. İkisi kavanoza baktı ve hiç konuşmadı. Biraz sonra ağaçtan küçük bir kozalak düştü. Kozalak kavanozun kapağına çarptı ve yine tık diye ses çıktı. "Sesi kozalaklar yapıyormuş, Mimi!" dedi Hello Kitty. Mimi de güldü. Sonra kavanozu açtılar ve kurabiyeleri paylaştılar. İki kardeş çok sevindi, çünkü sesin kozalaklardan geldiğini bulmuşlardı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kurabiye kavanozunu ağacın dibine"
   - Cümle 2: «Hello Kitty kurabiye kavanozunu ağacın dibine bıraktı.»
   - Açıklama: Karttaki özellik kurabiye yapmayı sevmek iken hikayede yalnız bir kurabiye kavanozu geçiyor ve özellik işe yarar biçimde kullanılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kavanozun yanından tık diye bir ses geldi"
   - Cümle 3: «Birden kavanozun yanından tık diye bir ses geldi.»
   - Açıklama: Sorun yalnız zararsız bir sesten ibaret; çocuğun önemseyeceği bir şey risk altında değil.
   - Açıklama: Düşen bir kozalağın çıkardığı tık sesi çocuğun önemseyeceği gerçek bir sorun değil, önemsiz bir olay.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mimi de güldü."
   - Cümle 10: «Mimi de güldü.»
   - Açıklama: Daha önce kimse gülmediği için 'de' bağlacı yanlış anlam veriyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kavanozu açtılar ve kurabiyeleri paylaştılar"
   - Cümle 11: «Sonra kavanozu açtılar ve kurabiyeleri paylaştılar.»
   - Açıklama: Karttaki özellik kurabiye yapmayı sevmek; kurabiye yalnız yiyecek olarak geçiyor ve sorunun çözümüne katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0053` birebir aynı, ardından `@onarim: 692bf11e50efc08108ecec2f89ca424d34637ba0`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0055 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0055
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'sabun', fiil 'susamak', sıfat 'sevimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: küçük bir kedi sıcakta çok susamıştı | kurabiye kutusunun kapağına su döküp kediye verdi
@tohum: hello_kitty-0055
@degisim: sabun -> kutu
Hello Kitty ile Mimi parkta ağacın gölgesinde oturuyordu. Birden yanlarına sevimli küçük bir kedi geldi. Kedi yere oturdu ve hızlı hızlı soludu, çünkü sıcakta çok susamıştı. "Bu kedi su istiyor galiba," dedi Mimi yavaşça. Hello Kitty'nin yanında bir şişe su ve evde yaptığı kurabiyelerin kutusu vardı. Hello Kitty kutunun kapağına biraz su döktü. Kapağı yavaşça kedinin önüne bıraktı. Kedi hemen suyu içmeye başladı. Mimi sevinçle ellerini çırptı. Kedi suyu bitirince neşeyle miyavladı. "Bak, Mimi, küçük kedi artık çok mutlu!" dedi Hello Kitty.
```

**Hakem bulguları (6):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "yanlarına sevimli küçük bir kedi geldi"
   - Cümle 2: «Birden yanlarına sevimli küçük bir kedi geldi.»
   - Açıklama: Başlıktaki Yan alanında yalnız Mimi var, kartın 'yanlar' bölümünde olmayan bir kedi olaya katılıyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Birden yanlarına sevimli küçük bir kedi geldi"
   - Cümle 2: «Birden yanlarına sevimli küçük bir kedi geldi.»
   - Açıklama: Başlıktaki yan yalnız Mimi, kartın yanlar bölümünde olmayan bir kedi olaya katılıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "yanlarına sevimli küçük bir kedi geldi"
   - Cümle 2: «Birden yanlarına sevimli küçük bir kedi geldi.»
   - Açıklama: Kartta hayvan arkadaş ya da başka bir kedi karakteri yok.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Birden yanlarına sevimli küçük bir kedi geldi"
   - Cümle 2: «Birden yanlarına sevimli küçük bir kedi geldi.»
   - Açıklama: Kartta Hello Kitty'nin hayvan arkadaşı ya da başka kedi karakteri yok.
5. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "hızlı hızlı soludu, çünkü sıcakta çok susamıştı"
   - Cümle 3: «Kedi yere oturdu ve hızlı hızlı soludu, çünkü sıcakta çok susamıştı.»
   - Açıklama: Sıcakta sıkıntı çeken bir hayvan acı ya da hastalık izlenimi veriyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kapağı yavaşça kedinin önüne bıraktı"
   - Cümle 7: «Kapağı yavaşça kedinin önüne bıraktı.»
   - Açıklama: Çocuk tanımadığı bir sokak hayvanına yaklaşıp onu beslemeyi taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0055` birebir aynı, `@degisim: sabun -> kutu` (tutuyorsan), ardından `@onarim: 6b287d9424daee8a174a01d63f64cad298a96d4e`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0056 (deneme 2 -> 3)

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
Bir sabah Hello Kitty annesiyle parkta piknik yapıyordu. İkisi evde birlikte yaptıkları kurabiyeleri yiyordu. Birden annesinin kolyesi boynundan düştü, çünkü kilidi açılmıştı. "Kolyemi bulamıyorum, kızım," dedi annesi üzgün bir sesle. "Üzülme, anne, ben ararım," dedi Hello Kitty. Hello Kitty önce bir an hareketsiz durdu ve etrafa dikkatle baktı. Sonra kurabiye sepetinde parlayan bir şey gördü. Kolye kurabiyelerin arasına düşmüştü. Hello Kitty kolyeyi aldı ve annesine verdi. "Teşekkür ederim, canım kızım," dedi annesi ve ona sarıldı. Hello Kitty bundan sonra kaybolan bir şeyi en yakındaki yerlerde aradı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra kaybolan bir şeyi en yakındaki yerlerde aradı"
   - Cümle 11: «Hello Kitty bundan sonra kaybolan bir şeyi en yakındaki yerlerde aradı.»
   - Açıklama: 'Bundan sonra' alışkanlık bildirir ama fiil tek seferlik '-dı' ile çekilmiş; 'arardı' olmalı.
   - Açıklama: 'Bundan sonra' ile genel alışkanlık anlatılırken '-dı' kullanılmış; 'arardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0056` birebir aynı, `@degisim: affetmek -> aramak` (tutuyorsan), ardından `@onarim: 32620dc10ea87b15661d2e0b2dea53ed7f070e2c`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0058
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'ağaç', fiil 'bulmak', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: doğum günü için evde parti şapkası yoktu | turtanın üstünde kırmızı bir kağıt bulup şapka yaptı
@tohum: hello_kitty-0058
@degisim: ağaç -> kağıt
Hello Kitty mutfakta babası için bir sürpriz hazırlıyordu. Bugün babasının doğum günüydü. Ona bir parti şapkası vermek istedi ama evde hiç şapka yoktu. Hello Kitty çekmeceleri tek tek aradı. Sonra dolaptan en sevdiği elmalı turtayı çıkardı. Turtanın üstünde büyük, kırmızı bir kağıt buldu. Kağıdı dikkatle katladı ve güzel bir şapka yaptı. Turtanın en büyük dilimini de babasına ayırdı. Biraz sonra babası mutfağa girdi. Babası eğilince Hello Kitty kağıt şapkayı onun başına taktı. Şapkalı babası çok komik görünüyordu. Babası kızına sıkıca sarıldı. Sonra Hello Kitty ile babası turtayı birlikte mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Turtanın üstünde büyük, kırmızı bir kağıt buldu"
   - Cümle 6: «Turtanın üstünde büyük, kırmızı bir kağıt buldu.»
   - Açıklama: Çözümü getiren kağıt turtanın üstünde tesadüfen ve sebepsizce beliriyor.
   - Açıklama: Kağıt turtanın üstünde sebepsizce beliriyor ve çözümü tesadüfle getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0058` birebir aynı, `@degisim: ağaç -> kağıt` (tutuyorsan), ardından `@onarim: 1aa9c86ee676865317bf391f450f9b6dde7c3a4d`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0059
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'gölge', fiil 'serinletmek', sıfat 'cesur'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: rüzgar perdeyi itti ve duvardaki gölgeler kayboldu | perdeyi kurdelesiyle pencerenin yanına bağladı
@tohum: hello_kitty-0059
@degisim: cesur -> komik
Açık pencereden hafif bir rüzgar esiyordu. Hello Kitty elleriyle duvarda komik gölgeler yapıyordu. Ama rüzgar perdeyi pencerenin önüne itti ve gölgeler kayboldu. Hello Kitty pencereyi kapatmak istemedi, çünkü rüzgar sıcak odayı serinletiyordu. Kırmızı kurdelesini başından çıkardı. Perdeyi kurdeleyle pencerenin yanına sıkıca bağladı. Güneş yine duvara vurdu. Hello Kitty ellerini kaldırdı ve gölgeler geri geldi. Önce kocaman bir kalp yaptı, sonra küçük bir çiçek yaptı. Bu oyunu yeni arkadaşlarına da öğretmek istedi. Hello Kitty gölgeleriyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Güneş yine duvara vurdu"
   - Cümle 7: «Güneş yine duvara vurdu.»
   - Açıklama: 'Güneş vurmak' deyimsel bir kullanım; küçük çocuk için mecazlı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu oyunu yeni arkadaşlarına da öğretmek istedi"
   - Cümle 10: «Bu oyunu yeni arkadaşlarına da öğretmek istedi.»
   - Açıklama: Tohumdaki arkadaş özelliği sorunun çözümünde işe yaramıyor, sona eklenmiş bir dilek olarak kalıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız sonradan eklenen bir istek olarak anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu oyunu yeni arkadaşlarına da öğretmek istedi"
   - Cümle 10: «Bu oyunu yeni arkadaşlarına da öğretmek istedi.»
   - Açıklama: Yeni arkadaşlara öğretme isteği hiçbir olaya bağlanmayan işlevsiz bir ayrıntı.
   - Açıklama: Yeni arkadaşlar hikayede yok; cümle olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0059` birebir aynı, `@degisim: cesur -> komik` (tutuyorsan), ardından `@onarim: 4c240c274e91c95afb58e676ee4a40b25aee7646`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0060 (deneme 2 -> 3)

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
@plan: annesi yavaşladı çünkü çantası çok ağırdı | ekmeği ve suyu kendi çantasına aldı
@tohum: hello_kitty-0060
Hello Kitty annesiyle ormandaki kamp yerine yürüyordu. Yol kısaydı ama annesi yavaşladı, çünkü çantası çok ağırdı. Çantada ekmek, su ve bir şişe yağ vardı. Hello Kitty'nin kendi çantası ise boştu. "Anne, arkadaş gibi paylaşalım, ekmeği ve suyu ben taşıyayım," dedi Hello Kitty. Annesi durdu ve çantasını açtı. Hello Kitty ekmeği ve su şişesini kendi çantasına koydu. Annesinin çantası artık daha hafifti. İkisi yan yana hızlı adımlarla yürüdü. Biraz sonra kamp yerine vardılar. Hello Kitty annesinin elini tuttu. "Teşekkür ederim, kızım, seninle yürümek çok güzeldi!" dedi annesi.
```

**Hakem bulguları (4):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "annesi yavaşladı çünkü çantası"
   - Cümle 2: «Yol kısaydı ama annesi yavaşladı, çünkü çantası çok ağırdı.»
   - Açıklama: Plan satırında 'çünkü' bağlacından önce virgül eksik.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "su ve bir şişe yağ vardı"
   - Cümle 3: «Çantada ekmek, su ve bir şişe yağ vardı.»
   - Açıklama: Yağ şişesi kurulup hiç kullanılmıyor, işlevsiz ayrıntı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaş gibi paylaşalım"
   - Cümle 5: «"Anne, arkadaş gibi paylaşalım, ekmeği ve suyu ben taşıyayım," dedi Hello Kitty.»
   - Açıklama: Anneye 'arkadaş gibi' demek kelimenin yerinde olmayan kullanımı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkadaş gibi paylaşalım"
   - Cümle 5: «"Anne, arkadaş gibi paylaşalım, ekmeği ve suyu ben taşıyayım," dedi Hello Kitty.»
   - Açıklama: 'Arkadaş gibi paylaşmak' benzetmeli ve soyut bir anlatım, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0060` birebir aynı, ardından `@onarim: 4d2e1a744c24578aebff99a1470d3c54a28dd4ed`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0061 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0061
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'makarna', fiil 'bölmek', sıfat 'tüylü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: tüylü küçük kedi yiyecek bulamamıştı ve açtı | kurabiyeyi küçük parçalara böldü ve verdi
@tohum: hello_kitty-0061
Ağacın altından ince bir ses geliyordu. Hello Kitty ile Mimi ağacın gölgesinde makarna yiyordu. Tüylü küçük bir kedi çimenlerde yiyecek bulamamıştı ve çok açtı. "Hello Kitty, bu kedi aç, ona makarna verelim mi?" diye sordu Mimi. "Makarnanın sosu acı, ona kurabiye verelim," dedi Hello Kitty. Hello Kitty çantasından bir kurabiye çıkardı. Kurabiyeyi küçük parçalara böldü ve çimenlere koydu. Küçük kedi yavaşça geldi ve parçaları tek tek yedi. Mimi sevinçle ellerini çırptı. "Kedi artık tok," dedi Mimi. Hello Kitty bundan sonra parka gelirken çantasına fazla kurabiye koydu.
```

**Hakem bulguları (7):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağacın altından ince bir ses geliyordu"
   - Cümle 1: «Ağacın altından ince bir ses geliyordu.»
   - Açıklama: İnce ses işe yarayacakmış gibi kuruluyor ama bir daha anılmıyor ve kediye bağlanmıyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Tüylü küçük bir kedi"
   - Cümle 3: «Tüylü küçük bir kedi çimenlerde yiyecek bulamamıştı ve çok açtı.»
   - Açıklama: Başlıktaki Yan alanında yalnız Mimi var; kedi kartın yanlar bölümünde yok ama olaya katılıyor.
   - Açıklama: Başlıktaki Yan alanında yalnız Mimi var; olaya katılan küçük kedi kartın 'yanlar' bölümünde yok.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Tüylü küçük bir kedi"
   - Cümle 3: «Tüylü küçük bir kedi çimenlerde yiyecek bulamamıştı ve çok açtı.»
   - Açıklama: Kartın kararlarına göre evcil ya da hayvan arkadaşlar kartta yok; kapalı dünyaya yeni bir hayvan karakter ekleniyor.
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları kartta yok; kapalı dünyaya yeni bir hayvan karakter ekleniyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty çantasından bir kurabiye çıkardı"
   - Cümle 6: «Hello Kitty çantasından bir kurabiye çıkardı.»
   - Açıklama: Özellikler alanı kurabiye yapmayı sevmesini söylüyor; hikayede kurabiye yapılmıyor, yalnız verilmek için çıkarılıyor.
   - Açıklama: Tohumdaki özellik kurabiye yapmayı sevmek; hikayede kurabiye yapılmıyor, yalnız hazır kurabiye veriliyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kurabiyeyi küçük parçalara böldü ve çimenlere koydu"
   - Cümle 7: «Kurabiyeyi küçük parçalara böldü ve çimenlere koydu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde sahipsiz bir hayvana yaklaşılıp insan yiyeceği veriliyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Küçük kedi yavaşça geldi"
   - Cümle 8: «Küçük kedi yavaşça geldi ve parçaları tek tek yedi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde sahipsiz bir hayvana yaklaşılıp yiyecek veriliyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çantasına fazla kurabiye koydu"
   - Cümle 11: «Hello Kitty bundan sonra parka gelirken çantasına fazla kurabiye koydu.»
   - Açıklama: 'Fazla' burada yanlış anlamda; 'fazladan kurabiye' olmalı.
   - Açıklama: 'Fazla' burada yanlış anlamda; 'daha çok' ya da 'fazladan' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0061` birebir aynı, ardından `@onarim: f1195a2d41d9c8e178e946746ff7afb9208b0b00`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0062 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0062
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'teneke', fiil 'uçuşmak', sıfat 'resimli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: rüzgar esti ve resimli kağıtlar havada uçuştu | kağıtları topladı ve üstüne ağır kutuyu koydu
@tohum: hello_kitty-0062
Parkta Hello Kitty, Mimi için bir sürpriz hazırlıyordu. Örtüye resimli kağıtlar dizmiş, yanına bir teneke kutu koymuştu. Ama birden rüzgar esti ve kağıtlar havada uçuştu. Mimi biraz uzakta çiçeklere bakıyordu. Hello Kitty kağıtların peşinden koştu ve hepsini topladı. Sonra kağıtları örtüye koydu ve teneke kutuyu üstlerine bıraktı. Kutu kurabiye doluydu ve ağırdı, kağıtlar artık uçmadı. "Mimi, gel, sana bir sürprizim var!" diye seslendi Hello Kitty. Mimi koşarak geldi ve resimlere baktı. "Bunlar çok güzel, teşekkür ederim!" dedi Mimi. Sonra ikisi kutuyu açtı ve kurabiyeleri paylaştı. Hello Kitty bundan sonra rüzgarda kağıtların üstüne ağır bir şey koydu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve kağıtlar havada uçuştu"
   - Cümle 3: «Ama birden rüzgar esti ve kağıtlar havada uçuştu.»
   - Açıklama: Rüzgarın kağıtları dağıtması ve hemen toplanması, yönergede M3 örneği verilen önemsiz 'dağıttı, topladı, bitti' olayıyla aynı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0062` birebir aynı, ardından `@onarim: 5e7c55c125531b3248bb26f8c22a18e2d19e01a1`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0064 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0064
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'elmas', fiil 'süslenmek', sıfat 'ucuz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: şeker kutusunun kapağı çok sıkıydı | annesinden kutuyu açmasını istedi
@tohum: hello_kitty-0064
@degisim: ucuz -> sıkı
Hello Kitty annesiyle ormandaki kamp yerinde piknik yapıyordu. Annesi elmalı bir turta ve küçük bir şeker kutusu getirmişti. Hello Kitty turtayı şekerlerle süslemek istedi ama kutunun kapağı çok sıkıydı. Hello Kitty kapağı çekti ve çevirdi ama açamadı. "Anne, bu kutuyu açar mısın?" diye sordu Hello Kitty. "Tabii, canım," dedi annesi ve kapağı açtı. Kutuda elmas gibi parlayan renkli şekerler vardı. Hello Kitty şekerleri turtanın üstüne tek tek dizdi. Turta şekerlerle süslendi. "Bu turta çok güzel oldu," dedi annesi. "Teşekkürler, anneciğim, en sevdiğim turta şimdi daha güzel!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "elmas gibi parlayan renkli"
   - Cümle 7: «Kutuda elmas gibi parlayan renkli şekerler vardı.»
   - Açıklama: 'Elmas gibi' benzetmesi 3 yaşındaki çocuğun bilmediği bir kelimeye dayanıyor.
   - Açıklama: 'elmas gibi' benzetmesi ve 'elmas' kelimesi 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0064` birebir aynı, `@degisim: ucuz -> sıkı` (tutuyorsan), ardından `@onarim: f6f63211932d3013785404ec3c47db644d950c4e`, sonra gövde.
