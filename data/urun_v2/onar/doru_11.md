# Editör görevi (onarım): Doru, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0034 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0034
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çit', fiil 'doğmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: bir kayanın arkasından garip bir ses geliyordu | sesi bulup fidanın üstündeki kuru dalı çekti
@tohum: doru-0034
@degisim: çit -> fidan
Bir sabah güneş dağın arkasından doğdu. Doru çimen yerken garip bir tak tak sesi duydu. Ses büyük bir kayanın arkasından geliyordu ve Doru onu çok merak etti. Kayanın arkasına yavaşça yürüdü ve baktı. Orada küçük bir fidan vardı. Fidanın üstüne kuru ve uzun bir dal düşmüştü. Rüzgar esince dal kayaya çarpıyor ve ses çıkarıyordu. Doru fidanı dalın altında görünce mutsuz oldu. Doru fidana yardım etmek istedi. Kuru dalı dişleriyle tuttu ve kenara çekti. Dal artık kayaya çarpmadı ve garip ses de bitti. Doru vadide çimen yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru fidana yardım etmek"
   - Cümle 9: «Doru fidana yardım etmek istedi.»
   - Açıklama: Art arda iki cümle gereksiz yere 'Doru' özneleriyle başlıyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru vadide çimen yemeye"
   - Cümle 12: «Doru vadide çimen yemeye mutlu mutlu devam etti.»
   - Açıklama: Hikaye dağda başlıyor ama vadide bitiyor; tek sahne kuralı belirsizleşiyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru vadide çimen yemeye mutlu mutlu devam etti"
   - Cümle 12: «Doru vadide çimen yemeye mutlu mutlu devam etti.»
   - Açıklama: Hikaye kayanın yanında geçerken son cümle Doru'yu sebepsizce vadiye taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0034` birebir aynı, `@degisim: çit -> fidan` (tutuyorsan), ardından `@onarim: 5b8165443f970aa89f9ad26000145e0baa28a25a`, sonra gövde.

### Hikâye 2: tohum doru-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0035
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'yün', fiil 'bağlamak', sıfat 'sevinçli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: oynarken annesinin sırtına çamur sıçradı | cesaretle özür diledi ve annesinin sırtını yıkadı
@tohum: doru-0035
@degisim: bağlamak -> yıkamak
Ormanda, bir çalıya biraz beyaz yün takılmıştı. Doru orada zıplayarak oynuyordu. Birden çamurlu bir yere bastı ve çamur annesinin sırtına sıçradı. Annesi başını çevirdi ve kirli sırtına baktı. Doru önce biraz utandı. Sonra cesaretle annesinin yanına gitti. "Özür dilerim, anne, daha dikkatli oynayacağım," dedi Doru. Annesi sevinçli bir sesle güldü. "Önemli değil, Doru, çamur suyla temizlenir," dedi annesi. Doru çalıdaki yünü dişleriyle aldı. İkisi birlikte yakındaki küçük dereye gitti. Doru yünü derede ıslattı ve annesinin sırtını yıkadı. Doru çok sevindi, çünkü annesinin sırtı yine tertemiz olmuştu.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "biraz beyaz yün takılmıştı"
   - Cümle 1: «Ormanda, bir çalıya biraz beyaz yün takılmıştı.»
   - Açıklama: Yün koyun ya da çiftlik dünyasını çağrıştırır ve kartın kapalı dünyasında böyle bir eşya yok.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bir çalıya biraz beyaz yün takılmıştı"
   - Cümle 1: «Ormanda, bir çalıya biraz beyaz yün takılmıştı.»
   - Açıklama: Yün kartın kapalı dünyasında olmayan, koyun ya da insan dünyasını çağrıştıran bir eşya olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0035` birebir aynı, `@degisim: bağlamak -> yıkamak` (tutuyorsan), ardından `@onarim: 21ad311d5c2053be6763883b1ad715a2fca02e41`, sonra gövde.

### Hikâye 3: tohum doru-0036 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0036
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'bambu', fiil 'seslenmek', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar en sevdiği dalı yokuştan aşağı yuvarladı | sürüye seslenip indi ve dalı çalıların arasında buldu
@tohum: doru-0036
@degisim: bambu -> dal
Rüzgar dağın üstünde esiyordu. Doru uzun bir dalı ağzıyla sallayarak oynuyordu. Bu dal onun en sevdiği oyuncağıydı. Birden rüzgar güçlendi ve dalı yokuştan aşağı yuvarladı. Doru dalı artık göremiyordu. Doru önce sürüye seslendi ve nereye gittiğini söyledi. Sonra yokuştan yavaş yavaş aşağı yürüdü. Dal, yokuşun dibindeki sık çalıların arasına girmişti. Çalıların arası biraz karanlıktı, ama Doru cesaretle başını uzattı. Dalı dişleriyle tuttu ve dışarı çekti. Dal çok sağlamdı ve hiç kırılmamıştı. Doru onu ağzında yukarı taşıdı. Doru çok sevindi, çünkü en sevdiği oyuncağını yeniden bulmuştu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve nereye gittiğini söyledi"
   - Cümle 6: «Doru önce sürüye seslendi ve nereye gittiğini söyledi.»
   - Açıklama: Henüz gitmediği için zaman uyumsuz; 'nereye gideceğini' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve nereye gittiğini söyledi"
   - Cümle 6: «Doru önce sürüye seslendi ve nereye gittiğini söyledi.»
   - Açıklama: Kimin nereye gittiği belli değil; dal mı Doru mu, ayrıca Doru henüz gitmediği için 'gideceğini' olmalı.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalıların arası biraz karanlıktı"
   - Cümle 9: «Çalıların arası biraz karanlıktı, ama Doru cesaretle başını uzattı.»
   - Açıklama: Karanlık çalıların arasına baş uzatmak küçük çocuk için korkutucu bir öğe olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0036` birebir aynı, `@degisim: bambu -> dal` (tutuyorsan), ardından `@onarim: 6a58de4f3341ba714c8e7597731d42681eb570f9`, sonra gövde.

