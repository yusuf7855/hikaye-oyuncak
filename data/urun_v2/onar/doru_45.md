# Editör görevi (onarım): Doru, onarım partisi 45

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar45.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Doru | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar45.txt --ad urun_v2`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Onarılacak hikâyeler

### Hikâye 1: tohum doru-0131 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0131
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çubuk', fiil 'gezdirmek', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yağmur yaklaşıyordu ve kuru yerin yolunu bilmiyordu | yardım istedi ve düz yoldan hızla koştu
@tohum: doru-0131
@degisim: gezdirmek -> göstermek
Doru ormanda Kırat'la birlikte yürüyordu. Birden gökte kara bulutlar toplandı ve yağmur yaklaştı. Doru kuru bir yere gitmek istedi ama yolu bilmiyordu. Kırat ormanı çok iyi tanıyordu. Doru ondan yolu göstermesini istedi. Kırat, kırık çubuklarla dolu yolu değil, yanındaki düz yolu gösterdi. Doru o düz yolda hızla koştu. Yağmur başlamadan büyük bir kayanın altına ulaştı. Kırat da yere bakarak, temkinli adımlarla arkasından geldi. Sonra yağmur başladı ama ikisi de kuru kaldı. Doru ile Kırat kayanın altında yağmuru mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yere bakarak, temkinli adımlarla"
   - Cümle 9: «Kırat da yere bakarak, temkinli adımlarla arkasından geldi.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kırat da yere bakarak, temkinli adımlarla arkasından geldi"
   - Cümle 9: «Kırat da yere bakarak, temkinli adımlarla arkasından geldi.»
   - Açıklama: Düz yolda temkinli yürüme ve kırık çubuklu yol ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0131` birebir aynı, `@degisim: gezdirmek -> göstermek` (tutuyorsan), ardından `@onarim: 7ec2875bdeb0d125f77d236d5210a1ba9e4cc012`, sonra gövde.

### Hikâye 2: tohum doru-0134 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0134
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'örgü', fiil 'gitmek', sıfat 'uzak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: arkadaşı saklanırken oyun yerini göremedi | arkadaşının sesini duyup hızla koştu ve onu buldu
@tohum: doru-0134
@degisim: örgü -> ağaç
Ormanda Doru ile Alaca saklanma oyunu oynuyordu. Alaca saklanmak için uzak ağaçlara gitti. Oradan geri dönmek istedi ama oyun yerini göremedi. "Doru, neredesin?" diye seslendi Alaca. Doru bu sesi hemen duydu. Ağaçların arasındaki düz ve açık yolda hızla koştu. Az sonra Alaca'yı büyük bir ağacın altında buldu. "Seni buldum, Alaca!" dedi Doru. "İyi ki geldin, Doru," dedi Alaca. "Benimle gel," dedi Doru. Alaca onun arkasından yürüdü ve ikisi oyun yerine döndü. Sonra iki arkadaş oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Alaca saklanmak için uzak ağaçlara gitti"
   - Cümle 2: «Alaca saklanmak için uzak ağaçlara gitti.»
   - Açıklama: En küçük karakter saklanmak için ormanda uzağa gidip kayboluyor; çocuk taklit ederse tehlikeli olur.
   - Açıklama: En küçük tay ormanda tek başına uzağa gidip yolunu kaybediyor; çocuk bunu taklit edebilir.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "düz ve açık yolda hızla koştu"
   - Cümle 6: «Ağaçların arasındaki düz ve açık yolda hızla koştu.»
   - Açıklama: Ağaçlar arasında düz ve açık bir yol varken Alaca'nın oyun yerini görememesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0134` birebir aynı, `@degisim: örgü -> ağaç` (tutuyorsan), ardından `@onarim: ae9160ab2e859594044dc2aeebecd78193f5b69b`, sonra gövde.

