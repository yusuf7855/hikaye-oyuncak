# Editör görevi (onarım): Elsa, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0029 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0029
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'demet', fiil 'zıplamak', sıfat 'turuncu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: ikisi hep aynı anda zıpladı ve kimin kazandığını göremediler | sırayla zıplamayı önerdi
@tohum: elsa-0029
Rüzgar ağaçların arasında hafifçe esiyordu. Elsa ile Kristoff karlı ormanda zıplama oyunu oynuyordu. Ama ikisi hep aynı anda zıpladı ve kimin daha uzağa gittiğini göremediler. "Sırayla zıplayalım, Kristoff. Kraliçe olarak ilk sırayı sana veriyorum," dedi Elsa. Kristoff güldü ve çantasından bir demet turuncu havuç çıkardı. "Havuçlar yerimizi gösterecek," dedi Kristoff. Önce Kristoff zıpladı ve durduğu yere bir havuç koydu. Sonra Elsa zıpladı. Elsa'nın havucu biraz daha ileride durdu. İkisi sırayla birkaç kez daha zıpladı. İkisi de çok sevindi, çünkü artık kimin uzağa zıpladığını görebiliyorlardı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe olarak ilk sırayı sana veriyorum"
   - Cümle 5: «Kraliçe olarak ilk sırayı sana veriyorum," dedi Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız söz olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "çantasından bir demet turuncu havuç çıkardı"
   - Cümle 6: «Kristoff güldü ve çantasından bir demet turuncu havuç çıkardı.»
   - Açıklama: Kimin uzağa zıpladığını görmeyi sağlayan havuç fikri figür Elsa'dan değil Kristoff'tan geliyor.
   - Açıklama: Kimin uzağa zıpladığını görmeyi sağlayan havuç işaretleri fikrini ve nesnesini Kristoff getiriyor, yani sorunu asıl yan karakter çözüyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kimin uzağa zıpladığını görebiliyorlardı"
   - Cümle 12: «İkisi de çok sevindi, çünkü artık kimin uzağa zıpladığını görebiliyorlardı.»
   - Açıklama: Karşılaştırma için 'daha uzağa' olmalı; 'uzağa' anlamı bozuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0029` birebir aynı, ardından `@onarim: 8685b3ecf8ab1f307f046c517e3e9da6c3fd56e0`, sonra gövde.

### Hikâye 2: tohum elsa-0031 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Anna
@tohum: elsa-0031
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'heykel', fiil 'damlamak', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | Anna
@plan: buzdan heykelden resmin üstüne su damladı | özür diledi ve kardeşiyle yeni bir resim yaptı
@tohum: elsa-0031
Bir sabah Anna sarayın büyük salonunda çizgili bir top resmi yapıyordu. Elsa masada resmin hemen yanına buzdan küçük bir heykel yaptı. Ama salon sıcaktı ve heykelden resmin üstüne su damladı. Resimdeki çizgiler birbirine karıştı. Anna üzüldü ve ıslak resmine baktı. "Özür dilerim, Anna. Heykeli resmine çok yakın yaptım," dedi Elsa. Elsa heykeli hemen dışarıya, soğuk karın üstüne götürdü. Sonra masadan temiz bir kağıt aldı. "Birlikte yeni bir top çizelim mi?" diye sordu Elsa. Anna gülümsedi ve başını salladı. İki kardeş yan yana oturdu ve yeni bir top çizdi. Sonra resim yapmaya mutlu mutlu devam ettiler.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "buzdan heykelden resmin"
   - Cümle 0 (plan satırı): «buzdan heykelden resmin üstüne su damladı | özür diledi ve kardeşiyle yeni bir resim yaptı»
   - Açıklama: Art arda iki ayrılma eki bozuk bir yapı kuruyor; 'buz heykelden' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "buzdan küçük bir heykel yaptı"
   - Cümle 2: «Elsa masada resmin hemen yanına buzdan küçük bir heykel yaptı.»
   - Açıklama: Buz özelliği sorunu çözmek yerine resmi bozarak sorun yaratıyor; işe yarar biçimde kullanılmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa heykeli hemen dışarıya, soğuk karın üstüne götürdü"
   - Cümle 8: «Elsa heykeli hemen dışarıya, soğuk karın üstüne götürdü.»
   - Açıklama: Çözüm özür, heykeli dışarı taşıma, yeni kağıt alma ve birlikte çizme olarak iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0031` birebir aynı, ardından `@onarim: 5286654b785f8a6172c2448a3c759ba70f65908a`, sonra gövde.

