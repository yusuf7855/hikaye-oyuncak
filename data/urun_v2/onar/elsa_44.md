# Editör görevi (onarım): Elsa, onarım partisi 44

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar44.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Elsa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar44.txt --ad urun_v2`
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

## Kart: Elsa (kaynaklı, kapalı dünya)

- Ad: Elsa (okunuş: elsa; kesme eki okunuşa uyar)
- Kimlik: Elsa, buzu ve karı yönetebilen, bir krallığın genç kraliçesidir.
- Tür: kraliçe
- Güvenli özellik kullanımı: Buz ve kar gücü yalnız zararsız, güzel şeyler için kullanılır: kar yağdırır, buzdan şekil yapar. Hiçbir canlı donmaz, üşümez ya da incinmez; kimse buz tutmuş göl ya da deniz üstünde yürümez.
- Özellikler:
  - buz: Elinden buz ve kar çıkar; buzdan şekiller yapabilir. (örnek biçimler: buzdan, buzu)
  - kraliçe: Kraliçedir; kız kardeşini korur. (örnek biçimler: kraliçe)
- Yerler:
  - dağ: Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.
  - orman: Karlı ağaçlarla dolu orman.
  - deniz: Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.
  - şato: Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Anna: Elsa'nın cesur küçük kız kardeşi. Tür: prenses; konuşur. Yüzey biçimleri: Anna, kardeş, kardeşi
  - Olaf: Elsa'nın büyüsüyle canlanan neşeli kardan adam; sıcak sarılmaları ve yazı sever. Tür: kardan adam; konuşur. Yüzey biçimleri: Olaf, kardan adam
  - Kristoff: Buz toplayıp satan cesur dağ adamı; ren geyiği Sven'in arkadaşı. Tür: adam; konuşur. Yüzey biçimleri: Kristoff
  - Sven: Kristoff'un ren geyiği; kızağı çeker. Tür: ren geyiği; KONUŞMAZ. Yüzey biçimleri: Sven, ren geyiği, geyik
- Dünya kuralları:
  - Sven konuşmaz; sesle ve hareketle anlatır.
  - Anna Elsa'nın küçük kız kardeşidir; Elsa ablasıdır.
  - Olaf Elsa'nın büyüsüyle yapılmış kardan adamdır; hikayede erimez ya da parçalanmaz.
  - Elsa'nın gücü kimseyi dondurmaz ve incitmez.
- Yasak adlar: Hans, Weselton, Pabbie, Oaken, Marshmallow, Bruni, Arendelle
- Yasak: Anne babanın gemi yolculuğu, fırtına, troller, kurtlar ve kar canavarı hikayeye girmez.
- İzinli dünya kelimeleri: buz, kar, kraliçe, saray, kızak, fiyort, geyik

## Onarılacak hikâyeler

### Hikâye 1: tohum elsa-0163 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0163
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'vanilya', fiil 'sabırsızlanmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: kapıyı kapadı ve kardan adamı dışarıda unuttu | kardan adamı arayıp kapıyı açtı ve özür diledi
@tohum: elsa-0163
@degisim: vanilya -> çan
Rüzgar dağın tepesinde sert esiyordu. Elsa buz sarayının büyük kapısını hemen kapadı. Ama Olaf dışarıda kalmıştı ve Elsa onu görmemişti. Olaf kapalı kapıya vurdu, ama rüzgar çok gürültülüydü. Olaf sabırsızlandı ve bir daha vurdu. İçeride Elsa salona baktı ama Olaf'ı göremedi. Elsa kapıya koştu ve onu açtı. "Özür dilerim, Olaf, seni dışarıda unuttum," dedi Elsa. "Tamam, ama bana sıkıca sarıl!" dedi Olaf. Elsa ona sarıldı. Sonra Elsa elini salladı ve kapının yanına buzdan küçük bir çan yaptı. Olaf çanı çaldı ve çan güzel bir ses çıkardı. Elsa ile Olaf çok sevindi, çünkü Olaf artık gelince çanı çalabilecekti.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Olaf dışarıda kalmıştı ve Elsa onu görmemişti"
   - Cümle 3: «Ama Olaf dışarıda kalmıştı ve Elsa onu görmemişti.»
   - Açıklama: Sert rüzgarda dışarıda unutulup duyulmayan Olaf küçük çocuk için korkutucu olabilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf sabırsızlandı ve bir daha"
   - Cümle 5: «Olaf sabırsızlandı ve bir daha vurdu.»
   - Açıklama: 'Sabırsızlandı' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf sabırsızlandı ve"
   - Cümle 5: «Olaf sabırsızlandı ve bir daha vurdu.»
   - Açıklama: 'Sabırsızlanmak' 3 yaşındaki bir çocuk için soyut bir duygu kelimesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0163` birebir aynı, `@degisim: vanilya -> çan` (tutuyorsan), ardından `@onarim: 99edd496bc68277d822d03828c1509d529add959`, sonra gövde.

