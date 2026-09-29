# Editör görevi (onarım): Pepee, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0035 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0035
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'krem', fiil 'uzamak', sıfat 'sabunlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: baloncuk uçurmak istedi ama halka evde kalmıştı | otu yuvarlak bal kabına sardı ve halka yaptı
@tohum: pepee-0035
@degisim: krem -> halka
Bir sabah Pepee ile Bebee ormanda kahvaltı yapıyordu. "Bak, Pepee, boyum uzadı, çiçekli dala dokunabiliyorum!" dedi Bebee. Pepee bunu baloncukla kutlamak istedi, ama halka evde kalmıştı. Çantada yalnız bir şişe sabunlu su vardı. Pepee yerde ince ve uzun bir ot buldu. Otu kahvaltıdaki yuvarlak bal kabına sardı. Böylece küçük bir halka yaptı. Halkayı suya batırdı ve yavaşça üfledi. Ağaçların arasına bir sürü baloncuk uçtu. Bebee onların arkasından koştu ve ellerini çırptı. "Bunlar senin için, Bebee!" dedi Pepee. Sonra ikisi sırayla baloncuk uçurdu ve mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Otu kahvaltıdaki yuvarlak bal kabına sardı"
   - Cümle 6: «Otu kahvaltıdaki yuvarlak bal kabına sardı.»
   - Açıklama: Tohumdaki kahvaltı sevgisi özelliği iki kez geçiyor ve yalnız sahne/eşya kaynağı olarak kalıyor, sorunu çözen özellik olarak kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0035` birebir aynı, `@degisim: krem -> halka` (tutuyorsan), ardından `@onarim: 04312a18c3cfba849c2c1e0320fff7c9c0af9c22`, sonra gövde.

### Hikâye 2: tohum pepee-0036 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0036
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Nenee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'çekmece', fiil 'yapıştırmak', sıfat 'akıllı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: koşarken ninesinin kumdan pastasına bastı | özür diledi ve kabukları yeniden yapıştırdı
@tohum: pepee-0036
@degisim: çekmece -> kabuk
Pepee deniz kıyısında hızlı hızlı koşuyordu. Koşarken Nenee'nin kumdan yaptığı pastaya bastı. Pasta dağıldı ve üstündeki deniz kabukları kuma saçıldı. Nenee buna çok üzüldü. Pepee durdu ve hemen ninesinden özür diledi. Sonra pastayı Nenee ile birlikte yeniden yaptı. Beyaz kabukları ıslak kumla pastanın üstüne yapıştırdı. En üste de kumdan bir yumurta koydu, çünkü kahvaltıda yumurtayı çok severdi. Nenee kumdan yumurtayı görünce kahkaha attı. Sonra Pepee'ye sarıldı ve onun akıllı bir çocuk olduğunu söyledi. Pepee çok sevindi, çünkü ninesi artık üzgün değildi ve pasta yine güzeldi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "En üste de kumdan bir yumurta koydu"
   - Cümle 8: «En üste de kumdan bir yumurta koydu, çünkü kahvaltıda yumurtayı çok severdi.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunu çözmüyor, yalnız süs olarak ekleniyor; çözüm özür ve kabukları yapıştırmakla geliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "görünce kahkaha attı"
   - Cümle 9: «Nenee kumdan yumurtayı görünce kahkaha attı.»
   - Açıklama: 'Kahkaha atmak' deyimsel bir kalıp; 3 yaşındaki çocuk için 'yüksek sesle güldü' daha uygun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0036` birebir aynı, `@degisim: çekmece -> kabuk` (tutuyorsan), ardından `@onarim: 6a4f51d6dd8e102d25ff7d7140d036b8cd5c95a4`, sonra gövde.

