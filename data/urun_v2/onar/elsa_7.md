# Editör görevi (onarım): Elsa, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar7.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0004 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0004
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yelpaze', fiil 'söylemek', sıfat 'özel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: ince tahta ayak ağır buzların altında kırıldı | buzdan kalın ve sağlam bir kızak ayağı yaptı
@tohum: elsa-0004
@degisim: yelpaze -> kızak
Bir sabah Elsa dağda, sarayının önünde yürüyordu. Kristoff orada kızağına buz parçaları yüklüyordu. Ama kızağın tahta ayağı çok inceydi ve buzların altında kırıldı. "Elsa, kızak kaymazsa buzları satamam!" dedi Kristoff. Elsa ona yardım etmek istedi. Kırık ayağa dikkatle baktı. Sonra Kristoff'a biraz geri durmasını söyledi. Elsa ellerini açtı ve kızağın altına buzdan kalın bir ayak yaptı. Kızak ağır buzlarla yeniden düz durdu. Kristoff kızağı itti ve kızak karda kolayca kaydı. "Bu çok özel bir kızak oldu, Elsa!" dedi Kristoff. Elsa çok sevindi, çünkü Kristoff'un kızağı yeniden kayıyordu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "buzdan kalın ve sağlam bir kızak ayağı yaptı"
   - Cümle 0 (plan satırı): «ince tahta ayak ağır buzların altında kırıldı | buzdan kalın ve sağlam bir kızak ayağı yaptı»
   - Açıklama: Gövdede Elsa'nın buzdan ayak yaptığı anlatılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0004` birebir aynı, `@degisim: yelpaze -> kızak` (tutuyorsan), ardından `@onarim: a96285419ac495fb9de926858b5d4382117a9c6b`, sonra gövde.

### Hikâye 2: tohum elsa-0012 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0012
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'fiyonk', fiil 'okumak', sıfat 'çekingen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: kurdele hep açıldı çünkü fiyonk bağlamayı bilmiyordu | arkadaşından yardım istedi ve fiyonk bağlamayı öğrendi
@tohum: elsa-0012
@degisim: okumak -> bağlamak
Bir sabah Elsa dağda, sarayının önünde buzdan küçük bir çiçek yaptı. Çiçeğin sapına kırmızı bir fiyonk bağlamak istedi. Ama fiyonk bağlamayı bilmiyordu ve kurdele hep açıldı. Kristoff biraz ileride kızağını dolduruyordu. Elsa önce çekingen çekingen Kristoff'a baktı. Sonra Kristoff'un yanına yürüdü. "Kristoff, bana fiyonk bağlamayı öğretir misin?" diye sordu Elsa. "Tabii, çok kolay," dedi Kristoff. Kristoff her adımı yavaşça gösterdi. Elsa da iki halka yaptı ve onları sıkıca bağladı. Bu kez kurdele hiç açılmadı. "Teşekkürler, Kristoff, bu fiyonklu çiçek de senin!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kurdele hep açıldı"
   - Cümle 3: «Ama fiyonk bağlamayı bilmiyordu ve kurdele hep açıldı.»
   - Açıklama: 'Hep' ile süreklilik anlatılırken '-dı' uyumsuz; 'hep açılıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0012` birebir aynı, `@degisim: okumak -> bağlamak` (tutuyorsan), ardından `@onarim: e832ab1e35fcf5b467983173a59195da5cb64e4e`, sonra gövde.

