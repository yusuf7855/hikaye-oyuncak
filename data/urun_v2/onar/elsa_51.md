# Editör görevi (onarım): Elsa, onarım partisi 51

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar51.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar51.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0196 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0196
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'paspas', fiil 'inanmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: kızağı çok hızlı itti ve buzlar kırıldı | özür dileyip elinden çıkan buzla kızağı doldurdu
@tohum: elsa-0196
@degisim: paspas -> kızak
Limanda Sven buz dolu bir kızak çekiyordu. Elsa ona yardım etmek için kızağı arkadan itti. Ama çok hızlı itti ve buzlar kızaktan düşüp kırıldı. Sven kırık parçalara baktı ve başını eğdi. Elsa hemen Sven'in yanına gitti ve başını okşadı. Sonra ondan özür diledi. Elsa ellerini kızağa doğru açtı. Elinden parlak buz çıktı ve kızak yeniden doldu. Sven buna inanmadı ve yeni buzlara burnuyla dokundu. Buzlar gerçekti ve eskilerinden de iyiydi. Sven sevinçle ayaklarını yere vurdu. Sonra Sven kızağı çekti ve Elsa mutlu mutlu yanında yürüdü.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sven buna inanmadı"
   - Cümle 9: «Sven buna inanmadı ve yeni buzlara burnuyla dokundu.»
   - Açıklama: Kastedilen şaşkınlık için 'inanamadı' olmalı; 'inanmadı' reddetme anlamı veriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sven buna inanmadı ve"
   - Cümle 9: «Sven buna inanmadı ve yeni buzlara burnuyla dokundu.»
   - Açıklama: 'İnanmadı' yanlış anlamda; şaşkınlık için 'inanamadı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0196` birebir aynı, `@degisim: paspas -> kızak` (tutuyorsan), ardından `@onarim: b1537f6d425404ecc4db403fe53d66ebe1fd52b2`, sonra gövde.

