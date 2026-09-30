# Editör görevi (onarım): Niloya, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Niloya | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar41.txt --ad urun_v2`
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

## Kart: Niloya (kaynaklı, kapalı dünya)

- Ad: Niloya (okunuş: niloya; kesme eki okunuşa uyar)
- Kimlik: Niloya, nehir kenarındaki bir köyde ailesiyle yaşayan küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Niloya'nın merakı bakarak, sorarak ve bir büyüğe haber vererek gösterilir; nehre ya da dereye girmez, suya yalnız kıyıdan bakar; ağaca ya da yüksek yere tırmanmaz.
- Özellikler:
  - keşfet: Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever. (örnek biçimler: merak etti, merakla, keşfetti)
  - soru: Merak ettiği her şeyi sorar. (örnek biçimler: sordu, soruyu, sorular)
  - şarkı: Şarkı söylemeyi çok sever. (örnek biçimler: şarkı, şarkısını)
- Yerler:
  - orman: Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.
  - dağ: Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.
  - ev: Niloya'nın nehir kenarındaki köy evi ve bahçesi.
  - park: Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Murat: Niloya'nın ağabeyi; küçük kardeşi Niloya'yı çok sever. Tür: oğlan; konuşur; huy: Top oynamayı, koşturmayı ve fındık toplamayı sever.. Yüzey biçimleri: Murat, ağabey, ağabeyi, abi, abisi, abiciğim
  - Mete: Murat'ın en yakın arkadaşı; Niloya ile aynı yaştadır ve onun da arkadaşıdır. Tür: oğlan; konuşur; huy: Oyuncaklarını dağıtır, sonra aradığını bulamaz.. Yüzey biçimleri: Mete
  - Tospik: Niloya'nın kaplumbağası ve en yakın arkadaşı. Tür: kaplumbağa; konuşur; huy: Oyun oynamayı ve uyumayı sever; Niloya'ya yetişmekte zorlanır.. Yüzey biçimleri: Tospik, kaplumbağa, kaplumbağası
  - dedesi: Niloya'nın dedesi; herkese iyi öğütler verir. Tür: dede; konuşur. Yüzey biçimleri: dede, dedesi, dedeciğim, Dede
  - babaannesi: Niloya'nın babaannesi; yemek yapmayı ve fındık toplamayı sever. Tür: babaanne; konuşur. Yüzey biçimleri: babaanne, babaannesi, babaanneciğim, Babaanne, nine, ninesi
  - annesi: Niloya'nın annesi; yemek yapmayı, ekinleri ve yaylayı sever. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
- Dünya kuralları:
  - Niloya'nın ağabeyi Murat'tır. Mete Niloya'nın ağabeyi değildir; Murat'ın arkadaşıdır.
  - Tospik yavaştır; Niloya'ya yetişmekte zorlanır, hızla koşmaz.
  - Köy nehir kenarındadır; hikayede kimse nehre ya da dereye girmez, suya kıyıdan bakılır.
- Yasak adlar: Elif, Mine, Fatoş, Cem, Ayşecik, Sarıkanat, Miniş
- Yasak: Babası kartta yok; hikayeye girmez (kapalı dünya).
- İzinli dünya kelimeleri: köy, nehir, yayla, fındık, kaplumbağa, kekik

## Onarılacak hikâyeler

