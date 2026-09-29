# Editör görevi (onarım): Elsa, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0008 (deneme 2 -> 3)

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
@plan: dağda tıkır tıkır garip bir ses geldi | dökülen küpleri gördü ve deliği buzla kapattı
@tohum: elsa-0008
@degisim: meşgul -> hızlı
Bir sabah Elsa dağda, sarayının yanında yürüyordu. Birden yukarıdan tıkır tıkır garip bir ses geldi. Ses hiç durmadı ve Elsa merakla o yöne yürüdü. Orada Kristoff kızağına buz küpleri yüklüyordu. Kristoff çok hızlı çalışıyordu ve arkasına hiç bakmıyordu. Kızağın arkasında küçük bir delik vardı. Küpler bu delikten tek tek yere dökülüyordu. Küpler taşlara düşünce tıkır tıkır ses çıkarıyordu. Garip ses buradan geliyordu. Elsa hemen deliği ince bir buzla kapattı. Artık hiçbir küp dökülmedi ve ses de durdu. Kristoff dönünce küpleri topladı ve Elsa'ya teşekkür etti. Elsa çok sevindi, çünkü sesi bulmuş ve durdurmuştu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "deliği buzla kapattı"
   - Cümle 0 (plan satırı): «dağda tıkır tıkır garip bir ses geldi | dökülen küpleri gördü ve deliği buzla kapattı»
   - Açıklama: Plan deliğin buzla kapatıldığını söylüyor ama gövdede bu olay yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0008` birebir aynı, `@degisim: meşgul -> hızlı` (tutuyorsan), ardından `@onarim: 89b02fb8c57179bc6413bc8b0d7f91d23a3a8511`, sonra gövde.

### Hikâye 2: tohum elsa-0012 (deneme 3 -> 4)

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
Bir sabah Elsa dağda, sarayının önünde buzdan küçük bir çiçek yaptı. Çiçeğin sapına kırmızı bir fiyonk bağlamak istedi. Ama fiyonk bağlamayı bilmiyordu ve kurdele hep açılıyordu. Kristoff biraz ileride kızağını dolduruyordu. Elsa önce çekingen çekingen Kristoff'a baktı. Sonra Kristoff'un yanına yürüdü. "Kristoff, bana fiyonk bağlamayı öğretir misin?" diye sordu Elsa. "Tabii, çok kolay," dedi Kristoff. Kristoff her adımı yavaşça gösterdi. Elsa da iki halka yaptı ve onları sıkıca bağladı. Bu kez kurdele hiç açılmadı. "Teşekkürler, Kristoff, bu fiyonklu çiçek de senin!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kristoff her adımı yavaşça gösterdi"
   - Cümle 9: «Kristoff her adımı yavaşça gösterdi.»
   - Açıklama: Bir işin 'adımı' mecazlı ve soyut bir kullanım, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0012` birebir aynı, `@degisim: okumak -> bağlamak` (tutuyorsan), ardından `@onarim: b578a9a684efc91df6eb25c329aba539ba757fd1`, sonra gövde.

