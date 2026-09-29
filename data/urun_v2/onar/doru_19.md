# Editör görevi (onarım): Doru, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0031 (deneme 5 -> 6)

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
Dağda, vadinin öbür ucunda küçük bir elma ağacı vardı. Doru ağacın alçak dalında kırmızı bir elma gördü. Elma bir taneydi, ama Doru da Karatay da acıkmıştı. Siyah ve şık Karatay beklemek istemedi, sabırsızlandı ve zıpladı. "Elmayı getireyim, ikimiz paylaşalım," dedi Doru. Doru düz vadide hızla koştu. Ağaca varınca elmayı dişleriyle daldan kopardı. Sonra Karatay'ın yanına geri döndü. Elmanın yarısını yedi ve öbür yarısını Karatay'a verdi. "Teşekkürler, Doru, çok tatlıymış," dedi Karatay. Doru bundan sonra bulduğu her elmayı arkadaşıyla paylaştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Siyah ve şık Karatay"
   - Cümle 4: «Siyah ve şık Karatay beklemek istemedi, sabırsızlandı ve zıpladı.»
   - Açıklama: 'Şık' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Siyah ve şık Karatay"
   - Cümle 4: «Siyah ve şık Karatay beklemek istemedi, sabırsızlandı ve zıpladı.»
   - Açıklama: Karatay önceki cümlede geçtikten sonra yeniden tanıtılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sabırsızlandı ve zıpladı"
   - Cümle 4: «Siyah ve şık Karatay beklemek istemedi, sabırsızlandı ve zıpladı.»
   - Açıklama: Karatay'ın sabırsızlanıp zıplaması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0031` birebir aynı, `@degisim: salatalık -> elma` (tutuyorsan), ardından `@onarim: 5211a32c8584515ba740a045a2daef12c804657a`, sonra gövde.

### Hikâye 2: tohum doru-0032 (deneme 5 -> 6)

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
@plan: sürpriz çiçekler uzaktaydı ve annesi az sonra gelecekti | hızla koşup çiçekli dalı annesi gelmeden getirdi
@tohum: doru-0032
@degisim: kaktüs -> çalı
Dağda, vadinin öbür ucunda pembe çiçekli bir çalı vardı. Doru annesine o çiçeklerle sürpriz yapmak istedi. Ama çalı çok uzaktaydı ve annesi kayanın arkasından az sonra gelecekti. Doru düz vadide hızla koştu ve çalıya vardı. Ağzıyla çiçekli bir dal kopardı. Sonra kayanın yanına döndü ve annesi tam o sırada geldi. Doru dalı yere bıraktı ve annesinin kulağına eğildi. "Anne, gözlerini kapat, sana bir sürpriz var," diye fısıldadı Doru. "Bu gizemli sürpriz ne acaba?" diye sordu annesi. Doru dalı ağzıyla alıp annesinin önüne koydu. Annesi gözlerini açtı ve pembe çiçekleri gördü. "Ne güzel bir sürpriz, teşekkür ederim, Doru!" dedi annesi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu gizemli sürpriz ne acaba?"
   - Cümle 9: «"Bu gizemli sürpriz ne acaba?" diye sordu annesi.»
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu gizemli sürpriz ne"
   - Cümle 9: «"Bu gizemli sürpriz ne acaba?" diye sordu annesi.»
   - Açıklama: 'Gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0032` birebir aynı, `@degisim: kaktüs -> çalı` (tutuyorsan), ardından `@onarim: 214ec60736505e40c138f0402c67f8ded54bb375`, sonra gövde.

