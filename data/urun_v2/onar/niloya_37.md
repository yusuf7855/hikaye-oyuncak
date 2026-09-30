# Editör görevi (onarım): Niloya, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0051 (deneme 2 -> 3)

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
@plan: dedesinin sepeti devrildi ve fındıklar çalının altına yuvarlandı | çalının altına uzanıp fındıkları dalla dışarı çekti
@tohum: niloya-0051
@degisim: palmiye -> sepet
Ormanda kuşlar cıvıl cıvıl ötüyordu. Niloya ile dedesi fındık topluyordu. Dedesi sepeti bir taşın üstüne koydu ama sepet kaydı ve devrildi. Fındıklar alçak bir çalının altına yuvarlandı. "Çalının altı çok alçak, ben oraya eğilemem," dedi dedesi. "Ben bakarım, dedeciğim," dedi Niloya. Niloya çalının altına merakla baktı. Dibinde kahverengi fındıklar duruyordu. Niloya yerden ince bir dal aldı. Sonra yere uzandı ve fındıkları dalla dışarı çekti. Fındıkları tek tek topladı ve sepete koydu. Sepet yine doldu. Dedesi gülümsedi ve Niloya'nın başını okşadı. "Aferin, Niloya, sen olmasaydın bu fındıklar orada kalırdı!" dedi dedesi.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çalının altına uzanıp fındıkları dalla dışarı çekti"
   - Cümle 0 (plan satırı): «dedesinin sepeti devrildi ve fındıklar çalının altına yuvarlandı | çalının altına uzanıp fındıkları dalla dışarı çekti»
   - Açıklama: Planda çözümü figür yapıyor, gövdede ise dedesi yapıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ben oraya eğilemem"
   - Cümle 5: «"Çalının altı çok alçak, ben oraya eğilemem," dedi dedesi.»
   - Açıklama: Dedesi eğilemediğini söylüyor ama sonra yere uzanıp fındıkları kendisi çekiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0051` birebir aynı, `@degisim: palmiye -> sepet` (tutuyorsan), ardından `@onarim: e0093ad2f215a6071c435b9d16acf09022d71369`, sonra gövde.

### Hikâye 2: tohum niloya-0094 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Bir sabah Niloya ile dedesi ormanda fındık ağaçlarının altına oturdu. Niloya, dedesinin resimli şarkı kitabını görmek için yanına sıkıştı. İkisi de ilk şarkıyı söylemek istedi ve aynı anda başladı. Sesler birbirine karıştı. Niloya biraz düşündü. "Dede, sırayla söyleyelim, bir şarkı ben, bir şarkı sen," dedi Niloya. Niloya ilk sayfayı açtı ve neşeli şarkıyı söyledi. Dedesi onu sessizce dinledi. Sonra dedesi öbür şarkıyı söyledi. Bu kez iki şarkı da çok güzel oldu. Niloya bundan sonra şarkıları dedesiyle hep sırayla söyledi.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Sesler birbirine karıştı"
   - Cümle 4: «Sesler birbirine karıştı.»
   - Açıklama: Plandaki sorun olan seslerin karışması ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0094` birebir aynı, `@degisim: konuşkan -> neşeli` (tutuyorsan), ardından `@onarim: 556b1a938af60d9f248c424f3e468f37b8956e38`, sonra gövde.

