# Editör görevi (onarım): Chase, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar25.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0073 (deneme 5 -> 6)

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
@plan: güneş yüzünden halatı göremedi ve atlayamadı | şapkasını gözlerinin üstüne indirdi ve on kez atladı
@tohum: chase-0073
@degisim: farklı -> geniş
Parkta kuşlar ötüyordu. Ryder halatı yerde döndürüyordu ve Chase üstünden atlıyordu. Chase on kez atlamak istiyordu, ama güneş çok parlaktı. Chase halatı göremedi ve hiç atlayamadı. Ryder halatı durdurdu. "Güneş yüzünden halatı göremiyorum, Ryder," dedi Chase. Sonra mavi şapkasının geniş önünü gözlerinin üstüne indirdi. Artık halatı çok iyi görüyordu. "Hazırım, Ryder, halatı döndür!" dedi Chase. Halat ona doğru geldi ve Chase hemen atladı. Ryder yüksek sesle saydı ve Chase tam on kez atladı. İkisi halat oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Chase halatı göremedi ve hiç atlayamadı"
   - Cümle 4: «Chase halatı göremedi ve hiç atlayamadı.»
   - Açıklama: İkinci cümlede Chase halatın üstünden atlıyordu denirken burada hiç atlayamadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0073` birebir aynı, `@degisim: farklı -> geniş` (tutuyorsan), ardından `@onarim: 7252724b56799a1fae1fbfb7d426b18a11aa153b`, sonra gövde.

### Hikâye 2: tohum chase-0075 (deneme 5 -> 6)

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
@plan: güneş karda parladığı için sesin geldiği yeri göremedi | şapkasını gözlerinin üstüne indirdi ve dala takılan bezi buldu
@tohum: chase-0075
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken pat pat diye bir ses duydu. Belki küçük bir hayvan bir yere sıkışmıştı. Sesin geldiği yere baktı, ama güneş karda çok parlıyordu. Chase uzağı hiç göremedi. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi uzaktaki çam ağacını iyi görüyordu. Ağacın alçak bir dalında gri bir şey dönüyordu. Chase ağaca doğru yavaşça yürüdü. Orada hayvan yoktu, dala takılmış gri bir bez vardı. Rüzgar esince bez dalın etrafında dönüyor ve ses çıkarıyordu. Chase bezi dişleriyle çekip daldan aldı. Ses hemen durdu. Chase bundan sonra güneşte şapkasını hep aşağı indirdi.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Belki küçük bir hayvan bir yere sıkışmıştı"
   - Cümle 3: «Belki küçük bir hayvan bir yere sıkışmıştı.»
   - Açıklama: Kaynağı bilinmeyen sesle sıkışmış bir hayvan ihtimali küçük çocuk için ürkütücü bir gerilim yaratıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Belki küçük bir hayvan bir yere sıkışmıştı.»
   - Açıklama: Plandaki sorun olan güneşin karda parlayıp görmeyi engellemesi ilk üç cümlede değil ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0075` birebir aynı, ardından `@onarim: d6195922c1bb3cfa7e2ae570144a9bea31bb2316`, sonra gövde.

