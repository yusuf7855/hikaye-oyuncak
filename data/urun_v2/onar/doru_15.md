# Editör görevi (onarım): Doru, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0051 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0051
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kök', fiil 'rahatlamak', sıfat 'meşgul'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: yolun ortasında uzun ve kara bir şey duruyordu | cesaretle yaklaştı ve onun bir kök olduğunu gördü
@tohum: doru-0051
@degisim: meşgul -> taze
Ormanda hafif bir rüzgar esiyordu. Doru keşif oyunu oynuyordu ve büyük meşe ağacına gidiyordu. Ama yolun ortasında uzun, kıvrımlı ve kara bir şey duruyordu. Doru onun ne olduğunu bilmiyordu. "Anne, yolda ne var?" diye sordu Doru. Annesi yakında taze çimen yiyordu. Hemen gelip Doru'nun yanında durdu. "Gel, birlikte bakalım," dedi annesi. Doru cesaretle kara şeye yaklaştı ve onun bir ağaç kökü olduğunu gördü. Doru rahatladı ve güldü. Kökün üstünden hopladı ve ağaca ulaştı. "Anne, ağaca vardım!" dedi Doru. Annesi gülümsedi ve Doru keşif oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "uzun, kıvrımlı ve kara bir şey"
   - Cümle 3: «Ama yolun ortasında uzun, kıvrımlı ve kara bir şey duruyordu.»
   - Açıklama: Yolda duran bilinmeyen uzun, kıvrımlı, kara şey yılan çağrışımıyla korkutucu bir öğe kuruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0051` birebir aynı, `@degisim: meşgul -> taze` (tutuyorsan), ardından `@onarim: eea257e476d34ae22dbb9869a44fe7e400293d0c`, sonra gövde.

### Hikâye 2: tohum doru-0052 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0052
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kozalak', fiil 'dinlemek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük arkadaşı kayanın arkasındaki kozalakları göremedi | onu kayanın arkasına götürdü ve kozalakları gösterdi
@tohum: doru-0052
Bir sabah dağ çok sessizdi. Doru ile Alaca büyük bir kayanın yanında dinleniyordu. Birden aşağıdan sesler geldi ama küçük Alaca kayanın arkasını göremedi. Doru sesi dikkatle dinledi ve kayanın üstünden baktı. Çam ağaçlarından düşen kozalaklar aşağı yuvarlanıyordu. Doru küçük arkadaşına yardım etti. Onu kayanın arkasına götürdü. Oradan kozalaklar iyi görünüyordu. Bir kozalak daha tık tık zıplayarak yuvarlandı. Alaca heyecanla kozalakları tek tek saydı. Doru çok sevindi, çünkü Alaca da kozalakları sonunda görmüştü.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük Alaca kayanın arkasını göremedi"
   - Cümle 3: «Birden aşağıdan sesler geldi ama küçük Alaca kayanın arkasını göremedi.»
   - Açıklama: Kozalakları görememek önemsiz bir olay; sorun çocuğun önemseyeceği bir güçlük değil.
   - Açıklama: Yuvarlanan kozalakları görememek çocuğun önemseyeceği bir sorun değil ve Alaca bunu dert etmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0052` birebir aynı, ardından `@onarim: 01bf35245a55a9cb483706e17ed711bac476e208`, sonra gövde.

