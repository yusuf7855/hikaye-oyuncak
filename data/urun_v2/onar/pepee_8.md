# Editör görevi (onarım): Pepee, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0001 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Annee
@tohum: pepee-0001
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'iz', fiil 'unutmak', sıfat 'dalgalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Annee
@plan: dalga su kenarındaki kalbi sildi | kuru kumda ayaklarıyla yeni bir kalp yaptı
@tohum: pepee-0001
Rüzgar esiyordu ve deniz biraz dalgalıydı. Pepee annesine sürpriz yapmak için su kenarındaki kuma bir kalp çizdi. Ama küçük bir dalga geldi ve çizgileri hemen sildi. Annee arkasında oturmuş, gözlerini kapatmıştı. Pepee bu kez sudan uzakta, annesinin yanındaki kuru kuma gitti. Annesi görsün diye ayaklarıyla büyük bir kalp çizmeyi denedi. Küçük adımlarla yürüdü ve her adım kumda bir iz bıraktı. Bu izler kocaman bir kalp oldu. "Anne, buraya bak, ayakla çizmeyi öğrendim!" dedi Pepee. Annee ayağa kalktı ve kumdaki kalbi gördü. "Ne güzel olmuş, bunu hiç unutmayacağım, Pepee," dedi Annee. Sonra ikisi kalbin yanına oturdu ve mutlu mutlu denizi seyretti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Annee arkasında oturmuş, gözlerini kapatmıştı"
   - Cümle 4: «Annee arkasında oturmuş, gözlerini kapatmıştı.»
   - Açıklama: Dalgalı denizde su kenarındaki çocuğu büyüğü izlemiyor; güvenli kullanım satırındaki büyüğün yanında deneme ilkesine aykırı.
   - Açıklama: Pepee su kenarında oynarken yanındaki büyük gözlerini kapatmış, güvenli kullanım satırındaki büyüğün gözetimi zayıflıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0001` birebir aynı, ardından `@onarim: faab8f07b728199646b9e06e92c617e71e4421fc`, sonra gövde.

### Hikâye 2: tohum pepee-0007 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0007
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'şort', fiil 'tekrarlamak', sıfat 'umutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kuru kumdan yapılan gemi hemen dağıldı | ıslak kumla sağlam bir gemi yaptı
@tohum: pepee-0007
@degisim: şort -> kova
Rüzgar hafif hafif esiyordu. Pepee kumda gemi oyunu oynuyordu. Kumdan bir gemi yaptı ama kuru kum hemen dağıldı. Pepee üzülmedi, yeniden denemek için umutluydu. Kumu elleriyle biraz kazdı. Kumun altı ıslaktı. Kovasını aldı ve bu kumla doldurdu. Islak kumu iyice bastırdı ve yeni bir gemi yaptı. Bu kez gemi hiç yıkılmadı. Pepee kovayı doldurmayı üç kez tekrarladı ve gemi büyüdü. Sonra geminin ortasına oturdu ve denize baktı. Pepee çok sevindi, çünkü ıslak kumla gemi yapmayı öğrenmişti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kumda gemi oyunu oynuyordu"
   - Cümle 2: «Pepee kumda gemi oyunu oynuyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında yalnız başına deniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeniden denemek için umutluydu"
   - Cümle 4: «Pepee üzülmedi, yeniden denemek için umutluydu.»
   - Açıklama: 'umutlu' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumu elleriyle biraz kazdı"
   - Cümle 5: «Kumu elleriyle biraz kazdı.»
   - Açıklama: Pepee'nin kumu neden kazdığı söylenmiyor; ıslak kum çözümü tesadüfen geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0007` birebir aynı, `@degisim: şort -> kova` (tutuyorsan), ardından `@onarim: fec389952566c95f7babe791ee5ab6dbf8989ce8`, sonra gövde.

