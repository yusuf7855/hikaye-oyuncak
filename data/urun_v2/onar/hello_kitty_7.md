# Editör görevi (onarım): Hello Kitty, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar7.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0004 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ağaçların arasından zil gibi ince bir ses geldi | sesin peşinden gitti ve dalda çarpışan kaşıkları buldu
@tohum: hello_kitty-0004
@degisim: ölçmek -> dinlemek
Bir sabah Hello Kitty ile annesi ormandaki kamp yerindeydi. Ilık bir rüzgar esiyordu. Birden ağaçların arasından zil gibi ince bir ses geldi. Hello Kitty bunu çok merak etti. "Anne, bu ses nereden geliyor?" diye sordu Hello Kitty. "Gel, birlikte bakalım," dedi annesi. İkisi çadırın arkasına yürüdü. Hello Kitty orada yeni bir arkadaş olabilir diye düşündü. "Merhaba!" diye seslendi Hello Kitty. Kimse cevap vermedi ama ses yine geldi. Hello Kitty sesi dinledi ve yukarı baktı. Alçak bir dalda, kurusun diye asılan iki kaşık vardı. Rüzgar esince kaşıklar birbirine çarpıyordu. İkisi de çok güldü, çünkü sesi iki kaşık yapıyordu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağaçların arasından zil gibi ince bir ses geldi"
   - Cümle 3: «Birden ağaçların arasından zil gibi ince bir ses geldi.»
   - Açıklama: Sorun gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir kayıp ya da engel yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni bir arkadaş olabilir"
   - Cümle 8: «Hello Kitty orada yeni bir arkadaş olabilir diye düşündü.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir düşünce olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty orada yeni bir arkadaş olabilir diye düşündü"
   - Cümle 8: «Hello Kitty orada yeni bir arkadaş olabilir diye düşündü.»
   - Açıklama: Karttaki arkadaş edinme özelliği yalnız bir düşünce olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0004` birebir aynı, `@degisim: ölçmek -> dinlemek` (tutuyorsan), ardından `@onarim: 692fc9460752186f17480315591752a9f25a4e2d`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0013 (deneme 2 -> 3)

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
Hello Kitty ile annesi parkta düz taşları boyuyordu. Annesi taşına küçük bir kedi yaptı. Ama kalın fırçasıyla kedinin ince bıyıklarını yapamadı. "Bu fırça çok kalın," dedi annesi. Hello Kitty herkese iyi bir arkadaştı, hemen kendi fırçalarına baktı. Onun bir de incecik bir fırçası vardı. "Anne, bu fırçayı sana veriyorum!" dedi Hello Kitty. Annesi fırçayı aldı ve bıyıkları tek tek çizdi. Taşın üstündeki kedi artık çok tatlı görünüyordu. "Teşekkürler, kızım," dedi annesi. Hello Kitty çok mutlu oldu, çünkü fırçasını annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hello Kitty herkese iyi bir arkadaştı, hemen kendi fırçalarına baktı"
   - Cümle 5: «Hello Kitty herkese iyi bir arkadaştı, hemen kendi fırçalarına baktı.»
   - Açıklama: İlgisiz iki yargı virgülle bitiştirilmiş ve 'herkese iyi bir arkadaş' yapısı dilbilgisel olarak bozuk.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iyi bir arkadaştı, hemen kendi fırçalarına baktı"
   - Cümle 5: «Hello Kitty herkese iyi bir arkadaştı, hemen kendi fırçalarına baktı.»
   - Açıklama: İki bağımsız cümle bağlaçsız virgülle birleştirilmiş, cümle bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0013` birebir aynı, `@degisim: yollamak -> vermek` (tutuyorsan), ardından `@onarim: 9c3b7e085ff79149c8f9f0468a916c0937e0ea60`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0014 (deneme 2 -> 3)

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
Bir sabah Hello Kitty parkta köpük balonu yapıyordu. Çubuğu sabunlu suya batırdı ve havada salladı. Ama rüzgar esince balonlar küçükken çubuktan koptu ve uzaklaştı. Hello Kitty yeni arkadaşlar için büyük bir balon yapmak istiyordu. Küçük balonlar çiçeklerin üstünde bir bir patladı. Hello Kitty etrafına baktı ve kalın bir ağaç gördü. Ağacın arkasına geçti, orada rüzgar yoktu. Bu kez çubuğu çok yavaş salladı. Çubuğun ucunda bir balon büyümeye başladı. Balon sonunda bir karnabahar kadar oldu! Hello Kitty çok sevindi, çünkü yeni arkadaşlar için büyük balonu yapmıştı.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yeni arkadaşlar için büyük"
   - Cümle 4: «Hello Kitty yeni arkadaşlar için büyük bir balon yapmak istiyordu.»
   - Açıklama: 'Yeni arkadaşlar için büyük balon' ifadesi gereksiz yere tekrarlanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşlar için büyük bir balon"
   - Cümle 4: «Hello Kitty yeni arkadaşlar için büyük bir balon yapmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği iki kez yalnız amaç olarak anılıyor ve çözümde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yeni arkadaşlar için büyük bir balon"
   - Cümle 4: «Hello Kitty yeni arkadaşlar için büyük bir balon yapmak istiyordu.»
   - Açıklama: Yeni arkadaşlar hedef olarak kuruluyor ama hikayede hiç görünmüyor ve balon onlara ulaşmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty yeni arkadaşlar için büyük bir balon yapmak istiyordu"
   - Cümle 4: «Hello Kitty yeni arkadaşlar için büyük bir balon yapmak istiyordu.»
   - Açıklama: Yeni arkadaşlar hedef gibi kuruluyor ama hikayede hiç görünmüyor ve kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0014` birebir aynı, ardından `@onarim: 179824e55efc3a8e8fd71e78ef8015c9e546e771`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0015 (deneme 2 -> 3)

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
@degisim: para -> dal
Bir sabah Hello Kitty, Mimi'yi ormandaki çadırlarının yanında gezdiriyordu. Orada devasa bir ağaç vardı. İkisi ağacın altından geçti. Birden Mimi'nin sarı kurdelesi alçak bir dala takıldı. Mimi kurdeleyi göremedi, çünkü kurdele başının arkasındaydı. Mimi kurdelesini çok seviyordu ve üzüldü. Hello Kitty herkese iyi bir arkadaştı ve hemen kardeşine yardım etti. Mimi'nin arkasına geçti ve dala baktı. Kurdele dalın ucuna dolanmıştı. Hello Kitty kurdeleyi daldan yavaşça çözdü. Sonra onu Mimi'nin başına güzelce bağladı. Mimi sevinçle gülümsedi ve kardeşine sarıldı. İki kardeş çadırların yanında gezmeye mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty, Mimi'yi ormandaki çadırlarının"
   - Cümle 1: «Bir sabah Hello Kitty, Mimi'yi ormandaki çadırlarının yanında gezdiriyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse uzağa gitmez; iki çocuk ormanda büyük olmadan geziyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Mimi'yi ormandaki çadırlarının yanında gezdiriyordu"
   - Cümle 1: «Bir sabah Hello Kitty, Mimi'yi ormandaki çadırlarının yanında gezdiriyordu.»
   - Açıklama: Yanlar alanında Mimi ikiz kardeş; 'gezdirmek' onu küçük ya da misafir gibi gösterip ilişkiyi bozuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Orada devasa bir ağaç"
   - Cümle 2: «Orada devasa bir ağaç vardı.»
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'çok büyük' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Orada devasa bir ağaç vardı"
   - Cümle 2: «Orada devasa bir ağaç vardı.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bildiği bir kelime değil.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «İkisi ağacın altından geçti.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor; ilk 3 cümlede sorun yok.
6. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden Mimi'nin sarı kurdelesi alçak bir dala takıldı"
   - Cümle 4: «Birden Mimi'nin sarı kurdelesi alçak bir dala takıldı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0015` birebir aynı, `@degisim: para -> dal` (tutuyorsan), ardından `@onarim: ae93039f29c07c32bbf6446ac87be4a3a7d321f5`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0016 (deneme 2 -> 3)

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
@plan: babasının elleri kirliydi ve temiz kazağını giyemedi | ellerine su döktü ve kazağı ona giydirdi
@tohum: hello_kitty-0016
@degisim: mercan -> kazak
Bir sabah ormandaki kamp yerinde serin bir rüzgar esti. Hello Kitty'nin babası kazağını giymek istedi. Ama çadırı kurarken elleri çok kirli olmuştu. "Temiz kazağı kirletmek istemiyorum," dedi babası. Hello Kitty kurabiye yaparken hep önce ellerini yıkardı. Hemen şişeyle su getirdi ve babasının ellerine döktü. Babası ellerini güzelce yıkadı. "Baba, kollarını kaldır!" dedi Hello Kitty. Babası güldü ve kollarını yukarı uzattı. Hello Kitty kazağı babasına dikkatle giydirdi. Kazak tertemiz kaldı. "Teşekkürler, kızım, şimdi çok iyiyim!" dedi babası. Hello Kitty bundan sonra kampta babasına hep yardım etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve temiz kazağını giyemedi"
   - Cümle 0 (plan satırı): «babasının elleri kirliydi ve temiz kazağını giyemedi | ellerine su döktü ve kazağı ona giydirdi»
   - Açıklama: Plan satırında kazağı giyemeyenin baba mı Hello Kitty mi olduğu belli değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kazağı babasına dikkatle giydirdi"
   - Cümle 10: «Hello Kitty kazağı babasına dikkatle giydirdi.»
   - Açıklama: Sebep kirli ellerdir ve eller yıkanınca sorun çözülmüştür; kazağı babaya çocuğun giydirmesi sebebe yönelmeyen gereksiz ek adımdır.
   - Açıklama: Babasının elleri temizlendikten sonra kazağı ona giydirmek sebebe yönelmeyen gereksiz bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0016` birebir aynı, `@degisim: mercan -> kazak` (tutuyorsan), ardından `@onarim: f359653450c44b42cfe16cf0320c0aaa8e652de8`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0017 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: çimenlerden hışır hışır bir ses geldi | sesin geldiği yere yürüdü ve kurabiye torbasını buldu
@tohum: hello_kitty-0017
@degisim: klasör -> torba
Hello Kitty annesiyle parkta piknik yapıyordu. Birden çimenlerden hışır hışır bir ses geldi. Hello Kitty sesin nereden geldiğini çok merak etti. "Anne, bak, bir ses var!" dedi Hello Kitty. Hello Kitty sesin geldiği yere doğru yürüdü. Orada tatlı bir koku vardı. Hello Kitty kokuyu hemen tanıdı, çünkü kurabiye yapmayı çok severdi. Çimenlerin arasında kıpkırmızı bir kağıt torba vardı. Rüzgar esince torba ses çıkarıyordu. Bu, evde annesiyle yaptığı kurabiyelerin torbasıydı. Rüzgar onu sepetten çimenlere düşürmüştü. Hello Kitty torbayı alınca ses bitti. Hello Kitty çok sevindi, çünkü hem sesi hem de kurabiyelerini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden çimenlerden hışır hışır bir ses geldi"
   - Cümle 2: «Birden çimenlerden hışır hışır bir ses geldi.»
   - Açıklama: Bir ses duymak sorun değil yalnız merak; asıl kayıp olan kurabiye torbası sonradan tesadüfen ortaya çıkıyor.
   - Açıklama: Sorun yalnız bir ses; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "torbayı alınca ses bitti"
   - Cümle 12: «Hello Kitty torbayı alınca ses bitti.»
   - Açıklama: Ses bitmez, kesilir; fiil öznesine uygun değil.
   - Açıklama: Ses bitmez, kesilir; ayrıca 13. cümlede 'sesi bulmuştu' da fiile uymuyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hem sesi hem de kurabiyelerini bulmuştu"
   - Cümle 13: «Hello Kitty çok sevindi, çünkü hem sesi hem de kurabiyelerini bulmuştu.»
   - Açıklama: Ses bulunmaz; 'sesin nereden geldiğini' anlamında yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0017` birebir aynı, `@degisim: klasör -> torba` (tutuyorsan), ardından `@onarim: 5097c6026cfb8419805f8e2c8e20f68835d5ffa5`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0018 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0018
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'ot', fiil 'dokunmak', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: turta kabının yuvarlak kapağı çok sıkıydı | babasından yardım istedi ve babası kapağı çevirdi
@tohum: hello_kitty-0018
Hello Kitty babasıyla parkta, yumuşak otların üstünde oturuyordu. Yanlarında en sevdiği elmalı turtanın kabı vardı. Ama kabın yuvarlak kapağı çok sıkıydı ve açılmadı. Hello Kitty kapağı iki eliyle çevirdi. Kapak hiç kıpırdamadı. "Baba, bu kapağı açmama yardım eder misin?" diye sordu Hello Kitty. "Tabii, kızım," dedi babası. Babası kabı sıkıca tuttu ve kapağı güçlü bir şekilde çevirdi. Kapak hemen açıldı. Turtanın güzel kokusu otların üstüne yayıldı. Hello Kitty sevinçle babasının koluna dokundu. "Teşekkürler, babacığım," dedi Hello Kitty. İkisi turtayı birlikte yedi. Hello Kitty bundan sonra sıkı bir kapak görünce babasından yardım istedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hello Kitty bundan sonra sıkı bir kapak görünce babasından yardım istedi"
   - Cümle 14: «Hello Kitty bundan sonra sıkı bir kapak görünce babasından yardım istedi.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor ama fiil tek seferlik '-dı' ile çekimlenmiş; 'isterdi' ya da 'istemeye başladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0018` birebir aynı, ardından `@onarim: edeee17fe7b38c9426ce264e3dd38f773eccf36f`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0019 (deneme 2 -> 3)

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
Ağaçlarda kuşlar ötüyordu. Hello Kitty ormandaki kamp yerinde, çadırın önündeydi. Çantasına baktı ama kurabiye kutusu yoktu. Çantanın kapağı açık kalmıştı ve kutu bir yere düşmüştü. Kutuda evde yaptığı yıldız kurabiyeleri vardı. Hello Kitty kütüğün yanına ve ağaçların dibine baktı. Kutu orada da yoktu. Çadırın içi biraz karanlıktı. Hello Kitty girişteki feneri açtı ve içeri tuttu. Işıkta köşedeki küçük kutuyu gördü. Bu, onun kurabiye kutusuydu! Çantayı çadırdan alırken kutu içeri düşmüştü. Hello Kitty kutuyu çıkardı ve kapağını açtı. Kurabiyelerin hepsi yerindeydi. Bir kurabiye aldı ve kapağı kutuya geri oturttu. Sonra kütüğe oturdu ve kurabiyesini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde, çadırın önündeydi.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde Hello Kitty ormanda yanında büyük olmadan tek başına dolaşıp arama yapıyor.
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini söylüyor; Hello Kitty ormandaki kamp yerinde yanında büyük olmadan yalnız.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kütüğün yanına ve ağaçların dibine baktı"
   - Cümle 6: «Hello Kitty kütüğün yanına ve ağaçların dibine baktı.»
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor; kutu çadırda düşmüşken önce ilgisiz yerlere bakılıyor ve arama ikiden fazla adım sürüyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Çantayı çadırdan alırken kutu içeri düşmüştü"
   - Cümle 12: «Çantayı çadırdan alırken kutu içeri düşmüştü.»
   - Açıklama: 'Alırken' zarf-fiilinin öznesi Hello Kitty ama ana cümlenin öznesi kutu; özne uyumsuz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0019` birebir aynı, `@degisim: gizemli -> küçük` (tutuyorsan), ardından `@onarim: 42c925bc9d5d9b43d761d42456e0910068bd6ae1`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0021 (deneme 2 -> 3)

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
@plan: rüzgar resim kağıdını alıp yüksek bir dala taktı | annesinden yardım istedi ve annesi kağıdı daldan aldı
@tohum: hello_kitty-0021
@degisim: değiştirmek -> tutmak
Rüzgar hızlı hızlı esiyordu. Hello Kitty parkta boyalarla resim yapıyordu, annesi de tuzlu kraker yiyordu. Birden rüzgar kağıdı havaya kaldırdı ve yüksek bir dala taktı. Hello Kitty zıpladı ama dala uzanamadı. "Anne, kağıdı daldan alır mısın?" diye sordu Hello Kitty. "Hemen alırım," dedi annesi. Annesi uzandı ve kağıdı daldan dikkatlice aldı. Hello Kitty kraker kutusunu kağıdın bir köşesine koydu. Öbür köşeyi de kendi eliyle tuttu. Kağıt artık hiç uçmadı. Hello Kitty resmine annesini ve kendisini iki arkadaş gibi el ele çizdi. "Teşekkürler, anneciğim, bu resim senin için!" dedi Hello Kitty.
```

