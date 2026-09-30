# Editör görevi (onarım): Doru, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0073 (deneme 3 -> 4)

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
Bir sabah Doru ile Kırat, sürünün çimen yediği parkta oynuyordu. Kırat bir cevizi saklıyor, Doru da onu buluyordu. Ama bu kez ceviz yuvarlandı ve içi boş bir kütüğe girdi. Kütüğün içinde hiçbir şey görünmüyordu. "Ceviz içeride kaldı, Doru," dedi Kırat. Doru önce durdu, sonra cesaretle kütüğün öbür ucuna gitti. Oradan içeri baktı ve cevizi gördü. Ceviz bu tarafa çok yakındı. Doru ağzıyla onu tuttu ve dışarı çıkardı. "Aferin, Doru, cevizi yine buldun!" dedi Kırat. Kırat bu kez cevizi çizgili bir taşın arkasına sakladı. Doru onu hemen buldu ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Aferin, Doru, cevizi yine buldun"
   - Cümle 10: «"Aferin, Doru, cevizi yine buldun!" dedi Kırat.»
   - Açıklama: Cevizi Kırat bulduğu halde Kırat Doru'yu cevizi bulduğu için övüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0073` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 0f4755274571ce72b2fb13ffcb791d6bd37fddba`, sonra gövde.

### Hikâye 2: tohum doru-0099 (deneme 2 -> 3)

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
Bir sabah Doru dağda küçük bir derenin yanında yürüyordu. Derenin kenarında ince, düz ve ilginç bir taş vardı. Orada sarı bir çiçek gördü. Çiçeğin yaprakları aşağı eğilmişti, çünkü toprağı çok kuruydu. Dere yakından akıyordu ama suyu çiçeğe gitmiyordu. Doru çiçeğe yardım etmek istedi. Önce ayağıyla toprağı şekillendirdi ve küçük bir su yolu açtı. Sonra düz taşı burnuyla itti ve suyun içine koydu. Su taşa çarptı ve yeni yoldan aktı. Su çiçeğin dibine geldi ve kuru toprak ıslandı. Çiçeğin yaprakları yavaş yavaş yukarı kalktı. Doru çiçeğe baktı ve çok sevindi. Doru bundan sonra kuru bir çiçek görünce ona su yolu açtı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Orada sarı bir çiçek gördü.»
   - Açıklama: Çiçeğin toprağının kuru olduğu sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
   - Açıklama: İlk üç cümlede sorun söylenmiyor; kuru toprak ancak 4. cümlede geliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ayağıyla toprağı şekillendirdi"
   - Cümle 7: «Önce ayağıyla toprağı şekillendirdi ve küçük bir su yolu açtı.»
   - Açıklama: 'Şekillendirmek' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
   - Açıklama: 'Şekillendirmek' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "görünce ona su yolu açtı"
   - Cümle 13: «Doru bundan sonra kuru bir çiçek görünce ona su yolu açtı.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor; 'açardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0099` birebir aynı, `@degisim: hazine -> taş` (tutuyorsan), ardından `@onarim: 5533327a1ad3665cee7342010ddd36eb3122c716`, sonra gövde.

