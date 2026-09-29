# Editör görevi (onarım): Maşa, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0030 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0030
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'gözlük', fiil 'köpürmek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: çimenlerde bir şey parladı ama yakından görünmedi | ilk durduğu yere dönüp oradan baktı ve yürüdü
@tohum: masa-0030
@degisim: köpürmek -> parlamak
Maşa tepede koşup oynuyordu. Birden uzun çimenlerin arasında bir şey parladı. Maşa hemen oraya koştu ama çimenler çok sıktı ve hiçbir şey göremedi. Maşa ilk durduğu yere döndü ve oradan bakmayı denedi. Işık yine parladı. Maşa bu kez ışığa bakarak yavaş yavaş yürüdü. Çimenlerin arasında Maşa'nın kayıp pembe oyuncak gözlüğü vardı. Gözlüğün camları güneşte parlıyordu. Maşa gözlüğü eline aldı ve güldü. Maşa çok sevindi, çünkü artık oyuncaklarından hiçbiri eksik değildi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın kayıp pembe oyuncak gözlüğü vardı"
   - Cümle 7: «Çimenlerin arasında Maşa'nın kayıp pembe oyuncak gözlüğü vardı.»
   - Açıklama: Gözlüğün kayıp olduğu önceden hiç kurulmadan sebepsizce ortaya çıkıyor ve son cümledeki eksik oyuncak hedefi de hazırlanmamış.
   - Açıklama: Gözlüğün kayıp olduğu önceden hiç kurulmuyor ve son cümle bu kurulmamış kayba dayanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0030` birebir aynı, `@degisim: köpürmek -> parlamak` (tutuyorsan), ardından `@onarim: 9015c61638e445ecbbbdd5217a24a00d8919c67e`, sonra gövde.

### Hikâye 2: tohum masa-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0031
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yelkenli', fiil 'dağıtmak', sıfat 'şanslı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: rüzgar yelkenliyi yaprakların arasına itti ve yelkenli takıldı | önce üfledi, sonra dalla yaprakları dağıttı
@tohum: masa-0031
@degisim: şanslı -> kırmızı
Rüzgar esiyordu. Maşa patikada, yağmurdan kalan küçük bir suda kırmızı yelkenlisini yüzdürüyordu. Ama rüzgar yelkenliyi yaprakların arasına itti ve yelkenli takıldı. Maşa önce yelkenliye üflemeyi denedi. Ama yelkenli hiç kıpırdamadı. Sonra Maşa yerden ince bir dal aldı. Dalla yaprakları yavaş yavaş dağıttı. Yapraklar bir yana gitti. Yelkenli kurtuldu ve suyun ortasına doğru gitti. Rüzgar yine esti ve yelkenli hızlandı. Maşa sevinçle ellerini çırptı. Maşa bundan sonra yelkenlisini yaprakların olmadığı temiz bir yerde yüzdürdü.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kalan küçük bir suda"
   - Cümle 2: «Maşa patikada, yağmurdan kalan küçük bir suda kırmızı yelkenlisini yüzdürüyordu.»
   - Açıklama: 'Bir suda' yanlış kullanım; 'su birikintisinde' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yağmurdan kalan küçük bir suda"
   - Cümle 2: «Maşa patikada, yağmurdan kalan küçük bir suda kırmızı yelkenlisini yüzdürüyordu.»
   - Açıklama: 'Küçük bir su' yanlış kelime; 'su birikintisi' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yapraklar bir yana gitti"
   - Cümle 8: «Yapraklar bir yana gitti.»
   - Açıklama: Yapraklar kendi başına gitmez; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0031` birebir aynı, `@degisim: şanslı -> kırmızı` (tutuyorsan), ardından `@onarim: ab4ba98a2fa7e87bcc18085cdabcac4e58bf9662`, sonra gövde.

