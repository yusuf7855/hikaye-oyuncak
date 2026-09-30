# Editör görevi (onarım): Maşa, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar32.txt --ad urun_v2`
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

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0115 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0115
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yağmur ya da kar günü
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'karabiber', fiil 'sormak', sıfat 'kalın'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: kar çok kuruydu ve kar topları dağıldı | tepenin güneşli yanındaki ıslak karı denedi
@tohum: masa-0115
@degisim: karabiber -> dal
Bir sabah tepede kalın bir kar vardı. Maşa ile Koca Ayı kardan bir ayı yapmak istedi. Ama kar çok kuruydu ve kar topları hemen dağıldı. Maşa hemen başka bir yer denedi. Tepenin güneşli yanına koştu ve bir avuç kar aldı. Bu kar biraz ıslaktı ve kolayca top oldu. "Koca Ayı, bu karla büyük toplar yapalım mı?" diye sordu Maşa. Koca Ayı başını salladı. İkisi birlikte büyük kar topları yuvarladı ve üst üste koydu. Bu kez kardan ayı hiç dağılmadı. Sonra Koca Ayı yerden iki dal aldı ve kardan ayıya kol yaptı. Maşa çok sevindi, çünkü kardan ayıyı sonunda yapabilmişti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Maşa hemen başka bir yer"
   - Cümle 4: «Maşa hemen başka bir yer denedi.»
   - Açıklama: 'Hemen' art arda iki cümlede gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0115` birebir aynı, `@degisim: karabiber -> dal` (tutuyorsan), ardından `@onarim: 93bfa0f13cc8de63bd1cb3978101378200583fa5`, sonra gövde.

### Hikâye 2: tohum masa-0117 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi, Daşa
@tohum: masa-0117
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'buket', fiil 'toplanmak', sıfat 'memnun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi, Daşa
@plan: reçel kavanozunun kapağı çok sıkıydı | kuzeninden yardım isteyip kapağı birlikte açtı
@tohum: masa-0117
@degisim: buket -> kavanoz
Bir sabah Maşa bahçede kirpi ile Daşa için kahvaltı masası hazırlıyordu. Masada ekmek, elmalar ve bir kavanoz çilek reçeli vardı. Maşa ekmeğine reçel sürmek istedi, ama kavanozun kapağı çok sıkıydı. Tam o sırada kuzeni Daşa bahçeye geldi. "Daşa, kapak açılmıyor, bana yardım eder misin?" diye sordu Maşa. Daşa kavanozu sıkıca tuttu. Maşa kapağı çevirdi. Bu kez kapak "pıt" diye açıldı. Kirpi de çitin altından masaya geldi. Maşa ona küçük bir elma verdi ve kirpi çok memnun oldu. Sonra hepsi masanın başında toplandı ve mutlu mutlu kahvaltı yaptı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Tam o sırada kuzeni Daşa bahçeye geldi"
   - Cümle 4: «Tam o sırada kuzeni Daşa bahçeye geldi.»
   - Açıklama: Daşa ilk cümlede zaten geçmişken burada 'kuzeni Daşa' diye yeniden tanıtılıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kuzeni Daşa bahçeye geldi"
   - Cümle 4: «Tam o sırada kuzeni Daşa bahçeye geldi.»
   - Açıklama: Daşa birinci cümlede zaten anılmışken burada yeniden tanıtılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kirpi de çitin altından masaya geldi"
   - Cümle 9: «Kirpi de çitin altından masaya geldi.»
   - Açıklama: Kirpi ve elma bölümü kapak sorunuyla ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0117` birebir aynı, `@degisim: buket -> kavanoz` (tutuyorsan), ardından `@onarim: 64acaa6c10d5fd49c322d1fdc616303df6396962`, sonra gövde.

