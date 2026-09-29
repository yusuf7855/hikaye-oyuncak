# Editör görevi (onarım): Maşa, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0047 (deneme 5 -> 6)

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
Hava çok sıcaktı. Maşa bahçede en sevdiği çilek reçelinden kuzeni Daşa için içecek hazırlamıştı. Ama şişe güneşte kaldığı için içecek ılık olmuştu. Maşa evden bir kova soğuk su getirdi. Şişeyi kovaya koydu ve kovayı ağacın gölgesine taşıdı. Maşa beklerken şişeye birkaç kez dokundu. Sonunda içecek iyice soğudu. Tam o sırada bahçe kapısından Daşa geldi. "Sürpriz, Daşa, bu içecek senin için!" dedi Maşa. Daşa bir yudum aldı ve gülümsedi. "Çok güzel olmuş, teşekkür ederim, Maşa," dedi Daşa. Sevinen Daşa çok konuşkan oldu ve Maşa'ya içeceği nasıl yaptığını sordu. Maşa ile Daşa ağacın altında oturup içeceklerini mutlu mutlu içti.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği çilek reçelinden"
   - Cümle 2: «Maşa bahçede en sevdiği çilek reçelinden kuzeni Daşa için içecek hazırlamıştı.»
   - Açıklama: Tohumdaki reçel özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sevinen Daşa çok konuşkan oldu"
   - Cümle 12: «Sevinen Daşa çok konuşkan oldu ve Maşa'ya içeceği nasıl yaptığını sordu.»
   - Açıklama: 'Konuşkan' bir kişilik özelliğidir, anlık durum için 'konuşkan oldu' yanlış kullanım.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Daşa çok konuşkan oldu"
   - Cümle 12: «Sevinen Daşa çok konuşkan oldu ve Maşa'ya içeceği nasıl yaptığını sordu.»
   - Açıklama: 'Konuşkan olmak' kalıcı bir özellik; bir anlık sevinç için yanlış anlamda kullanılmış.
4. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Sevinen Daşa çok konuşkan oldu"
   - Cümle 12: «Sevinen Daşa çok konuşkan oldu ve Maşa'ya içeceği nasıl yaptığını sordu.»
   - Açıklama: Kartın yanlar bölümünde Daşa düşünceli ve ciddi bir kız olarak tarif ediliyor.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Sevinen Daşa çok konuşkan oldu"
   - Cümle 12: «Sevinen Daşa çok konuşkan oldu ve Maşa'ya içeceği nasıl yaptığını sordu.»
   - Açıklama: Kartın yanlar bölümünde Daşa düşünceli ve ciddi bir kız; çok konuşkan olarak gösterilmesi yanlış bilgi.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sevinen Daşa çok konuşkan oldu"
   - Cümle 12: «Sevinen Daşa çok konuşkan oldu ve Maşa'ya içeceği nasıl yaptığını sordu.»
   - Açıklama: Daşa'nın konuşkanlaşıp soru sorması hiçbir sonuca bağlanmayan işlevsiz bir ayrıntı.
   - Açıklama: Daşa'nın konuşkanlığı ve sorusu hiçbir işe yaramıyor, soru cevapsız kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0047` birebir aynı, `@degisim: kereviz -> şişe` (tutuyorsan), ardından `@onarim: 43e5a6984682bfa4654099bd8e465e462386ba6d`, sonra gövde.

