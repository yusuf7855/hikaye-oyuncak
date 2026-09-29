# Editör görevi (onarım): Keloğlan, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0064 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0064
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'önlük', fiil 'çözülmek', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepede tık tık diye bir ses geldi | sesi dinleyerek kayanın üstündeki buzu buldu
@tohum: keloglan-0064
@degisim: önlük -> buz
Hava soğuktu ama güneş parlıyordu. Keloğlan tepede yürürken küçük bir ses duydu. Ses tık tık diye geliyordu ama ortada hiçbir şey yoktu. Keloğlan bu sesi çok merak etti. Önce bir taşın düştüğünü sandı ama hiç taş görmedi. Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı. Sesi dinleyerek bir kayanın yanına gitti. Kayanın üstünde küçük, ışıltılı bir buz vardı. Buz güneşte yavaş yavaş çözülüp su oluyordu. Taşa düşen damlalar tık tık ses çıkarıyordu. Keloğlan çok sevindi, çünkü sesin nereden geldiğini sonunda bulmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı.»
   - Açıklama: Görmediği şeye inanmamak dürüstlük değildir; 'dürüst' kelimesi yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı.»
   - Açıklama: 'Dürüst' kelimesi görmediğine inanmamak anlamında yanlış kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "görmediği bir şeye inanmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı.»
   - Açıklama: Görmediğine inanmamak soyut bir düşünce, 3 yaşındaki çocuğa uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı.»
   - Açıklama: Tohumdaki dürüstlük özelliği karttaki anlamıyla değil, kuşkuculuk olarak kullanılmış ve çözüme katkısı yok.
   - Açıklama: Kartın dürüstlük özelliği görmediğine inanmamak anlamında yanlış kullanılmış ve çözüme katkısı yok.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "görmediği bir şeye inanmadı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu, görmediği bir şeye inanmadı.»
   - Açıklama: Dürüstlük cümlesi olaydan çıkmıyor ve sesin bulunmasında hiçbir işlev görmüyor.
   - Açıklama: Dürüstlük cümlesi olaya bağlanmıyor ve sesi aramayı mantıklı biçimde sebeplendirmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0064` birebir aynı, `@degisim: önlük -> buz` (tutuyorsan), ardından `@onarim: bcfad3b1eba92f6e4b60b2f37c29c364c9c2d7e4`, sonra gövde.

### Hikâye 2: tohum keloglan-0065 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0065
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tuğla', fiil 'çekinmek', sıfat 'temkinli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kırmızı elmalar yüksek bir dalda duruyordu | önce çekindi sonra anasından yardım istedi
@tohum: keloglan-0065
@degisim: tuğla -> elma
Ormanda kuşlar ötüyordu. Keloğlan ile anası büyük bir ağacın altında elma topluyordu. Ama en kırmızı elmalar yüksek bir dalda duruyordu ve Keloğlan onlara yetişemedi. Keloğlan önce yardım istemeye çekindi. Sonra anasına döndü. "Anneciğim, elim dala yetişmiyor, yardım eder misin?" dedi dürüst Keloğlan. "Tabii ki," dedi anası. Anası dalı kırmadan, temkinli bir şekilde aşağı eğdi. Keloğlan kırmızı elmaları tek tek sepete koydu. Sepet kısa sürede doldu. Sonra ikisi ağacın gölgesinde oturdu ve elmaları mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan önce yardım istemeye çekindi"
   - Cümle 4: «Keloğlan önce yardım istemeye çekindi.»
   - Açıklama: 'Çekinmek' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan önce yardım istemeye çekindi"
   - Cümle 4: «Keloğlan önce yardım istemeye çekindi.»
   - Açıklama: Kartın özellikler alanında olmayan çekingenlik ikinci bir özellik olarak ekleniyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi dürüst Keloğlan"
   - Cümle 6: «"Anneciğim, elim dala yetişmiyor, yardım eder misin?" dedi dürüst Keloğlan.»
   - Açıklama: Tohum özelliği dürüstlük yalnız etiket olarak geçiyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Dürüstlük yalnız sıfat olarak yapıştırılmış, sorunu çözen bir davranış olarak kullanılmıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "temkinli bir şekilde aşağı eğdi"
   - Cümle 8: «Anası dalı kırmadan, temkinli bir şekilde aşağı eğdi.»
   - Açıklama: 'Temkinli bir şekilde' 3 yaşındaki çocuğun bilmeyeceği soyut bir ifade.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "temkinli bir şekilde aşağı"
   - Cümle 8: «Anası dalı kırmadan, temkinli bir şekilde aşağı eğdi.»
   - Açıklama: 'Temkinli bir şekilde' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0065` birebir aynı, `@degisim: tuğla -> elma` (tutuyorsan), ardından `@onarim: 91720625565cd1030578a5800c205333512cde0f`, sonra gövde.

