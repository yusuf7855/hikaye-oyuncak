# Editör görevi (onarım): Maşa, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0007 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0007
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kurabiye', fiil 'görünmek', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: büyük sesten kirpi kıvrıldı ve burnu görünmedi | yanına oturup yavaşça konuştu ve kurabiye verdi
@tohum: masa-0007
@degisim: çevik -> hızlı
Bir sabah Maşa, Koca Ayı ve kirpi tepede kurabiye yiyordu. Koca Ayı kurabiyeleri çok beğendi ve ellerini hızlı hızlı çırptı. Bu büyük sesten kirpi top gibi kıvrıldı ve burnu hiç görünmedi. Kirpi artık kurabiyesini yiyemiyordu. Maşa kirpiye yardım etmek istedi. Maşa hiç sessiz durmazdı, ama bu kez yeni bir şey denedi. Kirpinin yanına oturdu ve çok yavaş konuştu. "Kirpi, gel, sana bir kurabiye ayırdım," dedi Maşa. Kurabiyeyi kirpiye uzattı. Kirpi biraz açıldı ve önce küçük burnu göründü. Kurabiyeyi aldı ve hemen yedi. Üçü tepede kurabiyelerini mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yanına oturup yavaşça konuştu"
   - Cümle 0 (plan satırı): «büyük sesten kirpi kıvrıldı ve burnu görünmedi | yanına oturup yavaşça konuştu ve kurabiye verdi»
   - Açıklama: Gövdede Maşa kirpinin yanına oturmuyor ve yavaşça konuşmuyor; yalnız kurabiye uzatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0007` birebir aynı, `@degisim: çevik -> hızlı` (tutuyorsan), ardından `@onarim: 8a6f54a8dea5beccbe225e96c99921806da9ecad`, sonra gövde.

### Hikâye 2: tohum masa-0012 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0012
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tabure', fiil 'ölçmek', sıfat 'mutsuz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: kaşık ağacın yanındaki küçük bir deliğe düştü | sincaptan yardım istedi ve sincap kaşığı getirdi
@tohum: masa-0012
@degisim: tabure -> kaşık
Bir sabah Maşa ile Daşa ormanda büyük bir ağacın altında oturuyordu. Maşa kavanozdan küçük bir kaşıkla reçel yiyordu. Birden kaşık elinden kaydı ve ağacın yanındaki bir deliğe düştü. Delik Maşa'nın elinden çok daha küçüktü. Maşa çok mutsuz oldu, çünkü reçelinin yarısı daha kavanozdaydı. Daşa deliği iki parmağıyla ölçtü. "Benim elim de sığmaz, Maşa," dedi Daşa. Dalda küçük bir sincap onlara bakıyordu. "Sincap, kaşığımı bana getirir misin?" diye sordu Maşa. Sincap hızla indi ve deliğe girdi. Biraz sonra kaşığı ağzında tutarak dışarı çıktı. "Teşekkürler, sincap!" dedi Maşa. Maşa çok sevindi, çünkü kalan reçelini kaşığıyla yiyebilecekti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "reçelinin yarısı daha kavanozdaydı"
   - Cümle 5: «Maşa çok mutsuz oldu, çünkü reçelinin yarısı daha kavanozdaydı.»
   - Açıklama: 'Daha' burada 'hâlâ' anlamında konuşma diliyle kullanılmış ve 'yarısından fazlası' diye de okunabiliyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sincap hızla indi ve deliğe girdi"
   - Cümle 10: «Sincap hızla indi ve deliğe girdi.»
   - Açıklama: Delik Maşa'nın elinden çok daha küçükken sincabın bütün gövdesiyle içine girmesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0012` birebir aynı, `@degisim: tabure -> kaşık` (tutuyorsan), ardından `@onarim: f476d42779eec69f644da810c999998e867ebac0`, sonra gövde.

