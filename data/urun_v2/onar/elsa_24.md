# Editör görevi (onarım): Elsa, onarım partisi 24

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar24.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar24.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0086 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0086
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'düdük', fiil 'yürümek', sıfat 'yapışkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: geyiğin bacakları yapışkan kara battı | buzdan sert bir yol yaptı
@tohum: elsa-0086
Ormanda karlı ağaçların arasına yumuşak kar yağıyordu. Elsa saraya dönmek için düdüğünü öttürdü ve Sven'i çağırdı. Ama Sven yürüyemedi, çünkü bacakları derin ve yapışkan kara batmıştı. Sven üzgün bir ses çıkardı. Elsa ellerini Sven'e doğru uzattı. Elinden buz çıktı ve karın üstünde sert bir yol oldu. Yol, Sven'in tam önüne kadar uzandı. Sven ön ayaklarını sert yola koydu. Sonra bacaklarını kardan tek tek çekti. Buzdan yolda yavaş yavaş yürüdü ve Elsa'nın yanına geldi. Sven başını sevinçle Elsa'nın omzuna sürdü. "Aferin, Sven, şimdi birlikte saraya dönebiliriz!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "düdüğünü öttürdü ve Sven'i çağırdı"
   - Cümle 2: «Elsa saraya dönmek için düdüğünü öttürdü ve Sven'i çağırdı.»
   - Açıklama: Kartta Elsa'nın Sven'i çağırdığı bir düdük eşyası yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0086` birebir aynı, ardından `@onarim: 975cb886407cbd9226a9253d51420e8f7f21a756`, sonra gövde.

### Hikâye 2: tohum elsa-0087 (deneme 1 -> 2)

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
Elsa, Kristoff ile karlı dağda yürüyordu. Elsa kurabiye yemek için küçük bir keseyi açmak istedi. Ama soğukta ipi donmuş ve sıkı bir düğüm olmuştu. Elsa düğümü açmaya çalıştı ama açamadı. "Kristoff, bu düğümü açabilir misin?" diye sordu Elsa. Kristoff keseyi aldı ve güçlü parmaklarını kullandı. Önce düğümü avucunda biraz ısıttı. Sonra ipi yavaşça çekti ve düğüm açıldı. "İşte kurabiyeler, Kraliçe Elsa!" dedi Kristoff. Elsa kurabiyeleri ikiye böldü ve yarısını Kristoff'a verdi. İkisi berrak gökyüzünün altında kurabiyelerini yedi. Elsa çok mutlu oldu, çünkü yardım istediği için düğüm hemen açılmıştı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "İşte kurabiyeler, Kraliçe Elsa"
   - Cümle 9: «"İşte kurabiyeler, Kraliçe Elsa!" dedi Kristoff.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız hitapta geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İkisi berrak gökyüzünün altında"
   - Cümle 11: «İkisi berrak gökyüzünün altında kurabiyelerini yedi.»
   - Açıklama: 'Berrak' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü yardım istediği için"
   - Cümle 12: «Elsa çok mutlu oldu, çünkü yardım istediği için düğüm hemen açılmıştı.»
   - Açıklama: 'Çünkü' ile '-diği için' aynı cümlede birlikte kullanılmış; sebep bağlacı çift.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0087` birebir aynı, ardından `@onarim: 33a68a3fc7a5672014f2462df365541c1757bb6d`, sonra gövde.

