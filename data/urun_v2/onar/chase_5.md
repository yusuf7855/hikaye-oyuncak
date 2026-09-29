# Editör görevi (onarım): Chase, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0002 (deneme 5 -> 6)

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
Chase kumsalda sarı bir uçurtma uçuruyordu. Birden güçlü bir rüzgar esti ve uçurtma iskeleye doğru gitti. Uçurtmanın ipi iskelenin kısa bir direğine dolandı. Uçurtma tahtaların üstüne indi ve orada kaldı. Chase hemen iskeleye koşmak istedi. Ama Chase kurallara uydu ve iskelede koşmadı. Yavaş yavaş yürüdü ve tahtadaki uçurtmaya hiç basmadı. İp direğe düğüm olmuştu. Chase düğümü dişleriyle dikkatle çözdü. Sonra uçurtmayı aldı ve düz kuma geri döndü. Biraz koştu ve uçurtma tekrar havaya yükseldi. Chase çok sevindi, çünkü sarı uçurtması yine gökyüzündeydi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 6: «Ama Chase kurallara uydu ve iskelede koşmadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0002` birebir aynı, `@degisim: pirinç -> uçurtma` (tutuyorsan), ardından `@onarim: d9d48af6c6b678f49336deafe838789d8003c8df`, sonra gövde.

### Hikâye 2: tohum chase-0003 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: güneş çok parlaktı ve sarı çiçek solmaya başladı | şapkasıyla çiçeğe gölge yaptı
@tohum: chase-0003
@degisim: sabunlu -> parlak
Bir sabah Chase kamp yerinde çiçek sulama oyunu oynuyordu. Kamp valizinden bir şişe su çıkardı ve çiçekleri suladı. Ama ağaçlardan uzakta yetişen küçük sarı bir çiçek parlak güneşte solmaya başlamıştı. Çiçeğin üstünde hiç gölge yoktu. Chase bu çiçeğe hemen yardım etmek istedi. Mavi şapkasını çıkardı ve ağzıyla çiçeğin üstünde tuttu. Şapka çiçeğin üstüne küçük bir gölge yaptı. Biraz sonra çiçek yeniden dik durdu. Chase çok sevindi, çünkü sarı çiçeği kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kamp valizinden bir şişe su çıkardı ve çiçekleri suladı"
   - Cümle 2: «Kamp valizinden bir şişe su çıkardı ve çiçekleri suladı.»
   - Açıklama: Su kurulup solan çiçek için kullanılmıyor; sulama ayrıntısı sorunla bağlantısız kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0003` birebir aynı, `@degisim: sabunlu -> parlak` (tutuyorsan), ardından `@onarim: 1fd19d42cb1008541fb5e3b6ce7842d3f518dd2c`, sonra gövde.

