# Editör görevi (onarım): Elsa, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Elsa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar16.txt --ad urun_v2`
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

## Kart: Elsa (kaynaklı, kapalı dünya)

- Ad: Elsa (okunuş: elsa; kesme eki okunuşa uyar)
- Kimlik: Elsa, buzu ve karı yönetebilen, bir krallığın genç kraliçesidir.
- Tür: kraliçe
- Güvenli özellik kullanımı: Buz ve kar gücü yalnız zararsız, güzel şeyler için kullanılır: kar yağdırır, buzdan şekil yapar. Hiçbir canlı donmaz, üşümez ya da incinmez; kimse buz tutmuş göl ya da deniz üstünde yürümez.
- Özellikler:
  - buz: Elinden buz ve kar çıkar; buzdan şekiller yapabilir. (örnek biçimler: buzdan, buzu)
  - kraliçe: Kraliçedir; kız kardeşini korur. (örnek biçimler: kraliçe)
- Yerler:
  - dağ: Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.
  - orman: Karlı ağaçlarla dolu orman.
  - deniz: Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.
  - şato: Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Anna: Elsa'nın cesur küçük kız kardeşi. Tür: prenses; konuşur. Yüzey biçimleri: Anna, kardeş, kardeşi
  - Olaf: Elsa'nın büyüsüyle canlanan neşeli kardan adam; sıcak sarılmaları ve yazı sever. Tür: kardan adam; konuşur. Yüzey biçimleri: Olaf, kardan adam
  - Kristoff: Buz toplayıp satan cesur dağ adamı; ren geyiği Sven'in arkadaşı. Tür: adam; konuşur. Yüzey biçimleri: Kristoff
  - Sven: Kristoff'un ren geyiği; kızağı çeker. Tür: ren geyiği; KONUŞMAZ. Yüzey biçimleri: Sven, ren geyiği, geyik
- Dünya kuralları:
  - Sven konuşmaz; sesle ve hareketle anlatır.
  - Anna Elsa'nın küçük kız kardeşidir; Elsa ablasıdır.
  - Olaf Elsa'nın büyüsüyle yapılmış kardan adamdır; hikayede erimez ya da parçalanmaz.
  - Elsa'nın gücü kimseyi dondurmaz ve incitmez.
- Yasak adlar: Hans, Weselton, Pabbie, Oaken, Marshmallow, Bruni, Arendelle
- Yasak: Anne babanın gemi yolculuğu, fırtına, troller, kurtlar ve kar canavarı hikayeye girmez.
- İzinli dünya kelimeleri: buz, kar, kraliçe, saray, kızak, fiyort, geyik

## Onarılacak hikâyeler

### Hikâye 1: tohum elsa-0008 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0008
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'küp', fiil 'dökülmek', sıfat 'meşgul'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: yukarıdan dökülen buz küpleri kuleyi yıktı | küplerin geldiği deliği buldu ve buzla kapattı
@tohum: elsa-0008
@degisim: meşgul -> hızlı
Bir sabah Elsa dağda, sarayının önünde karla bir kule yapıyordu. Birden yukarıdan buz küpleri döküldü ve kule yıkıldı. Elsa küplerin nereden geldiğini çok merak etti. Elsa karda küçük izler gördü ve yokuşu çıktı. Orada Kristoff kızağına buz küpleri yüklüyordu. Kristoff çok hızlı çalışıyordu ve arkasına hiç bakmıyordu. Kızağın altında küçük bir delik vardı. Küpler bu delikten tek tek düşüyor ve aşağı kayıyordu. Elsa elinden buz çıkardı ve deliği sıkıca kapattı. Artık hiçbir küp dökülmedi. Kristoff dönünce buzlu deliği gördü ve Elsa'ya teşekkür etti. Elsa geri döndü ve kulesini yeniden yaptı. Elsa çok sevindi, çünkü deliği bulmuş ve kapatmıştı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa karda küçük izler gördü ve yokuşu çıktı"
   - Cümle 4: «Elsa karda küçük izler gördü ve yokuşu çıktı.»
   - Açıklama: Çözüm iz sürme, yokuşu çıkma, deliği bulma ve kapatma olmak üzere ikiden fazla adım sürüyor; izlerin ne olduğu da belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0008` birebir aynı, `@degisim: meşgul -> hızlı` (tutuyorsan), ardından `@onarim: e8dc80ae602cbc373f1e52984ec1cc137b3bfc74`, sonra gövde.

### Hikâye 2: tohum elsa-0027 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0027
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yatak', fiil 'küçülmek', sıfat 'sabunlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: arkadaşı da oynamak istedi ama tek dal vardı | dalı ikiye bölüp yarısını ona verdi
@tohum: elsa-0027
@degisim: yatak -> kova
Dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Elsa bir kova sabunlu suya ince bir dal batırıp baloncuk yapıyordu. Olaf da oynamak istedi ama karda başka dal yoktu. "Elsa, ben ne yapacağım?" diye sordu Olaf. Elsa kraliçeydi ve Olaf'ın üzülmesini istemedi. Dalı dikkatle ikiye böldü. İki parça da baloncuk yapmak için yeterince uzundu. "Olaf, bu parça senin," dedi Elsa. İkisi dallarını suya batırıp üfledi. Parlak baloncuklar havada yükseldi ve küçüldü. Olaf onların arasında zıpladı ve güldü. Elsa ile Olaf kovanın başında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve Olaf'ın üzülmesini istemedi"
   - Cümle 5: «Elsa kraliçeydi ve Olaf'ın üzülmesini istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği dalı bölmede işe yaramıyor, yalnız gerekçe olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0027` birebir aynı, `@degisim: yatak -> kova` (tutuyorsan), ardından `@onarim: 3594a01dc4fcefbb0a5680338328617c697aa5cd`, sonra gövde.

