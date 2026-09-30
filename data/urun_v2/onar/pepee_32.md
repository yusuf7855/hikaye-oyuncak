# Editör görevi (onarım): Pepee, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar32.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0150 (deneme 1 -> 2)

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
Bir sabah Pepee parktaki bankta kahvaltı yapıyordu. Şirin kupasında tahin ve pekmezi ilk kez kendisi karıştırmak istedi. Ama tahin çok koyuydu ve kaşık zor döndü. Pepee sabırsızlandı ve kaşığı hızlı hızlı çevirdi. Yine de tahin kupanın dibinde kaldı. Pepee durdu ve kupaya dikkatle baktı. Sonra kaşıkla küçük ve yavaş daireler çizdi. Koyu tahin sonunda pekmeze karıştı. Kupada kahverengi, parlak bir tahin pekmez oldu. Pepee ekmeğini kupaya batırdı ve tadına baktı. Tadı çok güzeldi. Pepee çok mutlu oldu, çünkü ilk tahin pekmezini kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee sabırsızlandı ve kaşığı"
   - Cümle 4: «Pepee sabırsızlandı ve kaşığı hızlı hızlı çevirdi.»
   - Açıklama: 'Sabırsızlandı' soyut bir kelimedir, 3 yaşındaki çocuk için ağır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee sabırsızlandı ve"
   - Cümle 4: «Pepee sabırsızlandı ve kaşığı hızlı hızlı çevirdi.»
   - Açıklama: 'Sabırsızlanmak' soyut bir duygu kelimesi, 3 yaşındaki çocuğa uygun olmayabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0150` birebir aynı, ardından `@onarim: 982074ff0830043b57a12029fd84b3d42758d9f0`, sonra gövde.

### Hikâye 2: tohum pepee-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0151
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'kum', fiil 'silkmek', sıfat 'tuhaf'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kum kuru olduğu için resmin çizgileri kapandı | ıslak kumda denedi ve evi çizdi
@tohum: pepee-0151
Bir sabah Pepee deniz kıyısında kuma resim çiziyordu. Elindeki küçük dalla bir ev çizmek istedi. Ama kum çok kuruydu ve çizgiler hemen kapandı. Ev tuhaf bir patatese benzedi ve Pepee güldü. Pepee su kenarındaki ıslak kumda yeniden denedi. Islak kumda çizgiler hiç kapanmadı. Pepee bir kapı, iki pencere ve bir çatı çizdi. Bu kez resim gerçek bir eve benzedi. Pepee ıslak kumun resim için daha iyi olduğunu öğrendi. Sonra ellerindeki kumu silkti. Pepee çok sevindi, çünkü evi artık kumda kaybolmuyordu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Pepee deniz kıyısında kuma resim çiziyordu"
   - Cümle 1: «Bir sabah Pepee deniz kıyısında kuma resim çiziyordu.»
   - Açıklama: Güvenli özellik kullanımı satırı Pepee'nin yeni şeyleri bir büyüğün yanında denediğini söylüyor, ama dört yaşındaki Pepee deniz kıyısında yalnız başına deniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "su kenarındaki ıslak kumda yeniden denedi"
   - Cümle 5: «Pepee su kenarındaki ıslak kumda yeniden denedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada su kenarında yanında büyük olmadan deniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çünkü evi artık kumda"
   - Cümle 11: «Pepee çok sevindi, çünkü evi artık kumda kaybolmuyordu.»
   - Açıklama: 'Evi' Pepee'nin kendi evi gibi okunuyor; kastedilen çizdiği ev resmi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0151` birebir aynı, ardından `@onarim: c835fab7268a5718a3b86ab3105e9b706d4b1727`, sonra gövde.