### Hikâye 1: tohum niloya-0051 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0051
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: dedesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'palmiye', fiil 'uzanmak', sıfat 'ince'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: dedesinin sepeti devrildi ve fındıklar çalının altına yuvarlandı | yere uzanıp fındıkları ince bir dalla dışarı çekti
@tohum: niloya-0051
@degisim: palmiye -> sepet
Ormanda kuşlar cıvıl cıvıl ötüyordu. Niloya ile dedesi fındık topluyordu. Dedesi sepeti bir taşın üstüne koydu ama sepet kaydı ve devrildi. Fındıklar alçak bir çalının altına yuvarlandı. "Benim kolum oraya yetişmiyor," dedi dedesi. "Ben bakarım, dedeciğim," dedi Niloya. Niloya çalının altına merakla baktı. Dibinde kahverengi fındıklar duruyordu. Niloya ince bir dal aldı. Sonra Niloya yere uzandı ve fındıkları dalla dışarı çekti. Fındıkları tek tek topladı ve sepete koydu. Sepet yine doldu. Dedesi gülümsedi ve Niloya'nın başını okşadı. "Aferin, Niloya, sen olmasaydın bu fındıklar orada kalırdı!" dedi dedesi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra Niloya yere uzandı"
   - Cümle 10: «Sonra Niloya yere uzandı ve fındıkları dalla dışarı çekti.»
   - Açıklama: Arka arkaya cümlelerde 'Niloya' adı gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0051` birebir aynı, `@degisim: palmiye -> sepet` (tutuyorsan), ardından `@onarim: 184ebf49e873d2370afd372f00214193ef735a65`, sonra gövde.

### Hikâye 2: tohum niloya-0073 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0073
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'halka', fiil 'sürmek', sıfat 'sevimli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: halka belinde dönmedi ve hep yere düştü | şarkı söyleyip belini yavaşça salladı
@tohum: niloya-0073
@degisim: sevimli -> renkli
Bir sabah Niloya yaylaya büyük renkli bir halka getirdi. Halkayı belinde çevirmeyi ilk kez deneyecekti. Ama halka hemen yere düştü, çünkü Niloya belini çok hızlı sallıyordu. Niloya halkayı yerden aldı ve biraz düşündü. Sonra neşeli bir şarkı söylemeye başladı. Şarkıyı söylerken belini yavaş yavaş salladı. Bu sefer halka düşmedi ve Niloya'nın etrafında döndü. Şarkı uzun sürdü, halka da uzun uzun döndü. Niloya şarkı bitene kadar hiç durmadı. Niloya çok sevindi, çünkü halkayı çevirmeyi sonunda öğrenmişti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "belini yavaş yavaş salladı"
   - Cümle 6: «Şarkıyı söylerken belini yavaş yavaş salladı.»
   - Açıklama: Çözüm söylenen sebebe (yeşil çimenler) yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0073` birebir aynı, `@degisim: sevimli -> renkli` (tutuyorsan), ardından `@onarim: c04f86384a4446e50e1e02035aa071587a7f782a`, sonra gövde.

### Hikâye 3: tohum niloya-0094 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0094
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'sayfa', fiil 'sıkışmak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: ikisi aynı anda şarkı söyledi ve sesler karıştı | şarkıları sırayla söylemeyi önerdi
@tohum: niloya-0094
@degisim: konuşkan -> neşeli
Bir sabah Niloya ile dedesi ormanda fındık ağaçlarının altına oturdu. Niloya, dedesinin resimli şarkı kitabını görmek için yanına sıkıştı. İkisi aynı anda şarkıya başladı ve sesleri birbirine karıştı. Niloya biraz düşündü. "Dede, sırayla söyleyelim, bir şarkı ben, bir şarkı sen," dedi Niloya. Niloya ilk sayfayı açtı ve oradaki neşeli şarkıyı söyledi. Dedesi onu sessizce dinledi. Sonra dedesi öbür şarkıyı söyledi. Bu kez iki şarkı da çok güzel oldu. Niloya bundan sonra şarkıları dedesiyle hep sırayla söyledi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "İkisi aynı anda şarkıya başladı ve sesleri birbirine karıştı"
   - Cümle 3: «İkisi aynı anda şarkıya başladı ve sesleri birbirine karıştı.»
   - Açıklama: Birlikte şarkı söylemek normalde sorun değil ve seslerin neden karıştığı, örneğin farklı şarkılar söyledikleri, söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0094` birebir aynı, `@degisim: konuşkan -> neşeli` (tutuyorsan), ardından `@onarim: de3a4cff0e78486016b1bdadc6eeae0fcb200373`, sonra gövde.

### Hikâye 4: tohum niloya-0095 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0095
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'anahtar', fiil 'işaretlemek', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: anahtar cebinden düştü ve karda kayboldu | yürüdüğü yere dönüp karda anahtarı buldu
@tohum: niloya-0095
@degisim: havalı -> beyaz
Kar sessizce yağıyordu. Niloya evin bahçesinde beyaz karda yürüyordu. Eldivenini cebinden çıkarınca evin anahtarı düştü ve kayboldu. Kapıyı bu anahtar açıyordu. Niloya durdu ve bir soru düşündü: Anahtar nereye düşmüştü? Sonra yürüdüğü yere geri döndü. Yerden bir dal aldı ve karda tek tek baktı. Baktığı her yeri dalla işaretledi. Böylece hiçbir yere iki kez bakmadı. Bir yerde karda küçük bir delik gördü. Niloya deliğe elini soktu ve anahtarı çıkardı. Niloya çok sevindi, çünkü anahtarı kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "karda tek tek baktı"
   - Cümle 7: «Yerden bir dal aldı ve karda tek tek baktı.»
   - Açıklama: 'Tek tek baktı' nesnesiz kalmış; 'karda her yere tek tek baktı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karda tek tek baktı"
   - Cümle 7: «Yerden bir dal aldı ve karda tek tek baktı.»
   - Açıklama: 'Tek tek' neye bakıldığını söylemeden kullanılmış; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0095` birebir aynı, `@degisim: havalı -> beyaz` (tutuyorsan), ardından `@onarim: 54dec7b3412f5ee34476fb41192b4c4035bac329`, sonra gövde.

