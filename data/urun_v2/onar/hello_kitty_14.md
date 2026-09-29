# Editör görevi (onarım): Hello Kitty, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hello Kitty | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar14.txt --ad urun_v2`
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

## Kart: Hello Kitty (kaynaklı, kapalı dünya)

- Ad: Hello Kitty (okunuş: helo kiti; kesme eki okunuşa uyar)
- Kimlik: Hello Kitty, ailesiyle birlikte bir evde yaşayan, kırmızı kurdeleli, beyaz ve iyi kalpli bir kedidir.
- Tür: kedi
- Güvenli özellik kullanımı: Kurabiye ve turta bir büyükle birlikte yapılır; fırını ve sıcak tepsiyi annesi ya da babası tutar. Kimse yabancıyla bir yere gitmez; kimse tek başına uzağa gitmez.
- Özellikler:
  - arkadaş: Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır. (örnek biçimler: arkadaş, arkadaşlar, arkadaşıyla)
  - kurabiye: Kurabiye yapmayı çok sever. (örnek biçimler: kurabiye, kurabiyeler, kurabiyeleri)
  - turta: En çok elmalı turtayı sever. (örnek biçimler: turta, turtayı, turtası)
- Yerler:
  - park: Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.
  - orman: Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.
  - ev: Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Mimi: Hello Kitty'nin ikiz kız kardeşi ve en iyi arkadaşı; utangaçtır ve sarı kurdele takar. Tür: kedi; konuşur. Yüzey biçimleri: Mimi, kardeş, kardeşi, ikiz, ikizi
  - annesi: Hello Kitty'nin annesi; çok iyi yemek yapar, elmalı turtası çok güzeldir. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
  - babası: Hello Kitty'nin babası; güvenilir ve komiktir, bazen bir şeyi unutur. Tür: baba; konuşur. Yüzey biçimleri: baba, babası, babacığım, Baba
- Dünya kuralları:
  - Hello Kitty, Mimi, annesi ve babası konuşur. Hikayede Hello Kitty'nin ağzından söz edilmez.
  - Mimi, Hello Kitty'nin ikiz kız kardeşidir; ablası ya da kuzeni değildir. Mimi sarı kurdele takar.
  - Hikaye evde, parkta ya da ormanda tek sahnede geçer; Londra'ya ya da başka bir şehre yolculuk yoktur.
  - Hello Kitty bir marka ya da satılan bir eşya olarak anılmaz; mağaza ve alışveriş yoktur.
- Yasak adlar: Dear Daniel, Daniel, Charmmy Kitty, Charmmy, Sugar, Ichigoman, Mimmy, Kitty White, George, Mary, Anthony, Margaret, Joey, Judy, Tippy, Thomas, Tracy, Rorry, My Melody
- Yasak: Marka, mağaza, alışveriş, uçak ya da trenle şehir yolculuğu ve zamanda yolculuk hikayeye girmez.
- İzinli dünya kelimeleri: kurdele, kurabiye, turta, piknik, kamp

## Onarılacak hikâyeler