### Hikâye 3: tohum elsa-0036 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0036
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kapı', fiil 'değiştirmek', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: kızak kabarık bir kar yığınına girip takıldı | kızaktan indi ve yolu değiştirdi
@tohum: elsa-0036
@degisim: kapı -> kızak
Karlı ormanda Elsa ile Sven kızak oyunu oynuyordu. Sven önde koşuyor, Elsa da kızakta neşeyle şarkı söylüyordu. Ama kızak kabarık bir kar yığınına girdi ve durdu. Sven bütün gücüyle çekti ama kızak hiç kıpırdamadı. Sven çok yoruldu. Elsa kraliçeydi ve yorgun Sven'i korumak için hemen kızaktan indi. Kızak hafifledi ve Sven onu kolayca geri çekti. "Sven, yolu değiştirelim, şu yolda kar sert," dedi Elsa. Sven başını salladı ve kızağı o yola götürdü. Elsa yeniden kızağa oturdu. Bu yolda kızak kolayca kaydı. Elsa ile Sven ağaçların arasında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yorgun Sven'i korumak için"
   - Cümle 6: «Elsa kraliçeydi ve yorgun Sven'i korumak için hemen kızaktan indi.»
   - Açıklama: Kızaktan inmek Sven'i korumak değil ona yardım etmek; 'korumak' yanlış anlamda.
   - Açıklama: Kızaktan inmek Sven'i korumak değil, yükünü hafifletmektir; fiil yanlış anlamda.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve yorgun Sven'i korumak"
   - Cümle 6: «Elsa kraliçeydi ve yorgun Sven'i korumak için hemen kızaktan indi.»
   - Açıklama: Karttaki özellik kız kardeşini korumak; burada kraliçelik Sven'e yöneltiliyor.
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; burada kraliçelik Sven'i korumaya bağlanarak karttan farklı kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0036` birebir aynı, `@degisim: kapı -> kızak` (tutuyorsan), ardından `@onarim: 3366e46b5f86c0e10218d5805b1bf6748f8322c0`, sonra gövde.

