# Editör görevi (onarım): Hello Kitty, onarım partisi 43

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar43.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar43.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0175 (deneme 1 -> 2)

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
Hello Kitty ormandaki kamp yerinde çadırın önünde oturuyordu. Arkadaşlarına vermek için bir orman resmi yapıyordu. Birden rüzgar esti ve ağaçların üstüne simsiyah bulutlar geldi. Yağmur yağarsa resim ıslanırdı. Rüzgarda ağaçların yaprakları dönüyordu. Hello Kitty kağıtlarını ve boyalarını hemen topladı. Hepsini çadırın içine taşıdı. Sonra kendisi de çadıra girdi ve kapısını kapattı. Biraz sonra yağmur damlaları çadırın üstüne düşmeye başladı. Hello Kitty resmine baktı. Resim yine kuruydu. Hello Kitty yağmurun sesini dinledi ve resmini çadırda mutlu mutlu bitirdi.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 1: «Hello Kitty ormandaki kamp yerinde çadırın önünde oturuyordu.»
   - Açıklama: Güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmediğini söylüyor, Hello Kitty ormanda yetişkinsiz yalnız kamp ediyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde çadırın önünde oturuyordu"
   - Cümle 1: «Hello Kitty ormandaki kamp yerinde çadırın önünde oturuyordu.»
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor, ama Hello Kitty ormanda büyüksüz tek başına.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Arkadaşlarına vermek için bir orman resmi"
   - Cümle 2: «Arkadaşlarına vermek için bir orman resmi yapıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
4. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "ağaçların üstüne simsiyah bulutlar geldi"
   - Cümle 3: «Birden rüzgar esti ve ağaçların üstüne simsiyah bulutlar geldi.»
   - Açıklama: Ormanda yalnız bir çocuğun üstüne gelen simsiyah bulutlar ve rüzgar küçük çocuk için ürkütücü olabilir.
   - Açıklama: Ormanda tek başına bir çocuğun üstüne gelen simsiyah bulutlar ve fırtına küçük çocuk için korkutucu olabilir.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ağaçların yaprakları dönüyordu"
   - Cümle 5: «Rüzgarda ağaçların yaprakları dönüyordu.»
   - Açıklama: Yapraklar dönmez; 'sallanıyordu' ya da 'hışırdıyordu' olmalı.
   - Açıklama: Dallardaki yapraklar rüzgarda dönmez, sallanır; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0175` birebir aynı, `@degisim: tartı -> çadır` (tutuyorsan), ardından `@onarim: 484c45b59532fef2d35c39d33c2210471becefd8`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0176 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0176
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'mücevher', fiil 'küçülmek', sıfat 'aydınlık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: turta sepeti yüksek bir dalda asılıydı ve uzanamadı | annesinden sepeti almasını istedi
@tohum: hello_kitty-0176
@degisim: mücevher -> sepet
Ormandaki aydınlık kamp yerinde Hello Kitty annesiyle oturuyordu. Annesi turta sepetini karıncalar gelmesin diye yüksek bir dala asmıştı. Hello Kitty elmalı turtayı çok istiyordu ama sepete uzanamıyordu. Parmaklarının ucunda durdu ama sepet yine çok yüksekteydi. Hello Kitty annesinin yanına gitti. "Anne, sepeti alır mısın, lütfen?" diye sordu Hello Kitty. "Tabii, tatlım, iyi ki bana sordun," dedi annesi. Annesi uzandı ve sepeti daldan indirdi. Sepetten elmalı turtayı çıkardı ve bir dilim kesti. Hello Kitty dilimi aldı ve mutlu mutlu yemeye başladı. Dilim yavaş yavaş küçüldü. Hello Kitty bundan sonra yüksekte kalan şeyler için annesinden yardım istedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yüksek bir dalda asılıydı ve uzanamadı"
   - Cümle 0 (plan satırı): «turta sepeti yüksek bir dalda asılıydı ve uzanamadı | annesinden sepeti almasını istedi»
   - Açıklama: Plan satırında iki yüklemin öznesi aynı görünüyor; 'uzanamadı' dilbilgisel olarak 'turta sepeti'ne bağlanıyor.
   - Açıklama: İkinci fiilin öznesi değişiyor ama belirtilmiyor; cümleye göre sepet uzanamıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0176` birebir aynı, `@degisim: mücevher -> sepet` (tutuyorsan), ardından `@onarim: ef0e54c098e756a53ba2b6bd9768e1027b8bb33e`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0177 (deneme 1 -> 2)

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
Parkta güçlü bir rüzgar esiyordu. Hello Kitty ağacın gölgesinde piknik tabaklarını düzenledi. Ama rüzgar Mimi'nin hafif plastik çatalını uçurdu ve çatal kayboldu. Mimi çimenlere baktı ama çatalını göremedi. Mimi çok utangaçtı ve üzgün üzgün sustu. Hello Kitty en iyi arkadaşının yanına oturdu ve elini tuttu. "Üzülme, Mimi, çatalını birlikte bulalım," dedi Hello Kitty. Mimi biraz rahatladı ve çiçekleri gösterdi. "Çatal o tarafa düştü," dedi Mimi. Hello Kitty çiçeklerin arasına eğildi. Küçük çatal bir yaprağın altındaydı. Hello Kitty çatalı alıp kardeşine verdi. Mimi çatalını sıkı sıkı tuttu ve güldü. İki kardeş yeniden oturdu ve mutlu mutlu piknik yaptı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşının yanına oturdu"
   - Cümle 6: «Hello Kitty en iyi arkadaşının yanına oturdu ve elini tuttu.»
   - Açıklama: Kardeş olarak verilen Mimi burada 'en iyi arkadaşı' diye anılıyor; çocuk bunun yeni biri olduğunu sanabilir, gösterilen kişi belirsizleşiyor.
   - Açıklama: Kardeşi olan Mimi birden 'en iyi arkadaşı' diye anılıyor, kimin kastedildiği karışıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hello Kitty en iyi arkadaşının yanına oturdu"
   - Cümle 6: «Hello Kitty en iyi arkadaşının yanına oturdu ve elini tuttu.»
   - Açıklama: Mimi önce en iyi arkadaş, sonra kardeş olarak anılıyor.
   - Açıklama: Mimi önce en iyi arkadaş, sonra kardeş olarak anılıyor; ilişki çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0177` birebir aynı, ardından `@onarim: 5963c40094f722c92b95d65d1461a1d09c9333c0`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0178 (deneme 1 -> 2)

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
Hello Kitty babasıyla parkta piknik yapıyordu. Babası sepeti askısından tuttu ve ağacın gölgesine koydu. Sepetten benekli bir armut çıkardı ama Hello Kitty tatmak istemedi. Daha önce hiç armut yememişti ve benekler ona garip geldi. "Biraz dene, çok tatlıdır," dedi babası. Hello Kitty sepete baktı ve elmalı turtayı gördü. "Baba, armudu turtamın üstüne koyar mısın?" diye sordu Hello Kitty. Babası armudu küçük parçalara kesti ve turtanın üstüne dizdi. Hello Kitty turtayı ısırdı. Tatlı armut ile elma birlikte çok güzeldi. "Armut da çok lezzetliymiş!" dedi Hello Kitty. Hello Kitty çok sevindi, çünkü yeni bir meyveyi denemişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sepeti askısından tuttu"
   - Cümle 2: «Babası sepeti askısından tuttu ve ağacın gölgesine koydu.»
   - Açıklama: Sepetin tutulan yeri askı değil sap; kelime yanlış anlamda.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Babası sepeti askısından tuttu"
   - Cümle 2: «Babası sepeti askısından tuttu ve ağacın gölgesine koydu.»
   - Açıklama: Piknik sepetinin tutulan yeri 'askı' değil 'sap'tır; kelime yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0178` birebir aynı, `@degisim: uyutmak -> tatmak` (tutuyorsan), ardından `@onarim: cca148c44e092bc3716cc7f3a17de3b237db0d24`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0179 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0179
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: kaybolan eşya
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'yağmurluk', fiil 'havalanmak', sıfat 'yorgun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: kardeşi yağmurluğunu çıkarıp bir yerde bırakmıştı | yorgun kardeşinin yanında kalıp yağmurluğu çiçeklerde gördü
@tohum: hello_kitty-0179
Parkta yağmur yeni dinmişti ve çimenler ıslaktı. Hello Kitty ile Mimi çiçeklerin arasında koşup oynamıştı. Mimi koşarken sarı yağmurluğunu çıkarmıştı ve şimdi onu bulamıyordu. Mimi çok yorgundu ve üzgündü. "Otur, Mimi, ben seninle kalırım," dedi Hello Kitty. En iyi arkadaşını yalnız bırakmadı. İki kardeş büyük ağacın gölgesine oturdu. Hello Kitty etrafa baktı. Tam o sırada rüzgar esti ve çiçeklerde sarı bir kol havalandı. "Bak, yağmurluğun orada!" diye seslendi Hello Kitty. Hemen çiçeklere koştu ve yağmurluğu aldı. Mimi yağmurluğunu giydi ve kardeşine sarıldı. Hello Kitty çok mutlu oldu, çünkü kardeşine yardım etmişti.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "En iyi arkadaşını yalnız"
   - Cümle 6: «En iyi arkadaşını yalnız bırakmadı.»
   - Açıklama: Mimi kardeştir; 'en iyi arkadaşını' yanlış kelime ve sonraki 'İki kardeş' ile çelişiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "En iyi arkadaşını yalnız bırakmadı"
   - Cümle 6: «En iyi arkadaşını yalnız bırakmadı.»
   - Açıklama: Kardeşi olan Mimi'ye 'en iyi arkadaşı' deniyor; kimin kastedildiği karışıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "En iyi arkadaşını yalnız bırakmadı"
   - Cümle 6: «En iyi arkadaşını yalnız bırakmadı.»
   - Açıklama: Mimi önce en iyi arkadaş, hemen sonra kardeş olarak anılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çiçeklerde sarı bir kol havalandı"
   - Cümle 9: «Tam o sırada rüzgar esti ve çiçeklerde sarı bir kol havalandı.»
   - Açıklama: 'Kol' tamlamasız kalınca çocuk için yağmurluğun kolu değil insan kolu gibi anlaşılıyor; 'yağmurluğun kolu' olmalı.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "rüzgar esti ve çiçeklerde sarı bir kol havalandı"
   - Cümle 9: «Tam o sırada rüzgar esti ve çiçeklerde sarı bir kol havalandı.»
   - Açıklama: Çözüm kaybolmanın sebebine yönelmiyor; yağmurluk rüzgarın şansıyla ortaya çıkıyor.
   - Açıklama: Hello Kitty yağmurluğu aramıyor, çözüm sebebe yönelmeden şansla geliyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada rüzgar esti"
   - Cümle 9: «Tam o sırada rüzgar esti ve çiçeklerde sarı bir kol havalandı.»
   - Açıklama: Çözümü figürün eylemi değil sebepsiz bir rüzgar getiriyor.
   - Açıklama: Yağmurluğu tesadüfen esen rüzgar gösteriyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0179` birebir aynı, ardından `@onarim: 3e2ff64de6d411041458669e8bf16f8c6bceb7da`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0180 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0180
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'valiz', fiil 'alışmak', sıfat 'komik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: ağaçların arasından garip bir gülme sesi geldi | sese merhaba dedi ve kendi sesini duydu
@tohum: hello_kitty-0180
Hello Kitty ile babası kamp yerinde valizi açıyordu. Babası komik bir yüz yaptı ve yüksek sesle güldü. Birden ağaçların arasından da bir gülme sesi geldi. Hello Kitty bu sesi çok merak etti. "Baba, orada yeni bir arkadaş mı var?" diye sordu Hello Kitty. Sonra ağaçlara doğru iki adım yürüdü. "Merhaba, benimle arkadaş olur musun?" dedi yüksek sesle. Ağaçların arasından hemen "Olur musun?" diye bir cevap duyuldu. Hello Kitty kendi sesini tanıdı ve güldü. "Bu bir yankı, sesin ağaçlardan geri geliyor," dedi babası. Hello Kitty de bu sese hemen alıştı. "Baba, bu oyun çok eğlenceli!" dedi Hello Kitty.
```

