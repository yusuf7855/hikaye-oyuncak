# Editör görevi (onarım): Pepee, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0087 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0087
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'toz', fiil 'uçuşmak', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: kar taneleri sıcak elinde hemen eriyordu | soğuk kolunu karın altına uzattı
@tohum: pepee-0087
@degisim: tozlu -> soğuk
Pepee evinin yanındaki ormanda oynarken kar yağmaya başladı. Küçük kar taneleri havada uçuşuyordu. Pepee onların şeklini görmek istedi ama taneler sıcak elinde hemen eriyordu. Pepee durdu ve biraz düşündü. Sonra tulumunun mavi kolunu karın altına uzattı. Kol, sıcak elinden daha soğuktu. Toz gibi ince kar, kolun üstüne yağdı. Taneler bu kez erimedi. Pepee kolunu gözüne yaklaştırdı ve dikkatle baktı. Her tane küçük bir yıldız gibiydi! Pepee çok sevindi, çünkü kar tanesinin şeklini öğrenmişti.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee evinin yanındaki ormanda oynarken"
   - Cümle 1: «Pepee evinin yanındaki ormanda oynarken kar yağmaya başladı.»
   - Açıklama: Güvenli kullanım satırı yeni şeyleri bir büyüğün yanında denemeyi ister, oysa Pepee kar yağarken ormanda yalnız oynuyor.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Pepee evinin yanındaki ormanda oynarken kar yağmaya başladı"
   - Cümle 1: «Pepee evinin yanındaki ormanda oynarken kar yağmaya başladı.»
   - Açıklama: Orman tarifi ağaçlarla ve çiçeklerle dolu genel bir orman diyor; ormanın evin yanında olduğu ve kar yağdığı bilgisi tarife eklenmiş.
3. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "evinin yanındaki ormanda"
   - Cümle 1: «Pepee evinin yanındaki ormanda oynarken kar yağmaya başladı.»
   - Açıklama: Kartın orman tarifi ve kararları ormanın eve bitişik olduğu gibi dizi bilgisi eklenmesine izin vermez.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee onların şeklini görmek istedi"
   - Cümle 3: «Pepee onların şeklini görmek istedi ama taneler sıcak elinde hemen eriyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada ormanda yalnız başına deneme yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0087` birebir aynı, `@degisim: tozlu -> soğuk` (tutuyorsan), ardından `@onarim: 83ab468ca0fd8fb7eda0fd8b6f272772b3b0e5e7`, sonra gövde.

### Hikâye 2: tohum pepee-0093 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0093
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: bir şey yapmak
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'süpürge', fiil 'öğretmek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kumdaki çukurlar yüzünden bahçe düz olmadı | eski süpürgeyle kumu düzeltmeyi öğrendi
@tohum: pepee-0093
@degisim: öğretmek -> düzeltmek
Bir sabah Pepee deniz kıyısına kovasını ve eski oyuncak süpürgesini getirdi. Sudan uzakta kumdan bir ev ve düz bir bahçe yapmak istedi. Ama kumda ayaklarından kalan bir sürü küçük çukur vardı. Pepee çukurları eliyle kapattı ama her yerde parmak izleri kaldı. Pepee biraz düşündü. Sonra süpürgesini aldı ve bahçenin üstünde ileri geri gezdirdi. Çukurlar doldu, izler de kayboldu ve bahçe dümdüz oldu. Böylece Pepee kumu süpürgeyle düzeltmeyi öğrendi. Sonra bahçeye kabuklardan küçük bir yol yaptı. Pepee kumdan evinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee deniz kıyısına"
   - Cümle 1: «Bir sabah Pepee deniz kıyısına kovasını ve eski oyuncak süpürgesini getirdi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında yapayalnız yeni bir şey deniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "deniz kıyısına kovasını ve eski"
   - Cümle 1: «Bir sabah Pepee deniz kıyısına kovasını ve eski oyuncak süpürgesini getirdi.»
   - Açıklama: Kova işe yarayacakmış gibi getiriliyor ama hikayede hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0093` birebir aynı, `@degisim: öğretmek -> düzeltmek` (tutuyorsan), ardından `@onarim: c9b832d53e2393b2b1fdb9290e8017a7d176d242`, sonra gövde.

