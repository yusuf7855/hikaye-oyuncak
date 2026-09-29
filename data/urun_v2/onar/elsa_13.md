# Editör görevi (onarım): Elsa, onarım partisi 13

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar13.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar13.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0008 (deneme 4 -> 5)

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
Bir sabah Elsa dağda, sarayının önünde karla bir kule yapıyordu. Birden yukarıdan buz küpleri döküldü ve kule yıkıldı. Elsa küpler nereden geldi diye çok merak etti. Elsa karda küçük izler gördü ve yokuşu çıktı. Orada Kristoff kızağına buz küpleri yüklüyordu. Kristoff çok hızlı çalışıyordu ve arkasına hiç bakmıyordu. Kızağın altında küçük bir delik vardı. Küpler bu delikten tek tek düşüyor ve aşağı kayıyordu. Elsa elinden buz çıkardı ve deliği sıkıca kapattı. Artık hiçbir küp dökülmedi. Kristoff dönünce buzlu deliği gördü ve Elsa'ya teşekkür etti. Elsa geri döndü ve kulesini yeniden yaptı. Elsa çok sevindi, çünkü düşen küpleri ve deliği bulmuştu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa küpler nereden geldi diye"
   - Cümle 3: «Elsa küpler nereden geldi diye çok merak etti.»
   - Açıklama: İç soru tırnaksız ve eksiz kurulmuş; 'küplerin nereden geldiğini merak etti' olmalı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Elsa küpler nereden geldi diye"
   - Cümle 3: «Elsa küpler nereden geldi diye çok merak etti.»
   - Açıklama: İç düşünce tırnaksız ve dolaylı anlatıma çevrilmeden yazılmış; 'küplerin nereden geldiğini' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "düşen küpleri ve deliği bulmuştu"
   - Cümle 13: «Elsa çok sevindi, çünkü düşen küpleri ve deliği bulmuştu.»
   - Açıklama: Düşen küpler bulunmadı; 'bulmak' fiili burada anlamca yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0008` birebir aynı, `@degisim: meşgul -> hızlı` (tutuyorsan), ardından `@onarim: 3cd286c69ad42a88d47d42ff5457c1902bbe095d`, sonra gövde.

### Hikâye 2: tohum elsa-0012 (deneme 5 -> 6)

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
@plan: kurdele hep açılıyordu çünkü fiyonk bağlamayı bilmiyordu | arkadaşından yardım istedi ve fiyonk bağlamayı öğrendi
@tohum: elsa-0012
@degisim: okumak -> bağlamak
Bir sabah Elsa dağda, sarayının önünde buzdan küçük bir çiçek yaptı. Çiçeğin sapına kırmızı bir fiyonk bağlamak istedi. Ama fiyonk bağlamayı bilmiyordu ve kurdele hep açılıyordu. Kristoff biraz ileride kızağını dolduruyordu. Elsa biraz çekingendi ve önce uzaktan Kristoff'a baktı. Sonra Kristoff'un yanına yürüdü. "Kristoff, bana fiyonk bağlamayı öğretir misin?" diye sordu Elsa. "Tabii, çok kolay," dedi Kristoff. Kristoff yavaşça bir fiyonk bağladı ve açtı. Elsa da iki halka yaptı ve onları sıkıca bağladı. Bu kez kurdele hiç açılmadı. "Teşekkürler, Kristoff, bu fiyonklu çiçek de senin!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "buzdan küçük bir çiçek yaptı"
   - Cümle 1: «Bir sabah Elsa dağda, sarayının önünde buzdan küçük bir çiçek yaptı.»
   - Açıklama: Tohumdaki buz özelliği yalnız başta geçiyor, fiyonk sorununun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0012` birebir aynı, `@degisim: okumak -> bağlamak` (tutuyorsan), ardından `@onarim: da087ed358b7add38a94c4ea18b56383591ea603`, sonra gövde.