### Hikâye 3: tohum elsa-0014 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar kardan geminin kağıt bayrağını uçurdu | buzdan minicik bir bayrak yapıp direğe astı
@tohum: elsa-0014
@degisim: ceviz -> bayrak
Rüzgar dağda sert sert esiyordu. Elsa sarayın önünde gemi oyunu oynuyordu. Ama rüzgar kardan gemisinin kağıt bayrağını alıp uzağa götürdü. Bayrak çok uzağa uçtu ve kayboldu. Elsa bayrağı olmayan gemisine baktı ve üzüldü. Sonra biraz düşündü. Elsa elini açtı ve buzdan minicik bir bayrak yaptı. Bayrağı geminin direğine sıkıca astı. Rüzgar yine esti ama yeni bayrak hiç uçmadı. Elsa gemisine bir daha baktı ve güldü. Elsa çok sevindi, çünkü gemisinin yeniden bir bayrağı vardı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bayrak çok uzağa uçtu"
   - Cümle 4: «Bayrak çok uzağa uçtu ve kayboldu.»
   - Açıklama: Bir önceki cümlede bayrağın uzağa götürüldüğü söylenmişti; tekrar gereksiz.
   - Açıklama: Bayrağın uzağa gittiği bir önceki cümlede söylenmişti; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0014` birebir aynı, `@degisim: ceviz -> bayrak` (tutuyorsan), ardından `@onarim: d67e729944eab1290673ddbb6812f97af389e837`, sonra gövde.

### Hikâye 4: tohum elsa-0017 (deneme 3 -> 4)

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
Elsa limanda ahşap sandalyesine oturmuş, denizi seyrediyordu. Kristoff uzun süre kızağını yüklemişti ve çok yorgundu. Ama kıyıdaki taşlar ıslaktı ve oturacak kuru bir yer yoktu. Elsa hemen sandalyesinden kalktı. "Kristoff, gel, bu sandalyeye sen otur," dedi Elsa. "Ama bu sandalye senin," dedi Kristoff. "Sen çok yorgunsun, kraliçe olarak sandalyemi sana veriyorum," dedi Elsa. Kristoff teşekkür etti ve sandalyeye oturdu. Elsa da sandalyenin yanında durdu. İkisi birlikte denizdeki küçük dalgalara baktı. Biraz sonra Kristoff dinlendi ve kalktı. Sonra Elsa ile Kristoff kızağı birlikte mutlu mutlu hazırladı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kızağı birlikte mutlu mutlu hazırladı"
   - Cümle 12: «Sonra Elsa ile Kristoff kızağı birlikte mutlu mutlu hazırladı.»
   - Açıklama: Kaybolan kızak bulunmadan son cümlede hazırlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0017` birebir aynı, ardından `@onarim: 42c28967c896592dec33c0937f0ffc9b8690e402`, sonra gövde.

### Hikâye 5: tohum elsa-0019 (deneme 3 -> 4)

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
@plan: arkadaşı sepetini unutmuştu ve yiyeceği yoktu | şeftaliyi ona verdi ve keki ikiye böldü
@tohum: elsa-0019
@degisim: değişmek -> paylaşmak
Bir sabah Elsa dağda, sarayının önünde sepetini açtı. Sepette bir şeftali ile çilekli bir kek vardı. O sırada Olaf geldi ama sepetini sarayda unutmuştu. Olaf sepete baktı ve sessizce bekledi. Elsa şeftaliyi hemen Olaf'a uzattı. Sonra çilekli keki elleriyle ikiye böldü. Elsa elini salladı ve buzdan iki küçük tabak yaptı. Kekin yarısını Olaf'ın tabağına koydu. Olaf kocaman gülümsedi ve Elsa'ya sarıldı. İkisi yan yana oturdu ve karlı dağı mutlu mutlu seyretti. Elsa bundan sonra yiyeceklerini hep Olaf ile paylaştı.
```

**Hakem bulguları (3):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "arkadaşı sepetini unutmuştu ve yiyeceği yoktu"
   - Cümle 0 (plan satırı): «arkadaşı sepetini unutmuştu ve yiyeceği yoktu | şeftaliyi ona verdi ve keki ikiye böldü»
   - Açıklama: Karttaki kardan adam Olaf'ın yiyeceğe ihtiyaç duyup kek yemesi dizideki tanınan Olaf'a uymuyor olabilir.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sepetini sarayda unutmuştu"
   - Cümle 3: «O sırada Olaf geldi ama sepetini sarayda unutmuştu.»
   - Açıklama: Elsa ve Olaf zaten sarayın önünde olduğu için sepeti unutmak sorun olamaz; bu, sahneyle çelişiyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "buzdan iki küçük tabak yaptı"
   - Cümle 7: «Elsa elini salladı ve buzdan iki küçük tabak yaptı.»
   - Açıklama: Tabak yapma ve kekin tabağa konması sebebe yönelmeyen ek adımlar olup çözümü iki adımın ötesine taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0019` birebir aynı, `@degisim: değişmek -> paylaşmak` (tutuyorsan), ardından `@onarim: 232b981e09566044ec402b9e92b6a7213c7b145e`, sonra gövde.

