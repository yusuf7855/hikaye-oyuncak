# Editör görevi (onarım): Elsa, onarım partisi 56

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar56.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar56.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0192 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0192
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kurabiye', fiil 'tanışmak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: sürpriz hazır olmadan arkadaşı erken geldi | ona kapıda gözlerini kapatmasını söyledi
@tohum: elsa-0192
@degisim: tanışmak -> hazırlamak
Karlı dağın tepesindeki sarayda Elsa bir sürpriz hazırlıyordu. Kraliçe, Kristoff için masaya kurabiyeler dizmek istiyordu. Ama Kristoff erken geldi ve kapıyı açtı. Masa daha hazır değildi. Elsa hemen elini kaldırdı. "Kristoff, kapıda dur ve gözlerini kapat," dedi Elsa. Kristoff durdu ve gözlerini sıkıca kapattı. Elsa kurabiyeleri hızla masaya dizdi. "Şimdi bakabilirsin, Kristoff," dedi Elsa. Kristoff baktı ve kurabiyeleri gördü. "Bugün çok şanslı bir günüm, teşekkürler, Elsa!" dedi Kristoff. İkisi kurabiyeleri birlikte yedi ve güldü. Elsa bundan sonra sürprizlerini hep erkenden hazırladı.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe, Kristoff için masaya kurabiyeler"
   - Cümle 2: «Kraliçe, Kristoff için masaya kurabiyeler dizmek istiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız ad olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe, Kristoff için masaya"
   - Cümle 2: «Kraliçe, Kristoff için masaya kurabiyeler dizmek istiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bugün çok şanslı bir günüm"
   - Cümle 11: «"Bugün çok şanslı bir günüm, teşekkürler, Elsa!" dedi Kristoff.»
   - Açıklama: Cümle dilbilgisel olarak kurulmamış; 'Bugün benim şanslı günüm' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok şanslı bir günüm"
   - Cümle 11: «"Bugün çok şanslı bir günüm, teşekkürler, Elsa!" dedi Kristoff.»
   - Açıklama: 'Şanslı' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bugün çok şanslı bir günüm"
   - Cümle 11: «"Bugün çok şanslı bir günüm, teşekkürler, Elsa!" dedi Kristoff.»
   - Açıklama: 'Şanslı bir gün' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0192` birebir aynı, `@degisim: tanışmak -> hazırlamak` (tutuyorsan), ardından `@onarim: 7742c948e6fe451623675124041c0e6ad3c5692d`, sonra gövde.

### Hikâye 2: tohum elsa-0196 (deneme 3 -> 4)

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
Limanda Sven buz dolu bir kızak çekiyordu. Elsa ona yardım etmek için kızağı arkadan itti. Ama çok hızlı itti ve buzlar kızaktan düşüp kırıldı. Sven kırık parçalara baktı ve başını eğdi. Elsa hemen Sven'in yanına gitti ve başını okşadı. Sonra ondan özür diledi. Elsa ellerini kızağa doğru açtı. Elinden parlak buz çıktı ve kızak yeniden doldu. Sven buna inanamadı ve yeni buzlara burnuyla dokundu. Buzlar gerçekti ve eskilerinden de iyiydi. Sven sevinçle ayaklarını yere vurdu. Sonra Sven kızağı çekti ve Elsa mutlu mutlu yanında yürüdü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sven buna inanamadı"
   - Cümle 9: «Sven buna inanamadı ve yeni buzlara burnuyla dokundu.»
   - Açıklama: 'İnanamadı' soyut bir duygu anlatımı; küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0196` birebir aynı, `@degisim: paspas -> kızak` (tutuyorsan), ardından `@onarim: 0a485c226992a652509e725c2c7d85f09b0a22fa`, sonra gövde.

