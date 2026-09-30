# Editör görevi (onarım): Doru, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar35.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0119
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'buket', fiil 'toplanmak', sıfat 'tertemiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: sürü buradaki bütün çiçekleri yemişti | hızla koşup uzaktan çiçek getirdi ve paylaştı
@tohum: doru-0119
@degisim: buket -> çiçek
Bir sabah Doru ile Alaca dağda çimen yiyordu. Sürü yola çıkmak için toplanıyordu. Alaca üzgündü, çünkü sürü buradaki bütün çiçekleri yemişti. "Ben daha hiç çiçek yemedim," dedi Alaca. Doru uzakta, düz bir yerde sarı çiçekler gördü. "Bekle, Alaca, hemen dönerim!" dedi Doru. Doru oraya hızla koştu. Ağzıyla birkaç çiçek kopardı ve geri döndü. Sürü daha yola çıkmamıştı. Doru çiçekleri Alaca'nın önüne, tertemiz çimenin üstüne koydu. "Gel, bunları birlikte yiyelim," dedi Doru. İkisi çiçekleri yan yana yedi. Doru çok mutluydu, çünkü çiçeklerini Alaca ile paylaşmıştı.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sürü yola çıkmak için toplanıyordu"
   - Cümle 2: «Sürü yola çıkmak için toplanıyordu.»
   - Açıklama: Belirsiz kelime sürü canlı ve eylem yapan bir karakter olarak geçiyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "sürü buradaki bütün çiçekleri yemişti"
   - Cümle 3: «Alaca üzgündü, çünkü sürü buradaki bütün çiçekleri yemişti.»
   - Açıklama: Arka plandaki çoğul canlı sürü çiçekleri yiyerek sorunu yaratıp olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0119` birebir aynı, `@degisim: buket -> çiçek` (tutuyorsan), ardından `@onarim: 02e6c0b2197944b1c391d734e200dafdb5f028a5`, sonra gövde.

### Hikâye 2: tohum doru-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0120
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'palmiye', fiil 'başlamak', sıfat 'cömert'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: kuru bir ot topu annesine doğru yuvarlandı | cesaretle ot topunun yanına gidip onu uzağa itti
@tohum: doru-0120
@degisim: palmiye -> çalı
Bir sabah dağda rüzgar esmeye başladı. Doru, annesiyle birlikte bir çalının yanında çimen yiyordu. Birden kocaman, kuru bir ot topu annesine doğru yuvarlandı. Annesi şaşırdı ve geri çekildi. "Doru, bu da ne?" dedi annesi. Doru biraz korktu ama cesaretle ot topuna yaklaştı. Burnuyla ona dokundu ve kokladı. "Korkma, anne, bu yalnız kuru ot," dedi Doru. Sonra ot topunu burnuyla itti ve uzağa yuvarladı. Annesi rahatladı ve cömert davranıp en taze çimenleri Doru'ya bıraktı. Doru çok sevindi, çünkü annesi artık korkmuyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "cömert davranıp en taze"
   - Cümle 10: «Annesi rahatladı ve cömert davranıp en taze çimenleri Doru'ya bıraktı.»
   - Açıklama: 'Cömert davranmak' soyut bir kavram ve 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Cömert davranmak' soyut bir kavram ve figürün özellik kelimesi değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0120` birebir aynı, `@degisim: palmiye -> çalı` (tutuyorsan), ardından `@onarim: ba88872cd7e012a56f5e99768616eadd4e88f2c2`, sonra gövde.

