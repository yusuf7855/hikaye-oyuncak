# Editör görevi (onarım): Chase, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Rubble
@tohum: chase-0116
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: paylaşmak
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'boya', fiil 'inanmak', sıfat 'sakar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | ev | Rubble
@plan: mama kabı boştu ve bisküvi kutusu kayboldu | kokusunu alıp kutuyu buldu ve paylaştı
@tohum: chase-0116
@degisim: sakar -> boş
Chase kulübesinin önünde Rubble ile oynuyordu. Birden Rubble'ın karnı guruldadı ve mama kabına koştu. Kap boştu ve bisküvi kutusu da yerinde yoktu. Kulübeler yeni boyanmıştı ve her yer boya kokuyordu. Ama Chase havayı dikkatle kokladı. Boyanın arasında tatlı bir bisküvi kokusu buldu. Bu kokunun peşinden kulenin kapısına yürüdü. Rubble kutunun orada olduğuna inanmadı ama yine de Chase ile gitti. Kutu gerçekten kapının arkasındaydı. İçinde tek bir büyük bisküvi kalmıştı. Chase bisküviyi ikiye böldü ve yarısını Rubble'a verdi. İkisi bisküvilerini yedi ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Rubble'ın karnı guruldadı ve mama kabına koştu"
   - Cümle 2: «Birden Rubble'ın karnı guruldadı ve mama kabına koştu.»
   - Açıklama: Özne kayıyor; dilbilgisel olarak koşan 'karnı' oluyor, 'Rubble'ın karnı guruldadı ve Rubble mama kabına koştu' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "karnı guruldadı ve mama kabına koştu"
   - Cümle 2: «Birden Rubble'ın karnı guruldadı ve mama kabına koştu.»
   - Açıklama: İkinci fiilin öznesi 'karnı' olarak kalıyor; özne uyumu bozuk.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bisküvi kutusu da yerinde yoktu"
   - Cümle 3: «Kap boştu ve bisküvi kutusu da yerinde yoktu.»
   - Açıklama: Kutunun neden kaybolup kulenin kapısının arkasına gittiği hiç söylenmiyor.
   - Açıklama: Kutunun neden kaybolduğu ve neden kulenin kapısının arkasında olduğu hiç söylenmiyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Boyanın arasında tatlı bir bisküvi kokusu buldu"
   - Cümle 6: «Boyanın arasında tatlı bir bisküvi kokusu buldu.»
   - Açıklama: Koku boyanın arasında bulunmaz, 'boya kokusunun arasında' olmalı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Boyanın arasında tatlı bir"
   - Cümle 6: «Boyanın arasında tatlı bir bisküvi kokusu buldu.»
   - Açıklama: Koku boyanın arasında değil boya kokusunun arasında bulunur; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0116` birebir aynı, `@degisim: sakar -> boş` (tutuyorsan), ardından `@onarim: 46a44c0f3c78e1bc8265de38d1c4313147072e60`, sonra gövde.

### Hikâye 2: tohum chase-0117 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0117
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'nota', fiil 'karşılaşmak', sıfat 'boş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: havuç derin karın içinde kayboldu | kokusunu bulup kazmak için yardım istedi
@tohum: chase-0117
@degisim: nota -> havuç
Karlı dağda Chase ile Ryder karşılaştı. İkisi birlikte kardan bir köpek yaptı. Ryder ona burun olarak havuç takarken havuç elinden kaydı. Havuç derin karın içinde kayboldu ve kardan köpeğin yüzü boş kaldı. Chase burnunu karın üstüne yaklaştırdı ve kokladı. Havucun kokusu küçük bir kayanın yanından geliyordu. Ama orada kar çok sertti ve Chase havucu çıkaramadı. "Ryder, havuç burada, yardım eder misin?" diye sordu Chase. "Tabii, Chase," dedi Ryder. İkisi sert karı birlikte kazdı. Chase havucu ağzıyla aldı ve Ryder'a verdi. Ryder onu yeniden yerine taktı. Sonra ikisi kardan köpeğin etrafında mutlu mutlu koşup oynadı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kokusunu bulup kazmak için"
   - Cümle 0 (plan satırı): «havuç derin karın içinde kayboldu | kokusunu bulup kazmak için yardım istedi»
   - Açıklama: Koku bulunmaz, alınır; plan satırında kelime yanlış kullanılmış.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "orada kar çok sertti ve Chase havucu çıkaramadı"
   - Cümle 7: «Ama orada kar çok sertti ve Chase havucu çıkaramadı.»
   - Açıklama: Havuç derin ve yumuşak karın içine batıp kayboldu ama aynı yerde kar kazılamayacak kadar sert deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0117` birebir aynı, `@degisim: nota -> havuç` (tutuyorsan), ardından `@onarim: 8a5ee782e4403fea053ecadeef49003509a48c0c`, sonra gövde.

