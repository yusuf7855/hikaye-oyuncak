# Editör görevi (onarım): Chase, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0044 (deneme 5 -> 6)

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
Chase, Skye ile çadırda eğlenceli resimler yapıyordu. Birden çadırın tepesinden tıp tıp diye bir ses geldi. Sonra Skye'ın resminin üstüne bir damla su düştü. "Bu su nereden geliyor?" diye sordu Skye. Ama çadırın tepesi karanlıktı ve orası görünmüyordu. Chase kurallara uydu ve çadırın tepesine tırmanmadı. Onun yerine lambayı yaktı ve çadır aydınlandı. Tepedeki ipte ıslak, sarı bir sünger vardı. Kurusun diye oraya asılmıştı. Su damla damla ondan düşüyordu. "Demek su bundan geliyormuş!" dedi Skye ve güldü. Chase süngeri ipten aldı ve dışarı çıkardı. Sonra ikisi resim yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çadırın tepesi karanlıktı ve orası görünmüyordu"
   - Cümle 5: «Ama çadırın tepesi karanlıktı ve orası görünmüyordu.»
   - Açıklama: Çadırda resim yapılacak kadar ışık varken tepede asılı süngerin hiç görünmemesi ve lambanın sonradan yakılması çelişkili.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 6: «Chase kurallara uydu ve çadırın tepesine tırmanmadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve hangi kuralın kastedildiği belli değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uydu ve çadırın tepesine tırmanmadı"
   - Cümle 6: «Chase kurallara uydu ve çadırın tepesine tırmanmadı.»
   - Açıklama: Tırmanma kuralı hiçbir olaydan çıkmıyor; özelliği göstermek için sebepsizce eklenmiş işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0044` birebir aynı, ardından `@onarim: 6e692300f0ccef66a2b7c14c13408994dc918ae7`, sonra gövde.

### Hikâye 2: tohum chase-0045 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0045
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kolye', fiil 'şakımak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: rüzgar kağıdı çadırın üstüne attı | şapkasıyla arkadaşını çağırdı ve birlikte dalla kağıdı ittiler
@tohum: chase-0045
@degisim: şakımak -> ötmek
Bir sabah kamp yerinde kuşlar ötüyordu. Chase çadırın önünde bir kağıda mavi bir kolye çiziyordu. Yanında kremalı bir kek vardı. Birden rüzgar esti ve kağıt çadırın üstüne uçtu. Chase zıpladı ama oraya yetişemedi. Yerdeki uzun dal ise Chase için çok ağırdı. Marshall uzakta, bir ağacın altında oturuyordu. Chase mavi şapkasını çıkardı ve havada salladı. Marshall şapkayı gördü ve hemen koşarak geldi. Chase ona dalı gösterdi. İkisi dalı birlikte kaldırdı ve kağıdı yavaşça itti. Kağıt kaydı ve aşağı düştü. Chase onu yerden aldı ve kekinin yarısını Marshall'a verdi. Sonunda Chase çok mutlu oldu, çünkü çizdiği resmi geri almıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Yanında kremalı bir kek vardı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0045` birebir aynı, `@degisim: şakımak -> ötmek` (tutuyorsan), ardından `@onarim: 3538d26e6a330f3384ae73585dfd42afc3af0015`, sonra gövde.

