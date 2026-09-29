# Editör görevi (onarım): Doru, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0048 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0048
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'köpük', fiil 'ıslatmak', sıfat 'komik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: susamıştı ama su içtiği çukur kuruydu | dinleyip hızla koştu ve sesi yapan dereyi buldu
@tohum: doru-0048
Doru ormanda çok susamıştı. Ama su içtiği küçük çukur kuruydu. Doru başka su bulmak için durdu ve dikkatle dinledi. Uzaktan şırıl şırıl bir ses geliyordu. Doru bu sesin sudan gelip gelmediğini merak etti. Ağaçların arasında geniş ve düz bir açıklık vardı. Doru açıklıkta hızla koştu ve sesin geldiği yere vardı. Orada küçük bir dere taşların üstünden akıyordu. Su taşlara çarpıyor ve beyaz köpükler yapıyordu. Ses buradan geliyordu. Doru başını eğdi ve dereden içti. Serin su Doru'nun burnunu ıslattı. Burnunda biraz köpük kaldı ve Doru çok komik göründü. Sonra Doru derenin kenarında mutlu mutlu otladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geniş ve düz bir açıklık"
   - Cümle 6: «Ağaçların arasında geniş ve düz bir açıklık vardı.»
   - Açıklama: 'Açıklık' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Burnunda biraz köpük kaldı ve Doru çok komik göründü"
   - Cümle 13: «Burnunda biraz köpük kaldı ve Doru çok komik göründü.»
   - Açıklama: Köpük ve komik görünme ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0048` birebir aynı, ardından `@onarim: a6a4d7dec1a3cefa2f9e7f450df87c21dc0a3298`, sonra gövde.

### Hikâye 2: tohum doru-0049 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0049
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'iz', fiil 'solmak', sıfat 'enerjik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: küçük çiçekler susuz kalmış ve solmuştu | izin yanından yürüdü ve taşı itip suyun yolunu açtı
@tohum: doru-0049
@degisim: enerjik -> neşeli
Bir sabah Doru parktaki geniş çayırda çok neşeliydi ve zıplaya zıplaya dolaşıyordu. Birden çimenlerin arasında küçük çiçekler gördü. Çiçekler susuz kalmış ve solmuştu. Biraz ileride ince ve ıslak bir iz vardı. Doru bu izin nereden geldiğini çok merak etti. İzin yanından yavaşça yürüdü. İzi küçük bir kaynaktan akan ince bir su yapıyordu. Su büyük bir taşın önünde birikmişti. Taş suyun çiçeklere giden yolunu kapatmıştı. Doru çiçeklere yardım etmek istedi. Başıyla taşı itti ve kenara yuvarladı. Su hemen kuru toprağa aktı ve çiçeklerin dibini ıslattı. Doru çok sevindi ve çayırda koşup oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İzi küçük bir kaynaktan akan ince bir su yapıyordu"
   - Cümle 7: «İzi küçük bir kaynaktan akan ince bir su yapıyordu.»
   - Açıklama: 'Kaynak' kelimesi ve izi suyun yapması anlatımı 3 yaşındaki çocuk için anlaşılması güç.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0049` birebir aynı, `@degisim: enerjik -> neşeli` (tutuyorsan), ardından `@onarim: 001a59b0f8359191cef0011932fb8f64a4c969cd`, sonra gövde.

