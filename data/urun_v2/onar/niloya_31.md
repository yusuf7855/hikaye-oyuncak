# Editör görevi (onarım): Niloya, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0124
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kapak', fiil 'parıldamak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: şemsiye yırtıktı ve damlalar başına düştü | parka bakıp kaydırağın altında kuru bir yer buldu
@tohum: niloya-0124
@degisim: kapak -> şemsiye
Yağmur birden hızlı hızlı yağmaya başladı. Niloya parkta hemen şemsiyesini açtı. Ama şemsiye yırtıktı ve damlalar Niloya'nın başına düştü. Niloya kuru bir yer bulmak için merakla parka baktı. Kaydırağın altında küçük, kuru bir yer gördü. Oraya yürüdü ve yağmurdan korundu. Orada başı hiç ıslanmadı. Niloya şemsiyesini kapattı ve yanına koydu. Biraz sonra yağmur dindi ve güneş çıktı. Parktaki damlalar güneşte parıldadı. Niloya kaydırağın altından çıktı ve su birikintilerinin üstünden mutlu mutlu zıpladı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kuru bir yer bulmak için merakla parka baktı"
   - Cümle 4: «Niloya kuru bir yer bulmak için merakla parka baktı.»
   - Açıklama: Kuru yer arayan çocuk için 'merakla' kelimesi anlama uymuyor; 'dikkatle' ya da 'etrafına' daha doğru olurdu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0124` birebir aynı, `@degisim: kapak -> şemsiye` (tutuyorsan), ardından `@onarim: 792e3a1656d96a3b04b92f43cd4542ffb1058893`, sonra gövde.

### Hikâye 2: tohum niloya-0125 (deneme 1 -> 2)

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
@plan: yağmurda kaydırak ıslaktı ve kayamadı | saksıyı ters çevirip yağmurla şarkı söyledi
@tohum: niloya-0125
@degisim: kazanmak -> çevirmek
Parkta yağmur yağıyordu ve kaydırak çok ıslaktı. Niloya parkta bankın yanında tek başına duruyordu. Kaydıraktan kayamadı ve oynayacak başka bir şey aradı. Yerde boş bir saksı gördü. Niloya saksıyı ters çevirdi ve yağmurun altına koydu. Damlalar saksıya düşünce davul gibi güzel bir ses çıktı. Niloya bu sesle birlikte en sevdiği şarkıyı söyledi. Damlalar hızlı düşünce Niloya da hızlı söyledi. Damlalar yavaş düşünce Niloya da yavaş söyledi. Niloya yağmurlu parkta yeni oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (8):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kaydırak ıslaktı ve kayamadı"
   - Cümle 0 (plan satırı): «yağmurda kaydırak ıslaktı ve kayamadı | saksıyı ters çevirip yağmurla şarkı söyledi»
   - Açıklama: Plan satırında 'kayamadı' fiilinin öznesi kaydırak oluyor; kaydırak kaymaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yağmurla şarkı söyledi"
   - Cümle 0 (plan satırı): «yağmurda kaydırak ıslaktı ve kayamadı | saksıyı ters çevirip yağmurla şarkı söyledi»
   - Açıklama: Plan satırında 'yağmurla şarkı söyledi' mecazlı bir anlatım.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kaydırak ıslaktı ve kayamadı"
   - Cümle 0 (plan satırı): «yağmurda kaydırak ıslaktı ve kayamadı | saksıyı ters çevirip yağmurla şarkı söyledi»
   - Açıklama: Plan satırında 'kayamadı' fiilinin öznesi kaydırak gibi okunuyor; kayamayan Niloya belirtilmemiş.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bankın yanında tek başına duruyordu"
   - Cümle 2: «Niloya parkta bankın yanında tek başına duruyordu.»
   - Açıklama: Küçük çocuk yağmurlu parkta yetişkin olmadan tek başına kalıyor; taklit edilince güvensiz.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya parkta bankın yanında"
   - Cümle 2: «Niloya parkta bankın yanında tek başına duruyordu.»
   - Açıklama: 'Parkta' bir önceki cümlede söylendi; gereksiz tekrar.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kaydıraktan kayamadı ve oynayacak başka bir şey aradı"
   - Cümle 3: «Kaydıraktan kayamadı ve oynayacak başka bir şey aradı.»
   - Açıklama: Çözüm ıslak kaydırağa yönelmiyor, sorun bırakılıp başka bir oyuna geçiliyor.
   - Açıklama: Çözüm ıslak kaydırağa yönelmiyor, sorunu bırakıp başka bir oyuna geçiyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yerde boş bir saksı gördü"
   - Cümle 4: «Yerde boş bir saksı gördü.»
   - Açıklama: Saksı sebepsizce beliriyor ve çözümü kendiliğinden getiriyor.
   - Açıklama: Saksı parkta sebepsizce beliriyor ve çözümü hazır getiriyor.
8. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Niloya yağmurlu parkta yeni oyununa mutlu mutlu devam etti"
   - Cümle 10: «Niloya yağmurlu parkta yeni oyununa mutlu mutlu devam etti.»
   - Açıklama: Kaydıraktan kayma hedefine hiç ulaşılmıyor; sorun çözülmeden hikaye bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0125` birebir aynı, `@degisim: kazanmak -> çevirmek` (tutuyorsan), ardından `@onarim: 7014e9da5b053229d24ec843b1a9a9aae01e99e2`, sonra gövde.