### Hikâye 3: tohum masa-0118 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0118
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'iplik', fiil 'yakalanmak', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: uçurtmanın ipliği bahçedeki bir çalıya takıldı | çekmeyi bırakıp ipliği dallardan yavaşça çözdü
@tohum: masa-0118
@degisim: yakalanmak -> takılmak
Bahçede hafif bir rüzgar esiyordu. Maşa ince ve kırılgan çubuklardan yapılmış bir uçurtma uçuruyordu. Birden rüzgar döndü ve uçurtmanın ipliği bahçedeki bir çalıya takıldı. Maşa ipliği çekti ama uçurtma çalıdan çıkmadı. Uçurtmanın çubukları eğildi ve neredeyse kırılacaktı. Maşa hemen durdu ve başka bir yol denedi. Çalının yanına yürüdü ve ipliği dallardan tek tek çözdü. Sonra uçurtmayı iki eliyle yavaşça dışarı aldı. Çubukların hiçbiri kırılmamıştı. Maşa bahçenin ortasına koştu ve uçurtmayı yeniden havaya kaldırdı. Uçurtma rüzgarla yükseldi ve Maşa sevinçle güldü. Maşa bundan sonra uçurtmasını hep çalılardan uzakta uçurdu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kırılgan çubuklardan yapılmış"
   - Cümle 2: «Maşa ince ve kırılgan çubuklardan yapılmış bir uçurtma uçuruyordu.»
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başka bir yol denedi"
   - Cümle 6: «Maşa hemen durdu ve başka bir yol denedi.»
   - Açıklama: 'Başka bir yol denemek' mecazlı ve soyut bir anlatım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hemen durdu ve başka bir yol denedi"
   - Cümle 6: «Maşa hemen durdu ve başka bir yol denedi.»
   - Açıklama: 'Başka bir yol denemek' yöntem anlamında mecazlı bir anlatım, küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0118` birebir aynı, `@degisim: yakalanmak -> takılmak` (tutuyorsan), ardından `@onarim: 5ef1f84fe8a485c4abb471bf51deb6b8f8bbb963`, sonra gövde.

### Hikâye 4: tohum masa-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0120
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'küp', fiil 'doldurmak', sıfat 'açık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: patikadaki çilekler yeşildi | güneşli açık yeri fark edip kırmızı çilek topladı
@tohum: masa-0120
Hafif bir rüzgar esiyordu ve güneş ormanı ısıtıyordu. Maşa elinde küçük bir küple patikada yürüyordu. Reçel için küpü doldurmak istedi, ama patikadaki çilekler yeşildi. Maşa etrafa dikkatle baktı ve bir şey fark etti. Ağaçların altındaki çilekler yeşildi, ama güneşte olan çilekler kırmızıydı. Maşa ağaçların arasındaki açık bir yere koştu. Burası güneşliydi ve çimenlerde bir sürü kırmızı çilek vardı. Maşa en kırmızı çilekleri tek tek topladı ve küpe koydu. Az sonra küp doldu. Maşa dolu küpü kucakladı ve mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Reçel için küpü doldurmak istedi"
   - Cümle 3: «Reçel için küpü doldurmak istedi, ama patikadaki çilekler yeşildi.»
   - Açıklama: Tohumdaki reçel özelliği yalnız niyet olarak anılıyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0120` birebir aynı, ardından `@onarim: de24cb744134afa00fc8d8132b08d281cbdc2e38`, sonra gövde.

### Hikâye 5: tohum masa-0122 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0122
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kabak', fiil 'yoğurmak', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: fındıklar kaygan tatlının üstünden yere yuvarlandı | tatlıya reçel sürüp fındıkları üstüne dizdi
@tohum: masa-0122
@degisim: yoğurmak -> süslemek
Bir sabah Maşa'nın kuzeni Daşa şehirden ziyarete gelecekti. Maşa ormanda kütüğün üstüne bir tabak kabak tatlısı koydu. Yanına en sevdiği çilek reçelini de koydu. Tatlıyı fındıklarla süslemek istedi, ama tatlı kaygandı ve fındıklar hep yere yuvarlandı. Simsiyah gözlü sincap düşen fındıkları tek tek geri getirdi. Maşa tatlının üstüne ince ince reçel sürdü. Sonra fındıkları reçelin üstüne güzelce dizdi. Bu kez fındıklar reçele yapıştı ve hiç düşmedi. Tam o sırada Daşa patikadan geldi. Maşa sevinçle kütüğü gösterdi. Daşa süslü tatlıyı görünce güldü ve Maşa'ya sarıldı. Maşa çok sevindi, çünkü sürprizi Daşa gelmeden hazır olmuştu.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Tatlıyı fındıklarla süslemek istedi, ama tatlı kaygandı ve fındıklar hep yere yuvarlandı.»
   - Açıklama: İlk üç cümle ziyareti ve hazırlığı anlatıyor; fındık sorunu ancak dördüncü cümlede geliyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "fındıklar hep yere yuvarlandı"
   - Cümle 4: «Tatlıyı fındıklarla süslemek istedi, ama tatlı kaygandı ve fındıklar hep yere yuvarlandı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü sürprizi Daşa gelmeden hazır olmuştu"
   - Cümle 12: «Maşa çok sevindi, çünkü sürprizi Daşa gelmeden hazır olmuştu.»
   - Açıklama: Belirtme durumundaki 'sürprizi' geçişsiz 'hazır olmuştu' ile uyumsuz; 'sürprizi hazırdı' ya da 'sürpriz hazır olmuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0122` birebir aynı, `@degisim: yoğurmak -> süslemek` (tutuyorsan), ardından `@onarim: cc989a146ae74e2e8ac8d9447bcf5f65c08c3759`, sonra gövde.

