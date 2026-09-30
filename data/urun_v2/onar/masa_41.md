# Editör görevi (onarım): Maşa, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar41.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0118 (deneme 4 -> 5)

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
Bahçede rüzgar esiyordu. Maşa kırılgan çubuklardan yapılmış bir uçurtma uçuruyordu. Birden sert bir rüzgar esti ve uçurtmanın ipliği bir çalıya takıldı. Maşa ipliği çekti ama uçurtma çalıdan çıkmadı. Çubuklar eğildi ve kırılacak gibi oldu. Maşa hemen durdu ve çekmek yerine çözmeyi denedi. Çalının yanına yürüdü ve ipliği dallardan tek tek çözdü. Sonra uçurtmayı iki eliyle yavaşça dışarı aldı. Çubukların hiçbiri kırılmamıştı. Maşa bahçenin ortasına koştu ve uçurtmayı yeniden havaya kaldırdı. Uçurtma rüzgarla yükseldi ve Maşa sevinçle güldü. Maşa bundan sonra uçurtmasını hep çalılardan uzakta uçurdu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa kırılgan çubuklardan yapılmış"
   - Cümle 2: «Maşa kırılgan çubuklardan yapılmış bir uçurtma uçuruyordu.»
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kırılgan çubuklardan yapılmış"
   - Cümle 2: «Maşa kırılgan çubuklardan yapılmış bir uçurtma uçuruyordu.»
   - Açıklama: 'Kırılgan' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0118` birebir aynı, `@degisim: yakalanmak -> takılmak` (tutuyorsan), ardından `@onarim: 1e6bb66930fce8fc96ff2718cfcb2d2edd0d35b4`, sonra gövde.

### Hikâye 2: tohum masa-0127 (deneme 3 -> 4)

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
@plan: fındıklar tepeden aşağı yuvarlandı | fındıkları boş reçel kavanozuna koyup bir dala astı
@tohum: masa-0127
@degisim: elmas -> kurdele
Maşa tepede hareketli sincap için bir sürpriz hazırlıyordu. Sincabın ağacının dibine fındık koyup kırmızı bir kurdeleyle süslemek istedi. Ama tepe yokuştu ve fındıklar hemen aşağı yuvarlandı. Maşa fındıkları yerden topladı ve biraz düşündü. Maşa bütün reçeli yemişti ve çantasında boş bir kavanoz vardı. Fındıkları kavanoza koydu. Sonra kavanozu kurdeleyle bağladı ve alçak bir dala astı. Kavanoz hiç kıpırdamadı ve fındıklar içinde kaldı. Biraz sonra sincap ağaçtan indi ve kavanozu gördü. "Sürpriz, sincap! Bu fındıklar senin için," dedi Maşa. Sincap kavanozdan fındıkları tek tek aldı ve kuyruğunu salladı. Maşa bundan sonra boş reçel kavanozlarını hiç atmadı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama tepe yokuştu"
   - Cümle 3: «Ama tepe yokuştu ve fındıklar hemen aşağı yuvarlandı.»
   - Açıklama: 'Yokuş' burada sıfat olarak yanlış kullanılmış; 'tepe dikti' olmalı.
   - Açıklama: Tepe yokuş olmaz; 'tepe dikti' ya da 'yer yokuştu' gibi uygun bir yüklem gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0127` birebir aynı, `@degisim: elmas -> kurdele` (tutuyorsan), ardından `@onarim: c941f63222431ad6bf19df1a9a376b16e24d5dfd`, sonra gövde.

