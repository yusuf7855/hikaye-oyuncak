# Editör görevi (onarım): Chase, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0122 (deneme 2 -> 3)

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
@plan: rüzgar duvarları yıktı ve torba karın altında kaldı | elmaların kokusunu alıp torbayı buldu
@tohum: chase-0122
Karlı dağda Chase ile Ryder karla üç küçük duvar ördü. Oyun için Ryder sulu elmalarla dolu bir torbayı bir duvarın arkasına sakladı. Ama birden güçlü bir rüzgar esti ve duvarlar yıkıldı. Torba karın altında kaldı ve hiç görünmedi. "Chase, torbayı göremiyorum!" dedi Ryder. Chase burnunu yerde gezdirdi. Bir köşede tatlı bir elma kokusu aldı. Patileriyle orayı kazdı ve torbayı buldu. Ryder torbayı açtı ve Chase'e kocaman bir elma verdi. Chase elmayı mutlu mutlu yedi. "Teşekkürler, Chase, torbamızı sen buldun!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "güçlü bir rüzgar esti ve duvarlar yıkıldı"
   - Cümle 3: «Ama birden güçlü bir rüzgar esti ve duvarlar yıkıldı.»
   - Açıklama: Rüzgarın kar duvarlarını yıkması ve torbayı saklayan Ryder'ın yerini bilmemesi akla pek yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0122` birebir aynı, ardından `@onarim: f765135f3d71b99bf4d5c46899e96b0d4cc4ab22`, sonra gövde.

### Hikâye 2: tohum chase-0125 (deneme 2 -> 3)

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
@plan: rüzgar şapkayı uçurdu ve şapka kayaların arasında kayboldu | arkadaşından yardım istedi ve birlikte şapkayı aradılar
@tohum: chase-0125
@degisim: eşarp -> kaya
Rüzgar esiyordu ve gökyüzü bulutlarla kapalıydı. Chase ile Marshall karlı dağda dolaşıyordu. Birden rüzgar Chase'in mavi şapkasını uçurdu. Şapka büyük kayaların arasında kayboldu. Chase etrafa baktı ama şapkayı göremedi. "Marshall, bana yardım eder misin?" diye sordu Chase. İkisi kayaların arasına ayrı ayrı baktı. Sonunda Marshall karın üstünde mavi bir şey gördü. "Chase, şapkan burada!" dedi Marshall. Chase şapkasını aldı ve yeniden taktı. İkisi neşeyle yürümeye devam etti. Chase bundan sonra bir sorun olunca hemen arkadaşından yardım istedi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Birden rüzgar Chase'in mavi şapkasını uçurdu"
   - Cümle 3: «Birden rüzgar Chase'in mavi şapkasını uçurdu.»
   - Açıklama: Tohumdaki şapka özelliği çözümde işe yarar biçimde kullanılmıyor, yalnız kaybolan eşya oluyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi kayaların arasına ayrı ayrı baktı"
   - Cümle 7: «İkisi kayaların arasına ayrı ayrı baktı.»
   - Açıklama: İki yavru rüzgarlı karlı dağda büyükler olmadan kayaların arasında ayrı ayrı dolaşıyor; çocuk taklit edebilir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase şapkasını aldı ve yeniden taktı"
   - Cümle 10: «Chase şapkasını aldı ve yeniden taktı.»
   - Açıklama: Tohum özelliği şapka yalnız kaybolan nesne olarak geçiyor, çözüme işe yarar biçimde katkı vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0125` birebir aynı, `@degisim: eşarp -> kaya` (tutuyorsan), ardından `@onarim: 606adeb120d18c5c79405ee88da3e446c344ecbd`, sonra gövde.

### Hikâye 3: tohum chase-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: top yuvarlandı ve yumuşak karın içinde kayboldu | izlere bakıp kokusuyla topu buldu
@tohum: chase-0128
Rüzgar hafifçe esiyordu ve karlı dağda güneş parlıyordu. Chase ile Skye kırmızı bir topla oynuyordu. Birden top yokuştan aşağı yuvarlandı ve yumuşak karın içinde kayboldu. "Chase, topu bulabilir misin?" diye sordu Skye kibar bir sesle. Chase yerde küçük yuvarlak izler fark etti. İzler büyük bir meşe ağacının dibinde bitiyordu. Chase oraya yattı ve burnunu yerde gezdirdi. Bir köşeden topun kokusu geliyordu. Chase patileriyle orayı kazdı ve kırmızı topu buldu. "Teşekkürler, Chase!" dedi Skye ve sevinçle zıpladı. İkisi meşe ağacının yanında topla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bir köşeden topun kokusu"
   - Cümle 8: «Bir köşeden topun kokusu geliyordu.»
   - Açıklama: Açık karlı dağda köşe yok; 'köşe' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Açık karlı yerde ağaç dibinde 'köşe' yok; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0128` birebir aynı, ardından `@onarim: d80a41f6cf9afa8557867f4dbbcf82928417a4cd`, sonra gövde.

