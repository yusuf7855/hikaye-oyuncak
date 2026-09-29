# Editör görevi (onarım): Elsa, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0099 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Sven
@tohum: elsa-0099
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'menekşe', fiil 'soğumak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | Sven
@plan: ren geyiğinin sırtı sıcak güneşte çok ısındı | kraliçe geyiği serin salona çağırdı
@tohum: elsa-0099
@degisim: sabırlı -> serin
Sarayın önünde menekşeler açmıştı ve güneş çok sıcaktı. Elsa dışarı çıktı ve Sven'i gördü. Sven'in sırtı güneşte çok ısınmıştı. Dışarıda hiç gölge yoktu. Elsa bu sarayın kraliçesiydi. Büyük salonun kapısını açtı ve Sven'e içeri girmesini söyledi. Sven kraliçenin sözünü dinledi ve salona girdi. Salonun taşları serindi. Sven taşların üstüne yattı ve sessizce bekledi. Sıcak sırtı yavaş yavaş soğudu. Sonra Sven kalktı ve başını Elsa'nın eline sürttü. Elsa ile Sven menekşelerin yanına mutlu mutlu geri döndüler.
```

**Hakem bulguları (3):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Sven'in sırtı güneşte çok ısınmıştı"
   - Cümle 3: «Sven'in sırtı güneşte çok ısınmıştı.»
   - Açıklama: Güneşte aşırı ısınan hayvan rahatsızlık ve sıcak çarpması çağrışımı taşıyor.
   - Açıklama: Ren geyiğinin güneşte aşırı ısınması bir canlının sıkıntı çektiği bir durum olarak veriliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 5: «Elsa bu sarayın kraliçesiydi.»
   - Açıklama: Kraliçelik bilgisi olaydan çıkmıyor ve çözüme bir şey katmayan zorlama bir ayrıntı olarak araya giriyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa ile Sven menekşelerin yanına mutlu mutlu geri döndüler"
   - Cümle 12: «Elsa ile Sven menekşelerin yanına mutlu mutlu geri döndüler.»
   - Açıklama: Sven gölgesiz ve çok sıcak dışarıdan kaçıp serinledikten hemen sonra aynı sıcağa geri dönüyor, çözüm boşa çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0099` birebir aynı, `@degisim: sabırlı -> serin` (tutuyorsan), ardından `@onarim: e4afd58422dfba142764bf8f5a526f8b5f675051`, sonra gövde.

