# Editör görevi (onarım): Pepee, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Pepee | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar35.txt --ad urun_v2`
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

## Kart: Pepee (kaynaklı, kapalı dünya)

- Ad: Pepee (okunuş: pepe; kesme eki okunuşa uyar)
- Kimlik: Pepee, mavi tulum ve mavi şapka giyen, dört yaşında meraklı bir oğlandır.
- Tür: oğlan
- Güvenli özellik kullanımı: Pepee yeni şeyleri bir büyüğün yanında dener; derin suya girmez, yüksek yere çıkmaz.
- Özellikler:
  - öğren: Yeni şeyler öğrenmeyi ve denemeyi sever. (örnek biçimler: öğrendi, öğrenmeyi)
  - kahvaltı: Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer. (örnek biçimler: kahvaltı, kahvaltıda)
  - dans: Oyun oynamayı ve dans etmeyi sever. (örnek biçimler: dans, dansı)
- Yerler:
  - orman: Ağaçlarla ve çiçeklerle dolu bir orman.
  - deniz: Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.
  - park: Salıncağı ve kaydırağı olan bir çocuk parkı.
  - ev: Pepee'nin ailesiyle yaşadığı ev.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Bebee: Pepee'nin küçük kız kardeşi; annesine hayrandır, Pepee ile oynamak için büyümek ister. Tür: kız; konuşur. Yüzey biçimleri: Bebee, kardeş, kardeşi
  - Şila: Pepee'nin kuzeni ve en yakın arkadaşı; çok güzel dans eder. Tür: kız; konuşur. Yüzey biçimleri: Şila, kuzen, kuzeni
  - Dedee: Pepee'nin dedesi; en az Pepee kadar hareketli bir oyun arkadaşı. Tür: dede; konuşur. Yüzey biçimleri: Dedee, dede, dedesi, dedeciğim
  - Nenee: Pepee'nin ninesi; komik ve eğlencelidir, yemek pişirmeyi sever. Tür: nine; konuşur. Yüzey biçimleri: Nenee, Ninee, nine, ninesi, nineciğim
  - Annee: Pepee'nin ve Bebee'nin annesi. Tür: anne; konuşur. Yüzey biçimleri: Annee, anne, annesi, anneciğim
- Dünya kuralları:
  - Bebee Pepee'nin küçük kız kardeşidir; Şila kuzenidir, kardeşi değildir.
  - Dizinin görünmeyen anlatıcısı hikayeye girmez; hikaye olayları kendisi anlatır.
- Yasak adlar: Şuşu, Şuşuu, Pisi, Zulu, Köpüş, Maymuş, Kaliş, Möcük, Zezee, Bibii, Kekee, Mimi, Mimii, Duduu, Tutuu, Ekee, Babaa, Zuku
- Yasak: Pepee'nin ve Bebee'nin konuşma zorluğu hikayeye konmaz; kimse konuşmasıyla alay etmez.
- Yasak: Dedee'nin uçan balonu hikayeye girmez (yükseklik).
- İzinli dünya kelimeleri: tulum, kahvaltı, pekmez, tahin, dans

## Onarılacak hikâyeler

