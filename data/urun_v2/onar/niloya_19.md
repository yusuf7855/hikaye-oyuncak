# Editör görevi (onarım): Niloya, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0037 (deneme 5 -> 6)

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
Ormanda kuşlar ötüyordu. Niloya bir elma ağacının dibinde küçük kırmızı güller gördü. Ama rüzgarın getirdiği plastik bir poşet güllerin üstüne takılmıştı. Poşet çiçeklerin çoğunu kapatıyordu. Niloya güllerin hepsini görmek istedi. Niloya merakla güllerin etrafında dolaştı ve dikkatle baktı. Poşet yalnız bir ucundan takılmıştı. Niloya öbür ucunu tuttu ve poşeti yavaşça çekip çıkardı. Hiçbir çiçek ezilmedi. Sonra poşeti küçük küçük katladı ve cebine koydu. Niloya çok sevindi, çünkü bütün kırmızı güller yeniden görünüyordu.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "rüzgarın getirdiği plastik bir poşet"
   - Cümle 3: «Ama rüzgarın getirdiği plastik bir poşet güllerin üstüne takılmıştı.»
   - Açıklama: Plastik poşet kartın tohum_yasak_kategoriler alanındaki çağdaş eşya kapsamına giriyor ve kartın köy dünyasında yer almıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0037` birebir aynı, `@degisim: paylaşmak -> katlamak` (tutuyorsan), ardından `@onarim: 66ae3736f66a2bc943d66eed1ef2816b1499d1c3`, sonra gövde.

### Hikâye 2: tohum niloya-0039 (deneme 5 -> 6)

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
Parkta güneşli bir sabah Niloya yerde oturmuş, topunu kaydırağa yuvarlıyordu. Top her seferinde geri geliyordu ve Niloya gülüyordu. Ama bir kez top hızla geri geldi ve bankın altına kaçtı. Niloya hemen kalktı ve bankın yanına koştu. Top bankın altında, arka köşede duruyordu. Niloya kolunu uzattı ama topa yetişemedi. Niloya kendine bir soru sordu: Bankın arkasından topa yetişebilir miydi? Niloya bankın arkasına geçti ve topu kolayca aldı. Bu kez topu kaydırağa daha yavaş yuvarladı. Top kaydıraktan indi ve tam Niloya'nın önünde durdu. Niloya çok memnun oldu ve oyununa neşeyle devam etti.
```

**Hakem bulguları (1):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya kendine bir soru sordu"
   - Cümle 7: «Niloya kendine bir soru sordu: Bankın arkasından topa yetişebilir miydi?»
   - Açıklama: Niloya kendi kendine soru soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0039` birebir aynı, `@degisim: turp -> top` (tutuyorsan), ardından `@onarim: 485b4105db4120e1e0629a52f9c984893fc1e5ad`, sonra gövde.

### Hikâye 3: tohum niloya-0047 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | annesi
@tohum: niloya-0047
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'lamba', fiil 'üflemek', sıfat 'gururlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | annesi
@plan: kaydıraktan kayarken annesinin tokasını otlara düşürdü | özür diledi ve kaydırağın altına bakıp tokayı buldu
@tohum: niloya-0047
@degisim: lamba -> toka
Parkta Niloya annesinin mavi tokasını saçına takmıştı. Sonra tokayı çıkarmadan kaydıraktan hızla kaydı ve toka otların içine düştü. Annesi bankta oturuyordu. Niloya hemen annesinin yanına gitti. "Özür dilerim, anne, tokanı düşürdüm," dedi Niloya. "Gel, birlikte bakalım," dedi annesi. Niloya kaydırağın altına merakla baktı. Orada mavi bir şey parlıyordu. Niloya tokayı aldı ve üstündeki tozu üfledi. Sonra onu gururlu gururlu annesine uzattı. Annesi gülümsedi ve Niloya'ya sarıldı. Niloya çok sevindi, çünkü tokayı kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onu gururlu gururlu annesine"
   - Cümle 10: «Sonra onu gururlu gururlu annesine uzattı.»
   - Açıklama: 'Gururlu gururlu' soyut bir kavramı alışılmadık bir ikilemeyle veriyor ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Gururlu gururlu' doğal olmayan bir ikileme ve 'gurur' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0047` birebir aynı, `@degisim: lamba -> toka` (tutuyorsan), ardından `@onarim: f326115fcff06ec9f11f980fbf5064f8e1278a34`, sonra gövde.

