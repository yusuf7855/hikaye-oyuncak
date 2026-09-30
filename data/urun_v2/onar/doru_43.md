# Editör görevi (onarım): Doru, onarım partisi 43

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar43.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar43.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0181 (deneme 1 -> 2)

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
Bir sabah Doru ile Karatay çayırda sırayla atlama oyunu oynuyordu. Çimenlerin ortasındaki alçak taşın önünde kaygan bir yosun vardı. Karatay koştu ama ayağı yosunun üstünde kaydı ve taşı geçemedi. Karatay üzüldü ve başını eğdi. Sıra Doru'daydı ama Doru önce arkadaşına yardım etti. Ön ayağıyla yosunu taşın önünden kazıdı ve temizledi. "Bir daha dene, Karatay, sıra yine sende," dedi Doru. Karatay yeniden koştu ve taşın üstünden yükseğe zıpladı. "Çok havalı zıpladın, Karatay!" dedi Doru. Sonra sıra Doru'ya geldi ve o da taşın üstünden atladı. İki arkadaş çayırda sırayla atlamaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Karatay çayırda sırayla"
   - Cümle 1: «Bir sabah Doru ile Karatay çayırda sırayla atlama oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Karatay çayırda"
   - Cümle 1: «Bir sabah Doru ile Karatay çayırda sırayla atlama oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çok havalı zıpladın"
   - Cümle 9: «"Çok havalı zıpladın, Karatay!" dedi Doru.»
   - Açıklama: 'Havalı' argo bir kelime ve 3 yaşındaki çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çok havalı zıpladın, Karatay!"
   - Cümle 9: «"Çok havalı zıpladın, Karatay!" dedi Doru.»
   - Açıklama: 'Havalı' argo ve soyut bir kelime, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0181` birebir aynı, `@degisim: giyinmek -> zıplamak` (tutuyorsan), ardından `@onarim: e9b16d570adebd49312bde4a45d8e3af0645e2a5`, sonra gövde.

### Hikâye 2: tohum doru-0182 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: aydınlık çimenliğe giden yolu eğri bir dal kapattı | cesaretle dalın altından geçti
@tohum: doru-0182
@degisim: binmek -> geçmek
Ormanda Doru, hazine arama oyunu oynuyordu. Oyunda aydınlık bir çimenlik onun hazinesiydi. Ama yolu eğri bir dal kapatmıştı. Dalın ucu yere değiyor ve büyük bir halka yapıyordu. Arkası karanlıktı ve görünmüyordu. Doru bir an durdu ve kulaklarını dikti. Sonra cesaretle başını eğdi ve halkadan geçti. Dalın arkasında güneşli, geniş bir çimenlik vardı. Doru çimenliğe koştu ve sevinçle zıpladı. Doru, oyunda aradığı hazineyi sonunda bulmuştu. Doru bundan sonra karanlık dallardan hiç korkmadı.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama yolu eğri bir dal kapatmıştı"
   - Cümle 3: «Ama yolu eğri bir dal kapatmıştı.»
   - Açıklama: Dal geçilebilir bir halka yapıyor, asıl sorun olan korku hiç söylenmiyor; sorunun sebebi açık değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yolu eğri bir dal kapatmıştı"
   - Cümle 3: «Ama yolu eğri bir dal kapatmıştı.»
   - Açıklama: Dalın yolu kapattığı söyleniyor ama Doru dalın yaptığı halkadan hiçbir engel olmadan geçiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle başını eğdi ve halkadan geçti"
   - Cümle 7: «Sonra cesaretle başını eğdi ve halkadan geçti.»
   - Açıklama: Arkası karanlık ve görünmeyen bir açıklıktan tek başına geçmek çocuğun taklit edebileceği riskli bir davranış olarak övülüyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra cesaretle başını eğdi ve halkadan geçti"
   - Cümle 7: «Sonra cesaretle başını eğdi ve halkadan geçti.»
   - Açıklama: Yolu kapattığı söylenen dal kolayca geçilen bir halka; kapanma ile çelişiyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru, oyunda aradığı hazineyi sonunda bulmuştu. Doru bundan sonra"
   - Cümle 10: «Doru, oyunda aradığı hazineyi sonunda bulmuştu.»
   - Açıklama: Doru adı art arda üç cümlenin başında gereksizce tekrarlanıyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karanlık dallardan hiç korkmadı"
   - Cümle 11: «Doru bundan sonra karanlık dallardan hiç korkmadı.»
   - Açıklama: Karanlık olan dal değil dalın arkasıydı; 'karanlık dallar' kelimeyi yanlış nesneye bağlıyor.
   - Açıklama: Dallar karanlık değil, dalın arkası karanlıktı; sıfat yanlış isme bağlanmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0182` birebir aynı, `@degisim: binmek -> geçmek` (tutuyorsan), ardından `@onarim: e24a2082577258cebc463c858c43aabe383828fb`, sonra gövde.