### Hikâye 3: tohum doru-0053 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: tatlı bir kokunun nereden geldiğini merak etti | dar yola cesaretle girdi ve çilekleri buldu
@tohum: doru-0053
@degisim: çan -> çilek
Rüzgar ağaçların arasında yavaşça esiyordu. Doru ormanın kenarında taze otları yiyordu. Birden rüzgarla birlikte tatlı bir koku geldi. Doru başını kaldırdı ve havayı kokladı. Bu kokunun nereden geldiğini çok merak etti. Koku, sık ağaçların arasındaki dar bir yoldan geliyordu. Yol çok karanlıktı. Doru bir an durdu, sonra cesaretle yola girdi. Dalları dikkatlice itti ve ilerledi. Yolun sonunda güneşli, küçük bir açıklık vardı. Açıklıkta her yer çilekle doluydu. Çilekler güneşte kızarmıştı ve çok güzelleşmişti. Koku işte bu çileklerden geliyordu. Doru çileklerden afiyetle yedi. Sonra güneşin altında mutlu mutlu dinlendi.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tatlı bir kokunun nereden geldiğini merak etti"
   - Cümle 0 (plan satırı): «tatlı bir kokunun nereden geldiğini merak etti | dar yola cesaretle girdi ve çilekleri buldu»
   - Açıklama: Bir kokuyu merak etmek çözülmesi gereken gerçek bir sorun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Bu kokunun nereden geldiğini çok merak etti"
   - Cümle 5: «Bu kokunun nereden geldiğini çok merak etti.»
   - Açıklama: Plandaki sorun olan merak ilk üç cümlede değil beşinci cümlede söyleniyor.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Yol çok karanlıktı"
   - Cümle 7: «Yol çok karanlıktı.»
   - Açıklama: Karanlık orman yolu küçük çocuk için korkutucu bir öğe.
   - Açıklama: Tek başına karanlık bir yola girme sahnesi küçük çocuk için korkutucu bir öğe taşıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sonra cesaretle yola girdi"
   - Cümle 8: «Doru bir an durdu, sonra cesaretle yola girdi.»
   - Açıklama: Tek başına karanlık ve dar bir orman yoluna girmek taklit edilince tehlikeli.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve çok güzelleşmişti"
   - Cümle 12: «Çilekler güneşte kızarmıştı ve çok güzelleşmişti.»
   - Açıklama: 'Güzelleşmek' çileğin olgunlaşması için yanlış seçilmiş bir kelime.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru çileklerden afiyetle yedi"
   - Cümle 14: «Doru çileklerden afiyetle yedi.»
   - Açıklama: Ormanda bulunan yabani meyveyi yemek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0053` birebir aynı, `@degisim: çan -> çilek` (tutuyorsan), ardından `@onarim: a9e52136c25f30f43de0ecf0d39a08c4e6b0b868`, sonra gövde.

### Hikâye 4: tohum doru-0054 (deneme 1 -> 2)

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
@plan: kayanın dibindeki elmaların çoğu yokuştan aşağı yuvarlandı | elmaları buldu ve kütükten cesaretle çıkardı
@tohum: doru-0054
@degisim: portakal -> elma
Doru, Kırat ile dağda yürüyordu. Kırat sürü için büyük bir kayanın dibine elma toplamıştı. Ama elmaların çoğu yokuştan aşağı yuvarlanmış ve kaybolmuştu. "Elmalarım kayboldu, Doru," dedi Kırat. Doru yere baktı. Çimenin üstünde dağınık birkaç elma vardı. Doru bu elmaların gittiği yoldan yavaşça yürüdü. Yolun sonunda içi boş, kocaman bir kütük vardı. Kütüğün içi çok karanlıktı. Doru bir an durdu. Sonra cesaretle başını kütüğün içine uzattı. Kayıp elmalar orada, yan yana duruyordu! Doru elmaları ağzıyla tek tek dışarı çıkardı. Sonra hepsini taşıdı ve kayanın yanındaki elmalara ekledi. "Teşekkürler, Doru, sürü bu elmalara çok sevinecek!" dedi Kırat.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "elmaların çoğu yokuştan aşağı yuvarlanmış ve kaybolmuştu"
   - Cümle 3: «Ama elmaların çoğu yokuştan aşağı yuvarlanmış ve kaybolmuştu.»
   - Açıklama: Elmaların neden yuvarlandığı söylenmiyor; sorunun sebebi verilmiyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Kütüğün içi çok karanlıktı"
   - Cümle 9: «Kütüğün içi çok karanlıktı.»
   - Açıklama: Karanlık kovuk önünde duraksama küçük çocuk için korku gerilimi yaratıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle başını kütüğün içine uzattı"
   - Cümle 11: «Sonra cesaretle başını kütüğün içine uzattı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde karanlık bir oyuğa baş sokuluyor.
   - Açıklama: Karanlık bir kovuğa başını sokmak çocuğun taklit edebileceği tehlikeli bir davranış olarak övülüyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kayıp elmalar orada, yan yana duruyordu"
   - Cümle 12: «Kayıp elmalar orada, yan yana duruyordu!»
   - Açıklama: Yokuştan yuvarlanan elmaların karanlık kütüğün içinde yan yana dizilmiş bulunması sebepsiz ve çözümü kolaylaştıran bir tesadüf.
   - Açıklama: Yokuştan yuvarlanan elmaların kütüğün içinde yan yana dizilmiş bulunması sebepsiz ve çözümü kolaylaştırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0054` birebir aynı, `@degisim: portakal -> elma` (tutuyorsan), ardından `@onarim: 69b1db87ff780281bce315d79a00cbff9d7727e5`, sonra gövde.

