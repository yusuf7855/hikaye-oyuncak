# Editör görevi (onarım): Niloya, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0116 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Ormanda küçük bir ses geliyordu. Niloya kolunda sepetiyle ağaçların arasında yürüyordu. Ses çok komikti ve hep Niloya'nın yanından geliyordu. Niloya ağaçların arkasına baktı ama bir şey göremedi. Sonra bir yürüme şarkısı söyledi ve şarkının her sözünde bir adım attı. Her adımda o ses de geldi. Niloya durunca ses de durdu. Niloya kolundaki sepete baktı. Ses sepetten geliyordu! Sepet eskiydi ve sallanınca ses çıkarıyordu. Niloya çok güldü. Sepeti düz ve pürüzsüz bir taşın üstüne koydu ve yanına oturdu. Sonra sepetteki ekmeği ve marulu mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düz ve pürüzsüz bir taşın"
   - Cümle 12: «Sepeti düz ve pürüzsüz bir taşın üstüne koydu ve yanına oturdu.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepeti düz ve pürüzsüz bir taşın üstüne koydu"
   - Cümle 12: «Sepeti düz ve pürüzsüz bir taşın üstüne koydu ve yanına oturdu.»
   - Açıklama: Düz ve pürüzsüz taş işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra sepetteki ekmeği ve marulu mutlu mutlu yedi"
   - Cümle 13: «Sonra sepetteki ekmeği ve marulu mutlu mutlu yedi.»
   - Açıklama: Son cümle sesin gizemi hedefine dönmüyor, ilgisiz bir yemek eylemiyle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0116` birebir aynı, `@degisim: çalıştırmak -> durmak` (tutuyorsan), ardından `@onarim: 3282d9e276810d26cf3476c56059ef4568d924f8`, sonra gövde.

### Hikâye 2: tohum niloya-0125 (deneme 3 -> 4)

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
Parkta yağmur tıp tıp yağıyordu. Niloya oynamak istedi, ama kaydırak ve oyuncaklar çok ıslaktı. Niloya damlaların sesini dinledi ve bu sesi daha yüksek duymak istedi. Bankın yanında boş bir saksı duruyordu. Niloya saksıyı ters çevirdi ve yağmurun altına koydu. Damlalar saksıya düşünce davul gibi güzel bir ses çıktı. Niloya bu sesle birlikte en sevdiği şarkıyı söyledi. Damlalar hızlı düşünce Niloya da hızlı söyledi. Damlalar yavaş düşünce Niloya da yavaş söyledi. Niloya ıslak kaydırağı unuttu ve yeni oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bankın yanında boş bir saksı duruyordu"
   - Cümle 4: «Bankın yanında boş bir saksı duruyordu.»
   - Açıklama: Parkta boş saksı tam gerektiği anda sebepsizce beliriyor ve çözümü kendisi getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0125` birebir aynı, `@degisim: kazanmak -> çevirmek` (tutuyorsan), ardından `@onarim: 57bbf973baf92d7b208831b53f4115801f846dc8`, sonra gövde.