### Hikâye 3: tohum pepee-0094 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Bebee
@tohum: pepee-0094
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bebee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'delik', fiil 'kazanmak', sıfat 'temkinli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Bebee
@plan: kazanmak için kardeşinin topunu elinden çekip aldı | özür diledi ve kardeşinden yavaş atmayı öğrendi
@tohum: pepee-0094
@degisim: temkinli -> yavaş
Pepee evde Bebee ile delikli bir kutuya top atıyordu. Bebee topları yavaş atıyordu ve hepsi kutuya giriyordu. Pepee kazanmak istedi ve kardeşinin elindeki topu çekip aldı. Bebee çok üzüldü ve ağlamaya başladı. Pepee durdu ve topu ona geri verdi. "Özür dilerim, Bebee. Bana nasıl attığını öğretir misin?" dedi Pepee. Bebee gözlerini sildi ve güldü. "Önce deliğe iyi bak, sonra yavaşça at," dedi Bebee. Pepee kardeşinden öğrendiği gibi topu attı. Top tam içeri girdi. Bebee sevinçle zıpladı. "Teşekkürler, Bebee, şimdi ikimiz de kazanıyoruz!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Pepee kazanmak istedi"
   - Cümle 3: «Pepee kazanmak istedi ve kardeşinin elindeki topu çekip aldı.»
   - Açıklama: Pepee'nin neden kaybettiği, yani kendi atışlarının kutuya girmediği hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0094` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: 7d3ce556edad44ff53eefa09e640b907b33d16b6`, sonra gövde.

### Hikâye 4: tohum pepee-0095 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Annee
@tohum: pepee-0095
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'yulaf', fiil 'izlemek', sıfat 'limonlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Annee
@plan: kurabiye saklıydı ve nereye bakacağını bilmiyordu | sıcak soğuk oyununu öğrendi ve kurabiyeyi buldu
@tohum: pepee-0095
Pepee parkta annesiyle yeni bir oyun oynuyordu. Annee limonlu bir yulaf kurabiyesini kaydırağın altına sakladı. Ama Pepee nereye bakacağını bilmiyordu ve onu bulamadı. "Anneciğim, kurabiye nerede?" diye sordu Pepee. "Yakına gelince 'sıcak', uzağa gidince 'soğuk' derim," dedi Annee. Sonra Annee oturdu ve onu izledi. Pepee sıcak soğuk oyununu hemen öğrendi ve salıncağa yürüdü. "Soğuk!" dedi Annee. Pepee geri döndü ve kaydırağa koştu. "Sıcak, çok sıcak!" dedi Annee. Pepee kaydırağın altına eğildi ve kurabiyeyi buldu. Onu ikiye böldü ve yarısını annesine verdi. "Anneciğim, bu oyun çok güzel, bir daha oynayalım!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sıcak soğuk oyununu öğrendi ve kurabiyeyi buldu"
   - Cümle 0 (plan satırı): «kurabiye saklıydı ve nereye bakacağını bilmiyordu | sıcak soğuk oyununu öğrendi ve kurabiyeyi buldu»
   - Açıklama: Planda oyunu Pepee öğreniyor ama gövdede oyunu öğrenen Annee olarak yazılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0095` birebir aynı, ardından `@onarim: 85cf5c0aa0f074d3c30a41a8095cc4ca178000d5`, sonra gövde.

### Hikâye 5: tohum pepee-0097 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0097
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'havlu', fiil 'gezinmek', sıfat 'kısa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: havlunun üstündeki yumurta kayboldu | kumdaki izin yanından yürüyüp yumurtayı buldu
@tohum: pepee-0097
Bir sabah Pepee ile Şila deniz kıyısında gezindi. Pepee yumurtasını bir kum tepesinde, havlunun üstüne koymuştu. Ama geri döndüklerinde yumurta havluda yoktu. "Şila, yumurtamı gördün mü?" diye sordu Pepee. "Hayır, görmedim," dedi Şila. Sonra Pepee kumda ince bir iz gördü ve çok merak etti. İz tepeden aşağı iniyordu. Pepee kahvaltıda hep yumurta yerdi ve yumurtanın yuvarlak olduğunu bilirdi. Bu yüzden izin yanından yavaşça yürüdü. İz kısaydı ve tepenin dibinde bitti. Yumurta orada, kumun üstünde duruyordu. "Yumurtam tepeden aşağı yuvarlanmış!" dedi Pepee. Pepee çok sevindi, çünkü yumurtasını bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yumurtanın yuvarlak olduğunu bilirdi"
   - Cümle 8: «Pepee kahvaltıda hep yumurta yerdi ve yumurtanın yuvarlak olduğunu bilirdi.»
   - Açıklama: Kahvaltıda yumurta yemesi ile izin yanından yürümesi arasında mantıklı bir bağ yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0097` birebir aynı, ardından `@onarim: 440a6d669d4044a3060cb0b495a27b65e4f2b39c`, sonra gövde.