### Hikâye 3: tohum chase-0118 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Rubble
@tohum: chase-0118
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yeni bir şeyi denemek
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'sebze', fiil 'duymak', sıfat 'çikolatalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Rubble
@plan: sebze turtasını hiç denememişti ve çekiniyordu | önce kokladı ve sevdiği peyniri bulunca tattı
@tohum: chase-0118
Parkta kuşlar ötüyordu ve Chase ile Rubble bankta oturuyordu. Rubble çantasından bir sebze turtası ve çikolatalı bir kek çıkardı. Chase sebze turtasını hiç denememişti ve ondan biraz çekiniyordu. "Chase, bu turta çok güzel, bir dene," dedi Rubble. Chase önce turtayı burnuyla dikkatle kokladı. İçinden havuç ve peynir kokusu geldi. "Peyniri çok severim," dedi Chase ve küçük bir ısırık aldı. Turta yumuşak ve sıcaktı. "Bu turta çok lezzetli!" dedi Chase. Rubble bunu duyunca sevinçle güldü. Sonra ikisi kekten de birer parça yedi. Karınları doyunca ikisi parkta mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çikolatalı bir kek çıkardı"
   - Cümle 2: «Rubble çantasından bir sebze turtası ve çikolatalı bir kek çıkardı.»
   - Açıklama: Kek sorunla ilgisiz, işlevsiz bir ayrıntı olarak kuruluyor ve yalnız sonda yeniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ikisi kekten de birer parça yedi"
   - Cümle 11: «Sonra ikisi kekten de birer parça yedi.»
   - Açıklama: Köpekler çikolatalı kek yiyor; çocuk köpeğine çikolata vermeyi taklit edebilir ve bu köpek için tehlikelidir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0118` birebir aynı, ardından `@onarim: 5b37d9fe7429f26f17216dcea46e03469a168ab5`, sonra gövde.

### Hikâye 4: tohum chase-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0122
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'torba', fiil 'örmek', sıfat 'sulu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: yeni kar izleri kapattı ve torba kayboldu | elmaların kokusunu alıp torbayı buldu
@tohum: chase-0122
Karlı dağda Chase ile Ryder karla üç küçük duvar ördü. Oyun için Ryder sulu elmalarla dolu bir torbayı bir duvarın arkasına sakladı. Ama birden kar yağdı, izler kapandı ve Ryder torbanın yerini unuttu. "Chase, torba hangi duvarın arkasında, bilmiyorum!" dedi Ryder. Chase burnunu karın üstünde gezdirdi. İkinci duvarın arkasında tatlı bir elma kokusu aldı. Patileriyle karı biraz kazdı ve torbayı buldu. Ryder torbayı açtı ve Chase'e kocaman bir elma verdi. Chase elmayı mutlu mutlu yedi. "Teşekkürler, Chase, oyunumuzu sen kurtardın!" dedi Ryder.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "izler kapandı ve Ryder torbanın yerini unuttu"
   - Cümle 3: «Ama birden kar yağdı, izler kapandı ve Ryder torbanın yerini unuttu.»
   - Açıklama: Ryder torbayı az önce kendisi sakladı ve yalnız üç duvar var; unutma sebebi akla yatkın değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ryder torbanın yerini unuttu"
   - Cümle 3: «Ama birden kar yağdı, izler kapandı ve Ryder torbanın yerini unuttu.»
   - Açıklama: Kendi sakladığı torbanın yalnız üç duvardan hangisinin arkasında olduğunu hemen unutması akla yatkın değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oyunumuzu sen kurtardın"
   - Cümle 10: «"Teşekkürler, Chase, oyunumuzu sen kurtardın!" dedi Ryder.»
   - Açıklama: 'oyunu kurtarmak' mecazdır, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Oyunu kurtarmak' mecazlı bir anlatım, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0122` birebir aynı, ardından `@onarim: 2708522b6472e570ae9c0bd2e4e6697105950f84`, sonra gövde.

