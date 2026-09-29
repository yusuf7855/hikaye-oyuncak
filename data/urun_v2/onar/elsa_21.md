# Editör görevi (onarım): Elsa, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0074 (deneme 2 -> 3)

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
Bir sabah Elsa ilk kez ormanda piknik yapmayı denedi. Elinde bir yastık ve küçük bir sepet vardı. Ama güneşli yerde kar erimişti ve yer çok ıslaktı. Elsa yastığını ıslak yere koyamadı. Elsa bu ormanın da kraliçesiydi ve ağaçlarını iyi bilirdi. Hemen büyük, yeşil bir çam ağacına gitti. Ağacın sık dalları karı tutmuştu, bu yüzden altı kuruydu. Elsa yastığını ağacın altındaki kuru yere koydu. Sonra sepetinden ekmek ve elma çıkardı. Elsa yastığına oturdu ve ilk pikniğini mutlu mutlu yaptı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu ormanın da kraliçesiydi ve ağaçlarını iyi bilirdi"
   - Cümle 5: «Elsa bu ormanın da kraliçesiydi ve ağaçlarını iyi bilirdi.»
   - Açıklama: Kraliçe özelliği karttaki anlamıyla değil, ağaçları bilmek diye zorlanmış ve çözüme gerçek katkısı yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu ormanın da kraliçesiydi"
   - Cümle 5: «Elsa bu ormanın da kraliçesiydi ve ağaçlarını iyi bilirdi.»
   - Açıklama: Kraliçelik kartın özellik alanında olmayan ağaçları bilme yeteneğine dönüştürülüyor.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Elsa bu ormanın da kraliçesiydi"
   - Cümle 5: «Elsa bu ormanın da kraliçesiydi ve ağaçlarını iyi bilirdi.»
   - Açıklama: Kartta Elsa'nın ormanın kraliçesi olduğu bilgisi yok; yanlış bilgi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0074` birebir aynı, ardından `@onarim: 67cb39175ac75bf42d7ec29ac4ce3a11749afc7e`, sonra gövde.

### Hikâye 2: tohum elsa-0075 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: şişe düştü ve yumuşak karın içinde kayboldu | karda küçük bir çukur gördü ve orayı kazdı
@tohum: elsa-0075
@degisim: plastik -> boş
Bir sabah Elsa ile Kristoff karlı ormanda komik bir oyun oynuyordu. Kraliçe Elsa'nın isteğiyle Kristoff başında boş bir şişe taşıyordu. Ama havucunu çiğnerken güldü ve şişe yumuşak karın içine düşüp kayboldu. Kristoff karı elleriyle karıştırdı ama şişeyi bulamadı. Elsa kara dikkatle baktı ve küçük bir çukur gördü. "Şişe burada olmalı," dedi Elsa. Çukuru kazdı ve şişeyi çıkardı. Kristoff şişeyi yine başına koydu. Bu kez hiç gülmedi ve şişe düşmedi. Ağaçların arasında yavaşça yürüdü. "Harika bir oyun, Elsa, çok eğlendim!" dedi Kristoff.
```

**Hakem bulguları (8):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "başında boş bir şişe taşıyordu"
   - Cümle 2: «Kraliçe Elsa'nın isteğiyle Kristoff başında boş bir şişe taşıyordu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde başta kırılabilir bir şişe taşınıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kristoff başında boş bir şişe"
   - Cümle 2: «Kraliçe Elsa'nın isteğiyle Kristoff başında boş bir şişe taşıyordu.»
   - Açıklama: Başta şişe taşıma oyunu çocuğun taklit edince şişe düşürüp kırabileceği bir davranış.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa'nın isteğiyle Kristoff"
   - Cümle 2: «Kraliçe Elsa'nın isteğiyle Kristoff başında boş bir şişe taşıyordu.»
   - Açıklama: Elsa ilk cümlede tanıtıldıktan sonra 'Kraliçe Elsa' diye yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa'nın isteğiyle Kristoff"
   - Cümle 2: «Kraliçe Elsa'nın isteğiyle Kristoff başında boş bir şişe taşıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yerine kraliçenin buyruk vermesi olarak kullanılıyor.
   - Açıklama: Kraliçelik kartın özellik alanındaki gibi işe yarar biçimde değil, yalnız unvan olarak geçiyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "başında boş bir şişe taşıyordu"
   - Cümle 2: «Kraliçe Elsa'nın isteğiyle Kristoff başında boş bir şişe taşıyordu.»
   - Açıklama: Sorun başta şişe taşıma oyununda şişenin düşmesi; önemsiz ve saçma bir olay.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama havucunu çiğnerken güldü"
   - Cümle 3: «Ama havucunu çiğnerken güldü ve şişe yumuşak karın içine düşüp kayboldu.»
   - Açıklama: Öznesiz cümlede havucu kimin çiğneyip güldüğü açık değil.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "havucunu çiğnerken güldü"
   - Cümle 3: «Ama havucunu çiğnerken güldü ve şişe yumuşak karın içine düşüp kayboldu.»
   - Açıklama: Havuç sebepsiz beliriyor ve şişenin düşmesini zorlama biçimde getiriyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama havucunu çiğnerken güldü"
   - Cümle 3: «Ama havucunu çiğnerken güldü ve şişe yumuşak karın içine düşüp kayboldu.»
   - Açıklama: Havuç sebepsiz beliriyor ve olayda başka hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0075` birebir aynı, `@degisim: plastik -> boş` (tutuyorsan), ardından `@onarim: ac44643c012e038b1dd0465ad107b2716f6d93d0`, sonra gövde.

