# Editör görevi (onarım): Elsa, onarım partisi 26

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar26.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar26.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0073 (deneme 4 -> 5)

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
@plan: rüzgar eldiveni karın içine düşürdü ve eldiven görünmedi | sesin geldiği yeri buldu ve eldiveni buzdan kürekle çıkardı
@tohum: elsa-0073
@degisim: saat -> eldiven
Elsa, Sven ile karlı ormanda yürüyordu. Rüzgar esti ve Elsa'nın elindeki eldiveni karın içine düşürdü. Elsa yere baktı ama eldiveni göremedi. "Sven, eldivenimi bulmama yardım eder misin?" diye sordu Elsa. Sven başını salladı ve karı koklamaya başladı. Biraz sonra bir ağacın dibinden tık tık diye bir ses geldi. Elsa bu sesi merak etti ve ağaca doğru yürüdü. Sven orada ayağıyla yere vuruyordu. Elsa buzdan küçük bir kürek yaptı. Küreği yavaşça kara soktu ve eldiveni çıkardı. Eldiven ıslaktı ama hiç yırtılmamıştı. Sven sevinçle kısa bir ses verdi. Elsa çok sevindi, çünkü eldivenini sesin geldiği yerde bulmuştu.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sven orada ayağıyla yere vuruyordu"
   - Cümle 8: «Sven orada ayağıyla yere vuruyordu.»
   - Açıklama: Eldivenin yerini Elsa değil Sven buluyor; Elsa yalnız sesi takip edip kazıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0073` birebir aynı, `@degisim: saat -> eldiven` (tutuyorsan), ardından `@onarim: bdbc0fe0c7536fda0b56a582f450e5373fa4e53c`, sonra gövde.

### Hikâye 2: tohum elsa-0074 (deneme 4 -> 5)

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
Bir sabah Elsa ilk kez ormanda piknik yapmayı denedi. Elinde bir yastık ve küçük bir sepet vardı. Ama güneşli yerde kar erimişti ve yer çok ıslaktı. Elsa yastığını ıslak yere koyamadı. Elsa iyi bir kraliçeydi ve sarayın yastığını ıslatmak istemedi. Hemen büyük, yeşil bir çam ağacına gitti. Ağacın sık dalları karı tutmuştu, bu yüzden altı kuruydu. Elsa yastığını ağacın altındaki kuru yere koydu. Sonra sepetinden ekmek ve elma çıkardı. Elsa yastığına oturdu ve ilk pikniğini mutlu mutlu yaptı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve sarayın yastığını"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve sarayın yastığını ıslatmak istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir; kız kardeşini korur) sorunun çözümünde hiçbir işe yaramıyor, yalnız etiket olarak geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve sarayın yastığını ıslatmak istemedi"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve sarayın yastığını ıslatmak istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği sorunu çözmeye katkı vermiyor, yalnız etiket olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa iyi bir kraliçeydi ve sarayın yastığını ıslatmak istemedi"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve sarayın yastığını ıslatmak istemedi.»
   - Açıklama: İyi bir kraliçe olmak yastığı ıslatmamanın sebebi değil; cümle olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0074` birebir aynı, ardından `@onarim: 2ef324916ffde3834face7048e2d7ccadb940b58`, sonra gövde.

