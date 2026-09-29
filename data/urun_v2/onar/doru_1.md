# Editör görevi (onarım): Doru, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0001 (deneme 1 -> 2)

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
@plan: kayaların arkasından gürültülü bir ses geldi | cesaretle gidip baktı ve dökülen suyu buldu
@tohum: doru-0001
Dağda güneş parlıyordu. Doru ile Karatay vadide çimen yiyordu. Birden kayaların arkasından gürültülü bir ses geldi. Karatay hemen durdu ve kayalara baktı. "Bu ses ne, Doru?" diye sordu Karatay. "Gel, gidip bakalım," dedi Doru. Doru cesaretle kayalara doğru yürüdü. Karatay da Doru'nun arkasından geldi. Kayaların arkasında küçük bir dere vardı. Su, kayaların üstünden aşağı dökülüyordu. Gürültülü ses bu sudan geliyordu. İki arkadaş dereye eğildi ve serin sudan içti. "Bu su çok güzel!" dedi Karatay. Doru çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden kayaların arkasından gürültülü bir ses geldi"
   - Cümle 3: «Birden kayaların arkasından gürültülü bir ses geldi.»
   - Açıklama: Ses sürekli akan bir dereden geliyor, birden başlaması akla yatkın değil ve sesin neden sorun olduğu söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0001` birebir aynı, ardından `@onarim: e2df9f69e66610d0283dcb3f00fa30b864226b60`, sonra gövde.

### Hikâye 2: tohum doru-0002 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0002
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çeşme', fiil 'kıvırmak', sıfat 'kuru'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: genç at oynarken annesine çamur sıçrattı | özür diledi ve çamuru kuru çimenle sildi
@tohum: doru-0002
@degisim: çeşme -> çamur
Çayırda rüzgar hafif hafif esiyordu. Doru'nun annesi bacaklarını kıvırdı ve kuru çimenlere yattı. Doru oynarken bir su birikintisine zıpladı ve annesine çamur sıçrattı. Annesinin sırtı çamurlu oldu. Doru bunu görünce çok üzüldü. "Özür dilerim, anneciğim, dikkat etmedim," dedi Doru. "Olsun, Doru, bundan sonra dikkat et," dedi annesi. Doru annesine hemen yardım etmek istedi. Ağzıyla biraz kuru çimen kopardı. Bu çimenle annesinin sırtındaki çamuru yavaş yavaş sildi. Hiç çamur kalmadı. Annesi ayağa kalktı ve başını Doru'nun başına sürttü. "Teşekkür ederim, Doru, sırtım yine tertemiz," dedi annesi.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çamuru kuru çimenle sildi"
   - Cümle 0 (plan satırı): «genç at oynarken annesine çamur sıçrattı | özür diledi ve çamuru kuru çimenle sildi»
   - Açıklama: Plan silmeyi söylüyor ama gövdede Doru çamuru silmiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda rüzgar hafif hafif esiyordu"
   - Cümle 1: «Çayırda rüzgar hafif hafif esiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.
   - Açıklama: Başlıktaki yer park olduğu halde hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park olduğu halde hikaye bir çayırda başlıyor ve bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0002` birebir aynı, `@degisim: çeşme -> çamur` (tutuyorsan), ardından `@onarim: 3f3e1a514e5058fd41bfd166b9044da25c96eacc`, sonra gövde.

