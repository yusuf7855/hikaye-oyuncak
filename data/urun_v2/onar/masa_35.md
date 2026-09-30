# Editör görevi (onarım): Maşa, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar35.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0057 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0057
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yosun', fiil 'içmek', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: sincap şaka yapmak için kavanozun üstüne yosun koydu | sincabın ağzında yosun görüp yosunların altına baktı
@tohum: masa-0057
@degisim: içmek -> saklamak
Maşa tepede Koca Ayı ve sincapla bir arama oyunu oynuyordu. Koca Ayı, Maşa'nın özel reçel kavanozunu bir taşın arkasına sakladı. Ama sincap şaka yapmak için kavanozun üstüne yosun koydu. Maşa taşların arkasına baktı ama kavanozu göremedi. Sonra sincabın ağzında biraz yosun gördü. Maşa etrafa baktı ve bir taşın dibinde kabarık bir yosun yığını buldu. Maşa hemen o taşa koştu ve yosunları kaldırdı. Reçel kavanozu tam oradaydı! "Buldum, sincap, sen çok komiksin!" dedi Maşa. Koca Ayı güldü ve ellerini çırptı. Sincap da kuyruğunu salladı. Maşa çok sevindi, çünkü sevdiği reçeli oyunun sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sincabın ağzında yosun görüp yosunların altına baktı"
   - Cümle 0 (plan satırı): «sincap şaka yapmak için kavanozun üstüne yosun koydu | sincabın ağzında yosun görüp yosunların altına baktı»
   - Açıklama: Gövdede Maşa sincabın ağzında yosun görmüyor, taşın dibindeki yosun yığınını buluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0057` birebir aynı, `@degisim: içmek -> saklamak` (tutuyorsan), ardından `@onarim: 634d2e541828062ce1010e295e558d6889cf870d`, sonra gövde.

### Hikâye 2: tohum masa-0079 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0079
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pilav', fiil 'kucaklamak', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: pilavı koyduğu ince yaprak yırtıldı ve pilav döküldü | pilavı boş reçel kavanozuna doldurup sofraya taşıdı
@tohum: masa-0079
Maşa ormanda yemek oyunu oynuyordu ve bir kütüğe sofra kurmuştu. Beyaz taşlardan pilav yaptı, en sevdiği reçelin boş kavanozu da yanındaydı. Ama pilavı koyduğu temiz yaprak çok inceydi, yırtıldı ve pilav yere döküldü. Maşa üzülmedi ve taşları tek tek topladı. Sonra hepsini boş kavanoza doldurdu. Kavanoz sağlamdı ve içindeki hiçbir taş dökülmedi. Maşa kavanozu sevinçle kucakladı ve kütüğe taşıdı. Kavanozu sofranın tam ortasına koydu. Sofra artık hazırdı. Maşa bundan sonra pilavını hep kavanoza koydu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği reçelin boş kavanozu"
   - Cümle 2: «Beyaz taşlardan pilav yaptı, en sevdiği reçelin boş kavanozu da yanındaydı.»
   - Açıklama: Tohumdaki reçel sevgisi işe yaramıyor; çözümü herhangi bir sağlam kap sağlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0079` birebir aynı, ardından `@onarim: f440efc0b28ea91850cd90881c8f02fe3a02d4d9`, sonra gövde.

