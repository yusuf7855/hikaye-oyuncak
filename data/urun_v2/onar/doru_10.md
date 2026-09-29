# Editör görevi (onarım): Doru, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0012 (deneme 4 -> 5)

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
@degisim: taramak -> bakmak
Doru ile Alaca geniş çayırda sırayla yaprak koparıyordu. Ağacın esnek bir dalında yeşil yapraklar vardı. Ama Alaca çok küçüktü ve sırası gelince dala uzanamadı. "Yapraklar çok yüksekte, Doru," dedi Alaca. Alaca çok üzüldü. Doru ona hemen yardım etmek istedi. Dala baktı ve biraz düşündü. Sonra dişleriyle dalın ucunu tuttu ve yavaşça aşağı çekti. Dal kolayca eğildi ve yapraklar Alaca'nın önüne geldi. "Sıra sende, Alaca," dedi Doru. Alaca bir yaprak kopardı ve keyifle yedi. "Bu, en tatlı yiyecek!" dedi Alaca. Doru çok sevindi, çünkü Alaca da kendi sırasında yaprak yemişti.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Alaca geniş çayırda"
   - Cümle 1: «Doru ile Alaca geniş çayırda sırayla yaprak koparıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "geniş çayırda sırayla yaprak koparıyordu"
   - Cümle 1: «Doru ile Alaca geniş çayırda sırayla yaprak koparıyordu.»
   - Açıklama: Başlıktaki yer park iken hikaye bir çayırda geçiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ağacın esnek bir dalında"
   - Cümle 2: «Ağacın esnek bir dalında yeşil yapraklar vardı.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0012` birebir aynı, `@degisim: taramak -> bakmak` (tutuyorsan), ardından `@onarim: ae2ee56e119c0f73f13b6f8f0db9e5f6e8c787b0`, sonra gövde.

### Hikâye 2: tohum doru-0015 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0015
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'domates', fiil 'katılmak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sürüye giden yolda çalılardan garip bir ses geldi | cesaretle çalılara baktı ve damlayan suyu buldu
@tohum: doru-0015
@degisim: domates -> damla
Doru yağmurdan sonra ormanda dolaşıyordu. Şimdi vadideki sürüsüne dönmek istiyordu. Ama yolun yanındaki çalılardan tık tık diye garip bir ses geliyordu. Doru bu sesi tanımadı ve yolda durdu. Sonra cesaretle çalılara yaklaştı ve başını uzatıp baktı. Çalıların arasında düz bir taş vardı. Taşın üstüne ıslak dallardan damla damla su düşüyordu. Her damla taşa değince tık diye bir ses çıkıyordu. Doru sesin nereden geldiğini bulmuştu. Artık hiç durmadı ve yoluna devam etti. Az sonra vadiye vardı ve sürüye katıldı. Doru orada yumuşacık çimenleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Az sonra vadiye vardı ve sürüye katıldı"
   - Cümle 11: «Az sonra vadiye vardı ve sürüye katıldı.»
   - Açıklama: Hikaye ormanda başlıyor ama vadide bitiyor; tek sahne kuralı çiğneniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0015` birebir aynı, `@degisim: domates -> damla` (tutuyorsan), ardından `@onarim: 71bc687cad8e1c387f5350206a4c2b42280ab650`, sonra gövde.