### Hikâye 5: tohum niloya-0098 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0098
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çeşme', fiil 'guruldamak', sıfat 'yalnız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: tek bir top vardı ve ikisi de istedi | şarkı bitene kadar sırayla oynamayı önerdi
@tohum: niloya-0098
@degisim: çeşme -> top
Niloya ile Murat ormanda fındık ağaçlarının arasında oynuyordu. Yanlarında yalnız bir top vardı. İkisi de topu ilk atmak istedi ve oyun durdu. Niloya biraz düşündü. "Murat, bir şarkı boyunca sen oyna, sonra ben," dedi Niloya. "Olur, önce sen söyle," dedi Murat. Murat topu aldı. "Dere guruldar, top zıplar!" diye şarkı söyledi Niloya. Şarkı bitince Murat topu Niloya'ya verdi. Sonra Murat şarkı söyledi ve Niloya topu attı. İkisi oyunlarına sırayla mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dere guruldar, top zıplar"
   - Cümle 8: «"Dere guruldar, top zıplar!" diye şarkı söyledi Niloya.»
   - Açıklama: 'Guruldamak' dere için yanlış kelimedir; dere şırıldar ya da çağıldar.
   - Açıklama: 'Guruldar' dere için yanlış kelime; dere 'şırıldar' ya da 'akar'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0098` birebir aynı, `@degisim: çeşme -> top` (tutuyorsan), ardından `@onarim: 1e9a4907f9c33471885dee5569dec49dd6f2c101`, sonra gövde.

### Hikâye 6: tohum niloya-0103 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0103
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'atkı', fiil 'takılmak', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: rüzgar atkıyı uçurdu ve atkı bir çalıya takıldı | kaplumbağasından yardım isteyip atkıyı kurtardı
@tohum: niloya-0103
Tepede serin bir rüzgar esiyordu. Niloya ile Tospik orada kekik topluyordu. Birden rüzgar Niloya'nın atkısını uçurdu ve atkı bir çalıya takıldı. Niloya dalgalı çizgili atkısını çok seviyordu. Atkı çalının en alt dalına dolanmıştı. Niloya çalının altına sığmıyordu. Niloya, Tospik'e çalının altına girip giremeyeceğini sordu. Tospik başını salladı ve yavaşça çalının altına girdi. Sonra atkıyı daldan itti. Niloya atkıyı dikkatle çekti ve atkı daldan çıktı. Niloya atkısını boynuna sardı ve Tospik'e sarıldı. Niloya çok sevindi, çünkü atkısını Tospik ile birlikte kurtarmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya atkısını boynuna sardı"
   - Cümle 11: «Niloya atkısını boynuna sardı ve Tospik'e sarıldı.»
   - Açıklama: Niloya adı art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0103` birebir aynı, ardından `@onarim: 6d4bbe8ab720528ad82d1dc91fac4a7074f21b90`, sonra gövde.