### Hikâye 6: tohum masa-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0123
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'sebze', fiil 'dizmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: üstteki kar topuna takılan havuç ağırdı ve düştü | sepetten hafif bir turp alıp burun yaptı
@tohum: masa-0123
Kar yavaş yavaş yağıyordu. Maşa tepede iki kocaman kar topunu üst üste koymuştu. Üstteki topa uzun bir havuç taktı ama havuç ağırdı ve hemen düştü. Maşa havucu bir daha taktı ama o yine düştü. Maşa sebze sepetine baktı ve başka bir şey denedi. Sepetten küçük bir turp aldı ve havucun yerine taktı. Turp hafifti ve yerinde kaldı. Sonra turpun altına küçük fasulyeleri bir gülümseme gibi dizdi. Kar topunun artık güzel bir yüzü vardı. Maşa uzun havucu da kendisi yedi ve güldü. Maşa bundan sonra burun için hep hafif bir sebze seçti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa sebze sepetine baktı"
   - Cümle 5: «Maşa sebze sepetine baktı ve başka bir şey denedi.»
   - Açıklama: Tepede daha önce hiç kurulmamış bir sebze sepeti tam çözüm gerektiğinde sebepsizce beliriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "fasulyeleri bir gülümseme gibi dizdi"
   - Cümle 8: «Sonra turpun altına küçük fasulyeleri bir gülümseme gibi dizdi.»
   - Açıklama: Benzetme (gülümseme gibi) mecazlı bir anlatım; küçük çocuk için somut değil.
   - Açıklama: 'Bir gülümseme gibi' benzetmesi küçük çocuk için mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0123` birebir aynı, ardından `@onarim: a63dc01cfefce0e86ed072f12d7a0d61253fd267`, sonra gövde.

### Hikâye 7: tohum masa-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0124
- yer: dağ (Ormanın yanındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'maske', fiil 'atlamak', sıfat 'çabuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: büyük maske zıplayan kızın gözlerine kaydı | maskeyi yüzünden alıp başının üstüne taktı
@tohum: masa-0124
Tepedeki yumuşak çimenlerde Maşa zıplama oyunu oynuyordu. Yüzünde kağıttan, uzun kulaklı bir maske vardı. Maşa ağaca kadar atlayarak gitmek istiyordu. Ama maske büyüktü. Maşa zıplayınca maske gözlerinin üstüne kaydı. Maşa önünü göremedi ve durdu. Koca Ayı ile kirpi merakla ona baktı. Maşa hemen yeni bir şey denedi. Maskeyi yüzünden aldı ve başının üstüne taktı. Şimdi maskenin kulakları yukarıdaydı ve Maşa her yeri görüyordu. "Koca Ayı, kirpi, haydi benimle zıplayın!" dedi Maşa. Maşa çabuk çabuk zıplayarak ağaca ilk vardı. Koca Ayı ağır ağır, kirpi de küçük adımlarla arkasından geldi. Sonra üçü ağacın altında zıplama oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama maske büyüktü"
   - Cümle 4: «Ama maske büyüktü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü ve beşinci cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Maşa zıplayınca maske gözlerinin üstüne kaydı"
   - Cümle 5: «Maşa zıplayınca maske gözlerinin üstüne kaydı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü ve beşinci cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0124` birebir aynı, ardından `@onarim: 7449e7934c8802fd64db3e3ed24cc7adff81a549`, sonra gövde.

