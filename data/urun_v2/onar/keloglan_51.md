# Editör görevi (onarım): Keloğlan, onarım partisi 51

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar51.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar51.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0156 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0156
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'şerit', fiil 'esnemek', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: rüzgar mavi şeridi uçurdu ve şerit çalıya takıldı | arkadaşından yardım istedi ve şeridi birlikte çıkardılar
@tohum: keloglan-0156
@degisim: somurtkan -> üzgün
Şatonun büyük bahçesinde Keloğlan ile Balkız oynuyordu. Birden rüzgar esti ve Balkız'ın mavi şeridi uçtu. Şerit bir çalıya takıldı ve Balkız üzgün üzgün baktı. Keloğlan şeridi ucundan çekti. Şerit esnedi ama dallardan çıkmadı. Keloğlan biraz sakardı ve şeridin ucunu elinden düşürdü. Keloğlan hemen Balkız'dan yardım istedi. Balkız dalları iki eliyle yavaşça ayırdı. Keloğlan da şeridi dalların arasından dikkatle çıkardı. Sonra şeridi Balkız'ın sarı saçına bağladı. Balkız hemen gülümsedi. Keloğlan çok sevindi, çünkü Balkız yine gülüyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve şeridin ucunu elinden düşürdü"
   - Cümle 6: «Keloğlan biraz sakardı ve şeridin ucunu elinden düşürdü.»
   - Açıklama: Şeridin ucunu düşürmek hiçbir sonuç doğurmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0156` birebir aynı, `@degisim: somurtkan -> üzgün` (tutuyorsan), ardından `@onarim: 55ff7f9acfb095779e5707bcfe9b03ebf756ca71`, sonra gövde.

### Hikâye 2: tohum keloglan-0158 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0158
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çorba', fiil 'koşuşturmak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: yorgun ve aç eşek ağacın altında durdu | elmasını eşeğiyle paylaşınca eşek yeniden yürüdü
@tohum: keloglan-0158
@degisim: sağlıklı -> sıcak
Keloğlan eşeğiyle ormandan eve dönüyordu. İkisi odun toplamak için ormanda çok koşuşturmuştu. Eşek çok yorulmuştu ve büyük bir ağacın altında durdu. Keloğlan eve gidip sıcak çorba içmek istiyordu. Eşeği ipinden çekti ama eşek hiç yürümedi. Keloğlan'ın çantasında iki elma vardı. Keloğlan eşeğin aç olduğunu anladı. O dürüst bir çocuktu ve elmaları eşit paylaştı. Elmalardan birini eşeğine verdi. Eşek elmayı çıtır çıtır yedi. Sonra eşek başını salladı ve yeniden yürüdü. Keloğlan çok sevindi, çünkü elmasını eşeğiyle paylaşmıştı.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "O dürüst bir çocuktu"
   - Cümle 8: «O dürüst bir çocuktu ve elmaları eşit paylaştı.»
   - Açıklama: Elmayı paylaşmak dürüstlük değil; 'dürüst' yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "O dürüst bir çocuktu ve elmaları eşit paylaştı"
   - Cümle 8: «O dürüst bir çocuktu ve elmaları eşit paylaştı.»
   - Açıklama: Eşit paylaşmak dürüstlük değil, adaletle ilgilidir; 'dürüst' yanlış anlamda kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "O dürüst bir çocuktu ve elmaları eşit paylaştı"
   - Cümle 8: «O dürüst bir çocuktu ve elmaları eşit paylaştı.»
   - Açıklama: Dürüstlük özelliği eşit paylaşma olarak yanlış kullanılıyor; kartın özellik alanıyla örtüşmüyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O dürüst bir çocuktu"
   - Cümle 8: «O dürüst bir çocuktu ve elmaları eşit paylaştı.»
   - Açıklama: Dürüstlük paylaşmayla ilgisiz, işlevsiz bir ayrıntı olarak sokulmuş.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O dürüst bir çocuktu ve elmaları eşit paylaştı"
   - Cümle 8: «O dürüst bir çocuktu ve elmaları eşit paylaştı.»
   - Açıklama: Dürüstlük ve eşit paylaşma olaydan çıkmıyor; eşeğe elma vermekle ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elmalardan birini eşeğine verdi"
   - Cümle 9: «Elmalardan birini eşeğine verdi.»
   - Açıklama: Sebep yorgunluk olarak kurulmuşken çözüm hiç işaret verilmeyen açlığa yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0158` birebir aynı, `@degisim: sağlıklı -> sıcak` (tutuyorsan), ardından `@onarim: 6593185aff0c3c390e079865542985cc95d43616`, sonra gövde.

