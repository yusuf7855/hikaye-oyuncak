# Editör görevi (onarım): Doru, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0003 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0003
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'yosun', fiil 'ayrılmak', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: ağacın altı taşlı ve sertti | kayanın dibinden yosun getirip yumuşak bir yatak yaptı
@tohum: doru-0003
@degisim: kibar -> yumuşak
Parkta büyük bir ağaç vardı. Doru bu ağacın gölgesinde dinlenmek istedi. Ama ağacın altı taşlı ve sertti. Doru orada yumuşak bir yatak yapmaya karar verdi. Parkın ucundaki büyük kayanın dibinde yeşil yosunlar vardı. Doru daha önce hiç yatak yapmamıştı ama cesaretle denedi. Yosunları dişleriyle tuttu ve çekti. Yosunlar taştan kolayca ayrıldı. Doru yosunları ağacın altına taşıdı ve taşların üstüne serdi. Ağacın altı yumuşacık oldu. Doru yeni yatağına uzandı ve gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta büyük bir ağaç vardı"
   - Cümle 1: «Parkta büyük bir ağaç vardı.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; metin çayır yerine taşlı, kayalı bir park anlatıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kayanın dibinde yeşil yosunlar vardı"
   - Cümle 5: «Parkın ucundaki büyük kayanın dibinde yeşil yosunlar vardı.»
   - Açıklama: Yosunlar Doru aramadan, çözümü getirmek için sebepsizce beliriyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hiç yatak yapmamıştı ama cesaretle denedi"
   - Cümle 6: «Doru daha önce hiç yatak yapmamıştı ama cesaretle denedi.»
   - Açıklama: Kartın özellikler alanındaki cesaret, yosundan yatak yapmak gibi cesaret gerektirmeyen bir işe zorla eklenmiş ve işe yarar biçimde kullanılmamış.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru daha önce hiç yatak yapmamıştı ama cesaretle denedi"
   - Cümle 6: «Doru daha önce hiç yatak yapmamıştı ama cesaretle denedi.»
   - Açıklama: Tohumdaki cesaret özelliği işe yaramadan, yatak yapmaya zorla eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0003` birebir aynı, `@degisim: kibar -> yumuşak` (tutuyorsan), ardından `@onarim: ae2fb4980310bae5f6f375455d3163dfbd604d80`, sonra gövde.

### Hikâye 2: tohum doru-0004 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0004
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'patlıcan', fiil 'üzülmek', sıfat 'berrak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yağmurdan sonra gölün suyu çamurlu olmuştu | su sesine doğru hızla koşup temiz bir dere buldu
@tohum: doru-0004
@degisim: patlıcan -> su
Bir sabah Doru ile Kırat ormanda su içmeye geldi. Ama yağmurdan sonra küçük gölün suyu çamurlu olmuştu. Kırat çok susamıştı ama bu suyu içemedi ve üzüldü. Doru, Kırat için temiz su bulmaya karar verdi. Uzaktan hafif bir su sesi geliyordu. Ormanın içinden o sese doğru geniş ve düz bir yol gidiyordu. Kırat gölün yanında bekledi. Doru bu yolda hızla koştu ve kısa sürede küçük bir dere buldu. Derenin suyu berraktı, dipteki taşlar görünüyordu. Doru hemen geri döndü ve Kırat'ı dereye götürdü. Kırat dereden bol bol içti. Sonra başını sevgiyle Doru'ya sürttü. Doru çok sevindi, çünkü Kırat artık temiz su içebiliyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Derenin suyu berraktı"
   - Cümle 9: «Derenin suyu berraktı, dipteki taşlar görünüyordu.»
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'temiz' ya da 'duru' daha uygun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0004` birebir aynı, `@degisim: patlıcan -> su` (tutuyorsan), ardından `@onarim: d3366b9bc177166dc3e91669c33ec0ec1a2adb20`, sonra gövde.