### Hikâye 3: tohum pepee-0010 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0010
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'şekerleme', fiil 'inmek', sıfat 'hazırlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: minder kalesinin üstündeki yastık düştü | minderleri yaklaştırdı ve yastığı yeniden koydu
@tohum: pepee-0010
@degisim: şekerleme -> tabak
Evde, Pepee iki büyük minderden bir kale yapıyordu. Kahvaltısını bu kalenin içinde yemek istiyordu. Ama minderler birbirinden çok uzaktı ve üstlerine koyduğu uzun yastık düştü. Pepee sandalyeye oturdu ve biraz düşündü. Sonra sandalyeden indi ve minderleri birbirine yaklaştırdı. Yastığı yeniden üstlerine koydu. Bu kez yastık düşmedi ve kale sağlam durdu. Pepee masadan tabağını getirdi. Tabakta yumurta, ballı ekmek ve tahin pekmez vardı. Pepee artık kahvaltı için hazırlıklıydı ve kalenin içine girdi. Yumurtasını ve ekmeğini orada afiyetle yedi. Pepee çok mutluydu, çünkü kalesinde kahvaltı yapmıştı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ballı ekmek ve tahin pekmez"
   - Cümle 9: «Tabakta yumurta, ballı ekmek ve tahin pekmez vardı.»
   - Açıklama: Tamlama eksik; 'tahinli pekmez' ya da 'tahin pekmezi' olmalı.
   - Açıklama: Tamlama eki eksik; 'tahinli pekmez' ya da 'tahin pekmezi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kahvaltı için hazırlıklıydı"
   - Cümle 10: «Pepee artık kahvaltı için hazırlıklıydı ve kalenin içine girdi.»
   - Açıklama: 'Hazırlıklı' burada yanlış anlamda; 'hazırdı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kahvaltı için hazırlıklıydı"
   - Cümle 10: «Pepee artık kahvaltı için hazırlıklıydı ve kalenin içine girdi.»
   - Açıklama: 'hazırlıklıydı' soyut ve çocuk için zor bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0010` birebir aynı, `@degisim: şekerleme -> tabak` (tutuyorsan), ardından `@onarim: 4d82a4ed5bdb0ae08245e5f68fecd1d0a2cc89b8`, sonra gövde.

### Hikâye 4: tohum pepee-0016 (deneme 3 -> 4)

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
Deniz kıyısında küçük dalgalar köpürüyordu. Pepee ile Nenee kumda oturmuş, denize bakıyordu. Birden yağmur başladı ve Pepee'nin mavi şapkası ıslandı. "Nineciğim, şemsiye var mı?" diye sordu Pepee. Nenee çantasından katlanmış bir şemsiye çıkardı. "Şemsiyeyi ben açabilir miyim?" diye sordu Pepee. "Tabii, ama yavaş aç, telleri çok ince ve kırılgan," dedi Nenee. Nenee ona küçük bir düğmeyi gösterdi. Pepee düğmeye bastı ve şemsiyeyi yavaşça yukarı itti. Şemsiye kocaman açıldı. İkisi şemsiyenin altına girdi ve artık hiç ıslanmadı. Yağmur damlaları şemsiyede tık tık ses yaptı. Pepee çok mutlu oldu, çünkü şemsiye açmayı kendisi öğrenmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "telleri çok ince ve kırılgan"
   - Cümle 7: «"Tabii, ama yavaş aç, telleri çok ince ve kırılgan," dedi Nenee.»
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0016` birebir aynı, `@degisim: pankek -> şemsiye` (tutuyorsan), ardından `@onarim: ca62acc15febddf3c4c9674b001f327416fba76a`, sonra gövde.

