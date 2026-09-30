# Editör görevi (onarım): Chase, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0144 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0144
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'çerçeve', fiil 'götürmek', sıfat 'resimli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: rüzgar toplanan yaprakları elden uçuruyordu | yaprakları şapkaya koyup masaya götürdü
@tohum: chase-0144
@degisim: çerçeve -> kitap
Rüzgar esiyordu ve ağaçlardan renkli yapraklar düşüyordu. Chase ile Ryder kamp yerinde resimli bir kitaptaki yaprakları topluyordu. Ama rüzgar topladıkları yaprakları her seferinde Ryder'ın elinden uçuruyordu. "Yapraklarımız yine uçtu!" dedi Ryder. Chase mavi şapkasını çıkardı ve ters çevirdi. "Yaprakları şapkama koy, Ryder," dedi Chase. Ryder kırmızı, sarı ve turuncu yaprakları şapkanın içine koydu. Şapkanın içindeki yapraklar hiç uçmadı. Chase şapkayı ağzıyla dikkatle tuttu ve kamp masasına götürdü. Ryder yaprakları kitabın yanına koydu ve hepsi resimlerle aynıydı. Chase ile Ryder çok sevindi, çünkü kitaptaki bütün yaprakları bulmuşlardı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "toplanan yaprakları elden uçuruyordu"
   - Cümle 0 (plan satırı): «rüzgar toplanan yaprakları elden uçuruyordu | yaprakları şapkaya koyup masaya götürdü»
   - Açıklama: İyelik eki eksik; 'elinden' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "resimli bir kitaptaki yaprakları topluyordu"
   - Cümle 2: «Chase ile Ryder kamp yerinde resimli bir kitaptaki yaprakları topluyordu.»
   - Açıklama: 'Kitaptaki yaprakları toplamak' kitabın içindeki yaprakları toplamak anlamına geliyor; kitaptaki resimlere benzeyen yapraklar kastediliyor.
   - Açıklama: 'Kitaptaki yapraklar' kitabın sayfaları olarak anlaşılıyor; anlam belirsiz.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar topladıkları yaprakları her seferinde"
   - Cümle 3: «Ama rüzgar topladıkları yaprakları her seferinde Ryder'ın elinden uçuruyordu.»
   - Açıklama: Rüzgarın dağıttığı yaprakları yeniden toplamak çocuk için önemsiz, zayıf bir sorun.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar topladıkları yaprakları her seferinde Ryder'ın elinden uçuruyordu"
   - Cümle 3: «Ama rüzgar topladıkları yaprakları her seferinde Ryder'ın elinden uçuruyordu.»
   - Açıklama: Rüzgarın yaprakları uçurması, toplanıp bitiveren önemsiz bir sorun olarak kalıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hepsi resimlerle aynıydı"
   - Cümle 10: «Ryder yaprakları kitabın yanına koydu ve hepsi resimlerle aynıydı.»
   - Açıklama: Yapraklar resimlerle 'aynı' olmaz; 'resimlere benziyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0144` birebir aynı, `@degisim: çerçeve -> kitap` (tutuyorsan), ardından `@onarim: 602d0dd5b561034719a88c801e8441306ab00735`, sonra gövde.

