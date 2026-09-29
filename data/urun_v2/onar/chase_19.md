# Editör görevi (onarım): Chase, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0075 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0075
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bez', fiil 'dönmek', sıfat 'gri'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: güneş parladığı için sesin geldiği yeri göremedi | şapkasını gözlerinin üstüne indirdi ve dala takılan bezi buldu
@tohum: chase-0075
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken pat pat diye bir ses duydu. Ses uzaktan geliyordu, ama güneş karda parladığı için Chase uzağı göremiyordu. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi uzaktaki çam ağacını iyi görüyordu. Ağacın alçak bir dalında gri bir şey dönüyordu. Chase ağaca doğru yavaşça yürüdü. Bu, rüzgarın dala taktığı gri bir bezdi. Rüzgar esince bez dalın etrafında dönüyor ve ses çıkarıyordu. Chase bezi dişleriyle çekip daldan aldı. Ses hemen durdu. Chase bundan sonra bir ses duyunca önce durup dikkatle baktı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "pat pat diye bir ses duydu"
   - Cümle 2: «Chase karda yürürken pat pat diye bir ses duydu.»
   - Açıklama: Sesin Chase için neden önemli olduğu söylenmiyor; uzaktaki bir bezin sesini görememek çocuğun önemseyeceği bir sorun olarak kurulmuyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "güneş karda parladığı için Chase uzağı göremiyordu"
   - Cümle 3: «Ses uzaktan geliyordu, ama güneş karda parladığı için Chase uzağı göremiyordu.»
   - Açıklama: Bilinmeyen ses ve güneşin gözü alması iki ayrı sorun olarak iç içe duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0075` birebir aynı, ardından `@onarim: 1e19bd80404bdeb3855402c170d22c70ea442c9b`, sonra gövde.

### Hikâye 2: tohum chase-0076 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0076
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pelerin', fiil 'uyandırmak', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: yavaş yürüdü ve pelerin hiç kalkmadı | kurallara uydu ve sert kumda rüzgara doğru koştu
@tohum: chase-0076
@degisim: uyandırmak -> uçurmak
Bir sabah Chase kumsalda kıpkırmızı bir pelerin buldu ve taktı. Pelerini rüzgarda uçurmayı ilk kez deneyecekti. Ama Chase yavaş yürüdü ve pelerin hiç kalkmadı. Chase koşmak için düz bir yer aradı. Uzun iskele çok düzdü, ama orada koşmak yasaktı. Chase kurallara uydu ve iskeleye çıkmadı. Biraz ileride kum sert ve düzdü. Chase orada rüzgara doğru hızlı hızlı koştu. Pelerin arkasında havaya kalktı ve uçtu. Chase başını çevirip arkasına baktı ve sevinçle havladı. Sonra kumsalda mutlu mutlu koşmaya devam etti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "kıpkırmızı bir pelerin buldu"
   - Cümle 1: «Bir sabah Chase kumsalda kıpkırmızı bir pelerin buldu ve taktı.»
   - Açıklama: Kartın özelliklerinde Chase'in giysisi yalnız mavi şapka; kırmızı pelerin kartta olmayan bir eşya olarak ekleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "havaya kalktı ve uçtu"
   - Cümle 9: «Pelerin arkasında havaya kalktı ve uçtu.»
   - Açıklama: Pelerin Chase'in sırtında dalgalanır, 'uçtu' pelerinin uçup gittiğini düşündürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0076` birebir aynı, `@degisim: uyandırmak -> uçurmak` (tutuyorsan), ardından `@onarim: 5ea2dbdc9aa5f68e340b66249e3afd1f52a9f023`, sonra gövde.