### Hikâye 3: tohum masa-0080 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0080
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'süs', fiil 'kurulamak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: reçel kavanozu ıslak çimenlerde kayboldu | reçelin kokusunu alıp kavanozu çalının altında buldu
@tohum: masa-0080
@degisim: süs -> örtü
Bir sabah Maşa ile kuzeni Daşa tepede sincapla piknik yapıyordu. Daşa tuzlu ekmekleri örtünün üstüne koydu. Ama Maşa'nın kapağı açık reçel kavanozu kaymış ve ıslak çimenlerde kaybolmuştu. "Reçelim nerede?" diye sordu Maşa. Daşa çimenlere uzun uzun baktı ama kavanozu göremedi. Maşa havayı derin derin kokladı. Reçeli çok sevdiği için onun tatlı kokusunu hemen tanıdı. Koku çalının altından geliyordu. Maşa eğildi ve kavanozu orada buldu. Kavanoz çimenlerde ıslanmıştı, Daşa onu örtünün ucuyla kuruladı. "Reçelim burada, Daşa!" dedi Maşa. Maşa ekmeğine reçel sürdü ve sincaba da bir parça verdi. Maşa ile Daşa çok sevindi, çünkü kaybolan reçel yine örtünün üstündeydi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "reçel kavanozu kaymış ve ıslak çimenlerde kaybolmuştu"
   - Cümle 3: «Ama Maşa'nın kapağı açık reçel kavanozu kaymış ve ıslak çimenlerde kaybolmuştu.»
   - Açıklama: Kavanozun nasıl olup da çalının altına kadar kayıp gözden kaybolduğu açıklanmıyor, sebep belirsiz.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa'nın kapağı açık reçel kavanozu kaymış"
   - Cümle 3: «Ama Maşa'nın kapağı açık reçel kavanozu kaymış ve ıslak çimenlerde kaybolmuştu.»
   - Açıklama: Kapağı açık kavanoz kayıp çalının altına gidiyor ama reçel dökülmüyor ve sonra ekmeğe sürülüyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Reçeli çok sevdiği için onun tatlı kokusunu hemen tanıdı"
   - Cümle 7: «Reçeli çok sevdiği için onun tatlı kokusunu hemen tanıdı.»
   - Açıklama: Karttaki özellik yalnız reçeli sevmek; hikaye bunu kartta olmayan bir koku alma becerisine dönüştürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0080` birebir aynı, `@degisim: süs -> örtü` (tutuyorsan), ardından `@onarim: 970d43c3e0cb30c3a72f34b11c9ccad69e999835`, sonra gövde.

### Hikâye 4: tohum masa-0083 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0083
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kemer', fiil 'sallamak', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: kavanozdaki çiçek gölgede kaldı ve açılmadı | kavanozu sepetle güneşli bir yere taşıdı
@tohum: masa-0083
@degisim: kemer -> sepet
Hava aydınlıktı ve evin önünde kuşlar ötüyordu. Maşa ile kirpi kavanozdaki kırmızı çiçeğin açılmasını bekliyordu. Ama kavanoz ağacın gölgesinde kalmıştı ve çiçek açılmıyordu. Kavanoz küçük ve hafifti. Maşa kavanozu reçel dolu sepetine koydu. Sonra sepeti güneşli bir yere taşıdı. Beklemek Maşa için zordu. Ama sepetten en sevdiği reçeli yedi ve kirpiyle sessizce oturdu. Güneş çiçeği ısıttı. Kırmızı çiçek yavaş yavaş açıldı. "Bak, kirpi, çiçek açıldı!" dedi Maşa. Kirpi çiçeği kokladı ve sevinçle başını salladı. Maşa ile kirpi çiçeğin yanında mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa kavanozu reçel dolu sepetine koydu"
   - Cümle 5: «Maşa kavanozu reçel dolu sepetine koydu.»
   - Açıklama: Kavanoz küçük ve hafif olduğu halde reçel dolu sepete konuyor; sepet ve reçel yalnız özelliği göstermek için sebepsizce kuruluyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sepetten en sevdiği reçeli yedi"
   - Cümle 8: «Ama sepetten en sevdiği reçeli yedi ve kirpiyle sessizce oturdu.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0083` birebir aynı, `@degisim: kemer -> sepet` (tutuyorsan), ardından `@onarim: 9b632dc145d2639f913762b3f57a0013a3dee752`, sonra gövde.

### Hikâye 5: tohum masa-0091 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0091
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: kaybolan eşya
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'baston', fiil 'sığınmak', sıfat 'çikolatalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: koşarken çikolatalı baston şekeri elinden düştü | yerdeki reçel izine bakarak şekeri buldu
@tohum: masa-0091
@degisim: sığınmak -> koşmak
Koca Ayı'nın evinin önünde Maşa çikolatalı baston şekerini reçele batırıp yiyordu. Sonra Koca Ayı ile koşmaya başladı. Ama koşarken şeker elinden düştü. Maşa şekeri otların arasında hiçbir yerde göremedi. Sonra reçel yediği yere döndü. Otların üstünde küçük, parlak reçel damlaları vardı. Maşa koşarken şekerden yere reçel düşmüştü. Maşa bu damlalara bakarak yürüdü. Son damla bir çalının dibindeydi. Çikolatalı şeker de orada, yaprakların arasında duruyordu. Maşa şekeri aldı ve sevinçle Koca Ayı'ya gösterdi. Koca Ayı gülümseyip başını salladı. Maşa bundan sonra şekerini yerken koşmadı, oturup yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa koşarken şekerden yere reçel düşmüştü"
   - Cümle 7: «Maşa koşarken şekerden yere reçel düşmüştü.»
   - Açıklama: Cümle Maşa'yı düşmüştü fiilinin öznesi gibi okutuyor; 'Maşa koşarken, şekerden yere reçel damlamıştı' gibi kurulmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0091` birebir aynı, `@degisim: sığınmak -> koşmak` (tutuyorsan), ardından `@onarim: 94d7c8bc18fa62c4a27891864d22628e6508ea67`, sonra gövde.