### Hikâye 3: tohum doru-0016 (deneme 4 -> 5)

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
Ormanda Doru ile Kırat sürünün arkasından gidiyordu. Kırat yavaş yürüyordu ve ikisi geride kaldı. Ağaçlar çok sıktı ve yol görünmüyordu. Doru Kırat'a yardım etmek istedi. Başını eğdi ve yere dikkatle baktı. Toprakta sürünün taze ayak izlerini buldu. "Bak, Kırat, izler bu yoldan gidiyor," dedi Doru. İkisi izlere bakarak birlikte yürüdü. Az sonra ağaçların arasında geniş bir çayır gördüler. Sürü orada çimenlerin arasındaki bezelye otlarını yiyordu. İkisi sürünün yanına geldi ve mutlu mutlu yemeye başladı. Doru bundan sonra yolu kaybedince toprakta izleri arardı.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Bak, Kırat, izler bu yoldan gidiyor"
   - Cümle 7: «"Bak, Kırat, izler bu yoldan gidiyor," dedi Doru.»
   - Açıklama: Kartın yanlar ilişkisinde Kırat en çok bilen ve danışılan yaşlı attır, burada yolu bilemeyip Doru'dan öğreniyor.
   - Açıklama: Kartın ilişki alanına göre en çok Kırat bilir ve ona danışılır; burada yolu bilemeyen ve Doru'ya uyan Kırat'tır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0016` birebir aynı, `@degisim: okumak -> bulmak` (tutuyorsan), ardından `@onarim: e8b415d65cd903dd8a640ca20dd9a18eb8a457bb`, sonra gövde.

### Hikâye 4: tohum doru-0017 (deneme 4 -> 5)

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
Bir sabah Doru ile Alaca dağda çimenlerin üstünde yuvarlanıyordu. Alaca kalktı ve derenin berrak suyuna baktı. Alnına uzun bir ot takılmıştı ve ot bir gözünün önüne sarkıyordu. Alaca başını salladı ama ot düşmedi. "Doru, otu çıkaramıyorum," dedi Alaca. Doru hemen ona yardım etmek istedi. Otu dişleriyle yavaşça tuttu ve çekti. Ot alnından çıktı ve yere düştü. Alaca yine suya baktı. "Şimdi her şeyi iyi görüyorum!" dedi Alaca. İkisi birlikte gülüştü. Alaca bundan sonra alnında ot olunca hemen Doru'ya söylerdi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "İkisi birlikte gülüştü"
   - Cümle 11: «İkisi birlikte gülüştü.»
   - Açıklama: 'Gülüşmek' zaten birlikteliği anlatır; 'birlikte' gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0017` birebir aynı, `@degisim: şeffaf -> berrak` (tutuyorsan), ardından `@onarim: a4952d3ce69cd5dc2a6401b5433f20ced1b0adc8`, sonra gövde.

### Hikâye 5: tohum doru-0018 (deneme 4 -> 5)

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
Doru ormanda dolaşıyordu. Sonra sürünün yanına dönmek istedi. Ama vadiye giden yolu bulamadı çünkü ağaçlar birbirine benziyordu. Birden yakından hafif bir ses geldi. Alaca açık ve düz bir çimenlikte şarkı mırıldanıyordu. Doru çimenliğe çıktı ve hızla onun yanına koştu. "Alaca, bana yardım eder misin? Vadinin yolunu bulamıyorum," dedi Doru. "Siyah dalı olan ağacın yanından gidiyoruz, bunu sen öğrettin," dedi Alaca. Alaca başını çevirdi ve büyük bir ağacı gösterdi. Ağacın bir dalı siyahtı. Doru o ağacı hemen hatırladı. İkisi ağacın yanından yürüdü ve az sonra vadiyi gördü. Doru çok sevindi, çünkü Alaca'dan yardım istemişti ve yolu bulmuştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden yakından hafif bir ses geldi"
   - Cümle 4: «Birden yakından hafif bir ses geldi.»
   - Açıklama: Alaca tam gerektiği anda sebepsizce beliriyor ve çözümü getiriyor.
   - Açıklama: Alaca sebepsizce tam gereken anda yakında beliriyor ve çözümü getiriyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hızla onun yanına koştu"
   - Cümle 6: «Doru çimenliğe çıktı ve hızla onun yanına koştu.»
   - Açıklama: Tohumdaki hız özelliği sorunun çözümünde işe yaramıyor; Alaca zaten yakındadır ve yolu Alaca'nın hatırlatması bulduruyor.
   - Açıklama: Tohumdaki hız özelliği sorunu çözmüyor; yol Alaca'ya sorularak bulunuyor, hız süs olarak kalıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Siyah dalı olan ağacın yanından gidiyoruz, bunu sen öğrettin"
   - Cümle 9: «"Siyah dalı olan ağacın yanından gidiyoruz, bunu sen öğrettin," dedi Alaca.»
   - Açıklama: Yolu Alaca'ya öğreten Doru'nun yolu bilmemesi ve ağaçların birbirine benzediğinin söylenip sonra siyah dallı ayırt edici bir ağaç çıkması çelişkili.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bunu sen öğrettin"
   - Cümle 9: «"Siyah dalı olan ağacın yanından gidiyoruz, bunu sen öğrettin," dedi Alaca.»
   - Açıklama: Yolu işaretleyen ağacı Alaca'ya Doru öğretmişken yolu bulamaması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0018` birebir aynı, ardından `@onarim: 2c53eae9d66c01678cd8c645c03795b663d78805`, sonra gövde.

