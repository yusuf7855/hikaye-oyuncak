# Editör görevi (onarım): Keloğlan, onarım partisi 24

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar24.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar24.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0067 (deneme 3 -> 4)

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
@plan: kağıt uçak hemen düştü çünkü kanatları aynı boyda değildi | kartı yeniden katlayıp iki kanadı aynı boyda yaptı
@tohum: keloglan-0067
Keloğlan tepede beyaz bir kartı katlayıp ilk kez kağıt uçak yaptı. Uçağı havaya attı ama uçak hemen yere düştü. Uçağın bir kanadı büyük, öbür kanadı küçüktü. Keloğlan uçağı açtı ve kartı dikkatle inceledi. Böylece iki kanadın aynı boyda olması gerektiğini öğrendi. Kartı bir daha katladı ve bu kez iki ucu tam ortada buluştu. Keloğlan uçağı rüzgara doğru hafifçe fırlattı. Beyaz uçak tepenin üstünde uzun uzun süzüldü. Sonra yumuşak otların üstüne yavaşça indi. Keloğlan kağıt uçağını aldı ve tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ilk kez kağıt uçak yaptı"
   - Cümle 1: «Keloğlan tepede beyaz bir kartı katlayıp ilk kez kağıt uçak yaptı.»
   - Açıklama: Uçak kavramı kartın masal köyü dünyasına ve tohum_yasak_kategoriler (çağdaş araç) alanına aykırı.
   - Açıklama: Uçak çağdaş bir araç kavramıdır ve kartın masal köyü dünyasında (tohum yasak kategorileri: çağdaş, araç) yer almaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0067` birebir aynı, ardından `@onarim: 06f76d0ef8760bf94207ca449514a00a7403241b`, sonra gövde.

### Hikâye 2: tohum keloglan-0072 (deneme 3 -> 4)

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
@plan: kutudaki beyaz taşlardan biri kırılmıştı | köklerde beyaz yuvarlak bir taş buldu
@tohum: keloglan-0072
@degisim: büyülü -> yuvarlak
Rüzgar ağaçların arasında hafifçe esiyordu. Keloğlan ormanda elinde satranç kutusuyla yürüyordu. Kutudaki beyaz taşlardan biri kırılmıştı ve yeni bir taş lazımdı. Keloğlan satranç oynamayı çok severdi. Ağaçların dibine baktı ama yalnız koyu taşlar gördü. Keloğlan biraz sakardı ve kutuyu büyük bir ağacın köklerine düşürdü. Satranç taşlarını kökler arasından tek tek topladı. O sırada kökün yanında küçük, beyaz ve yuvarlak bir taş fark etti. Bu taş da öbür beyaz taşlar kadar küçüktü. Keloğlan taşı silip kutuya koydu. Keloğlan çok sevindi, çünkü artık yine satranç oynayabilecekti.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "elinde satranç kutusuyla yürüyordu"
   - Cümle 2: «Keloğlan ormanda elinde satranç kutusuyla yürüyordu.»
   - Açıklama: Satranç kutusu ve satranç oyunu kartın kapalı dünyasında (masal köyü) olmayan bir eşya olarak ekleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan satranç oynamayı çok severdi"
   - Cümle 4: «Keloğlan satranç oynamayı çok severdi.»
   - Açıklama: Tohumdaki özellik sakarlık; satranç sevgisi kartta olmayan ikinci bir özellik olarak ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kutuyu büyük bir ağacın köklerine düşürdü"
   - Cümle 6: «Keloğlan biraz sakardı ve kutuyu büyük bir ağacın köklerine düşürdü.»
   - Açıklama: Beyaz taş, figürün aramasıyla değil kutunun rastlantısal düşmesiyle sebepsizce bulunuyor.
   - Açıklama: Çözümü getiren taş, sebepsiz bir düşürme kazasıyla rastlantı sonucu bulunuyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "küçük, beyaz ve yuvarlak bir taş fark etti"
   - Cümle 8: «O sırada kökün yanında küçük, beyaz ve yuvarlak bir taş fark etti.»
   - Açıklama: Keloğlan sorunu bilinçli bir çabayla değil şans eseri çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0072` birebir aynı, `@degisim: büyülü -> yuvarlak` (tutuyorsan), ardından `@onarim: 4ff63b85d8d5d176d28c2cc726a61c60380baec8`, sonra gövde.