### Hikâye 6: tohum pepee-0100 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0100
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'mikroskop', fiil 'hazırlanmak', sıfat 'ferah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: gösteri için müzik çalacak bir şeyleri yoktu | ayaklarını yere vurarak dans edip ses çıkardı
@tohum: pepee-0100
@degisim: mikroskop -> çiçek
Rüzgar ağaçların arasında hafifçe esiyordu. Pepee ile Şila ormanda ferah bir yerde gösteriye hazırlanıyordu. Ama yanlarında müzik çalacak hiçbir şey yoktu. "Pepee, müzik olmadan nasıl dans edeceğiz?" diye sordu Şila. Pepee biraz düşündü. Sonra ayaklarını yere vurarak dans etmeye başladı. Tap, tap, tap diye güzel bir ses çıktı. Pepee dönerken ellerini de çırptı. "Şila, işte müzik!" dedi Pepee. Şila bu sesle çiçeklerin arasında güzelce dans etti. Pepee ses çıkarmayı hiç bırakmadı. Gösterinin sonunda ikisi birbirini alkışladı. Sonra el ele tutuşup oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah bir yerde gösteriye"
   - Cümle 2: «Pepee ile Şila ormanda ferah bir yerde gösteriye hazırlanıyordu.»
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormanda ferah bir yerde"
   - Cümle 2: «Pepee ile Şila ormanda ferah bir yerde gösteriye hazırlanıyordu.»
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yanlarında müzik çalacak hiçbir şey yoktu"
   - Cümle 3: «Ama yanlarında müzik çalacak hiçbir şey yoktu.»
   - Açıklama: Gösteriye hazırlanırken neden müzik çalacak bir şeyleri olmadığı söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0100` birebir aynı, `@degisim: mikroskop -> çiçek` (tutuyorsan), ardından `@onarim: 3c7357335110e2df0d23c7292a1561619f1f124c`, sonra gövde.

### Hikâye 7: tohum pepee-0103 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0103
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'halka', fiil 'sormak', sıfat 'şeffaf'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: yumurtanın kabuğu çok sertti ve kardeşi onu çıkaramadı | yumurtayı kapağa vurdu ve avucunda yuvarladı
@tohum: pepee-0103
@degisim: halka -> kabuk
Deniz kıyısında Pepee ile Bebee kumun üstünde kahvaltı yapıyordu. Bebee şeffaf kutusundan bir yumurta aldı. Ama yumurtanın kabuğu çok sertti ve Bebee onu çıkaramadı. "Pepee, bu kabuk nasıl çıkar?" diye sordu Bebee. Pepee yumurtayı aldı ve kahvaltıda hep yaptığı gibi kutunun kapağına hafifçe vurdu. Kabuk küçük küçük çatladı. Sonra Pepee yumurtayı avucunda yavaşça yuvarladı. "Şimdi sen dene, Bebee," dedi Pepee. Bebee kabuğun parçalarını tek tek aldı. Kabuğun altından bembeyaz yumurta göründü. Bebee yumurtasını mutlu mutlu yedi. Pepee çok sevindi, çünkü kardeşine yardım etmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bebee şeffaf kutusundan bir"
   - Cümle 2: «Bebee şeffaf kutusundan bir yumurta aldı.»
   - Açıklama: 'Şeffaf' 3 yaşındaki bir çocuğun bilmeyeceği bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0103` birebir aynı, `@degisim: halka -> kabuk` (tutuyorsan), ardından `@onarim: 021e93042f3ac185557840569ad3e2bc13ae5cc6`, sonra gövde.

