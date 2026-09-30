# Editör görevi (onarım): Elsa, onarım partisi 43

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar43.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar43.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0149 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0149
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'maske', fiil 'karışmak', sıfat 'sakar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: rüzgar esti ve daldan şeklin üstüne kar düşecekti | dalın üstündeki karı eliyle öbür yana itti
@tohum: elsa-0149
@degisim: sakar -> kocaman
Elsa karlı ormanda tek başına yürüyordu. Birden bir ağacın gövdesinde maskeye benzeyen kocaman bir kar şekli fark etti. Ama rüzgar esiyordu ve üstteki daldan şeklin üstüne kar düşecekti. Elsa bir kraliçeydi ve bu şekli korumak istedi. Dalın üstündeki karı eliyle yavaşça öbür yana itti. Kar ağacın yanına döküldü ve şekle hiç değmedi. Sonra Elsa şekle yakından baktı. Kar taneleri birbirine karışmış ve iki göz, gülen bir ağız olmuştu. Elsa bu şekle bakıp çok sevindi. Elsa ormanda başka şekiller aramaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "üstteki daldan şeklin üstüne kar düşecekti"
   - Cümle 3: «Ama rüzgar esiyordu ve üstteki daldan şeklin üstüne kar düşecekti.»
   - Açıklama: Kardan bir şeklin üstüne kar düşme ihtimali henüz olmamış ve çocuk için önemsiz bir sorun.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve bu şekli korumak istedi"
   - Cümle 4: «Elsa bir kraliçeydi ve bu şekli korumak istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, çözümde işe yarar biçimde kullanılmıyor.
   - Açıklama: Kartın özellik alanındaki kraliçelik bir kar şeklini korumaya gerekçe yapılmış, çözümde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve bu şekli korumak istedi"
   - Cümle 4: «Elsa bir kraliçeydi ve bu şekli korumak istedi.»
   - Açıklama: Elsa'nın kraliçe olması şekli korumak istemesine sebep değil, işlevsiz bir ayrıntı olarak ekleniyor.
   - Açıklama: Kraliçe olmak şekli korumak istemenin sebebi değil; işlevsiz ve mantıksız bir bağlantı kuruluyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iki göz, gülen bir ağız olmuştu"
   - Cümle 8: «Kar taneleri birbirine karışmış ve iki göz, gülen bir ağız olmuştu.»
   - Açıklama: Cümle kuruluşu bozuk; 'iki göz ve gülen bir ağız oluşturmuştu' gibi olmalı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kar taneleri birbirine karışmış"
   - Cümle 8: «Kar taneleri birbirine karışmış ve iki göz, gülen bir ağız olmuştu.»
   - Açıklama: 'Karışmak' fiili kar tanelerinin bir yüz şekli oluşturmasını anlatmaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0149` birebir aynı, `@degisim: sakar -> kocaman` (tutuyorsan), ardından `@onarim: 5b382fe4c2d12e9f33a49bfe09d65485cb5e3ee9`, sonra gövde.

### Hikâye 2: tohum elsa-0150 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar oyundaki daireyi karla örttü | buzdan parlak bir halka yaptı
@tohum: elsa-0150
Limanda her yer karla kaplıydı ve Elsa kar topu oyunu oynuyordu. Karın üstüne bir daire çizmişti ve top daireye düşünce bisküvi yiyordu. Birden rüzgar esti ve daireyi karla örttü. Elsa karı itti ama eli daireyi de sildi. Elsa biraz düşündü ve elini yere doğru tuttu. Elinden buz çıktı ve karda parlak bir buz halkası oldu. Rüzgar yine uzun uzun esti ama halka yerinden kıpırdamadı. Elsa ilk topu attı. Top tam halkaya düştü ve Elsa sevinçle bir bisküvi yedi. Sonra kar topu oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "top daireye düşünce bisküvi yiyordu"
   - Cümle 2: «Karın üstüne bir daire çizmişti ve top daireye düşünce bisküvi yiyordu.»
   - Açıklama: Cümlede 'yiyordu' fiilinin öznesi 'top' gibi okunuyor; top bisküvi yemez.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve daireyi karla örttü"
   - Cümle 3: «Birden rüzgar esti ve daireyi karla örttü.»
   - Açıklama: Rüzgarın oyun dairesini örtmesi 'rüzgar yaprakları dağıttı' örneğine benzeyen önemsiz bir olay.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgar esti ve daireyi karla örttü"
   - Cümle 3: «Birden rüzgar esti ve daireyi karla örttü.»
   - Açıklama: Karla örtülen çizili daire yeniden çizilebilecek önemsiz bir olay; örnekteki rüzgarın oyunu bozması kalıbına benziyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa karı itti ama eli daireyi de sildi"
   - Cümle 4: «Elsa karı itti ama eli daireyi de sildi.»
   - Açıklama: Önce başarısız bir deneme geliyor ve buz halkasının yerinden kıpırdamaması sorunun sebebi olan karla örtülmeye doğrudan yönelmiyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "halka yerinden kıpırdamadı"
   - Cümle 7: «Rüzgar yine uzun uzun esti ama halka yerinden kıpırdamadı.»
   - Açıklama: Sorun dairenin karla örtülmesiydi ama çözüm halkanın kıpırdamamasını gösteriyor, karla örtülmeye doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0150` birebir aynı, ardından `@onarim: 1293f33f4eb3bac713116c9daf9d311635b24bd0`, sonra gövde.

