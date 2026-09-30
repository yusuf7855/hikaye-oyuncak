# Editör görevi (onarım): Keloğlan, onarım partisi 44

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar44.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar44.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0075 (deneme 2 -> 3)

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
Köy evinin içi serin ve sessizdi. Keloğlan yağmurda ıslanan ceketini kapının yanına astı. Birden duvarda simsiyah, küçük bir gölge gördü. Gölge hafifçe sallanıyordu. Keloğlan bu gölgeyi çok merak etti. Onun ne olduğunu öğrenmek istedi. Önce duvara yaklaştı ama duvarda başka bir şey göremedi. Sonra arkasına döndü ve pencereye baktı. Pencereden gelen ışık kapının yanındaki ceketin üstüne düşüyordu. Kapının altından hafif bir rüzgar geliyordu ve ceket sallanıyordu. Gölgeyi yapan şey ıslak ceketti. Keloğlan ceketi iki eliyle tuttu ve gölge hemen durdu. Keloğlan bundan sonra duvarda bir gölge görünce önce ışığa baktı.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "duvarda simsiyah, küçük bir gölge gördü"
   - Cümle 3: «Birden duvarda simsiyah, küçük bir gölge gördü.»
   - Açıklama: Sessiz evde birden beliren simsiyah sallanan gölge küçük çocuğu korkutabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0075` birebir aynı, `@degisim: hediye -> gölge` (tutuyorsan), ardından `@onarim: 8d190bf6b4ce4e60704c9ca7f5eabc89fc303e09`, sonra gövde.

### Hikâye 2: tohum keloglan-0094 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0094
- yer: dağ (Köyün yakınındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kapı', fiil 'sarılmak', sıfat 'paslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: çok bulut vardı ve kapı şeklini bulamadı | dürüst davranıp arkadaşına hangisi olduğunu sordu
@tohum: keloglan-0094
@degisim: paslı -> beyaz
Tepede gökyüzü bir sürü beyaz bulutla doluydu. Keloğlan ile Balkız çimenlere uzandı ve bulutlara baktı. Balkız kapıya benzeyen bir bulut gördü, ama Keloğlan onu bulamadı. Keloğlan dürüst davrandı ve "Göremiyorum, Balkız, hangisi?" diye sordu. "Ağacın üstündeki uzun bulut," dedi Balkız. Keloğlan oraya baktı ve uzun bir bulut gördü. Bulutun iki yanı düz, üstü yuvarlaktı. "Evet, bu gerçekten bir kapı!" dedi Keloğlan. Balkız da güldü ve ellerini çırptı. Keloğlan gülerek Balkız'a sarıldı. Keloğlan çok sevindi, çünkü kapı şeklini sonunda o da görmüştü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 4: «Keloğlan dürüst davrandı ve "Göremiyorum, Balkız, hangisi?" diye sordu.»
   - Açıklama: Tohumdaki dürüstlük özelliği 3. cümledeki doğruyu söylememe ile çelişiyor, tutarlı kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0094` birebir aynı, `@degisim: paslı -> beyaz` (tutuyorsan), ardından `@onarim: 308d2befadcff26b48529bfa45ae2bd89392ffb7`, sonra gövde.