### Hikâye 3: tohum masa-0014 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi, Daşa
@tohum: masa-0014
- yer: dağ (Ormanın yanındaki tepe.)
- tema: sırayla oynamak
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kürek', fiil 'dokunmak', sıfat 'ucuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi, Daşa
@plan: tek bir kürek vardı ve ikisi de kazmak istedi | sırayla kazdılar ve fidanı diktiler
@tohum: masa-0014
@degisim: ucuz -> küçük
Tepede serin bir rüzgar esiyordu. Maşa ile Daşa kirpi için küçük bir elma fidanı dikecekti. Ama tek bir kürek vardı ve ikisi de önce kazmak istedi. Küreği aynı anda çektiler ve kürek yere düştü. Maşa evden getirdiği reçel kavanozunu hatırladı. "Küreği önce sen al, Daşa, ben de reçelimi yiyeyim," dedi Maşa. Daşa kazarken Maşa reçelini yedi. Sonra küreği Maşa aldı ve biraz kazdı. Sonunda çukur hazır oldu. Fidanı çukura koyup etrafını toprakla doldurdular. Kirpi yaklaştı ve burnuyla fidana dokundu. Maşa ile Daşa çok sevindi, çünkü sırayla kazınca fidan çabucak dikilmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa evden getirdiği reçel kavanozunu hatırladı"
   - Cümle 5: «Maşa evden getirdiği reçel kavanozunu hatırladı.»
   - Açıklama: Reçel kavanozu sebepsizce beliriyor ve sıra sorununu çözmekle doğrudan ilgisi olmayan bir bahane olarak kullanılıyor.
   - Açıklama: Daha önce kurulmamış reçel kavanozu birden beliriyor ve sıralama çözümünü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0014` birebir aynı, `@degisim: ucuz -> küçük` (tutuyorsan), ardından `@onarim: a9d2c0128f4e4d3c813bc9f0215d7146d5a9f09d`, sonra gövde.

### Hikâye 4: tohum masa-0016 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0016
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'direk', fiil 'yerleştirmek', sıfat 'düz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: örtü hep kayıyordu çünkü çadırın direği çok inceydi | kalın ve düz bir dalı toprağa yerleştirdi
@tohum: masa-0016
Serin bir rüzgar esiyordu. Maşa reçelini rüzgardan uzakta yemek için kirpiyle ormanda çadır kurdu. Ama örtü hep yere kayıyordu, çünkü çadırın direği çok ince bir daldı. Maşa ince dalı yere bıraktı ve etrafa baktı. Çalıların yanında kalın ve düz bir dal buldu. Maşa dalı toprağa sıkıca yerleştirdi ve örtüyü üstüne serdi. Bu kez örtü hiç kaymadı. Güzel bir çadır olmuştu. Kirpi hemen çadırın içine girdi. Maşa da reçeliyle onun yanına oturdu. "Bak, kirpi, çadırımız hazır!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçelini rüzgardan uzakta"
   - Cümle 2: «Maşa reçelini rüzgardan uzakta yemek için kirpiyle ormanda çadır kurdu.»
   - Açıklama: Tohumdaki reçel özelliği iki kez geçiyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0016` birebir aynı, ardından `@onarim: df7e58abb72433d323ce6663f3d1d1594fe781e7`, sonra gövde.

### Hikâye 5: tohum masa-0018 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0018
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'lamba', fiil 'sıkılmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: uçurtma her seferinde yere düştü çünkü kuyruğu kısaydı | kavanozdaki kurdeleyi kuyruğa bağladı
@tohum: masa-0018
@degisim: lamba -> uçurtma
Tepede güçlü bir rüzgar esiyordu. Maşa süslü uçurtmasını ve sevdiği reçelin kavanozunu tepeye getirmişti. Ama uçurtma her seferinde dönüp yere düştü, çünkü kuyruğu çok kısaydı. Maşa hiç sıkılmadı ve uçurtmaya dikkatle baktı. Sonra kavanozun uzun, kırmızı kurdelesini gördü. Maşa kurdeleyi çözdü ve uçurtmanın kuyruğuna bağladı. Uçurtma bu kez dönmedi ve yavaş yavaş yükseldi. Maşa uçurtmanın ipini iki eliyle tuttu ve sevinçle güldü. Kırmızı kuyruk rüzgarda sallandı. Maşa uçurtmasını tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sevdiği reçelin kavanozunu tepeye"
   - Cümle 2: «Maşa süslü uçurtmasını ve sevdiği reçelin kavanozunu tepeye getirmişti.»
   - Açıklama: Tamlama doğal değil; 'sevdiği reçel kavanozunu' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sevdiği reçelin kavanozunu tepeye getirmişti"
   - Cümle 2: «Maşa süslü uçurtmasını ve sevdiği reçelin kavanozunu tepeye getirmişti.»
   - Açıklama: Tohum özelliği reçel sevgisi çözümde işe yaramıyor; çözümü yalnız kavanozun kurdelesi sağlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0018` birebir aynı, `@degisim: lamba -> uçurtma` (tutuyorsan), ardından `@onarim: 6b49f07e55b1d62d199aed69d8bbb1d794ef77fd`, sonra gövde.

### Hikâye 6: tohum masa-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0019
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çubuk', fiil 'utanmak', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: karda yıldız çizmek istedi ama ince çubuk kırıldı | kalın bir çubuk bulup yıldızı çizdi
@tohum: masa-0019
@degisim: temkinli -> kalın
Ormanda her yer karla kaplıydı. Maşa kar tanelerinin küçük yıldızlara benzediğini fark etti. Karda bir yıldız çizmek istedi ama aldığı ince çubuk hemen kırıldı. Maşa utanmadı ve ağaçların altında yeni bir çubuk aradı. Orada kalın ve sağlam bir çubuk buldu. Maşa bu çubukla yeniden denedi. Bu kez çubuğu kara hafifçe bastırdı. Yıldızın beş ucunu tek tek çizdi. Çubuk hiç kırılmadı. Artık karda büyük bir yıldız vardı. Maşa çok sevindi, çünkü kocaman yıldızını sonunda çizmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa utanmadı ve ağaçların"
   - Cümle 4: «Maşa utanmadı ve ağaçların altında yeni bir çubuk aradı.»
   - Açıklama: Kırılan çubukta utanılacak bir şey yok; 'üzülmedi' gibi bir kelime olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0019` birebir aynı, `@degisim: temkinli -> kalın` (tutuyorsan), ardından `@onarim: a497bb5de1e4685cd93fb0e3ee88aa2359d942e4`, sonra gövde.

