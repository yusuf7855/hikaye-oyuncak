# Editör görevi (onarım): Chase, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0158 (deneme 2 -> 3)

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
@plan: koşarken bir eldiven parkta kayboldu | öbür eldiveni kokladı ve otların arasında buldu
@tohum: chase-0158
@degisim: sabahlık -> eldiven
Bir sabah Ryder, Chase'i parkın kapısında karşıladı. Ryder üzgündü, çünkü kırmızı bir eldiveni kaybolmuştu. Parkta koşarken cebinden düşmüştü ama nereye düştüğünü görmemişti. "Chase, onu bulabilir misin?" diye sordu Ryder. Ryder öbür eldiveni Chase'e uzattı. Chase onu dikkatle kokladı. Sonra burnunu yere indirdi ve çevik adımlarla parkta dolaştı. Kaydırağın arkasındaki uzun otlarda aynı kokuyu buldu. Kırmızı eldiven otların arasındaydı. Chase eldiveni ağzıyla aldı ve Ryder'ın önüne bıraktı. "İşte eldivenin, Ryder," dedi Chase. Ryder ile Chase çok sevindi, çünkü kayıp eldiven artık Ryder'ın elindeydi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "koşarken bir eldiven parkta kayboldu"
   - Cümle 0 (plan satırı): «koşarken bir eldiven parkta kayboldu | öbür eldiveni kokladı ve otların arasında buldu»
   - Açıklama: 'Koşarken' zarf-fiilinin öznesi eldiven gibi duruyor; koşan kişi cümlede yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0158` birebir aynı, `@degisim: sabahlık -> eldiven` (tutuyorsan), ardından `@onarim: b790cf87a9f485a4e4d328c39f737bc110fb3147`, sonra gövde.

### Hikâye 2: tohum chase-0160 (deneme 2 -> 3)

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
@plan: dalgalar kumsala eski bir file getirdi | kurallara uydu ve fileyi çöpe attı
@tohum: chase-0160
@degisim: huzurlu -> serin
Kumsalda güneş yeni doğuyordu ve hava serindi. Chase su kenarında yürürken kumda büyük ve eski bir file gördü. Dalgalar fileyi denizden getirmiş ve kuma bırakmıştı. Chase kurallara uyan bir polis köpeğiydi. Kurala göre kumsaldaki çöpler çöp kutusuna atılırdı. Bu yüzden Chase fileyi orada bırakmadı. Fileyi ağzıyla tuttu ve yavaşça kuru kuma çekti. Sonra onu yakındaki çöp kutusuna götürdü ve attı. Kumsalda başka çöp kalmadı. Chase çok sevindi, çünkü kumsal yine temizdi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Dalgalar fileyi denizden getirmiş"
   - Cümle 3: «Dalgalar fileyi denizden getirmiş ve kuma bırakmıştı.»
   - Açıklama: Kumda bir file bulunması gerçek bir güçlük yaratmıyor; hiçbir engel olmadan çöpe atılıyor ve çocuğun önemseyeceği bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0160` birebir aynı, `@degisim: huzurlu -> serin` (tutuyorsan), ardından `@onarim: ef45c5ce5daa9d91497297d7f7ae6aa85df773a3`, sonra gövde.