### Hikâye 3: tohum chase-0081 (deneme 5 -> 6)

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
Kumsalda sert bir rüzgar esiyordu. Chase mamasını yiyecekti, ama mama kabı yerinde yoktu. Rüzgar hafif kabı uzağa götürmüştü ve mama yol boyunca dökülmüştü. Chase kumda küçük mama taneleri gördü. Kumdaki taneler uzağa doğru çoğalıyordu. Orada garip bir şey parlıyordu, ama güneş yüzünden Chase onu iyi göremedi. Chase mavi şapkasını gözlerinin üstüne indirdi. Şapkanın gölgesinde iyice baktı ve kendi mama kabını gördü. Kabın dibinde biraz mama kalmıştı. Chase oraya koştu, kabı ağzıyla aldı ve yerine geri getirdi. Sonra kalanını yedi. Chase çok sevindi, çünkü kaybolan kabını bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kumdaki taneler uzağa doğru çoğalıyordu"
   - Cümle 5: «Kumdaki taneler uzağa doğru çoğalıyordu.»
   - Açıklama: Taneler çoğalmaz; yol boyunca dizilmiş tanelere 'çoğalıyordu' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0081` birebir aynı, `@degisim: tekerlekli -> garip` (tutuyorsan), ardından `@onarim: 8d73fe050ef35765be5c617bd0814c9963b40956`, sonra gövde.

### Hikâye 4: tohum chase-0086 (deneme 4 -> 5)

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
@plan: tek top vardı ve ikisi de ilk atmak istedi | sırayı düşündü ve ilk atışı arkadaşına verdi
@tohum: chase-0086
@degisim: raf -> top
Chase ile Marshall karlı dağda bir top oyunu kuruyordu. Chase karın içine bir dal dikti ve ikisi topu bu dala atacaktı. Ama tek bir top vardı ve ikisi de onu ilk atmak istedi. Oyunda sıra kuralı vardı: topu bir kez Chase, bir kez Marshall atardı. "Önce sen at, Marshall," dedi Chase. "Teşekkürler, Chase, sonra sıra sende," dedi Marshall. Marshall attı ve top dala değdi. Çalışkan Marshall topu koşarak geri getirdi. Sonra Chase topu attı ve dalı vurdu. Chase ile Marshall çok sevindi, çünkü oyunları yine eğlenceliydi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oyunda sıra kuralı vardı"
   - Cümle 4: «Oyunda sıra kuralı vardı: topu bir kez Chase, bir kez Marshall atardı.»
   - Açıklama: 'Sıra kuralı' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0086` birebir aynı, `@degisim: raf -> top` (tutuyorsan), ardından `@onarim: ef6b8da807647f20053cd8594d4a8b8379c8e8c7`, sonra gövde.

### Hikâye 5: tohum chase-0091 (deneme 4 -> 5)

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
@plan: top dar bir deliğe düştü ve patisi yetişemedi | deliğe girmedi ve arkadaşından yardım istedi
@tohum: chase-0091
@degisim: umutlu -> dar
Chase kamp yerinde kırmızı topuyla oynuyordu. Top yuvarlandı ve bir ağacın yanındaki dar bir deliğe düştü. Chase patisini uzattı ama topa yetişemedi. Ekibin bir kuralı vardı: dar deliğe girmek yoktu. Bu yüzden Chase yardım için etrafına baktı. Ağaçların arasından bir kürek sesi geliyordu. Chase bu sesi hemen tanıdı. "Rubble, topum deliğe düştü, yardım eder misin?" diye sordu Chase. "Tabii, Chase," dedi Rubble. Rubble küreğiyle deliği biraz büyüttü. Chase deliğin yanında bekledi. Sonra patisini uzattı ve topunu çıkardı. "Teşekkürler, Rubble, iyi ki sana seslendim!" dedi Chase.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ekibin bir kuralı vardı"
   - Cümle 4: «Ekibin bir kuralı vardı: dar deliğe girmek yoktu.»
   - Açıklama: 'Kural' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Rubble küreğiyle deliği biraz büyüttü"
   - Cümle 10: «Rubble küreğiyle deliği biraz büyüttü.»
   - Açıklama: Sorun patinin topa yetişememesi ama deliği genişletmek derinliği değiştirmiyor, çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0091` birebir aynı, `@degisim: umutlu -> dar` (tutuyorsan), ardından `@onarim: 9a039da9420f177a906c4cd1389fa28fd6185d0c`, sonra gövde.

### Hikâye 6: tohum chase-0092 (deneme 4 -> 5)

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
@plan: dalga kovayı yuvarladı ve köpek topun yerini bulamadı | kumu kokladı ve topun yerini bulup kazdı
@tohum: chase-0092
@degisim: balkabağı -> kova
Chase kumsalda eğlenceli bir oyun oynuyordu. Benekli topunu kuma gömdü ve yanına kırmızı kovasını koydu. Ama küçük bir dalga kovayı uzağa yuvarladı ve Chase topun yerini bulamadı. Chase önce iki yeri yan yana kazdı. İki çukur birleşti ama top orada da yoktu. Chase kumlu kulaklarını salladı ve güldü. Sonra burnunu kuma yaklaştırdı ve dikkatle kokladı. Topunun kokusu biraz uzaktan geliyordu. Chase oraya koştu ve patileriyle kumu açtı. Benekli top kumun içinden çıktı. Chase topu yeniden gömdü ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İki çukur birleşti ama top orada da yoktu"
   - Cümle 5: «İki çukur birleşti ama top orada da yoktu.»
   - Açıklama: Çukurların birleşmesi olayda hiçbir işe yaramayan, sebepsiz bir ayrıntı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "patileriyle kumu açtı"
   - Cümle 9: «Chase oraya koştu ve patileriyle kumu açtı.»
   - Açıklama: Kum açılmaz; 'kumu eşeledi' ya da 'kazdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0092` birebir aynı, `@degisim: balkabağı -> kova` (tutuyorsan), ardından `@onarim: 4955770b447cb554272c105d2f25e2cdb793c22b`, sonra gövde.

