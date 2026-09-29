# Editör görevi (onarım): Doru, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0050 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0050
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: bir şey yapmak
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'şemsiye', fiil 'üflemek', sıfat 'nefis'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: en güzel otlar ağır bir dalın altında kalmıştı | dalı çekti ve arkadaşıyla birlikte yığını yaptı
@tohum: doru-0050
@degisim: şemsiye -> ot
Sürünün çimen yediği çayırda güneş parlıyordu. Doru ile Karatay öğle yemeği için büyük bir ot yığını yapıyordu. Ama en güzel otlar, ağaçtan düşen kuru bir dalın altında kalmıştı. Karatay dala baktı ve üzgün üzgün burnundan üfledi. Doru hemen arkadaşına yardım etmek istedi. Dalın bir ucunu dişleriyle tuttu ve çekti. Karatay da öbür ucunu tuttu. İkisi dalı birlikte kenara çekti. Sonra ikisi güzel otları kopardı ve yığına taşıdı. Yığın kocaman oldu ve nefis kokuyordu. Doru ile Karatay ot yığınının yanında mutlu mutlu yemek yedi.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sürünün çimen yediği çayırda"
   - Cümle 1: «Sürünün çimen yediği çayırda güneş parlıyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye sürünün çayırında geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda başlıyor ve bitiyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "öğle yemeği için büyük bir ot yığını"
   - Cümle 2: «Doru ile Karatay öğle yemeği için büyük bir ot yığını yapıyordu.»
   - Açıklama: Kimlik cümlesindeki özgür sürüde otlayan atlar öğle yemeği için ot yığını yapmaz; dizinin dünyasına yanlış bilgi ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0050` birebir aynı, `@degisim: şemsiye -> ot` (tutuyorsan), ardından `@onarim: 868391153ee569bba9aea60fdff5dc710783cd09`, sonra gövde.

### Hikâye 2: tohum doru-0053 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0053
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çan', fiil 'güzelleşmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | -
@plan: ağaçların arasından gelen ince sesi merak etti | cesaretle sese doğru yürüdü ve delikli dalı buldu
@tohum: doru-0053
@degisim: çan -> dal
Rüzgar ormanda esiyordu. Doru ağaçların yanında tatlı otları yiyordu. Birden ağaçların arasından ince bir ses geldi ve Doru çok merak etti. Belki küçük bir hayvan orada sıkışmıştı. Doru bir an durdu, sonra cesaretle sese doğru yürüdü. Ses, eğri bir ağacın kuru dalından geliyordu. Dalda küçük, yuvarlak bir delik vardı. Rüzgar deliğe girdikçe daldan ince bir ses çıkıyordu. Orada sıkışmış bir hayvan yoktu. Rüzgar biraz daha hızlı esince ses daha da güzelleşti. Doru ağacın yanındaki çimenlerde sesi dinleyerek mutlu mutlu otladı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ince bir ses geldi ve Doru çok merak etti"
   - Cümle 3: «Birden ağaçların arasından ince bir ses geldi ve Doru çok merak etti.»
   - Açıklama: Sorun yalnız bir merak; gerçek bir dert ya da çocuğun önemseyeceği bir kayıp yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0053` birebir aynı, `@degisim: çan -> dal` (tutuyorsan), ardından `@onarim: 9ab7920cc25f45853ba582767dc4703be35f6109`, sonra gövde.

