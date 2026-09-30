# Editör görevi (onarım): Chase, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Chase | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar35.txt --ad urun_v2`
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

## Kart: Chase (kaynaklı, kapalı dünya)

- Ad: Chase (okunuş: çeys; kesme eki okunuşa uyar)
- Kimlik: Chase, bir kurtarma ekibinin polis köpeği olan bir çoban köpeği yavrusudur.
- Tür: köpek
- Güvenli özellik kullanımı: Chase kaybolanı bulur ve küçük sorunları çözer; kimseyi kovalamaz, yakalamaz ya da cezalandırmaz. Kimse yabancıyla bir yere gitmez. 'Tehlike' yerine 'bir sorun var' denir. Kediler ve tüyler yüzünden hapşırması hikayeye konmaz.
- Özellikler:
  - koku: Burnuyla koku alarak çözüm bulur. (örnek biçimler: koku, kokladı, kokusunu)
  - kural: Ekibin polis köpeğidir; kurallara uyar. (örnek biçimler: kural, kurallara)
  - şapka: Mavi bir şapka takar. (örnek biçimler: şapka, şapkası)
- Yerler:
  - dağ: Kasabanın yakınındaki karlı dağ.
  - deniz: Kasabanın kıyısı; kumsal ve iskele.
  - orman: Kasabanın yakınında, ağaçların arasındaki kamp yeri.
  - park: Kasabadaki çocuk oyun parkı.
  - ev: Ekibin yüksek kulesi ve köpeklerin kulübeleri.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Ryder: On yaşında bir çocuk; ekibin başıdır. Köpeklere bakar ve işe uygun köpeği o seçer. Tür: oğlan; konuşur. Yüzey biçimleri: Ryder
  - Marshall: Ekibin itfaiyeci köpeği; altı yaşında, benekli bir köpek. Biraz sakardır ama cesur ve yardımseverdir. Tür: köpek; konuşur. Yüzey biçimleri: Marshall
  - Skye: Helikopter kullanan pilot köpek; ekibin en küçüğü, küçük hayvanları çok sever. Tür: köpek; konuşur. Yüzey biçimleri: Skye
  - Rubble: İnşaat köpeği; güçlü, şakacıdır ve yemek yemeyi sever. Tür: köpek; konuşur. Yüzey biçimleri: Rubble
- Dünya kuralları:
  - Chase slogan söylemez; kimse kendi adıyla konuşmaz.
  - Ryder bir çocuktur, köpek değildir.
  - Görevler karışmaz: Chase polis, Marshall itfaiyeci, Skye pilot, Rubble inşaat köpeğidir.
- Yasak adlar: Rocky, Zuma, Everest, Tracker, Goodway, Chickaletta, Turbot, Humdinger, Robo-Dog, Jake, Liberty, Rex
- Yasak: Araçların kovalamacası, sirenle hız ve kötü karakterler hikayeye girmez.
- İzinli dünya kelimeleri: polis, koku, şapka, itfaiye, helikopter, kule, kulübe, iskele

## Onarılacak hikâyeler

