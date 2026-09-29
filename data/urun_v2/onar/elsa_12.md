# Editör görevi (onarım): Elsa, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0037 (deneme 2 -> 3)

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
Bir sabah Elsa dağda, buz sarayında oturuyordu. Birden kapıdan garip bir tık tık sesi geldi. Elsa bu sarayın kraliçesiydi ve sesin ne olduğunu hemen bilmek istedi. Kapıyı açtı ama dışarıda kimse yoktu. Karın üstünde küçük kahverengi fıstıklar vardı. Elsa başını kaldırdı ve kapının yanındaki büyük ağacı gördü. Rüzgar ağacın dallarını sallıyordu. Bir fıstık daldan düştü ve kapıya çarptı. Tık tık sesi yine geldi. Elsa güldü. Bu eğlenceli sesi yapan düşen fıstıklardı. Sonra fıstıkları topladı ve sarayında mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 3: «Elsa bu sarayın kraliçesiydi ve sesin ne olduğunu hemen bilmek istedi.»
   - Açıklama: Karttaki kraliçe özelliği sorunun çözümünde hiç işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız anılıyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bu eğlenceli sesi yapan düşen fıstıklardı."
   - Cümle 11: «Bu eğlenceli sesi yapan düşen fıstıklardı.»
   - Açıklama: Özne ile yüklem arasında virgül olmadığı için 'yapan düşen' yan yana gelip cümle zor okunuyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "fıstıkları topladı ve sarayında mutlu mutlu yedi"
   - Cümle 12: «Sonra fıstıkları topladı ve sarayında mutlu mutlu yedi.»
   - Açıklama: Yerden toplanan fıstıkları yemek küçük çocuğun taklit edebileceği boğulma tehlikeli bir davranış.
   - Açıklama: Yerden toplanan bütün fıstıkları yemek küçük çocuk için taklit edilince boğulma riski taşıyan bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0037` birebir aynı, ardından `@onarim: 399990ac21e71877b864a2ba5b09e5fa36c80a85`, sonra gövde.

### Hikâye 2: tohum elsa-0039 (deneme 2 -> 3)

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
@plan: karlı bir çalının altından garip bir ses geldi | buzdan bir kürek yapıp karı kazdı ve sesi buldu
@tohum: elsa-0039
Elsa ile Olaf güneşli bir sabah dağda yürüyordu. Birden karlı bir çalının altından tıp tıp diye bir ses geldi. "Bu ses ne?" diye sordu Olaf. Çalının altı kalın karla doluydu ve hiçbir şey görünmüyordu. Elsa elini salladı ve buzdan küçük bir kürek yaptı. Sonra çalının altındaki karı yavaşça kazdı. Karın altında sararmış, yuvarlak bir yaprak vardı. Çalının dalında küçük bir buz parçası güneşte eriyordu. Buzdan su damlaları yaprağın üstüne düşüyordu. Tıp tıp sesi bu damlalardan geliyordu. "Bu ses bir davul gibi!" dedi Olaf. Sonra Elsa ile Olaf damlaların sesini dinleyip mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Karın altında sararmış, yuvarlak bir yaprak vardı"
   - Cümle 7: «Karın altında sararmış, yuvarlak bir yaprak vardı.»
   - Açıklama: Yaprak kalın karın altındayken damlaların doğrudan yaprağa düşüp ses çıkarması çelişiyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Buzdan su damlaları yaprağın üstüne düşüyordu"
   - Cümle 9: «Buzdan su damlaları yaprağın üstüne düşüyordu.»
   - Açıklama: Yaprak kalın karın altındayken damlaların ona düşüp ses çıkarması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0039` birebir aynı, ardından `@onarim: 2f0848a976f71a86723a934c9f0d38cc4c246082`, sonra gövde.