### Hikâye 3: tohum masa-0033 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0033
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çuval', fiil 'giydirmek', sıfat 'masmavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: patikada nereden geldiği bilinmeyen mor lekeler vardı | çuvalın altına baktı ve delikli köşesini bağladı
@tohum: masa-0033
@degisim: giydirmek -> bağlamak
Gökyüzü masmaviydi ve ormanda kuşlar ötüyordu. Maşa patikada reçel için böğürtlen dolu bir çuval taşıyordu. Birden arkasına baktı ve patikada mor lekeler gördü. Maşa bu lekelerin nereden geldiğini çok merak etti. Önce başını kaldırıp dallara baktı. Ama dallarda mor bir şey yoktu. Sonra çuvalını yere koydu ve altına baktı. Orada küçük bir delik vardı. Böğürtlenler bu delikten tek tek düşüp eziliyordu. Maşa çuvalın delikli köşesini sıkıca bağladı. Bu kez yere tek bir tane bile düşmedi. Maşa çok sevindi, çünkü böğürtlenlerini kurtarmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "reçel için böğürtlen dolu"
   - Cümle 2: «Maşa patikada reçel için böğürtlen dolu bir çuval taşıyordu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0033` birebir aynı, `@degisim: giydirmek -> bağlamak` (tutuyorsan), ardından `@onarim: d2b71b4b7f997279c66c33afd8cef32dd45ff1c4`, sonra gövde.

### Hikâye 4: tohum masa-0037 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0037
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'fıskiye', fiil 'güvenmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: top ağaca çarpıp dar bir deliğe düştü | dalın ucuna reçel sürdü ve topu çıkardı
@tohum: masa-0037
@degisim: fıskiye -> top
Maşa ormanda piknik yapıyor ve küçük sarı topuyla oynuyordu. Topu havaya atıyor ve yakalıyordu. Ama top bir ağaca çarptı ve ağacın altındaki dar bir deliğe düştü. Delik karanlıktı ve Maşa'nın eli içine girmiyordu. Maşa piknik sepetindeki tatlı reçele baktı. Reçelin yapışkan olduğunu biliyordu ve ona güvendi. Uzun bir dalın ucuna biraz reçel sürdü. Dalı deliğe soktu ve topa bastırdı. Top reçele yapıştı. Maşa dalı yavaşça çekti ve top dışarı çıktı. Top yapış yapış olmuştu. Maşa güldü ve onu otlara silip temizledi. Maşa bundan sonra topuyla ağaçlardan uzakta, açık bir yerde oynadı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa'nın eli içine girmiyordu"
   - Cümle 4: «Delik karanlıktı ve Maşa'nın eli içine girmiyordu.»
   - Açıklama: Ağaç dibindeki karanlık deliğe el sokmaya çalışmak taklit edilince tehlikeli olabilir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "biliyordu ve ona güvendi"
   - Cümle 6: «Reçelin yapışkan olduğunu biliyordu ve ona güvendi.»
   - Açıklama: Reçele güvenmek fiile uygun değil; 'güvendi' nesnesine yanlış anlamda kullanılmış.
   - Açıklama: Reçele güvenmek kelimenin yanlış ve soyut kullanımı.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Uzun bir dalın ucuna biraz reçel sürdü"
   - Cümle 7: «Uzun bir dalın ucuna biraz reçel sürdü.»
   - Açıklama: Çözüm reçel sürme, dalı sokup bastırma ve çekme diye ikiden fazla adıma yayılıyor ve reçelin topu kaldıracak kadar tutması akla pek yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0037` birebir aynı, `@degisim: fıskiye -> top` (tutuyorsan), ardından `@onarim: 3574172c3de1992e946565cfbefd1e28dc4fafdf`, sonra gövde.

