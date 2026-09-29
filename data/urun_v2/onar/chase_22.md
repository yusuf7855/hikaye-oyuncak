# Editör görevi (onarım): Chase, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0085 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Ormanda güçlü bir rüzgar esiyordu. Chase kamp yerinde sevimli arkadaşı Rubble için bir armut sepeti hazırlamıştı. Ama rüzgar sepeti devirdi ve armutlar toprağa düştü. Hepsinin üstü kirlendi. Ekibin bir kuralı vardı. Yere düşen meyve önce yıkanırdı. Chase kovadaki temiz suyla armutları tek tek yıkadı. Sonra onları sepete geri koydu. Tam o sırada Rubble geldi. "Bu armutlar benim için mi, Chase?" diye sordu Rubble. "Evet, Rubble, hepsi senin için," dedi Chase. Rubble bir armut aldı ve mutlu mutlu yedi. Chase çok sevindi, çünkü sürprizi arkadaşını mutlu etmişti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar sepeti devirdi ve armutlar toprağa düştü"
   - Cümle 3: «Ama rüzgar sepeti devirdi ve armutlar toprağa düştü.»
   - Açıklama: Sepetin devrilip armutları yıkayıp bitirmek önemsiz, kolayca kapanan bir olay.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kovadaki temiz suyla"
   - Cümle 7: «Chase kovadaki temiz suyla armutları tek tek yıkadı.»
   - Açıklama: Temiz su dolu kova önceden kurulmadan tam çözüm gerektiğinde sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0085` birebir aynı, `@degisim: fırçalamak -> yıkamak` (tutuyorsan), ardından `@onarim: 5a25eb36919af5bbd83967dcb766ca108cec82b0`, sonra gövde.

### Hikâye 2: tohum chase-0086 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: tek top vardı ve ikisi de ilk atmak istedi | kurallara uydu ve sırayı önce arkadaşına verdi
@tohum: chase-0086
@degisim: raf -> top
Chase ile Marshall karlı dağda top oyunu oynuyordu. Chase kara uzun bir dal dikmişti ve ikisi topu dala atıyordu. Ama tek bir top vardı ve ikisi de onu ilk atmak istedi. Oyun hemen durdu. Oyunun bir kuralı vardı. Herkes topu sırayla atardı. "Önce sen at, Marshall," dedi Chase. "Teşekkürler, Chase, sonra sıra sende," dedi Marshall. Marshall attı ve top dala değdi. Çalışkan Marshall topu koşarak geri getirdi. Sonra Chase attı ve o da dalı vurdu. Chase ile Marshall çok sevindi, çünkü oyunları yine çok eğlenceliydi.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ikisi topu dala atıyordu"
   - Cümle 2: «Chase kara uzun bir dal dikmişti ve ikisi topu dala atıyordu.»
   - Açıklama: Oyun zaten sürüyor ve top atılıyorken ikisinin birden ilk atmak istemesi çelişkili.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyun hemen durdu"
   - Cümle 4: «Oyun hemen durdu.»
   - Açıklama: Yağmur ve oyunun durması sonraki olaylara bağlanmıyor, işlevsiz kalıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Chase attı ve o da dalı vurdu"
   - Cümle 11: «Sonra Chase attı ve o da dalı vurdu.»
   - Açıklama: 'o' zamirinin Chase'i mi topu mu gösterdiği belli değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "o da dalı vurdu"
   - Cümle 11: «Sonra Chase attı ve o da dalı vurdu.»
   - Açıklama: 'O' zamirinin Chase'i mi topu mu gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0086` birebir aynı, `@degisim: raf -> top` (tutuyorsan), ardından `@onarim: f7d743603618cace2c4ba2da65dbf212169579e9`, sonra gövde.

