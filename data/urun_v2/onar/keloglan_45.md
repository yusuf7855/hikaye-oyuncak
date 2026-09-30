# Editör görevi (onarım): Keloğlan, onarım partisi 45

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar45.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar45.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0123 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0123
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bitki', fiil 'şaşırtmak', sıfat 'hevesli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: bahçede bir sürü bitki vardı ve naneyi tanımıyordu | kitaptaki resimden naneyi tanıyıp bir demet topladı
@tohum: keloglan-0123
Şatonun bahçesinde hafif bir rüzgar esiyordu. Keloğlan, naneyi çok seven Bilgecan Dede'yi bir demet nane ile şaşırtmak istiyordu. Ama bahçede bir sürü yeşil bitki vardı ve Keloğlan naneyi tanımıyordu. Dede bankta oturmuş bir bitki kitabı okuyordu. Keloğlan kitaba bakmak istedi ve Dede kitabı ona verdi. Keloğlan kitabın sayfalarını çevirdi ve bir nane resmi buldu. Resme bakıp nane yaprağını tanımayı öğrendi. Keloğlan çok hevesliydi ve hemen bahçede dolaştı. Aynı yaprakları duvarın dibinde buldu ve küçük bir demet topladı. Sonra demeti Dede'ye uzattı. Dede çok şaşırdı ve naneyi sevinçle kokladı. Keloğlan çok sevindi, çünkü naneyi tek başına bulmuştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dede bankta oturmuş bir bitki kitabı okuyordu"
   - Cümle 4: «Dede bankta oturmuş bir bitki kitabı okuyordu.»
   - Açıklama: Çözümü getiren bitki kitabı, sorun söylenir söylenmez sebepsizce hazır bulunuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan çok hevesliydi"
   - Cümle 8: «Keloğlan çok hevesliydi ve hemen bahçede dolaştı.»
   - Açıklama: 'Hevesli' soyut bir kelime ve 3 yaşındaki çocuk bilmeyebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan çok hevesliydi ve"
   - Cümle 8: «Keloğlan çok hevesliydi ve hemen bahçede dolaştı.»
   - Açıklama: 'Hevesli' soyut bir kelime, 3 yaşındaki çocuk için uygun değil.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Dede çok şaşırdı ve naneyi sevinçle kokladı"
   - Cümle 11: «Dede çok şaşırdı ve naneyi sevinçle kokladı.»
   - Açıklama: Dede Keloğlan'ın kitabında naneyi aradığını gördüğü halde sürprize şaşırıyor.
   - Açıklama: Dede kitabını Keloğlan'a verip onun nane aradığını gördüğü halde sürprize şaşırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0123` birebir aynı, ardından `@onarim: e34dc6d41ad1e43eeb57ee7ad99d49adf8830235`, sonra gövde.

### Hikâye 2: tohum keloglan-0126 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0126
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'bambu', fiil 'silmek', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kütük tozluydu ve halkalar iyi görünmüyordu | kütüğü suyla ıslatıp mendille sildi
@tohum: keloglan-0126
@degisim: bambu -> kütük
Keloğlan ile anası ormanda kesilmiş büyük bir kütüğün yanına geldi. Keloğlan kütüğün üstünde ince halkalar fark etti. Halkaları saymak istedi ama kütük tozluydu ve halkalar iyi görünmüyordu. Keloğlan tozu ıslatmak için su şişesini açtı. Suyu yavaşça dökecekti ama sakar Keloğlan şişeyi çok eğdi. Bütün su kütüğün üstüne döküldü ve tozu ıslattı. Keloğlan anasından bir mendil istedi. Anası ona yepyeni bir mendil verdi. Keloğlan ıslak kütüğü mendille sildi. Toz gitti ve bütün halkalar göründü. Keloğlan halkaları tek tek saydı ve tam yirmi halka buldu. Sonra ikisi ormanda başka kütükler aramaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sakar Keloğlan şişeyi çok eğdi"
   - Cümle 5: «Suyu yavaşça dökecekti ama sakar Keloğlan şişeyi çok eğdi.»
   - Açıklama: Suyun hepsinin dökülmesi hiçbir sonuç doğurmuyor; sakarlık olayı işlevsiz kalıyor.
   - Açıklama: Suyun hepsinin dökülmesi bir aksilik gibi kuruluyor ama hiçbir sonucu olmuyor, su yine tozu ıslatıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Toz gitti ve bütün"
   - Cümle 10: «Toz gitti ve bütün halkalar göründü.»
   - Açıklama: Toz gitmez; fiil öznesine uymuyor, 'toz silindi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0126` birebir aynı, `@degisim: bambu -> kütük` (tutuyorsan), ardından `@onarim: f142c88079b911606dd90ce869c95bb6cefaf403`, sonra gövde.

