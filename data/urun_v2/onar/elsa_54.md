# Editör görevi (onarım): Elsa, onarım partisi 54

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar54.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar54.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0153 (deneme 4 -> 5)

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
Ormanda hafif bir rüzgar esiyordu. Elsa ile Olaf büyük bir ağacın yanında heykel oyunu oynuyordu. Ama ikisi de ağaca dönüp saymak istedi. "Ben sayacağım!" dedi Olaf. "Kar kimin başına yağarsa, ilk o sayar," dedi Elsa. Sonra elini havaya kaldırdı ve elinden buz ve kar çıktı. Rüzgar karı taşıdı ve kar Olaf'ın başına yağdı. Olaf sevinçle ağaca döndü ve saydı. Elsa kollarını oynattı ve yürüdü. Olaf dönünce Elsa hareketsiz durdu. Sonra sıra Elsa'ya geldi ve o da ağaca döndü. Olaf'ın havuç burnu kıpırdadı ve ikisi de çok güldü. Elsa çok mutluydu, çünkü ikisi de sırayla saymıştı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kar kimin başına yağarsa, ilk o sayar"
   - Cümle 5: «"Kar kimin başına yağarsa, ilk o sayar," dedi Elsa.»
   - Açıklama: Karı Elsa kendisi yağdırdığı için bu kura adil bir çözüm değil, seçimi dolaylı yoldan Elsa yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0153` birebir aynı, ardından `@onarim: ca88b3aaea9df133d6b2874b7da1d21d010ed020`, sonra gövde.

### Hikâye 2: tohum elsa-0154 (deneme 4 -> 5)

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
@plan: ikisi topu kendine çekti ve top ikiye ayrıldı | sırayla itmeyi istedi ve top büyüdü
@tohum: elsa-0154
@degisim: çamur -> kar
Elsa ile Kristoff dağda, buz sarayının önünde oynuyordu. Elmalı turtayı koymak için kardan büyük bir masa yapacaklardı. Ama ikisi de kar topunu kendine doğru çekti ve top ikiye ayrıldı. Kraliçe Elsa hemen yeni ve küçük bir top yaptı. Elsa kızmadı ve Kristoff'a gülümsedi. "Kristoff, sen on adım it, sonra ben," dedi Elsa. Kristoff topu on adım itti ve top büyüdü. Sonra Elsa itti ve top daha da büyüdü. Sırayla ittiler ve top kocaman oldu. Kristoff turtayı topun üstüne koydu. "Bak, sırayla yaptık ve masa hazır, Kristoff!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen yeni"
   - Cümle 4: «Kraliçe Elsa hemen yeni ve küçük bir top yaptı.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen yeni"
   - Cümle 4: «Kraliçe Elsa hemen yeni ve küçük bir top yaptı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; çözüm sırayla itmek, özellik işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0154` birebir aynı, `@degisim: çamur -> kar` (tutuyorsan), ardından `@onarim: 30a2369035ac96622674a15daaefc06200d86acf`, sonra gövde.

