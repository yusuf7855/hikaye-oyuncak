# Editör görevi (onarım): Doru, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0135 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0135
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'ay', fiil 'çizmek', sıfat 'bembeyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kütüğün üstünden atlamayı hiç denememişti | yere bir çizgi çizdi ve cesaretle atladı
@tohum: doru-0135
@degisim: ay -> kütük
Rüzgar çayırda hafif hafif esiyordu. Doru çayırın ortasında bembeyaz, küçük bir kütük gördü. Doru bu kütüğün üstünden atlamak istedi, ama bunu hiç denememişti. Kütüğün önüne gelince durdu ve düşündü. Doru beş adım geri gitti. Ayağıyla yere uzun bir çizgi çizdi. Buradan koşmaya başlayacaktı. Doru çizginin arkasına geçti ve kütüğe baktı. Sonra cesaretle koştu ve kütüğün üstünden atladı. Dört ayağı da yumuşak çimenlere indi. Doru sevinçle başını salladı. Doru bundan sonra yeni bir şeyi denemekten hiç korkmadı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Rüzgar çayırda hafif hafif esiyordu"
   - Cümle 1: «Rüzgar çayırda hafif hafif esiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve geçiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama bunu hiç denememişti"
   - Cümle 3: «Doru bu kütüğün üstünden atlamak istedi, ama bunu hiç denememişti.»
   - Açıklama: Hiç denememiş olmak bir sorun ya da engel olarak kurulmuyor; korku ya da zorluk sebebi söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0135` birebir aynı, `@degisim: ay -> kütük` (tutuyorsan), ardından `@onarim: 69093e4908fc47ab4331ff09f586e074dab823de`, sonra gövde.

### Hikâye 2: tohum doru-0136 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0136
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'su', fiil 'yapışmak', sıfat 'memnun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: yuvarlanırken başkasının yiyeceği yonca yapraklarını ezdi | özür diledi ve hızla koşup yeni yonca getirdi
@tohum: doru-0136
@degisim: memnun -> mutlu
Parkta Kırat taze yonca yaprakları yiyordu. Doru oyun oynarken yaprakların üstünde yuvarlandı. Yapraklar ezildi ve Kırat onları yiyemedi. Birkaç yaprak Doru'nun sırtına yapışmıştı. Kırat sessizce o yapraklara baktı. Doru başını çevirdi, yaprakları gördü ve çok üzüldü. "Özür dilerim, Kırat, sana yeni yonca getireceğim," dedi Doru. Doru parkın öbür ucundaki suyun kenarına hızla koştu. Orada ağzını taze yonca ile doldurdu. Sonra geri gelip yaprakları Kırat'ın önüne bıraktı. Kırat yaprakları yedi ve çok mutlu oldu. "Teşekkürler, Doru, bu yonca çok tatlı!" dedi Kırat.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta Kırat taze yonca"
   - Cümle 1: «Parkta Kırat taze yonca yaprakları yiyordu.»
   - Açıklama: Park yerinin tarifi sürünün çimen yediği geniş bir çayırdır, hikaye ise çayır yerine düpedüz park diyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0136` birebir aynı, `@degisim: memnun -> mutlu` (tutuyorsan), ardından `@onarim: 9d123b7b665bb24dc79cc02d4a1f8cd7c606d5cb`, sonra gövde.

