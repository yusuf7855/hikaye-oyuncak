# Editör görevi (onarım): Doru, onarım partisi 46

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar46.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Doru | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar46.txt --ad urun_v2`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Onarılacak hikâyeler

### Hikâye 1: tohum doru-0164 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0164
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: -
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kar', fiil 'şaşırtmak', sıfat 'faydalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | -
@plan: kar yağmıştı ve çimenleri kapatmıştı | ayaklarıyla karı itip çimenleri ortaya çıkardı
@tohum: doru-0164
@degisim: faydalı -> bembeyaz
Parkın her tarafı bembeyazdı. Sabah yağan kar Doru'yu çok şaşırttı. Ama kar bütün çimenleri kapatmıştı ve sürü yiyecek bir şey bulamıyordu. Doru sürüye yardım etmek istedi. Ön ayaklarıyla karı iki yana itti. Karın altından yeşil çimenler çıktı. Doru biraz ileri yürüdü ve karı yine itti. Sonra bir yer daha açtı. Az sonra parkta geniş, yeşil bir yer oldu. Artık yemek için bol bol çimen vardı. Doru çok sevindi, çünkü bütün sürüye yetecek kadar çimeni karın altından çıkarmıştı.
```

**Hakem bulguları (4):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "sürü yiyecek bir şey bulamıyordu"
   - Cümle 3: «Ama kar bütün çimenleri kapatmıştı ve sürü yiyecek bir şey bulamıyordu.»
   - Açıklama: Arka plandaki çoğul canlılar (sürü) sorunun parçası olarak olaya katılıyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "sürü yiyecek bir şey bulamıyordu"
   - Cümle 3: «Ama kar bütün çimenleri kapatmıştı ve sürü yiyecek bir şey bulamıyordu.»
   - Açıklama: Belirsiz kelime sürü canlı bir rol olarak olayın içinde geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sürü yiyecek bir şey bulamıyordu"
   - Cümle 3: «Ama kar bütün çimenleri kapatmıştı ve sürü yiyecek bir şey bulamıyordu.»
   - Açıklama: Sürü hiç tanıtılmadan beliriyor ve sonra hikayede hiç görünmüyor.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Doru sürüye yardım etmek istedi"
   - Cümle 4: «Doru sürüye yardım etmek istedi.»
   - Açıklama: Arka plandaki çoğul canlı sürü, yardım edilen taraf olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0164` birebir aynı, `@degisim: faydalı -> bembeyaz` (tutuyorsan), ardından `@onarim: 0391ec0ecbfe7fa2ee8ce6c38038a82bc3bf09a7`, sonra gövde.

### Hikâye 2: tohum doru-0165 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0165
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sırayla oynamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'leke', fiil 'beğenmek', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: kozalak yoldan çıktı ve çalılara doğru yuvarlandı | düz yolda hızla koşup kozalağı durdurdu
@tohum: doru-0165
@degisim: leke -> kozalak
Doru ile Kırat ormanda kozalak oyunu oynuyordu. Kozalağı sırayla burunlarıyla itiyorlardı. Uykulu Kırat bir kez bakmadan itti ve kozalak yoldan çıktı. Kozalak sık çalılara doğru yuvarlandı. Çalıların arasında onu bir daha bulamazlardı. Doru hemen düz yolda hızla koştu. Kozalağı çalıların hemen önünde yakaladı ve ayağıyla durdurdu. Sonra onu burnuyla Kırat'a geri itti. Kırat bu kez kozalağı yavaşça itti. Kırat oyunu çok beğendi ve başını salladı. İkisi sırayla oynamaya devam etti. Doru çok sevindi, çünkü kozalak kaybolmamıştı ve oyunları sürüyordu.
```