### Hikâye 3: tohum keloglan-0127 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0127
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'cetvel', fiil 'katmak', sıfat 'yaratıcı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: çatıdan garip bir tık sesi geldi ve ev yıkıldı | bekledi ve düşen kozalağı görüp evi başka yere kurdu
@tohum: keloglan-0127
@degisim: yaratıcı -> küçük
Rüzgar ormanda hafif hafif esiyordu. Keloğlan büyük bir ağacın altında dallardan küçük bir ev yapıyordu. Tahta cetvelini evin çatısına koymuştu. Birden çatıdan bir "tık" sesi geldi ve ev yıkıldı. Keloğlan bu sesi çok merak etti. Keloğlan dürüst ve azimli bir çocuktu ve evi yeniden kurdu. Sonra evin yanına oturdu ve dikkatle bekledi. Biraz sonra yukarıdaki daldan bir kozalak düştü. Kozalak cetvele çarptı ve aynı ses geldi. Keloğlan evi ağacın altından çıkardı ve açık bir yere kurdu. Çatıya bir dal daha kattı. Keloğlan çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (7):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Tahta cetvelini evin çatısına"
   - Cümle 3: «Tahta cetvelini evin çatısına koymuştu.»
   - Açıklama: Cetvel kartta olmayan, masal köyü dünyasına uymayan çağdaş bir okul eşyası.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tahta cetvelini evin çatısına koymuştu"
   - Cümle 3: «Tahta cetvelini evin çatısına koymuştu.»
   - Açıklama: Dallardan yapılan evin çatısına cetvel koymak sebepsiz ve yalnız sesi üretmek için kurulmuş bir ayrıntı.
   - Açıklama: Cetvel çatıya sebepsizce konuyor ve yalnız sesi üretmek için kurulmuş.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keloğlan bu sesi çok merak etti"
   - Cümle 5: «Keloğlan bu sesi çok merak etti.»
   - Açıklama: Hikaye evin yıkılması ile sesin kaynağı arasında iki ayrı soruna bölünüyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 6: «Keloğlan dürüst ve azimli bir çocuktu ve evi yeniden kurdu.»
   - Açıklama: 'Dürüst' olayla ilgisiz soyut bir özellik kelimesi, tek kart özelliği istisnasına girmiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 6: «Keloğlan dürüst ve azimli bir çocuktu ve evi yeniden kurdu.»
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız sayılıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
6. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kozalak cetvele çarptı ve aynı ses geldi"
   - Cümle 9: «Kozalak cetvele çarptı ve aynı ses geldi.»
   - Açıklama: Kozalağın cetvele çarpmasının evi yıkması akla yatkın bir sebep değil ve evin yıkılma sebebi açıkça söylenmiyor.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "sesin nereden geldiğini bulmuştu"
   - Cümle 12: «Keloğlan çok sevindi, çünkü sesin nereden geldiğini bulmuştu.»
   - Açıklama: Son sesin bulunmasına dönüyor; evin artık yıkılmadığı görünmüyor, hedef belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0127` birebir aynı, `@degisim: yaratıcı -> küçük` (tutuyorsan), ardından `@onarim: 0e781718532a64768f5bba83ae0dea331838d4b7`, sonra gövde.

### Hikâye 4: tohum keloglan-0128 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0128
- yer: dağ (Köyün yakınındaki tepe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fındık', fiil 'sıkışmak', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: ıslak otlardaki ahşap kutunun kapağı sıkışmıştı | kutuyu taşa hafif hafif vurdu ve kapak açıldı
@tohum: keloglan-0128
Tepede hava serin ve sessizdi. Keloğlan orada oturmuş güneşin doğmasını bekliyordu. Yanındaki ahşap kutu ıslak otlarda durmuştu ve kapağı sıkışmıştı. Kutunun içinde Keloğlan'ın fındıkları vardı. Keloğlan kapağı çekti ama açamadı. Keloğlan biraz sakardı ve kutu elinden düz bir taşa düştü. Kapak biraz yukarı kalktı. Keloğlan bunu gördü ve kutuyu taşa hafif hafif vurdu. Kapak sonunda tam açıldı. Tam o sırada güneş tepenin arkasından doğdu. Keloğlan fındıklarını yiyerek güneşi mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ıslak otlarda durmuştu"
   - Cümle 3: «Yanındaki ahşap kutu ıslak otlarda durmuştu ve kapağı sıkışmıştı.»
   - Açıklama: 'Durmuştu' hareket eden bir şeyin durduğunu anlatır; kutu otlarda 'duruyordu' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kutu elinden düz bir taşa düştü"
   - Cümle 6: «Keloğlan biraz sakardı ve kutu elinden düz bir taşa düştü.»
   - Açıklama: Çözümün yolu Keloğlan'ın düşünmesinden değil, rastlantı bir düşüşten sebepsizce geliyor.
   - Açıklama: Çözüm figürün düşüncesinden değil, sebepsizce gelen bir kazadan çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0128` birebir aynı, ardından `@onarim: 979262d5a3cb691917ddd8b9465f6f7892489283`, sonra gövde.

