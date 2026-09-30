# Editör görevi (onarım): Chase, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0139 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0139
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: sırayla oynamak
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'tabak', fiil 'sıçramak', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: ikisi de hep atmak istedi ve sıra karıştı | şapkayı takan atar dedi ve şapkayı sırayla verdi
@tohum: chase-0139
@degisim: dağınık -> sarı
Chase ile Ryder kumsalda sarı bir plastik tabakla oynuyordu. Tabağı birbirine atıp havada tutuyorlardı. Ama ikisi de hep atmak istedi ve sıra karıştı. Chase biraz düşündü ve mavi şapkasını çıkardı. "Şapkayı takan tabağı atar, Ryder," dedi Chase. Chase şapkayı önce Ryder'a verdi. Ryder şapkayı taktı ve tabağı uzağa attı. Chase kumda koştu, sıçradı ve tabağı ağzıyla tuttu. Ryder gülerek şapkayı Chase'e uzattı. "Sıra sende, Chase," dedi Ryder. Chase şapkayı taktı ve tabağı Ryder'a attı. İkisi sırayla atarak oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "şapkayı takan atar dedi"
   - Cümle 0 (plan satırı): «ikisi de hep atmak istedi ve sıra karıştı | şapkayı takan atar dedi ve şapkayı sırayla verdi»
   - Açıklama: Plandaki aktarılan söz tırnak içinde değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi de hep atmak istedi ve sıra karıştı"
   - Cümle 3: «Ama ikisi de hep atmak istedi ve sıra karıştı.»
   - Açıklama: Birbirine tabak atılan oyunda sıra kendiliğinden değiştiği için sıranın karışmasının sebebi akla yatkın değil ve söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0139` birebir aynı, `@degisim: dağınık -> sarı` (tutuyorsan), ardından `@onarim: 31e142d1b07a1cf2955bb0b4c9607cf8843a85bf`, sonra gövde.

### Hikâye 2: tohum chase-0140 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Rubble
@tohum: chase-0140
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: paylaşmak
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'mont', fiil 'çırpmak', sıfat 'mutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | park | Rubble
@plan: soğuk rüzgarda arkadaşının başı açıktı | mavi şapkasını arkadaşıyla paylaştı
@tohum: chase-0140
Rüzgar parkta çok soğuk esiyordu. Chase ile Rubble salıncakların yanında oynuyordu. Rubble'ın kalın bir montu vardı ama başında hiçbir şey yoktu. "Başım çok soğuk," dedi Rubble. Chase mavi şapkasını çıkardı ve Rubble'ın başına taktı. "Şapkamı seninle paylaşırım, Rubble," dedi Chase. Şapka onu hemen ısıttı. Rubble mutlu oldu ve ön patilerini çırptı. Sonra montunu açtı ve bir ucunu Chase'in sırtına örttü. İki arkadaş yan yana oturdu. "Teşekkürler, Chase, paylaşınca ikimiz de sıcacık olduk!" dedi Rubble.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Rubble'ın kalın bir montu vardı"
   - Cümle 3: «Rubble'ın kalın bir montu vardı ama başında hiçbir şey yoktu.»
   - Açıklama: Kartta Rubble'ın montu yok; kapalı dünyaya kartta olmayan bir eşya ekleniyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şapka onu hemen ısıttı"
   - Cümle 7: «Şapka onu hemen ısıttı.»
   - Açıklama: 'Onu' zamirinin Chase'i mi Rubble'ı mı gösterdiği belli değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir ucunu Chase'in sırtına örttü"
   - Cümle 9: «Sonra montunu açtı ve bir ucunu Chase'in sırtına örttü.»
   - Açıklama: 'Örtmek' örtülen şeyi nesne alır; 'sırtına örttü' yerine 'sırtını örttü' ya da 'sırtına attı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0140` birebir aynı, ardından `@onarim: f9a397c2c3d5c1c7e5786497d019c772f7f9011b`, sonra gövde.

