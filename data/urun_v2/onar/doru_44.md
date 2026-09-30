# Editör görevi (onarım): Doru, onarım partisi 44

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar44.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar44.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0073 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0073
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'ceviz', fiil 'keşfetmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: ceviz yuvarlandı ve içi boş bir kütüğe girdi | cesaretle kütüğün öbür ucundan bakıp cevizi çıkardı
@tohum: doru-0073
@degisim: keşfetmek -> bulmak
Bir sabah Doru ile Kırat geniş bir çayırda oynuyordu. Kırat bir cevizi saklıyor, Doru da onu buluyordu. Ama bu kez ceviz yuvarlandı ve içi boş bir kütüğe girdi. Kütüğün içinde hiçbir şey görünmüyordu. "Ceviz içeride kaldı, Doru," dedi Kırat. Doru önce durdu, sonra cesaretle kütüğün öbür ucuna gitti. Oradan içeri baktı ve cevizi gördü. Ceviz bu tarafa çok yakındı. Doru ağzıyla onu tuttu ve dışarı çıkardı. "Aferin, Doru, cevizi kurtardın!" dedi Kırat. Kırat bu kez cevizi çizgili bir taşın arkasına sakladı. Doru onu hemen buldu ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "geniş bir çayırda oynuyordu"
   - Cümle 1: «Bir sabah Doru ile Kırat geniş bir çayırda oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0073` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: db1595ac3a13292ce68c6dec85b3c742ee4040e3`, sonra gövde.

### Hikâye 2: tohum doru-0099 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0099
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: bir şey yapmak
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'hazine', fiil 'şekillendirmek', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: çiçeğin toprağı kuruydu çünkü dere suyu gelmiyordu | toprakta su yolu açtı ve dereye bir taş koydu
@tohum: doru-0099
@degisim: hazine -> taş
Bir sabah Doru dağda bir derenin yanında yürüyordu. Orada sarı bir çiçek gördü. Çiçeğin yaprakları aşağı eğilmişti, çünkü toprağı çok kuruydu. Dere yakından akıyordu ama suyu çiçeğe gitmiyordu. Doru çiçeğe yardım etmek istedi. Önce ayağıyla toprağı şekillendirdi ve bir su yolu açtı. Derenin kenarında düz ve ilginç bir taş vardı. Doru taşı burnuyla itti ve suyun içine koydu. Su taşa çarptı ve yeni yoldan aktı. Su çiçeğin dibine geldi ve toprak ıslandı. Çiçeğin yaprakları yavaş yavaş yukarı kalktı. Doru çiçeğe baktı ve çok sevindi. Doru bundan sonra kuru bir çiçek görünce ona su yolu açardı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ayağıyla toprağı şekillendirdi"
   - Cümle 6: «Önce ayağıyla toprağı şekillendirdi ve bir su yolu açtı.»
   - Açıklama: 'Şekillendirmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Şekillendirdi' 3 yaşındaki çocuk için soyut ve zor bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düz ve ilginç bir taş"
   - Cümle 7: «Derenin kenarında düz ve ilginç bir taş vardı.»
   - Açıklama: 'İlginç' soyut bir kelime ve taşı anlatmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0099` birebir aynı, `@degisim: hazine -> taş` (tutuyorsan), ardından `@onarim: 9f8e0235f32c0dfa839be22e61f96e7b2eae964d`, sonra gövde.

### Hikâye 3: tohum doru-0102 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0102
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'mısır', fiil 'yıkanmak', sıfat 'ahşap'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: saklanırken ıslak yelesi çalının dallarına takıldı | cesaretle arkadaşından yardım istedi
@tohum: doru-0102
@degisim: ahşap -> sarı
Rüzgar esiyordu. Doru ile Karatay ormanda saklambaç oynuyordu. Doru'nun yelesi derede yeni yıkanmıştı ve ıslaktı. Doru, mısır sarısı çiçekli bir çalının arkasına saklandı. Ama ıslak yelesi çalının dallarına takıldı. Doru başını çekti ama yelesi dallarda kaldı. Doru seslenirse oyunu Karatay kazanacaktı. Yine de Doru cesaretle seslendi. "Karatay, bana yardım eder misin?" dedi Doru. Karatay hemen çalının yanına koştu. Dalı dişleriyle tuttu ve yavaşça yana çekti. Doru başını dışarı çıkardı. İkisi birlikte güldü. "Teşekkürler, Karatay, hadi yine oynayalım!" dedi Doru.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "mısır sarısı çiçekli bir çalının"
   - Cümle 4: «Doru, mısır sarısı çiçekli bir çalının arkasına saklandı.»
   - Açıklama: 'Mısır sarısı' renk adı 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ıslak yelesi çalının dallarına takıldı"
   - Cümle 5: «Ama ıslak yelesi çalının dallarına takıldı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak beşinci cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak beşinci cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0102` birebir aynı, `@degisim: ahşap -> sarı` (tutuyorsan), ardından `@onarim: c1581172979b6ed392df0f5bf77ea7fc063018d9`, sonra gövde.

