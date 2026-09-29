# Editör görevi (onarım): Doru, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0045 (deneme 5 -> 6)

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
Bir sabah orman çok soğuktu ve Doru ile Karatay acıkmıştı. Rüzgar, ağaçtan düşen kırmızı bir elmayı buzlu bir çalının dallarına takmıştı. Ama çalının dalları rüzgarda çıt çıt ses çıkarıyordu ve Karatay yaklaşmadı. Doru cesaretle çalıya yürüdü ve dallara baktı. Sesi yalnız ince buzlar çıkarıyordu. Doru elmayı dişleriyle tuttu ve dışarı çekti. "Karatay, bunu birlikte yiyelim," dedi Doru. Doru elmayı ısırdı ve ikiye böldü. İkisi elmayı yavaş yavaş yedi. Doru çok mutlu oldu, çünkü elmayı en yakın arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar, ağaçtan düşen kırmızı bir elmayı buzlu bir çalının dallarına takmıştı"
   - Cümle 2: «Rüzgar, ağaçtan düşen kırmızı bir elmayı buzlu bir çalının dallarına takmıştı.»
   - Açıklama: Yere düşen elmayı rüzgarın çalı dallarına takması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0045` birebir aynı, `@degisim: havuç -> elma` (tutuyorsan), ardından `@onarim: 3d44627f9bd86c36862685cb8171b06f06a469f5`, sonra gövde.

### Hikâye 2: tohum doru-0046 (deneme 5 -> 6)

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
Dağda lapa lapa kar yağıyordu. Kar bütün çimenlerin üstündeydi ve Doru yiyecek bulamıyordu. Uzakta büyük bir kaya vardı ve dibinde hiç kar yoktu. Doru orada yiyecek bulmak istedi. Ama arada yumuşak ve soğuk kar vardı. Doru cesaretle karın içine adım attı. Ayakları karda küçük izler bıraktı. Yavaş yavaş kayanın yanına vardı. Kayanın dibinde kuru otlar duruyordu. Doru ağzına sığdığı kadar ot aldı ve afiyetle yedi. Kayanın dibi kuru ve sıcaktı. Doru orada karnı tok, huzurlu ve mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dağda lapa lapa kar"
   - Cümle 1: «Dağda lapa lapa kar yağıyordu.»
   - Açıklama: 'Lapa lapa' deyimsel ikileme 3 yaşındaki çocuğun bilmeyeceği bir anlatımdır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karnı tok, huzurlu ve mutlu"
   - Cümle 12: «Doru orada karnı tok, huzurlu ve mutlu dinlendi.»
   - Açıklama: 'Huzurlu' soyut bir kavramdır ve 3 yaşındaki çocuğa uygun değildir.
   - Açıklama: 'Huzurlu' soyut bir kelime ve 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0046` birebir aynı, `@degisim: üzüm -> ot` (tutuyorsan), ardından `@onarim: 78dddb068bb8ac3a1df9f060798aab06420d7507`, sonra gövde.