### Hikâye 5: tohum pepee-0021 (deneme 3 -> 4)

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
Bir sabah Pepee ormanda evcilik oynuyordu. Büyük bir taşı masa yaptı ve üstüne kahvaltısını dizdi. Ama taş düz değildi ve yumurta masadan yuvarlandı. Pepee koştu ve yumurtayı otların arasından aldı. Pepee şanslıydı, çünkü yumurta hiç kırılmamıştı. Pepee yumurtayı çok severdi ve onu masada yemek istedi. Yerden ince dallar topladı. Dalları taşın kenarına, toprağa sıkıca dikti. Böylece taşın kenarında küçük bir çit oldu. Pepee yumurtayı yeniden masaya koydu. Yumurta yine yuvarlandı ama çite çarpıp durdu. Pepee güldü ve yumurtasını afiyetle yedi. Sonra oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee koştu ve yumurtayı otların arasından aldı"
   - Cümle 4: «Pepee koştu ve yumurtayı otların arasından aldı.»
   - Açıklama: Yere, otların arasına düşen yumurta sonra yeniyor; taklit edilince yerden yiyecek yeme davranışı örnekleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee şanslıydı, çünkü yumurta"
   - Cümle 5: «Pepee şanslıydı, çünkü yumurta hiç kırılmamıştı.»
   - Açıklama: 'Şanslı' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0021` birebir aynı, `@degisim: rahatlatmak -> dikmek` (tutuyorsan), ardından `@onarim: 4e2f3a587739061abb1dec716988516bf54033d7`, sonra gövde.

### Hikâye 6: tohum pepee-0024 (deneme 3 -> 4)

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
Ormanda serin bir rüzgar esiyordu. Pepee ile Dedee ağaçların arasında yürüyordu. Birden Dedee durdu, çünkü ev anahtarı cebinden düşmüştü. "Anahtar bu yaprakların arasında olmalı," dedi Dedee. Ama yerde çok yaprak vardı. "Dedeciğim, anahtarı nasıl buluruz?" diye sordu Pepee. "Güneş vurunca anahtar parlar," dedi Dedee. Pepee yeni şeyler öğrenmeyi çok severdi. Hemen eğildi ve güneşli yerlere dikkatle baktı. Bir çalının dibinde küçük bir şey ışıldadı. Pepee yaprağı kaldırdı ve anahtarı buldu. "Sen çok çalışkansın, Pepee," dedi Dedee. Pepee çok sevindi, çünkü dedesine yardım etmişti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee yeni şeyler öğrenmeyi çok severdi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi çok severdi.»
   - Açıklama: Tohumdaki öğrenme özelliği kartın özellikler alanındaki gibi işe yarar biçimde kullanılmıyor, yalnız özellik olarak sayılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee yeni şeyler öğrenmeyi çok severdi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi çok severdi.»
   - Açıklama: Öğrenme sevgisi anahtarı arama olayına bağlanmayan işlevsiz bir ayrıntı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bir çalının dibinde küçük bir şey ışıldadı"
   - Cümle 10: «Bir çalının dibinde küçük bir şey ışıldadı.»
   - Açıklama: Anahtar güneşte ışıldayarak görülüyor ama hemen ardından bir yaprağın altından çıkarılıyor; örtülü anahtarın parlaması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0024` birebir aynı, `@degisim: kırıntı -> anahtar` (tutuyorsan), ardından `@onarim: 21c8e5ef0a13485c1d60ba48773a228b987d8595`, sonra gövde.

### Hikâye 7: tohum pepee-0025 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0025
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'yelken', fiil 'yağmak', sıfat 'hazır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: yağmur başladı ve örtünün üstüne damlalar düştü | örtüyü sık yapraklı ağacın altına taşıdı
@tohum: pepee-0025
@degisim: yelken -> örtü
Pepee ormanda kardeşi Bebee için yere örtü serip sürpriz kahvaltı hazırlıyordu. Bebee gözlerini kapatmış, bir taşın üstünde bekliyordu. Ama yağmur yağmaya başladı ve örtünün üstüne damlalar düştü. Yakında yaprakları sık, büyük bir ağaç vardı. Pepee örtüyü dört ucundan topladı ve ağacın altına taşıdı. Sonra Bebee'nin elinden tuttu ve onu da oraya götürdü. Orada hiç damla düşmüyordu. Pepee örtüyü yeniden serdi ve yumurtayla balı dizdi. "Gözlerini aç, Bebee, sofra hazır!" dedi Pepee. Bebee baktı ve sevinçle el çırptı. "Bunları benim için mi getirdin?" diye sordu Bebee. "Evet, hepsi senin için," dedi Pepee. Pepee ile Bebee ağacın altında mutlu mutlu yemeğe başladı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yakında yaprakları sık"
   - Cümle 4: «Yakında yaprakları sık, büyük bir ağaç vardı.»
   - Açıklama: 'Yakında' zaman anlamına da gelir; 'yakınlarda' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0025` birebir aynı, `@degisim: yelken -> örtü` (tutuyorsan), ardından `@onarim: f1a72346a44b9558dcf7d8b9e53797d428dce842`, sonra gövde.

### Hikâye 8: tohum pepee-0026 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Şila
@tohum: pepee-0026
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mobilya', fiil 'değişmek', sıfat 'gri'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | Şila
@plan: kar tanesi sıcak elde hemen su oldu | kar tanesini soğuk kolunda yakaladı
@tohum: pepee-0026
@degisim: mobilya -> kapı
Evde, kapının önünde Pepee ile Şila karı izliyordu. Pepee bir kar tanesini yakından görmek istedi. Ama kar tanesi sıcak eline düşünce hemen değişti ve su oldu. Gri bulutlardan yine kar yağıyordu. Pepee soğuk kolunun üstündeki karın su olmadığını gördü. Pepee yeni şeyler öğrenmeyi severdi ve kolunu hemen uzattı. Mavi koluna bir kar tanesi kondu. Bu kez kar tanesi erimedi. Pepee yakından baktı ve minik bir yıldız gördü. "Şila, bak, kar tanesi yıldız gibi!" dedi Pepee. Şila da yanına gelip baktı ve güldü. Pepee çok sevindi, çünkü kar tanesini sonunda yakından görmüştü.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "baktı ve minik bir yıldız gördü"
   - Cümle 9: «Pepee yakından baktı ve minik bir yıldız gördü.»
   - Açıklama: Pepee gerçek bir yıldız değil yıldız biçiminde kar tanesi gördü; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0026` birebir aynı, `@degisim: mobilya -> kapı` (tutuyorsan), ardından `@onarim: 923b7ea5889200a30707633f4c0fb08ea2e70a1e`, sonra gövde.

