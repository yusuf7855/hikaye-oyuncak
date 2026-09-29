# Editör görevi (onarım): Chase, onarım partisi 6

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar6.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar6.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0007 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0007
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: sırayla oynamak
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kartopu', fiil 'gezmek', sıfat 'şık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: iki kartopu havada çarpıştı ve oyun bozuldu | şapkayı sıra işareti yapıp sırayla attılar
@tohum: chase-0007
Karlı dağda Chase ile Ryder geziyordu. Büyük bir ağaca kartopu atmaya başladılar. Ama ikisi aynı anda attı ve iki kartopu havada çarpıştı. Hiçbiri ağaca değmedi ve oyun bozuldu. Chase biraz düşündü ve mavi şapkasını çıkardı. "Şapkayı takan kartopu atar," dedi Chase. Sonra şapkayı Ryder'ın başına taktı. "Çok şık oldun, Ryder," dedi Chase. Ryder güldü ve bir kartopu attı. Kartopu ağaca tam değdi. Sonra şapka ve sıra Chase'e geçti. "Sırayla oynamak çok eğlenceli, Chase!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "iki kartopu havada çarpıştı"
   - Cümle 3: «Ama ikisi aynı anda attı ve iki kartopu havada çarpıştı.»
   - Açıklama: İki kartopunun havada bir kez çarpışıp oyunu bozması hem akla pek yatkın değil hem de önemsiz bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0007` birebir aynı, ardından `@onarim: 03d29d7d1f7b0165a1f5e97bd6c73116c3d3c14c`, sonra gövde.

### Hikâye 2: tohum chase-0012 (deneme 2 -> 3)

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
Dağda soğuk bir rüzgar esiyordu. Chase yumuşak kardan küçük bir pasta yapmıştı ve tepesine süs arıyordu. Ağaçtaki tek kozalak ise biraz yüksek bir dalda duruyordu. Chase önce ağaca tırmanmak istedi. Ama kurallara göre bu doğru değildi. Chase ön patileriyle ağacın gövdesine tutundu ve arka ayaklarının üstünde durdu. Sonra kozalağı ağzıyla yavaşça kopardı. Onu dikkatlice pastanın tepesine koydu. Kardan pasta artık çok güzel görünüyordu. Chase pastanın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama kurallara göre bu doğru değildi."
   - Cümle 5: «Ama kurallara göre bu doğru değildi.»
   - Açıklama: Hangi kural olduğu belli olmayan soyut bir kavram kullanılıyor.
   - Açıklama: 'Kurallara göre doğru değildi' soyut bir anlatım, küçük çocuğa uygun değil.
   - Açıklama: 'Kurallara göre doğru değil' soyut bir anlatım, çocuk için somut değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama kurallara göre bu doğru değildi"
   - Cümle 5: «Ama kurallara göre bu doğru değildi.»
   - Açıklama: Tırmanmayı yasaklayan kural sebepsiz beliriyor ve hangi kural olduğu hiç kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0012` birebir aynı, `@degisim: şapkalı -> yumuşak` (tutuyorsan), ardından `@onarim: 2d1ba64e20b330ee9ac24505f92c749cd6f8f53e`, sonra gövde.