### Hikâye 3: tohum elsa-0078 (deneme 3 -> 4)

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
@plan: karda her yerde ayak izi vardı ve saklanan bulunamadı | kar yağdırıp eski izleri kapattı ve yeni izleri buldu
@tohum: elsa-0078
@degisim: sünger -> kaya
Elsa ile Kristoff dağda saklambaç oynuyordu. Kristoff kayaların arkasına saklanmıştı. Ama karda her yerde eski ayak izleri vardı ve Elsa onu bulamadı. Elsa biraz düşündü ve ellerini gökyüzüne kaldırdı. Ellerinden buz taneleri ve sihirli bir kar yağdı. Yeni kar bütün eski izleri kapattı. Kristoff bu güzel karı görmek için kayanın arkasından çıktı. Sonra yine koşarak kayanın arkasına döndü. Karda onun yeni ayak izleri hemen göründü. Elsa izlerin peşinden gitti ve Kristoff'u buldu. "Tamam, yakalandım!" dedi Kristoff gülerek. Elsa çok sevindi, çünkü saklanan Kristoff'u sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kristoff bu güzel karı görmek için kayanın arkasından çıktı"
   - Cümle 7: «Kristoff bu güzel karı görmek için kayanın arkasından çıktı.»
   - Açıklama: Çözüm Elsa'nın eyleminden değil, saklanan Kristoff'un rastlantıyla dışarı çıkıp yeni iz bırakmasından geliyor.
   - Açıklama: Çözüm Kristoff'un sebepsizce saklandığı yerden çıkıp yeni iz bırakmasıyla geliyor, Elsa'nın çabasından çıkmıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Karda onun yeni ayak izleri hemen göründü"
   - Cümle 9: «Karda onun yeni ayak izleri hemen göründü.»
   - Açıklama: Kar yağdırmak tek başına sorunu çözmüyor; çözüm Kristoff'un çıkıp dönmesine bağlı dolaylı bir yoldan geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0078` birebir aynı, `@degisim: sünger -> kaya` (tutuyorsan), ardından `@onarim: bfc72cf2a921fa1f7d537b80dc1ffff29414ac25`, sonra gövde.

### Hikâye 4: tohum elsa-0079 (deneme 3 -> 4)

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
Bir sabah sarayın önü çok sisliydi. Elsa ile Olaf dışarıdan saraya elma taşıyordu. Olaf küçük kızağına çok elma yüklemişti ve kızak kıpırdamıyordu. "Bu çok ağır, Elsa!" dedi Olaf. Elsa iyi bir kraliçeydi ve Olaf'a hemen yardım etmek istedi. Elsa'nın kızağı ise çok büyüktü. Elsa bu büyük kızağı Olaf'ın yanına çekti. "Elmaları paylaşalım, Olaf," dedi Elsa. Elsa elmaların yarısını kendi kızağına aldı. Şimdi ikisinin yükü de hafifti. İkisi sisin içinde yan yana yürüdü ve kapıya vardı. Kapıda Olaf en güzel elmayı Elsa'ya uzattı. "Teşekkürler, Elsa, birlikte çok kolay oldu!" dedi Olaf.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve Olaf'a"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve Olaf'a hemen yardım etmek istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yükü paylaşma çözümüne katkı vermiyor, yalnız etiket olarak geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve Olaf'a hemen yardım etmek istedi"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve Olaf'a hemen yardım etmek istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor, yalnız etiket olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa'nın kızağı ise çok büyüktü"
   - Cümle 6: «Elsa'nın kızağı ise çok büyüktü.»
   - Açıklama: Elsa'nın büyük kızağı daha önce kurulmadan sebepsizce beliriyor ve çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0079` birebir aynı, `@degisim: elmas -> elma` (tutuyorsan), ardından `@onarim: 3a499119a05e8d5ada8c04cb5b8bcc0d43c1dc1c`, sonra gövde.

