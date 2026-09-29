# Editör görevi (onarım): Doru, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0012 (deneme 3 -> 4)

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
@plan: küçük arkadaşı sırası gelince yapraklara uzanamadı | dalı dişleriyle eğdi ve yaprakları arkadaşının önüne getirdi
@tohum: doru-0012
@degisim: esnek -> ince
Doru ile Alaca parktaki geniş çayırda sırayla yaprak koparıyordu. Ağacın ince bir dalında yeşil yapraklar vardı. Ama Alaca çok küçüktü ve sırası gelince dala uzanamadı. "Yapraklar çok yüksekte, Doru," dedi Alaca. Alaca çok üzüldü. Doru ona hemen yardım etmek istedi. Gözleriyle bütün dalı taradı ve biraz düşündü. Sonra dişleriyle dalın ucunu tuttu ve yavaşça aşağı çekti. Dal kolayca eğildi ve yapraklar Alaca'nın önüne geldi. "Sıra sende, Alaca," dedi Doru. Alaca bir yaprak kopardı ve keyifle yedi. "Bu, en tatlı yiyecek!" dedi Alaca. Doru çok sevindi, çünkü Alaca da kendi sırasında yaprak yemişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Gözleriyle bütün dalı taradı"
   - Cümle 7: «Gözleriyle bütün dalı taradı ve biraz düşündü.»
   - Açıklama: 'Gözleriyle taramak' mecazlı bir anlatım ve küçük çocuğa uygun değil.
   - Açıklama: 'gözleriyle taradı' mecazlı ve küçük çocuğun bilmeyeceği bir anlatım.
   - Açıklama: 'Gözleriyle taramak' mecazlı bir anlatım; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0012` birebir aynı, `@degisim: esnek -> ince` (tutuyorsan), ardından `@onarim: 68f3932b109b4b68640e98f5592bf219a71ccc88`, sonra gövde.

### Hikâye 2: tohum doru-0014 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: vadiden gelen garip bir ses arkadaşını korkuttu | hızla koşup sesi yapan dönen yapraklara yetişti
@tohum: doru-0014
@degisim: yetiştirmek -> yetişmek
Dağdaki vadide gökyüzü masmaviydi. Doru ile Karatay çimenlerin üstünde oynuyordu. Birden vadinin öbür ucundan hışır hışır bir ses geldi. Karatay bu sesten biraz korktu ve oyunu bıraktı. "Bu ses ne, Doru?" diye sordu Karatay. "Bilmiyorum, ama hemen gidip bakarım," dedi Doru. Ses yavaş yavaş uzaklaşıyordu. Vadi geniş ve düzdü. Doru hızla koştu ve sesin geldiği yere çabucak yetişti. Orada kuru yapraklar rüzgarla topaç gibi dönüyordu. Ses bu yapraklardan geliyordu. "Gel, Karatay, bunlar yalnız yaprak!" dedi Doru. Karatay geldi, dönen yapraklara baktı ve güldü. Doru çok sevindi, çünkü arkadaşı artık korkmuyordu.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "rüzgarla topaç gibi dönüyordu"
   - Cümle 10: «Orada kuru yapraklar rüzgarla topaç gibi dönüyordu.»
   - Açıklama: Topaç kartta olmayan bir insan oyuncağı olarak doğa dünyasına giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0014` birebir aynı, `@degisim: yetiştirmek -> yetişmek` (tutuyorsan), ardından `@onarim: 7ecffd6155b602364d3ac5d4c0082fb3c308d0b5`, sonra gövde.