### Hikâye 7: tohum masa-0021 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, sincap
@tohum: masa-0021
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'ayakkabı', fiil 'sektirmek', sıfat 'devasa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, sincap
@plan: top fındık sepetini devirdi ve fındıklar döküldü | özür diledi ve fındıkları yeniden topladı
@tohum: masa-0021
@degisim: devasa -> kocaman
Maşa bir kavanoz reçel almıştı ve kocaman bir ağacın yanında top sektiriyordu. Koca Ayı ile sincap da ağacın altında bir sepete fındık topluyordu. Maşa topa ayakkabısıyla çok sert vurdu ve top sepeti devirdi. Fındıklar yere döküldü ve sincap üzüldü. "Özür dilerim, sincap, dikkat etmedim," dedi Maşa. Sonra Maşa yere eğildi ve fındıkları tek tek topladı. Koca Ayı da ona yardım etti. Kısa sürede sepet yine fındıkla doldu. Maşa sincaba en sevdiği reçelden de biraz verdi. Sincap sevinçle kuyruğunu salladı. Sonra üçü ağacın altında birlikte mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "sincaba en sevdiği reçelden"
   - Cümle 9: «Maşa sincaba en sevdiği reçelden de biraz verdi.»
   - Açıklama: 'En sevdiği' reçelin Maşa'nın mı sincabın mı sevdiği olduğu belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa sincaba en sevdiği reçelden de biraz verdi"
   - Cümle 9: «Maşa sincaba en sevdiği reçelden de biraz verdi.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, sona eklenmiş bir ayrıntı olarak kalıyor.
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümüne hiç katılmıyor, yalnız süs olarak iki kez geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0021` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: d99425e6d746b7fc52512b1846b8efdf761b3a59`, sonra gövde.

