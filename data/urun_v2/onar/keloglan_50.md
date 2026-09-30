# Editör görevi (onarım): Keloğlan, onarım partisi 50

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar50.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar50.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0129 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0129
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kolye', fiil 'içmek', sıfat 'kokulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: dedenin kolyesini otların arasına düşürdü | özür diledi, otlara baktı ve kolyeyi buldu
@tohum: keloglan-0129
@degisim: içmek -> aramak
Rüzgar ormanda hafif hafif esiyordu. Bilgecan Dede, Keloğlan'a yeni yaptığı düdüklü bir kolyeyi gösterdi. Keloğlan sakar bir çocuktu ve kolyeyi kokulu otların arasına düşürdü. Otlar çok sıktı ve kolye hiç görünmüyordu. "Özür dilerim, Dede, kolyeni düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan, onu bulabiliriz," dedi Dede. Keloğlan eğildi ve otları yavaşça aradı. Sonunda otların arasında küçük düdüğü gördü. Onu dikkatle aldı ve iki eliyle Dede'ye verdi. Dede düdüğü çaldı ve ormanda ince bir ses çıktı. "Teşekkürler, Keloğlan, kolyemi sen buldun!" dedi Bilgecan Dede.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür diledi, otlara baktı ve kolyeyi buldu"
   - Cümle 0 (plan satırı): «dedenin kolyesini otların arasına düşürdü | özür diledi, otlara baktı ve kolyeyi buldu»
   - Açıklama: Plan özür dilemeyi söylüyor ama gövdede Keloğlan hiç özür dilemiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0129` birebir aynı, `@degisim: içmek -> aramak` (tutuyorsan), ardından `@onarim: 392ff097c3de2745e573d55712aec2e87dc096c1`, sonra gövde.

### Hikâye 2: tohum keloglan-0130 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0130
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'perde', fiil 'gitmek', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: yağmur başladı ve kuru bir yer yoktu | bomboş sepeti ters çevirip başına koydu
@tohum: keloglan-0130
@degisim: perde -> sepet
Ormanda Keloğlan bomboş sepetiyle fındık toplamaya gidiyordu. Birden yağmur yağmaya başladı ve Keloğlan'ın başı ıslandı. Keloğlan saklanacak kuru bir yer aradı, ama her yer ıslaktı. Keloğlan elindeki sepete baktı ve düşündü. Sonra sepeti ters çevirdi ve başına koydu. Yağmur damlaları sepetin üstüne düştü. Keloğlan biraz sakardı ve sepet bir kez başından kaydı. Keloğlan onu yerden aldı ve iki eliyle sıkıca tuttu. Artık başı hiç ıslanmadı. Keloğlan sepetin altında sessizce bekledi. Biraz sonra yağmur dindi ve güneş çıktı. Keloğlan sepeti başından aldı ve koluna taktı. Sonra mutlu mutlu fındık toplamaya başladı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve sepet bir kez başından kaydı"
   - Cümle 7: «Keloğlan biraz sakardı ve sepet bir kez başından kaydı.»
   - Açıklama: Tohumdaki sakarlık özelliği işe yarar biçimde kullanılmıyor; çözüme katkısı yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepet bir kez başından kaydı"
   - Cümle 7: «Keloğlan biraz sakardı ve sepet bir kez başından kaydı.»
   - Açıklama: Sepetin kayması hiçbir sonuca bağlanmayan, olay zincirinden çıkmayan araya sokulmuş bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve sepet bir kez başından kaydı"
   - Cümle 7: «Keloğlan biraz sakardı ve sepet bir kez başından kaydı.»
   - Açıklama: Sepetin kayması çözüme hiçbir şey katmayan, yalnız özelliği göstermek için eklenmiş bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0130` birebir aynı, `@degisim: perde -> sepet` (tutuyorsan), ardından `@onarim: da39d294eeefcc0fb465b94032ca1aecdad867d9`, sonra gövde.