### Hikâye 3: tohum doru-0138 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0138
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'nane', fiil 'küçülmek', sıfat 'iyi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesinin başı alçak çalının altına girmedi | naneleri dişleriyle koparıp annesiyle paylaştı
@tohum: doru-0138
Doru annesiyle dağda yürüyordu ve ikisi de acıkmıştı. Doru alçak bir çalının altında taze naneler gördü. Ama annesi büyüktü ve başı çalının altına girmedi. "Doru, keşke biraz küçülebilsem," dedi annesi. Doru gençti ve annesinden daha küçüktü. Doru hemen annesine yardım etmek istedi. Başını dalların altına uzattı ve naneleri dişleriyle kopardı. Naneleri ikiye ayırdı ve yarısını annesinin önüne bıraktı. Annesi bir nane tattı ve gülümsedi. "Çok güzel kokuyorlar, teşekkürler, Doru," dedi annesi. İkisi naneleri yan yana yiyip bitirdi. Doru bundan sonra iyi bir şey görünce hep annesiyle paylaşırdı.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hep annesiyle paylaşırdı"
   - Cümle 12: «Doru bundan sonra iyi bir şey görünce hep annesiyle paylaşırdı.»
   - Açıklama: Anlatım -dı'lı geçmişten -ırdı'lı alışkanlık kipine kayıyor; 'paylaştı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0138` birebir aynı, ardından `@onarim: f3967ae33a42f754b57ae997c2bad70480d5db3b`, sonra gövde.

### Hikâye 4: tohum doru-0141 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0141
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çember', fiil 'ilerlemek', sıfat 'meyveli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: uzun otlar yüzünden küçük arkadaşı ağacı göremedi | ona hangi yöne gideceğini söyleyerek yardım etti
@tohum: doru-0141
Kuşlar ötüyordu ve geniş çayırda hafif bir rüzgar esiyordu. Doru ile Alaca oynuyordu ve Alaca, Doru'yu meyveli ağaca götürecekti. Ama uzun otlar yüzünden küçük Alaca ağacı göremedi. "Hangi yöne gideceğim?" diye sordu Alaca. Doru başını kaldırdı ve ağacı gördü. Doru hemen Alaca'ya yardım etti. "Sağa dön, Alaca, sonra hep düz ilerle," dedi Doru. Alaca sağa döndü ve otların arasında ilerledi. Sonunda elmalarla dolu dallar göründü. "Ağaca geldik, teşekkürler, Doru!" dedi Alaca. Alaca sevinçle ağacın çevresinde çember gibi döndü. Sonra ikisi gölgede elmaları mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çevresinde çember gibi döndü"
   - Cümle 11: «Alaca sevinçle ağacın çevresinde çember gibi döndü.»
   - Açıklama: 'Çember gibi' benzetmesi 3 yaşındaki bir çocuk için soyut ve anlaşılması zor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağacın çevresinde çember gibi döndü"
   - Cümle 11: «Alaca sevinçle ağacın çevresinde çember gibi döndü.»
   - Açıklama: 'Çember gibi' benzetmesi ve 'çember' kelimesi 3 yaşındaki çocuk için belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0141` birebir aynı, ardından `@onarim: 5889de0512168ad07d2fcd699c5d0c55af2cec47`, sonra gövde.

### Hikâye 5: tohum doru-0145 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0145
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'meşe', fiil 'şakımak', sıfat 'çekingen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: büyük atın kuyruğu bir ağacın ince dalına takıldı | dişleriyle dalı eğdi ve kuyruğu kurtardı
@tohum: doru-0145
@degisim: şakı- -> öt-
Parktaki geniş çayırda büyük bir meşe vardı ve dallarında kuşlar ötüyordu. Doru ağacın altında Kırat'ı gördü. Kırat'ın uzun kuyruğu ince bir dala takılmıştı. Dal tam arkasındaydı ve Kırat onu göremiyordu. Kırat kuyruğunu her çektiğinde, kuyruk dala daha çok dolanıyordu. "Doru, kuyruğum takıldı, çıkaramıyorum," dedi Kırat alçak ve çekingen bir sesle. Doru ona yardım etmek için hemen yanına gitti. Dalı dişleriyle tuttu ve yavaşça eğdi. Sonra kuyruğu daldan dikkatle ayırdı. Kuyruk kurtuldu ve aşağı indi. Kırat sevinçle kuyruğunu salladı. "Teşekkürler, Doru, kuyruğum artık serbest!" dedi Kırat.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parktaki geniş çayırda büyük"
   - Cümle 1: «Parktaki geniş çayırda büyük bir meşe vardı ve dallarında kuşlar ötüyordu.»
   - Açıklama: Kartın park yeri tarifi sürünün çimen yediği bir çayırdır; dizide olmayan 'park' metne yer olarak giriyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Parktaki geniş çayırda büyük"
   - Cümle 1: «Parktaki geniş çayırda büyük bir meşe vardı ve dallarında kuşlar ötüyordu.»
   - Açıklama: Kartın park yeri notuna göre dizide park yok; 'Parktaki' ifadesi diziyi izlemiş çocuğa yanlış bir yer bilgisi verir, yer yalnız çayır olarak anılmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "alçak ve çekingen bir sesle"
   - Cümle 6: «"Doru, kuyruğum takıldı, çıkaramıyorum," dedi Kırat alçak ve çekingen bir sesle.»
   - Açıklama: 'Çekingen' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Çekingen' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0145` birebir aynı, `@degisim: şakı- -> öt-` (tutuyorsan), ardından `@onarim: a003c798c793d1a2cdaf994a1bed61f5e92a30b5`, sonra gövde.