### Hikâye 3: tohum elsa-0032 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0032
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'buğday', fiil 'sıçramak', sıfat 'sıkı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kar çok yumuşaktı ve kardan adamın ayakları battı | karın üstüne buzdan düz taşlar dizdi
@tohum: elsa-0032
@degisim: buğday -> taş
Elsa ile Olaf karlı ormanda yürüyordu. Olaf ağaçların arasında sıçrama oyunu oynamak istiyordu. Ama kar çok yumuşaktı ve Olaf'ın ayakları hep kara battı. "Hiç zıplayamıyorum!" dedi Olaf. Elsa ona yardım etmek istedi. Elinden buz çıkardı ve karın üstüne buzdan düz taşlar dizdi. Taşlar çok sıkı ve sertti. "Bu taşlarda dene, Olaf," dedi Elsa. Olaf ilk taşa sıçradı. Ayakları bu kez hiç batmadı. Olaf taştan taşa sıçradı ve güldü. Sonra Elsa'ya koştu ve ona sarıldı. "Teşekkürler, Elsa, bu en güzel oyun!" dedi Olaf.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Taşlar çok sıkı ve sertti"
   - Cümle 7: «Taşlar çok sıkı ve sertti.»
   - Açıklama: 'Sıkı' taş için uygun bir sıfat değil.
   - Açıklama: Taş için 'sıkı' sıfatı uygun değil.
   - Açıklama: 'Sıkı' sıfatı taşlara uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0032` birebir aynı, `@degisim: buğday -> taş` (tutuyorsan), ardından `@onarim: 64f8cc046465f3e54bc0098ada41f6865d4892e0`, sonra gövde.

### Hikâye 4: tohum elsa-0033 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0033
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'şekerleme', fiil 'ayırmak', sıfat 'sevecen'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: kardeşinin saçı alçak bir dala takıldı | saç tellerini daldan tek tek ayırdı
@tohum: elsa-0033
Karlı ormanda Elsa ile Anna yan yana yürüyordu. Birden Anna'nın saçı alçak bir dala takıldı. Anna başını çevirdi ama saçı daldan çıkmadı. Anna saçını hızla çekmek istedi. Kraliçe Elsa kardeşini korumak için onun elini yavaşça tuttu. Sonra saç tellerini daldan tek tek ayırdı. Sonunda Anna'nın saçı daldan kurtuldu. Anna sevinçle Elsa'ya sarıldı. Cebinden iki şekerleme çıkardı ve birini Elsa'ya verdi. Elsa ona sevecen bir gülümsemeyle baktı. Anna çok mutluydu, çünkü Elsa ona yardım etmişti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini korumak"
   - Cümle 5: «Kraliçe Elsa kardeşini korumak için onun elini yavaşça tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Cebinden iki şekerleme çıkardı"
   - Cümle 9: «Cebinden iki şekerleme çıkardı ve birini Elsa'ya verdi.»
   - Açıklama: Şekerlemeler sebepsiz beliriyor ve olaydan çıkmıyor.
   - Açıklama: Şekerleme sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ona sevecen bir gülümsemeyle"
   - Cümle 10: «Elsa ona sevecen bir gülümsemeyle baktı.»
   - Açıklama: 'Sevecen bir gülümseme' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir anlatım.
   - Açıklama: 'Sevecen bir gülümseme' soyut ve küçük çocuğa ağır bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0033` birebir aynı, ardından `@onarim: 9da420c51fbbd0e40f23a0f0042bfd392fdeca9c`, sonra gövde.