### Hikâye 3: tohum doru-0015 (deneme 3 -> 4)

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
@plan: çalıların arkasından tık tık diye bir ses geldi | cesaretle çalıların arasına baktı ve damlayan suyu buldu
@tohum: doru-0015
@degisim: domates -> damla
Doru sürünün yanındaki ormanda dolaşıyordu. Hava sıcaktı. Birden çalıların arkasından tık tık diye bir ses geldi. Doru bu sesi çok merak etti. Sesin ne olduğunu bulmak istedi. Doru cesaretle başını çalıların arasına uzattı ve baktı. Orada büyük bir kaya vardı. Kayanın üstünden damla damla su düşüyordu. Her damla alttaki taşa değince tık diye ses çıkıyordu. Taşın dibinde küçük bir çukurda su toplanmıştı. Doru bu serin sudan bol bol içti. Sonra sürüsüne katıldı ve yumuşacık çimenlerde mutlu mutlu otladı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çalıların arkasından tık tık diye bir ses geldi"
   - Cümle 3: «Birden çalıların arkasından tık tık diye bir ses geldi.»
   - Açıklama: Bir ses duymak gerçek bir sorun değil; çözülmesi gereken, çocuğun önemseyeceği bir dert yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru bu serin sudan bol bol içti"
   - Cümle 11: «Doru bu serin sudan bol bol içti.»
   - Açıklama: Çukurda birikmiş bilinmeyen suyu içmek çocuğun taklit edebileceği bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0015` birebir aynı, `@degisim: domates -> damla` (tutuyorsan), ardından `@onarim: da8827113752f0ae4d61cd926bec5453e695c99b`, sonra gövde.

### Hikâye 4: tohum doru-0016 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0016
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'bezelye', fiil 'okumak', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: sık ağaçlar yüzünden sürünün gittiği yolu göremediler | toprakta sürünün izlerini bulup peşinden yürüdü
@tohum: doru-0016
@degisim: okumak -> bulmak
Ormanda Doru ile Kırat sürünün arkasından gidiyordu. Kırat yavaş yürüyordu ve ikisi geride kaldı. Ağaçlar çok sıktı ve yol görünmüyordu. Doru Kırat'a yardım etmek istedi. "Yere bak, Doru, sürü iz bırakır," dedi Kırat. Doru başını eğdi ve toprakta taze ayak izleri buldu. "Bak, Kırat, izler bu yoldan gidiyor," dedi Doru. İkisi izlerin peşinden birlikte ilerledi. Az sonra ağaçların arasında geniş bir çayır gördüler. Sürü orada yeşil bezelyeleri yiyordu. Kırat da onların yanına geldi ve mutlu mutlu yemeye başladı. Doru bundan sonra yolu kaybedince toprakta izleri aradı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru Kırat'a yardım etmek istedi"
   - Cümle 4: «Doru Kırat'a yardım etmek istedi.»
   - Açıklama: Tohumdaki yardım özelliği işe yaramıyor, sorunu Kırat'ın öğüdü çözüyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Yere bak, Doru, sürü iz bırakır"
   - Cümle 5: «"Yere bak, Doru, sürü iz bırakır," dedi Kırat.»
   - Açıklama: Çözüm fikrini figür değil yan karakter Kırat buluyor; Doru yalnız söyleneni yapıyor.
   - Açıklama: Çözüm fikrini yan karakter Kırat veriyor, Doru yalnız söyleneni uyguluyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sürü orada yeşil bezelyeleri yiyordu"
   - Cümle 10: «Sürü orada yeşil bezelyeleri yiyordu.»
   - Açıklama: Bezelye ekili bir tarım ürünüdür ve kartın özgür at sürüsü doğa dünyasında yoktur.
   - Açıklama: Bezelye ekili bir tarla ürünüdür ve kartın özgür at sürüsü dünyasında yoktur; yasaklardaki çiftlik dünyasını çağrıştırır.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra yolu kaybedince toprakta izleri aradı"
   - Cümle 12: «Doru bundan sonra yolu kaybedince toprakta izleri aradı.»
   - Açıklama: Alışkanlık anlatan cümlede tek seferlik 'aradı' uyumsuz; 'arardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0016` birebir aynı, `@degisim: okumak -> bulmak` (tutuyorsan), ardından `@onarim: 032c0f9d0fc66cfb7136fcfdaa78024b9aad0d50`, sonra gövde.

