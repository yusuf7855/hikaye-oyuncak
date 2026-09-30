# Editör görevi (onarım): Doru, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar47.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0180 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0180
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'külah', fiil 'saçmak', sıfat 'umutlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: boş köşe için hiç tohumları yoktu | cesaretle parkın öbür ucuna koşup tohumlu bir çiçek getirdi
@tohum: doru-0180
@degisim: külah -> tohum
Parkta Doru ile Karatay rüzgar olma oyunu oynuyordu. Parkın bir köşesinde hiç çiçek yoktu. Oraya tohum uçurmak istediler ama hiç tohumları yoktu. Doru parkın öbür ucundaki beyaz, yumuşak çiçekleri hatırladı. O çiçeklerin üstünde bir sürü küçük tohum vardı. Ama orada çok sert bir rüzgar esiyordu. "Ben oraya gitmem, Doru," dedi Karatay. Doru korkmadı ve cesaretle parkın öbür ucuna koştu. Beyaz çiçeklerden birini ağzıyla kopardı ve geri getirdi. İkisi çiçeğe birlikte üfledi ve tohumları boş köşeye saçtı. Küçük tohumlar havada uçtu ve yere indi. Karatay umutluydu ve "Burada yakında çiçekler çıkar!" dedi. Doru çok sevindi, çünkü boş köşede artık tohumlar vardı.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkın bir köşesinde hiç çiçek yoktu"
   - Cümle 2: «Parkın bir köşesinde hiç çiçek yoktu.»
   - Açıklama: Kartın park tarifi geniş bir çayırdır; köşeleri olan, çiçek ekilen bir park insan yapımı bir yer gibi anlatılıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle parkın öbür ucuna koştu"
   - Cümle 8: «Doru korkmadı ve cesaretle parkın öbür ucuna koştu.»
   - Açıklama: Çok sert rüzgarın estiği yere gitmek cesaret örneği olarak sunuluyor; çocuk tehlikeli havaya çıkmayı taklit edebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay umutluydu ve"
   - Cümle 12: «Karatay umutluydu ve "Burada yakında çiçekler çıkar!" dedi.»
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Umutlu' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0180` birebir aynı, `@degisim: külah -> tohum` (tutuyorsan), ardından `@onarim: 0915716388b052cedfac6a4a8ba93d67cac22613`, sonra gövde.

### Hikâye 2: tohum doru-0181 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0181
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yosun', fiil 'giyinmek', sıfat 'havalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: kaygan yosun yüzünden arkadaşı taşın üstünden atlayamadı | yosunu ayağıyla kazıdı ve sırasını arkadaşına verdi
@tohum: doru-0181
@degisim: giyinmek -> zıplamak
Bir sabah Doru ile Karatay havalı parkta sırayla atlama oyunu oynuyordu. Çimenlerin ortasındaki alçak taşın önünde kaygan bir yosun vardı. Karatay koştu ama ayağı yosunun üstünde kaydı ve taşı geçemedi. Karatay üzüldü ve başını eğdi. Sıra Doru'daydı ama Doru önce arkadaşına yardım etti. Ön ayağıyla yosunu taşın önünden kazıdı ve temizledi. "Bir daha dene, Karatay, sıra yine sende," dedi Doru. Karatay yeniden koştu ve taşın üstünden yükseğe zıpladı. "Çok güzel zıpladın, Karatay!" dedi Doru. Sonra sıra Doru'ya geldi ve o da taşın üstünden atladı. İki arkadaş parkta sırayla atlamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Karatay havalı parkta sırayla"
   - Cümle 1: «Bir sabah Doru ile Karatay havalı parkta sırayla atlama oyunu oynuyordu.»
   - Açıklama: 'Havalı' argo ve bu bağlamda yanlış anlamda kullanılmış bir sıfat.
   - Açıklama: 'Havalı' park için yanlış anlamda kullanılmış bir sıfat.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Karatay havalı parkta sırayla"
   - Cümle 1: «Bir sabah Doru ile Karatay havalı parkta sırayla atlama oyunu oynuyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayır; 'havalı park' insan parkını çağrıştırıyor.
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; 'havalı park' insan yapımı bir parkı çağrıştırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0181` birebir aynı, `@degisim: giyinmek -> zıplamak` (tutuyorsan), ardından `@onarim: 3fa2c265080b52eeacaa598ccbc048d4cdac2ae5`, sonra gövde.

### Hikâye 3: tohum doru-0182 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0182
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'halka', fiil 'binmek', sıfat 'aydınlık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: yolda eğri bir dal alçak bir halka yapmıştı | cesaretle başını eğdi ve halkadan geçti
@tohum: doru-0182
@degisim: binmek -> geçmek
Ormanda Doru, hazine arama oyunu oynuyordu. Oyunda aydınlık bir çimenlik onun hazinesiydi. Ama yolda eğri bir dal yere eğilmiş ve alçak bir halka yapmıştı. Halkanın içinde yapraklar sallanıyordu ve Doru geçmeye biraz korktu. Sonra cesaretle başını aşağı eğdi ve halkadan yavaşça geçti. Yapraklar yalnız sırtına hafifçe değdi. Dalın arkasında güneşli, geniş bir çimenlik vardı. Doru çimenliğe koştu ve sevinçle zıpladı. Oyunda aradığı hazineyi sonunda bulmuştu. Doru bundan sonra alçak dallardan hiç korkmadı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aydınlık bir çimenlik onun hazinesiydi"
   - Cümle 2: «Oyunda aydınlık bir çimenlik onun hazinesiydi.»
   - Açıklama: Çimenliğin hazine olması mecazdır ve küçük çocuğa uygun değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "eğri bir dal yere eğilmiş ve alçak bir halka yapmıştı"
   - Cümle 3: «Ama yolda eğri bir dal yere eğilmiş ve alçak bir halka yapmıştı.»
   - Açıklama: Sorun yalnızca başı eğip geçilen önemsiz bir engel; gerçek bir sorun kurulmuyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru geçmeye biraz korktu"
   - Cümle 4: «Halkanın içinde yapraklar sallanıyordu ve Doru geçmeye biraz korktu.»
   - Açıklama: Korkmak fiili -den eki ister; 'geçmekten biraz korktu' olmalı.
   - Açıklama: 'Korkmak' ayrılma eki ister; 'geçmekten korktu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0182` birebir aynı, `@degisim: binmek -> geçmek` (tutuyorsan), ardından `@onarim: 999cc316879e3d4f91b981577b4eaf888d3b6611`, sonra gövde.

