# Editör görevi (onarım): Chase, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar29.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0094 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Skye
@tohum: chase-0094
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'paspas', fiil 'parıldamak', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Skye
@plan: rüzgar esti ve kurabiye torbası kayboldu | kokuyla torbayı bulup arkadaşından yardım istedi
@tohum: chase-0094
@degisim: paspas -> kurabiye
Kumsalda deniz güneşin altında parıldıyordu. Chase ile Skye oraya bir torba tatlı kurabiye getirmişti. Birden güçlü bir rüzgar esti ve kağıt torba uçtu ve kayboldu. Chase burnunu kuma yaklaştırdı ve dikkatle kokladı. Kurabiyelerin kokusu iskelenin başından geliyordu. Torba orada, en alttaki tahtanın altına sıkışmıştı. Ama Chase'in patisi o dar yere sığmadı. Chase koşup Skye'ın yanına gitti ve ondan yardım istedi. Skye'ın küçük patisi oraya kolayca girdi. Skye torbayı yavaşça dışarı çekti. İki arkadaş kuma oturdu ve kurabiyeleri paylaştı. Chase çok sevindi, çünkü yardım isteyince torbayı geri almışlardı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "esti ve kağıt torba uçtu ve kayboldu"
   - Cümle 3: «Birden güçlü bir rüzgar esti ve kağıt torba uçtu ve kayboldu.»
   - Açıklama: Aynı cümlede 've' gereksiz yere iki kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0094` birebir aynı, `@degisim: paspas -> kurabiye` (tutuyorsan), ardından `@onarim: 45116f42b733d83ed1c985220be5c7c07e835d9b`, sonra gövde.

### Hikâye 2: tohum chase-0102 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0102
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yağmur ya da kar günü
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'peynir', fiil 'gıdıklamak', sıfat 'açık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: yağmur yüzünden ağaçların arasında çadır görünmedi | peynir kokusunu izleyip çadırı buldu
@tohum: chase-0102
Yağmur birden hızlı hızlı yağmaya başladı. Chase ile Skye kamp yerinin yanında kozalak topluyordu. Ama yağmur yüzünden ağaçların arasında çadırlarını göremediler. "Chase, çadırımız hangi tarafta?" diye sordu Skye. Damlalar Skye'ın burnunu gıdıkladı ve Skye güldü. Chase hemen burnunu kaldırdı ve havayı kokladı. Çadırda peynirli ekmekleri vardı ve kapısı açık kalmıştı. Chase peynirin kokusunu tanıdı. Kokunun geldiği yöne yürüdü ve Skye de onu izledi. Az sonra çadırlarını buldular ve içeri girdiler. İçerisi kuru ve sıcaktı. "Çadırı bulduk, çok teşekkürler, Chase!" dedi Skye. Chase bundan sonra yolu bulamayınca önce burnunu kullandı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yağmur yüzünden ağaçların arasında çadırlarını göremediler"
   - Cümle 3: «Ama yağmur yüzünden ağaçların arasında çadırlarını göremediler.»
   - Açıklama: Kamp yerinin hemen yanında olan çocukların yağmur yüzünden çadırı görememesi zayıf ve akla pek yatkın olmayan bir sebep.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Damlalar Skye'ın burnunu gıdıkladı ve Skye güldü"
   - Cümle 5: «Damlalar Skye'ın burnunu gıdıkladı ve Skye güldü.»
   - Açıklama: Damlaların Skye'ı gıdıklaması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Damlalar Skye'ın burnunu gıdıkladı"
   - Cümle 5: «Damlalar Skye'ın burnunu gıdıkladı ve Skye güldü.»
   - Açıklama: Gıdıklanma ayrıntısı olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çadırda peynirli ekmekleri vardı"
   - Cümle 7: «Çadırda peynirli ekmekleri vardı ve kapısı açık kalmıştı.»
   - Açıklama: Peynirli ekmek ve açık kapı önceden kurulmadan tam çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0102` birebir aynı, ardından `@onarim: 71a235f9604db790526321dfa3b7df87b2dca11a`, sonra gövde.