### Hikâye 4: tohum elsa-0037 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0037
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'fıstık', fiil 'sallamak', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: buz sarayının kapısından garip bir ses geldi | dışarı çıkıp baktı ve düşen fıstıkları gördü
@tohum: elsa-0037
Bir sabah Elsa dağda, buz sarayında oturuyordu. Birden kapıdan garip bir tık tık sesi geldi. Elsa kraliçeydi ve konuğu karşılamak için hemen kapıya gitti. Kapıyı açtı ama dışarıda kimse yoktu. Karın üstünde küçük kahverengi fıstıklar vardı. Elsa başını kaldırdı ve kapının yanındaki büyük ağacı gördü. Rüzgar ağacın dallarını sallıyordu. Bir fıstık daldan düştü ve kapıya çarptı. Tık tık sesi yine geldi. Elsa güldü. Bu eğlenceli sesi düşen fıstıklar yapıyordu. Sonra Elsa fıstıkları topladı ve onlarla karda mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "konuğu karşılamak için hemen kapıya gitti"
   - Cümle 3: «Elsa kraliçeydi ve konuğu karşılamak için hemen kapıya gitti.»
   - Açıklama: Kimin çaldığı bilinmeyen kapıyı hemen açmak çocuğun taklit edebileceği güvensiz bir davranış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve konuğu karşılamak için"
   - Cümle 3: «Elsa kraliçeydi ve konuğu karşılamak için hemen kapıya gitti.»
   - Açıklama: Ortada bilinen bir konuk yokken belirli 'konuğu' kullanılmış; 'gelen konuğu' ya da 'konuk' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "konuğu karşılamak için"
   - Cümle 3: «Elsa kraliçeydi ve konuğu karşılamak için hemen kapıya gitti.»
   - Açıklama: Belirli 'konuğu' hiç tanıtılmamış bir kişiyi gösteriyor; 'gelen konuğu' ya da 'kimin geldiğine bakmak' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve konuğu karşılamak"
   - Cümle 3: «Elsa kraliçeydi ve konuğu karşılamak için hemen kapıya gitti.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşini korumaktır; burada yalnız kapıya gitme gerekçesi olarak geçiyor ve sorunu çözmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0037` birebir aynı, ardından `@onarim: 2c6a2e1c13b060802bfa40bd1eb8f2ed116a90cf`, sonra gövde.

### Hikâye 5: tohum elsa-0039 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0039
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çalı', fiil 'sararmak', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: kar topları birer birer kayboluyordu | izlere bakıp buzdan kaşıkla topları çıkardı
@tohum: elsa-0039
Elsa ile Olaf dağda, sarayın önünde yuvarlak kar topları yapıyordu. Olaf topları yokuşun başına diziyordu. Ama Olaf'ın topları birer birer kayboluyordu. "Toplarım nereye gidiyor?" diye sordu Olaf. Elsa karda ince izler gördü. İzler yokuştan aşağı, sararmış bir çalıya gidiyordu. Elsa ile Olaf çalıya kadar yürüdü. Toplar yokuştan yuvarlanmış ve çalının altına girmişti. Çalının dalları sıktı ve Elsa topları eliyle alamadı. Elsa elinden buzdan uzun bir kaşık yaptı. Topları çalının altından tek tek çıkardı. "İşte toplarım!" dedi Olaf sevinçle. Sonra Olaf topları düz bir yere dizdi. Elsa ile Olaf kar topu oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çalının dalları sıktı"
   - Cümle 9: «Çalının dalları sıktı ve Elsa topları eliyle alamadı.»
   - Açıklama: 'Sıkıydı' olmalı; 'sıktı' sıkmak fiili olarak okunuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çalının dalları sıktı"
   - Cümle 9: «Çalının dalları sıktı ve Elsa topları eliyle alamadı.»
   - Açıklama: 'sıktı' dalların bir şeyi sıktığı biçimde okunuyor; 'dalları çok sıktı/sık sıktı' anlamı belirsiz.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa elinden buzdan uzun bir kaşık yaptı"
   - Cümle 10: «Elsa elinden buzdan uzun bir kaşık yaptı.»
   - Açıklama: 'elinden ... yaptı' yapısı bozuk; 'Elsa buzdan uzun bir kaşık yaptı' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa elinden buzdan uzun"
   - Cümle 10: «Elsa elinden buzdan uzun bir kaşık yaptı.»
   - Açıklama: 'Elinden' burada yanlış anlamda; kaşık elden değil buzdan yapılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0039` birebir aynı, ardından `@onarim: 8505b0c82bdfa593745ce4a005399345d02ccdbd`, sonra gövde.

### Hikâye 6: tohum elsa-0040 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0040
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: kaybolan eşya
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'halat', fiil 'kurtarmak', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: kızağın halatı düştü ve iki taşın arasına girdi | buzdan uzun bir çubuk yapıp halatı çekti
@tohum: elsa-0040
@degisim: ferah -> geniş
Rüzgar esiyordu. Elsa sarayın önünde, geniş bir yerde kızağıyla oynuyordu. Ama halat kızağa sıkı bağlı değildi. Kızak iki büyük taşın yanından geçerken halat düştü ve kayboldu. Elsa her yere baktı. Sonunda iki taşın arasında halatı gördü. Ama taşların arası çok dardı ve eli oraya girmedi. Elsa parmaklarını oynattı ve buzdan uzun bir çubuk yaptı. Çubuğu taşların arasına soktu ve halatı yavaşça çekti. Halat taşların arasından çıktı. Elsa halatı kızağa bu kez sıkıca bağladı. Elsa çok sevindi, çünkü halatı kurtarmıştı ve oyununa dönebilirdi.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "halat düştü ve kayboldu"
   - Cümle 4: «Kızak iki büyük taşın yanından geçerken halat düştü ve kayboldu.»
   - Açıklama: Asıl sorun olan halatın düşüp kaybolması ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0040` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 97a7587b8d0c5f3bcf65eee2d9da814c7667cd20`, sonra gövde.

