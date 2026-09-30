# Editör görevi (onarım): Pepee, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0110 (deneme 1 -> 2)

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
Ormanda, ağaçların arasında gizli bir açıklık vardı. Pepee iki çalının arasından sokulup açıklığa geldi. Orada ilk kez tek ayak üstünde durmayı denedi ama hemen sallandı. Kolları iki yanında aşağıda duruyordu. Pepee biraz düşündü. Dans ederken kolları hep yukarıda olurdu. Pepee kollarını dansındaki gibi iki yana açtı. Sonra bir ayağını yavaşça kaldırdı. Bu kez hiç sallanmadı. Pepee bir, iki, üç, dört, beş diye saydı. Sonra öbür ayağıyla da denedi ve yine durabildi. Pepee çok sevindi, çünkü tek ayak üstünde durmayı başarmıştı.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee iki çalının arasından sokulup açıklığa geldi"
   - Cümle 2: «Pepee iki çalının arasından sokulup açıklığa geldi.»
   - Açıklama: Çocuğun ormanda tek başına çalıların arasından gizli bir yere sokulması taklit edilince tehlikeli.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki çalının arasından sokulup açıklığa"
   - Cümle 2: «Pepee iki çalının arasından sokulup açıklığa geldi.»
   - Açıklama: 'Sokulmak' bir yerin içine girmeyi anlatır, 'arasından' ile uyuşmuyor; 'geçip' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki çalının arasından sokulup"
   - Cümle 2: «Pepee iki çalının arasından sokulup açıklığa geldi.»
   - Açıklama: 'Sokulmak' burada yanlış anlamda; 'geçip' olmalı.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ilk kez tek ayak üstünde durmayı denedi"
   - Cümle 3: «Orada ilk kez tek ayak üstünde durmayı denedi ama hemen sallandı.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama burada ormanda gizli bir açıklıkta yalnız deniyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Orada ilk kez tek ayak üstünde durmayı denedi"
   - Cümle 3: «Orada ilk kez tek ayak üstünde durmayı denedi ama hemen sallandı.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener; burada ormanda gizli bir açıklıkta yalnız deniyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Dans ederken kolları hep yukarıda olurdu"
   - Cümle 6: «Dans ederken kolları hep yukarıda olurdu.»
   - Açıklama: Dansta kolların yukarıda olduğu söyleniyor ama Pepee kollarını dansındaki gibi iki yana açıyor.
   - Açıklama: Dansta kollar yukarıda deniyor ama Pepee dansındaki gibi diye kollarını iki yana açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0110` birebir aynı, `@degisim: su -> çalı` (tutuyorsan), ardından `@onarim: bd724efab8a5edc4b89f67a0f54e1e1ea8da047d`, sonra gövde.

### Hikâye 2: tohum pepee-0112 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Şila
@tohum: pepee-0112
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: bir şey yapmak
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'köpük', fiil 'çözmek', sıfat 'enerjik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | park | Şila
@plan: köpük halkası evde kalmıştı | kahvaltıdaki kamışı sabunlu suya batırıp üfledi
@tohum: pepee-0112
Bir sabah Pepee ile Şila parkta kahvaltı yapıyordu. Şila çantasının ipini çözdü ve bir şişe sabunlu su çıkardı. Ama köpük halkası evde kalmıştı ve köpük yapamadılar. Şila üzülerek şişeye baktı. Pepee meyve suyunun kamışını aldı. Onun bir ucunu sabunlu suya batırdı. Sonra öbür ucundan yavaşça üfledi. Küçük köpükler çıktı ve havaya uçtu. Enerjik Şila onların arkasından koşup zıpladı. Sonra Pepee kamışı Şila'ya verdi. İkisi parkta sırayla köpük yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Pepee ile Şila parkta kahvaltı yapıyordu"
   - Cümle 1: «Bir sabah Pepee ile Şila parkta kahvaltı yapıyordu.»
   - Açıklama: Tohumdaki kahvaltı sevgisi yalnız ortam olarak geçiyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Onun bir ucunu sabunlu suya batırdı"
   - Cümle 6: «Onun bir ucunu sabunlu suya batırdı.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyi bir büyüğün yanında dener; burada büyük yokken içme kamışıyla sabunlu su deneniyor ve taklit eden çocuk sabunlu suyu yutabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0112` birebir aynı, ardından `@onarim: 5a6940b9773f6dd61d4b9b1864ba7a485463ce6c`, sonra gövde.

