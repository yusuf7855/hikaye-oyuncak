# Editör görevi (onarım): Doru, onarım partisi 6

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar6.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar6.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0012 (deneme 2 -> 3)

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
@plan: küçük olan sırası gelince yaprağa uzanamadı | dalı dişleriyle eğdi ve ona sırasını verdi
@tohum: doru-0012
@degisim: taramak -> uzanmak
Doru ile Alaca parktaki geniş çayırda sırayla yaprak koparıyordu. Ağacın esnek bir dalında yeşil yapraklar vardı. Ama Alaca çok küçüktü ve sırası gelince dala uzanamadı. "Yapraklar çok yüksekte, Doru," dedi Alaca. Alaca çok üzüldü. Doru ona hemen yardım etmek istedi. Dala baktı ve biraz düşündü. Sonra dişleriyle dalın ucunu tuttu ve yavaşça aşağı çekti. Dal kolayca eğildi ve yapraklar Alaca'nın önüne geldi. "Sıra sende, Alaca," dedi Doru. Alaca bir yaprak kopardı ve keyifle yedi. "Bu, en tatlı yiyecek!" dedi Alaca. Doru çok sevindi, çünkü Alaca da kendi sırasında yaprak yemişti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ona sırasını verdi"
   - Cümle 0 (plan satırı): «küçük olan sırası gelince yaprağa uzanamadı | dalı dişleriyle eğdi ve ona sırasını verdi»
   - Açıklama: Plan satırında 'ona' zamirinin kimi gösterdiği belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ağacın esnek bir dalında"
   - Cümle 2: «Ağacın esnek bir dalında yeşil yapraklar vardı.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0012` birebir aynı, `@degisim: taramak -> uzanmak` (tutuyorsan), ardından `@onarim: 5978ba63488f9ffde542e335067b33f692962fc7`, sonra gövde.

### Hikâye 2: tohum doru-0014 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0014
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'topaç', fiil 'yetiştirmek', sıfat 'masmavi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: vadiden gelen garip bir ses arkadaşını korkuttu | hızla koşup sesi yapan dönen yapraklara yetişti
@tohum: doru-0014
@degisim: yetiştirmek -> yetişmek
Dağdaki vadide gökyüzü masmaviydi. Doru ile Karatay çimenlerin üstünde oynuyordu. Birden vadinin öbür ucundan hışır hışır bir ses geldi. Karatay bu sesten biraz korktu ve oyunu bıraktı. "Bu ses ne, Doru?" diye sordu Karatay. "Bilmiyorum, ama hemen gidip bakarım," dedi Doru. Ses yavaş yavaş uzaklaşıyordu. Vadi geniş ve düzdü. Doru sese doğru hızla koştu ve çabucak yetişti. Orada kuru yapraklar rüzgarla topaç gibi dönüyordu. Ses bu yapraklardan geliyordu. "Gel, Karatay, bunlar yalnız yaprak!" dedi Doru. Karatay geldi, dönen yapraklara baktı ve güldü. Doru çok sevindi, çünkü arkadaşı artık korkmuyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hızla koştu ve çabucak yetişti"
   - Cümle 9: «Doru sese doğru hızla koştu ve çabucak yetişti.»
   - Açıklama: Sese yetişilmez; fiil nesnesiz ve anlamca uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0014` birebir aynı, `@degisim: yetiştirmek -> yetişmek` (tutuyorsan), ardından `@onarim: f2d7275ee81701d496b0b932b0383f23cafa9967`, sonra gövde.