### Hikâye 3: tohum doru-0050 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0050
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'şemsiye', fiil 'üflemek', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: en güzel otlar ağır bir dalın altında kalmıştı | arkadaşıyla dalı birlikte çekti ve yığını yaptı
@tohum: doru-0050
@degisim: şemsiye -> ot
Parktaki geniş çayırda güneş parlıyordu. Doru ile Karatay öğle yemeği için büyük bir ot yığını yapıyordu. Ama en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı. Karatay dalı tek başına çekemedi ve burnundan üfledi. Doru hemen arkadaşına yardım etmek istedi. Dalın bir ucunu dişleriyle tuttu. Karatay da öbür ucunu tuttu. İkisi dalı birlikte kenara çekti. Sonra ikisi güzel otları kopardı ve yığına taşıdı. Yığın kocaman oldu ve nefis kokuyordu. Doru ile Karatay ot yığınının yanında mutlu mutlu yemek yedi.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parktaki geniş çayırda güneş"
   - Cümle 1: «Parktaki geniş çayırda güneş parlıyordu.»
   - Açıklama: Kartın park tarifi yalnız sürünün çimen yediği çayırdır ve dizide park yoktur; metin yeri insan parkı olarak adlandırıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Doru hemen arkadaşına yardım etmek istedi"
   - Cümle 5: «Doru hemen arkadaşına yardım etmek istedi.»
   - Açıklama: Dalı çekmeye Karatay girişiyor ve Doru yalnız ona yardım ediyor; figür sorunun sahibi ve çözücüsü değil yardımcı konumunda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0050` birebir aynı, `@degisim: şemsiye -> ot` (tutuyorsan), ardından `@onarim: 6e22619f28e27a65d198ffb4a400eaa83ac0e13c`, sonra gövde.

### Hikâye 4: tohum doru-0051 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0051
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kök', fiil 'rahatlamak', sıfat 'meşgul'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: yolun ortasında kahverengi ve kalın bir şey duruyordu | cesaretle yaklaştı ve onun bir kök olduğunu gördü
@tohum: doru-0051
@degisim: meşgul -> taze
Ormanda hafif bir rüzgar esiyordu. Doru keşif oyunu oynuyordu ve büyük meşe ağacına gidiyordu. Ama yolun ortasında kahverengi, kalın bir şey duruyordu. Doru onun ne olduğunu bilmiyordu. "Anne, yolda ne var?" diye sordu Doru. Annesi yakında taze çimen yiyordu. Hemen gelip Doru'nun yanında durdu. "Gel, birlikte bakalım," dedi annesi. Doru cesaretle kahverengi şeye yaklaştı ve onun bir ağaç kökü olduğunu gördü. Doru rahatladı ve güldü. Kökün üstünden hopladı ve ağaca ulaştı. "Anne, ağaca vardım!" dedi Doru. Annesi gülümsedi ve Doru keşif oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru keşif oyunu oynuyordu"
   - Cümle 2: «Doru keşif oyunu oynuyordu ve büyük meşe ağacına gidiyordu.»
   - Açıklama: 'Keşif' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Keşif' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0051` birebir aynı, `@degisim: meşgul -> taze` (tutuyorsan), ardından `@onarim: 0be98b0f4896679112e4ee80d1afef4ac4f79681`, sonra gövde.