### Hikâye 3: tohum elsa-0014 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0014
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'ceviz', fiil 'asmak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: oyundaki ağaçta hiç ceviz yoktu | buzdan minicik cevizler yapıp dallara astı
@tohum: elsa-0014
Rüzgar dağın tepesinde hafifçe esiyordu. Elsa sarayın önünde bahçe oyunu oynuyordu ve bir ceviz ağacı istiyordu. Ama önündeki ağaçta hiç ceviz yoktu, çünkü karlı dağda ceviz olmazdı. Elsa boş dallara baktı ve biraz düşündü. Sonra elini açtı ve buzdan minicik cevizler yaptı. Cevizleri tek tek dallara astı. Birkaç adım geri gidip ağaca baktı. Dallarda şimdi parlak cevizler vardı. Rüzgar esince cevizler birbirine değdi ve hafif bir ses çıkardı. Elsa gülerek ellerini çırptı. Elsa çok mutlu oldu, çünkü oyunu için bir ceviz ağacı yapmıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bahçe oyunu oynuyordu ve bir ceviz ağacı istiyordu"
   - Cümle 2: «Elsa sarayın önünde bahçe oyunu oynuyordu ve bir ceviz ağacı istiyordu.»
   - Açıklama: 'Bahçe oyunu' belirsiz ve ceviz ağacı isteğiyle anlamlı bir bağ kurmuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bir ceviz ağacı istiyordu"
   - Cümle 2: «Elsa sarayın önünde bahçe oyunu oynuyordu ve bir ceviz ağacı istiyordu.»
   - Açıklama: Sorun keyfi bir istekten doğuyor; çocuğun önemseyeceği gerçek bir aksilik yok.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "önündeki ağaçta hiç ceviz yoktu"
   - Cümle 3: «Ama önündeki ağaçta hiç ceviz yoktu, çünkü karlı dağda ceviz olmazdı.»
   - Açıklama: Karlı dağda ağaçta ceviz olmaması uydurma ve çocuğun önemseyeceği gerçek bir sorun değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oyunu için bir ceviz ağacı yapmıştı"
   - Cümle 11: «Elsa çok mutlu oldu, çünkü oyunu için bir ceviz ağacı yapmıştı.»
   - Açıklama: Elsa ağaç yapmadı, var olan ağaca buzdan cevizler astı; fiil yanlış anlamda.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir ceviz ağacı yapmıştı"
   - Cümle 11: «Elsa çok mutlu oldu, çünkü oyunu için bir ceviz ağacı yapmıştı.»
   - Açıklama: Elsa ağaç yapmadı, var olan ağaca buzdan ceviz astı; fiil olaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0014` birebir aynı, ardından `@onarim: e23d6ddd8593ecca1fefb41c52c6e2da7e23b5f1`, sonra gövde.

### Hikâye 4: tohum elsa-0017 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0017
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'sandalye', fiil 'hazırlamak', sıfat 'ahşap'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: yorgun arkadaşın oturacak kuru bir yeri yoktu | kendi ahşap sandalyesini ona verdi
@tohum: elsa-0017
Elsa limanda ahşap kraliçe sandalyesine oturmuş, denizi seyrediyordu. Kristoff uzun süre kızağını yüklemişti ve çok yorgundu. Ama kıyıdaki taşlar ıslaktı ve oturacak kuru bir yer yoktu. Elsa hemen sandalyesinden kalktı. "Kristoff, gel, bu sandalyeye sen otur," dedi Elsa. "Ama bu sandalye senin," dedi Kristoff. "Sen benden daha yorgunsun," dedi Elsa. Kristoff teşekkür etti ve sandalyeye oturdu. Elsa da sandalyenin yanında durdu. İkisi birlikte denizdeki küçük dalgalara baktı. Biraz sonra Kristoff dinlendi ve kalktı. Sonra Elsa ile Kristoff kızağı birlikte mutlu mutlu hazırladı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ahşap kraliçe sandalyesine oturmuş"
   - Cümle 1: «Elsa limanda ahşap kraliçe sandalyesine oturmuş, denizi seyrediyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız sandalyenin sıfatı olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0017` birebir aynı, ardından `@onarim: 0ce74eb8821f525a6402ed57df0d3294c888fdb8`, sonra gövde.

