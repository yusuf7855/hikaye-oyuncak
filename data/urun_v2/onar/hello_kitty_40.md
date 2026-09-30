# Editör görevi (onarım): Hello Kitty, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0119 (deneme 3 -> 4)

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
Bir sabah Hello Kitty parkta yeni bir şey denemek istedi. İlk kez tebeşirle parkın yoluna resim çizecekti. Ama kadife kese sıkı bir düğümle bağlıydı. Hello Kitty ipi hızlı hızlı çekti. Düğüm daha da sıkıştı. Hello Kitty yeni arkadaşlarla seksek oynamak istediği için vazgeçmedi. Durdu ve düğüme dikkatle baktı. Sonra ipin ucunu buldu ve düğümü yavaşça açtı. Kese renkli tebeşirlerle doluydu. Hello Kitty yere büyük bir seksek çizdi. Çizgiler çok güzel oldu. Hello Kitty bundan sonra düğümleri acele etmeden açtı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kadife kese sıkı bir düğümle bağlıydı"
   - Cümle 3: «Ama kadife kese sıkı bir düğümle bağlıydı.»
   - Açıklama: Kesenin neden sıkı düğümlü olduğu hiç söylenmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlarla seksek oynamak istediği"
   - Cümle 6: «Hello Kitty yeni arkadaşlarla seksek oynamak istediği için vazgeçmedi.»
   - Açıklama: Yeni arkadaşlar kurulup hiç görünmüyor; resim çizme hedefi de sebepsizce seksek çizmeye dönüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlarla seksek oynamak istediği için"
   - Cümle 6: «Hello Kitty yeni arkadaşlarla seksek oynamak istediği için vazgeçmedi.»
   - Açıklama: Yeni arkadaşlar işe yarayacakmış gibi anılıyor ama hikayede hiç görünmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0119` birebir aynı, ardından `@onarim: 72c304bd61689d238cc13f61b6b97116ddfe198b`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0121 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: koşarken kurabiye paketi cebinden düştü | kurabiyelerin kokusunu tanıdı ve paketi buldu
@tohum: hello_kitty-0121
@degisim: esnek -> mor
Hello Kitty yeleğini giymiş, parkta çimenlerin üstünde koşuyordu. Cebinde evde yaptığı kurabiyelerden bir paket vardı. Ama koşarken paket cebinden düşmüştü. Hello Kitty paketin nereye düştüğünü çok merak etti. Çimenlerde geri yürüdü ve her yere baktı. Paketi göremedi, ama birden tatlı bir koku duydu. Hello Kitty kurabiye yapmayı çok severdi ve bu kokuyu hemen tanıdı. Koku mor menekşelerin yanından geliyordu. Hello Kitty eğildi ve çiçeklere dikkatle baktı. Paket orada, yaprakların altında duruyordu. Hiçbir kurabiye kırılmamıştı. Hello Kitty bundan sonra cebinde kurabiye varken yavaş yürüdü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "birden tatlı bir koku duydu"
   - Cümle 6: «Paketi göremedi, ama birden tatlı bir koku duydu.»
   - Açıklama: Paketteki kurabiyelerin çiçeklerin arasından koku vermesi çözümü akla yatkın bir bağ kurmadan, rastlantıyla getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0121` birebir aynı, `@degisim: esnek -> mor` (tutuyorsan), ardından `@onarim: 31d78721ee0c99513855efa9948c64eaf5bdaec0`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0122 (deneme 3 -> 4)

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
Hello Kitty ile Mimi ormandaki kamp yerinde top oynuyordu. Topu şirin bir sepetin içine atıyorlardı. Ama bir tek top vardı ve ikisi de hep atmak istiyordu. Mimi utangaçtı, bir şey demedi ve oyundan ayrıldı. Bir ağacın altına oturdu ve topa baktı. Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı. Mimi'nin yanına gitti ve topu ona verdi. "İlk sıra sende, Mimi, sonra ben atarım," dedi Hello Kitty. Mimi topu attı ve top sepete girdi. "Sıra sende, Hello Kitty!" dedi Mimi sevinçle. Hello Kitty de attı ve top sepete düştü. İki kardeş sırayla atış yapıp oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkadaşlarına da kardeşine de hep iyi davranırdı"
   - Cümle 6: «Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı.»
   - Açıklama: Genel ve soyut bir karakter yargısı, olaydan çıkan somut bir ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0122` birebir aynı, `@degisim: pankek -> top` (tutuyorsan), ardından `@onarim: 52acea9353a6d1191d9d5e874c7a2653f6f12a37`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0124 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: annesi sürprizini ağacın arkasına sakladı | turtanın kokusunu tanıdı ve sepeti buldu
@tohum: hello_kitty-0124
@degisim: kanepe -> örtü
Parkta çimenler ıslak ve çamurluydu. Hello Kitty annesiyle ağacın altında, bir örtünün üstünde oturuyordu. "Sana bir sürpriz getirdim, ama onu sakladım," dedi annesi. Hello Kitty sürprizi çok merak etti. Birden tatlı bir koku duydu. Hello Kitty en çok elmalı turtayı severdi ve bu kokuyu hemen tanıdı. Çamurda annesinin ayak izleri de vardı. İzler yakındaki başka bir ağaca gidiyordu. Hello Kitty de o ağaca yavaşça yürüdü. Ağacın arkasında küçük bir sepet duruyordu. Sepetin içinde bir elmalı turta vardı! "Buldum, anne!" dedi Hello Kitty. Annesi güldü ve turtayı örtüye getirdi. "Anneciğim, bu oyun beni çok eğlendirdi!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "turtanın kokusunu tanıdı ve sepeti buldu"
   - Cümle 0 (plan satırı): «annesi sürprizini ağacın arkasına sakladı | turtanın kokusunu tanıdı ve sepeti buldu»
   - Açıklama: Gövdede sepeti koku değil çamurdaki ayak izleri buldurur; plan çözümü yanlış söylüyor.
   - Açıklama: Gövdede sepeti koku değil çamurdaki ayak izleri gösteriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden tatlı bir koku duydu"
   - Cümle 5: «Birden tatlı bir koku duydu.»
   - Açıklama: Koku çözüm gibi kuruluyor ama kullanılmıyor; sepete ayak izleri sebepsizce götürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0124` birebir aynı, `@degisim: kanepe -> örtü` (tutuyorsan), ardından `@onarim: 53ab91aa14706257e324c149babd64e90c7d1b35`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0125 (deneme 3 -> 4)

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
Bir sabah Hello Kitty evin yakınındaki parkta kırmızı topacıyla oynuyordu. Onu çimenlerin üstünde hızla çevirdi. Ama topaç yumuşak çimenlerde hemen durdu ve devrildi. Hello Kitty bir daha denedi. Topaç bu kez tuhaf bir şekilde sallandı ve yine yere düştü. Topacın dönmesi için düz ve sert bir yer gerekiyordu. Hello Kitty çantasına baktı. İçinde evde yaptığı kurabiyelerin kutusu vardı. Kutunun kapağı düz ve sertti. Hello Kitty kapağı çimenin üstüne koydu. Topacı onun ortasında çevirdi. Kırmızı topaç bu kez uzun uzun döndü. Hello Kitty sevinçle ellerini çırptı. Sonra orada mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve yine yere düştü"
   - Cümle 5: «Topaç bu kez tuhaf bir şekilde sallandı ve yine yere düştü.»
   - Açıklama: Topaç zaten yerde dönüyor; 'yere düştü' yerine 'devrildi' uygun olur.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İçinde evde yaptığı kurabiyelerin"
   - Cümle 8: «İçinde evde yaptığı kurabiyelerin kutusu vardı.»
   - Açıklama: Kartın güvenli özellik kullanımı satırı kurabiyenin bir büyükle yapılmasını ister; burada Hello Kitty'nin tek başına yaptığı ima ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0125` birebir aynı, ardından `@onarim: ddd51a276cf1b22c981417cd9e03bd93bf63e449`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0127 (deneme 3 -> 4)

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
Hello Kitty mutfakta en sevdiği elmalı turtayı arıyordu. Sonunda kutunun küçük bir ucunu en üst rafta buldu. Ama raf çok yüksekti ve kutunun önünde büyük bir pirinç torbası vardı. Hello Kitty uzandı, ama rafa yetişemedi. Babası o sırada salonda oturuyordu. "Babacığım, bana yardım eder misin?" diye sordu Hello Kitty. Babası hemen mutfağa geldi. "Tabii, bu benim için çok kolay," dedi babası. Önce ağır pirinç torbasını kenara çekti. Sonra kutuyu indirdi ve masaya koydu. Babası iki tabak da getirdi. Hello Kitty sevinçle ellerini çırptı. "Teşekkürler, babacığım, şimdi birlikte yiyelim!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kutunun küçük bir ucunu"
   - Cümle 2: «Sonunda kutunun küçük bir ucunu en üst rafta buldu.»
   - Açıklama: Kutunun 'ucu' olmaz ve daha önce anılmamış kutu belirli gibi kullanılıyor; 'köşesini' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonunda kutunun küçük bir ucunu en üst rafta buldu"
   - Cümle 2: «Sonunda kutunun küçük bir ucunu en üst rafta buldu.»
   - Açıklama: Turtayı ararken hiç tanıtılmamış bir kutu sebepsizce beliriyor ve turtanın bu kutuda olduğu söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0127` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 48cc7dea2fdf19efad66aadb61299f6fd6996352`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0128 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0128
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kurdele', fiil 'şişirmek', sıfat 'mutlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: küçük bir kedi çok acıkmıştı çünkü yerde yiyecek yoktu | sepetten turta çıkarıp küçük parçalarını çimenlere attı
@tohum: hello_kitty-0128
Bir sabah Hello Kitty ile Mimi parkta piknik yapıyordu. Birden ağacın altında küçük bir kedi gördüler. Kedi tüylerini şişirmişti ve yerde yiyecek arıyordu, ama hiç bulamıyordu. "Bu kedi çok aç galiba," dedi Mimi yavaşça. Hello Kitty sepete baktı. Sepetin kapağı kırmızı bir kurdeleyle bağlıydı. Hello Kitty kurdeleyi çözdü ve en sevdiği elmalı turtayı çıkardı. Turtanın kenarından küçük parçalar kopardı. Oturduğu yerden parçaları çimenlerin üstüne attı. Kedi yavaşça geldi ve parçaları yedi. "Bak, Mimi, artık karnı tok!" dedi Hello Kitty. Kedi neşeyle miyavladı. Sonra Hello Kitty ile Mimi pikniğe mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "küçük bir kedi gördüler"
   - Cümle 2: «Birden ağacın altında küçük bir kedi gördüler.»
   - Açıklama: Başlıktaki Yan alanında yalnız Mimi var ve kartın yanlar bölümünde böyle bir kedi karakteri yok.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "ağacın altında küçük bir kedi"
   - Cümle 2: «Birden ağacın altında küçük bir kedi gördüler.»
   - Açıklama: Başlığın Yan alanında yalnız Mimi var; küçük kedi kartın yanlar bölümünde yok.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "küçük bir kedi gördüler"
   - Cümle 2: «Birden ağacın altında küçük bir kedi gördüler.»
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları kartta yok, kartta olmayan bir hayvan karakteri olaya katılıyor.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ağacın altında küçük bir kedi"
   - Cümle 2: «Birden ağacın altında küçük bir kedi gördüler.»
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları kartta yok, kapalı dünyaya yeni bir hayvan karakter giriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepetin kapağı kırmızı bir kurdeleyle bağlıydı"
   - Cümle 6: «Sepetin kapağı kırmızı bir kurdeleyle bağlıydı.»
   - Açıklama: Kurdele ayrıntısı olayda hiçbir işlev görmeyen gereksiz bir ayrıntı.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "parçaları çimenlerin üstüne attı"
   - Cümle 9: «Oturduğu yerden parçaları çimenlerin üstüne attı.»
   - Açıklama: Tanımadığı sokak kedisine yiyecek verip yaklaştırmak çocuğun taklit edebileceği riskli bir davranış.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Oturduğu yerden parçaları çimenlerin üstüne attı"
   - Cümle 9: «Oturduğu yerden parçaları çimenlerin üstüne attı.»
   - Açıklama: Tanınmayan bir sokak hayvanını turtayla beslemek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0128` birebir aynı, ardından `@onarim: 4ab09147b0c923e91037ec5a107646069031616a`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0132 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0132
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'armut', fiil 'fırçalamak', sıfat 'yaratıcı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası oyunu unutup gülen çizgi olan muzu yedi | turtadan eğri bir parça koparıp yeni çizgi yaptı
@tohum: hello_kitty-0132
@degisim: fırçalamak -> koymak
Rüzgar parkta hafif esiyordu. Hello Kitty ile babası tabağa meyvelerden gülen komik bir yüz yapıyordu. Ama babası oyunu unuttu ve gülen çizgi olan muzu yedi. Yüzün iki üzüm gözü ve bir armut burnu vardı, ama artık gülmüyordu. "Babacığım, gülen çizgiyi yedin!" dedi Hello Kitty gülerek. "Ah, unuttum!" dedi babası ve o da güldü. Sepette başka muz kalmamıştı, yalnız bir dilim elmalı turta vardı. Hello Kitty en sevdiği turtadan ince ve eğri bir parça kopardı. Parçayı gözlerin altına, gülen bir çizgi gibi koydu. "Aferin, kızım, çok yaratıcısın!" dedi babası. "Bak, babacığım, komik yüz yine gülüyor!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kızım, çok yaratıcısın!"
   - Cümle 10: «"Aferin, kızım, çok yaratıcısın!" dedi babası.»
   - Açıklama: 'Yaratıcı' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok yaratıcısın!"
   - Cümle 10: «"Aferin, kızım, çok yaratıcısın!" dedi babası.»
   - Açıklama: 'Yaratıcı' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0132` birebir aynı, `@degisim: fırçalamak -> koymak` (tutuyorsan), ardından `@onarim: f3c52e821ff0608416a561ea052807c595c1d4a2`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0133 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0133
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'nilüfer', fiil 'gerinmek', sıfat 'kapalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: sürpriz kalp için toplanacak çiçekler daha kapalıydı | çiçekler yerine kurabiyeleri dizip bir kalp yaptı
@tohum: hello_kitty-0133
@degisim: nilüfer -> çiçek
Hello Kitty kamp yerinde uyandı, ama Mimi daha çadırda uyuyordu. Kardeşine çiçeklerden bir kalp yapıp sürpriz hazırlamak istedi. Ama sabah serindi ve çiçeklerin hepsi daha kapalıydı. Kalp için başka bir şey gerekiyordu. Kurabiye yapmayı çok severdi ve çantasında evde birlikte yaptıkları kurabiyeler vardı. Kurabiyeleri çadırın önüne, temiz bir örtünün üstüne tek tek dizdi. Böylece kocaman bir kalp yaptı. Az sonra Mimi çadırdan çıktı ve gerindi. "Bu kalp ne?" diye sordu Mimi. "Günaydın sürprizi, Mimi, hepsi senin için!" dedi Hello Kitty. Mimi utana utana gülümsedi ve bir kurabiye aldı. "Teşekkürler, Hello Kitty, bu en güzel sürpriz!" dedi Mimi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kurabiye yapmayı çok severdi"
   - Cümle 5: «Kurabiye yapmayı çok severdi ve çantasında evde birlikte yaptıkları kurabiyeler vardı.»
   - Açıklama: Önceki cümlenin öznesi 'bir şey' olduğundan kurabiye yapmayı kimin sevdiği belli değil.
   - Açıklama: Öznesiz cümlede kurabiye yapmayı kimin sevdiği ve 'birlikte' kiminle yapıldığı belli değil; önceki cümlenin öznesi 'başka bir şey'.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kurabiyeleri çadırın önüne, temiz bir örtünün üstüne tek tek dizdi"
   - Cümle 6: «Kurabiyeleri çadırın önüne, temiz bir örtünün üstüne tek tek dizdi.»
   - Açıklama: Sorunun sebebi çiçeklerin kapalı olması ama çözüm bu sebebe yönelmiyor, çiçekler yerine başka bir malzeme konuyor.
   - Açıklama: Çözüm çiçeklerin kapalı olması sebebine yönelmiyor, sorunu başka bir malzemeye geçerek atlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0133` birebir aynı, `@degisim: nilüfer -> çiçek` (tutuyorsan), ardından `@onarim: 1729515041f88aae2032b46f2e24da9a9e630553`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0134 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0134
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'posta', fiil 'kırpmak', sıfat 'şık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: yağmur başladı ve kurabiye sepetinin üstü açıktı | sepetin üstünü örtüyle kapatıp ağacın altına koştu
@tohum: hello_kitty-0134
@degisim: posta -> örtü
Yağmur damla damla yağmaya başladı. Hello Kitty parkta çimenlerin üstünde piknik yapıyordu. Sepetinde evde birlikte yaptıkları kurabiyeler vardı ve sepetin üstü açıktı. Bir damla burnuna düştü ve Hello Kitty gözlerini kırptı. Hemen şık kırmızı örtüsünü kaldırdı ve sepetin üstünü sıkıca kapattı. Sonra sepeti alıp büyük ağacın altına koştu. Ağacın yaprakları çok sıktı ve altı kuruydu. Hello Kitty örtüyü açtı ve sepete baktı. Kurabiyelerin hepsi kuru ve çıtır çıtırdı. Hello Kitty ağacın altında bir kurabiye yedi ve yağmuru izledi. Hello Kitty çok mutluydu, çünkü kurabiyelerini yağmurdan korumuştu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "evde birlikte yaptıkları kurabiyeler"
   - Cümle 3: «Sepetinde evde birlikte yaptıkları kurabiyeler vardı ve sepetin üstü açıktı.»
   - Açıklama: Hikayede tek kişi var; 'birlikte yaptıkları' kimleri gösterdiği belli değil.
   - Açıklama: 'Birlikte yaptıkları' kimi gösteriyor belli değil; hikayede Hello Kitty'den başka kimse yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0134` birebir aynı, `@degisim: posta -> örtü` (tutuyorsan), ardından `@onarim: 1ba535ef1808cf68c5e2c86db46cc360770c3209`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0135 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0135
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'bambu', fiil 'atlamak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: rüzgar çok gürültülü olduğu için geri gelen sesi duyamadı | rüzgarın durmasını bekledi ve yeniden seslendi
@tohum: hello_kitty-0135
@degisim: bambu -> rüzgar
Rüzgar ormanda hızlı hızlı esiyordu. Hello Kitty ile annesi kamp yerinde oturuyordu. Hello Kitty ağaçlara seslendi ama geri gelen sesi duyamadı. Hello Kitty dallara baktı ve rüzgarı dinledi. Rüzgarın sesi, Hello Kitty'nin sesinden daha yüksekti. "Anne, rüzgar durunca yine seslenirim," dedi Hello Kitty. Hello Kitty sabırsızdı ve yerinde iki kez atladı. Sonra yerine oturdu ve rüzgarın durmasını bekledi. Biraz sonra rüzgar durdu ve orman sessiz oldu. "Benimle arkadaş olur musun?" diye seslendi Hello Kitty. Uzaktan "Olur musun?" diye bir ses geri geldi. Annesi güldü ve kızına sarıldı. Hello Kitty çok sevindi, çünkü sesinin geri geldiğini sonunda duymuştu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hello Kitty ağaçlara seslendi ama geri gelen sesi duyamadı"
   - Cümle 3: «Hello Kitty ağaçlara seslendi ama geri gelen sesi duyamadı.»
   - Açıklama: Neden seslendiği ve yankı beklediği söylenmiyor; sorunun sebebi ve önemi belirsiz kalıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty dallara baktı"
   - Cümle 4: «Hello Kitty dallara baktı ve rüzgarı dinledi.»
   - Açıklama: Hello Kitty adı art arda beş cümlenin başında gereksizce tekrarlanıyor.
   - Açıklama: Özne adı art arda cümlelerde gereksiz yere tekrarlanıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty sabırsızdı ve yerinde"
   - Cümle 7: «Hello Kitty sabırsızdı ve yerinde iki kez atladı.»
   - Açıklama: Tohumdaki özellik arkadaş edinmek iken karttaki özellik listesinde olmayan sabırsızlık huyu ikinci bir özellik olarak ekleniyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty sabırsızdı ve"
   - Cümle 7: «Hello Kitty sabırsızdı ve yerinde iki kez atladı.»
   - Açıklama: Kartın özellikler alanında olmayan sabırsızlık ikinci bir özellik olarak ekleniyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Benimle arkadaş olur musun?" diye seslendi Hello Kitty"
   - Cümle 10: «"Benimle arkadaş olur musun?" diye seslendi Hello Kitty.»
   - Açıklama: Kartın özellikler alanındaki arkadaş edinme özelliği yalnız yankıya sorulan bir cümlede geçiyor ve sorunun çözümüne hiç katkı vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0135` birebir aynı, `@degisim: bambu -> rüzgar` (tutuyorsan), ardından `@onarim: 45b15f703d26c7ff839972476b7c7046c777b507`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0137 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0137
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çamaşır', fiil 'şakalaşmak', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: koşarken kardeşinin çamaşırlarını yere düşürdü | özür diledi ve çamaşırları kardeşiyle yeniden katladı
@tohum: hello_kitty-0137
@degisim: şakalaşmak -> oynamak
Dışarıda yağmur yağıyordu. Hello Kitty ile ikizi Mimi evde oyun oynuyordu. Hello Kitty koşarken Mimi'nin katladığı çamaşırlara çarptı ve hepsi yere düştü. Mimi yerdeki çamaşırlara baktı ve çok üzüldü. Hello Kitty hemen durdu ve kardeşinin yanına gitti. Mimi en iyi arkadaşıydı, bu yüzden Hello Kitty ondan özür diledi. Sonra Mimi'ye sıkıca sarıldı. Hello Kitty yumuşak havluları yerden tek tek topladı. Mimi de ona yardım etti. İkisi birlikte bütün çamaşırları yeniden katladı ve sepete koydu. Mimi gülümsedi ve Hello Kitty'nin elini tuttu. Hello Kitty bundan sonra evde koşarken etrafına dikkat etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu yüzden Hello Kitty ondan özür diledi"
   - Cümle 6: «Mimi en iyi arkadaşıydı, bu yüzden Hello Kitty ondan özür diledi.»
   - Açıklama: 'Bu yüzden' yanlış bağlaç; özür dilemenin nedeni Mimi'nin arkadaş olması değil, çamaşırları düşürmesi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mimi en iyi arkadaşıydı, bu yüzden Hello Kitty ondan özür diledi"
   - Cümle 6: «Mimi en iyi arkadaşıydı, bu yüzden Hello Kitty ondan özür diledi.»
   - Açıklama: Özrün sebebi çamaşırları düşürmesi değil Mimi'nin en iyi arkadaşı olması gibi gösteriliyor; olay bir öncekinden mantıkla çıkmıyor.
   - Açıklama: Özrün sebebi çamaşırları düşürmesi olmalıyken sebepsizce Mimi'nin en iyi arkadaşı olmasına bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0137` birebir aynı, `@degisim: şakalaşmak -> oynamak` (tutuyorsan), ardından `@onarim: 593c26e790d7b34826b101eec507707f159147d0`, sonra gövde.