### Hikâye 4: tohum doru-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0037
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çam', fiil 'bozulmak', sıfat 'zarif'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: rüzgar çiçekleri uçurdu ve sürpriz bozuldu | hızla koşup yeni papatyalar getirdi
@tohum: doru-0037
@degisim: zarif -> beyaz
Doru parkta, büyük bir çam ağacının altında duruyordu. Alaca çiçekleri çok severdi ve Doru ağacın altına onun için çiçek getirmişti. Ama birden rüzgar esti, çiçekler uçtu ve sürpriz bozuldu. Alaca da uzaktan ağaca doğru geliyordu. Çayırın öbür ucunda papatyalar vardı. Doru düz çayırda hızla koştu. Ağzıyla birçok papatya kopardı ve ağaca geri döndü. Tam o sırada Alaca geldi ve beyaz çiçeklere baktı. "Bunlar benim için mi, Doru?" diye sordu Alaca. "Evet, Alaca, hepsi senin," dedi Doru. Alaca sevinçle zıpladı. Doru da çok sevindi, çünkü sürprizini tam zamanında yeniden hazırlamıştı.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Doru parkta, büyük bir çam ağacının"
   - Cümle 1: «Doru parkta, büyük bir çam ağacının altında duruyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır ve dizide park yoktur; hikaye yeri park olarak adlandırıyor.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Doru parkta, büyük bir"
   - Cümle 1: «Doru parkta, büyük bir çam ağacının altında duruyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır ve dizide park yoktur; metin yeri 'park' diye adlandırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0037` birebir aynı, `@degisim: zarif -> beyaz` (tutuyorsan), ardından `@onarim: 9d94d424f31c093e2ac30342dbb42860c1d8f617`, sonra gövde.

### Hikâye 5: tohum doru-0038 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0038
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'paket', fiil 'rahatlatmak', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi | kozalağı dişleriyle çekip fidanı kurtardı
@tohum: doru-0038
@degisim: paket -> kozalak
Bir sabah gökyüzü mavi ve açıktı. Doru çayırda yuvarlak bir kozalağı burnuyla itip peşinden koşuyordu. Birden kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi. Doru fidana yardım etmek istedi. Kozalağı dişleriyle yavaşça tuttu ve dalların arasından çekti. Dallar kırılmadı ve fidan yeniden dik durdu. Dik duran fidan Doru'yu çok rahatlattı. Doru kozalağı dikkatlice çayırın ortasına götürdü. Oyununa açık çimenlerde yine neşeyle devam etti. Doru bundan sonra kozalağı fidanlardan uzakta itti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru çayırda yuvarlak bir kozalağı"
   - Cümle 2: «Doru çayırda yuvarlak bir kozalağı burnuyla itip peşinden koşuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor ve park hiç kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "fidan Doru'yu çok rahatlattı"
   - Cümle 7: «Dik duran fidan Doru'yu çok rahatlattı.»
   - Açıklama: Soyut 'rahatlatmak' fiili cansız özneyle 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Rahatlatmak' soyut bir duygu anlatımı ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0038` birebir aynı, `@degisim: paket -> kozalak` (tutuyorsan), ardından `@onarim: 4d5c1297232bb0b444da4efd113422e6f2342c33`, sonra gövde.