### Hikâye 3: tohum doru-0036 (deneme 5 -> 6)

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
@plan: oynadığı uzun dal rüzgarla yokuştan aşağı yuvarlandı | sürüye seslenip indi ve dalı çalıların arasında buldu
@tohum: doru-0036
@degisim: bambu -> dal
Rüzgar dağın üstünde esiyordu. Doru sürünün yanında en sevdiği uzun dalla oynuyordu. Birden rüzgar güçlendi ve dalı yokuştan aşağı yuvarladı. Doru dalı artık göremiyordu. Gitmeden önce sürüye seslendi ve nereye gideceğini söyledi. Sonra yokuştan yavaş yavaş aşağı yürüdü. Dal, yokuşun dibindeki çalıların arasına girmişti. Çalılar çok sıktı, ama Doru cesaretle başını içeri uzattı. Dalı dişleriyle tuttu ve dışarı çekti. Dal çok sağlamdı ve hiç kırılmamıştı. Doru onu ağzında sürünün yanına taşıdı. Doru çok sevindi, çünkü en sevdiği oyuncağını yeniden bulmuştu.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "oynadığı uzun dal rüzgarla"
   - Cümle 0 (plan satırı): «oynadığı uzun dal rüzgarla yokuştan aşağı yuvarlandı | sürüye seslenip indi ve dalı çalıların arasında buldu»
   - Açıklama: Plan satırında 'ile' eksik; 'ile oynadığı uzun dal' olmalı.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Gitmeden önce sürüye seslendi"
   - Cümle 5: «Gitmeden önce sürüye seslendi ve nereye gideceğini söyledi.»
   - Açıklama: Arka plandaki çoğul canlı sürü olaya muhatap olarak katılıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sürüye seslendi ve nereye gideceğini söyledi"
   - Cümle 5: «Gitmeden önce sürüye seslendi ve nereye gideceğini söyledi.»
   - Açıklama: Belirsiz kelime sürü canlı ve rol olarak geçiyor; yan alanında böyle bir karakter yok.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sürüye seslendi ve nereye"
   - Cümle 5: «Gitmeden önce sürüye seslendi ve nereye gideceğini söyledi.»
   - Açıklama: Belirsiz kelime sürü canlı bir topluluk olarak seslenilen rol üstleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0036` birebir aynı, `@degisim: bambu -> dal` (tutuyorsan), ardından `@onarim: 0d7d3808c57d6dee658698e9d5b077b9d6694dfc`, sonra gövde.

### Hikâye 4: tohum doru-0037 (deneme 5 -> 6)

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
@plan: sürpriz papatyalar uzaktaydı ve arkadaşı az sonra gelecekti | hızla koşup papatyaları arkadaşı gelmeden getirdi
@tohum: doru-0037
@degisim: zarif -> beyaz
Doru, büyük bir çam ağacının altında Alaca için sürpriz hazırlamak istedi. Alaca beyaz papatyaları çok severdi, ama ağacın altında hiç papatya yoktu. Papatyalar çok uzaktaydı ve Alaca az sonra gelecekti. Alaca erken gelse, sürpriz bozulurdu. Doru düz çayırda hızla koştu. Ağzıyla birçok beyaz papatya kopardı ve ağaca geri döndü. Papatyaları ağacın altına bıraktı. Tam o sırada Alaca geldi ve papatyaları gördü. "Bunlar benim için mi, Doru?" diye sordu Alaca. "Evet, Alaca, hepsi senin," dedi Doru. Alaca sevinçle zıpladı. Doru da çok sevindi, çünkü sürprizini tam zamanında hazırlamıştı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "büyük bir çam ağacının altında"
   - Cümle 1: «Doru, büyük bir çam ağacının altında Alaca için sürpriz hazırlamak istedi.»
   - Açıklama: Başlıktaki yer park ama hikaye çam ağacının altında ve uzak bir çayırda geçiyor; park hiç kurulmuyor.
   - Açıklama: Başlıktaki yer park olduğu halde hikaye hiç parkta geçmiyor; çam ağacı ve uzak çayır arasında gidip gelen bir sahne kuruluyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "erken gelse, sürpriz bozulurdu"
   - Cümle 4: «Alaca erken gelse, sürpriz bozulurdu.»
   - Açıklama: 'Sürpriz bozulmak' soyut ve mecazlı bir ifade.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Alaca erken gelse, sürpriz bozulurdu"
   - Cümle 4: «Alaca erken gelse, sürpriz bozulurdu.»
   - Açıklama: Sürprizin bozulması soyut ve varsayımlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0037` birebir aynı, `@degisim: zarif -> beyaz` (tutuyorsan), ardından `@onarim: 21b62af3dc54f50b563c612c1a44d41f81897193`, sonra gövde.

