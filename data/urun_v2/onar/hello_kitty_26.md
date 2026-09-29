# Editör görevi (onarım): Hello Kitty, onarım partisi 26

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar26.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar26.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0006
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'tabela', fiil 'anlatmak', sıfat 'sulu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: rüzgar tabelayı ters çevirdi ve ok yanlış yeri gösterdi | tabelayı düzeltti ve pencereyi kapattı
@tohum: hello_kitty-0006
Evde Hello Kitty, Mimi'ye yeni bir hazine oyunu anlattı. Kapıya mutfağı gösteren oklu bir tabela asmıştı. Ama pencereden esen rüzgar tabelayı ters çevirdi. Şimdi ok banyoyu gösteriyordu. Mimi oku izledi ve banyoya girdi. Orada yalnız bir sabun ile bir havlu buldu. "Hazine bu sabun mu?" diye sordu Mimi. Hello Kitty güldü ve tabelaya baktı. "Rüzgar oku çevirmiş!" dedi Hello Kitty. Tabelayı hemen düzeltti ve pencereyi kapattı. Mimi bu kez oku izleyip mutfağa koştu. Masada, Hello Kitty'nin en sevdiği sulu elmalı turta vardı. Mimi sevinçle ellerini çırptı. "Bu hazineyi seninle paylaşmak çok güzel, Mimi!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Tabelayı hemen düzeltti ve"
   - Cümle 10: «Tabelayı hemen düzeltti ve pencereyi kapattı.»
   - Açıklama: Tabelayı kimin düzelttiği belli değil; son özne Mimi ama işi Hello Kitty yapmış olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0006` birebir aynı, ardından `@onarim: a09f6dc1a02be0bf5c195302ae477b99ae2fc9b5`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0069 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0069
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'köfte', fiil 'çizmek', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: kedinin başı çok büyüktü ve köfte için yer kalmadı | büyük çizgileri silip daha küçük bir baş çizdi
@tohum: hello_kitty-0069
@degisim: düşünceli -> küçük
Parkta, yolun kenarında yumuşak bir toprak vardı. Hello Kitty yeni arkadaşlar için toprağa köfte yiyen bir kedi çiziyordu. Ama kedinin başını çok büyük çizmişti ve köfte için yer kalmadı. Hello Kitty toprağa baktı ve biraz düşündü. Sonra büyük çizgileri eliyle sildi. Bu kez daha küçük, yuvarlak bir baş çizdi. Şimdi toprakta köfte için de yer vardı. Hello Kitty başa iki göz, uzun bıyıklar ve iki sivri kulak ekledi. En sona kedinin önüne bir köfte çizdi. Hello Kitty çok sevindi, çünkü resmi yeni arkadaşlar için hazırdı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlar için toprağa"
   - Cümle 2: «Hello Kitty yeni arkadaşlar için toprağa köfte yiyen bir kedi çiziyordu.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız iki kez anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki 'arkadaş' özelliği iki kez anılıyor ve sorunun çözümünde işe yaramıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "En sona kedinin önüne"
   - Cümle 9: «En sona kedinin önüne bir köfte çizdi.»
   - Açıklama: 'En sona' bu yapıda yanlış; 'En son' ya da 'En sonunda' olmalı.
   - Açıklama: Zarf yanlış kurulmuş; 'En son' ya da 'En sonda' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0069` birebir aynı, `@degisim: düşünceli -> küçük` (tutuyorsan), ardından `@onarim: 3730c2af0f5d9bcd4fcad04adb9527cd8b5d1f0a`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0072 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0072
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'içecek', fiil 'yuvarlamak', sıfat 'rahat'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: oyun hamuru çok sertti ve kurabiyeler kırılıyordu | hamuru elleri arasında yuvarladı ve yumuşattı
@tohum: hello_kitty-0072
Dışarıda yağmur tıp tıp yağıyordu. Hello Kitty evde çay oyunu için oyun hamurundan kurabiye yapmak istedi. Ama hamur çok sertti ve kurabiyeler hep kırılıyordu. Hello Kitty hamura baktı ve biraz düşündü. Gerçek kurabiye yaparken hamuru hep elleriyle ısıtırdı. Sonra hamuru iki elinin arasında uzun uzun yuvarladı. Hamur ısındı ve yavaş yavaş yumuşadı. Hello Kitty küçük toplar yaptı ve hepsini düz bastırdı. Artık hiçbir kurabiye kırılmadı. Hello Kitty yuvarlak kurabiyeleri bir tabağa dizdi. Çay oyunu için yanına bir bardak içecek koydu. Sonra masaya rahatça oturdu ve çay oyununa mutlu mutlu başladı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Çay oyunu için yanına"
   - Cümle 11: «Çay oyunu için yanına bir bardak içecek koydu.»
   - Açıklama: 'Çay oyunu' ifadesi kısa metinde üç kez gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0072` birebir aynı, ardından `@onarim: b44575e40218cb62d5e92dff732fc6e2cbd7a6b7`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0075 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0075
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'mermer', fiil 'eşleştirmek', sıfat 'büyük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: babası elmaları nereye koyduğunu unuttu | çantayı hatırladı ve elmaları tezgahta buldu
@tohum: hello_kitty-0075
@degisim: eşleştirmek -> hatırlamak
Hello Kitty babasıyla mutfaktaki mermer tezgahta turta yapmak istedi. En çok elmalı turtayı severdi ama babası elmaları nereye koyduğunu unutmuştu. Babası dolaba baktı ve elmaları orada bulamadı. "Kızım, bana yardım eder misin?" diye sordu babası. Hello Kitty biraz düşündü ve hatırladı. "Baba, eve büyük bir çantayla geldin, belki elmalar oradadır," dedi Hello Kitty. Sonra etrafına baktı. Büyük çanta, tezgahın öbür ucunda duruyordu. Hello Kitty çantayı açtı ve içinde kırmızı elmaları buldu. Babası güldü ve elmaları yıkamaya başladı. "Teşekkürler, kızım, elmaları sen buldun!" dedi babası.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Büyük çanta, tezgahın öbür"
   - Cümle 8: «Büyük çanta, tezgahın öbür ucunda duruyordu.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.
   - Açıklama: Özneden sonra gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0075` birebir aynı, `@degisim: eşleştirmek -> hatırlamak` (tutuyorsan), ardından `@onarim: 7fcaee58d20c1470b6cfce2174cd55dadb982440`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0078 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0078
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fıskiye', fiil 'karşılamak', sıfat 'enerjik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası sırayı unutuyor ve topu hep kendisi tutuyordu | kızmadan babasına sırayla atmayı önerdi
@tohum: hello_kitty-0078
@degisim: fıskiye -> çimen
Bir sabah Hello Kitty babasıyla parkta top oynuyordu. Ama babası çok enerjikti ve sırayı hep unutuyordu. Topu havaya atıyor ve yine kendisi tutuyordu. Hello Kitty'ye hiç sıra gelmedi. Bir ara top ağacın gölgesine yuvarlandı ve babası onu getirdi. Hello Kitty babasını çimenlerde gülerek karşıladı. Kızmadı, çünkü herkese bir arkadaş gibi iyi davranırdı. "Baba, sırayla atalım, şimdi sıra bende," dedi Hello Kitty. "Haklısın, unuttum!" dedi babası ve topu ona verdi. Hello Kitty topu babasına attı ve babası onu tuttu. Sonra topu yavaşça ona geri attı. Hello Kitty onu iki eliyle yakaladı. Hello Kitty çok sevindi, çünkü artık sıra ikisine de geliyordu.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "babası çok enerjikti"
   - Cümle 2: «Ama babası çok enerjikti ve sırayı hep unutuyordu.»
   - Açıklama: 'Enerjik' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "babası çok enerjikti ve"
   - Cümle 2: «Ama babası çok enerjikti ve sırayı hep unutuyordu.»
   - Açıklama: 'Enerjik' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir ara top ağacın gölgesine yuvarlandı ve babası onu getirdi"
   - Cümle 5: «Bir ara top ağacın gölgesine yuvarlandı ve babası onu getirdi.»
   - Açıklama: Topun gölgeye yuvarlanması olaydan çıkmıyor ve hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "top ağacın gölgesine yuvarlandı"
   - Cümle 5: «Bir ara top ağacın gölgesine yuvarlandı ve babası onu getirdi.»
   - Açıklama: Topun gölgeye yuvarlanması hiçbir işe yaramayan işlevsiz bir olay.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "herkese bir arkadaş gibi iyi davranırdı"
   - Cümle 7: «Kızmadı, çünkü herkese bir arkadaş gibi iyi davranırdı.»
   - Açıklama: Soyut genelleme, olaydan çıkan somut bir ders değil.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra topu yavaşça ona geri attı"
   - Cümle 11: «Sonra topu yavaşça ona geri attı.»
   - Açıklama: Önceki cümlenin öznesi Hello Kitty olduğundan topu kimin kime attığı ve 'ona'nın kimi gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0078` birebir aynı, `@degisim: fıskiye -> çimen` (tutuyorsan), ardından `@onarim: 78472d99b8aefd9327f59586ffe3b131f3cd39c1`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0079 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0079
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kitap', fiil 'kucaklamak', sıfat 'dağınık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: mutfaktan bilinmeyen bir ses geldi | kurabiye kitabının durduğu tezgaha baktı ve sesi buldu
@tohum: hello_kitty-0079
Mutfağın penceresinden serin bir rüzgar esiyordu. Hello Kitty odasında otururken mutfaktan hışır hışır bir ses duydu. Bu sesi çok merak etti. Yavaşça mutfağa yürüdü. Ses, kağıttan geliyor gibiydi. Hello Kitty kurabiye yaparken hep bir kitaba bakardı. O kitap pencerenin önündeki tezgahta dururdu. Hemen tezgaha baktı. Rüzgar kitabın sayfalarını tek tek çeviriyordu. Ses buradan geliyordu. Pencereyi kapattı ve dağınık sayfaları düzeltti. Sonra kitabı sıkıca kucakladı. Hello Kitty çok sevindi, çünkü sesi bulmuş ve kitabını korumuştu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Pencereyi kapattı ve dağınık sayfaları düzeltti."
   - Cümle 11: «Pencereyi kapattı ve dağınık sayfaları düzeltti.»
   - Açıklama: Önceki cümlenin öznesi 'Ses' olduğu için pencereyi kimin kapattığı açıkça belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0079` birebir aynı, ardından `@onarim: ba3b1ad30c3181ca9c7d0ddcf9d83562fad19a4b`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0080 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0080
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'masa', fiil 'karıştırmak', sıfat 'bembeyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: babasının beyaz boyası bitti | kendi beyaz boyasını babasıyla paylaştı
@tohum: hello_kitty-0080
Dışarıda kar sessizce yağıyordu. Hello Kitty ve babası masada karlı bir resim yapıyordu. Ama babasının beyaz boyası bitmişti. "Eyvah, bende hiç beyaz kalmadı," dedi babası. Hello Kitty herkese iyi davranırdı. Kendi beyaz boyasını hemen babasının önüne koydu. "Baba, bunu birlikte kullanalım," dedi Hello Kitty. Babası fırçasını suya batırdı ve boyayla karıştırdı. Sonra kağıttaki karları bembeyaz yaptı. "Teşekkürler, kızım, sen çok iyi bir arkadaşsın," dedi babası. Hello Kitty gülümsedi. İkisi resimlerini yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fırçasını suya batırdı ve boyayla karıştırdı"
   - Cümle 8: «Babası fırçasını suya batırdı ve boyayla karıştırdı.»
   - Açıklama: Nesnesi fırça olarak okunuyor; fırça boyayla karıştırılmaz, fiil nesnesine uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "suya batırdı ve boyayla karıştırdı"
   - Cümle 8: «Babası fırçasını suya batırdı ve boyayla karıştırdı.»
   - Açıklama: Karıştırılan nesne belirsiz; fırça boyayla karıştırılmaz, 'fırçayı boyaya batırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0080` birebir aynı, ardından `@onarim: 7d629f023929f3663c804f57cf030109b0b6500a`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0084 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0084
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'piyano', fiil 'gülüşmek', sıfat 'rengarenk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: piyanonun tuşlarına küçük bir dal sıkıştı | piyanoyu ters çevirip salladı ve dalı düşürdü
@tohum: hello_kitty-0084
@degisim: gülüşmek -> gülmek
Ormanda rüzgar yavaşça esiyordu. Hello Kitty ailece kamp yapıyordu ve yeni arkadaşlar için şarkı hazırlıyordu. Ama ağaçtan küçük bir dal düştü ve rengarenk piyanosunun tuşlarına sıkıştı. Piyano artık güzel ses vermiyordu. Hello Kitty tuşlara dikkatle baktı ve dalı gördü. Piyanoyu yavaşça ters çevirdi ve biraz salladı. Küçük dal çimenlere düştü. Piyano yeniden güzel ses verdi. Hello Kitty şarkısını baştan sona çaldı ve neşeyle güldü. Hello Kitty çok mutluydu, çünkü şarkısı yeni arkadaşlar için hazırdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlar için şarkı"
   - Cümle 2: «Hello Kitty ailece kamp yapıyordu ve yeni arkadaşlar için şarkı hazırlıyordu.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız iki kez anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0084` birebir aynı, `@degisim: gülüşmek -> gülmek` (tutuyorsan), ardından `@onarim: 8907969bbe116de0cc2faca290d24fe500d1b73b`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0088 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0088
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yapboz', fiil 'kalkmak', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: yapbozun son parçası birden kayboldu | turta tabağını kaldırıp parçayı altında buldu
@tohum: hello_kitty-0088
Hello Kitty ormandaki kamp yerinde annesiyle yapboz yapıyordu. Yanlarında annesinin yaptığı elmalı turta duruyordu. Ama yapbozun son parçası bir anda kayboldu. Annesi yerinden kalktı ve eteğini salladı. Parça eteğinden düşmedi. Hello Kitty kararlıydı, yapbozu bitirmek istiyordu. Hello Kitty yapbozun yanındaki turta tabağına baktı. "Anne, belki parça tabağın altına kaydı," dedi Hello Kitty. Tabağı yavaşça kaldırdı ve altında küçük parçayı gördü. Hello Kitty parçayı hemen yerine koydu. "Anne, yapboz bitti, şimdi turta zamanı!" dedi Hello Kitty sevinçle.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yapbozun son parçası bir anda kayboldu"
   - Cümle 3: «Ama yapbozun son parçası bir anda kayboldu.»
   - Açıklama: Parçanın kaybolmasının sebebi söylenmiyor, parça sebepsizce bir anda yok oluyor.
   - Açıklama: Parçanın neden kaybolduğu söylenmiyor; tabağın altına nasıl girdiği açıklanmadan bir anda yok oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0088` birebir aynı, ardından `@onarim: d8704ae875e9128b5db271a7d20a2e2e0b754991`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0089 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0089
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'küp', fiil 'susmak', sıfat 'basit'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: ikisi aynı anda küp koyunca kule yıkıldı | kurabiyeyi sıra işareti yapıp sırayla küp koydular
@tohum: hello_kitty-0089
Parkta ağaçların gölgesinde Hello Kitty ile babası küp oyunu oynuyordu. İkisi küpleri üst üste koyup bir kule yapıyordu. Ama ikisi aynı anda küp koyunca kule yıkıldı. Babası bir an sustu, sonra güldü. "Böyle olmuyor, Hello Kitty," dedi babası. Hello Kitty sepetten evde babasıyla yaptığı bir kurabiyeyi çıkardı. "Önce sen koy, sonra kurabiyeyi bana ver," dedi Hello Kitty. Bu çok basit bir oyundu. Babası küpünü koydu ve kurabiyeyi Hello Kitty'ye verdi. Hello Kitty de küpünü koydu ve kurabiyeyi geri uzattı. Kule yavaş yavaş yükseldi ve bu kez hiç yıkılmadı. Sonra kurabiyeyi ikiye böldüler ve oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty sepetten evde babasıyla yaptığı bir kurabiyeyi çıkardı"
   - Cümle 6: «Hello Kitty sepetten evde babasıyla yaptığı bir kurabiyeyi çıkardı.»
   - Açıklama: Sepet ve kurabiye önceden kurulmadan beliriyor ve sıra işareti olarak çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0089` birebir aynı, ardından `@onarim: 59e00482199b8af707e9b114da343cd97a2b548c`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0092 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0092
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'inci', fiil 'korunmak', sıfat 'işaretli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: zıplarken incileri ıslak çimenlere döktü | özür diledi ve incileri tek tek topladı
@tohum: hello_kitty-0092
@degisim: işaretli -> ıslak
Yağmur çadırın üstüne tıp tıp yağıyordu. Hello Kitty annesiyle çadırın içinde yağmurdan korunuyordu. Zıplarken inci kabına çarptı ve inciler çadırın kapısından ıslak çimenlere döküldü. Hello Kitty o incilerle yeni arkadaşlarına bileklik yapmak istiyordu. Annesi incilere baktı ve bir şey demedi. "Özür dilerim, anne, dikkat etmedim," dedi Hello Kitty. Hemen eğildi ve incileri tek tek topladı. Hepsini kaba geri koydu. Annesi gülümsedi ve ona sarıldı. Sonra ikisi yağmurun sesini dinleyerek bileklikleri mutlu mutlu yaptı.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Yağmur çadırın üstüne tıp tıp yağıyordu"
   - Cümle 1: «Yağmur çadırın üstüne tıp tıp yağıyordu.»
   - Açıklama: Hikaye bir çadırda geçiyor ve başlıktaki orman hiç kurulmuyor, bu yüzden yer belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0092` birebir aynı, `@degisim: işaretli -> ıslak` (tutuyorsan), ardından `@onarim: 260a72e27a387d29dfb13a2c4e19c539255ccaac`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0093 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0093
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'salatalık', fiil 'anlamak', sıfat 'sevecen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesi salatalık keserken yüzüğünü kaybetti | salatalık kabına bakıp yüzüğü buldu ve annesine verdi
@tohum: hello_kitty-0093
@degisim: sevecen -> küçük
Bir sabah Hello Kitty annesiyle ormandaki kamp yerindeydi. Annesi piknik için salatalık keserken yüzüğünü çıkarmıştı. Ama şimdi onu hiçbir yerde bulamıyordu. Annesi çok üzüldü, çünkü o yüzüğü çok seviyordu. Hello Kitty annesinin elini tuttu. "Üzülme, anne, sana yardım edeyim," dedi Hello Kitty. Önce örtünün altına baktı ama orada bir şey yoktu. Sonra salatalık kabını gördü ve yüzüğün nerede olduğunu anladı. Küçük yüzük salatalık dilimlerinin arasındaydı. Hello Kitty onu dikkatle çıkardı ve annesine verdi. Annesi yüzüğü taktı ve ona sıkıca sarıldı. Hello Kitty bundan sonra arkadaşları bir şey kaybedince de yardım etti.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşları bir şey kaybedince de yardım etti"
   - Cümle 12: «Hello Kitty bundan sonra arkadaşları bir şey kaybedince de yardım etti.»
   - Açıklama: Tohum özelliği sona eklenmiş bir cümlede anılıyor, hikayenin sorununu çözmede işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bundan sonra arkadaşları bir şey kaybedince"
   - Cümle 12: «Hello Kitty bundan sonra arkadaşları bir şey kaybedince de yardım etti.»
   - Açıklama: Tohumdaki 'arkadaş' özelliği çözümde işe yaramıyor, yalnız son cümleye ekleniyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "arkadaşları bir şey kaybedince de yardım etti"
   - Cümle 12: «Hello Kitty bundan sonra arkadaşları bir şey kaybedince de yardım etti.»
   - Açıklama: Arka plandaki çoğul canlılar (arkadaşları) olaya katılıyor.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "bundan sonra arkadaşları bir şey kaybedince"
   - Cümle 12: «Hello Kitty bundan sonra arkadaşları bir şey kaybedince de yardım etti.»
   - Açıklama: Notlanan çoğul canlı 'arkadaşları' arka planda kalmıyor, olaya katılan kişiler olarak anlatılıyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bundan sonra arkadaşları bir şey kaybedince de yardım etti"
   - Cümle 12: «Hello Kitty bundan sonra arkadaşları bir şey kaybedince de yardım etti.»
   - Açıklama: Son cümle yüzük olayından çıkan somut bir ders ya da sıcak kapanış değil, olaydan kopuk genel bir sonraki davranış bildiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0093` birebir aynı, `@degisim: sevecen -> küçük` (tutuyorsan), ardından `@onarim: e9c44f97c8e074f483d64da5a8bf204424b27a1a`, sonra gövde.
