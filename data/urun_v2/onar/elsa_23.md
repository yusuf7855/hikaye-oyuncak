# Editör görevi (onarım): Elsa, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0067 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0067
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tahta', fiil 'uçmak', sıfat 'kırmızı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: kızaktan gelen tak tak sesi yüzünden geyik durdu | sese baktı ve sallanan tahtayı yerine bastırdı
@tohum: elsa-0067
@degisim: uçmak -> sallanmak
Elsa, Sven'in çektiği kızakla karlı ormanda gidiyordu. Birden kızağın arkasından tak tak diye bir ses geldi. Sven bu sesi duyunca durdu ve yürümek istemedi. "Bekle, Sven, sese ben bakayım," dedi Elsa. Kraliçe Elsa kızaktan indi ve sesin geldiği yere baktı. Kızağın arkasında kırmızı bir tahta sallanıyordu. Tahta her sallanınca kızağa vuruyor ve ses çıkarıyordu. Elsa tahtayı iki eliyle yerine sıkıca bastırdı. Ses hemen durdu. Sven sevinçle kızağı yeniden çekmeye başladı. Elsa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kızaktan indi"
   - Cümle 5: «Kraliçe Elsa kızaktan indi ve sesin geldiği yere baktı.»
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kızaktan indi"
   - Cümle 5: «Kraliçe Elsa kızaktan indi ve sesin geldiği yere baktı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik satırındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0067` birebir aynı, `@degisim: uçmak -> sallanmak` (tutuyorsan), ardından `@onarim: 477be1b485275fc1c00fcd1391ea93ab54d0391e`, sonra gövde.

### Hikâye 2: tohum elsa-0069 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0069
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'pedal', fiil 'katmak', sıfat 'yorgun'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: arkadaşı yazı seviyordu ama dağda çiçek yoktu | o uyurken buzdan çiçekler yaptı
@tohum: elsa-0069
@degisim: pedal -> çiçek
Dağın tepesinde hafif bir rüzgar esiyordu. Elsa ile Olaf buz sarayının önünde oturuyordu. Olaf yazı çok seviyordu ama karlı dağda hiç çiçek yoktu. Olaf dağa yürüyerek çıkmıştı ve çok yorgundu. Biraz sonra karın üstünde uyudu. Elsa ona bir sürpriz hazırlamak istedi. Ellerini salladı ve Olaf'ın yanına buzdan çiçekler yaptı. Olaf gözlerini açınca çiçekleri gördü. "Elsa, burada yaz var!" dedi Olaf. "Bunları senin için yaptım, Olaf," dedi Elsa. Olaf sevinçle dans etmeye başladı ve Elsa'yı da dansına kattı. Elsa ile Olaf çiçeklerin arasında mutlu mutlu eğlendi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'yı da dansına kattı"
   - Cümle 11: «Olaf sevinçle dans etmeye başladı ve Elsa'yı da dansına kattı.»
   - Açıklama: 'Dansına katmak' deyimsel bir anlatım; 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0069` birebir aynı, `@degisim: pedal -> çiçek` (tutuyorsan), ardından `@onarim: 53a2613194d2d28ce6472dd24a84ce010711e1ea`, sonra gövde.

