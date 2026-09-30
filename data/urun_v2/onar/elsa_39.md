# Editör görevi (onarım): Elsa, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0150 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0150
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'bisküvi', fiil 'silmek', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: rüzgar oyundaki daireyi karla örttü | buzdan bir halka ve uzun bir çizgi yaptı
@tohum: elsa-0150
Limanda her yer karla kaplıydı ve Elsa kar topu oyunu oynuyordu. Karın üstüne bir daire çizmişti ve top daireye düşünce bisküvi yiyordu. Birden rüzgar esti ve daireyi karla örttü. Elsa karı eliyle sildi ama çizgi de kayboldu. Elsa biraz düşündü ve elini yere doğru tuttu. Elinden buz çıktı ve karda parlak bir buz halkası oldu. Sonra buzdan uzun bir çizgi de yaptı ve arkasına geçti. Rüzgar yine esti ama halka yerinden kıpırdamadı. Elsa ilk topu attı ve top tam halkaya düştü. Elsa sevinçle zıpladı ve bir bisküvi yedi. Elsa kar topu oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa karı eliyle sildi"
   - Cümle 4: «Elsa karı eliyle sildi ama çizgi de kayboldu.»
   - Açıklama: Kar silinmez; fiil nesnesine uymuyor, ayrıca dairenin yerine 'çizgi' deniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra buzdan uzun bir çizgi"
   - Cümle 7: «Sonra buzdan uzun bir çizgi de yaptı ve arkasına geçti.»
   - Açıklama: Tohumdaki buz özelliği bir kez yerine iki ayrı kez kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra buzdan uzun bir çizgi de yaptı"
   - Cümle 7: «Sonra buzdan uzun bir çizgi de yaptı ve arkasına geçti.»
   - Açıklama: Atış çizgisi daha önce kurulmamış ve karla örtülen daire sorununa hiçbir katkısı yok.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa sevinçle zıpladı"
   - Cümle 10: «Elsa sevinçle zıpladı ve bir bisküvi yedi.»
   - Açıklama: Üç cümle üst üste 'Elsa' ile başlıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0150` birebir aynı, ardından `@onarim: 9af0d674c06b1e7c7783fb22bb7c9024bb9253d7`, sonra gövde.

### Hikâye 2: tohum elsa-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0151
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yeni bir şeyi denemek
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tutkal', fiil 'yarışmak', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: geyik yarışta başla sözünü beklemeden koşuyordu | bayrak yaptı ve bayrak kalkınca koşmayı söyledi
@tohum: elsa-0151
Bir sabah Elsa ile Sven limanda ilk kez yarışacaktı. Çevik Sven çok heyecanlıydı. Ama Sven her seferinde Elsa başla demeden koşuyordu. Elsa bir dala tutkalla kırmızı bir kağıt yapıştırdı. Bu küçük bir bayrak oldu. "Sven, bayrak yukarı kalkınca koşacağız," dedi Elsa. Sven kraliçeye baktı ve başını salladı. İkisi çizginin arkasında yan yana durdu. Sven bu kez bayrağa baktı ve bekledi. Elsa bayrağı yukarı kaldırdı ve ikisi birlikte koştu. Sven kıyının sonuna ilk vardı ve sevinçle zıpladı. Elsa gülerek arkasından geldi. Elsa çok sevindi, çünkü ilk yarışları çok güzel başlamıştı.
```

**Hakem bulguları (11):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "başla sözünü beklemeden"
   - Cümle 0 (plan satırı): «geyik yarışta başla sözünü beklemeden koşuyordu | bayrak yaptı ve bayrak kalkınca koşmayı söyledi»
   - Açıklama: Aktarılan söz 'başla' tırnak içinde yazılmalı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "yarışta başla sözünü beklemeden"
   - Cümle 0 (plan satırı): «geyik yarışta başla sözünü beklemeden koşuyordu | bayrak yaptı ve bayrak kalkınca koşmayı söyledi»
   - Açıklama: Plandaki 'başla' sözü tırnak içinde yazılmalı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "limanda ilk kez yarışacaktı"
   - Cümle 1: «Bir sabah Elsa ile Sven limanda ilk kez yarışacaktı.»
   - Açıklama: İlk kez yarışacakları söyleniyor ama Sven'in her seferinde erken koştuğu söyleniyor.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Elsa başla demeden koşuyordu"
   - Cümle 3: «Ama Sven her seferinde Elsa başla demeden koşuyordu.»
   - Açıklama: Aktarılan söz 'başla' tırnak içinde yazılmalı.
5. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "her seferinde Elsa başla demeden"
   - Cümle 3: «Ama Sven her seferinde Elsa başla demeden koşuyordu.»
   - Açıklama: Aktarılan 'başla' sözü tırnak içinde yazılmalı.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sven her seferinde Elsa başla demeden koşuyordu"
   - Cümle 3: «Ama Sven her seferinde Elsa başla demeden koşuyordu.»
   - Açıklama: İlk kez yarışacakları söylenirken Sven'in her seferinde erken koştuğu söyleniyor.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa bir dala tutkalla kırmızı bir kağıt yapıştırdı"
   - Cümle 4: «Elsa bir dala tutkalla kırmızı bir kağıt yapıştırdı.»
   - Açıklama: Sven'in sabırsızlığına bayrağın neden sözden daha iyi geleceği gösterilmiyor; çözüm sebebe doğrudan yönelmiyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir dala tutkalla kırmızı bir kağıt yapıştırdı"
   - Cümle 4: «Elsa bir dala tutkalla kırmızı bir kağıt yapıştırdı.»
   - Açıklama: Limanda tutkal ve kağıt sebepsizce beliriyor.
9. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sven kraliçeye baktı"
   - Cümle 7: «Sven kraliçeye baktı ve başını salladı.»
   - Açıklama: 'Kraliçe' daha önce tanıtılmadı; Elsa'yı gösterdiği çocuk için belli değil.
10. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçeye baktı"
   - Cümle 7: «Sven kraliçeye baktı ve başını salladı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız hitap olarak geçiyor, sorunu bayrak çözüyor.
11. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçeye baktı ve"
   - Cümle 7: «Sven kraliçeye baktı ve başını salladı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0151` birebir aynı, ardından `@onarim: 357cb2ff3ef15df12e2adebec6a61f7ed2c59e1a`, sonra gövde.

### Hikâye 3: tohum elsa-0153 (deneme 1 -> 2)

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
@plan: ikisi de heykel oyununda saymak istedi | sırası gelenin başına kar yağdırdı
@tohum: elsa-0153
Ormanda hafif bir rüzgar esiyordu. Elsa ile Olaf büyük bir ağacın yanında heykel oyunu oynuyordu. Ama ikisi de ağaca dönüp saymak istedi. "Ben sayacağım!" dedi Olaf. Elsa biraz düşündü ve elini havaya kaldırdı. Elinden buz ve kar çıktı, Olaf'ın başına kar yağdı. "Kar kimin başına yağarsa, sayma sırası onda," dedi Elsa. Olaf sevinçle ağaca döndü ve saydı. Elsa kollarını oynattı ve yürüdü. Olaf dönünce Elsa hareketsiz durdu. Sonra Elsa kendi başına kar yağdırdı ve ağaca döndü. Bu kez Olaf durmaya çalıştı ama havuç burnu kıpırdadı. İkisi de çok güldü. Elsa çok mutluydu, çünkü sırayla oynadıkları için ikisi de saymıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa kendi başına kar"
   - Cümle 11: «Sonra Elsa kendi başına kar yağdırdı ve ağaca döndü.»
   - Açıklama: 'Kendi başına' hem 'tek başına' hem 'kendi kafasına' diye okunuyor, anlam belirsiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa kendi başına kar"
   - Cümle 11: «Sonra Elsa kendi başına kar yağdırdı ve ağaca döndü.»
   - Açıklama: 'Kendi başına' deyim olarak 'yalnız başına' anlamına da gelir; anlam belirsiz.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kendi başına kar yağdırdı"
   - Cümle 11: «Sonra Elsa kendi başına kar yağdırdı ve ağaca döndü.»
   - Açıklama: Tohumdaki buz ve kar özelliği bir kez değil iki kez kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Elsa kendi başına kar yağdırdı"
   - Cümle 11: «Sonra Elsa kendi başına kar yağdırdı ve ağaca döndü.»
   - Açıklama: Tohumdaki buz ve kar özelliği bir kez değil iki kez kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0153` birebir aynı, ardından `@onarim: 19520839cc8faa71b97602443b9bc94883b9c1f6`, sonra gövde.