**Hakem bulguları (2):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Uykulu Kırat bir kez bakmadan itti"
   - Cümle 3: «Uykulu Kırat bir kez bakmadan itti ve kozalak yoldan çıktı.»
   - Açıklama: Kartın Kırat ilişkisi onu en çok bilen, danışılan en yaşlı üye olarak verir; dikkatsiz ve yanlış hamle yapan rol Karatay'ın özelliğidir.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Çalıların arasında onu bir daha bulamazlardı"
   - Cümle 5: «Çalıların arasında onu bir daha bulamazlardı.»
   - Açıklama: Kozalakla dolu ormanda bir kozalağın kaybolması önemsiz bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0165` birebir aynı, `@degisim: leke -> kozalak` (tutuyorsan), ardından `@onarim: 328fb62e7314edc45ee38d45a4a19df1825e70f6`, sonra gövde.

### Hikâye 3: tohum doru-0167 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0167
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'blok', fiil 'örtmek', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: oynarken annesinden uzaklaştı | düz yolda koşup annesine döndü ve özür diledi
@tohum: doru-0167
@degisim: kırılgan -> geniş
Doru ormanda annesiyle birlikte çimen yiyordu. Annesi ona yanında kalmasını söylemişti. Ama Doru yaprakların arasında oynarken annesinden uzaklaştı. Doru geri baktı ama büyük bir taş blok annesini örtüyordu. Doru annesini göremedi ve onun sözünü hatırladı. Annesinin yanına hemen dönmek istedi. Ormanın düz ve geniş yolunda hızla koştu. Annesi taşın yanında onu bekliyordu. Doru başını eğdi ve annesinden özür diledi. Annesi başını Doru'nun başına sürdü. Doru çok sevindi, çünkü annesinin yanına çabucak dönmüştü.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "taş blok annesini örtüyordu"
   - Cümle 4: «Doru geri baktı ama büyük bir taş blok annesini örtüyordu.»
   - Açıklama: Taş kimseyi örtmez; 'gizliyordu' ya da 'kapatıyordu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "büyük bir taş blok annesini örtüyordu"
   - Cümle 4: «Doru geri baktı ama büyük bir taş blok annesini örtüyordu.»
   - Açıklama: Taş annesini örtmez; 'gizliyordu' ya da 'kapatıyordu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir taş blok"
   - Cümle 4: «Doru geri baktı ama büyük bir taş blok annesini örtüyordu.»
   - Açıklama: 'Blok' kelimesini 3 yaşındaki çocuk bilmez.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ormanın düz ve geniş yolunda hızla koştu"
   - Cümle 7: «Ormanın düz ve geniş yolunda hızla koştu.»
   - Açıklama: Sorunun sebebi annesini taşın arkasında görememek, ama çözüm annesini nasıl bulacağına yönelmeden yolda koşmak oluyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ormanın düz ve geniş yolunda hızla koştu"
   - Cümle 7: «Ormanın düz ve geniş yolunda hızla koştu.»
   - Açıklama: Düz ve geniş yol sebepsiz beliriyor ve annesi zaten taşın yanında olduğu için koşmanın annesine nasıl götürdüğü anlaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0167` birebir aynı, `@degisim: kırılgan -> geniş` (tutuyorsan), ardından `@onarim: dcd11a641b52d07859bcd862a21e3f30fe503106`, sonra gövde.

