# Editör görevi (onarım): Elsa, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0047 (deneme 5 -> 6)

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
Karlı ormanda Kraliçe Elsa, Sven'in tüylerini tarıyordu. Birden tarak elinden kaydı ve kara düştü. Kar çok derindi ve tarak kayboldu. Elsa elleriyle aradı ama tarağı bulamadı. "Sven, tarağı bulmama yardım eder misin?" diye nazik bir sesle sordu Elsa. Sven burnunu kara soktu ve kokladı. Bir yerde durdu ve ayağıyla karı gösterdi. Elsa orayı kazdı ve tarağı karın içinden çıkardı. Elsa gülümsedi ve Sven'in başını okşadı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Elsa çok sevindi, çünkü yardım isteyince tarağını bulmuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Karlı ormanda Kraliçe Elsa"
   - Cümle 1: «Karlı ormanda Kraliçe Elsa, Sven'in tüylerini tarıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Karlı ormanda Kraliçe Elsa, Sven'in"
   - Cümle 1: «Karlı ormanda Kraliçe Elsa, Sven'in tüylerini tarıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa gülümsedi ve Sven'in"
   - Cümle 9: «Elsa gülümsedi ve Sven'in başını okşadı.»
   - Açıklama: Elsa adı art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0047` birebir aynı, ardından `@onarim: a55092cf07629d0b29fc030de4abb37ed01b51f0`, sonra gövde.

### Hikâye 2: tohum elsa-0051 (deneme 5 -> 6)

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
Bir sabah Kraliçe Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu. Kızağa uzun bir dal dikmiş ve pelerinini yelken yapmıştı. Ama kızak hiç kaymadı, çünkü yelken rüzgara ters duruyordu. Sarayın tepesinde bir bayrak vardı. Elsa bayrağa baktı ve rüzgarın sağdan estiğini gördü. Sonra yelkeni rüzgara doğru çevirdi. Yelken birden şişti. Kızak düz karın üstünde yavaş yavaş kaymaya başladı. Elsa kızağın içinde oturdu ve güldü. Kızak masmavi gökyüzünün altında sarayın yanından geçti. Elsa çok sevindi, çünkü yeni bir şeyi denemiş ve başarmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa dağda"
   - Cümle 1: «Bir sabah Kraliçe Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümüne yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0051` birebir aynı, `@degisim: susmak -> bakmak` (tutuyorsan), ardından `@onarim: 38ad96a46d00ac382d5765f7d6c50b985cf98480`, sonra gövde.

### Hikâye 3: tohum elsa-0052 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0052
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yağmurluk', fiil 'çalışmak', sıfat 'enerjik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: önüne bakmadan koştu ve havuçları karda dağıttı | özür diledi ve havuçları bulup buzdan kaseye koydu
@tohum: elsa-0052
@degisim: yağmurluk -> havuç
Karlı ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile enerjik Sven, karın üstüne dizili havuçların yanında koşup oynuyordu. Elsa önüne bakmadan koştu ve havuçları karın içine dağıttı. Sven karı kokladı ve üzgün bir ses çıkardı. "Özür dilerim, Sven, havuçlarını ben dağıttım," dedi Elsa. Sonra ikisi havuçları bulmak için birlikte çalıştı. Sven burnuyla, Elsa da elleriyle onları tek tek buldu. Havuçlar yine kaybolmasın diye Elsa buzdan bir kase yaptı. Havuçları kaseye koydu ve Sven'in önüne bıraktı. Sven başını Elsa'ya sürttü ve bir havuç yedi. Elsa bundan sonra ormanda koşarken hep önüne baktı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Havuçlar yine kaybolmasın diye Elsa buzdan bir kase yaptı"
   - Cümle 8: «Havuçlar yine kaybolmasın diye Elsa buzdan bir kase yaptı.»
   - Açıklama: Çözüm özür, havuçları arama ve buzdan kase yapma olarak üç adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0052` birebir aynı, `@degisim: yağmurluk -> havuç` (tutuyorsan), ardından `@onarim: e1800b590015431836d132223d3b82e0f25e08c9`, sonra gövde.

### Hikâye 4: tohum elsa-0053 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Kristoff
@tohum: elsa-0053
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'dolap', fiil 'denemek', sıfat 'çabuk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | şato | Kristoff
@plan: acele edince eldivenleri bir dolaba koydu ve unuttu | özür diledi ve dolapları tek tek açtı
@tohum: elsa-0053
@degisim: denemek -> açmak
Dışarıda kar sessizce yağıyordu. Elsa sarayın kraliçesiydi ve salonu çabuk çabuk topluyordu. Acele edince Kristoff'un eldivenlerini bir dolaba koydu ve bunu unuttu. Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı. "Elsa, eldivenlerimi gördün mü?" diye sordu Kristoff. "Özür dilerim, Kristoff, onları ben bir dolaba koydum," dedi Elsa. Ama salonda çok dolap vardı ve Elsa hangisine koyduğunu bilmiyordu. Elsa dolapları tek tek açtı. Eldivenler kapının yanındaki küçük dolaptaydı! Elsa eldivenleri Kristoff'a verdi. "Teşekkürler, Elsa, hadi şimdi birlikte dışarıda oynayalım!" dedi Kristoff.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa sarayın kraliçesiydi ve salonu"
   - Cümle 2: «Elsa sarayın kraliçesiydi ve salonu çabuk çabuk topluyordu.»
   - Açıklama: Tohumdaki özellik kraliçe (kız kardeşini korur) yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Kraliçe özelliği yalnız anılıyor, karttaki gibi kız kardeşini korumak için ve işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0053` birebir aynı, `@degisim: denemek -> açmak` (tutuyorsan), ardından `@onarim: 5618273a7f5ad00612c54c442c7d404a2c407f7b`, sonra gövde.

