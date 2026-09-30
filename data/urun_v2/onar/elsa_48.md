# Editör görevi (onarım): Elsa, onarım partisi 48

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar48.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar48.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0140 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0140
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'zincir', fiil 'koklamak', sıfat 'meraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: rüzgar esti ve kağıt zincir ortadan koptu | buzdan kalın halkalar yapıp onları birbirine taktı
@tohum: elsa-0140
@degisim: koklamak -> saymak
Meraklı martılar limanın üstünde ötüyordu. Elsa deniz kıyısında kağıttan uzun bir zincir yapıyordu. Ama birden rüzgar esti ve kağıt zincir ortadan koptu. Hafif halkalar taşların arasına uçuştu. Elsa çok üzüldü, çünkü zinciri bitirmek istiyordu. Bu kez daha sağlam bir zincir yapmak istedi. Ellerinden kalın buz halkaları çıkardı. Halkaları bir, iki, üç diye saydı ve birbirine taktı. On halka olunca zinciri yavaşça havaya kaldırdı. Rüzgar yine esti ama kalın zincir yerinde kaldı. Zincir güneşte pırıl pırıl parladı. Elsa uzun zincirle kıyıda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve kağıt zincir ortadan"
   - Cümle 3: «Ama birden rüzgar esti ve kağıt zincir ortadan koptu.»
   - Açıklama: Tamlama eki eksik; 'kağıt zinciri' ya da 'kağıttan zincir' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "esti ve kağıt zincir"
   - Cümle 3: «Ama birden rüzgar esti ve kağıt zincir ortadan koptu.»
   - Açıklama: Plan satırında tamlama eki eksik; 'kağıt zinciri' ya da 'kağıttan zincir' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0140` birebir aynı, `@degisim: koklamak -> saymak` (tutuyorsan), ardından `@onarim: a12237cf23d535d15f4fbf7e7359ae2dab407981`, sonra gövde.

### Hikâye 2: tohum elsa-0141 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0141
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'brokoli', fiil 'sokulmak', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: buzdan brokolinin ince sapı devrildi | kalın ve kısa yeni bir sap yaptı
@tohum: elsa-0141
@degisim: sokulmak -> gülmek
Bir sabah Elsa deniz kıyısında heyecanlı bir oyun oynuyordu. Buzdan kocaman bir brokoli yapıyordu. Ama brokolinin sapı çok inceydi ve brokoli devrildi. Brokoli taşların üstünde yan yatıyordu. Elsa buna baktı ve güldü. Sonra elini yavaşça oynattı. Bu kez kalın ve kısa bir sap yaptı. Sonra brokolinin başını dikkatle yeni sapın üstüne koydu. Elsa elini çekti ve bekledi. Brokoli hiç sallanmadı. Güneşte pırıl pırıl parladı. Elsa çok sevindi, çünkü buzdan brokoli artık dimdik duruyordu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa buna baktı ve güldü"
   - Cümle 5: «Elsa buna baktı ve güldü.»
   - Açıklama: Brokolinin devrilmesi Elsa'yı hiç üzmüyor; sorun önemsiz kalıyor ve çocuğun önemseyeceği bir hedef kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0141` birebir aynı, `@degisim: sokulmak -> gülmek` (tutuyorsan), ardından `@onarim: 389cda340274f51e336631f366167cf535fd55ca`, sonra gövde.