### Hikâye 2: tohum elsa-0101 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0101
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'dolma', fiil 'yayılmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: rüzgarda kalenin ön duvarı sallandı | kardan adamdan yardım istedi ve duvara buz yaydı
@tohum: elsa-0101
@degisim: dolma -> duvar
Rüzgar karlı ağaçların arasında esiyordu. Elsa ormanda Olaf ile kardan büyük bir kale yapıyordu. Ama rüzgar her estiğinde kalenin ön duvarı sallanıyordu. Elsa duvarı elleriyle tutunca buz yapamıyordu. Bu yüzden Elsa, Olaf'tan yardım istedi. Olaf hemen duvarın yanına geldi ve onu sıkıca tuttu. Elsa ellerini açtı ve duvara ince bir buz gönderdi. Buz duvarın her yerine yavaşça yayıldı. Duvar sağlam oldu ve rüzgarda artık sallanmadı. Olaf kaleyi çok sevdi. Cömert Olaf ilk olarak Elsa'yı kalenin içine aldı. İkisi kalenin içinde mutlu mutlu oyun oynadı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Cömert Olaf ilk olarak Elsa'yı kalenin içine aldı"
   - Cümle 11: «Cömert Olaf ilk olarak Elsa'yı kalenin içine aldı.»
   - Açıklama: Birlikte yaptıkları kaleye Olaf'ın Elsa'yı 'alması' olaydan çıkmayan, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0101` birebir aynı, `@degisim: dolma -> duvar` (tutuyorsan), ardından `@onarim: 974666fedc5455439363605c611363362cefd2b4`, sonra gövde.

### Hikâye 3: tohum elsa-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0104
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gözlük', fiil 'başlamak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: sert rüzgar narin çiçeği çok sallıyordu | çiçeğin önüne eğilip onu elleriyle korudu
@tohum: elsa-0104
@degisim: gözlük -> yaprak
Rüzgar esmeye başladı. Elsa dağın tepesinde, buzdan sarayının önünde küçük, mavi bir çiçek gördü. Rüzgar çiçeği çok sallıyordu ve narin yaprakları düşebilirdi. Elsa çiçeği korumak istedi. Kraliçe Elsa hemen çiçeğin önüne eğildi. Sırtını rüzgara döndü ve iki elini çiçeğin çevresine koydu. Soğuk hava Elsa'ya çarptı ama çiçeğe gelmedi. Elsa orada durdu ve bir süre bekledi. Sonra rüzgar yavaşladı ve durdu. Elsa ellerini yavaşça çekti ve çiçeğe baktı. Mavi çiçek yine dik duruyordu ve yapraklarının hepsi yerindeydi. Elsa çok sevindi, çünkü küçük çiçeği rüzgardan korumuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve narin yaprakları düşebilirdi"
   - Cümle 3: «Rüzgar çiçeği çok sallıyordu ve narin yaprakları düşebilirdi.»
   - Açıklama: 'Narin' 3 yaşındaki bir çocuğun bildiği bir kelime değil.
   - Açıklama: 'Narin' 3 yaşındaki bir çocuğun bilmediği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen çiçeğin önüne"
   - Cümle 5: «Kraliçe Elsa hemen çiçeğin önüne eğildi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen çiçeğin"
   - Cümle 5: «Kraliçe Elsa hemen çiçeğin önüne eğildi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor ve kız kardeşi koruma biçiminde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0104` birebir aynı, `@degisim: gözlük -> yaprak` (tutuyorsan), ardından `@onarim: c30dcf338d8299b0e2df60dc9b881a61333630db`, sonra gövde.