### Hikâye 3: tohum chase-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0104
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'tahta', fiil 'karışmak', sıfat 'berrak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: kule yaptığı tahta kutunun bir tahtası çıktı | şapkasını karla doldurup yeni kuleler yaptı
@tohum: chase-0104
@degisim: karışmak -> doldurmak
Chase dağda küçük bir tahta kutuyla kardan kuleler yapıyordu. Gökyüzü berraktı ve güneş parlıyordu. Ama birden kutunun bir tahtası çıktı ve kutu bozuldu. Chase artık kule yapamadı ve bir an durdu. Sonra mavi şapkasını başından çıkardı. Şapkayı karla doldurdu ve bastırdı. Onu ters çevirip yavaşça kaldırdı. Karda yuvarlak bir kule oldu. Bu kule çok güzeldi. Chase şapkayla dört kule daha yaptı. Kutudan çıkan tahtayı da kulelerin arasına kapı yaptı. Sonunda karda küçük bir kale oldu. Chase kalenin yanında oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Gökyüzü berraktı ve güneş"
   - Cümle 2: «Gökyüzü berraktı ve güneş parlıyordu.»
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
   - Açıklama: 'Berrak' kelimesi 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "birden kutunun bir tahtası çıktı"
   - Cümle 3: «Ama birden kutunun bir tahtası çıktı ve kutu bozuldu.»
   - Açıklama: Tahtanın neden çıktığı söylenmiyor, sorunun sebebi yok.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "arasına kapı yaptı"
   - Cümle 11: «Kutudan çıkan tahtayı da kulelerin arasına kapı yaptı.»
   - Açıklama: 'Tahtayı kapı yaptı' kuruluşu bozuk; 'kapı olarak koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0104` birebir aynı, `@degisim: karışmak -> doldurmak` (tutuyorsan), ardından `@onarim: 6cf19c0a3a619adab023287b6f3b8b30216ae8ea`, sonra gövde.

### Hikâye 4: tohum chase-0105 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0105
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'hazine', fiil 'oturmak', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: rüzgar hazine haritasını uçurdu | yalnız kum havuzunu kazıp hazineyi buldu
@tohum: chase-0105
Rüzgar serin serin esiyordu. Chase ile Skye parkta hazine avı oynuyordu. Birden rüzgar, Chase'in hazine haritasını uçurdu. Harita, uzun ağaçların arasında kayboldu. Hazineyi Skye saklamıştı ama oyunda yerini söylemek yasaktı. Oyunun bir kuralı da vardı: hazine yalnız kumda olurdu. Chase kurala uydu ve çimenlerde, çiçeklerde aramadı. Yalnız kum havuzunu dikkatle kazdı. Sonunda bir köşede küçük bir kutu buldu. İkisi hemen havuzun yanındaki banka oturdu. Kutuyu açtılar ve içinde renkli taşlar gördüler. Sonra hazineyi Chase sakladı ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Birden rüzgar, Chase'in hazine"
   - Cümle 3: «Birden rüzgar, Chase'in hazine haritasını uçurdu.»
   - Açıklama: Özneden sonra gereksiz virgül kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oyunun bir kuralı da vardı"
   - Cümle 6: «Oyunun bir kuralı da vardı: hazine yalnız kumda olurdu.»
   - Açıklama: 'Kural' ve 'yasak' 3 yaşındaki çocuğa soyut kavramlar.
   - Açıklama: 'Kural', 'kurala uydu' ve 'yasaktı' 3 yaşındaki çocuk için soyut kavramlar.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hazine yalnız kumda olurdu"
   - Cümle 6: «Oyunun bir kuralı da vardı: hazine yalnız kumda olurdu.»
   - Açıklama: Harita kaybolduktan hemen sonra sebepsizce ortaya çıkan kural çözümü hazır getiriyor ve haritayı anlamsız kılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyunun bir kuralı da vardı"
   - Cümle 6: «Oyunun bir kuralı da vardı: hazine yalnız kumda olurdu.»
   - Açıklama: Çözümü getiren kural sorundan sonra sebepsizce ortaya çıkıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yalnız kum havuzunu dikkatle kazdı"
   - Cümle 8: «Yalnız kum havuzunu dikkatle kazdı.»
   - Açıklama: Sorun uçan harita ama çözüm haritaya yönelmiyor, harita hiç bulunmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0105` birebir aynı, ardından `@onarim: f14b169926dd8161d119d9d8372034d36e23a15f`, sonra gövde.

### Hikâye 5: tohum chase-0106 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Rubble
@tohum: chase-0106
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'boncuk', fiil 'savrulmak', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Rubble
@plan: küçük kabukları kaleye taşımak çok zordu | şapkasını ters çevirip kabukları içinde taşıdı
@tohum: chase-0106
Kumsalda rüzgar esiyor, kumlar savruluyordu. Chase ile Rubble masmavi denizin kıyısında boncuk gibi parlak kabuklar gördü. Kumdan kalelerini onlarla süslemek istediler, ama kabuklar çok küçüktü ve hep düşüyordu. "Chase, bunları taşımak çok zor!" dedi Rubble. Chase mavi şapkasını çıkardı ve ters çevirdi. Kabukları tek tek şapkanın içine koydu. Şapka az sonra kabuklarla doldu. Chase şapkayı dikkatle kaleye taşıdı. Rubble kabukları kalenin duvarlarına dizdi. En büyük kabuğu da kulenin tepesine koydu. "Bu kale çok güzel oldu, teşekkürler, Chase!" dedi Rubble.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "esiyor, kumlar savruluyordu"
   - Cümle 1: «Kumsalda rüzgar esiyor, kumlar savruluyordu.»
   - Açıklama: 'Savrulmak' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "boncuk gibi parlak kabuklar"
   - Cümle 2: «Chase ile Rubble masmavi denizin kıyısında boncuk gibi parlak kabuklar gördü.»
   - Açıklama: Benzetme küçük çocuk için gereksiz bir mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0106` birebir aynı, ardından `@onarim: d2625745b499fd9d32693069ddf6e020b0709ad5`, sonra gövde.