### Hikâye 3: tohum niloya-0095 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar bulutların şeklini hızla değiştirdi | en yavaş bulutu bulup anahtarı işaretledi
@tohum: niloya-0095
@degisim: havalı -> beyaz
Bahçede hafif bir rüzgar esiyordu. Niloya kağıdına çizdiği anahtarı bulutlarda bulup işaretlemek istiyordu. Ama rüzgar beyaz bulutların şeklini hızla değiştiriyordu. Niloya'nın bir sorusu vardı: En yavaş bulut hangisiydi? Sonra bütün bulutlara tek tek baktı. Evin üstündeki büyük bulut çok yavaş gidiyordu. Niloya yalnız bu buluta uzun uzun baktı. Bulutun bir ucu yuvarlak, öbür ucu uzundu. Bu bulut tıpkı bir anahtara benziyordu. Niloya kalemini aldı ve kağıttaki anahtar resmini işaretledi. Niloya çok sevindi, çünkü aradığı şekli bulutlarda görmüştü.
```

**Hakem bulguları (6):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede hafif bir rüzgar esiyordu"
   - Cümle 1: «Bahçede hafif bir rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede, evin dışında geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "anahtarı bulutlarda bulup işaretlemek"
   - Cümle 2: «Niloya kağıdına çizdiği anahtarı bulutlarda bulup işaretlemek istiyordu.»
   - Açıklama: Buluttaki bir şey işaretlenemez; ne işaretleneceği belirsiz ve fiil nesnesine uymuyor.
   - Açıklama: Kağıda çizilmiş anahtar bulutlarda bulunup işaretlenemez; fiiller nesnesine uymuyor ve anlam karışık.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kağıdına çizdiği anahtarı bulutlarda bulup işaretlemek istiyordu"
   - Cümle 2: «Niloya kağıdına çizdiği anahtarı bulutlarda bulup işaretlemek istiyordu.»
   - Açıklama: Kendi çizdiği anahtarı kağıtta işaretlemek için bulutta aramak anlamsız bir hedef; sorun akla yatkın değil.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar beyaz bulutların şeklini hızla değiştiriyordu"
   - Cümle 3: «Ama rüzgar beyaz bulutların şeklini hızla değiştiriyordu.»
   - Açıklama: Bulutta anahtar aramak belirsiz ve önemsiz bir hedef; sorunun neden engel olduğu açık değil.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "En yavaş bulut hangisiydi?"
   - Cümle 4: «Niloya'nın bir sorusu vardı: En yavaş bulut hangisiydi?»
   - Açıklama: En yavaş bulutu arama fikri bir önceki olaydan çıkmadan sebepsizce beliriyor ve çözümü getiriyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kağıttaki anahtar resmini işaretledi"
   - Cümle 10: «Niloya kalemini aldı ve kağıttaki anahtar resmini işaretledi.»
   - Açıklama: Hedef buluttaki anahtarı işaretlemekti ama Niloya kendi kağıdındaki resmi işaretliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0095` birebir aynı, `@degisim: havalı -> beyaz` (tutuyorsan), ardından `@onarim: 2ba049e21f35677a7eea13b61c4abc058a118546`, sonra gövde.