### Hikâye 3: tohum elsa-0143 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0143
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'örgü', fiil 'tamamlanmak', sıfat 'şirin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: kaydırak geyik için çok dardı | buzla kaydırağı daha geniş yapıp geyikle paylaştı
@tohum: elsa-0143
@degisim: örgü -> kaydırak
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa karı elleriyle düzeltip tepede şirin bir kaydırak yapmıştı. Sven de kaymak istedi, ama kaydırak ona çok dardı. Sven kaydırağın başında üzgün üzgün bekledi. "Gel, Sven, bu kaydırağı paylaşalım," dedi Elsa. Elsa ellerini kaydırağın iki yanına uzattı. Elinden buz çıktı ve kaydırak genişledi. Elsa'nın işi tamamlanınca Sven sevinçle ayağını yere vurdu. Önce Elsa kaydı, sonra Sven dört ayağını açıp aşağı kaydı. Sven karın içine yuvarlandı ve burnundan neşeyle ses çıkardı. "Sıra yine sende, Sven!" dedi Elsa gülerek. Elsa çok mutluydu, çünkü kaydırağını Sven'le paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'nın işi tamamlanınca"
   - Cümle 8: «Elsa'nın işi tamamlanınca Sven sevinçle ayağını yere vurdu.»
   - Açıklama: 'İşi tamamlanınca' 3 yaşındaki çocuk için ağır ve soyut bir anlatım; 'Elsa işini bitirince' daha uygun.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'nın işi tamamlanınca Sven"
   - Cümle 8: «Elsa'nın işi tamamlanınca Sven sevinçle ayağını yere vurdu.»
   - Açıklama: 'İşi tamamlanınca' soyut ve küçük çocuğa ağır bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0143` birebir aynı, `@degisim: örgü -> kaydırak` (tutuyorsan), ardından `@onarim: afaba763f363836249d9051d3d44f59cdddec645`, sonra gövde.

### Hikâye 4: tohum elsa-0144 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0144
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'taş', fiil 'sıralamak', sıfat 'hareketli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: tepeden yuvarlanan taşlar küçük bir fidana çarpıyordu | büyük taşları fidanın önüne sıraladı
@tohum: elsa-0144
Elsa karlı ormanda yürürken tık tık diye bir ses duydu. Elsa bu sesi çok merak etti ve sesin geldiği yere gitti. Küçük bir tepeden hareketli taşlar yuvarlanıyor ve bir fidana çarpıyordu. Ses bu taşlardan geliyordu. Fidanın ince dalları taşlar çarptıkça sallanıyordu. Elsa bir kraliçeydi ve küçük fidanı korumak istedi. Yerdeki büyük taşları tek tek topladı. Sonra onları fidanın önüne yan yana sıraladı. Tepeden yeni bir taş yuvarlandı ve büyük taşlarda durdu. Fidana artık hiç taş çarpmadı. Elsa fidanın yeşil yapraklarına baktı ve çok sevindi. Elsa bundan sonra ormanda bir ses duyunca hemen gidip baktı.
```

**Hakem bulguları (12):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sesin geldiği yere gitti"
   - Cümle 2: «Elsa bu sesi çok merak etti ve sesin geldiği yere gitti.»
   - Açıklama: Elsa tanımadığı bir sesin peşinden tek başına gidiyor, çocuk için taklit edilince tehlikeli.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "hareketli taşlar yuvarlanıyor"
   - Cümle 3: «Küçük bir tepeden hareketli taşlar yuvarlanıyor ve bir fidana çarpıyordu.»
   - Açıklama: Elsa taş yuvarlanan tepenin yanında taş topluyor, taklit edilince tehlikeli.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Küçük bir tepeden hareketli taşlar"
   - Cümle 3: «Küçük bir tepeden hareketli taşlar yuvarlanıyor ve bir fidana çarpıyordu.»
   - Açıklama: 'Hareketli' canlılar için kullanılır; yuvarlanan taşlara uymuyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tepeden hareketli taşlar yuvarlanıyor"
   - Cümle 3: «Küçük bir tepeden hareketli taşlar yuvarlanıyor ve bir fidana çarpıyordu.»
   - Açıklama: 'Hareketli' taşlar için yanlış anlamda kullanılmış; gereksiz ve uygunsuz sıfat.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Küçük bir tepeden hareketli taşlar yuvarlanıyor"
   - Cümle 3: «Küçük bir tepeden hareketli taşlar yuvarlanıyor ve bir fidana çarpıyordu.»
   - Açıklama: Taşların neden sürekli tepeden yuvarlandığı hiç söylenmiyor.
   - Açıklama: Taşların neden durmadan tepeden yuvarlandığı söylenmiyor; sorunun sebebi yok.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve küçük fidanı korumak istedi"
   - Cümle 6: «Elsa bir kraliçeydi ve küçük fidanı korumak istedi.»
   - Açıklama: Kartın özellik alanı kraliçeliği kız kardeşini korumak olarak veriyor; burada fidana uygulanıyor ve çözüme katkısı yok.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yuvarlandı ve büyük taşlarda durdu"
   - Cümle 9: «Tepeden yeni bir taş yuvarlandı ve büyük taşlarda durdu.»
   - Açıklama: Hal eki yanlış; 'büyük taşlara çarpıp durdu' olmalı.
8. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve büyük taşlarda durdu"
   - Cümle 9: «Tepeden yeni bir taş yuvarlandı ve büyük taşlarda durdu.»
   - Açıklama: Hal eki yanlış; 'büyük taşların önünde durdu' olmalı.
9. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bir ses duyunca hemen gidip baktı"
   - Cümle 12: «Elsa bundan sonra ormanda bir ses duyunca hemen gidip baktı.»
   - Açıklama: Son cümle bilinmeyen seslere hemen gitmeyi örnek davranış olarak veriyor.
   - Açıklama: Taş yuvarlanan tepeye bilinmeyen sesin peşinden gitmek taklit edilince tehlikeli bir davranış olarak örnek gösteriliyor.
10. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "duyunca hemen gidip baktı"
   - Cümle 12: «Elsa bundan sonra ormanda bir ses duyunca hemen gidip baktı.»
   - Açıklama: 'Bundan sonra' alışkanlık bildirdiği için fiil 'gidip bakardı' olmalı; '-dı' ile uyumsuz.
11. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra ormanda bir ses duyunca"
   - Cümle 12: «Elsa bundan sonra ormanda bir ses duyunca hemen gidip baktı.»
   - Açıklama: Son ders cümlesi fidanı koruma olayından değil, ses merakından çıkıyor ve hedefe bağlı sıcak bir kapanış vermiyor.
12. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra ormanda bir ses duyunca hemen gidip baktı"
   - Cümle 12: «Elsa bundan sonra ormanda bir ses duyunca hemen gidip baktı.»
   - Açıklama: Son cümle fidanı koruma hedefine değil sese bakmaya dönüyor; kapanış olaydan çıkan bir ders vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0144` birebir aynı, ardından `@onarim: 394314ccc5cf2e608bf813b173e883d116e52bca`, sonra gövde.

### Hikâye 5: tohum elsa-0147 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0147
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sırayla oynamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'düğme', fiil 'giymek', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: ikisi de eski paltoyu aynı anda giymek istedi | buzdan bir yıldız yaptı ve yıldızı sırayla verdi
@tohum: elsa-0147
Elsa ile Olaf dağda, buz sarayının önünde oynuyordu. Giyinme oyunu için eskimiş kırmızı bir palto getirmişlerdi. Ama ikisi de paltoyu aynı anda giymek istedi. Olaf paltonun bir kolunu çekti, Elsa öbür kolunu tuttu. Elsa biraz düşündü. Sonra elinden buz çıktı ve küçük bir buz yıldızı oldu. Yıldızı tutan paltoyu giyecekti. Elsa yıldızı önce Olaf'a verdi. Olaf paltoyu giydi ve büyük düğmeleri tek tek ilikledi. Palto ona çok büyük geldi ve Olaf karda komik adımlarla yürüdü. Sonra Olaf yıldızı Elsa'ya uzattı. Elsa da paltoyu giydi ve iki kez döndü. Elsa çok mutlu oldu, çünkü ikisi de paltoyu sırayla giymişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yıldızı sırayla verdi"
   - Cümle 0 (plan satırı): «ikisi de eski paltoyu aynı anda giymek istedi | buzdan bir yıldız yaptı ve yıldızı sırayla verdi»
   - Açıklama: Yıldız tek kişiye bir kez verildi, sonra Olaf uzattı; 'sırayla verdi' anlamca yanlış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Yıldızı tutan paltoyu giyecekti"
   - Cümle 7: «Yıldızı tutan paltoyu giyecekti.»
   - Açıklama: Özne eksik; 'tutan paltoyu' tamlama gibi okunuyor, 'Yıldızı tutan kişi paltoyu giyecekti' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük düğmeleri tek tek ilikledi"
   - Cümle 9: «Olaf paltoyu giydi ve büyük düğmeleri tek tek ilikledi.»
   - Açıklama: 'İliklemek' 3 yaşındaki çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0147` birebir aynı, ardından `@onarim: 4906f28122b7e21542c75dcae141d820b0cf8979`, sonra gövde.