### Hikâye 6: tohum chase-0107 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0107
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kemer', fiil 'giydirmek', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kuru kumla yapılan kemer hemen yıkıldı | kokuyla ıslak kumu bulup kemeri yeniden yaptı
@tohum: chase-0107
@degisim: giydirmek -> yapmak
Kumsalda Chase kumdan basit kuleler yapıyordu. Sonra ilk kez kapı gibi bir kemer yapmayı denedi. Ama kum çok kuruydu ve kemer hemen yıkıldı. Chase ıslak kum bulmak istedi. Burnunu kuma yaklaştırdı ve dikkatle kokladı. Bir yerden serin bir koku geldi. Chase orayı patileriyle kazdı. Kuru kumun altından ıslak kum çıktı. Chase bu kumla yeniden bir kemer yaptı. Bu kez kemer yıkılmadı ve sağlam durdu. Chase kemerin yanına kuleler de yaptı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bir yerden serin bir koku geldi"
   - Cümle 6: «Bir yerden serin bir koku geldi.»
   - Açıklama: Koku serin olmaz; sıfat nesnesine uymuyor.
   - Açıklama: Koku serin olmaz; sıfat öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0107` birebir aynı, `@degisim: giydirmek -> yapmak` (tutuyorsan), ardından `@onarim: b4acc70dbf5c88c37af4a709eed7b851dee2d2c4`, sonra gövde.

### Hikâye 7: tohum chase-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0108
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'düdük', fiil 'döndürmek', sıfat 'lezzetli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | ev | -
@plan: kulübelerin yanında bilinmeyen bir düdük sesi duyuldu | kokuyu izleyip düdüklü oyuncak kemiği buldu
@tohum: chase-0108
Kulübelerin önünde serin bir rüzgar esiyordu. Chase o sırada ince bir düdük sesi duydu. Chase sesin nereden geldiğini çok merak etti. Etrafa baktı ama hiçbir şey göremedi. Sonra burnunu yere yaklaştırdı ve kokladı. Kulübenin arkasından lezzetli bir kemik kokusu geliyordu. Chase kokuyu izledi ve otların arasında bir kemik buldu. Bu, içinde düdük olan oyuncak bir kemikti. Chase kemiği patisiyle döndürdü ve küçük bir delik gördü. Rüzgar bu delikten geçince düdük ötüyordu. Chase kemiği kulübesine götürdü ve onunla mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "lezzetli bir kemik kokusu geliyordu"
   - Cümle 6: «Kulübenin arkasından lezzetli bir kemik kokusu geliyordu.»
   - Açıklama: Bulunan şey oyuncak bir kemik olduğu halde lezzetli kemik kokusu yaydığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0108` birebir aynı, ardından `@onarim: e8991681e21de7fcec23f5b42b31daa69c2de93c`, sonra gövde.

### Hikâye 8: tohum chase-0109 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0109
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bulaşık', fiil 'okumak', sıfat 'uzak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: tabeladaki yazıyı okuyamadı ve yolu bulamadı | şapkasını salladı ve arkadaşından yardım istedi
@tohum: chase-0109
@degisim: bulaşık -> kızak
Chase karlı dağda bir tabelanın önüne geldi. Ryder biraz uzakta, kızakları hazırlıyordu. Chase tabeladaki yazıyı okuyamadı ve kızak yolunu bulamadı. Chase, Ryder'a seslendi ama rüzgar yüzünden Ryder onu duymadı. Sonra mavi şapkasını çıkarıp havada salladı. Ryder mavi şapkayı hemen gördü ve yanına koştu. "Ryder, bu tabelada ne yazıyor?" diye sordu Chase. Ryder tabelayı yüksek sesle okudu. "Kızak yolu bu tarafta, Chase," dedi Ryder. Sonra ikisi o yoldan gitti ve kızakla mutlu mutlu kaydı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Chase tabeladaki yazıyı okuyamadı"
   - Cümle 3: «Chase tabeladaki yazıyı okuyamadı ve kızak yolunu bulamadı.»
   - Açıklama: Chase'in tabelayı neden okuyamadığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0109` birebir aynı, `@degisim: bulaşık -> kızak` (tutuyorsan), ardından `@onarim: 6696d03c63104b471c0869cae994d4f1f7176f7c`, sonra gövde.

