# Editör görevi (onarım): Doru, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0151
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'basamak', fiil 'tutunmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: yağmur başladı ve yelesi ıslandı | hızla koşup büyük ağaçların altına girdi
@tohum: doru-0151
@degisim: basamak -> damla
Doru ormanın kenarındaki açıklıkta çimen yiyordu. Birden kara bulutlar geldi ve yağmur yağmaya başladı. Doru'nun yelesi hemen ıslandı ve çok karışık oldu. Kuru kalmak için büyük ağaçların altına gitmeliydi. Ama ağaçlar biraz uzaktaydı. Doru açık ve düz çimenlerin üstünde hızla koştu. Kısa sürede sık yaprakların altına vardı. Burada yağmur onu ıslatmıyordu. Damlalar yukarıdaki yapraklara tutunuyordu. Doru başını iki kez salladı. Sonra yağmurun sesini rahatça dinledi. Doru bundan sonra yağmur başlayınca hemen büyük ağaçların altına koştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hemen ıslandı ve çok karışık oldu"
   - Cümle 3: «Doru'nun yelesi hemen ıslandı ve çok karışık oldu.»
   - Açıklama: Yelenin karışması sorun gibi kuruluyor ama hikayede bir daha ele alınmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru'nun yelesi hemen ıslandı ve çok karışık oldu"
   - Cümle 3: «Doru'nun yelesi hemen ıslandı ve çok karışık oldu.»
   - Açıklama: Yelenin karışması kurulup bir daha hiç kullanılmıyor ve çözülmüyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Damlalar yukarıdaki yapraklara tutunuyordu"
   - Cümle 9: «Damlalar yukarıdaki yapraklara tutunuyordu.»
   - Açıklama: Damlalar tutunmaz; fiil öznesine uymuyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Doru bundan sonra yağmur başlayınca hemen büyük ağaçların altına koştu"
   - Cümle 12: «Doru bundan sonra yağmur başlayınca hemen büyük ağaçların altına koştu.»
   - Açıklama: Son cümle hikayede zaten yapılanı tekrarlayan kuru bir eylem; sıcak bir kapanış ya da doyurucu bir ders vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0151` birebir aynı, `@degisim: basamak -> damla` (tutuyorsan), ardından `@onarim: 9ff44c18c8da992236ebbbaae820435ec25adb2b`, sonra gövde.

### Hikâye 2: tohum doru-0152 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0152
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bağcık', fiil 'tamamlamak', sıfat 'kaygan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: vadinin ucundan tık tık diye bir ses geldi | hızla koşup sesi yapan damlaları buldu
@tohum: doru-0152
@degisim: bağcık -> kütük
Doru annesiyle vadide çimen yiyordu. Birden vadinin öbür ucundan "tık, tık" diye bir ses geldi. Doru bu sesi çok merak etti, ama ses bazen duruyordu. "Anne, sesi bulmaya gidebilir miyim?" diye sordu Doru. "Git, ama ıslak taşlara basma," dedi annesi. Doru açık ve düz çimenlerin üstünde hızla koştu. Koşusunu vadinin ucunda tamamladı. Orada yüksek bir kayadan su damlıyordu. Damlalar kuru bir kütüğe düşüp "tık, tık" diye ses çıkarıyordu. Kütüğün yanındaki taşlar ıslak ve kaygandı. Doru onlara basmadı ve kenardan baktı. "Anne, sesi su yapıyormuş!" diye seslendi Doru. Doru çok sevindi, çünkü sesi yapan şeyi kendisi bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "diye bir ses geldi"
   - Cümle 2: «Birden vadinin öbür ucundan "tık, tık" diye bir ses geldi.»
   - Açıklama: Bir ses duyulması sorun değil; ortada çözülecek bir dert ve sebep yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ama ses bazen duruyordu"
   - Cümle 3: «Doru bu sesi çok merak etti, ama ses bazen duruyordu.»
   - Açıklama: Sesin bazen durması bir güçlük gibi kuruluyor ama hikayede hiçbir işe yaramıyor.
   - Açıklama: Sesin bazen durması işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Koşusunu vadinin ucunda tamamladı"
   - Cümle 7: «Koşusunu vadinin ucunda tamamladı.»
   - Açıklama: 'Koşusunu tamamladı' soyut ve resmi bir anlatım; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Koşusunu tamamladı' soyut ve küçük çocuğa uygun olmayan yapay bir anlatım.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Damlalar kuru bir kütüğe düşüp"
   - Cümle 9: «Damlalar kuru bir kütüğe düşüp "tık, tık" diye ses çıkarıyordu.»
   - Açıklama: Üstüne sürekli su damlayan kütüğün kuru olması çelişki.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0152` birebir aynı, `@degisim: bağcık -> kütük` (tutuyorsan), ardından `@onarim: 873d1a36b6ed982c551abe0e8e400d62f5d8b25f`, sonra gövde.

