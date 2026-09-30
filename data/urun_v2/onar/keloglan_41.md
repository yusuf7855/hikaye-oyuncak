# Editör görevi (onarım): Keloğlan, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar41.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0136 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0136
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'beşik', fiil 'sormak', sıfat 'lezzetli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: elma sepetinin ipi sıkı bir düğüm olmuştu | düğümün ucunu bulup yavaşça çekti
@tohum: keloglan-0136
@degisim: beşik -> sepet
Tepede serin bir rüzgar esiyordu. Keloğlan, eşeği Karakaçan'a bir sürpriz hazırlamıştı. Sepette lezzetli elmalar vardı, ama kapağın ipi sıkı bir düğüm olmuştu. Keloğlan elmalar düşmesin diye ipi çok iyi bağlamıştı. "Karakaçan, sürprizini görmek ister misin?" diye sordu Keloğlan. Eşek başını salladı. Keloğlan düğümün ucunu buldu ve yavaşça çekti. Düğüm çözüldü ve kapak açıldı. Ama Keloğlan biraz sakardı ve sepeti devirdi. Kırmızı elmalar çimenlere yuvarlandı. Karakaçan hemen bir elma yedi ve kulaklarını oynattı. Keloğlan güldü ve eşeğinin başını okşadı. "Afiyet olsun, Karakaçan, bu elmalar senin için!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama Keloğlan biraz sakardı ve sepeti devirdi"
   - Cümle 9: «Ama Keloğlan biraz sakardı ve sepeti devirdi.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunu çözmekte işe yaramıyor, çözümden sonra süs olarak ekleniyor.
   - Açıklama: Tohumdaki sakarlık sorun çözüldükten sonra süs olarak geçiyor, işe yaramıyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keloğlan biraz sakardı ve sepeti devirdi"
   - Cümle 9: «Ama Keloğlan biraz sakardı ve sepeti devirdi.»
   - Açıklama: Düğüm çözüldükten sonra sepetin devrilmesiyle ikinci bir sorun başlıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve sepeti devirdi"
   - Cümle 9: «Ama Keloğlan biraz sakardı ve sepeti devirdi.»
   - Açıklama: Sorun çözüldükten sonra sepetin devrilmesi önceki olaydan çıkmayan sebepsiz yeni bir olay.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama Keloğlan biraz sakardı ve sepeti devirdi"
   - Cümle 9: «Ama Keloğlan biraz sakardı ve sepeti devirdi.»
   - Açıklama: Sepetin devrilmesi düğüm sorunundan çıkmıyor ve çözüme bir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0136` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: 8dc032426fe930d5b79196b02bd38fa62bb37f62`, sonra gövde.

### Hikâye 2: tohum keloglan-0137 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0137
- yer: dağ (Köyün yakınındaki tepe.)
- tema: bir şey yapmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'takvim', fiil 'anlatmak', sıfat 'büyük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: uçurtma kuyruğu olmadığı için düşüyordu | düşen kurdeleyi uçurtmaya kuyruk olarak bağladı
@tohum: keloglan-0137
@degisim: takvim -> kurdele
Tepede güçlü bir rüzgar esiyordu. Keloğlan ile Balkız büyük bir uçurtma yapmıştı. Ama uçurtma kuyruğu olmadığı için havada dönüyor ve yere düşüyordu. Keloğlan süs için getirdikleri uzun kurdeleyi eline aldı. Sakar Keloğlan kurdeleyi elinden yere düşürdü. Yerdeki kurdele bir kuyruk gibi duruyordu. "Balkız, bu kurdele uçurtmaya kuyruk olur," diye anlattı Keloğlan. Sonra kurdeleyi uçurtmanın ucuna sıkıca bağladı. Balkız ipi tuttu ve Keloğlan uçurtmayı havaya bıraktı. Uçurtma bu kez dönmedi ve dümdüz yükseldi. "Ne güzel uçuyor, Balkız, onu birlikte yaptık!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan kurdeleyi elinden yere düşürdü"
   - Cümle 5: «Sakar Keloğlan kurdeleyi elinden yere düşürdü.»
   - Açıklama: Çözüm fikri Keloğlan'ın düşünmesinden değil, kurdeleyi rastlantıyla düşürmesinden sebepsizce geliyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kuyruk olur," diye anlattı Keloğlan"
   - Cümle 7: «"Balkız, bu kurdele uçurtmaya kuyruk olur," diye anlattı Keloğlan.»
   - Açıklama: Kısa bir öneri için 'anlattı' yanlış fiil; 'dedi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0137` birebir aynı, `@degisim: takvim -> kurdele` (tutuyorsan), ardından `@onarim: 5863d12f835d959d9ed7bb2a17c6c3790ff2a225`, sonra gövde.

