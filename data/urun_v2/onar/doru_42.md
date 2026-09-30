# Editör görevi (onarım): Doru, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0167 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0167
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'blok', fiil 'örtmek', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: oynarken annesinden uzaklaştı | düz yolda koşup annesine döndü ve özür diledi
@tohum: doru-0167
@degisim: blok -> dal
Doru ormanda annesiyle birlikte çimen yiyordu. Annesi ona yanında kalmasını söylemişti. Ama Doru yaprakların arasında oynarken annesinden uzaklaştı. Birden bulutlar güneşi örttü. Doru o zaman annesini hatırladı. Annesinin yanına hemen dönmek istedi. Ormanın düz ve geniş yolunda hızla koştu. Yoldaki kuru dallar çok kırılgandı ve ayaklarının altında çıt çıt kırıldı. Annesi bu sesi duydu ve başını kaldırdı. Büyük bir ağacın yanında onu bekliyordu. Doru başını eğdi ve annesinden özür diledi. Annesi başını Doru'nun başına sürdü. Doru çok sevindi, çünkü annesinin yanına çabucak dönmüştü.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden bulutlar güneşi örttü"
   - Cümle 4: «Birden bulutlar güneşi örttü.»
   - Açıklama: Bulutların güneşi örtmesi sebepsiz beliriyor ve Doru'nun annesini hatırlamasına akla yatkın bir bağ kurmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuru dallar çok kırılgandı"
   - Cümle 8: «Yoldaki kuru dallar çok kırılgandı ve ayaklarının altında çıt çıt kırıldı.»
   - Açıklama: 'Kırılgan' kelimesi 3 yaşındaki çocuğun bileceği bir kelime değil.
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kırılgandı ve ayaklarının altında çıt çıt kırıldı"
   - Cümle 8: «Yoldaki kuru dallar çok kırılgandı ve ayaklarının altında çıt çıt kırıldı.»
   - Açıklama: Aynı cümlede 'kırılgandı' ve 'kırıldı' gereksiz tekrar ediyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yoldaki kuru dallar çok kırılgandı"
   - Cümle 8: «Yoldaki kuru dallar çok kırılgandı ve ayaklarının altında çıt çıt kırıldı.»
   - Açıklama: Kırılan dallar ve annenin sesi duyması çözüme bir şey katmıyor; Doru zaten annesine dönüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0167` birebir aynı, `@degisim: blok -> dal` (tutuyorsan), ardından `@onarim: d148f1bf6d34514f9f4a0aed7e22f5b6a102de12`, sonra gövde.

### Hikâye 2: tohum doru-0168 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0168
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bez', fiil 'dokunmak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar en sevdiği tüyü vadinin öbür ucuna götürdü | açık ve düz yerde koşup tüyü buldu
@tohum: doru-0168
@degisim: bez -> tüy
Bir sabah Doru vadide en sevdiği beyaz tüyle oynuyordu. Birden sert bir rüzgar esti ve Doru'nun yelesini karmakarışık etti. Rüzgar beyaz tüyü de alıp vadinin öbür ucuna götürdü. Doru tüyünü artık göremiyordu. Doru onu hemen bulmak istedi. Vadinin ortası açık ve düzdü. Doru orada hızla koştu. Uzakta, bir kayanın dibinde küçük beyaz bir şey gördü. Doru yaklaştı ve burnuyla ona dokundu. Bu onun tüyüydü! Doru tüyü dişleriyle tuttu ve oyun yerine döndü. Sonra tüyüyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Doru'nun yelesini karmakarışık etti"
   - Cümle 2: «Birden sert bir rüzgar esti ve Doru'nun yelesini karmakarışık etti.»
   - Açıklama: Yelenin karışması kurulup olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Karışan yele ayrıntısı bir daha ele alınmıyor ve olayda işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0168` birebir aynı, `@degisim: bez -> tüy` (tutuyorsan), ardından `@onarim: 34a9dceae6c304c10607cb7a2e83a4932cfcf73d`, sonra gövde.