### Hikâye 3: tohum elsa-0198 (deneme 3 -> 4)

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
Elsa karlı bir günde sarayın önünde koşuşturuyordu. Kar yavaş yavaş yağıyordu. Birden küçük bir ağacın ince dalı karın altında eğildi. Kar çok ağırdı ve dal kırılabilirdi. Elsa sarayın kraliçesiydi ve saraydaki ağaçları o koruyordu. Küçük ağaca yardım etmek için hemen yanına koştu. Dalın ucunu eliyle yavaşça tuttu. Sonra dalı hafifçe salladı ve kar yere döküldü. Dal yukarı kalktı ve düzeldi. Elsa diğer dalları da temizledi. Küçük ağaç yine dik duruyordu. Elsa çok sevinçliydi ve karda koşuşturmaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "saraydaki ağaçları o koruyordu"
   - Cümle 5: «Elsa sarayın kraliçesiydi ve saraydaki ağaçları o koruyordu.»
   - Açıklama: Karttaki özellik kız kardeşini korumak; hikayede kraliçelik ağaçları korumaya çevrilmiş.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa sarayın kraliçesiydi ve saraydaki ağaçları o koruyordu"
   - Cümle 5: «Elsa sarayın kraliçesiydi ve saraydaki ağaçları o koruyordu.»
   - Açıklama: Karttaki özellik kız kardeşini korumak; hikaye bunu ağaçları korumaya çeviriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0198` birebir aynı, ardından `@onarim: 1f77c53016f0a2302f9c5be73465540a60026d27`, sonra gövde.

### Hikâye 4: tohum elsa-0199 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0199
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'karabiber', fiil 'solmak', sıfat 'kırık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kırık tahta yüzünden eski kızak yolda döndü | kardeşini kendi kızağına aldı ve sıkıca tuttu
@tohum: elsa-0199
@degisim: karabiber -> kızak
Dağın tepesinde, buzdan sarayın önünde kar parlıyordu. Elsa ile Anna kızaklarla yokuştan kayıyordu. Ama Anna'nın kızağında kırık bir tahta vardı, bu yüzden kızak yolda döndü. Anna geriye bakarak kaydı ve karın içinde durdu. Saçları karla doldu ve çok güldü. Elsa kızağa baktı. Kızak çok eskiydi ve rengi solmuştu. Anna aynı kızakla yine kaymak istedi. "Dur, Anna, bu kızağa binme, benim kızağıma gel!" dedi Kraliçe Elsa. Anna hemen Elsa'nın kızağına bindi. Elsa da arkasına oturdu ve onu sıkıca tuttu. Kızak bu kez düz kaydı ve Anna sevinçle bağırdı. Elsa çok mutluydu, çünkü kardeşini korumuştu ve oyunları yine eğlenceliydi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Saçları karla doldu ve çok güldü"
   - Cümle 5: «Saçları karla doldu ve çok güldü.»
   - Açıklama: Bağlı fiilin öznesi 'saçları' oluyor; gülenin Anna olduğu cümlede belirtilmemiş.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kızak çok eskiydi ve rengi solmuştu"
   - Cümle 7: «Kızak çok eskiydi ve rengi solmuştu.»
   - Açıklama: Kızağın solmuş rengi işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0199` birebir aynı, `@degisim: karabiber -> kızak` (tutuyorsan), ardından `@onarim: 1610c6c1e7925ee84420f23803b1843a60fda59a`, sonra gövde.

