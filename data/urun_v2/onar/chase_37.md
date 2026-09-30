# Editör görevi (onarım): Chase, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0132 (deneme 3 -> 4)

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
@plan: havuç yere düştü ve kirlendi | kirli havucu yemedi, önce yıkadı sonra tattı
@tohum: chase-0132
Kulübenin önünde Marshall, Chase'e turuncu bir havuç getirdi. Chase havucu daha önce hiç yememişti. Ama Marshall tökezledi ve havuç toprağa düştü. Chase havuca burnuyla dokundu ve toprağı gördü. Chase bir kural biliyordu ve kirli havucu hemen yemedi. "Marshall, suyu açar mısın?" diye sordu Chase. Marshall musluğu açtı ve borudan su aktı. Chase havucu suyun altında tuttu ve yıkadı. Havuç tertemiz oldu. Chase ilk ısırığı aldı ve "Çok tatlı!" dedi. Chase çok sevindi, çünkü yeni bir yiyeceği denemişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bir kural biliyordu"
   - Cümle 5: «Chase bir kural biliyordu ve kirli havucu hemen yemedi.»
   - Açıklama: Hangi kural olduğu söylenmeyen 'kural' soyut bir kavram ve 3 yaşındaki çocuğa belirsiz kalıyor.
   - Açıklama: Hangi kural olduğu söylenmeyen 'kural' soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0132` birebir aynı, ardından `@onarim: d6d9248153ed289de1ed4f44ff6a0a65696d26be`, sonra gövde.

### Hikâye 2: tohum chase-0133 (deneme 3 -> 4)

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
@plan: rüzgar döndü ve uçurtmanın ipi karmakarışık oldu | ipi çekmedi ve düğümleri yavaşça açtı
@tohum: chase-0133
@degisim: yatak -> uçurtma
Rüzgar hafifçe esiyordu. Chase kumsalda kırmızı bir uçurtma uçuruyordu. Birden rüzgar döndü ve uçurtmanın ipi karmakarışık oldu. Uçurtma yavaşça kuma indi. Chase ipi hemen çekmek istedi. Ama Chase bir kural biliyordu ve ipi çekmedi. Çekince düğümler daha sıkı olurdu. Chase ipe yakından baktı ve üç düğüm gördü. Düğümleri patisiyle ve dişleriyle tek tek açtı. Sonunda ip düzgün oldu. Chase ipi ağzıyla tuttu ve kumda koştu. Uçurtma yeniden havaya, bulutlara doğru yükseldi. Chase sevinçle havladı. Chase bundan sonra karışık ipleri hep yavaşça açtı.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase ipi hemen çekmek istedi. Ama Chase bir kural"
   - Cümle 5: «Chase ipi hemen çekmek istedi.»
   - Açıklama: Chase adı art arda cümlelerde gereksizce tekrarlanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bir kural biliyordu"
   - Cümle 6: «Ama Chase bir kural biliyordu ve ipi çekmedi.»
   - Açıklama: 'Kural' soyut bir kavram ve hangi kural olduğu somut olarak söylenmiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çekince düğümler daha sıkı olurdu"
   - Cümle 7: «Çekince düğümler daha sıkı olurdu.»
   - Açıklama: '-ince' zarf-fiili 'olurdu' şart kipiyle uyumsuz; 'Çekerse düğümler daha sıkı olurdu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0133` birebir aynı, `@degisim: yatak -> uçurtma` (tutuyorsan), ardından `@onarim: 923f64d2f50ea5d2b7cbc15c823a46d805eabf4a`, sonra gövde.

