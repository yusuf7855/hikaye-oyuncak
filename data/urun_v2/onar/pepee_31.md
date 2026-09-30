# Editör görevi (onarım): Pepee, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0135 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0135
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kabuk', fiil 'saymak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: kelebekler hiç durmadığı için sayı karıştı | yumurta kabuğuna bal koydu ve kelebekleri saydı
@tohum: pepee-0135
@degisim: sağlıklı -> güzel
Kuşlar ötüyordu ve Pepee ağacın altında güzel bir kahvaltı yapıyordu. Birden çiçeklerin üstünde uçan kelebekleri gördü ve saymak istedi. Ama kelebekler hiç durmuyordu ve Pepee sayıyı karıştırıyordu. Pepee yumurtanın kabuğundan küçük bir kap yaptı. Kabuğun içine tabağındaki baldan biraz koydu. Sonra onu çiçeklerin arasına bıraktı ve biraz uzağa oturdu. Az sonra balın üstünde kelebekler duruyordu. Pepee onları tek tek saydı. Tam beş tane vardı. Pepee çok sevindi, çünkü sonunda bütün kelebekleri saymıştı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ağacın altında güzel bir kahvaltı yapıyordu"
   - Cümle 1: «Kuşlar ötüyordu ve Pepee ağacın altında güzel bir kahvaltı yapıyordu.»
   - Açıklama: Güvenli özellik kullanımı satırı yeni şeylerin bir büyüğün yanında denendiğini söylüyor, ama Pepee ormanda yalnız başına yeni bir şey deniyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Az sonra balın üstünde kelebekler duruyordu"
   - Cümle 7: «Az sonra balın üstünde kelebekler duruyordu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, balın üstüne konup sorunun çözümüne katılıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "balın üstünde kelebekler duruyordu"
   - Cümle 7: «Az sonra balın üstünde kelebekler duruyordu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, balı konup olayın çözümüne katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0135` birebir aynı, `@degisim: sağlıklı -> güzel` (tutuyorsan), ardından `@onarim: 955333cc70b77e1f597907e594a0097dbbfa1837`, sonra gövde.

### Hikâye 2: tohum pepee-0136 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0136
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: paylaşmak
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bot', fiil 'oturmak', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: annenin tabağı boştu çünkü evde yumurta kalmamıştı | kendi yumurtasını ikiye bölüp annesiyle paylaştı
@tohum: pepee-0136
@degisim: bot -> tabak
Bir sabah Pepee ile Annee mutfakta masaya oturdu. Pepee'nin tabağında bir yumurta vardı. Ama Annee'nin yeşil tabağı boştu, çünkü evde başka yumurta yoktu. Pepee annesinin boş tabağına baktı. Kahvaltısındaki yumurtayı çatalıyla ikiye böldü. Büyük parçayı annesinin tabağına koydu. Sonra bal kavanozunu da ona uzattı. Annee önce çok şaşırdı. Sonra Pepee'ye sarıldı ve onu öptü. İkisi yumurtayı yan yana yedi. Ekmeklerine de bal sürdüler. Annee çok sevindi, çünkü Pepee en sevdiği yumurtayı onunla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bal kavanozunu da ona uzattı"
   - Cümle 7: «Sonra bal kavanozunu da ona uzattı.»
   - Açıklama: Bal ve ekmek sorunla ilgisiz biçimde beliriyor ve çözüme bir şey katmıyor.
   - Açıklama: Bal kavanozu sorunla ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0136` birebir aynı, `@degisim: bot -> tabak` (tutuyorsan), ardından `@onarim: e31f1ab98f571632d6e74b9a8ee4c8d6595bdf3c`, sonra gövde.

