# Editör görevi (onarım): Keloğlan, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0033 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0033
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'eldiven', fiil 'açmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek acıktı ama ormanda hiç ot yoktu | çantasını açıp havuçları eşeğine yedirdi
@tohum: keloglan-0033
@degisim: puantiyeli -> benekli
Keloğlan benekli eldivenleriyle ormanda odun topluyordu. Eşeği Karakaçan odunları sırtında taşıyordu. Birden Karakaçan durdu ve yürümedi, çünkü çok acıkmıştı. Ama büyük ağaçların altında hiç ot yoktu. "Bekle, Karakaçan, çantamda havuç var," dedi Keloğlan. Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı. Sonra çantasını açtı ve havuçları aldı. Havuçları Karakaçan'a tek tek verdi. Eşek hepsini yedi ve mutlu mutlu kuyruğunu oynattı. "Karnın doydu mu, Karakaçan?" diye sordu Keloğlan. Karakaçan başını iki kez salladı. Keloğlan çok sevindi, çünkü eşeği artık aç değildi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan benekli eldivenleriyle ormanda odun topluyordu"
   - Cümle 1: «Keloğlan benekli eldivenleriyle ormanda odun topluyordu.»
   - Açıklama: Eldivenler önemliymiş gibi kuruluyor ama sorunda ya da çözümde işe yaramıyor, yalnız sebepsizce çıkarılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "havuçları düşürmemek için eldivenlerini çıkardı"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı.»
   - Açıklama: Karttaki sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmiyor, yalnız önlem gerekçesi olarak geçiyor.
   - Açıklama: Güvenli özellik kullanımı sakarlığı düşürme ya da karıştırma olarak ister; burada sakarlık gösterilmiyor, yalnız önlem gerekçesi olarak anılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "havuçları düşürmemek için eldivenlerini çıkardı"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı.»
   - Açıklama: Eldiven ve sakarlık ayrıntısı sorunla ya da çözümle ilgisiz, işlevsiz bir ara adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0033` birebir aynı, `@degisim: puantiyeli -> benekli` (tutuyorsan), ardından `@onarim: 67a6be09e00593cc4167c22d60f4dce617d2428d`, sonra gövde.

### Hikâye 2: tohum keloglan-0034 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0034
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'krema', fiil 'güvenmek', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: sepet taşa çarptı ve arkadaşının keki ezildi | kekini ikiye bölüp arkadaşıyla paylaştı
@tohum: keloglan-0034
@degisim: güvenmek -> bölmek
Tepede serin bir rüzgar esiyordu. Keloğlan ile Balkız tekerlekli sepeti tepeye çekiyordu. Sepet bir taşa çarptı ve Balkız'ın keki yere düşüp ezildi. Balkız yerdeki keke üzgün üzgün baktı. Keloğlan'ın kremalı keki ise sepette duruyordu. Keloğlan kekini Balkız ile paylaşmak istedi. Keloğlan biraz sakardı, bu yüzden keki çok yavaş ikiye böldü. Kekin üstündeki krema hiç dökülmedi. Sonra büyük parçayı Balkız'a verdi. Balkız teşekkür etti ve gülümsedi. İkisi çimenlere oturdu ve parçalarını yedi. Keloğlan çok mutluydu, çünkü kekini arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden keki çok yavaş ikiye böldü"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden keki çok yavaş ikiye böldü.»
   - Açıklama: Güvenli özellik kullanımı sakarlığı düşürmek ya da karıştırmak olarak ister; burada sakarlık dikkatli ve yavaş davranışa dönüşmüş, işe yaramıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmeli; burada yalnız gerekçe olarak anılıyor ve işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0034` birebir aynı, `@degisim: güvenmek -> bölmek` (tutuyorsan), ardından `@onarim: 1dc517af1c8ab28b3d9515fed7058fa0d96493d3`, sonra gövde.