### Hikâye 7: tohum elsa-0041 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0041
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gül', fiil 'tanımak', sıfat 'uyanık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: havucu tanımadı ve onu yokuştan aşağı attı | özür diledi ve saraydan yeni havuç getirdi
@tohum: elsa-0041
@degisim: gül -> havuç
Karlı dağda, buzdan sarayın kapısında Elsa karı temizliyordu. Karın içinde turuncu bir uç vardı ama Elsa onu tanımadı. Onu bir dal sandı ve yokuştan aşağı attı. Birden Sven geldi ve yokuşa üzgün üzgün baktı. O, Sven'in karda sakladığı havuçtu. Sven uyanıktı ve çok acıkmıştı. Elsa hatasını hemen anladı. "Özür dilerim, Sven, havucunu ben attım," dedi Elsa. Elsa bu sarayın kraliçesiydi ve hemen içeri girdi. Saraydan Sven'e yeni ve büyük bir havuç getirdi. Sven havucu yedi ve Elsa'ya burnunu sürttü. Sonra Elsa ile Sven karda mutlu mutlu koştu.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Onu bir dal sandı"
   - Cümle 3: «Onu bir dal sandı ve yokuştan aşağı attı.»
   - Açıklama: Karda turuncu bir ucu dal sanmak akla yatkın bir sebep değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O, Sven'in karda sakladığı havuçtu"
   - Cümle 5: «O, Sven'in karda sakladığı havuçtu.»
   - Açıklama: 'O' zamiri Sven'den hemen sonra geldiği için neyi gösterdiği belirsiz.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "O, Sven'in karda sakladığı havuçtu"
   - Cümle 5: «O, Sven'in karda sakladığı havuçtu.»
   - Açıklama: Atılan şeyin havuç olduğu ve sorun ancak 5. cümlede anlaşılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sven uyanıktı ve çok"
   - Cümle 6: «Sven uyanıktı ve çok acıkmıştı.»
   - Açıklama: 'Uyanık' burada anlamsız ve 'kurnaz' anlamına da kayabiliyor; yerinde kullanılmamış.
   - Açıklama: 'Uyanık' burada anlamı belirsiz ve bağlama uymuyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sven uyanıktı ve çok acıkmıştı"
   - Cümle 6: «Sven uyanıktı ve çok acıkmıştı.»
   - Açıklama: Sven'in uyanık olması hiçbir işe yaramayan sebepsiz bir ayrıntı.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve hemen içeri girdi"
   - Cümle 9: «Elsa bu sarayın kraliçesiydi ve hemen içeri girdi.»
   - Açıklama: Tohumdaki kraliçe özelliği havuç getirmede gerçekten işe yaramıyor, yalnız anılıyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 9: «Elsa bu sarayın kraliçesiydi ve hemen içeri girdi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, kız kardeşini koruma biçiminde işe yarar kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız sayılıyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 9: «Elsa bu sarayın kraliçesiydi ve hemen içeri girdi.»
   - Açıklama: Elsa'nın kraliçe olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0041` birebir aynı, `@degisim: gül -> havuç` (tutuyorsan), ardından `@onarim: 470b00d94999d4db193899bfd854aca85ca395b9`, sonra gövde.