### Hikâye 3: tohum doru-0183 (deneme 1 -> 2)

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
@plan: rüzgar esti ve bulutun gölgesi öne geçti | düz çayırda hızla koşup gölgeyi geride bıraktı
@tohum: doru-0183
@degisim: baloncuk -> gölge
Doru çayırda bir bulutun gölgesiyle yarışıyordu. Çayırın sonundaki mor çiçeklere gölgeden önce varmak istiyordu. Ama birden rüzgar esti ve gölge Doru'nun önüne geçti. Gölge çimenlerin üstünde çabucak ilerledi. Doru bir an durdu ve gölgeye baktı. Sonra başını öne uzattı ve düz çayırda hızla koştu. Az sonra gölgeye yetişti ve onu geride bıraktı. Mor çiçeklerin yanına ilk o vardı. Gölge ancak biraz sonra çiçeklerin üstüne geldi. Doru çiçeklerin çevresinde neşeyle zıpladı. Doru çok sevindi, çünkü yarışı gölgeden önce bitirmişti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru çayırda bir bulutun gölgesiyle yarışıyordu"
   - Cümle 1: «Doru çayırda bir bulutun gölgesiyle yarışıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor ve park hiç anılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve gölge Doru'nun önüne geçti"
   - Cümle 3: «Ama birden rüzgar esti ve gölge Doru'nun önüne geçti.»
   - Açıklama: Rüzgarın gölgeyi öne geçirmesi ve koşup geçmek önemsiz bir sorun; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0183` birebir aynı, `@degisim: baloncuk -> gölge` (tutuyorsan), ardından `@onarim: effcd782c9692c3d8f0525ff39c3002bd912db98`, sonra gövde.

### Hikâye 4: tohum doru-0184 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: küçük arkadaşın sevdiği ekşi erikler çok uzaktaydı | düz vadide hızla koşup bir erik getirdi
@tohum: doru-0184
@degisim: tohum -> erik
Doru dağda küçük Alaca'ya bir sürpriz hazırlamak istedi. Alaca bu sabah ilk kez vadinin sonuna kadar gitmişti. Ama Alaca'nın çok sevdiği ekşi erikler çok uzaktaydı. Alaca şimdi çimenlerin üstünde uyuyordu. Doru düz vadide hızla koştu ve erik ağacına vardı. Yere düşmüş bir eriği ağzına aldı ve hemen döndü. Eriği Alaca'nın önüne yavaşça bıraktı. Alaca gözlerini açtı ve eriği gördü. "Bu benim için mi, Doru?" diye sordu Alaca. "Evet, bugün çok yol gittin," dedi Doru. Alaca eriği ısırdı ve mutlulukla başını salladı. Doru bundan sonra Alaca'ya hep ekşi erik getirdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ilk kez vadinin sonuna"
   - Cümle 2: «Alaca bu sabah ilk kez vadinin sonuna kadar gitmişti.»
   - Açıklama: 'Vadi' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Alaca'nın çok sevdiği"
   - Cümle 3: «Ama Alaca'nın çok sevdiği ekşi erikler çok uzaktaydı.»
   - Açıklama: 'Ama' bağlacı önceki cümleyle bir karşıtlık kurmuyor; yanlış anlamda kullanılmış.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ekşi erikler çok uzaktaydı"
   - Cümle 3: «Ama Alaca'nın çok sevdiği ekşi erikler çok uzaktaydı.»
   - Açıklama: Eriklerin uzakta olması ortada bir sorun yaratmıyor; sorun ve sebebi belirsiz.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru bundan sonra Alaca'ya hep ekşi erik getirdi"
   - Cümle 12: «Doru bundan sonra Alaca'ya hep ekşi erik getirdi.»
   - Açıklama: Son cümle ders değil, zamanı ileriye atlatan bir alışkanlık anlatıyor.
   - Açıklama: Son cümle olaydan çıkan bir ders değil, hikayeyi sonraki günlere taşıyan bir alışkanlık anlatımı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0184` birebir aynı, `@degisim: tohum -> erik` (tutuyorsan), ardından `@onarim: 96ed732a6ceee38d4eb0dfe616e1c57e0468bb86`, sonra gövde.