### Hikâye 3: tohum chase-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0141
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'şal', fiil 'sığmak', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: top yosunların arasına düştü ve görünmedi | yosunları tek tek kokladı ve topu buldu
@tohum: chase-0141
@degisim: şal -> top
Bir sabah Chase kumsalda yepyeni topuyla oynuyordu. Topu burnunun ucunda zıplatıyordu. Her seferinde Chase'in kulakları da havaya kalkıyordu. Bir kez top uzağa sıçradı ve yosunların arasına düştü. Orada bir sürü yosun vardı ve top görünmüyordu. Chase yosunları burnuyla tek tek kokladı. Bir yerde topunun kokusunu aldı. Yosunları patisiyle itti. Top küçük bir çukura tam sığmıştı. Chase topu çukurdan çıkardı ve yine zıplatmaya başladı. Chase çok sevindi, çünkü topunu bulmuş ve oyununa dönmüştü.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Her seferinde Chase'in kulakları da havaya kalkıyordu.»
   - Açıklama: Sorun ilk 3 cümlede değil ancak 4. cümlede söyleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Her seferinde Chase'in kulakları da havaya kalkıyordu"
   - Cümle 3: «Her seferinde Chase'in kulakları da havaya kalkıyordu.»
   - Açıklama: Kulakların kalkması olayda hiçbir işe yaramayan ayrıntı.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Bir kez top uzağa sıçradı ve yosunların arasına düştü"
   - Cümle 4: «Bir kez top uzağa sıçradı ve yosunların arasına düştü.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0141` birebir aynı, `@degisim: şal -> top` (tutuyorsan), ardından `@onarim: 6718f8f2e0f5680b9373c3fdc38e21316dc3b996`, sonra gövde.

### Hikâye 4: tohum chase-0142 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0142
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'köfte', fiil 'incelemek', sıfat 'çabuk'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: yeni köfte çok sıcaktı ve üstünden buhar çıkıyordu | şapkasını salladı ve köfte soğudu
@tohum: chase-0142
Chase kulübesinin önünde ilk kez köfte yemeyi deneyecekti. Köfteyi dikkatle inceledi. Ama köfte çok sıcaktı ve üstünden buhar çıkıyordu. Chase çabuk yemek istiyordu. Mavi şapkasını çıkardı ve köfteye doğru salladı. Şapkadan serin bir rüzgar geldi. Buhar yavaş yavaş azaldı. Chase biraz daha bekledi. Sonunda köfte soğudu ve ılık oldu. Chase köfteyi yedi ve tadını çok beğendi. Sonra şapkasını yine başına taktı. Chase bundan sonra sıcak yemeği yemeden önce hep biraz bekledi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapkadan serin bir rüzgar geldi"
   - Cümle 6: «Şapkadan serin bir rüzgar geldi.»
   - Açıklama: Karttaki özellik mavi şapka takmaktır; şapka burada rüzgar üreten bir araç gibi gösteriliyor ve köfteyi asıl soğutan beklemek oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0142` birebir aynı, ardından `@onarim: c199c21e0fc44028921d9179b6cf0ee98a60f7dd`, sonra gövde.

