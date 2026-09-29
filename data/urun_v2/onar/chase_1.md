# Editör görevi (onarım): Chase, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0001 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0001
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'biftek', fiil 'susamak', sıfat 'mor'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: susadı ama çeşmenin önünde mor kelebekler vardı | kelebekleri korkutmadan yavaşça su içti
@tohum: chase-0001
Ormanda, kamp yerinde sıcak bir gündü. Chase biraz önce biftek yemişti ve çok susamıştı. Ama çeşmenin önünde mor kelebekler oturuyordu. Chase kelebekleri korkutmak istemedi. Kampın kuralı belliydi: hayvanları korkutmak yasaktı. Chase durdu ve kelebeklere dikkatle baktı. Kelebekler ıslak taşlardan su içiyordu! Chase çok yavaş adımlarla çeşmenin öbür yanına yürüdü. Başını eğdi ve sessizce içmeye başladı. Kelebeklerin hiçbiri uçup gitmedi. Chase onları tek tek saydı; tam beş taneydi. Chase çok sevindi, çünkü kelebekleri hiç korkutmadan suyunu içmişti.
```

**Hakem bulguları (5):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "çeşmenin önünde mor kelebekler oturuyordu"
   - Cümle 3: «Ama çeşmenin önünde mor kelebekler oturuyordu.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, hikayenin sorununu oluşturup olaya katılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Kampın kuralı belliydi"
   - Cümle 5: «Kampın kuralı belliydi: hayvanları korkutmak yasaktı.»
   - Açıklama: 'Kural' ve 'belliydi' soyut kavramlar, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Kural' ve 'belliydi' soyut kavramlar; 3 yaşındaki çocuk için uygun değil.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "hayvanları korkutmak yasaktı"
   - Cümle 5: «Kampın kuralı belliydi: hayvanları korkutmak yasaktı.»
   - Açıklama: Kelebekleri korkutmak istemediği bir önceki cümlede söylenmişken aynı fikir tekrar ediliyor.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Kelebekler ıslak taşlardan su içiyordu"
   - Cümle 7: «Kelebekler ıslak taşlardan su içiyordu!»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun parçası olarak olaya katılıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Chase onları tek tek saydı; tam beş taneydi"
   - Cümle 11: «Chase onları tek tek saydı; tam beş taneydi.»
   - Açıklama: Kelebekleri saymak olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Kelebekleri sayma ayrıntısı olayla bağlantısız ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0001` birebir aynı, ardından `@onarim: 63d9c65c20716ae69f41e3bfd14924a473fc92cd`, sonra gövde.

