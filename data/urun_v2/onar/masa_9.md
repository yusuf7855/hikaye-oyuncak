# Editör görevi (onarım): Maşa, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0011 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0011
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'beşik', fiil 'öğrenmek', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: çilekler büyük yaprakların altında görünmüyordu | yaprakları yavaşça kaldırıp çilekleri buldu
@tohum: masa-0011
@degisim: beşik -> sepet
Bir sabah Maşa evinin önündeki bahçede tek bir kırmızı çilek fark etti. Maşa çilek reçelini çok severdi ve sepetini çilekle doldurmak istedi. Ama öteki çilekler görünmüyordu, çünkü büyük yaprakların altındaydı. Maşa yere eğildi ve bir yaprağı yavaşça kaldırdı. Altında kıpkırmızı bir çilek duruyordu! Maşa narin yaprakları yırtmadan kaldırmayı çabucak öğrendi. Her seferinde yeni bir çilek buldu ve sepete koydu. Sepet kısa sürede çileklerle doldu. Maşa en büyük çileği hemen yedi ve mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa çilek reçelini çok severdi"
   - Cümle 2: «Maşa çilek reçelini çok severdi ve sepetini çilekle doldurmak istedi.»
   - Açıklama: Tohumdaki reçel sevgisi karttaki özellik olarak yalnız söyleniyor, hikayede reçel hiç işe yarar biçimde kullanılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa narin yaprakları yırtmadan"
   - Cümle 6: «Maşa narin yaprakları yırtmadan kaldırmayı çabucak öğrendi.»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmediği bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0011` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: a042890da49c94571421b383f3c8ab895430f545`, sonra gövde.

### Hikâye 2: tohum masa-0012 (deneme 3 -> 4)

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
Bir sabah Maşa ile Daşa ormanda büyük bir ağacın altında oturuyordu. Maşa küçük bir kaşıkla en sevdiği reçeli yiyordu. Birden kaşık elinden kaydı ve ağacın yanındaki bir deliğe düştü. Delik Maşa'nın elinden çok daha küçüktü. Maşa çok mutsuz oldu. Daşa deliği iki parmağıyla ölçtü. "Benim elim de sığmaz, Maşa," dedi Daşa. Dalda küçük bir sincap onlara bakıyordu. "Sincap, kaşığımı bana getirir misin?" diye sordu Maşa. Sincap hızla indi ve deliğe girdi. Biraz sonra kaşığı ağzında tutarak dışarı çıktı. "Teşekkürler, sincap!" dedi Maşa. Maşa çok sevindi, çünkü reçelini yine kaşığıyla yiyebilecekti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği reçeli yiyordu"
   - Cümle 2: «Maşa küçük bir kaşıkla en sevdiği reçeli yiyordu.»
   - Açıklama: Tohumdaki reçel özelliği iki kez anılıyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0012` birebir aynı, `@degisim: tabure -> kaşık` (tutuyorsan), ardından `@onarim: bb66c12c5c81a1b612ef971146a73cadac9d09bd`, sonra gövde.

### Hikâye 3: tohum masa-0014 (deneme 3 -> 4)

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
Tepede serin bir rüzgar esiyordu. Maşa ile Daşa kirpi için küçük bir elma fidanı dikecekti. Ama tek bir kürek vardı ve ikisi de önce kazmak istedi. Küreği aynı anda çektiler ve kürek yere düştü. Maşa işi bitirip reçel yemek istiyordu. "Sırayla kazalım, Daşa, böyle daha hızlı biter," dedi Maşa. Önce Daşa biraz kazdı, sonra küreği Maşa aldı. Böyle sırayla kazdılar ve çukur hazır oldu. Fidanı çukura koyup etrafını toprakla doldurdular. Kirpi yaklaştı ve burnuyla fidana dokundu. Maşa ile Daşa çok sevindi, çünkü sırayla kazınca fidan çabucak dikilmişti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa işi bitirip reçel yemek istiyordu"
   - Cümle 5: «Maşa işi bitirip reçel yemek istiyordu.»
   - Açıklama: Reçel özelliği yalnız süs olarak anılıyor, çözümde işe yaramıyor.
   - Açıklama: Tohumdaki reçel özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa işi bitirip reçel yemek istiyordu"
   - Cümle 5: «Maşa işi bitirip reçel yemek istiyordu.»
   - Açıklama: Reçel isteği kuruluyor ama hikayede bir daha kullanılmıyor.
   - Açıklama: Reçel isteği kurulup hikayede hiç kullanılmıyor; işlevsiz ayrıntı.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Böyle sırayla kazdılar ve çukur hazır oldu"
   - Cümle 8: «Böyle sırayla kazdılar ve çukur hazır oldu.»
   - Açıklama: Bir önceki cümlede anlatılan sırayla kazma 'sırayla' kelimesiyle gereksiz yere yeniden söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0014` birebir aynı, `@degisim: ucuz -> küçük` (tutuyorsan), ardından `@onarim: 018087c0b8ee071515c5f37e3e72e0b54a8c5768`, sonra gövde.

