# Editör görevi (onarım): Pepee, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0055 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0055
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: kaybolan eşya
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mercan', fiil 'beslemek', sıfat 'uzak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: pembe mercan parçası kumda kayboldu | kumdaki ayak izlerini takip etti ve mercan parçasını buldu
@tohum: pepee-0055
@degisim: beslemek -> bırakmak
Bir sabah Pepee ile kuzeni Şila kumda deniz kabuğu topluyordu. Birden Şila durdu, çünkü pembe mercan parçası kaybolmuştu. "Mercan parçasını kumda bir yere bıraktım ama yerini unuttum," dedi Şila. Pepee, Şila'nın kumdaki küçük ayak izlerini gördü. Pepee daha önce hiç iz takip etmemişti ve bunu öğrenmek istedi. Bu izleri adım adım takip etti. İzler onları kumda biraz uzak bir yere götürdü. Orada kumun içinde pembe bir uç vardı. Pepee kumu elleriyle açtı ve mercan parçasını buldu. "İşte mercan, Şila!" dedi Pepee. Şila onu aldı ve Pepee'ye sarıldı. Sonra ikisi kabuk toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İzler onları kumda biraz uzak bir yere götürdü"
   - Cümle 7: «İzler onları kumda biraz uzak bir yere götürdü.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada yetişkin olmadan izleri takip ederek uzaklaşıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, oysa iki çocuk yanlarında büyük olmadan kumsalda uzağa gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0055` birebir aynı, `@degisim: beslemek -> bırakmak` (tutuyorsan), ardından `@onarim: c8d5b557a41e00b3cc36f69eae202834777e49e1`, sonra gövde.

### Hikâye 2: tohum pepee-0056 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0056
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'vazo', fiil 'yapmak', sıfat 'reçelli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kuru kumdan yapılan vazo hemen dağıldı | kumu açıp altındaki ıslak kumla vazoyu yeniden yaptı
@tohum: pepee-0056
@degisim: reçelli -> ıslak
Bir sabah Pepee deniz kıyısında kumla oynuyordu. Kumdan bir vazo yapmayı ilk kez deniyordu. Ama kum çok kuruydu ve vazo hemen dağıldı. Pepee biraz düşündü ve kumu kazdı. Kumun altı koyu renkliydi ve ıslaktı. Pepee kovasını bu ıslak kumla doldurdu. Kumu elleriyle sıkıca bastırdı ve uzun bir vazo yaptı. Sonra ortasını parmağıyla açtı. Bu kez vazo sağlam kaldı. Pepee vazonun içine iki uzun deniz kabuğu koydu. Kabuklar vazoda çiçek gibi duruyordu. Pepee çok sevindi, çünkü ıslak kumla vazo yapmayı öğrenmişti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumu açıp altındaki ıslak kumla"
   - Cümle 0 (plan satırı): «kuru kumdan yapılan vazo hemen dağıldı | kumu açıp altındaki ıslak kumla vazoyu yeniden yaptı»
   - Açıklama: Kum açılmaz; burada 'kazıp' olmalı, gövde de 'kumu kazdı' diyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumu açıp altındaki"
   - Cümle 0 (plan satırı): «kuru kumdan yapılan vazo hemen dağıldı | kumu açıp altındaki ıslak kumla vazoyu yeniden yaptı»
   - Açıklama: Kum açılmaz; 'kumu kazıp' olmalı.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee deniz kıyısında kumla oynuyordu"
   - Cümle 1: «Bir sabah Pepee deniz kıyısında kumla oynuyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız deniyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kumdan bir vazo yapmayı ilk kez deniyordu"
   - Cümle 2: «Kumdan bir vazo yapmayı ilk kez deniyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; deniz kıyısında yalnız deniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kabuklar vazoda çiçek gibi"
   - Cümle 11: «Kabuklar vazoda çiçek gibi duruyordu.»
   - Açıklama: Benzetme kullanılmış; mecaz sayılabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0056` birebir aynı, `@degisim: reçelli -> ıslak` (tutuyorsan), ardından `@onarim: af106af8d45003bc013b6e4e88fe454dc36ce8e8`, sonra gövde.

