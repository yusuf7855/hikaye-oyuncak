# Editör görevi (onarım): Doru, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0033 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: oyuna katılmak istedi ama sormaya utandı | cesaretle yanına gidip sıra istedi ve sırayla oynadılar
@tohum: doru-0033
@degisim: çalışkan -> uzun
Bir sabah Doru dağda Kırat'ı izliyordu. Kırat ağaç kabuğundan uzun bir şeridi havaya atıp yakalıyordu. Doru da oynamak istedi, ama sürünün en büyüğüne sormaya utandı. Doru cesaretle Kırat'ın yanına gitti. Başını eğdi ve ondan bir sıra istedi. Kırat başını salladı ve şeridi Doru'ya attı. Doru zıpladı ve şeridi dişleriyle yakaladı. Sonra şeridi Kırat'a geri attı. Bu kez Kırat onu ağzıyla tuttu. İkisi sırayla oynamaya devam etti. Doru çok sevindi, çünkü sonunda o da Kırat'la oynuyordu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sürünün en büyüğüne sormaya"
   - Cümle 3: «Doru da oynamak istedi, ama sürünün en büyüğüne sormaya utandı.»
   - Açıklama: Daha önce anılmayan 'sürünün en büyüğü' ifadesinin Kırat olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0033` birebir aynı, `@degisim: çalışkan -> uzun` (tutuyorsan), ardından `@onarim: 63298207830143210ac777ebf849ae3358c2c703`, sonra gövde.

### Hikâye 2: tohum doru-0099 (deneme 1 -> 2)

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
@plan: çiçeğin toprağı kuruydu çünkü dere suyu gelmiyordu | toprağı şekillendirip taşla suyu çiçeğe çevirdi
@tohum: doru-0099
@degisim: hazine -> taş
Bir sabah Doru dağda küçük bir derenin yanında yürüyordu. Orada sarı bir çiçek gördü. Çiçeğin yaprakları aşağı eğilmişti, çünkü toprağı çok kuruydu. Dere yakından akıyordu ama suyu çiçeğe gitmiyordu. Doru çiçeğe yardım etmek istedi. Önce ayağıyla toprağı kazdı ve küçük bir su yolu şekillendirdi. Sonra yerde ilginç bir taş buldu. Taş ince ve düzdü. Doru taşı burnuyla itti ve derenin kenarına koydu. Düz taş suyu yeni yola çevirdi. Su aktı ve çiçeğin dibine geldi. Kuru toprak ıslandı. Çiçeğin yaprakları yavaş yavaş yukarı kalktı. Doru çiçeğe baktı ve çok sevindi. Doru bundan sonra kuru bir çiçek görünce ona su yolu açtı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "taşla suyu çiçeğe çevirdi"
   - Cümle 0 (plan satırı): «çiçeğin toprağı kuruydu çünkü dere suyu gelmiyordu | toprağı şekillendirip taşla suyu çiçeğe çevirdi»
   - Açıklama: 'Suyu çiçeğe çevirdi' suyu çiçeğe dönüştürmek anlamına da gelir; 'çiçeğe doğru yönlendirdi' kastediliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük bir su yolu şekillendirdi"
   - Cümle 6: «Önce ayağıyla toprağı kazdı ve küçük bir su yolu şekillendirdi.»
   - Açıklama: Yol şekillendirilmez, açılır ya da kazılır; kelime yanlış ve çocuğa ağır.
   - Açıklama: Su yolu şekillendirilmez, kazılır ya da açılır; fiil uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yerde ilginç bir taş"
   - Cümle 7: «Sonra yerde ilginç bir taş buldu.»
   - Açıklama: 'İlginç' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yerde ilginç bir taş buldu"
   - Cümle 7: «Sonra yerde ilginç bir taş buldu.»
   - Açıklama: Çözümü getiren taş önceden kurulmadan sebepsizce ve tam gerektiği anda beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0099` birebir aynı, `@degisim: hazine -> taş` (tutuyorsan), ardından `@onarim: 93e7af30dc76c96945cf9e640af52696973e3751`, sonra gövde.