### Hikâye 3: tohum chase-0050 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0050
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'keman', fiil 'silmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: keman yapış yapış olmuştu | kokuyu izleyip çantada açık bal kavanozunu buldu
@tohum: chase-0050
@degisim: güvenli -> temiz
Chase kamp yerinde Ryder ile oturuyordu. Ryder keman çalmak için kemanını çantasından çıkardı. Ama kemanın her yeri yapış yapıştı ve Ryder onu çalamadı. "Chase, bu yapışkan şey ne?" diye sordu Ryder. Chase bunu çok merak etti. Kemanı dikkatle kokladı ve tatlı bir koku aldı. Sonra aynı kokuyu Ryder'ın çantasında da buldu. Çantanın içinde kapağı açık bir bal kavanozu vardı. "Bu bal, Ryder! Kavanozdan kemana akmış," dedi Chase. Ryder kavanozun kapağını sıkıca kapattı. Sonra bir bezle kemanı güzelce sildi. Keman yine temiz oldu. Sonra Ryder kemanını çaldı ve Chase mutlu mutlu dinledi.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Ryder keman çalmak için"
   - Cümle 2: «Ryder keman çalmak için kemanını çantasından çıkardı.»
   - Açıklama: Kartın yanlar bölümünde Ryder'ın keman çalma yeteneği ya da kemanı yok.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra aynı kokuyu Ryder'ın"
   - Cümle 7: «Sonra aynı kokuyu Ryder'ın çantasında da buldu.»
   - Açıklama: 'Sonra' kelimesi kısa hikayede üç kez gereksiz tekrarlanıyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Ryder kavanozun kapağını sıkıca kapattı"
   - Cümle 11: «Ryder kavanozun kapağını sıkıca kapattı.»
   - Açıklama: Kavanozu kapatıp kemanı silerek sorunu asıl gideren Chase değil yan karakter Ryder.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonra bir bezle kemanı güzelce sildi"
   - Cümle 12: «Sonra bir bezle kemanı güzelce sildi.»
   - Açıklama: Kavanozu kapatıp kemanı temizleyerek sorunu Chase değil yan karakter Ryder çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0050` birebir aynı, `@degisim: güvenli -> temiz` (tutuyorsan), ardından `@onarim: bba761ff19de1ae594a1c76099905ce08426d233`, sonra gövde.

### Hikâye 4: tohum chase-0059 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0059
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bezelye', fiil 'ıslanmak', sıfat 'çiçekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: top fıskiyenin altına yuvarlandı | şapkasını başına bastırdı ve topu aldı
@tohum: chase-0059
@degisim: bezelye -> top
Bir sabah Chase parkta topla komik bir oyun oynuyordu. Topu burnunun üstünde tutuyor ve çiçekli çimlerin arasında yürüyordu. Ama top birden kaydı ve fıskiyenin altına yuvarlandı. Chase topu almak istedi ama başı ıslanacaktı. Chase biraz düşündü. Sonra mavi şapkasını başına iyice bastırdı. Suyun altına koştu ve topu ağzıyla aldı. Şapkanın altında başı kuru kaldı. Ama sırtı ve kuyruğu ıslanmıştı. Chase buna çok güldü. Chase bundan sonra topla oynarken fıskiyeden uzak durdu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "topu almak istedi ama başı ıslanacaktı"
   - Cümle 4: «Chase topu almak istedi ama başı ıslanacaktı.»
   - Açıklama: Asıl engel yalnız başın ıslanması; bu önemsiz ve çocuğu kaygılandırmayacak bir sorun.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Chase topu almak istedi ama başı ıslanacaktı"
   - Cümle 4: «Chase topu almak istedi ama başı ıslanacaktı.»
   - Açıklama: Sorun yalnız başın ıslanması; sonunda sırtı ve kuyruğu ıslanınca Chase gülüyor, yani sorun önemsiz kalıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ama sırtı ve kuyruğu ıslanmıştı"
   - Cümle 9: «Ama sırtı ve kuyruğu ıslanmıştı.»
   - Açıklama: Şapka ıslanmayı önleme çözümü olarak sunuluyor ama Chase yine ıslanıyor ve son ders çözümün işe yaramadığını ima ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0059` birebir aynı, `@degisim: bezelye -> top` (tutuyorsan), ardından `@onarim: 15b8fcda814a03cf156064d5875c658dcf27d712`, sonra gövde.

