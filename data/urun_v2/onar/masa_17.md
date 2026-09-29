# Editör görevi (onarım): Maşa, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0016 (deneme 4 -> 5)

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
Serin bir rüzgar esiyordu. Uçan yapraklar reçeline düşünce Maşa kirpiyle ormanda çadır kurdu. Ama örtü hep yere kayıyordu, çünkü çadırın direği çok ince bir daldı. Maşa ince dalı yere bıraktı ve etrafa baktı. Çalıların yanında kalın ve düz bir dal buldu. Maşa dalı toprağa sıkıca yerleştirdi ve örtüyü üstüne serdi. Bu kez örtü hiç kaymadı. Güzel bir çadır olmuştu. Kirpi hemen çadırın içine girdi. Maşa da onun yanına oturdu. "Bak, kirpi, çadırımız hazır!" dedi Maşa.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Uçan yapraklar reçeline düşünce"
   - Cümle 2: «Uçan yapraklar reçeline düşünce Maşa kirpiyle ormanda çadır kurdu.»
   - Açıklama: 'Reçeline' iyelik eki Maşa henüz anılmadan kullanılıyor, kimin reçeli olduğu belli değil.
   - Açıklama: Daha önce geçmeyen reçelin kime ait olduğu belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Uçan yapraklar reçeline düşünce"
   - Cümle 2: «Uçan yapraklar reçeline düşünce Maşa kirpiyle ormanda çadır kurdu.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yarar biçimde kullanılmıyor, yalnız anılıyor.
   - Açıklama: Tohumdaki reçel özelliği yalnız geçiyor, sorunun çözümünde işe yaramıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Uçan yapraklar reçeline düşünce"
   - Cümle 2: «Uçan yapraklar reçeline düşünce Maşa kirpiyle ormanda çadır kurdu.»
   - Açıklama: Reçele yaprak düşmesi ve kayan örtü olmak üzere iki ayrı sorun açılıyor.
   - Açıklama: Reçele yaprak düşmesi ile örtünün kayması iki ayrı sorun olarak açılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Uçan yapraklar reçeline düşünce"
   - Cümle 2: «Uçan yapraklar reçeline düşünce Maşa kirpiyle ormanda çadır kurdu.»
   - Açıklama: Reçele düşen yapraklar çadırın sebebi gibi kuruluyor ama bir daha hiç kullanılmıyor.
   - Açıklama: Reçele düşen yapraklar çadırın sebebi olarak kuruluyor ama reçel bir daha hiç anılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0016` birebir aynı, ardından `@onarim: 80ef1d8485527eb8e8e9bea44686472d31dee4df`, sonra gövde.

### Hikâye 2: tohum masa-0018 (deneme 5 -> 6)

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
Tepede güçlü bir rüzgar esiyordu. Maşa süslü uçurtmasını ve reçel kavanozunu tepeye getirmişti. Ama uçurtma her seferinde dönüp yere düştü, çünkü kuyruğu çok kısaydı. Maşa hiç sıkılmadı ve uçurtmaya dikkatle baktı. Sonra kavanozun uzun, kırmızı kurdelesini gördü. Maşa kurdeleyi çözdü ve uçurtmanın kuyruğuna bağladı. Uçurtma bu kez dönmedi ve yavaş yavaş yükseldi. Maşa uçurtmanın ipini iki eliyle tuttu ve sevinçle güldü. Kırmızı kuyruk rüzgarda sallandı. Maşa uçurtmasını tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "reçel kavanozunu tepeye getirmişti"
   - Cümle 2: «Maşa süslü uçurtmasını ve reçel kavanozunu tepeye getirmişti.»
   - Açıklama: Tohumdaki reçel sevgisi işe yaramıyor; yalnız kavanozun kurdelesi kullanılıyor, reçeli sevme özelliği hikayede rol almıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "reçel kavanozunu tepeye getirmişti"
   - Cümle 2: «Maşa süslü uçurtmasını ve reçel kavanozunu tepeye getirmişti.»
   - Açıklama: Uçurtma uçurmaya reçel kavanozu getirmesinin sebebi yok; kavanoz yalnız çözümdeki kurdeleyi hazır etmek için beliriyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kavanozun uzun, kırmızı kurdelesini gördü"
   - Cümle 5: «Sonra kavanozun uzun, kırmızı kurdelesini gördü.»
   - Açıklama: Tohumdaki özellik reçeli sevmek; hikayede yalnız kavanozun kurdelesi kullanılıyor, reçel sevgisi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0018` birebir aynı, `@degisim: lamba -> uçurtma` (tutuyorsan), ardından `@onarim: dab8890cdb966a90c34d555be37112fca75ae99b`, sonra gövde.