### Hikâye 6: tohum doru-0019 (deneme 4 -> 5)

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
Rüzgar dağda hafif hafif esiyordu. Doru küçük bir derenin yanındaki düz çimenlerde oynuyordu. Suyun üstünde güzel bir yaprak gidiyordu ve Doru onunla yarışıyordu. Ama birden yaprak iki taşın arasına takıldı. Yaprak taşları aşamadı ve olduğu yerde kaldı. Doru o sırada biraz ileri gitmişti ve geri baktı. Sonra çimenlerde hızla geri koştu ve yaprağın yanına vardı. Dere orada çok sığdı. Doru burnuyla yaprağı yavaşça itti. Yaprak taşların arasından çıktı ve su onu yeniden götürdü. Doru yine suyun yanında onunla yarıştı. Doru çok sevindi, çünkü yarış oyunu yeniden başlamıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dere orada çok sığdı"
   - Cümle 8: «Dere orada çok sığdı.»
   - Açıklama: 'Sığ' kelimesi küçük çocuk için zor ve 'sığmak' fiiliyle karışıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0019` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: 8383132aa1397c1d8e45100e2bf80e143d6bab6d`, sonra gövde.

### Hikâye 7: tohum doru-0024 (deneme 3 -> 4)

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
@degisim: kova -> kaya
Dağda yağmur yeni dinmişti. Doru ile Kırat ıslak tüylerini kurutmak için güneşli bir kayaya gidiyordu. Birden kayanın arkasından garip bir ıslık sesi geldi. Kırat durdu ve kulaklarını dikti. "Doru, bu sese bir bakar mısın?" dedi Kırat. Doru cesurca kayanın arkasına yürüdü ve baktı. Kayada yuvarlak bir delik vardı. Rüzgar bu delikten geçince ince bir ses çıkıyordu. "Gel, Kırat, bu sesi rüzgar yapıyor!" dedi Doru. Kırat da geldi ve deliğe baktı. İkisi pürüzsüz kayanın yanında güneşte durdu ve tüyleri kurudu. "Teşekkürler, Doru, artık o sesi biliyoruz!" dedi Kırat.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İkisi pürüzsüz kayanın yanında"
   - Cümle 11: «İkisi pürüzsüz kayanın yanında güneşte durdu ve tüyleri kurudu.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İkisi pürüzsüz kayanın"
   - Cümle 11: «İkisi pürüzsüz kayanın yanında güneşte durdu ve tüyleri kurudu.»
   - Açıklama: 'Pürüzsüz' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0024` birebir aynı, `@degisim: kova -> kaya` (tutuyorsan), ardından `@onarim: 5e146cfbda1178f6b0d6aa603466327ca787da32`, sonra gövde.

### Hikâye 8: tohum doru-0025 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0025
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yıldız', fiil 'doyurmak', sıfat 'ışıltılı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: arkadaşı acıktı ama başka elma kalmamıştı | bulduğu elmaların yarısını arkadaşına verdi
@tohum: doru-0025
@degisim: ışıltılı -> parlak
Ormanda büyük bir elma ağacı vardı. Doru ağacın dibinde yıldız gibi parlak dört elma buldu. Az sonra aç Karatay koşarak geldi, ama ağaçta başka elma kalmamıştı. Karatay boş dallara baktı ve üzüldü. Doru arkadaşına yardım etmek istedi. "Gel, Karatay, bu elmaları paylaşalım," dedi Doru. Sonra iki elmayı burnuyla Karatay'ın önüne itti. İki arkadaş elmaları çimenlerin üstünde yan yana yedi. Tatlı elmalar ikisini de doyurdu. Karatay kuyruğunu neşeyle salladı. Doru çok sevindi, çünkü elmalarını arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yıldız gibi parlak dört elma"
   - Cümle 2: «Doru ağacın dibinde yıldız gibi parlak dört elma buldu.»
   - Açıklama: Elmaların yıldız gibi parlaması mecazdır; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Elmaların yıldız gibi parlaması mecazlı bir benzetme.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0025` birebir aynı, `@degisim: ışıltılı -> parlak` (tutuyorsan), ardından `@onarim: 308bb818bdf4f4c867c6a4e9086265a3310b3708`, sonra gövde.