### Hikâye 3: tohum keloglan-0073 (deneme 3 -> 4)

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
Tepede kuşlar ötüyordu. Keloğlan flüt çalıyordu, anası da yanında siyah bir atkı örüyordu. Birden rüzgar esti ve anasının yumağı yokuştan aşağı yuvarlandı. Yumak dikenli bir çalının altında durdu. "Anneciğim, ben getiririm!" dedi Keloğlan. Çalıya kadar dikkatle yürüdü. Elini dikenlere sokmadı, uzun flütüyle yumağı dışarı itti. Keloğlan biraz sakardı, bu yüzden yumağı iki eliyle sıkıca tuttu. Yumağı hiç düşürmeden anasının yanına getirdi. "Teşekkür ederim, Keloğlan," dedi anası ve gülümsedi. Sonra anası atkısını örmeye, Keloğlan da flüt çalmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Keloğlan flüt çalıyordu"
   - Cümle 2: «Keloğlan flüt çalıyordu, anası da yanında siyah bir atkı örüyordu.»
   - Açıklama: Kartta Keloğlan'ın flütü ya da flüt çalma yeteneği yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden yumağı iki eliyle sıkıca tuttu"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden yumağı iki eliyle sıkıca tuttu.»
   - Açıklama: Tohumdaki sakarlık özelliği güvenli kullanım satırındaki gibi bir şeyi düşürmek ya da karıştırmak olarak gösterilmiyor ve işe yaramıyor.
   - Açıklama: Sakarlık güvenli kullanım satırındaki gibi bir şeyi düşürmek ya da karıştırmak olarak gösterilmiyor, yalnız söylenip işe yaramadan geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0073` birebir aynı, `@degisim: uyanmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 096bcb439b4f0a747b1077ace3f403c83883bee6`, sonra gövde.

### Hikâye 4: tohum keloglan-0076 (deneme 2 -> 3)

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
Bir sabah Keloğlan annesine bir sürpriz yapmak istedi. Anası mutfaktayken tahta bloklardan ona bir kule yapmaya başladı. Ama kule her seferinde devrildi, çünkü en altta küçük bloklar vardı. Keloğlan yere oturdu ve üzgün bir yüzle bloklara baktı. Sonra büyük blokları alta, küçükleri üste koydu. Bu kez kule hiç devrilmedi. Keloğlan böylece büyük blokların altta sağlam durduğunu öğrendi. Sonra sürpriz için en güzel gömleğini giydi ve annesini çağırdı. "Anneciğim, gel, sana bir sürprizim var!" dedi Keloğlan. Anası kuleyi ve Keloğlan'ın gömleğini gördü ve güldü. "Ne güzel bir kule, teşekkür ederim!" dedi anası. Sonra ikisi bloklarla birlikte mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sürpriz için en güzel gömleğini giydi"
   - Cümle 8: «Sonra sürpriz için en güzel gömleğini giydi ve annesini çağırdı.»
   - Açıklama: Gömlek giyme olaydan çıkmıyor ve kule sorununa hiçbir işlev katmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en güzel gömleğini giydi"
   - Cümle 8: «Sonra sürpriz için en güzel gömleğini giydi ve annesini çağırdı.»
   - Açıklama: Gömlek sorunla ya da çözümle ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0076` birebir aynı, ardından `@onarim: fbc7b5bc6fab4adaa7132b53475b91b363fbc46b`, sonra gövde.