### Hikâye 7: tohum chase-0093 (deneme 4 -> 5)

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
@plan: çizginin ortası ayakkabıyla silindi | boşluğa basmadı ve ortaya yeni bir çizgi çizdi
@tohum: chase-0093
@degisim: tomurcuk -> tebeşir
Chase ile Ryder kulübelerin önünde çizgi oyunu oynuyordu. Ryder yere tebeşirle uzun, dalgalı bir çizgi çizmişti. Ama Ryder yürürken ayakkabısıyla çizginin ortasını sildi. "Sıra sende, Chase," dedi Ryder ve kulübeye yaslandı. Oyunun bir kuralı vardı: çizginin dışına basmak yoktu. Ama çizginin ortası boştu. Chase tebeşiri patisiyle tuttu ve ortaya yeni bir çizgi çizdi. Ryder çizgiye baktı ve sevindi. "Çok güzel olmuş, hadi yürü," dedi Ryder. Chase çizginin üstünde yavaş yavaş yürüdü. Sonra Chase ile Ryder oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "boşluğa basmadı ve ortaya"
   - Cümle 0 (plan satırı): «çizginin ortası ayakkabıyla silindi | boşluğa basmadı ve ortaya yeni bir çizgi çizdi»
   - Açıklama: Gövdede Chase'in boşluğa basmadığı anlatılmıyor; çözüm yalnız yeni çizgi çizmek.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ortaya yeni bir çizgi çizdi"
   - Cümle 7: «Chase tebeşiri patisiyle tuttu ve ortaya yeni bir çizgi çizdi.»
   - Açıklama: 'Ortaya' burada 'çizginin ortasına' anlamında yanlış kullanılmış; anlam belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0093` birebir aynı, `@degisim: tomurcuk -> tebeşir` (tutuyorsan), ardından `@onarim: 0340bbe770ac84cccd85e58007855a03bba46f27`, sonra gövde.

### Hikâye 8: tohum chase-0096 (deneme 3 -> 4)

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
@plan: rüzgar yastığı suya uçurdu | kuralı biliyordu ve suya yalnız girmeden yastığı getirdi
@tohum: chase-0096
@degisim: değerli -> yumuşak
Bir sabah Ryder ile Chase kumsaldaydı. Ryder kumda oturmak için yumuşak, yeşil yastığını getirmişti. Ama güçlü bir rüzgar esti ve yastığı suya uçurdu. "Chase, yastığı getirir misin?" diye sordu Ryder. Kumsalda bir kural vardı. Kimse tek başına suya girmezdi. Chase kuralı biliyordu. "Ryder, suya benimle gelir misin?" diye sordu Chase. İkisi sığ suya birlikte girdi. Chase yastığı ağzıyla tuttu ve kıyıya getirdi. "Aferin, Chase, yastığım geri geldi!" dedi Ryder. Ryder güneşli bir yer seçti ve ıslak yastığı oraya koydu. Chase de yanına uzandı ve ikisi mutlu mutlu denizi seyretti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi sığ suya birlikte girdi"
   - Cümle 9: «İkisi sığ suya birlikte girdi.»
   - Açıklama: Rüzgarın uçurduğu eşyayı almak için denize girmek, çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Uçan eşyayı almak için bir çocuk ve köpek denize giriyor; çocuğun taklit edebileceği biçimde suya giriliyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Chase de yanına uzandı"
   - Cümle 13: «Chase de yanına uzandı ve ikisi mutlu mutlu denizi seyretti.»
   - Açıklama: 'yanına' zamirinin Ryder'ı mı yastığı mı gösterdiği belli değil ve 'de' Ryder'ın da uzandığını ima ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0096` birebir aynı, `@degisim: değerli -> yumuşak` (tutuyorsan), ardından `@onarim: c4b758b0dd88ac08bc3cf0f907c6848e2e0442ad`, sonra gövde.