### Hikâye 3: tohum chase-0004 (deneme 5 -> 6)

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
@plan: saklandı ama mavi şapkası görünüyordu | şapkasını karla bembeyaz yaptı ve yeniden saklandı
@tohum: chase-0004
@degisim: kilit -> kar
Bir sabah Chase ile Rubble karlı dağda saklambaç oynuyordu. Chase büyük bir kar yığınının arkasına saklandı. Ama mavi şapkası yığının üstünden görünüyordu ve Rubble onu hemen buldu. "Şapkanı gördüm, Chase!" dedi Rubble ve güldü. Chase şapkasını yumuşak karda iyice yuvarladı. Mavi şapkaya kar yapıştı ve şapka önce beyaz puantiyeli, sonra bembeyaz oldu. Chase başka bir yığının arkasına saklandı. Rubble her yere baktı ama onu bulamadı. "Buradayım!" dedi Chase ve karın arkasından zıpladı. İkisi de çok sevindi, çünkü bu oyun çok eğlenceli olmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şapka önce beyaz puantiyeli"
   - Cümle 6: «Mavi şapkaya kar yapıştı ve şapka önce beyaz puantiyeli, sonra bembeyaz oldu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "önce beyaz puantiyeli, sonra"
   - Cümle 6: «Mavi şapkaya kar yapıştı ve şapka önce beyaz puantiyeli, sonra bembeyaz oldu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0004` birebir aynı, `@degisim: kilit -> kar` (tutuyorsan), ardından `@onarim: ebf39e474571ca32af036da31978257149b1debe`, sonra gövde.

### Hikâye 4: tohum chase-0005 (deneme 5 -> 6)

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
@plan: elma kuma düştü ve her yeri kum oldu | elmayı yağmurun altında yıkadı
@tohum: chase-0005
@degisim: barışmak -> yıkamak
Chase yağmurlu bir sabah kumsalda kırmızı bir elma yiyordu. Birden elma ağzından düştü ve ıslak kumda yuvarlandı. Elmanın her yerine kum yapıştı. Chase elmayı hemen yemek istedi. Ama kurallara uydu ve kumlu elmayı yemedi. Elmayı iki patisiyle tuttu ve yağmura doğru kaldırdı. Damlalar elmanın üstüne tık tık düştü. Kum yavaş yavaş aktı ve elma tertemiz oldu. Chase kırmızı elmasına baktı ve kuyruğunu salladı. Chase çok sevindi, çünkü yağmur elmasındaki bütün kumu yıkamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama kurallara uydu ve kumlu"
   - Cümle 5: «Ama kurallara uydu ve kumlu elmayı yemedi.»
   - Açıklama: 'Kurallara uymak' hangi kural olduğu belirsiz soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama kurallara uydu"
   - Cümle 5: «Ama kurallara uydu ve kumlu elmayı yemedi.»
   - Açıklama: 'kurallara uydu' soyut bir ifade, küçük çocuk için somut değil.
   - Açıklama: 'Kurallara uymak' soyut kavram; olayda somut bir kural yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0005` birebir aynı, `@degisim: barışmak -> yıkamak` (tutuyorsan), ardından `@onarim: 07898c1444b6b102df1bae6a0bc748f252c2e541`, sonra gövde.

### Hikâye 5: tohum chase-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0012
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pasta', fiil 'tutunmak', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: süs olacak kozalak yüksek bir dala tutunuyordu | kurallara uydu, ağacı sallamadı ve bekledi
@tohum: chase-0012
@degisim: şapkalı -> yumuşak
Dağda soğuk bir rüzgar esiyordu. Chase yumuşak kardan küçük bir pasta yapmıştı ve tepesine süs arıyordu. Tek kozalak ise yüksek bir dala tutunuyordu. Chase kurallara uydu ve ağacı sallamadı. Pastanın yanında sessizce bekledi. Birden rüzgar güçlendi ve dal sallandı. Kozalak aşağı düştü ve karda kayboldu. Chase hemen koştu ve kozalağı karın içinden çıkardı. Onu dikkatlice pastanın tepesine koydu. Kardan pasta artık çok güzel görünüyordu. Chase pastanın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yüksek bir dala tutunuyordu"
   - Cümle 3: «Tek kozalak ise yüksek bir dala tutunuyordu.»
   - Açıklama: Kozalak bir şeye tutunamaz; fiil öznesine uymuyor.
   - Açıklama: Kozalak canlı değildir, dala tutunmaz; fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 4: «Chase kurallara uydu ve ağacı sallamadı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavramdır ve hangi kural olduğu belli değildir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu"
   - Cümle 4: «Chase kurallara uydu ve ağacı sallamadı.»
   - Açıklama: 'Kurallar' hangi kural olduğu belli olmayan soyut bir kavram.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase kurallara uydu ve ağacı sallamadı"
   - Cümle 4: «Chase kurallara uydu ve ağacı sallamadı.»
   - Açıklama: Çözüm sebebe yönelmiyor; Chase yalnız bekliyor ve sonuç şansa kalıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pastanın yanında sessizce bekledi"
   - Cümle 5: «Pastanın yanında sessizce bekledi.»
   - Açıklama: Beklemek sebebe (yüksek dal) yönelen bir çözüm değil.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "rüzgar güçlendi ve dal sallandı"
   - Cümle 6: «Birden rüzgar güçlendi ve dal sallandı.»
   - Açıklama: Kartın özellikler alanındaki 'kurallara uyar' özelliği sorunu çözmüyor; kozalağı rüzgar düşürüyor.
7. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Birden rüzgar güçlendi ve dal sallandı"
   - Cümle 6: «Birden rüzgar güçlendi ve dal sallandı.»
   - Açıklama: Kozalağı Chase değil rüzgar indiriyor; sorunu şans çözüyor.
   - Açıklama: Kozalağı Chase değil rüzgar düşürüyor; sorunu figür çözmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0012` birebir aynı, `@degisim: şapkalı -> yumuşak` (tutuyorsan), ardından `@onarim: a82a033880d01b3d3e7d7e28bdf553cb38648978`, sonra gövde.

### Hikâye 6: tohum chase-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Rubble
@tohum: chase-0013
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'tekne', fiil 'yardımlaşmak', sıfat 'sağlıklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | deniz | Rubble
@plan: ters duran teknenin altından bir ses geldi | arkadaşıyla tekneyi kaldırıp sesi yapan kabukları buldu
@tohum: chase-0013
@degisim: sağlıklı -> renkli
Bir sabah Chase ile Rubble kumsalda yürüyordu. Birden ters duran küçük bir tekneden "tık tık" diye bir ses geldi. Chase bu sesi çok merak etti. "Rubble, tekneyi birlikte kaldıralım mı?" diye sordu Chase. "Tabii, ben çok güçlüyüm," dedi Rubble. İkisi yardımlaştı ve tekneyi yavaşça kaldırdı. Altında renkli deniz kabukları vardı. Dalga gelince kabuklar tahtaya vuruyor ve bu sesi yapıyordu. Chase kabukları saklamak için mavi şapkasına doldurdu. Rubble kabuklara bakıp güldü. "Sesi birlikte bulduk, Chase!" dedi Rubble sevinçle.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "saklamak için mavi şapkasına doldurdu"
   - Cümle 9: «Chase kabukları saklamak için mavi şapkasına doldurdu.»
   - Açıklama: Tohumdaki şapka özelliği sorun çözüldükten sonra yalnız eşya olarak geçiyor, çözüme katkısı yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kabukları saklamak için mavi şapkasına doldurdu"
   - Cümle 9: «Chase kabukları saklamak için mavi şapkasına doldurdu.»
   - Açıklama: Tohumdaki özellik şapka sorunun çözümünde işe yaramıyor, yalnız sonradan kap olarak kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kabukları saklamak için mavi şapkasına doldurdu"
   - Cümle 9: «Chase kabukları saklamak için mavi şapkasına doldurdu.»
   - Açıklama: Şapka ayrıntısı olaya bağlanmıyor ve hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0013` birebir aynı, `@degisim: sağlıklı -> renkli` (tutuyorsan), ardından `@onarim: e374eda647e9f8fb72643cf2bce5c520655be3bd`, sonra gövde.

### Hikâye 7: tohum chase-0014 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0014
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'cips', fiil 'yoğurmak', sıfat 'sevecen'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: cips paketi karın altında kayboldu | burnuyla kokladı ve paketi karın içinden çıkardı
@tohum: chase-0014
Kar yavaş yavaş yağıyordu. Chase ile Skye yemek oyunu oynuyor ve sofra hazırlıyordu. Ama cips paketi karın altında kaybolmuştu. Skye karı hamur gibi yoğurdu ve kurabiye yaptı. "Cips olmadan sofra eksik kaldı," dedi Skye. Chase burnunu kara yaklaştırdı ve dikkatle kokladı. Sonra bir yeri patileriyle hızlıca eşeledi. Sarı cips paketi karın içinden çıktı. "Buldum, Skye," dedi Chase. Sevecen Skye hemen Chase'e sarıldı. İkisi paketi kurabiyelerin yanına koydu. Chase ile Skye çok sevindi, çünkü sofra artık tamamdı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama cips paketi karın altında kaybolmuştu"
   - Cümle 3: «Ama cips paketi karın altında kaybolmuştu.»
   - Açıklama: Paketin karın altında neden kaybolduğu söylenmiyor.
   - Açıklama: Cips paketinin karın altına nasıl girdiği, yani sorunun sebebi hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0014` birebir aynı, ardından `@onarim: 8eddf4cfeaa2085741bd17e75119d36243aec79a`, sonra gövde.

### Hikâye 8: tohum chase-0015 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0015
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'çamaşır', fiil 'paketlemek', sıfat 'tedbirli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: yağmur başladı ve havlular ıslanacaktı | kurallara uydu ve havluları poşete paketledi
@tohum: chase-0015
Denizden serin bir rüzgar esiyordu. Chase havlularını kumsalda bir çamaşır ipine asmıştı. Birden yağmur başladı ve Chase hemen ipe koştu. Yağmurda herkes eşyasını toplardı, kural buydu. Chase kurallara uydu ve havluları ipten aldı. Tedbirli Chase yanında büyük bir poşet getirmişti. Havluları katladı ve poşete güzelce paketledi. Sonra poşeti sıkıca bağladı. Yağmur poşete hiç giremedi. Az sonra yağmur dindi ve güneş çıktı. Chase poşeti açtı; havlular kuru kalmıştı. Chase kuru bir havluyu kuma serdi ve üstüne mutlu mutlu uzandı.
```

