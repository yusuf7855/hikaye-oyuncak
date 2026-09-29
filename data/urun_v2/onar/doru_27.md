# Editör görevi (onarım): Doru, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0070 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0070
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gölge', fiil 'anlatmak', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yağmur başladı ve yakında hiç ağaç yoktu | cesaretle yağmurda yürüyüp büyük kayanın altına girdi
@tohum: doru-0070
@degisim: anlatmak -> saklanmak
Dağda güneş vardı ve Doru tek başına çimen yiyordu. Birden Doru'nun gölgesi kayboldu, çünkü bulutlar gelmişti. Sonra yağmur başladı ve Doru'nun sırtı ıslandı. Yakında hiç ağaç yoktu. Eskimiş küçük bir kütük vardı ama Doru'yu yağmurdan koruyamazdı. Biraz ileride büyük bir kaya vardı. Yağmur çok yağıyordu ama Doru cesaretle kayaya kadar yürüdü. Kayanın bir yanı öne çıkmıştı ve altı kuruydu. Doru oraya girdi ve daha fazla ıslanmadı. Bir süre sonra bulutlar gitti ve güneş çıktı. Doru oradan çıktı ve yeniden çimen yemeye başladı. Doru bundan sonra yağmur başlayınca o kayanın altına saklandı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Eskimiş küçük bir kütük vardı"
   - Cümle 5: «Eskimiş küçük bir kütük vardı ama Doru'yu yağmurdan koruyamazdı.»
   - Açıklama: Kütük kurulup hiçbir işe yaramıyor; işlevsiz ayrıntı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "o kayanın altına saklandı"
   - Cümle 12: «Doru bundan sonra yağmur başlayınca o kayanın altına saklandı.»
   - Açıklama: 'Bundan sonra ... başlayınca' alışkanlık bildiriyor; 'saklanırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0070` birebir aynı, `@degisim: anlatmak -> saklanmak` (tutuyorsan), ardından `@onarim: c9084ebd3ac0d9fe0a242f52f4141b4269d1d26d`, sonra gövde.

### Hikâye 2: tohum doru-0072 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0072
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'taş', fiil 'sıkılmak', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sürü uyuyordu ve oynayacak kimse yoktu | çalıların arkasına bakıp damlayan suyu buldu ve oynadı
@tohum: doru-0072
Bir ses geliyordu: tık, tık. Sürüdeki atlar uyuyordu ve Doru ormanda tek başına sıkılmıştı. Oynayacak bir şey arıyordu. Ses yakındaki çalıların arkasından geliyordu ve Doru onu çok merak etti. Doru çalıların yanından dolaştı ve arkaya baktı. Arkada büyük, düz bir taş vardı. Yukarıdaki kayalardan ince bir su iniyordu. Her damla taşa düşünce tık diye ses çıkarıyordu. Doru cesaretle suyun altına girdi ve sırılsıklam oldu. Serin su Doru'yu çok güldürdü. Doru artık sıkılmıyordu, çünkü suyla yeni bir oyun bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayalardan ince bir su iniyordu"
   - Cümle 7: «Yukarıdaki kayalardan ince bir su iniyordu.»
   - Açıklama: Su 'inmez', akar ya da damlar; sonraki cümledeki damlalarla da uyuşmuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle suyun altına girdi ve sırılsıklam oldu"
   - Cümle 9: «Doru cesaretle suyun altına girdi ve sırılsıklam oldu.»
   - Açıklama: Tek başına kayalardan inen suyun altına girip sırılsıklam olmak çocuğun taklit edebileceği riskli bir davranış.
   - Açıklama: Kayalardan inen suyun altına girip sırılsıklam olmak çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0072` birebir aynı, ardından `@onarim: 2258a7394c2205ddd33c88d0d3c1421977ab17db`, sonra gövde.

### Hikâye 3: tohum doru-0078 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0078
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'buz', fiil 'katmak', sıfat 'puantiyeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: gölet buzla kaplıydı ve arkadaşı su içemedi | ıslak izleri görüp ağacın altında su buldu
@tohum: doru-0078
@degisim: puantiyeli -> yuvarlak
Bir sabah ormandaki küçük gölet buzla kaplıydı. Doru'nun arkadaşı Karatay çok susamıştı ama buzdan su içemiyordu. Doru ona yardım etmek için etrafa baktı. Uzaktaki bir ağacın altında, karda yuvarlak ve ıslak izler gördü. Doru bunları merak etti ve Karatay'ı da yanına kattı. İkisi ağaca yürüdü. Ağacın dallarında buzlar vardı ve güneşte eriyordu. Damlalar tek tek karın üstüne düşüyordu. İzleri bu damlalar yapmıştı. Ağacın altında çukur bir taş vardı ve içi suyla doluydu. Karatay soğuk suyu keyifle içti. Doru çok sevindi, çünkü arkadaşına su bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay'ı da yanına kattı"
   - Cümle 5: «Doru bunları merak etti ve Karatay'ı da yanına kattı.»
   - Açıklama: 'Yanına katmak' kalıp bir deyim; küçük çocuk için 'yanına aldı' denmeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0078` birebir aynı, `@degisim: puantiyeli -> yuvarlak` (tutuyorsan), ardından `@onarim: 7eb3c831aa4aa6929b609a6b31e62a27197a29b5`, sonra gövde.

