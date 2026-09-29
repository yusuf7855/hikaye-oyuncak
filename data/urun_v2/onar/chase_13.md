# Editör görevi (onarım): Chase, onarım partisi 13

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar13.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar13.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0045 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0045
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kolye', fiil 'şakımak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: rüzgar resmi çadırın üstüne attı | yetişemedi ve şapkasıyla arkadaşını çağırdı
@tohum: chase-0045
@degisim: kolye -> çadır
Bir sabah kamp yerinde kuşlar şakıyordu. Chase çadırın önünde kremalı bir kek yiyor ve resmine bakıyordu. Birden rüzgar esti ve resim çadırın üstüne uçtu. Chase zıpladı ama oraya yetişemedi. Marshall uzakta, bir ağacın altında oturuyordu. Chase mavi şapkasını çıkardı ve havada salladı. Marshall onu gördü ve hemen koşarak geldi. Chase patisiyle çadırın üstünü gösterdi. Marshall çadırın ipini hafifçe salladı. Çadır sallandı ve resim kayıp aşağı düştü. Chase resmi yerden aldı. Sonra ikisi yan yana oturdu. Chase kekinin yarısını Marshall'a verdi. Chase çok mutlu oldu, çünkü resmini geri almıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kamp yerinde kuşlar şakıyordu"
   - Cümle 1: «Bir sabah kamp yerinde kuşlar şakıyordu.»
   - Açıklama: 'Şakımak' 3 yaşındaki bir çocuğun bilmeyeceği edebi bir kelime.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Marshall çadırın ipini hafifçe salladı"
   - Cümle 9: «Marshall çadırın ipini hafifçe salladı.»
   - Açıklama: Resmi indiren asıl eylemi Chase değil yan karakter Marshall yapıyor.
   - Açıklama: Resmi indiren asıl eylemi Chase değil Marshall yapıyor; Chase yalnız gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0045` birebir aynı, `@degisim: kolye -> çadır` (tutuyorsan), ardından `@onarim: 318dda6ba368b2043973d28318da61b82e662ce9`, sonra gövde.

### Hikâye 2: tohum chase-0048 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0048
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'gümüş', fiil 'boyamak', sıfat 'somurtkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: rüzgar uçurtmayı yüksek bir dala taktı | ağaca tırmanmadı ve arkadaşından yardım istedi
@tohum: chase-0048
@degisim: somurtkan -> üzgün
Parkta güçlü bir rüzgar esiyordu. Chase gümüş rengine boyadığı uçurtmasını uçuruyordu. Birden rüzgar uçurtmayı yüksek bir ağacın dalına taktı. Chase üzgün bir yüzle dala baktı. Kurala göre ağaca tırmanmak yasaktı. Skye da parktaydı ve Chase ona koştu. "Skye, uçurtmam ağaca takıldı, bana yardım eder misin?" diye sordu Chase. "Tabii, hemen gelirim," dedi Skye. Skye helikopteriyle ağacın üstüne uçtu. Uçurtmanın ipini dikkatle çekti ve daldan kurtardı. Uçurtma yavaşça Chase'in önüne indi. Chase çok sevindi, çünkü uçurtmasını geri almıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala göre ağaca tırmanmak yasaktı"
   - Cümle 5: «Kurala göre ağaca tırmanmak yasaktı.»
   - Açıklama: 'Kurala göre' soyut ve belirsiz; hangi kural olduğu somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0048` birebir aynı, `@degisim: somurtkan -> üzgün` (tutuyorsan), ardından `@onarim: a650cb76fd8436eca700ba2da87058c997ffb3c5`, sonra gövde.

