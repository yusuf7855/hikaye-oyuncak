# Editör görevi (onarım): Niloya, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0001 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0001
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'düdük', fiil 'gülüşmek', sıfat 'pahalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: çimenlerde kekik yoktu ve sepet boş kaldı | kayalara baktı ve kekik bulunca düdük çaldı
@tohum: niloya-0001
@degisim: pahalı -> yeşil
Rüzgar tepelerde hafif hafif esiyordu. Niloya babaannesiyle dağda kekik topluyordu. Ama sepet boştu, çünkü çimenlerin arasında hiç kekik yoktu. "Babaanne, ben şu kayalara bakayım," dedi Niloya. Babaannesi Niloya'ya küçük bir düdük verdi. "Kekik bulursan bu düdüğü çal," dedi babaannesi. Niloya merakla büyük kayaların arasına baktı. Bir kayanın arkasında yeşil kekikler buldu. Niloya hemen düdüğü çaldı. Babaannesi sesi duydu ve Niloya'nın yanına geldi. "Burada ne çok kekik var!" dedi babaannesi. İkisi sepeti birlikte doldurdu. Sonra dolu sepete bakıp gülüştüler. Niloya çok mutluydu, çünkü babaannesine yardım etmişti.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çimenlerde kekik yoktu ve sepet boş kaldı"
   - Cümle 0 (plan satırı): «çimenlerde kekik yoktu ve sepet boş kaldı | kayalara baktı ve kekik bulunca düdük çaldı»
   - Açıklama: Gövdede sebep çimenlerde kekik olmaması değil, taşların gri olması olarak veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0001` birebir aynı, `@degisim: pahalı -> yeşil` (tutuyorsan), ardından `@onarim: 1ceb0b0821d872a416fcf4ff9d3f7401a9f52e37`, sonra gövde.

### Hikâye 2: tohum niloya-0013 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0013
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'pedal', fiil 'doğmak', sıfat 'dikkatli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yapraklı taç çok büyüktü ve gözlerine kaydı | dalın uçlarını üst üste getirip tacı küçülttü
@tohum: niloya-0013
@degisim: pedal -> dal
Niloya ormandaydı ve güneş yeni doğuyordu. İnce bir dala yapraklar takıp bir taç yaptı. Ama taç çok büyüktü ve başından gözlerine kaydı. Tacı çıkardı ve ona uzun uzun baktı. Niloya'nın aklına dalın çok mu uzun olduğu sorusu geldi. Cevabı bulmak için dalı başına göre ölçtü. Dalın gerçekten çok uzun olduğunu gördü. İki ucu biraz daha üst üste getirdi. Kırmamak için çok dikkatli davrandı ve dalı sıkıca sardı. Taç bu kez tam başına oturdu. Niloya yapraklı tacıyla ormanda neşeyle dolaştı. Niloya taç yaparken dalı önce başına göre ölçmeyi öğrendi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına dalın çok mu uzun olduğu sorusu geldi"
   - Cümle 5: «Niloya'nın aklına dalın çok mu uzun olduğu sorusu geldi.»
   - Açıklama: 'Aklına soru gelmek' deyimli ve soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0013` birebir aynı, `@degisim: pedal -> dal` (tutuyorsan), ardından `@onarim: 7d07f01f45cd6429082d4d9ea3f7aa53c28ae960`, sonra gövde.

### Hikâye 3: tohum niloya-0017 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0017
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'ay', fiil 'götürmek', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: suyun içindeki beyaz ve yuvarlak şeyi merak etti | gökyüzüne bakıp ayın suda göründüğünü buldu
@tohum: niloya-0017
@degisim: yetenekli -> yuvarlak
Bir sabah Niloya ormanda fındık dolu sepetini götürüyordu. Birden yerdeki küçük bir çukurda biraz su gördü. Suyun içinde beyaz, yuvarlak bir şey vardı. Niloya'nın aklına bir soru geldi: Suya ay mı düşmüştü? Cevabı bulmak için suyun yanına eğildi ve dikkatle baktı. Sonra suya küçük bir yaprak attı. Beyaz şey titredi ve dağıldı. Su durunca beyaz şey yine yerine geldi. Niloya başını kaldırıp gökyüzüne baktı. Ağaçların üstünde beyaz ay duruyordu. Ay suya hiç düşmemişti, gökyüzündeydi. Niloya gülümsedi ve sepetiyle neşeyle yürümeye devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 4: «Niloya'nın aklına bir soru geldi: Suya ay mı düşmüştü?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Suya ay mı düşmüştü"
   - Cümle 4: «Niloya'nın aklına bir soru geldi: Suya ay mı düşmüştü?»
   - Açıklama: Niloya'nın merak ettiği soru ilk üç cümlede değil ancak dördüncü cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0017` birebir aynı, `@degisim: yetenekli -> yuvarlak` (tutuyorsan), ardından `@onarim: 60feccccfa77c03b6cc5a0c758e81fc45764ce0b`, sonra gövde.