### Hikâye 2: tohum elsa-0165 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0165
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'teker', fiil 'ısınmak', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: arabanın tekeri bir taşa çarpıp çatladı | sarayın küçük arabasını paylaştı ve buzları taşıdılar
@tohum: elsa-0165
Bir sabah Kristoff limanda buz dolu arabasını çekiyordu. Kraliçe Elsa da sarayın küçük arabasıyla oradaydı. Ama Kristoff'un arabasının tekeri bir taşa çarptı ve çatladı. Araba yana yattı ve bir buz parçası yere düştü. Elsa'nın arabasında biraz boş yer vardı. Elsa arabasını hemen Kristoff ile paylaştı. Kristoff buzları yetenekli elleriyle Elsa'nın arabasına dizdi. Elsa da düşen buz parçasını aldı ve arabaya koydu. İkisi çalıştıkça ısındı ve yüzleri kızardı. Kristoff teşekkür etmek için Elsa'ya en parlak buz parçasını verdi. Elsa o buzu güneşe tuttu ve güldü. Sonra Elsa ile Kristoff arabayı mutlu mutlu birlikte çekti.
```

**Hakem bulguları (7):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa da sarayın küçük arabasıyla"
   - Cümle 2: «Kraliçe Elsa da sarayın küçük arabasıyla oradaydı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın 'özellikler' alanındaki gibi işe yarar biçimde kullanılmıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa'nın arabasında biraz boş yer vardı"
   - Cümle 5: «Elsa'nın arabasında biraz boş yer vardı.»
   - Açıklama: Arabada yalnız biraz boş yer varken buz dolu bir arabanın bütün buzları oraya sığıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa arabasını hemen Kristoff ile paylaştı"
   - Cümle 6: «Elsa arabasını hemen Kristoff ile paylaştı.»
   - Açıklama: Sorunun sebebi çatlayan teker ama çözüm tekere yönelmiyor, yalnız başka arabaya geçiliyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzları yetenekli elleriyle Elsa'nın"
   - Cümle 7: «Kristoff buzları yetenekli elleriyle Elsa'nın arabasına dizdi.»
   - Açıklama: 'Yetenekli eller' mecazlı ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzları yetenekli elleriyle"
   - Cümle 7: «Kristoff buzları yetenekli elleriyle Elsa'nın arabasına dizdi.»
   - Açıklama: 'yetenekli elleriyle' soyut ve kalıp bir anlatım, 3 yaşındaki çocuğa uygun değil.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İkisi çalıştıkça ısındı ve yüzleri kızardı"
   - Cümle 9: «İkisi çalıştıkça ısındı ve yüzleri kızardı.»
   - Açıklama: Isınıp yüzlerinin kızarması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Isınıp yüzlerin kızarması olaydan çıkmayan işlevsiz bir ayrıntı.
7. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "arabayı mutlu mutlu birlikte çekti"
   - Cümle 12: «Sonra Elsa ile Kristoff arabayı mutlu mutlu birlikte çekti.»
   - Açıklama: Hikayede iki araba var (Kristoff'un kırık arabası ve Elsa'nın arabası); 'arabayı' hangisini gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0165` birebir aynı, ardından `@onarim: 64bd6f4e53dad4e321bdb34098cc3aef5fd0cb31`, sonra gövde.