### Hikâye 5: tohum keloglan-0078 (deneme 2 -> 3)

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
Bir sabah Keloğlan ile Balkız tepede oturuyordu. Gökyüzü bulutsuz ve berraktı. Balkız'ın karnı acıkmıştı ama çantasında ekmek yoktu. Çantasında yalnız küçük bir kavanoz bal vardı. Keloğlan'ın çantasında ise bir ekmek vardı. "Balkız, bu ekmeği seninle paylaşalım mı?" diye sordu Keloğlan. "Olur, ben de balımı seninle paylaşırım," dedi Balkız. Keloğlan ekmeği iki eşit parçaya böldü. Balkız kavanozu açtı ve kaşıkla kendi parçasına biraz bal sürdü. Keloğlan da aynısını yaptı. İkisi ekmeklerini yan yana oturup yedi. "Teşekkürler, Balkız, ballı ekmeği senden öğrendim, çok tatlıymış!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Gökyüzü bulutsuz ve berraktı."
   - Cümle 2: «Gökyüzü bulutsuz ve berraktı.»
   - Açıklama: 'Berrak' 3 yaşındaki çocuğun bilmeyeceği bir kelimedir.
   - Açıklama: 'Berrak' 3 yaşındaki bir çocuğun bilmediği bir kelime.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bu ekmeği seninle paylaşalım mı?"
   - Cümle 6: «"Balkız, bu ekmeği seninle paylaşalım mı?" diye sordu Keloğlan.»
   - Açıklama: Birinci çoğul 'paylaşalım' ile 'seninle' uyumsuz; 'seninle paylaşayım mı' olmalı.
   - Açıklama: 'Seninle' ile birinci çoğul 'paylaşalım' uyumsuz; 'paylaşayım mı' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ballı ekmeği senden öğrendim"
   - Cümle 12: «"Teşekkürler, Balkız, ballı ekmeği senden öğrendim, çok tatlıymış!" dedi Keloğlan.»
   - Açıklama: Tohumdaki öğrenme özelliği sona eklenmiş, paylaşma sorununun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki öğrenme özelliği sorunun çözümünde iş görmüyor, yalnız sona eklenmiş; özellik kartın öngördüğü gibi işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0078` birebir aynı, `@degisim: tomurcuk -> kavanoz` (tutuyorsan), ardından `@onarim: 8d614037777dc4076f06ac6a6f81ba7d4023bbb7`, sonra gövde.

### Hikâye 6: tohum keloglan-0079 (deneme 2 -> 3)

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
Köy evinin içi sıcak ve aydınlıktı. Keloğlan'ın anası kocaman kırmızı eşarbını arıyordu. Rüzgar eşarbı pencerenin önünden bir yere düşürmüştü. Anası bu eşarbı çok beğeniyordu ve biraz üzüldü. "Anneciğim, ben sana yardım ederim," dedi Keloğlan. Önce pencerenin önünde yere baktı ama eşarp orada yoktu. "Bırak, sonra buluruz," dedi anası. Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı. Sonra pencerenin altındaki sepete baktı. Kırmızı eşarp sepetin içindeydi! Keloğlan eşarbı çıkarıp annesine verdi. Anası eşarbını boynuna sardı ve Keloğlan'a sarıldı. Keloğlan çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 8: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: Aramayı bırakmamak dürüstlükle ilgili değil; 'dürüst' yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 8: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: 'Dürüst' ve 'azimli' soyut kelimeler; 'dürüst' olayla da ilgisiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0079` birebir aynı, ardından `@onarim: 401ec3759796b2366a9a3ff3cb813489ea85d41e`, sonra gövde.

### Hikâye 7: tohum keloglan-0081 (deneme 2 -> 3)

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
Tepede serin bir rüzgar esiyordu. Keloğlan elinde defteriyle çimenlerin arasında geziniyordu. Sonra büyük bir çam ağacının altına oturdu ve defterine bir çiçek çizdi. Ama birden resmin üstüne yapışkan, sarı bir damla düştü. Biraz sonra bir damla daha düştü. Keloğlan bu damlaları çok merak etti. Başını kaldırdı ve dallara dikkatle baktı. Dalda küçük bir delikten sarı damlalar yavaş yavaş akıyordu. Keloğlan böylece çam ağacının bu damlaları yaptığını öğrendi. Hemen defterini aldı ve ağaçtan uzak bir taşa oturdu. Orada çiçek resmine yeni renkler ekledi. Keloğlan çok sevindi, çünkü damlaları yapan ağacı bulmuştu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama birden resmin üstüne"
   - Cümle 4: «Ama birden resmin üstüne yapışkan, sarı bir damla düştü.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede ortaya çıkıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama birden resmin üstüne yapışkan, sarı bir damla düştü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede, damla resmin üstüne düşünce söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0081` birebir aynı, ardından `@onarim: e6170a8b9ecf5ce26b106f8c509a2097603e705b`, sonra gövde.

### Hikâye 8: tohum keloglan-0082 (deneme 2 -> 3)

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
Bir sabah Keloğlan ile Bilgecan Dede ormanda bir sofra kurdu. Dede kitabını da sofraya koymuştu. Keloğlan acele etti ve şişenin kapağını kapatmadan onu sofraya yatırdı. Su hemen aktı ve kitabın sayfaları ıslandı. "Özür dilerim, Dede, kitabın ıslandı," dedi Keloğlan. "Üzülme, Keloğlan," dedi Bilgecan Dede. Keloğlan kitabı açtı ve güneşli bir taşın üstüne koydu. Rüzgar sayfaları yavaşça çevirdi. Biraz sonra sayfalar kurudu. Keloğlan böylece güneşin ıslak kağıdı kuruttuğunu öğrendi. Sonra şişenin kapağını kapadı ve şişeyi sofraya dik koydu. "Aferin, Keloğlan, kitabım yine kuru!" dedi Bilgecan Dede.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kapatmadan onu sofraya yatırdı"
   - Cümle 3: «Keloğlan acele etti ve şişenin kapağını kapatmadan onu sofraya yatırdı.»
   - Açıklama: 'Onu' zamirinin kapağı mı şişeyi mi gösterdiği belli değil.
   - Açıklama: 'Onu' zamirinin şişeyi mi kapağı mı gösterdiği belli değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "güneşin ıslak kağıdı kuruttuğunu öğrendi"
   - Cümle 10: «Keloğlan böylece güneşin ıslak kağıdı kuruttuğunu öğrendi.»
   - Açıklama: Keloğlan kitabı kurutmak için bilerek güneşe koyuyor, sonra bunu yeni öğrenmiş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0082` birebir aynı, `@degisim: pahalı -> ıslak` (tutuyorsan), ardından `@onarim: bf219fe539d606591fcaef64c862392c10a1e946`, sonra gövde.