### Hikâye 3: tohum doru-0101 (deneme 1 -> 2)

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
Doru, Kırat ile dağın karlı tepesindeydi. Sürü aşağıda, vadide çimen yiyordu. Ama yolda çok kalın kar vardı. "Bu karda yürümek bana zor, Doru," dedi Kırat. Doru karda daha önce hiç önde gitmemişti. Yine de Kırat'a yardım etmek istedi. "Ben önde gideyim, sen de beni izle," dedi Doru. Doru güçlü ayaklarıyla karda yürüdü. Karda derin ayak izleri kaldı. Böylece kar üstünde işaretli bir yol oldu. Kırat da aynı yerlere bastı ve rahatça yürüdü. Sonunda ikisi vadiye indi. Vadide kar erimişti ve çimenler yemyeşildi. "Teşekkürler, Doru," dedi Kırat. Doru bundan sonra karda hep önde yürüdü.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sürü aşağıda, vadide çimen"
   - Cümle 2: «Sürü aşağıda, vadide çimen yiyordu.»
   - Açıklama: Belirsiz kelime 'sürü' cansız anlamda değil, canlı at sürüsü olarak geçiyor; kullanıcı kararı bunu yasaklıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru güçlü ayaklarıyla karda yürüdü. Karda derin ayak izleri"
   - Cümle 8: «Doru güçlü ayaklarıyla karda yürüdü.»
   - Açıklama: 'karda' kelimesi art arda cümlelerde ve hikaye boyunca gereksizce tekrarlanıyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sonunda ikisi vadiye indi"
   - Cümle 12: «Sonunda ikisi vadiye indi.»
   - Açıklama: Hikaye dağın karlı tepesinde başlıyor ama vadide, başka bir yerde bitiyor.
   - Açıklama: Hikaye dağın karlı tepesinde başlıyor ama vadide bitiyor; sahne değişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0101` birebir aynı, `@degisim: dilim -> kar` (tutuyorsan), ardından `@onarim: 8e465c28e2253ede0438b3042357050207e1e7f0`, sonra gövde.

### Hikâye 4: tohum doru-0102 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: çiçek tozu sırtına yapıştı ve sırtı sarı oldu | derede arkadaşından sırtına su atmasını istedi
@tohum: doru-0102
@degisim: ahşap -> sarı
Rüzgar esiyordu. Doru ile Karatay ormandaki çiçeklerin arasında koşuyordu. Çiçeklerin tozu Doru'nun sırtına yapıştı ve sırtı mısır gibi sarı oldu. Doru bu tozdan kurtulmak için yıkanmak istedi. İkisi küçük bir dereye gitti. Su çok soğuktu ama Doru cesaretle suya girdi. Ama ağzıyla sırtına su atamıyordu. "Karatay, sırtıma su atar mısın?" diye sordu Doru. Karatay da ayağıyla suya vurdu. Su Doru'nun sırtına sıçradı. Karatay güldü ve bunu üç kez yaptı. Sarı toz sırtından yavaş yavaş gitti. Doru'nun sırtı yine kahverengi oldu. "Teşekkürler, Karatay, artık hiç toz yok!" dedi Doru.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sırtı mısır gibi sarı oldu"
   - Cümle 3: «Çiçeklerin tozu Doru'nun sırtına yapıştı ve sırtı mısır gibi sarı oldu.»
   - Açıklama: Sırtın çiçek tozuyla sararması çocuğun önemseyeceği gerçek bir sorun değil, zararsız ve önemsiz bir olay.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Su çok soğuktu ama Doru cesaretle suya girdi"
   - Cümle 6: «Su çok soğuktu ama Doru cesaretle suya girdi.»
   - Açıklama: Çok soğuk dere suyuna girmek cesaret olarak övülüyor ve çocuk taklit edebilir.
   - Açıklama: Soğuk dere suyuna cesaretle girmek çocuğun taklit edebileceği tehlikeli bir davranış ve güvenli özellik kullanımı satırının dışında.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Karatay da ayağıyla suya vurdu"
   - Cümle 9: «Karatay da ayağıyla suya vurdu.»
   - Açıklama: 'da' bağlacı yanlış anlamda; Karatay'dan önce suya vuran kimse yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0102` birebir aynı, `@degisim: ahşap -> sarı` (tutuyorsan), ardından `@onarim: 00d0d4c6b7f7ab35d706984dd5cf16509e549aaa`, sonra gövde.