### Hikâye 3: tohum doru-0169 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0169
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'demet', fiil 'uyandırmak', sıfat 'küçük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: koşarken arkadaşının çiçeklerini yere dağıttı | cesaretle özür diledi ve çiçekleri topladı
@tohum: doru-0169
@degisim: demet -> çiçek
Kuşlar ötüyordu ve Doru ormanda neşeyle koşuyordu. Karatay bir ağacın dibinde uyuyordu. Yanında küçük çiçekler vardı. Doru yanlışlıkla çiçeklere çarptı ve hepsi yere dağıldı. Doru'nun ayak sesleri Karatay'ı uyandırdı. "Çiçeklerim nerede?" diye sordu Karatay. Doru önce biraz durdu ve Karatay'a baktı. Sonra cesaretle Karatay'ın yanına gitti. "Özür dilerim, Karatay, onları ben dağıttım," dedi Doru. Doru çiçekleri tek tek ağzıyla topladı. Hepsini Karatay'ın önüne bıraktı. "Teşekkürler, Doru, çiçeklerim yine bir arada!" dedi Karatay.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Doru çiçekleri tek tek ağzıyla topladı"
   - Cümle 10: «Doru çiçekleri tek tek ağzıyla topladı.»
   - Açıklama: Dağılan çiçekleri toplamak 'dağıttı, topladı, bitti' türünden önemsiz bir olay olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0169` birebir aynı, `@degisim: demet -> çiçek` (tutuyorsan), ardından `@onarim: 22ffb3747b0b2e738c3b80eebef476eb02367e24`, sonra gövde.

### Hikâye 4: tohum doru-0170 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0170
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'yama', fiil 'yatmak', sıfat 'paslı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: yakındaki çiçekler gölgede kaldı ve açmadı | çayırın öbür ucunu gördü ve oraya koştu
@tohum: doru-0170
@degisim: paslı -> sarı
Bir sabah Doru ile Kırat çayırda yatıyor ve çiçeklerin açmasını bekliyordu. Ama yakındaki çiçekler büyük bir ağacın altında, gölgede kalmıştı. Bu yüzden o çiçekler açmıyordu. Doru başını kaldırdı ve çayırın öbür ucuna baktı. Orada, güneşte yama gibi sarı bir yer vardı. "Kırat, oradaki çiçekler güneşte, onlar açılır!" dedi Doru. Doru hızla oraya koştu. Sarı yapraklar yavaş yavaş açılıyordu. Doru bir çiçeğin açılmasını baştan sona gördü. Kırat da yavaşça Doru'nun yanına geldi. "Ne güzel, değil mi?" dedi Kırat. Sonra ikisi açan çiçekleri birlikte mutlu mutlu seyretti.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Kırat çayırda yatıyor"
   - Cümle 1: «Bir sabah Doru ile Kırat çayırda yatıyor ve çiçeklerin açmasını bekliyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor ve park hiç anılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güneşte yama gibi sarı bir yer"
   - Cümle 5: «Orada, güneşte yama gibi sarı bir yer vardı.»
   - Açıklama: 'Yama gibi' benzetmesi ve 'yama' kelimesi 3 yaşındaki çocuk için uygun değildir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güneşte yama gibi sarı"
   - Cümle 5: «Orada, güneşte yama gibi sarı bir yer vardı.»
   - Açıklama: 'Yama gibi' benzetmesi mecazdır ve 3 yaşındaki çocuk 'yama' kelimesini bilmeyebilir.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oradaki çiçekler güneşte, onlar açılır"
   - Cümle 6: «"Kırat, oradaki çiçekler güneşte, onlar açılır!" dedi Doru.»
   - Açıklama: Çiçek için 'açar' denir; 'açılır' fiili burada öznesine tam uymuyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru hızla oraya koştu"
   - Cümle 7: «Doru hızla oraya koştu.»
   - Açıklama: Çözüm gölge sebebine yönelmiyor; gölgedeki çiçekler açmadan kalıyor, Doru yalnız başka yere gidiyor.
   - Açıklama: Çözüm gölgedeki çiçeklerin sorununa yönelmiyor, onları bırakıp başka çiçeklere gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0170` birebir aynı, `@degisim: paslı -> sarı` (tutuyorsan), ardından `@onarim: 62e5902ef10123d33b7329aeea45d8de35ac60f5`, sonra gövde.