### Hikâye 3: tohum doru-0047 (deneme 5 -> 6)

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
Dağda sert bir rüzgar esiyordu. Doru kayaların arasında biten bir marulu ağzında taşıyordu. Birden ayağı bir taşa takıldı ve marul yokuştan aşağı yuvarlandı. Doru o marulu çok sevmişti. Marulu aramak için yokuştan yavaşça indi. Aşağıda yamuk bir ağaç vardı. Rüzgarda ağacın dalları birbirine çarpıyor ve ses çıkarıyordu. Ama Doru cesaretle ağacın arkasına yürüdü. Marul orada, iki kökün arasında duruyordu. Doru marulu dişleriyle aldı ve ağacın dibinde afiyetle yedi. Doru bundan sonra yokuşta yavaş ve dikkatli yürüdü.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kayaların arasında biten bir"
   - Cümle 2: «Doru kayaların arasında biten bir marulu ağzında taşıyordu.»
   - Açıklama: 'Biten' burada 'yetişen' anlamında; 3 yaşındaki çocuk bunu 'sona eren' diye anlar.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kayaların arasında biten bir marulu"
   - Cümle 2: «Doru kayaların arasında biten bir marulu ağzında taşıyordu.»
   - Açıklama: 'Biten' yetişen anlamında eski bir kullanım; küçük çocuk bu anlamı bilmez.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "kayaların arasında biten bir marulu"
   - Cümle 2: «Doru kayaların arasında biten bir marulu ağzında taşıyordu.»
   - Açıklama: Marul bahçe sebzesidir; kartın özgür at sürüsü dünyasında kayalarda biten marul yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0047` birebir aynı, `@degisim: barışmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 10ad9c240916efaddbcfa84e33d494d8c4921a56`, sonra gövde.

### Hikâye 4: tohum doru-0048 (deneme 5 -> 6)

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
@plan: susamıştı ama su içtiği çukur kurumuştu | dinleyip hızla koştu ve sesi yapan dereyi buldu
@tohum: doru-0048
@degisim: komik -> serin
Doru ormanda çok susamıştı. Ama sıcak güneşte, su içtiği küçük çukur kurumuştu. Doru başka su bulmak için durdu ve dikkatle dinledi. Uzaktan şırıl şırıl bir ses geliyordu. Doru bu sesin sudan gelip gelmediğini merak etti. Ağaçların arasında geniş ve düz bir yol vardı. Doru bu yolda hızla koştu ve sesin geldiği yere vardı. Orada küçük bir dere taşların üstünden akıyordu. Su taşlara çarpıyor ve beyaz köpükler yapıyordu. Ses buradan geliyordu. Doru başını eğdi ve dereden içti. Serin su Doru'nun burnunu ıslattı. Sonra Doru derenin kenarında mutlu mutlu otladı.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Ama sıcak güneşte, su içtiği"
   - Cümle 2: «Ama sıcak güneşte, su içtiği küçük çukur kurumuştu.»
   - Açıklama: 'Güneşte' sonrasındaki virgül gereksiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0048` birebir aynı, `@degisim: komik -> serin` (tutuyorsan), ardından `@onarim: d5d10bd4d5a6db42caa6a6cb5d0bab6658b00dc7`, sonra gövde.

### Hikâye 5: tohum doru-0049 (deneme 5 -> 6)

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
Bir sabah Doru parkta çok neşeliydi. Birden otların arasında küçük çiçekler gördü. Çiçekler susuz kalmış ve solmuştu. Biraz ileride ince ve ıslak bir iz vardı. Doru bu izin nereden geldiğini çok merak etti. İzin yanından yavaşça yürüdü. İzin sonunda yerden ince bir su çıkıyordu. Su küçük bir taşın önünde birikmişti. Taş suyun çiçeklere giden yolunu kapatmıştı. Doru çiçeklere yardım etmek istedi. Burnuyla taşı yavaşça kenara itti. Su hemen kuru toprağa aktı ve çiçeklerin dibini ıslattı. Sonra Doru parkta koşup oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra Doru parkta koşup oynamaya mutlu mutlu devam etti"
   - Cümle 13: «Sonra Doru parkta koşup oynamaya mutlu mutlu devam etti.»
   - Açıklama: Son cümle çiçeklere dönmüyor, çiçeklerin canlandığı görünmüyor ve kapanış olaya bağlı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0049` birebir aynı, `@degisim: enerjik -> neşeli` (tutuyorsan), ardından `@onarim: 4290aa0747f589f4341d7b57e1f4540f7bbef996`, sonra gövde.

### Hikâye 6: tohum doru-0050 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: en güzel otlar kuru bir dalın altında kalmıştı | dalı çekti ve arkadaşıyla birlikte yığını yaptı
@tohum: doru-0050
@degisim: şemsiye -> ot
Sürünün çimen yediği geniş parkta güneş parlıyordu. Doru ile Karatay birlikte büyük bir ot yığını yapıyordu. Ama en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı. Karatay dala baktı ve üzgün üzgün burnundan üfledi. Doru hemen arkadaşına yardım etmek istedi. Dalın bir ucunu dişleriyle tuttu ve çekti. Karatay da öbür ucunu tuttu. İkisi dalı birlikte kenara çekti. Sonra ikisi güzel otları kopardı ve yığına taşıdı. Yığın kocaman oldu ve nefis kokuyordu. Doru ile Karatay ot yığınının yanında mutlu mutlu yemek yedi.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Sürünün çimen yediği geniş parkta"
   - Cümle 1: «Sürünün çimen yediği geniş parkta güneş parlıyordu.»
   - Açıklama: Kartın park tarifi geniş bir çayırdır ve dizide park yoktur, ama hikaye yeri metinde park diye anıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı"
   - Cümle 3: «Ama en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı.»
   - Açıklama: Parkta bol çimen varken otların bir dalın altında kalması önemsiz, zayıf bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0050` birebir aynı, `@degisim: şemsiye -> ot` (tutuyorsan), ardından `@onarim: e00cefe90f452396cd3a72d542cf902cacae5ec2`, sonra gövde.

