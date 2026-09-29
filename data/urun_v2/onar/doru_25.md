# Editör görevi (onarım): Doru, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar25.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0053 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0053
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çan', fiil 'güzelleşmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sıcakta susamıştı ama su bulamamıştı | cesaretle çalılardan geçip sesi yapan suyu buldu
@tohum: doru-0053
@degisim: çan -> dal
Ormanda bir ses geliyordu: tıp, tıp. Doru sıcakta çok susamıştı ama su bulamamıştı. Ses sık çalıların arkasından geliyordu ve Doru onu merak etti. Belki orada su vardı. Doru bir an durdu, sonra cesaretle çalıların arasından geçti. Arkada yukarıdaki kayalardan ince bir su iniyordu. Su bir dalın üstünden akıp taşlara düşüyordu. Ses bu sudan geliyordu. Doru başını eğdi ve serin, tatlı sudan içti. Su içince Doru'nun sıcak günü birden güzelleşti. Doru suyun yanındaki çimenlerde mutlu mutlu otladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru'nun sıcak günü birden güzelleşti"
   - Cümle 10: «Su içince Doru'nun sıcak günü birden güzelleşti.»
   - Açıklama: 'Günü güzelleşti' soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.
   - Açıklama: Günün güzelleşmesi soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0053` birebir aynı, `@degisim: çan -> dal` (tutuyorsan), ardından `@onarim: d6715da15958038c272c6fd7bbee854979cc03f3`, sonra gövde.

### Hikâye 2: tohum doru-0070 (deneme 4 -> 5)

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
Dağda güneş vardı ve Doru tek başına çimen yiyordu. Birden Doru'nun gölgesi kayboldu, çünkü bulutlar gelmişti. Sonra yağmur başladı ve Doru'nun sırtı ıslandı. Yakında hiç ağaç yoktu, yalnız eskimiş küçük bir kütük vardı. Biraz ileride büyük bir kaya vardı. Yağmur çok yağıyordu ama Doru cesaretle kayaya kadar yürüdü. Kayanın bir yanı öne çıkmıştı ve altı kuruydu. Doru oraya girdi ve daha fazla ıslanmadı. Bir süre sonra bulutlar gitti ve güneş çıktı. Doru oradan çıktı ve yeniden çimen yemeye başladı. Doru bundan sonra yağmur başlayınca o kayanın altına saklandı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yalnız eskimiş küçük bir kütük vardı"
   - Cümle 4: «Yakında hiç ağaç yoktu, yalnız eskimiş küçük bir kütük vardı.»
   - Açıklama: Kütük işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.
   - Açıklama: Kütük kurulup hiçbir işe yaramıyor, işlevsiz ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0070` birebir aynı, `@degisim: anlatmak -> saklanmak` (tutuyorsan), ardından `@onarim: 5a29537ffabbc3038d7e6209e3f6619415341f39`, sonra gövde.