### Hikâye 3: tohum chase-0136 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0136
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'basamak', fiil 'yıkamak', sıfat 'pembe'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalgalar basamakları yıkamıştı ve hepsi kaygandı | kaygan yere basmadı ve kurumasını bekledi
@tohum: chase-0136
Chase bir sabah erkenden kumsala geldi. Gökyüzünde pembe bulutlar vardı ve Chase onlara iskelenin üstünden bakmak istedi. Ama dalgalar basamakları yıkamıştı ve hepsi çok kaygandı. Chase bir kural biliyordu ve kaygan yere basmadı. Kumun üstüne oturdu ve bekledi. Biraz sonra güneş çıktı ve her yer kurudu. Chase basamakları yavaş yavaş çıktı ve iskelenin ortasına yürüdü. Orada durdu ve pembe bulutlara uzun uzun baktı. Chase çok mutluydu, çünkü bulutlara ilk kez iskelenin üstünden bakmıştı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Biraz sonra güneş çıktı ve her yer kurudu"
   - Cümle 6: «Biraz sonra güneş çıktı ve her yer kurudu.»
   - Açıklama: Dalgaların yıkadığı basamaklar biraz sonra kuruyor ve güneş sonradan çıkıyor, ama şafağın pembe bulutları bu beklemeden sonra hâlâ yerinde duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0136` birebir aynı, ardından `@onarim: 31d4b77c7fdd405d4ebe510b8bbdd20abc89de30`, sonra gövde.

### Hikâye 4: tohum chase-0137 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0137
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kebap', fiil 'hazırlamak', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: arkadaşı sandviçleri koyduğu çalıyı bulamadı | burnuyla sandviçlerin kokusunu alıp onları buldu
@tohum: chase-0137
@degisim: kebap -> sandviç
Ormanda, kamp yerinde Chase ile Marshall bir piknik hazırlıyordu. Marshall sandviçleri gölgede bir çalının dibine koymuştu. Ama çalılar birbirine benziyordu ve Marshall onları bulamadı. "Çok acıktım, sandviçler nerede?" diye sordu Marshall. Chase burnunu yere yaklaştırdı ve havayı kokladı. Sonra kokunun geldiği yere yürüdü. Kabarık ekmekli sandviçler büyük bir çalının dibindeydi. "Buldum, Marshall, hepsi burada!" dedi Chase. Chase sandviçleri alıp Marshall'a getirdi. Marshall hemen bir sandviç yedi ve kuyruğunu salladı. Chase çok sevindi, çünkü aç arkadaşına yardım etmişti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve Marshall onları bulamadı"
   - Cümle 3: «Ama çalılar birbirine benziyordu ve Marshall onları bulamadı.»
   - Açıklama: 'Onları' en yakın çoğul olan 'çalılar'ı gösteriyor gibi, oysa sandviçler kastediliyor.
   - Açıklama: 'Onları' zamiri en yakın çoğul olan çalıları mı yoksa sandviçleri mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0137` birebir aynı, `@degisim: kebap -> sandviç` (tutuyorsan), ardından `@onarim: 334cbef20d107b36c7a5fe9b7f47c4139148c032`, sonra gövde.

### Hikâye 5: tohum chase-0138 (deneme 3 -> 4)

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
@plan: kütüklerin çoğu yağmurdan ıslanmıştı | kütükleri kokladı ve kuru bir kütük buldu
@tohum: chase-0138
@degisim: ilginç -> yüksek
Ormandaki kamp yerinde yağmur yeni durmuştu. Chase kendine kütükten bir koltuk yapmak istiyordu. Ama kütüklerin çoğu yağmurdan ıslanmıştı. Chase burnuyla kütükleri tek tek kokladı. Islak kütükler toprak gibi kokuyordu. Sonra büyük bir ağacın altında saklanmış bir kütük buldu. Bu kütük kuru odun kokuyordu. Kütüğün arkası yüksekti ve bir koltuğa benziyordu. Chase ağacın altındaki kuru yaprakları topladı. Yaprakları kütüğün üstüne yumuşak bir yatak gibi serdi. Sonra yeni koltuğuna rahatça oturdu. Chase çok mutluydu, çünkü kendi koltuğunu kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "altında saklanmış bir kütük"
   - Cümle 6: «Sonra büyük bir ağacın altında saklanmış bir kütük buldu.»
   - Açıklama: Kütük kendisi saklanamaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0138` birebir aynı, `@degisim: ilginç -> yüksek` (tutuyorsan), ardından `@onarim: b726449643db19d3236ae61b7fee755fb40ad7ab`, sonra gövde.

### Hikâye 6: tohum chase-0143 (deneme 3 -> 4)

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
@plan: koşunca bardaktaki su döküldü | bardağı yeniden doldurup yavaş yürümeyi söyledi
@tohum: chase-0143
@degisim: utangaç -> üzgün
Kulübelerin önünde Chase ile Skye küçük bir çiçeğe su taşıyordu. Ama Skye koştuğu için bardaktaki su hep dökülüyordu. "Çiçeğe hiç su kalmıyor," dedi Skye üzgün bir sesle. Chase bardağı musluktan yeniden doldurdu ve Skye'a verdi. "Su taşırken koşmak yok, Skye, bu bir kural," dedi Chase. Skye bardağı dikkatle tuttu ve yavaş yavaş yürüdü. Chase de onun yanında yürüdü. Bardaktaki su hiç dökülmedi. Skye suyu çiçeğe döktü. Skye bundan sonra su taşırken hiç koşmadı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu bir kural"
   - Cümle 5: «"Su taşırken koşmak yok, Skye, bu bir kural," dedi Chase.»
   - Açıklama: 'Kural' soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0143` birebir aynı, `@degisim: utangaç -> üzgün` (tutuyorsan), ardından `@onarim: 43428942bf1dbb1fb0914e86a5e04a6a2f3ee25a`, sonra gövde.