### Hikâye 3: tohum keloglan-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0138
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'tutkal', fiil 'dinlemek', sıfat 'harika'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: tutkal masadan düşüp kaybolmuştu | dolabın altına elma yuvarladı, sesi dinledi ve tutkalı buldu
@tohum: keloglan-0138
Evde her yer sessizdi. Keloğlan anasının kırık tahta kaşığını tutkalla yapıştırmak istedi. Ama tutkal masadan düşmüş ve kaybolmuştu. "Anneciğim, tutkalı gördün mü?" diye sordu Keloğlan. "Görmedim, belki yere düştü," dedi anası. Sakar Keloğlan etrafa bakarken elma sepetini düşürdü. Elmalar yere döküldü ve yuvarlandı. Keloğlan elmalara bakınca tutkalın da yuvarlanmış olabileceğini düşündü. Bir elmayı dolabın altına yuvarladı ve dikkatle dinledi. Elma bir şeye çarptı ve küçük bir ses geldi. Keloğlan tutkalı dolabın altından çıkardı ve kaşığı yapıştırdı. "Harika olmuş, Keloğlan!" dedi anası. Sonra Keloğlan ile anası elmaları gülerek birlikte topladı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sakar Keloğlan etrafa bakarken"
   - Cümle 6: «Sakar Keloğlan etrafa bakarken elma sepetini düşürdü.»
   - Açıklama: Zaten tanıtılmış Keloğlan sıfatla yeniden tanıtılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan etrafa bakarken elma sepetini düşürdü"
   - Cümle 6: «Sakar Keloğlan etrafa bakarken elma sepetini düşürdü.»
   - Açıklama: Çözümü getiren elma sepeti kazayla sebepsizce devreye giriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "etrafa bakarken elma sepetini düşürdü"
   - Cümle 6: «Sakar Keloğlan etrafa bakarken elma sepetini düşürdü.»
   - Açıklama: Çözümü getiren fikir, sebepsiz bir sepet düşürme kazasından doğuyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bir elmayı dolabın altına yuvarladı ve dikkatle dinledi"
   - Cümle 9: «Bir elmayı dolabın altına yuvarladı ve dikkatle dinledi.»
   - Açıklama: Dolabın altına bakmak yerine elma yuvarlayıp ses dinlemek sebebe doğrudan yönelmeyen dolambaçlı bir çözüm.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bir elmayı dolabın altına yuvarladı"
   - Cümle 9: «Bir elmayı dolabın altına yuvarladı ve dikkatle dinledi.»
   - Açıklama: Tutkalı bulmak için dolabın altına bakmak yerine elma yuvarlayıp ses dinlemek dolaylı ve zorlama bir çözüm.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0138` birebir aynı, ardından `@onarim: 4e8e9f4645ba53fdc9eb6814ff359cf5b5ef7f32`, sonra gövde.

### Hikâye 4: tohum keloglan-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0139
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yastık', fiil 'tamamlanmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: yağmurda kulübenin çatısı bitmemişti | düşürdüğü dalları görüp çatıdaki boşluğa dizdi
@tohum: keloglan-0139
@degisim: yastık -> dal
Yağmur yavaş yavaş yağmaya başladı. Keloğlan ile Balkız ormanda dallardan küçük bir kulübe yapıyordu. Ama kulübenin çatısı bitmemişti ve içeri yağmur damlıyordu. "Keloğlan, çabuk, biraz daha dal getir!" dedi Balkız. Keloğlan kucağına kocaman bir yığın dal aldı. Kulübenin yanında sakar Keloğlan dalları elinden düşürdü. Dallar yere yan yana düştü ve küçük bir çatı gibi durdu. Keloğlan onları aynı biçimde çatıdaki boşluğa dizdi. Böylece çatı tamamlandı. İçeri artık hiç su girmedi. Dışarıda otlar sırılsıklam oldu, ama ikisi hiç ıslanmadı. "Teşekkürler, Keloğlan, kulübemiz bitti!" dedi Balkız. Keloğlan çok sevindi, çünkü yaptıkları kulübe ikisini de yağmurdan korumuştu.
```