### Hikâye 3: tohum doru-0072 (deneme 4 -> 5)

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
@plan: tek başına sıkılmıştı ve çalılardan bir ses geliyordu | çalıların arkasına bakıp damlayan suyu buldu ve oynadı
@tohum: doru-0072
Bir ses geliyordu: tık, tık. Doru ormanda tek başına çok sıkılmıştı ve bu sesi hemen duydu. Ses yakındaki çalıların arkasından geliyordu ve Doru onu çok merak etti. Doru çalıların yanından dolaştı ve arkaya baktı. Arkada büyük, düz bir taş vardı. Yukarıdaki kayalardan ince bir su iniyordu. Her damla taşa düşünce tık diye ses çıkarıyordu. Doru cesaretle suyun altına girdi ve sırılsıklam oldu. Serin su Doru'yu çok güldürdü. Doru artık sıkılmıyordu, çünkü suyla yeni bir oyun bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Doru ormanda tek başına çok sıkılmıştı"
   - Cümle 2: «Doru ormanda tek başına çok sıkılmıştı ve bu sesi hemen duydu.»
   - Açıklama: Sorun yalnız can sıkıntısı ve merak edilen bir ses; açık, önemsenecek bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0072` birebir aynı, ardından `@onarim: 7ed9a5f1b5cb93aa29de812692a04f85fdb0b768`, sonra gövde.

### Hikâye 4: tohum doru-0078 (deneme 3 -> 4)

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
Bir sabah ormandaki küçük gölet buzla kaplıydı. Doru'nun arkadaşı Karatay çok susamıştı ama buzdan su içemiyordu. Doru ona yardım etmek için etrafa baktı. Uzaktaki bir ağacın altında, karda yuvarlak ve ıslak izler gördü. Doru bunları merak etti ve Karatay ile ağaca yürüdü. Ağacın dallarında buzlar vardı ve güneşte eriyordu. Damlalar tek tek karın üstüne düşüyordu. İzleri bu damlalar yapmıştı. Ağacın altında çukur bir taş vardı ve içinde biraz su toplanmıştı. Ama su çok azdı. Doru dallardan düşen küçük buzları burnuyla suya kattı. Buzlar güneşte eridi ve su çoğaldı. Karatay soğuk suyu keyifle içti. Doru çok sevindi, çünkü arkadaşına su bulmuştu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru dallardan düşen küçük buzları burnuyla suya kattı"
   - Cümle 11: «Doru dallardan düşen küçük buzları burnuyla suya kattı.»
   - Açıklama: Çözüm göletteki buza yönelmiyor; iz sürme, taşı bulma ve buz ekleme gibi ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0078` birebir aynı, `@degisim: puantiyeli -> yuvarlak` (tutuyorsan), ardından `@onarim: 422c9885c6c311e7e887c0298f3b3e31fde73af8`, sonra gövde.

### Hikâye 5: tohum doru-0081 (deneme 3 -> 4)

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
@plan: yakındaki çalıda yalnız üç çilek vardı | açıklıkta hızla koştu ve bol çilek getirdi
@tohum: doru-0081
@degisim: oyuncak -> çilek
Bir sabah Kırat ormanda bir ağacın altında uyuyordu. Doru onu sevindirmek için çilek toplamak istedi. Ama yakındaki çalıda yalnız üç çilek vardı ve bu çok azdı. Çok çilek ise ormanın öbür ucundaki geniş açıklıktaydı. Doru ağaçların arasından yavaşça geçti ve açıklıkta hızla koştu. Çilekli bir dalı ağzıyla kopardı ve geri döndü. Çilekleri düz bir taşın üstüne düzenli bir sırayla dizdi. Kırat gözlerini açtı ve taşa baktı. "Bunlar benim için mi, Doru?" diye sordu Kırat. "Hepsi senin için!" dedi Doru. Kırat bir çilek tattı ve gülümsedi. "Çok tatlı, teşekkürler, Doru," dedi Kırat. Doru bundan sonra sevdiklerine sık sık küçük sürprizler hazırladı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bu çok azdı"
   - Cümle 3: «Ama yakındaki çalıda yalnız üç çilek vardı ve bu çok azdı.»
   - Açıklama: Uyuyan arkadaşa üç çileğin neden yetmediği akla yatkın biçimde söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sevdiklerine sık sık küçük sürprizler hazırladı"
   - Cümle 13: «Doru bundan sonra sevdiklerine sık sık küçük sürprizler hazırladı.»
   - Açıklama: 'Sevdikleri' ve 'sürpriz' soyut kavramlar; genelleyici cümle olaydan çıkan somut bir ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0081` birebir aynı, `@degisim: oyuncak -> çilek` (tutuyorsan), ardından `@onarim: 6b2f64c34e51f670f87e355a63609d5700d7a184`, sonra gövde.

### Hikâye 6: tohum doru-0082 (deneme 3 -> 4)

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
Geniş çayırda kuşlar ötüyordu. Doru bir ağacın altında iki kırmızı elma buldu. Küçük Alaca da geldi ama ağaçta başka elma kalmamıştı. Alaca kırmızı elmaları tanımıyordu ve merakla baktı. "Doru, bunlar ne?" diye sordu Alaca. "Bunlar elma, çok tatlıdır," dedi Doru. Doru Alaca'ya yardım etmek istedi. Elmalardan birini burnuyla Alaca'nın önüne itti. "Bu elma senin, Alaca," dedi Doru. Alaca elmayı yavaşça ısırdı ve sevinçle zıpladı. "Çok güzelmiş, teşekkürler," dedi Alaca. İki at elmalarını yan yana yedi. Doru çok sevindi, çünkü elmasını Alaca ile paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Geniş çayırda kuşlar ötüyordu"
   - Cümle 1: «Geniş çayırda kuşlar ötüyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0082` birebir aynı, `@degisim: mercan -> elma` (tutuyorsan), ardından `@onarim: 83b176d4cdb9d17278213a5c8554dc7f41c7b2c5`, sonra gövde.

