# Editör görevi (onarım): Pepee, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0001 (deneme 3 -> 4)

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
Rüzgar esiyordu ve deniz biraz dalgalıydı. Pepee annesine sürpriz yapmak için su kenarındaki kuma bir kalp çizdi. Ama küçük bir dalga geldi ve çizgileri hemen sildi. Annee biraz ileride oturmuş, denize bakıyordu. Pepee bu kez sudan uzakta, kuru kuma gitti. Annesi uzaktan görsün diye ayaklarıyla büyük bir kalp çizmeyi denedi. Küçük adımlarla yürüdü ve her adım kumda bir iz bıraktı. Bu izler kocaman bir kalp oldu. "Anne, buraya bak, ayakla çizmeyi öğrendim!" dedi Pepee. Annee döndü ve kumdaki kalbi gördü. "Ne güzel olmuş, bunu hiç unutmayacağım, Pepee," dedi Annee. Sonra ikisi kalbin yanına oturdu ve mutlu mutlu denizi seyretti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Annee biraz ileride oturmuş, denize bakıyordu"
   - Cümle 4: «Annee biraz ileride oturmuş, denize bakıyordu.»
   - Açıklama: Dalgalı denizde Pepee su kenarındayken annesi yanında değil ve ona bakmıyor; bu, güvenli kullanım satırındaki bir büyüğün yanında deneme koşuluna aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0001` birebir aynı, ardından `@onarim: 250e211da0150407f9a5364d95136644fb45083b`, sonra gövde.

### Hikâye 2: tohum pepee-0007 (deneme 3 -> 4)

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
Rüzgar hafif hafif esiyordu. Pepee kumda gemi oyunu oynuyordu. Kumdan bir gemi yaptı ama kuru kum hemen dağıldı. Pepee üzülmedi ve umutlu bir yüzle su kenarına gitti. Orada kum ıslaktı ve dağılmıyordu. Kovasını aldı ve bu kumla doldurdu. Islak kumu elleriyle sıktı ve yeni bir gemi yaptı. Bu kez gemi hiç yıkılmadı. Pepee kovayı doldurmayı üç kez tekrarladı ve gemi büyüdü. Sonra geminin ortasına oturdu ve denize baktı. Pepee çok sevindi, çünkü ıslak kumla gemi yapmayı öğrenmişti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee üzülmedi ve umutlu bir yüzle su kenarına gitti"
   - Cümle 4: «Pepee üzülmedi ve umutlu bir yüzle su kenarına gitti.»
   - Açıklama: Güvenli özellik kullanımı satırına aykırı olarak Pepee yeni şeyi hiçbir büyük yokken, tek başına su kenarında deniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "umutlu bir yüzle su kenarına gitti"
   - Cümle 4: «Pepee üzülmedi ve umutlu bir yüzle su kenarına gitti.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama burada su kenarına yanında hiçbir büyük olmadan tek başına gidiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "umutlu bir yüzle su"
   - Cümle 4: «Pepee üzülmedi ve umutlu bir yüzle su kenarına gitti.»
   - Açıklama: 'Umutlu bir yüz' soyut bir ifade; 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Umutlu' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0007` birebir aynı, `@degisim: şort -> kova` (tutuyorsan), ardından `@onarim: 5edf49fc4084c253939123d7e75f26a6e7c81061`, sonra gövde.