### Hikâye 3: tohum doru-0054 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0054
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: kaybolan eşya
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'portakal', fiil 'eklemek', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: kaya yokuşun başındaydı ve elmaların çoğu aşağı yuvarlandı | cesaretle karanlık çalının arkasına geçti ve elmaları buldu
@tohum: doru-0054
@degisim: portakal -> elma
Doru, Kırat ile dağda yürüyordu. Kırat sürü için büyük bir kayanın dibine elma toplamıştı. Ama kaya bir yokuşun başındaydı ve elmaların çoğu aşağı yuvarlanmıştı. "Elmalarım kayboldu, Doru," dedi Kırat. Doru yere baktı. Çimenin üstünde dağınık birkaç elma vardı. Doru bu elmaların gittiği yoldan yavaşça yürüdü. Yokuşun dibinde büyük bir çalı vardı. Çalının arkası çok karanlıktı. Doru bir an durdu. Sonra cesaretle çalının arkasına geçti. Kaybolan elmalar orada yerde duruyordu. Doru elmaları ağzıyla tek tek taşıdı ve kayanın dibindeki elmalara ekledi. "Teşekkürler, Doru, sürü bu elmalara çok sevinecek!" dedi Kırat.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Çalının arkası çok karanlıktı"
   - Cümle 9: «Çalının arkası çok karanlıktı.»
   - Açıklama: Karanlık çalının arkasına girmek küçük çocuk için korkutucu bir öğe.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kayanın dibindeki elmalara ekledi"
   - Cümle 13: «Doru elmaları ağzıyla tek tek taşıdı ve kayanın dibindeki elmalara ekledi.»
   - Açıklama: Elmalar yine yokuş başındaki kayaya konuyor; yuvarlanma sebebi giderilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0054` birebir aynı, `@degisim: portakal -> elma` (tutuyorsan), ardından `@onarim: 69b5d5ab9cb384f1edf5db4edabbaa3fca5ea7ab`, sonra gövde.

### Hikâye 4: tohum doru-0059 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Kırat
@tohum: doru-0059
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'külah', fiil 'tamamlanmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Kırat
@plan: turuncu çiçekler uzaktaydı ve arkadaşı birazdan uyanacaktı | hızla koşup çiçekleri getirdi ve arkadaşının çevresine dizdi
@tohum: doru-0059
@degisim: külah -> çiçek
Dağdaki düz bir yerde Kırat bir kayanın yanında uyuyordu. Doru, Kırat'ın en sevdiği turuncu çiçeklerle ona bir sürpriz yapmak istedi. Ama çiçekler uzaktaydı ve güneş kayaya gelince Kırat uyanacaktı. Doru düz vadide hızla koştu. Çiçeklerin yanına geldi ve ağzıyla bir demet çiçek kopardı. Sonra çiçekleri ağzında taşıyarak geri döndü. Çiçekleri Kırat'ın çevresine tek tek dizdi. Sonunda turuncu çiçeklerden bir halka tamamlandı. Tam o anda güneş kayaya geldi ve Kırat gözlerini açtı. "Sürpriz, Kırat!" dedi Doru. Kırat çiçeklere baktı ve güldü. "Çiçekler çok güzel, teşekkür ederim, Doru!" dedi Kırat.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "arkadaşı birazdan uyanacaktı"
   - Cümle 0 (plan satırı): «turuncu çiçekler uzaktaydı ve arkadaşı birazdan uyanacaktı | hızla koşup çiçekleri getirdi ve arkadaşının çevresine dizdi»
   - Açıklama: Kartın yanlar alanında Kırat sürünün en yaşlı, danışılan üyesidir; arkadaş olarak geçmesi ilişkiye uymuyor.
   - Açıklama: Kartta Kırat sürünün en yaşlı ve bilge üyesi; arkadaş ilişkisi kartın ilişki alanına uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0059` birebir aynı, `@degisim: külah -> çiçek` (tutuyorsan), ardından `@onarim: a9b3bdc50d074c4d59d6845f72da03ac9cd66410`, sonra gövde.