### Hikâye 3: tohum chase-0077 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0077
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'yaprak', fiil 'ıslatmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: çiçeğin toprağı kuruydu ve kova çok ağırdı | şapkasına su doldurdu ve çiçeğe götürdü
@tohum: chase-0077
Ormandaki kamp yerinde güneş parlıyordu. Chase çiçek bakma oyunu oynuyordu ve küçük bir çiçeği seçmişti. Ama çiçeğin toprağı kuruydu ve yaprakları aşağı eğilmişti. Chase su aradı ve ağacın dibinde soğuk suyla dolu bir kova buldu. Chase kovayı itti, ama kova çok ağırdı. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı kovaya daldırdı ve suyla doldurdu. Sonra şapkayı ağzıyla tuttu ve yavaş yavaş çiçeğe yürüdü. Su toprağı ve yaprakları ıslattı. Biraz sonra çiçeğin yaprakları yavaşça kalktı. Chase çok sevindi, çünkü küçük çiçek yine dik duruyordu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Chase çiçek bakma oyunu oynuyordu"
   - Cümle 2: «Chase çiçek bakma oyunu oynuyordu ve küçük bir çiçeği seçmişti.»
   - Açıklama: Tamlama bozuk; 'çiçeğe bakma oyunu' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ağacın dibinde soğuk suyla dolu bir kova buldu"
   - Cümle 4: «Chase su aradı ve ağacın dibinde soğuk suyla dolu bir kova buldu.»
   - Açıklama: Ormanda ağacın dibinde suyla dolu bir kova sebepsizce hazır bulunuyor ve çözümü kolaylaştırıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Chase kovayı itti, ama kova çok ağırdı"
   - Cümle 5: «Chase kovayı itti, ama kova çok ağırdı.»
   - Açıklama: Kuru toprak sorununun yanına ağır kova ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0077` birebir aynı, ardından `@onarim: d46bb4bd6e32a62e726f0ce8057f422313ae2ba0`, sonra gövde.

### Hikâye 4: tohum chase-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0078
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'çarşaf', fiil 'süpürmek', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: rüzgar çarşafı kaldırdı ve bir elma kayboldu | burnuyla elmanın kokusunu alıp onu buldu
@tohum: chase-0078
@degisim: konuşkan -> kırmızı
Kumsalda serin bir rüzgar esiyordu. Ryder ile Chase büyük bir çarşafın üstünde oturuyordu. Birden rüzgar çarşafın ucunu kaldırdı ve iki kırmızı elma kuma yuvarlandı. Ryder bir elmayı hemen buldu, ama öbürü yoktu. Chase burnunu kuma yaklaştırdı ve elmanın kokusunu aldı. Sonra küçük bir kum tepesine doğru yürüdü. Elma tepenin arkasında, kumun içindeydi. Chase patisiyle kumu süpürdü ve elma göründü. Chase elmayı ağzıyla aldı ve Ryder'a getirdi. "Teşekkürler, Chase, bir elma sana, bir elma bana," dedi Ryder. İkisi çarşafta elmalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden rüzgar çarşafın ucunu kaldırdı ve iki kırmızı elma kuma yuvarlandı.»
   - Açıklama: İlk üç cümlede yalnız elmaların yuvarlandığı söyleniyor; bir elmanın kaybolduğu sorunu ancak 4. cümlede açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0078` birebir aynı, `@degisim: konuşkan -> kırmızı` (tutuyorsan), ardından `@onarim: 9bd968b35db2d62abd93c7da74c9e210112ee142`, sonra gövde.