### Hikâye 3: tohum doru-0101 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0101
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'dilim', fiil 'erimek', sıfat 'işaretli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: yolda çok kalın kar vardı ve yürümek zordu | önden yürüyüp karda ayak izleri bıraktı
@tohum: doru-0101
@degisim: dilim -> kar
Doru, Kırat ile dağın karlı tepesindeydi. Biraz aşağıda kar erimişti ve yeşil çimenler çıkmıştı. Ama yolda çok kalın kar vardı. "Bu karda yürümek bana zor, Doru," dedi Kırat. Doru daha önce hiç önde gitmemişti. Yine de Kırat'a yardım etmek istedi. "Ben önde gideyim, sen de beni izle," dedi Doru. Doru güçlü ayaklarıyla yavaşça yürüdü. Arkasında derin ayak izleri kaldı. Böylece işaretli bir yol oldu. Kırat da aynı yerlere bastı ve rahatça yürüdü. Sonunda ikisi çimenlerin yanına geldi. "Teşekkürler, Doru," dedi Kırat. Doru bundan sonra karda hep önde yürüdü.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru güçlü ayaklarıyla yavaşça"
   - Cümle 8: «Doru güçlü ayaklarıyla yavaşça yürüdü.»
   - Açıklama: Tohumdaki özellik yardım; güç ikinci bir kart özelliği olarak ekleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Böylece işaretli bir yol oldu"
   - Cümle 10: «Böylece işaretli bir yol oldu.»
   - Açıklama: 'İşaretli bir yol oldu' soyut ve küçük çocuk için anlaşılması zor bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0101` birebir aynı, `@degisim: dilim -> kar` (tutuyorsan), ardından `@onarim: 3208eb85e620b784e9c9a2ae9dce002191045a89`, sonra gövde.

### Hikâye 4: tohum doru-0102 (deneme 2 -> 3)

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
@plan: saklanırken yelesi çalının dallarına takıldı | cesaretle arkadaşından yardım istedi
@tohum: doru-0102
@degisim: ahşap -> sarı
Rüzgar esiyordu. Doru ile Karatay ormanda saklambaç oynuyordu. Doru sarı çiçekli bir çalının arkasına saklandı ve yelesi dallara takıldı. Doru başını çekti ama yelesi dallarda kaldı. Karatay sesini duyunca onu bulacak ve oyunu kazanacaktı. Yine de Doru cesaretle seslendi. "Karatay, bana yardım eder misin?" dedi Doru. Karatay hemen çalının yanına koştu. Dalı dişleriyle tuttu ve yavaşça yana çekti. Doru başını dışarı çıkardı. Yelesi çiçeklerden mısır gibi sarı olmuştu. İkisi birlikte güldü. "Teşekkürler, Karatay, şimdi sığ derede yıkanalım ve yine oynayalım!" dedi Doru.
```

**Hakem bulguları (8):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Karatay sesini duyunca onu"
   - Cümle 5: «Karatay sesini duyunca onu bulacak ve oyunu kazanacaktı.»
   - Açıklama: 'Sesini' ve 'onu' zamirlerinin kimi gösterdiği açık değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Karatay sesini duyunca onu bulacak"
   - Cümle 5: «Karatay sesini duyunca onu bulacak ve oyunu kazanacaktı.»
   - Açıklama: 'sesini' zamirinin Doru'nun sesini mi Karatay'ın sesini mi gösterdiği belli değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çiçeklerden mısır gibi sarı olmuştu"
   - Cümle 11: «Yelesi çiçeklerden mısır gibi sarı olmuştu.»
   - Açıklama: Benzetme ve olağan dışı anlatım küçük çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çiçeklerden mısır gibi sarı"
   - Cümle 11: «Yelesi çiçeklerden mısır gibi sarı olmuştu.»
   - Açıklama: 'mısır gibi sarı' benzetmesi 3 yaşındaki çocuk için mecazlı ve anlaşılması zor.
5. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Yelesi çiçeklerden mısır gibi sarı"
   - Cümle 11: «Yelesi çiçeklerden mısır gibi sarı olmuştu.»
   - Açıklama: Mısır kartın özgür at sürüsü doğa dünyasında olmayan bir çiftlik ürünü.
6. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Yelesi çiçeklerden mısır gibi sarı olmuştu"
   - Cümle 11: «Yelesi çiçeklerden mısır gibi sarı olmuştu.»
   - Açıklama: Takılma çözüldükten sonra yelenin sararması yeni bir sorun açıyor ve yıkanma gerektiriyor.
   - Açıklama: Sorun çözüldükten sonra yelenin sararması ikinci bir sorun açıyor ve hikaye içinde çözülmüyor.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "şimdi sığ derede yıkanalım"
   - Cümle 13: «"Teşekkürler, Karatay, şimdi sığ derede yıkanalım ve yine oynayalım!" dedi Doru.»
   - Açıklama: Son cümle suya girip yıkanmayı özendiriyor; çocuk taklit ederse su tehlikesi doğabilir.
   - Açıklama: Derede yıkanmaya çağrı çocuğun taklit edebileceği su kenarı davranışı.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şimdi sığ derede yıkanalım"
   - Cümle 13: «"Teşekkürler, Karatay, şimdi sığ derede yıkanalım ve yine oynayalım!" dedi Doru.»
   - Açıklama: 'Sığ' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0102` birebir aynı, `@degisim: ahşap -> sarı` (tutuyorsan), ardından `@onarim: 796c27a93cf6a529f2b7076a146035d6022db854`, sonra gövde.

### Hikâye 5: tohum doru-0104 (deneme 2 -> 3)

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
@plan: çiçeklerin önündeki uzun otlardan geçemedi | önden yürüyüp otları ayırdı ve yol açtı
@tohum: doru-0104
@degisim: sadık -> uzun
Parkta yağmur yeni dinmişti. Doru ile Alaca uzaktaki mor çiçeklerde fasulye kadar küçük kelebekler gördü. Ama çiçeklerin önündeki uzun otları yağmur birbirine yapıştırmıştı. "Buradan geçemiyorum, Doru," dedi Alaca. "Ben önden giderim, sen beni izle," dedi Doru. Doru'nun başı otlardan yüksekti. Doru cesaretle öne geçti ve otları iki yana itti. Alaca, Doru'nun açtığı yoldan yürüdü. Az sonra ikisi mor çiçeklerin yanına çıktı. Kelebekler çiçeklerin üstünde uçuyordu. "Teşekkürler, Doru, yolu sen açtın!" dedi Alaca. Doru ile Alaca kelebekleri izleyerek çimen yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çiçeklerin önündeki uzun otlardan geçemedi"
   - Cümle 0 (plan satırı): «çiçeklerin önündeki uzun otlardan geçemedi | önden yürüyüp otları ayırdı ve yol açtı»
   - Açıklama: Plan figürün geçemediğini söylüyor ama gövdede otlardan geçemeyen Alaca.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "fasulye kadar küçük kelebekler"
   - Cümle 2: «Doru ile Alaca uzaktaki mor çiçeklerde fasulye kadar küçük kelebekler gördü.»
   - Açıklama: Fasulye özgür at sürüsü dünyasında olmayan bir mutfak öğesidir.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çimen yemeye mutlu mutlu devam etti"
   - Cümle 12: «Doru ile Alaca kelebekleri izleyerek çimen yemeye mutlu mutlu devam etti.»
   - Açıklama: Daha önce çimen yedikleri anlatılmadığı için 'devam etti' yanlış anlamda kullanılmış.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çimen yemeye mutlu mutlu devam etti"
   - Cümle 12: «Doru ile Alaca kelebekleri izleyerek çimen yemeye mutlu mutlu devam etti.»
   - Açıklama: Doru ile Alaca daha önce çimen yemiyordu ama yemeye devam ettikleri söyleniyor.
   - Açıklama: Hikayede daha önce çimen yenmediği halde çimen yemeye devam ettikleri söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0104` birebir aynı, `@degisim: sadık -> uzun` (tutuyorsan), ardından `@onarim: c2bce5f74924f9b8c0c386bb4648107fc4a2a5cc`, sonra gövde.

