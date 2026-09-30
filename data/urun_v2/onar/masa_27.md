# Editör görevi (onarım): Maşa, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0092 (deneme 1 -> 2)

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
Rüzgar hafif hafif esiyordu. Maşa ile Koca Ayı, sincabın ağacının dibine fındık dolu bir bot koydu. Bu bir sürprizdi ama sincap yuvasındaydı ve onları duymuyordu. Maşa önce ellerini çırptı ama sincap dışarı çıkmadı. Sonra yerden incecik bir dal aldı. Dalla botun altına tak tak vurmayı denedi. Bot yüksek ve komik bir ses çıkardı. Sincap sesi duydu ve ağaçtan hızla indi. Botun içindeki fındıkları görünce kuyruğunu salladı. Sonra fındıkları birer birer yuvasına taşıdı. Koca Ayı sevinçle Maşa'ya sarıldı. Maşa bundan sonra sincabı çağırmak için hep botun altına vurdu.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "sincabı çağırmak için hep botun altına vurdu"
   - Cümle 12: «Maşa bundan sonra sincabı çağırmak için hep botun altına vurdu.»
   - Açıklama: Son cümle olaydan çıkan sıcak bir kapanış değil, çıplak bir alışkanlık eylemiyle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0092` birebir aynı, ardından `@onarim: af7ff0e2fdd29ffed3af5d11d23750d193a4becd`, sonra gövde.

### Hikâye 2: tohum masa-0093 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0093
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kutu', fiil 'üflemek', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: beyaz çiçeğe üfledi ama az tohum uçtu | çiçekleri kutuya koyup kutunun içine üfledi
@tohum: masa-0093
Maşa tepede yeni kutusuna çiçek topluyordu. Birden otların arasında beyaz, top gibi çiçekler fark etti. Bir tanesine üfledi ama yalnız birkaç küçük tohum uçtu. Maşa tohumların kar gibi uçmasını istedi. Önce daha güçlü üfledi, yine az tohum uçtu. Sonra beyaz çiçekleri tek tek toplayıp kutusuna koymayı denedi. Kutuyu yüzüne yaklaştırdı ve içine kuvvetle üfledi. Bir anda kutudan havaya bir sürü tohum uçtu. Tohumlar tepenin üstünde kar taneleri gibi dönüyordu. Maşa tohumların arasında mutlu mutlu koşup zıpladı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bir tanesine üfledi ama yalnız birkaç küçük tohum uçtu"
   - Cümle 3: «Bir tanesine üfledi ama yalnız birkaç küçük tohum uçtu.»
   - Açıklama: Az tohum uçmasının sebebi hikayede söylenmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yalnız birkaç küçük tohum uçtu"
   - Cümle 3: «Bir tanesine üfledi ama yalnız birkaç küçük tohum uçtu.»
   - Açıklama: Neden az tohum uçtuğu hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0093` birebir aynı, ardından `@onarim: 56ed40a57678faa6d4a68f167828b7638fbf5841`, sonra gövde.