### Hikâye 6: tohum elsa-0020 (deneme 3 -> 4)

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
Rüzgar dağda sert sert esiyordu. Sven, Elsa'nın sarayına girip dinlenmek istedi. Ama kapıya giden yol buzluydu ve Sven her adımda kaydı. Sven kapıya ulaşamadı ve geri çekildi. Elsa kapıdan onu gördü. "Üzülme, Sven, sana yardım edeceğim," dedi Elsa. Elsa'nın yepyeni kraliçe pelerini çok uzundu. Elsa pelerinini çıkardı ve buzlu yolun üstüne serdi. Sven pelerine bastı ve bu kez hiç kaymadı. Yavaş yavaş yürüdü ve kapıya ulaştı. Elsa sarayda ona bir havuç verdi. Sven havucu mutlu mutlu yedi ve Elsa da sevinçle güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa'nın yepyeni kraliçe pelerini çok uzundu"
   - Cümle 7: «Elsa'nın yepyeni kraliçe pelerini çok uzundu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız pelerin sıfatı olarak geçiyor; kartın özellik satırındaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0020` birebir aynı, `@degisim: bileklik -> havuç` (tutuyorsan), ardından `@onarim: e8bf0bf1a4e6d92c69b32535a4fd67860d8caec5`, sonra gövde.

### Hikâye 7: tohum elsa-0023 (deneme 3 -> 4)

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
Dağda soğuk bir rüzgar esiyordu. Elsa ile Sven buzdan sarayın önünde oturuyordu. İkisi de çok acıkmıştı ama sepette yetiştirilmiş tek bir havuç vardı. Sven havuca baktı ve kulaklarını oynattı. "Sven, ben kraliçeyim ve yanımda kimse aç kalmaz," dedi Elsa. Soğuk havuç kırılgandı ve Elsa onu tak diye ikiye böldü. Yarısını Sven'e verdi, öteki yarısını kendisi yedi. Sven kendi yarısını hemen bitirdi ve Elsa'ya burnunu sürttü. Elsa gülerek onu okşadı. Elsa bundan sonra havuçlarını hep Sven ile paylaştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ikisi de açtı ama"
   - Cümle 0 (plan satırı): «ikisi de açtı ama yalnız bir havuç vardı | kırılgan havucu ikiye böldü ve geyikle paylaştı»
   - Açıklama: 'Açtı' yanlış kelime; 'acıktı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sepette yetiştirilmiş tek bir havuç"
   - Cümle 3: «İkisi de çok acıkmıştı ama sepette yetiştirilmiş tek bir havuç vardı.»
   - Açıklama: 'Yetiştirilmiş' burada anlamsız ve yanlış kullanılmış.
   - Açıklama: 'Yetiştirilmiş' burada yanlış ve gereksiz; havuç sepette yetiştirilmiş gibi okunuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sepette yetiştirilmiş tek bir havuç vardı"
   - Cümle 3: «İkisi de çok acıkmıştı ama sepette yetiştirilmiş tek bir havuç vardı.»
   - Açıklama: Neden yalnız bir havuç olduğu söylenmiyor ve yarım havucun açlığı gidermesi de akla yatkın değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ben kraliçeyim ve yanımda kimse aç kalmaz"
   - Cümle 5: «"Sven, ben kraliçeyim ve yanımda kimse aç kalmaz," dedi Elsa.»
   - Açıklama: Kraliçe özelliği karttaki gibi kız kardeşi korumak için değil süs olarak geçiyor; çözüm (havucu bölmek) ona dayanmıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Soğuk havuç kırılgandı"
   - Cümle 6: «Soğuk havuç kırılgandı ve Elsa onu tak diye ikiye böldü.»
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0023` birebir aynı, `@degisim: takvim -> havuç` (tutuyorsan), ardından `@onarim: 169403ce335333842ed56a96bddff97e3fe4cf68`, sonra gövde.

### Hikâye 8: tohum elsa-0025 (deneme 2 -> 3)

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
Elsa karlı dağda gemi oyunu oynuyordu. Buzdan küçük bir gemi yapmıştı ve geminin bir direği vardı. Ama geminin yelkeni yoktu ve rüzgar gemiyi hiç götürmedi. Elsa gemisinin karın üstünde kaymasını istiyordu. Biraz düşündü ve cebinden beyaz bir bez çıkardı. Bezi geminin direğine sıkıca bağladı. Rüzgar esti ve bez yelken gibi şişti. Küçük gemi düz karın üstünde yavaşça kaymaya başladı. Elsa ayağa kalktı ve gemisinin arkasından koştu. Gemi karda uzun bir iz bıraktı. Elsa gemisini tuttu ve yeniden rüzgara bıraktı. Elsa gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "cebinden beyaz bir bez çıkardı"
   - Cümle 5: «Biraz düşündü ve cebinden beyaz bir bez çıkardı.»
   - Açıklama: Çözümü getiren bez daha önce kurulmadan cepten sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0025` birebir aynı, `@degisim: paslı -> beyaz` (tutuyorsan), ardından `@onarim: ec744b70b3d10abb3b5552fdbafa0d900800b5d9`, sonra gövde.