### Hikâye 5: tohum doru-0017 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0017
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'ot', fiil 'gülüşmek', sıfat 'şeffaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: uzun bir ot alnına takıldı ve gözünü kapattı | otu dişleriyle yavaşça çekip çıkardı
@tohum: doru-0017
@degisim: şeffaf -> berrak
Bir sabah Doru ile Alaca dağda çimenlerin üstünde yuvarlanıyordu. Alaca kalktı ve derenin berrak suyuna baktı. Alnına uzun bir ot takılmıştı ve ot bir gözünün önüne sarkıyordu. Alaca başını salladı ama ot düşmedi. "Doru, otu çıkaramıyorum," dedi Alaca. Doru hemen ona yardım etmek istedi. Otu dişleriyle yavaşça tuttu ve çekti. Ot alnından çıktı ve yere düştü. Alaca yine suya baktı. "Şimdi her şeyi iyi görüyorum!" dedi Alaca. İkisi birlikte gülüştü. Alaca bundan sonra alnında ot olunca hemen Doru'ya söyledi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "alnında ot olunca hemen Doru'ya söyledi"
   - Cümle 12: «Alaca bundan sonra alnında ot olunca hemen Doru'ya söyledi.»
   - Açıklama: Alışkanlık anlatımında 'söylerdi' olmalı; kip uyumu bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0017` birebir aynı, `@degisim: şeffaf -> berrak` (tutuyorsan), ardından `@onarim: a9a2068747406fb62f4b165f4c523af6de65b042`, sonra gövde.

### Hikâye 6: tohum doru-0018 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0018
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'dal', fiil 'mırıldanmak', sıfat 'siyah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: vadiye giden yolu bulamadı çünkü ağaçlar birbirine benziyordu | hızla küçük arkadaşına koşup yolu sordu
@tohum: doru-0018
Doru ormanda dolaşıyordu. Sonra sürünün yanına dönmek istedi. Ama vadiye giden yolu bulamadı çünkü ağaçlar birbirine benziyordu. Birden ileriden hafif bir ses geldi. Alaca düz bir çimenlikte şarkı mırıldanıyordu. Doru hızla koştu ve onun yanına vardı. "Alaca, vadinin yolunu biliyor musun?" diye sordu Doru. "Evet, siyah dalı olan ağacın yanından gidiyoruz," dedi Alaca. Alaca başını çevirdi ve büyük bir ağacı gösterdi. Ağacın bir dalı siyahtı. İkisi ağacın yanından yürüdü ve az sonra vadiyi gördü. Doru çok sevindi, çünkü Alaca'ya sormuştu ve yolu bulmuştu.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru hızla koştu ve onun yanına vardı"
   - Cümle 6: «Doru hızla koştu ve onun yanına vardı.»
   - Açıklama: Güvenli özellik kullanımı satırı hızı açık ve düz yerde ister; burada Doru ağaçları birbirine benzeyen ormanın içinden hızla koşuyor.
   - Açıklama: Güvenli özellik kullanımı hızı açık ve düz yerde gösterir, burada ağaçlık ormanda koşuyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "vadinin yolunu biliyor musun"
   - Cümle 7: «"Alaca, vadinin yolunu biliyor musun?" diye sordu Doru.»
   - Açıklama: Kartın ilişki alanında Alaca Doru'dan öğrenir; burada ilişki tersine dönüyor.
3. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Evet, siyah dalı olan ağacın yanından gidiyoruz"
   - Cümle 8: «"Evet, siyah dalı olan ağacın yanından gidiyoruz," dedi Alaca.»
   - Açıklama: Kartın yanlar ilişkisinde Alaca Doru'dan öğrenen en küçük üyedir, burada yolu bilen ve Doru'ya yol gösteren o oluyor.
4. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "siyah dalı olan ağacın yanından gidiyoruz"
   - Cümle 8: «"Evet, siyah dalı olan ağacın yanından gidiyoruz," dedi Alaca.»
   - Açıklama: Kartın Alaca ilişkisi onun Doru'dan öğrendiğini söylüyor, burada yolu Doru'ya Alaca öğretiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0018` birebir aynı, ardından `@onarim: e7278cbc2816f954b109a5b4f3a435e05452eb56`, sonra gövde.