### Hikâye 3: tohum masa-0094 (deneme 1 -> 2)

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
@plan: üçü de aynı anda topa uzandı ve oyun durdu | önce kuzenine sırayı verip beklerken reçel yedi
@tohum: masa-0094
Tepede Maşa, Daşa ve kirpi, eğri bir kökün üstünden top yuvarlıyordu. Top kökten kayıp çimenlere iniyordu ve herkes buna gülüyordu. Ama üçü de aynı anda topa uzandı ve oyun durdu. "Hepimiz ilk olmak istiyoruz," dedi Daşa. Maşa sepetinden reçel kavanozunu çıkardı. "Önce sen at, Daşa, ben beklerken reçel yerim," dedi Maşa. Daşa topu attı, Maşa da bir kaşık reçel yedi. Sonra sıra kirpiye geldi. Maşa sakin kirpiyi başından yavaşça okşadı ve topu önüne koydu. Kirpi topu burnuyla itti ve top kökten kaydı. En son Maşa attı ve iki kız sevinçle güldü. "Sırayla oynamak çok eğlenceli, Daşa!" dedi Maşa.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa sepetinden reçel kavanozunu çıkardı"
   - Cümle 5: «Maşa sepetinden reçel kavanozunu çıkardı.»
   - Açıklama: Reçel sıra sorununun çözümüne katkı vermiyor; yalnız süs olarak kurulmuş bir ayrıntı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ben beklerken reçel yerim"
   - Cümle 6: «"Önce sen at, Daşa, ben beklerken reçel yerim," dedi Maşa.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümüne katkı vermeyen süs olarak kullanılmış, kartın özellik alanındaki işe yarar kullanım sağlanmamış.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa sakin kirpiyi başından yavaşça okşadı"
   - Cümle 9: «Maşa sakin kirpiyi başından yavaşça okşadı ve topu önüne koydu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde dikenli yabani bir hayvan elle okşanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0094` birebir aynı, ardından `@onarim: 30deaab80a9fb0b045dea8e64204627252bab456`, sonra gövde.

### Hikâye 4: tohum masa-0095 (deneme 1 -> 2)

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
Bir sabah ormanda gökyüzü berraktı. Daşa, Maşa'ya şehirden bir paket kurabiye getirmişti. Maşa sevinçle zıplarken paketi düşürdü ve içindeki kurabiyeler ikiye kırıldı. "Hepsi kırıldı," dedi Daşa üzgün bir sesle. "Özür dilerim, Daşa, çok acele ettim," dedi Maşa. Sonra sepetinden reçel kavanozunu çıkardı. Kırık parçaların arasına reçel sürüp onları birbirine yapıştırdı. Kurabiyeler yine bütün ve reçelli oldu. Paketten dökülen kırıntıları da bir dalla yakındaki kirpiye doğru süpürdü. Kirpi kırıntıları kokladı ve mutlu mutlu yedi. Daşa reçelli bir kurabiye tattı ve gülümsedi. "Teşekkürler, Maşa, bunlar çok güzel olmuş!" dedi Daşa.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormanda gökyüzü berraktı"
   - Cümle 1: «Bir sabah ormanda gökyüzü berraktı.»
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kırıntıları da bir dalla yakındaki kirpiye doğru süpürdü"
   - Cümle 9: «Paketten dökülen kırıntıları da bir dalla yakındaki kirpiye doğru süpürdü.»
   - Açıklama: Kırıntıları kirpiye süpürme olayı sorunla ilgisiz, işlevsiz bir yan olay.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yakındaki kirpiye doğru süpürdü"
   - Cümle 9: «Paketten dökülen kırıntıları da bir dalla yakındaki kirpiye doğru süpürdü.»
   - Açıklama: Kirpi sebepsiz beliriyor ve kırıntı süpürme olayı sorunla ilgisiz bir ayrıntı.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kirpi kırıntıları kokladı ve mutlu mutlu yedi"
   - Cümle 10: «Kirpi kırıntıları kokladı ve mutlu mutlu yedi.»
   - Açıklama: Yabani bir kirpiye kurabiye kırıntısı yedirmek çocuğun taklit edebileceği sakıncalı bir davranış örneği.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0095` birebir aynı, ardından `@onarim: eddfba832f8491b89e17c35b01d172e0eb2b698c`, sonra gövde.

