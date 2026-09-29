# Editör görevi (onarım): Chase, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0070 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0070
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'televizyon', fiil 'sevinmek', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: top kuyruğa çarptı ve bankın altına yuvarlandı | şapkasının ucuyla topu kendine çekti
@tohum: chase-0070
@degisim: televizyon -> top
Parkta Chase simsiyah bir topla oynuyordu. Topu burnuyla havaya atıyor, sonra kuyruğuyla tutmaya çalışıyordu. Ama top bir kez kuyruğuna çarptı ve bankın altına yuvarlandı. Chase patisini uzattı, ama top çok uzaktaydı. Bankın altı dardı ve Chase oraya giremedi. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkanın ucuyla topa dokundu ve onu yavaşça kendine çekti. Top bankın altından çıktı. Chase şapkasını başına taktı. Sonra topu burnuyla havaya attı ve bu sefer ağzıyla yakaladı. Chase çok sevindi, çünkü komik oyununu yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapkanın ucuyla topa dokundu"
   - Cümle 7: «Şapkanın ucuyla topa dokundu ve onu yavaşça kendine çekti.»
   - Açıklama: Kartın özellik alanı şapkayı takılan bir eşya olarak veriyor; burada şapka çıkarılıp topu çekmek için kanca gibi kullanılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çünkü komik oyununu yine oynayabiliyordu"
   - Cümle 11: «Chase çok sevindi, çünkü komik oyununu yine oynayabiliyordu.»
   - Açıklama: Oyun daha önce komik diye anlatılmadı; 'komik' kelimesi yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0070` birebir aynı, `@degisim: televizyon -> top` (tutuyorsan), ardından `@onarim: 08384cd56f09dfa743f2f3abbf57f13070c8924c`, sonra gövde.

### Hikâye 2: tohum chase-0071 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0071
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'mermer', fiil 'sıkılmak', sıfat 'özel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: koşarken kardan köpeğe çarptı ve köpeğin başı düştü | özür diledi ve kardan başı yerine koydu
@tohum: chase-0071
@degisim: mermer -> kar
Bir sabah Rubble karlı dağda kardan özel bir köpek yapıyordu. Chase onu bekliyordu, ama çok sıkıldı ve karda koşmaya başladı. Koşarken kardan köpeğe çarptı. Kardan köpeğin başı yere yuvarlandı. Rubble yerdeki başa baktı ve üzüldü. Chase bir kural biliyordu: hata yapan özür diler. "Özür dilerim, Rubble, beklerken sıkıldım ve koştum," dedi Chase. Sonra yuvarlanan başı itip geri getirdi. İkisi birlikte başı yerine koydu. Chase başın üstüne iki küçük kulak da yaptı. "Teşekkürler, Chase, köpeğimiz şimdi daha da güzel!" dedi Rubble.
```

**Hakem bulguları (3):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hata yapan özür diler"
   - Cümle 6: «Chase bir kural biliyordu: hata yapan özür diler.»
   - Açıklama: Anlatım cümlesinde geniş zamana kayılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bir kural biliyordu: hata yapan özür diler."
   - Cümle 6: «Chase bir kural biliyordu: hata yapan özür diler.»
   - Açıklama: 'Kural' ve 'hata' soyut kavramlar ve cümle olaydan çıkan somut bir ders değil, genel bir öğüt.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hata yapan özür diler"
   - Cümle 6: «Chase bir kural biliyordu: hata yapan özür diler.»
   - Açıklama: Genel kural cümlesi ve 'hata' soyut kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0071` birebir aynı, `@degisim: mermer -> kar` (tutuyorsan), ardından `@onarim: dc157976c8308cbcbe3665421bfb02f844eea859`, sonra gövde.

### Hikâye 3: tohum chase-0072 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0072
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'plak', fiil 'şaşırtmak', sıfat 'neşeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: rüzgar topu götürdü ve iskelenin altından bir ses geldi | kokladı ve sesin topundan geldiğini buldu
@tohum: chase-0072
@degisim: plak -> top
Kumsalda sert bir rüzgar esiyordu. Rüzgar Chase'in kırmızı topunu uzağa yuvarladı. Chase topunu aradı ama hiçbir yerde bulamadı. Birden iskelenin altından tok tok diye bir ses geldi. Bu ses Chase'i çok şaşırttı. Orası gölgeydi ve hiçbir şey görünmüyordu. Chase burnunu yere yaklaştırdı ve derin derin kokladı. Gölgede kendi topunun kokusunu hemen tanıdı. Top, iskelenin direğine hafif hafif çarpıyordu. Tok tok sesi buradan geliyordu. Chase topu patisiyle yavaşça dışarı çekti. Sonra neşeli neşeli havladı. Chase çok sevindi, çünkü kaybolan topunu bulmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra neşeli neşeli havladı"
   - Cümle 12: «Sonra neşeli neşeli havladı.»
   - Açıklama: Derin derin, hafif hafif, neşeli neşeli gibi ikilemeler gereksiz yere üst üste kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0072` birebir aynı, `@degisim: plak -> top` (tutuyorsan), ardından `@onarim: 7402987539025748bf57f91cc022891d95d46085`, sonra gövde.