### Hikâye 2: tohum chase-0002 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0002
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pirinç', fiil 'çözmek', sıfat 'düz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: uçurtmanın ipi iskelenin direğine dolandı | yavaşça yürüdü ve düğümü çözdü
@tohum: chase-0002
@degisim: pirinç -> uçurtma
Chase kumsalda sarı bir uçurtma uçuruyordu. Birden güçlü bir rüzgar esti ve uçurtma iskeleye doğru gitti. Uçurtmanın ipi, iskelenin kısa bir direğine dolandı. Uçurtma tahtaların üstüne indi ve orada kaldı. Chase hemen iskeleye koşmak istedi. Ama kuralı biliyordu: iskelede koşmak yasaktı. Chase yavaş yavaş yürüdü. İp direğe düğüm olmuştu. Chase düğümü dişleriyle dikkatle çözdü. Sonra uçurtmayı aldı ve düz kuma geri döndü. Biraz koştu ve uçurtma tekrar havaya yükseldi. Chase çok sevindi, çünkü sarı uçurtması yine gökyüzündeydi.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Uçurtmanın ipi, iskelenin kısa"
   - Cümle 3: «Uçurtmanın ipi, iskelenin kısa bir direğine dolandı.»
   - Açıklama: Özne ile tümleç arasına gereksiz virgül konmuş.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Ama kuralı biliyordu: iskelede koşmak yasaktı."
   - Cümle 6: «Ama kuralı biliyordu: iskelede koşmak yasaktı.»
   - Açıklama: 'Kural' ve 'yasak' soyut kavramlar; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0002` birebir aynı, `@degisim: pirinç -> uçurtma` (tutuyorsan), ardından `@onarim: 6590a4d5e40788f2dc92ffbe5176a8a01074edc7`, sonra gövde.

### Hikâye 3: tohum chase-0003 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0003
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'valiz', fiil 'yetişmek', sıfat 'sabunlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: güneş çok parlaktı ve yolu göremedi | şapkasını gözlerine doğru çekti ve trene koştu
@tohum: chase-0003
@degisim: sabunlu -> parlak
Bir sabah Chase ormandaki kamp yerinde tren oyunu oynuyordu. Büyük ağacın yanındaki kütük onun treni olacaktı. Ama güneş çok parlaktı ve Chase yolu göremiyordu. Chase mavi şapkasını gözlerine doğru çekti. Şapka gözlerine gölge yaptı. Chase artık yolu çok iyi görüyordu. Küçük valizini aldı ve ağaca doğru koştu. Kütüğün üstüne atladı ve valizi yanına koydu. Sonra bir tren gibi uzun uzun ses çıkardı ve yolculuk başladı. Chase çok sevindi, çünkü trenine tam zamanında yetişti.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "güneş çok parlaktı ve Chase yolu göremiyordu"
   - Cümle 3: «Ama güneş çok parlaktı ve Chase yolu göremiyordu.»
   - Açıklama: Ormanda hemen yandaki ağaca gitmek için güneş yüzünden yolu görememek akla yatkın ve önemli bir sorun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Küçük valizini aldı ve"
   - Cümle 7: «Küçük valizini aldı ve ağaca doğru koştu.»
   - Açıklama: Valiz sebepsiz beliriyor ve hikayede hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Küçük valizini aldı ve ağaca doğru koştu"
   - Cümle 7: «Küçük valizini aldı ve ağaca doğru koştu.»
   - Açıklama: Valiz daha önce kurulmadan sebepsiz beliriyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "trenine tam zamanında yetişti"
   - Cümle 10: «Chase çok sevindi, çünkü trenine tam zamanında yetişti.»
   - Açıklama: Tren oyununda treni Chase'in kendisi kurmuş; 'tam zamanında yetişmek' anlamca yerine oturmuyor.
   - Açıklama: Kütük Chase'in kendi oyun treni; kalkan bir trene yetişmek anlamı olaya uymuyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "trenine tam zamanında yetişti"
   - Cümle 10: «Chase çok sevindi, çünkü trenine tam zamanında yetişti.»
   - Açıklama: 'Tam zamanında yetişmek' soyut bir kalıp ve hayali trene mecazlı uygulanıyor.
   - Açıklama: 'Tam zamanında yetişmek' oyun treni için mecazlı ve soyut bir anlatım.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "trenine tam zamanında yetişti"
   - Cümle 10: «Chase çok sevindi, çünkü trenine tam zamanında yetişti.»
   - Açıklama: Tren Chase'in kendi oyunundaki bir kütük; yetişilecek bir zaman hiç yokken tam zamanında yetiştiği söyleniyor.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "trenine tam zamanında yetişti"
   - Cümle 10: «Chase çok sevindi, çünkü trenine tam zamanında yetişti.»
   - Açıklama: Trene yetişme hedefi ve zaman baskısı hiç kurulmadığı için son, kurulmamış bir hedefe ulaşmış gibi bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0003` birebir aynı, `@degisim: sabunlu -> parlak` (tutuyorsan), ardından `@onarim: 27a34b5378d09cd9d21d3627dc696fca43e0385e`, sonra gövde.