### Hikâye 5: tohum doru-0186 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0186
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'marul', fiil 'fışkırmak', sıfat 'sert'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: sert rüzgar karşıdan esti ve koşmak zorlaştı | başını öne eğdi ve düz vadide hızla koştu
@tohum: doru-0186
@degisim: marul -> kaya
Dağda sert bir rüzgar esiyordu. Doru, Kırat'ın anlattığı kayalara ilk kez koşmayı denedi. Ama rüzgar karşıdan esiyordu ve Doru çok yavaş gidiyordu. "O kayaların arasından su çıkar," dedi Kırat. Doru suyu görmeyi çok istiyordu. Başını öne eğdi ve düz vadide hızla koştu. Doru kısa sürede kayalara vardı. Kayaların arasından soğuk su fışkırıyordu. Kırat yavaş yavaş arkasından geldi. "Aferin, Doru, ilk denemede kayalara vardın!" dedi Kırat. İkisi soğuk sudan içti ve mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Başını öne eğdi ve düz vadide hızla koştu"
   - Cümle 6: «Başını öne eğdi ve düz vadide hızla koştu.»
   - Açıklama: Rüzgar hâlâ karşıdan eserken başını eğmek yavaşlık sorununu gerçekten çözmüyor; çözüm sebebe yönelmeden yalnız istekle geliyor.
   - Açıklama: Rüzgar hala karşıdan eserken yalnız başını eğip hızla koşması sebebe yönelmiyor, yavaşlık sorunu açıklamasızca kalkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "düz vadide hızla koştu"
   - Cümle 6: «Başını öne eğdi ve düz vadide hızla koştu.»
   - Açıklama: Dağda sebepsizce düz bir vadi beliriyor ve çözümü kendiliğinden getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0186` birebir aynı, `@degisim: marul -> kaya` (tutuyorsan), ardından `@onarim: c7537929c079c05e86f95cb41bcae901620c2c72`, sonra gövde.

### Hikâye 6: tohum doru-0187 (deneme 1 -> 2)

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
Çayırda Doru ile annesi yan yana çimen yiyordu. Birden annesinin uzun yelesi sık bir çalıya takıldı. Annesi başını çekti ama yelesi dallardan çıkmadı. "Doru, bana yardım eder misin?" dedi annesi. Rüzgar esince çalı sallanıyor ve garip sesler çıkarıyordu. Doru bu seslerden önce biraz çekindi. Sonra cesaretle çalıya yaklaştı ve dalı dişleriyle tuttu. Dalı yavaşça geri çekti ve annesi başını kurtardı. Annesi yelesini salladı, hiçbir tel eksik değildi. "Teşekkürler, Doru, çok iyi yardım ettin," dedi annesi. İkisi çayırda yan yana mutlu mutlu çimen yemeye devam etti.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda Doru ile annesi"
   - Cümle 1: «Çayırda Doru ile annesi yan yana çimen yiyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "çalı sallanıyor ve garip sesler çıkarıyordu"
   - Cümle 5: «Rüzgar esince çalı sallanıyor ve garip sesler çıkarıyordu.»
   - Açıklama: Garip sesler çıkaran çalı küçük çocuk için ürkütücü bir öğe olarak kuruluyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bu seslerden önce biraz çekindi"
   - Cümle 6: «Doru bu seslerden önce biraz çekindi.»
   - Açıklama: 'önce' kelimesinin yeri yanlış; 'sesler çıkmadan önce' gibi okunuyor, 'Doru önce bu seslerden biraz çekindi' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "seslerden önce biraz çekindi"
   - Cümle 6: «Doru bu seslerden önce biraz çekindi.»
   - Açıklama: 'çekindi' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'korktu' daha uygun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0187` birebir aynı, `@degisim: limon -> çalı` (tutuyorsan), ardından `@onarim: 9e4c9866e0cc2d9582a8d4642d87470826acd60c`, sonra gövde.