### Hikâye 3: tohum keloglan-0163 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0163
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'nota', fiil 'çevirmek', sıfat 'faydalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşeğin uzun ipi büyük bir ağaca takıldı | ipin ağaca dolandığını görüp eşeği öbür yana çevirdi
@tohum: keloglan-0163
@degisim: nota -> ip
Ormanda büyük ağaçların arasında kuşlar ötüyordu. Keloğlan ıslık çaldı ve eşeğini çağırdı. Karakaçan koşarak geldi, ama uzun ipi bir ağaca takıldı. Eşek ileri gidemedi. Keloğlan ipi çekti ama ip çıkmadı. "Dur, Karakaçan, önce ipe bakayım," dedi Keloğlan. Keloğlan ağacın arkasına baktı ve yeni bir şey öğrendi. İp ağacın arkasından dönüp geri geliyordu. Keloğlan eşeğin başını öbür yana çevirdi ve onu geri götürdü. İp ağaçtan hemen çıktı. Karakaçan başını salladı ve Keloğlan'ın yanına geldi. "Ağacın arkasına bakmak çok faydalı oldu," dedi Keloğlan. Keloğlan bundan sonra ip takılınca önce dikkatle baktı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "baktı ve yeni bir şey öğrendi"
   - Cümle 7: «Keloğlan ağacın arkasına baktı ve yeni bir şey öğrendi.»
   - Açıklama: Keloğlan bir şey öğrenmedi, ipin dolandığını gördü; 'öğrendi' yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bakmak çok faydalı oldu"
   - Cümle 12: «"Ağacın arkasına bakmak çok faydalı oldu," dedi Keloğlan.»
   - Açıklama: 'Faydalı' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ağacın arkasına bakmak çok faydalı oldu"
   - Cümle 12: «"Ağacın arkasına bakmak çok faydalı oldu," dedi Keloğlan.»
   - Açıklama: 'Faydalı' soyut bir kelime ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0163` birebir aynı, `@degisim: nota -> ip` (tutuyorsan), ardından `@onarim: 34d4f150f4101f2f59c50e5bdfc617db6ea7acb4`, sonra gövde.

### Hikâye 4: tohum keloglan-0166 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0166
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kitap', fiil 'doymak', sıfat 'yeterli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: rüzgar kitabı pencereden düşürdü ve kitap kayboldu | eşeğe sorup sepetteki samanın içinde kitabı buldu
@tohum: keloglan-0166
@degisim: yeterli -> sağlam
Köy evinde Keloğlan kitabını pencerenin önüne koymuştu. Birden rüzgar esti ve kitap pencereden bahçeye düştü. Keloğlan koşup bahçeye çıktı, ama kitabı hiçbir yerde göremedi. Pencerenin altında Karakaçan duruyordu. Yanında bir saman sepeti vardı. "Karakaçan, kitabımı gördün mü?" diye sordu Keloğlan. Karakaçan başını sepete doğru salladı. Keloğlan sepete baktı ve elleriyle samanı karıştırdı. Keloğlan biraz sakardı ve samanın yarısını yere döktü. Samanın içinden kitap çıktı! Keloğlan samanı sepete geri koydu. Karakaçan da samanını yiyip doydu. Keloğlan çok sevindi, çünkü kitabını sağlam bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve samanın yarısını yere döktü"
   - Cümle 9: «Keloğlan biraz sakardı ve samanın yarısını yere döktü.»
   - Açıklama: Samanı dökme olayı hiçbir işe yaramıyor ve yalnız özelliği göstermek için ekleniyor.
   - Açıklama: Samanın dökülmesi ve sonra geri konması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karakaçan da samanını yiyip doydu"
   - Cümle 12: «Karakaçan da samanını yiyip doydu.»
   - Açıklama: Eşeğin saman yemesi sorun ve çözümle ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Eşeğin samanı yemesi sorunla ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0166` birebir aynı, `@degisim: yeterli -> sağlam` (tutuyorsan), ardından `@onarim: e161d8865243450bfefba39c28903fd1806f1d8b`, sonra gövde.