### Hikâye 3: tohum elsa-0151 (deneme 2 -> 3)

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
@plan: geyik yarışta işareti beklemeden koştu | kağıttan bir bayrak yaptı ve onu yukarı kaldırdı
@tohum: elsa-0151
Bir sabah Elsa ile Sven limanda ilk kez yarışacaktı. Elsa kraliçe olduğu için yarışta işareti o verecekti. Ama çevik Sven çok heyecanlıydı ve Elsa "Başla!" demeden koştu. Elsa, Sven'i yeniden yanına çağırdı. Yakındaki bir kutuda tutkal ve kırmızı bir kağıt vardı. Elsa kağıdı tutkalla bir dala yapıştırdı ve küçük bir bayrak yaptı. "Sven, bu bayrak kalkınca koşacağız," dedi Elsa. Sven bayrağa baktı ve başını salladı. Sven bu kez yerinden kıpırdamadan bekledi. Elsa bayrağı yukarı kaldırdı ve ikisi birlikte koştu. Sven yolun sonuna ilk vardı ve sevinçle zıpladı. Elsa gülerek arkasından geldi. Elsa çok sevindi, çünkü ilk yarışları çok güzel olmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yakındaki bir kutuda tutkal ve kırmızı bir kağıt vardı"
   - Cümle 5: «Yakındaki bir kutuda tutkal ve kırmızı bir kağıt vardı.»
   - Açıklama: Tutkal ve kağıt çözüm için sebepsizce hazır beliriyor.
   - Açıklama: Tutkal ve kağıt limanda sebepsizce hazır beliriyor ve çözümü kolayca getiriyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "küçük bir bayrak yaptı"
   - Cümle 6: «Elsa kağıdı tutkalla bir dala yapıştırdı ve küçük bir bayrak yaptı.»
   - Açıklama: Sorunun sebebi Sven'in heyecanı ama çözüm yalnız sözlü işaretin yerine başka bir işaret koyuyor, sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0151` birebir aynı, ardından `@onarim: c368c5e67dcaae4c409a8796b8f6333e4105fcf9`, sonra gövde.

