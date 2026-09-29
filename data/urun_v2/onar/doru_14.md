# Editör görevi (onarım): Doru, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0036 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0036
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'bambu', fiil 'seslenmek', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar en sevdiği dalı yokuştan aşağı yuvarladı | sürüye seslenip indi ve dalı çalıların arasında buldu
@tohum: doru-0036
@degisim: bambu -> dal
Rüzgar dağın üstünde esiyordu. Doru uzun bir dalı ağzıyla sallayarak oynuyordu. Bu dal onun en sevdiği oyuncağıydı. Birden rüzgar güçlendi ve dalı yokuştan aşağı yuvarladı. Doru dalı artık göremiyordu. Önce sürüye seslendi ve aşağı ineceğini söyledi. Sonra yokuştan yavaş yavaş aşağı yürüdü. Dal, yokuşun dibindeki sık çalıların arasına girmişti. Çalıların arasına girmek zordu, ama Doru cesaretle başını uzattı. Dalı dişleriyle tuttu ve dışarı çekti. Dal çok sağlamdı ve hiç kırılmamıştı. Doru onu ağzında yukarı taşıdı. Doru çok sevindi, çünkü en sevdiği oyuncağını yeniden bulmuştu.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "dalı yokuştan aşağı yuvarladı"
   - Cümle 4: «Birden rüzgar güçlendi ve dalı yokuştan aşağı yuvarladı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce sürüye seslendi ve aşağı ineceğini söyledi"
   - Cümle 6: «Önce sürüye seslendi ve aşağı ineceğini söyledi.»
   - Açıklama: Sürü hikayede hiç kurulmadan beliriyor ve sonra olayda bir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce sürüye seslendi"
   - Cümle 6: «Önce sürüye seslendi ve aşağı ineceğini söyledi.»
   - Açıklama: Sürü daha önce hiç kurulmadan sebepsizce beliriyor ve olayda işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0036` birebir aynı, `@degisim: bambu -> dal` (tutuyorsan), ardından `@onarim: 2da1471e297f8d6c73c0b6a05e5260110d3f5ec5`, sonra gövde.

### Hikâye 2: tohum doru-0037 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0037
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çam', fiil 'bozulmak', sıfat 'zarif'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: rüzgar çiçekleri uçurdu ve sürpriz bozuldu | hızla koşup yeni papatyalar getirdi
@tohum: doru-0037
@degisim: zarif -> beyaz
Doru, sürünün çimen yediği çayırda, büyük bir çam ağacının altındaydı. Alaca çiçekleri çok severdi ve Doru ağacın altına onun için çiçek getirmişti. Ama birden rüzgar esti, çiçekler uçtu ve sürpriz bozuldu. Alaca da uzaktan ağaca doğru geliyordu. Çayırın öbür ucunda papatyalar vardı. Doru düz çayırda hızla koştu. Ağzıyla birçok papatya kopardı ve ağaca geri döndü. Tam o sırada Alaca geldi ve beyaz çiçeklere baktı. "Bunlar benim için mi, Doru?" diye sordu Alaca. "Evet, Alaca, hepsi senin," dedi Doru. Alaca sevinçle zıpladı. Doru da çok sevindi, çünkü sürprizini tam zamanında yeniden hazırlamıştı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sürünün çimen yediği çayırda"
   - Cümle 1: «Doru, sürünün çimen yediği çayırda, büyük bir çam ağacının altındaydı.»
   - Açıklama: Başlıktaki yer park ama hikaye sürünün otladığı bir çayırda geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çiçekler uçtu ve sürpriz bozuldu"
   - Cümle 3: «Ama birden rüzgar esti, çiçekler uçtu ve sürpriz bozuldu.»
   - Açıklama: 'Sürpriz bozuldu' soyut bir anlatım, 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0037` birebir aynı, `@degisim: zarif -> beyaz` (tutuyorsan), ardından `@onarim: 43d921947b1b67b8e5b73aaacc0117faa0693c2b`, sonra gövde.

