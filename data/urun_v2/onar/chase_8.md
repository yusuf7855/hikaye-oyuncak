# Editör görevi (onarım): Chase, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0006 (deneme 2 -> 3)

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
Yağmur yeni dinmişti ve ağaçlardan damlalar düşüyordu. Chase ile Skye ormandaki kamp yerinde bir meyve tabağı yapmak istedi. Ama yağmur yüzünden kampın masası çok çamurlu olmuştu. Chase kuralı biliyordu: yemek masası temiz olmalıydı. "Önce masayı temizleyelim, Skye," dedi Chase. Chase bir kova su ve bir bez getirdi. Masayı sildi ve güzelce kuruladı. Skye kırmızı çilekleri, Chase de yeşil üzümleri getirdi. İkisi meyveleri büyük bir tabağa dizdi. Çilekler çiçek yaprakları gibi duruyordu, üzümler de tam ortadaydı. Skye tabağa baktı ve sevinçle zıpladı. "Tabak çiçek gibi oldu, teşekkürler, Chase!" dedi Skye.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çilekler çiçek yaprakları gibi duruyordu"
   - Cümle 10: «Çilekler çiçek yaprakları gibi duruyordu, üzümler de tam ortadaydı.»
   - Açıklama: Benzetme küçük çocuk için mecaz sayılır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0006` birebir aynı, `@degisim: kavuşmak -> dizmek` (tutuyorsan), ardından `@onarim: 2aa27fc6be6512cba4e13467b4bc4f226d43d2db`, sonra gövde.

### Hikâye 2: tohum chase-0012 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Dağda soğuk bir rüzgar esiyordu. Chase yumuşak kardan küçük bir pasta yapmıştı ve tepesine süs arıyordu. Ağaçtaki tek kozalak ise biraz yüksek bir dalda duruyordu. Chase önce ağaca tırmanmak istedi. Ama bu yasaktı ve Chase kurallara uydu. Chase ön patileriyle ağacın gövdesine tutundu ve arka ayaklarının üstünde durdu. Sonra kozalağı ağzıyla yavaşça kopardı. Onu dikkatlice pastanın tepesine koydu. Kardan pasta artık çok güzel görünüyordu. Chase pastanın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama bu yasaktı ve Chase kurallara uydu"
   - Cümle 5: «Ama bu yasaktı ve Chase kurallara uydu.»
   - Açıklama: 'Yasak' ve 'kurallara uymak' soyut kavramlar, 3 yaşındaki çocuk için somut değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 5: «Ama bu yasaktı ve Chase kurallara uydu.»
   - Açıklama: 'Kurallara uymak' ve 'yasak' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama bu yasaktı ve Chase kurallara uydu"
   - Cümle 5: «Ama bu yasaktı ve Chase kurallara uydu.»
   - Açıklama: Tırmanmanın neden yasak olduğu söylenmiyor; kural sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0012` birebir aynı, `@degisim: şapkalı -> yumuşak` (tutuyorsan), ardından `@onarim: a3d8e68e8c1992a62b2b50a552a4cdcf355172c3`, sonra gövde.

