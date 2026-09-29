# Editör görevi (onarım): Chase, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0034 (deneme 5 -> 6)

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
Ağaçlarda kuşlar ötüyordu. Chase parkta ilk kez mavi mürekkeple pati resmi yapmayı deniyordu. Ama rüzgar esince beyaz kağıt hep havaya kalkıyordu. Chase kurallara uyardı ve parka hiç çöp bırakmazdı. Kağıdı tutmak için yerden küçük taşlar topladı. Taşları kağıdın dört köşesine koydu. Artık kağıt rüzgarda hiç kıpırdamadı. Chase patisini dikkatli bir şekilde mürekkebe batırdı. Sonra kağıda düz basmaya çalıştı. Kağıtta çok güzel bir pati izi çıktı. Chase çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uyardı ve parka hiç çöp bırakmazdı"
   - Cümle 4: «Chase kurallara uyardı ve parka hiç çöp bırakmazdı.»
   - Açıklama: Tohumdaki kural özelliği yalnız anılıyor, sorunu çözmekte işe yaramıyor; sorun taşlarla çözülüyor.
   - Açıklama: Tohumdaki kural özelliği yalnız anılıyor, kağıdın uçması sorununun taşlarla çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uyardı ve parka hiç çöp bırakmazdı"
   - Cümle 4: «Chase kurallara uyardı ve parka hiç çöp bırakmazdı.»
   - Açıklama: Kurallara uyma ve çöp ayrıntısı olayda hiçbir işe yaramıyor.
   - Açıklama: Kurallara uyma ve çöp bırakmama ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0034` birebir aynı, ardından `@onarim: ff5d6e13caff028efd16b655da9c36437ce2ebd0`, sonra gövde.

### Hikâye 2: tohum chase-0044 (deneme 4 -> 5)

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
Chase, Skye ile çadırda eğlenceli resimler yapıyordu. Birden çadırın tepesinden tıp tıp diye bir ses geldi. Sonra Skye'ın resminin üstüne bir damla su düştü. "Bu su nereden geliyor?" diye sordu Skye. Ama çadırın tepesi karanlıktı ve orası görünmüyordu. Chase kurallara uyardı ve karanlıkta hep ışık yakardı. Hemen lambayı yaktı ve çadır aydınlandı. Tepedeki ipte ıslak, sarı bir sünger vardı. Su damla damla ondan düşüyordu. "Bu benim, kurusun diye oraya koymuştum!" dedi Skye ve güldü. Chase süngeri ipten aldı ve dışarı çıkardı. Sonra ikisi resim yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 6: «Chase kurallara uyardı ve karanlıkta hep ışık yakardı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram; ayrıca 'uyardı' fiili 'uyarmak' ile karışıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uyardı ve karanlıkta hep ışık yakardı"
   - Cümle 6: «Chase kurallara uyardı ve karanlıkta hep ışık yakardı.»
   - Açıklama: Kartın 'kurallara uyar' özelliği uydurma bir alışkanlığa bağlanıyor; ışık yakmak kurala uymakla işe yarar biçimde ilişkili değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu benim, kurusun diye oraya koymuştum"
   - Cümle 10: «"Bu benim, kurusun diye oraya koymuştum!" dedi Skye ve güldü.»
   - Açıklama: Süngeri oraya Skye kendisi koymuşken suyun nereden geldiğini bilmiyormuş gibi soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0044` birebir aynı, ardından `@onarim: e2b25fe8feddb8dfc8fd3e3689b78bfae87a90b3`, sonra gövde.