### Hikâye 4: tohum elsa-0106 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0106
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'baston', fiil 'ayrılmak', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: karda bastonu olmayan arkadaş geride kaldı | bastonu sırayla kullanmak için kural koydu
@tohum: elsa-0106
Bir sabah Elsa ile Kristoff karlı ormanda yürüyordu. Kar çok derindi ve Kristoff'un bastonu yoktu. Bu yüzden Kristoff yavaş ilerliyor ve geride kalıyordu. Elsa'nın elinde ise uzun bir baston vardı. Kristoff dürüst bir adamdı ve çok yorulduğunu söyledi. Elsa bastonunu onunla paylaşmak istedi. Elsa kraliçeydi ve kısa bir kural koydu. Her büyük ağaçta bastonu birbirlerine vereceklerdi. Kristoff kurala uydu ve bastonu sırayla kullandılar. Artık ikisi de kolayca yürüdü. Hiç ayrılmadan yan yana ormanın içinden geçtiler. Kristoff gülümsedi ve Elsa'ya teşekkür etti. Elsa bundan sonra bastonunu yorulan arkadaşlarıyla paylaştı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kristoff dürüst bir adamdı"
   - Cümle 5: «Kristoff dürüst bir adamdı ve çok yorulduğunu söyledi.»
   - Açıklama: Kristoff'un dürüst olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kristoff kurala uydu ve bastonu sırayla kullandılar"
   - Cümle 9: «Kristoff kurala uydu ve bastonu sırayla kullandılar.»
   - Açıklama: Tekil özne 'Kristoff' ile çoğul yüklem 'kullandılar' aynı cümlede uyuşmuyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Artık ikisi de kolayca yürüdü"
   - Cümle 10: «Artık ikisi de kolayca yürüdü.»
   - Açıklama: Tek baston sırayla kullanılırken ikisinin de her an kolayca yürümesi çelişkili.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "bastonunu yorulan arkadaşlarıyla paylaştı"
   - Cümle 13: «Elsa bundan sonra bastonunu yorulan arkadaşlarıyla paylaştı.»
   - Açıklama: Çoğul arkadaşlar arka planda kalmıyor, bastonu alarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0106` birebir aynı, ardından `@onarim: b89a98de940a7e36d7215f975c7b962ba6ed6358`, sonra gövde.

### Hikâye 5: tohum elsa-0107 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0107
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'paket', fiil 'uzaklaştırmak', sıfat 'kahverengi'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: küçük bir çiçek sarayın yolunun ortasındaydı | çiçeği kurdeleyle çevirip yolu ondan uzaklaştırdı
@tohum: elsa-0107
Dağda, sarayın önünde sabah güneşi parlıyordu. Elsa elinde kahverengi bir paketle saraya yürüyordu. Birden yolun ortasında karın içinden çıkan küçük bir çiçek gördü. Çiçek tam yolun üstündeydi ve kolayca basılabilirdi. Elsa bu minik çiçeği korumak istedi. Paketin içinde sarayı süslemek için kırmızı kurdeleler vardı. Elsa kurdeleleri çıkardı ve çiçeğin etrafına bir çember yaptı. Elsa kraliçeydi ve sarayın yolunu o seçerdi. Eski yolu çiçekten uzaklaştırdı ve karda yeni bir yol açtı. Sonra yeni yoldan sarayın kapısına yürüdü. Çiçek kırmızı çemberin ortasında güneşte duruyordu. Elsa çok sevindi, çünkü çiçek artık güvendeydi.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve kolayca basılabilirdi"
   - Cümle 4: «Çiçek tam yolun üstündeydi ve kolayca basılabilirdi.»
   - Açıklama: 'Basmak' yönelme eki ister; özne 'çiçek' ile edilgen çatı kurulamaz, 'çiçeğe kolayca basılabilirdi' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çiçek tam yolun üstündeydi ve kolayca basılabilirdi"
   - Cümle 4: «Çiçek tam yolun üstündeydi ve kolayca basılabilirdi.»
   - Açıklama: 'Basmak' yönelme ister; 'çiçek basılabilirdi' dilbilgisel değil, 'çiçeğe basılabilirdi' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve sarayın yolunu o seçerdi"
   - Cümle 8: «Elsa kraliçeydi ve sarayın yolunu o seçerdi.»
   - Açıklama: Yolu taşıma çözümü olaydan çıkmayan zorlama bir kraliçelik bilgisiyle sebepsizce getiriliyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Eski yolu çiçekten uzaklaştırdı"
   - Cümle 9: «Eski yolu çiçekten uzaklaştırdı ve karda yeni bir yol açtı.»
   - Açıklama: Yol uzaklaştırılmaz; fiil nesnesine uymuyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Eski yolu çiçekten uzaklaştırdı"
   - Cümle 9: «Eski yolu çiçekten uzaklaştırdı ve karda yeni bir yol açtı.»
   - Açıklama: Kurdele çemberi çiçeği zaten korurken var olan yolu yerinden oynatmak mantıksız ve kraliçelik bilgisi yalnız bu çözümü sebepsizce getirmek için ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0107` birebir aynı, ardından `@onarim: 510578920ef548e84b72a1f469fba6504cbf07db`, sonra gövde.