**Hakem bulguları (3):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "biraz daha dal getir"
   - Cümle 4: «"Keloğlan, çabuk, biraz daha dal getir!" dedi Balkız.»
   - Açıklama: Çözüm fikrini (daha dal getirmek) yan karakter Balkız veriyor, Keloğlan yalnız uyguluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sakar Keloğlan dalları elinden düşürdü"
   - Cümle 6: «Kulübenin yanında sakar Keloğlan dalları elinden düşürdü.»
   - Açıklama: Çatının biçimi dalların tesadüfen düşmesiyle sebepsizce ortaya çıkıyor; çözüm şansa dayanıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dallar yere yan yana düştü ve küçük bir çatı gibi durdu"
   - Cümle 7: «Dallar yere yan yana düştü ve küçük bir çatı gibi durdu.»
   - Açıklama: Çözüm, sakarlıkla düşen dalların tesadüfen çatı biçimi almasıyla sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0139` birebir aynı, `@degisim: yastık -> dal` (tutuyorsan), ardından `@onarim: d9aeead69e5e96636686d3889602ba28ce62b417`, sonra gövde.

### Hikâye 5: tohum keloglan-0140 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0140
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'simit', fiil 'gezdirmek', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: simit arabada dik durduğu için düşüp yuvarlanıyordu | simidi arabaya yan yatırdı ve simit düşmedi
@tohum: keloglan-0140
Keloğlan ormanda komik bir oyun oynuyordu. Basit bir tahta arabayla bir simit gezdiriyordu. Ama simit arabada dik duruyordu ve her taşta düşüp yuvarlanıyordu. Keloğlan simidi yakalamak için koştu ve güldü. Simidi arabaya geri koydu, ama simit yine kaçtı. Sonra durdu ve dikkatle baktı. Bu kez simidi arabanın içine yan yatırdı. Araba taşların üstünden geçti, ama simit hiç kıpırdamadı. Keloğlan böylece yeni bir şey öğrendi. Keloğlan çok sevindi, çünkü oyununa artık rahatça devam edebiliyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama simit yine kaçtı"
   - Cümle 5: «Simidi arabaya geri koydu, ama simit yine kaçtı.»
   - Açıklama: Simit kaçmaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0140` birebir aynı, ardından `@onarim: 8a41cae4fe51b10a773474ab0fa5d4f2f75be012`, sonra gövde.