### Hikâye 5: tohum chase-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0124
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'erik', fiil 'uzamak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: torba yırtıldı ve erikler uzamış otlara yuvarlandı | şapkasını tutması için arkadaşından yardım istedi
@tohum: chase-0124
Bir sabah Chase ile Skye parkta piknik yapıyordu. Yanlarında tuzlu bir simit ve bir torba erik vardı. Birden torba yırtıldı ve erikler uzamış otların arasına yuvarlandı. Chase erikleri buldu ama taşıyacak bir yer yoktu. Hemen mavi şapkasını çıkardı ve ters çevirdi. "Skye, şapkamı tutar mısın?" diye sordu Chase. "Tabii," dedi Skye ve şapkayı sıkıca tuttu. Chase erikleri ağzıyla tek tek şapkaya koydu. Sonunda bütün erikler şapkanın içindeydi. İkisi simidi ve erikleri keyifle paylaştı. Chase çok mutlu oldu, çünkü Skye'dan yardım istemiş ve pikniği kurtarmıştı.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "torba yırtıldı ve erikler uzamış otlara yuvarlandı"
   - Cümle 0 (plan satırı): «torba yırtıldı ve erikler uzamış otlara yuvarlandı | şapkasını tutması için arkadaşından yardım istedi»
   - Açıklama: Gövdede erikler otlarda hemen bulunuyor; çözülen asıl sorun eriklerin taşınacak bir yerinin olmaması, plan bunu söylemiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama taşıyacak bir yer"
   - Cümle 4: «Chase erikleri buldu ama taşıyacak bir yer yoktu.»
   - Açıklama: 'taşıyacak bir yer' yanlış; 'koyacak bir yer' ya da 'taşıyacak bir şey' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "taşıyacak bir yer yoktu"
   - Cümle 4: «Chase erikleri buldu ama taşıyacak bir yer yoktu.»
   - Açıklama: 'Yer' kap anlamında yanlış kullanılmış; 'taşıyacak bir şey' olmalı.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Chase erikleri buldu ama taşıyacak bir yer yoktu"
   - Cümle 4: «Chase erikleri buldu ama taşıyacak bir yer yoktu.»
   - Açıklama: Otlara yuvarlanan erikler sorunundan sonra ikinci bir sorun olan taşıma sorunu ortaya çıkıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve pikniği kurtarmıştı"
   - Cümle 11: «Chase çok mutlu oldu, çünkü Skye'dan yardım istemiş ve pikniği kurtarmıştı.»
   - Açıklama: 'pikniği kurtarmak' mecazdır, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0124` birebir aynı, ardından `@onarim: fd3e918a9d7b263c497dc51871345ef1968929ec`, sonra gövde.

### Hikâye 6: tohum chase-0125 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Marshall
@tohum: chase-0125
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'eşarp', fiil 'dolaşmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Marshall
@plan: rüzgar şapkayı uçurdu ve şapka yine uçabilirdi | arkadaşından eşarp istedi ve şapkasını bağladı
@tohum: chase-0125
Rüzgar esiyordu ve gökyüzü bulutlarla kapalıydı. Chase ile Marshall karlı dağda dolaşıyordu. Birden rüzgar Chase'in mavi şapkasını başından uçurdu. Chase şapkayı karın üstünden hemen aldı. Ama rüzgar çok güçlüydü ve şapka yine uçabilirdi. "Marshall, şapkamı tutacak bir şeyin var mı?" diye sordu Chase. Marshall boynundaki kırmızı eşarbı çıkardı ve Chase'e verdi. Chase şapkasını taktı ve eşarbı üstünden sıkıca bağladı. Rüzgar yine esti ama şapka yerinden kıpırdamadı. İkisi karda neşeyle yürümeye devam etti. Chase bundan sonra bir sorun olunca hemen arkadaşından yardım istedi.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Chase şapkayı karın üstünden hemen aldı"
   - Cümle 4: «Chase şapkayı karın üstünden hemen aldı.»
   - Açıklama: Asıl sorun hemen kendiliğinden çözülüyor, kalan sorun yalnız şapkanın yine uçabileceği ihtimali.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar çok güçlüydü ve şapka yine uçabilirdi"
   - Cümle 5: «Ama rüzgar çok güçlüydü ve şapka yine uçabilirdi.»
   - Açıklama: Şapka hemen geri alınıyor; asıl sorun (şapkanın yine uçabilmesi) ancak 5. cümlede söyleniyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Marshall boynundaki kırmızı eşarbı"
   - Cümle 7: «Marshall boynundaki kırmızı eşarbı çıkardı ve Chase'e verdi.»
   - Açıklama: Kartta Marshall'ın kırmızı eşarbı gibi bir eşya yok; kapalı dünyaya eşya ekleniyor.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Marshall boynundaki kırmızı eşarbı çıkardı"
   - Cümle 7: «Marshall boynundaki kırmızı eşarbı çıkardı ve Chase'e verdi.»
   - Açıklama: Kartın yanlar bölümünde Marshall'ın eşarbı yok; kartta olmayan bir eşya ekleniyor.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Marshall boynundaki kırmızı eşarbı"
   - Cümle 7: «Marshall boynundaki kırmızı eşarbı çıkardı ve Chase'e verdi.»
   - Açıklama: Diziyi izleyen çocuk Marshall'ı eşarpla tanımaz; yanlış bilgi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0125` birebir aynı, ardından `@onarim: 8ffae338709376b95c66aff8cae339441e12e14a`, sonra gövde.