### Hikâye 5: tohum doru-0103 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0103
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'elma', fiil 'şaşırmak', sıfat 'patlak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: elma ağacı uzaktaydı ve sürü gitmek üzereydi | düz çimende koşup elmayı getirdi
@tohum: doru-0103
@degisim: patlak -> kırmızı
Dağın düz tepesinde Doru ile Kırat otluyordu. Doru daha önce hiç elma yememişti ve çok merak ediyordu. Ama elma ağacı uzaktaydı ve sürü birazdan vadiye gidiyordu. "Sürü gitmeden dönmelisin, Doru," dedi Kırat. Doru düz çimenin üstünden hızla koştu. Ağacın altında kırmızı bir elma buldu. Elmayı ağzına aldı ve Kırat'ın yanına geri döndü. Elmayı bir taşın üstüne koydu ve bir ısırık aldı. Doru elmanın tatlı tadına çok şaşırdı. Sonra elmanın kalanını Kırat'a verdi. "Kırat, elma çok tatlıymış, sen de ye!" dedi Doru.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Doru düz çimenin üstünden hızla koştu"
   - Cümle 5: «Doru düz çimenin üstünden hızla koştu.»
   - Açıklama: Ağacın uzak olması gerçek bir engel değil; Doru yalnızca koşup elmayı alıyor ve sürünün gitmesi bir daha hiç önem kazanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0103` birebir aynı, `@degisim: patlak -> kırmızı` (tutuyorsan), ardından `@onarim: dd2b84825a12f9e63d6481e3318cc5a23547d925`, sonra gövde.

### Hikâye 6: tohum doru-0104 (deneme 1 -> 2)

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
@plan: çiçeklerin önünde çok uzun otlar vardı | önden otlara girip yavruya yol açtı
@tohum: doru-0104
@degisim: fasulye -> yağmur
Çayırda yağmur yeni dinmişti. Doru ile Alaca uzaktaki mor çiçeklerde kelebekler gördü. Ama çiçeklerin önünde Alaca'nın başından yüksek otlar vardı. "Otların içinde yolu göremiyorum, Doru," dedi Alaca. "Ben önden giderim, sen beni izle," dedi Doru. Doru cesaretle uzun otların içine girdi. Alaca burnunu Doru'nun kuyruğuna yapıştırdı. Sonra onun arkasından yürüdü. Az sonra ikisi mor çiçeklerin yanına çıktı. Kelebekler çiçeklerin üstünde uçuyordu. "Beni hiç bırakmadın, sen sadık bir dostsun," dedi Alaca. Doru ile Alaca kelebekleri izleyerek çimen yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda yağmur yeni dinmişti"
   - Cümle 1: «Çayırda yağmur yeni dinmişti.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve geçiyor.
   - Açıklama: Başlıktaki yer park olduğu halde hikaye çayırda geçiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle uzun otların içine girdi"
   - Cümle 6: «Doru cesaretle uzun otların içine girdi.»
   - Açıklama: Baştan yüksek, içi görünmeyen otlara girmek cesaret olarak övülüyor ve çocuk için taklit edilince tehlikeli olabilir.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "burnunu Doru'nun kuyruğuna yapıştırdı"
   - Cümle 7: «Alaca burnunu Doru'nun kuyruğuna yapıştırdı.»
   - Açıklama: 'Yapıştırdı' burada yanlış anlamda; 'dayadı' ya da 'yaklaştırdı' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen sadık bir dostsun"
   - Cümle 11: «"Beni hiç bırakmadın, sen sadık bir dostsun," dedi Alaca.»
   - Açıklama: Tohumdaki özellik cesaret; kartın özellikler alanında olmayan sadakat ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik cesaret; sadakat ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0104` birebir aynı, `@degisim: fasulye -> yağmur` (tutuyorsan), ardından `@onarim: 159f6e7821e4321018359f533188f146671cb4d6`, sonra gövde.