### Hikâye 3: tohum elsa-0167 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0167
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tepsi', fiil 'çıkmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: tepsi karlı tepede bir şeye çarpıp durdu | karı itip gizli taşı buldu ve yanından kaydı
@tohum: elsa-0167
Ormanda küçük ve karlı bir tepe vardı. Elsa bir tepsiye oturdu ve tepeden aşağı kaydı. Ama tepsi tepenin ortasında "tak" diye bir şeye çarptı ve durdu. Elsa bu sesi çok merak etti. Tepsiden kalktı ve karı eliyle yavaşça kenara itti. Karın altından gizli, büyük bir taş çıktı. Tepsi bu taşa çarpmıştı. Elsa kraliçeydi ve kimsenin bu taşa çarpmasını istemedi. Yerden uzun bir dal aldı ve taşın yanına dikti. Sonra Elsa tepeye geri yürüdü. Bu kez dalın öbür yanından aşağı kaydı. Tepsi hiç durmadan en alta kadar gitti. Elsa gülerek tepeye koştu ve mutlu mutlu bir daha kaydı.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Tepsi bu taşa çarpmıştı"
   - Cümle 7: «Tepsi bu taşa çarpmıştı.»
   - Açıklama: Taşa çarptığı zaten anlatılmıştı; cümle gereksiz tekrar.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve kimsenin"
   - Cümle 8: «Elsa kraliçeydi ve kimsenin bu taşa çarpmasını istemedi.»
   - Açıklama: Kartın özellik alanındaki kraliçelik (kız kardeşini korur) yalnız etiket olarak geçiyor, çözüme katkısı yok.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yerden uzun bir dal aldı"
   - Cümle 9: «Yerden uzun bir dal aldı ve taşın yanına dikti.»
   - Açıklama: Taşı bulup yanından kaymak yeterken dal dikmek çözüme üçüncü bir adım ekliyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yerden uzun bir dal aldı ve taşın yanına dikti"
   - Cümle 9: «Yerden uzun bir dal aldı ve taşın yanına dikti.»
   - Açıklama: Karı itme, dal dikme, tepeye yürüme ve yanından kayma ile çözüm iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0167` birebir aynı, ardından `@onarim: ec8106533f5a43e077f42a9773edc5bbae1394c4`, sonra gövde.

### Hikâye 4: tohum elsa-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0170
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'altın', fiil 'indirmek', sıfat 'hazırlıklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: rüzgar şapkayı yüksek bir dala taktı | buzdan bir topla dalı salladı ve şapkayı düşürdü
@tohum: elsa-0170
@degisim: altın -> yün
Bir sabah Elsa ile Kristoff karlı ormanda yürüyordu. Birden rüzgar esti ve Kristoff'un yün şapkası yüksek bir dala takıldı. Kristoff hazırlıklı bir adamdı ve çantasından bir ip çıkardı. Ama ipi attı ve ip dala yetişmedi. "Elsa, şapkamı daldan nasıl indireceğim?" diye sordu Kristoff. "Ben sana yardım ederim," dedi Elsa. Elsa elini dala doğru uzattı. Elinden buzdan küçük bir top çıktı ve dala yavaşça çarptı. Dal sallandı ve şapka yumuşak karın üstüne düştü. Kristoff şapkayı aldı ve başına taktı. "Teşekkürler, Elsa, başım yine sıcak," dedi Kristoff. Sonra ikisi ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "rüzgar şapkayı yüksek bir dala taktı"
   - Cümle 0 (plan satırı): «rüzgar şapkayı yüksek bir dala taktı | buzdan bir topla dalı salladı ve şapkayı düşürdü»
   - Açıklama: Rüzgar bilinçli bir özne değil, 'takmak' fiili ona uymuyor; 'şapka dala takıldı' olmalı.
   - Açıklama: Rüzgar bir şeyi dala takmaz; fiil öznesine uymuyor, gövdedeki gibi 'takıldı' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elinden buzdan küçük bir top çıktı ve dala yavaşça çarptı"
   - Cümle 8: «Elinden buzdan küçük bir top çıktı ve dala yavaşça çarptı.»
   - Açıklama: Güvenli özellik kullanımı satırı yalnız kar yağdırmak ve buzdan şekil yapmayı sayıyor; buz topu dala fırlatılan bir mermi olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0170` birebir aynı, `@degisim: altın -> yün` (tutuyorsan), ardından `@onarim: 622486acd304cb6e79968ec92485654fe56d19d0`, sonra gövde.