### Hikâye 6: tohum elsa-0149 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0149
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'maske', fiil 'karışmak', sıfat 'sakar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: rüzgar beyaz maskeyi uçurdu ve maske karla karıştı | kardaki uzun çizginin yanından yürüyüp maskeyi buldu
@tohum: elsa-0149
@degisim: sakar -> kocaman
Elsa karlı ormanda saraya doğru yürüyordu. Elinde şenlik için kocaman, beyaz bir maske vardı. Elsa kraliçeydi ve saraydaki şenliği o açacaktı. Ama birden rüzgar esti ve maske elinden uçtu. Beyaz maske karın içine düştü ve karla karıştı. Elsa maskeyi beyaz karda göremedi. Sonra durdu ve yerdeki kara dikkatle baktı. Karda uzun ince bir çizgi fark etti. Maske kayarken karda bu çizgiyi bırakmıştı. Elsa çizginin yanından yavaşça yürüdü. Çizgi büyük bir ağacın dibinde bitti. Maske de oradaydı. Elsa maskeyi aldı ve şenliğe mutlu mutlu koştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "saraydaki şenliği o açacaktı"
   - Cümle 3: «Elsa kraliçeydi ve saraydaki şenliği o açacaktı.»
   - Açıklama: 'Şenliği açmak' küçük çocuk için soyut ve mecazlı bir anlatım.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve saraydaki şenliği o açacaktı"
   - Cümle 3: «Elsa kraliçeydi ve saraydaki şenliği o açacaktı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız arka plan bilgisi olarak geçiyor, maskeyi bulmada işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve saraydaki şenliği"
   - Cümle 3: «Elsa kraliçeydi ve saraydaki şenliği o açacaktı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama birden rüzgar esti ve maske elinden uçtu"
   - Cümle 4: «Ama birden rüzgar esti ve maske elinden uçtu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede ortaya çıkıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "düştü ve karla karıştı"
   - Cümle 5: «Beyaz maske karın içine düştü ve karla karıştı.»
   - Açıklama: Maske karla karışmaz; 'karda kayboldu' anlamında yanlış fiil kullanılmış.
   - Açıklama: Maske karla karışmaz; 'karıştı' burada mecazlı ve yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0149` birebir aynı, `@degisim: sakar -> kocaman` (tutuyorsan), ardından `@onarim: 02e4ca1661919dcbfc5bf97dfc0b31ea72591125`, sonra gövde.

### Hikâye 7: tohum elsa-0150 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0150
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'bisküvi', fiil 'silmek', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: kaydırak kısaydı ve bisküvi tabağa gelmeden düştü | elinden çıkan buzla kaydırağı tabağa kadar uzattı
@tohum: elsa-0150
Limanda Elsa buzdan kısa bir kaydırak ve bir tabak yapmıştı. Bisküviler kaydıraktan kayıp tabağa düşecekti. Ama kaydırak kısaydı ve ilk bisküvi tabağa gelmeden yere düştü. Bisküvi karlı yerde ıslandı. Elsa ıslak bisküviyi kenara koydu ve biraz düşündü. Sonra elini kaydırağın ucuna doğru tuttu. Elinden buz çıktı ve kaydırak tabağa kadar uzadı. Elsa uzun kaydırağın üstündeki karı eliyle sildi. Sonra cebinden yeni bir bisküvi çıkardı ve yukarıdan bıraktı. Bisküvi hızla kaydı ve tam tabağa düştü. Elsa sevinçle güldü ve bisküviyi yedi. Sonra limanda oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Limanda Elsa buzdan kısa bir kaydırak"
   - Cümle 1: «Limanda Elsa buzdan kısa bir kaydırak ve bir tabak yapmıştı.»
   - Açıklama: Buz gücü kartın özellik alanındaki gibi bir kez değil, 1. ve 7. cümlede iki ayrı kez kullanılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "uzun kaydırağın üstündeki karı eliyle sildi"
   - Cümle 8: «Elsa uzun kaydırağın üstündeki karı eliyle sildi.»
   - Açıklama: Kaydırağın üstündeki kar sebepsiz beliriyor ve olaya hiçbir şey katmıyor.
   - Açıklama: Yeni uzatılan kaydırakta sebepsiz kar beliriyor ve bu ayrıntı olaya bir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0150` birebir aynı, ardından `@onarim: f426a1f3fb5e95162745c11d745b22964b4200bf`, sonra gövde.

