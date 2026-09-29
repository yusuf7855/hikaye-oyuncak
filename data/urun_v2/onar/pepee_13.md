# Editör görevi (onarım): Pepee, onarım partisi 13

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar13.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar13.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0043 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | -
@tohum: pepee-0043
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'ayçiçeği', fiil 'aramak', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | -
@plan: ayçiçeğinin toprağı çok kuruydu ve çiçek eğilmişti | çeşmeyi arayıp kovasıyla çiçeğe su taşıdı
@tohum: pepee-0043
@degisim: sulu -> kuru
Bir sabah Pepee parkta bahçe oyunu oynuyordu. Elinde küçük, kırmızı bir kova vardı. Kaydırağın yanındaki ayçiçeği yere doğru eğilmişti, çünkü toprağı çok kuruydu. Pepee çiçeğe hemen su vermek istedi. Parkta çeşmeyi aradı ve onu salıncakların arkasında buldu. Kovasını doldurdu ve çiçeğe geri koştu. Suyu dikkatle toprağa döktü. Sonra çiçeğin yanına oturdu ve bekledi. Biraz sonra ayçiçeği yavaş yavaş doğruldu. Pepee böylece kuru toprağa su vermek gerektiğini öğrendi. Pepee çok sevindi, çünkü ayçiçeği artık dik duruyordu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Parkta çeşmeyi aradı ve onu salıncakların arkasında buldu"
   - Cümle 5: «Parkta çeşmeyi aradı ve onu salıncakların arkasında buldu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada parkta yalnız dolaşıp deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0043` birebir aynı, `@degisim: sulu -> kuru` (tutuyorsan), ardından `@onarim: e9c62f111e2e0587c5f99c21b4d6972ce09eb824`, sonra gövde.

### Hikâye 2: tohum pepee-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0044
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'çikolata', fiil 'kaldırmak', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: yağmur başladı ve kulenin tepesi dağıldı | kovasını kulenin üstüne kapatıp yağmurun dinmesini bekledi
@tohum: pepee-0044
@degisim: çikolata -> kova
Pepee deniz kıyısında, sudan uzakta yapışkan kumdan bir kule yapıyordu. Birden yağmur başladı. Damlalar kulenin tepesine düştü ve tepe yavaş yavaş dağıldı. Pepee kulesini yağmurdan korumak istedi. Kovayı kaldırdı ve kulenin üstüne ters kapattı. Artık damlalar kovanın üstüne düşüyordu. Pepee kovanın yanına çömeldi ve bekledi. Yağmur kısa sürdü ve biraz sonra dindi. Pepee kovayı yavaşça çekti. Kule yerinde sağlam duruyordu ve daha fazla dağılmamıştı. Pepee çok sevindi, çünkü kovayla kulesini korumayı öğrenmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzakta yapışkan kumdan bir"
   - Cümle 1: «Pepee deniz kıyısında, sudan uzakta yapışkan kumdan bir kule yapıyordu.»
   - Açıklama: Kum yapışkan olmaz; kule yapılan kum için 'ıslak kum' denmeli.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kovayı kaldırdı ve kulenin üstüne ters kapattı"
   - Cümle 5: «Kovayı kaldırdı ve kulenin üstüne ters kapattı.»
   - Açıklama: Kova hikayede önceden kurulmadan çözümü getirmek için birden beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0044` birebir aynı, `@degisim: çikolata -> kova` (tutuyorsan), ardından `@onarim: 1cb26bcdaba4623fa49b111a66c3457e7d993e2d`, sonra gövde.