### Hikâye 5: tohum doru-0055 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0055
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'balkabağı', fiil 'bükmek', sıfat 'minik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesinin kuyruğu çalının dallarına takıldı | dalları ağzıyla büktü ve kuyruğu kurtardı
@tohum: doru-0055
@degisim: balkabağı -> çalı
Dağdaki geniş çayırda Doru ile annesi saklambaç oynuyordu. Annesi büyük bir çalının arkasına saklandı. Ama kuyruğu çalının minik dallarına takıldı. Annesi kuyruğunu salladı ama dallardan kurtulamadı. Doru çalının etrafında dolaştı ve annesini buldu. "Anneciğim, seni buldum!" dedi Doru. "Buldun ama çıkamıyorum, kuyruğum dallara takıldı," dedi annesi. Doru hemen annesinin yardımına koştu. Bir dalı ağzıyla tuttu ve yavaşça geriye büktü. Sonra öbür dalı da büktü. Annesinin kuyruğu dallardan kurtuldu. Annesi Doru'ya gülümsedi. "Teşekkürler, Doru, şimdi saklanma sırası sende!" dedi annesi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "annesinin yardımına koştu"
   - Cümle 8: «Doru hemen annesinin yardımına koştu.»
   - Açıklama: 'Yardımına koşmak' deyimsel bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hemen annesinin yardımına koştu"
   - Cümle 8: «Doru hemen annesinin yardımına koştu.»
   - Açıklama: Doru zaten yanında olduğu için 'yardımına koştu' gerçek koşma değil, deyimsel kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0055` birebir aynı, `@degisim: balkabağı -> çalı` (tutuyorsan), ardından `@onarim: 3345bd9171a9ca8073d838726039e4a071015de8`, sonra gövde.

### Hikâye 6: tohum doru-0056 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0056
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kabak', fiil 'uçuşmak', sıfat 'yuvarlak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: oynadığı taş bir kayaya çarpıp çalılara doğru yuvarlandı | çayırda hızla koştu ve taşı çalılardan önce durdurdu
@tohum: doru-0056
@degisim: kabak -> taş
Güneş dağların üstünde parlıyordu. Doru vadide yuvarlak, beyaz bir taşı burnuyla itip oynuyordu. Birden taş küçük bir kayaya çarptı ve sık çalılara doğru yuvarlandı. Doru en sevdiği taşı kaybetmek istemedi. Düz çayırın üstünde hızla koştu. Yerdeki kuru yapraklar arkasında havada uçuştu. Bir yaprak Doru'nun burnuna kondu ama Doru durmadı. Doru taştan önce çalılara vardı. Taş gelince onu ayağıyla durdurdu. Doru taşı burnuyla çayırın ortasına geri itti. Sonra yeniden oyununa başladı. Doru taşını kurtardığı için çok sevindi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir yaprak Doru'nun burnuna kondu"
   - Cümle 7: «Bir yaprak Doru'nun burnuna kondu ama Doru durmadı.»
   - Açıklama: Uçuşan yapraklar ve buruna konan yaprak hiçbir işe yaramayan ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir yaprak Doru'nun burnuna kondu ama Doru durmadı"
   - Cümle 7: «Bir yaprak Doru'nun burnuna kondu ama Doru durmadı.»
   - Açıklama: Burna konan yaprak bir engel gibi kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0056` birebir aynı, `@degisim: kabak -> taş` (tutuyorsan), ardından `@onarim: d3ef5ae5b8d770bb3d1bd5900d2d3d7253f68bfa`, sonra gövde.

