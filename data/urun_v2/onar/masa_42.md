# Editör görevi (onarım): Maşa, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0156 (deneme 3 -> 4)

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
Maşa ile Daşa tepede bir kumaşın üstünde piknik yapıyordu. Sepette kurabiyeler vardı. Birden yakından çıtır çıtır bir ses geldi. Ama ikisi de bir şey yemiyordu. "Kurabiyeleri kim yiyor?" diye sordu Daşa. "Ben reçelli kurabiyeleri çok severim, Daşa, onlar hiç çıtır değil!" dedi Maşa. Maşa sessizce durdu ve dinledi. Ses büyük bir kayanın arkasından geliyordu. İkisi yavaşça kayanın arkasına baktı. Orada bir sincap fındık kırıyordu. Bu ses fındığın kabuğundan çıkıyordu. Sincap fındığını çok beğendi ve kuyruğunu salladı. Maşa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ben reçelli kurabiyeleri çok severim"
   - Cümle 6: «"Ben reçelli kurabiyeleri çok severim, Daşa, onlar hiç çıtır değil!" dedi Maşa.»
   - Açıklama: Tohumdaki reçel özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki reçel özelliği sesin kaynağını bulmaya yaramıyor; çözüm dinlemekle geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ben reçelli kurabiyeleri çok severim"
   - Cümle 6: «"Ben reçelli kurabiyeleri çok severim, Daşa, onlar hiç çıtır değil!" dedi Maşa.»
   - Açıklama: Maşa'nın reçelli kurabiye repliği sorunla ilgisiz ve olayı ilerletmeyen işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0156` birebir aynı, ardından `@onarim: c5a15c1a1ee4088e1be63a5c7d6f567c4e12a314`, sonra gövde.

### Hikâye 2: tohum masa-0159 (deneme 2 -> 3)

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
Bir sabah Maşa ile Koca Ayı ormandaki patikada yürüyordu. Koca Ayı kucağında küçük, yuvarlak bir fıçı taşıyordu. Patikada aç bir kirpi elma arıyordu ama yakında hiç elma yoktu. Kirpi Maşa'ya baktı ve burnunu kıpırdattı. "Koca Ayı, kirpi çok acıkmış," dedi Maşa. Sonra fıçının kapağını açtı. İçinde Maşa'nın en sevdiği elma reçeli vardı. Koca Ayı, Maşa'ya bir kaşık uzattı. Maşa bir yaprağın üstüne üç kaşık reçel koydu. "Bir kaşık, iki kaşık, üç kaşık," diye saydı Maşa. Kirpi yaprağa koştu ve reçeli yedi. Sonra Maşa'nın ayağının yanına mutlu mutlu oturdu. "Afiyet olsun, küçük kirpi!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra fıçının kapağını açtı."
   - Cümle 6: «Sonra fıçının kapağını açtı.»
   - Açıklama: Fıçıyı Koca Ayı taşıdığı için kapağı kimin açtığı belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0159` birebir aynı, ardından `@onarim: 6c4515d21aec763bad26ba0855dcf081fd19f661`, sonra gövde.

### Hikâye 3: tohum masa-0160 (deneme 2 -> 3)

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
Tepede serin bir rüzgar esiyordu. Maşa hazırlıklı gelmişti ve kağıttan bir uçurtma yapmıştı. Ama rüzgar uçurtmanın kağıt kuyruğunu koparıp çimlere attı. Kuyruğun ucu yırtılmıştı ve artık bağlanmıyordu. Maşa reçeli çok severdi, bu yüzden çantasında bir kavanoz vardı. Kavanozu hatırladı ve kuyruğun ucuna biraz reçel sürdü. Kuyruğu uçurtmanın altına bastırdı ve kuyruk sıkıca yapıştı. Maşa parmağındaki reçeli de yaladı ve güldü. Sonra uçurtmanın ipini tuttu ve koşmaya başladı. Rüzgar uçurtmayı havaya kaldırdı. Uzun kuyruk da gökyüzünde sallandı. Maşa uçurtmasını mutlu mutlu uçurdu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa hazırlıklı gelmişti"
   - Cümle 2: «Maşa hazırlıklı gelmişti ve kağıttan bir uçurtma yapmıştı.»
   - Açıklama: 'Hazırlıklı gelmek' soyut bir anlatım, küçük çocuk için anlaşılır değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bu yüzden çantasında bir kavanoz vardı"
   - Cümle 5: «Maşa reçeli çok severdi, bu yüzden çantasında bir kavanoz vardı.»
   - Açıklama: Reçel kavanozu sorundan sonra tam çözüm gerektiğinde beliriyor ve çözümü kolayca getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0160` birebir aynı, `@degisim: mektup -> uçurtma` (tutuyorsan), ardından `@onarim: 61193393c837ce514c25b39021ea8f052ee74060`, sonra gövde.

