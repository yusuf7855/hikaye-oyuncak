# Editör görevi (onarım): Pepee, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum pepee-0057 (deneme 5 -> 6)

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
@plan: pastaya koyacak parlak bir süs yoktu | kumu eliyle serpti ve kabuktaki inciyi buldu
@tohum: pepee-0057
@degisim: yardımsever -> parlak
Pepee deniz kıyısında, sudan uzakta kumdan bir pasta yapıyordu. Pastanın tepesine parlak bir süs koymak istiyordu. Ama etrafta yalnız gri taşlar vardı. Pepee süs bulmak için bir avuç kum aldı. Kumu parmaklarının arasından yavaşça serpti. Avucunda kapalı küçük bir kabuk kaldı. Pepee kabuğun içini çok merak etti. Kabuğu yavaşça açtı. İçinde beyaz bir inci vardı! Pepee ilk kez gerçek bir inci görüyordu. İnciyi pastanın tepesine koydu. Pasta artık çok güzel olmuştu. Pepee o sabah kabukların içinde inci olabileceğini öğrendi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Avucunda kapalı küçük bir kabuk kaldı"
   - Cümle 6: «Avucunda kapalı küçük bir kabuk kaldı.»
   - Açıklama: İnci dolu kabuk sebepsizce, şans eseri beliriyor ve çözümü kendiliğinden getiriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kabuğu yavaşça açtı"
   - Cümle 8: «Kabuğu yavaşça açtı.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada kapalı kabuğu yalnız başına açıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama burada deniz kıyısında yalnızken yeni bir şey deniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İçinde beyaz bir inci vardı"
   - Cümle 9: «İçinde beyaz bir inci vardı!»
   - Açıklama: Çözümü getiren inci kumdan rastgele çıkan kabukta sebepsizce beliriyor; çözüm şansa dayanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0057` birebir aynı, `@degisim: yardımsever -> parlak` (tutuyorsan), ardından `@onarim: 4411339021400f96756b627e1bfbb32fbdb5a1cf`, sonra gövde.

### Hikâye 2: tohum pepee-0062 (deneme 5 -> 6)

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
@plan: ballı ekmek birden ıslandı | kalkıp yukarı baktı ve suyun geldiği dalı buldu
@tohum: pepee-0062
Ormanda hava serindi ve yapraklar ıslaktı. Pepee sağlam bir kütüğe oturdu ve çantasından kahvaltısını çıkardı. Ama ballı ekmek birden ıslandı, çünkü üstüne su damlıyordu. Pepee bu suyun nereden geldiğini çok merak etti. Kütükten kalktı ve yukarı baktı. Tam üstünde yapraklı bir dal vardı. Dalın yapraklarından küçük damlalar düşüyordu. Pepee ekmek ve yumurtayla güneşli bir çimenliğe gitti. Orada üstüne hiç su düşmedi. Pepee ekmekten büyük bir lokma aldı ve yumurtasını da yedi. Pepee çok sevindi, çünkü suyun nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kalkıp yukarı baktı ve suyun geldiği dalı buldu"
   - Cümle 0 (plan satırı): «ballı ekmek birden ıslandı | kalkıp yukarı baktı ve suyun geldiği dalı buldu»
   - Açıklama: Gövdede sorunu çözen şey dalı bulmak değil, güneşli çimenliğe taşınmak; plan çözümü doğru söylemiyor.
   - Açıklama: Gövdede sorunu çözen adım güneşli çimenliğe gitmek; plan bu çözümü söylemiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee ekmek ve yumurtayla güneşli"
   - Cümle 8: «Pepee ekmek ve yumurtayla güneşli bir çimenliğe gitti.»
   - Açıklama: Yumurta daha önce hiç kurulmadan sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0062` birebir aynı, ardından `@onarim: 87b233554341824dab70b4a2913ba38043a1f642`, sonra gövde.