### Hikâye 5: tohum elsa-0055 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0055
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yumurta', fiil 'bölmek', sıfat 'kısa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: küçük yuva insanların geçtiği yolun hemen yanındaydı | taşları yuvanın önüne dizdi ve kısa bir duvar yaptı
@tohum: elsa-0055
@degisim: bölmek -> dizmek
Limanda hafif bir rüzgar esiyordu. Kraliçe Elsa kıyıda yürürken taşların arasında küçük bir yuva gördü. Yuvada üç küçük yumurta vardı, ama yuva yolun hemen yanındaydı. Yoldan geçen insanlar yumurtaları kırabilirdi. Elsa yuvaya elini sürmedi. Kıyıdan düz taşlar topladı ve onları yuvanın önüne yan yana dizdi. Yuvanın önünde kısa ama sağlam bir duvar oldu. Elsa yuvaya bir kez daha baktı ve yumurtaları saydı. Elsa çok sevindi, çünkü üç yumurta da artık güvendeydi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kıyıda yürürken"
   - Cümle 2: «Kraliçe Elsa kıyıda yürürken taşların arasında küçük bir yuva gördü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde (kız kardeşini koruma) kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0055` birebir aynı, `@degisim: bölmek -> dizmek` (tutuyorsan), ardından `@onarim: 378717347487392df87eb16af99fde1070c1ede9`, sonra gövde.

### Hikâye 6: tohum elsa-0056 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0056
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tartı', fiil 'alkışlamak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: zıplamayı izlemeyi unuttu ve arkadaşını dışarıda bıraktı | dışarı koşup özür diledi ve zıplamayı alkışladı
@tohum: elsa-0056
@degisim: tartı -> pencere
Elsa buzdan sarayının önünde Sven ile oynuyordu. Sven sağlam bacaklarıyla karda yüksek yüksek zıplıyordu. Ama Elsa su içmek için saraya girdi ve Sven'e bakmayı unuttu. Sven karda yalnız kaldı ve başını öne eğdi. Elsa pencereden baktı ve Sven'in üzgün olduğunu gördü. Kraliçe Elsa hemen dışarı koştu. Sven'e sarıldı ve ondan özür diledi. Sonra karın üstüne oturdu ve Sven'i izledi. Sven yeniden zıpladı ve bu kez daha yükseğe çıktı. Elsa onu gülerek alkışladı. Sven de başını sevinçle Elsa'ya sürttü. Elsa çok sevindi, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen dışarı koştu"
   - Cümle 6: «Kraliçe Elsa hemen dışarı koştu.»
   - Açıklama: Zaten tanıtılmış Elsa unvanla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen dışarı koştu"
   - Cümle 6: «Kraliçe Elsa hemen dışarı koştu.»
   - Açıklama: Tohumdaki özellik kraliçe (kız kardeşini korur) yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0056` birebir aynı, `@degisim: tartı -> pencere` (tutuyorsan), ardından `@onarim: 82c20ffc83643204a0f15afbf1a2f497ddc9e203`, sonra gövde.