### Hikâye 3: tohum pepee-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0057
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'inci', fiil 'serpmek', sıfat 'yardımsever'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: pastaya koyacak parlak bir süs yoktu | kumdaki kabuğun içine baktı ve inci buldu
@tohum: pepee-0057
@degisim: yardımsever -> parlak
Pepee deniz kıyısında kumdan bir pasta yapıyordu. Pastanın tepesine parlak bir süs koymak istiyordu. Ama etrafta yalnız gri taşlar vardı. Birden kumdaki bir kabuğun içinde beyaz bir şey gördü. Pepee bunun ne olduğunu çok merak etti. Kabuğu dikkatle eline aldı ve içine baktı. Kabuğun içinde küçük, beyaz bir inci vardı! Pepee ilk kez gerçek bir inci görüyordu. Önce pastanın üstüne şeker gibi kuru kum serpti. Sonra inciyi pastanın tepesine yavaşça koydu. Pasta artık çok güzel olmuştu. Pepee o sabah kabukların içinde inci olabileceğini öğrendi.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee deniz kıyısında kumdan bir pasta yapıyordu"
   - Cümle 1: «Pepee deniz kıyısında kumdan bir pasta yapıyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden kumdaki bir kabuğun içinde beyaz bir şey gördü"
   - Cümle 4: «Birden kumdaki bir kabuğun içinde beyaz bir şey gördü.»
   - Açıklama: Çözümü getiren inci Pepee'nin bir çabası olmadan tesadüfen beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce pastanın üstüne şeker gibi kuru kum serpti"
   - Cümle 9: «Önce pastanın üstüne şeker gibi kuru kum serpti.»
   - Açıklama: Kum serpme adımı sebepsiz ekleniyor ve sorunun çözümüne hiçbir katkısı yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "pastanın üstüne şeker gibi kuru kum serpti"
   - Cümle 9: «Önce pastanın üstüne şeker gibi kuru kum serpti.»
   - Açıklama: Kum serpme ayrıntısı soruna ya da çözüme hiçbir katkı yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0057` birebir aynı, `@degisim: yardımsever -> parlak` (tutuyorsan), ardından `@onarim: 10fc317361f7077d7997cbeb80b2ed2a1530b892`, sonra gövde.

### Hikâye 4: tohum pepee-0060 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0060
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kağıt', fiil 'sevinmek', sıfat 'hareketsiz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: çalıdan küçük bir ses geldi | hareketsiz durup dinledi ve dala takılı kağıdı buldu
@tohum: pepee-0060
Ormanda serin bir sabahtı. Pepee ağaçların arasında yürürken küçük bir ses duydu. Ses yanındaki küçük bir çalıdan geliyordu. Pepee sesin ne olduğunu çok merak etti. Hareketsiz durdu ve dikkatle dinledi. Rüzgar esince ses geliyor, rüzgar durunca ses kesiliyordu. Pepee çalıya iyice baktı. Çalıda bir dala takılmış büyük, beyaz bir kağıt vardı! Kağıt sallandıkça hışır hışır ses çıkarıyordu. Pepee sesin kağıttan geldiğini öğrendi. Kağıdı daldan aldı ve çöpe atmak için katladı. Pepee çok sevindi, çünkü sesi yapan şeyi bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesin kağıttan geldiğini öğrendi"
   - Cümle 10: «Pepee sesin kağıttan geldiğini öğrendi.»
   - Açıklama: Burada 'öğrendi' yerine 'anladı' uygun; fiil anlamca yerinde değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0060` birebir aynı, ardından `@onarim: 413d4636fc1354fc3c6349f3a3240737915b8d4e`, sonra gövde.