### Hikâye 3: tohum chase-0088 (deneme 2 -> 3)

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
Dağda büyük kar taneleri yağıyordu. Chase'in yanında sıcacık süt dolu bir sürahi vardı. Ama kar taneleri açık sürahiye, sütün içine düşüyordu. Kar yüzünden süt soğumaya başlamıştı. Sürahinin bir kapağı da yoktu. Chase mavi şapkasını çıkardı. Şapkayı sürahiye kapak gibi koydu. Kar taneleri artık şapkanın üstüne düşüyordu. Chase onları tek tek saydı ve güldü. Biraz sonra şapkayı kaldırdı ve yeniden taktı. Süt yine sıcaktı ve güzel kokuyordu. Chase sütünü yavaş yavaş içti ve karı mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase onları tek tek saydı"
   - Cümle 9: «Chase onları tek tek saydı ve güldü.»
   - Açıklama: Kar tanelerini saymak olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Süt yine sıcaktı ve güzel kokuyordu"
   - Cümle 11: «Süt yine sıcaktı ve güzel kokuyordu.»
   - Açıklama: Süt kar yüzünden soğumaya başlamışken şapkayla örtmek onu yeniden ısıtamaz, yine de süt yine sıcak deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0088` birebir aynı, ardından `@onarim: b572a7626756795e374e1e455711d9a27e07fad2`, sonra gövde.

### Hikâye 4: tohum chase-0091 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0091
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'delik', fiil 'tanımak', sıfat 'umutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: top dar bir deliğe düştü ve patisi yetişemedi | kurallara uydu ve arkadaşından yardım istedi
@tohum: chase-0091
Chase kamp yerinde kırmızı topuyla oynuyordu. Top yuvarlandı ve bir ağacın yanındaki dar bir deliğe düştü. Chase patisini uzattı ama topa yetişemedi. Ekipte toprağı yalnız Rubble kazardı. Chase bu kurala uydu ve etrafına baktı. Ağaçların arasından bir kürek sesi geliyordu. Chase bu sesi hemen tanıdı. "Rubble, topum deliğe düştü, yardım eder misin?" diye sordu Chase. "Tabii, Chase," dedi Rubble. Rubble küreğiyle deliği biraz büyüttü. Chase umutlu bir yüzle bekledi. Sonra patisini uzattı ve topunu çıkardı. "Teşekkürler, Rubble, iyi ki sana seslendim!" dedi Chase.
```

**Hakem bulguları (3):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Ekipte toprağı yalnız Rubble kazardı"
   - Cümle 4: «Ekipte toprağı yalnız Rubble kazardı.»
   - Açıklama: Kartın dünya kurallarında ve özelliklerinde böyle bir kural yok; hikaye diziye yanlış bir ekip kuralı ekliyor.
   - Açıklama: Kartta ya da dizide böyle bir ekip kuralı yok; dünya hakkında uydurma bilgi veriliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağaçların arasından bir kürek sesi geliyordu"
   - Cümle 6: «Ağaçların arasından bir kürek sesi geliyordu.»
   - Açıklama: Rubble'ın kürek sesi ve uydurulan kazma kuralı çözümü sebepsizce, hazır biçimde getiriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase umutlu bir yüzle bekledi"
   - Cümle 11: «Chase umutlu bir yüzle bekledi.»
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Umutlu bir yüzle' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0091` birebir aynı, ardından `@onarim: 64bd52d2bb4e26430deb847b180ff3f42fe06c20`, sonra gövde.