### Hikâye 3: tohum keloglan-0133 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0133
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tartı', fiil 'gülmek', sıfat 'oynak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yeni tartı taşların üstünde sallanıyordu | tartıyı taşlardan alıp düz bir yere koydu
@tohum: keloglan-0133
Rüzgar büyük ağaçların arasında hafifçe esiyordu. Keloğlan ormanda Bilgecan Dede'nin yeni yaptığı tartıyı gördü. Dede tartıyı otların üstüne koymuştu, ama tartı oynak duruyor ve hep sallanıyordu. Dede cevizleri köyün çocukları için tartmak ve iki torbaya koymak istiyordu. "Dede, bu tartı neden sallanıyor?" diye sordu Keloğlan. "Bilmiyorum, sen de bir bak," dedi Bilgecan Dede. Keloğlan yeni şeyler öğrenmeyi severdi ve hemen tartının altına baktı. Otların arasında küçük taşlar vardı. Keloğlan tartıyı taşlardan aldı ve düz bir yere koydu. Tartı artık hiç sallanmadı. Dede cevizleri tarttı ve iki torbaya koydu. Keloğlan ile Dede birlikte güldü ve torbaları mutlu mutlu bağladı.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: ""Bilmiyorum, sen de bir bak," dedi Bilgecan Dede"
   - Cümle 6: «"Bilmiyorum, sen de bir bak," dedi Bilgecan Dede.»
   - Açıklama: Kartın ilişki alanında Bilgecan Dede köyün en bilge kişisi ve çocuklara bilmediklerini öğreten kişidir; burada kendi icadını bilmiyor.
   - Açıklama: Kartın ilişki alanında köyün en bilge kişisi ve mucit olan Dede kendi yaptığı tartının sorununu bilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0133` birebir aynı, ardından `@onarim: a4e259060c593e07c3b6fb2c9b754bca220d96ae`, sonra gövde.

### Hikâye 4: tohum keloglan-0136 (deneme 4 -> 5)

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
Tepede serin bir rüzgar esiyordu. Keloğlan, eşeği Karakaçan'a bir sürpriz hazırlamıştı. Sepette lezzetli elmalar vardı, ama kapağın ipi sıkı bir düğüm olmuştu. Keloğlan elmalar düşmesin diye ipi çok iyi bağlamıştı. "Karakaçan, sürprizini görmek ister misin?" diye sordu Keloğlan. Eşek başını salladı. Keloğlan biraz sakardı ve sepeti elinden yere düşürdü. Ama hiçbir elma dökülmedi. Sonra düğümün ucunu buldu ve yavaşça çekti. Düğüm çözüldü ve kapak açıldı. Karakaçan hemen bir elma yedi ve kulaklarını oynattı. Keloğlan güldü ve eşeğinin başını okşadı. "Afiyet olsun, Karakaçan, bu elmalar senin için!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve sepeti elinden yere düşürdü"
   - Cümle 7: «Keloğlan biraz sakardı ve sepeti elinden yere düşürdü.»
   - Açıklama: Sakarlık bir şeyi düşürmek olarak gösterilse de sorunun çözümüne hiç katkı yapmıyor, işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sakardı ve sepeti elinden yere düşürdü"
   - Cümle 7: «Keloğlan biraz sakardı ve sepeti elinden yere düşürdü.»
   - Açıklama: Tohum özelliği sakarlık hiçbir sonuç doğurmuyor ve çözüme katkısı yok; özellik işe yarar biçimde kullanılmamış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepeti elinden yere düşürdü"
   - Cümle 7: «Keloğlan biraz sakardı ve sepeti elinden yere düşürdü.»
   - Açıklama: Sepetin düşmesi hiçbir sonuç doğurmayan, olaydan çıkmayan işlevsiz bir ayrıntı.
   - Açıklama: Sepetin düşmesi olaya hiçbir şey katmıyor ve işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0136` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: cb7f930b033ec1e9b4663091c75e346c636272b9`, sonra gövde.

### Hikâye 5: tohum keloglan-0137 (deneme 4 -> 5)

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
@plan: uçurtma kuyruğu olmadığı için düşüyordu | uzun kurdeleyi uçurtmaya kuyruk olarak bağladı
@tohum: keloglan-0137
@degisim: takvim -> kurdele
Tepede güçlü bir rüzgar esiyordu. Keloğlan ile Balkız büyük bir uçurtma yapmıştı. Ama uçurtma kuyruğu olmadığı için havada dönüyor ve yere düşüyordu. Keloğlan süs için getirdikleri uzun kurdeleyi eline aldı. Kurdele rüzgarda bir kuyruk gibi sallandı. "Balkız, bu kurdele uçurtmaya kuyruk olur," dedi Keloğlan. Sonra Balkız'a ne yapacağını anlattı. Sakar Keloğlan uçurtmayı eline alınca onu yere düşürdü. Balkız uçurtmayı yerden aldı ve sıkıca tuttu. Keloğlan da kurdeleyi uçurtmanın ucuna bağladı. Sonra Balkız ipi aldı ve Keloğlan uçurtmayı havaya bıraktı. Uçurtma bu kez dönmedi ve dümdüz yükseldi. "Ne güzel uçuyor, Balkız, onu birlikte yaptık!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "uçurtma kuyruğu olmadığı için düşüyordu"
   - Cümle 0 (plan satırı): «uçurtma kuyruğu olmadığı için düşüyordu | uzun kurdeleyi uçurtmaya kuyruk olarak bağladı»
   - Açıklama: İyelik eki eksik; 'uçurtmanın kuyruğu olmadığı için' olmalı, yoksa 'uçurtma kuyruğu' tamlama gibi okunuyor ve fiilin öznesi kalmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan uçurtmayı eline alınca onu yere düşürdü"
   - Cümle 8: «Sakar Keloğlan uçurtmayı eline alınca onu yere düşürdü.»
   - Açıklama: Uçurtmanın düşürülmesi olaya hiçbir şey katmayan işlevsiz bir ara olay.
   - Açıklama: Uçurtmanın düşürülmesi sorundan çıkmayan, çözüme katkısı olmayan işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0137` birebir aynı, `@degisim: takvim -> kurdele` (tutuyorsan), ardından `@onarim: 4fb4ad9f5beb0995e998ada059846c3cf8ab55be`, sonra gövde.