### Hikâye 8: tohum pepee-0105 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Annee
@tohum: pepee-0105
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'pasta', fiil 'hatırlamak', sıfat 'ufak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | Annee
@plan: salıncakta kendi başına sallanmayı bilmiyordu | dansını hatırladı ve bacaklarını ileri geri salladı
@tohum: pepee-0105
@degisim: pasta -> ip
Bir sabah Pepee ile Annee parktaydı. Pepee ufak salıncağa oturdu ve kendisi sallanmayı denedi. Ama salıncak hiç kıpırdamadı, çünkü Pepee ne yapacağını bilmiyordu. Pepee dans ederken bacaklarını nasıl salladığını hatırladı. Önce iki eliyle ipleri sıkı sıkı tuttu. Sonra bacaklarını ileri ve geri salladı. Salıncak yavaş yavaş yükselmeye başladı. "Bak, anne, kendim yaptım!" dedi Pepee. "Aferin, Pepee!" dedi Annee ve gülümsedi. Annee de hep salıncağın yanında durdu. Pepee çok sevindi, çünkü salıncağı ilk kez kendisi sallamıştı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "oturdu ve kendisi sallanmayı denedi"
   - Cümle 2: «Pepee ufak salıncağa oturdu ve kendisi sallanmayı denedi.»
   - Açıklama: 'Kendisi sallanmayı' bozuk; 'kendi kendine sallanmayı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Annee de hep salıncağın"
   - Cümle 10: «Annee de hep salıncağın yanında durdu.»
   - Açıklama: 'de' bağlacı yersiz; başka kimse durmuyordu, ayrıca 'hep' olayın sırasına uymuyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Annee de hep salıncağın yanında durdu"
   - Cümle 10: «Annee de hep salıncağın yanında durdu.»
   - Açıklama: 'de' ve 'hep' burada anlamsız; kimle birlikte ve ne zamandan beri durduğu belli değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annee de hep salıncağın yanında durdu"
   - Cümle 10: «Annee de hep salıncağın yanında durdu.»
   - Açıklama: Bu cümle olaydan çıkmıyor ve hikayede hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Olaydan sonra eklenen bu ayrıntı hiçbir işe yaramıyor ve akışı bozuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0105` birebir aynı, `@degisim: pasta -> ip` (tutuyorsan), ardından `@onarim: f2ab99feda2a540583691981170680ebf3b001fc`, sonra gövde.

### Hikâye 9: tohum pepee-0110 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0110
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'su', fiil 'sokulmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: tek ayak üstünde dururken hemen sallandı | dansındaki gibi kollarını iki yana açtı
@tohum: pepee-0110
@degisim: su -> çalı
Ormanda, iki büyük çalının arasında gizli, düz bir çimen vardı. Pepee çalıların arasından bu çimene sokuldu. Orada tek ayak üstünde durmayı denedi ama hemen sallandı. Kolları iki yanında aşağıda duruyordu. Pepee dansını düşündü. Dans ederken kollarını hep iki yana açardı. Pepee yine kollarını açtı ve bir ayağını yavaşça kaldırdı. Bu kez hiç sallanmadı. Pepee bir, iki, üç, dört, beş diye saydı. Sonra öbür ayağıyla da denedi ve yine durabildi. Pepee çok sevindi, çünkü tek ayak üstünde durmayı başarmıştı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çalıların arasından bu çimene sokuldu"
   - Cümle 2: «Pepee çalıların arasından bu çimene sokuldu.»
   - Açıklama: Pepee büyüğü olmadan ormanda gizli bir yere sokuluyor; güvenli kullanım satırı yeni şeylerin bir büyüğün yanında denenmesini söyler.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee çalıların arasından bu çimene sokuldu"
   - Cümle 2: «Pepee çalıların arasından bu çimene sokuldu.»
   - Açıklama: Pepee ormanda büyüksüz, çalıların arasındaki gizli bir yere sokulup yeni bir şeyi yalnız deniyor; güvenli kullanım satırı yeni şeylerin bir büyüğün yanında denenmesini ister.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu çimene sokuldu"
   - Cümle 2: «Pepee çalıların arasından bu çimene sokuldu.»
   - Açıklama: 'Sokulmak' burada yanlış anlamda kullanılmış ve 'çimen' yer adı olarak uygun değil; 'çimenliğe girdi' olmalı.
   - Açıklama: 'Sokulmak' birine yaklaşmak anlamındadır; bir yere girmek için yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0110` birebir aynı, `@degisim: su -> çalı` (tutuyorsan), ardından `@onarim: fd7584129626e1b239140ec45057bff48b4ec7e9`, sonra gövde.

