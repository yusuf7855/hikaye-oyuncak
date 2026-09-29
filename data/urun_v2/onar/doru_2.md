# Editör görevi (onarım): Doru, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar2.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0001
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'güneş', fiil 'dökülmek', sıfat 'gürültülü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: iki arkadaş çok susamıştı ama yakında su yoktu | cesaretle gürültülü sese gidip dökülen suyu buldu
@tohum: doru-0001
Dağda güneş çok sıcak parlıyordu. Doru ile Karatay koşup oynamış ve çok susamıştı. Ama yakında içecek hiç su yoktu. Kayaların yanından geçerken gürültülü bir ses duydular. Karatay hemen durdu ve kayalara baktı. "Bu ses ne, Doru?" diye sordu Karatay. "Gel, gidip bakalım," dedi Doru. Doru cesaretle kayalara doğru yürüdü. Karatay da Doru'nun arkasından geldi. Kayaların arkasında küçük bir dere vardı. Su, kayaların üstünden aşağı dökülüyordu. Gürültülü ses bu sudan geliyordu. İki arkadaş dereye eğildi ve serin sudan içti. "Bu su çok güzel!" dedi Karatay. Doru ile Karatay çok sevindi, çünkü sesin nereden geldiğini bulmuşlardı.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ama yakında içecek hiç su yoktu"
   - Cümle 3: «Ama yakında içecek hiç su yoktu.»
   - Açıklama: Yakında hiç su olmadığı söyleniyor ama hemen kayaların arkasında akan bir dere çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kayaların yanından geçerken gürültülü bir ses duydular"
   - Cümle 4: «Kayaların yanından geçerken gürültülü bir ses duydular.»
   - Açıklama: Suya götüren ses sebepsizce beliriyor ve çözümü şans eseri getiriyor.
   - Açıklama: Çözümü getiren ses sebepsizce ve tesadüfen beliriyor; figür suyu aramak için bir şey yapmadan su kendiliğinden ortaya çıkıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: ""Gel, gidip bakalım," dedi Doru"
   - Cümle 7: «"Gel, gidip bakalım," dedi Doru.»
   - Açıklama: Doru su aramıyor, yalnız sesi merak edip gidiyor; çözüm sorunun sebebine bilinçli olarak yönelmiyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "çünkü sesin nereden geldiğini bulmuşlardı"
   - Cümle 15: «Doru ile Karatay çok sevindi, çünkü sesin nereden geldiğini bulmuşlardı.»
   - Açıklama: Hedef su bulmakken son cümledeki sevinç sesin kaynağını bulmaya bağlanıyor ve susuzluk hedefine dönülmüyor.
   - Açıklama: Hedef susuzluğu gidermekken son cümle sevinci sesin kaynağını bulmaya bağlıyor ve kapanış asıl hedefe dönmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0001` birebir aynı, ardından `@onarim: 1268dbcbd6d817091dfff1027fc84ea037ac6b24`, sonra gövde.

### Hikâye 2: tohum doru-0003 (deneme 2 -> 3)

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
Parkta büyük bir ağaç vardı. Doru bu ağacın gölgesinde dinlenmek istedi. Ama ağacın altı taşlı ve sertti. Doru orada yumuşak bir yatak yapmaya karar verdi. Çayırın ucunda büyük bir kaya duruyordu. Kayanın dibinde yeşil yosunlar vardı. Kayanın yanındaki uzun otlar rüzgarda sallanıp ses çıkarıyordu. Doru bu sesten korkmadı ve cesaretle kayaya yürüdü. Yosunu dişleriyle tuttu ve çekti. Yosun taştan kolayca ayrıldı. Doru yosunları tek tek ağacın altına taşıdı. Hepsini taşların üstüne serdi. Ağacın altı yumuşacık oldu. Doru yeni yatağına uzandı ve gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "uzun otlar rüzgarda sallanıp ses çıkarıyordu"
   - Cümle 7: «Kayanın yanındaki uzun otlar rüzgarda sallanıp ses çıkarıyordu.»
   - Açıklama: Otların sesi yalnız cesaret göstermek için ekleniyor, yatak sorununa hiçbir katkısı yok.
   - Açıklama: Otların sesi olaydan çıkmıyor ve sorunun çözümünde hiçbir işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru bu sesten korkmadı ve cesaretle kayaya yürüdü"
   - Cümle 8: «Doru bu sesten korkmadı ve cesaretle kayaya yürüdü.»
   - Açıklama: Tohumdaki cesaret özelliği yalnız ot hışırtısına karşı süs olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0003` birebir aynı, `@degisim: kibar -> yumuşak` (tutuyorsan), ardından `@onarim: 8afe099c435040cf3113760274d46acce9b020db`, sonra gövde.

