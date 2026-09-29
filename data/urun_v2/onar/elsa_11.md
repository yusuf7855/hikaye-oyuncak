# Editör görevi (onarım): Elsa, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0008 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: dağda tıkır tıkır garip bir ses geldi | kızaktaki deliği buldu ve buzla kapattı
@tohum: elsa-0008
@degisim: meşgul -> hızlı
Bir sabah Elsa dağda, sarayının yanında yürüyordu. Birden yukarıdan tıkır tıkır garip bir ses geldi. Ses hiç durmadı ve Elsa merakla o yöne yürüdü. Orada Kristoff kızağına buz küpleri yüklüyordu. Kristoff çok hızlı çalışıyordu ve arkasına hiç bakmıyordu. Kızağın arkasında küçük bir delik vardı. Küpler bu delikten tek tek yere dökülüyordu. Küpler taşlara düşünce tıkır tıkır ses çıkarıyordu. Garip ses buradan geliyordu. Elsa elinden buz çıkardı ve kızaktaki deliği kapattı. Artık hiçbir küp dökülmedi ve ses de durdu. Kristoff dönünce küpleri topladı ve Elsa'ya teşekkür etti. Elsa çok sevindi, çünkü sesi bulmuş ve durdurmuştu.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kızaktaki deliği buldu ve buzla kapattı"
   - Cümle 0 (plan satırı): «dağda tıkır tıkır garip bir ses geldi | kızaktaki deliği buldu ve buzla kapattı»
   - Açıklama: Gövdede delik buzla kapatılmıyor; plan çözümü gövdeyle uyuşmuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yukarıdan tıkır tıkır garip bir ses geldi"
   - Cümle 2: «Birden yukarıdan tıkır tıkır garip bir ses geldi.»
   - Açıklama: Garip bir ses Elsa için gerçek bir sorun değil; asıl sorun Kristoff'un küplerini kaybetmesi ve bu Elsa'nın sorunu olarak kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tıkır tıkır garip bir ses"
   - Cümle 2: «Birden yukarıdan tıkır tıkır garip bir ses geldi.»
   - Açıklama: Garip bir ses Elsa için gerçek bir sorun değil; asıl sorun Kristoff'un küplerinin dökülmesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0008` birebir aynı, `@degisim: meşgul -> hızlı` (tutuyorsan), ardından `@onarim: c2f800f8d4668b0c89ad47389868fd738c7bc531`, sonra gövde.

