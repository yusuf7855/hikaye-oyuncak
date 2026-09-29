# Editör görevi (onarım): Pepee, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0016 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0016
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yağmur ya da kar günü
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'pankek', fiil 'köpürmek', sıfat 'kırılgan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: yağmur başladı ve şapka ıslandı | ninesinden şemsiye isteyip onu açmayı öğrendi
@tohum: pepee-0016
@degisim: pankek -> şemsiye
Deniz kıyısında küçük dalgalar köpürüyordu. Pepee ile Nenee kumda oturmuş, denize bakıyordu. Birden yağmur başladı ve Pepee'nin mavi şapkası ıslandı. "Nineciğim, şemsiye var mı?" diye sordu Pepee. Nenee çantasından katlanmış bir şemsiye çıkardı. "Şemsiyeyi ben açabilir miyim?" diye sordu Pepee. "Tabii, ama yavaş aç, bu teller kırılgan, kolay kırılır," dedi Nenee. Nenee ona küçük bir düğmeyi gösterdi. Pepee düğmeye bastı ve şemsiyeyi yavaşça yukarı itti. Şemsiye kocaman açıldı. İkisi şemsiyenin altına girdi ve artık hiç ıslanmadı. Yağmur damlaları şemsiyede tık tık ses yaptı. Pepee çok mutlu oldu, çünkü şemsiye açmayı kendisi öğrenmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu teller kırılgan"
   - Cümle 7: «"Tabii, ama yavaş aç, bu teller kırılgan, kolay kırılır," dedi Nenee.»
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "bu teller kırılgan, kolay kırılır"
   - Cümle 7: «"Tabii, ama yavaş aç, bu teller kırılgan, kolay kırılır," dedi Nenee.»
   - Açıklama: 'Kırılgan' ile 'kolay kırılır' aynı şeyi gereksiz yere tekrarlıyor.
   - Açıklama: 'Kırılgan' ile 'kolay kırılır' aynı şeyi gereksizce tekrar ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0016` birebir aynı, `@degisim: pankek -> şemsiye` (tutuyorsan), ardından `@onarim: 6e3803a43c2b88be2a98c2b276974361798f93dc`, sonra gövde.

### Hikâye 2: tohum pepee-0021 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0021
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'çit', fiil 'rahatlatmak', sıfat 'şanslı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: taş düz değildi ve yumurta masadan yuvarlandı | taşın kenarına dalları dikti ve çit yaptı
@tohum: pepee-0021
@degisim: rahatlatmak -> dikmek
Bir sabah Pepee ormanda evcilik oynuyordu. Büyük bir taşı masa yaptı ve üstüne kahvaltısını dizdi. Ama taş düz değildi ve yumurta masadan yuvarlandı. Pepee hemen koştu ve yumurtayı elleriyle yakaladı. Yumurta yere düşmedi, Pepee çok şanslıydı. Pepee yumurtayı çok severdi ve onu masada yemek istedi. Yerden ince dallar topladı. Dalları taşın kenarına, toprağa sıkıca dikti. Böylece taşın kenarında küçük bir çit oldu. Pepee yumurtayı yeniden masaya koydu. Yumurta yine yuvarlandı ama çite çarpıp durdu. Pepee güldü ve yumurtasını afiyetle yedi. Sonra oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee çok şanslıydı"
   - Cümle 5: «Yumurta yere düşmedi, Pepee çok şanslıydı.»
   - Açıklama: 'Şanslı' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0021` birebir aynı, `@degisim: rahatlatmak -> dikmek` (tutuyorsan), ardından `@onarim: 538cd5ac628996fa2a8804843b4bde63271a70c2`, sonra gövde.