### Hikâye 4: tohum masa-0161 (deneme 2 -> 3)

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
@plan: sincabın fındığı flütün içinde sıkıştı | parçayı ters çevirip hafifçe vurdu ve fındığı çıkardı
@tohum: masa-0161
Evin önündeki bahçede Maşa oyuncak flütünün iki parçasını temizliyordu. Bir sincap geldi ve bir parçaya küçük bir fındık sakladı. Ama fındık bu dar yerde sıkıştı ve dışarı çıkmadı. Sincap üzgün üzgün Maşa'ya baktı. "Üzülme, sincap, sana yardım ederim," dedi Maşa. Maşa önce parçayı salladı ama fındık yerinden oynamadı. Sonra parçayı ters çevirip ucuna hafifçe vurmayı denedi. Fındık "pıt" diye çimlere düştü. Sincap fındığını hemen kaptı ve sevinçle zıpladı. Maşa iki parçayı birleştirdi ve flütünden yavaş bir ses çıkardı. Sincap sesi duyunca kuyruğunu salladı. İkisi bahçede mutlu mutlu eğlenmeye devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "flütünden yavaş bir ses çıkardı"
   - Cümle 10: «Maşa iki parçayı birleştirdi ve flütünden yavaş bir ses çıkardı.»
   - Açıklama: Ses için 'yavaş' yanlış sıfat; 'yumuşak' ya da 'hafif' olmalı.
   - Açıklama: Ses 'yavaş' olmaz; 'hafif' ya da 'ince' bir ses olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0161` birebir aynı, ardından `@onarim: 709749ae72e4efab8225cd0df601ee035c0083a8`, sonra gövde.

### Hikâye 5: tohum masa-0162 (deneme 2 -> 3)

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
@degisim: takmak -> asmak
Maşa yağmurdan sonra çamurlu bahçeye çıkamadı ve evde kaldı. Pencereden baktı ve bahçede yeni açmış kırmızı çiçekler gördü. Onların resmini yapmak istedi ama kırmızı boyası bitmişti. Maşa hemen mutfaktan en sevdiği çilek reçelini getirdi. Parmağını reçele batırdı ve kağıda çiçekler yaptı. Sonra boyalarıyla yeşil yapraklar çizdi. Parmağında kalan reçeli de yaladı ve güldü. Resim bahçedeki çiçeklere çok benzedi. Maşa resmi pencerenin yanındaki çiviye astı. Şimdi dışarı çıkmadan da kırmızı çiçeklere bakabilirdi. Maşa mutlu mutlu el çırptı.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "yağmurdan sonra çamurlu bahçeye çıkamadı"
   - Cümle 1: «Maşa yağmurdan sonra çamurlu bahçeye çıkamadı ve evde kaldı.»
   - Açıklama: Dışarı çıkamama ve kırmızı boyanın bitmesi olmak üzere iki ayrı sorun kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0162` birebir aynı, `@degisim: takmak -> asmak` (tutuyorsan), ardından `@onarim: 1d42455dadb85a68fb88fd3281efd1c837e6588b`, sonra gövde.

### Hikâye 6: tohum masa-0164 (deneme 2 -> 3)

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
@plan: kirpi yerde yiyecek arıyordu ve yanına gelmedi | yoğurttan sonra elma getirmeyi denedi ve arkadaş oldu
@tohum: masa-0164
@degisim: çekingen -> küçük
Evin önünde hafif bir rüzgar esiyordu. Maşa çalının altında küçük bir kirpi gördü. Onunla arkadaş olmak istedi ama kirpi burnuyla yerde yiyecek arıyordu. "Merhaba, kirpi, benimle oynar mısın?" dedi Maşa. Kirpi başını kaldırmadı. Maşa bir kaseye biraz yoğurt koydu ve kirpiye götürdü. Kirpi yoğurdu kokladı ama yemedi. Maşa bu kez başka bir şey denedi. Oyuncak arabasına kırmızı elmalar yükledi ve arabayı ona doğru çekti. Kirpi elmaları görünce başını kaldırdı. Sonra bir elmayı ısırdı ve Maşa'nın yanına geldi. Maşa çok sevindi, çünkü yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa bir kaseye biraz yoğurt koydu"
   - Cümle 6: «Maşa bir kaseye biraz yoğurt koydu ve kirpiye götürdü.»
   - Açıklama: Yabani kirpiye süt ürünü vermek taklit edildiğinde hayvana zarar verebilecek bir davranış örneği.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0164` birebir aynı, `@degisim: çekingen -> küçük` (tutuyorsan), ardından `@onarim: e12c3b58706d7409811c04690b18c9039c3d7de4`, sonra gövde.

### Hikâye 7: tohum masa-0166 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: yürürken nereden geldiği bilinmeyen bir ses geldi | durup dinledi ve sesi çantasında buldu
@tohum: masa-0166
Bir sabah Maşa ormandaki patikada yürüyordu. Örgü çantasında en sevdiği reçel vardı. Yürürken yakından "tık tık" diye bir ses geliyordu. Maşa bu sesi çok merak etti. Biraz yorgundu ve bir kütüğe oturdu. O zaman ses de hemen sustu. Maşa kalkıp yeniden yürüdü ve ses yine başladı. Bu kez yürürken sesi iyi dinledi. Ses çantadan geliyordu! Maşa çantayı açtı ve içine baktı. İçindeki kaşık reçel kavanozuna çarpıp "tık tık" ediyordu. Kaşığı alıp cebine koydu ve güldü. Maşa bundan sonra bir ses duyunca önce durup dikkatle dinledi.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yürürken nereden geldiği bilinmeyen bir ses geldi"
   - Cümle 0 (plan satırı): «yürürken nereden geldiği bilinmeyen bir ses geldi | durup dinledi ve sesi çantasında buldu»
   - Açıklama: 'Yürürken' ulacının öznesi 'ses' olamaz; plan cümlesi özne uyumsuz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi çantasında buldu"
   - Cümle 0 (plan satırı): «yürürken nereden geldiği bilinmeyen bir ses geldi | durup dinledi ve sesi çantasında buldu»
   - Açıklama: Ses bulunmaz; bulunan sesin kaynağıdır, fiil nesnesine uymuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği reçel vardı"
   - Cümle 2: «Örgü çantasında en sevdiği reçel vardı.»
   - Açıklama: Tohumdaki reçel sevgisi (kartın özellikler alanı) yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0166` birebir aynı, ardından `@onarim: c10278717fd04682767be63430537b87330715b8`, sonra gövde.