### Hikâye 2: tohum elsa-0012 (deneme 4 -> 5)

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
Bir sabah Elsa dağda, sarayının önünde buzdan küçük bir çiçek yaptı. Çiçeğin sapına kırmızı bir fiyonk bağlamak istedi. Ama fiyonk bağlamayı bilmiyordu ve kurdele hep açılıyordu. Kristoff biraz ileride kızağını dolduruyordu. Elsa önce çekingen çekingen Kristoff'a baktı. Sonra Kristoff'un yanına yürüdü. "Kristoff, bana fiyonk bağlamayı öğretir misin?" diye sordu Elsa. "Tabii, çok kolay," dedi Kristoff. Kristoff yavaşça bir fiyonk bağladı ve açtı. Elsa da iki halka yaptı ve onları sıkıca bağladı. Bu kez kurdele hiç açılmadı. "Teşekkürler, Kristoff, bu fiyonklu çiçek de senin!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa önce çekingen çekingen"
   - Cümle 5: «Elsa önce çekingen çekingen Kristoff'a baktı.»
   - Açıklama: 'Çekingen' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0012` birebir aynı, `@degisim: okumak -> bağlamak` (tutuyorsan), ardından `@onarim: e44c12e7f83c32f7401fa61dc5388c8c62d12ffa`, sonra gövde.

### Hikâye 3: tohum elsa-0017 (deneme 4 -> 5)

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
Elsa limanda ahşap sandalyesine oturmuş, denizi seyrediyordu. Kristoff uzun süre buz taşımıştı ve çok yorgundu. Ama kıyıdaki taşlar ıslaktı ve oturacak kuru bir yer yoktu. Elsa hemen sandalyesinden kalktı. "Kristoff, gel, bu sandalyeye sen otur," dedi Elsa. "Ama bu sandalye senin," dedi Kristoff. "Sen çok yorgunsun, kraliçe olarak sandalyemi sana veriyorum," dedi Elsa. Kristoff teşekkür etti ve sandalyeye oturdu. Elsa da sandalyenin yanında durdu. İkisi birlikte denizdeki küçük dalgalara baktı. Biraz sonra Kristoff dinlendi ve kalktı. Sonra Elsa ile Kristoff kızağı birlikte hazırladılar ve mutlu mutlu güldüler.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kraliçe olarak sandalyemi sana veriyorum"
   - Cümle 7: «"Sen çok yorgunsun, kraliçe olarak sandalyemi sana veriyorum," dedi Elsa.»
   - Açıklama: Sandalyeyi vermenin kraliçelikle ilgisi yok; 'kraliçe olarak' anlamca yersiz ve soyut.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kraliçe olarak sandalyemi sana"
   - Cümle 7: «"Sen çok yorgunsun, kraliçe olarak sandalyemi sana veriyorum," dedi Elsa.»
   - Açıklama: 'Kraliçe olarak' soyut bir rol ifadesidir ve küçük çocuk için anlaşılır değildir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe olarak sandalyemi sana veriyorum"
   - Cümle 7: «"Sen çok yorgunsun, kraliçe olarak sandalyemi sana veriyorum," dedi Elsa.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşini korumaktır; burada işe yarar bir özellik olarak değil süs olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) sorunu çözmede işe yarar biçimde kullanılmıyor, yalnız adı geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa ile Kristoff kızağı birlikte hazırladılar"
   - Cümle 12: «Sonra Elsa ile Kristoff kızağı birlikte hazırladılar ve mutlu mutlu güldüler.»
   - Açıklama: Kızak sebepsiz beliriyor ve hikayedeki sorunla hiçbir bağı yok.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kızağı birlikte hazırladılar"
   - Cümle 12: «Sonra Elsa ile Kristoff kızağı birlikte hazırladılar ve mutlu mutlu güldüler.»
   - Açıklama: Kızak deniz kıyısında sebepsiz beliriyor ve olayla bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0017` birebir aynı, ardından `@onarim: b232cccc39cc3526c5d85747d84893ebc9cc9351`, sonra gövde.