### Hikâye 3: tohum keloglan-0040 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0040
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mermer', fiil 'savurmak', sıfat 'süslü'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: ikisi de ipi aynı anda çekti | sırayla oynamayı söyledi ve önce arkadaşına verdi
@tohum: keloglan-0040
@degisim: mermer -> taş
Keloğlan ile Balkız şatonun bahçesinde taş bir yolda oynuyordu. Ellerinde tek bir süslü topaç vardı. İkisi de ipi aynı anda çekti ve ip karmakarışık oldu. "Balkız, sırayla oynayalım, önce sen çevir," dedi Keloğlan. Keloğlan ipi çözdü ve topacı Balkız'a verdi. Balkız ipi sardı ve topacı yere savurdu. Topaç taşın üstünde uzun uzun döndü. Sıra Keloğlan'a geldi. Keloğlan sakar olduğu için ipi yavaş yavaş ve sıkıca sardı. Sonra topacı yere attı. Topaç da güzelce döndü. İkisi de güldü. "Sırayla oynamak çok eğlenceli, Balkız!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan sakar olduğu için ipi yavaş yavaş"
   - Cümle 9: «Keloğlan sakar olduğu için ipi yavaş yavaş ve sıkıca sardı.»
   - Açıklama: Karttaki sakarlık özelliği bir şeyi düşürmek ya da karıştırmak olarak değil, dikkatli sarmanın gerekçesi olarak kullanılıyor ve işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan sakar olduğu için ipi yavaş"
   - Cümle 9: «Keloğlan sakar olduğu için ipi yavaş yavaş ve sıkıca sardı.»
   - Açıklama: Tohumdaki sakarlık kartın güvenli kullanım satırındaki gibi düşürme ya da karıştırma olarak gösterilmiyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0040` birebir aynı, `@degisim: mermer -> taş` (tutuyorsan), ardından `@onarim: 2c8221a60e8d4723cf2b97539eb6822f0b7546d8`, sonra gövde.

### Hikâye 4: tohum keloglan-0042 (deneme 4 -> 5)

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
Keloğlan tepede resim yapma oyunu oynuyordu. Bilgecan Dede de yanına oturmuş, onu izliyordu. Keloğlan kağıttaki tepeyi boyamak istedi ama yeşil boyası bitmişti. Elinde yalnız sarı ile mavi boya vardı. "Dede, yeşil boyam bitti, ne yapayım?" diye sordu Keloğlan. "Sarı ile maviyi karıştır, yeşil olur," dedi Bilgecan Dede. Keloğlan sakar olduğu için boya kabını iki eliyle tuttu. Sarı boyayı yavaşça mavi boyanın içine döktü. Sonra fırçasıyla iki rengi karıştırdı. Mavi renk yeşile döndü. Keloğlan resimdeki tepeyi yemyeşil boyadı. Bilgecan Dede resmi görünce ellerini çırptı. Keloğlan da mutlu mutlu yeni bir resme başladı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan sakar olduğu için boya kabını"
   - Cümle 7: «Keloğlan sakar olduğu için boya kabını iki eliyle tuttu.»
   - Açıklama: Kartın güvenli özellik kullanımı sakarlığı bir şeyi düşürmek ya da karıştırmak olarak gösterir; burada sakarlık yalnız etiket olarak geçiyor ve çözüme katkısı yok.
   - Açıklama: Tohumdaki sakarlık kartın güvenli kullanım satırındaki gibi bir şeyi düşürmek ya da karıştırmak olarak gösterilmiyor ve sorunun çözümüne katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0042` birebir aynı, `@degisim: yağmurluk -> fırça` (tutuyorsan), ardından `@onarim: 2ef479698a5212ed8701492ee36444762ed01203`, sonra gövde.

