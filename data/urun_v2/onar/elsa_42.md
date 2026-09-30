# Editör görevi (onarım): Elsa, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0134 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Anna
@tohum: elsa-0134
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çubuk', fiil 'parlatmak', sıfat 'akıllı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | Anna
@plan: tozlu camın üst tarafına eli yetişmedi | kardeşinden uzun bir çubuk istedi ve camı parlattı
@tohum: elsa-0134
Elsa sarayın büyük salonunda Anna ile karı izlemek istiyordu. Ama salonun penceresi çok tozluydu ve dışarısı iyi görünmüyordu. Elsa bir bezle camı silmeye başladı ama camın üst tarafına eli yetişmedi. Anna hemen bir sandalyeye çıkmak istedi. Elsa kardeşini koruyan bir kraliçeydi ve buna izin vermedi. Sonra Anna'dan köşedeki uzun çubuğu getirmesini istedi. Anna çubuğu getirdi. Elsa akıllı davrandı ve bezi çubuğun ucuna bağladı. Çubuğu iki eliyle tuttu ve camın üst tarafını yavaş yavaş parlattı. Cam pırıl pırıl oldu. Dışarıdaki beyaz kar artık çok iyi görünüyordu. Elsa çok sevindi, çünkü kardeşiyle birlikte karı izleyebiliyordu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa akıllı davrandı"
   - Cümle 8: «Elsa akıllı davrandı ve bezi çubuğun ucuna bağladı.»
   - Açıklama: Tohumdaki özellik kraliçe; akıllılık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0134` birebir aynı, ardından `@onarim: 7959f3f094854f067e2a147efdbd77400d2c72ef`, sonra gövde.

### Hikâye 2: tohum elsa-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0137
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çadır', fiil 'beklemek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: kızağın içi karışıktı ve kurabiye kutusu bulunamadı | eşyaları dışarı çıkarıp sıraya dizdi ve kutuyu buldu
@tohum: elsa-0137
@degisim: çadır -> kızak
Ormanda karlı ağaçların arasında Kristoff'un yeni kızağı duruyordu. Elsa ile Kristoff kızağın yanında küçük bir kutlama yapacaktı. Ama kızağın içi çok karışıktı ve Kristoff kurabiye kutusunu bulamadı. Kristoff kutuyu aramak için eşyaların üstüne basmak istedi. Elsa bir kraliçeydi ve arkadaşını korumak istedi. Ona eşyaları tek tek dışarı çıkarmasını söyledi. Elsa da eşyaları karın üstüne bir sıraya dizdi. İplerin arasından küçük kurabiye kutusu çıktı. Kristoff eşyaları geri koydu ve Elsa onu bekledi. Sonra ikisi oturdu ve mutlu mutlu kurabiye yedi. Kristoff bundan sonra kızağını hep düzenli tuttu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşını korumak istedi"
   - Cümle 5: «Elsa bir kraliçeydi ve arkadaşını korumak istedi.»
   - Açıklama: Ortada bir tehlike yokken 'korumak' fiili yanlış anlamda kullanılmış.
   - Açıklama: Ortada bir tehlike yokken 'korumak' fiili yerinde kullanılmamış; eşyaların üstüne basmasını engellemek kastediliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve arkadaşını korumak istedi"
   - Cümle 5: «Elsa bir kraliçeydi ve arkadaşını korumak istedi.»
   - Açıklama: Koruma gerekçesi olaydan çıkmıyor; eşyaların üstüne basmak bir tehlike olarak kurulmuyor.
   - Açıklama: Eşyaların üstüne basmakta bir tehlike kurulmadığı için koruma gerekçesi sebepsiz ve işlevsiz.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Ona eşyaları tek tek dışarı çıkarmasını söyledi"
   - Cümle 6: «Ona eşyaları tek tek dışarı çıkarmasını söyledi.»
   - Açıklama: Eşyaları çıkarma işini yan karakter Kristoff yapıyor; çözümün ana eylemi figürde değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0137` birebir aynı, `@degisim: çadır -> kızak` (tutuyorsan), ardından `@onarim: 592cd5d9f6e4862738b849b9d8b777f9da204027`, sonra gövde.

