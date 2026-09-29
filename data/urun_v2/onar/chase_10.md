# Editör görevi (onarım): Chase, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0010 (deneme 3 -> 4)

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
@plan: koşarken arkadaşının kalesini yıktı | özür diledi ve şapkasıyla kaleye yeni bir tepe yaptı
@tohum: chase-0010
@degisim: başörtüsü -> top
Kumsalda Marshall kumdan bir kale yapmıştı. Chase de yıldız işaretli topunu arıyordu. Chase topu görünce hemen koştu ve Marshall'ın kalesine çarptı. Kalenin tepesi yıkıldı ve kuma dağıldı. Marshall üzgün üzgün kaleye baktı. "Özür dilerim, Marshall," dedi Chase. Chase mavi şapkasını ıslak kumla doldurdu. Şapkayı kalenin üstüne ters çevirdi ve yavaşça kaldırdı. Kalenin üstünde yuvarlak yeni bir tepe vardı. "Kale yine çok güzel oldu, teşekkürler, Chase!" dedi Marshall. İkisi kaleden biraz uzakta mutlu mutlu top oynadı.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Kale yine çok güzel oldu, teşekkürler, Chase!"
   - Cümle 10: «"Kale yine çok güzel oldu, teşekkürler, Chase!" dedi Marshall.»
   - Açıklama: İki ayrı cümle virgülle birleştirilmiş; noktalama yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0010` birebir aynı, `@degisim: başörtüsü -> top` (tutuyorsan), ardından `@onarim: 882677b93999092f1315879f1449c89d86a574ff`, sonra gövde.

### Hikâye 2: tohum chase-0012 (deneme 4 -> 5)

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
@plan: süs olacak kozalak biraz yüksek bir dalda duruyordu | ağaca tırmanmadı, gövdeye tutundu ve kozalağı aldı
@tohum: chase-0012
@degisim: şapkalı -> yumuşak
Dağda soğuk bir rüzgar esiyordu. Chase yumuşak kardan küçük bir pasta yapmıştı ve tepesine süs arıyordu. Ağaçtaki tek kozalak ise biraz yüksek bir dalda duruyordu. Chase önce ağaca tırmanmak istedi. Ama kurala göre karlı ağaca çıkmak yasaktı, çünkü dallar kaygandı. Chase ön patileriyle ağacın gövdesine tutundu ve arka ayaklarının üstünde durdu. Sonra kozalağı ağzıyla yavaşça kopardı. Onu dikkatlice pastanın tepesine koydu. Kardan pasta artık çok güzel görünüyordu. Chase pastanın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama kurala göre karlı ağaca çıkmak yasaktı"
   - Cümle 5: «Ama kurala göre karlı ağaca çıkmak yasaktı, çünkü dallar kaygandı.»
   - Açıklama: 'Kural' ve 'yasak' soyut kavramlar; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kurala göre karlı ağaca çıkmak yasaktı"
   - Cümle 5: «Ama kurala göre karlı ağaca çıkmak yasaktı, çünkü dallar kaygandı.»
   - Açıklama: 'Kurala göre' soyut ve hangi kural olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0012` birebir aynı, `@degisim: şapkalı -> yumuşak` (tutuyorsan), ardından `@onarim: 379ec826dd6bb024961ef7b1b788f1e87e9d6b84`, sonra gövde.