### Hikâye 5: tohum elsa-0172 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0172
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'eldiven', fiil 'saymak', sıfat 'renkli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: sık çalılar yüzünden ağacın arkası görünmüyordu | kardan adamdan yardım isteyip yıldızları saydırdı
@tohum: elsa-0172
Elsa karlı ormanda büyük bir ağacı buzdan yıldızlarla süslüyordu. Eldivenlerini çıkardı ve elinden yıldızlar yaptı. Ama ağacın arkasında sık çalılar vardı ve Elsa oraya geçemiyordu. "Olaf, bana yardım eder misin?" diye sordu Elsa. "Tabii, Elsa!" dedi Olaf. Olaf çalıların altından ağacın arkasına geçti. Arkadaki yıldızları tek tek saydı. "Burada yalnız iki yıldız var," dedi Olaf. Elsa elini ağacın üstünden uzattı ve arkaya beş yıldız daha yaptı. "Şimdi iki yan da aynı!" dedi Olaf. Güneş çıktı ve yıldızlar renkli renkli parladı. Sonra Elsa ile Olaf ağacın etrafında mutlu mutlu dans etti.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ağacın arkası görünmüyordu"
   - Cümle 0 (plan satırı): «sık çalılar yüzünden ağacın arkası görünmüyordu | kardan adamdan yardım isteyip yıldızları saydırdı»
   - Açıklama: Gövdede sorun arkanın görünmemesi değil, Elsa'nın çalılar yüzünden oraya geçememesi.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkaya beş yıldız daha yaptı"
   - Cümle 9: «Elsa elini ağacın üstünden uzattı ve arkaya beş yıldız daha yaptı.»
   - Açıklama: Buz özelliği bir kez değil, birden çok kez yıldız yapmak için kullanılıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa elini ağacın üstünden uzattı"
   - Cümle 9: «Elsa elini ağacın üstünden uzattı ve arkaya beş yıldız daha yaptı.»
   - Açıklama: Elsa büyük ağacın arkasına geçemiyorken elini ağacın üstünden uzatıp arkaya yıldız yapabiliyor; bu hem çelişkili hem akla yatkın değil.
   - Açıklama: Elsa ağacın arkasına ulaşamadığı sorun olarak kurulmuşken sonra elini ağacın üstünden uzatıp arkaya yıldız yapabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0172` birebir aynı, ardından `@onarim: beb213c502591ab76f4404c0207d429e8337ce93`, sonra gövde.

### Hikâye 6: tohum elsa-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0173
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'gömlek', fiil 'yardımlaşmak', sıfat 'bozuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: masanın bozuk ayağı yüzünden masa sallanıyordu | buzdan sağlam bir ayak yapıp masayı düzeltti
@tohum: elsa-0173
@degisim: gömlek -> masa
Elsa ile Anna karlı ormanda ilk kar için küçük bir kutlama hazırlıyordu. Anna saraydan küçük bir masa ve bir tabak kurabiye getirmişti. Ama masanın bir ayağı bozuktu ve masa sallanıyordu. Kurabiyeler tabakta kayıyordu. "Elsa, kurabiyeler düşecek!" dedi Anna. "Gel, yardımlaşalım," dedi Elsa. Anna masayı iki eliyle tuttu. Elsa eski ayağın yanına buzdan sağlam bir ayak yaptı. Masa artık hiç sallanmadı. Anna kurabiyeleri masanın ortasına dizdi. Sonra Elsa masanın üstüne küçük kar yıldızları yağdırdı. "Elsa, bu en güzel kar kutlaması!" dedi Anna.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Elsa masanın üstüne küçük kar yıldızları yağdırdı"
   - Cümle 11: «Sonra Elsa masanın üstüne küçük kar yıldızları yağdırdı.»
   - Açıklama: Kartın buz ve kar özelliği bir kez yerine ikinci kez kullanılıyor.
   - Açıklama: Buz ve kar özelliği bir kez yerine iki kez kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0173` birebir aynı, `@degisim: gömlek -> masa` (tutuyorsan), ardından `@onarim: 560c823a30876722b9dd02c0a4c9a51e5cdc9340`, sonra gövde.