### Hikâye 3: tohum doru-0038 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0038
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'paket', fiil 'rahatlatmak', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi | kozalağı dişleriyle çekip fidanı kurtardı
@tohum: doru-0038
@degisim: paket -> kozalak
Bir sabah gökyüzü mavi ve açıktı. Doru, sürünün çimen yediği çayırda bir kozalağı burnuyla itip peşinden koşuyordu. Birden kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi. Doru fidana yardım edip onu rahatlatmak istedi. Kozalağı dişleriyle yavaşça tuttu ve dalların arasından çekti. Dallar kırılmadı ve fidan yeniden dik durdu. Doru çok sevindi. Doru kozalağı dikkatlice çayırın ortasına götürdü. Oyununa açık çimenlerde yine neşeyle devam etti. Doru bundan sonra kozalağı fidanlardan uzakta itti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sürünün çimen yediği çayırda"
   - Cümle 2: «Doru, sürünün çimen yediği çayırda bir kozalağı burnuyla itip peşinden koşuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye sürünün otladığı bir çayırda geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu rahatlatmak istedi"
   - Cümle 4: «Doru fidana yardım edip onu rahatlatmak istedi.»
   - Açıklama: Fidan rahatlatılmaz; fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0038` birebir aynı, `@degisim: paket -> kozalak` (tutuyorsan), ardından `@onarim: 9308b8342ec1ee54854dc2fcba6a698e75281bd7`, sonra gövde.

### Hikâye 4: tohum doru-0040 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0040
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'misket', fiil 'karışmak', sıfat 'kolay'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: sürü vadiye inmişti ve yerdeki izler karışmıştı | küçük arkadaşına yolu sordu ve sürüye yetişti
@tohum: doru-0040
@degisim: misket -> iz
Dağda serin bir rüzgar esiyordu. Doru ile Alaca büyük bir kayanın yanında oynuyordu. Oyun bitince Doru etrafına baktı ama sürü vadiye inmişti. Yerde çok iz vardı ve bütün izler birbirine karışmıştı. Doru hangi yoldan gideceğini bilemedi. "Alaca, sürü hangi yoldan indi, gördün mü?" diye sordu Doru. "Evet, sarı çiçekli yoldan indiler, bulmak çok kolay," dedi Alaca. İkisi o yoldan birlikte yavaşça indi. Aşağıda geniş ve düz bir vadi vardı. Sürü onun öbür ucunda çimen yiyordu. Doru sürüye doğru hızla koştu, Alaca da arkasından geldi. Az sonra ikisi de sürünün yanındaydı. "Teşekkürler, Alaca, yolu sen buldun!" dedi Doru.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sarı çiçekli yoldan indiler"
   - Cümle 7: «"Evet, sarı çiçekli yoldan indiler, bulmak çok kolay," dedi Alaca.»
   - Açıklama: Alaca Doru ile birlikte oynarken sürünün hangi yoldan indiğini görmüş olması, Doru'nun hiç görmemesiyle çelişiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Aşağıda geniş ve düz bir vadi vardı"
   - Cümle 9: «Aşağıda geniş ve düz bir vadi vardı.»
   - Açıklama: Hikaye dağda başlıyor ama vadiye inip orada bitiyor; tek sahne kuralı çiğneniyor.
   - Açıklama: Hikaye dağda başlıyor ama vadiye inip orada bitiyor; sahne değişiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru sürüye doğru hızla koştu"
   - Cümle 11: «Doru sürüye doğru hızla koştu, Alaca da arkasından geldi.»
   - Açıklama: Tohumdaki hız özelliği sorunu çözmüyor; yol Alaca'ya sorularak bulunuyor, hız işe yarar biçimde kullanılmamış.
4. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Teşekkürler, Alaca, yolu sen buldun"
   - Cümle 13: «"Teşekkürler, Alaca, yolu sen buldun!" dedi Doru.»
   - Açıklama: Kartın Alaca ilişkisine göre Alaca Doru'dan öğrenir ve ona yardım edilir; burada ilişki tersine çevriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0040` birebir aynı, `@degisim: misket -> iz` (tutuyorsan), ardından `@onarim: 8c4295c3ecde56edae2f202a5f8cab46d8d73437`, sonra gövde.