### Hikâye 4: tohum masa-0018 (deneme 2 -> 3)

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
Tepede güçlü bir rüzgar esiyordu. Maşa süslü uçurtmasını ve kurdeleli reçel kavanozunu tepeye getirmişti. Ama uçurtma her seferinde dönüp yere düştü, çünkü kuyruğu çok kısaydı. Maşa hiç sıkılmadı ve uçurtmaya dikkatle baktı. Sonra kavanozun uzun, kırmızı kurdelesini gördü. Maşa kurdeleyi çözdü ve uçurtmanın kuyruğuna bağladı. Uçurtma bu kez dönmedi ve yavaş yavaş yükseldi. Maşa ipi sıkıca tuttu ve sevinçle zıpladı. Kırmızı kuyruk rüzgarda sallandı. Maşa uçurtmasını tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa ipi sıkıca tuttu"
   - Cümle 8: «Maşa ipi sıkıca tuttu ve sevinçle zıpladı.»
   - Açıklama: İp kaybolmuşken Maşa sonra aynı ipi tutuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0018` birebir aynı, `@degisim: lamba -> uçurtma` (tutuyorsan), ardından `@onarim: 9f9e1a6f96c7d590549c5f72fdaf159a27055cd3`, sonra gövde.

### Hikâye 5: tohum masa-0019 (deneme 3 -> 4)

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
@degisim: utanmak -> çizmek
Ormanda her yer karla kaplıydı. Maşa kar tanelerinin küçük yıldızlara benzediğini fark etti. Maşa da ince bir çubukla yıldız çizmek istedi, ama çubuk kırıldı. Maşa ağaçların altında yeni bir çubuk aradı. Sonunda kalın ve sağlam bir çubuk buldu. Maşa bu çubukla yeniden denedi. Çubuğu karda yavaş ve temkinli çekti. Yıldızın beş ucunu tek tek çizdi. Çubuk bu kez hiç kırılmadı. Artık karda büyük bir yıldız vardı. Maşa çok sevindi, çünkü kocaman yıldızını sonunda çizmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa da ince bir çubukla"
   - Cümle 3: «Maşa da ince bir çubukla yıldız çizmek istedi, ama çubuk kırıldı.»
   - Açıklama: Başka kimse çizmediği halde 'da' kullanılmış; bağlaç anlamsız.
   - Açıklama: Daha önce yıldız çizen kimse olmadığı için 'da' bağlacı yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karda yavaş ve temkinli çekti"
   - Cümle 7: «Çubuğu karda yavaş ve temkinli çekti.»
   - Açıklama: 'Temkinli' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yavaş ve temkinli çekti"
   - Cümle 7: «Çubuğu karda yavaş ve temkinli çekti.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0019` birebir aynı, `@degisim: utanmak -> çizmek` (tutuyorsan), ardından `@onarim: e4a6fb7b2c8c6359c180c10e8dc0a370d8a5e59f`, sonra gövde.

### Hikâye 6: tohum masa-0021 (deneme 3 -> 4)

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
Maşa reçelini kocaman bir ağacın dibine koydu ve top sektirmeye başladı. Koca Ayı ile sincap da ağacın yanında bir sepete fındık topluyordu. Maşa topa ayakkabısıyla çok sert vurdu ve top sepeti devirdi. Fındıklar yere döküldü ve sincap üzüldü. "Özür dilerim, sincap, dikkat etmedim," dedi Maşa. Sonra Maşa yere eğildi ve fındıkları tek tek topladı. Koca Ayı da ona yardım etti. Kısa sürede sepet yine fındıkla doldu. Sincap sevinçle kuyruğunu salladı. Maşa çok sevdiği reçelini onlarla paylaştı ve üçü mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçelini kocaman bir ağacın dibine koydu"
   - Cümle 1: «Maşa reçelini kocaman bir ağacın dibine koydu ve top sektirmeye başladı.»
   - Açıklama: Reçel iki kez geçiyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0021` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: 4ddb29a507f963856072db2d4eaecb0fc54e2d21`, sonra gövde.