### Hikâye 2: tohum chase-0145 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0145
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'çeşme', fiil 'kırpmak', sıfat 'rahat'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: çeşme açık kaldı ve güçlü su gemiyi devirdi | çeşmeyi kapattı ve gemi karşıya gitti
@tohum: chase-0145
Ağaçların arasında rüzgar hafif esiyordu. Chase ile Ryder kamp yerinde çeşmenin havuzunda yapraktan gemiyle deniz oyunu oynuyordu. Ama çeşme açık kalmıştı ve güçlü su gemiyi hep deviriyordu. "Gemim karşıya hiç gitmiyor," dedi Ryder. "Çeşme açık kalmaz, Ryder, bu bir kural," dedi Chase. Chase patisiyle çeşmeyi kapattı. Havuzdaki su artık kıpırdamıyordu. Ryder gemiyi yeniden suya koydu. Gemi rahatça karşı kenara gitti. Ryder sevinçle Chase'e göz kırptı. Chase ile Ryder bundan sonra oyuna başlamadan önce çeşmeyi kapattılar.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu bir kural"
   - Cümle 5: «"Çeşme açık kalmaz, Ryder, bu bir kural," dedi Chase.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ryder, bu bir kural"
   - Cümle 5: «"Çeşme açık kalmaz, Ryder, bu bir kural," dedi Chase.»
   - Açıklama: 'Kural' soyut bir kavramdır; somut ders cümlesi değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0145` birebir aynı, ardından `@onarim: 900e00039978a7e99e9960fc30e4deb9ce7bd855`, sonra gövde.

### Hikâye 3: tohum chase-0146 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0146
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: paylaşmak
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'değnek', fiil 'özlemek', sıfat 'kokulu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: yerde tek değnek vardı ve ikisi de çizmek istedi | dal koparmadı ve değneği ikiye böldü ve paylaştı
@tohum: chase-0146
Chase ile Marshall kamp yerinde toprağa resim çizmek istedi. Etrafta kokulu çam ağaçları vardı. Ama yerde yalnız bir değnek vardı. Marshall evdeki yüksek kuleyi özlemişti. "Hadi ağaçtan yeni bir dal koparalım," dedi Marshall. "Olmaz, Marshall, dal koparmak yok, bu bir kural," dedi Chase. Chase değneği ikiye böldü. "Gel, bunu paylaşalım," dedi Chase ve bir parçasını Marshall'a verdi. Marshall toprağa büyük bir kule çizdi. Chase de yanına küçük bir kulübe çizdi. Marshall kuyruğunu mutlu mutlu salladı. Değneği paylaşınca ikisi de resim çizdi.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ikiye böldü ve paylaştı"
   - Cümle 0 (plan satırı): «yerde tek değnek vardı ve ikisi de çizmek istedi | dal koparmadı ve değneği ikiye böldü ve paylaştı»
   - Açıklama: Plan satırında 've' bağlacı gereksiz yere art arda tekrarlanıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ve değneği ikiye böldü ve paylaştı"
   - Cümle 0 (plan satırı): «yerde tek değnek vardı ve ikisi de çizmek istedi | dal koparmadı ve değneği ikiye böldü ve paylaştı»
   - Açıklama: Plan satırında 've' gereksiz yere tekrarlanıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama yerde yalnız bir değnek vardı"
   - Cümle 3: «Ama yerde yalnız bir değnek vardı.»
   - Açıklama: Çam ağaçlarıyla dolu ormanda yerde yalnız bir değnek olması akla yatkın değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu bir kural"
   - Cümle 6: «"Olmaz, Marshall, dal koparmak yok, bu bir kural," dedi Chase.»
   - Açıklama: 'kural' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0146` birebir aynı, ardından `@onarim: a33cccd75a55ee1769c8493e6c957df16fbb341e`, sonra gövde.

### Hikâye 4: tohum chase-0148 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0148
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'taç', fiil 'takılmak', sıfat 'temkinli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: yapraklardan yapılan taç hep dağılıyordu | yaprakları şapkanın kenarına takıp taç yaptı
@tohum: chase-0148
@degisim: temkinli -> yeşil
Chase ile Rubble kamp yerinde yapraklardan bir taç yapıyordu. Ama yaprakları bağlayacak bir şey yoktu ve taç hep dağılıyordu. "Taç yine başımdan düştü!" dedi Rubble ve güldü. Chase mavi şapkasını çıkardı. "Yaprakları şapkamın kenarına takalım," dedi Chase. Chase yeşil yaprakları şapkanın kenarına tek tek soktu. Yapraklar şapkaya sıkıca takıldı ve hiç düşmedi. Şapka artık güzel bir taç gibi görünüyordu. Chase tacı Rubble'ın başına koydu. "Bu taç başımda duruyor, teşekkürler, Chase!" dedi Rubble. Chase ile Rubble oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Rubble kamp yerinde yapraklardan"
   - Cümle 1: «Chase ile Rubble kamp yerinde yapraklardan bir taç yapıyordu.»
   - Açıklama: Başlıktaki yer orman ama hikaye kamp yerinde başlıyor ve orman hiç anılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0148` birebir aynı, `@degisim: temkinli -> yeşil` (tutuyorsan), ardından `@onarim: aedc08f26369b72f3f9503e73d88f6db51b30029`, sonra gövde.

### Hikâye 5: tohum chase-0149 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0149
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'posta', fiil 'savurmak', sıfat 'yardımsever'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: rüzgar teşekkür kartını yüksek bir kayaya savurdu | kurallara uydu, tırmanmadı ve yardım istedi
@tohum: chase-0149
@degisim: posta -> kart
Bir sabah Chase dağda yardımsever Skye için bir teşekkür kartı yapıyordu. Birden rüzgar kartı savurdu ve kart yüksek bir kayanın üstüne düştü. Chase kurallara uydu ve kayaya tırmanmadı. "Skye, kartım kayanın üstünde kaldı, yardım eder misin?" dedi Chase. "Hemen geliyorum, Chase!" dedi Skye. Skye helikopteriyle kayanın üstüne uçtu. Helikopterin rüzgarı kartı aşağı itti. Chase kartı karın üstünden aldı. Skye helikopteri indirdi ve yanına geldi. Chase kartı hemen Skye'a verdi. Skye çok sevindi, çünkü Chase ona güzel bir sürpriz hazırlamıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 3: «Chase kurallara uydu ve kayaya tırmanmadı.»
   - Açıklama: 'Kurallara uymak' somut bir kural anılmadan kullanılan soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve kayaya tırmanmadı"
   - Cümle 3: «Chase kurallara uydu ve kayaya tırmanmadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavramdır ve 3 yaşındaki bir çocuğa uygun değildir.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Chase ona güzel bir sürpriz hazırlamıştı"
   - Cümle 11: «Skye çok sevindi, çünkü Chase ona güzel bir sürpriz hazırlamıştı.»
   - Açıklama: Chase kartı kurtarmak için Skye'dan yardım istediği hâlde son cümle kartı sürpriz olarak sunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0149` birebir aynı, `@degisim: posta -> kart` (tutuyorsan), ardından `@onarim: 3649de21c2f24568917c09c726121f73c559a2ef`, sonra gövde.