### Hikâye 3: tohum masa-0024 (deneme 5 -> 6)

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
Bir kış sabahı Maşa, Koca Ayı ve kirpi tepedeydi. Maşa ile Koca Ayı kızak yarışı yapacaktı. Ama ağacın yanındaki kırmızı kızak yağan karın altında kalmıştı. Maşa önce ağacın önündeki karı kazmayı denedi. Orada yalnız bir taş vardı. Sonra ağacın arkasına koştu ve orayı da kazdı. Bu kez karda bir ip ucu gördü. Maşa ipi çekti ve kızak karın içinden çıktı. Kirpi sevinçle etrafta koştu. "Hadi, Koca Ayı, yarışalım!" dedi Maşa. Maşa ile Koca Ayı kızaklarıyla tepenin alçak ve güvenli yerinden kaydı. Yarışı Maşa kazandı. Sonra üçü tepede mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa ile Koca Ayı kızaklarıyla"
   - Cümle 11: «Maşa ile Koca Ayı kızaklarıyla tepenin alçak ve güvenli yerinden kaydı.»
   - Açıklama: Yalnız bir kızak kurulmuşken Koca Ayı'nın kızağı sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0024` birebir aynı, ardından `@onarim: 400a62f73b1d43b097ed7fb647b6d46accae6d40`, sonra gövde.

### Hikâye 4: tohum masa-0026 (deneme 5 -> 6)

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
Ormanda patikanın kenarında yapraklı bitkiler vardı. Maşa yaprakların altında kırmızı çilekler gördü. Onlardan reçel yapmak istedi, ama çilekleri koyacak sepeti yoktu. Maşa önce çilekleri avuçlarına doldurdu. Ama ellerine yalnız birkaç çilek sığdı. Maşa başörtüsünün sağlam olduğuna inandı. Başörtüsünü çıkardı ve yere serdi. Çilekleri tek tek onun üstüne koydu. Başörtüsünü sıkıca bağladı ve küçük bir çanta yaptı. Çanta çileklerle doldu. Maşa dolu çantaya baktı ve güldü. Sonra çantayı sırtına aldı ve reçel için çileklerini mutlu mutlu taşıdı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "başörtüsünün sağlam olduğuna inandı"
   - Cümle 6: «Maşa başörtüsünün sağlam olduğuna inandı.»
   - Açıklama: 'İnandı' fiili bu bağlamda yanlış ve soyut; 'başörtüsünün sağlam olduğunu gördü' gibi somut olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başörtüsünün sağlam olduğuna inandı"
   - Cümle 6: «Maşa başörtüsünün sağlam olduğuna inandı.»
   - Açıklama: 'Sağlam olduğuna inandı' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0026` birebir aynı, `@degisim: pelerin -> başörtüsü` (tutuyorsan), ardından `@onarim: dad81d5e78fc9ae2dda7454a0fb2f60de77249db`, sonra gövde.

### Hikâye 5: tohum masa-0030 (deneme 5 -> 6)

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
Maşa tepede koşarken pembe oyuncak gözlüğünü düşürmüştü. Şimdi uzun çimenlerde onu arıyordu. Birden çimenlerin arasında bir şey parladı. Maşa hemen oraya koştu ama çimenler çok sıktı ve hiçbir şey göremedi. Maşa ilk durduğu yere döndü ve oradan bakmayı denedi. Işık yine parladı. Maşa bu kez ışığa bakarak yavaş yavaş yürüdü. Çimenlerin arasında Maşa'nın pembe gözlüğü vardı. Gözlüğün camları güneşte parlıyordu. Maşa onu eline aldı. Hiçbir parçası eksik değildi. Maşa çok sevindi, çünkü gözlüğünü sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa ilk durduğu yere döndü"
   - Cümle 5: «Maşa ilk durduğu yere döndü ve oradan bakmayı denedi.»
   - Açıklama: İlk durduğu yer daha önce kurulmuyor ve oraya dönmenin neden işe yarayacağı söylenmediği için çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0030` birebir aynı, `@degisim: köpürmek -> parlamak` (tutuyorsan), ardından `@onarim: 4ef6066118dd631614fcf5535da31ba6d4c65185`, sonra gövde.