### Hikâye 2: tohum elsa-0198 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0198
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'dal', fiil 'koşuşturmak', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: ağır kar küçük ağacın ince dalını eğdi | dalı hafifçe salladı ve karı yere döktü
@tohum: elsa-0198
Elsa karlı bir günde sarayın önünde koşuşturuyordu. Kar yavaş yavaş yağıyordu. Birden küçük bir ağacın ince dalı karın altında eğildi. Kar çok ağırdı ve dal kırılabilirdi. Elsa bu sarayın kraliçesiydi ve bahçesindeki ağaçları seviyordu. Ağacı korumak için hemen yanına koştu. Dalın ucunu eliyle yavaşça tuttu. Sonra dalı hafifçe salladı ve kar yere döküldü. Dal yukarı kalktı ve düzeldi. Elsa diğer dalları da temizledi. Küçük ağaç yine dik duruyordu. Elsa çok sevinçliydi ve karda koşuşturmaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve bahçesindeki ağaçları seviyordu"
   - Cümle 5: «Elsa bu sarayın kraliçesiydi ve bahçesindeki ağaçları seviyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kartın özellikler alanı) yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0198` birebir aynı, ardından `@onarim: 613af4ee5a3ee02310a9d315e544fcfc47a98901`, sonra gövde.

### Hikâye 3: tohum elsa-0200 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0200
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'mayo', fiil 'aramak', sıfat 'sakin'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: rüzgar gemi oyunundaki bayrağı hep düşürdü | sarayın kapısını açıp oyunu sakin içeriye taşıdı
@tohum: elsa-0200
@degisim: mayo -> bayrak
Dağın tepesinde sert bir rüzgar esiyordu. Elsa kızağını bir gemi yapmıştı ve gemi oyunu oynuyordu. Ama gemisine diktiği küçük bayrak rüzgarda hep yere düştü. Elsa oyun için sakin bir yer aradı. Sonra arkasındaki sarayına baktı. Kraliçe Elsa sarayın büyük kapısını açtı ve kızağı içeri çekti. İçeride hiç rüzgar yoktu. Elsa bayrağı yeniden gemisine dikti. Bayrak bu kez hiç düşmedi. Elsa gemisinin önüne oturdu ve uzaklara baktı. Elsa gemi oyununa sarayında mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "oyunu sakin içeriye taşıdı"
   - Cümle 0 (plan satırı): «rüzgar gemi oyunundaki bayrağı hep düşürdü | sarayın kapısını açıp oyunu sakin içeriye taşıdı»
   - Açıklama: 'Sakin içeriye' tamlaması bozuk; 'sakin olan içeriye' ya da 'rüzgarsız içeriye' olmalı.
   - Açıklama: 'sakin' sıfatı 'içeriye' zarfını nitelemiyor; 'oyunu sakin bir yere, içeriye taşıdı' gibi olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa sarayın büyük"
   - Cümle 6: «Kraliçe Elsa sarayın büyük kapısını açtı ve kızağı içeri çekti.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sarayın büyük kapısını açtı"
   - Cümle 6: «Kraliçe Elsa sarayın büyük kapısını açtı ve kızağı içeri çekti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohum özelliği 'Kraliçedir; kız kardeşini korur' yalnız unvan olarak geçiyor, kardeş yok ve özellik işe yaramıyor.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sarayın büyük kapısını açtı ve kızağı içeri çekti"
   - Cümle 6: «Kraliçe Elsa sarayın büyük kapısını açtı ve kızağı içeri çekti.»
   - Açıklama: Hikaye dağın tepesinde başlıyor ama sarayın içinde bitiyor; tek sahne kuralı çiğneniyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa gemi oyununa sarayında mutlu mutlu devam etti"
   - Cümle 11: «Elsa gemi oyununa sarayında mutlu mutlu devam etti.»
   - Açıklama: Hikaye başlıktaki dağda başlıyor ama saray içinde bitiyor; tek sahne kuralı çiğneniyor.
6. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "gemi oyununa sarayında mutlu mutlu devam etti"
   - Cümle 11: «Elsa gemi oyununa sarayında mutlu mutlu devam etti.»
   - Açıklama: Hikaye başlıktaki dağda başlıyor ama sarayın içinde bitiyor; sahne değişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0200` birebir aynı, `@degisim: mayo -> bayrak` (tutuyorsan), ardından `@onarim: b659c461aadf28fb39f62d91638ba02314fb7d59`, sonra gövde.