### Hikâye 9: tohum elsa-0027 (deneme 2 -> 3)

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
Dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Elsa bir kova sabunlu suya ince bir dal batırıp baloncuk yapıyordu. Olaf da oynamak istedi ama karın içinde başka dal yoktu. "Elsa, ben ne yapacağım?" diye sordu Olaf. Elsa bir kraliçeydi ve kimsenin üzülmesini istemezdi. Dalı dikkatle ikiye böldü. Dal küçüldü ama iki parça da yeterince uzundu. "Olaf, bu parça senin," dedi Elsa. İkisi dallarını suya batırıp üfledi. Havada bir sürü parlak baloncuk uçtu. Olaf onların arasında zıpladı ve güldü. Elsa ile Olaf kovanın başında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve kimsenin üzülmesini istemezdi"
   - Cümle 5: «Elsa bir kraliçeydi ve kimsenin üzülmesini istemezdi.»
   - Açıklama: Kraliçe özelliği karttaki gibi kız kardeşi korumak için kullanılmıyor; çözüm (dalı bölmek) ona dayanmıyor.
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşi korumak; özellik sorunu çözmede işe yaramıyor, yalnız anılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dal küçüldü ama iki"
   - Cümle 7: «Dal küçüldü ama iki parça da yeterince uzundu.»
   - Açıklama: İkiye bölünen dal için 'küçüldü' doğru anlamda değil; 'parçalar kısaydı' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0027` birebir aynı, `@degisim: yatak -> kova` (tutuyorsan), ardından `@onarim: ba33e9535a1f8e181e9acd3f41a74f21b9433e96`, sonra gövde.

### Hikâye 10: tohum elsa-0028 (deneme 2 -> 3)

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
@plan: geyik hızlı koştu, çukura kaydı ve çıkamadı | çukurun içine buzdan merdiven yaptı
@tohum: elsa-0028
@degisim: zeytin -> kar
Bir sabah dağda gökyüzü pembeydi. Elsa sarayın önünde yürürken bir ses duydu. Sven karda hızlı koşmuş ve karlı bir çukura kaymıştı. Çukurdaki kar yumuşaktı ve Sven'in ayakları hep kayıyordu. Sven başını kaldırdı ve Elsa'ya baktı. Elsa çukurun kenarına geldi ve elinden buz çıkardı. Çukurun içine buzdan geniş bir merdiven yaptı. Sven önce merdivene baktı ve durdu. Elsa ona elini uzattı ve gülümsedi. Sven Elsa'ya güvendi ve ilk basamağa bastı. Adım adım yukarı çıktı ve çukurdan kurtuldu. Sonra başını Elsa'nın eline sürttü. Sven bundan sonra karlı yerlerde hep yavaş yürüdü.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çukurun içine buzdan geniş bir merdiven yaptı"
   - Cümle 7: «Çukurun içine buzdan geniş bir merdiven yaptı.»
   - Açıklama: Sven'in ayakları karda kayarken buzdan merdiven daha da kaygan olmalı, yine de Sven rahatça çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0028` birebir aynı, `@degisim: zeytin -> kar` (tutuyorsan), ardından `@onarim: 98dac1a6da3bc8edf1684d57f7f2cdcd51788594`, sonra gövde.