### Hikâye 6: tohum elsa-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0108
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ayakkabı', fiil 'katlamak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: battaniye çok büyüktü ve sandalyelerden kayıyordu | kardan adamdan köşeleri tutmasını istedi
@tohum: elsa-0108
@degisim: ayakkabı -> battaniye
Elsa dağda, sarayında Olaf ile oynuyordu. Elsa yumuşacık bir battaniyeden küçük bir çadır kurmak istedi. Ama battaniye çok büyüktü ve iki sandalyeden yere kayıyordu. Elsa battaniyeyi ikiye katladı ama yine tek başına tutamadı. Bunun üzerine Olaf'tan yardım istedi. Elsa kraliçeydi ve Olaf'a açık bir iş verdi. Olaf iki köşeyi tutacak, Elsa öbür köşeleri yerleştirecekti. Olaf köşeleri sıkıca tuttu ve battaniye kaymadı. Elsa öbür köşeleri sandalyelerin arkasına geçirdi. Sonunda küçük çadır kuruldu. Olaf ile Elsa çadırın içine girip oturdu. Elsa çok sevindi, çünkü Olaf'ın yardımıyla çadırı bitirmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf'a açık bir iş verdi"
   - Cümle 6: «Elsa kraliçeydi ve Olaf'a açık bir iş verdi.»
   - Açıklama: 'Açık bir iş' mecazlı ve soyut bir anlatım.
   - Açıklama: 'Açık bir iş' soyut bir anlatım ve küçük çocuk 'açık' kelimesini bu anlamda bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve Olaf'a açık bir iş verdi"
   - Cümle 6: «Elsa kraliçeydi ve Olaf'a açık bir iş verdi.»
   - Açıklama: Kraliçelik bilgisi olayda işlevsiz, zorlama bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0108` birebir aynı, `@degisim: ayakkabı -> battaniye` (tutuyorsan), ardından `@onarim: f6a4c92812ea17c2b49f1fe3ca2ccee4bf35789d`, sonra gövde.

### Hikâye 7: tohum elsa-0109 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0109
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'mısır', fiil 'yetişmek', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: kızak için sarayın önündeki yokuş çok yüksekti | kısa ve güvenli bir tepede kaydı
@tohum: elsa-0109
@degisim: mısır -> kızak
Elsa dağda ilk kez kızakla kaymayı denemek istedi. Ama sarayın önündeki yokuş çok yüksek ve uzundu. Kızak burada çok hızlı kayabilirdi. Elsa kızağı yokuşun başına koydu ve biraz bekledi. Kızak kendi kendine kaymaya başladı. Elsa iki adımda kızağa yetişti ve onu tuttu. Elsa kraliçeydi ve dağda kızak yerini o seçerdi. Sarayın yanındaki kısa ve düz bir tepeyi seçti. Burası kızak için daha güvenliydi. Elsa kızağa oturdu ve yavaşça aşağı kaydı. Kar yüzüne değdi ve Elsa neşeyle güldü. Elsa bundan sonra yeni bir şeyi önce güvenli bir yerde denedi.
```