### Hikâye 7: tohum elsa-0174 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0174
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tabure', fiil 'ölçmek', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: hızlı koşarken tabureye çarptı ve buzlar düştü | özür diledi ve buzları toplayıp yeniden dizdi
@tohum: elsa-0174
Bir sabah Kristoff ormanda taburenin üstündeki buz parçalarını ölçüyordu. Elsa onun yanına çok hızlı koştu ve tabureye çarptı. Tabure devrildi ve buz parçaları karın içine düştü. Kristoff şaşırdı ve karda duran parçalara baktı. Elsa hemen onun yanına eğildi ve özür diledi. Sonra Kraliçe Elsa, Kristoff'a ölçmek için hazır beklemesini işaret etti. Kristoff başını salladı ve bekledi. Elsa buz parçalarını kardan tek tek topladı. Hepsini yeniden yerine dizdi. Kristoff her parçayı yeniden ölçtü ve hiçbiri kırılmamıştı. Sonra ikisi işlerine mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kristoff'a ölçmek için hazır beklemesini işaret etti"
   - Cümle 6: «Sonra Kraliçe Elsa, Kristoff'a ölçmek için hazır beklemesini işaret etti.»
   - Açıklama: Cümle bozuk kurulmuş; 'ölçmek için hazır beklemesini işaret etmek' dilbilgisel ve anlaşılır değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hazır beklemesini işaret etti"
   - Cümle 6: «Sonra Kraliçe Elsa, Kristoff'a ölçmek için hazır beklemesini işaret etti.»
   - Açıklama: 'Beklemesini işaret etti' dilbilgisel olarak bozuk; 'beklemesi için işaret etti' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra Kraliçe Elsa, Kristoff'a"
   - Cümle 6: «Sonra Kraliçe Elsa, Kristoff'a ölçmek için hazır beklemesini işaret etti.»
   - Açıklama: Önceden tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa yeni bir unvanla yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Kraliçe Elsa, Kristoff'a ölçmek"
   - Cümle 6: «Sonra Kraliçe Elsa, Kristoff'a ölçmek için hazır beklemesini işaret etti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın 'özellikler' alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Kartın özellikler alanındaki kraliçelik yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hepsini yeniden yerine dizdi"
   - Cümle 9: «Hepsini yeniden yerine dizdi.»
   - Açıklama: Tabure devrilmişken hiç kaldırılmadan buzlar yeniden yerine diziliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0174` birebir aynı, ardından `@onarim: 340e617b782f43de4efb3b5dc015bb1ab38e7896`, sonra gövde.

### Hikâye 8: tohum elsa-0175 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0175
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'domates', fiil 'okşamak', sıfat 'umutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: domates sepeti çok ağırdı ve kızak yolda geri kaydı | arkadaşından yardım istedi ve kızağı birlikte yukarı çektiler
@tohum: elsa-0175
Elsa ile Olaf karlı dağda yukarı yürüyordu. Elsa'nın elindeki domates sepeti çok ağırdı. Sepeti tepedeki buz sarayına taşıyıp çorba yapacaklardı. Elsa elini salladı ve buzdan küçük bir kızak yaptı. Sepeti kızağa koydu ve kızağı önden çekti. Ama kızak dik yolda durmadan geri kaydı. Elsa, Olaf'a umutlu bir yüzle baktı. "Olaf, kızağı arkadan itip bana yardım eder misin?" diye sordu Elsa. "Tabii, yardım etmeyi çok severim!" dedi Olaf. Olaf kızağı arkadan itti, Elsa da önden çekti. Kızak yavaş yavaş yukarı çıktı ve sarayın kapısına geldi. Elsa gülümsedi ve Olaf'ın başını okşadı. Elsa çok sevindi, çünkü yardım istediği için domatesler saraya gelmişti.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kızak dik yolda durmadan geri kaydı"
   - Cümle 6: «Ama kızak dik yolda durmadan geri kaydı.»
   - Açıklama: Plandaki asıl sorun olan kızağın geri kayması ilk 3 cümlede değil ancak 6. cümlede ortaya çıkıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf'a umutlu bir yüzle baktı"
   - Cümle 7: «Elsa, Olaf'a umutlu bir yüzle baktı.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir ifade, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "umutlu bir yüzle baktı"
   - Cümle 7: «Elsa, Olaf'a umutlu bir yüzle baktı.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir ifade; 3 yaşındaki çocuk için uygun değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Olaf kızağı arkadan itti"
   - Cümle 10: «Olaf kızağı arkadan itti, Elsa da önden çekti.»
   - Açıklama: Dik yolda geri kayan yüklü kızağı arkadan itmek çocuğun taklit edince ezilebileceği tehlikeli bir davranış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "domatesler saraya gelmişti"
   - Cümle 13: «Elsa çok sevindi, çünkü yardım istediği için domatesler saraya gelmişti.»
   - Açıklama: Domatesler kendi gelmez; fiil öznesine uymuyor, 'getirilmişti' olmalı.
   - Açıklama: Domatesler kendiliğinden gelmez; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0175` birebir aynı, ardından `@onarim: 506bd31f6696cf52664b5ecc09bcc44506de4b79`, sonra gövde.