### Hikâye 4: tohum doru-0104 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0104
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'fasulye', fiil 'yapıştırmak', sıfat 'sadık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: arkadaşı çiçeklerin önündeki uzun otlardan geçemedi | önden yürüyüp otları ayırdı ve yol açtı
@tohum: doru-0104
@degisim: fasulye -> çiçek
Geniş çayırda yağmur yeni dinmişti. Doru ile Alaca uzaktaki mor çiçeklerde küçük kelebekler gördü. Ama çiçeklerin önündeki uzun otları yağmur birbirine yapıştırmıştı. "Buradan geçemiyorum, Doru," dedi Alaca. "Ben önden giderim, sen beni izle," dedi Doru. Doru'nun başı otlardan yüksekti. Doru cesaretle öne geçti ve otları iki yana itti. Sadık Alaca, Doru'nun hemen arkasından yürüdü. Az sonra ikisi mor çiçeklerin yanına çıktı. Kelebekler çiçeklerin üstünde uçuyordu. "Teşekkürler, Doru, yolu sen açtın!" dedi Alaca. Doru ile Alaca kelebekleri mutlu mutlu izledi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Geniş çayırda yağmur yeni dinmişti"
   - Cümle 1: «Geniş çayırda yağmur yeni dinmişti.»
   - Açıklama: Başlıktaki yer park iken hikaye geniş bir çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor ve park hiç anılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0104` birebir aynı, `@degisim: fasulye -> çiçek` (tutuyorsan), ardından `@onarim: aa2b7f43338740d4a9b8148c7e457e50e821f258`, sonra gövde.

### Hikâye 5: tohum doru-0106 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0106
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'ayçiçeği', fiil 'durdurmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: elma taşa çarptı ve dikenli çalılara doğru yuvarlandı | hızlıca koşup elmayı ayağıyla durdurdu
@tohum: doru-0106
@degisim: elmalı -> yuvarlak
Doru ormandaki düz ve açık bir yerde oyun oynuyordu. En sevdiği yuvarlak elmayı burnuyla bir ayçiçeğine doğru itiyordu. Birden elma bir taşa çarptı ve dikenli çalılara doğru yuvarlandı. Elma çalılara girerse Doru onu alamayacaktı. Doru düz yerde hızlıca koştu ve elmanın önüne geçti. Elmayı ayağıyla nazikçe durdurdu. Sonra Doru elmayı yine burnuyla itti. Bu kez taşın yanından dikkatle geçti. Elma sonunda ayçiçeğinin dibine vardı. Doru elmayı ayçiçeğinin yanında yedi. Doru çok sevindi, çünkü elmasını dikenlerden kurtarmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru düz yerde hızlıca koştu"
   - Cümle 5: «Doru düz yerde hızlıca koştu ve elmanın önüne geçti.»
   - Açıklama: 'Düz yer' ilk cümlede zaten söylenmişti; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0106` birebir aynı, `@degisim: elmalı -> yuvarlak` (tutuyorsan), ardından `@onarim: 6e2eb9be17c4841647d9c46283701b4f97f33b10`, sonra gövde.