### Hikâye 9: tohum chase-0098 (deneme 3 -> 4)

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
@plan: kardan köpek bembeyazdı ve polis köpeğine benzemiyordu | kardan köpeğe yelek giydirdi ve kendi mavi şapkasını taktı
@tohum: chase-0098
Karlı dağda Chase ile Ryder küçük bir kar şenliği hazırlıyordu. Şenlik için Chase gibi olsun diye kardan bir köpek yapmışlardı. Ama kardan köpek bembeyazdı ve hiç Chase'e benzemiyordu. Kardan köpek için Ryder çantasına yumuşacık bir yelek koymuştu. Chase yeleği ağzıyla aldı ve kardan köpeğe giydirdi. "Güzel oldu ama bir şey eksik," dedi Ryder. Chase kardan köpeğe dikkatle baktı. Sonra kendi mavi şapkasını çıkardı ve kardan köpeğin başına taktı. Kardan köpek yeleği ve şapkasıyla güzelce süslendi. Chase sevinçle havladı ve kuyruğunu salladı. "Harika, Chase, kardan köpek tıpkı senin gibi oldu!" dedi Ryder.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kardan köpek için Ryder çantasına yumuşacık bir yelek koymuştu"
   - Cümle 4: «Kardan köpek için Ryder çantasına yumuşacık bir yelek koymuştu.»
   - Açıklama: Çözümün yarısı olan yelek sebepsizce ve hazır biçimde yan karakterin çantasından çıkıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Kardan köpek yeleği ve şapkasıyla"
   - Cümle 9: «Kardan köpek yeleği ve şapkasıyla güzelce süslendi.»
   - Açıklama: 'Kardan köpek' ifadesi hikaye boyunca gereksizce çok kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0098` birebir aynı, ardından `@onarim: 2f2f039fd0a78413d8a611a20eb6f00995c1dfd3`, sonra gövde.

### Hikâye 10: tohum chase-0100 (deneme 3 -> 4)

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
@plan: portakal yuvarlandı ve ağır bir tahtanın altına kaçtı | kokladı ve tahtayı kaldırmak için arkadaşından yardım istedi
@tohum: chase-0100
Martılar kumsalda bağırıyordu. Chase ile Rubble iskelenin yanında piknik yapıyordu. Chase'in portakalı ağzından düştü ve iskelenin arkasına yuvarlandı. Chase oraya koştu ama portakalı göremedi. Burnunu yere yaklaştırdı ve kokladı. Portakalın kokusu büyük bir tahtanın altından geliyordu. Chase tahtayı itti ama tahta çok ağırdı. "Rubble, bu tahtayı birlikte kaldıralım mı?" diye sordu Chase. Rubble hemen geldi. İkisi tahtayı birlikte kaldırdı ve Chase portakalı aldı. Sonra portakalı Rubble ile paylaştı. Rubble da Chase'e peynirli sandviçinden bir parça verdi. Chase bundan sonra ağır bir şeyi kaldıramayınca arkadaşından yardım istedi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tahtanın altına kaçtı"
   - Cümle 0 (plan satırı): «portakal yuvarlandı ve ağır bir tahtanın altına kaçtı | kokladı ve tahtayı kaldırmak için arkadaşından yardım istedi»
   - Açıklama: Portakal kaçmaz; fiil cansız özneye uymuyor, 'yuvarlandı' olmalı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Chase bundan sonra ağır"
   - Cümle 13: «Chase bundan sonra ağır bir şeyi kaldıramayınca arkadaşından yardım istedi.»
   - Açıklama: Alışkanlık anlatan cümlede '-dı' yerine '-rdı' gerekir; 'isterdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0100` birebir aynı, ardından `@onarim: 64dcad574d57228bd45fe92d465d4d4b334ddda7`, sonra gövde.