### Hikâye 5: tohum chase-0092 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0092
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'balkabağı', fiil 'birleşmek', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalga kovayı yuvarladı ve topun yeri kayboldu | kumu kokladı ve topun yerini bulup kazdı
@tohum: chase-0092
@degisim: balkabağı -> kova
Chase kumsalda eğlenceli bir oyun oynuyordu. Benekli topunu kuma gömdü ve yanına kırmızı kovasını koydu. Ama küçük bir dalga kovayı uzağa yuvarladı ve Chase topun yerini bulamadı. Chase önce iki yeri yan yana kazdı. İki çukur birleşti ve kocaman bir çukur oldu. Ama top orada da yoktu. Chase kumlu kulaklarını salladı ve güldü. Sonra burnunu kuma yaklaştırdı ve dikkatle kokladı. Topunun kokusu biraz uzaktan geliyordu. Chase oraya koştu ve patileriyle kumu açtı. Benekli top kumun içinden çıktı. Chase topu yeniden gömdü ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve topun yeri kayboldu"
   - Cümle 0 (plan satırı): «dalga kovayı yuvarladı ve topun yeri kayboldu | kumu kokladı ve topun yerini bulup kazdı»
   - Açıklama: Bir yer kaybolmaz; 'topun yerini bulamadı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "topun yeri kayboldu"
   - Cümle 0 (plan satırı): «dalga kovayı yuvarladı ve topun yeri kayboldu | kumu kokladı ve topun yerini bulup kazdı»
   - Açıklama: Yer kaybolmaz; 'Chase topun yerini unuttu' gibi olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İki çukur birleşti ve kocaman bir çukur oldu"
   - Cümle 5: «İki çukur birleşti ve kocaman bir çukur oldu.»
   - Açıklama: Çukurların birleşmesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Çukurların birleşmesi hiçbir işe yaramayan, olaya katkısı olmayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0092` birebir aynı, `@degisim: balkabağı -> kova` (tutuyorsan), ardından `@onarim: 90c57facacbcca6ef75e20eb6936ee53faa18834`, sonra gövde.

### Hikâye 6: tohum chase-0093 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Ryder
@tohum: chase-0093
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'tomurcuk', fiil 'yaslanmak', sıfat 'dalgalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | ev | Ryder
@plan: ayakkabı çizginin ortasını sildi ve oyun durdu | kurallara uydu ve yeni bir çizgi çizdi
@tohum: chase-0093
@degisim: tomurcuk -> tebeşir
Chase ile Ryder kulübelerin önünde çizgi oyunu oynuyordu. Ryder yere tebeşirle uzun, dalgalı bir çizgi çizmişti. Ama Ryder yürürken ayakkabısıyla çizginin ortasını sildi. "Sıra sende, Chase," dedi Ryder ve kulübeye yaslandı. Oyunda çizginin dışına basmak yoktu. Chase bu kurala uydu ve silinen yere basmadı. Chase tebeşiri patisiyle tuttu ve ortaya yeni bir çizgi çizdi. Ryder çizgiye baktı ve sevindi. "Çok güzel olmuş, hadi yürü," dedi Ryder. Chase çizginin üstünde yavaş yavaş yürüdü. Sonra Chase ile Ryder oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çizginin ortasını sildi ve oyun durdu"
   - Cümle 0 (plan satırı): «ayakkabı çizginin ortasını sildi ve oyun durdu | kurallara uydu ve yeni bir çizgi çizdi»
   - Açıklama: Gövdede oyun durmuyor; Ryder silinmeden hemen sonra sırayı Chase'e veriyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ayakkabı çizginin ortasını sildi ve oyun durdu"
   - Cümle 0 (plan satırı): «ayakkabı çizginin ortasını sildi ve oyun durdu | kurallara uydu ve yeni bir çizgi çizdi»
   - Açıklama: Gövdede oyun durmuyor; Ryder hemen sırayı Chase'e veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0093` birebir aynı, `@degisim: tomurcuk -> tebeşir` (tutuyorsan), ardından `@onarim: b6e17954f27085076d1001904bc102b74c40b610`, sonra gövde.