### Hikâye 4: tohum elsa-0153 (deneme 2 -> 3)

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
Ormanda hafif bir rüzgar esiyordu. Elsa ile Olaf büyük bir ağacın yanında heykel oyunu oynuyordu. Ama ikisi de ağaca dönüp saymak istedi. "Ben sayacağım!" dedi Olaf. Elsa biraz düşündü ve elini havaya kaldırdı. Elinden buz ve kar çıktı, Olaf'ın başına kar yağdı. "Kar kimin başına yağarsa, ilk o sayar," dedi Elsa. Olaf sevinçle ağaca döndü ve saydı. Elsa kollarını oynattı ve yürüdü. Olaf dönünce Elsa hareketsiz durdu. Sonra sıra Elsa'ya geldi ve o da ağaca döndü. Bu kez Olaf durmaya çalıştı ama havuç burnu kıpırdadı. İkisi de çok güldü. Elsa çok mutluydu, çünkü sırayla oynadıkları için ikisi de saymıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kar kimin başına yağarsa, ilk o sayar"
   - Cümle 7: «"Kar kimin başına yağarsa, ilk o sayar," dedi Elsa.»
   - Açıklama: Kuralı kar yağdıktan sonra koyuyor; kimin sayacağını belirleyen olay kuraldan çıkmıyor, sıra keyfi biçimde veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0153` birebir aynı, ardından `@onarim: 31785a1f68465589ef93d123a27abe8fd3240a03`, sonra gövde.

### Hikâye 5: tohum elsa-0154 (deneme 2 -> 3)

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
@plan: kar topunu aynı anda ittiler ve top ikiye ayrıldı | sırayla itmeyi söyledi ve top büyüdü
@tohum: elsa-0154
@degisim: çamur -> kar
Elsa ile Kristoff dağda, buz sarayının önünde oynuyordu. Elmalı turtayı koymak için kardan büyük bir masa yapacaklardı. Ama ikisi kar topunu aynı anda itti ve top ikiye ayrıldı. Elsa hemen yeni ve küçük bir top yaptı. Elsa kraliçeydi ama ilk sırayı Kristoff'a verdi. "Kristoff, sen on adım it, sonra ben," dedi Elsa. Kristoff topu on adım itti ve top büyüdü. Sonra Elsa itti ve top daha da büyüdü. Sırayla ittiler ve top kocaman oldu. Kristoff turtayı topun üstüne koydu. "Bak, sırayla yaptık ve masa hazır, Kristoff!" dedi Elsa.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi kar topunu aynı anda itti ve top ikiye ayrıldı"
   - Cümle 3: «Ama ikisi kar topunu aynı anda itti ve top ikiye ayrıldı.»
   - Açıklama: Topu aynı anda itmenin onu ikiye ayırması akla yatkın bir sebep değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ama ilk sırayı"
   - Cümle 5: «Elsa kraliçeydi ama ilk sırayı Kristoff'a verdi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız etiket olarak geçiyor, kartın 'özellikler' alanındaki gibi işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ama ilk sırayı Kristoff'a verdi"
   - Cümle 5: «Elsa kraliçeydi ama ilk sırayı Kristoff'a verdi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) karttaki gibi kullanılmıyor, yalnız süs olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0154` birebir aynı, `@degisim: çamur -> kar` (tutuyorsan), ardından `@onarim: 24eea51898ba9f4b3edc8b500bc8c9c06b79fb4c`, sonra gövde.

### Hikâye 6: tohum elsa-0155 (deneme 2 -> 3)

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
Bir sabah dağda ılık bir güneş vardı. Sven, Elsa'nın buz sarayına oynamaya gelmişti. Ama güneş yüzünden sarayın içi ıslak ve kaygandı. Sven içeri girince ayakları kaydı ve kendini durduramadı. Sonunda duvarın yanında yavaşça durdu. Elsa bu sarayın kraliçesiydi ve halının yerini biliyordu. Hemen köşeden uzun, yumuşak bir halı getirdi. Halıyı kapıdan salona kadar yere serdi. Sonra Sven'e elini kaldırıp halıyı gösterdi. Sven halıya dikkatle bastı. Ayakları bu kez hiç kaymadı. Sven halının üstünde rahatça yürüdü ve başını salladı. Elsa çok sevindi, çünkü Sven artık sarayda hiç kaymıyordu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güneş buzu kaygan yaptı"
   - Cümle 0 (plan satırı): «ılık güneş buzu kaygan yaptı ve geyik kaydı | yere halı serdi ve geyiğe halıyı gösterdi»
   - Açıklama: Plan satırında 'kaygan yaptı' dilbilgisel olarak doğal değil; 'kayganlaştırdı' olmalı.
   - Açıklama: Plan satırında 'kaygan yaptı' dilbilgisel açıdan kusurlu; 'buzu kaygan hale getirdi' ya da 'buzu eritti' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve halının yerini biliyordu"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve halının yerini biliyordu.»
   - Açıklama: Kraliçe özelliği karttaki 'kız kardeşini korur' biçiminde kullanılmıyor, halının yerini bilmeye bağlanıyor.
   - Açıklama: Kraliçe özelliği karttaki anlamıyla değil, halının yerini bilmek için zorlama bir gerekçe olarak kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "halının yerini biliyordu"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve halının yerini biliyordu.»
   - Açıklama: Halı daha önce kurulmadan çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0155` birebir aynı, ardından `@onarim: 6144e2b7588cd43e54f02f8b205b01d88347f476`, sonra gövde.

### Hikâye 7: tohum elsa-0157 (deneme 2 -> 3)

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
@plan: ikisi topu aynı anda itti ve top dağıldı | sırayla yuvarlamayı söyledi
@tohum: elsa-0157
@degisim: cesur -> kocaman
Bir sabah Elsa ile Kristoff limanda kardan bir dondurma yapıyordu. İkisi de kar topunu aynı anda itti. Top ikiye ayrıldı ve yere dağıldı. "Önce ben yapacağım!" dedi Kristoff. Elsa bir kraliçeydi ama önce Kristoff'un yapmasına izin verdi. "Kristoff, sen üç kez yuvarla, sonra ben," dedi Elsa. Kristoff başını salladı ve güldü. Kristoff yeni bir topu üç kez yuvarladı. Sonra sıra Elsa'ya geldi ve o da üç kez yuvarladı. İkisi sırayla topu biraz daha büyüttü. Sonunda kocaman, yuvarlak bir dondurma topu oldu. Elsa ile Kristoff yeni toplar yapmaya sırayla ve mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ama önce Kristoff'un yapmasına izin verdi"
   - Cümle 5: «Elsa bir kraliçeydi ama önce Kristoff'un yapmasına izin verdi.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki 'kız kardeşini korur' anlamıyla değil, sorunu çözmeyen bir rütbe notu olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumak olarak tanımlı, burada yalnız ad olarak anılıyor ve işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0157` birebir aynı, `@degisim: cesur -> kocaman` (tutuyorsan), ardından `@onarim: aec98abf0d252d1c81ac9aa7be1df9d6defcb314`, sonra gövde.