### Hikâye 3: tohum elsa-0088 (deneme 1 -> 2)

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
@plan: yıldız gibi kar tanesi elinde hemen eridi | buzdan büyük bir kar tanesi yaptı
@tohum: elsa-0088
Dağda hafif hafif kar yağıyordu. Elsa'nın eline yıldıza benzeyen küçük bir kar tanesi kondu. Elsa ona yakından bakmak istedi ama kar tanesi hemen eridi. Elsa başka kar tanelerini de yakaladı. Hepsi çok küçüktü ve elinde hemen eriyordu. Elsa biraz düşündü. Sonra ellerini havaya kaldırdı ve buzdan büyük bir kar tanesi yaptı. Bu kar tanesi bir çörek kadar büyüktü. Altı ucu vardı ve çok parlaktı. Elsa her ucuna rahatça baktı. Uçlarda minik dallar ve ince çizgiler gördü. Elsa sevinçle ellerini çırptı. Sonra kar tanesini sarayının kapısına astı ve ona mutlu mutlu baktı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kar tanesi hemen eridi"
   - Cümle 3: «Elsa ona yakından bakmak istedi ama kar tanesi hemen eridi.»
   - Açıklama: Kar tanesinin neden eridiği hikayede söylenmiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "kar tanesini sarayının kapısına astı"
   - Cümle 13: «Sonra kar tanesini sarayının kapısına astı ve ona mutlu mutlu baktı.»
   - Açıklama: Hikaye dağda geçerken sonda sarayın kapısına geçiliyor; tek sahne kuralı bozuluyor.
   - Açıklama: Hikaye dağda geçerken sonda sebepsizce sarayın kapısına geçiliyor; tek sahne belirsizleşiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0088` birebir aynı, ardından `@onarim: 4ff55cd4fde1254e39dc5f309a95f4f408f2e51f`, sonra gövde.

### Hikâye 4: tohum elsa-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Bir sabah Elsa karlı ormanda yürüyordu. Birden karın üstünde ince ve uzun izler gördü. Karda hiç ayak izi yoktu ve Elsa bunu çok merak etti. İzler küçük bir yokuştan aşağı iniyordu. Elsa parmaklarını kıvırdı ve avucunda buzdan küçük bir top yaptı. Top bir misket kadar küçük ve yuvarlaktı. Elsa topu yokuştan aşağı bıraktı. Top yuvarlandı ve karda aynı ince izi yaptı. Tam o sırada bir daldan küçük bir kar parçası düştü. Kar parçası da yokuştan aşağı yuvarlandı ve yeni bir iz yaptı. Elsa çok sevindi, çünkü izleri daldan düşen karın yaptığını bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada bir daldan küçük bir kar parçası düştü"
   - Cümle 9: «Tam o sırada bir daldan küçük bir kar parçası düştü.»
   - Açıklama: İzlerin sebebi Elsa'nın denemesinden değil, tam o anda tesadüfen düşen kar parçasından çıkıyor.
   - Açıklama: Cevabı veren kar parçası tesadüfen tam o anda düşüyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0089` birebir aynı, `@degisim: huzurlu -> yuvarlak` (tutuyorsan), ardından `@onarim: 65df39ccb271c443ecf68a969c58d22dcf666b05`, sonra gövde.

### Hikâye 5: tohum elsa-0090 (deneme 1 -> 2)

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
Bir sabah Elsa ile Kristoff karlı dağda halka oyunu oynuyordu. Elsa buzdan halkalar yapmış ve çatal bir dalı karın içine dikmişti. Ama ikisi halkaları hep aynı anda attı ve halkalar havada çarpıştı. Hiçbir halka dala geçmedi ve Kristoff somurttu. "Sırayla atalım, önce sen at, Kristoff," dedi Elsa. Kristoff temkinli bir şekilde nişan aldı ve halkayı yavaşça attı. Halka dalın bir ucuna geçti. Sonra Elsa attı ve onun halkası öbür uca geçti. Kristoff sevinçle güldü ve ellerini çırptı. "Sırayla oynamak çok daha eğlenceli, Elsa!" dedi Kristoff.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kristoff temkinli bir şekilde nişan aldı"
   - Cümle 6: «Kristoff temkinli bir şekilde nişan aldı ve halkayı yavaşça attı.»
   - Açıklama: 'Temkinli' ve 'nişan aldı' 3 yaşındaki çocuğun bilmediği kelimeler.
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bildiği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0090` birebir aynı, ardından `@onarim: 29079a1bd35e9afd461a50f412e6716d05ee43ee`, sonra gövde.

### Hikâye 6: tohum elsa-0091 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: otların arasından çıtır çıtır bir ses geldi | buzdan bir ot yapıp sesi gösterdi
@tohum: elsa-0091
Elsa, Olaf ile deniz kıyısında yürüyordu. Rüzgar esti ve otların arasından çıtır çıtır bir ses geldi. "Bu ses nereden geliyor, Elsa?" diye sordu Olaf. Elsa otlara eğildi ve yakından baktı. Otlar soğuktan sert olmuştu. Ama Olaf sesin nasıl çıktığını anlamadı. Elsa elini salladı ve buzdan ince bir ot yaptı. Sonra bu otu parmağıyla hafifçe eğdi. Ot eğildi ve çıtır diye küçük bir ses çıkardı. Olaf da yerdeki otlara dokundu ve aynı sesi duydu. "Anladım, sert otlar rüzgarda eğilip ses çıkarıyor, teşekkürler, Elsa!" dedi Olaf.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir ot yapıp sesi gösterdi"
   - Cümle 0 (plan satırı): «otların arasından çıtır çıtır bir ses geldi | buzdan bir ot yapıp sesi gösterdi»
   - Açıklama: Ses gösterilmez; fiil nesnesine uymuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "otların arasından çıtır çıtır bir ses geldi"
   - Cümle 2: «Rüzgar esti ve otların arasından çıtır çıtır bir ses geldi.»
   - Açıklama: Otlardan gelen bir ses gerçek bir sorun değil; çocuğun önemseyeceği bir kayıp ya da engel yok, yalnız bir merak var.
   - Açıklama: Bir ses duymak gerçek bir sorun değil ve deniz kıyısında otların soğuktan sertleşmesi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0091` birebir aynı, ardından `@onarim: 674b0e914ea3fd2f05e244708b563888651f8cf2`, sonra gövde.