### Hikâye 3: tohum doru-0006 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0006
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'iplik', fiil 'eşleştirmek', sıfat 'yalnız'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: uzun yoldan gelen at çok acıkmıştı | dört elmanın yarısını ona verdi
@tohum: doru-0006
@degisim: iplik -> elma
Bir sabah Doru dağda küçük bir elma ağacı buldu. Ağacın altında yalnız dört elma vardı, ikisi kırmızı ve ikisi yeşildi. Yanındaki Kırat uzun bir yoldan gelmişti ve çok acıkmıştı. Doru, Kırat'a yardım etmek ve elmaları paylaşmak istedi. Doru her kırmızı elmayı bir yeşil elmayla eşleştirdi. Bir kırmızı ve bir yeşil elmayı ağzıyla Kırat'a uzattı. "Bu iki elma senin, Kırat," dedi Doru. "Teşekkür ederim, Doru, gel birlikte yiyelim," dedi Kırat. Doru kalan iki elmayı da aldı. İkisi yan yana durdu ve elmalarını yedi. Elmalar çok tatlıydı. Doru çok mutlu oldu, çünkü elmalarını paylaşınca Kırat da doymuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir yeşil elmayla eşleştirdi"
   - Cümle 5: «Doru her kırmızı elmayı bir yeşil elmayla eşleştirdi.»
   - Açıklama: 'Eşleştirdi' 3 yaşındaki çocuk için soyut ve bilinmeyen bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru her kırmızı elmayı bir yeşil elmayla eşleştirdi"
   - Cümle 5: «Doru her kırmızı elmayı bir yeşil elmayla eşleştirdi.»
   - Açıklama: Kırmızı-yeşil eşleştirme açlık sorununa hiçbir katkı yapmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0006` birebir aynı, `@degisim: iplik -> elma` (tutuyorsan), ardından `@onarim: 0fa6da4c0a6b94aab10787f77e4be07e9d4d965b`, sonra gövde.

### Hikâye 4: tohum doru-0011 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0011
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'yumurta', fiil 'savurmak', sıfat 'yardımsever'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: oyunun beyaz taşı otlara doğru yuvarlandı | hızla koşup taşı otlara girmeden durdurdu
@tohum: doru-0011
@degisim: yardımsever -> beyaz
Parkta güneş parlıyordu. Doru ile Karatay beyaz ve yuvarlak bir taşa yumurta diyerek oynuyordu. Karatay sevinçle ön ayağını savurdu ve taşı yanlışlıkla uzun otlara doğru itti. "Yumurta otların arasında kaybolacak!" dedi Karatay telaşla. "Korkma, ben yakalarım," dedi Doru. Park geniş ve düzdü. Doru hızla koştu ve yuvarlanan taşı otlara girmeden önce durdurdu. Sonra taşı burnuyla yavaşça itip Karatay'a geri getirdi. "Teşekkürler, Doru, yumurta kaybolmadı!" dedi Karatay. Doru çok sevindi, çünkü beyaz yumurtayı zamanında yakalamıştı.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta güneş parlıyordu"
   - Cümle 1: «Parkta güneş parlıyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır ve dizide park yoktur; metin yeri çayır yerine park olarak sunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0011` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 4cd9273b608bbf031c219c0e5306da4433f49da1`, sonra gövde.

### Hikâye 5: tohum doru-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0012
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yiyecek', fiil 'taramak', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük olan sırası gelince yaprağa uzanamadı | dalı dişleriyle eğdi ve ona sırasını verdi
@tohum: doru-0012
@degisim: taramak -> uzanmak
Doru ile Alaca çayırda sırayla yaprak koparıyordu. Ağacın esnek bir dalında yeşil yapraklar vardı. Ama Alaca çok küçüktü ve sırası gelince dala uzanamadı. "Ben hiç yaprak koparamıyorum, Doru," dedi Alaca. Alaca'nın gözleri doldu. Doru ona hemen yardım etmek istedi. Dala baktı ve biraz düşündü. Sonra dişleriyle dalın ucunu tuttu ve yavaşça aşağı çekti. Dal kolayca eğildi ve yapraklar Alaca'nın önüne geldi. "Sıra sende, Alaca," dedi Doru. Alaca bir yaprak kopardı ve keyifle yedi. "Bu, en tatlı yiyecek!" dedi Alaca. Doru çok sevindi, çünkü artık ikisi de sırayla oynayabiliyordu.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Alaca çayırda sırayla yaprak koparıyordu"
   - Cümle 1: «Doru ile Alaca çayırda sırayla yaprak koparıyordu.»
   - Açıklama: Başlıktaki yer park iken hikaye çayırda geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Alaca'nın gözleri doldu"
   - Cümle 5: «Alaca'nın gözleri doldu.»
   - Açıklama: 'Gözleri doldu' mecazlı bir anlatım; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Gözleri doldu' deyimdir; 3 yaşındaki çocuk için somut değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ikisi de sırayla oynayabiliyordu"
   - Cümle 13: «Doru çok sevindi, çünkü artık ikisi de sırayla oynayabiliyordu.»
   - Açıklama: İkisi yaprak koparıp yiyordu; 'oynamak' fiili olaya uymuyor.
   - Açıklama: Hikayede oyun değil yaprak koparma var; 'oynayabiliyordu' yerine 'yaprak koparabiliyordu' uygun olur.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0012` birebir aynı, `@degisim: taramak -> uzanmak` (tutuyorsan), ardından `@onarim: 1a90a33c59ba0bc33a7301a935a706ccbf4d3fec`, sonra gövde.