### Hikâye 3: tohum chase-0045 (deneme 4 -> 5)

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
@plan: rüzgar kağıdı çadırın üstüne attı | şapkasıyla arkadaşını çağırdı ve dalla kağıdı itti
@tohum: chase-0045
@degisim: şakımak -> ötmek
Bir sabah kamp yerinde kuşlar ötüyordu. Chase çadırın önünde bir kağıda mavi bir kolye çiziyordu. Yanında kremalı bir kek vardı. Birden rüzgar esti ve kağıt çadırın üstüne uçtu. Chase zıpladı ama oraya yetişemedi. Marshall uzakta, bir ağacın altında oturuyordu. Chase mavi şapkasını çıkardı ve havada salladı. Marshall şapkayı gördü ve hemen koşarak geldi. Çadırın üstündeki kağıdı görünce uzun bir dal getirdi. Chase dalla kağıdı yavaşça itti. Kağıt kaydı ve aşağı düştü. Chase onu yerden aldı ve kekinin yarısını Marshall'a verdi. Sonunda Chase çok mutlu oldu, çünkü çizdiği resmi geri almıştı.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "uzun bir dal getirdi"
   - Cümle 9: «Çadırın üstündeki kağıdı görünce uzun bir dal getirdi.»
   - Açıklama: Kağıdı indirme fikrini ve aracını Chase değil Marshall buluyor; yan karakter çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0045` birebir aynı, `@degisim: şakımak -> ötmek` (tutuyorsan), ardından `@onarim: b733bf417b3834b8d48c94939a1baddfeae3559c`, sonra gövde.

### Hikâye 4: tohum chase-0050 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: arkadaşının kemanı açık çantadan düşüp kayboldu | çantayı kokladı ve kokuyla kemanı buldu
@tohum: chase-0050
@degisim: güvenli -> temiz
Chase kamp yerinde Ryder ile oynuyordu. Birden Ryder çantasına baktı ve üzüldü. "Chase, çantam açık kalmış, kemanım yolda düşmüş," dedi Ryder. Chase kemanın nerede olduğunu çok merak etti. Önce boş çantayı dikkatle kokladı. Sonra aynı kokuyu yerde aradı. Bir çalının dibinde durdu. Keman orada, çamurun içinde duruyordu. "Ryder, kemanını buldum!" diye seslendi Chase. Ryder koşarak geldi ve kemanı aldı. Çamuru eliyle dikkatle sildi. Keman yine temiz oldu. "Teşekkürler, Chase, burnun çok iyi koku alıyor!" dedi Ryder. Sonra Ryder kemanı çaldı, Chase de mutlu mutlu dinledi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kemanım yolda düşmüş"
   - Cümle 3: «"Chase, çantam açık kalmış, kemanım yolda düşmüş," dedi Ryder.»
   - Açıklama: Kemanın açık çantadan fark edilmeden düşmesi zayıf bir sebep ve keman yolda değil kamp yerindeki çalının dibinde bulunuyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keman orada, çamurun içinde duruyordu"
   - Cümle 8: «Keman orada, çamurun içinde duruyordu.»
   - Açıklama: Kayıp kemana ek olarak çamurlanma ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0050` birebir aynı, `@degisim: güvenli -> temiz` (tutuyorsan), ardından `@onarim: 36f70c6a21042b9f9cf37f9050eea7512d2c9812`, sonra gövde.