### Hikâye 5: tohum doru-0171 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0171
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kütük', fiil 'kopmak', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: rüzgarda bir dal koptu ve kütüğe giden yolu kapattı | cesaretle dala yaklaştı ve onu yolun kenarına itti
@tohum: doru-0171
Rüzgar ağaçların arasında sert sert esiyordu. Doru ormanda bir oyun oynuyordu; geniş bir kütük onun dağı olacaktı. Ama rüzgarda büyük bir dal koptu ve kütüğe giden yolu kapattı. Doru önce durdu ve biraz düşündü. Sonra cesaretle büyük dala yaklaştı. Dalı burnuyla yavaş yavaş yolun kenarına itti. Yol açılınca hemen kütüğe koştu. Doru ön ayaklarını kütüğün üstüne koydu ve başını kaldırdı. Artık oyundaki dağın tepesindeydi. Doru çok sevindi, çünkü oyununu yine oynayabiliyordu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra cesaretle büyük dala yaklaştı"
   - Cümle 5: «Sonra cesaretle büyük dala yaklaştı.»
   - Açıklama: Sert rüzgarda dal koparken ağaçların altındaki büyük dala yaklaşmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Sert rüzgarda kopan büyük dala yaklaşmak cesaret örneği olarak sunuluyor ve taklit edilince tehlikelidir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0171` birebir aynı, ardından `@onarim: a46a170795494e35c874d8455847126f13172cef`, sonra gövde.

### Hikâye 6: tohum doru-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0173
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'buğday', fiil 'süslenmek', sıfat 'rüzgarlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: kayaların arasından garip bir ıslık sesi geldi | cesaretle kayalara yürüdü ve taşta bir delik buldu
@tohum: doru-0173
@degisim: buğday -> delik
Dağda rüzgarlı bir sabahtı. Doru büyük kayaların yakınında çimen yiyordu. Birden kayaların arasından ince bir ıslık sesi geldi. Doru bu sesi çok merak etti. Ses biraz garipti ama Doru cesurdu. Kayaların arasına adım adım yürüdü. Orada eski ve büyük bir taş gördü. Taşın ortasında yuvarlak bir delik vardı. Deliğin etrafı küçük mor çiçeklerle süslenmişti. Rüzgar esince delikten ıslık sesi çıktı. Rüzgar durunca ses de durdu. Doru sesin bu delikten geldiğini anladı. Sonra taşın yanında mutlu mutlu çimen yemeye devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Deliğin etrafı küçük mor çiçeklerle süslenmişti"
   - Cümle 9: «Deliğin etrafı küçük mor çiçeklerle süslenmişti.»
   - Açıklama: Mor çiçekler kuruluyor ama olayda hiçbir işe yaramıyor.
   - Açıklama: Mor çiçekler sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0173` birebir aynı, `@degisim: buğday -> delik` (tutuyorsan), ardından `@onarim: 72861da2e27147206e7fa3dd144353856c854f3f`, sonra gövde.