### Hikâye 6: tohum chase-0150 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0150
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'testi', fiil 'büyümek', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: çiçeklere su götürmek istedi ama kaygan testi kaydı | testiyi ters şapkanın içine koyup taşıdı
@tohum: chase-0150
Parkta hava sisliydi. Chase çiçeklere bakma oyunu oynuyordu. Parktaki küçük çiçeklerin toprağı çok kuruydu. Chase çiçekler büyüsün diye onlara su götürmek istedi. Oyun için suyla dolu küçük bir testi getirmişti. Ama testi çok kaygandı ve ağzından iki kez kaydı. Chase biraz düşündü. Sonra mavi şapkasını çıkardı ve yere ters koydu. Testiyi burnuyla şapkanın içine itti. Şapkanın kenarını ağzıyla tuttu ve dikkatle yürüdü. Testi bu kez hiç kaymadı. Chase çiçeklerin yanına varınca testiyi yavaşça eğdi. Su aktı ve toprak ıslandı. Chase bundan sonra kaygan şeyleri hep böyle taşıdı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ağzından iki kez kaydı"
   - Cümle 6: «Ama testi çok kaygandı ve ağzından iki kez kaydı.»
   - Açıklama: 'Ağzından' sözcüğünün testinin mi Chase'in mi ağzı olduğu belli değil.
   - Açıklama: 'ağzından' kelimesinin testinin ağzını mı Chase'in ağzını mı gösterdiği belli değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "testi çok kaygandı ve ağzından iki kez kaydı"
   - Cümle 6: «Ama testi çok kaygandı ve ağzından iki kez kaydı.»
   - Açıklama: Sorun (testinin kayması) ancak 6. cümlede söyleniyor, ilk 3 cümlede değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0150` birebir aynı, ardından `@onarim: 9043171734cba7d96163791c3c8c9478f0f56ef8`, sonra gövde.

### Hikâye 7: tohum chase-0151 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0151
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'çan', fiil 'homurdanmak', sıfat 'zor'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: ağaçların arasından çan gibi bir ses geldi | şapkasıyla gözlerini korudu ve buzları buldu
@tohum: chase-0151
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken çan gibi bir ses duydu. Ses ağaçların arasından geliyordu. Chase çok merak etti ve ağaçlara doğru gitti. Ama dallardan yüzüne kar dökülüyordu. Karın içinde bir şey görmek çok zordu. Chase başını salladı ve homurdandı. Sonra mavi şapkasını gözlerinin üstüne biraz indirdi. Kar artık yüzüne gelmedi. Chase dallara dikkatle baktı. Bir dalda küçük buz parçaları asılı duruyordu. Rüzgar esince buzlar birbirine değiyordu. Chase çok sevindi, çünkü o sesi yapan buzları bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağaçların arasından çan gibi bir ses geldi"
   - Cümle 0 (plan satırı): «ağaçların arasından çan gibi bir ses geldi | şapkasıyla gözlerini korudu ve buzları buldu»
   - Açıklama: Merak uyandıran bir ses gerçek bir sorun değil; çocuğun önemseyeceği bir güçlük yok.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama dallardan yüzüne kar dökülüyordu"
   - Cümle 5: «Ama dallardan yüzüne kar dökülüyordu.»
   - Açıklama: Sesin kaynağını bulma merakının yanına yüze dökülen kar diye ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0151` birebir aynı, ardından `@onarim: 7609dfd4149db57184eb63f15c399b2bbc1a1c3f`, sonra gövde.

