# Editör görevi (onarım): Chase, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar41.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0163 (deneme 3 -> 4)

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
@plan: kutudan bir şekerleme düştü ve dalga üstünü kumla örttü | burnuyla kokusunu alıp şekerlemeyi kumdan çıkardı
@tohum: chase-0163
Bir sabah Chase kumsalda gemi oyunu oynuyordu. Kumdan bir gemi yapmıştı ve ona dolu bir kutu şekerleme taşıyordu. Ama yolda bir şekerleme kutudan kuma düştü. Hemen küçük bir dalga geldi ve onun üstünü kumla örttü. Chase kuma baktı ama şekerlemeyi göremedi. Sonra burnunu kuma yaklaştırdı ve kokladı. Bir yerden tatlı bir koku geliyordu. Chase o yeri patisiyle yavaşça kazdı. Kırmızı şekerleme kumun altından çıktı. Kağıdı olduğu için şekerleme temizdi. Chase onu kutuya geri koydu. Sonra kutuyu gemisine götürdü. Chase çok sevindi, çünkü gemisinin bütün yükü tamamdı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ona dolu bir kutu şekerleme taşıyordu"
   - Cümle 2: «Kumdan bir gemi yapmıştı ve ona dolu bir kutu şekerleme taşıyordu.»
   - Açıklama: 'Ona taşıyordu' yanlış ek; 'onunla taşıyordu' ya da 'ona yüklüyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0163` birebir aynı, ardından `@onarim: 0fe08308171e68ea7b22b534389049c37a62bd13`, sonra gövde.

### Hikâye 2: tohum chase-0168 (deneme 3 -> 4)

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
@plan: dalga saklanan kozalağı alıp götürdü | kumda çam kokusunu aradı ve kozalağı buldu
@tohum: chase-0168
@degisim: katmak -> saklamak
Kumsalda Chase ile Marshall sırayla bir çam kozalağı saklıyordu. Sıra Chase'teydi ve kozalağı su kenarında kuma sakladı. Ama bir dalga geldi ve kozalağı alıp götürdü. "Oyunumuz bitti mi?" diye sordu Marshall. "Hayır, bulmak kolay, Marshall," dedi Chase. Chase burnunu kuma yaklaştırdı ve çam kokusunu aradı. Kozalağı bir kayanın yanında buldu. Sonra onu Marshall'a verdi. "Sıra sende, Marshall," dedi Chase. Marshall sevinçle kozalağı kuma sakladı. "Seninle sırayla oynamak çok güzel, Chase!" dedi Marshall.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama bir dalga geldi ve kozalağı alıp götürdü"
   - Cümle 3: «Ama bir dalga geldi ve kozalağı alıp götürdü.»
   - Açıklama: Dalganın götürdüğü kozalak hiçbir güçlük olmadan kayanın yanında hemen bulunuyor; sorun kaybolup bulundu-bitti biçiminde önemsizleşiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0168` birebir aynı, `@degisim: katmak -> saklamak` (tutuyorsan), ardından `@onarim: fbb2fefc6601143c5b4e8685e6f0431bc90d2161`, sonra gövde.

### Hikâye 3: tohum chase-0172 (deneme 3 -> 4)

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
@plan: kanatları düz olmadığı için kağıt uçak düştü | resimdeki kurala uydu ve kanatları eşit katladı
@tohum: chase-0172
@degisim: elmalı -> beyaz
Bir sabah Chase evde ilk kez kağıttan uçak yapmayı denedi. Defterden beyaz bir sayfa kopardı ve katladı. Ama uçak hemen yere düştü, çünkü kanatları düz değildi. Defterin arkasında bir uçak resmi vardı. Resmin altında da bir kural yazılıydı: İki kanat düz ve eşit olmalıydı. Chase kurallara uyan bir polis köpeğiydi. Kanatları resimdeki gibi katladı. Sonra uçağı havaya attı. Uçak havada uzun uzun uçtu. Chase sevinçle havladı ve uçağın arkasından koştu. Chase bundan sonra kağıttan bir şey katlarken hep önce resme baktı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Defterin arkasında bir uçak resmi vardı"
   - Cümle 4: «Defterin arkasında bir uçak resmi vardı.»
   - Açıklama: Çözümü getiren resim ve kural sebepsizce defterin arkasında beliriyor.
   - Açıklama: Çözümü hazır veren resim ve kural sorundan sonra sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0172` birebir aynı, `@degisim: elmalı -> beyaz` (tutuyorsan), ardından `@onarim: 0530514172dc9938ae48a742914ab97100edd23a`, sonra gövde.

