# Editör görevi (onarım): Doru, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Doru | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar12.txt --ad urun_v2`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Onarılacak hikâyeler

### Hikâye 1: tohum doru-0048 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0048
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'köpük', fiil 'ıslatmak', sıfat 'komik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: ormanın içinden şırıl şırıl bir ses geldi | hızla koşup sesi yapan dereyi buldu
@tohum: doru-0048
Doru ormanda serin gölgede yürüyordu. Birden uzaktan şırıl şırıl bir ses geldi. Doru bu sesin ne olduğunu çok merak etti. Ağaçların arasında geniş ve düz bir açıklık vardı. Doru açıklıkta hızla koştu ve sesin geldiği yere vardı. Orada küçük bir dere taşların üstünden akıyordu. Su taşlara çarpınca beyaz köpükler oluyordu. Doru köpükleri koklamak için başını eğdi. Birden su sıçradı ve Doru'nun burnunu ıslattı. Burnunun ucunda beyaz bir köpük kaldı. Doru başını salladı ve komik köpük havaya uçtu. Sonra Doru dereden serin su içti ve kenarda mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "uzaktan şırıl şırıl bir ses geldi"
   - Cümle 2: «Birden uzaktan şırıl şırıl bir ses geldi.»
   - Açıklama: Uzaktan gelen bir su sesi gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir sorun kurulmuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru köpükleri koklamak için başını eğdi"
   - Cümle 8: «Doru köpükleri koklamak için başını eğdi.»
   - Açıklama: Köpük ve burun ıslanması olayı sorunla ilgisiz, işlevsiz bir ek olay.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden su sıçradı ve Doru'nun burnunu ıslattı"
   - Cümle 9: «Birden su sıçradı ve Doru'nun burnunu ıslattı.»
   - Açıklama: Köpük ve burnun ıslanması olayı çözümden sonra sebepsiz ekleniyor ve hikayede hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0048` birebir aynı, ardından `@onarim: e2ea1211ce0ffdefc43bb0ce2602bd8686e578ef`, sonra gövde.

### Hikâye 2: tohum doru-0049 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0049
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'iz', fiil 'solmak', sıfat 'enerjik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: çimenlerin arasında ince ve ıslak bir iz vardı | izin sonunu buldu ve taşı itip suyu açtı
@tohum: doru-0049
Bir sabah Doru çok enerjikti ve çayırda zıplaya zıplaya dolaşıyordu. Birden çimenlerin arasında ince ve ıslak bir iz gördü. Doru bu izin nereye gittiğini çok merak etti. İzin yanından yavaşça yürüdü. İz, küçük bir kaynaktan gelen ince bir suydu. Su büyük bir taşın önünde birikmişti. Taş suyun yolunu kapatmıştı. Taşın arkasında toprak kuruydu ve küçük çiçekler solmuştu. Doru çiçeklere yardım etmek istedi. Ayağıyla taşı itti ve kenara çekti. Su hemen kuru toprağa aktı ve çiçeklerin dibini ıslattı. Doru çok sevindi ve çayırda koşup oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "taşı itip suyu açtı"
   - Cümle 0 (plan satırı): «çimenlerin arasında ince ve ıslak bir iz vardı | izin sonunu buldu ve taşı itip suyu açtı»
   - Açıklama: 'Suyu açmak' musluk için kullanılır; burada 'suyun yolunu açtı' olmalı.
   - Açıklama: Plan satırında 'suyu açtı' musluk açmak anlamındadır; taşı itmekle suyun yolu açılır.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çimenlerin arasında ince ve ıslak bir iz vardı"
   - Cümle 0 (plan satırı): «çimenlerin arasında ince ve ıslak bir iz vardı | izin sonunu buldu ve taşı itip suyu açtı»
   - Açıklama: Plan sorunu bir iz olarak veriyor ama asıl sorun taşın suyu kesmesi ve çiçeklerin solması.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "çayırda zıplaya zıplaya dolaşıyordu"
   - Cümle 1: «Bir sabah Doru çok enerjikti ve çayırda zıplaya zıplaya dolaşıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor ve park hiç anılmıyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor ve park hiç kurulmuyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "İz, küçük bir kaynaktan gelen ince bir suydu"
   - Cümle 5: «İz, küçük bir kaynaktan gelen ince bir suydu.»
   - Açıklama: İz su olamaz; 'iz' kelimesi yanlış anlamda kullanılmış.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "küçük çiçekler solmuştu"
   - Cümle 8: «Taşın arkasında toprak kuruydu ve küçük çiçekler solmuştu.»
   - Açıklama: Asıl sorun olan solan çiçekler ancak 8. cümlede söyleniyor; ilk üç cümlede yalnız merak uyandıran bir iz var.
6. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Taşın arkasında toprak kuruydu ve küçük çiçekler solmuştu"
   - Cümle 8: «Taşın arkasında toprak kuruydu ve küçük çiçekler solmuştu.»
   - Açıklama: Asıl sorun olan solan çiçekler ancak 8. cümlede söyleniyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ayağıyla taşı itti ve kenara çekti."
   - Cümle 10: «Ayağıyla taşı itti ve kenara çekti.»
   - Açıklama: Taşı iten Doru'nun aynı anda onu çekmesi çelişkili; fiil yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0049` birebir aynı, ardından `@onarim: 5719c954b93c96b9d72c8618dcc7f50db0108f37`, sonra gövde.

