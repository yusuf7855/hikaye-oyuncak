# Editör görevi (onarım): Chase, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar32.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0028 (deneme 4 -> 5)

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
@plan: kovanın dibi delikti ve kum dökülüyordu | şapkasını kumla doldurup kule yaptı
@tohum: chase-0028
@degisim: dondurma -> yaprak
Rüzgar esiyordu ve kuru yapraklar çıtır çıtır ses çıkarıyordu. Chase parktaki kum havuzunda bir kum kulesi yapmak istedi. Ama oradaki kovanın dibi delikti ve kum hemen dökülüyordu. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı kumla doldurdu ve patileriyle iyice bastırdı. Sonra şapkayı ters çevirdi ve yavaşça yukarı çekti. Kumdan küçük bir kule çıktı ve dimdik durdu. Chase şapkayı silkeledi ve yine başına taktı. Sonra kulenin yanına iki kule daha yaptı. Chase kum oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şapkasını kumla doldurup kule yaptı"
   - Cümle 0 (plan satırı): «kovanın dibi delikti ve kum dökülüyordu | şapkasını kumla doldurup kule yaptı»
   - Açıklama: Plan şapkanın kumla doldurulduğunu söylüyor ama gövdede bu adım yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0028` birebir aynı, `@degisim: dondurma -> yaprak` (tutuyorsan), ardından `@onarim: 68432ca4dc1238ffe486fdf432a6fd34ab36f3e1`, sonra gövde.

### Hikâye 2: tohum chase-0102 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0102
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yağmur ya da kar günü
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'peynir', fiil 'gıdıklamak', sıfat 'açık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: arkadaşı çadıra koşarken yemek torbasını otlara düşürdü | peynir kokusunu izleyip torbayı buldu
@tohum: chase-0102
@degisim: gıdıklamak -> ıslanmak
Yağmur hızlı hızlı yağıyordu. Chase ile Skye kamp yerinde çadırın içinde oturuyordu. Ama Skye koşarken peynirli ekmek torbasını otlara düşürmüştü. "Chase, torbamı otların arasında göremiyorum!" dedi Skye. Chase çadırın açık kapısından havayı kokladı. Peynir kokusu büyük ağacın altından geliyordu. Chase oraya koştu ve torbayı otların arasında buldu. Torbayı ağzıyla alıp hemen çadıra getirdi. Torba ağacın altında olduğu için hiç ıslanmamıştı. "Teşekkürler, Chase, şimdi birlikte yiyelim!" dedi Skye. İkisi ekmekleri çadırda mutlu mutlu yedi. Chase bundan sonra kaybolan bir şeyi önce burnuyla aradı.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Chase bundan sonra kaybolan bir şeyi önce burnuyla aradı"
   - Cümle 12: «Chase bundan sonra kaybolan bir şeyi önce burnuyla aradı.»
   - Açıklama: 'bundan sonra' ile tek seferlik -dı uyumsuz; 'arardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0102` birebir aynı, `@degisim: gıdıklamak -> ıslanmak` (tutuyorsan), ardından `@onarim: e6d9572f873414e1006faa89fa4e6aad53994931`, sonra gövde.