### Hikâye 3: tohum chase-0050 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0050
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'keman', fiil 'silmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: kamp yerinde kimin olduğu bilinmeyen bir kutu vardı | kutuyu kokladı ve kokunun sahibini buldu
@tohum: chase-0050
@degisim: güvenli -> temiz
Chase kamp yerinde bir kütüğün yanında siyah bir kutu gördü. Kutu çamurluydu ve kimin olduğu belli değildi. Chase bu kutuyu çok merak etti. Burnunu yaklaştırdı ve kokladı. Bu, Ryder'ın kokusuydu! "Ryder, bu kutu senin mi?" diye seslendi Chase. Ryder koşarak geldi. "Evet, bu benim, burada unutmuşum!" dedi Ryder. Ryder çamuru bir bezle sildi ve kutuyu açtı. İçindeki oyuncak keman temiz kalmıştı. Ryder kemanı Chase'e gösterdi ve güldü. Sonra Chase ile Ryder kemanla mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kimin olduğu belli değildi"
   - Cümle 2: «Kutu çamurluydu ve kimin olduğu belli değildi.»
   - Açıklama: Sahibi belli olmayan bir kutu Chase için gerçek bir sorun değil; önemsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0050` birebir aynı, `@degisim: güvenli -> temiz` (tutuyorsan), ardından `@onarim: 060cce24d1604744fdea1c32086edc27beb77898`, sonra gövde.

### Hikâye 4: tohum chase-0051 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0051
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kumaş', fiil 'kaydetmek', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: bazı kabukların içinde minik canlılar vardı | canlıları bırakıp yalnız boş kabukları topladı
@tohum: chase-0051
@degisim: kaydetmek -> yaymak
Kumsalda dalgalar yavaş yavaş geliyordu. Chase kumaş örtüsünü yaydı ve hemen yanında renkli kabuklar gördü. Onları toplamak istedi ama bazı kabukların içinde minik canlılar vardı. Kurala göre kumsaldan canlı bir şey almak yasaktı. Chase her kabuğun içine dikkatle baktı. İçinde canlı olanları suyun kenarına yavaşça geri bıraktı. Boş kabukları ıslak, yapışkan kumdan tek tek çıkardı. Sonra kabuklarla örtünün üstünde büyük bir yıldız yaptı. Chase yıldızına bakıp mutlu mutlu kuyruğunu salladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurala göre kumsaldan canlı"
   - Cümle 4: «Kurala göre kumsaldan canlı bir şey almak yasaktı.»
   - Açıklama: 'Kurala göre' ve 'yasak' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0051` birebir aynı, `@degisim: kaydetmek -> yaymak` (tutuyorsan), ardından `@onarim: 8b892fe00b8caac9b1bb7c95b40b60a20edc7e36`, sonra gövde.

### Hikâye 5: tohum chase-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0053
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'zincir', fiil 'kucaklamak', sıfat 'sabırlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: rüzgar esti ve kardan köpeğin havuç burnu karda kayboldu | karı kokladı ve havucu bulup yerine taktı
@tohum: chase-0053
Karlı dağda hava güneşliydi. Chase, Skye için kardan bir köpek yapmış, boynuna kağıttan bir zincir takmıştı. Ama rüzgar esti ve kardan köpeğin havuç burnu karın içine düştü. Skye biraz ileride gözlerini kapatmış, sabırlı bir şekilde bekliyordu. Chase burnunu karın üstüne eğdi ve dikkatle kokladı. Havucu küçük bir çukurun içinde buldu. Onu çıkardı ve eski yerine taktı. "Şimdi gözlerini açabilirsin," dedi Chase. Skye gözlerini açtı ve kardan köpeği gördü. "Bu benim için mi?" diye sordu Skye. Sonra koştu ve Chase'i sıkıca kucakladı. Chase çok sevindi, çünkü Skye sürprizi çok beğenmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "boynuna kağıttan bir zincir takmıştı"
   - Cümle 2: «Chase, Skye için kardan bir köpek yapmış, boynuna kağıttan bir zincir takmıştı.»
   - Açıklama: Kağıttan zincir kurulup hikayede hiçbir işe yaramıyor.
   - Açıklama: Kağıttan zincir işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0053` birebir aynı, ardından `@onarim: 1fe3b3b3c2395908b8321fc12a1337d3683997db`, sonra gövde.

### Hikâye 6: tohum chase-0054 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Rubble
@tohum: chase-0054
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'fıstık', fiil 'rahatlatmak', sıfat 'ince'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | Rubble
@plan: arkadaşının kağıt torbası yırtıldı ve fıstıklar kuma döküldü | şapkasını ters çevirip fıstıkları içine topladı
@tohum: chase-0054
Chase, Rubble ile kumsalda iskeleye doğru yürüyordu. Rubble ince bir kağıt torbada fıstık taşıyordu. Birden torba yırtıldı ve bütün fıstıklar kuma döküldü. Rubble üzgün üzgün baktı, çünkü fıstıkları koyacak bir kabı yoktu. Chase biraz düşündü ve mavi şapkasını başından çıkardı. Şapkayı ters çevirip kumun üstüne koydu. İki arkadaş fıstıkları tek tek topladı ve şapkanın içine doldurdu. Sonunda kumda tek bir fıstık bile kalmadı. Bu yardım Rubble'ı çok rahatlattı. Rubble kuyruğunu salladı ve Chase'in yanağını yaladı. Chase de çok mutluydu, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu yardım Rubble'ı çok rahatlattı"
   - Cümle 9: «Bu yardım Rubble'ı çok rahatlattı.»
   - Açıklama: Soyut 'yardım' öznesi ve 'rahatlatmak' fiili küçük çocuk için soyut.
   - Açıklama: 'Yardım rahatlattı' soyut bir anlatım; çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0054` birebir aynı, ardından `@onarim: bd2ddc558c70e653b2a0908bd60e845cee637aac`, sonra gövde.