### Hikâye 5: tohum chase-0080 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0080
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'beşik', fiil 'yedirmek', sıfat 'plastik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: arkadaşı kardan pastayı ısırmak istedi ama kar yemek yasaktı | kurallara uydu ve arkadaşına bisküvi yedirdi
@tohum: chase-0080
@degisim: beşik -> pasta
Bir sabah Chase karlı dağda Rubble için kardan bir pasta yaptı. Pastanın yanına içi bisküvi dolu plastik bir kutu koydu. Rubble pastayı görünce hemen ısırmak istedi, ama kar yemek yasaktı. Chase kurallara uydu ve Rubble'ı durdurdu. "Dur, Rubble, kar yenmez, ama bu kutu senin!" dedi Chase. Rubble kutuyu açtı ve bisküvileri gördü. Kuyruğunu hızlı hızlı salladı. Chase bisküvileri tek tek Rubble'a yedirdi. "Bu çok güzel bir sürpriz, Chase!" dedi Rubble. Chase bundan sonra her kardan pastanın yanına bisküvi de koydu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama kar yemek yasaktı"
   - Cümle 3: «Rubble pastayı görünce hemen ısırmak istedi, ama kar yemek yasaktı.»
   - Açıklama: Rubble için yenmeyecek bir kar pastası yapıp sonra yasakla durdurmak yapay ve akla yatkın olmayan bir sorun.
   - Açıklama: Yasağın sebebi söylenmiyor ve sorun çocuğun önemseyeceği gerçek bir sorun gibi kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kurallara uydu ve Rubble'ı durdurdu"
   - Cümle 4: «Chase kurallara uydu ve Rubble'ı durdurdu.»
   - Açıklama: Kuralı çiğneyecek olan Rubble; 'kurallara uydu' Chase'in eylemine uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 4: «Chase kurallara uydu ve Rubble'ı durdurdu.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Chase bundan sonra her kardan pastanın yanına bisküvi de koydu"
   - Cümle 10: «Chase bundan sonra her kardan pastanın yanına bisküvi de koydu.»
   - Açıklama: Chase bisküviyi zaten baştan koymuştu; son cümle olaydan çıkan bir ders ya da sıcak kapanış vermiyor.
   - Açıklama: Chase bisküviyi zaten baştan koymuştu; son cümle olaydan çıkan bir ders vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0080` birebir aynı, `@degisim: beşik -> pasta` (tutuyorsan), ardından `@onarim: 36e3f17e95867e24d2aa38db9cf1ec8aa3503b32`, sonra gövde.

### Hikâye 6: tohum chase-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0081
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'mama', fiil 'çoğalmak', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: rüzgar mama kabını uzağa yuvarladı | şapkasını gözlerinin üstüne indirdi ve parlayan kabı buldu
@tohum: chase-0081
@degisim: tekerlekli -> garip
Kumsalda sert bir rüzgar esiyordu. Chase mamasını yiyecekti, ama mama kabı yerinde yoktu. Rüzgar kabı uzağa götürmüştü ve mama kuma dökülmüştü. Chase kumda küçük mama taneleri gördü. Tanelere bakarak yürüdü ve taneler çoğaldı. Uzakta, kumda garip bir şey parlıyordu. Chase mavi şapkasını gözlerinin üstüne indirdi. Şapkanın gölgesinde iyice baktı ve kendi mama kabını gördü. Chase kabı ağzıyla aldı ve yerine geri getirdi. Chase çok sevindi, çünkü kaybolan mama kabını bulmuştu.
```

**Hakem bulguları (2):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Chase çok sevindi, çünkü kaybolan mama kabını bulmuştu"
   - Cümle 10: «Chase çok sevindi, çünkü kaybolan mama kabını bulmuştu.»
   - Açıklama: Chase'in hedefi mamasını yemekti ama mama kuma dökülmüş kalıyor; boş kabın bulunmasıyla hedefe ulaşılmadan bitiyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "kaybolan mama kabını bulmuştu"
   - Cümle 10: «Chase çok sevindi, çünkü kaybolan mama kabını bulmuştu.»
   - Açıklama: Chase'in hedefi mamasını yemekti ama mama kuma dökülmüş kalıyor ve hikaye yalnız boş kabın bulunmasıyla bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0081` birebir aynı, `@degisim: tekerlekli -> garip` (tutuyorsan), ardından `@onarim: e1d8d4ffef8dfff81e08f4d5ab6481fc9b3980e1`, sonra gövde.