### Hikâye 7: tohum doru-0174 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0174
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yonca', fiil 'bitirmek', sıfat 'kilitli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: rüzgarda annesinin tüylerine kuru bir dal takıldı | dalı dişleriyle yavaşça çekip çıkardı
@tohum: doru-0174
@degisim: kilitli -> mor
Doru annesiyle dağda mor yoncalar yiyordu. Birden rüzgar esti ve annesinin tüylerine kuru bir dal takıldı. Annesi başını salladı ama dal düşmedi. "Doru, bu dalı alabilir misin?" diye sordu annesi. Doru daha önce hiç böyle bir şey yapmamıştı. Ama annesine hemen yardım etmek istedi. Dala dikkatle baktı. Sonra dalı dişleriyle yavaşça tuttu ve çekti. Dal tüylerden kolayca çıktı. "Oldu, anneciğim!" dedi Doru. "Aferin, Doru, çok güzel yaptın," dedi annesi. Sonra ikisi yemeklerini mutlu mutlu bitirdi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "annesinin tüylerine kuru bir dal takıldı"
   - Cümle 2: «Birden rüzgar esti ve annesinin tüylerine kuru bir dal takıldı.»
   - Açıklama: Tüye takılan bir dal önemsiz bir olay ve tek dokunuşta kolayca çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0174` birebir aynı, `@degisim: kilitli -> mor` (tutuyorsan), ardından `@onarim: d596c235484e6d3b74eeb7acaca9b580e8baad86`, sonra gövde.

### Hikâye 8: tohum doru-0175 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0175
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kereviz', fiil 'inanmak', sıfat 'sarı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: saklanırken annesinin kuyruğu çalının dallarına takıldı | dalları dişleriyle kenara çekip kuyruğu kurtardı
@tohum: doru-0175
@degisim: kereviz -> çalı
Ormanda Doru ile annesi sarı yaprakların arasında saklambaç oynuyordu. Annesi büyük bir çalının arkasına saklandı ama kuyruğu dışarıda kaldı. Sonra kuyruğu çalının dallarına takıldı. Doru kuyruğu hemen gördü ve güldü. "Seni buldum, anne!" dedi Doru. "Buna inanamıyorum, kuyruğum beni gösterdi!" dedi annesi ve güldü. Annesi çıkmak istedi ama kuyruğunu dallardan kurtaramadı. "Doru, bana yardım eder misin?" diye sordu annesi. Doru dalları dişleriyle tek tek kenara çekti. Kuyruk kurtuldu ve annesi çalıdan çıktı. İkisi birbirine bakıp yine güldü. Doru çok mutluydu, çünkü annesinin kuyruğunu kurtarmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Buna inanamıyorum, kuyruğum beni gösterdi!"
   - Cümle 6: «"Buna inanamıyorum, kuyruğum beni gösterdi!" dedi annesi ve güldü.»
   - Açıklama: 'Buna inanamıyorum' kalıp söz ve 'kuyruğum beni gösterdi' mecazlı, küçük çocuğa soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0175` birebir aynı, `@degisim: kereviz -> çalı` (tutuyorsan), ardından `@onarim: 488df8d6528194fc0ec8ba0dd748a64daf4bf03f`, sonra gövde.