### Hikâye 6: tohum doru-0146 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0146
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: paylaşmak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'boncuk', fiil 'yoğurmak', sıfat 'yüksek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: ağaçtaki son elma bir taşa çarpıp uzaklaştı | hızla koşup elmayı durdurdu ve arkadaşıyla paylaştı
@tohum: doru-0146
@degisim: yoğur- -> yuvarlan-
Doru ile Karatay parktaki geniş çayırda bir elma ağacının altında duruyordu. Karatay yüksek bir dala uzandı ve son elmayı düşürdü. Ama elma bir taşa çarptı, çimenlerde yuvarlandı ve uzaklaştı. "Son elma gidiyor!" dedi Karatay. Doru hemen düz ve açık çayırda hızla koştu. Elmanın önüne geçti ve onu ayağıyla durdurdu. Sonra elmayı ağzıyla aldı ve ağacın altına getirdi. "Gel, Karatay, bu elmayı paylaşalım," dedi Doru. Doru elmayı ısırdı, ikiye böldü ve yarısını Karatay'a verdi. Elmanın içinde boncuk gibi küçük, siyah çekirdekler vardı. Arkadaşlar yan yana durdu ve elmayı yedi. İkisi de çok mutluydu, çünkü son elmayı paylaşmışlardı.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "parktaki geniş çayırda"
   - Cümle 1: «Doru ile Karatay parktaki geniş çayırda bir elma ağacının altında duruyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği çayırdır; dizide olmayan insan yapımı park yeri metne giriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elmanın içinde boncuk gibi küçük, siyah çekirdekler vardı"
   - Cümle 10: «Elmanın içinde boncuk gibi küçük, siyah çekirdekler vardı.»
   - Açıklama: Çekirdekler olaya hiçbir katkı yapmayan işlevsiz bir ayrıntı.
   - Açıklama: Çekirdekler olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşlar yan yana durdu"
   - Cümle 11: «Arkadaşlar yan yana durdu ve elmayı yedi.»
   - Açıklama: 'Arkadaşlar' Doru ile Karatay'ı gösteriyor ama yeni kişiler gibi okunabiliyor; 'İkisi' denmeliydi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0146` birebir aynı, `@degisim: yoğur- -> yuvarlan-` (tutuyorsan), ardından `@onarim: f274e4aef4ad3e4ce35b18476de23c45b79557c1`, sonra gövde.