### Hikâye 7: tohum doru-0105 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0105
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'halat', fiil 'tekrarlamak', sıfat 'çilekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: annesi çilek kokusunu aldı ama yeri bulamadı | uzun otlara girip çilekleri buldu ve annesine seslendi
@tohum: doru-0105
@degisim: halat -> ot
Doru annesiyle geniş çayırda çimen yiyordu. Annesi burnunu kaldırdı ve çilek kokusunu aldı. Ama koku uzun ve sık otların arasından geliyordu ve annesi yeri bulamadı. "Otların içi çok karanlık, Doru," dedi annesi. Doru cesaretle otların arasına girdi. Biraz yürüdü ve çilekli küçük bir yer buldu. "Anne, buradayım, çilekler burada!" diye seslendi Doru. Bu sözleri birkaç kez tekrarladı. Annesi sesin geldiği yere doğru yürüdü. Sonunda Doru'nun yanına vardı. Kırmızı çilekleri görünce çok sevindi. İkisi birlikte çilek yedi. "Teşekkürler, Doru, bu çilekler çok tatlı!" dedi annesi.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru annesiyle geniş çayırda çimen yiyordu"
   - Cümle 1: «Doru annesiyle geniş çayırda çimen yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda başlıyor ve orada geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve annesi yeri bulamadı"
   - Cümle 3: «Ama koku uzun ve sık otların arasından geliyordu ve annesi yeri bulamadı.»
   - Açıklama: 'Yeri' neyin yeri olduğu belirtilmeden kullanılmış; 'kokunun geldiği yeri' olmalı.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Otların içi çok karanlık"
   - Cümle 4: «"Otların içi çok karanlık, Doru," dedi annesi.»
   - Açıklama: Doru'nun annesinden ayrılıp girdiği otlar karanlık ve korkutucu olarak tarif ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0105` birebir aynı, `@degisim: halat -> ot` (tutuyorsan), ardından `@onarim: 08fd71dad98d0a51817b8dcecab895b615967b2d`, sonra gövde.

### Hikâye 8: tohum doru-0106 (deneme 1 -> 2)

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
@plan: elma bir köke çarptı ve çalılara doğru yuvarlandı | hızla koşup elmayı ayağıyla durdurdu
@tohum: doru-0106
@degisim: elmalı -> yuvarlak
Doru ormandaki düz bir açıklıkta tek başına oynuyordu. Ağaçtan düşmüş yuvarlak bir elmayı burnuyla bir ayçiçeğine doğru itiyordu. Bu onun en sevdiği oyundu. Birden elma bir köke çarptı ve yana döndü. Elma dikenli çalılara doğru yuvarlanmaya başladı. Doru elmanın çalılara girmesini istemedi. Hızla koştu ve elmanın önüne geçti. Elmayı ayağıyla nazikçe durdurdu. Sonra elmayı yine burnuyla itti. Bu kez yavaş yavaş ve dikkatle itti. Elma sonunda ayçiçeğinin dibinde durdu. Doru çok sevindi, çünkü elmayı kaybetmeden oyununu bitirmişti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Bu onun en sevdiği oyundu.»
   - Açıklama: Sorun ancak 4. ve 5. cümlede, elma köke çarpıp çalılara yuvarlanınca söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elma dikenli çalılara doğru yuvarlanmaya başladı"
   - Cümle 5: «Elma dikenli çalılara doğru yuvarlanmaya başladı.»
   - Açıklama: Sorun önemsiz bir an ve Doru elmayı hemen durdurunca bitiyor; çocuğu önemsetecek bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0106` birebir aynı, `@degisim: elmalı -> yuvarlak` (tutuyorsan), ardından `@onarim: 1e004bc92c928aa55e2146a31ab999d7df3be7ae`, sonra gövde.

### Hikâye 9: tohum doru-0107 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0107
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çilek', fiil 'süslemek', sıfat 'düzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: ormanda tık tık diye bir ses geldi | hızla koşup sesi yapan dalı buldu
@tohum: doru-0107
@degisim: süslemek -> izlemek
Rüzgar esiyordu ve ormanda tık tık diye bir ses geliyordu. Doru bir ağacın altında çilek yiyordu. Bu sesin nereden geldiğini çok merak etti. Ses bazen duruyor, sonra yine başlıyordu. Doru, ses durmadan yerini bulmak istedi. Ağaçların arasındaki düz yoldan hızla koştu. Ses büyük bir ağaçtan geliyordu. Ağacın kuru bir dalı rüzgarda sallanıyordu. Rüzgar esince dal ağaca vuruyordu. Tık tık sesini bu dal yapıyordu. Dal ağaca hep aynı yerden, düzgün vuruyordu. Doru ağacın dibinde de çilekler buldu. Sallanan dalı izleyerek çilek yemeye mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ormanda tık tık diye bir ses geldi"
   - Cümle 1: «Rüzgar esiyordu ve ormanda tık tık diye bir ses geliyordu.»
   - Açıklama: Bir sesin duyulması çocuğun önemseyeceği gerçek bir sorun değil, yalnız bir merak konusu.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ormanda tık tık diye bir ses geliyordu"
   - Cümle 1: «Rüzgar esiyordu ve ormanda tık tık diye bir ses geliyordu.»
   - Açıklama: Sorun yalnız bir sesin merakı; çocuğun önemseyeceği gerçek bir sorun yok.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aynı yerden, düzgün vuruyordu"
   - Cümle 11: «Dal ağaca hep aynı yerden, düzgün vuruyordu.»
   - Açıklama: 'Düzgün' burada yanlış anlamda; 'düzenli' olmalı.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Dal ağaca hep aynı yerden, düzgün vuruyordu"
   - Cümle 11: «Dal ağaca hep aynı yerden, düzgün vuruyordu.»
   - Açıklama: Dalın ağaca vurduğu 9. ve 10. cümlelerden sonra yeniden anlatılıyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Dal ağaca hep aynı yerden"
   - Cümle 11: «Dal ağaca hep aynı yerden, düzgün vuruyordu.»
   - Açıklama: Dalın ağaca vurduğu önceki cümlelerde zaten söylenmişti; gereksiz tekrar.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dal ağaca hep aynı yerden, düzgün vuruyordu"
   - Cümle 11: «Dal ağaca hep aynı yerden, düzgün vuruyordu.»
   - Açıklama: Bu ayrıntı olayda hiçbir işe yaramıyor.
   - Açıklama: Bu ayrıntı ve sonradan beliren çilekler olayda hiçbir işe yaramıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru ağacın dibinde de çilekler buldu"
   - Cümle 12: «Doru ağacın dibinde de çilekler buldu.»
   - Açıklama: Çilekler sebepsiz beliriyor ve sorunla ilgisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0107` birebir aynı, `@degisim: süslemek -> izlemek` (tutuyorsan), ardından `@onarim: c08c1e1613094fcf805a5eea70f3e552c05350cf`, sonra gövde.