### Hikâye 3: tohum niloya-0126 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0126
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'pilav', fiil 'okşamak', sıfat 'şeffaf'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: boş kap hiç ses çıkarmadı | kaba fındık koyup şarkı söylerken salladı
@tohum: niloya-0126
@degisim: okşamak -> sallamak
Niloya ormanda pilavını bitirdi ve şeffaf kabı boşaldı. Niloya kabından ses çıkaran bir oyuncak yapmak istedi. Ama kabı salladı ve hiç ses çıkmadı. Niloya yerdeki fındıklardan üç tane topladı ve kaba koydu. Kabın kapağını sıkıca taktı. Sonra kabı salladı ve en sevdiği şarkıyı söyledi. Ama şarkı söylerken fındıkların sesi duyulmadı. Niloya kaba bir avuç fındık daha koydu. Şimdi fındıklar kabın içinde yüksek bir ses çıkardı. Niloya yeni oyuncağını sallayarak ormanda mutlu mutlu dolaştı.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kaba fındık koyup şarkı söylerken salladı"
   - Cümle 0 (plan satırı): «boş kap hiç ses çıkarmadı | kaba fındık koyup şarkı söylerken salladı»
   - Açıklama: Plan asıl çözümü, yani kaba bir avuç fındık daha koymayı söylemiyor; şarkı söylerken sallamak işe yaramıyor.
   - Açıklama: Plandaki çözüm gövdede işe yaramıyor; asıl çözüm kaba daha çok fındık koymak.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve şeffaf kabı boşaldı"
   - Cümle 1: «Niloya ormanda pilavını bitirdi ve şeffaf kabı boşaldı.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kabı salladı ve en sevdiği şarkıyı söyledi"
   - Cümle 6: «Sonra kabı salladı ve en sevdiği şarkıyı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunu çözmüyor; sesi fındık eklemek sağlıyor, özellik işe yarar biçimde kullanılmamış.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "şarkı söylerken fındıkların sesi duyulmadı"
   - Cümle 7: «Ama şarkı söylerken fındıkların sesi duyulmadı.»
   - Açıklama: Tohumdaki şarkı özelliği sorunu çözmekte işe yaramıyor; çözümü daha çok fındık koymak sağlıyor.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama şarkı söylerken fındıkların sesi duyulmadı"
   - Cümle 7: «Ama şarkı söylerken fındıkların sesi duyulmadı.»
   - Açıklama: İlk sorun çözüldükten sonra şarkı sesinin fındık sesini bastırması ikinci bir sorun olarak ekleniyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ama şarkı söylerken fındıkların sesi duyulmadı"
   - Cümle 7: «Ama şarkı söylerken fındıkların sesi duyulmadı.»
   - Açıklama: İlk çözüm işe yaramıyor ve sorun ancak üçüncü bir adımla, bir avuç fındık daha eklenerek çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0126` birebir aynı, `@degisim: okşamak -> sallamak` (tutuyorsan), ardından `@onarim: d2fe6ca8d883cd04d33080c46d632743168b1548`, sonra gövde.

### Hikâye 4: tohum niloya-0127 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0127
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'eldiven', fiil 'kalmak', sıfat 'neşeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: tık tık diye garip bir ses geldi | orada kim olduğunu sordu ve düşen fındıkları gördü
@tohum: niloya-0127
Rüzgar esiyordu ve fındık ağaçlarının dalları sallanıyordu. Niloya ormanda eldivenleriyle fındık topluyordu. Birden arkasından tık tık diye garip bir ses geldi. Niloya bu sesi çok merak etti. Etrafa baktı ama hiçbir şey göremedi. Niloya yüksek sesle orada kim olduğunu sordu. Hiç cevap gelmedi, ama tık tık sesi yine duyuldu. Demek ki orada kimse yoktu. Niloya yere eğildi ve dikkatle baktı. Rüzgar esince dallardan fındıklar düşüyordu. Fındıklar yerdeki kuru dallara çarpıp o sesi çıkarıyordu. Niloya neşeli bir sesle güldü. Düşen fındıkları tek tek topladı ve yerde hiç fındık kalmadı. Niloya bundan sonra ormanda fındık düşünce o sesi hemen tanıdı.
```