### Hikâye 5: tohum chase-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0143
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'bardak', fiil 'doldurmak', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: küçük köpek koştuğu için bardaktaki su döküldü | kurallara uydu, yavaş yürüdü ve suyu taşıdı
@tohum: chase-0143
Kulenin önünde Chase ile Skye küçük bir çiçeğe su taşıyordu. Ama Skye koştuğu için bardaktaki su hep döküldü. "Çiçeğe hiç su kalmıyor," dedi Skye utangaç bir sesle. Chase bardağı musluktan yeniden doldurdu. "Kurallara göre su taşırken koşmak yok, Skye," dedi Chase. Chase bardağı ağzıyla dikkatle tuttu ve yavaş yavaş yürüdü. Skye da onun yanında yürüdü. Bardaktaki su hiç dökülmedi. Chase bardağı Skye'a verdi ve Skye suyu çiçeğe döktü. Skye bundan sonra Chase gibi su taşırken hiç koşmadı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurallara uydu, yavaş"
   - Cümle 0 (plan satırı): «küçük köpek koştuğu için bardaktaki su döküldü | kurallara uydu, yavaş yürüdü ve suyu taşıdı»
   - Açıklama: Plan satırında soyut 'kurallara uymak' kavramı var.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Kulenin önünde Chase ile Skye"
   - Cümle 1: «Kulenin önünde Chase ile Skye küçük bir çiçeğe su taşıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye kulenin önünde geçiyor, ev hiç kurulmuyor.
   - Açıklama: Başlıktaki yer ev ama hikaye kulenin önünde, dışarıda geçiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedi Skye utangaç bir sesle"
   - Cümle 3: «"Çiçeğe hiç su kalmıyor," dedi Skye utangaç bir sesle.»
   - Açıklama: Suyun dökülmesine üzülen birinin sesi 'utangaç' olmaz; kelime duruma uymuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara göre su taşırken"
   - Cümle 5: «"Kurallara göre su taşırken koşmak yok, Skye," dedi Chase.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0143` birebir aynı, ardından `@onarim: 66e6473deccf3268024c819a4c1e0c983db5cdc4`, sonra gövde.

### Hikâye 6: tohum chase-0145 (deneme 1 -> 2)

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
@plan: çeşme açık kaldı ve güçlü su gemiyi devirdi | kurallara uydu, çeşmeyi kapattı ve gemi karşıya gitti
@tohum: chase-0145
Ağaçların arasında rüzgar hafif esiyordu. Chase ile Ryder kamp yerinde çeşmenin havuzunda yaprak gemiyle deniz oyunu oynuyordu. Ama çeşme açık kalmıştı ve güçlü su gemiyi hep devirdi. "Gemim karşıya hiç gitmiyor," dedi Ryder. "Kurallara göre çeşme açık kalmaz, Ryder," dedi Chase. Chase patisiyle çeşmeyi kapattı. Havuzdaki su artık kıpırdamıyordu. Ryder gemiyi yeniden suya koydu. Gemi rahatça karşı kenara gitti. Ryder sevinçle Chase'e göz kırptı. Chase ile Ryder bundan sonra oyuna başlamadan önce çeşmeyi hep kapattı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurallara uydu, çeşmeyi kapattı"
   - Cümle 0 (plan satırı): «çeşme açık kaldı ve güçlü su gemiyi devirdi | kurallara uydu, çeşmeyi kapattı ve gemi karşıya gitti»
   - Açıklama: Plandaki 'kurallara uymak' soyut bir kavram.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güçlü su gemiyi hep devirdi"
   - Cümle 3: «Ama çeşme açık kalmıştı ve güçlü su gemiyi hep devirdi.»
   - Açıklama: 'Hep' ile süreklilik anlatılıyor; 'hep deviriyordu' olmalı.
   - Açıklama: 'Hep' ile süreklilik anlatılırken -dı yerine 'deviriyordu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara göre çeşme açık kalmaz"
   - Cümle 5: «"Kurallara göre çeşme açık kalmaz, Ryder," dedi Chase.»
   - Açıklama: 'Kurallara göre' soyut kavram, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Kurallar' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "önce çeşmeyi hep kapattı"
   - Cümle 11: «Chase ile Ryder bundan sonra oyuna başlamadan önce çeşmeyi hep kapattı.»
   - Açıklama: 'Bundan sonra hep' ile görünüş uyumsuz; 'hep kapattılar/kapatıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0145` birebir aynı, ardından `@onarim: 328b10079f89f0e33a2b3a3af25afec9d79842cf`, sonra gövde.