### Hikâye 4: tohum chase-0073 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar şapkayı gözlerinin önüne düşürdü | şapkasını yukarı itti ve sıkıca taktı
@tohum: chase-0073
Rüzgar hafif hafif esiyordu. Chase ile Ryder parkta halat çekme oyunu oynuyordu. Ama birden rüzgar Chase'in mavi şapkasını gözlerinin önüne düşürdü. Chase hiçbir şey göremedi ve halatı farklı bir yöne çekti. "Chase, ben bu taraftayım!" dedi Ryder gülerek. Chase durdu ve patisiyle şapkasını yukarı itti. Sonra onu başına sıkıca taktı. Artık Ryder'ı çok iyi görüyordu. "Hazırım, Ryder, hadi yine çekelim!" dedi Chase. "Gel bakalım, Chase!" dedi Ryder. Chase halatı ağzıyla tuttu ve geriye doğru çekti. İkisi halat çekmeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar Chase'in mavi şapkasını gözlerinin önüne düşürdü"
   - Cümle 3: «Ama birden rüzgar Chase'in mavi şapkasını gözlerinin önüne düşürdü.»
   - Açıklama: Şapkanın göze düşmesi bir itişle hemen biten önemsiz bir olay; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0073` birebir aynı, ardından `@onarim: 8ddff876aa2073138f99d645ccf3d64ea994e282`, sonra gövde.

### Hikâye 5: tohum chase-0074 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0074
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bant', fiil 'sektirmek', sıfat 'sert'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: güneş karda parladı ve topu göremedi | mavi şapkasını arkadaşına verdi
@tohum: chase-0074
@degisim: bant -> top
Chase ile Skye karlı dağda top oynuyordu. Chase topu sert karın üstünde sektirdi ve arkadaşına attı. Ama güneş karda çok parlıyordu ve Skye topu göremedi. Top onun yanından geçti ve kara düştü. "Güneş gözüme geliyor, Chase," dedi Skye. Chase biraz düşündü ve mavi şapkasını çıkardı. "Bunu tak, Skye, güneş gözüne gelmez," dedi Chase. Skye şapkayı taktı ve gülümsedi. Chase topu yeniden attı. Skye bu sefer topu kolayca yakaladı. "Şimdi her şeyi görüyorum!" dedi Skye sevinçle. İki arkadaş top oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güneş karda parladı ve topu göremedi"
   - Cümle 0 (plan satırı): «güneş karda parladı ve topu göremedi | mavi şapkasını arkadaşına verdi»
   - Açıklama: Plan satırında 'göremedi' fiilinin öznesi yok; cümle güneşi özne yapıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Güneş gözüme geliyor, Chase"
   - Cümle 5: «"Güneş gözüme geliyor, Chase," dedi Skye.»
   - Açıklama: 'Güneş gözüme geliyor' kalıplaşmış deyimsel bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0074` birebir aynı, `@degisim: bant -> top` (tutuyorsan), ardından `@onarim: b87f87db36eeec80501fffd2b24f9bda3ac07f52`, sonra gövde.