### Hikâye 4: tohum doru-0168 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0168
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bez', fiil 'dokunmak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: rüzgar en sevdiği tüyü vadinin öbür ucuna götürdü | açık ve düz yerde koşup tüyü buldu
@tohum: doru-0168
@degisim: bez -> tüy
Bir sabah Doru vadide en sevdiği beyaz tüyle oynuyordu. Birden sert bir rüzgar esti ve tüyü vadinin öbür ucuna götürdü. Tüy orada karmakarışık otların arasına düştü. Doru tüyünü artık göremiyordu. Doru onu hemen bulmak istedi. Vadinin ortası açık ve düzdü. Doru orada hızla koştu. Otların arasında küçük beyaz bir şey gördü. Doru yaklaştı ve burnuyla ona dokundu. Bu onun tüyüydü! Doru tüyü dişleriyle tuttu ve oyun yerine döndü. Sonra tüyüyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sert bir rüzgar esti ve tüyü vadinin öbür ucuna götürdü"
   - Cümle 2: «Birden sert bir rüzgar esti ve tüyü vadinin öbür ucuna götürdü.»
   - Açıklama: Rüzgar tüyü götürüyor, Doru koşup buluyor ve bitiyor; sorun örnekteki önemsiz 'rüzgar dağıttı, topladı, bitti' kalıbına çok yakın.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0168` birebir aynı, `@degisim: bez -> tüy` (tutuyorsan), ardından `@onarim: 9fcf3d82c76188fdd4ca66f3ba2bdbb86122a756`, sonra gövde.

### Hikâye 5: tohum doru-0169 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0169
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Karatay
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'demet', fiil 'uyandırmak', sıfat 'küçük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: oynarken yüksek sesle uyuyan arkadaşını uyandırdı | cesaretle özür diledi ve ona yonca getirdi
@tohum: doru-0169
Kuşlar ötüyordu ve Karatay ormanda bir ağacın altında uyuyordu. Doru yakında oynarken yüksek sesle kişnedi. Karatay bu sesle birden uyandı ve kızgın kızgın baktı. "Doru, ben uyuyordum!" dedi Karatay. Doru önce durdu ve yere baktı. Sonra cesaretle Karatay'ın yanına gitti. "Özür dilerim, Karatay, seni ben uyandırdım," dedi Doru. Doru arkadaşını sevindirmek de istedi. Ağzıyla küçük bir demet yonca kopardı. Onları Karatay'ın önüne bıraktı. Karatay hepsini yedi ve güldü. "Teşekkürler, Doru, sen çok iyi bir arkadaşsın!" dedi Karatay.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yüksek sesle uyuyan arkadaşını uyandırdı"
   - Cümle 0 (plan satırı): «oynarken yüksek sesle uyuyan arkadaşını uyandırdı | cesaretle özür diledi ve ona yonca getirdi»
   - Açıklama: Söz dizimi yüzünden 'yüksek sesle' uyumayı niteliyor gibi okunuyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "oynarken yüksek sesle uyuyan arkadaşını"
   - Cümle 0 (plan satırı): «oynarken yüksek sesle uyuyan arkadaşını uyandırdı | cesaretle özür diledi ve ona yonca getirdi»
   - Açıklama: Kelime sırası yüzünden 'yüksek sesle' uyumayı niteliyor gibi okunuyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Onları Karatay'ın önüne bıraktı"
   - Cümle 10: «Onları Karatay'ın önüne bıraktı.»
   - Açıklama: Tekil 'bir demet yonca' için çoğul 'onları' zamiri uyumsuz.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onları Karatay'ın önüne bıraktı"
   - Cümle 10: «Onları Karatay'ın önüne bıraktı.»
   - Açıklama: Çoğul 'onları' zamiri tekil 'demet' kelimesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0169` birebir aynı, ardından `@onarim: a382ac88c9cfdee0eab7e14079cd16f63f22e6ff`, sonra gövde.

### Hikâye 6: tohum doru-0170 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0170
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'yama', fiil 'yatmak', sıfat 'paslı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: yakındaki çiçekler gölgede kaldı ve açmadı | güneşteki çiçekleri gördü ve oraya koştu
@tohum: doru-0170
@degisim: paslı -> sarı
Bir sabah Doru ile Kırat parkta yatıyor ve çiçeklerin açmasını bekliyordu. Ama yakındaki çiçekler büyük bir ağacın altında, gölgede kalmıştı. Bu yüzden o çiçekler açmıyordu. Doru başını kaldırdı ve parkın öbür ucuna baktı. Orada güneşin altında sarı çiçeklerden bir yama vardı. "Kırat, oradaki çiçekler güneşte, onlar açar!" dedi Doru. Doru hızla oraya koştu. Bu çiçekler yavaş yavaş açıyordu. Doru bir çiçeğin açmasını baştan sona gördü. Kırat da yavaşça Doru'nun yanına geldi. "Ne güzel, değil mi?" dedi Kırat. Sonra ikisi açan çiçekleri birlikte mutlu mutlu seyretti.
```

**Hakem bulguları (4):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Doru ile Kırat parkta yatıyor"
   - Cümle 1: «Bir sabah Doru ile Kırat parkta yatıyor ve çiçeklerin açmasını bekliyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; hikaye yeri insan yapımı bir park olarak adlandırıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sarı çiçeklerden bir yama"
   - Cümle 5: «Orada güneşin altında sarı çiçeklerden bir yama vardı.»
   - Açıklama: 'Yama' kumaş parçası demektir; çiçek öbeği anlamında yanlış kullanılmış.
   - Açıklama: Yama giysiye dikilen parçadır, çiçek öbeği anlamında kullanılmaz.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru hızla oraya koştu"
   - Cümle 7: «Doru hızla oraya koştu.»
   - Açıklama: Tohumdaki hız özelliği sorunun çözümüne katkı yapmıyor; güneşteki çiçeklere yavaş gitmek de yeterdi.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Doru hızla oraya koştu"
   - Cümle 7: «Doru hızla oraya koştu.»
   - Açıklama: Çözüm gölge sebebine yönelmiyor; gölgedeki çiçekler açmıyor, Doru yalnız başka çiçeklere gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0170` birebir aynı, `@degisim: paslı -> sarı` (tutuyorsan), ardından `@onarim: 1be9eb12e0f45cd12278131c01d16d95ef2f7fa2`, sonra gövde.