### Hikâye 3: tohum doru-0004 (deneme 2 -> 3)

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
Bir sabah Doru ile Kırat ormanda su içmeye geldi. Ama yağmurdan sonra küçük gölün suyu çamurlu olmuştu. Kırat bu suyu içemedi ve üzüldü. Doru, Kırat için temiz su bulmaya karar verdi. Uzaktan hafif bir su sesi geliyordu. Ormanın içinden o sese doğru geniş ve düz bir yol gidiyordu. Doru bu yolda hızla koştu. Yolun sonunda küçük bir dere vardı. Derenin suyu berrak ve serindi, dibindeki taşlar görünüyordu. Doru geri döndü ve Kırat'ın yanına geldi. Kırat'ı yavaş yavaş dereye götürdü. Kırat temiz sudan bol bol içti. Sonra başını sevgiyle Doru'ya sürttü. Doru çok sevindi, çünkü Kırat artık temiz su içebiliyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "suyu berrak ve serindi"
   - Cümle 9: «Derenin suyu berrak ve serindi, dibindeki taşlar görünüyordu.»
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez; 'temiz' yeterliydi.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru geri döndü ve Kırat'ın yanına geldi"
   - Cümle 10: «Doru geri döndü ve Kırat'ın yanına geldi.»
   - Açıklama: Doru dereyi tek başına bulup geri dönüyor ve Kırat'ı sonra götürüyor; çözüm iki adımdan uzun sürüyor.
   - Açıklama: Çözüm koşup dereyi bulma, geri dönme ve Kırat'ı dereye götürme olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0004` birebir aynı, `@degisim: patlıcan -> su` (tutuyorsan), ardından `@onarim: 3a443e5c38ce78e29e72bbe46124fb712f10a794`, sonra gövde.

### Hikâye 4: tohum doru-0006 (deneme 2 -> 3)

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
@plan: uzaktan gelen yaşlı at çok acıkmıştı | dört elmanın yarısını ona götürdü
@tohum: doru-0006
@degisim: iplik -> elma
Bir sabah Doru dağda küçük bir elma ağacı buldu. Ağacın altında yalnız dört elma vardı, ikisi kırmızı ve ikisi yeşildi. Yanına gelen Kırat çok uzaktan gelmişti ve çok acıkmıştı. Doru, Kırat'a yardım etmek ve elmaları paylaşmak istedi. Her kırmızı elmayı bir yeşil elmayla eşleştirdi. Bir kırmızı ve bir yeşil elmayı ağzıyla Kırat'a götürdü. "Bu iki elma senin, Kırat," dedi Doru. "Teşekkür ederim, Doru, gel birlikte yiyelim," dedi Kırat. Doru kalan iki elmayı da getirdi. İkisi yan yana durdu ve elmalarını yedi. Elmalar çok tatlıydı. Doru çok mutlu oldu, çünkü elmalarını paylaşınca Kırat da doymuştu.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "uzaktan gelen yaşlı at çok acıkmıştı"
   - Cümle 0 (plan satırı): «uzaktan gelen yaşlı at çok acıkmıştı | dört elmanın yarısını ona götürdü»
   - Açıklama: Gövdede aç olan at yaşlı bir yabancı değil Kırat'tır ve yaşlı olduğu hiç söylenmez.
   - Açıklama: Plan atı yaşlı diye tanıtıyor ama gövdede Kırat'ın yaşlı olduğu hiç söylenmiyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Yanına gelen Kırat çok uzaktan gelmişti"
   - Cümle 3: «Yanına gelen Kırat çok uzaktan gelmişti ve çok acıkmıştı.»
   - Açıklama: Aynı cümlede 'gelen' ve 'gelmişti' gereksiz tekrar ediliyor.
   - Açıklama: Aynı cümlede 'gelen' ve 'gelmişti' gereksiz yere tekrarlanıyor.
   - Açıklama: 'gelen' ve 'gelmişti' aynı cümlede gereksiz yere tekrarlanıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Her kırmızı elmayı bir yeşil elmayla eşleştirdi"
   - Cümle 5: «Her kırmızı elmayı bir yeşil elmayla eşleştirdi.»
   - Açıklama: 'Eşleştirdi' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0006` birebir aynı, `@degisim: iplik -> elma` (tutuyorsan), ardından `@onarim: a46a3ddd17adf2819e92358d5b9fc52d35fc0618`, sonra gövde.

### Hikâye 5: tohum doru-0007 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0007
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'rüzgar', fiil 'kirletmek', sıfat 'yapraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: rüzgar esti ve elma çalıların arasında kayboldu | cesaretle çalılara girip elmayı buldu
@tohum: doru-0007
Bir sabah Doru ormanda kırmızı bir elma buldu. Tam elmayı yiyecekti ki güçlü bir rüzgar esti. Elma yokuştan yuvarlandı ve yapraklı çalıların arasında kayboldu. Doru elmasını bulmak istedi. Çalıların arası çok çamurluydu. Doru çamurdan kaçmadı ve cesaretle çalılara girdi. Çamur Doru'nun ayaklarını kirletti ama Doru durmadı. Yaprakları burnuyla yavaşça itti. Kırmızı elma büyük bir ağacın dibinde duruyordu. Doru elmayı ağzıyla aldı ve çalıların arasından çıktı. Ayaklarını yumuşak çimenlere sildi. Sonra elmasını güneşte mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Tam elmayı yiyecekti ki güçlü bir rüzgar esti"
   - Cümle 2: «Tam elmayı yiyecekti ki güçlü bir rüzgar esti.»
   - Açıklama: Rüzgarın Doru'nun yemek üzere olduğu elmayı yokuştan yuvarlaması zorlama ve pek akla yatkın olmayan bir sebep.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0007` birebir aynı, ardından `@onarim: ab03263c8d2651ae3f6d2899296d2db637486c48`, sonra gövde.