**Hakem bulguları (8):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "havluları poşete paketledi"
   - Cümle 0 (plan satırı): «yağmur başladı ve havlular ıslanacaktı | kurallara uydu ve havluları poşete paketledi»
   - Açıklama: Plan satırında 'poşete paketledi' yanlış fiil kullanımı var.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "herkes eşyasını toplardı, kural buydu"
   - Cümle 4: «Yağmurda herkes eşyasını toplardı, kural buydu.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaş için uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 5: «Chase kurallara uydu ve havluları ipten aldı.»
   - Açıklama: 'Kurallara uymak' soyut bir anlatım.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurallara uydu ve havluları"
   - Cümle 5: «Chase kurallara uydu ve havluları ipten aldı.»
   - Açıklama: Plan satırında soyut 'kurallara uydu' anlatımı var.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Tedbirli Chase yanında büyük bir poşet getirmişti"
   - Cümle 6: «Tedbirli Chase yanında büyük bir poşet getirmişti.»
   - Açıklama: Tohumdaki özellik kurallara uymak; tedbirlilik karttaki özellikler alanında olmayan ikinci bir özellik olarak ekleniyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Tedbirli Chase yanında büyük"
   - Cümle 6: «Tedbirli Chase yanında büyük bir poşet getirmişti.»
   - Açıklama: Tohumdaki özellik kural; tedbirlilik çözüme ikinci bir özellik olarak ekleniyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tedbirli Chase yanında büyük bir poşet getirmişti"
   - Cümle 6: «Tedbirli Chase yanında büyük bir poşet getirmişti.»
   - Açıklama: Poşet önceden kurulmadan tam çözüm anında beliriyor.
   - Açıklama: Çözümü sağlayan poşet önceden kurulmadan tam gerektiği anda sebepsizce beliriyor.
8. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "poşete güzelce paketledi"
   - Cümle 7: «Havluları katladı ve poşete güzelce paketledi.»
   - Açıklama: 'Paketlemek' yönelme ekli nesneyle kullanılmaz; 'poşete koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0015` birebir aynı, ardından `@onarim: 79a9e1ca1fc4a8103e286f03a5e3fc6694b262ee`, sonra gövde.