### Hikâye 5: tohum elsa-0034 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0034
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kabak', fiil 'yakalamak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: rüzgar şapkayı suya doğru uçurdu | hemen koştu ve şapkayı kıyıda yakaladı
@tohum: elsa-0034
@degisim: kabak -> şapka
Elsa limanda Kristoff ile yürüyordu. Kıyıda güçlü bir rüzgar esiyordu. Birden rüzgar Kristoff'un şapkasını başından uçurdu. Şapka kumda suya doğru yuvarlandı. "Şapkam suya gidiyor!" dedi Kristoff. Elsa hemen koştu. Şapka suya düşmeden önce, Elsa onu incecik ipinden yakaladı. Sonra şapkayı Kristoff'a geri verdi. Kristoff şapkasını başına taktı ve ipini sıkıca bağladı. Artık şapka rüzgarda hiç uçmadı. "Teşekkürler, kraliçem, çok hızlıydın!" dedi Kristoff. Elsa güldü. İkisi limanda yürümeye mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şapka suya düşmeden önce"
   - Cümle 7: «Şapka suya düşmeden önce, Elsa onu incecik ipinden yakaladı.»
   - Açıklama: Rüzgarla suya giden eşyanın peşinden su kenarına koşmak çocuğun taklit edebileceği tehlikeli bir davranış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Teşekkürler, kraliçem, çok hızlıydın"
   - Cümle 11: «"Teşekkürler, kraliçem, çok hızlıydın!" dedi Kristoff.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir hitap sözü olarak geçiyor, kartın 'ozellikler' alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız hitap olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0034` birebir aynı, `@degisim: kabak -> şapka` (tutuyorsan), ardından `@onarim: 81a385929bb0acd30f4d098346c8843a64486486`, sonra gövde.

### Hikâye 6: tohum elsa-0035 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0035
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'tomurcuk', fiil 'esnemek', sıfat 'yemyeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: top çok hızlı gitti ve bir dala takıldı | dalı yavaşça çekti ve top düştü
@tohum: elsa-0035
@degisim: tomurcuk -> top
Soğuk bir rüzgar esiyordu. Elsa dağda buzdan bir halka yapmış, topunu halkadan geçirmeye çalışıyordu. Ama top çok hızlı gitti ve yemyeşil bir ağacın dalına takıldı. Elsa uzandı ama topa ulaşamadı. Sonra dalın alçak ucunu tuttu ve yavaşça aşağı çekti. Dal esnedi ve eğildi. Top dalın üstünden kaydı ve yumuşak kara düştü. Elsa dalı yavaşça bıraktı. Topu kardan aldı ve bu kez daha yavaş attı. Top halkadan rahatça geçti. Elsa çok sevindi, çünkü topunu kurtarmış ve oyununa dönmüştü.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa dağda buzdan bir halka yapmış"
   - Cümle 2: «Elsa dağda buzdan bir halka yapmış, topunu halkadan geçirmeye çalışıyordu.»
   - Açıklama: Kartın 'ozellikler' alanındaki buz gücü yalnız süs olarak kullanılıyor, sorunun çözümünde işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dal esnedi ve eğildi"
   - Cümle 6: «Dal esnedi ve eğildi.»
   - Açıklama: Dal için 'esnemek' küçük çocuğun bildiği anlamda değil, 'esnemek' ona uykudan esnemeyi çağrıştırır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0035` birebir aynı, `@degisim: tomurcuk -> top` (tutuyorsan), ardından `@onarim: ba3cb2b9fa40143411edc1018cd1e908c2826b30`, sonra gövde.