### Hikâye 7: tohum chase-0146 (deneme 1 -> 2)

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
@plan: yerde tek değnek vardı ve ikisi de çizmek istedi | kurallara uydu, dal koparmadı ve değneği ikiye böldü
@tohum: chase-0146
Chase ile Marshall kamp yerinde toprağa resim çizmek istedi. Etrafta kokulu çam ağaçları vardı. Ama yerde yalnız bir değnek vardı. Marshall kuleyi özlemişti ve onun resmini çizmek istiyordu. "Hadi ağaçtan yeni bir dal koparalım," dedi Marshall. "Olmaz, Marshall, kurallara göre dal koparmak yasak," dedi Chase. Chase değneği ikiye böldü. "Gel, bunu paylaşalım," dedi Chase ve bir parçasını Marshall'a verdi. Marshall toprağa büyük bir kule çizdi. Chase de yanına küçük bir kulübe çizdi. Marshall kuyruğunu mutlu mutlu salladı. Chase ile Marshall bundan sonra tek değneği hep ikiye böldü.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Marshall kuleyi özlemişti"
   - Cümle 4: «Marshall kuleyi özlemişti ve onun resmini çizmek istiyordu.»
   - Açıklama: Hangi kulenin kastedildiği belli değil; kule önceden tanıtılmadan belirli biçimde geçiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onun resmini çizmek istiyordu"
   - Cümle 4: «Marshall kuleyi özlemişti ve onun resmini çizmek istiyordu.»
   - Açıklama: 'onun' zamirinin kuleyi mi yoksa başka birini mi gösterdiği belli değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurallara göre dal koparmak yasak"
   - Cümle 6: «"Olmaz, Marshall, kurallara göre dal koparmak yasak," dedi Chase.»
   - Açıklama: 'kurallar' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tek değneği hep ikiye böldü"
   - Cümle 12: «Chase ile Marshall bundan sonra tek değneği hep ikiye böldü.»
   - Açıklama: Belirtili 'tek değneği' ile 'bundan sonra hep' uyumsuz; 'tek değnek olunca onu ikiye böldü' gibi olmalı.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bundan sonra tek değneği hep ikiye böldü"
   - Cümle 12: «Chase ile Marshall bundan sonra tek değneği hep ikiye böldü.»
   - Açıklama: Son cümle olaydan çıkan anlamlı bir ders ya da sıcak kapanış değil, tuhaf bir alışkanlık genellemesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0146` birebir aynı, ardından `@onarim: 10eb64da28ced78aabc4c9e6baa239e1204a50ac`, sonra gövde.

### Hikâye 8: tohum chase-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0147
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kağıt', fiil 'planlamak', sıfat 'üzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: kulenin tepesi için hiç kozalak bulamadı | burnuyla bir kokuyu izledi ve karın altında kozalak buldu
@tohum: chase-0147
Chase karlı dağda kardan bir kule yapıyordu. Kuleyi önce bir kağıda çizerek planladı. Resimde kulenin tepesinde bir kozalak vardı ama karda hiç kozalak yoktu. Chase biraz üzgündü. Birden karın altından güzel bir koku geldi. Chase bu kokuyu çok merak etti. Burnunu karda gezdirdi ve adım adım ilerledi. Koku bir çam ağacının yanından geliyordu. Chase karı patileriyle kazdı ve kokuyu yapan büyük bir kozalak buldu. Chase kozalağı kulenin tepesine koydu. Kule tıpkı kağıttaki resim gibi oldu. Chase çok sevindi, çünkü kokunun nereden geldiğini bulmuş ve kulesini bitirmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kağıda çizerek planladı"
   - Cümle 2: «Kuleyi önce bir kağıda çizerek planladı.»
   - Açıklama: 'Planlamak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Planlamak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden karın altından güzel bir koku geldi"
   - Cümle 5: «Birden karın altından güzel bir koku geldi.»
   - Açıklama: Çözüm Chase aramadan, rastlantıyla gelen bir kokuyla sebepsizce geliyor.
   - Açıklama: Çözümü getiren koku sebepsizce, tam gerektiği anda beliriyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kokuyu yapan büyük bir kozalak"
   - Cümle 9: «Chase karı patileriyle kazdı ve kokuyu yapan büyük bir kozalak buldu.»
   - Açıklama: Koku yapılmaz; 'kokuyu yapan' fiil nesnesine uymuyor.
   - Açıklama: Koku 'yapılmaz'; 'kokan bir kozalak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0147` birebir aynı, ardından `@onarim: 5b8b84a9f407f904304379ba41f3a10d7a433dc8`, sonra gövde.