### Hikâye 3: tohum keloglan-0067 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0067
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kart', fiil 'buluşmak', sıfat 'beyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: kağıt uçurtma hemen düştü çünkü kanatları aynı boyda değildi | kartı yeniden katlayıp iki kanadı aynı boyda yaptı
@tohum: keloglan-0067
Keloğlan tepede beyaz bir kartı katlayıp ilk kez kağıt uçurtma yaptı. Uçurtmayı havaya attı ama uçurtma hemen yere düştü. Uçurtmanın bir kanadı büyük, öbür kanadı küçüktü. Keloğlan uçurtmayı açtı ve kartı dikkatle inceledi. Böylece iki kanadın aynı boyda olması gerektiğini öğrendi. Kartı bir daha katladı ve bu kez iki ucu tam ortada buluştu. Keloğlan uçurtmayı rüzgara doğru hafifçe fırlattı. Beyaz uçurtma tepenin üstünde uzun uzun süzüldü. Sonra yumuşak otların üstüne yavaşça kondu. Keloğlan kağıt uçurtmasını aldı ve tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Uçurtmanın bir kanadı büyük"
   - Cümle 3: «Uçurtmanın bir kanadı büyük, öbür kanadı küçüktü.»
   - Açıklama: Kanatlı, süzülüp konan katlanmış kağıt uçurtma değil kağıt uçaktır; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0067` birebir aynı, ardından `@onarim: de1be3a50c2c3aacff64205652fc304d0c8a87c8`, sonra gövde.

### Hikâye 4: tohum keloglan-0071 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0071
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'papatya', fiil 'sürtmek', sıfat 'neşeli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: taç çok büyüktü ve dedenin burnuna kaydı | birkaç papatyayı çıkarıp tacı yeniden bağladı
@tohum: keloglan-0071
Tepede Keloğlan ile Bilgecan Dede papatyalardan bir taç yapıyordu. Keloğlan tacı bitirdi ve Bilgecan Dede'nin başına koydu. Ama taç çok büyüktü ve dedenin burnuna kaydı. Beyaz papatyalar burnuna sürtündü ve dedeyi gıdıkladı. İkisi de kahkaha attı. "Dede, bu tacı nasıl küçük yaparım?" diye sordu Keloğlan. "Birkaç papatyayı çıkar ve yeniden bağla," dedi Bilgecan Dede. Keloğlan yeni şeyler öğrenmeyi severdi ve dedeyi dikkatle dinledi. Üç papatyayı çıkardı ve sapları sıkıca bağladı. Bu kez taç dedenin başından hiç kaymadı. Bilgecan Dede neşeli bir yüzle tacına dokundu. "Bu taç çok güzel oldu, Keloğlan, teşekkür ederim!" dedi Bilgecan Dede.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İkisi de kahkaha attı"
   - Cümle 5: «İkisi de kahkaha attı.»
   - Açıklama: 'Kahkaha atmak' kalıplaşmış bir deyim ve küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0071` birebir aynı, ardından `@onarim: e64245d0d3a9d7116ce18d29b07fca14d7086a8d`, sonra gövde.