### Hikâye 1: tohum pepee-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Nenee
@tohum: pepee-0141
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yağmur ya da kar günü
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'çömlek', fiil 'bindirmek', sıfat 'ahşap'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Nenee
@plan: yağmur yağdı ve salıncak oyunu bozuldu | şemsiyenin altında dans edip yeni bir oyun buldu
@tohum: pepee-0141
@degisim: çömlek -> şemsiye
Parkta hafif bir yağmur başladı. Nenee Pepee'yi ahşap salıncağa bindirmek istiyordu. Ama salıncak yağmurdan ıslanmıştı. "Salıncak ıslak, şimdi ne oynayalım?" dedi Nenee üzgün bir sesle. Sonra çantasından büyük bir şemsiye çıkardı. İkisi şemsiyenin altına girdi. Damlalar şemsiyeye tık tık vurdu. Pepee bu sesle dans etmeye başladı. Bir sağa, bir sola zıpladı ve ellerini çırptı. "Nenee, sen de gel!" dedi Pepee. Nenee çok güldü ve Pepee'nin elini tuttu. İkisi el ele yavaşça döndü. "Pepee, bu yağmur oyunu salıncaktan da güzel!" dedi Nenee.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonra çantasından büyük bir şemsiye çıkardı"
   - Cümle 5: «Sonra çantasından büyük bir şemsiye çıkardı.»
   - Açıklama: Çözümün ilk ve belirleyici adımını figür Pepee değil yan karakter Nenee atıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0141` birebir aynı, `@degisim: çömlek -> şemsiye` (tutuyorsan), ardından `@onarim: e9a7fcaae7d7b80115dfbcd899d24081b870de3a`, sonra gövde.

### Hikâye 2: tohum pepee-0142 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0142
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: paylaşmak
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'fincan', fiil 'tatmak', sıfat 'üzgün'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: fincanı olmadığı için kumdan kulesi yıkıldı | kuzeninden kule yapmayı öğrendi ve kendisi denedi
@tohum: pepee-0142
@degisim: tatmak -> doldurmak
Pepee ile kuzeni Şila deniz kıyısında kumdan kule yapıyordu. Şila küçük bir fincanla güzel kuleler yaptı. Ama Pepee'nin fincanı yoktu, elle yaptığı kule hemen yıkıldı. Pepee yıkılan kuleye üzgün üzgün baktı. "Şila, ben de kule yapmayı öğrenmek istiyorum," dedi Pepee. "Tabii, fincanı seninle paylaşırım," dedi Şila. Şila fincanı ıslak kumla doldurdu ve kuma ters çevirdi. Pepee Şila'yı dikkatle izledi. Sonra fincanı aldı ve aynısını yaptı. Pepee fincanı kaldırdı ve kum yıkılmadı. Kumda küçük, yuvarlak bir kule duruyordu. Pepee sevinçle ellerini çırptı. Pepee ile Şila fincanı sırayla kullandı ve mutlu mutlu yeni kuleler yaptı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ile kuzeni Şila deniz kıyısında"
   - Cümle 1: «Pepee ile kuzeni Şila deniz kıyısında kumdan kule yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, oysa iki küçük çocuk deniz kıyısında büyük olmadan yeni bir şey deniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şila deniz kıyısında kumdan kule"
   - Cümle 1: «Pepee ile kuzeni Şila deniz kıyısında kumdan kule yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; iki çocuk deniz kıyısında büyük olmadan yalnız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0142` birebir aynı, `@degisim: tatmak -> doldurmak` (tutuyorsan), ardından `@onarim: a6d50532579fb611d98065222adfa7f5a607928a`, sonra gövde.