### Hikâye 3: tohum pepee-0113 (deneme 1 -> 2)

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
@plan: ağacın altına girince gölgesi kayboldu | dans ederek güneşli çiçeklere gitti
@tohum: pepee-0113
@degisim: halı -> gölge
Bir sabah Pepee ormanda gölgesiyle oyun oynuyordu. Pepee el salladı, gölgesi de otların üstünde el salladı. Ama Pepee büyük bir ağacın altına girince gölgesi kayboldu. Pepee otlara baktı ama gölgesi yoktu. Ağacın altına hiç güneş gelmiyordu. İleride güneş çiçeklerin üstünde parıldıyordu. Pepee dans ederek ağacın altından çıktı ve çiçeklere gitti. Gölgesi otların üstünde hemen geri geldi. Sonra Pepee yeni bir dans yaptı ve tek ayak üstünde döndü. Gölgesi de aynı dansı yaptı. Pepee çok sevindi, çünkü gölgesini yeniden bulmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee dans ederek ağacın altından çıktı"
   - Cümle 7: «Pepee dans ederek ağacın altından çıktı ve çiçeklere gitti.»
   - Açıklama: Tohumdaki dans özelliği sorunu çözmüyor; gölge güneşe çıkınca geri geliyor, dans yalnız süs olarak geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Pepee yeni bir dans yaptı"
   - Cümle 9: «Sonra Pepee yeni bir dans yaptı ve tek ayak üstünde döndü.»
   - Açıklama: Tohumdaki dans özelliği bir kez değil, sorun çözüldükten sonra yeniden kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0113` birebir aynı, `@degisim: halı -> gölge` (tutuyorsan), ardından `@onarim: 390fc44234550e92084e9de44646d1e9b206c0cd`, sonra gövde.

### Hikâye 4: tohum pepee-0114 (deneme 1 -> 2)

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
@plan: kum atılırken patik kumun altında kaldı | kumun her yerine basarak dans etti
@tohum: pepee-0114
Pepee ile Bebee deniz kıyısında kumla oynuyordu. Bebee patiğini çıkarıp yanına koymuştu. Ama Bebee kum atarken patiği kumun altında kaldı ve kayboldu. "Patiğim nerede?" diye sordu Bebee. Pepee kuma baktı ama patik yoktu. "Bebee, gel, kumun her yerine basarak dans edelim!" dedi Pepee. İkisi el ele tutuştu ve küçük adımlarla dans etti. Bebee sağa sola sallandı ve güldü. Birden Pepee'nin ayağı yumuşak bir şeye değdi. Pepee kumu eliyle açtı ve pembe patiği buldu. Patiği Bebee'nin ayağına giydirdi ve incecik ipini bağladı. "Teşekkürler, Pepee!" dedi Bebee. İkisi kumda oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kumun her yerine basarak dans edelim"
   - Cümle 6: «"Bebee, gel, kumun her yerine basarak dans edelim!" dedi Pepee.»
   - Açıklama: Kaybolan patiği bulmak için kumu kazmak yerine dans etmek sebebe doğrudan yönelmiyor ve patik tesadüfen bulunuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee kumu eliyle açtı"
   - Cümle 10: «Pepee kumu eliyle açtı ve pembe patiği buldu.»
   - Açıklama: Kum 'açılmaz'; 'kumu eliyle kazdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0114` birebir aynı, ardından `@onarim: a045d5cf3546c3f0713415eab0623caf0ebf9d0b`, sonra gövde.

