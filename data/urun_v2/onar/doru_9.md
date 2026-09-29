# Editör görevi (onarım): Doru, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0029
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yeni bir şeyi denemek
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'bayrak', fiil 'vermek', sıfat 'yeşil'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: çalıdan geçerken sırtına küçük dallar ve yapraklar takıldı | dişleriyle hepsini tek tek aldı
@tohum: doru-0029
@degisim: bayrak -> dal
Ormanda Doru ile Kırat yeşil ağaçların altında yürüyordu. Kırat bir çalıdan geçerken sırtına küçük dallar ve yapraklar takıldı. Kırat sırtına uzanamıyordu ve sırtı kaşınıyordu. Doru ona yardım etmek istedi ama daha önce hiç dal toplamamıştı. "Kırat, sırtındakileri ben alırım," dedi Doru. Doru ilk kez denedi ve bir yaprağı dişleriyle çekti. Yaprak kolayca düştü. Doru bütün dalları ve yaprakları tek tek aldı. Sonra Kırat'ın sırtını dişleriyle hafifçe kaşıdı. Kırat gözlerini kapattı ve kuyruğunu salladı. "Nasıl oldu, Kırat?" diye sordu Doru. "Çok güzel oldu, teşekkürler, Doru!" diye cevap verdi Kırat.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "daha önce hiç dal toplamamıştı"
   - Cümle 4: «Doru ona yardım etmek istedi ama daha önce hiç dal toplamamıştı.»
   - Açıklama: Doru'nun deneyimsizliği bir zorluk gibi kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0029` birebir aynı, `@degisim: bayrak -> dal` (tutuyorsan), ardından `@onarim: 71c1ce1aba487a068b3ed3b6a575e3d56cbb80a3`, sonra gövde.

### Hikâye 2: tohum doru-0031 (deneme 1 -> 2)

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
@plan: ağaçta tek elma vardı ve ikisi de onu istiyordu | hızla koşup elmayı getirdi ve yarısını arkadaşına verdi
@tohum: doru-0031
@degisim: salatalık -> elma
Dağda, vadinin öbür ucunda küçük bir elma ağacı vardı. Doru ağacın alçak dalında şık, kırmızı bir elma gördü. Elma bir taneydi, ama Karatay da acıkmıştı. Karatay sabırsızlandı ve yerinde zıpladı. "Elmayı ben getiririm," dedi Doru. Doru düz vadide hızla koştu. Ağaca varınca elmayı dişleriyle daldan kopardı. Sonra Karatay'ın yanına geri döndü. "Bu elmayı ikimiz paylaşalım," dedi Doru. Elmanın yarısını yedi ve öbür yarısını Karatay'a verdi. "Teşekkürler, Doru, çok tatlıymış," dedi Karatay. Doru bundan sonra bulduğu her elmayı arkadaşıyla paylaştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şık, kırmızı bir elma"
   - Cümle 2: «Doru ağacın alçak dalında şık, kırmızı bir elma gördü.»
   - Açıklama: 'Şık' giyim için kullanılır; elmaya uygun değil.
   - Açıklama: 'Şık' giysi için kullanılır, elmaya uygun değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru düz vadide hızla koştu"
   - Cümle 6: «Doru düz vadide hızla koştu.»
   - Açıklama: Sorun tek elmayı ikisinin de istemesi; hızla koşmak bu sebebe yönelmiyor, sorunu yalnız paylaşmak çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0031` birebir aynı, `@degisim: salatalık -> elma` (tutuyorsan), ardından `@onarim: 5c5f06b56eb0621b7a4f430fc7c4b029b8fc6090`, sonra gövde.

### Hikâye 3: tohum doru-0032 (deneme 1 -> 2)

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
@plan: kaktüsteki çiçek açılıyordu ama annesi uzaktaydı | hızla koşup annesini çiçeğin yanına getirdi
@tohum: doru-0032
Dağda, güneşli bir tepede büyük bir kaktüs vardı. Doru kaktüsün üstünde gizemli, pembe bir tomurcuk gördü. Tomurcuk yavaş yavaş açılıyordu, ama annesi vadinin öbür ucundaydı. Doru bu çiçeği annesine göstermek istedi. Hemen düz vadide hızla koştu. Annesi orada çimen yiyordu. Doru annesinin kulağına eğildi. "Anne, benimle gel, sana bir sürpriz var," diye fısıldadı Doru. Annesi gülümsedi ve Doru'nun yanında tepeye yürüdü. Kaktüsün üstündeki pembe çiçek tam açılmıştı. Annesi çiçeğe uzun uzun baktı. Doru sevinçle annesine sokuldu. "Ne güzel bir sürpriz, teşekkür ederim, Doru!" dedi annesi.
```