### Hikâye 3: tohum elsa-0155 (deneme 4 -> 5)

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
@plan: ılık güneş sarayın buzunu eritti ve geyik kaydı | yere halı serdi ve geyiğe halıyı gösterdi
@tohum: elsa-0155
Bir sabah dağda ılık bir güneş vardı. Sven, Elsa'nın buz sarayına oynamaya gelmişti. Ama güneş yüzünden sarayın içi ıslak ve kaygandı. Sven kapıdan bir adım attı ve ayağı biraz kaydı. Elsa sarayın kraliçesiydi ve Sven'i korumak istedi. Hemen Sven'i kapının önünde durdurdu. Sonra salonun köşesindeki uzun, yumuşak halıyı getirdi. Halıyı kapıdan salona kadar yere serdi. Elsa, Sven'e halıyı eliyle gösterdi. Sven halıya dikkatle bastı. Ayakları bu kez hiç kaymadı. Sven halının üstünde rahatça yürüdü ve başını salladı. Elsa çok sevindi, çünkü Sven artık sarayda hiç kaymıyordu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa sarayın kraliçesiydi ve Sven'i korumak istedi"
   - Cümle 5: «Elsa sarayın kraliçesiydi ve Sven'i korumak istedi.»
   - Açıklama: Kartın özellik alanı kız kardeşini korumayı söylüyor; kraliçelik sorunu çözmekte işe yaramıyor, çözüm halı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0155` birebir aynı, ardından `@onarim: 1a7ebf3004db838cadb8ccdf7062141e711b0009`, sonra gövde.

### Hikâye 4: tohum elsa-0157 (deneme 4 -> 5)

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
@plan: ikisi topu aynı anda itti ve top dağıldı | sırayla yuvarlamayı istedi
@tohum: elsa-0157
@degisim: cesur -> kocaman
Bir sabah kraliçe Elsa ile Kristoff limanda kardan bir dondurma yapıyordu. İkisi de kar topunu aynı anda itti. Top ikiye ayrıldı ve yere dağıldı. "Önce ben yapacağım!" dedi Kristoff. Elsa kızmadı ve ona gülümsedi. "Kristoff, sen üç kez yuvarla, sonra ben," dedi Elsa. Kristoff başını salladı ve güldü. Kristoff yeni bir topu üç kez yuvarladı. Sonra sıra Elsa'ya geldi ve o da üç kez yuvarladı. İkisi sırayla topu biraz daha büyüttü. Sonunda kocaman, yuvarlak bir dondurma topu oldu. Elsa ile Kristoff yeni toplar yapmaya sırayla ve mutlu mutlu devam ettiler.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bir sabah kraliçe Elsa"
   - Cümle 1: «Bir sabah kraliçe Elsa ile Kristoff limanda kardan bir dondurma yapıyordu.»
   - Açıklama: Ada bağlı unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Unvan özel adla birlikte büyük harfle yazılır: 'Kraliçe Elsa'.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe Elsa ile Kristoff"
   - Cümle 1: «Bir sabah kraliçe Elsa ile Kristoff limanda kardan bir dondurma yapıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0157` birebir aynı, `@degisim: cesur -> kocaman` (tutuyorsan), ardından `@onarim: 2f63b4ff028934578ad1c6ac9116fe274e58e967`, sonra gövde.

### Hikâye 5: tohum elsa-0158 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0158
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'terazi', fiil 'düzenlemek', sıfat 'neşeli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: rüzgar masadaki örtüyü havaya kaldırdı | kardan adama örtüyü tutmasını söyledi ve üstüne terazi koydu
@tohum: elsa-0158
Kraliçe Elsa limanda Olaf ile ilk kar için neşeli bir şenlik hazırlıyordu. Olaf, limandaki ağır terazinin yanındaki masaya beyaz bir örtü serdi. Ama rüzgar esti ve örtü havaya kalktı. Kurabiye tabakları masada duramadı. "Olaf, sen örtüyü sıkıca tut," dedi Elsa. Olaf örtüyü iki eliyle tuttu. Elsa o teraziyi getirdi ve örtünün ortasına koydu. Örtü artık rüzgarda kalkmadı. İkisi kurabiyeleri masada güzelce düzenledi. "Bu şenlik harika olacak!" dedi Olaf. Sonra Elsa ile Olaf şenliğe mutlu mutlu başladı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa limanda Olaf"
   - Cümle 1: «Kraliçe Elsa limanda Olaf ile ilk kar için neşeli bir şenlik hazırlıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa limanda Olaf ile"
   - Cümle 1: «Kraliçe Elsa limanda Olaf ile ilk kar için neşeli bir şenlik hazırlıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve örtü havaya kalktı"
   - Cümle 3: «Ama rüzgar esti ve örtü havaya kalktı.»
   - Açıklama: Rüzgarın örtüyü kaldırması önemsiz, rüzgar-dağıttı kalıbında bir sorun.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa o teraziyi getirdi"
   - Cümle 7: «Elsa o teraziyi getirdi ve örtünün ortasına koydu.»
   - Açıklama: Ağır olarak kurulan terazi Elsa tarafından zahmetsizce taşınıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0158` birebir aynı, ardından `@onarim: ce70a09692ace26ff90d4c9076ea5dd8e607f944`, sonra gövde.

### Hikâye 6: tohum elsa-0159 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0159
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'süs', fiil 'güldürmek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: rüzgar esti ve süs elinden uçup kayboldu | buz duvarına bakıp süsü saçında gördü
@tohum: elsa-0159
Bir sabah dağa sulu kar yağıyordu. Kraliçe Elsa buz sarayının kapısına yeni bir süs asmak istiyordu. Ama rüzgar esti, süs elinden uçtu ve kayboldu. Elsa kapının önündeki kara eğildi ve baktı. Sulu karın içinde yalnız küçük taşlar vardı. Elsa üzüldü ve sarayın duvarına döndü. Duvarın buzu ayna gibi parlıyordu. Elsa duvarda kendini gördü. Süs onun saçına takılmıştı! Süsün saçında olması Elsa'yı çok güldürdü. Süsü saçından çıkardı ve kapıya astı. Elsa çok sevindi, çünkü süsünü hiç uzağa gitmeden bulmuştu.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa buz sarayının"
   - Cümle 2: «Kraliçe Elsa buz sarayının kapısına yeni bir süs asmak istiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa üzüldü ve sarayın duvarına döndü"
   - Cümle 6: «Elsa üzüldü ve sarayın duvarına döndü.»
   - Açıklama: Elsa süsü aramak için değil üzüldüğü için duvara dönüyor; çözüm sebebe yönelmiyor, tesadüfle geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa üzüldü ve sarayın duvarına döndü"
   - Cümle 6: «Elsa üzüldü ve sarayın duvarına döndü.»
   - Açıklama: Süs Elsa'nın aramasıyla değil, tesadüfen duvarda görülerek bulunuyor; çözüm sebepsizce geliyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzu ayna gibi parlıyordu"
   - Cümle 7: «Duvarın buzu ayna gibi parlıyordu.»
   - Açıklama: Benzetme (mecaz) kullanılmış; madde mecaz istemiyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Süs onun saçına takılmıştı"
   - Cümle 9: «Süs onun saçına takılmıştı!»
   - Açıklama: Kaybolan süsün saçta çıkması sebepsiz bir tesadüf olarak çözümü getiriyor.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Süsün saçında olması Elsa'yı"
   - Cümle 10: «Süsün saçında olması Elsa'yı çok güldürdü.»
   - Açıklama: 'Süsün saçında' tamlaması 'süsün saçı' gibi okunuyor; ağır ve yanlış anlaşılan bir yapı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0159` birebir aynı, ardından `@onarim: e3dcfc4cac37b73c506efc221d2050fc31123615`, sonra gövde.