### Hikâye 6: tohum doru-0110 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0110
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'tüy', fiil 'esmek', sıfat 'düz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: rüzgar esince yuvadaki tüy kayadan düşüyordu | cesaretle yuvaya gidip tüyü iki taşın arasına soktu
@tohum: doru-0110
Dağın düz bir yerinde Doru ile Kırat yuva oyunu oynuyordu. Büyük bir kayayı yuva yaptılar ve üstüne beyaz bir tüy koydular. Ama rüzgar esince tüy hep kayadan düşüyordu. "Tüy olmadan yuva olmaz, Doru," dedi Kırat. Doru tüyü ağzıyla yerden aldı. Rüzgar yüzüne esiyordu ama Doru cesaretle yuvanın yanına gitti. Tüyü kayanın yanındaki iki taşın arasına sıkıca soktu. Rüzgar yine esti ama tüy düşmedi, yalnız sallandı. "Bak, Kırat, tüy artık düşmüyor!" dedi Doru. Doru ile Kırat oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru cesaretle yuvanın yanına gitti"
   - Cümle 6: «Rüzgar yüzüne esiyordu ama Doru cesaretle yuvanın yanına gitti.»
   - Açıklama: Cesaret özelliği sorunu çözmeye yaramıyor; sorun tüyü taşların arasına sokarak çözülüyor.
   - Açıklama: Tohumdaki cesaret özelliği yalnız hafif rüzgarda yürümek için anılıyor ve sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar yüzüne esiyordu ama Doru cesaretle yuvanın yanına gitti"
   - Cümle 6: «Rüzgar yüzüne esiyordu ama Doru cesaretle yuvanın yanına gitti.»
   - Açıklama: Zaten yuvanın başında oynayan Doru'nun yanına gitmesi için cesaret gerektiren bir sebep yok; cesaret işlevsiz ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0110` birebir aynı, ardından `@onarim: 691ea2cd58c317ac078882b36f1a36fbd2357c48`, sonra gövde.

### Hikâye 7: tohum doru-0118 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0118
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'top', fiil 'yakalanmak', sıfat 'ferah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: annesi durmadan kuyruğunu sallıyordu | kuyruğa takılan ot topunu burnuyla itip çıkardı
@tohum: doru-0118
@degisim: yakalanmak -> takılmak
Çayır geniş, ferah ve serindi. Doru ile annesi çimen yiyordu. Annesi birden durmadan kuyruğunu sallamaya başladı. Doru bunu çok merak etti ve annesine yaklaştı. "Anne, neden kuyruğunu sallıyorsun?" diye sordu Doru. "Bir şey var ama göremiyorum," dedi annesi. Doru dikkatle baktı ve küçük, kuru bir ot topu gördü. Top, uzun kuyruğa sıkıca takılmıştı. "Dur, anneciğim, sana yardım edeyim," dedi Doru. Doru topu burnuyla yavaşça itti. Ot topu çıktı ve çimenlere düştü. "Teşekkürler, Doru," dedi annesi. Doru çok sevindi, çünkü annesinin neden kuyruğunu salladığını bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geniş, ferah ve serindi"
   - Cümle 1: «Çayır geniş, ferah ve serindi.»
   - Açıklama: 'Ferah' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çayır geniş, ferah ve serindi."
   - Cümle 1: «Çayır geniş, ferah ve serindi.»
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayır geniş, ferah ve serindi"
   - Cümle 1: «Çayır geniş, ferah ve serindi.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda başlıyor ve geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0118` birebir aynı, `@degisim: yakalanmak -> takılmak` (tutuyorsan), ardından `@onarim: 81690081ab5692a044f458fb55d20f1d543f9271`, sonra gövde.

### Hikâye 8: tohum doru-0120 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0120
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'palmiye', fiil 'başlamak', sıfat 'cömert'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: kuru bir ot topu annesine doğru yuvarlandı | cesaretle ot topunun yanına gidip onu uzağa itti
@tohum: doru-0120
@degisim: palmiye -> çalı
Bir sabah dağda rüzgar esmeye başladı. Doru, annesiyle birlikte bir çalının yanında çimen yiyordu. Birden kocaman, kuru bir ot topu annesine doğru yuvarlandı. Annesi şaşırdı ve geri çekildi. "Doru, bu da ne?" dedi annesi. Doru biraz korktu ama cesaretle ot topuna yaklaştı. Burnuyla ona dokundu ve kokladı. "Korkma, anne, bu yalnız kuru ot," dedi Doru. Sonra ot topunu burnuyla itti ve uzağa yuvarladı. Annesi rahatladı ve en taze çimenleri cömertçe Doru'ya bıraktı. Doru çok sevindi, çünkü annesi artık korkmuyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "en taze çimenleri cömertçe"
   - Cümle 10: «Annesi rahatladı ve en taze çimenleri cömertçe Doru'ya bıraktı.»
   - Açıklama: 'Cömertçe' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Cömertçe' soyut bir kelime ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0120` birebir aynı, `@degisim: palmiye -> çalı` (tutuyorsan), ardından `@onarim: 28b934f27fa1aa4c46eb88d08dc42872ea85c2c5`, sonra gövde.