### Hikâye 3: tohum doru-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0153
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'limon', fiil 'uçurmak', sıfat 'güneşli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: koşarken çiçeğin bütün tüylerini uçurdu | özür diledi ve hızla koşup yeni bir çiçek buldu
@tohum: doru-0153
@degisim: limon -> çiçek
Güneşli bir günde Doru vadide oyun oynuyordu. Kırat ise beyaz tüylü bir çiçeğin tüylerini havaya uçurmak istiyordu. Ama Doru koşarken çiçeğin dibinden geçti ve bütün tüyler uçup gitti. Kırat çiçeğe üzgün üzgün baktı. Doru hemen Kırat'ın yanına geldi. "Özür dilerim, Kırat, sana yeni bir çiçek bulacağım!" dedi Doru. Doru açık ve düz çimenlerde hızla koştu. Uzakta beyaz tüylü başka bir çiçek buldu. "Kırat, burada bir tane var!" diye seslendi Doru. Kırat yavaş yavaş onun yanına geldi. Çiçeğe hafifçe üfledi ve tüyler havada uçuştu. "Teşekkürler, Doru, çok güzel," dedi Kırat. Doru çok sevindi, çünkü Kırat'ı yeniden mutlu etmişti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru vadide oyun oynuyordu"
   - Cümle 1: «Güneşli bir günde Doru vadide oyun oynuyordu.»
   - Açıklama: Başlıktaki yer dağ iken hikaye vadide başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0153` birebir aynı, `@degisim: limon -> çiçek` (tutuyorsan), ardından `@onarim: 39ed0418194712654efaf0af20e0dca62a3ab352`, sonra gövde.

### Hikâye 4: tohum doru-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0154
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fide', fiil 'köpürmek', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: yola kalın bir dal düşmüştü ve küçük at geçemedi | dalı iterek yolun kenarına yuvarladı
@tohum: doru-0154
@degisim: fide -> dal
Doru Alaca'ya vadideki güzel suyu göstermek istiyordu. Bu onun için küçük bir sürpriz olacaktı. Ama yola kalın bir dal düşmüştü ve Alaca onun üstünden geçemedi. "Doru, bu dal benim için çok yüksek," dedi Alaca. Doru ona yardım etmek için dalı burnuyla itti. Dal yolun kenarına yuvarlandı. Alaca kolayca geçti. Az sonra ikisi suyun yanına vardı. Su taşların arasında beyaz beyaz köpürüyordu. "Sürpriz, Alaca!" dedi Doru sevecen bir sesle. "Çok güzel, teşekkürler, Doru!" dedi Alaca. Alaca sevinçle zıpladı. Doru çok mutlu oldu, çünkü sürprizi Alaca'yı sevindirmişti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bu onun için küçük bir sürpriz olacaktı"
   - Cümle 2: «Bu onun için küçük bir sürpriz olacaktı.»
   - Açıklama: 'onun' zamirinin Doru'yu mu Alaca'yı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0154` birebir aynı, `@degisim: fide -> dal` (tutuyorsan), ardından `@onarim: 77a5725b9b38b33a87458b24e2bd8fd146168530`, sonra gövde.

