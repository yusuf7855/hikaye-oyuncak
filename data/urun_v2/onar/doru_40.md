# Editör görevi (onarım): Doru, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum doru-0123 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0123
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: paylaşmak
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'uçurtma', fiil 'güvenmek', sıfat 'konuşkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: küçük arkadaşının önündeki çimenler çok kısaydı | önündeki iki elmayı onunla paylaştı
@tohum: doru-0123
@degisim: uçurtma -> elma
Parkta Doru ile Alaca yeşil çimen yiyordu. Ama Alaca'nın önündeki çimenler çok kısaydı ve Alaca doyamadı. Doru'nun önünde ise ağaçtan düşmüş iki kırmızı elma vardı. "Gel, Alaca, bu elmaları paylaşalım," dedi Doru. Doru hemen Alaca'ya yardım etti ve bir elmayı ona doğru itti. Alaca elmayı görünce çok konuşkan oldu. "Elma nedir? Acı mı? Sert mi?" diye sordu Alaca. "Elma tatlıdır, ben de çok yedim," dedi Doru. Alaca Doru'ya güvendi ve elmayı ısırdı. İki arkadaş elmalarını yan yana, sevinçle yedi. "Teşekkürler, Doru, elma çok güzelmiş!" dedi Alaca.
```

**Hakem bulguları (5):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Parkta Doru ile Alaca"
   - Cümle 1: «Parkta Doru ile Alaca yeşil çimen yiyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği geniş bir çayırdır; hikaye yeri çayır değil park olarak adlandırıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çok konuşkan oldu"
   - Cümle 6: «Alaca elmayı görünce çok konuşkan oldu.»
   - Açıklama: 'Konuşkan' kalıcı bir özelliktir; anlık durumu anlatmak için 'oldu' ile kullanımı uygun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elmayı görünce çok konuşkan oldu"
   - Cümle 6: «Alaca elmayı görünce çok konuşkan oldu.»
   - Açıklama: 'Konuşkan' kalıcı bir özellik; bir anlık durum için 'oldu' ile kullanımı yanlış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Alaca elmayı görünce çok konuşkan oldu"
   - Cümle 6: «Alaca elmayı görünce çok konuşkan oldu.»
   - Açıklama: Alaca'nın birden konuşkan olması ve elmayı sorgulaması sebepsiz beliren, çözüme katkısı olmayan bir ayrıntı.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Alaca Doru'ya güvendi"
   - Cümle 11: «Alaca Doru'ya güvendi ve elmayı ısırdı.»
   - Açıklama: 'Güvenmek' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0123` birebir aynı, `@degisim: uçurtma -> elma` (tutuyorsan), ardından `@onarim: d211efe56e7befeccf9d47d60d2c1814a4d740a3`, sonra gövde.