### Hikâye 7: tohum doru-0151 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0151
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'basamak', fiil 'tutunmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: yağmur başladı ve yelesi ıslandı | hızla koşup sık dalların altına girdi
@tohum: doru-0151
@degisim: basamak -> damla
Doru ormanın kenarındaki açıklıkta çimen yiyordu. Birden hafif bir yağmur yağmaya başladı. Doru'nun yelesi hemen ıslandı. Kuru kalmak için büyük ağaçların altına gitmeliydi. Ama ağaçlar biraz uzaktaydı. Doru açık ve düz çimenlerin üstünde hızla koştu. Kısa sürede ağaçların altına vardı. Orada dallar sık ve karışıktı. Damlalar yapraklara tutunuyor ve aşağı düşmüyordu. Doru başını iki kez salladı ve yelesi biraz kurudu. Sonra kuru yerde yağmurun sesini mutlu mutlu dinledi. Doru bundan sonra yağmur başlayınca hemen kuru bir yer aradı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Damlalar yapraklara tutunuyor"
   - Cümle 9: «Damlalar yapraklara tutunuyor ve aşağı düşmüyordu.»
   - Açıklama: Damlalar tutunmaz; fiil öznesine uygun değil.
   - Açıklama: Damlalar tutunmaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0151` birebir aynı, `@degisim: basamak -> damla` (tutuyorsan), ardından `@onarim: 834a374d9e09081254b1202f9559383e5b02782c`, sonra gövde.

### Hikâye 8: tohum doru-0152 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0152
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bağcık', fiil 'tamamlamak', sıfat 'kaygan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: susamıştı ve uzaktan bir su sesi geldi | hızla koşup sesi buldu ve kayadan damlayan suyu içti
@tohum: doru-0152
@degisim: bağcık -> kütük
Doru annesiyle dağda çimen yiyordu. Çok susamıştı, ama yanlarında su yoktu. Birden uzaktan "şıp, şıp" diye bir ses geldi. Doru bu sesi çok merak etti. "Anne, bu bir su sesi mi?" diye sordu Doru. "Olabilir, git bak, ben seni buradan görüyorum," dedi annesi. Doru açık ve düz çimenlerde hızla koştu. Sesin geldiği yerde yüksek bir kayadan su damlıyordu. Damlalar eski bir kütüğün üstüne düşüyor ve ses çıkarıyordu. Kayanın yanındaki taşlar ıslak ve kaygandı. Bu yüzden Doru çimende durdu ve damlaları içti. Annesi de yemeğini tamamladı ve Doru'nun yanına geldi. Doru çok sevindi, çünkü hem sesi hem de suyu bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kayanın yanındaki taşlar ıslak ve kaygandı"
   - Cümle 10: «Kayanın yanındaki taşlar ıslak ve kaygandı.»
   - Açıklama: Kaygan taşlar ve kütük tehlike gibi kuruluyor ama olaya katkısı yok, Doru'nun yüksek kayadan damlayan suyu çimende durarak nasıl içtiği de açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0152` birebir aynı, `@degisim: bağcık -> kütük` (tutuyorsan), ardından `@onarim: def35c7113eb5398c022a9be4e783352fc302be8`, sonra gövde.

### Hikâye 9: tohum doru-0154 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0154
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fide', fiil 'köpürmek', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: yola kalın bir dal düşmüştü ve küçük at geçemedi | dalı iterek yolun kenarına yuvarladı
@tohum: doru-0154
@degisim: fide -> dal
Doru Alaca'ya dağda güzel bir su göstermek istiyordu. Bu, Alaca için küçük bir sürpriz olacaktı. Ama yola kalın bir dal düşmüştü ve Alaca onun üstünden geçemedi. "Doru, bu dal benim için çok yüksek," dedi Alaca. Doru ona yardım etmek için dalı burnuyla itti. Dal yolun kenarına yuvarlandı. Alaca kolayca geçti. Az sonra ikisi suyun yanına vardı. Su taşların arasında beyaz beyaz köpürüyordu. "Sürpriz, Alaca!" dedi Doru ve ona sevecen gözlerle baktı. "Çok güzel, teşekkürler, Doru!" dedi Alaca. Alaca sevinçle zıpladı. Doru çok mutlu oldu, çünkü sürprizi Alaca'yı sevindirmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ona sevecen gözlerle baktı"
   - Cümle 10: «"Sürpriz, Alaca!" dedi Doru ve ona sevecen gözlerle baktı.»
   - Açıklama: 'Sevecen gözlerle' soyut bir ifade ve 3 yaşındaki çocuğun bilmeyeceği bir kelime içeriyor.
   - Açıklama: 'Sevecen gözlerle bakmak' kalıplaşmış soyut bir anlatım ve 'sevecen' küçük çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0154` birebir aynı, `@degisim: fide -> dal` (tutuyorsan), ardından `@onarim: f6970c9fc0585c9cc8bad23f467f1d134b5b69cf`, sonra gövde.

### Hikâye 10: tohum doru-0156 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0156
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'sis', fiil 'konmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sisin içinde küçük renkli şeyler kıpırdıyordu | cesaretle çalıya yaklaştı ve kelebekleri gördü
@tohum: doru-0156
Ormanda sabah sisi vardı ve ağaçlar zor görünüyordu. Doru biraz ileride, bir çalının üstünde küçük renkli şeyler gördü. Bunlar kıpırdıyordu, ama Doru sis yüzünden ne olduklarını anlayamadı. Doru önce yerinde durdu. Sonra cesaretle çalıya doğru birkaç adım attı. Çalı sarı çiçeklerle doluydu. Beyaz ve mavi oynak kelebekler çiçeklere konuyor ve yeniden uçuyordu. Doru çalının yanında durdu ve onları uzun uzun izledi. Doru çok mutlu oldu, çünkü sisin içinde ne olduğunu bulmuştu.
```