### Hikâye 5: tohum doru-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0156
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'sis', fiil 'konmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sisin içinde oynak renkler vardı ama sis çok kalındı | cesaretle sisin içine yürüdü ve kelebekleri buldu
@tohum: doru-0156
Ormanda sabah sisi vardı ve ağaçlar zor görünüyordu. Doru sisin arasında oynak, küçük renkler gördü. Bunların ne olduğunu çok merak etti, ama sis çok kalındı. Doru cesaretle sisin içine doğru yürüdü. Adım adım ilerledi ve renkler yaklaştı. Sonunda büyük bir çalının yanına vardı. Çalı sarı çiçeklerle doluydu. Beyaz ve mavi kelebekler de çiçeklere konuyor ve yeniden uçuyordu. Uzaktan gördüğü renkler bu kelebeklerdi. Doru çalının yanında durdu ve onları uzun uzun izledi. Doru çok mutlu oldu, çünkü sisin içindeki renklerin ne olduğunu bulmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sisin içinde oynak renkler"
   - Cümle 0 (plan satırı): «sisin içinde oynak renkler vardı ama sis çok kalındı | cesaretle sisin içine yürüdü ve kelebekleri buldu»
   - Açıklama: Plan satırında da 'oynak renkler' mecazı var.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sisin arasında oynak, küçük renkler gördü"
   - Cümle 2: «Doru sisin arasında oynak, küçük renkler gördü.»
   - Açıklama: Renklerin 'oynak' olması mecazdır ve 3 yaşındaki çocuk için anlaşılır değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oynak, küçük renkler gördü"
   - Cümle 2: «Doru sisin arasında oynak, küçük renkler gördü.»
   - Açıklama: 'Oynak renkler' mecazlı bir anlatım; küçük çocuk için somut değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle sisin içine doğru yürüdü"
   - Cümle 4: «Doru cesaretle sisin içine doğru yürüdü.»
   - Açıklama: Görüşün kapalı olduğu kalın sisin içine tek başına yürümek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0156` birebir aynı, ardından `@onarim: 4eea78a2c501f664696c0af91951affeca3ddd0f`, sonra gövde.

### Hikâye 6: tohum doru-0157 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0157
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kaya', fiil 'uyumak', sıfat 'sakin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: bir bulutun gölgesi büyük kayaya doğru ilerliyordu | düz yerde hızla koşup kayaya gölgeden önce vardı
@tohum: doru-0157
Bir sabah sürü daha uyuyordu ve vadi çok sakindi. Doru annesinin yanında dururken yerde bir bulutun gölgesini gördü. Gölge büyük bir kayaya ilerliyordu ve Doru ondan önce varmak istedi. "Anne, gölgeyle yarışabilir miyim?" diye sordu Doru. "Olur, ama yalnız düz yerde koş," dedi annesi. Doru açık vadide hızla koştu. Kayaya vardığında gölge daha gerideydi. Az sonra gölge de kayanın üstüne geldi. Annesi yavaş yavaş Doru'nun yanına yürüdü. "Aferin, Doru, gölgeyi geçtin!" dedi annesi. Sonra ikisi kayanın yanında mutlu mutlu çimen yedi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Doru ondan önce varmak istedi"
   - Cümle 3: «Gölge büyük bir kayaya ilerliyordu ve Doru ondan önce varmak istedi.»
   - Açıklama: 'Ondan' gölgeyi mi kayayı mı gösteriyor belli değil ve varılacak yer söylenmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Gölge büyük bir kayaya ilerliyordu"
   - Cümle 3: «Gölge büyük bir kayaya ilerliyordu ve Doru ondan önce varmak istedi.»
   - Açıklama: Gölgeyle yarışmak bir oyun isteği, çözülmesi gereken bir sorun yok.
   - Açıklama: Bulut gölgesinin kayaya ilerlemesi gerçek bir sorun değil, yalnız bir yarış isteği.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0157` birebir aynı, ardından `@onarim: d1985a0edff5ec6b57c2aeeda6b48837ab86217d`, sonra gövde.