**Hakem bulguları (3):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hello Kitty kraker kutusunu kağıdın bir köşesine koydu"
   - Cümle 8: «Hello Kitty kraker kutusunu kağıdın bir köşesine koydu.»
   - Açıklama: Kağıt daldan alındıktan sonra kağıdın yeniden uçması ikinci bir sorun olarak ele alınıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "iki arkadaş gibi el ele çizdi"
   - Cümle 11: «Hello Kitty resmine annesini ve kendisini iki arkadaş gibi el ele çizdi.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız resimde süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "annesini ve kendisini iki arkadaş gibi"
   - Cümle 11: «Hello Kitty resmine annesini ve kendisini iki arkadaş gibi el ele çizdi.»
   - Açıklama: Kartın özellikler alanındaki arkadaş edinme özelliği sorunun çözümünde işe yaramıyor, sona süs olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0021` birebir aynı, `@degisim: değiştirmek -> tutmak` (tutuyorsan), ardından `@onarim: 48e2890430b2f185d314cdd51776bfb52c21ed8b`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0022 (deneme 1 -> 2)

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
Evin mutfağında Hello Kitty ile Mimi masadaki tabağa baktı. Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı. İkisi de onu denemek istiyordu, ama tabakta başka kurabiye yoktu. Mimi utangaçtı ve hiçbir şey söylemedi. "Mimi, bu kurabiyeyi seninle paylaşmak istiyorum," dedi Hello Kitty. Mimi sevindi ama biraz düşündü. "İki parça aynı büyüklükte olur mu?" diye sordu Mimi. Hello Kitty çekmeceden bir cetvel aldı. Cetveli kurabiyenin tam ortasına koydu. Sonra kurabiyeyi cetvelin kenarından yavaşça ikiye kırdı. İki parça tam aynı boydaydı. Hello Kitty bir parçayı Mimi'ye verdi. İki kardeş yan yana oturdu ve parçalarını mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı"
   - Cümle 2: «Tabakta yıldız şeklinde, özel bir kurabiye kalmıştı.»
   - Açıklama: Karttaki özellik kurabiye yapmayı sevmek, hikayede kurabiye yalnız paylaşılan bir yiyecek ve özellik işe yarar biçimde kullanılmıyor.
   - Açıklama: Kartın özellikler alanında kurabiye yapmayı sevmek var, ama hikayede kurabiye yapılmıyor, yalnız kalan kurabiye bölünüp yeniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu denemek istiyordu"
   - Cümle 3: «İkisi de onu denemek istiyordu, ama tabakta başka kurabiye yoktu.»
   - Açıklama: Kurabiye için 'denemek' yerine 'yemek' kelimesi doğru anlamı verir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0022` birebir aynı, ardından `@onarim: a67a5d71590973e0fcdc7bbce2f4fe3bacef2c1e`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0024 (deneme 1 -> 2)

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
@plan: kırmızı böğürtlenler sertti ve dalından çıkmıyordu | annesine sordu ve siyah yumuşak olanları kopardı
@tohum: hello_kitty-0024
Bir sabah Hello Kitty, ormandaki kamp yerinde ilk kez böğürtlen toplamayı denedi. Onları annesinin getirdiği elmalı turtanın üstüne koymak istiyordu. Ama kırmızı böğürtlenler çok sertti ve dalından çıkmıyordu. Hello Kitty çalıya dikkatle baktı. Yaprakların arasında siyah ve yumuşak böğürtlenler de vardı. "Anne, siyah olanları alabilir miyim?" diye sordu Hello Kitty. "Evet, siyah olanlar yenir," dedi annesi. Hello Kitty siyah bir tanesine hafifçe dokundu ve o hemen koptu. Sonra birkaç tane daha kopardı. Onları turtanın pürüzsüz üstüne tek tek dizdi. "Turtamız çok güzel oldu!" dedi annesi. İkisi gölgeye oturdu ve Hello Kitty'nin en sevdiği turtayı mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ilk kez böğürtlen toplamayı denedi"
   - Cümle 1: «Bir sabah Hello Kitty, ormandaki kamp yerinde ilk kez böğürtlen toplamayı denedi.»
   - Açıklama: Ormanda yabani meyve koparıp yemek çocuğun taklit edince tehlikeli olabilecek bir davranış.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "siyah olanlar yenir"
   - Cümle 7: «"Evet, siyah olanlar yenir," dedi annesi.»
   - Açıklama: Çalıdan yabani böğürtlen toplayıp yemek çocuğun taklit edince tehlikeli olabilecek bir davranış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "turtanın pürüzsüz üstüne"
   - Cümle 10: «Onları turtanın pürüzsüz üstüne tek tek dizdi.»
   - Açıklama: 'Pürüzsüz' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bileceği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0024` birebir aynı, ardından `@onarim: 9f68851aebcfba47c57c17462482c0eb96a96636`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0025 (deneme 1 -> 2)

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
Hello Kitty ile Mimi mutfakta ilk kez limonata yapmayı denedi. Büyük bir kaseye soğuk su, limon suyu ve şeker koydular. Ama şeker erimedi ve kasenin dibinde kaldı, çünkü su çok soğuktu. Hello Kitty biraz düşündü. "Mimi, bana uzun bir kaşık verir misin?" diye sordu Hello Kitty. Mimi çekmeceden bir kaşık çıkardı ve ona verdi. Hello Kitty limonatayı kaşıkla uzun uzun karıştırdı. Şeker yavaş yavaş eridi ve limonata tatlı oldu. Hello Kitty iki bardağa limonata koydu. Kibar davrandı ve ilk bardağı en iyi arkadaşı Mimi'ye uzattı. "Çok güzel olmuş, teşekkürler!" dedi Mimi. Sonra iki kardeş limonatalarını mutlu mutlu içti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı Mimi'ye"
   - Cümle 10: «Kibar davrandı ve ilk bardağı en iyi arkadaşı Mimi'ye uzattı.»
   - Açıklama: Kardeş olarak tanıtılan Mimi yeniden 'en iyi arkadaşı' diye farklı biçimde tanıtılıyor.
   - Açıklama: Mimi ikinci kez ve çelişkili biçimde 'en iyi arkadaşı' diye tanıtılıyor, sonda ise 'iki kardeş' deniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ilk bardağı en iyi arkadaşı Mimi'ye uzattı"
   - Cümle 10: «Kibar davrandı ve ilk bardağı en iyi arkadaşı Mimi'ye uzattı.»
   - Açıklama: Mimi önce kardeş, sonra en iyi arkadaş, sonra yine kardeş olarak anılıyor ve ilişki tutarsız görünüyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "en iyi arkadaşı Mimi'ye uzattı"
   - Cümle 10: «Kibar davrandı ve ilk bardağı en iyi arkadaşı Mimi'ye uzattı.»
   - Açıklama: Mimi hem kardeş hem en iyi arkadaş olarak anılıyor ve ilişki çelişkili görünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0025` birebir aynı, `@degisim: şampuan -> kaşık` (tutuyorsan), ardından `@onarim: 30a5bf8c0acfd21095f6b70f5b44006f62de5bcd`, sonra gövde.