### Hikâye 5: tohum doru-0042 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0042
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çim', fiil 'küçültmek', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: çayırın kenarından garip bir ses geldi | sesi bulup kuru dalı uzağa çekti
@tohum: doru-0042
@degisim: küçültmek -> çekmek
Bir sabah Doru, sürüyle birlikte geniş çayırda çim yiyordu. Yağmurdan sonra her yer temiz ve yeşildi. Birden çayırın kenarından garip bir ses geldi. Doru bu sesin nereden geldiğini çok merak etti. Yavaşça çayırın kenarına yürüdü. Orada genç bir fidan vardı. Fidanın yanına kuru bir dal düşmüştü. Rüzgar esince dal fidana sürtünüyor ve ses çıkarıyordu. Doru fidana yardım etmek istedi. Kuru dalı dişleriyle tuttu ve uzağa çekti. Rüzgar yine esti ama ses gelmedi. Doru çok sevindi ve çayırda çim yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sürüyle birlikte geniş çayırda çim yiyordu"
   - Cümle 1: «Bir sabah Doru, sürüyle birlikte geniş çayırda çim yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir sürünün otladığı çayırda geçiyor ve park hiç kurulmuyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sürüyle birlikte geniş çayırda"
   - Cümle 1: «Bir sabah Doru, sürüyle birlikte geniş çayırda çim yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye sürünün otladığı bir çayırda geçiyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çayırın kenarından garip bir ses geldi"
   - Cümle 3: «Birden çayırın kenarından garip bir ses geldi.»
   - Açıklama: Ses kimseyi rahatsız etmiyor ve fidana bir zarar göstermiyor; sorun çocuk için önemsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0042` birebir aynı, `@degisim: küçültmek -> çekmek` (tutuyorsan), ardından `@onarim: a8423adef48c32e91545cc911b0121d67946d643`, sonra gövde.

### Hikâye 6: tohum doru-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0044
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gümüş', fiil 'kalmak', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: rüzgar küçük çiçeğe çok sert esiyordu | cesaretle çiçeğin önünde durup onu korudu
@tohum: doru-0044
@degisim: narin -> ince
Ormanda güçlü bir rüzgar esiyordu. Doru annesiyle ağaçların arasında yürüyordu. Birden yerde gümüş renkli, küçük bir çiçek gördü. Çiçeğin sapı çok inceydi ve rüzgarda sağa sola eğiliyordu. "Anne, bak, bu çiçek kırılacak!" dedi Doru. "Evet, rüzgar çok sert," dedi annesi. "Ben onun önünde dururum, anne," dedi Doru. Rüzgar Doru'ya sert sert esti, ama Doru cesaretle yerinden ayrılmadı. Rüzgar artık çiçeğe gelmedi. Az sonra rüzgar yavaşladı. Annesi yanına geldi ve başını Doru'nun başına sürttü. Doru çok sevindi, çünkü küçük çiçek dik kalmıştı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden yerde gümüş renkli, küçük bir çiçek gördü.»
   - Açıklama: İlk üç cümlede yalnız rüzgar ve çiçek var; çiçeğin tehlikede olduğu ancak 4. ve 5. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "bu çiçek kırılacak"
   - Cümle 5: «"Anne, bak, bu çiçek kırılacak!" dedi Doru.»
   - Açıklama: Çiçeğin kırılma tehlikesi ancak beşinci cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0044` birebir aynı, `@degisim: narin -> ince` (tutuyorsan), ardından `@onarim: f2c6d6019529e032050cd14b5864ff66dcdcd1a7`, sonra gövde.

