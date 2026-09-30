# Editör görevi (onarım): Doru, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0073 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0073
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'ceviz', fiil 'keşfetmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: ceviz yuvarlandı ve içi boş bir kütüğe girdi | cesaretle kütüğün öbür ucundan bakıp cevizi çıkardı
@tohum: doru-0073
@degisim: keşfetmek -> bulmak
Bir sabah Doru ile Kırat, sürünün çimen yediği parkta oynuyordu. Kırat bir cevizi saklıyor, Doru da onu buluyordu. Ama bu kez ceviz yuvarlandı ve içi boş bir kütüğe girdi. Kütüğün içinde hiçbir şey görünmüyordu. "Ceviz içeride kaldı, Doru," dedi Kırat. Doru önce durdu, sonra cesaretle kütüğün öbür ucuna gitti. Oradan içeri baktı ve cevizi gördü. Ceviz bu tarafa çok yakındı. Doru ağzıyla onu tuttu ve dışarı çıkardı. "Aferin, Doru, cevizi kurtardın!" dedi Kırat. Kırat bu kez cevizi çizgili bir taşın arkasına sakladı. Doru onu hemen buldu ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "sürünün çimen yediği parkta"
   - Cümle 1: «Bir sabah Doru ile Kırat, sürünün çimen yediği parkta oynuyordu.»
   - Açıklama: Kartın park tarifi bir çayırdır ve dizide park yoktur; gövde yeri insan dünyasına ait 'park' adıyla anıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0073` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 85f2fcd8d9ee3bb18779be9604b52b12e4a33504`, sonra gövde.

### Hikâye 2: tohum doru-0099 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0099
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: bir şey yapmak
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'hazine', fiil 'şekillendirmek', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: çiçeğin toprağı kuruydu çünkü dere suyu gelmiyordu | toprakta su yolu açtı ve dereye bir taş koydu
@tohum: doru-0099
@degisim: şekillendirmek -> kazmak
Bir sabah Doru dağda bir derenin yanında yürüyordu. Orada sarı bir çiçek gördü. Çiçeğin yaprakları aşağı eğilmişti, çünkü toprağı çok kuruydu. Dere yakından akıyordu ama suyu çiçeğe gitmiyordu. Doru çiçeğe yardım etmek istedi. Önce ayağıyla toprağı kazdı ve bir su yolu açtı. Derenin kenarında düz ve ilginç bir taş vardı. Bu taş Doru'nun küçük hazinesiydi. Doru hazinesini burnuyla itti ve suyun içine koydu. Su taşa çarptı ve yeni yoldan aktı. Su çiçeğin dibine geldi ve toprak ıslandı. Çiçeğin yaprakları yavaş yavaş yukarı kalktı. Doru çiçeğe baktı ve çok sevindi. Doru bundan sonra kuru bir çiçek görünce ona su yolu açardı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu taş Doru'nun küçük hazinesiydi"
   - Cümle 8: «Bu taş Doru'nun küçük hazinesiydi.»
   - Açıklama: 'Hazine' burada mecazlı ve 3 yaşındaki çocuğa uygun değil.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Bu taş Doru'nun küçük hazinesiydi"
   - Cümle 8: «Bu taş Doru'nun küçük hazinesiydi.»
   - Açıklama: Kartta Doru'nun hazinesi ya da sahip olduğu bir eşya yok; kapalı dünyaya yeni bir eşya ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu taş Doru'nun küçük hazinesiydi"
   - Cümle 8: «Bu taş Doru'nun küçük hazinesiydi.»
   - Açıklama: Taşın Doru'nun hazinesi olduğu kuruluyor ama bu hiçbir şekilde işlenmiyor; Doru hazinesini hiç tepkisiz suya atıyor.
   - Açıklama: Derenin kenarındaki taşın Doru'nun hazinesi olması sebepsiz ve işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0099` birebir aynı, `@degisim: şekillendirmek -> kazmak` (tutuyorsan), ardından `@onarim: 3b5f47538baded4adc782d6a536f888742a9776f`, sonra gövde.