### Hikâye 3: tohum pepee-0146 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0146
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: sırayla oynamak
- yan: Bebee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kebap', fiil 'koşturmak', sıfat 'soğuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: bir kova vardı ve ikisi de onu istedi | sayı sayarak sırayla kovayı kullandılar
@tohum: pepee-0146
@degisim: kebap -> kova
Deniz kıyısında Pepee ile Bebee kumdan pasta yapıyordu. İkisi de kırmızı kovayı kullanmak istedi. Ama yalnız bir kova vardı ve Bebee üzüldü. Pepee on saymayı yeni öğrenmişti. "Bebee, önce sen doldur, ben de sayı sayarım," dedi Pepee. Bebee soğuk, ıslak kumu kovaya koydu. Pepee parmaklarını tek tek açarak on saydı. Sonra kova Pepee'ye geçti. "Şimdi ben sayabilir miyim?" diye sordu Bebee. "Tabii, parmaklarına bak," dedi Pepee. Pepee kumu doldururken Bebee de yavaşça on saydı. Pepee ile Bebee sırayla kovayı doldurdu ve kumdan pastalar yaptı. Sonra ikisi pastaların etrafında mutlu mutlu koşturdu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee kumu doldururken"
   - Cümle 11: «Pepee kumu doldururken Bebee de yavaşça on saydı.»
   - Açıklama: Kum doldurulmaz, kova doldurulur; 'kovayı kumla doldururken' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0146` birebir aynı, `@degisim: kebap -> kova` (tutuyorsan), ardından `@onarim: 7fe4bfc8597c30ca5b831d0bbffdccb2fbe2278c`, sonra gövde.

### Hikâye 4: tohum pepee-0148 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0148
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'davetiye', fiil 'zıplamak', sıfat 'kırık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: müzik olmadığı için dans oyunu olmadı | zıplarken bulduğu kırık kütüğe davul gibi vurdu
@tohum: pepee-0148
@degisim: davetiye -> kütük
Pepee ile Şila ormanda oynuyordu. Şila dans etmek istedi ama hiç müzik yoktu. Şila üzüldü ve yere oturdu. Pepee onu sevindirmek için yaprakların üstünde zıplayarak dans etti. Birden yerden davul gibi bir ses geldi. Pepee bu sesin ne olduğunu çok merak etti. Hemen yaprakları elleriyle kenara çekti. Altında içi boş, kırık bir kütük vardı. Pepee kütüğe eliyle vurdu ve aynı ses yine geldi. Şila sesi duyunca sevinçle ayağa kalktı. Pepee kütüğe tık tık vurdu ve Şila bu sesle zıplayıp döndü. Pepee bundan sonra garip bir ses duyunca nereden geldiğine hep baktı.
```