### Hikâye 3: tohum pepee-0068 (deneme 4 -> 5)

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
Deniz kıyısında serin bir rüzgar esiyordu. Pepee kovayla kumdan bir kale yapıyordu. Ama kuru kum kovadan çıkınca hemen dağıldı. Pepee üzüldü ve kumda oturdu. Şila somurtkan Pepee'nin yanına geldi. "Ne oldu, Pepee?" diye sordu Şila. "Kum hep dağılıyor," dedi Pepee. Pepee sonra su kenarına baktı. Oradaki ıslak kumda Şila'nın ayak izleri duruyordu. Pepee kovayı ıslak kumla doldurdu ve ters çevirdi. Bu kez güzel bir kale çıktı. Şila küçük taşlar getirdi. Pepee taşları kalenin üstüne tek tek sıraladı. "Ne güzel bir kale, Pepee!" dedi Şila. Pepee o gün kaleyi ıslak kumla yapmayı öğrendi.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şila somurtkan Pepee'nin yanına geldi"
   - Cümle 5: «Şila somurtkan Pepee'nin yanına geldi.»
   - Açıklama: 'Somurtkan' kelimesinin yeri cümleyi belirsiz ve bozuk kılıyor; Şila mı Pepee mi somurtkan anlaşılmıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şila somurtkan Pepee'nin yanına"
   - Cümle 5: «Şila somurtkan Pepee'nin yanına geldi.»
   - Açıklama: Sıfatın yeri yanlış; 'somurtkan' kelimesinin Şila'yı mı Pepee'yi mi nitelediği belirsiz.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee kovayı ıslak kumla doldurdu"
   - Cümle 10: «Pepee kovayı ıslak kumla doldurdu ve ters çevirdi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama denizde yanında hiçbir büyük yokken yeni bir yöntem deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0068` birebir aynı, `@degisim: çan -> kova` (tutuyorsan), ardından `@onarim: f00429660dd42c2b7be2f4d5c74faef9b8f1562b`, sonra gövde.

### Hikâye 4: tohum pepee-0070 (deneme 4 -> 5)

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
@plan: küçük dalgalar örtüye yaklaştı | örtüyü dedesinin kuru ayakkabılarının yanına taşıdı
@tohum: pepee-0070
Güneş parlıyordu ve deniz ışıltılıydı. Pepee su kenarında dedesine sürpriz bir kahvaltı hazırlıyordu. Ama küçük dalgalar gelip örtüye yaklaştı. Örtünün ucu ıslandı. Pepee etrafına baktı. Dedee biraz uzakta gözleri kapalı bekliyordu. Dedee'nin ayakkabıları da oradaki kumda duruyordu. Ayakkabılar kuruydu, çünkü dalga oraya gelmiyordu. Pepee örtüyü ve üstündeki her şeyi ayakkabıların yanına taşıdı. Artık örtü hiç ıslanmadı. Sonra Dedee gözlerini açtı. Sürprizi görünce güldü ve Pepee'ye sarıldı. İkisi kumda oturup balı ve yumurtayı paylaştı. Pepee o günden sonra örtüsünü hep kuru kuma serdi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "deniz ışıltılıydı"
   - Cümle 1: «Güneş parlıyordu ve deniz ışıltılıydı.»
   - Açıklama: 'Işıltılı' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve deniz ışıltılıydı"
   - Cümle 1: «Güneş parlıyordu ve deniz ışıltılıydı.»
   - Açıklama: 'Işıltılı' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Dedee biraz uzakta gözleri kapalı bekliyordu"
   - Cümle 6: «Dedee biraz uzakta gözleri kapalı bekliyordu.»
   - Açıklama: Güvenli kullanım satırı Pepee'nin bir büyüğün yanında olmasını ister; burada Pepee su kenarındayken dedesi uzakta ve gözleri kapalıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0070` birebir aynı, ardından `@onarim: 2f04a872476d93256ce0501484198e978c04cd18`, sonra gövde.