### Hikâye 5: tohum pepee-0062 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0062
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'lokma', fiil 'kalkmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yukarıdan ekmeğe küçük bir şey düştü | kozalakları buldu ve ağaçtan uzak bir kütüğe oturdu
@tohum: pepee-0062
Ormanda hava çok güzeldi. Pepee büyük bir çam ağacının altında ballı ekmek yiyordu. Birden yukarıdan ekmeğe küçük bir şey düştü. Pepee ağzındaki lokmayı yuttu ve dikkatle baktı. Balın içinde küçük, kahverengi bir kozalak vardı. Pepee bunun nereden geldiğini merak etti ve başını kaldırdı. Rüzgar esince dallardan kozalaklar düşüyordu. Pepee kahvaltısını korumak istedi. Kozalağı çıkarıp yere bıraktı ve kalktı. Ağaçtan uzaktaki sağlam bir kütüğe oturdu. Burada hiçbir kozalak düşmedi. Pepee çok sevindi, çünkü ekmeğini artık rahatça yiyebilirdi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yukarıdan ekmeğe küçük bir şey düştü"
   - Cümle 3: «Birden yukarıdan ekmeğe küçük bir şey düştü.»
   - Açıklama: Ekmeğe küçük bir kozalak düşmesi 'kurdele hamurun içine düştü' gibi önemsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0062` birebir aynı, ardından `@onarim: 0060f2b8f9fda49d2f247289121580fa154130df`, sonra gövde.

### Hikâye 6: tohum pepee-0063 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0063
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'avokado', fiil 'affetmek', sıfat 'berrak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: avokado kumda yuvarlandı ve kayboldu | ninesiyle kumdaki çizgiye bakarak avokadoyu buldu
@tohum: pepee-0063
@degisim: berrak -> yuvarlak
Bir sabah Pepee ile ninesi deniz kıyısında oturuyordu. Nenee sepetinden yeşil, yuvarlak bir avokado çıkardı. Ama avokado elinden düştü ve kumda hızla yuvarlandı. "Affet beni, Pepee, onu tutamadım," dedi Nenee. Pepee etrafa baktı ama avokadoyu göremedi. "O nereye gitti?" diye sordu Pepee. "Kumdaki şu ince çizgiye bak, bu onun izi," dedi Nenee. Pepee izin ne olduğunu ilk kez öğrendi. Sonra ninesiyle birlikte çizgiye bakarak su kenarına yürüdü. Avokado orada, küçük dalgaların yanında duruyordu! Pepee eğildi ve onu dikkatle aldı. "Nineciğim, bak, buldum!" dedi Pepee. "Teşekkürler, Pepee, hadi onu şimdi yiyelim!" dedi Nenee.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kumda hızla yuvarlandı"
   - Cümle 3: «Ama avokado elinden düştü ve kumda hızla yuvarlandı.»
   - Açıklama: Avokadonun yumuşak kumda hızla yuvarlanıp su kenarına kadar gitmesi ve açık kumsalda görünmemesi akla yatkın değil.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kumdaki şu ince çizgiye bak, bu onun izi"
   - Cümle 7: «"Kumdaki şu ince çizgiye bak, bu onun izi," dedi Nenee.»
   - Açıklama: Çözümün anahtarını yan karakter Nenee buluyor; Pepee yalnız onun gösterdiği izi takip ediyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee izin ne olduğunu ilk kez öğrendi"
   - Cümle 8: «Pepee izin ne olduğunu ilk kez öğrendi.»
   - Açıklama: 'izin' kelimesi 'izin (müsaade)' ile karışıyor ve cümle soyut bir öğrenme anlatıyor.
   - Açıklama: Soyut bir öğrenme cümlesi; 'izin' kelimesi 'izin vermek' ile de karışıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0063` birebir aynı, `@degisim: berrak -> yuvarlak` (tutuyorsan), ardından `@onarim: eef6df2383107c30e7834991489740967c739fcd`, sonra gövde.

### Hikâye 7: tohum pepee-0067 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0067
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'topaç', fiil 'birleşmek', sıfat 'rengarenk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: yumuşak kumda ayakları battı | sert kuma gidip orada döndüler
@tohum: pepee-0067
Küçük dalgalar kıyıda ses çıkarıyordu. Pepee ile Bebee kumda iki rengarenk topaç olmuştu. Dönerek ortada birleşmek istiyorlardı ama ayakları yumuşak kuma battı. "Pepee, ayaklarım battı!" dedi Bebee. Pepee etrafına baktı. Su kenarındaki kum ıslak ve sertti. "Gel, Bebee, orada dönelim!" dedi Pepee. İkisi hemen su kenarına yürüdü. Pepee kollarını açtı ve dans ederek döndü. Bebee de ona bakıp kendi yerinde döndü. Ayakları bu kez hiç batmadı. İki topaç dönerek yaklaştı ve ortada birleşti. İkisi birbirine sarıldı. Pepee ile Bebee gülerek oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kumda iki rengarenk topaç olmuştu"
   - Cümle 2: «Pepee ile Bebee kumda iki rengarenk topaç olmuştu.»
   - Açıklama: Çocukların topaç olması mecazdır, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Çocukların topaç olması mecazdır; 3 yaşındaki çocuk için anlaşılmaz.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi hemen su kenarına yürüdü"
   - Cümle 8: «İkisi hemen su kenarına yürüdü.»
   - Açıklama: İki küçük çocuk yanlarında büyük olmadan su kenarına gidiyor; güvenli kullanım satırı bir büyüğün yanında olmayı ister.
   - Açıklama: İki küçük çocuk hiçbir büyük olmadan su kenarına gidiyor; güvenli kullanım satırı büyüğün yanında denemeyi istiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İki topaç dönerek yaklaştı"
   - Cümle 12: «İki topaç dönerek yaklaştı ve ortada birleşti.»
   - Açıklama: Pepee ile Bebee'ye mecazla 'topaç' deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0067` birebir aynı, ardından `@onarim: 84129b3b4a26796650b5450aa4313d4ed2f8717b`, sonra gövde.