### Hikâye 3: tohum chase-0162 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: güneş yüzünden oyuncak arabanın gittiği yer görünmedi | şapkasını gözlerine indirdi ve arabayı buldu
@tohum: chase-0162
@degisim: tereyağı -> zil
Rüzgar hafif esiyordu. Chase parkta oyuncak arabasını gezdiriyordu ve onu kaydıraktan bıraktı. Ama güneş çok parladı ve Chase arabanın gittiği yeri göremedi. Birden otların arasından garip bir ses geldi. Chase sesin nereden geldiğini çok merak etti. Hemen mavi şapkasını gözlerinin üstüne indirdi. Artık her yeri iyi gördü. Chase otların arasında küçük arabasını buldu. Arabanın üstündeki zil rüzgarda sallanıyor ve çınlıyordu. Ses bu zilden geliyordu. Chase arabasını ağzıyla aldı ve sevinçle kuyruğunu salladı. Chase bundan sonra güneş parlakken şapkasını hep aşağı çekti.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden otların arasından garip bir ses geldi"
   - Cümle 4: «Birden otların arasından garip bir ses geldi.»
   - Açıklama: Birden gelen garip ses küçük çocuk için ürkütücü bir öğe olabilir.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Birden otların arasından garip bir ses geldi"
   - Cümle 4: «Birden otların arasından garip bir ses geldi.»
   - Açıklama: Arabanın görünmemesine ikinci bir sorun olarak garip ses gizemi ekleniyor.
   - Açıklama: Kayıp araba sorununun yanına ayrı bir gizemli ses sorunu ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arabanın üstündeki zil rüzgarda sallanıyor"
   - Cümle 9: «Arabanın üstündeki zil rüzgarda sallanıyor ve çınlıyordu.»
   - Açıklama: Zil önceden kurulmadan sebepsiz beliriyor ve Chase'in şapkayı indirmesi arabayı değil sesi merak etmesinden çıkıyor.
   - Açıklama: Arabada daha önce hiç anılmayan bir zil yalnız sesi açıklamak için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0162` birebir aynı, `@degisim: tereyağı -> zil` (tutuyorsan), ardından `@onarim: f682d3e36128fd8abb08b3dca1dd54ab3d817f30`, sonra gövde.

### Hikâye 4: tohum chase-0163 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0163
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'şekerleme', fiil 'taşımak', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kutudan bir şekerleme düştü ve kumun altına girdi | burnuyla kokusunu alıp şekerlemeyi kumdan çıkardı
@tohum: chase-0163
Bir sabah Chase kumsalda gemi oyunu oynuyordu. Kumdan bir gemi yapmıştı ve ona dolu bir kutu şekerleme taşıyordu. Ama yolda bir şekerleme kutudan düştü ve kumun altına girdi. Chase kuma baktı ama şekerlemeyi göremedi. Sonra burnunu kuma yaklaştırdı ve kokladı. Bir yerden tatlı bir koku geliyordu. Chase o yeri patisiyle yavaşça kazdı. Kırmızı şekerleme kumun altından çıktı. Şekerleme paketinin içindeydi ve yine temizdi. Chase onu kutuya geri koydu. Sonra kutuyu kumdan gemisine götürdü. Chase çok sevindi, çünkü gemisinin bütün yükü tamamdı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bir şekerleme kutudan düştü ve kumun altına girdi"
   - Cümle 3: «Ama yolda bir şekerleme kutudan düştü ve kumun altına girdi.»
   - Açıklama: Düşen bir şekerlemenin kendiliğinden kumun altına girmesi akla yatkın bir sebep değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve yine temizdi"
   - Cümle 9: «Şekerleme paketinin içindeydi ve yine temizdi.»
   - Açıklama: 'Yine' yanlış anlamda kullanılmış; 'hâlâ temizdi' kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0163` birebir aynı, ardından `@onarim: e737db239c084e56610488d00fe1961c19d0da76`, sonra gövde.

### Hikâye 5: tohum chase-0165 (deneme 2 -> 3)

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
@degisim: şeffaf -> boş
Kumsalda Chase ile Ryder oyuncak bir bot yapıyordu. Botu boş bir limonata şişesinden yapacaklardı. Ama şişenin kapağı Ryder'ın elinden kaydı ve kumda kayboldu. "Kapak olmazsa şişeye su girer," dedi Ryder. Chase şişeyi kokladı ve limon kokusunu aldı. Sonra burnunu kuma yaklaştırdı ve aynı kokuyu aradı. Kokuyu bir kayanın yanında buldu. Chase kapağı dişleriyle tuttu ve Ryder'a götürdü. Ryder kapağı şişeye koydu ve sıkıca çevirdi. Sonra botu su kenarına koydu ve bot güzelce yüzdü. "Aferin, Chase, bot hazır!" dedi Ryder. Chase çok sevindi, çünkü botu Ryder ile birlikte bitirmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kokuyu bir kayanın yanında buldu"
   - Cümle 7: «Kokuyu bir kayanın yanında buldu.»
   - Açıklama: Bulunan şey koku değil kapak olmalı; nesne yanlış.
   - Açıklama: Bulunan şey koku değil kapak olmalı; fiil nesnesiyle uyuşmuyor ve kapağın bulunduğu söylenmiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ryder kapağı şişeye koydu"
   - Cümle 9: «Ryder kapağı şişeye koydu ve sıkıca çevirdi.»
   - Açıklama: Kapak şişeye 'konmaz', 'takılır'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0165` birebir aynı, `@degisim: şeffaf -> boş` (tutuyorsan), ardından `@onarim: 000cdc04248afb1cdc0f79cfc82f223f7168f381`, sonra gövde.

### Hikâye 6: tohum chase-0166 (deneme 2 -> 3)

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
Kumsalda Chase hazine oyunu oynuyordu. Hazinesi olan kemiği kuma gömmüş ve üstüne altın renkli bir çubuk dikmişti. Ama bir dalga, hazinenin yerini gösteren çubuğu götürmüştü. Chase kumda bir o yana bir bu yana koşturdu. Ama hazinenin yerini bulamadı. Sonra durdu ve burnunu kuma yaklaştırdı. Kumu dikkatle kokladı. Birden kemiğin kokusunu aldı. Hemen o yeri kazdı ve kemiğini çıkardı. Chase kemiği ağzına aldı ve gururlu bir sesle havladı. Chase bundan sonra hazinesini suyun uzağındaki kuru kuma gömdü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gururlu bir sesle havladı"
   - Cümle 10: «Chase kemiği ağzına aldı ve gururlu bir sesle havladı.»
   - Açıklama: 'Gururlu bir ses' soyut bir nitelemedir, küçük çocuğa uygun değil.
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0166` birebir aynı, ardından `@onarim: 0a1c8cf4c0713c67a35e1e97fd5c30e748db7776`, sonra gövde.