### Hikâye 8: tohum masa-0024 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0024
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kızak', fiil 'kazanmak', sıfat 'güvenli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: kızak yağan karın altında kalmıştı | karı iki yerde kazdı ve kızağı buldu
@tohum: masa-0024
Bir kış sabahı Maşa ile Koca Ayı tepede kızak yarışı yapacaktı. Ama Maşa'nın kırmızı kızağı yağan karın altında kalmıştı. "Kızak nerede?" diye sordu Maşa. Önce ağacın önündeki karı kazmayı denedi. Orada yalnız bir taş vardı. Birden bir kirpi ağacın arkasına koştu ve karı eşeledi. Maşa da orayı kazdı ve bir ip gördü. Maşa ipi çekti ve kızak karın içinden çıktı. Kirpi sevinçle etrafta koştu. "Hadi, yarışalım!" dedi Maşa. İkisi tepenin alçak ve güvenli yerinden aşağı kaydı. Yarışı Maşa kazandı ve üçü mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (5):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "bir kirpi ağacın arkasına koştu ve karı eşeledi"
   - Cümle 6: «Birden bir kirpi ağacın arkasına koştu ve karı eşeledi.»
   - Açıklama: Kızağın yerini Maşa değil kirpi buluyor; yan karakter sorunu çözüyor.
   - Açıklama: Kızağın yerini Maşa değil kirpi buluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden bir kirpi ağacın arkasına"
   - Cümle 6: «Birden bir kirpi ağacın arkasına koştu ve karı eşeledi.»
   - Açıklama: Kirpi sebepsiz beliriyor ve çözümü getiriyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İkisi tepenin alçak"
   - Cümle 11: «İkisi tepenin alçak ve güvenli yerinden aşağı kaydı.»
   - Açıklama: 'İkisi' Maşa ile Koca Ayı'yı mı yoksa kirpiyi mi gösteriyor belli değil, sonra da 'üçü' deniyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İkisi tepenin alçak ve güvenli"
   - Cümle 11: «İkisi tepenin alçak ve güvenli yerinden aşağı kaydı.»
   - Açıklama: Ortamda Maşa, Koca Ayı ve kirpi var; 'İkisi' kimleri gösterdiği belli değil.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "üçü mutlu mutlu oynamaya"
   - Cümle 12: «Yarışı Maşa kazandı ve üçü mutlu mutlu oynamaya devam etti.»
   - Açıklama: Önce ikisi tek kızakla kayıyor, sonra üçü diye sayılıyor ve tek kızakla yarış tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0024` birebir aynı, ardından `@onarim: e7693a088158ca268dbd4bff39caad0f53f0f976`, sonra gövde.

### Hikâye 9: tohum masa-0026 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0026
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pelerin', fiil 'inanmak', sıfat 'yapraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çilekleri koyacak bir sepet yoktu | başörtüsünü bağladı ve küçük bir çanta yaptı
@tohum: masa-0026
@degisim: pelerin -> başörtüsü
Ormanda patikanın kenarında yapraklı bitkiler vardı. Maşa yaprakların altında kırmızı çilekler gördü. Onlardan reçel yapmak istedi, ama çilekleri koyacak sepeti yoktu. Maşa önce çilekleri avuçlarına doldurdu. Ama ellerine yalnız birkaç çilek sığdı. Maşa başörtüsünü çıkardı ve yere serdi. Çilekleri tek tek onun üstüne koydu. Başörtüsünü sıkıca bağladı ve küçük bir çanta yaptı. Çanta çileklerle doldu. Maşa dolu çantaya baktı ve gördüğüne inanamadı. Sonra çantayı sırtına aldı ve reçel için çileklerini mutlu mutlu taşıdı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gördüğüne inanamadı"
   - Cümle 10: «Maşa dolu çantaya baktı ve gördüğüne inanamadı.»
   - Açıklama: 'Gördüğüne inanamamak' deyimdir, küçük çocuğa uygun değil.
   - Açıklama: 'Gördüğüne inanamamak' deyimdir, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0026` birebir aynı, `@degisim: pelerin -> başörtüsü` (tutuyorsan), ardından `@onarim: e682601829ba04a58b206bb513f5bbe4330767d3`, sonra gövde.

### Hikâye 10: tohum masa-0030 (deneme 4 -> 5)

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
@plan: koşarken düşen gözlük uzun çimenlerde görünmedi | ilk durduğu yere dönüp oradan baktı ve yürüdü
@tohum: masa-0030
@degisim: köpürmek -> parlamak
Maşa tepede koşarken pembe oyuncak gözlüğünü düşürmüş, onu arıyordu. Birden uzun çimenlerin arasında bir şey parladı. Maşa hemen oraya koştu ama çimenler çok sıktı ve hiçbir şey göremedi. Maşa ilk durduğu yere döndü ve oradan bakmayı denedi. Işık yine parladı. Maşa bu kez ışığa bakarak yavaş yavaş yürüdü. Çimenlerin arasında Maşa'nın pembe gözlüğü vardı. Gözlüğün camları güneşte parlıyordu. Maşa gözlüğü eline aldı ve güldü. Maşa çok sevindi, çünkü artık oyuncaklarından hiçbiri eksik değildi.
```

**Hakem bulguları (2):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "gözlüğünü düşürmüş, onu arıyordu"
   - Cümle 1: «Maşa tepede koşarken pembe oyuncak gözlüğünü düşürmüş, onu arıyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı kipe kayıyor; 'düşürmüştü' olmalı.
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor; 'düşürmüştü' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "artık oyuncaklarından hiçbiri eksik değildi"
   - Cümle 10: «Maşa çok sevindi, çünkü artık oyuncaklarından hiçbiri eksik değildi.»
   - Açıklama: Hikayede hiç kurulmamış bir oyuncak takımı son cümlede sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0030` birebir aynı, `@degisim: köpürmek -> parlamak` (tutuyorsan), ardından `@onarim: e6fd5d308e2a9b5e0bc081702dbe0b55095338e3`, sonra gövde.

