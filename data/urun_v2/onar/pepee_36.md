# Editör görevi (onarım): Pepee, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0071 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0071
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'koni', fiil 'buluşmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: çiçekler küçük ellerinden düşüyordu | ninesinden yardım istedi ve kağıttan koni yaptı
@tohum: pepee-0071
Kuşlar ağaçlarda ötüyordu. Pepee ormanda renkli çiçekler topluyordu ama çiçekler küçük ellerinden düşüyordu. Pepee büyük ağacın altında Nenee ile buluştu ve ondan yardım istedi. Nenee elmalı kurabiyeleri bir kağıda sarmıştı. Kurabiyeleri çıkardı ve kağıdı açtı. Sonra Pepee'ye kağıttan koni yapmayı gösterdi. Pepee kağıdı yavaşça kıvırdı ve bir koni yaptı. Böylece yeni bir şey öğrendi. Pepee çiçekleri koninin içine tek tek koydu. Artık hiçbir çiçek düşmüyordu. Nenee koniye bakıp güldü. Sonra ikisi ağacın altına oturdu. Pepee ile Nenee elmalı kurabiyeleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ninesinden yardım istedi ve kağıttan koni yaptı"
   - Cümle 0 (plan satırı): «çiçekler küçük ellerinden düşüyordu | ninesinden yardım istedi ve kağıttan koni yaptı»
   - Açıklama: Plan koniyi Pepee'nin yaptığını söylüyor ama gövdede koniyi Nenee yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0071` birebir aynı, ardından `@onarim: fb4a06911d60c3eb3e1dae34fcc185da4071052b`, sonra gövde.

### Hikâye 2: tohum pepee-0087 (deneme 5 -> 6)

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
Pepee ormanda yürürken kar yağmaya başladı. Küçük kar taneleri havada uçuşuyordu. Pepee onların şekline bakmak istedi ama taneler sıcak elinde hemen eriyordu. Pepee durdu ve biraz düşündü. Sonra tulumunun mavi kolunu karın altına uzattı. Kol, sıcak elinden daha soğuktu. Toz gibi ince kar, kolun üstüne yağdı. Taneler bu kez erimedi. Pepee kolunu gözüne yaklaştırdı ve dikkatle baktı. Her tane küçük bir yıldız gibiydi! Pepee çok sevindi, çünkü kar tanesinin şeklini öğrenmişti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ormanda yürürken kar"
   - Cümle 1: «Pepee ormanda yürürken kar yağmaya başladı.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada ormanda yalnız başına deniyor.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "ormanda yürürken kar yağmaya"
   - Cümle 1: «Pepee ormanda yürürken kar yağmaya başladı.»
   - Açıklama: Kartın orman tarifi ağaçlarla ve çiçeklerle dolu bir orman diyor; karlı kış ormanı bu tarife uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0087` birebir aynı, `@degisim: tozlu -> soğuk` (tutuyorsan), ardından `@onarim: fb0e1c7004bd0a7144c4f72c6b40d6026f43bca8`, sonra gövde.

### Hikâye 3: tohum pepee-0093 (deneme 4 -> 5)

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
Bir sabah Pepee deniz kıyısına eski oyuncak süpürgesini getirdi. Sudan uzakta kumdan bir ev ve düz bir bahçe yapmak istedi. Ama kumda ayaklarından kalan bir sürü küçük çukur vardı. Pepee çukurları eliyle kapattı ama her yerde parmak izleri kaldı. Pepee biraz düşündü. Sonra süpürgesini aldı ve bahçenin üstünde ileri geri gezdirdi. Çukurlar doldu, izler de kayboldu ve bahçe dümdüz oldu. Böylece Pepee kumu süpürgeyle düzeltmeyi öğrendi. Sonra bahçeye kabuklardan küçük bir yol yaptı. Pepee kumdan evinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Böylece Pepee kumu süpürgeyle düzeltmeyi öğrendi"
   - Cümle 8: «Böylece Pepee kumu süpürgeyle düzeltmeyi öğrendi.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız başına deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0093` birebir aynı, `@degisim: öğretmek -> düzeltmek` (tutuyorsan), ardından `@onarim: e7df395922f520f4cc86143047f62c50ba087f01`, sonra gövde.