### Hikâye 5: tohum doru-0038 (deneme 5 -> 6)

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
Bir sabah gökyüzü mavi ve açıktı. Doru, geniş çayırda bir kozalağı burnuyla itip peşinden koşuyordu. Birden kozalak küçük bir fidanın dallarına takıldı ve fidan eğildi. Doru fidana yardım etmek istedi. Kozalağı dişleriyle yavaşça tuttu ve dalların arasından çekti. Dallar hiç kırılmadı, fidan yeniden dik durdu ve bu Doru'yu çok rahatlattı. Doru kozalağı dikkatlice çayırın ortasına götürdü. Oyununa açık çimenlerde yine neşeyle devam etti. Doru bundan sonra kozalağı fidanlardan uzakta itti.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru, geniş çayırda bir kozalağı"
   - Cümle 2: «Doru, geniş çayırda bir kozalağı burnuyla itip peşinden koşuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor ve park hiç anılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu Doru'yu çok rahatlattı"
   - Cümle 6: «Dallar hiç kırılmadı, fidan yeniden dik durdu ve bu Doru'yu çok rahatlattı.»
   - Açıklama: Olayı gösteren soyut 'bu' öznesi ve 'rahatlattı' duygusu 3 yaşındaki çocuk için soyut bir anlatım.
   - Açıklama: 'Bu' soyut bir durumu gösteriyor ve 'rahatlattı' küçük çocuğa soyut kalıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru bundan sonra kozalağı fidanlardan uzakta itti"
   - Cümle 9: «Doru bundan sonra kozalağı fidanlardan uzakta itti.»
   - Açıklama: 'Bundan sonra' süreklilik ister; 'itiyordu' ya da 'uzakta itmeye başladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0038` birebir aynı, `@degisim: paket -> kozalak` (tutuyorsan), ardından `@onarim: 7edf55c1464a1c8184bf95c2475f7c7c258fbdc4`, sonra gövde.

### Hikâye 6: tohum doru-0040 (deneme 5 -> 6)

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
@plan: sürü tepenin arkasına geçmişti ve izler karışmıştı | küçük arkadaşına yolu sordu ve hızla sürüye vardı
@tohum: doru-0040
@degisim: misket -> iz
Dağda serin bir rüzgar esiyordu. Doru ile Alaca büyük bir kayanın yanında saklambaç oynuyordu. Oyun bitince Doru baktı, sürü yakındaki bir tepenin arkasına geçmişti. Yerde çok iz vardı ve bütün izler birbirine karışmıştı. Doru nereye gideceğini bilemedi. "Alaca, sürü hangi yoldan gitti, gördün mü?" diye sordu Doru. "Evet, saklanırken gördüm, sarı çiçekli yoldan gittiler," dedi Alaca. O yolu bulmak kolaydı. Sürü tepenin arkasında çimen yiyordu. Doru düz yolda hızla koştu, Alaca da arkasından geldi. Az sonra ikisi de sürünün yanındaydı. "Teşekkürler, Alaca, iyi ki sana sordum!" dedi Doru.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Oyun bitince Doru baktı, sürü"
   - Cümle 3: «Oyun bitince Doru baktı, sürü yakındaki bir tepenin arkasına geçmişti.»
   - Açıklama: 'Baktı' nesnesiz kalmış ve iki cümle virgülle bozuk biçimde bağlanmış; 'Doru baktı ki' ya da 'Doru bakınca' olmalı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sürü yakındaki bir tepenin arkasına geçmişti"
   - Cümle 3: «Oyun bitince Doru baktı, sürü yakındaki bir tepenin arkasına geçmişti.»
   - Açıklama: Doru sürünün tepenin arkasında olduğunu görüyor ama sonra nereye gideceğini bilemiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0040` birebir aynı, `@degisim: misket -> iz` (tutuyorsan), ardından `@onarim: 271ced8e9f0f2383ee10969a4e45d8524acdd762`, sonra gövde.

### Hikâye 7: tohum doru-0044 (deneme 4 -> 5)

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
Ormanda güçlü bir rüzgar esiyordu. Doru annesiyle ağaçların arasında yürüyordu. Birden yerde gümüş gibi parlayan küçük bir çiçek gördü. Çiçeğin sapı çok inceydi ve rüzgarda kırılacak gibiydi. "Anne, bak, rüzgar bu çiçeği sallıyor!" dedi Doru. "Evet, rüzgar çok sert," dedi annesi. "Ben çiçeğin önünde dururum, anne," dedi Doru. Rüzgar Doru'ya sert sert esti, ama Doru cesaretle yerinden ayrılmadı. Arkasındaki çiçek artık sallanmadı. Az sonra rüzgar yavaşladı. Annesi yanına geldi ve başını Doru'nun başına sürttü. Doru çok sevindi, çünkü küçük çiçek dik kalmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gümüş gibi parlayan küçük"
   - Cümle 3: «Birden yerde gümüş gibi parlayan küçük bir çiçek gördü.»
   - Açıklama: 'Gümüş gibi' benzetmesi küçük çocuk için mecazlı ve zor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Çiçeğin sapı çok inceydi ve rüzgarda kırılacak gibiydi"
   - Cümle 4: «Çiçeğin sapı çok inceydi ve rüzgarda kırılacak gibiydi.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0044` birebir aynı, `@degisim: narin -> ince` (tutuyorsan), ardından `@onarim: 9b4adb14bdde23b5b1d9ce448a4fda0958ce1c2a`, sonra gövde.