### Hikâye 7: tohum chase-0056 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kumsaldan garip bir ses geliyordu ama güneş çok parlaktı | şapkasını gözlerine indirdi ve dönen fırıldağı gördü
@tohum: chase-0056
@degisim: yakalamak -> dönmek
Kumsalda hafif bir rüzgar esiyordu. Chase iskelenin yanında yürürken garip bir ses duydu. Ses kumsalın ortasından geliyordu. Ama güneş çok parlaktı ve Chase bir şey göremedi. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi her yeri rahatça gördü. Kumda renkli bir oyuncak fırıldak duruyordu. Fırıldak rüzgarda hızlı hızlı dönüyordu. Garip ses bu küçük aletten geliyordu. Chase yanına gitti ve onu dikkatle dinledi. Rüzgar durunca fırıldak da durdu ve ses kesildi. Chase çok mutlu oldu, çünkü sesi yapan şeyi bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama güneş çok parlaktı ve Chase bir şey göremedi"
   - Cümle 4: «Ama güneş çok parlaktı ve Chase bir şey göremedi.»
   - Açıklama: Garip sesin kaynağını görememek zayıf bir sorun; ortada çocuğun önemseyeceği bir kayıp ya da ihtiyaç yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0056` birebir aynı, `@degisim: yakalamak -> dönmek` (tutuyorsan), ardından `@onarim: 9835afc4a2d1ba34c9a9b9bbbd2138b7d9cd3c2c`, sonra gövde.

### Hikâye 8: tohum chase-0058 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Ryder
@tohum: chase-0058
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'çörek', fiil 'düzenlemek', sıfat 'yakın'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | ev | Ryder
@plan: rüzgar çörek torbasını masadan düşürüp sürükledi | havayı koklayıp torbayı en yakın kulübenin arkasında buldu
@tohum: chase-0058
Rüzgar kulübelerin arasında hızlı hızlı esiyordu. Chase, kulede çalışan Ryder için bir sürpriz hazırlıyordu. Ama rüzgar masadaki çörek torbasını yere düşürdü ve sürükledi. Chase torbayı hiçbir yerde göremedi. Burnunu havaya kaldırdı ve kokladı. Sonra en yakın kulübenin arkasına koştu. Torba orada, çimlerin üstünde duruyordu. Chase torbayı masaya geri getirdi. Çörekleri masanın üstünde yan yana düzenledi. "Ryder, şimdi gelebilirsin!" diye seslendi Chase. Ryder aşağı indi ve çörekleri gördü. "Teşekkürler, Chase, bu çok güzel bir sürpriz!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Rüzgar kulübelerin arasında hızlı hızlı esiyordu"
   - Cümle 1: «Rüzgar kulübelerin arasında hızlı hızlı esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye dışarıda kulübeler, kule ve çimler arasında geçiyor.
   - Açıklama: Başlıktaki yer ev olduğu halde hikaye kulübelerin arasında ve kulenin yanında geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0058` birebir aynı, ardından `@onarim: 409217dd5134048218047269bffc27892aa5d2e1`, sonra gövde.

