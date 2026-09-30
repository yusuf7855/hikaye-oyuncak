# Editör görevi (onarım): Niloya, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0131 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0131
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'fidan', fiil 'koparmak', sıfat 'lezzetli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağa çiçeklerin arasında kayboldu | şarkı söyledi ve kaplumbağa sesi izleyip geldi
@tohum: niloya-0131
@degisim: fidan -> çiçek
Niloya bahçede Tospik için lezzetli bir marul yaprağı kopardı. Ama Tospik bir sürü çiçeğin arasında kaybolmuştu. "Niloya, buradan çıkamıyorum!" diye seslendi Tospik. Niloya çiçeklere basmak istemedi ve biraz düşündü. "Tospik, sesime doğru gel!" dedi Niloya. Sonra en sevdiği şarkıyı söylemeye başladı. Tospik şarkıyı duydu ve sese doğru yavaş yavaş yürüdü. Sonunda yaprakların arasından başını çıkardı. Niloya marul yaprağını ona uzattı. Tospik yaprağı hemen yedi. "Teşekkürler, Niloya, hem şarkın hem de yaprak çok güzeldi!" dedi Tospik.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Niloya bahçede Tospik için"
   - Cümle 1: «Niloya bahçede Tospik için lezzetli bir marul yaprağı kopardı.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bahçede bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0131` birebir aynı, `@degisim: fidan -> çiçek` (tutuyorsan), ardından `@onarim: 6e71c275da405312271d6ddeb3fd9f31d933d34e`, sonra gövde.

### Hikâye 2: tohum niloya-0134 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0134
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'patates', fiil 'koşturmak', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: rüzgar şapkayı uçurdu ve şapka kayboldu | rüzgarın yönünü düşündü ve o yöne gidip şapkayı buldu
@tohum: niloya-0134
@degisim: patates -> şapka
Rüzgar birden sertçe esti. Niloya ormanın kenarında, çimenlerin üstünde koşturuyordu ve sarı şapkası başından uçtu. Rüzgar şapkayı çok uzağa götürdü. Niloya etrafına baktı ama şapkasını göremedi. Niloya durdu ve bir soru düşündü. Rüzgar hangi yöne esiyordu? Niloya ağaçların dallarına baktı. Dallar hep aynı yöne doğru sallanıyordu. Niloya o yöne doğru yavaşça yürüdü. Çalıların arkasına dikkatle baktı. Şapkası yüksek bir çalının dibinde duruyordu. Niloya şapkayı aldı ve başına sıkıca taktı. Niloya çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "durdu ve bir soru düşündü"
   - Cümle 5: «Niloya durdu ve bir soru düşündü.»
   - Açıklama: 'Bir soru düşündü' doğal değil; 'kendine sordu' ya da 'düşündü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0134` birebir aynı, `@degisim: patates -> şapka` (tutuyorsan), ardından `@onarim: c6162afae44cc9d08a619b9dd11b93e9718b7e50`, sonra gövde.

### Hikâye 3: tohum niloya-0135 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0135
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'koltuk', fiil 'sabırsızlanmak', sıfat 'yeterli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: yaklaşınca kelebekler hemen uçup gidiyordu | kekiklerin yanındaki kayaya oturup sessizce bekledi
@tohum: niloya-0135
@degisim: koltuk -> kaya
Niloya dağda yeşil otların arasında yürüyordu. Otların üstünde sarı kelebekler uçuyordu. Niloya onları yakından görmek istedi, ama yaklaşınca hepsi uçup gitti. Niloya çok sabırsızlandı. Sonra onların nereye gittiğine merakla baktı. Hepsi mor çiçekli kekiklere konuyordu. Kekiklerin yanında büyük bir kaya vardı. Kayanın üstünde Niloya için yeterli yer vardı. Niloya kayaya yavaşça oturdu ve hiç kıpırdamadı. Biraz sonra kelebekler geri geldi. En yakın kekiklere kondular. Artık Niloya onları çok iyi gördü. Sarı kanatları güneşte parlıyordu. Niloya çok sevindi, çünkü kelebekleri sonunda yakından görmüştü.
```

**Hakem bulguları (3):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "ama yaklaşınca hepsi uçup gitti"
   - Cümle 3: «Niloya onları yakından görmek istedi, ama yaklaşınca hepsi uçup gitti.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün merkezinde olaya katılıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kayanın üstünde Niloya için yeterli yer vardı"
   - Cümle 8: «Kayanın üstünde Niloya için yeterli yer vardı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Niloya yüksek yere tırmanmaz; büyük kayanın üstüne çıkıp oturması taklit edilebilir.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Biraz sonra kelebekler geri geldi"
   - Cümle 10: «Biraz sonra kelebekler geri geldi.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün parçası olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0135` birebir aynı, `@degisim: koltuk -> kaya` (tutuyorsan), ardından `@onarim: 702d9f3f2e4f8bd73b595ee4f4b3ff88d2fbb748`, sonra gövde.