### Hikâye 5: tohum elsa-0080 (deneme 3 -> 4)

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
@plan: geyik acıkmıştı ve kutudaki ekmekler biberliydi | kutudaki havuçları ona verdi
@tohum: elsa-0080
Elsa elinde bir yemek kutusuyla sarayından çıktı. Kapının önünde Sven burnuyla karı karıştırıyordu. Karın altında hiç ot yoktu ve Sven çok acıkmıştı. Elsa iyi bir kraliçeydi ve Sven'i aç bırakmak istemedi. Hemen kutusunu açtı. Kutunun üstünde biberli ekmekler, dibinde iki havuç vardı. Sven bir ekmeği kokladı ve başını çevirdi. "Biberli ekmeği sevmiyorsun, değil mi?" diye sordu Elsa. Sven başını iki yana salladı. Elsa ekmekleri kaldırdı ve iki havucu aldı. Havuçları hemen Sven'e uzattı. Sven onları yedi ve sevinçle zıpladı. "Afiyet olsun, Sven, bunlar senin için!" dedi Elsa gülerek.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve Sven'i"
   - Cümle 4: «Elsa iyi bir kraliçeydi ve Sven'i aç bırakmak istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği çözüme katkı vermiyor; yalnız genel bir iyilik gerekçesi olarak anılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kutunun üstünde biberli ekmekler"
   - Cümle 6: «Kutunun üstünde biberli ekmekler, dibinde iki havuç vardı.»
   - Açıklama: Ekmekler kutunun içinde üstte; 'kutunun üstünde' kutunun dışını anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0080` birebir aynı, ardından `@onarim: e2657fad1d115551d2c28e52d7914f3cc95a945c`, sonra gövde.

### Hikâye 6: tohum elsa-0084 (deneme 2 -> 3)

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
Rüzgar karlı ağaçların arasında hafif hafif esiyordu. Elsa ile Olaf ormanda kardan küçük bir arkadaş yapıyordu. Ama rüzgar kardan arkadaşın başını yere düşürdü. "Arkadaşımın başı düştü, Elsa!" dedi Olaf üzgün üzgün. Elsa iyi bir kraliçeydi ve Olaf'a yardım etmek istedi. Hemen Olaf'ın yanına eğildi. Başı yerine koydu ve karı iki eliyle bastırdı. Sonra kendi temiz eşarbını çıkardı. Eşarbı yeni arkadaşın boynuna sıkıca bağladı. Rüzgar yine esti ama baş artık düşmedi. "Yaşasın, yeni arkadaşım hazır!" dedi Olaf. Elsa ile Olaf yeni arkadaşın yanında mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama rüzgar kardan arkadaşın başını yere düşürdü"
   - Cümle 3: «Ama rüzgar kardan arkadaşın başını yere düşürdü.»
   - Açıklama: Rüzgar hafif hafif eserken kardan başı düşürmesi akla yatkın bir sebep değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve Olaf'a"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve Olaf'a yardım etmek istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor, yalnız yardım gerekçesi olarak etiketleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0084` birebir aynı, `@degisim: yaratmak -> yapmak` (tutuyorsan), ardından `@onarim: 884c09f76781d8fe45cd17c65f1f1590a1dd8a6c`, sonra gövde.

### Hikâye 7: tohum elsa-0085 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0085
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ekmek', fiil 'dilemek', sıfat 'siyah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: kurabiye torbası kaygan karda kayıp derin kara düştü | geyikten yardım diledi ve geyik torbayı getirdi
@tohum: elsa-0085
@degisim: ekmek -> kurabiye
Karlı dağın tepesinde güneşli bir sabahtı. Elsa, Sven için siyah bir torbada kurabiye taşıyordu. Ama torba kaygan karda kaydı ve aşağıdaki derin karın içine düştü. Elsa oraya gidemedi, çünkü kar onun için çok derindi. Siyah torba beyaz karda kolayca görünüyordu. Elsa, Sven'den yardım diledi. "Sven, aşağı in ve torbayı bana getir," dedi kraliçe Elsa. Sven kraliçenin sözünü dinledi ve uzun bacaklarıyla karda koştu. Torbayı dişleriyle tuttu ve yukarı çıktı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Sven sevinçle başını salladı. Sonra ikisi buzdan sarayın önüne oturdu ve kurabiyeleri mutlu mutlu paylaştı.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Siyah torba beyaz karda kolayca görünüyordu"
   - Cümle 5: «Siyah torba beyaz karda kolayca görünüyordu.»
   - Açıklama: Torbanın kolay görünmesi işe yarayacakmış gibi kuruluyor ama çözümde hiç kullanılmıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "aşağı in ve torbayı bana getir"
   - Cümle 7: «"Sven, aşağı in ve torbayı bana getir," dedi kraliçe Elsa.»
   - Açıklama: Elsa'nın kendisi için çok derin dediği kara bir arkadaşını gönderiyor; çocuk için taklit edilebilir tehlikeli davranış örneği.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçenin sözünü dinledi"
   - Cümle 8: «Sven kraliçenin sözünü dinledi ve uzun bacaklarıyla karda koştu.»
   - Açıklama: Kraliçe özelliği birden çok kez ve kartın özellik alanındaki koruma anlamında değil, emir verme olarak kullanılıyor.
   - Açıklama: Özellikler alanında kraliçelik kız kardeşini korumak olarak veriliyor; burada Sven'e emir veren bir otorite olarak kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra ikisi buzdan sarayın önüne oturdu"
   - Cümle 12: «Sonra ikisi buzdan sarayın önüne oturdu ve kurabiyeleri mutlu mutlu paylaştı.»
   - Açıklama: Buzdan saray önceden hiç kurulmadan son cümlede sebepsizce beliriyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "ikisi buzdan sarayın önüne oturdu"
   - Cümle 12: «Sonra ikisi buzdan sarayın önüne oturdu ve kurabiyeleri mutlu mutlu paylaştı.»
   - Açıklama: Hikaye dağın tepesinde başlıyor ama buzdan sarayın önünde bitiyor; sahne değişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0085` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: f0ebbaf5c91810149b2dd97d439ddb12ca899d3f`, sonra gövde.