### Hikâye 4: tohum chase-0129 (deneme 2 -> 3)

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
@plan: top iskelenin altına kaçtı ve oraya girmek yasaktı | iskelenin altına girmedi ve yardım istedi
@tohum: chase-0129
@degisim: dosya -> kürek
Chase sıcak kumsalda Rubble'a yeni bir top oyunu öğretiyordu. Chase topa patisiyle vurdu ve top iskelenin altına kaçtı. Ama kumsalda iskelenin altına girmek yasaktı. Chase bu kurala uydu ve oraya girmedi. Chase iskelenin önünde durdu ve Rubble'dan yardım istedi. Rubble hemen kumda oynadığı sarı küreği getirdi. Chase küreği iskelenin altına doğru uzattı. Kürek topa değdi ve Chase topu yavaşça dışarı çekti. Rubble sevinçle zıpladı. Chase çok sevindi, çünkü top oyununu Rubble'a öğretmeye devam edebilirdi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bu kurala uydu"
   - Cümle 4: «Chase bu kurala uydu ve oraya girmedi.»
   - Açıklama: 'Kurala uymak' soyut bir kavram ve 3 yaşındaki çocuk için ağır bir ifade.
   - Açıklama: 'Kurala uymak' soyut bir kavram; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0129` birebir aynı, `@degisim: dosya -> kürek` (tutuyorsan), ardından `@onarim: 14bb2d9d821ca604517da2a9efbb7dc6d91b820c`, sonra gövde.

### Hikâye 5: tohum chase-0130 (deneme 2 -> 3)

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
Chase ormandaki kamp yerine geldi. Skye bir kütüğün üstünde yalnız oturuyordu ve kraker yiyordu. Birden yağmur başladı ama krakerlerin üstü açıktı. Skye krakerleri koruyacak bir şey bulamadı. Chase hemen mavi şapkasını çıkardı. Şapkayı onların üstüne kapattı. İkisi kütüğün yanında biraz bekledi. Kısa bir süre sonra yağmur dindi. Chase şapkayı kaldırdı ve krakerler kuruydu. Skye sevinçle bir kraker Chase'e uzattı. Chase de kütüğe oturup yemeğe katıldı ve ikisi krakerleri paylaştı. Chase bundan sonra arkadaşlarına hep böyle yardım etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yağmur başladı ama krakerlerin"
   - Cümle 3: «Birden yağmur başladı ama krakerlerin üstü açıktı.»
   - Açıklama: 'ama' karşıtlık bildirir, burada anlama uymuyor; 've' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şapkayı onların üstüne kapattı"
   - Cümle 6: «Şapkayı onların üstüne kapattı.»
   - Açıklama: 'onların' zamirinin krakerleri mi Skye'ı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0130` birebir aynı, ardından `@onarim: 30049f7a8da9acb1e42edced44ffdf98ad95aa7c`, sonra gövde.

### Hikâye 6: tohum chase-0132 (deneme 2 -> 3)

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
Kulübenin önünde güneş parlıyordu. Marshall, Chase'e turuncu bir havuç getirdi. Chase havucu daha önce hiç yememişti. Ama Marshall tökezledi ve havuç toprağa düştü. Chase havuca burnuyla dokundu ve toprağı gördü. Kirli havuç yemek yasaktı ve Chase kurallara uydu. "Marshall, suyu açar mısın?" diye sordu Chase. Marshall musluğu açtı ve borudan su aktı. Chase havucu suyun altında tuttu ve yıkadı. Havuç tertemiz oldu. Chase ilk ısırığı aldı ve "Çok tatlı!" dedi. Chase çok sevindi, çünkü yeni bir yiyeceği denemişti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Marshall tökezledi ve havuç toprağa düştü"
   - Cümle 4: «Ama Marshall tökezledi ve havuç toprağa düştü.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak 4. cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 6: «Kirli havuç yemek yasaktı ve Chase kurallara uydu.»
   - Açıklama: 'Kurallara uymak' ve 'yasak' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Yasak' ve 'kurallara uymak' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0132` birebir aynı, ardından `@onarim: 6dab4f49398cbbe385b2a1e316a62777d7f3dd5e`, sonra gövde.