### Hikâye 9: tohum chase-0059 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0059
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bezelye', fiil 'ıslanmak', sıfat 'çiçekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: çimenlere su geldi ve şapka suyla doldu | suyu döktü ve şapkayı kuru bir yere taşıdı
@tohum: chase-0059
@degisim: bezelye -> top
Bir sabah Chase parkta komik bir oyun oynuyordu. Mavi şapkasını ters çevirip çiçekli çimenin yanına koymuş, içine top atıyordu. Ama yakındaki fıskiye birden açıldı ve şapka ıslanmaya başladı. Şapkanın içi kısa sürede suyla doldu. Chase topu attı ve top suya düştü. Su sıçradı ve Chase'in burnunu ıslattı. Buna çok güldü. Sonra şapkayı aldı ve içindeki suyu döktü. Onu sudan uzak, kuru bir yere taşıdı. Oraya hiç su gelmiyordu. Chase topu yeniden attı ve top tam şapkanın içine düştü. Chase sevinçle zıpladı. Chase bundan sonra oyunlarını sudan uzakta kurdu.
```

**Hakem bulguları (6):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "çiçekli çimenin yanına koymuş"
   - Cümle 2: «Mavi şapkasını ters çevirip çiçekli çimenin yanına koymuş, içine top atıyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -miş'li geçmişe kayıyor; 'koymuştu' olmalı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "yanına koymuş, içine top"
   - Cümle 2: «Mavi şapkasını ters çevirip çiçekli çimenin yanına koymuş, içine top atıyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şapkanın içi kısa sürede suyla doldu"
   - Cümle 4: «Şapkanın içi kısa sürede suyla doldu.»
   - Açıklama: Sorun önemsiz bir oyun aksaklığı; su dökülüp şapka taşınınca bitiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Su sıçradı ve Chase'in burnunu ıslattı"
   - Cümle 6: «Su sıçradı ve Chase'in burnunu ıslattı.»
   - Açıklama: Topun suya düşüp burnu ıslatması olayı ilerletmeyen işlevsiz bir ara sahne.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu sudan uzak, kuru"
   - Cümle 9: «Onu sudan uzak, kuru bir yere taşıdı.»
   - Açıklama: 'Onu' zamiri en yakın ad olan suyu da gösterebiliyor; şapka mı su mu belli değil.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oyunlarını sudan uzakta kurdu"
   - Cümle 13: «Chase bundan sonra oyunlarını sudan uzakta kurdu.»
   - Açıklama: 'Oyun kurmak' deyimsel bir kullanım, küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0059` birebir aynı, `@degisim: bezelye -> top` (tutuyorsan), ardından `@onarim: c2101691e3c6123dc98b9d732532fa3036ea2f11`, sonra gövde.