### Hikâye 5: tohum doru-0052 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0052
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kozalak', fiil 'dinlemek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: oyun için ağaçların altında hiç kozalak yoktu | dikkatle dinledi ve kozalak düşen çam ağacını buldu
@tohum: doru-0052
Bir sabah dağda her yer çok sessizdi. Doru ile Alaca kozalak oyunu oynamak istiyordu. Ama yakındaki ağaçların altında hiç kozalak yoktu. Küçük Alaca çok üzüldü ve başını eğdi. Doru arkadaşına yardım etmek istedi. Durdu ve dikkatle dinledi. Birden uzaktan tık diye bir ses geldi. Doru sese doğru baktı ve büyük bir çam ağacı gördü. Ağacın dalından bir kozalak daha yere düştü. İkisi birlikte çam ağacının altına yürüdü. Orada yerde bir sürü kozalak vardı. Doru en büyük kozalakları burnuyla Alaca'nın önüne itti. Alaca kozalakları çimenin üstünde yuvarladı ve güldü. Doru çok sevindi, çünkü küçük arkadaşı mutlu mutlu oynuyordu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakındaki ağaçların altında hiç kozalak yoktu"
   - Cümle 3: «Ama yakındaki ağaçların altında hiç kozalak yoktu.»
   - Açıklama: Ağaçların altında neden kozalak olmadığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0052` birebir aynı, ardından `@onarim: 3c68bb5aed0b3103913efe919682cb14fa39a584`, sonra gövde.

### Hikâye 6: tohum doru-0053 (deneme 2 -> 3)

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
@plan: ağaçların arasından gelen ince sesi merak etti | cesaretle sese yürüdü ve delikli dalı buldu
@tohum: doru-0053
@degisim: çan -> dal
Rüzgar ormanda esiyordu. Doru ağaçların yanında taze otları yiyordu. Birden ağaçların arasından ince bir ses geldi ve Doru çok merak etti. Belki küçük bir hayvan orada sıkışmıştı. Doru bir an durdu, sonra cesaretle sese doğru yürüdü. Ses, eğri bir ağacın kuru dalından geliyordu. Dalda küçük, yuvarlak bir delik vardı. Rüzgar deliğe girdikçe daldan tatlı bir ses çıkıyordu. Orada sıkışmış bir hayvan yoktu. Rüzgar biraz daha hızlı esince ses daha da güzelleşti. Doru ağacın yanındaki çimenlerde sesi dinleyerek mutlu mutlu otladı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "cesaretle sese yürüdü"
   - Cümle 0 (plan satırı): «ağaçların arasından gelen ince sesi merak etti | cesaretle sese yürüdü ve delikli dalı buldu»
   - Açıklama: Plan satırında 'doğru' eksik; 'sese doğru yürüdü' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "daldan tatlı bir ses"
   - Cümle 8: «Rüzgar deliğe girdikçe daldan tatlı bir ses çıkıyordu.»
   - Açıklama: Ses için 'tatlı' mecazlı bir kullanım; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0053` birebir aynı, `@degisim: çan -> dal` (tutuyorsan), ardından `@onarim: 3ab87b321c64ec88cf579557b83138091593f117`, sonra gövde.

### Hikâye 7: tohum doru-0054 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0054
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'portakal', fiil 'eklemek', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: kaya yokuşun başındaydı ve elmaların çoğu aşağı yuvarlandı | elmaları çamurda buldu ve cesaretle çamurdan çıkardı
@tohum: doru-0054
@degisim: portakal -> elma
Doru, Kırat ile dağda yürüyordu. Kırat sürü için büyük bir kayanın dibine elma toplamıştı. Ama kaya bir yokuşun başındaydı ve elmaların çoğu aşağı yuvarlanmıştı. "Elmalarım kayboldu, Doru," dedi Kırat. Doru yere baktı. Çimenin üstünde dağınık birkaç elma vardı. Doru bu elmaların gittiği yoldan yavaşça yürüdü. Yokuşun dibinde sığ ve yumuşak bir çamur vardı. Elmalar bu çamura saplanmıştı. Doru bir an durdu. Sonra cesaretle çamurun içine girdi. Doru elmaları ağzıyla tek tek çamurdan çıkardı. Sonra hepsini taşıdı ve kayanın yanındaki elmalara ekledi. "Teşekkürler, Doru, sürü bu elmalara çok sevinecek!" dedi Kırat.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sığ ve yumuşak bir çamur"
   - Cümle 8: «Yokuşun dibinde sığ ve yumuşak bir çamur vardı.»
   - Açıklama: 'Sığ' su için kullanılır; çamura uygun düşmüyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra cesaretle çamurun içine girdi"
   - Cümle 11: «Sonra cesaretle çamurun içine girdi.»
   - Açıklama: Cesaret övülerek bilinmeyen bir çamurun içine giriliyor; çocuk taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0054` birebir aynı, `@degisim: portakal -> elma` (tutuyorsan), ardından `@onarim: bb63ac03093e769751a4e4e371c1f184e2e19711`, sonra gövde.

### Hikâye 8: tohum doru-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0059
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'külah', fiil 'tamamlanmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: turuncu çiçekler uzaktaydı ve arkadaşı birazdan uyanacaktı | hızla koşup çiçekleri getirdi ve arkadaşının çevresine dizdi
@tohum: doru-0059
@degisim: külah -> çiçek
Dağdaki düz bir yerde Kırat bir kayanın yanında uyuyordu. Doru ona en sevdiği turuncu çiçeklerle bir sürpriz yapmak istedi. Ama çiçekler uzaktaydı ve güneş kayaya gelince Kırat uyanacaktı. Doru düz vadide hızla koştu. Çiçeklerin yanına geldi ve ağzıyla bir demet çiçek kopardı. Sonra çiçekleri ağzında taşıyarak geri döndü. Çiçekleri Kırat'ın çevresine tek tek dizdi. Sonunda turuncu çiçeklerden bir halka tamamlandı. Tam o anda güneş kayaya geldi ve Kırat gözlerini açtı. "Sürpriz, Kırat!" dedi Doru. Kırat çiçeklere baktı ve güldü. "Çiçekler çok güzel, teşekkür ederim, Doru!" dedi Kırat.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Doru ona en sevdiği turuncu çiçeklerle"
   - Cümle 2: «Doru ona en sevdiği turuncu çiçeklerle bir sürpriz yapmak istedi.»
   - Açıklama: 'En sevdiği' çiçeklerin Doru'nun mu Kırat'ın mı olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0059` birebir aynı, `@degisim: külah -> çiçek` (tutuyorsan), ardından `@onarim: 9e07c80652e65e66f381e65d829ac8df252a87eb`, sonra gövde.