### Hikâye 4: tohum elsa-0019 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: arkadaşı yazı severdi ve şeftaliyi çok istedi | şeftaliyi ona verdi ve keki ikiye böldü
@tohum: elsa-0019
@degisim: değişmek -> paylaşmak
Bir sabah Elsa dağda, sarayının önünde sepetini açtı. Sepette bir şeftali ile çilekli bir kek vardı. O sırada Olaf geldi ve şeftaliye uzun uzun baktı. Olaf yazı severdi ve şeftaliyi çok istedi. Elsa şeftaliyi hemen Olaf'a uzattı. Sonra buzdan ince bir çubuk yaptı. Çilekli keki bu çubukla ikiye böldü. Kekin yarısını da Olaf'a verdi. Olaf kocaman gülümsedi ve Elsa'ya sarıldı. İkisi yan yana oturdu ve karlı dağı mutlu mutlu seyretti. Elsa bundan sonra yiyeceklerini hep Olaf ile paylaştı.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şeftaliyi ona verdi ve keki ikiye böldü"
   - Cümle 0 (plan satırı): «arkadaşı yazı severdi ve şeftaliyi çok istedi | şeftaliyi ona verdi ve keki ikiye böldü»
   - Açıklama: Planda keki Elsa bölüyor ama gövdede keki Olaf bölüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf yazı severdi"
   - Cümle 4: «Olaf yazı severdi ve şeftaliyi çok istedi.»
   - Açıklama: 'yazı' kelimesi küçük çocukta 'yazı' (harfler) ile karışır; 'yaz mevsimini severdi' gibi açık bir söyleyiş gerekir.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Olaf yazı severdi ve şeftaliyi çok istedi"
   - Cümle 4: «Olaf yazı severdi ve şeftaliyi çok istedi.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Olaf yazı severdi ve şeftaliyi çok istedi"
   - Cümle 4: «Olaf yazı severdi ve şeftaliyi çok istedi.»
   - Açıklama: Ortada gerçek bir sorun yok; Olaf'ın şeftali istemesi hemen karşılanıyor.
   - Açıklama: Yazı sevmek şeftaliyi istemenin akla yatkın sebebi değil ve Elsa'nın hemen verdiği şeftali bir sorun oluşturmuyor.
   - Açıklama: Olaf'ın şeftaliyi istemesi bir engel ya da sorun değil; Elsa hemen veriyor, gerçek bir sorun yok.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Çilekli keki bu çubukla ikiye böldü"
   - Cümle 7: «Çilekli keki bu çubukla ikiye böldü.»
   - Açıklama: Keki ikiye bölmek şeftali isteğine yönelmiyor ve çözüme gereksiz adımlar ekliyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çilekli keki bu çubukla ikiye böldü"
   - Cümle 7: «Çilekli keki bu çubukla ikiye böldü.»
   - Açıklama: Olaf şeftaliyi istemişti; kekin bölünmesi sorundan çıkmıyor ve sonradan eklenmiş bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0019` birebir aynı, `@degisim: değişmek -> paylaşmak` (tutuyorsan), ardından `@onarim: 2e0d830f01fe208f552ca08aadd021fceb3339df`, sonra gövde.

### Hikâye 5: tohum elsa-0020 (deneme 4 -> 5)

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
Rüzgar dağda sert sert esiyordu. Sven, Elsa'nın sarayına girip dinlenmek istedi. Ama kapıya giden yol buzluydu ve Sven her adımda kaydı. Sven kapıya ulaşamadı ve geri çekildi. Elsa kapıdan onu gördü. "Üzülme, Sven, sana yardım edeceğim," dedi Elsa. Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu. Elsa pelerinini çıkardı ve buzlu yolun üstüne serdi. Sven pelerine bastı ve bu kez hiç kaymadı. Yavaş yavaş yürüdü ve kapıya ulaştı. Elsa sarayda ona bir havuç verdi. Sven havucu mutlu mutlu yedi ve Elsa da sevinçle güldü.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa kraliçe olduğu için yepyeni"
   - Cümle 7: «Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu.»
   - Açıklama: 'Kraliçe olduğu için' sebep bağı yerinde değil; 'için' yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu"
   - Cümle 7: «Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşini korumaktır; burada pelerin sahibi olma gerekçesi olarak kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin"
   - Cümle 7: «Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu.»
   - Açıklama: Pelerin çözüm için kraliçelik gibi ilgisiz bir sebeple sonradan getiriliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu"
   - Cümle 7: «Elsa kraliçe olduğu için yepyeni ve uzun bir pelerin giyiyordu.»
   - Açıklama: Pelerinin yepyeni olması kraliçelikle sebepsizce bağlanıyor ve bu ayrıntı hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0020` birebir aynı, `@degisim: bileklik -> havuç` (tutuyorsan), ardından `@onarim: e596e9e9026f6a34ec3732e78f4df0d90ba68c3d`, sonra gövde.