### Hikâye 8: tohum elsa-0158 (deneme 2 -> 3)

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
@plan: rüzgar masadaki örtüyü havaya kaldırdı | kardan adama örtüyü tutturdu ve üstüne terazi koydu
@tohum: elsa-0158
Elsa limanda Olaf ile ilk kar için neşeli bir şenlik hazırlıyordu. Olaf, limandaki büyük terazinin yanındaki masaya beyaz bir örtü serdi. Ama rüzgar esti ve örtü havaya kalktı. Kurabiye tabakları masada duramadı. "Olaf, sen örtüyü sıkıca tut," dedi Elsa. Olaf, kraliçesi Elsa'nın sözünü dinledi ve örtüyü iki eliyle tuttu. Elsa ağır teraziyi getirdi ve örtünün ortasına koydu. Örtü artık rüzgarda kalkmadı. İkisi kurabiyeleri masada güzelce düzenledi. "Bu şenlik harika olacak!" dedi Olaf. Sonra Elsa ile Olaf şenliğe mutlu mutlu başladı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'nın sözünü dinledi"
   - Cümle 6: «Olaf, kraliçesi Elsa'nın sözünü dinledi ve örtüyü iki eliyle tuttu.»
   - Açıklama: 'Sözünü dinlemek' deyimsel anlatım küçük çocuğa uygun değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kraliçesi Elsa'nın sözünü dinledi"
   - Cümle 6: «Olaf, kraliçesi Elsa'nın sözünü dinledi ve örtüyü iki eliyle tuttu.»
   - Açıklama: Önceden tanıtılmış Elsa yeniden unvanıyla tanıtılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Olaf, kraliçesi Elsa'nın sözünü"
   - Cümle 6: «Olaf, kraliçesi Elsa'nın sözünü dinledi ve örtüyü iki eliyle tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa 'kraliçesi' diye yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçesi Elsa'nın sözünü dinledi"
   - Cümle 6: «Olaf, kraliçesi Elsa'nın sözünü dinledi ve örtüyü iki eliyle tuttu.»
   - Açıklama: Kartın özellik alanındaki kraliçelik (kız kardeşini korur) çözüme katkı sağlamıyor; sorun terazi ile çözülüyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0158` birebir aynı, ardından `@onarim: 7890b6744a780013824205cf6afb261d0abd460f`, sonra gövde.

### Hikâye 9: tohum elsa-0159 (deneme 2 -> 3)

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
Bir sabah dağa sulu kar yağıyordu. Elsa buz sarayının kraliçesiydi ve kapısına yeni bir süs asmak istiyordu. Ama rüzgar esti, süs elinden uçtu ve kayboldu. Elsa kapının önündeki kara eğildi ve baktı. Sulu karın içinde yalnız küçük taşlar vardı. Sonra kapının iki yanına da baktı. Süsü hiçbir yerde göremedi. Elsa kendi üstüne de bakmak için parlak buz duvarına yaklaştı. Duvarda saçına takılmış süsü gördü. Süsün saçında olması Elsa'yı çok güldürdü. Süsü saçından çıkardı ve kapıya astı. Elsa çok sevindi, çünkü süsünü hiç uzağa gitmeden bulmuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa buz sarayının kraliçesiydi"
   - Cümle 2: «Elsa buz sarayının kraliçesiydi ve kapısına yeni bir süs asmak istiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği süs olarak geçiyor ve çözümde işe yaramıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kapının iki yanına da baktı"
   - Cümle 6: «Sonra kapının iki yanına da baktı.»
   - Açıklama: Elsa önce kara, sonra kapının yanlarına, en son duvara bakıyor; çözüm iki adımı aşıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Duvarda saçına takılmış süsü gördü"
   - Cümle 9: «Duvarda saçına takılmış süsü gördü.»
   - Açıklama: Süs duvarda değil, Elsa duvardaki yansımasında görüyor; 'Duvarda' yanlış anlam veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0159` birebir aynı, ardından `@onarim: 75b95bcd2a82a444162248d88d0e29f772dbd939`, sonra gövde.