### Hikâye 3: tohum masa-0131 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ayı ile kirpi aşağıda çiçek topluyordu ve bulutu görmedi | ekmeğe reçel sürdü ve kokusuyla onları tepeye çağırdı
@tohum: masa-0131
@degisim: fasulye -> çiçek
Maşa tepede, ferah bir çimenlikte piknik yapıyordu. Birden gökyüzünde kalp şeklinde kocaman bir bulut fark etti. Ama Koca Ayı ile kirpi aşağıda çiçek topluyordu ve gökyüzüne hiç bakmıyordu. Maşa "Yukarı bakın!" diye seslendi, ama onlar çok uzaktaydı ve duymadı. Maşa onları reçel kokusuyla çağırmayı planladı. Kavanozunu açtı ve üç dilim ekmeğe bol bol reçel sürdü. Reçelin tatlı kokusu rüzgarla aşağıya gitti. Koca Ayı kokuyu aldı, çiçekleri bıraktı ve kirpiyle tepeye geldi. "Bakın, kalp şeklinde bir bulut!" dedi Maşa ve gökyüzünü gösterdi. Koca Ayı ile kirpi yukarı baktı ve sevinçle ses çıkardı. Üçü çimenlikte ekmeklerini yiyip bulutu mutlu mutlu izledi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah bir çimenlikte"
   - Cümle 1: «Maşa tepede, ferah bir çimenlikte piknik yapıyordu.»
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "gökyüzüne hiç bakmıyordu"
   - Cümle 3: «Ama Koca Ayı ile kirpi aşağıda çiçek topluyordu ve gökyüzüne hiç bakmıyordu.»
   - Açıklama: Arkadaşların bir bulutu görmemesi zayıf ve önemsiz bir sorun; gerçek bir güçlük yaratmıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "onlar çok uzaktaydı ve duymadı"
   - Cümle 4: «Maşa "Yukarı bakın!" diye seslendi, ama onlar çok uzaktaydı ve duymadı.»
   - Açıklama: Açık 'onlar' öznesiyle fiil çoğul olmalı: 'duymadılar'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0131` birebir aynı, `@degisim: fasulye -> çiçek` (tutuyorsan), ardından `@onarim: 1d57493ded964ea7508ebed90111a7450568482a`, sonra gövde.

### Hikâye 4: tohum masa-0132 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0132
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'leke', fiil 'uzatmak', sıfat 'düzgün'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: top kocaman bir çalının altına kaçtı | kirpiye reçel uzatıp ondan yardım istedi
@tohum: masa-0132
@degisim: düzgün -> kocaman
Maşa evinin önünde kırmızı topuyla oynuyordu. Yanında bir kavanoz reçel ve bir kaşık vardı. Birden top yere çarpıp zıpladı ve kocaman bir çalının altına kaçtı. Maşa kolunu dalların arasına soktu ama topa yetişemedi. O sırada çalının yanından küçük bir kirpi geçti. Maşa kirpiden yardım istemeye karar verdi. Kaşığa biraz reçel koydu ve kirpiye uzattı. Sonra parmağıyla çalının altını gösterdi. Kirpi kaşığı yaladı ve dalların altına girdi. Burnuyla topu dışarı itti. Top yuvarlandı ve Maşa'nın ayağına geldi. Kirpi burnunda küçük bir reçel lekesiyle çıktı. Maşa güldü ve lekeyi bir yaprakla sildi. Maşa çok mutlu oldu, çünkü kirpi ona topu geri getirmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanında bir kavanoz reçel ve bir kaşık vardı"
   - Cümle 2: «Yanında bir kavanoz reçel ve bir kaşık vardı.»
   - Açıklama: Top oynarken reçel kavanozu ve kaşık sebepsizce hazır bulunuyor ve çözümü getiriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kaşığa biraz reçel koydu ve kirpiye uzattı"
   - Cümle 7: «Kaşığa biraz reçel koydu ve kirpiye uzattı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde yabani bir kirpiye elle reçel yediriliyor ve yüzüne dokunuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0132` birebir aynı, `@degisim: düzgün -> kocaman` (tutuyorsan), ardından `@onarim: f9b27a7dfc3c3e95345d28a96afcd5b33100a3c6`, sonra gövde.