### Hikâye 6: tohum keloglan-0139 (deneme 4 -> 5)

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
@plan: yağmurda kulübenin çatısı bitmemişti | dalları taşıyıp çatıdaki boşluğa dizdi
@tohum: keloglan-0139
@degisim: yastık -> dal
Yağmur yavaş yavaş yağmaya başladı. Keloğlan ile Balkız ormanda dallardan küçük bir kulübe yapıyordu. Ama kulübenin çatısı bitmemişti ve içeri yağmur damlıyordu. "Keloğlan, çatıdan içeri su geliyor!" dedi Balkız. Keloğlan yerdeki büyük dallara baktı ve düşündü. Sakar Keloğlan dalları taşırken birkaçını yere düşürdü. Balkız onları yerden aldı ve ona verdi. Keloğlan dalları çatıdaki boşluğa yan yana dizdi. Böylece çatı tamamlandı. İçeri artık hiç su girmedi. Dışarıda otlar sırılsıklam oldu, ama kulübenin içi kuru kaldı. "Teşekkürler, Keloğlan, kulübemiz bitti!" dedi Balkız. Keloğlan çok sevindi, çünkü yaptıkları kulübe ikisini de yağmurdan korumuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sakar Keloğlan dalları taşırken birkaçını yere düşürdü"
   - Cümle 6: «Sakar Keloğlan dalları taşırken birkaçını yere düşürdü.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunun ya da çözümün parçası değil, işe yaramayan bir süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0139` birebir aynı, `@degisim: yastık -> dal` (tutuyorsan), ardından `@onarim: 1ca5744b70220b58da5fc3a6c3b7663fe25ce127`, sonra gövde.

### Hikâye 7: tohum keloglan-0145 (deneme 4 -> 5)

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
Dağda Keloğlan büyük bir ağaçtan gri bir kayaya koşma oyunu oynuyordu. Oyundan önce yürüyüp adımlarını saymış ve kayanın on adım uzakta olduğunu öğrenmişti. Ama birden tepeye hafif, beyaz bir sis indi ve kaya görünmez oldu. O sırada Keloğlan ağacın yanındaydı. Ağaçla kaya arasında yalnız düz, yumuşak çimenler vardı. Keloğlan koşmadı, çimenlerin üstünde dikkatle yürüdü. Bir, iki, üç diye adımlarını tek tek saydı. On adım sonra eli soğuk kayaya değdi. Keloğlan sevinçle zıpladı ve kayaya sarıldı. Biraz sonra rüzgar esti ve sis dağıldı. Hava yine tertemiz oldu ve oyun devam etti. Keloğlan çok mutluydu, çünkü kayayı sisin içinde bile bulmuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan koşmadı, çimenlerin üstünde dikkatle yürüdü"
   - Cümle 6: «Keloğlan koşmadı, çimenlerin üstünde dikkatle yürüdü.»
   - Açıklama: Tek başına bir çocuğun sisli tepede görünmeyen bir yere doğru yürümeye devam etmesi taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0145` birebir aynı, ardından `@onarim: b0cd2a0f40c8658b37c515ff582fddea2b14a8f9`, sonra gövde.