### Hikâye 3: tohum chase-0105 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0105
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'hazine', fiil 'oturmak', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: rüzgar haritayı uçurdu ve hazinenin yeri bilinmedi | kuralı hatırlayıp kum havuzunda hazineyi buldu
@tohum: chase-0105
Rüzgar serin serin esiyordu. Chase ile Skye parkta hazine avı oynuyordu. Ama rüzgar Skye'ın çizdiği haritayı uçurdu. Chase artık hazinenin yerini bilmiyordu. Oyunun başında ikisi bir kural koymuştu: hazine yalnız kum havuzunda olacaktı. Chase bu kuralı hatırladı ve kum havuzuna koştu. Çimenlerde ve çiçeklerde hiç aramadı. Kumu patileriyle dikkatle kazdı. Sonunda bir köşede küçük bir kutu buldu. İkisi havuzun yanındaki uzun banka oturdu. Kutuyu açtılar ve içinde renkli taşlar gördüler. Sonra hazineyi Chase sakladı ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hazinenin yeri bilinmedi"
   - Cümle 0 (plan satırı): «rüzgar haritayı uçurdu ve hazinenin yeri bilinmedi | kuralı hatırlayıp kum havuzunda hazineyi buldu»
   - Açıklama: Süren bir durum için 'bilinmedi' uyumsuz; 'bilinmiyordu' olmalı.
   - Açıklama: Plan satırında zaman uyumsuz; 'hazinenin yeri bilinmiyordu' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar Skye'ın çizdiği haritayı uçurdu"
   - Cümle 3: «Ama rüzgar Skye'ın çizdiği haritayı uçurdu.»
   - Açıklama: Haritayı Skye çizdiği için hazinenin yerini zaten biliyor olmalı, sorun akla yatkın değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "hazine yalnız kum havuzunda olacaktı"
   - Cümle 5: «Oyunun başında ikisi bir kural koymuştu: hazine yalnız kum havuzunda olacaktı.»
   - Açıklama: Hazinenin yeri baştan kuralla biliniyor ve haritayı Skye çizdiği için yer bilinmiyor sorunu akla yatkın değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyunun başında ikisi bir kural koymuştu"
   - Cümle 5: «Oyunun başında ikisi bir kural koymuştu: hazine yalnız kum havuzunda olacaktı.»
   - Açıklama: Çözümü getiren kural önceden kurulmadan tam gerektiği anda sebepsizce beliriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İkisi havuzun yanındaki uzun banka oturdu"
   - Cümle 10: «İkisi havuzun yanındaki uzun banka oturdu.»
   - Açıklama: Bank ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0105` birebir aynı, ardından `@onarim: 97744672c9f8ea73791abb726f6b0f3964727e15`, sonra gövde.

### Hikâye 4: tohum chase-0110 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0110
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kristal', fiil 'tamamlanmak', sıfat 'düşünceli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: arkadaşının kristali çimenlere düştü ve kayboldu | kutudaki kristali bulup arkadaşına verdi
@tohum: chase-0110
Chase kamp yerinde Marshall'ın yanına geldi. Marshall çadırın önünde taşlardan küçük bir kule yapıyordu. Ama kulenin en üstündeki kristal çimenlere düşmüş ve kaybolmuştu. Marshall düşünceli düşünceli yere bakıyordu. "Chase, kristal taşım hiçbir yerde yok," dedi Marshall. Chase biraz önce çimenlerde parlak bir taş bulmuştu. Kampta bir kural vardı: yerde bir şey bulan onu büyük kutuya koyardı. Chase de taşı hemen o kutuya koymuştu. İkisi hemen kutunun yanına koştu. Kristal kutunun içinde duruyordu. Marshall kristali kulenin en üstüne koydu. Böylece kule tamamlandı. Chase çok sevindi, çünkü arkadaşının kristalini bulmuştu.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kutudaki kristali bulup arkadaşına verdi"
   - Cümle 0 (plan satırı): «arkadaşının kristali çimenlere düştü ve kayboldu | kutudaki kristali bulup arkadaşına verdi»
   - Açıklama: Gövdede Chase kristali arkadaşına vermiyor; ikisi kutuya koşuyor ve kristali Marshall kendisi alıp kuleye koyuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Marshall düşünceli düşünceli yere"
   - Cümle 4: «Marshall düşünceli düşünceli yere bakıyordu.»
   - Açıklama: 'Düşünceli' soyut bir durum kelimesi, 3 yaşındaki çocuk bilmeyebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kampta bir kural vardı"
   - Cümle 7: «Kampta bir kural vardı: yerde bir şey bulan onu büyük kutuya koyardı.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kampta bir kural vardı"
   - Cümle 7: «Kampta bir kural vardı: yerde bir şey bulan onu büyük kutuya koyardı.»
   - Açıklama: Daha önce hiç kurulmamış bir kural ve Chase'in önceden taşı kutuya koyması çözümü sebepsizce getiriyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "İkisi hemen kutunun yanına"
   - Cümle 9: «İkisi hemen kutunun yanına koştu.»
   - Açıklama: 'Hemen' art arda iki cümlede gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0110` birebir aynı, ardından `@onarim: 5e194cde084baac0c8a7a49ec45c4d683d88f07c`, sonra gövde.