### Hikâye 6: tohum doru-0014 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0014
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'topaç', fiil 'yetiştirmek', sıfat 'masmavi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: vadide topaç gibi dönen masmavi bir şey gördüler | hızla koşup ona yetişti ve tüy olduğunu gördü
@tohum: doru-0014
@degisim: yetiştirmek -> yetişmek
Dağda serin bir rüzgar esiyordu. Doru ile Karatay yukarıdan vadiye bakıyordu. Birden aşağıda, çimenlerin üstünde masmavi bir şey topaç gibi döndü. "Bu ne, Doru?" diye sordu Karatay. "Bilmiyorum, ama hemen bulalım!" dedi Doru. İkisi yavaşça aşağı indi. Rüzgar o şeyi vadinin öbür ucuna doğru götürüyordu. Vadi açık ve düzdü. Doru orada hızla koştu ve ona yetişti. Rüzgar durunca o şey Doru'nun önüne düştü. Bu, uzun ve yumuşak bir tüydü! Karatay da koşarak geldi ve tüye baktı. "Ne güzel bir tüy!" dedi Karatay. Doru çok sevindi, çünkü dönen şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "hızla koşup ona yetişti ve tüy olduğunu gördü"
   - Cümle 0 (plan satırı): «vadide topaç gibi dönen masmavi bir şey gördüler | hızla koşup ona yetişti ve tüy olduğunu gördü»
   - Açıklama: Plan figürün koşup yetiştiğini söylüyor ama gövdede Karatay koşuyor ve tüy rüzgar durunca düşüyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "masmavi bir şey topaç gibi döndü"
   - Cümle 3: «Birden aşağıda, çimenlerin üstünde masmavi bir şey topaç gibi döndü.»
   - Açıklama: Sorun gerçek bir sorun değil, yalnız bir merak; çözülmesi gereken bir güçlük kurulmuyor.
   - Açıklama: Sorun yalnız merak edilen bir görüntü ve bir tüyün çimenlerde topaç gibi dönmesi akla yatkın değil.
   - Açıklama: Dönen bir şeyi görmek gerçek bir sorun değil, sebebi de sorun olarak kurulmuyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "İkisi yavaşça aşağı indi"
   - Cümle 6: «İkisi yavaşça aşağı indi.»
   - Açıklama: Hikaye dağın tepesinde başlıyor ve vadiye inerek başka bir sahneye geçiyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "hızla koştu ve ona yetişti"
   - Cümle 9: «Doru orada hızla koştu ve ona yetişti.»
   - Açıklama: Araya 'Vadi' cümlesi girdiği için 'ona' zamirinin mavi şeyi gösterdiği belirsiz.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar durunca o şey Doru'nun önüne düştü"
   - Cümle 10: «Rüzgar durunca o şey Doru'nun önüne düştü.»
   - Açıklama: Çözüm figürün eyleminden değil rüzgarın sebepsizce durmasından geliyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Karatay da koşarak geldi ve tüye baktı"
   - Cümle 12: «Karatay da koşarak geldi ve tüye baktı.»
   - Açıklama: Karatay zaten koşup şeye yetişmişken sonradan koşarak geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0014` birebir aynı, `@degisim: yetiştirmek -> yetişmek` (tutuyorsan), ardından `@onarim: 93f4378c565ec6dd6bbbfeee5c091f3ed6eea801`, sonra gövde.

### Hikâye 7: tohum doru-0015 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0015
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'domates', fiil 'katılmak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: çalıların arkasından garip bir ses geldi | cesaretle çalılardan geçti ve taşa düşen damlaları buldu
@tohum: doru-0015
@degisim: domates -> damla
Doru yağmurdan sonra ormanın kenarında otluyordu. Birden sık çalıların arkasından tık tık diye bir ses geldi. Doru bu sesin ne olduğunu çok merak etti. Ama çalılar çok sıktı ve arkası görünmüyordu. Doru cesaretle başını çalıların arasına uzattı. Sonra yavaşça öbür tarafa geçti. Orada büyük bir taş vardı. Taşın üstündeki ağaçtan su damlaları düşüyordu. Her damla taşa değince tık diye ses çıkıyordu. Doru sesin nereden geldiğini bulmuştu. Taşın yanında yumuşacık yeşil yosunlar vardı. Doru yosunların üstüne uzandı ve sesi dinledi. Sonra damlaların şarkısına neşeyle başını sallayarak katıldı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çalıların arkasından tık tık diye bir ses geldi"
   - Cümle 2: «Birden sık çalıların arkasından tık tık diye bir ses geldi.»
   - Açıklama: Merak edilen bir ses gerçek bir sorun değil; ortada çözülmesi gereken bir dert yok.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Taşın üstündeki ağaçtan su"
   - Cümle 8: «Taşın üstündeki ağaçtan su damlaları düşüyordu.»
   - Açıklama: 'Taşın üstündeki ağaç' ağacın taşın üzerinde durduğunu söylüyor; 'taşın üstündeki dallardan' kastediliyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Taşın üstündeki ağaçtan"
   - Cümle 8: «Taşın üstündeki ağaçtan su damlaları düşüyordu.»
   - Açıklama: Ağaç taşın üstünde durmaz; 'taşın yanındaki ağaçtan' ya da 'taşın üstüne ağaçtan' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra damlaların şarkısına neşeyle"
   - Cümle 13: «Sonra damlaların şarkısına neşeyle başını sallayarak katıldı.»
   - Açıklama: Damlalar şarkı söylemez; mecaz 3 yaşındaki çocuğa uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "damlaların şarkısına neşeyle"
   - Cümle 13: «Sonra damlaların şarkısına neşeyle başını sallayarak katıldı.»
   - Açıklama: Damlaların şarkısı mecazdır, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0015` birebir aynı, `@degisim: domates -> damla` (tutuyorsan), ardından `@onarim: b79032634476be7e81dd3efc31f5801ae7a0806f`, sonra gövde.