### Hikâye 4: tohum doru-0081 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0081
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'oyuncak', fiil 'tatmak', sıfat 'düzenli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yakındaki çalıda yalnız yeşil çilekler vardı | açıklıkta hızla koştu ve kırmızı çilek getirdi
@tohum: doru-0081
@degisim: oyuncak -> çilek
Bir sabah Kırat ormanda bir ağacın altında uyuyordu. Doru onu sevindirmek için çilek toplamak istedi. Ama yakındaki çalıda yalnız üç çilek vardı ve hepsi daha yeşildi. Kırmızı çilekler ise ormanın öbür ucundaki geniş açıklıktaydı. Doru ağaçların arasından yavaşça geçti ve açıklıkta hızla koştu. Çilekli bir dalı ağzıyla kopardı ve geri döndü. Çilekleri düz bir taşın üstüne düzenli bir sırayla dizdi. Kırat gözlerini açtı ve taşa baktı. "Bunlar benim için mi, Doru?" diye sordu Kırat. "Hepsi senin için!" dedi Doru. Kırat bir çilek tattı ve gülümsedi. "Çok tatlı, teşekkürler, Doru," dedi Kırat. Doru bundan sonra yeşil çilekleri değil, kırmızı çilekleri toplardı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hepsi daha yeşildi"
   - Cümle 3: «Ama yakındaki çalıda yalnız üç çilek vardı ve hepsi daha yeşildi.»
   - Açıklama: 'Daha' burada 'henüz' anlamında kullanılmış ve 'daha çok yeşil' diye yanlış anlaşılabiliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve hepsi daha yeşildi"
   - Cümle 3: «Ama yakındaki çalıda yalnız üç çilek vardı ve hepsi daha yeşildi.»
   - Açıklama: 'Daha' burada 'henüz' anlamında kullanılmış ve 'daha yeşil' karşılaştırması gibi okunuyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "ormanın öbür ucundaki geniş açıklıktaydı"
   - Cümle 4: «Kırmızı çilekler ise ormanın öbür ucundaki geniş açıklıktaydı.»
   - Açıklama: Doru ormanın öbür ucuna gidip dönüyor; hikaye tek sahnede kalmıyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Doru bundan sonra yeşil çilekleri değil, kırmızı çilekleri toplardı"
   - Cümle 13: «Doru bundan sonra yeşil çilekleri değil, kırmızı çilekleri toplardı.»
   - Açıklama: Doru hiç yeşil çilek toplamadığı için son ders yaşanan olaydan çıkmıyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Doru bundan sonra yeşil çilekleri değil"
   - Cümle 13: «Doru bundan sonra yeşil çilekleri değil, kırmızı çilekleri toplardı.»
   - Açıklama: Doru hikayede hiç yeşil çilek toplamadığı için son ders cümlesi yaşanan olaydan çıkmıyor ve sıcak kapanışı bozuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0081` birebir aynı, `@degisim: oyuncak -> çilek` (tutuyorsan), ardından `@onarim: a8e2c27ca562da60114309b4104507420678c088`, sonra gövde.

### Hikâye 5: tohum doru-0082 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0082
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: paylaşmak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'mercan', fiil 'tanımak', sıfat 'kırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşının hiç elması yoktu | iki elmadan birini arkadaşına verdi
@tohum: doru-0082
@degisim: mercan -> elma
Geniş parkta kuşlar ötüyordu. Doru bir ağacın altında iki kırmızı elma buldu. Küçük Alaca da geldi ama ağaçta başka elma kalmamıştı. Alaca kırmızı elmaları tanımıyordu ve merakla baktı. "Doru, bunlar ne?" diye sordu Alaca. "Bunlar elma, çok tatlıdır," dedi Doru. Doru Alaca'ya yardım etmek istedi. Elmalardan birini burnuyla Alaca'nın önüne itti. "Bu elma senin, Alaca," dedi Doru. Alaca elmayı yavaşça ısırdı ve sevinçle zıpladı. "Çok güzelmiş, teşekkürler," dedi Alaca. İki at elmalarını yan yana yedi. Doru çok sevindi, çünkü elmasını Alaca ile paylaşmıştı.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Geniş parkta kuşlar ötüyordu"
   - Cümle 1: «Geniş parkta kuşlar ötüyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayır; metin yeri insan yapımı bir park olarak anıyor ve dizide park yok.
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; hikaye yeri çayır olarak değil insan parkı olarak sunuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Alaca kırmızı elmaları tanımıyordu ve merakla baktı"
   - Cümle 4: «Alaca kırmızı elmaları tanımıyordu ve merakla baktı.»
   - Açıklama: Alaca'nın elmayı tanımaması sorunla ilgisiz ikinci bir iplik olarak kuruluyor ve çözüme bir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0082` birebir aynı, `@degisim: mercan -> elma` (tutuyorsan), ardından `@onarim: 155d13b58665f23104a49f299dd108120937050d`, sonra gövde.