### Hikâye 7: tohum doru-0171 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0171
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'kütük', fiil 'kopmak', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: rüzgarda bir dal koptu ve kütüğe giden yolu kapattı | rüzgar dinince cesaretle dala yaklaştı ve onu kenara itti
@tohum: doru-0171
Rüzgar ağaçların arasında sert sert esiyordu. Doru ormanda bir oyun oynuyordu; geniş bir kütük onun dağı olacaktı. Ama rüzgarda büyük bir dal koptu ve kütüğe giden yolu kapattı. Doru önce durdu ve rüzgarın dinmesini bekledi. Hava sakin olunca cesaretle büyük dala yaklaştı. Dalı burnuyla yavaş yavaş yolun kenarına itti. Yol açılınca hemen kütüğe koştu. Doru ön ayaklarını kütüğün üstüne koydu ve başını kaldırdı. Artık oyundaki dağın tepesindeydi. Doru çok sevindi, çünkü oyununu yine oynayabiliyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "geniş bir kütük onun dağı olacaktı"
   - Cümle 2: «Doru ormanda bir oyun oynuyordu; geniş bir kütük onun dağı olacaktı.»
   - Açıklama: Kütüğün hayali bir dağ olması mecazlı bir anlatım, küçük çocuk için belirsiz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kütüğe giden yolu kapattı"
   - Cümle 3: «Ama rüzgarda büyük bir dal koptu ve kütüğe giden yolu kapattı.»
   - Açıklama: Ormanda tek bir dalın kütüğe giden yolu kapatması, etrafından dolaşılabileceği için zayıf bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0171` birebir aynı, ardından `@onarim: c29d4c9ca372cea6f2aea5e679a22f94e38f7904`, sonra gövde.

### Hikâye 8: tohum doru-0173 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0173
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'buğday', fiil 'süslenmek', sıfat 'rüzgarlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: kayaların arasından garip bir ıslık sesi geldi | cesaretle kayalara yürüdü ve taşta bir delik buldu
@tohum: doru-0173
@degisim: buğday -> delik
Dağda rüzgarlı bir sabahtı. Doru büyük kayaların yakınında çimen yiyordu. Birden kayaların arasından ince bir ıslık sesi geldi. Doru bu sesi çok merak etti. Ses biraz garipti ama Doru cesurdu. Kayaların arasına adım adım yürüdü. Orada eski ve büyük bir taş gördü. Taşın ortasında yuvarlak bir delik vardı. Deliğin kenarı ince otlarla süslenmişti. Rüzgar esince delikten ıslık sesi çıktı ve otlar sallandı. Rüzgar durunca ses de otlar da durdu. Doru sesin bu delikten geldiğini anladı. Sonra taşın yanında mutlu mutlu çimen yemeye devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kayaların arasından ince bir ıslık sesi geldi"
   - Cümle 3: «Birden kayaların arasından ince bir ıslık sesi geldi.»
   - Açıklama: Garip bir ses gerçek bir sorun değil; Doru'nun önemseyeceği bir şey bozulmuyor, yalnız merak var.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ince otlarla süslenmişti"
   - Cümle 9: «Deliğin kenarı ince otlarla süslenmişti.»
   - Açıklama: 'Süslenmek' birinin süslemesini gerektirir; otlar için yanlış anlamda.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Deliğin kenarı ince otlarla süslenmişti"
   - Cümle 9: «Deliğin kenarı ince otlarla süslenmişti.»
   - Açıklama: Otların deliği süslemesi mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0173` birebir aynı, `@degisim: buğday -> delik` (tutuyorsan), ardından `@onarim: e9da341f7258b38b9e8cf855c0b0c41127ae63ef`, sonra gövde.