### Hikâye 5: tohum keloglan-0072 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0072
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'satranç', fiil 'sevmek', sıfat 'büyülü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kutudaki beyaz taşlardan biri kırılmıştı | ağacın köklerine bakıp beyaz yuvarlak bir taş buldu
@tohum: keloglan-0072
@degisim: büyülü -> yuvarlak
Rüzgar ağaçların arasında hafifçe esiyordu. Keloğlan ormanda elinde satranç kutusuyla yürüyordu. Kutudaki beyaz taşlardan biri kırılmıştı ve yeni bir taş lazımdı. Keloğlan satranç oynamayı çok severdi. Ağaçların dibine baktı ama yalnız koyu taşlar gördü. Sonra büyük bir ağacın köklerini tek tek aradı. Kökün yanında küçük, beyaz ve yuvarlak bir taş fark etti. Taş, öbür beyaz taşlar kadar küçüktü. Keloğlan taşı silip kutuya koydu. Keloğlan biraz sakardı ve yeni taşı öbürleriyle karıştırdı. Yeni taşı hiç ayıramadı, çünkü hepsi aynı görünüyordu. Keloğlan çok sevindi, çünkü artık yine satranç oynayabilecekti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan biraz sakardı ve"
   - Cümle 10: «Keloğlan biraz sakardı ve yeni taşı öbürleriyle karıştırdı.»
   - Açıklama: 'Sakar' beceriksiz demektir; taşları karıştırıp ayıramamak sakarlık değil, kelime yanlış anlamda.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni taşı öbürleriyle karıştırdı"
   - Cümle 10: «Keloğlan biraz sakardı ve yeni taşı öbürleriyle karıştırdı.»
   - Açıklama: Sakarlık kartın güvenli kullanım satırındaki gibi karıştırma olarak geçiyor ama sorunun çözümüne bir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni taşı öbürleriyle karıştırdı"
   - Cümle 10: «Keloğlan biraz sakardı ve yeni taşı öbürleriyle karıştırdı.»
   - Açıklama: Taşların karışması hiçbir sonuca bağlanmayan işlevsiz bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve yeni taşı öbürleriyle karıştırdı"
   - Cümle 10: «Keloğlan biraz sakardı ve yeni taşı öbürleriyle karıştırdı.»
   - Açıklama: Sakarlık ve taşları karıştırma olayı çözümden sonra sebepsizce ekleniyor ve hikayeye bir şey katmıyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "hepsi aynı görünüyordu"
   - Cümle 11: «Yeni taşı hiç ayıramadı, çünkü hepsi aynı görünüyordu.»
   - Açıklama: Ormanda bulunan yuvarlak bir taşın biçimli satranç taşlarıyla tıpatıp aynı görünmesi akla aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0072` birebir aynı, `@degisim: büyülü -> yuvarlak` (tutuyorsan), ardından `@onarim: 492243d0d785aff75ce56e7b1af69a3b714bce24`, sonra gövde.

### Hikâye 6: tohum keloglan-0073 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0073
- yer: dağ (Köyün yakınındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'flüt', fiil 'uyanmak', sıfat 'siyah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: rüzgar yumağı yokuştan aşağı çalıya yuvarladı | flütüyle yumağı dışarı itip anasına getirdi
@tohum: keloglan-0073
@degisim: uyanmak -> yuvarlanmak
Tepede kuşlar ötüyordu. Keloğlan flüt çalıyordu, anası da yanında siyah bir atkı örüyordu. Birden rüzgar esti ve anasının yumağı yokuştan aşağı yuvarlandı. Yumak dikenli bir çalının altında durdu. "Anneciğim, ben getiririm!" dedi Keloğlan. Çalıya kadar dikkatle yürüdü. Elini dikenlere sokmadı, uzun flütüyle yumağı dışarı itti. Yumağı alıp anasının yanına döndü. Keloğlan biraz sakardı ve yumağı uzatırken düşürdü. Yumak tam anasının kucağına kondu. "Teşekkür ederim, Keloğlan," dedi anası ve gülümsedi. Sonra anası atkısını örmeye, Keloğlan da flüt çalmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve yumağı uzatırken düşürdü"
   - Cümle 9: «Keloğlan biraz sakardı ve yumağı uzatırken düşürdü.»
   - Açıklama: Sorun çözüldükten sonra işlevsiz bir düşürme olayı ekleniyor.
   - Açıklama: Düşürme olayı hiçbir sonuca bağlanmayan işlevsiz bir ayrıntı; yumak sebepsizce kucağa konuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tam anasının kucağına kondu"
   - Cümle 10: «Yumak tam anasının kucağına kondu.»
   - Açıklama: 'Konmak' kuş gibi canlılar için kullanılır; yumak için 'düştü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0073` birebir aynı, `@degisim: uyanmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: e558caff97bb382db8012961c1254fa45bb52668`, sonra gövde.