### Hikâye 4: tohum chase-0173 (deneme 3 -> 4)

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
@plan: çitin kapısı kilitliydi ve açılmadı | çite çıkmadı ve hortumu tahtaların arasından itti
@tohum: chase-0173
@degisim: karabiber -> hortum
Chase parkta çiçek sulama oyunu oynuyordu. Parkın musluğuna takılı uzun bir hortum vardı. Ama çiçeklerin çevresindeki çitin kapısı kilitliydi ve açılmadı. Parkta bir kural vardı: Çitin üstüne kimse çıkmazdı. Chase bir polis köpeğiydi, bu yüzden o da çıkmadı. Hortum esnekti, yani kolayca bükülüyordu. Chase hortumu büktü ve ucunu iki tahtanın arasından içeri itti. Musluğu açtı ve su çiçeklere aktı. Kuru çiçeklerin toprağı ıslandı. Chase kuyruğunu salladı ve sevinçle havladı. Chase bundan sonra kapı kilitliyken de çiçekleri böyle suladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hortum esnekti, yani kolayca"
   - Cümle 6: «Hortum esnekti, yani kolayca bükülüyordu.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki bir çocuk bilmez ve 'yani' ile yapılan tanım açıklaması çocuk diline uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0173` birebir aynı, `@degisim: karabiber -> hortum` (tutuyorsan), ardından `@onarim: c68015cb73ab12ffa484ad110853edca4e1a422d`, sonra gövde.

### Hikâye 5: tohum chase-0177 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0177
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'bluz', fiil 'kabarmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | -
@plan: parkta tatlı bir koku vardı ama çiçek görünmüyordu | kokuyu izleyip çitin arkasında çiçeği buldu
@tohum: chase-0177
@degisim: bluz -> çiçek
Chase parkta çimlerin üstünde oturuyordu. Birden rüzgar esti ve Chase'in tüyleri kabardı. Rüzgar tatlı bir koku getirdi ama etrafta hiç çiçek yoktu. Chase bu kokunun nereden geldiğini çok merak etti. Hemen ayağa kalktı. Burnunu havaya kaldırdı ve havayı kokladı. Koku çitin arkasından geliyordu. Chase kokuya doğru çitin yanından yürüdü. Çitin sonunda mor bir çiçek vardı. Çiçek yeni açmıştı ve çok güzel kokuyordu. Chase onu daha iyi görmek için yavaşça yaklaştı. Sonra çiçeğin yanına oturdu ve onu mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Chase bu kokunun nereden geldiğini çok merak etti"
   - Cümle 4: «Chase bu kokunun nereden geldiğini çok merak etti.»
   - Açıklama: Sorun yalnız bir merak; ortada çözülmesi gereken, çocuğun önemseyeceği gerçek bir sorun yok.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Burnunu havaya kaldırdı ve havayı kokladı"
   - Cümle 6: «Burnunu havaya kaldırdı ve havayı kokladı.»
   - Açıklama: 'Hava' kelimesi aynı cümlede gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0177` birebir aynı, `@degisim: bluz -> çiçek` (tutuyorsan), ardından `@onarim: 7506d729638a309127912b108ce3b42e4cc02932`, sonra gövde.

### Hikâye 6: tohum chase-0178 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Ryder
@tohum: chase-0178
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'telefon', fiil 'kutlamak', sıfat 'çizgili'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Ryder
@plan: kek kutusunun nerede olduğu unutulmuştu | burnuyla çilek kokusunu izleyip kutuyu buldu
@tohum: chase-0178
Chase evde doğum gününü Ryder ile kutlamak istiyordu. Ryder çizgili bir kutuya çilekli bir kek koymuştu. Ama telefonla konuşurken kutuyu nereye bıraktığını unutmuştu. "Chase, kek kutusunu bulabilir misin?" diye sordu Ryder. Chase burnunu havaya kaldırdı ve kokladı. Kulübelerin arasından tatlı bir çilek kokusu geliyordu. Chase kokuyu izledi ve en küçük kulübeye koştu. Çizgili kutu kulübenin içinde duruyordu. Chase kutuyu dişleriyle tuttu ve Ryder'a getirdi. "Harika, Chase, şimdi kutlayabiliriz!" dedi Ryder. İkisi keki paylaştı ve şarkı söyledi. Chase çok mutluydu, çünkü kayıp keki kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kulübelerin arasından tatlı bir çilek kokusu geliyordu"
   - Cümle 6: «Kulübelerin arasından tatlı bir çilek kokusu geliyordu.»
   - Açıklama: Evde geçen hikayede kulübeler hiç kurulmadan sebepsizce beliriyor ve kek kutusunun oraya nasıl gittiği açıklanmıyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "en küçük kulübeye koştu"
   - Cümle 7: «Chase kokuyu izledi ve en küçük kulübeye koştu.»
   - Açıklama: Başlıktaki yer ev iken olay kulübelerin arasına kayıyor ve yer belirsizleşiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0178` birebir aynı, ardından `@onarim: dafb9f7ba74cafe0eca3f38a77dd1d93f47e7877`, sonra gövde.

### Hikâye 7: tohum chase-0179 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0179
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'tost', fiil 'yapmak', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: güzel bir kabuk kıyıdan uzakta suyun içindeydi | suya girmeden kıyıda bekledi ve dalgalar kabuğu getirdi
@tohum: chase-0179
@degisim: tost -> kabuk
Chase ile Marshall kumsalda kumdan bir kale yapıyordu. Birden Chase suyun içinde yuvarlak, pembe bir kabuk gördü. Kabuk dalgaların arasında parlıyordu ama kıyıdan biraz uzaktaydı. "Bu kabuk kaleye çok yakışır, hadi suya girip alalım!" dedi Marshall. "Dur, Marshall, kural şu: suya girmek yok, kıyıda bekleyelim," dedi Chase. Marshall kıyıda durdu ve Chase'in yanına oturdu. Her dalga kabuğu biraz daha kıyıya getirdi. Sonunda kabuk Chase'in önüne geldi. Chase kabuğu ağzıyla aldı ve kalenin tepesine koydu. "Teşekkürler, Chase, kalemiz artık çok güzel oldu!" dedi Marshall.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Her dalga kabuğu biraz daha kıyıya getirdi"
   - Cümle 7: «Her dalga kabuğu biraz daha kıyıya getirdi.»
   - Açıklama: Sorunu Chase değil dalgalar çözüyor; Chase yalnız bekliyor ve kabuk şans eseri önüne geliyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Her dalga kabuğu biraz daha kıyıya getirdi"
   - Cümle 7: «Her dalga kabuğu biraz daha kıyıya getirdi.»
   - Açıklama: Çözümü Chase'in eylemi değil dalgaların şansı getiriyor; çözüm sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0179` birebir aynı, `@degisim: tost -> kabuk` (tutuyorsan), ardından `@onarim: 1a071edd9d678fdb42805c3da4157c74c409eb26`, sonra gövde.
