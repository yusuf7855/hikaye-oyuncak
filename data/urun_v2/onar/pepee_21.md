# Editör görevi (onarım): Pepee, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0044 (deneme 5 -> 6)

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
Pepee deniz kıyısında, sudan uzakta kovasıyla ıslak kumdan bir kule yapıyordu. Islak kum yapışkandı ve kule dimdik duruyordu. Birden yağmur başladı ve damlalar kulenin tepesini dağıttı. Pepee kulesini yağmurdan korumak istedi. Kovayı kaldırdı ve kulenin üstüne ters kapattı. Artık damlalar kovanın üstüne düşüyordu. Pepee kovanın yanına çömeldi ve bekledi. Yağmur kısa sürdü ve biraz sonra dindi. Pepee kovayı yavaşça çekti. Kule yerinde sağlam duruyordu ve daha fazla dağılmamıştı. Pepee çok sevindi, çünkü kovayla kulesini korumayı öğrenmişti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kovanın yanına çömeldi ve bekledi"
   - Cümle 7: «Pepee kovanın yanına çömeldi ve bekledi.»
   - Açıklama: Güvenli kullanım satırı yeni şeyleri bir büyüğün yanında denemesini söylüyor; Pepee yağmurda deniz kıyısında yalnız kalıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kovayla kulesini korumayı öğrenmişti"
   - Cümle 11: «Pepee çok sevindi, çünkü kovayla kulesini korumayı öğrenmişti.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0044` birebir aynı, `@degisim: çikolata -> kova` (tutuyorsan), ardından `@onarim: e89f1b98e9b4481b8d7761809cc79b1bedff1e71`, sonra gövde.

### Hikâye 2: tohum pepee-0045 (deneme 5 -> 6)

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
@plan: kağıttan zincir öbür sandalyeye ulaşmadı | üç halka daha yapıp zinciri uzattı
@tohum: pepee-0045
@degisim: kamera -> kağıt
Yağmur cama tık tık vuruyordu. Pepee odasında kardeşi Bebee için kağıttan renkli bir zincir yapmıştı. Zinciri iki sandalyenin arasına asmak istedi. Ama zincir kısaydı ve öbür sandalyeye ulaşmadı. Pepee masadaki kağıtlara baktı. Kağıttan halka yapmayı yeni öğrenmişti. Hemen üç halka daha yaptı ve zincire ekledi. Şimdi zincir iki sandalyeye de ulaştı. Pepee zinciri astı ve Bebee'yi çağırdı. Bebee odaya geldi ve zincirin altında oynak bir dans yaptı. "Bu zincir benim için mi?" diye sordu Bebee. "Evet, Bebee, senin için yaptım," dedi Pepee. "Çok güzel olmuş, teşekkür ederim, Pepee!" dedi Bebee.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama zincir kısaydı ve öbür sandalyeye ulaşmadı"
   - Cümle 4: «Ama zincir kısaydı ve öbür sandalyeye ulaşmadı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oynak bir dans yaptı"
   - Cümle 10: «Bebee odaya geldi ve zincirin altında oynak bir dans yaptı.»
   - Açıklama: 'Oynak' dans için alışılmadık ve 3 yaşındaki çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0045` birebir aynı, `@degisim: kamera -> kağıt` (tutuyorsan), ardından `@onarim: 977273166b205e3a55d5bf2218c876d869c54a34`, sonra gövde.