### Hikâye 4: tohum niloya-0142 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0142
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'armut', fiil 'saymak', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: armutlar yaprakların arkasında kaldı | ağacın öbür tarafına gidip kalan armutları saydı
@tohum: niloya-0142
Ormanda Niloya çok yorgundu ve bir armut ağacının altına oturdu. Dallarda sarı armutlar vardı ve Niloya onları saymak istedi. Ama armutlar yaprakların arkasında kalıyordu. Niloya ancak beş armut görebildi. Niloya bir soru düşündü. Ağacın öbür tarafında da armut var mıydı? Niloya biraz dinlendi, sonra kalktı ve ağacın öbür tarafına yürüdü. Oradan başka armutlar da görünüyordu. Niloya onları tek tek saydı. Orada yedi armut daha vardı! Ağaçta tam on iki armut vardı. Niloya çok sevindi, çünkü ağaçtaki bütün armutları bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama armutlar yaprakların arkasında kalıyordu"
   - Cümle 3: «Ama armutlar yaprakların arkasında kalıyordu.»
   - Açıklama: Armutları sayamamak gerçek bir sorun değil, çocuğun önemseyeceği bir derdi olmayan zayıf bir olaydır.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya bir soru düşündü"
   - Cümle 5: «Niloya bir soru düşündü.»
   - Açıklama: 'Soru düşünmek' doğal bir eşdizim değil; 'aklına bir soru geldi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0142` birebir aynı, ardından `@onarim: e403d35019be54ff375985b95a45e52bd844e595`, sonra gövde.

### Hikâye 5: tohum niloya-0146 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0146
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babaannesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'brokoli', fiil 'takmak', sıfat 'iyi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: babaannesi eşarbını koyduğu ağacı hatırlamadı | bir soru sordu ve taşın yanındaki ağacı buldu
@tohum: niloya-0146
@degisim: brokoli -> fındık
Niloya babaannesiyle ormanda fındık topluyordu. Hava sıcaktı. Babaannesi eşarbını alçak bir dala asmıştı. Sepet dolunca babaannesi eşarbını aradı, ama hangi ağaçta olduğunu hatırlamadı. Oradaki ağaçlar hep aynıydı. "Babaanne, o ağacın yanında ne vardı?" diye sordu Niloya. "Dibinde büyük, gri bir taş vardı," dedi babaannesi. Niloya etrafa dikkatle baktı. İleride o taşı gördü ve oraya koştu. Taşın yanındaki ağacın dalında mavi eşarp duruyordu. Niloya eşarbı alıp babaannesine götürdü. Babaannesi eşarbını başına taktı ve Niloya'ya sarıldı. "Sağ ol, Niloya, sen çok iyi bir kızsın," dedi babaannesi. Niloya bundan sonra ormanda bir şey bırakınca yanına iyi baktı.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama hangi ağaçta olduğunu hatırlamadı"
   - Cümle 4: «Sepet dolunca babaannesi eşarbını aradı, ama hangi ağaçta olduğunu hatırlamadı.»
   - Açıklama: Eşarbın yerinin hatırlanmaması ancak 4. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Sepet dolunca babaannesi eşarbını aradı"
   - Cümle 4: «Sepet dolunca babaannesi eşarbını aradı, ama hangi ağaçta olduğunu hatırlamadı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Niloya bundan sonra ormanda bir şey bırakınca yanına iyi baktı"
   - Cümle 14: «Niloya bundan sonra ormanda bir şey bırakınca yanına iyi baktı.»
   - Açıklama: 'Bundan sonra' süreklilik bildirirken tek seferlik '-dı' kullanılmış; 'bakardı' olmalı ve 'yanına iyi baktı' anlamı belirsiz.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bir şey bırakınca yanına iyi baktı"
   - Cümle 14: «Niloya bundan sonra ormanda bir şey bırakınca yanına iyi baktı.»
   - Açıklama: 'Yanına' Niloya'nın yanını mı bırakılan şeyin yanını mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0146` birebir aynı, `@degisim: brokoli -> fındık` (tutuyorsan), ardından `@onarim: cab2b2ca7897b8637ce0b6af052de295a936d384`, sonra gövde.