### Hikâye 2: tohum masa-0050 (deneme 5 -> 6)

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
@plan: resmin köşesinde yapışkan kırmızı lekeler vardı | reçeli kokusundan tanıdı ve sincabı buldu
@tohum: masa-0050
@degisim: kilitli -> yapışkan
Maşa tepede Koca Ayı'yla birlikte büyük bir tablo yapıyordu. Koca Ayı tablo için yere bir tahta dikmişti. Ama resmin köşesinde yapışkan kırmızı lekeler vardı ve resim kirlenmişti. Maşa bunu kimin yaptığını çok merak etti. Lekeleri kokladı ve kokuyu hemen tanıdı. Bu, onun en sevdiği çilek reçeliydi. Maşa sepetindeki reçel kavanozuna baktı. Kavanozun yanında minik kırmızı pati izleri vardı. İzler bir ağaca gidiyordu ve Maşa da oraya yürüdü. Ağacın arkasında patileri reçelli küçük bir sincap vardı. Koca Ayı sincabı görünce güldü. Maşa da resimdeki lekeleri bir bezle sildi. Maşa çok sevindi, çünkü lekeleri kimin yaptığını bulmuştu ve resim yine temizdi.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir tablo yapıyordu"
   - Cümle 1: «Maşa tepede Koca Ayı'yla birlikte büyük bir tablo yapıyordu.»
   - Açıklama: 'Tablo' 3 yaşındaki çocuğun bilmeyeceği bir kelime ve 'tablo yapmak' yerine 'resim yapmak' daha uygun.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Koca Ayı tablo için yere bir tahta dikmişti"
   - Cümle 2: «Koca Ayı tablo için yere bir tahta dikmişti.»
   - Açıklama: Tahta kuruluyor ama olayda hiçbir işe yaramıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bu, onun en sevdiği"
   - Cümle 6: «Bu, onun en sevdiği çilek reçeliydi.»
   - Açıklama: 'onun' zamirinin Maşa'yı mı Koca Ayı'yı mı gösterdiği belli değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kavanozun yanında minik kırmızı pati izleri vardı"
   - Cümle 8: «Kavanozun yanında minik kırmızı pati izleri vardı.»
   - Açıklama: Lekeyi temizlemek yerine koklama, kavanoza bakma, iz sürme ve sincabı bulma gibi ikiden fazla adımlı bir dedektiflik çözüme ekleniyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İzler bir ağaca gidiyordu"
   - Cümle 9: «İzler bir ağaca gidiyordu ve Maşa da oraya yürüdü.»
   - Açıklama: Çözüm koklama, kavanoza bakma, izleri bulma ve ağaca yürüme gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0050` birebir aynı, `@degisim: kilitli -> yapışkan` (tutuyorsan), ardından `@onarim: 2b2923ebf516b4eccf1fe929c8293f187dadc56d`, sonra gövde.

### Hikâye 3: tohum masa-0054 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0054
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'paspas', fiil 'boşaltmak', sıfat 'cömert'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: sebzeleri sulamak istedi ama su dolu kova çok ağırdı | suyun yarısını boşalttı ve kovayı rahatça taşıdı
@tohum: masa-0054
@degisim: paspas -> kova
Ormandaki ağaç evin bahçesinde Koca Ayı bir ağacın altında uyuyordu. Maşa, cömert dostu Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi. Ama su dolu büyük kova çok ağırdı. Maşa kovayı iki eliyle kaldırmaya çalıştı ama kaldıramadı. Maşa kovayı yana yatırdı ve suyun yarısını domateslere boşaltmayı denedi. Kova hafifledi ve Maşa onu rahatça taşıdı. Kalan suyu da havuçlara döktü. Sonra Koca Ayı uyandı ve ıslak bahçeyi gördü. Şaşırdı ve kocaman gülümsedi. Maşa'ya koştu ve ona sıkıca sarıldı. "Sürpriz, Koca Ayı! Bugün bahçeni ben suladım!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "cömert dostu Koca Ayı'ya sürpriz"
   - Cümle 2: «Maşa, cömert dostu Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi.»
   - Açıklama: 'Cömert' soyut bir sıfat ve burada figürün kendi özelliği olarak değil Koca Ayı için kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0054` birebir aynı, `@degisim: paspas -> kova` (tutuyorsan), ardından `@onarim: 66a6d7c68876610aa352bd19916780401082749e`, sonra gövde.