### Hikâye 3: tohum pepee-0045 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Bebee
@tohum: pepee-0045
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kamera', fiil 'asmak', sıfat 'oynak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Bebee
@plan: kağıt zincir öbür sandalyeye yetmedi | üç halka daha yapıp zinciri uzattı
@tohum: pepee-0045
@degisim: kamera -> kağıt
Yağmur cama tık tık vuruyordu. Pepee odasında kardeşi Bebee için kağıttan renkli bir zincir yapmıştı. Zinciri iki sandalyenin arasına asmak istedi ama zincir öbür sandalyeye yetmedi. Pepee masadaki kağıtlara baktı. Halka yapmayı yeni öğrenmişti. Hemen üç halka daha yaptı ve zincire ekledi. Şimdi zincir iki sandalyeye de yetti. Pepee zinciri astı ve Bebee'yi çağırdı. Bebee oynak adımlarla odaya geldi. "Bu zincir benim için mi?" diye sordu Bebee. "Evet, Bebee, senin için yaptım," dedi Pepee. "Çok güzel olmuş, teşekkür ederim, Pepee!" dedi Bebee.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Halka yapmayı yeni öğrenmişti"
   - Cümle 5: «Halka yapmayı yeni öğrenmişti.»
   - Açıklama: Kartın 'yeni şeyler öğrenmeyi ve denemeyi sever' özelliği işe yarar biçimde kullanılmıyor, yalnız geçmişe dair bir not olarak eklenmiş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bebee oynak adımlarla odaya"
   - Cümle 9: «Bebee oynak adımlarla odaya geldi.»
   - Açıklama: 'Oynak' adım için yanlış anlamda kullanılmış; 'paytak' ya da 'küçük' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bebee oynak adımlarla odaya"
   - Cümle 9: «Bebee oynak adımlarla odaya geldi.»
   - Açıklama: 'Oynak adımlar' alışılmadık ve çocuğun bilmeyeceği bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0045` birebir aynı, `@degisim: kamera -> kağıt` (tutuyorsan), ardından `@onarim: 345e77dad77cf85a2892a00fae5184716f87bebc`, sonra gövde.

### Hikâye 4: tohum pepee-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0046
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: sırayla oynamak
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bilet', fiil 'sığınmak', sıfat 'pahalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: tek düdük vardı ve ikisi de onu çalmak istedi | düdüğü sırayla çalmayı önerdi
@tohum: pepee-0046
@degisim: sığınmak -> beklemek
Mutfakta Pepee ile Annee tren oyunu oynuyordu. Sandalyeler trenin vagonları olmuştu. Ama tek bir düdük vardı ve ikisi de onu çalmak istiyordu. Pepee masadaki yumurtaya baktı ve biraz düşündü. "Anneciğim, önce sen çal, ben kahvaltı yapayım, sonra ben çalarım," dedi Pepee. "Olur," dedi Annee ve düdüğü çaldı. Pepee sandalyeye oturdu ve annesine kağıttan biletini gösterdi. "Bu pahalı bir bilet, iyi yolculuklar!" dedi Annee. Pepee yumurtasını yedi ve bekledi. Sonra düdük Pepee'ye geçti ve bu kez o çaldı. Pepee çok mutluydu, çünkü sırayla oynadıkları için ikisi de düdüğü çalmıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "annesine kağıttan biletini gösterdi"
   - Cümle 7: «Pepee sandalyeye oturdu ve annesine kağıttan biletini gösterdi.»
   - Açıklama: Bilet ve pahalı bilet konuşması sebepsiz beliriyor ve sorunun çözümüne hiçbir katkısı yok.
   - Açıklama: Bilet sebepsiz beliriyor ve düdük sorununun çözümünde hiçbir işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu pahalı bir bilet"
   - Cümle 8: «"Bu pahalı bir bilet, iyi yolculuklar!" dedi Annee.»
   - Açıklama: 'Pahalı' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0046` birebir aynı, `@degisim: sığınmak -> beklemek` (tutuyorsan), ardından `@onarim: 4fe70dd809f79697ea75958c69874cd8e7ce40ba`, sonra gövde.