### Hikâye 3: tohum elsa-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Olaf
@tohum: elsa-0138
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'muz', fiil 'çağırmak', sıfat 'resimli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | Olaf
@plan: kolu çarpınca muz yere düşüp kırıldı | özür diledi ve buzdan yeni bir muz yaptı
@tohum: elsa-0138
Sarayın büyük salonunda Elsa ile Olaf resimli bir kitaba bakıyordu. Olaf'ın elinde Elsa'nın yaptığı küçük bir muz vardı. Bu muz, kitaptaki muz resmine çok benziyordu. Elsa ayağa kalkarken kolu Olaf'ın eline çarptı. Muz yere düştü ve kırıldı. Olaf üzgün üzgün salonun öbür ucuna gitti. Elsa hemen Olaf'ı yanına çağırdı ve ondan özür diledi. Sonra ellerini yavaşça açtı ve buzdan yeni bir muz yaptı. Olaf muzu eline aldı ve güldü. Sonra Elsa'ya sıkıca sarıldı. Elsa ile Olaf yeni muzla salonda mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 5: «Muz yere düştü ve kırıldı.»
   - Açıklama: Muzun düşüp kırılması sorunu ancak 5. cümlede geliyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Muz yere düştü ve kırıldı"
   - Cümle 5: «Muz yere düştü ve kırıldı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak beşinci cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0138` birebir aynı, ardından `@onarim: ffc37994f31b829b20fef2fe1709a52af3d2711f`, sonra gövde.

### Hikâye 4: tohum elsa-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0139
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'etiket', fiil 'düzeltmek', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: yükselen dalgalar kumdaki kabuk resmini bozdu | kabukları kuru kuma taşıyıp yeniden dizdiler
@tohum: elsa-0139
@degisim: etiket -> kova
Rüzgar hafif hafif esiyordu. Elsa ile Olaf renkli kabuklarla kumda bir güneş yaptı. Ama deniz yükseldi ve dalgalar güneşin bir ucunu bozdu. Olaf kabukları hemen aynı yere yeniden dizmek istedi. Kraliçe Elsa ise eliyle limanın yanındaki kuru kumu gösterdi. Olaf bütün kabukları kovasına koydu. Sonra dolu kovayı oraya taşıdı. Elsa ile Olaf kabukları orada yeniden dizdi. Olaf eğri duran bir kabuğu düzeltti. Dalgalar artık kabuklara ulaşamıyordu. Elsa ile Olaf çok sevindi, çünkü kumdaki güneş artık dalgalardan uzaktaydı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa ise eliyle"
   - Cümle 5: «Kraliçe Elsa ise eliyle limanın yanındaki kuru kumu gösterdi.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
   - Açıklama: Önceden tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa ise eliyle limanın yanındaki kuru kumu gösterdi"
   - Cümle 5: «Kraliçe Elsa ise eliyle limanın yanındaki kuru kumu gösterdi.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi kız kardeşi korumak için değil, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumak olarak tanımlı, burada yalnız unvan olarak geçiyor ve işe yaramıyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Olaf bütün kabukları kovasına koydu"
   - Cümle 6: «Olaf bütün kabukları kovasına koydu.»
   - Açıklama: Kabukları toplayıp kuru kuma taşıyan Olaf; Elsa yalnız eliyle yeri gösteriyor, çözümün işini yan karakter yapıyor.
   - Açıklama: Elsa yalnız yeri gösteriyor; kabukları toplayıp taşıyan, yani çözümü uygulayan yan karakter Olaf.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0139` birebir aynı, `@degisim: etiket -> kova` (tutuyorsan), ardından `@onarim: 75476a65cb7d4c5736ed549162da80e620ad5c92`, sonra gövde.

