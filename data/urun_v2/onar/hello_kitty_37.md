# Editör görevi (onarım): Hello Kitty, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0143 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0143
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'demet', fiil 'doldurmak', sıfat 'uyanık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: topla oynarken babasının meyve suyunu döktü | özür diledi ve bardağı yeniden doldurdu
@tohum: hello_kitty-0143
@degisim: demet -> bardak
Hello Kitty babasıyla parkta, ağacın gölgesinde piknik yapıyordu. Babası örtünün üstünde uzanmış, dinleniyordu. Hello Kitty topla oynarken top babasının bardağına çarptı ve meyve suyu döküldü. Soğuk meyve suyu babasının eline döküldü. "Eyvah, elim ıslandı, ama artık uyanık oldum!" dedi babası. Hello Kitty babasının yanına koştu. "Özür dilerim, babacığım, hiç dikkat etmedim," dedi Hello Kitty. Hello Kitty en sevdiği elmalı turtadan bir dilim de babasına verdi. Sonra şişeyi aldı ve bardağı yeniden doldurdu. Babası turtayı yedi, meyve suyunu içti ve kızına sarıldı. İkisi pikniklerine mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Soğuk meyve suyu babasının eline döküldü"
   - Cümle 4: «Soğuk meyve suyu babasının eline döküldü.»
   - Açıklama: Meyve suyunun döküldüğü bir önceki cümlede zaten söylendi.
   - Açıklama: Meyve suyunun döküldüğü bir önceki cümlede zaten söylendi, gereksiz tekrar.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama artık uyanık oldum"
   - Cümle 5: «"Eyvah, elim ıslandı, ama artık uyanık oldum!" dedi babası.»
   - Açıklama: Babası uyumuyordu, dinleniyordu; 'uyanık oldum' yanlış ve 'uyanık' zeki anlamına da gelir.
   - Açıklama: 'Uyanık oldum' yanlış kullanım; 'uyandım' olmalı.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "elmalı turtadan bir dilim de babasına verdi"
   - Cümle 8: «Hello Kitty en sevdiği elmalı turtadan bir dilim de babasına verdi.»
   - Açıklama: Özür ve bardağı doldurmanın yanına turta vermek de ekleniyor; çözüm iki adımı aşıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği elmalı turtadan bir dilim"
   - Cümle 8: «Hello Kitty en sevdiği elmalı turtadan bir dilim de babasına verdi.»
   - Açıklama: Turta daha önce hiç kurulmadan sebepsizce beliriyor ve çözüme gerekmeyen fazladan bir adım ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0143` birebir aynı, `@degisim: demet -> bardak` (tutuyorsan), ardından `@onarim: 78c2495b8c1570881ff2f901f0f0ece2bb8eda1d`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0144 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0144
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'pul', fiil 'ovmak', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: camın üstü su damlalarıyla doluydu ve kar görünmüyordu | kurabiye kalıbını cama tuttu ve içini ovdu
@tohum: hello_kitty-0144
@degisim: pul -> kalıp
Dışarıda sessizce kar yağıyordu. Hello Kitty mutfaktaki pencereden kara bakmak istedi. Ama mutfak çok sıcaktı ve camın üstü su damlalarıyla doluydu. Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi. Kalıp plastikti, bu yüzden cam için güvenliydi. Hello Kitty kalıbı cama tuttu ve içini parmağıyla yavaşça ovdu. Camda yıldız şeklinde küçük, temiz bir yer açıldı. Hello Kitty yıldızın içinden dışarıya baktı. Beyaz kar taneleri yavaş yavaş yere düşüyordu. Hello Kitty karı görünce çok sevindi. Hello Kitty bundan sonra cam ıslanınca kalıpla camda bir yıldız açardı.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yıldız şeklindeki kurabiye kalıbını"
   - Cümle 4: «Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi.»
   - Açıklama: Tohumdaki özellik kurabiye yapmayı sevmek; hikayede yalnız bir kalıp eşyası geçiyor, özellik kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yıldız şeklindeki kurabiye kalıbını getirdi"
   - Cümle 4: «Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi.»
   - Açıklama: Tohumdaki özellik kurabiye yapmayı sevmek; burada yalnız kalıp bir alet olarak kullanılıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "cam için güvenliydi"
   - Cümle 5: «Kalıp plastikti, bu yüzden cam için güvenliydi.»
   - Açıklama: 'Güvenli' soyut bir kavram ve küçük çocuğa açıklamasız kalıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu yüzden cam için güvenliydi"
   - Cümle 5: «Kalıp plastikti, bu yüzden cam için güvenliydi.»
   - Açıklama: 'Güvenli' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kalıp plastikti, bu yüzden cam için güvenliydi"
   - Cümle 5: «Kalıp plastikti, bu yüzden cam için güvenliydi.»
   - Açıklama: Kalıbın plastik ve güvenli olduğu ayrıntısı olayda işe yaramıyor ve kalıp çözüme sebepsizce getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0144` birebir aynı, `@degisim: pul -> kalıp` (tutuyorsan), ardından `@onarim: 5882dd720a11a6be6e5902c3862a832baa2d92b8`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0145 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0145
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'etiket', fiil 'kıvrılmak', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: kardan kedinin yüzündeki dal aşağı kıvrılmıştı | dalı ters çevirip gülen bir yüz yaptı
@tohum: hello_kitty-0145
@degisim: etiket -> düğme
Kar yavaş yavaş yağıyordu. Hello Kitty parkta ağır kar toplarıyla kardan bir kedi yapıyordu. Ama yüzüne koyduğu dalın ucu aşağı kıvrılmıştı. Kardan kedi bu yüzden çok üzgün görünüyordu. Hello Kitty yeni arkadaşlar edinmeyi çok severdi. Kardan kedinin de mutlu olmasını istedi. Dalı karın içinden çekip çıkardı ve ters çevirdi. Sonra dalı yeniden karın içine bastırdı. Artık dalın ucu yukarı bakıyordu. Kardan kedinin yüzü şimdi gülen bir yüzdü. Hello Kitty yerden üç küçük taş buldu ve onları kedinin düğmeleri yaptı. Hello Kitty kardan kedinin yanında karda mutlu mutlu oynadı.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty parkta ağır kar toplarıyla"
   - Cümle 2: «Hello Kitty parkta ağır kar toplarıyla kardan bir kedi yapıyordu.»
   - Açıklama: Küçük çocuk parkta tek başına ve büyüksüz; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama yüzüne koyduğu dalın"
   - Cümle 3: «Ama yüzüne koyduğu dalın ucu aşağı kıvrılmıştı.»
   - Açıklama: 'Yüzüne' zamirinin Hello Kitty'yi mi kardan kediyi mi gösterdiği belli değil.
   - Açıklama: 'Yüzüne' zamirinin Hello Kitty'nin mi kardan kedinin mi yüzünü gösterdiği belli değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 5: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: 'Arkadaş edinmek' soyut bir ifade olup 3 yaşındaki çocuğun bileceği bir kelime değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 5: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: Tohumdaki arkadaş özelliği karttan liste gibi sayılıyor; kardan kedi yeni bir arkadaş değil, özellik işe yarar biçimde kullanılmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yerden üç küçük taş buldu"
   - Cümle 11: «Hello Kitty yerden üç küçük taş buldu ve onları kedinin düğmeleri yaptı.»
   - Açıklama: Sorun çözüldükten sonra taşlar sebepsiz beliriyor ve düğme ayrıntısı olaya hiçbir şey katmıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty yerden üç küçük taş buldu"
   - Cümle 11: «Hello Kitty yerden üç küçük taş buldu ve onları kedinin düğmeleri yaptı.»
   - Açıklama: Sorun çözüldükten sonra gelen taş düğmeler olaya bağlı olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0145` birebir aynı, `@degisim: etiket -> düğme` (tutuyorsan), ardından `@onarim: 07d6e1f6cabc70e9a5707ee7bed35bdcabb1e3a7`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0147
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'balon', fiil 'koklamak', sıfat 'soslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: kardeşi kurabiyeleri kokladı ama utandığı için istemedi | sos kasesini ortaya koyup kardeşini birlikte yapmaya çağırdı
@tohum: hello_kitty-0147
@degisim: balon -> kase
Evin mutfağında tatlı bir koku vardı. Hello Kitty kurabiyelere çikolata sosu dökerken Mimi kapıdan onu izliyordu. Mimi kurabiyeleri kokladı ama utangaç olduğu için bir şey istemedi. Hello Kitty bunu gördü. "Mimi, gel, soslu kurabiyeleri birlikte yapalım!" dedi Hello Kitty. Sos kasesini masanın ortasına koydu ve kurabiyelerin yarısını Mimi'ye verdi. Mimi de kendi kurabiyelerini süsledi. Birlikte kalpli ve yıldızlı kurabiyeler yaptılar. "Teşekkürler, Hello Kitty, seninle yapmak çok güzel!" dedi Mimi. İkisi kurabiyelerden birer tane yedi ve güldü. Hello Kitty bundan sonra kurabiye yaparken hep Mimi'yi de çağırdı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Birlikte kalpli ve yıldızlı kurabiyeler yaptılar"
   - Cümle 8: «Birlikte kalpli ve yıldızlı kurabiyeler yaptılar.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kurabiye bir büyükle yapılır ama mutfakta yalnız iki çocuk var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0147` birebir aynı, `@degisim: balon -> kase` (tutuyorsan), ardından `@onarim: 8e2f43ea4ffcd22bd3e282d0de1854045ae61a94`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0148 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0148
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'tost', fiil 'yapıştırmak', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: ormanda tatlı bir koku vardı | kokuya doğru yürüyüp turuncu çiçekleri buldu
@tohum: hello_kitty-0148
@degisim: yapıştırmak -> koklamak
Ormandaki kamp yerinde hava serindi. Hello Kitty tostunu yerken tatlı bir koku duydu. Kokunun nereden geldiğini çok merak etti. Önce tostunu kokladı, ama tost yalnız peynir kokuyordu. Hello Kitty kurabiye yapmayı çok severdi ve kurabiyelerine hep bal koyardı. Bu yüzden bal kokusunu hemen tanıdı. Hello Kitty kokuya doğru yavaşça birkaç adım attı. Çadırın hemen yanında turuncu çiçekler vardı. Hello Kitty eğildi ve çiçekleri kokladı. Koku bu çiçeklerden geliyordu. Hello Kitty çok sevindi, çünkü kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tatlı bir koku duydu"
   - Cümle 2: «Hello Kitty tostunu yerken tatlı bir koku duydu.»
   - Açıklama: Tatlı bir koku duymak gerçek bir sorun değil; ortada çözülmesi gereken bir güçlük yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kokunun nereden geldiğini çok merak etti"
   - Cümle 3: «Kokunun nereden geldiğini çok merak etti.»
   - Açıklama: Tatlı bir kokunun nereden geldiğini merak etmek gerçek bir sorun değil; ortada çözülmesi gereken bir güçlük yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden bal kokusunu hemen tanıdı"
   - Cümle 6: «Bu yüzden bal kokusunu hemen tanıdı.»
   - Açıklama: Bal kokusunu tanıma ayrıntısı kurulup kullanılmıyor, çünkü koku baldan değil turuncu çiçeklerden çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0148` birebir aynı, `@degisim: yapıştırmak -> koklamak` (tutuyorsan), ardından `@onarim: b43bbd9fda3a369827f45c17f80b9af483f7e31f`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0149 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0149
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'saat', fiil 'beklemek', sıfat 'çabuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: top çabuk atılınca annesinin meyve suyu döküldü | özür diledi ve annesine yeni bardak doldurdu
@tohum: hello_kitty-0149
@degisim: saat -> bardak
Hello Kitty parkta annesiyle piknik yapıyordu. Topunu çok çabuk attı ve top annesinin bardağına çarptı. Bardak devrildi ve meyve suyu örtüye döküldü. Annesi boş bardağına baktı ve biraz üzüldü. Hello Kitty hiç beklemedi ve annesinin yanına koştu. "Özür dilerim, anneciğim, topu bakmadan attım," dedi Hello Kitty. Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı. Peçeteyle örtüyü sildi. Şişeden bardağa yeni meyve suyu doldurdu ve iki eliyle annesine verdi. Annesi gülümsedi ve Hello Kitty'ye sarıldı. "Teşekkürler, Hello Kitty, gel birlikte içelim," dedi annesi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "herkese hep iyi davranırdı"
   - Cümle 7: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Olaydan kopuk, soyut bir genel nitelendirme cümlesi.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı"
   - Cümle 7: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Ad art arda cümlelerde gereksiz yere tekrarlanıyor ve olaya katkısı olmayan bir cümle araya sokulmuş.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı"
   - Cümle 7: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Tohumdaki özellik olaya işlenmeden karttaki cümle gibi ayrıca sayılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı"
   - Cümle 7: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Olay akışını kesen, olaydan çıkmayan işlevsiz bir özellik cümlesi araya giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0149` birebir aynı, `@degisim: saat -> bardak` (tutuyorsan), ardından `@onarim: 6330cdc2bd387541b885d87f1db675a35f359e58`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0150 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0150
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'sünger', fiil 'eklemek', sıfat 'karışık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: oyun turtası çok karışık oldu | yaprakları alıp üstüne elma dilimleri dizdi
@tohum: hello_kitty-0150
Parkta ağacın gölgesinde Hello Kitty ile Mimi turta yapma oyunu oynuyordu. Temiz, sarı bir sünger onların turtasıydı. Mimi turtaya yaprak ve dal ekledi, ama turta çok karışık oldu. "Bu hiç turta gibi olmadı," dedi Mimi. Hello Kitty en çok elmalı turtayı severdi. Yaprakları ve dalları turtanın üstünden aldı. Sonra sepetten elma dilimlerini çıkardı. Dilimleri turtanın üstüne yan yana dizdi. "Şimdi gerçek bir elmalı turta gibi oldu!" dedi Mimi. İkisi turtayı örtünün ortasına koydu ve güldü. Hello Kitty bundan sonra oyun turtasına yalnız elma ekledi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama turta çok karışık oldu"
   - Cümle 3: «Mimi turtaya yaprak ve dal ekledi, ama turta çok karışık oldu.»
   - Açıklama: Süngerden oyun turtasının karışık görünmesi çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra sepetten elma dilimlerini çıkardı"
   - Cümle 7: «Sonra sepetten elma dilimlerini çıkardı.»
   - Açıklama: Sepet ve elma dilimleri önceden kurulmadan çözümü getirmek için beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0150` birebir aynı, ardından `@onarim: 8d18ca35a054d143defccdc842f56fded6cf0321`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0151
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'karpuz', fiil 'seçmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesinin karpuz dilimi elinden kaydı ve yere düştü | kendi dilimini annesiyle paylaştı
@tohum: hello_kitty-0151
Bir sabah Hello Kitty ile annesi parkta komik bir karpuz oyunu oynuyordu. Gözleri kapalı birer dilim seçtiler ve Hello Kitty kocaman dilimi buldu. Ama annesinin dilimi elinden kaydı ve yere düştü. Annesinin hiç karpuzu kalmadı. Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı. Dilimini elleriyle ikiye böldü. Büyük parçayı annesine verdi. Annesi gülümsedi ve Hello Kitty'ye sarıldı. Sonra ikisi yan yana oturup karpuz yedi. Hello Kitty çok sevindi, çünkü kocaman dilim ikisine de yetti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı"
   - Cümle 5: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Tohumdaki özellik olaya işlenmeden karttaki cümle gibi ayrıca sayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0151` birebir aynı, ardından `@onarim: 78a44981d8e134abf262f3c421ae871c6043b3c6`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0152 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0152
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'köpük', fiil 'serpmek', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: çiçekler kuruydu ve kelebekler yakına gelmiyordu | çiçeklere su serpti ve kelebekler yakına geldi
@tohum: hello_kitty-0152
@degisim: köpük -> su
Bir sabah orman bulutlu ve serindi. Hello Kitty kamp yerinde uçan sarı kelebekler gördü. Ama çiçekler kuruydu ve kelebekler hep uzakta uçuyordu. Hello Kitty yeni arkadaşlar edinmeyi çok severdi. Çantasından su şişesini aldı ve suyu avucuna döktü. Suyu damla damla ve yavaşça çiçeklerin üstüne serpti. Sonra sessizce bekledi. Biraz sonra kelebekler ıslak çiçeklere geldi. Kelebekler çiçeklerden su içti ve Hello Kitty'nin hemen yanında uçtu. Hello Kitty yeni arkadaşlarını izleyerek çiçeklerin yanında mutlu mutlu oturdu.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde uçan"
   - Cümle 2: «Hello Kitty kamp yerinde uçan sarı kelebekler gördü.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda yalnız.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 4: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: 'Arkadaş edinmek' soyut ve 3 yaşındaki çocuğun bilmediği bir ifade.
   - Açıklama: 'Arkadaş edinmek' soyut bir kalıp ve 3 yaşındaki çocuğun bilmeyeceği bir kelime içeriyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Kelebekler çiçeklerden su içti"
   - Cümle 9: «Kelebekler çiçeklerden su içti ve Hello Kitty'nin hemen yanında uçtu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, olaya katılıyor.
   - Açıklama: Arka plandaki çoğul canlı kelebekler olaya katılıyor ve çözümün parçası oluyor.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Hello Kitty yeni arkadaşlarını izleyerek"
   - Cümle 10: «Hello Kitty yeni arkadaşlarını izleyerek çiçeklerin yanında mutlu mutlu oturdu.»
   - Açıklama: Kartın yanlar alanında hayvan arkadaşları yok; kelebekler arkadaş olarak sunuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0152` birebir aynı, `@degisim: köpük -> su` (tutuyorsan), ardından `@onarim: b70a295b0ba349ddf5d3fb8a9ce0aa81b2c6dd1c`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0153
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'fındık', fiil 'kaydetmek', sıfat 'uzun'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: yuvarlak fındıklar turtanın üstünden kayıp düştü | fındıkları parmağıyla hamura bastırdı
@tohum: hello_kitty-0153
@degisim: kaydetmek -> kaymak
Hello Kitty babasıyla mutfakta elmalı turta yapıyordu. Bu kez turtanın üstüne fındık koymayı denedi. Ama yuvarlak fındıklar hamurun üstünden kaydı ve masaya düştü. "Babacığım, fındıklar durmuyor!" dedi Hello Kitty. Hello Kitty en sevdiği turtanın güzel olmasını istedi. Fındıkları tek tek parmağıyla hamura hafifçe bastırdı. Artık hiçbiri kaymadı. Babası uzun hamur şeritlerini turtanın üstüne dizdi. "Çok güzel oldu, kızım!" dedi babası. Sonra babası turtayı fırına koydu. Biraz sonra mutfak elma ve fındık kokusuyla doldu. Hello Kitty çok sevindi, çünkü ilk fındıklı turtası çok güzel olmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ilk fındıklı turtası çok güzel olmuştu"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü ilk fındıklı turtası çok güzel olmuştu.»
   - Açıklama: 'Güzel' ve 'çok güzel' kısa hikayede üç kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0153` birebir aynı, `@degisim: kaydetmek -> kaymak` (tutuyorsan), ardından `@onarim: ec70195f86cc5b416b70ac6f877c00677c12405d`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0154
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'üzüm', fiil 'ulaşmak', sıfat 'berrak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: top yüksek bir dala takıldı | annesinden yardım istedi ve topu geri aldı
@tohum: hello_kitty-0154
Hello Kitty parkta annesiyle top oynuyordu. Gökyüzü berrak ve maviydi. Ama top yükseğe zıpladı ve bir ağacın dalına takıldı. Hello Kitty zıpladı, ama topa ulaşamadı. Annesi ağacın gölgesinde üzüm yiyordu. Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı. Annesinin yanına gitti ve güzelce yardım istedi. Annesi kalktı ve uzun koluyla topu daldan aldı. Hello Kitty annesine sarıldı ve teşekkür etti. Sonra en güzel üzümleri annesine verdi. İkisi üzüm yiyip oyuna devam etti. Hello Kitty çok mutluydu, çünkü topu geri almıştı.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Annesi ağacın gölgesinde üzüm yiyordu"
   - Cümle 5: «Annesi ağacın gölgesinde üzüm yiyordu.»
   - Açıklama: Annesiyle top oynadığı söylenirken annesi aynı anda gölgede üzüm yiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "herkese hep iyi davranırdı"
   - Cümle 6: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Olaydan kopuk, genel ve soyut bir nitelik cümlesi.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı"
   - Cümle 6: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Tohum özelliği olaya katılmadan bir özellik cümlesi olarak sayılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı"
   - Cümle 6: «Hello Kitty arkadaşlarına ve herkese hep iyi davranırdı.»
   - Açıklama: Arkadaşlarına iyi davranma cümlesi olayla bağsız, işlevsiz bir ayrıntı.
   - Açıklama: Özellik cümlesi olayın ortasına işlevsiz bir ayrıntı olarak giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0154` birebir aynı, ardından `@onarim: 0b1545a7f5f34f19832f2cbaa17dc72c2f3f5777`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0155 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0155
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'bağcık', fiil 'okşamak', sıfat 'limonlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: bakmadan oturdu ve kardeşinin kurabiyesini ezdi | özür diledi ve son kurabiyesini kardeşine verdi
@tohum: hello_kitty-0155
Yağmur cama tık tık vuruyordu. Hello Kitty mutfakta bakmadan bir sandalyeye oturdu. Ama sandalyede Mimi'nin limonlu kurabiyesi vardı ve kurabiye ezildi. Mimi bağcığını bağlamak için onu oraya koymuştu. Mimi küçük parçalara baktı ve çok üzüldü. Hello Kitty hemen ayağa kalktı ve kardeşinden özür diledi. Sonra onun başını yavaşça okşadı. Hello Kitty'nin tabağında son bir kurabiye kalmıştı. Onu en iyi arkadaşına, Mimi'ye verdi. Mimi kurabiyeyi ikiye böldü ve yarısını ikizine uzattı. İkisi yağmuru dinleyerek kurabiyelerini yedi. Hello Kitty çok sevindi, çünkü kardeşi yine gülüyordu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu en iyi arkadaşına, Mimi'ye verdi."
   - Cümle 9: «Onu en iyi arkadaşına, Mimi'ye verdi.»
   - Açıklama: Kardeş olarak tanıtılan Mimi burada 'en iyi arkadaşı' diye yeniden tanıtılıyor.
   - Açıklama: Kardeş olarak bilinen Mimi burada 'en iyi arkadaş' diye yeniden tanıtılıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Onu en iyi arkadaşına, Mimi'ye verdi"
   - Cümle 9: «Onu en iyi arkadaşına, Mimi'ye verdi.»
   - Açıklama: Mimi hikaye boyunca kardeş ve ikiz olarak anılırken burada en iyi arkadaş diye tanıtılıyor.
   - Açıklama: Mimi önce kardeşi olarak anılıyor, burada en iyi arkadaşı deniyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yarısını ikizine uzattı"
   - Cümle 10: «Mimi kurabiyeyi ikiye böldü ve yarısını ikizine uzattı.»
   - Açıklama: 'ikizine' ile kimin kastedildiği belirsiz; Hello Kitty'nin ikiz olduğu hiç söylenmedi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0155` birebir aynı, ardından `@onarim: 2139b2e103d22f7d191743db7f9cfb2ccc4de364`, sonra gövde.