### Hikâye 4: tohum niloya-0097 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0097
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'battaniye', fiil 'güldürmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: şarkı çok uzundu ve sözler unutuldu | sözlerin yerine ormandaki şeyleri söyledi
@tohum: niloya-0097
Niloya ormanda yere büyük bir battaniye serdi. Orada eğlenceli bir şarkı oyunu oynuyordu. Ama şarkı çok uzundu ve Niloya şarkının ortasında sözleri unuttu. Oyunun bitmesini istemedi ve biraz düşündü. Sonra sözlerin yerine ormandaki şeyleri söylemeye başladı. Fındıkları, yaprakları ve ağaçları şarkıya kattı. Bir fındık yere düştü ve Niloya onu da şarkıya ekledi. Bu yeni şarkı Niloya'yı çok güldürdü. Niloya şarkıyı sonuna kadar söyledi. Niloya bundan sonra sözleri unutunca ormandaki şeyleri söyledi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yere büyük bir battaniye serdi"
   - Cümle 1: «Niloya ormanda yere büyük bir battaniye serdi.»
   - Açıklama: Battaniye özenle kuruluyor ama hikayede hiçbir işe yaramıyor.
   - Açıklama: Battaniye bir eylem olarak kuruluyor ama hikayede hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0097` birebir aynı, ardından `@onarim: 1b1a8492041190587a25a3b94164e91bec44c392`, sonra gövde.

### Hikâye 5: tohum niloya-0098 (deneme 3 -> 4)

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
Niloya ile Murat ormanda fındık ağaçlarının arasında oynuyordu. Yanlarında yalnız bir top vardı. İkisi de topu ilk atmak istedi ve oyun durdu. Niloya biraz düşündü. "Murat, bir şarkı boyunca sen oyna, sonra ben," dedi Niloya. "Olur, önce sen söyle," dedi Murat. Murat topu aldı ve Niloya su gibi guruldayarak kısa bir şarkı söyledi. Şarkı bitince Murat topu Niloya'ya verdi. Sonra Murat şarkı söyledi ve Niloya topu attı. İkisi oyunlarına sırayla mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya su gibi guruldayarak"
   - Cümle 7: «Murat topu aldı ve Niloya su gibi guruldayarak kısa bir şarkı söyledi.»
   - Açıklama: Şarkı söylemek için 'guruldamak' fiili uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "su gibi guruldayarak kısa bir şarkı söyledi"
   - Cümle 7: «Murat topu aldı ve Niloya su gibi guruldayarak kısa bir şarkı söyledi.»
   - Açıklama: Guruldamak şarkı söyleyen bir çocuğa uygun bir fiil değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "su gibi guruldayarak kısa"
   - Cümle 7: «Murat topu aldı ve Niloya su gibi guruldayarak kısa bir şarkı söyledi.»
   - Açıklama: 'Su gibi' benzetmesi mecazlı ve 3 yaşındaki çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya su gibi guruldayarak"
   - Cümle 7: «Murat topu aldı ve Niloya su gibi guruldayarak kısa bir şarkı söyledi.»
   - Açıklama: 'Su gibi guruldayarak' benzetmesi mecazdır ve küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0098` birebir aynı, `@degisim: çeşme -> top` (tutuyorsan), ardından `@onarim: eea8860ced68e21711e768a3f5549e0d52ccce9c`, sonra gövde.

### Hikâye 6: tohum niloya-0099 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0099
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'elma', fiil 'yollamak', sıfat 'umutlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: sepete on elma koyacaklardı ama sayı karıştı | şarkı söyleyerek elmaları tek tek saydı
@tohum: niloya-0099
@degisim: umutlu -> kırmızı
Bir sabah Niloya ile dedesi ormanda kırmızı elmalar topluyordu. Dedesi, "Bu sepete on elma koyalım," dedi. Ama yerde çok elma vardı ve Niloya sayıyı karıştırdı. Niloya biraz düşündü ve dedesine baktı. "Dede, sayarken şarkı söyleyelim mi?" diye sordu Niloya. Dedesi başını salladı. Niloya sepeti boşalttı ve şarkıya başladı. "Bir, iki, üç elma, gel sepete elma!" diye söyledi Niloya. Her sayıda dedesi bir elma yolladı ve Niloya onu sepete koydu. Şarkı bitince sepette tam on elma vardı. "Aferin, Niloya, sepet hazır!" dedi dedesi. Niloya çok sevindi, çünkü sepeti dedesiyle doldurmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedesi bir elma yolladı"
   - Cümle 9: «Her sayıda dedesi bir elma yolladı ve Niloya onu sepete koydu.»
   - Açıklama: 'Yollamak' uzaktan göndermek demektir; elmayı eliyle uzatan dede için 'uzattı' ya da 'verdi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Her sayıda dedesi bir elma yolladı"
   - Cümle 9: «Her sayıda dedesi bir elma yolladı ve Niloya onu sepete koydu.»
   - Açıklama: Elma elden ele verilirken 'yolladı' uygun değil; 'uzattı' ya da 'verdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0099` birebir aynı, `@degisim: umutlu -> kırmızı` (tutuyorsan), ardından `@onarim: eb17874f8d597d76fb9915b64cb1e43f5c7e35be`, sonra gövde.