### Hikâye 10: tohum pepee-0113 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0113
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'halı', fiil 'parıldamak', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: ağacın altına girince gölgesi kayboldu | dönüp güneşi gördü ve çiçeklere gitti
@tohum: pepee-0113
@degisim: halı -> gölge
Bir sabah Pepee ormanda gölgesiyle yeni bir oyun oynuyordu. Pepee el salladı, gölgesi de otların üstünde el salladı. Ama Pepee büyük bir ağacın altına girince gölgesi kayboldu. Pepee otlara baktı ama gölgesi yoktu. Ağacın altına hiç güneş gelmiyordu. Pepee dans ederken yaptığı gibi yavaşça döndü ve her yere baktı. İleride güneş çiçeklerin üstünde parıldıyordu. Pepee ağacın altından çıktı ve çiçeklere gitti. Gölgesi otların üstünde hemen geri geldi. Sonra Pepee tek ayak üstünde zıpladı, gölgesi de aynısını yaptı. Pepee çok sevindi, çünkü gölgesini yeniden bulmuştu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Gölgesi otların üstünde hemen geri geldi"
   - Cümle 9: «Gölgesi otların üstünde hemen geri geldi.»
   - Açıklama: 'Geri geldi' fiili bulunma eki değil yönelme eki ister: 'otların üstüne geri geldi'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0113` birebir aynı, `@degisim: halı -> gölge` (tutuyorsan), ardından `@onarim: 5eb2959beea7176d07c78f3d5de0d48fedda63b1`, sonra gövde.

### Hikâye 11: tohum pepee-0114 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0114
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: kaybolan eşya
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'patik', fiil 'sallanmak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: patik kumun altında kaldı ve kayboldu | kumun üstünde dans edip patiği ayağıyla buldu
@tohum: pepee-0114
Pepee ile Bebee deniz kıyısında kumla oynuyordu. Bebee patiğini çıkarıp yanına koymuştu. Ama Bebee kum atarken patiği kumun altında kaldı ve kayboldu. "Patiğim nerede?" diye sordu Bebee. Pepee kumun üstüne baktı ama patiği göremedi. "Bebee, gel, burada dans edip patiği arayalım!" dedi Pepee. İkisi el ele tutuştu ve küçük adımlarla dans etti. Bebee sağa sola sallandı ve güldü. Az sonra Pepee'nin ayağı kumun altında yumuşak bir şeye değdi. Pepee kumu eliyle kazdı ve pembe patiği buldu. Patiği Bebee'nin ayağına giydirdi ve incecik ipini bağladı. İkisi kumda oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "burada dans edip patiği arayalım"
   - Cümle 6: «"Bebee, gel, burada dans edip patiği arayalım!" dedi Pepee.»
   - Açıklama: Dans etmek kumun altındaki patiği bulmaya doğrudan yönelmiyor; patik rastlantıyla bulunuyor.
   - Açıklama: Kumda kaybolan patiği bulmak için dans etmek sebebe doğrudan yönelen bir arama değil, tesadüfe dayanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0114` birebir aynı, ardından `@onarim: b1cae0b10161755083bcb0c3e683ce08e01b4c30`, sonra gövde.

### Hikâye 12: tohum pepee-0119 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0119
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'tekne', fiil 'tanımak', sıfat 'özel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: hafif tekne dalgalar gelince hep devrildi | teknenin ortasına düz bir taş koydu
@tohum: pepee-0119
@degisim: tanımak -> denemek
Küçük dalgalar kumda hafif bir ses çıkarıyordu. Pepee kumda oturmuş, küçük oyuncak teknesiyle oynuyordu. Ama tekne çok hafifti ve dalgalar gelince hep devrildi. Pepee tekneyi üç kez düzeltmeyi denedi ama tekne yine devrildi. Sonra biraz düşündü. Tekneyi dik tutmak için kumdan özel bir taş seçti. Taş düz ve ağırdı. Pepee taşı teknenin tam ortasına koydu. Bir dalga geldi ama tekne bu kez dik kaldı. Tekne dalgaların üstünde sallanarak yüzdü. Pepee taşın tekneyi sağlam tuttuğunu öğrendi. Pepee çok sevindi, çünkü teknesiyle yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee tekneyi üç kez düzeltmeyi denedi"
   - Cümle 4: «Pepee tekneyi üç kez düzeltmeyi denedi ama tekne yine devrildi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada dalgaların kenarında yalnız başına deniyor.
   - Açıklama: Pepee dalgaların geldiği su kenarında büyüksüz tek başına yeni bir şey deniyor; güvenli kullanım satırı yeni şeylerin bir büyüğün yanında denenmesini ister.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumdan özel bir taş seçti"
   - Cümle 6: «Tekneyi dik tutmak için kumdan özel bir taş seçti.»
   - Açıklama: 'Özel' kelimesi anlamsız kullanılmış; taş sıradan, düz ve ağır bir taş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0119` birebir aynı, `@degisim: tanımak -> denemek` (tutuyorsan), ardından `@onarim: 4a7b01fbe45e75a984619cebdd78dc4732b2a1ca`, sonra gövde.