### Hikâye 4: tohum elsa-0201 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0201
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'lale', fiil 'gıdıklamak', sıfat 'kocaman'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: arkadaşına çiçek sürprizi yapmak istedi ama çiçek yoktu | buzdan kocaman bir lale yaptı
@tohum: elsa-0201
Bir sabah Elsa ile Olaf karlı ormanda yürüyordu. Olaf yazı ve çiçekleri çok seviyordu. Elsa ona bir sürpriz yapmak istedi ama ormanda hiç çiçek yoktu. "Olaf, gözlerini kapar mısın?" diye sordu Elsa. Olaf gözlerini sıkıca kapadı. Elsa ellerini açtı ve buzdan kocaman bir lale yaptı. Yaprakları güneşte parlıyordu. "Şimdi bakabilirsin, Olaf," dedi Elsa. Olaf baktı ve burnunu çiçeğe yaklaştırdı. Parlak yapraklar burnunu gıdıkladı ve Olaf yüksek sesle güldü. "Teşekkürler, Elsa, bu en güzel yaz çiçeği!" dedi Olaf.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Olaf yazı ve çiçekleri"
   - Cümle 2: «Olaf yazı ve çiçekleri çok seviyordu.»
   - Açıklama: 'Yazı' hem 'yaz mevsimini' hem 'yazıyı' anlatabiliyor; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0201` birebir aynı, ardından `@onarim: 5b774a97a36983ce2543049e936e55f6790dd76a`, sonra gövde.

### Hikâye 5: tohum elsa-0202 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0202
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çeşme', fiil 'koşturmak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: yumuşak karda kardan sarayın ince kulesi yıkıldı | gerçek saraya bakıp kulenin altını geniş yaptı
@tohum: elsa-0202
@degisim: çeşme -> heykel
Limanda yumuşak yumuşak kar yağıyordu. Elsa kıyıda kardan bir saray heykeli yapıyordu. Ama sarayın ince kulesi yamuk durdu ve yana yıkıldı. Yumuşak kar ince kuleyi taşıyamamıştı. Kraliçe Elsa arkasındaki kendi sarayına baktı. O sarayın kulelerinin altı genişti, üstü inceydi. Elsa hemen limanda koşturup bir yığın kar topladı. Yeni kulenin altını geniş yaptı ve karı elleriyle bastırdı. Bu kez kule düz durdu. Kar yağmaya devam etti ama kule yıkılmadı. Elsa kardan sarayına mutlu mutlu yeni kuleler yapmaya devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşak yumuşak kar yağıyordu"
   - Cümle 1: «Limanda yumuşak yumuşak kar yağıyordu.»
   - Açıklama: 'Yumuşak yumuşak' ikilemesi yağmak fiiliyle yanlış kullanılmış; 'lapa lapa' ya da 'yavaş yavaş' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kardan bir saray heykeli"
   - Cümle 2: «Elsa kıyıda kardan bir saray heykeli yapıyordu.»
   - Açıklama: Kardan saray yapılır, 'saray heykeli' kelime yanlış seçilmiş.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir saray heykeli yapıyordu"
   - Cümle 2: «Elsa kıyıda kardan bir saray heykeli yapıyordu.»
   - Açıklama: 'Saray heykeli' yanlış kelime seçimi; 'kardan bir saray' olmalı.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa arkasındaki kendi"
   - Cümle 5: «Kraliçe Elsa arkasındaki kendi sarayına baktı.»
   - Açıklama: Elsa zaten tanıtılmışken unvanıyla yeniden tanıtılıyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yeni kuleler yapmaya devam etti"
   - Cümle 11: «Elsa kardan sarayına mutlu mutlu yeni kuleler yapmaya devam etti.»
   - Açıklama: 'devam etti' art arda iki cümlede gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0202` birebir aynı, `@degisim: çeşme -> heykel` (tutuyorsan), ardından `@onarim: 733ec1903a8b72367a37fe9ac0f6dd3e01341cad`, sonra gövde.

### Hikâye 6: tohum elsa-0203 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0203
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'ay', fiil 'açmak', sıfat 'değişik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: kapıyı hızlı açınca karlar geyiğin başına döküldü | özür dileyip buzdan bir ay yaptı
@tohum: elsa-0203
Elsa sarayının büyük kapısını hızla açtı. Sven kapının önünde bekliyordu ve kapının üstündeki karlar onun başına döküldü. Sven karları silkeledi ve üzgün üzgün geri çekildi. "Özür dilerim, Sven, kapıyı çok hızlı açtım," dedi Elsa. Sonra ellerini birleştirdi ve buzdan değişik bir şekil yaptı. Şekil ince ve parlak bir ay gibiydi. "Bu ay senin için, Sven," dedi Elsa. Sven burnuyla aya dokundu ve sevinçle zıpladı. Sonra Elsa'ya yaklaştı ve ona sokuldu. Elsa bundan sonra sarayın kapısını hep yavaşça açtı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "buzdan değişik bir şekil yaptı"
   - Cümle 5: «Sonra ellerini birleştirdi ve buzdan değişik bir şekil yaptı.»
   - Açıklama: Buzdan ay hediyesi Sven'in başına dökülen kara ya da kapının hızlı açılmasına yönelmiyor, sebepten bağımsız bir teselli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0203` birebir aynı, ardından `@onarim: 49eb25f168a5bedaf1f77bda689400803a9e6940`, sonra gövde.