### Hikâye 3: tohum pepee-0024 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0024
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kırıntı', fiil 'ışıldamak', sıfat 'çalışkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: dedenin anahtarı yaprakların arasına düştü | güneşte parlayan yere bakıp anahtarı buldu
@tohum: pepee-0024
@degisim: kırıntı -> anahtar
Ormanda serin bir rüzgar esiyordu. Pepee ile Dedee ağaçların arasında yürüyordu. Birden Dedee durdu, çünkü ev anahtarı cebinden düşmüştü. "Anahtar bu yaprakların arasında olmalı," dedi Dedee. Ama yerde çok yaprak vardı. "Dedeciğim, anahtarı nasıl buluruz?" diye sordu Pepee. "Güneş vurunca anahtar parlar," dedi Dedee. Pepee dedesinden öğrendiğini hemen denedi ve güneşli yerlere dikkatle baktı. İki yaprağın arasında küçük bir şey ışıldadı. Pepee oraya koştu ve anahtarı buldu. "Sen çok çalışkansın, Pepee," dedi Dedee. Pepee çok sevindi, çünkü dedesine yardım etmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sen çok çalışkansın, Pepee"
   - Cümle 11: «"Sen çok çalışkansın, Pepee," dedi Dedee.»
   - Açıklama: Anahtarı dikkatle bakarak bulmak çalışkanlık değil; övgü kelimesi olaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0024` birebir aynı, `@degisim: kırıntı -> anahtar` (tutuyorsan), ardından `@onarim: c217283831986572ddb078c53593d0d17b3aa2f2`, sonra gövde.

### Hikâye 4: tohum pepee-0028 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0028
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'pizza', fiil 'yeşillenmek', sıfat 'basit'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: yapraktan pizzayı pişirecek bir fırın yoktu | ağaçtaki küçük deliği fırın yapıp pizzayı içine koydu
@tohum: pepee-0028
@degisim: yeşillenmek -> toplamak
Rüzgar ağaçların arasında esiyordu. Pepee ile Nenee ormanda pizza oyunu oynuyordu. Yuvarlak bir yaprağı pizza yaptılar ama onu pişirecek bir fırın yoktu. Nenee yerden yeşil otlar topladı ve pizzanın üstüne koydu. "Nine, fırını nerede buluruz?" diye sordu Pepee. "Fırın gibi bir yer ara, bu çok basit," dedi Nenee ve güldü. Pepee kalın bir ağacın dibinde küçük bir delik buldu. Ninesinden öğrendiği gibi bu deliği fırın yaptı. Pizzayı dikkatle deliğin içine koydu. İkisi birlikte ona kadar saydı. Sonra Pepee pizzayı çıkardı ve ninesine uzattı. "Buyur, nineciğim, orman pizzası pişti!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Nenee yerden yeşil otlar topladı"
   - Cümle 4: «Nenee yerden yeşil otlar topladı ve pizzanın üstüne koydu.»
   - Açıklama: Otlar pizzanın üstüne konuyor ama olayda hiçbir işe yaramıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fırını nerede buluruz"
   - Cümle 5: «"Nine, fırını nerede buluruz?" diye sordu Pepee.»
   - Açıklama: Ortada olmayan bir fırın belirtme ekiyle anılmış; 'bir fırın nerede bulabiliriz' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0028` birebir aynı, `@degisim: yeşillenmek -> toplamak` (tutuyorsan), ardından `@onarim: cb1b4b9605b9cde23580d1ca0acc3170ef07add7`, sonra gövde.