### Hikâye 6: tohum masa-0037 (deneme 4 -> 5)

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
Maşa ormanda piknik yapıyor ve küçük sarı topuyla oynuyordu. Topu havaya atıyor ve yakalıyordu. Ama top bir ağaca çarptı ve iki taşın arasına düştü. Taşların arası çok dardı ve Maşa'nın eli oraya sığmadı. Maşa sepetteki en sevdiği tatlı reçele baktı. Sarı top çok hafifti, reçel de yapışkandı. Maşa reçelin topu tutacağına güvendi. Uzun bir dalın ucuna biraz reçel sürdü. Dalı taşların arasına uzattı ve top reçele yapıştı. Maşa dalı yavaşça çekti ve top dışarı çıktı. Top yapış yapış olmuştu. Maşa güldü ve onu otlara silip temizledi. Maşa bundan sonra topuyla ağaçlardan uzakta, açık bir yerde oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa reçelin topu tutacağına güvendi"
   - Cümle 7: «Maşa reçelin topu tutacağına güvendi.»
   - Açıklama: 'Güvenmek' burada soyut bir kavram ve cümle küçük çocuğa ağır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "reçelin topu tutacağına güvendi"
   - Cümle 7: «Maşa reçelin topu tutacağına güvendi.»
   - Açıklama: 'Tutacağına güvendi' soyut bir inanç ifadesi; 3 yaşındaki çocuk için ağır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0037` birebir aynı, `@degisim: fıskiye -> top` (tutuyorsan), ardından `@onarim: 64d4635934d583b4d97186bc560f91c9a91a0257`, sonra gövde.

### Hikâye 7: tohum masa-0039 (deneme 4 -> 5)

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
@plan: çamurdan pasta yaparken elleri çok kirlendi | kovadaki yağmur suyuyla ellerini yıkadı
@tohum: masa-0039
@degisim: koni -> kova
Maşa bulutlu bir günde ormanda çamurdan pasta yapıyordu. Pasta yapmak için yanındaki kovada yağmur suyu biriktirmişti. Birden karnı acıktı ama elleri çok kirliydi. Sepetindeki reçelli ekmeği hemen yemek istedi. Maşa reçeli çok sevdiği için hiç beklemedi. Kovadaki su serin ve temizdi. Maşa bu suyla ellerini iyice yıkadı. Sonra ellerini salladı ve kuruttu. Büyük bir ağacın altına oturdu. Ekmeğini sepetten aldı ve afiyetle yedi. Maşa çok mutluydu, çünkü elleri temizdi ve karnı doymuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok sevdiği için hiç beklemedi"
   - Cümle 5: «Maşa reçeli çok sevdiği için hiç beklemedi.»
   - Açıklama: Kartın reçel sevgisi özelliği yalnız söylenip geçiyor, sorunu (kirli eller) çözmede işe yaramıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çok sevdiği için hiç beklemedi"
   - Cümle 5: «Maşa reçeli çok sevdiği için hiç beklemedi.»
   - Açıklama: Maşa'nın hiç beklemediği söyleniyor ama hemen ardından ellerini yıkayıp kurutuyor ve ağacın altına oturuyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "reçeli çok sevdiği için hiç beklemedi"
   - Cümle 5: «Maşa reçeli çok sevdiği için hiç beklemedi.»
   - Açıklama: Maşa hiç beklemedi deniyor ama hemen ardından ellerini yıkayıp kurutarak bekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0039` birebir aynı, `@degisim: koni -> kova` (tutuyorsan), ardından `@onarim: 62158bc2f5cc9d73600ed2dd395e435c09d41aff`, sonra gövde.