### Hikâye 6: tohum doru-0087 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0087
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'örtü', fiil 'görüşmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: rüzgar topu yaprakların altına itti ve top kayboldu | cesaretle kuru yaprakların üstünde yürüdü ve topu buldu
@tohum: doru-0087
@degisim: görüşmek -> yuvarlamak
Parkta rüzgar esiyordu. Doru kocaman bir ot topuyla oynuyordu. Topu burnuyla yuvarlıyor ve peşinden koşuyordu. Ama rüzgar birden güçlendi ve hafif topu ağaçlara doğru itti. Ağaçların altını kalın bir kuru yaprak örtüsü kaplıyordu. Top bu yaprakların altına girdi ve kayboldu. Doru hemen oraya gitti. Kuru yapraklar ayaklarının altında yüksek sesle çıtırdadı. Doru bir an durdu ama cesaretle yaprakların üstünde yürüdü. Burnuyla yaprakları itti ve topunu buldu. Onu yeniden parkın ortasına yuvarladı. Doru kocaman topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Doru kocaman bir ot topuyla oynuyordu"
   - Cümle 2: «Doru kocaman bir ot topuyla oynuyordu.»
   - Açıklama: Kartın kapalı dünyasında Doru'nun oyuncak topla oynaması yok; top karta eklenmiş bir eşya.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Topu burnuyla yuvarlıyor ve peşinden koşuyordu.»
   - Açıklama: İlk üç cümle yalnız oyunu anlatıyor; sorun ancak 4. ve 6. cümlede ortaya çıkıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kalın bir kuru yaprak örtüsü"
   - Cümle 5: «Ağaçların altını kalın bir kuru yaprak örtüsü kaplıyordu.»
   - Açıklama: 'Yaprak örtüsü' mecazlı ve küçük çocuk için zor bir anlatım.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Top bu yaprakların altına girdi ve kayboldu"
   - Cümle 6: «Top bu yaprakların altına girdi ve kayboldu.»
   - Açıklama: Kocaman diye anlatılan top yaprak örtüsünün altında görünmez oluyor; bu kendi içinde çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0087` birebir aynı, `@degisim: görüşmek -> yuvarlamak` (tutuyorsan), ardından `@onarim: 7691cce51ffe042ee429666fb96b4e03017742f7`, sonra gövde.

### Hikâye 7: tohum doru-0091 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0091
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'turp', fiil 'asmak', sıfat 'güçlü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: turp yuvarlandı ve karanlık bir çalının altına girdi | korkmadan turpu çalının altından dişleriyle çıkardı
@tohum: doru-0091
@degisim: asmak -> saklamak
Ormanda Doru ile Alaca topraktan çıkan küçük bir turpla oynuyordu. İkisi turpu sırayla saklıyordu. Sıra Alaca'daydı ve Alaca turpu yokuşta bir taşın arkasına koydu. Ama turp aşağı yuvarlandı ve sık bir çalının altına girdi. Çalının altı karanlıktı ve Alaca yaklaşmaya korktu. "Doru, oyunumuz bitti mi?" diye sordu Alaca. "Hayır, Alaca, ben çıkarırım," dedi Doru. Doru cesaretle çalının yanına gitti ve eğildi. Güçlü dişleriyle turpu tuttu ve dışarı çekti. Alaca sevinçle zıpladı. "Sıra sende, Doru," dedi Alaca. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Sıra Alaca'daydı ve Alaca turpu yokuşta bir taşın arkasına koydu.»
   - Açıklama: Turpun çalının altına girmesi ancak 4. cümlede söyleniyor; ilk 3 cümlede sorun yok.
   - Açıklama: Turpun çalının altına girmesi ancak 4. cümlede söyleniyor, ilk 3 cümlede sorun yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Güçlü dişleriyle turpu tuttu"
   - Cümle 9: «Güçlü dişleriyle turpu tuttu ve dışarı çekti.»
   - Açıklama: Tohumdaki özellik cesaret; güç ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0091` birebir aynı, `@degisim: asmak -> saklamak` (tutuyorsan), ardından `@onarim: c5d0bdaa76e94c4722033be2807d37e068db1d1e`, sonra gövde.