### Hikâye 1: tohum chase-0157 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0157
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'ay', fiil 'toplamak', sıfat 'yavaş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: sepet bir ağacın dibinde kaldı ve yeri unutuldu | kokuyu yavaşça izleyip sepeti buldu
@tohum: chase-0157
Ağaçların arasında rüzgar hafif esiyordu. Chase ile Marshall kamp yerinde yürüyordu. Marshall kozalak dolu sepetini bir ağacın dibine bırakmış ve yerini unutmuştu. "Chase, sepetim kayboldu," dedi Marshall. Gökyüzünde ay vardı ama ışığı azdı. Sepette Marshall'ın kokusu vardı. Chase önce Marshall'ı kokladı. Sonra burnunu yere yaklaştırdı ve yavaş yavaş yürüdü. Aynı kokuyu büyük bir çalının arkasında buldu. Sepet oradaydı ve kozalaklar içindeydi. "İşte sepetin, Marshall," dedi Chase. Chase ile Marshall çok sevindi, çünkü toplanan kozalaklar kaybolmamıştı.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Gökyüzünde ay vardı ama ışığı azdı"
   - Cümle 5: «Gökyüzünde ay vardı ama ışığı azdı.»
   - Açıklama: Gece karanlığında ormanda dolaşmak küçük çocuk için korkutucu bir ortam kuruyor.
   - Açıklama: Gece karanlığında ormanda kayıp eşya aramak küçük çocuğa ürkütücü gelebilir.
   - Açıklama: Ormanda az ışıklı gece sahnesi küçük çocuk için ürkütücü olabilir.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Aynı kokuyu büyük bir çalının arkasında buldu"
   - Cümle 9: «Aynı kokuyu büyük bir çalının arkasında buldu.»
   - Açıklama: Sepet bir ağacın dibine bırakılmışken bir çalının arkasında bulunuyor.
   - Açıklama: Sepet bir ağacın dibine bırakılmıştı ama bir çalının arkasında bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0157` birebir aynı, ardından `@onarim: 4edf41fc61b7c183868744f17c6ca43cd946f37c`, sonra gövde.

### Hikâye 2: tohum chase-0158 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Ryder
@tohum: chase-0158
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'sabahlık', fiil 'karşılamak', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Ryder
@plan: salıncakta sallanırken bir eldiven kumda kayboldu | öbür eldiveni kokladı ve kumun içinde buldu
@tohum: chase-0158
@degisim: sabahlık -> eldiven
Bir sabah Ryder, Chase'i parkın kapısında karşıladı. Ryder üzgündü, çünkü kırmızı bir eldiveni kaybolmuştu. Salıncakta sallanırken cebinden düşmüştü. "Chase, onu bulabilir misin?" diye sordu Ryder. Ryder öbür eldiveni Chase'e uzattı. Chase onu dikkatle kokladı. Sonra burnunu yere indirdi ve çevik adımlarla salıncağa koştu. Salıncağın altındaki kumda aynı kokuyu buldu. Chase patileriyle kumu yavaşça eşeledi. Kumun içinden kırmızı eldiven çıktı. "İşte eldivenin, Ryder," dedi Chase. Ryder ile Chase çok sevindi, çünkü kayıp eldiven artık Ryder'ın elindeydi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Salıncakta sallanırken cebinden düşmüştü"
   - Cümle 3: «Salıncakta sallanırken cebinden düşmüştü.»
   - Açıklama: Eldivenin nereye düştüğü biliniyorken bulunamaması ve kendiliğinden kumun içine gömülmesi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0158` birebir aynı, `@degisim: sabahlık -> eldiven` (tutuyorsan), ardından `@onarim: 894e700b4b4702bd7830e5539208df03626e0cf8`, sonra gövde.