### Hikâye 5: tohum doru-0063 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0063
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'çimen', fiil 'güzelleştirmek', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: dikenli tohumlar sırtına yapıştı ve düşmedi | annesinden tohumları almasını istedi
@tohum: doru-0063
Dağda yumuşak çimenler vardı ve aralarında benekli çiçekler açmıştı. Doru çimene yattı ve sağa sola yuvarlandı. Ama kuru, dikenli tohumlar sırtına yapıştı. Doru kendini salladı ama tohumlar düşmedi. Ağzı da sırtına yetişmedi. Doru biraz utandı ama cesaretle annesine gitti. Annesinden sırtındaki tohumları almasını istedi. Annesi tohumları dişleriyle tek tek aldı. Sonunda son tohum da yere düştü. Sonra annesi Doru'nun tüylerini burnuyla düzeltti ve güzelleştirdi. Doru ile annesi benekli çiçeklerin yanında mutlu mutlu otladı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "tüylerini burnuyla düzeltti ve güzelleştirdi"
   - Cümle 10: «Sonra annesi Doru'nun tüylerini burnuyla düzeltti ve güzelleştirdi.»
   - Açıklama: 'Düzeltti ve güzelleştirdi' aynı işi gereksizce tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0063` birebir aynı, ardından `@onarim: 219570473803cbdd228b06d0b9d7bce2d839c0fd`, sonra gövde.

### Hikâye 6: tohum doru-0065 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0065
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'zeytin', fiil 'sokulmak', sıfat 'nazik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşı zeytin ağacını tanımadığı için yanlış ağaca koştu | zeytin ağacının yapraklarını anlatıp ona yardım etti
@tohum: doru-0065
Doru ile Alaca, sürünün çimen yediği çayırda koşu oyunu oynuyordu. Sırayla zeytin ağacına koşup ona dokunuyorlardı. Sıra Alaca'ya gelince o yanlış ağaca koştu, çünkü zeytin ağacını tanımıyordu. Alaca geri döndü ve üzgün üzgün başını eğdi. Doru, Alaca'ya yardım etmek istedi. "Zeytin ağacının küçük, gri yaprakları var, Alaca," dedi Doru nazik bir sesle. Alaca çayıra dikkatle baktı ve o ağacı buldu. Bu kez doğru ağaca gitti ve ona dokundu. Sonra sevinçle geri geldi ve Doru'ya sokuldu. "Seninle oynamak çok güzel, Doru!" dedi Alaca.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "sürünün çimen yediği çayırda koşu oyunu oynuyordu"
   - Cümle 1: «Doru ile Alaca, sürünün çimen yediği çayırda koşu oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer park ama hikaye sürünün otladığı bir çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye bir çayırda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0065` birebir aynı, ardından `@onarim: 44f0c8c9eb30a5846777228bef8f01b1818d1778`, sonra gövde.

### Hikâye 7: tohum doru-0070 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0070
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'gölge', fiil 'anlatmak', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: yağmur başladı ve yakında hiç ağaç yoktu | cesaretle yağmurda yürüyüp büyük kayanın altına girdi
@tohum: doru-0070
@degisim: anlatmak -> saklanmak
Dağda güneş vardı ve Doru tek başına çimen yiyordu. Birden Doru'nun gölgesi kayboldu, çünkü bulutlar gelmişti. Sonra yağmur başladı ve Doru'nun sırtı ıslandı. Yakında hiç ağaç yoktu, yalnız eskimiş kısa bir kütük vardı. Biraz ileride büyük bir kaya vardı. Yağmur çok yağıyordu ama Doru cesaretle kayaya kadar yürüdü. Kayanın bir yanı çatı gibi öne çıkmıştı ve altı kuruydu. Doru oraya girdi ve hiç ıslanmadı. Bir süre sonra bulutlar gitti ve güneş çıktı. Doru oradan çıktı ve yeniden çimen yemeye başladı. Doru bundan sonra yağmur başlayınca o kayanın altına saklandı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yalnız eskimiş kısa bir kütük"
   - Cümle 4: «Yakında hiç ağaç yoktu, yalnız eskimiş kısa bir kütük vardı.»
   - Açıklama: 'Eskimiş' eşyalar için kullanılır, ağaç kütüğüne uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yalnız eskimiş kısa bir kütük vardı"
   - Cümle 4: «Yakında hiç ağaç yoktu, yalnız eskimiş kısa bir kütük vardı.»
   - Açıklama: Kütük işe yarayacakmış gibi kuruluyor ama olayda hiç kullanılmıyor.
   - Açıklama: Kütük işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0070` birebir aynı, `@degisim: anlatmak -> saklanmak` (tutuyorsan), ardından `@onarim: 7996a1a9f2a21d4bba6afeade3abfeee526166cb`, sonra gövde.

### Hikâye 8: tohum doru-0072 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0072
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'taş', fiil 'sıkılmak', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: çalıların arkasından garip bir ses geldi | cesaretle geçip taşa damlayan suyu buldu
@tohum: doru-0072
Garip bir ses geliyordu: tık, tık. Doru ormanda tek başına sıkılmıştı ve bu sesi hemen duydu. Ses büyük çalıların arkasından geliyordu ve Doru onu çok merak etti. Doru oraya daha önce hiç gitmemişti. Ama Doru cesaretle çalıların arasından geçti. Arkada büyük, düz bir taş vardı. Yukarıdaki kayalardan ince bir su iniyordu. Her damla taşa düşünce tık diye ses çıkarıyordu. Doru suyun altında oynadı ve az sonra sırılsıklam oldu. Serin su Doru'yu çok güldürdü. Doru çok sevindi, çünkü o garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Garip bir ses geliyordu"
   - Cümle 1: «Garip bir ses geliyordu: tık, tık.»
   - Açıklama: Sorun yalnız bir merak; ortada çocuğun önemseyeceği bir kayıp ya da engel yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ama Doru cesaretle çalıların arasından geçti"
   - Cümle 5: «Ama Doru cesaretle çalıların arasından geçti.»
   - Açıklama: Hiç gitmediği bir yere tek başına garip bir sesin peşinden gitmek çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Tek başına daha önce gitmediği yere garip bir sesin peşinden gitmek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0072` birebir aynı, ardından `@onarim: 4e8e984471d577d26585ecabe158e1892ef2e55c`, sonra gövde.