### Hikâye 8: tohum doru-0092 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0092
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'böğürtlen', fiil 'susmak', sıfat 'neşeli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: rüzgar çok gürültülüydü ve şarkının bittiğini duymadı | annesinden şarkı bitince başını sallamasını istedi
@tohum: doru-0092
Bir sabah Doru ile annesi geniş parkta neşeli bir oyun oynuyordu. Annesi şarkı söylerken Doru koşuyor, şarkı bitince duruyordu. Ama rüzgar çok gürültülüydü ve Doru annesini duymadı. Doru durmadı ve böğürtlen çalısına kadar koştu. Annesi güldü. "Doru, şarkı bitti ama sen koşuyordun!" dedi annesi. Doru gülümsedi ve biraz düşündü. "Anne, şarkı bitince başını da salla," dedi Doru. Annesi yeniden şarkıya başladı ve Doru hızla koştu. Sonra annesi birden sustu ve başını salladı. Doru bunu hemen gördü ve tam yerinde durdu. "Aferin, Doru!" dedi annesi ve çalıdan ona bir böğürtlen verdi. Doru bundan sonra rüzgar esince annesini dikkatle izlerdi.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "geniş parkta neşeli bir oyun"
   - Cümle 1: «Bir sabah Doru ile annesi geniş parkta neşeli bir oyun oynuyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayır; metin yeri insan yapımı bir park olarak anıyor ve dizide park yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru hızla koştu"
   - Cümle 9: «Annesi yeniden şarkıya başladı ve Doru hızla koştu.»
   - Açıklama: Tohumdaki hız özelliği sorunu çözmüyor; sorun annenin başını sallamasıyla çözülüyor, yani özellik işe yarar biçimde kullanılmamış.
   - Açıklama: Tohumdaki hız özelliği sorunu çözmekte işe yaramıyor; sorun annenin başını sallamasıyla çözülüyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru bunu hemen gördü"
   - Cümle 11: «Doru bunu hemen gördü ve tam yerinde durdu.»
   - Açıklama: Doru annesinden uzağa koşarken annesinin başını salladığını hemen görmesi çelişkili görünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0092` birebir aynı, ardından `@onarim: 2ab7ac1e3b6e98835cd12f28251711614a0b238c`, sonra gövde.

### Hikâye 9: tohum doru-0093 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0093
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'koni', fiil 'çözmek', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: rüzgar yolun üstüne uzun bir dal düşürdü | otları dişleriyle çözdü ve dalı yolun kenarına çekti
@tohum: doru-0093
@degisim: koni -> çiçek
Doru ormanda yol koruma oyunu oynuyordu. Birden rüzgar esti ve uzun, çiçekli bir dal yolun üstüne düştü. Artık sürüdeki küçük atlar oradan geçemezdi. Doru onlara yardım etmek istedi. Dalın ucuna uzun otlar dolanmıştı ve dal yerinden kıpırdamıyordu. Üstünde küçük mor çiçekler vardı ve Doru onları koparmak istemedi. Doru otları dişleriyle tuttu ve yavaşça çözdü. Sonra dalı ağzıyla yolun kenarına çekti. Mor çiçeklerin hiçbiri düşmedi. Artık yol küçük atlar için güvenliydi. Doru çok sevindi, çünkü oyununda sürünün yolunu korumuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Üstünde küçük mor çiçekler vardı ve Doru onları koparmak istemedi"
   - Cümle 6: «Üstünde küçük mor çiçekler vardı ve Doru onları koparmak istemedi.»
   - Açıklama: Mor çiçekler önemli bir engel gibi kuruluyor ama çözümde hiçbir işlev görmüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Üstünde küçük mor çiçekler vardı"
   - Cümle 6: «Üstünde küçük mor çiçekler vardı ve Doru onları koparmak istemedi.»
   - Açıklama: Çiçekler çözümü etkilemeyen, olayın akışından çıkmayan ek bir ayrıntı olarak kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0093` birebir aynı, `@degisim: koni -> çiçek` (tutuyorsan), ardından `@onarim: cd83cab78082cf5047596c7405594f3fef22b0f2`, sonra gövde.