### Hikâye 3: tohum chase-0013 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | deniz | Rubble
@tohum: chase-0013
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'tekne', fiil 'yardımlaşmak', sıfat 'sağlıklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Rubble
@plan: teknenin içinden bir ses geldi | arkadaşıyla örtüyü açıp sesi yapan kabukları buldu
@tohum: chase-0013
@degisim: sağlıklı -> renkli
Bir sabah Chase ile Rubble kumsalda yürüyordu. Birden küçük bir tekneden "tık tık" diye bir ses geldi. Teknenin üstünde büyük bir örtü vardı. Chase bu sesi çok merak etti. "Rubble, bu örtüyü birlikte açalım mı?" diye sordu Chase. "Tabii, ben çok güçlüyüm," dedi Rubble. İkisi yardımlaştı ve örtüyü yavaşça açtı. Teknenin içinde renkli deniz kabukları vardı. Dalgalar tekneyi sallıyordu ve kabuklar birbirine çarpıyordu. Chase kabukları mavi şapkasına doldurdu ve şapkayı salladı. Şapkadan da aynı "tık tık" sesi geldi. Rubble kabuklara bakıp güldü. "Sesi kabuklar yapıyormuş, Chase!" dedi Rubble sevinçle.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük bir tekneden "tık tık" diye bir ses geldi"
   - Cümle 2: «Birden küçük bir tekneden "tık tık" diye bir ses geldi.»
   - Açıklama: Tekneden gelen ses gerçek bir sorun değil, hikayede önemsenecek bir aksilik kurulmuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden küçük bir tekneden"
   - Cümle 2: «Birden küçük bir tekneden "tık tık" diye bir ses geldi.»
   - Açıklama: Tekneden gelen ses bir sorun değil, yalnız merak konusu; çözülecek gerçek bir sorun yok.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi yardımlaştı ve örtüyü yavaşça açtı"
   - Cümle 7: «İkisi yardımlaştı ve örtüyü yavaşça açtı.»
   - Açıklama: Dalgaların salladığı, bilinmeyen bir teknenin örtüsünü açmak çocuğun taklit edebileceği riskli bir davranış.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kabukları mavi şapkasına doldurdu"
   - Cümle 10: «Chase kabukları mavi şapkasına doldurdu ve şapkayı salladı.»
   - Açıklama: Tohumdaki şapka özelliği sorunu çözmüyor; sorun örtüyü açınca zaten çözülmüş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0013` birebir aynı, `@degisim: sağlıklı -> renkli` (tutuyorsan), ardından `@onarim: bea6fff1f0838271155ba31f96d1babece1e98cb`, sonra gövde.

### Hikâye 4: tohum chase-0015 (deneme 3 -> 4)

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
Denizden serin bir rüzgar esiyordu. Chase kumsalda havlularını kurusun diye bir çamaşır ipine asmıştı. Havlular kurumuştu ama birden yağmur başladı. Yağmurda eşyalar hemen toplanırdı ve Chase bu kurala uydu. Hemen koştu ve havluları ipten aldı. Onları katladı ve getirdiği büyük poşete koyup sıkıca paketledi. Poşete hiç yağmur girmedi. Az sonra yağmur dindi ve güneş çıktı. Chase poşeti açtı; havlular kuru kalmıştı. Chase kuru bir havluyu kuma serdi ve üstüne mutlu mutlu uzandı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "eşyalar hemen toplanırdı ve Chase bu kurala uydu"
   - Cümle 4: «Yağmurda eşyalar hemen toplanırdı ve Chase bu kurala uydu.»
   - Açıklama: 'Kurala uymak' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "getirdiği büyük poşete koyup"
   - Cümle 6: «Onları katladı ve getirdiği büyük poşete koyup sıkıca paketledi.»
   - Açıklama: Poşet önceden kurulmadan tam çözüm anında beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0015` birebir aynı, `@degisim: tedbirli -> büyük` (tutuyorsan), ardından `@onarim: c8169236d32422febace5a3328339af93d203bd8`, sonra gövde.