### Hikâye 9: tohum keloglan-0083 (deneme 2 -> 3)

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
@plan: taç yapmak istedi ama çiçekler hep koptu | arkadaşından yardım istedi ve çiçekleri yumuşakça bağladı
@tohum: keloglan-0083
@degisim: çöp -> papatya
Keloğlan ile Balkız tepeye çıktı. Tepede bir sürü beyaz papatya vardı. Keloğlan papatyalardan taç yapmak istedi, ama sert çekince çiçekler koptu. Sonra Balkız'dan yardım istedi. Balkız yanına geldi ve ona yavaşça gösterdi. Çiçekleri yumuşakça birbirine bağlamak gerekiyordu. Keloğlan dikkatle baktı ve bunu hemen öğrendi. Sonra papatyaları tek tek ekledi. Bu kez hiçbir çiçek kopmadı. Keloğlan'ın tacı çok güzel oldu. Keloğlan tacı Balkız'ın sarı saçlarına taktı. Balkız da ona hızlıca bir taç yaptı. Keloğlan ile Balkız çimenlere rahatça oturdu ve mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ona yavaşça gösterdi"
   - Cümle 5: «Balkız yanına geldi ve ona yavaşça gösterdi.»
   - Açıklama: 'Gösterdi' fiilinin nesnesi eksik; neyi gösterdiği söylenmiyor.
   - Açıklama: 'Gösterdi' fiilinin nesnesi eksik; neyi gösterdiği belli değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşakça birbirine bağlamak"
   - Cümle 6: «Çiçekleri yumuşakça birbirine bağlamak gerekiyordu.»
   - Açıklama: 'Yumuşakça bağlamak' yanlış kelime seçimi; 'nazikçe' ya da 'yavaşça' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0083` birebir aynı, `@degisim: çöp -> papatya` (tutuyorsan), ardından `@onarim: 6ff36af05463ecb6d43629d0a05e30b8fb9a5edf`, sonra gövde.

### Hikâye 10: tohum keloglan-0084 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0084
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kürek', fiil 'döndürmek', sıfat 'kuru'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalak yumuşak yosunların üstünde dönmedi ve devrildi | kuru ve düz bir kütüğün üstünde döndürdü
@tohum: keloglan-0084
@degisim: kürek -> kozalak
Bir sabah Keloğlan ormanda büyük bir kozalak buldu. Kozalağı topaç gibi döndürmek istedi. Ama kozalak yumuşak yosunların üstünde dönmedi ve hemen devrildi. Keloğlan bir kez daha denedi ama yine olmadı. Sonra etrafına baktı ve yakında kuru, düz bir kütük gördü. Kozalağı kütüğün üstüne koydu ve parmaklarıyla hızlıca çevirdi. Kozalak kütüğün üstünde uzun uzun döndü. Keloğlan böylece kozalağın düz ve sert bir yerde daha iyi döndüğünü öğrendi. Sonra kozalağı kütüğün üstünde döndürmeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kozalağı kütüğün üstünde döndürmeye"
   - Cümle 9: «Sonra kozalağı kütüğün üstünde döndürmeye mutlu mutlu devam etti.»
   - Açıklama: 'Kütüğün üstünde' ifadesi art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0084` birebir aynı, `@degisim: kürek -> kozalak` (tutuyorsan), ardından `@onarim: 3b84e85b7bf1f1b2f587b25c8c6a0c60c35b47c6`, sonra gövde.