### Hikâye 7: tohum chase-0128 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0128
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'meşe', fiil 'yatmak', sıfat 'kibar'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: karlı dağda bir çiçek kokusu geldi ama çiçek görünmedi | burnuyla kokunun peşinden gidip çiçeği buldu
@tohum: chase-0128
Rüzgar hafifçe esiyordu ve karlı dağda güneş parlıyordu. Chase ile Skye karda kartopu oynuyordu. Birden Chase hafif bir çiçek kokusu aldı ama etrafta hiç çiçek yoktu. "Bu koku nereden geliyor?" diye sordu Skye. Chase burnunu havaya kaldırdı ve derin derin kokladı. Koku büyük bir meşe ağacının dibinden geliyordu. İkisi ağaca doğru yavaşça yürüdü. Ağacın dibinde kar biraz erimişti. Orada küçük beyaz bir çiçek açmıştı. Chase karın üstüne yattı ve çiçeğe dikkatle baktı. "Buradan uzak duralım, çiçek çok küçük," dedi Skye kibar bir sesle. Chase başını salladı. İkisi çiçekten biraz uzakta kartopu oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden Chase hafif bir çiçek kokusu aldı"
   - Cümle 3: «Birden Chase hafif bir çiçek kokusu aldı ama etrafta hiç çiçek yoktu.»
   - Açıklama: Görünmeyen bir çiçeğin kokusu gerçek bir sorun değil; kimse bir şey kaybetmiyor ya da zarar görmüyor, çocuğun önemseyeceği bir dert yok.
2. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "Bu koku nereden geliyor?"
   - Cümle 4: «"Bu koku nereden geliyor?" diye sordu Skye.»
   - Açıklama: Kokuyu Chase aldığı halde soruyu Skye soruyor; konuşan kişi yanlış görünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0128` birebir aynı, ardından `@onarim: 3012a136de8b17cbc5597d92ec064c3c2446ec7f`, sonra gövde.

### Hikâye 8: tohum chase-0129 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Rubble
@tohum: chase-0129
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'dosya', fiil 'öğretmek', sıfat 'sıcak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Rubble
@plan: top suya düştü ve dalgalarla sallandı | kurallara uydu, suya girmedi ve yardım istedi
@tohum: chase-0129
@degisim: dosya -> kürek
Chase sıcak kumsalda Rubble'a yeni bir top oyunu öğretiyordu. Chase topa patisiyle vurdu ama top çok uzağa gitti. Top suya düştü ve dalgalarla sallanmaya başladı. Chase kurallara uydu ve suya tek başına girmedi. Kıyıda durdu ve Rubble'dan yardım istedi. Rubble hemen sarı küreğini getirdi. Chase küreği kıyıdan suya doğru uzattı. Kürek topa değdi ve Chase topu yavaşça kıyıya çekti. Rubble sevinçle zıpladı. Chase çok sevindi, çünkü top oyununu Rubble'a öğretmeye devam edebilirdi.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "top çok uzağa gitti"
   - Cümle 2: «Chase topa patisiyle vurdu ama top çok uzağa gitti.»
   - Açıklama: Top çok uzağa gitmişken Chase onu kıyıdan bir kürekle çekebiliyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase kurallara uydu ve suya tek başına girmedi"
   - Cümle 4: «Chase kurallara uydu ve suya tek başına girmedi.»
   - Açıklama: 'Tek başına' vurgusu birlikteyken dalgalı suya girmenin uygun olduğunu ima ediyor ve çocuk dalgadaki topa uzanmayı taklit edebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 4: «Chase kurallara uydu ve suya tek başına girmedi.»
   - Açıklama: Hangi kural olduğu belirtilmeden soyut 'kurallara uydu' kavramı kullanılıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase küreği kıyıdan suya doğru uzattı"
   - Cümle 7: «Chase küreği kıyıdan suya doğru uzattı.»
   - Açıklama: Dalgalardaki topa kıyıdan uzanmak ve 'tek başına girmedi' demek çocuğun taklit edebileceği bir su kenarı davranışı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0129` birebir aynı, `@degisim: dosya -> kürek` (tutuyorsan), ardından `@onarim: 637cd1c943021ec4c9e73de12aace641a350a639`, sonra gövde.