### Hikâye 3: tohum doru-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0137
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'fener', fiil 'tasarlamak', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: sondaki kalın kütük çok büyük göründü | cesurca yeniden koşup kütüğün üstünden atladı
@tohum: doru-0137
@degisim: fener -> dal
Vadide Doru yeni bir atlama oyunu tasarladı. Kuru dalları çimene dalgalı bir çizgi gibi dizdi. Ama çizginin sonundaki kalın kütük çok büyük görünüyordu. Doru ince dalların üstünden tek tek geçti. Kütüğün önünde birden durdu ve burnu ona değdi. Doru biraz güldü ve kütüğe yeniden baktı. Sonra cesur davrandı ve geri gidip yeniden koştu. Bu kez kütüğün üstünden rahatça atladı. Dört ayağı da yumuşak çimene indi. Doru çizginin başına döndü ve oyunu bir kez daha oynadı. Hiçbir yerde durmadan hepsinin üstünden geçti. Doru çok sevindi, çünkü kendi oyununu sonuna kadar oynamıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni bir atlama oyunu tasarladı"
   - Cümle 1: «Vadide Doru yeni bir atlama oyunu tasarladı.»
   - Açıklama: 'Tasarladı' 3 yaşındaki çocuğun bilmediği bir kelime.
   - Açıklama: 'Tasarlamak' 3 yaşındaki bir çocuğun bildiği bir kelime değil.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Vadide Doru yeni bir atlama oyunu tasarladı"
   - Cümle 1: «Vadide Doru yeni bir atlama oyunu tasarladı.»
   - Açıklama: Başlıktaki yer dağ, ama hikaye vadide başlıyor ve bitiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kütüğün üstünden rahatça atladı"
   - Cümle 8: «Bu kez kütüğün üstünden rahatça atladı.»
   - Açıklama: Çok büyük görünen kalın kütüğün üstünden atlamak taklit edilince tehlikeli olabilir.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bu kez kütüğün üstünden rahatça atladı"
   - Cümle 8: «Bu kez kütüğün üstünden rahatça atladı.»
   - Açıklama: Kartın güvenli kullanım satırı hızı düz yerde koşarken gösterir; koşup kalın kütüğün üstünden atlamak taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0137` birebir aynı, `@degisim: fener -> dal` (tutuyorsan), ardından `@onarim: 9c09d4756732627632a25dd06a7a85541f316fb4`, sonra gövde.

### Hikâye 4: tohum doru-0138 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: annesinin önünde yalnız kuru otlar vardı | bulduğu naneleri annesiyle paylaştı
@tohum: doru-0138
Doru annesiyle birlikte dağda yürüyordu. Bir kayanın yanında taze nane buldu ve yemeye başladı. Annesi de acıkmıştı, ama onun önünde yalnız kuru otlar vardı. Doru her yediğinde naneler biraz daha küçülüyordu. Doru hemen durdu ve annesine baktı. "Anneciğim, gel, bu naneleri birlikte yiyelim," dedi Doru. Doru annesine yardım etti ve ona en yumuşak naneleri bıraktı. Annesi bir nane tattı ve gülümsedi. "Çok güzel kokuyorlar, teşekkürler, Doru," dedi annesi. İkisi naneleri yan yana bitirdi. Doru bundan sonra iyi bir şey bulunca annesiyle paylaştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "onun önünde yalnız kuru otlar vardı"
   - Cümle 3: «Annesi de acıkmıştı, ama onun önünde yalnız kuru otlar vardı.»
   - Açıklama: Anne de nanenin yanına gelebilecekken sorunun sebebi zorlama ve inandırıcı değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "naneler biraz daha küçülüyordu"
   - Cümle 4: «Doru her yediğinde naneler biraz daha küçülüyordu.»
   - Açıklama: Naneler küçülmez, azalır; fiil yanlış anlamda kullanılmış.
   - Açıklama: Nane yaprakları küçülmez, azalan nane yığınıdır; fiil öznesine uymuyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra iyi bir şey bulunca annesiyle paylaştı"
   - Cümle 11: «Doru bundan sonra iyi bir şey bulunca annesiyle paylaştı.»
   - Açıklama: 'Bundan sonra' ile tek seferlik 'paylaştı' uyuşmuyor; 'paylaşırdı' gibi alışkanlık bildiren biçim gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0138` birebir aynı, ardından `@onarim: 0effac9a811f87f3960af4af0be47985ac3c50a4`, sonra gövde.