### Hikâye 9: tohum chase-0016 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0016
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'pilav', fiil 'kilitlemek', sıfat 'aceleci'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: karlı dağda bilinmeyen bir pilav kokusu geldi | burnuyla kokuyu izleyip yemek kutusunu buldu
@tohum: chase-0016
Dağın karlı yolunda Chase ile Rubble yürüyordu. Birden Chase güzel bir pilav kokusu aldı. "Bu koku nereden geliyor?" diye sordu Chase. "Ben de bilmiyorum," dedi Rubble. Chase burnunu yere yaklaştırdı ve kokuyu izledi. Büyük bir kayanın arkasında bir yemek kutusu buldu. Kutunun kapağı biraz açıktı ve içi pilav doluydu. "Bu benim yemek kutum!" dedi Rubble sevinçle. Aceleci Rubble koşarken kutusu çantasından düşmüştü. Chase kutunun kapağını kapattı ve kilitledi. Rubble kutuyu çantasına sıkıca koydu. Chase ile Rubble bundan sonra yemek kutusunu hep kilitli taşıdı.
```

**Hakem bulguları (8):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "burnuyla kokuyu izleyip yemek kutusunu buldu"
   - Cümle 0 (plan satırı): «karlı dağda bilinmeyen bir pilav kokusu geldi | burnuyla kokuyu izleyip yemek kutusunu buldu»
   - Açıklama: Gövdede kutuyu Chase değil Rubble buluyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "karlı dağda bilinmeyen bir pilav kokusu geldi"
   - Cümle 0 (plan satırı): «karlı dağda bilinmeyen bir pilav kokusu geldi | burnuyla kokuyu izleyip yemek kutusunu buldu»
   - Açıklama: Gövdedeki asıl sorun Rubble'ın çantasından düşen yemek kutusu; plan bunu söylemiyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bilinmeyen bir pilav kokusu geldi"
   - Cümle 0 (plan satırı): «karlı dağda bilinmeyen bir pilav kokusu geldi | burnuyla kokuyu izleyip yemek kutusunu buldu»
   - Açıklama: Bir kokunun gelmesi çocuğun önemseyeceği bir sorun değil ve kutunun düşme sebebi geç söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "karlı dağda bilinmeyen bir pilav kokusu"
   - Cümle 0 (plan satırı): «karlı dağda bilinmeyen bir pilav kokusu geldi | burnuyla kokuyu izleyip yemek kutusunu buldu»
   - Açıklama: Bilinmeyen bir koku gerçek bir sorun değil; asıl sorun olan kayıp kutu ise sonradan ortaya çıkıyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden Chase güzel bir pilav kokusu aldı"
   - Cümle 2: «Birden Chase güzel bir pilav kokusu aldı.»
   - Açıklama: Bir pilav kokusu almak çocuğun önemseyeceği bir sorun değil.
6. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «"Bu koku nereden geliyor?" diye sordu Chase.»
   - Açıklama: İlk üç cümlede yalnız bir koku var; asıl sorun olan Rubble'ın kaybolan yemek kutusu ancak dokuzuncu cümlede ortaya çıkıyor.
7. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Aceleci Rubble koşarken kutusu çantasından düşmüştü"
   - Cümle 9: «Aceleci Rubble koşarken kutusu çantasından düşmüştü.»
   - Açıklama: Kartın yanlar alanında Rubble güçlü, şakacı ve yemek sever olarak tanımlı; acelecilik karta aykırı bir özellik.
8. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bundan sonra yemek kutusunu hep kilitli taşıdı"
   - Cümle 12: «Chase ile Rubble bundan sonra yemek kutusunu hep kilitli taşıdı.»
   - Açıklama: Kutu çantadan düştüğü için kaybolmuştu; kilitlemek bunu önlemez, ders olaydan çıkmıyor.
   - Açıklama: Kutu kapağı açıldığı için değil çantadan düştüğü için kaybolmuştu; kilitleme dersi olaydan çıkmıyor.
   - Açıklama: Kutu çantadan düştüğü için kaybolmuştu; kapağı kilitlemek bu olaydan çıkan bir ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0016` birebir aynı, ardından `@onarim: 183e89c8080253e4ae6227852cea22e625868b2c`, sonra gövde.