### Hikâye 2: tohum doru-0124 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0124
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'avokado', fiil 'koklamak', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yüksekteki elmalara uzanamadı | yardım istedi ve alçak bir dal buldu
@tohum: doru-0124
@degisim: avokado -> elma
Ormanda ağaçların arasından tatlı bir koku geliyordu. Doru havayı kokladı ve bir elma ağacı buldu. Ama kırmızı elmalar çok yüksekteydi ve Doru onlara uzanamadı. Kırat yakında, kahverengi bir kütüğün yanında dinleniyordu. "Kırat, elmalar çok yüksek, onlara nasıl ulaşırım?" diye sordu Doru. "Dar yoldan geç, orada alçak bir dal var," dedi Kırat. Doru cesaretle o yoldan yürüdü. Gerçekten de alçak bir dalda elmalar vardı. Doru bir elmayı dişleriyle koparıp yedi. Sonra bir tane de Kırat'a getirdi. Doru çok mutlu oldu, çünkü Kırat'a sormuş ve elmalara ulaşmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Doru cesaretle o yoldan yürüdü"
   - Cümle 7: «Doru cesaretle o yoldan yürüdü.»
   - Açıklama: Tohumdaki cesaret özelliği sorunu çözmüyor; çözümü Kırat'ın tavsiyesi getiriyor, cesaret işe yarar biçimde kullanılmamış.
   - Açıklama: Tohumdaki cesaret özelliği sorunu çözmüyor; çözüm yardım istemekle geliyor ve cesaret işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0124` birebir aynı, `@degisim: avokado -> elma` (tutuyorsan), ardından `@onarim: 1769cf256e0f204f1ba69987771c9afd62d9a80b`, sonra gövde.

### Hikâye 3: tohum doru-0126 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0126
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çuval', fiil 'tanışmak', sıfat 'pembe'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: koşarken saymayı hep unutuyordu | küçük arkadaşından saymasını istedi
@tohum: doru-0126
@degisim: çuval -> çiçek
Doru dağda, saymayla yeni tanışan küçük Alaca ile oynuyordu. Doru uzaktaki pembe çiçeklere koşup hemen geri dönmek istiyordu. Ama koşarken saymayı hep unutuyordu ve ne kadar çabuk döndüğünü bilemiyordu. Doru biraz düşündü. "Alaca, ben koşarken sen sayar mısın?" diye sordu Doru. "Tabii, Doru!" dedi Alaca ve saymaya başladı. Doru hemen dağın düz ve açık yerinde hızla koştu. Pembe çiçeklere dokundu ve geri döndü. Alaca sekiz derken Doru onun yanına gelmişti. Doru sevinçle Alaca'ya teşekkür etti. Doru bundan sonra koşarken saymak için hep Alaca'dan yardım istedi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "saymayla yeni tanışan küçük"
   - Cümle 1: «Doru dağda, saymayla yeni tanışan küçük Alaca ile oynuyordu.»
   - Açıklama: Saymayla tanışmak mecazlı bir anlatım; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "saymayla yeni tanışan küçük Alaca"
   - Cümle 1: «Doru dağda, saymayla yeni tanışan küçük Alaca ile oynuyordu.»
   - Açıklama: 'Saymayla tanışmak' mecazlı bir anlatım, küçük çocuğa uygun değil.
3. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "hep Alaca'dan yardım istedi"
   - Cümle 11: «Doru bundan sonra koşarken saymak için hep Alaca'dan yardım istedi.»
   - Açıklama: Kartın ilişki alanında Alaca Doru'dan öğrenir ve ona yardım edilir; hikaye ilişkiyi tersine çevirip Doru'yu kalıcı olarak Alaca'ya bağımlı gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0126` birebir aynı, `@degisim: çuval -> çiçek` (tutuyorsan), ardından `@onarim: 670fa8e567111190bee9575cbc334f23faeacd20`, sonra gövde.

### Hikâye 4: tohum doru-0128 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0128
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'düğüm', fiil 'yazmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesini dinlemedi ve annesinin kuyruğu dallara takıldı | özür diledi ve düğümü dişleriyle açtı
@tohum: doru-0128
@degisim: yazmak -> çekmek
Doru annesini dinlemedi ve dağda sık çalıların arasına koştu. Annesi arkasından geldi ve uzun kuyruğu dallara takıldı. Kuyruğunda küçük bir düğüm oldu. Doru geri döndü ve annesine baktı. "Özür dilerim, anneciğim, seni dinlemeliydim," dedi Doru. "Tamam, Doru, önce bu düğümü çözelim," dedi annesi. Doru yardım etmek için dişleriyle dalları tek tek çekti. Sonra düğümü de yavaşça açtı. "Yeterli, Doru, kuyruğum kurtuldu," dedi annesi. Annesi Doru'yu burnuyla okşadı. "Bundan sonra seni hep dinleyeceğim, anneciğim," dedi Doru.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yeterli, Doru, kuyruğum kurtuldu"
   - Cümle 9: «"Yeterli, Doru, kuyruğum kurtuldu," dedi annesi.»
   - Açıklama: 'Yeterli' bu replikte yanlış anlamda kullanılmış; 'Tamam' ya da 'Yeter' olmalı.
   - Açıklama: 'Yeterli' bu bağlamda yanlış kelime; 'Tamam' ya da 'Oldu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0128` birebir aynı, `@degisim: yazmak -> çekmek` (tutuyorsan), ardından `@onarim: 179c77c66e24eaeb878b91d04b7bdb55cd69b4c5`, sonra gövde.