### Hikâye 7: tohum doru-0053 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0053
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çan', fiil 'güzelleşmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sıcakta susamıştı ama yakında hiç su yoktu | cesaretle çalılardan geçip sesi yapan suyu buldu
@tohum: doru-0053
@degisim: çan -> dal
Ormanda bir ses geliyordu: tıp, tıp. Doru sıcakta çok susamıştı ama yakında hiç su yoktu. Ses sık çalıların arkasından geliyordu ve Doru onu merak etti. Belki orada su vardı. Doru bir an durdu, sonra cesaretle çalıların arasından geçti. Arkada yukarıdaki kayalardan ince bir su iniyordu. Su bir dalın üstünden akıp taşlara düşüyordu. Ses bu sudan geliyordu. Doru başını eğdi ve serin, tatlı sudan içti. Güneş vurunca su damlaları parladı ve orası daha da güzelleşti. Doru suyun yanındaki çimenlerde mutlu mutlu otladı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ama yakında hiç su yoktu"
   - Cümle 2: «Doru sıcakta çok susamıştı ama yakında hiç su yoktu.»
   - Açıklama: Yakında hiç su olmadığı söyleniyor ama su hemen çalıların arkasında çıkıyor.
   - Açıklama: Yakında hiç su olmadığı kesin söyleniyor ama su hemen yandaki çalıların arkasında çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Güneş vurunca su damlaları parladı"
   - Cümle 10: «Güneş vurunca su damlaları parladı ve orası daha da güzelleşti.»
   - Açıklama: Parlayan damlalar olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0053` birebir aynı, `@degisim: çan -> dal` (tutuyorsan), ardından `@onarim: cd9b990ccc23853128d6ec6c40b5173254126757`, sonra gövde.

### Hikâye 8: tohum doru-0054 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0054
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'portakal', fiil 'eklemek', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: kaya yokuşun başındaydı ve elmaların çoğu aşağı yuvarlandı | cesaretle çalının arkasına geçti ve elmaları düz yere yığdı
@tohum: doru-0054
@degisim: portakal -> elma
Doru, Kırat ile dağda yürüyordu. Kırat sürü için büyük bir kayanın dibine elma toplamıştı. Ama kaya bir yokuşun başındaydı ve elmaların çoğu aşağı yuvarlanmıştı. "Elmalarım kayboldu, Doru," dedi Kırat. Doru yere baktı. Çimenin üstünde dağınık birkaç elma vardı. Doru bu elmaların gittiği yoldan yavaşça yürüdü. Yokuşun dibinde büyük ve sık bir çalı vardı. Doru bir an durdu. Sonra cesaretle çalının arkasına geçti. Kaybolan elmalar orada yerde duruyordu. Doru bu elmaları çalının yanındaki düz çimene yığdı. Sonra kayanın yanındaki elmaları da getirip yığına ekledi. "Teşekkürler, Doru, elmalar burada kalır, sürü çok sevinecek!" dedi Kırat.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra cesaretle çalının arkasına geçti"
   - Cümle 10: «Sonra cesaretle çalının arkasına geçti.»
   - Açıklama: Çalının arkasında hiçbir tehlike kurulmadığı için cesaret gerektiren an sebepsiz kalıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kayanın yanındaki elmaları da getirip yığına ekledi"
   - Cümle 13: «Sonra kayanın yanındaki elmaları da getirip yığına ekledi.»
   - Açıklama: Çözüm iz sürme, çalının arkasına geçme, yığma ve kalan elmaları taşıma olarak ikiden fazla adıma yayılıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sürü çok sevinecek"
   - Cümle 14: «"Teşekkürler, Doru, elmalar burada kalır, sürü çok sevinecek!" dedi Kırat.»
   - Açıklama: Belirsiz kelime sürü canlı ve duygu taşıyan bir rol olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0054` birebir aynı, `@degisim: portakal -> elma` (tutuyorsan), ardından `@onarim: 10b91e91df92ed53f0c21260ffe58831ed8a9e42`, sonra gövde.