### Hikâye 4: tohum chase-0004 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0004
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kilit', fiil 'yapışmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: mavi şapkası görünüyordu ve hemen bulundu | şapkasını karla beyaz yaptı ve yeniden saklandı
@tohum: chase-0004
@degisim: kilit -> kar
Bir sabah Chase ile Rubble karlı dağda saklambaç oynuyordu. Chase büyük bir kar yığınının arkasına saklandı. Ama mavi şapkası yığının üstünden görünüyordu ve Rubble onu hemen buldu. "Şapkanı gördüm, Chase!" dedi Rubble ve güldü. Chase bir yol düşündü. Şapkasını yumuşak karın üstüne bastırdı. Kar şapkaya yapıştı ve şapka beyaz puantiyeli oldu. Chase başka bir yığının arkasına saklandı. Rubble her yere baktı ama onu bulamadı. "Buradayım!" dedi Chase ve karın arkasından zıpladı. Rubble şaşırdı ve kahkaha attı. İkisi de çok sevindi, çünkü bu oyun çok eğlenceli olmuştu.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "mavi şapkası görünüyordu ve hemen bulundu"
   - Cümle 0 (plan satırı): «mavi şapkası görünüyordu ve hemen bulundu | şapkasını karla beyaz yaptı ve yeniden saklandı»
   - Açıklama: Plan satırında öznesiz 'bulundu' şapkaya bağlanıyor; bulunanın Chase olduğu belli değil.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şapkasını karla beyaz yaptı"
   - Cümle 0 (plan satırı): «mavi şapkası görünüyordu ve hemen bulundu | şapkasını karla beyaz yaptı ve yeniden saklandı»
   - Açıklama: Plan şapkanın beyaz yapıldığını söylüyor ama gövdede şapka yalnız beyaz puantiyeli oluyor.
   - Açıklama: Plan şapkanın beyaz olduğunu söylüyor ama gövdede şapka yalnız beyaz puantiyeli oluyor, yani hala mavi kalıyor.
   - Açıklama: Plan şapkanın beyaz olduğunu söylüyor ama gövdede şapka yalnız beyaz puantiyeli oluyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Chase bir yol düşündü"
   - Cümle 5: «Chase bir yol düşündü.»
   - Açıklama: 'Yol düşünmek' çözüm anlamında mecazlı bir kullanım.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "şapka beyaz puantiyeli oldu"
   - Cümle 7: «Kar şapkaya yapıştı ve şapka beyaz puantiyeli oldu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Puantiyeli' 3 yaşındaki çocuğun bilmediği bir kelime.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "şapka beyaz puantiyeli oldu"
   - Cümle 7: «Kar şapkaya yapıştı ve şapka beyaz puantiyeli oldu.»
   - Açıklama: Şapka yalnız beyaz puantiyeli oluyor, yani mavisi hâlâ görünüyor; çözüm görünme sebebini tam gidermiyor ve Chase'in bulunamaması akla yatkın değil.
   - Açıklama: Şapka yalnız beyaz puantiyeli oluyor, mavisi hâlâ görünüyor; çözüm görünme sebebini tam gidermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0004` birebir aynı, `@degisim: kilit -> kar` (tutuyorsan), ardından `@onarim: 8c5e717d603e01ebcfaef07d366fd99c439d2785`, sonra gövde.

### Hikâye 5: tohum chase-0005 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0005
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'elma', fiil 'barışmak', sıfat 'ıslak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: yağmur başladı ve kumsal ıslak oldu | kurala uydu ve şemsiyenin altında kuru kaldı
@tohum: chase-0005
@degisim: barışmak -> dinlemek
Chase kumsalda oturmuş, kırmızı bir elma yiyordu. Birden yağmur başladı ve kum çabucak ıslak oldu. Chase'in tüyleri de ıslanmaya başladı. Chase kuralı biliyordu: yağmurda kuru bir yere gitmek gerekiyordu. Elmasını ağzına aldı ve kumsalda duran büyük şemsiyenin altına koştu. Orada hiç yağmur yoktu. Damlalar şemsiyenin üstüne tık tık vuruyordu. Chase elmasını yerken bu sesi dinledi. Ses küçük bir davulun sesine benziyordu. Biraz sonra yağmur dindi ve güneş çıktı. Chase elmasını bitirdi. Chase çok mutluydu, çünkü yağmuru kuru bir yerde, elmasını yiyerek dinlemişti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kum çabucak ıslak oldu"
   - Cümle 2: «Birden yağmur başladı ve kum çabucak ıslak oldu.»
   - Açıklama: 'Islak oldu' bozuk bir yapı; 'ıslandı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Chase kuralı biliyordu"
   - Cümle 4: «Chase kuralı biliyordu: yağmurda kuru bir yere gitmek gerekiyordu.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "kumsalda duran büyük şemsiyenin altına koştu"
   - Cümle 5: «Elmasını ağzına aldı ve kumsalda duran büyük şemsiyenin altına koştu.»
   - Açıklama: Şemsiye önceden kurulmadan tam gerektiği anda sebepsizce beliriyor ve çözümü getiriyor.
   - Açıklama: Şemsiye önceden kurulmadan tam çözüm anında sebepsizce beliriyor.
   - Açıklama: Şemsiye önceden kurulmadan tam gerektiği anda beliriyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Şemsiye önceden kurulmadan çözüm anında sebepsizce beliriyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase elmasını bitirdi"
   - Cümle 11: «Chase elmasını bitirdi.»
   - Açıklama: 'Elmasını' kelimesi hikayede gereksiz yere çok kez tekrarlanıyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yağmuru kuru bir yerde, elmasını yiyerek dinlemişti"
   - Cümle 12: «Chase çok mutluydu, çünkü yağmuru kuru bir yerde, elmasını yiyerek dinlemişti.»
   - Açıklama: Son cümle 8. cümledeki elma yiyerek sesi dinleme bilgisini gereksizce tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0005` birebir aynı, `@degisim: barışmak -> dinlemek` (tutuyorsan), ardından `@onarim: 8368d9d87d8975c5b8eadc6322ed4fa0c74124e8`, sonra gövde.

