# Editör görevi (onarım): Doru, onarım partisi 3

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 4 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar3.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar3.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0003 (deneme 3 -> 4)

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
Parkta büyük bir ağaç vardı. Doru bu ağacın gölgesinde dinlenmek istedi. Ama ağacın altı taşlı ve sertti. Doru orada yumuşak bir yatak yapmaya karar verdi. Çayırın ucunda büyük bir kaya duruyordu. Kayanın dibi karanlıktı ve orada yeşil yosunlar vardı. Doru karanlıktan korkmadı ve cesaretle kayanın dibine yürüdü. Yosunu dişleriyle tuttu ve çekti. Yosun taştan kolayca ayrıldı. Doru yosunları tek tek ağacın altına taşıdı. Hepsini taşların üstüne serdi. Ağacın altı yumuşacık oldu. Doru yeni yatağına uzandı ve gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta büyük bir ağaç vardı"
   - Cümle 1: «Parkta büyük bir ağaç vardı.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır ve kartın notuna göre dizide park yoktur; metin yeri park olarak adlandırıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kayanın dibi karanlıktı ve orada yeşil yosunlar vardı"
   - Cümle 6: «Kayanın dibi karanlıktı ve orada yeşil yosunlar vardı.»
   - Açıklama: Kayanın dibindeki karanlık hiçbir engel oluşturmuyor ve yalnız cesaret özelliğini göstermek için sebepsizce kuruluyor.
   - Açıklama: Kaya ve yosun Doru aramadan çözümü getirmek için sebepsizce beliriyor, karanlık da bir engel gibi kurulup hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0003` birebir aynı, `@degisim: kibar -> yumuşak` (tutuyorsan), ardından `@onarim: f5368bea4bebca43dcbf4067050c3bda72790b9d`, sonra gövde.

### Hikâye 2: tohum doru-0004 (deneme 3 -> 4)

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
Bir sabah Doru ile Kırat ormanda su içmeye geldi. Ama yağmurdan sonra küçük gölün suyu çamurlu olmuştu. Kırat bu suyu içemedi ve üzüldü. Doru, Kırat için temiz su bulmaya karar verdi. Uzaktan hafif bir su sesi geliyordu. Ormanın içinden o sese doğru geniş ve düz bir yol gidiyordu. Doru bu yolda hızla koştu. Kırat da yavaş yavaş Doru'nun arkasından geldi. Yolun sonunda küçük bir dere vardı. Derenin suyu çok temiz ve berraktı, dibindeki taşlar görünüyordu. Kırat dereye gelince temiz sudan bol bol içti. Sonra başını sevgiyle Doru'ya sürttü. Doru çok sevindi, çünkü Kırat artık temiz su içebiliyordu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru bu yolda hızla koştu"
   - Cümle 7: «Doru bu yolda hızla koştu.»
   - Açıklama: Doru'nun hızla koşması hiçbir işe yaramıyor; Kırat yavaş yavaş gelip dereye yine ulaşıyor ve hız çözümde rol oynamıyor.
   - Açıklama: Doru'nun hızla koşması hiçbir işe yaramıyor, çünkü Kırat zaten yavaş yavaş gelip suyu ancak kendisi varınca içiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok temiz ve berraktı"
   - Cümle 10: «Derenin suyu çok temiz ve berraktı, dibindeki taşlar görünüyordu.»
   - Açıklama: 'Berrak' 3 yaşındaki bir çocuğun bilmeyeceği edebi bir kelime.
   - Açıklama: 'Berrak' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime ve 'temiz' ile aynı şeyi söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0004` birebir aynı, `@degisim: patlıcan -> su` (tutuyorsan), ardından `@onarim: 8373dab76a2fda20823f021e192c2e0b6601bb10`, sonra gövde.

