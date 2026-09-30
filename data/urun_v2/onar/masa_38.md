# Editör görevi (onarım): Maşa, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0155 (deneme 2 -> 3)

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
Tepede yağmur yağmıyordu ve güzel bir rüzgar esiyordu. Maşa uçurtmasını tutarak çimenlerin üstünde dönüyordu. Ama dönerken ip ayaklarına dolandı ve karmakarışık oldu. Uçurtma yere indi ve Maşa buna çok güldü. Sepetinde boş bir reçel kavanozu vardı. Az önce içindeki reçelin hepsini yemişti. Maşa ipin ucunu kavanoza bağladı. Sonra ipi dikkatle çözdü ve kavanozun etrafına sardı. Artık ip kavanozda düzgünce duruyordu. Rüzgar esince Maşa ipi kavanozdan yavaş yavaş bıraktı. Uçurtma yeniden havaya yükseldi. Maşa kavanozu sıkıca tuttu ve uçurtma oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepetinde boş bir reçel kavanozu vardı"
   - Cümle 5: «Sepetinde boş bir reçel kavanozu vardı.»
   - Açıklama: Sepet ve kavanoz çözümü getirmek için sebepsizce beliriyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa ipin ucunu kavanoza bağladı"
   - Cümle 7: «Maşa ipin ucunu kavanoza bağladı.»
   - Açıklama: Çözüm ipi kavanoza bağlama, çözme ve sarma olarak ikiden fazla adım sürüyor; kavanoz dolanmanın sebebine yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0155` birebir aynı, `@degisim: bambu -> uçurtma` (tutuyorsan), ardından `@onarim: 5c02a5394ce1e0b37b824af03faec4cc15eea27b`, sonra gövde.

### Hikâye 2: tohum masa-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0156
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kumaş', fiil 'beğenmek', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: tepede nereden geldiği bilinmeyen bir ses vardı | sessizce dinledi ve sesi kayanın arkasında buldu
@tohum: masa-0156
Maşa ile Daşa tepede bir kumaşın üstünde piknik yapıyordu. Sepette reçelli kurabiyeler vardı. Birden yakından çıtır çıtır bir ses geldi. Ama ikisi de bir şey yemiyordu. "Kurabiyeleri kim yiyor?" diye sordu Daşa. Maşa reçelli kurabiyeleri çok severdi ve tadını iyi bilirdi. "Kurabiyelerimiz yumuşak, Daşa, bu ses onlardan gelmiyor!" dedi Maşa. Maşa sessizce durdu ve dinledi. Ses büyük bir kayanın arkasından geliyordu. İkisi yavaşça kayanın arkasına baktı. Orada bir sincap fındık kırıyordu. Ses fındığın kabuğundan geliyordu. Sincap fındığını çok beğenmiş gibi kuyruğunu salladı. Maşa çok güldü, çünkü çıtır sesi yapan küçük bir sincaptı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçelli kurabiyeleri çok severdi ve tadını iyi bilirdi"
   - Cümle 6: «Maşa reçelli kurabiyeleri çok severdi ve tadını iyi bilirdi.»
   - Açıklama: Tohumdaki reçel özelliği iki kez anılıyor ve sorunun çözümünde (sesi dinleyip kayanın arkasında bulmak) işe yaramıyor.
   - Açıklama: Tohumdaki reçel sevgisi sorunu çözmekte işe yaramıyor; ses sessizce dinlenerek bulunuyor, bu da kartın özellik kullanımına tam uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa reçelli kurabiyeleri çok severdi ve tadını iyi bilirdi"
   - Cümle 6: «Maşa reçelli kurabiyeleri çok severdi ve tadını iyi bilirdi.»
   - Açıklama: Kurabiyenin tadını bilmek sesin kaynağını bulmakla ilgisiz, özelliği göstermek için eklenmiş işlevsiz bir ayrıntı.
   - Açıklama: Maşa'nın kurabiye sevgisi çözüme katkısı olmayan işlevsiz bir ayrıntı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok beğenmiş gibi kuyruğunu"
   - Cümle 13: «Sincap fındığını çok beğenmiş gibi kuyruğunu salladı.»
   - Açıklama: 'Beğenmiş gibi' benzetmesi küçük çocuk için soyut bir çıkarım.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü çıtır sesi yapan küçük bir sincaptı"
   - Cümle 14: «Maşa çok güldü, çünkü çıtır sesi yapan küçük bir sincaptı.»
   - Açıklama: Cümlenin öznesi eksik; 'sesi yapan şey küçük bir sincaptı' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0156` birebir aynı, ardından `@onarim: 59795318bda7e6397e2c2e7d0acafea1b7bf2546`, sonra gövde.