### Hikâye 5: tohum masa-0096 (deneme 1 -> 2)

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
@plan: sincap boş bir boya kovasına düştü ve çıkamadı | kovaya uzun bir dal koydu ve sincap tırmandı
@tohum: masa-0096
Bir sabah Koca Ayı'nın bahçesinde yapraklar sararmıştı. Koca Ayı ağaç evinin kapısını boyuyordu, Maşa da ona bakıyordu. Birden bir sincap boş bir boya kovasına düştü ve çıkamadı. Sincap kovanın dibinde döndü ama kovanın içi kaygandı. Maşa heyecanlı heyecanlı kovanın yanına koştu. Önce elini uzattı ama kova çok derindi. Sonra kovanın içine uzun bir dal koymayı denedi. Sincap dala tutundu ve hızla yukarı tırmandı. Kovadan atladı ve kuyruğunu sallayarak ağaca koştu. Koca Ayı Maşa'ya bakıp gülümsedi. Maşa bundan sonra boş kovaları hep ters çevirip koydu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden bir sincap boş bir boya kovasına düştü"
   - Cümle 3: «Birden bir sincap boş bir boya kovasına düştü ve çıkamadı.»
   - Açıklama: Sincabın kovaya neden düştüğü söylenmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kovanın içine uzun bir dal koymayı denedi"
   - Cümle 7: «Sonra kovanın içine uzun bir dal koymayı denedi.»
   - Açıklama: Uzun dal önceden kurulmadan sebepsizce beliriyor ve çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0096` birebir aynı, ardından `@onarim: a13b9bb211ca4f8bd72f1ba165b07335b96d47a7`, sonra gövde.

### Hikâye 6: tohum masa-0097 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0097
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'şeftali', fiil 'inmek', sıfat 'kahverengi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: yuvarlak şeftali her adımda yere düştü | şeftaliyi çevirip düz yanını kaşığa koydu
@tohum: masa-0097
Bir sabah Maşa bahçede kaşık oyunu oynuyordu. Kaşığa büyük bir şeftali koyup kapıdan bahçenin öbür ucuna taşıyacaktı. Ama şeftali çok yuvarlaktı ve her adımda kaydı. Bir kez kahverengi toprağa düştü. Bir kez de çimenlerde uzağa yuvarlandı. Maşa buna çok güldü. Sonra şeftaliyi çevirip düz yanını kaşığa koymayı denedi. Şeftali artık hiç kıpırdamadı. Maşa yavaş yavaş yürüdü ve kapının merdiveninden dikkatle indi. Sonunda bahçenin öbür ucuna vardı. Şeftali yine kaşığın içindeydi. Maşa sevinçle zıpladı ve oyunu baştan bir daha oynadı.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yuvarlak şeftali her adımda yere düştü"
   - Cümle 0 (plan satırı): «yuvarlak şeftali her adımda yere düştü | şeftaliyi çevirip düz yanını kaşığa koydu»
   - Açıklama: Gövdede şeftali her adımda kayıyor, yalnız iki kez düşüyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa bahçede kaşık oyunu oynuyordu"
   - Cümle 1: «Bir sabah Maşa bahçede kaşık oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye baştan sona bahçede geçiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "her adımda kaydı"
   - Cümle 3: «Ama şeftali çok yuvarlaktı ve her adımda kaydı.»
   - Açıklama: Tekrarlanan eylem için 'kayıyordu' olmalı; 'her adımda kaydı' kip uyumsuz.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "düz yanını kaşığa koymayı denedi"
   - Cümle 7: «Sonra şeftaliyi çevirip düz yanını kaşığa koymayı denedi.»
   - Açıklama: Şeftali çok yuvarlak diye anlatılıyor ama sonra düz bir yanı olduğu söyleniyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "şeftaliyi çevirip düz yanını kaşığa"
   - Cümle 7: «Sonra şeftaliyi çevirip düz yanını kaşığa koymayı denedi.»
   - Açıklama: Şeftali çok yuvarlak deniyor ama sonra düz bir yanı olduğu söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0097` birebir aynı, ardından `@onarim: 6127da25ebbd6356228fdf536d2a7f105aa034a6`, sonra gövde.