### Hikâye 8: tohum elsa-0044 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0044
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kayık', fiil 'durmak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: arkadaşı da kaymak istedi ama kızağı yoktu | büyük kızağını paylaşıp onu arkasına oturttu
@tohum: elsa-0044
@degisim: kayık -> kızak
Ormanda hafif bir rüzgar esiyordu. Elsa küçük bir yokuştan kızakla kayıyordu. Olaf da kaymak istedi ama onun kızağı yoktu. "Ben de kaymak istiyorum!" dedi Olaf sabırsız bir sesle. Kızak aşağıda, Olaf'ın hemen önünde durdu. Elsa bir kraliçeydi ve kızağı çok büyüktü. "Gel, Olaf, bu kızak ikimize de yeter," dedi Elsa. İkisi kızağı yokuşun başına çekti. Elsa öne oturdu ve kızağın ipini iki eliyle tuttu. Olaf onun arkasına yerleşti ve ona sıkıca tutundu. Kızak yavaşça aşağı indi. Olaf kollarını açtı ve kahkahalarla güldü. "Birlikte çok daha eğlenceli!" dedi Olaf. Elsa ile Olaf mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bir kraliçeydi ve"
   - Cümle 6: «Elsa bir kraliçeydi ve kızağı çok büyüktü.»
   - Açıklama: Elsa hikayenin ortasında yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve kızağı çok büyüktü"
   - Cümle 6: «Elsa bir kraliçeydi ve kızağı çok büyüktü.»
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumakla ilgili; burada yalnız büyük kızağa bahane olarak zayıf biçimde kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve kızağı çok büyüktü"
   - Cümle 6: «Elsa bir kraliçeydi ve kızağı çok büyüktü.»
   - Açıklama: Kraliçelik bilgisi olaya zorla eklenmiş ve kızağın büyüklüğünü sebepsizce açıklıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0044` birebir aynı, `@degisim: kayık -> kızak` (tutuyorsan), ardından `@onarim: 735144dfe13aa6725821d830a61142ce8bbf4fd9`, sonra gövde.

### Hikâye 9: tohum elsa-0045 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0045
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çekirdek', fiil 'eklemek', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yumuşak kardan yapılan kule yana devrildi | karı sıkıca bastırıp duvara yeni bir kule ekledi
@tohum: elsa-0045
@degisim: çekirdek -> duvar
Karlı dağda, buzdan sarayın yanında güneş parlıyordu. Elsa karla küçük bir kale yapıyordu. Ama kalenin uzun kulesi yumuşak kardandı ve birden yana devrildi. Elsa devrilen kuleye baktı ve biraz mutsuz oldu. Sonra sarayına baktı. Elsa bir kraliçeydi ve sarayının kuleleri sert buzdandı. Elsa yerden yeni kar aldı. Karı iki eliyle sıkıca bastırdı ve sert bir top yaptı. Bu sıkı kardan kalenin duvarına yeni bir kule ekledi. Elsa kuleye yavaşça dokundu. Yeni kule bu kez hiç devrilmedi ve duvarın üstünde dik durdu. Elsa kalesinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve sarayının kuleleri sert buzdandı"
   - Cümle 6: «Elsa bir kraliçeydi ve sarayının kuleleri sert buzdandı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir; kız kardeşini korur) sorunu çözmede işe yaramıyor, yalnız anılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve sarayının kuleleri"
   - Cümle 6: «Elsa bir kraliçeydi ve sarayının kuleleri sert buzdandı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız sayılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve sarayının kuleleri sert buzdandı"
   - Cümle 6: «Elsa bir kraliçeydi ve sarayının kuleleri sert buzdandı.»
   - Açıklama: Kraliçelik ayrıntısı olaya bağlanmadan araya sokuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0045` birebir aynı, `@degisim: çekirdek -> duvar` (tutuyorsan), ardından `@onarim: f7e13e1b3f172efb5d01ca5ba13f259eb06dfddd`, sonra gövde.

### Hikâye 10: tohum elsa-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0047
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tarak', fiil 'gülümsemek', sıfat 'nazik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: tarak elinden kayıp derin karın içinde kayboldu | nazikçe yardım istedi ve geyiğin gösterdiği yeri kazdı
@tohum: elsa-0047
Karlı ormanda Elsa, Sven'in tüylerini tarıyordu. Birden tarak elinden kaydı ve kara düştü. Kar çok derindi ve tarak kayboldu. Elsa elleriyle aradı ama tarağı bulamadı. Elsa bir kraliçeydi, ama Sven'e emir vermedi. "Sven, tarağı bulmama yardım eder misin?" diye nazikçe sordu Elsa. Sven burnunu kara soktu ve kokladı. Bir yerde durdu ve ayağıyla karı gösterdi. Elsa orayı kazdı ve tarağı karın içinden çıkardı. Elsa gülümsedi ve Sven'in başını okşadı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Elsa çok sevindi, çünkü yardım isteyince tarağını bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sven'e emir vermedi"
   - Cümle 5: «Elsa bir kraliçeydi, ama Sven'e emir vermedi.»
   - Açıklama: 'Emir vermek' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama Sven'e emir vermedi"
   - Cümle 5: «Elsa bir kraliçeydi, ama Sven'e emir vermedi.»
   - Açıklama: 'Kraliçe' ve 'emir vermek' soyut kavramlar, 3 yaşındaki çocuk için uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi, ama Sven'e emir vermedi"
   - Cümle 5: «Elsa bir kraliçeydi, ama Sven'e emir vermedi.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki 'kız kardeşini korur' anlamında değil, yalnız olumsuz bir not olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız etiket olarak anılıyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0047` birebir aynı, ardından `@onarim: 1ec75f530aec935c928343e19508a4b738c148b2`, sonra gövde.