### Hikâye 9: tohum doru-0063 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0063
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çimen', fiil 'güzelleştirmek', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: dikenli tohumlar sırtına yapıştı ve düşmedi | annesinden tohumları almasını istedi
@tohum: doru-0063
Dağda yumuşak çimenler vardı ve aralarında benekli çiçekler açmıştı. Doru çimene yattı ve sağa sola yuvarlandı. Ama kuru, dikenli tohumlar sırtına yapıştı. Doru kendini salladı ama tohumlar düşmedi. Ağzı da sırtına yetişmedi. Doru biraz utandı ama cesaretle annesine gitti. Annesinden sırtındaki tohumları almasını istedi. Annesi tohumları dişleriyle tek tek aldı. Sonunda son tohum da yere düştü. Sonra annesi burnuyla Doru'nun tüylerini güzelleştirdi. Doru ile annesi benekli çiçeklerin yanında mutlu mutlu otladı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru'nun tüylerini güzelleştirdi"
   - Cümle 10: «Sonra annesi burnuyla Doru'nun tüylerini güzelleştirdi.»
   - Açıklama: 'Tüylerini güzelleştirdi' doğal değil; 'tüylerini düzeltti' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "burnuyla Doru'nun tüylerini güzelleştirdi"
   - Cümle 10: «Sonra annesi burnuyla Doru'nun tüylerini güzelleştirdi.»
   - Açıklama: 'Burnuyla tüyleri güzelleştirmek' yanlış kelime seçimi; 'düzeltti' ya da 'yaladı' gibi somut bir fiil olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0063` birebir aynı, ardından `@onarim: bb9e0da40e1eea5b178ecc18e44e2dfdaabef168`, sonra gövde.

### Hikâye 10: tohum doru-0070 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0070
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gölge', fiil 'anlatmak', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yağmur başladı ve yakında hiç ağaç yoktu | cesaretle yağmurda yürüyüp büyük kayanın altına girdi
@tohum: doru-0070
@degisim: anlatmak -> saklanmak
Dağda güneş vardı ve Doru tek başına çimen yiyordu. Birden Doru'nun gölgesi kayboldu, çünkü bulutlar gelmişti. Sonra yağmur başladı ve Doru'nun sırtı ıslandı. Yakında hiç ağaç yoktu. Biraz ileride eskimiş, büyük bir kaya vardı. Yağmur çok yağıyordu ama Doru cesaretle kayaya kadar yürüdü. Kayanın bir yanı öne çıkmıştı ve altı kuruydu. Doru oraya girdi ve hiç ıslanmadı. Bir süre sonra bulutlar gitti ve güneş çıktı. Doru oradan çıktı ve yeniden çimen yemeye başladı. Doru bundan sonra yağmur başlayınca o kayanın altına saklandı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ileride eskimiş, büyük bir kaya"
   - Cümle 5: «Biraz ileride eskimiş, büyük bir kaya vardı.»
   - Açıklama: Kaya için 'eskimiş' kelimesi uygun değil.
   - Açıklama: Kaya eskimez; sıfat öznesine uymuyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru oraya girdi ve hiç ıslanmadı"
   - Cümle 8: «Doru oraya girdi ve hiç ıslanmadı.»
   - Açıklama: Doru'nun sırtı yağmurda zaten ıslanmış ve sağanakta yürümüşken hiç ıslanmadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0070` birebir aynı, `@degisim: anlatmak -> saklanmak` (tutuyorsan), ardından `@onarim: 3c9ad98b2a73290990209e064119f0ad9fc12e6e`, sonra gövde.