### Hikâye 3: tohum niloya-0129 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0129
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'file', fiil 'bozulmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | -
@plan: kar tanesi sıcak elinde eridi ve bozuldu | kaydırağın soğuk üstündeki karlara baktı
@tohum: niloya-0129
@degisim: file -> kaydırak
Parkta kar yağıyordu ve hava çok soğuktu. Niloya yıldız gibi kar tanelerini yakından görmek istedi. Ama bir kar tanesi eline düştü, hemen eridi ve şekli bozuldu. Niloya başka bir yer bulmak için etrafa merakla baktı. Kaydırağın üstünde de ince bir kar vardı. Niloya kaydırağa yaklaştı ve eğildi. Kaydırak soğuktu ve kar taneleri orada erimiyordu. Niloya onlara yakından baktı. Hepsinin küçük, sivri uçları vardı! Kar taneleri gerçekten minik yıldızlara benziyordu. Niloya çok sevindi, çünkü kar tanelerini sonunda yakından görmüştü.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kaydırağın soğuk üstündeki karlara"
   - Cümle 0 (plan satırı): «kar tanesi sıcak elinde eridi ve bozuldu | kaydırağın soğuk üstündeki karlara baktı»
   - Açıklama: Sıfat tamlamanın arasına yanlış girmiş; 'kaydırağın soğuk yüzeyindeki' ya da 'soğuk kaydırağın üstündeki' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0129` birebir aynı, `@degisim: file -> kaydırak` (tutuyorsan), ardından `@onarim: 522c81cd0b43af463bf8fa282fab407964ede523`, sonra gövde.

### Hikâye 4: tohum niloya-0131 (deneme 3 -> 4)

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
Niloya bahçede Tospik için lezzetli bir marul yaprağı kopardı. Ama Tospik bir sürü çiçeğin arasında kaybolmuştu. "Niloya, buradan çıkamıyorum!" diye seslendi Tospik. Niloya çiçeklere basmak istemedi. Niloya biraz düşündü. "Tospik, sesime doğru gel!" dedi Niloya. Sonra en sevdiği şarkıyı söylemeye başladı. Tospik şarkıyı duydu ve sese doğru yavaş yavaş yürüdü. Sonunda yaprakların arasından başını çıkardı. Niloya marul yaprağını ona uzattı. Tospik yaprağı hemen yedi. "Teşekkürler, Niloya, hem şarkın hem de yaprak çok güzeldi!" dedi Tospik.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya çiçeklere basmak istemedi. Niloya biraz düşündü."
   - Cümle 4: «Niloya çiçeklere basmak istemedi.»
   - Açıklama: Ad art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0131` birebir aynı, `@degisim: fidan -> çiçek` (tutuyorsan), ardından `@onarim: 471a59fd17d6d41d6f3d75c9876ceee44188dd27`, sonra gövde.

### Hikâye 5: tohum niloya-0134 (deneme 3 -> 4)

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
Rüzgar birden sertçe esti. Niloya ormanın kenarında, çimenlerin üstünde koşturuyordu ve sarı şapkası başından uçtu. Şapka uzağa uçtu ve kayboldu. Niloya etrafına baktı ama şapkasını göremedi. Niloya durdu ve kendine sordu: Rüzgar hangi yöne esiyordu? Niloya ağaçların dallarına baktı. Dallar hep aynı yöne doğru sallanıyordu. Niloya o yöne doğru yavaşça yürüdü. Çalıların arkasına dikkatle baktı. Şapkası yüksek bir çalının dibinde duruyordu. Niloya şapkayı aldı ve başına sıkıca taktı. Niloya çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şapka uzağa uçtu ve kayboldu"
   - Cümle 3: «Şapka uzağa uçtu ve kayboldu.»
   - Açıklama: Şapkanın uçtuğu bir önceki cümlede söylendi; 'uçtu' gereksiz tekrarlanıyor.
   - Açıklama: Şapkanın uçtuğu bir önceki cümlede söylenmişti; 'uçtu' gereksiz tekrarlanıyor.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya durdu ve kendine sordu"
   - Cümle 5: «Niloya durdu ve kendine sordu: Rüzgar hangi yöne esiyordu?»
   - Açıklama: Niloya kendi kendine soru soruyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "kendine sordu: Rüzgar hangi yöne esiyordu?"
   - Cümle 5: «Niloya durdu ve kendine sordu: Rüzgar hangi yöne esiyordu?»
   - Açıklama: Doğrudan aktarılan soru tırnak içinde değil.
   - Açıklama: Doğrudan soru tırnak içine alınmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0134` birebir aynı, `@degisim: patates -> şapka` (tutuyorsan), ardından `@onarim: 784b0358ea8dcb35cac4cc94c042da1e1904a706`, sonra gövde.

### Hikâye 6: tohum niloya-0135 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: güzel bir koku vardı ama kaya önünü kapattı | kayanın öbür yanına baktı ve kekikleri buldu
@tohum: niloya-0135
@degisim: koltuk -> kaya
Niloya dağda yürürken çok güzel bir koku fark etti. Kokunun nereden geldiğini bulmak istedi. Ama önünde büyük bir kaya vardı ve arkasını göremiyordu. Niloya kokuyu hemen bulmak için sabırsızlandı. Kayanın öbür yanını çok merak etti. Kayanın yanında geçmek için yeterli yer vardı. Niloya kayanın yanından dolaşıp öbür tarafa geçti. Kayanın arkasında mor çiçekli kekikler vardı! Güzel koku bu kekiklerden geliyordu. Niloya eğildi ve kekikleri yavaşça kokladı. Sonra derin bir nefes aldı ve gülümsedi. Niloya çok sevindi, çünkü güzel kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kayanın yanında geçmek için"
   - Cümle 6: «Kayanın yanında geçmek için yeterli yer vardı.»
   - Açıklama: Ek yanlış; 'kayanın yanından geçmek' olmalı.
   - Açıklama: Yönelme/ayrılma eki yanlış; 'kayanın yanından geçmek' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kayanın yanında geçmek için yeterli yer vardı"
   - Cümle 6: «Kayanın yanında geçmek için yeterli yer vardı.»
   - Açıklama: Kaya aslında bir engel değil, yanından geçilince sorun kendiliğinden kalktığı için sorun önemsiz kalıyor.
   - Açıklama: Kayanın yanından rahatça geçilebildiği için engel gerçek bir sorun değil, önemsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0135` birebir aynı, `@degisim: koltuk -> kaya` (tutuyorsan), ardından `@onarim: cd9cb0607c9ad9bba1457e65a925abfe6bb85785`, sonra gövde.