### Hikâye 3: tohum doru-0121 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0121
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'şeftali', fiil 'izlemek', sıfat 'beyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yaşlı atın sevdiği şeftaliler uzun otların arasındaydı | cesaretle otların arasına girip şeftali getirdi
@tohum: doru-0121
Kuşlar ormanda neşeyle ötüyordu. Doru, Kırat'a bir sürpriz hazırlamak istedi. Kırat şeftaliyi çok severdi ama buralarda hiç şeftali yoktu. Şeftali ağacı ormanın öbür yanında, uzun otların arasındaydı. Doru önce durdu, sonra cesaretle otların arasına girdi. Ağacın altında yere düşmüş iki olgun şeftali buldu. Doru şeftalileri ağzıyla tek tek taşıdı. Onları Kırat'ın dinlendiği ağacın dibine, beyaz çiçeklerin yanına koydu. Sonra bir çalının arkasına saklandı ve izledi. Kırat başını kaldırdı ve şeftalileri gördü. Yaşlı at şeftalileri keyifle yedi. Doru çok sevindi, çünkü sürprizi Kırat'ı mutlu etmişti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şeftali ağacı ormanın öbür yanında, uzun otların arasındaydı"
   - Cümle 4: «Şeftali ağacı ormanın öbür yanında, uzun otların arasındaydı.»
   - Açıklama: Uzun otların neden bir engel ya da korku sebebi olduğu söylenmiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yaşlı at şeftalileri keyifle yedi"
   - Cümle 11: «Yaşlı at şeftalileri keyifle yedi.»
   - Açıklama: Gövdede Kırat hiç 'yaşlı at' diye tanıtılmadığı için bu adın Kırat'ı gösterdiği belli değil, yeni bir at gibi okunuyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yaşlı at şeftalileri keyifle"
   - Cümle 11: «Yaşlı at şeftalileri keyifle yedi.»
   - Açıklama: 'Yaşlı at' gövdede tanıtılmadığından Kırat mı Doru mu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0121` birebir aynı, ardından `@onarim: 9b1d69dd3111abbbfd4cb2e28f7f5709bd782c5c`, sonra gövde.

### Hikâye 4: tohum doru-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0123
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: paylaşmak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'uçurtma', fiil 'güvenmek', sıfat 'konuşkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşının önündeki çimenler çok kısaydı | önündeki iki elmayı onunla paylaştı
@tohum: doru-0123
@degisim: uçurtma -> elma
Geniş çayırda Doru ile Alaca çimen yiyordu. Ama Alaca'nın önündeki çimenler çok kısaydı ve Alaca doyamadı. Doru'nun önünde ise ağaçtan düşmüş iki kırmızı elma vardı. "Gel, Alaca, bu elmaları paylaşalım," dedi Doru. Doru hemen Alaca'ya yardım etti ve bir elmayı ona doğru itti. "Elma nedir? Acı mı? Sert mi?" diye sordu konuşkan Alaca. "Elma tatlıdır, bana güven," dedi Doru. Alaca Doru'ya güvendi ve elmayı ısırdı. İki arkadaş elmalarını yan yana, sevinçle yedi. "Teşekkürler, Doru, elma çok güzelmiş!" dedi Alaca.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Geniş çayırda Doru ile Alaca"
   - Cümle 1: «Geniş çayırda Doru ile Alaca çimen yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "diye sordu konuşkan Alaca"
   - Cümle 8: «Sert mi?" diye sordu konuşkan Alaca.»
   - Açıklama: Kartın yanlar bölümündeki Alaca ilişkisinde konuşkanlık yok; yan karaktere kartta olmayan bir huy veriliyor.
   - Açıklama: Kartın yanlar bölümünde Alaca için konuşkanlık özelliği yok; yan karakter karttaki tanımın dışına çıkıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elma tatlıdır, bana güven"
   - Cümle 9: «"Elma tatlıdır, bana güven," dedi Doru.»
   - Açıklama: 'Güvenmek' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Güven' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0123` birebir aynı, `@degisim: uçurtma -> elma` (tutuyorsan), ardından `@onarim: ebb5e747cdbb456cac428b3e6bc82d54a517b7d0`, sonra gövde.

### Hikâye 5: tohum doru-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0124
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'avokado', fiil 'koklamak', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: elmalar çok yüksekteydi ve uzanamadı | yaşlı ata sordu ve alçak dalı buldu
@tohum: doru-0124
@degisim: avokado -> elma
Ormanda ağaçların arasından tatlı bir koku geliyordu. Doru havayı kokladı ve bir elma ağacı buldu. Ama kırmızı elmalar çok yüksekteydi ve Doru onlara uzanamadı. Yaşlı Kırat yakında, kahverengi bir kütüğün yanında dinleniyordu. "Kırat, elmalar çok yüksek, onlara nasıl ulaşırım?" diye sordu Doru. "Dar yoldan geç, orada alçak bir dal var," dedi Kırat. Doru cesaretle o yoldan yürüdü. Gerçekten de alçak bir dalda elmalar vardı. Doru bir elmayı dişleriyle koparıp yedi. Sonra bir tane de Kırat'a getirdi. Doru çok mutlu oldu, çünkü Kırat'a sormuş ve elmalara ulaşmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "elmalar çok yüksekteydi ve uzanamadı"
   - Cümle 0 (plan satırı): «elmalar çok yüksekteydi ve uzanamadı | yaşlı ata sordu ve alçak dalı buldu»
   - Açıklama: Plan satırında 'uzanamadı' fiilinin öznesi 'elmalar' gibi okunuyor; Doru'nun uzanamadığı dilbilgisel olarak belirtilmemiş.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "yaşlı ata sordu ve alçak dalı buldu"
   - Cümle 0 (plan satırı): «elmalar çok yüksekteydi ve uzanamadı | yaşlı ata sordu ve alçak dalı buldu»
   - Açıklama: Belirsiz kelime yaşlı bir rol olarak karakteri adlandırmak için kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0124` birebir aynı, `@degisim: avokado -> elma` (tutuyorsan), ardından `@onarim: ffeec92b19eed42f38069eeab99851591bbcde3a`, sonra gövde.

### Hikâye 6: tohum doru-0126 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0126
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çuval', fiil 'tanışmak', sıfat 'pembe'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: koşarken aynı anda sayamıyordu | küçük arkadaşından saymasını istedi
@tohum: doru-0126
@degisim: çuval -> çiçek
Doru vadide küçük Alaca ile yeni tanışmıştı. Doru uzaktaki pembe çiçeklere koşup hemen geri dönmek istiyordu. Ama koşarken saymayı hep unutuyordu ve ne kadar çabuk döndüğünü bilemiyordu. Doru biraz düşündü. "Alaca, ben koşarken sen sayar mısın?" diye sordu Doru. "Tabii, Doru!" dedi Alaca ve saymaya başladı. Doru hemen vadinin düz ve açık yerinde hızla koştu. Pembe çiçeklere dokundu ve geri döndü. Alaca sekiz derken Doru onun yanına gelmişti. Doru sevinçle Alaca'ya teşekkür etti. Doru bundan sonra tek başına yapamadığı işlerde arkadaşlarından yardım istedi.
```