### Hikâye 7: tohum chase-0145 (deneme 3 -> 4)

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
Ağaçların arasında rüzgar hafif esiyordu. Chase ile Ryder kamp yerinde çeşmenin havuzunda yapraktan gemiyle deniz oyunu oynuyordu. Ama çeşme açık kalmıştı ve güçlü su gemiyi hep deviriyordu. "Gemim karşıya hiç gitmiyor," dedi Ryder. "Ryder, kamp yerinde kuralımız çeşmeyi kapatmak," dedi Chase. Chase patisiyle çeşmeyi kapattı. Havuzdaki su artık kıpırdamıyordu. Ryder gemiyi yeniden suya koydu. Gemi rahatça karşı kenara gitti. Ryder sevinçle Chase'e göz kırptı. Chase ile Ryder bundan sonra oyuna başlamadan önce çeşmeyi kapattılar.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "güçlü su gemiyi hep deviriyordu"
   - Cümle 3: «Ama çeşme açık kalmıştı ve güçlü su gemiyi hep deviriyordu.»
   - Açıklama: Suya 'güçlü' denmez; 'suyun akışı güçlüydü' gibi anlatılmalı.
   - Açıklama: Su 'güçlü' olmaz; 'hızlı akan su' gibi öznesine uygun bir söz gerekir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kamp yerinde kuralımız çeşmeyi kapatmak"
   - Cümle 5: «"Ryder, kamp yerinde kuralımız çeşmeyi kapatmak," dedi Chase.»
   - Açıklama: 'Kural' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0145` birebir aynı, ardından `@onarim: ac72cc163ed973d9090c5cea287f84ab080a3209`, sonra gövde.

### Hikâye 8: tohum chase-0146 (deneme 3 -> 4)

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
@plan: yerde tek değnek vardı ve ikisi de çizmek istedi | değneği ikiye böldü ve bir parçasını verdi
@tohum: chase-0146
Chase ile Marshall kamp yerinde toprağa resim çizmek istedi. Etrafta kokulu çam ağaçları vardı. Ama kamp yeri temizdi ve yerde yalnız bir değnek vardı. Marshall evdeki yüksek kuleyi özlemişti. "Hadi ağaçtan yeni bir dal koparalım," dedi Marshall. "Olmaz, Marshall, kurallara göre dal koparmak yok," dedi Chase. Chase değneği ikiye böldü. "Gel, bunu paylaşalım," dedi Chase ve bir parçasını Marshall'a verdi. Marshall toprağa büyük bir kule çizdi. Chase de yanına küçük bir kulübe çizdi. Marshall kuyruğunu mutlu mutlu salladı. Değneği paylaşınca ikisi de resim çizdi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Marshall evdeki yüksek kuleyi özlemişti"
   - Cümle 4: «Marshall evdeki yüksek kuleyi özlemişti.»
   - Açıklama: Kuleyi özleme ayrıntısı sorunla çözüm arasına sebepsizce giriyor ve olaydan çıkmıyor.
   - Açıklama: Evdeki kuleyi özleme ayrıntısı sebepsiz beliriyor ve sorunla ya da çözümle bağı yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurallara göre dal koparmak"
   - Cümle 6: «"Olmaz, Marshall, kurallara göre dal koparmak yok," dedi Chase.»
   - Açıklama: 'Kurallara göre' soyut bir ifade; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Kurallara göre' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0146` birebir aynı, ardından `@onarim: ead2816a78afbc7ea2033c9b3268d78316846b14`, sonra gövde.