### Hikâye 3: tohum doru-0006 (deneme 3 -> 4)

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
@plan: uzun yoldan gelen at çok acıkmıştı | dört elmanın yarısını ona götürdü
@tohum: doru-0006
@degisim: iplik -> elma
Bir sabah Doru dağda küçük bir elma ağacı buldu. Ağacın altında yalnız dört elma vardı, ikisi kırmızı ve ikisi yeşildi. Yanındaki Kırat uzun bir yoldan gelmişti ve çok acıkmıştı. Doru, Kırat'a yardım etmek ve elmaları paylaşmak istedi. Doru elmaları eşleştirdi ve her kırmızı elmanın yanına bir yeşil elma koydu. Bir kırmızı ve bir yeşil elmayı ağzıyla Kırat'a götürdü. "Bu iki elma senin, Kırat," dedi Doru. "Teşekkür ederim, Doru, gel birlikte yiyelim," dedi Kırat. Doru kalan iki elmayı da getirdi. İkisi yan yana durdu ve elmalarını yedi. Elmalar çok tatlıydı. Doru çok mutlu oldu, çünkü elmalarını paylaşınca Kırat da doymuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bir kırmızı ve bir yeşil elmayı ağzıyla Kırat'a götürdü"
   - Cümle 6: «Bir kırmızı ve bir yeşil elmayı ağzıyla Kırat'a götürdü.»
   - Açıklama: Kırat Doru'nun hemen yanında olduğu söylendiği halde Doru elmaları ona uzaktan götürüp getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0006` birebir aynı, `@degisim: iplik -> elma` (tutuyorsan), ardından `@onarim: df047033e0125410547f4da35f78a01182c1ba7d`, sonra gövde.

### Hikâye 4: tohum doru-0011 (deneme 3 -> 4)

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
@plan: oyunun beyaz taşı otlara doğru yuvarlandı | hızla koşup taşı otlara girmeden durdurdu
@tohum: doru-0011
@degisim: yardımsever -> beyaz
Rüzgar esiyordu ve Doru ile Karatay parkta yumurta oyunu oynuyordu. Oyunda beyaz, yuvarlak bir taş yumurta oluyordu. Ama Karatay sevinçle başını savurdu ve burnu taşa çarptı. Taş, uzun otlara doğru yuvarlandı. "Yumurta otların arasında kaybolacak!" dedi Karatay telaşla. "Korkma, ben yakalarım," dedi Doru. Çayır açık ve düzdü. Doru hızla koştu ve taşı otlara girmeden durdurdu. Sonra taşı burnuyla itip Karatay'a getirdi. "Teşekkürler, Doru, yumurta kaybolmadı!" dedi Karatay. Doru çok sevindi, çünkü oyunun yumurtasını yakalamıştı.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar esiyordu ve Doru ile Karatay"
   - Cümle 1: «Rüzgar esiyordu ve Doru ile Karatay parkta yumurta oyunu oynuyordu.»
   - Açıklama: Rüzgar işe yarayacakmış gibi kuruluyor ama olayda hiçbir rol oynamıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir taş yumurta oluyordu"
   - Cümle 2: «Oyunda beyaz, yuvarlak bir taş yumurta oluyordu.»
   - Açıklama: Taş yumurta olmaz; 'yumurta oluyordu' fiili yanlış anlamda kullanılmış.
3. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "burnu taşa çarptı"
   - Cümle 3: «Ama Karatay sevinçle başını savurdu ve burnu taşa çarptı.»
   - Açıklama: Karatay'ın burnunun taşa çarpması yaralanma ya da acı çağrıştırır.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Karatay sevinçle başını"
   - Cümle 3: «Ama Karatay sevinçle başını savurdu ve burnu taşa çarptı.»
   - Açıklama: Önceki cümleyle karşıtlık olmadığı halde 'Ama' bağlacı yanlış anlamda kullanılmış.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Taş, uzun otlara doğru yuvarlandı"
   - Cümle 4: «Taş, uzun otlara doğru yuvarlandı.»
   - Açıklama: Plandaki sorun olan taşın otlara yuvarlanması ilk üç cümlede değil dördüncü cümlede söyleniyor.
   - Açıklama: Taşın otlara yuvarlanması sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0011` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: ef1c8904f8ac45cb2618818eca388cf2f7939e59`, sonra gövde.