### Hikâye 3: tohum elsa-0076 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0076
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'pantolon', fiil 'sığınmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: rüzgar karı yüzlerine çarpıyordu ve oynayamıyorlardı | buzdan büyük bir gemi yapıp içine sığındı
@tohum: elsa-0076
@degisim: pantolon -> gemi
Dağın tepesinde sert bir rüzgar esiyordu. Elsa ile Olaf gemi oyunu oynayacaktı. Ama rüzgar karı yüzlerine çarpıyordu ve oynayamıyorlardı. Elsa ellerini kaldırdı ve buzdan büyük bir gemi yaptı. Geminin duvarları çok yüksekti. İkisi hemen geminin içine sığındı. İçerisi sakin ve sessizdi. Olaf geminin önüne geçti ve "Gemi yola çıkıyor!" dedi. "Nereye gidiyoruz, Olaf?" diye sordu Elsa. Olaf dağın arkasındaki kıpkırmızı güneşi gösterdi. "Oraya gidiyoruz, orada hep yaz var!" dedi Olaf. Elsa güldü ve onun yanına oturdu. "Teşekkürler, Elsa, bu gemi çok güzel!" dedi Olaf.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Dağın tepesinde sert bir rüzgar esiyordu"
   - Cümle 1: «Dağın tepesinde sert bir rüzgar esiyordu.»
   - Açıklama: Sert rüzgar ve gemi birlikte kartın 'yasaklar' öğelerindeki gemi yolculuğu ve fırtına imgesine yaklaşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0076` birebir aynı, `@degisim: pantolon -> gemi` (tutuyorsan), ardından `@onarim: 3d38313325afb904b20bdbae74a6de702d1d71cd`, sonra gövde.

### Hikâye 4: tohum elsa-0077 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0077
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: bir şey yapmak
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'sepet', fiil 'uzamak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: sepetin altı yırtıktı ve kozalaklar düştü | yırtık yerin üstüne buzdan ince bir kapak yaptı
@tohum: elsa-0077
Bir sabah Elsa karlı ormanda küçük bir kardan kale yapıyordu. Kalenin duvarlarını süslemek için sepetine çam kozalakları topladı. Ama sepetin altı yırtıktı ve kozalaklar birer birer kara düştü. Elsa sepete baktı ve yırtık yer biraz daha uzadı. Önce düşen kozalakları yerden aldı. Sonra elini yırtık yerin üstüne koydu ve buzdan ince bir kapak yaptı. Kapak deliği sıkıca kapattı. Elsa kozalakları sepete geri koydu ve hiçbiri düşmedi. Kaleye döndü ve kozalakları duvarlara dizdi. Küçük kale şimdi çok güzel görünüyordu. Elsa bundan sonra kozalak toplamadan önce sepetinin altına baktı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yırtık yer biraz daha uzadı"
   - Cümle 4: «Elsa sepete baktı ve yırtık yer biraz daha uzadı.»
   - Açıklama: Yırtık 'uzamaz', büyür; ayrıca bakmakla yırtığın büyümesi anlamca uyumsuz.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yırtık yer biraz daha uzadı"
   - Cümle 4: «Elsa sepete baktı ve yırtık yer biraz daha uzadı.»
   - Açıklama: Yırtığın bakınca sebepsizce uzaması kuruluyor ama olayda hiçbir sonucu olmuyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa bundan sonra kozalak toplamadan önce sepetinin altına baktı"
   - Cümle 11: «Elsa bundan sonra kozalak toplamadan önce sepetinin altına baktı.»
   - Açıklama: 'Bundan sonra' ile tek seferlik '-dı' uyuşmuyor; 'bakardı' ya da 'bakacaktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0077` birebir aynı, ardından `@onarim: 1c62b14d65687eb46effe45abce582521be7a832`, sonra gövde.