### Hikâye 3: tohum pepee-0010 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: yumurta kaşıktan kayıp masanın altına yuvarlandı | sandalyeden inip yumurtayı buldu ve kaşığın altına tabak tuttu
@tohum: pepee-0010
@degisim: şekerleme -> tabak
Evde masa hazırdı ve Pepee sandalyesine oturmuştu. Pepee yumurtasını kaşıkla masada gezdirip oynuyordu. Ama yumurta kaşıktan kaydı ve masanın altına yuvarlandı. Pepee kahvaltıda en çok yumurtayı severdi. Hemen sandalyesinden indi ve yere baktı. Yumurtayı bir masa ayağının yanında buldu. Sonra yerine oturdu ve oyuna devam etti. Bu kez Pepee hazırlıklıydı ve kaşığın altına bir tabak tuttu. Yumurta yine kaydı, ama bu sefer tabağa düştü. Pepee oyunu iki kez daha oynadı ve güldü. Sonra yumurtasını soydu ve afiyetle yedi. Pepee çok mutluydu, çünkü hem oynamış hem de yumurtasını yemişti.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Yumurtayı bir masa ayağının yanında buldu"
   - Cümle 6: «Yumurtayı bir masa ayağının yanında buldu.»
   - Açıklama: Sorun Pepee'nin yemekle oynamasından doğan önemsiz bir olay ve yumurta hemen bulunarak kendiliğinden bitiyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra yerine oturdu ve oyuna devam etti"
   - Cümle 7: «Sonra yerine oturdu ve oyuna devam etti.»
   - Açıklama: Yumurta bulunduktan sonra çözüm aynı riskli oyunu sürdürüp tabak tutma adımıyla ikiden fazla adıma uzuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu kez Pepee hazırlıklıydı"
   - Cümle 8: «Bu kez Pepee hazırlıklıydı ve kaşığın altına bir tabak tuttu.»
   - Açıklama: 'Hazırlıklı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu kez Pepee hazırlıklıydı ve kaşığın altına bir tabak tuttu"
   - Cümle 8: «Bu kez Pepee hazırlıklıydı ve kaşığın altına bir tabak tuttu.»
   - Açıklama: Çözüm inmek, bulmak, oyuna dönmek ve tabak tutmak diye ikiden fazla adıma yayılıyor ve tabak asıl sebebe (yemekle oynamak) yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0010` birebir aynı, `@degisim: şekerleme -> tabak` (tutuyorsan), ardından `@onarim: 78c9a27eaa358c1ca19896fdccd0c61b93632c4a`, sonra gövde.

### Hikâye 4: tohum pepee-0015 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Dedee
@tohum: pepee-0015
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: paylaşmak
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kayık', fiil 'durmak', sıfat 'açık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Dedee
@plan: dedenin çantası açık kaldı ve ekmeği yolda düştü | kendi yumurtasını ve ekmeğini dedesiyle paylaştı
@tohum: pepee-0015
@degisim: kayık -> çanta
Rüzgar hafif hafif esiyordu. Pepee ile Dedee parkta salıncağın yanına oturdu. Ama Dedee'nin çantası açık kalmıştı ve ekmeği yolda düşmüştü. "Eyvah, yiyecek hiçbir şeyim yok," dedi Dedee. Pepee kendi çantasına baktı. İçinde iki yumurta ve iki ballı ekmek vardı. Pepee kahvaltıyı çok severdi ama bir an durdu ve düşündü. Sonra bir yumurtayı ve bir ekmeği dedesine uzattı. "Buyur, Dedee, bunlar senin," dedi Pepee. Dedee gülümsedi ve yumurtasını soydu. İkisi yan yana oturup ekmeklerini yedi. "Teşekkürler, Pepee, karnım doydu ve çok mutluyum!" dedi Dedee.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ekmeği yolda düştü"
   - Cümle 3: «Ama Dedee'nin çantası açık kalmıştı ve ekmeği yolda düşmüştü.»
   - Açıklama: Yönelme eki gerekir; 'yola düştü' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra bir yumurtayı ve bir ekmeği dedesine uzattı"
   - Cümle 8: «Sonra bir yumurtayı ve bir ekmeği dedesine uzattı.»
   - Açıklama: Sebep açık çanta ve yolda düşen ekmek, ama çözüm bu sebebe yönelmeden başka yiyecek vermekle yetiniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0015` birebir aynı, `@degisim: kayık -> çanta` (tutuyorsan), ardından `@onarim: efae28f4775cd58100e40b53975e953857a46d52`, sonra gövde.

### Hikâye 5: tohum pepee-0016 (deneme 1 -> 2)

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
@plan: yağmur başladı ve şapka ıslandı | ninesinin yanında şemsiye açmayı öğrendi
@tohum: pepee-0016
@degisim: pankek -> şemsiye
Deniz kıyısında küçük dalgalar köpürüyordu. Pepee ile Nenee kumda oturmuş, denize bakıyordu. Birden yağmur başladı ve Pepee'nin mavi şapkası ıslandı. Nenee çantasından katlanmış bir şemsiye çıkardı. "Nineciğim, şemsiyeyi ben açabilir miyim?" diye sordu Pepee. "Tabii, ama yavaş aç, bu şemsiye biraz kırılgan," dedi Nenee. Nenee ona küçük bir düğmeyi gösterdi. Pepee düğmeye bastı ve şemsiyeyi yavaşça yukarı itti. Şemsiye kocaman açıldı. İkisi şemsiyenin altına girdi ve artık hiç ıslanmadı. Yağmur damlaları üstlerinde tık tık ses yaptı. Pepee çok mutlu oldu, çünkü şemsiye açmayı kendisi öğrenmişti.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Nenee çantasından katlanmış bir şemsiye çıkardı"
   - Cümle 4: «Nenee çantasından katlanmış bir şemsiye çıkardı.»
   - Açıklama: Çözümün asıl adımını Pepee istemeden Nenee kendiliğinden atıyor; Pepee yalnız düğmeye basıyor.
   - Açıklama: Çözümü getiren şemsiyeyi Pepee değil Nenee kendiliğinden çıkarıyor; Pepee yalnız açıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu şemsiye biraz kırılgan"
   - Cümle 6: «"Tabii, ama yavaş aç, bu şemsiye biraz kırılgan," dedi Nenee.»
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0016` birebir aynı, `@degisim: pankek -> şemsiye` (tutuyorsan), ardından `@onarim: ae598806c7277687c82c9a3207c640dbe821b252`, sonra gövde.

### Hikâye 6: tohum pepee-0018 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0018
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Annee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'pijama', fiil 'uyanmak', sıfat 'çiçekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: uyanınca nereden geldiği bilinmeyen tatlı bir koku duydu | kokunun peşinden yürüdü ve sarı çiçekleri buldu
@tohum: pepee-0018
@degisim: pijama -> çalı
Ormanda ağaçların altı serin ve sessizdi. Pepee, Annee'nin yanında kısa bir süre uyumuştu. Uyanınca tatlı bir koku duydu ama nereden geldiğini bilmiyordu. "Anneciğim, burada bal mı var?" diye sordu Pepee. Pepee kahvaltıda en çok balı severdi ve bu kokuyu hemen tanımıştı. "Bilmiyorum, hadi birlikte bakalım," dedi Annee. Pepee kokunun peşinden yavaşça yürüdü. Önce bir ağacı, sonra bir taşı kokladı. Sonunda sarı çiçekli bir çalı buldu. Tatlı koku bu küçük sarı çiçeklerden geliyordu. "Bu çiçekler bal gibi kokuyor!" dedi Pepee. Sonra Pepee ile Annee çalının yanında mutlu mutlu oyun oynadı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Uyanınca tatlı bir koku duydu"
   - Cümle 3: «Uyanınca tatlı bir koku duydu ama nereden geldiğini bilmiyordu.»
   - Açıklama: Tatlı bir kokunun kaynağını bilmemek gerçek bir sorun değil, önemsiz bir merak olarak kalıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Uyanınca tatlı bir koku duydu ama nereden geldiğini bilmiyordu"
   - Cümle 3: «Uyanınca tatlı bir koku duydu ama nereden geldiğini bilmiyordu.»
   - Açıklama: Tatlı bir kokunun kaynağını bilmemek gerçek bir sorun değil, çocuğun önemseyeceği bir engel kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0018` birebir aynı, `@degisim: pijama -> çalı` (tutuyorsan), ardından `@onarim: ea8b84d24fa5ace4168e7bf2338fc270e9fe6b8f`, sonra gövde.