### Hikâye 3: tohum masa-0158 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0158
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'minder', fiil 'dolanmak', sıfat 'yaratıcı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: tüy iki taşın arasındaki dar bir yere düştü | çubuğun ucuna reçel sürdü ve tüyü çıkardı
@tohum: masa-0158
@degisim: yaratıcı -> komik
Bir sabah Maşa dağda minderine oturmuş, kavanozdan reçel yiyordu. Sonra minderden çıkan beyaz bir tüyle komik bir oyun buldu. Tüyü havaya üfledi ama tüy iki taşın arasındaki dar bir yere düştü. Maşa taşların etrafında dolandı. Eli bu dar yere sığmadı. Maşa yerde ince bir çubuk buldu. En sevdiği reçelden biraz aldı ve çubuğun ucuna sürdü. Çubuğu yavaşça taşların arasına uzattı. Tüy reçele yapıştı. Maşa çubuğu çekti ve tüy dışarı çıktı. Tüyün ucunu çimlere silip temizledi. Sonra onu yine havaya üfledi ve oyununa devam etti. Maşa çok sevindi, çünkü tüyünü geri almıştı.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Bir sabah Maşa dağda"
   - Cümle 1: «Bir sabah Maşa dağda minderine oturmuş, kavanozdan reçel yiyordu.»
   - Açıklama: Kartın dağ tarifi ve kararı bu yeri ormanın yanındaki tepe olarak tanımlıyor; dizide 'dağ' adıyla geçen yer yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0158` birebir aynı, `@degisim: yaratıcı -> komik` (tutuyorsan), ardından `@onarim: dc817d3368091859420583eadc85b4cc611ada54`, sonra gövde.

### Hikâye 4: tohum masa-0159 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0159
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'fıçı', fiil 'saymak', sıfat 'yuvarlak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: aç bir kirpi elma arıyordu ama yakında elma yoktu | fıçıdaki elma reçelinden kirpiye biraz verdi
@tohum: masa-0159
Bir sabah Maşa ile Koca Ayı ormandaki patikada yürüyordu. Koca Ayı kucağında küçük, yuvarlak bir fıçı taşıyordu. Patikada aç bir kirpi elma arıyordu ama yakında hiç elma yoktu. Kirpi Maşa'ya baktı ve burnunu kıpırdattı. "Koca Ayı, kirpi çok acıkmış," dedi Maşa. Maşa fıçının kapağını açtı. İçinde en sevdiği elma reçeli vardı. Koca Ayı ona bir kaşık uzattı. Maşa bir yaprağın üstüne üç kaşık reçel koydu. "Bir kaşık, iki kaşık, üç kaşık," diye saydı Maşa. Kirpi yaprağa koştu ve reçeli yedi. Sonra Maşa'nın ayağının yanına mutlu mutlu oturdu. Koca Ayı gülümsedi ve fıçıyı kapattı. "Afiyet olsun, küçük kirpi!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İçinde en sevdiği elma"
   - Cümle 7: «İçinde en sevdiği elma reçeli vardı.»
   - Açıklama: Fıçıyı Koca Ayı taşıyor, son özne Maşa; reçeli en çok kimin sevdiği belli değil.
   - Açıklama: 'En sevdiği' reçelin kimin en sevdiği olduğu belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Koca Ayı ona bir kaşık"
   - Cümle 8: «Koca Ayı ona bir kaşık uzattı.»
   - Açıklama: 'Ona' Maşa'yı mı kirpiyi mi gösteriyor belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0159` birebir aynı, ardından `@onarim: fef4f1e8df74a3b86d30dea90c9bf99e78b20c71`, sonra gövde.