### Hikâye 3: tohum chase-0013 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: ters duran teknenin altından bir ses geldi | arkadaşıyla tekneyi kaldırıp sesi yapan kabukları buldu
@tohum: chase-0013
@degisim: sağlıklı -> renkli
Bir sabah Chase ile Rubble kumsalda yürüyordu. Birden ters duran küçük bir tekneden "tık tık" diye bir ses geldi. Chase bu sesi çok merak etti. "Rubble, tekneyi birlikte kaldıralım mı?" diye sordu Chase. "Tabii, ben çok güçlüyüm," dedi Rubble. İkisi yardımlaştı ve tekneyi yavaşça kaldırdı. Altında renkli deniz kabukları vardı. Chase kabukları mavi şapkasına doldurdu ve şapkayı salladı. Şapkadan da aynı "tık tık" sesi geldi. Rubble kabuklara bakıp güldü. "Sesi kabuklar yapıyormuş, Chase!" dedi Rubble sevinçle.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ters duran küçük bir tekneden"
   - Cümle 2: «Birden ters duran küçük bir tekneden "tık tık" diye bir ses geldi.»
   - Açıklama: Kimsenin dokunmadığı teknenin altındaki kabukların kendiliğinden tık tık ses çıkarması akla yatkın bir sebep değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "tekneyi yavaşça kaldırdı"
   - Cümle 6: «İkisi yardımlaştı ve tekneyi yavaşça kaldırdı.»
   - Açıklama: Ağır bir tekneyi kaldırıp altındaki bilinmeyen sese bakmak taklit edilince tehlikeli olabilir.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Altında renkli deniz kabukları vardı"
   - Cümle 7: «Altında renkli deniz kabukları vardı.»
   - Açıklama: Ters teknenin altında duran kabukların kendiliğinden tık tık ses çıkarması akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0013` birebir aynı, `@degisim: sağlıklı -> renkli` (tutuyorsan), ardından `@onarim: 86f0ec98da147c966429deca4a8d8e42db9a3624`, sonra gövde.

### Hikâye 4: tohum chase-0015 (deneme 2 -> 3)

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
@plan: yağmur başladı ama havlular ipte asılıydı | havluları ipten aldı ve poşete koyup paketledi
@tohum: chase-0015
@degisim: tedbirli -> büyük
Denizden serin bir rüzgar esiyordu. Chase havlularını kumsala büyük bir poşet içinde getirmişti. Onları bir çamaşır ipine asmıştı. Birden yağmur başladı ve Chase hemen ipe koştu. Kurallara göre yağmurda eşyalar hemen toplanırdı. Chase havluları ipten aldı. Onları katladı, poşete koydu ve sıkıca paketledi. Poşete hiç yağmur girmedi. Az sonra yağmur dindi ve güneş çıktı. Chase poşeti açtı; havlular kuru kalmıştı. Chase kuru bir havluyu kuma serdi ve üstüne mutlu mutlu uzandı.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Onları bir çamaşır ipine asmıştı.»
   - Açıklama: Sorun (yağmur) ilk üç cümlede değil, dördüncü cümlede söyleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Onları bir çamaşır ipine asmıştı"
   - Cümle 3: «Onları bir çamaşır ipine asmıştı.»
   - Açıklama: Kumsalda çamaşır ipi ve havluların neden asıldığı sebepsiz kuruluyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden yağmur başladı ve Chase hemen ipe koştu"
   - Cümle 4: «Birden yağmur başladı ve Chase hemen ipe koştu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara göre yağmurda eşyalar hemen toplanırdı"
   - Cümle 5: «Kurallara göre yağmurda eşyalar hemen toplanırdı.»
   - Açıklama: 'Kurallara göre' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Kurallara göre' soyut bir ifade ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0015` birebir aynı, `@degisim: tedbirli -> büyük` (tutuyorsan), ardından `@onarim: 9e6d2147e3aecd9ba51eda44b84f633ef71b95a5`, sonra gövde.