### Hikâye 8: tohum chase-0152 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0152
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'çakıl', fiil 'dökülmek', sıfat 'kararlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kuru kumdan yapılan kalenin duvarları döküldü | şapkasını ıslak kumla doldurup kuleler yaptı
@tohum: chase-0152
@degisim: kararlı -> ıslak
Bir sabah Chase kumsalda oynuyordu. İlk kez kumdan bir kale yapmayı denedi. Ama kum çok kuruydu ve kalenin duvarları hep dökülüyordu. Chase biraz düşündü ve su kenarına gitti. Orası ıslaktı. Chase mavi şapkasını çıkardı ve içini ıslak kumla doldurdu. Sonra kalesinin yerine döndü. Şapkayı yavaşça ters çevirdi ve kaldırdı. Yerde yuvarlak ve sağlam bir kule durdu. Chase aynı yolla üç tane daha yaptı. Kulelerin üstüne küçük çakıllar dizdi. Bu kez kale hiç dökülmedi. Chase çok sevindi, çünkü ilk kalesini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase aynı yolla üç"
   - Cümle 10: «Chase aynı yolla üç tane daha yaptı.»
   - Açıklama: 'Yol' burada 'yöntem' anlamında soyut kullanılmış; 'aynı şekilde' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0152` birebir aynı, `@degisim: kararlı -> ıslak` (tutuyorsan), ardından `@onarim: 934aaec26cd0a9dd5592c5b11192cd9929b49682`, sonra gövde.

### Hikâye 9: tohum chase-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0153
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'jelibon', fiil 'öpmek', sıfat 'küçücük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: kabukları koyacak yer kalmadı ve kabuklar kuma düştü | şapkasını paylaştı ve kabukları içine koydular
@tohum: chase-0153
@degisim: jelibon -> kabuk
Kumsalda güneş parlıyordu. Chase ile Ryder küçücük kabuklar topluyordu. Ama Ryder'ın cepleri dolmuştu ve kabuklar kuma düşüyordu. "Bunları nereye koyacağız?" diye sordu Ryder. Chase mavi şapkasını çıkardı ve ters çevirdi. "Şapkamı seninle paylaşırım, hepsi buraya sığar, Ryder," dedi Chase. Ryder kabuklarını tek tek şapkanın içine koydu. Chase de kendi bulduklarını ağzıyla ekledi. Az sonra şapka tamamen doldu. Ryder güldü ve Chase'in başını öptü. "Çok teşekkürler, Chase," dedi Ryder. Chase ile Ryder toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Az sonra şapka tamamen doldu"
   - Cümle 9: «Az sonra şapka tamamen doldu.»
   - Açıklama: Şapka tamamen dolmuşken toplamaya devam etmeleri yer kalmadı sorununu yeniden doğuruyor; çözüm çelişkili.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Chase ile Ryder toplamaya mutlu mutlu devam etti"
   - Cümle 12: «Chase ile Ryder toplamaya mutlu mutlu devam etti.»
   - Açıklama: Şapka tamamen dolmuşken kabuk toplamaya devam etmeleri sorunun yeniden doğacağı bir çelişki yaratıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0153` birebir aynı, `@degisim: jelibon -> kabuk` (tutuyorsan), ardından `@onarim: bba012a9db8df5b34dfde2b61a30464d988c5c93`, sonra gövde.

### Hikâye 10: tohum chase-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Marshall
@tohum: chase-0154
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yeni bir şeyi denemek
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'meyve', fiil 'sıçratmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Marshall
@plan: güneş kardan kulenin tepesini eritti | şapkasını tepeye koyup gölge yaptı
@tohum: chase-0154
@degisim: meyve -> taş
Chase ile Marshall karlı dağda ilk kez kardan bir kule yapıyordu. Marshall sevinçle zıpladı ve karı her yere sıçrattı. Ama güneş çok parlaktı ve kulenin tepesi erimeye başladı. "Chase, kulemiz eriyor!" dedi Marshall. Chase mavi şapkasını çıkardı ve kulenin tepesine koydu. Şapkanın gölgesi tepeyi güneşten korudu. Tepedeki kar artık hiç erimedi. "Bu gölge yeterli, Marshall," dedi Chase. Marshall kulenin önüne küçük taşlarla bir kapı yaptı. Chase ile Marshall kulenin etrafında mutlu mutlu koştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Marshall sevinçle zıpladı ve karı her yere sıçrattı"
   - Cümle 2: «Marshall sevinçle zıpladı ve karı her yere sıçrattı.»
   - Açıklama: Karın sıçratılması sorunla ya da çözümle bağlanmayan işlevsiz bir ayrıntı.
   - Açıklama: Marshall'ın karı sıçratması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0154` birebir aynı, `@degisim: meyve -> taş` (tutuyorsan), ardından `@onarim: ac84f3fe38a54f1c9486e72068fd5f59503c82e9`, sonra gövde.

