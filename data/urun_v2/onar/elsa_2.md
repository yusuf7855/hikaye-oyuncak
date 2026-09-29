# Editör görevi (onarım): Elsa, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar2.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0001 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0001
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yağmur ya da kar günü
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çöp', fiil 'ekmek', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kar birden çok hızlı yağmaya başladı | kardeşini açık kapıdan saraya aldı ve bahçeyi bitirdi
@tohum: elsa-0001
@degisim: çöp -> dal
Elsa ile Anna dağda, sarayın önünde kar bahçesi yapıyordu. Anna karın içine küçük dallar ekiyordu. Birden kar çok hızlı yağmaya başladı. "Elsa, saçlarım karla doldu!" dedi Anna. Elsa kardeşini korumak için hemen elinden tuttu. "Gel, Anna, içeride bekleyelim," dedi Elsa. İki kardeş sarayın açık kapısından içeri koştu. Orada yan yana durup yağan karı izlediler. Biraz sonra kar yavaşladı. Elsa ile Anna bahçeye geri döndü. Anna kalan dalları da tek tek ekti. Elsa bahçenin çevresine küçük kar topları dizdi. "Teşekkürler, kraliçem, bu en güzel kar bahçesi oldu!" dedi Anna.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karın içine küçük dallar ekiyordu"
   - Cümle 2: «Anna karın içine küçük dallar ekiyordu.»
   - Açıklama: Dal ekilmez, dikilir; fiil nesnesine uymuyor.
   - Açıklama: Dal ekilmez, dikilir; 'ekmek' fiili nesnesine uymuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden kar çok hızlı yağmaya başladı"
   - Cümle 3: «Birden kar çok hızlı yağmaya başladı.»
   - Açıklama: Sorunun sebebi söylenmiyor ve karın kendiliğinden yavaşlamasıyla geçen önemsiz bir hava olayı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0001` birebir aynı, `@degisim: çöp -> dal` (tutuyorsan), ardından `@onarim: f5399ee1a0289f46630178e6e10567bd1195a0ad`, sonra gövde.

### Hikâye 2: tohum elsa-0003 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0003
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'şemsiye', fiil 'yemek', sıfat 'sıcak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: rüzgar esti ve şemsiye karın içinde durmadı | şemsiyenin dibine buzdan sağlam bir ayak yaptı
@tohum: elsa-0003
Bir sabah Elsa ile Olaf karlı kıyıda sıcak yaz günü oyunu oynuyordu. Olaf büyük bir şemsiyeyi karın içine dikti. Ama rüzgar esti ve şemsiye yere düştü. Olaf onu tekrar dikti, ama şemsiye yine devrildi. "Elsa, bu şemsiye hiç durmuyor!" dedi Olaf. Elsa eğildi ve şemsiyenin dibine buzdan sağlam bir ayak yaptı. Rüzgar bir kez daha esti, ama şemsiye bu kez kıpırdamadı. İkisi şemsiyenin altına oturdu. Olaf kardan iki küçük kek hazırladı ve birini Elsa'ya verdi. İkisi de kekleri yiyormuş gibi yaptı. "Bu kek çok lezzetli!" dedi Olaf ve güldü. Elsa çok sevindi, çünkü şemsiyeleri artık rüzgarda hiç düşmüyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karlı kıyıda sıcak yaz günü oyunu oynuyordu"
   - Cümle 1: «Bir sabah Elsa ile Olaf karlı kıyıda sıcak yaz günü oyunu oynuyordu.»
   - Açıklama: 'Sıcak yaz günü oyunu' karlı kıyıda anlamı belirsiz ve küçük çocuk için kafa karıştırıcı bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0003` birebir aynı, ardından `@onarim: 91d5be66d7b20388b09e52870e0caa72fd63ac1c`, sonra gövde.