### Hikâye 7: tohum niloya-0100 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0100
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'boru', fiil 'yıkanmak', sıfat 'kırık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: dalın kırık yerinde delik vardı ve ses az çıktı | deliği parmağıyla kapatıp yeniden söyledi
@tohum: niloya-0100
@degisim: yıkanmak -> ıslanmak
Yağmur yeni dinmişti ve tepedeki otlar ıslanmıştı. Niloya otların arasında boru gibi içi boş bir dal buldu. İçine ilk kez şarkı söyledi, ama ses çok az çıktı. Niloya dalı çevirdi ve kırık yerinde küçük bir delik gördü. Deliği parmağıyla sıkıca kapattı. Sonra en sevdiği şarkıyı yeniden dalın içine söyledi. Bu kez ses yüksek ve çok güzel çıktı. Niloya güldü ve şarkısını bir kez daha söyledi. Niloya çok mutlu oldu, çünkü deliği kendisi bulup kapatmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parmağıyla kapatıp yeniden söyledi"
   - Cümle 0 (plan satırı): «dalın kırık yerinde delik vardı ve ses az çıktı | deliği parmağıyla kapatıp yeniden söyledi»
   - Açıklama: Plan satırında 'söyledi' nesnesiz kalmış; 'şarkıyı yeniden söyledi' olmalı, yoksa 'dedi' anlamı çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0100` birebir aynı, `@degisim: yıkanmak -> ıslanmak` (tutuyorsan), ardından `@onarim: 137534600ef9c759869658d662286fbe51b9fed9`, sonra gövde.

### Hikâye 8: tohum niloya-0103 (deneme 3 -> 4)

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
Tepede serin bir rüzgar esiyordu. Niloya ile Tospik orada kekik topluyordu. Birden rüzgar Niloya'nın atkısını uçurdu ve atkı bir çalıya takıldı. Niloya dalgalı çizgili atkısını çok seviyordu. Atkı çalının en alt dalına dolanmıştı. Niloya çalının altına sığmıyordu. Niloya, Tospik'ten yardım istedi. Tospik çalının altına girebilir miydi? Niloya bunu ona sordu. Tospik başını salladı ve yavaşça çalının altına girdi. Sonra atkıyı daldan itti. Niloya atkıyı dikkatle çekti ve atkı daldan çıktı. Niloya atkısını boynuna sardı ve Tospik'e sarıldı. Niloya çok sevindi, çünkü atkısını Tospik ile birlikte kurtarmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya bunu ona sordu"
   - Cümle 9: «Niloya bunu ona sordu.»
   - Açıklama: Yardım isteği önceki cümlede zaten söylendi; aynı şey dolaylı soruyla gereksizce tekrarlanıyor.
   - Açıklama: Yardım isteme ve soru aynı olayı gereksizce tekrar ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0103` birebir aynı, ardından `@onarim: 53c855f3b187d5d03e03eb876e1dcbcb1b5f1c77`, sonra gövde.