### Hikâye 4: tohum niloya-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0019
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: kaybolan eşya
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'topaç', fiil 'gerinmek', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: toprak düz olmadığı için topaç çiçeklerin arasından ileri yuvarlandı | çiçeklerin ötesine, çitin yanına baktı ve topacı buldu
@tohum: niloya-0019
@degisim: mükemmel -> düz
Evin bahçesinde Niloya kırmızı topacını çeviriyordu. Topaç hızla döndü ama bahçenin toprağı düz değildi. Topaç bir yana kaydı ve çiçeklerin arasından ileri yuvarlandı. Niloya topacın nereye gittiğini çok merak etti. Çiçeklerin arasına eğildi ve her yere baktı. Ama topaç orada yoktu. Niloya uzun süre eğilmişti. Ayağa kalkıp gerinince çiçeklerin ötesini, çitin yanını gördü. Kırmızı topaç çitin dibinde duruyordu. Niloya hemen oraya koştu ve topacını sevinçle aldı. Niloya bundan sonra topacını hep düz yerde çevirdi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya uzun süre eğilmişti"
   - Cümle 7: «Niloya uzun süre eğilmişti.»
   - Açıklama: Çözüm Niloya'nın gerinmesiyle sebepsizce, tesadüfen geliyor.
   - Açıklama: Çözümü getiren gerinme olayı sebepsizce ve rastlantıyla geliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ayağa kalkıp gerinince"
   - Cümle 8: «Ayağa kalkıp gerinince çiçeklerin ötesini, çitin yanını gördü.»
   - Açıklama: 'Gerinmek' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ayağa kalkıp gerinince çiçeklerin ötesini"
   - Cümle 8: «Ayağa kalkıp gerinince çiçeklerin ötesini, çitin yanını gördü.»
   - Açıklama: Niloya topacı aramaya yönelmiyor, gerinirken tesadüfen görüyor.
   - Açıklama: Topaç arayışla değil gerinirken tesadüfen görülüyor; çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0019` birebir aynı, `@degisim: mükemmel -> düz` (tutuyorsan), ardından `@onarim: 8b0270d55614cf39dce67efaf2f90c16c654f972`, sonra gövde.

### Hikâye 5: tohum niloya-0020 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0020
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: kaybolan eşya
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'trompet', fiil 'kurmak', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar oyuncak trompeti yokuştan aşağı yuvarladı | yokuşun dibine inip çalıların altına bakınca trompeti buldu
@tohum: niloya-0020
@degisim: kurmak -> bulmak
Niloya yeşil tepede oyuncak trompetini çalıyordu. Sonra onu çimenlere bıraktı ve kekik toplamaya başladı. Birden güçlü bir rüzgar esti ve trompet yokuştan aşağı yuvarlandı. Niloya arkasına döndü ama trompetini göremedi. Niloya yokuştan aceleci değil, yavaş yavaş indi. Orada büyük kekik çalıları vardı. Niloya çalıların yanına gitti ve merakla eğildi. İlk çalının arkasında hiçbir şey yoktu. İkinci çalının altında sarı bir şey parlıyordu. Bu, onun trompetiydi! Niloya onu aldı ve neşeyle üfledi. Trompetten güzel bir ses çıktı. Niloya çok sevindi, çünkü kaybolan trompetini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "güçlü bir rüzgar esti ve trompet yokuştan aşağı yuvarlandı"
   - Cümle 3: «Birden güçlü bir rüzgar esti ve trompet yokuştan aşağı yuvarlandı.»
   - Açıklama: Rüzgar trompeti yuvarlıyor, Niloya arıyor ve buluyor; sorun basit bir düşme-bulma olayı olarak önemsiz kalıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yokuştan aceleci değil, yavaş yavaş"
   - Cümle 5: «Niloya yokuştan aceleci değil, yavaş yavaş indi.»
   - Açıklama: Sıfat zarf yerine kullanılmış; 'acele etmeden' olmalı.
   - Açıklama: 'Aceleci değil' zarf yerinde kullanılmış; cümle dilbilgisel değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0020` birebir aynı, `@degisim: kurmak -> bulmak` (tutuyorsan), ardından `@onarim: 055f237430931a1b23166e88485b81f8dce8da5d`, sonra gövde.