### Hikâye 7: tohum niloya-0106 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0106
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'yumurta', fiil 'solmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: yolda bir taş vardı ve yumurta çimlere yuvarlandı | yumurtayı yapraklarda bulup taşı yoldan kaldırdı
@tohum: niloya-0106
@degisim: düzenli -> yavaş
Bir sabah Niloya evin bahçesinde eğlenceli bir oyun oynuyordu. Kaşığın üstünde haşlanmış bir yumurta taşıyordu. Ama yolda bir taş vardı ve yumurta düşüp çimlere yuvarlandı. Niloya yumurtayı göremedi ve çimlere merakla baktı. Yumurta bahçenin kenarındaki solmuş yaprakların arasında duruyordu. Niloya yumurtayı aldı ve yeniden kaşığa koydu. Sonra taşı yoldan kaldırdı ve kenara koydu. Kaşığı kapıya kadar yavaş yavaş taşıdı. Yumurta hiç düşmedi. Niloya çok mutluydu, çünkü hem yumurtayı bulmuş hem de oyunu bitirmişti.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Niloya yumurtayı göremedi ve çimlere merakla baktı"
   - Cümle 4: «Niloya yumurtayı göremedi ve çimlere merakla baktı.»
   - Açıklama: Taş sorununun yanında kaybolan yumurtayı arama ikinci bir sorun olarak açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0106` birebir aynı, `@degisim: düzenli -> yavaş` (tutuyorsan), ardından `@onarim: daec2d734d8f6c0ad27176af232e093102715cd1`, sonra gövde.

### Hikâye 8: tohum niloya-0108 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0108
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'palto', fiil 'somurtmak', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: palto sandalyeden hep yere kaydı | paltoya iyice baktı ve düğmeleri kapattı
@tohum: niloya-0108
Niloya evde gemi oyunu oynuyordu. Gemisi iki sandalyeydi ama yelkeni yoktu. Niloya paltosunu bir sandalyeye astı ama palto iki kez yere kaydı. Niloya biraz somurttu. Sonra bir soru düşündü: Palto neden hep kayıyordu? Niloya iyice baktı. Düğmeler açıktı, bu yüzden palto duramıyordu. Niloya paltoyu sandalyenin arkasına geçirdi ve bütün düğmeleri kapattı. Bu kez palto sandalyeden düşmedi. Gemisinin artık bir yelkeni vardı. Niloya öbür sandalyeye oturdu ve hızlı bir gemi yolculuğuna çıktı. Niloya çok sevindi, çünkü yelkeni kendi başına kurmuştu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "paltoya iyice baktı ve düğmeleri kapattı"
   - Cümle 0 (plan satırı): «palto sandalyeden hep yere kaydı | paltoya iyice baktı ve düğmeleri kapattı»
   - Açıklama: Plan düğmelerin kapatıldığını söylüyor ama gövdede bu eylem yok.
   - Açıklama: Planda düğmeler kapatılıyor ama gövdede bu eylem hiç geçmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0108` birebir aynı, ardından `@onarim: 30d15cd82ddcd9dc9224ec57cb9ea093ea4e917d`, sonra gövde.

### Hikâye 9: tohum niloya-0109 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0109
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'ceviz', fiil 'çözülmek', sıfat 'kabarık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: torba dala takıldı, ipi çözüldü ve cevizler döküldü | yaprakların altına bakıp cevizleri tek tek buldu
@tohum: niloya-0109
@degisim: kabarık -> kuru
Ormanda kuşlar ötüyordu. Niloya, Mete'nin doğum günü için bir torba ceviz getirmişti. Ama torba bir dala takıldı, ipi çözüldü ve cevizler yapraklara döküldü. Mete biraz uzakta, oyuncaklarıyla oynuyordu ve bunu görmedi. Niloya dökülen cevizleri merakla aradı. Kuru yaprakları tek tek kaldırdı ve altlarına baktı. Bütün cevizleri bulup torbaya koydu. Sonra torbanın ipini sıkıca bağladı. "Mete, sana bir hediyem var!" dedi Niloya. Mete koşarak geldi ve torbayı açtı. "Çok teşekkür ederim, Niloya!" dedi Mete. İkisi bir ağacın altına oturdu ve cevizleri mutlu mutlu paylaştı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ipi çözüldü ve cevizler yapraklara döküldü"
   - Cümle 3: «Ama torba bir dala takıldı, ipi çözüldü ve cevizler yapraklara döküldü.»
   - Açıklama: Dökülen cevizleri toplayıp bitirmek, örnekteki 'dağıttı, topladı, bitti' türünden önemsiz bir sorundur.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dökülen cevizleri merakla aradı"
   - Cümle 5: «Niloya dökülen cevizleri merakla aradı.»
   - Açıklama: Döküldüğünü bildiği cevizleri aramak merakla yapılmaz; kelime anlamca uymuyor.
   - Açıklama: Dökülen cevizleri aramak meraktan değil dikkatten olur; 'merakla' kelimesi bağlama uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0109` birebir aynı, `@degisim: kabarık -> kuru` (tutuyorsan), ardından `@onarim: 9e21abd5844cfce5ea8b24151bccfa59f4a98d11`, sonra gövde.

### Hikâye 10: tohum niloya-0112 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0112
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: kaybolan eşya
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'nane', fiil 'serinletmek', sıfat 'bozuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: su şişesini bir yere bırakıp unuttu | en son nerede su içtiğini düşündü ve şişeyi buldu
@tohum: niloya-0112
Tepede güneş çok sıcak parlıyordu. Niloya kekik topluyordu ve çok susamıştı. Ama su şişesini bir yere bırakmış ve unutmuştu. Şişede nane yapraklı serin su vardı. Niloya durdu ve bir soru düşündü: Şişeden en son nerede su içmişti? Sonra hatırladı. Bozuk bir çitin yanında oturup su içmişti. Niloya tepeden aşağı yürüdü ve çite gitti. Şişe çitin dibinde, otların arasında duruyordu. Niloya şişeyi açtı ve sudan içti. Nane kokulu su onu hemen serinletti. Sonra Niloya kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "durdu ve bir soru düşündü"
   - Cümle 5: «Niloya durdu ve bir soru düşündü: Şişeden en son nerede su içmişti?»
   - Açıklama: 'Bir soru düşündü' doğal değil; 'kendine sordu' ya da 'düşündü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0112` birebir aynı, ardından `@onarim: d82d9f5515886886207848cf4143c5dfbd9f6cd2`, sonra gövde.