### Hikâye 3: tohum chase-0015 (deneme 4 -> 5)

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
@plan: havlular ipte asılıydı ve yağmur başladı | havluları ipten aldı ve poşete koyup paketledi
@tohum: chase-0015
@degisim: tedbirli -> büyük
Denizden serin bir rüzgar esiyordu. Chase kumsalda havlularını kurusun diye bir çamaşır ipine asmıştı. Havluları getirdiği büyük poşet de ipin altında duruyordu. Havlular kurumuştu ama birden yağmur başladı. Kurala göre yağmurda eşyalar hemen toplanırdı. Chase koştu ve havluları ipten aldı. Onları katladı ve poşete koyup sıkıca paketledi. Poşete hiç yağmur girmedi. Az sonra yağmur dindi ve güneş çıktı. Chase poşeti açtı; havlular kuru kalmıştı. Chase kuru bir havluyu kuma serdi ve üstüne mutlu mutlu uzandı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Havlular kurumuştu ama birden yağmur başladı"
   - Cümle 4: «Havlular kurumuştu ama birden yağmur başladı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede ortaya çıkıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "birden yağmur başladı"
   - Cümle 4: «Havlular kurumuştu ama birden yağmur başladı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala göre yağmurda eşyalar"
   - Cümle 5: «Kurala göre yağmurda eşyalar hemen toplanırdı.»
   - Açıklama: 'Kurala göre' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0015` birebir aynı, `@degisim: tedbirli -> büyük` (tutuyorsan), ardından `@onarim: 3f147542655c413a27d70a3f8b9416294211b2e1`, sonra gövde.

### Hikâye 4: tohum chase-0017 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: sepet düştü ve elmalar uzun otların arasında kayboldu | burnuyla kokuyu izleyip elmaları buldu ve yuvarladı
@tohum: chase-0017
@degisim: kumbara -> elma
Bir sabah Chase kulübesinin önünde oturuyordu. Ryder bütün köpekler için bir sepet elma getirdi. Ama sepet elinden kaydı ve elmalar uzun otların arasına yuvarlandı. Ryder otlara baktı ama hiçbir elma göremedi. "Çok tuhaf, elmalar nereye gitti?" diye sordu Ryder. Chase burnunu otlara yaklaştırdı ve dikkatle kokladı. Tatlı elma kokusunu izledi ve elmaları otların arasında tek tek buldu. Sonra onları burnuyla Ryder'a doğru yuvarladı. Ryder elmaları sepete koydu ve güldü. "Teşekkürler, Chase, şimdi herkese birer elma var!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "burnuyla kokuyu izleyip elmaları buldu"
   - Cümle 0 (plan satırı): «sepet düştü ve elmalar uzun otların arasında kayboldu | burnuyla kokuyu izleyip elmaları buldu ve yuvarladı»
   - Açıklama: Plan kokuyu Chase'in izlediğini söylüyor ama gövdede elmaları kokudan bulan Ryder.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0017` birebir aynı, `@degisim: kumbara -> elma` (tutuyorsan), ardından `@onarim: 4b20af47ecef0f9c9eaea7f9fd5936099c50777d`, sonra gövde.