### Hikâye 5: tohum masa-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0160
- yer: dağ (Ormanın yanındaki tepe.)
- tema: bir şey yapmak
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'mektup', fiil 'hatırlamak', sıfat 'hazırlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: rüzgar uçurtmanın kağıt kuyruğunu kopardı | kuyruğu reçelle uçurtmaya yeniden yapıştırdı
@tohum: masa-0160
@degisim: mektup -> uçurtma
Dağda serin bir rüzgar esiyordu. Maşa hazırlıklı gelmişti ve kağıttan bir uçurtma yapmıştı. Ama rüzgar uçurtmanın kağıt kuyruğunu koparıp çimlere attı. Kuyruğun ucu yırtılmıştı ve artık bağlanmıyordu. Maşa biraz düşündü ve çantasındaki reçel kavanozunu hatırladı. Kavanozu açtı ve kuyruğun ucuna biraz reçel sürdü. Kuyruğu uçurtmanın altına bastırdı ve kuyruk sıkıca yapıştı. Maşa parmağındaki reçeli de yaladı ve güldü. Sonra uçurtmanın ipini tuttu ve tepede koştu. Rüzgar uçurtmayı havaya kaldırdı. Uzun kuyruk da gökyüzünde sallandı. Maşa uçurtmasını mutlu mutlu uçurdu.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Dağda serin bir rüzgar esiyordu"
   - Cümle 1: «Dağda serin bir rüzgar esiyordu.»
   - Açıklama: Kartın dağ tarifi ve kararı yeri ormanın yanındaki tepe olarak verir; hikaye yeri dağ diye anıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kuyruğun ucuna biraz reçel sürdü"
   - Cümle 6: «Kavanozu açtı ve kuyruğun ucuna biraz reçel sürdü.»
   - Açıklama: Kartın özelliği reçeli çok sevmek; reçel burada yapıştırıcı olarak kullanılıyor, özellik karttaki gibi işlemiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0160` birebir aynı, `@degisim: mektup -> uçurtma` (tutuyorsan), ardından `@onarim: 78095ba75790542ed66fd5fd248837c0bd4beaf4`, sonra gövde.

### Hikâye 6: tohum masa-0161 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap
@tohum: masa-0161
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'flüt', fiil 'birleştirmek', sıfat 'yavaş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | sincap
@plan: sincabın fındığı flütün içinde sıkıştı | flütün ucundan üfledi ve fındığı çıkardı
@tohum: masa-0161
Evin önündeki bahçede Maşa flütünün iki parçasını temizliyordu. Bir sincap geldi ve bir parçaya küçük bir fındık sakladı. Ama fındık bu dar yerde sıkıştı ve dışarı çıkmadı. Sincap üzgün üzgün Maşa'ya baktı. "Üzülme, sincap, sana yardım ederim," dedi Maşa. Maşa önce parçayı salladı ama fındık yerinden oynamadı. Sonra parçanın öbür ucundan hızla üflemeyi denedi. Fındık "pıt" diye çimlere fırladı. Sincap fındığını hemen kaptı ve sevinçle zıpladı. Maşa iki parçayı birleştirdi ve yavaş bir şarkı çaldı. Sincap şarkıya göre kuyruğunu salladı. İkisi bahçede mutlu mutlu eğlenmeye devam etti.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "öbür ucundan hızla üflemeyi denedi"
   - Cümle 7: «Sonra parçanın öbür ucundan hızla üflemeyi denedi.»
   - Açıklama: İçinde fındık sıkışmış bir boruya ağızla üflemek küçük çocukta yutma ya da soluma tehlikesi taşıyan taklit edilebilir bir davranış.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "yavaş bir şarkı çaldı"
   - Cümle 10: «Maşa iki parçayı birleştirdi ve yavaş bir şarkı çaldı.»
   - Açıklama: Kartın özellikler ve kimlik alanlarında Maşa'nın flütü ya da flüt çalma yeteneği yok.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sincap şarkıya göre kuyruğunu salladı"
   - Cümle 11: «Sincap şarkıya göre kuyruğunu salladı.»
   - Açıklama: 'Şarkıya göre' bu anlamda yanlış; 'şarkıyla birlikte' ya da 'şarkıya uyup' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sincap şarkıya göre kuyruğunu"
   - Cümle 11: «Sincap şarkıya göre kuyruğunu salladı.»
   - Açıklama: 'Şarkıya göre' yanlış kullanım; 'şarkıyla birlikte' ya da 'şarkıya uyarak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0161` birebir aynı, ardından `@onarim: 2003c8f7d95f1e92db829a00a8a2784947d3786e`, sonra gövde.

