# Editör görevi (onarım): Chase, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0056 (deneme 4 -> 5)

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
@plan: uçurtmanın ipi koptu ve uçurtma güneşe doğru uçtu | şapkasını gözlerinin üstüne indirdi ve uçurtmayı buldu
@tohum: chase-0056
@degisim: alet -> taş
Kumsalda güçlü bir rüzgar esiyordu. Chase iskelenin yanında renkli uçurtmasını uçuruyordu. Birden ipi koptu ve uçurtma güneşe doğru uçtu. Güneş çok parlaktı ve Chase o tarafa bakamadı. Uçurtmanın nereye düştüğünü çok merak etti. Hemen mavi şapkasını gözlerinin üstüne indirdi. Şapka gözlerine gölge yaptı ve Chase kumsala rahatça baktı. Uçurtma bir taşa takılmıştı ve rüzgarda sallanıyordu. Chase koştu ve uçurtmayı ağzıyla yakaladı. Sonra iskeleye geri döndü. Kaybolan uçurtmasını bulduğu için Chase çok sevindi.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Güneş çok parlaktı ve Chase o tarafa bakamadı"
   - Cümle 4: «Güneş çok parlaktı ve Chase o tarafa bakamadı.»
   - Açıklama: İpin kopması ve güneşin göz almasıyla iki ayrı sorun var.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hemen mavi şapkasını gözlerinin üstüne indirdi"
   - Cümle 6: «Hemen mavi şapkasını gözlerinin üstüne indirdi.»
   - Açıklama: Çözüm ipin kopması sebebine değil yalnız güneşin parlaklığına yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0056` birebir aynı, `@degisim: alet -> taş` (tutuyorsan), ardından `@onarim: 30db9be26cd1c39e60816b676e52e7c8c2ef3f08`, sonra gövde.

### Hikâye 2: tohum chase-0105 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar hazine haritasını uçurdu | kuralı hatırlayıp kum havuzunda hazineyi buldu
@tohum: chase-0105
Rüzgar esiyordu ve Chase ile Skye parkta hazine avı oynuyordu. Oyunun kuralı şuydu: hazine yalnız kum havuzuna saklanırdı. Ama rüzgar, Skye'ın Chase için çizdiği haritayı uçurdu. Hazineyi Skye saklamıştı ve şimdi arama sırası Chase'teydi. Chase bu kuralı hatırladı ve kum havuzuna koştu. Çimenlerde ve çiçeklerde hiç aramadı. Kumu patileriyle uzun uzun kazdı. Sonunda bir köşede küçük bir kutu buldu. İkisi havuzun kenarına oturdu ve kutuyu açtı. Kutunun içinde renkli taşlar vardı. Sonra hazineyi Chase sakladı ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Oyunun kuralı şuydu: hazine yalnız"
   - Cümle 2: «Oyunun kuralı şuydu: hazine yalnız kum havuzuna saklanırdı.»
   - Açıklama: İki noktadan sonra gelen cümle büyük harfle başlamalı: 'Hazine yalnız'.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "hazine yalnız kum havuzuna saklanırdı"
   - Cümle 2: «Oyunun kuralı şuydu: hazine yalnız kum havuzuna saklanırdı.»
   - Açıklama: Hazinenin yeri kuralla baştan belli olduğu için haritanın uçması gerçek bir sorun olmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar, Skye'ın Chase için çizdiği haritayı uçurdu"
   - Cümle 3: «Ama rüzgar, Skye'ın Chase için çizdiği haritayı uçurdu.»
   - Açıklama: Kural hazinenin yerini zaten söylediği için haritanın uçması gerçek bir sorun oluşturmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0105` birebir aynı, ardından `@onarim: 481beaa30fe0024a0610aa62f5efda0bbdb57771`, sonra gövde.