### Hikâye 5: tohum elsa-0078 (deneme 1 -> 2)

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
Elsa ile Kristoff dağda sihirli bir saklambaç oynuyordu. Kristoff kayaların arkasına saklanmıştı. Ama karda her yerde eski ayak izleri vardı ve Elsa onu bulamadı. Elsa biraz düşündü ve ellerini gökyüzüne kaldırdı. Ellerinden ince buz taneleri ve hafif bir kar yağdı. Kar bütün eski izleri kapattı. Elsa sessizce bekledi. Biraz sonra Kristoff başka bir kayanın arkasına koştu. Yeni karda onun ayak izleri hemen göründü. Elsa izlerin peşinden gitti ve Kristoff'u buldu. "Tamam, yakalandım!" dedi Kristoff gülerek. Elsa çok sevindi, çünkü saklanan Kristoff'u sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sonra Kristoff başka bir kayanın arkasına koştu"
   - Cümle 8: «Biraz sonra Kristoff başka bir kayanın arkasına koştu.»
   - Açıklama: Çözüm, saklanan Kristoff'un sebepsizce yer değiştirmesine dayanıyor; Elsa'nın kar yağdırması tek başına onu buldurmuyor.
   - Açıklama: Saklanan Kristoff'un sebepsizce yer değiştirmesi çözümü Elsa'nın yerine getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0078` birebir aynı, `@degisim: sünger -> kaya` (tutuyorsan), ardından `@onarim: 3cc1aa44aaf149b887b72132fa4a4c356f4c139a`, sonra gövde.

### Hikâye 6: tohum elsa-0079 (deneme 1 -> 2)

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
Bir sabah sarayın önü çok sisliydi. Elsa ile Olaf dışarıdan saraya elma taşıyordu. Olaf küçük kızağına çok elma yüklemişti ve kızak kıpırdamıyordu. "Bu çok ağır, Elsa!" dedi Olaf. Kraliçe Elsa kendi büyük kızağını onun yanına çekti. "Elmaları paylaşalım, Olaf," dedi Elsa. Elsa elmaların yarısını kendi kızağına aldı. Şimdi ikisinin yükü de hafifti. İkisi sisin içinde yan yana yürüdü ve kapıya vardı. Kapıda Olaf en güzel elmayı Elsa'ya uzattı. "Teşekkürler, Elsa, birlikte çok kolay oldu!" dedi Olaf.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kendi büyük"
   - Cümle 5: «Kraliçe Elsa kendi büyük kızağını onun yanına çekti.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kendi büyük kızağını onun yanına çekti"
   - Cümle 5: «Kraliçe Elsa kendi büyük kızağını onun yanına çekti.»
   - Açıklama: Kraliçe özelliği yalnız unvan olarak anılıyor; sorun paylaşmayla çözülüyor, özellik işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kendi büyük kızağını"
   - Cümle 5: «Kraliçe Elsa kendi büyük kızağını onun yanına çekti.»
   - Açıklama: Tohum özelliği kraliçelik yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0079` birebir aynı, `@degisim: elmas -> elma` (tutuyorsan), ardından `@onarim: 7f9ec2f9aa55653951718bbf744e96d28f6cfafa`, sonra gövde.

