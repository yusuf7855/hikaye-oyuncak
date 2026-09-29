# Editör görevi (onarım): Hello Kitty, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0004 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0004
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'zil', fiil 'ölçmek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesinin küçük zili çantadan düştü | ince sesi dinledi ve zili çalının dalında buldu
@tohum: hello_kitty-0004
@degisim: ölçmek -> dinlemek
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Ilık bir rüzgar esiyordu. Annesinin küçük zili çantasında yoktu. Zil çantadan bir yere düşmüştü ve annesi üzüldü. Birden ağaçların arasından ince bir ses geldi. Hello Kitty sesi merak etti ve durup dinledi. "Anne, belki orada yeni bir arkadaş vardır!" dedi Hello Kitty. "Gel, bakalım," dedi annesi. Hello Kitty sese doğru yürüdü, annesi de arkasından geldi. Ses bir çalının içinden geliyordu. Hello Kitty çalıya baktı ve dalda küçük zili buldu. Zil rüzgarda sallanıyor ve çalıyordu. Hello Kitty zili annesine verdi ve annesi ona sarıldı. Hello Kitty çok sevindi, çünkü annesinin zilini bulmuştu.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Zil çantadan bir yere düşmüştü"
   - Cümle 4: «Zil çantadan bir yere düşmüştü ve annesi üzüldü.»
   - Açıklama: Çantadan düşen zilin bir çalının dalına nasıl çıktığı akla yatkın biçimde söylenmiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "belki orada yeni bir arkadaş vardır"
   - Cümle 7: «"Anne, belki orada yeni bir arkadaş vardır!" dedi Hello Kitty.»
   - Açıklama: Arkadaş edinme özelliği yalnız bir tahmin olarak geçiyor; sorunu çözen zilin sesini dinlemek, özellik işe yaramıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "belki orada yeni bir arkadaş vardır"
   - Cümle 7: «"Anne, belki orada yeni bir arkadaş vardır!" dedi Hello Kitty.»
   - Açıklama: Hello Kitty zili aramıyor, yeni arkadaş sanarak sese gidiyor; çözüm sebebe yönelmiyor.
   - Açıklama: Hello Kitty zili aramıyor, sese yeni arkadaş sanarak gidiyor; çözüm sebebe yönelmiyor, tesadüfle geliyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty sese doğru yürüdü"
   - Cümle 9: «Hello Kitty sese doğru yürüdü, annesi de arkasından geldi.»
   - Açıklama: Ormanda bilinmeyen bir sese 'yeni arkadaş' diye yürümek, çocuğun yabancıya yaklaşmasını örnekleyebilir.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dalda küçük zili buldu"
   - Cümle 11: «Hello Kitty çalıya baktı ve dalda küçük zili buldu.»
   - Açıklama: Çantadan düşen zilin çalının dalına asılı olması sebepsiz ve çözümü tesadüfen getiriyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Zil rüzgarda sallanıyor ve çalıyordu"
   - Cümle 12: «Zil rüzgarda sallanıyor ve çalıyordu.»
   - Açıklama: Zil tesadüfen çalıp bulunuyor; çözüm sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0004` birebir aynı, `@degisim: ölçmek -> dinlemek` (tutuyorsan), ardından `@onarim: 36ae29e4a82b7bb984b5c1f304e18809ffbaf5ca`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0013 (deneme 4 -> 5)

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
Hello Kitty ile annesi parkta düz taşları boyuyordu. Annesi taşına Hello Kitty için küçük bir kedi arkadaş yaptı. Ama kalın fırçasıyla kedinin ince bıyıklarını yapamadı. "Bu fırça çok kalın," dedi annesi. Hello Kitty bu yeni kedinin bıyıksız kalmasını istemedi. Hemen kendi fırçalarına baktı. Hello Kitty'nin bir de incecik bir fırçası vardı. "Anne, bu fırçayı sana veriyorum!" dedi Hello Kitty. Annesi fırçayı aldı ve bıyıkları tek tek çizdi. Taşın üstündeki kedi artık çok tatlı görünüyordu. "Teşekkürler, kızım," dedi annesi. Hello Kitty çok mutlu oldu, çünkü fırçasını annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük bir kedi arkadaş yaptı"
   - Cümle 2: «Annesi taşına Hello Kitty için küçük bir kedi arkadaş yaptı.»
   - Açıklama: Taşa kedi resmi çizilir; 'kedi arkadaş yaptı' kelimeyi yanlış anlamda kullanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "küçük bir kedi arkadaş yaptı"
   - Cümle 2: «Annesi taşına Hello Kitty için küçük bir kedi arkadaş yaptı.»
   - Açıklama: Arkadaş özelliği Hello Kitty'nin kendi huyu olarak kullanılmıyor, çözüme katkısı yok.
   - Açıklama: Tohumdaki arkadaş edinme özelliği boyanan bir resme indirgenmiş, çözümde karttaki gibi işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0013` birebir aynı, `@degisim: yollamak -> vermek` (tutuyorsan), ardından `@onarim: b5f0f4730cef78a47dafbdf88cb4f375d503ac27`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0014 (deneme 4 -> 5)

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
Bir sabah Hello Kitty parkta köpük balonu yapıyordu. Çubuğu sabunlu suya batırdı ve havada salladı. Ama rüzgar esince balonlar küçükken çubuktan koptu ve uzaklaştı. Hello Kitty çok büyük bir balon yapmak istiyordu. Küçük balonlar çiçeklerin üstünde bir bir patladı. Hello Kitty etrafına baktı ve kalın bir ağaç gördü. Ağacın arkasına geçti, orada rüzgar yoktu. Bu kez çubuğu çok yavaş salladı. Çubuğun ucunda bir balon büyümeye başladı. Balon sonunda bir karnabahar kadar oldu! Hello Kitty çok sevindi, çünkü arkadaşlarına gösterecek büyük bir balon yapmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarına gösterecek büyük bir balon"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü arkadaşlarına gösterecek büyük bir balon yapmıştı.»
   - Açıklama: Tohum özelliği (arkadaş) yalnız son cümlede süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği sorunun çözümünde işe yaramıyor, yalnız sonda süs olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0014` birebir aynı, ardından `@onarim: c5c4ed9b64de0c4aa9824dc20e01cb7bb71248c0`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0015 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0015
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'para', fiil 'gezdirmek', sıfat 'devasa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kardeşinin kurdelesi başının arkasında bir dala takıldı | kurdeleyi daldan yavaşça çıkardı ve yine bağladı
@tohum: hello_kitty-0015
@degisim: devasa -> büyük
Bir sabah Hello Kitty ile Mimi ormandaki kamp yerinde, çadırın yanındaydı. Mimi büyük bir ağacın altında parlak bir para gördü. Parayı aldı ama kalkarken sarı kurdelesi alçak bir dala takıldı. Mimi kurdeleyi göremedi, çünkü kurdele başının arkasındaydı. Mimi kurdelesini çok seviyordu ve üzüldü. Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin arkasına hemen geçti. Dala baktı. Kurdele dala dolanmıştı. Hello Kitty parmaklarını dalın üstünde gezdirdi ve kurdelenin ucunu buldu. Kurdeleyi daldan yavaşça çözdü. Sonra onu Mimi'nin başına güzelce bağladı. Mimi sevinçle gülümsedi ve kardeşine sarıldı. Sonra iki kardeş çadırın yanında parayla mutlu mutlu oynadı.
```