### Hikâye 7: tohum doru-0083 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0083
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'file', fiil 'gülümsemek', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: kozalak köke çarpıp çalılara doğru yuvarlandı | hızla koşup kozalağı çalıların önünde durdurdu
@tohum: doru-0083
@degisim: file -> kozalak
Bir sabah Doru ormandaki geniş bir açıklıkta heyecanlı bir oyun oynuyordu. En sevdiği büyük kozalağı burnuyla itiyor ve peşinden koşuyordu. Ama kozalak bir köke çarptı ve uzağa yuvarlandı. Yakında sık çalılar vardı. Kozalak çalıların içinde kaybolabilirdi. Doru açık ve düz çimende hızla koştu. Onun önüne geçti ve burnuyla durdurdu. Kozalak çalıların hemen önünde kaldı. Doru ona baktı ve gülümsedi. Sonra onu köklerin olmadığı düz bir yere götürdü. Doru en sevdiği kozalakla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun önüne geçti ve burnuyla durdurdu"
   - Cümle 7: «Onun önüne geçti ve burnuyla durdurdu.»
   - Açıklama: Önceki cümlenin öznesi Doru olduğundan 'Onun' zamirinin kozalağı gösterdiği belli değil.
   - Açıklama: 'Onun' zamirinin kozalağı gösterdiği önceki cümlede Doru özne olduğu için belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0083` birebir aynı, `@degisim: file -> kozalak` (tutuyorsan), ardından `@onarim: 6b9361eea1d743df8684c098b8561cb7de2f3349`, sonra gövde.

### Hikâye 8: tohum doru-0087 (deneme 3 -> 4)

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
Çayırda rüzgar esiyordu. Doru kocaman bir ot topuyla oynuyordu. Topu burnuyla yuvarlıyor ve peşinden koşuyordu. Ama rüzgar birden güçlendi ve hafif topu ağaçlara doğru itti. Ağaçların altını kalın bir kuru yaprak örtüsü kaplıyordu. Top bu yaprakların altına girdi ve kayboldu. Doru hemen oraya gitti. Kuru yapraklar ayaklarının altında yüksek sesle çıtırdadı. Doru bir an durdu ama cesaretle yaprakların üstünde yürüdü. Burnuyla yaprakları itti ve topunu buldu. Onu yeniden çayırın ortasına yuvarladı. Doru kocaman topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda rüzgar esiyordu"
   - Cümle 1: «Çayırda rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlayıp çayırda bitiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve orada bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0087` birebir aynı, `@degisim: görüşmek -> yuvarlamak` (tutuyorsan), ardından `@onarim: 832ac003a14602058d7f23a9d15fb6258c4879bc`, sonra gövde.