### Hikâye 4: tohum masa-0056 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0056
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yağ', fiil 'sakinleşmek', sıfat 'sabırsız'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: yaprakların arasından gelen sesi merak etti | sakinleşti ve yere elma koyunca kirpiyi gördü
@tohum: masa-0056
@degisim: yağ -> elma
Maşa ormanda elinde bir elmayla yürüyordu. Birden yaprakların arasından hışır hışır bir ses geldi. Maşa bu sesi çok merak etti. Maşa çok sabırsızdı ve hemen sesin geldiği yere koştu. Ama ses kesildi ve hiçbir şey kıpırdamadı. Maşa biraz bekledi ve sakinleşti. Sonra yeni bir şey denedi ve elmasını yere koydu. Yavaşça geri çekildi ve sessizce oturdu. Az sonra yaprakların arasından küçük bir burun çıktı. Ardından dikenli bir kirpi göründü. Kirpi elmayı hemen kokladı ve mutlu mutlu yemeye başladı. Maşa çok sevindi, çünkü sesi yapan kirpiyi sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa çok sabırsızdı"
   - Cümle 4: «Maşa çok sabırsızdı ve hemen sesin geldiği yere koştu.»
   - Açıklama: Tohumdaki özellik denemek; kartın özellikler alanında olmayan sabırsızlık ek özellik olarak ekleniyor.
   - Açıklama: Kartın özellikler alanında olmayan sabırsızlık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0056` birebir aynı, `@degisim: yağ -> elma` (tutuyorsan), ardından `@onarim: f9d14970f461fa27e54795bc50aa27bb7ae82d3f`, sonra gövde.

### Hikâye 5: tohum masa-0057 (deneme 4 -> 5)

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
Maşa tepede Koca Ayı ve sincapla bir arama oyunu oynuyordu. Koca Ayı, Maşa'nın özel reçel kavanozunu bir taşın arkasına sakladı. Ama sincap şaka yapmak için kavanozun üstüne yosun koydu. Maşa taşların arkasına baktı ama kavanozu göremedi. Sonra sincabın ağzında biraz yosun gördü. Sincap yosunu büyük bir taşın yanına götürdü ve bıraktı. Orada kabarık bir yosun yığını vardı. Maşa hemen o taşa koştu ve yosunları kaldırdı. Reçel kavanozu tam oradaydı! "Buldum, sincap, sen çok komiksin!" dedi Maşa. Koca Ayı güldü ve ellerini çırptı. Sincap da kuyruğunu salladı. Maşa çok sevindi, çünkü sevdiği reçeli oyunun sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sincap yosunu büyük bir taşın yanına götürdü ve bıraktı"
   - Cümle 6: «Sincap yosunu büyük bir taşın yanına götürdü ve bıraktı.»
   - Açıklama: Kavanozun yerini şakayı yapan sincap yosunu oraya taşıyarak gösteriyor, Maşa yalnız onu izliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0057` birebir aynı, `@degisim: içmek -> saklamak` (tutuyorsan), ardından `@onarim: 0f01a87dd0887bb50dde6502c77d1dff2f12f425`, sonra gövde.