### Hikâye 6: tohum masa-0092 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, sincap
@tohum: masa-0092
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'bot', fiil 'duymak', sıfat 'incecik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, sincap
@plan: sincap yuvasındaydı ve onları duymuyordu | incecik bir dalla botun altına vurdu
@tohum: masa-0092
Rüzgar hafif hafif esiyordu. Maşa ile Koca Ayı, sincabın ağacının dibine fındık dolu bir bot koydu. Bu bir sürprizdi ama sincap yuvasındaydı ve onları duymuyordu. Maşa önce ellerini çırptı ama sincap dışarı çıkmadı. Sonra yerden incecik bir dal aldı. Dalla botun altına tak tak vurmayı denedi. Bot yüksek ve komik bir ses çıkardı. Sincap sesi duydu ve ağaçtan hızla indi. Botun içindeki fındıkları görünce kuyruğunu salladı. Sonra fındıkları birer birer yuvasına taşıdı. Koca Ayı sevinçle Maşa'ya sarıldı. Maşa, botun komik sesiyle sincabı çağırmayı öğrendi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sincap yuvasındaydı ve onları duymuyordu"
   - Cümle 3: «Bu bir sürprizdi ama sincap yuvasındaydı ve onları duymuyordu.»
   - Açıklama: Plan satırında 'onları' zamirinin kimi gösterdiği belli değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bot yüksek ve komik bir ses çıkardı"
   - Cümle 7: «Bot yüksek ve komik bir ses çıkardı.»
   - Açıklama: İncecik bir dalla bota vurmak el çırpmaktan daha yüksek ses çıkarmaz; çözüm kendi kurduğu durumla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0092` birebir aynı, ardından `@onarim: 0703bb4d06c22da961ed41c5a45b3d8442b1b5df`, sonra gövde.

### Hikâye 7: tohum masa-0094 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi, Daşa
@tohum: masa-0094
- yer: dağ (Ormanın yanındaki tepe.)
- tema: sırayla oynamak
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kök', fiil 'okşamak', sıfat 'sakin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi, Daşa
@plan: üçü de aynı anda topa uzandı ve oyun durdu | bekleyene reçel verdi ve herkes sırayla attı
@tohum: masa-0094
Tepede Maşa, Daşa ve kirpi, eğri bir kökün üstünden top yuvarlıyordu. Top kökün üstünden kayıp çimenlere iniyordu ve herkes buna gülüyordu. Ama üçü de aynı anda topa uzandı ve oyun durdu. "Hepimiz ilk olmak istiyoruz," dedi Daşa. Maşa sepetinden reçel kavanozunu çıkardı. "Bekleyen reçel yesin, Daşa," dedi Maşa. Artık kimse acele etmedi. Önce Daşa attı, sonra sakin kirpi topu burnuyla itti. En son Maşa attı. Her seferinde bekleyen ikisi reçel yedi. İki kız sevinçle güldü. Daşa, Maşa'nın başını okşadı. "Sırayla oynamak çok eğlenceli, Daşa!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa sepetinden reçel kavanozunu çıkardı"
   - Cümle 5: «Maşa sepetinden reçel kavanozunu çıkardı.»
   - Açıklama: Daha önce hiç kurulmamış sepet ve reçel, çözümü getirmek için sebepsizce beliriyor.
   - Açıklama: Sepet ve reçel önceden kurulmadan çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0094` birebir aynı, ardından `@onarim: 0cbf4b68b6a6fc7bd5ba46fcee0ceab06af8083f`, sonra gövde.