### Hikâye 8: tohum keloglan-0146 (deneme 4 -> 5)

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
@plan: yakından bir çan sesi geliyordu ama çan görünmüyordu | eğilip çalının dibine baktı ve çanı buldu
@tohum: keloglan-0146
Hafif bir rüzgar esiyordu. Keloğlan, Bilgecan Dede ile ormanda tuzlu peynirli ekmek tattı. Birden yakından bir "çın" sesi geldi ama ortada hiçbir şey yoktu. "Dede, bu ses nereden geliyor?" diye sordu Keloğlan. "Onu senin için yaptım, bul bakalım," dedi Bilgecan Dede. Keloğlan ekmeğini elinde tuttu ve sesin geldiği çalılara yürüdü. Ama çalıların arasında hiçbir şey göremedi. Keloğlan biraz sakardı ve ekmek elinden çalının dibine düştü. Keloğlan ekmeği almak için eğildi ve oraya baktı. Orada bir dalda ay biçiminde küçük bir çan vardı! "Teşekkürler, Dede, çok güzel bir çan!" dedi Keloğlan. Sonra ikisi çanın sesini mutlu mutlu dinledi.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu senin için yaptım"
   - Cümle 5: «"Onu senin için yaptım, bul bakalım," dedi Bilgecan Dede.»
   - Açıklama: 'Onu' zamiri henüz anılmamış çanı gösteriyor, önceki cümlede yalnız ses var; kimi gösterdiği belli değil.
   - Açıklama: Çan henüz anılmadığı için 'onu' zamirinin neyi gösterdiği belli değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "ekmek elinden çalının dibine düştü"
   - Cümle 8: «Keloğlan biraz sakardı ve ekmek elinden çalının dibine düştü.»
   - Açıklama: Çan Keloğlan'ın sese yönelmesiyle değil, ekmeğin kazara düşmesiyle bulunuyor; çözüm sebebe doğrudan yönelmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ekmek elinden çalının dibine düştü"
   - Cümle 8: «Keloğlan biraz sakardı ve ekmek elinden çalının dibine düştü.»
   - Açıklama: Çan, Keloğlan'ın aramasıyla değil ekmeğin tesadüfen düşmesiyle sebepsizce bulunuyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve ekmek elinden çalının dibine düştü"
   - Cümle 8: «Keloğlan biraz sakardı ve ekmek elinden çalının dibine düştü.»
   - Açıklama: Çözümü tesadüfi bir sakarlık sebepsizce getiriyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan ekmeği almak için eğildi"
   - Cümle 9: «Keloğlan ekmeği almak için eğildi ve oraya baktı.»
   - Açıklama: Çözüm sorunun sebebine yönelmiyor; Keloğlan çanı aramak için değil ekmeği almak için eğiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0146` birebir aynı, ardından `@onarim: e4c76fa7f5476cba514f63bdf4391367163a9245`, sonra gövde.

### Hikâye 9: tohum keloglan-0147 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0147
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'güneş', fiil 'erimek', sıfat 'çikolatalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: güneş vurdu ve çikolata erimeye başladı | tabağı düşürmemek için dededen yardım istedi ve gölgeye taşıdılar
@tohum: keloglan-0147
Güneş ormanda sıcacık parlıyordu. Keloğlan ile Bilgecan Dede çimende çikolatalı kurabiye yiyordu. Ama güneş tabağa vurdu ve çikolata erimeye başladı. Keloğlan tabağı gölgeye koymak için kaldırdı. Ama sakar Keloğlan'ın elinde tabak sallanmaya başladı. "Dede, tabağı birlikte taşır mıyız?" diye sordu Keloğlan. "Tabii, sen bir yanından tut, ben de öbür yanından," dedi Bilgecan Dede. İkisi tabağı yavaşça bir ağacın gölgesine götürdü. Gölge serindi ve çikolata artık erimedi. Sonra Keloğlan ile dede kurabiyeleri mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tabağı birlikte taşır mıyız?"
   - Cümle 6: «"Dede, tabağı birlikte taşır mıyız?" diye sordu Keloğlan.»
   - Açıklama: 'Taşır mıyız' bu istekte doğal değil; 'birlikte taşıyalım mı' olmalı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Keloğlan ile dede kurabiyeleri mutlu mutlu yedi"
   - Cümle 10: «Sonra Keloğlan ile dede kurabiyeleri mutlu mutlu yedi.»
   - Açıklama: Kaybolduğu söylenen kurabiyeler sonunda bulunmadan yeniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0147` birebir aynı, ardından `@onarim: 26cd40a02df60263b20af144d9b5fd6cd95dac35`, sonra gövde.