### Hikâye 3: tohum doru-0003 (deneme 1 -> 2)

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
Çayırda büyük bir ağaç vardı. Doru bu ağacın gölgesinde dinlenmek istedi. Ama ağacın altı taşlı ve sertti. Doru orada yumuşak bir yatak yapmaya karar verdi. Çayırın ucunda büyük bir kaya duruyordu. Kayanın dibinde yeşil yosunlar vardı. Kayanın altı biraz karanlıktı. Doru cesaretle başını karanlığa uzattı. Yosunu dişleriyle tuttu ve çekti. Yosun taştan kolayca ayrıldı. Doru yosunları tek tek ağacın altına taşıdı. Hepsini taşların üstüne serdi. Ağacın altı yumuşacık oldu. Doru yeni yatağına uzandı ve gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda büyük bir ağaç vardı"
   - Cümle 1: «Çayırda büyük bir ağaç vardı.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Kayanın altı biraz karanlıktı"
   - Cümle 7: «Kayanın altı biraz karanlıktı.»
   - Açıklama: Karanlık bir tehlike gibi kuruluyor ama olayda hiçbir işe yaramıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle başını karanlığa uzattı"
   - Cümle 8: «Doru cesaretle başını karanlığa uzattı.»
   - Açıklama: Kayanın altındaki karanlık boşluğa baş sokmak çocuğun taklit edebileceği riskli bir davranış olarak cesaret diye örnekleniyor.
   - Açıklama: Çocuğun taklit edebileceği biçimde kaya altındaki karanlık bir boşluğa baş uzatılıyor.
   - Açıklama: Kayanın altındaki karanlık boşluğa baş uzatmak çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0003` birebir aynı, `@degisim: kibar -> yumuşak` (tutuyorsan), ardından `@onarim: 3265caeb5fdf9085cce1b772a998c17e74bfd426`, sonra gövde.

### Hikâye 4: tohum doru-0004 (deneme 1 -> 2)

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
@plan: yağmurdan sonra gölün suyu çamurlu olmuştu | hızla koşup berrak bir dere buldu
@tohum: doru-0004
@degisim: patlıcan -> su
Bir sabah Doru ile Kırat ormanda su içmeye geldi. Ama yağmurdan sonra küçük gölün suyu çamurlu olmuştu. Kırat bu suyu içemedi ve üzüldü. Doru, Kırat için temiz su bulmaya karar verdi. Ormanın içinden geniş ve düz bir yol geçiyordu. Doru bu yolda hızla koştu. Yolun sonunda berrak bir dere buldu. Derenin suyu tertemizdi ve serindi. Doru geri döndü ve Kırat'ın yanına geldi. Kırat'ı yavaş yavaş dereye götürdü. Kırat berrak sudan bol bol içti. Sonra başını sevgiyle Doru'ya sürttü. Doru çok sevindi, çünkü Kırat artık temiz su içebiliyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Yolun sonunda berrak bir dere buldu"
   - Cümle 7: «Yolun sonunda berrak bir dere buldu.»
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki çocuk bilmeyebilir; 'temiz' yeterli.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Yolun sonunda berrak bir dere buldu"
   - Cümle 7: «Yolun sonunda berrak bir dere buldu.»
   - Açıklama: Dere hiçbir ipucu ya da sebep olmadan yolun sonunda hazır beliriyor ve çözümü kendiliğinden getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0004` birebir aynı, `@degisim: patlıcan -> su` (tutuyorsan), ardından `@onarim: fec9b8e87703eee6cc8e66405535c41fbc351330`, sonra gövde.