### Hikâye 8: tohum masa-0172 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0172
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yelek', fiil 'hızlanmak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: yelek kızın kolundan kaydı ve kayboldu | reçel kokusunu izleyip yeleğini otların arasında buldu
@tohum: masa-0172
Bir sabah Maşa ormandaki patikada koşuyordu. Hava sıcaktı ve yeleğini çıkarıp koluna asmıştı. Maşa hızlandı ve yelek kolundan kaydı, bir yere düştü. Biraz sonra yeleğin kolunda olmadığını fark etti. Yeleğin cebinde kremalı, reçelli bir çörek vardı. Maşa geri döndü ama yeşil yelek uzun otların arasında görünmüyordu. Sonra durdu ve havayı derin derin kokladı. En sevdiği reçelin kokusunu hemen tanıdı. Kokunun geldiği yere yürüdü. Otların arasında yeşil yeleğini buldu. Çörek de cebinde duruyordu. Maşa yeleğini hemen giydi ve güldü. Maşa çok sevindi, çünkü yeleğini kendi burnuyla bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yeleğin cebinde kremalı, reçelli bir çörek vardı"
   - Cümle 5: «Yeleğin cebinde kremalı, reçelli bir çörek vardı.»
   - Açıklama: Cepteki çörek sorun çıktıktan sonra sebepsizce kuruluyor ve koku ile bulma çözümünü hazır getiriyor.
   - Açıklama: Cepteki çörek yelek kaybolduktan sonra, yalnız çözümü getirmek için sebepsizce ortaya çıkarılıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa yeleğini hemen giydi"
   - Cümle 12: «Maşa yeleğini hemen giydi ve güldü.»
   - Açıklama: Hava sıcak olduğu için çıkardığı yeleği sebepsizce hemen yeniden giyiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0172` birebir aynı, ardından `@onarim: 45cad0ecb04df7c3fc06c30327de1b36e36c16cf`, sonra gövde.

### Hikâye 9: tohum masa-0173 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0173
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'tekne', fiil 'fısıldamak', sıfat 'gri'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: yırtık yapraktan yapılan tekneye su doldu | kuzeninden yardım isteyip kabuktan tekne yaptı
@tohum: masa-0173
Ormanda gökyüzü griydi ve patikada büyük bir su birikintisi vardı. Maşa kuru bir yapraktan küçük bir tekne yaptı. Ama yaprak yırtıktı ve teknenin içine hemen su doldu. Kuzeni Daşa bir ağacın altında oturuyordu. "Daşa, teknem batıyor, bana yardım eder misin?" diye sordu Maşa. Daşa biraz düşündü. "Kalın bir ağaç kabuğu batmaz," diye fısıldadı Daşa. Maşa bunu hemen denedi. Yerden gri bir kabuk buldu. Sonra yeni teknesini suya bıraktı. Gri tekne batmadı ve suyun üstünde yüzdü. "Teşekkürler, Daşa, teknem yüzüyor!" dedi Maşa. Maşa ile Daşa çok sevindi, çünkü tekne sonunda yüzmüştü.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "tekne sonunda yüzmüştü"
   - Cümle 13: «Maşa ile Daşa çok sevindi, çünkü tekne sonunda yüzmüştü.»
   - Açıklama: Teknenin yüzdüğü daha önce iki kez söylendi; son cümle gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0173` birebir aynı, ardından `@onarim: 422f49c941aa7d333a4bfc829cf6d103ed60d91c`, sonra gövde.