### Hikâye 6: tohum chase-0006 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0006
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'masa', fiil 'kavuşmak', sıfat 'çamurlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: yağmur yüzünden kampın masası çok çamurlu oldu | kurala uydu, masayı temizledi ve tabağı hazırladı
@tohum: chase-0006
@degisim: kavuşmak -> dizmek
Yağmur yeni dinmişti ve ağaçlardan damlalar düşüyordu. Chase ile Skye ormandaki kamp yerinde bir meyve tabağı yapmak istedi. Ama yağmur yüzünden kampın masası çok çamurlu olmuştu. Chase kuralı biliyordu: yemek masası temiz olmalıydı. "Önce masayı temizleyelim, Skye," dedi Chase. Chase bir kova su ve bir bez getirdi. Masayı sildi ve güzelce kuruladı. Skye kırmızı çilekleri, Chase de yeşil üzümleri getirdi. İkisi meyveleri büyük bir tabağa dizdi. Çilekler bir çiçeğin yaprakları, üzümler de ortası oldu. Skye tabağa baktı ve sevinçle zıpladı. "Tabak çiçek gibi oldu, teşekkürler, Chase!" dedi Skye.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Çilekler bir çiçeğin yaprakları"
   - Cümle 10: «Çilekler bir çiçeğin yaprakları, üzümler de ortası oldu.»
   - Açıklama: Çileklerin çiçek yaprağı 'olması' mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Çilekler bir çiçeğin yaprakları, üzümler de ortası oldu"
   - Cümle 10: «Çilekler bir çiçeğin yaprakları, üzümler de ortası oldu.»
   - Açıklama: Meyvelerin çiçeğin parçaları 'olması' mecazlı bir anlatım, küçük çocuk için açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0006` birebir aynı, `@degisim: kavuşmak -> dizmek` (tutuyorsan), ardından `@onarim: fa8a237c201a57511d2f7b5bd92e360b8116f96d`, sonra gövde.

### Hikâye 7: tohum chase-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0008
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: kaybolan eşya
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kakao', fiil 'kurmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: rüzgar esti ve bardak kayboldu | kurala uydu ve son yerden aramaya başladı
@tohum: chase-0008
@degisim: kakao -> süt
Kumsalda rüzgarlı bir gündü. Chase ile Marshall kuma büyük bir şemsiye kurdu. Birden rüzgar esti ve Marshall'ın bardağı uzağa yuvarlandı. "Bardağım nerede?" diye sordu Marshall. "Kural şu: aramaya son yerden başlarız," dedi Chase. Chase şemsiyenin yanına gitti ve kumda küçük izler gördü. İzler iskeleye doğru gidiyordu. Chase o yöne yürüdü. Bardak iskelenin yanında, bir kum yığınının arkasındaydı! Chase bardağı Marshall'a getirdi. Marshall iki bardağa da süt koydu. Sonra ikisi şemsiyenin altında oturdu ve sütlerini mutlu mutlu içti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurala uydu ve son yerden aramaya başladı"
   - Cümle 0 (plan satırı): «rüzgar esti ve bardak kayboldu | kurala uydu ve son yerden aramaya başladı»
   - Açıklama: Plan satırında 'son yerden' anlamı belirsiz kalıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "kurala uydu ve son"
   - Cümle 0 (plan satırı): «rüzgar esti ve bardak kayboldu | kurala uydu ve son yerden aramaya başladı»
   - Açıklama: 'Kurala uymak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aramaya son yerden başlarız"
   - Cümle 5: «"Kural şu: aramaya son yerden başlarız," dedi Chase.»
   - Açıklama: 'son yerden' anlamı belirsiz; 'en son görülen yerden' kastediliyor.
   - Açıklama: 'Son yerden' anlamsız; 'son gördüğümüz yerden' gibi bir anlam kastedilmiş ama söylenmemiş.
   - Açıklama: 'Son yerden' anlamı belirsiz; 'son görülen yerden' kastediliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Marshall iki bardağa da süt koydu"
   - Cümle 11: «Marshall iki bardağa da süt koydu.»
   - Açıklama: Yalnız bir bardak kurulmuşken ikinci bardak ve süt sebepsiz beliriyor.
   - Açıklama: İkinci bardak ve süt sebepsiz beliriyor; önceki olaylardan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0008` birebir aynı, `@degisim: kakao -> süt` (tutuyorsan), ardından `@onarim: 55f832dceea687096c4b00c2227b4292d25c3f09`, sonra gövde.

