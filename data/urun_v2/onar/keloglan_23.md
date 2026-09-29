# Editör görevi (onarım): Keloğlan, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0006 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0006
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: paylaşmak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'jöle', fiil 'çoğalmak', sıfat 'yırtık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: un az kaldı ve kek ikisine yetmezdi | annesine sorup hamura elma kattı ve keki paylaştı
@tohum: keloglan-0006
@degisim: jöle -> kek
Bir sabah Keloğlan ile anası evde kek yapmak istedi. Ama un torbası yırtıktı ve unun çoğu yere dökülmüştü. Kalan un çok azdı, bu yüzden kek ikisine yetmezdi. Keloğlan keki annesiyle paylaşmak istiyordu. "Anneciğim, hamur nasıl çoğalır?" diye sordu Keloğlan. "Hamura elma parçaları koy," dedi anası. Keloğlan yeni şeyler öğrenmeyi severdi ve hemen denedi. Küçük elma parçalarını hamura kattı. Hamur gerçekten çoğaldı. Az sonra fırından büyük bir kek çıktı. Keloğlan keki ikiye böldü ve yarısını annesine verdi. Anası keki tattı ve gülümsedi. "Seninle paylaşmak çok güzel, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "annesine sorup hamura elma kattı"
   - Cümle 0 (plan satırı): «un az kaldı ve kek ikisine yetmezdi | annesine sorup hamura elma kattı ve keki paylaştı»
   - Açıklama: Planda elmayı Keloğlan katıyor ama gövdede elmayı anası katıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0006` birebir aynı, `@degisim: jöle -> kek` (tutuyorsan), ardından `@onarim: 3443e146ff6d7a6c4b025f959f45784d7b834459`, sonra gövde.

### Hikâye 2: tohum keloglan-0010 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0010
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'odun', fiil 'süpürmek', sıfat 'kırık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: kule kuru yaprakların üstünde kayıp yıkıldı | yaprakları kırık dalla süpürdü ve kuleyi düz yerde yaptı
@tohum: keloglan-0010
Bir sabah Keloğlan ile eşeği Karakaçan ormanda küçük bir odun kulesi yapıyordu. Karakaçan sırtında odunlar getirdi, Keloğlan onları üst üste dizdi. Ama yer kuru yapraklarla doluydu ve kule onların üstünde kayıp yıkıldı. Keloğlan yaprakların altında ne olduğunu öğrenmek istedi. Bir yaprağı kaldırdı ve altında düz, sert toprak gördü. Hemen kırık bir dal aldı ve yaprakları sağa sola süpürdü. Keloğlan kuleyi bu düz toprağın üstüne yeniden yaptı. "Bak, Karakaçan, kulemiz bu kez hiç kaymadı!" dedi Keloğlan. Karakaçan başını salladı. Keloğlan çok sevindi, çünkü kuleyi birlikte bitirmişlerdi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yaprakları kırık dalla süpürdü"
   - Cümle 0 (plan satırı): «kule kuru yaprakların üstünde kayıp yıkıldı | yaprakları kırık dalla süpürdü ve kuleyi düz yerde yaptı»
   - Açıklama: Plan süpürmeyi Keloğlan'a veriyor ama gövdede yaprakları eşek süpürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0010` birebir aynı, ardından `@onarim: 3332637806c3080c7acbf0b90d5d613c85b44284`, sonra gövde.