### Hikâye 3: tohum pepee-0057 (deneme 4 -> 5)

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
@plan: pastaya koyacak parlak bir süs yoktu | parlayan kumu eliyle serpti ve kabuktaki inciyi buldu
@tohum: pepee-0057
@degisim: yardımsever -> parlak
Pepee deniz kıyısında, sudan uzakta kumdan bir pasta yapıyordu. Pastanın tepesine parlak bir süs koymak istiyordu. Ama etrafta yalnız gri taşlar vardı. Pepee süs bulmak için kuma dikkatle baktı. Kumun içinde küçük bir şey parlıyordu. Pepee bunun ne olduğunu çok merak etti. Parlayan yerden bir avuç kum aldı. Kumu parmaklarının arasından yavaşça serpti. Avucunda küçük bir kabuk kaldı. Kabuğun içinde beyaz bir inci vardı! Pepee ilk kez gerçek bir inci görüyordu. İnciyi pastanın tepesine koydu. Pasta artık çok güzel olmuştu. Pepee o sabah kabukların içinde inci olabileceğini öğrendi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumun içinde küçük bir şey parlıyordu"
   - Cümle 5: «Kumun içinde küçük bir şey parlıyordu.»
   - Açıklama: Çözümü getiren parlak inci sebepsizce, tesadüfen beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0057` birebir aynı, `@degisim: yardımsever -> parlak` (tutuyorsan), ardından `@onarim: 8a0761cffa718ba462ab29ce1ba3b547e13c0bec`, sonra gövde.

### Hikâye 4: tohum pepee-0062 (deneme 4 -> 5)

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
@plan: yakından garip bir ses duyuldu | dikkatle dinledi ve sesin karnından geldiğini buldu
@tohum: pepee-0062
Ormanda hava serindi. Pepee çantasıyla ağaçların arasında yürüyordu. Birden yakından garip bir ses duyuldu. Pepee bu sesi çok merak etti. Sağlam bir kütüğe oturdu ve dikkatle dinledi. Ses çok yakındı. Pepee elini karnına koydu. Ses onun karnından geliyordu! Pepee daha kahvaltı yapmamıştı ve acıkmıştı. Hemen çantasından ballı ekmeğini ve yumurtasını çıkardı. Ekmekten büyük bir lokma aldı ve yumurtasını da yedi. Karnından artık hiç ses gelmedi. Pepee kahvaltısını bitirince kütükten kalktı. Pepee çok sevindi, çünkü garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses onun karnından geliyordu!"
   - Cümle 8: «Ses onun karnından geliyordu!»
   - Açıklama: Pepee'nin kendi karnının sesini yakından gelen garip bir ses sanması zayıf ve inandırıcılığı düşük bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0062` birebir aynı, ardından `@onarim: 2366ce6f90e655885406fe9d3851a3b4aa2ea33e`, sonra gövde.

### Hikâye 5: tohum pepee-0067 (deneme 3 -> 4)

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
@degisim: rengarenk -> yumuşak
Küçük dalgalar kıyıda ses çıkarıyordu. Pepee ile Bebee kumda topaç oyunu oynuyordu. İkisi dönerek birbirine yaklaşmak ve ellerini birleştirmek istiyordu. Ama ayakları yumuşak kuma battı. "Pepee, ayaklarım battı!" dedi Bebee. Pepee etrafına baktı. Biraz ileride kum düz ve sertti. "Gel, Bebee, orada dönelim!" dedi Pepee. İkisi hemen oraya yürüdü. Pepee kollarını açtı ve dans ederek döndü. Bebee de ona bakıp kendi yerinde döndü. Ayakları bu kez hiç batmadı. Kardeşler dönerek yaklaştı ve ellerini birleştirdi. İkisi birbirine sarıldı. Pepee ile Bebee gülerek oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ayakları yumuşak kuma battı"
   - Cümle 4: «Ama ayakları yumuşak kuma battı.»
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0067` birebir aynı, `@degisim: rengarenk -> yumuşak` (tutuyorsan), ardından `@onarim: 3e1de341ee2aa5481678e718f0141024e58b486a`, sonra gövde.

### Hikâye 6: tohum pepee-0068 (deneme 3 -> 4)

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
Deniz kıyısında serin bir rüzgar esiyordu. Pepee kovayla kumdan bir kale yapıyordu. Ama kuru kum kovadan çıkınca hemen dağıldı. Pepee üzüldü ve somurtkan bir yüzle kumda oturdu. "Ne oldu, Pepee?" diye sordu Şila. "Kum hep dağılıyor," dedi Pepee. Pepee sonra su kenarına baktı. Oradaki ıslak kumda Şila'nın ayak izleri duruyordu. Pepee kovayı ıslak kumla doldurdu ve ters çevirdi. Bu kez güzel bir kale çıktı. Şila küçük taşlar getirdi. Pepee taşları kalenin üstüne tek tek sıraladı. "Ne güzel bir kale, Pepee!" dedi Şila. Pepee o gün kaleyi ıslak kumla yapmayı öğrendi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "somurtkan bir yüzle kumda"
   - Cümle 4: «Pepee üzüldü ve somurtkan bir yüzle kumda oturdu.»
   - Açıklama: 'Somurtkan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0068` birebir aynı, `@degisim: çan -> kova` (tutuyorsan), ardından `@onarim: c5d13b4b1de409302ad7f23959bd57246e04a544`, sonra gövde.