### Hikâye 7: tohum chase-0133 (deneme 2 -> 3)

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
Rüzgar hafifçe esiyordu. Chase kumsalda kırmızı bir uçurtma uçuruyordu. Birden rüzgar döndü ve uçurtmanın ipi karmakarışık oldu. Uçurtma yavaşça kuma indi. Chase ipi hemen çekmek istedi. Ama karışık bir ipi çekmek yasaktı. Chase kurallara uydu ve ipi çekmedi. Sonra ipe yakından baktı ve üç düğüm gördü. Düğümleri patisiyle ve dişleriyle tek tek açtı. Sonunda ip düzgün oldu. Chase ipi ağzıyla tuttu ve kumda koştu. Uçurtma yeniden havaya, bulutlara doğru yükseldi. Chase sevinçle havladı. Chase bundan sonra dolaşan ipleri hep yavaşça açtı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karışık bir ipi çekmek yasaktı"
   - Cümle 6: «Ama karışık bir ipi çekmek yasaktı.»
   - Açıklama: Karışık ipi çekmek yasak değil, yalnızca doğru değil; 'yasak' kelimesi yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ipi çekmek yasaktı"
   - Cümle 6: «Ama karışık bir ipi çekmek yasaktı.»
   - Açıklama: 'Yasak' burada yanlış anlamda; ipi çekmek kural değil, ipi daha çok karıştırır.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "karışık bir ipi çekmek yasaktı"
   - Cümle 6: «Ama karışık bir ipi çekmek yasaktı.»
   - Açıklama: İpi çekmenin neden yasak olduğu söylenmiyor; kural sebepsiz beliriyor ve çözümü keyfi biçimde yönlendiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama karışık bir ipi çekmek yasaktı"
   - Cümle 6: «Ama karışık bir ipi çekmek yasaktı.»
   - Açıklama: Karışık ipi çekmenin yasak olması sebepsiz bir kural olarak beliriyor; ipi çekmemenin gerçek sebebi söylenmiyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dolaşan ipleri hep yavaşça"
   - Cümle 14: «Chase bundan sonra dolaşan ipleri hep yavaşça açtı.»
   - Açıklama: 'Dolaşan' yürüyüp gezen demektir; karışmış ip için 'dolaşık' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0133` birebir aynı, `@degisim: yatak -> uçurtma` (tutuyorsan), ardından `@onarim: 2cf1b955bf6d60bce0273a51824e2f5c46299817`, sonra gövde.

### Hikâye 8: tohum chase-0136 (deneme 2 -> 3)

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
@plan: dalgalar basamakları yıkamıştı ve hepsi kaygandı | kurallara uydu ve yavaş yavaş çıktı
@tohum: chase-0136
Chase bir sabah erkenden kumsala geldi. Gökyüzünde pembe bulutlar vardı. Chase onlara ilk kez iskelenin üstünden bakmak istedi. Ama dalgalar basamakları yıkamıştı ve hepsi çok kaygandı. Chase önce koşmak istedi. Sonra kurallara uydu ve ıslak yerde koşmadı. Her basamağa yavaş yavaş bastı. Hiç düşmeden yukarı çıktı. Chase iskelenin ortasında durdu ve bulutlara uzun uzun baktı. Güneş de denizin üstünde yavaşça yükseldi. Chase çok mutluydu, çünkü iskeleye ilk kez kendi başına çıkmıştı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama dalgalar basamakları yıkamıştı"
   - Cümle 4: «Ama dalgalar basamakları yıkamıştı ve hepsi çok kaygandı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak 4. cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra kurallara uydu"
   - Cümle 6: «Sonra kurallara uydu ve ıslak yerde koşmadı.»
   - Açıklama: Hangi kural olduğu söylenmeden geçen 'kurallara uymak' soyut bir anlatım.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "iskeleye ilk kez kendi başına çıkmıştı"
   - Cümle 11: «Chase çok mutluydu, çünkü iskeleye ilk kez kendi başına çıkmıştı.»
   - Açıklama: Deniz kıyısında kaygan iskele basamaklarına tek başına çıkmak çocuğun taklit edebileceği tehlikeli bir davranıştır.
   - Açıklama: Dalgaların ıslattığı kaygan iskele basamaklarına tek başına çıkmak övülüyor ve taklit edilince tehlikeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0136` birebir aynı, ardından `@onarim: f3e96b3f5724ce0b10a40b5e8a2ed624a54a09b7`, sonra gövde.