### Hikâye 3: tohum doru-0101 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0101
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'dilim', fiil 'erimek', sıfat 'işaretli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: yolda çok kalın kar vardı ve yürümek zordu | önden yürüyüp karda ayak izleri bıraktı
@tohum: doru-0101
@degisim: dilim -> kar
Doru, Kırat ile dağın karlı tepesindeydi. Biraz aşağıda kar erimişti ve yeşil çimenler çıkmıştı. Ama yolda çok kalın kar vardı. "Bu karda yürümek bana zor, Doru," dedi Kırat. Doru daha önce hiç önde gitmemişti. Yine de Kırat'a yardım etmek istedi. "Ben önde gideyim, sen de beni izle," dedi Doru. Doru yavaşça yürüdü ve arkasında derin ayak izleri kaldı. Kırat da izlerle işaretli yoldan rahatça yürüdü. Sonunda ikisi çimenlerin yanına geldi. "Teşekkürler, Doru," dedi Kırat. Doru bundan sonra karda hep önde yürüdü.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru daha önce hiç önde gitmemişti"
   - Cümle 5: «Doru daha önce hiç önde gitmemişti.»
   - Açıklama: Doru'nun hiç önde gitmemiş olması bir zorluk gibi kuruluyor ama olayda hiçbir işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "izlerle işaretli yoldan"
   - Cümle 9: «Kırat da izlerle işaretli yoldan rahatça yürüdü.»
   - Açıklama: 'İşaretli yol' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir anlatım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "izlerle işaretli yoldan rahatça"
   - Cümle 9: «Kırat da izlerle işaretli yoldan rahatça yürüdü.»
   - Açıklama: 'İzlerle işaretli yol' ifadesi 3 yaşındaki bir çocuk için soyut ve ağır; 'Doru'nun izlerine basarak' gibi somut olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0101` birebir aynı, `@degisim: dilim -> kar` (tutuyorsan), ardından `@onarim: ebd86dbf8ef6125c31b75fbe87494b364e7c9240`, sonra gövde.

### Hikâye 4: tohum doru-0102 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0102
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'mısır', fiil 'yıkanmak', sıfat 'ahşap'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: saklanırken yelesi çalının dallarına takıldı | cesaretle arkadaşından yardım istedi
@tohum: doru-0102
@degisim: ahşap -> sarı
Rüzgar esiyordu. Doru ile Karatay ormanda saklambaç oynuyordu. Yağmurda yıkanmış yapraklar parlıyordu. Doru, mısır sarısı çiçekli bir çalının arkasına saklandı. Ama yelesi çalının dallarına takıldı. Doru başını çekti ama yelesi dallarda kaldı. Doru seslenirse oyunu Karatay kazanacaktı. Yine de Doru cesaretle seslendi. "Karatay, bana yardım eder misin?" dedi Doru. Karatay hemen çalının yanına koştu. Dalı dişleriyle tuttu ve yavaşça yana çekti. Doru başını dışarı çıkardı. İkisi birlikte güldü. "Teşekkürler, Karatay, hadi yine oynayalım!" dedi Doru.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yağmurda yıkanmış yapraklar parlıyordu"
   - Cümle 3: «Yağmurda yıkanmış yapraklar parlıyordu.»
   - Açıklama: Yer betimi ikinci kez ekleniyor ve olmayan bir yağmuru ima eden işlevsiz bir ayrıntı oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0102` birebir aynı, `@degisim: ahşap -> sarı` (tutuyorsan), ardından `@onarim: bb7e478ba0bb28daa54500ca800bf1797c845528`, sonra gövde.

### Hikâye 5: tohum doru-0104 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0104
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'fasulye', fiil 'yapıştırmak', sıfat 'sadık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: arkadaşı çiçeklerin önündeki uzun otlardan geçemedi | önden yürüyüp otları ayırdı ve yol açtı
@tohum: doru-0104
@degisim: fasulye -> çiçek
Parkta yağmur yeni dinmişti. Doru ile Alaca uzaktaki mor çiçeklerde küçük kelebekler gördü. Ama çiçeklerin önündeki uzun otları yağmur birbirine yapıştırmıştı. "Buradan geçemiyorum, Doru," dedi Alaca. "Ben önden giderim, sen beni izle," dedi Doru. Doru'nun başı otlardan yüksekti. Doru cesaretle öne geçti ve otları iki yana itti. Sadık Alaca, Doru'nun hemen arkasından yürüdü. Az sonra ikisi mor çiçeklerin yanına çıktı. Kelebekler çiçeklerin üstünde uçuyordu. "Teşekkürler, Doru, yolu sen açtın!" dedi Alaca. Doru ile Alaca kelebekleri mutlu mutlu izledi.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta yağmur yeni dinmişti"
   - Cümle 1: «Parkta yağmur yeni dinmişti.»
   - Açıklama: Kartın park tarifi sürünün otladığı geniş bir çayırdır ve dizide park yoktur; gövde yeri park olarak adlandırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0104` birebir aynı, `@degisim: fasulye -> çiçek` (tutuyorsan), ardından `@onarim: 2fa726c714fcc0392964f3190d70b9368b33a93b`, sonra gövde.