### Hikâye 3: tohum keloglan-0020 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0020
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kaktüs', fiil 'koparmak', sıfat 'yağmurlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: küçük yaprak gemisi suda batıyordu | büyük bir yaprak koparıp kenarlarını kıvırdı
@tohum: keloglan-0020
@degisim: kaktüs -> yaprak
Bir sabah ormanda hava yağmurluydu ve yerde küçük bir su yolu vardı. Keloğlan ile Bilgecan Dede bu suda yaprak gemisi yarışı yapıyordu. Ama Keloğlan'ın gemisi hep batıyordu, çünkü yaprağı çok küçüktü. "Dede, benim gemim neden batıyor?" diye sordu Keloğlan. "Büyük bir yaprak al ve kenarlarını kıvır," dedi Bilgecan Dede. Keloğlan daldan geniş bir yaprak kopardı ve kenarlarını kıvırdı. Yeni gemi suda batmadı ve hızla yüzdü. Keloğlan sevinçle ellerini çırptı. Sonra iki gemi yan yana yüzdü. "Teşekkürler, Dede, yüzen bir gemi yapmayı öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Büyük bir yaprak al ve kenarlarını kıvır"
   - Cümle 5: «"Büyük bir yaprak al ve kenarlarını kıvır," dedi Bilgecan Dede.»
   - Açıklama: Çözümü Keloğlan bulmuyor; Bilgecan Dede çözümün tamamını hazır söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0020` birebir aynı, `@degisim: kaktüs -> yaprak` (tutuyorsan), ardından `@onarim: e9055530dae46750fcdde447e0a892434f20a016`, sonra gövde.

### Hikâye 4: tohum keloglan-0042 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0042
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yağmurluk', fiil 'boyamak', sıfat 'yemyeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: resmi boyamak için yeşil boya bitmişti | dededen yardım isteyip sarı ile maviyi karıştırdı
@tohum: keloglan-0042
@degisim: yağmurluk -> fırça
Keloğlan tepede resim yapma oyunu oynuyordu. Bilgecan Dede de yanına oturmuş, onu izliyordu. Keloğlan kağıttaki tepeyi boyamak istedi ama yeşil boyası bitmişti. Elinde yalnız sarı ile mavi boya vardı. "Dede, yeşil boyam bitti, ne yapayım?" diye sordu Keloğlan. "Sarı ile maviyi karıştır, yeşil olur," dedi Bilgecan Dede. Keloğlan biraz sakardı ve sarı boya kabını elinden düşürdü. Sarı boya mavi boyanın içine döküldü. Sonra fırçasıyla iki rengi karıştırdı. Mavi renk yeşile döndü. Keloğlan resimdeki tepeyi yemyeşil boyadı. Bilgecan Dede resmi görünce ellerini çırptı. Keloğlan da mutlu mutlu yeni bir resme başladı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sarı boya kabını elinden düşürdü"
   - Cümle 7: «Keloğlan biraz sakardı ve sarı boya kabını elinden düşürdü.»
   - Açıklama: Boyaların karışması Keloğlan'ın kararıyla değil sebepsiz bir kazayla geliyor.
   - Açıklama: Çözüm Keloğlan'ın kendi eylemiyle değil sebepsiz bir kazayla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0042` birebir aynı, `@degisim: yağmurluk -> fırça` (tutuyorsan), ardından `@onarim: 3b6773ddb5b3a2e6acc35a0ebbdb50df8cb60e60`, sonra gövde.

### Hikâye 5: tohum keloglan-0045 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0045
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'boya', fiil 'duymak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: boya kabını düşürdü ve boya yere döküldü | dededen özür diledi ve evi birlikte boyadılar
@tohum: keloglan-0045
@degisim: hazırlıklı -> kırmızı
Ormanda Bilgecan Dede kuşlar için tahta bir ev boyuyordu. Keloğlan ona çantasında iki kap kırmızı boya getirmişti. Ama Keloğlan biraz sakardı, bir kabı düşürdü ve boya yere döküldü. Bilgecan Dede sesi duydu ve arkasına döndü. Keloğlan yerdeki kırmızı lekeye baktı ve başını eğdi. "Özür dilerim, dede, kabı ben düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan," dedi Bilgecan Dede ve gülümsedi. Keloğlan çantasından ikinci kabı çıkardı ve onu iki eliyle sıkıca tuttu. İkisi evi birlikte boyadı ve bitirdi. Keloğlan çok sevindi, çünkü dede ona kızmamıştı ve kuşların evi hazırdı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 3: «Ama Keloğlan biraz sakardı, bir kabı düşürdü ve boya yere döküldü.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Sakar' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0045` birebir aynı, `@degisim: hazırlıklı -> kırmızı` (tutuyorsan), ardından `@onarim: 52d00afeaedf8b2dd07bcd99c6fad3dae0bb567a`, sonra gövde.