### Hikâye 3: tohum pepee-0040 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0040
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kolye', fiil 'dinlemek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yumurta yuvarlak olduğu için kaşıktan düştü | peçeteyi katlayıp kaşığın içine koydu
@tohum: pepee-0040
@degisim: kolye -> peçete
Bir sabah Pepee ormanda kuşları dinleyerek kahvaltı yapıyordu. Sonra sıcacık yumurtasını kaşığa koydu ve ağaca kadar taşımak istedi. Ama yumurta yuvarlaktı ve ilk adımda yumuşak otların üstüne düştü. Pepee bir kez daha denedi, ama yumurta yine düştü. Pepee kahvaltı sofrasına baktı ve peçetesini gördü. Peçeteyi katladı ve kaşığın içine koydu. Yumurtayı peçetenin üstüne yerleştirdi. Yumurta peçetenin üstünde güzelce durdu. Pepee yavaş adımlarla büyük ağaca kadar yürüdü. Yumurta bir kez bile düşmedi. Pepee sevinçle zıpladı ve oyunu mutlu mutlu bir kez daha oynadı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "oyunu mutlu mutlu bir"
   - Cümle 11: «Pepee sevinçle zıpladı ve oyunu mutlu mutlu bir kez daha oynadı.»
   - Açıklama: Daha önce bir oyun tanıtılmadığı için 'oyunu' kelimesinin neyi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "oyunu mutlu mutlu bir kez daha oynadı"
   - Cümle 11: «Pepee sevinçle zıpladı ve oyunu mutlu mutlu bir kez daha oynadı.»
   - Açıklama: 'Oyunu' hangi oyunu gösterdiği belli değil; hikayede oyun tanıtılmadı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0040` birebir aynı, `@degisim: kolye -> peçete` (tutuyorsan), ardından `@onarim: 45262d7dca0e58a8e053a36b46eeead70559d2b9`, sonra gövde.

### Hikâye 4: tohum pepee-0043 (deneme 5 -> 6)

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
Bir sabah Pepee parkta bahçe oyunu oynuyordu. Elinde küçük, kırmızı bir kova vardı. Kaydırağın yanındaki ayçiçeği yere doğru eğilmişti, çünkü toprağı çok kuruydu. Pepee çiçeğe hemen su vermek istedi. Gözleriyle çeşmeyi aradı ve onu kaydırağın yanında gördü. Kovasını doldurdu ve çiçeğe geri yürüdü. Suyu dikkatle toprağa döktü. Sonra çiçeğin yanına oturdu ve bekledi. Biraz sonra ayçiçeği yavaş yavaş doğruldu. Pepee böylece kuru toprağa su vermek gerektiğini öğrendi. Pepee çok sevindi, çünkü ayçiçeği artık dik duruyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parkta bahçe oyunu oynuyordu"
   - Cümle 1: «Bir sabah Pepee parkta bahçe oyunu oynuyordu.»
   - Açıklama: 'Bahçe oyunu' belirsiz ve parkta geçen olaya uymayan bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0043` birebir aynı, `@degisim: sulu -> kuru` (tutuyorsan), ardından `@onarim: 8288dfada2255e64a26e544b9a6493a63eab6741`, sonra gövde.