**Hakem bulguları (6):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "güneşli bir tepede büyük bir kaktüs vardı"
   - Cümle 1: «Dağda, güneşli bir tepede büyük bir kaktüs vardı.»
   - Açıklama: Kartın dağ tarifi ve dizinin dünyasında kaktüs yok; yanlış bir dünya bilgisi veriyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "büyük bir kaktüs vardı"
   - Cümle 1: «Dağda, güneşli bir tepede büyük bir kaktüs vardı.»
   - Açıklama: Kaktüs kartın dağ tarifindeki yılkı atı dünyasına ait değil, diziyi izleyen çocuk için yanlış bilgi.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "üstünde gizemli, pembe bir tomurcuk"
   - Cümle 2: «Doru kaktüsün üstünde gizemli, pembe bir tomurcuk gördü.»
   - Açıklama: 'Gizemli' 3 yaşındaki çocuğa uygun olmayan soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gizemli, pembe bir tomurcuk"
   - Cümle 2: «Doru kaktüsün üstünde gizemli, pembe bir tomurcuk gördü.»
   - Açıklama: 'Gizemli' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ama annesi vadinin öbür"
   - Cümle 3: «Tomurcuk yavaş yavaş açılıyordu, ama annesi vadinin öbür ucundaydı.»
   - Açıklama: Son özne tomurcuk olduğu için 'annesi' zamirinin kimi gösterdiği belirsiz.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hemen düz vadide hızla koştu"
   - Cümle 5: «Hemen düz vadide hızla koştu.»
   - Açıklama: 'Hemen' ve 'hızla' aynı cümlede gereksiz tekrar yapıyor.
   - Açıklama: 'Hemen' ve 'hızla' aynı cümlede gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0032` birebir aynı, ardından `@onarim: 1ba59da718bd72f3129c7c2e402b351ae9714b02`, sonra gövde.

### Hikâye 4: tohum doru-0033 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0033
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'şerit', fiil 'yakalamak', sıfat 'çalışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: şerit oyunu için bir arkadaş gerekiyordu | cesaretle yanındaki atı oyuna çağırdı
@tohum: doru-0033
@degisim: çalışkan -> uzun
Bir sabah Doru dağda ağaç kabuğundan uzun bir şerit buldu. Şeridi havaya atıp yakalamak için bir arkadaş gerekiyordu. Ama yakında oynayacak kimse yoktu, yalnız Kırat vardı. Kırat sessizce çimen yiyordu. Doru cesaretle onun yanına gitti ve onu oyuna çağırdı. Kırat başını salladı ve oyuna katıldı. Önce Doru şeridi ağzıyla havaya attı ve Kırat onu yakaladı. Sonra sıra Kırat'a geldi. Kırat şeridi attı ve Doru zıplayıp onu dişleriyle tuttu. İkisi sırayla oynamaya devam etti. Doru çok sevindi, çünkü oyun için güzel bir arkadaş bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama yakında oynayacak kimse"
   - Cümle 3: «Ama yakında oynayacak kimse yoktu, yalnız Kırat vardı.»
   - Açıklama: 'Yakında' burada 'yakınında' anlamında yanlış kullanılmış; 'yakında' zaman bildirir.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama yakında oynayacak kimse yoktu, yalnız Kırat vardı"
   - Cümle 3: «Ama yakında oynayacak kimse yoktu, yalnız Kırat vardı.»
   - Açıklama: Kırat zaten yanında olduğu için arkadaş bulma sorunu akla yatkın değil.
   - Açıklama: Oynayacak arkadaş zaten yanında olduğu için sorun zayıf ve çağırmak için neden cesaret gerektiği söylenmiyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakında oynayacak kimse yoktu, yalnız Kırat vardı"
   - Cümle 3: «Ama yakında oynayacak kimse yoktu, yalnız Kırat vardı.»
   - Açıklama: Oyun arkadaşı Kırat zaten yanında olduğu için sorun gerçek bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0033` birebir aynı, `@degisim: çalışkan -> uzun` (tutuyorsan), ardından `@onarim: 844abb77a8a0ff986cc5aa2a40000d3c5eb67e43`, sonra gövde.