### Hikâye 3: tohum doru-0015 (deneme 2 -> 3)

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
@plan: çok susamıştı ve çalıların arkasından garip bir ses geldi | cesaretle çalılardan geçti ve damlayan suyu buldu
@tohum: doru-0015
@degisim: domates -> damla
Doru sürünün yanındaki ormanda dolaşıyordu. Hava sıcaktı ve Doru çok susamıştı. Birden sık çalıların arkasından tık tık diye bir ses geldi. Doru bu sesi çok merak etti. Çalıların arkası karanlıktı ve hiçbir şey görünmüyordu. Doru cesaretle çalıların arasından yavaşça geçti. Orada büyük bir kaya vardı. Kayanın üstünden damla damla su düşüyordu. Her damla alttaki taşa değince tık diye ses çıkıyordu. Taşın dibinde küçük bir çukurda su toplanmıştı. Doru bu serin sudan bol bol içti. Sonra sürüsüne katıldı ve yumuşacık çimenlerde mutlu mutlu otladı.
```

**Hakem bulguları (5):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "çok susamıştı ve çalıların arkasından garip bir ses geldi"
   - Cümle 0 (plan satırı): «çok susamıştı ve çalıların arkasından garip bir ses geldi | cesaretle çalılardan geçti ve damlayan suyu buldu»
   - Açıklama: Susuzluk ve garip ses iki ayrı sorun olarak kuruluyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "çalıların arkasından tık tık diye bir ses geldi"
   - Cümle 3: «Birden sık çalıların arkasından tık tık diye bir ses geldi.»
   - Açıklama: Susuzluk sorununun yanına ayrı bir merak sorunu olarak garip ses ekleniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru bu sesi çok merak etti"
   - Cümle 4: «Doru bu sesi çok merak etti.»
   - Açıklama: Doru su aramıyor, sesi merak ettiği için gidiyor ve suyu tesadüfen buluyor; çözüm susuzluğa doğrudan yönelmiyor.
4. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalıların arkası karanlıktı ve hiçbir şey görünmüyordu"
   - Cümle 5: «Çalıların arkası karanlıktı ve hiçbir şey görünmüyordu.»
   - Açıklama: Garip sesle birlikte karanlık ve görünmeyen bir yer korkutucu bir öğe olarak kuruluyor.
   - Açıklama: Karanlık çalılardan gelen garip ses küçük çocuk için korkutucu bir öğedir.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle çalıların arasından yavaşça geçti"
   - Cümle 6: «Doru cesaretle çalıların arasından yavaşça geçti.»
   - Açıklama: Garip bir sesin geldiği karanlık yere tek başına girmek taklit edilince tehlikeli bir davranıştır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0015` birebir aynı, `@degisim: domates -> damla` (tutuyorsan), ardından `@onarim: 60ebfbda5346f7129359bb7ae519954167e9d143`, sonra gövde.

### Hikâye 4: tohum doru-0016 (deneme 2 -> 3)

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
@plan: yavaş yürüyen arkadaşıyla sürüden geride kaldı | toprakta sürünün izlerini bulup yanından yürüdü
@tohum: doru-0016
@degisim: okumak -> bulmak
Ormanda sürü taze bezelye yemeye gidiyordu. Doru en arkada Kırat'ın yanında yürüyordu. Kırat çok yavaş yürüdü ve sürü uzaklaştı. Ağaçlar sıktı ve sürünün nereye gittiği görünmüyordu. "Sürü hangi yoldan gitti, Doru?" diye sordu Kırat. Doru Kırat'a yardım etmek istedi. Başını eğdi ve toprakta taze ayak izleri buldu. "Bak, Kırat, izler bu yoldan gidiyor," dedi Doru. İkisi bu yoldan birlikte yürüdü. Az sonra ağaçların arasında geniş bir çayır gördüler. Sürü orada yeşil bezelyeleri yiyordu. Kırat sürünün yanına geldi ve mutlu mutlu yemeye başladı. Doru bundan sonra sürüyü kaybedince toprakta izleri aradı.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "izlerini bulup yanından yürüdü"
   - Cümle 0 (plan satırı): «yavaş yürüyen arkadaşıyla sürüden geride kaldı | toprakta sürünün izlerini bulup yanından yürüdü»
   - Açıklama: 'Yanından yürüdü' izleri takip etmeyi anlatmıyor; 'izlerden yürüdü' ya da 'izleri takip etti' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sürünün izlerini bulup yanından yürüdü"
   - Cümle 0 (plan satırı): «yavaş yürüyen arkadaşıyla sürüden geride kaldı | toprakta sürünün izlerini bulup yanından yürüdü»
   - Açıklama: 'Yanından yürüdü' yanlış anlamda; kimin yanından yürüdüğü belli değil, 'izlerin peşinden yürüdü' olmalı.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sürü taze bezelye yemeye"
   - Cümle 1: «Ormanda sürü taze bezelye yemeye gidiyordu.»
   - Açıklama: Kartın yerler ve dünya alanında bezelye gibi ekili bir ürün yok; doğa dünyasına yabancı bir öğe.
4. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Ormanda sürü taze bezelye"
   - Cümle 1: «Ormanda sürü taze bezelye yemeye gidiyordu.»
   - Açıklama: Özgür at sürüsünün doğa dünyasında ekili bir bitki olan bezelye yemesi dizinin dünyasına uymayan yanlış bilgidir.
5. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Kırat çok yavaş yürüdü"
   - Cümle 3: «Kırat çok yavaş yürüdü ve sürü uzaklaştı.»
   - Açıklama: Kartın ilişki alanında Kırat en çok bilen ve danışılan bilge attır; burada yolu bilemeyip Doru'ya soran geride kalan biri olarak gösteriliyor.
6. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Kırat çok yavaş yürüdü ve sürü uzaklaştı"
   - Cümle 3: «Kırat çok yavaş yürüdü ve sürü uzaklaştı.»
   - Açıklama: Arka plandaki çoğul canlı sürü olaya katılıyor ve sorunu yaratıyor.
7. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "ve sürü uzaklaştı"
   - Cümle 3: «Kırat çok yavaş yürüdü ve sürü uzaklaştı.»
   - Açıklama: Arka plandaki çoğul canlı sürü uzaklaşarak sorunu yaratıyor ve olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0016` birebir aynı, `@degisim: okumak -> bulmak` (tutuyorsan), ardından `@onarim: 3022a2876e111984b2a9aca919918820bf574510`, sonra gövde.

### Hikâye 5: tohum doru-0017 (deneme 2 -> 3)

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
Bir sabah Doru ile Alaca dağda çimenlerin üstünde yuvarlanıyordu. Alaca kalktı ve derenin şeffaf suyuna baktı. Alnına uzun bir ot takılmıştı ve ot gözünün önüne sarkıyordu. Alaca başını salladı ama ot düşmedi. "Doru, bir şey göremiyorum," dedi Alaca. Doru hemen ona yardım etmek istedi. Otu dişleriyle yavaşça tuttu ve çekti. Ot alnından çıktı ve yere düştü. Alaca yine suya baktı. "Şimdi her şeyi görüyorum!" dedi Alaca. İkisi birlikte gülüştü. Alaca bundan sonra alnına ot takılınca hemen Doru'ya söyledi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "derenin şeffaf suyuna"
   - Cümle 2: «Alaca kalktı ve derenin şeffaf suyuna baktı.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'berrak' ya da 'temiz' daha basit olur.
   - Açıklama: 'Şeffaf' 3 yaşındaki çocuğun bilmeyeceği bir kelime; 'berrak' ya da 'temiz' daha uygun.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru, bir şey göremiyorum"
   - Cümle 5: «"Doru, bir şey göremiyorum," dedi Alaca.»
   - Açıklama: Ot yalnız bir gözün önüne sarkıyor ve Alaca suya bakıp görebiliyor, ama hiçbir şey göremediğini söylüyor.
   - Açıklama: Alaca az önce suya bakıp alnındaki otu görmüşken hiçbir şey göremediğini söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0017` birebir aynı, ardından `@onarim: 1c7bb46dc0666760331342a04484894eb4199c85`, sonra gövde.