### Hikâye 5: tohum pepee-0049 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0049
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'buzdolabı', fiil 'ödemek', sıfat 'çikolatalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: oyuncak para dolabın altına yuvarlandı | süpürgeyle parayı çekti ve bisküvi için ödedi
@tohum: pepee-0049
@degisim: buzdolabı -> dolap
Pepee mutfakta komik bir market oyunu oynuyordu. Çikolatalı bisküvi almak için üç oyuncak para sayıyordu. Ama bir para yere düştü ve dolabın altına yuvarlandı. Pepee yere eğildi ama paraya uzanamadı. Pepee biraz düşündü. Sonra kapının yanındaki süpürgeyi getirdi. Süpürgeyi dolabın altına yavaşça uzattı. Onu kendine doğru çekti ve para dışarı çıktı. Pepee parayı aldı ve paraları yeniden saydı: bir, iki, üç! Para saymayı yeni öğrenmişti ve hiç yanlış yapmadı. Sonra bisküvi için üç parayı kasaya koydu ve parasını ödedi. Pepee çikolatalı bisküviyi aldı ve market oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "komik bir market oyunu"
   - Cümle 1: «Pepee mutfakta komik bir market oyunu oynuyordu.»
   - Açıklama: 'Komik' kelimesi oyun için doğru anlamda kullanılmamış; 'eğlenceli' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu kendine doğru çekti"
   - Cümle 8: «Onu kendine doğru çekti ve para dışarı çıktı.»
   - Açıklama: 'Onu' zamirinin süpürgeyi mi parayı mı gösterdiği belirsiz.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Para saymayı yeni öğrenmişti"
   - Cümle 10: «Para saymayı yeni öğrenmişti ve hiç yanlış yapmadı.»
   - Açıklama: Tohumdaki öğrenme özelliği arka plan bilgisi olarak anılıyor, çözüm süpürgeyle geliyor ve özellik işe yaramıyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kasaya koydu ve parasını ödedi"
   - Cümle 11: «Sonra bisküvi için üç parayı kasaya koydu ve parasını ödedi.»
   - Açıklama: Parayı kasaya koymak zaten ödemek olduğu için 'parasını ödedi' gereksiz tekrar.
   - Açıklama: Parayı kasaya koymak zaten ödemek; aynı eylem gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0049` birebir aynı, `@degisim: buzdolabı -> dolap` (tutuyorsan), ardından `@onarim: 32476ab3ab616168cdb0e6cc96fbc8f94a1f872f`, sonra gövde.

### Hikâye 6: tohum pepee-0050 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0050
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'televizyon', fiil 'işaretlemek', sıfat 'serin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: yakından ince bir ıslık sesi geliyordu | sesi duyduğu yerleri işaretledi ve boş şişeyi buldu
@tohum: pepee-0050
@degisim: televizyon -> şişe
Serin bir rüzgar esiyordu. Pepee deniz kıyısında, sudan uzakta kumdan bir yol yapıyordu. Birden yakından ince bir ıslık sesi geldi. Pepee sesin nereden geldiğini çok merak etti. Bir dal aldı ve sesi duyduğu her yeri kuma işaretledi. Çizgilerin hepsi büyük bir taşın yanındaydı. Kahvaltıda Pepee boş pekmez şişesine üfleyince de böyle bir ses çıkardı. Bu yüzden taşın arkasında bir şişe aradı. Orada boş bir şişe yatıyordu. Rüzgar şişenin ağzından geçince o ses çıkıyordu. Pepee çok sevindi, çünkü sesi yapan şeyi kendisi bulmuştu.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "her yeri kuma işaretledi"
   - Cümle 5: «Bir dal aldı ve sesi duyduğu her yeri kuma işaretledi.»
   - Açıklama: 'Her yeri kuma işaretledi' bozuk; 'kumda işaretledi' ya da 'kuma çizgi çizdi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi duyduğu her yeri kuma işaretledi"
   - Cümle 5: «Bir dal aldı ve sesi duyduğu her yeri kuma işaretledi.»
   - Açıklama: Sesi duyduğu yerler kuma işaretlenemez; kelimeler anlamca uyuşmuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sesi duyduğu her yeri kuma işaretledi"
   - Cümle 5: «Bir dal aldı ve sesi duyduğu her yeri kuma işaretledi.»
   - Açıklama: Kıyıda yol yapan Pepee'nin sesi duyduğu yerleri kuma işaretlemesi sesin kaynağını bulmaya akla yatkın biçimde yönelmiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sesi duyduğu her yeri kuma işaretledi"
   - Cümle 5: «Bir dal aldı ve sesi duyduğu her yeri kuma işaretledi.»
   - Açıklama: Sesi duyduğu yerleri işaretlemek sesin kaynağını bulmaya akla yatkın biçimde götürmüyor; işaretlerin taşı göstermesi sebepsiz.
5. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "üfleyince de böyle bir ses çıkardı"
   - Cümle 7: «Kahvaltıda Pepee boş pekmez şişesine üfleyince de böyle bir ses çıkardı.»
   - Açıklama: Kahvaltıdaki önceki olay -mişti ile anlatılmalı ('çıkarmıştı'), zaman kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0050` birebir aynı, `@degisim: televizyon -> şişe` (tutuyorsan), ardından `@onarim: 12b3f71caea85e35c13e04bbe4990d7c09573b0b`, sonra gövde.