### Hikâye 5: tohum pepee-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0115
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: kaybolan eşya
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'havuç', fiil 'koklamak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: havuç yırtık çantadan düşüp kayboldu | aynı dansı yeniden yapıp havucu buldu
@tohum: pepee-0115
@degisim: koklamak -> aramak
Deniz kıyısında Pepee kumdan büyük bir yüz yapıyordu. Yüzün burnu için çantasına bir havuç koymuştu. Ama çanta yırtıktı ve havuç delikten düşüp kaybolmuştu. Pepee havucu kumun üstünde aradı ama bulamadı. Az önce bu yüzün etrafında dans edip dönmüştü. Pepee aynı dansı yeniden yaptı ve aynı yerlerden geçti. İki kez döndü ve bir kez zıpladı. Tam orada kumun içinde turuncu bir uç gördü. Pepee havucu kumdan çekip çıkardı. Havucu silkti ve yüzün tam ortasına taktı. Pepee burnu olan kum yüzüyle oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İki kez döndü ve bir kez zıpladı"
   - Cümle 7: «İki kez döndü ve bir kez zıpladı.»
   - Açıklama: Dans hareketleri havucu bulmaya yaramaz; havuç tam dansın bittiği yerde sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0115` birebir aynı, `@degisim: koklamak -> aramak` (tutuyorsan), ardından `@onarim: 7ba7ccbdd92dee01044ba708c5ac3bf797ac485e`, sonra gövde.

### Hikâye 6: tohum pepee-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0116
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: sırayla oynamak
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'brokoli', fiil 'görüşmek', sıfat 'tatlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: ikisi aynı anda attı ve kozalaklar havada çarpıştı | dedesine sordu ve sırayla atmayı öğrendi
@tohum: pepee-0116
@degisim: görüşmek -> atmak
Rüzgar ağaçların yapraklarını hafifçe sallıyordu. Pepee ile Dedee kozalakları brokoliye benzeyen yuvarlak bir çalıya atıyordu. Ama ikisi aynı anda attı ve kozalaklar havada çarpıştı. "Dedeciğim, kozalaklar neden düşüyor?" diye sordu Pepee. "Aynı anda atıyoruz, sırayla atalım," dedi Dedee. Pepee bunu hemen öğrendi ve ilk kozalağı attı. Kozalak çalının tam ortasına düştü. "Sıra sende, Dedee!" dedi Pepee. Dedee tatlı bir sesle güldü ve o da attı. Onun kozalağı da tam ortaya düştü. İkisi sırayla atmaya devam etti ve her kozalak çalıya girdi. "Sırayla oynamak çok eğlenceli, Dedee!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kozalaklar neden düşüyor"
   - Cümle 4: «"Dedeciğim, kozalaklar neden düşüyor?" diye sordu Pepee.»
   - Açıklama: Sorun kozalakların havada çarpışması iken Pepee düşmelerini soruyor; soru sorunla örtüşmüyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee bunu hemen öğrendi"
   - Cümle 6: «Pepee bunu hemen öğrendi ve ilk kozalağı attı.»
   - Açıklama: Bir öneriyi kabul etmek için 'öğrendi' fiili doğru anlamda kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0116` birebir aynı, `@degisim: görüşmek -> atmak` (tutuyorsan), ardından `@onarim: 3ab0fb32e7abc3c7f28c0eb0442681f158591794`, sonra gövde.