### Hikâye 5: tohum chase-0062 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0062
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'takvim', fiil 'vedalaşmak', sıfat 'kısa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: güneş çok parlaktı ve uçan kuşlar görünmedi | mavi şapkasını arkadaşının başına taktı
@tohum: chase-0062
@degisim: vedalaşmak -> sallamak
Chase, Skye ile kulenin içinde, pencerenin önünde oturuyordu. İkisi bir takvimde kısa kuyruklu kuşların resmine bakıyordu. Birden kuşların sesi geldi, ama güneş çok parlaktı ve Skye bakamadı. "Kuşlar nerede, Chase? Hiçbirini göremiyorum," dedi Skye. Chase mavi şapkasını çıkardı ve Skye'ın başına taktı. Şapka Skye'ın gözlerini güneşten korudu. Skye şimdi kuşları rahatça gördü. "Bunlar takvimdeki kuşlar! Güle güle!" dedi Skye ve patisini salladı. Chase de sevinçle havladı. Sonra kuşlar yavaş yavaş uzaklaştı. Skye çok sevindi, çünkü kuşlar gitmeden onları görmüştü.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "kulenin içinde, pencerenin önünde"
   - Cümle 1: «Chase, Skye ile kulenin içinde, pencerenin önünde oturuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bir kulenin içinde geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Skye ile kulenin içinde, pencerenin önünde"
   - Cümle 1: «Chase, Skye ile kulenin içinde, pencerenin önünde oturuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bir kulenin içinde geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0062` birebir aynı, `@degisim: vedalaşmak -> sallamak` (tutuyorsan), ardından `@onarim: 6cd613c10842aecc27536db38df7c047bd3dfd44`, sonra gövde.

### Hikâye 6: tohum chase-0065 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0065
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'zarf', fiil 'havalanmak', sıfat 'büyük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: arkadaşı uçak yapmak istedi ama kağıdı yoktu | kağıtları ikiye ayırıp yarısını ona verdi
@tohum: chase-0065
Chase kumsalda büyük bir zarf açtı. İçinde uçak yapmak için renkli kağıtlar vardı. Ryder de uçak yapmak istedi, ama onun kağıtları kulede kalmıştı. Chase kurallara uyardı ve her şeyi arkadaşlarıyla paylaşırdı. Kağıtları hemen ikiye ayırdı. "Ryder, yarısı senin," dedi Chase. "Teşekkürler, Chase!" dedi Ryder. İkisi kağıtları katladı ve güzel uçaklar yaptı. Sonra onları havaya attılar. Uçaklar rüzgarla havalandı ve yumuşak kuma kondu. Chase ile Ryder uçaklarını tekrar tekrar uçurdu ve mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uyardı ve her şeyi arkadaşlarıyla paylaşırdı"
   - Cümle 4: «Chase kurallara uyardı ve her şeyi arkadaşlarıyla paylaşırdı.»
   - Açıklama: Karttaki kurallara uyma özelliği işe yarar biçimde kullanılmıyor, paylaşmayla karıştırılıp yalnız söyleniyor.
   - Açıklama: Tohumdaki kural özelliği işe yarar biçimde kullanılmıyor; paylaşmak kurala uymakla ilgili değil, özellik etiket olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0065` birebir aynı, ardından `@onarim: 82ef2675f2d015b83faade913fa3f90f44786be4`, sonra gövde.

### Hikâye 7: tohum chase-0066 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Rubble
@tohum: chase-0066
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: sırayla oynamak
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'trompet', fiil 'kapatmak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Rubble
@plan: tek trompet vardı ve ikisi de çalmak istedi | kurallara uydu ve sırayla çalmayı söyledi
@tohum: chase-0066
@degisim: hazırlıklı -> neşeli
Parkta kuşlar neşeli neşeli ötüyordu. Rubble ile Chase kaydırağın yanında oyuncak bir trompetle oynuyordu. Ama tek bir trompet vardı ve ikisi de çalmak istedi. Parkta kurallar vardı ve herkes sırayla oynardı. "Sırayla çalalım, Rubble," dedi Chase. "Olur, önce ben çalayım," dedi Rubble. Rubble çaldı ve Chase gözlerini kapatıp şarkıyı dinledi. Sonra trompeti Chase aldı ve güzel bir şarkı çaldı. Rubble kuyruğunu salladı. Chase ile Rubble çok sevindi, çünkü sırayla çalınca ikisi de eğlenmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Parkta kurallar vardı"
   - Cümle 4: «Parkta kurallar vardı ve herkes sırayla oynardı.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0066` birebir aynı, `@degisim: hazırlıklı -> neşeli` (tutuyorsan), ardından `@onarim: 867fa6855c67b12516e4d3fd5c2e0ce87c22f51f`, sonra gövde.

### Hikâye 8: tohum chase-0069 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Marshall
@tohum: chase-0069
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'piyano', fiil 'kaybetmek', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Marshall
@plan: çukur kazarken arkadaşının piyanosunu kumla örtüp kaybetti | özür diledi ve kokusunu izleyip piyanoyu kumdan çıkardı
@tohum: chase-0069
@degisim: gizemli -> renkli
Parkta Chase, Marshall'ın renkli oyuncak piyanosuyla oynuyordu. Sonra piyanoyu ağzıyla kum havuzuna götürdü. Orada bir çukur kazdı ve kumu arkasına attı. Kum piyanonun üstünü örttü ve Chase piyanoyu kaybetti. Marshall piyanosunu aradı ve çok üzüldü. Chase, Marshall'dan hemen özür diledi. Sonra burnunu yere yaklaştırdı ve piyanonun kokusunu aradı. Arkasındaki küçük tepede o kokuyu aldı. Chase orayı kazdı ve piyanoyu çıkardı. Onu silkti ve Marshall'a verdi. Marshall kuyruğunu salladı ve Chase'e sarıldı. Sonra ikisi piyanoyu sırayla çalıp mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Kum piyanonun üstünü örttü ve Chase piyanoyu kaybetti"
   - Cümle 4: «Kum piyanonun üstünü örttü ve Chase piyanoyu kaybetti.»
   - Açıklama: Sorun (piyanonun kaybolması) ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ancak dördüncü cümlede ortaya çıkıyor, ilk üç cümlede söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0069` birebir aynı, `@degisim: gizemli -> renkli` (tutuyorsan), ardından `@onarim: 3a49a158160ce0a1b4052a46d5ab17acd051ef24`, sonra gövde.