### Hikâye 3: tohum pepee-0152 (deneme 1 -> 2)

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
Pepee ile Dedee kar yağan bir sabah parktaydı. Parktaki masanın üstü kar doluydu. Pepee masada kar topu yapmak istedi ama kuru kar hep dağıldı. "Dedeciğim, kar topunu nasıl yaparım?" diye sordu Pepee. "Karı iki elinle iyice sık," dedi Dedee. Pepee iki eliyle biraz kar aldı ve denedi. Önce hafifçe, sonra daha sıkı bastırdı. Bu kez kar yuvarlak bir top oldu. Pepee büyük, küçük, değişik toplar yapıp masaya dizdi. Dedee en büyük topun üstüne küçük bir top koydu. "Bak, Pepee, kardan bir kule yaptık!" dedi Dedee. Pepee çok sevindi, çünkü kar topu yapmayı öğrenmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kar topunu nasıl yaparım"
   - Cümle 4: «"Dedeciğim, kar topunu nasıl yaparım?" diye sordu Pepee.»
   - Açıklama: Belirtme eki yersiz; 'kar topu nasıl yaparım' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0152` birebir aynı, `@degisim: boyamak -> sıkmak` (tutuyorsan), ardından `@onarim: d301a6681cfb2789dd5b2c53f3cc6dd36654bbaf`, sonra gövde.

### Hikâye 4: tohum pepee-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0153
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'limonata', fiil 'ölçmek', sıfat 'ince'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: limonata çok ekşiydi çünkü içinde şeker yoktu | annesinden yardım istedi ve balı ölçtü
@tohum: pepee-0153
Rüzgar hafif hafif esiyordu. Pepee ile Annee ormanda kahvaltı yapıyordu. Pepee limonatayı tattı ve yüzünü buruşturdu. Limonata çok ekşiydi, çünkü içinde hiç şeker yoktu. Pepee kahvaltıda en sevdiği bal kavanozunu sepetten çıkardı. Ama bardağa ne kadar bal koyacağını bilmiyordu. Pepee annesinden yardım istedi. Annee ona ince bir kaşık verdi ve iki parmağını gösterdi. Pepee iki kaşık balı dikkatle ölçtü ve bardağa koydu. Sonra limonatayı güzelce karıştırdı ve tadına baktı. Limonata artık hiç ekşi değildi. Pepee ile Annee kahvaltılarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Limonata çok ekşiydi, çünkü içinde hiç şeker yoktu"
   - Cümle 4: «Limonata çok ekşiydi, çünkü içinde hiç şeker yoktu.»
   - Açıklama: Sorun ilk üç cümlede yalnız ima ediliyor, açıkça ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0153` birebir aynı, ardından `@onarim: 1ef5251265446f9e76cf00664375fd8402374fcd`, sonra gövde.