### Hikâye 7: tohum niloya-0137 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0137
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'taş', fiil 'güvenmek', sıfat 'kırmızı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: yıldız için kırmızı taş gerekiyordu ama önlerinde yoktu | merakla etrafa bakıp kütüğün dibinde kırmızı taşlar buldu
@tohum: niloya-0137
@degisim: güvenmek -> kapatmak
Ormanda, fındık ağaçlarının altında, Niloya ile Mete oynuyordu. Niloya, Mete'ye taşlardan sürpriz bir yıldız yapmak istedi. Mete kırmızıyı çok severdi, ama önlerindeki taşların hiçbiri kırmızı değildi. "Gözlerini kapat, Mete, biraz bekle," dedi Niloya. Mete gözlerini kapattı ve bir ağaca yaslandı. Niloya merakla etrafta dolaştı. Yaprakların altına ve kütüklerin yanına baktı. Bir kütüğün dibinde küçük kırmızı taşlar buldu. Niloya bu taşlarla yere büyük bir yıldız yaptı. "Şimdi aç, Mete!" dedi Niloya. Mete yıldızı gördü ve sevinçle zıpladı. "Benim için mi, çok güzel!" dedi Mete. Niloya çok sevindi, çünkü Mete yıldızı sevmişti.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: ""Benim için mi, çok güzel!""
   - Cümle 12: «"Benim için mi, çok güzel!" dedi Mete.»
   - Açıklama: Soru ekinden sonra virgül değil soru işareti gelmeli: 'Benim için mi? Çok güzel!'

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0137` birebir aynı, `@degisim: güvenmek -> kapatmak` (tutuyorsan), ardından `@onarim: b75eb39fb23e61ed9b454548d3eb2db1374dd2c2`, sonra gövde.

### Hikâye 8: tohum niloya-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0139
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'yoğurt', fiil 'yorulmak', sıfat 'hareketli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: oyunda otların arasında kekiği tanıyamadı | kekiğin kokusunu düşündü ve otları kokladı
@tohum: niloya-0139
@degisim: hareketli -> yeşil
Dağda Niloya yemek oyunu oynuyordu. Yanında boş bir yoğurt kabı vardı ve içine kekik koyacaktı. Ama çimenlerde çok yeşil ot vardı ve Niloya kekiği tanıyamadı. Kekik bulmak için otların arasında koştu ve yoruldu. Bir taşa oturdu. O zaman Niloya'nın aklına bir soru geldi: Kekiğin kokusu nasıldı? Niloya kekiğin güzel koktuğunu biliyordu. Yakındaki otları tek tek kokladı. Küçük yapraklı bir ot çok güzel kokuyordu. Bu kekikti! Niloya kekiği yoğurt kabına koydu ve oyundaki yemeği hazırladı. Niloya bundan sonra kekiği kokusundan tanıdı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aklına bir soru geldi"
   - Cümle 6: «O zaman Niloya'nın aklına bir soru geldi: Kekiğin kokusu nasıldı?»
   - Açıklama: 'Aklına gelmek' deyimdir; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 6: «O zaman Niloya'nın aklına bir soru geldi: Kekiğin kokusu nasıldı?»
   - Açıklama: 'Aklına bir soru gelmek' deyimsel ve soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0139` birebir aynı, `@degisim: hareketli -> yeşil` (tutuyorsan), ardından `@onarim: 24ef43ba29c0376afc7183be00e4602d0e443360`, sonra gövde.