### Hikâye 5: tohum elsa-0140 (deneme 2 -> 3)

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
Meraklı martılar limanın üstünde ötüyordu. Elsa deniz kıyısında kağıttan uzun bir zincir yapıyordu. Ama birden rüzgar esti ve kağıt zincir ortadan koptu. Hafif halkalar taşların arasına uçuştu. Elsa çok üzüldü, çünkü zinciri bitirmek istiyordu. Bu kez daha sağlam bir zincir yapmak istedi. Ellerinden kalın buz halkaları çıkardı. Halkaları bir, iki, üç diye saydı ve birbirine taktı. On halka olunca zinciri yavaşça havaya kaldırdı. Rüzgar yine esti ama kalın zincir yerinde kaldı. Zincir güneşte pırıl pırıl parladı. Elsa kağıt halkaları da topladı ve zincirin ucuna ekledi. Elsa uzun zincirle kıyıda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa kağıt halkaları da topladı"
   - Cümle 12: «Elsa kağıt halkaları da topladı ve zincirin ucuna ekledi.»
   - Açıklama: Sorun buz zincirle çözüldükten sonra kopan kağıt halkaları eklemek çözüme gereksiz bir adım katıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0140` birebir aynı, `@degisim: koklamak -> saymak` (tutuyorsan), ardından `@onarim: 261320578019ee21938fe0c09b72c9900afbb2a1`, sonra gövde.

### Hikâye 6: tohum elsa-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Bir sabah Elsa deniz kıyısında heyecanlı bir oyun oynuyordu. Buzdan kocaman bir brokoli yapıyordu. Ama brokolinin sapı çok inceydi ve brokoli devrildi. Brokoli taşların üstünde küçük bir ağaç gibi yatıyordu. Elsa buna baktı ve güldü. Sonra elini yavaşça oynattı. Bu kez kalın ve kısa bir sap yaptı. Sonra brokolinin başını dikkatle üstüne koydu. Elsa elini çekti ve bekledi. Brokoli hiç sallanmadı. Güneşte pırıl pırıl parladı. Elsa çok sevindi, çünkü buzdan brokoli artık dimdik duruyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir ağaç gibi yatıyordu"
   - Cümle 4: «Brokoli taşların üstünde küçük bir ağaç gibi yatıyordu.»
   - Açıklama: Benzetme küçük çocuk için mecazlı bir anlatım.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "brokolinin başını dikkatle üstüne koydu"
   - Cümle 8: «Sonra brokolinin başını dikkatle üstüne koydu.»
   - Açıklama: 'Üstüne' kelimesinin neyin üstü olduğunu gösterdiği belli değil; yeni sap anılmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0141` birebir aynı, `@degisim: sokulmak -> gülmek` (tutuyorsan), ardından `@onarim: 83cba9a672d947222caf376f16f624665bc72fa4`, sonra gövde.