### Hikâye 5: tohum keloglan-0167 (deneme 3 -> 4)

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
@plan: anası tabağı süslemek istedi ama yakında çiçek yoktu | düşen elmayı ararken taşın arkasında çiçek buldu
@tohum: keloglan-0167
@degisim: un -> kek
Tepenin üstü geniş ve düzdü. Keloğlan ile anası orada piknik yapıyordu. Anası kekin tabağını çiçeklerle süslemek istiyordu ama yakında hiç çiçek yoktu. "Ben sana çiçek bulurum, anneciğim," dedi Keloğlan. Keloğlan biraz sakardı ve kalkarken elindeki elmayı düşürdü. Elma yuvarlandı ve büyük bir taşın arkasına gitti. Keloğlan elmayı almak için taşın arkasına baktı. Orada bir sürü sarı çiçek vardı! Keloğlan elmayı aldı ve birkaç çiçek topladı. "Çiçekler taşın arkasındaymış, anneciğim!" dedi Keloğlan. Anası çiçekleri tabağın kenarına dizdi ve kekin tabağı güzelce süslendi. Keloğlan ile anası kekten birer dilim alıp mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yakında hiç çiçek yoktu"
   - Cümle 3: «Anası kekin tabağını çiçeklerle süslemek istiyordu ama yakında hiç çiçek yoktu.»
   - Açıklama: Yakında hiç çiçek olmadığı söyleniyor ama hemen yandaki taşın arkasında bir sürü çiçek çıkıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kalkarken elindeki elmayı düşürdü"
   - Cümle 5: «Keloğlan biraz sakardı ve kalkarken elindeki elmayı düşürdü.»
   - Açıklama: Çözüm çiçek aramaya yönelmiyor; çiçekler düşen elmanın peşinde tesadüfen bulunuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalkarken elindeki elmayı düşürdü"
   - Cümle 5: «Keloğlan biraz sakardı ve kalkarken elindeki elmayı düşürdü.»
   - Açıklama: Çiçekler şans eseri düşen bir elma sayesinde bulunuyor; çözüm sebepsizce geliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elma yuvarlandı ve büyük bir taşın arkasına gitti"
   - Cümle 6: «Elma yuvarlandı ve büyük bir taşın arkasına gitti.»
   - Açıklama: Çözümü sebepsiz bir tesadüf getiriyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan elmayı almak için taşın arkasına baktı"
   - Cümle 7: «Keloğlan elmayı almak için taşın arkasına baktı.»
   - Açıklama: Keloğlan çiçek aramıyor, elmasının peşinden giderken çiçeğe rastlıyor; çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0167` birebir aynı, `@degisim: un -> kek` (tutuyorsan), ardından `@onarim: 8b873fb902815593e71c59b5092c5369fc137f0b`, sonra gövde.

### Hikâye 6: tohum keloglan-0172 (deneme 3 -> 4)

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
@degisim: filiz -> çiçek
Büyük ağaçlarda kuşlar ötüyordu. Keloğlan ile Balkız ormanda sepetle bir oyun oynuyordu. Ama ikisi de ellerini aynı anda sepete soktu. Elleri çarpıştı ve kimse bir şey çıkaramadı. "Balkız, önce sen oyna, ben seni izleyeyim," dedi Keloğlan. Balkız gözlerini kapadı ve sepetten bir şey çıkardı. "Bu sert bir kozalak!" dedi Balkız. Keloğlan onu dikkatle izledi ve nasıl oynandığını öğrendi. Sonra sıra ona geldi. Keloğlan gözlerini kapadı ve yapışkan bir şey tuttu. "Bu reçelli ekmek!" diye güldü Keloğlan. Balkız da sırası gelince sepetten küçük bir çiçek çıkardı. İki arkadaş çok eğlendi, çünkü sırayla oynamak çok güzeldi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "nasıl oynandığını öğrendi"
   - Cümle 8: «Keloğlan onu dikkatle izledi ve nasıl oynandığını öğrendi.»
   - Açıklama: Keloğlan oyunu baştan beri oynuyorken oyunun nasıl oynandığını yeni öğrenmiş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0172` birebir aynı, `@degisim: filiz -> çiçek` (tutuyorsan), ardından `@onarim: ca3de220a7a23b679f466e9ccb06cdac740718e1`, sonra gövde.