### Hikâye 5: tohum chase-0112 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0112
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'baston', fiil 'uçuşmak', sıfat 'tertemiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: yapraklar küçük köpeğin kemiğini örttü | şapkasıyla yaprakları itip kemiği buldu
@tohum: chase-0112
@degisim: baston -> kemik
Rüzgar esiyordu ve ormanda sarı yapraklar uçuşuyordu. Chase ile Skye kamp yerinde küçük bir köpek gördü. Köpek çok açtı ama yapraklar kemiğinin üstünü örtmüştü. Skye yere baktı ama kemiği göremedi. Chase mavi şapkasını başından çıkardı. Şapkasıyla yaprakları hızlıca bir kenara itti. Altından tertemiz, büyük bir kemik çıktı. Skye kemiği küçük köpeğin önüne koydu. Köpek kemiği patileriyle tuttu ve yemeye başladı. Chase ile Skye sevinçle birbirine baktı. Chase bundan sonra aç bir köpek görünce hemen yardım etti.
```

**Hakem bulguları (4):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "kamp yerinde küçük bir köpek gördü"
   - Cümle 2: «Chase ile Skye kamp yerinde küçük bir köpek gördü.»
   - Açıklama: Başlığın Yan alanında yalnız Skye var; kartın 'yanlar' bölümünde olmayan isimsiz bir köpek olaya katılıyor.
   - Açıklama: Başlıktaki Yan alanında ve kartın 'yanlar' bölümünde olmayan isimsiz bir köpek olaya katılıyor.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Köpek çok açtı"
   - Cümle 3: «Köpek çok açtı ama yapraklar kemiğinin üstünü örtmüştü.»
   - Açıklama: Aç ve sıkıntıdaki bir hayvan gösteriliyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "aç bir köpek görünce hemen yardım etti"
   - Cümle 11: «Chase bundan sonra aç bir köpek görünce hemen yardım etti.»
   - Açıklama: Tanımadığı bir köpeğe yaklaşıp yemek vermek taklit edilince tehlikeli bir davranış olarak öğütleniyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "görünce hemen yardım etti"
   - Cümle 11: «Chase bundan sonra aç bir köpek görünce hemen yardım etti.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor ama fiil tek seferlik geçmişte; 'yardım ederdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0112` birebir aynı, `@degisim: baston -> kemik` (tutuyorsan), ardından `@onarim: 844363d114afef3bd4bc15732f4608a3a3ca9da8`, sonra gövde.