### Hikâye 6: tohum keloglan-0143 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0143
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kavun', fiil 'asılmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kelebeklere yaklaşınca onlar hep uçup gidiyordu | tatlı kavunu yere koyup kıpırdamadan bekledi
@tohum: keloglan-0143
@degisim: cömert -> tatlı
Güneş ormanda sıcacık parlıyordu. Keloğlan bir ağacın altında renkli kelebekler gördü. Onlara yakından bakmak istedi, ama o yaklaşınca kelebekler hep uçtu. Keloğlan'ın kavunu serin kalsın diye bir torbada dala asılmıştı. Kelebekler tatlı kokuyu çok severdi. Torbayı daldan indirdi ve kavunu açmak istedi. Ama sakar Keloğlan kavunu elinden düşürdü. Kavun otların üstünde ikiye ayrıldı ve kokusu yayıldı. Keloğlan yarım kavunun yanına oturdu ve hiç kıpırdamadı. Biraz sonra kavunun üstünde kelebekler vardı. Onlara yakından baktı. Sonra kavunun öbür yarısını yedi ve kelebekleri mutlu mutlu izledi.
```

**Hakem bulguları (8):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "tatlı kavunu yere koyup kıpırdamadan bekledi"
   - Cümle 0 (plan satırı): «kelebeklere yaklaşınca onlar hep uçup gidiyordu | tatlı kavunu yere koyup kıpırdamadan bekledi»
   - Açıklama: Gövdede Keloğlan kavunu yere koymuyor, kavun elinden düşüp ikiye ayrılıyor.
   - Açıklama: Gövdede kavun yere konmuyor, elden düşüp ikiye ayrılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan'ın kavunu serin kalsın diye"
   - Cümle 4: «Keloğlan'ın kavunu serin kalsın diye bir torbada dala asılmıştı.»
   - Açıklama: Kavun sebepsiz beliriyor ve çözüm kavunun kazayla düşmesiyle şans eseri geliyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Torbayı daldan indirdi ve"
   - Cümle 6: «Torbayı daldan indirdi ve kavunu açmak istedi.»
   - Açıklama: Önceki cümlenin öznesi kelebekler olduğu için torbayı kimin indirdiği belirsiz.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Torbayı daldan indirdi"
   - Cümle 6: «Torbayı daldan indirdi ve kavunu açmak istedi.»
   - Açıklama: Önceki cümlenin öznesi kelebekler olduğu için torbayı kimin indirdiği belli değil.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "sakar Keloğlan kavunu elinden düşürdü"
   - Cümle 7: «Ama sakar Keloğlan kavunu elinden düşürdü.»
   - Açıklama: Sorunu Keloğlan'ın bilinçli çözümü değil kavunun kazayla düşüp açılması çözüyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sakar Keloğlan kavunu elinden düşürdü"
   - Cümle 7: «Ama sakar Keloğlan kavunu elinden düşürdü.»
   - Açıklama: Kelebekleri çeken kavun kokusu figürün kararıyla değil bir kazayla, sebepsizce ortaya çıkıyor.
7. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "kavunun üstünde kelebekler vardı"
   - Cümle 10: «Biraz sonra kavunun üstünde kelebekler vardı.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün parçası olarak olaya katılıyor.
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, çözümün parçası olarak olaya katılıyor.
8. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onlara yakından baktı."
   - Cümle 11: «Onlara yakından baktı.»
   - Açıklama: Önceki cümlenin öznesi kelebekler; bakan kişi belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0143` birebir aynı, `@degisim: cömert -> tatlı` (tutuyorsan), ardından `@onarim: 730f04dbcfbb444fa8e9703c4038f0ac156bb434`, sonra gövde.