### Hikâye 3: tohum chase-0110 (deneme 3 -> 4)

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
@plan: arkadaşının kristali çimenlere düştü ve kayboldu | koşmadan yavaşça yürüdü ve kristali buldu
@tohum: chase-0110
@degisim: düşünceli -> üzgün
Chase kamp yerinde Marshall'ın yanına geldi. Marshall çadırın önünde taşlardan küçük bir kule yapıyordu. Ama kulenin en üstündeki kristal çimenlere düşmüş ve kaybolmuştu. Marshall üzgün üzgün yere bakıyordu. "Chase, kristal taşım hiçbir yerde yok," dedi Marshall. Kampta bir kural vardı: çimenlerde koşmak yoktu. Chase bu kurala uydu ve yavaş yavaş yürüdü. Böylece kristale hiç basmadı. Her yere dikkatle baktı. Sonunda kristali bir çiçeğin dibinde buldu. Chase kristali ağzıyla alıp Marshall'a verdi. Marshall kristali kulenin en üstüne koydu ve kule tamamlandı. Chase çok sevindi, çünkü arkadaşının kristalini bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kampta bir kural vardı"
   - Cümle 6: «Kampta bir kural vardı: çimenlerde koşmak yoktu.»
   - Açıklama: 'Kural' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bu kurala uydu"
   - Cümle 7: «Chase bu kurala uydu ve yavaş yavaş yürüdü.»
   - Açıklama: 'Kurala uymak' soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0110` birebir aynı, `@degisim: düşünceli -> üzgün` (tutuyorsan), ardından `@onarim: 65123cfffd57098b0e7774d724cf4ab73c9617fd`, sonra gövde.

### Hikâye 4: tohum chase-0113 (deneme 3 -> 4)

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
@plan: arkadaşı acıktı ama mama için kap yoktu | şapkasını çıkarıp ters çevirdi ve kap yaptı
@tohum: chase-0113
@degisim: mücevher -> mama
Kulübelerin önünde rüzgar esiyordu. Chase ile Skye orada oynuyordu. Birden Skye acıktı. Kulübenin yanında bir torba mama vardı ama hiç boş kap yoktu. "Chase, mamamı neye koyacağım?" diye sordu Skye. Chase mavi şapkasını çıkardı ve ters çevirdi. Şapka küçük bir kap gibi oldu. Skye koyu kahverengi mamaları şapkanın içine koydu. Sonra mamaları hemen yedi ve kuyruğunu salladı. "Teşekkürler, Chase, karnım doydu!" dedi Skye. Chase bundan sonra kulübenin önüne hep boş bir kap koyardı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama hiç boş kap yoktu"
   - Cümle 4: «Kulübenin yanında bir torba mama vardı ama hiç boş kap yoktu.»
   - Açıklama: Asıl sorun olan kap yokluğu ilk üç cümlede değil dördüncü cümlede söyleniyor.
   - Açıklama: Asıl sorun olan kabın yokluğu ilk üç cümlede değil dördüncü cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kulübenin yanında bir torba mama vardı ama hiç boş kap yoktu"
   - Cümle 4: «Kulübenin yanında bir torba mama vardı ama hiç boş kap yoktu.»
   - Açıklama: Kabın neden olmadığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0113` birebir aynı, `@degisim: mücevher -> mama` (tutuyorsan), ardından `@onarim: b3a150c2a8df00dd473d0036f5ed1f94a5434c03`, sonra gövde.

### Hikâye 5: tohum chase-0116 (deneme 3 -> 4)

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
Chase kulübesinin önünde Rubble ile oynuyordu. Birden Rubble acıktı ve mama kabına koştu. Kap boştu ve bisküvi kutusu da yerinde yoktu. Kulübeler boyanırken kutu başka bir yere konmuştu. Her yer boya kokuyordu ama Chase havayı dikkatle kokladı. Havada tatlı bir bisküvi kokusu da vardı. Chase bu kokunun peşinden kulübelerin arkasına yürüdü. Rubble ona inandı ve onunla gitti. Kutu gerçekten bir kulübenin arkasındaydı. İçinde tek bir büyük bisküvi kalmıştı. Chase bisküviyi ikiye böldü ve yarısını Rubble'a verdi. İkisi bisküvilerini yedi ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Rubble ona inandı"
   - Cümle 8: «Rubble ona inandı ve onunla gitti.»
   - Açıklama: Chase bir şey söylemediği için 'inandı' fiili yerinde değil ve soyut; 'Rubble da onun peşinden gitti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0116` birebir aynı, `@degisim: sakar -> boş` (tutuyorsan), ardından `@onarim: 1ce84708ac8c46115faf0d3ad1a7242f5c1ae62e`, sonra gövde.