### Hikâye 6: tohum keloglan-0053 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0053
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'dolma', fiil 'esmek', sıfat 'parlak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek sırasını bekleyemedi ve topu hep kendisi itti | bir sen bir ben diyerek sırayla oynamayı önerdi
@tohum: keloglan-0053
@degisim: dolma -> top
Bir sabah ormanda serin bir rüzgar esiyordu. Keloğlan ile eşeği Karakaçan parlak bir topu büyük bir ağaca doğru itiyordu. Ama Karakaçan sırasını bekleyemedi ve topu hep kendisi itti. Keloğlan Karakaçan'ın başını okşadı. "Karakaçan, bir sen, bir ben oynayalım," dedi Keloğlan. Karakaçan başını salladı. Keloğlan topa ayağıyla bir kez vurdu. Sonra dürüst davrandı ve Karakaçan'ı bekledi. Karakaçan da topu burnuyla itti. Sıra yine Keloğlan'daydı. Keloğlan topa vurdu ve top ağaca değdi. Karakaçan sevinçle anırdı. Keloğlan çok mutluydu, çünkü sırayla oynamak çok eğlenceli olmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra dürüst davrandı ve"
   - Cümle 8: «Sonra dürüst davrandı ve Karakaçan'ı bekledi.»
   - Açıklama: Sırasını beklemek dürüstlük değil sabır ya da adalettir; kelime yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra dürüst davrandı"
   - Cümle 8: «Sonra dürüst davrandı ve Karakaçan'ı bekledi.»
   - Açıklama: Sırasını beklemek dürüstlük değildir; 'dürüst' yanlış anlamda kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra dürüst davrandı ve Karakaçan'ı bekledi"
   - Cümle 8: «Sonra dürüst davrandı ve Karakaçan'ı bekledi.»
   - Açıklama: Tohumdaki dürüstlük özelliği karttaki gibi kullanılmıyor; sıra beklemek dürüstlük olarak yapıştırılmış ve sorunu çözmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0053` birebir aynı, `@degisim: dolma -> top` (tutuyorsan), ardından `@onarim: 8a49c2a2f1b941e9548cb4bcfdc4c3aa37d26fe6`, sonra gövde.

### Hikâye 7: tohum keloglan-0057 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0057
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kalem', fiil 'bindirmek', sıfat 'tozlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: tepede tuhaf bir ses duyuldu | sesin peşinden gidip kayada küçük bir delik buldu
@tohum: keloglan-0057
@degisim: bindirmek -> karıştırmak
Rüzgar esiyordu ve tepede tuhaf bir ses duyuluyordu. Keloğlan tozlu bir taşa oturmuş, kalemiyle resim çiziyordu. Bu sesi çok merak etti. Keloğlan biraz sakardı ve sesi önce eşeği Karakaçan'ın sesiyle karıştırdı. "Karakaçan, bunu sen mi yapıyorsun?" diye sordu Keloğlan. Karakaçan başını iki yana salladı. Keloğlan sesin peşinden kayaların arasına yürüdü. Bir kayanın dibinde küçük bir delik gördü. Deliği kapatmak için kalemini deliğin üstüne koydu. Kalem deliği kapattı ve ses hemen kesildi. Keloğlan kalemi aldı ve ses yeniden başladı. Rüzgar bu delikten geçerken ıslık gibi bir ses çıkarıyordu. "Buldum, Karakaçan, sesi bu küçük delik yapıyormuş!" dedi Keloğlan sevinçle.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan biraz sakardı ve sesi önce"
   - Cümle 4: «Keloğlan biraz sakardı ve sesi önce eşeği Karakaçan'ın sesiyle karıştırdı.»
   - Açıklama: Sesleri karıştırmak sakarlık değildir; 'sakar' yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan biraz sakardı ve"
   - Cümle 4: «Keloğlan biraz sakardı ve sesi önce eşeği Karakaçan'ın sesiyle karıştırdı.»
   - Açıklama: 'Sakar' beceriksiz demektir; sesleri karıştırmakla ilgisi yok, kelime yanlış anlamda.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve sesi"
   - Cümle 4: «Keloğlan biraz sakardı ve sesi önce eşeği Karakaçan'ın sesiyle karıştırdı.»
   - Açıklama: Sakarlık özelliği sebepsiz ekleniyor; bir ıslık sesini eşek sesiyle karıştırmak sakarlıktan çıkmıyor ve olaya işlev katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0057` birebir aynı, `@degisim: bindirmek -> karıştırmak` (tutuyorsan), ardından `@onarim: e0a8a05a9946c7da74582acb4a904968fe6eb13e`, sonra gövde.