### Hikâye 5: tohum doru-0005 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0005
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'biber', fiil 'bakmak', sıfat 'boş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: tepenin önündeki uzun otlar yolu kapatıyordu | önden cesaretle yürüdü ve otların arasında yol açtı
@tohum: doru-0005
@degisim: biber -> ot
Rüzgar esiyordu ve Doru ile Alaca keşif oyunu oynuyordu. İkisi çayırın ucundaki tepeye çıkmak istiyordu. Ama tepenin önünde çok uzun ve sık otlar vardı. Alaca otların önünde durdu. "Otların arasında yol göremiyorum," dedi Alaca. "Sen arkamdan gel, Alaca," dedi Doru. Doru cesaretle otların arasına ilk girdi. Otları ayaklarıyla ezdi ve bir yol açtı. Alaca bu yoldan Doru'nun arkasından yürüdü. Sonunda tepeye çıktılar. Tepenin üstü boş ve düzdü. İkisi oradan aşağıya baktı. Aşağıdaki çayır çok küçük görünüyordu. Doru ile Alaca çok sevindi, çünkü keşif oyununda tepeye ulaşmışlardı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Alaca keşif oyunu oynuyordu"
   - Cümle 1: «Rüzgar esiyordu ve Doru ile Alaca keşif oyunu oynuyordu.»
   - Açıklama: 'Keşif' kelimesi 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.
   - Açıklama: 'Keşif' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "çayırın ucundaki tepeye çıkmak"
   - Cümle 2: «İkisi çayırın ucundaki tepeye çıkmak istiyordu.»
   - Açıklama: Park tarifi geniş bir çayır der; hikaye yüksek bir tepeye taşınıyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "İkisi çayırın ucundaki tepeye çıkmak istiyordu"
   - Cümle 2: «İkisi çayırın ucundaki tepeye çıkmak istiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda ve tepede geçiyor, park hiç görünmüyor.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "çayırın ucundaki tepeye çıkmak"
   - Cümle 2: «İkisi çayırın ucundaki tepeye çıkmak istiyordu.»
   - Açıklama: Başlıktaki yer park olduğu halde hikaye bir çayırda ve tepede geçiyor, park hiç görünmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0005` birebir aynı, `@degisim: biber -> ot` (tutuyorsan), ardından `@onarim: 4b12847bd29675160cf5d4e5c8359741c2202778`, sonra gövde.

### Hikâye 6: tohum doru-0006 (deneme 1 -> 2)

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
@plan: yalnız duran atın hiç yiyeceği yoktu | elmaları eşleştirip yarısını ona götürdü
@tohum: doru-0006
@degisim: iplik -> elma
Bir sabah Doru dağda küçük bir elma ağacı buldu. Ağacın altında iki kırmızı ve iki yeşil elma vardı. Biraz ileride Kırat yalnız başına duruyordu ve önünde hiç yiyecek yoktu. Doru, Kırat'a yardım etmek istedi. Elmaları renklerine göre eşleştirdi. Bir kırmızı ve bir yeşil elmayı ağzıyla Kırat'a götürdü. "Bu iki elma senin, Kırat," dedi Doru. "Teşekkür ederim, Doru, gel birlikte yiyelim," dedi Kırat. Doru kalan iki elmayı da getirdi. İkisi yan yana durdu ve elmalarını yedi. Elmalar çok tatlıydı. Doru çok mutlu oldu, çünkü elmalarını paylaşınca Kırat artık yalnız değildi.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "önünde hiç yiyecek yoktu"
   - Cümle 3: «Biraz ileride Kırat yalnız başına duruyordu ve önünde hiç yiyecek yoktu.»
   - Açıklama: Kırat'ın neden yiyeceği olmadığı söylenmiyor.
   - Açıklama: Kırat'ın neden yiyeceği olmadığı söylenmiyor; sorunun sebebi yok.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elmaları renklerine göre eşleştirdi"
   - Cümle 5: «Elmaları renklerine göre eşleştirdi.»
   - Açıklama: Renklerine göre eşleştirip sonra bir kırmızı ile bir yeşili götürmesi kelimenin anlamıyla çelişiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Elmaları renklerine göre eşleştirdi"
   - Cümle 5: «Elmaları renklerine göre eşleştirdi.»
   - Açıklama: 'Eşleştirmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Elmaları renklerine göre eşleştirdi"
   - Cümle 5: «Elmaları renklerine göre eşleştirdi.»
   - Açıklama: Renge göre eşleştirme olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Elmaları renge göre eşleştirmek çözüme hiçbir şey katmayan işlevsiz bir ayrıntı.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kırat artık yalnız değildi"
   - Cümle 12: «Doru çok mutlu oldu, çünkü elmalarını paylaşınca Kırat artık yalnız değildi.»
   - Açıklama: Yiyecek sorununun yanında yalnızlık ikinci bir sorun olarak kuruluyor ve son buna bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0006` birebir aynı, `@degisim: iplik -> elma` (tutuyorsan), ardından `@onarim: 4726634615de24d06f725a5ad33bb0acf371ee59`, sonra gövde.