### Hikâye 8: tohum elsa-0087 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0087
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kese', fiil 'kullanmak', sıfat 'berrak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: soğukta ip donup sıkı bir düğüm oldu | düğümü açmak için arkadaşından yardım istedi
@tohum: elsa-0087
@degisim: berrak -> mavi
Elsa, Kristoff ile karlı dağda yürüyordu. Elsa kurabiye yemek için küçük bir keseyi açmak istedi. Ama soğukta ipi donmuş ve sıkı bir düğüm olmuştu. Elsa bir kraliçeydi ama düğümü tek başına açamadı. "Kristoff, bu düğümü açabilir misin?" diye sordu Elsa. Kristoff keseyi aldı ve güçlü parmaklarını kullandı. Önce düğümü avucunda biraz ısıttı. Sonra ipi yavaşça çekti ve düğüm açıldı. "İşte kurabiyeler, Elsa!" dedi Kristoff. Elsa kurabiyeleri ikiye böldü ve yarısını Kristoff'a verdi. İkisi mavi gökyüzünün altında kurabiyelerini yedi. Elsa çok mutlu oldu, çünkü yardım isteyince düğüm hemen açılmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ama"
   - Cümle 4: «Elsa bir kraliçeydi ama düğümü tek başına açamadı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ama düğümü tek başına açamadı"
   - Cümle 4: «Elsa bir kraliçeydi ama düğümü tek başına açamadı.»
   - Açıklama: Tohumdaki kraliçe özelliği çözüme hiçbir katkı yapmıyor, 'ozellikler' alanındaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0087` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: 4f0ac74d2dba04a32b13bda91ba2d54a5da963b5`, sonra gövde.

### Hikâye 9: tohum elsa-0088 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0088
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çörek', fiil 'çırpmak', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yıldız gibi kar tanesi çok küçüktü ve hemen eridi | buzdan büyük bir kar tanesi yaptı
@tohum: elsa-0088
Dağda hafif hafif kar yağıyordu. Elsa'nın eline yıldıza benzeyen küçük bir kar tanesi kondu. Elsa ona yakından bakmak istedi. Ama kar tanesi çok küçüktü ve elinde hemen eridi. Elsa başka kar tanelerini de yakaladı. Onlar da hemen eridi. Elsa biraz düşündü. Sonra ellerini havaya kaldırdı ve buzdan büyük bir kar tanesi yaptı. Bu kar tanesi bir çörek kadar büyüktü. Altı ucu vardı ve çok parlaktı. Elsa her ucuna rahatça baktı. Uçlarda minik dallar ve ince çizgiler gördü. Elsa sevinçle ellerini çırptı. Sonra kar tanesini karın üstüne koydu ve mutlu mutlu gülümsedi.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama kar tanesi çok küçüktü ve elinde hemen eridi.»
   - Açıklama: Kar tanesinin küçük olup erimesi sorunu ilk 3 cümlede değil 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0088` birebir aynı, ardından `@onarim: eac9d8e070e464a08333df487d1856a768e7a5cb`, sonra gövde.

### Hikâye 10: tohum elsa-0089 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0089
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'misket', fiil 'kıvırmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: karda ayak izi olmayan ince izler vardı | buzdan bir top yuvarladı ve izleri neyin yaptığını buldu
@tohum: elsa-0089
@degisim: huzurlu -> yuvarlak
Bir sabah Elsa karlı ormanda yürüyordu. Birden karın üstünde ince ve uzun izler gördü. Karda hiç ayak izi yoktu ve Elsa bunu çok merak etti. İzler karlı bir dalın altından başlayıp yokuştan aşağı iniyordu. Elsa parmaklarını kıvırdı ve avucunda buzdan küçük bir top yaptı. Top bir misket kadar küçük ve yuvarlaktı. Elsa topu yokuştan aşağı bıraktı. Top yuvarlandı ve karda aynı ince izi yaptı. Sonra Elsa dalı hafifçe salladı ve daldan bir kar parçası düştü. Kar parçası da yokuştan aşağı yuvarlandı ve yeni bir iz yaptı. Elsa çok sevindi, çünkü izleri daldan düşen karın yaptığını bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Karda hiç ayak izi yoktu ve Elsa bunu çok merak etti"
   - Cümle 3: «Karda hiç ayak izi yoktu ve Elsa bunu çok merak etti.»
   - Açıklama: Karda ince izler görmek bir sorun değil yalnız merak edilen bir durum; çocuğun önemseyeceği bir sorun kurulmuyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra Elsa dalı hafifçe salladı"
   - Cümle 9: «Sonra Elsa dalı hafifçe salladı ve daldan bir kar parçası düştü.»
   - Açıklama: Çözüm top yapma, topu yuvarlama ve dalı sallama olarak ikiden fazla adım sürüyor ve top denemesi sebebi doğrudan bulmuyor.
   - Açıklama: Buz topu denemesi izlerin kaynağını göstermiyor, çözüm ancak ayrı bir üçüncü adımla (dalı sallamak) geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0089` birebir aynı, `@degisim: huzurlu -> yuvarlak` (tutuyorsan), ardından `@onarim: bc1733377bbdae8bcb98015ed6041693dd4f30d1`, sonra gövde.