### Hikâye 3: tohum keloglan-0109 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0109
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'saksı', fiil 'seçmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: cevizler saksının sert kenarına çarpıp dışarı düşüyordu | saksıyı yere yatırdı ve cevizleri yerden yuvarladı
@tohum: keloglan-0109
Keloğlan evde eğlenceli bir oyun oynuyordu. En büyük boş saksıyı seçti ve duvarın dibine koydu. Ama attığı cevizler saksının sert kenarına çarpıp dışarı düşüyordu. Keloğlan yere bir ip koymuştu ve cevizleri ipin arkasından atıyordu. Keloğlan dürüst davrandı, ipin arkasında kaldı ve biraz düşündü. Sonra saksıyı yere yan yatırdı. Bu sefer cevizi atmadı, yerden yavaşça yuvarladı. Ceviz yerde ilerledi ve içeri girdi. Keloğlan öteki cevizleri de tek tek yuvarladı. Hepsi saksının içinde toplandı. Keloğlan çok sevindi, çünkü bütün cevizleri ipin arkasından saksıya sokmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst davrandı, ipin arkasında kaldı"
   - Cümle 5: «Keloğlan dürüst davrandı, ipin arkasında kaldı ve biraz düşündü.»
   - Açıklama: Hile yapma isteği hiç kurulmadan dürüstlük sebepsizce araya sokuluyor ve olay akışından çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0109` birebir aynı, ardından `@onarim: e6c5334cb06ff8f2caf93617cfb1690d72be524e`, sonra gövde.

### Hikâye 4: tohum keloglan-0111 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0111
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kaşık', fiil 'hazırlanmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ormanda nereden geldiği bilinmeyen bir ses vardı | aramayı bırakmadı ve sesin kendi çantasından geldiğini buldu
@tohum: keloglan-0111
Hafif bir rüzgar esiyordu. Keloğlan çantasını alçak bir dala astı ve yemeğe hazırlandı. Birden yakından ince bir ses geldi. Keloğlan bu sesin nereden geldiğini çok merak etti. Büyük bir kayanın arkasına baktı ama hiçbir şey göremedi. Biraz mutsuz oldu. Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı. Durdu ve sesi dikkatle dinledi. Sonunda sesin kendi çantasından geldiğini buldu. Rüzgar çantayı sallıyordu. İçindeki kaşık da bardağa çarpıp ses çıkarıyordu. Keloğlan güldü ve kaşığı çıkardı. Ses hemen kesildi. Keloğlan bundan sonra bir sesi merak edince onu bulana kadar aradı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: 'Dürüst' aramayı bırakmamakla ilgili değil; kelime yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' aramayı bırakmamakla ilgili değil; özellik kelimesi yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Dürüstlük özelliği işe yaramıyor; aramayı sürdürmek dürüstlükle değil azimle açıklanıyor ve kartın özellik alanı işe yarar biçimde kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 7: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Dürüst olmak aramayı sürdürmenin sebebi değil; olay bir öncekinden çıkmıyor.
   - Açıklama: Dürüstlük aramayı sürdürmenin sebebi olamaz; ayrıntı olayla ilgisiz bir gerekçe kuruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0111` birebir aynı, ardından `@onarim: 5aff33ae7cc9c43abdd6948291cd02ea1280bf1d`, sonra gövde.