### Hikâye 7: tohum pepee-0022 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0022
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'yemek', fiil 'oynatmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: ağacın altına girince gölgesi kayboldu | güneşli bir yere yürüdü ve gölgesiyle dans etti
@tohum: pepee-0022
@degisim: yemek -> gölge
Ormanda, ağaçların arasında süslü çiçekler açmıştı. Pepee çiçeklerin yanında, yerde kendi gölgesini fark etti. Gölgesiyle dans etmek istedi ama büyük bir ağacın altına girince gölgesi kayboldu. Pepee biraz düşündü ve çevresine baktı. İleride güneşin vurduğu açık bir yer vardı. Pepee oraya yürüdü ve gölgesi yeniden göründü. Sonra kollarını oynattı ve dans etti. Gölgesi de onunla birlikte sallandı. Pepee tek ayağının üstünde döndü, gölge de döndü. Sonra kahkahalarla güldü. Pepee bundan sonra gölgesiyle oynamak için güneşli yerleri seçti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arasında süslü çiçekler açmıştı"
   - Cümle 1: «Ormanda, ağaçların arasında süslü çiçekler açmıştı.»
   - Açıklama: Çiçekler süslü olmaz; sıfat isme uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ağaçların arasında süslü çiçekler"
   - Cümle 1: «Ormanda, ağaçların arasında süslü çiçekler açmıştı.»
   - Açıklama: 'Süslü' çiçekler için doğru anlamda değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0022` birebir aynı, `@degisim: yemek -> gölge` (tutuyorsan), ardından `@onarim: 0f23c16027dd4f84c200e82dc31d98184b651d9d`, sonra gövde.

### Hikâye 8: tohum pepee-0023 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0023
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'eşarp', fiil 'hazırlamak', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: dans ederken nereden geldiği bilinmeyen bir ses duydu | kovasına ve cebine baktı ve kabukları buldu
@tohum: pepee-0023
@degisim: eşarp -> kabuk
Bir sabah Pepee deniz kıyısında yeni bir dans hazırlıyordu. Kumda her zıpladığında küçük bir ses duyuldu. Pepee bu sesin nereden geldiğini çok merak etti. Önce kovasına baktı ama kova bomboştu. Sonra kumun üstüne baktı, orada da hiçbir şey yoktu. Pepee yeniden zıpladı ve ses yine geldi. Bu kez ses tulumunun cebinden geliyordu. Pepee elini cebine soktu ve iki küçük kabuk çıkardı. Onları dansa başlamadan önce kıyıda toplamıştı. Zıplayınca kabuklar birbirine çarpıyor ve ses yapıyordu. Pepee kabukları avucunda salladı ve güldü. Pepee çok sevindi, çünkü dansı için güzel bir ses bulmuştu.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce kovasına baktı ama kova bomboştu"
   - Cümle 4: «Önce kovasına baktı ama kova bomboştu.»
   - Açıklama: Pepee sesin kaynağını bulmadan önce kovaya, kuma bakıp yeniden zıplıyor; çözüm iki adımı aşıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kumun üstüne baktı"
   - Cümle 5: «Sonra kumun üstüne baktı, orada da hiçbir şey yoktu.»
   - Açıklama: Pepee kovaya, kuma ve yeniden zıplayıp cebine bakıyor; çözüm iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0023` birebir aynı, `@degisim: eşarp -> kabuk` (tutuyorsan), ardından `@onarim: 8fe54c34fe034c947fd5365dbea490a2c9e271d9`, sonra gövde.