### Hikâye 6: tohum niloya-0022 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Tospik
@tohum: niloya-0022
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'sebze', fiil 'sıkmak', sıfat 'küçük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | Tospik
@plan: havuç kaydırağın altına sıkıştı ve kaplumbağa yetişemedi | arkasına havuç koyup onu geri çağırdı
@tohum: niloya-0022
@degisim: sıkmak -> sıkışmak
Parkta Niloya, Tospik'e küçük sebze parçaları veriyordu. Bir havuç parçası yere düştü ve kaydırağın alçak ucunun altına yuvarlandı. Tospik havucun peşinden gitti ama kabuğu kaydırağın altına sığmadı. Oradan ince bir ses geldi. Niloya merakla eğildi ve baktı. Havuç kaydırağın altına sıkışmıştı ve Tospik ona yetişemiyordu. "Bana yardım eder misin, Niloya?" diye sordu Tospik. "Tabii, Tospik," dedi Niloya. Niloya başka bir havucu Tospik'in arkasına koydu. "Geri gel, Tospik, havuç burada," dedi Niloya. Tospik yavaşça geri geri yürüdü ve kaydırağın yanından çıktı. Sonra havucu afiyetle yedi ve ikisi parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kabuğu kaydırağın altına sığmadı"
   - Cümle 3: «Tospik havucun peşinden gitti ama kabuğu kaydırağın altına sığmadı.»
   - Açıklama: Tospik'in kabuğu kaydırağın altına sığmıyor ama sonra geri geri yürüyüp kaydırağın yanından çıkıyor, sanki altına girip sıkışmış gibi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oradan ince bir ses geldi"
   - Cümle 4: «Oradan ince bir ses geldi.»
   - Açıklama: Sesin kimden geldiği belirsiz ve olayda işlevi yok.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Niloya başka bir havucu Tospik'in arkasına koydu"
   - Cümle 9: «Niloya başka bir havucu Tospik'in arkasına koydu.»
   - Açıklama: Çözüm sıkışan havuca yönelmiyor; sıkışan havuç orada kalıyor.
   - Açıklama: Sorun sıkışan havuç iken çözüm havucu çıkarmıyor, yerine başka havuç koyuyor; sebebe doğrudan yönelmiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tospik yavaşça geri geri yürüdü ve kaydırağın yanından çıktı"
   - Cümle 11: «Tospik yavaşça geri geri yürüdü ve kaydırağın yanından çıktı.»
   - Açıklama: Kabuğu kaydırağın altına sığmayan Tospik orada sıkışmamışken geri çağrılıp oradan çıkıyor; anlatım kendisiyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0022` birebir aynı, `@degisim: sıkmak -> sıkışmak` (tutuyorsan), ardından `@onarim: d2bb28353eabd980922418734d34b8f681da662f`, sonra gövde.

### Hikâye 7: tohum niloya-0026 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0026
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'tabure', fiil 'uyumak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: rüzgarda sallanan sepet uyuyan babaannenin yanında ses yapıyordu | sepeti daldan indirdi ve babaannesine yumuşak bir şarkı söyledi
@tohum: niloya-0026
@degisim: kremalı -> boş
Rüzgar esiyordu ve ağaçların arasından tak tak bir ses geliyordu. Niloya'nın babaannesi yorulmuştu ve küçük bir taburede uyuyordu. Niloya babaannesinin rahat rahat uyumasını istedi. Sesin nereden geldiğini bulmak için etrafa baktı. Babaannesinin boş sepeti alçak bir dala asılıydı. Sepet rüzgarda sallanıyor ve ağaca çarpıyordu. Niloya sepeti daldan yavaşça indirdi ve yere koydu. Ses hemen kesildi. Ama babaannesi biraz kıpırdadı. Niloya onun yanına oturdu ve yumuşak bir sesle şarkı söyledi. Babaannesi gülümsedi ve tatlı tatlı uyudu. Niloya da onun yanında mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama babaannesi biraz kıpırdadı"
   - Cümle 9: «Ama babaannesi biraz kıpırdadı.»
   - Açıklama: Ses sorunu çözüldükten sonra babaannenin uyanması ikinci bir sorun olarak açılıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "yumuşak bir sesle şarkı söyledi"
   - Cümle 10: «Niloya onun yanına oturdu ve yumuşak bir sesle şarkı söyledi.»
   - Açıklama: Ses kesildikten sonra şarkı söylemek sebebe yönelmeyen ek bir adım; çözüm sepeti indirmekle bitmiyor ve yeni bir kıpırdama sorununa kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0026` birebir aynı, `@degisim: kremalı -> boş` (tutuyorsan), ardından `@onarim: 12234bf463a4ecffa57996ae5552c8e0b597455d`, sonra gövde.