### Hikâye 9: tohum chase-0110 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0110
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kristal', fiil 'tamamlanmak', sıfat 'düşünceli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: rüzgar esti ve yapbozu dağıttı | kurala uydu ve önce kenar parçalarını buldu
@tohum: chase-0110
@degisim: kristal -> yapboz
Chase kamp yerinde Marshall'ın yanına geldi. Marshall çadırın önünde büyük bir yapboz yapıyordu. Ama rüzgar esti ve yapbozu dağıttı. Marshall düşünceli düşünceli parçalara bakıyordu. "Chase, bu yapbozu bitiremiyorum," dedi Marshall. Yapbozda bir kural vardı ve Chase ona uydu. Önce yalnız kenar parçalarını ayırdı. İkisi bu parçaları tek tek koydu. Sonra öteki parçaları da kolayca buldular. Az sonra yapboz tamamlandı. Resimde kırmızı bir itfaiye arabası vardı. Marshall sevinçle zıpladı. Chase çok mutlu oldu, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve yapbozu dağıttı"
   - Cümle 3: «Ama rüzgar esti ve yapbozu dağıttı.»
   - Açıklama: Rüzgarın yapbozu dağıtıp sonra yeniden toplanması önemsiz, ağırlıksız bir sorun.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama rüzgar esti ve yapbozu dağıttı"
   - Cümle 3: «Ama rüzgar esti ve yapbozu dağıttı.»
   - Açıklama: Rüzgarın parçaları dağıtıp toplanması önemsiz bir sorun ve talimattaki M3 örneğinin aynısı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yapbozda bir kural vardı"
   - Cümle 6: «Yapbozda bir kural vardı ve Chase ona uydu.»
   - Açıklama: 'Kural' ve 'uymak' soyut; hangi kural olduğu somut değil.
   - Açıklama: Kuralın ne olduğu söylenmeden soyut 'kural' kavramı kullanılmış.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yapbozda bir kural vardı"
   - Cümle 6: «Yapbozda bir kural vardı ve Chase ona uydu.»
   - Açıklama: Karttaki 'kurallara uyar' özelliği polis köpeğinin kurallara uymasıdır; burada kural yalnız bir yapboz ipucuna dönüştürülmüş.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yapbozda bir kural vardı ve Chase ona uydu"
   - Cümle 6: «Yapbozda bir kural vardı ve Chase ona uydu.»
   - Açıklama: Karttaki özellik polis köpeği olarak kurallara uymaktır; yapboz yöntemi zorlama biçimde kural diye sunuluyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yapbozda bir kural vardı ve Chase ona uydu"
   - Cümle 6: «Yapbozda bir kural vardı ve Chase ona uydu.»
   - Açıklama: Çözüm rüzgar sebebine değil yapbozu yeniden kurmaya yöneliyor ve kural sebepsiz beliriyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Resimde kırmızı bir itfaiye arabası vardı"
   - Cümle 11: «Resimde kırmızı bir itfaiye arabası vardı.»
   - Açıklama: Resmin ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0110` birebir aynı, `@degisim: kristal -> yapboz` (tutuyorsan), ardından `@onarim: 1a1d118b0269cd5782b191d334a7276815142dba`, sonra gövde.

### Hikâye 10: tohum chase-0111 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0111
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'sucuk', fiil 'birleştirmek', sıfat 'hazır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: tahta çok ağırdı ve bank bitmedi | şapkasını salladı ve arkadaşından yardım istedi
@tohum: chase-0111
Chase kamp yerinde piknik için bir bank yapıyordu. İki kütüğü uzun bir tahtayla birleştirmek istedi. Ama tahta çok ağırdı ve Chase onu kaldıramadı. Chase güçlü arkadaşı Rubble'ı düşündü. Rubble kampın öbür ucunda yüksek sesle şarkı söylüyordu. Chase seslendi ama Rubble onu duymadı. Chase mavi şapkasını çıkardı ve havada salladı. Rubble mavi şapkayı hemen gördü ve koşup geldi. "Rubble, bana yardım eder misin?" diye sordu Chase. İkisi tahtayı birlikte kütüklerin üstüne koydu. Sucuk ve ekmek hazırdı, ikisi yeni bankta oturup yedi. Chase çok sevindi, çünkü Rubble'ın yardımıyla bank bitmişti.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase seslendi ama Rubble onu duymadı"
   - Cümle 6: «Chase seslendi ama Rubble onu duymadı.»
   - Açıklama: Yardım istemek duyulmama engeli yüzünden seslenme, şapka sallama ve sorma adımlarına uzuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sucuk ve ekmek hazırdı"
   - Cümle 11: «Sucuk ve ekmek hazırdı, ikisi yeni bankta oturup yedi.»
   - Açıklama: Sucuk ve ekmek sebepsiz beliriyor, önceden hiç kurulmamış.
   - Açıklama: Sucuk ve ekmek sebepsiz beliriyor ve sorunla hiçbir bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0111` birebir aynı, ardından `@onarim: c9f9860a03b91959947a61fc8529d5056f94b612`, sonra gövde.