### Hikâye 7: tohum elsa-0092 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0092
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'buket', fiil 'uyanmak', sıfat 'gizemli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: iki kardeş de buketi önce saklamak istedi | sırayla saklamayı önerdi
@tohum: elsa-0092
Elsa, Anna ile karlı ormanda saklama oyunu oynuyordu. Elsa bu oyun için buzdan parlak bir buket yapmıştı. Ama ikisi de buketi önce saklamak istedi. "Sırayla saklayalım, önce sen sakla, Anna," dedi Elsa. Elsa gözlerini kapadı ve uyuyor gibi yaptı. Anna buketi karlı bir çalının arkasına sakladı. "Uyan, Elsa, buket gizemli bir yerde!" dedi Anna. Elsa gözlerini açtı ve çalılara baktı. Buket güneşte parladı ve Elsa onu hemen buldu. Sonra sıra Elsa'ya geldi ve Anna gözlerini kapadı. Elsa buketi karlı bir ağacın dibine sakladı. Anna buketi bulunca sevinçle zıpladı. "Şimdi yine sıra bende, Elsa!" dedi Anna.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buket gizemli bir yerde"
   - Cümle 7: «"Uyan, Elsa, buket gizemli bir yerde!" dedi Anna.»
   - Açıklama: 'Gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'gizemli' soyut kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0092` birebir aynı, ardından `@onarim: 2d14a0604b4de95fb2cee79cc7ccdecafc157561`, sonra gövde.

### Hikâye 8: tohum elsa-0093 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0093
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yama', fiil 'üzülmek', sıfat 'rüzgarlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: uçurtma sivri bir kayaya çarpıp delindi | kuyruğundan bir parça koparıp deliğe yama yaptı
@tohum: elsa-0093
Bir sabah Elsa ile Sven rüzgarlı dağda uçurtma uçuruyordu. Elsa ipi tutuyordu ve Sven de yanında koşuyordu. Ama uçurtma sivri bir kayaya çarptı ve kağıdında bir delik açıldı. Uçurtma yere düştü ve Elsa çok üzüldü. Sven de başını önüne eğdi. "Üzülme, Sven, bunu düzeltebiliriz," dedi Elsa. Kraliçe Elsa uçurtmanın uzun kuyruğundan küçük bir parça kopardı. Parçayı deliğin üstüne bağladı ve güzel bir yama yaptı. Rüzgar yine esti ve uçurtma havaya yükseldi. Sven sevinçle zıpladı. Sonra Elsa ile Sven uçurtmayı mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa uçurtmanın uzun"
   - Cümle 7: «Kraliçe Elsa uçurtmanın uzun kuyruğundan küçük bir parça kopardı.»
   - Açıklama: Elsa zaten tanıtılmışken unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa uçurtmanın uzun kuyruğundan"
   - Cümle 7: «Kraliçe Elsa uçurtmanın uzun kuyruğundan küçük bir parça kopardı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa uçurtmanın uzun"
   - Cümle 7: «Kraliçe Elsa uçurtmanın uzun kuyruğundan küçük bir parça kopardı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0093` birebir aynı, ardından `@onarim: 50d9c423b3a715e1900b63820840984960822697`, sonra gövde.