### Hikâye 5: tohum keloglan-0113 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0113
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'basamak', fiil 'hızlanmak', sıfat 'serin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: ekmeklerin üstüne tepeden küçük şeyler düşüyordu | anasına sordu ve ağacın altından çıktı
@tohum: keloglan-0113
@degisim: basamak -> kozalak
Ormanda serin bir rüzgar esiyordu. Keloğlan anasıyla büyük bir ağacın altında yemek yiyordu. Ama ekmeklerin üstüne tepeden tık tık küçük şeyler düşüyordu. Keloğlan bu sesi çok merak etti. Bunlardan birini aldı ve anasına gösterdi. "Anneciğim, bu nedir?" diye sordu Keloğlan. "Bu bir kozalak, ağacın dallarından düşüyor," dedi anası. O sırada rüzgar hızlandı ve bir kozalak daha tık diye düştü. Keloğlan böylece kozalakları rüzgarın düşürdüğünü öğrendi. Hemen ekmekleri aldı ve anasıyla ağacın altından çıktı. Yeni yerde ekmeklerin üstüne hiç kozalak düşmedi. Keloğlan çok sevindi, çünkü sesi yapan kozalakları bulmuş ve ekmeklerini korumuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi yapan kozalakları bulmuş"
   - Cümle 12: «Keloğlan çok sevindi, çünkü sesi yapan kozalakları bulmuş ve ekmeklerini korumuştu.»
   - Açıklama: 'Sesi yapmak' yanlış kullanım; 'sesi çıkaran' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0113` birebir aynı, `@degisim: basamak -> kozalak` (tutuyorsan), ardından `@onarim: 7643946a6731393b67f8ae85ce22febc02c75599`, sonra gövde.

### Hikâye 6: tohum keloglan-0114 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0114
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'taç', fiil 'serinletmek', sıfat 'bulutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: sıcaktan tacın çiçekleri aşağı eğildi | arkadaşına sordu ve tacı soğuk suya koydu
@tohum: keloglan-0114
Hava bulutluydu ama çok sıcaktı. Keloğlan evde Balkız için çiçeklerden bir taç yapmıştı. Ama sıcaktan tacın çiçekleri aşağı eğildi. O sırada Balkız kapıdan içeri girdi. "Ne saklıyorsun, Keloğlan?" diye sordu Balkız. Keloğlan tacı saklamadı, çünkü dürüsttü. "Senin için yaptım, sıcakta bozuldu, ne yapalım?" diye sordu Keloğlan. "Çiçekler soğuk suda kalkar," dedi Balkız. Keloğlan bir kova su getirdi. Tacı suya koydu ve çiçekleri serinletti. Biraz sonra çiçekler yeniden yukarı kalktı. Keloğlan tacı Balkız'ın başına taktı. "Çok güzel bir taç, teşekkür ederim, Keloğlan!" dedi Balkız.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ne saklıyorsun, Keloğlan?"
   - Cümle 5: «"Ne saklıyorsun, Keloğlan?" diye sordu Balkız.»
   - Açıklama: Keloğlan hiçbir şey saklamazken Balkız ne sakladığını soruyor ve hemen ardından tacı saklamadığı söyleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Keloğlan tacı saklamadı, çünkü dürüsttü"
   - Cümle 6: «Keloğlan tacı saklamadı, çünkü dürüsttü.»
   - Açıklama: Balkız ne sakladığını soruyor ama Keloğlan'ın hiçbir şey saklamadığı söyleniyor; soru ile olay çelişiyor.
3. **K5** (K merceği) — Konuşmayan karakter konuşmuyor; dünyanın kuralları çiğnenmiyor.
   - Alıntı: "Keloğlan tacı Balkız'ın başına taktı"
   - Cümle 12: «Keloğlan tacı Balkız'ın başına taktı.»
   - Açıklama: Balkız için özel çiçek tacı yapıp başına takmak, kartın dünya kurallarındaki aşk konusu yasağına yaklaşan romantik bir çağrışım taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0114` birebir aynı, ardından `@onarim: bb9843d699eb97b2a8b91c9213ffb272218188ac`, sonra gövde.

### Hikâye 7: tohum keloglan-0115 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0115
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kıyafet', fiil 'güneşlenmek', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: yeşil boya döküldü ve bitti | sarı ile maviyi karıştırıp yeşil yaptı
@tohum: keloglan-0115
Tepede hafif bir rüzgar esiyordu. Keloğlan'ın eşeği Karakaçan otların üstünde güneşleniyordu. Sakar Keloğlan ilk kez resim yapıyordu ve yeşil boyayı elinden düşürdü. Bütün boya mavi kıyafetine döküldü. Elinde yalnız sarı ve mavi boya kaldı. Keloğlan resimdeki otlar için ne yapacağını düşündü. Sonra yeni bir şey denedi ve sarı ile maviyi fırçayla karıştırdı. Yeşil bir boya oldu ve Keloğlan güldü. Hemen resimdeki otları yeşile boyadı. Karakaçan resme bakıp başını salladı. Keloğlan artık sarı ile maviden yeşil yapmayı biliyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bütün boya mavi kıyafetine döküldü"
   - Cümle 4: «Bütün boya mavi kıyafetine döküldü.»
   - Açıklama: Kıyafetin boyanması ikinci bir sorun gibi kuruluyor ama bir daha ele alınmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0115` birebir aynı, ardından `@onarim: 016af0161c67ad1c614a08ea563eebc460789061`, sonra gövde.

### Hikâye 8: tohum keloglan-0116 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0116
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kereviz', fiil 'küçültmek', sıfat 'ferah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: anası acıkmıştı ve sert kereviz ikiye kırılmadı | kerevizi taşa vurdu ve ikiye ayırdı
@tohum: keloglan-0116
@degisim: ferah -> düz
Keloğlan anasıyla ormanda büyük ve düz bir taşa oturdu. Anası çok acıkmıştı ve çantada yalnız bir kereviz vardı. Keloğlan onu paylaşmak istedi, ama kereviz çok sertti. Kerevizi küçültmek için iki eliyle bükmeye çalıştı. Kereviz kırılmadı ve sakar Keloğlan'ın elinden kayıp kucağına düştü. Keloğlan kerevizi yine aldı ve taşa baktı. Sonra kerevizi taşın kenarına bir kez vurdu. Kereviz çat diye ikiye ayrıldı. "Anneciğim, bu parça senin, bu da benim," dedi Keloğlan. Anası parçasını aldı ve Keloğlan'ı öptü. İkisi kerevizi mutlu mutlu yedi. "Teşekkürler, Keloğlan, birlikte yemek çok güzel!" dedi anası.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kerevizi küçültmek için iki"
   - Cümle 4: «Kerevizi küçültmek için iki eliyle bükmeye çalıştı.»
   - Açıklama: Amaç kerevizi ikiye bölmek; 'küçültmek' yanlış anlamda.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sakar Keloğlan'ın elinden kayıp"
   - Cümle 5: «Kereviz kırılmadı ve sakar Keloğlan'ın elinden kayıp kucağına düştü.»
   - Açıklama: Tohumdaki sakarlık özelliği kerevizi düşürmekle kalıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elinden kayıp kucağına düştü"
   - Cümle 5: «Kereviz kırılmadı ve sakar Keloğlan'ın elinden kayıp kucağına düştü.»
   - Açıklama: Kerevizin kucağa düşmesi olayı ilerletmeyen, çözüme hiçbir katkısı olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0116` birebir aynı, `@degisim: ferah -> düz` (tutuyorsan), ardından `@onarim: 500012a133aff1430f192d62b43ee8b8e0501328`, sonra gövde.