### Hikâye 9: tohum doru-0061 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0061
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'yonca', fiil 'uyutmak', sıfat 'bomboş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: sıcak güneşte en sevdiği yerdeki yonca kurumuştu | yeri bilen atın yanına gidip sordu ve oraya koştu
@tohum: doru-0061
@degisim: uyutmak -> sormak
Kuşlar vadide neşeyle ötüyordu. Doru'nun karnı bomboştu. Hemen en sevdiği yoncaların yanına gitti. Ama güneş çok sıcaktı ve bütün yonca kurumuştu. Doru başka bir yonca yeri bilmiyordu. Biraz ileride Kırat bir kayanın gölgesinde dinleniyordu. Doru, Kırat'ın yanına gitti. "Kırat, taze yonca nerede var?" diye sordu Doru. "Vadinin öbür ucunda, büyük çam ağacının yanında taze yonca var," dedi Kırat. Doru, Kırat'a teşekkür etti. Sonra düz vadide hızla koştu. Büyük çam ağacının yanında yemyeşil yonca vardı. Doru karnını doyurdu. Doru çok sevindi, çünkü Kırat'a sormuş ve taze yonca bulmuştu.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama güneş çok sıcaktı ve bütün yonca kurumuştu.»
   - Açıklama: Yoncanın kuruduğu sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0061` birebir aynı, `@degisim: uyutmak -> sormak` (tutuyorsan), ardından `@onarim: d7f1a0c7f9fe6e8510e4130f106767ca5561e6d4`, sonra gövde.

### Hikâye 10: tohum doru-0062 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0062
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'filiz', fiil 'çekmek', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: son kütüğün üstünde değişik bir şey vardı | cesaretle yaklaştı ve kuru dalı kenara çekti
@tohum: doru-0062
Hafif bir yağmur yeni dinmişti. Doru ormanda yerdeki küçük kütüklerin üstünden atlama oyunu oynuyordu. Ama son kütüğün üstünde değişik bir şey vardı ve Doru atlayamadı. Doru onun ne olduğunu bilmiyordu. Doru bir an bekledi, sonra cesaretle yaklaştı. Bu, rüzgarın kütüğün üstüne düşürdüğü kuru bir daldı. Doru dalı ağzıyla tuttu ve kenara çekti. Dalın altında minicik, yeşil bir filiz vardı. Doru ona basmadan son kütüğün üstünden de atladı. Doru çok sevindi, çünkü oyununu bitirmişti.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru onun ne olduğunu"
   - Cümle 4: «Doru onun ne olduğunu bilmiyordu.»
   - Açıklama: Doru adı art arda cümlelerin başında gereksiz yere tekrarlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dalın altında minicik, yeşil bir filiz"
   - Cümle 8: «Dalın altında minicik, yeşil bir filiz vardı.»
   - Açıklama: Filiz önemli bir şeymiş gibi kuruluyor ama olayda hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dalın altında minicik, yeşil bir filiz vardı"
   - Cümle 8: «Dalın altında minicik, yeşil bir filiz vardı.»
   - Açıklama: Filiz sebepsiz beliriyor ve yalnız üstüne basılmadığı söylenerek olaya bir şey katmadan geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0062` birebir aynı, ardından `@onarim: 5aa8d1134578cd533d1001bcfe79b7b216f5cbe0`, sonra gövde.