### Hikâye 5: tohum chase-0056 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0056
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'alet', fiil 'yakalamak', sıfat 'renkli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: uçurtmanın ipi koptu ve uçurtma güneşe doğru uçtu | şapkasını gözlerine indirdi ve uçurtmayı buldu
@tohum: chase-0056
@degisim: yakalamak -> dönmek
Kumsalda güçlü bir rüzgar esiyordu. Chase iskelenin yanında renkli uçurtmasını uçuruyordu. Birden ipi koptu ve uçurtma güneşe doğru uçtu. Chase o tarafa baktı ama güneş çok parlaktı ve uçurtmayı göremedi. Uçurtmanın nereye düştüğünü çok merak etti. Hemen mavi şapkasını gözlerinin üstüne indirdi. Şapka gözlerine gölge yaptı ve Chase her yeri rahatça gördü. Uçurtma bir taşa takılmıştı ve rüzgarda bir müzik aleti gibi ses çıkarıyordu. Chase uçurtmayı ağzıyla aldı ve iskeleye geri döndü. Kaybolan uçurtmasını bulduğu için Chase çok sevindi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkasını gözlerine indirdi"
   - Cümle 0 (plan satırı): «uçurtmanın ipi koptu ve uçurtma güneşe doğru uçtu | şapkasını gözlerine indirdi ve uçurtmayı buldu»
   - Açıklama: Şapkayı gözlerine indirmek gözleri kapatır; kastedilen gözlerinin üstüne indirip gölge yapmak.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase o tarafa baktı ama güneş çok parlaktı"
   - Cümle 4: «Chase o tarafa baktı ama güneş çok parlaktı ve uçurtmayı göremedi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde doğrudan güneşe doğru bakılıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir müzik aleti gibi ses"
   - Cümle 8: «Uçurtma bir taşa takılmıştı ve rüzgarda bir müzik aleti gibi ses çıkarıyordu.»
   - Açıklama: 'Müzik aleti gibi' benzetmesi ve 'alet' kelimesi 3 yaşındaki çocuk için soyut ve uygun değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "rüzgarda bir müzik aleti gibi ses çıkarıyordu"
   - Cümle 8: «Uçurtma bir taşa takılmıştı ve rüzgarda bir müzik aleti gibi ses çıkarıyordu.»
   - Açıklama: Uçurtmanın müzik aleti gibi ses çıkarması kurulup hiç kullanılmayan işlevsiz bir ayrıntı.
   - Açıklama: Uçurtmanın çıkardığı ses kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0056` birebir aynı, `@degisim: yakalamak -> dönmek` (tutuyorsan), ardından `@onarim: 269e6aff7a5fb086ab6364d4e6729c4d7ae0443a`, sonra gövde.

### Hikâye 6: tohum chase-0059 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: top havuza düştü ve kenardan uzakta kaldı | şapkasını topun arkasına uzatıp topu kenara çekti
@tohum: chase-0059
@degisim: bezelye -> top
Bir sabah Chase parkta topla komik bir oyun oynuyordu. Topu burnunun üstünde tutuyor ve çiçekli çimlerin arasında yürüyordu. Ama top birden kaydı ve parktaki küçük havuza düştü. Top kenardan biraz uzakta kaldı ve Chase ona uzanamadı. Chase suya girmedi ve biraz düşündü. Sonra mavi şapkasını çıkardı ve ağzıyla tuttu. Şapkayı topun arkasına uzattı ve topu yavaş yavaş kenara çekti. Chase topu sudan aldı. Ama şapkası da ıslanmıştı. Chase buna çok güldü. Chase bundan sonra topla oynarken havuzdan uzak durdu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şapkayı topun arkasına uzattı"
   - Cümle 7: «Şapkayı topun arkasına uzattı ve topu yavaş yavaş kenara çekti.»
   - Açıklama: Havuza düşen topa kenardan uzanıp çekmek çocuğun taklit edebileceği suya yakın tehlikeli bir davranış.
   - Açıklama: Havuz kenarından suya uzanıp sudaki topu almak çocuğun taklit edebileceği tehlikeli bir davranış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapkayı topun arkasına uzattı"
   - Cümle 7: «Şapkayı topun arkasına uzattı ve topu yavaş yavaş kenara çekti.»
   - Açıklama: Kartın özellik alanı şapkayı takılan bir eşya olarak veriyor; burada şapka sudaki topu çekmek için alet olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0059` birebir aynı, `@degisim: bezelye -> top` (tutuyorsan), ardından `@onarim: 7ed0d17b08bd7017c823feeba8b3343df1e271be`, sonra gövde.