### Hikâye 3: tohum elsa-0004 (deneme 2 -> 3)

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
@plan: ağır buzlar yüzünden kızağın ayağı kırıldı | buzdan yeni bir kızak ayağı yaptı
@tohum: elsa-0004
@degisim: yelpaze -> kızak
Bir sabah Elsa dağda, sarayının önünde yürüyordu. Kristoff orada kızağına buz parçaları yüklüyordu. Ama buzlar çok ağırdı ve kızağın tahta ayağı kırıldı. "Elsa, kızak kaymazsa buzları satamam!" dedi Kristoff. Elsa ona yardım etmek istedi. Kırık ayağa dikkatle baktı. Sonra Kristoff'a biraz geri durmasını söyledi. Elsa ellerini açtı ve kızağın altına buzdan yeni bir ayak yaptı. Kızak yeniden düz durdu. Kristoff kızağı itti ve kızak karda kolayca kaydı. "Bu çok özel bir kızak oldu, Elsa!" dedi Kristoff. Elsa çok sevindi, çünkü Kristoff'un kızağı yeniden kayıyordu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kızağın altına buzdan yeni bir ayak yaptı"
   - Cümle 8: «Elsa ellerini açtı ve kızağın altına buzdan yeni bir ayak yaptı.»
   - Açıklama: Ayağı kıran sebep ağır yüktür ama çözüm yükü hiç ele almıyor, yalnız kırık ayağı değiştiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0004` birebir aynı, `@degisim: yelpaze -> kızak` (tutuyorsan), ardından `@onarim: 32e35e7fbe4b760fc41f739037bf7749cc7379af`, sonra gövde.

### Hikâye 4: tohum elsa-0005 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0005
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'fıçı', fiil 'hoşlanmak', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: çorbayı karıştırmak için kaşığı yoktu | buzdan sağlam bir kaşık yapıp çorbayı karıştırdı
@tohum: elsa-0005
@degisim: esnek -> yumuşak
Bir sabah Elsa dağda, sarayının önünde yemek yapma oyunu oynuyordu. Boş bir fıçıyı karla doldurdu ve kar çorbası yaptı. Ama çorbayı karıştırmak için kaşığı yoktu. Elsa yerden ince bir dal aldı. Dal çok yumuşaktı ve karın içinde hemen eğildi. Elsa biraz düşündü. Buzdan uzun, sağlam bir kaşık yaptı. Elsa bu kaşıkla çorbayı güzelce karıştırdı. Sonra çorbanın tadına bakıyormuş gibi yaptı ve güldü. Elsa bu oyundan çok hoşlandı, çünkü kar çorbası sonunda hazırdı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Boş bir fıçıyı karla"
   - Cümle 2: «Boş bir fıçıyı karla doldurdu ve kar çorbası yaptı.»
   - Açıklama: 'Fıçı' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama çorbayı karıştırmak için kaşığı yoktu"
   - Cümle 3: «Ama çorbayı karıştırmak için kaşığı yoktu.»
   - Açıklama: Kaşığın neden olmadığı söylenmiyor; sorunun sebebi verilmiyor.
   - Açıklama: Kaşığın neden olmadığı hiç söylenmiyor; sorunun sebebi verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0005` birebir aynı, `@degisim: esnek -> yumuşak` (tutuyorsan), ardından `@onarim: 7341732ee2deda68a55f4061f795672533a232de`, sonra gövde.