### Hikâye 11: tohum niloya-0116 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0116
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'marul', fiil 'çalıştırmak', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yürürken yanından küçük bir ses geliyordu | şarkı söyleyip adım attı ve sesi sepette buldu
@tohum: niloya-0116
@degisim: çalıştırmak -> durmak
Ormanda küçük bir ses geliyordu. Niloya kolunda marul dolu sepetiyle ağaçların arasında yürüyordu. Ses çok komikti ve hep Niloya'nın yanından geliyordu. Niloya ağaçların arkasına baktı ama bir şey göremedi. Sonra bir yürüme şarkısı söyledi ve şarkının her sözünde bir adım attı. Her adımda o ses de geldi. Niloya durunca ses de durdu. Niloya kolundaki sepete baktı. Ses sepetten geliyordu! Sepet eskiydi ve sallanınca ses çıkarıyordu. Niloya çok güldü. Sepeti pürüzsüz bir taşın üstüne koydu ve ses hiç gelmedi. Sonra sepeti yeniden koluna aldı ve ağaçların arasında mutlu mutlu yürüdü.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ormanda küçük bir ses geliyordu"
   - Cümle 1: «Ormanda küçük bir ses geliyordu.»
   - Açıklama: Sepetten gelen komik bir ses çocuğun önemseyeceği bir sorun değil ve hikaye bu önemsiz olay üzerine kurulu.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses çok komikti ve hep Niloya'nın yanından geliyordu"
   - Cümle 3: «Ses çok komikti ve hep Niloya'nın yanından geliyordu.»
   - Açıklama: Zararsız bir sepet sesi çözülmesi gereken gerçek bir sorun değildir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sepeti pürüzsüz bir taşın"
   - Cümle 12: «Sepeti pürüzsüz bir taşın üstüne koydu ve ses hiç gelmedi.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
   - Açıklama: 'Pürüzsüz' kelimesini 3 yaşındaki bir çocuk bilmez.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepeti pürüzsüz bir taşın üstüne koydu ve ses hiç gelmedi"
   - Cümle 12: «Sepeti pürüzsüz bir taşın üstüne koydu ve ses hiç gelmedi.»
   - Açıklama: Sepet hemen yeniden kola alındığı için taşa koyma olayı hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0116` birebir aynı, `@degisim: çalıştırmak -> durmak` (tutuyorsan), ardından `@onarim: 8d7c46f8cf9f6ed2abd3f65edf45b281a776e9b1`, sonra gövde.

### Hikâye 12: tohum niloya-0125 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0125
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'saksı', fiil 'kazanmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: kaydırak ve oyuncaklar ıslaktı, oynanacak bir şey yoktu | saksıyı ters çevirip damla sesiyle şarkı söyledi
@tohum: niloya-0125
@degisim: kazanmak -> çevirmek
Parkta yağmur tıp tıp yağıyordu. Niloya oynamak istedi, ama kaydırak ve oyuncaklar çok ıslaktı. Niloya damlaların sesini dinledi ve bu sesi daha yüksek duymak istedi. Etrafa baktı ve bankın yanında boş bir saksı gördü. Niloya saksıyı ters çevirdi ve yağmurun altına koydu. Damlalar saksıya düşünce davul gibi güzel bir ses çıktı. Niloya bu sesle birlikte en sevdiği şarkıyı söyledi. Damlalar hızlı düşünce Niloya da hızlı söyledi. Damlalar yavaş düşünce Niloya da yavaş söyledi. Niloya ıslak kaydırağı unuttu ve yeni oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Niloya saksıyı ters çevirdi ve yağmurun altına koydu"
   - Cümle 5: «Niloya saksıyı ters çevirdi ve yağmurun altına koydu.»
   - Açıklama: Sorun ıslak oyuncaklar ama çözüm bu sebebe yönelmiyor, yerine başka bir oyun kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0125` birebir aynı, `@degisim: kazanmak -> çevirmek` (tutuyorsan), ardından `@onarim: a66b6f6b1c5df7108a1dac2ed40f54ed24d7da99`, sonra gövde.