**Hakem bulguları (5):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden arkasından tık tık diye garip bir ses geldi"
   - Cümle 3: «Birden arkasından tık tık diye garip bir ses geldi.»
   - Açıklama: Ormanda yalnız kalan Niloya'nın arkasından gelen, kaynağı bilinmeyen garip ses ve cevapsız 'kim var' sorusu küçük çocuk için korkutucu bir gerilim kuruyor.
   - Açıklama: Tek başına ormandaki Niloya'nın arkasından gelen, cevapsız kalan garip ses küçük çocuk için ürkütücü olabilir.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Niloya yüksek sesle orada kim olduğunu sordu"
   - Cümle 6: «Niloya yüksek sesle orada kim olduğunu sordu.»
   - Açıklama: Sormak sebebe yönelmiyor, cevapsız kalınca 'kimse yoktu' diye temelsiz bir çıkarım yapılıyor ve sebep ancak etrafa bakma, sorma, yere eğilme adımlarından sonra bulunuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Demek ki orada kimse yoktu"
   - Cümle 8: «Demek ki orada kimse yoktu.»
   - Açıklama: 'Demek ki' soyut çıkarım kalıbı küçük çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Demek ki orada kimse"
   - Cümle 8: «Demek ki orada kimse yoktu.»
   - Açıklama: 'Demek ki' çıkarım bağlacı soyut ve 3 yaşındaki çocuğa uygun değil.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Demek ki orada kimse yoktu"
   - Cümle 8: «Demek ki orada kimse yoktu.»
   - Açıklama: Cevap gelmemesinden kimsenin olmadığı sonucu çıkarılıyor; bu mantık hatalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0127` birebir aynı, ardından `@onarim: fd9f8586d500dc83e5dfceb61043a26e5a749c5b`, sonra gövde.

### Hikâye 5: tohum niloya-0128 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0128
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'domates', fiil 'düşünmek', sıfat 'meraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağanın karnı açtı ama yiyecek bulamadı | ne istediğini sordu ve ona küçük bir domates verdi
@tohum: niloya-0128
Bahçede sıcak bir öğle vaktiydi. Niloya domateslerin yanında oturuyordu ve Tospik yavaşça yanına geldi. Tospik'in karnı açtı, ama bahçede yiyecek bir şey bulamamıştı. "Tospik, ne yemek istersin?" diye sordu Niloya. Tospik biraz düşündü. "Kırmızı ve sulu bir şey istiyorum," dedi Tospik. Sonra meraklı gözlerle domateslere baktı. Ama kırmızı domatesler Tospik için çok yüksekteydi. Niloya en kırmızı olanı dalından kopardı. Onu Tospik'in önüne, yere koydu. Tospik onu yavaş yavaş yedi. "Çok lezzetli, teşekkürler, Niloya!" dedi Tospik. Niloya bundan sonra bahçede Tospik için hep küçük bir domates ayırdı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede sıcak bir öğle vaktiydi"
   - Cümle 1: «Bahçede sıcak bir öğle vaktiydi.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Niloya bundan sonra bahçede Tospik için hep küçük bir domates ayırdı"
   - Cümle 13: «Niloya bundan sonra bahçede Tospik için hep küçük bir domates ayırdı.»
   - Açıklama: Son cümle bir ders değil, sonraki günlere atlayan bir alışkanlık anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0128` birebir aynı, ardından `@onarim: 6a5bc065d69aec5ab740f06012214310868ccb10`, sonra gövde.

