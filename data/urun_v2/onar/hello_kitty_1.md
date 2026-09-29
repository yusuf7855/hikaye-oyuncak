# Editör görevi (onarım): Hello Kitty, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0001 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0001
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kova', fiil 'koşturmak', sıfat 'faydalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar esti ve yapraklar çimenlere dağıldı | yaprakları kovaya topladı ve rüzgardan korudu
@tohum: hello_kitty-0001
Parkta serin bir sabahtı. Hello Kitty ağaçların gölgesinde yapraklardan yeni arkadaşlar yapıyordu. Ama birden rüzgar esti ve yapraklar çimenlere dağıldı. Hello Kitty önce şaşırdı, sonra güldü. Kırmızı kovasını aldı ve çimenlerde koşturdu. Uçan yaprakları tek tek kovaya topladı. Sonra kovayı gölgeye koydu. Rüzgar yine esti ama kovadaki yapraklar uçmadı. Kova, yaprak saçlı komik bir yüze benziyordu. Kova bugün çok faydalı olmuştu. Hello Kitty kovanın yanına oturdu ve mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (9):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yapraklardan yeni arkadaşlar yapıyordu"
   - Cümle 2: «Hello Kitty ağaçların gölgesinde yapraklardan yeni arkadaşlar yapıyordu.»
   - Açıklama: Yapraklardan arkadaş yapılmaz; 'arkadaş' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Yapraklardan arkadaş yapılmaz; kelime anlamca yerinde değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yapraklardan yeni arkadaşlar yapıyordu"
   - Cümle 2: «Hello Kitty ağaçların gölgesinde yapraklardan yeni arkadaşlar yapıyordu.»
   - Açıklama: Kartın özellikler alanındaki yeni arkadaş edinme özelliği yapraktan oyuncak yapmaya dönüşmüş ve sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohum özelliği (arkadaş edinmeyi sevme) karttaki gibi kullanılmıyor; yapraktan arkadaş yapmaya çevrilmiş ve sonra reddedilmiş.
   - Açıklama: Kartın özellikler alanındaki arkadaş edinme özelliği yapraktan oyuncak yapmaya çevrilmiş ve sorunun çözümünde işe yaramıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "birden rüzgar esti ve yapraklar çimenlere dağıldı"
   - Cümle 3: «Ama birden rüzgar esti ve yapraklar çimenlere dağıldı.»
   - Açıklama: Rüzgarın yaprakları dağıtıp toplanması istemdeki önemsiz olay örneğinin aynısı; Hello Kitty de sorunu umursamayıp gülüyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve yapraklar çimenlere dağıldı"
   - Cümle 3: «Ama birden rüzgar esti ve yapraklar çimenlere dağıldı.»
   - Açıklama: Rüzgarın yaprakları dağıtıp onların toplanması önemsiz bir olay; Hello Kitty bile şaşırıp gülüyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Kırmızı kovasını aldı"
   - Cümle 5: «Kırmızı kovasını aldı ve çimenlerde koşturdu.»
   - Açıklama: Kova önceden kurulmadan sebepsizce beliriyor ve çözümü getiriyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "yaprak saçlı komik bir yüze benziyordu"
   - Cümle 9: «Kova, yaprak saçlı komik bir yüze benziyordu.»
   - Açıklama: Kovanın yaprak saçlı bir yüze benzetilmesi 3 yaşındaki çocuk için uygun olmayan bir mecaz.
   - Açıklama: Benzetme ve mecaz 3 yaşındaki çocuğa uygun değil.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Kova, yaprak saçlı komik bir yüze benziyordu"
   - Cümle 9: «Kova, yaprak saçlı komik bir yüze benziyordu.»
   - Açıklama: İşlevsiz bir ayrıntı; olaya hiçbir katkısı yok.
   - Açıklama: Kovanın yüze benzemesi işlevsiz bir ayrıntı.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Kova bugün çok faydalı olmuştu"
   - Cümle 10: «Kova bugün çok faydalı olmuştu.»
   - Açıklama: 'Faydalı' soyut bir kelime ve 3 yaşındaki çocuğun bilmeyeceği bir sözcük.
   - Açıklama: 'Faydalı' soyut bir kavram ve somut bir ders cümlesi değil.
9. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "mutlu mutlu oynamaya devam etti"
   - Cümle 11: «Hello Kitty kovanın yanına oturdu ve mutlu mutlu oynamaya devam etti.»
   - Açıklama: Yapraklardan arkadaş yapma hedefine dönülmüyor; kapanış genel ve olaydan kopuk.
   - Açıklama: Yapraklardan arkadaş yapma hedefine dönülmüyor ve hikaye olaya bağlı bir kapanış olmadan kesiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0001` birebir aynı, ardından `@onarim: 23a17b756fa56d7bedce45488021c90b6f2998cb`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0002 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0002
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'düğüm', fiil 'ilgilenmek', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: kurdelenin düğümü çözüldü ve kurdele kayboldu | kurabiyelere bakıp kurdeleyi hamurun içinde buldu
@tohum: hello_kitty-0002
Güneşli bir sabahtı. Hello Kitty evin mutfağında oyun hamurundan kurabiye yapıyordu. Ama kurdelesinin düğümü çözüldü ve kurdele kayboldu. Hello Kitty masanın altına baktı. Kurdele orada yoktu. Sandalyeye de baktı ama yine bulamadı. Sonra yine kurabiyeleriyle ilgilendi. Bir kurabiyenin içinde kırmızı bir uç vardı. Kurdele hamurun içine düşmüştü! Hello Kitty kurdeleyi hamurdan yavaşça çekti ve güldü. Sonra kurdeleyi başına sıkı bir düğümle bağladı. Hello Kitty kurabiye yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Sonra yine kurabiyeleriyle ilgilendi."
   - Cümle 7: «Sonra yine kurabiyeleriyle ilgilendi.»
   - Açıklama: 'İlgilenmek' soyut bir fiil; 3 yaşındaki çocuk için somut bir eylem değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "yine kurabiyeleriyle ilgilendi"
   - Cümle 7: «Sonra yine kurabiyeleriyle ilgilendi.»
   - Açıklama: 'İlgilendi' soyut bir fiil; 3 yaşındaki çocuk için somut değil.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra yine kurabiyeleriyle ilgilendi."
   - Cümle 7: «Sonra yine kurabiyeleriyle ilgilendi.»
   - Açıklama: 'Yine' art arda iki cümlede gereksiz tekrarlanıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra yine kurabiyeleriyle ilgilendi"
   - Cümle 7: «Sonra yine kurabiyeleriyle ilgilendi.»
   - Açıklama: Kurdele aranarak değil tesadüfen bulunuyor; çözüm sebebe yönelmiyor.
   - Açıklama: Hello Kitty aramayı bırakıyor ve kurdele tesadüfen bulunuyor; çözüm sebebe yönelmiyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Bir kurabiyenin içinde kırmızı bir uç vardı"
   - Cümle 8: «Bir kurabiyenin içinde kırmızı bir uç vardı.»
   - Açıklama: Çözüm figürün eyleminden değil tesadüften çıkıyor.
6. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kurdele hamurun içine düşmüştü"
   - Cümle 9: «Kurdele hamurun içine düşmüştü!»
   - Açıklama: Kurdelenin hamurun içine düşmesi önemsiz ve zorlama bir sorun.
   - Açıklama: Kurdelenin hamurun içine düşmesi yönergede örnek verilen önemsiz ve saçma bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0002` birebir aynı, ardından `@onarim: 05ce3b6d508c26d3817b2ba0bfc08f2a03eac6e8`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0005 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0005
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'yosun', fiil 'değmek', sıfat 'eskimiş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: eskimiş kalıp bozuktu ve kurabiyeler komik çıktı | bardağın ağzıyla yuvarlak kurabiyeler kesti
@tohum: hello_kitty-0005
@degisim: yosun -> bardak
Bir sabah Hello Kitty ile Mimi mutfakta oyun hamuruyla oynuyordu. İkisi hamurdan kurabiyeler yapıyordu. Ama eskimiş kalp kalıbı bozuktu ve kurabiyeler komik şekillerde çıkıyordu. Mimi bir kurabiyeyi gösterdi ve utanarak güldü. "Bu kurabiye bir patatese benziyor," dedi Mimi. Hello Kitty biraz düşündü ve masadaki bardağı aldı. Bardağın ağzını hamura yavaşça bastırdı. Bardak hamura değince yuvarlak bir kurabiye çıktı. "Şimdi sen dene, Mimi," dedi Hello Kitty. Mimi de bardakla yuvarlak bir kurabiye yaptı. İkisi masayı yuvarlak kurabiyelerle doldurdu. "Teşekkürler, Hello Kitty, bu oyun çok eğlenceli!" dedi Mimi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kurabiyeler komik şekillerde çıkıyordu"
   - Cümle 3: «Ama eskimiş kalp kalıbı bozuktu ve kurabiyeler komik şekillerde çıkıyordu.»
   - Açıklama: Oyun hamurundan komik şekilli kurabiyeler çıkması gerçek bir sorun değil, Mimi buna gülüyor bile.
   - Açıklama: Oyun hamurundan kurabiyelerin komik şekilli çıkması gülünen önemsiz bir olay, gerçek bir sorun değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "masadaki bardağı aldı"
   - Cümle 6: «Hello Kitty biraz düşündü ve masadaki bardağı aldı.»
   - Açıklama: Masa kaybolduğu söylendikten sonra masadaki bardak alınıyor ve masa kurabiyelerle dolduruluyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "masayı yuvarlak kurabiyelerle doldurdu"
   - Cümle 11: «İkisi masayı yuvarlak kurabiyelerle doldurdu.»
   - Açıklama: 'Yuvarlak kurabiye' art arda üç cümlede tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0005` birebir aynı, `@degisim: yosun -> bardak` (tutuyorsan), ardından `@onarim: 59a95c5fe33a34f0dc0e34a6ebdd22eb25cabdb0`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0007 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0007
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'çerçeve', fiil 'saçmak', sıfat 'keyifli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: şekeri yukarıdan saçtı ve rüzgar şekeri uçurdu | eğilip şekeri kurabiyelerin hemen üstüne saçtı
@tohum: hello_kitty-0007
Hello Kitty parkta annesiyle keyifli bir piknik yapıyordu. Oyunda çimenler mutfaktı ve Hello Kitty tabaktaki kurabiyeleri süslüyordu. Ama renkli şekeri yukarıdan saçtı ve rüzgar şekeri uçurdu. "Şeker uçuyor, kızım!" dedi annesi ve güldü. Hello Kitty tabağın yanına eğildi. Şekeri bu kez kurabiyelerin hemen üstüne yavaşça saçtı. Şeker uçmadı ve kurabiyelerin üstünde kaldı. Sonra kurabiyeleri tabağın kenarına bir çerçeve gibi dizdi. Tabak çok güzel oldu. Hello Kitty tabağı annesine verdi. "Buyur, anneciğim, renkli kurabiyelerin hazır!" dedi Hello Kitty.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Oyunda çimenler mutfaktı"
   - Cümle 2: «Oyunda çimenler mutfaktı ve Hello Kitty tabaktaki kurabiyeleri süslüyordu.»
   - Açıklama: Çimenlerin oyunda mutfak olması soyut bir benzetme; 3 yaşındaki çocuk için anlaşılmaz.
   - Açıklama: Çimenlerin mutfak olması mecazlı bir oyun kurgusudur ve küçük çocuk için anlaşılmaz.
   - Açıklama: Çimenlerin mutfak olması mecazlı bir hayali oyun anlatımı; 3 yaşındaki çocuk için somut değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Oyunda çimenler mutfaktı"
   - Cümle 2: «Oyunda çimenler mutfaktı ve Hello Kitty tabaktaki kurabiyeleri süslüyordu.»
   - Açıklama: Oyun mutfağı kurgusu gerçek piknikle karışıyor ve hikayede hiçbir işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "bir çerçeve gibi dizdi"
   - Cümle 8: «Sonra kurabiyeleri tabağın kenarına bir çerçeve gibi dizdi.»
   - Açıklama: 'Çerçeve gibi' benzetmesi ve 'çerçeve' kelimesi 3 yaşındaki çocuk için uygun değil.
   - Açıklama: Benzetme ve 'çerçeve' kelimesi 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0007` birebir aynı, ardından `@onarim: 87083a19da2adc17d8cffa3fbeaeb3682a6abe4f`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0008
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'perde', fiil 'çekmek', sıfat 'biberli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: ip sıkı değildi ve perde çimenlere düştü | ipi sıkıca çekip ağaca yeniden bağladı
@tohum: hello_kitty-0008
@degisim: biberli -> renkli
Bir sabah Hello Kitty parkta kukla oyunu oynamak istedi. İki ağacın arasına bir ip gerdi ve renkli bir perde astı. Ama ip sıkı değildi ve perde hemen çimenlere düştü. Hello Kitty ipi iki eliyle sıkıca çekti. Sonra ipin ucunu ağaca yeniden bağladı. Perdeyi tekrar astı ve bu kez perde düşmedi. Hello Kitty perdenin arkasına geçti ve kukla oyununa başladı. Oyunda iki kukla yeni arkadaşlar oldu. Hello Kitty çok sevindi, çünkü kukla oyunu sonunda başlamıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iki kukla yeni arkadaşlar oldu"
   - Cümle 8: «Oyunda iki kukla yeni arkadaşlar oldu.»
   - Açıklama: 'Arkadaş olmak' kalıbında çoğul eki kullanılmaz; 'iki kukla arkadaş oldu' olmalı.
   - Açıklama: 'Arkadaş olmak' kalıbında çoğul eki uygun değil; 'arkadaş oldu' olmalı.
   - Açıklama: Doğal kullanım 'arkadaş oldu' olmalı; çoğul 'arkadaşlar oldu' dilbilgisel olarak aksak.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Oyunda iki kukla yeni arkadaşlar oldu"
   - Cümle 8: «Oyunda iki kukla yeni arkadaşlar oldu.»
   - Açıklama: Tohumdaki özellik Hello Kitty'nin arkadaş edinmesidir; burada kuklalar arkadaş oluyor ve özellik sorunu çözmede işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş edinme özelliği Hello Kitty'de değil kuklalarda süs olarak geçiyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0008` birebir aynı, `@degisim: biberli -> renkli` (tutuyorsan), ardından `@onarim: 8544a01a6dfe9304466f3abc5c4cd7b17171795e`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0009 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0009
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'testi', fiil 'oturmak', sıfat 'hareketli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: kütük sallanıyordu çünkü yer düz değildi | düz bir yer buldu ve babasından yardım istedi
@tohum: hello_kitty-0009
@degisim: hareketli -> düz
Ormandaki kamp yerinde hava serindi. Hello Kitty'nin babası çadırı kurmuştu ve çok yorulmuştu. Babası bir kütüğe oturmak istedi ama kütük sallandı, çünkü yer düz değildi. "Bu kütük hiç durmuyor, kızım!" dedi babası ve güldü. Hello Kitty etrafa baktı ve düz bir yer aradı. Ağaçların arasında düz bir yer buldu. "Baba, kütüğü buraya getirelim," dedi Hello Kitty. Babası kütüğü yavaşça oraya yuvarladı. Kütük artık hiç sallanmıyordu. Hello Kitty su testisini getirdi ve kütüğün yanına koydu. "Teşekkürler, benim iyi kalpli kamp arkadaşım," dedi babası. Sonra ikisi kütükte yan yana oturup testiden mutlu mutlu su içti.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Hello Kitty su testisini getirdi"
   - Cümle 10: «Hello Kitty su testisini getirdi ve kütüğün yanına koydu.»
   - Açıklama: Su testisi sebepsiz beliriyor ve sorunla ilgisi olmayan bir ayrıntı olarak ekleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hello Kitty su testisini getirdi"
   - Cümle 10: «Hello Kitty su testisini getirdi ve kütüğün yanına koydu.»
   - Açıklama: Kaybolduğu söylenen testi hiç bulunmadan Hello Kitty tarafından getiriliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "iyi kalpli kamp arkadaşım"
   - Cümle 11: «"Teşekkürler, benim iyi kalpli kamp arkadaşım," dedi babası.»
   - Açıklama: 'İyi kalpli' mecazlı bir ifade ve 3 yaşındaki çocuğun bilmeyebileceği soyut bir niteleme.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "benim iyi kalpli kamp arkadaşım"
   - Cümle 11: «"Teşekkürler, benim iyi kalpli kamp arkadaşım," dedi babası.»
   - Açıklama: 'İyi kalpli' mecazlı bir deyimdir ve 3 yaşındaki çocuk için soyuttur.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "benim iyi kalpli kamp arkadaşım"
   - Cümle 11: «"Teşekkürler, benim iyi kalpli kamp arkadaşım," dedi babası.»
   - Açıklama: Tohumdaki yeni arkadaş edinme özelliği kullanılmıyor, yalnız babasının sözünde arkadaş kelimesi geçiyor.
   - Açıklama: Tohumdaki arkadaş edinme özelliği işe yarar biçimde kullanılmıyor, yalnız babasının sözünde bir hitap kelimesi olarak geçiyor.
   - Açıklama: Kartın özellikler alanındaki yeni arkadaş edinme özelliği kullanılmıyor; kelime yalnız babanın hitabında geçiyor ve işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0009` birebir aynı, `@degisim: hareketli -> düz` (tutuyorsan), ardından `@onarim: 6005b33f7b46909453eb2a16e9a2ae780f228e1e`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0010 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0010
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'yama', fiil 'okumak', sıfat 'kabarık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar esti ve kitabın sayfaları döndü | kaldığı sayfayı bulup araya kurdelesini koydu
@tohum: hello_kitty-0010
@degisim: yama -> kurdele
Hello Kitty parkta kabarık bulutların altında oturuyordu. İlk kez bir kitabı kendisi okumayı deniyordu. Ama rüzgar esti ve kitabın sayfaları hızla döndü. Hello Kitty kaldığı sayfayı bulamadı. Sayfaları tek tek çevirdi ve kaldığı yeri buldu. Sonra kırmızı kurdelesini çıkardı ve o sayfanın arasına koydu. Rüzgar yine esti ama kurdele sayfayı gösteriyordu. Hello Kitty kurdeleli sayfayı hemen açtı. Kitap, yeni arkadaşlar bulan küçük bir kediyi anlatıyordu. Hello Kitty yeni arkadaşları çok sevdiği için bu kitabı keyifle okudu. Hello Kitty bundan sonra dışarıda okurken kaldığı sayfaya kurdelesini koydu.
```

**Hakem bulguları (9):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve kitabın sayfaları hızla döndü"
   - Cümle 3: «Ama rüzgar esti ve kitabın sayfaları hızla döndü.»
   - Açıklama: Sayfaların dönmesi önemsiz bir olay; Hello Kitty sayfaları çevirip hemen buluyor ve sorun kendiliğinden bitiyor.
   - Açıklama: Rüzgarın sayfaları çevirmesi hemen giderilen önemsiz bir olay; yönergedeki rüzgar örneğine benziyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sayfaları tek tek çevirdi ve kaldığı yeri buldu"
   - Cümle 5: «Sayfaları tek tek çevirdi ve kaldığı yeri buldu.»
   - Açıklama: Rüzgarın sayfaları çevirmesi önemsiz bir olay; sayfa hemen bulunuyor ve sorun kendiliğinden bitiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "o sayfanın arasına koydu"
   - Cümle 6: «Sonra kırmızı kurdelesini çıkardı ve o sayfanın arasına koydu.»
   - Açıklama: Tek sayfanın arası olmaz; 'sayfaların arasına' olmalı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kitap, yeni arkadaşlar bulan küçük bir kediyi anlatıyordu"
   - Cümle 9: «Kitap, yeni arkadaşlar bulan küçük bir kediyi anlatıyordu.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız kitabın konusu olarak anılıyor, sorunun çözümünde işe yaramıyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yeni arkadaşları çok sevdiği için"
   - Cümle 10: «Hello Kitty yeni arkadaşları çok sevdiği için bu kitabı keyifle okudu.»
   - Açıklama: 'arkadaşları' kitaptaki kedinin arkadaşlarını mı Hello Kitty'nin arkadaşlarını mı gösteriyor belli değil.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşları çok sevdiği için"
   - Cümle 10: «Hello Kitty yeni arkadaşları çok sevdiği için bu kitabı keyifle okudu.»
   - Açıklama: Tohum özelliği (arkadaş) sorunun çözümünde işe yaramıyor, yalnız kitabın konusu olarak sona eklenmiş; kartın özellik alanındaki kullanım işlevsiz.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşları çok sevdiği için"
   - Cümle 10: «Hello Kitty yeni arkadaşları çok sevdiği için bu kitabı keyifle okudu.»
   - Açıklama: Arkadaş özelliği iki kez ve yalnız söylenerek geçiyor, sorunun çözümünde işe yaramıyor.
8. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bundan sonra dışarıda okurken"
   - Cümle 11: «Hello Kitty bundan sonra dışarıda okurken kaldığı sayfaya kurdelesini koydu.»
   - Açıklama: Son cümle sahneden çıkıp sonraki zamanlara atlıyor.
9. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hello Kitty bundan sonra dışarıda okurken"
   - Cümle 11: «Hello Kitty bundan sonra dışarıda okurken kaldığı sayfaya kurdelesini koydu.»
   - Açıklama: Son cümle o anki sahneden çıkıp sonraki günlere atlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0010` birebir aynı, `@degisim: yama -> kurdele` (tutuyorsan), ardından `@onarim: 428f7ec2ebeb87138d4b631cf6537264f30d804f`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0011 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0011
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'meyve', fiil 'yuvarlanmak', sıfat 'çevik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babasının meyvesi yuvarlandı ve çamura düştü | kendi kurabiyelerini babasıyla paylaştı
@tohum: hello_kitty-0011
Yağmur yeni dinmişti ve çimenler ıslaktı. Hello Kitty ile babası parkta piknik yapıyordu. Babasının meyvesi elinden kaydı, yuvarlandı ve çamura düştü. Hello Kitty çevik adımlarla koştu ama meyveye yetişemedi. "Meyvem çamurlu oldu, kızım!" dedi babası ve komik bir yüz yaptı. Sepette başka meyve yoktu. Hello Kitty kendi kutusunu açtı. Kutuda babasıyla yaptığı kurabiyeler vardı. Hello Kitty kurabiyelerin yarısını babasına verdi. "Buyur, babacığım, birlikte yiyelim," dedi Hello Kitty. Babası bir kurabiye yedi ve gülümsedi. "Paylaşınca kurabiye daha tatlı oluyor," dedi babası. Hello Kitty bundan sonra kurabiyelerini hep babasıyla paylaştı.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Hello Kitty çevik adımlarla koştu"
   - Cümle 4: «Hello Kitty çevik adımlarla koştu ama meyveye yetişemedi.»
   - Açıklama: 'Çevik' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty çevik adımlarla koştu"
   - Cümle 4: «Hello Kitty çevik adımlarla koştu ama meyveye yetişemedi.»
   - Açıklama: Tohumdaki özellik kurabiye; kartın özellikler alanında olmayan çeviklik ikinci bir özellik olarak ekleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Paylaşınca kurabiye daha tatlı oluyor"
   - Cümle 12: «"Paylaşınca kurabiye daha tatlı oluyor," dedi babası.»
   - Açıklama: Paylaşınca kurabiyenin tadı değişmez; bu mecazlı bir anlatım.
   - Açıklama: Paylaşınca kurabiyenin tatlanması mecazdır, somut değildir.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hello Kitty bundan sonra kurabiyelerini hep"
   - Cümle 13: «Hello Kitty bundan sonra kurabiyelerini hep babasıyla paylaştı.»
   - Açıklama: Son cümle zamanı parkın dışına, sonraki günlere atlatıyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bundan sonra kurabiyelerini hep babasıyla paylaştı"
   - Cümle 13: «Hello Kitty bundan sonra kurabiyelerini hep babasıyla paylaştı.»
   - Açıklama: Son cümle sahneden çıkıp ileriki zamanlara atlıyor; tek zaman kuralı çiğneniyor.
6. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hello Kitty bundan sonra kurabiyelerini hep babasıyla paylaştı"
   - Cümle 13: «Hello Kitty bundan sonra kurabiyelerini hep babasıyla paylaştı.»
   - Açıklama: Son cümle piknik sahnesinin dışına, sonraki zamanlara atlıyor.
   - Açıklama: Son cümle parktaki andan çıkıp belirsiz bir geleceğe atlıyor; tek zaman kuralı çiğneniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0011` birebir aynı, ardından `@onarim: b65159281b85027c1236e9ccbe8dd953588bf60e`, sonra gövde.