### Hikâye 3: tohum elsa-0020 (deneme 5 -> 6)

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
Rüzgar dağda sert sert esiyordu. Sven, Elsa'nın sarayına girip dinlenmek istedi. Ama kapıya giden yol buzluydu ve Sven her adımda kaydı. Sven kapıya ulaşamadı ve geri çekildi. Elsa kapıdan onu gördü. "Üzülme, Sven, sana yardım edeceğim," dedi Elsa. Elsa'nın omzunda yepyeni ve uzun bir kraliçe pelerini vardı. Elsa pelerinini çıkardı ve buzlu yolun üstüne serdi. Sven pelerine bastı ve bu kez hiç kaymadı. Yavaş yavaş yürüdü ve kapıya ulaştı. Elsa sarayda ona bir havuç verdi. Sven havucu mutlu mutlu yedi ve Elsa da sevinçle güldü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa'nın omzunda yepyeni ve uzun bir kraliçe pelerini vardı"
   - Cümle 7: «Elsa'nın omzunda yepyeni ve uzun bir kraliçe pelerini vardı.»
   - Açıklama: Pelerin tam çözüm gerekince sebepsizce kuruluyor ve 'yepyeni' ayrıntısı hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0020` birebir aynı, `@degisim: bileklik -> havuç` (tutuyorsan), ardından `@onarim: 06ae376d56e196da9c43509fdcf9658057b98859`, sonra gövde.

### Hikâye 4: tohum elsa-0023 (deneme 5 -> 6)

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
@plan: ikisi de acıkmıştı ama sepette tek havuç vardı | kırılgan havucu ikiye böldü ve geyikle paylaştı
@tohum: elsa-0023
@degisim: takvim -> havuç
Dağda soğuk bir rüzgar esiyordu. Elsa ile Sven sarayın önünde oturuyordu ve ikisi de biraz acıkmıştı. Ama sepette tek havuç kalmıştı, çünkü öteki havuçları sabah yemişlerdi. Sven havucu burnuyla kraliçeye doğru itti. "Sven, bu havucu ikimiz için yetiştireceğim," dedi Elsa. Soğuk havuç kırılgandı ve Elsa onu kolayca ikiye kırdı. Yarısını Sven'e verdi, öteki yarısını kendisi yedi. Sven kendi yarısını hemen bitirdi ve Elsa'ya burnunu sürttü. Elsa gülerek onu okşadı. Elsa bundan sonra havuçlarını hep Sven ile paylaştı.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven havucu burnuyla kraliçeye doğru itti"
   - Cümle 4: «Sven havucu burnuyla kraliçeye doğru itti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir ad olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "havucu burnuyla kraliçeye doğru itti"
   - Cümle 4: «Sven havucu burnuyla kraliçeye doğru itti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir hitap olarak geçiyor, havuç paylaşımında işe yaramıyor ve kız kardeşi koruma ile ilgisi yok.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu havucu ikimiz için yetiştireceğim"
   - Cümle 5: «"Sven, bu havucu ikimiz için yetiştireceğim," dedi Elsa.»
   - Açıklama: 'Yetiştirmek' burada yanlış anlamda; havucu paylaştırmak ya da yetirmek kastediliyor.
   - Açıklama: Havuç yetiştirilmiyor, bölünüyor; 'böleceğim' olmalı.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bu havucu ikimiz için yetiştireceğim"
   - Cümle 5: «"Sven, bu havucu ikimiz için yetiştireceğim," dedi Elsa.»
   - Açıklama: Elsa havucu yetiştireceğini söylüyor ama hemen ardından eldeki havucu kırıp paylaşıyor; söz eylemle çelişiyor ve anlamsız.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Soğuk havuç kırılgandı"
   - Cümle 6: «Soğuk havuç kırılgandı ve Elsa onu kolayca ikiye kırdı.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0023` birebir aynı, `@degisim: takvim -> havuç` (tutuyorsan), ardından `@onarim: e18066b3c481ffea78118ccd9e4e627c8471f956`, sonra gövde.