### Hikâye 6: tohum niloya-0131 (deneme 1 -> 2)

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
@plan: kaplumbağa küçük ağaçların arasında yolunu kaybetti | şarkı söyledi ve kaplumbağa sesi izleyip geldi
@tohum: niloya-0131
Niloya bahçede Tospik için lezzetli bir marul yaprağı kopardı. Ama Tospik sık fidanların arasında yolunu kaybetmişti. "Niloya, buradan çıkamıyorum!" diye seslendi Tospik. Fidanlar çok küçüktü ve Niloya onlara basmak istemedi. Niloya biraz düşündü. "Tospik, sesimi izle ve gel!" dedi Niloya. Sonra en sevdiği şarkıyı söylemeye başladı. Tospik şarkıyı duydu ve sese doğru yavaş yavaş yürüdü. Sonunda yaprakların arasından başını çıkardı. Niloya marul yaprağını ona uzattı. Tospik yaprağı hemen yedi. "Teşekkürler, Niloya, hem şarkın hem de yaprak çok güzeldi!" dedi Tospik.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Tospik sık fidanların arasında"
   - Cümle 2: «Ama Tospik sık fidanların arasında yolunu kaybetmişti.»
   - Açıklama: 'Sık' ve 'fidan' 3 yaşındaki çocuğun bilmediği kelimeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0131` birebir aynı, ardından `@onarim: d563bb44eacc5a8d00943594e9e905ae65f7c905`, sonra gövde.

### Hikâye 7: tohum niloya-0132 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Tospik
@tohum: niloya-0132
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'hazine', fiil 'basmak', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | Tospik
@plan: kaplumbağa acıktı ama elmalar çok yüksekteydi | merakla etrafa bakıp yere düşmüş elmaları buldu
@tohum: niloya-0132
Rüzgar hafifçe esiyordu. Niloya ile Tospik ormanda elma ağaçlarının altında yürüyordu. Tospik acıkmıştı, ama elmalar dallarda çok yüksekteydi. "Niloya, ben o elmalara yetişemem," dedi Tospik. Niloya ağaçların altına merakla baktı. Sonra aydınlık bir yere doğru yürüdü. Orada, güneşin altında, düşmüş kırmızı elmalar vardı. Niloya elmalara basmamak için dikkatle yürüdü. "Tospik, buraya gel, elma buldum!" dedi Niloya. Tospik yavaş yavaş geldi ve elmaları gördü. Niloya en yumuşak elmayı onun önüne koydu. Tospik elmayı keyifle yedi. "Burası bir hazine gibi, teşekkürler, Niloya!" dedi Tospik.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "merakla etrafa bakıp yere"
   - Cümle 0 (plan satırı): «kaplumbağa acıktı ama elmalar çok yüksekteydi | merakla etrafa bakıp yere düşmüş elmaları buldu»
   - Açıklama: Plan çözümünde özne belirsiz; sorundaki öznesi kaplumbağa olduğu için arayan kaplumbağa sanılıyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Tospik acıkmıştı, ama elmalar"
   - Cümle 3: «Tospik acıkmıştı, ama elmalar dallarda çok yüksekteydi.»
   - Açıklama: 'ama' bağlacından önce virgül gereksiz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra aydınlık bir yere doğru yürüdü"
   - Cümle 6: «Sonra aydınlık bir yere doğru yürüdü.»
   - Açıklama: Niloya'nın aydınlık yere neden gittiği söylenmiyor ve düşmüş elmalar ağaçların altında değil orada sebepsizce beliriyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Burası bir hazine gibi"
   - Cümle 13: «"Burası bir hazine gibi, teşekkürler, Niloya!" dedi Tospik.»
   - Açıklama: 'Hazine gibi' benzetmesi mecazdır.
   - Açıklama: 'Hazine gibi' benzetmesi mecaz ve küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0132` birebir aynı, ardından `@onarim: 9d6fd573a59991f251e00bbe9250f4d70075251c`, sonra gövde.