### Hikâye 3: tohum elsa-0070 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0070
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'testi', fiil 'dinmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: sarayın bir yeri kırılıyor gibi bir ses duydu | balkona yürüdü ve sesi yapan testiyi buldu
@tohum: elsa-0070
@degisim: tatlı -> ince
Dağın tepesindeki buz sarayında soğuk bir rüzgar esiyordu. Elsa sarayın içinde ince bir ses duydu. Elsa sarayın bir yerinin kırıldığını sandı. Kraliçe Elsa sarayına bakmak için sesin geldiği yere yürüdü. Sarayın balkonunda boş bir testi duruyordu. Ama balkonda kırık bir şey yoktu. Rüzgar testinin ağzına esiyordu ve ses oradan çıkıyordu. Birden rüzgar dindi ve ses de durdu. Elsa testinin yanında biraz bekledi. Rüzgar yeniden esti ve testiden yine aynı ses geldi. Elsa çok sevindi, çünkü saray kırılmamıştı ve ses testiden geliyordu.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa sarayın bir yerinin kırıldığını sandı"
   - Cümle 3: «Elsa sarayın bir yerinin kırıldığını sandı.»
   - Açıklama: Art arda cümleler 'Elsa sarayın' ile başlıyor ve 'saray' gereksiz yere tekrarlanıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Kraliçe Elsa sarayına bakmak"
   - Cümle 4: «Kraliçe Elsa sarayına bakmak için sesin geldiği yere yürüdü.»
   - Açıklama: 'Saray' kelimesi art arda cümlelerde (2-5) gereksiz yere tekrarlanıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sarayına bakmak için"
   - Cümle 4: «Kraliçe Elsa sarayına bakmak için sesin geldiği yere yürüdü.»
   - Açıklama: Tohumdaki özellik kraliçe (kız kardeşini korur) yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0070` birebir aynı, `@degisim: tatlı -> ince` (tutuyorsan), ardından `@onarim: 6091355040175e1bbed7f4b8d714592350cf42de`, sonra gövde.

### Hikâye 4: tohum elsa-0071 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0071
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: bir şey yapmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ayçiçeği', fiil 'tamamlamak', sıfat 'üzgün'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: rüzgar esti ve buzdan çiçeğin bir yaprağı kırıldı | kızakta yaprağa benzeyen bir buz parçası buldu
@tohum: elsa-0071
Bir sabah Kraliçe Elsa dağda Kristoff'un yanına geldi. Kristoff onun için kızağındaki buz parçalarıyla bir ayçiçeği yapıyordu. Ama rüzgar esti ve çiçeğin ince bir yaprağı düşüp kırıldı. "Çiçeği bitiremedim," dedi Kristoff üzgün bir sesle. Elsa kızaktaki buz parçalarına baktı. İnce ve yaprağa benzeyen bir parça buldu. "Bu parça yaprak olabilir mi?" diye sordu Elsa. Elsa parçayı çiçeğin boş yerine dikkatle yerleştirdi. Parça boş yere tam sığdı ve ayçiçeği tamamlandı. Kristoff çiçeğe baktı ve kocaman gülümsedi. "Çok güzel oldu, Elsa!" dedi Kristoff. Sonra Elsa ile Kristoff buzdan ayçiçeğinin yanında mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa dağda Kristoff'un yanına geldi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0071` birebir aynı, ardından `@onarim: 12c871f93fd8f736ec97caabf114b85a95951df3`, sonra gövde.

### Hikâye 5: tohum elsa-0073 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0073
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'saat', fiil 'vermek', sıfat 'ıslak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: küçük saat karların içine düştü ve görünmedi | sesin geldiği yeri buldu ve saati buzdan kürekle çıkardı
@tohum: elsa-0073
Elsa, Sven ile karlı ormanda yürüyordu. Elsa küçük saatine bakarken saat elinden kaydı ve karların içine düştü. Elsa karların üstüne baktı ama saati göremedi. "Sven, saatim karların içinde kayboldu," dedi Elsa. O sırada karların altından tık tık diye bir ses geldi. Sven hemen durdu ve hiç ses çıkarmadı. Elsa bu sesi merak etti ve başını yere doğru eğdi. Ses bir ağacın dibinden geliyordu. "Bu benim saatimin sesi, Sven!" dedi Elsa. Elsa buzdan küçük bir kürek yaptı. Küreği yavaşça karlara soktu ve saati çıkardı. Saat ıslaktı ama yine tık tık ses veriyordu. Elsa çok sevindi, çünkü saatini sesinden bulmuştu.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Elsa küçük saatine bakarken"
   - Cümle 2: «Elsa küçük saatine bakarken saat elinden kaydı ve karların içine düştü.»
   - Açıklama: Kartta Elsa'nın saati yok ve saat, kartın tohum yasak kategorilerindeki çağdaş eşyaya yakın bir öğe.
   - Açıklama: Kartta Elsa'nın tık tık ses çıkaran küçük saati gibi bir eşya yok.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "karların üstüne baktı"
   - Cümle 3: «Elsa karların üstüne baktı ama saati göremedi.»
   - Açıklama: 'Karların' kelimesi art arda cümlelerde dört kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0073` birebir aynı, ardından `@onarim: 67a8b3731ef814e52f2b612348ce396c8891c8c4`, sonra gövde.

### Hikâye 6: tohum elsa-0074 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0074
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yastık', fiil 'erimek', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: güneşli yerde kar erimişti ve yer ıslaktı | sık dallı bir ağacın altında kuru bir yer buldu
@tohum: elsa-0074
Bir sabah Elsa ilk kez ormanda piknik yapmayı denedi. Elinde bir yastık ve küçük bir sepet vardı. Ama güneşli yerde kar erimişti ve yer çok ıslaktı. Elsa yastığını ıslak yere koyamadı. Elsa bir kraliçeydi ve hiç vazgeçmedi. Hemen büyük, yeşil bir çam ağacına gitti. Ağacın sık dalları karı tutmuştu, bu yüzden altı kuruydu. Elsa yastığını ağacın altındaki kuru yere koydu. Sonra sepetinden ekmek ve elma çıkardı. Elsa yastığına oturdu ve ilk pikniğini mutlu mutlu yaptı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve hiç vazgeçmedi"
   - Cümle 5: «Elsa bir kraliçeydi ve hiç vazgeçmedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız etiket olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Kraliçe özelliği karttaki 'kız kardeşini korur' anlamında değil, vazgeçmeme gerekçesi olarak ve işe yaramadan kullanılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve hiç vazgeçmedi"
   - Cümle 5: «Elsa bir kraliçeydi ve hiç vazgeçmedi.»
   - Açıklama: Kraliçe olmak vazgeçmemenin sebebi değil; olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0074` birebir aynı, ardından `@onarim: 207273d3eb5ad6fbd8dcd44dd2ecebfc7c0110c1`, sonra gövde.