**Hakem bulguları (5):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "vadide küçük Alaca ile yeni tanışmıştı"
   - Cümle 1: «Doru vadide küçük Alaca ile yeni tanışmıştı.»
   - Açıklama: Kartın yanlar alanına göre Alaca Doru'nun sürüsündeki en küçük üye ve ondan öğrenen biri; onunla yeni tanışmış olması ilişkiye aykırı.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "vadide küçük Alaca ile yeni tanışmıştı"
   - Cümle 1: «Doru vadide küçük Alaca ile yeni tanışmıştı.»
   - Açıklama: Diziyi izleyen çocuk Alaca'yı Doru'nun sürüsünden tanır; yeni tanışma yanlış bilgi verir.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "küçük Alaca ile yeni tanışmıştı"
   - Cümle 1: «Doru vadide küçük Alaca ile yeni tanışmıştı.»
   - Açıklama: Yanlar alanına göre Alaca sürünün en küçük üyesi ve Doru'nun ona hep yardım ettiği bir sürü arkadaşıdır, yeni tanışılan biri değildir.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru vadide küçük Alaca ile yeni tanışmıştı"
   - Cümle 1: «Doru vadide küçük Alaca ile yeni tanışmıştı.»
   - Açıklama: Başlıktaki yer dağ ama hikaye vadide geçiyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tek başına yapamadığı işlerde arkadaşlarından yardım istedi"
   - Cümle 11: «Doru bundan sonra tek başına yapamadığı işlerde arkadaşlarından yardım istedi.»
   - Açıklama: Son cümle olaydan çıkan somut bir ders değil, 'işler' gibi soyut ve genellenmiş bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0126` birebir aynı, `@degisim: çuval -> çiçek` (tutuyorsan), ardından `@onarim: f645ffed70bba3740958e5c03ef1e6d3743b32d8`, sonra gövde.

### Hikâye 7: tohum doru-0127 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0127
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'yem', fiil 'dikmek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: kayadan ağlama gibi ince bir ses geldi | cesaretle kayaya yaklaştı ve sesi yapan deliği buldu
@tohum: doru-0127
@degisim: dikmek -> dinlemek
Doru sıcacık bir sabah dağda yem arıyordu. Birden büyük bir kayadan ince bir ağlama sesi geldi. Doru orada küçük bir hayvan olduğunu düşündü ve üzüldü. Yemini bıraktı ve sesi dikkatle dinledi. Ses hep kayanın aynı yerinden geliyordu. Doru cesaretle kayaya yavaşça yaklaştı. Kayanın üstünde küçük, yuvarlak bir delik vardı. Rüzgar esince bu delikten o ses çıkıyordu. Orada hiç hayvan yoktu. Doru rahatladı ve kayanın yanındaki taze otları yedi. Doru böylece garip bir sesin bazen yalnız rüzgar olduğunu öğrendi.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "ince bir ağlama sesi geldi"
   - Cümle 2: «Birden büyük bir kayadan ince bir ağlama sesi geldi.»
   - Açıklama: Kayadan gelen gizemli ağlama sesi küçük çocuk için ürkütücü bir öğe.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kayadan ince bir ağlama sesi geldi"
   - Cümle 2: «Birden büyük bir kayadan ince bir ağlama sesi geldi.»
   - Açıklama: Kayadan gelen gizemli ağlama sesi küçük çocuk için ürkütücü olabilir.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "büyük bir kayadan ince bir ağlama sesi geldi"
   - Cümle 2: «Birden büyük bir kayadan ince bir ağlama sesi geldi.»
   - Açıklama: Kayadan gelen gizemli ağlama sesi küçük çocuklar için ürkütücü olabilir.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Yemini bıraktı ve sesi"
   - Cümle 4: «Yemini bıraktı ve sesi dikkatle dinledi.»
   - Açıklama: Doru yem arıyordu ama elinde yem varmış gibi yemini bırakıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0127` birebir aynı, `@degisim: dikmek -> dinlemek` (tutuyorsan), ardından `@onarim: 6c895652736f3781e0c9ece8fed2355395750b17`, sonra gövde.