**Hakem bulguları (5):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Birden yerden davul gibi bir ses geldi"
   - Cümle 5: «Birden yerden davul gibi bir ses geldi.»
   - Açıklama: Çözüm müzik eksikliğine yönelik bir girişimden değil, dans ederken tesadüfen duyulan sesten çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden yerden davul gibi bir ses geldi"
   - Cümle 5: «Birden yerden davul gibi bir ses geldi.»
   - Açıklama: Çözümü getiren kütük sesi rastlantıyla, sebepsizce beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Altında içi boş, kırık bir kütük vardı"
   - Cümle 8: «Altında içi boş, kırık bir kütük vardı.»
   - Açıklama: Çözümü getiren kütük hiç kurulmadan tesadüfen beliriyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "garip bir ses duyunca nereden geldiğine hep baktı"
   - Cümle 12: «Pepee bundan sonra garip bir ses duyunca nereden geldiğine hep baktı.»
   - Açıklama: Büyük olmadan ormanda garip seslerin kaynağını hep aramak örnek alınacak biçimde veriliyor; güvenli kullanım satırı yeni şeylerin bir büyüğün yanında denenmesini ister.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Pepee bundan sonra garip bir ses duyunca nereden geldiğine hep baktı"
   - Cümle 12: «Pepee bundan sonra garip bir ses duyunca nereden geldiğine hep baktı.»
   - Açıklama: Son ders müzik ve dans hedefine değil başka bir konuya bağlanıyor; kapanış hikayenin hedefini doyurmuyor.
   - Açıklama: Son ders cümlesi müzik ve dans hedefine değil, garip seslere bakmaya dair; kapanış hikayenin sorunundan kopuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0148` birebir aynı, `@degisim: davetiye -> kütük` (tutuyorsan), ardından `@onarim: f24db893ff7b6c5fe82705b87362492f9e644dbd`, sonra gövde.

### Hikâye 5: tohum pepee-0149 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | park | Bebee
@tohum: pepee-0149
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'cetvel', fiil 'yapışmak', sıfat 'devasa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Bebee
@plan: cetvel bankta sarı bir şeye yapıştı | izi kokladı ve bal olduğunu buldu
@tohum: pepee-0149
Pepee parkta devasa bir yaprak buldu. Bebee yaprağı ölçmek için çantasından bir cetvel çıkardı. Ama Bebee'nin banka koyduğu cetvel sarı bir şeye yapıştı. "Pepee, bu sarı şey ne?" diye sordu Bebee. Pepee de bu izi çok merak etti. Eğildi ve yavaşça kokladı. Tatlı bir koku geldi. Pepee kahvaltıda hep bal yediği için bu kokuyu hemen bildi. "Bu bal, Bebee!" dedi Pepee. Sonra cetveli yavaşça çekip banktan aldı. İkisi devasa yaprağı birlikte ölçtü. Yaprak cetvelden bile uzundu! Pepee çok sevindi, çünkü sarı izin bal olduğunu bulmuştu.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "izi kokladı ve bal olduğunu buldu"
   - Cümle 0 (plan satırı): «cetvel bankta sarı bir şeye yapıştı | izi kokladı ve bal olduğunu buldu»
   - Açıklama: Plan çözümü koklamak olarak veriyor ama gövdede sorun cetveli çekip almakla çözülüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "parkta devasa bir yaprak"
   - Cümle 1: «Pepee parkta devasa bir yaprak buldu.»
   - Açıklama: 'Devasa' 3 yaşındaki çocuğun bildiği bir kelime değil.
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmediği bir kelime; 'kocaman' olmalı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bebee'nin banka koyduğu cetvel sarı bir şeye yapıştı"
   - Cümle 3: «Ama Bebee'nin banka koyduğu cetvel sarı bir şeye yapıştı.»
   - Açıklama: Bankta balın neden olduğu söylenmiyor ve sorun önemsiz bir yapışmaya dayanıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "cetvel sarı bir şeye yapıştı"
   - Cümle 3: «Ama Bebee'nin banka koyduğu cetvel sarı bir şeye yapıştı.»
   - Açıklama: Bankta balın neden olduğu söylenmiyor ve cetvelin yapışması önemsiz bir olay.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Eğildi ve yavaşça kokladı"
   - Cümle 6: «Eğildi ve yavaşça kokladı.»
   - Açıklama: Pepee bankta bulduğu bilinmeyen yapışkan bir maddeyi eğilip kokluyor; çocuk yabancı maddeleri koklamayı taklit edebilir.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Eğildi ve yavaşça kokladı"
   - Cümle 6: «Eğildi ve yavaşça kokladı.»
   - Açıklama: İzi koklayıp bal olduğunu anlamak cetvelin yapışmasını çözmüyor, çözüm sebebe yönelmiyor.
   - Açıklama: İzi koklayıp bal olduğunu bulmak yapışmayı çözmüyor; cetvel sonradan sebepsizce çekilip alınıyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu kokuyu hemen bildi"
   - Cümle 8: «Pepee kahvaltıda hep bal yediği için bu kokuyu hemen bildi.»
   - Açıklama: Koku bilinmez, tanınır; 'kokuyu hemen tanıdı' olmalı.
   - Açıklama: Koku 'bilinmez', 'tanınır'; 'kokuyu hemen tanıdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0149` birebir aynı, ardından `@onarim: 90a898d490782bdc037754a6fdad2770bc8d44b3`, sonra gövde.