### Hikâye 7: tohum doru-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0160
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'patates', fiil 'kurtulmak', sıfat 'simsiyah'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: sırası gelen atın kuyruğu çalıya takıldı | çalının dalını dişleriyle çekip kuyruğu kurtardı
@tohum: doru-0160
@degisim: patates -> taş
Bir sabah Doru ile Kırat çayırda sırayla bir taşın üstünden atlıyordu. Taş simsiyah ve alçaktı. Sıra Kırat'a geldi ama Kırat'ın kuyruğu dikenli bir çalıya takılmıştı. "Doru, kuyruğum çıkmıyor!" dedi Kırat. Kırat kuyruğunu çekti ama kurtulamadı. Doru hemen Kırat'ın yardımına koştu. Çalının dalını dişleriyle tuttu ve yavaşça yana çekti. Kırat bir anda serbest kaldı. "Teşekkürler, Doru, şimdi atlayabilirim," dedi Kırat. Kırat koştu ve taşın üstünden güzelce atladı. Doru sevinçle başını salladı. Doru ile Kırat sırayla atlamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Kırat çayırda sırayla"
   - Cümle 1: «Bir sabah Doru ile Kırat çayırda sırayla bir taşın üstünden atlıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru hemen Kırat'ın yardımına koştu"
   - Cümle 6: «Doru hemen Kırat'ın yardımına koştu.»
   - Açıklama: 'Yardımına koşmak' kalıplaşmış bir deyimdir; küçük çocuk için somut değildir.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Çalının dalını dişleriyle tuttu"
   - Cümle 7: «Çalının dalını dişleriyle tuttu ve yavaşça yana çekti.»
   - Açıklama: Dikenli çalının dalını ağızla tutmak taklit edilince yaralanmaya yol açabilir.
   - Açıklama: Dikenli çalıyı ağızla çekmek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0160` birebir aynı, `@degisim: patates -> taş` (tutuyorsan), ardından `@onarim: 1d73472fdae58207b4b12d783a459c3a898106af`, sonra gövde.

### Hikâye 8: tohum doru-0162 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0162
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çiçek', fiil 'eğmek', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: havada beyaz bir şey vardı ve rüzgar onu götürüyordu | düz yolda koşup onu yakaladı ve çiçeği buldu
@tohum: doru-0162
Rüzgar hafif hafif esiyordu. Doru ormanın tozlu yolunda havada beyaz bir şey gördü. Ama rüzgar onu yolun ucuna doğru götürüyordu. Doru bunun ne olduğunu çok merak etti. Yol düz ve açıktı. Doru hızla koştu ve beyaz şeyin önüne geçti. O şey yavaşça Doru'nun burnuna kondu. Bu, ince tüyleri olan küçük bir tohumdu. Doru etrafına baktı. Yolun kenarında yuvarlak, pamuk gibi çiçekler vardı. Tohum bu çiçeklerden gelmişti. Doru başını bir çiçeğe eğdi ve üfledi. Havaya bir sürü tohum uçtu. Doru çiçeklere üflemeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "havada beyaz bir şey gördü"
   - Cümle 2: «Doru ormanın tozlu yolunda havada beyaz bir şey gördü.»
   - Açıklama: Havada uçan beyaz bir şeyin rüzgarla gitmesi gerçek bir sorun değil, çocuğun önemseyeceği bir dert kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0162` birebir aynı, ardından `@onarim: 477221ee46e04a9ab6cdc996051f0cd194f0475d`, sonra gövde.