### Hikâye 7: tohum doru-0188 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar esti ve kuru bir dal izi kapattı | cesaretle dalı kaldırdı ve kenara çekti
@tohum: doru-0188
Bir sabah Doru ormanda ıslak toprakta bir oyun oynuyordu. Ayaklarıyla çamurda büyük, yuvarlak bir iz yapıyordu. Ama birden rüzgar esti ve kuru bir dal izi kapattı. Dal büyüktü ve yaprakları sallanıyordu. Doru önce dala yaklaşmak istemedi. Sonra cesaretle dalın ucunu dişleriyle tuttu. Dalı yavaşça kaldırdı ve kenara çekti. Altındaki iz hiç bozulmadı. Doru yuvarlağı son bir adımla bitirdi. Sonra izine baktı ve neşeyle zıpladı. Doru çok sevindi, çünkü kirli ayaklarıyla yaptığı iz yerinde duruyordu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "birden rüzgar esti ve kuru bir dal izi kapattı"
   - Cümle 3: «Ama birden rüzgar esti ve kuru bir dal izi kapattı.»
   - Açıklama: Rüzgarın dalı getirip dalın kaldırılmasıyla biten olay önemsiz ve sorun gibi durmuyor; iz zaten hiç bozulmuyor.
   - Açıklama: Sorun önemsiz bir olay; dal kenara çekilince biter ve büyük dalın çamurdaki izi hiç bozmaması da akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0188` birebir aynı, ardından `@onarim: e3ad29565ee01ec83c8976e47e400dcaebe591b8`, sonra gövde.

### Hikâye 8: tohum doru-0189 (deneme 1 -> 2)

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
Bir sabah Doru dağda Alaca ile ilgileniyordu. İkisi bir kozalağı ayaklarıyla itip eğlenceli bir oyun oynuyordu. Ama kozalak yuvarlandı ve iki kaya arasına girdi. Doru burnunu uzattı ama yer ona dardı. "Alaca, sen küçüksün, onu alır mısın?" diye sordu Doru. "Orası çok karanlık, korkuyorum," dedi Alaca. Doru cesaretle başını eğdi ve içeri baktı. "Korkma, Alaca, içeride yalnız kozalak var," dedi Doru. Alaca başını soktu ve kozalağı dişleriyle çıkardı. "İşte buldum!" dedi Alaca. Doru çok sevindi, çünkü yardım isteyince oyunları yine başlamıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru dağda Alaca ile ilgileniyordu"
   - Cümle 1: «Bir sabah Doru dağda Alaca ile ilgileniyordu.»
   - Açıklama: 'İlgilenmek' burada yanlış anlamda; iki arkadaş birlikte oynuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Alaca ile ilgileniyordu"
   - Cümle 1: «Bir sabah Doru dağda Alaca ile ilgileniyordu.»
   - Açıklama: 'İlgilenmek' soyut bir kelime ve 3 yaşındaki çocuk için ne yapıldığı belli değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yer ona dardı"
   - Cümle 4: «Doru burnunu uzattı ama yer ona dardı.»
   - Açıklama: 'Yer' belirsiz kullanılmış; kastedilen iki kaya arasındaki aralık.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Alaca başını soktu ve kozalağı"
   - Cümle 9: «Alaca başını soktu ve kozalağı dişleriyle çıkardı.»
   - Açıklama: En küçük at karanlık ve dar bir kaya arasına başını sokuyor; çocuk taklit ederse dar boşluğa sıkışabilir.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Alaca başını soktu ve kozalağı dişleriyle çıkardı"
   - Cümle 9: «Alaca başını soktu ve kozalağı dişleriyle çıkardı.»
   - Açıklama: İki kaya arasındaki dar ve karanlık aralığa baş sokmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0189` birebir aynı, `@degisim: soğan -> kozalak` (tutuyorsan), ardından `@onarim: 2cb977c2a70358afb68680a38cbef173f006b1eb`, sonra gövde.