### Hikâye 6: tohum pepee-0150 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | -
@tohum: pepee-0150
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kupa', fiil 'sabırsızlanmak', sıfat 'şirin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | -
@plan: tahin çok koyuydu ve pekmeze karışmadı | kaşığı yavaş yavaş çevirip ikisini karıştırdı
@tohum: pepee-0150
@degisim: sabırsızlanmak -> üzülmek
Bir sabah Pepee parktaki bankta kahvaltı yapıyordu. Şirin kupasında tahin ve pekmezi ilk kez kendisi karıştırmak istedi. Ama tahin çok koyuydu ve kaşık zor döndü. Pepee biraz üzüldü ve kaşığı hızlı hızlı çevirdi. Yine de tahin kupanın dibinde kaldı. Pepee durdu ve kupaya dikkatle baktı. Sonra kaşıkla küçük ve yavaş daireler çizdi. Koyu tahin sonunda pekmeze karıştı. Kupada kahverengi, parlak bir tahin pekmez oldu. Pepee ekmeğini kupaya batırdı ve tadına baktı. Tadı çok güzeldi. Pepee çok mutlu oldu, çünkü ilk tahin pekmezini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şirin kupasında tahin ve"
   - Cümle 2: «Şirin kupasında tahin ve pekmezi ilk kez kendisi karıştırmak istedi.»
   - Açıklama: Cümle başındaki 'Şirin' bir ad gibi okunuyor; kelimenin anlamı ve kupanın kime ait olduğu belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0150` birebir aynı, `@degisim: sabırsızlanmak -> üzülmek` (tutuyorsan), ardından `@onarim: e45b58f74512e2673d898c7d823c5737d96a32e9`, sonra gövde.

### Hikâye 7: tohum pepee-0152 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Dedee
@tohum: pepee-0152
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yağmur ya da kar günü
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'masa', fiil 'boyamak', sıfat 'değişik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Dedee
@plan: kuru kar dağıldı ve kar topu olmadı | dedesinden öğrendi ve karı iyice sıktı
@tohum: pepee-0152
@degisim: boyamak -> sıkmak
Pepee ile Dedee kar yağan bir sabah parktaydı. Parktaki masanın üstü kar doluydu. Pepee masada kar topu yapmak istedi ama kuru kar hep dağıldı. "Dedeciğim, kardan nasıl top yaparım?" diye sordu Pepee. "Karı iki elinle iyice sık," dedi Dedee. Pepee iki eliyle biraz kar aldı ve denedi. Önce hafifçe, sonra daha sıkı bastırdı. Bu kez kar yuvarlak bir top oldu. Pepee büyük, küçük, değişik toplar yapıp masaya dizdi. Dedee en büyük topun üstüne küçük bir top koydu. "Bak, Pepee, kardan bir kule yaptık!" dedi Dedee. Pepee çok sevindi, çünkü kar topu yapmayı öğrenmişti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Karı iki elinle iyice sık"
   - Cümle 5: «"Karı iki elinle iyice sık," dedi Dedee.»
   - Açıklama: Sorunun sebebi karın kuru olması ama çözüm yalnız daha sıkı bastırmak, kuruluğa yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0152` birebir aynı, `@degisim: boyamak -> sıkmak` (tutuyorsan), ardından `@onarim: 921dcea762b4a46dacf64d5a6190f98de9798bd1`, sonra gövde.

