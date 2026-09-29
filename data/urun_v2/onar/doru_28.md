# Editör görevi (onarım): Doru, onarım partisi 28

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar28.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0078 (deneme 5 -> 6)

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
Bir sabah ormandaki küçük gölet buzla kaplıydı. Doru'nun arkadaşı Karatay çok susamıştı ama buzdan su içemiyordu. Doru ona yardım etmek için etrafa baktı. Uzaktaki bir ağacın altında, karda yuvarlak ve ıslak izler gördü. Doru bunları merak etti ve Karatay'ı da yanına aldı. İkisi ağaca yürüdü. Ağacın dallarında buzlar vardı ve güneşte eriyordu. Damlalar tek tek karın üstüne düşüyordu. İzleri bu damlalar yapmıştı. Ağacın altında çukur bir taş vardı ve içi suyla doluydu. Her damla o suya biraz daha su katıyordu. Karatay soğuk suyu keyifle içti. Doru çok sevindi, çünkü arkadaşına su bulmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "o suya biraz daha su katıyordu"
   - Cümle 11: «Her damla o suya biraz daha su katıyordu.»
   - Açıklama: Aynı cümlede 'su' kelimesi gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0078` birebir aynı, `@degisim: puantiyeli -> yuvarlak` (tutuyorsan), ardından `@onarim: 21c4f67debef75d5898f4160c549c95026b173c5`, sonra gövde.

### Hikâye 2: tohum doru-0081 (deneme 5 -> 6)

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
Bir sabah Kırat ormanda bir ağacın altında uyuyordu. Doru onu sevindirmek için çilek toplamak istedi. Ama yakındaki çalıda yalnız üç çilek vardı ve hepsi yeşildi. Kırmızı çilekler ise ağaçların arkasındaki geniş açıklıktaydı. Doru ağaçların arasından yavaşça geçti ve açıklıkta hızla koştu. Çilekli bir sapı ağzıyla kopardı ve geri döndü. Çilekleri düz bir taşın üstüne düzenli bir sırayla dizdi. Kırat gözlerini açtı ve taşa baktı. "Bunlar benim için mi, Doru?" diye sordu Kırat. "Hepsi senin için!" dedi Doru. Kırat bir çilek tattı ve gülümsedi. "Çok tatlı, teşekkürler, Doru," dedi Kırat. Doru bundan sonra kırmızı çilekleri hep o açıklıkta aradı.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Doru bundan sonra kırmızı çilekleri hep o açıklıkta aradı"
   - Cümle 13: «Doru bundan sonra kırmızı çilekleri hep o açıklıkta aradı.»
   - Açıklama: Son cümle sıcak bir kapanış ya da olaydan çıkan bir ders değil, düz bir alışkanlık bildirimiyle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0081` birebir aynı, `@degisim: oyuncak -> çilek` (tutuyorsan), ardından `@onarim: 8c6ab07401c0ef9d1431eb777324cad56cb70fc6`, sonra gövde.

### Hikâye 3: tohum doru-0082 (deneme 5 -> 6)

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
Geniş çayırda kuşlar ötüyordu. Doru bir ağacın altında son iki kırmızı elmayı buldu. Küçük Alaca da geldi ama onun hiç elması yoktu. Alaca elmalara baktı ve üzüldü. Doru Alaca'yı iyi tanıyordu ve onun elmayı sevdiğini biliyordu. Doru Alaca'ya yardım etmek istedi. Elmalardan birini burnuyla Alaca'nın önüne itti. "Bu elma senin, Alaca," dedi Doru. Alaca elmayı yavaşça ısırdı ve sevinçle zıpladı. "Çok tatlıymış, teşekkürler, Doru," dedi Alaca. İki at elmalarını yan yana yedi. Doru çok sevindi, çünkü elmasını Alaca ile paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Geniş çayırda kuşlar ötüyordu"
   - Cümle 1: «Geniş çayırda kuşlar ötüyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0082` birebir aynı, `@degisim: mercan -> elma` (tutuyorsan), ardından `@onarim: c1737e848b3449f4df3101b77178cdfcd7dc72eb`, sonra gövde.

### Hikâye 4: tohum doru-0091 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar esti ve turp karanlık bir çalının altına yuvarlandı | korkmadan turpu çalının altından dişleriyle çıkardı
@tohum: doru-0091
@degisim: asmak -> saklamak
Ormanda Doru ile Alaca küçük bir turpu sırayla saklıyordu. Sıra Alaca'daydı ve Alaca turpu yokuşta bir taşın arkasına koydu. Ama güçlü bir rüzgar esti ve turp sık bir çalının altına yuvarlandı. Çalının altı karanlıktı ve Alaca yaklaşmaya korktu. "Doru, oyunumuz bitti mi?" diye sordu Alaca. "Hayır, Alaca, ben çıkarırım," dedi Doru. Doru cesaretle çalının yanına gitti ve eğildi. Dişleriyle turpu tuttu ve dışarı çekti. Alaca sevinçle zıpladı. "Sıra sende, Doru," dedi Alaca. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "güçlü bir rüzgar esti ve turp"
   - Cümle 3: «Ama güçlü bir rüzgar esti ve turp sık bir çalının altına yuvarlandı.»
   - Açıklama: Rüzgarın bir turpu çalının altına yuvarlaması zayıf ve inandırıcılığı düşük bir sebep.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalının altı karanlıktı ve Alaca yaklaşmaya korktu"
   - Cümle 4: «Çalının altı karanlıktı ve Alaca yaklaşmaya korktu.»
   - Açıklama: Karanlık çalı ve korku 3-6 yaş için korkutucu bir öğe olabilir.
   - Açıklama: Karanlık çalı altı küçük çocuk için korkutucu bir öğe olarak sunuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0091` birebir aynı, `@degisim: asmak -> saklamak` (tutuyorsan), ardından `@onarim: 48fb483a7d2ef0022fcaf9acec7ad53a8f48538f`, sonra gövde.