### Hikâye 6: tohum doru-0106 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: elma bir köke çarptı ve dereye doğru yuvarlandı | hızla koşup elmayı ayağıyla durdurdu
@tohum: doru-0106
@degisim: elmalı -> yuvarlak
Doru ormandaki düz bir açıklıkta en sevdiği oyunu oynuyordu. Yuvarlak bir elmayı burnuyla bir ayçiçeğine doğru itiyordu. Birden elma bir köke çarptı ve küçük bir dereye doğru yuvarlandı. Elma suya düşerse Doru onu bir daha bulamazdı. Doru hızla koştu ve elmanın önüne geçti. Elmayı ayağıyla nazikçe durdurdu. Sonra Doru elmayı yine burnuyla itti. Bu kez köklerin yanından dikkatle geçti. Elma sonunda ayçiçeğinin dibine vardı. Doru çok sevindi, çünkü elma suya düşmedi ve oyun bitti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "elma bir köke çarptı"
   - Cümle 3: «Birden elma bir köke çarptı ve küçük bir dereye doğru yuvarlandı.»
   - Açıklama: Elma yuvarlanıyor, Doru onu tek hamlede durduruyor ve olay bitiyor; sorun önemsiz bir olay olarak kalıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru hızla koştu ve elmanın önüne geçti"
   - Cümle 5: «Doru hızla koştu ve elmanın önüne geçti.»
   - Açıklama: Dereye yuvarlanan nesnenin peşinden suya doğru koşmak çocuğun taklit edebileceği tehlikeli bir davranış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elma suya düşmedi ve oyun bitti"
   - Cümle 10: «Doru çok sevindi, çünkü elma suya düşmedi ve oyun bitti.»
   - Açıklama: Sevinmenin nedeni olarak 'oyun bitti' yanlış anlam veriyor; kastedilen oyunu başarıyla tamamlamak.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0106` birebir aynı, `@degisim: elmalı -> yuvarlak` (tutuyorsan), ardından `@onarim: b95e4e933ee69c8f87606a8f2bc12c6b763a592b`, sonra gövde.

### Hikâye 7: tohum doru-0108 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0108
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'halka', fiil 'ödemek', sıfat 'kokulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşı acıkmıştı ama dağda otlar kuru ve sertti | arkadaşını vadideki kokulu çimenlere götürdü
@tohum: doru-0108
@degisim: öde- -> doy-
Rüzgar dağda serin serin esiyordu. Doru ile Karatay kayaların arasında yürüyordu. Karatay çok acıkmıştı, ama buradaki otlar kuru ve sertti. "Doru, bu otları yiyemiyorum," dedi Karatay. Doru aşağıdaki vadide kokulu çimenler olduğunu hatırladı. "Benimle gel, Karatay, orada yumuşak çimenler var," dedi Doru. Doru arkadaşına yardım etti ve önden yavaşça yürüdü. Karatay da onun arkasından geldi. Vadide büyük bir kayanın çevresinde halka gibi çimenler vardı. Karatay çimenleri yedi ve sonunda doydu. Doru onun yanında sevinçle bekledi. "Teşekkürler, Doru, karnım artık tok!" dedi Karatay.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru aşağıdaki vadide kokulu çimenler olduğunu hatırladı"
   - Cümle 5: «Doru aşağıdaki vadide kokulu çimenler olduğunu hatırladı.»
   - Açıklama: Hikaye dağdaki kayalarda başlıyor ve aşağıdaki vadiye taşınarak sahne değiştiriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "halka gibi çimenler vardı"
   - Cümle 9: «Vadide büyük bir kayanın çevresinde halka gibi çimenler vardı.»
   - Açıklama: 'Halka gibi' benzetmesi küçük çocuk için soyut bir mecaz.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Vadide büyük bir kayanın çevresinde"
   - Cümle 9: «Vadide büyük bir kayanın çevresinde halka gibi çimenler vardı.»
   - Açıklama: Hikaye dağdaki kayalıkta başlıyor ama aşağıdaki vadiye geçip orada bitiyor; tek sahne kuralı çiğneniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0108` birebir aynı, `@degisim: öde- -> doy-` (tutuyorsan), ardından `@onarim: 07d0db4caddf0fae3e640709e94fd28bc327e7dd`, sonra gövde.