### Hikâye 5: tohum pepee-0044 (deneme 4 -> 5)

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
Pepee deniz kıyısında, sudan uzakta kovasıyla ıslak kumdan bir kule yapıyordu. Islak kum yapışkandı ve kule dimdik duruyordu. Birden yağmur başladı. Damlalar kulenin tepesine düştü ve tepe yavaş yavaş dağıldı. Pepee kulesini yağmurdan korumak istedi. Kovayı kaldırdı ve kulenin üstüne ters kapattı. Artık damlalar kovanın üstüne düşüyordu. Pepee kovanın yanına çömeldi ve bekledi. Yağmur kısa sürdü ve biraz sonra dindi. Pepee kovayı yavaşça çekti. Kule yerinde sağlam duruyordu ve daha fazla dağılmamıştı. Pepee çok sevindi, çünkü kovayla kulesini korumayı öğrenmişti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Damlalar kulenin tepesine düştü ve tepe yavaş yavaş dağıldı"
   - Cümle 4: «Damlalar kulenin tepesine düştü ve tepe yavaş yavaş dağıldı.»
   - Açıklama: Kulenin dağılması sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0044` birebir aynı, `@degisim: çikolata -> kova` (tutuyorsan), ardından `@onarim: 65d08d7e9952311b3293a205f06b3461585e3531`, sonra gövde.

### Hikâye 6: tohum pepee-0045 (deneme 4 -> 5)

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
Yağmur cama tık tık vuruyordu. Pepee odasında kardeşi Bebee için kağıttan renkli bir zincir yapmıştı. Zinciri iki sandalyenin arasına asmak istedi ama zincir öbür sandalyeye yetmedi. Pepee masadaki kağıtlara baktı. Kağıttan halka yapmayı yeni öğrenmişti. Hemen üç halka daha yaptı ve zincire ekledi. Şimdi zincir iki sandalyeye de yetti. Pepee zinciri astı ve Bebee'yi çağırdı. Bebee odaya geldi ve zincirin altında oynak bir dans yaptı. "Bu zincir benim için mi?" diye sordu Bebee. "Evet, Bebee, senin için yaptım," dedi Pepee. "Çok güzel olmuş, teşekkür ederim, Pepee!" dedi Bebee.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kağıt zincir öbür sandalyeye"
   - Cümle 0 (plan satırı): «kağıt zincir öbür sandalyeye yetmedi | üç halka daha yapıp zinciri uzattı»
   - Açıklama: Tamlama eki eksik; 'kağıt zinciri' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kağıt zincir öbür sandalyeye yetmedi"
   - Cümle 0 (plan satırı): «kağıt zincir öbür sandalyeye yetmedi | üç halka daha yapıp zinciri uzattı»
   - Açıklama: 'Yetmek' burada yanlış anlamda; zincir sandalyeye 'uzanmadı/ulaşmadı' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "zincir öbür sandalyeye yetmedi"
   - Cümle 3: «Zinciri iki sandalyenin arasına asmak istedi ama zincir öbür sandalyeye yetmedi.»
   - Açıklama: 'Yetmek' burada yanlış anlamda; zincir öbür sandalyeye 'uzanmadı' ya da 'yetişmedi' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "zincir iki sandalyeye de yetti"
   - Cümle 7: «Şimdi zincir iki sandalyeye de yetti.»
   - Açıklama: 'Yetmek' ulaşmak anlamında yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0045` birebir aynı, `@degisim: kamera -> kağıt` (tutuyorsan), ardından `@onarim: f6aaf052ec6dd4e58c401f1e222b1d7cb44f3449`, sonra gövde.

### Hikâye 7: tohum pepee-0053 (deneme 4 -> 5)

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
Ormanda Pepee ile Nenee çiçeklerin arasında oynuyordu. Pepee ninesine mavi bir kurdeleyle yeni bir dans göstermek istiyordu. Birden rüzgar esti ve kurdele bir dala takıldı. Dal, Pepee'nin başının çok üstündeydi. Pepee zıpladı ama kurdeleye yetişemedi. "Nineciğim, kurdeleyi alır mısın?" diye sordu Pepee. Nenee güldü ve kolunu dala uzattı. Kurdeleyi daldan yavaş yavaş çekti. Kurdele Pepee'nin eline düştü. "Teşekkürler, nineciğim!" dedi Pepee. "Bu kez kurdeleyi sıkıca tut," dedi Nenee. Pepee kurdeleyi iki eliyle tuttu ve ninesine dansını gösterdi. Nenee ellerini çırptı ve ikisi mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni bir dans göstermek"
   - Cümle 2: «Pepee ninesine mavi bir kurdeleyle yeni bir dans göstermek istiyordu.»
   - Açıklama: Tohumdaki dans özelliği iki kez geçiyor ve sorunun çözümünde işe yaramıyor; kurdeleyi nine alıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0053` birebir aynı, `@degisim: duvar -> dal` (tutuyorsan), ardından `@onarim: a6cc58af5e18a40d697655139e2532be3821c571`, sonra gövde.

### Hikâye 8: tohum pepee-0055 (deneme 3 -> 4)

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
Bir sabah Pepee ile kuzeni Şila kumda, sudan uzakta deniz kabuğu topluyordu. Birden Şila durdu, çünkü pembe mercan parçası kaybolmuştu. "Mercan parçasını kumda bir yere bıraktım ama yerini unuttum," dedi Şila. Pepee, Şila'nın kumdaki küçük ayak izlerini gördü. Pepee daha önce hiç iz takip etmemişti ve bunu öğrenmek istedi. Bu izleri adım adım takip etti. İzler biraz ileride bitti. Orada kumun içinde pembe bir uç vardı. Pepee kumu elleriyle açtı ve mercan parçasını buldu. "İşte mercan, Şila!" dedi Pepee. Şila onu aldı ve Pepee'ye sarıldı. Sonra ikisi kabuk toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İzler biraz ileride bitti"
   - Cümle 7: «İzler biraz ileride bitti.»
   - Açıklama: Şila oradan yürüyüp döndüğü halde izlerin tam mercanın yanında sebepsizce bitmesi çözümü kolayca getiriyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İzler biraz ileride bitti"
   - Cümle 7: «İzler biraz ileride bitti.»
   - Açıklama: Şila izlerin bittiği yerden şimdi bulunduğu yere yürüdüğüne göre izlerin orada bitmesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0055` birebir aynı, `@degisim: beslemek -> bırakmak` (tutuyorsan), ardından `@onarim: 0d623fa7fdc26a68ec45f423926710d5772bde50`, sonra gövde.