### Hikâye 7: tohum keloglan-0075 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0075
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'hediye', fiil 'ıslanmak', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: duvarda simsiyah bir gölge sallanıyordu | pencereye baktı ve gölgeyi yapan ceketi buldu
@tohum: keloglan-0075
@degisim: hediye -> gölge
Köy evinin içi serin ve sessizdi. Keloğlan yağmurda ıslanan ceketini kapının yanına astı. Birden duvarda simsiyah, büyük bir gölge sallanmaya başladı. Keloğlan bu gölgeyi çok merak etti. Onun ne olduğunu öğrenmek istedi. Önce duvara yaklaştı ama duvarda başka bir şey göremedi. Sonra arkasına döndü ve pencereye baktı. Pencereden gelen ışık kapının yanındaki ceketin üstüne düşüyordu. Kapının altından hafif bir rüzgar geliyordu ve ceket sallanıyordu. Duvardaki şey, ıslak ceketin gölgesiydi. Keloğlan ceketi iki eliyle tuttu ve gölge hemen durdu. Keloğlan bundan sonra duvarda bir gölge görünce önce ışığa baktı.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "simsiyah, büyük bir gölge sallanmaya"
   - Cümle 3: «Birden duvarda simsiyah, büyük bir gölge sallanmaya başladı.»
   - Açıklama: Duvarda sallanan simsiyah büyük gölge küçük çocuklar için korkutucu olabilir.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "duvarda simsiyah, büyük bir gölge sallanmaya başladı"
   - Cümle 3: «Birden duvarda simsiyah, büyük bir gölge sallanmaya başladı.»
   - Açıklama: Evde duvarda sallanan simsiyah büyük gölge 3-6 yaş için korkutucu bir öğe.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Duvardaki şey, ıslak ceketin"
   - Cümle 10: «Duvardaki şey, ıslak ceketin gölgesiydi.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0075` birebir aynı, `@degisim: hediye -> gölge` (tutuyorsan), ardından `@onarim: 1bdc3eff0671996730ebc5a1fa53e53f58aca5f2`, sonra gövde.

### Hikâye 8: tohum keloglan-0076 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0076
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'blok', fiil 'giymek', sıfat 'üzgün'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: tahta bloklardan yapılan kule her seferinde devrildi | büyük blokları alta koyup kuleyi sağlam yaptı
@tohum: keloglan-0076
Bir sabah Keloğlan annesine bir sürpriz yapmak istedi. Anası mutfaktayken tahta bloklardan ona bir kule yapmaya başladı. Ama kule her seferinde devrildi, çünkü en altta küçük bloklar vardı. Keloğlan yere oturdu ve üzgün bir yüzle bloklara baktı. Sonra büyük blokları alta, küçükleri üste koydu. Bu kez kule hiç devrilmedi. Keloğlan böylece büyük blokların altta sağlam durduğunu öğrendi. Sonra temiz gömleğini giydi ve annesini çağırdı. "Anneciğim, gel, sana bir sürprizim var!" dedi Keloğlan. Anası kuleyi gördü ve güldü. "Ne güzel bir kule, teşekkür ederim!" dedi anası. Sonra ikisi bloklarla birlikte mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra temiz gömleğini giydi"
   - Cümle 8: «Sonra temiz gömleğini giydi ve annesini çağırdı.»
   - Açıklama: Gömlek giyme sebepsiz ve işlevsiz bir ayrıntı.
   - Açıklama: Temiz gömlek sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0076` birebir aynı, ardından `@onarim: 9e60d391daa2983b4ebeecaf98810db959c880ff`, sonra gövde.