### Hikâye 5: tohum elsa-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0006
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'poğaça', fiil 'toplanmak', sıfat 'soğuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: dağda garip bir ses duyuldu | sesin aç geyikten geldiğini buldu ve onu doyurdu
@tohum: elsa-0006
Bir sabah Elsa ile Sven dağda yürüyordu. Elsa'nın kolunda poğaça dolu bir sepet vardı. Birden yakından garip bir ses duyuldu. "Bu ses nereden geliyor, Sven?" diye sordu Elsa. Sven hemen sepete baktı. Ses yine geldi ve bu kez çok yakındı. Elsa kulağını Sven'in karnına yaklaştırdı. "Sven, bu ses senin karnından geliyor!" dedi Elsa ve güldü. Sven çok acıkmıştı. Yerde soğuk kar toplanmıştı. Poğaçalar karın içine düşmesin diye Elsa buzdan bir tabak yaptı. Poğaçaları tabağın üstüne dizdi. Sven iki poğaçayı hemen yedi. Sonra Elsa ile Sven yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Poğaçalar karın içine düşmesin"
   - Cümle 11: «Poğaçalar karın içine düşmesin diye Elsa buzdan bir tabak yaptı.»
   - Açıklama: Az önce Sven'in karnından söz edildiği için 'karın' hem kar hem karın olarak okunuyor; 'karların içine' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa buzdan bir tabak yaptı"
   - Cümle 11: «Poğaçalar karın içine düşmesin diye Elsa buzdan bir tabak yaptı.»
   - Açıklama: Sven'i doyurmak yerine önce tabak yapıp poğaçaları dizmek gibi ek adımlar ekleniyor ve çözüm ikiden fazla adım sürüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa buzdan bir tabak yaptı"
   - Cümle 11: «Poğaçalar karın içine düşmesin diye Elsa buzdan bir tabak yaptı.»
   - Açıklama: Buz tabak yalnız özelliği göstermek için sebepsizce kuruluyor; Sven'i doyurmak için gerekli değil.
   - Açıklama: Kar ve buzdan tabak ayrıntısı çözüme gereksiz, zorlama bir adım ekliyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Poğaçaları tabağın üstüne dizdi"
   - Cümle 12: «Poğaçaları tabağın üstüne dizdi.»
   - Açıklama: Geyiği doyurmak doğrudan poğaça vermek yerine tabak yapma ve dizme gibi fazladan adımlarla uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0006` birebir aynı, ardından `@onarim: 8df69f943e71c5b78a650d766f2f785ea377b607`, sonra gövde.

### Hikâye 6: tohum elsa-0007 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0007
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bağcık', fiil 'taramak', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: rüzgar esti ve mavi bağcığı uçup gitti | limanı iyi tanıdığı için bağcığı direğin dibinde buldu
@tohum: elsa-0007
@degisim: saygılı -> uzun
Bir sabah Elsa limanın kıyısında yürüyordu. Birden sert bir rüzgar esti ve saçlarını dağıttı. Elsa'nın mavi bağcığı da çözüldü ve uçup gitti. Uzun pelerini yere doğru kaymaya başladı. Elsa pelerini iki eliyle tuttu. Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu. Hemen limanın en yakın direğine doğru yürüdü. Mavi bağcığı direğin dibinde gördü ve yavaşça aldı. Pelerinini yeniden sıkıca bağladı. Sonra saçlarını parmaklarıyla taradı. Elsa çok sevindi, çünkü kaybolan bağcığı kendi başına bulmuştu.
```