### Hikâye 7: tohum elsa-0057 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0057
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'trompet', fiil 'küçültmek', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: rüzgar esti ve trompetin içine kar doldu | trompeti ters çevirip salladı ve karı döktü
@tohum: elsa-0057
@degisim: küçültmek -> sallamak
Dağın tepesinde Elsa, ışıltılı oyuncak trompetiyle bir ses oyunu oynuyordu. Kraliçe trompeti her çaldığında, ses dağlardan geri geliyordu. Ama birden rüzgar esti ve trompetin içine kar doldu. Elsa yine üfledi, ama trompetten hiç ses çıkmadı. Dağlardan da hiç ses gelmedi. Elsa trompetin içine baktı ve karı gördü. Trompeti ters çevirdi ve iki kez salladı. Bütün kar yere döküldü. Elsa bir kez daha üfledi ve trompet yüksek bir ses çıkardı. Ses dağlardan geri geldi ve Elsa güldü. Elsa bundan sonra rüzgar esince trompetinin ağzını eliyle kapattı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe trompeti her çaldığında"
   - Cümle 2: «Kraliçe trompeti her çaldığında, ses dağlardan geri geliyordu.»
   - Açıklama: Elsa'ya birden 'Kraliçe' denmesi yeni biri tanıtılıyormuş gibi belirsizlik yaratıyor.
   - Açıklama: Elsa aniden 'Kraliçe' diye anılıyor; bu adın kimi gösterdiği çocuk için belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe trompeti her çaldığında"
   - Cümle 2: «Kraliçe trompeti her çaldığında, ses dağlardan geri geliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0057` birebir aynı, `@degisim: küçültmek -> sallamak` (tutuyorsan), ardından `@onarim: f1c9d2c57490318dceb28b2ab47525af5e5224b2`, sonra gövde.

### Hikâye 8: tohum elsa-0058 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0058
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yeni bir şeyi denemek
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'zil', fiil 'yoğurmak', sıfat 'yavaş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: kar çok kuru olduğu için kar topu dağıldı | yardım istedi ve karı iyice yoğurdu
@tohum: elsa-0058
Bir sabah Kraliçe Elsa sarayından karlı ormana küçük bir zil getirdi. Kristoff zili bir dala astı. Elsa zili kar topuyla ilk kez çalmayı denedi ama kar çok kuruydu. Top zile varmadan havada dağıldı. "Kristoff, bana yardım eder misin?" diye sordu Elsa. "Bu kar çok kuru, Elsa, onu ellerinde yavaş yavaş yoğur," dedi Kristoff. Elsa karı iki eliyle sıkıca yoğurdu. Bu kez top sağlam oldu. Elsa topu dala doğru fırlattı. Top zile çarptı ve zil çın çın çaldı. Kristoff sevinçle ellerini çırptı. "Harika, Elsa, zili çaldın!" dedi Kristoff. Sonra ikisi sırayla zili çalarak mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa sarayından"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayından karlı ormana küçük bir zil getirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0058` birebir aynı, ardından `@onarim: 25e9172e49b583ce5a09909d5dd4825c6f464d89`, sonra gövde.

### Hikâye 9: tohum elsa-0059 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0059
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'erik', fiil 'paketlemek', sıfat 'kuru'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: yürürken bir ses geldi ve paket hafifledi | delikten düşen erikleri buldu ve buzdan kutuya koydu
@tohum: elsa-0059
Bir sabah Elsa limanda kuru erikleri paketledi. Onları deniz kenarında yemek istiyordu. Ama tahta yolda yürürken paket hafifledi, çünkü içindeki erikler azalmıştı. Arkasından "tık, tık" diye bir ses geliyordu. Elsa durdu ve arkasına baktı. Yolda kuru erikler duruyordu. Paketin altında küçük bir delik vardı. Erikler bu delikten düşüyor ve tahtaya çarpınca ses çıkarıyordu. Elsa geri yürüdü ve yerdeki erikleri topladı. Ama paket delikti ve erikler yine düşecekti. Elsa elini salladı ve buzdan küçük bir kutu yaptı. Erikleri kutuya koydu ve kapağını kapattı. Artık hiçbir erik düşmedi. Elsa deniz kenarında bir taşa oturdu ve erikleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ama paket delikti"
   - Cümle 10: «Ama paket delikti ve erikler yine düşecekti.»
   - Açıklama: 'Delik' sıfat gibi kullanılmış; 'paket delikliydi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0059` birebir aynı, ardından `@onarim: 7e1e95e90684a962b55e00d98123a280313d9e1f`, sonra gövde.