### Hikâye 8: tohum masa-0126 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0126
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'hediye', fiil 'saklamak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: ayı hediyeyi saklamak istedi ama kirpi hep peşindeydi | kozalak yuvarladı ve kirpiyle oynadı
@tohum: masa-0126
Bir sabah Maşa ormanda Koca Ayı'yı gördü. Koca Ayı'nın elinde kirpi için bir hediye vardı, kırmızı bir elma. Ayı elmayı saklamak istiyordu ama oynak kirpi hep peşinden koşuyordu. Koca Ayı durdu ve üzgün üzgün Maşa'ya baktı. Maşa hemen yeni bir oyun denedi. Yerden bir kozalak aldı ve patikada yavaşça yuvarladı. Kirpi sevinçle kozalağı kovaladı. O sırada Koca Ayı elmayı yaprakların altına sakladı. Biraz sonra kirpi geri geldi ve burnuyla yaprakları kokladı. Kırmızı elmayı buldu ve mutlu mutlu yemeye başladı. Koca Ayı da Maşa'ya sarıldı. Maşa bundan sonra Koca Ayı sürpriz hazırlarken ona hep böyle yardım etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ayı elmayı saklamak istiyordu"
   - Cümle 3: «Ayı elmayı saklamak istiyordu ama oynak kirpi hep peşinden koşuyordu.»
   - Açıklama: Hediyeyi alacak kirpiden neden saklamak gerektiği söylenmiyor ve kirpi elmayı hemen bulunca saklamanın anlamı kalmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0126` birebir aynı, ardından `@onarim: 3cfddf116d84a12fc8032e90bd780f2c3c0ba5a8`, sonra gövde.

### Hikâye 9: tohum masa-0127 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap
@tohum: masa-0127
- yer: dağ (Ormanın yanındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'elmas', fiil 'asmak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap
@plan: fındıklar kuru ekmekten yere kaydı | ekmeğe reçel sürdü ve fındıkları yapıştırdı
@tohum: masa-0127
@degisim: elmas -> kurdele
Maşa tepede hareketli sincap için bir sürpriz hazırlıyordu. Bir dilim ekmeğin üstüne fındık koymak istedi. Ama ekmek kuruydu ve yuvarlak fındıklar hemen yere kaydı. Maşa fındıkları topladı ve biraz düşündü. Sonra çantasından sevdiği reçel kavanozunu çıkardı. Ekmeğe kalın bir kat reçel sürdü ve fındıkları üstüne bastırdı. Fındıklar bu kez yapıştı ve hiç düşmedi. Maşa sincap sürprizi görsün diye bir dala kırmızı bir kurdele astı. Sincap kurdeleyi görünce hemen yanına koştu. "Bu senin için, sincap!" dedi Maşa. Sincap fındıkları tek tek yedi ve kuyruğunu salladı. Maşa bundan sonra fındıkları ekmeğe hep reçelle yapıştırdı.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Maşa sincap sürprizi görsün"
   - Cümle 8: «Maşa sincap sürprizi görsün diye bir dala kırmızı bir kurdele astı.»
   - Açıklama: Virgül eksik; 'sincap sürprizi' tamlama gibi okunuyor, 'Maşa, sincap sürprizi görsün diye' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "görünce hemen yanına koştu"
   - Cümle 9: «Sincap kurdeleyi görünce hemen yanına koştu.»
   - Açıklama: 'Yanına' zamirinin kurdeleyi mi Maşa'yı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0127` birebir aynı, `@degisim: elmas -> kurdele` (tutuyorsan), ardından `@onarim: 0633e3bd6d0ea89862210c6f1a762b30aed17d50`, sonra gövde.