### Hikâye 3: tohum pepee-0137 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0137
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'bisiklet', fiil 'hoplamak', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: tek ayakla giderken hep bir yana eğildi | kollarını iki yana açıp yeniden hopladı
@tohum: pepee-0137
@degisim: bisiklet -> taş
Deniz kıyısında nefis bir sabahtı. Pepee kumdaki bir taşa kadar tek ayakla gitmeyi denedi. Ama her seferinde bir yana eğildi ve öbür ayağı kuma değdi. Pepee biraz düşündü. Dans ederken kollarını iki yana açtığını hatırladı. Kollarını yine öyle açtı ve tek ayakla hopladı. Bu kez öbür ayağı kuma hiç değmedi. Pepee küçük küçük zıpladı ve taşa kadar gitti. Pepee kollarını havaya kaldırdı ve güldü. Pepee çok sevindi, çünkü ilk kez tek ayakla oraya varmıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "nefis bir sabahtı"
   - Cümle 1: «Deniz kıyısında nefis bir sabahtı.»
   - Açıklama: 'Nefis' yiyecekler için kullanılır, sabaha uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Deniz kıyısında nefis bir sabahtı"
   - Cümle 1: «Deniz kıyısında nefis bir sabahtı.»
   - Açıklama: 'Nefis' yiyecek için kullanılır, sabaha uymuyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kumdaki bir taşa kadar tek ayakla gitmeyi denedi"
   - Cümle 2: «Pepee kumdaki bir taşa kadar tek ayakla gitmeyi denedi.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada deniz kıyısında yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0137` birebir aynı, `@degisim: bisiklet -> taş` (tutuyorsan), ardından `@onarim: 9d8ff9882d595c21b602ecbc17415c6a36decc8e`, sonra gövde.

### Hikâye 4: tohum pepee-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0138
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mısır', fiil 'örtmek', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kale suya çok yakındı ve dalgalar onu dağıttı | dalgaların nereye geldiğini öğrendi ve kuru kumda kale yaptı
@tohum: pepee-0138
@degisim: mısır -> kova
Deniz kıyısında Şila kovasıyla kumdan bir kale yapıyordu. Pepee de onun yanında deniz kabukları topluyordu. Ama kale suya çok yakındı ve küçük dalgalar dibini dağıttı. Şila üzüldü. Pepee ona yardım etmek istedi. Önce dalgaları dikkatle izledi. Dalgaların yalnız ıslak kuma kadar geldiğini öğrendi. Pepee kovayı kuru kumla doldurdu ve ters çevirdi. Dalgalardan uzakta yeni ve büyük bir kale çıktı. Şila da kalenin tepesini Pepee'nin bir kabuğuyla örttü. Dalgalar yine geldi ama yeni kaleye hiç değmedi. Şila sevinçle ellerini çırptı. Pepee bundan sonra kaleleri hep kuru kumda yaptı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kalenin tepesini Pepee'nin bir kabuğuyla örttü"
   - Cümle 10: «Şila da kalenin tepesini Pepee'nin bir kabuğuyla örttü.»
   - Açıklama: Tek bir kabukla kalenin tepesi örtülmez; 'süsledi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tepesini Pepee'nin bir kabuğuyla örttü"
   - Cümle 10: «Şila da kalenin tepesini Pepee'nin bir kabuğuyla örttü.»
   - Açıklama: Tek bir kabukla kalenin tepesi örtülmez; 'süsledi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0138` birebir aynı, `@degisim: mısır -> kova` (tutuyorsan), ardından `@onarim: 5a26f6f9c1262909b1c85de3ff8df17f0e8bba96`, sonra gövde.