### Hikâye 7: tohum chase-0062 (deneme 3 -> 4)

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
Chase, Skye ile kulenin önünde oturuyordu. İkisi bir takvimde kısa kuyruklu kuşların resmine bakıyordu. Birden kuşların sesi geldi, ama güneş çok parlaktı ve Skye bakamadı. "Kuşlar nerede, Chase? Hiçbirini göremiyorum," dedi Skye. Chase mavi şapkasını çıkardı ve Skye'ın başına taktı. Şapka Skye'ın gözlerini güneşten korudu. Skye şimdi kuşları rahatça gördü. "Bunlar takvimdeki kuşlar! Güle güle!" dedi Skye ve patisini salladı. Chase de sevinçle havladı. Sonra kuşlar yavaş yavaş uzaklaştı. Skye çok sevindi, çünkü kuşlar gitmeden onları görmüştü.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Skye ile kulenin önünde oturuyordu"
   - Cümle 1: «Chase, Skye ile kulenin önünde oturuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye kulenin önünde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye kulenin önünde, dışarıda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0062` birebir aynı, `@degisim: vedalaşmak -> sallamak` (tutuyorsan), ardından `@onarim: 31464c0d6aa043d7f5610722a5b802d93a99cb05`, sonra gövde.

### Hikâye 8: tohum chase-0064 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0064
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'şemsiye', fiil 'yetiştirmek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: yağmur geliyordu ve ince sapı olan çiçek kırılabilirdi | yağmuru kokladı ve saksıyı kulübesine taşıdı
@tohum: chase-0064
@degisim: şemsiye -> saksı
Bir sabah Chase kulübesinin önünde saksıda küçük bir çiçek yetiştiriyordu. Gökyüzü açıktı ama Chase burnuyla yağmurun kokusunu aldı. Çiçeğin sapı çok inceydi ve sert damlalar onu kırabilirdi. Chase saksıyı ağzıyla dikkatle tuttu ve kulübesine taşıdı. Saksıyı kapının yanına, kuru bir yere koydu. Biraz sonra yağmur başladı. Damlalar kulübenin üstünde tık tık ses çıkardı. Chase çiçeğin yanında sessiz sessiz bekledi. Yağmur dinince saksıyı yine dışarı çıkardı. Çiçek hiç kırılmamıştı ve dimdik duruyordu. Chase bundan sonra yağmurdan önce çiçeğini hep içeri taşıdı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yağmuru kokladı ve saksıyı"
   - Cümle 0 (plan satırı): «yağmur geliyordu ve ince sapı olan çiçek kırılabilirdi | yağmuru kokladı ve saksıyı kulübesine taşıdı»
   - Açıklama: Henüz yağmayan yağmur koklanmaz; 'yağmurun kokusunu aldı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0064` birebir aynı, `@degisim: şemsiye -> saksı` (tutuyorsan), ardından `@onarim: 14d157c75eeb40b2ff1e87ce3f520487b1ce5677`, sonra gövde.

### Hikâye 9: tohum chase-0065 (deneme 2 -> 3)

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
@plan: arkadaşı uçak yapmak istedi ama kağıdı yoktu | kağıtlarının yarısını ona verdi
@tohum: chase-0065
Chase kumsalda büyük bir zarf açtı. İçinde uçak yapmak için renkli kağıtlar vardı. Ryder de uçak yapmak istedi, ama onun kağıtları kulede kalmıştı. Chase bir kural biliyordu: arkadaşınla paylaş. Chase kağıtları hemen ikiye ayırdı. "Ryder, yarısı senin," dedi Chase. "Teşekkürler, Chase!" dedi Ryder. İkisi kağıtları katladı ve güzel uçaklar yaptı. Sonra onları havaya attılar. Uçaklar rüzgarla havalandı ve yumuşak kuma kondu. Chase ile Ryder uçaklarını tekrar tekrar uçurdu ve mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "bir kural biliyordu: arkadaşınla paylaş."
   - Cümle 4: «Chase bir kural biliyordu: arkadaşınla paylaş.»
   - Açıklama: İki noktadan sonra aktarılan kural tırnak içinde ve büyük harfle yazılmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0065` birebir aynı, ardından `@onarim: 4dc8877119108b495eefeaefa3e8379e24b38191`, sonra gövde.

### Hikâye 10: tohum chase-0066 (deneme 2 -> 3)

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
Parkta neşeli bir trompet sesi duyuldu. Rubble ile Chase kaydırağın yanında oyuncak bir trompetle oynuyordu. Ama tek bir trompet vardı ve ikisi de çalmak istedi. Parkta herkes sırayla oynardı. Chase de kurallara uyardı. "Sırayla çalalım, Rubble," dedi Chase. "Olur, önce ben çalayım," dedi Rubble. Rubble çaldı ve Chase gözlerini kapatıp şarkıyı dinledi. Sonra trompeti Chase aldı ve güzel bir şarkı çaldı. Rubble kuyruğunu salladı. Chase ile Rubble çok sevindi, çünkü sırayla çalınca ikisi de eğlenmişti.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Parkta neşeli bir trompet sesi duyuldu"
   - Cümle 1: «Parkta neşeli bir trompet sesi duyuldu.»
   - Açıklama: Trompet sesi duyuluyor ama sonra ikisinin de henüz çalmadığı ve çalmak için sıra beklediği anlatılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase de kurallara uyardı"
   - Cümle 5: «Chase de kurallara uyardı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve 3 yaşındaki çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0066` birebir aynı, `@degisim: hazırlıklı -> neşeli` (tutuyorsan), ardından `@onarim: 313613a95dec65ea4d5b2c7fd80703e35b84e150`, sonra gövde.