### Hikâye 11: tohum elsa-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0029
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'demet', fiil 'zıplamak', sıfat 'turuncu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: ikisi hep aynı anda zıpladı ve kimin kazandığını göremediler | sırayla zıplamayı ve havuç koymayı önerdi
@tohum: elsa-0029
Rüzgar ağaçların arasında hafifçe esiyordu. Elsa ile Kristoff karlı ormanda zıplama oyunu oynuyordu. Ama ikisi hep aynı anda zıpladı ve kimin daha uzağa gittiğini göremediler. Elsa bir kraliçeydi ve yeni bir kural koydu. "Sırayla zıplayalım, Kristoff. Sonra da yere birer havuç koyalım," dedi Elsa. Kristoff çantasından bir demet turuncu havuç çıkardı. Önce Kristoff zıpladı ve durduğu yere bir havuç koydu. Sonra Elsa zıpladı. Elsa'nın havucu biraz daha ileride durdu. Birkaç kez daha sırayla zıpladılar. İkisi de çok sevindi, çünkü artık kimin daha uzağa zıpladığını görebiliyorlardı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ikisi hep aynı anda zıpladı ve kimin daha uzağa gittiğini göremediler"
   - Cümle 3: «Ama ikisi hep aynı anda zıpladı ve kimin daha uzağa gittiğini göremediler.»
   - Açıklama: Aynı cümlede 'ikisi' için tekil 'zıpladı' ile çoğul 'göremediler' karışık kullanılmış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi hep aynı anda zıpladı ve kimin daha uzağa gittiğini göremediler"
   - Cümle 3: «Ama ikisi hep aynı anda zıpladı ve kimin daha uzağa gittiğini göremediler.»
   - Açıklama: Yan yana aynı anda zıplamak kimin daha uzağa gittiğini görmeyi engellemez; asıl sebep düşülen yerin işaretlenmemesi, sebep akla yatkın değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir kural koydu"
   - Cümle 4: «Elsa bir kraliçeydi ve yeni bir kural koydu.»
   - Açıklama: 'Kural koymak' soyut bir kavram, küçük çocuğa uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve yeni bir kural koydu"
   - Cümle 4: «Elsa bir kraliçeydi ve yeni bir kural koydu.»
   - Açıklama: Kraliçe özelliği karttaki gibi kız kardeşi korumak için kullanılmıyor, yalnız kural koyma gerekçesi olarak ekleniyor.
   - Açıklama: Tohumdaki özellik 'kraliçedir; kız kardeşini korur' iken kraliçelik yalnız oyun kuralı koymak için anılıyor, karttaki gibi kullanılmıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "havucu biraz daha ileride durdu"
   - Cümle 10: «Elsa'nın havucu biraz daha ileride durdu.»
   - Açıklama: Havuç hareket etmediği için 'durdu' yanlış; 'duruyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0029` birebir aynı, ardından `@onarim: 8fbcc9e655585b829fe24dacdef4db10ff4e8eb2`, sonra gövde.

### Hikâye 12: tohum elsa-0033 (deneme 2 -> 3)

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
Karlı ormanda Elsa ile Anna yan yana yürüyor ve şekerleme yiyordu. Birden Anna'nın saçı alçak bir dala takıldı. Anna başını çevirdi ama saçı daldan çıkmadı. Anna saçını hızla çekmek istedi. Elsa bir kraliçeydi ve kardeşini korumak için onun elini yavaşça tuttu. Sonra saç tellerini daldan tek tek ayırdı. Sonunda Anna'nın saçı kurtuldu. Anna sevinçle Elsa'ya sarıldı. Teşekkür için son şekerlemesini Elsa'ya verdi. Elsa tatlı hediyeyi aldı ve kardeşine gülümsedi. Anna çok mutluydu, çünkü Elsa ona yardım etmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Teşekkür için son şekerlemesini"
   - Cümle 9: «Teşekkür için son şekerlemesini Elsa'ya verdi.»
   - Açıklama: 'Teşekkür için' eksik bir yapı; 'Teşekkür etmek için' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0033` birebir aynı, `@degisim: sevecen -> tatlı` (tutuyorsan), ardından `@onarim: 05308262eae1a1bcbc268a9b99815df2b0f9583b`, sonra gövde.