### Hikâye 7: tohum keloglan-0145 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0145
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sis', fiil 'koşmak', sıfat 'tertemiz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: dağa sis indi ve koşma oyununda kaya görünmez oldu | adımlarını sayarak yürüdü ve kayayı sisin içinde buldu
@tohum: keloglan-0145
Dağda Keloğlan büyük bir ağaçtan gri bir kayaya koşuyordu. Oyundan önce yürüyüp adımlarını saymış ve kayanın yirmi adım uzakta olduğunu öğrenmişti. Ama birden tepeye beyaz bir sis indi ve kaya görünmez oldu. Keloğlan ağacın yanında durdu. Ağaçla kaya arasında yalnız düz, yumuşak çimenler vardı. Bu kez koşmadı, yavaş yavaş yürüdü. Bir, iki, üç diye adımlarını tek tek saydı. Yirmi adım sonra eli soğuk kayaya değdi. Keloğlan sevinçle zıpladı ve kayaya sarıldı. Biraz sonra rüzgar esti ve sis dağıldı. Hava yine tertemiz oldu ve oyun devam etti. Keloğlan çok mutluydu, çünkü kayayı sisin içinde bile bulmuştu.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Keloğlan ağacın yanında durdu"
   - Cümle 4: «Keloğlan ağacın yanında durdu.»
   - Açıklama: Keloğlan ağaçtan kayaya koşarken birden ağacın yanında duruyor; konumu çelişiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bu kez koşmadı, yavaş yavaş yürüdü"
   - Cümle 6: «Bu kez koşmadı, yavaş yavaş yürüdü.»
   - Açıklama: Dağda tek başına olan çocuk sis inince durup beklemek yerine sisin içinde yürüyor; bu taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0145` birebir aynı, ardından `@onarim: 0967898e8307e53c84feed1072fff821edaa1d3b`, sonra gövde.

### Hikâye 8: tohum keloglan-0146 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0146
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'ay', fiil 'tatmak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yakından şırıl şırıl bir ses geliyordu ama su görünmüyordu | bisküviyi düşürdü ve yaprakların altında ince bir su buldu
@tohum: keloglan-0146
Serin bir rüzgar esiyordu ve gökyüzünde soluk bir ay vardı. Keloğlan ile Bilgecan Dede ormanda bir ağacın altında oturuyordu. Birden yakından şırıl şırıl bir ses geldi ama hiç su görünmüyordu. Keloğlan bu sesi çok merak etti. "Dede, bu ses nereden geliyor?" diye sordu Keloğlan. "Bul bakalım," dedi Bilgecan Dede ve ona tuzlu bir bisküvi uzattı. Keloğlan bisküviyi tatmak için ağzına götürdü. Ama Keloğlan biraz sakardı ve bisküvi elinden yaprakların arasına düştü. Keloğlan bisküviyi almak için yaprakları kaldırdı. Yaprakların altında ince bir su akıyordu! "Ses buradan geliyormuş!" dedi Keloğlan. Dede gülümsedi. Sonra Keloğlan ile dede suyun sesini mutlu mutlu dinledi.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ona tuzlu bir bisküvi uzattı"
   - Cümle 6: «"Bul bakalım," dedi Bilgecan Dede ve ona tuzlu bir bisküvi uzattı.»
   - Açıklama: Bisküvi sebepsiz beliriyor ve çözümü rastlantıyla getiriyor.
   - Açıklama: Bisküvi sebepsiz beliriyor ve çözümü yalnız rastlantıyla getiriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 8: «Ama Keloğlan biraz sakardı ve bisküvi elinden yaprakların arasına düştü.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "bisküvi elinden yaprakların arasına düştü"
   - Cümle 8: «Ama Keloğlan biraz sakardı ve bisküvi elinden yaprakların arasına düştü.»
   - Açıklama: Suyu Keloğlan aramıyor, bisküvinin kazara düşmesiyle rastlantı sonucu buluyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bisküvi elinden yaprakların arasına düştü"
   - Cümle 8: «Ama Keloğlan biraz sakardı ve bisküvi elinden yaprakların arasına düştü.»
   - Açıklama: Su tesadüfen, düşen bisküviyi alırken bulunuyor; çözüm sesin kaynağını aramaya yönelmiyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bisküviyi almak için yaprakları kaldırdı"
   - Cümle 9: «Keloğlan bisküviyi almak için yaprakları kaldırdı.»
   - Açıklama: Çözüm sesin kaynağını aramaya yönelmiyor, düşen bisküviyi almaya yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0146` birebir aynı, ardından `@onarim: 56e5841f39eabc0be61256732b0f2405d69d887f`, sonra gövde.