### Hikâye 4: tohum elsa-0154 (deneme 1 -> 2)

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
@plan: kar topunu aynı anda ittiler ve top ayrıldı | sırayla itmeyi söyledi ve top büyüdü
@tohum: elsa-0154
@degisim: çamur -> kar
Elsa ile Kristoff dağda, buz sarayının önünde oynuyordu. Elmalı turtayı koymak için kardan büyük bir masa yapacaklardı. Ama ikisi kar topunu aynı anda itti ve top ikiye ayrıldı. Kristoff şaşırdı ve karın üstüne oturdu. Elsa hemen yeni ve küçük bir top yaptı. "Kristoff, önce sen on adım it, sonra ben," dedi Elsa. "Peki, kraliçem," dedi Kristoff ve güldü. Kristoff topu on adım itti ve top büyüdü. Sonra Elsa itti ve top daha da büyüdü. Sırayla ittiler ve top kocaman oldu. Kristoff turtayı topun üstüne koydu. "Bak, sırayla yaptık ve masa hazır, Kristoff!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ittiler ve top ayrıldı"
   - Cümle 0 (plan satırı): «kar topunu aynı anda ittiler ve top ayrıldı | sırayla itmeyi söyledi ve top büyüdü»
   - Açıklama: Top tek başına 'ayrılmaz'; 'ikiye ayrıldı' olmalı.
   - Açıklama: 'Top ayrıldı' gitti anlamına gelir; 'ikiye ayrıldı' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Peki, kraliçem," dedi Kristoff"
   - Cümle 7: «"Peki, kraliçem," dedi Kristoff ve güldü.»
   - Açıklama: Kraliçe özelliği yalnız hitap olarak geçiyor, kartın 'kız kardeşini korur' özelliği işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir hitapta geçiyor, olayda işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0154` birebir aynı, `@degisim: çamur -> kar` (tutuyorsan), ardından `@onarim: d420912eb07817ebeeb36e33f5bbef51888e9c47`, sonra gövde.

### Hikâye 5: tohum elsa-0155 (deneme 1 -> 2)

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
@plan: ılık güneş buzu kaygan yaptı ve geyik kaydı | yere halı serdi ve geyiğe halıyı gösterdi
@tohum: elsa-0155
Bir sabah dağda ılık bir güneş vardı. Sven, Elsa'nın buz sarayına oynamaya gelmişti. Ama güneş sarayın buz yerini ıslak ve kaygan yapmıştı. Sven içeri girince ayakları kaydı ve kendini durduramadı. Sonunda duvarın yanında yavaşça durdu. Elsa hemen sarayın köşesinden uzun, yumuşak bir halı getirdi. Halıyı kapıdan salona kadar yere serdi. Sonra Sven'e elini kaldırıp halıyı gösterdi. Sven kraliçenin gösterdiği halıya dikkatle bastı. Ayakları bu kez hiç kaymadı. Sven halının üstünde rahatça yürüdü ve başını salladı. Elsa çok sevindi, çünkü Sven artık sarayda kaymadan yürüyebiliyordu.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sarayın buz yerini ıslak"
   - Cümle 3: «Ama güneş sarayın buz yerini ıslak ve kaygan yapmıştı.»
   - Açıklama: 'Buz yerini' bozuk tamlama; 'buzdan yerini' ya da 'buz zeminini' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sarayın buz yerini ıslak"
   - Cümle 3: «Ama güneş sarayın buz yerini ıslak ve kaygan yapmıştı.»
   - Açıklama: 'buz yeri' yanlış kelime; 'buz zemini' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sven kraliçenin gösterdiği halıya"
   - Cümle 9: «Sven kraliçenin gösterdiği halıya dikkatle bastı.»
   - Açıklama: 'Kraliçe' hikayede tanıtılmadan Elsa yerine kullanılıyor, kimi gösterdiği belirsiz.
   - Açıklama: Elsa bir anda 'kraliçe' diye anılıyor; kimi gösterdiği belli değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçenin gösterdiği halıya"
   - Cümle 9: «Sven kraliçenin gösterdiği halıya dikkatle bastı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Kartın özellikler alanındaki kraliçelik çözümde işe yaramıyor; halı sermek kraliçeliğe bağlı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0155` birebir aynı, ardından `@onarim: 82f576e065410252075dba9e3a7155a732b504eb`, sonra gövde.