### Hikâye 7: tohum chase-0168 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Kumsalda Chase ile Marshall sırayla bir kozalak saklıyordu. Sıra Marshall'daydı ve ormandan getirdiği kozalağı kuma gömdü. Ama bir dalga geldi ve kumdaki izleri sildi. "Chase, dalga bütün izleri sildi!" dedi Marshall. "Bunu bulmak kolay, Marshall," dedi Chase. Chase burnunu kuma yaklaştırdı ve kokladı. Çam kokusunu hemen aldı. Kokuyu izledi ve bir kayanın yanında durdu. Orayı kazdı ve kozalağı çıkardı. Marshall sevinçle zıpladı ve kuma yuvarlandı. Sonra sıra Chase'e geçti. Chase de kozalağı kuma sakladı. "Seninle sırayla oynamak çok güzel, Chase!" dedi Marshall.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çam kokusunu izledi ve kozalağı buldu"
   - Cümle 0 (plan satırı): «dalga kumdaki izleri sildi | çam kokusunu izledi ve kozalağı buldu»
   - Açıklama: Planda Chase kokuyu izleyip buluyor, gövdede ise kokuyu izleyip kozalağı çıkaran Marshall.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama bir dalga geldi ve kumdaki izleri sildi"
   - Cümle 3: «Ama bir dalga geldi ve kumdaki izleri sildi.»
   - Açıklama: Kozalağı saklayan Marshall için izlerin silinmesi bir sorun değil, saklambaçta işine bile yarar.
   - Açıklama: Saklama oyununda izlerin silinmesi zaten oyunun gereği; saklayan Marshall'ın bunu sorun sayması akla yatkın değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Chase, dalga bütün izleri sildi!"
   - Cümle 4: «"Chase, dalga bütün izleri sildi!" dedi Marshall.»
   - Açıklama: Kozalağı kendisi gömen Marshall yerini bilmesi gerekirken onu kaybetmiş gibi davranıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0168` birebir aynı, `@degisim: katmak -> saklamak` (tutuyorsan), ardından `@onarim: a9e3d65c5c842895432b9e801bc60415d649c946`, sonra gövde.

### Hikâye 8: tohum chase-0170 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: arkadaşı yiyeceğini kulede unuttu ve acıktı | sandviçini ikiye böldü ve onunla paylaştı
@tohum: chase-0170
@degisim: klasör -> sandviç
Bir sabah Chase ile Skye karlı dağda kardan bir köpek yaptı. Sonra ikisi de acıktı ama Skye sandviçini kulede unutmuştu. "Benim yiyecek hiçbir şeyim yok, Chase," dedi Skye. Chase'in soslu sandviçi bir taşın üstünde duruyordu. Hafif kar yağıyordu ama sandviç hiç ıslanmamıştı. Chase onu mavi şapkasıyla örtmüştü. Chase şapkasını kaldırdı ve sandviçi ikiye böldü. "Sandviçimi seninle paylaşalım, Skye," dedi Chase. Sonra yarısını Skye'a verdi. Skye sevinçle kuyruğunu salladı. "Teşekkürler, Chase!" dedi Skye. Sonra ikisi kardan köpeğin yanına oturdu ve sandviçlerini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase onu mavi şapkasıyla örtmüştü"
   - Cümle 6: «Chase onu mavi şapkasıyla örtmüştü.»
   - Açıklama: Kar ve şapkayla örtülen sandviç ayrıntısı soruna ya da çözüme hiçbir katkı yapmayan işlevsiz bir ayrıntı.
   - Açıklama: Şapka ve sandviçin ıslanmaması ayrıntısı olayda hiçbir işe yaramıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Sandviçimi seninle paylaşalım"
   - Cümle 8: «"Sandviçimi seninle paylaşalım, Skye," dedi Chase.»
   - Açıklama: 'Seninle' ile birinci çoğul 'paylaşalım' uyumsuz; 'seninle paylaşayım' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Sandviçimi seninle paylaşalım, Skye"
   - Cümle 8: «"Sandviçimi seninle paylaşalım, Skye," dedi Chase.»
   - Açıklama: 'Seninle' ile 'paylaşalım' kişi uyumu bozuk; 'paylaşayım' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0170` birebir aynı, `@degisim: klasör -> sandviç` (tutuyorsan), ardından `@onarim: 61e003a1dc102374bf172fcc957d7cb139fb1dac`, sonra gövde.