### Hikâye 8: tohum masa-0040 (deneme 4 -> 5)

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
Rüzgar tepede hafif hafif esiyordu. Şehirden gelen Daşa, kolye yapmak için çimenlerde Maşa'yı bekliyordu. Maşa kuzenini çok özlemişti. Ona kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü. Renkli boncuklar çimenlerin arasına döküldü. Daşa çok üzüldü. "Özür dilerim, Daşa, hepsini hemen toplayacağım," dedi Maşa. Maşa çimenlere eğildi ve boncukları tek tek toplamayı denedi. Daşa da kutuyu açık tuttu. Sonunda bütün boncuklar kutudaydı. Daşa kutuya baktı ve gülümsedi. "Teşekkürler, Maşa, hadi kolyeyi birlikte yapalım," dedi Daşa. Maşa çok sevindi, çünkü kuzeni yine gülüyordu.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Maşa kuzenini çok özlemişti.»
   - Açıklama: Kutunun düşüp boncukların dökülmesi ancak 4. ve 5. cümlede söyleniyor; ilk 3 cümlede sorun yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ona kavuşmak için"
   - Cümle 4: «Ona kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: 'Kavuşmak' soyut ve edebi bir kelime; 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ona kavuşmak için boncuk"
   - Cümle 4: «Ona kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki bir çocuğun bilmeyeceği edebi bir kelime.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ama kutu elinden düştü"
   - Cümle 4: «Ona kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0040` birebir aynı, `@degisim: uyanık -> renkli` (tutuyorsan), ardından `@onarim: 890ca24a945367141d2e91512a24fc822fa87c12`, sonra gövde.

### Hikâye 9: tohum masa-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Daşa
@tohum: masa-0047
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kereviz', fiil 'soğumak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Daşa
@plan: içecek güneşte kaldığı için ılık olmuştu | şişeyi soğuk sulu kovaya koyup gölgede bekledi
@tohum: masa-0047
@degisim: kereviz -> şişe
Hava çok sıcaktı. Maşa, kuzeni Daşa için bahçede en sevdiği çilek reçelinden bir içecek hazırlamıştı. Ama şişe güneşte kaldığı için içecek ılık olmuştu. Maşa evden bir kova soğuk su getirdi. Şişeyi kovaya koydu ve kovayı ağacın gölgesine taşıdı. Maşa beklerken şişeye birkaç kez dokundu. Sonunda içecek iyice soğudu. Tam o sırada bahçe kapısından Daşa geldi. "Sürpriz, Daşa, bu içecek senin için!" dedi Maşa. Daşa bir yudum aldı ve gülümsedi. "Çok güzel olmuş, teşekkür ederim, Maşa," dedi Daşa. Konuşkan Maşa, içeceği kovada nasıl soğuttuğunu anlattı. Maşa ile Daşa ağacın altında oturup içeceklerini mutlu mutlu içti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "için bahçede en sevdiği çilek"
   - Cümle 2: «Maşa, kuzeni Daşa için bahçede en sevdiği çilek reçelinden bir içecek hazırlamıştı.»
   - Açıklama: 'En sevdiği' Maşa'yı mı Daşa'yı mı gösteriyor belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Konuşkan Maşa, içeceği kovada"
   - Cümle 12: «Konuşkan Maşa, içeceği kovada nasıl soğuttuğunu anlattı.»
   - Açıklama: Tohumdaki özellik reçel; kartın özellikler alanında olmayan konuşkanlık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0047` birebir aynı, `@degisim: kereviz -> şişe` (tutuyorsan), ardından `@onarim: 2a812661cee9754a61963b755a7afb069744faed`, sonra gövde.

