# Editör görevi (onarım): Keloğlan, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0079 (deneme 3 -> 4)

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
@plan: rüzgar annesinin eşarbını pencerenin önünden düşürdü | aramayı bırakmadı ve eşarbı sepette buldu
@tohum: keloglan-0079
Köy evinin içi sıcak ve aydınlıktı. Keloğlan'ın anası kocaman kırmızı eşarbını arıyordu. Rüzgar eşarbı pencerenin önünden bir yere düşürmüştü. Anası bu eşarbı çok beğeniyordu ve biraz üzüldü. "Anneciğim, ben sana yardım ederim," dedi Keloğlan. Önce pencerenin önünde yere baktı ama eşarp orada yoktu. "Bırak, sonra buluruz," dedi anası. Ama Keloğlan aramayı bırakmadı. Sonra pencerenin altındaki sepete baktı. Kırmızı eşarp sepetin içindeydi! Keloğlan dürüst bir çocuktu. "Sepeti buraya ben koydum, eşarp içine düşmüş," dedi Keloğlan. Keloğlan eşarbı çıkarıp annesine verdi. Anası eşarbını boynuna sardı ve Keloğlan'a sarıldı. Keloğlan çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepeti buraya ben koydum"
   - Cümle 12: «"Sepeti buraya ben koydum, eşarp içine düşmüş," dedi Keloğlan.»
   - Açıklama: Keloğlan'ın dürüstlük itirafı olaydan çıkmıyor; kimse suçlu değilken sebepsiz ve işlevsiz bir ayrıntı olarak ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepeti buraya ben koydum, eşarp içine düşmüş"
   - Cümle 12: «"Sepeti buraya ben koydum, eşarp içine düşmüş," dedi Keloğlan.»
   - Açıklama: Dürüstlük itirafı olaydan çıkmıyor ve işlevsiz; suç yokken itiraf ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0079` birebir aynı, ardından `@onarim: 71be0e6f749498e53899b4c047db11b533a188dc`, sonra gövde.

### Hikâye 2: tohum keloglan-0081 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: çizdiği resmin üstüne yapışkan sarı damlalar düştü | dala bakıp damlaları buldu ve uzağa oturdu
@tohum: keloglan-0081
Tepede serin bir rüzgar esiyordu. Keloğlan defteriyle gezindi ve büyük bir çam ağacının altında çiçek çizdi. Ama birden resmin üstüne yapışkan, sarı bir damla düştü. Biraz sonra bir damla daha düştü. Keloğlan bu damlaları çok merak etti. Başını kaldırdı ve dallara dikkatle baktı. Dalda küçük bir delikten sarı damlalar yavaş yavaş akıyordu. Keloğlan böylece çam ağacının bu damlaları yaptığını öğrendi. Hemen defterini aldı ve ağaçtan uzak bir taşa oturdu. Orada çiçek resmine yeni renkler ekledi. Keloğlan çok sevindi, çünkü damlaları yapan ağacı bulmuştu.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "damlaları yapan ağacı bulmuştu"
   - Cümle 11: «Keloğlan çok sevindi, çünkü damlaları yapan ağacı bulmuştu.»
   - Açıklama: Ağacın damlaları yaptığı 8. cümlede zaten söylenmişti; son cümle aynı bilgiyi gereksiz tekrarlıyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "damlaları yapan ağacı bulmuştu"
   - Cümle 11: «Keloğlan çok sevindi, çünkü damlaları yapan ağacı bulmuştu.»
   - Açıklama: Hedef çiçek resmini kurtarmakken son cümle ağacı bulmayı kutluyor ve resimdeki yapışkan damlalara hiç dönülmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0081` birebir aynı, ardından `@onarim: 5d573986e3d130efcf7493d70d5d6eba106c3f3a`, sonra gövde.