### Hikâye 7: tohum doru-0019 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: yarıştığı yaprak derede iki taşın arasına takıldı | burnuyla yaprağı itip taşlardan kurtardı
@tohum: doru-0019
@degisim: çöp -> yaprak
Rüzgar dağda hafif hafif esiyordu. Doru derede akan güzel bir yaprakla yarışıyor ve kenarda hızla koşuyordu. Ama birden yaprak iki taşın arasına takıldı. Yaprak taşları aşamadı ve olduğu yerde kaldı. Doru hemen yaprağın yanına geri döndü. Dere orada çok sığdı. Doru kenarda durdu ve başını suya doğru eğdi. Burnuyla yaprağı yavaşça itti. Yaprak taşların arasından çıktı ve yeniden akmaya başladı. Doru yine düz çimenlerde onun yanında koştu. Doru çok sevindi, çünkü yarış oyunu yeniden başlamıştı.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "derede akan güzel bir yaprakla yarışıyor ve kenarda hızla koşuyordu"
   - Cümle 2: «Doru derede akan güzel bir yaprakla yarışıyor ve kenarda hızla koşuyordu.»
   - Açıklama: Güvenli özellik kullanımı hızı açık ve düz yerde gösterir; burada dere kenarında suyla yarışarak koşuluyor, çocuğun taklit edebileceği su kenarı davranışı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yarışıyor ve kenarda hızla koşuyordu"
   - Cümle 2: «Doru derede akan güzel bir yaprakla yarışıyor ve kenarda hızla koşuyordu.»
   - Açıklama: Tohumdaki hız özelliği yalnız süs olarak geçiyor, sorunu çözmekte işe yaramıyor; çözüm burunla itmek.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kenarda hızla koşuyordu"
   - Cümle 2: «Doru derede akan güzel bir yaprakla yarışıyor ve kenarda hızla koşuyordu.»
   - Açıklama: Tohum özelliği hız yalnız oyunda geçiyor, sorunun çözümünde işe yaramıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "başını suya doğru eğdi"
   - Cümle 7: «Doru kenarda durdu ve başını suya doğru eğdi.»
   - Açıklama: Dere kenarından suya uzanmak çocuğun taklit edebileceği tehlikeli bir davranış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yeniden akmaya başladı"
   - Cümle 9: «Yaprak taşların arasından çıktı ve yeniden akmaya başladı.»
   - Açıklama: Yaprak akmaz, suda sürüklenir; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0019` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: 1bc8b85c5ac7118b99ecccff03bf66c19539bdbd`, sonra gövde.