### Hikâye 7: tohum doru-0007 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Bir sabah Doru ormanda kırmızı bir elma buldu. Tam elmayı yiyecekti ki güçlü bir rüzgar esti. Elma yokuştan yuvarlandı ve yapraklı çalıların arasında kayboldu. Doru elmasını bulmak istedi. Çalıların altı biraz karanlık ve çamurluydu. Doru cesaretle başını yaprakların arasına soktu. Ayaklarını çamurla kirletti ama durmadı. Yaprakları burnuyla yavaşça itti. Kırmızı elma bir dalın dibinde duruyordu. Doru elmayı ağzıyla aldı ve güneşli açıklığa çıktı. Orada ayaklarını yumuşak çimenlere sildi. Sonra elmasını güneşte mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ayaklarını çamurla kirletti"
   - Cümle 7: «Ayaklarını çamurla kirletti ama durmadı.»
   - Açıklama: 'Kirletti' isteyerek yapılmış gibi okunuyor; 'ayakları çamura bulandı' anlamı kastediliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir dalın dibinde duruyordu"
   - Cümle 9: «Kırmızı elma bir dalın dibinde duruyordu.»
   - Açıklama: Dalın dibi olmaz; 'ağacın dibinde' ya da 'dalın altında' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "ve güneşli açıklığa çıktı"
   - Cümle 10: «Doru elmayı ağzıyla aldı ve güneşli açıklığa çıktı.»
   - Açıklama: 'Açıklık' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0007` birebir aynı, ardından `@onarim: af901c97ac7e7fbea7d23d00b0890ccb7dda4a94`, sonra gövde.

### Hikâye 8: tohum doru-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Ormanda rüzgar hafif hafif esiyordu. Doru ile annesi ağaçların arasında sırayla saklambaç oynuyordu. Önce annesi yemyeşil çalıların arkasına saklandı ve Doru onu bulamadı. Çalıların arkası sık ve biraz karanlıktı. Doru cesaretle çalıların arasına girdi. Birden yerdeki kuru tohumlar hışırdadı. Ses, annesinin ayaklarının altından geliyordu. Doru sese doğru yürüdü ve annesini buldu. "Buldum seni, anneciğim!" dedi Doru. "Çok güzel buldun, şimdi sıra sende, Doru," dedi annesi. Bu kez Doru büyük bir ağacın arkasına saklandı. Annesi biraz aradı ve Doru'yu buldu. Doru ile annesi çok sevindi, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çalıların arkası sık"
   - Cümle 4: «Çalıların arkası sık ve biraz karanlıktı.»
   - Açıklama: 'Sık' çalılar için uygun, çalıların arkası için değil; kelime öznesine uymuyor.
   - Açıklama: Sık olan çalılardır, çalıların arkası değil; sıfat öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0008` birebir aynı, `@degisim: silmek -> saklanmak` (tutuyorsan), ardından `@onarim: 2d08d8d198aa131a4c7fcc1edbdeb22c917c8eec`, sonra gövde.