### Hikâye 8: tohum doru-0045 (deneme 4 -> 5)

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
@plan: elma buzlu dallara takılmıştı ve dallar ses çıkarıyordu | cesaretle gidip elmayı aldı ve paylaştı
@tohum: doru-0045
@degisim: havuç -> elma
Bir sabah orman çok soğuktu ve Doru ile Karatay acıkmıştı. Ağaçtan düşen kırmızı bir elma buzlu bir çalının dallarına takılmıştı. Ama çalının dalları rüzgarda çıt çıt ses çıkarıyordu ve Karatay yaklaşmadı. Doru cesaretle çalıya yürüdü ve dallara baktı. Sesi yalnız ince buzlar çıkarıyordu. Doru dişlerini elmaya taktı ve onu dışarı çekti. "Karatay, bunu birlikte yiyelim," dedi Doru. Doru elmayı ısırdı ve ikiye böldü. İkisi elmayı yavaş yavaş yedi. Doru çok mutlu oldu, çünkü elmayı en yakın arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru dişlerini elmaya taktı"
   - Cümle 6: «Doru dişlerini elmaya taktı ve onu dışarı çekti.»
   - Açıklama: Dişler elmaya 'takılmaz', 'geçirilir'; fiil yanlış anlamda.
   - Açıklama: Diş elmaya takılmaz, 'geçirdi' olmalı; fiil anlamca uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0045` birebir aynı, `@degisim: havuç -> elma` (tutuyorsan), ardından `@onarim: 2a63e2132b5a803723858699d0927794f08489bc`, sonra gövde.

### Hikâye 9: tohum doru-0046 (deneme 4 -> 5)

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
@plan: kar çimenlerin üstünü kapladı ve yiyecek yoktu | cesaretle karda yürüyüp kayanın dibinde kuru ot buldu
@tohum: doru-0046
@degisim: üzüm -> ot
Dağda lapa lapa kar yağıyordu. Kar bütün çimenlerin üstündeydi ve Doru yiyecek bulamıyordu. Uzakta büyük bir kaya gördü ve altında kar yoktu. Doru orada yiyecek bulmak istedi. Ama arada yumuşak ve soğuk kar vardı. Doru cesaretle karın içine adım attı. Ayakları karda küçük izler bıraktı. Yavaş yavaş kayanın yanına vardı. Kayanın dibinde kuru otlar duruyordu. Doru ağzına sığdığı kadar ot aldı ve afiyetle yedi. Kayanın dibi kuru, sıcak ve huzurluydu. Doru orada karnı tok, mutlu mutlu dinlendi.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kaya gördü ve altında kar yoktu"
   - Cümle 3: «Uzakta büyük bir kaya gördü ve altında kar yoktu.»
   - Açıklama: Özne kayıyor ve iyelik belirsiz; 'kayanın dibinde kar yoktu' gibi kurulmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sıcak ve huzurluydu"
   - Cümle 11: «Kayanın dibi kuru, sıcak ve huzurluydu.»
   - Açıklama: 'Huzurlu' soyut bir kavram; 3 yaşındaki çocuk bilmeyebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuru, sıcak ve huzurluydu"
   - Cümle 11: «Kayanın dibi kuru, sıcak ve huzurluydu.»
   - Açıklama: 'Huzurlu' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0046` birebir aynı, `@degisim: üzüm -> ot` (tutuyorsan), ardından `@onarim: 368e5efd6a9cca49e1a649b1c360f3613aefbe6d`, sonra gövde.