### Hikâye 8: tohum keloglan-0058 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Bilgecan Dede
@tohum: keloglan-0058
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'atkı', fiil 'kutlamak', sıfat 'yetenekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Bilgecan Dede
@plan: ikisi ipi aynı anda çekti ve topaç devrildi | sırayla oynamayı önerdi ve atkıyı dedeye verdi
@tohum: keloglan-0058
@degisim: yetenekli -> hızlı
Keloğlan ile Bilgecan Dede evde tahta bir topaçla oynuyordu. Topacın yalnız bir ipi vardı. İkisi de ipi aynı anda çekti ve topaç devrildi. "Sırayla oynayalım, atkı sende olunca sen çevir," dedi Keloğlan. Sonra atkısını çıkardı ve dedenin boynuna taktı. Dede ipi çekince topaç masada uzun uzun döndü. "Dede, topacın çok hızlı döndü!" dedi Keloğlan. Dede gülümsedi ve atkıyı Keloğlan'a geri verdi. Keloğlan biraz sakardı ve ipi çekerken topacı masadan düşürdü. Ama topaç yerde de güzelce döndü. İkisi bunu el çırparak kutladı. Keloğlan çok sevindi, çünkü sırayla oynamak ikisini de mutlu etmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve ipi çekerken topacı masadan düşürdü"
   - Cümle 9: «Keloğlan biraz sakardı ve ipi çekerken topacı masadan düşürdü.»
   - Açıklama: Sorun çözüldükten sonra olaydan çıkmayan yeni bir sakarlık olayı ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ipi çekerken topacı masadan düşürdü"
   - Cümle 9: «Keloğlan biraz sakardı ve ipi çekerken topacı masadan düşürdü.»
   - Açıklama: Sorun çözüldükten sonra sakarlıkla gelen düşme olayı hiçbir sonuç doğurmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0058` birebir aynı, `@degisim: yetenekli -> hızlı` (tutuyorsan), ardından `@onarim: 4714fe16b0f628087b149fe70238f418c99ba6f2`, sonra gövde.

### Hikâye 9: tohum keloglan-0061 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0061
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'davul', fiil 'parıldamak', sıfat 'saygılı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: annesine sormadan tencereyi alıp davul gibi çaldı | özür dileyip tencereyi geri verdi
@tohum: keloglan-0061
@degisim: saygılı -> üzgün
Keloğlan evde davul çalmak istedi. Anasına sormadan mutfaktan parıldayan büyük tencereyi aldı. Tencereyi ters çevirdi ve kaşıkla davul gibi çaldı. Tam o sırada anası mutfağa girdi. "Keloğlan, tencerem nerede? Çorba pişirecektim," dedi anası. Keloğlan tencereyi hemen anasına geri verdi. "Sormadan aldım, özür dilerim, anneciğim," dedi Keloğlan üzgün bir sesle. Anası gülümsedi ve onu kucakladı. "Davul çalmayı öğrenmek istiyorum, eski kovayı alabilir miyim?" diye sordu Keloğlan. Anası başını salladı ve kovayı ona verdi. Anası çorbayı pişirirken Keloğlan kovaya kaşıkla vurdu. İkisi mutfakta mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tam o sırada anası mutfağa girdi"
   - Cümle 4: «Tam o sırada anası mutfağa girdi.»
   - Açıklama: Keloğlan tencereyi mutfaktan alıp başka yerde çalmışken anası mutfakta tencereyi arıyor ama Keloğlan onu hemen geri veriyor; sahne ve gürültülü davul sesi tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0061` birebir aynı, `@degisim: saygılı -> üzgün` (tutuyorsan), ardından `@onarim: 4616027d7e50a1941b3c2a3c56b64df76a8a90f1`, sonra gövde.

### Hikâye 10: tohum keloglan-0063 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0063
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kağıt', fiil 'sıçramak', sıfat 'kilitli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: rüzgar kağıt topu sepetten uzağa itti | rüzgarın durmasını bekledi ve topu yavaşça attı
@tohum: keloglan-0063
@degisim: kilitli -> beyaz
Rüzgar tepede hafif hafif esiyordu. Keloğlan beyaz kağıttan topunu eşeği Karakaçan'ın sırtındaki sepete atmak istiyordu. Ama rüzgar kağıt topu her seferinde sepetten uzağa itti. Bir kez top sepetin kenarına çarptı ve yere sıçradı. Keloğlan topu yerden aldı. Dürüst ve azimli bir çocuktu, atmayı bırakmadı. "Top içeri girmedi, bir daha atacağım," dedi Keloğlan. Sonra rüzgarın durmasını bekledi. Rüzgar durunca topu yavaşça attı. Kağıt top sepetin içine düştü. Karakaçan başını salladı ve neşeyle anırdı. Keloğlan çok sevindi, çünkü kağıt topu sonunda sepete sokmuştu.
```

**Hakem bulguları (2):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: ""Top içeri girmedi, bir daha atacağım," dedi Keloğlan"
   - Cümle 7: «"Top içeri girmedi, bir daha atacağım," dedi Keloğlan.»
   - Açıklama: Yanında yalnız eşek varken Keloğlan kendi kendine konuşuyor.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "bir daha atacağım," dedi Keloğlan"
   - Cümle 7: «"Top içeri girmedi, bir daha atacağım," dedi Keloğlan.»
   - Açıklama: Keloğlan kimseye seslenmeden kendi kendine konuşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0063` birebir aynı, `@degisim: kilitli -> beyaz` (tutuyorsan), ardından `@onarim: 6018d38e3f4e3c67edb63f6b560f7f7f87ccf60f`, sonra gövde.