### Hikâye 5: tohum doru-0129 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0129
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bitki', fiil 'boşaltmak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşı acıkmıştı ama sevdiği bitki burada yoktu | vadide hızla koşup bitkileri getirdi
@tohum: doru-0129
@degisim: sabırlı -> tatlı
Rüzgar dağda serin serin esiyordu. Doru ile Karatay bir ağacın altında dinleniyordu. Karatay acıkmıştı, ama sevdiği tatlı bitki burada hiç yoktu. O bitki yalnız yakındaki vadide büyüyordu. Karatay çok yorgundu ve biraz sonra uyudu. Doru ona bir sürpriz hazırlamak istedi. Doru vadinin düz yerinde hızla koştu. Orada tatlı bitkileri buldu ve ağzına doldurdu. Sonra aynı yoldan geri döndü. Bitkileri Karatay'ın yanındaki büyük bir taşa boşalttı. Karatay uyandı ve taşın üstündeki bitkileri gördü. Sevinçle zıpladı ve bitkilerin hepsini yedi. Doru bundan sonra acıkan arkadaşlarını böyle sürprizlerle sevindirdi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yalnız yakındaki vadide büyüyordu"
   - Cümle 4: «O bitki yalnız yakındaki vadide büyüyordu.»
   - Açıklama: 'Vadi' 3 yaşındaki bir çocuğun bilmeyeceği bir kelimedir.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru vadinin düz yerinde hızla koştu"
   - Cümle 7: «Doru vadinin düz yerinde hızla koştu.»
   - Açıklama: Hikaye dağda başlıyor ama olay vadiye taşınıyor; tek sahne kuralı çiğneniyor.
   - Açıklama: Hikaye dağda ağacın altında başlıyor ama olay vadiye taşınıyor; tek sahne kuralı zorlanıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "acıkan arkadaşlarını böyle sürprizlerle sevindirdi"
   - Cümle 13: «Doru bundan sonra acıkan arkadaşlarını böyle sürprizlerle sevindirdi.»
   - Açıklama: Notlanan çoğul canlılar (arkadaşlar) arka planda kalmayıp olaya katılıyor; tek adlı yan Karatay sınırı aşılıyor.
   - Açıklama: Kodun notladığı çoğul canlı arkadaşlar son cümlede olaya dahil ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0129` birebir aynı, `@degisim: sabırlı -> tatlı` (tutuyorsan), ardından `@onarim: c9e8f1af9066aeb878c94ca4b18d938a7f9a1f09`, sonra gövde.

### Hikâye 6: tohum doru-0131 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0131
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çubuk', fiil 'gezdirmek', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yağmur yaklaşıyordu ve kuru yerin yolunu bilmiyordu | yardım istedi ve düz yoldan hızla koştu
@tohum: doru-0131
@degisim: gezdirmek -> göstermek
Doru ormanda Kırat'la birlikte yürüyordu. Birden gökte kara bulutlar toplandı ve yağmur yaklaştı. Doru kuru bir yere gitmek istedi ama yolu bilmiyordu. Kırat ormanı çok iyi tanıyordu. Doru ondan yolu göstermesini istedi. Kırat, kırık çubuklarla dolu yolu değil, yanındaki düz yolu gösterdi. Doru o düz yolda hızla koştu. Yağmur başlamadan büyük bir kayanın altına ulaştı. Kırat da yavaş ve temkinli adımlarla arkasından geldi. Sonra yağmur başladı ama ikisi de kuru kaldı. Doru ile Kırat, kayanın altında yağmuru mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "temkinli adımlarla arkasından"
   - Cümle 9: «Kırat da yavaş ve temkinli adımlarla arkasından geldi.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yavaş ve temkinli adımlarla"
   - Cümle 9: «Kırat da yavaş ve temkinli adımlarla arkasından geldi.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0131` birebir aynı, `@degisim: gezdirmek -> göstermek` (tutuyorsan), ardından `@onarim: e604b80695907e38a12c69b0bdea1d94e47d9bfb`, sonra gövde.