### Hikâye 5: tohum doru-0034 (deneme 1 -> 2)

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
Bir sabah güneş dağın arkasından doğdu. Doru çimen yerken garip bir tak tak sesi duydu. Ses büyük bir kayanın arkasından geliyordu ve Doru onu çok merak etti. Kayanın arkasına yavaşça yürüdü ve baktı. Orada küçük bir fidan vardı. Fidanın üstüne kuru ve uzun bir dal düşmüştü. Rüzgar esince dal kayaya çarpıyor ve ses çıkarıyordu. Fidan dalın altında eğilmişti ve Doru bunu görünce mutsuz oldu. Doru fidana yardım etmek istedi. Kuru dalı dişleriyle tuttu ve kenara çekti. Fidan yeniden dik durdu ve garip ses de bitti. Doru vadide çimen yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Fidan dalın altında eğilmişti"
   - Cümle 8: «Fidan dalın altında eğilmişti ve Doru bunu görünce mutsuz oldu.»
   - Açıklama: Garip ses sorununun üstüne eğilen fidan diye ikinci bir sorun ekleniyor.
   - Açıklama: Garip ses merakı çözülürken fidanın eğilmesi hikayenin ortasında ikinci bir sorun olarak ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0034` birebir aynı, `@degisim: çit -> fidan` (tutuyorsan), ardından `@onarim: 862527a30690d3a6a40350142dfeafa3205e0dee`, sonra gövde.

### Hikâye 6: tohum doru-0035 (deneme 1 -> 2)

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
@plan: oynarken annesinin sırtına çamur sıçradı | cesaretle özür diledi ve annesiyle dereye gitti
@tohum: doru-0035
@degisim: bağlamak -> yıkamak
Ormanda, ağaçların üstünde yün gibi beyaz bulutlar vardı. Doru orada zıplayarak oynuyordu. Birden çamurlu bir yere bastı ve çamur annesinin sırtına sıçradı. Annesi başını çevirdi ve kirli sırtına baktı. Doru önce biraz utandı. Sonra cesaretle annesinin yanına gitti. "Özür dilerim, anne, daha dikkatli oynayacağım," dedi Doru. Annesi sevinçli bir sesle güldü. "Önemli değil, Doru, çamur suyla temizlenir," dedi annesi. İkisi birlikte yakındaki küçük dereye gitti. Annesi sırtını derede yıkadı ve Doru onu kenarda bekledi. Doru çok sevindi, çünkü annesinin sırtı yine tertemiz olmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yün gibi beyaz bulutlar"
   - Cümle 1: «Ormanda, ağaçların üstünde yün gibi beyaz bulutlar vardı.»
   - Açıklama: Bulutları yüne benzeten benzetme mecazlı bir anlatımdır.
   - Açıklama: 'Yün gibi' benzetmesi 3 yaşındaki çocuk için mecazlı bir anlatım.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Annesi sırtını derede yıkadı ve Doru onu kenarda bekledi"
   - Cümle 11: «Annesi sırtını derede yıkadı ve Doru onu kenarda bekledi.»
   - Açıklama: Çamuru annesi kendisi temizliyor, Doru yalnız kenarda bekliyor.
   - Açıklama: Kirli sırt sorununu Doru değil annesi çözüyor; Doru yalnız kenarda bekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0035` birebir aynı, `@degisim: bağlamak -> yıkamak` (tutuyorsan), ardından `@onarim: f1bb09432e841bed91f33e2cee783019b6ee1ffb`, sonra gövde.