### Hikâye 6: tohum doru-0008 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0008
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'tohum', fiil 'silmek', sıfat 'yemyeşil'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: saklanan anne yeşil çalıların arkasında bulunamadı | cesaretle çalılara girdi ve sesi izleyip buldu
@tohum: doru-0008
@degisim: silmek -> saklanmak
Ormanda rüzgar hafif hafif esiyordu. Doru ile annesi ağaçların arasında sırayla saklambaç oynuyordu. Önce annesi yemyeşil çalıların arkasına saklandı ve Doru onu bulamadı. Çalılar çok sık ve yüksekti. Doru cesaretle çalıların arasına girdi. Birden yerdeki kuru tohumlar hışırdadı. Ses, annesinin ayaklarının altından geliyordu. Doru sese doğru yürüdü ve annesini buldu. "Buldum seni, anneciğim!" dedi Doru. "Çok güzel buldun, şimdi sıra sende, Doru," dedi annesi. Bu kez Doru büyük bir ağacın arkasına saklandı. Annesi biraz aradı ve Doru'yu buldu. Doru ile annesi çok sevindi, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "annesi yemyeşil çalıların arkasına saklandı ve Doru onu bulamadı"
   - Cümle 3: «Önce annesi yemyeşil çalıların arkasına saklandı ve Doru onu bulamadı.»
   - Açıklama: Saklambaçta saklananı hemen bulamamak oyunun kendisidir, gerçek bir sorun sayılmaz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yerdeki kuru tohumlar hışırdadı"
   - Cümle 6: «Birden yerdeki kuru tohumlar hışırdadı.»
   - Açıklama: Hışırdamak yaprak için kullanılır; tohumlara uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden yerdeki kuru tohumlar hışırdadı"
   - Cümle 6: «Birden yerdeki kuru tohumlar hışırdadı.»
   - Açıklama: Çözümü getiren ses tesadüfen ve sebepsizce beliriyor.
   - Açıklama: Çözümü getiren ses Doru'nun bir eyleminden değil, sebepsiz bir rastlantıdan çıkıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kez Doru büyük bir ağacın arkasına saklandı"
   - Cümle 11: «Bu kez Doru büyük bir ağacın arkasına saklandı.»
   - Açıklama: Sorun çözüldükten sonra ikinci bir saklambaç turu sorunla bağı olmayan ek bir olay olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0008` birebir aynı, `@degisim: silmek -> saklanmak` (tutuyorsan), ardından `@onarim: e02196dee21aeb2ba8e9461705a021816b757b73`, sonra gövde.

### Hikâye 7: tohum doru-0009 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0009
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'menekşe', fiil 'kapatmak', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yuvarlak taş büyük bir kütüğün arkasında kayboldu | cesaretle kütüğün arkasına gidip yaprakların altında buldu
@tohum: doru-0009
Dağda yepyeni menekşeler açmıştı. Doru çiçeklerin arasında yuvarlak bir taşla oynuyordu. Birden taş yuvarlandı ve büyük bir kütüğün arkasında kayboldu. Kütüğün arkasındaki kuru yapraklar rüzgarda ses çıkarıyordu. Doru önce durdu. Sonra cesaretle kütüğün arkasına yürüdü. Ama taşı göremedi. Kuru yapraklar taşın üstünü kapatmıştı. Doru yaprakları burnuyla yavaşça itti. Yuvarlak taş yaprakların altındaydı. Doru taşı burnuyla çiçeklere doğru yuvarladı. Taş yine güneşe çıktı. Doru bu kez kütükten uzakta oynadı. Taşını çiçeklerin arasında mutlu mutlu itmeye devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dağda yepyeni menekşeler açmıştı."
   - Cümle 1: «Dağda yepyeni menekşeler açmıştı.»
   - Açıklama: Çiçek için 'yepyeni' uygun sıfat değil; 'yeni açmış menekşeler' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden taş yuvarlandı ve büyük bir kütüğün arkasında kayboldu"
   - Cümle 3: «Birden taş yuvarlandı ve büyük bir kütüğün arkasında kayboldu.»
   - Açıklama: Taş yalnızca birkaç adım öteye yuvarlanıyor ve hemen bulunuyor; sorun 'dağıldı, topladı, bitti' türünden önemsiz bir olay.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden taş yuvarlandı ve"
   - Cümle 3: «Birden taş yuvarlandı ve büyük bir kütüğün arkasında kayboldu.»
   - Açıklama: Taşın neden yuvarlandığı söylenmiyor; sorunun sebebi verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0009` birebir aynı, ardından `@onarim: b2435a54393cb7889139fe5d814dd326dd780b6f`, sonra gövde.