### Hikâye 9: tohum doru-0026 (deneme 3 -> 4)

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
Doru ile annesi vadide sırayla gölge yakalama oyunu oynuyordu. Önce annesi koştu ve büyük bir bulutun gölgesine bastı. Şimdi sıra Doru'daydı, ama rüzgar bulutu uzağa götürüyordu. Bulutun gölgesi de çimenlerin üstünde vadinin öbür ucuna gidiyordu. "Acele et, Doru, gölge gidiyor!" dedi annesi. Meraklı Doru gölgenin gittiği yere baktı. Orada vadi açık ve düzdü. Doru hızla koştu ve az sonra gölgeye yetişti. Sonra dört ayağıyla gölgenin içine bastı. "Yakaladım, anne!" dedi Doru. Annesi de yanına geldi ve güldü. "Çok güzel oynadın, Doru!" dedi annesi. "Teşekkürler, anneciğim, şimdi yine sıra sende!" dedi Doru.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Meraklı Doru gölgenin gittiği"
   - Cümle 6: «Meraklı Doru gölgenin gittiği yere baktı.»
   - Açıklama: Tohumdaki özellik hız; kartta olmayan merak ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik hız; kartın özellikler alanında olmayan meraklılık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0026` birebir aynı, `@degisim: giydirmek -> koşmak` (tutuyorsan), ardından `@onarim: 0bb7e316fc852a33c1ba74805e01424882af36bb`, sonra gövde.

### Hikâye 10: tohum doru-0027 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0027
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kırıntı', fiil 'çoğalmak', sıfat 'şirin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: uzaktan gelen bir ses yüzünden uyuyamadı | hızla koşup taşa vuran kuru dalı çimene bıraktı
@tohum: doru-0027
@degisim: kırıntı -> dal
Rüzgar esiyordu. Doru geniş çayırda şirin çiçeklerin arasına uzanmıştı. Uyumak istiyordu ama uzaktan tık tık diye bir ses geliyordu. Doru bu ses yüzünden uyuyamadı. Rüzgar daha çok esti ve sesler çoğaldı. Doru sesin nereden geldiğini merak etti. Ses çayırın öbür ucundaki taşlardan geliyordu. Doru kalktı ve düz çimende hızla koştu. Az sonra taşlara vardı. Taşların üstünde kuru bir dal vardı. Rüzgar esince dal taşa vuruyor ve tık tık ediyordu. Doru dalı dişleriyle tuttu ve yumuşak çimene bıraktı. Tık tık sesi durdu. Doru çiçeklerin arasına geri döndü ve mutlu mutlu uyudu.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru geniş çayırda şirin"
   - Cümle 2: «Doru geniş çayırda şirin çiçeklerin arasına uzanmıştı.»
   - Açıklama: Başlıktaki yer park iken hikaye bir çayırda geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru geniş çayırda şirin çiçeklerin arasına uzanmıştı"
   - Cümle 2: «Doru geniş çayırda şirin çiçeklerin arasına uzanmıştı.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor ve park hiç kurulmuyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru bu ses yüzünden uyuyamadı"
   - Cümle 4: «Doru bu ses yüzünden uyuyamadı.»
   - Açıklama: Bir önceki cümlede anlatılan durum gereksiz yere tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0027` birebir aynı, `@degisim: kırıntı -> dal` (tutuyorsan), ardından `@onarim: bcabdd5d82afa30d9daa69765534557b0626dae7`, sonra gövde.