**Hakem bulguları (5):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "garip bir gülme sesi geldi"
   - Cümle 0 (plan satırı): «ağaçların arasından garip bir gülme sesi geldi | sese merhaba dedi ve kendi sesini duydu»
   - Açıklama: Ormanda ağaçların arasından gelen garip gülme sesi küçük bir çocuk için ürkütücü olabilir.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden ağaçların arasından da bir gülme sesi geldi"
   - Cümle 3: «Birden ağaçların arasından da bir gülme sesi geldi.»
   - Açıklama: Gülme sesi gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir sorun kurulmuyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty de bu sese hemen alıştı"
   - Cümle 11: «Hello Kitty de bu sese hemen alıştı.»
   - Açıklama: 'de' başka birinin de alıştığını ima ediyor ama böyle biri yok; bağlaç yanlış anlamda.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty de bu sese"
   - Cümle 11: «Hello Kitty de bu sese hemen alıştı.»
   - Açıklama: 'de' bağlacının gösterdiği başka biri yok; kimin de alıştığı belli değil.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bu oyun çok eğlenceli"
   - Cümle 12: «"Baba, bu oyun çok eğlenceli!" dedi Hello Kitty.»
   - Açıklama: Hikayede bir oyun tanıtılmadığı için 'bu oyun' ifadesinin neyi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0180` birebir aynı, ardından `@onarim: 5f7a321ee92cb01f75c3ac2cc833bb08fc7ca53d`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0181 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0181
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'mürekkep', fiil 'oynamak', sıfat 'yırtık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: resim yapacağı tek kağıt ortadan yırtıktı | yırtık kağıdı ikiye bölüp annesine iki resim yaptı
@tohum: hello_kitty-0181
Parkta kuşlar neşeyle ötüyordu. Hello Kitty ağacın gölgesinde annesine güzel bir resim yapmak istedi. Ama sepetteki tek kağıt bir dala takılıp ortadan yırtılmıştı. Annesi ona mürekkepli bir kalem verdi. "Bu kalemle ilk kez resim yapacaksın," dedi annesi. Hello Kitty kalemle biraz oynadı ve yırtık kağıda baktı. Sonra kağıdı yırtık yerinden iki parçaya ayırdı. Bir parçaya mavi bir çiçek çizdi. Öbür parçaya gülen bir güneş çizdi. Hello Kitty iki resmi de annesine verdi. "Anneciğim, sen benim arkadaşımsın, ikisi de senin," dedi Hello Kitty. Annesi resimlere baktı ve Hello Kitty'ye sarıldı. "Teşekkürler, tatlım, bunlar çok güzel!" dedi annesi.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ona mürekkepli bir kalem"
   - Cümle 4: «Annesi ona mürekkepli bir kalem verdi.»
   - Açıklama: 'Mürekkepli' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi ona mürekkepli bir kalem verdi"
   - Cümle 4: «Annesi ona mürekkepli bir kalem verdi.»
   - Açıklama: İlk kez kullanılacak kalem önemliymiş gibi kuruluyor ama olayda hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kalemle ilk kez resim yapacaksın"
   - Cümle 5: «"Bu kalemle ilk kez resim yapacaksın," dedi annesi.»
   - Açıklama: Mürekkepli kalemle ilk kez resim yapma ayrıntısı işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen benim arkadaşımsın, ikisi de senin"
   - Cümle 11: «"Anneciğim, sen benim arkadaşımsın, ikisi de senin," dedi Hello Kitty.»
   - Açıklama: Tohumdaki 'yeni arkadaş edinme, herkese iyi davranma' özelliği sorunun çözümünde iş görmüyor, anneye 'arkadaşım' demekle yalnız etiket olarak geçiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen benim arkadaşımsın"
   - Cümle 11: «"Anneciğim, sen benim arkadaşımsın, ikisi de senin," dedi Hello Kitty.»
   - Açıklama: Karttaki yeni arkadaş edinme özelliği annesine söylenen bir sözle anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0181` birebir aynı, ardından `@onarim: 117941cddc7f0e4f19ed431f7789a1aa90f2cfe6`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0182 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0182
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'ipek', fiil 'içmek', sıfat 'renkli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası yiyecek sepetini evde unuttu ve tabaklar boştu | çantasındaki kurabiyeleri çıkarıp tabaklara koydu
@tohum: hello_kitty-0182
Hello Kitty kamp yerinde babasıyla parti oyunu oynuyordu. Yere ipek bir örtü serdi ve renkli bardakları koydu. Ama babası yiyecek sepetini evde unutmuştu ve tabaklar boştu. "Şimdi ne yiyeceğiz?" diye sordu babası. Sonra bardağını kaldırdı ve komik bir sesle su içti. Hello Kitty kahkahayla güldü. Birden kendi çantasını hatırladı. Çantada evde birlikte yaptıkları kurabiyeler vardı. Hello Kitty kurabiyeleri çıkardı ve tabaklara tek tek dizdi. Babası bir kurabiye yedi ve gözlerini kapattı. "Bunlar ormandaki en güzel kurabiyeler!" dedi babası. Hello Kitty de bir kurabiye aldı ve babasına gülümsedi. "Baba, partimiz şimdi çok güzel oldu!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "komik bir sesle su içti"
   - Cümle 5: «Sonra bardağını kaldırdı ve komik bir sesle su içti.»
   - Açıklama: Su içmek bir ses çıkarma eylemi değil; 'komik bir sesle' fiile uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bardağını kaldırdı ve komik bir sesle su içti"
   - Cümle 5: «Sonra bardağını kaldırdı ve komik bir sesle su içti.»
   - Açıklama: Yiyecek yokken bardaklarda nereden geldiği belli olmayan su beliriyor ve bu ayrıntı olayda işe yaramıyor.
   - Açıklama: Babanın komik sesle su içmesi sorunla ya da çözümle bağlantısız, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0182` birebir aynı, ardından `@onarim: f2186bf911384e7a4be8ed9fcb4ced4f9f45db72`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0183 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0183
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kek', fiil 'bozulmak', sıfat 'dürüst'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: tabak eğildi ve annesinin keki toprağa düştü | kendi kekini ikiye bölüp yarısını annesine verdi
@tohum: hello_kitty-0183
@degisim: dürüst -> düzgün
Ormandaki kamp yerinde Hello Kitty annesiyle kek partisi oyunu oynuyordu. Hello Kitty iki dilim keki iki tabağa koydu. Ama annesinin tabağı bir taşın üstünde eğildi ve keki toprağa düştü. Kekin şekli bozuldu ve üstü kirlendi. "Kızım, benim kekim nereye gitti?" diye sordu annesi gülerek. Hello Kitty kendi tabağına baktı. Tabakta tek bir düzgün dilim kalmıştı. Hello Kitty dilimi dikkatle ikiye böldü. Büyük yarısını annesinin tabağına koydu. "Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty. Annesi gülümsedi ve Hello Kitty'nin başını okşadı. Kirli keki de birlikte çöpe attılar. Sonra ikisi keklerini yedi ve oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Buyurun, sevgili arkadaşım, bu dilim sizin"
   - Cümle 10: «"Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty.»
   - Açıklama: Hello Kitty annesine 'sevgili arkadaşım' diye sesleniyor, hitap konuşulan kişiye uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Buyurun, sevgili arkadaşım, bu"
   - Cümle 10: «"Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty.»
   - Açıklama: Hello Kitty annesine 'sevgili arkadaşım' diye sesleniyor; hitap konuşulan kişiye uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Buyurun, sevgili arkadaşım, bu dilim sizin"
   - Cümle 10: «"Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş özelliği işe yaramıyor, annesine 'arkadaşım' diye hitap edilerek zorla sokulmuş.
4. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Buyurun, sevgili arkadaşım, bu dilim sizin"
   - Cümle 10: «"Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty.»
   - Açıklama: Kartın yanlar bölümünde annesi Hello Kitty'nin annesidir; ona arkadaş rolü verilerek ilişki değiştiriliyor.
   - Açıklama: Kartın yanlar bölümündeki ilişkiye göre annesi olan yan, arkadaş olarak ve 'siz' diye anılıyor.
5. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sevgili arkadaşım"
   - Cümle 10: «"Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty.»
   - Açıklama: Belirsiz kelime sevgili bir rol hitabı olarak geçiyor; kartta böyle bir rol yok.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Buyurun, sevgili arkadaşım, bu dilim sizin"
   - Cümle 10: «"Buyurun, sevgili arkadaşım, bu dilim sizin," dedi Hello Kitty.»
   - Açıklama: Hello Kitty keki annesine veriyor ama ona arkadaşı gibi sesleniyor; ilişkiyle çelişiyor.
   - Açıklama: Hello Kitty annesine arkadaşım diye sesleniyor; karakter ilişkisiyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0183` birebir aynı, `@degisim: dürüst -> düzgün` (tutuyorsan), ardından `@onarim: abd0268ff32ce387c76333937764c6194c3ed31d`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0184 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0184
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kravat', fiil 'cevaplamak', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: oyuncağın kozalak başı kalın dalın üstünde durmadı | ince ve sivri bir dala kozalağı sıkıca taktı
@tohum: hello_kitty-0184
@degisim: cevaplamak -> dikmek
Bir sabah ormandaki kamp yeri bomboştu. Hello Kitty orada dallardan oyuncak arkadaşlar yapıyordu. Bir tanesi hazırdı ama öbürünün kozalak başı dalın üstünde durmadı. Dalın ucu çok kalındı ve kozalak hep yere kayıyordu. Hello Kitty o dalı bıraktı ve ince, sivri bir dal buldu. Yeni dalı toprağa dikti. Kozalağı dalın sivri ucuna sıkıca taktı. Bu kez baş hiç düşmedi. Hello Kitty uzun yeşil bir yapraktan ona bir kravat yaptı. İki küçük taştan da gözler koydu. Sonra ikisinin arasına oturdu ve gülümsedi. Hello Kitty çok sevindi, çünkü oyuncak arkadaşlarının ikisi de hazırdı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ormandaki kamp yeri bomboştu"
   - Cümle 1: «Bir sabah ormandaki kamp yeri bomboştu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kimse tek başına uzağa gitmez ama Hello Kitty ormanda yapayalnız.
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylerken Hello Kitty ormanda bomboş kamp yerinde yalnız kalıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ince, sivri bir dal buldu"
   - Cümle 5: «Hello Kitty o dalı bıraktı ve ince, sivri bir dal buldu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde sivri dal toplanıp kullanılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yapraktan ona bir kravat"
   - Cümle 9: «Hello Kitty uzun yeşil bir yapraktan ona bir kravat yaptı.»
   - Açıklama: Önceki cümlenin öznesi 'baş' olduğu için 'ona' zamirinin oyuncağı mı başı mı gösterdiği belli değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yapraktan ona bir kravat yaptı"
   - Cümle 9: «Hello Kitty uzun yeşil bir yapraktan ona bir kravat yaptı.»
   - Açıklama: 'ona' zamirinin yeni oyuncağı mı, başı mı, öbür oyuncağı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0184` birebir aynı, `@degisim: cevaplamak -> dikmek` (tutuyorsan), ardından `@onarim: 52413e892d74dbbc654db850d79e6df870bc4fcc`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0185 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0185
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kazak', fiil 'kaybetmek', sıfat 'düz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: kardeşinin kazağını sormadan giydi ve kaybetti | özür diledi ve kazağı bulup kardeşine verdi
@tohum: hello_kitty-0185
Serin bir rüzgar esiyordu. Hello Kitty parkta Mimi'nin sarı kazağını sormadan giymişti. Sonra koşarken kazağı çıkarmış ve bir yerde kaybetmişti. Mimi kazağını aradı ama bulamadı ve çok üzüldü. Hello Kitty yaptığı şeyi anladı. Mimi'nin yanına gitti ve en iyi arkadaşından özür diledi. Mimi başını salladı ve kardeşine gülümsedi. Hello Kitty nerede koştuğunu düşündü. Büyük ağacın yanındaki düz çimenlerde oynamıştı. Hello Kitty oraya gitti ve sarı kazağı çimenlerin üstünde buldu. Kazağı hemen Mimi'ye götürdü. Mimi kazağını giydi ve sevindi. İki kardeş el ele tutuştu ve mutlu mutlu oyunlarına döndü.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşından özür diledi"
   - Cümle 6: «Mimi'nin yanına gitti ve en iyi arkadaşından özür diledi.»
   - Açıklama: Kardeşi olan Mimi'ye 'en iyi arkadaşı' denmesi yeni bir kişi varmış gibi gösterip göndergeyi belirsizleştiriyor.
   - Açıklama: Kardeşi olan Mimi 'en iyi arkadaşı' diye yeniden tanıtılıyor ve kimin kastedildiği karışıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşından özür diledi"
   - Cümle 6: «Mimi'nin yanına gitti ve en iyi arkadaşından özür diledi.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği yalnız Mimi için bir etiket olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir etiket olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "en iyi arkadaşından özür diledi"
   - Cümle 6: «Mimi'nin yanına gitti ve en iyi arkadaşından özür diledi.»
   - Açıklama: Mimi aynı hikayede hem kardeş hem en iyi arkadaş olarak anılıyor ve bu çelişki yaratıyor.
   - Açıklama: Mimi önce en iyi arkadaş, sonra kardeş olarak anılıyor; ilişki çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0185` birebir aynı, ardından `@onarim: 505a7bef40a8ad44ac032de9ab87035c71dfd97b`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0186 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0186
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'lastik', fiil 'güzelleşmek', sıfat 'ıslak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: mutfaktan garip bir tık tık sesi geldi | ıslak kurabiye kutusunu masaya koyup kuruladı
@tohum: hello_kitty-0186
@degisim: güzelleşmek -> kurulamak
Dışarıda yağmur yağıyordu. Hello Kitty ile Mimi odada resim yapıyordu. Birden mutfaktan garip bir tık tık sesi geldi. Mimi biraz çekindi ve kardeşinin elini tuttu. "Gel, Mimi, bu sese birlikte bakalım," dedi Hello Kitty. İkisi yavaşça mutfağa yürüdü. Pencere biraz açıktı ve yağmur damlaları içeri düşüyordu. Damlalar pencerenin önündeki kurabiye kutusuna vuruyordu. Hello Kitty'nin en sevdiği kurabiyeler o kutudaydı. Hello Kitty ıslak kutuyu hemen masaya taşıdı ve bir bezle kuruladı. Mimi de pencereyi kapattı. Hello Kitty kutuyu açtı ve içine baktı. Kutunun lastik kapağı sayesinde kurabiyeler kuruydu. Hello Kitty çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (9):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ıslak kurabiye kutusunu masaya koyup kuruladı"
   - Cümle 0 (plan satırı): «mutfaktan garip bir tık tık sesi geldi | ıslak kurabiye kutusunu masaya koyup kuruladı»
   - Açıklama: Sorun tık tık sesi ama plan çözümü sesi değil kutunun kurulanmasını söylüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi biraz çekindi"
   - Cümle 4: «Mimi biraz çekindi ve kardeşinin elini tuttu.»
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi; 3 yaşındaki çocuk bilmeyebilir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty'nin en sevdiği kurabiyeler o kutudaydı"
   - Cümle 9: «Hello Kitty'nin en sevdiği kurabiyeler o kutudaydı.»
   - Açıklama: Kartta özellik kurabiye yapmayı sevmek; hikaye bunu en sevdiği kurabiyeler diye değiştiriyor ve özellik çözümde işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği kurabiyeler o kutudaydı"
   - Cümle 9: «Hello Kitty'nin en sevdiği kurabiyeler o kutudaydı.»
   - Açıklama: Tohumdaki özellik kurabiye yapmayı sevmek; hikayede yalnız kutudaki kurabiyelerden söz ediliyor ve özellik çözüme katkı vermiyor.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Hello Kitty'nin en sevdiği kurabiyeler o kutudaydı"
   - Cümle 9: «Hello Kitty'nin en sevdiği kurabiyeler o kutudaydı.»
   - Açıklama: Kartın özellikler alanına göre Hello Kitty en çok elmalı turtayı sever; en sevdiğinin kurabiye olduğu yanlış bilgidir.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty ıslak kutuyu hemen masaya taşıdı"
   - Cümle 10: «Hello Kitty ıslak kutuyu hemen masaya taşıdı ve bir bezle kuruladı.»
   - Açıklama: Sesin sebebi açık pencereden düşen damlalar; kutuyu kurulamak bu sebebe yönelmiyor.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "ıslak kutuyu hemen masaya taşıdı"
   - Cümle 10: «Hello Kitty ıslak kutuyu hemen masaya taşıdı ve bir bezle kuruladı.»
   - Açıklama: Figürün çözümü kutuyu kurulamak; sesin sebebi olan açık pencereye yönelmiyor.
8. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Mimi de pencereyi kapattı"
   - Cümle 11: «Mimi de pencereyi kapattı.»
   - Açıklama: Sesin asıl sebebini yan karakter Mimi pencereyi kapatarak gideriyor.
   - Açıklama: Sesin asıl sebebi olan açık pencereyi figür değil yan karakter Mimi kapatıyor.
9. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "lastik kapağı sayesinde"
   - Cümle 13: «Kutunun lastik kapağı sayesinde kurabiyeler kuruydu.»
   - Açıklama: 'Sayesinde' soyut bir bağlantı kelimesi; küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0186` birebir aynı, `@degisim: güzelleşmek -> kurulamak` (tutuyorsan), ardından `@onarim: 189d5eb88f9d6cb2d5ffb32e7b59903fa040cfd0`, sonra gövde.