### Hikâye 8: tohum doru-0109 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0109
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'fındık', fiil 'kutlamak', sıfat 'taze'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: arkadaşı fındık ararken ormanda kayboldu | sesin geldiği yere hızla koşup onu buldu
@tohum: doru-0109
@degisim: kutla- -> seslen-
Ormanda fındık ağaçları vardı ve yerde taze fındıklar duruyordu. Doru ile Karatay fındık yiyordu. Karatay fındık ararken çok uzağa gitti ve kayboldu. "Doru, neredesin?" diye seslendi Karatay. Ses uzaktan, ormanın öbür ucundan geliyordu. Doru önündeki düz ve açık yola baktı. Sonra bu yolda hızla koştu. Az sonra Karatay'ı büyük bir kayanın yanında buldu. "Buradayım, Karatay!" dedi Doru. "Ne kadar çabuk geldin!" dedi Karatay sevinçle. Doru onu fındıkların yanına geri götürdü. İkisi taze fındıkları birlikte yedi. Karatay bundan sonra ormanda Doru'dan hiç uzaklaşmadı.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "çok uzağa gitti ve kayboldu"
   - Cümle 3: «Karatay fındık ararken çok uzağa gitti ve kayboldu.»
   - Açıklama: Ormanda kaybolan arkadaş küçük çocuk için korkutucu bir öğe.
   - Açıklama: Arkadaşın ormanda kaybolması küçük çocuk için korkutucu bir öğe.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0109` birebir aynı, `@degisim: kutla- -> seslen-` (tutuyorsan), ardından `@onarim: 9beb5823ecd42d7aec7f3306337049bee9ef24c9`, sonra gövde.

### Hikâye 9: tohum doru-0110 (deneme 2 -> 3)

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
@plan: rüzgar esince bayrak olan tüy kayadan düşüyordu | tüyü iki taşın arasına sıkıca soktu
@tohum: doru-0110
Dağın düz tepesinde Doru ile Kırat gemi oyunu oynuyordu. Büyük bir kaya gemi oldu, beyaz bir tüy de bayrak oldu. Ama rüzgar esince tüy hep kayadan düşüyordu. "Bayrak olmadan oyun olmaz, Doru," dedi Kırat. Doru tüyü ağzıyla yerden aldı. Rüzgar çok sertti ama Doru cesaretle kayanın yanında kaldı. Tüyü kayanın yanındaki iki taşın arasına sıkıca soktu. Rüzgar yine esti ama tüy düşmedi, yalnız sallandı. "Bak Kırat, bayrak artık düşmüyor!" dedi Doru. Doru ile Kırat oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Doru ile Kırat gemi oyunu oynuyordu"
   - Cümle 1: «Dağın düz tepesinde Doru ile Kırat gemi oyunu oynuyordu.»
   - Açıklama: Kapalı doğa dünyasında gemi ve bayrak gibi kartta olmayan nesneler oyuna giriyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kırat gemi oyunu oynuyordu"
   - Cümle 1: «Dağın düz tepesinde Doru ile Kırat gemi oyunu oynuyordu.»
   - Açıklama: Gemi kartın doğa dünyasında olmayan bir eşya ve kapalı dünyaya aykırı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Rüzgar çok sertti ama Doru cesaretle kayanın yanında kaldı"
   - Cümle 6: «Rüzgar çok sertti ama Doru cesaretle kayanın yanında kaldı.»
   - Açıklama: Tohumdaki cesaret özelliği sorunu çözmüyor; çözüm tüyü taşların arasına sokmak.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0110` birebir aynı, ardından `@onarim: dfd87416c1be3580f8c2087ef4319de92d3b8702`, sonra gövde.

### Hikâye 10: tohum doru-0112 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0112
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'lokma', fiil 'yetişmek', sıfat 'akıllı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: ikisi de acıkmıştı ve tek bir elma kalmıştı | hızla koşup elmayı getirdi ve annesiyle paylaştı
@tohum: doru-0112
@degisim: akıllı -> kırmızı
Bir sabah Doru ile annesi dağda uzun bir yol yürüdü. İkisi de çok acıkmıştı ama orada hiç çimen yoktu. Doru vadinin öbür ucunda bir elma ağacı gördü. Ağaçta tek bir kırmızı elma kalmıştı. Annesi uzun yoldan çok yorulmuştu. "Anne, sen burada dinlen, ben elmayı getiririm," dedi Doru. Doru düz vadide hızla koştu ve ağaca yetişti. Elmayı daldan ağzıyla kopardı. Sonra elmayı annesine getirdi. "Bu elma ikimize de yeter," dedi Doru. Önce annesi küçük bir lokma aldı, sonra Doru. "Çok teşekkür ederim, Doru," dedi annesi. Doru çok mutluydu, çünkü elmayı annesiyle paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "vadinin öbür ucunda"
   - Cümle 3: «Doru vadinin öbür ucunda bir elma ağacı gördü.»
   - Açıklama: 'Vadi' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "koştu ve ağaca yetişti"
   - Cümle 7: «Doru düz vadide hızla koştu ve ağaca yetişti.»
   - Açıklama: 'Yetişmek' burada yanlış anlamda; ağaca 'vardı' ya da 'ulaştı' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ağaca yetişti"
   - Cümle 7: «Doru düz vadide hızla koştu ve ağaca yetişti.»
   - Açıklama: 'Yetişmek' hareket eden bir şeye yetişmek içindir; ağaç için 'ağaca ulaştı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0112` birebir aynı, `@degisim: akıllı -> kırmızı` (tutuyorsan), ardından `@onarim: fc40bb4e47db793f2e550d0b9564446c7c02670c`, sonra gövde.