### Hikâye 8: tohum elsa-0151 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0151
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yeni bir şeyi denemek
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tutkal', fiil 'yarışmak', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: geyik dalgaların sesini işaret sandı ve erken koştu | kağıttan bir bayrak yaptı ve onu yukarı kaldırdı
@tohum: elsa-0151
Bir sabah Elsa ile Sven limanda ilk kez yarışacaktı. Elsa kraliçe olduğu için yarışta işareti o verecekti. Ama limanda dalgalar çok gürültülüydü. Çevik Sven dalgaların sesini işaret sandı ve erken koştu. Elsa, Sven'i yeniden yanına çağırdı. Elsa'nın cebinde mektup için kırmızı bir kağıt ve tutkal vardı. Elsa kağıdı tutkalla bir dala yapıştırdı ve küçük bir bayrak yaptı. "Sven, bu bayrak kalkınca koşacağız," dedi Elsa. Sven bu kez yerinden kıpırdamadan bekledi. Elsa bayrağı yukarı kaldırdı ve ikisi birlikte koştu. Sven yolun sonuna ilk vardı ve sevinçle zıpladı. Elsa gülerek arkasından geldi. Elsa çok sevindi, çünkü ilk yarışları çok güzel olmuştu.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçe olduğu için yarışta işareti o verecekti"
   - Cümle 2: «Elsa kraliçe olduğu için yarışta işareti o verecekti.»
   - Açıklama: Tohum özelliği 'Kraliçedir; kız kardeşini korur' sorunun çözümünde işe yaramıyor, kardeş koruma yok.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "dalgaların sesini işaret sandı ve erken koştu"
   - Cümle 4: «Çevik Sven dalgaların sesini işaret sandı ve erken koştu.»
   - Açıklama: Asıl sorun olan Sven'in erken koşması ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Çevik Sven dalgaların sesini işaret sandı ve erken koştu"
   - Cümle 4: «Çevik Sven dalgaların sesini işaret sandı ve erken koştu.»
   - Açıklama: Asıl sorun olan Sven'in erken koşması ilk üç cümlede değil dördüncü cümlede söyleniyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "cebinde mektup için kırmızı bir kağıt ve tutkal vardı"
   - Cümle 6: «Elsa'nın cebinde mektup için kırmızı bir kağıt ve tutkal vardı.»
   - Açıklama: Kağıt ve tutkal çözüm gerektiği anda sebepsizce beliriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa'nın cebinde mektup için kırmızı bir kağıt ve tutkal vardı"
   - Cümle 6: «Elsa'nın cebinde mektup için kırmızı bir kağıt ve tutkal vardı.»
   - Açıklama: Kağıt ve tutkal önceden kurulmadan tam çözüm gerektiğinde sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0151` birebir aynı, ardından `@onarim: 583bb14f4e6966bbc8fe7f024f8c7116e58c09c3`, sonra gövde.

### Hikâye 9: tohum elsa-0153 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0153
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'ağaç', fiil 'oynatmak', sıfat 'hareketsiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: ikisi de heykel oyununda saymak istedi | kardan adamın başına kar yağdırdı ve sırayla saydılar
@tohum: elsa-0153
Ormanda hafif bir rüzgar esiyordu. Elsa ile Olaf büyük bir ağacın yanında heykel oyunu oynuyordu. Ama ikisi de ağaca dönüp saymak istedi. "Ben sayacağım!" dedi Olaf. "Kar kimin başına yağarsa, ilk o sayar," dedi Elsa. Sonra elini havaya kaldırdı ve elinden buz ve kar çıktı. Rüzgar karı taşıdı ve kar Olaf'ın başına yağdı. Olaf sevinçle ağaca döndü ve saydı. Elsa kollarını oynattı ve yürüdü. Olaf dönünce Elsa hareketsiz durdu. Sonra sıra Elsa'ya geldi ve o da ağaca döndü. Bu kez Olaf durmaya çalıştı ama havuç burnu kıpırdadı. Elsa çok mutluydu, çünkü sırayla oynadıkları için ikisi de saymıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kez Olaf durmaya çalıştı ama havuç burnu kıpırdadı"
   - Cümle 12: «Bu kez Olaf durmaya çalıştı ama havuç burnu kıpırdadı.»
   - Açıklama: Olaf'ın kıpırdaması oyunda bir sonuca bağlanmıyor ve havada kalan işlevsiz bir olay.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa çok mutluydu, çünkü sırayla oynadıkları için"
   - Cümle 13: «Elsa çok mutluydu, çünkü sırayla oynadıkları için ikisi de saymıştı.»
   - Açıklama: 'Çünkü' ile 'için' aynı cümlede iki kez sebep bildiriyor; biri fazla.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0153` birebir aynı, ardından `@onarim: 5e1b1cb04fb93a94f53355f0cc9ec9dc2c73fbef`, sonra gövde.