### Hikâye 5: tohum pepee-0078 (deneme 3 -> 4)

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
@plan: yapraklar küçük elinden havaya çıkmadı | şapkasını yaprakla doldurup yaprakları havaya savurdu
@tohum: pepee-0078
@degisim: minder -> şapka
Ormanda yapraklı ağaçların altına bir sürü sarı yaprak düşmüştü. Pepee yaprakları havaya atıp altında zıplamak istedi. Ama küçük eli çok az yaprak tuttu ve yapraklar havaya hiç çıkmadı. Pepee durdu ve biraz düşündü. Sonra mavi şapkasını çıkardı ve onu yapraklarla doldurdu. Yaprakları şapkadan havaya doğru savurdu. Yapraklar yavaş yavaş başına döküldü. Pepee sevinçle zıpladı ve şapkayı yine doldurdu. Yapraklar bu sefer daha yükseğe uçtu. Sonunda Pepee'nin mavi tulumunun her yerinde yaprak vardı. Pepee çok mutluydu, çünkü şapkayla yaprak uçurmayı öğrenmişti.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yapraklı ağaçların altına bir sürü sarı yaprak"
   - Cümle 1: «Ormanda yapraklı ağaçların altına bir sürü sarı yaprak düşmüştü.»
   - Açıklama: 'Yapraklı' ile 'yaprak' aynı cümlede gereksiz tekrar ediyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "mavi şapkasını çıkardı ve onu yapraklarla doldurdu"
   - Cümle 5: «Sonra mavi şapkasını çıkardı ve onu yapraklarla doldurdu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama ormanda yalnızken yeni bir şey deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0078` birebir aynı, `@degisim: minder -> şapka` (tutuyorsan), ardından `@onarim: 9f6ce20fd73344a05d95849035c0dfd23a1b22c6`, sonra gövde.

### Hikâye 6: tohum pepee-0081 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Parkta güneş parlıyordu. Pepee bankta oturup güneşlenirken yerden iki küçük taş aldı ve cebine koydu. Sonra dans etti, ama her zıpladığında tık tık diye bir ses geldi. Pepee bu sesi çok merak etti. Pepee aceleci olmadı ve zıplamayı bıraktı. Ses de hemen kesildi. Sonra yavaşça bir kez daha zıpladı ve dinledi. Ses tulumunun cebinden geliyordu. Elini cebine soktu ve iki taşı buldu. Pepee zıplayınca taşlar cebinde birbirine vuruyordu. Taşları elinde salladı ve güldü. Pepee çok sevindi, çünkü sesi yapan şeyi kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yerden iki küçük taş aldı ve cebine koydu"
   - Cümle 2: «Pepee bankta oturup güneşlenirken yerden iki küçük taş aldı ve cebine koydu.»
   - Açıklama: Sesi Pepee'nin kendi koyduğu taşlar yapıyor; sorun önemsiz ve okur için baştan belli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee aceleci olmadı"
   - Cümle 5: «Pepee aceleci olmadı ve zıplamayı bıraktı.»
   - Açıklama: 'Aceleci olmadı' soyut bir anlatım, somut davranış yerine kişilik kelimesi kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee aceleci olmadı"
   - Cümle 5: «Pepee aceleci olmadı ve zıplamayı bıraktı.»
   - Açıklama: Tohumdaki özellik dans; sabırlılık (aceleci olmamak) karttaki özelliklere ek ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0081` birebir aynı, `@degisim: kızak -> taş` (tutuyorsan), ardından `@onarim: 5f99f02bdf5f544db6ee8fba8f40dd6e4be43f71`, sonra gövde.

### Hikâye 7: tohum pepee-0083 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0083
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: kaybolan eşya
- yan: Dedee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'çörek', fiil 'kirletmek', sıfat 'soslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: rüzgar esti ve mavi şapkayı uçurdu | olduğu yerde dönerek her yere baktı ve şapkayı buldu
@tohum: pepee-0083
@degisim: soslu -> şekerli
Deniz kıyısında Pepee ile Dedee kumda çörek yiyordu. Pepee'nin elleri şekerliydi, o yüzden şapkasını kirletmemek için yanına koymuştu. Birden rüzgar esti ve şapkayı uçurdu. Pepee önüne baktı ama şapkasını göremedi. "Dedeciğim, şapkam uçtu, bana yardım eder misin?" dedi Pepee. Dedee hemen ayağa kalktı. Pepee de olduğu yerde dansta yaptığı gibi yavaşça döndü. Böylece her yöne baktı. Sonunda su kenarında, kumun üstünde mavi bir şey gördü. Bu onun şapkasıydı! Dedee şapkayı getirip Pepee'nin başına taktı. Pepee ile Dedee çörek yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Dedee şapkayı getirip Pepee'nin başına taktı"
   - Cümle 11: «Dedee şapkayı getirip Pepee'nin başına taktı.»
   - Açıklama: Şapkayı geri getiren Pepee değil Dedee; çözümün son adımını yan karakter yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0083` birebir aynı, `@degisim: soslu -> şekerli` (tutuyorsan), ardından `@onarim: 1af2ba6f66e6e3825ab89ae748bd790bcfc6ead9`, sonra gövde.