### Hikâye 7: tohum chase-0095 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Marshall
@tohum: chase-0095
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: kaybolan eşya
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'fener', fiil 'yorulmak', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | ev | Marshall
@plan: yorgun arkadaşı fenerini yolda düşürmüştü | geldiği yolu kokladı ve feneri buldu
@tohum: chase-0095
Kulenin önünde Chase ile Marshall oturuyordu. Marshall uzun bir işten yeni dönmüştü ve çok yorulmuştu. Ama kırmızı fenerini bulamadı, çünkü yolda bir yere düşürmüştü. Marshall bu feneri işlerde hep kullanıyordu. Uykulu gözlerle her yere baktı ve üzüldü. Chase hemen yere eğildi ve Marshall'ın geldiği yolu kokladı. Koku onu yavaş yavaş kulenin arkasındaki çimenlere götürdü. Kırmızı fener çimenlerin arasında duruyordu. Chase feneri ağzına aldı ve koşarak Marshall'a getirdi. Marshall kuyruğunu salladı ve feneri kulübesine koydu. Sonra iki arkadaş yan yana uzandı ve mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Kulenin önünde Chase ile Marshall oturuyordu"
   - Cümle 1: «Kulenin önünde Chase ile Marshall oturuyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye kulenin önünde başlıyor ve kulenin arkasındaki çimenlerde sürüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Koku onu yavaş yavaş"
   - Cümle 7: «Koku onu yavaş yavaş kulenin arkasındaki çimenlere götürdü.»
   - Açıklama: Kokunun birini bir yere götürmesi mecazdır.
   - Açıklama: Kokunun birini bir yere götürmesi mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0095` birebir aynı, ardından `@onarim: 36111060edb05fb1cb1b2a8b78d8bd7b3a3f0185`, sonra gövde.

### Hikâye 8: tohum chase-0096 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0096
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'yastık', fiil 'seçmek', sıfat 'değerli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: rüzgar yastığın üstünü kumla örttü | kurallara uydu ve kumsalı sırayla aradı
@tohum: chase-0096
Bir sabah Ryder ile Chase kumsaldaydı. Ryder kumda oturmak için küçük yeşil yastığını getirmişti. Ama güçlü bir rüzgar esti ve yastığın üstünü kumla örttü. Ryder her yere baktı ama yastığını bulamadı. "Bu yastık benim için çok değerli," dedi Ryder. Sonra onu bulmak için Chase'i seçti. Chase kurallara uydu ve kumsalı baştan sona sırayla aradı. Üçüncü sırada patisi yumuşak bir şeye dokundu. Chase kumu açtı ve yeşil yastığı çıkardı. "Aferin, Chase, buldun!" dedi Ryder. Ryder yastığı silkti ve üstüne oturdu. Chase de yanına uzandı ve ikisi mutlu mutlu denizi seyretti.
```

**Hakem bulguları (9):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurallara uydu ve kumsalı sırayla aradı"
   - Cümle 0 (plan satırı): «rüzgar yastığın üstünü kumla örttü | kurallara uydu ve kumsalı sırayla aradı»
   - Açıklama: Bir yeri 'sırayla aramak' ve belirsiz 'kurallara uymak' bu bağlamda anlamsız kullanılmış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "güçlü bir rüzgar esti ve yastığın üstünü kumla örttü"
   - Cümle 3: «Ama güçlü bir rüzgar esti ve yastığın üstünü kumla örttü.»
   - Açıklama: Rüzgarın bir yastığı bir anda bulunamayacak kadar kumla örtmesi akla yatkın bir sebep değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "benim için çok değerli"
   - Cümle 5: «"Bu yastık benim için çok değerli," dedi Ryder.»
   - Açıklama: 'Değerli' soyut bir kavram ve 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Değerli' 3 yaşındaki çocuk için soyut bir kavram.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra onu bulmak için Chase'i seçti"
   - Cümle 6: «Sonra onu bulmak için Chase'i seçti.»
   - Açıklama: Seçim yapılacak başka kimse yokken Chase'in seçilmesi ve sonraki 'üçüncü sıra' ayrıntısı sebepsiz ve işlevsiz.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 7: «Chase kurallara uydu ve kumsalı baştan sona sırayla aradı.»
   - Açıklama: 'Kurallara uymak' hangi kural olduğu belli olmayan soyut bir ifade.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uydu ve kumsalı baştan sona sırayla aradı"
   - Cümle 7: «Chase kurallara uydu ve kumsalı baştan sona sırayla aradı.»
   - Açıklama: Tohumdaki kurallara uyma özelliği hiçbir kurala bağlanmıyor; sırayla aramak kurala uymak değil, özellik işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kural özelliği işe yarar biçimde kullanılmıyor; ortada uyulan bir kural yok, yalnız etiket olarak geçiyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uydu ve kumsalı"
   - Cümle 7: «Chase kurallara uydu ve kumsalı baştan sona sırayla aradı.»
   - Açıklama: Hiçbir kural kurulmadan 'kurallara uydu' deniyor; ayrıntı işlevsiz ve aramayı sebepsizce getiriyor.
8. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Üçüncü sırada patisi yumuşak"
   - Cümle 8: «Üçüncü sırada patisi yumuşak bir şeye dokundu.»
   - Açıklama: 'Üçüncü sırada' ifadesi bağlamda anlamsız; hangi sıra olduğu belli değil.
   - Açıklama: 'Üçüncü sırada' neyi gösterdiği belli olmayan yanlış bir kullanım.
9. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Üçüncü sırada patisi yumuşak"
   - Cümle 8: «Üçüncü sırada patisi yumuşak bir şeye dokundu.»
   - Açıklama: Sıraların ne olduğu hiç kurulmadan 'üçüncü sıra' beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0096` birebir aynı, ardından `@onarim: 763da54c490740c48e62d305ccb61807d7d1bd8d`, sonra gövde.

### Hikâye 9: tohum chase-0098 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0098
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'yelek', fiil 'süslenmek', sıfat 'yumuşacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: kardan köpek bembeyazdı ve polis köpeğine hiç benzemiyordu | yelek giydirdi ve kendi mavi şapkasını taktı
@tohum: chase-0098
Karlı dağda Chase ile Ryder küçük bir kar şenliği hazırlıyordu. Şenlik için Chase gibi olsun diye kardan bir köpek yapmışlardı. Ama kardan köpek bembeyazdı ve hiç Chase'e benzemiyordu. Ryder, kardan köpek için getirdiği yumuşacık yeleği çantasından çıkardı. Yeleği kardan köpeğe giydirdi. "Güzel oldu ama bir şey eksik," dedi Ryder. Chase kardan köpeğe dikkatle baktı. Sonra kendi mavi şapkasını çıkardı ve kardan köpeğin başına taktı. Kardan köpek yeleği ve şapkasıyla güzelce süslendi. Artık mavi şapkasıyla tam bir polis köpeği olmuştu. Chase sevinçle havladı ve kuyruğunu salladı. "Harika, Chase, kardan köpek tıpkı senin gibi oldu!" dedi Ryder.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yelek giydirdi ve kendi mavi şapkasını taktı"
   - Cümle 0 (plan satırı): «kardan köpek bembeyazdı ve polis köpeğine hiç benzemiyordu | yelek giydirdi ve kendi mavi şapkasını taktı»
   - Açıklama: Plan yeleği figürün giydirdiğini söylüyor ama gövdede yeleği Ryder giydiriyor.
   - Açıklama: Plan yeleği figürün giydirdiğini ima ediyor ama gövdede yeleği Ryder giydiriyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Ryder, kardan köpek için getirdiği yumuşacık yeleği"
   - Cümle 4: «Ryder, kardan köpek için getirdiği yumuşacık yeleği çantasından çıkardı.»
   - Açıklama: Yeleği figür Chase değil yan karakter Ryder getirip giydiriyor, çözümün yarısını o yapıyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Yeleği kardan köpeğe giydirdi"
   - Cümle 5: «Yeleği kardan köpeğe giydirdi.»
   - Açıklama: Yeleği getiren ve giydiren Ryder; çözümün yarısını yan karakter yapıyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Artık mavi şapkasıyla tam bir polis köpeği olmuştu."
   - Cümle 10: «Artık mavi şapkasıyla tam bir polis köpeği olmuştu.»
   - Açıklama: Bir önceki cümlede söylenen şapka bilgisi gereksizce tekrarlanıyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Artık mavi şapkasıyla tam"
   - Cümle 10: «Artık mavi şapkasıyla tam bir polis köpeği olmuştu.»
   - Açıklama: Bir önceki cümledeki 'şapkasıyla' gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0098` birebir aynı, ardından `@onarim: d37fa3b13b0aa55679260dac87492aebe4e47e99`, sonra gövde.