### Hikâye 7: tohum keloglan-0173 (deneme 3 -> 4)

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
@plan: eşek de oyuna katılmak istedi ama fırçayla çizemezdi | dalla boya sıçratmayı öğrendi ve dalı eşeğin ağzına verdi
@tohum: keloglan-0173
@degisim: tablo -> resim
Ormanda rüzgar serin serin esiyordu. Keloğlan büyük bir ağacın dibinde ucuz mavi boyayla tahtaya resim yapıyordu. Eşeği Karakaçan da oyuna katılmak istedi ama fırçayla çizemezdi. Keloğlan bir dalı boyaya batırdı ve hafifçe salladı. Boya tahtaya küçük noktalar halinde sıçradı. Keloğlan böylece dalla boya sıçratmayı öğrendi. Keloğlan dalın temiz ucunu Karakaçan'ın ağzına verdi. "Sıra sende, Karakaçan," dedi Keloğlan. Karakaçan başını salladı ve tahtaya mavi noktalar sıçradı. Sonra sıra yine Keloğlan'a geldi. Keloğlan ile Karakaçan sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ucuz mavi boyayla tahtaya"
   - Cümle 2: «Keloğlan büyük bir ağacın dibinde ucuz mavi boyayla tahtaya resim yapıyordu.»
   - Açıklama: 'Ucuz' fiyat gibi soyut bir kavram, küçük çocuğa uygun ve gerekli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ucuz mavi boyayla tahtaya"
   - Cümle 2: «Keloğlan büyük bir ağacın dibinde ucuz mavi boyayla tahtaya resim yapıyordu.»
   - Açıklama: Boyanın ucuz olması kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0173` birebir aynı, `@degisim: tablo -> resim` (tutuyorsan), ardından `@onarim: c553cd1bdf0c64b38a1b28cfae1a45a4667506e1`, sonra gövde.

### Hikâye 8: tohum keloglan-0174 (deneme 3 -> 4)

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
@plan: hamur az ezilmişti ve köfte elinde dağıldı | doğruyu söyledi ve hamuru iyice ezdi
@tohum: keloglan-0174
@degisim: vanilyalı -> yuvarlak
Köy evinin mutfağında Keloğlan ile anası lokanta oyunu oynuyordu. "Bana bir tabak köfte, lütfen," dedi anası. Ama hamur az ezilmişti ve köfte Keloğlan'ın elinde dağıldı. Keloğlan dürüst davrandı ve anasına söyledi: "Anneciğim, köfteler dağılıyor." "Hamuru biraz daha ez," dedi anası. Keloğlan hamuru iki eliyle uzun uzun ezdi. Sonunda ekmek ve et iyice karıştı. Keloğlan küçük bir parça aldı ve yuvarladı. Bu kez köfte bozulmadı, yuvarlak ve düzgün oldu. Keloğlan köfteleri bir tepsiye dizdi ve anasına götürdü. "Ne güzel köfteler!" dedi anası ve güldü. Keloğlan bundan sonra köfte yaparken hamuru iyice ezdi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama hamur az ezilmişti"
   - Cümle 3: «Ama hamur az ezilmişti ve köfte Keloğlan'ın elinde dağıldı.»
   - Açıklama: Köfte harcı ezilmez, yoğrulur; fiil yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0174` birebir aynı, `@degisim: vanilyalı -> yuvarlak` (tutuyorsan), ardından `@onarim: e2163bfcdecd951eb465db00ba90110142d12483`, sonra gövde.

### Hikâye 9: tohum keloglan-0175 (deneme 3 -> 4)

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
Tepede güneşli ve güzel bir gündü. Keloğlan yeni tahta topacını döndürmek istiyordu. Ama çimenler uzundu ve topaç hemen devrildi. Keloğlan ipi yeniden sardı ve topacı bir daha attı. Topaç bu kez biraz sallandı ve yine yan yattı. Keloğlan kahkahalarla güldü. Sonra nedenini öğrenmek istedi. Yere eğildi ve çimenlere dikkatle baktı. Topaç uzun çimenlere takılıyordu. Keloğlan çimenlerin yanında büyük ve düz bir taş buldu. Bu kez acele etmedi, sabırlı oldu ve ipi yavaşça sardı. Topacı taşın üstüne attı ve topaç hızlı hızlı döndü. Keloğlan sevinçle ellerini çırptı. Keloğlan bundan sonra topacını hep düz bir yerde döndürdü.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "acele etmedi, sabırlı oldu"
   - Cümle 11: «Bu kez acele etmedi, sabırlı oldu ve ipi yavaşça sardı.»
   - Açıklama: Tohumdaki özellik öğrenmeyi sevmek; sabır ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik öğrenmek; sabır ikinci bir özellik olarak ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kez acele etmedi, sabırlı oldu"
   - Cümle 11: «Bu kez acele etmedi, sabırlı oldu ve ipi yavaşça sardı.»
   - Açıklama: Sorunun sebebi uzun çimenler olduğu halde sabır ve acele etmeme sebepsizce çözümün parçası gibi sunuluyor.
   - Açıklama: Sorunun sebebi çimenlerken çözüme daha önce hiç kurulmamış bir acele/sabır sebebi ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0175` birebir aynı, `@degisim: kilitlemek -> sarmak` (tutuyorsan), ardından `@onarim: acf1a21e525ea7f62fe356c5043e89bd59722ede`, sonra gövde.

### Hikâye 10: tohum keloglan-0176 (deneme 3 -> 4)

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
Rüzgar esiyordu ve dere şırıl şırıl akıyordu. Keloğlan ormanda yürürken tak tak diye garip bir ses duydu. Ama derenin sesi yüzünden sesin yerini bulamadı. Keloğlan önce sağa, sonra sola yürüdü. Ses bir kesildi, bir yeniden geldi. Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı. Dereden biraz uzaklaştı ve dikkatle dinledi. Ses şimdi daha açık geliyordu. Ses yakındaki büyük bir elma ağacından geliyordu. Rüzgar esince ağaçtan kıpkırmızı elmalar düşüyordu. Elmalar ağacın altındaki düz bir taşa çarpıp tak tak ses yapıyordu. Keloğlan güldü ve yerdeki elmaları topladı. Keloğlan bundan sonra bir sesi ararken önce sessiz bir yerde dinledi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 6: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: 'Dürüst' ve 'azimli' soyut kavramlar ve 'dürüst' olayla ilgisiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 6: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: 'Dürüst' ve 'azimli' soyut kelimeler; 'dürüst' olayla ilgisiz ve 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 6: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: Tohum özelliğindeki dürüstlük hikayede işe yaramıyor, yalnız azimle birlikte sayılıyor; özellikler alanı işe yarar tek kullanım ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0176` birebir aynı, `@degisim: bluz -> elma` (tutuyorsan), ardından `@onarim: 539ac895ed497bb055c4755ee23ead02236613fb`, sonra gövde.