### Hikâye 10: tohum masa-0129 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0129
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'topaç', fiil 'kopmak', sıfat 'ıslak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: kopan bir dal sincabın yuvasını kapattı | ipi dala bağladı ve dalı birlikte çektiler
@tohum: masa-0129
Bir sabah Maşa ile kuzeni Daşa ormanda topaç çeviriyordu. Birden rüzgarda küçük bir dal koptu ve bir ağacın dibine düştü. Dal, bir sincabın yuvasının önünü kapattı ve sincap dışarı çıkamadı. Maşa ile Daşa dalı çekmeye çalıştı. "Dal çok ıslak, elimden kayıyor," dedi Daşa. Maşa hemen yeni bir şey denedi. Cebinden topaç ipini çıkardı ve dalın ucuna sıkıca bağladı. İki kız ipi birlikte çekti ve dal yavaş yavaş kaydı. Yuvanın önü açıldı ve sincap zıplayarak dışarı çıktı. Sincap kuyruğunu salladı ve bir ağacın dalına koştu. "Yaşasın, Daşa, sincap artık dışarıda!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Dal çok ıslak, elimden kayıyor"
   - Cümle 5: «"Dal çok ıslak, elimden kayıyor," dedi Daşa.»
   - Açıklama: Küçük bir dal için iki kız yetmiyor ve yağmur olmadığı halde dal ıslak deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0129` birebir aynı, ardından `@onarim: 9306d4d52db9a4dd5e719723165701226965d4cd`, sonra gövde.

### Hikâye 11: tohum masa-0130 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0130
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'şapka', fiil 'gitmek', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: kız koşarken kelebekler uçup gitti | şapkaya çiçek koydu ve sessizce bekledi
@tohum: masa-0130
Maşa şapkasıyla ormandaki patikada yürüyordu. Birden küçük sarı kelebekler gördü ve onlara yakından bakmak istedi. Ama Maşa yanlarına koşarken kelebekler hemen uçup gitti. Maşa durdu ve başka bir yol denedi. Patikanın kenarından birkaç çiçek topladı ve şapkasına koydu. Sonra şapkayı çimenlere bıraktı ve yanına sessizce oturdu. Maşa hiç kıpırdamadan bekledi. Biraz sonra küçük kelebekler geri geldi ve çiçeklerin üstüne kondu. Maşa onları bu kez çok yakından gördü. Maşa kelebekleri uzun uzun izledi ve mutlu mutlu gülümsedi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başka bir yol denedi"
   - Cümle 4: «Maşa durdu ve başka bir yol denedi.»
   - Açıklama: 'Yol denemek' mecazlı kullanım; 3 yaşındaki çocuk patikadaki yol sanabilir.
   - Açıklama: 'Yol' burada yöntem anlamında mecazlı; patikada yürüyen bir hikayede çocuğu şaşırtır.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Biraz sonra küçük kelebekler geri geldi"
   - Cümle 8: «Biraz sonra küçük kelebekler geri geldi ve çiçeklerin üstüne kondu.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, olayın merkezinde yer alıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "küçük kelebekler geri geldi"
   - Cümle 8: «Biraz sonra küçük kelebekler geri geldi ve çiçeklerin üstüne kondu.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün parçası olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0130` birebir aynı, ardından `@onarim: 777a70121d54e6d0b59ae456b84ff4eccab4c3d4`, sonra gövde.

### Hikâye 12: tohum masa-0131 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0131
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'fasulye', fiil 'planlamak', sıfat 'ferah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: ayı ile kirpi aşağıda çiçek topluyordu ve bulutu görmedi | ekmeğe reçel sürdü ve onları tepeye çağırdı
@tohum: masa-0131
@degisim: fasulye -> çiçek
Maşa tepede ferah bir çimenlikte piknik yapıyordu. Birden gökyüzünde kalp şeklinde kocaman bir bulut fark etti. Ama Koca Ayı ile kirpi aşağıda çiçek topluyordu ve gökyüzüne hiç bakmıyordu. Maşa onları yukarı getirmeyi planladı. Kavanozunu açtı ve üç dilim ekmeğe bol bol reçel sürdü. "Koca Ayı, kirpi, ekmekler hazır!" diye seslendi Maşa. Koca Ayı çiçekleri bıraktı ve kirpiyle birlikte tepeye geldi. "Bakın, kalp şeklinde bir bulut!" dedi Maşa ve gökyüzünü gösterdi. Koca Ayı ile kirpi yukarı baktı ve sevinçle ses çıkardı. Üçü ferah çimenlikte ekmeklerini yiyip bulutu mutlu mutlu izledi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tepede ferah bir çimenlikte"
   - Cümle 1: «Maşa tepede ferah bir çimenlikte piknik yapıyordu.»
   - Açıklama: 'Ferah' küçük çocuğun bilmeyeceği soyut bir sıfat.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa tepede ferah bir çimenlikte"
   - Cümle 1: «Maşa tepede ferah bir çimenlikte piknik yapıyordu.»
   - Açıklama: 'Ferah' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa onları yukarı getirmeyi planladı"
   - Cümle 4: «Maşa onları yukarı getirmeyi planladı.»
   - Açıklama: 'Planladı' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "üç dilim ekmeğe bol bol reçel sürdü"
   - Cümle 5: «Kavanozunu açtı ve üç dilim ekmeğe bol bol reçel sürdü.»
   - Açıklama: Sorun arkadaşların gökyüzüne bakmaması iken Maşa onlara bakmalarını söylemek yerine dolaylı yoldan ekmek hazırlayıp çağırıyor.
   - Açıklama: Sorun onların gökyüzüne bakmaması iken Maşa onları doğrudan buluta çağırmak yerine dolambaçlı bir ekmek hazırlığına giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0131` birebir aynı, `@degisim: fasulye -> çiçek` (tutuyorsan), ardından `@onarim: a5d896a26d46b2d3c4d603319492e24f4c526367`, sonra gövde.