### Hikâye 5: tohum keloglan-0130 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0130
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'perde', fiil 'gitmek', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: yağmur başladı ve kuru bir yer yoktu | ters dönen sepeti görüp başına koydu
@tohum: keloglan-0130
@degisim: perde -> sepet
Ormanda Keloğlan bomboş sepetiyle fındık toplamaya gidiyordu. Birden yağmur yağmaya başladı ve Keloğlan'ın başı ıslandı. Keloğlan saklanacak kuru bir yer aradı, ama her yer ıslaktı. Keloğlan biraz sakardı ve sepet elinden kayıp yere düştü. Sepet yerde ters durdu ve küçük bir şapkaya benzedi. Keloğlan bunu görünce sepeti başına ters koydu. Yağmur damlaları sepetin üstüne düştü. Ama Keloğlan'ın başı artık ıslanmadı. Keloğlan sepetin altında sessizce bekledi. Biraz sonra yağmur dindi ve güneş çıktı. Keloğlan sepeti başından aldı ve koluna taktı. Sonra mutlu mutlu fındık toplamaya başladı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepet elinden kayıp yere düştü"
   - Cümle 4: «Keloğlan biraz sakardı ve sepet elinden kayıp yere düştü.»
   - Açıklama: Çözüm Keloğlan'ın düşüncesinden değil, sepetin tesadüfen ters düşmesinden geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve sepet elinden kayıp yere düştü"
   - Cümle 4: «Keloğlan biraz sakardı ve sepet elinden kayıp yere düştü.»
   - Açıklama: Çözüm figürün düşüncesinden değil, sepetin tesadüfen düşüp ters durmasından sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0130` birebir aynı, `@degisim: perde -> sepet` (tutuyorsan), ardından `@onarim: 6cf693abe2e31595d73cdffba3a95adad46996f5`, sonra gövde.

### Hikâye 6: tohum keloglan-0133 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0133
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tartı', fiil 'gülmek', sıfat 'oynak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yeni tartı taşların üstünde sallanıyordu | tartıyı düz bir yere koydu
@tohum: keloglan-0133
Rüzgar büyük ağaçların arasında hafifçe esiyordu. Keloğlan ormanda Bilgecan Dede'nin yeni yaptığı tartıyı gördü. Ama tartı taşların üstünde oynak duruyor ve hep sallanıyordu. Dede cevizleri köyün çocukları için tartıp iki torbaya koymak istiyordu. "Dede, bu tartı neden sallanıyor?" diye sordu Keloğlan. "Tartı yalnız düz bir yerde iyi çalışır," dedi Bilgecan Dede. Keloğlan böylece yeni bir şey öğrendi ve etrafına baktı. Tartıyı taşlardan aldı ve düz bir yere koydu. Tartı artık hiç sallanmadı. Dede cevizleri tarttı ve iki torbaya koydu. Keloğlan ile Dede birlikte güldü ve torbaları mutlu mutlu bağladı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Tartı yalnız düz bir yerde iyi çalışır"
   - Cümle 6: «"Tartı yalnız düz bir yerde iyi çalışır," dedi Bilgecan Dede.»
   - Açıklama: Tartıyı yapan ve düz yer gerektiğini bilen Dede'nin onu taşların üstüne koyması sorunun sebebini akla yatkın kılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan böylece yeni bir şey öğrendi"
   - Cümle 7: «Keloğlan böylece yeni bir şey öğrendi ve etrafına baktı.»
   - Açıklama: Somut olmayan, soyut bir öğrenme cümlesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0133` birebir aynı, ardından `@onarim: 8c6f25f86a6d17e9d68fcdea6ea59a50cb4ec612`, sonra gövde.