### Hikâye 7: tohum elsa-0161 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Sven
@tohum: elsa-0161
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'uçurtma', fiil 'eğilmek', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | Sven
@plan: uçurtmanın ipi geyiğin ayaklarına dolandı | geyiğe durmasını söyledi, eğilip ipi çözdü
@tohum: elsa-0161
Bir sabah Kraliçe Elsa sarayın önünde mavi bir uçurtma uçuruyordu. Sven de onu izliyordu. Birden rüzgar durdu ve uçurtmanın ipi Sven'in ayaklarına dolandı. Sven ayaklarını salladı ama ipi çıkaramadı. Sonra döndü ve gürültülü sesler çıkardı. İp daha çok dolandı. "Sven, dur ve hiç kıpırdama!" dedi Elsa yüksek sesle. Sven hemen durdu ve sakin sakin bekledi. Elsa eğildi ve ipi yavaşça çözdü. Sonra uçurtmayı dikkatle yere koydu. Sven sevinçle burnunu Elsa'nın eline sürttü. Elsa çok mutlu oldu, çünkü Sven'e yardım etmişti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sarayın önünde"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayın önünde mavi bir uçurtma uçuruyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayın önünde mavi bir uçurtma uçuruyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, hikayede işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0161` birebir aynı, ardından `@onarim: fb10af0ce8c830d54cd5ab7a91de44bd8b4cd2ae`, sonra gövde.