### Hikâye 6: tohum niloya-0154 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0154
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'top', fiil 'inanmak', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: topu atıp tutmak istedi ama top düştü | şarkı söyleyerek topu yavaşça attı ve tuttu
@tohum: niloya-0154
Niloya ormanda dedesiyle gösteri oyunu oynuyordu. Topu beş kez havaya atıp tutmak istiyordu. Ama acele ediyordu ve top her seferinde yere düşüyordu. "Dede, bana inan, bu kez tutacağım," dedi Niloya. Sonra en sevdiği özel şarkısını söylemeye başladı. Şarkının her sözünde topu yavaşça havaya attı. Niloya bir, iki, üç, dört, beş diye saydı ve topu hep tuttu. Dedesi ellerini çırptı. "Çok güzel oynadın, Niloya!" dedi dedesi. Niloya bundan sonra topu atıp tutarken hep şarkı söyledi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedesiyle gösteri oyunu oynuyordu"
   - Cümle 1: «Niloya ormanda dedesiyle gösteri oyunu oynuyordu.»
   - Açıklama: 'Gösteri oyunu oynamak' anlamı belirsiz ve yerinde olmayan bir söz öbeği.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "en sevdiği özel şarkısını"
   - Cümle 5: «Sonra en sevdiği özel şarkısını söylemeye başladı.»
   - Açıklama: 'En sevdiği' ile 'özel' aynı şeyi gereksiz yere tekrarlıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra en sevdiği özel şarkısını söylemeye başladı"
   - Cümle 5: «Sonra en sevdiği özel şarkısını söylemeye başladı.»
   - Açıklama: Şarkı çözümü sebepsizce geliyor; Niloya'nın acele ettiğini fark edip yavaşlamak için şarkı seçtiği gösterilmiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bir, iki, üç, dört, beş diye saydı"
   - Cümle 7: «Niloya bir, iki, üç, dört, beş diye saydı ve topu hep tuttu.»
   - Açıklama: Niloya şarkı söylerken aynı anda sayı sayıyor; iki eylem birbiriyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0154` birebir aynı, ardından `@onarim: ba3353fefbbbad2722b33ad8603cdb6c586f2df5`, sonra gövde.

### Hikâye 7: tohum niloya-0156 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0156
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: bir şey yapmak
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'tablo', fiil 'yaklaşmak', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar kağıdı salladı ve resim bozuldu | rüzgarın geldiği yere bakıp büyük bir kayanın arkasına oturdu
@tohum: niloya-0156
@degisim: dürüst -> büyük
Rüzgar tepede hızlı hızlı esiyordu. Niloya orada boyalarıyla kağıda bir tablo, yani bir resim yapmak istiyordu. Ama rüzgar kağıdını sallıyordu ve resim bozuluyordu. Rüzgar nereden geliyordu? Niloya bu soruyu düşündü ve otlara baktı. Bütün otlar aynı yana eğiliyordu. Rüzgar karşıdaki tepeden esiyordu. Niloya yakındaki büyük bir kayaya yaklaştı. Kayanın öbür yanına oturdu. Orada rüzgar yoktu ve kağıt hiç kıpırdamadı. Niloya köyü, nehri ve evleri rahatça boyadı. Niloya bundan sonra rüzgarlı günlerde resmini büyük bir kayanın arkasında yaptı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "bir tablo, yani bir resim"
   - Cümle 2: «Niloya orada boyalarıyla kağıda bir tablo, yani bir resim yapmak istiyordu.»
   - Açıklama: 'Tablo, yani resim' gereksiz bir açıklama tekrarı; yalnız 'resim' yeterli.
   - Açıklama: 'Tablo' kelimesi gereksiz yere verilip 'resim' ile tekrar açıklanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0156` birebir aynı, `@degisim: dürüst -> büyük` (tutuyorsan), ardından `@onarim: c6f4fc6f45af0cb00734702cac5186797c544f10`, sonra gövde.