### Hikâye 9: tohum doru-0091 (deneme 2 -> 3)

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
@plan: turp yuvarlandı ve karanlık bir deliğe girdi | korkmadan turpu delikten dişleriyle çıkardı
@tohum: doru-0091
@degisim: asmak -> saklamak
Ormanda Doru ile Alaca sırayla turp saklıyordu. Sıra Alaca'daydı ve Alaca turpu yokuşta bir taşın arkasına koydu. Ama turp aşağı yuvarlandı ve büyük bir ağacın altındaki deliğe girdi. Delik çok karanlıktı ve Alaca yaklaşmaya korktu. "Doru, oyunumuz bitti mi?" diye sordu Alaca. "Hayır, Alaca, ben çıkarırım," dedi Doru. Doru cesaretle başını deliğe soktu. Güçlü dişleriyle turpu tuttu ve dışarı çekti. Alaca sevinçle zıpladı. "Sıra sende, Doru," dedi Alaca. Sonra ikisi oyunlarına sırayla, mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Doru ile Alaca sırayla turp saklıyordu"
   - Cümle 1: «Ormanda Doru ile Alaca sırayla turp saklıyordu.»
   - Açıklama: Özgür at sürüsünün doğa dünyasında ekili bir sebze olan turp kartta olmayan bir eşya olarak oyuna sokuluyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle başını deliğe soktu"
   - Cümle 7: «Doru cesaretle başını deliğe soktu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde ağaç altındaki karanlık bir deliğe baş sokuluyor.
   - Açıklama: Ağaç altındaki karanlık bir deliğe baş sokmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0091` birebir aynı, `@degisim: asmak -> saklamak` (tutuyorsan), ardından `@onarim: 891594b5da2ca7d5631fa46218b2f5ebb05fc910`, sonra gövde.

### Hikâye 10: tohum doru-0092 (deneme 2 -> 3)

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
@plan: rüzgar çok gürültülüydü ve şarkının bittiğini duymadı | annesine şarkı bitince başını salla dedi
@tohum: doru-0092
Bir sabah Doru ile annesi geniş çayırda neşeli bir oyun oynuyordu. Annesi şarkı söylerken Doru hızla koşuyor, şarkı bitince duruyordu. Ama rüzgar çok gürültülüydü ve Doru annesini duymadı. Doru durmadı ve böğürtlen çalısına kadar koştu. Annesi güldü. "Doru, şarkı bitti ama sen koşuyordun!" dedi annesi. Doru gülümsedi ve biraz düşündü. "Anne, şarkı bitince başını da salla," dedi Doru. Annesi yeniden şarkıya başladı. Sonra birden sustu ve başını salladı. Doru bunu hemen gördü ve tam yerinde durdu. "Aferin, Doru!" dedi annesi ve çalıdan ona bir böğürtlen verdi. Doru bundan sonra rüzgar esince annesine de dikkatle baktı.
```

**Hakem bulguları (4):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "şarkı bitince başını salla dedi"
   - Cümle 0 (plan satırı): «rüzgar çok gürültülüydü ve şarkının bittiğini duymadı | annesine şarkı bitince başını salla dedi»
   - Açıklama: Plandaki doğrudan aktarılan söz tırnaksız ve noktalamasız yazılmış.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "annesi geniş çayırda neşeli"
   - Cümle 1: «Bir sabah Doru ile annesi geniş çayırda neşeli bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru hızla koşuyor"
   - Cümle 2: «Annesi şarkı söylerken Doru hızla koşuyor, şarkı bitince duruyordu.»
   - Açıklama: Tohumdaki hız özelliği yalnız oyunun parçası olarak geçiyor, sorunun çözümünde işe yaramıyor (çözüm baş sallama).
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru bundan sonra rüzgar esince annesine de dikkatle baktı"
   - Cümle 13: «Doru bundan sonra rüzgar esince annesine de dikkatle baktı.»
   - Açıklama: 'Bundan sonra' süreklilik bildirdiği için fiil 'bakardı' ya da 'bakıyordu' olmalı.
   - Açıklama: 'Bundan sonra' süreklilik bildirirken fiil tek seferlik 'baktı' olmuş; 'bakıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0092` birebir aynı, ardından `@onarim: 7497c7062e3fe5defeb7b10084cc9b51a52c58f9`, sonra gövde.