### Hikâye 7: tohum chase-0082 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0082
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'madalya', fiil 'kalkmak', sıfat 'gürültülü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: gürültülü bir rüzgar madalyanın yerini gösteren dalı götürdü | karı kokladı ve madalyayı bulup çıkardı
@tohum: chase-0082
Bir sabah Chase dağda hazine oyunu oynuyordu. Madalyasını karın içine saklamış ve üstüne bir dal dikmişti. Ama gürültülü bir rüzgar esti ve dalı uzağa götürdü. Artık madalyanın yeri belli değildi. Chase bir süre oturdu ve düşündü. Sonra ayağa kalktı ve burnunu yere yaklaştırdı. Madalyanın kokusunu küçük bir ağacın yanında buldu. Chase karı patileriyle hızlı hızlı kazdı. Beyaz karın içinden parlak madalya çıktı. Chase'in burnunun ucu da bembeyaz olmuştu. Chase madalyayı ağzına aldı ve sevinçle zıpladı. Chase çok mutluydu, çünkü madalyasını kendi burnuyla bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase'in burnunun ucu da bembeyaz olmuştu"
   - Cümle 10: «Chase'in burnunun ucu da bembeyaz olmuştu.»
   - Açıklama: Burnun beyazlaması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0082` birebir aynı, ardından `@onarim: b54da8118b270d1ed332df96051f3bd237e04a25`, sonra gövde.

### Hikâye 8: tohum chase-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0083
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: kaybolan eşya
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'dal', fiil 'düşünmek', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: küçük bir dalga kırılgan kabuğu kumla örttü | kumu kokladı ve kabuğu yavaşça çıkardı
@tohum: chase-0083
Bir sabah Chase ile Ryder kumsalda kırılgan bir deniz kabuğu buldu. Ryder kabuğu kuru bir dalın yanına bıraktı. Ama küçük bir dalga geldi ve kabuk kumun altında kayboldu. Ryder kumu eliyle karıştırdı ama onu bulamadı. Chase dalın yanında durdu ve düşündü. Sonra burnunu kuma yaklaştırdı ve kokladı. Kabuğun kokusu dalın biraz yanından geliyordu. Chase kabuk kırılmasın diye kumu yavaş yavaş kazdı. Kumun altından ince, beyaz kabuk çıktı. Chase onu ağzıyla Ryder'a götürdü. Ryder gülümsedi ve Chase'in başını okşadı. Chase çok sevindi, çünkü arkadaşının kabuğunu bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kumsalda kırılgan bir deniz kabuğu"
   - Cümle 1: «Bir sabah Chase ile Ryder kumsalda kırılgan bir deniz kabuğu buldu.»
   - Açıklama: 'Kırılgan' kelimesi 3 yaşındaki bir çocuğun bildiği bir kelime değil.
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0083` birebir aynı, ardından `@onarim: d69379b863e6f32b48b3c88bb668dc1ef38c31d2`, sonra gövde.

### Hikâye 9: tohum chase-0084 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0084
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'çatal', fiil 'bitmek', sıfat 'güçlü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: güçlü bir rüzgar sürpriz masasındaki çiçekleri uçurdu | çiçekleri toplayıp mavi şapkasının içine koydu
@tohum: chase-0084
Bir sabah Chase kulübelerin önünde Skye için sürpriz hazırlıyordu. Masaya bir kek, iki çatal ve sarı çiçekler dizdi. Ama güçlü bir rüzgar esti ve çiçekleri masadan uçurdu. Chase çiçekleri yerden topladı. Masada onları koyacak bir kap yoktu. Chase başındaki mavi şapkasını çıkardı. Çiçekleri şapkanın içine yerleştirdi ve kekin yanına bıraktı. Rüzgar yine esti ama çiçekler uçmadı. Böylece hazırlık bitti. Az sonra Skye geldi. "Bu sürpriz benim için mi, Chase?" diye sordu Skye. "Evet, Skye, çiçekler de senin için," dedi Chase. İkisi çatalları aldı ve keki birlikte yedi. Chase bundan sonra rüzgarlı havada hafif şeyleri bir kabın içine koydu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "güçlü bir rüzgar esti ve çiçekleri masadan uçurdu"
   - Cümle 3: «Ama güçlü bir rüzgar esti ve çiçekleri masadan uçurdu.»
   - Açıklama: Rüzgarın çiçekleri dağıtıp Chase'in onları toplaması önemsiz bir sorun.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "İkisi çatalları aldı ve keki birlikte yedi"
   - Cümle 13: «İkisi çatalları aldı ve keki birlikte yedi.»
   - Açıklama: Kartın tür alanına göre Chase ve Skye köpek yavrusudur; çatalla yemek yemeleri diziyi bilen çocuğa yanlış bilgi verir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0084` birebir aynı, ardından `@onarim: 033b773f7c4b7df835393671b229e0b2d51b842f`, sonra gövde.

### Hikâye 10: tohum chase-0085 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0085
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'armut', fiil 'fırçalamak', sıfat 'sevimli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: rüzgar sepeti devirdi ve armutlar kirlendi | kurallara uydu ve armutları temiz suyla yıkadı
@tohum: chase-0085
@degisim: fırçalamak -> yıkamak
Ormanda güçlü bir rüzgar esiyordu. Chase kamp yerinde Rubble için sevimli bir armut sepeti hazırlamıştı. Ama rüzgar sepeti devirdi ve armutlar toprağa düştü. Hepsinin üstü kirlendi. Kampın kurallarına göre yere düşen meyve önce yıkanırdı. Chase kovadaki temiz suyla armutları tek tek yıkadı. Sonra onları sepete geri koydu. Tam o sırada Rubble geldi. "Bu armutlar benim için mi, Chase?" diye sordu Rubble. "Evet, Rubble, hepsi senin için," dedi Chase. Rubble bir armut aldı ve mutlu mutlu yedi. Chase çok sevindi, çünkü sürprizi arkadaşını mutlu etmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sevimli bir armut sepeti"
   - Cümle 2: «Chase kamp yerinde Rubble için sevimli bir armut sepeti hazırlamıştı.»
   - Açıklama: 'Sevimli' bir sepet için uygun sıfat değil.
   - Açıklama: 'Sevimli' sıfatı bir sepete uygun düşmüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kampın kurallarına göre"
   - Cümle 5: «Kampın kurallarına göre yere düşen meyve önce yıkanırdı.»
   - Açıklama: 'Kurallarına göre' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0085` birebir aynı, `@degisim: fırçalamak -> yıkamak` (tutuyorsan), ardından `@onarim: c70055a8cf55b870edf332d83919b1a6d542b0e6`, sonra gövde.