### Hikâye 9: tohum chase-0171 (deneme 2 -> 3)

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
Bir sabah Chase karlı dağda yürürken tüylerindeki karı patisiyle tarıyordu. Önüne bakmadığı için Marshall'ın kar kalesini görmedi ve ona çarptı. Kalenin yuvarlak tepesi yıkıldı ve karda dağıldı. Marshall üzüldü ve kulaklarını indirdi. Chase hemen Marshall'dan özür diledi. Sonra mavi şapkasını çıkardı ve içini karla doldurdu. Karı patileriyle sıkıca bastırdı. Şapkayı ters çevirdi ve yavaşça kaldırdı. Karda yuvarlak bir tepe duruyordu. Chase bu tepeyi kalenin üstüne dikkatle koydu. Kale eskisi gibi güzel oldu. Marshall çok memnun oldu ve kuyruğunu salladı. Sonra ikisi kalenin yanında mutlu mutlu kartopu oynadı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tüylerindeki karı patisiyle tarıyordu"
   - Cümle 1: «Bir sabah Chase karlı dağda yürürken tüylerindeki karı patisiyle tarıyordu.»
   - Açıklama: Kar taranmaz; 'taramak' fiili nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0171` birebir aynı, `@degisim: gazete -> kar` (tutuyorsan), ardından `@onarim: 860e94d07dcef31bc3b52a1a9a1fb401dac0a306`, sonra gövde.

### Hikâye 10: tohum chase-0172 (deneme 2 -> 3)

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
Bir sabah Chase kulede ilk kez kağıttan uçak yapmayı denedi. Defterden beyaz bir sayfa kopardı ve katladı. Ama uçak hemen yere düştü, çünkü kanatları düz değildi. Defterin arkasında bir uçak resmi vardı. Kurallara göre önce resme bakmak gerekiyordu. Chase bu kuralı hatırladı ve resme dikkatle baktı. Kanatları resimdeki gibi düz ve eşit katladı. Sonra uçağı havaya attı. Uçak süzüldü ve kulenin öbür ucuna kadar uçtu. Chase sevinçle havladı ve uçağın arkasından koştu. Chase bundan sonra kağıttan bir şey katlarken hep önce resme baktı.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Chase kulede ilk kez kağıttan uçak"
   - Cümle 1: «Bir sabah Chase kulede ilk kez kağıttan uçak yapmayı denedi.»
   - Açıklama: Başlıktaki yer ev ama hikaye kulede başlıyor ve geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Chase kulede ilk kez"
   - Cümle 1: «Bir sabah Chase kulede ilk kez kağıttan uçak yapmayı denedi.»
   - Açıklama: Başlıktaki yer ev ama hikaye kulede geçiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara göre önce resme bakmak gerekiyordu"
   - Cümle 5: «Kurallara göre önce resme bakmak gerekiyordu.»
   - Açıklama: 'Kurallara göre' soyut bir anlatım; hangi kural olduğu somut değil ve 3 yaşındaki çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara göre önce resme"
   - Cümle 5: «Kurallara göre önce resme bakmak gerekiyordu.»
   - Açıklama: 'Kurallara göre' soyut bir anlatım ve 3 yaşındaki çocuğa uygun değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kurallara göre önce resme bakmak gerekiyordu"
   - Cümle 5: «Kurallara göre önce resme bakmak gerekiyordu.»
   - Açıklama: Kartın özellikler alanındaki 'polis köpeği olarak kurallara uyar' özelliği, kağıt katlarken resme bakma talimatına indirgenerek zorlama ve kartla ilgisiz biçimde kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0172` birebir aynı, `@degisim: elmalı -> beyaz` (tutuyorsan), ardından `@onarim: 932875fd3eeac507cd1dde79e152781642fb590f`, sonra gövde.