### Hikâye 7: tohum pepee-0052 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0052
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'fide', fiil 'dalgalanmak', sıfat 'beyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: rüzgar esince ince ağaç hep yana eğiliyordu | ağacı kurdeleyle bir dala bağladı
@tohum: pepee-0052
@degisim: fide -> ağaç
Serin bir rüzgar esiyordu. Pepee ile Annee ormanda beyaz çiçekli küçük bir ağaç dikmişti. Ama rüzgar esince ince ağaç hep yana eğiliyordu. Pepee bu yeni ağaç için dansla bir kutlama yapmak istiyordu. Pepee yerden düz ve sağlam bir dal buldu. Dalı ağacın yanında toprağa soktu. "Anneciğim, çantada ip var mı?" diye sordu Pepee. Annee çantasından uzun bir kurdele çıkardı. Pepee ağacı kurdeleyle dala yavaşça bağladı. Rüzgar yine esti ama ağaç artık dik duruyordu. Kurdele rüzgarda dalgalandı. Sonra Pepee ağacın etrafında kutlama dansını yaptı. Annee de gülerek ellerini çırptı. Pepee çok mutluydu, çünkü küçük ağaç artık hiç eğilmiyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee bu yeni ağaç için dansla bir kutlama yapmak istiyordu"
   - Cümle 4: «Pepee bu yeni ağaç için dansla bir kutlama yapmak istiyordu.»
   - Açıklama: Tohumdaki dans özelliği iki kez geçiyor ve sorunun çözümüne hiç katkı vermiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dansla bir kutlama yapmak"
   - Cümle 4: «Pepee bu yeni ağaç için dansla bir kutlama yapmak istiyordu.»
   - Açıklama: Tohumdaki dans özelliği iki kez geçiyor ve sorunun çözümünde işe yaramıyor, yalnız süs olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0052` birebir aynı, `@degisim: fide -> ağaç` (tutuyorsan), ardından `@onarim: de0bfc919cb3401c6345d124b6aaf4b643f8916b`, sonra gövde.

### Hikâye 8: tohum pepee-0053 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0053
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'duvar', fiil 'takılmak', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: rüzgar esti ve kurdele yüksek bir dala takıldı | ninesinden yardım istedi ve kurdelesini geri aldı
@tohum: pepee-0053
@degisim: duvar -> dal
Ormanda Pepee ile Nenee çiçeklerin arasında oynuyordu. Pepee uzun, mavi bir kurdeleyle dans ediyordu. Birden rüzgar esti ve kurdele bir dala takıldı. Dal, Pepee'nin başının çok üstündeydi. Pepee zıpladı ama kurdeleye yetişemedi. "Nineciğim, kurdeleyi alır mısın?" diye sordu Pepee. Nenee güldü ve parmaklarının ucunda yükseldi. Kurdeleyi daldan yavaş yavaş çekti. Kurdele Pepee'nin eline düştü. "Teşekkürler, nineciğim!" dedi Pepee. "Bu kez kurdeleyi sıkıca tut," dedi Nenee. Pepee ile Nenee kurdeleyi birlikte tuttu ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "mavi bir kurdeleyle dans ediyordu"
   - Cümle 2: «Pepee uzun, mavi bir kurdeleyle dans ediyordu.»
   - Açıklama: Tohumdaki dans özelliği yalnız sahne olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0053` birebir aynı, `@degisim: duvar -> dal` (tutuyorsan), ardından `@onarim: 307540f63d32c7b5c99656cdf43e96bb7ae4b261`, sonra gövde.