### Hikâye 9: tohum keloglan-0117 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0117
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fide', fiil 'gerinmek', sıfat 'kısa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: fidan rüzgarda yana yatıyordu ve dallar kısaydı | ağaçların arasında uzun bir dal buldu ve fidanı bağladı
@tohum: keloglan-0117
@degisim: fide -> fidan
Bir sabah Keloğlan ile Balkız ormanda küçük bir fidan dikiyordu. Rüzgar esince ince fidan hep yana yatıyordu. Onu bağlamak için yerdeki dallar çok kısaydı. "Balkız, uzun bir dal bulacağım," dedi Keloğlan. Ayağa kalkıp gerindi ve ağaçların arasına baktı. Büyük bir ağacın dibinde uzun, kuru bir dal gördü. Sakar Keloğlan dalı bir kez düşürdü ve hemen aldı. Sonra dalı fidanın yanında toprağa bastırdı. "Balkız, ipin var mı?" diye sordu Keloğlan. Balkız cebinden bir ip çıkardı ve Keloğlan fidanı dala bağladı. Rüzgar yine esti, ama fidan dik kaldı. "Teşekkürler, Keloğlan, fidanımız kurtuldu!" dedi Balkız.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sakar Keloğlan dalı bir kez düşürdü"
   - Cümle 7: «Sakar Keloğlan dalı bir kez düşürdü ve hemen aldı.»
   - Açıklama: Tohumdaki sakarlık özelliği süs olarak ekleniyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan dalı bir kez düşürdü ve hemen aldı"
   - Cümle 7: «Sakar Keloğlan dalı bir kez düşürdü ve hemen aldı.»
   - Açıklama: Dalı düşürmek olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Dalın düşürülmesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0117` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: f3cdcba668325aee7370355836d8036e3e232bf9`, sonra gövde.