### Hikâye 3: tohum chase-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0160
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'file', fiil 'doğmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalgalar balıkların yanına eski bir file getirdi | kurallara uydu ve fileyi çöpe attı
@tohum: chase-0160
Kumsalda güneş yeni doğuyordu ve deniz çok huzurluydu. Chase su kenarında yürürken sığ suda küçük balıklar gördü. Ama dalgalar balıkların yanına eski bir file getirmişti. Küçük balıklar o fileye takılıp kalabilirdi. Chase kurallara uyan bir polis köpeğiydi. Bu yüzden çöpü hiç denizde bırakmadı. Fileyi ağzıyla tuttu ve yavaşça kuru kuma çekti. Sonra onu çöp kutusuna götürdü ve attı. Balıklar sığ suda rahatça yüzmeye devam etti. Chase çok sevindi, çünkü balıkların suyu yine temizdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "deniz çok huzurluydu"
   - Cümle 1: «Kumsalda güneş yeni doğuyordu ve deniz çok huzurluydu.»
   - Açıklama: 'Huzurlu' soyut bir kelime ve denize mecazla yüklenmiş; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Huzurlu' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Küçük balıklar o fileye takılıp kalabilirdi"
   - Cümle 4: «Küçük balıklar o fileye takılıp kalabilirdi.»
   - Açıklama: Balıkların fileye takılıp zarar görme olasılığı çocuğa bir yaralanma kaygısı olarak sunuluyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Küçük balıklar o fileye takılıp kalabilirdi"
   - Cümle 4: «Küçük balıklar o fileye takılıp kalabilirdi.»
   - Açıklama: Notlanan çoğul canlı balıklar arka planda kalmıyor, sorunun parçası olarak olaya katılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çöpü hiç denizde bırakmadı"
   - Cümle 6: «Bu yüzden çöpü hiç denizde bırakmadı.»
   - Açıklama: Tek bir olay için 'hiç' yanlış anlamda kullanılmış ve 'çöpü' fileyi belirsiz gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0160` birebir aynı, ardından `@onarim: 26dd9dbd726ffd015b1392c1d14c183b6b2e8954`, sonra gövde.

### Hikâye 4: tohum chase-0162 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0162
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'tereyağı', fiil 'gezdirmek', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: ağaçtan garip bir ses geldi ama güneşten dallar görünmedi | şapkasını gözlerinin üstüne indirdi ve zili gördü
@tohum: chase-0162
@degisim: tereyağı -> zil
Rüzgar hafifçe esiyordu. Chase parkta oyuncak arabasını gezdiriyordu. Birden büyük ağacın tepesinden garip bir ses geldi. Chase sesin nereden geldiğini çok merak etti. Ağacın altına koştu ve yukarı baktı. Ama güneş çok parlaktı ve Chase dalları göremedi. Hemen mavi şapkasını gözlerinin üstüne indirdi. Artık güneş gözlerine gelmedi ve dallar göründü. Bir dalda küçük bir zil asılıydı. Rüzgar esince zil sallanıyor ve çınlıyordu. Ses bu zilden geliyordu. Chase sevindi ve kuyruğunu salladı. Chase bundan sonra parlak güneşte yukarı bakarken hep böyle yaptı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden büyük ağacın tepesinden garip bir ses geldi"
   - Cümle 3: «Birden büyük ağacın tepesinden garip bir ses geldi.»
   - Açıklama: Sorun yalnız merak edilen önemsiz bir ses; bulununca hiçbir şey değişmiyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama güneş çok parlaktı ve Chase dalları göremedi"
   - Cümle 6: «Ama güneş çok parlaktı ve Chase dalları göremedi.»
   - Açıklama: Çözülen sorun olan güneşin dalları göstermemesi ilk üç cümlede değil 6. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0162` birebir aynı, `@degisim: tereyağı -> zil` (tutuyorsan), ardından `@onarim: 34ad1ea256436378d694707eb282b6a58c04951a`, sonra gövde.

### Hikâye 5: tohum chase-0165 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0165
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: bir şey yapmak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'bot', fiil 'çevirmek', sıfat 'şeffaf'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: şişenin kapağı kumda kayboldu | limon kokusunu izleyip kapağı buldu
@tohum: chase-0165
Kumsalda Chase ile Ryder oyuncak bir bot yapıyordu. Botu şeffaf bir limonata şişesinden yapacaklardı. Ama şişenin kapağı Ryder'ın elinden kaydı ve kumda kayboldu. "Kapak olmazsa şişeye su girer," dedi Ryder. Chase şişeyi kokladı ve limon kokusunu aldı. Sonra burnunu kuma yaklaştırdı ve aynı kokuyu aradı. Kokuyu bir kayanın yanında buldu. Chase kapağı dişleriyle tuttu ve Ryder'a götürdü. Ryder kapağı şişeye koydu ve sıkıca çevirdi. Sonra botu su kenarına koydu ve bot güzelce yüzdü. "Aferin, Chase, bot hazır!" dedi Ryder. Chase çok sevindi, çünkü botu Ryder ile birlikte bitirmişlerdi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Botu şeffaf bir limonata"
   - Cümle 2: «Botu şeffaf bir limonata şişesinden yapacaklardı.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "botu Ryder ile birlikte bitirmişlerdi"
   - Cümle 12: «Chase çok sevindi, çünkü botu Ryder ile birlikte bitirmişlerdi.»
   - Açıklama: Özne Chase tekil iken yüklem çoğul çekimli; 'bitirmişti' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ryder ile birlikte bitirmişlerdi"
   - Cümle 12: «Chase çok sevindi, çünkü botu Ryder ile birlikte bitirmişlerdi.»
   - Açıklama: Özne Chase tekil iken fiil çoğul; 'Ryder ile birlikte bitirmişti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0165` birebir aynı, ardından `@onarim: 92fcdcf66c0a2bc0719281b79a624e2aa8f22dde`, sonra gövde.