### Hikâye 9: tohum chase-0137 (deneme 2 -> 3)

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
@plan: küçük bir köpek kayboldu ve çalıların arasında görünmüyordu | burnuyla köpeğin kokusunu alıp onu buldu
@tohum: chase-0137
@degisim: kebap -> sandviç
Ormanda, kamp yerinde Chase ile Marshall bir piknik hazırlıyordu. Birden ağaçların arasından küçük bir köpeğin sesi geldi. Küçük köpek kaybolmuştu ve sık çalıların arasından görünmüyordu. "Onu nasıl bulacağız?" diye sordu Marshall. Chase burnunu yere yaklaştırdı ve köpeğin kokusunu aldı. Sonra kokunun geldiği yere yürüdü. Kabarık tüylü küçük köpek büyük bir çalının arkasındaydı. "Seni bulduk, küçük dost!" dedi Chase. Marshall piknikten küçük köpeğe bir sandviç verdi. Küçük köpek sandviçi yedi ve kuyruğunu salladı. Chase ile Marshall çok sevindi, çünkü kaybolan küçük köpeği bulmuşlardı.
```

**Hakem bulguları (7):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Küçük köpek kaybolmuştu ve"
   - Cümle 3: «Küçük köpek kaybolmuştu ve sık çalıların arasından görünmüyordu.»
   - Açıklama: Başlığın Yan alanında yalnız Marshall var; olaya katılan kayıp küçük köpek kartın 'yanlar' bölümünde yok.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Küçük köpek kaybolmuştu ve sık"
   - Cümle 3: «Küçük köpek kaybolmuştu ve sık çalıların arasından görünmüyordu.»
   - Açıklama: Başlıktaki Yan alanında yalnız Marshall var; küçük köpek kartın yanlar bölümünde olmayan ek bir karakter.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Küçük köpek kaybolmuştu ve"
   - Cümle 3: «Küçük köpek kaybolmuştu ve sık çalıların arasından görünmüyordu.»
   - Açıklama: Kartın kapalı dünyasında olmayan yeni bir köpek karakteri hikayeye ekleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Küçük köpek kaybolmuştu"
   - Cümle 3: «Küçük köpek kaybolmuştu ve sık çalıların arasından görünmüyordu.»
   - Açıklama: Küçük köpeğin neden kaybolduğu hiç söylenmiyor; sorunun sebebi yok.
5. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kabarık tüylü küçük köpek büyük"
   - Cümle 7: «Kabarık tüylü küçük köpek büyük bir çalının arkasındaydı.»
   - Açıklama: Kartın yanlar bölümünde olmayan yeni bir köpek karakteri hikayeye ekleniyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Marshall piknikten küçük köpeğe bir sandviç verdi"
   - Cümle 9: «Marshall piknikten küçük köpeğe bir sandviç verdi.»
   - Açıklama: Tanınmayan kayıp bir köpeğe yaklaşıp yiyecek vermek çocuğun taklit edebileceği riskli bir davranış.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Marshall piknikten küçük köpeğe"
   - Cümle 9: «Marshall piknikten küçük köpeğe bir sandviç verdi.»
   - Açıklama: Sandviç 'piknikten' değil piknik yiyeceklerinden ya da sepetinden verilir; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0137` birebir aynı, `@degisim: kebap -> sandviç` (tutuyorsan), ardından `@onarim: 5336d984af0f17c5f71ac409b32cc1d0609890bf`, sonra gövde.