### Hikâye 9: tohum elsa-0176 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0176
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'cetvel', fiil 'değmek', sıfat 'küçücük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: geyiğin başı alçak bir dala takıldı | durmasını söyledi ve küçük dalı kenara itti
@tohum: elsa-0176
@degisim: cetvel -> dal
Rüzgar hafifçe esiyordu. Elsa karlı ormanda Sven'i arıyordu. Sven'in başı iki ağacın arasındaki alçak bir dala takılmıştı. Sven başını çekti ama kurtulamadı. Dal her seferinde Sven'in başına değiyordu. Elsa hemen yanına koştu. Sonra bir kraliçe gibi açık bir sesle konuştu. "Sven, dur ve başını yavaşça aşağı indir," dedi Elsa. Sven hemen durdu ve başını indirdi. Elsa küçücük bir dalı eliyle kenara itti. Sven'in başı daldan kolayca çıktı. Sven sevinçle zıpladı ve Elsa'nın yanına geldi. "Aferin, Sven, beni çok güzel dinledin!" dedi Elsa.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sven'in başı iki ağacın arasındaki alçak bir dala takılmıştı"
   - Cümle 3: «Sven'in başı iki ağacın arasındaki alçak bir dala takılmıştı.»
   - Açıklama: Sven'in başının dala neden takıldığı söylenmiyor ve küçücük bir dalın onu tutması akla yatkın değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kraliçe gibi açık bir sesle"
   - Cümle 7: «Sonra bir kraliçe gibi açık bir sesle konuştu.»
   - Açıklama: 'Kraliçe gibi' benzetmesi ve 'açık ses' mecazlı anlatım 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Kraliçe gibi açık bir sesle' benzetmesi soyut ve küçük çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir kraliçe gibi açık bir sesle konuştu"
   - Cümle 7: «Sonra bir kraliçe gibi açık bir sesle konuştu.»
   - Açıklama: Kartın özellikler alanında kraliçelik kız kardeşini korumak olarak verilmiş; buyurucu ses olarak kullanımı kartta yok.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra bir kraliçe gibi açık bir sesle konuştu"
   - Cümle 7: «Sonra bir kraliçe gibi açık bir sesle konuştu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız benzetme olarak geçiyor ve kartındaki koruma anlamıyla çözümü taşımıyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa küçücük bir dalı eliyle kenara itti"
   - Cümle 10: «Elsa küçücük bir dalı eliyle kenara itti.»
   - Açıklama: Sven'in kurtulamadığı dal küçücük bir dal olarak anlatılıyor; bir geyiği tutan dalın küçücük olması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0176` birebir aynı, `@degisim: cetvel -> dal` (tutuyorsan), ardından `@onarim: 62eba2a3f575b82cf2b1cc8dc93bf5a0d5c289fa`, sonra gövde.