### Hikâye 6: tohum elsa-0023 (deneme 4 -> 5)

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
Dağda soğuk bir rüzgar esiyordu. Elsa ile Sven sarayın önünde oturuyordu ve ikisi de biraz acıkmıştı. Ama sepette tek havuç kalmıştı, çünkü öteki havuçları sabah yemişlerdi. Sven havucu burnuyla Elsa'ya itti, çünkü Elsa kraliçeydi. "Sven, bu havucu ikimize yetiştiririm," dedi Elsa. Havuç soğuktan kırılgan olmuştu ve Elsa onu kolayca ikiye böldü. Yarısını Sven'e verdi, öteki yarısını kendisi yedi. Sven kendi yarısını hemen bitirdi ve Elsa'ya burnunu sürttü. Elsa gülerek onu okşadı. Elsa bundan sonra havuçlarını hep Sven ile paylaştı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çünkü Elsa kraliçeydi"
   - Cümle 4: «Sven havucu burnuyla Elsa'ya itti, çünkü Elsa kraliçeydi.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşini korumaktır; burada yalnız havuç önceliği gerekçesi olarak ve işe yaramadan geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven havucu burnuyla Elsa'ya itti, çünkü Elsa kraliçeydi"
   - Cümle 4: «Sven havucu burnuyla Elsa'ya itti, çünkü Elsa kraliçeydi.»
   - Açıklama: Kraliçe özelliği karttaki 'kız kardeşini korur' anlamında değil, yalnız bir ayrıcalık gerekçesi olarak kullanılıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu havucu ikimize yetiştiririm"
   - Cümle 5: «"Sven, bu havucu ikimize yetiştiririm," dedi Elsa.»
   - Açıklama: 'Yetiştirmek' burada yanlış anlamda; 'ikimize yetirir' ya da 'paylaşırız' olmalı.
   - Açıklama: 'Yetiştirmek' yanlış anlamda kullanılmış; 'ikimize yetecek gibi bölerim' denmeli.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Havuç soğuktan kırılgan olmuştu"
   - Cümle 6: «Havuç soğuktan kırılgan olmuştu ve Elsa onu kolayca ikiye böldü.»
   - Açıklama: 'Kırılgan' kelimesi 3 yaşındaki çocuk için ağır bir sözcük.
   - Açıklama: 'Kırılgan' kelimesi 3 yaşındaki çocuk için zor ve plan satırında da geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0023` birebir aynı, `@degisim: takvim -> havuç` (tutuyorsan), ardından `@onarim: 628276f5a3ba84009bf4d12296ab9221ea8546b1`, sonra gövde.

### Hikâye 7: tohum elsa-0025 (deneme 3 -> 4)

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
@plan: buzdan geminin yelkeni yoktu ve gemi gitmedi | elindeki bezi geminin direğine bağladı
@tohum: elsa-0025
@degisim: paslı -> beyaz
Elsa karlı dağda gemi oyunu oynuyordu. Buzdan küçük bir gemi yapmıştı ve üstündeki karı beyaz bir bezle siliyordu. Ama geminin yelkeni yoktu ve rüzgar gemiyi hiç götürmedi. Elsa gemisinin karın üstünde kaymasını istiyordu. Biraz düşündü ve elindeki beze baktı. Bezi geminin direğine sıkıca bağladı. Rüzgar esti ve bez yelken gibi şişti. Küçük gemi düz karın üstünde yavaşça kaymaya başladı. Elsa ayağa kalktı ve gemisinin arkasından koştu. Gemi karda uzun bir iz bıraktı. Elsa gemisini tuttu ve yeniden rüzgara bıraktı. Elsa gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Buzdan küçük bir gemi yapmıştı"
   - Cümle 2: «Buzdan küçük bir gemi yapmıştı ve üstündeki karı beyaz bir bezle siliyordu.»
   - Açıklama: Tohumdaki buz özelliği sorunu çözmekte işe yaramıyor; çözümü bez sağlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0025` birebir aynı, `@degisim: paslı -> beyaz` (tutuyorsan), ardından `@onarim: 09932baa19fecd03577eab4aef46092048101d55`, sonra gövde.