### Hikâye 5: tohum chase-0019 (deneme 4 -> 5)

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
@plan: bakmadan koştu ve papatya dolu kovaya çarptı | kuralı hatırlayıp özür diledi ve papatyaları topladı
@tohum: chase-0019
@degisim: yüklemek -> doldurmak
Dalgalar kumsala hafifçe vuruyordu. Chase kumsalda koşuyor, Marshall ise rengarenk kovasını papatyalarla dolduruyordu. Chase önüne bakmadı ve kovaya çarptı. Bütün papatyalar kuma döküldü. "Eyvah, papatyalar!" dedi Marshall üzgün bir sesle. Chase kuralı biliyordu: yere bir şey dökülünce hemen toplanırdı. "Özür dilerim, Marshall, kovanı görmedim," dedi Chase. Sonra papatyaları tek tek topladı ve kovayı yeniden doldurdu. "Sorun değil, Chase, teşekkür ederim," dedi Marshall. Marshall dolu kovasını mutlu mutlu taşıdı. Chase bundan sonra kumsalda koşarken hep önüne baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kuralı biliyordu"
   - Cümle 6: «Chase kuralı biliyordu: yere bir şey dökülünce hemen toplanırdı.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0019` birebir aynı, `@degisim: yüklemek -> doldurmak` (tutuyorsan), ardından `@onarim: 1d3b0cf5a90c2478b456d772d8facdb03061a7c4`, sonra gövde.

### Hikâye 6: tohum chase-0022 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0022
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'ayakkabı', fiil 'düzeltmek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: oyuncak ayakkabı karın içine battı ve kayboldu | burnuyla kokusunu alıp karı kazdı
@tohum: chase-0022
@degisim: saygılı -> yumuşak
Karlı dağda yumuşak kar yağıyordu. Chase karda kırmızı bir oyuncak ayakkabıyı havaya atıp yakalıyordu. Ama ayakkabı bir kez uzağa düştü ve karın içine battı. Chase oraya koştu ama ayakkabıyı göremedi. Her yer bembeyazdı. Sonra burnunu yere yaklaştırdı ve oyuncağın kokusunu aldı. Koku küçük bir kar yığınının içinden geliyordu. Chase patileriyle orayı hızlı hızlı kazdı. Kırmızı ayakkabı sonunda göründü. Ucu biraz ezilmişti ve Chase onu patisiyle düzeltti. Chase onu ağzına aldı ve sıkıca tuttu. Chase çok sevindi, çünkü kaybolan oyuncağını bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ucu biraz ezilmişti ve Chase onu patisiyle düzeltti"
   - Cümle 10: «Ucu biraz ezilmişti ve Chase onu patisiyle düzeltti.»
   - Açıklama: Ezik uç ayrıntısı sonradan kuruluyor ve hiçbir işe yaramıyor.
   - Açıklama: Ezilen uç sebepsiz ekleniyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0022` birebir aynı, `@degisim: saygılı -> yumuşak` (tutuyorsan), ardından `@onarim: 6e23320ff896b82da33f04ff47ef1e7680978d8d`, sonra gövde.

### Hikâye 7: tohum chase-0026 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0026
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: bir şey yapmak
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'sandviç', fiil 'akmak', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: kardan köpeğin gözleri eksikti ama taşlar yolun dışındaydı | iki siyah zeytini göz olarak koydu
@tohum: chase-0026
Chase karlı dağda, yolun kenarında kardan bir köpek yapıyordu. Köpeğin başı ve kulakları hazırdı. Ama gözleri eksikti, çünkü yolda hiç koyu taş yoktu. Koyu taşlar yolun dışında, akan küçük bir suyun yanındaydı. Kurala göre dağda yoldan çıkmak yasaktı, çünkü kar derindi. Chase biraz düşündü ve çantasını açtı. Çantada öğle yemeği için bir sandviç vardı. Sandviçin arasında siyah zeytinler görünüyordu. Chase iki zeytini aldı ve onları köpeğin yüzüne koydu. Artık köpeğin iki parlak gözü vardı. Chase sandviçinin kalanını onun yanında mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala göre dağda yoldan çıkmak yasaktı"
   - Cümle 5: «Kurala göre dağda yoldan çıkmak yasaktı, çünkü kar derindi.»
   - Açıklama: 'Kurala göre' soyut bir kavram; 3 yaşındaki çocuk için somut değil.
   - Açıklama: 'Kural' ve 'yasak' soyut kavramlar, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0026` birebir aynı, ardından `@onarim: df4da0cced02db8e8508b51678540c7a3b269cf7`, sonra gövde.

### Hikâye 8: tohum chase-0028 (deneme 3 -> 4)

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
Rüzgar esiyordu ve yerdeki çıtır yapraklar uçuşuyordu. Chase parktaki kum havuzunda bir kum kulesi yapmak istedi. Ama oradaki kovanın dibi delikti ve kum hemen dökülüyordu. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı kumla doldurdu ve patileriyle iyice bastırdı. Sonra şapkayı ters çevirdi ve yavaşça yukarı çekti. Kumdan küçük bir kule çıktı ve dimdik durdu. Chase şapkayı silkeledi ve yine başına taktı. Sonra kulenin yanına iki kule daha yaptı. Chase kum oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yerdeki çıtır yapraklar uçuşuyordu"
   - Cümle 1: «Rüzgar esiyordu ve yerdeki çıtır yapraklar uçuşuyordu.»
   - Açıklama: 'Çıtır' yiyecek için kullanılır, yapraklar için 'kuru' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0028` birebir aynı, `@degisim: dondurma -> yaprak` (tutuyorsan), ardından `@onarim: e332a1456596b884690461de67d2dd6f33467927`, sonra gövde.