### Hikâye 5: tohum elsa-0200 (deneme 2 -> 3)

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
@plan: rüzgar gemideki bayrağı hep düşürdü | sarayın arkasında sakin bir köşe buldu
@tohum: elsa-0200
@degisim: mayo -> bayrak
Dağın tepesinde sert bir rüzgar esiyordu. Elsa kızağını bir gemi yapmıştı ve gemi oyunu oynuyordu. Ama gemisine diktiği küçük bayrak rüzgarda hep yere düştü. Elsa oyun için sakin bir yer aradı. Elsa bu buzdan sarayın kraliçesiydi ve sarayın her yanını biliyordu. Sarayın arkasında rüzgar olmayan küçük bir köşe vardı. Kızağı hemen o köşeye çekti. Bayrağı yeniden gemisine dikti. Bayrak bu kez hiç düşmedi. Gemisine oturdu ve uzaklara baktı. Elsa gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "rüzgar gemideki bayrağı hep düşürdü"
   - Cümle 0 (plan satırı): «rüzgar gemideki bayrağı hep düşürdü | sarayın arkasında sakin bir köşe buldu»
   - Açıklama: 'Hep' tekrarlanan eylem bildirir, '-dı' ile uyumsuz; 'hep düşürüyordu' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bayrak rüzgarda hep yere düştü"
   - Cümle 3: «Ama gemisine diktiği küçük bayrak rüzgarda hep yere düştü.»
   - Açıklama: 'Hep' ile basit geçmiş uyumsuz; 'hep yere düşüyordu' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bu buzdan sarayın"
   - Cümle 5: «Elsa bu buzdan sarayın kraliçesiydi ve sarayın her yanını biliyordu.»
   - Açıklama: Saray daha önce hiç anılmadan 'bu' ile gösteriliyor; neyi gösterdiği belli değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bu buzdan sarayın kraliçesiydi"
   - Cümle 5: «Elsa bu buzdan sarayın kraliçesiydi ve sarayın her yanını biliyordu.»
   - Açıklama: 'Bu' daha önce anılmamış bir sarayı gösteriyor; neyi gösterdiği belli değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu buzdan sarayın kraliçesiydi"
   - Cümle 5: «Elsa bu buzdan sarayın kraliçesiydi ve sarayın her yanını biliyordu.»
   - Açıklama: Kartın kraliçe özelliği kız kardeşini korumaktır; burada sarayın her yanını bilmek olarak kartta olmayan biçimde kullanılıyor.
6. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Elsa bu buzdan sarayın kraliçesiydi"
   - Cümle 5: «Elsa bu buzdan sarayın kraliçesiydi ve sarayın her yanını biliyordu.»
   - Açıklama: Kartın kimlik cümlesine göre Elsa krallığın kraliçesidir, buz sarayının kraliçesi olarak verilmesi yanlış bilgi.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu buzdan sarayın kraliçesiydi"
   - Cümle 5: «Elsa bu buzdan sarayın kraliçesiydi ve sarayın her yanını biliyordu.»
   - Açıklama: Daha önce hiç anılmayan saray çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0200` birebir aynı, `@degisim: mayo -> bayrak` (tutuyorsan), ardından `@onarim: 0ce771560f214135243cd7070b9a10c4dafc24ec`, sonra gövde.

### Hikâye 6: tohum elsa-0202 (deneme 2 -> 3)

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
@plan: yumuşak karda kardan heykelin ince kulesi yıkıldı | gerçek saraya bakıp kulenin altını geniş yaptı
@tohum: elsa-0202
@degisim: çeşme -> heykel
Limanda yavaş yavaş kar yağıyordu. Elsa kıyıda kardan bir heykel yapıyordu. Heykel küçük bir saraya benziyordu. Ama heykelin ince kulesi yamuk durdu ve yana yıkıldı. Yumuşak kar ince kuleyi taşıyamamıştı. Elsa bu krallığın kraliçesiydi ve gerçek sarayı hemen arkasındaydı. Dönüp o sarayın kulelerine baktı. Kulelerin altı genişti, üstü inceydi. Elsa limanda koşturup bir yığın kar topladı. Yeni kulenin altını geniş yaptı ve karı elleriyle bastırdı. Bu kez kule düz durdu. Kar yine yağdı ama kule yıkılmadı. Elsa kardan heykeline mutlu mutlu yeni kuleler yaptı.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yumuşak karda kardan heykelin"
   - Cümle 0 (plan satırı): «yumuşak karda kardan heykelin ince kulesi yıkıldı | gerçek saraya bakıp kulenin altını geniş yaptı»
   - Açıklama: Plan satırında 'karda kardan' yan yana gereksiz tekrar ediyor ve cümleyi bozuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu krallığın kraliçesiydi"
   - Cümle 6: «Elsa bu krallığın kraliçesiydi ve gerçek sarayı hemen arkasındaydı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız sarayın yakında olduğunu söylemek için geçiyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "gerçek sarayı hemen arkasındaydı"
   - Cümle 6: «Elsa bu krallığın kraliçesiydi ve gerçek sarayı hemen arkasındaydı.»
   - Açıklama: Çözümü getiren gerçek saray o ana kadar hiç kurulmadan, tam gerektiği anda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0202` birebir aynı, `@degisim: çeşme -> heykel` (tutuyorsan), ardından `@onarim: f78491aa9f6c76a5aec7c7b003d3d48057287a7a`, sonra gövde.