### Hikâye 3: tohum elsa-0040 (deneme 2 -> 3)

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
@plan: kızağın halatı çözüldü ve iki taşın arasına düştü | buzdan uzun bir çubuk yapıp halatı çekti
@tohum: elsa-0040
Rüzgar esiyordu. Elsa sarayın önünde, ferah bir yerde kızağıyla oynuyordu. Birden rüzgar kızağı itti ve kızağın halatı çözüldü. Kızak iki büyük taşın yanında durdu ama halat yoktu. Elsa her yere baktı. Sonunda iki taşın arasında halatı gördü. Ama taşların arası çok dardı ve eli oraya girmedi. Elsa parmaklarını oynattı ve buzdan uzun bir çubuk yaptı. Çubuğu taşların arasına soktu ve halatı yavaşça çekti. Halat taşların arasından çıktı. Elsa halatı kızağa yine sıkıca bağladı. Elsa çok sevindi, çünkü halatı kurtarmıştı ve oyununa dönebilirdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah bir yerde kızağıyla"
   - Cümle 2: «Elsa sarayın önünde, ferah bir yerde kızağıyla oynuyordu.»
   - Açıklama: 'ferah' kelimesini 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "önünde, ferah bir yerde"
   - Cümle 2: «Elsa sarayın önünde, ferah bir yerde kızağıyla oynuyordu.»
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgar kızağı itti ve kızağın halatı çözüldü"
   - Cümle 3: «Birden rüzgar kızağı itti ve kızağın halatı çözüldü.»
   - Açıklama: Rüzgarın kızağı itmesiyle bağlı halatın çözülüp taşların arasına düşmesi akla yatkın bir sebep değil.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar kızağı itti ve kızağın halatı çözüldü"
   - Cümle 3: «Birden rüzgar kızağı itti ve kızağın halatı çözüldü.»
   - Açıklama: Rüzgarın kızağı itmesiyle bağlı halatın çözülüp taşların arasına düşmesi akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0040` birebir aynı, ardından `@onarim: 7368d1ba8871fb38086c291fdc6262756dac4e90`, sonra gövde.

### Hikâye 4: tohum elsa-0041 (deneme 2 -> 3)

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
@plan: karın altındaki geyiği tanımadı ve ona havuç taktı | ondan özür diledi ve üstündeki karı sildi
@tohum: elsa-0041
@degisim: gül -> havuç
Karlı dağda Elsa sarayının önünde Sven'i arıyordu. Elinde Sven için bir havuç vardı. Kapının yanında karla örtülü büyük bir yığın gördü. Elsa onu tanımadı ve bir kar yığını sandı. Yığını süslemek için havucu ona burun gibi taktı. Birden yığın sallandı ve karlar yere döküldü. Karın altından Sven'in başı çıktı. Sven uyanıktı ve Elsa'ya şaşkın şaşkın bakıyordu. "Özür dilerim, Sven, seni tanımadım," dedi Elsa. Elsa kraliçe pelerinini çıkardı ve Sven'in üstündeki karı sildi. Sven havucu yedi ve sevinçle başını salladı. Sonra ikisi karda mutlu mutlu koştular.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Elsa onu tanımadı ve bir kar yığını sandı"
   - Cümle 4: «Elsa onu tanımadı ve bir kar yığını sandı.»
   - Açıklama: Sorun ancak dördüncü cümlede ortaya çıkıyor ve açık bir sorun olarak söylenmiyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yığını süslemek için havucu ona burun gibi taktı"
   - Cümle 5: «Yığını süslemek için havucu ona burun gibi taktı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü ve beşinci cümlede ortaya çıkıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sven uyanıktı ve Elsa'ya şaşkın şaşkın bakıyordu"
   - Cümle 8: «Sven uyanıktı ve Elsa'ya şaşkın şaşkın bakıyordu.»
   - Açıklama: Uyanık bir geyiğin karın altında kıpırdamadan yığın gibi durması akla yatkın bir sebep değil.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sven uyanıktı ve Elsa'ya şaşkın"
   - Cümle 8: «Sven uyanıktı ve Elsa'ya şaşkın şaşkın bakıyordu.»
   - Açıklama: Uyanık bir geyiğin karla tamamen örtülüp kıpırdamadan durması ve burnuna havuç takılması akla yatkın bir sebep değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçe pelerinini çıkardı"
   - Cümle 10: «Elsa kraliçe pelerinini çıkardı ve Sven'in üstündeki karı sildi.»
   - Açıklama: Tohumdaki özellik 'kız kardeşini korur' iken kraliçelik yalnız pelerin sıfatı olarak geçiyor.
   - Açıklama: Kraliçe özelliği karttaki 'kız kardeşini korur' anlamında değil, yalnız pelerine etiket olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0041` birebir aynı, `@degisim: gül -> havuç` (tutuyorsan), ardından `@onarim: 89f120ca4bd3a340f9390ddfe82364ec283895ae`, sonra gövde.