### Hikâye 3: tohum keloglan-0082 (deneme 3 -> 4)

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
Bir sabah Keloğlan ile Bilgecan Dede ormanda bir sofra kurdu. Dede kitabını da sofraya koymuştu. Keloğlan acele etti ve kapağı açık şişeyi sofraya yatırdı. Su hemen aktı ve kitabın sayfaları ıslandı. "Özür dilerim, Dede, kitabın ıslandı," dedi Keloğlan. "Üzülme, Keloğlan," dedi Bilgecan Dede. Keloğlan kitabı açtı ve güneşli bir taşın üstüne koydu. Rüzgar sayfaları yavaşça çevirdi. Biraz sonra ıslak sayfalar kurudu. Keloğlan böylece açık şişenin suyu döktüğünü öğrendi. Sonra şişenin kapağını kapadı ve şişeyi sofraya dik koydu. "Aferin, Keloğlan, kitabım yine kuru!" dedi Bilgecan Dede.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kapağı açık şişeyi sofraya yatırdı"
   - Cümle 3: «Keloğlan acele etti ve kapağı açık şişeyi sofraya yatırdı.»
   - Açıklama: Kazayla düşürmek 'devirdi' ile anlatılır; 'yatırdı' bilerek yere koymak anlamına gelir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0082` birebir aynı, `@degisim: pahalı -> ıslak` (tutuyorsan), ardından `@onarim: 924f1e6b00a25898274dd0e5a1bb796c8f004846`, sonra gövde.

### Hikâye 4: tohum keloglan-0083 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0083
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çöp', fiil 'çıkmak', sıfat 'rahat'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: taç yapmak istedi ama çiçekler hep koptu | arkadaşından yardım istedi ve çiçekleri yavaşça bağladı
@tohum: keloglan-0083
@degisim: çöp -> papatya
Keloğlan ile Balkız tepeye çıktı. Tepede bir sürü beyaz papatya vardı. Keloğlan papatyalardan taç yapmak istedi, ama sert çekince çiçekler koptu. Sonra Balkız'dan yardım istedi. Balkız yanına geldi ve iki çiçeği yavaşça birbirine bağladı. Keloğlan dikkatle baktı ve bunu hemen öğrendi. Sonra papatyaları tek tek ekledi. Bu kez hiçbir çiçek kopmadı. Keloğlan'ın tacı çok güzel oldu. Keloğlan tacı Balkız'ın sarı saçlarına taktı. Balkız da ona hızlıca bir taç yaptı. Keloğlan ile Balkız çimenlere rahatça oturdu ve mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "iki çiçeği yavaşça birbirine bağladı"
   - Cümle 5: «Balkız yanına geldi ve iki çiçeği yavaşça birbirine bağladı.»
   - Açıklama: Çiçekleri bağlama yolunu Keloğlan değil Balkız bulup uyguluyor; Keloğlan yalnız ondan öğreniyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "baktı ve bunu hemen öğrendi"
   - Cümle 6: «Keloğlan dikkatle baktı ve bunu hemen öğrendi.»
   - Açıklama: 'Bunu' zamirinin neyi gösterdiği (çiçekleri bağlamayı) açıkça belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0083` birebir aynı, `@degisim: çöp -> papatya` (tutuyorsan), ardından `@onarim: 8fe563042c8527122607444751c909457c92a6e3`, sonra gövde.