### Hikâye 4: tohum pepee-0094 (deneme 4 -> 5)

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
Pepee evde Bebee ile delikli bir kutuya top atıyordu. Bebee'nin yavaş attığı toplar giriyordu ama Pepee'ninkiler girmiyordu. Pepee kazanmak istedi ve kardeşinin elindeki topu çekip aldı. Bebee çok üzüldü ve ağlamaya başladı. Pepee durdu ve topu ona geri verdi. "Özür dilerim, Bebee. Bana nasıl attığını öğretir misin?" dedi Pepee. Bebee gözlerini sildi ve güldü. "Önce deliğe iyi bak, sonra yavaşça at," dedi Bebee. Pepee kardeşinden öğrendiği gibi topu attı. Top tam içeri girdi. Bebee sevinçle zıpladı. "Teşekkürler, Bebee, şimdi ikimiz de kazanıyoruz!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Bebee'nin yavaş attığı toplar giriyordu ama Pepee'ninkiler girmiyordu"
   - Cümle 2: «Bebee'nin yavaş attığı toplar giriyordu ama Pepee'ninkiler girmiyordu.»
   - Açıklama: Kartın ilişki alanında Bebee Pepee ile oynamak için büyümek isteyen küçük kardeştir, burada ise Pepee'ye öğreten usta oyuncu olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0094` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: 23a00e1ed1faf83384a48ae30420351e4561747a`, sonra gövde.

### Hikâye 5: tohum pepee-0095 (deneme 3 -> 4)

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
@plan: kurabiye saklıydı ve nereye bakacağını bilmiyordu | annesine sordu ve sıcak soğuk oyunuyla kurabiyeyi buldu
@tohum: pepee-0095
Pepee parkta annesiyle yeni bir oyun oynuyordu. Annee limonlu bir yulaf kurabiyesini kaydırağın altına sakladı. Ama Pepee nereye bakacağını bilmiyordu ve onu bulamadı. "Anneciğim, kurabiye nerede?" diye sordu Pepee. "Yakına gelince 'sıcak', uzağa gidince 'soğuk' derim," dedi Annee. Sonra Annee oturdu ve onu izledi. Pepee sıcak soğuk oyununu hemen öğrendi ve salıncağa yürüdü. "Soğuk!" dedi Annee. Pepee geri döndü ve kaydırağa koştu. "Sıcak, çok sıcak!" dedi Annee. Pepee kaydırağın altına eğildi ve kurabiyeyi buldu. Onu ikiye böldü ve yarısını annesine verdi. "Anneciğim, bu oyun çok güzel, bir daha oynayalım!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kurabiye saklıydı ve nereye bakacağını bilmiyordu"
   - Cümle 0 (plan satırı): «kurabiye saklıydı ve nereye bakacağını bilmiyordu | annesine sordu ve sıcak soğuk oyunuyla kurabiyeyi buldu»
   - Açıklama: Plan cümlesinde iki yüklemin öznesi aynı görünüyor; 'bilmiyordu' kurabiyeye bağlanıyor, Pepee öznesi eksik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0095` birebir aynı, ardından `@onarim: 2923d930772111884e6c67b25977a683b31fe3dd`, sonra gövde.

### Hikâye 6: tohum pepee-0100 (deneme 4 -> 5)

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
@degisim: ferah -> geniş
Rüzgar ağaçların arasında hafifçe esiyordu. Pepee ile Şila ormanda geniş bir yerde gösteriye hazırlanıyordu. Ama Şila müzik kutusu yerine oyuncak mikroskobunu getirmişti. "Pepee, müzik olmadan nasıl dans edeceğiz?" diye sordu Şila. Pepee biraz düşündü. Sonra ayaklarını yere vurarak dans etmeye başladı. Tap, tap, tap diye güzel bir ses çıktı. Pepee dönerken ellerini de çırptı. "Şila, işte müzik!" dedi Pepee. Şila bu sesle çiçeklerin arasında güzelce dans etti. Pepee ses çıkarmayı hiç bırakmadı. Gösterinin sonunda ikisi birbirini alkışladı. Sonra el ele tutuşup oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yerine oyuncak mikroskobunu getirmişti"
   - Cümle 3: «Ama Şila müzik kutusu yerine oyuncak mikroskobunu getirmişti.»
   - Açıklama: 'Mikroskop' 3 yaşındaki bir çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0100` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: f6d532a8d628d5c9df7418fdd50811f26db8bf60`, sonra gövde.

### Hikâye 7: tohum pepee-0103 (deneme 4 -> 5)

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
@degisim: şeffaf -> sert
Deniz kıyısında Pepee ile Bebee kumun üstünde kahvaltı yapıyordu. Bebee kutusundan bir yumurta aldı. Ama yumurtanın kabuğu çok sertti ve Bebee onu çıkaramadı. "Pepee, bu kabuk nasıl çıkar?" diye sordu Bebee. Pepee yumurtayı aldı ve kahvaltıda hep yaptığı gibi kutunun kapağına hafifçe vurdu. Kabuk küçük küçük çatladı. Sonra Pepee yumurtayı avucunda yavaşça yuvarladı. Çatlaklar yumurtanın çevresinde bir halka oldu. "Şimdi sen dene, Bebee," dedi Pepee. Bebee kabuğun parçalarını tek tek aldı. Kabuğun altından bembeyaz yumurta göründü. Bebee yumurtasını mutlu mutlu yedi. Pepee çok sevindi, çünkü kardeşine yardım etmişti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee ile Bebee kumun üstünde"
   - Cümle 1: «Deniz kıyısında Pepee ile Bebee kumun üstünde kahvaltı yapıyordu.»
   - Açıklama: İki küçük kardeş deniz kıyısında yanlarında bir büyük olmadan yalnız bulunuyor; güvenli kullanım satırı büyüğün yanında olmayı ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0103` birebir aynı, `@degisim: şeffaf -> sert` (tutuyorsan), ardından `@onarim: 6a585e3e9858401a5d65e426ec3759d8e7cd1b94`, sonra gövde.