### Hikâye 6: tohum chase-0113 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0113
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'mücevher', fiil 'çıkarmak', sıfat 'koyu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: küçük bir köpek açtı ama mama için kap yoktu | şapkasını çıkarıp ters çevirdi ve kap yaptı
@tohum: chase-0113
@degisim: mücevher -> mama
Kulübelerin önünde rüzgar esiyordu. Chase ile Skye orada küçük, aç bir köpek gördü. Kulübenin yanında bir torba mama vardı ama hiç boş kap yoktu. "Chase, bu küçük köpek çok aç!" dedi Skye. Chase mavi şapkasını çıkardı ve ters çevirdi. Skye koyu kahverengi mamaları şapkanın içine koydu. Chase şapkayı yavaşça küçük köpeğin önüne itti. Küçük köpek mamaları hemen yedi ve kuyruğunu salladı. "Aferin, Chase, köpeğin karnı doydu!" dedi Skye. Chase bundan sonra kulübenin önüne hep boş bir kap koydu.
```

**Hakem bulguları (3):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "orada küçük, aç bir köpek gördü"
   - Cümle 2: «Chase ile Skye orada küçük, aç bir köpek gördü.»
   - Açıklama: Başlıktaki Yan alanında yalnız Skye var; küçük aç köpek başlıkta ve kartın yanlar bölümünde yok.
   - Açıklama: Başlıktaki Yan alanında ve kartın 'yanlar' bölümünde olmayan isimsiz bir köpek olaya katılıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "orada küçük, aç bir köpek gördü"
   - Cümle 2: «Chase ile Skye orada küçük, aç bir köpek gördü.»
   - Açıklama: Kapalı dünyada kartın yanlar bölümünde olmayan yeni bir köpek karakteri olaya katılıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "şapkayı yavaşça küçük köpeğin önüne itti"
   - Cümle 7: «Chase şapkayı yavaşça küçük köpeğin önüne itti.»
   - Açıklama: Tanınmayan sahipsiz bir köpeğe yaklaşıp onu beslemek çocuk için taklit edilince tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0113` birebir aynı, `@degisim: mücevher -> mama` (tutuyorsan), ardından `@onarim: 9ff505114408dfe9e1f4571b74e44b2c0e31588e`, sonra gövde.

### Hikâye 7: tohum chase-0116 (deneme 2 -> 3)

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
Chase kulübesinin önünde Rubble ile oynuyordu. Birden Rubble acıktı ve mama kabına koştu. Kap boştu ve bisküvi kutusu da yerinde yoktu. Kulübeler boyanırken kutu başka bir yere konmuştu. Her yer boya kokuyordu ama Chase havayı dikkatle kokladı. Havada tatlı bir bisküvi kokusu da vardı. Chase bu kokunun peşinden kulenin kapısına yürüdü. Rubble kutunun orada olduğuna inanmadı ama yine de Chase ile gitti. Kutu gerçekten kapının arkasındaydı. İçinde tek bir büyük bisküvi kalmıştı. Chase bisküviyi ikiye böldü ve yarısını Rubble'a verdi. İkisi bisküvilerini yedi ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "kokunun peşinden kulenin kapısına yürüdü"
   - Cümle 7: «Chase bu kokunun peşinden kulenin kapısına yürüdü.»
   - Açıklama: Hikaye kulübenin önünde başlıyor, sonra kulenin kapısına geçiyor; tek sahne kuralı zorlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rubble kutunun orada olduğuna inanmadı"
   - Cümle 8: «Rubble kutunun orada olduğuna inanmadı ama yine de Chase ile gitti.»
   - Açıklama: Rubble'ın inanmaması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0116` birebir aynı, `@degisim: sakar -> boş` (tutuyorsan), ardından `@onarim: c64c59526aa515f79dcafc30d46c87da8bcea2df`, sonra gövde.