### Hikâye 5: tohum doru-0140 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0140
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gökkuşağı', fiil 'taşınmak', sıfat 'garip'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: renkli tüy rüzgarla uzun otların arasına taşındı | cesurca otlara gidip tüyü buldu
@tohum: doru-0140
@degisim: gökkuşağı -> tüy
Bir sabah Kırat dağda garip, renkli bir tüy buldu. Tüyü Doru'ya göstermek için bir taşın üstüne koydu. Ama birden rüzgar esti ve tüy uzun otların arasına taşındı. Otlar rüzgarda hışır hışır ses çıkarıyordu. Doru önce durdu ve bu sesi dinledi. Sonra cesur davrandı ve otlara yavaşça yaklaştı. Burnuyla otları iki yana itti ve yere baktı. Renkli tüy bir otun dibinde duruyordu. Doru tüyü dişleriyle tuttu ve Kırat'a getirdi. "İşte tüyün, Kırat," dedi Doru. "Teşekkürler, Doru, onu çok seviyorum," dedi Kırat. Doru çok sevindi, çünkü Kırat'ın tüyünü geri getirmişti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tüy uzun otların arasına taşındı"
   - Cümle 3: «Ama birden rüzgar esti ve tüy uzun otların arasına taşındı.»
   - Açıklama: Az önce bulunan bir tüyün hemen yakındaki otlara uçması önemsiz bir olay ve kolayca bulunup bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0140` birebir aynı, `@degisim: gökkuşağı -> tüy` (tutuyorsan), ardından `@onarim: d73057c67c0ea82e2a3c46e1c145f1f583c78010`, sonra gövde.

### Hikâye 6: tohum doru-0141 (deneme 2 -> 3)

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
Kuşlar ötüyordu ve çayırda hafif bir rüzgar esiyordu. Doru ile Alaca bir oyun oynuyordu. Oyunda Alaca büyük bir attı ve Doru'yu meyveli ağaca götürecekti. Ama uzun otlar yüzünden küçük Alaca ağacı göremedi. "Hangi yöne gideceğim?" diye sordu Alaca. Doru başını kaldırdı ve ağacı gördü. Doru hemen Alaca'ya yardım etti. "Sağa dön, Alaca, sonra hep düz ilerle," dedi Doru. Alaca sağa döndü ve otların arasında ilerledi. Sonunda elmalarla dolu dallar göründü. "Buldum, seni ben getirdim!" dedi Alaca. Alaca sevinçle ağacın çevresinde çember gibi döndü. Sonra ikisi gölgede elmaları mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "çayırda hafif bir rüzgar esiyordu"
   - Cümle 1: «Kuşlar ötüyordu ve çayırda hafif bir rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor; park hiç anılmıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "küçük Alaca ağacı göremedi"
   - Cümle 4: «Ama uzun otlar yüzünden küçük Alaca ağacı göremedi.»
   - Açıklama: Alaca bir önceki cümlede büyük bir at olarak kuruluyor ama hemen ardından küçük olduğu için ağacı göremiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0141` birebir aynı, ardından `@onarim: eff901179c423251c183b65cc9acd1efeba8dea9`, sonra gövde.

### Hikâye 7: tohum doru-0144 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0144
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kürek', fiil 'açmak', sıfat 'soğuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: büyük bir kütük dar yolu kapattı | cesaretle küçük arkadaşından yardım istedi ve kütüğü birlikte ittiler
@tohum: doru-0144
@degisim: kürek -> kütük
Ormanda soğuk bir rüzgar esiyordu. Doru ile Alaca ormandaki güneşli açıklığa gitmek istiyordu. Ama dar yola büyük bir kütük düşmüştü ve yol kapanmıştı. Doru kütüğü tek başına itti ama kütük kıpırdamadı. Alaca çok küçüktü ve Doru ondan yardım istemeye utandı. Sonra cesur davrandı ve Alaca'ya döndü. "Alaca, bana yardım eder misin?" diye sordu Doru. "Tabii, Doru, birlikte itelim," dedi Alaca. İkisi yan yana durdu ve kütüğü itti. Kütük yavaşça yuvarlandı ve yolun kenarına düştü. İkisi hemen güneşli açıklığa koştu. Doru çok sevindi, çünkü Alaca'dan yardım isteyip yolu açmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormandaki güneşli açıklığa"
   - Cümle 2: «Doru ile Alaca ormandaki güneşli açıklığa gitmek istiyordu.»
   - Açıklama: 'Açıklık' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0144` birebir aynı, `@degisim: kürek -> kütük` (tutuyorsan), ardından `@onarim: 5e92001818a1e91ae01729ce265328b38de167b1`, sonra gövde.

### Hikâye 8: tohum doru-0145 (deneme 2 -> 3)

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
@degisim: çekingen -> ince
Çayırda büyük bir meşe vardı ve dallarında kuşlar şakıyordu. Doru ağacın altında Kırat'ı gördü. Kırat'ın uzun kuyruğu ince bir dala takılmıştı. Dal tam arkasındaydı ve Kırat onu göremiyordu. Kırat her çekince dal kuyruğunu daha çok sarıyordu. "Doru, kuyruğum takıldı, çıkaramıyorum!" dedi Kırat. Doru hemen ona yardım etti ve yanına gitti. Dalı dişleriyle tuttu ve yavaşça eğdi. Sonra kuyruğu daldan dikkatle ayırdı. Kuyruk kurtuldu ve aşağı indi. Kırat sevinçle kuyruğunu salladı. "Teşekkürler, Doru, kuyruğum artık serbest!" dedi Kırat.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dallarında kuşlar şakıyordu"
   - Cümle 1: «Çayırda büyük bir meşe vardı ve dallarında kuşlar şakıyordu.»
   - Açıklama: 'şakımak' 3 yaşındaki bir çocuğun bilmeyeceği edebi bir kelime.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda büyük bir meşe vardı"
   - Cümle 1: «Çayırda büyük bir meşe vardı ve dallarında kuşlar şakıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda başlıyor ve geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda başlıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kırat her çekince dal"
   - Cümle 5: «Kırat her çekince dal kuyruğunu daha çok sarıyordu.»
   - Açıklama: 'her çekince' dilbilgisel değil; 'her çektiğinde' olmalı.
   - Açıklama: 'Her çekince' dilbilgisel değil ve nesnesi eksik; 'Kırat kuyruğunu her çektiğinde' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0145` birebir aynı, `@degisim: çekingen -> ince` (tutuyorsan), ardından `@onarim: 177fa56a13d0855e191c942a3dacef427b8efa49`, sonra gövde.