### Hikâye 7: tohum elsa-0206 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0206
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kızartma', fiil 'sevinmek', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: kar yumuşaktı ve kızartmalar hemen dağıldı | buzdan kızartmalar ve küçük bir tabak yaptı
@tohum: elsa-0206
Bulutlu gökten yavaş yavaş kar yağıyordu. Elsa buz sarayının önünde yemek oyunu oynuyordu. Kardan kızartma yaptı ama kar yumuşaktı ve hepsi hemen dağıldı. Elsa biraz düşündü. Sonra ellerinden ince ve uzun buz çubukları çıkardı. Çubuklar tam patates kızartması gibiydi. Elsa buzdan küçük bir tabak da yaptı. Çubukları tabağa tek tek dizdi. Bu kez hiçbiri bozulmadı ve tabak doldu. Elsa tabağı iki eliyle tuttu ve çok sevindi. Sonra Elsa yemek oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "tam patates kızartması gibiydi"
   - Cümle 6: «Çubuklar tam patates kızartması gibiydi.»
   - Açıklama: Patates kızartması kartın masal krallığı dünyasına ve tohum yasak kategorilerindeki çağdaş öğelere aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0206` birebir aynı, ardından `@onarim: c73891b0af9d7a7ee9ae3f4b01585bc6402d230d`, sonra gövde.

### Hikâye 8: tohum elsa-0207 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0207
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'fincan', fiil 'uzaklaşmak', sıfat 'boş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: renkli ışığa yürüdü ama ışık hep uzaklaştı | fincanda buz yapıp güneşe tuttu
@tohum: elsa-0207
Bir sabah Elsa sarayının önünde bir fincan sıcak süt içti. Birden karşı tepenin üstünde, havada renk renk bir ışık gördü. Ona doğru yürüdü, ama renkli ışık hep ondan uzaklaştı. Elsa durdu ve elindeki boş fincana baktı. Sonra parmağını fincana doğru tuttu ve içini buzla doldurdu. Yuvarlak buzu fincandan çıkardı ve güneşe doğru kaldırdı. Güneşin ışığı buzun içinden geçti. Karın üstüne küçük, renk renk bir ışık düştü. Elsa eğilip renklere yakından baktı. Elsa çok sevindi, çünkü o renkleri artık yakından görebiliyordu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "renkli ışık hep ondan uzaklaştı"
   - Cümle 3: «Ona doğru yürüdü, ama renkli ışık hep ondan uzaklaştı.»
   - Açıklama: Işığın neden uzaklaştığı söylenmiyor ve sorunun sebebi belirsiz kalıyor.
   - Açıklama: Işığın neden uzaklaştığı söylenmiyor; sorunun sebebi verilmiyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yuvarlak buzu fincandan çıkardı ve güneşe doğru kaldırdı"
   - Cümle 6: «Yuvarlak buzu fincandan çıkardı ve güneşe doğru kaldırdı.»
   - Açıklama: Çözüm uzaklaşan ışığa ulaşmaya değil yeni bir ışık yapmaya yöneliyor ve ikiden fazla adım sürüyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "o renkleri artık yakından görebiliyordu"
   - Cümle 10: «Elsa çok sevindi, çünkü o renkleri artık yakından görebiliyordu.»
   - Açıklama: 'Yakından' ve 'renkler' art arda iki cümlede gereksizce tekrarlanıyor.
   - Açıklama: Bir önceki cümledeki 'yakından baktı' hemen tekrarlanıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0207` birebir aynı, ardından `@onarim: c67d8cf300a2e5ecc6aa962b4bf4cbfd0f0c8c1a`, sonra gövde.