### Hikâye 5: tohum elsa-0019 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0019
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'şeftali', fiil 'değişmek', sıfat 'çilekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: arkadaşı geldi ama onun hiç yiyeceği yoktu | şeftaliyi ona verdi ve keki ikiye böldü
@tohum: elsa-0019
@degisim: değişmek -> paylaşmak
Bir sabah Elsa dağda, sarayının önünde sepetini açtı. Sepette bir şeftali ile çilekli bir kek vardı. O sırada Olaf geldi ama onun hiç yiyeceği yoktu. Olaf sepete baktı ve sessizce bekledi. Elsa şeftaliyi hemen Olaf'a uzattı. Sonra çilekli keki elleriyle ikiye böldü. Elsa elini salladı ve buzdan iki küçük tabak yaptı. Kekin yarısını Olaf'ın tabağına koydu. Olaf kocaman gülümsedi ve Elsa'ya sarıldı. İkisi yan yana oturdu ve keklerini mutlu mutlu yedi. Elsa bundan sonra yiyeceklerini hep Olaf ile paylaştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Olaf geldi ama onun hiç yiyeceği yoktu"
   - Cümle 3: «O sırada Olaf geldi ama onun hiç yiyeceği yoktu.»
   - Açıklama: Olaf'ın neden hiç yiyeceği olmadığı, yani sorunun sebebi söylenmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "onun hiç yiyeceği yoktu"
   - Cümle 3: «O sırada Olaf geldi ama onun hiç yiyeceği yoktu.»
   - Açıklama: Olaf'ın neden yiyeceği olmadığı söylenmiyor; sorunun sebebi yok.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "keklerini mutlu mutlu yedi"
   - Cümle 10: «İkisi yan yana oturdu ve keklerini mutlu mutlu yedi.»
   - Açıklama: Kartın yanlar alanında kardan adam olarak tanımlanan Olaf dizide kek ve şeftali yiyen biri olarak bilinmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0019` birebir aynı, `@degisim: değişmek -> paylaşmak` (tutuyorsan), ardından `@onarim: 94a2b6e643ab9f91dc4d24b618e31d7aaf57736b`, sonra gövde.

### Hikâye 6: tohum elsa-0020 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0020
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bileklik', fiil 'ulaşmak', sıfat 'yepyeni'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik buzlu yolda kaydı ve kapıya ulaşamadı | pelerinini yola serdi ve geyik kapıya yürüdü
@tohum: elsa-0020
@degisim: bileklik -> havuç
Rüzgar dağda sert sert esiyordu. Sven, Elsa'nın sarayına girmek istedi, çünkü rüzgar çok sertti. Ama kapıya giden yol buzluydu ve Sven her adımda kaydı. Sven kapıya ulaşamadı ve geri çekildi. Elsa kapıdan onu gördü. "Üzülme, Sven, sana yardım edeceğim," dedi Elsa. Elsa yepyeni kraliçe pelerinini çıkardı. Pelerini buzlu yolun üstüne serdi. Sven pelerine bastı ve bu kez hiç kaymadı. Yavaş yavaş yürüdü ve kapıya ulaştı. Elsa sarayda ona bir havuç verdi. Sven havucu mutlu mutlu yedi ve Elsa da sevinçle güldü.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çünkü rüzgar çok sertti"
   - Cümle 2: «Sven, Elsa'nın sarayına girmek istedi, çünkü rüzgar çok sertti.»
   - Açıklama: Bir önceki cümledeki sert rüzgar gereksiz yere tekrarlanıyor.
   - Açıklama: Rüzgarın sert estiği bir önceki cümlede zaten söylendi; gereksiz tekrar.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa yepyeni kraliçe pelerinini çıkardı"
   - Cümle 7: «Elsa yepyeni kraliçe pelerinini çıkardı.»
   - Açıklama: Tohumdaki kraliçelik özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız pelerine süs sıfatı olarak geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yepyeni kraliçe pelerinini çıkardı"
   - Cümle 7: «Elsa yepyeni kraliçe pelerinini çıkardı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız pelerinin sıfatı olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0020` birebir aynı, `@degisim: bileklik -> havuç` (tutuyorsan), ardından `@onarim: e96b7708dcc7af72a80f678069dee5cb4a9f0887`, sonra gövde.