### Hikâye 6: tohum masa-0058 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0058
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'basamak', fiil 'şişirmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: parmakları reçelden kaygandı ve balonun ucunu tutamadı | parmaklarını yaladı ve balonu sıkıca bağladı
@tohum: masa-0058
@degisim: düzenli -> sıkı
Güneş parlıyordu. Maşa tepede reçelli ekmeğini bitirdi ve kırmızı bir balon şişirdi. Ama parmakları reçelden kaygan olmuştu. Maşa balonun ucunu tutamadı ve balon elinden kaçtı. Balon komik bir sesle sağa sola uçtu. Sonra söndü ve taş bir basamağın üstüne düştü. Maşa balonuna baktı ve üzüldü. Maşa reçeli çok severdi ve parmaklarını tek tek yaladı. Artık parmakları temizdi. Balonu yeniden şişirdi ve ucuna sıkı bir düğüm attı. Bu kez balon hiç kaçmadı. Maşa balonu havaya attı ve yakaladı. Maşa balonuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Maşa balonun ucunu tutamadı ve balon elinden kaçtı.»
   - Açıklama: İlk 3 cümlede yalnız parmakların kayganlığı var; balonu tutamama sorunu ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0058` birebir aynı, `@degisim: düzenli -> sıkı` (tutuyorsan), ardından `@onarim: d8cca86269e837f5a9359f944ae19b5750956031`, sonra gövde.

### Hikâye 7: tohum masa-0062 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0062
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'külah', fiil 'çırpmak', sıfat 'yamuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: tanımadığı sincap utandı ve yaprakların arasına saklandı | yapraktan külah yapıp içine fındık koydu
@tohum: masa-0062
Maşa ormanda reçel yiyerek yürüyordu. Bir ağacın dalında daha önce görmediği bir sincap gördü. Sincap onu görünce utandı ve yaprakların arasına saklandı. "Merhaba, sincap, benimle arkadaş olur musun?" diye sordu Maşa. Ama sincap saklandığı yerden çıkmadı. Maşa etrafına baktı ve yerde fındıklar gördü. Hepsini taşımak için büyük bir yaprağı kıvırdı. Yaprağın iki ucunu biraz reçelle birbirine yapıştırdı. Yamuk bir külah olmuştu. Maşa külahı fındıkla doldurup ağacın dibine koydu. Sincap hemen aşağı indi ve bir fındık aldı. Sonra Maşa'nın yanına geldi ve kuyruğunu salladı. Maşa sevinçle ellerini yavaşça çırptı. Maşa çok mutluydu, çünkü yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "biraz reçelle birbirine yapıştırdı"
   - Cümle 8: «Yaprağın iki ucunu biraz reçelle birbirine yapıştırdı.»
   - Açıklama: Tohumdaki özellik reçeli sevmek; reçel yapıştırıcı olarak kullanılıyor ve özellik karttaki gibi işlemiyor.
   - Açıklama: Kart özelliği reçeli sevmek; reçel iki kez geçiyor ve yapıştırıcı olarak kullanılıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yaprağın iki ucunu biraz reçelle birbirine yapıştırdı"
   - Cümle 8: «Yaprağın iki ucunu biraz reçelle birbirine yapıştırdı.»
   - Açıklama: Çözüm fındık toplama, yaprak kıvırma, reçelle yapıştırma ve doldurma gibi ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0062` birebir aynı, ardından `@onarim: 566066f4cebd2d2a877ea3a1e8dba10c1c920844`, sonra gövde.

### Hikâye 8: tohum masa-0064 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0064
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'mendil', fiil 'aydınlanmak', sıfat 'kuru'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi uzun otların arasından kelebekleri göremedi | taşa reçelli ekmek koydu ve kirpi taşa çıktı
@tohum: masa-0064
Yağmur dindi ve orman birden aydınlandı. Maşa ile Koca Ayı reçelli ekmek yerken renkli kelebekler gördü. Ama küçük kirpi uzun otların arasından onları göremedi. "Kirpi, sen de görmelisin!" dedi Maşa. Otların yanında büyük ve düz bir taş vardı. Taş yağmurdan ıslaktı ve Maşa onu kuru mendiliyle sildi. Maşa reçeli çok severdi ama ekmeğini ikiye böldü ve yarısını taşa koydu. Kirpi reçelli ekmeğe doğru yürüdü ve taşın üstüne çıktı. Kirpi oradan kelebekleri görünce sevinçle burnunu oynattı. Maşa, Koca Ayı ve kirpi yan yana oturup kelebekleri mutlu mutlu seyretti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa onu kuru mendiliyle sildi"
   - Cümle 6: «Taş yağmurdan ıslaktı ve Maşa onu kuru mendiliyle sildi.»
   - Açıklama: Taşın ıslak olması ve mendille silinmesi çözüme hiçbir katkı yapmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0064` birebir aynı, ardından `@onarim: cb54a60e157d5bcd44d24fa5aa352fe8035c3d5b`, sonra gövde.

### Hikâye 9: tohum masa-0066 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0066
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'altın', fiil 'yavaşlamak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: en sevdiği plastik yüzük uzun otlara düştü | yavaşladı ve parlayan yüzüğü otların arasında buldu
@tohum: masa-0066
Maşa tepede koşarak oynuyordu. Birden parmağındaki altın renkli plastik yüzük otlara düştü. Bu, Maşa'nın en sevdiği oyuncaktı. Maşa hemen yavaşladı ve otlara baktı. Ama otlar uzundu ve hiçbir şey görünmüyordu. Maşa yere eğildi ve otların dibine yakından baktı. Orada küçük bir şey parladı. Maşa bu parlak şeyi çok merak etti. Otları iki eliyle dikkatle açmayı denedi. Parlayan şey onun yüzüğüydü! Maşa yüzüğü parmağına taktı ve sevinçle güldü. Maşa bundan sonra koşmadan önce yüzüğünü hep cebine koydu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bu parlak şeyi çok merak etti"
   - Cümle 8: «Maşa bu parlak şeyi çok merak etti.»
   - Açıklama: Tohumdaki özellik enerji ve deneme; merak ikinci bir özellik olarak ekleniyor ve deneme yalnız sıradan bir fiil olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0066` birebir aynı, ardından `@onarim: 44cc32a2b49c92772417a98e44f08be9dbd4ee63`, sonra gövde.