### Hikâye 5: tohum keloglan-0085 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | eşeği
@tohum: keloglan-0085
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'fıskiye', fiil 'belirmek', sıfat 'pembe'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | eşeği
@plan: ikisi de acıkmıştı ama yalnız bir elma vardı | elmayı ikiye böldü ve yarısını eşeğe verdi
@tohum: keloglan-0085
@degisim: belirmek -> bölmek
Bir sabah Keloğlan ile eşeği Karakaçan şatonun bahçesine vardı. Yol çok uzundu ve ikisinin de karnı acıkmıştı. Ama Keloğlan'ın cebinde yalnız bir pembe elma vardı. Keloğlan elmayı fıskiyenin suyunda yıkadı. Elmayı elleriyle ikiye bölmek istedi. İki başparmağını elmanın ortasına bastırdı ve sıkıca çevirdi. Elma çıt diye ayrıldı. Keloğlan böylece elmayı elle bölmeyi öğrendi. Büyük parçayı Karakaçan'a uzattı, küçük parçayı kendisi aldı. Karakaçan elmasını yedi ve sevinçle anırdı. "Afiyet olsun, Karakaçan, bu elma ikimizin!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Keloğlan böylece elmayı elle bölmeyi öğrendi"
   - Cümle 8: «Keloğlan böylece elmayı elle bölmeyi öğrendi.»
   - Açıklama: Elmayı elle bölme bilgisi 5. cümleden sonra gereksizce tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0085` birebir aynı, `@degisim: belirmek -> bölmek` (tutuyorsan), ardından `@onarim: 7222b639dde509e9b4338f34cad401e08bf97233`, sonra gövde.

### Hikâye 6: tohum keloglan-0086 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0086
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'uçurtma', fiil 'sığmak', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: sürpriz uçurtma çantaya sığmadı | uçurtmayı kalın bir ağacın arkasına sakladı
@tohum: keloglan-0086
Rüzgar ormanın ağaçları arasında hafifçe esiyordu. Keloğlan, Balkız'ın doğum günü için değişik bir uçurtma yapmıştı. Uçurtmayı Balkız gelmeden saklamak istedi ama uçurtma çantasına sığmadı. Keloğlan etrafına baktı ve büyük bir ağaç gördü. Uçurtmayı ağacın arkasına dikkatlice koydu. Ağacın gövdesi çok kalındı ve uçurtma hiç görünmedi. Biraz sonra Balkız geldi ve Keloğlan'ın yanına oturdu. Balkız, Keloğlan'ın ağaca baktığını gördü ve ne olduğunu sordu. Keloğlan dürüst bir çocuktu ve uçurtmayı hemen ağacın arkasından çıkardı. Uçurtmayı Balkız'a verdi. Balkız uçurtmayı görünce ellerini çırptı. İkisi uçurtmayı birlikte uçurdu. Keloğlan çok sevindi, çünkü sürprizi Balkız'ı mutlu etmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve uçurtmayı hemen ağacın arkasından çıkardı"
   - Cümle 9: «Keloğlan dürüst bir çocuktu ve uçurtmayı hemen ağacın arkasından çıkardı.»
   - Açıklama: Saklama çözümü, Balkız'ın tek sorusuyla ve sebepsizce eklenen dürüstlük özelliğiyle hemen boşa çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 9: «Keloğlan dürüst bir çocuktu ve uçurtmayı hemen ağacın arkasından çıkardı.»
   - Açıklama: Saklama çözümü olaydan değil sebepsizce getirilen dürüstlük özelliğiyle hemen boşa çıkıyor; saklamanın işlevi kalmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0086` birebir aynı, ardından `@onarim: 76c5fd054e252fba3f3dd8c96c9aaf6602b27abe`, sonra gövde.

### Hikâye 7: tohum keloglan-0087 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0087
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'salata', fiil 'soğumak', sıfat 'dalgalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: ikisi aynı anda karıştırınca kaşıklar çarpıştı | salatayı sırayla karıştırmayı istedi
@tohum: keloglan-0087
@degisim: soğumak -> karıştırmak
Evde Keloğlan ile anası dalgalı desenli bir kasede salata yapıyordu. İkisi salatayı aynı anda karıştırınca kaşıklar çarpıştı. Keloğlan biraz sakardı ve bir marul yaprağını masaya düşürdü. Keloğlan yaprağı alıp kaseye geri koydu. "Anne, sırayla karıştıralım," dedi Keloğlan. "Olur, önce sen başla," dedi anası. Keloğlan salatayı beş kez yavaşça çevirdi. Sonra kaşığını bıraktı ve sırayı anasına verdi. Anası da beş kez çevirdi. Artık hiçbir yaprak düşmedi. "Sırayla yapınca salata çok güzel oldu, anneciğim, hadi yiyelim!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "İkisi salatayı aynı anda karıştırınca kaşıklar çarpıştı"
   - Cümle 2: «İkisi salatayı aynı anda karıştırınca kaşıklar çarpıştı.»
   - Açıklama: Kaşıkların çarpışması çocuğun önemseyeceği bir sorun olmayacak kadar önemsiz bir olay.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "aynı anda karıştırınca kaşıklar çarpıştı"
   - Cümle 2: «İkisi salatayı aynı anda karıştırınca kaşıklar çarpıştı.»
   - Açıklama: Kaşıkların çarpışması çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve bir marul yaprağını masaya düşürdü"
   - Cümle 3: «Keloğlan biraz sakardı ve bir marul yaprağını masaya düşürdü.»
   - Açıklama: Yaprağın düşmesi kaşıkların çarpışmasına değil sakarlığa bağlanıyor, ama çözüm yalnız çarpışmayı hedefliyor.
   - Açıklama: Yaprağın düşmesi çarpışmaya değil sakarlığa bağlanıyor, yine de sırayla karıştırmak bunu çözmüş gibi gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0087` birebir aynı, `@degisim: soğumak -> karıştırmak` (tutuyorsan), ardından `@onarim: 25d3c3ade9639d75644d07fd2470a7a4c8bdca5b`, sonra gövde.

### Hikâye 8: tohum keloglan-0089 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0089
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'marul', fiil 'toplamak', sıfat 'eskimiş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: dedenin eskimiş torbası yırtıldı ve marullar döküldü | marulları toplayıp kendi torbasını dedeyle paylaştı
@tohum: keloglan-0089
Şatonun büyük bahçesi serin ve sessizdi. Keloğlan torbası elinde yürürken Bilgecan Dede'yi gördü ve ona el salladı. Birden dedenin eskimiş torbası yırtıldı ve marullar çimenlere döküldü. Keloğlan hemen koştu ve marulları topladı. Ama biraz sakardı ve marullar kucağından yine düştü. Keloğlan onları yerden aldı ve torbasını açtı. "Gel, Dede, torbamı seninle paylaşayım," dedi Keloğlan. Keloğlan marulları kendi torbasına koydu. Sonra torbanın bir ucunu kendisi, öbür ucunu dede tuttu. Birlikte bahçenin kapısına kadar yürüdüler. "Teşekkür ederim, Keloğlan, bana çok yardım ettin," dedi Bilgecan Dede. Keloğlan çok sevindi, çünkü torbasını dedeyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "marullar kucağından yine düştü"
   - Cümle 5: «Ama biraz sakardı ve marullar kucağından yine düştü.»
   - Açıklama: Marullar toplanıp yeniden düşüyor ve çözüm ikiden fazla adıma uzuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "marullar kucağından yine düştü"
   - Cümle 5: «Ama biraz sakardı ve marullar kucağından yine düştü.»
   - Açıklama: Marulların yeniden düşmesi olaya bir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0089` birebir aynı, ardından `@onarim: 1a1423827ac42179aec228ca783553880c7ae50e`, sonra gövde.