### Hikâye 5: tohum pepee-0139 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0139
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: sırayla oynamak
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'tabela', fiil 'yıkamak', sıfat 'siyah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: tabela çamurla kaplıydı ve yolu göstermiyordu | tabelayı suyla yıkadı ve okun ne demek olduğunu öğrendi
@tohum: pepee-0139
Yağmur yeni dinmişti. Pepee ile Dedee ormanda sırayla önden yürüme oyunu oynuyordu. Sıra Pepee'deydi ama tabela çamurla kaplıydı. Pepee nereye gideceğini bilemedi. "Dede, bana biraz su verir misin?" diye sordu Pepee. Dedee su şişesini hemen ona verdi. Pepee suyla tabelayı güzelce yıkadı. Çamurun altından siyah bir ok çıktı. "Bu ok ne demek, dedeciğim?" diye sordu Pepee. "Ok, bize yolu gösterir," dedi Dedee. Pepee bunu hemen öğrendi ve okun gösterdiği tarafa yürüdü. Dedee de gülerek arkasından geldi. Pepee bundan sonra ormanda hep tabeladaki oka baktı.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Bu ok ne demek, dedeciğim?"
   - Cümle 9: «"Bu ok ne demek, dedeciğim?" diye sordu Pepee.»
   - Açıklama: Çamur sorunu çözüldükten sonra okun anlamını bilmeme diye ikinci bir sorun açılıyor ve onu Dedee çözüyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu ok ne demek, dedeciğim?"
   - Cümle 9: «"Bu ok ne demek, dedeciğim?" diye sordu Pepee.»
   - Açıklama: Tabela yıkandıktan sonra çözüm okun anlamını sormak gibi ek bir adımla uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0139` birebir aynı, ardından `@onarim: 109d221cc9af62f4614329149b132ef3e8d44ec1`, sonra gövde.

### Hikâye 6: tohum pepee-0141 (deneme 1 -> 2)

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
Parkta hafif bir yağmur başladı. Nenee Pepee'yi ahşap salıncağa bindirmek istiyordu. Ama salıncak yağmurdan ıslanmıştı. "Bugün salıncak oyunu yok," dedi Nenee üzgün bir sesle. Sonra çantasından büyük bir şemsiye çıkardı. İkisi şemsiyenin altına girdi. Damlalar şemsiyeye tık tık vurdu. Pepee bu sesi dinledi ve ona göre dans etmeye başladı. Bir sağa, bir sola zıpladı ve ellerini çırptı. "Nenee, sen de gel!" dedi Pepee. Nenee çok güldü ve Pepee'nin elini tuttu. İkisi el ele yavaşça döndü. "Pepee, bu yağmur oyunu salıncaktan da güzel!" dedi Nenee.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ona göre dans etmeye"
   - Cümle 8: «Pepee bu sesi dinledi ve ona göre dans etmeye başladı.»
   - Açıklama: 'Sese göre dans etmek' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ona göre dans etmeye"
   - Cümle 8: «Pepee bu sesi dinledi ve ona göre dans etmeye başladı.»
   - Açıklama: 'Ona' zamirinin sesi mi kişiyi mi gösterdiği belli değil; 'sese göre' olmalı.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "ona göre dans etmeye başladı"
   - Cümle 8: «Pepee bu sesi dinledi ve ona göre dans etmeye başladı.»
   - Açıklama: Çözüm ıslak salıncağa yönelmiyor, salıncak oyununu başka bir oyunla değiştiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0141` birebir aynı, `@degisim: çömlek -> şemsiye` (tutuyorsan), ardından `@onarim: 5e94d5675fe648a56afdc8700df419961070aa0a`, sonra gövde.

### Hikâye 7: tohum pepee-0142 (deneme 1 -> 2)

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
Pepee ile Şila deniz kıyısında kumdan kule yapıyordu. Şila küçük bir fincanla güzel kuleler yaptı. Ama Pepee'nin fincanı yoktu, elle yaptığı kule hemen yıkıldı. Pepee yıkılan kuleye üzgün üzgün baktı. "Şila, ben de kule yapmayı öğrenmek istiyorum," dedi Pepee. "Tabii, fincanı seninle paylaşırım," dedi Şila. Şila fincanı ıslak kumla doldurdu ve kuma ters çevirdi. Pepee onu dikkatle izledi. Sonra fincanı aldı ve aynısını kendisi denedi. Pepee fincanı kaldırdı ve kum yıkılmadı. Kumda küçük, yuvarlak bir kule duruyordu. Pepee sevinçle ellerini çırptı. Pepee ile Şila fincanı sırayla kullandı ve mutlu mutlu yeni kuleler yaptı.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kuzeninden kule yapmayı öğrendi"
   - Cümle 0 (plan satırı): «fincanı olmadığı için kumdan kulesi yıkıldı | kuzeninden kule yapmayı öğrendi ve kendisi denedi»
   - Açıklama: Gövdede Şila'nın kuzen olduğu hiç söylenmiyor; plan gövdede olmayan bir ilişki anlatıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Pepee onu dikkatle izledi"
   - Cümle 8: «Pepee onu dikkatle izledi.»
   - Açıklama: 'onu' zamiri hem Şila'yı hem son geçen fincanı gösterebiliyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "fincanı aldı ve aynısını kendisi denedi"
   - Cümle 9: «Sonra fincanı aldı ve aynısını kendisi denedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; yanında yalnız çocuk olan kuzeni var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0142` birebir aynı, `@degisim: tatmak -> doldurmak` (tutuyorsan), ardından `@onarim: 54e2fb73d33efb46e2d3bacd88571f12134a9776`, sonra gövde.

### Hikâye 8: tohum pepee-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0143
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'sandalye', fiil 'yuvarlamak', sıfat 'şık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: sandalye toprak yığınının üstünde sallandı | toprağın üstünde dans edip yeri düz yaptı
@tohum: pepee-0143
@degisim: yuvarlamak -> sallanmak
Bir sabah Pepee ile Annee ormanda gösteri oyunu oynuyordu. Annee küçük bir sandalyeye oturdu ve Pepee'yi izlemeye hazırlandı. Ama sandalyenin bir ayağı küçük bir toprak yığınının üstündeydi ve sandalye sallandı. "Böyle izleyemem, Pepee!" dedi Annee gülerek. Annee ayağa kalktı. Pepee yığına baktı ve güzel bir fikir buldu. Yığının üstünde ayaklarını yere vurarak komik bir dans yaptı. Toprak her adımda biraz daha aşağı indi. Sonunda yer düz oldu. Annee sandalyeyi düz yere koydu ve yeniden oturdu. Sandalye artık hiç sallanmadı. Pepee tulumunu düzeltti ve şık bir selam verdi. Annee Pepee'yi alkışladı ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve güzel bir fikir buldu"
   - Cümle 6: «Pepee yığına baktı ve güzel bir fikir buldu.»
   - Açıklama: 'Fikir' soyut bir kavram ve 'fikir bulmak' küçük çocuğa uygun somut bir anlatım değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve şık bir selam verdi"
   - Cümle 12: «Pepee tulumunu düzeltti ve şık bir selam verdi.»
   - Açıklama: 'Şık' kelimesi selama uymuyor; anlamca yanlış kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0143` birebir aynı, `@degisim: yuvarlamak -> sallanmak` (tutuyorsan), ardından `@onarim: 80fb0b13912b7eeaf2dc0a048841e1c1f00370b9`, sonra gövde.