**Hakem bulguları (6):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kızak kendi kendine kaymaya başladı"
   - Cümle 5: «Kızak kendi kendine kaymaya başladı.»
   - Açıklama: Yüksek yokuş sorununun yanında kızağın kendi kendine kayması ikinci bir sorun olarak açılıp kapanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kızak kendi kendine kaymaya başladı"
   - Cümle 5: «Kızak kendi kendine kaymaya başladı.»
   - Açıklama: Kızağın kendi kendine kayıp yakalanması sorunla ya da çözümle bağlantısız, işlevsiz bir ara olay.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elsa iki adımda kızağa yetişti"
   - Cümle 6: «Elsa iki adımda kızağa yetişti ve onu tuttu.»
   - Açıklama: Dik ve uzun yokuşta kendi kendine kayan kızağın peşinden koşmak taklit edilince tehlikeli olabilir.
   - Açıklama: Yüksek ve uzun yokuşta kendi kendine kayan kızağın peşinden koşup tutmak çocuğun taklit edebileceği tehlikeli bir davranış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve dağda kızak yerini o seçerdi"
   - Cümle 7: «Elsa kraliçeydi ve dağda kızak yerini o seçerdi.»
   - Açıklama: Kraliçelik bilgisi çözüme bir şey katmıyor, işlevsiz ayrıntı.
   - Açıklama: Kraliçelik bilgisi olaydan çıkmıyor ve çözüme hiçbir şey katmıyor; kaçan kızak bölümü de sonra işe yaramıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kısa ve düz bir tepeyi"
   - Cümle 8: «Sarayın yanındaki kısa ve düz bir tepeyi seçti.»
   - Açıklama: Tepe düz olmaz ve düz yerde kızakla kayılmaz; kelime yanlış anlamda.
   - Açıklama: Tepe düz olmaz ve 'kısa' tepeye uymuyor; 'alçak ve eğimi az bir tepe' gibi olmalı.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kısa ve düz bir tepeyi seçti"
   - Cümle 8: «Sarayın yanındaki kısa ve düz bir tepeyi seçti.»
   - Açıklama: Düz diye anlatılan yerde Elsa sonra aşağı kayıyor; düz ile aşağı kaymak çelişiyor.
   - Açıklama: Düz bir yerden kızakla aşağı kayılamaz; tepe hem düz hem kayılacak yer olarak çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0109` birebir aynı, `@degisim: mısır -> kızak` (tutuyorsan), ardından `@onarim: ae955e66bb72d2030d065e7f824384d9ede5d0d6`, sonra gövde.

### Hikâye 8: tohum elsa-0110 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0110
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'toz', fiil 'gizlenmek', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: karın altından ince bir ses geliyordu | kardaki zili bulup dala geri astı
@tohum: elsa-0110
Ormanda ağaçların üstünde kar tozu parlıyordu. Elsa biraz uykuluydu ama birden gözleri açıldı. Yerden ince bir ses geliyordu. Elsa etrafına baktı ama hiçbir şey göremedi. Ses karın altından geliyordu. Elsa durdu ve düşündü. Kraliçe olarak bu yolun dallarına küçük ziller asmıştı. Ziller kızakların yolunu gösteriyordu. Elsa en yakın dala baktı ve bir zilin eksik olduğunu gördü. Karı elleriyle eşeledi. Küçük zil karın altına gizlenmişti. Rüzgar esince zil karın altında sallanıyordu. Elsa zili bulup dala geri astı. Elsa çok sevindi, çünkü sesi yapan zili bulmuştu.
```

**Hakem bulguları (9):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa biraz uykuluydu ama birden gözleri açıldı"
   - Cümle 2: «Elsa biraz uykuluydu ama birden gözleri açıldı.»
   - Açıklama: Elsa'nın uykulu olması hiçbir işe yaramayan, sebepsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa biraz uykuluydu"
   - Cümle 2: «Elsa biraz uykuluydu ama birden gözleri açıldı.»
   - Açıklama: Elsa'nın uykulu olması olayda hiçbir işe yaramıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu yolun dallarına küçük"
   - Cümle 7: «Kraliçe olarak bu yolun dallarına küçük ziller asmıştı.»
   - Açıklama: Yolun dalı olmaz; ziller ağaçların dallarına asılır.
   - Açıklama: Yolun dalı olmaz; 'yolun kenarındaki dallara' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe olarak bu yolun"
   - Cümle 7: «Kraliçe olarak bu yolun dallarına küçük ziller asmıştı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız arka plan bilgisi olarak geçiyor, sorunun çözümünde işe yaramıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Küçük zil karın altına gizlenmişti"
   - Cümle 11: «Küçük zil karın altına gizlenmişti.»
   - Açıklama: Zil kendi kendine gizlenemez; fiil öznesine uymuyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "zil karın altına gizlenmişti"
   - Cümle 11: «Küçük zil karın altına gizlenmişti.»
   - Açıklama: Zil kendini gizleyemez; 'gizlenmek' fiili cansız özneye uymuyor.
7. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Küçük zil karın altına gizlenmişti"
   - Cümle 11: «Küçük zil karın altına gizlenmişti.»
   - Açıklama: Zilin neden dalından düştüğü söylenmiyor ve karın altından gelen ses çocuğun önemseyeceği açık bir sorun kurmuyor.
8. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar esince zil karın altında sallanıyordu"
   - Cümle 12: «Rüzgar esince zil karın altında sallanıyordu.»
   - Açıklama: Karın altına gömülü zilin rüzgarla sallanıp ses çıkarması akla yatkın değil ve zilin nasıl düştüğü söylenmiyor.
9. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Rüzgar esince zil karın altında sallanıyordu"
   - Cümle 12: «Rüzgar esince zil karın altında sallanıyordu.»
   - Açıklama: Karın altına gömülü bir zilin rüzgarla sallanıp çalması kendi içinde çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0110` birebir aynı, ardından `@onarim: c26766826544c088ff5ec172ce0aad1adb583a14`, sonra gövde.

### Hikâye 9: tohum elsa-0111 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0111
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kadife', fiil 'bulmak', sıfat 'büyük'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: rüzgar hediye kutusunun kurdelesini uçurdu | kardan adama gözlerini kapatmasını söyleyip kurdeleyi buldu
@tohum: elsa-0111
Bir sabah Elsa limanda Olaf için büyük bir hediye kutusu hazırlıyordu. Ama rüzgar esti ve kutunun kadife kurdelesi uçtu. Tam o sırada Olaf geliyordu ve sürprizi görmemeliydi. Elsa kraliçe olarak ona kısa ve açık bir iş verdi. "Olaf, orada dur, gözlerini kapat ve ona kadar say!" dedi Elsa. Olaf gözlerini kapattı ve saymaya başladı. Kurdele limandaki bir direğe takılmıştı. Elsa kurdeleyi buldu ve kutuya bağladı. "Şimdi gözlerini aç, Olaf!" dedi Elsa. Olaf kutuyu açtı ve içinde sarı bir güneş resmi gördü. "Yaz güneşi, en sevdiğim şey!" dedi Olaf. Olaf Elsa'ya sıcacık sarıldı ve ikisi limanda mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Tam o sırada Olaf geliyordu ve sürprizi görmemeliydi"
   - Cümle 3: «Tam o sırada Olaf geliyordu ve sürprizi görmemeliydi.»
   - Açıklama: Kurdelenin uçmasının yanına Olaf'ın sürprizi görmemesi diye ikinci bir sorun ekleniyor.
   - Açıklama: Kaybolan kurdelenin yanına sürprizin görülmemesi diye ikinci bir sorun ekleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kısa ve açık bir iş"
   - Cümle 4: «Elsa kraliçe olarak ona kısa ve açık bir iş verdi.»
   - Açıklama: 'Açık' sıfatı 'iş' kelimesine uymuyor; kastedilen açık bir talimat.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kısa ve açık bir iş verdi"
   - Cümle 4: «Elsa kraliçe olarak ona kısa ve açık bir iş verdi.»
   - Açıklama: 'Açık bir iş' kelimesi burada yanlış anlamda ve çocuk için anlaşılmaz kullanılmış.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Olaf, orada dur, gözlerini kapat ve ona kadar say"
   - Cümle 5: «"Olaf, orada dur, gözlerini kapat ve ona kadar say!" dedi Elsa.»
   - Açıklama: Göz kapatma çözümü rüzgarla uçan kurdeleye değil sürpriz sorununa yöneliyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kurdele limandaki bir direğe takılmıştı"
   - Cümle 7: «Kurdele limandaki bir direğe takılmıştı.»
   - Açıklama: Kurdele hiç aranmadan hazır bir yerde beliriyor ve çözüm sebepsizce geliyor.
   - Açıklama: Kurdele aranmadan sebepsizce bir direkte bulunuyor ve çözüm kendiliğinden geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0111` birebir aynı, ardından `@onarim: df15fb24b03346aa1b385e51b73af3e6857cbbdf`, sonra gövde.