### Hikâye 5: tohum doru-0092 (deneme 4 -> 5)

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
Bir sabah Doru ile annesi geniş çayırda neşeli bir oyun oynuyordu. Annesi şarkı söylerken Doru koşuyor, şarkı bitince duruyordu. Ama rüzgar çok gürültülüydü ve Doru annesini duymadı. Doru durmadı ve uzaktaki böğürtlen çalısına kadar koştu. Annesi güldü. "Doru, şarkı bitti ama sen koşuyordun!" dedi annesi. Doru gülümsedi ve biraz düşündü. "Anne, şarkı bitince başını da salla," dedi Doru. Annesi yeniden şarkıya başladı ve Doru onun yanında hızla koştu. Sonra annesi birden sustu ve başını salladı. Doru annesine bakıyordu, bu yüzden hemen durdu. "Aferin, Doru!" dedi annesi. Doru bundan sonra rüzgar esince annesini dikkatle izlerdi.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "geniş çayırda neşeli bir oyun"
   - Cümle 1: «Bir sabah Doru ile annesi geniş çayırda neşeli bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile annesi geniş çayırda"
   - Cümle 1: «Bir sabah Doru ile annesi geniş çayırda neşeli bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru onun yanında hızla koştu"
   - Cümle 9: «Annesi yeniden şarkıya başladı ve Doru onun yanında hızla koştu.»
   - Açıklama: Tohumdaki hız özelliği yalnız süs olarak geçiyor, sorunu çözmekte işe yaramıyor.
   - Açıklama: Tohumdaki hız özelliği sorunun çözümünde işe yaramıyor; sorunu annesinin baş sallaması çözüyor.
4. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "annesini dikkatle izlerdi"
   - Cümle 13: «Doru bundan sonra rüzgar esince annesini dikkatle izlerdi.»
   - Açıklama: Anlatım -dı'lı geçmişten geniş zamanın hikayesine ('izlerdi') kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0092` birebir aynı, ardından `@onarim: 4ab4164cfe0323fad48a8f7d175b46307939232c`, sonra gövde.