### Hikâye 7: tohum masa-0098 (deneme 1 -> 2)

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
@plan: sepetteki biberin üstünde küçük diş izleri vardı | yaprağa reçel koyup bekledi ve sincabı gördü
@tohum: masa-0098
Ormanda güneş yeni doğmuştu. Maşa sepetini bir ağacın altına bırakıp yakında çiçek topladı. Döndüğünde sepetteki kırmızı biberin üstünde küçük diş izleri vardı. Maşa bu izleri çok merak etti. Bir yaprağa şekerli reçelinden biraz sürdü ve yaprağı sepetin yanına koydu. Sonra ağacın arkasına saklandı ve sessizce bekledi. Biraz sonra dalların arasından bir sincap hızla indi. Sincap önce biberi kokladı, sonra reçeli yaladı. Maşa güldü ve ağacın arkasından çıktı. "Demek biberi sen ısırdın, sincap!" dedi Maşa. Sincap kuyruğunu salladı ve reçelin hepsini bitirdi. Sonra Maşa ile sincap ağacın altında mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bırakıp yakında çiçek topladı"
   - Cümle 2: «Maşa sepetini bir ağacın altına bırakıp yakında çiçek topladı.»
   - Açıklama: 'Yakında' çoğunlukla 'az sonra' anlamında; 'yakınlarda' anlamı belirsiz.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Sincap önce biberi kokladı, sonra reçeli yaladı"
   - Cümle 8: «Sincap önce biberi kokladı, sonra reçeli yaladı.»
   - Açıklama: Kartın 'yanlar' bölümünde sincap fındık ve meşe palamudu sever; burada biber ısırıp reçel yiyen bir sincap var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0098` birebir aynı, ardından `@onarim: 3dd42bf74929c7713636ef131e8b47d1df575d68`, sonra gövde.

### Hikâye 8: tohum masa-0099 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0099
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'şişe', fiil 'sabırsızlanmak', sıfat 'sevimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: sabırsızlandı ve şişeyi çekti, su döküldü | özür diledi ve kalan suyla baloncuk yaptı
@tohum: masa-0099
Maşa, Koca Ayı ile tepede baloncuk yapıyordu. Koca Ayı bir şişedeki sabunlu suya halka batırıp baloncuk yapıyordu. Maşa sabırsızlandı, şişeyi hızla çekti ve su çimenlere döküldü. Koca Ayı üzgün üzgün şişeye baktı. "Özür dilerim, Koca Ayı, sabırlı olmadım," dedi Maşa. Şişenin dibinde birazcık sabunlu su kalmıştı. Maşa şişeyi eğdi ve halkayı dibe kadar batırmayı denedi. Sonra halkaya yavaşça üfledi. Halkadan kocaman bir baloncuk çıktı ve havada süzüldü. Koca Ayı sevimli bir sesle güldü ve ellerini çırptı. Bu kez Maşa halkayı Koca Ayı'ya verdi ve sırasını bekledi. Maşa çok sevindi, çünkü Koca Ayı yeniden gülüyordu.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "halka batırıp baloncuk yapıyordu"
   - Cümle 2: «Koca Ayı bir şişedeki sabunlu suya halka batırıp baloncuk yapıyordu.»
   - Açıklama: Bir önceki cümledeki 'baloncuk yapıyordu' hemen tekrarlanıyor.
   - Açıklama: 'Baloncuk yapıyordu' ilk iki cümlede art arda tekrarlanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sevimli bir sesle güldü"
   - Cümle 10: «Koca Ayı sevimli bir sesle güldü ve ellerini çırptı.»
   - Açıklama: 'Sevimli' ses için uygun bir sıfat değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0099` birebir aynı, ardından `@onarim: 5e27949f2960818f9fb19099a98413821140728b`, sonra gövde.

