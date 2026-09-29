# Editör görevi (onarım): Doru, onarım partisi 13

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar13.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar13.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0012 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0012
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yiyecek', fiil 'taramak', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşı sırası gelince yapraklara uzanamadı | dalı dişleriyle eğdi ve yaprakları arkadaşının önüne getirdi
@tohum: doru-0012
@degisim: esnek -> ince
Doru ile Alaca parkta sırayla yaprak koparıyordu. Ağacın ince bir dalında yeşil yapraklar vardı. Ama Alaca çok küçüktü ve sırası gelince dala uzanamadı. "Yapraklar çok yüksekte, Doru," dedi Alaca. Alaca çok üzüldü. Doru ona hemen yardım etmek istedi. Dalı gözleriyle taradı ve biraz düşündü. Sonra dişleriyle dalın ucunu tuttu ve yavaşça aşağı çekti. Dal kolayca eğildi ve yapraklar Alaca'nın önüne geldi. "Sıra sende, Alaca," dedi Doru. Alaca bir yaprak kopardı ve keyifle yedi. "Bu, en tatlı yiyecek!" dedi Alaca. Doru çok sevindi, çünkü Alaca da kendi sırasında yaprak yemişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dalı gözleriyle taradı"
   - Cümle 7: «Dalı gözleriyle taradı ve biraz düşündü.»
   - Açıklama: 'Gözleriyle taramak' mecazlı bir anlatım, küçük çocuğa uygun değil.
   - Açıklama: 'Gözleriyle taramak' mecazlı bir anlatım, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0012` birebir aynı, `@degisim: esnek -> ince` (tutuyorsan), ardından `@onarim: 226482a6fbb35a47a10ed8b30e93a65b56b25b27`, sonra gövde.

### Hikâye 2: tohum doru-0016 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0016
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'bezelye', fiil 'okumak', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: sık ağaçlar yüzünden sürünün gittiği yolu göremediler | toprakta sürünün izlerini bulup peşinden yürüdü
@tohum: doru-0016
@degisim: okumak -> bulmak
Ormanda Doru ile Kırat sürünün arkasından gidiyordu. Kırat yavaş yürüyordu ve ikisi geride kaldı. Ağaçlar çok sıktı ve yol görünmüyordu. Doru Kırat'a yardım etmek istedi. Başını eğdi ve yere dikkatle baktı. Toprakta taze ayak izleri buldu. "Kırat, bu izler sürünün mü?" diye sordu Doru. "Evet, Doru, sürü bu yoldan gitmiş," dedi Kırat. İkisi izlere bakarak birlikte yürüdü. Az sonra ağaçların arasında geniş bir çayır gördüler. Sürü orada çimenlerin arasındaki bezelye otlarını yiyordu. İkisi sürünün yanına geldi ve mutlu mutlu yemeye başladı. Doru bundan sonra yolu kaybedince toprakta izleri arardı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bezelye otlarını yiyordu"
   - Cümle 11: «Sürü orada çimenlerin arasındaki bezelye otlarını yiyordu.»
   - Açıklama: Bezelye otu bir sürünün çayırda yediği ot için yanlış ve çocuğun bilmediği bir kelime.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sürü orada çimenlerin arasındaki"
   - Cümle 11: «Sürü orada çimenlerin arasındaki bezelye otlarını yiyordu.»
   - Açıklama: Belirsiz kelime sürü canlı bir grup olarak geçiyor; belirsiz kelimeler karakter olarak kullanılamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0016` birebir aynı, `@degisim: okumak -> bulmak` (tutuyorsan), ardından `@onarim: 345d29e66deb021ed88cfc08e069f77065a6d576`, sonra gövde.