### Hikâye 9: tohum chase-0031 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0031
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'askı', fiil 'yarışmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kabukları ağzıyla taşıyamadı | şapkasını çıkarıp kabukları içine koydu
@tohum: chase-0031
@degisim: askı -> kabuk
Kumsalda Chase iskeleye kadar koşup yarış oyunu oynuyordu. Birden kumda karışık renkli, küçük kabuklar gördü. Hepsini toplamak istedi ama ağzına yalnız bir kabuk sığıyordu. Chase kabuklara baktı ve biraz düşündü. Sonra mavi şapkasını çıkardı ve ters çevirip kuma koydu. Kabukları tek tek şapkasının içine yerleştirdi. Pembe, beyaz ve sarı kabuklar şapkayı doldurdu. Chase şapkanın ucunu ağzıyla tuttu ve onu dikkatle kaldırdı. Hiçbir kabuk kuma düşmedi. Chase çok sevindi, çünkü bütün kabukları toplamıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "iskeleye kadar koşup yarış oyunu oynuyordu"
   - Cümle 1: «Kumsalda Chase iskeleye kadar koşup yarış oyunu oynuyordu.»
   - Açıklama: İskele ve yarış oyunu kuruluyor ama hikayede hiç kullanılmıyor, işlevsiz ayrıntı kalıyor.
   - Açıklama: Yarış oyunu kuruluyor ama hikayede bir daha geçmiyor ve hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0031` birebir aynı, `@degisim: askı -> kabuk` (tutuyorsan), ardından `@onarim: 5575d76334b275440a83baa49815576355d09f74`, sonra gövde.

### Hikâye 10: tohum chase-0033 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0033
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kaktüs', fiil 'sallamak', sıfat 'güneşli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: çocuğun kızağı kırılmıştı ve tek kızak vardı | kızağını çocukla paylaştı ve birlikte kaydılar
@tohum: chase-0033
@degisim: kaktüs -> kızak
Bir sabah karlı dağ çok güneşliydi. Chase ile Ryder kaymak için küçük bir tepeye çıktı. Ama yalnız Chase'in kızağı vardı, çünkü Ryder'ın kızağı kırılmıştı. Ryder üzgün üzgün Chase'e baktı. "Ryder, gel, bu kızak ikimizin!" dedi Chase. "İkimiz sığar mıyız?" diye sordu Ryder. Chase kuyruğunu salladı ve öne oturdu. Ryder de arkasına oturdu. "Bir kural var, Ryder: kızağı iki elinle tut," dedi Chase. Ryder hemen öyle yaptı. Kızak karın üstünde yavaşça aşağı indi. Sonra ikisi aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bir kural var, Ryder"
   - Cümle 9: «"Bir kural var, Ryder: kızağı iki elinle tut," dedi Chase.»
   - Açıklama: 'Kural' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0033` birebir aynı, `@degisim: kaktüs -> kızak` (tutuyorsan), ardından `@onarim: cac141dc22f93f7d79cde3a5db9833eaac94f2d2`, sonra gövde.