### Hikâye 7: tohum elsa-0075 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0075
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'şişe', fiil 'çiğnemek', sıfat 'plastik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: boş şişeler çok hafifti ve rüzgar onları devirdi | şişeleri karla doldurup ağır yaptı
@tohum: elsa-0075
@degisim: çiğnemek -> doldurmak
Bir sabah Elsa ile Kristoff karlı ormanda komik bir şişe oyunu oynuyordu. Karın üstüne üç boş plastik şişe koydular. Ama şişeler çok hafifti ve rüzgar onları devirdi. Kristoff şişeleri yeniden koydu ama şişeler yine yere düştü. "Böyle oynayamayız, Elsa," dedi Kristoff. Elsa biraz düşündü. Sonra her şişeyi karla doldurdu. Şimdi şişeler ağırdı ve rüzgarda dik durdu. Elsa küçük bir kar topu yaptı ve Kristoff'a verdi. "Kraliçe olarak ilk sırayı sana veriyorum," dedi Elsa. Kristoff topu attı ve üç şişe birden devrildi. "Harika bir fikir, Elsa, çok eğlendim!" dedi Kristoff.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şişeleri karla doldurup ağır yaptı"
   - Cümle 0 (plan satırı): «boş şişeler çok hafifti ve rüzgar onları devirdi | şişeleri karla doldurup ağır yaptı»
   - Açıklama: 'Ağır yaptı' yanlış kullanım; 'ağırlaştırdı' olmalı.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "üç boş plastik şişe"
   - Cümle 2: «Karın üstüne üç boş plastik şişe koydular.»
   - Açıklama: Plastik şişe kartın masal krallığı dünyasına ve tohum yasak kategorilerindeki çağdaş öğe kuralına aykırı.
   - Açıklama: Plastik şişe kartın masal krallığı dünyasında olmayan çağdaş bir eşya.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe olarak ilk sırayı sana veriyorum"
   - Cümle 10: «"Kraliçe olarak ilk sırayı sana veriyorum," dedi Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi kız kardeşini korumak için değil, işe yaramayan bir söz olarak geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kraliçe olarak ilk sırayı sana veriyorum"
   - Cümle 10: «"Kraliçe olarak ilk sırayı sana veriyorum," dedi Elsa.»
   - Açıklama: Elsa'nın kraliçeliği olaya hiçbir şey katmayan işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0075` birebir aynı, `@degisim: çiğnemek -> doldurmak` (tutuyorsan), ardından `@onarim: d6f9b819074d1531a8c1c39d33d634fd8346e41b`, sonra gövde.