### Hikâye 9: tohum doru-0146 (deneme 2 -> 3)

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
@plan: ağaçtaki son elma çimenlerde yuvarlandı ve uzaklaştı | hızla koşup elmayı durdurdu ve arkadaşıyla paylaştı
@tohum: doru-0146
@degisim: yoğur- -> yuvarlan-
Doru ile Karatay çayırda bir elma ağacının altında duruyordu. Karatay yüksek bir dala uzandı ve son elmayı düşürdü. Ama elma çimenlerin üstünde yuvarlandı ve uzaklaştı. "Son elma gidiyor!" dedi Karatay. Doru hemen düz ve açık çayırda hızla koştu. Elmanın önüne geçti ve onu ayağıyla durdurdu. Sonra elmayı ağzıyla aldı ve ağacın altına getirdi. "Gel, Karatay, bu elmayı paylaşalım," dedi Doru. Doru elmayı ısırdı, ikiye böldü ve yarısını Karatay'a verdi. Karatay'ın boncuk gibi gözleri parladı. Arkadaşlar elmalarını yan yana yedi. İkisi de çok mutluydu, çünkü son elmayı paylaşmışlardı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Karatay çayırda"
   - Cümle 1: «Doru ile Karatay çayırda bir elma ağacının altında duruyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "boncuk gibi gözleri parladı"
   - Cümle 10: «Karatay'ın boncuk gibi gözleri parladı.»
   - Açıklama: 'Gözleri parladı' sevinç için mecazdır ve benzetmeyle birlikte küçük çocuğa uygun değil.
   - Açıklama: Benzetme ve mecaz, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay'ın boncuk gibi gözleri parladı"
   - Cümle 10: «Karatay'ın boncuk gibi gözleri parladı.»
   - Açıklama: 'Boncuk gibi gözleri parladı' benzetme ve mecaz içeriyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Arkadaşlar elmalarını yan yana yedi"
   - Cümle 11: «Arkadaşlar elmalarını yan yana yedi.»
   - Açıklama: Tek elma ikiye bölünmüşken 'elmalarını' çoğul kullanımı yanlış anlam veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0146` birebir aynı, `@degisim: yoğur- -> yuvarlan-` (tutuyorsan), ardından `@onarim: 5ce6402ad4a054208a945e67accd8ba2f4a194b8`, sonra gövde.

### Hikâye 10: tohum doru-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0147
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fidan', fiil 'atlamak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: ormanda tık tık diye bir ses geliyordu | sesi yapan kuru dalı bulup yere bıraktı
@tohum: doru-0147
Doru annesiyle ormanda yürüyordu. Birden yakından tık tık diye bir ses geldi. Doru sesi çok merak etti, ama bir şey göremedi. "Anneciğim, bu ses ne?" diye sordu Doru. "Bilmiyorum, Doru, gel birlikte bakalım," dedi annesi. Yolda küçük bir kütük vardı ve Doru kütüğün üstünden atladı. Fidanın hemen üstünde hareketli, kuru bir dal sallanıyordu. Rüzgar esince dal fidana vuruyordu ve ses buradan geliyordu. Fidanın ince gövdesi yana eğilmişti. Doru fidana yardım etti. Kuru dalı dişleriyle tuttu ve yere bıraktı. Ses kesildi ve fidan yeniden düz durdu. Doru çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru kütüğün üstünden atladı"
   - Cümle 6: «Yolda küçük bir kütük vardı ve Doru kütüğün üstünden atladı.»
   - Açıklama: Kütük sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yolda küçük bir kütük vardı"
   - Cümle 6: «Yolda küçük bir kütük vardı ve Doru kütüğün üstünden atladı.»
   - Açıklama: Kütük ve üstünden atlama olayda hiçbir işe yaramıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hareketli, kuru bir dal sallanıyordu"
   - Cümle 7: «Fidanın hemen üstünde hareketli, kuru bir dal sallanıyordu.»
   - Açıklama: 'Hareketli' dal için yanlış anlamda kullanılmış ve 'sallanıyordu' ile gereksiz tekrar oluşturuyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "hareketli, kuru bir dal sallanıyordu"
   - Cümle 7: «Fidanın hemen üstünde hareketli, kuru bir dal sallanıyordu.»
   - Açıklama: 'Hareketli' ile 'sallanıyordu' aynı şeyi söylüyor; gereksiz tekrar.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Fidanın ince gövdesi yana eğilmişti"
   - Cümle 9: «Fidanın ince gövdesi yana eğilmişti.»
   - Açıklama: Sesin kaynağını bulma sorununun yanına eğilen fidanı düzeltme diye ikinci bir sorun ekleniyor.
   - Açıklama: Ses sorununun yanına eğilen fidan diye ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0147` birebir aynı, ardından `@onarim: d4059da0cddc70f9aa57500181184d8de3c2ac5e`, sonra gövde.