### Hikâye 5: tohum elsa-0027 (deneme 4 -> 5)

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
Dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Elsa bir kova sabunlu suya ince bir dal batırıp baloncuk yapıyordu. Olaf da oynamak istedi ama karın içinde başka dal yoktu. "Elsa, ben ne yapacağım?" diye sordu Olaf. Kraliçe Elsa dalı dikkatle ikiye böldü. İki parça da baloncuk yapmak için yeterince uzundu. "Olaf, bu parça senin," dedi Elsa. İkisi dallarını suya batırıp üfledi. Parlak baloncuklar havada yükseldi ve küçüldü. Olaf onların arasında zıpladı ve güldü. Elsa ile Olaf kovanın başında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karın içinde başka dal"
   - Cümle 3: «Olaf da oynamak istedi ama karın içinde başka dal yoktu.»
   - Açıklama: 'karın içinde' hem 'karda' hem 'midenin içinde' okunabiliyor ve dal için doğal değil; 'karda' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa dalı dikkatle ikiye böldü"
   - Cümle 5: «Kraliçe Elsa dalı dikkatle ikiye böldü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, dalı bölmekte işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0027` birebir aynı, `@degisim: yatak -> kova` (tutuyorsan), ardından `@onarim: 5dc18ac8d142924c9b5b2de849257a1f07763df8`, sonra gövde.

### Hikâye 6: tohum elsa-0033 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0033
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'şekerleme', fiil 'ayırmak', sıfat 'sevecen'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: kardeşinin saçı alçak bir dala takıldı | saç tellerini daldan tek tek ayırdı
@tohum: elsa-0033
@degisim: sevecen -> tatlı
Karlı ormanda Elsa ile Anna yan yana yürüyor ve şekerleme yiyordu. Birden Anna'nın saçı alçak bir dala takıldı. Anna başını çevirdi ama saçı daldan çıkmadı. Anna saçını hızla çekmek istedi. Kraliçe Elsa kardeşini korumak için onun elini yavaşça tuttu. Sonra saç tellerini daldan tek tek ayırdı. Sonunda Anna'nın saçı kurtuldu. Anna sevinçle Elsa'ya sarıldı. Teşekkür etmek için son şekerlemesini Elsa'ya verdi. Elsa tatlı hediyeyi aldı ve kardeşine gülümsedi. Anna çok mutluydu, çünkü Elsa ona yardım etmişti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini korumak"
   - Cümle 5: «Kraliçe Elsa kardeşini korumak için onun elini yavaşça tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0033` birebir aynı, `@degisim: sevecen -> tatlı` (tutuyorsan), ardından `@onarim: f7fc59c919b2ff1bb5712a83bc6197de9fa65872`, sonra gövde.

### Hikâye 7: tohum elsa-0034 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0034
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kabak', fiil 'yakalamak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: rüzgar şapkayı uçurdu ve şapka yolda yuvarlandı | arkadaşını durdurdu, koşup şapkayı ipinden yakaladı
@tohum: elsa-0034
@degisim: kabak -> şapka
Elsa limanda Kristoff ile yürüyordu. Kristoff iki eliyle büyük bir buz kalıbı taşıyordu. Birden güçlü bir rüzgar Kristoff'un şapkasını başından uçurdu. Şapka limanın taş yolunda yuvarlandı. Kristoff ağır buzla şapkanın peşinden gitmek istedi. Kraliçe Elsa onu hemen durdurdu. "Sen burada kal, Kristoff, ben alırım," dedi Elsa. Hemen koştu ve şapkayı incecik ipinden yakaladı. Sonra şapkayı Kristoff'un başına taktı ve ipini sıkıca bağladı. Artık şapka rüzgarda hiç uçmadı. "Teşekkürler, Elsa, çok hızlıydın!" dedi Kristoff. Elsa güldü. İkisi limanda yürümeye mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa onu hemen"
   - Cümle 6: «Kraliçe Elsa onu hemen durdurdu.»
   - Açıklama: Zaten anlatılan Elsa unvanla yeniden tanıtılıyor.
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa onu hemen durdurdu"
   - Cümle 6: «Kraliçe Elsa onu hemen durdurdu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, şapkayı yakalamakta işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen koştu ve şapkayı"
   - Cümle 8: «Hemen koştu ve şapkayı incecik ipinden yakaladı.»
   - Açıklama: Limanda rüzgarda yuvarlanan şapkanın peşinden koşmak çocuğun su kenarında taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0034` birebir aynı, `@degisim: kabak -> şapka` (tutuyorsan), ardından `@onarim: c6c5d4edcb66b9750c344a7d6563713512549fec`, sonra gövde.

### Hikâye 8: tohum elsa-0036 (deneme 3 -> 4)

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
Karlı ormanda Elsa ile Sven kızak oyunu oynuyordu. Sven önde koşuyor, Elsa da arkada neşeyle şarkı söylüyordu. Ama kızak kabarık bir kar yığınına girdi ve durdu. Sven bütün gücüyle çekti ama kızak hiç kıpırdamadı. Sven çok yoruldu. Kraliçe Elsa hemen kızaktan indi ve kızak hafifledi. Sven bu kez kızağı geri çekti. "Sven, yolu değiştirelim, şu yolda kar sert," dedi Elsa. Sven başını salladı ve kızağı o yola çekti. Elsa yeniden kızağa oturdu. Bu yolda kızak kolayca kaydı. Elsa ile Sven ağaçların arasında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen kızaktan"
   - Cümle 6: «Kraliçe Elsa hemen kızaktan indi ve kızak hafifledi.»
   - Açıklama: Elsa hikayenin ortasında unvanıyla ikinci kez tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen kızaktan indi"
   - Cümle 6: «Kraliçe Elsa hemen kızaktan indi ve kızak hafifledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor (kart 'ozellikler').
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kızağın kurtulmasında kraliçelik ya da kardeşi korumanın payı yok.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kraliçe Elsa hemen kızaktan indi"
   - Cümle 6: «Kraliçe Elsa hemen kızaktan indi ve kızak hafifledi.»
   - Açıklama: Çözüm inmek, kızağı geri çekmek ve yol değiştirmek olarak iki adımdan uzun sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0036` birebir aynı, `@degisim: kapı -> kızak` (tutuyorsan), ardından `@onarim: a1797abb5b70ce10b9a215bf6c184ca28c4a199f`, sonra gövde.