### Hikâye 9: tohum doru-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0163
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'nilüfer', fiil 'ışıldamak', sıfat 'çevik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: yanlışlıkla arkadaşının bulduğu papatyayı yedi | cesaretle karanlık yere gidip ondan özür diledi
@tohum: doru-0163
@degisim: nilüfer -> papatya
Doru ile Alaca ormanın güneşli bir yerinde oynuyordu. Alaca güneşte ışıldayan beyaz bir papatya buldu. Ama Doru bakmadan papatyayı çimenle birlikte yedi. Alaca çok üzüldü. Sonra çevik adımlarla sık ağaçların arasına koştu. Orası karanlık ve sessizdi. Doru biraz durdu, sonra cesaretle içeri girdi. Alaca büyük bir ağacın dibinde duruyordu. Doru başını eğdi ve Alaca'dan özür diledi. Alaca başını Doru'nun boynuna dayadı. Sonra ikisi birlikte güneşli yere döndü. Orada yeni papatyalar buldular. Doru ile Alaca papatyaların yanında mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra çevik adımlarla sık ağaçların arasına koştu"
   - Cümle 5: «Sonra çevik adımlarla sık ağaçların arasına koştu.»
   - Açıklama: Küçük birinin üzülünce tek başına karanlık, sık ağaçların arasına kaçması taklit edilince tehlikeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra çevik adımlarla"
   - Cümle 5: «Sonra çevik adımlarla sık ağaçların arasına koştu.»
   - Açıklama: 'Çevik' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Çevik adımlarla' edebi bir anlatım, 'çevik' kelimesini 3 yaşındaki çocuk bilmez.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Orası karanlık ve sessizdi"
   - Cümle 6: «Orası karanlık ve sessizdi.»
   - Açıklama: Küçük Alaca'nın kaçtığı karanlık ve sessiz yer 3-6 yaş için korkutucu bir ortam.
   - Açıklama: Küçük Alaca'nın kaçtığı karanlık ve sessiz yer 3-6 yaş için korkutucu bir öğe.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0163` birebir aynı, `@degisim: nilüfer -> papatya` (tutuyorsan), ardından `@onarim: 39328e0b158d375fafe241a7e63aec1d0afaa2fe`, sonra gövde.

### Hikâye 10: tohum doru-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0164
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kar', fiil 'şaşırtmak', sıfat 'faydalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kar çimenleri kapattı ve sürü yiyecek bulamadı | ayaklarıyla karı itip çimenleri açtı
@tohum: doru-0164
Çayırın her tarafı bembeyazdı. Sabah yağan kar Doru'yu çok şaşırttı. Ama kar çimenleri kapatmıştı ve sürü yiyecek bulamadı. Doru sürüye yardım etmek istedi. Ön ayaklarıyla karı iki yana itti. Karın altından yeşil çimenler çıktı. Ayakları bu işte çok faydalıydı. Doru biraz ileri yürüdü ve karı yine itti. Sonra bir yer daha açtı. Az sonra çayırda geniş bir yeşil alan oldu. Artık sürünün yemesi için bol bol çimen vardı. Doru çok sevindi, çünkü herkese yetecek kadar çimen açmıştı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırın her tarafı bembeyazdı"
   - Cümle 1: «Çayırın her tarafı bembeyazdı.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "sürü yiyecek bulamadı"
   - Cümle 3: «Ama kar çimenleri kapatmıştı ve sürü yiyecek bulamadı.»
   - Açıklama: Arka plandaki çoğul canlı olan sürü sorunun öznesi olarak olaya katılıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ayakları bu işte çok faydalıydı"
   - Cümle 7: «Ayakları bu işte çok faydalıydı.»
   - Açıklama: 'Bu işte faydalıydı' soyut bir anlatım ve 'faydalı' 3 yaşındaki çocuğun bilmeyebileceği bir kelime.
   - Açıklama: 'Bu işte çok faydalıydı' soyut bir anlatım ve 'faydalı' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ayakları bu işte çok faydalıydı"
   - Cümle 7: «Ayakları bu işte çok faydalıydı.»
   - Açıklama: Tohumdaki özellik yardım; ayakların faydası ayrı bir özellik gibi öne çıkarılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0164` birebir aynı, ardından `@onarim: 0d8092e631f4b2a943f184bb09b92cf6f71eb992`, sonra gövde.

### Hikâye 11: tohum doru-0166 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0166
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'zambak', fiil 'korumak', sıfat 'utangaç'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: koşu yolunda bir zambak vardı ve arkadaşı onu görmedi | zambağın önünde durup arkadaşına başka yol gösterdi
@tohum: doru-0166
@degisim: utangaç -> beyaz
Bir sabah Doru ile Karatay vadide sırayla koşuyordu. Her biri büyük kayaya kadar koşup geri dönüyordu. Sıra Karatay'a geldi ama yolun ortasında beyaz bir zambak açmıştı. Heyecanlı Karatay zambağı görmedi ve koşmaya hazırlandı. "Dur, Karatay, çiçeğe basma!" dedi Doru. Doru zambağa yardım etmek için hemen yanına gitti ve önünde durdu. "Karatay, zambağın yanından geç," dedi Doru. Karatay güldü ve çiçeğin yanından koştu. Sonra kayaya kadar gitti ve geri döndü. "Zambağı görmemiştim, teşekkürler, Doru!" dedi Karatay. Doru çok sevindi, çünkü zambağı korumuş ve oyunu bozmamıştı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "vadide sırayla koşuyordu"
   - Cümle 1: «Bir sabah Doru ile Karatay vadide sırayla koşuyordu.»
   - Açıklama: Başlıktaki yer dağ ama hikaye vadide geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Karatay vadide sırayla koşuyordu"
   - Cümle 1: «Bir sabah Doru ile Karatay vadide sırayla koşuyordu.»
   - Açıklama: Başlıktaki yer dağ ama hikaye vadide geçiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru zambağa yardım etmek"
   - Cümle 6: «Doru zambağa yardım etmek için hemen yanına gitti ve önünde durdu.»
   - Açıklama: Çiçeğe yardım edilmez; 'yardım etmek' öznesine/nesnesine uygun değil.
   - Açıklama: Çiçeğe yardım edilmez; 'yardım etmek' nesnesine uymuyor, 'zambağı korumak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0166` birebir aynı, `@degisim: utangaç -> beyaz` (tutuyorsan), ardından `@onarim: 2263765600de4c2ff7b3e602edada1392f78d828`, sonra gövde.