### Hikâye 9: tohum doru-0190 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0190
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'rüzgar', fiil 'kurtarmak', sıfat 'ucuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yavaş gidince yaprak uçmadı ve aşağı düştü | düz vadide hızla koştu ve yaprak havaya kalktı
@tohum: doru-0190
@degisim: ucuz -> geniş
Rüzgar vadide hafifçe esiyordu. Doru geniş bir yaprağı ağzına aldı. Onu rüzgarda uçurmayı ilk kez denedi. Ama Doru yavaş gidince yaprak hep aşağı düştü. Yeni oyunu bozulmak üzereydi. Doru bu oyunu kurtarmak istedi. Düz ve açık bir yere çıktı ve hızla koştu. Hava yaprağın altına doldu. Yaprak havalandı ve Doru'nun başının yanında çırpındı. Yaprak gittikçe daha yükseğe kalktı. Doru bu yeni oyunu çok sevdi. Doru yaprağıyla vadide mutlu mutlu koşmaya devam etti.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Doru yavaş gidince yaprak hep aşağı düştü"
   - Cümle 4: «Ama Doru yavaş gidince yaprak hep aşağı düştü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yeni oyunu bozulmak üzereydi"
   - Cümle 5: «Yeni oyunu bozulmak üzereydi.»
   - Açıklama: Oyunun bozulması soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Oyun bozulmak üzereydi' soyut ve mecazlı bir anlatım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu oyunu kurtarmak istedi"
   - Cümle 6: «Doru bu oyunu kurtarmak istedi.»
   - Açıklama: Oyunu kurtarmak mecazlı ve soyut bir ifade.
   - Açıklama: 'Oyunu kurtarmak' mecaz; 3 yaşındaki çocuğa uygun değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hava yaprağın altına doldu"
   - Cümle 8: «Hava yaprağın altına doldu.»
   - Açıklama: 'Hava doldu' öznesine uygun değil; 'rüzgar yaprağın altına girdi' olmalı.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Yaprak gittikçe daha yükseğe kalktı"
   - Cümle 10: «Yaprak gittikçe daha yükseğe kalktı.»
   - Açıklama: Yaprak Doru'nun ağzında tutuluyorken gittikçe daha yükseğe kalkması çelişkili.
   - Açıklama: Yaprak Doru'nun ağzında tutulurken gittikçe daha yükseğe kalkamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0190` birebir aynı, `@degisim: ucuz -> geniş` (tutuyorsan), ardından `@onarim: abd9adb4f4bdd770fdb9042266c5a55fed36b0e9`, sonra gövde.

### Hikâye 10: tohum doru-0192 (deneme 1 -> 2)

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
Çayırın kenarından pat diye bir ses geldi. Doru çimen yerken başını kaldırdı ve dinledi. Ses büyük bir ağacın altındaki sık çalıdan gelmişti. Çalının içi karanlıktı ve dalları sallanıyordu. Doru bu sesi çok merak etti. Cesaretle çalıya yaklaştı ve burnuyla dalları itti. Çimenlerin arasında kırmızı bir elma duruyordu. Elmanın kabuğu plastik gibi parlaktı. O anda ağaçtan bir elma daha düştü ve pat diye ses çıkardı. Doru elmayı afiyetle yedi. Doru çok sevindi, çünkü sesin düşen tatlı bir yiyecekten geldiğini anlamıştı.
```

**Hakem bulguları (7):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırın kenarından pat diye"
   - Cümle 1: «Çayırın kenarından pat diye bir ses geldi.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda başlıyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalının içi karanlıktı ve dalları sallanıyordu"
   - Cümle 4: «Çalının içi karanlıktı ve dalları sallanıyordu.»
   - Açıklama: Garip sesle birlikte karanlık ve sallanan çalı 3-6 yaş için ürkütücü bir gerilim kuruyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kabuğu plastik gibi parlaktı"
   - Cümle 8: «Elmanın kabuğu plastik gibi parlaktı.»
   - Açıklama: 'Plastik gibi' benzetmesi gereksiz bir mecaz ve elmaya uygun değil.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Elmanın kabuğu plastik gibi parlaktı"
   - Cümle 8: «Elmanın kabuğu plastik gibi parlaktı.»
   - Açıklama: Kapalı doğa dünyasında kartta olmayan çağdaş bir malzeme (plastik) anılıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elmanın kabuğu plastik gibi parlaktı"
   - Cümle 8: «Elmanın kabuğu plastik gibi parlaktı.»
   - Açıklama: Elmanın plastik gibi olduğu vurgulanıp sahte olabileceği ima ediliyor ama bu ayrıntı hiçbir işe yaramıyor ve Doru elmayı yiyor.
   - Açıklama: Elmanın plastik gibi olduğu ayrıntısı bir işe yaramıyor ve elmanın gerçek olup olmadığını şüpheli bırakıyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru elmayı afiyetle yedi"
   - Cümle 10: «Doru elmayı afiyetle yedi.»
   - Açıklama: Plastik gibi görünen, çalı dibinde yerde bulunan bir şeyin yenmesi çocuk için taklit edilince tehlikeli bir örnek olabilir.
7. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Doru elmayı afiyetle yedi"
   - Cümle 10: «Doru elmayı afiyetle yedi.»
   - Açıklama: İki elma varken hangi elmanın yendiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0192` birebir aynı, `@degisim: anlaşmak -> anlamak` (tutuyorsan), ardından `@onarim: ed838a7ee976355e3363f62986223505ed6a0e43`, sonra gövde.