### Hikâye 9: tohum pepee-0057 (deneme 3 -> 4)

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
@plan: pastaya koyacak parlak bir süs yoktu | kumu elinden serpti ve kabuktaki inciyi buldu
@tohum: pepee-0057
@degisim: yardımsever -> parlak
Pepee deniz kıyısında, sudan uzakta kumdan bir pasta yapıyordu. Pastanın tepesine parlak bir süs koymak istiyordu. Ama etrafta yalnız gri taşlar vardı. Pepee süs bulmak için eline biraz kum aldı. Kumu yavaşça yere serpti ve elinde küçük bir kabuk kaldı. Kabukta beyaz bir şey parlıyordu. Pepee bunun ne olduğunu çok merak etti. Kabuğun içine dikkatle baktı. Orada küçük, beyaz bir inci vardı! Pepee ilk kez gerçek bir inci görüyordu. İnciyi pastanın tepesine yavaşça koydu. Pasta artık çok güzel olmuştu. Pepee o sabah kabukların içinde inci olabileceğini öğrendi.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee süs bulmak için eline biraz kum aldı"
   - Cümle 4: «Pepee süs bulmak için eline biraz kum aldı.»
   - Açıklama: Kum avuçlamak süs bulmaya doğrudan yönelen bir çözüm değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumu yavaşça yere serpti ve elinde küçük bir kabuk kaldı"
   - Cümle 5: «Kumu yavaşça yere serpti ve elinde küçük bir kabuk kaldı.»
   - Açıklama: İncili kabuk tesadüfen, sebepsizce çıkıp çözümü getiriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kabukta beyaz bir şey parlıyordu"
   - Cümle 6: «Kabukta beyaz bir şey parlıyordu.»
   - Açıklama: Kumdaki kabukta inci bulunması tesadüf; çözüm sebepsizce geliyor.
   - Açıklama: İnci şans eseri ve sebepsizce beliriyor, çözümü tesadüf getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0057` birebir aynı, `@degisim: yardımsever -> parlak` (tutuyorsan), ardından `@onarim: ead030c085b1eca0d135dd45fd0ff3ed3a9e77e1`, sonra gövde.

### Hikâye 10: tohum pepee-0062 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: yakından garip bir ses duyuldu | dikkatle dinledi ve sesin karnından geldiğini buldu
@tohum: pepee-0062
Ormanda hava serindi. Pepee çantasıyla ağaçların arasında yürüyordu. Birden yakından garip bir ses duyuldu. Pepee bu sesi çok merak etti. Önce çalıların arkasına baktı ama orada bir şey yoktu. Sonra sağlam bir kütüğe oturdu ve dikkatle dinledi. Ses bu kez daha yakındı. Pepee elini karnına koydu. Ses onun karnından geliyordu! Pepee daha kahvaltı yapmamıştı ve acıkmıştı. Hemen çantasından ballı ekmeğini ve yumurtasını çıkardı. Ekmekten büyük bir lokma aldı ve yumurtasını da yedi. Karnından artık hiç ses gelmedi. Pepee kahvaltısını bitirince kütükten kalktı. Pepee çok sevindi, çünkü garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce çalıların arkasına baktı"
   - Cümle 5: «Önce çalıların arkasına baktı ama orada bir şey yoktu.»
   - Açıklama: Çözüm çalılara bakma, dinleme, karnına el koyma ve yemek yeme gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0062` birebir aynı, ardından `@onarim: 5258e8572a22e94b5ff7644208f44281cb007085`, sonra gövde.