### Hikâye 6: tohum doru-0018 (deneme 2 -> 3)

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
@plan: vadiye giden yolu bulamadı çünkü ağaçlar birbirine benziyordu | yolu bilen küçük arkadaşına sordu
@tohum: doru-0018
Doru ormanda Alaca ile oynuyordu. Doru sürünün yanına dönmek istedi ama vadiye giden yolu bulamadı. Çünkü bütün ağaçlar birbirine benziyordu. Doru düz bir çimenlikte hızla koştu ve her yana baktı. Ama yolu yine göremedi. Alaca yakında bir şarkı mırıldanıyordu. "Alaca, vadinin yolunu biliyor musun?" diye sordu Doru. "Evet, siyah dalı olan ağacın yanından gidiyoruz," dedi Alaca. Alaca başını çevirdi ve büyük bir ağacı gösterdi. Ağacın bir dalı siyahtı. İkisi ağacın yanından yürüdü ve az sonra vadiyi gördü. Doru çok sevindi, çünkü Alaca'ya sormuştu ve yolu bulmuştu.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çünkü bütün ağaçlar birbirine benziyordu."
   - Cümle 3: «Çünkü bütün ağaçlar birbirine benziyordu.»
   - Açıklama: 'Çünkü' ile başlayan yan cümle ana cümleden ayrılıp tek başına cümle yapılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru düz bir çimenlikte hızla koştu"
   - Cümle 4: «Doru düz bir çimenlikte hızla koştu ve her yana baktı.»
   - Açıklama: Tohumdaki hız özelliği sorunu çözmüyor; yol Alaca'ya sorularak bulunuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama yolu yine göremedi"
   - Cümle 5: «Ama yolu yine göremedi.»
   - Açıklama: Tohum özelliği hız işe yaramıyor; sorun hızla değil Alaca'ya sorarak çözülüyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Alaca yakında bir şarkı mırıldanıyordu"
   - Cümle 6: «Alaca yakında bir şarkı mırıldanıyordu.»
   - Açıklama: Şarkı mırıldanma işlevsiz bir ayrıntı; üstelik Alaca zaten Doru ile oynuyordu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0018` birebir aynı, ardından `@onarim: e492bf91a005bd65432370e2e95b63407ae1aa8d`, sonra gövde.

### Hikâye 7: tohum doru-0019 (deneme 2 -> 3)

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
@plan: yarıştığı yaprak derede iki taşın arasına takıldı | burnuyla yaprağı itip taşlardan kurtardı
@tohum: doru-0019
@degisim: çöp -> yaprak
Rüzgar dağda hafif hafif esiyordu. Doru vadideki küçük derenin kenarında oynuyordu. Büyük ve güzel bir yaprağı suya koymuştu. Yaprak suyla birlikte akıyordu. Doru da düz çimenlerde onun yanında hızla koşuyordu. Bu yarış çok eğlenceliydi. Ama birden yaprak iki taşın arasına takıldı. Yaprak taşları aşamadı ve olduğu yerde kaldı. Dere orada çok sığdı. Doru kenarda durdu ve başını suya doğru eğdi. Burnuyla yaprağı yavaşça itti. Yaprak taşların arasından çıktı ve yeniden akmaya başladı. Doru çok sevindi, çünkü yarış oyunu yeniden başlamıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Büyük ve güzel bir yaprağı suya koymuştu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak yedinci cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0019` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: 58d355914775fc217eb853209f3ddb01b6f4cf4e`, sonra gövde.

### Hikâye 8: tohum doru-0020 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0020
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'toz', fiil 'eğlendirmek', sıfat 'lezzetli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: rüzgar çimenleri tozla kapladı ve annesi yiyemedi | onu derenin kenarındaki temiz çimenlere götürdü
@tohum: doru-0020
@degisim: eğlendirmek -> götürmek
Bir sabah Doru ile annesi parktaki geniş çayırda çimen yiyordu. Birden rüzgar esti ve çimenlerin üstünü kalın bir toz kapladı. Annesi çok açtı ama tozlu çimenleri yiyemiyordu. "Doru, bu çimenler yenmez," dedi annesi. Doru etrafına baktı ve biraz ileride küçük bir dere gördü. Derenin kenarındaki çimenler yeşil ve temizdi. Doru, annesine yardım etmek için onu oraya götürdü. Annesi temiz çimenleri yedi. "Bunlar çok lezzetli, Doru!" dedi annesi. Doru bundan sonra rüzgarlı günlerde temiz çimenleri derenin kenarında arardı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çimenlerin üstünü kalın bir toz kapladı"
   - Cümle 2: «Birden rüzgar esti ve çimenlerin üstünü kalın bir toz kapladı.»
   - Açıklama: Rüzgarın parktaki çimenleri kalın tozla kaplaması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0020` birebir aynı, `@degisim: eğlendirmek -> götürmek` (tutuyorsan), ardından `@onarim: dd658d610ea229191505c3cdf7712664d4fe5670`, sonra gövde.