### Hikâye 6: tohum chase-0166 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0166
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'altın', fiil 'koşturmak', sıfat 'gururlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalga hazinenin yerini gösteren çubuğu götürdü | kumu kokladı, kemiği buldu ve çıkardı
@tohum: chase-0166
Kumsalda Chase hazine oyunu oynuyordu. Oyunda kuma gömdüğü kemik, onun altın hazinesiydi. Ama bir dalga, hazinenin yerini gösteren çubuğu götürmüştü. Chase kumda bir o yana bir bu yana koşturdu. Ama hazinenin yerini bulamadı. Sonra durdu ve burnunu kuma yaklaştırdı. Kumu dikkatle kokladı. Birden kemiğin kokusunu aldı. Hemen o yeri kazdı ve kemiğini çıkardı. Chase kemiği ağzına aldı ve gururlu bir sesle havladı. Chase bundan sonra hazinesini suyun uzağındaki kuru kuma gömdü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onun altın hazinesiydi"
   - Cümle 2: «Oyunda kuma gömdüğü kemik, onun altın hazinesiydi.»
   - Açıklama: Kemiğin 'altın hazine' olması mecazdır; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Kemiğe 'altın hazine' demek mecazdır ve küçük çocuğu yanıltır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0166` birebir aynı, ardından `@onarim: 28d1deee6e9bb65f14709e7298504ae456ea1a88`, sonra gövde.

### Hikâye 7: tohum chase-0168 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0168
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: sırayla oynamak
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kozalak', fiil 'katmak', sıfat 'kolay'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: dalga kumdaki izleri sildi | çam kokusunu izledi ve kozalağı buldu
@tohum: chase-0168
@degisim: katmak -> saklamak
Kumsalda Chase ile Marshall sırayla bir kozalak saklıyordu. Sıra Marshall'daydı ve ormandan getirdiği kozalağı kuma gömdü. Ama bir dalga geldi ve kumdaki izleri sildi. "Kozalak nerede, hiç göremiyorum!" dedi Marshall. "Bunu bulmak kolay, Marshall," dedi Chase. Chase burnunu kuma yaklaştırdı ve kokladı. Çam kokusunu hemen aldı. Kokuyu izledi ve bir kayanın yanında durdu. Orayı kazdı ve kozalağı çıkardı. Marshall sevinçle zıpladı ve kuma yuvarlandı. Sonra sıra Chase'e geldi ve kozalağı sakladı. "Seninle sırayla oynamak çok güzel, Chase!" dedi Marshall.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kozalak nerede, hiç göremiyorum"
   - Cümle 4: «"Kozalak nerede, hiç göremiyorum!" dedi Marshall.»
   - Açıklama: Kozalağı az önce kendisi gömen Marshall yerini bilmiyormuş gibi davranıyor; saklayan ile arayan rolleri çelişiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sıra Chase'e geldi ve kozalağı sakladı"
   - Cümle 11: «Sonra sıra Chase'e geldi ve kozalağı sakladı.»
   - Açıklama: İkinci yüklemin öznesi 'sıra' gibi kalıyor; kozalağı saklayanın Chase olduğu dilbilgisel olarak kurulmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0168` birebir aynı, `@degisim: katmak -> saklamak` (tutuyorsan), ardından `@onarim: 6149a424c5644626ad38f2b75b5e58bf94e61109`, sonra gövde.