### Hikâye 9: tohum doru-0177 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0177
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'leke', fiil 'yardımlaşmak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: zıplarken su dolu çukurun ortasına indi | korkmadan daha uzun koşup çukurun üstünden atladı
@tohum: doru-0177
@degisim: yardımlaşmak -> zıplamak
Doru çayırda zıplama oyunu oynuyordu. Yağmurdan sonra çayırdaki küçük bir çukur suyla dolmuştu. Çukurun ortasında yırtık, sarı bir yaprak yüzüyordu. Doru yaprağın ve çukurun üstünden atlamak istedi. Koştu ve zıpladı ama suyun tam ortasına indi. Çamurlu su her yere sıçradı. Doru'nun bacakları kahverengi lekelerle doldu. Doru bacaklarına baktı ve güldü. Ama ıslanmaktan korkmadı. Cesaretle biraz geri gitti ve bu kez daha uzun koştu. Sonra çok yüksek zıpladı ve çukurun üstünden geçti. Doru lekeli bacaklarıyla çayırda mutlu mutlu zıplamaya devam etti.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru çayırda zıplama oyunu"
   - Cümle 1: «Doru çayırda zıplama oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Çukurun ortasında yırtık, sarı bir yaprak yüzüyordu.»
   - Açıklama: Sorun (çukurun ortasına inmek) ilk 3 cümlede değil ancak 5. cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Koştu ve zıpladı ama suyun tam ortasına indi"
   - Cümle 5: «Koştu ve zıpladı ama suyun tam ortasına indi.»
   - Açıklama: Sorun ancak beşinci cümlede ortaya çıkıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Koştu ve zıpladı ama suyun tam ortasına indi"
   - Cümle 5: «Koştu ve zıpladı ama suyun tam ortasına indi.»
   - Açıklama: Doru'nun neden çukurun ortasına indiği söylenmiyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama ıslanmaktan korkmadı"
   - Cümle 9: «Ama ıslanmaktan korkmadı.»
   - Açıklama: Önceki cümlede Doru güldüğü için 'ama' bağlacı karşıtlık kurmuyor, yanlış anlamda kullanılmış.
   - Açıklama: 'Ama' bir önceki cümleyle karşıtlık kurmuyor; bağlaç yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0177` birebir aynı, `@degisim: yardımlaşmak -> zıplamak` (tutuyorsan), ardından `@onarim: 6a467e39887b14c1da5c118a59ec5095a9ac2ce7`, sonra gövde.

### Hikâye 10: tohum doru-0178 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0178
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'brokoli', fiil 'sunmak', sıfat 'sabırsız'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: çalıdan bilinmeyen tık tık sesleri geldi | cesaretle çalıya gidip düşen kozalakları gördü
@tohum: doru-0178
@degisim: sunmak -> düşürmek
Doru ormanda yavaşça yürüyordu. Birden yakındaki bir çalıdan tık tık sesleri geldi. Çalı brokoli gibi yuvarlak ve yeşildi. Doru sesin ne olduğunu çok merak etti ve sabırsızlandı. Ses çok yakındı ama Doru korkmadı. Cesaretle çalıya yaklaştı ve dallarına baktı. Tam o sırada yukarıdan bir kozalak düştü. Kozalak çalının dallarına çarptı ve tık diye ses çıkardı. Doru başını kaldırdı. Çalının üstünde büyük bir çam ağacı vardı. Rüzgar esince ağaç kozalaklarını düşürüyordu. Sesi yapan bu kozalaklardı. Doru bundan sonra tık tık sesini duyunca hemen yukarıdaki kozalaklara baktı.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Çalı brokoli gibi yuvarlak"
   - Cümle 3: «Çalı brokoli gibi yuvarlak ve yeşildi.»
   - Açıklama: Brokoli kartın doğa dünyasında olmayan bir mutfak nesnesi; kapalı dünya kuralına aykırı.
   - Açıklama: Brokoli kartın doğa dünyasına ait değil; tohum yasak kategorilerindeki mutfak ve yiyecek öğesi dünyaya giriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalı brokoli gibi yuvarlak ve yeşildi"
   - Cümle 3: «Çalı brokoli gibi yuvarlak ve yeşildi.»
   - Açıklama: Brokoli sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok merak etti ve sabırsızlandı"
   - Cümle 4: «Doru sesin ne olduğunu çok merak etti ve sabırsızlandı.»
   - Açıklama: 'sabırsızlandı' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Sabırsızlandı' soyut bir duygu kelimesidir ve 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0178` birebir aynı, `@degisim: sunmak -> düşürmek` (tutuyorsan), ardından `@onarim: 0f76b290c301988fc1f7d64d3535f36b1378552f`, sonra gövde.