### Hikâye 7: tohum masa-0162 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0162
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pencere', fiil 'takmak', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: çiçeklerin resmi için kırmızı boya yoktu | boya yerine çilek reçeliyle çiçekleri boyadı
@tohum: masa-0162
Maşa yağmurdan sonra çamurlu bahçeden eve koştu. Pencereden baktı ve bahçede yeni açmış kırmızı çiçekler gördü. Onların resmini yapmak istedi ama kırmızı boyası bitmişti. Maşa hemen mutfaktan en sevdiği çilek reçelini getirdi. Parmağını reçele batırdı ve kağıda çiçekler yaptı. Sonra boyalarıyla yeşil yapraklar çizdi. Parmağında kalan reçeli de yaladı ve güldü. Resim bahçedeki çiçeklere çok benzedi. Maşa resmi pencerenin yanındaki çiviye taktı. Artık çiçekler hem bahçede hem de evin içindeydi. Maşa resmine baktı ve mutlu mutlu el çırptı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yağmurdan sonra çamurlu bahçeden eve koştu"
   - Cümle 1: «Maşa yağmurdan sonra çamurlu bahçeden eve koştu.»
   - Açıklama: Yağmur ve çamurlu bahçe işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.
   - Açıklama: Yağmur ve çamurlu bahçe kurulup hiçbir işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "pencerenin yanındaki çiviye taktı"
   - Cümle 9: «Maşa resmi pencerenin yanındaki çiviye taktı.»
   - Açıklama: Resim çiviye takılmaz, asılır; 'çiviye astı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Artık çiçekler hem bahçede hem de evin içindeydi"
   - Cümle 10: «Artık çiçekler hem bahçede hem de evin içindeydi.»
   - Açıklama: Resimdeki çiçeklerin evin içinde olduğunu söyleyen mecazlı cümle küçük çocuk için yanıltıcı.
   - Açıklama: Evdeki çiçeklerin resim olduğu mecazla anlatılıyor, küçük çocuk için karışık.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0162` birebir aynı, ardından `@onarim: 200789308a406e19cd453d872246e1744ca9d478`, sonra gövde.

### Hikâye 8: tohum masa-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0164
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yoğurt', fiil 'yüklemek', sıfat 'çekingen'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: çekingen kirpi saklandı ve yanına gelmedi | yoğurttan sonra elma getirmeyi denedi ve arkadaş oldu
@tohum: masa-0164
Bahçede hafif bir rüzgar esiyordu. Maşa çalının altında küçük, çekingen bir kirpi gördü. Onunla arkadaş olmak istedi ama kirpi hemen yaprakların arkasına saklandı. "Merhaba, kirpi, benimle oynar mısın?" dedi Maşa. Kirpi yerinden kıpırdamadı. Maşa bir kaseye biraz yoğurt koydu ve yaprakların önüne bıraktı. Kirpi yoğurdu kokladı ama yemedi. Maşa bu kez başka bir şey denedi. Oyuncak arabasına kırmızı elmalar yükledi ve arabayı ona doğru çekti. Kirpi elmaları görünce başını çıkardı. Sonra bir elmayı ısırdı ve Maşa'nın yanına geldi. Maşa ona gülümsedi. Maşa çok sevindi, çünkü yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede hafif bir rüzgar esiyordu"
   - Cümle 1: «Bahçede hafif bir rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bitiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede, çalının altında geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, çekingen bir kirpi"
   - Cümle 2: «Maşa çalının altında küçük, çekingen bir kirpi gördü.»
   - Açıklama: 'Çekingen' soyut bir kelime ve figürün kart özelliği değil, 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Çekingen' soyut bir kelime ve 3 yaşındaki çocuk bilmez; plan satırında da geçiyor.
3. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "küçük, çekingen bir kirpi"
   - Cümle 2: «Maşa çalının altında küçük, çekingen bir kirpi gördü.»
   - Açıklama: Kartın 'yanlar' alanındaki ilişki kirpiyi dost canlısı bir orman tanıdığı olarak verir; burada Maşa'dan kaçan yabancı, çekingen bir kirpi olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0164` birebir aynı, ardından `@onarim: 61ba62ae100359712c70cf80429304b321f9f2a9`, sonra gövde.