### Hikâye 8: tohum chase-0169 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0169
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'maske', fiil 'sarmak', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | -
@plan: havada nereden geldiği bilinmeyen tatlı bir koku vardı | kokuyu izleyip ağaca sarılmış çiçekleri buldu
@tohum: chase-0169
@degisim: maske -> çiçek
Chase ormandaki kamp yerinde ağaçların arasında yürüyordu. Birden havada tatlı bir koku aldı. Chase bu kokunun nereden geldiğini çok merak etti. Burnunu havaya kaldırdı ve kokuyu izledi. Kıvrımlı bir patikada yavaş yavaş ilerledi. Koku gittikçe güçlendi. Sonunda büyük bir çam ağacının yanına geldi. İnce yeşil bir dal, ağacın gövdesini sarmıştı. Dalın üstünde küçük beyaz çiçekler açmıştı. Tatlı koku bu çiçeklerden geliyordu. Chase kuyruğunu salladı ve çiçekleri sevinçle kokladı. Sonra ağacın gölgesine uzandı ve çiçeklerin yanında mutlu mutlu dinlendi.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden havada tatlı bir koku aldı"
   - Cümle 2: «Birden havada tatlı bir koku aldı.»
   - Açıklama: Tatlı bir koku gerçek bir sorun değil, yalnız bir merak konusu; ortada çözülmesi gereken bir dert ve sebebi yok.
   - Açıklama: Tatlı bir koku almak gerçek bir sorun değil; çocuğun önemseyeceği bir güçlük kurulmuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kıvrımlı bir patikada yavaş yavaş ilerledi"
   - Cümle 5: «Kıvrımlı bir patikada yavaş yavaş ilerledi.»
   - Açıklama: Chase ormanda tek başına bilinmeyen bir kokunun peşinden kamp yerinden uzaklaşıyor; çocuk tek başına ormanda uzaklaşmayı taklit edebilir.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "İnce yeşil bir dal"
   - Cümle 8: «İnce yeşil bir dal, ağacın gövdesini sarmıştı.»
   - Açıklama: Ağacın gövdesini saran şey dal değil sarmaşıktır; kelime yanlış anlamda kullanılmış.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "İnce yeşil bir dal, ağacın gövdesini sarmıştı"
   - Cümle 8: «İnce yeşil bir dal, ağacın gövdesini sarmıştı.»
   - Açıklama: Özne ile nesne arasına gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0169` birebir aynı, `@degisim: maske -> çiçek` (tutuyorsan), ardından `@onarim: cc89817cc5824493a24873179e133f2a4a49bacf`, sonra gövde.

### Hikâye 9: tohum chase-0170 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0170
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'klasör', fiil 'örtmek', sıfat 'soslu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: rüzgar kardan köpeğin dalını uçurdu | mavi şapkasını kardan köpekle paylaştı
@tohum: chase-0170
@degisim: klasör -> sandviç
Bir sabah Chase ile Skye karlı dağda kardan bir köpek yapıyordu. Skye onun başına bir çam dalı koymuştu. Ama rüzgar esti ve dalı alıp götürdü. "Başında hiçbir şey kalmadı, Chase," dedi Skye. Chase biraz düşündü. Sonra mavi şapkasıyla kardan köpeğin başını örttü. "Şapkamı onunla paylaşalım, Skye," dedi Chase. Skye güldü ve iki küçük taşla ona gözler yaptı. "Çok güzel oldu, Chase!" dedi Skye. Sonra ikisi onun yanına oturdu ve soslu sandviçlerini mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Skye onun başına bir"
   - Cümle 2: «Skye onun başına bir çam dalı koymuştu.»
   - Açıklama: 'Onun' zamirinin Chase'i mi kardan köpeği mi gösterdiği belli değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve dalı alıp götürdü"
   - Cümle 3: «Ama rüzgar esti ve dalı alıp götürdü.»
   - Açıklama: Kardan köpeğin başındaki dalın uçması çocuğun önemseyeceği bir sorun olarak kurulmuyor.
   - Açıklama: Kardan köpeğin başındaki dalın uçması çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şapkamı onunla paylaşalım"
   - Cümle 7: «"Şapkamı onunla paylaşalım, Skye," dedi Chase.»
   - Açıklama: Şapka kardan köpeğin başına verildiği için 'paylaşmak' fiili anlama uymuyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "soslu sandviçlerini mutlu mutlu yedi"
   - Cümle 10: «Sonra ikisi onun yanına oturdu ve soslu sandviçlerini mutlu mutlu yedi.»
   - Açıklama: Sandviçler hikayede daha önce hiç kurulmadan sebepsizce beliriyor.
   - Açıklama: Sandviçler sebepsiz beliriyor ve olayla ilgisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0170` birebir aynı, `@degisim: klasör -> sandviç` (tutuyorsan), ardından `@onarim: 956330163193305bdcca6e7a331a6dad3da00de2`, sonra gövde.