### Hikâye 9: tohum keloglan-0090 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0090
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'çorap', fiil 'silkmek', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: rüzgar çorabı kırmızı yaprakların arasına düşürdü | yapraklara tek tek dokundu ve yumuşak çorabı buldu
@tohum: keloglan-0090
@degisim: çevik -> kırmızı
Bir sabah Keloğlan ile Balkız ormanda yürüyordu. Balkız bir kütüğe oturdu ve çorabını çıkardı, çünkü içine toprak girmişti. O sırada rüzgar esti ve kırmızı çorap yaprakların arasına düştü. Yapraklar da kırmızı olduğu için Balkız çorabı göremedi. "Üzülme, Balkız, ben bulurum," dedi Keloğlan. Ama biraz sakardı ve önce bir yaprağı çorap sandı. Keloğlan yaprağı hemen yere bıraktı. Sonra Keloğlan yapraklara tek tek dokundu. Kuru yapraklar sertti, ama yün çorap yumuşacıktı. Keloğlan çorabı silkti ve Balkız'a verdi. "Teşekkürler, Keloğlan," dedi Balkız ve çorabını giydi. Keloğlan bundan sonra göremediği şeyleri elleriyle dokunarak arardı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama biraz sakardı ve önce bir yaprağı çorap sandı"
   - Cümle 6: «Ama biraz sakardı ve önce bir yaprağı çorap sandı.»
   - Açıklama: Yaprağı çorap sanmak sakarlık değil karıştırmaktır; 'sakar' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Yaprağı çorap sanmak sakarlık değildir; kelime yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0090` birebir aynı, `@degisim: çevik -> kırmızı` (tutuyorsan), ardından `@onarim: b6443ff50cd4d6bfef51b5d870f2dfc04adf3830`, sonra gövde.

### Hikâye 10: tohum keloglan-0092 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0092
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bayrak', fiil 'yatmak', sıfat 'şeffaf'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: ıslak dal demeti çok ağırdı ve onu kaldıramadı | ıslık çalıp eşeğinden yardım istedi
@tohum: keloglan-0092
@degisim: bayrak -> dal
Yağmur yeni dinmişti ve yapraklarda cam gibi şeffaf damlalar vardı. Keloğlan ormanda büyük bir demet dal toplamıştı. Ama ıslak dallar çok ağırdı ve Keloğlan demeti kaldıramadı. Eşeği Karakaçan biraz uzakta, bir ağacın altında yatıyordu. Keloğlan ıslık çaldı. Eşek hemen kalktı ve yanına geldi. "Karakaçan, bu dalları taşımama yardım eder misin?" diye sordu Keloğlan. Eşek başını salladı. Keloğlan dalları tek tek eşeğin sırtına koydu. Karakaçan yükü kolayca taşıdı. Keloğlan böylece yeni bir şey öğrendi: ıslak dallar kuru dallardan ağırdı. Keloğlan ile Karakaçan dalları köye götürmek için yan yana, mutlu mutlu yürüdü.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "cam gibi şeffaf damlalar"
   - Cümle 1: «Yağmur yeni dinmişti ve yapraklarda cam gibi şeffaf damlalar vardı.»
   - Açıklama: Benzetme ve 'şeffaf' kelimesi 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Şeffaf' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan böylece yeni bir şey öğrendi"
   - Cümle 11: «Keloğlan böylece yeni bir şey öğrendi: ıslak dallar kuru dallardan ağırdı.»
   - Açıklama: Islak dalların ağır olduğu baştan biliniyor ve hiçbir karşılaştırma yapılmıyor; bu öğrenme olaydan çıkmıyor, sebepsizce ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0092` birebir aynı, `@degisim: bayrak -> dal` (tutuyorsan), ardından `@onarim: 6546ca39ced1e8b77c270307bc5ff94df2048284`, sonra gövde.