### Hikâye 11: tohum keloglan-0177 (deneme 3 -> 4)

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
Keloğlan evde, Bilgecan Dede'nin yaptığı yeni bir tahta alete bakıyordu. Aletin hareketli bir kolu vardı. Bu kol meyveleri sepete atmak için yapılmıştı. Ama kol meyveleri sepete değil, yere düşürüyordu. "Aletim güzel mi, Keloğlan?" diye sordu Bilgecan Dede. Keloğlan kolu izledi ve dürüst bir cevap verdi. "Güzel, ama kolun çubuğu kırılmış," dedi Keloğlan. Bilgecan Dede eğilip baktı ve başını salladı. Keloğlan mutfaktan tahta bir kaşık getirdi. Kaşığı bir iple kırık çubuğun yerine bağladı. Kol yeniden döndü ve bir elmayı tam sepete attı. Bilgecan Dede sevinçle ellerini çırptı. Keloğlan da çok mutlu oldu, çünkü dedenin aleti artık çalışıyordu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kol meyveleri sepete değil, yere düşürüyordu"
   - Cümle 4: «Ama kol meyveleri sepete değil, yere düşürüyordu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Güzel, ama kolun çubuğu kırılmış"
   - Cümle 7: «"Güzel, ama kolun çubuğu kırılmış," dedi Keloğlan.»
   - Açıklama: Önce sebep gri taşlar deniyor, sonra kırık çubuk olarak değişiyor; iki sebep çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0177` birebir aynı, ardından `@onarim: cf170f24d9cf3a72ebe7fe79546d619b1453b4c7`, sonra gövde.

### Hikâye 12: tohum keloglan-0180 (deneme 3 -> 4)

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
Keloğlan karlı tepede kardan bir kule yapıyordu. Kuleye küçük pencereler açmak için sağ eldivenini çıkardı. Ama sakar Keloğlan eldiveni düşürdü ve eldiven karda aşağı kaydı. Aşağıda bir sürü karışık kar yığını vardı. Keloğlan karda eğilip baktı, ama eldiveni bulamadı. Sonra sol eldivenini çıkardı ve onu da aynı yerden kaydırdı. Keloğlan onun nereye gittiğine dikkatle baktı ve peşinden yavaşça yürüdü. Sol eldiven bir kar yığınının dibinde durdu. Sağ eldiven de tam orada, karın içindeydi. Keloğlan iki eldiveni de kardan kurtardı. Eldivenleri salladı ve ellerine taktı. Sonra kulenin yanına döndü ve kuleyi mutlu mutlu bitirdi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir sürü karışık kar yığını"
   - Cümle 4: «Aşağıda bir sürü karışık kar yığını vardı.»
   - Açıklama: 'Karışık' kar yığını için yanlış anlamda kullanılmış; kastedilen 'dağınık' ya da yalnız 'kar yığını'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0180` birebir aynı, `@degisim: mürekkep -> eldiven` (tutuyorsan), ardından `@onarim: f7e6a6a69754fa42472225db3c1de49f9abba44f`, sonra gövde.
