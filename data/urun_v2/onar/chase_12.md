# Editör görevi (onarım): Chase, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0006 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0006
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'masa', fiil 'kavuşmak', sıfat 'çamurlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: yağmur yüzünden kampın masası çok çamurlu oldu | kurala uydu, masayı temizledi ve tabağı hazırladı
@tohum: chase-0006
@degisim: kavuşmak -> dizmek
Yağmur yeni dinmişti ve ağaçlardan damlalar düşüyordu. Chase ile Skye ormandaki kamp yerinde bir meyve tabağı yapmak istedi. Ama yağmur yüzünden kampın masası çok çamurlu olmuştu. Chase kuralı biliyordu: yemek masası temiz olmalıydı. "Önce masayı temizleyelim, Skye," dedi Chase. Chase bir kova su ve bir bez getirdi. Masayı sildi ve güzelce kuruladı. Skye kırmızı çilekleri, Chase de yeşil üzümleri getirdi. İkisi meyveleri büyük bir tabağa dizdi. Çilekler kenarda, üzümler de tam ortadaydı. Skye tabağa baktı ve sevinçle zıpladı. "Tabak harika oldu, teşekkürler, Chase!" dedi Skye.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Skye kırmızı çilekleri, Chase de yeşil üzümleri getirdi"
   - Cümle 8: «Skye kırmızı çilekleri, Chase de yeşil üzümleri getirdi.»
   - Açıklama: Meyve kaybolmuşken hiçbir açıklama olmadan meyveler getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0006` birebir aynı, `@degisim: kavuşmak -> dizmek` (tutuyorsan), ardından `@onarim: 7d55ff729427dfd0802d13d7b43eff63e9498fdb`, sonra gövde.

### Hikâye 2: tohum chase-0012 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0012
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pasta', fiil 'tutunmak', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: süs olacak kozalak biraz yüksek bir dalda duruyordu | ağaca tırmanmadı, gövdeye tutundu ve kozalağı aldı
@tohum: chase-0012
@degisim: şapkalı -> yumuşak
Dağda soğuk bir rüzgar esiyordu. Chase yumuşak kardan küçük bir pasta yapmıştı ve tepesine süs arıyordu. Ağaçtaki tek kozalak ise biraz yüksek bir dalda duruyordu. Chase önce ağaca tırmanmak istedi. Ama Chase kurallara uydu ve karlı ağaca çıkmadı, çünkü dallar kaygandı. Chase ön patileriyle ağacın gövdesine tutundu ve arka ayaklarının üstünde durdu. Sonra kozalağı ağzıyla yavaşça kopardı. Onu dikkatlice pastanın tepesine koydu. Kardan pasta artık çok güzel görünüyordu. Chase pastanın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "biraz yüksek bir dalda duruyordu"
   - Cümle 3: «Ağaçtaki tek kozalak ise biraz yüksek bir dalda duruyordu.»
   - Açıklama: Kozalak arka ayaklar üstünde durunca alınabildiği için sorun neredeyse yok ve zayıf.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama Chase kurallara uydu"
   - Cümle 5: «Ama Chase kurallara uydu ve karlı ağaca çıkmadı, çünkü dallar kaygandı.»
   - Açıklama: Hangi kurala uyulduğu söylenmiyor; kural sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0012` birebir aynı, `@degisim: şapkalı -> yumuşak` (tutuyorsan), ardından `@onarim: 257a6d077b1b12c86f6b3971fb258023c15ac9cb`, sonra gövde.