### Hikâye 6: tohum doru-0106 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0106
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'ayçiçeği', fiil 'durdurmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: elma taşa çarptı ve dikenli çalılara yuvarlandı | hızlıca koşup elmayı ayağıyla durdurdu
@tohum: doru-0106
@degisim: elmalı -> yuvarlak
Doru ormandaki düz ve açık bir yerde oyun oynuyordu. En sevdiği yuvarlak elmayı burnuyla bir ayçiçeğine doğru itiyordu. Birden elma bir taşa çarptı ve dikenli çalılara doğru yuvarlandı. Elma çalılara girerse Doru onu alamayacaktı. Doru düz yerde hızlıca koştu ve elmanın önüne geçti. Elmayı ayağıyla nazikçe durdurdu. Sonra Doru elmayı yine burnuyla itti. Bu kez taşı dikkatle dolaştı. Elma sonunda ayçiçeğinin dibine vardı. Doru elmayı ayçiçeğinin yanında yedi. Doru çok sevindi, çünkü elmasını dikenlerden kurtarmıştı.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "elma taşa çarptı ve dikenli çalılara yuvarlandı"
   - Cümle 0 (plan satırı): «elma taşa çarptı ve dikenli çalılara yuvarlandı | hızlıca koşup elmayı ayağıyla durdurdu»
   - Açıklama: Gövdede elma çalılara girmiyor, yalnız çalılara doğru yuvarlanıyor ve önceden durduruluyor.
   - Açıklama: Gövdede elma çalılara girmiyor, yalnız çalılara doğru yuvarlanıyor ve Doru onu önceden durduruyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu kez taşı dikkatle dolaştı"
   - Cümle 8: «Bu kez taşı dikkatle dolaştı.»
   - Açıklama: 'Taşı dolaştı' engelin çevresinden geçmek anlamında yanlış; 'taşın çevresinden dolandı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0106` birebir aynı, `@degisim: elmalı -> yuvarlak` (tutuyorsan), ardından `@onarim: 472b86106c16263062b8ed58b160b9cbb88f969a`, sonra gövde.