### Hikâye 7: tohum doru-0045 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0045
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: paylaşmak
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'havuç', fiil 'takmak', sıfat 'buzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: elma buzlu dalların altındaydı ve dallar ses çıkarıyordu | cesaretle gidip elmayı aldı ve paylaştı
@tohum: doru-0045
@degisim: havuç -> elma
Bir sabah orman çok soğuktu ve Doru ile Karatay acıkmıştı. Buzlu bir çalının altında kırmızı bir elma gördüler. Ama çalının dalları rüzgarda çıt çıt ses çıkarıyordu ve Karatay yaklaşmadı. Doru cesaretle çalıya yürüdü ve dallara baktı. Sesi yalnız ince buzlar çıkarıyordu. Doru elmayı dişleriyle tuttu ve dışarı çekti. "Karatay, bunu birlikte yiyelim," dedi Doru. Karatay güldü ve Doru'ya "buz atı" adını taktı. Doru elmayı ısırdı ve ikiye böldü. İkisi elmayı yavaş yavaş yedi. Doru çok mutlu oldu, çünkü elmayı en yakın arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (5):**

1. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Karatay güldü ve Doru'ya"
   - Cümle 8: «Karatay güldü ve Doru'ya "buz atı" adını taktı.»
   - Açıklama: Karatay Doru'ya alaycı bir lakap takıyor ve bu örnek alınacak biçimde sunuluyor.
2. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Doru'ya "buz atı" adını taktı"
   - Cümle 8: «Karatay güldü ve Doru'ya "buz atı" adını taktı.»
   - Açıklama: Karatay'ın Doru'ya lakap takması örnek alınabilecek bir alay olarak okunabiliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""buz atı" adını taktı"
   - Cümle 8: «Karatay güldü ve Doru'ya "buz atı" adını taktı.»
   - Açıklama: 'Ad takmak' deyimsel ve lakap kavramı küçük çocuk için soyut.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karatay güldü ve Doru'ya "buz atı" adını taktı"
   - Cümle 8: «Karatay güldü ve Doru'ya "buz atı" adını taktı.»
   - Açıklama: Lakap takma olaya bağlanmayan işlevsiz bir ayrıntı.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru'ya "buz atı" adını taktı"
   - Cümle 8: «Karatay güldü ve Doru'ya "buz atı" adını taktı.»
   - Açıklama: Lakap takma olayı hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0045` birebir aynı, `@degisim: havuç -> elma` (tutuyorsan), ardından `@onarim: 02cd09c5d5b37eeb6b5208ded13641951ddd8983`, sonra gövde.

### Hikâye 8: tohum doru-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0046
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'üzüm', fiil 'sığmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: kar çimenlerin üstünü kapladı ve yiyecek yoktu | cesaretle karda yürüyüp kayanın altında kuru ot buldu
@tohum: doru-0046
@degisim: üzüm -> ot
Dağda lapa lapa kar yağıyordu. Kar bütün çimenlerin üstündeydi ve Doru yiyecek bulamıyordu. Uzakta büyük bir kaya gördü ve altında kar yoktu. Doru orada yiyecek bulmak istedi. Ama arada yumuşak kar vardı ve Doru daha önce hiç kar görmemişti. Doru cesaretle karın içine adım attı. Ayakları karda küçük izler bıraktı. Yavaş yavaş kayanın yanına vardı. Kayanın altındaki yer küçüktü, ama Doru başını eğdi ve oraya sığdı. Yerde kuru otlar duruyordu. Doru otları afiyetle yedi ve karnını doyurdu. Sonra orada huzurlu huzurlu dinlendi.
```