### Hikâye 9: tohum keloglan-0149 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0149
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'şal', fiil 'şekillendirmek', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: gölgesini kocaman yapmak istedi ama gölgesi küçüktü | elini açınca gölgesi büyüdü ve şalı iki yana açtı
@tohum: keloglan-0149
Ormanda ağaçların arasından güneş vuruyordu. Keloğlan omzunda bir şalla yürürken yerde gizemli bir şekil gördü. Bu kendi gölgesiydi ama büyük ağacın gölgesine göre çok küçüktü. Keloğlan gölgesini de kocaman yapmak istedi. Elini yavaşça açtı ve yerdeki gölge de büyüdü. Böylece açık elin büyük gölge yaptığını öğrendi. Hemen şalın iki ucunu tuttu ve kollarını iki yana açtı. Şal, gölgesini kocaman bir kanat gibi şekillendirdi. Keloğlan'ın gölgesi artık büyük ağacın gölgesi kadar genişti. Keloğlan kollarını salladı ve kocaman gölge de sallandı. Keloğlan yeni gölgesiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "gölgesi büyüdü ve şalı iki yana açtı"
   - Cümle 0 (plan satırı): «gölgesini kocaman yapmak istedi ama gölgesi küçüktü | elini açınca gölgesi büyüdü ve şalı iki yana açtı»
   - Açıklama: Plan satırında 'açtı' fiilinin öznesi 'gölgesi' gibi okunuyor; özne uyumu bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yerde gizemli bir şekil"
   - Cümle 2: «Keloğlan omzunda bir şalla yürürken yerde gizemli bir şekil gördü.»
   - Açıklama: 'gizemli' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelimedir, 3 yaşındaki çocuk bilmez.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Keloğlan gölgesini de kocaman yapmak istedi"
   - Cümle 4: «Keloğlan gölgesini de kocaman yapmak istedi.»
   - Açıklama: Gölgenin küçük olması gerçek bir sorun değil, önemsiz ve zorlama bir istek; üstelik şalla gölgenin büyük ağacın gölgesi kadar genişlemesi akla yatkın değil.
   - Açıklama: Gölgenin küçük olması gerçek bir sorun değil, sebepsiz bir istek.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gibi şekillendirdi"
   - Cümle 8: «Şal, gölgesini kocaman bir kanat gibi şekillendirdi.»
   - Açıklama: 'şekillendirdi' küçük çocuk için zor ve soyut bir fiil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gölgesini kocaman bir kanat gibi şekillendirdi"
   - Cümle 8: «Şal, gölgesini kocaman bir kanat gibi şekillendirdi.»
   - Açıklama: Benzetme ve 'şekillendirdi' küçük çocuk için soyut ve ağırdır.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "gölgesi artık büyük ağacın gölgesi kadar genişti"
   - Cümle 9: «Keloğlan'ın gölgesi artık büyük ağacın gölgesi kadar genişti.»
   - Açıklama: Bir çocuğun şalla yaptığı gölgenin büyük ağacın gölgesi kadar geniş olması akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0149` birebir aynı, ardından `@onarim: 7dce73691ff425644e7baa52af01e17c6bb175ef`, sonra gövde.

### Hikâye 10: tohum keloglan-0150 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0150
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'tüy', fiil 'havalanmak', sıfat 'yardımsever'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: eşek de oynamak istedi ama tüyü tutamıyordu | tüyü eşeğin burnuna uzatıp sırayla oynadılar
@tohum: keloglan-0150
@degisim: yardımsever -> beyaz
Evin önünde Keloğlan yerde beyaz bir tüy buldu. Tüyü avucuna koyup üfledi ve tüy havalandı. Eşeği Karakaçan da oynamak istedi, ama tüyü tutacak eli yoktu. Sakar Keloğlan tüyü yakalarken elinden düşürdü. Tüy yavaşça Karakaçan'ın burnunun önüne indi. Karakaçan burnundan hızla üfledi ve tüy yukarı uçtu. Keloğlan güldü ve tüyü eliyle eşeğin burnuna tuttu. Karakaçan bir daha üfledi ve tüy yine havalandı. Sonra sıra Keloğlan'a geldi. Keloğlan ile eşeği tüyle sırayla oynayarak çok eğlendi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan tüyü yakalarken elinden düşürdü"
   - Cümle 4: «Sakar Keloğlan tüyü yakalarken elinden düşürdü.»
   - Açıklama: Çözüm Keloğlan'ın düşüncesinden değil tesadüfi bir düşürmeden sebepsizce çıkıyor.
   - Açıklama: Çözüm Keloğlan'ın düşünmesinden değil tüyün kazayla eşeğin burnuna düşmesinden sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0150` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 94425d36632e61d5a74a8090d9b654fcf309420f`, sonra gövde.

### Hikâye 11: tohum keloglan-0151 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0151
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'turşu', fiil 'gizlenmek', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: turuncu top turşu kavanozunun arkasında kayboldu | kaşığı uzattı, kaşık düşüp topu dışarı itti
@tohum: keloglan-0151
@degisim: gizlenmek -> aramak
Evin mutfağında Keloğlan turuncu topuyla oynuyordu. Top zıpladı, yuvarlandı ve büyük turşu kavanozunun arkasına gitti. Keloğlan topunu orada aradı ama göremedi. Kavanoz çok ağırdı, Keloğlan onu kaldıramadı. Masadan uzun bir kaşık aldı ve onun arkasına uzattı. Ama biraz sakar olduğu için kaşığı elinden düşürdü. Kaşık topa çarptı ve top dışarı yuvarlandı. Keloğlan turuncu topunu hemen yakaladı. Sonra kaşığı da alıp masaya koydu. Keloğlan çok sevindi, çünkü kaybolan topunu sonunda bulmuştu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve onun arkasına uzattı"
   - Cümle 5: «Masadan uzun bir kaşık aldı ve onun arkasına uzattı.»
   - Açıklama: 'onun' zamirinin kavanozu mu masayı mı gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kaşığı elinden düşürdü"
   - Cümle 6: «Ama biraz sakar olduğu için kaşığı elinden düşürdü.»
   - Açıklama: Top Keloğlan'ın amaçlı bir eylemiyle değil, kaşığın tesadüfen düşmesiyle çıkıyor; çözüm sebepsizce geliyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kaşık topa çarptı ve top dışarı yuvarlandı"
   - Cümle 7: «Kaşık topa çarptı ve top dışarı yuvarlandı.»
   - Açıklama: Top, figürün sebebe yönelik eylemiyle değil kaşığın kazara düşmesiyle çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0151` birebir aynı, `@degisim: gizlenmek -> aramak` (tutuyorsan), ardından `@onarim: 8e542d28fe15012e8801d088360f44a06b391b59`, sonra gövde.