### Hikâye 11: tohum chase-0086 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Marshall
@tohum: chase-0086
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: sırayla oynamak
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'raf', fiil 'dikmek', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Marshall
@plan: ikisi aynı anda attı ve toplar birbirine çarptı | kurallara uydu ve sırayla atmayı söyledi
@tohum: chase-0086
@degisim: raf -> top
Chase ile Marshall dağda kar topu oyunu oynuyordu. Hedef, Chase'in kara diktiği bir daldı. Ama ikisi aynı anda attı ve toplar havada birbirine çarptı. Oyunun bir kuralı vardı, herkes sırayla atardı. "Sırayla atalım, Marshall," dedi Chase. "Olur, önce sen at," dedi Marshall. Chase attı ve topu dala değdi. Marshall'ın topu ise çok uzağa gitti. Marshall karda yuvarlandı ve güldü. Çalışkan Marshall hemen yeni toplar yaptı. Bu kez dalı o vurdu. Chase ile Marshall çok mutluydu, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hedef, Chase'in kara"
   - Cümle 2: «Hedef, Chase'in kara diktiği bir daldı.»
   - Açıklama: 'Hedef' kelimesi 3 yaşındaki bir çocuk için soyut ve zor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "toplar havada birbirine çarptı"
   - Cümle 3: «Ama ikisi aynı anda attı ve toplar havada birbirine çarptı.»
   - Açıklama: Kar toplarının havada çarpışması çocuğun önemseyeceği gerçek bir sorun değil, zararsız ve önemsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0086` birebir aynı, `@degisim: raf -> top` (tutuyorsan), ardından `@onarim: eea701fce203fee55fddcffd48186035f304ffa9`, sonra gövde.

### Hikâye 12: tohum chase-0088 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0088
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'sürahi', fiil 'kokmak', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: kar taneleri sıcak sütün içine düşüyordu | mavi şapkasını sürahiye kapak gibi koydu
@tohum: chase-0088
Dağda büyük kar taneleri yağıyordu. Chase'in yanında sıcacık süt dolu bir sürahi vardı. Ama kar taneleri açık sürahiye, sütün içine düşüyordu. Süt böyle soğumaya başlamıştı. Sürahinin bir kapağı da yoktu. Chase mavi şapkasını çıkardı. Şapkayı sürahiye kapak gibi koydu. Kar taneleri artık şapkanın üstüne düşüyordu. Chase onları tek tek saydı ve güldü. Biraz sonra şapkayı kaldırdı ve yeniden taktı. Süt yine sıcaktı ve güzel kokuyordu. Chase sütünü yavaş yavaş içti ve karı mutlu mutlu seyretti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Süt böyle soğumaya başlamıştı"
   - Cümle 4: «Süt böyle soğumaya başlamıştı.»
   - Açıklama: 'Böyle' yanlış anlamda kullanılmış; 'bu yüzden' kastediliyor.
   - Açıklama: 'Böyle' kelimesi bu cümlede anlamsız ve belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0088` birebir aynı, ardından `@onarim: 0fdf9d4158f318b4fd5c39a173017d9ebe270ae2`, sonra gövde.