### Hikâye 8: tohum elsa-0027 (deneme 3 -> 4)

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
Dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Elsa bir kova sabunlu suya ince bir dal batırıp baloncuk yapıyordu. Olaf da oynamak istedi ama karın içinde başka dal yoktu. "Elsa, ben ne yapacağım?" diye sordu Olaf. Elsa bir kraliçeydi ve Olaf'ı hep korurdu. Dalı dikkatle ikiye böldü. İki parça da baloncuk yapmak için yeterince uzundu. "Olaf, bu parça senin," dedi Elsa. İkisi dallarını suya batırıp üfledi. Parlak baloncuklar havada yükseldi ve küçüldü. Olaf onların arasında zıpladı ve güldü. Elsa ile Olaf kovanın başında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve Olaf'ı hep korurdu"
   - Cümle 5: «Elsa bir kraliçeydi ve Olaf'ı hep korurdu.»
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; Olaf'a aktarılıyor ve çözümde işe yaramıyor.
   - Açıklama: Kartta özellik kız kardeşini korumak; Olaf'a aktarılıyor ve çözüm bu özellikten gelmiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf'ı hep korurdu"
   - Cümle 5: «Elsa bir kraliçeydi ve Olaf'ı hep korurdu.»
   - Açıklama: Karttaki özellik kız kardeşini korumak iken hikayede Olaf korunuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve Olaf'ı hep korurdu"
   - Cümle 5: «Elsa bir kraliçeydi ve Olaf'ı hep korurdu.»
   - Açıklama: Kraliçelik ve koruma bilgisi dalı bölme çözümüne hiçbir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0027` birebir aynı, `@degisim: yatak -> kova` (tutuyorsan), ardından `@onarim: 23e436819177ef6aabe6c926e9074237b0924a88`, sonra gövde.

### Hikâye 9: tohum elsa-0029 (deneme 3 -> 4)

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
@plan: ikisi aynı anda zıpladı ve rüzgar izleri kapattı | sırayla zıplamayı ve havuç koymayı önerdi
@tohum: elsa-0029
Rüzgar ağaçların arasında sert sert esiyordu. Elsa ile Kristoff karlı ormanda zıplama oyunu oynuyordu. Ama ikisi hep aynı anda zıpladı ve rüzgar izlerini hemen kapattı. Kimin daha uzağa gittiğini hiç göremediler. "Kristoff, sırayla zıplayalım ve durduğumuz yere havuç koyalım," dedi Elsa. Kristoff çantasından bir demet turuncu havuç çıkardı. Elsa bir kraliçeydi ve ilk sırayı Kristoff'a verdi. Önce Kristoff zıpladı ve durduğu yere bir havuç koydu. Sonra Elsa zıpladı ve kendi havucunu biraz daha ileriye koydu. Rüzgar esti ama havuçlar yerinde kaldı. Birkaç kez daha sırayla zıpladılar. İkisi de çok sevindi, çünkü artık kimin daha uzağa zıpladığını görebiliyorlardı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi hep aynı anda zıpladı ve rüzgar izlerini hemen kapattı"
   - Cümle 3: «Ama ikisi hep aynı anda zıpladı ve rüzgar izlerini hemen kapattı.»
   - Açıklama: Aynı anda zıplamak ile rüzgarın izleri kapatması arasında akla yatkın bir sebep bağı yok.
   - Açıklama: Aynı anda zıplamak rüzgarın izleri kapatmasının sebebi değil; sebep akla yatkın değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kristoff, sırayla zıplayalım ve durduğumuz yere havuç koyalım"
   - Cümle 5: «"Kristoff, sırayla zıplayalım ve durduğumuz yere havuç koyalım," dedi Elsa.»
   - Açıklama: Sırayla zıplamak rüzgar sebebine yönelmiyor; asıl işi yalnız havuç işareti görüyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve ilk sırayı Kristoff'a verdi"
   - Cümle 7: «Elsa bir kraliçeydi ve ilk sırayı Kristoff'a verdi.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşini korumaktır; burada sorunu çözmeyen bir sıra verme gerekçesi olarak kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve ilk sırayı"
   - Cümle 7: «Elsa bir kraliçeydi ve ilk sırayı Kristoff'a verdi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) sorunun çözümünde işe yarar biçimde kullanılmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve ilk sırayı Kristoff'a verdi"
   - Cümle 7: «Elsa bir kraliçeydi ve ilk sırayı Kristoff'a verdi.»
   - Açıklama: Kraliçelik bilgisi olaydan çıkmıyor ve sıranın verilmesine hiçbir sebep oluşturmuyor.
   - Açıklama: Kraliçe olmak ilk sırayı vermenin sebebi değil; işlevsiz ve kopuk bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0029` birebir aynı, ardından `@onarim: 6f046ba3c5994827c07e9d60242aab29369bba69`, sonra gövde.

### Hikâye 10: tohum elsa-0033 (deneme 3 -> 4)

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
Karlı ormanda Elsa ile Anna yan yana yürüyor ve şekerleme yiyordu. Birden Anna'nın saçı alçak bir dala takıldı. Anna başını çevirdi ama saçı daldan çıkmadı. Anna saçını hızla çekmek istedi. Elsa bir kraliçeydi ve kardeşini korumak için onun elini yavaşça tuttu. Sonra saç tellerini daldan tek tek ayırdı. Sonunda Anna'nın saçı kurtuldu. Anna sevinçle Elsa'ya sarıldı. Teşekkür etmek için son şekerlemesini Elsa'ya verdi. Elsa tatlı hediyeyi aldı ve kardeşine gülümsedi. Anna çok mutluydu, çünkü Elsa ona yardım etmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi"
   - Cümle 5: «Elsa bir kraliçeydi ve kardeşini korumak için onun elini yavaşça tuttu.»
   - Açıklama: Elsa'nın kraliçe olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0033` birebir aynı, `@degisim: sevecen -> tatlı` (tutuyorsan), ardından `@onarim: 56974309d931076c354082b91cba1669d9c85785`, sonra gövde.