### Hikâye 4: tohum doru-0183 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0183
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'baloncuk', fiil 'geçmek', sıfat 'mor'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kozalak bir taşa çarptı ve çalılara doğru yuvarlandı | düz çimende hızla koşup kozalağa yetişti
@tohum: doru-0183
@degisim: baloncuk -> kozalak
Doru parkta bir kozalakla eğlenceli bir oyun oynuyordu. Kozalağı burnuyla itip mor çiçeklerin yanına götürüyordu. Ama kozalak bir taşa çarptı ve çiçeklerin yanından geçip gitti. Kozalak parkın kenarındaki sık çalılara doğru yuvarlanıyordu. Doru onu hemen yakalamak istedi. Doru düz çimenlerin üstünde hızla koştu. Kozalağa yetişti ve onu ön ayağıyla durdurdu. Kozalak çalıların hemen önünde kaldı. Doru onu burnuyla yavaşça geri itti. Bu kez kozalak mor çiçeklerin tam yanına vardı. Doru çok sevindi, çünkü kozalağını kaybetmemişti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama kozalak bir taşa çarptı"
   - Cümle 3: «Ama kozalak bir taşa çarptı ve çiçeklerin yanından geçip gitti.»
   - Açıklama: Kozalak yuvarlanıyor, Doru koşup yakalıyor ve bitiyor; sorun önemsiz bir olay.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kozalak bir taşa çarptı ve çiçeklerin yanından geçip gitti"
   - Cümle 3: «Ama kozalak bir taşa çarptı ve çiçeklerin yanından geçip gitti.»
   - Açıklama: Yuvarlanan kozalağa koşup yetişmek önemsiz bir olay; sorun kurulur kurulmaz tek hamlede bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0183` birebir aynı, `@degisim: baloncuk -> kozalak` (tutuyorsan), ardından `@onarim: f9cd3699aef95c041be8003e79b229be5b324d5f`, sonra gövde.

### Hikâye 5: tohum doru-0184 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0184
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'tohum', fiil 'sevmek', sıfat 'ekşi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük arkadaş yorgundu ve ekşi erikler uzaktaydı | düz çimenlikte hızla koşup bir erik getirdi
@tohum: doru-0184
@degisim: tohum -> erik
Doru dağda küçük Alaca'ya bir sürpriz hazırlamak istedi. Alaca bu sabah ilk kez çok uzağa gitmişti. Alaca ekşi erikleri çok severdi ama erik ağacı uzaktaydı. Alaca yorgundu ve şimdi çimenlerin üstünde uyuyordu. Doru düz çimenlikte hızla koştu ve erik ağacına vardı. Yere düşmüş bir eriği ağzına aldı ve hemen döndü. Eriği Alaca'nın önüne yavaşça bıraktı. Alaca gözlerini açtı ve eriği gördü. "Bu benim için mi, Doru?" diye sordu Alaca. "Evet, bugün çok yol gittin," dedi Doru. Alaca eriği ısırdı ve mutlulukla başını salladı. Doru, küçük bir sürprizin arkadaşını mutlu ettiğini öğrendi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama erik ağacı uzaktaydı"
   - Cümle 3: «Alaca ekşi erikleri çok severdi ama erik ağacı uzaktaydı.»
   - Açıklama: Uzaklık hızlı Doru için gerçek bir engel değil; Doru yalnız koşup eriği getiriyor, ortada önemsenecek bir sorun yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Alaca ekşi erikleri çok severdi ama erik ağacı uzaktaydı"
   - Cümle 3: «Alaca ekşi erikleri çok severdi ama erik ağacı uzaktaydı.»
   - Açıklama: Uyuyan Alaca'nın hiçbir sorunu yok; hikayede gerçek bir sorun yerine yalnız bir sürpriz isteği var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0184` birebir aynı, `@degisim: tohum -> erik` (tutuyorsan), ardından `@onarim: 8c8ee54042c729f97fb30934ddf1c89e963e229d`, sonra gövde.