### Hikâye 9: tohum masa-0100 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0100
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'jöle', fiil 'ekmek', sıfat 'tedbirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: kazarken yaprakları dağıttı ve kirpi uyandı | özür diledi ve kirpiye elma jölesi verdi
@tohum: masa-0100
Bahçede Maşa, küçük bir kürekle çiçek tohumu ekiyordu. Hızla kazarken bir yaprak yığınını da dağıttı. Yaprakların altında uyuyan kirpi uyandı ve top gibi büzüldü. "Özür dilerim, kirpi, seni görmedim," dedi Maşa. Ama kirpi hiç kıpırdamadı. Maşa koşup evden bir kase elma jölesi getirdi. Jöleyi kirpiye uzatmayı denedi. Kirpi elmanın kokusunu aldı ve yavaşça açıldı. Jöleyi tattı ve burnunu Maşa'nın eline sürdü. Maşa bu kez tedbirli davrandı ve kirpiye dikkat edip yavaşça kazdı. "Artık barıştık, kirpi, hadi birlikte çiçek ekelim!" dedi Maşa.
```

**Hakem bulguları (4):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bahçede Maşa, küçük bir"
   - Cümle 1: «Bahçede Maşa, küçük bir kürekle çiçek tohumu ekiyordu.»
   - Açıklama: Özneden sonra gereksiz virgül kullanılmış.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "koşup evden bir kase elma jölesi getirdi"
   - Cümle 6: «Maşa koşup evden bir kase elma jölesi getirdi.»
   - Açıklama: Hikaye başlıktaki evde değil bahçede geçiyor ve Maşa jöle için eve gidip dönüyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Jöleyi kirpiye uzatmayı denedi"
   - Cümle 7: «Jöleyi kirpiye uzatmayı denedi.»
   - Açıklama: Çocuğun taklit edebileceği biçimde yabani bir hayvan elden insan yiyeceğiyle besleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa bu kez tedbirli davrandı"
   - Cümle 10: «Maşa bu kez tedbirli davrandı ve kirpiye dikkat edip yavaşça kazdı.»
   - Açıklama: 'Tedbirli davranmak' 3 yaşındaki bir çocuğun bilmediği soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0100` birebir aynı, ardından `@onarim: 8e13ec18866b96f3d51df73e540929301b6ce102`, sonra gövde.

### Hikâye 10: tohum masa-0101 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0101
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yaprak', fiil 'bitirmek', sıfat 'yardımsever'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: yapraklar bitince evin kırmızı çatısı eksik kaldı | kendi yapraklarını paylaştı ve çatıya tek tek koydu
@tohum: masa-0101
Hava güneşli ve sıcaktı. Maşa ile kuzeni Daşa ormanda yere yapraklardan birer ev yapıyordu. Ama Daşa evinin çatısını bitiremedi, çünkü kırmızı yaprağı kalmamıştı. "Evimin çatısı eksik kaldı," dedi Daşa. Maşa kendi yaprak yığınına baktı. Orada daha bir sürü kırmızı yaprak vardı. "Bu yaprakları seninle paylaşırım, Daşa," dedi Maşa. Maşa yaprakları çatının boş yerine tek tek koymayı denedi. Büyükler sığmadı ama küçükler tam oldu. Sonunda Daşa'nın evinin de kırmızı bir çatısı vardı. Daşa sevinçle ellerini çırptı. "Teşekkürler, Maşa, sen çok yardımsever bir kızsın!" dedi Daşa.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Büyükler sığmadı ama küçükler"
   - Cümle 9: «Büyükler sığmadı ama küçükler tam oldu.»
   - Açıklama: 'Büyükler' ve 'küçükler' yapraklar için kullanılmış; 'büyükler' çocuğa yetişkinleri çağrıştırıyor, 'büyük yapraklar' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Büyükler sığmadı ama küçükler"
   - Cümle 9: «Büyükler sığmadı ama küçükler tam oldu.»
   - Açıklama: 'Büyükler' ve 'küçükler' neyi gösterdiği belirsiz; yapraklar yerine insanlar anlaşılabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0101` birebir aynı, ardından `@onarim: 0890642e3fec0cb0faa073ff2a725afbb69b2dc8`, sonra gövde.

### Hikâye 11: tohum masa-0102 (deneme 1 -> 2)

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
@plan: zıplarken ayakkabısı yumuşak çamura takıldı | ayağını sağa sola küçük küçük salladı
@tohum: masa-0102
@degisim: kanepe -> çamur
Bir sabah ormanda yağmur yeni dinmişti. Maşa patikadaki su birikintilerine zıplıyor, sular havaya fışkırıyordu. Ama bir anda Maşa'nın ayakkabısı yumuşak bir çamura takıldı. Maşa ayağını hızla çekti ama ayağı yerinden çıkmadı. Maşa durmadı ve başka bir yol denedi. Ayağını sağa ve sola küçük küçük salladı. Ayakkabı biraz oynadı ve Maşa umutlu bir yüzle devam etti. Sonunda ayağı ayakkabısıyla birlikte çamurdan çıktı. Maşa çamurlu ayakkabısına baktı ve güldü. Sonra yine su birikintilerine zıpladı ama bu kez çamurdan uzak durdu. Maşa bundan sonra çamurda ayağını çekmedi, yavaşça salladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa umutlu bir yüzle"
   - Cümle 7: «Ayakkabı biraz oynadı ve Maşa umutlu bir yüzle devam etti.»
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa umutlu bir yüzle devam etti"
   - Cümle 7: «Ayakkabı biraz oynadı ve Maşa umutlu bir yüzle devam etti.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir ifade ve neye devam ettiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0102` birebir aynı, `@degisim: kanepe -> çamur` (tutuyorsan), ardından `@onarim: 65b9d24af78e59b0be054c2971602ada310e3acb`, sonra gövde.