### Hikâye 3: tohum doru-0017 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0017
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'ot', fiil 'gülüşmek', sıfat 'şeffaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: uzun bir ot alnına takıldı ve gözünü kapattı | otu dişleriyle yavaşça çekip çıkardı
@tohum: doru-0017
@degisim: şeffaf -> berrak
Bir sabah Doru ile Alaca dağda çimenlerin üstünde yuvarlanıyordu. Alaca kalktı ve derenin berrak suyuna baktı. Alnına uzun bir ot takılmıştı ve ot bir gözünün önüne sarkıyordu. Alaca başını salladı ama ot düşmedi. "Doru, otu çıkaramıyorum," dedi Alaca. Doru hemen ona yardım etmek istedi. Otu dişleriyle yavaşça tuttu ve çekti. Ot alnından çıktı ve yere düştü. Alaca yine suya baktı. "Şimdi her şeyi iyi görüyorum!" dedi Alaca. İkisi gülüştü. Alaca bundan sonra alnında ot olunca hemen Doru'ya söylerdi.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "hemen Doru'ya söylerdi"
   - Cümle 12: «Alaca bundan sonra alnında ot olunca hemen Doru'ya söylerdi.»
   - Açıklama: Anlatım -dı'lı geçmişten '-ardı' kalıbına kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0017` birebir aynı, `@degisim: şeffaf -> berrak` (tutuyorsan), ardından `@onarim: 6ad1464f2548af30af2f32cdc8dc4e06522a995d`, sonra gövde.

### Hikâye 4: tohum doru-0018 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0018
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'dal', fiil 'mırıldanmak', sıfat 'siyah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: vadiye giden yolu bulamadı çünkü ağaçlar birbirine benziyordu | hızla küçük arkadaşına koşup yardım istedi
@tohum: doru-0018
Doru ormanda dolaşıyordu. Sonra sürünün yanına dönmek istedi. Ama vadiye giden yolu bulamadı, çünkü ağaçların siyah dalları birbirine benziyordu. Doru, Alaca'nın yakındaki bir çimenlikte oynadığını biliyordu. Uzakta Alaca şarkı mırıldanıyordu. Doru sese doğru yürüdü ve açık, düz bir çimenliğe çıktı. Alaca oradaydı ve sürüye doğru gidiyordu. Doru hızla koştu ve ona yetişti. "Alaca, bana yardım eder misin? Yolu bulamıyorum," dedi Doru. "Tabii, Doru, benimle gel," dedi Alaca. İkisi yan yana yürüdü ve az sonra vadiyi gördü. Doru çok sevindi, çünkü Alaca'dan yardım istemişti.
```

**Hakem bulguları (3):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "hızla küçük arkadaşına koşup yardım istedi"
   - Cümle 0 (plan satırı): «vadiye giden yolu bulamadı çünkü ağaçlar birbirine benziyordu | hızla küçük arkadaşına koşup yardım istedi»
   - Açıklama: Kartın yanlar ilişkisinde Alaca'ya Doru yardım eder, burada ilişki tersine dönüyor.
   - Açıklama: Kartın yanlar ilişkisinde Alaca Doru'dan öğrenen ve yardım alan en küçük üyedir; burada ilişki tersine çevriliyor.
   - Açıklama: Kartın Alaca ilişki alanına göre sürünün en küçüğü Alaca Doru'dan öğrenir ve ona yardım edilir, burada ise yolunu kaybeden Doru'ya yol gösteren Alaca oluyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Uzakta Alaca şarkı mırıldanıyordu"
   - Cümle 5: «Uzakta Alaca şarkı mırıldanıyordu.»
   - Açıklama: Bir önceki cümlede Alaca yakındaki çimenlikte deniyor, hemen ardından uzakta olduğu söyleniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru sese doğru yürüdü"
   - Cümle 6: «Doru sese doğru yürüdü ve açık, düz bir çimenliğe çıktı.»
   - Açıklama: Çözüm sese yürümek, çimenliğe çıkmak, koşup yetişmek ve yardım istemek gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0018` birebir aynı, ardından `@onarim: bd02ddc2400213753b9436da8b325540eed62b79`, sonra gövde.

### Hikâye 5: tohum doru-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0019
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çöp', fiil 'aşmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yaprak derede iki taşın arasına takıldı | hızla geri koşup yaprağı burnuyla taşlardan itti
@tohum: doru-0019
@degisim: çöp -> yaprak
Rüzgar dağda hafif hafif esiyordu. Doru küçük bir derenin yanındaki düz çimenlerde oynuyordu. Suyun üstünde güzel bir yaprak gidiyordu ve Doru onunla yarışıyordu. Ama birden yaprak iki taşın arasına takıldı. Yaprak taşları aşamadı ve olduğu yerde kaldı. Doru o sırada biraz ileri gitmişti ve geri baktı. Sonra çimenlerde hızla geri koştu ve yaprağın yanına vardı. Taşlar kıyıya çok yakındı. Doru burnuyla yaprağı yavaşça itti. Yaprak taşların arasından çıktı ve su onu yeniden götürdü. Doru yine suyun yanında onunla yarıştı. Doru çok sevindi, çünkü yarış oyunu yeniden başlamıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama birden yaprak iki taşın arasına takıldı"
   - Cümle 4: «Ama birden yaprak iki taşın arasına takıldı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0019` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: 56482664105930b7307c3c029ed55518041bdbda`, sonra gövde.