### Hikâye 7: tohum elsa-0080 (deneme 1 -> 2)

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
@plan: geyik açtı ve kutudaki ekmekler biberliydi | kutunun dibinde havuç bulup ona verdi
@tohum: elsa-0080
Elsa elinde bir yemek kutusuyla buz sarayından çıktı. Kapının önünde Sven burnuyla karı karıştırıyordu. Karın altında hiç ot yoktu ve Sven çok acıkmıştı. Kraliçe Elsa hemen kutusunu açtı. Kutuda biberli ekmekler vardı. Sven bir ekmeği kokladı ve başını çevirdi. "Biberli ekmeği sevmiyorsun, değil mi?" diye sordu Elsa. Sven başını iki yana salladı. Elsa kutunun dibine baktı ve iki havuç buldu. Havuçları hemen Sven'e uzattı. Sven onları yedi ve sevinçle zıpladı. "Afiyet olsun, Sven, bunlar senin için!" dedi Elsa gülerek.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geyik açtı ve kutudaki ekmekler biberliydi"
   - Cümle 0 (plan satırı): «geyik açtı ve kutudaki ekmekler biberliydi | kutunun dibinde havuç bulup ona verdi»
   - Açıklama: 'Açtı' yanlış kelime; 'acıktı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geyik açtı ve kutudaki"
   - Cümle 0 (plan satırı): «geyik açtı ve kutudaki ekmekler biberliydi | kutunun dibinde havuç bulup ona verdi»
   - Açıklama: 'açtı' fiili bu bağlamda yanlış anlamda ve geyiğe uymuyor.
   - Açıklama: 'Açtı' yanlış kelime; geyik 'acıktı' olmalı.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "geyik açtı ve kutudaki"
   - Cümle 0 (plan satırı): «geyik açtı ve kutudaki ekmekler biberliydi | kutunun dibinde havuç bulup ona verdi»
   - Açıklama: Plan satırında yazım hatası var; 'geyik acıktı' olmalı.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen kutusunu açtı"
   - Cümle 4: «Kraliçe Elsa hemen kutusunu açtı.»
   - Açıklama: Zaten tanıtılmış Elsa 'Kraliçe Elsa' olarak yeniden tanıtılıyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen kutusunu"
   - Cümle 4: «Kraliçe Elsa hemen kutusunu açtı.»
   - Açıklama: Zaten tanıtılmış Elsa 'Kraliçe Elsa' diye yeniden tanıtılıyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen kutusunu"
   - Cümle 4: «Kraliçe Elsa hemen kutusunu açtı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen kutusunu açtı"
   - Cümle 4: «Kraliçe Elsa hemen kutusunu açtı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor ve buz özelliği de ayrıca anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0080` birebir aynı, ardından `@onarim: c3a477d4cc813d50f4bc88e173bcae8ce479cc11`, sonra gövde.

### Hikâye 8: tohum elsa-0081 (deneme 1 -> 2)

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
Dağın tepesinde güneş parlıyordu. Elsa pasta oyunu oynuyordu ve karla büyük bir pasta yapıyordu. Ama güneşli havada kar köpük gibi yumuşadı ve pastanın üstü yana kaydı. Elsa kayan karı eliyle geri koydu ama kar yine aşağı aktı. Biraz düşündü ve ellerini salladı. Önünde buzdan sağlam bir pasta belirdi. Yeni pasta güneşte pırıl pırıl parladı ve hiç kaymadı. Elsa yakındaki bir çamdan küçük dallar aldı. Pastanın üstünü bu yeşil dallarla süsledi. Sonra pastayı dikkatle sarayın kapısına taşıdı. Elsa pasta oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "pasta oyunu oynuyordu ve karla büyük bir pasta yapıyordu"
   - Cümle 2: «Elsa pasta oyunu oynuyordu ve karla büyük bir pasta yapıyordu.»
   - Açıklama: 'Pasta' kelimesi aynı cümlede gereksiz yere tekrarlanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kar yine aşağı aktı"
   - Cümle 4: «Elsa kayan karı eliyle geri koydu ama kar yine aşağı aktı.»
   - Açıklama: Kar akmaz; fiil öznesine uymuyor, 'kaydı' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "pastayı dikkatle sarayın kapısına taşıdı"
   - Cümle 10: «Sonra pastayı dikkatle sarayın kapısına taşıdı.»
   - Açıklama: Saray sebepsiz beliriyor ve pastanın oraya taşınması olayda hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra pastayı dikkatle sarayın kapısına taşıdı"
   - Cümle 10: «Sonra pastayı dikkatle sarayın kapısına taşıdı.»
   - Açıklama: Pastanın saraya taşınması sebepsiz ve olaya hiçbir katkısı olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0081` birebir aynı, `@degisim: sormak -> süslemek` (tutuyorsan), ardından `@onarim: 1d8e6da5181c54e9bc4fe5608d0ab18d09c702b8`, sonra gövde.