### Hikâye 5: tohum elsa-0044 (deneme 2 -> 3)

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
@plan: arkadaşı da kaymak istedi ama kızağı yoktu | kızağı paylaşıp onu arkasına oturttu
@tohum: elsa-0044
@degisim: kayık -> kızak
Ormanda hafif bir rüzgar esiyordu. Elsa küçük, açık bir yokuştan kızakla kayıyordu. Olaf da kaymak istedi ama onun kızağı yoktu. Olaf sabırsızdı ve yokuşun dibinde zıplayarak bekliyordu. Kızak aşağıda, Olaf'ın hemen önünde durdu. "Gel, Olaf, bu kızak ikimize de yeter," dedi Elsa. İkisi kızağı yokuşun başına çekti. Elsa kraliçeydi ve arkadaşını korumak için öne oturdu. Olaf onun arkasına yerleşti ve ona sıkıca tutundu. Kızak yavaşça aşağı indi. Olaf kollarını açtı ve kahkahalarla güldü. "Birlikte çok daha eğlenceli!" dedi Olaf. Elsa ile Olaf mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük, açık bir yokuştan"
   - Cümle 2: «Elsa küçük, açık bir yokuştan kızakla kayıyordu.»
   - Açıklama: 'Açık' yokuş için belirsiz ve yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf sabırsızdı ve yokuşun"
   - Cümle 4: «Olaf sabırsızdı ve yokuşun dibinde zıplayarak bekliyordu.»
   - Açıklama: 'Sabırsız' soyut bir kavram ve kartın özellik kelimesi değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve arkadaşını korumak için öne oturdu"
   - Cümle 8: «Elsa kraliçeydi ve arkadaşını korumak için öne oturdu.»
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; burada arkadaşa uygulanıyor ve sorunu çözmüyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve arkadaşını korumak için öne oturdu"
   - Cümle 8: «Elsa kraliçeydi ve arkadaşını korumak için öne oturdu.»
   - Açıklama: Kraliçe olmak öne oturmanın sebebi olarak zorlama ve işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0044` birebir aynı, `@degisim: kayık -> kızak` (tutuyorsan), ardından `@onarim: 06a9fd83205b4e74fcea86917b50fb25d0a37712`, sonra gövde.

### Hikâye 6: tohum elsa-0045 (deneme 2 -> 3)

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
@plan: yumuşak kardan yapılan kule yana devrildi | karı sıkıca bastırıp kulenin önüne duvar ekledi
@tohum: elsa-0045
@degisim: çekirdek -> duvar
Karlı dağda, buzdan sarayın yanında güneş parlıyordu. Elsa karla uzun kuleli, küçük bir kale yapıyordu. Ama kulenin karı çok yumuşaktı ve kule birden yana devrildi. Elsa biraz mutsuz oldu. Sonra karı iki eliyle sıkıca bastırdı ve kuleyi daha sağlam yaptı. Elsa kraliçeydi ve kalesini korumak istedi. Kulenin önüne, rüzgarın geldiği yana, karla kalın bir duvar ekledi. Biraz sonra rüzgar esti ama kule duvarın arkasında dik durdu. Elsa kalesinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "karı sıkıca bastırıp kulenin önüne duvar ekledi"
   - Cümle 0 (plan satırı): «yumuşak kardan yapılan kule yana devrildi | karı sıkıca bastırıp kulenin önüne duvar ekledi»
   - Açıklama: Plan duvarı çözümün parçası sayıyor oysa kule sıkı kar yüzünden düzeldi, duvar sorunla ilgisiz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve kalesini korumak istedi"
   - Cümle 6: «Elsa kraliçeydi ve kalesini korumak istedi.»
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; burada kar kalesine çarpıtılıyor ve çözümde işe yaramıyor.
   - Açıklama: Karttaki özellik kız kardeşini korumak; burada kardan kaleyi korumaya kaydırılmış ve kraliçelik işe yarar biçimde kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve kalesini korumak istedi"
   - Cümle 6: «Elsa kraliçeydi ve kalesini korumak istedi.»
   - Açıklama: Kraliçelik ve korumak isteği önceki olaydan çıkmıyor, duvarı sebepsizce getiriyor.
   - Açıklama: Kraliçelik ve rüzgar duvarı sorundan çıkmıyor; rüzgar daha önce sebep olarak hiç kurulmadı.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kulenin önüne, rüzgarın geldiği yana, karla kalın bir duvar ekledi"
   - Cümle 7: «Kulenin önüne, rüzgarın geldiği yana, karla kalın bir duvar ekledi.»
   - Açıklama: Sorunun sebebi yumuşak kardı; rüzgara karşı duvar sebebe yönelmeyen fazladan bir adım.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "karla kalın bir duvar ekledi"
   - Cümle 7: «Kulenin önüne, rüzgarın geldiği yana, karla kalın bir duvar ekledi.»
   - Açıklama: Sorunun sebebi yumuşak kar iken rüzgar duvarı sebebe yönelmeyen fazladan bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0045` birebir aynı, `@degisim: çekirdek -> duvar` (tutuyorsan), ardından `@onarim: 97a76d5e0675a82a2b6f729217740e7b139eaece`, sonra gövde.