### Hikâye 8: tohum niloya-0031 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0031
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kızak', fiil 'katılmak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: rüzgar ağabeyinin sepetindeki kekikleri uçurdu | kendi kekiklerinin yarısını ona verdi
@tohum: niloya-0031
@degisim: kızak -> sepet
Niloya ile Murat yeşil tepede kekik topluyordu. Birden güçlü bir rüzgar esti ve Murat'ın sepeti devrildi. Sepetteki kekikler rüzgarla uçup gitti. Murat boş sepetine baktı ve üzüldü. Niloya kendi dolu sepetine baktı. Kekiklerinin yarısını Murat'ın sepetine koydu. "Al, abi, yarısı senin," dedi Niloya. "Sen çok yardımseversin, Niloya!" dedi Murat. Sonra Niloya neşeli bir şarkı söyledi. Murat gülümsedi ve şarkıya katıldı. Niloya ile Murat tepede mutlu mutlu kekik toplamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Niloya neşeli bir şarkı söyledi"
   - Cümle 9: «Sonra Niloya neşeli bir şarkı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümüne katkı vermiyor, işe yarar biçimde kullanılmamış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Niloya neşeli bir şarkı söyledi"
   - Cümle 9: «Sonra Niloya neşeli bir şarkı söyledi.»
   - Açıklama: Şarkı önceki olaydan çıkmıyor, hikayeye sonradan eklenmiş işlevsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0031` birebir aynı, `@degisim: kızak -> sepet` (tutuyorsan), ardından `@onarim: 2de026230535e1c15fb55432b42c5d73803e43c6`, sonra gövde.

### Hikâye 9: tohum niloya-0032 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | annesi
@tohum: niloya-0032
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'zambak', fiil 'sıçratmak', sıfat 'tekerlekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | annesi
@plan: bir ağacın yanından bilinmeyen bir ses geldi | yavaşça bakıp sesi çıkaran damlaları buldu
@tohum: niloya-0032
@degisim: tekerlekli -> beyaz
Niloya annesiyle ormanda meyve toplayıp sepetlerine koyuyordu. Birden büyük bir fındık ağacının yanından küçük bir ses geldi. Niloya bu sesi çok merak etti. "Anne, şu sese bakacağım," dedi Niloya. Annesi başını salladı ve onun arkasından yürüdü. Niloya yavaşça ağaca yaklaştı ve alçak dalların altına baktı. Orada beyaz bir zambak ve küçük bir su birikintisi vardı. Ağacın yapraklarından zambağın üstüne damlalar düşüyordu. Damlalar zambaktan birikintiye kayıyor ve suyu sıçratıyordu. "Ses yağmurdan kalan damlalardan geliyor, anne!" dedi Niloya. Annesi gülümsedi ve "Doğru buldun," dedi. Sonra Niloya ile annesi meyve toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ses yağmurdan kalan damlalardan geliyor"
   - Cümle 10: «"Ses yağmurdan kalan damlalardan geliyor, anne!" dedi Niloya.»
   - Açıklama: Hikayede daha önce hiç yağmur kurulmadığı için damlaların kaynağı sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0032` birebir aynı, `@degisim: tekerlekli -> beyaz` (tutuyorsan), ardından `@onarim: f269adff55a309e15c5d78edcdeee089eb254015`, sonra gövde.