### Hikâye 8: tohum niloya-0161 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0161
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'eşarp', fiil 'ışıldamak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: parkta şarkıyı tekrar eden minicik bir ses duydu | sesin kaydıraktan gelen kendi sesi olduğunu buldu
@tohum: niloya-0161
@degisim: eşarp -> kaydırak
Niloya parkta salıncakta şarkı söylüyordu. Birden minicik bir ses onun şarkısını tekrarladı. Niloya bu sesi bulmak istedi ve hemen salıncaktan indi. Ses kapalı kaydıraktan geliyordu. Kaydırak güneşte ışıldıyordu. Niloya kaydırağın yanına gitti. Şarkısını bir kez daha söyledi. Minicik ses bu kez kaydırağın içinden geldi. Niloya içeri eğilip baktı ama orada kimse yoktu. Kaydırak onun kendi sesini geri veriyordu. Niloya bunu bulduğu için çok sevindi. Niloya ellerini çırptı ve kaydırağın içine mutlu mutlu yeni şarkılar söyledi.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden minicik bir ses onun şarkısını tekrarladı"
   - Cümle 2: «Birden minicik bir ses onun şarkısını tekrarladı.»
   - Açıklama: Kaynağı bilinmeyen gizemli bir sesin çocuğun şarkısını tekrarlaması küçük yaş için ürkütücü olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0161` birebir aynı, `@degisim: eşarp -> kaydırak` (tutuyorsan), ardından `@onarim: 22c96ed2d4863d116dd82397a95fa7904da1d3c0`, sonra gövde.

### Hikâye 9: tohum niloya-0163 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0163
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'mermer', fiil 'korumak', sıfat 'büyük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: alttaki küçük taşlar yüzünden kale hep yıkıldı | büyük bir mermer taşı en alta koydu
@tohum: niloya-0163
Tepede kuşlar ötüyordu. Niloya orada taşlardan bir kale yapıp onu korumak istiyordu. Ama altta küçük taşlar vardı ve kale hep yıkılıyordu. Kale neden duramıyordu? Niloya bu soruyu düşündü ve kaleye iyice baktı. Alttaki taşlar küçük ve yuvarlaktı. Üstteki taşları hiç tutamıyordu. Niloya otların arasında büyük, düz bir mermer taşı buldu. Onu kalenin en altına koydu. Küçük taşları da üstüne dizdi. Kale bu kez yıkılmadı. Niloya kalesinin önüne oturdu ve onu korudu. Niloya bundan sonra kale yaparken büyük taşları hep en alta koydu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yapıp onu korumak istiyordu"
   - Cümle 2: «Niloya orada taşlardan bir kale yapıp onu korumak istiyordu.»
   - Açıklama: Kaleyi neyden koruduğu yok; 'korumak' burada anlamca yerine oturmuyor.
   - Açıklama: Kaleyi neyden koruduğu belli değil; 'korumak' fiili bağlamda anlamsız kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kale yapıp onu korumak istiyordu"
   - Cümle 2: «Niloya orada taşlardan bir kale yapıp onu korumak istiyordu.»
   - Açıklama: Kaleyi korumak hedefi kuruluyor ama korunacak hiçbir tehlike yok, sonda da işlevsizce 'onu korudu' deniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "önüne oturdu ve onu korudu"
   - Cümle 12: «Niloya kalesinin önüne oturdu ve onu korudu.»
   - Açıklama: Ortada tehlike yokken 'korudu' fiili yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0163` birebir aynı, ardından `@onarim: 7eb1e8e870cacd47bfabffd230359d0c87764945`, sonra gövde.