### Hikâye 7: tohum elsa-0047 (deneme 1 -> 2)

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
@plan: tarak elden kayıp derin karın içinde kayboldu | nazikçe yardım istedi ve geyik tarağı karda buldu
@tohum: elsa-0047
Karlı ormanda Elsa, Sven'in tüylerini tarıyordu. Birden tarak elinden kaydı ve kara düştü. Kar çok derindi ve tarak kayboldu. Elsa elleriyle aradı ama tarağı bulamadı. Elsa nazik bir kraliçeydi ve Sven'den yardım istedi. "Sven, tarağı bulmama yardım eder misin?" diye sordu Elsa. Sven burnunu kara soktu ve kokladı. Sonra bir ayağıyla karı kazdı. Tarak karın içinden çıktı. Sven tarağı ağzıyla Elsa'ya getirdi. Elsa gülümsedi ve Sven'in başını okşadı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Elsa çok sevindi, çünkü Sven sayesinde tarağını geri almıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa nazik bir kraliçeydi"
   - Cümle 5: «Elsa nazik bir kraliçeydi ve Sven'den yardım istedi.»
   - Açıklama: Tohumdaki özellik 'kız kardeşini korur' iken kraliçelik nazik olmakla ilişkilendiriliyor, karttaki gibi kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız nazik sıfatıyla etiket olarak geçiyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sven burnunu kara soktu ve kokladı"
   - Cümle 7: «Sven burnunu kara soktu ve kokladı.»
   - Açıklama: Tarağı Elsa değil Sven bulup çıkarıyor; yan karakter sorunu kendisi çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0047` birebir aynı, ardından `@onarim: a8c517d5c88de93dcc79b97ccacb44455c156c59`, sonra gövde.

### Hikâye 8: tohum elsa-0048 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0048
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yemek', fiil 'boyamak', sıfat 'kibar'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: yemek tabakları yumuşak karın içine battı | buzdan bir masa yapıp tabakları üstüne koydu
@tohum: elsa-0048
@degisim: boyamak -> süslemek
Bir sabah Elsa ormanda Anna için bir sürpriz hazırlıyordu. Karın üstüne tabaklarla güzel bir yemek koydu. Ama kar çok yumuşaktı ve tabaklar karın içine battı. Elsa tabakları çıkardı ve biraz düşündü. Sonra elini salladı ve buzdan küçük bir masa yaptı. Masayı çam dallarıyla süsledi. Tabakları masanın üstüne koydu ve bu kez hiçbiri batmadı. Tam o sırada Anna geldi. "Sürpriz, Anna!" dedi Elsa. "Ne güzel bir masa, çok teşekkür ederim!" dedi Anna kibar bir sesle. İki kardeş masada yemeklerini mutlu mutlu yedi. Elsa bundan sonra karda sofra kurunca hep buzdan bir masa yaptı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tabaklarla güzel bir yemek koydu"
   - Cümle 2: «Karın üstüne tabaklarla güzel bir yemek koydu.»
   - Açıklama: 'Tabaklarla yemek koymak' doğal değil; 'tabaklara yemek koyup karın üstüne dizdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0048` birebir aynı, `@degisim: boyamak -> süslemek` (tutuyorsan), ardından `@onarim: fe4d5e3e66ae7db7242b4a923c1d6dda898f2241`, sonra gövde.