**Hakem bulguları (3):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Doru daha önce hiç kar görmemişti"
   - Cümle 5: «Ama arada yumuşak kar vardı ve Doru daha önce hiç kar görmemişti.»
   - Açıklama: Dağlarda yaşayan sürünün genç atı için kartta kar görmemiş olduğuna dair bilgi yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru başını eğdi ve oraya sığdı"
   - Cümle 9: «Kayanın altındaki yer küçüktü, ama Doru başını eğdi ve oraya sığdı.»
   - Açıklama: Tek başına kayanın altındaki dar boşluğa girmek taklit edilince tehlikeli.
   - Açıklama: Kayanın altındaki dar bir boşluğa girmek çocuğun taklit edebileceği tehlikeli bir davranış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "orada huzurlu huzurlu dinlendi"
   - Cümle 12: «Sonra orada huzurlu huzurlu dinlendi.»
   - Açıklama: 'Huzurlu huzurlu' soyut ve alışılmadık bir ikileme, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Huzurlu huzurlu' soyut ve alışılmadık bir ikileme.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0046` birebir aynı, `@degisim: üzüm -> ot` (tutuyorsan), ardından `@onarim: 7419dd72f72167d66499d47fd0e64720ec8bc66c`, sonra gövde.

### Hikâye 9: tohum doru-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0047
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'marul', fiil 'barışmak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar esti ve marul yokuştan yuvarlandı | yamuk ağacın arkasına cesaretle gidip marulu buldu
@tohum: doru-0047
@degisim: barışmak -> yuvarlanmak
Dağda sert bir rüzgar esiyordu. Doru kayaların arasında bulduğu küçük bir marulu yiyordu. Birden rüzgar yine esti ve marul yokuştan aşağı yuvarlandı. Doru marulu aramak için yokuştan yavaşça indi. Aşağıda yamuk bir ağaç vardı. Ağacın yanında rüzgar daha da sert esiyordu. Ama Doru cesaretle ağacın arkasına yürüdü. Marul orada, iki kökün arasında duruyordu. Doru marulu dişleriyle aldı ve çok sevindi. Doru bundan sonra rüzgarlı havada yemeğini bir kayanın dibinde yerdi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ama Doru cesaretle ağacın arkasına yürüdü"
   - Cümle 7: «Ama Doru cesaretle ağacın arkasına yürüdü.»
   - Açıklama: Sert rüzgarda yuvarlanan yiyeceğin peşinden yokuş aşağı ağacın yanına gitmek taklit edilince tehlikeli bir davranış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru cesaretle ağacın arkasına yürüdü"
   - Cümle 7: «Ama Doru cesaretle ağacın arkasına yürüdü.»
   - Açıklama: Doru marulun ağacın arkasında olduğunu gösteren bir ipucu olmadan oraya gidiyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0047` birebir aynı, `@degisim: barışmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 959dbc4d5bc5d2d425e900a005e170d5269adb6c`, sonra gövde.

### Hikâye 10: tohum doru-0048 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0048
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'köpük', fiil 'ıslatmak', sıfat 'komik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: susamıştı ama su içtiği çukur kuruydu | hızla koşup sesi yapan dereyi buldu
@tohum: doru-0048
Doru ormanda çok susamıştı. Ama su içtiği küçük çukur kuruydu. Birden uzaktan komik bir ses geldi. Doru bu sesin ne olduğunu çok merak etti. Ağaçların arasında geniş ve düz bir açıklık vardı. Doru açıklıkta hızla koştu ve sesin geldiği yere vardı. Orada küçük bir dere taşların üstünden akıyordu. Su taşlara çarpıyor ve beyaz köpükler yapıyordu. Komik ses buradan geliyordu. Doru başını eğdi ve dereden içti. Serin su Doru'nun ağzını ıslattı. Sonra Doru derenin kenarında mutlu mutlu otladı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzaktan komik bir ses"
   - Cümle 3: «Birden uzaktan komik bir ses geldi.»
   - Açıklama: Derenin akan su sesi komik değildir; kelime yanlış anlamda.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden uzaktan komik bir ses geldi"
   - Cümle 3: «Birden uzaktan komik bir ses geldi.»
   - Açıklama: Çözümü getiren ses sebepsizce beliriyor ve dereyi tesadüfen buldurtuyor.
   - Açıklama: Dereyi bulduran ses sebepsizce beliriyor ve çözümü Doru'nun çabası değil rastlantı getiriyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru bu sesin ne olduğunu çok merak etti"
   - Cümle 4: «Doru bu sesin ne olduğunu çok merak etti.»
   - Açıklama: Doru su aramaya değil meraka yöneliyor; çözüm susuzluk sorununa doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0048` birebir aynı, ardından `@onarim: cabef8f937fa9bfbb7dacad3b6289fdd4abc1fed`, sonra gövde.