### Hikâye 7: tohum doru-0134 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Alaca
@tohum: doru-0134
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'örgü', fiil 'gitmek', sıfat 'uzak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Alaca
@plan: arkadaşı saklanırken oyun yerini göremedi | arkadaşının sesini duyup hızla koştu ve onu buldu
@tohum: doru-0134
@degisim: örgü -> ağaç
Ormanda Doru ile Alaca saklanma oyunu oynuyordu. Alaca saklanmak için uzak ağaçlara gitti. Oradan geri dönmek istedi ama oyun yerini göremedi. "Doru, neredesin?" diye seslendi Alaca. Doru bu sesi hemen duydu. Ağaçlara kadar düz çimende hızla koştu. Az sonra Alaca'yı büyük bir ağacın altında buldu. "Seni buldum, Alaca!" dedi Doru. "İyi ki geldin, Doru," dedi Alaca. "Benimle gel," dedi Doru. Alaca onun arkasından yürüdü ve oyun yerine döndüler. Sonra iki arkadaş oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ağaçlara kadar düz çimende hızla koştu"
   - Cümle 6: «Ağaçlara kadar düz çimende hızla koştu.»
   - Açıklama: Oyun ormanda geçerken ağaçlar uzakta ve arada düz çimen varmış gibi anlatılıyor, yer kendi içinde çelişiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Alaca onun arkasından yürüdü ve oyun yerine döndüler"
   - Cümle 11: «Alaca onun arkasından yürüdü ve oyun yerine döndüler.»
   - Açıklama: Özne tekil 'Alaca' iken ikinci yüklem çoğul 'döndüler'; uyum bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0134` birebir aynı, `@degisim: örgü -> ağaç` (tutuyorsan), ardından `@onarim: 96e4aa88f07fd43e41d48f1162d4175c1ba5a7a1`, sonra gövde.

### Hikâye 8: tohum doru-0138 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0138
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'nane', fiil 'küçülmek', sıfat 'iyi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesinin başı dar kayaların arasına sığmadı | naneleri dişleriyle çıkarıp annesiyle paylaştı
@tohum: doru-0138
Doru annesiyle dağda yürüyordu ve ikisi de acıkmıştı. Doru iki büyük kayanın arasında taze naneler gördü. Ama kayaların arası çok dardı ve annesinin başı oraya sığmadı. "Doru, keşke biraz küçülebilsem," dedi annesi. Doru gençti ve onun başı daha küçüktü. Doru hemen annesine yardım etmek istedi. Başını kayaların arasına soktu ve naneleri dişleriyle kopardı. Naneleri ikiye ayırdı ve yarısını annesinin önüne bıraktı. Annesi bir nane tattı ve gülümsedi. "Çok güzel kokuyorlar, teşekkürler, Doru," dedi annesi. İkisi naneleri yan yana yiyip bitirdi. Doru bundan sonra iyi bir şey görünce hep annesiyle paylaşırdı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Başını kayaların arasına soktu"
   - Cümle 7: «Başını kayaların arasına soktu ve naneleri dişleriyle kopardı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde başını dar bir aralığa sokma davranışı örnekleniyor.
   - Açıklama: Çocuğun taklit edip başını dar bir aralığa sokması sıkışma tehlikesi taşır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0138` birebir aynı, ardından `@onarim: abc8b78b345d0d8e02994b2075b169ee4e51c497`, sonra gövde.