### Hikâye 8: tohum pepee-0068 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0068
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yeni bir şeyi denemek
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'çan', fiil 'sıralamak', sıfat 'somurtkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kuru kum kovadan çıkınca dağıldı | kovayı ıslak kumla doldurup kale yaptı
@tohum: pepee-0068
@degisim: çan -> kova
Deniz kıyısında serin bir rüzgar esiyordu. Pepee ilk kez kovayla kumdan bir kale yapmayı deniyordu. Ama kuru kum kovadan çıkınca hemen dağıldı. Pepee somurtkan bir yüzle kuma baktı. "Ne oldu, Pepee?" diye sordu Şila. "Kum hep dağılıyor," dedi Pepee. Pepee sonra su kenarına baktı. Oradaki ıslak kumda Şila'nın ayak izleri duruyordu. Pepee kovayı ıslak kumla doldurdu ve ters çevirdi. Bu kez güzel bir kale çıktı. Şila küçük taşlar getirdi. Pepee taşları kalenin üstüne tek tek sıraladı. "Ne güzel bir kale, Pepee!" dedi Şila. Pepee o gün kaleyi ıslak kumla yapmayı öğrendi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ilk kez kovayla kumdan bir kale yapmayı deniyordu"
   - Cümle 2: «Pepee ilk kez kovayla kumdan bir kale yapmayı deniyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama burada deniz kıyısında yanında yalnız çocuk kuzeni var.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee somurtkan bir yüzle"
   - Cümle 4: «Pepee somurtkan bir yüzle kuma baktı.»
   - Açıklama: 'Somurtkan' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0068` birebir aynı, `@degisim: çan -> kova` (tutuyorsan), ardından `@onarim: 01127e513ebe04768127bd1a945e96560d4a0416`, sonra gövde.

### Hikâye 9: tohum pepee-0069 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0069
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'dalga', fiil 'eğilmek', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: tomurcuk açmamıştı çünkü güneş gelmemişti | kahvaltı yapıp güneşin gelmesini bekledi
@tohum: pepee-0069
@degisim: dalga -> tomurcuk
Ormanda serin bir sabah Pepee ile Annee kahvaltı yapıyordu. Yanlarında sarı bir çiçek tomurcuğu vardı. Tomurcuk daha açmamıştı, çünkü güneş ona gelmemişti. Pepee onun açmasını görmek istiyordu. Annee güneşin ağaçların üstüne çıktığını gösterdi. Pepee beklerken ekmeğine bal sürdü ve bir yumurta yedi. Annee de kremalı bir çörek yedi. Sonra güneş ağaçların arasından çiçeğin üstüne geldi. Pepee hemen onun yanına eğildi. Sarı yapraklar yavaş yavaş açıldı. Annee gülümsedi ve Pepee'nin elini tuttu. Pepee çok sevindi, çünkü çiçeğin açmasını kendisi görmüştü.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kahvaltı yapıp güneşin gelmesini bekledi"
   - Cümle 0 (plan satırı): «tomurcuk açmamıştı çünkü güneş gelmemişti | kahvaltı yapıp güneşin gelmesini bekledi»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunun çözümüne katkı vermiyor, yalnız bekleme sırasında süs olarak geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annee de kremalı bir çörek yedi"
   - Cümle 7: «Annee de kremalı bir çörek yedi.»
   - Açıklama: Çörek ayrıntısı olayda hiçbir işe yaramıyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonra güneş ağaçların arasından çiçeğin üstüne geldi"
   - Cümle 8: «Sonra güneş ağaçların arasından çiçeğin üstüne geldi.»
   - Açıklama: Sorunu Pepee çözmüyor; güneş kendiliğinden gelince tomurcuk açılıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Pepee hemen onun yanına eğildi"
   - Cümle 9: «Pepee hemen onun yanına eğildi.»
   - Açıklama: 'onun' zamirinin çiçeği mi Annee'yi mi gösterdiği belli değil.
   - Açıklama: Önceki cümlenin öznesi güneş olduğu için 'onun' zamirinin çiçeği mi güneşi mi gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0069` birebir aynı, `@degisim: dalga -> tomurcuk` (tutuyorsan), ardından `@onarim: d161a6a7e30d252a18e8cf00c306d92e0aa8ca3c`, sonra gövde.