### Hikâye 7: tohum doru-0058 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0058
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'kiraz', fiil 'uyanmak', sıfat 'kısa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: yağmur geliyordu ve küçük arkadaşı açık yerde uyuyordu | hızla koşup onu kaldırdı ve ağacın altına götürdü
@tohum: doru-0058
Bir sabah geniş çayırda Doru bir kiraz ağacının altında otluyordu. Alaca ise çayırın öbür ucunda, açık bir yerde uyuyordu. Birden koyu bulutlar geldi ve yağmur yaklaştı. Alaca yağmuru hiç sevmiyordu. Doru düz çayırda hızla koştu. Alaca'nın yanına geldi ve onu burnuyla dürttü. "Alaca, kalk, yağmur geliyor!" dedi Doru. Alaca hemen uyandı ve bulutlara baktı. "Kiraz ağacının altına gidelim," dedi Doru. İkisi birlikte ağacın altına koştu. Tam o anda yağmur başladı. Yağmur kısa sürdü. Sonra yere düşen kirazları birlikte yediler. Alaca çok mutluydu, çünkü Doru sayesinde kuru kalmıştı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bir sabah geniş çayırda Doru"
   - Cümle 1: «Bir sabah geniş çayırda Doru bir kiraz ağacının altında otluyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlayıp bitiyor.
   - Açıklama: Başlıktaki yer park ama hikaye geniş bir çayırda geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çünkü Doru sayesinde kuru"
   - Cümle 14: «Alaca çok mutluydu, çünkü Doru sayesinde kuru kalmıştı.»
   - Açıklama: 'Sayesinde' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0058` birebir aynı, ardından `@onarim: 41e66858b31c8d3afe1c85638a6cf2ed877e1474`, sonra gövde.

### Hikâye 8: tohum doru-0059 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0059
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'külah', fiil 'tamamlanmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: turuncu çiçekler vadinin öbür ucunda açmıştı | hızla koşup çiçekleri getirdi ve etrafına dizdi
@tohum: doru-0059
@degisim: külah -> çiçek
Dağdaki düz bir yerde Kırat bir kayanın yanında uyuyordu. Doru ona en sevdiği turuncu çiçeklerden bir sürpriz yapmak istedi. Ama turuncu çiçekler vadinin öbür ucundaydı ve Kırat'ın uykusu hafifti. Doru düz vadide hızla koştu. Çiçeklerin yanına geldi ve ağzıyla bir demet çiçek kopardı. Sonra çiçekleri ağzında taşıyarak geri döndü. Çiçekleri Kırat'ın çevresine tek tek dizdi. Sonunda turuncu çiçeklerden bir halka tamamlandı. Tam o anda Kırat gözlerini açtı. "Sürpriz, Kırat!" dedi Doru. Kırat çiçeklere baktı ve güldü. "Ne güzel bir sürpriz, çok teşekkür ederim, Doru!" dedi Kırat.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çiçekleri getirdi ve etrafına dizdi"
   - Cümle 0 (plan satırı): «turuncu çiçekler vadinin öbür ucunda açmıştı | hızla koşup çiçekleri getirdi ve etrafına dizdi»
   - Açıklama: Plan satırında 'etrafına' zamirinin kimi gösterdiği belli değil; özne Doru olduğu için Doru'nun kendi etrafı gibi okunuyor, oysa Kırat'ın etrafı kastediliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kırat'ın uykusu hafifti"
   - Cümle 3: «Ama turuncu çiçekler vadinin öbür ucundaydı ve Kırat'ın uykusu hafifti.»
   - Açıklama: 'Uykusu hafif' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Uykusu hafif' deyimsel bir anlatım ve 3 yaşındaki bir çocuğun anlayacağı somut bir ifade değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "turuncu çiçekler vadinin öbür ucundaydı"
   - Cümle 3: «Ama turuncu çiçekler vadinin öbür ucundaydı ve Kırat'ın uykusu hafifti.»
   - Açıklama: Çiçeklerin uzakta olması gerçek bir sorun değil; Doru yalnız koşup getiriyor ve sorun önemsiz kalıyor.
   - Açıklama: Çiçeklerin uzakta olması gerçek bir sorun değil; Doru yalnızca gidip getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kırat'ın uykusu hafifti"
   - Cümle 3: «Ama turuncu çiçekler vadinin öbür ucundaydı ve Kırat'ın uykusu hafifti.»
   - Açıklama: Hafif uyku işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0059` birebir aynı, `@degisim: külah -> çiçek` (tutuyorsan), ardından `@onarim: 1a9c1cfba10b40f262f620dab96bc37cc22906df`, sonra gövde.