**Hakem bulguları (1):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "kelebekler çiçeklere konuyor ve yeniden uçuyordu"
   - Cümle 7: «Beyaz ve mavi oynak kelebekler çiçeklere konuyor ve yeniden uçuyordu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun çözümü olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0156` birebir aynı, ardından `@onarim: 391c597420b561efde156e9cced0f3faf22d4e39`, sonra gövde.

### Hikâye 11: tohum doru-0157 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0157
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kaya', fiil 'uyumak', sıfat 'sakin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: gökkuşağı kaybolabilirdi ve annesi uzakta uyuyordu | hızla koşup annesini uyandırdı ve gökkuşağını gösterdi
@tohum: doru-0157
Bir sabah yağmur yeni dinmişti ve dağ çok sakindi. Doru büyük bir kayanın yanında çimen yiyordu. Birden kayanın arkasında, gökyüzünde bir gökkuşağı çıktı. Doru onu annesine göstermek istedi, ama gökkuşağı her an kaybolabilirdi. Annesi biraz uzakta, çimenlerin üstünde uyuyordu. Doru açık ve düz çimenlerde hızla koştu. "Anne, uyan, gökyüzünde bir gökkuşağı var!" dedi Doru. Annesi gözlerini açtı ve başını kaldırdı. Gökkuşağı daha oradaydı. "Ne güzel, Doru!" dedi annesi. Sonra ikisi yan yana durdu ve gökkuşağını mutlu mutlu izledi.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama gökkuşağı her an kaybolabilirdi"
   - Cümle 4: «Doru onu annesine göstermek istedi, ama gökkuşağı her an kaybolabilirdi.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Doru onu annesine göstermek istedi, ama gökkuşağı her an kaybolabilirdi.»
   - Açıklama: Sorun (gökkuşağı kaybolmadan annesine gösterme) ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Gökkuşağı daha oradaydı"
   - Cümle 9: «Gökkuşağı daha oradaydı.»
   - Açıklama: Olumlu cümlede 'daha' 'hâlâ' anlamında konuşma diline özgü ve belirsiz; 'hâlâ oradaydı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0157` birebir aynı, ardından `@onarim: 0d39e6adf3074c545d88831e5784ec1cc304a6e5`, sonra gövde.

### Hikâye 12: tohum doru-0163 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0163
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'nilüfer', fiil 'ışıldamak', sıfat 'çevik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: yanlışlıkla arkadaşının bulduğu papatyayı yedi | cesaretle onun yanına gidip özür diledi
@tohum: doru-0163
@degisim: nilüfer -> papatya
Doru ile Alaca ormanın güneşli bir yerinde oynuyordu. Alaca beyaz bir papatya buldu ve papatya güneşte ışıldıyordu. Ama Doru bakmadan papatyayı çimenle birlikte yedi. Alaca çok üzüldü ve çevik adımlarla biraz uzaklaştı. Doru onun üzgün yüzünü gördü ve papatyayı yediğini anladı. Biraz utandı ama cesaretle Alaca'nın yanına gitti. Doru başını eğdi ve Alaca'dan özür diledi. Alaca başını Doru'nun boynuna dayadı. Sonra ikisi birlikte güneşli yere döndü. Orada yeni papatyalar buldular. Doru ile Alaca papatyaların yanında mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "buldu ve papatya güneşte"
   - Cümle 2: «Alaca beyaz bir papatya buldu ve papatya güneşte ışıldıyordu.»
   - Açıklama: 'Papatya' aynı cümlede gereksiz yere tekrarlanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çevik adımlarla biraz uzaklaştı"
   - Cümle 4: «Alaca çok üzüldü ve çevik adımlarla biraz uzaklaştı.»
   - Açıklama: 'Çevik' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Çevik' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0163` birebir aynı, `@degisim: nilüfer -> papatya` (tutuyorsan), ardından `@onarim: f885c7249436123c8879eff2fa75246d3f1e4e81`, sonra gövde.