### Hikâye 8: tohum elsa-0162 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0162
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çember', fiil 'incelemek', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: dalgalar taşları ıslattı ve çember kaydı | limanın kuru tarafına geçti
@tohum: elsa-0162
Kraliçe Elsa limanda ilk kez çember çevirmeyi deniyordu. Ama deniz o sabah çok dalgalıydı. Dalgalar kıyıya vurdu ve taşları ıslattı. Çember ıslak taşların üstünde kaydı ve düştü. Elsa çemberi ve taşları dikkatle inceledi. Taşlar yalnız kıyıya yakın yerde ıslaktı. Limanın arka tarafına dalgalar gelmiyordu. Elsa hemen o kuru tarafa geçti. Orada çemberi yeniden yuvarladı. Bu kez çember kaymadı ve uzun süre döndü. Sonra Elsa limanda çemberiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa limanda ilk"
   - Cümle 1: «Kraliçe Elsa limanda ilk kez çember çevirmeyi deniyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, hikayede işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Çember ıslak taşların üstünde kaydı"
   - Cümle 4: «Çember ıslak taşların üstünde kaydı ve düştü.»
   - Açıklama: Dalgalı denizin vurduğu ıslak kıyı taşlarında oynamak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0162` birebir aynı, ardından `@onarim: 34cfa7defab598408305a01aec1116fcae3a1c36`, sonra gövde.

### Hikâye 9: tohum elsa-0163 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0163
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'vanilya', fiil 'sabırsızlanmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: kapıyı buzla kapadı ve kardan adamı dışarıda unuttu | sesi duyup kapıyı açtı ve özür diledi
@tohum: elsa-0163
@degisim: sabırsızlanmak -> beklemek
Rüzgar dağın tepesinde hafifçe esiyordu. Elsa rüzgar girmesin diye sarayın kapısını buzla kapadı. Ama Olaf dışarıda karla oynuyordu ve Elsa bunu unutmuştu. Elsa salonda vanilyalı kurabiyeleri bir tabağa diziyordu. Olaf kapalı kapıya vurdu ve bekledi. Elsa sesi duydu ve hemen kapıya koştu. Elini salladı, kapıdaki buzu kaldırdı ve kapıyı açtı. "Özür dilerim, Olaf, seni dışarıda unuttum," dedi Elsa. "Tamam, ama bana sıkıca sarıl!" dedi Olaf. Elsa ona sarıldı ve birlikte içeri girdiler. Elsa ile Olaf çok sevindi, çünkü yine birlikteydiler.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sarayın kapısını buzla kapadı"
   - Cümle 2: «Elsa rüzgar girmesin diye sarayın kapısını buzla kapadı.»
   - Açıklama: Buz özelliği iki kez kullanılıyor ve ilk kullanımda sorunu yaratıyor, tek ve işe yarar kullanım değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "vanilyalı kurabiyeleri bir tabağa diziyordu"
   - Cümle 4: «Elsa salonda vanilyalı kurabiyeleri bir tabağa diziyordu.»
   - Açıklama: Kurabiyeler işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa salonda vanilyalı kurabiyeleri bir tabağa diziyordu"
   - Cümle 4: «Elsa salonda vanilyalı kurabiyeleri bir tabağa diziyordu.»
   - Açıklama: Kurabiyeler bir daha geçmiyor ve olayda hiçbir işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kapıdaki buzu kaldırdı"
   - Cümle 7: «Elini salladı, kapıdaki buzu kaldırdı ve kapıyı açtı.»
   - Açıklama: Buz özelliği bir kez değil iki kez (kapıyı kapamak ve açmak için) kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0163` birebir aynı, `@degisim: sabırsızlanmak -> beklemek` (tutuyorsan), ardından `@onarim: befcad7ef0cbc5e657e347a796bd7692341acd0e`, sonra gövde.