### Hikâye 9: tohum doru-0141 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Alaca
@tohum: doru-0141
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Alaca
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'çember', fiil 'ilerlemek', sıfat 'meyveli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | park | Alaca
@plan: uzun otlar yüzünden küçük arkadaşı ağacı göremedi | ona hangi yöne gideceğini söyleyerek yardım etti
@tohum: doru-0141
Kuşlar ötüyordu ve parktaki geniş çayırda hafif bir rüzgar esiyordu. Doru ile Alaca bir oyun oynuyordu. Oyunda Alaca önden gidecek ve Doru'yu meyveli ağaca götürecekti. Ama uzun otlar yüzünden küçük Alaca ağacı göremedi. "Hangi yöne gideceğim?" diye sordu Alaca. Doru başını kaldırdı ve ağacı gördü. Doru hemen Alaca'ya yardım etti. "Sağa dön, Alaca, sonra hep düz ilerle," dedi Doru. Alaca sağa döndü ve otların arasında ilerledi. Sonunda elmalarla dolu dallar göründü. "Buldum, seni ben getirdim!" dedi Alaca. Alaca sevinçle ağacın çevresinde çember gibi döndü. Sonra ikisi gölgede elmaları mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "parktaki geniş çayırda"
   - Cümle 1: «Kuşlar ötüyordu ve parktaki geniş çayırda hafif bir rüzgar esiyordu.»
   - Açıklama: Kartın park tarifi sürünün çimen yediği bir çayırdır ve dizide park yoktur; metin yeri park olarak adlandırıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Oyunda Alaca önden gidecek ve Doru'yu meyveli ağaca götürecekti.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede yok.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Buldum, seni ben getirdim!"
   - Cümle 11: «"Buldum, seni ben getirdim!" dedi Alaca.»
   - Açıklama: Alaca yolu Doru'nun tarifiyle bulduğu halde kendisinin getirdiğini söylüyor.
   - Açıklama: Yolu Doru gösterdiği halde Alaca Doru'yu kendisinin getirdiğini söylüyor; oyunun kuralı ile olan olay çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0141` birebir aynı, ardından `@onarim: e1e32b2e94b7399cf0b2d5ea71788768c5456482`, sonra gövde.