### Hikâye 8: tohum chase-0009 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0009
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'çöp', fiil 'damlamak', sıfat 'akıllı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: ağaçtan kar döküldü ve kurabiye kutusunu kapattı | kutuyu kokusundan buldu ve kurabiyeleri paylaştı
@tohum: chase-0009
Güneş çıkmıştı ve ağaçlardan su damlıyordu. Chase karlı dağda kurabiyelerini Skye ile paylaşacaktı. Ama birden ağaçtan kar döküldü ve kurabiye kutusunun üstünü kapattı. "Kutu nerede?" diye sordu Skye. Chase burnunu kara yaklaştırdı ve kokladı. Kurabiyelerin tatlı kokusunu hemen aldı. Patileriyle karı kazıdı ve kutuyu buldu. "Ne akıllı bir burnun var, Chase!" dedi Skye. Chase kutuyu açtı; içinde altı kurabiye vardı. Chase üç kurabiyeyi Skye'a verdi. İkisi kurabiyelerini yan yana oturup yedi. Chase boş kutuyu kapattı ve çöpü dağda bırakmadı. Chase çok mutluydu, çünkü kurabiyelerini arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kar döküldü ve kurabiye kutusunu kapattı"
   - Cümle 0 (plan satırı): «ağaçtan kar döküldü ve kurabiye kutusunu kapattı | kutuyu kokusundan buldu ve kurabiyeleri paylaştı»
   - Açıklama: Kar kutuyu kapatmaz, üstünü örter; fiil öznesine uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ne akıllı bir burnun"
   - Cümle 8: «"Ne akıllı bir burnun var, Chase!" dedi Skye.»
   - Açıklama: Burun akıllı olmaz; sıfat öznesine uymuyor ve mecazlı bir kullanım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Ne akıllı bir burnun var"
   - Cümle 8: «"Ne akıllı bir burnun var, Chase!" dedi Skye.»
   - Açıklama: Burun akıllı olmaz; mecazlı bir kullanım.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Chase boş kutuyu kapattı ve çöpü dağda bırakmadı"
   - Cümle 12: «Chase boş kutuyu kapattı ve çöpü dağda bırakmadı.»
   - Açıklama: Çöp bırakmama ayrıntısı olaydan çıkmıyor ve hikayede bir işlevi yok.
   - Açıklama: Çöp ayrıntısı olaydan çıkmıyor ve sorunla ilgisiz bir ek ders olarak araya giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0009` birebir aynı, ardından `@onarim: d652a4691abfe1e3af030dfd97251f7c95a20874`, sonra gövde.

### Hikâye 9: tohum chase-0010 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0010
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'başörtüsü', fiil 'aramak', sıfat 'işaretli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: koşarken arkadaşının kalesini yıktı | özür dileyip kaleyi birlikte yeniden yaptı
@tohum: chase-0010
@degisim: başörtüsü -> top
Kumsalda Chase topuyla oynuyordu. Marshall da kumdan bir kale yapmıştı; kapısı beyaz taşlarla işaretliydi. Chase topunun peşinden koşarken kaleyi görmedi ve ona çarptı. Kalenin tepesi yıkıldı ve beyaz taşlar kuma dağıldı. Marshall üzgün üzgün kaleye baktı. "Özür dilerim, Marshall, gel kaleyi birlikte yapalım," dedi Chase. İkisi ıslak kumla kalenin tepesini yeniden yaptı. Chase beyaz taşları kumda aradı ve hepsini buldu. Marshall taşları yine kapıya dizdi. Sonra Chase mavi şapkasını kalenin en üstüne koydu. "Şimdi bu bir polis kalesi oldu!" dedi Marshall ve güldü. İkisi kaleden biraz uzakta mutlu mutlu top oynadı.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür dileyip kaleyi birlikte yeniden yaptı"
   - Cümle 0 (plan satırı): «koşarken arkadaşının kalesini yıktı | özür dileyip kaleyi birlikte yeniden yaptı»
   - Açıklama: Gövdede Chase hiç özür dilemiyor; plan çözümü yanlış söylüyor.
   - Açıklama: Plan özür dilendiğini söylüyor ama gövdede Chase hiç özür dilemiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "kapısı beyaz taşlarla işaretliydi"
   - Cümle 2: «Marshall da kumdan bir kale yapmıştı; kapısı beyaz taşlarla işaretliydi.»
   - Açıklama: 'İşaretli' 3 yaşındaki çocuğun bilmeyebileceği soyut bir kelime.
   - Açıklama: 'İşaretli' kelimesi 3 yaşındaki bir çocuk için soyut ve zor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase beyaz taşları kumda aradı"
   - Cümle 8: «Chase beyaz taşları kumda aradı ve hepsini buldu.»
   - Açıklama: Çözüm kaleyi yapma, taşları arama, dizme ve şapka koyma gibi ikiden fazla adım sürüyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Chase mavi şapkasını kalenin en üstüne koydu"
   - Cümle 10: «Sonra Chase mavi şapkasını kalenin en üstüne koydu.»
   - Açıklama: Tohumdaki şapka özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase mavi şapkasını kalenin en üstüne koydu"
   - Cümle 10: «Sonra Chase mavi şapkasını kalenin en üstüne koydu.»
   - Açıklama: Tohumdaki şapka özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra Chase mavi şapkasını kalenin en üstüne koydu"
   - Cümle 10: «Sonra Chase mavi şapkasını kalenin en üstüne koydu.»
   - Açıklama: Çözüm kaleyi yeniden yapma, taşları arama, taşları dizme ve şapka koyma olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0010` birebir aynı, `@degisim: başörtüsü -> top` (tutuyorsan), ardından `@onarim: 8a3b37c47e2832a2e26ae9b414fe843742052bcc`, sonra gövde.