### Hikâye 9: tohum keloglan-0078 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0078
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tomurcuk', fiil 'sürmek', sıfat 'berrak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: arkadaşının karnı acıkmıştı ama ekmeği yoktu | ekmeğini ikiye böldü ve onunla paylaştı
@tohum: keloglan-0078
@degisim: tomurcuk -> kavanoz
Bir sabah Keloğlan ile Balkız tepede oturuyordu. Gökyüzü berrak ve maviydi. Balkız'ın karnı acıkmıştı ama çantasında ekmek yoktu. Çantasında yalnız küçük bir kavanoz bal vardı. Keloğlan'ın çantasında ise bir ekmek vardı. "Balkız, bu ekmeği seninle paylaşalım mı?" diye sordu Keloğlan. "Olur, ben de balımı seninle paylaşırım," dedi Balkız. Keloğlan ekmeği iki eşit parçaya böldü. Balkız kavanozu açtı ve kaşıkla kendi parçasına biraz bal sürdü. Keloğlan da onu izledi ve ekmeğe bal sürmeyi öğrendi. İkisi ekmeklerini yan yana oturup yedi. "Teşekkürler, Balkız, bu çok tatlı bir kahvaltı oldu!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Gökyüzü berrak ve maviydi"
   - Cümle 2: «Gökyüzü berrak ve maviydi.»
   - Açıklama: 'Berrak' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ekmeğe bal sürmeyi öğrendi"
   - Cümle 10: «Keloğlan da onu izledi ve ekmeğe bal sürmeyi öğrendi.»
   - Açıklama: Keloğlan'ın bal sürmeyi öğrenmesi sorundan çıkmayan, işlevsiz ve sebepsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0078` birebir aynı, `@degisim: tomurcuk -> kavanoz` (tutuyorsan), ardından `@onarim: ae88cc32b7d55ee458f9d3b4abdcefaafce239f0`, sonra gövde.

### Hikâye 10: tohum keloglan-0079 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0079
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'eşarp', fiil 'beğenmek', sıfat 'kocaman'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: rüzgar annesinin eşarbını yere düşürdü | aramayı bırakmadı ve eşarbı sepette buldu
@tohum: keloglan-0079
Köy evinin içi sıcak ve aydınlıktı. Keloğlan'ın anası kocaman kırmızı eşarbını arıyordu. Rüzgar eşarbı pencerenin önünden bir yere düşürmüştü. Anası bu eşarbı çok beğeniyordu ve biraz üzüldü. "Anneciğim, ben sana yardım ederim," dedi Keloğlan. Önce masanın altına baktı ama eşarp orada yoktu. Sonra kapının arkasına baktı, orada da yoktu. "Bırak, belki bir daha buluruz," dedi anası. "Anneciğim, dürüst söylüyorum, eşarbı bulana kadar ararım," dedi Keloğlan. Sonra pencerenin altındaki sepete baktı. Kırmızı eşarp sepetin içindeydi! Keloğlan eşarbı çıkarıp annesine verdi. Anası eşarbını boynuna sardı ve Keloğlan'a sarıldı. Keloğlan çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (5):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce masanın altına baktı ama eşarp orada yoktu"
   - Cümle 6: «Önce masanın altına baktı ama eşarp orada yoktu.»
   - Açıklama: Eşarp pencereden düştüğü halde Keloğlan önce masa ve kapı arkasına bakıyor; çözüm sebebe doğrudan yönelmiyor ve ikiden fazla adım sürüyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "belki bir daha buluruz"
   - Cümle 8: «"Bırak, belki bir daha buluruz," dedi anası.»
   - Açıklama: 'Bir daha' yanlış anlamda; 'sonra buluruz' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst söylüyorum, eşarbı bulana"
   - Cümle 9: «"Anneciğim, dürüst söylüyorum, eşarbı bulana kadar ararım," dedi Keloğlan.»
   - Açıklama: 'Dürüst' kelimesi yersiz ve yanlış bağlamda kullanılmış.
   - Açıklama: 'Dürüst söylüyorum' bağlama uymuyor; kararlılık bildiren cümlede yanlış kullanılmış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Anneciğim, dürüst söylüyorum, eşarbı"
   - Cümle 9: «"Anneciğim, dürüst söylüyorum, eşarbı bulana kadar ararım," dedi Keloğlan.»
   - Açıklama: 'Dürüst söylüyorum' kararlılığı anlatmak için yanlış kullanılmış.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dürüst söylüyorum, eşarbı bulana kadar ararım"
   - Cümle 9: «"Anneciğim, dürüst söylüyorum, eşarbı bulana kadar ararım," dedi Keloğlan.»
   - Açıklama: Özellikler alanındaki dürüstlük gerçek bir dürüst davranış olarak kullanılmıyor; kelime yalnız söz süsü olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0079` birebir aynı, ardından `@onarim: 4ae446d195914586c571817ec01b2635a9752858`, sonra gövde.

### Hikâye 11: tohum keloglan-0081 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0081
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'defter', fiil 'gezinmek', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: ağacın gövdesinde yapışkan sarı damlalar vardı | yakından baktı ve damlaları ağacın yaptığını buldu
@tohum: keloglan-0081
Tepede hava serin ve güzeldi. Keloğlan elinde defteriyle çimenlerin arasında geziniyordu. Birden bir çam ağacının gövdesinde parlak sarı damlalar gördü. Damlalar bal gibi parlıyordu. Keloğlan bu damlaları çok merak etti. Parmağıyla yavaşça dokundu. Damla çok yapışkandı ve çam gibi kokuyordu. Sonra ağaca daha yakından baktı. Damlalar ağaçtaki küçük bir delikten yavaş yavaş akıyordu. Keloğlan böylece bu damlaları ağacın kendisinin yaptığını öğrendi. Defterine çam ağacını ve sarı damlaları çizdi. Keloğlan çok sevindi, çünkü damlaların nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağacın gövdesinde yapışkan sarı damlalar vardı"
   - Cümle 0 (plan satırı): «ağacın gövdesinde yapışkan sarı damlalar vardı | yakından baktı ve damlaları ağacın yaptığını buldu»
   - Açıklama: Damlalar yalnız bir gözlem; ortada çocuğun önemseyeceği gerçek bir sorun yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Parmağıyla yavaşça dokundu"
   - Cümle 6: «Parmağıyla yavaşça dokundu.»
   - Açıklama: Bal gibi parlayan bilinmeyen yapışkan damlaya parmakla dokunmak çocuğun taklit edebileceği bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0081` birebir aynı, ardından `@onarim: 5933228b70f701621af52dd9b77cf7f053afd84e`, sonra gövde.