### Hikâye 9: tohum chase-0130 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0130
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kraker', fiil 'katılmak', sıfat 'yalnız'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: yağmur başladı ve yiyecekler açıkta kaldı | mavi şapkasını çıkarıp üstlerine kapattı
@tohum: chase-0130
Chase ormandaki kamp yerine geldi. Skye bir kütüğün üstünde yalnız oturuyordu ve kraker yiyordu. Birden yağmur başladı ama krakerlerin üstü açıktı. Skye krakerleri koruyacak bir şey bulamadı. Chase hemen mavi şapkasını çıkardı. Şapkayı onların üstüne kapattı. İkisi kütüğün yanında biraz bekledi. Kısa bir süre sonra yağmur dindi. Chase şapkayı kaldırdı ve krakerler kuruydu. Skye sevinçle bir kraker Chase'e uzattı. Chase de ona katıldı ve ikisi krakerleri paylaştı. Chase bundan sonra arkadaşlarına hep böyle yardım etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase de ona katıldı"
   - Cümle 11: «Chase de ona katıldı ve ikisi krakerleri paylaştı.»
   - Açıklama: Kendisine kraker uzatılan Chase için 'ona katıldı' anlamca uygun değil.
   - Açıklama: Skye kraker uzatıyor, 'ona katıldı' fiili bu durumda anlamca uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0130` birebir aynı, ardından `@onarim: bb5624ff25dbd758aad08438a5b73c0938740387`, sonra gövde.

### Hikâye 10: tohum chase-0132 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Marshall
@tohum: chase-0132
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: yeni bir şeyi denemek
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'boru', fiil 'dokunmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Marshall
@plan: havuç yere düştü ve kirlendi | kurallara uydu ve havucu yıkayıp tattı
@tohum: chase-0132
Kulübenin önünde güneş parlıyordu. Marshall denemesi için Chase'e turuncu bir havuç getirdi. Ama Marshall tökezledi ve havuç toprağa düştü. Chase havuca burnuyla dokundu ve toprağı gördü. Chase kurallara uydu ve kirli havucu yemedi. "Marshall, suyu açar mısın?" diye sordu Chase. Marshall kulübenin yanındaki su borusunu açtı. Chase havucu suyun altında tuttu ve yıkadı. Havuç tertemiz oldu. Chase ilk ısırığı aldı ve "Çok tatlı!" dedi. Chase çok sevindi, çünkü yeni bir yiyeceği denemişti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Marshall denemesi için Chase'e"
   - Cümle 2: «Marshall denemesi için Chase'e turuncu bir havuç getirdi.»
   - Açıklama: 'Denemesi için' kimin denemesi olduğunu belirsiz bırakan bozuk bir yapı; 'Chase denesin diye' olmalı.
   - Açıklama: 'denemesi' iyelik eki kimi gösterdiği belirsiz ve tamlama bozuk; 'Chase denesin diye' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 5: «Chase kurallara uydu ve kirli havucu yemedi.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 5: «Chase kurallara uydu ve kirli havucu yemedi.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yanındaki su borusunu açtı"
   - Cümle 7: «Marshall kulübenin yanındaki su borusunu açtı.»
   - Açıklama: Su borusu açılmaz; musluk ya da hortum açılır.
   - Açıklama: Boru açılmaz, musluk açılır; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0132` birebir aynı, ardından `@onarim: 0fd10338ed90520abe17061abe6d9d36baad7c03`, sonra gövde.