### Hikâye 7: tohum elsa-0203 (deneme 2 -> 3)

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
@plan: kapıyı hızlı açınca karlar geyiğin başına döküldü | özür diledi ve kapının üstüne buzdan çatı yaptı
@tohum: elsa-0203
Elsa sarayının büyük kapısını hızla açtı. Sven kapının önünde bekliyordu ve kapının üstündeki karlar onun başına döküldü. Sven karları silkeledi ve üzgün üzgün geri çekildi. "Özür dilerim, Sven, kapıyı çok hızlı açtım," dedi Elsa. Sonra ellerini kaldırdı ve kapının üstüne buzdan küçük bir çatı yaptı. Çatının şekli değişikti ve ince bir ay gibiydi. "Artık karlar senin başına düşmeyecek, Sven," dedi Elsa. Sven kapının önüne geri geldi ve çatıya baktı. Sonra sevinçle zıpladı ve Elsa'ya sokuldu. Elsa bundan sonra sarayın kapısını hep yavaşça açtı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çatının şekli değişikti"
   - Cümle 6: «Çatının şekli değişikti ve ince bir ay gibiydi.»
   - Açıklama: 'Değişik' burada yanlış anlamda kullanılmış; 'farklıydı' ya da somut bir betim olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çatının şekli değişikti ve ince bir ay gibiydi"
   - Cümle 6: «Çatının şekli değişikti ve ince bir ay gibiydi.»
   - Açıklama: Çatının ay biçimi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0203` birebir aynı, ardından `@onarim: 17875542c52bb45f4508b35ac9396da9e98ec6da`, sonra gövde.

### Hikâye 8: tohum elsa-0207 (deneme 2 -> 3)

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
@plan: uzaktaki gökkuşağına yürüdü ama o hep uzaklaştı | fincanda buz yapıp güneşe tuttu
@tohum: elsa-0207
Bir sabah Elsa sarayının önünde bir fincan sıcak süt içti. Birden karşı tepenin üstünde küçük bir gökkuşağı gördü. Ona doğru yürüdü, ama gökkuşağı hep ondan uzaklaştı. Gökkuşağına yürüyerek kimse yetişemiyordu. Elsa durdu ve elindeki boş fincana baktı. Sonra parmağını fincana doğru tuttu ve içini buzla doldurdu. Buzu fincandan çıkardı ve güneşe doğru kaldırdı. Güneşin ışığı buzun içinden geçti. Karın üstüne küçük, renk renk bir ışık düştü. Eğilip bu ışığa yakından baktı. Elsa çok sevindi, çünkü bu kez renkler tam önündeydi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Karın üstüne küçük"
   - Cümle 9: «Karın üstüne küçük, renk renk bir ışık düştü.»
   - Açıklama: Kar daha önce hiç anılmadığı için 'Karın' kelimesi 'karın' (vücut) ile karışıyor ve anlamı belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0207` birebir aynı, ardından `@onarim: c7181ffb86de953c6ab49e812865a8024bb45819`, sonra gövde.