### Hikâye 8: tohum doru-0023 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0023
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fıstık', fiil 'kavuşmak', sıfat 'gizli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: elmalar yüksekteydi ve küçük arkadaşı onlara uzanamıyordu | dalı dişleriyle salladı ve elmaları yere düşürdü
@tohum: doru-0023
@degisim: fıstık -> elma
Doru dağda Alaca için bir sürpriz hazırlıyordu. Alaca kırmızı elmaları çok severdi. Kayaların arkasında gizli bir elma ağacı vardı ama elmalar yüksekteydi. Küçük Alaca onlara uzanamıyordu. Doru boynunu uzattı ve elmalı bir dalı dişleriyle salladı. Kırmızı elmalar çimenlerin üstüne düştü. Doru elmaları burnuyla ağacın altında bir araya itti. Sonra Alaca'yı çağırdı. "Gel, Alaca, sana bir sürprizim var," dedi Doru. Alaca kayaların arkasına geldi ve elmaları gördü. "Ne kadar çok elma!" dedi Alaca. Alaca koşup elmalara kavuştu ve mutlu mutlu yedi. Doru çok sevindi, çünkü küçük arkadaşına yardım edip onu sevindirmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "koşup elmalara kavuştu"
   - Cümle 12: «Alaca koşup elmalara kavuştu ve mutlu mutlu yedi.»
   - Açıklama: 'Kavuşmak' soyut ve mecazlı bir kelime, 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Alaca koşup elmalara kavuştu"
   - Cümle 12: «Alaca koşup elmalara kavuştu ve mutlu mutlu yedi.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki çocuğa ağır gelen edebi bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0023` birebir aynı, `@degisim: fıstık -> elma` (tutuyorsan), ardından `@onarim: 25615b5ceaa0ae877fe034060738d7fe5e6317bb`, sonra gövde.

### Hikâye 9: tohum doru-0024 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0024
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kova', fiil 'kurutmak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: kayanın arkasından garip bir ıslık sesi geldi | cesurca gidip sesi yapan rüzgarı buldu
@tohum: doru-0024
@degisim: pürüzsüz -> düz
Dağda yağmur yeni dinmişti. Doru ile Kırat ıslak tüylerini kurutmak için güneşli bir kayaya gidiyordu. Birden kayanın arkasından garip bir ıslık sesi geldi. Kırat durdu ve kulaklarını dikti. "Doru, bu ses kayanın arkasından geliyor," dedi Kırat. Doru cesurca kayanın arkasına yürüdü ve baktı. Kayada kova gibi yuvarlak bir delik vardı. Rüzgar bu delikten geçiyor ve ıslık çalıyordu. "Gel, Kırat, bu ıslığı rüzgar çalıyor!" dedi Doru. Kırat da geldi ve deliğe baktı. İkisi düz kayanın yanında güneşte durdu ve tüyleri kurudu. "Teşekkürler, Doru, artık o sesi biliyoruz!" dedi Kırat.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "bu ses kayanın arkasından geliyor"
   - Cümle 5: «"Doru, bu ses kayanın arkasından geliyor," dedi Kırat.»
   - Açıklama: Replik bir önceki anlatım cümlesini gereksizce tekrarlıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kayada kova gibi yuvarlak"
   - Cümle 7: «Kayada kova gibi yuvarlak bir delik vardı.»
   - Açıklama: Kova kartta olmayan bir insan eşyası olarak doğa dünyasına giriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "delikten geçiyor ve ıslık çalıyordu"
   - Cümle 8: «Rüzgar bu delikten geçiyor ve ıslık çalıyordu.»
   - Açıklama: Rüzgarın ıslık çalması kişileştirme ve mecazdır; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Rüzgarın ıslık çalması bir mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0024` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: 6231dc269fc51ec7af6f4d3a3d577e7ce7fac738`, sonra gövde.

### Hikâye 10: tohum doru-0025 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0025
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yıldız', fiil 'doyurmak', sıfat 'ışıltılı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: arkadaşı acıktı ama başka elma kalmamıştı | bulduğu elmaların yarısını arkadaşına verdi
@tohum: doru-0025
@degisim: yıldız -> elma
Ormanda büyük bir elma ağacı vardı. Doru ağacın dibinde dört ışıltılı elma buldu. Az sonra Karatay koşarak geldi, ama başka elma kalmamıştı. "Doru, karnım çok acıktı," dedi Karatay. Karatay ağaca baktı ve üzüldü. Doru elmalara ve arkadaşına baktı. Doru arkadaşına yardım etmek istedi. "Gel, Karatay, bu elmaları paylaşalım," dedi Doru. Doru iki elmayı burnuyla Karatay'ın önüne itti. İki arkadaş elmaları yan yana yedi. Tatlı elmalar ikisini de doyurdu. Karatay kuyruğunu neşeyle salladı. Doru çok sevindi, çünkü elmalarını arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dört ışıltılı elma buldu"
   - Cümle 2: «Doru ağacın dibinde dört ışıltılı elma buldu.»
   - Açıklama: Elmalar ışıltılı olmaz; kelime nesnesine uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dört ışıltılı elma"
   - Cümle 2: «Doru ağacın dibinde dört ışıltılı elma buldu.»
   - Açıklama: 'Işıltılı' 3 yaşındaki çocuğun bilmeyeceği bir kelime; 'parlak' olmalı.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Doru, karnım çok acıktı"
   - Cümle 4: «"Doru, karnım çok acıktı," dedi Karatay.»
   - Açıklama: Arkadaşın acıktığı sorun ancak 4. cümlede söyleniyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru arkadaşına yardım etmek istedi"
   - Cümle 7: «Doru arkadaşına yardım etmek istedi.»
   - Açıklama: Doru adı art arda dört cümlenin başında gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0025` birebir aynı, `@degisim: yıldız -> elma` (tutuyorsan), ardından `@onarim: a80f0d30c1e52179dfc68b71115223909c52f477`, sonra gövde.