### Hikâye 10: tohum elsa-0177 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0177
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'sofra', fiil 'şakalaşmak', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kardeşini gıdıkladı ve elmalar yere düştü | özür diledi ve elmaları toplayıp tepsiyi kendisi taşıdı
@tohum: elsa-0177
Dağdaki buz sarayında Elsa ile Anna sofra kuruyordu. Anna ağır bir elma tepsisi taşırken Elsa onunla şakalaştı ve onu gıdıkladı. Anna güldü, tepsi sallandı ve elmalar yere yuvarlandı. Anna üzüldü ve yerdeki elmalara baktı. Elsa elmaların kendi yüzünden düştüğünü anladı. Hemen kardeşinden özür diledi ve ona sarıldı. Sonra Elsa, kraliçe olarak Anna'ya oturup dinlenmesini söyledi. Anna oturdu ve Elsa'yı izledi. Elsa elmaları tek tek topladı ve tepsiye koydu. Ağır tepsiyi de kendisi sofraya taşıdı. Anna gülümsedi ve Elsa'ya bir elma uzattı. Elsa bundan sonra kardeşi ağır bir şey taşırken onu gıdıklamadı.
```

**Hakem bulguları (4):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "özür diledi ve elmaları toplayıp tepsiyi kendisi taşıdı"
   - Cümle 0 (plan satırı): «kardeşini gıdıkladı ve elmalar yere düştü | özür diledi ve elmaları toplayıp tepsiyi kendisi taşıdı»
   - Açıklama: Çözüm özür dilemek, elmaları toplamak ve tepsiyi taşımak olmak üzere iki adımdan uzun sürüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "elmaların kendi yüzünden düştüğünü"
   - Cümle 5: «Elsa elmaların kendi yüzünden düştüğünü anladı.»
   - Açıklama: 'kendi yüzünden' kalıp anlatım 3 yaşındaki çocuğa uygun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa, kraliçe olarak Anna'ya"
   - Cümle 7: «Sonra Elsa, kraliçe olarak Anna'ya oturup dinlenmesini söyledi.»
   - Açıklama: 'kraliçe olarak' ifadesi bu bağlamda anlamsız ve yersiz.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa, kraliçe olarak Anna'ya"
   - Cümle 7: «Sonra Elsa, kraliçe olarak Anna'ya oturup dinlenmesini söyledi.»
   - Açıklama: 'kraliçe olarak' soyut bir rol ifadesi, küçük çocuğa uygun değil ve olaya bir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0177` birebir aynı, ardından `@onarim: 1c99f48a19ff6dfe19bf1b30d10c0a8f7357d859`, sonra gövde.