### Hikâye 9: tohum elsa-0208 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0208
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'peynir', fiil 'dönmek', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: daldan kar döküldü ve taç karın içine düştü | peynir yediği ağaca geri dönüp tacı buldu
@tohum: elsa-0208
Ormanda karlı ağaçların dalları çok alçaktı. Elsa büyük bir ağacın altında durdu ve nefis bir peynir yedi. Birden daldan başına kar döküldü ve kraliçe tacı karın içine düştü. Elsa başındaki karı eliyle sildi ve tacı görmeden yürüdü. Biraz sonra başına dokundu ve tacın yerinde olmadığını fark etti. Elsa hemen peyniri yediği ağaca geri döndü. Ağacın altındaki karda parlak bir şey vardı. Elsa karı eliyle yavaşça açtı. Elsa tacını orada buldu. Elsa tacın üstündeki karı temizledi ve onu yine başına taktı. Elsa çok sevindi, çünkü kraliçe tacını geri bulmuştu.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "nefis bir peynir yedi"
   - Cümle 2: «Elsa büyük bir ağacın altında durdu ve nefis bir peynir yedi.»
   - Açıklama: 'Nefis' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "nefis bir peynir yedi"
   - Cümle 2: «Elsa büyük bir ağacın altında durdu ve nefis bir peynir yedi.»
   - Açıklama: Ormanda peynir yemek sebepsiz beliren bir ayrıntı ve yalnız ağacı işaretlemek için kuruluyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe tacı karın içine düştü"
   - Cümle 3: «Birden daldan başına kar döküldü ve kraliçe tacı karın içine düştü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız taç sıfatı olarak geçiyor, çözümde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız taç sıfatı olarak geçiyor ve çözümde işe yaramıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa başındaki karı eliyle sildi"
   - Cümle 4: «Elsa başındaki karı eliyle sildi ve tacı görmeden yürüdü.»
   - Açıklama: Elsa başını eliyle sildiği hâlde tacın olmadığını fark etmiyor, sonra başına dokununca hemen fark ediyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa karı eliyle yavaşça açtı"
   - Cümle 8: «Elsa karı eliyle yavaşça açtı.»
   - Açıklama: Kar 'açılmaz'; 'karı eşeledi' ya da 'karı kenara itti' olmalı.
   - Açıklama: 'Karı açtı' kar için yanlış fiil; 'karı eşeledi' ya da 'karı kenara itti' olmalı.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa tacını orada buldu"
   - Cümle 9: «Elsa tacını orada buldu.»
   - Açıklama: 8-11. cümlelerin dördü de 'Elsa' ile başlıyor; ad gereksiz yere tekrarlanıyor.
   - Açıklama: Art arda cümleler gereksiz yere hep 'Elsa' ile başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0208` birebir aynı, ardından `@onarim: 3f13c9d20b1c83d951c1d3177a34c5b3bd466a8a`, sonra gövde.

### Hikâye 10: tohum elsa-0209 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0209
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çanta', fiil 'yaymak', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yerde az kar vardı ve kızak taşlara takıldı | ellerinden kar çıkarıp yola yaydı
@tohum: elsa-0209
@degisim: çanta -> kızak
Bir sabah dağda ince ince kar yağmaya başladı. Elsa buz sarayının önündeki küçük tepeden kızakla kaymak istedi. Ama yerde çok az kar vardı ve kızak taşlara takıldı. Elsa kızaktan indi ve taşlara baktı. Sonra ellerinden bol bol kar çıkardı. Karı taşların üstüne ve bütün yola yaydı. Kar biraz sonra taşlardan daha yüksek oldu. Elsa kızağa yeniden bindi. Bu kez kızak hiç takılmadan aşağıya kadar kaydı. Elsa neşeyle güldü ve kızağı yukarı çekti. Elsa bundan sonra kaymadan önce yola hep dikkatle baktı.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra kaymadan önce yola hep dikkatle baktı"
   - Cümle 11: «Elsa bundan sonra kaymadan önce yola hep dikkatle baktı.»
   - Açıklama: Sorun kar yayarak çözüldüğü halde son ders yola bakmak üzerine; ders yaşanan çözümden çıkmıyor.
   - Açıklama: Sorun yola dikkat etmemekten değil az kardan çıktığı için son ders yaşanan olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0209` birebir aynı, `@degisim: çanta -> kızak` (tutuyorsan), ardından `@onarim: 33355a58d5a5d93efecd1263ca747bf33edccc38`, sonra gövde.