### Hikâye 7: tohum elsa-0142 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0142
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kıyafet', fiil 'kıpırdamak', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: sert rüzgar küçük çiçeğin ince sapını sallıyordu | uzun eteğini açıp çiçeği rüzgardan korudu
@tohum: elsa-0142
Rüzgar limanda hızlı hızlı esiyordu. Elsa limanda taşların arasında ortası simsiyah, kırmızı bir çiçek fark etti. Rüzgar çiçeğin ince sapını çok sallıyordu ve çiçek yere eğildi. Elsa çiçeğin yanına eğildi. Sonra uzun kraliçe kıyafetinin eteğini çiçeğin önüne bir duvar gibi açtı. Rüzgar artık çiçeğe gelmiyordu. Çiçeğin sapı yavaş yavaş doğruldu ve çiçek hiç kıpırdamadı. Elsa orada sessizce bekledi. Biraz sonra rüzgar dindi. Elsa eteğini topladı ve çiçeğe gülümsedi. Elsa bundan sonra kıyıda yürürken taşların arasındaki çiçeklere dikkatle baktı.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa limanda taşların"
   - Cümle 2: «Elsa limanda taşların arasında ortası simsiyah, kırmızı bir çiçek fark etti.»
   - Açıklama: 'Limanda' art arda iki cümlede gereksiz yere tekrarlanıyor.
   - Açıklama: 'Limanda' bir önceki cümlede geçtiği halde gereksiz tekrar ediliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "önüne bir duvar gibi açtı"
   - Cümle 5: «Sonra uzun kraliçe kıyafetinin eteğini çiçeğin önüne bir duvar gibi açtı.»
   - Açıklama: 'Bir duvar gibi' benzetmesi mecaz sayılır.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra uzun kraliçe kıyafetinin eteğini"
   - Cümle 5: «Sonra uzun kraliçe kıyafetinin eteğini çiçeğin önüne bir duvar gibi açtı.»
   - Açıklama: Kraliçe özelliği karttaki 'kız kardeşini korur' biçiminde değil, kıyafet eteği olarak kullanılıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çiçeğin sapı yavaş yavaş doğruldu ve çiçek hiç kıpırdamadı"
   - Cümle 7: «Çiçeğin sapı yavaş yavaş doğruldu ve çiçek hiç kıpırdamadı.»
   - Açıklama: Sap doğrulurken çiçeğin hiç kıpırdamadığı söyleniyor; iki ifade çelişiyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra kıyıda yürürken taşların arasındaki çiçeklere dikkatle baktı"
   - Cümle 11: «Elsa bundan sonra kıyıda yürürken taşların arasındaki çiçeklere dikkatle baktı.»
   - Açıklama: Son cümledeki ders çiçeği rüzgardan koruma olayından çıkmıyor ve sıcak bir kapanış vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0142` birebir aynı, ardından `@onarim: 64edd34927b8f1877dfe71d2f5f57a3105082e5e`, sonra gövde.

### Hikâye 8: tohum elsa-0143 (deneme 2 -> 3)

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
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa karı elleriyle düzeltip tepede şirin bir kaydırak yapmıştı. Sven de kaymak istedi, ama kaydırak ona çok dardı. Sven kaydırağın başında üzgün üzgün bekledi. "Gel, Sven, bu kaydırağı paylaşalım," dedi Elsa. Elsa ellerini kaydırağın iki yanına uzattı. Elinden buz çıktı ve kaydırak genişledi. Kaydırak tamamlanınca Sven sevinçle ayağını yere vurdu. Önce Elsa kaydı, sonra Sven dört ayağını açıp aşağı kaydı. Sven karın içine yuvarlandı ve burnundan neşeyle ses çıkardı. "Sıra yine sende, Sven!" dedi Elsa gülerek. Elsa çok mutluydu, çünkü kaydırağını Sven'le paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kaydırak tamamlanınca Sven sevinçle"
   - Cümle 8: «Kaydırak tamamlanınca Sven sevinçle ayağını yere vurdu.»
   - Açıklama: Kaydırak zaten yapılmıştı; 'tamamlanınca' yerine 'genişleyince' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0143` birebir aynı, `@degisim: örgü -> kaydırak` (tutuyorsan), ardından `@onarim: e434ba1d50f5668f15f9fe0409cfc9a263d6d58b`, sonra gövde.