### Hikâye 12: tohum keloglan-0082 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0082
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sofra', fiil 'yatırmak', sıfat 'pahalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: su şişesini yatırdı ve kitap ıslandı | özür diledi ve kitabı güneşte kuruttu
@tohum: keloglan-0082
@degisim: pahalı -> ıslak
Bir sabah Keloğlan ile Bilgecan Dede ormanda bir sofra kurdu. Dede kitabını da sofraya koymuştu. Keloğlan acele etti ve kapağı açık su şişesini sofraya yatırdı. Su hemen aktı ve kitabın sayfaları ıslandı. "Özür dilerim, Dede, kitabını ıslattım," dedi Keloğlan. "Üzülme, gel, ıslak sayfaları birlikte kurutalım," dedi Bilgecan Dede. Keloğlan kitabı açtı ve güneşli bir taşın üstüne koydu. Rüzgar sayfaları yavaşça çevirdi. Biraz sonra sayfalar kurudu. Keloğlan böylece güneşin ıslak kağıdı kuruttuğunu öğrendi. Sonra şişenin kapağını kapadı ve şişeyi sofraya dik koydu. "Aferin, Keloğlan, kitabım yine kuru!" dedi Bilgecan Dede.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "su şişesini sofraya yatırdı"
   - Cümle 3: «Keloğlan acele etti ve kapağı açık su şişesini sofraya yatırdı.»
   - Açıklama: Kazayla dökülen şişe için 'yatırdı' değil 'devirdi' uygun fiildir.
   - Açıklama: 'Yatırmak' isteyerek yere koymak demektir; kazayla olan olay için 'devirdi' olmalı.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "ıslak sayfaları birlikte kurutalım"
   - Cümle 6: «"Üzülme, gel, ıslak sayfaları birlikte kurutalım," dedi Bilgecan Dede.»
   - Açıklama: Kitabı kurutma çözümünü Keloğlan değil Bilgecan Dede öneriyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "gel, ıslak sayfaları birlikte kurutalım"
   - Cümle 6: «"Üzülme, gel, ıslak sayfaları birlikte kurutalım," dedi Bilgecan Dede.»
   - Açıklama: Kurutma çözümünü Keloğlan değil Bilgecan Dede öneriyor.
   - Açıklama: Çözüm fikrini Keloğlan değil Bilgecan Dede buluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0082` birebir aynı, `@degisim: pahalı -> ıslak` (tutuyorsan), ardından `@onarim: 0c5ca3868f853d3f73f0f321e85dd1cfbb8936ad`, sonra gövde.