### Hikâye 8: tohum doru-0011 (deneme 2 -> 3)

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
@plan: oyunun beyaz taşı düşüp otlara doğru yuvarlandı | hızla koşup taşı otlara girmeden durdurdu
@tohum: doru-0011
@degisim: yardımsever -> beyaz
Rüzgar esiyordu ve Doru ile Karatay parkta gemi oyunu oynuyordu. Oyunun hazinesi yumurta gibi beyaz, yuvarlak bir taştı. Ama Karatay sevinçle başını savurdu ve taş ağzından düşüp yuvarlandı. Taş, geniş çayırın ucundaki uzun otlara doğru gidiyordu. "Hazinemiz otlarda kaybolacak!" dedi Karatay telaşla. "Merak etme, ben yakalarım," dedi Doru. Çayır açık ve düzdü. Doru hızla koştu ve taşı otlara girmeden durdurdu. Sonra taşı ağzıyla alıp Karatay'a getirdi. Karatay bu kez taşı ağzında dikkatle tuttu. "Teşekkürler, Doru, hazinemiz kurtuldu!" dedi Karatay. Doru çok sevindi, çünkü arkadaşının oyununu kurtarmıştı.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "parkta gemi oyunu oynuyordu"
   - Cümle 1: «Rüzgar esiyordu ve Doru ile Karatay parkta gemi oyunu oynuyordu.»
   - Açıklama: Gemi ve hazine oyunu özgür at sürüsünün doğa dünyasında olmayan bir nesne ve kavram, kart kapalı dünyasına aykırı.
   - Açıklama: Özgür at sürüsünün doğa dünyasında gemi yoktur; kapalı dünyaya karttaki olmayan bir nesne ekleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Merak etme, ben yakalarım,""
   - Cümle 6: «"Merak etme, ben yakalarım," dedi Doru.»
   - Açıklama: 'Merak etme' kalıplaşmış bir deyim; küçük çocuk için 'Korkma' gibi somut bir söz gerekir.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Karatay bu kez taşı ağzında dikkatle tuttu"
   - Cümle 10: «Karatay bu kez taşı ağzında dikkatle tuttu.»
   - Açıklama: Yumurta büyüklüğünde taşı ağızda taşımak çocuğun taklit edince yutma tehlikesi doğurabilecek bir davranış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkadaşının oyununu kurtarmıştı"
   - Cümle 12: «Doru çok sevindi, çünkü arkadaşının oyununu kurtarmıştı.»
   - Açıklama: 'Oyunu kurtarmak' mecazlı ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0011` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 2aaac0ed0fd262112bb8fbd2e0d1a4bb6f1d2a8a`, sonra gövde.