### Hikâye 4: tohum niloya-0054 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | Tospik
@tohum: niloya-0054
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'alet', fiil 'fırçalamak', sıfat 'devasa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Tospik
@plan: arkadaşı çok yavaştı ve geride kaldı | şarkı söyleyip onu çağırdı ve ona fındık verdi
@tohum: niloya-0054
@degisim: fırçalamak -> dikmek
Bir sabah Niloya ormandaki devasa fındık ağacının altına geldi. Tospik de onunla gelmişti ama çok yavaştı ve geride kalmıştı. Niloya iki fındık dikmek istiyordu, biri Tospik'in olacaktı. Tospik'i çağırmak için yüksek sesle neşeli bir şarkı söyledi. Tospik şarkıyı duydu ve ağacın altına geldi. Niloya sepetinden küçük bir bahçe aleti çıkardı ve iki çukur açtı. "Tospik, bu fındık senin," dedi Niloya. "Sağ ol, Niloya," dedi Tospik. Tospik fındığını burnuyla çukura itti. Niloya da kendi fındığını koydu ve çukurları toprakla örttü. Niloya bundan sonra fındıklarını hep Tospik'le paylaştı.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ona fındık verdi"
   - Cümle 0 (plan satırı): «arkadaşı çok yavaştı ve geride kaldı | şarkı söyleyip onu çağırdı ve ona fındık verdi»
   - Açıklama: Fındık vermek geride kalma sorununun çözümü değil, planın çözümü gövdedeki sorunla örtüşmüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormandaki devasa fındık ağacının"
   - Cümle 1: «Bir sabah Niloya ormandaki devasa fındık ağacının altına geldi.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'kocaman' olmalı.
   - Açıklama: 'Devasa' kelimesi 3 yaşındaki bir çocuğun bildiği bir kelime değil.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "ormandaki devasa fındık ağacının"
   - Cümle 1: «Bir sabah Niloya ormandaki devasa fındık ağacının altına geldi.»
   - Açıklama: Kartın orman tarifindeki fındık ağaçları küçük ağaçlardır; devasa fındık ağacı diziyi bilen çocuğa yanlış bilgi verir.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama çok yavaştı ve geride kalmıştı"
   - Cümle 2: «Tospik de onunla gelmişti ama çok yavaştı ve geride kalmıştı.»
   - Açıklama: Sorun önemsiz; Tospik'in geride kalması tek bir şarkıyla hemen çözülüyor ve hikayenin asıl olayı başka bir hedefe (fındık dikme) kayıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya iki fındık dikmek"
   - Cümle 3: «Niloya iki fındık dikmek istiyordu, biri Tospik'in olacaktı.»
   - Açıklama: Fındık tohumu dikilmez, ekilir; 'fındık ekmek' olmalı.
   - Açıklama: Fındık tohum olarak ekilir, dikilmez; 'fındık ekmek' olmalı.
6. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Niloya iki fındık dikmek istiyordu"
   - Cümle 3: «Niloya iki fındık dikmek istiyordu, biri Tospik'in olacaktı.»
   - Açıklama: Tospik'in geride kalması sorununun yanına ayrı bir fındık dikme işi ekleniyor.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Niloya bundan sonra fındıklarını hep Tospik'le paylaştı"
   - Cümle 11: «Niloya bundan sonra fındıklarını hep Tospik'le paylaştı.»
   - Açıklama: Paylaşma dersi yaşanan sorundan (Tospik'in yavaşlığı) çıkmıyor; kapanış olaya bağlı değil.
   - Açıklama: Paylaşma dersi, sorun olan Tospik'in yavaşlığından çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0054` birebir aynı, `@degisim: fırçalamak -> dikmek` (tutuyorsan), ardından `@onarim: ebdf043f1127a7a896959a7a06eb62a3f617f924`, sonra gövde.

### Hikâye 5: tohum niloya-0057 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0057
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kitaplık', fiil 'kırılmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: öteki dallar kuruydu ve hemen kırılıyordu | tek sağlam dalı sırayla kullanıp resim çizdiler
@tohum: niloya-0057
@degisim: kitaplık -> dal
Rüzgar ağaçların arasında hafifçe esiyordu. Niloya ormanda merakla dolaştı ve sağlam bir dal buldu. Bu dalla toprağa resim çizmeye başladı. Mete de çizmek istedi ama yerdeki öteki dallar kuruydu ve hemen kırılıyordu. Başka sağlam dal da yoktu. Niloya dalı gülümseyerek Mete'ye uzattı ve ikisi sırayla çizmeye başladı. Önce Mete toprağa büyük bir ağaç çizdi. Sonra Niloya ağacın yanına küçük bir çiçek çizdi. Mete ağacın üstüne yuvarlak bir güneş ekledi. Niloya da güneşin altına el ele tutuşan iki çocuk çizdi. Resim bitince ikisi de ona bakıp güldü. Niloya çok sevindi, çünkü sırayla çizince kocaman bir resim yapmışlardı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Mete de çizmek istedi ama yerdeki öteki dallar kuruydu"
   - Cümle 4: «Mete de çizmek istedi ama yerdeki öteki dallar kuruydu ve hemen kırılıyordu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0057` birebir aynı, `@degisim: kitaplık -> dal` (tutuyorsan), ardından `@onarim: c7ef22ef457486217a8c7f6430309cb80cbc10bd`, sonra gövde.

### Hikâye 6: tohum niloya-0059 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0059
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'dalga', fiil 'sunmak', sıfat 'sadık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: ağabeyinin sepetinde delik vardı ve fındıkları döküldü | kendi sağlam sepetini ağabeyiyle paylaştı
@tohum: niloya-0059
@degisim: sadık -> sağlam
Ormanda Niloya ile Murat fındık topluyordu. Ama Murat'ın sepetinin dibinde bir delik vardı. Topladığı fındıklar delikten yere dökülüyordu. Murat boş sepetine üzgün üzgün baktı. Niloya onu güldürmek için nehirdeki dalgaları anlatan bir şarkı söyledi. Murat şarkıyı duyunca güldü. Sonra Niloya kendi sepetini ağabeyine sundu. "Abiciğim, benim sepetim sağlam, fındıklarımızı buna koyalım," dedi Niloya. "Teşekkürler, Niloya, sen çok iyisin," dedi Murat. Murat yerdekileri topladı ve Niloya'nın sepetine koydu. İkisi sırayla sepete fındık attı. Niloya ile Murat aynı sepeti mutlu mutlu doldurdu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "nehirdeki dalgaları anlatan bir şarkı söyledi"
   - Cümle 5: «Niloya onu güldürmek için nehirdeki dalgaları anlatan bir şarkı söyledi.»
   - Açıklama: Şarkı sorunun çözümüne hiç katkı vermeyen işlevsiz bir ayrıntı olarak araya giriyor.
   - Açıklama: Ormanda nehir dalgaları şarkısı sebepsiz ekleniyor ve sepet sorununun çözümüne hiçbir katkısı yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "nehirdeki dalgaları anlatan bir şarkı"
   - Cümle 5: «Niloya onu güldürmek için nehirdeki dalgaları anlatan bir şarkı söyledi.»
   - Açıklama: Nehirdeki dalgalar şarkısı delikli sepet sorununa hiçbir katkı yapmayan işlevsiz bir ayrıntı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kendi sepetini ağabeyine sundu"
   - Cümle 7: «Sonra Niloya kendi sepetini ağabeyine sundu.»
   - Açıklama: 'Sunmak' 3 yaşındaki bir çocuğun bilmeyeceği resmi bir kelime; 'uzattı' ya da 'verdi' olmalı.
   - Açıklama: 'Sundu' resmi bir kelime, küçük çocuk için 'verdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0059` birebir aynı, `@degisim: sadık -> sağlam` (tutuyorsan), ardından `@onarim: 742b42f8efa8c34e73fa814768f9fb47921283bf`, sonra gövde.

### Hikâye 7: tohum niloya-0060 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0060
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'çekirdek', fiil 'karıştırmak', sıfat 'ekşi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: çiçeklerin yanından bilinmeyen bir ses geldi | başını kaldırıp çiçeklerden düşen çekirdekleri gördü
@tohum: niloya-0060
@degisim: ekşi -> kuru
Bir sabah Niloya evin bahçesinde oynuyordu. Birden çiçeklerin yanından küçük bir ses geldi. Niloya bu sesin nereden geldiğini bilmiyordu. Sesi ne çıkarıyordu? Niloya bu soruyu çok düşündü. Niloya çiçeklerin yanına yavaşça yürüdü. Yerdeki kuru yaprakları elleriyle karıştırdı. Ama yaprakların altında hiçbir şey yoktu. Sonra başını kaldırıp büyük sarı çiçeklere baktı. Rüzgar esince çiçeklerin başları sallanıyordu. Çiçeklerden küçük siyah çekirdekler düşüyordu. Çekirdekler yapraklara değince tık tık diye ses çıkarıyordu. Niloya çok sevindi, çünkü o küçük sesi yapan şeyi bulmuştu.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya bu soruyu çok düşündü."
   - Cümle 5: «Niloya bu soruyu çok düşündü.»
   - Açıklama: Sesin kaynağını bilmediği art arda üç cümlede tekrar ediliyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bu soruyu çok düşündü"
   - Cümle 5: «Niloya bu soruyu çok düşündü.»
   - Açıklama: Kartın özellik satırı Niloya'nın merak ettiğini sorduğunu söyler; burada kimseye soru sorulmuyor, soru yalnız içten düşünülüyor ve çözüme katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0060` birebir aynı, `@degisim: ekşi -> kuru` (tutuyorsan), ardından `@onarim: c9b814843560f911345aa49af613fc5ffa710139`, sonra gövde.

### Hikâye 8: tohum niloya-0063 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0063
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'üzüm', fiil 'düzeltmek', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: yağmur yüzünden bahçede piknik yapamadı | örtüyü odaya yayıp evde piknik yaptı
@tohum: niloya-0063
Yağmur pencereye tıp tıp vuruyordu. Niloya bir tabağa üzüm koymuştu ve bahçede piknik yapmak istiyordu. Ama yağmur yüzünden bahçeye çıkamadı. Niloya pencereden dışarı baktı ve biraz üzüldü. Sonra piknik örtüsünü odanın ortasına yaydı. Örtünün bir ucunu elleriyle düzeltti. Üzüm tabağını da örtünün üstüne bıraktı. Yağmurun sesi odaya kadar geliyordu. Niloya bu sese uyan neşeli bir yağmur şarkısı söyledi. Şarkı söylerken üzümlerini tek tek yedi. Evdeki piknik de çok eğlenceli oldu. Niloya çok sevinçliydi, çünkü yağmurlu günde de pikniğini yapmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu sese uyan neşeli"
   - Cümle 9: «Niloya bu sese uyan neşeli bir yağmur şarkısı söyledi.»
   - Açıklama: 'Sese uyan' soyut bir anlatım, 3 yaşındaki çocuk için anlaşılmaz.
   - Açıklama: 'Sese uyan' soyut ve 'uyan' emir kipiyle karışabilir; 3 yaşındaki çocuk anlamaz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "neşeli bir yağmur şarkısı söyledi"
   - Cümle 9: «Niloya bu sese uyan neşeli bir yağmur şarkısı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümüne katkı vermiyor, yalnız süs olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0063` birebir aynı, ardından `@onarim: 68bce27a6eb903639bd542a2d16f8a5b83d7c537`, sonra gövde.

### Hikâye 9: tohum niloya-0065 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0065
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'yaprak', fiil 'yuvarlamak', sıfat 'kilitli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: dedenin yırtık çantasından fındıklar döküldü | fındıkları bulup bir şarkı ile tek tek saydı
@tohum: niloya-0065
@degisim: kilitli -> yırtık
Yeşil tepede serin bir rüzgar esiyordu. Niloya dedesiyle çimenlerde oturmuş, fındık yiyordu. Birden dedenin yırtık çantasından on fındık döküldü. Fındıklar aşağıya, kuru yaprakların arasına yuvarlandı. "Aman, fındıklarım kayboldu!" dedi dede. "Üzülme, dedeciğim, ben hepsini bulurum," dedi Niloya. Niloya yavaşça aşağı indi ve yaprakları kaldırıp baktı. Fındıkları tek tek buldu ve avucunda topladı. Sonra dedesinin yanına döndü ve bir sayma şarkısı söyledi. Şarkıda her sayı geçince bir fındığı dedesine yuvarladı. Dede de şarkıya katıldı ve onları saydı. Şarkı bitince son fındık da dedenin eline ulaştı. Dede hepsini cebine koydu ve güldü. Niloya çok sevindi, çünkü dedesinin bütün fındıklarını bulmuştu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bir sayma şarkısı söyledi"
   - Cümle 9: «Sonra dedesinin yanına döndü ve bir sayma şarkısı söyledi.»
   - Açıklama: Fındıklar bulununca sorun çözülmüşken şarkıyla tek tek yuvarlayıp sayma sebebe yönelmeyen fazladan bir adım ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0065` birebir aynı, `@degisim: kilitli -> yırtık` (tutuyorsan), ardından `@onarim: 31b26939c937221a99d10a72318c4f2d9dbb4860`, sonra gövde.

### Hikâye 10: tohum niloya-0066 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0066
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çatal', fiil 'içmek', sıfat 'şık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: tek dal vardı ve ikisi aynı anda şarkı söyledi | sırayla şarkı söylemeyi önerdi ve dalı ağabeyine verdi
@tohum: niloya-0066
@degisim: şık -> neşeli
Ormanda kuşlar ötüyordu. Niloya ile Murat neşeli bir şarkı oyunu oynuyordu. Şarkı söyleyen, elinde çatal bir dal tutuyordu. Ama dal bir taneydi ve ikisi de aynı anda söylemek istedi. Sesleri birbirine karıştı ve şarkı bozuldu. Niloya biraz düşündü ve sırayla söylemeyi önerdi. Önce Niloya dalı tuttu ve fındık şarkısını söyledi. Murat onu dinledi ve alkışladı. Şarkı bitince Niloya dalı Murat'a verdi. Çok şarkı söylediği için biraz su içti. Bu sefer Murat top şarkısını söyledi. Niloya da ağabeyini sevinçle dinledi. Niloya ile Murat çok mutluydu, çünkü sırayla söyleyince şarkılar güzel olmuştu.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Şarkı söyleyen, elinde çatal bir dal tutuyordu.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor; ilk üç cümlede sorun yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Çok şarkı söylediği için biraz su içti"
   - Cümle 10: «Çok şarkı söylediği için biraz su içti.»
   - Açıklama: Öznesiz cümlede su içenin Niloya mı Murat mı olduğu belirsiz.
   - Açıklama: Öznesiz cümlede su içenin Niloya mı Murat mı olduğu belli değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok şarkı söylediği için biraz su içti"
   - Cümle 10: «Çok şarkı söylediği için biraz su içti.»
   - Açıklama: Su içme ayrıntısı olayda hiçbir işe yaramıyor ve kimin içtiği de belirsiz.
   - Açıklama: Su içme ayrıntısı kimin yaptığı belirsiz ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0066` birebir aynı, `@degisim: şık -> neşeli` (tutuyorsan), ardından `@onarim: bd61dfbc3ed77ab414c6e80affc6da2e8eb8024f`, sonra gövde.

### Hikâye 11: tohum niloya-0070 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0070
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'bot', fiil 'zıplamak', sıfat 'tuzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: botu ayağından çıktı ve yaprakların arasında kayboldu | dağılmış yaprakları açıp botunu buldu
@tohum: niloya-0070
@degisim: tuzlu -> kırmızı
Niloya ormanda kuru yaprakların üstünde zıplıyordu. Birden sağ botu ayağından çıktı ve uzağa fırladı. Bot yaprakların arasına düştü ve kayboldu. Niloya tek ayağıyla durdu ve etrafına baktı. Yerde bir sürü sarı yaprak vardı, ama bot görünmüyordu. Bot nereye düşmüştü? Niloya bu soruyu çok düşündü. Niloya önündeki yapraklara dikkatle baktı. Bir yerde yapraklar dağılmıştı. Niloya oradaki yaprakları elleriyle yavaşça kenara itti. Kırmızı botu yaprakların altında duruyordu. Niloya botu ayağına giydi ve bağcıklarını sıkıca bağladı. Niloya çok sevindi, çünkü kaybolan botunu bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dağılmış yaprakları açıp botunu"
   - Cümle 0 (plan satırı): «botu ayağından çıktı ve yaprakların arasında kayboldu | dağılmış yaprakları açıp botunu buldu»
   - Açıklama: Yapraklar açılmaz; 'kenara itip' gibi bir fiil olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dağılmış yaprakları açıp"
   - Cümle 0 (plan satırı): «botu ayağından çıktı ve yaprakların arasında kayboldu | dağılmış yaprakları açıp botunu buldu»
   - Açıklama: Yapraklar açılmaz; 'kenara itip' ya da 'aralayıp' olmalı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden sağ botu ayağından çıktı"
   - Cümle 2: «Birden sağ botu ayağından çıktı ve uzağa fırladı.»
   - Açıklama: Botun ayaktan neden çıktığı söylenmiyor; sorunun sebebi verilmiyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bu soruyu çok düşündü"
   - Cümle 7: «Niloya bu soruyu çok düşündü.»
   - Açıklama: Kartın 'sorar' özelliği ve güvenli kullanım satırı sorarak göstermeyi ister; Niloya kimseye soru sormuyor, soru çözüme bir iş görmüyor.
   - Açıklama: Tohumdaki soru özelliği kimseye sorulmuyor; kartta 'merak ettiği her şeyi sorar' denirken soru yalnız içinden düşünülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0070` birebir aynı, `@degisim: tuzlu -> kırmızı` (tutuyorsan), ardından `@onarim: 703ad45d35113dea4eadf022f2eba78dc4e4022b`, sonra gövde.

### Hikâye 12: tohum niloya-0071 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0071
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: sırayla oynamak
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'defter', fiil 'gezinmek', sıfat 'mor'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: kaplumbağa yavaş olduğu için hiç çiçek bulamadı | sırayla aradılar ve şarkıyla sırayı değiştirdiler
@tohum: niloya-0071
Bir sabah Niloya ile Tospik yeşil tepede çiçek arıyordu. Niloya mor çiçekleri defterinin arasına koymak istiyordu. Ama Tospik çok yavaştı ve çiçeklere hep Niloya önce ulaştı. Tospik hiç çiçek bulamadı ve başını kabuğuna çekti. Niloya bunu gördü ve sırayla aramayı önerdi. Sonra kısa bir şarkı söyledi. Şarkı bitene kadar yalnız Tospik kekiklerin arasında gezindi. Tospik yavaş yavaş yürüdü ve büyük, mor bir çiçek buldu. Niloya çiçeği defterin ilk sayfasına koydu. Sonra sıra Niloya'ya geçti ve Tospik bekledi. Defterin sayfaları çiçeklerle doldu. Niloya ile Tospik çok mutluydu, çünkü ikisi de çiçek bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yalnız Tospik kekiklerin arasında"
   - Cümle 7: «Şarkı bitene kadar yalnız Tospik kekiklerin arasında gezindi.»
   - Açıklama: 'Kekik' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0071` birebir aynı, ardından `@onarim: 5cc4dd974bb899f7d8041ad1b22989433316ae3b`, sonra gövde.