### Hikâye 11: tohum doru-0148 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0148
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'karnabahar', fiil 'savrulmak', sıfat 'tüylü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: en küçük at uçan tohumlara yetişemedi çünkü boyu kısaydı | çiçeği salladı ve tohumlar alçaktan uçtu
@tohum: doru-0148
@degisim: karnabahar -> çiçek
Vadide Doru ile Alaca tüylü çiçeklerin yanında oynuyordu. Rüzgarda savrulan tohumları burunlarıyla yakalamaya çalışıyorlardı. Ama Alaca çok küçüktü ve uçan tohumlara boyu yetmiyordu. Doru üç tohum tuttu, Alaca ise hiç tutamadı. Alaca üzüldü ve oyunu bırakmak istedi. Doru ona yardım etmek için en büyük çiçeğin yanına gitti. Başını eğdi ve çiçeği yavaşça salladı. Tohumlar bu kez alçaktan, tam Alaca'nın önünden uçtu. Alaca zıpladı ve bir tohumu burnuyla yakaladı. Sonra bir tane daha tuttu ve sevinçle güldü. Doru bundan sonra oyunlarda tohumları Alaca için hep aşağıdan uçurdu.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Vadide Doru ile Alaca"
   - Cümle 1: «Vadide Doru ile Alaca tüylü çiçeklerin yanında oynuyordu.»
   - Açıklama: Başlıktaki yer dağ iken hikaye vadide başlıyor ve geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0148` birebir aynı, `@degisim: karnabahar -> çiçek` (tutuyorsan), ardından `@onarim: 52fc83ac06d801dc3b1935615bf9fb400e3735be`, sonra gövde.

### Hikâye 12: tohum doru-0150 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0150
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'ağaç', fiil 'dalgalanmak', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: ufak bir ağacın dallarına kuru otlar dolanmıştı | otları dişleriyle tek tek çekip çıkardı
@tohum: doru-0150
Doru ormanda çimen yiyordu. Rüzgar esiyordu ve ağaçların yaprakları dalgalanıyordu. Ama ufak bir ağacın dallarına kuru ve uzun otlar dolanmıştı. Bu yüzden onun yaprakları hiç kıpırdamıyordu. Doru bunu gördü ve ağaca yardım etmek istedi. Otları dişleriyle tuttu ve yavaşça çekti. Önce bir dal, sonra öbür dal kurtuldu. Doru son otu da çekip yere attı. Ağacın dalları hafifçe doğruldu. Şimdi onun yaprakları da rüzgarda sallanıyordu. Doru ağaca baktı ve sevinçle güldü. Sonra ağacın yanındaki taze çimenleri keyifle yedi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kuru ve uzun otlar dolanmıştı"
   - Cümle 3: «Ama ufak bir ağacın dallarına kuru ve uzun otlar dolanmıştı.»
   - Açıklama: Kuru otların ağaç dallarına dolanması ve yaprakların kıpırdamaması hem akla az yatkın hem de çocuğun önemseyeceği bir sorun değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu yüzden onun yaprakları hiç kıpırdamıyordu"
   - Cümle 4: «Bu yüzden onun yaprakları hiç kıpırdamıyordu.»
   - Açıklama: Yaprakların rüzgarda kıpırdamaması hem akla yatkın değil hem de çocuğun önemseyeceği bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0150` birebir aynı, ardından `@onarim: 49456d08bbc1c4b3640f10d06c1140b0f557b945`, sonra gövde.