### Hikâye 11: tohum doru-0026 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0026
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bulut', fiil 'giydirmek', sıfat 'meraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesi saklandı ama beyaz kayalar arasında görünmüyordu | hızla koşup kayaların arkasına tek tek baktı
@tohum: doru-0026
@degisim: giydirmek -> koşmak
Doru ile annesi dağda sırayla saklambaç oynuyordu. Önce annesi saklandı ve Doru onu aramaya başladı. Ama çayırda bulut gibi beyaz kayalar çoktu ve Doru annesini göremedi. Doru meraklı gözlerle etrafına baktı. Kayalar birbirinden uzaktı ve aralarındaki çayır düzdü. Doru hızla koştu ve kayaların arkasına tek tek baktı. Sonunda en büyük kayanın arkasında annesini buldu. "Buldum seni, anne!" dedi Doru. "Beni buldun, Doru!" dedi annesi ve güldü. Şimdi saklanma sırası Doru'daydı. "Bu oyun çok güzel, anneciğim, şimdi sen beni ara!" dedi Doru.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bulut gibi beyaz kayalar çoktu ve Doru annesini göremedi"
   - Cümle 3: «Ama çayırda bulut gibi beyaz kayalar çoktu ve Doru annesini göremedi.»
   - Açıklama: Beyaz kayaların anneyi neden gizlediği söylenmiyor ve saklambaçta aramak oyunun kendisi, gerçek bir sorun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru meraklı gözlerle etrafına"
   - Cümle 4: «Doru meraklı gözlerle etrafına baktı.»
   - Açıklama: 'Meraklı gözlerle' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0026` birebir aynı, `@degisim: giydirmek -> koşmak` (tutuyorsan), ardından `@onarim: 6118fa262f4f24bc511cdc5c05c71653107186e8`, sonra gövde.

### Hikâye 12: tohum doru-0027 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0027
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kırıntı', fiil 'çoğalmak', sıfat 'şirin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: uzaktan gelen bir ses yüzünden uyuyamadı | hızla koşup taşa vuran kuru dalı çimene bıraktı
@tohum: doru-0027
@degisim: kırıntı -> dal
Rüzgar esiyordu. Doru parkta şirin çiçeklerin arasına uzanmıştı. Uyumak istiyordu ama uzaktan tık tık diye bir ses geliyordu. Doru bu ses yüzünden uyuyamadı. Rüzgar daha çok esti ve sesler çoğaldı. Doru sesin nereden geldiğini merak etti. Ses parkın öbür ucundaki taşlardan geliyordu. Doru kalktı ve düz çimende hızla koştu. Az sonra taşlara vardı. Taşların üstünde kuru bir dal vardı. Rüzgar esince dal taşa vuruyor ve tık tık ediyordu. Doru dalı dişleriyle tuttu ve yumuşak çimene bıraktı. Tık tık sesi durdu. Doru çiçeklerin arasına geri döndü ve mutlu mutlu uyudu.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Doru parkta şirin çiçeklerin"
   - Cümle 2: «Doru parkta şirin çiçeklerin arasına uzanmıştı.»
   - Açıklama: Kartın park tarifi sürünün otladığı geniş bir çayırdır; metin dizide olmayan bir 'park' yeri kuruyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Doru parkta şirin çiçeklerin"
   - Cümle 2: «Doru parkta şirin çiçeklerin arasına uzanmıştı.»
   - Açıklama: Kart notuna göre dizide park yok; metin yeri çayır yerine park diye adlandırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0027` birebir aynı, `@degisim: kırıntı -> dal` (tutuyorsan), ardından `@onarim: 88ab1a69f5804f016cfec839f84a9cdd594a9bc8`, sonra gövde.