### Hikâye 6: tohum elsa-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0156
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'nane', fiil 'kapamak', sıfat 'kilitli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kapı kilitli değildi ve kardeşi erken geldi | kardeşine saymasını söyledi ve pastayı bitirdi
@tohum: elsa-0156
Dağın tepesindeki buz sarayı çok sessizdi. Elsa, Anna'nın doğum günü için nane yapraklı bir pasta yapıyordu. Ama kapı kilitli değildi ve Anna erkenden içeri girdi. Pasta daha bitmemişti. Elsa hemen pastanın önüne geçti. "Anna, gözlerini kapat ve yavaşça say," dedi Elsa. "Tamam, kraliçem," dedi Anna gülerek. Anna gözlerini kapadı ve saymaya başladı. Elsa pastanın üstüne son nane yapraklarını dizdi. "Şimdi gözlerini açabilirsin," dedi Elsa. Anna pastayı görünce sevinçle zıpladı. "Bu çok güzel bir sürpriz, Elsa!" dedi Anna. Elsa bundan sonra sürpriz hazırlarken önce kapıyı kilitledi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçem," dedi Anna gülerek"
   - Cümle 7: «"Tamam, kraliçem," dedi Anna gülerek.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız hitap olarak geçiyor, çözümde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Tamam, kraliçem," dedi Anna"
   - Cümle 7: «"Tamam, kraliçem," dedi Anna gülerek.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız Anna'nın hitabında geçiyor, kardeşi koruma işine yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0156` birebir aynı, ardından `@onarim: 4d265cf98a94e46cec767d50d353164cc10bb56d`, sonra gövde.