### Hikâye 9: tohum chase-0070 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0070
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'televizyon', fiil 'sevinmek', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: top kuyruğa çarptı ve bankın altına yuvarlandı | başını eğdi ve şapkasının önüyle topu kendine çekti
@tohum: chase-0070
@degisim: televizyon -> top
Parkta Chase simsiyah bir topla oynuyordu. Topu burnuyla havaya atıyor, sonra kuyruğuyla tutmaya çalışıyordu. Ama top bir kez kuyruğuna çarptı ve bankın altına yuvarlandı. Chase patisini uzattı, ama top çok uzaktaydı. Bankın altı dardı ve Chase oraya giremedi. Chase biraz düşündü ve başını yere eğdi. Mavi şapkasının önünü topun arkasına uzattı. Sonra başını yavaşça geri çekti ve top bankın altından çıktı. Chase topu burnuyla havaya attı ve bu sefer ağzıyla yakaladı. Chase çok sevindi, çünkü topuyla yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "top kuyruğa çarptı"
   - Cümle 0 (plan satırı): «top kuyruğa çarptı ve bankın altına yuvarlandı | başını eğdi ve şapkasının önüyle topu kendine çekti»
   - Açıklama: İyelik eki eksik; kimin kuyruğu olduğu belli değil, 'kuyruğuna' olmalı.
   - Açıklama: İyelik eki eksik; 'kuyruğuna' olmalı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Mavi şapkasının önünü topun arkasına uzattı"
   - Cümle 7: «Mavi şapkasının önünü topun arkasına uzattı.»
   - Açıklama: Uzattığı patisi topa yetişmezken başındaki şapkanın önünün topun arkasına uzanabilmesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0070` birebir aynı, `@degisim: televizyon -> top` (tutuyorsan), ardından `@onarim: a17d932d731a2117e8a13ce04afd6017ea7640e1`, sonra gövde.

### Hikâye 10: tohum chase-0071 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0071
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'mermer', fiil 'sıkılmak', sıfat 'özel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: koşarken kardan köpeğe çarptı ve köpeğin başı düştü | özür diledi ve kardan başı yerine koydu
@tohum: chase-0071
@degisim: mermer -> kar
Bir sabah Rubble karlı dağda kardan özel bir köpek yapıyordu. Chase onu bekliyordu, ama çok sıkıldı ve karda koşmaya başladı. Koşarken kardan köpeğe çarptı. Kardan köpeğin başı yere yuvarlandı. Rubble yerdeki başa baktı ve üzüldü. Chase kurallara uydu ve hemen Rubble'ın yanına gitti. "Özür dilerim, Rubble, beklerken sıkıldım ve koştum," dedi Chase. Sonra yuvarlanan başı itip geri getirdi. İkisi birlikte başı yerine koydu. Chase başın üstüne iki küçük kulak da yaptı. "Teşekkürler, Chase, köpeğimiz şimdi daha da güzel!" dedi Rubble.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Kardan köpeğin başı yere yuvarlandı"
   - Cümle 4: «Kardan köpeğin başı yere yuvarlandı.»
   - Açıklama: Planın sorunu olan başın düşmesi ancak dördüncü cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 6: «Chase kurallara uydu ve hemen Rubble'ın yanına gitti.»
   - Açıklama: Hikayede bir kural yok; 'kurallara uydu' bu bağlamda anlamsız kullanılmış.
   - Açıklama: Rubble'ın yanına gitmek bir kurala uymak değildir; 'kurallara uydu' eyleme uymuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uydu ve hemen Rubble'ın yanına gitti"
   - Cümle 6: «Chase kurallara uydu ve hemen Rubble'ın yanına gitti.»
   - Açıklama: Tohumdaki kurallara uyma özelliği sorunu çözmeye yaramıyor, yalnız adı geçiyor; kartın özellikler alanındaki işe yarar kullanıma aykırı.
   - Açıklama: Tohumdaki kural özelliği hangi kurala uyulduğu belli olmadan etiket gibi ekleniyor, çözümde işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uydu ve hemen"
   - Cümle 6: «Chase kurallara uydu ve hemen Rubble'ın yanına gitti.»
   - Açıklama: Chase'in kurallara uyması hiçbir kurala bağlanmıyor ve olayda işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0071` birebir aynı, `@degisim: mermer -> kar` (tutuyorsan), ardından `@onarim: aa786b4d035827791387b63b41749c7bdec487c6`, sonra gövde.