### Hikâye 7: tohum doru-0110 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0110
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'tüy', fiil 'esmek', sıfat 'düz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: rüzgar esince yuvadaki tüy kayadan düşüyordu | cesaretle yuvaya gidip tüyü iki taşın arasına soktu
@tohum: doru-0110
Dağın düz tepesinde Doru ile Kırat yuva oyunu oynuyordu. Büyük bir kaya onların yuvası oldu. Yuvanın üstüne beyaz bir tüy koydular. Ama rüzgar esince tüy hep kayadan düşüyordu. "Tüy olmadan yuva olmaz, Doru," dedi Kırat. Doru tüyü ağzıyla yerden aldı. Rüzgar çok sertti ama Doru cesaretle yuvanın yanına gitti. Tüyü kayanın yanındaki iki taşın arasına sıkıca soktu. Rüzgar yine esti ama tüy düşmedi, yalnız sallandı. "Bak, Kırat, tüy artık düşmüyor!" dedi Doru. Doru ile Kırat oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "rüzgar esince tüy hep kayadan düşüyordu"
   - Cümle 4: «Ama rüzgar esince tüy hep kayadan düşüyordu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Rüzgar çok sertti ama Doru cesaretle"
   - Cümle 7: «Rüzgar çok sertti ama Doru cesaretle yuvanın yanına gitti.»
   - Açıklama: Dağ tepesinde sert rüzgarda cesaretle ilerlemek yüksek yerde taklit edilebilecek riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0110` birebir aynı, ardından `@onarim: aee665656334aabf5b757fe1a9866c662b0fbf86`, sonra gövde.

### Hikâye 8: tohum doru-0112 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0112
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'lokma', fiil 'yetişmek', sıfat 'akıllı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: ikisi de acıkmıştı ve ağaçta tek bir elma vardı | hızla koşup elmayı getirdi ve annesiyle paylaştı
@tohum: doru-0112
@degisim: akıllı -> kırmızı
Bir sabah Doru ile annesi dağda uzun bir yol yürüdü. İkisi de çok acıkmıştı ama orada hiç çimen yoktu. Doru biraz ileride bir elma ağacı gördü. Ağaçta tek bir kırmızı elma yetişmişti. Annesi uzun yoldan çok yorulmuştu. "Anne, sen burada dinlen, ben elmayı getiririm," dedi Doru. Doru düz yerde hızla koştu ve ağaca vardı. Elmayı daldan ağzıyla kopardı. Sonra elmayı annesine getirdi. "Bu elma ikimize de yeter," dedi Doru. Önce annesi küçük bir lokma aldı, sonra Doru. "Çok teşekkür ederim, Doru," dedi annesi. Doru çok mutluydu, çünkü elmayı annesiyle paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu elma ikimize de yeter"
   - Cümle 10: «"Bu elma ikimize de yeter," dedi Doru.»
   - Açıklama: Çok acıkmış iki atın tek elmadan birer küçük lokmayla doyması açlık sorunuyla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0112` birebir aynı, `@degisim: akıllı -> kırmızı` (tutuyorsan), ardından `@onarim: 117dc1fcadf0aad4192c43b41b06a0aad7211cf2`, sonra gövde.

### Hikâye 9: tohum doru-0118 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0118
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'top', fiil 'yakalanmak', sıfat 'ferah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: annesi durmadan kuyruğunu sallıyordu | kuyruğa takılan ot topunu burnuyla itip çıkardı
@tohum: doru-0118
@degisim: yakalanmak -> takılmak
Park ferah ve serindi. Doru ile annesi çimen yiyordu. Annesi birden durmadan kuyruğunu sallamaya başladı. Doru bunu çok merak etti ve annesine yaklaştı. "Anne, neden kuyruğunu sallıyorsun?" diye sordu Doru. "Bir şey var ama göremiyorum," dedi annesi. Doru dikkatle baktı ve küçük, kuru bir ot topu gördü. Top, uzun kuyruğa sıkıca takılmıştı. "Dur, anneciğim, sana yardım edeyim," dedi Doru. Doru topu burnuyla yavaşça itti. Ot topu çıktı ve çimenlere düştü. "Teşekkürler, Doru," dedi annesi. Doru çok sevindi, çünkü annesinin neden kuyruğunu salladığını bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Park ferah ve serindi"
   - Cümle 1: «Park ferah ve serindi.»
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Park ferah ve serindi"
   - Cümle 1: «Park ferah ve serindi.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; hikaye yeri çayır değil park olarak adlandırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0118` birebir aynı, `@degisim: yakalanmak -> takılmak` (tutuyorsan), ardından `@onarim: da815574d99c81b6159bcccc24a7593c6258a397`, sonra gövde.

### Hikâye 10: tohum doru-0119 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: yakında hiç çiçek yoktu | hızla koşup uzaktan çiçek getirdi ve paylaştı
@tohum: doru-0119
@degisim: buket -> çiçek
Bir sabah dağda çimenlerin üstünde küçük su damlaları toplanmıştı. Doru ile Alaca orada çimen yiyordu. Alaca üzgündü, çünkü yakında hiç çiçek yoktu. "Ben daha önce çiçek yemedim," dedi Alaca. Doru uzakta, düz bir yerde sarı çiçekler gördü. "Bekle, Alaca, hemen dönerim!" dedi Doru. Doru oraya hızla koştu. Ağzıyla birkaç çiçek kopardı ve geri döndü. Doru çiçekleri Alaca'nın önüne, tertemiz çimenin üstüne koydu. "Gel, bunları birlikte yiyelim," dedi Doru. İkisi çiçekleri yan yana yedi. Doru çok mutluydu, çünkü çiçeklerini Alaca ile paylaşmıştı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ben daha önce çiçek yemedim"
   - Cümle 4: «"Ben daha önce çiçek yemedim," dedi Alaca.»
   - Açıklama: Sorunun sebebi zayıf; Alaca'nın yakında çiçek olmamasına neden üzüldüğü akla yatkın biçimde kurulmuyor.
   - Açıklama: Alaca'nın üzüntüsünün sebebi belirsiz ve zayıf; yakında çiçek olmaması neden önemli bir sorun olduğu akla yatkın biçimde kurulmuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: ""Gel, bunları birlikte yiyelim," dedi Doru"
   - Cümle 10: «"Gel, bunları birlikte yiyelim," dedi Doru.»
   - Açıklama: Kırdan koparılan çiçekleri yemek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0119` birebir aynı, `@degisim: buket -> çiçek` (tutuyorsan), ardından `@onarim: 254e01abf7e16741158d8fb3cf9fcdf88e9c23ca`, sonra gövde.