### Hikâye 10: tohum elsa-0165 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0165
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'teker', fiil 'ısınmak', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: güneşte yerdeki buzlar erimeye başladı | arabasını paylaştı ve buzları gölgeye taşıdılar
@tohum: elsa-0165
@degisim: yetenekli -> güçlü
Bir sabah Kraliçe Elsa saray için buz almaya limana geldi. Yanında sarayın boş arabası vardı. Ama hava ısınıyordu ve Kristoff'un yerdeki buzları eriyordu. Kristoff buzları tek tek eliyle gölgeye taşıyordu. Buzlar çoktu ve Kristoff hepsine yetişemiyordu. Elsa arabasını hemen Kristoff ile paylaştı. Kristoff çok güçlüydü ve buzları hızlıca arabaya dizdi. Elsa da küçük parçaları topladı ve arabaya koydu. İkisi arabayı birlikte gölgeye çekti. Arabanın büyük tekerleri taşların üstünde kolayca döndü. Gölgede buzlar artık erimedi. Sonra Elsa ile Kristoff gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa saray için"
   - Cümle 1: «Bir sabah Kraliçe Elsa saray için buz almaya limana geldi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa saray için buz almaya"
   - Cümle 1: «Bir sabah Kraliçe Elsa saray için buz almaya limana geldi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "saray için buz almaya limana geldi"
   - Cümle 1: «Bir sabah Kraliçe Elsa saray için buz almaya limana geldi.»
   - Açıklama: Elsa'nın buz alma amacı kuruluyor ama hikayede hiç kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arabanın büyük tekerleri taşların üstünde kolayca döndü"
   - Cümle 10: «Arabanın büyük tekerleri taşların üstünde kolayca döndü.»
   - Açıklama: Tekerlerin dönmesi hiçbir işe yaramayan işlevsiz bir ayrıntı.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa ile Kristoff gölgede mutlu mutlu dinlendi"
   - Cümle 12: «Sonra Elsa ile Kristoff gölgede mutlu mutlu dinlendi.»
   - Açıklama: Elsa saray için buz almaya gelmişti ama bu hedefe hiç dönülmüyor ve hikaye bu hedef açıkta kalarak bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0165` birebir aynı, `@degisim: yetenekli -> güçlü` (tutuyorsan), ardından `@onarim: 75b817f5b37c4e2bc0ecc99b4feb00de38eb16b2`, sonra gövde.

### Hikâye 11: tohum elsa-0167 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0167
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tepsi', fiil 'çıkmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: tepsi karlı tepede bir şeye çarpıp durdu | karı itip gizli taşı buldu ve yanından kaydırdı
@tohum: elsa-0167
Ormanda küçük ve karlı bir tepe vardı. Kraliçe Elsa bir tepsiyi tepeden aşağı kaydırıyordu. Ama tepsi tepenin ortasında "tak" diye bir şeye çarptı ve durdu. Elsa bu sesi çok merak etti. Tepsinin yanına yürüdü ve karı eliyle yavaşça kenara itti. Karın altından gizli, büyük bir taş çıktı. Elsa taşın üstünü açık bıraktı. Artık büyük taş uzaktan görünüyordu. Sonra Elsa tepsiyi alıp tepeye geri yürüdü. Bu kez tepsiyi taşın öbür yanından kaydırdı. Tepsi hiç durmadan en alta kadar gitti. Elsa gülerek tepeye koştu ve tepsiyi mutlu mutlu bir daha kaydırdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa bir tepsiyi"
   - Cümle 2: «Kraliçe Elsa bir tepsiyi tepeden aşağı kaydırıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0167` birebir aynı, ardından `@onarim: 8cef824faeca5b36fc2f8a43b172c661e4bc6358`, sonra gövde.

### Hikâye 12: tohum elsa-0168 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0168
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yağ', fiil 'kurtulmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: kızaktaki oynak bir tahta yerinden çıktı | kendi kızağını kardeşiyle paylaştı
@tohum: elsa-0168
@degisim: yağ -> kızak
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa ile Anna kızaklarını çekerek tepeye yürüdü. Ama Anna'nın kızağındaki oynak bir tahta yerinden çıktı ve kara düştü. Anna kırık kızağa baktı ve çok üzüldü. Kraliçe Elsa kızağını kardeşine gösterdi ve öne oturmasını söyledi. Anna hemen öne oturdu. Elsa da arkasına oturdu ve kardeşine sıkıca sarıldı. İki kardeş tepeden yavaş yavaş kaydı. Anna kahkahalarla güldü. Böylece Anna'nın kızak oyunu kurtuldu. Aşağıda kalkıp bir kez daha yukarı yürüdüler. Elsa çok mutlu oldu, çünkü kızağını kardeşiyle paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kızak oyunu kurtuldu"
   - Cümle 10: «Böylece Anna'nın kızak oyunu kurtuldu.»
   - Açıklama: Oyunun kurtulması mecazdır, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anna'nın kızak oyunu kurtuldu"
   - Cümle 10: «Böylece Anna'nın kızak oyunu kurtuldu.»
   - Açıklama: 'Oyunu kurtuldu' mecazlı ve soyut bir anlatım, küçük çocuğa uygun değil.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Aşağıda kalkıp bir kez"
   - Cümle 11: «Aşağıda kalkıp bir kez daha yukarı yürüdüler.»
   - Açıklama: Nereden kalktıkları eksik ve öznesiz cümle bozuk; 'Aşağıda kızaktan kalkıp' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0168` birebir aynı, `@degisim: yağ -> kızak` (tutuyorsan), ardından `@onarim: f4d0d98aa80f6ad0207ce5bc223c209e437a020c`, sonra gövde.