### Hikâye 8: tohum pepee-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0156
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: paylaşmak
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'ceket', fiil 'gülüşmek', sıfat 'karmakarışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: sepet sallandı ve çiçekler karmakarışık oldu | çiçekleri tek tek alıp annesiyle paylaştı
@tohum: pepee-0156
Pepee ormanda annesinin yanında sepete çiçek topluyordu. Pepee çiçeklerin yarısını annesine vermek istedi. Ama sepet çok sallandı ve çiçekler karmakarışık oldu. "Anneciğim, bunları nasıl düzeltirim?" diye sordu Pepee. Annee ceketini yere serdi ve çiçekleri onun üstüne yaydı. Sonra bir çiçeği tuttu ve yavaşça çekip aldı. "Böyle tek tek alırsan çiçekler kırılmaz," dedi Annee. Pepee bunu hemen öğrendi ve kendisi denedi. Çiçekleri tek tek aldı ve iki demet yaptı. Bir demeti annesine uzattı. "Bu demet senin, anneciğim," dedi Pepee. Annee çiçekleri kokladı ve ikisi gülüştü. Pepee çok mutlu oldu, çünkü çiçeklerini annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sepet çok sallandı"
   - Cümle 3: «Ama sepet çok sallandı ve çiçekler karmakarışık oldu.»
   - Açıklama: Sepetin neden sallandığı söylenmiyor, sorunun sebebi belirsiz.
   - Açıklama: Sepetin neden sallandığı söylenmiyor; sorunun sebebi belirsiz kalıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Annee ceketini yere serdi ve çiçekleri onun üstüne yaydı"
   - Cümle 5: «Annee ceketini yere serdi ve çiçekleri onun üstüne yaydı.»
   - Açıklama: Çözümün ilk adımını ve yöntemini anne uyguluyor; Pepee yalnız annesini taklit ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0156` birebir aynı, ardından `@onarim: 8c59e2ddc9c26cada06d293dbcec9ba6b862ab84`, sonra gövde.

### Hikâye 9: tohum pepee-0157 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0157
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'tarak', fiil 'dağılmak', sıfat 'kokulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kum çok kuruydu ve kale hemen dağıldı | ıslak kumu kovaya doldurup yeni bir kale yaptı
@tohum: pepee-0157
Pepee deniz kokulu kumsalda kumdan bir kale yapıyordu. Kaleyi süslemek için küçük deniz tarağı kabukları toplamıştı. Ama kum çok kuruydu ve kale hemen dağıldı. Pepee kumu yeniden yığdı ama kale yine yıkıldı. Sonra su kenarındaki ıslak kuma baktı. Oradaki kum birbirine yapışıyordu. Pepee ıslak kumun kale için daha iyi olduğunu öğrendi. Kovasını oradaki kumla doldurdu. Kovayı ters çevirdi ve yavaşça kaldırdı. Bu kez kale hiç dağılmadı. Pepee kalenin üstüne tarak kabuklarını tek tek dizdi. Pepee bundan sonra kum kalelerini hep ıslak kumla yaptı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra su kenarındaki ıslak kuma baktı"
   - Cümle 5: «Sonra su kenarındaki ıslak kuma baktı.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada deniz kıyısında su kenarında yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0157` birebir aynı, ardından `@onarim: 2b6ea6f53586fb97afd6457e41df33563826f881`, sonra gövde.

### Hikâye 10: tohum pepee-0159 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0159
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'yağ', fiil 'kurmak', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: yepyeni çorapları yerde kayıyordu | çoraplarını çıkarıp kar taneleri gibi dans etti
@tohum: pepee-0159
@degisim: yağ -> kar
Dışarıda kar yağıyordu. Pepee pencereden havada dönen kar tanelerine baktı. Onlar gibi dans etmek istedi ama yepyeni çorapları yerde kayıyordu. Pepee hemen yere oturdu ve çoraplarını çıkardı. Artık ayakları yere iyi basıyordu. Pepee kendine bir kar tanesi oyunu kurdu. Kollarını iki yana açtı ve pencerenin önünde yavaşça döndü. Sonra dışarıdaki taneler gibi yere indi. Yeniden kalktı ve bir kez daha döndü. Pepee kar taneleriyle birlikte mutlu mutlu dans etmeye devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Onlar gibi dans etmek"
   - Cümle 3: «Onlar gibi dans etmek istedi ama yepyeni çorapları yerde kayıyordu.»
   - Açıklama: Kar taneleri dans etmez; mecaz 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kar taneleriyle birlikte mutlu"
   - Cümle 10: «Pepee kar taneleriyle birlikte mutlu mutlu dans etmeye devam etti.»
   - Açıklama: İçerideki Pepee'nin dışarıdaki kar taneleriyle birlikte dans etmesi mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0159` birebir aynı, `@degisim: yağ -> kar` (tutuyorsan), ardından `@onarim: 1e027a769f396443a11f023fdc94bcfb5185e2e2`, sonra gövde.