### Hikâye 9: tohum niloya-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0141
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kilit', fiil 'hatırlamak', sıfat 'hazır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: koşarken sepete çarptı ve kekikler döküldü | özür diledi ve kayanın arkasında yeni kekik buldu
@tohum: niloya-0141
@degisim: kilit -> kapak
Niloya babaannesiyle dağda kekik topluyordu. Yanlarında büyük bir kaya vardı. Ama Niloya koşarken sepete çarptı ve kekikler yere döküldü. Kekiklerin çoğu ayağının altında ezildi. Babaannesi üzgün üzgün baktı. "Özür dilerim, babaanne, sepeti görmedim," dedi Niloya. "Olsun, güzel kızım," dedi babaannesi. Niloya kayanın arkasına hiç bakmadıklarını hatırladı. Hemen gidip merakla baktı. Orada çok kekik vardı! "Babaanne, gel, sepeti buraya getir!" dedi Niloya. İkisi sepeti hemen doldurdu. Babaannesi sepetin kapağını kapattı ve "Sepet hazır," dedi. Sonra ikisi kayanın yanına oturdu ve mutlu mutlu dinlendi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Niloya koşarken sepete"
   - Cümle 3: «Ama Niloya koşarken sepete çarptı ve kekikler yere döküldü.»
   - Açıklama: 'Ama' önceki cümleyle bir karşıtlık kurmuyor; bağlaç yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0141` birebir aynı, `@degisim: kilit -> kapak` (tutuyorsan), ardından `@onarim: d01bad5c96c9c884616a524152e087f6913614fb`, sonra gövde.

### Hikâye 10: tohum niloya-0142 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Ormanda Niloya çok yorgundu ve bir armut ağacının altına oturdu. Dallarda sarı armutlar vardı ve Niloya onları saymak istedi. Ama armutlar yaprakların arkasında kalıyordu. Niloya ancak beş armut görebildi. Niloya'nın aklına bir soru geldi: Ağacın öbür tarafında da armut var mıydı? Niloya hemen kalktı ve ağacın öbür tarafına yürüdü. Oradan başka armutlar da görünüyordu. Niloya onları tek tek saydı. Orada yedi armut daha vardı! Ağaçta tam on iki armut vardı. Niloya çok sevindi, çünkü ağaçtaki bütün armutları bulmuştu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ormanda Niloya çok yorgundu"
   - Cümle 1: «Ormanda Niloya çok yorgundu ve bir armut ağacının altına oturdu.»
   - Açıklama: Niloya'nın yorgunluğu kuruluyor ama hiç kullanılmıyor, üstelik hemen kalkıp yürüyor.
   - Açıklama: Yorgunluk kuruluyor ama hiç kullanılmıyor; Niloya hemen kalkıp yürüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 5: «Niloya'nın aklına bir soru geldi: Ağacın öbür tarafında da armut var mıydı?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Aklına bir soru gelmek' deyimsel bir anlatım; küçük çocuk için soyut.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aklına bir soru geldi"
   - Cümle 5: «Niloya'nın aklına bir soru geldi: Ağacın öbür tarafında da armut var mıydı?»
   - Açıklama: 'Aklına gelmek' deyimi 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0142` birebir aynı, ardından `@onarim: 57721b7ee198bf142f139258af18bac51f8b23bc`, sonra gövde.