### Hikâye 9: tohum pepee-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0144
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Nenee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bilgisayar', fiil 'anlatmak', sıfat 'lezzetli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: nine balın hangi kavanozda olduğunu unuttu | iki kavanozdan da biraz tattı ve balı buldu
@tohum: pepee-0144
@degisim: bilgisayar -> kavanoz
Deniz kıyısında Pepee ile Nenee lokanta oyunu oynuyordu. Pepee ekmeğine bal istedi. Ama iki kavanoz da aynıydı ve Nenee balın hangi kavanozda olduğunu unuttu. "Hangisi bal, hangisi pekmez?" dedi Nenee gülerek. Pepee bir kaşıkla iki kavanozdan da biraz tattı. Pepee tadı hemen tanıdı. "Bal bu kavanozda, Nenee!" dedi Pepee. Nenee ekmeğe bal sürdü ve Pepee'ye verdi. "Nasıl bildin?" diye sordu Nenee. Pepee kahvaltıda hep bal yediğini anlattı. Sonra lezzetli ekmeği keyifle yedi. Pepee ile Nenee bundan sonra bal kavanozuna hep küçük bir işaret koydu.
```

**Hakem bulguları (1):**

1. **C6** (K merceği) — Kalıp yargı yok.
   - Alıntı: "Nenee balın hangi kavanozda olduğunu unuttu"
   - Cümle 3: «Ama iki kavanoz da aynıydı ve Nenee balın hangi kavanozda olduğunu unuttu.»
   - Açıklama: Sorun unutkan nine kalıp yargısına dayanıyor; kartın ilişki alanı Nenee'yi komik ve eğlenceli diye tanımlıyor, unutkan değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0144` birebir aynı, `@degisim: bilgisayar -> kavanoz` (tutuyorsan), ardından `@onarim: 67fba8f7f818f1fe486d704f9b4483d50d09a35a`, sonra gövde.