### Hikâye 7: tohum keloglan-0134 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0134
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'fidan', fiil 'görüşmek', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar deliğin önündeki fidana çarpıyordu | yüksekten atmayı öğrendi ve kozalağı deliğe attı
@tohum: keloglan-0134
@degisim: görüşmek -> fırlatmak
Keloğlan ormanda komik bir kozalak oyunu oynuyordu. Kozalakları büyük bir ağacın dibindeki deliğe atmaya çalışıyordu. Ama deliğin önünde küçük bir fidan vardı ve kozalaklar hep ona çarpıyordu. Keloğlan fidana kibar davrandı ve onun dallarını kırmadı. Durdu ve kozalağı fidanın üstünden atmayı öğrenmek istedi. Bu kez kozalağı yukarı doğru, yüksekten fırlattı. Kozalak fidanın üstünden geçti ama delikten uzağa düştü. Keloğlan ikinci kozalağı biraz daha yavaş fırlattı. Bu kez kozalak tam deliğin içine girdi! Keloğlan sevinçle güldü ve ellerini çırptı. Sonra oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan fidana kibar davrandı"
   - Cümle 4: «Keloğlan fidana kibar davrandı ve onun dallarını kırmadı.»
   - Açıklama: Bir fidana kibar davranılmaz; sıfat nesneye uymuyor.
   - Açıklama: 'Kibar davranmak' insanlara karşı kullanılır; fidana uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan fidana kibar davrandı"
   - Cümle 4: «Keloğlan fidana kibar davrandı ve onun dallarını kırmadı.»
   - Açıklama: 'Kibar davranmak' burada mecazlı ve soyut kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0134` birebir aynı, `@degisim: görüşmek -> fırlatmak` (tutuyorsan), ardından `@onarim: abe15b8c950847828dd556356c2819375709ed46`, sonra gövde.

### Hikâye 8: tohum keloglan-0136 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0136
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'beşik', fiil 'sormak', sıfat 'lezzetli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: elma sepetinin ipi sıkı bir düğüm olmuştu | düğümün ucunu bulup yavaşça çekti
@tohum: keloglan-0136
@degisim: beşik -> sepet
Tepede serin bir rüzgar esiyordu. Keloğlan, eşeği Karakaçan'a bir sürpriz hazırlamıştı. Sepette lezzetli elmalar vardı, ama kapağın ipi sıkı bir düğüm olmuştu. Keloğlan elmalar düşmesin diye ipi çok iyi bağlamıştı. "Karakaçan, sürprizini görmek ister misin?" diye sordu Keloğlan. Eşek başını salladı. Keloğlan biraz sakardı, bu yüzden sepeti devirmemek için önce yere koydu. Sonra düğümün ucunu buldu ve yavaşça çekti. Düğüm çözüldü ve kapak açıldı. Karakaçan hemen bir elma yedi ve kulaklarını oynattı. Keloğlan güldü ve eşeğinin başını okşadı. "Afiyet olsun, Karakaçan, bu elmalar senin için!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden sepeti devirmemek için önce yere koydu"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden sepeti devirmemek için önce yere koydu.»
   - Açıklama: Tohumdaki sakarlık özelliği karttaki gibi bir şeyi düşürme ya da karıştırma olarak gösterilmiyor ve çözüme hiç katkı yapmıyor, yalnız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0136` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: accdec04a346ca1bb2c19bd69ae4a3c618ffce31`, sonra gövde.

### Hikâye 9: tohum keloglan-0137 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0137
- yer: dağ (Köyün yakınındaki tepe.)
- tema: bir şey yapmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'takvim', fiil 'anlatmak', sıfat 'büyük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: uçurtma kuyruğu olmadığı için düşüyordu | uzun kurdeleyi uçurtmaya kuyruk olarak bağladı
@tohum: keloglan-0137
@degisim: takvim -> kurdele
Tepede güçlü bir rüzgar esiyordu. Keloğlan ile Balkız büyük bir uçurtma yapmıştı. Ama uçurtma kuyruğu olmadığı için havada dönüyor ve yere düşüyordu. Keloğlan süs için getirdikleri uzun kurdeleyi eline aldı. Kurdele rüzgarda bir kuyruk gibi sallandı. "Balkız, bu kurdele uçurtmaya kuyruk olur," dedi Keloğlan. Sonra Balkız'a ne yapacağını anlattı. Keloğlan biraz sakardı, bu yüzden Balkız uçurtmayı sıkıca tuttu. Keloğlan da kurdeleyi uçurtmanın ucuna bağladı. Sonra Balkız ipi aldı ve Keloğlan uçurtmayı havaya bıraktı. Uçurtma bu kez dönmedi ve dümdüz yükseldi. "Ne güzel uçuyor, Balkız, onu birlikte yaptık!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden Balkız uçurtmayı sıkıca tuttu.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden Balkız uçurtmayı sıkıca tuttu"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden Balkız uçurtmayı sıkıca tuttu.»
   - Açıklama: Tohumdaki sakarlık yalnız etiket olarak söyleniyor; güvenli özellik kullanımı satırındaki gibi bir şeyi düşürme ya da karıştırma olarak gösterilmiyor ve çözümde işe yaramıyor.
   - Açıklama: Kartın güvenli özellik kullanımı sakarlığı bir şeyi düşürmek ya da karıştırmak olarak gösterir; burada sakarlık gösterilmeden yalnız etiket olarak geçiyor ve işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden Balkız uçurtmayı sıkıca tuttu"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden Balkız uçurtmayı sıkıca tuttu.»
   - Açıklama: Sakarlık ayrıntısı olayda hiçbir işe yaramıyor ve Balkız'ın uçurtmayı tutmasına sebep olarak zorla bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0137` birebir aynı, `@degisim: takvim -> kurdele` (tutuyorsan), ardından `@onarim: 80bdf8fafa794f43240cc2bf77eaa9bed3ad9951`, sonra gövde.