### Hikâye 11: tohum masa-0037 (deneme 3 -> 4)

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
@plan: top ağaca çarpıp iki taşın arasına düştü | dalın ucuna reçel sürdü ve topu çıkardı
@tohum: masa-0037
@degisim: fıskiye -> top
Maşa ormanda piknik yapıyor ve küçük sarı topuyla oynuyordu. Topu havaya atıyor ve yakalıyordu. Ama top bir ağaca çarptı ve iki taşın arasına düştü. Taşların arası çok dardı ve Maşa topa yetişemedi. Maşa sepetteki en sevdiği tatlı reçele baktı. Sarı top çok hafifti, reçel de yapışkandı. Maşa bu yapışkan reçele güvendi. Uzun bir dalın ucuna biraz reçel sürdü. Dalı taşların arasına uzattı ve top reçele yapıştı. Maşa dalı yavaşça çekti ve top dışarı çıktı. Top yapış yapış olmuştu. Maşa güldü ve onu otlara silip temizledi. Maşa bundan sonra topuyla ağaçlardan uzakta, açık bir yerde oynadı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa topa yetişemedi"
   - Cümle 4: «Taşların arası çok dardı ve Maşa topa yetişemedi.»
   - Açıklama: 'Yetişemedi' yanlış anlamda; 'ulaşamadı' olmalı.
   - Açıklama: 'Yetişmek' yanlış; 'topa uzanamadı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa bu yapışkan reçele güvendi"
   - Cümle 7: «Maşa bu yapışkan reçele güvendi.»
   - Açıklama: Reçele güvenmek fiilin nesnesine uymayan tuhaf bir kullanım.
   - Açıklama: 'Güvenmek' reçel için yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu yapışkan reçele güvendi"
   - Cümle 7: «Maşa bu yapışkan reçele güvendi.»
   - Açıklama: 'Güvenmek' burada soyut bir kavram olarak kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa bu yapışkan reçele güvendi"
   - Cümle 7: «Maşa bu yapışkan reçele güvendi.»
   - Açıklama: Reçele güvenmek soyut ve küçük çocuğa uygun olmayan bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0037` birebir aynı, `@degisim: fıskiye -> top` (tutuyorsan), ardından `@onarim: e20cd34ce0b9995abf6eb97d8b9fdc4c77c19bb1`, sonra gövde.

### Hikâye 12: tohum masa-0038 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: sepet devrildi ve elmalar tepeden aşağı dağıldı | elmaları topladı ve sepete ağır reçel kavanozu koydu
@tohum: masa-0038
@degisim: bilezik -> sepet
Tepede güneş parlıyordu. Maşa, Koca Ayı ve kirpi çimenlerde piknik yapıyordu. Sepette değişik renklerde elmalar vardı. Ama kirpi elma almak için sepete dayandı ve sepet devrildi. Elmalar tepeden aşağı yuvarlandı ve çimenlere dağıldı. Kirpi üzgün üzgün başını eğdi. "Üzülme, kirpi, elmaları birlikte toplarız!" dedi Maşa. Maşa önce en sevdiği ağır reçel kavanozunu sepetin dibine koydu. Sonra elmaları tek tek topladı ve sepete koydu. Koca Ayı da ona yardım etti. Kirpi sepete yine dayandı ama sepet bu kez devrilmedi. Kirpi bir elma aldı ve mutlu mutlu yedi. Maşa çok sevindi, çünkü bütün elmalar yine sepetteydi.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kirpi elma almak için sepete dayandı"
   - Cümle 4: «Ama kirpi elma almak için sepete dayandı ve sepet devrildi.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor, ilk üç cümlede sorun yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği ağır reçel kavanozunu sepetin dibine"
   - Cümle 8: «Maşa önce en sevdiği ağır reçel kavanozunu sepetin dibine koydu.»
   - Açıklama: Reçel kavanozu daha önce hiç kurulmadan çözümü getirmek için sebepsizce beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa önce en sevdiği ağır reçel kavanozunu sepetin dibine koydu"
   - Cümle 8: «Maşa önce en sevdiği ağır reçel kavanozunu sepetin dibine koydu.»
   - Açıklama: Reçel kavanozu daha önce hiç kurulmadan tam çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0038` birebir aynı, `@degisim: bilezik -> sepet` (tutuyorsan), ardından `@onarim: 7ebe5dadb393d658b0f84f9eea6b374366d559d0`, sonra gövde.