### Hikâye 10: tohum doru-0096 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0096
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'düğme', fiil 'tanıştırmak', sıfat 'rengarenk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: koşarken küçük çiçeklerin üstüne basıp onları eğdi | cesurca özür diledi ve çiçekleri burnuyla kaldırdı
@tohum: doru-0096
@degisim: tanıştırmak -> dilemek
Hafif bir rüzgar esiyordu ve Doru ormanda oynuyordu. Kırat bir ağacın altında, küçük ve rengarenk düğme çiçeklerine bakıyordu. Doru koşup geldi ve çiçeklerin üstüne bastı. Çiçeklerin çoğu yere doğru eğildi. Kırat buna çok üzüldü. Doru önce biraz utandı ve saklanmak istedi. Sonra cesurca Kırat'ın yanına gitti. "Özür dilerim, Kırat, çiçekleri görmedim," dedi Doru. "Teşekkürler, Doru," dedi Kırat gülümseyerek. Doru eğilmiş çiçekleri burnuyla tek tek kaldırdı. Hepsi yeniden güneşe doğru döndü. Sonra Doru çiçeklerin yanından dikkatle geçti ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "rengarenk düğme çiçeklerine bakıyordu"
   - Cümle 2: «Kırat bir ağacın altında, küçük ve rengarenk düğme çiçeklerine bakıyordu.»
   - Açıklama: 'Düğme çiçeği' 3 yaşındaki bir çocuğun bilmediği, büyük olasılıkla yanlış bir çiçek adıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0096` birebir aynı, `@degisim: tanıştırmak -> dilemek` (tutuyorsan), ardından `@onarim: 0882127d4e1e48000d72ad6c2147985f451744f2`, sonra gövde.

### Hikâye 11: tohum doru-0097 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0097
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'damla', fiil 'taşmak', sıfat 'boyalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: gölet taştı ve su renkli tüyü götürdü | suyun peşinden gidip tüyü çalıda buldu
@tohum: doru-0097
@degisim: boyalı -> renkli
Doru dağda otlarken yapraklardan son yağmur damlaları düşüyordu. Birden Alaca üzgün üzgün yanına geldi. "Doru, gölet taştı ve su bulduğum renkli tüyü götürdü," dedi Alaca. Doru hemen Alaca'ya yardım etmek istedi. İkisi birlikte göletin yanına gitti. Göletin suyu çimenlerin arasından aşağı akıyordu. Doru suyun peşinden dikkatle yürüdü. Aşağıda küçük bir çalı vardı. Renkli tüy, çalının dalına takılmıştı. Doru tüyü dişleriyle yavaşça aldı ve Alaca'ya verdi. Alaca sevinçle zıpladı. "Teşekkürler, Doru, sen olmasan onu hiç bulamazdım!" dedi Alaca.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Renkli tüy, çalının dalına"
   - Cümle 9: «Renkli tüy, çalının dalına takılmıştı.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0097` birebir aynı, `@degisim: boyalı -> renkli` (tutuyorsan), ardından `@onarim: ad1e3a7f7172619b4ad8fccb0b7ad58840bcd649`, sonra gövde.