### Hikâye 10: tohum keloglan-0139 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0139
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yastık', fiil 'tamamlanmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: yağmurda kulübenin çatısı bitmemişti | dalları tek tek taşıyıp çatıdaki boşluğa dizdi
@tohum: keloglan-0139
@degisim: yastık -> dal
Yağmur yavaş yavaş yağmaya başladı. Keloğlan ile Balkız ormanda dallardan küçük bir kulübe yapıyordu. Ama kulübenin çatısı bitmemişti ve içeri yağmur damlıyordu. "Keloğlan, çatıdan içeri su geliyor!" dedi Balkız. Keloğlan yerdeki büyük dallara baktı ve düşündü. Keloğlan biraz sakardı, bu yüzden dalları tek tek taşıdı. Dalları çatıdaki boşluğa yan yana dizdi. Böylece çatı tamamlandı. İçeri artık hiç su girmedi. Dışarıda otlar sırılsıklam oldu, ama kulübenin içi kuru kaldı. "Teşekkürler, Keloğlan, kulübemiz bitti!" dedi Balkız. Keloğlan çok sevindi, çünkü yaptıkları kulübe ikisini de yağmurdan korumuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden dalları tek tek taşıdı"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden dalları tek tek taşıdı.»
   - Açıklama: Sakarlık kartın güvenli kullanım satırındaki gibi bir şeyi düşürmek ya da karıştırmak olarak değil, dikkatli davranmanın gerekçesi olarak kullanılıyor.
   - Açıklama: Kartın güvenli özellik kullanımı sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterir; burada sakarlık gösterilmeden yalnız etiket olarak geçiyor ve çözüme yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden dalları tek tek taşıdı"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden dalları tek tek taşıdı.»
   - Açıklama: Sakarlık ile dalları tek tek taşımak arasında akla yatkın bir sebep bağı yok; özellik zorla eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0139` birebir aynı, `@degisim: yastık -> dal` (tutuyorsan), ardından `@onarim: da5e2efab51e2196f5323a28de3811b0e9a86598`, sonra gövde.

### Hikâye 11: tohum keloglan-0145 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0145
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sis', fiil 'koşmak', sıfat 'tertemiz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: dağa sis indi ve koşma oyununda kaya görünmez oldu | adımlarını sayarak yürüdü ve kayayı sisin içinde buldu
@tohum: keloglan-0145
Dağda Keloğlan büyük bir ağaçtan gri bir kayaya koşma oyunu oynuyordu. Oyundan önce yürüyüp adımlarını saymış ve kayanın on adım uzakta olduğunu öğrenmişti. Ama birden tepeye beyaz bir sis indi ve kaya görünmez oldu. O sırada Keloğlan ağacın yanındaydı. Ağaçla kaya arasında yalnız düz, yumuşak çimenler vardı. Keloğlan koşmadı, çimenlerin üstünde dikkatle yürüdü. Bir, iki, üç diye adımlarını tek tek saydı. On adım sonra eli soğuk kayaya değdi. Keloğlan sevinçle zıpladı ve kayaya sarıldı. Biraz sonra rüzgar esti ve sis dağıldı. Hava yine tertemiz oldu ve oyun devam etti. Keloğlan çok mutluydu, çünkü kayayı sisin içinde bile bulmuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "tepeye beyaz bir sis indi ve kaya görünmez oldu"
   - Cümle 3: «Ama birden tepeye beyaz bir sis indi ve kaya görünmez oldu.»
   - Açıklama: Keloğlan yetişkinsiz olarak dağda yoğun siste yürüyor; çocuk taklit ederse tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0145` birebir aynı, ardından `@onarim: 3699ecb6267c6196ca94c29f477bfcb4d8d3fe27`, sonra gövde.