### Hikâye 3: tohum doru-0050 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0050
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'şemsiye', fiil 'üflemek', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: en güzel otlar ağır bir dalın altında kalmıştı | arkadaşıyla dalı çekti ve yığını yaptı
@tohum: doru-0050
@degisim: şemsiye -> ot
Geniş çayırda güneş parlıyordu. Doru ile Karatay öğle yemeği için büyük bir ot yığını yapıyordu. Ama en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı. Karatay dalı tek başına çekemedi. Doru hemen arkadaşına yardım etti. İkisi dalı dişleriyle tuttu ve birlikte kenara çekti. Doru otların üstüne burnuyla üfledi ve kuru yapraklar havaya uçtu. Karatay buna çok güldü. Sonra ikisi otları kopardı ve yığına taşıdı. Yığın kocaman oldu ve nefis kokuyordu. Doru ile Karatay ot yığınının yanında mutlu mutlu yemek yedi.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Geniş çayırda güneş parlıyordu"
   - Cümle 1: «Geniş çayırda güneş parlıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda başlıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Doru hemen arkadaşına yardım etti"
   - Cümle 5: «Doru hemen arkadaşına yardım etti.»
   - Açıklama: Dalı çekme işini Karatay başlatıyor, figür Doru ise yalnız yardım eden konumunda kalıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru otların üstüne burnuyla üfledi"
   - Cümle 7: «Doru otların üstüne burnuyla üfledi ve kuru yapraklar havaya uçtu.»
   - Açıklama: Yaprakları üfleme ayrıntısı olayda hiçbir işe yaramıyor.
   - Açıklama: Yaprakların uçması ve Karatay'ın gülmesi olaya hiçbir katkı yapmayan işlevsiz ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0050` birebir aynı, `@degisim: şemsiye -> ot` (tutuyorsan), ardından `@onarim: 8e567223ef08b65556dcc988053474b471df1aca`, sonra gövde.

### Hikâye 4: tohum doru-0051 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0051
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kök', fiil 'rahatlamak', sıfat 'meşgul'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: yolun ortasında uzun ve kara bir şey duruyordu | cesaretle yaklaştı ve onun bir kök olduğunu gördü
@tohum: doru-0051
Ormanda hafif bir rüzgar esiyordu. Doru keşif oyunu oynuyordu ve büyük meşe ağacına gidiyordu. Ama yolun ortasında uzun, kıvrımlı ve kara bir şey duruyordu. Doru onun ne olduğunu bilmiyordu. "Anne, yolda ne var?" diye sordu Doru. Annesi çimen yemekle meşguldü. "Git bak, ben buradayım," dedi annesi. Doru cesaretle kara şeye yaklaştı ve onun bir ağaç kökü olduğunu gördü. Doru rahatladı ve güldü. Kökün üstünden hopladı ve ağaca ulaştı. "Anne, ağaca vardım!" dedi Doru. Annesi gülümsedi ve Doru keşif oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Annesi çimen yemekle meşguldü."
   - Cümle 6: «Annesi çimen yemekle meşguldü.»
   - Açıklama: 'Meşgul' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Git bak, ben buradayım"
   - Cümle 7: «"Git bak, ben buradayım," dedi annesi.»
   - Açıklama: Anne, yanına gelmeden yavruyu yoldaki kıvrımlı, kara ve bilinmeyen bir şeye tek başına yolluyor; çocuk bilinmeyen bir şeye yaklaşmayı taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0051` birebir aynı, ardından `@onarim: 2c57002bb307b5bf1029c55b5a9d911ea75ee236`, sonra gövde.

### Hikâye 5: tohum doru-0052 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0052
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kozalak', fiil 'dinlemek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük arkadaşı kayanın arkasındaki kozalakları göremedi | onu düz bir yere götürdü ve kozalakları gösterdi
@tohum: doru-0052
Bir sabah dağ çok sessizdi. Doru ile Alaca büyük bir kayanın yanında dinleniyordu. Birden aşağıdan sesler geldi ama küçük Alaca kayanın arkasını göremedi. Doru sesi dikkatle dinledi ve kayanın üstünden baktı. Çam ağaçlarından düşen kozalaklar aşağı yuvarlanıyordu. Doru küçük arkadaşına yardım etti. Onu kayanın yanındaki düz bir yere götürdü. Oradan her yer iyi görünüyordu. Bir kozalak daha tık tık zıplayarak yuvarlandı. Alaca heyecanla kozalakları tek tek saydı. Doru çok sevindi, çünkü Alaca da kozalakları sonunda görmüştü.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Onu kayanın yanındaki düz bir yere götürdü"
   - Cümle 7: «Onu kayanın yanındaki düz bir yere götürdü.»
   - Açıklama: Alaca küçük olduğu için kayanın arkasını göremiyor; kayanın yanındaki düz bir yerin bu sebebi neden çözdüğü belli değil.
   - Açıklama: Sorun kayanın görüşü kapatması iken düz bir yere gitmek görüşü açacak bir çözüm değil, sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0052` birebir aynı, ardından `@onarim: 56cca6292041d0ba3769602c9e7d424cd693aa57`, sonra gövde.