### Hikâye 10: tohum chase-0138 (deneme 2 -> 3)

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
@degisim: ilginç -> yüksek
Ormandaki kamp yerinde yağmur yeni durmuştu. Chase kendine kütükten bir koltuk yapmak istiyordu. Ama bütün kütükler yağmurdan ıslanmıştı. Chase burnuyla kütükleri tek tek kokladı. Çoğu ıslak toprak kokuyordu. Sonra büyük bir ağacın altındaki bir kütükten kuru odun kokusu aldı. Ağacın kalın dalları bu kütüğü yağmurdan saklamıştı. Kütüğün arkası yüksekti ve bir koltuğa benziyordu. Chase ağacın altındaki kuru yaprakları topladı. Yaprakları kütüğün üstüne yumuşak bir yatak gibi serdi. Sonra yeni koltuğuna rahatça oturdu. Chase çok mutluydu, çünkü kendi koltuğunu kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bütün kütükler yağmurdan ıslanmıştı"
   - Cümle 3: «Ama bütün kütükler yağmurdan ıslanmıştı.»
   - Açıklama: Bütün kütüklerin ıslak olduğu söyleniyor ama sonra kuru bir kütük bulunuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu kütüğü yağmurdan saklamıştı"
   - Cümle 7: «Ağacın kalın dalları bu kütüğü yağmurdan saklamıştı.»
   - Açıklama: 'Saklamak' yanlış anlamda kullanılmış; dallar kütüğü yağmurdan 'korumuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0138` birebir aynı, `@degisim: ilginç -> yüksek` (tutuyorsan), ardından `@onarim: 22073439ccb3d96b12b3d97c777e01d923d75fb2`, sonra gövde.

### Hikâye 11: tohum chase-0142 (deneme 2 -> 3)

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
Chase kulübesinin önünde ilk kez köfte yemeyi deneyecekti. Köfteyi dikkatle inceledi. Ama köfte çok sıcaktı ve üstünden buhar çıkıyordu. Chase çabuk yemek istiyordu. Mavi şapkasını çıkardı ve köfteye doğru hızlı hızlı salladı. Buhar hemen azaldı. Köfte biraz soğudu ve ılık oldu. Chase köfteye burnuyla dokundu ve artık sıcak olmadığını anladı. Chase köfteyi yedi ve tadını çok beğendi. Sonra şapkasını yine başına taktı. Chase bundan sonra sıcak yemeği önce şapkasıyla serinletti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase köfteye burnuyla dokundu"
   - Cümle 8: «Chase köfteye burnuyla dokundu ve artık sıcak olmadığını anladı.»
   - Açıklama: Sıcak yemeğe burunla dokunarak sıcaklığını denemek çocuğun taklit edince yanabileceği bir davranış.
   - Açıklama: Sıcak yemeğe yüzle dokunarak sıcaklığı sınamak çocuğun taklit edebileceği tehlikeli bir davranış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Chase bundan sonra sıcak yemeği önce şapkasıyla serinletti"
   - Cümle 11: «Chase bundan sonra sıcak yemeği önce şapkasıyla serinletti.»
   - Açıklama: 'Bundan sonra' süreklilik bildirirken tek seferlik -dı kullanılmış; 'serinletirdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0142` birebir aynı, ardından `@onarim: 6f739852cedf44eac6e52bc7a51d2b33b02d216a`, sonra gövde.

### Hikâye 12: tohum chase-0143 (deneme 2 -> 3)

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
@plan: küçük köpek koştuğu için bardaktaki su döküldü | yavaş yürüyerek suyu dökmeden taşıdı
@tohum: chase-0143
@degisim: utangaç -> üzgün
Kulenin içinde Chase ile Skye küçük bir çiçeğe su taşıyordu. Ama Skye koştuğu için bardaktaki su hep dökülüyordu. "Çiçeğe hiç su kalmıyor," dedi Skye üzgün bir sesle. Chase bardağı musluktan yeniden doldurdu. "Su taşırken koşmak yok, Skye, bu bir kural," dedi Chase. Chase bardağı ağzıyla dikkatle tuttu ve yavaş yavaş yürüdü. Skye da onun yanında yürüdü. Bardaktaki su hiç dökülmedi. Chase bardağı Skye'a verdi ve Skye suyu çiçeğe döktü. Skye bundan sonra Chase gibi su taşırken hiç koşmadı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Kulenin içinde Chase ile Skye"
   - Cümle 1: «Kulenin içinde Chase ile Skye küçük bir çiçeğe su taşıyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye bir kulenin içinde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye kulenin içinde geçiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase bardağı ağzıyla dikkatle tuttu"
   - Cümle 6: «Chase bardağı ağzıyla dikkatle tuttu ve yavaş yavaş yürüdü.»
   - Açıklama: Bardağı ağızla taşımak çocuğun taklit edince kırılıp yaralanabileceği bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0143` birebir aynı, `@degisim: utangaç -> üzgün` (tutuyorsan), ardından `@onarim: f8f98b6a55b49dbc7de683101d145c1aaee335e5`, sonra gövde.