### Hikâye 12: tohum keloglan-0146 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0146
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'ay', fiil 'tatmak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yakından şırıl şırıl bir ses geliyordu ama su görünmüyordu | sesin geldiği yerde yaprakları kaldırıp ince bir su buldu
@tohum: keloglan-0146
Serin bir rüzgar esiyordu ve gökyüzünde soluk bir ay vardı. Keloğlan ile Bilgecan Dede ormanda bir ağacın altında oturuyordu. Birden yakından şırıl şırıl bir ses geldi ama hiç su görünmüyordu. Keloğlan o sırada dedenin verdiği tuzlu bisküviyi tadıyordu. "Dede, bu ses nereden geliyor?" diye sordu Keloğlan. "Bul bakalım," dedi Bilgecan Dede. Keloğlan biraz sakardı, bu yüzden bisküviyi düşürmemek için dedeye verdi. Sonra sesin geldiği yere gitti ve yaprakları iki eliyle kaldırdı. Yaprakların altında ince bir su akıyordu! "Ses buradan geliyormuş!" dedi Keloğlan. Dede gülümsedi. Sonra Keloğlan ile dede suyun sesini mutlu mutlu dinledi.
```

**Hakem bulguları (8):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gökyüzünde soluk bir ay"
   - Cümle 1: «Serin bir rüzgar esiyordu ve gökyüzünde soluk bir ay vardı.»
   - Açıklama: 'Soluk ay' şiirsel bir betimleme; 3 yaşındaki çocuk 'soluk' kelimesini bu anlamda bilmez.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakından şırıl şırıl bir ses geldi"
   - Cümle 3: «Birden yakından şırıl şırıl bir ses geldi ama hiç su görünmüyordu.»
   - Açıklama: Görünmeyen suyun sesi çocuğun önemseyeceği bir sorun değil; bulunca hiçbir şey değişmiyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "dedenin verdiği tuzlu bisküviyi"
   - Cümle 4: «Keloğlan o sırada dedenin verdiği tuzlu bisküviyi tadıyordu.»
   - Açıklama: Tuzlu bisküvi masal köyü dünyasına uymayan çağdaş bir eşya; kartın tohum yasak kategorileri çağdaş öğeleri dışlıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dedenin verdiği tuzlu bisküviyi tadıyordu"
   - Cümle 4: «Keloğlan o sırada dedenin verdiği tuzlu bisküviyi tadıyordu.»
   - Açıklama: Bisküvi sorunla ilgisiz biçimde kuruluyor ve olayda hiçbir işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tuzlu bisküviyi tadıyordu"
   - Cümle 4: «Keloğlan o sırada dedenin verdiği tuzlu bisküviyi tadıyordu.»
   - Açıklama: Bisküvi olaya hiçbir katkı yapmayan işlevsiz bir ayrıntı olarak kuruluyor ve bir kenara bırakılıyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden bisküviyi düşürmemek için dedeye verdi.»
   - Açıklama: 'Sakar' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden bisküviyi düşürmemek"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden bisküviyi düşürmemek için dedeye verdi.»
   - Açıklama: Tohumdaki sakarlık özelliği yalnız söyleniyor, kartın güvenli kullanım satırındaki gibi bir şeyi düşürme olarak gösterilmiyor ve sorunun çözümüne yaramıyor.
8. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden bisküviyi düşürmemek için dedeye verdi"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden bisküviyi düşürmemek için dedeye verdi.»
   - Açıklama: Güvenli özellik kullanımı sakarlığı bir şeyi düşürmek olarak gösterir; burada sakarlık gösterilmiyor ve sorunun çözümüne katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0146` birebir aynı, ardından `@onarim: 5739ff9cc5e882e77a148ff40128e77d5e6fcc6e`, sonra gövde.