### Hikâye 10: tohum chase-0062 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0062
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'takvim', fiil 'vedalaşmak', sıfat 'kısa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: güneş çok parlaktı ve uçan kuşlar görünmedi | mavi şapkasını arkadaşının başına taktı
@tohum: chase-0062
@degisim: takvim -> güneş
Chase, Skye ile kulenin önünde oturuyordu. Gökyüzünde kuşlar uzaklara doğru uçuyordu. Skye kuşlarla vedalaşmak istedi ama güneş çok parlaktı ve kuşları göremedi. "Kuşlar nerede, Chase? Hiçbirini göremiyorum," dedi Skye. Chase mavi şapkasını çıkardı ve arkadaşının başına taktı. Şapka onun gözlerini güneşten korudu. Skye şimdi kuşları rahatça gördü. Kuşlar kısa bir süre kulenin üstünde döndü. "Güle güle, kuşlar!" dedi Skye ve patisini salladı. Chase de sevinçle havladı. Sonra kuşlar yavaş yavaş uzaklaştı. Skye çok sevindi, çünkü kuşlar gitmeden onları görebilmişti.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Skye ile kulenin önünde oturuyordu"
   - Cümle 1: «Chase, Skye ile kulenin önünde oturuyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye kulenin önünde, dışarıda geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Skye kuşlarla vedalaşmak istedi"
   - Cümle 3: «Skye kuşlarla vedalaşmak istedi ama güneş çok parlaktı ve kuşları göremedi.»
   - Açıklama: 'Vedalaşmak' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime; 'güle güle demek' daha uygun olurdu.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Skye kuşlarla vedalaşmak istedi"
   - Cümle 3: «Skye kuşlarla vedalaşmak istedi ama güneş çok parlaktı ve kuşları göremedi.»
   - Açıklama: Çoğul canlı kuşlar arka planda kalmıyor; hikayenin olayı onlarla vedalaşmak ve kulenin üstünde dönmeleri üzerine kurulu.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Kuşlar kısa bir süre kulenin üstünde döndü"
   - Cümle 9: «Kuşlar kısa bir süre kulenin üstünde döndü.»
   - Açıklama: Notlanan çoğul canlı kuşlar arka planda kalmıyor, Skye'nin vedasına karşılık verir gibi olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0062` birebir aynı, `@degisim: takvim -> güneş` (tutuyorsan), ardından `@onarim: 1aca2e521384f6fbe911b599c349acd965f49261`, sonra gövde.

### Hikâye 11: tohum chase-0064 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0064
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'şemsiye', fiil 'yetiştirmek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: yağmur geliyordu ve ince sapı olan çiçek kırılabilirdi | şemsiyesini açıp çiçeğin yanına dikti
@tohum: chase-0064
Bir sabah Chase kulübesinin önünde küçük bir çiçek yetiştiriyordu. Birden havayı kokladı ve yağmurun yaklaştığını anladı. Çiçeğin sapı çok inceydi ve sert damlalar onu kırabilirdi. Chase hemen içeri koştu ve sarı şemsiyesini getirdi. Şemsiyeyi açtı ve çiçeğin yanında toprağa dikti. Şemsiye çiçeği tamamen kapattı. Biraz sonra yağmur başladı. Damlalar şemsiyenin üstünde tık tık ses çıkardı. Chase kapının önünde sessiz sessiz bekledi. Yağmur dinince şemsiyeyi kaldırdı. Çiçek hiç kırılmamıştı ve dimdik duruyordu. Chase bundan sonra yağmurlu günlerde şemsiyesini hep çiçeğinin yanında tuttu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "şemsiyesini açıp çiçeğin yanına dikti"
   - Cümle 0 (plan satırı): «yağmur geliyordu ve ince sapı olan çiçek kırılabilirdi | şemsiyesini açıp çiçeğin yanına dikti»
   - Açıklama: Tohumdaki özellik 'burnuyla koku alarak çözüm bulur' iken sorunu koku değil kartta olmayan şemsiye çözüyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "havayı kokladı ve yağmurun"
   - Cümle 2: «Birden havayı kokladı ve yağmurun yaklaştığını anladı.»
   - Açıklama: Tohumdaki koku özelliği çözüme katkı vermiyor; sorunu şemsiye çözüyor, oysa kart özelliği burnuyla koku alarak çözüm bulmaktır.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ve sarı şemsiyesini getirdi"
   - Cümle 4: «Chase hemen içeri koştu ve sarı şemsiyesini getirdi.»
   - Açıklama: Kartta Chase'in şemsiyesi gibi bir eşyası yok; kapalı dünya kuralına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0064` birebir aynı, ardından `@onarim: 20b12287d51b8da88012619bf2da86ea10872405`, sonra gövde.