### Hikâye 5: tohum pepee-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0154
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Nenee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'dilim', fiil 'yerleştirmek', sıfat 'düz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: yerdeki kökler dans ederken ayaklarına takılıyordu | çiçeklerin arasında düz bir yer bulup orada dans etti
@tohum: pepee-0154
Bir sabah Nenee ormandaki pikniğe dilim dilim kek getirmişti. Pepee ninesine teşekkür için bir dans sürprizi hazırlamak istedi. Ama ağaçların altında bir sürü kök vardı ve ayakları onlara takılıyordu. Pepee çiçeklerin arasında düz bir yer aradı. Büyük bir ağacın yanında yumuşak bir çimen buldu. Sonra kek dilimlerini bir tabağa yerleştirdi. "Nineciğim, gel, her şey hazır!" dedi Pepee. Nenee gelip tabağın yanına oturdu. Pepee çimenin üstünde döne döne dans etti. Ayakları bu kez hiç takılmadı. Nenee güldü ve ellerini çırptı. "Bu çok güzel bir sürpriz, Pepee!" dedi Nenee. Pepee bundan sonra dans etmek için hep düz bir yer seçti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kökler dans ederken ayaklarına"
   - Cümle 0 (plan satırı): «yerdeki kökler dans ederken ayaklarına takılıyordu | çiçeklerin arasında düz bir yer bulup orada dans etti»
   - Açıklama: Plan satırında 'dans ederken' kökleri özne gibi gösteriyor; özne uyumsuz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ninesine teşekkür için bir"
   - Cümle 2: «Pepee ninesine teşekkür için bir dans sürprizi hazırlamak istedi.»
   - Açıklama: 'Teşekkür için' eksik; 'teşekkür etmek için' olmalı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Büyük bir ağacın yanında yumuşak bir çimen buldu"
   - Cümle 5: «Büyük bir ağacın yanında yumuşak bir çimen buldu.»
   - Açıklama: Kökler ağaçların altında sorun çıkarırken Pepee düz yeri yine büyük bir ağacın yanında buluyor, bu da sorunun sebebiyle çelişiyor.
   - Açıklama: Kökler ağaçların altında sorun yaratıyorken düz yer yine büyük bir ağacın yanında bulunuyor ve plandaki çiçeklerin arası da değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0154` birebir aynı, ardından `@onarim: 6b547ecd8dd445871d638ebd7d1be7fbfb2dfe94`, sonra gövde.

### Hikâye 6: tohum pepee-0157 (deneme 1 -> 2)

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
Pepee deniz kokulu kumsalda kumdan bir kale yapıyordu. Kaleyi süslemek için küçük deniz tarağı kabukları toplamıştı. Ama kum çok kuruydu ve kale hemen dağıldı. Pepee kumu yeniden yığdı ama kale yine yıkıldı. Sonra su kenarındaki ıslak kuma baktı. Oradaki kum birbirine yapışıyordu. Pepee yeni bir şey öğrenmişti ve hemen denedi. Kovasını oradaki kumla doldurdu. Kovayı ters çevirdi ve yavaşça kaldırdı. Bu kez kale hiç dağılmadı. Pepee kalenin üstüne tarak kabuklarını tek tek dizdi. Pepee bundan sonra kum kalelerini hep ıslak kumla yaptı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee yeni bir şey öğrenmişti ve hemen denedi"
   - Cümle 7: «Pepee yeni bir şey öğrenmişti ve hemen denedi.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada su kenarında yalnız deniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yeni bir şey öğrenmişti ve hemen denedi"
   - Cümle 7: «Pepee yeni bir şey öğrenmişti ve hemen denedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada su kenarında yalnız deniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee yeni bir şey öğrenmişti"
   - Cümle 7: «Pepee yeni bir şey öğrenmişti ve hemen denedi.»
   - Açıklama: 'Yeni bir şey öğrenmek' soyut bir anlatım; ne öğrenildiği ve neyin denendiği somut olarak söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0157` birebir aynı, ardından `@onarim: aa76823af73a5ce51ec86881439300e676321cb3`, sonra gövde.