### Hikâye 11: tohum chase-0114 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0114
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'örgü', fiil 'gülümsemek', sıfat 'uslu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: top ağaçların arasına yuvarlandı ve kayboldu | tek başına gitmedi ve yardım istedi
@tohum: chase-0114
@degisim: örgü -> top
Chase kamp yerinde Ryder ile top oynuyordu. Ryder topa sert vurdu. Top ağaçların arasına yuvarlandı ve kayboldu. Chase topu hemen bulmak istedi. Ama bir kural vardı: kimse kamp yerinden tek başına ayrılmazdı. Chase uslu uslu yerinde durdu ve Ryder'a döndü. "Ryder, benimle gelip topu arar mısın?" diye sordu Chase. Ryder gülümsedi. "Tabii, birlikte gidelim," dedi Ryder. İkisi yan yana ağaçların arasına yürüdü. Chase bir çalının arkasında kırmızı topu gördü. Topu ağzıyla aldı ve Ryder'a getirdi. Sonra ikisi kamp yerine döndü ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama bir kural vardı"
   - Cümle 5: «Ama bir kural vardı: kimse kamp yerinden tek başına ayrılmazdı.»
   - Açıklama: 'Kural' soyut bir kavram ve 3 yaşındaki çocuk için zor olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0114` birebir aynı, `@degisim: örgü -> top` (tutuyorsan), ardından `@onarim: 84a61ec2987ead7947941972b68839f70f5b4961`, sonra gövde.

### Hikâye 12: tohum chase-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0115
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'damla', fiil 'çizmek', sıfat 'meyveli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: güneş arkadaşının gözlerine geldi ve çizemedi | mavi şapkasını onunla paylaştı
@tohum: chase-0115
@degisim: damla -> gölge
Kumsalda güneş çok parlıyordu. Chase ile Marshall iskelenin yanında kuma resim çiziyordu. Marshall meyveli bir pasta çizmek istiyordu ama güneş gözlerine geliyordu. "Çizgileri göremiyorum," dedi Marshall. Chase mavi şapkasına baktı. Sonra şapkayı başından aldı ve Marshall'ın başına taktı. "Şapkamı seninle paylaşırım, Marshall," dedi Chase. Şapkanın gölgesi Marshall'ın gözlerini korudu. Marshall kuma büyük bir pasta çizdi. Pastanın üstüne çilekler ve portakallar ekledi. Chase de pastanın etrafına küçük kalpler çizdi. "Teşekkürler, Chase, pastamız çok güzel oldu!" dedi Marshall.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güneş arkadaşının gözlerine geldi ve çizemedi"
   - Cümle 0 (plan satırı): «güneş arkadaşının gözlerine geldi ve çizemedi | mavi şapkasını onunla paylaştı»
   - Açıklama: Bağlanan iki yüklemin öznesi farklı; dilbilgisel olarak 'çizemedi'nin öznesi güneş oluyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "gözlerine geldi ve çizemedi"
   - Cümle 0 (plan satırı): «güneş arkadaşının gözlerine geldi ve çizemedi | mavi şapkasını onunla paylaştı»
   - Açıklama: Bağlı cümlede özne güneş kalıyor; çizemeyen arkadaş olduğu dilbilgisel olarak belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0115` birebir aynı, `@degisim: damla -> gölge` (tutuyorsan), ardından `@onarim: 3edf3b5585a01dfb3176367f3dba30c1877c3a57`, sonra gövde.