### Hikâye 11: tohum elsa-0090 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0090
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sırayla oynamak
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çatal', fiil 'somurtmak', sıfat 'temkinli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: iki arkadaş halkaları aynı anda atınca halkalar çarpıştı | sırayla atmayı önerdi
@tohum: elsa-0090
@degisim: temkinli -> dikkatli
Bir sabah Elsa ile Kristoff karlı dağda halka oyunu oynuyordu. Elsa buzdan halkalar yapmış ve çatal bir dalı karın içine dikmişti. Ama ikisi halkaları hep aynı anda attı ve halkalar havada çarpıştı. Hiçbir halka dala geçmedi ve Kristoff somurttu. "Sırayla atalım, önce sen at, Kristoff," dedi Elsa. Kristoff dikkatli bir şekilde dala baktı ve halkayı yavaşça attı. Halka dalın bir ucuna geçti. Sonra Elsa attı ve onun halkası öbür uca geçti. Kristoff sevinçle güldü ve ellerini çırptı. "Sırayla oynamak çok daha eğlenceli, Elsa!" dedi Kristoff.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa buzdan halkalar yapmış"
   - Cümle 2: «Elsa buzdan halkalar yapmış ve çatal bir dalı karın içine dikmişti.»
   - Açıklama: Buz özelliği yalnız başlangıç düzeninde geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0090` birebir aynı, `@degisim: temkinli -> dikkatli` (tutuyorsan), ardından `@onarim: dee5b0ca1d7e3f5ea210dc0a623a18bdd93de743`, sonra gövde.

### Hikâye 12: tohum elsa-0091 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0091
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'ot', fiil 'anlamak', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: saklanan arkadaşı sık otların içinde görünmedi | otlara kar döktü ve sallanan otları buldu
@tohum: elsa-0091
Elsa, Olaf ile fiyort kıyısında saklambaç oynuyordu. Olaf uzun ve kuru otların içine saklandı. Otlar çok sıktı ve Elsa onu hiç göremedi. Birden otlardan çıtır çıtır bir ses geldi. Ama Elsa sesin nereden geldiğini anlamadı. Elsa elini salladı ve elinden buz ve kar çıktı. Kar otların üstüne yağdı ve her yer bembeyaz oldu. Sonra ses yine geldi ve bazı otlar sallandı. Onların üstündeki kar yere döküldü. Elsa oraya yürüdü ve yavaşça baktı. Olaf otların arasında gülerek oturuyordu. "Ben biraz döndüm ve kuru otlar çıtır çıtır etti," dedi Olaf. "Buldum seni, Olaf, bu oyun çok güzeldi!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf ile fiyort kıyısında"
   - Cümle 1: «Elsa, Olaf ile fiyort kıyısında saklambaç oynuyordu.»
   - Açıklama: 'Fiyort' 3 yaşındaki bir çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0091` birebir aynı, ardından `@onarim: 5a15208d2b31d42b325ba35e2c48dd9c2c08bf01`, sonra gövde.