### Hikâye 9: tohum doru-0009 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: yuvarlak taş boş bir kütüğün içinde kayboldu | cesaretle kütüğe bakıp yaprakların altında buldu
@tohum: doru-0009
Vadide yepyeni menekşeler açmıştı. Doru menekşelerin arasında yuvarlak bir taşla oynuyordu. Birden taş yuvarlandı ve büyük bir kütüğün içinde kayboldu. Kütüğün içi boştu ve biraz karanlıktı. Doru önce durdu. Sonra cesaretle başını kütüğe uzattı. Ama taşı göremedi. Kuru yapraklar taşın üstünü kapatmıştı. Doru yaprakları burnuyla yavaşça itti. Yuvarlak taş yaprakların altındaydı. Doru taşı burnuyla dışarı yuvarladı. Taş yine güneşe çıktı. Doru bu kez kütükten uzakta oynadı. Taşını menekşelerin arasında mutlu mutlu itmeye devam etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Vadide yepyeni menekşeler açmıştı"
   - Cümle 1: «Vadide yepyeni menekşeler açmıştı.»
   - Açıklama: Başlıktaki yer dağ ama hikaye vadide geçiyor; sahne başlıktaki yerle örtüşmüyor.
   - Açıklama: Başlıktaki yer dağ olduğu halde hikaye vadide başlayıp orada bitiyor.
   - Açıklama: Başlıktaki yer dağ iken hikaye vadide başlıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra cesaretle başını kütüğe uzattı"
   - Cümle 6: «Sonra cesaretle başını kütüğe uzattı.»
   - Açıklama: Karanlık, içi boş bir kütüğe baş sokmak çocuğun taklit edebileceği riskli bir davranış olarak cesaret diye örnekleniyor.
   - Açıklama: Çocuğun taklit edebileceği biçimde karanlık, boş bir kovuğa baş sokuluyor.
   - Açıklama: Karanlık, boş bir kütüğün içine baş uzatmak çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0009` birebir aynı, ardından `@onarim: fec3d0169e9f7ffb69bfeee51a7a61efcd9d249c`, sonra gövde.

### Hikâye 10: tohum doru-0011 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar yuvanın otlarını çayıra savurdu | otları hızla toplayıp yuvayı kayanın arkasına kurdu
@tohum: doru-0011
@degisim: yardımsever -> beyaz
Rüzgar çayırda sert esiyordu. Doru ile Karatay kuru otlardan bir yuva yapmış, yumurta oyunu oynuyordu. Ama rüzgar yuvanın otlarını çayıra savurdu. Yuvada yalnız beyaz, yuvarlak bir taş kaldı. Oyunda o taşa yumurta diyorlardı. "Yumurtanın yuvası gitti!" dedi Karatay heyecanla. "Üzülme, otları hemen toplarım," dedi Doru. Çayır açık ve düzdü. Otlar uzağa gitmeden Doru hızla koştu ve hepsini ağzıyla topladı. Bu kez yuvayı büyük bir kayanın arkasına kurdular. Orada hiç rüzgar yoktu. "Yumurta artık rahat, teşekkürler, Doru!" dedi Karatay. Doru çok sevindi, çünkü yuvayı birlikte kurtarmışlardı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Rüzgar çayırda sert esiyordu"
   - Cümle 1: «Rüzgar çayırda sert esiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
   - Açıklama: Başlıktaki yer park olduğu halde hikaye çayırda başlıyor ve bitiyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "kuru otlardan bir yuva yapmış"
   - Cümle 2: «Doru ile Karatay kuru otlardan bir yuva yapmış, yumurta oyunu oynuyordu.»
   - Açıklama: Kartın tür alanında at olan Doru ve Karatay'ın yuva kurup yumurta oyunu oynaması dizideki at dünyasına yabancı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar yuvanın otlarını çayıra savurdu"
   - Cümle 3: «Ama rüzgar yuvanın otlarını çayıra savurdu.»
   - Açıklama: Rüzgarın oyun otlarını dağıtıp Doru'nun toplaması, istemde M3 örneği olarak verilen önemsiz dağıldı-topladı sorununun aynısı.
   - Açıklama: Sorun, istemdeki 'rüzgar oyun yapraklarını dağıttı, topladı' örneğine çok yakın, önemsiz bir oyun aksilliği.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedi Karatay heyecanla"
   - Cümle 6: «"Yumurtanın yuvası gitti!" dedi Karatay heyecanla.»
   - Açıklama: Yuva dağılınca söylenen üzgün sözde 'heyecanla' duyguya uymuyor; 'telaşla' ya da 'üzgünce' olmalı.
   - Açıklama: Yuva dağılınca söylenen üzgün sözde 'heyecanla' duyguya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0011` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 06009b440e7b08795e86c31706cb8b38cd1ae02a`, sonra gövde.