### Hikâye 11: tohum doru-0179 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0179
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'köpük', fiil 'dökmek', sıfat 'somurtkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük at karı ilk kez gördü ve basmak istemedi | önce kendisi cesaretle kara basıp gösterdi
@tohum: doru-0179
@degisim: köpük -> kar
Dağda ilk kar yağmıştı ve her yer bembeyazdı. Doru ile Alaca karı ilk kez görüyordu. Alaca kenarda somurtkan bir yüzle duruyordu. "Kar çok garip, ona basmak istemiyorum," dedi Alaca. Doru da karı hiç tanımıyordu ama korkmadı. Cesaretle karın üstüne ilk adımı attı. Kar ayaklarının altında çok yumuşaktı. Doru düz bir yerde bir tur koştu ve karda yuvarlandı. Sonra kalktı, başını salladı ve sırtındaki karı döktü. "Gel, Alaca, çok eğlenceli!" dedi Doru. Alaca yavaşça kara bastı ve birden güldü. Sonra o da Doru'nun yanında karda yuvarlandı. Doru bundan sonra Alaca yeni bir şeyden korkunca ilk adımı kendisi attı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "önce kendisi cesaretle kara"
   - Cümle 0 (plan satırı): «küçük at karı ilk kez gördü ve basmak istemedi | önce kendisi cesaretle kara basıp gösterdi»
   - Açıklama: Plan satırında sorunun öznesi küçük at, çözümdeki 'kendisi' kimi gösterdiği belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "somurtkan bir yüzle duruyordu"
   - Cümle 3: «Alaca kenarda somurtkan bir yüzle duruyordu.»
   - Açıklama: 'Somurtkan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ilk adımı kendisi attı"
   - Cümle 13: «Doru bundan sonra Alaca yeni bir şeyden korkunca ilk adımı kendisi attı.»
   - Açıklama: Sonraki alışkanlık anlatılırken '-dı' uygun değil; 'ilk adımı hep kendisi atardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0179` birebir aynı, `@degisim: köpük -> kar` (tutuyorsan), ardından `@onarim: ada52a35bae0f1bebb22473db8b36a8960d3c147`, sonra gövde.

### Hikâye 12: tohum doru-0180 (deneme 1 -> 2)

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
@plan: boş köşe için hiç tohumları yoktu | cesaretle çalılardan geçip tohum dolu bir çiçek getirdi
@tohum: doru-0180
@degisim: külah -> tohum
Çayırda Doru ile Karatay bahçe yapma oyunu oynuyordu. Çayırın bir köşesinde hiç çiçek yoktu. Oraya çiçek ekmek istediler ama hiç tohumları yoktu. Doru sık çalıların arkasındaki beyaz, yumuşak çiçekleri hatırladı. O çiçeklerin üstünde bir sürü küçük tohum vardı. Çalıların arkası hiç görünmüyordu. "Ben oraya gitmem, Doru," dedi Karatay. Doru korkmadı ve cesaretle çalıların arasından geçti. Beyaz çiçeklerden birini ağzıyla kopardı ve geri getirdi. İkisi çiçeğe birlikte üfledi ve tohumları boş köşeye saçtı. Küçük tohumlar havada uçtu ve yere indi. "Belki burada yakında çiçekler çıkar," dedi Karatay umutlu bir sesle. Doru çok sevindi, çünkü boş köşede artık tohumlar vardı.
```

**Hakem bulguları (4):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "bahçe yapma oyunu oynuyordu"
   - Cümle 1: «Çayırda Doru ile Karatay bahçe yapma oyunu oynuyordu.»
   - Açıklama: Kartın kimlik cümlesindeki özgür at sürüsü dünyasında atların bahçe yapıp çiçek ekmesi diziye yabancı bir bilgidir.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda Doru ile Karatay"
   - Cümle 1: «Çayırda Doru ile Karatay bahçe yapma oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve geçiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle çalıların arasından geçti"
   - Cümle 8: «Doru korkmadı ve cesaretle çalıların arasından geçti.»
   - Açıklama: Arkası görünmeyen sık çalıların arasına tek başına girmek çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Arkadaşı gitmezken arkası görünmeyen sık çalılara tek başına girmek çocuğun taklit edebileceği riskli bir davranıştır.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Karatay umutlu bir sesle"
   - Cümle 12: «"Belki burada yakında çiçekler çıkar," dedi Karatay umutlu bir sesle.»
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Umutlu bir sesle' soyut bir anlatım ve 3 yaşındaki çocuğun bildiği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0180` birebir aynı, `@degisim: külah -> tohum` (tutuyorsan), ardından `@onarim: e677432063b3a605038cf62b6c6fe62dcfaec5e8`, sonra gövde.