### Hikâye 11: tohum chase-0155 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0155
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'ayna', fiil 'gezinmek', sıfat 'yeşil'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: yağan kar küçük köpeğin gözlerine doldu | şapkasını paylaşıp onun başına taktı
@tohum: chase-0155
@degisim: ayna -> kar
Bir sabah Chase ile Skye karlı dağda geziniyordu. İkisi yeşil çam ağaçlarının arasından yavaşça yürüdü. Birden kar yağmaya başladı. Skye çok küçüktü ve kar taneleri gözlerine doluyordu. "Chase, yolu hiç göremiyorum," dedi Skye. Chase hemen durdu ve biraz düşündü. Sonra mavi şapkasını çıkardı. "Şapkamı seninle paylaşayım, Skye," dedi Chase. Chase şapkayı Skye'ın başına dikkatle taktı. Şapkanın önü kar tanelerini gözlerinden uzak tuttu. Skye etrafa baktı ve yolu gördü. Sevinçle kuyruğunu salladı. "Teşekkürler, Chase, şimdi her yeri görüyorum!" dedi Skye.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Skye çok küçüktü ve kar taneleri gözlerine doluyordu"
   - Cümle 4: «Skye çok küçüktü ve kar taneleri gözlerine doluyordu.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şapkamı seninle paylaşayım, Skye"
   - Cümle 8: «"Şapkamı seninle paylaşayım, Skye," dedi Chase.»
   - Açıklama: Chase şapkayı bütünüyle Skye'a veriyor; 'paylaşmak' burada anlamca doğru değil, 'vereyim' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0155` birebir aynı, `@degisim: ayna -> kar` (tutuyorsan), ardından `@onarim: b56c2755abcca0614bbb3c5cfcd5233792d16788`, sonra gövde.

### Hikâye 12: tohum chase-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0156
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'sakız', fiil 'tekrarlamak', sıfat 'uyanık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: ikisi aynı anda attı ve kozalaklar yere düştü | şapkasını kütüğe koydu ve sırayla oynadılar
@tohum: chase-0156
@degisim: sakız -> kozalak
Chase ile Rubble sabah çok erken uyanıktı ve kamp yerinde oynuyordu. İkisi kozalakları eski bir kütüğün üstüne atıyordu. Ama ikisi hep aynı anda atıyordu. Kozalaklar havada birbirine çarptı ve yere düştü. "Hiçbiri kütükte kalmıyor!" dedi Rubble. Chase mavi şapkasını çıkardı ve kütüğün üstüne ters koydu. "Sırayla atalım, önce sen, Rubble," dedi Chase. Rubble attı ve kozalak şapkanın içine düştü. Sonra Chase attı ve onun kozalağı da içeri girdi. İkisi oyunu sırayla birkaç kez tekrarladı. Az sonra şapka doldu. "Kamp yerinde sırayla oynamak çok eğlenceli, Chase!" dedi Rubble.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sabah çok erken uyanıktı"
   - Cümle 1: «Chase ile Rubble sabah çok erken uyanıktı ve kamp yerinde oynuyordu.»
   - Açıklama: 'Çok erken uyanıktı' dilbilgisel olarak sakat; 'erkenden uyanmıştı' olmalı.
   - Açıklama: 'Erken uyanıktı' dilbilgisel değil; 'erken uyanmıştı' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase mavi şapkasını çıkardı"
   - Cümle 6: «Chase mavi şapkasını çıkardı ve kütüğün üstüne ters koydu.»
   - Açıklama: Sebep kozalakların havada çarpışması iken şapka adımı bu sebebe yönelmeyen fazladan bir çözüm ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0156` birebir aynı, `@degisim: sakız -> kozalak` (tutuyorsan), ardından `@onarim: 19b61d620818b76bd79d3176e68b2d0d01f75ae5`, sonra gövde.