### Hikâye 10: tohum keloglan-0149 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kar çok kuru olduğu için elinde dağılıyordu | güneşte ıslak kar bulup onunla kale yaptı
@tohum: keloglan-0149
@degisim: gizemli -> ıslak
Ormanda Keloğlan kardan bir kale yapmak istiyordu. Yanına bayrak için eski bir şal almıştı. Ama kar çok kuruydu ve elinde hemen dağılıyordu. Keloğlan büyük ağaçların arasına dikkatle baktı. Güneşin vurduğu bir yerde kar parlıyordu ve biraz ıslaktı. Oradan bir avuç kar aldı ve sıktı. Bu kar hemen top oldu. Keloğlan böylece ıslak karın daha iyi olduğunu öğrendi. Sonra o karı avucunda sıkıp şekillendirdi ve küçük bir kale yaptı. Eski şalı bir dala bağladı ve kalenin üstüne dikti. Keloğlan kalesinin yanında mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "avucunda sıkıp şekillendirdi"
   - Cümle 9: «Sonra o karı avucunda sıkıp şekillendirdi ve küçük bir kale yaptı.»
   - Açıklama: 'Şekillendirdi' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Şekillendirmek' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra o karı avucunda sıkıp"
   - Cümle 9: «Sonra o karı avucunda sıkıp şekillendirdi ve küçük bir kale yaptı.»
   - Açıklama: Karı avuçta sıkma 6. cümlede zaten anlatılmıştı; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0149` birebir aynı, `@degisim: gizemli -> ıslak` (tutuyorsan), ardından `@onarim: 44a9cf6eb6097a4f36ada933c27caecbd06711ce`, sonra gövde.

### Hikâye 11: tohum keloglan-0150 (deneme 4 -> 5)

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
Evin önünde Keloğlan yerde beyaz bir tüy buldu. Tüyü avucuna koyup üfledi ve tüy havalandı. Eşeği Karakaçan da oynamak istedi, ama tüyü tutacak eli yoktu. Keloğlan tüyü yerden aldı ve eşeğe uzattı. Keloğlan biraz sakardı ve tüy elinden Karakaçan'ın burnuna düştü. Karakaçan burnundan hızla üfledi ve tüy yukarı uçtu. Keloğlan güldü, tüyü yakaladı ve yine eşeğin burnuna tuttu. Karakaçan bir daha üfledi ve tüy tekrar havalandı. Sonra sıra Keloğlan'a geldi. Keloğlan ile eşeği tüyle sırayla oynayarak çok eğlendi.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "tüy elinden Karakaçan'ın burnuna düştü"
   - Cümle 5: «Keloğlan biraz sakardı ve tüy elinden Karakaçan'ın burnuna düştü.»
   - Açıklama: Çözüm Keloğlan'ın bilinçli hamlesiyle değil, tüyün kazara eşeğin burnuna düşmesiyle geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tüy elinden Karakaçan'ın burnuna düştü"
   - Cümle 5: «Keloğlan biraz sakardı ve tüy elinden Karakaçan'ın burnuna düştü.»
   - Açıklama: Çözüm Keloğlan'ın düşünmesinden değil sakarlıkla gelen bir rastlantıdan çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0150` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 2c844fa5f1d327763c98bae5a2ca44597b6aac2f`, sonra gövde.

### Hikâye 12: tohum keloglan-0153 (deneme 4 -> 5)

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
@plan: rüzgar esti ve tohumları avucundan uçurmaya başladı | şemsiyeyi açtı ve arkasında tohumları ekti
@tohum: keloglan-0153
@degisim: ilginç -> çizgili
Dağda hava bulutluydu ve Keloğlan yanına bir şemsiye almıştı. Keloğlan bahçe oyunu oynuyordu ve elinde çizgili ayçiçeği tohumları vardı. Ama rüzgar esti ve tohumları avucundan uçurmaya başladı. Keloğlan tohumları sıkıca tuttu. O dürüst ve azimli bir çocuktu ve oyunu bırakmadı. Şemsiyeyi açtı ve rüzgara karşı yere koydu. Şemsiyenin arkasında hiç rüzgar yoktu. Keloğlan toprağı parmağıyla kazdı. Tohumları tek tek ekti ve üstlerini örttü. Tohumlar artık uçmadı ve bahçe hazır oldu. Keloğlan bundan sonra rüzgarlı havada tohumlarını şemsiyenin arkasında ekti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan bahçe oyunu oynuyordu"
   - Cümle 2: «Keloğlan bahçe oyunu oynuyordu ve elinde çizgili ayçiçeği tohumları vardı.»
   - Açıklama: Gerçek tohum ekerken 'bahçe oyunu oynuyordu' demek kelimeyi yanlış anlamda kullanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "O dürüst ve azimli bir çocuktu"
   - Cümle 5: «O dürüst ve azimli bir çocuktu ve oyunu bırakmadı.»
   - Açıklama: 'Dürüst' olayla ilgisiz; oyunu bırakmamak dürüstlükle anlatılmaz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 5: «O dürüst ve azimli bir çocuktu ve oyunu bırakmadı.»
   - Açıklama: 'Azimli' soyut bir kavram ve küçük çocuk için bilinmeyen bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "O dürüst ve azimli bir çocuktu"
   - Cümle 5: «O dürüst ve azimli bir çocuktu ve oyunu bırakmadı.»
   - Açıklama: 'Dürüst' ve 'azimli' soyut kelimeler olaya bağlı değil ve 3 yaşındaki çocuk bilmez.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O dürüst ve azimli bir çocuktu"
   - Cümle 5: «O dürüst ve azimli bir çocuktu ve oyunu bırakmadı.»
   - Açıklama: Dürüstlük olayda hiçbir işe yaramıyor; işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0153` birebir aynı, `@degisim: ilginç -> çizgili` (tutuyorsan), ardından `@onarim: 547738868211e6d80c8d73391d00cdc3bec4fb0c`, sonra gövde.