### Hikâye 11: tohum chase-0173 (deneme 2 -> 3)

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
@plan: çitin kapısı kilitliydi ve açılmadı | kurallara uydu ve esnek hortumu tahtaların arasından itti
@tohum: chase-0173
@degisim: karabiber -> hortum
Chase parkta çiçek sulama oyunu oynuyordu. Musluğa takılı uzun bir hortumu vardı. Ama çiçeklerin çevresindeki çitin kapısı kilitliydi ve açılmadı. Parkta çitin üstüne çıkmak yasaktı. Chase kurallara uydu ve çite çıkmadı. Hortum esnekti ve kolayca bükülüyordu. Chase hortumu büktü ve ucunu iki tahtanın arasından içeri itti. Musluğu açtı ve su çiçeklere aktı. Kuru çiçeklerin toprağı ıslandı. Chase kuyruğunu salladı ve sevinçle havladı. Chase bundan sonra çitin üstüne hiç çıkmadı ve çiçekleri hortumla suladı.
```

**Hakem bulguları (5):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Musluğa takılı uzun bir hortumu vardı"
   - Cümle 2: «Musluğa takılı uzun bir hortumu vardı.»
   - Açıklama: Kartın özellikler ve yanlar alanında Chase'e ait bir hortum yok; hortum itfaiyeci Marshall'ın görevine ait bir eşya olarak Chase'e verilmiş.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 5: «Chase kurallara uydu ve çite çıkmadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hortum esnekti ve kolayca"
   - Cümle 6: «Hortum esnekti ve kolayca bükülüyordu.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki bir çocuk bilmez.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase bundan sonra çitin üstüne hiç çıkmadı"
   - Cümle 11: «Chase bundan sonra çitin üstüne hiç çıkmadı ve çiçekleri hortumla suladı.»
   - Açıklama: Çite çıkmama bilgisi 4. ve 5. cümleden sonra gereksiz yere tekrarlanıyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Chase bundan sonra çitin üstüne hiç çıkmadı"
   - Cümle 11: «Chase bundan sonra çitin üstüne hiç çıkmadı ve çiçekleri hortumla suladı.»
   - Açıklama: Chase zaten çite çıkmamıştı; son ders olaydan çıkmıyor ve sıcak bir kapanış vermiyor.
   - Açıklama: Chase zaten hiç çite çıkmamıştı; son ders cümlesi yaşanan olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0173` birebir aynı, `@degisim: karabiber -> hortum` (tutuyorsan), ardından `@onarim: 978bd0066c0da9a981fd8ac589589e0111c9528b`, sonra gövde.

### Hikâye 12: tohum chase-0175 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0175
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'rüzgar', fiil 'uçmak', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: rüzgar kağıt uçağı çalıların arasına götürdü | burnuyla kendi kokusunu izleyip uçağı buldu
@tohum: chase-0175
Rüzgar ağaçların arasında hafif hafif esiyordu. Chase kamp yerinde ilk kez bir kağıt uçak uçurmayı denedi. Ama rüzgar uçağı aldı ve sık çalıların arasına götürdü. Chase çalılara baktı ama uçağı göremedi. Uçağı ağzıyla tuttuğu için üstünde onun kokusu vardı. Chase burnunu yere yaklaştırdı ve kokladı. Kokuyu izledi ve uçağı bir çalının dibinde buldu. Uçağı ağaçların olmadığı açık bir yere götürdü. Sonra onu bir kez daha attı. Bu kez uçak uzun uzun uçtu ve yavaşça yere indi. Bu mükemmel bir atıştı. Chase çok sevindi, çünkü ilk uçağını hem bulmuş hem de uçurmuştu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "üstünde onun kokusu vardı"
   - Cümle 5: «Uçağı ağzıyla tuttuğu için üstünde onun kokusu vardı.»
   - Açıklama: 'Onun' zamirinin Chase'i mi uçağı mı gösterdiği belirsiz.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase burnunu yere yaklaştırdı"
   - Cümle 6: «Chase burnunu yere yaklaştırdı ve kokladı.»
   - Açıklama: Uçak havada uçup gittiği için yerde koku izi olamaz; çözüm sebepsizce geliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu mükemmel bir atıştı"
   - Cümle 11: «Bu mükemmel bir atıştı.»
   - Açıklama: 'Mükemmel bir atış' soyut bir değerlendirme; küçük çocuğa uygun değil.
   - Açıklama: 'Mükemmel' ve 'atış' 3 yaşındaki çocuğun bilmeyebileceği soyut kelimeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0175` birebir aynı, ardından `@onarim: 595d0f03b51f0c50573defa1cc10229cec69c73e`, sonra gövde.