### Hikâye 8: tohum elsa-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0078
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'sünger', fiil 'yakalanmak', sıfat 'sihirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: karda her yerde ayak izi vardı ve saklanan bulunamadı | kar yağdırıp eski izleri kapattı ve yeni izi buldu
@tohum: elsa-0078
@degisim: sünger -> kaya
Elsa ile Kristoff dağda sihirli bir saklambaç oynuyordu. Kristoff kayaların arkasına saklanmıştı. Ama karda her yerde eski ayak izleri vardı ve Elsa onu bulamadı. Elsa biraz düşündü ve ellerini gökyüzüne kaldırdı. Ellerinden ince buz taneleri ve hafif bir kar yağdı. Kar bütün eski izleri kapattı. "Kristoff, yerini değiştir!" diye seslendi Elsa. Sonra gözlerini kapadı. Kristoff başka bir kayanın arkasına koştu. Yeni karda onun ayak izleri hemen göründü. Elsa izlerin peşinden gitti ve Kristoff'u buldu. "Tamam, yakalandım!" dedi Kristoff gülerek. Elsa çok sevindi, çünkü saklanan Kristoff'u sonunda bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sihirli bir saklambaç oynuyordu"
   - Cümle 1: «Elsa ile Kristoff dağda sihirli bir saklambaç oynuyordu.»
   - Açıklama: Oyunun kendisi sihirli değil; sıfat yanlış yere bağlanmış.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kristoff, yerini değiştir!"
   - Cümle 7: «"Kristoff, yerini değiştir!" diye seslendi Elsa.»
   - Açıklama: Çözüm kar yağdırmakla bitmiyor; Kristoff'a yer değiştirtmek, göz kapamak ve izleri takip etmek gibi ikiden fazla adıma yayılıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kristoff başka bir kayanın arkasına koştu"
   - Cümle 9: «Kristoff başka bir kayanın arkasına koştu.»
   - Açıklama: Çözüm kar yağdırmanın yanında Kristoff'un yer değiştirmesini ve izlerin takibini gerektirip ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0078` birebir aynı, `@degisim: sünger -> kaya` (tutuyorsan), ardından `@onarim: 9dcf099c88da170fd6df19b2e4051f6fcb20cf1e`, sonra gövde.

### Hikâye 9: tohum elsa-0079 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Olaf
@tohum: elsa-0079
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: paylaşmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'elmas', fiil 'yüklemek', sıfat 'sisli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | şato | Olaf
@plan: kardan adamın kızağı çok ağırdı ve kıpırdamadı | elmaların yarısını kendi kızağına aldı
@tohum: elsa-0079
@degisim: elmas -> elma
Bir sabah sarayın önü çok sisliydi. Elsa ile Olaf dışarıdan saraya elma taşıyordu. Olaf küçük kızağına çok elma yüklemişti ve kızak kıpırdamıyordu. "Bu çok ağır, Elsa!" dedi Olaf. Elsa'nın kraliçe kızağı çok büyüktü. Elsa bu büyük kızağı Olaf'ın yanına çekti. "Elmaları paylaşalım, Olaf," dedi Elsa. Elsa elmaların yarısını kendi kızağına aldı. Şimdi ikisinin yükü de hafifti. İkisi sisin içinde yan yana yürüdü ve kapıya vardı. Kapıda Olaf en güzel elmayı Elsa'ya uzattı. "Teşekkürler, Elsa, birlikte çok kolay oldu!" dedi Olaf.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa'nın kraliçe kızağı çok büyüktü"
   - Cümle 5: «Elsa'nın kraliçe kızağı çok büyüktü.»
   - Açıklama: 'Kraliçe kızağı' tamlaması bozuk; 'Elsa'nın kızağı' ya da 'kraliçenin kızağı' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa'nın kraliçe kızağı çok büyüktü"
   - Cümle 5: «Elsa'nın kraliçe kızağı çok büyüktü.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi (kız kardeşini koruyan kraliçe) kullanılmıyor, yalnız kızağa sıfat olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0079` birebir aynı, `@degisim: elmas -> elma` (tutuyorsan), ardından `@onarim: f7f810e684553bf2c9a31f93d1a063cb60151f0b`, sonra gövde.