### Hikâye 9: tohum elsa-0208 (deneme 2 -> 3)

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
@degisim: nefis -> yumuşak
Ormanda karlı ağaçların dalları çok alçaktı. Elsa acıkmıştı ve büyük bir ağacın altında yumuşak bir peynir yedi. Birden daldan başına kar döküldü ve tacı karın içine düştü. Elsa elbisesindeki karı silkeledi ve tacı görmeden yürüdü. Biraz sonra başına dokundu ve tacın yerinde olmadığını fark etti. Elsa bu krallığın kraliçesiydi ve ormanı çok iyi tanıyordu. Hemen peyniri yediği ağacı buldu ve oraya geri döndü. Ağacın altındaki karda parlak bir şey vardı. Karı eliyle yavaşça kenara itti. Tacı oradaydı. Elsa tacın üstündeki karı temizledi ve onu yine başına taktı. Elsa çok sevindi, çünkü tacını geri bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu krallığın kraliçesiydi ve ormanı çok iyi tanıyordu"
   - Cümle 6: «Elsa bu krallığın kraliçesiydi ve ormanı çok iyi tanıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi (kız kardeşini korur) kullanılmıyor, çözüme katkısı olmayan bir etiket olarak geçiyor.
   - Açıklama: Karttaki özellik kız kardeşini koruyan kraliçe; burada kraliçelik ormanı tanımaya bağlanarak karttan farklı kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0208` birebir aynı, `@degisim: nefis -> yumuşak` (tutuyorsan), ardından `@onarim: 62f4698c668f3da8bfe0fc2c1d9af516f51d8ce7`, sonra gövde.

### Hikâye 10: tohum elsa-0210 (deneme 2 -> 3)

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
Dağda soğuk bir rüzgar esiyordu. Elsa ile Olaf, sarayın penceresine koymak için bir kavanozu karla dolduruyordu. Ama rüzgar karı hep kavanozun ağzından uçuruyordu. "Kavanoz hiç dolmuyor!" dedi Olaf. "Olaf, sırtını rüzgara dön ve kavanozu önünde tut," dedi Elsa. Olaf kraliçesinin dediğini hemen yaptı. Rüzgar artık Olaf'ın sırtına çarpıyordu. Elsa eliyle kavanoza kar koydu. Bu kez kar uçmadı ve kavanoz çabucak doldu. Olaf kavanozun kapağını sıkıca kapattı. "Teşekkürler, Elsa, pencere çok güzel olacak!" dedi Olaf. Elsa bundan sonra rüzgarda tedbirli oldu ve kavanozu hep Olaf'ın arkasında doldurdu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf kraliçesinin dediğini hemen yaptı"
   - Cümle 6: «Olaf kraliçesinin dediğini hemen yaptı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) karttaki gibi kullanılmıyor, yalnız emir veren unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) karttaki gibi kullanılmıyor; sorunu kraliçelik değil rüzgara sırt dönme fikri çözüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "rüzgarda tedbirli oldu"
   - Cümle 12: «Elsa bundan sonra rüzgarda tedbirli oldu ve kavanozu hep Olaf'ın arkasında doldurdu.»
   - Açıklama: 'Tedbirli' soyut bir kelime ve 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0210` birebir aynı, `@degisim: doymak -> dolmak` (tutuyorsan), ardından `@onarim: 51348ad98b37bad5958a99a2f994372dba4db44f`, sonra gövde.

