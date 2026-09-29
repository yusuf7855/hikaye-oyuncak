# Editör görevi (onarım): Chase, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0034 (deneme 1 -> 2)

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
@plan: rüzgar esince kağıt hep havaya kalkıyordu | kağıdı küçük taşlarla yere tuttu
@tohum: chase-0034
Ağaçlarda kuşlar ötüyordu. Chase parkta ilk kez mavi mürekkeple pati resmi yapmayı deniyordu. Ama rüzgar esince beyaz kağıt hep havaya kalkıyordu. Chase resmi hemen banka yapmayı düşündü. Ama parkta banklara boya sürmek yasaktı ve Chase kurallara uyardı. Bunun yerine yerden küçük taşlar topladı. Taşları kağıdın dört köşesine koydu. Artık kağıt rüzgarda hiç kıpırdamadı. Chase patisini dikkatli bir şekilde mürekkebe batırdı. Sonra kağıda düz basmaya çalıştı. Kağıtta çok güzel bir pati izi çıktı. Chase çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kağıdı küçük taşlarla yere tuttu"
   - Cümle 0 (plan satırı): «rüzgar esince kağıt hep havaya kalkıyordu | kağıdı küçük taşlarla yere tuttu»
   - Açıklama: 'Yere tuttu' dilbilgisel değil; 'yerde tuttu' ya da 'yere sabitledi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase resmi hemen banka yapmayı"
   - Cümle 4: «Chase resmi hemen banka yapmayı düşündü.»
   - Açıklama: 'Banka yapmak' bankın üstüne resim yapmak anlamını vermiyor, para bankasıyla karışıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase resmi hemen banka yapmayı düşündü"
   - Cümle 4: «Chase resmi hemen banka yapmayı düşündü.»
   - Açıklama: 'Resmi banka yapmak' anlamca yanlış; resim banka yapılmaz, 'banka çizmek' denmeli.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase resmi hemen banka yapmayı düşündü"
   - Cümle 4: «Chase resmi hemen banka yapmayı düşündü.»
   - Açıklama: Banka resim yapma fikri sorundan çıkmıyor, yalnız kural özelliğini göstermek için kurulup bırakılıyor.
   - Açıklama: Banka resim yapma fikri sorunla ilgisiz bir sapma olarak kuruluyor ve olayda işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0034` birebir aynı, ardından `@onarim: ac8ac8d79e443cd6888a47713adba4a6273ed30e`, sonra gövde.

### Hikâye 2: tohum chase-0035 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0035
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kravat', fiil 'bindirmek', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | -
@plan: rüzgar durdu ve yaprak suyun ortasında kaldı | suya girmedi ve kenarda rüzgarı bekledi
@tohum: chase-0035
@degisim: kravat -> yaprak
Bir sabah parkta, kaydırağın yanında su dolu küçük bir çukur vardı. Chase pürüzsüz bir yaprağa küçük bir kozalak bindirdi ve onu suya bıraktı. Yaprak suda yüzdü, ama rüzgar durunca çukurun ortasında kaldı. Chase suya girip onu itmek istedi. Ama Chase kurallara uyardı ve suya girmedi. Kenarda durdu ve rüzgarı bekledi. Biraz sonra hafif bir rüzgar yeniden esti. Yaprak bu kez kenara doğru yavaş yavaş yüzdü. Kozalak da düşmeden onun üstünde kaldı. Sonunda yaprak Chase'in önüne geldi. Chase onu yeniden yüzdürdü ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pürüzsüz bir yaprağa"
   - Cümle 2: «Chase pürüzsüz bir yaprağa küçük bir kozalak bindirdi ve onu suya bıraktı.»
   - Açıklama: 'Pürüzsüz' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase pürüzsüz bir yaprağa"
   - Cümle 2: «Chase pürüzsüz bir yaprağa küçük bir kozalak bindirdi ve onu suya bıraktı.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama rüzgar durunca çukurun ortasında kaldı"
   - Cümle 3: «Yaprak suda yüzdü, ama rüzgar durunca çukurun ortasında kaldı.»
   - Açıklama: Sorun rüzgarın durmasıyla geliyor ve kendiliğinden rüzgarın yeniden esmesiyle bitiyor; önemsiz, kendi kendine çözülen bir olay.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Biraz sonra hafif bir rüzgar yeniden esti"
   - Cümle 7: «Biraz sonra hafif bir rüzgar yeniden esti.»
   - Açıklama: Sorunu Chase değil kendiliğinden esen rüzgar çözüyor; Chase yalnız bekliyor.
   - Açıklama: Sorunu Chase değil rüzgar çözüyor; Chase yalnız bekliyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sonra hafif bir rüzgar yeniden esti"
   - Cümle 7: «Biraz sonra hafif bir rüzgar yeniden esti.»
   - Açıklama: Çözüm figürün bir eyleminden çıkmıyor, rüzgar sebepsizce yeniden esiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0035` birebir aynı, `@degisim: kravat -> yaprak` (tutuyorsan), ardından `@onarim: 475e5dd67eccd91dc91c1988d552be80f8a2594c`, sonra gövde.