### Hikâye 8: tohum pepee-0110 (deneme 4 -> 5)

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
Ormanda, iki büyük çalının arasında gizli, düz bir çimenlik vardı. Pepee orada oynuyordu. Tek ayak üstünde durmayı denedi ama hemen sallandı. Elleri ceplerine sokulmuştu. Pepee dansını düşündü. Dans ederken kollarını hep iki yana açardı. Pepee ellerini cebinden çıkardı ve kollarını açtı. Bir ayağını yavaşça kaldırdı. Bu kez hiç sallanmadı. Pepee bir, iki, üç, dört, beş diye saydı. Sonra öbür ayağıyla da denedi ve yine durabildi. Pepee çok sevindi, çünkü tek ayak üstünde durmayı başarmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elleri ceplerine sokulmuştu"
   - Cümle 4: «Elleri ceplerine sokulmuştu.»
   - Açıklama: Edilgen 'sokulmuştu' ellerini başkası sokmuş gibi gösteriyor; 'Elleri cebindeydi' olmalı.
   - Açıklama: Edilgen 'sokulmuştu' öznesine uymuyor; 'Ellerini ceplerine sokmuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0110` birebir aynı, `@degisim: su -> çalı` (tutuyorsan), ardından `@onarim: 66e79d321d51f6d80e52c87ccf85cd90eb065489`, sonra gövde.