### Hikâye 7: tohum elsa-0157 (deneme 1 -> 2)

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
@plan: ikisi topu aynı anda itti ve top dağıldı | sırayla oynama kuralı koydu
@tohum: elsa-0157
@degisim: cesur -> kocaman
Bir sabah Elsa ile Kristoff limanda kardan bir dondurma yapıyordu. İkisi de kar topunu aynı anda itti. Top ikiye ayrıldı ve yere dağıldı. "Önce ben yapacağım!" dedi Kristoff. Elsa elini kaldırdı. "Kristoff, kraliçe olarak bir kural koyuyorum: sırayla oynayacağız," dedi Elsa. Kristoff başını salladı ve kabul etti. Önce Kristoff yeni bir topu üç kez yuvarladı. Sonra sıra Elsa'ya geldi ve o da üç kez yuvarladı. Her sırada ikisi de topu biraz daha büyüttü. Sonunda kocaman, yuvarlak bir dondurma topu oldu. Elsa ile Kristoff yeni toplar yapmaya sırayla ve mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kraliçe olarak bir kural koyuyorum"
   - Cümle 6: «"Kristoff, kraliçe olarak bir kural koyuyorum: sırayla oynayacağız," dedi Elsa.»
   - Açıklama: 'Kraliçe olarak kural koymak' küçük çocuk için soyut bir anlatım.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe olarak bir kural koyuyorum"
   - Cümle 6: «"Kristoff, kraliçe olarak bir kural koyuyorum: sırayla oynayacağız," dedi Elsa.»
   - Açıklama: Karttaki özellik kraliçeliği kız kardeşini korumakla tanımlıyor; burada Kristoff'a oyun kuralı dayatmak için kullanılıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Her sırada ikisi de"
   - Cümle 10: «Her sırada ikisi de topu biraz daha büyüttü.»
   - Açıklama: 'Her sırada' anlatımı dilbilgisel olarak kurulmamış; 'Her seferinde' ya da 'Sırası gelince' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0157` birebir aynı, `@degisim: cesur -> kocaman` (tutuyorsan), ardından `@onarim: 25164c8b2e41a0fc1edce89f814a98073007ad9a`, sonra gövde.

### Hikâye 8: tohum elsa-0158 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar masadaki örtüyü havaya kaldırdı | kardan adama ucu tutturdu ve teraziyi koydu
@tohum: elsa-0158
Elsa limanda Olaf ile ilk kar için neşeli bir şenlik hazırlıyordu. Olaf masaya beyaz bir örtü serdi. Ama rüzgar esti ve örtü havaya kalktı. Kurabiye tabakları masada duramadı. Kraliçe Elsa hemen Olaf'a ne yapacağını söyledi. "Olaf, sen örtünün bu ucunu sıkıca tut," dedi Elsa. Olaf ucu iki eliyle tuttu. Elsa limanın ağır terazisini getirdi ve örtünün öbür ucuna koydu. Sonra Olaf kendi ucuna bir kurabiye tabağı koydu. Örtü artık rüzgarda kalkmadı. İkisi kurabiyeleri masada güzelce düzenledi. "Bu şenlik harika olacak!" dedi Olaf. Sonra Elsa ile Olaf şenliğe mutlu mutlu başladı.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Kraliçe Elsa hemen Olaf'a ne yapacağını söyledi"
   - Cümle 5: «Kraliçe Elsa hemen Olaf'a ne yapacağını söyledi.»
   - Açıklama: Hemen ardından gelen replik aynı şeyi söylediği için bu cümle gereksiz tekrar.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen Olaf'a"
   - Cümle 5: «Kraliçe Elsa hemen Olaf'a ne yapacağını söyledi.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden ve farklı adla anılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen Olaf'a ne yapacağını söyledi"
   - Cümle 5: «Kraliçe Elsa hemen Olaf'a ne yapacağını söyledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan ve emir olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "limanın ağır terazisini getirdi"
   - Cümle 8: «Elsa limanın ağır terazisini getirdi ve örtünün öbür ucuna koydu.»
   - Açıklama: Ağır terazi hiç kurulmadan çözümü getirmek için sebepsizce beliriyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Olaf kendi ucuna bir kurabiye tabağı koydu"
   - Cümle 9: «Sonra Olaf kendi ucuna bir kurabiye tabağı koydu.»
   - Açıklama: Çözüm tutma, terazi koyma ve tabak koyma olarak iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0158` birebir aynı, ardından `@onarim: d348e76c5497baeb39227aaf92c668f6cb502e35`, sonra gövde.