### Hikâye 7: tohum pepee-0070 (deneme 3 -> 4)

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
@plan: küçük dalgalar örtüye yaklaştı | örtüyü kuru ayakkabıların yanına taşıdı
@tohum: pepee-0070
Güneş parlıyordu ve deniz ışıltılıydı. Pepee su kenarında dedesine sürpriz bir kahvaltı hazırlıyordu. Ama küçük dalgalar gelip örtüye yaklaştı. Örtünün ucu ıslandı. Pepee etrafına baktı. Dedee biraz uzakta gözleri kapalı bekliyordu. Dedee'nin ayakkabıları da oradaki kumda duruyordu. Ayakkabılar kuruydu, çünkü dalga oraya gelmiyordu. Pepee örtüyü ve her şeyi ayakkabıların yanına taşıdı. Artık örtü hiç ıslanmadı. Sonra Dedee gözlerini açtı. Sürprizi görünce güldü ve Pepee'ye sarıldı. İkisi kumda oturup balı ve yumurtayı paylaştı. Pepee bundan sonra sofrayı hep kuru kumda kurdu.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "örtüyü kuru ayakkabıların yanına taşıdı"
   - Cümle 0 (plan satırı): «küçük dalgalar örtüye yaklaştı | örtüyü kuru ayakkabıların yanına taşıdı»
   - Açıklama: Planda örtüyü figür taşıyor ama gövdede Dedee taşıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee bundan sonra sofrayı"
   - Cümle 14: «Pepee bundan sonra sofrayı hep kuru kumda kurdu.»
   - Açıklama: Geçmiş anlatımda 'bundan sonra' yerine 'o günden sonra' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0070` birebir aynı, ardından `@onarim: 907eaae3c6414de4afba2dedd49672bc17dcc6e8`, sonra gövde.

### Hikâye 8: tohum pepee-0073 (deneme 3 -> 4)

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
@plan: dans yeri kuru dallarla doluydu | dalları tek tek toplayıp kenara taşıdı
@tohum: pepee-0073
@degisim: çekirdek -> çiçek
Pepee ormanda kardeşi Bebee için bir dans hazırlıyordu. Bebee bir ağacın arkasında gözlerini kapatıp bekliyordu. Ama yer kuru dallarla doluydu ve dallar ayağa takılıyordu. Pepee dalları tek tek topladı ve kenara taşıdı. Çiçeklerin arasındaki yer artık güvenliydi. "Şimdi gözlerini aç, Bebee!" dedi Pepee. Bebee gözlerini açtı. Pepee çimenlerde döndü, zıpladı ve ellerini çırptı. "Ne güzel, Pepee!" dedi Bebee ve güldü. Sonra Pepee kardeşinin elini tuttu ve ikisi birlikte oynayıp çok eğlendi. Pepee çok mutluydu, çünkü kardeşi sevinmişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dallar ayağa takılıyordu"
   - Cümle 3: «Ama yer kuru dallarla doluydu ve dallar ayağa takılıyordu.»
   - Açıklama: İyelik eksik ve 'ayağa' belirsiz; 'Pepee'nin ayağına' gibi olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yer artık güvenliydi"
   - Cümle 5: «Çiçeklerin arasındaki yer artık güvenliydi.»
   - Açıklama: 'Güvenli' soyut bir kavram ve 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0073` birebir aynı, `@degisim: çekirdek -> çiçek` (tutuyorsan), ardından `@onarim: 4408a9cc157630f7f6c411269102a114ed621625`, sonra gövde.