### Hikâye 8: tohum masa-0095 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi, Daşa
@tohum: masa-0095
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'paket', fiil 'süpürmek', sıfat 'berrak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi, Daşa
@plan: zıplarken paketi düşürdü ve kurabiyeler kırıldı | özür diledi ve kırık parçaları reçelle yapıştırdı
@tohum: masa-0095
@degisim: berrak -> mavi
Bir sabah ormanda gökyüzü maviydi. Daşa, Maşa'ya ve kirpiye şehirden bir paket kurabiye getirmişti. Maşa sevinçle zıplarken paketi düşürdü ve içindeki kurabiyeler ikiye kırıldı. "Hepsi kırıldı," dedi Daşa üzgün bir sesle. "Özür dilerim, Daşa, çok acele ettim," dedi Maşa. Sonra sepetinden reçel kavanozunu çıkardı. Kırık parçaların arasına reçel sürüp onları birbirine yapıştırdı. Kurabiyeler yine bütün ve reçelli oldu. Sonra Maşa yere dökülen kırıntıları bir dalla bir yaprağa süpürdü. Kirpi kırıntıları mutlu mutlu yedi. Daşa reçelli bir kurabiye tattı ve gülümsedi. "Teşekkürler, Maşa, bunlar çok güzel olmuş!" dedi Daşa.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Daşa, çok acele ettim"
   - Cümle 5: «"Özür dilerim, Daşa, çok acele ettim," dedi Maşa.»
   - Açıklama: Maşa acele etmedi, sevinçle zıpladı; 'acele ettim' olaya uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra sepetinden reçel kavanozunu çıkardı"
   - Cümle 6: «Sonra sepetinden reçel kavanozunu çıkardı.»
   - Açıklama: Daha önce hiç geçmeyen sepet ve reçel kavanozu çözümü sebepsizce getiriyor.
   - Açıklama: Sepet ve reçel kavanozu önceden kurulmadan sebepsizce beliriyor ve çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0095` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: ba83c810baadf689c06e597dad87b5d486690276`, sonra gövde.

### Hikâye 9: tohum masa-0096 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı, sincap
@tohum: masa-0096
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boya', fiil 'sararmak', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı, sincap
@plan: sincap boş bir kovaya girdi ve dışarı çıkamadı | kovaya uzun bir dal koydu ve sincap tırmandı
@tohum: masa-0096
Bir sabah Koca Ayı'nın bahçesinde yapraklar sararmış, yere dallar düşmüştü. Koca Ayı ağaç evinin kapısına boya sürüyordu, Maşa da ona bakıyordu. Oynayan bir sincap zıplayıp boş bir kovaya girdi. Ama kovanın içi kaygandı ve sincap dışarı çıkamadı. Maşa heyecanlı heyecanlı sincabın yanına koştu. Önce elini uzattı ama kova çok derindi. Sonra yerdeki uzun bir dalı kovaya koymayı denedi. Sincap dala tutundu ve hızla yukarı tırmandı. Kovadan atladı ve kuyruğunu sallayarak ağaca koştu. Koca Ayı Maşa'ya bakıp gülümsedi. Maşa bundan sonra boş kovaları hep ters çevirip koydu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Koca Ayı ağaç evinin kapısına"
   - Cümle 2: «Koca Ayı ağaç evinin kapısına boya sürüyordu, Maşa da ona bakıyordu.»
   - Açıklama: 'Ağaç ev' ağaçtaki ev demektir; ahşap ev kastediliyorsa kelime yanlış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Koca Ayı ağaç evinin kapısına boya sürüyordu"
   - Cümle 2: «Koca Ayı ağaç evinin kapısına boya sürüyordu, Maşa da ona bakıyordu.»
   - Açıklama: Boya sürme işi kuruluyor ama olayda hiç kullanılmıyor, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0096` birebir aynı, ardından `@onarim: 117893a1ef038b125e7fd91d85644545b7906ace`, sonra gövde.

### Hikâye 10: tohum masa-0098 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0098
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'biber', fiil 'doğmak', sıfat 'şekerli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: sepetteki fındıklar azalmıştı ve kimin aldığı bilinmiyordu | yaprağa reçel sürdü ve reçelli izleri takip etti
@tohum: masa-0098
@degisim: biber -> fındık
Ormanda güneş yeni doğmuştu. Maşa sepetini bir ağacın altına bırakıp biraz uzakta çiçek topladı. Geri geldiğinde sepetteki fındıklar azalmıştı. Maşa fındıkları kimin aldığını çok merak etti. Sepetin önüne bir yaprak koydu ve üstüne şekerli reçelinden sürdü. Sonra yine çiçek toplamaya gitti. Döndüğünde reçelin üstünde küçük ayak izleri vardı. Reçelli izler yerde bir ağaca kadar gidiyordu. Maşa ağaca baktı ve dalda bir sincap gördü. Sincabın ağzında bir fındık vardı. "Demek fındıkları sen aldın, sincap!" dedi Maşa. Sonra Maşa ile sincap ağacın altında mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra Maşa ile sincap ağacın altında mutlu mutlu oynadı"
   - Cümle 12: «Sonra Maşa ile sincap ağacın altında mutlu mutlu oynadı.»
   - Açıklama: Azalan fındıklara ne olduğu söylenmiyor ve son, sorunla bağı kurulmadan ansızın oyuna geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0098` birebir aynı, `@degisim: biber -> fındık` (tutuyorsan), ardından `@onarim: 8540c8506f852b16c37254e005e9731a5b06bbb7`, sonra gövde.