### Hikâye 9: tohum pepee-0027 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0027
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'karpuz', fiil 'kırpmak', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: güneş çok parlaktı ve yumurta kaşıktan düştü | şapkasını öne çekip yumurtayı yavaşça taşıdı
@tohum: pepee-0027
@degisim: karpuz -> kaşık
Bir sabah Pepee ormanda eğlenceli bir oyun oynuyordu. Kahvaltıda en sevdiği yumurtayı kaşıkta taşıyıp büyük ağacın altında yiyecekti. Ama güneş çok parlaktı, Pepee gözlerini kırptı ve yumurta otlara düştü. Otlar yumuşaktı ve yumurta kırılmadı. Pepee onu aldı ve toprağını sildi. Sonra mavi şapkasını biraz öne çekti. Artık güneş gözüne gelmedi. Pepee yumurtayı kaşığa koydu ve yavaş yürüdü. Yumurta sallandı ama düşmedi. Pepee ağaca vardı ve güldü. Orada yumurtanın kabuğunu soydu ve onu yedi. Pepee çok sevindi, çünkü yumurtayı sonunda ağaca getirmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu aldı ve toprağını sildi"
   - Cümle 5: «Pepee onu aldı ve toprağını sildi.»
   - Açıklama: Yumurtanın kendi toprağı olmaz; 'üstündeki toprağı' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kabuğunu soydu ve onu yedi"
   - Cümle 11: «Orada yumurtanın kabuğunu soydu ve onu yedi.»
   - Açıklama: 'Onu' zamiri kabuğu da yumurtayı da gösterebilir.
   - Açıklama: 'onu' zamiri en yakın ad olan kabuğu da gösterebiliyor, yumurta olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0027` birebir aynı, `@degisim: karpuz -> kaşık` (tutuyorsan), ardından `@onarim: 11820b37b2fc5558c5938d4c9e10ee590547d803`, sonra gövde.

### Hikâye 10: tohum pepee-0028 (deneme 2 -> 3)

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
Rüzgar ağaçların arasında esiyordu. Pepee ile Nenee ormanda pizza oyunu oynuyordu. Yuvarlak bir yaprağı pizza yaptılar ama onu pişirecek bir fırın yoktu. Nenee yerden yeşil otlar topladı ve pizzanın üstüne koydu. "Nine, fırını nerede buluruz?" diye sordu Pepee. "Fırın gibi bir yer ara, bu çok basit," dedi Nenee ve güldü. Pepee kalın bir ağacın dibinde küçük bir delik buldu. Pepee yeni bir şey öğrenmek istedi ve bu deliği fırın yaptı. Pizzayı dikkatle deliğin içine koydu. İkisi birlikte ona kadar saydı. Sonra Pepee pizzayı çıkardı ve ninesine uzattı. "Buyur, nineciğim, orman pizzası pişti!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee yeni bir şey öğrenmek istedi"
   - Cümle 8: «Pepee yeni bir şey öğrenmek istedi ve bu deliği fırın yaptı.»
   - Açıklama: 'Yeni bir şey öğrenmek istedi' ifadesi deliği fırın yapma eylemine anlamca uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee yeni bir şey öğrenmek istedi"
   - Cümle 8: «Pepee yeni bir şey öğrenmek istedi ve bu deliği fırın yaptı.»
   - Açıklama: Deliği fırın yapmanın sebebi olaydan çıkmıyor; özellik sebepsizce araya sokulmuş.
   - Açıklama: Öğrenme isteği olaydan çıkmıyor; deliği fırın yapmayı sebepsiz bir özellik cümlesi getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0028` birebir aynı, `@degisim: yeşillenmek -> toplamak` (tutuyorsan), ardından `@onarim: 7245f6c741e4a767afd62d732a9f47ab0668a867`, sonra gövde.