### Hikâye 8: tohum niloya-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0133
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'bağcık', fiil 'dizmek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: fındıklar çok fazlaydı ve sayarken karışıyordu | şarkı söyleyip sırayla birer fındık dizdiler
@tohum: niloya-0133
@degisim: saygılı -> uzun
Yapraklar hışır hışır sallanıyordu. Niloya ile Murat ormanda bir torba fındık toplamıştı. Fındıkları paylaşmak istediler, ama fındıklar çok fazlaydı ve sayarken karışıyordu. Murat torbanın bağcığını açtı. Niloya biraz düşündü ve bir şarkı söylemeye başladı. Şarkı sürerken ikisi de sırayla birer fındık aldı. Fındıkları kütüğün üstüne iki uzun sıra halinde dizdiler. Torbada fındık bitene kadar şarkıyı söylediler. Sonunda iki sırada da aynı sayıda fındık vardı. Murat sevinçle ellerini çırptı. Niloya bundan sonra bir şeyi paylaşırken hep bu şarkıyı söyledi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fındıklar çok fazlaydı ve sayarken karışıyordu"
   - Cümle 3: «Fındıkları paylaşmak istediler, ama fındıklar çok fazlaydı ve sayarken karışıyordu.»
   - Açıklama: Karışan fındıklar değil sayım olduğu halde fiil fındıklara bağlanmış, özne-fiil uyumu anlamca bozuk.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve sayarken karışıyordu"
   - Cümle 3: «Fındıkları paylaşmak istediler, ama fındıklar çok fazlaydı ve sayarken karışıyordu.»
   - Açıklama: Fındıklar karışmaz, sayan çocuklardır; özne ile fiil uyuşmuyor, sayı karışıyordu olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çok fazlaydı ve sayarken karışıyordu"
   - Cümle 3: «Fındıkları paylaşmak istediler, ama fındıklar çok fazlaydı ve sayarken karışıyordu.»
   - Açıklama: Plan satırında da sayarken karışan fındıklar olarak yazılmış; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0133` birebir aynı, `@degisim: saygılı -> uzun` (tutuyorsan), ardından `@onarim: 27a921134051cfc03ae530468c396307c0b7ee57`, sonra gövde.

### Hikâye 9: tohum niloya-0134 (deneme 1 -> 2)

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
@plan: rüzgar şapkayı yüksek otların arasına götürdü | rüzgarın yönünü sordu ve o yöne gidip şapkayı buldu
@tohum: niloya-0134
@degisim: patates -> şapka
Rüzgar birden sertçe esti. Niloya ormanda koşturuyordu ve sarı şapkası başından uçtu. Şapka yüksek otların arasına düştü ve kayboldu. Niloya otların arasına baktı ama şapkasını göremedi. Niloya durdu ve kendine bir soru sordu. Rüzgar hangi yöne esiyordu? Niloya ağaçların dallarına baktı. Dallar hep aynı yöne doğru sallanıyordu. Niloya o yöne doğru yavaşça yürüdü. Otları elleriyle araladı ve dikkatle baktı. Şapkası bir çalının dibinde duruyordu. Niloya şapkayı aldı ve başına sıkıca taktı. Niloya çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "kendine bir soru sordu"
   - Cümle 5: «Niloya durdu ve kendine bir soru sordu.»
   - Açıklama: Niloya kendi kendine soru soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0134` birebir aynı, `@degisim: patates -> şapka` (tutuyorsan), ardından `@onarim: 0a21a16885a7116e35f59ee62514063730a4cdef`, sonra gövde.