### Hikâye 8: tohum chase-0117 (deneme 2 -> 3)

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
@plan: havuç derin karın içinde kayboldu | kokusunu alıp karı kazmak için yardım istedi
@tohum: chase-0117
@degisim: nota -> havuç
Karlı dağda Chase ile Ryder karşılaştı. İkisi birlikte kardan bir köpek yaptı. Ryder ona burun olarak havuç takarken havuç elinden kaydı. Havuç derin karın içinde kayboldu ve kardan köpeğin yüzü boş kaldı. Chase burnunu karın üstüne yaklaştırdı ve kokladı. Havucun kokusu küçük bir kayanın yanından geliyordu. Ama havuç çok aşağıdaydı ve Chase onu tek başına çıkaramadı. "Ryder, havuç burada, yardım eder misin?" diye sordu Chase. "Tabii, Chase," dedi Ryder. İkisi karı birlikte kazdı. Chase havucu ağzıyla aldı ve Ryder'a verdi. Ryder onu yeniden yerine taktı. Sonra ikisi kardan köpeğin etrafında mutlu mutlu koşup oynadı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Havuç derin karın içinde kayboldu"
   - Cümle 4: «Havuç derin karın içinde kayboldu ve kardan köpeğin yüzü boş kaldı.»
   - Açıklama: Havucun kaybolduğu sorunu ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Havuç derin karın içinde kayboldu ve kardan köpeğin yüzü boş kaldı.»
   - Açıklama: İlk üç cümlede havuç yalnız elden kayıyor; havucun karda kaybolduğu sorun ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0117` birebir aynı, `@degisim: nota -> havuç` (tutuyorsan), ardından `@onarim: 8a58bec137106c76b00be8adf4f71cc72a37bb52`, sonra gövde.

### Hikâye 9: tohum chase-0118 (deneme 2 -> 3)

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
@degisim: çikolatalı -> büyük
Parkta kuşlar ötüyordu ve Chase ile Rubble bankta oturuyordu. Rubble çantasından büyük bir sebze turtası çıkardı. Chase sebze turtasını hiç denememişti ve ondan biraz çekiniyordu. "Chase, bu turta çok güzel, bir dene," dedi Rubble. Chase önce turtayı burnuyla dikkatle kokladı. İçinden havuç ve peynir kokusu geldi. "Peyniri çok severim," dedi Chase ve küçük bir ısırık aldı. Turta yumuşak ve sıcaktı. "Bu turta çok lezzetli!" dedi Chase. Rubble bunu duyunca sevinçle güldü. Sonra ikisi turtayı birlikte bitirdi. Karınları doyunca ikisi parkta mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ondan biraz çekiniyordu"
   - Cümle 3: «Chase sebze turtasını hiç denememişti ve ondan biraz çekiniyordu.»
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmez.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "turtayı burnuyla dikkatle kokladı"
   - Cümle 5: «Chase önce turtayı burnuyla dikkatle kokladı.»
   - Açıklama: 'Burnuyla kokladı' gereksiz tekrar; koklamak zaten burunla yapılır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0118` birebir aynı, `@degisim: çikolatalı -> büyük` (tutuyorsan), ardından `@onarim: b30b685d8c363bc3b6d677ddf14e58eb003bbb2f`, sonra gövde.