### Hikâye 9: tohum pepee-0074 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0074
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: sırayla oynamak
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'bant', fiil 'yumuşamak', sıfat 'şapkalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: tek bir bant vardı ve ikisi aynı anda istedi | sırayla yapıştırmayı önerdi ve resmi birlikte bitirdiler
@tohum: pepee-0074
@degisim: yumuşamak -> yapıştırmak
Pepee ile Nenee ormanda bir kağıda yapraklardan şapkalı bir mantar yapıyordu. Ama tek bir bant vardı ve ikisi de aynı anda banda uzandı. İkisi bandı birden çekti ve hiçbir yaprak yapışmadı. Pepee biraz düşündü. "Nineciğim, sırayla yapıştıralım mı? Önce sen, sonra ben," dedi Pepee. "Tamam, sen de beni izle ve öğren," dedi Nenee ve güldü. Nenee kağıda büyük sarı bir yaprak koydu ve bandı üstüne bastırdı. Pepee onu dikkatle izledi. Sonra Nenee bandı Pepee'ye verdi. Pepee de küçük kırmızı bir yaprağı mantarın başına yapıştırdı. Sırayla çalışınca mantar çabucak bitti. Pepee ile Nenee bitmiş resme bakıp sevinçle birbirine sarıldı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen de beni izle ve öğren"
   - Cümle 7: «"Tamam, sen de beni izle ve öğren," dedi Nenee ve güldü.»
   - Açıklama: Öğrenme özelliği Pepee'nin çözümünde işe yaramıyor, yalnız ninenin repliğine eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0074` birebir aynı, `@degisim: yumuşamak -> yapıştırmak` (tutuyorsan), ardından `@onarim: cd1427da59c21b95d5dece2d6d3d154eb00b29a1`, sonra gövde.

### Hikâye 10: tohum pepee-0075 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Rüzgar parkta hızlı hızlı esiyordu. Pepee kahvaltı kutusunu kaydırağın yanına koydu ve kaydıraktan kaydı. Dönünce kutusunu göremedi, çünkü sarı yapraklar onun üstünü kaplamıştı. Meraklı Pepee her yere baktı. Kaydırağın yanında büyük bir yaprak yığını vardı. Pepee rüzgarın düşürdüğü kuru bir dalı aldı. Dalla yaprakları yavaş yavaş kenara itti. Yaprakların altından mavi kutusu göründü. Pepee kutuyu açtı ve içine baktı. Balı ve yumurtası yerinde duruyordu. Pepee kutusuna sarıldı ve güldü. Pepee bundan sonra kaybolan şeyleri yaprakların altında da aradı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sarı yapraklar onun üstünü kaplamıştı"
   - Cümle 3: «Dönünce kutusunu göremedi, çünkü sarı yapraklar onun üstünü kaplamıştı.»
   - Açıklama: Kaydıraktan bir kez kayacak kadar kısa sürede yaprakların kutuyu tümüyle örtmesi akla pek yatkın değil ve yaprakları itip bitirmek önemsiz bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0075` birebir aynı, ardından `@onarim: 414977e13a90f786787aa29b430d2251b34f20c6`, sonra gövde.

### Hikâye 11: tohum pepee-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0078
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'minder', fiil 'savurmak', sıfat 'yapraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yapraklar küçük elinden hemen yere düştü | şapkasını yaprakla doldurup yaprakları havaya savurdu
@tohum: pepee-0078
@degisim: minder -> şapka
Ormanda yapraklı ağaçların altına bir sürü sarı yaprak düşmüştü. Pepee yaprakları havaya atıp altında zıplamak istedi. Ama küçük eline iki üç yaprak sığdı ve hepsi hemen düştü. Pepee durdu ve biraz düşündü. Sonra mavi şapkasını çıkardı ve onu yapraklarla doldurdu. Yaprakları şapkadan havaya doğru savurdu. Yapraklar yavaş yavaş başına döküldü. Pepee sevinçle zıpladı ve şapkayı yine doldurdu. Yapraklar bu sefer daha yükseğe uçtu. Sonunda Pepee'nin mavi tulumunun her yerinde yaprak vardı. Pepee çok mutluydu, çünkü yaprakları şapkayla uçurmayı kendisi öğrenmişti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük eline iki üç yaprak sığdı ve hepsi hemen düştü"
   - Cümle 3: «Ama küçük eline iki üç yaprak sığdı ve hepsi hemen düştü.»
   - Açıklama: Yaprakların düşmesi zaten istenen şey olduğundan sorunun ne olduğu belirsiz ve akla yatkın değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yaprakları şapkayla uçurmayı kendisi öğrenmişti"
   - Cümle 11: «Pepee çok mutluydu, çünkü yaprakları şapkayla uçurmayı kendisi öğrenmişti.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama ormanda yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0078` birebir aynı, `@degisim: minder -> şapka` (tutuyorsan), ardından `@onarim: 9f60b47584a8872b1341f42e6a91bf293adfaaeb`, sonra gövde.