### Hikâye 10: tohum chase-0017 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | ev | Ryder
@tohum: chase-0017
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'kumbara', fiil 'yuvarlamak', sıfat 'tuhaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | ev | Ryder
@plan: kulübelerin önüne tatlı ama tuhaf bir koku geldi | burnuyla kokuyu izleyip düşen elmaları buldu
@tohum: chase-0017
@degisim: kumbara -> elma
Bir sabah Chase kulübesinin önünde oturuyordu. Birden rüzgarla tatlı ama tuhaf bir koku geldi. "Ryder, bu koku nereden geliyor?" diye sordu Chase. "Bilmiyorum, hadi bulalım," dedi Ryder. Chase burnunu havaya kaldırdı ve kulenin arkasına yürüdü. Ryder de arkasından koştu. Orada bir elma ağacı vardı ve yere kırmızı elmalar düşmüştü. Elmalar uzun otların arasında saklıydı. Chase onları burnuyla tek tek Ryder'a doğru yuvarladı. Ryder elmaları kucağına aldı ve güldü. "Teşekkürler, Chase, kahvaltıda hep birlikte elma yiyeceğiz!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tatlı ama tuhaf bir koku geldi"
   - Cümle 2: «Birden rüzgarla tatlı ama tuhaf bir koku geldi.»
   - Açıklama: Tatlı bir koku çocuğun önemseyeceği gerçek bir sorun değil; ortada çözülecek bir dert yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0017` birebir aynı, `@degisim: kumbara -> elma` (tutuyorsan), ardından `@onarim: c5f01b0ccae50fd347ee47eb09093d188b03e57a`, sonra gövde.

### Hikâye 11: tohum chase-0019 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0019
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'papatya', fiil 'yüklemek', sıfat 'rengarenk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: bakmadan koştu ve papatya dolu kamyona çarptı | kuralı hatırlayıp özür diledi ve papatyaları topladı
@tohum: chase-0019
Dalgalar kumsala hafifçe vuruyordu. Chase kumsalda koşuyor, Marshall ise kamyonuna papatya yüklüyordu. Chase önüne bakmadı ve rengarenk kamyona çarptı. Bütün papatyalar kuma döküldü. "Eyvah, papatyalar!" dedi Marshall üzgün bir sesle. Chase bir kuralı hatırladı: hata yapan özür diler. "Özür dilerim, Marshall, sana bakmadan koştum," dedi Chase. Sonra papatyaları tek tek topladı ve yeniden kamyona yükledi. "Sorun değil, Chase, teşekkür ederim," dedi Marshall. Marshall kamyonunu mutlu mutlu çekti. Chase bundan sonra kumsalda koşarken hep önüne baktı.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Marshall ise kamyonuna papatya yüklüyordu"
   - Cümle 2: «Chase kumsalda koşuyor, Marshall ise kamyonuna papatya yüklüyordu.»
   - Açıklama: Kartın yanlar alanında Marshall itfaiyeci köpektir; papatya taşıyan bir kamyonu kartta yok.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hata yapan özür diler"
   - Cümle 6: «Chase bir kuralı hatırladı: hata yapan özür diler.»
   - Açıklama: Anlatımda geniş zamana kayılıyor; kural cümlesi -dı'lı geçmiş zamanda değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0019` birebir aynı, ardından `@onarim: a340de8e8571d494cc27d557d63c4125797f99ea`, sonra gövde.

### Hikâye 12: tohum chase-0021 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0021
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'taş', fiil 'dolmak', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kuru kumdan yapılan kale hemen dağıldı | ıslak kumu burnuyla buldu ve kaleyi onunla yaptı
@tohum: chase-0021
Bir sabah Chase kumsalda ilk kez kumdan kale yapmayı denedi. Kovası kuru kumla doldu ve Chase onu ters çevirdi. Ama kuru kum hemen dağıldı ve kale yıkıldı. Chase burnunu kuma yaklaştırdı ve dikkatle kokladı. Su kenarındaki kum ıslak ve tuzlu kokuyordu. Chase kovayı oradaki ıslak kumla doldurdu. Kovayı ters çevirdi ve yavaşça kaldırdı. Bu kez kale hiç yıkılmadı. Kale güneşte çok güzel görünüyordu. Chase kalenin üstüne değişik renklerde küçük taşlar dizdi. Chase çok sevindi, çünkü ilk kum kalesini kendi yapmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ilk kum kalesini kendi yapmıştı"
   - Cümle 11: «Chase çok sevindi, çünkü ilk kum kalesini kendi yapmıştı.»
   - Açıklama: 'Kendi' tek başına özne olmaz; 'kendisi' ya da 'kendi başına' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kum kalesini kendi yapmıştı"
   - Cümle 11: «Chase çok sevindi, çünkü ilk kum kalesini kendi yapmıştı.»
   - Açıklama: Özne olarak 'kendi' değil 'kendisi' ya da 'kendi başına' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0021` birebir aynı, ardından `@onarim: ad64c8ff772c03a43e5c8ca001f36e102a93afeb`, sonra gövde.