### Hikâye 10: tohum masa-0050 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0050
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tablo', fiil 'dikmek', sıfat 'kilitli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: resmin köşesinde yapışkan kırmızı izler vardı | kokudan reçeli tanıdı ve izleri takip edip sincabı buldu
@tohum: masa-0050
@degisim: kilitli -> yapışkan
Maşa tepede reçel kavanozunu yanına koymuş, Koca Ayı'yı izliyordu. Koca Ayı bir tahtayı yere dikmiş, üstüne resimli bir tablo asmıştı. Birden Maşa resmin köşesinde küçük kırmızı izler gördü. Bunlar yapışkandı ve çok güzel kokuyordu. Maşa kokuyu hemen tanıdı, bu onun en sevdiği reçeldi! Maşa reçel kavanozuna baktı, kapak açıktı. Kavanozun yanında minik ayak izleri vardı. Maşa onların peşinden gitti ve ağacın arkasında bir sincap buldu. Sincabın patileri kırmızı reçelle kaplıydı. Koca Ayı sincabı görünce gülümsedi. Maşa da resmin köşesini hemen temizledi. Maşa çok sevindi, çünkü izlerin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üstüne resimli bir tablo asmıştı"
   - Cümle 2: «Koca Ayı bir tahtayı yere dikmiş, üstüne resimli bir tablo asmıştı.»
   - Açıklama: Tablo zaten resimdir; 'resimli bir tablo' anlamca yanlış ve gereksiz.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "üstüne resimli bir tablo"
   - Cümle 2: «Koca Ayı bir tahtayı yere dikmiş, üstüne resimli bir tablo asmıştı.»
   - Açıklama: Tablo zaten resimdir; 'resimli tablo' gereksiz tekrar.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa onların peşinden gitti"
   - Cümle 8: «Maşa onların peşinden gitti ve ağacın arkasında bir sincap buldu.»
   - Açıklama: Kokuyu tanıma, kavanoza bakma, izleri takip etme, sincabı bulma ve temizleme ile çözüm ikiden çok adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0050` birebir aynı, `@degisim: kilitli -> yapışkan` (tutuyorsan), ardından `@onarim: 7a2993c53acde393561ad7e8ee1ec02bed686600`, sonra gövde.

### Hikâye 11: tohum masa-0052 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0052
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sırayla oynamak
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'gölge', fiil 'süslenmek', sıfat 'limonlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: tek kaşık vardı ve ikisi de onu hemen istedi | sırayla sürmeyi önerdi ve keki birlikte süslediler
@tohum: masa-0052
Rüzgar ağaçların arasında hafif hafif esiyordu. Maşa ile sincap ağacın gölgesinde limonlu bir kekin üstüne reçel sürecekti. Ama tek bir kaşık vardı ve ikisi de onu hemen istedi. İkisi de kaşığı kendine çekti ve kek boş kaldı. Sincap üzgün üzgün keke baktı. Maşa reçeli çok severdi ama kaşığı sincaba uzattı. "Sırayla sürelim, sincap, önce sen," dedi Maşa. Sincap kekin bir yanına biraz reçel sürdü. Sonra kaşığı Maşa'ya geri verdi. Maşa da kekin öbür yanına sürdü. Böylece limonlu kek baştan sona süslendi. Maşa ile sincap çok sevindi, çünkü kekleri çok güzel olmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve kek boş kaldı"
   - Cümle 4: «İkisi de kaşığı kendine çekti ve kek boş kaldı.»
   - Açıklama: Kek boş kalmaz; 'reçelsiz kaldı' kastediliyor, kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0052` birebir aynı, ardından `@onarim: e2da7306b0abedb6d4eb71abb50e04875e125318`, sonra gövde.

### Hikâye 12: tohum masa-0053 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0053
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: bir şey yapmak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kaktüs', fiil 'ovmak', sıfat 'sağlam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: yan yatan kavanoz yuvarlandı ve fındıklar döküldü | kavanozu iki taşın arasına dik koydu
@tohum: masa-0053
@degisim: kaktüs -> kavanoz
Bir sabah Maşa ile kuzeni Daşa ormanda sincaba bir fındık kabı yapıyordu. Maşa kavanozdaki son reçeli yedi ve Daşa içini yaprakla ovdu. Ama kavanoz yan yatıyordu, bu yüzden içine fındık koyunca yuvarlandı. Fındıklar yere döküldü. "Maşa, bu kavanoz hiç yerinde durmuyor," dedi Daşa. Maşa etrafına baktı ve iki büyük taş buldu. Kavanozu iki taşın arasına dik koydu. Kavanoz artık hiç kıpırdamadı. Daşa fındıkları topladı ve kavanoza geri koydu. Sincap hemen geldi ve kavanozdan bir fındık aldı. "Bak, Daşa, sincap bu kabı çok sevdi!" dedi Maşa. Maşa ile Daşa çok sevindi, çünkü sincabın artık sağlam bir kabı vardı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa kavanozdaki son reçeli yedi"
   - Cümle 2: «Maşa kavanozdaki son reçeli yedi ve Daşa içini yaprakla ovdu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama kavanoz yan yatıyordu"
   - Cümle 3: «Ama kavanoz yan yatıyordu, bu yüzden içine fındık koyunca yuvarlandı.»
   - Açıklama: Kavanozun neden yan yattığı ve dik durması için neden taş gerektiği söylenmiyor; sebep akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0053` birebir aynı, `@degisim: kaktüs -> kavanoz` (tutuyorsan), ardından `@onarim: 3826a114b71c25bdeed94f921bfcbeddfac58281`, sonra gövde.