### Hikâye 6: tohum doru-0187 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0187
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'limon', fiil 'takılmak', sıfat 'eksik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: annesinin yelesi sık bir çalıya takıldı | cesaretle çalıya yaklaştı ve dalı dişleriyle çekti
@tohum: doru-0187
@degisim: limon -> çalı
Parkta Doru ile annesi yan yana çimen yiyordu. Birden annesinin uzun yelesi sık bir çalıya takıldı. Annesi başını çekti ama yelesi dallardan çıkmadı. "Doru, bana yardım eder misin?" dedi annesi. Çalının dibi ıslak ve çamurluydu. Doru çamurdan hiç kaçmadı. Sonra cesaretle çalıya yaklaştı ve dalı dişleriyle tuttu. Dalı yavaşça geri çekti ve annesi başını kurtardı. Annesi yelesini salladı, hiçbir tel eksik değildi. "Teşekkürler, Doru, çok iyi yardım ettin," dedi annesi. İkisi parkta yan yana mutlu mutlu çimen yemeye devam etti.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta Doru ile annesi"
   - Cümle 1: «Parkta Doru ile annesi yan yana çimen yiyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; gövde yeri insan yapımı bir park gibi 'park' diye adlandırıyor ve dizide park yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "annesi başını kurtardı"
   - Cümle 8: «Dalı yavaşça geri çekti ve annesi başını kurtardı.»
   - Açıklama: 'Başını kurtarmak' bir deyimdir ve burada kurtarılan baş değil yeledir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0187` birebir aynı, `@degisim: limon -> çalı` (tutuyorsan), ardından `@onarim: 3dafa78ebcb8de25c6ac5a785f01565be09a7c06`, sonra gövde.

### Hikâye 7: tohum doru-0188 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0188
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'iz', fiil 'kaldırmak', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: elma yuvarlandı ve yapraklı bir dalın altına girdi | cesaretle iz boyunca yürüdü ve dalı kaldırdı
@tohum: doru-0188
Bir sabah Doru ormanda bir elmayı burnuyla itip oynuyordu. Ama elma yuvarlandı ve yapraklı bir dalın altına girdi. Doru elmasını göremedi ve çok üzüldü. Dalın çevresi ıslak ve çamurluydu. Çamurda elmanın yuvarlanırken yaptığı ince bir iz vardı. Doru çamurdan kaçmadı ve cesaretle iz boyunca yürüdü. İz dalın altında bitiyordu. Doru dalı dişleriyle tuttu ve yavaşça kaldırdı. Kırmızı elma yaprakların altında duruyordu. Doru elmayı burnuyla dışarı itti ve dalı bıraktı. Ayakları çamurdan kirli olmuştu. Doru çok sevindi, çünkü elmasını bulmuş ve oyununa geri dönmüştü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ayakları çamurdan kirli olmuştu"
   - Cümle 11: «Ayakları çamurdan kirli olmuştu.»
   - Açıklama: Kirli ayaklar ayrıntısı olaya hiçbir şey katmıyor ve bir daha kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0188` birebir aynı, ardından `@onarim: 9d72533a9b1b346f0c1b3ea8bf429d2a9c00c04f`, sonra gövde.