### Hikâye 3: tohum chase-0015 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0015
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'çamaşır', fiil 'paketlemek', sıfat 'tedbirli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: havlular ipte asılıydı ve yağmur başladı | havluları ipten aldı ve poşete koyup paketledi
@tohum: chase-0015
@degisim: tedbirli -> büyük
Denizden serin bir rüzgar esiyordu. Chase kumsalda havlularını kurusun diye bir çamaşır ipine asmıştı. Havlular kurumuştu ama birden yağmur başladı. Havluları getirdiği büyük poşet de ipin altında duruyordu. Yağmurda eşyalar hemen toplanırdı ve Chase bu kurala uydu. Chase koştu ve havluları ipten aldı. Onları katladı ve poşete koyup sıkıca paketledi. Poşete hiç su girmedi. Az sonra yağmur dindi ve güneş çıktı. Chase poşeti açtı; havlular kuru kalmıştı. Chase kuru bir havluyu kuma serdi ve üstüne mutlu mutlu uzandı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yağmurda eşyalar hemen toplanırdı"
   - Cümle 5: «Yağmurda eşyalar hemen toplanırdı ve Chase bu kurala uydu.»
   - Açıklama: Kural cümlesi soyut ve genel bir ifade; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bu kurala uydu"
   - Cümle 5: «Yağmurda eşyalar hemen toplanırdı ve Chase bu kurala uydu.»
   - Açıklama: 'Kural' ve 'kurala uymak' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0015` birebir aynı, `@degisim: tedbirli -> büyük` (tutuyorsan), ardından `@onarim: 9d4e282c674ed9efddbc5f032d15f57adb1ef26d`, sonra gövde.

### Hikâye 4: tohum chase-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0019
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'papatya', fiil 'yüklemek', sıfat 'rengarenk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: bakmadan koştu ve papatya dolu kovaya çarptı | özür diledi, kurala uyup papatyaları topladı
@tohum: chase-0019
@degisim: yüklemek -> doldurmak
Dalgalar kumsala hafifçe vuruyordu. Chase kumsalda koşuyor, Marshall ise rengarenk kovasını papatyalarla dolduruyordu. Chase önüne bakmadı ve kovaya çarptı. Bütün papatyalar kuma döküldü. "Eyvah, papatyalar!" dedi Marshall üzgün bir sesle. "Özür dilerim, Marshall, kovanı görmedim," dedi Chase. Chase kurallara uydu, papatyaları kumdan tek tek topladı ve kovayı yeniden doldurdu. "Sorun değil, Chase, teşekkür ederim," dedi Marshall. Marshall dolu kovasını mutlu mutlu taşıdı. Chase bundan sonra kumsalda koşarken hep önüne baktı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kurallara uydu, papatyaları"
   - Cümle 7: «Chase kurallara uydu, papatyaları kumdan tek tek topladı ve kovayı yeniden doldurdu.»
   - Açıklama: Papatyaları toplamak bir kurala uymak değil; 'kurallara uydu' yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 7: «Chase kurallara uydu, papatyaları kumdan tek tek topladı ve kovayı yeniden doldurdu.»
   - Açıklama: Hangi kural olduğu belli olmayan soyut 'kurallara uydu' ifadesi papatya toplamayı anlatmaya uymuyor.
   - Açıklama: Hangi kural olduğu belli olmayan soyut 'kurallara uymak' ifadesi çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uydu, papatyaları kumdan tek tek topladı"
   - Cümle 7: «Chase kurallara uydu, papatyaları kumdan tek tek topladı ve kovayı yeniden doldurdu.»
   - Açıklama: Kartın 'kurallara uyar' özelliği hiçbir kural olmadan etiket gibi söyleniyor; çözümü sağlayan kural değil özür ve toplama.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 7: «Chase kurallara uydu, papatyaları kumdan tek tek topladı ve kovayı yeniden doldurdu.»
   - Açıklama: Hikayede hiçbir kural kurulmadığı için kurala uyma sebepsiz ve işlevsiz bir ekleme.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0019` birebir aynı, `@degisim: yüklemek -> doldurmak` (tutuyorsan), ardından `@onarim: 8e76bae3dcff714a3299646d5c20bdbf5ea7ab23`, sonra gövde.