### Hikâye 10: tohum keloglan-0120 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0120
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'ip', fiil 'kırpmak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: uçurtmadan gürültülü bir ses geliyordu | uçurtmaya baktı ve fazla ipi sardı
@tohum: keloglan-0120
@degisim: kırpmak -> sarmak
Bir sabah Keloğlan ile Bilgecan Dede tepede uçurtma uçuruyordu. Birden yukarıdan gürültülü bir ses geldi. "Dede, bu ses nereden geliyor?" diye sordu Keloğlan. "Sen ne düşünüyorsun?" diye sordu Dede. Keloğlan dürüst davrandı. "Bilmiyorum, Dede, ama bakacağım," dedi Keloğlan. Keloğlan uçurtmayı yavaşça indirdi ve her yerine dikkatle baktı. Uçurtmanın altında çok uzun bir ip parçası sallanıyordu. Rüzgar esince bu ip uçurtmaya çarpıp ses yapıyordu. Keloğlan ipin fazla ucunu uçurtmaya sıkıca sardı. Uçurtma bu kez sessizce yükseldi. Keloğlan çok sevindi, çünkü sesin nereden geldiğini kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yukarıdan gürültülü bir ses geldi"
   - Cümle 2: «Birden yukarıdan gürültülü bir ses geldi.»
   - Açıklama: Uçurtmadan gelen bir ses zarar vermeyen önemsiz bir olay; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 5: «Keloğlan dürüst davrandı.»
   - Açıklama: Dürüstlük cümlesi olaya bağlanmayan, işlevsiz bir ayrıntı olarak araya sokulmuş.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ipin fazla ucunu uçurtmaya"
   - Cümle 10: «Keloğlan ipin fazla ucunu uçurtmaya sıkıca sardı.»
   - Açıklama: 'Fazla' uca bağlanmış, anlam bozuk; 'ipin fazla kalan ucunu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0120` birebir aynı, `@degisim: kırpmak -> sarmak` (tutuyorsan), ardından `@onarim: 1c2f47459c10b97361ec08671f5570eb4a202917`, sonra gövde.

### Hikâye 11: tohum keloglan-0121 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0121
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'etiket', fiil 'dinlenmek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar sert sepetten hep dışarı zıplıyordu | sepetin içine yumuşak yosun koydu
@tohum: keloglan-0121
@degisim: etiket -> kozalak
Keloğlan ormanda eğlenceli bir oyun oynuyordu. Kozalakları uzaktan sepetine atıyordu. Ama sepet çok sertti ve kozalaklar hep dışarı zıplıyordu. Keloğlan birkaç kez daha denedi ama olmadı. Sonra yoruldu ve bir kütüğün üstüne oturup dinlendi. Kütüğün yanında sulu toprak ve yumuşak yosunlar vardı. Keloğlan merak etti ve bir kozalağı yosunların üstüne attı. Kozalak hiç zıplamadı. Böylece kozalağın yumuşak yerde durduğunu öğrendi. Hemen sepetin dibine biraz yosun koydu. Sonra kozalakları yine attı. Bu kez hepsi sepette kaldı ve Keloğlan sevinçle el çırptı. Keloğlan bundan sonra oyunda hep sepete yosun koydu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kütüğün yanında sulu toprak ve yumuşak yosunlar vardı"
   - Cümle 6: «Kütüğün yanında sulu toprak ve yumuşak yosunlar vardı.»
   - Açıklama: Sulu toprak işlevsiz bir ayrıntı ve yosunlar çözümü getirmek için tesadüfen beliriyor.
   - Açıklama: Sulu toprak işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor ve yosun çözümü tesadüfen önüne getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0121` birebir aynı, `@degisim: etiket -> kozalak` (tutuyorsan), ardından `@onarim: 3559a5036a6d488c71a2070a59ed451f450d47a7`, sonra gövde.

### Hikâye 12: tohum keloglan-0122 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0122
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yonca', fiil 'götürmek', sıfat 'sert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: rüzgar otları sallıyordu ve yaprakları saymak zordu | otları eliyle tuttu ve birer birer saydı
@tohum: keloglan-0122
Rüzgar ormanda sert esiyordu. Keloğlan ilk kez dört yapraklı bir yonca aramayı denedi. Ama rüzgar yüzünden otlar hep sallanıyordu ve yaprakları saymak zordu. Keloğlan bir yonca buldu ve eliyle tuttu. Böylece yonca sallanmadı, ama yalnız üç yaprağı vardı. Keloğlan onu dört yapraklı diye cebine koymadı, çünkü dürüsttü. Sonra öteki otları da birer birer eliyle tuttu ve saydı. Sonunda gerçek bir dört yapraklı yonca buldu. Keloğlan onu eve götürmek için dikkatle cebine koydu ve sevinçle güldü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan onu dört yapraklı diye cebine koymadı, çünkü dürüsttü"
   - Cümle 6: «Keloğlan onu dört yapraklı diye cebine koymadı, çünkü dürüsttü.»
   - Açıklama: Kimseyi kandırma durumu yokken dürüstlük gerekçesi sebepsiz ve işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0122` birebir aynı, ardından `@onarim: 9b1b5507a9e4530d334ca6a663206c2ca35f6c2f`, sonra gövde.