### Hikâye 9: tohum elsa-0159 (deneme 1 -> 2)

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
@plan: rüzgar esti ve süs elinden uçup kayboldu | karda ve kapıda aradı, süsü saçında buldu
@tohum: elsa-0159
Bir sabah dağa sulu kar yağıyordu. Kraliçe Elsa, buz sarayının kapısına yeni bir süs asmak istiyordu. Ama rüzgar esti, süs elinden uçtu ve kayboldu. Elsa kapının önündeki kara eğildi ve baktı. Sulu karın içinde yalnız küçük taşlar vardı. Sonra kapının iki yanına da baktı. Süsü hiçbir yerde göremedi. Elsa başını salladı. Tam o sırada saçında bir şey parladı. Süs rüzgarla uçmuş ve saçına takılmıştı. Bu süs Elsa'yı çok güldürdü. Elsa süsü çıkardı ve kapıya astı. Elsa çok sevindi, çünkü süsünü hiç uzağa gitmeden bulmuştu.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, buz sarayının kapısına"
   - Cümle 2: «Kraliçe Elsa, buz sarayının kapısına yeni bir süs asmak istiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, buz sarayının"
   - Cümle 2: «Kraliçe Elsa, buz sarayının kapısına yeni bir süs asmak istiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; sorunun çözümünde kullanılmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Tam o sırada saçında bir şey parladı"
   - Cümle 9: «Tam o sırada saçında bir şey parladı.»
   - Açıklama: Elsa'nın aramaları sonuç vermiyor ve süs, çözüm adımlarından değil tesadüften bulunuyor.
   - Açıklama: Süs Elsa'nın aramasıyla değil tesadüfen bulunuyor; çözüm sebebe yönelmiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Süs rüzgarla uçmuş ve saçına takılmıştı"
   - Cümle 10: «Süs rüzgarla uçmuş ve saçına takılmıştı.»
   - Açıklama: Çözüm, figürün eyleminden çıkmadan sebepsizce ortaya çıkıyor.
   - Açıklama: Çözüm sebepsiz bir rastlantıyla geliyor ve karda yapılan arama sonuca bağlanmıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu süs Elsa'yı çok güldürdü"
   - Cümle 11: «Bu süs Elsa'yı çok güldürdü.»
   - Açıklama: Süs kendisi güldürmez; fiil öznesine uymuyor.
   - Açıklama: Güldüren süsün kendisi değil olaydır; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0159` birebir aynı, ardından `@onarim: 7704e3381d5273e54cde9e39204a6adb3db24fe9`, sonra gövde.

### Hikâye 10: tohum elsa-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0160
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'meşe', fiil 'sakinleşmek', sıfat 'güzel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kar topu dala çarptı ve ağaca gitmedi | kardeşini sakinleştirdi ve ağaca atmasını söyledi
@tohum: elsa-0160
Rüzgar dağda hafifçe esiyordu. Elsa ile Anna güzel bir meşe ağacına kar topu atıyordu. Ama Anna'nın topu bir dala çarptı ve kar onun başına döküldü. Anna kızdı ve topları çok hızlı atmaya başladı. Hiçbir top ağaca gitmedi. Elsa kardeşinin başından karı eliyle temizledi. "Anna, acele etme ve topu ağaca doğru at," dedi kraliçe Elsa. Anna sakinleşti ve topu yavaşça attı. Top tam ağaca çarptı. "Başardım, Elsa!" dedi Anna. Anna sevinçle zıpladı ve Elsa'ya sarıldı. Elsa çok sevindi, çünkü Anna topu sonunda ağaca atmıştı.
```

**Hakem bulguları (6):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "kar onun başına döküldü"
   - Cümle 3: «Ama Anna'nın topu bir dala çarptı ve kar onun başına döküldü.»
   - Açıklama: Karın başa dökülmesi ve topların ağaca gitmemesi iki ayrı sorun olarak görünüyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Anna'nın topu bir dala çarptı"
   - Cümle 3: «Ama Anna'nın topu bir dala çarptı ve kar onun başına döküldü.»
   - Açıklama: Dal ağacın parçası olduğu için dala çarpmak ağaca çarpmak sayılır; sorunun sebebi karışık ve inandırıcı değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hiçbir top ağaca gitmedi"
   - Cümle 5: «Hiçbir top ağaca gitmedi.»
   - Açıklama: Top ağaca gitmez; 'ağaca çarpmadı' ya da 'ağaca ulaşmadı' olmalı.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Hiçbir top ağaca gitmedi"
   - Cümle 5: «Hiçbir top ağaca gitmedi.»
   - Açıklama: Asıl sorun olan topların ağaca gitmemesi ancak 5. cümlede söyleniyor.
5. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 7: «"Anna, acele etme ve topu ağaca doğru at," dedi kraliçe Elsa.»
   - Açıklama: Ada bağlı unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Unvan addan önce gelince büyük harfle yazılır: 'Kraliçe Elsa'.
6. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Anna sakinleşti ve topu yavaşça attı"
   - Cümle 8: «Anna sakinleşti ve topu yavaşça attı.»
   - Açıklama: Sorunu figür Elsa değil, topu atan yan karakter Anna çözüyor; Elsa yalnız öğüt veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0160` birebir aynı, ardından `@onarim: a8400f8c214065d5d5b1af8111424c9f3bf26fc2`, sonra gövde.

### Hikâye 11: tohum elsa-0161 (deneme 1 -> 2)

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
@plan: uçurtmanın ipi geyiğin başına dolandı | geyiğe durmasını söyledi ve ipi çözdü
@tohum: elsa-0161
Bir sabah Elsa sarayın önünde mavi bir uçurtma uçuruyordu. Sven de onu izliyordu. Birden rüzgar durdu ve uçurtmanın ipi Sven'in başına dolandı. Sven başını salladı ama ipi çıkaramadı. Sonra döndü ve gürültülü sesler çıkardı. İp daha çok dolandı. "Sven, dur ve biraz eğil!" dedi kraliçe Elsa yüksek sesle. Sven hemen durdu ve Elsa'ya doğru eğildi. Elsa ipi Sven'in başından yavaşça çözdü. Sonra uçurtmayı dikkatle yere koydu. Sven sevinçle burnunu Elsa'nın eline sürttü. Elsa çok mutlu oldu, çünkü Sven'e yardım etmişti.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "uçurtmanın ipi Sven'in başına dolandı"
   - Cümle 3: «Birden rüzgar durdu ve uçurtmanın ipi Sven'in başına dolandı.»
   - Açıklama: Bir hayvanın başına ipin dolanıp daha çok sıkışması boğulma çağrıştıran ürkütücü bir öğe olabilir.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa yüksek"
   - Cümle 7: «"Sven, dur ve biraz eğil!" dedi kraliçe Elsa yüksek sesle.»
   - Açıklama: Ada bağlı unvan büyük harfle yazılmalı: 'Kraliçe Elsa'.
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa yüksek sesle"
   - Cümle 7: «"Sven, dur ve biraz eğil!" dedi kraliçe Elsa yüksek sesle.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği işe yarar biçimde kullanılmıyor; yalnız unvan olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0161` birebir aynı, ardından `@onarim: c50431bd0011b0853545157139020a2c33f06958`, sonra gövde.

### Hikâye 12: tohum elsa-0162 (deneme 1 -> 2)

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
@plan: dalgalar taşları ıslattı ve çember kaydı | kıyıdan uzak kuru meydana geçti
@tohum: elsa-0162
Elsa limanda ilk kez çember çevirmeyi deniyordu. Ama deniz o sabah çok dalgalıydı. Dalgalar kıyıya vurdu ve taşları ıslattı. Çember ıslak taşların üstünde kaydı ve düştü. Elsa çemberi ve taşları dikkatle inceledi. Taşlar yalnız kıyıya yakın yerde ıslaktı. Elsa kraliçe olarak limana bir kural koymuştu. Bu kural, oyunda kıyıdan uzak durmaktı. Elsa hemen kuru meydana geçti. Orada çemberi yeniden yuvarladı. Bu kez çember kaymadı ve uzun süre döndü. Sonra Elsa meydanda çemberiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kraliçe olarak limana bir kural koymuştu"
   - Cümle 7: «Elsa kraliçe olarak limana bir kural koymuştu.»
   - Açıklama: 'Kural koymak' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Kraliçe olarak kural koymak' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçe olarak limana bir kural koymuştu"
   - Cümle 7: «Elsa kraliçe olarak limana bir kural koymuştu.»
   - Açıklama: Kural daha önce kurulmadan birden ortaya çıkıyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Kural sebepsiz beliriyor ve kendi koyduğu kurala neden uymadığı açıklanmıyor.
   - Açıklama: Daha önce hiç anılmayan kural çözümü sebepsizce getiriyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu kural, oyunda kıyıdan uzak durmaktı"
   - Cümle 8: «Bu kural, oyunda kıyıdan uzak durmaktı.»
   - Açıklama: Elsa kıyıdan uzak durma kuralını kendisi koymuşken kıyıda oynuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0162` birebir aynı, ardından `@onarim: 51df01997e78ec585953235abddc11e12d778df8`, sonra gövde.