### Hikâye 9: tohum masa-0165 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0165
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kırıntı', fiil 'göstermek', sıfat 'kokulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: küçük kokulu çiçekler elinde ezildi | reçeli bitirdi ve çiçekleri kavanoza koydu
@tohum: masa-0165
@degisim: göstermek -> koklamak
Bir sabah Maşa dağda ekmeğini reçel kavanozuna batırıp yiyordu. Birden çimlerin arasında küçük, kokulu mor çiçekler gördü. Onlardan biraz topladı ama çiçekler elinde hemen ezildi. Maşa kavanoza baktı ve dibinde biraz reçel gördü. Son reçeli de ekmeğine sürdü ve yedi. Sonra kavanozdaki ekmek kırıntılarını çimlere döktü. Yeni çiçekleri tek tek koparıp boş kavanoza koydu. Bu kez çiçekler kavanozda güzel durdu. Maşa kavanozu burnuna tuttu ve kokladı. Sonra çiçekli kavanozunu kucakladı ve çimlerde mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Bir sabah Maşa dağda"
   - Cümle 1: «Bir sabah Maşa dağda ekmeğini reçel kavanozuna batırıp yiyordu.»
   - Açıklama: Kartın dağ tarifi ve kararı yeri ormanın yanındaki tepe olarak veriyor, dağ olarak değil.
   - Açıklama: Kartın dağ tarifi ve kararı yeri ormanın yanındaki tepe olarak veriyor; hikaye dağ diyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çiçekler elinde hemen ezildi"
   - Cümle 3: «Onlardan biraz topladı ama çiçekler elinde hemen ezildi.»
   - Açıklama: Çiçeklerin neden elinde ezildiği söylenmiyor ve sorun zayıf kalıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Son reçeli de ekmeğine sürdü"
   - Cümle 5: «Son reçeli de ekmeğine sürdü ve yedi.»
   - Açıklama: Çözüm reçeli bitirme, kırıntıları dökme ve çiçekleri koyma olarak ikiden fazla adım sürüyor ve çiçekler yine elle koparılıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kavanozdaki ekmek kırıntılarını çimlere döktü"
   - Cümle 6: «Sonra kavanozdaki ekmek kırıntılarını çimlere döktü.»
   - Açıklama: Çözüm reçeli bitirme, kırıntıları dökme ve çiçekleri koyma olmak üzere ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0165` birebir aynı, `@degisim: göstermek -> koklamak` (tutuyorsan), ardından `@onarim: 76912e9473ef7d7168d3abfb44bb3a11a1e81c6d`, sonra gövde.

### Hikâye 10: tohum masa-0166 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0166
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'örgü', fiil 'susmak', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: ormanda tatlı bir koku vardı ama yeri belli değildi | reçelini kokladı, sustu ve çilekleri buldu
@tohum: masa-0166
Bir sabah Maşa ormanda çok koşmuştu ve yorgundu. Bir kütüğe oturdu ve şarkı söyledi. Birden tatlı bir koku duydu ama bu kokunun yerini bilmiyordu. Maşa şarkısını bitirdi ve sustu. Örgü çantasından en sevdiği çilek reçelini çıkarıp kokladı. İki koku aynıydı, yani yakında çilek vardı! Gözlerini kapattı ve burnunu havaya kaldırdı. Tatlı koku küçük bir patikadan geliyordu. Maşa patikada yürüdü ve yerde kıpkırmızı, küçük çilekler buldu. Çantasını çileklerle doldurdu. Bir çileği tattı ve güldü. Maşa bundan sonra ormanda bir şey ararken önce susup etrafı kokladı.
```