### Hikâye 11: tohum masa-0102 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0102
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kanepe', fiil 'fışkırmak', sıfat 'umutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: zıplarken ayakkabısı yumuşak çamura battı | ayağını sağa sola küçük küçük salladı
@tohum: masa-0102
@degisim: kanepe -> çamur
Bir sabah ormanda yağmur yeni dinmişti. Maşa patikadaki su birikintilerine zıplıyor, sular havaya fışkırıyordu. Ama bir anda Maşa'nın ayakkabısı yumuşak bir çamura battı. Maşa ayağını hızla çekti ama ayağı yerinden çıkmadı. Maşa durmadı ve başka bir şey denedi. Ayağını sağa ve sola küçük küçük salladı. Ayakkabı biraz oynadı ve Maşa umutlu bir yüzle daha çok salladı. Sonunda ayağı ayakkabısıyla birlikte çamurdan çıktı. Maşa çamurlu ayakkabısına baktı ve güldü. Sonra yine su birikintilerine zıpladı ama bu kez çamurdan uzak durdu. Maşa bundan sonra çamurda ayağını çekmedi, yavaşça salladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa umutlu bir yüzle"
   - Cümle 7: «Ayakkabı biraz oynadı ve Maşa umutlu bir yüzle daha çok salladı.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir ifade; 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Umutlu bir yüz' soyut bir kavramdır; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0102` birebir aynı, `@degisim: kanepe -> çamur` (tutuyorsan), ardından `@onarim: 4487c2d2a9cb2334b698561deebfb7a753478a63`, sonra gövde.

### Hikâye 12: tohum masa-0103 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0103
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'şerit', fiil 'kaçmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: reçel kavanozu yokuştan aşağı yuvarlandı ve kayboldu | kavanozdaki kırmızı şeridi otların arasında aradı
@tohum: masa-0103
@degisim: kaçmak -> yuvarlanmak
Rüzgar hafif hafif esiyordu. Maşa tepede elmalı bir kurabiye ve bir reçel kavanozu tutuyordu. Kavanozun kapağına kırmızı bir şerit bağlıydı. Birden kavanoz elinden kaydı ve yokuştan aşağı yuvarlandı. Kavanoz uzun otların arasında kayboldu. Maşa aşağıya yavaşça indi ve otlara baktı. Ama otlar çok sıktı ve kavanoz görünmüyordu. Maşa otların arasında o kırmızı şeridi aradı. Sonunda bir çalının dibinde kırmızı şerit göründü. Maşa kavanozu aldı ve ona sevinçle sarıldı. Sonra tepeye geri çıktı ve kurabiyesine reçel sürüp mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kavanozun kapağına kırmızı bir şerit bağlıydı.»
   - Açıklama: Kavanozun yuvarlanıp kaybolması ancak 4. ve 5. cümlede söyleniyor; ilk üç cümlede sorun yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0103` birebir aynı, `@degisim: kaçmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 0c167f9b1623bcd51e9258ab795328535866fd3d`, sonra gövde.