### Hikâye 6: tohum doru-0024 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0024
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kova', fiil 'kurutmak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: kayanın arkasından garip bir ıslık sesi geldi | cesurca gidip sesi yapan rüzgarı buldu
@tohum: doru-0024
@degisim: pürüzsüz -> düz
Dağda yağmur yeni dinmişti. Doru ile Kırat ıslak tüylerini kurutmak için güneşli bir kayaya gidiyordu. Birden kayanın arkasından garip bir ıslık sesi geldi. Kırat durdu ve kulaklarını dikti. "Doru, bu sese bir bakar mısın?" dedi Kırat. Doru cesurca kayanın arkasına yürüdü ve baktı. Kayada kova gibi yuvarlak bir delik vardı. Rüzgar bu delikten geçince ince bir ses çıkıyordu. "Gel, Kırat, bu sesi rüzgar yapıyor!" dedi Doru. Kırat da geldi ve deliğe baktı. İkisi düz kayanın yanında güneşte durdu ve tüyleri kurudu. "Teşekkürler, Doru, artık o sesi biliyoruz!" dedi Kırat.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kayada kova gibi yuvarlak"
   - Cümle 7: «Kayada kova gibi yuvarlak bir delik vardı.»
   - Açıklama: Kova bir ev eşyasıdır ve kartın doğa dünyasında yer almaz.
   - Açıklama: Kova bir ev eşyası; kartın doğa dünyasında ve tohum yasak kategorilerinde (ev_esyasi) olmayan bir nesne getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0024` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: c6c67e57b5a17c45c1997c449cf4459c3f155cfe`, sonra gövde.

### Hikâye 7: tohum doru-0026 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0026
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bulut', fiil 'giydirmek', sıfat 'meraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: sırası gelince rüzgar bulutun gölgesini uzağa götürdü | düz vadide hızla koşup gölgeye yetişti
@tohum: doru-0026
@degisim: giydirmek -> koşmak
Doru ile annesi vadide sırayla gölge yakalama oyunu oynuyordu. Önce annesi koştu ve büyük bir bulutun gölgesine bastı. Şimdi sıra Doru'daydı, ama rüzgar bulutu uzağa götürüyordu. Bulutun gölgesi de çimenlerin üstünde vadinin öbür ucuna gidiyordu. "Acele et, Doru, gölge gidiyor!" dedi annesi. Doru gölgenin gittiği yere baktı. Orada vadi açık ve düzdü. Annesi meraklı gözlerle onu izledi. Doru hızla koştu ve az sonra gölgeye yetişti. Sonra dört ayağıyla gölgenin içine bastı. "Yakaladım, anne!" dedi Doru. Annesi de yanına geldi ve güldü. "Çok güzel oynadın, Doru!" dedi annesi. "Teşekkürler, anneciğim, şimdi yine sıra sende!" dedi Doru.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sırayla gölge yakalama oyunu"
   - Cümle 1: «Doru ile annesi vadide sırayla gölge yakalama oyunu oynuyordu.»
   - Açıklama: Kartın güvenli özellik kullanımı satırı kovalamacanın hikayeye girmediğini söylüyor; hız bir yakalama oyununda kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0026` birebir aynı, `@degisim: giydirmek -> koşmak` (tutuyorsan), ardından `@onarim: a6cdcc33b9701257efdefa509b109d63a655dd54`, sonra gövde.

### Hikâye 8: tohum doru-0030 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0030
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'meyve', fiil 'öğretmek', sıfat 'basit'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: oyunda itilen meyve sık çalıların arasına yuvarlandı | cesaretle çalılara girip meyveyi dışarı itti
@tohum: doru-0030
Ormanda Doru, Alaca'ya basit bir oyun öğretiyordu. Sırayla burunlarıyla bir meyveyi itip büyük ağaca götüreceklerdi. Ama Alaca meyveyi sert itti ve meyve sık çalıların arasına yuvarlandı. "Oraya girmekten korkuyorum," dedi Alaca. Doru çalılara baktı ve cesaretle aralarına girdi. Meyveyi burnuyla dikkatlice dışarı itti. "İşte meyve burada, sıra yine sende, Alaca," dedi Doru. Alaca bu sefer meyveyi yavaşça itti. Meyve çimenlerde ilerledi ve ağaca ulaştı. "Başardım, Doru!" dedi Alaca. Sonra sıra Doru'ya geldi ve o da meyveyi ağaca götürdü. Doru çok sevindi, çünkü oyunları yeniden eğlenceli olmuştu.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "cesaretle çalılara girip meyveyi dışarı itti"
   - Cümle 0 (plan satırı): «oyunda itilen meyve sık çalıların arasına yuvarlandı | cesaretle çalılara girip meyveyi dışarı itti»
   - Açıklama: Planda meyveyi Doru itiyor, gövdede ise Alaca itiyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Oraya girmekten korkuyorum"
   - Cümle 4: «"Oraya girmekten korkuyorum," dedi Alaca.»
   - Açıklama: Alaca çalılara girmekten korkuyor ama çalıların içindeki meyveyi o dışarı itiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0030` birebir aynı, ardından `@onarim: 945a1a1f0626839650f09ea799bdab46eec1b938`, sonra gövde.