### Hikâye 11: tohum elsa-0050 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0050
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'alet', fiil 'yıkanmak', sıfat 'şapkalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: iki kardeş tek kar aletini aynı anda istedi | sırayla kullanmayı önerdi ve önce kardeşine verdi
@tohum: elsa-0050
@degisim: yıkanmak -> beklemek
Ormanda Elsa ile şapkalı Anna kardan bir kale yapıyordu. Ama ellerinde Elsa'nın buzdan yaptığı tek bir kar aleti vardı. İkisi de aleti aynı anda istedi. "Önce ben kazacağım!" dedi Anna. Elsa biraz düşündü. "Sırayla kullanalım, Anna, önce sen başla," dedi Elsa. Anna aletle kaleye güzel bir kapı açtı. Elsa da sırasını bekledi. Biraz sonra Anna aleti Elsa'ya verdi. Elsa aletle kaleye küçük bir pencere açtı. "Kalemiz çok güzel oldu, Elsa!" dedi Anna. Elsa çok sevindi, çünkü sırayla oynayınca kaleyi birlikte bitirmişlerdi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa'nın buzdan yaptığı tek bir kar aleti"
   - Cümle 2: «Ama ellerinde Elsa'nın buzdan yaptığı tek bir kar aleti vardı.»
   - Açıklama: Tohumdaki buz özelliği sorunu çözmekte işe yaramıyor, yalnız arka planda anılıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa'nın buzdan yaptığı tek bir kar aleti"
   - Cümle 2: «Ama ellerinde Elsa'nın buzdan yaptığı tek bir kar aleti vardı.»
   - Açıklama: Elsa buzdan şekiller yapabildiği halde ikinci bir alet yapmaması sorunun sebebini akla yatkın olmaktan çıkarıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0050` birebir aynı, `@degisim: yıkanmak -> beklemek` (tutuyorsan), ardından `@onarim: b46e47bb21963280591293d14a6f373a54e41594`, sonra gövde.

### Hikâye 12: tohum elsa-0051 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0051
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yelken', fiil 'susmak', sıfat 'masmavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yelken rüzgara ters durduğu için kızak kaymadı | bayrağa bakıp yelkeni rüzgara çevirdi
@tohum: elsa-0051
@degisim: susmak -> bakmak
Bir sabah Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu. Kızağa uzun bir dal dikmiş ve pelerinini yelken yapmıştı. Ama kızak hiç kaymadı, çünkü yelken rüzgara ters duruyordu. Sarayın tepesinde Kraliçe Elsa'nın bayrağı vardı. Elsa bayrağa baktı ve rüzgarın sağdan estiğini gördü. Sonra yelkeni rüzgara doğru çevirdi. Yelken birden şişti. Kızak düz karın üstünde yavaş yavaş kaymaya başladı. Elsa kızağın içinde oturdu ve güldü. Kızak masmavi gökyüzünün altında sarayın önünde bir tur attı. Elsa çok sevindi, çünkü yeni bir şeyi denemiş ve başarmıştı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sarayın tepesinde Kraliçe Elsa'nın bayrağı"
   - Cümle 4: «Sarayın tepesinde Kraliçe Elsa'nın bayrağı vardı.»
   - Açıklama: Elsa unvanıyla üçüncü kişi gibi anılıyor; aynı kişi mi belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa'nın bayrağı vardı"
   - Cümle 4: «Sarayın tepesinde Kraliçe Elsa'nın bayrağı vardı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız bayrak etiketi olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bayrak sahibi olarak anılıyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0051` birebir aynı, `@degisim: susmak -> bakmak` (tutuyorsan), ardından `@onarim: b9b60ae8bf84aef0e10fb9ebe009c851e61a40a9`, sonra gövde.