### Hikâye 6: tohum chase-0119 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Kulübelerin önünde rüzgar esiyordu. Chase, Marshall için gizlice küçük bir pasta hazırlamıştı. Ama Marshall saklambaçta çok iyi saklanmıştı ve Chase onu bulamıyordu. Chase burnunu yere yaklaştırdı ve kokladı. Marshall'ın kokusu bir kulübenin arkasından geliyordu. Chase oraya koştu ve Marshall'ı buldu. "Seni buldum, Marshall! Sana bir sürprizim var," dedi Chase. Chase pastayı getirdi ve incecik dilimlere böldü. Marshall pastayı kirletmemek için tozlu patilerini sildi. Sonra ikisi birlikte pastayı yedi. "Bu çok güzel bir sürpriz, teşekkürler, Chase!" dedi Marshall.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase, Marshall için gizlice küçük bir pasta hazırlamıştı"
   - Cümle 2: «Chase, Marshall için gizlice küçük bir pasta hazırlamıştı.»
   - Açıklama: Pasta sürprizi saklambaç sorunundan çıkmayan ayrı bir iplik olarak kuruluyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Marshall saklambaçta çok iyi saklanmıştı"
   - Cümle 3: «Ama Marshall saklambaçta çok iyi saklanmıştı ve Chase onu bulamıyordu.»
   - Açıklama: Saklambaçta saklananı aramak oyunun kendisidir, gerçek bir sorun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Marshall pastayı kirletmemek için tozlu patilerini sildi"
   - Cümle 10: «Marshall pastayı kirletmemek için tozlu patilerini sildi.»
   - Açıklama: Pati silme işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0119` birebir aynı, `@degisim: yüzük -> pasta` (tutuyorsan), ardından `@onarim: 927f5c6b1201fdd1918fe16902b8b252fd42c912`, sonra gövde.

### Hikâye 7: tohum chase-0120 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: dalga taşlardan yapılan yıldızı dağıttı | kuralı hatırlayıp taşları sudan uzağa taşıdı
@tohum: chase-0120
Bir sabah Chase kumsalda oynuyordu. Siyah taşlarla kumun üstüne çok büyük bir yıldız yaptı. Ama bir dalga geldi ve taşları dağıttı. Chase'in patileri de ıslandı ve Chase güldü. Kumsalda bir kural vardı: herkes dalgalardan uzakta oynardı. Chase bu kuralı hatırladı ve taşları sudan uzağa götürdü. Yıldızı orada yeniden yaptı. Sonra yıldızın bir ucundan öbür ucuna zıpladı. Dalgalar artık yıldıza gelmiyordu. Chase sevinçle havladı ve kuyruğunu salladı. Chase bundan sonra yıldızlarını hep kurumuş kumda yapardı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "patileri de ıslandı ve Chase güldü"
   - Cümle 4: «Chase'in patileri de ıslandı ve Chase güldü.»
   - Açıklama: Yıldızı dağılan Chase gülüyor, bu yüzden sorun önemsiz bir olay gibi kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase'in patileri de ıslandı ve Chase güldü"
   - Cümle 4: «Chase'in patileri de ıslandı ve Chase güldü.»
   - Açıklama: Islanan patiler işlevsiz bir ayrıntı ve yıldızı dağılmışken gülmek sorunla bağdaşmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yıldızın bir ucundan öbür ucuna zıpladı"
   - Cümle 8: «Sonra yıldızın bir ucundan öbür ucuna zıpladı.»
   - Açıklama: Zıplama olayı hiçbir işe yaramayan işlevsiz bir ayrıntı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hep kurumuş kumda yapardı"
   - Cümle 11: «Chase bundan sonra yıldızlarını hep kurumuş kumda yapardı.»
   - Açıklama: Kumsaldaki kuru kum için 'kurumuş' yerine 'kuru' kelimesi uygun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0120` birebir aynı, ardından `@onarim: d9ba37a140e85afb4e4129a6f3c4c64efa7d3d65`, sonra gövde.