### Hikâye 7: tohum pepee-0118 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0118
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: kaybolan eşya
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'taç', fiil 'serinletmek', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: taç dalın altında başından kaydı ve kayboldu | zıplayıp sallanarak dans edince taç sırtından düştü
@tohum: pepee-0118
Hafif bir rüzgar esti ve Pepee'yi serinletti. Pepee ormanda sarı çiçeklerden yaptığı tacıyla yürüyordu. Ama alçak bir dalın altından geçerken taç başından kaydı ve kayboldu. Pepee çamurlu yola ve çiçeklerin arasına baktı. Ama tacını hiçbir yerde göremedi. Pepee üzülmek yerine zıplayarak ve sallanarak dans etti. Birden sırtından yere sarı bir şey düştü. Bu onun tacıydı, sırtında takılı kalmıştı. Pepee tacı yerden aldı ve başına yeniden taktı. Sonra ormanda tacıyla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Ama tacını hiçbir yerde"
   - Cümle 5: «Ama tacını hiçbir yerde göremedi.»
   - Açıklama: Art arda iki cümle gereksiz yere 'Ama' ile başlıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Pepee üzülmek yerine zıplayarak ve sallanarak dans etti"
   - Cümle 6: «Pepee üzülmek yerine zıplayarak ve sallanarak dans etti.»
   - Açıklama: Pepee tacı aramak için bir şey yapmıyor; taç tesadüfen bulunuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee üzülmek yerine zıplayarak ve sallanarak dans etti"
   - Cümle 6: «Pepee üzülmek yerine zıplayarak ve sallanarak dans etti.»
   - Açıklama: Dans etmek tacı aramaya yönelik değil; taç tesadüfen bulunuyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Birden sırtından yere sarı bir şey düştü"
   - Cümle 7: «Birden sırtından yere sarı bir şey düştü.»
   - Açıklama: Çözüm sebebe yönelmiyor, dans sırasında şans eseri geliyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden sırtından yere sarı bir şey düştü"
   - Cümle 7: «Birden sırtından yere sarı bir şey düştü.»
   - Açıklama: Çözüm figürün eyleminden değil şanstan geliyor.
   - Açıklama: Çözüm önceki olaydan çıkmıyor, sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0118` birebir aynı, ardından `@onarim: 9b7bd18a9dce511b77cc75789f70048ccb60bdcc`, sonra gövde.

### Hikâye 8: tohum pepee-0119 (deneme 1 -> 2)

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
Küçük dalgalar kumda hafif bir ses çıkarıyordu. Pepee su kenarında en özel oyuncağı olan küçük teknesiyle oynuyordu. Ama tekne çok hafifti ve dalgalar gelince hep devrildi. Pepee tekneyi üç kez düzeltti ama olmadı. Sonra yeni bir şey denedi. Kumdan düz ve küçük bir taş aldı. Taşı teknenin tam ortasına koydu. Bir dalga geldi ama tekne bu kez dik kaldı. Tekne dalgaların üstünde sallanarak yüzdü. Pepee taşın tekneyi sağlam tuttuğunu öğrendi. Pepee çok sevindi, çünkü teknesiyle yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "en özel oyuncağı olan küçük teknesiyle"
   - Cümle 2: «Pepee su kenarında en özel oyuncağı olan küçük teknesiyle oynuyordu.»
   - Açıklama: Kartta Pepee'nin en özel oyuncağı olan bir tekne yok; karta eşya ekleniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra yeni bir şey denedi"
   - Cümle 5: «Sonra yeni bir şey denedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada su kenarında yalnız deniyor.
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kenarında yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0119` birebir aynı, `@degisim: tanımak -> denemek` (tutuyorsan), ardından `@onarim: 5da57d94b988e3b91f72f6246edacf8df6086f73`, sonra gövde.