**Hakem bulguları (6):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çok koşmuştu ve yorgundu"
   - Cümle 1: «Bir sabah Maşa ormanda çok koşmuştu ve yorgundu.»
   - Açıklama: Yorgunluk kuruluyor ama olayda hiçbir işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu kokunun yerini bilmiyordu"
   - Cümle 3: «Birden tatlı bir koku duydu ama bu kokunun yerini bilmiyordu.»
   - Açıklama: Kokunun 'yeri' denmez; 'nereden geldiğini' bilmiyordu olmalı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bu kokunun yerini bilmiyordu"
   - Cümle 3: «Birden tatlı bir koku duydu ama bu kokunun yerini bilmiyordu.»
   - Açıklama: Bir kokunun yerini bilmemek zayıf bir sorun ve sebebi söylenmiyor.
   - Açıklama: Bir kokunun yerini bilmemek belirsiz bir sorun ve sebebi söylenmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "en sevdiği çilek reçelini çıkarıp kokladı"
   - Cümle 5: «Örgü çantasından en sevdiği çilek reçelini çıkarıp kokladı.»
   - Açıklama: Reçeli koklamak kokunun yerini bulmaya yönelmiyor; çözüm dolambaçlı ve ikiden çok adım sürüyor.
   - Açıklama: Reçeli koklamak kokunun yerini bulmaya yönelmiyor ve çözüm susma, reçel koklama, burnu kaldırma diye ikiden çok adım sürüyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir çileği tattı ve"
   - Cümle 11: «Bir çileği tattı ve güldü.»
   - Açıklama: Ormanda yerde bulunan yabani meyveyi yemek çocuğun taklit edebileceği tehlikeli bir davranıştır.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir çileği tattı ve güldü"
   - Cümle 11: «Bir çileği tattı ve güldü.»
   - Açıklama: Ormanda yerde bulunan yabani meyveyi hemen tatmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0166` birebir aynı, ardından `@onarim: 23a6efa89090d280d3e8136153eb6afb9e8c3f49`, sonra gövde.

### Hikâye 11: tohum masa-0169 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0169
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'masa', fiil 'çoğalmak', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: ağır sepetini bir kütüğe bıraktı ve bulamadı | yerdeki reçel izini takip etti ve sepeti buldu
@tohum: masa-0169
@degisim: masa -> kütük
Maşa ormanda içinde reçel kavanozu olan ağır bir sepet taşıyordu. Sepeti bir kütüğün üstüne bıraktı ve çilek toplamaya gitti. Geri dönünce sepeti bulamadı, çünkü bütün kütükler birbirine benziyordu. Maşa patikaya döndü ve yerde küçük reçel damlaları gördü. Kavanozun kapağı biraz açık kalmıştı. Maşa bu izi takip etti. Damlalar gittikçe çoğaldı. Sonunda büyük bir kütüğün üstünde sepetini buldu. Maşa kavanozun kapağını sıkıca kapattı. Sonra topladığı çilekleri de sepete koydu. Maşa ağır sepetini aldı ve neşeyle eve yürüdü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yerde küçük reçel damlaları gördü"
   - Cümle 4: «Maşa patikaya döndü ve yerde küçük reçel damlaları gördü.»
   - Açıklama: Tohumdaki özellik reçeli çok sevmek; reçel burada yalnız sızan bir iz olarak geçiyor, özellik karttaki gibi kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0169` birebir aynı, `@degisim: masa -> kütük` (tutuyorsan), ardından `@onarim: 491522b39478bfc9c693e1fda0eee503930a5541`, sonra gövde.

### Hikâye 12: tohum masa-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0170
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'mercan', fiil 'ovuşturmak', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: rüzgar yoktu ve tohumlar uçmadı | çiçeğe üfledi ve tohumlar havaya uçtu
@tohum: masa-0170
@degisim: mercan -> tohum
Tepede güneş vardı ama hiç rüzgar yoktu. Maşa çimenlerde beyaz, pamuk gibi bir çiçek buldu. Çiçeğin minik tohumlarını havada uçurmak istedi, ama tohumlar hiç kıpırdamadı. Maşa çiçeği havaya kaldırdı ve bir süre bekledi. Tohumlar yine yerinden ayrılmadı. Maşa heyecanla ellerini ovuşturdu ve yeni bir yol denedi. Derin bir nefes aldı ve çiçeğe üfledi. Minik tohumlar havalandı ve tepenin üstünde uçuştu. Maşa ellerini çırptı ve tohumların arkasından koştu. Çiçeğin sapı bomboş kalmıştı. Maşa çok sevindi, çünkü minik tohumlar sonunda uçmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve yeni bir yol denedi"
   - Cümle 6: «Maşa heyecanla ellerini ovuşturdu ve yeni bir yol denedi.»
   - Açıklama: 'Yol' burada 'yöntem' anlamında mecaz olarak kullanılmış.
   - Açıklama: 'Yeni bir yol denemek' soyut ve mecazlı bir anlatım; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0170` birebir aynı, `@degisim: mercan -> tohum` (tutuyorsan), ardından `@onarim: 9a49cac7a8fb92ab781eba70fbb59aedaff1f582`, sonra gövde.