### Hikâye 5: tohum keloglan-0045 (deneme 4 -> 5)

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
Ormanda Bilgecan Dede kuşlar için tahta bir ev boyuyordu. Keloğlan ona çantasında iki kap kırmızı boya getirmişti. Ama Keloğlan biraz sakardı, bir kabı düşürdü ve boya yere döküldü. Bilgecan Dede sesi duydu ve arkasına döndü. Keloğlan yerdeki kırmızı lekeye baktı ve başını eğdi. "Özür dilerim, dede, boyayı ben düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan," dedi Bilgecan Dede ve gülümsedi. Keloğlan çantasından ikinci kabı çıkardı ve onu iki eliyle sıkıca tuttu. İkisi evi birlikte boyadı ve bitirdi. Keloğlan çok sevindi, çünkü dede ona kızmamıştı ve kuşların evi hazırdı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "boyayı ben düşürdüm"
   - Cümle 6: «"Özür dilerim, dede, boyayı ben düşürdüm," dedi Keloğlan.»
   - Açıklama: Düşen boya değil kaptır; boya dökülmüştür, 'kabı düşürdüm' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0045` birebir aynı, `@degisim: hazırlıklı -> kırmızı` (tutuyorsan), ardından `@onarim: fa5067f4f00ca22290b5ba7d0b82cab896755f55`, sonra gövde.

### Hikâye 6: tohum keloglan-0048 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0048
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'gölge', fiil 'alışmak', sıfat 'plastik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: eşek acıktı ama tepedeki otlar kuruydu | kayanın gölgesinde taze ot bulup eşeği çağırdı
@tohum: keloglan-0048
@degisim: plastik -> taze
Tepede sıcak bir rüzgar esiyordu. Keloğlan ile eşeği Karakaçan yavaşça yürüyordu. Karakaçan çok acıkmıştı ama buradaki otlar kuruydu. Eşek durdu ve yüksek sesle anırdı. Karakaçan yeşil otlara alışmıştı ve sarı otları yemedi. "Üzülme, sana taze ot bulacağım," dedi Keloğlan. Taşların arasına baktı ama hiç yeşil ot göremedi. "Karakaçan, burada yeşil ot yok," dedi Keloğlan dürüst bir sesle. Sonra büyük bir kayanın gölgesine baktı. Gölgede taze ve yeşil otlar vardı. Keloğlan ıslık çaldı ve Karakaçan hemen yanına geldi. Eşek otları yedi ve başını salladı. Karakaçan ile Keloğlan serin gölgede mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedi Keloğlan dürüst bir sesle"
   - Cümle 8: «"Karakaçan, burada yeşil ot yok," dedi Keloğlan dürüst bir sesle.»
   - Açıklama: Ses dürüst olmaz; özellik kelimesi öznesine uymayan biçimde kullanılmış.
   - Açıklama: 'Dürüst' ses için kullanılmaz; özellik kelimesi yanlış yerde kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Keloğlan dürüst bir sesle"
   - Cümle 8: «"Karakaçan, burada yeşil ot yok," dedi Keloğlan dürüst bir sesle.»
   - Açıklama: Tohum özelliği dürüstlük yalnız bir konuşma etiketi olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız bir sıfat olarak eklenmiş, sorunun çözümüne işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0048` birebir aynı, `@degisim: plastik -> taze` (tutuyorsan), ardından `@onarim: 5591fc20ae1fc67381a96de261aaf3a760b29ec1`, sonra gövde.

### Hikâye 7: tohum keloglan-0049 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0049
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'balon', fiil 'şişirmek', sıfat 'elmalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: kırmızı balon çok sert olduğu için büyümedi | balonu önce çekip yumuşattı sonra şişirdi
@tohum: keloglan-0049
@degisim: elmalı -> kırmızı
Ormanda kuşlar neşeyle ötüyordu. Keloğlan ile Balkız ağaçların altında balon dükkanı oyunu oynuyordu. Balkız kırmızı bir balon istedi ama balon çok sertti ve hiç büyümüyordu. Keloğlan balonu tek eliyle çekip yumuşatmak istedi. Ama biraz sakardı ve balon tek elinden kayıp düştü. Keloğlan bu kez balonu iki eliyle tuttu ve birkaç kez çekip gerdi. Balon biraz yumuşadı. Sonra Keloğlan derin bir nefes aldı ve balonu şişirdi. Kırmızı balon yavaş yavaş büyüdü. "İşte kırmızı balonun, Balkız!" dedi Keloğlan. Balkız balonu aldı ve sevinçle güldü. Sonra ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Balkız kırmızı bir balon istedi"
   - Cümle 3: «Balkız kırmızı bir balon istedi ama balon çok sertti ve hiç büyümüyordu.»
   - Açıklama: Şişirilen lastik balon masal köyü dünyasına ait olmayan çağdaş bir eşyadır; kartın tohum_yasak_kategoriler (çağdaş) alanı ve kapalı dünya ilkesine aykırı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "balon tek elinden kayıp düştü"
   - Cümle 5: «Ama biraz sakardı ve balon tek elinden kayıp düştü.»
   - Açıklama: Çözüm başarısız bir deneme, çekip germe ve şişirme ile ikiden fazla adım sürüyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "derin bir nefes aldı ve balonu şişirdi"
   - Cümle 8: «Sonra Keloğlan derin bir nefes aldı ve balonu şişirdi.»
   - Açıklama: Küçük çocukların taklit edebileceği biçimde ağızla balon şişirme gösteriliyor ve balon boğulma tehlikesi taşır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0049` birebir aynı, `@degisim: elmalı -> kırmızı` (tutuyorsan), ardından `@onarim: b98bc4a7518cfefb24879e15044e98edc7d4c6e4`, sonra gövde.

### Hikâye 8: tohum keloglan-0053 (deneme 3 -> 4)

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
Bir sabah ormanda serin bir rüzgar esiyordu. Keloğlan ile eşeği Karakaçan ağaçların altında top oynuyordu. Parlak topu sırayla büyük bir ağaca doğru itiyorlardı. Ama Karakaçan sırasını bekleyemedi ve topu hep kendisi itti. Keloğlan Karakaçan'ın başını okşadı. "Karakaçan, bir sen, bir ben oynayalım," dedi Keloğlan. Karakaçan başını salladı. Keloğlan topa ayağıyla vurdu. Sonra yanlışlıkla topa yine vurdu. "İki kez vurdum, sen de iki kez it," dedi dürüst Keloğlan. Karakaçan topu burnuyla iki kez itti ve top ağaca değdi. Keloğlan çok mutluydu, çünkü sırayla oynamak yine eğlenceli olmuştu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Karakaçan sırasını bekleyemedi"
   - Cümle 4: «Ama Karakaçan sırasını bekleyemedi ve topu hep kendisi itti.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sonra yanlışlıkla topa yine vurdu"
   - Cümle 9: «Sonra yanlışlıkla topa yine vurdu.»
   - Açıklama: Keloğlan'ın kendisinin sırayı bozması ikinci bir sorun ekliyor.
   - Açıklama: Sıra sorunu çözüldükten sonra Keloğlan'ın iki kez vurmasıyla ikinci bir sorun açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0053` birebir aynı, `@degisim: dolma -> top` (tutuyorsan), ardından `@onarim: a2b74db340392f28259e613c9547ccfe6d636bd7`, sonra gövde.