### Hikâye 9: tohum doru-0061 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0061
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'yonca', fiil 'uyutmak', sıfat 'bomboş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: sıcak güneşte en sevdiği yerdeki yonca kurumuştu | yeri bilen atın yanına gidip sordu ve oraya koştu
@tohum: doru-0061
@degisim: uyutmak -> sormak
Kuşlar vadide neşeyle ötüyordu. Doru'nun karnı bomboştu ve en sevdiği yonca yerine geldi. Ama güneş çok sıcaktı ve bütün yonca kurumuştu. Doru başka bir yonca yeri bilmiyordu. Biraz ileride Kırat bir kayanın gölgesinde dinleniyordu. Doru, Kırat'ın yanına gitti. "Kırat, taze yonca nerede var?" diye sordu Doru. "Vadinin öbür ucunda, büyük çam ağacının yanında taze yonca var," dedi Kırat. Doru, Kırat'a teşekkür etti. Sonra düz vadide hızla koştu. Büyük çam ağacının yanında yemyeşil yonca vardı. Doru karnını doyurdu. Doru çok sevindi, çünkü Kırat ona doğru yeri göstermişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Doru'nun karnı bomboştu ve en sevdiği yonca yerine geldi"
   - Cümle 2: «Doru'nun karnı bomboştu ve en sevdiği yonca yerine geldi.»
   - Açıklama: Özne uyumsuz; 'karnı' öznesi 'geldi' fiiline bağlanıyor ve 'yonca yerine' 'yonca yerine (yerini tutarak)' diye de okunabiliyor.
   - Açıklama: İkinci yüklemin öznesi 'karnı' olarak kalıyor; özne uyumu bozuk.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kırat ona doğru yeri göstermişti"
   - Cümle 13: «Doru çok sevindi, çünkü Kırat ona doğru yeri göstermişti.»
   - Açıklama: 'Ona doğru' yön anlamıyla da okunabiliyor; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0061` birebir aynı, `@degisim: uyutmak -> sormak` (tutuyorsan), ardından `@onarim: fcc2e861040c43853193ac508d9c3bca9727f2e4`, sonra gövde.

### Hikâye 10: tohum doru-0062 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0062
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'filiz', fiil 'çekmek', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: son kütüğün üstünde değişik bir şekil vardı | cesaretle yaklaştı ve kuru dalı kenara çekti
@tohum: doru-0062
Hafif bir yağmur yeni dinmişti. Doru ormanda yerdeki küçük kütüklerin üstünden atlama oyunu oynuyordu. Ama son kütüğün üstünde değişik, uzun bir şekil vardı ve Doru durdu. Şekil kıpırdamıyordu ama çok garip görünüyordu. Doru biraz çekindi, sonra cesaretle yaklaştı. Bu, rüzgarın kütüğün üstüne düşürdüğü kuru bir daldı. Doru dalı ağzıyla tuttu ve kenara çekti. Dalın altında minicik, yeşil bir filiz vardı. Dal ağırdı ama filiz kırılmamıştı. Doru ona basmadan son kütüğün üstünden de atladı. Doru çok sevindi, çünkü hem oyununu bitirmişti hem de küçük filizi kurtarmıştı.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Şekil kıpırdamıyordu ama çok garip görünüyordu"
   - Cümle 4: «Şekil kıpırdamıyordu ama çok garip görünüyordu.»
   - Açıklama: Kütüğün üstündeki uzun, garip şekil yılan gibi korkutucu bir gerilim yaratıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru biraz çekindi"
   - Cümle 5: «Doru biraz çekindi, sonra cesaretle yaklaştı.»
   - Açıklama: 'Çekinmek' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dalın altında minicik, yeşil bir filiz vardı"
   - Cümle 8: «Dalın altında minicik, yeşil bir filiz vardı.»
   - Açıklama: Filiz sebepsiz beliriyor ve sona 'kurtarmıştı' diye ikinci bir başarı olarak ekleniyor, oysa Doru onu kurtarmak için bir şey yapmadı.
   - Açıklama: Filiz sebepsiz beliriyor ve sonda hikayenin hedefine sonradan eklenen ikinci bir kurtarma gibi sunuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0062` birebir aynı, ardından `@onarim: c9a252acf5aaef01fbe7e6d199232149c2839cff`, sonra gövde.