### Hikâye 5: tohum chase-0016 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0016
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'pilav', fiil 'kilitlemek', sıfat 'aceleci'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: çanta kilitli değildi ve yemek kutusu karda kayboldu | burnuyla pilav kokusunu izleyip kutuyu buldu
@tohum: chase-0016
@degisim: aceleci -> büyük
Karlı dağda Chase ile Rubble kartopu oynuyordu. Ama Rubble'ın çantası kilitli değildi ve yemek kutusu karın içine düştü. Rubble çok üzüldü, çünkü kutuda en sevdiği pilav vardı. "Chase, kutumu bulabilir misin?" diye sordu Rubble. Chase burnunu kara yaklaştırdı ve dikkatle kokladı. Karın altından pilav kokusu geliyordu. Chase kokuyu izledi ve büyük bir kayanın yanında durdu. Patileriyle karı eşeledi ve yemek kutusunu çıkardı. "Teşekkürler, Chase, pilavım burada!" dedi Rubble sevinçle. Rubble bundan sonra koşmadan önce çantasını hep kilitledi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çantası kilitli değildi"
   - Cümle 2: «Ama Rubble'ın çantası kilitli değildi ve yemek kutusu karın içine düştü.»
   - Açıklama: Çocuk çantası kilitlenmez; 'kapalı değildi' anlamında yanlış kelime.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Rubble bundan sonra koşmadan önce çantasını hep kilitledi"
   - Cümle 10: «Rubble bundan sonra koşmadan önce çantasını hep kilitledi.»
   - Açıklama: Ders yaşanan olaydan çıkmıyor; hikayede koşma yok, kartopu oynanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0016` birebir aynı, `@degisim: aceleci -> büyük` (tutuyorsan), ardından `@onarim: 1c6b6ad0c414e3a242cf3df39454ae583a569194`, sonra gövde.

### Hikâye 6: tohum chase-0017 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Ryder
@tohum: chase-0017
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kumbara', fiil 'yuvarlamak', sıfat 'tuhaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | ev | Ryder
@plan: sepet düştü ve elmalar uzun otların arasında kayboldu | burnuyla kokuyu izleyip elmaları buldu ve yuvarladı
@tohum: chase-0017
@degisim: kumbara -> elma
Bir sabah Chase kulübesinin önünde oturuyordu. Ryder bütün köpekler için bir sepet elma getirdi. Ama sepet elinden düştü ve elmalar uzun otların arasına kaçtı. Ryder otlara baktı ama hiçbir elma göremedi. "Çok tuhaf, elmalar nereye gitti?" diye sordu Ryder. Chase burnunu otlara yaklaştırdı ve dikkatle kokladı. Tatlı elma kokusunu izledi ve elmaları otların arasında tek tek buldu. Sonra onları burnuyla Ryder'a doğru yuvarladı. Ryder elmaları sepete koydu ve güldü. "Teşekkürler, Chase, şimdi herkese birer elma var!" dedi Ryder.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elmalar uzun otların arasına kaçtı"
   - Cümle 3: «Ama sepet elinden düştü ve elmalar uzun otların arasına kaçtı.»
   - Açıklama: Elmalar kaçmaz; fiil öznesine uymuyor, 'yuvarlandı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "otların arasına kaçtı"
   - Cümle 3: «Ama sepet elinden düştü ve elmalar uzun otların arasına kaçtı.»
   - Açıklama: Elmalar kaçmaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0017` birebir aynı, `@degisim: kumbara -> elma` (tutuyorsan), ardından `@onarim: d03224a59ce7e6aa1d33c60ca1d6c469dfee160b`, sonra gövde.

### Hikâye 7: tohum chase-0019 (deneme 2 -> 3)

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
Dalgalar kumsala hafifçe vuruyordu. Chase kumsalda koşuyor, Marshall ise rengarenk kovasını papatyalarla dolduruyordu. Chase önüne bakmadı ve kovaya çarptı. Bütün papatyalar kuma döküldü. "Eyvah, papatyalar!" dedi Marshall üzgün bir sesle. Chase kuralı hatırladı: hata yapınca özür dilemek gerekiyordu. "Özür dilerim, Marshall, sana bakmadan koştum," dedi Chase. Sonra papatyaları tek tek topladı ve kovayı yeniden doldurdu. "Sorun değil, Chase, teşekkür ederim," dedi Marshall. Marshall dolu kovasını mutlu mutlu taşıdı. Chase bundan sonra kumsalda koşarken hep önüne baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hata yapınca özür dilemek gerekiyordu"
   - Cümle 6: «Chase kuralı hatırladı: hata yapınca özür dilemek gerekiyordu.»
   - Açıklama: 'Kural' ve 'hata yapınca özür dilemek gerekiyordu' soyut bir kural anlatımı, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0019` birebir aynı, `@degisim: yüklemek -> doldurmak` (tutuyorsan), ardından `@onarim: 6e994a423a89cef5afb4905505a7d1849cd5077a`, sonra gövde.

### Hikâye 8: tohum chase-0021 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0021
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'taş', fiil 'dolmak', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kuru kumdan yapılan kale hemen dağıldı | ıslak kumu burnuyla buldu ve kaleyi onunla yaptı
@tohum: chase-0021
Bir sabah Chase kumsalda ilk kez kumdan kale yapmayı denedi. Kovası kuru kumla doldu ve Chase onu ters çevirdi. Ama kuru kum hemen dağıldı ve kale yıkıldı. Chase burnunu kuma yaklaştırdı ve dikkatle kokladı. Su kenarındaki kum ıslak ve tuzlu kokuyordu. Chase kovayı oradaki ıslak kumla doldurdu. Kovayı ters çevirdi ve yavaşça kaldırdı. Bu kez kale hiç yıkılmadı. Kale güneşte çok güzel görünüyordu. Chase kalenin üstüne değişik renklerde küçük taşlar dizdi. Chase çok sevindi, çünkü ilk kum kalesini kendi başına yapmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kovası kuru kumla doldu"
   - Cümle 2: «Kovası kuru kumla doldu ve Chase onu ters çevirdi.»
   - Açıklama: Kovayı Chase doldurduğu halde fiil kova kendiliğinden dolmuş gibi kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0021` birebir aynı, ardından `@onarim: 6d6e084976e8f172f16d0ab6fcf1b1ccc0afb62a`, sonra gövde.