### Hikâye 5: tohum masa-0038 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0038
- yer: dağ (Ormanın yanındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bilezik', fiil 'dağılmak', sıfat 'değişik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: rüzgar ayının sepetini devirdi ve meyveler dağıldı | sepeti kaldırıp meyveleri tek tek topladı
@tohum: masa-0038
@degisim: bilezik -> sepet
Tepede güneş parlıyordu. Maşa, Koca Ayı ve kirpi değişik meyveler topluyordu. Ama rüzgar Koca Ayı'nın sepetini devirdi ve meyveler yere dağıldı. Koca Ayı üzgün üzgün meyvelere baktı. "Üzülme, Koca Ayı, ben sana yardım ederim!" dedi Maşa. Maşa sepeti kaldırdı ve meyveleri tek tek içine koydu. Maşa reçeli çok severdi ve tatlı meyveleri çimenlerin arasında hemen buldu. Kirpi de dikenlerine takılan küçük meyveleri getirdi. Sepet kısa sürede doldu. Koca Ayı sevinçle Maşa'ya sarıldı. Maşa çok mutluydu, çünkü eski dostuna yardım etmişti.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar Koca Ayı'nın sepetini devirdi"
   - Cümle 3: «Ama rüzgar Koca Ayı'nın sepetini devirdi ve meyveler yere dağıldı.»
   - Açıklama: Rüzgar sepeti devirdi, meyveler toplandı, bitti; sorun önemsiz ve kendiliğinden kapanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok severdi"
   - Cümle 7: «Maşa reçeli çok severdi ve tatlı meyveleri çimenlerin arasında hemen buldu.»
   - Açıklama: Özellik karttaki cümle gibi sayılıyor, reçel işe yarar biçimde kullanılmıyor.
   - Açıklama: Reçel sevgisi özellik olarak sayılıyor, meyveleri bulmakla gerçek bir bağı yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa reçeli çok severdi ve tatlı meyveleri çimenlerin arasında hemen buldu"
   - Cümle 7: «Maşa reçeli çok severdi ve tatlı meyveleri çimenlerin arasında hemen buldu.»
   - Açıklama: Reçel sevgisi meyveleri hemen bulmanın sebebi gibi sunuluyor ama olayla bağı yok, işlevsiz ve zorlama bir ayrıntı.
   - Açıklama: Reçel sevgisi meyveleri hızlı bulmanın sebebi olarak işlevsiz ve zorlama bir ayrıntı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çünkü eski dostuna yardım"
   - Cümle 11: «Maşa çok mutluydu, çünkü eski dostuna yardım etmişti.»
   - Açıklama: 'Eski dost' soyut bir kavram ve küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0038` birebir aynı, `@degisim: bilezik -> sepet` (tutuyorsan), ardından `@onarim: 97e5ccb852220de37e31ba713b486cd2792ef0e4`, sonra gövde.

### Hikâye 6: tohum masa-0039 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0039
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'koni', fiil 'yıkamak', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çamur oyunu yüzünden elleri çamur içindeydi | yağmur suyunu kovada toplayıp ellerini yıkadı
@tohum: masa-0039
@degisim: koni -> kova
Maşa bulutlu bir günde ormanda kovasıyla çamurdan pasta yapıyordu. Birden karnı acıktı ve sepetindeki reçelli ekmeği yemek istedi. Ama çamur oyunu yüzünden elleri çamur içindeydi. Maşa önce ellerini otlara sildi, ama çamur çıkmadı. Sonra bulutlardan küçük damlalar düşmeye başladı. Maşa hemen boş kovasını yağmurun altına koydu. Kovada biraz yağmur suyu birikti. Maşa ellerini bu suyla yıkadı ve elleri tertemiz oldu. Sonra büyük bir ağacın altına oturdu. Reçelli ekmeğini afiyetle yedi. Maşa çok mutluydu, çünkü elleri temizdi ve karnı doymuştu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bulutlardan küçük damlalar düşmeye başladı"
   - Cümle 5: «Sonra bulutlardan küçük damlalar düşmeye başladı.»
   - Açıklama: Çözümü getiren yağmur tam o anda kendiliğinden başlıyor; çözüm figürün çabasından değil tesadüften çıkıyor.
   - Açıklama: Çözümü getiren yağmur tam gerektiği anda tesadüfen başlıyor; çözüm Maşa'nın bir fikrinden değil rastlantıdan çıkıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ellerini bu suyla yıkadı ve elleri tertemiz oldu"
   - Cümle 8: «Maşa ellerini bu suyla yıkadı ve elleri tertemiz oldu.»
   - Açıklama: 'Eller' aynı cümlede gereksiz yere tekrarlanıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Reçelli ekmeğini afiyetle yedi"
   - Cümle 10: «Reçelli ekmeğini afiyetle yedi.»
   - Açıklama: Reçel özelliği iki kez anılıyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0039` birebir aynı, `@degisim: koni -> kova` (tutuyorsan), ardından `@onarim: 2e9cfe89a5af4950b6973ede6b10aa81c7e0531e`, sonra gövde.

### Hikâye 7: tohum masa-0040 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Daşa
@tohum: masa-0040
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boncuk', fiil 'kavuşmak', sıfat 'uyanık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Daşa
@plan: koşarken kutu elinden düştü ve boncuklar döküldü | özür diledi ve boncukları tek tek topladı
@tohum: masa-0040
@degisim: uyanık -> renkli
Rüzgar tepede hafif hafif esiyordu. Daşa çimenlere oturmuş, kolye yapmak için Maşa'yı bekliyordu. Maşa boncuk kutusuyla koşmayı denedi, ama kutu elinden düştü. Renkli boncuklar çimenlerin arasına döküldü. Daşa çok üzüldü. "Özür dilerim, Daşa, hepsini hemen toplayacağım," dedi Maşa. Maşa çimenlere eğildi ve boncukları tek tek topladı. Daşa da kutuyu açık tuttu. Sonunda bütün boncuklar kutudaydı. Daşa kolyesinin boncuklarına kavuştu ve gülümsedi. "Teşekkürler, Maşa, hadi kolyeyi birlikte yapalım," dedi Daşa. Maşa çok sevindi, çünkü kuzeni yine gülüyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa boncuk kutusuyla koşmayı denedi"
   - Cümle 3: «Maşa boncuk kutusuyla koşmayı denedi, ama kutu elinden düştü.»
   - Açıklama: Tohumdaki deneme özelliği işe yarar biçimde değil, yalnız sorunu doğuran bir kaza olarak kullanılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kolyesinin boncuklarına kavuştu"
   - Cümle 10: «Daşa kolyesinin boncuklarına kavuştu ve gülümsedi.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki çocuk için soyut ve edebi bir fiil.
   - Açıklama: 'Kavuştu' küçük çocuk için soyut ve ağır bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0040` birebir aynı, `@degisim: uyanık -> renkli` (tutuyorsan), ardından `@onarim: 88e883757a4df3ba115bedb4bf616a28b51e7910`, sonra gövde.