### Hikâye 10: tohum elsa-0154 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0154
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sırayla oynamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çamur', fiil 'büyümek', sıfat 'elmalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: ikisi topu kendine çekti ve top ikiye ayrıldı | sırayla itmeyi söyledi ve top büyüdü
@tohum: elsa-0154
@degisim: çamur -> kar
Elsa ile Kristoff dağda, buz sarayının önünde oynuyordu. Elmalı turtayı koymak için kardan büyük bir masa yapacaklardı. Ama ikisi de kar topunu kendine doğru çekti ve top ikiye ayrıldı. Elsa hemen yeni ve küçük bir top yaptı. Elsa kraliçe olduğu için sırayı o söyledi. "Kristoff, sen on adım it, sonra ben," dedi Elsa. Kristoff topu on adım itti ve top büyüdü. Sonra Elsa itti ve top daha da büyüdü. Sırayla ittiler ve top kocaman oldu. Kristoff turtayı topun üstüne koydu. "Bak, sırayla yaptık ve masa hazır, Kristoff!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sırayı o söyledi"
   - Cümle 5: «Elsa kraliçe olduğu için sırayı o söyledi.»
   - Açıklama: 'Sırayı söylemek' doğal değil; 'sırayı o belirledi' anlamı kastediliyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçe olduğu için sırayı o söyledi"
   - Cümle 5: «Elsa kraliçe olduğu için sırayı o söyledi.»
   - Açıklama: Kraliçe özelliği karttaki gibi (kız kardeşini korur) değil, buyurma yetkisi olarak kullanılıyor.
   - Açıklama: Kartın özellikler alanındaki kraliçe özelliği kız kardeşi korumaktır; burada arkadaşına emir verme yetkisi olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0154` birebir aynı, `@degisim: çamur -> kar` (tutuyorsan), ardından `@onarim: 530e6598a5a48e8b308477de6bba4ce8b8786443`, sonra gövde.

### Hikâye 11: tohum elsa-0155 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0155
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'halı', fiil 'durdurmak', sıfat 'ılık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: ılık güneş sarayın içini ıslattı ve geyik kaydı | yere halı serdi ve geyiğe halıyı gösterdi
@tohum: elsa-0155
Bir sabah dağda ılık bir güneş vardı. Sven, Elsa'nın buz sarayına oynamaya gelmişti. Ama güneş yüzünden sarayın içi ıslak ve kaygandı. Sven içeri girince ayakları kaydı ve kendini durduramadı. Sonunda duvarın yanında yavaşça durdu. Elsa sarayın kraliçesiydi ve Sven'i korumak istedi. Hemen salonun köşesindeki uzun, yumuşak halıyı getirdi. Halıyı kapıdan salona kadar yere serdi. Sonra Sven'e elini kaldırıp halıyı gösterdi. Sven halıya dikkatle bastı. Ayakları bu kez hiç kaymadı. Sven halının üstünde rahatça yürüdü ve başını salladı. Elsa çok sevindi, çünkü Sven artık sarayda hiç kaymıyordu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ılık güneş sarayın içini ıslattı"
   - Cümle 0 (plan satırı): «ılık güneş sarayın içini ıslattı ve geyik kaydı | yere halı serdi ve geyiğe halıyı gösterdi»
   - Açıklama: Güneş ıslatmaz; buzu eritir, fiil öznesine uymuyor.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "ayakları kaydı ve kendini durduramadı"
   - Cümle 4: «Sven içeri girince ayakları kaydı ve kendini durduramadı.»
   - Açıklama: Kaygan zeminde kontrolsüz kayma düşme ve yaralanma tehlikesi sahneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0155` birebir aynı, ardından `@onarim: 02dc9ecdfa801919713f4a346bbb16b656c4d6ee`, sonra gövde.