### Hikâye 12: tohum keloglan-0153 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0153
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'şemsiye', fiil 'ekmek', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: rüzgar esti ve iki tohum avucundan uçtu | şemsiyeyi açtı ve arkasında tohumları ekti
@tohum: keloglan-0153
Dağda Keloğlan bahçe oyunu oynuyordu. Yanına bir şemsiye almıştı, çünkü hava bulutluydu. Elinde ilginç, çizgili ayçiçeği tohumları vardı. Ama rüzgar esti ve iki tohum avucundan uçtu. Keloğlan öbür tohumları avucunda sıkıca tuttu. Keloğlan azimli ve dürüst bir çocuktu, oyununu bırakmadı ve şemsiyeyi açtı. Şemsiyeyi rüzgara karşı yere koydu. Şemsiyenin arkasında hiç rüzgar yoktu. Keloğlan toprağı parmağıyla kazdı ve tohumları tek tek ekti. Üstlerini toprakla örttü. Tohumlar artık uçmadı ve bahçe hazır oldu. Keloğlan bundan sonra rüzgarlı havada tohumlarını şemsiyenin arkasında ekti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "rüzgar esti ve iki tohum avucundan uçtu"
   - Cümle 4: «Ama rüzgar esti ve iki tohum avucundan uçtu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar esti ve iki tohum avucundan uçtu"
   - Cümle 4: «Ama rüzgar esti ve iki tohum avucundan uçtu.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "iki tohum avucundan uçtu"
   - Cümle 4: «Ama rüzgar esti ve iki tohum avucundan uçtu.»
   - Açıklama: Uçan iki tohuma bir daha dönülmüyor; asıl sorun çözülmeden hikaye kapanıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan azimli ve dürüst bir çocuktu"
   - Cümle 6: «Keloğlan azimli ve dürüst bir çocuktu, oyununu bırakmadı ve şemsiyeyi açtı.»
   - Açıklama: 'Azimli' ve olayla ilgisiz 'dürüst' soyut kelimelerdir, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0153` birebir aynı, ardından `@onarim: ae3be60a02977d5bd71002553b3b46b9a9217ed6`, sonra gövde.