### Hikâye 11: tohum chase-0067 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0067
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'yün', fiil 'asmak', sıfat 'zarif'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: koşarken yünden yapılmış çiçeğe çarptı ve onu düşürdü | özür diledi ve çiçeği çite geri astı
@tohum: chase-0067
@degisim: zarif -> güzel
Rüzgar esiyordu ve Chase parkta koşuyordu. Skye yünden güzel bir çiçek yapmış ve parkın çitine bağlamıştı. Chase koşarken dikkat etmedi, çiçeğe çarptı ve onu yere düşürdü. Skye yerdeki çiçeğe baktı ve üzüldü. Chase bir kural biliyordu: hata yapan özür diler. "Özür dilerim, Skye, çiçeğini düşürdüm," dedi Chase. Sonra çiçeği yerden aldı ve tozunu silkti. Chase onu dikkatle çite geri astı. "Teşekkürler, Chase, çiçeğim yine yerinde," dedi Skye. Sonra ikisi parkta kaydıraktan mutlu mutlu kaydı.
```

**Hakem bulguları (2):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hata yapan özür diler"
   - Cümle 5: «Chase bir kural biliyordu: hata yapan özür diler.»
   - Açıklama: Anlatımda -dı'lı geçmiş zamandan geniş zamana kayılmış; 'özür dilerdi' gibi olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bir kural biliyordu: hata yapan özür diler"
   - Cümle 5: «Chase bir kural biliyordu: hata yapan özür diler.»
   - Açıklama: 'Kural' ve 'hata yapan özür diler' soyut bir genelleme; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0067` birebir aynı, `@degisim: zarif -> güzel` (tutuyorsan), ardından `@onarim: 6b02387e011f420a7f10d9212c2f3ef0b784e911`, sonra gövde.

### Hikâye 12: tohum chase-0069 (deneme 2 -> 3)

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
@plan: arkadaşının oyuncak piyanosunu bir yere bırakıp kaybetti | özür diledi ve kokuyu izleyip piyanoyu buldu
@tohum: chase-0069
@degisim: gizemli -> renkli
Parkta Chase, Marshall'ın renkli oyuncak piyanosuyla oynuyordu. Sonra kaydırağa koşarken piyanoyu kum havuzuna bıraktı. Ama nereye bıraktığını unuttu ve piyanoyu kaybetti. Marshall piyanosunu aradı ve çok üzüldü. Chase, Marshall'dan hemen özür diledi. Piyanoda Marshall'ın kokusu vardı. Chase burnuyla bu kokuyu izledi ve kum havuzuna gitti. Piyano orada, kumun üstünde duruyordu. Chase onu aldı, kumunu silkti ve Marshall'a verdi. Marshall kuyruğunu salladı ve Chase'e sarıldı. Sonra ikisi piyanoyu sırayla çalıp mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama nereye bıraktığını unuttu"
   - Cümle 3: «Ama nereye bıraktığını unuttu ve piyanoyu kaybetti.»
   - Açıklama: Piyano az önce parktaki kum havuzuna, kumun üstüne açıkça bırakılmışken kaybolması akla yatkın değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Piyanoda Marshall'ın kokusu vardı"
   - Cümle 6: «Piyanoda Marshall'ın kokusu vardı.»
   - Açıklama: Çözümü getiren koku sebepsizce beliriyor ve Marshall da parkta dolaştığı için onun kokusunu izlemek Chase'i piyanoya götürmek için akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0069` birebir aynı, `@degisim: gizemli -> renkli` (tutuyorsan), ardından `@onarim: 6d843f7a3461c1ca6ea5c31e20803eace21afe45`, sonra gövde.