### Hikâye 6: tohum chase-0075 (deneme 1 -> 2)

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
@plan: karlı dağda garip bir ses geldi | şapkasıyla uzağa baktı ve dala takılan bezi buldu
@tohum: chase-0075
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken garip bir ses duydu. Ses uzaktan geliyordu ve Chase onun ne olduğunu çok merak etti. Ama güneş karda parlıyordu ve Chase uzağı göremiyordu. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi uzaktaki çam ağacını iyi görüyordu. Ağacın alçak bir dalında gri bir şey dönüyordu. Chase ağaca doğru yavaşça yürüdü. Bu, rüzgarın dala taktığı gri bir bezdi. Rüzgar esince bez dalın etrafında dönüyor ve ses çıkarıyordu. Chase bezi dişleriyle çekip daldan aldı. Ses hemen durdu. Chase bundan sonra garip bir ses duyunca önce durup dikkatle baktı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkasıyla uzağa baktı"
   - Cümle 0 (plan satırı): «karlı dağda garip bir ses geldi | şapkasıyla uzağa baktı ve dala takılan bezi buldu»
   - Açıklama: Şapkayla bakılmaz; plan satırında fiil anlamca uymuyor.
   - Açıklama: Şapkayla bakılmaz; plan satırında araç yanlış kullanılmış.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Chase karda yürürken garip bir ses duydu"
   - Cümle 2: «Chase karda yürürken garip bir ses duydu.»
   - Açıklama: Karlı dağda yalnızken duyulan kaynağı belirsiz garip ses küçük çocuk için ürkütücü olabilir.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Chase uzağı göremiyordu"
   - Cümle 4: «Ama güneş karda parlıyordu ve Chase uzağı göremiyordu.»
   - Açıklama: Garip sesin merakına ikinci bir sorun olarak güneşin göz kamaştırması ekleniyor ve plan çözümü bu ikinci soruna yöneliyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama güneş karda parlıyordu ve Chase uzağı göremiyordu"
   - Cümle 4: «Ama güneş karda parlıyordu ve Chase uzağı göremiyordu.»
   - Açıklama: Garip ses sorununun yanına güneşten uzağı görememe diye ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0075` birebir aynı, ardından `@onarim: 5c96157de1b23f517595f53a80ebc27ddef7e901`, sonra gövde.

### Hikâye 7: tohum chase-0076 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0076
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pelerin', fiil 'uyandırmak', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: yavaş yürüdü ve pelerin hiç kalkmadı | kurallara uydu ve kumsalda rüzgara doğru koştu
@tohum: chase-0076
@degisim: uyandırmak -> uçurmak
Bir sabah Chase kumsalda kıpkırmızı bir pelerin taktı. Pelerini rüzgarda uçurmayı ilk kez deneyecekti. Ama Chase yavaş yürüdü ve pelerin hiç kalkmadı. Chase koşmak için düz bir yer aradı. Uzun iskele çok düzdü, ama orada koşmak yasaktı. Chase kurallara uyardı ve iskele yerine kumsalda koştu. Rüzgara doğru hızlı hızlı koştu. Pelerin arkasında havaya kalktı ve uçtu. Chase başını çevirip arkasına baktı ve sevinçle havladı. Sonra kumsalda mutlu mutlu koşmaya devam etti.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "kıpkırmızı bir pelerin taktı"
   - Cümle 1: «Bir sabah Chase kumsalda kıpkırmızı bir pelerin taktı.»
   - Açıklama: Kartın özellikler ve görünüş alanlarında Chase'in pelerini yok; o yalnız mavi şapka takar.
   - Açıklama: Kartta Chase'in pelerini yok; kartın görünüş ve özellikler alanı yalnız mavi şapka veriyor, kapalı dünyaya eşya ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Uzun iskele çok düzdü, ama orada koşmak yasaktı"
   - Cümle 5: «Uzun iskele çok düzdü, ama orada koşmak yasaktı.»
   - Açıklama: İskele kurulup hiç kullanılmıyor; Chase zaten bulunduğu kumsalda koşuyor, bu ayrıntı olaya işlev katmıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kurallara uyardı ve"
   - Cümle 6: «Chase kurallara uyardı ve iskele yerine kumsalda koştu.»
   - Açıklama: 'uyardı' hem 'ikaz etti' diye okunabiliyor hem de anlatıma geniş zaman kayması getiriyor; 'kurallara uydu' olmalı.
   - Açıklama: 'Uyardı' geniş zamanın hikayesi olarak 'uyarmak' fiiliyle karışıyor; 'uydu' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 6: «Chase kurallara uyardı ve iskele yerine kumsalda koştu.»
   - Açıklama: 'Uyardı' hem 'uyar-dı' hem 'uyar-ı-dı' olarak okunabiliyor ve geniş zamanlı geçmiş anlatımda belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0076` birebir aynı, `@degisim: uyandırmak -> uçurmak` (tutuyorsan), ardından `@onarim: ec052e98a0f0122ee5247ffd567552c2789acb0b`, sonra gövde.