### Hikâye 5: tohum chase-0022 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0022
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'ayakkabı', fiil 'düzeltmek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: oyuncak ayakkabı karın içine battı ve kayboldu | burnuyla kokusunu alıp karı kazdı
@tohum: chase-0022
@degisim: saygılı -> yumuşak
Karlı dağda yumuşak kar yağıyordu. Chase karda kırmızı bir oyuncak ayakkabıyı havaya atıp yakalıyordu. Ama ayakkabı bir kez uzağa düştü ve karın içine battı. Chase oraya koştu ama ayakkabıyı göremedi. Her yer bembeyazdı. Sonra burnunu yere yaklaştırdı ve oyuncağın kokusunu aldı. Koku küçük bir kar yığınının içinden geliyordu. Chase patileriyle orayı hızlı hızlı kazdı. Kırmızı ayakkabı sonunda göründü ama ters duruyordu. Chase onu patisiyle düzeltti ve ağzına aldı. Chase çok sevindi, çünkü kaybolan oyuncağını bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "göründü ama ters duruyordu"
   - Cümle 9: «Kırmızı ayakkabı sonunda göründü ama ters duruyordu.»
   - Açıklama: Ayakkabının ters durması işlevsiz bir ayrıntı; olaya hiçbir şey katmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kırmızı ayakkabı sonunda göründü ama ters duruyordu"
   - Cümle 9: «Kırmızı ayakkabı sonunda göründü ama ters duruyordu.»
   - Açıklama: Ayakkabının ters durması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0022` birebir aynı, `@degisim: saygılı -> yumuşak` (tutuyorsan), ardından `@onarim: 05035f9aedc99ebe40424779c2284863a213afb7`, sonra gövde.

### Hikâye 6: tohum chase-0026 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0026
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: bir şey yapmak
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'sandviç', fiil 'akmak', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: kardan köpeğin gözleri eksikti ama taşlar yolun dışındaydı | iki siyah zeytini göz olarak koydu
@tohum: chase-0026
Chase karlı dağda, yolun kenarında kardan bir köpek yapıyordu. Köpeğin başı ve kulakları hazırdı. Ama gözleri eksikti, çünkü yolda hiç koyu taş yoktu. Koyu taşlar yolun dışında, akan küçük bir suyun yanındaydı. Ama Chase kurallara uydu ve yoldan çıkmadı, çünkü kar derindi. Chase biraz düşündü ve çantasını açtı. Çantada öğle yemeği için bir sandviç vardı. Sandviçin arasında siyah zeytinler görünüyordu. Chase iki zeytini aldı ve onları köpeğin yüzüne koydu. Artık köpeğin iki parlak gözü vardı. Chase sandviçinin kalanını onun yanında mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "akan küçük bir suyun yanındaydı"
   - Cümle 4: «Koyu taşlar yolun dışında, akan küçük bir suyun yanındaydı.»
   - Açıklama: Akan su ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yoldan çıkmadı, çünkü kar derindi"
   - Cümle 5: «Ama Chase kurallara uydu ve yoldan çıkmadı, çünkü kar derindi.»
   - Açıklama: 'Çünkü' bağlacı kurala uymayı derin karla gerekçelendiriyor; bağlaç yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 5: «Ama Chase kurallara uydu ve yoldan çıkmadı, çünkü kar derindi.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Ama Chase kurallara uydu"
   - Cümle 5: «Ama Chase kurallara uydu ve yoldan çıkmadı, çünkü kar derindi.»
   - Açıklama: İki cümle önce de 'Ama' ile başlandığı için bağlaç gereksiz tekrarlanıyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onun yanında mutlu mutlu yedi"
   - Cümle 11: «Chase sandviçinin kalanını onun yanında mutlu mutlu yedi.»
   - Açıklama: 'onun' zamirinin kardan köpeği mi başka birini mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0026` birebir aynı, ardından `@onarim: 4d7922bfbfb779efd271f79a7b9c63add14e9b0e`, sonra gövde.