### Hikâye 9: tohum niloya-0106 (deneme 3 -> 4)

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
Bir sabah Niloya evin bahçesinde eğlenceli bir oyun oynuyordu. Kaşığın üstünde haşlanmış bir yumurta taşıyordu. Ama yolda bir taş vardı ve yumurta düşüp çimlere yuvarlandı. Niloya yumurtayı göremedi ve çimlerin ucuna merakla baktı. Yumurta bahçenin ucundaki solmuş yaprakların arasında duruyordu. Niloya yumurtayı aldı ve yeniden kaşığa koydu. Sonra taşı yoldan kaldırdı ve kenara koydu. Kaşığı kapıya kadar yavaş yavaş taşıdı. Yumurta hiç düşmedi. Niloya çok mutluydu, çünkü hem yumurtayı bulmuş hem de oyunu bitirmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çimlerin ucuna merakla baktı"
   - Cümle 4: «Niloya yumurtayı göremedi ve çimlerin ucuna merakla baktı.»
   - Açıklama: 'Çimlerin ucu' burada anlamsız; bahçenin kenarına ya da çimlere bakmak kastediliyor.
   - Açıklama: 'Çimlerin ucu' çimenliğin kenarı anlamında yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0106` birebir aynı, `@degisim: düzenli -> yavaş` (tutuyorsan), ardından `@onarim: 28510fce2da8bb549a5ada61cf67e5b365264ccf`, sonra gövde.

### Hikâye 10: tohum niloya-0109 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Ormanda kuşlar ötüyordu. Niloya, Mete'nin doğum günü için bir torba ceviz getirmişti. Ama torba bir dala takıldı, ipi çözüldü ve cevizler yapraklara döküldü. Mete biraz uzakta, oyuncaklarıyla oynuyordu ve bunu görmedi. Niloya, cevizler nereye gitti diye merak etti. Kuru yaprakları tek tek kaldırdı ve altlarına baktı. Bütün cevizleri bulup torbaya koydu. Sonra torbanın ipini sıkıca bağladı. "Mete, sana bir hediyem var!" dedi Niloya. Mete koşarak geldi ve torbayı açtı. "Çok teşekkür ederim, Niloya!" dedi Mete. İkisi bir ağacın altına oturdu ve cevizleri mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Niloya, cevizler nereye gitti diye"
   - Cümle 5: «Niloya, cevizler nereye gitti diye merak etti.»
   - Açıklama: Aktarılan soru tırnak içinde değil ve soru işareti eksik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0109` birebir aynı, `@degisim: kabarık -> kuru` (tutuyorsan), ardından `@onarim: 8aa99c0b14d170155d8fa3ffcc5a58b2bdfd4f9c`, sonra gövde.

### Hikâye 11: tohum niloya-0110 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | annesi
@tohum: niloya-0110
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kızartma', fiil 'aşmak', sıfat 'taze'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | park | annesi
@plan: rüzgar topu çitin arkasına uçurdu | topun yerini buldu ve annesinden yardım istedi
@tohum: niloya-0110
Niloya parkta top oynuyordu. Annesi bankta oturuyordu ve yanında taze patates kızartması vardı. Birden rüzgar esti ve hafif top uçup çiti aştı. Niloya oraya koştu ve merakla çitin arasından baktı. Top çitin arkasındaki uzun otların arasındaydı. Çit yüksekti ve Niloya ona tırmanmadı. Hemen annesinin yanına koştu. "Anne, topum çitin arkasına düştü, bana yardım eder misin?" diye sordu Niloya. Annesi başını salladı ve parkın kapısından çıktı. Niloya parmağıyla topun yerini gösterdi. Annesi topu otların arasından aldı ve Niloya'ya verdi. "Teşekkürler, anneciğim, şimdi birlikte kızartma yiyelim!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "taze patates kızartması vardı"
   - Cümle 2: «Annesi bankta oturuyordu ve yanında taze patates kızartması vardı.»
   - Açıklama: Kartın köy dünyasında ve izinli dünya köklerinde olmayan çağdaş bir yiyecek (patates kızartması) hikayeye eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0110` birebir aynı, ardından `@onarim: 80643b2eb452b33fd36243f5b7f54beb67718678`, sonra gövde.

### Hikâye 12: tohum niloya-0112 (deneme 3 -> 4)

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
Tepede güneş çok sıcak parlıyordu. Niloya kekik topluyordu ve çok susamıştı. Ama su şişesini bir yere bırakmış ve unutmuştu. Şişede nane yapraklı serin su vardı. Niloya durdu ve kendine sordu: Şişeden en son nerede su içmişti? Sonra hatırladı. Bozuk bir çitin yanında oturup su içmişti. Niloya tepeden aşağı yürüdü ve çite gitti. Şişe çitin dibinde, otların arasında duruyordu. Niloya şişeyi açtı ve sudan içti. Nane kokulu su onu hemen serinletti. Sonra Niloya kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya durdu ve kendine sordu"
   - Cümle 5: «Niloya durdu ve kendine sordu: Şişeden en son nerede su içmişti?»
   - Açıklama: Niloya kendi kendine soru soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0112` birebir aynı, ardından `@onarim: e6449e35d3b32c975548254f47cd99c2b9bce06f`, sonra gövde.