### Hikâye 9: tohum chase-0022 (deneme 2 -> 3)

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
@plan: oyuncak ayakkabı karın altında kayboldu | burnuyla kokusunu alıp karı kazdı
@tohum: chase-0022
@degisim: saygılı -> yumuşak
Karlı dağda yumuşak kar yağıyordu. Chase kırmızı oyuncak ayakkabısını ağzıyla havaya atıp yakalıyordu. Ama ayakkabı uzağa düştü ve yeni yağan kar onu örttü. Chase oraya koştu ama ayakkabıyı göremedi. Her yer bembeyazdı. Sonra burnunu yere yaklaştırdı ve oyuncağının kokusunu aldı. Koku küçük bir çukurdan geliyordu. Chase patileriyle orayı hızlı hızlı kazdı. Kırmızı ayakkabı sonunda göründü. Ucu biraz ezilmişti ve Chase onu dişleriyle yavaşça düzeltti. Chase çok sevindi, çünkü en sevdiği oyuncağını bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yeni yağan kar onu örttü"
   - Cümle 3: «Ama ayakkabı uzağa düştü ve yeni yağan kar onu örttü.»
   - Açıklama: Yağan karın düşen ayakkabıyı anında örtmesi akla yatkın bir sebep değil.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ucu biraz ezilmişti ve Chase onu dişleriyle yavaşça düzeltti"
   - Cümle 10: «Ucu biraz ezilmişti ve Chase onu dişleriyle yavaşça düzeltti.»
   - Açıklama: Ayakkabı bulunduktan sonra ezik uç olarak ikinci bir küçük sorun ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ucu biraz ezilmişti ve Chase"
   - Cümle 10: «Ucu biraz ezilmişti ve Chase onu dişleriyle yavaşça düzeltti.»
   - Açıklama: Ezilme ve düzeltme sorunla ilgisiz, sonradan eklenen işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0022` birebir aynı, `@degisim: saygılı -> yumuşak` (tutuyorsan), ardından `@onarim: 6f45eb75ffbfc00439670f5d61d5a55682ef8a88`, sonra gövde.

### Hikâye 10: tohum chase-0024 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0024
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'muffin', fiil 'toplanmak', sıfat 'çilekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: rüzgar sürpriz kutusunu çalıların arasına düşürdü | burnuyla çilek kokusunu alıp kutuyu buldu
@tohum: chase-0024
@degisim: toplanmak -> saklamak
Parkta hafif bir rüzgar esiyordu. Chase, Skye için çilekli bir muffini kutuya koyup saklamıştı. Ama rüzgar kutuyu düşürdü ve kutu çalıların arasında kayboldu. Chase çalılara baktı ama kutuyu göremedi. Sonra burnunu yere yaklaştırdı ve tatlı bir çilek kokusu aldı. Büyük bir çalının altına gitti ve kutuyu orada buldu. Birazdan Skye parka geldi. "Skye, bu senin için!" dedi Chase. Skye kutuyu açtı ve gülümsedi. "Çilekli muffin, çok teşekkürler!" dedi Skye. Chase çok sevindi, çünkü sürprizini tam zamanında bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çilekli bir muffini kutuya"
   - Cümle 2: «Chase, Skye için çilekli bir muffini kutuya koyup saklamıştı.»
   - Açıklama: 'Muffin' yabancı bir kelime ve 3 yaşındaki çocuk bilmeyebilir.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama rüzgar kutuyu düşürdü"
   - Cümle 3: «Ama rüzgar kutuyu düşürdü ve kutu çalıların arasında kayboldu.»
   - Açıklama: Hafif bir rüzgarın içinde muffin olan saklı kutuyu düşürüp çalılara götürmesi akla yatkın değil.
   - Açıklama: Kutunun nerede durduğu söylenmiyor ve hafif bir rüzgarın içi muffinli kutuyu düşürmesi sebep olarak zayıf kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0024` birebir aynı, `@degisim: toplanmak -> saklamak` (tutuyorsan), ardından `@onarim: 587b9be9eecc3e50889d7c3125f19eb0e1188c9a`, sonra gövde.