### Hikâye 11: tohum elsa-0034 (deneme 3 -> 4)

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
Elsa limanda Kristoff ile yürüyordu. Kristoff iki eliyle büyük bir buz kalıbı taşıyordu. Birden güçlü bir rüzgar Kristoff'un şapkasını başından uçurdu. Şapka limanın taş yolunda yuvarlandı. Kristoff ağır buzla şapkanın peşinden gitmek istedi. Elsa kraliçeydi ve arkadaşını korumak için onu durdurdu. "Sen burada kal, Kristoff, ben alırım," dedi Elsa. Hemen koştu ve şapkayı incecik ipinden yakaladı. Sonra şapkayı Kristoff'un başına taktı ve ipini sıkıca bağladı. Artık şapka rüzgarda hiç uçmadı. "Teşekkürler, Elsa, çok hızlıydın!" dedi Kristoff. Elsa güldü. İkisi limanda yürümeye mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşını korumak için onu durdurdu"
   - Cümle 6: «Elsa kraliçeydi ve arkadaşını korumak için onu durdurdu.»
   - Açıklama: Karttaki özellik kız kardeşini korumak iken hikayede Kristoff korunuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve arkadaşını korumak için onu durdurdu"
   - Cümle 6: «Elsa kraliçeydi ve arkadaşını korumak için onu durdurdu.»
   - Açıklama: Elsa'nın kraliçe olması şapkayı almakla ilgisiz, sebep olarak işlevsiz bir ayrıntı gibi kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0034` birebir aynı, `@degisim: kabak -> şapka` (tutuyorsan), ardından `@onarim: bc72e93f422e69e5c088c60fd491ad2936ee33c5`, sonra gövde.

### Hikâye 12: tohum elsa-0036 (deneme 2 -> 3)

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
@plan: kızak kabarık bir kar yığınına girip takıldı | kızaktan inip kızağı geri çekti ve yolu değiştirdi
@tohum: elsa-0036
@degisim: kapı -> kızak
Karlı ormanda Elsa ile Sven kızak oyunu oynuyordu. Sven önde koşuyor, Elsa da arkada neşeyle şarkı söylüyordu. Ama kızak kabarık bir kar yığınına girdi ve durdu. Sven bütün gücüyle çekti ama kızak hiç kıpırdamadı. Sven çok yoruldu. Elsa kraliçeydi ve arkadaşını korumak için hemen kızaktan indi. Kızağı arkadan tuttu ve onu yığından geri çekti. "Sven, yolu değiştirelim," dedi Elsa. Sven başını salladı ve kızağı başka bir yola çekti. Bu yolda kar sertti ve kızak kolayca kaydı. Elsa yeniden yerine oturdu. Elsa ile Sven ağaçların arasında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşını korumak için hemen kızaktan indi"
   - Cümle 6: «Elsa kraliçeydi ve arkadaşını korumak için hemen kızaktan indi.»
   - Açıklama: Sven bir tehlikede değil; 'korumak' yanlış anlamda, 'yardım etmek' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşını korumak için hemen"
   - Cümle 6: «Elsa kraliçeydi ve arkadaşını korumak için hemen kızaktan indi.»
   - Açıklama: Elsa arkadaşını korumuyor, ona yardım ediyor; 'korumak' yanlış anlamda.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve arkadaşını korumak için"
   - Cümle 6: «Elsa kraliçeydi ve arkadaşını korumak için hemen kızaktan indi.»
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; burada arkadaşa uygulanıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve arkadaşını korumak"
   - Cümle 6: «Elsa kraliçeydi ve arkadaşını korumak için hemen kızaktan indi.»
   - Açıklama: Karttaki özellik kız kardeşini korumak; burada Sven'i korumaya kaydırılmış ve kraliçelik gerekçe olarak etiketleniyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sven, yolu değiştirelim"
   - Cümle 8: «"Sven, yolu değiştirelim," dedi Elsa.»
   - Açıklama: Çözüm kızaktan inme, kızağı geri çekme ve yolu değiştirme olarak iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0036` birebir aynı, `@degisim: kapı -> kızak` (tutuyorsan), ardından `@onarim: 89aa24765c969dc94c36b8f36b1b3362c0182077`, sonra gövde.