### Hikâye 10: tohum niloya-0169 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0169
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'gözlük', fiil 'çiğnemek', sıfat 'yamuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: hızlı yürüdü ve kaplumbağası kabuğuna girdi | özür diledi ve şarkı söyleyerek onu dışarı çıkardı
@tohum: niloya-0169
@degisim: gözlük -> yaprak
Niloya ile Tospik yeşil tepede kekik topluyordu. Niloya yolda çok hızlı yürüdü ve Tospik'i geride bıraktı. Tospik ona yetişemedi ve üzüldü, sonra kabuğuna girdi. Niloya hemen geri döndü ve kaplumbağasının yanına oturdu. "Özür dilerim, Tospik, seni beklemeden yürüdüm," dedi Niloya. Ama Tospik kabuğundan çıkmadı. Niloya ona tatlı ve yavaş bir şarkı söyledi. Tospik şarkıyı duyunca önce başını, sonra ayaklarını dışarı çıkardı. "Bu şarkı çok güzel," dedi Tospik. Niloya ona taze bir yaprak verdi. Tospik yaprağı çiğnedi ve yaprağın kenarı yamuk oldu. "Bundan sonra seninle yan yana yürüyeceğim," dedi Niloya.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yaprağın kenarı yamuk oldu"
   - Cümle 11: «Tospik yaprağı çiğnedi ve yaprağın kenarı yamuk oldu.»
   - Açıklama: Çiğnenen yaprağın kenarı için 'yamuk' kelimesi doğru anlamda kullanılmamış.
   - Açıklama: Isırılan yaprak kenarı için 'yamuk' yanlış anlamda kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tospik yaprağı çiğnedi ve yaprağın kenarı yamuk oldu"
   - Cümle 11: «Tospik yaprağı çiğnedi ve yaprağın kenarı yamuk oldu.»
   - Açıklama: Yaprak ve yamuk kenarı olayda hiçbir işe yaramayan işlevsiz ayrıntı.
   - Açıklama: Yaprak ve yamuk kenarı olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0169` birebir aynı, `@degisim: gözlük -> yaprak` (tutuyorsan), ardından `@onarim: e37cc522674229890ce57020ace4a8a0218ca8ac`, sonra gövde.

### Hikâye 11: tohum niloya-0173 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0173
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'yağ', fiil 'sergilemek', sıfat 'tüylü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: arkadaşının tüylü topu kayboldu | oynarken söyledikleri şarkıyı söyleyip topun yerini hatırladı
@tohum: niloya-0173
@degisim: yağ -> kütük
Ormanda rüzgar hafif esiyordu. Mete oyuncaklarını büyük bir kütüğün üstüne dizip Niloya'ya sergiledi. Ama tüylü sarı topu yoktu. Mete onu nereye koyduğunu bilmiyordu. "Topum kayboldu!" dedi Mete. Niloya biraz düşündü. Az önce top oynarken bir şarkı söylemişlerdi. Niloya o şarkıyı yeniden söyledi. Şarkının sonunda oyun fındık ağacının yanında bitmişti. "Mete, gel, top ağacın yanında!" dedi Niloya. İkisi fındık ağacına koştu. Tüylü top yaprakların arasında duruyordu. Mete topu sevinçle kütüğe koydu. Sonra iki arkadaş bütün oyuncaklarla mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dizip Niloya'ya sergiledi"
   - Cümle 2: «Mete oyuncaklarını büyük bir kütüğün üstüne dizip Niloya'ya sergiledi.»
   - Açıklama: 'Sergilemek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Sergilemek' 3 yaşındaki bir çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0173` birebir aynı, `@degisim: yağ -> kütük` (tutuyorsan), ardından `@onarim: 347a129ddebc034bba4dba35ddbfef6ef1ca8188`, sonra gövde.

### Hikâye 12: tohum niloya-0178 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0178
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'kebap', fiil 'bırakmak', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: taşın yanından garip bir ses geldi | yanına gidip baktı ve sallanan kağıdı buldu
@tohum: niloya-0178
@degisim: soslu -> kokulu
Bir sabah Niloya yeşil tepede kekik topluyordu. Niloya'nın kokulu kebap ekmeği, kağıdın içinde bir taşın üstünde duruyordu. Birden o taşın yanından garip bir ses geldi. Niloya'nın aklında bir soru vardı: Bu ses neydi? Kekikleri bıraktı ve taşa doğru yavaşça yürüdü. Kağıdın bir ucu açılmış, rüzgarda sallanıyordu. Sesi bu kağıt yapıyordu! Ekmek ise yerindeydi. Niloya kağıdın ucunu küçük bir taşla bastırdı. Kağıt artık hiç sallanmadı. Sonra kekik toplamaya mutlu mutlu devam etti. Niloya çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "o taşın yanından garip bir ses geldi"
   - Cümle 3: «Birden o taşın yanından garip bir ses geldi.»
   - Açıklama: Sorun rüzgarda sallanan bir kağıdın sesi; önemsiz bir olay.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "taşa doğru yavaşça yürüdü"
   - Cümle 5: «Kekikleri bıraktı ve taşa doğru yavaşça yürüdü.»
   - Açıklama: Niloya tepede tek başına garip bir sesin geldiği yere gidiyor; güvenli kullanım satırı merakın bakarak, sorarak ve bir büyüğe haber vererek gösterilmesini istiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0178` birebir aynı, `@degisim: soslu -> kokulu` (tutuyorsan), ardından `@onarim: f087aac787e4769322e2b4c744633d30c8fefc24`, sonra gövde.