### Hikâye 12: tohum elsa-0157 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0157
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: sırayla oynamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'dondurma', fiil 'büyütmek', sıfat 'cesur'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: ikisi topu aynı anda itti ve top dağıldı | sırayla yuvarlamayı söyledi
@tohum: elsa-0157
@degisim: cesur -> kocaman
Bir sabah Elsa ile Kristoff limanda kardan bir dondurma yapıyordu. İkisi de kar topunu aynı anda itti. Top ikiye ayrıldı ve yere dağıldı. "Önce ben yapacağım!" dedi Kristoff. Elsa kraliçe olduğu için sırayı o söyledi. "Kristoff, sen üç kez yuvarla, sonra ben," dedi Elsa. Kristoff başını salladı ve güldü. Kristoff yeni bir topu üç kez yuvarladı. Sonra sıra Elsa'ya geldi ve o da üç kez yuvarladı. İkisi sırayla topu biraz daha büyüttü. Sonunda kocaman, yuvarlak bir dondurma topu oldu. Elsa ile Kristoff yeni toplar yapmaya sırayla ve mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sırayı o söyledi"
   - Cümle 5: «Elsa kraliçe olduğu için sırayı o söyledi.»
   - Açıklama: 'Sırayı söylemek' yanlış kullanım; 'sırayı o belirledi' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçe olduğu için sırayı o söyledi"
   - Cümle 5: «Elsa kraliçe olduğu için sırayı o söyledi.»
   - Açıklama: Sıra kararı sorunun sebebinden değil, figürün kraliçe olmasından sebepsizce çıkarılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0157` birebir aynı, `@degisim: cesur -> kocaman` (tutuyorsan), ardından `@onarim: e155140c6c361f9054298ccad64621c4dab2a5bf`, sonra gövde.