### Hikâye 9: tohum pepee-0054 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0054
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: paylaşmak
- yan: Dedee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'tuz', fiil 'döndürmek', sıfat 'konuşkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: dede de oynamak istedi ama tek çember vardı | çemberi dedesiyle paylaştı ve dansla döndürmeyi gösterdi
@tohum: pepee-0054
@degisim: tuz -> çember
Bir sabah Pepee ile konuşkan dedesi kumda oynuyordu. Pepee'nin elinde kırmızı bir çember vardı. Dedee de çemberle oynamak istedi ama başka çember yoktu. "Pepee, ben de çemberini çevirebilir miyim?" diye sordu Dedee. "Tabii, dedeciğim, önce sana göstereyim," dedi Pepee. Pepee çemberi beline geçirdi ve dans ederek döndürdü. Sonra onu dedesine verdi. Dedee de belini salladı ve çemberi döndürdü. Çember hiç düşmeden dönüyordu. İkisi sırayla oynadı ve çok güldü. "Pepee, çemberini benimle paylaştığın için teşekkür ederim!" dedi Dedee.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Pepee ile konuşkan dedesi"
   - Cümle 1: «Bir sabah Pepee ile konuşkan dedesi kumda oynuyordu.»
   - Açıklama: Kartın ilişki alanı Dedee'yi hareketli bir oyun arkadaşı olarak tanımlar; konuşkan huyu kartta yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0054` birebir aynı, `@degisim: tuz -> çember` (tutuyorsan), ardından `@onarim: bd17a25060993c6185a0e21afcff85b477f6575b`, sonra gövde.