### Hikâye 8: tohum doru-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0128
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'düğüm', fiil 'yazmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesini dinlemedi ve annesinin kuyruğu dallara takıldı | özür diledi ve düğümü dişleriyle açtı
@tohum: doru-0128
@degisim: yazmak -> çekmek
Doru annesini dinlemedi ve dağda sık çalıların arasına koştu. Annesi arkasından geldi ve uzun kuyruğu dallara takıldı. Kuyruğunda küçük bir düğüm oldu. Doru geri döndü ve annesine baktı. "Özür dilerim, anneciğim, seni dinlemeliydim," dedi Doru. "Tamam, Doru, önce bu düğümü çözelim," dedi annesi. Doru yardım etmek için dişleriyle dalları tek tek çekti. Sonra düğümü de yavaşça açtı. Doru bir dalı daha çekmek istedi. "Bu kadar yeterli, kuyruğum kurtuldu," dedi annesi. Annesi Doru'yu burnuyla okşadı. "Bundan sonra seni hep dinleyeceğim, anneciğim," dedi Doru.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru bir dalı daha çekmek istedi"
   - Cümle 9: «Doru bir dalı daha çekmek istedi.»
   - Açıklama: Düğüm açıldıktan sonra bir dal daha çekme isteği işlevsiz bir ayrıntı.
   - Açıklama: Düğüm çözüldükten sonra gelen bu olay hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0128` birebir aynı, `@degisim: yazmak -> çekmek` (tutuyorsan), ardından `@onarim: 27103010d6d95452d1f105a5402281db2627d95e`, sonra gövde.

### Hikâye 9: tohum doru-0129 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0129
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bitki', fiil 'boşaltmak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşının sevdiği bitki vadinin öbür yanında büyüyordu | düz vadide koşup bitkileri getirdi
@tohum: doru-0129
@degisim: sabırlı -> tatlı
Rüzgar dağda serin serin esiyordu. Doru, Karatay'a küçük bir sürpriz hazırlamak istedi. Ama Karatay'ın sevdiği tatlı bitki vadinin öbür yanında büyüyordu. Karatay dereden su içiyordu. Az sonra geri gelecekti. Doru düz vadide hızla koştu. Orada yeşil bitkileri ağzına doldurdu. Sonra aynı yoldan geri döndü. Ağzındaki bitkileri düz bir taşın üstüne boşalttı. Tam o sırada Karatay geldi ve taşa baktı. Karatay sevinçle zıpladı ve hepsini yedi. Doru böylece küçük bir sürprizin Karatay'ı çok mutlu ettiğini öğrendi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tatlı bitki vadinin öbür yanında büyüyordu"
   - Cümle 3: «Ama Karatay'ın sevdiği tatlı bitki vadinin öbür yanında büyüyordu.»
   - Açıklama: Bitkinin uzakta büyümesi gerçek bir sorun değil; Doru hiçbir engelle karşılaşmadan gidip getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0129` birebir aynı, `@degisim: sabırlı -> tatlı` (tutuyorsan), ardından `@onarim: b826e0dc35b129623870b8d555a679a5594a07a2`, sonra gövde.