### Hikâye 11: tohum doru-0093 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kuru bir ot çiçeği aşağı çekiyordu | otu dişleriyle tuttu ve yavaşça çözdü
@tohum: doru-0093
@degisim: koni -> çiçek
Doru ormanda, ağaçların arasında çiçekleri koruma oyunu oynuyordu. Birden yere eğilmiş, mor bir çiçek gördü. Ona kuru bir ot sarılmıştı ve onu aşağı çekiyordu. Doru bu küçük çiçeğe yardım etmek istedi. Önce onu kırmamak için yavaşça yaklaştı. Otu dişleriyle tuttu ve dikkatle çözdü. Ot yere düştü ve mor çiçek hafifçe sallandı. Sonra yeniden yukarı kalktı ve güneşe doğru döndü. Artık çiçek güvenliydi. Doru çiçeği burnuyla kokladı. Çiçeğin kokusu çok güzeldi. Doru çok sevindi, çünkü oyununda ilk çiçeğini korumuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ona kuru bir ot sarılmıştı"
   - Cümle 3: «Ona kuru bir ot sarılmıştı ve onu aşağı çekiyordu.»
   - Açıklama: Kuru bir otun çiçeği aşağı çekmesi akla pek yatkın ve çocuğun önemseyeceği bir sorun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Artık çiçek güvenliydi"
   - Cümle 9: «Artık çiçek güvenliydi.»
   - Açıklama: 'Güvenli' tehlikesiz demektir; çiçek için 'güvendeydi' olmalı.
   - Açıklama: 'Güvenli' tehlikesiz demektir; burada 'güvendeydi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0093` birebir aynı, `@degisim: koni -> çiçek` (tutuyorsan), ardından `@onarim: 4072a0d5aa1d9269f0a7e3adf66394420bfc9e8b`, sonra gövde.

### Hikâye 12: tohum doru-0095 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0095
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'baloncuk', fiil 'guruldamak', sıfat 'uyanık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: bir taş suyu kapattı ve papatyalar kurudu | taşı burnuyla yana itti ve su papatyalara aktı
@tohum: doru-0095
Bir sabah sürüdeki atlar uyuyordu, yalnız Doru uyanıktı. Doru vadide çiçekleri koruma oyunu oynuyordu. Ama küçük papatyalar kuruyordu, çünkü bir taş dereden gelen suyu kapatmıştı. Doru papatyalara yardım etmek istedi. Taşı burnuyla güçlüce yana itti. Su hemen papatyalara doğru aktı. Su kuru toprağa girdi ve toprakta küçük baloncuklar çıktı. Papatyalar yavaş yavaş yeniden kalktı. Doru çok çalışmıştı ve karnı guruldadı. Papatyaların yanındaki taze çimenlerden biraz yedi. Sonra Doru oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir taş suyu kapattı"
   - Cümle 0 (plan satırı): «bir taş suyu kapattı ve papatyalar kurudu | taşı burnuyla yana itti ve su papatyalara aktı»
   - Açıklama: Taş suyu kapatmaz, suyun önünü kapatır; fiil nesnesine uymuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Taşı burnuyla güçlüce yana itti"
   - Cümle 5: «Taşı burnuyla güçlüce yana itti.»
   - Açıklama: Tohumdaki özellik yardım; güç ikinci bir kart özelliği olarak ekleniyor.
   - Açıklama: Tohumdaki özellik yardım; güç ikinci bir özellik olarak ekleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Papatyalar yavaş yavaş yeniden kalktı"
   - Cümle 8: «Papatyalar yavaş yavaş yeniden kalktı.»
   - Açıklama: Çiçekler kalkmaz; 'doğruldu' gibi öznesine uygun bir fiil gerekir.
   - Açıklama: Çiçekler kalkmaz; 'dikildi' ya da 'doğruldu' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru çok çalışmıştı ve karnı guruldadı"
   - Cümle 9: «Doru çok çalışmıştı ve karnı guruldadı.»
   - Açıklama: Karnının guruldaması ve çimen yemesi sorundan çıkmayan, işlevsiz bir ek olay.
   - Açıklama: Tek bir itişten sonra acıkıp çimen yemek sorunla ilgisiz işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0095` birebir aynı, ardından `@onarim: faac2415deeedde9b4bd0e9d551f774f54bb52cc`, sonra gövde.