### Hikâye 10: tohum niloya-0137 (deneme 1 -> 2)

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
@plan: yıldız için kırmızı taş gerekiyordu ama yerde yoktu | merakla etrafa bakıp kütüğün dibinde kırmızı taşlar buldu
@tohum: niloya-0137
Ormanda, fındık ağaçlarının altında, Niloya ile Mete oynuyordu. Niloya, Mete'ye taşlardan sürpriz bir yıldız yapmak istedi. Mete kırmızıyı çok severdi, ama yerde hiç kırmızı taş yoktu. "Gözlerini kapat, Mete, bana güven," dedi Niloya. Mete gözlerini kapattı ve bir ağaca yaslandı. Niloya merakla etrafta dolaştı. Yaprakların altına ve kütüklerin yanına baktı. Bir kütüğün dibinde küçük kırmızı taşlar buldu. Niloya bu taşlarla yere büyük bir yıldız yaptı. "Şimdi aç, Mete!" dedi Niloya. Mete yıldızı gördü ve sevinçle zıpladı. "Benim için mi, çok güzel!" dedi Mete. Niloya çok sevindi, çünkü Mete sürprizini çok sevmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bana güven"
   - Cümle 4: «"Gözlerini kapat, Mete, bana güven," dedi Niloya.»
   - Açıklama: 'Güven' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çünkü Mete sürprizini çok sevmişti"
   - Cümle 13: «Niloya çok sevindi, çünkü Mete sürprizini çok sevmişti.»
   - Açıklama: 'Sürprizini' iyelik eki sürprizin Mete'nin kendisine ait olduğunu gösteriyor; kimin sürprizi olduğu belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0137` birebir aynı, ardından `@onarim: 5464e9b4ccd91d0110853d0b7a0e4b8cba8ea46a`, sonra gövde.

### Hikâye 11: tohum niloya-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0138
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'patik', fiil 'açılmak', sıfat 'ucuz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: oyuncak bebeğin ayağındaki bağ açıldı | ağabeyinden yardım isteyip bağlamayı öğrendi
@tohum: niloya-0138
@degisim: ucuz -> yumuşak
Ormanda, fındık ağaçlarının altında, Niloya oyuncak bebeğiyle oynuyordu. Oyuncak bebeğin ayağında yumuşak, küçük patikler vardı. Birden patiklerden birinin bağı açıldı ve o yere düştü. Niloya bağı bağlamaya çalıştı, ama fiyonk yapmayı bilmiyordu. "Abi, bana fiyonk yapmayı gösterir misin?" diye sordu Niloya. Murat hemen yanına oturdu. "Önce iki halka yap, sonra onları birbirine geçir," dedi Murat. Niloya patiği ayağa taktı, iki küçük halka yaptı ve sıkıca bağladı. Artık patik hiç düşmedi. "Oldu, abiciğim!" dedi Niloya. Murat gülümsedi ve başını okşadı. Niloya çok sevindi, çünkü fiyonk yapmayı öğrenmişti.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bağı açıldı ve o yere düştü"
   - Cümle 3: «Birden patiklerden birinin bağı açıldı ve o yere düştü.»
   - Açıklama: 'O' zamirinin bağı mı patiği mi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "açıldı ve o yere düştü"
   - Cümle 3: «Birden patiklerden birinin bağı açıldı ve o yere düştü.»
   - Açıklama: 'o' zamirinin bağı mı patiği mi gösterdiği belli değil.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Niloya patiği ayağa taktı"
   - Cümle 8: «Niloya patiği ayağa taktı, iki küçük halka yaptı ve sıkıca bağladı.»
   - Açıklama: İyelik eki eksik; 'bebeğin ayağına' olmalı.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Niloya patiği ayağa taktı"
   - Cümle 8: «Niloya patiği ayağa taktı, iki küçük halka yaptı ve sıkıca bağladı.»
   - Açıklama: Hangi ayak olduğu belli değil; 'bebeğin ayağına' olmalı.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Murat gülümsedi ve başını okşadı"
   - Cümle 11: «Murat gülümsedi ve başını okşadı.»
   - Açıklama: 'başını' kimin başı olduğu belli değil; 'Niloya'nın başını' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0138` birebir aynı, `@degisim: ucuz -> yumuşak` (tutuyorsan), ardından `@onarim: 8cbc3a1816a2bca139da93012659a9af6ef1238d`, sonra gövde.