### Hikâye 11: tohum keloglan-0064 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Hava soğuktu ama güneş parlıyordu. Keloğlan tepede yürürken küçük bir ses duydu. Ses tık tık diye geliyordu ama ortada hiçbir şey yoktu. Keloğlan bu sesi çok merak etti. Önce bir taşın düştüğünü sandı ama hiç taş görmedi. Keloğlan dürüst ve azimli bir çocuktu, aramayı hiç bırakmadı. Sesi dinleyerek bir kayanın yanına gitti. Kayanın üstünde küçük, ışıltılı bir buz vardı. Buz güneşte yavaş yavaş çözülüp su oluyordu. Taşa düşen damlalar tık tık ses çıkarıyordu. Keloğlan çok sevindi, çünkü sesin nereden geldiğini sonunda bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses tık tık diye geliyordu"
   - Cümle 3: «Ses tık tık diye geliyordu ama ortada hiçbir şey yoktu.»
   - Açıklama: Merak edilen bir ses gerçek bir sorun değil; çocuğun önemseyeceği bir güçlük yok.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "sandı ama hiç taş görmedi"
   - Cümle 5: «Önce bir taşın düştüğünü sandı ama hiç taş görmedi.»
   - Açıklama: İlk beş cümlenin üçünde 'ama' bağlacı tekrarlanıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, ışıltılı bir buz"
   - Cümle 8: «Kayanın üstünde küçük, ışıltılı bir buz vardı.»
   - Açıklama: 'Işıltılı' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0064` birebir aynı, `@degisim: önlük -> buz` (tutuyorsan), ardından `@onarim: ec93b2647d41915133530d4572375da144daea0f`, sonra gövde.

### Hikâye 12: tohum keloglan-0065 (deneme 3 -> 4)

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
@plan: kırmızı elmalar yüksek bir dalda duruyordu | doğruyu söyleyip anasından yardım istedi
@tohum: keloglan-0065
@degisim: tuğla -> elma
Ormanda kuşlar ötüyordu. Keloğlan ile anası büyük bir ağacın altında elma topluyordu. Ama en kırmızı elmalar yüksek bir dalda duruyordu ve Keloğlan onlara yetişemedi. Keloğlan ağaca tırmanmaktan çekindi, çünkü dal çok inceydi. Keloğlan dürüst bir çocuktu ve anasına doğruyu söyledi. "Anneciğim, elim dala yetişmiyor, yardım eder misin?" dedi Keloğlan. "Tabii ki," dedi anası. Anası temkinliydi, dalı kırmamak için yavaşça aşağı eğdi. Keloğlan kırmızı elmaları tek tek sepete koydu. Sepet kısa sürede doldu. Sonra ikisi ağacın gölgesinde oturdu ve elmaları mutlu mutlu yedi.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ağaca tırmanmaktan çekindi, çünkü dal çok inceydi"
   - Cümle 4: «Keloğlan ağaca tırmanmaktan çekindi, çünkü dal çok inceydi.»
   - Açıklama: Tırmanmaktan kaçınmanın gerekçesi yalnız dalın inceliği olarak verildiği için kalın dala tırmanmak uygunmuş gibi örtük bir mesaj taşıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağaca tırmanmaktan çekindi"
   - Cümle 4: «Keloğlan ağaca tırmanmaktan çekindi, çünkü dal çok inceydi.»
   - Açıklama: 'Çekinmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve anasına doğruyu söyledi"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve anasına doğruyu söyledi.»
   - Açıklama: Tohumdaki dürüstlük özelliği sorunu çözmekte işe yaramıyor; yalnız yardım istemek dürüstlük diye etiketleniyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve anasına doğruyu söyledi"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve anasına doğruyu söyledi.»
   - Açıklama: Saklanacak ya da yalan söylenecek bir şey yokken dürüstlük işlevsiz biçimde araya sokuluyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anası temkinliydi, dalı kırmamak"
   - Cümle 8: «Anası temkinliydi, dalı kırmamak için yavaşça aşağı eğdi.»
   - Açıklama: 'Temkinli' kelimesini 3 yaşındaki bir çocuk bilmez.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anası temkinliydi, dalı"
   - Cümle 8: «Anası temkinliydi, dalı kırmamak için yavaşça aşağı eğdi.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0065` birebir aynı, `@degisim: tuğla -> elma` (tutuyorsan), ardından `@onarim: b1e94843787301e7c3df24a8965af93ece987e6e`, sonra gövde.