### Hikâye 10: tohum elsa-0080 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0080
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kutu', fiil 'sevmek', sıfat 'biberli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik acıkmıştı ve kutudaki ekmekler biberliydi | kutunun dibinde havuç bulup ona verdi
@tohum: elsa-0080
Elsa elinde bir yemek kutusuyla sarayından çıktı. Kapının önünde Sven burnuyla karı karıştırıyordu. Karın altında hiç ot yoktu ve Sven çok acıkmıştı. Elsa iyi bir kraliçeydi ve Sven'i aç bırakmak istemedi. Hemen kutusunu açtı. Kutuda biberli ekmekler vardı. Sven bir ekmeği kokladı ve başını çevirdi. "Biberli ekmeği sevmiyorsun, değil mi?" diye sordu Elsa. Sven başını iki yana salladı. Elsa kutunun dibine baktı ve iki havuç buldu. Havuçları hemen Sven'e uzattı. Sven onları yedi ve sevinçle zıpladı. "Afiyet olsun, Sven, bunlar senin için!" dedi Elsa gülerek.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kutunun dibine baktı ve iki havuç buldu"
   - Cümle 10: «Elsa kutunun dibine baktı ve iki havuç buldu.»
   - Açıklama: Havuçlar önceden kurulmadan kutunun dibinde beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0080` birebir aynı, ardından `@onarim: 0bb7b83e33421589c9efbf60c3c2e8d1eefd09ba`, sonra gövde.

### Hikâye 11: tohum elsa-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0081
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'köpük', fiil 'sormak', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: güneşte kar yumuşadı ve pastanın üstü kaydı | buzdan sağlam bir pasta yapıp dallarla süsledi
@tohum: elsa-0081
@degisim: sormak -> süslemek
Dağın tepesinde güneş parlıyordu. Elsa karla büyük bir oyun pastası yapıyordu. Ama güneşli havada kar köpük gibi yumuşadı ve pastanın üstü yana kaydı. Elsa kayan karı eliyle geri koydu ama kar yine düştü. Biraz düşündü ve ellerini salladı. Önünde buzdan sağlam bir pasta belirdi. Yeni pasta güneşte pırıl pırıl parladı ve hiç kaymadı. Elsa yakındaki bir çamdan küçük dallar aldı. Pastanın üstünü bu yeşil dallarla süsledi. Elsa oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kar köpük gibi yumuşadı"
   - Cümle 3: «Ama güneşli havada kar köpük gibi yumuşadı ve pastanın üstü yana kaydı.»
   - Açıklama: 'Köpük gibi' benzetmesi küçük çocuk için gereksiz bir mecaz.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pastanın üstünü bu yeşil dallarla süsledi"
   - Cümle 9: «Pastanın üstünü bu yeşil dallarla süsledi.»
   - Açıklama: Dallarla süsleme sorunun sebebine yönelmeyen fazladan bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0081` birebir aynı, `@degisim: sormak -> süslemek` (tutuyorsan), ardından `@onarim: b44508e0dd0e780b18d4969e6edbafec0b4736fc`, sonra gövde.

### Hikâye 12: tohum elsa-0084 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0084
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'eşarp', fiil 'yaratmak', sıfat 'temiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: rüzgar kardan arkadaşın başını yere düşürdü | başı yerine koyup boynuna eşarp bağladı
@tohum: elsa-0084
@degisim: yaratmak -> yapmak
Rüzgar karlı ağaçların arasında hafif hafif esiyordu. Elsa ile Olaf ormanda kardan küçük bir arkadaş yapıyordu. Ama rüzgar kardan arkadaşın başını yere düşürdü. "Arkadaşımın başı düştü, Elsa!" dedi Olaf üzgün üzgün. Kraliçe Elsa hemen Olaf'ın yanına eğildi. Başı yerine koydu ve karı iki eliyle bastırdı. Sonra kendi temiz eşarbını çıkardı. Eşarbı yeni arkadaşın boynuna sıkıca bağladı. Rüzgar yine esti ama baş artık düşmedi. "Yaşasın, yeni arkadaşım hazır!" dedi Olaf. Elsa ile Olaf yeni arkadaşın yanında mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen Olaf'ın yanına eğildi"
   - Cümle 5: «Kraliçe Elsa hemen Olaf'ın yanına eğildi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözüme katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0084` birebir aynı, `@degisim: yaratmak -> yapmak` (tutuyorsan), ardından `@onarim: 27a639e0aeeae4840bd00ff3c30d3b25e09639b5`, sonra gövde.