### Hikâye 9: tohum doru-0031 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0031
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'salatalık', fiil 'sabırsızlanmak', sıfat 'şık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: ağaçta tek elma vardı ve ikisi de acıkmıştı | hızla koşup elmayı getirdi ve yarısını arkadaşına verdi
@tohum: doru-0031
@degisim: salatalık -> elma
Dağda, vadinin öbür ucunda küçük bir elma ağacı vardı. Doru ağacın alçak dalında kırmızı bir elma gördü. Elma bir taneydi, ama Doru da Karatay da acıkmıştı. Karatay sabırsızlandı ve yerinde zıpladı. Şık, siyah yelesi iki yana sallandı. "Elmayı getireyim, ikimiz paylaşalım," dedi Doru. Doru düz vadide hızla koştu. Ağaca varınca elmayı dişleriyle daldan kopardı. Sonra Karatay'ın yanına geri döndü. Elmanın yarısını yedi ve öbür yarısını Karatay'a verdi. "Teşekkürler, Doru, çok tatlıymış," dedi Karatay. Doru bundan sonra bulduğu her elmayı arkadaşıyla paylaştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şık, siyah yelesi"
   - Cümle 5: «Şık, siyah yelesi iki yana sallandı.»
   - Açıklama: 'Şık' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şık, siyah yelesi iki yana sallandı"
   - Cümle 5: «Şık, siyah yelesi iki yana sallandı.»
   - Açıklama: Yelenin kime ait olduğu belli değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şık, siyah yelesi iki yana sallandı"
   - Cümle 5: «Şık, siyah yelesi iki yana sallandı.»
   - Açıklama: Karatay'ın yelesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Yele betimi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0031` birebir aynı, `@degisim: salatalık -> elma` (tutuyorsan), ardından `@onarim: b0ab48caca3ebeeff956843eca6287b39237bcdd`, sonra gövde.