### Hikâye 10: tohum masa-0074 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap
@tohum: masa-0074
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'top', fiil 'incelemek', sıfat 'rahat'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap
@plan: sert vurduğu top sincabın fındıklarını dağıttı | özür diledi ve fındıkları toplayıp geri verdi
@tohum: masa-0074
Tepede kuşlar neşeyle ötüyordu. Maşa topuyla oynarken yeni ve çok sert bir vuruş denedi. Top uçtu ve sincabın topladığı fındıkları dağıttı. Sincap kuyruğunu kabarttı ve kızgın kızgın baktı. Maşa koşup geldi ve dağılan fındıkları dikkatle inceledi. Hiçbiri kırılmamıştı. "Özür dilerim, sincap, hepsini hemen toplarım," dedi Maşa. Maşa fındıkları tek tek topladı ve sincabın önüne koydu. Sincap bir fındığı ağzına aldı ve rahat rahat yemeye başladı. Maşa topu bu kez sincaptan uzağa yavaşça yuvarladı. Maşa çok sevindi, çünkü sincap artık ona kızgın değildi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "fındıkları toplayıp geri verdi"
   - Cümle 0 (plan satırı): «sert vurduğu top sincabın fındıklarını dağıttı | özür diledi ve fındıkları toplayıp geri verdi»
   - Açıklama: Gövdede fındıklar toplanıp sincaba geri verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0074` birebir aynı, ardından `@onarim: f218d39213afaf7d5fee8e586fd8f83fb189d9fa`, sonra gövde.

### Hikâye 11: tohum masa-0076 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0076
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'poğaça', fiil 'güldürmek', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: kar tanesi burnuna düşünce hemen eridi | soğuk montunun kolunda kar tanesine baktı
@tohum: masa-0076
Maşa evinin önündeki bahçede sıcak bir poğaça yiyordu ve kar yağıyordu. Bir kar tanesi Maşa'nın burnuna düştü ve onu güldürdü. Maşa bu taneye yakından bakmak istedi. Ama burnu sıcaktı ve tane hemen eridi. Maşa poğaçayı bitirdi ve montunun kolunu havaya kaldırmayı denedi. Mont soğuktu ve kolun üstüne ufak bir kar tanesi kondu. Bu tane erimedi. Maşa ona dikkatle baktı. Kar tanesi minik bir yıldıza benziyordu. Maşa sevinçle zıpladı ve bir tane daha yakaladı. Maşa bundan sonra kar tanelerine hep montunun kolunda baktı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kolunu havaya kaldırmayı denedi"
   - Cümle 5: «Maşa poğaçayı bitirdi ve montunun kolunu havaya kaldırmayı denedi.»
   - Açıklama: Kolu kaldırmak denenecek bir iş değil; 'denedi' yanlış anlamda, 'kaldırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0076` birebir aynı, ardından `@onarim: 2923bda8b957500dc847a8ecaf55bd8ab8f7d0dc`, sonra gövde.