### Hikâye 9: tohum doru-0124 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0124
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'avokado', fiil 'koklamak', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yüksekteki elmalara uzanamadı | yardım istedi ve alçak bir dal buldu
@tohum: doru-0124
@degisim: avokado -> elma
Ormanda ağaçların arasından tatlı bir koku geliyordu. Doru havayı kokladı ve bir elma ağacı buldu. Ama kırmızı elmalar çok yüksekteydi ve Doru onlara uzanamadı. Kırat yakında, kahverengi bir kütüğün yanında dinleniyordu. "Kırat, elmalar çok yüksek, onlara nasıl ulaşırım?" diye sordu Doru. "Dar yoldan geç, orada alçak bir dal var," dedi Kırat. Dar yol sık dalların arasından geçiyordu. Doru durmadı ve cesaretle dalların arasından geçti. Gerçekten de alçak bir dalda elmalar vardı. Doru bir elmayı dişleriyle koparıp yedi. Sonra bir tane de Kırat'a getirdi. Doru çok mutlu oldu, çünkü Kırat'a sormuş ve elmalara ulaşmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kırat yakında, kahverengi bir kütüğün yanında"
   - Cümle 4: «Kırat yakında, kahverengi bir kütüğün yanında dinleniyordu.»
   - Açıklama: 'Yakında' burada 'yakın bir yerde' anlamında belirsiz ve 'yanında' ile çakışıyor; 'yakında' çocuk için 'birazdan' anlamına da gelir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0124` birebir aynı, `@degisim: avokado -> elma` (tutuyorsan), ardından `@onarim: 0c5d101223ffe6d8e63a8022d97e81b69ef98c39`, sonra gövde.

### Hikâye 10: tohum doru-0126 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0126
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çuval', fiil 'tanışmak', sıfat 'pembe'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: koşarken saymayı hep unutuyordu | küçük arkadaşından saymasını istedi
@tohum: doru-0126
@degisim: çuval -> çiçek
Doru dağda, sürüyle yeni tanışan küçük Alaca ile oynuyordu. Doru uzaktaki pembe çiçeklere koşup hemen geri dönmek istiyordu. Ama koşarken saymayı hep unutuyordu ve ne kadar çabuk döndüğünü bilemiyordu. Doru biraz düşündü. "Alaca, ben koşarken sen sayar mısın?" diye sordu Doru. "Tabii, Doru!" dedi Alaca ve saymaya başladı. Doru hemen dağın düz ve açık yerinde hızla koştu. Pembe çiçeklere dokundu ve geri döndü. Alaca sekiz derken Doru onun yanına gelmişti. Doru sevinçle Alaca'ya teşekkür etti. Doru bundan sonra bir şeyi tek başına yapamayınca yardım istedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sürüyle yeni tanışan küçük Alaca"
   - Cümle 1: «Doru dağda, sürüyle yeni tanışan küçük Alaca ile oynuyordu.»
   - Açıklama: 'Sürüyle yeni tanışan' ifadesinin kimi ve neyi anlattığı belirsiz ve anlamı bulanık.
   - Açıklama: 'Sürüyle yeni tanışan' ifadesinin anlamı belirsiz ve yerinde kullanılmamış.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "sürüyle yeni tanışan küçük Alaca"
   - Cümle 1: «Doru dağda, sürüyle yeni tanışan küçük Alaca ile oynuyordu.»
   - Açıklama: Kartın yanlar alanında Alaca sürünün en küçük üyesidir; sürüyle yeni tanışan biri gibi anlatılması yanlış bilgi.
   - Açıklama: Kartın yanlar bölümünde Alaca sürünün en küçük üyesidir; sürüyle yeni tanışan biri olarak anlatılması yanlış bilgidir.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "koşarken saymayı hep unutuyordu"
   - Cümle 3: «Ama koşarken saymayı hep unutuyordu ve ne kadar çabuk döndüğünü bilemiyordu.»
   - Açıklama: Saymayı neden unuttuğu söylenmiyor ve sorun zayıf, çocuğun önemseyeceği açık bir sebebe dayanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0126` birebir aynı, `@degisim: çuval -> çiçek` (tutuyorsan), ardından `@onarim: d47bd8a3e7707e498e71ab900bf4f16623e343d4`, sonra gövde.