### Hikâye 7: tohum elsa-0022 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0022
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'su', fiil 'dolanmak', sıfat 'soslu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kardeşi susamıştı ama yakında hiç su yoktu | su sesini izleyip dereyi buldu ve buzdan bardak yaptı
@tohum: elsa-0022
@degisim: soslu -> berrak
Elsa ile Anna dağda sarayın yakınında yürüyordu. Anna çok susamıştı ama yakında hiç su yoktu. Birden karın altından şırıl şırıl bir ses geldi. "Bu ses nereden geliyor, Elsa?" diye sordu Anna. İkisi büyük bir kayanın etrafında dolandı ve dinledi. Ses kayanın dibinden geliyordu. Elsa oradaki karı elleriyle iki yana itti. Karın altında berrak, küçük bir dere akıyordu. "Sesi bu dere yapıyormuş!" dedi Anna. Elsa elini salladı ve buzdan küçük bir bardak yaptı. Bardağı dereden doldurdu ve kardeşine verdi. Anna soğuk suyu içti ve güldü. "Teşekkürler, Elsa, su çok güzel!" dedi Anna. Sonra Elsa ile Anna yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden karın altından şırıl şırıl bir ses"
   - Cümle 3: «Birden karın altından şırıl şırıl bir ses geldi.»
   - Açıklama: Suyu bulduran ses tam susuzluk söylendiği anda sebepsizce beliriyor ve çözümü kendiliğinden getiriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bardağı dereden doldurdu ve kardeşine verdi"
   - Cümle 11: «Bardağı dereden doldurdu ve kardeşine verdi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde dereden arıtılmamış su içiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0022` birebir aynı, `@degisim: soslu -> berrak` (tutuyorsan), ardından `@onarim: 91277958c6087b3c0e165657187e5e50a47dae15`, sonra gövde.

### Hikâye 8: tohum elsa-0023 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0023
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'takvim', fiil 'yetiştirmek', sıfat 'kırılgan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: ikisi de açtı ama yalnız bir havuç vardı | kırılgan havucu ikiye böldü ve geyikle paylaştı
@tohum: elsa-0023
@degisim: takvim -> havuç
Dağda soğuk bir rüzgar esiyordu. Kraliçe Elsa buzdan sarayının önünde oturuyordu. Sven çok acıkmıştı ve Elsa'nın yanına geldi. Elsa da acıkmıştı ama sepetinde kendi yetiştirdiği tek bir havuç vardı. Sven havuca baktı ve kulaklarını oynattı. "Gel, Sven, bu havucu birlikte yiyelim," dedi Elsa. Havuç soğukta kalmış ve kırılgan olmuştu. Elsa havucu tak diye kolayca ikiye böldü. Yarısını Sven'e verdi, öteki yarısını kendisi yedi. Sven havucu hemen yedi ve Elsa'ya burnunu sürttü. Elsa gülerek onu okşadı. Elsa bundan sonra havuçlarını hep Sven ile paylaştı.
```

**Hakem bulguları (8):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa buzdan sarayının önünde oturuyordu"
   - Cümle 2: «Kraliçe Elsa buzdan sarayının önünde oturuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, hikayede işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa buzdan sarayının"
   - Cümle 2: «Kraliçe Elsa buzdan sarayının önünde oturuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "kendi yetiştirdiği tek bir havuç"
   - Cümle 4: «Elsa da acıkmıştı ama sepetinde kendi yetiştirdiği tek bir havuç vardı.»
   - Açıklama: Kartta Elsa'nın sebze yetiştirdiğine dair bir özellik ya da yetenek yok.
4. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "sepetinde kendi yetiştirdiği tek bir havuç"
   - Cümle 4: «Elsa da acıkmıştı ama sepetinde kendi yetiştirdiği tek bir havuç vardı.»
   - Açıklama: Kartta Elsa'nın havuç yetiştirdiğine dair bilgi yok; figüre yabancı bir etkinlik ekleniyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "sepetinde kendi yetiştirdiği tek bir havuç vardı"
   - Cümle 4: «Elsa da acıkmıştı ama sepetinde kendi yetiştirdiği tek bir havuç vardı.»
   - Açıklama: Tek havuç sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kendi yetiştirdiği tek bir havuç"
   - Cümle 4: «Elsa da acıkmıştı ama sepetinde kendi yetiştirdiği tek bir havuç vardı.»
   - Açıklama: Havucun Elsa'nın yetiştirdiği olması olayda hiçbir işe yaramayan ayrıntı.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "soğukta kalmış ve kırılgan olmuştu"
   - Cümle 7: «Havuç soğukta kalmış ve kırılgan olmuştu.»
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki çocuk bilmez.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve kırılgan olmuştu"
   - Cümle 7: «Havuç soğukta kalmış ve kırılgan olmuştu.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0023` birebir aynı, `@degisim: takvim -> havuç` (tutuyorsan), ardından `@onarim: 6b7f53c11e96ceb13f862a250aead10f86bde3dc`, sonra gövde.

### Hikâye 9: tohum elsa-0024 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0024
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'börek', fiil 'dayamak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: buzdan kaydırak yumuşak kumda hep yana düştü | kaydırağı büyük bir kayaya dayadı
@tohum: elsa-0024
@degisim: börek -> taş
Kıyıda hafif bir rüzgar esiyordu. Elsa limanın önünde buzdan süslü bir kaydırak yapmıştı. Ama kum çok yumuşaktı ve kaydırak hep yana düştü. Elsa bu kaydıraktan küçük taşlar yuvarlamak istiyordu. Çevresine baktı ve kumun ucunda büyük bir kaya gördü. Kaydırağı kaldırdı ve yavaşça kayaya dayadı. Bu kez kaydırak hiç düşmedi. Elsa kumdan yuvarlak taşlar topladı. İlk taşı kaydırağın tepesine koydu ve bıraktı. Taş hızla kaydı ve kumda yuvarlandı. Elsa güldü ve ikinci taşı bıraktı. Bu taş daha da uzağa gitti. Elsa çok sevindi, çünkü oyununu yeniden kurmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumun ucunda büyük bir kaya"
   - Cümle 5: «Çevresine baktı ve kumun ucunda büyük bir kaya gördü.»
   - Açıklama: Kumun ucu olmaz; 'kumsalın ucunda' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0024` birebir aynı, `@degisim: börek -> taş` (tutuyorsan), ardından `@onarim: 88635a48879a67059fbde1df3e3a304212971211`, sonra gövde.