### Hikâye 11: tohum chase-0072 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0072
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'plak', fiil 'şaşırtmak', sıfat 'neşeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: rüzgar topu götürdü ve iskelenin altından bir ses geldi | kokladı ve sesin topundan geldiğini buldu
@tohum: chase-0072
@degisim: plak -> top
Kumsalda sert bir rüzgar esiyordu. Rüzgar Chase'in kırmızı topunu uzağa yuvarladı. Chase topunu aradı ama hiçbir yerde bulamadı. Birden iskelenin altından tok tok diye bir ses geldi. Bu ses Chase'i çok şaşırttı. Orası gölgeydi ve hiçbir şey görünmüyordu. Chase burnunu yere yaklaştırdı ve dikkatle kokladı. Gölgede kendi topunun kokusunu hemen tanıdı. Top, iskelenin direğine hafifçe çarpıyordu. Tok tok sesi buradan geliyordu. Chase topu patisiyle yavaşça dışarı çekti. Sonra neşeli bir sesle havladı. Chase çok sevindi, çünkü kaybolan topunu bulmuştu.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Orası gölgeydi ve hiçbir şey görünmüyordu"
   - Cümle 6: «Orası gölgeydi ve hiçbir şey görünmüyordu.»
   - Açıklama: Karanlık gölgeden gelen gizemli ses küçük çocuk için ürkütücü olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0072` birebir aynı, `@degisim: plak -> top` (tutuyorsan), ardından `@onarim: 39abb2e2cd131d53d1600bd80238310bc5f40a3e`, sonra gövde.

### Hikâye 12: tohum chase-0073 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Ryder
@tohum: chase-0073
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'halat', fiil 'gelmek', sıfat 'farklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Ryder
@plan: güneş yüzünden halatı göremedi ve ona takıldı | şapkasını gözlerinin üstüne indirdi ve on kez atladı
@tohum: chase-0073
Parkta kuşlar ötüyordu. Ryder halatı yerde döndürüyordu ve Chase üstünden atlıyordu. Chase on kez atlamak istiyordu, ama güneş gözlerine parlıyordu. Chase halatı göremedi ve halat ayağına takıldı. Chase çimlere yuvarlandı ve ikisi de güldü. "Güneş yüzünden halatı göremiyorum, Ryder," dedi Chase. Sonra mavi şapkasını farklı taktı ve önünü gözlerinin üstüne indirdi. Artık halatı çok iyi görüyordu. "Hazırım, Ryder, halatı döndür!" dedi Chase. Halat ona doğru geldi ve Chase hemen atladı. Ryder yüksek sesle saydı ve Chase tam on kez atladı. İkisi halat oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mavi şapkasını farklı taktı"
   - Cümle 7: «Sonra mavi şapkasını farklı taktı ve önünü gözlerinin üstüne indirdi.»
   - Açıklama: 'Farklı taktı' belirsiz; şapkanın nasıl takıldığı anlaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0073` birebir aynı, ardından `@onarim: 9bce53e4ab6c36035f85ca4cc9483846a88267c9`, sonra gövde.