### Hikâye 10: tohum doru-0145 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Kırat
@tohum: doru-0145
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kırat
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'meşe', fiil 'şakımak', sıfat 'çekingen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | park | Kırat
@plan: büyük atın kuyruğu bir ağacın ince dalına takıldı | dişleriyle dalı eğdi ve kuyruğu kurtardı
@tohum: doru-0145
@degisim: şakı- -> öt-
Parktaki geniş çayırda büyük bir meşe vardı ve dallarında kuşlar ötüyordu. Doru ağacın altında Kırat'ı gördü. Kırat'ın uzun kuyruğu ince bir dala takılmıştı. Dal tam arkasındaydı ve Kırat onu göremiyordu. Kırat kuyruğunu her çektiğinde, kuyruk dala daha çok dolanıyordu. "Doru, kuyruğum takıldı, çıkaramıyorum," dedi Kırat çekingen bir sesle. Doru hemen ona yardım etti ve yanına gitti. Dalı dişleriyle tuttu ve yavaşça eğdi. Sonra kuyruğu daldan dikkatle ayırdı. Kuyruk kurtuldu ve aşağı indi. Kırat sevinçle kuyruğunu salladı. "Teşekkürler, Doru, kuyruğum artık serbest!" dedi Kırat.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Kırat çekingen bir sesle"
   - Cümle 6: «"Doru, kuyruğum takıldı, çıkaramıyorum," dedi Kırat çekingen bir sesle.»
   - Açıklama: 'Çekingen' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Doru hemen ona yardım etti ve yanına gitti"
   - Cümle 7: «Doru hemen ona yardım etti ve yanına gitti.»
   - Açıklama: 'Yardım etti' sonraki eylemleri önceden özetliyor ve sıra ters; gereksiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0145` birebir aynı, `@degisim: şakı- -> öt-` (tutuyorsan), ardından `@onarim: c7ce066f6086797a211fb5182b66a492bb5618c5`, sonra gövde.

### Hikâye 11: tohum doru-0146 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | Karatay
@tohum: doru-0146
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: paylaşmak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'boncuk', fiil 'yoğurmak', sıfat 'yüksek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | Karatay
@plan: ağaçtaki son elma çimenlerde yuvarlandı ve uzaklaştı | hızla koşup elmayı durdurdu ve arkadaşıyla paylaştı
@tohum: doru-0146
@degisim: yoğur- -> yuvarlan-
Doru ile Karatay parktaki geniş çayırda bir elma ağacının altında duruyordu. Karatay yüksek bir dala uzandı ve son elmayı düşürdü. Ama elma çimenlerin üstünde yuvarlandı ve uzaklaştı. "Son elma gidiyor!" dedi Karatay. Doru hemen düz ve açık çayırda hızla koştu. Elmanın önüne geçti ve onu ayağıyla durdurdu. Sonra elmayı ağzıyla aldı ve ağacın altına getirdi. "Gel, Karatay, bu elmayı paylaşalım," dedi Doru. Doru elmayı ısırdı, ikiye böldü ve yarısını Karatay'a verdi. Karatay boncuk gibi siyah gözleriyle Doru'ya baktı ve güldü. Arkadaşlar yan yana durdu ve elmayı yedi. İkisi de çok mutluydu, çünkü son elmayı paylaşmışlardı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "elma çimenlerin üstünde yuvarlandı ve uzaklaştı"
   - Cümle 3: «Ama elma çimenlerin üstünde yuvarlandı ve uzaklaştı.»
   - Açıklama: Elmanın düz ve açık çayırda neden uzağa yuvarlandığı söylenmiyor ve sorun akla yatkın değil.
   - Açıklama: Elmanın düz ve açık çayırda neden yuvarlanıp uzaklaştığına dair akla yatkın bir sebep verilmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "boncuk gibi siyah gözleriyle"
   - Cümle 10: «Karatay boncuk gibi siyah gözleriyle Doru'ya baktı ve güldü.»
   - Açıklama: 'Boncuk gibi' benzetmesi mecazlı bir anlatım.
   - Açıklama: 'Boncuk gibi' benzetmesi mecazdır; küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0146` birebir aynı, `@degisim: yoğur- -> yuvarlan-` (tutuyorsan), ardından `@onarim: 8636656e90c42f800cf56891686f2d53d30400ed`, sonra gövde.

### Hikâye 12: tohum doru-0147 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | annesi
@tohum: doru-0147
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'fidan', fiil 'atlamak', sıfat 'hareketli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | annesi
@plan: ormanda tık tık diye bir ses geliyordu | sesi yapan kuru dalı bulup yere bıraktı
@tohum: doru-0147
Doru annesiyle ormanda yürüyordu. Birden yakından tık tık diye bir ses geldi. Doru sesi çok merak etti, ama bir şey göremedi. "Anneciğim, bu ses ne?" diye sordu Doru. "Bilmiyorum, Doru, gel birlikte bakalım," dedi annesi. Doru'nun hareketli kulakları sesin geldiği yöne döndü. İkisi o yöne yürüdü. Küçük bir fidanın hemen üstünde kuru bir dal sallanıyordu. Rüzgar esince dal fidana vuruyordu ve ses buradan geliyordu. Doru fidana yardım etti. Kuru dalı dişleriyle tuttu ve yere bıraktı. Ses hemen kesildi ve Doru yerinde neşeyle atladı. Doru çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru fidana yardım etti"
   - Cümle 10: «Doru fidana yardım etti.»
   - Açıklama: Kuru dalı indirmek fidana yardım sayılmaz; fiil burada anlamca uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0147` birebir aynı, ardından `@onarim: 081c96e321c18a870a7a56d032fc4b38242644ea`, sonra gövde.