### Hikâye 8: tohum chase-0077 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0077
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'yaprak', fiil 'ıslatmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: çiçeğin toprağı kuruydu ve kova çok ağırdı | şapkasına su doldurdu ve çiçeğe götürdü
@tohum: chase-0077
Ormandaki kamp yerinde güneş parlıyordu. Chase bahçe oyunu oynuyordu ve küçük bir çiçeğe bakıyordu. Ama çiçeğin toprağı kuruydu ve yaprakları aşağı eğilmişti. Ağacın dibinde soğuk suyla dolu bir kova vardı. Chase kovayı itti, ama kova çok ağırdı. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı kovaya daldırdı ve suyla doldurdu. Sonra şapkayı ağzıyla tuttu ve yavaş yavaş çiçeğe yürüdü. Su toprağı ve yaprakları ıslattı. Chase bunu üç kez daha yaptı. Sonunda çiçeğin toprağı iyice ıslandı. Chase çok sevindi, çünkü oyunundaki çiçeğe su vermişti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase bahçe oyunu oynuyordu"
   - Cümle 2: «Chase bahçe oyunu oynuyordu ve küçük bir çiçeğe bakıyordu.»
   - Açıklama: 'bahçe oyunu' belirsiz ve anlamı açık olmayan bir kullanım.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağacın dibinde soğuk suyla dolu bir kova vardı"
   - Cümle 4: «Ağacın dibinde soğuk suyla dolu bir kova vardı.»
   - Açıklama: Suyla dolu kova sebepsizce tam gerektiği anda beliriyor ve çözümü getiriyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase bunu üç kez daha yaptı"
   - Cümle 10: «Chase bunu üç kez daha yaptı.»
   - Açıklama: Çözüm şapkayla dört kez su taşımaya uzuyor ve iki adımı aşıyor.
   - Açıklama: Çözüm tekrarlarla dört sefere uzuyor, en çok iki adım sınırını aşıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oyunundaki çiçeğe su vermişti"
   - Cümle 12: «Chase çok sevindi, çünkü oyunundaki çiçeğe su vermişti.»
   - Açıklama: Gerçek çiçek 'oyunundaki çiçek' diye anılıyor; 'bahçe oyunu' ile birlikte anlam bulanık.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0077` birebir aynı, ardından `@onarim: 4bd01435d4d463957f44cbb160de9c1d77157033`, sonra gövde.

### Hikâye 9: tohum chase-0078 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0078
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'çarşaf', fiil 'süpürmek', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: rüzgar çarşafı kaldırdı ve bir elma kayboldu | burnuyla elmanın kokusunu alıp onu buldu
@tohum: chase-0078
@degisim: konuşkan -> kırmızı
Kumsalda serin bir rüzgar esiyordu. Ryder ile Chase büyük bir çarşafın üstünde oturuyordu. Birden rüzgar çarşafın ucunu kaldırdı ve iki kırmızı elma kuma yuvarlandı. Ryder bir elmayı hemen buldu, ama öbürü yoktu. Chase burnunu kuma yaklaştırdı ve elmanın kokusunu aldı. Sonra küçük bir kum tepesine doğru yürüdü. Elma tepenin arkasındaydı. Chase elmayı ağzıyla aldı ve Ryder'a getirdi. Çarşafın üstü de kum doluydu. Chase kuyruğuyla kumu süpürdü. "Teşekkürler, Chase, bir elma sana, bir elma bana," dedi Ryder. İkisi temiz çarşafta elmalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Çarşafın üstü de kum doluydu"
   - Cümle 9: «Çarşafın üstü de kum doluydu.»
   - Açıklama: Elma bulunduktan sonra çarşafın kumla dolması ikinci bir sorun olarak ekleniyor.
   - Açıklama: Kayıp elma sorunundan sonra kumlu çarşaf diye ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0078` birebir aynı, `@degisim: konuşkan -> kırmızı` (tutuyorsan), ardından `@onarim: e144dbe2cd5cede09264aef7309a0e498eab0588`, sonra gövde.