### Hikâye 11: tohum keloglan-0096 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0096
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'yüzük', fiil 'başlamak', sıfat 'yapraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: bol yüzük parmağından kaydı ve kayboldu | bir taşı bırakıp gittiği yere baktı ve yüzüğü buldu
@tohum: keloglan-0096
Evin önünde Keloğlan, eşeği Karakaçan'ın sırtına bir çuval yüklüyordu. Birden bol yüzüğü parmağından kaydı ve toprağa düştü. Keloğlan etrafa baktı ama yüzüğü göremedi. "Karakaçan, yüzüğüm nereye gitti?" diye sordu Keloğlan. Karakaçan kulaklarını oynattı. Keloğlan yeni bir şey denemeye başladı. Yerden yuvarlak bir taş aldı ve yavaşça bıraktı. Taş yuvarlandı ve yapraklı bir bitkinin arkasında durdu. Böylece Keloğlan yerin düz olmadığını öğrendi. Bitkinin arkasına baktı ve yüzüğünü orada buldu. "Bak, Karakaçan, yüzüğüm buradaymış!" dedi Keloğlan. Keloğlan bundan sonra iş yaparken yüzüğünü cebine koydu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bir taşı bırakıp gittiği yere"
   - Cümle 0 (plan satırı): «bol yüzük parmağından kaydı ve kayboldu | bir taşı bırakıp gittiği yere baktı ve yüzüğü buldu»
   - Açıklama: Yapı bozuk; gidenin taş olduğu anlaşılmıyor, 'taşın gittiği yere' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0096` birebir aynı, ardından `@onarim: af19217009ebfc3067c3d26cba006cc60ce777ac`, sonra gövde.

### Hikâye 12: tohum keloglan-0097 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0097
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çim', fiil 'karıştırmak', sıfat 'yeni'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: acele edip çiçekleri bakmadan attı ve karıştırdı | doğruyu söyleyip özür diledi ve çiçekleri yeniden ayırdı
@tohum: keloglan-0097
Bir sabah Keloğlan ile anası ormanda çiçek topluyordu. Anası yeni bir buket için çimlere iki küçük yığın yapmıştı. Bir yığın sarı, öbür yığın mor çiçekti. Keloğlan acele etti, çiçeklerini bakmadan attı ve iki yığını karıştırdı. Anası yığınlara baktı ve şaşırdı. "Bu çiçekler neden karışık?" diye sordu anası. "Ben yaptım, anneciğim, özür dilerim," dedi Keloğlan. Sonra çimlere oturdu ve çiçekleri tek tek ayırdı. Anası gülümsedi ve Keloğlan'ın başını okşadı. "Dürüst davrandın, Keloğlan, teşekkür ederim," dedi anası. Sonra ikisi güzel bir buket bağladı. Keloğlan ile anası çiçek toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Keloğlan acele etti, çiçeklerini bakmadan attı ve iki yığını karıştırdı.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor, ilk üç cümlede sorun yok.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Keloğlan acele etti, çiçeklerini bakmadan attı ve iki yığını karıştırdı"
   - Cümle 4: «Keloğlan acele etti, çiçeklerini bakmadan attı ve iki yığını karıştırdı.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0097` birebir aynı, ardından `@onarim: 9603004dacea54dcdd0a95c862636b63cbd2fcbf`, sonra gövde.