### Hikâye 9: tohum doru-0023 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0023
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fıstık', fiil 'kavuşmak', sıfat 'gizli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: elmalar yüksekteydi ve küçük arkadaşı onlara uzanamıyordu | dalı dişleriyle salladı ve elmaları yere düşürdü
@tohum: doru-0023
@degisim: fıstık -> elma
Doru dağda Alaca için bir sürpriz hazırlıyordu. Alaca kırmızı elmaları çok severdi. Kayaların arkasında gizli bir elma ağacı vardı ama elmalar çok yüksekteydi. Küçük Alaca onlara uzanamıyordu. Doru ağacın alçak bir dalını dişleriyle tuttu ve salladı. Kırmızı elmalar çimenlerin üstüne düştü. Doru elmaları burnuyla ağacın altında bir araya itti. Sonra Alaca'yı çağırdı. "Gel, Alaca, sana bir sürprizim var," dedi Doru. Alaca kayaların arkasına geldi ve elmaları gördü. "Ne kadar çok elma!" dedi Alaca. Alaca sevdiği elmalara kavuştu ve mutlu mutlu yedi. Doru çok sevindi, çünkü küçük arkadaşına yardım edip onu güldürmüştü.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ağacın alçak bir dalını dişleriyle tuttu"
   - Cümle 5: «Doru ağacın alçak bir dalını dişleriyle tuttu ve salladı.»
   - Açıklama: Elmalar çok yüksekte denirken alçak bir dalı sallamanın yüksekteki elmaları düşürmesi tutarsız kalıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Alaca sevdiği elmalara kavuştu"
   - Cümle 12: «Alaca sevdiği elmalara kavuştu ve mutlu mutlu yedi.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sevdiği elmalara kavuştu"
   - Cümle 12: «Alaca sevdiği elmalara kavuştu ve mutlu mutlu yedi.»
   - Açıklama: 'Kavuşmak' soyut ve edebi bir kelime, 3 yaşındaki çocuğun bilmeyeceği bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0023` birebir aynı, `@degisim: fıstık -> elma` (tutuyorsan), ardından `@onarim: e0848c0b4069107ff038235e5057d66f66d3b632`, sonra gövde.

### Hikâye 10: tohum doru-0024 (deneme 1 -> 2)

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
@degisim: kova -> delik
Dağda yağmur yeni dinmişti. Doru ile Kırat ıslak tüylerini kurutmak için güneşli bir kayaya gidiyordu. Birden kayanın arkasından garip bir ıslık sesi geldi. Kırat durdu ve kulaklarını dikti. "Bu ses nereden geliyor, Doru?" diye sordu Kırat. Doru cesurca kayanın arkasına yürüdü ve baktı. Kayada küçük bir delik vardı. Rüzgar bu delikten geçiyor ve ıslık çalıyordu. "Gel, Kırat, bu ıslığı rüzgar çalıyor!" dedi Doru. Kırat da geldi ve deliğe baktı. İkisi pürüzsüz kayanın yanında güneşte durdu ve tüyleri kurudu. "Teşekkürler, Doru, artık o sesi biliyoruz!" dedi Kırat.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: ""Bu ses nereden geliyor, Doru?" diye sordu Kırat"
   - Cümle 5: «"Bu ses nereden geliyor, Doru?" diye sordu Kırat.»
   - Açıklama: Kartın ilişki alanına göre en çok Kırat bilir ve sürüdekiler ona danışır; burada Kırat Doru'ya danışıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İkisi pürüzsüz kayanın yanında"
   - Cümle 11: «İkisi pürüzsüz kayanın yanında güneşte durdu ve tüyleri kurudu.»
   - Açıklama: 'Pürüzsüz' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0024` birebir aynı, `@degisim: kova -> delik` (tutuyorsan), ardından `@onarim: 84c47313e1a782a946aaa3c9bb2ca7678bc79c37`, sonra gövde.