### Hikâye 8: tohum doru-0019 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0019
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çöp', fiil 'aşmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar oyundaki yaprağı tepenin arkasına uçurdu | tepeyi aştı ve düz vadide hızla koşup yaprağa yetişti
@tohum: doru-0019
@degisim: çöp -> yaprak
Rüzgar dağda hafif hafif esiyordu. Doru, büyük sarı bir yaprakla oyun oynuyordu. Ama birden rüzgar sert esti ve yaprak küçük bir tepenin arkasına uçtu. Doru yaprağı artık göremiyordu. Yavaş yavaş yürüdü ve tepeyi aştı. Aşağıda geniş ve düz bir vadi vardı. Rüzgar sarı yaprağı vadinin içinde ileri doğru götürüyordu. Doru düz çimenlerde hızla koştu ve yaprağa yetişti. Ayağını yavaşça yaprağın ucuna koydu. Yaprak artık uçmuyordu. Sonra Doru yaprağı dişleriyle tuttu ve havaya attı. Doru çok sevindi, çünkü güzel oyununa yeniden başlamıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar sert esti ve yaprak küçük bir tepenin arkasına uçtu"
   - Cümle 3: «Ama birden rüzgar sert esti ve yaprak küçük bir tepenin arkasına uçtu.»
   - Açıklama: Rüzgarın sıradan bir yaprağı uçurması önemsiz bir sorun; dağda başka yaprak da bulunabilirdi.
   - Açıklama: Rüzgarın oyun yaprağını uçurması ve kovalanıp geri alınması önemsiz bir sorun; M3 örneğine çok yakın.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0019` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: c5ca8aba14642020b70915cc9459e2756bc96356`, sonra gövde.