**Hakem bulguları (8):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "esti ve saçlarını dağıttı"
   - Cümle 2: «Birden sert bir rüzgar esti ve saçlarını dağıttı.»
   - Açıklama: Özne rüzgar olduğu için 'saçlarını' zamirinin Elsa'yı gösterdiği belli değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "mavi bağcığı da çözüldü ve uçup gitti"
   - Cümle 3: «Elsa'nın mavi bağcığı da çözüldü ve uçup gitti.»
   - Açıklama: Rüzgarın uçurduğu bağcık hemen yakında bulunuyor; sorun 'uçtu, buldu, bitti' türünden önemsiz bir olay.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa krallığın kraliçesiydi"
   - Cümle 6: «Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu.»
   - Açıklama: 'Krallığın kraliçesi' gereksiz anlam tekrarı içeriyor ve cümle üst üste ikinci kez 'Elsa' ile başlıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu"
   - Cümle 6: «Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu.»
   - Açıklama: Karttaki özellik kraliçe olup kız kardeşini korumaktır; burada kraliçelik limanı tanımaya dönüştürülüyor ve bağcığın bulunmasında işe yaramıyor.
   - Açıklama: Tohumdaki özellik kartta 'Kraliçedir; kız kardeşini korur' olarak geçer; burada yalnız limanı tanımanın gerekçesi olarak anılıyor ve karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği kartta 'kız kardeşini korur' olarak tanımlı; burada limanı tanımaya bağlanıyor ve sorunun çözümünde gerçek bir işe yaramıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu"
   - Cümle 6: «Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu.»
   - Açıklama: Limanı tanımak rüzgarın bağcığı nereye uçurduğunu bulmaya yönelik bir çözüm değil; bağcık şans eseri bulunuyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu"
   - Cümle 6: «Elsa krallığın kraliçesiydi ve limanı çok iyi tanıyordu.»
   - Açıklama: Kraliçe olmak ve limanı tanımak bağcığın direğin dibinde olduğunu açıklamıyor; çözüm sebepsizce geliyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "limanın en yakın direğine"
   - Cümle 7: «Hemen limanın en yakın direğine doğru yürüdü.»
   - Açıklama: 'En yakın' neye yakın olduğu belirtilmeden limana bağlanmış; anlam belirsiz.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hemen limanın en yakın direğine doğru yürüdü"
   - Cümle 7: «Hemen limanın en yakın direğine doğru yürüdü.»
   - Açıklama: Uçup giden bağcığın neden direğin dibinde olduğu hiçbir olaydan çıkmıyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0007` birebir aynı, `@degisim: saygılı -> uzun` (tutuyorsan), ardından `@onarim: ae426d95613990b7d7f5f02e975c10d20a1758cb`, sonra gövde.

### Hikâye 7: tohum elsa-0010 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0010
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'beşik', fiil 'silkmek', sıfat 'faydalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: kaygan kıyıda geyiğin havuçları denize düştü | havuçlarını paylaştı ve buzdan bir kaseye koydu
@tohum: elsa-0010
@degisim: faydalı -> tatlı
Limanda kayıklar beşik gibi yavaş yavaş sallanıyordu. Elsa ile Sven hafif karın altında kıyıda oturuyordu. Birden Sven'in havuç kovası kaygan kıyıda kaydı ve havuçlar denize düştü. Sven üzgün üzgün suya baktı, çünkü çok acıkmıştı. Elsa'nın sepetinde yalnız üç tatlı havuç vardı. "Gel, Sven, havuçlarımı seninle paylaşayım," dedi Elsa. Havuçlar yine düşmesin diye buzdan derin bir kase yaptı. İki havucu kaseye koydu ve Sven'in önüne itti. Sven havuçları hemen yedi. Sonra sevinçle sırtındaki karı silkti. Elsa da kendi havucunu yedi. Elsa ile Sven kıyıda yan yana mutlu mutlu karı izledi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kayıklar beşik gibi yavaş"
   - Cümle 1: «Limanda kayıklar beşik gibi yavaş yavaş sallanıyordu.»
   - Açıklama: 'Beşik gibi' benzetmesi mecazlı bir anlatım ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Beşik gibi sallanmak' benzetmesi mecazlı bir imge olup 3 yaşındaki çocuk için soyut kalabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0010` birebir aynı, `@degisim: faydalı -> tatlı` (tutuyorsan), ardından `@onarim: b2f16cd4bf676560a82d5c0991dd94690d068c24`, sonra gövde.

### Hikâye 8: tohum elsa-0011 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0011
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kum', fiil 'koparmak', sıfat 'büyülü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: bayrak için dal gerekti ama dallar çok yüksekteydi | kardeşine buzdan küçük bir bayrak yaptı
@tohum: elsa-0011
@degisim: kum -> kar
Limanın kıyısında Elsa ile Anna kardan bir kale yapıyordu. Anna kalenin tepesine bir bayrak koymak istedi. Bir ağaçtan dal koparmak için uzandı, ama dala ulaşamadı. "Elsa, dallar çok yüksek!" dedi Anna. "Bekle, Anna, sana bir bayrak yapayım," dedi Elsa. Elsa ellerini birleştirdi ve buzdan küçük bir bayrak yaptı. Bayrak güneşte pırıl pırıl parladı. Anna bayrağı dikkatle kalenin tepesine dikti. Kardan kale artık tamamdı. Elsa ile Anna kalelerine sevinçle baktı. "Teşekkürler, Elsa, bu büyülü bayrak kaleye çok yakıştı!" dedi Anna.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa, dallar çok yüksek!"
   - Cümle 4: «"Elsa, dallar çok yüksek!" dedi Anna.»
   - Açıklama: Anlatıcı sebebi bulutların beyazlığı diye veriyor, Anna ise dalların yüksekliğini söylüyor; sebep kendisiyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0011` birebir aynı, `@degisim: kum -> kar` (tutuyorsan), ardından `@onarim: 9c7b82330d19dbee0721442dd996e961ee3b233c`, sonra gövde.