### Hikâye 9: tohum chase-0149 (deneme 2 -> 3)

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
@plan: rüzgar teşekkür kartını yüksek bir kayaya savurdu | kayaya tırmanmadı ve yardım istedi
@tohum: chase-0149
@degisim: posta -> kart
Bir sabah Chase dağda yardımsever Skye için bir teşekkür kartı yapıyordu. Birden rüzgar kartı savurdu ve kart yüksek bir kayanın üstüne düştü. Kurallara göre Chase yüksek kayaya tırmanmadı. "Skye, kartım kayanın üstünde kaldı, yardım eder misin?" dedi Chase. "Hemen geliyorum, Chase!" dedi Skye. Skye helikopteriyle kayanın üstüne uçtu. Helikopterin rüzgarı kartı aşağı itti. Chase kartı karın üstünden aldı. Skye helikopteri indirdi ve yanına geldi. Chase kartı hemen Skye'a verdi. Skye çok sevindi, çünkü o güzel kart kendisi içindi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurallara göre Chase yüksek"
   - Cümle 3: «Kurallara göre Chase yüksek kayaya tırmanmadı.»
   - Açıklama: 'Kurallara göre' soyut bir kavram; hangi kural olduğu da belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kartı karın üstünden aldı"
   - Cümle 8: «Chase kartı karın üstünden aldı.»
   - Açıklama: Kar daha önce hiç kurulmadan sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0149` birebir aynı, `@degisim: posta -> kart` (tutuyorsan), ardından `@onarim: cc6e349ad85f44703c99316cffcbcdfadee4336f`, sonra gövde.

### Hikâye 10: tohum chase-0150 (deneme 2 -> 3)

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
Parkta hava sisliydi. Chase çiçeklere bakma oyunu oynuyordu ve suyla dolu bir testi taşıyordu. Ama testi ıslak ve kaygandı, Chase onu ağzıyla tutamıyordu. Parktaki küçük çiçeklerin toprağı çok kuruydu. Chase çiçekler büyüsün diye onlara su götürmek istiyordu. Chase biraz düşündü. Sonra mavi şapkasını çıkardı ve yere ters koydu. Testiyi burnuyla şapkanın içine itti. Şapkanın kenarını ağzıyla tuttu ve dikkatle yürüdü. Testi bu kez hiç kaymadı. Chase çiçeklerin yanına varınca testiyi yavaşça eğdi. Su aktı ve toprak ıslandı. Chase bundan sonra kaygan şeyleri hep böyle taşıdı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "suyla dolu bir testi taşıyordu"
   - Cümle 2: «Chase çiçeklere bakma oyunu oynuyordu ve suyla dolu bir testi taşıyordu.»
   - Açıklama: Chase testiyi taşıyor deniyor ama hemen ardından onu ağzıyla tutamadığı söyleniyor.
   - Açıklama: Chase testiyi taşıyor deniyor, hemen ardından onu ağzıyla tutamadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0150` birebir aynı, ardından `@onarim: 86c5abfc5977b64b8fb7e634e20c868502536822`, sonra gövde.

### Hikâye 11: tohum chase-0151 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: çan gibi sesin nereden geldiğini bulamadı | şapkasına baktı ve kenarındaki buzları gördü
@tohum: chase-0151
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken çan gibi bir ses duydu. Ama sesin nereden geldiğini bulmak çok zordu. Chase kayaların arkasına ve ağaçların altına baktı. Ama orada hiçbir şey yoktu. Chase yürüdükçe ses de hep onunla geliyordu. Chase durunca ses de duruyordu. Chase başını salladı ve homurdandı. Ses bu kez tam başının üstünden geldi. Chase mavi şapkasını çıkardı ve ona baktı. Şapkanın kenarında küçük buz parçaları asılıydı. Buzlar birbirine değiyor ve o sesi çıkarıyordu. Chase çok sevindi, çünkü sesi yapan buzları kendi şapkasında bulmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase durunca ses de duruyordu"
   - Cümle 7: «Chase durunca ses de duruyordu.»
   - Açıklama: Art arda cümleler gereksiz yere hep 'Chase' adıyla başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0151` birebir aynı, ardından `@onarim: 080e602ea50d88f994984a935ace6ad36aef1c5b`, sonra gövde.

### Hikâye 12: tohum chase-0156 (deneme 2 -> 3)

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
@plan: ikisi aynı anda attı ve kozalaklar havada çarpıştı | sırayla atmayı önerdi ve kozalaklar şapkaya girdi
@tohum: chase-0156
@degisim: sakız -> kozalak
Chase ile Rubble uyanıktı ve sabah erkenden ormandaki kamp yerinde oynuyordu. İkisi kozalakları, Chase'in kütüğe koyduğu mavi şapkaya atıyordu. Ama hep aynı anda atıyorlardı ve kozalaklar havada birbirine çarpıyordu. "Hiçbiri şapkaya girmedi!" dedi Rubble. Chase biraz düşündü. "Sırayla atalım, önce sen, Rubble," dedi Chase. Rubble attı ve kozalak şapkanın içine düştü. Sonra Chase attı ve onun kozalağı da içeri girdi. İkisi oyunu sırayla birkaç kez tekrarladı. Az sonra şapka doldu. "Kamp yerinde sırayla oynamak çok eğlenceli, Chase!" dedi Rubble.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Rubble uyanıktı ve sabah"
   - Cümle 1: «Chase ile Rubble uyanıktı ve sabah erkenden ormandaki kamp yerinde oynuyordu.»
   - Açıklama: 'Uyanıktı' gereksiz ve iki anlamlı (uyanık/kurnaz), cümlede yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0156` birebir aynı, `@degisim: sakız -> kozalak` (tutuyorsan), ardından `@onarim: 9941860528b4d3811747f1d1912ad6006d5e84c1`, sonra gövde.