### Hikâye 10: tohum chase-0011 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Ryder
@tohum: chase-0011
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'inci', fiil 'parlamak', sıfat 'şanslı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Ryder
@plan: bilye düştü ve uzun otların arasında kayboldu | özür diledi ve bilyeyi kokusundan buldu
@tohum: chase-0011
@degisim: inci -> bilye
Bir sabah Ryder parkta Chase'e şanslı bilyesini gösteriyordu. Chase sevinçle zıpladı ve yanlışlıkla Ryder'ın eline çarptı. Bilye yere düştü ve uzun otların arasında kayboldu. "Özür dilerim, Ryder," dedi Chase. Sonra burnunu otlara yaklaştırdı ve kokladı. Bilyenin üstünde Ryder'ın elinin kokusu vardı. Chase bu kokuyu izledi ve bir çalının dibinde durdu. Orada küçük, mavi bir bilye güneşte parladı. Chase bilyeyi burnuyla Ryder'a doğru itti. "Teşekkürler, Chase!" dedi Ryder. Chase çok sevindi, çünkü Ryder'ın şanslı bilyesini bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Chase'e şanslı bilyesini gösteriyordu"
   - Cümle 1: «Bir sabah Ryder parkta Chase'e şanslı bilyesini gösteriyordu.»
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0011` birebir aynı, `@degisim: inci -> bilye` (tutuyorsan), ardından `@onarim: 162a73466cfc54f12e8770a3905f2e330391f376`, sonra gövde.