### Hikâye 5: tohum masa-0134 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı
@tohum: masa-0134
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yağmur ya da kar günü
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'nota', fiil 'kurtulmak', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı
@plan: yağmur pikniği bozdu ve ayı çok üzüldü | ağacın altında boş kavanozla yağmur şarkısı yaptı
@tohum: masa-0134
@degisim: utangaç -> boş
Ormanda Maşa ile Koca Ayı piknik yapıyordu. Birden yağmur başladı ve piknik yarım kaldı. Koca Ayı buna çok üzüldü. İkisi sepeti alıp büyük bir ağacın altına koştu ve yağmurdan kurtuldu. Maşa pikniği orada da eğlenceli yapmak istedi. Sepette biraz reçel kalmıştı. Maşa reçeli çok severdi ve son kaşığını hemen yedi. Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu. Damlalar kavanoza ve bardaklara düşünce farklı notalar çıktı. "Dinle, Koca Ayı, bu bizim yağmur şarkımız!" dedi Maşa. Koca Ayı gülümsedi ve başını salladı. İkisi ağacın altında pikniğe devam etti. Maşa çok sevindi, çünkü Koca Ayı artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "düşünce farklı notalar çıktı"
   - Cümle 9: «Damlalar kavanoza ve bardaklara düşünce farklı notalar çıktı.»
   - Açıklama: Nota yazılı işarettir; damlalardan nota değil ses çıkar.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düşünce farklı notalar çıktı"
   - Cümle 9: «Damlalar kavanoza ve bardaklara düşünce farklı notalar çıktı.»
   - Açıklama: 'Nota' 3 yaşındaki çocuğun bilmeyeceği bir kavram; 'farklı sesler' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0134` birebir aynı, `@degisim: utangaç -> boş` (tutuyorsan), ardından `@onarim: 23a0b9cb734977269032dfeeefb6a359904fc4da`, sonra gövde.

### Hikâye 6: tohum masa-0138 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0138
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kavun', fiil 'çekilmek', sıfat 'şeffaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: ağacın arkasındaki yapraklardan bir ses geldi | yere kavun bırakıp geri çekildi ve kirpiyi gördü
@tohum: masa-0138
@degisim: şeffaf -> mavi
Bir sabah Maşa ormanda bir kütüğün üstünde oturuyordu. Mavi bir kutudan dilim dilim kavun yiyordu. Birden ağacın arkasındaki kuru yapraklar hışır hışır ses çıkardı. Maşa bu sesi çok merak etti. "Orada kim var?" diye seslendi Maşa. Ama ses hemen kesildi. Bu kez Maşa başka bir şey denedi. Kütüğün yanına bir dilim kavun koydu ve biraz geri çekildi. Az sonra ağacın arkasından küçük bir kirpi çıktı. Kirpi yavaşça yaklaştı ve kavunu kokladı. Sonra kavunu afiyetle yemeye başladı. "Demek o ses sendin," dedi Maşa gülerek. Maşa çok sevindi, çünkü sesi yapan kirpiyi bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağacın arkasındaki kuru yapraklar hışır hışır ses çıkardı"
   - Cümle 3: «Birden ağacın arkasındaki kuru yapraklar hışır hışır ses çıkardı.»
   - Açıklama: Yapraklardaki bir ses gerçek bir sorun değil, yalnız bir merak konusu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0138` birebir aynı, `@degisim: şeffaf -> mavi` (tutuyorsan), ardından `@onarim: 54aa47acd5e5981b48502287af682b9af389ec32`, sonra gövde.