### Hikâye 9: tohum elsa-0144 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: yola küçük taşlar yuvarlandı ve yürümek zorlaştı | taşları iten suyu buldu ve taşları suyun yanına sıraladı
@tohum: elsa-0144
Elsa karlı ormanda saraya giden yolda yürüyordu. Birden yolun ortasına küçük taşlar yuvarlandı. Taşlar yüzünden yolda yürümek zorlaştı. Elsa bu hareketli taşları çok merak etti. Yolun kenarına yavaşça yaklaştı ve baktı. Karın altından ince bir su akıyordu ve taşları yola itiyordu. Elsa bu krallığın kraliçesiydi ve yoldan geçen herkesi korumak istedi. Taşları tek tek topladı ve suyun iki yanına sıraladı. Artık yola hiç taş gelmedi ve yol yine temiz oldu. Elsa bundan sonra yolda taş görünce onu kenara koydu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Taşlar yüzünden yolda yürümek zorlaştı"
   - Cümle 3: «Taşlar yüzünden yolda yürümek zorlaştı.»
   - Açıklama: Yola yuvarlanan küçük taşlar çocuğun önemseyeceği bir sorun değil ve karın altındaki ince suyun taşları yola itmesi zayıf bir sebep.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "suyun iki yanına sıraladı"
   - Cümle 8: «Taşları tek tek topladı ve suyun iki yanına sıraladı.»
   - Açıklama: Taşları suyun yanına sıralamak suyun taşları yola itmesini nasıl durdurduğu belirsiz; çözüm sebebe açıkça yönelmiyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra yolda taş görünce onu kenara koydu"
   - Cümle 10: «Elsa bundan sonra yolda taş görünce onu kenara koydu.»
   - Açıklama: Son cümle sorunun çözüldüğü ve yola artık taş gelmediği bilgisiyle çelişen, sıcaklığı olmayan bir eylemle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0144` birebir aynı, ardından `@onarim: 38882831e8b4fa2180891694c5a922d4bbe48b7b`, sonra gövde.

### Hikâye 10: tohum elsa-0146 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0146
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yeni bir şeyi denemek
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'balkabağı', fiil 'satmak', sıfat 'koyu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: yeni tatlı yemek için çok sıcaktı | kabın etrafına ince bir buz yaptı
@tohum: elsa-0146
@degisim: balkabağı -> elma
Elsa ile Anna fiyort kıyısında yan yana oturuyordu. Önlerinde koyu kırmızı bir elma tatlısı vardı. İkisi bu tatlıyı ilk kez deneyecekti ama tatlı çok sıcaktı. "Elsa, bu tatlı çok sıcak!" dedi Anna. Elsa gülümsedi ve elini kabın yanına koydu. Elinden ince bir buz çıktı ve kabın etrafını sardı. Tatlı yavaş yavaş soğudu. Anna ilk kaşığı ağzına koydu ve gözlerini kocaman açtı. "Çok güzel! Bu tatlıyı kimseye satmayalım," dedi Anna. Elsa da bir kaşık tattı ve güldü. Elsa ile Anna çok sevindi, çünkü yeni tatlı çok güzeldi.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa ile Anna fiyort kıyısında"
   - Cümle 1: «Elsa ile Anna fiyort kıyısında yan yana oturuyordu.»
   - Açıklama: 'Fiyort' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anna fiyort kıyısında"
   - Cümle 1: «Elsa ile Anna fiyort kıyısında yan yana oturuyordu.»
   - Açıklama: 'Fiyort' 3 yaşındaki bir çocuğun bilmediği bir kelime.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu tatlıyı kimseye satmayalım"
   - Cümle 10: «Bu tatlıyı kimseye satmayalım," dedi Anna.»
   - Açıklama: Satış bağlamı olmadığından 'satmayalım' fiili yerinde ve anlamlı kullanılmamış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu tatlıyı kimseye satmayalım"
   - Cümle 10: «Bu tatlıyı kimseye satmayalım," dedi Anna.»
   - Açıklama: 'Kimseye satmayalım' olaya bağlanmayan, beğeniyi dolaylı anlatan bir söz; çocuk için anlaşılır değil.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Bu tatlıyı kimseye satmayalım"
   - Cümle 10: «Bu tatlıyı kimseye satmayalım," dedi Anna.»
   - Açıklama: Kartın tür alanında prenses ve kraliçe olan kardeşler tatlı satan biri gibi gösteriliyor; dizide böyle bir bilgi yok.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu tatlıyı kimseye satmayalım"
   - Cümle 10: «Bu tatlıyı kimseye satmayalım," dedi Anna.»
   - Açıklama: Tatlı satma fikri hiçbir yerden çıkmıyor ve olayla ilgisiz.
   - Açıklama: Tatlıyı satma fikri hiçbir yerden çıkmıyor ve olayda işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0146` birebir aynı, `@degisim: balkabağı -> elma` (tutuyorsan), ardından `@onarim: f75b300c76fd8234b5109af65e27e78f9c2e22e2`, sonra gövde.