### Hikâye 9: tohum pepee-0114 (deneme 4 -> 5)

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
Pepee ile Bebee deniz kıyısında kumla oynuyordu. Bebee patiğini çıkarıp yanına koymuştu. Ama Bebee kum atarken patiği kumun altında kaldı ve kayboldu. "Patiğim nerede?" diye sordu Bebee. Pepee kumun üstüne baktı ama patiği göremedi. "Bebee, gel, oturduğun yerde dans edelim!" dedi Pepee. İkisi el ele tutuştu ve orada küçük adımlarla dans etti. Bebee sağa sola sallandı ve güldü. Az sonra Pepee'nin ayağı kumun altında yumuşak bir şeye değdi. Pepee kumu eliyle kazdı ve pembe patiği buldu. Patiği Bebee'nin ayağına giydirdi ve incecik ipini bağladı. İkisi kumda oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "gel, oturduğun yerde dans edelim"
   - Cümle 6: «"Bebee, gel, oturduğun yerde dans edelim!" dedi Pepee.»
   - Açıklama: Patiği bulmak için kumu kazmak yerine dans ediliyor; çözüm sebebe doğrudan yönelmiyor ve patik tesadüfen bulunuyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "oturduğun yerde dans edelim"
   - Cümle 6: «"Bebee, gel, oturduğun yerde dans edelim!" dedi Pepee.»
   - Açıklama: Çözüm patiği aramaya değil dansa yöneliyor; patik aranmıyor, rastlantıyla bulunuyor.
   - Açıklama: Kumda kaybolan patik için dans etmek sebebe doğrudan yönelmiyor; patik tesadüfen ayağa değiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee'nin ayağı kumun altında yumuşak bir şeye değdi"
   - Cümle 9: «Az sonra Pepee'nin ayağı kumun altında yumuşak bir şeye değdi.»
   - Açıklama: Patik bir aramadan değil sebepsiz bir rastlantıdan çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0114` birebir aynı, ardından `@onarim: 1f019ac1cdfaa4672849c78084ad8d35f93db1ff`, sonra gövde.

### Hikâye 10: tohum pepee-0119 (deneme 4 -> 5)

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
Küçük dalgalar kumda ses çıkarıyordu. Pepee kumda oturmuş, özel oyuncak teknesiyle oynuyordu. Ama tekne çok hafifti ve dalgalar gelince hep devrildi. Pepee tekneyi üç kez düzeltti ama tekne yine devrildi. Sonra biraz düşündü. Tekneye ağır bir taş koymayı denedi. Kumdan düz ve ağır bir taş seçti. Pepee taşı teknenin tam ortasına koydu. Bir dalga geldi ama tekne bu kez dik kaldı. Tekne dalgaların üstünde sallanarak yüzdü. Pepee taşın tekneyi sağlam tuttuğunu öğrendi. Pepee çok sevindi, çünkü teknesiyle yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kumda oturmuş, özel oyuncak teknesiyle oynuyordu"
   - Cümle 2: «Pepee kumda oturmuş, özel oyuncak teknesiyle oynuyordu.»
   - Açıklama: Kartın güvenli özellik kullanımı satırına aykırı olarak Pepee dalgalardaki teknesiyle deniz kıyısında yalnız ve büyük olmadan deneme yapıyor.
   - Açıklama: Dört yaşındaki Pepee deniz kıyısında büyük olmadan tek başına oynuyor ve yeni şey deniyor; güvenli kullanım satırı bir büyüğün yanında denemesini ister.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Tekneye ağır bir taş koymayı denedi"
   - Cümle 6: «Tekneye ağır bir taş koymayı denedi.»
   - Açıklama: Taş koyma eylemi önce özetlenip hemen ardından yeniden anlatılıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0119` birebir aynı, `@degisim: tanımak -> denemek` (tutuyorsan), ardından `@onarim: 38488d0cea7a602bfbeafad6f4f3c837864492c6`, sonra gövde.