### Hikâye 6: tohum doru-0093 (deneme 4 -> 5)

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
Doru ormanda yol koruma oyunu oynuyordu. Birden rüzgar esti ve uzun, çiçekli bir dal yolun üstüne düştü. Artık sürüdeki küçük atlar oradan geçemezdi. Doru onlara yardım etmek istedi. Dalın ucuna uzun otlar dolanmıştı ve dal yerinden kıpırdamıyordu. Doru önce dala baktı ve biraz düşündü. Doru otları dişleriyle tuttu ve yavaşça çözdü. Sonra dalı ağzıyla tuttu ve yolun kenarına çekti. Artık yol küçük atlar için yeniden güvenliydi. Doru çok sevindi, çünkü oyununda sürünün yolunu korumuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dalın ucuna uzun otlar dolanmıştı"
   - Cümle 5: «Dalın ucuna uzun otlar dolanmıştı ve dal yerinden kıpırdamıyordu.»
   - Açıklama: Dalı tutan otlar sebepsizce beliriyor ve yalnız çözümü getirmek için kuruluyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "oyununda sürünün yolunu korumuştu"
   - Cümle 10: «Doru çok sevindi, çünkü oyununda sürünün yolunu korumuştu.»
   - Açıklama: Hikaye bir oyun olarak başlıyor ama küçük atların gerçekten geçemediği söyleniyor; oyun ile gerçek çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0093` birebir aynı, `@degisim: koni -> çiçek` (tutuyorsan), ardından `@onarim: c6452e92020c80cdc40d1b17b6f26cc7c4a42ba9`, sonra gövde.

### Hikâye 7: tohum doru-0096 (deneme 4 -> 5)

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
Hafif bir rüzgar esiyordu ve Doru ormanda oynuyordu. Kırat bir ağacın altında, düğme gibi küçük ve rengarenk çiçeklere bakıyordu. Doru koşup geldi ve çiçeklerin üstüne bastı. Çiçeklerin çoğu yere doğru eğildi. Kırat buna çok üzüldü. Doru önce biraz utandı ve saklanmak istedi. Sonra cesurca Kırat'ın yanına gitti. "Özür dilerim, Kırat, çiçekleri görmedim," dedi Doru. "Teşekkürler, Doru," dedi Kırat gülümseyerek. Doru eğilmiş çiçekleri burnuyla tek tek kaldırdı. Hepsi yeniden güneşe doğru döndü. Sonra Doru çiçeklerin yanından dikkatle geçti ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "düğme gibi küçük ve rengarenk"
   - Cümle 2: «Kırat bir ağacın altında, düğme gibi küçük ve rengarenk çiçeklere bakıyordu.»
   - Açıklama: Doğa dünyasında olmayan düğme eşyası (giysi kategorisi) benzetme olarak hikayeye giriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: ""Teşekkürler, Doru," dedi Kırat"
   - Cümle 9: «"Teşekkürler, Doru," dedi Kırat gülümseyerek.»
   - Açıklama: Özre 'teşekkürler' diye karşılık vermek anlamca uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0096` birebir aynı, `@degisim: tanıştırmak -> dilemek` (tutuyorsan), ardından `@onarim: a2dd559377a414ac88695c9543bb629d73c238fd`, sonra gövde.

### Hikâye 8: tohum doru-0098 (deneme 3 -> 4)

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
Doru annesiyle ormandaki büyük kiraz ağacının altına geldi. Ama ağacın alçak dalları boşalmıştı, çünkü oradaki kirazlar yenmişti. İkisinin de karnı çok açtı. Doru çevresine baktı. Ağaçların arasındaki dar bir yolun sonunda küçük bir kiraz ağacı gördü. Yolu uzun otlar kapatmıştı. Doru hazırlıklıydı ve cesaretle öne geçti. Otların arasından yürüdü ve annesi de arkasından geldi. Küçük ağaçta yuvarlak, kırmızı kirazlar vardı. Doru kirazlı bir dalı ağzıyla kopardı ve annesinin önüne koydu. "Anneciğim, bunları birlikte yiyelim," dedi Doru. Annesi gülümsedi ve kirazların yarısını aldı. Doru da öbür yarısını yedi. Doru bundan sonra bulduğu kirazları hep annesiyle paylaştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru hazırlıklıydı ve cesaretle"
   - Cümle 7: «Doru hazırlıklıydı ve cesaretle öne geçti.»
   - Açıklama: 'Hazırlıklıydı' bu bağlamda anlamsız ve yanlış kullanılmış.
   - Açıklama: 'Hazırlıklıydı' bağlamda anlamsız ve soyut; neye hazırlıklı olduğu belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru hazırlıklıydı ve cesaretle"
   - Cümle 7: «Doru hazırlıklıydı ve cesaretle öne geçti.»
   - Açıklama: Tohumdaki özellik cesaret; hazırlıklı olmak karttaki özelliklerde olmayan ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik cesaret; hazırlıklı olmak ikinci bir özellik olarak ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru hazırlıklıydı ve cesaretle öne geçti"
   - Cümle 7: «Doru hazırlıklıydı ve cesaretle öne geçti.»
   - Açıklama: Doru'nun neye hazırlıklı olduğu hiç kurulmuyor ve bu ayrıntı olayda işlevsiz kalıyor.
   - Açıklama: Doru'nun neye hazırlıklı olduğu kurulmuyor ve bu ayrıntı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0098` birebir aynı, `@degisim: bilye -> kiraz` (tutuyorsan), ardından `@onarim: befa474810531d088486d044b326e6245815e3af`, sonra gövde.