### Hikâye 7: tohum chase-0033 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0033
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kaktüs', fiil 'sallamak', sıfat 'güneşli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: çocuğun kızağı kırılmıştı ve tek kızak vardı | kızağını çocukla paylaştı ve birlikte kaydılar
@tohum: chase-0033
@degisim: kaktüs -> kızak
Bir sabah karlı dağ çok güneşliydi. Chase ile Ryder kaymak için küçük bir tepeye çıktı. Ama yalnız Chase'in kızağı vardı, çünkü Ryder'ın kızağı kırılmıştı. Ryder üzgün üzgün Chase'e baktı. "Ryder, gel, bu kızak ikimizin!" dedi Chase. "İkimiz sığar mıyız?" diye sordu Ryder. Chase kuyruğunu salladı ve öne oturdu. Ryder de arkasına oturdu. "Ryder, kızağı iki elinle sıkıca tut," dedi Chase. Ryder bu kurala hemen uydu. Kızak karın üstünde yavaşça aşağı indi. Sonra ikisi aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu kurala hemen uydu"
   - Cümle 10: «Ryder bu kurala hemen uydu.»
   - Açıklama: 'Kurala uymak' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ryder bu kurala hemen uydu."
   - Cümle 10: «Ryder bu kurala hemen uydu.»
   - Açıklama: 'Kurala uymak' soyut bir ifade ve Chase'in sözü kural olarak kurulmamıştı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ryder bu kurala hemen uydu"
   - Cümle 10: «Ryder bu kurala hemen uydu.»
   - Açıklama: Karttaki özellik Chase'in kurallara uymasıdır; burada kurala uyan Ryder, Chase ise ekibin başına kural koyuyor.
   - Açıklama: Karttaki 'kurallara uyar' özelliği Chase'e ait; burada kurala uyan Ryder oluyor ve özellik figürde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0033` birebir aynı, `@degisim: kaktüs -> kızak` (tutuyorsan), ardından `@onarim: 4e6ab1b7f46d5a924292f86c9a41e8c48f58623f`, sonra gövde.

### Hikâye 8: tohum chase-0034 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0034
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'mürekkep', fiil 'çalışmak', sıfat 'dikkatli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: rüzgar esince kağıt hep havaya kalkıyordu | kağıdın köşelerine küçük taşlar koydu
@tohum: chase-0034
Ağaçlarda kuşlar ötüyordu. Chase parkta ilk kez mavi mürekkeple pati resmi yapmayı deniyordu. Ama rüzgar esince beyaz kağıt hep havaya kalkıyordu. Chase yerden küçük taşlar topladı. Taşları kağıdın dört köşesine koydu. Artık kağıt rüzgarda hiç kıpırdamadı. Chase patisini dikkatli bir şekilde mürekkebe batırdı. Kurallara uydu ve mürekkepli patisiyle yere hiç basmadı. Sonra kağıda düz basmaya çalıştı. Kağıtta çok güzel bir pati izi çıktı. Chase çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara uydu ve"
   - Cümle 8: «Kurallara uydu ve mürekkepli patisiyle yere hiç basmadı.»
   - Açıklama: 'Kurallara uymak' soyuttur ve hangi kural olduğu belli değildir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara uydu ve mürekkepli"
   - Cümle 8: «Kurallara uydu ve mürekkepli patisiyle yere hiç basmadı.»
   - Açıklama: 'Kurallara uymak' soyut ve hikayede kural anlatılmamış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kurallara uydu ve mürekkepli patisiyle"
   - Cümle 8: «Kurallara uydu ve mürekkepli patisiyle yere hiç basmadı.»
   - Açıklama: Kartın 'kurallara uyar' özelliği sorunla (uçan kağıt) ilgisiz, işe yaramayan bir ek olarak geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kurallara uydu ve mürekkepli patisiyle yere hiç basmadı"
   - Cümle 8: «Kurallara uydu ve mürekkepli patisiyle yere hiç basmadı.»
   - Açıklama: Kurala uyma ayrıntısı hiçbir kurala ya da olaya bağlanmıyor ve olayda işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0034` birebir aynı, ardından `@onarim: 73afd93a1716c80c1e1c798a555b92a3ca1934a0`, sonra gövde.

### Hikâye 9: tohum chase-0035 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0035
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kravat', fiil 'bindirmek', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | -
@plan: kamyon ağacın altındaydı ve boya ıslak kaldı | kamyonu güneşe itti ve kurumasını bekledi
@tohum: chase-0035
@degisim: bindirmek -> taşımak
Bir sabah Chase parkta pürüzsüz bir kağıttan kravat yaptı. Kravatı maviye boyadı ve yanındaki oyuncak kamyonunun üstüne koydu. Ama kamyon ağacın altındaydı ve boya ıslak kaldı. Chase kravatı takıp parkta gezmek istiyordu. Chase kurallara uydu ve ıslak boyaya dokunmadı. Kamyonu burnuyla itti ve kravatı güneşe taşıdı. Sonra kamyonun yanına oturdu ve bekledi. Güneş kravatı ısıttı ve boya kısa sürede kurudu. Chase patisiyle kravatın ucuna hafifçe dokundu. Boya artık patisine yapışmadı. Chase mavi kravatını taktı ve parkta mutlu mutlu gezdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "parkta pürüzsüz bir kağıttan"
   - Cümle 1: «Bir sabah Chase parkta pürüzsüz bir kağıttan kravat yaptı.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pürüzsüz bir kağıttan"
   - Cümle 1: «Bir sabah Chase parkta pürüzsüz bir kağıttan kravat yaptı.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmediği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 5: «Chase kurallara uydu ve ıslak boyaya dokunmadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve olaydan çıkan somut bir ders cümlesi değil.
   - Açıklama: 'Kurallara uymak' soyut bir kavram.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uydu ve ıslak boyaya dokunmadı"
   - Cümle 5: «Chase kurallara uydu ve ıslak boyaya dokunmadı.»
   - Açıklama: Tohumdaki kural özelliği sorunu çözmüyor; boyayı güneş kurutuyor, yani özellik kartın 'ozellikler' alanındaki gibi işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0035` birebir aynı, `@degisim: bindirmek -> taşımak` (tutuyorsan), ardından `@onarim: d4c56ededfde02dc4c3245b1680eb2bff697f91f`, sonra gövde.