### Hikâye 11: tohum doru-0063 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0063
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çimen', fiil 'güzelleştirmek', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: dikenli tohumlar sırtına yapıştı ve düşmedi | annesinden tohumları almasını istedi
@tohum: doru-0063
Dağda yumuşak bir çimen vardı ve orada benekli çiçekler açmıştı. Doru çimene yattı ve sağa sola yuvarlandı. Ama kuru, dikenli tohumlar sırtına yapıştı. Doru kendini salladı ama tohumlar düşmedi. Ağzı da sırtına yetişmedi. Doru annesine gitti ve tohumları almasını istedi. Annesinin dişleri sırtına çok yakındı ama Doru cesaretle hiç kıpırdamadı. Böylece annesi tohumları dişleriyle kolayca aldı. Sonunda son tohum da yere düştü. Sonra annesi Doru'nun tüylerini burnuyla düzeltti ve güzelleştirdi. Doru ile annesi benekli çiçeklerin yanında mutlu mutlu otladı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dağda yumuşak bir çimen vardı"
   - Cümle 1: «Dağda yumuşak bir çimen vardı ve orada benekli çiçekler açmıştı.»
   - Açıklama: 'Bir çimen' tekil kullanımı yanlış; 'çimenlik' ya da 'çimenler' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşak bir çimen vardı"
   - Cümle 1: «Dağda yumuşak bir çimen vardı ve orada benekli çiçekler açmıştı.»
   - Açıklama: 'Bir çimen' tek ot anlamına gelir; 'çimenlik' ya da 'çimenler' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru cesaretle hiç kıpırdamadı"
   - Cümle 7: «Annesinin dişleri sırtına çok yakındı ama Doru cesaretle hiç kıpırdamadı.»
   - Açıklama: Tohumdaki cesaret özelliği sorunu çözmüyor, annesinin dişlerinden korkma gibi zorlama bir biçimde ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0063` birebir aynı, ardından `@onarim: eb095d84beb1adb5812135bfd6f9ee1f0cd2b469`, sonra gövde.

### Hikâye 12: tohum doru-0065 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0065
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'zeytin', fiil 'sokulmak', sıfat 'nazik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşı zeytin ağacını tanımadığı için yanlış ağaca koştu | zeytin ağacının yapraklarını anlatıp ona yardım etti
@tohum: doru-0065
Doru ile Alaca geniş çayırda bir koşu oyunu oynuyordu. Sırayla zeytin ağacına koşup burnuyla ona dokunuyorlardı. Sıra Alaca'ya gelince o yanlış ağaca koştu, çünkü zeytin ağacını tanımıyordu. Alaca geri döndü ve üzgün üzgün başını eğdi. Doru, Alaca'ya yardım etmek istedi. "Zeytin ağacının küçük, gri yaprakları var, Alaca," dedi Doru nazik bir sesle. Alaca çayıra dikkatle baktı ve o ağacı buldu. Bu kez doğru ağaca gitti ve ona dokundu. Sonra sevinçle geri geldi ve Doru'ya sokuldu. "Seninle oynamak çok güzel, Doru!" dedi Alaca.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Alaca geniş çayırda bir koşu oyunu"
   - Cümle 1: «Doru ile Alaca geniş çayırda bir koşu oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "burnuyla ona dokunuyorlardı"
   - Cümle 2: «Sırayla zeytin ağacına koşup burnuyla ona dokunuyorlardı.»
   - Açıklama: Çoğul özneyle tekil iyelik uyumsuz; 'burunlarıyla' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0065` birebir aynı, ardından `@onarim: 691f99df04f39136def7a905f0bba8415603fe05`, sonra gövde.