### Hikâye 9: tohum keloglan-0057 (deneme 3 -> 4)

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
Rüzgar esiyordu ve tepede tuhaf bir ses duyuluyordu. Keloğlan tozlu bir taşa oturmuş, kalemiyle resim çiziyordu. Bu sesi çok merak etti. Keloğlan önce bu sesi yanında otlayan eşeği Karakaçan'ın sesiyle karıştırdı. "Karakaçan, bunu sen mi yapıyorsun?" diye sordu Keloğlan. Karakaçan başını iki yana salladı. Keloğlan sesin peşinden kayaların arasına yürüdü. Bir kayanın dibinde küçük bir delik gördü. Keloğlan biraz sakardı ve kalemini deliğin üstüne düşürdü. Kalem deliği kapattı ve ses hemen kesildi. Keloğlan kalemi aldı ve ses yeniden başladı. Rüzgar bu delikten geçerken ıslık gibi bir ses çıkarıyordu. "Buldum, Karakaçan, sesi bu küçük delik yapıyormuş!" dedi Keloğlan sevinçle.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalemini deliğin üstüne düşürdü"
   - Cümle 9: «Keloğlan biraz sakardı ve kalemini deliğin üstüne düşürdü.»
   - Açıklama: Sesin kaynağını doğrulayan olay figürün eylemiyle değil, tesadüfi bir sakarlıkla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0057` birebir aynı, `@degisim: bindirmek -> karıştırmak` (tutuyorsan), ardından `@onarim: c70bb0f774d04df61c3dc20dbcb4b946a955e278`, sonra gövde.

### Hikâye 10: tohum keloglan-0058 (deneme 3 -> 4)

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
@plan: ikisi ipi aynı anda çekti ve topaç devrildi | sırayla oynamayı önerdi ve ipi düzgünce sardı
@tohum: keloglan-0058
@degisim: atkı -> topaç
Keloğlan ile Bilgecan Dede evde tahta bir topaçla oynuyordu. Topacın yalnız bir ipi vardı. İkisi de ipi aynı anda çekti ve topaç devrildi. "Sırayla oynayalım, önce sen çevir, dede," dedi Keloğlan. Dede ipi çekince topaç masada uzun uzun döndü. "Dede, topacı ne güzel çevirdin, sen çok yeteneklisin!" dedi Keloğlan. Sonra sıra Keloğlan'a geldi. Keloğlan biraz sakardı ve ipi karıştırdı. Sonra ipi açtı ve bu kez yavaşça, düzgünce sardı. Keloğlan ipi çekince topaç da dedeninki kadar uzun döndü. İkisi bu güzel dönüşü el çırparak kutladı. Keloğlan çok sevindi, çünkü sırayla oynamak ikisini de mutlu etmişti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sen çok yeteneklisin"
   - Cümle 6: «"Dede, topacı ne güzel çevirdin, sen çok yeteneklisin!" dedi Keloğlan.»
   - Açıklama: 'Yetenekli' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "biraz sakardı ve ipi karıştırdı"
   - Cümle 8: «Keloğlan biraz sakardı ve ipi karıştırdı.»
   - Açıklama: İp 'karıştırılmaz', 'dolaştırılır'; fiil anlamca yanlış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve ipi karıştırdı"
   - Cümle 8: «Keloğlan biraz sakardı ve ipi karıştırdı.»
   - Açıklama: İp karıştırılmaz, dolaşır; doğrusu 'ipi dolaştırdı' olmalı.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keloğlan biraz sakardı ve ipi karıştırdı"
   - Cümle 8: «Keloğlan biraz sakardı ve ipi karıştırdı.»
   - Açıklama: Topacın devrilmesi sorunundan sonra ipin karışması ikinci bir sorun olarak geliyor.
   - Açıklama: Sıra sorunu çözüldükten sonra ipin karışması ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0058` birebir aynı, `@degisim: atkı -> topaç` (tutuyorsan), ardından `@onarim: 470e54b0707e69e71368f496e3c155c4d3c47129`, sonra gövde.