### Hikâye 10: tohum chase-0040 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0040
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'vanilya', fiil 'yayılmak', sıfat 'narin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: zıplarken kurabiyeleri düşürdü ve kırdı | özür dileyip parçaları beraber yemeyi istedi
@tohum: chase-0040
@degisim: narin -> ince
Bir sabah Chase karlı dağda sevinçle zıplıyordu. Rubble bir taşın üstüne vanilyalı kurabiyeler koymuştu. Chase zıplarken kuyruğu ince kurabiyeleri taştan düşürdü. Kurabiyeler kırıldı ve parçaları kara yayıldı. Rubble kırık kurabiyelere üzgün üzgün baktı. Ekibin bir kuralı vardı: Bir şeyi kıran özür diler. "Özür dilerim, Rubble, parçaları beraber yiyelim mi?" diye sordu Chase. Rubble bir parçayı ağzına attı ve güldü. İki arkadaş parçaları birlikte yedi. Chase çok sevindi, çünkü Rubble ona hiç kızmamıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ekibin bir kuralı vardı"
   - Cümle 6: «Ekibin bir kuralı vardı: Bir şeyi kıran özür diler.»
   - Açıklama: 'Ekip' ve 'kural' küçük çocuk için soyut, ekip de tanıtılmadan geçiyor.
   - Açıklama: Olaydan çıkmayan genel bir kural cümlesi soyut; 'kural' ve 'ekip' küçük çocuk için soyut kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0040` birebir aynı, `@degisim: narin -> ince` (tutuyorsan), ardından `@onarim: 2ae79dd822776bf803ae3b76629a036ec0cc7f0f`, sonra gövde.

### Hikâye 11: tohum chase-0041 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0041
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'patates', fiil 'köpürmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: kelebekler koşan köpeği görüp uçtu | koşmadı ve sessizce oturup bekledi
@tohum: chase-0041
@degisim: köpürmek -> koşmak
Kulenin önündeki kulübeler düzenli bir sırada duruyordu. Chase kasesinden patates yerken sarı kelebekler gördü. Hemen onlara doğru koştu ama kelebekler havalandı ve uçup gitti. Chase onları daha iyi görmek istiyordu. Sonra bir kuralı hatırladı: Kulübelerin önünde koşmak yasaktı. Chase yerine döndü ve sessizce oturdu. Biraz sonra sarı kelebekler geri geldi. Önce kulenin yanında biraz uçtular. Sonra Chase'in kulübesinin çatısına kondular. Chase hiç kıpırdamadı ve onlara yakından baktı. Chase çok sevindi, çünkü kelebekler sonunda yanına gelmişti.
```