### Hikâye 11: tohum elsa-0211 (deneme 2 -> 3)

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
@plan: salondaki sesi neyin yaptığını merak etti | kar şeridini izleyip sesi yapan lambayı buldu
@tohum: elsa-0211
Bir sabah Elsa sarayında ince bir ses duydu. Ses büyük salondan geliyordu. Elsa sesi neyin yaptığını çok merak etti. Sesi iyi duymak için dikkatli adımlarla yavaş yavaş yürüdü. Yerde, pencereye kadar giden ince bir kar şeridi gördü. Elsa bu sarayın kraliçesiydi ve salonu çok iyi tanıyordu. Bu kar şeridi salonda yeniydi ve onu pencereye götürdü. Pencere açık kalmıştı ve içeri rüzgar giriyordu. Rüzgar tavandaki parlak lambanın küçük parçalarını sallıyordu. Parçalar birbirine değince o ince ses çıkıyordu. Elsa sesi yapan şeyi sonunda bulmuştu. Sonra Elsa pencerenin yanına oturdu ve güzel sesi mutlu mutlu dinledi.
```

**Hakem bulguları (7):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bir sabah Elsa sarayında ince bir ses duydu"
   - Cümle 1: «Bir sabah Elsa sarayında ince bir ses duydu.»
   - Açıklama: Başlıktaki yer dağ ama hikaye baştan sona sarayın salonunda geçiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve salonu çok iyi tanıyordu.»
   - Açıklama: Elsa hikayenin ortasında yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve salonu çok iyi tanıyordu"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve salonu çok iyi tanıyordu.»
   - Açıklama: Kraliçelik kartın 'kız kardeşini korur' özelliğiyle değil, salonu tanıma bilgisi olarak kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve salonu çok iyi tanıyordu.»
   - Açıklama: Kraliçelik bilgisi olayın akışına zorla sokulmuş, işlevi zayıf bir ayrıntı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu kar şeridi salonda yeniydi ve onu pencereye götürdü"
   - Cümle 7: «Bu kar şeridi salonda yeniydi ve onu pencereye götürdü.»
   - Açıklama: Kar şeridi kimseyi götürmez; fiil öznesine uymuyor.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yeniydi ve onu pencereye götürdü"
   - Cümle 7: «Bu kar şeridi salonda yeniydi ve onu pencereye götürdü.»
   - Açıklama: 'Onu' zamirinin Elsa'yı mı salonu mu gösterdiği belli değil.
7. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve onu pencereye götürdü"
   - Cümle 7: «Bu kar şeridi salonda yeniydi ve onu pencereye götürdü.»
   - Açıklama: 'onu' zamirinin Elsa'yı mı sesi mi gösterdiği belli değil ve şerit özne olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0211` birebir aynı, ardından `@onarim: 9ec7e44f0f68ed356e79d8ca0b014872422b0d4c`, sonra gövde.

### Hikâye 12: tohum elsa-0213 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0213
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kilit', fiil 'fırçalamak', sıfat 'basit'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: bir kızak vardı ve ikisi de önce binmek istedi | kraliçe basit bir sıra önerdi
@tohum: elsa-0213
@degisim: kilit -> kızak
Rüzgar karlı ağaçların arasında hafifçe esiyordu. Elsa ile Olaf ormandaki küçük bir yokuşun başında duruyordu. Bir kızakları vardı ve ikisi de önce binmek istedi. "Ben önce bineyim!" dedi Olaf. "Olaf, basit bir sıra yapalım, önce sen, sonra ben," dedi Kraliçe Elsa. Olaf hemen kızağa bindi ve yokuştan neşeyle kaydı. Aşağıda durunca kızağı yukarı çekti. Sonra dal kollarıyla kızağın üstündeki karı fırçaladı. "Sıra sende, Elsa," dedi Olaf. Elsa kızağa bindi ve gülerek kaydı. Sonra ikisi sırayla kaymaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "basit bir sıra yapalım"
   - Cümle 5: «"Olaf, basit bir sıra yapalım, önce sen, sonra ben," dedi Kraliçe Elsa.»
   - Açıklama: 'Basit bir sıra yapmak' sırayla binmeyi anlatmak için doğal bir söyleyiş değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 5: «"Olaf, basit bir sıra yapalım, önce sen, sonra ben," dedi Kraliçe Elsa.»
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşi korumak; burada yalnız unvan olarak geçiyor, özellik işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dal kollarıyla kızağın üstündeki karı fırçaladı"
   - Cümle 8: «Sonra dal kollarıyla kızağın üstündeki karı fırçaladı.»
   - Açıklama: Kızaktaki kar sebepsiz kuruluyor ve olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0213` birebir aynı, `@degisim: kilit -> kızak` (tutuyorsan), ardından `@onarim: 95b253b31319bfd6fe528be19146abf0adcce4dc`, sonra gövde.