### Hikâye 7: tohum doru-0036 (deneme 1 -> 2)

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
@plan: rüzgar en sevdiği dalı yokuştan aşağı yuvarladı | rüzgara karşı cesaretle yürüyüp dalı kayaların arasında buldu
@tohum: doru-0036
@degisim: bambu -> dal
Rüzgar dağın üstünde sert sert esiyordu. Doru uzun bir dalı ağzıyla sallayarak oynuyordu. Bu dal onun en sevdiği oyuncağıydı. Birden rüzgar dalı yokuştan aşağı yuvarladı ve dal kayboldu. Doru sürüye seslendi, ama sürü çok uzaktaydı. Doru rüzgara karşı cesaretle yokuştan aşağı yürüdü. Kayaların arasına ve otların içine baktı. Sonunda dalı büyük bir kayanın dibinde buldu. Dal çok sağlamdı ve hiç kırılmamıştı. Doru onu ağzına aldı ve yavaş yavaş yukarı çıktı. Doru çok sevindi, çünkü en sevdiği oyuncağını yeniden bulmuştu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru sürüye seslendi, ama sürü çok uzaktaydı"
   - Cümle 5: «Doru sürüye seslendi, ama sürü çok uzaktaydı.»
   - Açıklama: Sürü sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru rüzgara karşı cesaretle yokuştan aşağı yürüdü"
   - Cümle 6: «Doru rüzgara karşı cesaretle yokuştan aşağı yürüdü.»
   - Açıklama: Sert rüzgarda sürüden uzakta tek başına yokuş aşağı gitmek taklit edilince tehlikeli bir davranış örneği.
   - Açıklama: Sürüden uzakta, tek başına sert rüzgarda yokuş aşağı inmek çocuğun taklit edebileceği riskli bir davranıştır.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru rüzgara karşı cesaretle yokuştan aşağı yürüdü"
   - Cümle 6: «Doru rüzgara karşı cesaretle yokuştan aşağı yürüdü.»
   - Açıklama: Rüzgar dalı yokuştan aşağı yuvarladığına göre aşağı esiyor; aşağı yürüyen Doru rüzgara karşı değil rüzgarla birlikte yürür.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0036` birebir aynı, `@degisim: bambu -> dal` (tutuyorsan), ardından `@onarim: eb3ea1a7152d9abba71c9ba4b07de27fdc87ad4a`, sonra gövde.

### Hikâye 8: tohum doru-0037 (deneme 1 -> 2)

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
Doru çayırda, büyük bir çam ağacının altında duruyordu. Alaca çiçekleri çok severdi ve Doru ağacın altına ona çiçek topluyordu. Ama birden rüzgar esti, çiçekler uçtu ve sürpriz bozuldu. Alaca da uzaktan buraya doğru geliyordu. Çayırın öbür ucunda papatyalar vardı. Doru düz çayırda hızla koştu. Ağzıyla birkaç papatya aldı ve ağaca geri döndü. Bunu iki kez daha yaptı. Tam o sırada Alaca geldi ve zarif çiçeklere baktı. "Bunlar benim için mi, Doru?" diye sordu Alaca. "Evet, Alaca, hepsi senin," dedi Doru. Alaca sevinçle zıpladı. Doru da çok sevindi, çünkü sürprizini tam zamanında yeniden hazırlamıştı.
```