### Hikâye 11: tohum chase-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0133
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'yatak', fiil 'havlamak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: rüzgar döndü ve uçurtmanın ipi karmakarışık oldu | kurallara uydu ve düğümleri yavaşça açtı
@tohum: chase-0133
@degisim: yatak -> uçurtma
Rüzgar hafifçe esiyordu. Chase kumsalda kırmızı bir uçurtma uçuruyordu. Birden rüzgar döndü ve uçurtmanın ipi karmakarışık oldu. Uçurtma yavaşça kuma indi. Chase ipi hemen çekmek istedi. Ama kurallara uydu ve ipi hiç çekmedi. Chase ipe yakından baktı ve üç düğüm gördü. Düğümleri patisiyle ve dişleriyle tek tek açtı. Sonunda ip düzgün oldu. Chase ipi ağzıyla tuttu ve kumda koştu. Uçurtma yeniden havaya, bulutlara doğru yükseldi. Chase sevinçle havladı. Chase bundan sonra dolaşan ipleri hep yavaşça açtı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurallara uydu ve düğümleri"
   - Cümle 0 (plan satırı): «rüzgar döndü ve uçurtmanın ipi karmakarışık oldu | kurallara uydu ve düğümleri yavaşça açtı»
   - Açıklama: Plandaki 'kurallara uydu' soyut bir ifade.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama kurallara uydu"
   - Cümle 6: «Ama kurallara uydu ve ipi hiç çekmedi.»
   - Açıklama: 'Kurallara uymak' hangi kural olduğu belirsiz soyut bir kavram.
   - Açıklama: 'Kurallara uymak' hangi kural olduğu belli olmayan soyut bir ifade.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama kurallara uydu ve ipi hiç çekmedi"
   - Cümle 6: «Ama kurallara uydu ve ipi hiç çekmedi.»
   - Açıklama: Kartın özellikler alanındaki kurallara uyma özelliği belirli bir kural olmadan sabır yerine kullanılmış, işe yarar biçimde değil.
   - Açıklama: Kartın özelliği polis köpeğinin kurallara uyması; burada ortada olmayan bir kural anılıp özellik içi boş biçimde kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kurallara uydu ve ipi hiç çekmedi"
   - Cümle 6: «Ama kurallara uydu ve ipi hiç çekmedi.»
   - Açıklama: Hangi kurala uyulduğu kurulmadan kurallar sebepsizce çözüme getiriliyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama kurallara uydu"
   - Cümle 6: «Ama kurallara uydu ve ipi hiç çekmedi.»
   - Açıklama: Hiçbir kural kurulmadan Chase'in kurallara uyduğu söyleniyor; ayrıntı olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0133` birebir aynı, `@degisim: yatak -> uçurtma` (tutuyorsan), ardından `@onarim: ad2400f6422051e0decccfa856f1960b97928da8`, sonra gövde.

### Hikâye 12: tohum chase-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0138
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'koltuk', fiil 'saklamak', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: bütün kütükler yağmurdan ıslanmıştı | kütükleri kokladı ve kuru bir kütük buldu
@tohum: chase-0138
Ormandaki kamp yerinde yağmur yeni durmuştu. Chase kendine kütükten bir koltuk yapmak istiyordu. Ama bütün kütükler yağmurdan ıslanmıştı. Chase burnuyla kütükleri tek tek kokladı. Çoğu ıslak toprak kokuyordu. Sonra büyük bir ağacın altında kuru odun kokusu aldı. Ağacın kalın dalları bu kütüğü yağmurdan saklamıştı. Kütük çok ilginçti, arkası yüksek bir koltuğa benziyordu. Chase oradaki yaprakları topladı. Yaprakları kütüğün üstüne yumuşak bir yatak gibi serdi. Sonra yeni koltuğuna rahatça oturdu. Chase çok mutluydu, çünkü kendi koltuğunu kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dalları bu kütüğü yağmurdan"
   - Cümle 7: «Ağacın kalın dalları bu kütüğü yağmurdan saklamıştı.»
   - Açıklama: 'Bu kütük' daha önce tanıtılmadı, hangi kütüğü gösterdiği belli değil.
   - Açıklama: 'Bu kütük' daha önce tanıtılmamış; neyi gösterdiği belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kütük çok ilginçti"
   - Cümle 8: «Kütük çok ilginçti, arkası yüksek bir koltuğa benziyordu.»
   - Açıklama: 'İlginç' soyut bir kelime, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0138` birebir aynı, ardından `@onarim: c83862f00f85dc677f4a43983a406d817ed4fd05`, sonra gövde.