### Hikâye 10: tohum elsa-0060 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0060
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'pilav', fiil 'dikmek', sıfat 'minik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kar yüzünden minik fidan yere eğilmişti | fidanı yavaşça silkti ve yanına sağlam bir dal dikti
@tohum: elsa-0060
@degisim: pilav -> fidan
Ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile Olaf karlı yolda yürüyordu. Elsa yolun kenarında minik bir fidan gördü; fidan karın altında yere eğilmişti. "Elsa, bu küçük ağaç kırılacak mı?" diye sordu Olaf. "Ona yardım edelim, Olaf," dedi Elsa. Kraliçe Elsa hemen fidanın yanına gitti. Önce fidanı eliyle yavaşça silkti ve kar yere düştü. Fidan biraz kalktı, ama yine yana eğik duruyordu. Sonra Elsa yerden sağlam bir dal aldı ve fidanın yanına dikti. Olaf fidanı tuttu ve Elsa onu dala yasladı. "Bak, Elsa, artık dik duruyor!" dedi Olaf. Elsa ile Olaf çok sevindi, çünkü minik fidanı kurtarmışlardı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen fidanın"
   - Cümle 6: «Kraliçe Elsa hemen fidanın yanına gitti.»
   - Açıklama: Zaten tanınan Elsa ikinci kez unvanıyla tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa, 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen fidanın yanına gitti"
   - Cümle 6: «Kraliçe Elsa hemen fidanın yanına gitti.»
   - Açıklama: Tohumdaki özellik kraliçe (kız kardeşini korur) yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözüme katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0060` birebir aynı, `@degisim: pilav -> fidan` (tutuyorsan), ardından `@onarim: d289c2a5153645a5a5e6b595ec819155a5bd62ac`, sonra gövde.

### Hikâye 11: tohum elsa-0065 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0065
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yeni bir şeyi denemek
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'fide', fiil 'sergilemek', sıfat 'düz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kız kardeşi ilk kez kaymak istiyordu ama yol dikti | ona küçük bir tepe buldu ve kızağı hafifçe itti
@tohum: elsa-0065
@degisim: sergilemek -> göstermek
Elsa ile Anna buz sarayının önündeydi. Anna yeni kızağını Elsa'ya gösteriyordu. Kızakla ilk kez kaymak istiyordu ama sarayın kapısından inen yol çok dikti. Anna aşağıya bakınca kızağını bıraktı. Kraliçe Elsa kardeşini korumak istedi. Sarayın arkasında küçük bir tepe buldu. Tepenin altı düz ve genişti. "Anna, burada deneyelim," dedi Elsa. Anna küçük tepeye çıktı ve kızağa oturdu. Elsa kızağı arkadan tuttu ve hafifçe itti. Anna aşağı kaydı ve küçük bir çam fidesinin yanında yavaşça durdu. Sonra güldü ve hemen ayağa kalktı. "Teşekkürler, Elsa, kızakla kaymak çok güzelmiş!" dedi Anna.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini korumak"
   - Cümle 5: «Kraliçe Elsa kardeşini korumak istedi.»
   - Açıklama: Elsa zaten tanıtılmışken unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük bir çam fidesinin"
   - Cümle 11: «Anna aşağı kaydı ve küçük bir çam fidesinin yanında yavaşça durdu.»
   - Açıklama: 'Fide' sebze için kullanılır; çam için 'fidan' olmalı.
   - Açıklama: Ağaç yavrusu için 'fide' değil 'fidan' kullanılır.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir çam fidesinin yanında"
   - Cümle 11: «Anna aşağı kaydı ve küçük bir çam fidesinin yanında yavaşça durdu.»
   - Açıklama: 'Fide' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0065` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: a25f28d33ab17ef27de09275b69695a48f3932d2`, sonra gövde.

### Hikâye 12: tohum elsa-0066 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0066
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'file', fiil 'susamak', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik çok susadı ama yerdeki kar tozluydu | kayadan damlayan temiz suyu bir kapta topladı
@tohum: elsa-0066
Bir sabah Elsa ile Sven karlı dağda yürüyordu. Sven çok susamıştı ve biraz kar yemek istedi. Ama yerdeki kar çok tozluydu. Elsa etrafına baktı ve güneşli bir kaya gördü. Kayanın üstündeki buz eriyordu ve su damla damla düşüyordu. Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı. Kabı kayanın altına koydu ve bekledi. Kap yavaş yavaş temiz suyla doldu. Elsa kabı Sven'in önüne bıraktı. Sven suyu hızlıca içti ve sevinçle başını salladı. Sonra Elsa ile Sven dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kolundaki fileyi"
   - Cümle 6: «Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kolundaki fileyi açtı"
   - Cümle 6: «Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi kız kardeşini koruma biçiminde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kolundaki fileyi"
   - Cümle 6: «Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı"
   - Cümle 6: «Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı.»
   - Açıklama: Daha önce hiç kurulmamış file ve kap, çözüm gerektiği anda sebepsizce beliriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kolundaki fileyi açtı ve küçük bir kap çıkardı"
   - Cümle 6: «Kraliçe Elsa kolundaki fileyi açtı ve küçük bir kap çıkardı.»
   - Açıklama: File ve içindeki kap önceden kurulmadan tam gerektiği anda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0066` birebir aynı, ardından `@onarim: e296ecef9881470caa21e613b185a35c41817cc1`, sonra gövde.