### Hikâye 11: tohum pepee-0121 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: ormanda çok ağaç vardı ve dedesini bulamadı | kahvaltı kokusunu tanıdı ve kokuya doğru gitti
@tohum: pepee-0121
@degisim: piyano -> örtü
Pepee ormanda Dedee ile saklambaç oynuyordu. Dedee elinde bir sepetle saklandı. Pepee onu aradı ama ormanda çok ağaç vardı ve dedesini bulamadı. Az sonra ağaçların arasından tatlı bir koku geldi. Pepee havayı kokladı ve bu kokuyu kahvaltıdan tanıdı. Bu, tahin ile pekmezin kokusuydu! Pepee kokuya doğru yürüdü ve büyük bir ağacın arkasına baktı. Dedee'nin iki eli de meşguldü, çünkü yere bir örtü seriyordu. Örtünün üstünde yumurta, bal ve tahin pekmez vardı. "Seni buldum, dedeciğim!" dedi Pepee. "Buldun, sana sürpriz bir kahvaltı hazırladım," dedi Dedee. Pepee dedesine sıkıca sarıldı. İkisi örtüye oturdu ve kahvaltıyı mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iki eli de meşguldü"
   - Cümle 8: «Dedee'nin iki eli de meşguldü, çünkü yere bir örtü seriyordu.»
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dedee'nin iki eli de meşguldü"
   - Cümle 8: «Dedee'nin iki eli de meşguldü, çünkü yere bir örtü seriyordu.»
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dedee'nin iki eli de meşguldü"
   - Cümle 8: «Dedee'nin iki eli de meşguldü, çünkü yere bir örtü seriyordu.»
   - Açıklama: Dedenin ellerinin meşgul olması işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
   - Açıklama: Dedenin ellerinin meşgul olması kurulup hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0121` birebir aynı, `@degisim: piyano -> örtü` (tutuyorsan), ardından `@onarim: e0ca70da6f75a5578b12c06138a9e6c8d9667124`, sonra gövde.

### Hikâye 12: tohum pepee-0124 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0124
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'sünger', fiil 'dizmek', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: yer düz değildi ve yumurtalardan biri kayboldu | parlak izin yanından yürüdü ve yumurtayı ağacın dibinde buldu
@tohum: pepee-0124
@degisim: esnek -> yumuşak
Pepee ormanda kahvaltı yapmak için yere bir örtü serdi. Örtünün üstüne üç yumurtayı yan yana dizdi. Ama yer düz değildi ve yumurtalardan biri kayboldu. Pepee yumurtanın nereye gittiğini çok merak etti. Pepee kahvaltıyı çok severdi ve yumurtaların üstüne hep bal sürerdi. Otların arasında ince ve parlak bir bal izi vardı. Pepee izin yanından yavaşça yürüdü. İz, büyük bir ağacın dibinde bitti. Yumurta orada, otların üstünde duruyordu. Yumurtadaki bala kuru yapraklar yapışmıştı. Pepee cebinden yumuşak bir sünger çıkardı ve yaprakları sildi. Sonra örtüyü ağacın yanındaki düz yere taşıdı. Pepee çok sevindi, çünkü kaybolan yumurtasını bulmuştu.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee kahvaltıyı çok severdi"
   - Cümle 5: «Pepee kahvaltıyı çok severdi ve yumurtaların üstüne hep bal sürerdi.»
   - Açıklama: Tohumdaki kahvaltı özelliği ikinci kez açıklama cümlesi olarak sayılıyor; kartın özellik kullanımı bir kez ve işe yarar biçimde olmalı.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "yumurtaların üstüne hep bal sürerdi"
   - Cümle 5: «Pepee kahvaltıyı çok severdi ve yumurtaların üstüne hep bal sürerdi.»
   - Açıklama: Kartın özellik alanı yalnız yumurta, bal ve tahin pekmez yediğini söyler; yumurtaya bal sürme alışkanlığı karta eklenmiş yanlış bilgidir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Otların arasında ince ve parlak bir bal izi"
   - Cümle 6: «Otların arasında ince ve parlak bir bal izi vardı.»
   - Açıklama: Yumurtaya bal sürüldüğü hiç gösterilmeden bal izi sebepsizce belirip çözümü getiriyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Yumurtadaki bala kuru yapraklar yapışmıştı"
   - Cümle 10: «Yumurtadaki bala kuru yapraklar yapışmıştı.»
   - Açıklama: Yumurta bulunduktan sonra yaprakların yapışması ikinci bir sorun açıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee cebinden yumuşak bir sünger çıkardı"
   - Cümle 11: «Pepee cebinden yumuşak bir sünger çıkardı ve yaprakları sildi.»
   - Açıklama: Sünger hiçbir kurulum olmadan cepten sebepsizce beliriyor.
   - Açıklama: Sünger sebepsiz beliriyor ve sorundan sonra işlevsiz ek adımlar ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0124` birebir aynı, `@degisim: esnek -> yumuşak` (tutuyorsan), ardından `@onarim: fbbccf5180eab4078934538465778a3dde5bea6e`, sonra gövde.