### Hikâye 8: tohum chase-0121 (deneme 3 -> 4)

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
Rüzgar esiyordu ve dalgalar kumsala geliyordu. Chase kumda büyük, parlak bir kabuk gördü ve onu almak istedi. Ama her dalga gelince kabuk suyun altında kalıyordu. Chase kurallara uydu ve suya girmedi. Kumun üstünde durdu ve bekledi. Dalga geri gidince kabuk yeniden göründü. Sonunda bir dalga kabuğu kuru kumun kenarına kadar itti. Chase kabuğu oradan ağzıyla aldı. Kabuk biraz ağırdı ama Chase onu sıkıca tuttu. Chase kabuğa uzun uzun baktı ve çok sevindi. Chase bundan sonra kabuk toplarken hep sudan uzakta beklerdi.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve suya girmedi"
   - Cümle 4: «Chase kurallara uydu ve suya girmedi.»
   - Açıklama: 'Kurallara uymak' hangi kural olduğu söylenmeyen soyut bir kavram, 3 yaşındaki çocuk için somut değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 4: «Chase kurallara uydu ve suya girmedi.»
   - Açıklama: Hangi kurallar olduğu belirtilmeyen soyut 'kural' kavramı küçük çocuğa somut değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kumun üstünde durdu ve bekledi"
   - Cümle 5: «Kumun üstünde durdu ve bekledi.»
   - Açıklama: Beklemek sebebe yönelen bir çözüm değil, kabuk şans eseri kıyıya geliyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonunda bir dalga kabuğu kuru kumun kenarına kadar itti"
   - Cümle 7: «Sonunda bir dalga kabuğu kuru kumun kenarına kadar itti.»
   - Açıklama: Sorunu Chase değil dalga çözüyor; Chase yalnız bekliyor.
5. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hep sudan uzakta beklerdi"
   - Cümle 11: «Chase bundan sonra kabuk toplarken hep sudan uzakta beklerdi.»
   - Açıklama: Anlatım -dı'lı geçmişten -r-di'li geçmişe kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0121` birebir aynı, `@degisim: spagetti -> kabuk` (tutuyorsan), ardından `@onarim: fd6fc560b9c97dda7207bdf399f9a5663be679b0`, sonra gövde.

### Hikâye 9: tohum chase-0122 (deneme 3 -> 4)

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
@plan: kar topu oynarken torbanın üstü karla kapandı | elmaların kokusunu alıp torbayı buldu
@tohum: chase-0122
Karlı dağda Chase ile Ryder karla üç küçük duvar ördü. Ryder sulu elmalarla dolu bir torbayı bir duvarın dibine koydu. Ama ikisi kar topu oynarken torbanın üstü karla kapandı. Üç duvar birbirine benziyordu ve torba hiç görünmüyordu. "Chase, torba hangi duvarın arkasında?" diye sordu Ryder. Chase burnunu yerde gezdirdi. Bir duvarın arkasında tatlı bir elma kokusu aldı. Patileriyle orayı kazdı ve torbayı buldu. Ryder torbayı açtı ve Chase'e kocaman bir elma verdi. Chase elmayı mutlu mutlu yedi. "Teşekkürler, Chase, torbamızı sen buldun!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "ikisi kar topu oynarken"
   - Cümle 3: «Ama ikisi kar topu oynarken torbanın üstü karla kapandı.»
   - Açıklama: Oyun adı olan 'kartopu' bitişik yazılır (plan satırında da aynı hata var).

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0122` birebir aynı, ardından `@onarim: b41a1f6a0e989123dde6d153c1b1694265ac1527`, sonra gövde.