### Hikâye 1: tohum hello_kitty-0013 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0013
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fırça', fiil 'yollamak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesinin fırçası çok kalındı | kendi incecik fırçasını annesine verdi
@tohum: hello_kitty-0013
@degisim: yollamak -> vermek
Hello Kitty ile annesi parkta düz taşları boyuyordu. Annesi taşına küçük bir kedi çizdi. Ama kalın fırçasıyla kedinin ince bıyıklarını yapamadı. "Bu fırça çok kalın," dedi annesi. Hello Kitty bu kedinin bıyıksız kalmasını istemedi. Hello Kitty fırçalarını arkadaşlarına da hep verirdi. Hemen kendi fırçalarına baktı. Hello Kitty'nin bir de incecik bir fırçası vardı. "Anne, bu fırçayı sana veriyorum!" dedi Hello Kitty. Annesi fırçayı aldı ve bıyıkları tek tek çizdi. Taşın üstündeki kedi artık çok tatlı görünüyordu. "Teşekkürler, kızım," dedi annesi. Hello Kitty çok mutlu oldu, çünkü fırçasını annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty fırçalarını arkadaşlarına da hep verirdi"
   - Cümle 6: «Hello Kitty fırçalarını arkadaşlarına da hep verirdi.»
   - Açıklama: Tohumdaki özellik yeni arkadaş edinmek; burada ilgisiz bir ek cümleyle fırça vermeye çevrilmiş ve çözüme katkısı yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty fırçalarını arkadaşlarına da hep verirdi"
   - Cümle 6: «Hello Kitty fırçalarını arkadaşlarına da hep verirdi.»
   - Açıklama: Sahnede olmayan arkadaşlara fırça verme bilgisi olayda işlevi olmayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0013` birebir aynı, `@degisim: yollamak -> vermek` (tutuyorsan), ardından `@onarim: 9cb0b887e1e868d34053a8e97f1e1057045a9e0d`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0014 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0014
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'karnabahar', fiil 'uzaklaşmak', sıfat 'sabunlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar esince köpük balonları küçükken uzaklaştı | kalın bir ağacın arkasına geçip çubuğu yavaşça salladı
@tohum: hello_kitty-0014
Bir sabah Hello Kitty parkta köpük balonu yapıyordu. Çubuğu sabunlu suya batırdı ve havada salladı. Ama rüzgar esince balonlar küçükken çubuktan koptu ve uzaklaştı. Hello Kitty arkadaşlarına göstermek için çok büyük bir balon yapmak istiyordu. Küçük balonlar çiçeklerin üstünde bir bir patladı. Hello Kitty etrafına baktı ve kalın bir ağaç gördü. Ağacın arkasına geçti, orada rüzgar yoktu. Bu kez çubuğu çok yavaş salladı. Çubuğun ucunda bir balon büyümeye başladı. Balon bir karnabahar kadar oldu! Hello Kitty çok sevindi, çünkü sonunda büyük bir balon yapmıştı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Hello Kitty parkta köpük balonu yapıyordu"
   - Cümle 1: «Bir sabah Hello Kitty parkta köpük balonu yapıyordu.»
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor; Hello Kitty parkta yanında büyük olmadan yalnız.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına göstermek için"
   - Cümle 4: «Hello Kitty arkadaşlarına göstermek için çok büyük bir balon yapmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçerken anılıyor; sorunu çözmede işe yaramıyor.
   - Açıklama: Karttaki arkadaş özelliği yalnız bir istek gerekçesi olarak anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "arkadaşlarına göstermek için çok büyük"
   - Cümle 4: «Hello Kitty arkadaşlarına göstermek için çok büyük bir balon yapmak istiyordu.»
   - Açıklama: Balonu arkadaşlarına gösterme amacı kuruluyor ama arkadaşlar hiç görünmüyor ve bu amaç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0014` birebir aynı, ardından `@onarim: 9f181a440be26c4596412df8e3b81186268c37ca`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0016 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0016
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mercan', fiil 'giydirmek', sıfat 'kirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babasının elleri kirliydi ve babası temiz kazağını giyemedi | babasının ellerine su döktü ve babası ellerini yıkadı
@tohum: hello_kitty-0016
@degisim: mercan -> kazak
Bir sabah ormandaki kamp yerinde serin bir rüzgar esti. Hello Kitty'nin babası kazağını giymek istedi. Ama çadırı kurarken elleri çok kirli olmuştu. "Temiz kazağı kirletmek istemiyorum," dedi babası. Hello Kitty kurabiye yapmayı çok severdi, yapmadan önce ellerini hep yıkardı. Bunu düşündü, hemen şişeyle su getirdi ve babasının ellerine döktü. Babası ellerini güzelce yıkadı, ama elleri ıslak kaldı. "Baba, kazağı sana ben giydireyim mi?" diye sordu Hello Kitty. "Evet, kızım, çok teşekkürler," dedi babası. Hello Kitty kazağı babasına dikkatlice giydirdi. Kazak tertemiz kaldı ve babası gülerek ona sarıldı. Hello Kitty bundan sonra kirli elleri görünce hemen su getirmeye başladı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kurabiye yapmayı çok severdi"
   - Cümle 5: «Hello Kitty kurabiye yapmayı çok severdi, yapmadan önce ellerini hep yıkardı.»
   - Açıklama: Kurabiye özelliği hikayede yapılmıyor, yalnız özellik olarak sayılıp geçiliyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bunu düşündü, hemen"
   - Cümle 6: «Bunu düşündü, hemen şişeyle su getirdi ve babasının ellerine döktü.»
   - Açıklama: 'Bunu' zamirinin neyi gösterdiği belli değil.
   - Açıklama: 'Bunu' zamirinin neyi gösterdiği tam belli değil.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "ama elleri ıslak kaldı"
   - Cümle 7: «Babası ellerini güzelce yıkadı, ama elleri ıslak kaldı.»
   - Açıklama: Kirli eller çözülünce ıslak eller diye ikinci bir sorun başlıyor.
   - Açıklama: El yıkama sorunu çözülünce ıslak eller ikinci bir sorun olarak ortaya çıkıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kazağı babasına dikkatlice giydirdi"
   - Cümle 10: «Hello Kitty kazağı babasına dikkatlice giydirdi.»
   - Açıklama: Çözüm su dökme ve yıkamayla bitmiyor, kazağı giydirme gibi ek adımlar gerekiyor.
   - Açıklama: Çözüm su dökme ve yıkamayla bitmiyor, kazağı giydirme gibi ek adımlara uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0016` birebir aynı, `@degisim: mercan -> kazak` (tutuyorsan), ardından `@onarim: 55c5b6769d38f901cb11f0c4062a4025b10e0a09`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0019
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'fener', fiil 'oturtmak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: çantanın kapağı açık kaldı ve kurabiye kutusu düştü | fenerle çadırın içine baktı ve kutuyu buldu
@tohum: hello_kitty-0019
@degisim: gizemli -> küçük
Ağaçlarda kuşlar ötüyordu. Hello Kitty ormandaki kamp yerinde, çadırın önündeydi. Çantasına baktı ama kurabiye kutusu yoktu. Çantanın kapağı açık kalmıştı ve kutu bir yere düşmüştü. Kutuda evde yaptığı yıldız kurabiyeleri vardı. Hello Kitty çantayı az önce çadırın içinde açmıştı. Çadırın içi biraz karanlıktı. Hello Kitty girişteki feneri açtı ve içeri tuttu. Işıkta köşedeki küçük kutuyu gördü. Bu, onun kurabiye kutusuydu! Hello Kitty feneri yere koydu ve kutuyu iki eliyle çıkardı. Kurabiyelerin hepsi kutuda yerindeydi. Hello Kitty bir kurabiye aldı ve kutunun kapağını yerine oturttu. Sonra çadırın önüne oturdu ve kurabiyesini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde, çadırın önündeydi.»
   - Açıklama: Kartın güvenli kullanım satırına aykırı olarak Hello Kitty ormanda bir büyük olmadan tek başına.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde, çadırın önündeydi"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde, çadırın önündeydi.»
   - Açıklama: Hello Kitty ormandaki kamp yerinde yalnız; güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söyler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0019` birebir aynı, `@degisim: gizemli -> küçük` (tutuyorsan), ardından `@onarim: 043b53446ca7d74501775b6aee6ab26519fcdfb2`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0021 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0021
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'boya', fiil 'değiştirmek', sıfat 'tuzlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: rüzgar kağıdı kaldırdı ve kağıt yüksek bir dala takıldı | annesinden yardım istedi ve annesi kağıdı daldan indirdi
@tohum: hello_kitty-0021
@degisim: değiştirmek -> tutmak
Rüzgar hızlı hızlı esiyordu. Hello Kitty parkta yeni arkadaşı için boyalarla resim yapıyordu. Birden rüzgar kağıdı havaya kaldırdı ve kağıt yüksek bir dala takıldı. Hello Kitty zıpladı ama dala uzanamadı. Annesi de yanında tuzlu kraker yiyordu. "Anne, kağıdı daldan alır mısın?" diye sordu Hello Kitty. "Hemen alırım," dedi annesi. Annesi uzandı ve kağıdı daldan dikkatlice indirdi. Hello Kitty kağıdı iki eliyle sıkıca tuttu. Sonra resmini bitirdi ve annesine gösterdi. "Anneciğim, teşekkürler, şimdi birlikte kraker yiyelim mi?" dedi Hello Kitty.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşı için boyalarla resim yapıyordu"
   - Cümle 2: «Hello Kitty parkta yeni arkadaşı için boyalarla resim yapıyordu.»
   - Açıklama: Karttaki arkadaş özelliği yalnız resmin gerekçesi olarak anılıyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "parkta yeni arkadaşı için boyalarla resim yapıyordu"
   - Cümle 2: «Hello Kitty parkta yeni arkadaşı için boyalarla resim yapıyordu.»
   - Açıklama: Resmin yapıldığı yeni arkadaş hiç görünmüyor ve olayda hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Annesi de yanında tuzlu kraker yiyordu"
   - Cümle 5: «Annesi de yanında tuzlu kraker yiyordu.»
   - Açıklama: Kraker sorunla ilgisiz bir ayrıntı olarak kuruluyor ve son cümle resim hedefinden krakere kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0021` birebir aynı, `@degisim: değiştirmek -> tutmak` (tutuyorsan), ardından `@onarim: db9d00f5e12f102a3f4ff920c2e0f027e3f0c1d3`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0022 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0022
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'cetvel', fiil 'denemek', sıfat 'özel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: tabakta iki kardeşe tek bir kurabiye kaldı | kurabiyeyi cetvelle tam ortadan ikiye böldü
@tohum: hello_kitty-0022
@degisim: denemek -> yemek
Evin mutfağında Hello Kitty ile Mimi masadaki tabağa baktı. Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı. İkisi de onu yemek istiyordu, ama tabakta başka kurabiye yoktu. Mimi utangaçtı ve hiçbir şey söylemedi. "Mimi, bu kurabiyeyi seninle paylaşmak istiyorum," dedi Hello Kitty. "İki parça aynı büyüklükte olur mu?" diye sordu Mimi. Hello Kitty kurabiye yaparken hamuru hep cetvelle keserdi. Çekmeceden bir cetvel aldı. Cetveli kurabiyenin tam ortasına koydu. Sonra kurabiyeyi cetvelin kenarından yavaşça ikiye kırdı. İki parça tam aynı boydaydı. Hello Kitty bir parçayı Mimi'ye verdi. İki kardeş yan yana oturdu ve parçalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi utangaçtı ve hiçbir"
   - Cümle 4: «Mimi utangaçtı ve hiçbir şey söylemedi.»
   - Açıklama: 'Utangaç' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0022` birebir aynı, `@degisim: denemek -> yemek` (tutuyorsan), ardından `@onarim: 2dadc4ecc962ccf328366214d5697bfbbdec5c7d`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0024 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0024
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yeni bir şeyi denemek
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'böğürtlen', fiil 'koparmak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: kırmızı böğürtlenler olgun değildi ve daldan çıkmıyordu | annesine sordu ve siyah yumuşak olanları kopardı
@tohum: hello_kitty-0024
@degisim: pürüzsüz -> düz
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Hello Kitty, annesinin gösterdiği çalıdan ilk kez böğürtlen koparmayı denedi. Ama kırmızı böğürtlenler daha olgun değildi, çok sertti ve daldan çıkmıyordu. Hello Kitty böğürtlenleri annesinin elmalı turtasına koymak istiyordu. Yaprakların arasında siyah ve yumuşak böğürtlenler de vardı. "Anne, siyah olanları koparabilir miyim?" diye sordu Hello Kitty. "Evet, siyah olanlar daha tatlı," dedi annesi. Hello Kitty siyah böğürtlenleri hafifçe çekti ve kolayca kopardı. Böğürtlenleri turtanın üstüne düz bir sıra olarak dizdi. "Turtamız çok güzel oldu!" dedi annesi. İkisi gölgeye oturdu ve Hello Kitty'nin en sevdiği turtayı mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çalıdan ilk kez böğürtlen koparmayı denedi"
   - Cümle 2: «Hello Kitty, annesinin gösterdiği çalıdan ilk kez böğürtlen koparmayı denedi.»
   - Açıklama: Ormanda yabani meyve koparıp yemek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0024` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: 85cbbc916e50ab2a164e29a14c1fa89c67466c4d`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0025 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0025
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'şampuan', fiil 'erimek', sıfat 'kibar'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: şeker soğuk suda erimedi | kardeşinden kaşık isteyip limonatayı uzun uzun karıştırdı
@tohum: hello_kitty-0025
@degisim: şampuan -> kaşık
Hello Kitty ile Mimi mutfakta ilk kez limonata yapmayı denedi. Büyük bir kaseye soğuk su, limon suyu ve şeker koydular. Ama şeker erimedi ve kasenin dibinde kaldı, çünkü su çok soğuktu. Hello Kitty biraz düşündü. "Mimi, bana uzun bir kaşık verir misin?" diye sordu Hello Kitty. Mimi çekmeceden bir kaşık çıkardı ve ona verdi. Hello Kitty limonatayı kaşıkla uzun uzun karıştırdı. Şeker yavaş yavaş eridi ve limonata tatlı oldu. Hello Kitty iki bardağa limonata koydu. Hello Kitty kibar bir arkadaştı ve ilk bardağı Mimi'ye uzattı. "Çok güzel olmuş, teşekkürler!" dedi Mimi. Sonra iki kardeş limonatalarını mutlu mutlu içti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty kibar bir arkadaştı"
   - Cümle 10: «Hello Kitty kibar bir arkadaştı ve ilk bardağı Mimi'ye uzattı.»
   - Açıklama: Mimi onun kardeşi; 'arkadaş' kelimesi yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kibar bir arkadaştı"
   - Cümle 10: «Hello Kitty kibar bir arkadaştı ve ilk bardağı Mimi'ye uzattı.»
   - Açıklama: Tohumdaki arkadaş özelliği çözüme katkı vermeden etiket olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0025` birebir aynı, `@degisim: şampuan -> kaşık` (tutuyorsan), ardından `@onarim: a300fb590468febd21d3e23fdd5b39447800fd34`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0029 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0029
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çorba', fiil 'açılmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: rüzgar kapıyı açtı ve kapı kapanmadı | kardeşinden yardım isteyip kapıyı birlikte itti
@tohum: hello_kitty-0029
Hello Kitty ile Mimi mutfakta sıcak çorbalarını içiyordu. Dışarısı çok rüzgarlıydı. Birden kapı rüzgarla açıldı ve içeri soğuk hava doldu. Hello Kitty kaşığını bıraktı ve kapıya gitti. Kapıyı itti, ama rüzgar çok güçlüydü ve kapı kapanmadı. Hello Kitty arkadaşlarından hep kibarca yardım isterdi. "Mimi, lütfen bana yardım eder misin?" diye sordu Hello Kitty. Mimi gülümsedi ve hemen kardeşinin yanına koştu. İkisi "Bir, iki, üç!" diye saydı ve kapıyı birlikte itti. Kapı yavaşça kapandı. Mutfak yine sıcacık oldu. İkisi masaya döndü ve çorbalarını bitirdi. "Teşekkürler, Mimi, çok yardımcı oldun!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarından hep kibarca yardım isterdi"
   - Cümle 6: «Hello Kitty arkadaşlarından hep kibarca yardım isterdi.»
   - Açıklama: Tohumdaki özellik yeni arkadaş edinmek; hikaye onu kibarca yardım istemek olarak değiştiriyor.
   - Açıklama: Karttaki özellik yeni arkadaş edinmeyi sevmek; burada arkadaşlardan yardım isteme alışkanlığına çevrilmiş ve sorunu çözmede işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0029` birebir aynı, ardından `@onarim: 2de9f2f0fbd3981f3332efb867a09cfe80e965ef`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0033 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0033
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'ay', fiil 'üzülmek', sıfat 'sıcacık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: çizdiği ay yuvarlak olmadı ve çok üzüldü | annesinden yardım isteyip bardağın çevresini çizdi
@tohum: hello_kitty-0033
Hello Kitty pencerenin önünde oturmuş, gökyüzündeki aya bakıyordu. Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu. Ama çizdiği ay yuvarlak olmadı, çünkü eli hep kayıyordu. Hello Kitty resme baktı ve çok üzüldü. Annesi de odadaydı. "Anne, ay yuvarlak olmuyor, bana yardım eder misin?" diye sordu Hello Kitty. Annesi gülümsedi ve ona bir bardak verdi. "Bardağı kağıda koy ve çevresini çiz," dedi annesi. Hello Kitty bardağı kağıda koydu ve kalemle etrafından yavaşça çizdi. Kağıtta kocaman, yuvarlak bir ay vardı. Hello Kitty sevindi, çünkü artık resmi arkadaşlarına verebilecekti. Annesine sıcacık sarıldı. Hello Kitty bundan sonra bir şeyi yapamayınca annesinden yardım istedi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu"
   - Cümle 2: «Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu.»
   - Açıklama: Karttaki arkadaş özelliği yalnız bir istek gerekçesi olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0033` birebir aynı, ardından `@onarim: c625792965db7c1109c8bb34f6f652998ea82f6d`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0034 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0034
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'eşarp', fiil 'özlemek', sıfat 'buzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası yanındaydı ve her şeyi görüyordu | babasının gözlerini eşarpla kapattı ve kurabiyeleri dizdi
@tohum: hello_kitty-0034
Ormanda ağaçların dalları buzluydu. Hello Kitty kamp yerinde babasına bir sürpriz hazırlamak istedi. Ama babası hemen yanında oturuyordu ve her şeyi görüyordu. "Kurabiyeleri çok özledim," dedi babası. Hello Kitty'nin çantasında evde babasıyla yaptığı kurabiyeler ve pembe bir eşarp vardı. "Baba, bu eşarpla gözlerini bağlayayım mı?" diye sordu Hello Kitty. Babası gülerek başını salladı. Hello Kitty eşarbı babasının gözlerine yavaşça bağladı. Sonra kurabiyeleri çantadan çıkarıp kütüğün üstüne dizdi. En sonunda eşarbı çözdü. Babası kurabiyeleri görünce çok şaşırdı. "Bu çok güzel bir sürpriz, kızım!" dedi babası. "Afiyet olsun, babacığım!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasında evde babasıyla yaptığı kurabiyeler ve pembe bir eşarp vardı"
   - Cümle 5: «Hello Kitty'nin çantasında evde babasıyla yaptığı kurabiyeler ve pembe bir eşarp vardı.»
   - Açıklama: Çözümü sağlayan eşarp tam gerektiği anda sebepsizce çantada beliriyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "evde babasıyla yaptığı kurabiyeler"
   - Cümle 5: «Hello Kitty'nin çantasında evde babasıyla yaptığı kurabiyeler ve pembe bir eşarp vardı.»
   - Açıklama: Kurabiyeleri babasıyla birlikte yapmışken babanın kurabiyeleri görünce çok şaşırması sürprizle çelişiyor.
   - Açıklama: Babası kurabiyeleri kendisi birlikte yapmışken onları görünce çok şaşırması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0034` birebir aynı, ardından `@onarim: ef1375d8c214f274e42d4703602031374e1215a3`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0035 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0035
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'sebze', fiil 'karışmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar tabağı devirdi ve sebzelerden yapılan yüz bozuldu | tabağı ağacın dibine koyup yüzü yeniden yaptı
@tohum: hello_kitty-0035
Parkta, ağaçların gölgesinde Hello Kitty piknik yapıyordu. Kağıt tabağına sebzelerle gülen bir yüz yapmıştı. Ama birden rüzgar esti ve hafif tabak çimenlere devrildi. Sebzeler birbirine karıştı ve yüz bozuldu. Hello Kitty bu yüzü yeni arkadaşlarına göstermek istiyordu. Şimdi biraz mutsuzdu. Önce tabağı ağacın dibine, rüzgarın gelmediği yere koydu. Sonra sebzeleri tek tek topladı. İki havuç dilimi yüzün gözleri oldu. Bir domates dilimi de ağız oldu. İki salatalık parçasını da kulak diye yukarıya dizdi. Rüzgar yine esti ama tabak artık kıpırdamadı. Hello Kitty çok sevindi, çünkü gülen yüzü arkadaşlarına gösterebilecekti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty piknik yapıyordu"
   - Cümle 1: «Parkta, ağaçların gölgesinde Hello Kitty piknik yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty parkta yanında büyük olmadan yalnız.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bu yüzü yeni arkadaşlarına göstermek istiyordu"
   - Cümle 5: «Hello Kitty bu yüzü yeni arkadaşlarına göstermek istiyordu.»
   - Açıklama: Kartın özellikler alanındaki arkadaş özelliği sorunu çözmekte işe yaramıyor, yalnız iki kez anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0035` birebir aynı, ardından `@onarim: 74b4d7ba214f6b50c23116a6cb9d5272bdb0cd18`, sonra gövde.