### Hikâye 6: tohum doru-0040 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0040
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'misket', fiil 'karışmak', sıfat 'kolay'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: sürü vadiye inmişti ve yerdeki izler karışmıştı | küçük arkadaşına yolu sordu ve sürüye yetişti
@tohum: doru-0040
@degisim: misket -> iz
Dağda serin bir rüzgar esiyordu. Doru ile Alaca büyük bir kayanın yanında oynuyordu. Oyun bitince Doru etrafına baktı ama sürü vadiye inmişti. Yerde çok iz vardı ve bütün izler birbirine karışmıştı. Doru hangi yoldan gideceğini bilemedi. "Alaca, sürü hangi yoldan indi, gördün mü?" diye sordu Doru. "Evet, sarı çiçekli yoldan indiler, bulmak çok kolay," dedi Alaca. İkisi o yoldan birlikte yavaşça indi. Aşağıda geniş ve düz bir vadi vardı. Sürü onun öbür ucunda çimen yiyordu. Doru orada hızla koştu, Alaca da arkasından geldi. Az sonra ikisi de sürünün yanındaydı. "Teşekkürler, Alaca, yolu sen buldun!" dedi Doru.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru orada hızla koştu"
   - Cümle 11: «Doru orada hızla koştu, Alaca da arkasından geldi.»
   - Açıklama: Sürüye doğru koşmak yönelme eki ister; 'oraya' olmalı.
   - Açıklama: Yön bildiren fiille bulunma eki kullanılmış; 'oraya koştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0040` birebir aynı, `@degisim: misket -> iz` (tutuyorsan), ardından `@onarim: c9849231381602e1fe5cd3eddeb99ff327920e19`, sonra gövde.