### Hikâye 9: tohum doru-0020 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0020
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'toz', fiil 'eğlendirmek', sıfat 'lezzetli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: rüzgar çimenleri tozla kapladı ve annesi yiyemedi | onu derenin kenarındaki temiz çimenlere götürdü
@tohum: doru-0020
Bir sabah Doru ile annesi çayırda çimen yiyordu. Birden rüzgar esti ve çimenlerin üstünü kalın bir toz kapladı. Annesi çok açtı ama tozlu çimenleri yiyemiyordu. "Doru, bu çimenler yenmez," dedi annesi. Doru etrafına baktı ve biraz ileride küçük bir dere gördü. Derenin kenarındaki çimenler yeşil ve temizdi. Doru, annesine yardım etmek için onu oraya götürdü. Yolda komik komik zıpladı ve annesini eğlendirdi. Annesi güldü ve temiz çimenleri yedi. "Bunlar çok lezzetli, Doru!" dedi annesi. Doru bundan sonra rüzgarlı bir günde temiz çimenleri derenin kenarında aradı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile annesi çayırda çimen yiyordu"
   - Cümle 1: «Bir sabah Doru ile annesi çayırda çimen yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yolda komik komik zıpladı ve annesini eğlendirdi"
   - Cümle 8: «Yolda komik komik zıpladı ve annesini eğlendirdi.»
   - Açıklama: Zıplama ayrıntısı olaya hiçbir şey katmıyor, işlevsiz.
   - Açıklama: Zıplama ayrıntısı sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "rüzgarlı bir günde temiz"
   - Cümle 11: «Doru bundan sonra rüzgarlı bir günde temiz çimenleri derenin kenarında aradı.»
   - Açıklama: 'Bundan sonra' ile tekil 'bir günde' uyumsuz; 'rüzgarlı günlerde' olmalı.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru bundan sonra rüzgarlı bir günde"
   - Cümle 11: «Doru bundan sonra rüzgarlı bir günde temiz çimenleri derenin kenarında aradı.»
   - Açıklama: 'Bundan sonra' ile tekil 'bir günde' ve '-dı' uyumsuz; 'rüzgarlı günlerde ... arardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0020` birebir aynı, ardından `@onarim: 4bec7f0cd98502ee56598e1abb63e4dccf85029a`, sonra gövde.

### Hikâye 10: tohum doru-0021 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0021
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'balon', fiil 'içmek', sıfat 'hafif'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: dere kurumuştu ve içecek su yoktu | suyun yerini sordu ve pınarın üstündeki yaprakları itti
@tohum: doru-0021
@degisim: balon -> su
Bir sabah Doru ormanda Kırat ile yürüyordu. Hava sıcaktı ve Doru çok susamıştı. Ama ormandaki küçük dere kurumuştu ve içinde hiç su yoktu. "Kırat, burada içecek suyu nerede bulurum?" diye sordu Doru. Kırat biraz düşündü. "Büyük meşe ağacının dibinde bir kaynak var," dedi Kırat. İkisi meşe ağacına yürüdü. Kaynağın üstünü hafif, kuru yapraklar kapatmıştı. Doru, Kırat'a yardım etmek için yaprakları burnuyla kenara itti. Serin ve temiz su hemen göründü. Önce Kırat, sonra Doru bu sudan içti. Sonra ikisi ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kaynak var," dedi Kırat"
   - Cümle 6: «"Büyük meşe ağacının dibinde bir kaynak var," dedi Kırat.»
   - Açıklama: 'Kaynak' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru, Kırat'a yardım etmek için yaprakları"
   - Cümle 9: «Doru, Kırat'a yardım etmek için yaprakları burnuyla kenara itti.»
   - Açıklama: Kartın özellikler alanındaki yardım işe yarar biçimde kullanılmamış, çünkü suya ihtiyacı olan Doru'nun kendisidir ve Kırat'a yardım söylemi zorlamadır.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru, Kırat'a yardım etmek için yaprakları burnuyla kenara itti"
   - Cümle 9: «Doru, Kırat'a yardım etmek için yaprakları burnuyla kenara itti.»
   - Açıklama: Susayan ve su arayan Doru iken yaprakları Kırat'a yardım etmek için ittiği söyleniyor.
   - Açıklama: Susayan ve sorunu olan Doru iken yaprakları Kırat'a yardım etmek için ittiği söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0021` birebir aynı, `@degisim: balon -> su` (tutuyorsan), ardından `@onarim: fedfddd727f0ff68919007724a5ceb52688b3855`, sonra gövde.