### Hikâye 10: tohum elsa-0160 (deneme 2 -> 3)

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
@plan: kardeşi dalların altındaydı ve başına kar döküldü | kardeşini dalların altından uzağa götürdü
@tohum: elsa-0160
Rüzgar dağda hafifçe esiyordu. Kraliçe Elsa ile kardeşi Anna güzel bir meşe ağacına kar topu atıyordu. Ama Anna dalların altındaydı ve kar hep başına döküldü. Anna kızdı ve topları çok hızlı atmaya başladı. Saçları karla doldu. Elsa kardeşinin başından karı eliyle temizledi. Sonra onu elinden tuttu ve dalların altından uzağa götürdü. "Anna, buradan at, kar artık başına düşmez," dedi Elsa. Anna sakinleşti ve topu yavaşça attı. Top tam ağaca çarptı ve kar bu kez yere döküldü. "Başardım, Elsa!" dedi Anna. Anna sevinçle zıpladı ve Elsa'ya sarıldı. Elsa çok sevindi, çünkü kardeşini dökülen kardan korumuştu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kar hep başına döküldü"
   - Cümle 3: «Ama Anna dalların altındaydı ve kar hep başına döküldü.»
   - Açıklama: 'hep' süreklilik bildirir, fiil 'dökülüyordu' olmalı; görünüş uyumu bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0160` birebir aynı, ardından `@onarim: 931315927f67bf9de9287bf3111d43511ab80b0d`, sonra gövde.

### Hikâye 11: tohum elsa-0161 (deneme 2 -> 3)

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
Bir sabah Kraliçe Elsa sarayın önünde mavi bir uçurtma uçuruyordu. Sven de onu izliyordu. Birden rüzgar durdu ve uçurtmanın ipi Sven'in ayaklarına dolandı. Sven ayaklarını salladı ama ipi çıkaramadı. Sonra döndü ve gürültülü sesler çıkardı. İp daha çok dolandı. "Sven, dur ve hiç kıpırdama!" dedi Elsa yüksek sesle. Sven hemen durdu. Elsa yanına eğildi ve ipi yavaşça çözdü. Sonra uçurtmayı dikkatle yere koydu. Sven sevinçle burnunu Elsa'nın eline sürttü. Elsa çok mutlu oldu, çünkü Sven'e yardım etmişti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayın önünde mavi bir uçurtma uçuruyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Kartın özellikler alanındaki kraliçelik yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0161` birebir aynı, ardından `@onarim: f5b1d97d9914c804a5a20e70927031022ac4f3b5`, sonra gövde.

### Hikâye 12: tohum elsa-0162 (deneme 2 -> 3)

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
Elsa limanda ilk kez çember çevirmeyi deniyordu. Ama deniz o sabah çok dalgalıydı. Dalgalar kıyıya vurdu ve taşları ıslattı. Çember ıslak taşların üstünde kaydı ve düştü. Elsa çemberi ve taşları dikkatle inceledi. Taşlar yalnız kıyıya yakın yerde ıslaktı. Elsa kraliçe olduğu için limanı çok iyi tanıyordu. Kıyıdan uzakta kuru bir meydan olduğunu biliyordu. Hemen o kuru meydana geçti. Orada çemberi yeniden yuvarladı. Bu kez çember kaymadı ve uzun süre döndü. Sonra Elsa meydanda çemberiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hemen o kuru meydana geçti"
   - Cümle 9: «Hemen o kuru meydana geçti.»
   - Açıklama: Hikaye deniz kıyısında başlıyor ama kıyıdan uzak bir meydanda bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0162` birebir aynı, ardından `@onarim: 30809a28203d43f922dedd55a8c08b4d20c07e94`, sonra gövde.