### Hikâye 11: tohum niloya-0145 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | park | dedesi
@tohum: niloya-0145
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'salatalık', fiil 'birikmek', sıfat 'zarif'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | dedesi
@plan: kaydırağın yanından garip bir ses geldi | suyun nereden geldiğini sordu ve damlaları buldu
@tohum: niloya-0145
@degisim: zarif -> ıslak
Bir sabah Niloya ile dedesi parktaki bankta oturuyordu. Dedesi ona dilim dilim salatalık verdi. Birden kaydırağın yanından "tıp, tıp" diye bir ses geldi. Niloya bu sesin ne olduğunu çok merak etti. Kaydırağın yanına koştu ve yerde biraz su gördü. "Dede, bu su nereden geldi?" diye sordu Niloya. "Dün yağmur yağdı," dedi dedesi. Niloya kaydırağın ıslak tepesine baktı. Orada yağmur suyu birikmişti. Su oradan yavaş yavaş aşağı damlıyordu. Her damla yerdeki suya düşünce "tıp" diye ses çıkarıyordu. Niloya dedesinin yanına döndü ve salatalığını mutlu mutlu yedi. Niloya çok sevindi, çünkü sesi yapan damlaları kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden kaydırağın yanından"
   - Cümle 3: «Birden kaydırağın yanından "tıp, tıp" diye bir ses geldi.»
   - Açıklama: Garip bir ses gerçek bir sorun değil, yalnız bir merak; ortada çözülmesi gereken bir dert yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0145` birebir aynı, `@degisim: zarif -> ıslak` (tutuyorsan), ardından `@onarim: e2304da4e940e87fe573a74a2e688aa9c4902a6e`, sonra gövde.

### Hikâye 12: tohum niloya-0146 (deneme 2 -> 3)

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
Niloya babaannesiyle ormanda fındık topluyordu. Hava sıcaktı ve babaannesi eşarbını alçak bir dala asmıştı. Sepet dolunca babaannesi eşarbını almak istedi. Ama hangi ağaçta olduğunu hatırlamadı. Etraftaki ağaçlar birbirine çok benziyordu. "Babaanne, o ağacın yanında ne vardı?" diye sordu Niloya. "Dibinde büyük, gri bir taş vardı," dedi babaannesi. Niloya etrafa dikkatle baktı. İleride o taşı gördü ve oraya koştu. Taşın yanındaki ağacın dalında mavi eşarp duruyordu. Niloya eşarbı alıp babaannesine götürdü. Babaannesi eşarbını başına taktı ve Niloya'ya sarıldı. "Sağ ol, Niloya, sen çok iyi bir kızsın," dedi babaannesi. Niloya bundan sonra kaybolan bir şeyi ararken önce sorular sordu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama hangi ağaçta olduğunu hatırlamadı"
   - Cümle 4: «Ama hangi ağaçta olduğunu hatırlamadı.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "önce sorular sordu"
   - Cümle 14: «Niloya bundan sonra kaybolan bir şeyi ararken önce sorular sordu.»
   - Açıklama: Tohumdaki soru özelliği bir kez kullanıldıktan sonra son cümlede ikinci kez ders gibi tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0146` birebir aynı, `@degisim: brokoli -> fındık` (tutuyorsan), ardından `@onarim: 09d4763489d2d3bb842fde4de4203e6472cb291a`, sonra gövde.