### Hikâye 10: tohum doru-0110 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar en büyük tüyü iki kayanın arasına uçurdu | cesaretle başını uzatıp tüyü çıkardı
@tohum: doru-0110
Dağın tepesinde Doru ile Kırat yuva oyunu oynuyordu. Yuva için yerden beyaz tüyler topluyorlardı. Birden rüzgar esti ve en büyük tüyü iki kayanın arasına uçurdu. "O büyük tüy yuvanın ortasına lazım," dedi Kırat. Kayaların arası dar ve karanlıktı. Doru cesaretle başını karanlığa uzattı. Tüyü ağzıyla tuttu ve dışarı çıkardı. Sonra tüyü düz kayanın üstündeki yuvaya koydu. "Aferin, Doru, yuva şimdi çok güzel oldu!" dedi Kırat. Doru ile Kırat oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve en büyük tüyü iki kayanın arasına uçurdu"
   - Cümle 3: «Birden rüzgar esti ve en büyük tüyü iki kayanın arasına uçurdu.»
   - Açıklama: Oyun tüyünün kayalar arasına düşmesi önemsiz bir sorun; çıkarıldı ve bitti.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru cesaretle başını karanlığa uzattı"
   - Cümle 6: «Doru cesaretle başını karanlığa uzattı.»
   - Açıklama: Dar ve karanlık kaya arasına baş sokmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0110` birebir aynı, ardından `@onarim: a38e0a7f5b28da469b6b6bfbd5165d9995c82ba3`, sonra gövde.

### Hikâye 11: tohum doru-0111 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0111
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'alet', fiil 'öpmek', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: vadinin öbür ucunda beyaz bir şey parladı | bulut gelmeden hızla koşup karı buldu
@tohum: doru-0111
@degisim: alet -> kar
Yüksek dağda hava sıcaktı. Doru vadide çimen yiyordu. Birden vadinin öbür ucunda beyaz bir şey parladı. Doru bunun ne olduğunu çok merak etti. Ama büyük bir bulut güneşe doğru geliyordu. Doru bulut gelmeden oraya gitmek istedi. Düz vadide hızla koştu ve hemen yetişti. Bir kayanın dibinde küçük, yuvarlak bir kar yığını vardı. Kar güneşte parlıyordu ve mükemmel bir top gibi duruyordu. Doru burnuyla kar yığınını yavaşça öptü. Kar çok soğuktu ve Doru güldü. Doru çok sevindi, çünkü parlayan şeyin kar olduğunu bulmuştu.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "beyaz bir şey parladı"
   - Cümle 3: «Birden vadinin öbür ucunda beyaz bir şey parladı.»
   - Açıklama: Uzakta parlayan bir şey gerçek bir sorun değil; sebebi olan bir güçlük yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden vadinin öbür ucunda beyaz bir şey parladı"
   - Cümle 3: «Birden vadinin öbür ucunda beyaz bir şey parladı.»
   - Açıklama: Ortada çocuğun önemseyeceği bir sorun yok, yalnız bir merak var.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "büyük bir bulut güneşe doğru geliyordu"
   - Cümle 5: «Ama büyük bir bulut güneşe doğru geliyordu.»
   - Açıklama: Bulut bir tehlike gibi kuruluyor ama bir daha geçmiyor ve olayda işe yaramıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hızla koştu ve hemen yetişti"
   - Cümle 7: «Düz vadide hızla koştu ve hemen yetişti.»
   - Açıklama: 'Yetişmek' tümleçsiz ve yanlış anlamda kullanılmış; 'oraya vardı' olmalı.
   - Açıklama: 'Yetişti' yanlış anlamda; 'oraya vardı' olmalı.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "mükemmel bir top gibi"
   - Cümle 9: «Kar güneşte parlıyordu ve mükemmel bir top gibi duruyordu.»
   - Açıklama: 'Mükemmel' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "mükemmel bir top gibi duruyordu"
   - Cümle 9: «Kar güneşte parlıyordu ve mükemmel bir top gibi duruyordu.»
   - Açıklama: 'Mükemmel' soyut bir kelime ve benzetme 3 yaşındaki çocuğa uygun değil.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kar yığınını yavaşça öptü"
   - Cümle 10: «Doru burnuyla kar yığınını yavaşça öptü.»
   - Açıklama: At burnuyla öpmez; 'burnuyla dokundu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0111` birebir aynı, `@degisim: alet -> kar` (tutuyorsan), ardından `@onarim: dbf356445d6fb20d665802f979f1ad2b408d85d7`, sonra gövde.