### Hikâye 11: tohum doru-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0114
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'delik', fiil 'düzelmek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: sık ağaçlar yüzünden ıslak sırtına güneş gelmiyordu | cesaretle dar yoldan geçip güneşli bir yere çıktı
@tohum: doru-0114
@degisim: saygılı -> dar
Yağmur durdu ve hava yavaş yavaş düzeldi. Ama Doru'nun durduğu yerde ağaçlar çok sıktı ve güneş gelmiyordu. Doru'nun sırtı ıslaktı ve Doru güneşe çıkmak istedi. Yukarıdaki yapraklarda küçük bir delik vardı. Delikten, uzakta parlak bir ışık görünüyordu. Oraya ağaçların arasından dar bir yol gidiyordu. Doru bu yolu hiç bilmiyordu. Yolun iki yanında uzun çalılar sallanıyordu. Doru bir an bekledi, sonra cesaretle ilerledi. Çalıların arasından geçti ve sonunda geniş, açık bir yere çıktı. Orada güneş her yeri ısıtıyordu. Doru güneşte durdu ve sırtı kurudu. Doru çok sevindi, çünkü artık sıcacık ve kuruydu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yukarıdaki yapraklarda küçük bir delik vardı"
   - Cümle 4: «Yukarıdaki yapraklarda küçük bir delik vardı.»
   - Açıklama: Yukarıdaki yapraklardaki delikten uzaktaki yerin görünmesi akla yatmıyor ve yolu sebepsizce getiriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru bu yolu hiç bilmiyordu"
   - Cümle 7: «Doru bu yolu hiç bilmiyordu.»
   - Açıklama: Figür yalnız başına bilmediği karanlık bir yola giriyor; taklit edilince tehlikeli.
   - Açıklama: Tek başına bilinmeyen dar yola girmek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0114` birebir aynı, `@degisim: saygılı -> dar` (tutuyorsan), ardından `@onarim: fa092ece23d77d67d58c5f0d3ece7014a88d6af4`, sonra gövde.

### Hikâye 12: tohum doru-0118 (deneme 2 -> 3)

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
@degisim: ferah -> geniş
Park geniş ve serindi. Doru ile annesi çimen yiyordu. Annesi birden durmadan kuyruğunu sallamaya başladı. Doru bunu çok merak etti ve annesine yaklaştı. "Anne, neden kuyruğunu sallıyorsun?" diye sordu Doru. "Bir şey var ama göremiyorum," dedi annesi. Doru dikkatle baktı ve küçük, kuru bir ot topu gördü. Top, uzun kuyruğa sıkıca yakalanmıştı. "Dur, anneciğim, sana yardım edeyim," dedi Doru. Doru topu burnuyla yavaşça itti. Ot topu çıktı ve çimenlere düştü. "Teşekkürler, Doru," dedi annesi. Doru çok sevindi, çünkü annesinin neden kuyruğunu salladığını bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzun kuyruğa sıkıca yakalanmıştı"
   - Cümle 8: «Top, uzun kuyruğa sıkıca yakalanmıştı.»
   - Açıklama: Top yakalanmaz; 'takılmıştı' olmalı.
   - Açıklama: Top kuyruğa yakalanmaz, takılır; fiil yanlış anlamda.
   - Açıklama: Ot topu kuyruğa yakalanmaz, takılır; fiil yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0118` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 92bcaa6062cdecb13e4a081e0dc62bfdb98ccf2e`, sonra gövde.