### Hikâye 11: tohum doru-0120 (deneme 3 -> 4)

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
Bir sabah dağda rüzgar esmeye başladı. Doru, annesiyle birlikte bir çalının yanında çimen yiyordu. Birden kocaman, kuru bir ot topu annesine doğru yuvarlandı. Annesi şaşırdı ve geri çekildi. "Doru, bu da ne?" dedi annesi. Doru biraz korktu ama cesaretle ot topuna yaklaştı. Burnuyla ona dokundu ve kokladı. "Korkma, anne, bu yalnız kuru ot," dedi Doru. Sonra ot topunu burnuyla itti ve uzağa yuvarladı. Annesi rahatladı. Sonra cömert anne en taze çimenleri Doru'ya bıraktı. Doru çok sevindi, çünkü annesi artık korkmuyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra cömert anne en"
   - Cümle 11: «Sonra cömert anne en taze çimenleri Doru'ya bıraktı.»
   - Açıklama: 'Cömert' 3 yaşındaki çocuğun bilmeyeceği soyut bir sıfat ve anneyi yeniden tanıtır gibi kullanılmış.
   - Açıklama: 'Cömert' kahramanın kart kelimesi değil ve 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0120` birebir aynı, `@degisim: palmiye -> çalı` (tutuyorsan), ardından `@onarim: a2905be30ac969aa6accd5e17cdac7d46b469d7a`, sonra gövde.

### Hikâye 12: tohum doru-0121 (deneme 3 -> 4)

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
@plan: şeftali ağacı çok uzun otların arasındaydı | cesaretle otların arasına girip şeftali getirdi
@tohum: doru-0121
Kuşlar ormanda neşeyle ötüyordu. Doru, Kırat'a bir sürpriz hazırlamak istedi. Kırat şeftaliyi çok severdi ama buralarda hiç şeftali yoktu. Şeftali ağacı ormanın öbür yanında, çok uzun otların arasındaydı. O otlar Doru'nun başından da yüksekti. Doru önce durdu, sonra cesaretle otların arasına girdi. Ağacın altında yere düşmüş iki olgun şeftali buldu. Doru şeftalileri ağzıyla tek tek taşıdı. Onları Kırat'ın dinlendiği ağacın dibine, beyaz çiçeklerin yanına koydu. Sonra bir çalının arkasına saklandı ve izledi. Kırat başını kaldırdı ve şeftalileri gördü. Onları keyifle yedi. Doru çok sevindi, çünkü sürprizi Kırat'ı mutlu etmişti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kırat şeftaliyi çok severdi ama buralarda hiç şeftali yoktu.»
   - Açıklama: Plandaki asıl sorun olan uzun otlar ilk üç cümlede değil ancak 4. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Şeftali ağacı ormanın öbür yanında, çok uzun otların arasındaydı"
   - Cümle 4: «Şeftali ağacı ormanın öbür yanında, çok uzun otların arasındaydı.»
   - Açıklama: Plandaki asıl sorun olan uzun otlar ancak dördüncü cümlede söyleniyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle otların arasına girdi"
   - Cümle 6: «Doru önce durdu, sonra cesaretle otların arasına girdi.»
   - Açıklama: Doru başından yüksek otların arasına tek başına giriyor; çocuğun taklit edebileceği görünmez bir yere girme davranışı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0121` birebir aynı, ardından `@onarim: aec84b1698013bcf46d0cb43e999600f43d0d940`, sonra gövde.