### Hikâye 5: tohum chase-0019 (deneme 3 -> 4)

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
@plan: bakmadan koştu ve papatya dolu kovaya çarptı | kuralı hatırlayıp özür diledi ve papatyaları topladı
@tohum: chase-0019
@degisim: yüklemek -> doldurmak
Dalgalar kumsala hafifçe vuruyordu. Chase kumsalda koşuyor, Marshall ise rengarenk kovasını papatyalarla dolduruyordu. Chase önüne bakmadı ve kovaya çarptı. Bütün papatyalar kuma döküldü. "Eyvah, papatyalar!" dedi Marshall üzgün bir sesle. Chase kuralı hatırladı ve hemen Marshall'ın yanına gitti. "Özür dilerim, Marshall, sana bakmadan koştum," dedi Chase. Sonra papatyaları tek tek topladı ve kovayı yeniden doldurdu. "Sorun değil, Chase, teşekkür ederim," dedi Marshall. Marshall dolu kovasını mutlu mutlu taşıdı. Chase bundan sonra kumsalda koşarken hep önüne baktı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kuralı hatırladı"
   - Cümle 6: «Chase kuralı hatırladı ve hemen Marshall'ın yanına gitti.»
   - Açıklama: Hiç anlatılmamış bir 'kural' soyut kavram olarak geçiyor ve çocuk neyi kastettiğini bilemez.
   - Açıklama: Hiç anlatılmamış soyut bir 'kural'dan söz ediliyor; çocuk hangi kuralı kastettiğini bilemez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kuralı hatırladı"
   - Cümle 6: «Chase kuralı hatırladı ve hemen Marshall'ın yanına gitti.»
   - Açıklama: Tohumdaki kurallara uyma özelliği hangi kural olduğu söylenmeden belirsiz biçimde geçiyor ve çözümü kural değil özür sağlıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kuralı hatırladı"
   - Cümle 6: «Chase kuralı hatırladı ve hemen Marshall'ın yanına gitti.»
   - Açıklama: Hangi kuralın hatırlandığı hiç söylenmiyor; kural sebepsizce özellikten beliriyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sana bakmadan koştum"
   - Cümle 7: «"Özür dilerim, Marshall, sana bakmadan koştum," dedi Chase.»
   - Açıklama: Chase önüne bakmadan koştu; 'sana bakmadan' yanlış anlam veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0019` birebir aynı, `@degisim: yüklemek -> doldurmak` (tutuyorsan), ardından `@onarim: b2483b650c01f870ec4dd9ecbe97b5deee9d9fe4`, sonra gövde.

### Hikâye 6: tohum chase-0022 (deneme 3 -> 4)

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
Karlı dağda yumuşak kar yağıyordu. Chase kırmızı oyuncak ayakkabısını ağzında düzeltip havaya atıyordu. Ama ayakkabı bir kez uzağa düştü ve karın içine battı. Chase oraya koştu ama ayakkabıyı göremedi. Her yer bembeyazdı. Sonra burnunu yere yaklaştırdı ve oyuncağının kokusunu aldı. Koku küçük bir kar yığınının içinden geliyordu. Chase patileriyle orayı hızlı hızlı kazdı. Kırmızı ayakkabı sonunda göründü. Chase onu ağzına aldı ve sıkıca tuttu. Chase çok sevindi, çünkü en sevdiği oyuncağını bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ağzında düzeltip havaya atıyordu"
   - Cümle 2: «Chase kırmızı oyuncak ayakkabısını ağzında düzeltip havaya atıyordu.»
   - Açıklama: Ayakkabıyı ağızda 'düzeltmek' anlamca uygun değil.
   - Açıklama: 'Ağzında düzeltmek' anlamsız, fiil bağlama uymuyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Chase kırmızı oyuncak ayakkabısını"
   - Cümle 2: «Chase kırmızı oyuncak ayakkabısını ağzında düzeltip havaya atıyordu.»
   - Açıklama: Kartta Chase'in en sevdiği oyuncak olarak kırmızı bir oyuncak ayakkabısı yok; kapalı dünyaya karttan olmayan bir eşya ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0022` birebir aynı, `@degisim: saygılı -> yumuşak` (tutuyorsan), ardından `@onarim: fdd3df0d3ccc701a257f64c8074da35746cf1986`, sonra gövde.