### Hikâye 11: tohum doru-0072 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0072
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'taş', fiil 'sıkılmak', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: tek başına sıkılmıştı ve çalılardan bir ses geliyordu | cesaretle geçip taşa damlayan suyu buldu ve oynadı
@tohum: doru-0072
Garip bir ses geliyordu: tık, tık. Doru ormanda tek başına çok sıkılmıştı ve bu sesi hemen duydu. Ses yakındaki çalıların arkasından geliyordu ve Doru onu çok merak etti. Doru bir an durdu, sonra cesaretle çalıların arasından geçti. Arkada büyük, düz bir taş vardı. Yukarıdaki kayalardan ince bir su iniyordu. Her damla taşa düşünce tık diye ses çıkarıyordu. Doru suyun altında oynadı ve az sonra sırılsıklam oldu. Serin su Doru'yu çok güldürdü. Doru artık sıkılmıyordu, çünkü sesin yanında yeni bir oyun bulmuştu.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Garip bir ses geliyordu"
   - Cümle 1: «Garip bir ses geliyordu: tık, tık.»
   - Açıklama: Ormanda tek başına duyulan garip ses gerilim ve korku öğesi olarak açılıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sonra cesaretle çalıların arasından geçti"
   - Cümle 4: «Doru bir an durdu, sonra cesaretle çalıların arasından geçti.»
   - Açıklama: Tek başına bilinmeyen bir sesin geldiği çalılığa girmek çocuk için taklit edilince tehlikeli bir davranış.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle çalıların arasından geçti"
   - Cümle 4: «Doru bir an durdu, sonra cesaretle çalıların arasından geçti.»
   - Açıklama: Tek başına bilinmeyen bir sesin peşinden çalılara girmek çocuğun taklit edebileceği riskli bir davranış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesin yanında yeni bir oyun"
   - Cümle 10: «Doru artık sıkılmıyordu, çünkü sesin yanında yeni bir oyun bulmuştu.»
   - Açıklama: 'Sesin yanında' anlamsız; sesin bir yanı olmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0072` birebir aynı, ardından `@onarim: 3d450e9bbba0589f2ad57aea56d44edbc63e931c`, sonra gövde.

### Hikâye 12: tohum doru-0074 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0074
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'küp', fiil 'selamlamak', sıfat 'uslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük arkadaşı alçak sesle konuşunca ses geri gelmedi | cesaretle onunla birlikte yüksek sesle bağırdı
@tohum: doru-0074
@degisim: küp -> kaya
Dağda Doru ile Alaca bir ses oyunu oynuyordu. Sırayla kayaya "Merhaba!" diye bağırıyor, ses geri geliyordu. Sıra Alaca'ya gelince o çok alçak sesle konuştu ve ses gelmedi. Alaca başını eğdi ve üzüldü. "Gel, birlikte bağıralım, Alaca," dedi Doru. Doru ile Alaca cesaretle ve yüksek sesle kayayı selamladı. Ses hemen kayadan döndü ve ikisi güldü. "Şimdi sen dene, Alaca," dedi Doru. Alaca yüksek sesle bağırdı. Bu kez onun sesi de döndü. Sonra Alaca uslu durdu ve Doru'nun sırasını bekledi. "Sıra sende, Doru, bu oyun çok güzel!" dedi Alaca.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Alaca uslu durdu ve Doru'nun sırasını bekledi"
   - Cümle 11: «Sonra Alaca uslu durdu ve Doru'nun sırasını bekledi.»
   - Açıklama: Sorun çözüldükten sonra eklenen sıra bekleme ayrıntısı olaydan çıkmıyor ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0074` birebir aynı, `@degisim: küp -> kaya` (tutuyorsan), ardından `@onarim: 101de1f427c5be9d9ec96ac56284d7835c3e98ed`, sonra gövde.