### Hikâye 9: tohum doru-0174 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0174
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yonca', fiil 'bitirmek', sıfat 'kilitli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesi başını iki taşın arasına sokamadı | ilk kez başını taşların arasına uzatıp yonca çekti
@tohum: doru-0174
@degisim: kilitli -> mor
Doru annesiyle dağda yonca arıyordu. İki büyük taşın arasında mor yonca vardı. Annesi başını uzattı ama taşların arası onun için çok dardı. Doru daha önce hiç böyle bir şey yapmamıştı. Ama annesine yardım etmek istedi. "Anne, ben yapabilirim!" dedi Doru. Doru küçük başını taşların arasına uzattı ve yoncayı dişleriyle çekti. Sonra onu annesinin önüne bıraktı. "Aferin, Doru, bunu ilk kez yaptın!" dedi annesi. Doru birkaç kez daha başını uzattı ve yonca çekti. Sonra ikisi hepsini mutlu mutlu yiyip bitirdi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "hiç böyle bir şey yapmamıştı"
   - Cümle 4: «Doru daha önce hiç böyle bir şey yapmamıştı.»
   - Açıklama: 'Böyle bir şey' henüz anlatılmamış bir eylemi gösteriyor; neyi kastettiği belli değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru küçük başını taşların arasına uzattı"
   - Cümle 7: «Doru küçük başını taşların arasına uzattı ve yoncayı dişleriyle çekti.»
   - Açıklama: Başı dar bir aralığa sokmak çocuğun taklit edebileceği, sıkışma tehlikesi olan bir davranış.
   - Açıklama: Başı dar bir aralığa sokmak çocuğun taklit edince sıkışabileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0174` birebir aynı, `@degisim: kilitli -> mor` (tutuyorsan), ardından `@onarim: f70e430d8b1e8336d5f6a9d7560df209242abb0b`, sonra gövde.

### Hikâye 10: tohum doru-0175 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0175
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'kereviz', fiil 'inanmak', sıfat 'sarı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: saklanırken annesinin kuyruğu çalının dallarına takıldı | dalları dişleriyle kenara çekip kuyruğu kurtardı
@tohum: doru-0175
@degisim: kereviz -> çalı
Ormanda Doru ile annesi sarı yaprakların arasında saklambaç oynuyordu. Annesi büyük bir çalının arkasına saklandı ama kuyruğu dışarıda kaldı. Sonra kuyruğu çalının dallarına takıldı. Doru kuyruğu hemen gördü ve güldü. "Seni buldum, anne!" dedi Doru. Annesi önce Doru'ya inanmadı, sonra kuyruğunu gördü ve güldü. Annesi çıkmak istedi ama kuyruğunu dallardan kurtaramadı. "Doru, bana yardım eder misin?" diye sordu annesi. Doru dalları dişleriyle tek tek kenara çekti. Kuyruk kurtuldu ve annesi çalıdan çıktı. İkisi birbirine bakıp yine güldü. Doru çok mutluydu, çünkü annesinin kuyruğunu kurtarmıştı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "sonra kuyruğunu gördü ve güldü"
   - Cümle 6: «Annesi önce Doru'ya inanmadı, sonra kuyruğunu gördü ve güldü.»
   - Açıklama: 'Kuyruğu gördü ve güldü' kalıbı art arda cümlelerde tekrarlanıyor ve 'güldü' üç kez yineleniyor.
   - Açıklama: 'Kuyruğu gördü ve güldü' kalıbı 4. cümlenin tekrarı, 'güldü' de üç kez yineleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi önce Doru'ya inanmadı"
   - Cümle 6: «Annesi önce Doru'ya inanmadı, sonra kuyruğunu gördü ve güldü.»
   - Açıklama: Annenin bulunduğuna inanmaması sebepsiz ve olayda işlevi olmayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0175` birebir aynı, `@degisim: kereviz -> çalı` (tutuyorsan), ardından `@onarim: fc7f7b6c42d0e193d8ac285f04d755d19dcfee12`, sonra gövde.

### Hikâye 11: tohum doru-0177 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | park | -
@tohum: doru-0177
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'leke', fiil 'yardımlaşmak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | -
@plan: zıplarken az koştu ve su dolu çukura indi | korkmadan daha uzun koşup çukurun üstünden atladı
@tohum: doru-0177
@degisim: yardımlaşmak -> zıplamak
Doru parkta yaprakların üstünden zıplama oyunu oynuyordu. Yırtık, sarı bir yaprak da suyla dolu bir çukurda yüzüyordu. Doru az koşup zıpladı ve suyun tam ortasına indi. Çamurlu su her yere sıçradı. Doru'nun bacakları kahverengi lekelerle doldu. Doru bacaklarına baktı ve güldü. Islanmaktan hiç korkmadı. Cesaretle biraz geri gitti ve bu kez daha uzun koştu. Sonra çok yüksek zıpladı ve çukurun üstünden geçti. Doru lekeli bacaklarıyla parkta mutlu mutlu zıplamaya devam etti.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "zıplarken az koştu ve"
   - Cümle 0 (plan satırı): «zıplarken az koştu ve su dolu çukura indi | korkmadan daha uzun koşup çukurun üstünden atladı»
   - Açıklama: Koşma zıplamadan önce olur; 'zıplarken az koştu' anlamca yanlış kurulmuş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "zıplarken az koştu"
   - Cümle 0 (plan satırı): «zıplarken az koştu ve su dolu çukura indi | korkmadan daha uzun koşup çukurun üstünden atladı»
   - Açıklama: Zıplarken koşulmaz; 'zıplamadan önce kısa koştu' anlamı yanlış kelimelerle kurulmuş.
3. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Doru parkta yaprakların üstünden"
   - Cümle 1: «Doru parkta yaprakların üstünden zıplama oyunu oynuyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; hikaye yeri insan yapımı bir park olarak adlandırıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yırtık, sarı bir yaprak da suyla dolu bir çukurda yüzüyordu"
   - Cümle 2: «Yırtık, sarı bir yaprak da suyla dolu bir çukurda yüzüyordu.»
   - Açıklama: Çukurdaki yaprak özenle kuruluyor ama olayda hiçbir işe yaramıyor.
   - Açıklama: Çukurdaki sarı yaprak hedefmiş gibi kuruluyor ama sonra hiç kullanılmıyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Doru bacaklarına baktı ve güldü"
   - Cümle 6: «Doru bacaklarına baktı ve güldü.»
   - Açıklama: Doru çamura inince hiç üzülmüyor, bu yüzden sorun gerçek bir sorun gibi durmuyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çok yüksek zıpladı ve çukurun üstünden geçti"
   - Cümle 9: «Sonra çok yüksek zıpladı ve çukurun üstünden geçti.»
   - Açıklama: Su dolu çukurun üstünden yüksek zıplama çocuğun taklit edebileceği tehlikeli bir davranış ve güvenli kullanım satırının hızı düz yerde koşmayla sınırlamasına aykırı.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra çok yüksek zıpladı ve çukurun üstünden geçti"
   - Cümle 9: «Sonra çok yüksek zıpladı ve çukurun üstünden geçti.»
   - Açıklama: Çukurun üstünden atlamak önceden hedef olarak konmadığı için hikayenin hedefi belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0177` birebir aynı, `@degisim: yardımlaşmak -> zıplamak` (tutuyorsan), ardından `@onarim: 2d22e5be53220a4b080757f9aaf43a7c64dcb4fe`, sonra gövde.

### Hikâye 12: tohum doru-0179 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0179
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yeni bir şeyi denemek
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'köpük', fiil 'dökmek', sıfat 'somurtkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük at karı ilk kez gördü ve basmak istemedi | arkadaşı cesaretle kara basıp ona gösterdi
@tohum: doru-0179
@degisim: somurtkan -> sessiz
Dağda ilk kar yağmıştı ve her yer bembeyazdı. Doru ile Alaca karı ilk kez görüyordu. Alaca kenarda sessiz ve üzgün duruyordu. "Kar çok garip, ona basmak istemiyorum," dedi Alaca. Doru da karı hiç tanımıyordu ama korkmadı. Cesaretle karın üstüne ilk adımı attı. Kar ayaklarının altında köpük gibi yumuşaktı. Doru düz bir yerde bir tur koştu ve karda yuvarlandı. Sonra kalktı, başını salladı ve sırtındaki karı döktü. "Gel, Alaca, çok eğlenceli!" dedi Doru. Alaca yavaşça kara bastı ve birden güldü. Sonra o da Doru'nun yanında karda yuvarlandı. Doru bundan sonra Alaca bir şeyden korkunca ilk adımı hep kendisi atardı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Alaca kenarda sessiz ve üzgün duruyordu.»
   - Açıklama: İlk üç cümlede yalnız Alaca'nın üzgün durduğu söyleniyor; kara basmak istememe sorunu ancak 4. cümlede açıkça söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Kar çok garip, ona basmak istemiyorum"
   - Cümle 4: «"Kar çok garip, ona basmak istemiyorum," dedi Alaca.»
   - Açıklama: Alaca'nın kara basmak istememesi ilk üç cümlede değil ancak dördüncü cümlede açıkça söyleniyor.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "ilk adımı hep kendisi atardı"
   - Cümle 13: «Doru bundan sonra Alaca bir şeyden korkunca ilk adımı hep kendisi atardı.»
   - Açıklama: Anlatım -dı'lı geçmişten '-ardı' biçimine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0179` birebir aynı, `@degisim: somurtkan -> sessiz` (tutuyorsan), ardından `@onarim: c7c6a3b945dc4b77905deb88e82661975077b872`, sonra gövde.