### Hikâye 11: tohum keloglan-0061 (deneme 3 -> 4)

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
Keloğlan evde davul çalmak istedi. Anasına sormadan mutfaktan parıldayan büyük tencereyi aldı. Tencereyi ters çevirdi ve kaşıkla davul gibi çaldı. Tam o sırada anası mutfağa girdi. "Keloğlan, tencerem nerede? Çorba pişirecektim," dedi anası. Keloğlan tencereyi hemen anasına geri verdi. "Sormadan aldım, özür dilerim, anneciğim," dedi Keloğlan saygılı bir sesle. Anası gülümsedi ve onu kucakladı. "Davul çalmayı öğrenmek istiyorum, eski kovayı alabilir miyim?" diye sordu Keloğlan. Anası başını salladı ve kovayı ona verdi. Anası çorbayı pişirirken Keloğlan kovaya kaşıkla vurdu. İkisi mutfakta mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Keloğlan saygılı bir sesle"
   - Cümle 8: «"Sormadan aldım, özür dilerim, anneciğim," dedi Keloğlan saygılı bir sesle.»
   - Açıklama: 'Saygılı bir ses' soyut bir nitelik; 3 yaşındaki çocuk için anlaşılmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0061` birebir aynı, ardından `@onarim: 61eec375185fffebbf5d16749751955846d57419`, sonra gövde.

### Hikâye 12: tohum keloglan-0063 (deneme 3 -> 4)

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
Rüzgar tepede hafif hafif esiyordu. Keloğlan beyaz kağıttan topunu eşeği Karakaçan'ın sırtındaki sepete atmak istiyordu. Ama rüzgar kağıt topu her seferinde sepetten uzağa itti. Bir kez top sepetin kenarına çarptı ve yere sıçradı. Keloğlan topu yerden aldı. Onu elle sepete koymadı, çünkü dürüst bir çocuktu. "Top içeri girmedi, bir daha atacağım," dedi Keloğlan. Sonra rüzgarın durmasını bekledi. Rüzgar durunca topu yavaşça attı. Kağıt top sepetin içine düştü. Karakaçan başını salladı ve neşeyle anırdı. Keloğlan çok sevindi, çünkü kağıt topu sonunda sepete sokmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çünkü dürüst bir çocuktu"
   - Cümle 6: «Onu elle sepete koymadı, çünkü dürüst bir çocuktu.»
   - Açıklama: Topu elle sepete koymama ayrıntısı olayı ilerletmiyor, yalnız özelliği göstermek için ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0063` birebir aynı, `@degisim: kilitli -> beyaz` (tutuyorsan), ardından `@onarim: eeda30bdb4b17d92d406d56b327402301242de55`, sonra gövde.