### Hikâye 12: tohum doru-0098 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0098
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'bilye', fiil 'boşalmak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: ağacın alçak dallarında hiç kiraz kalmamıştı | dar yoldan cesaretle geçip kiraz buldu ve paylaştı
@tohum: doru-0098
@degisim: bilye -> kiraz
Doru annesiyle ormandaki büyük kiraz ağacının altına geldi. Ama ağacın alçak dalları boşalmıştı, çünkü kirazların hepsi yenmişti. İkisinin de karnı çok açtı. Doru çevresine baktı. Ağaçların arasındaki dar bir yolun sonunda küçük bir kiraz ağacı gördü. Yolu uzun otlar kapatmıştı. "Hazırlıklı mısın, Doru?" diye sordu annesi. Doru cesaretle öne geçti ve otların arasından yürüdü. Annesi de arkasından geldi. Küçük ağaçta yuvarlak, kırmızı kirazlar vardı. Doru kirazlı bir dalı ağzıyla kopardı ve annesinin önüne koydu. "Anneciğim, bunları birlikte yiyelim," dedi Doru. Annesi gülümsedi ve kirazların yarısını aldı. Doru da öbür yarısını yedi. Paylaşınca Doru'nun da annesinin de karnı doydu.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çünkü kirazların hepsi yenmişti"
   - Cümle 2: «Ama ağacın alçak dalları boşalmıştı, çünkü kirazların hepsi yenmişti.»
   - Açıklama: Yalnız alçak dalların boşaldığı söyleniyor ama sebep olarak kirazların hepsinin yendiği söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Hazırlıklı mısın, Doru?""
   - Cümle 7: «"Hazırlıklı mısın, Doru?" diye sordu annesi.»
   - Açıklama: 'Hazırlıklı' kelimesi 3 yaşındaki çocuk için ağır; 'hazır' olmalı.
   - Açıklama: 'Hazırlıklı' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime; 'hazır' olmalı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Paylaşınca Doru'nun da annesinin de karnı doydu"
   - Cümle 15: «Paylaşınca Doru'nun da annesinin de karnı doydu.»
   - Açıklama: Tek bir kirazlı dalın yarısı çok aç iki atın karnını doyurmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0098` birebir aynı, `@degisim: bilye -> kiraz` (tutuyorsan), ardından `@onarim: e1b2c94510a93f63211fad0020f8c47cf786fa55`, sonra gövde.