### Hikâye 11: tohum pepee-0063 (deneme 3 -> 4)

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
@plan: avokado kum tepesinden yuvarlandı ve kayboldu | kumdaki çizgiyi ninesiyle takip edip avokadoyu buldu
@tohum: pepee-0063
@degisim: berrak -> yuvarlak
Bir sabah Pepee ile ninesi deniz kıyısında oturuyordu. Nenee sepetinden yeşil, yuvarlak bir avokado çıkardı. Ama avokado elinden düştü ve küçük bir kum tepesinden aşağı yuvarlandı. "Affet beni, Pepee, onu tutamadım," dedi Nenee. Pepee tepeden aşağı baktı ama avokadoyu göremedi. Sonra kumda ince, uzun bir çizgi gördü. Pepee bunun avokadonun izi olduğunu anladı. Daha önce hiç iz takip etmemişti ve bunu öğrenmek istedi. Ninesinin elini tuttu ve çizgiye bakarak yürüdü. Çizgi büyük bir taşın arkasında bitti. Avokado orada duruyordu! Pepee eğildi ve onu dikkatle aldı. "Nineciğim, bak, buldum!" dedi Pepee. "Teşekkürler, Pepee, hadi onu şimdi yiyelim!" dedi Nenee.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hiç iz takip etmemişti ve bunu öğrenmek istedi"
   - Cümle 8: «Daha önce hiç iz takip etmemişti ve bunu öğrenmek istedi.»
   - Açıklama: 'İz takip etmek' ve bunu öğrenmek istemek 3 yaşındaki çocuk için soyut ve zor bir anlatım.
   - Açıklama: 'İz takip etmeyi öğrenmek istemek' soyut, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0063` birebir aynı, `@degisim: berrak -> yuvarlak` (tutuyorsan), ardından `@onarim: dcb95fbd0d6ad5a0b797e25a3ce7923b27503266`, sonra gövde.

### Hikâye 12: tohum pepee-0067 (deneme 2 -> 3)

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
Küçük dalgalar kıyıda ses çıkarıyordu. Pepee ile Bebee kumda topaç oyunu oynuyordu. Rengarenk bir topaç gibi dönerek ortada birleşmek istiyorlardı. Ama ayakları yumuşak kuma battı. "Pepee, ayaklarım battı!" dedi Bebee. Pepee etrafına baktı. Biraz ileride kum düz ve sertti. "Gel, Bebee, orada dönelim!" dedi Pepee. İkisi hemen oraya yürüdü. Pepee kollarını açtı ve dans ederek döndü. Bebee de ona bakıp kendi yerinde döndü. Ayakları bu kez hiç batmadı. Kardeşler dönerek yaklaştı ve ortada birleşti. İkisi birbirine sarıldı. Pepee ile Bebee gülerek oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Rengarenk bir topaç gibi dönerek"
   - Cümle 3: «Rengarenk bir topaç gibi dönerek ortada birleşmek istiyorlardı.»
   - Açıklama: Benzetme (mecaz) kullanılmış ve 'ortada birleşmek' ifadesi çocuğa soyut kalıyor.
   - Açıklama: Kendini topaca benzetme bir mecaz (benzetme) ve küçük çocuk için kafa karıştırıcı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0067` birebir aynı, ardından `@onarim: 3744e21c434b36fef08b374e7ec3dfd92e6f2bf6`, sonra gövde.