**Hakem bulguları (7):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kasesinden patates yerken"
   - Cümle 2: «Chase kasesinden patates yerken sarı kelebekler gördü.»
   - Açıklama: Patates yeme ayrıntısı hiçbir işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen onlara doğru koştu"
   - Cümle 3: «Hemen onlara doğru koştu ama kelebekler havalandı ve uçup gitti.»
   - Açıklama: Kartın 'güvenli özellik kullanımı' satırına göre Chase kimseyi kovalamaz, burada kelebekleri kovalıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre Chase kimseyi kovalamaz, ama burada kelebeklerin peşinden koşuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra bir kuralı hatırladı"
   - Cümle 5: «Sonra bir kuralı hatırladı: Kulübelerin önünde koşmak yasaktı.»
   - Açıklama: 'Kural' ve 'yasak' soyut kavramlardır, 3 yaşındaki çocuk için uygun değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra bir kuralı hatırladı"
   - Cümle 5: «Sonra bir kuralı hatırladı: Kulübelerin önünde koşmak yasaktı.»
   - Açıklama: Chase kelebekleri geri getirmek için değil tesadüfen bir kural yüzünden oturuyor; çözüm sebebe bilinçli yönelmiyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bir kuralı hatırladı"
   - Cümle 5: «Sonra bir kuralı hatırladı: Kulübelerin önünde koşmak yasaktı.»
   - Açıklama: Çözüm kelebekleri ürküten koşmayı fark etmekten değil, sebepsizce hatırlanan bir kuraldan geliyor.
6. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "sarı kelebekler geri geldi"
   - Cümle 7: «Biraz sonra sarı kelebekler geri geldi.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, uçup gidip geri gelerek olaya katılıyor.
7. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Biraz sonra sarı kelebekler geri geldi"
   - Cümle 7: «Biraz sonra sarı kelebekler geri geldi.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor; uçup gidip geri gelerek olaya katılıyorlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0041` birebir aynı, `@degisim: köpürmek -> koşmak` (tutuyorsan), ardından `@onarim: 31cf72c2ba6c7640ea919b25db918f6c2fcc4a39`, sonra gövde.

### Hikâye 12: tohum chase-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0044
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'sünger', fiil 'aydınlanmak', sıfat 'eğlenceli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: çadırda resmin üstüne su damladı | lambayı yakıp ıslak süngeri buldu
@tohum: chase-0044
Chase, Skye ile çadırda eğlenceli resimler yapıyordu. Birden çadırın tepesinden tıp tıp diye bir ses geldi. Sonra Skye'ın resminin üstüne bir damla su düştü. "Bu su nereden geliyor?" diye sordu Skye. Çadırın içi karanlıktı. Kurala göre karanlıkta önce lamba yakmak gerekiyordu. Chase lambayı yaktı ve çadır aydınlandı. Tepedeki ipte ıslak, sarı bir sünger vardı. Su damla damla ondan düşüyordu. "Bu benim, kurusun diye oraya koymuştum!" dedi Skye ve güldü. Chase onu ipten aldı ve dışarı çıkardı. Sonra ikisi resim yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çadırın içi karanlıktı"
   - Cümle 5: «Çadırın içi karanlıktı.»
   - Açıklama: İkisi çadırda resim yapıyordu ama çadırın içi karanlık deniyor; karanlıkta resim yapılamaz.
   - Açıklama: Çocuklar çadırda resim yaparken içerinin karanlık olması çelişkili.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala göre karanlıkta önce"
   - Cümle 6: «Kurala göre karanlıkta önce lamba yakmak gerekiyordu.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala göre karanlıkta önce lamba yakmak gerekiyordu"
   - Cümle 6: «Kurala göre karanlıkta önce lamba yakmak gerekiyordu.»
   - Açıklama: 'Kurala göre' soyut bir kavram ve 3 yaşındaki çocuğa uygun olmayan kalıp bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0044` birebir aynı, ardından `@onarim: 1314da9012e7f736c61bc341da43f70e240d5e00`, sonra gövde.