### Hikâye 11: tohum doru-0128 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0128
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'düğüm', fiil 'yazmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesini dinlemedi ve annesinin kuyruğu dallara takıldı | özür diledi ve düğümü dişleriyle açtı
@tohum: doru-0128
@degisim: yazmak -> çekmek
Doru annesini dinlemedi ve dağda sık çalıların arasına koştu. Annesi arkasından geldi ve uzun kuyruğu dallara takıldı. Kuyruğunda küçük bir düğüm oldu. Doru geri döndü ve annesine baktı. "Özür dilerim, anneciğim, seni dinlemeliydim," dedi Doru. "Tamam, Doru, önce bu düğümü çözelim," dedi annesi. Doru yardım etmek için dişleriyle dalları tek tek çekti. Ama dalları çekmek yeterli olmadı. Doru düğümü de yavaşça açtı. "Teşekkürler, Doru, kuyruğum kurtuldu," dedi annesi. Annesi Doru'yu burnuyla okşadı. "Bundan sonra seni hep dinleyeceğim, anneciğim," dedi Doru.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ama dalları çekmek yeterli olmadı"
   - Cümle 8: «Ama dalları çekmek yeterli olmadı.»
   - Açıklama: Çözüm özür, dalları çekme ve düğümü açma olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0128` birebir aynı, `@degisim: yazmak -> çekmek` (tutuyorsan), ardından `@onarim: 9bab38d9ffe680f964069b56701611ef836934b6`, sonra gövde.

### Hikâye 12: tohum doru-0129 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0129
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bitki', fiil 'boşaltmak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşı acıkmıştı ama sevdiği bitki burada yoktu | dağda hızla koşup bitkileri getirdi
@tohum: doru-0129
@degisim: sabırlı -> tatlı
Rüzgar dağda serin serin esiyordu. Doru ile Karatay bir ağacın altında dinleniyordu. Karatay acıkmıştı, ama sevdiği tatlı bitki burada hiç yoktu. O bitki yalnız dağın öbür yanında büyüyordu. Karatay çok yorgundu ve biraz sonra uyudu. Doru ona bir sürpriz hazırlamak istedi. Doru düz yoldan hızla dağın öbür yanına koştu. Orada tatlı bitkileri buldu ve ağzına doldurdu. Sonra aynı yoldan geri döndü. Bitkileri Karatay'ın yanındaki büyük bir taşa boşalttı. Karatay uyandı ve taşın üstündeki bitkileri gördü. Sevinçle zıpladı ve bitkilerin hepsini yedi. Doru bundan sonra Karatay acıkınca ona hep bu bitkiden getirdi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru bundan sonra Karatay acıkınca ona hep bu bitkiden getirdi"
   - Cümle 13: «Doru bundan sonra Karatay acıkınca ona hep bu bitkiden getirdi.»
   - Açıklama: Son cümle bir ders değil, hikayenin dışına uzanan bir zaman atlaması.
   - Açıklama: Son cümle bir ders değil, hikayeyi sonraki günlere taşıyan bir zaman atlaması.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0129` birebir aynı, `@degisim: sabırlı -> tatlı` (tutuyorsan), ardından `@onarim: b758c06dcaae9550137c54a5ee7f1c340fa7a8e4`, sonra gövde.