### Hikâye 9: tohum pepee-0120 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Annee
@tohum: pepee-0120
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'ruj', fiil 'fışkırmak', sıfat 'çilekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | park | Annee
@plan: damlalardaki renkler hemen kayboldu | güneşe arkasını dönüp şişeden su fışkırttı
@tohum: pepee-0120
@degisim: ruj -> damla
Bir sabah Pepee ile Annee parkta kahvaltı yapıyordu. Annee su şişesini sıktı ve su havaya fışkırdı. Güneşte damlalar renk renk parladı ama hemen yere düştü. Pepee o renkleri yine görmek istedi. Çilekli ekmeğini bıraktı ve su şişesini aldı. Güneşe arkasını döndü ve şişeyi havaya doğru sıktı. Su yine fışkırdı ve havada küçük damlalar uçuştu. Damlalar kırmızı, sarı ve mavi renklerle parladı. Annee sevinçle ellerini çırptı. Pepee şişeyi Annee'ye verdi ve o da su fışkırttı. İkisi renkli damlalar yapıp kahvaltılarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee ile Annee parkta kahvaltı yapıyordu"
   - Cümle 1: «Bir sabah Pepee ile Annee parkta kahvaltı yapıyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız ortam olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız dekor olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Güneşe arkasını döndü ve şişeyi havaya doğru sıktı"
   - Cümle 6: «Güneşe arkasını döndü ve şişeyi havaya doğru sıktı.»
   - Açıklama: Sebep damlaların hemen düşmesi olarak verilmiş ama çözüm bu sebebe yönelmiyor; üstelik renkler ilk fışkırtmada da zaten görünmüştü.
   - Açıklama: Renklerin kaybolma sebebi damlaların hemen düşmesi; çözüm bu sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0120` birebir aynı, `@degisim: ruj -> damla` (tutuyorsan), ardından `@onarim: cf514ce02f4fcfb0f340ceb3999104dd0c6a9aec`, sonra gövde.

### Hikâye 10: tohum pepee-0121 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0121
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'piyano', fiil 'paylaşmak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: birden ormanda tatlı bir koku geldi | kokuyu kahvaltıdan tanıdı ve ağacın arkasına gitti
@tohum: pepee-0121
@degisim: piyano -> örtü
Pepee ormanda çiçek topluyordu. Dedee biraz ileride bir ağacın arkasında çok meşguldü. Birden rüzgarla tatlı bir koku geldi. Pepee kokunun nereden geldiğini çok merak etti. Havayı kokladı ve bu kokuyu kahvaltıdan tanıdı. Bu, tahin ile pekmezin kokusuydu! Pepee kokunun peşinden ağaca doğru yürüdü. Ağacın arkasında Dedee yere bir örtü sermişti. Örtünün üstünde yumurta, bal ve bir kase tahin pekmez vardı. "Dedeciğim, bu koku buradan mı geliyordu?" diye sordu Pepee. "Evet, sana sürpriz bir kahvaltı hazırladım," dedi Dedee. Pepee dedesine sıkıca sarıldı. İkisi örtüye oturdu ve kahvaltıyı mutlu mutlu paylaştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağacın arkasında çok meşguldü"
   - Cümle 2: «Dedee biraz ileride bir ağacın arkasında çok meşguldü.»
   - Açıklama: 'Meşgul' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgarla tatlı bir koku geldi"
   - Cümle 3: «Birden rüzgarla tatlı bir koku geldi.»
   - Açıklama: Tatlı bir koku gelmesi bir sorun değil; ortada çözülmesi gereken bir dert yok.
   - Açıklama: Tatlı bir koku gelmesi çözülmesi gereken bir sorun değil, yalnız bir merak ve sürpriz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0121` birebir aynı, `@degisim: piyano -> örtü` (tutuyorsan), ardından `@onarim: 4cf077bb44abfce6ac1fe066a34583ac166567be`, sonra gövde.