### Hikâye 5: tohum pepee-0029 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0029
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: kaybolan eşya
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'gazete', fiil 'yorulmak', sıfat 'kirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: şapka koltukta görünmüyordu | annesini dinleyip koltukta gazetenin altına baktı
@tohum: pepee-0029
@degisim: kirli -> mavi
Evde Pepee mavi şapkasını arıyordu. Şapkayı az önce koltuğa koymuştu ama şimdi orada göremiyordu. Mutfağa ve odasına da baktı, ama şapka hiçbir yerde yoktu. Sonunda Pepee yoruldu ve masada oturan annesinin yanına gitti. "Anne, şapkam kayboldu," dedi Pepee. "Şapkayı nereye koydun? Koyduğun yere yine bak, eşyaların altına da bak," dedi Annee. Pepee bunu annesinden öğrendi ve koltuğa döndü. Koltukta annesinin gazetesi duruyordu. Pepee gazeteyi kaldırdı ve şapkasını altında buldu. Şapkayı hemen başına taktı. "Teşekkürler, anneciğim, şapkamı buldum!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bunu annesinden öğrendi"
   - Cümle 8: «Pepee bunu annesinden öğrendi ve koltuğa döndü.»
   - Açıklama: 'Öğrendi' fiili burada yerinde değil; anne yalnızca öneri verdi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0029` birebir aynı, `@degisim: kirli -> mavi` (tutuyorsan), ardından `@onarim: 5219140bce5bae977f08c31fb613fd6b05dd772e`, sonra gövde.

### Hikâye 6: tohum pepee-0031 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0031
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: paylaşmak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'boru', fiil 'ıslanmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: ağacın altındaki kuru yer küçüktü ve annesi ıslanıyordu | ağaca yaslanıp dans ederek annesini kuru yere çekti
@tohum: pepee-0031
@degisim: boru -> ağaç
Yağmur yapraklara hafifçe vuruyordu. Pepee ile Annee ormanda büyük bir ağacın altına koştu. Ama ağacın altındaki kuru yer küçüktü ve Annee'nin omzu ıslanıyordu. Pepee annesine yer açmak istedi. Hemen ağaca iyice yaslandı. Sonra annesinin elini tuttu ve dans ederek onu yanına çekti. Annee dönerek kuru yere geldi ve güldü. Şimdi ikisi de yaprakların altında kuruydu. Annee Pepee'nin başını okşadı. Annee yağmuru huzurlu bir yüzle izledi. Yağmur bir süre daha yağdı, sonra durdu. Pepee çok mutluydu, çünkü kuru yerini annesiyle paylaşmıştı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "büyük bir ağacın altına koştu"
   - Cümle 2: «Pepee ile Annee ormanda büyük bir ağacın altına koştu.»
   - Açıklama: Yağmurda ormanda ağaç altına sığınmak çocuğun taklit edebileceği tehlikeli bir davranış (yıldırım riski).
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yağmuru huzurlu bir yüzle izledi"
   - Cümle 10: «Annee yağmuru huzurlu bir yüzle izledi.»
   - Açıklama: 'Huzurlu bir yüzle' soyut bir ifade, 3 yaşındaki çocuk bilmeyebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yağmuru huzurlu bir yüzle"
   - Cümle 10: «Annee yağmuru huzurlu bir yüzle izledi.»
   - Açıklama: 'Huzurlu bir yüzle' soyut bir ifade; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0031` birebir aynı, `@degisim: boru -> ağaç` (tutuyorsan), ardından `@onarim: 4d2d30e2f15dd997a28e5ee9f42f325af294b484`, sonra gövde.

### Hikâye 7: tohum pepee-0032 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0032
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bambu', fiil 'katmak', sıfat 'vanilyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: bambu yaprakları camın yarısını kapatıyordu | tabağını aldı ve öbür sandalyeye geçti
@tohum: pepee-0032
@degisim: vanilyalı -> uzun
Evde, pencerenin önünde uzun bir bambu vardı. Pepee kahvaltı yaparken dışarıda kar yağdığını gördü. Ama bambu yaprakları camın yarısını kapatıyordu. Pepee karı iyice görmek istedi. Ama tabağındaki yumurtayı da bırakmak istemedi. Bambu saksısı ise çok ağırdı. Pepee tabağını aldı ve öbür sandalyeye geçti. Buradan bütün cam görünüyordu. Kocaman kar taneleri yavaşça yere iniyordu. Pepee kar tanelerini tek tek saydı. Sonra pekmezine biraz tahin kattı ve pencereye bakarak yedi. Pepee çok sevindi, çünkü hem kahvaltısını yapıyor hem de yağan karı görüyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra pekmezine biraz tahin kattı"
   - Cümle 11: «Sonra pekmezine biraz tahin kattı ve pencereye bakarak yedi.»
   - Açıklama: Pekmez ve tahin sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0032` birebir aynı, `@degisim: vanilyalı -> uzun` (tutuyorsan), ardından `@onarim: c726a73c9dd0319d68a2b183559a6c2a0060f506`, sonra gövde.

### Hikâye 8: tohum pepee-0035 (deneme 2 -> 3)

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
@plan: baloncuk uçurmak istedi ama halka yoktu | ince bir ottan yeni bir halka yaptı
@tohum: pepee-0035
@degisim: krem -> halka
Bir sabah Pepee ile Bebee ormanda kahvaltı yapıyordu. "Bak, Pepee, boyum uzadı!" dedi Bebee. Bebee artık çiçekli dala dokunabiliyordu. Pepee bunu kutlamak için baloncuk uçurmak istedi, ama çantada halka yoktu. Çantada yalnız bir şişe sabunlu su vardı. Pepee yerde ince ve uzun bir ot buldu. Otun ucunu kıvırdı ve küçük bir halka yaptı. Halkayı suya batırdı ve yavaşça üfledi. Ağaçların arasına bir sürü baloncuk uçtu. Bebee onların arkasından koştu ve ellerini çırptı. "Bunlar senin için, Bebee!" dedi Pepee. Sonra Pepee en sevdiği balı da Bebee'ye verdi. İkisi mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ile Bebee ormanda"
   - Cümle 1: «Bir sabah Pepee ile Bebee ormanda kahvaltı yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama iki küçük çocuk ormanda büyüksüz kalıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ormanda kahvaltı yapıyordu"
   - Cümle 1: «Bir sabah Pepee ile Bebee ormanda kahvaltı yapıyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunun çözümünde işe yaramıyor, yalnız sahne olarak geçiyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Bebee artık çiçekli dala dokunabiliyordu.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "çantada halka yoktu"
   - Cümle 4: «Pepee bunu kutlamak için baloncuk uçurmak istedi, ama çantada halka yoktu.»
   - Açıklama: Halkanın olmaması sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee en sevdiği balı da Bebee'ye verdi"
   - Cümle 12: «Sonra Pepee en sevdiği balı da Bebee'ye verdi.»
   - Açıklama: Bal olaya bağlanmayan işlevsiz bir ekleme.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Pepee en sevdiği balı da Bebee'ye verdi"
   - Cümle 12: «Sonra Pepee en sevdiği balı da Bebee'ye verdi.»
   - Açıklama: Bal sebepsiz beliriyor ve baloncuk olayından çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0035` birebir aynı, `@degisim: krem -> halka` (tutuyorsan), ardından `@onarim: 4f90a58a26b27115ba5bdcd8a521e0d025c69090`, sonra gövde.