### Hikâye 10: tohum elsa-0112 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0112
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gökkuşağı', fiil 'tekrarlamak', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: karın üstünde küçük bir yıldız belirdi | başını çevirip ışığı tacının yaptığını buldu
@tohum: elsa-0112
@degisim: gökkuşağı -> yıldız
Bir sabah Elsa karlı ormanda yürüyordu. Güneş ağaçların arasından parlıyordu. Birden karın üstünde küçük, parlak bir yıldız gördü. Elsa bu yıldızı çok merak etti. Eğildi ama karda hiçbir şey yoktu. Sonra başını çevirdi ve yıldız da kaydı. Elsa bunu birkaç kez tekrarladı. Her seferinde yıldız onunla birlikte gitti. Elsa elini başına götürdü ve tacına dokundu. Elsa bir kraliçeydi ve sabah parlak tacını takmıştı. Güneş tacın taşlarına vuruyor ve karda bu yıldızı yapıyordu. Elsa yıldızın nereden geldiğini bulduğu için güldü. Sonra onu ağaçtan ağaca gezdirip mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "karın üstünde küçük bir yıldız belirdi"
   - Cümle 0 (plan satırı): «karın üstünde küçük bir yıldız belirdi | başını çevirip ışığı tacının yaptığını buldu»
   - Açıklama: Karda beliren ışık bir sorun değil yalnız bir merak konusu; çözülmesi gereken bir dert yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "parlak bir yıldız gördü"
   - Cümle 3: «Birden karın üstünde küçük, parlak bir yıldız gördü.»
   - Açıklama: Karda yansıyan ışığa 'yıldız' denmesi mecazdır ve küçük çocuğu yanıltır.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karda bu yıldızı yapıyordu"
   - Cümle 11: «Güneş tacın taşlarına vuruyor ve karda bu yıldızı yapıyordu.»
   - Açıklama: Güneşin tactan yansıyan ışığına 'yıldız' demek mecazdır ve 3 yaşındaki çocuğu yanıltır.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra onu ağaçtan ağaca"
   - Cümle 13: «Sonra onu ağaçtan ağaca gezdirip mutlu mutlu oynadı.»
   - Açıklama: 'onu' zamirinin yıldızı mı tacı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0112` birebir aynı, `@degisim: gökkuşağı -> yıldız` (tutuyorsan), ardından `@onarim: 966a7078b54d4878accd2341ed11e0e979aaf1a8`, sonra gövde.

### Hikâye 11: tohum elsa-0113 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0113
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: sırayla oynamak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yelkenli', fiil 'taşınmak', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: ikisi birlikte üfledi ve oyuncak yelkenli devrildi | sırayla üflemek için açık bir kural koydu
@tohum: elsa-0113
@degisim: taşınmak -> üflemek
Elsa ile Anna limanda büyük bir kovanın başında oturuyordu. Kovada Anna'nın küçük oyuncak yelkenlisi yüzüyordu. İkisi de yelkenliye aynı anda üfledi ve yelkenli devrildi. Anna yelkenliyi düzeltti ve yeniden üflemek istedi. Elsa kraliçeydi ve hemen açık bir kural koydu. "Sırayla oynayalım, Anna. Önce sen üfle," dedi Elsa. Anna yavaşça üfledi ve yelkenli kovanın öbür ucuna gitti. Sonra sıra Elsa'ya geldi. Elsa da üfledi ve yelkenli geri döndü. Çalışkan Anna her seferinde yelkenliyi kovanın ortasına koydu. Yelkenli bir daha hiç devrilmedi. "Bu oyun sırayla çok daha güzel!" dedi Anna. Elsa bundan sonra Anna ile hep sırayla oynadı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sırayla üflemek için açık bir kural"
   - Cümle 0 (plan satırı): «ikisi birlikte üfledi ve oyuncak yelkenli devrildi | sırayla üflemek için açık bir kural koydu»
   - Açıklama: 'Açık bir kural' mecazlı ve soyut bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hemen açık bir kural koydu"
   - Cümle 5: «Elsa kraliçeydi ve hemen açık bir kural koydu.»
   - Açıklama: 'Açık bir kural' mecazlı ve soyut bir anlatım.
   - Açıklama: 'Açık bir kural koymak' soyut bir ifade, 3 yaşındaki çocuk için uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalışkan Anna her seferinde yelkenliyi kovanın ortasına koydu"
   - Cümle 11: «Çalışkan Anna her seferinde yelkenliyi kovanın ortasına koydu.»
   - Açıklama: Yelkenli kovanın uçlarına gidip dönerken her seferinde ortaya konması işlevsiz ve akışla uyuşmayan bir ayrıntı.
   - Açıklama: Yelkenliyi ortaya koyma ayrıntısı işlevsiz ve yelkenlinin uçtan uca gidip dönmesiyle uyuşmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0113` birebir aynı, `@degisim: taşınmak -> üflemek` (tutuyorsan), ardından `@onarim: acb24473f594ac21fa12dd954e1b877037fec29a`, sonra gövde.