### Hikâye 10: tohum chase-0080 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0080
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'beşik', fiil 'yedirmek', sıfat 'plastik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: kardan pastanın üstü bomboştu ve süs yoktu | tanımadığı meyveye dokunmadı ve bisküvileri koydu
@tohum: chase-0080
@degisim: beşik -> pasta
Bir sabah Chase karlı dağda Rubble için kardan bir pasta yaptı. Bu, Rubble'a küçük bir sürprizdi. Ama pastanın üstü bomboştu ve hiç süsü yoktu. Chase çalının üstünde kırmızı meyveler gördü. Ama Chase kurallara uyardı ve tanımadığı meyveye dokunmadı. Sonra yanındaki plastik kutuyu açtı. Kutuda köpek bisküvileri vardı. Chase bisküvileri pastanın üstüne dizdi. Biraz sonra Rubble geldi. "Bu pasta benim için mi?" diye sordu Rubble. "Evet, Rubble, bisküviler de senin," dedi Chase. Chase bisküvileri tek tek Rubble'a yedirdi. Chase bundan sonra da tanımadığı meyvelere hiç dokunmadı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama pastanın üstü bomboştu ve hiç süsü yoktu"
   - Cümle 3: «Ama pastanın üstü bomboştu ve hiç süsü yoktu.»
   - Açıklama: Süssüz pastanın bir sebebi söylenmiyor ve sorun zayıf kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Chase kurallara uyardı"
   - Cümle 5: «Ama Chase kurallara uyardı ve tanımadığı meyveye dokunmadı.»
   - Açıklama: 'uyardı' 'uyarmak' fiiliyle karışıyor; 'kurallara uyardı' küçük çocuk için belirsiz, 'kurallara uyuyordu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 5: «Ama Chase kurallara uyardı ve tanımadığı meyveye dokunmadı.»
   - Açıklama: 'Kurallara uyardı' soyut ve 'uyarmak' fiiliyle karışabilen, 3 yaşındaki çocuğun anlamayacağı bir anlatım.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yanındaki plastik kutuyu açtı"
   - Cümle 6: «Sonra yanındaki plastik kutuyu açtı.»
   - Açıklama: Bisküvili kutu sebepsizce beliriyor ve çözümü hazır getiriyor.
   - Açıklama: Bisküvili kutu önceden kurulmadan çözümü sebepsizce getiriyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Chase bundan sonra da tanımadığı meyvelere hiç dokunmadı"
   - Cümle 13: «Chase bundan sonra da tanımadığı meyvelere hiç dokunmadı.»
   - Açıklama: Son cümle sürpriz pasta hedefine dönmüyor; olaydan çıkmayan vaaz gibi bir kuralla bitiyor.
   - Açıklama: Son cümle ana olaydan (pasta sürprizi) değil yan ayrıntıdan çıkan vaaz gibi bir ders veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0080` birebir aynı, `@degisim: beşik -> pasta` (tutuyorsan), ardından `@onarim: d43b1e629982e3a8a1c12df2fdb77694a2fa5056`, sonra gövde.

### Hikâye 11: tohum chase-0081 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: şapkadan garip bir tık sesi geldi | şapkasını çıkarıp baktı ve yağmur damlalarını gördü
@tohum: chase-0081
@degisim: tekerlekli -> garip
Kumsalda hava bulutluydu. Chase iskelenin yanında kabından mamasını yiyordu. Birden mavi şapkasından garip bir tık sesi geldi. Chase bu sesi çok merak etti. Chase başını sağa sola çevirdi, ama hiçbir şey görmedi. Tık sesleri yavaş yavaş çoğaldı. Chase şapkasını çıkardı ve dikkatle baktı. Şapkanın üstünde küçük su damlaları vardı. O anda burnuna da bir damla düştü. Sesi yapan, yağmurun ilk damlalarıydı! Chase şapkasını yine başına taktı ve mamasını bitirdi. Chase çok sevindi, çünkü o garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden mavi şapkasından garip bir tık sesi geldi"
   - Cümle 3: «Birden mavi şapkasından garip bir tık sesi geldi.»
   - Açıklama: Şapkadan gelen tık sesi çocuğun önemseyeceği gerçek bir sorun değil, ortada kaybedilecek ya da düzeltilecek bir şey yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0081` birebir aynı, `@degisim: tekerlekli -> garip` (tutuyorsan), ardından `@onarim: 0cd8be88ba70b2f4ae74a1ebc51bfe0a5cba2b9e`, sonra gövde.