### Hikâye 7: tohum doru-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0042
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çim', fiil 'küçültmek', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: çayırın kenarından garip bir ses geldi | sesi bulup kuru dalı uzağa çekti
@tohum: doru-0042
@degisim: küçültmek -> çekmek
Bir sabah Doru geniş çayırda çim yiyordu. Yağmurdan sonra her yer temiz ve yeşildi. Birden çayırın kenarından garip bir ses geldi. Doru bu sesin nereden geldiğini çok merak etti. Yavaşça çayırın kenarına yürüdü. Orada genç bir fidan vardı. Fidanın yanına kuru bir dal düşmüştü. Rüzgar esince dal fidana sürtünüyor ve ses çıkarıyordu. Dal, fidanın ince yapraklarını koparıyordu. Doru fidana yardım etmek istedi. Kuru dalı dişleriyle tuttu ve uzağa çekti. Rüzgar yine esti ama ses gelmedi. Doru çok sevindi ve çayırda çim yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru geniş çayırda çim yiyordu"
   - Cümle 1: «Bir sabah Doru geniş çayırda çim yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor ve park hiç anılmıyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor ve park hiç kurulmuyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Dal, fidanın ince yapraklarını koparıyordu"
   - Cümle 9: «Dal, fidanın ince yapraklarını koparıyordu.»
   - Açıklama: Asıl sorun olan fidanın zarar görmesi ancak 9. cümlede söyleniyor; ilk üç cümlede yalnız garip bir ses var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0042` birebir aynı, `@degisim: küçültmek -> çekmek` (tutuyorsan), ardından `@onarim: 9737d8ea0f3f061ea0ba6711b26c330daceb68df`, sonra gövde.

### Hikâye 8: tohum doru-0043 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0043
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çadır', fiil 'kaplamak', sıfat 'gri'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: yağmur geliyordu ama sürünün bilge atı uyuyordu | onu uyandırıp birlikte kayanın altına gitti
@tohum: doru-0043
@degisim: çadır -> bulut
Bir sabah gri bulutlar dağın üstünü kapladı. Doru yağmurun geleceğini anladı. Ama Kırat vadinin ucunda bir ağacın altında uyuyordu ve bulutları görmemişti. Doru, Kırat'ın ıslanmasını istemedi ve ona yardım etmek için yanına gitti. "Kırat, uyan, yağmur geliyor!" dedi Doru. Kırat gözlerini açtı ve gökyüzüne baktı. "Haklısın, Doru, hadi büyük kayaya gidelim," dedi Kırat. İkisi kayanın altına birlikte yürüdü. Az sonra yağmur yağmaya başladı. Kayanın altı kuruydu ve ikisi hiç ıslanmadı. Kırat, Doru'ya dönüp gülümsedi. "Teşekkürler, Doru, iyi ki beni uyandırdın!" dedi Kırat.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "hadi büyük kayaya gidelim"
   - Cümle 7: «"Haklısın, Doru, hadi büyük kayaya gidelim," dedi Kırat.»
   - Açıklama: Kuru yere gitme çözümünü figür Doru değil yan karakter Kırat öneriyor.
   - Açıklama: Sığınma yerini figür Doru değil yan karakter Kırat buluyor; çözümün bir parçasını yan karakter getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0043` birebir aynı, `@degisim: çadır -> bulut` (tutuyorsan), ardından `@onarim: 44d01e6da3dff3c09abe4a6e19c04d42c999bdc3`, sonra gövde.