### Hikâye 7: tohum pepee-0158 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0158
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Dedee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'yosun', fiil 'saklanmak', sıfat 'hevesli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: dede yosun dolu bir taşın arkasına saklandı | dans edip şarkı söyledi ve dedesi çıktı
@tohum: pepee-0158
Deniz kıyısında Pepee ile Dedee kumdan bir gemide oynuyordu. Oyunda Pepee, gemisiyle dedesini arıyordu. Dedee üstü yosun dolu büyük bir taşın arkasına saklanmıştı ve hiç görünmüyordu. Pepee kumda her yere baktı ama dedesini bulamadı. Pepee dedesinin hareketli oyunları çok sevdiğini biliyordu. Kumun üstünde zıplayarak dans etmeye başladı. "Hop, hop, gemide dans var!" diye şarkı söyledi Pepee. Hevesli Dedee taşın arkasından koşarak çıktı. Dedee de Pepee'nin yanında zıplayıp dans etti. "Buldum seni, dedeciğim!" dedi Pepee. İkisi kumdaki gemide birlikte güldü. "Pepee, bu çok güzel bir oyundu!" dedi Dedee.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Buldum seni, dedeciğim!"
   - Cümle 10: «"Buldum seni, dedeciğim!" dedi Pepee.»
   - Açıklama: Dedee kendisi taşın arkasından çıktığı halde Pepee onu bulmuş gibi konuşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0158` birebir aynı, ardından `@onarim: c19990a2293c2ca96d4dc333a4e5f7eacd3445ab`, sonra gövde.

### Hikâye 8: tohum pepee-0159 (deneme 1 -> 2)

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
Dışarıda kar yağıyordu. Pepee pencereden baktı. Kar taneleri havada dönüyordu. Pepee de onlar gibi dans etmek istedi ama yepyeni çorapları yerde kayıyordu. Pepee hemen yere oturdu ve çoraplarını çıkardı. Artık ayakları yere iyi basıyordu. Pepee kendine bir kar tanesi oyunu kurdu. Kollarını iki yana açtı ve pencerenin önünde yavaşça döndü. Sonra dışarıdaki taneler gibi yavaşça yere indi. Yeniden kalktı ve bir kez daha döndü. Dışarıda taneler dönerken Pepee de içeride dönüyordu. Pepee pencerenin önünde mutlu mutlu dans etmeye devam etti.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Pepee de onlar gibi dans etmek istedi ama yepyeni çorapları yerde kayıyordu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "yepyeni çorapları yerde kayıyordu"
   - Cümle 4: «Pepee de onlar gibi dans etmek istedi ama yepyeni çorapları yerde kayıyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Dışarıda taneler dönerken Pepee"
   - Cümle 11: «Dışarıda taneler dönerken Pepee de içeride dönüyordu.»
   - Açıklama: Tanelerin ve Pepee'nin döndüğü önceki cümlelerde anlatılmışken gereksiz yere yeniden söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0159` birebir aynı, `@degisim: yağ -> kar` (tutuyorsan), ardından `@onarim: c16ff344331088e10a00698aad54b4aac7975f89`, sonra gövde.

### Hikâye 9: tohum pepee-0161 (deneme 1 -> 2)

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
@plan: yağmur başladı ve ekmek ıslanmaya başladı | dedesinden yardım istedi ve şemsiyeyi açtı
@tohum: pepee-0161
Bir sabah Pepee ile Dedee bulutlu havada parkta kahvaltı yapıyordu. Pepee en sevdiği ballı ekmeği yemeye başlamıştı. Birden yağmur başladı ve ekmeğin üstüne damlalar düştü. Pepee ekmeğini kuru yemek istedi. Dedee bulutları görünce sepete büyük bir şemsiye koymuştu. Ama Pepee şemsiyeyi açamadı. "Dedeciğim, bana yardım eder misin?" diye sordu Pepee. "Tabii, bu çok kolay," dedi Dedee ve düğmeyi gösterdi. Pepee düğmeye bastı ve şemsiye hemen açıldı. Dedee şemsiyeyi ikisinin üstünde tuttu. Pepee ballı ekmeğini şemsiyenin altında bitirdi. İkisi yağmurun sesini dinleyip güldü. Pepee bundan sonra zor bir işte dedesinden yardım istedi.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama Pepee şemsiyeyi açamadı"
   - Cümle 6: «Ama Pepee şemsiyeyi açamadı.»
   - Açıklama: Ekmeğin ıslanmasının yanına sebebi söylenmeyen ikinci bir sorun (şemsiyenin açılmaması) ekleniyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "zor bir işte dedesinden"
   - Cümle 13: «Pepee bundan sonra zor bir işte dedesinden yardım istedi.»
   - Açıklama: Tekil 'zor bir işte' alışkanlık anlatan cümleye uymuyor; 'zor işlerde' olmalı.
   - Açıklama: 'Bundan sonra' ile tekil 'zor bir işte' uyumsuz; 'zor işlerde' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0161` birebir aynı, ardından `@onarim: 11ba2f3da93a5da1f69b9ce6748fd4e6cd5874fc`, sonra gövde.

### Hikâye 10: tohum pepee-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Annee
@tohum: pepee-0163
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: paylaşmak
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'çatal', fiil 'kopmak', sıfat 'masmavi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | deniz | Annee
@plan: sepetin sapı koptu ve annenin yumurtası kuma düştü | kendi yumurtasını ve ekmeğini annesiyle paylaştı
@tohum: pepee-0163
Pepee annesiyle masmavi denizin kıyısında kahvaltı yapıyordu. Annee sepeti kaldırdı ama sepetin sapı koptu. Sepet devrildi ve Annee'nin yumurtası kuma düştü. "Eyvah, yumurtam kum oldu," dedi Annee. Pepee kendi tabağına baktı. Tabakta en sevdiği iki yumurta ve ballı ekmek vardı. "Anneciğim, benimkini paylaşalım," dedi Pepee. Pepee çatalıyla bir yumurtayı alıp annesine uzattı. Sonra ballı ekmeğini de ikiye böldü. Annee yumurtayı ve ekmeği keyifle yedi. İkisi dalgalara bakıp güldü. "Sağ ol, Pepee, seninle yemek çok güzel!" dedi Annee.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Eyvah, yumurtam kum oldu"
   - Cümle 4: «"Eyvah, yumurtam kum oldu," dedi Annee.»
   - Açıklama: Yumurta kum olmaz; 'kuma bulandı' anlamında yanlış ve mecazlı kullanım.
   - Açıklama: Yumurta kum olmaz; 'kuma bulandı' anlamı yanlış kelimeyle verilmiş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en sevdiği iki yumurta"
   - Cümle 6: «Tabakta en sevdiği iki yumurta ve ballı ekmek vardı.»
   - Açıklama: 'En sevdiği' iki yumurtaya uygunsuz bağlanmış; anlam bozuk.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Anneciğim, benimkini paylaşalım"
   - Cümle 7: «"Anneciğim, benimkini paylaşalım," dedi Pepee.»
   - Açıklama: Çözüm sorunun sebebi olan kopan sapa yönelmiyor, yalnız sonucunu telafi ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0163` birebir aynı, ardından `@onarim: 897dd54752b3bb90ae21193ae87304cd7f794887`, sonra gövde.