### Hikâye 10: tohum doru-0032 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0032
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kaktüs', fiil 'fısıldamak', sıfat 'gizemli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: çalının üstündeki çiçek açılıyordu ama annesi uzaktaydı | hızla koşup annesini çiçeğin yanına getirdi
@tohum: doru-0032
@degisim: kaktüs -> çalı
Dağda, geniş ve düz bir çimenlikte büyük bir çalı vardı. Doru çalının üstünde pembe bir tomurcuk gördü. Tomurcuk açılıyordu, ama Doru'nun annesi uzakta çimen yiyordu. Doru bu çiçeği annesine göstermek istedi. Doru çimenlikte hızla koştu ve annesinin yanına vardı. Doru annesinin kulağına eğildi. "Anne, benimle gel, sana gizemli bir sürpriz var," diye fısıldadı Doru. Annesi gülümsedi ve Doru'nun yanında çalıya yürüdü. Çalının üstündeki pembe çiçek tam açılmıştı. Annesi çiçeğe uzun uzun baktı. Doru sevinçle annesine sokuldu. "Ne güzel bir sürpriz, teşekkür ederim, Doru!" dedi annesi.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru çimenlikte hızla koştu"
   - Cümle 5: «Doru çimenlikte hızla koştu ve annesinin yanına vardı.»
   - Açıklama: Üst üste cümleler gereksiz yere 'Doru' adıyla başlıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sana gizemli bir sürpriz"
   - Cümle 7: «"Anne, benimle gel, sana gizemli bir sürpriz var," diye fısıldadı Doru.»
   - Açıklama: 'Gizemli' kelimesi soyut ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sana gizemli bir sürpriz var"
   - Cümle 7: «"Anne, benimle gel, sana gizemli bir sürpriz var," diye fısıldadı Doru.»
   - Açıklama: 'Gizemli' soyut bir kelime ve 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0032` birebir aynı, `@degisim: kaktüs -> çalı` (tutuyorsan), ardından `@onarim: 3d2398becb5f59147c220e3359fe80f57b1fa2fe`, sonra gövde.

### Hikâye 11: tohum doru-0034 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0034
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çit', fiil 'doğmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: bir kayanın arkasından garip bir ses geliyordu | sesi bulup fidanın üstündeki kuru dalı çekti
@tohum: doru-0034
@degisim: çit -> fidan
Bir sabah güneş dağın arkasından doğdu. Doru çimen yerken garip bir tak tak sesi duydu. Ses büyük bir kayanın arkasından geliyordu ve Doru onu çok merak etti. Kayanın arkasına yavaşça yürüdü ve baktı. Orada küçük bir fidan vardı. Fidanın üstüne kuru ve uzun bir dal düşmüştü. Rüzgar esince dal kayaya çarpıyor ve ses çıkarıyordu. Doru fidanı dalın altında görünce mutsuz oldu ve ona yardım etmek istedi. Kuru dalı dişleriyle tuttu ve kenara çekti. Dal artık kayaya çarpmadı ve garip ses de bitti. Doru orada çimen yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Doru fidanı dalın altında görünce mutsuz oldu"
   - Cümle 8: «Doru fidanı dalın altında görünce mutsuz oldu ve ona yardım etmek istedi.»
   - Açıklama: Sorun garip sesten dal altındaki fidana kayıyor; hikayede iki ayrı sorun var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0034` birebir aynı, `@degisim: çit -> fidan` (tutuyorsan), ardından `@onarim: 38aec002a58172a4102d37cba0640b9d738cd628`, sonra gövde.

### Hikâye 12: tohum doru-0035 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0035
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'yün', fiil 'bağlamak', sıfat 'sevinçli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: oynarken annesinin sırtına çamur sıçradı | cesaretle özür diledi ve annesinin sırtını yıkadı
@tohum: doru-0035
@degisim: bağlamak -> yıkamak
Ormanda, bir çalının dalında bir tutam yumuşak yün vardı. Doru orada zıplayarak oynuyordu. Birden çamurlu bir yere bastı ve çamur annesinin sırtına sıçradı. Annesi başını çevirdi ve kirli sırtına baktı. Doru önce biraz utandı. Sonra cesaretle annesinin yanına gitti. "Özür dilerim, anne, daha dikkatli oynayacağım," dedi Doru. Annesi sevinçli bir sesle güldü. "Önemli değil, Doru, çamur suyla temizlenir," dedi annesi. Doru çalıdaki yünü dişleriyle aldı. İkisi birlikte yakındaki küçük dereye gitti. Doru yünü derede ıslattı ve annesinin sırtını yıkadı. Doru çok sevindi, çünkü annesinin sırtı yine tertemiz olmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir tutam yumuşak yün"
   - Cümle 1: «Ormanda, bir çalının dalında bir tutam yumuşak yün vardı.»
   - Açıklama: 'Tutam' kelimesini 3 yaşındaki çocuk bilmez.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bir tutam yumuşak yün"
   - Cümle 1: «Ormanda, bir çalının dalında bir tutam yumuşak yün vardı.»
   - Açıklama: Yün kartın kapalı dünyasında olmayan, koyun ya da insan dünyasını çağrıştıran bir eşya olarak kullanılıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru çalıdaki yünü dişleriyle aldı"
   - Cümle 10: «Doru çalıdaki yünü dişleriyle aldı.»
   - Açıklama: Özürden sonra yünü alma, dereye gitme ve yıkama ile çözüm iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0035` birebir aynı, `@degisim: bağlamak -> yıkamak` (tutuyorsan), ardından `@onarim: 264741f28a6dc85115add173807a163f604051b7`, sonra gövde.