### Hikâye 10: tohum chase-0171 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Marshall
@tohum: chase-0171
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'gazete', fiil 'taramak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Marshall
@plan: kar kalesine çarpıp tepesini yıktı | özür diledi ve şapkasıyla yeni bir tepe yaptı
@tohum: chase-0171
@degisim: gazete -> kar
Bir sabah Chase karlı dağda her yeri dikkatle tarıyordu. Uzağa bakarken Marshall'ın kar kalesini görmedi ve ona çarptı. Kalenin yuvarlak tepesi yıkıldı ve karda dağıldı. Marshall üzüldü ve kulaklarını indirdi. Chase hemen Marshall'dan özür diledi. Sonra mavi şapkasını çıkardı ve içini karla doldurdu. Sonra patileriyle sıkıca bastırdı. Şapkayı ters çevirdi ve yavaşça kaldırdı. Karda yuvarlak bir tepe duruyordu. Chase bu tepeyi kalenin üstüne dikkatle koydu. Kale eskisi gibi güzel oldu. Marshall çok memnun oldu ve kuyruğunu salladı. Sonra ikisi kalenin yanında mutlu mutlu kartopu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "her yeri dikkatle tarıyordu"
   - Cümle 1: «Bir sabah Chase karlı dağda her yeri dikkatle tarıyordu.»
   - Açıklama: 'Taramak' burada mecazlı ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Taramak' gözle bakma anlamında mecazlı ve 3 yaşındaki çocuğa yabancı.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra patileriyle sıkıca bastırdı"
   - Cümle 7: «Sonra patileriyle sıkıca bastırdı.»
   - Açıklama: Art arda iki cümle 'Sonra' ile başlıyor; gereksiz tekrar.
   - Açıklama: Art arda iki cümle 'Sonra' ile başlıyor, gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0171` birebir aynı, `@degisim: gazete -> kar` (tutuyorsan), ardından `@onarim: 70920f5de1a6459767fb23dec9700f7adf6f9113`, sonra gövde.

### Hikâye 11: tohum chase-0172 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0172
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'defter', fiil 'koparmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: kanatları düz olmadığı için kağıt uçak düştü | kuralı hatırladı ve resme bakarak katladı
@tohum: chase-0172
@degisim: elmalı -> beyaz
Bir sabah Chase kulede ilk kez kağıttan uçak yapmayı denedi. Defterden beyaz bir sayfa kopardı ve katladı. Ama uçak hemen yere düştü, çünkü kanatları düz değildi. Defterin arkasında bir uçak resmi vardı. Kulede bir kural vardı: yeni bir işte önce resme bak. Chase bu kuralı hatırladı ve resme dikkatle baktı. Kanatları resimdeki gibi düz ve eşit katladı. Sonra kulübelerin önünde uçağı havaya attı. Uçak süzüldü ve uzağa uçtu. Chase sevinçle havladı ve uçağın arkasından koştu. Chase bundan sonra kağıttan bir şey katlarken önce resme baktı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir işte önce resme bak"
   - Cümle 5: «Kulede bir kural vardı: yeni bir işte önce resme bak.»
   - Açıklama: 'Kural' ve 'yeni bir iş' soyut kavramlar, 3 yaşındaki çocuk için somut değil.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "bir kural vardı: yeni bir işte"
   - Cümle 5: «Kulede bir kural vardı: yeni bir işte önce resme bak.»
   - Açıklama: İki noktadan sonra gelen tam cümle büyük harfle başlamalı.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sonra kulübelerin önünde uçağı havaya attı"
   - Cümle 8: «Sonra kulübelerin önünde uçağı havaya attı.»
   - Açıklama: Hikaye kulede başlıyor, kulübelerin önüne geçiyor ve başlıktaki ev sahnesinde kalmıyor.
   - Açıklama: Hikaye kulede başlıyor, sonra kulübelerin önüne geçiyor; tek sahne kuralı çiğneniyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "katlarken önce resme baktı"
   - Cümle 11: «Chase bundan sonra kağıttan bir şey katlarken önce resme baktı.»
   - Açıklama: 'Bundan sonra' ile alışkanlık anlatılıyor ama fiil tek seferlik geçmişte; 'bakardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0172` birebir aynı, `@degisim: elmalı -> beyaz` (tutuyorsan), ardından `@onarim: 4ecee76c751104bce8bb07f7dc75321bc52edef1`, sonra gövde.