### Hikâye 10: tohum pepee-0070 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0070
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'ayakkabı', fiil 'yaklaşmak', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: küçük dalgalar örtüye yaklaştı | örtüyü ayakkabının yanındaki kuru kuma taşıdı
@tohum: pepee-0070
Güneş parlıyordu ve deniz ışıltılıydı. Pepee su kenarında dedesine sürpriz bir kahvaltı hazırlıyordu. Ama küçük dalgalar gelip örtüye yaklaştı. Örtünün ucu ıslandı. Pepee etrafına baktı. Dedee ayakkabısını kuru kumda bırakıp yürümeye gitmişti. Pepee örtüyü ve her şeyi oraya taşıdı. Balı, yumurtayı ve ekmeği ayakkabının yanına koydu. Dalgalar artık oraya gelemedi. Biraz sonra Dedee geri geldi. Sürprizi görünce güldü ve Pepee'ye sarıldı. İkisi kumda oturup balı ve yumurtayı paylaştı. Pepee bundan sonra sofrayı hep kuru kumda kurdu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Dedee ayakkabısını kuru kumda bırakıp yürümeye gitmişti"
   - Cümle 6: «Dedee ayakkabısını kuru kumda bırakıp yürümeye gitmişti.»
   - Açıklama: Pepee su kenarında büyüğü olmadan yalnız bırakılıyor; güvenli kullanım satırı bir büyüğün yanında olmayı ister.
   - Açıklama: Dört yaşındaki Pepee su kenarında dalgaların yanında büyüksüz yalnız kalıyor; bu, güvenli özellik kullanımı satırına aykırı ve taklit edilince tehlikeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0070` birebir aynı, ardından `@onarim: 1591b1084d1200e14e2963bf764061c02c4b943d`, sonra gövde.

### Hikâye 11: tohum pepee-0073 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0073
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'çekirdek', fiil 'eğlenmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: oynayacakları yer kuru dallarla doluydu | dalları kenara taşıyıp çiçekler koydu
@tohum: pepee-0073
@degisim: çekirdek -> çiçek
Pepee ormanda kardeşi Bebee için bir sürpriz hazırlıyordu. Bebee bir ağacın arkasında gözlerini kapatıp bekliyordu. Ama oynayacakları yer kuru dallarla doluydu ve güvenli değildi. Pepee dalları tek tek topladı ve kenara taşıdı. Yerde yumuşak çimenler kaldı. Pepee çimenlerin etrafına renkli çiçekler koydu. "Şimdi gözlerini aç, Bebee!" dedi Pepee. Bebee gözlerini açtı ve çiçekleri gördü. "Ne güzel bir yer!" dedi Bebee. Pepee kardeşinin elini tuttu ve ikisi çimenlerde dans etti. Döndüler, zıpladılar ve çok eğlendiler. Pepee çok mutluydu, çünkü sürprizi kardeşini sevindirmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee çimenlerin etrafına renkli çiçekler koydu"
   - Cümle 6: «Pepee çimenlerin etrafına renkli çiçekler koydu.»
   - Açıklama: Çiçekler nereden geldiği söylenmeden sebepsizce beliriyor.
   - Açıklama: Çiçeklerin nereden geldiği söylenmiyor, sebepsizce beliriyorlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0073` birebir aynı, `@degisim: çekirdek -> çiçek` (tutuyorsan), ardından `@onarim: 08bd71dce0a8f8986bcb251346d0c6c1f08b37b9`, sonra gövde.

### Hikâye 12: tohum pepee-0075 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | -
@tohum: pepee-0075
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: kaybolan eşya
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'dal', fiil 'kaplamak', sıfat 'meraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | -
@plan: sarı yapraklar kahvaltı kutusunun üstünü kapladı | bir dalla yaprakları kenara itip kutuyu buldu
@tohum: pepee-0075
Rüzgar parkta hızlı hızlı esiyordu. Pepee kahvaltı kutusunu kaydırağın yanına koydu ve kaydıraktan kaydı. Dönünce kutusunu göremedi, çünkü sarı yapraklar onun üstünü kaplamıştı. Pepee meraklı gözlerle her yere baktı. Kaydırağın yanında büyük bir yaprak yığını vardı. Pepee rüzgarın düşürdüğü kuru bir dalı aldı. Dalla yaprakları yavaş yavaş kenara itti. Yaprakların altından mavi kutusu göründü. Pepee kutuyu açtı ve içine baktı. Balı ve yumurtası yerinde duruyordu. Pepee kutusuna sarıldı ve güldü. Pepee bundan sonra kaybolan şeyleri yaprakların altında da aradı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee meraklı gözlerle her"
   - Cümle 4: «Pepee meraklı gözlerle her yere baktı.»
   - Açıklama: 'Meraklı gözlerle' mecazlı bir kalıp; 3 yaşındaki çocuk için sade değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0075` birebir aynı, ardından `@onarim: 1abdada30d2a83156bffdef3881637a550eda056`, sonra gövde.