### Hikâye 10: tohum pepee-0146 (deneme 1 -> 2)

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
Deniz kıyısında Pepee ile Bebee kumdan pasta yapıyordu. İkisi de kırmızı kovayı kullanmak istedi. Ama yalnız bir kova vardı ve Bebee üzüldü. Pepee biraz düşündü ve yeni öğrendiği saymayı denedi. "Bebee, önce sen doldur, ben de sayı sayarım," dedi Pepee. Bebee soğuk, ıslak kumu kovaya koydu. Pepee parmaklarını tek tek açarak on saydı. Sonra kova Pepee'ye geçti. "Şimdi ben sayabilir miyim?" diye sordu Bebee. "Tabii, parmaklarına bak," dedi Pepee. Bebee de parmaklarıyla saymayı denedi. Pepee kumu doldururken Bebee sevinçle etrafta koşturdu. Pepee ile Bebee sırayla kovayı doldurdu ve mutlu mutlu kumdan pastalar yaptı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Deniz kıyısında Pepee ile Bebee"
   - Cümle 1: «Deniz kıyısında Pepee ile Bebee kumdan pasta yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; iki küçük çocuk deniz kıyısında büyüksüz yeni bir şey deniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yeni öğrendiği saymayı denedi"
   - Cümle 4: «Pepee biraz düşündü ve yeni öğrendiği saymayı denedi.»
   - Açıklama: Güvenli kullanım satırı yeni şeylerin bir büyüğün yanında denenmesini ister, oysa Pepee ile küçük Bebee deniz kıyısında büyüksüz.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bebee sevinçle etrafta koşturdu"
   - Cümle 12: «Pepee kumu doldururken Bebee sevinçle etrafta koşturdu.»
   - Açıklama: Bebee sayma sırasını isteyip saymayı denerken bir sonraki cümlede etrafta koşuyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Pepee kumu doldururken Bebee sevinçle etrafta koşturdu"
   - Cümle 12: «Pepee kumu doldururken Bebee sevinçle etrafta koşturdu.»
   - Açıklama: Sıra kuralına göre Bebee sayı saymalıyken etrafta koşturuyor, bu kurulan düzenle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0146` birebir aynı, `@degisim: kebap -> kova` (tutuyorsan), ardından `@onarim: 154439f7772ffc33b56e592d1ad51e6406980493`, sonra gövde.

### Hikâye 11: tohum pepee-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0147
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Nenee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'ip', fiil 'yarışmak', sıfat 'garip'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: nine çok acıktığı için yarışa devam edemedi | kahvaltısını ninesiyle paylaştı
@tohum: pepee-0147
Pepee ile Nenee deniz kıyısında yarışıyordu. Kumun ucunda bitiş için uzun bir ip vardı. Ama Nenee birden durdu, çünkü karnından garip bir ses geldi. "Çok acıktım, Pepee, kahvaltı yapmadım," dedi Nenee gülerek. Pepee hemen çantasını açtı. İçinde yumurta ve bal sürülmüş ekmek vardı. Pepee kahvaltısını ikiye böldü ve yarısını Nenee'ye verdi. İkisi kuma oturup hepsini yedi. Nenee'nin karnı doydu ve o ses de kesildi. "Hadi, Pepee, şimdi ipe kadar yarışalım!" dedi Nenee. İkisi koştu ve ipe aynı anda vardı. Pepee çok sevindi, çünkü kahvaltısını paylaşınca yarış yeniden başlamıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kumun ucunda bitiş"
   - Cümle 2: «Kumun ucunda bitiş için uzun bir ip vardı.»
   - Açıklama: 'Kumun ucu' anlamca uygun değil; 'kumsalın ucunda' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kumun ucunda bitiş için"
   - Cümle 2: «Kumun ucunda bitiş için uzun bir ip vardı.»
   - Açıklama: 'Kumun ucu' kumsalın bitiş yeri için doğal bir kullanım değil; 'kumsalın ucunda' olmalı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İçinde yumurta ve bal sürülmüş ekmek vardı"
   - Cümle 6: «İçinde yumurta ve bal sürülmüş ekmek vardı.»
   - Açıklama: Ekmek kayboldu denmişken hemen sonra çantada ekmek bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0147` birebir aynı, ardından `@onarim: 78dd9407035b9156311ba45393cca61d7d7ca5f1`, sonra gövde.

### Hikâye 12: tohum pepee-0148 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ormanda yerden davul gibi bir ses geldi | dans edip sesin çıktığı yeri buldu
@tohum: pepee-0148
@degisim: davetiye -> kütük
Pepee ile Şila ormanda yaprakların üstünde oynuyordu. Pepee bir ara zıpladı ve yerden davul gibi bir ses geldi. Pepee bu sesin nereden geldiğini çok merak etti. Şila da hemen yanına geldi. Pepee sesi bulmak için orada burada küçük bir dans yaptı. Bir sağa, bir sola adım attı ve her adımda dinledi. Davul sesi yalnız büyük bir ağacın yanında çıktı. Pepee ile Şila oradaki yaprakları elleriyle kenara çekti. Yaprakların altında içi boş, kırık bir kütük vardı. Şila kütüğe eliyle vurdu ve aynı ses geldi. İkisi birbirine bakıp güldü. Pepee bundan sonra bir ses duyunca yerini dikkatle dinleyerek aradı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yerden davul gibi bir ses geldi"
   - Cümle 2: «Pepee bir ara zıpladı ve yerden davul gibi bir ses geldi.»
   - Açıklama: Sorun gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir sıkıntı yaratmıyor.
   - Açıklama: Sorun yalnız bir merak; çocuğun önemseyeceği gerçek bir sorun ve sebep kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0148` birebir aynı, `@degisim: davetiye -> kütük` (tutuyorsan), ardından `@onarim: 0768cd1eade0e3fcc202b0e22ecb78f4786be40d`, sonra gövde.