### Hikâye 10: tohum chase-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Marshall
@tohum: chase-0119
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'yüzük', fiil 'kirletmek', sıfat 'incecik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | ev | Marshall
@plan: saklambaç oynayan arkadaşı saklandı ve bulunamadı | burnuyla kokusunu alıp onu buldu
@tohum: chase-0119
@degisim: yüzük -> pasta
Kulenin önünde rüzgar esiyordu. Chase, Marshall'ın doğum günü için gizlice bir pasta hazırlamıştı. Ama saklambaç oynayan Marshall iyi saklanmıştı ve Chase onu bulamıyordu. Chase burnunu yere yaklaştırdı ve kokladı. Marshall'ın kokusu kulenin arkasından geliyordu. Chase oraya koştu ve Marshall'ı bir kutunun arkasında buldu. "Seni buldum, Marshall! Sana bir sürprizim var," dedi Chase. Chase pastayı getirdi ve incecik dilimlere böldü. Marshall pastayı kirletmemek için tozlu patilerini sildi. Sonra ikisi birlikte pastayı yedi. "Bu çok güzel bir sürpriz, teşekkürler, Chase!" dedi Marshall.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Kulenin önünde rüzgar esiyordu"
   - Cümle 1: «Kulenin önünde rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye kulenin önünde başlıyor.
   - Açıklama: Başlıktaki yer ev iken hikaye kulenin önünde başlıyor ve orada geçiyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Marshall'ın doğum günü için gizlice bir pasta hazırlamıştı"
   - Cümle 2: «Chase, Marshall'ın doğum günü için gizlice bir pasta hazırlamıştı.»
   - Açıklama: Saklambaçta Marshall'ı bulma sorununun yanında ayrı bir doğum günü sürprizi hedefi var.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Marshall'ın doğum günü için gizlice bir pasta hazırlamıştı"
   - Cümle 2: «Chase, Marshall'ın doğum günü için gizlice bir pasta hazırlamıştı.»
   - Açıklama: Pasta saklambaç sorunuyla hiçbir bağı olmadan kuruluyor ve hikayeyi sorundan koparıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase pastayı getirdi ve incecik dilimlere böldü"
   - Cümle 9: «Chase pastayı getirdi ve incecik dilimlere böldü.»
   - Açıklama: Pasta sorundan çıkmıyor ve hikayenin sonunu saklambaçla ilgisiz bir olaya taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0119` birebir aynı, `@degisim: yüzük -> pasta` (tutuyorsan), ardından `@onarim: ecbe213d1a32df3a634e842cac6d862ea8b160f9`, sonra gövde.

### Hikâye 11: tohum chase-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0120
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'yıldız', fiil 'kurumak', sıfat 'siyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalga taşlardan yapılan yıldızı dağıttı | kurallara uydu ve oyununu sudan uzağa taşıdı
@tohum: chase-0120
Bir sabah Chase kumsalda oynuyordu. Siyah taşlarla kumun üstüne çok büyük bir yıldız yaptı. Ama bir dalga geldi ve taşları dağıttı. Chase'in patileri de ıslandı ve Chase güldü. Sonra Chase kurallara uydu ve oyununu sudan uzağa taşıdı. Taşları kurumuş kumun üstüne götürdü. Yıldızı orada yeniden yaptı. Sonra yıldızın bir ucundan öbür ucuna zıpladı. Dalgalar artık yıldıza gelmiyordu. Chase sevinçle havladı ve kuyruğunu salladı. Chase bundan sonra kumsalda hep sudan uzakta oynadı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve oyununu sudan uzağa taşıdı"
   - Cümle 5: «Sonra Chase kurallara uydu ve oyununu sudan uzağa taşıdı.»
   - Açıklama: 'Kurallara uymak' soyut ve 'oyununu taşıdı' mecazlı; hikayede kural da yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 5: «Sonra Chase kurallara uydu ve oyununu sudan uzağa taşıdı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve hangi kural olduğu somut değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Chase kurallara uydu"
   - Cümle 5: «Sonra Chase kurallara uydu ve oyununu sudan uzağa taşıdı.»
   - Açıklama: Hikayede hiç kurulmamış bir kural çözümü sebepsizce getiriyor.
   - Açıklama: Hikayede hiçbir kural kurulmadan çözüm sebepsizce kurallara bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0120` birebir aynı, ardından `@onarim: bd22cd36039a61c1a649d9d9f60219cd636bcbbc`, sonra gövde.

### Hikâye 12: tohum chase-0121 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0121
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'spagetti', fiil 'görünmek', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalgalar büyük kabuğu suyun altında bırakıyordu | kurallara uydu, suya girmedi ve bekledi
@tohum: chase-0121
@degisim: spagetti -> kabuk
Rüzgar esiyordu ve dalgalar kumsala geliyordu. Chase kumda büyük, parlak bir kabuk gördü ve onu almak istedi. Ama her dalga gelince kabuk suyun altında kalıyordu. Chase kurallara uydu ve suya girmedi. Kumun üstünde durdu ve dalganın geri gitmesini bekledi. Dalga geri gidince kabuk yeniden göründü. Chase hemen koştu ve kabuğu ağzıyla aldı. Kabuk biraz ağırdı ama Chase onu kuru kuma taşıdı. Chase kabuğa uzun uzun baktı ve çok sevindi. Chase bundan sonra kabuk toplarken hep dalganın gitmesini bekledi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase hemen koştu ve kabuğu ağzıyla aldı"
   - Cümle 7: «Chase hemen koştu ve kabuğu ağzıyla aldı.»
   - Açıklama: Dalgaların geldiği su kenarına dalga arasında koşmak çocuğun taklit edebileceği riskli bir davranış.
   - Açıklama: Dalga çekilince su kenarına koşup bir şey kapmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0121` birebir aynı, `@degisim: spagetti -> kabuk` (tutuyorsan), ardından `@onarim: 8a9c614ff68373352dfa9ce61a9fda160bb07098`, sonra gövde.