### Hikâye 7: tohum masa-0023 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap, Daşa
@tohum: masa-0023
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'düdük', fiil 'yorulmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | sincap, Daşa
@plan: yorulunca kuzeninin ekmeğini sormadan yedi | özür diledi ve ona reçelli yeni bir ekmek hazırladı
@tohum: masa-0023
Bahçede bir düdük sesi duyuldu. Maşa düdüğüyle yarışı başlatmıştı ve sincapla ağaçların arasında koşuyordu. Maşa çok yoruldu ve Daşa'nın masadaki reçelli ekmeğini sormadan yedi. Biraz sonra Daşa bahçeye geldi ve boş tabağa baktı. "Ekmeğim nerede, Maşa?" diye sordu Daşa. Maşa'nın yüzü kıpkırmızı oldu. "Özür dilerim, Daşa, ekmeğini ben yedim," dedi Maşa. Masada bir ekmek daha vardı. Maşa ona en sevdiği çilek reçelinden bol bol sürdü. Ekmeği iki eliyle Daşa'ya verdi. "Teşekkür ederim, Maşa," dedi Daşa ve gülümsedi. Sonra Maşa, Daşa ve sincap bahçede hep birlikte mutlu mutlu yarıştı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Masada bir ekmek daha vardı"
   - Cümle 8: «Masada bir ekmek daha vardı.»
   - Açıklama: Çözüm için gereken ekmek sebepsizce masada beliriyor.
   - Açıklama: Yeni ekmek önceden kurulmadan tam çözüm anında sebepsizce beliriyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Maşa ona en sevdiği"
   - Cümle 9: «Maşa ona en sevdiği çilek reçelinden bol bol sürdü.»
   - Açıklama: 'ona' ve 'en sevdiği' ekmeği mi Daşa'yı mı gösteriyor belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Maşa ona en sevdiği çilek reçelinden"
   - Cümle 9: «Maşa ona en sevdiği çilek reçelinden bol bol sürdü.»
   - Açıklama: 'ona' zamirinin ekmeği mi Daşa'yı mı gösterdiği, 'en sevdiği'nin de kimin sevdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0023` birebir aynı, ardından `@onarim: ebc5bffd110ac589b21e26e306c95be263af1162`, sonra gövde.