### Hikâye 9: tohum doru-0044 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0044
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gümüş', fiil 'kalmak', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: karanlık çalıların arkasında bir şey parlıyordu | cesaretle gidip parlayan çiçeği buldu
@tohum: doru-0044
Yağmur yeni dinmişti ve ormanda hafif bir rüzgar esiyordu. Doru annesiyle ağaçların arasında yürüyordu. Birden karanlık çalıların arkasında gümüş renkli bir parıltı gördü. Doru orada ne olduğunu çok merak etti. "Anne, orada parlayan ne?" diye sordu Doru. "Bilmiyorum, gidip bakabilirsin," dedi annesi. Doru cesaretle çalıların arkasına yürüdü. İki taşın arasında narin, beyaz bir çiçek vardı. Yapraklarındaki yağmur damlaları ışıl ışıl parlıyordu. "Anne, gel, bu bir çiçek!" dedi Doru. Annesi hemen yanına geldi ve çiçeğe baktı. Doru çiçeğe hiç basmadı ve çiçek yerinde kaldı. Doru çok sevindi, çünkü parlayan şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "karanlık çalıların arkasında gümüş renkli bir parıltı gördü"
   - Cümle 3: «Birden karanlık çalıların arkasında gümüş renkli bir parıltı gördü.»
   - Açıklama: Parlayan bir şeyi merak etmek gerçek bir sorun değil; ortada çözülmesi gereken bir dert yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "narin, beyaz bir çiçek"
   - Cümle 8: «İki taşın arasında narin, beyaz bir çiçek vardı.»
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmediği bir kelime.
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru çiçeğe hiç basmadı ve çiçek yerinde kaldı"
   - Cümle 12: «Doru çiçeğe hiç basmadı ve çiçek yerinde kaldı.»
   - Açıklama: Çiçeğe basmamak daha önce kurulmamış, işlevsiz bir ayrıntı.
   - Açıklama: Çiçeğe basma tehlikesi hiç kurulmadığı için bu cümle işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0044` birebir aynı, ardından `@onarim: 26b743c22ebaa5019b12b413bc2213ff7d2d421c`, sonra gövde.

### Hikâye 10: tohum doru-0045 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0045
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'havuç', fiil 'takmak', sıfat 'buzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: elma buzlu dalların altındaydı ve dallar ses çıkarıyordu | cesaretle gidip elmayı aldı ve paylaştı
@tohum: doru-0045
@degisim: havuç -> elma
Bir sabah orman soğuk ve sessizdi. Doru ile Karatay acıkmıştı ve yiyecek arıyordu. Bir çalının altında kırmızı bir elma gördüler ama Karatay çalıya yaklaşmadı. Çalının dalları buzluydu ve rüzgarda çıt çıt ses çıkarıyordu. Doru cesaretle çalıya yürüdü ve dallara baktı. Sesi yalnız ince buzlar çıkarıyordu. Doru elmayı dişleriyle tuttu ve dışarı çekti. Ama orada tek bir elma vardı. "Karatay, bunu birlikte yiyelim," dedi Doru. Karatay güldü ve elmaya "kırmızı top" adını taktı. Doru elmayı ısırdı ve ikiye böldü. İkisi elmayı yavaş yavaş yedi. Doru çok mutlu oldu, çünkü elmayı en yakın arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Çalının dalları buzluydu ve rüzgarda çıt çıt ses çıkarıyordu"
   - Cümle 4: «Çalının dalları buzluydu ve rüzgarda çıt çıt ses çıkarıyordu.»
   - Açıklama: Sorunun ne olduğu ancak 4. cümlede anlaşılıyor; ilk üç cümlede Karatay'ın neden yaklaşmadığı söylenmiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama orada tek bir elma vardı."
   - Cümle 8: «Ama orada tek bir elma vardı.»
   - Açıklama: 'Ama' bağlacı önceki cümleyle karşıtlık kurmuyor; yanlış anlamda kullanılmış.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama orada tek bir elma vardı"
   - Cümle 8: «Ama orada tek bir elma vardı.»
   - Açıklama: Korku sorunu çözüldükten sonra tek elmayı paylaşma diye ikinci bir sorun açılıyor.
   - Açıklama: Korku sorunu çözüldükten sonra tek elma ikinci bir sorun olarak açılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elmaya "kırmızı top" adını taktı"
   - Cümle 10: «Karatay güldü ve elmaya "kırmızı top" adını taktı.»
   - Açıklama: Elmaya ad takılması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Elmaya ad takılması işlevsiz bir ayrıntı ve hiçbir yere bağlanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0045` birebir aynı, `@degisim: havuç -> elma` (tutuyorsan), ardından `@onarim: 9277a749886d37b765020fc97068ee5811ecad19`, sonra gövde.