### Hikâye 9: tohum pepee-0036 (deneme 2 -> 3)

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
Pepee deniz kıyısında kahvaltıya koşuyordu, çünkü kahvaltıyı çok severdi. Koşarken Nenee'nin kumdan yaptığı pastaya bastı. Pasta dağıldı ve üstündeki deniz kabukları kuma saçıldı. Nenee buna çok üzüldü. Pepee durdu ve hemen ninesinden özür diledi. Sonra pastayı Nenee ile birlikte yeniden yaptı. Kabukları ıslak kumla pastanın üstüne yapıştırdı ve gülen bir yüz yaptı. Nenee yüzü görünce kahkaha attı. Sonra Pepee'ye sarıldı ve onun akıllı bir çocuk olduğunu söyledi. Pepee çok sevindi, çünkü ninesi artık üzgün değildi ve pasta yine güzeldi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çünkü kahvaltıyı çok severdi"
   - Cümle 1: «Pepee deniz kıyısında kahvaltıya koşuyordu, çünkü kahvaltıyı çok severdi.»
   - Açıklama: Tohumdaki kahvaltı özelliği iki kez geçiyor ve işe yarar biçimde kullanılmak yerine huy olarak sayılıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ve gülen bir yüz yaptı"
   - Cümle 7: «Kabukları ıslak kumla pastanın üstüne yapıştırdı ve gülen bir yüz yaptı.»
   - Açıklama: 'Yaptı' fiili art arda cümlelerde gereksiz yere tekrarlanıyor.
   - Açıklama: Bir önceki cümledeki 'yaptı' fiili gereksiz yere tekrar ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0036` birebir aynı, `@degisim: çekmece -> kabuk` (tutuyorsan), ardından `@onarim: 7600b928afbd7f9d01d0ecfa2545a07c315767cc`, sonra gövde.

### Hikâye 10: tohum pepee-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0037
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'bulmaca', fiil 'tanıştırmak', sıfat 'tuzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: bulmacanın son sorusunu bilmiyordu | dedesinden yardım istedi ve cevabı buldu
@tohum: pepee-0037
@degisim: tanıştırmak -> sormak
Deniz kıyısında hava güzeldi. Pepee ile Dedee kumda oturmuş, resimli bir bulmaca yapıyordu. Son soru deniz suyunun tadını soruyordu, ama Pepee bunu bilmiyordu. "Dedeciğim, bana yardım eder misin?" diye sordu Pepee. Dedee onu su kenarındaki büyük bir taşa götürdü. Taşın üstünde ince, beyaz bir tuz vardı. "Bu tuz denizden geldi. Deniz suyu tuzlu," dedi Dedee. Pepee böylece yeni bir kelime öğrendi. Kelimeyi dedesiyle birlikte bulmacaya yazdı. Bulmaca bitmişti ve Pepee ile Dedee mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Son soru deniz suyunun tadını soruyordu"
   - Cümle 3: «Son soru deniz suyunun tadını soruyordu, ama Pepee bunu bilmiyordu.»
   - Açıklama: 'Soru ... soruyordu' aynı kökü gereksiz yere tekrarlıyor.
   - Açıklama: 'Soru ... soruyordu' gereksiz bir kök tekrarı yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0037` birebir aynı, `@degisim: tanıştırmak -> sormak` (tutuyorsan), ardından `@onarim: 1290bfb8929f989977ab5bce69fa2fa7ae299906`, sonra gövde.