### Hikâye 10: tohum doru-0130 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0130
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'lale', fiil 'serinletmek', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yağmur damlaları küçük çiçeği çamura doğru itiyordu | başını çiçeğin üstüne uzattı ve onu korudu
@tohum: doru-0130
Yağmur taşlara tık tık vurdu ve sıcak dağı serinletti. Doru kayaların yanında küçük, kırmızı bir lale gördü. Damlalar çiçeği çamurlu toprağa doğru itiyordu. Çiçeğin ince sapı kırılacak gibiydi. Doru çiçeğe yardım etmek için hemen yanına gitti. Başını ve boynunu çiçeğin üstüne uzattı. Artık su çiçeğe değil, Doru'nun sırtına düşüyordu. Doru hiç kıpırdamadan bekledi. Bir süre sonra yağmur dindi ve güneş çıktı. Doru başını kaldırdı ve geri çekildi. Küçük lale yavaş yavaş kalktı ve yeniden düz durdu. Doru çok sevindi, çünkü çiçeğin sapı kırılmamıştı.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Artık su çiçeğe değil, Doru'nun sırtına düşüyordu"
   - Cümle 7: «Artık su çiçeğe değil, Doru'nun sırtına düşüyordu.»
   - Açıklama: Doru başını ve boynunu uzatmışken suyun sırtına düştüğü söyleniyor; bu anlatımla çelişiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "lale yavaş yavaş kalktı"
   - Cümle 11: «Küçük lale yavaş yavaş kalktı ve yeniden düz durdu.»
   - Açıklama: Çiçek için 'kalktı' uygun değil; 'doğruldu' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Küçük lale yavaş yavaş kalktı"
   - Cümle 11: «Küçük lale yavaş yavaş kalktı ve yeniden düz durdu.»
   - Açıklama: Çiçek kalkmaz; 'doğruldu' olmalı, fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0130` birebir aynı, ardından `@onarim: 19c026cc86f20fa01ea5374687e95750707dfc11`, sonra gövde.

### Hikâye 11: tohum doru-0131 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0131
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çubuk', fiil 'gezdirmek', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yağmur yaklaşıyordu ve kuru yerin yolunu bilmiyordu | yaşlı ata yolu sordu ve düz yoldan koştu
@tohum: doru-0131
@degisim: gezdirmek -> göstermek
Doru ormanda Kırat'la birlikte yürüyordu. Birden gökte kara bulutlar toplandı ve yağmur yaklaştı. Doru kuru bir yere gitmek istedi ama yolu bilmiyordu. Temkinli Kırat ormanı çok iyi tanıyordu. Doru ondan yolu göstermesini istedi. Kırat, kırık çubuklarla dolu yolu değil, yanındaki düz yolu gösterdi. Doru o düz yolda hızla koştu. Yağmur başlamadan büyük bir kayanın altına ulaştı. Kırat da yavaş yavaş arkasından geldi. Sonra yağmur başladı ama ikisi de kuru kaldı. Doru ile Kırat, kayanın altında yağmuru mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yaşlı ata yolu sordu"
   - Cümle 0 (plan satırı): «yağmur yaklaşıyordu ve kuru yerin yolunu bilmiyordu | yaşlı ata yolu sordu ve düz yoldan koştu»
   - Açıklama: Gövdede yol sorulan Kırat yaşlı bir at olarak geçmiyor, plan çözümü yanlış söylüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Temkinli Kırat ormanı"
   - Cümle 4: «Temkinli Kırat ormanı çok iyi tanıyordu.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0131` birebir aynı, `@degisim: gezdirmek -> göstermek` (tutuyorsan), ardından `@onarim: 8c832f06552c5098d9d840861f96730c437aaac0`, sonra gövde.

### Hikâye 12: tohum doru-0134 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0134
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'örgü', fiil 'gitmek', sıfat 'uzak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: küçük at saklanırken oyun yerini göremedi | sesini duyup koştu ve onu geri getirdi
@tohum: doru-0134
@degisim: örgü -> ağaç
Ormanda Doru ile Alaca saklanma oyunu oynuyordu. Alaca saklanmak için uzak ağaçlara gitti. Oradan geri dönmek istedi ama oyun yerini göremedi. "Doru, neredesin?" diye seslendi Alaca. Doru bu sesi hemen duydu. Ağaçlara kadar düz çimende hızla koştu. Az sonra Alaca'yı büyük bir ağacın altında buldu. "Seni buldum, Alaca!" dedi Doru. "İyi ki geldin, Doru," dedi Alaca. "Benimle gel," dedi Doru. Alaca onun arkasından yürüdü ve oyun yerine döndüler. Sonra iki arkadaş oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sesini duyup koştu ve onu geri getirdi"
   - Cümle 0 (plan satırı): «küçük at saklanırken oyun yerini göremedi | sesini duyup koştu ve onu geri getirdi»
   - Açıklama: Plan satırında koşanın kim olduğu ve 'sesini' ile 'onu' zamirlerinin kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0134` birebir aynı, `@degisim: örgü -> ağaç` (tutuyorsan), ardından `@onarim: 7cad2a01b5e03530ce8ae25db311ad01d69eb271`, sonra gövde.