### Hikâye 11: tohum pepee-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0122
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'fıçı', fiil 'sığmak', sıfat 'tertemiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: koşarken kuzeninin havlusunun üstüne kum saçtı | özür diledi, havluyu silkti ve komik bir dans yaptı
@tohum: pepee-0122
@degisim: fıçı -> havlu
Bir sabah Pepee ile Şila deniz kıyısında oynuyordu. Şila yeni havlusunu kumun üstüne serdi. Pepee koşarken dikkat etmedi ve havlunun üstüne kum saçtı. Şila havluya baktı ve çok üzüldü. Pepee hemen Şila'nın yanına gitti ve ondan özür diledi. Sonra havluyu iki ucundan tuttu ve güzelce silkti. Kumlar yere döküldü ve havlu yine tertemiz oldu. Ama Şila daha gülmüyordu. Pepee onu güldürmek için komik bir dans yaptı. Kollarını salladı ve kumda yan yan yürüdü. Şila kahkaha attı ve o da dansa katıldı. Sonra ikisi küçük havluya sığdı ve mutlu mutlu dalgaları seyretti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee onu güldürmek için komik bir dans yaptı"
   - Cümle 9: «Pepee onu güldürmek için komik bir dans yaptı.»
   - Açıklama: Çözüm özür, silkme ve dans olmak üzere üç adıma uzuyor.
   - Açıklama: Çözüm özür, silkeleme ve dans olmak üzere üç adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0122` birebir aynı, `@degisim: fıçı -> havlu` (tutuyorsan), ardından `@onarim: cb22e516ba043d0b11a8085f0f43e5f4e70e7d40`, sonra gövde.

### Hikâye 12: tohum pepee-0123 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0123
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'fıstık', fiil 'sallamak', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: torbayı hızlıca salladı ve fıstıklar kuma döküldü | özür diledi ve kabuğu açmayı öğrendi
@tohum: pepee-0123
Güneş deniz kenarındaki kumu ısıtıyordu. Pepee ile Nenee kumda oturup kabuğu olan fıstıklar yiyordu. Pepee sormadan fıstık torbasını hızlıca salladı ve fıstıklar kuma döküldü. Nenee kuma baktı ve biraz üzüldü. "Özür dilerim, nineciğim," dedi Pepee. Sonra fıstıkları tek tek kumdan topladı. "Bunların üstü kum oldu, yine yenir mi?" diye sordu Pepee. "Fıstık kabuğun içinde saklı, o yüzden temiz kaldı," dedi Nenee. Nenee bir kabuğu iki parmağıyla açıp gösterdi. Pepee de bir fıstığı aynı biçimde sıktı. Kabuk açıldı ve içinden temiz bir fıstık çıktı. Pepee çok sevindi, çünkü fıstık açmayı öğrenmişti ve Nenee ona gülümsüyordu.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür diledi ve kabuğu açmayı öğrendi"
   - Cümle 0 (plan satırı): «torbayı hızlıca salladı ve fıstıklar kuma döküldü | özür diledi ve kabuğu açmayı öğrendi»
   - Açıklama: Dökülen fıstıklar kabuk açmayı öğrenerek değil kumdan toplanarak çözülüyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "özür diledi ve kabuğu açmayı öğrendi"
   - Cümle 0 (plan satırı): «torbayı hızlıca salladı ve fıstıklar kuma döküldü | özür diledi ve kabuğu açmayı öğrendi»
   - Açıklama: Kabuk açmayı öğrenmek fıstıkların kuma dökülmesi sebebine yönelmiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kabuğu olan fıstıklar yiyordu"
   - Cümle 2: «Pepee ile Nenee kumda oturup kabuğu olan fıstıklar yiyordu.»
   - Açıklama: Bütün fıstık 3-6 yaş için boğulma tehlikesi taşır ve kuma dökülen yiyeceğin yenmesi örnek alınabilir.
   - Açıklama: Fıstık 3-6 yaş için boğulma riski taşıyan bir yiyecek ve kuma dökülen yiyeceği yeme örnek alınabilir.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bunların üstü kum oldu"
   - Cümle 7: «"Bunların üstü kum oldu, yine yenir mi?" diye sordu Pepee.»
   - Açıklama: Fıstıkların üstü kum olmaz; 'kumlu oldu' ya da 'kum bulaştı' olmalı.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Bunların üstü kum oldu, yine yenir mi?"
   - Cümle 7: «"Bunların üstü kum oldu, yine yenir mi?" diye sordu Pepee.»
   - Açıklama: Dökülme sorunu toplanınca çözülüyor, ardından fıstıkların yenip yenmeyeceği ikinci bir sorun olarak açılıyor.
6. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Fıstık kabuğun içinde saklı, o yüzden temiz kaldı"
   - Cümle 8: «"Fıstık kabuğun içinde saklı, o yüzden temiz kaldı," dedi Nenee.»
   - Açıklama: İkinci sorunu Pepee değil Nenee açıklayıp çözüyor.
7. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Fıstık kabuğun içinde saklı"
   - Cümle 8: «"Fıstık kabuğun içinde saklı, o yüzden temiz kaldı," dedi Nenee.»
   - Açıklama: Fıstıkların temiz olduğunu çözen bilgiyi Pepee değil Nenee veriyor ve gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0123` birebir aynı, ardından `@onarim: a565e8bd169f87dbf5af21985200b2f98d9247f9`, sonra gövde.