**Hakem bulguları (8):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ile Mimi ormandaki kamp yerinde"
   - Cümle 1: «Bir sabah Hello Kitty ile Mimi ormandaki kamp yerinde, çadırın yanındaydı.»
   - Açıklama: İki küçük kardeş ormanda büyük olmadan yalnız; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "parlak bir para gördü"
   - Cümle 2: «Mimi büyük bir ağacın altında parlak bir para gördü.»
   - Açıklama: Para sebepsiz beliriyor ve sonda kurdele sorunuyla ilgisiz bir oyun nesnesine dönüşüyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin"
   - Cümle 6: «Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin arkasına hemen geçti.»
   - Açıklama: Virgül cümleyi üç ayrı kişi sayılıyormuş gibi okutuyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin"
   - Cümle 6: «Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin arkasına hemen geçti.»
   - Açıklama: Önceden tanıtılmış Mimi yeniden tanıtılıyor ve cümle üç ayrı kişi gibi okunabiliyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kardeşi ve en iyi arkadaşı Mimi'nin"
   - Cümle 6: «Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin arkasına hemen geçti.»
   - Açıklama: Mimi hikayenin ortasında yeniden tanıtılıyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kardeşi ve en iyi arkadaşı"
   - Cümle 6: «Hello Kitty, kardeşi ve en iyi arkadaşı Mimi'nin arkasına hemen geçti.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği yalnız ilişki etiketi olarak geçiyor, işe yaramıyor.
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, yalnız Mimi'nin ilişkisi sayılıyor.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çadırın yanında parayla mutlu mutlu oynadı"
   - Cümle 13: «Sonra iki kardeş çadırın yanında parayla mutlu mutlu oynadı.»
   - Açıklama: Yerde bulunan bozuk parayla oynamak küçük çocuk için yutma tehlikesi taşıyan taklit edilebilir bir davranış.
8. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "parayla mutlu mutlu oynadı"
   - Cümle 13: «Sonra iki kardeş çadırın yanında parayla mutlu mutlu oynadı.»
   - Açıklama: Yerden bulunan bozuk parayla oynamak küçük çocuk için yutma tehlikesi taşıyan, taklit edilebilir bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0015` birebir aynı, `@degisim: devasa -> büyük` (tutuyorsan), ardından `@onarim: db7d8f1b630a08a6bfdd898e9c89e1ee9022fb0b`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0016 (deneme 4 -> 5)

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
Bir sabah ormandaki kamp yerinde serin bir rüzgar esti. Hello Kitty'nin babası kazağını giymek istedi. Ama çadırı kurarken elleri çok kirli olmuştu. "Temiz kazağı kirletmek istemiyorum," dedi babası. Hello Kitty kurabiye yapmadan önce ellerini hep suyla yıkardı. Bunu düşündü, hemen şişeyle su getirdi ve babasının ellerine döktü. Babası ellerini güzelce yıkadı. "Baba, kazağı sana ben giydireyim mi?" diye sordu Hello Kitty. "Teşekkürler, kızım, ellerim artık temiz, kendim giyerim," dedi babası. Babası kazağını giydi ve kazak tertemiz kaldı. Sonra gülerek Hello Kitty'ye sarıldı. Hello Kitty bundan sonra kirli elleri görünce hemen su getirmeye başladı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kurabiye yapmadan önce"
   - Cümle 5: «Hello Kitty kurabiye yapmadan önce ellerini hep suyla yıkardı.»
   - Açıklama: Tohumdaki kurabiye yapma özelliği yalnız dolaylı bir anı olarak anılıyor, karttaki gibi kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kazağı sana ben giydireyim mi"
   - Cümle 8: «"Baba, kazağı sana ben giydireyim mi?" diye sordu Hello Kitty.»
   - Açıklama: Eller zaten yıkanmışken kazağı giydirme teklifi işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0016` birebir aynı, `@degisim: mercan -> kazak` (tutuyorsan), ardından `@onarim: 61244d16dc3e9c750405b894d3819c7da8c14616`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0017 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0017
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'klasör', fiil 'bitmek', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: rüzgar kurabiye torbasını sepetten uçurdu | hışırtının geldiği yere yürüdü ve torbayı buldu
@tohum: hello_kitty-0017
@degisim: klasör -> torba
Hello Kitty annesiyle parkta piknik yapıyordu. Sepete baktı ama kurabiye torbası yerinde yoktu. Rüzgar torbayı sepetten uçurmuştu. "Anne, kurabiyelerimiz kayboldu!" dedi Hello Kitty. "Gel, birlikte arayalım," dedi annesi. Birden çiçeklerin arasından hışır hışır bir ses geldi. Hello Kitty bu sesi çok merak etti. Sese doğru yürüdü ve tatlı bir koku duydu. Hello Kitty kokuyu hemen tanıdı, çünkü kurabiye yapmayı çok severdi. Çiçeklerin arasında onların kıpkırmızı torbası duruyordu. Rüzgar esince kağıt torba ses çıkarıyordu. Hello Kitty torbayı aldı ve annesine gösterdi. Hello Kitty çok sevindi, çünkü piknik bitmeden kurabiyelerini bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty kokuyu hemen tanıdı, çünkü kurabiye yapmayı çok severdi"
   - Cümle 9: «Hello Kitty kokuyu hemen tanıdı, çünkü kurabiye yapmayı çok severdi.»
   - Açıklama: Koku ve kurabiye yapma sevgisi çözüme bir şey katmıyor; torba zaten hışırtıyla bulunuyor ve ayrıntı işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0017` birebir aynı, `@degisim: klasör -> torba` (tutuyorsan), ardından `@onarim: 17532a8ecacd6d31888119155afe66a0a9b6b194`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0019 (deneme 4 -> 5)

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
Ağaçlarda kuşlar ötüyordu. Hello Kitty büyüklerle ormandaki kamp yerinde, çadırın önündeydi. Çantasına baktı ama kurabiye kutusu yoktu. Çantanın kapağı açık kalmıştı ve kutu bir yere düşmüştü. Kutuda evde yaptığı yıldız kurabiyeleri vardı. Hello Kitty çantayı az önce çadırın içinde açmıştı. Çadırın içi biraz karanlıktı. Hello Kitty girişteki feneri açtı ve içeri tuttu. Işıkta köşedeki küçük kutuyu gördü. Bu, onun kurabiye kutusuydu! Hello Kitty feneri yere oturttu ve kutuyu iki eliyle çıkardı. Kurabiyelerin hepsi kutuda yerindeydi. Hello Kitty bir kurabiye aldı ve kutuyu kapattı. Sonra çadırın önüne oturdu ve kurabiyesini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Hello Kitty büyüklerle ormandaki"
   - Cümle 2: «Hello Kitty büyüklerle ormandaki kamp yerinde, çadırın önündeydi.»
   - Açıklama: Kartın yanlar bölümünde olmayan belirsiz 'büyükler' hikayeye ekleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty feneri yere oturttu"
   - Cümle 11: «Hello Kitty feneri yere oturttu ve kutuyu iki eliyle çıkardı.»
   - Açıklama: Fener için 'oturtmak' uygun değil; 'yere koydu' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "feneri yere oturttu"
   - Cümle 11: «Hello Kitty feneri yere oturttu ve kutuyu iki eliyle çıkardı.»
   - Açıklama: Fener oturtulmaz; 'yere koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0019` birebir aynı, `@degisim: gizemli -> küçük` (tutuyorsan), ardından `@onarim: 74873fea4ea1ca373e56dffc9f1486a5ab2c78bf`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0021 (deneme 4 -> 5)

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
@plan: rüzgar kağıdı kaldırdı ve kağıt yüksek bir dala takıldı | annesinden yardım istedi ve annesi kağıdı daldan aldı
@tohum: hello_kitty-0021
@degisim: değiştirmek -> tutmak
Rüzgar hızlı hızlı esiyordu. Hello Kitty parkta boyalarla resim yapıyordu, annesi de tuzlu kraker yiyordu. Birden rüzgar kağıdı havaya kaldırdı ve kağıt yüksek bir dala takıldı. Hello Kitty zıpladı ama dala uzanamadı. "Anne, kağıdı daldan alır mısın?" diye sordu Hello Kitty. "Hemen alırım," dedi annesi. Annesi uzandı ve kağıdı daldan dikkatlice aldı. Hello Kitty kağıdı yere koydu ve bir köşesini sıkıca tuttu. Annesi de kraker kutusunu öteki köşeye koydu. Kağıt artık uçmadı. Hello Kitty resmine annesini ve kendisini iki arkadaş gibi el ele çizdi. "Anneciğim, bu resim senin, teşekkürler!" dedi Hello Kitty.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "annesinden yardım istedi ve annesi kağıdı daldan aldı"
   - Cümle 0 (plan satırı): «rüzgar kağıdı kaldırdı ve kağıt yüksek bir dala takıldı | annesinden yardım istedi ve annesi kağıdı daldan aldı»
   - Açıklama: Gövdede annesi kağıdı daldan almıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kağıdı yere koydu ve bir köşesini sıkıca tuttu"
   - Cümle 8: «Hello Kitty kağıdı yere koydu ve bir köşesini sıkıca tuttu.»
   - Açıklama: Kağıt alındıktan sonra çözüm köşe tutma ve kraker kutusu koyma adımlarıyla ikiden fazla adıma uzuyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Annesi de kraker kutusunu öteki köşeye koydu"
   - Cümle 9: «Annesi de kraker kutusunu öteki köşeye koydu.»
   - Açıklama: Kağıt daldan alındıktan sonra çözüm ek adımlarla sürüyor ve ikinci bir sabitleme işine dönüşüyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "iki arkadaş gibi el ele"
   - Cümle 11: «Hello Kitty resmine annesini ve kendisini iki arkadaş gibi el ele çizdi.»
   - Açıklama: Tohum özelliği (yeni arkadaş edinmek) yalnız benzetme olarak geçiyor, olayda işe yaramıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "annesini ve kendisini iki arkadaş gibi"
   - Cümle 11: «Hello Kitty resmine annesini ve kendisini iki arkadaş gibi el ele çizdi.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği sona eklenmiş, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0021` birebir aynı, `@degisim: değiştirmek -> tutmak` (tutuyorsan), ardından `@onarim: 99de0841dc6f9ac3ac1a6170a5b61b599244f8e0`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0022 (deneme 3 -> 4)

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
Evin mutfağında Hello Kitty ile Mimi masadaki tabağa baktı. Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı. İkisi de onu yemek istiyordu, ama tabakta başka kurabiye yoktu. Mimi utangaçtı ve hiçbir şey söylemedi. "Mimi, bu kurabiyeyi seninle paylaşmak istiyorum," dedi Hello Kitty. "İki parça aynı büyüklükte olur mu?" diye sordu Mimi. Hello Kitty çok kurabiye yapmıştı ve ne yapacağını biliyordu. Çekmeceden bir cetvel aldı. Cetveli kurabiyenin tam ortasına koydu. Sonra kurabiyeyi cetvelin kenarından yavaşça ikiye kırdı. İki parça tam aynı boydaydı. Hello Kitty bir parçayı Mimi'ye verdi. İki kardeş yan yana oturdu ve parçalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty çok kurabiye yapmıştı"
   - Cümle 7: «Hello Kitty çok kurabiye yapmıştı ve ne yapacağını biliyordu.»
   - Açıklama: Cümle o an çok kurabiye yaptığı gibi okunuyor; kastedilen daha önce çok kurabiye yapmış olması ve anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0022` birebir aynı, `@degisim: denemek -> yemek` (tutuyorsan), ardından `@onarim: 1b9fa031b7123f1daf413a79db995b9089477b97`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0024 (deneme 3 -> 4)

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
@plan: kırmızı böğürtlenler sertti ve daldan çıkmıyordu | annesine sordu ve siyah yumuşak olanları kopardı
@tohum: hello_kitty-0024
@degisim: pürüzsüz -> düz
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Hello Kitty, çalıdan ilk kez böğürtlen koparmayı denedi. Ama kırmızı böğürtlenler çok sertti ve daldan çıkmıyordu. Hello Kitty böğürtlenleri annesinin elmalı turtasına koymak istiyordu. Yaprakların arasında siyah ve yumuşak böğürtlenler de vardı. "Anne, siyah olanları koparabilir miyim?" diye sordu Hello Kitty. "Evet, siyah olanlar daha tatlı," dedi annesi. Hello Kitty siyah bir tanesine hafifçe dokundu ve o hemen koptu. Sonra birkaç tane daha kopardı. Böğürtlenleri turtanın üstüne düz bir sıra olarak dizdi. "Turtamız çok güzel oldu!" dedi annesi. İkisi gölgeye oturdu ve Hello Kitty'nin en sevdiği turtayı mutlu mutlu paylaştı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çalıdan ilk kez böğürtlen koparmayı"
   - Cümle 2: «Hello Kitty, çalıdan ilk kez böğürtlen koparmayı denedi.»
   - Açıklama: Ormanda çalıdan yabani meyve koparıp yemek çocuğun taklit edebileceği tehlikeli bir davranış.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çalıdan ilk kez böğürtlen koparmayı denedi"
   - Cümle 2: «Hello Kitty, çalıdan ilk kez böğürtlen koparmayı denedi.»
   - Açıklama: Ormanda çalıdan yabani meyve koparmak çocuğun taklit edebileceği tehlikeli bir davranış.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kırmızı böğürtlenler çok sertti"
   - Cümle 3: «Ama kırmızı böğürtlenler çok sertti ve daldan çıkmıyordu.»
   - Açıklama: Kırmızı böğürtlenlerin neden sert olduğu (olgunlaşmamış olmaları) söylenmiyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve o hemen koptu"
   - Cümle 8: «Hello Kitty siyah bir tanesine hafifçe dokundu ve o hemen koptu.»
   - Açıklama: 'o' zamiri Hello Kitty'den hemen sonra geliyor ve böğürtleni gösterdiği tam belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0024` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: 001a818d5002da0457a479ba6d17055903215c3a`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0028 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0028
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kavun', fiil 'sıkılmak', sıfat 'değerli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: ağacın altından garip bir ses geldi | turtasına baktı ve kavuna düşen kozalağı gördü
@tohum: hello_kitty-0028
@degisim: değerli -> küçük
Bir sabah Hello Kitty büyüklerle ormandaki kamp yerinde piknik yapıyordu. Birden yakındaki bir ağacın altından garip bir ses geldi: tok, tok. Hello Kitty bu sesi çok merak etti. Sepeti de o ağacın altında duruyordu. Sepette kocaman bir kavun ve en sevdiği elmalı turta vardı. Hello Kitty önce turtasına baktı. Turtanın üstünde küçük bir kozalak vardı. Hello Kitty başını kaldırdı ve ağaca baktı. Tam o sırada ağaçtan bir kozalak düştü ve kavuna çarptı: tok! Sesi yapan, düşen kozalaklardı. Hello Kitty kozalağı turtadan aldı ve sepeti açık bir yere çekti. Hello Kitty hiç sıkılmadı ve çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağacın altından garip bir ses geldi"
   - Cümle 2: «Birden yakındaki bir ağacın altından garip bir ses geldi: tok, tok.»
   - Açıklama: Sorun yalnız merak edilen bir ses; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty hiç sıkılmadı"
   - Cümle 12: «Hello Kitty hiç sıkılmadı ve çok sevindi, çünkü sesin nereden geldiğini bulmuştu.»
   - Açıklama: 'sıkılmadı' olaya uymuyor; Hello Kitty'nin sıkılması için bir neden yoktu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0028` birebir aynı, `@degisim: değerli -> küçük` (tutuyorsan), ardından `@onarim: c5a97e0ac3dd6d71a0dbbea643f914b73433f316`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0029 (deneme 3 -> 4)

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
Hello Kitty ile Mimi mutfakta sıcak çorbalarını içiyordu. Dışarısı çok rüzgarlıydı. Birden kapı rüzgarla açıldı ve içeri soğuk hava doldu. Hello Kitty kaşığını bıraktı ve kapıya gitti. Kapıyı itti, ama rüzgar çok güçlüydü ve kapı kapanmadı. Hello Kitty en iyi arkadaşı olan kardeşine döndü. "Mimi, lütfen bana yardım eder misin?" diye sordu Hello Kitty. Mimi gülümsedi ve hemen kardeşinin yanına koştu. İkisi "Bir, iki, üç!" diye saydı ve kapıyı birlikte itti. Kapı yavaşça kapandı. Mutfak yine sıcacık oldu. İkisi masaya döndü ve çorbalarını bitirdi. "Teşekkürler, Mimi, çok yardımcı oldun!" dedi Hello Kitty.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı olan kardeşine"
   - Cümle 6: «Hello Kitty en iyi arkadaşı olan kardeşine döndü.»
   - Açıklama: İlk cümlede tanıtılan Mimi burada yeniden tanıtılıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı olan kardeşine döndü"
   - Cümle 6: «Hello Kitty en iyi arkadaşı olan kardeşine döndü.»
   - Açıklama: Baştan tanıtılmış Mimi burada yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşı olan kardeşine"
   - Cümle 6: «Hello Kitty en iyi arkadaşı olan kardeşine döndü.»
   - Açıklama: Tohum özelliği yeni arkadaş edinmek; 'arkadaş' yalnız Mimi'nin kart ilişkisini anlatıyor, özellik işe yaramıyor.
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, yalnız Mimi'nin ilişkisi tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0029` birebir aynı, ardından `@onarim: 13a75bb25a67aa4b6092432d6a9b22c3f86a9337`, sonra gövde.