### Hikâye 9: tohum elsa-0037 (deneme 3 -> 4)

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
Bir sabah Elsa dağda, buz sarayında oturuyordu. Birden kapıdan garip bir tık tık sesi geldi. Elsa sarayın kraliçesiydi ve sarayı korumak için hemen kapıya gitti. Kapıyı açtı ama dışarıda kimse yoktu. Karın üstünde küçük kahverengi fıstıklar vardı. Elsa başını kaldırdı ve kapının yanındaki büyük ağacı gördü. Rüzgar ağacın dallarını sallıyordu. Bir fıstık daldan düştü ve kapıya çarptı. Tık tık sesi yine geldi. Elsa güldü. Bu eğlenceli sesi düşen fıstıklar yapıyordu. Sonra Elsa fıstıkları topladı ve onlarla karda mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "sarayın kraliçesiydi ve sarayı korumak"
   - Cümle 3: «Elsa sarayın kraliçesiydi ve sarayı korumak için hemen kapıya gitti.»
   - Açıklama: 'Saray' kelimesi art arda gereksiz yere tekrarlanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sarayı korumak için hemen kapıya gitti"
   - Cümle 3: «Elsa sarayın kraliçesiydi ve sarayı korumak için hemen kapıya gitti.»
   - Açıklama: Kartın özellik alanı kız kardeşini korumayı söylüyor; özellik sarayı korumaya kaydırılmış ve sorunu çözmüyor.
   - Açıklama: Kartın özellik alanında Elsa kız kardeşini korur; burada özellik sarayı korumaya çevrilmiş ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0037` birebir aynı, ardından `@onarim: 61d556657c260697f7f5418e68a28fce00dd32f9`, sonra gövde.

### Hikâye 10: tohum elsa-0039 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: karlı bir çalının altından garip bir ses geldi | buzdan bir kürek yapıp karı kazdı ve sesi buldu
@tohum: elsa-0039
Elsa ile Olaf güneşli bir sabah dağda yürüyordu. Birden karlı bir çalının altından tıp tıp diye bir ses geldi. "Bu ses ne?" diye sordu Olaf. Çalının önü kalın karla doluydu ve hiçbir şey görünmüyordu. Elsa elini salladı ve buzdan küçük bir kürek yaptı. Sonra çalının önündeki karı yavaşça kazdı. Çalının altında sararmış, yuvarlak bir yaprak vardı. Çalının dalında küçük bir buz parçası güneşte eriyordu. Eriyen buzdan damlalar tek tek yaprağa düşüyordu. Tıp tıp sesi bu damlalardan geliyordu. "Bu ses bir davul gibi!" dedi Olaf. Sonra Elsa ile Olaf damlaların sesini dinleyip mutlu mutlu güldü.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karı kazdı ve sesi buldu"
   - Cümle 0 (plan satırı): «karlı bir çalının altından garip bir ses geldi | buzdan bir kürek yapıp karı kazdı ve sesi buldu»
   - Açıklama: Ses bulunmaz; sesin nereden geldiğini buldu denmeli.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "karlı bir çalının altından garip bir ses geldi"
   - Cümle 0 (plan satırı): «karlı bir çalının altından garip bir ses geldi | buzdan bir kürek yapıp karı kazdı ve sesi buldu»
   - Açıklama: Garip bir ses gerçek bir sorun değil, çocuğun önemseyeceği bir derdi yok.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Eriyen buzdan damlalar tek tek yaprağa düşüyordu"
   - Cümle 9: «Eriyen buzdan damlalar tek tek yaprağa düşüyordu.»
   - Açıklama: Yaprak kalın karın altındayken damlaların ona düşüp kazıdan önce tıp tıp ses çıkarması çelişkili.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu ses bir davul gibi!"
   - Cümle 11: «"Bu ses bir davul gibi!" dedi Olaf.»
   - Açıklama: Benzetme (mecaz) kullanılmış; D6 mecaz yasağına takılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0039` birebir aynı, ardından `@onarim: f663d882b0bcf7b26b3feac5a132686089f9220c`, sonra gövde.