### Hikâye 11: tohum pepee-0161 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Dedee
@tohum: pepee-0161
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'yağmur', fiil 'yemek', sıfat 'kolay'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Dedee
@plan: yağmur başladı ve ekmek ıslanmaya başladı | dedesinden yardım istedi ve şemsiyenin altında yedi
@tohum: pepee-0161
Bir sabah Pepee ile Dedee bulutlu havada parkta kahvaltı yapıyordu. Pepee en sevdiği ballı ekmeği yemeye başlamıştı. Birden yağmur başladı ve ekmeğin üstüne damlalar düştü. Pepee ekmeğini kuru yemek istedi. "Dedeciğim, ekmeğim ıslanıyor, bana yardım eder misin?" diye sordu Pepee. "Tabii, bu çok kolay," dedi Dedee. Dedee sepetten büyük bir şemsiye çıkardı ve açtı. Pepee ballı ekmeğini şemsiyenin altında bitirdi. İkisi yağmurun sesini dinleyip güldü. Pepee bundan sonra zorda kalınca dedesinden yardım istedi.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yağmur başladı ve ekmek ıslanmaya başladı"
   - Cümle 0 (plan satırı): «yağmur başladı ve ekmek ıslanmaya başladı | dedesinden yardım istedi ve şemsiyenin altında yedi»
   - Açıklama: Plan satırında 'başladı' fiili gereksiz yere iki kez tekrarlanıyor.
   - Açıklama: 'Başladı' fiili aynı cümlede gereksiz yere tekrar ediliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "zorda kalınca dedesinden yardım"
   - Cümle 10: «Pepee bundan sonra zorda kalınca dedesinden yardım istedi.»
   - Açıklama: 'Zorda kalmak' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bundan sonra zorda kalınca"
   - Cümle 10: «Pepee bundan sonra zorda kalınca dedesinden yardım istedi.»
   - Açıklama: 'Zorda kalmak' deyimsel ve soyut, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0161` birebir aynı, ardından `@onarim: 794b9a1331084f0e70343e0186ee88c532eebb66`, sonra gövde.

### Hikâye 12: tohum pepee-0164 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Şila
@tohum: pepee-0164
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kaktüs', fiil 'süpürmek', sıfat 'ıslak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Şila
@plan: top kaktüsü devirdi ve toprak yere döküldü | özür diledi ve toprağı süpürdü
@tohum: pepee-0164
Yağmur cama tıp tıp vuruyordu. Pepee ile Şila kahvaltıdan önce evde yumuşak bir topla oynuyordu. Pepee topa sert vurdu ve top, Şila'nın getirdiği kaktüsü devirdi. Saksının ıslak toprağı yere döküldü. Şila çok üzüldü, çünkü kaktüsü Pepee için getirmişti. "Özür dilerim, Şila, dikkat etmedim," dedi Pepee. Pepee saksıyı kaldırdı ve yerine koydu. Sonra süpürgeyi getirdi ve yerdeki toprağı süpürüp saksıya koydu. Kaktüs yine dimdik duruyordu. Şila gülümsedi ve Pepee'ye sarıldı. "Hadi, Şila, şimdi birlikte kahvaltı yapalım!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kahvaltıdan önce evde yumuşak"
   - Cümle 2: «Pepee ile Şila kahvaltıdan önce evde yumuşak bir topla oynuyordu.»
   - Açıklama: Tohum özelliği kahvaltı sorunun çözümünde işe yaramıyor, yalnız süs olarak iki kez anılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee ile Şila kahvaltıdan önce"
   - Cümle 2: «Pepee ile Şila kahvaltıdan önce evde yumuşak bir topla oynuyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği iki kez süs olarak geçiyor ve sorunun çözümünde hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0164` birebir aynı, ardından `@onarim: 04b7a474ce35e68e9d560eaf8b046e3b0d0abcb3`, sonra gövde.