### Hikâye 12: tohum elsa-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0115
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'filiz', fiil 'dolmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: elmalar derin karın içine batıyordu | elinden çıkan buzla geniş bir tabak yaptı
@tohum: elsa-0115
@degisim: filiz -> elma
Bir sabah Elsa dağda Sven ile dinleniyordu. Elsa'nın puantiyeli çantası kırmızı elmalarla dolmuştu. Elsa elmaları Sven ile paylaşmak istedi ama elmalar derin kara batıyordu. Sven burnunu kara soktu ve bir elmayı aradı. "Bekle, Sven, sana bir tabak yapayım," dedi Elsa. Elsa elini salladı ve buzdan geniş bir tabak yaptı. Tabağı karın üstüne koydu ve elmaların yarısını içine döktü. Sven başını salladı ve elmaları çıtır çıtır yedi. Elsa da kalan elmalardan birini aldı. "Bunlar da benim payım, Sven," dedi Elsa. Sonra ikisi karlı dağda yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (8):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'nın puantiyeli çantası kırmızı"
   - Cümle 2: «Elsa'nın puantiyeli çantası kırmızı elmalarla dolmuştu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmediği bir kelime.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Elsa'nın puantiyeli çantası kırmızı"
   - Cümle 2: «Elsa'nın puantiyeli çantası kırmızı elmalarla dolmuştu.»
   - Açıklama: Kartta Elsa'ya ait puantiyeli çanta gibi çağdaş bir eşya yok; kart dışı eşya ekleniyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Elsa'nın puantiyeli çantası"
   - Cümle 2: «Elsa'nın puantiyeli çantası kırmızı elmalarla dolmuştu.»
   - Açıklama: Kartta Elsa'ya ait puantiyeli bir çanta gibi bir eşya yok.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama elmalar derin kara batıyordu"
   - Cümle 3: «Elsa elmaları Sven ile paylaşmak istedi ama elmalar derin kara batıyordu.»
   - Açıklama: Elmaların neden kara düştüğü ya da battığı söylenmiyor; çantadaki elmaların kara batmasının sebebi yok.
   - Açıklama: Elmaların neden karın içine düştüğü ya da konduğu söylenmiyor; sorunun sebebi açık değil.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bunlar da benim payım"
   - Cümle 10: «"Bunlar da benim payım, Sven," dedi Elsa.»
   - Açıklama: Elsa tek elma aldığı halde çoğul 'Bunlar' kullanılmış; sayı uyumu bozuk.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bunlar da benim payım"
   - Cümle 10: «"Bunlar da benim payım, Sven," dedi Elsa.»
   - Açıklama: Elsa tek elma aldı ama 'Bunlar' çoğul diyor; sözcük duruma uymuyor.
7. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bunlar da benim payım, Sven"
   - Cümle 10: «"Bunlar da benim payım, Sven," dedi Elsa.»
   - Açıklama: Elsa yalnız bir elma alıyor ama çoğul 'bunlar' diyor.
8. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bunlar da benim payım"
   - Cümle 10: «"Bunlar da benim payım, Sven," dedi Elsa.»
   - Açıklama: Elsa kalan elmalardan yalnız birini alıyor ama 'bunlar benim payım' diyerek çoğul konuşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0115` birebir aynı, `@degisim: filiz -> elma` (tutuyorsan), ardından `@onarim: 7ab7308ef25e87363ce59fca90eb884475560873`, sonra gövde.