### Hikâye 9: tohum elsa-0050 (deneme 1 -> 2)

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
@plan: iki kardeş tek kar aletini aynı anda istedi | sırayla kullanmayı önerdi ve kaleye buzdan kule yaptı
@tohum: elsa-0050
@degisim: yıkanmak -> beklemek
Ormanda Elsa ile Anna kardan bir kale yapıyordu. Ama ellerinde tek bir kar aleti vardı. İkisi de aleti aynı anda istedi. "Önce ben kazacağım!" dedi Anna. Elsa biraz düşündü. "Sırayla kullanalım, Anna, önce sen başla," dedi Elsa. Anna aletle kaleye güzel bir kapı açtı. Elsa da sırasını bekledi. Biraz sonra Anna aleti Elsa'ya verdi. Elsa aletle kaleye küçük bir pencere açtı. Sonra elini salladı ve kalenin üstüne buzdan şapkalı bir kule yaptı. "Kalemiz çok güzel oldu, Elsa!" dedi Anna. Elsa çok sevindi, çünkü sırayla oynayınca kaleyi birlikte bitirmişlerdi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzdan şapkalı bir kule"
   - Cümle 11: «Sonra elini salladı ve kalenin üstüne buzdan şapkalı bir kule yaptı.»
   - Açıklama: Kuleye şapka demek mecazdır; küçük çocuk için somut değil.
   - Açıklama: Kuleye 'şapkalı' demek mecazdır; küçük çocuk için anlaşılmaz.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalenin üstüne buzdan şapkalı bir kule yaptı"
   - Cümle 11: «Sonra elini salladı ve kalenin üstüne buzdan şapkalı bir kule yaptı.»
   - Açıklama: Buzdan kule sıra sorunundan çıkmıyor ve alet paylaşımıyla ilgisi olmayan eklenmiş bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0050` birebir aynı, `@degisim: yıkanmak -> beklemek` (tutuyorsan), ardından `@onarim: 4e3b03c84f0f9fc10fba32455d0a5d7f4957a436`, sonra gövde.

### Hikâye 10: tohum elsa-0051 (deneme 1 -> 2)

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
@plan: yelken rüzgara ters durduğu için kızak kaymadı | susup rüzgarı dinledi ve yelkeni rüzgara çevirdi
@tohum: elsa-0051
Bir sabah Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu. Kızağa uzun bir dal dikmiş ve kraliçe pelerinini yelken yapmıştı. Ama kızak hiç kaymadı, çünkü yelken rüzgara ters duruyordu. Elsa sustu ve rüzgarı dikkatle dinledi. Rüzgar sağ tarafından esiyordu. Elsa yelkeni rüzgara doğru çevirdi. Yelken birden şişti. Kızak düz karın üstünde yavaş yavaş kaymaya başladı. Elsa kızağın içinde oturdu ve güldü. Kızak masmavi gökyüzünün altında sarayın önünde bir tur attı. Elsa çok sevindi, çünkü yeni bir şeyi denemiş ve başarmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe pelerinini yelken yapmıştı"
   - Cümle 2: «Kızağa uzun bir dal dikmiş ve kraliçe pelerinini yelken yapmıştı.»
   - Açıklama: Tohumdaki özellik 'kız kardeşini korur' iken kraliçelik yalnız pelerin sıfatı olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız pelerine etiket olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Rüzgar sağ tarafından esiyordu"
   - Cümle 5: «Rüzgar sağ tarafından esiyordu.»
   - Açıklama: 'Tarafından' iyelik ekinin kimin (Elsa'nın mı kızağın mı) sağını gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0051` birebir aynı, ardından `@onarim: 01811c8ce602b57dd772ad2da71a4cb315ba6bc0`, sonra gövde.