### Hikâye 11: tohum doru-0046 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0046
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'üzüm', fiil 'sığmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: kar çimenlerin üstünü kapladı ve yiyecek yoktu | cesaretle karda yürüyüp kayanın altına sığdı
@tohum: doru-0046
@degisim: üzüm -> ot
Dağda lapa lapa kar yağıyordu. Kar bütün çimenlerin üstündeydi ve Doru yiyecek bulamıyordu. Uzakta büyük bir kaya gördü. Ama arada yumuşak kar vardı ve bu Doru'nun ilk karıydı. Doru cesaretle karın içine adım attı. Ayakları karda küçük izler bıraktı. Yavaş yavaş kayanın yanına vardı. Kayanın altında kuru ve küçük bir yer buldu. Doru başını eğdi ve o yere sığdı. Yerde kuru otlar duruyordu. Doru otları afiyetle yedi. Dışarıda kar yağıyordu ama kayanın altı huzurluydu. Doru karnını doyurdu ve orada mutlu mutlu dinlendi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayanın altına sığdı"
   - Cümle 0 (plan satırı): «kar çimenlerin üstünü kapladı ve yiyecek yoktu | cesaretle karda yürüyüp kayanın altına sığdı»
   - Açıklama: 'Sığdı' yanlış anlamda; barınmak için 'sığındı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o yere sığdı"
   - Cümle 9: «Doru başını eğdi ve o yere sığdı.»
   - Açıklama: 'Sığdı' yanlış anlamda kullanılmış; 'sığındı' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yerde kuru otlar duruyordu"
   - Cümle 10: «Yerde kuru otlar duruyordu.»
   - Açıklama: Kuru otlar kayanın altında sebepsizce beliriyor ve çözümü tesadüfe bırakıyor; Doru kayaya yiyecek bulmak için gittiği söylenmiyor.
   - Açıklama: Doru kayaya yiyecek için değil sığınmak için gidiyor ve kuru otlar çözümü sebepsizce getiriyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kayanın altı huzurluydu"
   - Cümle 12: «Dışarıda kar yağıyordu ama kayanın altı huzurluydu.»
   - Açıklama: 'Huzurlu' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Huzurlu' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0046` birebir aynı, `@degisim: üzüm -> ot` (tutuyorsan), ardından `@onarim: c99d5982fef5580fb26993411c7ec785d85ee519`, sonra gövde.

### Hikâye 12: tohum doru-0047 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0047
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'marul', fiil 'barışmak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar esti ve marul yokuştan yuvarlandı | gölgeli ağacın arkasına cesaretle gidip marulu buldu
@tohum: doru-0047
@degisim: barışmak -> yuvarlanmak
Dağda sert bir rüzgar esiyordu. Doru kayaların arasında bulduğu taze bir marulu yiyordu. Birden rüzgar yine esti ve marul yokuştan aşağı yuvarlandı. Doru marulu aramak için yokuştan yavaşça indi. Aşağıda yamuk bir ağaç vardı. Ağacın arkası gölgeliydi ve dallar rüzgarda garip sesler çıkarıyordu. Doru bir an durdu. Sonra cesaretle ağacın arkasına yürüdü. Marul orada, iki kökün arasında duruyordu. Doru marulu buldu ve çok sevindi. Doru bundan sonra rüzgarlı havada yemeğini bir kayanın dibinde yedi.
```

**Hakem bulguları (5):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "taze bir marulu yiyordu"
   - Cümle 2: «Doru kayaların arasında bulduğu taze bir marulu yiyordu.»
   - Açıklama: Kartın kapalı doğa dünyasında ekili bir sebze olan marul yok; dağda marul bulunması kart dünyasına aykırı.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bulduğu taze bir marulu"
   - Cümle 2: «Doru kayaların arasında bulduğu taze bir marulu yiyordu.»
   - Açıklama: Kartın doğa dünyasında (özgür at sürüsü, dağ) ekili bir sebze olan marul yer almıyor.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "dallar rüzgarda garip sesler çıkarıyordu"
   - Cümle 6: «Ağacın arkası gölgeliydi ve dallar rüzgarda garip sesler çıkarıyordu.»
   - Açıklama: Gölgeli ağaç arkası ve garip seslerle küçük çocuk için ürkütücü bir öğe kuruluyor.
   - Açıklama: Gölgeli ağacın arkasından gelen açıklanmayan garip sesler küçük çocuk için ürkütücü.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "dallar rüzgarda garip sesler çıkarıyordu"
   - Cümle 6: «Ağacın arkası gölgeliydi ve dallar rüzgarda garip sesler çıkarıyordu.»
   - Açıklama: Kayan marul sorununa gölgeli ağaçtan korkma diye ikinci bir sorun ekleniyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru bundan sonra rüzgarlı havada yemeğini bir kayanın dibinde yedi"
   - Cümle 11: «Doru bundan sonra rüzgarlı havada yemeğini bir kayanın dibinde yedi.»
   - Açıklama: 'Bundan sonra' alışkanlık bildirir; 'yedi' yerine 'yerdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0047` birebir aynı, `@degisim: barışmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 49aeab1930812846d40682e8116c017f455a8144`, sonra gövde.