### Hikâye 11: tohum chase-0027 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0027
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'mobilya', fiil 'uzaklaştırmak', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | -
@plan: kemik büyük bir yaprak yığınına girdi | burnuyla kemiğin kokusunu alıp yaprakları kazdı
@tohum: chase-0027
@degisim: mobilya -> kemik
Ormandaki kamp yerinde Chase nefis bir kemikle oynuyordu. Kemiği burnuyla itip uzaklaştırıyor, sonra koşup yakalıyordu. Ama bir kez kemik yuvarlandı ve büyük bir yaprak yığınına girdi. Chase yaprakların arasına baktı ama kemiği göremedi. Yaprakların hepsi birbirine benziyordu. Chase burnunu yığına soktu ve kemiğin kokusunu aldı. Sonra patileriyle yaprakları kazdı ve kemiği buldu. Kemik çıkınca Chase'in burnunun üstünde sarı bir yaprak kaldı. Chase başını salladı ve yaprak uçup gitti. Sonra Chase kemiğiyle oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase nefis bir kemikle oynuyordu"
   - Cümle 1: «Ormandaki kamp yerinde Chase nefis bir kemikle oynuyordu.»
   - Açıklama: 'Nefis' yiyecek için kullanılır, oynanan kemiğe uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "patileriyle yaprakları kazdı ve"
   - Cümle 7: «Sonra patileriyle yaprakları kazdı ve kemiği buldu.»
   - Açıklama: Yapraklar kazılmaz; 'eşeledi' ya da 'yaprakları kenara itti' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "burnunun üstünde sarı bir yaprak kaldı"
   - Cümle 8: «Kemik çıkınca Chase'in burnunun üstünde sarı bir yaprak kaldı.»
   - Açıklama: Burundaki sarı yaprak olayı sorunla ve çözümle ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Sorun çözüldükten sonra eklenen yaprak olayı hiçbir işe yaramayan ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase'in burnunun üstünde sarı bir yaprak kaldı"
   - Cümle 8: «Kemik çıkınca Chase'in burnunun üstünde sarı bir yaprak kaldı.»
   - Açıklama: Sorun çözüldükten sonra gelen sarı yaprak ayrıntısı hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0027` birebir aynı, `@degisim: mobilya -> kemik` (tutuyorsan), ardından `@onarim: 942447f36472cb219d055abef57f31a6463bb6c8`, sonra gövde.

### Hikâye 12: tohum chase-0028 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar şapkayı salıncağın üstüne uçurdu | salıncağı yavaşça çekip şapkayı düşürdü
@tohum: chase-0028
@degisim: dondurma -> yaprak
Rüzgar esiyordu ve parkta sarı yapraklar uçuşuyordu. Chase yaprak yığınına zıplıyor ve çıtır sesler çıkarıyordu. Birden güçlü bir rüzgar esti ve Chase'in mavi şapkasını uçurdu. Şapka salıncağın tahta oturağına düştü. Salıncak sallanıyordu ve Chase şapkaya uzanamadı. Chase salıncağın ipini ağzıyla tuttu ve yavaşça çekti. Salıncak durdu ve biraz eğildi. Şapka kaydı ve yere düştü. Chase şapkasını hemen başına taktı. Sonra yine yaprak yığınına koştu. Chase yaprak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Salıncak sallanıyordu ve Chase şapkaya uzanamadı"
   - Cümle 5: «Salıncak sallanıyordu ve Chase şapkaya uzanamadı.»
   - Açıklama: Chase sallanan oturaktaki şapkaya uzanamıyor ama aynı sallanan salıncağın ipini ağzıyla tutabiliyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase salıncağın ipini ağzıyla tuttu"
   - Cümle 6: «Chase salıncağın ipini ağzıyla tuttu ve yavaşça çekti.»
   - Açıklama: Sallanan bir salıncağı ipinden ağızla tutup durdurmak çocuğun taklit edince çarpılabileceği bir davranış.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "salıncağın ipini ağzıyla tuttu"
   - Cümle 6: «Chase salıncağın ipini ağzıyla tuttu ve yavaşça çekti.»
   - Açıklama: Sallanan salıncağa yaklaşıp ipinden tutmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0028` birebir aynı, `@degisim: dondurma -> yaprak` (tutuyorsan), ardından `@onarim: dcf7133dc7b36e12ed8c19203b9049c2076cc93a`, sonra gövde.