### Hikâye 11: tohum pepee-0029 (deneme 2 -> 3)

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
Evde Pepee mavi şapkasını arıyordu. Şapkayı az önce koltuğa koymuştu ama şimdi orada göremiyordu. Mutfağa ve odasına da baktı, ama şapka hiçbir yerde yoktu. Sonunda Pepee yoruldu ve masada oturan annesinin yanına gitti. "Anne, şapkam kayboldu," dedi Pepee. "Şapkayı nereye koydun? Oraya bak, eşyaların altına da bak," dedi Annee. Pepee annesinden yeni bir şey öğrendi ve koltuğa geri döndü. Koltukta annesinin gazetesi duruyordu. Pepee gazeteyi kaldırdı ve şapkasını altında buldu. Şapkayı hemen başına taktı. "Teşekkürler, anneciğim, şapkamı buldum!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Oraya bak, eşyaların altına"
   - Cümle 7: «Oraya bak, eşyaların altına da bak," dedi Annee.»
   - Açıklama: 'Oraya' zamirinin hangi yeri gösterdiği belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "annesinden yeni bir şey öğrendi"
   - Cümle 8: «Pepee annesinden yeni bir şey öğrendi ve koltuğa geri döndü.»
   - Açıklama: 'Yeni bir şey öğrendi' soyut ve belirsiz bir anlatım; somut olarak ne yaptığı söylenmeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0029` birebir aynı, `@degisim: kirli -> mavi` (tutuyorsan), ardından `@onarim: 73634e4db1f01c0fc85ac83b13c471cfa8017866`, sonra gövde.

### Hikâye 12: tohum pepee-0030 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0030
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mıknatıs', fiil 'kıpırdamak', sıfat 'kibar'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: dalga kumdan pastanın bir yanını yıktı | pastayı suyun uzağında yeniden yaptı
@tohum: pepee-0030
@degisim: mıknatıs -> kabuk
Bir sabah Pepee ile Şila kumsalda oynuyordu. O gün Şila'nın doğum günüydü ve Pepee ona kumdan pasta yapıyordu. Ama pasta suya yakındı ve bir dalga pastanın yanını yıktı. Şila arkasını dönmüş, kıpırdamadan duruyordu. "Biraz daha bekler misin, Şila?" diye sordu Pepee kibar bir sesle. "Tabii, Pepee," dedi Şila. Pepee dalgalara baktı ve onların yalnız ıslak kuma geldiğini öğrendi. Pastayı daha yukarıda yeniden yaptı. Üstüne küçük deniz kabukları dizdi. Bu kez hiçbir dalga pastaya gelmedi. "Şimdi dönebilirsin, Şila!" dedi Pepee. Şila pastayı görünce sevinçle zıpladı. Pepee ile Şila pastanın yanında mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kuma geldiğini öğrendi"
   - Cümle 7: «Pepee dalgalara baktı ve onların yalnız ıslak kuma geldiğini öğrendi.»
   - Açıklama: Bakarak öğrenilmez; 'gördü' olmalı.
   - Açıklama: Bakarak bir şey görülür, 'öğrendi' yerine 'gördü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0030` birebir aynı, `@degisim: mıknatıs -> kabuk` (tutuyorsan), ardından `@onarim: 472c4311543db2b8c9ada4e45c40e96037cbada7`, sonra gövde.