### Hikâye 12: tohum chase-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0173
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'karabiber', fiil 'açılmak', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: çitin kapısı kilitliydi ve açılmadı | kuralı bozmadı ve esnek hortumla suladı
@tohum: chase-0173
@degisim: karabiber -> hortum
Chase parkta çiçek bakma oyunu oynuyordu. Oyunda çiçekleri sulamak onun işiydi. Ama çiçeklerin çevresindeki çitin kapısı kilitliydi ve açılmadı. Parkın bir kuralı vardı: çitin üstüne çıkmak yasak. Chase kuralı bozmadı ve çite çıkmadı. Sonra musluğa takılı uzun ve esnek bir hortum gördü. Hortumun ucunu iki tahtanın arasından içeri itti. Musluğu açtı ve su çiçeklere aktı. Kuru çiçeklerin toprağı ıslandı. Chase kuyruğunu salladı ve sevinçle havladı. Chase bundan sonra kapı kilitli olunca başka bir yol aradı.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "parkta çiçek bakma oyunu"
   - Cümle 1: «Chase parkta çiçek bakma oyunu oynuyordu.»
   - Açıklama: Tamlama bozuk; 'çiçeğe bakma oyunu' olmalı.
   - Açıklama: Tamlama bozuk; 'çiçeklere bakma' ya da 'çiçek bakımı' olmalı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "çitin üstüne çıkmak yasak."
   - Cümle 4: «Parkın bir kuralı vardı: çitin üstüne çıkmak yasak.»
   - Açıklama: Anlatım geniş zamana kaydı; 'yasaktı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "uzun ve esnek bir hortum"
   - Cümle 6: «Sonra musluğa takılı uzun ve esnek bir hortum gördü.»
   - Açıklama: 'Esnek' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "musluğa takılı uzun ve esnek bir hortum gördü"
   - Cümle 6: «Sonra musluğa takılı uzun ve esnek bir hortum gördü.»
   - Açıklama: Hortum daha önce kurulmadan tam gerektiği anda beliriyor ve çözümü sebepsizce getiriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra musluğa takılı uzun ve esnek bir hortum gördü"
   - Cümle 6: «Sonra musluğa takılı uzun ve esnek bir hortum gördü.»
   - Açıklama: Hortum daha önce kurulmadan tam gerektiği anda sebepsizce beliriyor ve çözümü getiriyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kapı kilitli olunca başka bir yol aradı"
   - Cümle 11: «Chase bundan sonra kapı kilitli olunca başka bir yol aradı.»
   - Açıklama: Kilitli kapı karşısında başka yoldan içeri ulaşmayı genel ders olarak veriyor; çocuk kilitli yerlere girmeye çalışarak taklit edebilir.
7. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Chase bundan sonra kapı kilitli olunca başka bir yol aradı."
   - Cümle 11: «Chase bundan sonra kapı kilitli olunca başka bir yol aradı.»
   - Açıklama: 'Bundan sonra' ile geçmiş zaman uyumsuz, zaman kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0173` birebir aynı, `@degisim: karabiber -> hortum` (tutuyorsan), ardından `@onarim: d2d52c7f5a3853eb82681c93292705cd2b2a9c7f`, sonra gövde.