### Hikâye 8: tohum masa-0024 (deneme 2 -> 3)

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
Bir kış sabahı Maşa, Koca Ayı ve kirpi kızak yarışı için tepedeydi. Koca Ayı'nın kızağı hazırdı ama Maşa'nın kızağı görünmüyordu. Kırmızı kızağı, yağan karın altında kalmıştı. "Kızak nerede?" diye sordu Maşa. Önce ağacın önündeki karı kazmayı denedi. Orada yalnız bir taş vardı. Sonra ağacın arkasını kazdı ve bir ip gördü. Maşa ipi çekti ve kızak karın içinden çıktı. Kirpi sevinçle etrafta koştu. Koca Ayı tepenin alçak ve güvenli bir yerini gösterdi. "Hadi, yarışalım!" dedi Maşa. Yarışı Maşa ile kirpi kazandı ve üçü mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kırmızı kızağı, yağan karın altında"
   - Cümle 3: «Kırmızı kızağı, yağan karın altında kalmıştı.»
   - Açıklama: 'Kızağı' iyelik eki sahipsiz kalıyor; 'Maşa'nın kırmızı kızağı' olmalı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Kırmızı kızağı, yağan karın"
   - Cümle 3: «Kırmızı kızağı, yağan karın altında kalmıştı.»
   - Açıklama: Özneden sonra gereksiz virgül var; ayrıca iyelik ekinin sahibi belirtilmemiş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Koca Ayı tepenin alçak ve güvenli bir yerini gösterdi"
   - Cümle 10: «Koca Ayı tepenin alçak ve güvenli bir yerini gösterdi.»
   - Açıklama: Güvenli yer ayrıntısı olayda hiçbir işe yaramıyor.
   - Açıklama: Güvenli yer ayrıntısı kurulup hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yarışı Maşa ile kirpi kazandı"
   - Cümle 12: «Yarışı Maşa ile kirpi kazandı ve üçü mutlu mutlu kaymaya devam etti.»
   - Açıklama: Kızağı hiç anılmayan kirpinin yarışı Maşa ile birlikte kazanması sebepsiz ve sorundan çıkmayan ek bir olay.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Yarışı Maşa ile kirpi kazandı"
   - Cümle 12: «Yarışı Maşa ile kirpi kazandı ve üçü mutlu mutlu kaymaya devam etti.»
   - Açıklama: Kirpinin kızağı hiç yokken yarışı iki kişinin birden kazanması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0024` birebir aynı, ardından `@onarim: b2a525723587210d36b4d65725df5b436d237a47`, sonra gövde.

### Hikâye 9: tohum masa-0026 (deneme 2 -> 3)

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
@plan: çilekleri koyacak bir sepet yoktu | pelerinini bağlayıp küçük bir çanta yaptı
@tohum: masa-0026
@degisim: inanmak -> bağlamak
Ormanda patikanın kenarında yapraklı bitkiler vardı. Maşa yaprakların altında kırmızı çilekler gördü. Onlardan reçel yapmak istedi, ama çilekleri koyacak sepeti yoktu. Maşa önce çilekleri avuçlarına doldurdu. Ama ellerine yalnız birkaç çilek sığdı. Sonra kırmızı pelerinini çıkardı ve yere serdi. Çilekleri tek tek onun üstüne koydu. Sonra pelerinini sıkıca bağladı ve küçük bir çanta yaptı. Çanta çileklerle doldu. Maşa en küçük çileği hemen ağzına attı ve güldü. Sonra çantayı sırtına aldı ve reçel için çileklerini mutlu mutlu taşıdı.
```

**Hakem bulguları (4):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Sonra kırmızı pelerinini çıkardı"
   - Cümle 6: «Sonra kırmızı pelerinini çıkardı ve yere serdi.»
   - Açıklama: Kartın kimlik bilgisinde ve dizide Maşa'nın kırmızı pelerini yok; bu, diziyi izlemiş çocuğa yanlış bir görünüş bilgisi verir.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra pelerinini sıkıca bağladı"
   - Cümle 8: «Sonra pelerinini sıkıca bağladı ve küçük bir çanta yaptı.»
   - Açıklama: 'Sonra' ile başlayan cümle üç kez tekrarlanıyor.
   - Açıklama: Üç cümle üst üste 'Sonra' ile başlıyor; gereksiz tekrar.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa en küçük çileği hemen ağzına attı"
   - Cümle 10: «Maşa en küçük çileği hemen ağzına attı ve güldü.»
   - Açıklama: Ormanda bulunan yabani meyveyi toplayıp hemen yemek çocuğun taklit edebileceği tehlikeli bir davranış.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "en küçük çileği hemen ağzına attı"
   - Cümle 10: «Maşa en küçük çileği hemen ağzına attı ve güldü.»
   - Açıklama: Ormanda bulunan yabani meyveyi yıkamadan hemen yemek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0026` birebir aynı, `@degisim: inanmak -> bağlamak` (tutuyorsan), ardından `@onarim: 5470fab744ff4548ca959ce88919e8542cb1c71b`, sonra gövde.

### Hikâye 10: tohum masa-0027 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0027
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tutkal', fiil 'katlamak', sıfat 'peynirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: tutkal bitti ve yapraklar kağıtta durmadı | yaprakların arkasına yapışkan reçel sürdü
@tohum: masa-0027
Ormanda Maşa kendine bir taç yapıyordu. Bir kağıdı katladı ve üstüne renkli yapraklar koymak istedi. Ama tutkal bitmişti ve yapraklar kağıtta durmuyordu. Maşa piknik sepetini açtı. İçinde peynirli bir sandviç ve bir kavanoz çilek reçeli vardı. Reçel çok yapışkandı. Maşa parmağıyla yaprakların arkasına ondan biraz sürdü. Sonra yaprakları kağıda bastırdı. Bu sefer hepsi sıkıca yapıştı. Taç çok güzel oldu, ama çilek gibi kokuyordu. Maşa tacı başına taktı ve güldü. Sonra yapış yapış parmaklarını yaladı. En son sandviçini yedi ve tacıyla oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İçinde peynirli bir sandviç"
   - Cümle 5: «İçinde peynirli bir sandviç ve bir kavanoz çilek reçeli vardı.»
   - Açıklama: Sandviç çözüme hiç katkı vermiyor; işlevsiz bir ayrıntı olarak kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0027` birebir aynı, ardından `@onarim: bc61b83355ea7747a7f711f73c11d5cd071884bd`, sonra gövde.