### Hikâye 7: tohum chase-0023 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | Rubble
@tohum: chase-0023
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'yorgan', fiil 'denemek', sıfat 'nazik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Rubble
@plan: rüzgar kırmızı yaprağı çiçeklerin arasına düşürdü | çiçeklere basmadan uzun bir dalla yaprağı çekti
@tohum: chase-0023
@degisim: yorgan -> yaprak
Bir sabah Chase ile Rubble parkta sarı yapraklara bakıyordu. Rubble yerde kocaman, kırmızı bir yaprak gördü. Ama rüzgar esti ve yaprak çiçeklerin arasına düştü. Rubble hemen çiçeklere doğru koştu. "Dur, Rubble, çiçeklere basmak yasak," dedi Chase. Chase parkın kurallarına her zaman uyardı. Yolun kenarında uzun bir dal buldu. "Bunu bir deneyelim," dedi Chase. Dalı çiçeklerin üstünden uzattı ve yaprağı yavaşça kendine çekti. Kırmızı yaprak hiç yırtılmadan yola geldi. Rubble onu aldı ve sevinçle zıpladı. "Sen çok naziksin, Chase," dedi Rubble. Sonra Chase ile Rubble parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve yaprak çiçeklerin arasına düştü"
   - Cümle 3: «Ama rüzgar esti ve yaprak çiçeklerin arasına düştü.»
   - Açıklama: Parkta yerden alınan bir yaprağın uçması önemsiz bir sorun; yerde başka yapraklar da var.
   - Açıklama: Sarı yapraklarla dolu parkta rüzgarın tek bir yaprağı çiçeklere düşürmesi önemsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0023` birebir aynı, `@degisim: yorgan -> yaprak` (tutuyorsan), ardından `@onarim: 8b3c5708877b777ca7e8c165a5803b6cb54825f9`, sonra gövde.

### Hikâye 8: tohum chase-0026 (deneme 2 -> 3)

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
@plan: kardan köpeğin gözleri eksikti ve yakında taş yoktu | iki siyah zeytini göz olarak koydu
@tohum: chase-0026
Chase karlı dağda, yolun kenarında kardan bir köpek yapıyordu. Köpeğin başı ve kulakları hazırdı. Ama gözleri eksikti, çünkü yolda hiç koyu taş yoktu. Koyu taşlar yolun dışında, akan küçük bir suyun yanındaydı. Chase kurallara uyardı ve yoldan çıkmadı. Biraz düşündü ve çantasını açtı. Çantada öğle yemeği için bir sandviç vardı. Sandviçin arasında siyah zeytinler görünüyordu. Chase iki zeytini aldı ve onları köpeğin yüzüne koydu. Artık köpeğin iki parlak gözü vardı. Chase sandviçinin kalanını onun yanında mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yakında taş yoktu"
   - Cümle 0 (plan satırı): «kardan köpeğin gözleri eksikti ve yakında taş yoktu | iki siyah zeytini göz olarak koydu»
   - Açıklama: Gövdede koyu taşlar yakında, yolun dışında suyun yanında var; plan taş olmadığını söylüyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kardan köpeğin gözleri eksikti ve yakında taş yoktu"
   - Cümle 0 (plan satırı): «kardan köpeğin gözleri eksikti ve yakında taş yoktu | iki siyah zeytini göz olarak koydu»
   - Açıklama: Gövdede taş yakında, akan suyun yanında var; sorun taşın olmaması değil yoldan çıkamamak.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 5: «Chase kurallara uyardı ve yoldan çıkmadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve 'uyardı' 'uyarmak' ile karışabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0026` birebir aynı, ardından `@onarim: 2fc426856553134150f8ad9e323ea50cb91d1ff1`, sonra gövde.

### Hikâye 9: tohum chase-0028 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0028
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'dondurma', fiil 'çekmek', sıfat 'çıtır'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | -
@plan: rüzgar şapkayı salıncağın ipine uçurdu | şapkayı ağzıyla tuttu ve yavaşça çekti
@tohum: chase-0028
@degisim: dondurma -> yaprak
Rüzgar esiyordu ve parkta sarı yapraklar uçuşuyordu. Chase yaprak yığınına zıplıyor ve çıtır sesler çıkarıyordu. Birden güçlü bir rüzgar esti ve Chase'in mavi şapkasını uçurdu. Şapka boş salıncağın ipine takıldı ve orada kaldı. Chase salıncağın yanına gitti ve şapkaya dikkatle baktı. Şapkanın ucunu ağzıyla tuttu ve yavaşça çekti. Şapka ipten çıktı ve yere düştü. Chase şapkasını hemen başına taktı. Sonra yine yaprak yığınına koştu. Chase yaprak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şapka boş salıncağın ipine takıldı"
   - Cümle 4: «Şapka boş salıncağın ipine takıldı ve orada kaldı.»
   - Açıklama: Rüzgarın şapkayı uçurması ve şapkanın hemen geri alınması, 'uçurdu, topladı, bitti' türünden önemsiz bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0028` birebir aynı, `@degisim: dondurma -> yaprak` (tutuyorsan), ardından `@onarim: c11c943a565248b38bf7f2554c214069e7fba14f`, sonra gövde.

### Hikâye 10: tohum chase-0030 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0030
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'elbise', fiil 'dizmek', sıfat 'bol'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: güneş karda parlıyordu ve arkadaşı göremiyordu | kendi şapkasını arkadaşına verdi
@tohum: chase-0030
@degisim: elbise -> duvar
Rüzgar hafif hafif esiyordu. Dağda bol kar vardı ve Chase ile Rubble kardan bir duvar yapıyordu. Ama güneş karda çok parlıyordu ve Rubble gözlerini açamıyordu. "Hiçbir şey göremiyorum, Chase," dedi Rubble. Chase mavi şapkasını çıkardı. "Al, Rubble, bunu sen tak," dedi Chase. Rubble onu hemen başına taktı. Artık güneş gözlerine gelmiyordu. Rubble kar toplarını yan yana, dümdüz dizdi. Chase da yeni toplar yaptı ve ona uzattı. Kısa sürede duvar bitti. "Teşekkürler, Chase, sen çok iyi bir arkadaşsın!" dedi Rubble.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Chase da yeni toplar"
   - Cümle 10: «Chase da yeni toplar yaptı ve ona uzattı.»
   - Açıklama: 'Chase' okunuşuna göre bağlaç 'de' olmalı; ek uyumu belirsiz.
   - Açıklama: 'Chase' ince ünlüyle okunur, bağlaç 'de' olmalı: 'Chase de'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0030` birebir aynı, `@degisim: elbise -> duvar` (tutuyorsan), ardından `@onarim: 64e4dcce2de8e98beae18be96b915a6d44a06b74`, sonra gövde.