### Hikâye 3: tohum chase-0037 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0037
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kase', fiil 'aşmak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | -
@plan: top kaseyi aştı ve otların arasında kayboldu | burnuyla kokusunu alıp taşın dibinde buldu
@tohum: chase-0037
Ormandaki kamp yerinde Chase komik bir top oyunu oynuyordu. Topu yamuk bir kütüğün üstünden boş bir kaseye atıyordu. Ama top bu kez çok hızlı gitti, kaseyi aştı ve otlara düştü. Chase otlara baktı ama hiçbir şey göremedi. Sonra burnunu yere indirdi ve topun kokusunu aldı. Otların arasında yavaşça yürüdü. Top büyük bir taşın dibinde duruyordu. Chase onu ağzıyla aldı ve kütüğün yanına döndü. Bu kez yavaşça attı. Bu sefer top tam kaseye düştü. Chase kuyruğunu salladı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu kez yavaşça attı"
   - Cümle 9: «Bu kez yavaşça attı.»
   - Açıklama: 'Bu kez' ve hemen ardından 'Bu sefer' gereksiz tekrar ediliyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu sefer top tam"
   - Cümle 10: «Bu sefer top tam kaseye düştü.»
   - Açıklama: Art arda iki cümle 'Bu kez' ve 'Bu sefer' ile başlıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0037` birebir aynı, ardından `@onarim: 312e40206ceb4eef65898bd24650f278cd1eae5a`, sonra gövde.

### Hikâye 4: tohum chase-0038 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0038
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yağmur ya da kar günü
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'çim', fiil 'birikmek', sıfat 'dürüst'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: yağmurda kalenin yüksek kulesi yıkılıyordu | mavi şapkasını kulenin üstüne koydu
@tohum: chase-0038
@degisim: dürüst -> ıslak
Bir sabah Chase ile Marshall kumsalda, çimlerin yanında bir kum kalesi yaptı. Birden bulutlar geldi ve yağmur başladı. Damlalar kalenin yüksek kulesine düştü ve kule yıkılmaya başladı. "Kulemiz yıkılıyor, Chase!" dedi Marshall. Chase mavi şapkasını çıkardı ve kulenin üstüne koydu. Artık damlalar kuleye değmedi. Kalenin çevresindeki çukurda ise yağmur suyu birikti. "Bak, kalenin küçük bir gölü oldu!" dedi Marshall ve güldü. Biraz sonra yağmur dindi. Kule ıslak kumun ortasında dimdik duruyordu. "Teşekkürler, Chase, kuleyi sen kurtardın!" dedi Marshall.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kalenin çevresindeki çukurda ise yağmur suyu birikti"
   - Cümle 7: «Kalenin çevresindeki çukurda ise yağmur suyu birikti.»
   - Açıklama: Çukur ve biriken göl sebepsiz beliriyor ve sorunun çözümünde hiçbir işe yaramıyor.
   - Açıklama: Önceden kurulmamış çukur ve göl ayrıntısı sorunla ya da çözümle ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0038` birebir aynı, `@degisim: dürüst -> ıslak` (tutuyorsan), ardından `@onarim: f3d03b3a575012eb145e3be8fefc3c799708ce60`, sonra gövde.

### Hikâye 5: tohum chase-0040 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0040
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'vanilya', fiil 'yayılmak', sıfat 'narin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: zıplarken taşa çarptı ve kurabiyeler kırıldı | özür diledi ve kırık parçaları topladı
@tohum: chase-0040
Bir sabah Chase karlı dağda sevinçle zıplıyordu. Rubble bir taşın üstüne vanilyalı kurabiyeler koymuştu. Chase zıplarken taşa çarptı, narin kurabiyeler kırıldı ve kara yayıldı. Rubble kırık kurabiyelere üzgün üzgün baktı. Chase kurallara uyardı: hata yapan özür dilerdi. "Özür dilerim, Rubble, dikkat etmeden zıpladım," dedi Chase. Sonra parçaları kardan tek tek topladı. Rubble bir parçayı ağzına attı ve güldü. "Kırık kurabiye de çok güzel oluyor," dedi Rubble. İki arkadaş parçaları birlikte yedi. Chase çok sevindi, çünkü Rubble ona hiç kızmamıştı.
```

**Hakem bulguları (5):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Chase zıplarken taşa çarptı"
   - Cümle 3: «Chase zıplarken taşa çarptı, narin kurabiyeler kırıldı ve kara yayıldı.»
   - Açıklama: Zıplarken taşa çarpmak çocuk için bir yaralanma ya da acı çağrışımı taşıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "narin kurabiyeler kırıldı"
   - Cümle 3: «Chase zıplarken taşa çarptı, narin kurabiyeler kırıldı ve kara yayıldı.»
   - Açıklama: 'narin' kelimesini 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Narin' kelimesini 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı: hata yapan özür dilerdi"
   - Cümle 5: «Chase kurallara uyardı: hata yapan özür dilerdi.»
   - Açıklama: Kural ve hata gibi soyut kavramlar 3 yaş için uygun değil.
   - Açıklama: Kurallara uymak ve hata yapmak soyut, genel bir anlatım; 3 yaşındaki çocuğa uygun değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra parçaları kardan tek tek topladı"
   - Cümle 7: «Sonra parçaları kardan tek tek topladı.»
   - Açıklama: Parçaları toplamak kırık kurabiyeleri düzeltmiyor; çözüm sorunu gidermiyor.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kırık kurabiye de çok güzel oluyor"
   - Cümle 9: «"Kırık kurabiye de çok güzel oluyor," dedi Rubble.»
   - Açıklama: Sorunu kırık kurabiyeyi kabul eden Rubble kapatıyor, Chase değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0040` birebir aynı, ardından `@onarim: cde52c9dde5472b456197f5c65d4895188d64e40`, sonra gövde.