### Hikâye 10: tohum chase-0099 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0099
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kalem', fiil 'yeşillenmek', sıfat 'paslı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | -
@plan: parkta yalnız küçük bir yer yemyeşildi | ıslak toprağı kokladı ve paslı musluğu buldu
@tohum: chase-0099
@degisim: kalem -> musluk
Bir sabah Chase parkta yürüyordu. Parkın çimenleri kuruydu ama kaydırağın arkasındaki küçük bir yer yeşillenmişti. Chase bu yeşil yeri çok merak etti. Oraya gitti, burnunu yere yaklaştırdı ve kokladı. Burnuna ıslak toprak kokusu geldi. Chase bu kokunun peşinden çitin yanına kadar yürüdü. Çitin yanında eski ve paslı bir musluk vardı. Musluktan yavaş yavaş su damlıyordu. Damlalar ince bir yoldan o yeşil yere akıyordu. Otlar bu suyla büyümüştü. Chase otların neden yeşil olduğunu bulmuştu. Sevinçle koştu ve yeşil otların üstünde mutlu mutlu yuvarlandı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "parkta yalnız küçük bir yer yemyeşildi"
   - Cümle 0 (plan satırı): «parkta yalnız küçük bir yer yemyeşildi | ıslak toprağı kokladı ve paslı musluğu buldu»
   - Açıklama: Küçük bir yerin yeşil olması gerçek bir sorun değil, yalnız bir merak konusu.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük bir yer yeşillenmişti"
   - Cümle 2: «Parkın çimenleri kuruydu ama kaydırağın arkasındaki küçük bir yer yeşillenmişti.»
   - Açıklama: Yeşil bir yer sorun değil, yalnız merak konusu; çocuğun önemseyeceği bir dert yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0099` birebir aynı, `@degisim: kalem -> musluk` (tutuyorsan), ardından `@onarim: 69adeb962560b88d4ced195beb535da064dcf239`, sonra gövde.

### Hikâye 11: tohum chase-0100 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Rubble
@tohum: chase-0100
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'portakal', fiil 'sormak', sıfat 'peynirli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Rubble
@plan: portakal yuvarlandı ve ağır bir tahtanın altına kaçtı | kokusunu buldu ve tahta için arkadaşından yardım istedi
@tohum: chase-0100
Martılar kumsalda bağırıyordu. Chase ile Rubble iskelenin yanında piknik yapıyordu. Chase'in portakalı ağzından düştü ve iskelenin arkasına yuvarlandı. Chase oraya koştu ama portakalı göremedi. Burnunu yere yaklaştırdı ve kokladı. Portakalın kokusu büyük bir tahtanın altından geliyordu. Chase tahtayı itti ama tahta çok ağırdı. "Rubble, bu tahtayı birlikte kaldıralım mı?" diye sordu Chase. Peynirli sandviçini yiyen Rubble hemen geldi. İkisi tahtayı birlikte kaldırdı ve Chase portakalı aldı. Sonra portakalı Rubble ile paylaştı. Chase bundan sonra ağır bir şey için hemen arkadaşından yardım istedi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kokusunu buldu ve tahta"
   - Cümle 0 (plan satırı): «portakal yuvarlandı ve ağır bir tahtanın altına kaçtı | kokusunu buldu ve tahta için arkadaşından yardım istedi»
   - Açıklama: Koku bulunmaz, izlenir; 'kokusunu buldu' fiil nesnesine uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Peynirli sandviçini yiyen Rubble"
   - Cümle 9: «Peynirli sandviçini yiyen Rubble hemen geldi.»
   - Açıklama: Rubble'ın peynirli sandviçi hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0100` birebir aynı, ardından `@onarim: 10df0c2b6f3f05059a221f0dd4c82129772b0cc8`, sonra gövde.