### Hikâye 10: tohum elsa-0025 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0025
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'bez', fiil 'kalkmak', sıfat 'paslı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: buzdan geminin yelkeni yoktu ve gemi gitmedi | cebindeki bezi geminin direğine bağladı
@tohum: elsa-0025
@degisim: paslı -> beyaz
Elsa karlı dağda gemi oyunu oynuyordu. Buzdan direği olan küçük bir gemi yapmıştı. Ama geminin yelkeni yoktu ve rüzgar gemiyi hiç götürmedi. Elsa gemisinin karın üstünde kaymasını istiyordu. Biraz düşündü ve cebinden beyaz bir bez çıkardı. Bezi geminin direğine sıkıca bağladı. Rüzgar esti ve bez yelken gibi şişti. Küçük gemi düz karın üstünde yavaşça kaymaya başladı. Elsa ayağa kalktı ve gemisinin arkasından koştu. Gemi karda uzun bir iz bıraktı. Elsa gemisini tuttu ve yeniden rüzgara bıraktı. Elsa gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Buzdan direği olan küçük"
   - Cümle 2: «Buzdan direği olan küçük bir gemi yapmıştı.»
   - Açıklama: Tamlama belirsiz; buzdan olanın gemi mi direk mi olduğu anlaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0025` birebir aynı, `@degisim: paslı -> beyaz` (tutuyorsan), ardından `@onarim: d411fe9ce6ad950c0497c18a2257e3ee768c029f`, sonra gövde.

### Hikâye 11: tohum elsa-0026 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Kristoff
@tohum: elsa-0026
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: sırayla oynamak
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çim', fiil 'beğenmek', sıfat 'sağlıklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | Kristoff
@plan: ikisi de topa hep aynı anda vurmak istedi | buzdan kale yapıp sırayla atmayı önerdi
@tohum: elsa-0026
@degisim: sağlıklı -> yeşil
Kuşlar neşeyle ötüyordu. Elsa ile Kristoff sarayın önündeki yeşil çimlerde top oynuyordu. Ama ikisi de topa hep aynı anda vurmak istedi ve oyun durdu. Elsa biraz düşündü. Sonra elinden buz çıkardı ve çimlerin ucuna küçük bir kale yaptı. "Sırayla atalım, Kristoff. Önce sen at," dedi Elsa. Kristoff topa vurdu ve top kaleye girdi. Elsa bunu çok beğendi ve el çırptı. Sonra sıra Elsa'ya geldi. Onun topu da kalenin tam ortasına girdi. "Sırayla oynamak çok eğlenceli!" dedi Kristoff. İkisi sırayla birkaç kez daha attı. Elsa bundan sonra her oyunda sırayla oynadı.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "sarayın önündeki yeşil çimlerde"
   - Cümle 2: «Elsa ile Kristoff sarayın önündeki yeşil çimlerde top oynuyordu.»
   - Açıklama: Şato tarifi büyük salonlar ve avlu diyor; sarayın önündeki yeşil çimler bu tarifin dışında kalabilir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çimlerin ucuna küçük bir kale"
   - Cümle 5: «Sonra elinden buz çıkardı ve çimlerin ucuna küçük bir kale yaptı.»
   - Açıklama: Çimlerin 'ucu' olmaz; 'kenarına' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0026` birebir aynı, `@degisim: sağlıklı -> yeşil` (tutuyorsan), ardından `@onarim: 0a4f2b7800515f38b5d8f5fdcb51e109415ea86b`, sonra gövde.

### Hikâye 12: tohum elsa-0028 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0028
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'zeytin', fiil 'güvenmek', sıfat 'pembe'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: ren geyiği karlı bir çukura düştü ve çıkamadı | çukurun içine buzdan merdiven yaptı
@tohum: elsa-0028
@degisim: zeytin -> kar
Bir sabah dağda gökyüzü pembeydi. Elsa sarayın önünde yürürken bir ses duydu. Sven karlı bir çukura düşmüştü ve kar yumuşak olduğu için çıkamıyordu. Sven başını kaldırdı ve üzgün bir ses çıkardı. Elsa çukurun kenarına geldi ve elinden buz çıkardı. Çukurun içine buzdan geniş bir merdiven yaptı. Sven önce merdivene baktı ve durdu. Elsa ona elini uzattı ve gülümsedi. Sven Elsa'ya güvendi ve ilk basamağa bastı. Adım adım yukarı çıktı ve çukurdan kurtuldu. Sonra başını Elsa'nın eline sürttü. Sven bundan sonra karlı yerlerde hep yavaş yürüdü.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Sven karlı bir çukura düşmüştü"
   - Cümle 3: «Sven karlı bir çukura düşmüştü ve kar yumuşak olduğu için çıkamıyordu.»
   - Açıklama: Çukura düşüp mahsur kalan ve üzgün ses çıkaran hayvan küçük çocuk için endişe verici olabilir.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sven bundan sonra karlı yerlerde hep yavaş yürüdü"
   - Cümle 12: «Sven bundan sonra karlı yerlerde hep yavaş yürüdü.»
   - Açıklama: Sven'in hızlı yürüdüğü için düştüğü hiç söylenmediğinden son ders yaşanan olaydan çıkmıyor.
   - Açıklama: Sven hızlı yürüdüğü için düşmedi; son ders olaydan çıkmıyor ve sıcak bir kapanış vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0028` birebir aynı, `@degisim: zeytin -> kar` (tutuyorsan), ardından `@onarim: 04a7643baf60f387530683e391ee3659e44328a7`, sonra gövde.