### Hikâye 11: tohum pepee-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0039
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'meşe', fiil 'büyütmek', sıfat 'yamuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: fidan yamuk duruyordu çünkü üstünde kuru dal vardı | dalı kaldırdı ve fidanı bir kaşığa yasladı
@tohum: pepee-0039
Bir sabah Pepee ile Şila ormanda bir meşe ağacının altında kahvaltı yapıyordu. Pepee ağacın dibinde küçük bir meşe fidanı gördü. Fidan yamuk duruyordu, çünkü üstünde kuru bir dal vardı. "Şila, bu fidanı büyütmek istiyorum," dedi Pepee. Pepee kuru dalı fidanın üstünden yavaşça kaldırdı. Fidan biraz doğruldu, ama yine eğikti. "Pepee, onu nasıl dik tutacağız?" diye sordu Şila. Pepee tabağının yanındaki tahta kaşığı aldı. Kaşığı fidanın yanında toprağa soktu ve fidanı ona yasladı. Fidan artık dimdik duruyordu. Pepee ile Şila fidana bakıp mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kaşığı fidanın yanında toprağa soktu"
   - Cümle 9: «Kaşığı fidanın yanında toprağa soktu ve fidanı ona yasladı.»
   - Açıklama: Söylenen sebep kuru daldı ama dal kalkınca fidan düzelmiyor; asıl çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0039` birebir aynı, ardından `@onarim: d5a858cf58fde0e6083a23a1393c35a0d5237d3d`, sonra gövde.

### Hikâye 12: tohum pepee-0040 (deneme 2 -> 3)

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
@plan: yumurta yuvarlak olduğu için yere düştü | peçeteyi katlayıp kaşığın içine koydu
@tohum: pepee-0040
@degisim: kolye -> peçete
Bir sabah Pepee ormanda kuşları dinleyerek kahvaltı yapıyordu. Sonra sıcacık yumurtasını kaşığa koydu ve ağaca kadar taşımak istedi. Ama yumurta yuvarlaktı ve ilk adımda yere düştü. Pepee bir kez daha denedi, ama yumurta yine düştü. Pepee kaşığa baktı ve düşündü. Sonra peçetesini katladı ve kaşığın içine koydu. Yumurtayı peçetenin üstüne yerleştirdi. Yumurta peçetenin üstünde güzelce durdu. Pepee yavaş adımlarla büyük ağaca kadar yürüdü. Yumurta bir kez bile düşmedi. Sonra Pepee ağacın altına oturdu ve yumurtasını mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ormanda kuşları dinleyerek"
   - Cümle 1: «Bir sabah Pepee ormanda kuşları dinleyerek kahvaltı yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama ormanda yalnız başına kahvaltı edip deneme yapıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağaca kadar taşımak istedi"
   - Cümle 2: «Sonra sıcacık yumurtasını kaşığa koydu ve ağaca kadar taşımak istedi.»
   - Açıklama: Yumurtayı kaşıkla ağaca taşıma hedefi sebepsiz ve yapay, yere iki kez düşen yumurtanın sonra yenmesi de akla yatkın değil.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yumurtasını mutlu mutlu yedi"
   - Cümle 11: «Sonra Pepee ağacın altına oturdu ve yumurtasını mutlu mutlu yedi.»
   - Açıklama: İki kez yere düşen yumurtanın yenmesi çocuğa yerden yemek yemeyi örnek gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0040` birebir aynı, `@degisim: kolye -> peçete` (tutuyorsan), ardından `@onarim: a486ccfc6b4986760220d4905349e5cbe37ee1df`, sonra gövde.