### Hikâye 11: tohum chase-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0031
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'askı', fiil 'yarışmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kabukları ağzıyla taşıyamadı | şapkasını çıkarıp kabukları içine koydu
@tohum: chase-0031
@degisim: askı -> kabuk
Kumsalda Chase küçük dalgalarla yarışıyordu. Birden kumda karışık renkli kabuklar gördü. Kabuklar çok güzeldi. Hepsini toplamak istedi ama ağzına yalnız bir kabuk sığıyordu. Chase biraz düşündü. Sonra mavi şapkasını çıkardı ve kuma koydu. Kabukları tek tek şapkasının içine yerleştirdi. Pembe, beyaz ve sarı kabuklar şapkayı doldurdu. Chase şapkanın ucunu ağzıyla tuttu ve dikkatle kaldırdı. Hiçbir kabuk düşmedi. Şimdi kumda hiç kabuk kalmamıştı, hepsi şapkadaydı. Chase çok sevindi, çünkü bütün kabukları toplamıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase küçük dalgalarla yarışıyordu"
   - Cümle 1: «Kumsalda Chase küçük dalgalarla yarışıyordu.»
   - Açıklama: Dalgalarla yarışmak mecazdır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük dalgalarla yarışıyordu"
   - Cümle 1: «Kumsalda Chase küçük dalgalarla yarışıyordu.»
   - Açıklama: Dalgalar yarışmaz; mecazlı anlatım küçük çocuğa uygun değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ağzına yalnız bir kabuk sığıyordu"
   - Cümle 4: «Hepsini toplamak istedi ama ağzına yalnız bir kabuk sığıyordu.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase çok sevindi, çünkü bütün kabukları toplamıştı"
   - Cümle 12: «Chase çok sevindi, çünkü bütün kabukları toplamıştı.»
   - Açıklama: Bir önceki cümledeki bütün kabukların şapkada olduğu bilgisi gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0031` birebir aynı, `@degisim: askı -> kabuk` (tutuyorsan), ardından `@onarim: b4a86fde71c9db6d6b19e12efd232166f5caf2b8`, sonra gövde.

### Hikâye 12: tohum chase-0033 (deneme 2 -> 3)

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
Bir sabah karlı dağ çok güneşliydi. Chase ile Ryder kaymak için küçük bir tepeye çıktı. Ama yalnız Chase'in kızağı vardı, çünkü Ryder'ın kızağı kırılmıştı. Ryder üzgün üzgün Chase'e baktı. "Ryder, gel, bu kızak ikimizin!" dedi Chase. "İkimiz sığar mıyız?" diye sordu Ryder. Chase kuyruğunu salladı ve öne oturdu. Ryder de arkasına oturdu. "Kurala uyalım, sıkı tutun," dedi Chase. Ryder iki eliyle kızağı tuttu. Kızak karın üstünde yavaşça aşağı indi. Sonra ikisi aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kurala uyalım, sıkı tutun"
   - Cümle 9: «"Kurala uyalım, sıkı tutun," dedi Chase.»
   - Açıklama: Tek kişiye 'tutun' değil 'tut' denmeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala uyalım, sıkı tutun"
   - Cümle 9: «"Kurala uyalım, sıkı tutun," dedi Chase.»
   - Açıklama: 'Kural' soyut bir kavram ve hangi kuralın kastedildiği belli değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala uyalım, sıkı"
   - Cümle 9: «"Kurala uyalım, sıkı tutun," dedi Chase.»
   - Açıklama: 'Kural' soyut ve önceden tanıtılmamış bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0033` birebir aynı, `@degisim: kaktüs -> kızak` (tutuyorsan), ardından `@onarim: 78acaf69e0752d90c05623cdbb1d00c580fd2dab`, sonra gövde.