### Hikâye 10: tohum niloya-0037 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0037
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'gül', fiil 'paylaşmak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: rüzgarın getirdiği poşet güllerin üstüne takıldı | poşete dikkatle bakıp ucundan yavaşça çekti
@tohum: niloya-0037
@degisim: paylaşmak -> katlamak
Ormanda kuşlar ötüyordu. Niloya fındık ağaçlarının yanında güzel kırmızı güller gördü. Ama rüzgarın getirdiği plastik bir poşet güllerin üstüne takılmıştı. Poşet çiçeklerin çoğunu kapatıyordu. Niloya güllerin hepsini görmek istedi. Niloya merakla güllerin etrafında dolaştı ve dikkatle baktı. Poşet yalnız bir ucundan takılmıştı. Niloya öbür ucunu tuttu ve poşeti yavaşça çekip çıkardı. Hiçbir çiçek ezilmedi. Sonra poşeti küçük küçük katladı ve cebine koydu. Niloya çok sevindi, çünkü bütün kırmızı güller yeniden görünüyordu.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Niloya fındık ağaçlarının yanında güzel kırmızı güller gördü"
   - Cümle 2: «Niloya fındık ağaçlarının yanında güzel kırmızı güller gördü.»
   - Açıklama: Kartın orman tarifi meyve ve fındık ağaçlarıyla sınırlı; güller tarifte yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0037` birebir aynı, `@degisim: paylaşmak -> katlamak` (tutuyorsan), ardından `@onarim: 90151955a2c9bad3764ca9d4d57d3ccb474fb028`, sonra gövde.

### Hikâye 11: tohum niloya-0038 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Mete
@tohum: niloya-0038
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'nilüfer', fiil 'gıdıklamak', sıfat 'güçlü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | park | Mete
@plan: tek salıncak vardı ve ikisi de binmek istedi | bir şarkı bitince sırayı değiştirmeyi önerdi
@tohum: niloya-0038
@degisim: nilüfer -> salıncak
Bir sabah Niloya ile Mete parka geldi. Parkta yalnız bir salıncak vardı ve ikisi de binmek istedi. Aynı anda salıncağa koştular. "Sırayla binelim, Mete, önce sen bin, şarkı bitince de ben," dedi Niloya. Mete sevindi ve ilk o oturdu. Niloya onu hafifçe itti ve güçlü bir sesle neşeli bir şarkı söyledi. Şarkı bitince Mete hemen indi. "Sıra sende, Niloya," dedi Mete. Bu kez Mete salıncağı itti ve aynı şarkıyı söyledi. Mete susunca Niloya indi ve gülerek Mete'yi gıdıkladı. "Bu şarkı oyunu çok güzel, Mete, yine oynayalım!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "güçlü bir sesle neşeli"
   - Cümle 6: «Niloya onu hafifçe itti ve güçlü bir sesle neşeli bir şarkı söyledi.»
   - Açıklama: Şarkı için 'güçlü bir sesle' yerine 'yüksek sesle' gibi uygun bir kullanım gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0038` birebir aynı, `@degisim: nilüfer -> salıncak` (tutuyorsan), ardından `@onarim: c9d8efbd6c9f85ca82dbc6e5c2dc4e4bd1dfc9f3`, sonra gövde.

### Hikâye 12: tohum niloya-0039 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0039
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'turp', fiil 'kalkmak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: hızla geri gelen top bankın altına kaçtı | bankın arkasına geçip topu kolayca aldı
@tohum: niloya-0039
@degisim: turp -> top
Parkta güneşli bir sabah Niloya yerde oturmuş, topunu kaydırağa yuvarlıyordu. Top her seferinde geri geliyordu ve Niloya gülüyordu. Ama bir kez top hızla geri geldi ve bankın altına kaçtı. Niloya hemen kalktı ve bankın yanına koştu. Top bankın altında, arka köşede duruyordu. Niloya kolunu uzattı ama topa yetişemedi. Sonra Niloya kendine sordu: Topu bankın arkasından alabilir miydi? Niloya bankın arkasına geçti ve topu kolayca aldı. Bu kez topu kaydırağa daha yavaş yuvarladı. Top kaydıraktan indi ve tam Niloya'nın önünde durdu. Niloya çok memnun oldu ve oyununa neşeyle devam etti.
```

**Hakem bulguları (2):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Sonra Niloya kendine sordu"
   - Cümle 7: «Sonra Niloya kendine sordu: Topu bankın arkasından alabilir miydi?»
   - Açıklama: Niloya kendi kendine soru soruyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Niloya kendine sordu"
   - Cümle 7: «Sonra Niloya kendine sordu: Topu bankın arkasından alabilir miydi?»
   - Açıklama: Karttaki soru özelliği merak ettiğini sormaktır; burada kendine bir çözüm sorusu soruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0039` birebir aynı, `@degisim: turp -> top` (tutuyorsan), ardından `@onarim: bcdffc17418f952641eddf59d1b57931a5abf050`, sonra gövde.