**Hakem bulguları (6):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru çayırda, büyük bir çam ağacının altında duruyordu"
   - Cümle 1: «Doru çayırda, büyük bir çam ağacının altında duruyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru ağacın altına ona çiçek topluyordu"
   - Cümle 2: «Alaca çiçekleri çok severdi ve Doru ağacın altına ona çiçek topluyordu.»
   - Açıklama: 'Ağacın altına çiçek toplamak' yönelme ekiyle bozuk kuruluyor; 'ağacın altında toplamak' ya da 'ağacın altına getirmek' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzaktan buraya doğru geliyordu"
   - Cümle 4: «Alaca da uzaktan buraya doğru geliyordu.»
   - Açıklama: Anlatıcı dilinde 'buraya' yeri belirsiz kılıyor; 'ağaca doğru' gibi bir yer adı gerekir.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bunu iki kez daha yaptı"
   - Cümle 8: «Bunu iki kez daha yaptı.»
   - Açıklama: Çözüm aynı gidiş gelişin üç kez tekrarıyla ikiden fazla adım sürüyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "zarif çiçeklere baktı"
   - Cümle 9: «Tam o sırada Alaca geldi ve zarif çiçeklere baktı.»
   - Açıklama: 'Zarif' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geldi ve zarif çiçeklere baktı"
   - Cümle 9: «Tam o sırada Alaca geldi ve zarif çiçeklere baktı.»
   - Açıklama: 'Zarif' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir sıfat.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0037` birebir aynı, ardından `@onarim: d93dfc5c261fb439cd2aba7a3a4947f07cd138fe`, sonra gövde.

### Hikâye 9: tohum doru-0038 (deneme 1 -> 2)

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
Bir sabah gökyüzü mavi ve açıktı. Doru çayırda yuvarlak bir kozalağı burnuyla itip peşinden koşuyordu. Birden kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi. Doru fidana yardım etmek istedi. Kozalağı dişleriyle yavaşça tuttu ve dalların arasından çekti. Dallar kırılmadı ve fidan yeniden dik durdu. Fidanın dik durduğunu görmek Doru'yu rahatlattı. Doru kozalağı dikkatlice çayırın ortasına götürdü. Oyununa açık çimenlerde yine neşeyle devam etti. Doru bundan sonra kozalağı fidanlardan uzakta itti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "görmek Doru'yu rahatlattı"
   - Cümle 7: «Fidanın dik durduğunu görmek Doru'yu rahatlattı.»
   - Açıklama: Adlaştırılmış yapı ve 'rahatlattı' soyut duygu anlatımı 3 yaşa ağır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0038` birebir aynı, `@degisim: paket -> kozalak` (tutuyorsan), ardından `@onarim: c3de1b025ea15fa44e8ce1247dd54f82dd6a42f3`, sonra gövde.

### Hikâye 10: tohum doru-0039 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0039
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'soğan', fiil 'havalanmak', sıfat 'hazır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: yarışta arkadaşını beklemeden koşmaya başladı | özür diledi ve yarışa birlikte yeniden başladı
@tohum: doru-0039
@degisim: soğan -> yaprak
Doru ile Karatay ormandaki düz açıklıkta büyük ağaca kadar yarışacaktı. "Hazır mısın, Doru?" diye sordu Karatay. Ama Doru, Karatay'ı beklemeden hızla koştu. Kuru yapraklar ayaklarının altından havalandı. Doru ağaca ilk vardı ve arkasına baktı. Karatay yerinde duruyordu ve üzgündü. "Ben daha hazır değildim," dedi Karatay. Doru hatasını anladı ve Karatay'ın yanına geri döndü. "Özür dilerim, Karatay, çok acele ettim," dedi Doru. "Tamam, bu kez birlikte başlayalım," dedi Karatay. Sonra iki arkadaş aynı anda yola çıktı. Doru çok sevindi, çünkü Karatay yine onunla gülerek yarışıyordu.
```

**Hakem bulguları (1):**

1. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: ""Hazır mısın, Doru?" diye sordu Karatay"
   - Cümle 2: «"Hazır mısın, Doru?" diye sordu Karatay.»
   - Açıklama: Karatay sonra hazır olmadığını söylüyor; soruyu Doru'nun Karatay'a sorması gerekirdi, konuşan yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0039` birebir aynı, `@degisim: soğan -> yaprak` (tutuyorsan), ardından `@onarim: 8fc58fa3acc4472d6006ec9903b4f12f57786fbe`, sonra gövde.