### Hikâye 8: tohum doru-0189 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0189
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'soğan', fiil 'ilgilenmek', sıfat 'eğlenceli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: kozalak iki kayanın arasına girdi ve çıkmadı | küçük arkadaşından yardım istedi ve önce kendisi baktı
@tohum: doru-0189
@degisim: soğan -> kozalak
Bir sabah dağda küçük Alaca yerdeki bir kozalakla ilgilendi. Doru ile Alaca onu itip eğlenceli bir oyun oynadı. Ama kozalak yuvarlandı ve iki kaya arasına girdi. Doru burnunu uzattı ama kayaların arasına sığmadı. "Alaca, sen küçüksün, onu alır mısın?" diye sordu Doru. "Orası çok karanlık, korkuyorum," dedi Alaca. Doru cesaretle başını eğdi ve içeri baktı. "Korkma, Alaca, içeride yalnız kozalak var," dedi Doru. Alaca küçük ön ayağını uzattı ve kozalağı dışarı yuvarladı. "İşte buldum!" dedi Alaca. Doru çok sevindi, çünkü yardım isteyince oyunları yine başlamıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yerdeki bir kozalakla ilgilendi"
   - Cümle 1: «Bir sabah dağda küçük Alaca yerdeki bir kozalakla ilgilendi.»
   - Açıklama: 'İlgilenmek' soyut bir fiil, 3 yaşındaki çocuk için somut değil.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Orası çok karanlık, korkuyorum"
   - Cümle 6: «"Orası çok karanlık, korkuyorum," dedi Alaca.»
   - Açıklama: Kozalağın sıkışmasına ek olarak Alaca'nın karanlık korkusu ikinci bir sorun olarak ortaya çıkıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Alaca küçük ön ayağını uzattı"
   - Cümle 9: «Alaca küçük ön ayağını uzattı ve kozalağı dışarı yuvarladı.»
   - Açıklama: Karanlık kaya aralığına ayak (el) sokmak çocuğun taklit edebileceği tehlikeli bir davranış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "İşte buldum!" dedi Alaca"
   - Cümle 10: «"İşte buldum!" dedi Alaca.»
   - Açıklama: Kozalak kaybolmamıştı, kayaların arasında sıkışmıştı; 'buldum' yerine 'aldım' uygun olurdu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0189` birebir aynı, `@degisim: soğan -> kozalak` (tutuyorsan), ardından `@onarim: 1b9ab6ba5f26e438d7e14693273bbc5f1f941004`, sonra gövde.

### Hikâye 9: tohum doru-0192 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0192
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'yiyecek', fiil 'anlaşmak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: çalının dibinden garip bir pat sesi geldi | cesaretle çalıya yaklaştı ve düşen elmayı buldu
@tohum: doru-0192
@degisim: anlaşmak -> anlamak
Parkın kenarından pat diye bir ses geldi. Doru çimen yerken başını kaldırdı ve dinledi. Ses büyük bir ağacın altındaki sık çalıdan gelmişti. Çalının dibi ıslak ve çamurluydu. Doru bu sesi çok merak etti. Cesaretle çalıya yaklaştı ve burnuyla dalları itti. Çimenlerin arasında kırmızı bir elma duruyordu. Elma çok parlaktı ama plastik değildi, gerçek bir yiyecekti. O anda ağaçtan bir elma daha düştü ve pat diye ses çıkardı. Doru çok sevindi, çünkü sesin düşen elmalardan geldiğini anlamıştı.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkın kenarından pat diye"
   - Cümle 1: «Parkın kenarından pat diye bir ses geldi.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; hikaye yeri insan yapımı bir park olarak adlandırıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalının dibi ıslak ve çamurluydu"
   - Cümle 4: «Çalının dibi ıslak ve çamurluydu.»
   - Açıklama: Islak ve çamurlu çalı dibi ile elmanın plastik olmadığı ayrıntısı kurulup hiçbir işe yaramıyor.
   - Açıklama: Çalının ıslak ve çamurlu olması işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ama plastik değildi"
   - Cümle 8: «Elma çok parlaktı ama plastik değildi, gerçek bir yiyecekti.»
   - Açıklama: Plastik doğa dünyasındaki kapalı karta ait olmayan çağdaş bir nesne.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0192` birebir aynı, `@degisim: anlaşmak -> anlamak` (tutuyorsan), ardından `@onarim: 22f1ad04ed1d860af96f83c6d653c2ea7311fa55`, sonra gövde.