### Hikâye 7: tohum masa-0141 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0141
- yer: dağ (Ormanın yanındaki tepe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yatak', fiil 'temizlenmek', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: kuzeninin yiyeceği yoktu ve tek ekmek vardı | reçelli ekmeğini ikiye bölüp kuzeniyle paylaştı
@tohum: masa-0141
@degisim: yatak -> kırıntı
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa çimenlerin üstünde oturuyordu. Maşa'nın elinde tek bir reçelli ekmek vardı, ama Daşa'nın yiyeceği yoktu. Daşa şehirden gelirken çantasını evde unutmuştu. Maşa reçeli çok severdi, ama ekmeğini hemen ikiye böldü. "Al, Daşa, yarısı senin!" dedi Maşa. "Teşekkürler, Maşa!" dedi Daşa. Ekmekten çimenlere birkaç kırıntı düştü. Bir kayanın arkasında saklı bir sincap onlara bakıyordu. Maşa kırıntıları sincap için orada bıraktı. Sincap hemen dışarı çıktı ve kırıntıları yedi. Böylece çimenler temizlendi. Maşa bundan sonra ekmeğini hep dostlarıyla paylaştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir kayanın arkasında saklı bir sincap"
   - Cümle 9: «Bir kayanın arkasında saklı bir sincap onlara bakıyordu.»
   - Açıklama: Sorun çözüldükten sonra sorunla ilgisiz bir sincap ve kırıntı olayı ekleniyor.
   - Açıklama: Sincap ve kırıntılar sorunla ilgisiz, sonradan eklenmiş işlevsiz bir yan olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0141` birebir aynı, `@degisim: yatak -> kırıntı` (tutuyorsan), ardından `@onarim: 6a0a584b812525efe956292fdad7ab5c5d7318f0`, sonra gövde.

### Hikâye 8: tohum masa-0143 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0143
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pasta', fiil 'oynamak', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: yalnızdı ve oynayacak bir arkadaşı yoktu | kirpiye reçelli pasta verip oyuna çağırdı
@tohum: masa-0143
Bir sabah tepede ılık bir rüzgar esiyordu. Maşa çimenlere oturmuş, reçelli pastasını yiyordu. Ama Maşa yalnızdı ve oynayacak bir arkadaşı yoktu. O sırada taşın yanında küçük bir kirpi gördü. Maşa onunla arkadaş olmak ve oynamak istedi. Pastasından bir parça kopardı. Parçayı yavaşça taşın yanına koydu. "Bu senin için, gel birlikte yiyelim," dedi Maşa. Kirpi parçayı kokladı ve hemen yedi. Sonra Maşa'nın yanına geldi. Maşa yerden bir çam kozalağı aldı ve kirpiye doğru yuvarladı. Kirpi kozalağı burnuyla geri itti. "Sen çok iyi oynuyorsun!" dedi Maşa gülerek. Maşa çok mutluydu, çünkü artık kirpiyle arkadaş olmuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kirpi parçayı kokladı ve hemen yedi"
   - Cümle 9: «Kirpi parçayı kokladı ve hemen yedi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde yabani bir kirpiye reçelli pasta yediriliyor.
   - Açıklama: Yabani bir hayvana reçelli pasta yedirmek çocuğun taklit edebileceği uygunsuz bir davranış ve kartta kirpi elma sever.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0143` birebir aynı, ardından `@onarim: 5628a79adb1dc382fcab00b6ef775e41b8057c01`, sonra gövde.

### Hikâye 9: tohum masa-0150 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0150
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'zincir', fiil 'saklanmak', sıfat 'çalışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: papatyaları bağladı ama ince bir sap koptu | her sapı parmağıyla deldi ve çiçekleri deliklerden geçirdi
@tohum: masa-0150
@degisim: saklanmak -> bağlamak
Çalışkan arılar çiçeklerin arasında vızıldıyordu. Maşa ormanda ilk kez papatyalardan bir zincir yapıyordu. Maşa papatyaları birbirine bağladı ama bir papatyanın ince sapı hemen koptu. Zincir dağıldı ve çiçekler yere düştü. Maşa durmadı ve yeniden denedi. Parmağıyla her sapı ortasından deldi. Sonra bir çiçeği öbür çiçeğin deliğinden geçirdi. Bu kez zincir hiç kopmadı. Maşa bir sürü papatyayı arka arkaya dizdi. Sonra uzun zinciri bir halka yaptı ve başına taç gibi taktı. Maşa bundan sonra papatya zincirini hep böyle yaptı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "öbür çiçeğin deliğinden geçirdi"
   - Cümle 7: «Sonra bir çiçeği öbür çiçeğin deliğinden geçirdi.»
   - Açıklama: Delik çiçekte değil sapta açılmıştı; kelime yanlış yere bağlanmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0150` birebir aynı, `@degisim: saklanmak -> bağlamak` (tutuyorsan), ardından `@onarim: bce84cb46a878d9023c2b3c63cfd13d0426b0ccd`, sonra gövde.

### Hikâye 10: tohum masa-0151 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0151
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bez', fiil 'korumak', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: reçel için çilek arıyordu ama hiç göremedi | her yeri kokladı ve çilekleri yaprakların altında buldu
@tohum: masa-0151
Maşa sepetiyle ormandaki patikada yürüyordu. Reçel yapmak için çilek arıyordu ama bir tane bile göremedi. Patikanın kenarı büyük yapraklarla kaplıydı. Maşa somurtkan bir yüzle bir ağacın altına oturdu. Birden tatlı bir koku aldı. Maşa reçeli çok severdi ve bu kokuyu hemen tanıdı. Bu, çilek reçelinin kokusuna benziyordu. Maşa kokunun nereden geldiğini çok merak etti. Yere eğildi ve her yeri kokladı. Koku büyük yaprakların altından geliyordu. Maşa yaprakları kaldırdı ve kırmızı çilekleri gördü. Çilekleri toplayıp sepetine doldurdu. Sonra onları ezilmekten korumak için sepetteki beze sardı. Maşa çok sevindi, çünkü reçel için çilekleri bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa somurtkan bir yüzle"
   - Cümle 4: «Maşa somurtkan bir yüzle bir ağacın altına oturdu.»
   - Açıklama: 'Somurtkan' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Somurtkan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepetteki beze sardı"
   - Cümle 13: «Sonra onları ezilmekten korumak için sepetteki beze sardı.»
   - Açıklama: Bez daha önce kurulmadan beliriyor ve sorunla ilgisiz işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0151` birebir aynı, ardından `@onarim: 7b614be408b46b2e4c49119970f5b167ef9972b4`, sonra gövde.

### Hikâye 11: tohum masa-0154 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0154
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'baharat', fiil 'ıslatmak', sıfat 'güneşli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi baharatlı elmayı kokladı ve yemedi | elma dilimini suyla ıslattı ve üstünü sildi
@tohum: masa-0154
Güneşli bir gündü ve ormanda kuşlar ötüyordu. Koca Ayı, Maşa'ya baharatlı elma dilimleri ve bir şişe su verdi. Maşa bir dilimi kirpiye verdi, ama kirpi baharatı kokladı ve yemedi. Maşa elmasını kirpiyle paylaşmak istedi. Hemen yeni bir şey denedi. Bir elma dilimini şişedeki suyla ıslattı ve üstünü parmağıyla sildi. Sonra dilimi kirpiye uzattı. "Kirpi, bu sana, afiyet olsun!" dedi Maşa. Kirpi dilimi kokladı ve bu kez hemen yedi. Sonra burnunu Maşa'nın eline sürdü. Koca Ayı da gülümsedi ve başını salladı. Maşa çok sevindi, çünkü elmasını kirpiyle paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Maşa elmasını kirpiyle paylaşmak istedi"
   - Cümle 4: «Maşa elmasını kirpiyle paylaşmak istedi.»
   - Açıklama: Dilim zaten verilmişken paylaşma isteği gereksizce tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0154` birebir aynı, ardından `@onarim: e38d9ab6e31e558d6a3444d36da2f5acd0922004`, sonra gövde.

### Hikâye 12: tohum masa-0155 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0155
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'bambu', fiil 'yağmak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: dönerken uçurtmanın ipi ayaklarına dolandı ve karıştı | ipi çözdü ve boş reçel kavanozuna sardı
@tohum: masa-0155
@degisim: bambu -> uçurtma
Tepede yağmur yağmıyordu ve güzel bir rüzgar esiyordu. Maşa çok sevdiği reçelin hepsini yemişti ve kavanoz boştu. Maşa uçurtmasıyla dönerken ip ayaklarına dolandı ve karmakarışık oldu. Uçurtma yere indi ve Maşa buna çok güldü. Sonra çimlere oturdu ve ipi ayaklarından dikkatle çözdü. İpi boş kavanozun etrafına düzgünce sardı. Artık ip hiç karışmıyordu. Rüzgar esince Maşa ipi kavanozdan yavaş yavaş bıraktı. Uçurtma yeniden havaya yükseldi. Maşa kavanozu sıkıca tuttu ve uçurtma oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Uçurtma yere indi ve Maşa buna çok güldü"
   - Cümle 4: «Uçurtma yere indi ve Maşa buna çok güldü.»
   - Açıklama: Maşa karışan ipe gülüyor, bu yüzden sorun önemsenecek bir şey gibi kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0155` birebir aynı, `@degisim: bambu -> uçurtma` (tutuyorsan), ardından `@onarim: de1713b8bc133e0e18a8f7b9a61083e4d95154b3`, sonra gövde.