### Hikâye 9: tohum doru-0073 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0073
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'ceviz', fiil 'keşfetmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: ceviz yuvarlandı ve içi boş bir kütüğe girdi | cesaretle kütüğün öbür ucundan bakıp cevizi çıkardı
@tohum: doru-0073
@degisim: keşfetmek -> bulmak
Bir sabah Doru ile Kırat, parktaki ceviz ağacının altında oynuyordu. Kırat bir cevizi saklıyor, Doru da onu buluyordu. Ama bu kez ceviz yuvarlandı ve içi boş bir kütüğe girdi. Kütüğün içi karanlıktı ve hiçbir şey görünmüyordu. "Ceviz içeride kaldı, Doru," dedi Kırat. Doru biraz çekindi ama sonra cesaretle kütüğün öbür ucuna gitti. Oradan içeri baktı ve cevizi gördü. Ceviz bu tarafa çok yakındı. Doru ağzıyla onu tuttu ve dışarı çıkardı. "Aferin, Doru, cevizi yine buldun!" dedi Kırat. Kırat bu kez cevizi çizgili bir taşın arkasına sakladı. Doru onu hemen buldu ve ikisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "parktaki ceviz ağacının altında"
   - Cümle 1: «Bir sabah Doru ile Kırat, parktaki ceviz ağacının altında oynuyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; metin insan parkını çağrıştıran 'park' kelimesini kullanıyor.
   - Açıklama: Kartın park tarifi sürünün çimen yediği çayır; dizide park yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Doru biraz çekindi"
   - Cümle 6: «Doru biraz çekindi ama sonra cesaretle kütüğün öbür ucuna gitti.»
   - Açıklama: 'Çekinmek' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0073` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: f01b6760214be0d0d84a6d097b3eaf9a4bb718b6`, sonra gövde.

### Hikâye 10: tohum doru-0074 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0074
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: sırayla oynamak
- yan: Alaca
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'küp', fiil 'selamlamak', sıfat 'uslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: küçük arkadaşı çok sessiz konuşunca ses geri gelmedi | cesaretle onunla birlikte yüksek sesle bağırdı
@tohum: doru-0074
@degisim: küp -> kaya
Dağda Doru ile Alaca bir ses oyunu oynuyordu. Sırayla kayaya "Merhaba!" diye bağırıyor, ses geri geliyordu. Sıra Alaca'ya gelince o çok sessiz konuştu ve ses gelmedi. Alaca başını eğdi ve üzüldü. "Gel, birlikte bağıralım, Alaca," dedi Doru. Doru ile Alaca cesaretle ve yüksek sesle kayayı selamladı. Ses hemen kayadan döndü ve ikisi güldü. "Şimdi sen dene, Alaca," dedi Doru. Alaca yüksek sesle bağırdı. Bu kez onun sesi de döndü. Sonra Alaca uslu durdu ve Doru'nun sırasını bekledi. "Sıra sende, Doru, bu oyun çok güzel!" dedi Alaca.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o çok sessiz konuştu"
   - Cümle 3: «Sıra Alaca'ya gelince o çok sessiz konuştu ve ses gelmedi.»
   - Açıklama: 'Sessiz' ses çıkarmamak demek; 'alçak sesle konuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0074` birebir aynı, `@degisim: küp -> kaya` (tutuyorsan), ardından `@onarim: 7fb9f3b6e28a6ff9336a6c07bac582e4bde33177`, sonra gövde.