### Hikâye 11: tohum doru-0063 (deneme 1 -> 2)

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
Dağda yumuşak bir çimen vardı ve orada benekli çiçekler açmıştı. Doru çimene yattı ve sağa sola yuvarlandı. Ama kuru, dikenli tohumlar sırtına yapıştı. Doru kendini salladı ama tohumlar düşmedi. Ağzı da sırtına yetişmedi. Doru annesine gitti ve tohumları almasını istedi. Annesi tohumları dişleriyle tek tek aldı. Doru cesaretle hiç kıpırdamadan durdu. Sonunda son tohum da yere düştü. Sonra annesi Doru'nun tüylerini burnuyla düzeltti ve güzelleştirdi. Doru ile annesi benekli çiçeklerin yanında mutlu mutlu otladı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru cesaretle hiç kıpırdamadan durdu"
   - Cümle 8: «Doru cesaretle hiç kıpırdamadan durdu.»
   - Açıklama: Tohumdaki cesaret özelliği sorunu çözmüyor; sorunu annesi çözüyor, özellik işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0063` birebir aynı, ardından `@onarim: 09d9b7a38093ef90717bf3cfe22b3bcfd951a8f4`, sonra gövde.

### Hikâye 12: tohum doru-0064 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0064
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çekirdek', fiil 'homurdanmak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: koşarken arkadaşının yaprak yığınını dağıttı | cesaretle özür diledi ve yığını birlikte yeniden yaptılar
@tohum: doru-0064
@degisim: çekirdek -> yaprak
Bir sabah Doru ile Karatay ormanda oynuyordu. Karatay içine atlamak için kuru yapraklardan kocaman bir yığın yapıyordu. Ama Doru koşarken yığını görmedi ve yaprakların içinden geçti. Yapraklar her yere dağıldı. Karatay ağzı yaprakla dolu geri geldi ve yığını gördü. Karatay kızdı ve homurdandı. Doru önce ne yapacağını bilemedi. Sonra cesaretle arkadaşının yanına gitti ve ondan özür diledi. Karatay başını salladı ve gülümsedi. Sonra ikisi birlikte yaprakları topladı. Yeni yığın ilk yığından da büyük oldu. Karatay koştu ve yığının içine atladı. Doru da hemen onun arkasından atladı. Doru çok mutluydu, çünkü arkadaşı artık ona kızgın değildi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geri geldi ve yığını gördü"
   - Cümle 5: «Karatay ağzı yaprakla dolu geri geldi ve yığını gördü.»
   - Açıklama: Yığın dağılmış olduğu için 'yığını gördü' yanlış; dağılan yaprakları görmüş olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0064` birebir aynı, `@degisim: çekirdek -> yaprak` (tutuyorsan), ardından `@onarim: 33ccc166eae4ca2b64ca9151d16e308ae71d4dee`, sonra gövde.