### Hikâye 10: tohum chase-0125 (deneme 3 -> 4)

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
@plan: rüzgar şapkayı uçurdu ve şapka kayaların arasında kayboldu | arkadaşından yardım istedi ve mavi şapkayı karda gördüler
@tohum: chase-0125
@degisim: eşarp -> kaya
Rüzgar esiyordu ve gökyüzü bulutlarla kapalıydı. Chase ile Marshall karlı dağda dolaşıyordu. Birden rüzgar Chase'in mavi şapkasını uçurdu. Şapka yolun yanındaki kayaların arasına düştü. Chase etrafa baktı ama şapkayı göremedi. "Marshall, şapkam mavi, onu karda arar mısın?" diye sordu Chase. İkisi yan yana yürüdü ve kayaların arasına baktı. Sonunda Marshall beyaz karın üstünde mavi bir şey gördü. "Chase, şapkan burada!" dedi Marshall. Chase şapkasını aldı ve yeniden taktı. İkisi neşeyle yürümeye devam etti. Chase bundan sonra bir sorun olunca hemen arkadaşından yardım istedi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "arkadaşından yardım istedi ve mavi şapkayı karda gördüler"
   - Cümle 0 (plan satırı): «rüzgar şapkayı uçurdu ve şapka kayaların arasında kayboldu | arkadaşından yardım istedi ve mavi şapkayı karda gördüler»
   - Açıklama: Aynı cümlede tekil özneden çoğul yüklem 'gördüler'e geçiliyor, özne-yüklem uyumu bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bundan sonra bir sorun olunca"
   - Cümle 12: «Chase bundan sonra bir sorun olunca hemen arkadaşından yardım istedi.»
   - Açıklama: 'Bir sorun olunca' genelleme yapan soyut bir ifade, somut ders cümlesi değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0125` birebir aynı, `@degisim: eşarp -> kaya` (tutuyorsan), ardından `@onarim: e8ebb53275a1be32a703c0fe1f7a414623f02107`, sonra gövde.

### Hikâye 11: tohum chase-0128 (deneme 3 -> 4)

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
Rüzgar hafifçe esiyordu ve karlı dağda güneş parlıyordu. Chase ile Skye kırmızı bir topla oynuyordu. Birden top yokuştan aşağı yuvarlandı ve yumuşak karın içinde kayboldu. "Chase, topu bulabilir misin?" diye sordu Skye kibar bir sesle. Chase yerde küçük yuvarlak izler fark etti. İzler büyük bir meşe ağacının dibinde bitiyordu. Chase oraya yattı ve burnunu yerde gezdirdi. Ağacın dibindeki karın altından topun kokusu geliyordu. Chase patileriyle orayı kazdı ve kırmızı topu buldu. "Teşekkürler, Chase!" dedi Skye ve sevinçle zıpladı. İkisi meşe ağacının yanında topla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "izlere bakıp kokusuyla topu buldu"
   - Cümle 0 (plan satırı): «top yuvarlandı ve yumuşak karın içinde kayboldu | izlere bakıp kokusuyla topu buldu»
   - Açıklama: 'Kokusuyla' topun kokusu mu Chase'in burnu mu belli değil; 'kokusunu alarak' ya da 'koklayarak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0128` birebir aynı, ardından `@onarim: 663ab480cf2eeec4d8c8a9748da09094a214ddc3`, sonra gövde.

### Hikâye 12: tohum chase-0129 (deneme 3 -> 4)

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
Chase sıcak kumsalda Rubble'a yeni bir top oyunu öğretiyordu. Chase topa patisiyle vurdu ve top iskelenin altına kaçtı. Ama kurala göre kumsalda iskelenin altına girmek yasaktı. Chase de oraya girmedi. Chase iskelenin önünde durdu ve Rubble'dan yardım istedi. Rubble hemen kumda oynadığı sarı küreği getirdi. Chase küreği iskelenin altına doğru uzattı. Kürek topa değdi ve Chase topu yavaşça dışarı çekti. Rubble sevinçle zıpladı. Chase çok sevindi, çünkü top oyununu Rubble'a öğretmeye devam edebilirdi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase de oraya girmedi"
   - Cümle 4: «Chase de oraya girmedi.»
   - Açıklama: 'de' (dahi) bağlacı yanlış anlamda; başka kimse girmemiş değil, 'Chase oraya girmedi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0129` birebir aynı, `@degisim: dosya -> kürek` (tutuyorsan), ardından `@onarim: 5b92491d70aa34915055fbe4dcd6a048ef699070`, sonra gövde.