### Hikâye 11: tohum elsa-0147 (deneme 2 -> 3)

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
Elsa ile Olaf dağda, buz sarayının önünde oynuyordu. Giyinme oyunu için eskimiş kırmızı bir palto getirmişlerdi. Ama ikisi de paltoyu aynı anda giymek istedi. Olaf paltonun bir kolunu çekti, Elsa öbür kolunu tuttu. Elsa biraz düşündü. Sonra elinden buz çıktı ve küçük bir buz yıldızı oldu. Yıldızı tutan paltoyu giyecekti. Elsa yıldızı önce Olaf'a verdi. Olaf paltoyu giydi ve büyük düğmeleri tek tek kapattı. Palto ona çok büyük geldi ve Olaf karda komik adımlarla yürüdü. Sonra Olaf yıldızı Elsa'ya uzattı. Elsa da paltoyu giydi ve iki kez döndü. Elsa çok mutlu oldu, çünkü ikisi de paltoyu sırayla giymişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "büyük düğmeleri tek tek kapattı"
   - Cümle 9: «Olaf paltoyu giydi ve büyük düğmeleri tek tek kapattı.»
   - Açıklama: Düğmeler kapatılmaz, iliklenir; fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0147` birebir aynı, ardından `@onarim: 8b7f99b9540c8b8c48eeb9663848a87323098312`, sonra gövde.

### Hikâye 12: tohum elsa-0148 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0148
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'zambak', fiil 'uçuşmak', sıfat 'şaşkın'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: ağır buzlar küçük bir fidanın üstüne konacaktı | buzları taşın yanına koymasını söyledi
@tohum: elsa-0148
@degisim: zambak -> fidan
Elsa dağda, havada uçuşan kar tanelerini izliyordu. Birden karın arasında küçük yeşil bir fidan fark etti. Ama Kristoff ağır buz parçalarını tam fidanın üstüne koymak üzereydi. Elsa bir kraliçeydi ve fidanı korumak istedi. "Dur, Kristoff!" dedi Elsa. Kristoff şaşkın bir yüzle durdu. "Kristoff, buzları şu büyük taşın yanına koy," dedi Elsa. Kristoff buzları taşın yanına taşıdı. Sonra eğildi ve fidana dikkatle baktı. "Karın içinde fidan mı büyüyor?" diye sordu Kristoff. Elsa gülümsedi ve fidanın üstündeki karı eliyle yavaşça açtı. Fidanın yaprakları yeniden göründü. "Teşekkürler, Kristoff, fidan artık güvende!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kristoff ağır buz parçalarını tam fidanın üstüne koymak üzereydi"
   - Cümle 3: «Ama Kristoff ağır buz parçalarını tam fidanın üstüne koymak üzereydi.»
   - Açıklama: Kristoff'un buzları neden fidanın üstüne koymak istediği söylenmiyor, sorunun sebebi eksik.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karı eliyle yavaşça açtı"
   - Cümle 11: «Elsa gülümsedi ve fidanın üstündeki karı eliyle yavaşça açtı.»
   - Açıklama: Kar açılmaz; 'karı eliyle temizledi' olmalı.
   - Açıklama: Kar açılmaz; 'karı temizledi' ya da 'süpürdü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0148` birebir aynı, `@degisim: zambak -> fidan` (tutuyorsan), ardından `@onarim: 7fd7f90cb4f24445dbc57800fbe07bf0cabbcc15`, sonra gövde.