### Hikâye 12: tohum pepee-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | -
@tohum: pepee-0081
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'kızak', fiil 'güneşlenmek', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | park | -
@plan: dans ederken her zıplayışta garip bir ses geldi | durup dinledi ve sesi yapan cebindeki taşları buldu
@tohum: pepee-0081
@degisim: kızak -> taş
Parkta güneş parlıyordu. Pepee bankta oturup güneşlenirken yerden iki küçük taş aldı ve cebine koydu. Sonra kalktı ve kaydırağın yanında dans etmeye başladı. Ama her zıpladığında tık tık diye bir ses geliyordu. Pepee bu sesi çok merak etti. Önce aceleci adımlarla bankın arkasına koştu. Orada hiçbir şey yoktu. O durunca ses de durdu. Sonra yavaşça bir kez daha zıpladı ve dinledi. Ses tulumunun cebinden geliyordu. Elini cebine soktu ve iki taşı buldu. Taşlar zıplayınca birbirine vuruyordu. Taşları elinde salladı ve güldü. Pepee çok sevindi, çünkü sesi yapan şeyi kendisi bulmuştu.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Sonra kalktı ve kaydırağın yanında dans etmeye başladı.»
   - Açıklama: Sorun olan tık tık sesi ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Önce aceleci adımlarla bankın"
   - Cümle 6: «Önce aceleci adımlarla bankın arkasına koştu.»
   - Açıklama: 'Aceleci' kişiyi niteler, adıma uymuyor; ayrıca çocuk için soyut.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Önce aceleci adımlarla"
   - Cümle 6: «Önce aceleci adımlarla bankın arkasına koştu.»
   - Açıklama: 'Aceleci' kişilik sıfatı adımlara mecazlı yüklenmiş; 3 yaşındaki çocuğa uygun değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce aceleci adımlarla bankın arkasına koştu"
   - Cümle 6: «Önce aceleci adımlarla bankın arkasına koştu.»
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor, önce ilgisiz bir yere koşuluyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Taşlar zıplayınca birbirine vuruyordu"
   - Cümle 12: «Taşlar zıplayınca birbirine vuruyordu.»
   - Açıklama: Zıplayan Pepee'dir; 'zıplayınca' fiili taşlar öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0081` birebir aynı, `@degisim: kızak -> taş` (tutuyorsan), ardından `@onarim: a78d176c8cd3d14cf13ffe37fa2f9e2da04b3f14`, sonra gövde.