### Hikâye 10: tohum doru-0047 (deneme 4 -> 5)

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
@plan: ayağı taşa takıldı ve marul yokuştan yuvarlandı | yamuk ağacın arkasına cesaretle gidip marulu buldu
@tohum: doru-0047
@degisim: barışmak -> yuvarlanmak
Dağda sert bir rüzgar esiyordu. Doru kayaların arasında bulduğu bir marulu ağzında taşıyordu. Birden ayağı bir taşa takıldı ve marul yokuştan aşağı yuvarlandı. Doru o marulu çok sevmişti. Marulu aramak için yokuştan yavaşça indi. Aşağıda yamuk bir ağaç vardı. Rüzgarda ağacın dalları birbirine çarpıyor ve ses çıkarıyordu. Ama Doru cesaretle ağacın arkasına yürüdü. Marul orada, iki kökün arasında duruyordu. Doru marulu dişleriyle aldı ve ağacın dibinde afiyetle yedi. Doru bundan sonra yokuşta yavaş ve dikkatli yürüdü.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bulduğu bir marulu ağzında"
   - Cümle 2: «Doru kayaların arasında bulduğu bir marulu ağzında taşıyordu.»
   - Açıklama: Marul ekili bir sebzedir ve kartın doğa dünyasında (özgür at sürüsü) yer almıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0047` birebir aynı, `@degisim: barışmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 122b82842d2adfc5195c5f61a4f02a5d19eff493`, sonra gövde.

### Hikâye 11: tohum doru-0048 (deneme 4 -> 5)

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
@plan: susamıştı ama su içtiği çukur kuruydu | dinleyip hızla koştu ve sesi yapan dereyi buldu
@tohum: doru-0048
@degisim: komik -> serin
Doru ormanda çok susamıştı. Ama su içtiği küçük çukur kuruydu. Doru başka su bulmak için durdu ve dikkatle dinledi. Uzaktan şırıl şırıl bir ses geliyordu. Doru bu sesin sudan gelip gelmediğini merak etti. Ağaçların arasında geniş ve düz bir yol vardı. Doru bu yolda hızla koştu ve sesin geldiği yere vardı. Orada küçük bir dere taşların üstünden akıyordu. Su taşlara çarpıyor ve beyaz köpükler yapıyordu. Ses buradan geliyordu. Doru başını eğdi ve dereden içti. Serin su Doru'nun burnunu ıslattı. Sonra Doru derenin kenarında mutlu mutlu otladı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "su içtiği küçük çukur kuruydu"
   - Cümle 2: «Ama su içtiği küçük çukur kuruydu.»
   - Açıklama: Çukurun neden kuru olduğu söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0048` birebir aynı, `@degisim: komik -> serin` (tutuyorsan), ardından `@onarim: 1b1e4b54acbbc533367f51a71eb3514909cbf8e8`, sonra gövde.

### Hikâye 12: tohum doru-0049 (deneme 4 -> 5)

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
@degisim: enerjik -> neşeli
Bir sabah Doru, sürünün çimen yediği çayırda çok neşeliydi. Birden otların arasında küçük çiçekler gördü. Çiçekler susuz kalmış ve solmuştu. Biraz ileride ince ve ıslak bir iz vardı. Doru bu izin nereden geldiğini çok merak etti. İzin yanından yavaşça yürüdü. İzin sonunda yerden ince bir su çıkıyordu. Su büyük bir taşın önünde birikmişti. Taş suyun çiçeklere giden yolunu kapatmıştı. Doru çiçeklere yardım etmek istedi. Başıyla taşı itti ve kenara yuvarladı. Su hemen kuru toprağa aktı ve çiçeklerin dibini ıslattı. Doru çok sevindi ve çayırda koşup oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sürünün çimen yediği çayırda"
   - Cümle 1: «Bir sabah Doru, sürünün çimen yediği çayırda çok neşeliydi.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye sürünün otladığı bir çayırda geçiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Başıyla taşı itti ve kenara yuvarladı"
   - Cümle 11: «Başıyla taşı itti ve kenara yuvarladı.»
   - Açıklama: Büyük bir taşı başla itmek çocuğun taklit edince tehlikeli olabilecek bir davranış.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru çok sevindi ve çayırda koşup oynamaya mutlu mutlu"
   - Cümle 13: «Doru çok sevindi ve çayırda koşup oynamaya mutlu mutlu devam etti.»
   - Açıklama: 'Çok sevindi' ile 'mutlu mutlu' aynı duyguyu gereksiz yere tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0049` birebir aynı, `@degisim: enerjik -> neşeli` (tutuyorsan), ardından `@onarim: 8f21d641ac4206a5567fb21235a37d84b9aa7482`, sonra gövde.