### Hikâye 11: tohum doru-0031 (deneme 2 -> 3)

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
Dağda, vadinin öbür ucunda küçük bir elma ağacı vardı. Doru ağacın alçak dalında kırmızı bir elma gördü. Elma bir taneydi, ama Doru da Karatay da acıkmıştı. Karatay sabırsızlandı ve şık, siyah yelesini salladı. "Elmayı getireyim, ikimiz paylaşalım," dedi Doru. Doru düz vadide hızla koştu. Ağaca varınca elmayı dişleriyle daldan kopardı. Sonra Karatay'ın yanına geri döndü. Elmanın yarısını yedi ve öbür yarısını Karatay'a verdi. "Teşekkürler, Doru, çok tatlıymış," dedi Karatay. Doru bundan sonra bulduğu her elmayı arkadaşıyla paylaştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sabırsızlandı ve şık, siyah yelesini"
   - Cümle 4: «Karatay sabırsızlandı ve şık, siyah yelesini salladı.»
   - Açıklama: 'Sabırsızlandı' ve 'şık' kelimeleri 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay sabırsızlandı ve şık, siyah yelesini"
   - Cümle 4: «Karatay sabırsızlandı ve şık, siyah yelesini salladı.»
   - Açıklama: 'Sabırsızlandı' ve 'şık' 3 yaşındaki bir çocuğun bilmeyeceği soyut kelimelerdir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0031` birebir aynı, `@degisim: salatalık -> elma` (tutuyorsan), ardından `@onarim: a2fe6e8cd26bd8aa92b3c71cbbca6f243d4df97b`, sonra gövde.

### Hikâye 12: tohum doru-0032 (deneme 2 -> 3)

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
@plan: çalıdaki çiçek açılıyordu ama annesi uzaktaydı | hızla koşup annesini çiçeğin yanına getirdi
@tohum: doru-0032
@degisim: kaktüs -> çalı
Dağda, güneşli bir tepede büyük bir çalı vardı. Doru çalının üstünde gizemli, pembe bir tomurcuk gördü. Tomurcuk açılıyordu, ama Doru'nun annesi vadinin öbür ucundaydı. Doru bu çiçeği annesine göstermek istedi. Doru düz vadide hızla koştu. Annesi orada çimen yiyordu. Doru annesinin kulağına eğildi. "Anne, benimle gel, sana bir sürpriz var," diye fısıldadı Doru. Annesi gülümsedi ve Doru'nun yanında tepeye yürüdü. Çalının üstündeki pembe çiçek tam açılmıştı. Annesi çiçeğe uzun uzun baktı. Doru sevinçle annesine sokuldu. "Ne güzel bir sürpriz, teşekkür ederim, Doru!" dedi annesi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gizemli, pembe bir tomurcuk"
   - Cümle 2: «Doru çalının üstünde gizemli, pembe bir tomurcuk gördü.»
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru düz vadide hızla koştu"
   - Cümle 5: «Doru düz vadide hızla koştu.»
   - Açıklama: Hikaye tepedeki çalıdan vadinin öbür ucuna geçip geri dönüyor; tek sahne kuralı zorlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0032` birebir aynı, `@degisim: kaktüs -> çalı` (tutuyorsan), ardından `@onarim: 8ce40d34629cb0abfdfc8e1162c0a58209d7d681`, sonra gövde.