### Hikâye 12: tohum doru-0167 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0167
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'blok', fiil 'örtmek', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: oynarken annesinden uzaklaştı | düz yolda koşup annesine döndü ve özür diledi
@tohum: doru-0167
@degisim: blok -> dal
Doru ormanda annesiyle birlikte çimen yiyordu. Annesi ona yanında kalmasını söylemişti. Ama Doru yaprakların arasında oynarken annesinden uzaklaştı. Birden bulutlar güneşi örttü. Doru o zaman annesini hatırladı. Doru annesinin yanına hemen dönmek istedi. Doru ormanın düz ve geniş yolunda hızla koştu. Kırılgan kuru dallar ayaklarının altında ses çıkardı. Annesi büyük bir ağacın yanında onu bekliyordu. Doru başını eğdi ve annesinden özür diledi. Annesi başını Doru'nun başına sürdü. Doru çok sevindi, çünkü annesinin yanına çabucak dönmüştü.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru annesinin yanına hemen"
   - Cümle 6: «Doru annesinin yanına hemen dönmek istedi.»
   - Açıklama: Art arda üç cümle 'Doru' ile başlıyor; ad gereksiz tekrar ediliyor.
   - Açıklama: Art arda üç cümle gereksizce 'Doru' ile başlıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kırılgan kuru dallar"
   - Cümle 8: «Kırılgan kuru dallar ayaklarının altında ses çıkardı.»
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Kırılgan' kelimesi 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kırılgan kuru dallar ayaklarının altında ses çıkardı"
   - Cümle 8: «Kırılgan kuru dallar ayaklarının altında ses çıkardı.»
   - Açıklama: Kuru dallar olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Dalların çıkardığı ses olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0167` birebir aynı, `@degisim: blok -> dal` (tutuyorsan), ardından `@onarim: 8ccbb260dd4c058059beecc9610e67cb85ee4744`, sonra gövde.