### Hikâye 11: tohum elsa-0210 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0210
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: bir şey yapmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kavanoz', fiil 'doymak', sıfat 'tedbirli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: rüzgar karı kavanozun ağzından uçurdu | kardan adama sırtını rüzgara dönmesini söyledi
@tohum: elsa-0210
@degisim: doymak -> dolmak
Dağda soğuk bir rüzgar esiyordu. Elsa ile Olaf, sarayın penceresine koymak için bir kavanozu karla dolduruyordu. Ama rüzgar karı hep kavanozun ağzından uçuruyordu. "Kavanoz hiç dolmuyor!" dedi Olaf. "Olaf, sırtını rüzgara dön ve kavanozu önünde tut," dedi Kraliçe Elsa. Olaf hemen onun dediğini yaptı. Rüzgar artık Olaf'ın sırtına çarpıyordu. Elsa eliyle kavanoza kar koydu. Bu kez kar uçmadı ve kavanoz çabucak doldu. Olaf kavanozun kapağını sıkıca kapattı. "Teşekkürler, Elsa, pencere çok güzel olacak!" dedi Olaf. Elsa bundan sonra rüzgarda hep tedbirli oldu ve sırtını rüzgara döndü.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 5: «"Olaf, sırtını rüzgara dön ve kavanozu önünde tut," dedi Kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
   - Açıklama: Tohum özelliği 'Kraliçedir; kız kardeşini korur' yalnız unvan olarak geçiyor, kardeşi koruma işe yarar biçimde kullanılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hep tedbirli oldu"
   - Cümle 12: «Elsa bundan sonra rüzgarda hep tedbirli oldu ve sırtını rüzgara döndü.»
   - Açıklama: 'Tedbirli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "rüzgarda hep tedbirli oldu"
   - Cümle 12: «Elsa bundan sonra rüzgarda hep tedbirli oldu ve sırtını rüzgara döndü.»
   - Açıklama: 'Tedbirli' soyut bir kavram ve 3 yaşındaki bir çocuğun bildiği bir kelime değil.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra rüzgarda hep tedbirli oldu"
   - Cümle 12: «Elsa bundan sonra rüzgarda hep tedbirli oldu ve sırtını rüzgara döndü.»
   - Açıklama: Ders olaydan çıkmıyor; sırtını rüzgara dönen Elsa değil Olaf'tı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0210` birebir aynı, `@degisim: doymak -> dolmak` (tutuyorsan), ardından `@onarim: 7f540409bb54faeb04bae26cec6262ce6c9849fe`, sonra gövde.

### Hikâye 12: tohum elsa-0211 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0211
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'şerit', fiil 'gelmek', sıfat 'dikkatli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: saraydaki sesin nereden geldiğini merak etti | kar şeridini izleyip sesi yapan lambayı buldu
@tohum: elsa-0211
Bir sabah Kraliçe Elsa sarayında ince bir ses duydu. Ses büyük salondan geliyordu. Elsa bu sesin nereden geldiğini çok merak etti. Salonun yeri çok kaygandı. Elsa dikkatli adımlarla yavaş yavaş yürüdü. Yerde, pencereye kadar giden ince bir kar şeridi gördü. Pencere açık kalmıştı ve içeri rüzgar giriyordu. Rüzgar tavandaki parlak lambanın küçük parçalarını sallıyordu. Parçalar birbirine değince o ince ses çıkıyordu. Elsa sesi yapan şeyi sonunda bulmuştu. Sonra Elsa pencerenin yanına oturdu ve güzel sesi mutlu mutlu dinledi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa sarayında"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayında ince bir ses duydu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sarayında ince"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayında ince bir ses duydu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kız kardeşini koruma biçiminde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Salonun yeri çok kaygandı"
   - Cümle 4: «Salonun yeri çok kaygandı.»
   - Açıklama: Kaygan zemin bir engel gibi kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0211` birebir aynı, ardından `@onarim: b1b6b4988d245641a25583cefdc98e6ae3ba0609`, sonra gövde.
