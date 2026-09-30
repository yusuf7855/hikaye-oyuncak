# Editör görevi (onarım): Keloğlan, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar47.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0167 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0167
- yer: dağ (Köyün yakınındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'un', fiil 'süslenmek', sıfat 'geniş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: anası tabağı süslemek istedi ama yakında çiçek yoktu | tepeye dikkatle bakıp taşın arkasında çiçek buldu
@tohum: keloglan-0167
@degisim: un -> kek
Tepenin üstü geniş ve düzdü. Keloğlan ile anası orada piknik yapıyordu. Anası kekin tabağını çiçeklerle süslemek istiyordu ama yakında hiç çiçek yoktu. "Ben sana çiçek bulurum, anneciğim," dedi Keloğlan. Keloğlan tepenin kenarına yürüdü ve her yere dikkatle baktı. Büyük bir taşın arkasında bir sürü sarı çiçek vardı! Keloğlan birkaç çiçek topladı. Biraz sakardı ve dönerken iki çiçeği düşürdü. Hemen eğildi, onları da aldı ve anasına götürdü. "Çiçekler taşın arkasındaymış, anneciğim!" dedi Keloğlan. Anası çiçekleri tabağın kenarına dizdi ve kekin tabağı güzelce süslendi. Keloğlan ile anası kekten birer dilim alıp mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan tepenin kenarına yürüdü"
   - Cümle 5: «Keloğlan tepenin kenarına yürüdü ve her yere dikkatle baktı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde yüksek bir tepenin kenarına yalnız gidiliyor.
   - Açıklama: Tepenin kenarına yürümek çocuğun taklit edebileceği yüksek yer kenarı davranışı olabilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Biraz sakardı ve dönerken iki çiçeği düşürdü"
   - Cümle 8: «Biraz sakardı ve dönerken iki çiçeği düşürdü.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sakardı ve dönerken iki çiçeği düşürdü"
   - Cümle 8: «Biraz sakardı ve dönerken iki çiçeği düşürdü.»
   - Açıklama: Çiçeklerin düşürülüp hemen geri alınması olayda hiçbir işe yaramayan, özelliği göstermek için eklenmiş bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0167` birebir aynı, `@degisim: un -> kek` (tutuyorsan), ardından `@onarim: af4798cf1cdc41ff525da15d4a6a3b4bb7a38639`, sonra gövde.

### Hikâye 2: tohum keloglan-0168 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0168
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çalı', fiil 'örtmek', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: güneş çamurdan pastayı kuruttu ve pasta çatladı | çalının altında ıslak çamur bulup pastayı yapraklarla örttü
@tohum: keloglan-0168
Güneş büyük ağaçların arasından sıcak sıcak parlıyordu. Keloğlan ormanda çamurdan pasta yapma oyunu oynuyordu. Ama güneş pastayı kuruttu ve pastanın üstü çatladı. Keloğlan krema sürmek istedi, ama elindeki çamur da kurudu. Keloğlan etrafına baktı ve büyük bir çalı gördü. Elini çalının altındaki toprağa soktu. Oradaki toprak ıslak ve yumuşaktı. Keloğlan yeni bir şey öğrendi: gölgede çamur ıslak kalıyordu. Yumuşak topraktan bir avuç aldı ve pastanın üstüne sürdü. Sonra pastanın üstünü büyük yapraklarla örttü. Biraz bekledi ve yaprakları kaldırdı. Krema yine ıslak ve parlaktı. Keloğlan çok sevindi, çünkü kremalı pastasını sonunda bitirmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan krema sürmek istedi"
   - Cümle 4: «Keloğlan krema sürmek istedi, ama elindeki çamur da kurudu.»
   - Açıklama: Çamur açıklanmadan 'krema' diye anılıyor; kelime yanlış anlamda.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra pastanın üstünü büyük yapraklarla örttü"
   - Cümle 10: «Sonra pastanın üstünü büyük yapraklarla örttü.»
   - Açıklama: Çözüm ıslak çamur bulma, sürme, yapraklarla örtme, bekleme ve açma adımlarına yayılıyor ve çatlayan pastanın kendisine değil kremaya yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0168` birebir aynı, ardından `@onarim: a7aecfb8524f3e71ce6039a6730ef7336ef46e78`, sonra gövde.

### Hikâye 3: tohum keloglan-0171 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0171
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'düğme', fiil 'boşaltmak', sıfat 'mutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: arkadaşı düğme oyunu biliyordu ama düğmesi yoktu | cebini boşalttı ve düğmelerini paylaştı
@tohum: keloglan-0171
Keloğlan, Balkız ile şatonun bahçesinde oturuyordu. Keloğlan'ın cebi renkli düğmelerle doluydu. Balkız düğmeyle oynanan bir oyun biliyordu, ama hiç düğmesi yoktu. "Bu oyunu bana öğretir misin, Balkız?" diye sordu Keloğlan. "Öğretirim, ama bana da düğme lazım," dedi Balkız. Keloğlan hemen cebini çimenlere boşalttı. Onları ikiye ayırdı ve yarısını Balkız'a verdi. Balkız parmağıyla bir düğmeyi itti ve başka bir düğmeyi vurdu. "Vurduğun düğme senin olur," dedi Balkız. Keloğlan da kendi düğmesini itti ve bir tane kazandı. Keloğlan çok mutluydu, çünkü paylaşınca yeni bir oyun öğrenmişti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onları ikiye ayırdı ve"
   - Cümle 7: «Onları ikiye ayırdı ve yarısını Balkız'a verdi.»
   - Açıklama: 'Onları' zamiri önceki cümlede düğmeler anılmadığı için belirsiz; önceki nesne 'cebini'.
   - Açıklama: 'Onları' zamiri önceki cümledeki 'cebini'ye bağlanıyor, düğmeleri gösterdiği belli değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "başka bir düğmeyi vurdu"
   - Cümle 8: «Balkız parmağıyla bir düğmeyi itti ve başka bir düğmeyi vurdu.»
   - Açıklama: Çarpma anlamında 'vurmak' yönelme eki ister: 'başka bir düğmeye vurdu'.
   - Açıklama: 'Vurmak' burada yönelme eki ister; 'düğmeye vurdu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0171` birebir aynı, ardından `@onarim: 315b1411531246aa0d6cbe9e3b465db537b745a6`, sonra gövde.

### Hikâye 4: tohum keloglan-0172 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0172
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'filiz', fiil 'çıkarmak', sıfat 'reçelli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: ikisi aynı anda sepete el soktu ve oyun karıştı | önce arkadaşını izledi ve sırayla oynadılar
@tohum: keloglan-0172
Büyük ağaçlarda kuşlar ötüyordu. Keloğlan ile Balkız ormanda sepetle bir tahmin oyunu oynuyordu. Ama ikisi de gözlerini kapadı ve ellerini aynı anda sepete soktu. Elleri çarpıştı ve kimse bir şey çıkaramadı. "Balkız, önce sen oyna, ben de oyunu öğreneyim," dedi Keloğlan. Balkız gözlerini kapadı ve sepetten bir şey çıkardı. "Bu sert bir kozalak!" dedi Balkız. Keloğlan onu dikkatle izledi. Sonra sıra ona geldi. Keloğlan gözlerini kapadı ve yapışkan bir şey tuttu. "Bu reçelli ekmek!" diye güldü Keloğlan. Balkız da sırası gelince küçük bir filiz buldu. İki arkadaş çok eğlendi, çünkü sırayla oyun çok güzel olmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir tahmin oyunu oynuyordu"
   - Cümle 2: «Keloğlan ile Balkız ormanda sepetle bir tahmin oyunu oynuyordu.»
   - Açıklama: 'Tahmin' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ben de oyunu öğreneyim"
   - Cümle 5: «"Balkız, önce sen oyna, ben de oyunu öğreneyim," dedi Keloğlan.»
   - Açıklama: İkisi zaten oyunu oynuyorken Keloğlan'ın oyunu yeni öğrenecekmiş gibi konuşması çelişkili.
   - Açıklama: İkisi zaten oyunu oynuyorken Keloğlan oyunu öğrenmek istediğini söylüyor; bu bir çelişki.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir filiz buldu"
   - Cümle 12: «Balkız da sırası gelince küçük bir filiz buldu.»
   - Açıklama: 'filiz' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü sırayla oyun çok güzel olmuştu"
   - Cümle 13: «İki arkadaş çok eğlendi, çünkü sırayla oyun çok güzel olmuştu.»
   - Açıklama: 'Sırayla oyun' bozuk bir yapı; 'sırayla oynamak' olmalı.
   - Açıklama: 'sırayla oyun' dilbilgisel değil; 'sırayla oynamak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0172` birebir aynı, ardından `@onarim: 6c85bac85a61b923209e138f783b004e00563552`, sonra gövde.

### Hikâye 5: tohum keloglan-0173 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0173
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tablo', fiil 'sıçratmak', sıfat 'ucuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek de oyuna katılmak istedi ama fırça tutamazdı | dalla boya sıçratmayı öğrendi ve eşeğin kuyruğunu boyaya batırdı
@tohum: keloglan-0173
@degisim: ucuz -> mavi
Ormanda rüzgar serin serin esiyordu. Keloğlan büyük bir ağacın dibinde tahtaya mavi boyayla bir tablo yapıyordu. Eşeği Karakaçan da oyuna katılmak istedi ama fırça tutamazdı. Keloğlan bir dalı boyaya batırdı ve hafifçe salladı. Boya tahtaya küçük noktalar halinde sıçradı. Keloğlan böylece dalla boya sıçratmayı öğrendi. Karakaçan'ın kuyruğu da dal gibi sallanıyordu! Keloğlan kuyruğun ucunu boyaya hafifçe batırdı. "Sıra sende, Karakaçan," dedi Keloğlan. Karakaçan kuyruğunu salladı ve tahtaya mavi noktalar sıçradı. Sonra sıra yine Keloğlan'a geldi. Keloğlan ile Karakaçan sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "mavi boyayla bir tablo yapıyordu"
   - Cümle 2: «Keloğlan büyük bir ağacın dibinde tahtaya mavi boyayla bir tablo yapıyordu.»
   - Açıklama: 'Tablo' kelimesini 3 yaşındaki çocuk bilmeyebilir; 'resim' daha uygun.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir tablo yapıyordu"
   - Cümle 2: «Keloğlan büyük bir ağacın dibinde tahtaya mavi boyayla bir tablo yapıyordu.»
   - Açıklama: 'Tablo' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'resim' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuyruğu da dal gibi sallanıyordu"
   - Cümle 7: «Karakaçan'ın kuyruğu da dal gibi sallanıyordu!»
   - Açıklama: Benzetme içeren mecazlı anlatım 3 yaşındaki çocuğa uygun değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kuyruğun ucunu boyaya hafifçe batırdı"
   - Cümle 8: «Keloğlan kuyruğun ucunu boyaya hafifçe batırdı.»
   - Açıklama: Bir hayvanın kuyruğunu boyaya batırmak çocuğun evcil hayvanlarda taklit edebileceği güvensiz bir davranıştır.
   - Açıklama: Çocuk bir hayvanın kuyruğunu boyaya batırmayı taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0173` birebir aynı, `@degisim: ucuz -> mavi` (tutuyorsan), ardından `@onarim: da527690d5e5a80325afb19a8354f3de13bdf01f`, sonra gövde.

### Hikâye 6: tohum keloglan-0174 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0174
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'köfte', fiil 'karışmak', sıfat 'vanilyalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: köfte hamuru iyi olmamıştı ve elde dağıldı | doğruyu söyledi ve hamuru iyice ezdi
@tohum: keloglan-0174
@degisim: vanilyalı -> yuvarlak
Köy evinin mutfağında Keloğlan ile anası lokanta oyunu oynuyordu. "Bana bir tabak köfte, lütfen," dedi anası. Ama köfte hamuru iyi olmamıştı ve Keloğlan'ın elinde dağıldı. Keloğlan dürüst davrandı ve anasına söyledi: "Anneciğim, köfteler dağılıyor." "Hamuru biraz daha ez," dedi anası. Keloğlan hamuru iki eliyle uzun uzun ezdi. Sonunda ekmek ve et iyice karıştı. Keloğlan küçük bir parça aldı ve yuvarladı. Bu kez köfte bozulmadı, yuvarlak ve düzgün oldu. Keloğlan köfteleri bir tepsiye dizdi ve anasına götürdü. "Ne güzel köfteler!" dedi anası ve güldü. Keloğlan bundan sonra köfte yaparken hamuru iyice ezdi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iyi olmamıştı ve elde dağıldı"
   - Cümle 0 (plan satırı): «köfte hamuru iyi olmamıştı ve elde dağıldı | doğruyu söyledi ve hamuru iyice ezdi»
   - Açıklama: İyelik eki eksik; plan satırında 'elinde dağıldı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "köfte hamuru iyi olmamıştı"
   - Cümle 3: «Ama köfte hamuru iyi olmamıştı ve Keloğlan'ın elinde dağıldı.»
   - Açıklama: Hamurun neden iyi olmadığı söylenmiyor; sebep ancak çözümde anneden öğreniliyor.
   - Açıklama: Hamurun neden dağıldığı söylenmiyor; 'iyi olmamıştı' bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0174` birebir aynı, `@degisim: vanilyalı -> yuvarlak` (tutuyorsan), ardından `@onarim: 3cb9f137f868085116da9eb91fc1c0110fd4774e`, sonra gövde.

### Hikâye 7: tohum keloglan-0175 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0175
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'topaç', fiil 'kilitlemek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: topaç uzun çimenlerin üstünde dönmeden devrildi | nedenini öğrendi ve topacı düz bir taşın üstünde döndürdü
@tohum: keloglan-0175
@degisim: kilitlemek -> sarmak
Tepede güneşli ve güzel bir gündü. Keloğlan yeni tahta topacını döndürmek istiyordu. Ama çimenler uzundu ve topaç hemen devrildi. Keloğlan ipi yeniden sardı ve topacı bir daha attı. Topaç bu kez biraz sallandı ve yine yan yattı. Keloğlan kahkahalarla güldü. Sonra nedenini öğrenmek istedi. Yere eğildi ve çimenlere dikkatle baktı. Topaç uzun çimenlere takılıyordu. Keloğlan yakında büyük ve düz bir taş buldu. İpi yavaş yavaş ve sabırlı bir şekilde sardı. Topacı taşın üstüne attı ve topaç hızlı hızlı döndü. Keloğlan sevinçle ellerini çırptı. Keloğlan bundan sonra topacını hep düz bir yerde döndürdü.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan yakında büyük ve düz"
   - Cümle 10: «Keloğlan yakında büyük ve düz bir taş buldu.»
   - Açıklama: 'Yakında' burada 'birazdan' diye okunabiliyor, 'yakınlarda' ya da 'yanında' denmeliydi.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yavaş yavaş ve sabırlı bir şekilde sardı"
   - Cümle 11: «İpi yavaş yavaş ve sabırlı bir şekilde sardı.»
   - Açıklama: Tohumdaki özellik öğrenmeyi sevmek; sabır karttaki özelliklerde olmayan ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik öğrenmek; sabır ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0175` birebir aynı, `@degisim: kilitlemek -> sarmak` (tutuyorsan), ardından `@onarim: 9f966842c54c56cba199e4a8e73f2cd1a0695a71`, sonra gövde.

### Hikâye 8: tohum keloglan-0176 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0176
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'bluz', fiil 'akmak', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: derenin sesi yüzünden garip sesin yeri bulunamadı | dereden uzaklaşıp dinledi ve sesi yapan elmaları buldu
@tohum: keloglan-0176
@degisim: bluz -> elma
Rüzgar esiyordu ve dere şırıl şırıl akıyordu. Keloğlan ormanda yürürken tak tak diye garip bir ses duydu. Ama derenin sesi yüzünden sesin yerini bulamadı. Keloğlan önce sağa, sonra sola yürüdü. Ses bir kesildi, bir yeniden geldi. Dürüst Keloğlan yine de aramayı bırakmadı. Dereden biraz uzaklaştı ve dikkatle dinledi. Ses şimdi daha açık geliyordu. Sesin peşinden yürüdü ve büyük bir elma ağacı buldu. Rüzgar esince ağaçtan kıpkırmızı elmalar düşüyordu. Elmalar ağacın altındaki düz bir taşa çarpıp tak tak ses yapıyordu. Keloğlan güldü ve yerdeki elmaları topladı. Keloğlan bundan sonra merak ettiği bir sesi sonuna kadar aradı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dürüst Keloğlan yine de aramayı bırakmadı"
   - Cümle 6: «Dürüst Keloğlan yine de aramayı bırakmadı.»
   - Açıklama: Aramayı bırakmamak dürüstlük değil sabırdır; özellik kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Aramayı bırakmamak dürüstlükle ilgili değil; 'dürüst' kelimesi yanlış yerde kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Dürüst Keloğlan yine de aramayı bırakmadı"
   - Cümle 6: «Dürüst Keloğlan yine de aramayı bırakmadı.»
   - Açıklama: Tohumdaki özellik kartta 'Dürüsttür ve azimlidir' olarak geçiyor ama hikayede dürüstlük gösterilmeden azim 'dürüst' diye adlandırılıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sesin peşinden yürüdü"
   - Cümle 9: «Sesin peşinden yürüdü ve büyük bir elma ağacı buldu.»
   - Açıklama: Tek başına dere kenarındaki ormanda garip bir sesin peşinden gitmek taklit edilince tehlikeli olabilir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir sesi sonuna kadar aradı"
   - Cümle 13: «Keloğlan bundan sonra merak ettiği bir sesi sonuna kadar aradı.»
   - Açıklama: 'Sonuna kadar' soyut bir kalıp; ders cümlesi somut bir olaya dayanmıyor.
   - Açıklama: 'Sonuna kadar' soyut bir kalıp; küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0176` birebir aynı, `@degisim: bluz -> elma` (tutuyorsan), ardından `@onarim: db18128453ab4906d3806dde5e2ef0dd912a82f7`, sonra gövde.

### Hikâye 9: tohum keloglan-0177 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Bilgecan Dede
@tohum: keloglan-0177
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'meyve', fiil 'kırılmak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Bilgecan Dede
@plan: dedenin yaptığı aletin kolu meyveleri yere düşürüyordu | çubuğun kırık olduğunu söyledi ve yerine kaşık bağladı
@tohum: keloglan-0177
Keloğlan evde, Bilgecan Dede'nin yaptığı yeni bir tahta alete bakıyordu. Aletin hareketli bir kolu vardı ve kol meyveleri sepete atıyordu. Ama kol meyveleri sepete değil, yere düşürüyordu. "Aletim güzel mi, Keloğlan?" diye sordu Bilgecan Dede. Keloğlan kolu izledi ve dürüst bir cevap verdi. "Güzel, ama kolun çubuğu kırılmış," dedi Keloğlan. Bilgecan Dede eğilip baktı ve başını salladı. Keloğlan mutfaktan tahta bir kaşık getirdi. Kaşığı bir iple kırık çubuğun yerine bağladı. Kol yeniden döndü ve bir elmayı tam sepete attı. Bilgecan Dede sevinçle ellerini çırptı. Keloğlan da çok mutlu oldu, çünkü dedenin aleti artık çalışıyordu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kol meyveleri sepete atıyordu"
   - Cümle 2: «Aletin hareketli bir kolu vardı ve kol meyveleri sepete atıyordu.»
   - Açıklama: Kolun meyveleri sepete attığı söyleniyor, sonraki cümle bunun tersini söylüyor; 'atmalıydı' anlamı yanlış kelimeyle verilmiş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "vardı ve kol meyveleri sepete atıyordu"
   - Cümle 2: «Aletin hareketli bir kolu vardı ve kol meyveleri sepete atıyordu.»
   - Açıklama: Kol meyveleri sepete atmıyordu; 'atmalıydı' anlamı 'atıyordu' ile yanlış verilmiş ve sonraki cümleyle çelişiyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kol meyveleri sepete atıyordu"
   - Cümle 2: «Aletin hareketli bir kolu vardı ve kol meyveleri sepete atıyordu.»
   - Açıklama: Kol önce meyveleri sepete atıyor deniyor, hemen sonra sepete değil yere düşürdüğü söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0177` birebir aynı, ardından `@onarim: 99e5c80f56ffc1c8b0fe39306852725063eb80cc`, sonra gövde.

### Hikâye 10: tohum keloglan-0179 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0179
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'limon', fiil 'kopmak', sıfat 'benekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: dolu piknik sepetinin sapı koptu ve sepet taşınamadı | anasından yardım istedi ve mendille yeni bir sap yaptı
@tohum: keloglan-0179
Ormanda büyük ağaçların altı serin ve güzeldi. Keloğlan piknik sepetini taşıyarak anasıyla yürüyordu. Sepet doluydu ve sapı birden koptu. Sepetteki sarı limonlar yere yuvarlandı. Keloğlan limonları topladı ve sepeti kucağına aldı. Ama sapı olmayan sepeti taşımak çok zordu. Keloğlan dürüst davrandı. "Anne, bu sepeti tek başıma taşıyamıyorum, yardım eder misin?" diye sordu Keloğlan. Anası gülümsedi ve cebinden benekli bir mendil çıkardı. Keloğlan mendili sepete bağladı ve yeni bir sap yaptı. Sonra ikisi sepeti birlikte taşıdı. "Teşekkürler, anneciğim, şimdi sepet çok hafif!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sepetteki sarı limonlar yere yuvarlandı"
   - Cümle 4: «Sepetteki sarı limonlar yere yuvarlandı.»
   - Açıklama: Asıl sorundan önce limonların dökülmesi ikinci bir küçük sorun olarak açılıp hemen kapanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 7: «Keloğlan dürüst davrandı.»
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız etiket olarak söyleniyor; sorunun çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız etiket olarak söyleniyor, yardım istemek karttaki dürüstlüğü işe yarar biçimde göstermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0179` birebir aynı, ardından `@onarim: ed12af0ee7b31cd761eed842f91db7c99682f8a4`, sonra gövde.

### Hikâye 11: tohum keloglan-0180 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0180
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mürekkep', fiil 'kurtarmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: sağ eldiven karda aşağı kaydı ve kayboldu | öbür eldiveni de bırakıp peşinden gitti ve ikisini buldu
@tohum: keloglan-0180
@degisim: mürekkep -> eldiven
Keloğlan karlı tepede kardan bir kule yapıyordu. Kuleye küçük pencereler açmak için sağ eldivenini çıkardı. Ama sakar Keloğlan eldiveni düşürdü ve eldiven karda aşağı kaydı. Kulenin yanında Keloğlan'ın bir sürü karışık ayak izi vardı. Keloğlan izlerin arasında eğilip baktı, ama eldiveni bulamadı. Sonra sol eldivenini çıkardı ve onu da aynı yerden kaydırdı. Keloğlan onun nereye gittiğine dikkatle baktı ve peşinden yavaşça yürüdü. Sol eldiven bir kar yığınının dibinde durdu. Sağ eldiven de tam orada, karın içindeydi. Keloğlan iki eldiveni de kardan kurtardı. Eldivenleri salladı ve ellerine taktı. Sonra kulenin yanına döndü ve kuleyi mutlu mutlu bitirdi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kulenin yanında Keloğlan'ın bir sürü karışık ayak izi vardı"
   - Cümle 4: «Kulenin yanında Keloğlan'ın bir sürü karışık ayak izi vardı.»
   - Açıklama: Eldiven aşağı kaymışken ayak izleri arasında aranması olaydan çıkmıyor ve izler hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0180` birebir aynı, `@degisim: mürekkep -> eldiven` (tutuyorsan), ardından `@onarim: 90d25f413d9fc889b72311e5ad53a7240b9273bb`, sonra gövde.

### Hikâye 12: tohum keloglan-0181 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | eşeği
@tohum: keloglan-0181
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'heykel', fiil 'dinmek', sıfat 'gizli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | şato | eşeği
@plan: eşek peşinden geliyordu ve sürprizi görecekti | doğruyu söyledi ve eşekten beklemesini istedi
@tohum: keloglan-0181
Bir sabah yağmur dindi ve şatonun bahçesinde güneş çıktı. Keloğlan, Karakaçan için gizli bir sürpriz hazırlıyordu. Ama Karakaçan hep peşinden geliyordu ve sürprizi görecekti. Keloğlan ona yalan söylemedi, dürüst davrandı. "Karakaçan, sana bir sürpriz yapıyorum, kapının yanında bekle," dedi Keloğlan. Karakaçan başını salladı ve kapının yanında bekledi. Keloğlan bir sepet havucu taş heykelin arkasına koydu. Sonra ıslık çaldı ve Karakaçan koşarak geldi. "Sürpriz, Karakaçan, bunlar senin!" dedi Keloğlan. Karakaçan havuçları görünce sevinçle başını salladı. Karakaçan havuçları mutlu mutlu yedi. Keloğlan da ona bakıp güldü.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir sabah yağmur dindi"
   - Cümle 1: «Bir sabah yağmur dindi ve şatonun bahçesinde güneş çıktı.»
   - Açıklama: Yağmurun dinmesi bir olay olarak kuruluyor ama hikayede hiçbir işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ona yalan söylemedi, dürüst davrandı"
   - Cümle 4: «Keloğlan ona yalan söylemedi, dürüst davrandı.»
   - Açıklama: 'Dürüst davranmak' olaydan çıkan somut bir ders değil, soyut bir yorum.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Karakaçan havuçları mutlu mutlu yedi"
   - Cümle 11: «Karakaçan havuçları mutlu mutlu yedi.»
   - Açıklama: Bir önceki cümle de 'Karakaçan havuçları' ile başlıyor ve 'başını salladı' daha önce de geçti; gereksiz tekrar var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0181` birebir aynı, ardından `@onarim: 5f06716f7254051c009c3bb18fd036808069abd8`, sonra gövde.