### Hikâye 11: tohum keloglan-0085 (deneme 2 -> 3)

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
Bir sabah Keloğlan ile eşeği Karakaçan şatonun bahçesine vardı. Yol çok uzundu ve ikisinin de karnı acıkmıştı. Ama Keloğlan'ın cebinde yalnız bir pembe elma vardı. Keloğlan elmayı fıskiyenin suyunda yıkadı. Elmayı elleriyle ikiye bölmek istedi. İki başparmağını elmanın ortasına bastırdı ve sıkıca çevirdi. Elma çıt diye ayrıldı. Keloğlan böylece yeni bir şey öğrendi. Büyük parçayı Karakaçan'a uzattı, küçük parçayı kendisi aldı. Karakaçan elmasını yedi ve sevinçle anırdı. "Afiyet olsun, Karakaçan, bu elma ikimizin!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan böylece yeni bir şey öğrendi"
   - Cümle 8: «Keloğlan böylece yeni bir şey öğrendi.»
   - Açıklama: Somut olmayan, belirsiz ve soyut bir ders cümlesi.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan böylece yeni bir şey öğrendi"
   - Cümle 8: «Keloğlan böylece yeni bir şey öğrendi.»
   - Açıklama: Tohumdaki öğrenme özelliği ne öğrenildiği belirtilmeden etiket olarak ekleniyor ve sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan böylece yeni bir şey öğrendi"
   - Cümle 8: «Keloğlan böylece yeni bir şey öğrendi.»
   - Açıklama: Öğrenme olaydan çıkmıyor; özelliği göstermek için eklenmiş işlevsiz bir cümle.
   - Açıklama: Neyin öğrenildiği belirsiz kalan bu cümle olaydan çıkmıyor ve işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0085` birebir aynı, `@degisim: belirmek -> bölmek` (tutuyorsan), ardından `@onarim: 36f75404683d937ee7c0bc98fe1b10a4a59b2127`, sonra gövde.

### Hikâye 12: tohum keloglan-0086 (deneme 2 -> 3)

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
Rüzgar ormanın ağaçları arasında hafifçe esiyordu. Keloğlan, Balkız'ın doğum günü için değişik bir uçurtma yapmıştı. Uçurtmayı Balkız gelmeden saklamak istedi ama uçurtma çantasına sığmadı. Keloğlan dürüst ve azimli bir çocuktu, hemen vazgeçmedi. Etrafına baktı ve kalın bir ağaç gördü. Uçurtmayı ağacın arkasına dikkatlice koydu. Ağacın gövdesi çok kalındı ve uçurtma hiç görünmedi. Biraz sonra Balkız geldi ve Keloğlan'ın yanına oturdu. Keloğlan uçurtmayı ağacın arkasından çıkarıp Balkız'a verdi. Balkız uçurtmayı görünce ellerini çırptı. İkisi uçurtmayı birlikte uçurdu. Keloğlan çok sevindi, çünkü sürprizi Balkız'ı çok mutlu etmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dürüst ve azimli bir çocuktu"
   - Cümle 4: «Keloğlan dürüst ve azimli bir çocuktu, hemen vazgeçmedi.»
   - Açıklama: 'Azimli' ve 'dürüst' soyut kelimeler 3 yaşındaki çocuğa uygun değil ve olayla ilgisiz.
   - Açıklama: 'Dürüst' ve 'azimli' soyut kelimeler ve olayla bağlantısız.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 4: «Keloğlan dürüst ve azimli bir çocuktu, hemen vazgeçmedi.»
   - Açıklama: Dürüstlük olayla ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0086` birebir aynı, ardından `@onarim: 15da188a5f02937e6691409b8f1be8aabdd2ef73`, sonra gövde.