### Hikâye 10: tohum pepee-0055 (deneme 1 -> 2)

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
Bir sabah Pepee ile kuzeni Şila kumda deniz kabuğu topluyordu. Birden Şila durdu, çünkü pembe mercan parçası kaybolmuştu. "Mercan parçasını kumda bir yere bıraktım ama yerini unuttum," dedi Şila. Pepee, Şila'nın kumdaki küçük ayak izlerini gördü. Pepee bu izleri adım adım takip etti. Bunu yapmayı yeni öğrenmişti. İzler onları kıyıdan biraz uzak bir yere götürdü. Orada kumun içinde pembe bir uç vardı. Pepee kumu elleriyle açtı ve mercan parçasını buldu. "İşte mercan, Şila!" dedi Pepee. Şila onu aldı ve Pepee'ye sarıldı. Sonra ikisi kabuk toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bunu yapmayı yeni öğrenmişti"
   - Cümle 6: «Bunu yapmayı yeni öğrenmişti.»
   - Açıklama: Kartın 'yeni şeyler öğrenmeyi ve denemeyi sever' özelliği işe yarar biçimde kullanılmıyor, yalnız geçmişe dair bir not olarak eklenmiş.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "onları kıyıdan biraz uzak bir yere"
   - Cümle 7: «İzler onları kıyıdan biraz uzak bir yere götürdü.»
   - Açıklama: Deniz tarifi herkesin kumda ve su kenarında kaldığını söylüyor, kıyıdan uzaklaşmak bu tarife aykırı olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0055` birebir aynı, `@degisim: beslemek -> bırakmak` (tutuyorsan), ardından `@onarim: 98b4d831017f131366818f7ddcfaf4975d53e393`, sonra gövde.

### Hikâye 11: tohum pepee-0056 (deneme 1 -> 2)

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
@plan: kuru kumdan yapılan vazo hemen dağıldı | su kenarındaki ıslak kumla vazoyu yeniden yaptı
@tohum: pepee-0056
@degisim: reçelli -> ıslak
Bir sabah Pepee deniz kıyısında kumla oynuyordu. Kumdan bir vazo yapmayı yeni öğrenmişti. Ama kum çok kuruydu ve vazo hemen dağıldı. Pepee biraz düşündü. Su kenarındaki kum koyu renkliydi ve birbirine yapışıyordu. Pepee kovasını oradan ıslak kumla doldurdu. Kumu elleriyle sıkıca bastırdı ve uzun bir vazo yaptı. Sonra ortasını parmağıyla açtı. Bu kez vazo hiç dağılmadı. Pepee vazonun içine iki uzun deniz kabuğu koydu. Kabuklar vazoda çiçek gibi duruyordu. Pepee çok sevindi, çünkü vazosu artık yıkılmıyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kumdan bir vazo yapmayı yeni öğrenmişti"
   - Cümle 2: «Kumdan bir vazo yapmayı yeni öğrenmişti.»
   - Açıklama: Öğrenme özelliği yalnız geçmiş bilgi olarak anılıyor, çözümde işe yarar biçimde kullanılmıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kovasını oradan ıslak kumla doldurdu"
   - Cümle 6: «Pepee kovasını oradan ıslak kumla doldurdu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada su kenarında büyüksüz yalnız oynuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0056` birebir aynı, `@degisim: reçelli -> ıslak` (tutuyorsan), ardından `@onarim: 52bf66c96410d8d2d0f25c397d9f588bc7177b69`, sonra gövde.

### Hikâye 12: tohum pepee-0057 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kumun içinde parlak bir şey gördü | üstüne su serpti ve bir inci buldu
@tohum: pepee-0057
@degisim: yardımsever -> parlak
Pepee deniz kıyısında kumda yürüyordu. Birden kumun içinde parlak bir şey gördü. Pepee bunun ne olduğunu çok merak etti. Ama o şeyin çoğu kumun altındaydı. Pepee su kenarına gitti ve avucuna biraz su aldı. Suyu o şeyin üstüne yavaşça serpti. Kum aktı ve açık bir deniz kabuğu göründü. Kabuğun içinde küçük, beyaz bir inci vardı! Pepee ilk kez gerçek bir inci görüyordu. İnciyi kabuğuyla birlikte dikkatle avucuna aldı. Uzun uzun baktı ve çok sevindi. Pepee o sabah kabukların içinde inci olabileceğini öğrendi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kumun içinde parlak bir şey gördü"
   - Cümle 2: «Birden kumun içinde parlak bir şey gördü.»
   - Açıklama: Parlak bir şey görmek gerçek bir sorun değil, yalnız bir merak; hikayede aşılması gereken bir güçlük kurulmuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee su kenarına gitti"
   - Cümle 5: «Pepee su kenarına gitti ve avucuna biraz su aldı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada dört yaşındaki Pepee su kenarında yalnız deniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Suyu o şeyin üstüne yavaşça serpti"
   - Cümle 6: «Suyu o şeyin üstüne yavaşça serpti.»
   - Açıklama: Kumun altındaki şeyi ortaya çıkarmak için bir avuç su serpmek sebebe doğrudan yönelmiyor; kazmak yerine dolaylı ve inandırıcı olmayan bir yol seçiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0057` birebir aynı, `@degisim: yardımsever -> parlak` (tutuyorsan), ardından `@onarim: adaebd2979f28b0dfb1a5c08bf264f58e1d0bc35`, sonra gövde.