### Hikâye 12: tohum doru-0112 (deneme 1 -> 2)

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
@plan: ikisi de acıkmıştı ve tek bir elma kalmıştı | hızla koşup elmayı tuttu ve annesiyle paylaştı
@tohum: doru-0112
Bir sabah Doru ile annesi dağda uzun bir yol yürüdü. İkisi de çok acıkmıştı ama orada hiç çimen yoktu. Doru vadinin öbür ucunda bir elma ağacı gördü. Ağaçta tek bir kırmızı elma kalmıştı. Rüzgar esti ve elma dalda sallandı. "Anne, elma düşerse aşağı yuvarlanır!" dedi Doru. Doru düz vadide hızla koştu ve ağaca yetişti. Elma tam o sırada düştü ve Doru onu ağzıyla tuttu. Sonra elmayı annesine getirdi. "Bu elma ikimize de yeter," dedi Doru. Önce annesi küçük bir lokma aldı, sonra Doru. "Sen çok akıllısın, Doru," dedi annesi. Doru çok mutluydu, çünkü elmayı annesiyle paylaşmıştı.
```

**Hakem bulguları (5):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "elma düşerse aşağı yuvarlanır"
   - Cümle 6: «"Anne, elma düşerse aşağı yuvarlanır!" dedi Doru.»
   - Açıklama: Açlık ve tek elmanın paylaşılması sorununun yanına elmanın düşüp yuvarlanması diye ikinci bir sorun ekleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Doru düz vadide hızla koştu"
   - Cümle 7: «Doru düz vadide hızla koştu ve ağaca yetişti.»
   - Açıklama: Vadi düz deniyor ama Doru elmanın düşerse aşağı yuvarlanacağından korkuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elma tam o sırada düştü"
   - Cümle 8: «Elma tam o sırada düştü ve Doru onu ağzıyla tuttu.»
   - Açıklama: Elmanın tam Doru yetiştiği anda düşmesi çözümü rastlantıyla getiriyor.
   - Açıklama: Elmanın tam Doru yetiştiği anda düşmesi çözümü tesadüfle, sebepsizce getiriyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Sen çok akıllısın, Doru," dedi annesi"
   - Cümle 12: «"Sen çok akıllısın, Doru," dedi annesi.»
   - Açıklama: Tohumdaki özellik hız; akıllılık ikinci bir özellik olarak ekleniyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sen çok akıllısın, Doru"
   - Cümle 12: «"Sen çok akıllısın, Doru," dedi annesi.»
   - Açıklama: Tohumdaki özellik hız; akıllılık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0112` birebir aynı, ardından `@onarim: 21f6407d3eb9b93adadcfca39450d207a2b238fe`, sonra gövde.