### Hikâye 11: tohum elsa-0178 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0178
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kavun', fiil 'yatırmak', sıfat 'aydınlık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kavun çok hızlı gitti ve aşağı kaçtı | buzdan alçak bir duvar yapıp kavunu durdurdu
@tohum: elsa-0178
Orman bugün çok aydınlıktı. Elsa ile Olaf, kara koydukları üç dalı kavunla yatırmaya çalışıyordu. Ama Olaf kavunu çok hızlı itti ve kavun aşağı kaçtı. "Kavun kaçıyor!" diye bağırdı Olaf. Elsa hemen ellerini uzattı. Yolun altında buzdan alçak bir duvar yaptı. Kavun duvara hafifçe çarptı ve durdu. Olaf koşup kavunu aldı ve güldü. "Bu sefer yavaş yapacağım," dedi Olaf. Olaf kavunu yavaşça itti ve üç dal birden kara yattı. "Hepsi yattı!" dedi Olaf sevinçle. Elsa gülerek onu alkışladı. Elsa ile Olaf bundan sonra kavunu hep yavaş itti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kara koydukları üç dalı kavunla yatırmaya çalışıyordu"
   - Cümle 2: «Elsa ile Olaf, kara koydukları üç dalı kavunla yatırmaya çalışıyordu.»
   - Açıklama: Ormanda karda kavunla dal devirme oyunu saçma ve akla yatkın olmayan bir olay kuruyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yolun altında buzdan alçak"
   - Cümle 6: «Yolun altında buzdan alçak bir duvar yaptı.»
   - Açıklama: Kavun yolun aşağısına kaçıyor; duvarın 'yolun altında' yapılması anlamca yanlış, 'yolun sonunda' olmalı.
   - Açıklama: 'Yolun altında' yanlış; kavunun kaçtığı yerin aşağısı kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0178` birebir aynı, ardından `@onarim: 76567e17049bc02974dcfc4d44dc8f213fba7d0c`, sonra gövde.

### Hikâye 12: tohum elsa-0180 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0180
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: bir şey yapmak
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'mücevher', fiil 'kaybetmek', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: sarayı gösteren tahta kirliydi ve ok görünmüyordu | tahtayı karla sildi ve üstüne mavi bir mücevher koydu
@tohum: elsa-0180
Bir sabah Elsa karlı ormanda yürüyordu. Yolun başında sarayı gösteren eski bir tahta vardı. Ama tahta çok kirliydi ve üstündeki ok görünmüyordu. Böyle kalırsa ormana gelenler yolu kaybederdi. Elsa önce temiz karla tahtayı iyice sildi. Ok yeniden göründü ama Elsa tahtanın uzaktan da görünmesini istedi. Elsa'nın kraliçe kolyesinde mavi bir mücevher vardı. Mücevheri çıkardı ve tahtanın tepesindeki küçük deliğe koydu. Güneş vurunca mücevher uzaktan parladı. Elsa birkaç adım geri gitti ve tahtaya baktı. Temiz ok ve mavi ışık ağaçların arasından görünüyordu. Elsa çok sevindi, çünkü artık herkes sarayı kolayca bulacaktı.
```

**Hakem bulguları (5):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Elsa tahtanın uzaktan da görünmesini istedi"
   - Cümle 6: «Ok yeniden göründü ama Elsa tahtanın uzaktan da görünmesini istedi.»
   - Açıklama: Ok göründükten sonra tahtanın uzaktan görünmesi diye ikinci bir sorun açılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa'nın kraliçe kolyesinde mavi bir mücevher vardı"
   - Cümle 7: «Elsa'nın kraliçe kolyesinde mavi bir mücevher vardı.»
   - Açıklama: Kraliçe özelliği karttaki 'kız kardeşini korur' biçiminde değil, bir kolye eşyası olarak kullanılıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Elsa'nın kraliçe kolyesinde mavi bir mücevher vardı"
   - Cümle 7: «Elsa'nın kraliçe kolyesinde mavi bir mücevher vardı.»
   - Açıklama: Kartta Elsa'nın mücevherli kolyesi gibi bir eşya yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tahtanın tepesindeki küçük deliğe"
   - Cümle 8: «Mücevheri çıkardı ve tahtanın tepesindeki küçük deliğe koydu.»
   - Açıklama: Mücevherin tam oturacağı delik önceden kurulmadan çözüme uygun biçimde beliriyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tahtanın tepesindeki küçük deliğe koydu"
   - Cümle 8: «Mücevheri çıkardı ve tahtanın tepesindeki küçük deliğe koydu.»
   - Açıklama: Mücevherin sığacağı delik önceden kurulmadan çözüme uygun biçimde beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0180` birebir aynı, ardından `@onarim: 366570237543eb1b6b896467b1972ec94381d405`, sonra gövde.