### Hikâye 11: tohum chase-0034 (deneme 2 -> 3)

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
@plan: rüzgar esince kağıt hep havaya kalkıyordu | kağıdın köşelerine küçük taşlar koydu
@tohum: chase-0034
Ağaçlarda kuşlar ötüyordu. Chase parkta ilk kez mavi mürekkeple pati resmi yapmayı deniyordu. Ama rüzgar esince beyaz kağıt hep havaya kalkıyordu. Chase resmini bankın üstüne yapmayı düşündü, çünkü bank rüzgarda uçmazdı. Ama parkta banklara boya sürmek yasaktı ve Chase kurallara uyardı. Bunun yerine yerden küçük taşlar topladı. Taşları kağıdın dört köşesine koydu. Artık kağıt rüzgarda hiç kıpırdamadı. Chase patisini dikkatli bir şekilde mürekkebe batırdı. Sonra kağıda düz basmaya çalıştı. Kağıtta çok güzel bir pati izi çıktı. Chase çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase resmini bankın üstüne yapmayı düşündü"
   - Cümle 4: «Chase resmini bankın üstüne yapmayı düşündü, çünkü bank rüzgarda uçmazdı.»
   - Açıklama: Bankın üstüne resim yapma fikri olaydan çıkmıyor ve hiçbir işe yaramadan bırakılan işlevsiz bir ara adım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 5: «Ama parkta banklara boya sürmek yasaktı ve Chase kurallara uyardı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0034` birebir aynı, ardından `@onarim: 4aca1a1355e9266c27e8563868ddaf144eb19dd3`, sonra gövde.

### Hikâye 12: tohum chase-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kamyon ağacın altındaydı ve boya ıslak kaldı | kamyonu güneşe itti ve kurumasını bekledi
@tohum: chase-0035
@degisim: pürüzsüz -> ıslak
Bir sabah Chase parkta kağıttan bir kravat yaptı. Kravatı oyuncak kamyonuna bindirdi ve maviye boyadı. Chase kravatla kaydıraktan kaymak istiyordu, ama boya ıslaktı. Kamyon ağacın altında duruyordu ve oraya güneş gelmiyordu. Chase kurallara uyardı ve ıslak boyaya dokunmadı. Kamyonu burnuyla yavaşça güneşe itti. Sonra kamyonun yanına oturdu ve bekledi. Güneş kravatı ısıttı ve boya kısa sürede kurudu. Chase patisiyle kravatın ucuna hafifçe dokundu. Boya artık patisine yapışmadı. Chase kravatı boynuna taktı ve kaydırağa koştu. Mavi kravatıyla kaydıraktan kaydı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kravatı oyuncak kamyonuna bindirdi"
   - Cümle 2: «Kravatı oyuncak kamyonuna bindirdi ve maviye boyadı.»
   - Açıklama: Kravat binen bir canlı değildir; 'bindirdi' yerine 'koydu' olmalı.
   - Açıklama: 'Bindirmek' yolcu için kullanılır; kravat için 'koydu' ya da 'yükledi' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kravatı oyuncak kamyonuna bindirdi"
   - Cümle 2: «Kravatı oyuncak kamyonuna bindirdi ve maviye boyadı.»
   - Açıklama: Kağıt kravatı boyamak için oyuncak kamyona bindirmek sebepsiz; kamyon yalnız itilebilsin diye kuruluyor.
   - Açıklama: Kağıt kravatın sebepsizce oyuncak kamyona bindirilmesi yapay bir kurgu; kamyon yalnız sorunu kurmak için beliriyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Chase kravatı boynuna taktı ve kaydırağa koştu"
   - Cümle 11: «Chase kravatı boynuna taktı ve kaydırağa koştu.»
   - Açıklama: Boyna bağlı bir şeyle kaydıraktan kaymak çocuğun taklit edebileceği boğulma tehlikesi taşıyan bir davranış.
   - Açıklama: Boyna bağlı bir kravatla kaydıraktan kaymak çocuğun taklit edebileceği bir boğulma/takılma tehlikesidir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0035` birebir aynı, `@degisim: pürüzsüz -> ıslak` (tutuyorsan), ardından `@onarim: 45a66d1f0d5eaf3603136fc2cadf5f40d683661e`, sonra gövde.