### Hikâye 11: tohum doru-0025 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: arkadaşının durduğu yerde hiç çimen yoktu | bulduğu taze otları onunla paylaştı
@tohum: doru-0025
@degisim: yıldız -> ot
Ormanda güneş ağaçların arasından ışıltılı çimenlere düşüyordu. Doru bir ağacın altında taze otlar buldu. Karatay'ın durduğu yerde ağaçlar çok sıktı ve hiç çimen yoktu. "Doru, karnım çok acıktı," dedi Karatay. Doru otlara ve arkadaşına baktı. "Gel, Karatay, bu otları paylaşalım," dedi Doru. Doru arkadaşına yardım etmek için otların yarısını ona bıraktı. İki at yan yana durdu ve birlikte yedi. Otlar ikisini de doyurdu. Karatay kuyruğunu neşeyle salladı. Karatay çok sevindi, çünkü Doru otlarını onunla paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağaçların arasından ışıltılı çimenlere düşüyordu"
   - Cümle 1: «Ormanda güneş ağaçların arasından ışıltılı çimenlere düşüyordu.»
   - Açıklama: 'Işıltılı' ve güneşin çimenlere düşmesi 3 yaşındaki çocuğa uygun olmayan mecazlı bir anlatım.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ışıltılı çimenlere düşüyordu"
   - Cümle 1: «Ormanda güneş ağaçların arasından ışıltılı çimenlere düşüyordu.»
   - Açıklama: Ormanda güneşli çimenler varken Karatay'ın çimensiz yerde kalıp aç olması akla yatkın bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0025` birebir aynı, `@degisim: yıldız -> ot` (tutuyorsan), ardından `@onarim: 8cf262b7c1d70ef750b97fe20b619e9f3fa352bf`, sonra gövde.

### Hikâye 12: tohum doru-0026 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: sıra ona gelince baktığı bulut dağın arkasına kaydı | düz çayırda hızla koşup bulutu yeniden gördü
@tohum: doru-0026
@degisim: giydirmek -> koşmak
Doru ile annesi dağda bulut oyunu oynuyordu. "Şu bulut yuvarlak bir top," dedi annesi ve sıra Doru'ya geldi. Ama Doru'nun baktığı bulut rüzgarla dağın arkasına kaydı. Doru meraklı gözlerle etrafına baktı. Sonra vadideki düz çayıra hızla koştu. Oradan bulut yeniden göründü. Bulutun uzun bir kuyruğu ve dört ayağı vardı. "Anne, bu bulut bir ata benziyor!" dedi Doru. Annesi de çayıra geldi ve buluta baktı. "Evet, uzun kuyruğu tıpkı seninki gibi!" dedi annesi. İkisi birlikte güldü. "Bu oyun çok güzel, anneciğim, sıra yine sende!" dedi Doru.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Doru'nun baktığı bulut rüzgarla dağın arkasına kaydı"
   - Cümle 3: «Ama Doru'nun baktığı bulut rüzgarla dağın arkasına kaydı.»
   - Açıklama: Oyunda başka bir buluta bakmak yeterken bir bulutun kayması çocuğun önemseyeceği bir sorun değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "vadideki düz çayıra hızla koştu"
   - Cümle 5: «Sonra vadideki düz çayıra hızla koştu.»
   - Açıklama: Dağın arkasına kayan bulutu görmek için aşağıdaki vadiye inmek sebebe yönelen akla yatkın bir çözüm değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0026` birebir aynı, `@degisim: giydirmek -> koşmak` (tutuyorsan), ardından `@onarim: 84eb6aaa222e538b60cb5d027526e86d628199e4`, sonra gövde.