### Hikâye 11: tohum doru-0076 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | -
@tohum: doru-0076
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'salıncak', fiil 'tartmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | -
@plan: dallar kelebekleri kapatıyordu ve kelebekler uzaklaşıyordu | yeni yolda hızla koşup ormanın kenarına vardı
@tohum: doru-0076
@degisim: tartmak -> denemek
Doru ormanda çiçeklerle süslü, uzun ve düz bir yol buldu. Ağaçların arasından vadide uçan renkli kelebekler gördü. Ama dallar rüzgarda salıncak gibi sallanıyor ve kelebekleri kapatıyordu. Kelebekler de yavaş yavaş uzaklaşıyordu. Yolun sonu ormanın kenarına çıkıyordu. Doru bu yolda daha önce hiç koşmamıştı ama denemek istedi. Açık ve düz yolda hızla koştu. Kısa sürede ormanın kenarına vardı. Orada önünde hiç dal yoktu. Doru bütün kelebekleri açıkça gördü. Az sonra kelebekler uçup gitti. Doru çok sevindi, çünkü ilk kez bu yolda koşmuş ve kelebekleri görmüştü.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sallanıyor ve kelebekleri kapatıyordu"
   - Cümle 3: «Ama dallar rüzgarda salıncak gibi sallanıyor ve kelebekleri kapatıyordu.»
   - Açıklama: Dallar kelebekleri kapatmaz; görüşü kapatıyordu denmeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "rüzgarda salıncak gibi sallanıyor"
   - Cümle 3: «Ama dallar rüzgarda salıncak gibi sallanıyor ve kelebekleri kapatıyordu.»
   - Açıklama: Dalların salıncağa benzetilmesi mecazdır.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "dallar rüzgarda salıncak gibi"
   - Cümle 3: «Ama dallar rüzgarda salıncak gibi sallanıyor ve kelebekleri kapatıyordu.»
   - Açıklama: Salıncak kartın doğa dünyasında olmayan bir insan eşyası.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Doru bu yolda daha önce hiç koşmamıştı ama denemek istedi"
   - Cümle 6: «Doru bu yolda daha önce hiç koşmamıştı ama denemek istedi.»
   - Açıklama: Kelebekleri görme sorununa yeni yolda ilk kez koşma hedefi karışıyor ve son bu ikinci hedefe dönüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0076` birebir aynı, `@degisim: tartmak -> denemek` (tutuyorsan), ardından `@onarim: 1e980672791a949207852afea5d6dcfb3353c0a1`, sonra gövde.

### Hikâye 12: tohum doru-0081 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0081
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'oyuncak', fiil 'tatmak', sıfat 'düzenli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yakındaki çalıda yalnız üç çilek vardı | açıklığa hızla koştu ve çilekli bir dal getirdi
@tohum: doru-0081
@degisim: oyuncak -> çilek
Bir sabah Kırat ormanda bir ağacın altında uyuyordu. Doru onu sevindirmek için çilek toplamak istedi. Ama yakındaki çalıda yalnız üç çilek vardı ve bu çok azdı. Çok çilek ise ormanın öbür ucundaki açıklıktaydı. Doru düz yolda hızla koştu ve oraya çabucak vardı. Çilekli bir dalı ağzıyla kopardı ve geri döndü. Çilekleri düz bir taşın üstüne düzenli bir sırayla dizdi. Kırat gözlerini açtı ve taşa baktı. "Bunlar benim için mi, Doru?" diye sordu Kırat. "Hepsi senin için!" dedi Doru. Kırat bir çilek tattı ve gülümsedi. "Çok tatlı, teşekkürler, Doru," dedi Kırat. Doru bundan sonra sevdiklerine sık sık küçük sürprizler hazırladı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çilekli bir dal getirdi"
   - Cümle 0 (plan satırı): «yakındaki çalıda yalnız üç çilek vardı | açıklığa hızla koştu ve çilekli bir dal getirdi»
   - Açıklama: Gövdede çilekli bir dal hiç geçmiyor; Doru dal getirmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0081` birebir aynı, `@degisim: oyuncak -> çilek` (tutuyorsan), ardından `@onarim: 7356245ac8b70f790fede15f23b6afcfacc96adc`, sonra gövde.