### Hikâye 11: tohum masa-0028 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0028
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kova', fiil 'seyretmek', sıfat 'şaşkın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: ağacın altından garip bir ses geldi | taşın arkasına baktı, sonra ağacı sessizce seyretti
@tohum: masa-0028
Tepede serin bir rüzgar esiyordu. Maşa ile Koca Ayı kozalak toplamaya gelmişti ve kovaları ağacın altındaydı. Birden ağacın altından garip bir ses geldi. "Bu ses nereden geliyor?" diye sordu Maşa. Koca Ayı da şaşkın bir yüzle omuzlarını kaldırdı. Maşa önce yakındaki büyük bir taşın arkasına bakmayı denedi. Orada hiçbir şey yoktu. Sonra ağacın dibine oturdu ve dalları seyretti. Dallar sallandı ve bir kozalak boş kovanın içine düştü. Kovadan yine aynı ses geldi. "Sesi kovaya düşen kozalak yapıyormuş!" dedi Maşa. Koca Ayı güldü ve kozalağı kovadan çıkardı. Maşa çok sevindi, çünkü sesi yapan şeyi kendisi bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "taşın arkasına bakmayı denedi"
   - Cümle 6: «Maşa önce yakındaki büyük bir taşın arkasına bakmayı denedi.»
   - Açıklama: Bakmak denenecek bir iş değil; 'bakmayı denedi' anlamca uygunsuz, 'arkasına baktı' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "yakındaki büyük bir taşın arkasına bakmayı denedi"
   - Cümle 6: «Maşa önce yakındaki büyük bir taşın arkasına bakmayı denedi.»
   - Açıklama: Sesin ağacın altından geldiği söylenmişken taşın arkasına bakmak sebebe yönelmeyen boşa bir adım.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra ağacın dibine oturdu ve dalları seyretti"
   - Cümle 8: «Sonra ağacın dibine oturdu ve dalları seyretti.»
   - Açıklama: Çözüm sebebe yönelmiyor; ses Maşa'nın bir eylemiyle değil tesadüfen düşen kozalakla çözülüyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bir kozalak boş kovanın içine düştü"
   - Cümle 9: «Dallar sallandı ve bir kozalak boş kovanın içine düştü.»
   - Açıklama: Sorun kovaya düşen bir kozalağın sesi; çocuğun önemseyeceği bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0028` birebir aynı, ardından `@onarim: 19b9c4ccd04a884acfaef60509d52624a901ff9b`, sonra gövde.

### Hikâye 12: tohum masa-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0029
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'fırça', fiil 'aramak', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: yağmur dinmişti ama fırça yine ıslanıyordu | yukarı bakıp damlayan dalı buldu ve fırçayı taşıdı
@tohum: masa-0029
Bir sabah Maşa bahçede resim yapmak istedi. Ama masadaki fırçası sırılsıklamdı. Yağmur çoktan dinmişti ama fırça yine ıslanıyordu. Maşa bu suyun nereden geldiğini merak etti ve aramaya başladı. Masanın yanında durdu ve yukarıya bakmayı denedi. Masanın üstünde ağacın yapraklı bir dalı vardı. Rüzgar esince yapraklardan fırçanın üstüne damlalar düştü. Su, yapraklarda kalan yağmurdan geliyordu. Maşa kağıdını ve fırçasını güneşli bir köşeye taşıdı. Fırça güneşte kurudu ve Maşa resmine başladı. Maşa bundan sonra ıslak bir şey görünce önce yukarıya baktı.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa bahçede resim yapmak istedi"
   - Cümle 1: «Bir sabah Maşa bahçede resim yapmak istedi.»
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yukarıya bakmayı denedi"
   - Cümle 5: «Masanın yanında durdu ve yukarıya bakmayı denedi.»
   - Açıklama: Bakmak denenen bir iş değil; 'denedi' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0029` birebir aynı, ardından `@onarim: 6bf575e2dd317a88f1977249dce5a0c8cd6fdd3c`, sonra gövde.