### Hikâye 11: tohum doru-0049 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0049
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'iz', fiil 'solmak', sıfat 'enerjik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: küçük çiçekler susuz kalmış ve solmuştu | izin yanından yürüdü ve taşı itip suyun yolunu açtı
@tohum: doru-0049
Bir sabah Doru parkta çok enerjikti ve zıplaya zıplaya dolaşıyordu. Birden çimenlerin arasında küçük çiçekler gördü. Çiçekler susuz kalmış ve solmuştu. Biraz ileride ince ve ıslak bir iz vardı. Doru bu izin nereden geldiğini çok merak etti. İzin yanından yavaşça yürüdü. İzi küçük bir kaynaktan akan ince bir su yapıyordu. Su büyük bir taşın önünde birikmişti. Taş suyun çiçeklere giden yolunu kapatmıştı. Doru çiçeklere yardım etmek istedi. Başıyla taşı itti ve kenara yuvarladı. Su hemen kuru toprağa aktı ve çiçeklerin dibini ıslattı. Doru çok sevindi ve parkta koşup oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru parkta çok enerjikti"
   - Cümle 1: «Bir sabah Doru parkta çok enerjikti ve zıplaya zıplaya dolaşıyordu.»
   - Açıklama: 'Enerjik' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Doru parkta çok enerjikti"
   - Cümle 1: «Bir sabah Doru parkta çok enerjikti ve zıplaya zıplaya dolaşıyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği çayırdır; gövde dizide olmayan bir parkı anlatıyor.
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; metinde insan yapımı bir park olarak adlandırılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0049` birebir aynı, ardından `@onarim: 75e9c3946fbc2cdec5ca53b540d8c880c26529da`, sonra gövde.

### Hikâye 12: tohum doru-0050 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0050
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'şemsiye', fiil 'üflemek', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: en güzel otlar ağır bir dalın altında kalmıştı | arkadaşıyla dalı birlikte çekti ve yığını yaptı
@tohum: doru-0050
@degisim: şemsiye -> ot
Parktaki geniş çayırda güneş parlıyordu. Doru ile Karatay öğle yemeği için büyük bir ot yığını yapıyordu. Ama en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı. Karatay dalı tek başına çekemedi. Doru hemen arkadaşına yardım etmek istedi. Dalın bir ucunu dişleriyle tuttu. Karatay da öbür ucunu tuttu. İkisi dalı birlikte kenara çekti. Otların üstünde dalın yaprakları kalmıştı. Doru yapraklara burnuyla üfledi ve yapraklar otların üstünden uçtu. Sonra ikisi temiz otları kopardı ve yığına taşıdı. Yığın kocaman oldu ve nefis kokuyordu. Doru ile Karatay ot yığınının yanında mutlu mutlu yemek yedi.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Otların üstünde dalın yaprakları kalmıştı"
   - Cümle 9: «Otların üstünde dalın yaprakları kalmıştı.»
   - Açıklama: Dalı çektikten sonra yaprakları üfleme ve ot toplama gibi ek adımlar çözümü ikiden fazla adıma uzatıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru yapraklara burnuyla üfledi"
   - Cümle 10: «Doru yapraklara burnuyla üfledi ve yapraklar otların üstünden uçtu.»
   - Açıklama: Dal çekildikten sonra yaprakları temizleme gibi ek bir adım ekleniyor ve çözüm ikiden fazla adıma uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0050` birebir aynı, `@degisim: şemsiye -> ot` (tutuyorsan), ardından `@onarim: d6340ac1690d70653cf029066ef3b533f9f64aa1`, sonra gövde.