### Hikâye 11: tohum pepee-0164 (deneme 1 -> 2)

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
Yağmur cama tıp tıp vuruyordu. Pepee ile Şila evde yumuşak bir topla oynuyordu. Pepee topa sert vurdu ve top, Şila'nın getirdiği kaktüsü devirdi. Saksının ıslak toprağı yere döküldü. Şila çok üzüldü, çünkü kaktüsü Pepee için getirmişti. "Özür dilerim, Şila, dikkat etmedim," dedi Pepee. Pepee saksıyı kenarından tuttu ve yerine koydu. Sonra süpürgeyi getirdi ve yerdeki toprağı süpürdü. Toprağı yeniden saksıya doldurdu. Pepee kahvaltıdan kalan balı bir ekmeğe sürdü ve Şila'ya verdi. Şila ekmeği ısırdı ve gülümsedi. "Seni affettim, Pepee, balın da çok tatlı!" dedi Şila.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Toprağı yeniden saksıya doldurdu"
   - Cümle 9: «Toprağı yeniden saksıya doldurdu.»
   - Açıklama: Çözüm özür, saksıyı kaldırma, süpürme, doldurma ve bal verme gibi ikiden fazla adıma yayılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee kahvaltıdan kalan balı"
   - Cümle 10: «Pepee kahvaltıdan kalan balı bir ekmeğe sürdü ve Şila'ya verdi.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunu çözmüyor, özür ve süpürmeden sonra işlevsiz bir ek olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee kahvaltıdan kalan balı bir ekmeğe sürdü"
   - Cümle 10: «Pepee kahvaltıdan kalan balı bir ekmeğe sürdü ve Şila'ya verdi.»
   - Açıklama: Bal ve ekmek sebepsiz beliriyor ve barışmayı temizlik yerine bal getiriyor gibi görünüyor.
   - Açıklama: Bal ve ekmek sebepsizce beliriyor ve barışmayı çözümden koparıp işlevsiz bir ek adım getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0164` birebir aynı, ardından `@onarim: dea738472249e11968f0254fc927c2ea014cabce`, sonra gövde.