### Hikâye 11: tohum elsa-0040 (deneme 3 -> 4)

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
Rüzgar esiyordu. Elsa sarayın önünde, geniş bir yerde kızağıyla oynuyordu. Ama halat kızağa sıkı bağlı değildi ve birden kızaktan düştü. Kızak iki büyük taşın yanında durdu ama halat yoktu. Elsa her yere baktı. Sonunda iki taşın arasında halatı gördü. Ama taşların arası çok dardı ve eli oraya girmedi. Elsa parmaklarını oynattı ve buzdan uzun bir çubuk yaptı. Çubuğu taşların arasına soktu ve halatı yavaşça çekti. Halat taşların arasından çıktı. Elsa halatı kızağa yine sıkıca bağladı. Elsa çok sevindi, çünkü halatı kurtarmıştı ve oyununa dönebilirdi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kızak iki büyük taşın yanında durdu ama halat yoktu"
   - Cümle 4: «Kızak iki büyük taşın yanında durdu ama halat yoktu.»
   - Açıklama: Kızaktan düşen halatın nasıl iki taşın dar arasına girdiği açıklanmıyor; sorunun sebebi akla yatkın kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "halatı kızağa yine sıkıca"
   - Cümle 11: «Elsa halatı kızağa yine sıkıca bağladı.»
   - Açıklama: Halat önceden sıkı bağlı değildi; 'yine sıkıca' yanlış anlam veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0040` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 192239053e21ac6814bab03f734f2277019083af`, sonra gövde.

### Hikâye 12: tohum elsa-0041 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: karın altındaki geyiği tanımadı ve ona havuç taktı | ondan özür diledi ve üstündeki karı sildi
@tohum: elsa-0041
@degisim: gül -> havuç
Karlı dağda, sarayın önünde Sven uyuyordu ve üstü karla örtülmüştü. Elsa elinde bir havuçla Sven'i arıyordu ama onu tanımadı. Onu bir kar yığını sandı ve havucu ona burun gibi taktı. Birden yığın sallandı ve karlar yere döküldü. Karın altından Sven'in başı çıktı. Sven artık uyanıktı ve Elsa'ya şaşkın şaşkın bakıyordu. Elsa iyi bir kraliçeydi ve hatasını hemen anladı. "Özür dilerim, Sven, seni tanımadım," dedi Elsa. Elsa Sven'in üstündeki karı elleriyle sildi. Sven havucu yedi ve sevinçle başını salladı. Sonra ikisi karda mutlu mutlu koştular.
```

**Hakem bulguları (5):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "üstü karla örtülmüştü"
   - Cümle 1: «Karlı dağda, sarayın önünde Sven uyuyordu ve üstü karla örtülmüştü.»
   - Açıklama: Sven'in karın altında kalması güvenli kullanım satırındaki hiçbir canlı üşümez ilkesine aykırı bir üşüme riski taşıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "havucu ona burun gibi taktı"
   - Cümle 3: «Onu bir kar yığını sandı ve havucu ona burun gibi taktı.»
   - Açıklama: Uyuyan geyiğe havuç takmak kimseye zarar vermeyen önemsiz bir şaka olayı; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Onu bir kar yığını sandı ve havucu ona burun gibi taktı"
   - Cümle 3: «Onu bir kar yığını sandı ve havucu ona burun gibi taktı.»
   - Açıklama: Sven'i arayan Elsa'nın onu tanımayıp havucu burun diye takması akla yatkın olmayan, saçma bir sorun.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi"
   - Cümle 7: «Elsa iyi bir kraliçeydi ve hatasını hemen anladı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız etiket olarak geçiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve hatasını hemen anladı"
   - Cümle 7: «Elsa iyi bir kraliçeydi ve hatasını hemen anladı.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi (kız kardeşini korumak) kullanılmıyor, yalnız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0041` birebir aynı, `@degisim: gül -> havuç` (tutuyorsan), ardından `@onarim: b5f3c0a9d2906cef94501cf80ea25e17a568a8d4`, sonra gövde.