### Hikâye 12: tohum masa-0103 (deneme 1 -> 2)

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
@plan: reçel kavanozu yokuştan aşağı kaçtı ve kayboldu | kavanozdaki kırmızı şeridi otların arasında aradı
@tohum: masa-0103
Rüzgar hafif hafif esiyordu. Maşa tepede elmalı reçel kavanozunu kucağında tutuyordu. Birden kavanoz elinden kaydı ve yokuştan aşağı kaçtı. Kavanoz uzun otların arasında kayboldu. Maşa aşağıya yavaşça indi ve otlara baktı. Ama otlar çok sıktı ve kavanoz görünmüyordu. Maşa reçelini hiç kaybetmemek için kavanozun kapağına kırmızı bir şerit bağlamıştı. Şimdi otların arasında o kırmızı rengi aradı. Sonunda bir çalının dibinde kırmızı şerit göründü. Maşa kavanozu aldı ve ona sevinçle sarıldı. Sonra tepeye geri çıktı ve reçelinden mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kavanozu yokuştan aşağı kaçtı"
   - Cümle 0 (plan satırı): «reçel kavanozu yokuştan aşağı kaçtı ve kayboldu | kavanozdaki kırmızı şeridi otların arasında aradı»
   - Açıklama: Kavanoz kaçmaz; fiil öznesine uymuyor.
   - Açıklama: Plan satırında da kavanoz için 'kaçtı' kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yokuştan aşağı kaçtı"
   - Cümle 3: «Birden kavanoz elinden kaydı ve yokuştan aşağı kaçtı.»
   - Açıklama: Kavanoz kaçmaz; 'yuvarlandı' olmalı.
   - Açıklama: Kavanoz kaçmaz; fiil cansız özneye uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kavanozun kapağına kırmızı bir şerit bağlamıştı"
   - Cümle 7: «Maşa reçelini hiç kaybetmemek için kavanozun kapağına kırmızı bir şerit bağlamıştı.»
   - Açıklama: Çözümü getiren şerit önceden kurulmadan tam gerektiği anda geriye dönük olarak ortaya çıkıyor.
   - Açıklama: Kırmızı şerit önceden kurulmadan tam çözüm gerektiğinde sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0103` birebir aynı, ardından `@onarim: c7a5a5cab37a60b3e32235f162594a75aaf6b7c6`, sonra gövde.
