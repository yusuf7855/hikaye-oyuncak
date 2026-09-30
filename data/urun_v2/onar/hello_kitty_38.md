# Editör görevi (onarım): Hello Kitty, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0156 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0156
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'havlu', fiil 'kurulanmak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babasının getirdiği havlunun içinde ne olduğunu merak etti | havluyu kokladı ve içindeki elmalı turtayı buldu
@tohum: hello_kitty-0156
@degisim: kurulanmak -> koklamak
Bir sabah Hello Kitty babasıyla parkta piknik yapıyordu. Babası sepetten havluya sarılı bir şey çıkardı. Hello Kitty onun ne olduğunu çok merak etti. "Baba, havlunun içinde ne var?" diye sordu Hello Kitty. "Bil bakalım," dedi babası ve göz kırptı. Hello Kitty yaklaştı ve onu kokladı. Tatlı bir elma kokusu geldi. Hello Kitty bu kokuyu hemen tanıdı. "Bu benim en sevdiğim elmalı turta!" dedi Hello Kitty. Babası güldü ve havluyu açtı. Gerçekten de sıcak bir turta vardı. "Sen çok hazırlıklı bir babasın!" dedi Hello Kitty. Hello Kitty çok sevindi, çünkü turtayı kokusundan kendi bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hello Kitty onun ne olduğunu çok merak etti"
   - Cümle 3: «Hello Kitty onun ne olduğunu çok merak etti.»
   - Açıklama: Sorun yalnız bir merak; babası havluyu zaten açacağı için gerçek bir sorun kurulmuyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hello Kitty yaklaştı ve onu kokladı"
   - Cümle 6: «Hello Kitty yaklaştı ve onu kokladı.»
   - Açıklama: 'Onu' zamiri önceki cümledeki babayı da gösterebilir; havlunun kastedildiği belli değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok hazırlıklı bir babasın"
   - Cümle 12: «"Sen çok hazırlıklı bir babasın!" dedi Hello Kitty.»
   - Açıklama: 'hazırlıklı' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Hazırlıklı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "turtayı kokusundan kendi bulmuştu"
   - Cümle 13: «Hello Kitty çok sevindi, çünkü turtayı kokusundan kendi bulmuştu.»
   - Açıklama: 'Kendi' yerine 'kendisi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0156` birebir aynı, `@degisim: kurulanmak -> koklamak` (tutuyorsan), ardından `@onarim: 66beb315e1ef897804c13e77694c0cefc47556e4`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0157 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0157
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'paket', fiil 'ıslanmak', sıfat 'zarif'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: suya zıpladı ve babasının pantolonu ıslandı | özür diledi ve babasına bir kurabiye verdi
@tohum: hello_kitty-0157
Parkta, çimenlerin arasında küçük bir su çukuru vardı. Hello Kitty koşarak geldi ve hızla çukura zıpladı. Su her yana sıçradı ve babasının pantolonu ıslandı. Babası elinde zarif bir paket tutuyordu. İçinde evde birlikte yaptıkları kurabiyeler vardı. Hello Kitty babasının pantolonuna baktı ve üzüldü. "Özür dilerim, babacığım," dedi Hello Kitty. Sonra paketin kırmızı kurdelesini çözdü. İçinden en güzel kurabiyeyi seçti ve babasına uzattı. Babası kurabiyeyi yedi ve kızına sarıldı. "Teşekkürler, Hello Kitty, bu kurabiye çok güzel olmuş!" dedi babası.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "elinde zarif bir paket"
   - Cümle 4: «Babası elinde zarif bir paket tutuyordu.»
   - Açıklama: 'Zarif' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Zarif' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İçinden en güzel kurabiyeyi seçti ve babasına uzattı"
   - Cümle 9: «İçinden en güzel kurabiyeyi seçti ve babasına uzattı.»
   - Açıklama: Sorun ıslanan pantolon ama kurabiye vermek bu sonuca ya da sebebine yönelmiyor.
   - Açıklama: Kurabiye vermek ıslak pantolona yönelik değil; sorunun sebebine dönük bir çözüm yok.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 11: «"Teşekkürler, Hello Kitty, bu kurabiye çok güzel olmuş!" dedi babası.»
   - Açıklama: Babanın ıslak pantolonu hiç ele alınmıyor, sorunun çözüldüğü görünmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0157` birebir aynı, ardından `@onarim: 4f5482a10b4d178d8ee84072f9ca26f7af6b458d`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0160 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0160
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'tabak', fiil 'gıdıklamak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesi yanındaydı ve sürprizi görebilirdi | annesinden gözlerini kapatmasını istedi ve kurabiyeleri dizdi
@tohum: hello_kitty-0160
@degisim: yardımsever -> mutlu
Hello Kitty annesiyle parkta, ağacın gölgesinde oturuyordu. Bugün annesinin doğum günüydü ve Hello Kitty ona sürpriz hazırlamak istedi. Ama annesi hemen yanındaydı ve her şeyi görecekti. "Anneciğim, gözlerini kapatıp yüze kadar sayar mısın?" diye sordu Hello Kitty. Annesi gülümsedi ve iki eliyle yüzünü kapattı. Hello Kitty sepetten büyük bir tabak çıkardı. Sabah birlikte yaptıkları kurabiyeleri tabağa kalp gibi dizdi. "Yüz!" dedi annesi ve ellerini indirdi. Tabakta kurabiyelerden kocaman bir kalp vardı. Annesi kızına sarıldı ve onu gıdıkladı. Hello Kitty neşeyle güldü. "Mutlu yıllar, anneciğim!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sabah birlikte yaptıkları kurabiyeleri"
   - Cümle 7: «Sabah birlikte yaptıkları kurabiyeleri tabağa kalp gibi dizdi.»
   - Açıklama: Kurabiyeler annesiyle birlikte yapıldığı için sürpriz olmasıyla çelişiyor.
   - Açıklama: Sürpriz kurabiyeleri annesiyle birlikte yapılmış; annenin göreceği şeyin sürpriz olması zayıflıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0160` birebir aynı, `@degisim: yardımsever -> mutlu` (tutuyorsan), ardından `@onarim: 5163f853d5f70cdf2ccc2ead89fba7bb7b14dbf3`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0162 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0162
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yün', fiil 'çekinmek', sıfat 'çalışkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: kardeşi yemeğini evde unutmuştu ve acıkmıştı | turtayı ikiye bölüp büyük parçayı kardeşine verdi
@tohum: hello_kitty-0162
Rüzgar hafifçe esiyordu. Hello Kitty ile Mimi parkta, ağacın gölgesinde oturuyordu. Mimi kendi yemeğini evde unutmuştu ve karnı acıkmıştı. Ama utandı ve bir şey istemekten çekindi. Sessizce yün atkısını örmeye devam etti. Hello Kitty kardeşinin sepete baktığını gördü. Hello Kitty sepetinden en sevdiği elmalı turtayı çıkardı. Turtayı ikiye böldü ve büyük parçayı Mimi'ye uzattı. "Sen çok çalışkansın, Mimi, biraz dinlen ve ye," dedi Hello Kitty. Mimi atkısını bıraktı ve turtayı aldı. "Teşekkürler, Hello Kitty, bu turta çok güzel!" dedi Mimi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir şey istemekten çekindi"
   - Cümle 4: «Ama utandı ve bir şey istemekten çekindi.»
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "yün atkısını örmeye devam"
   - Cümle 5: «Sessizce yün atkısını örmeye devam etti.»
   - Açıklama: Kartta Mimi'nin örgü yeteneği ya da yün atkısı yok.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sessizce yün atkısını örmeye"
   - Cümle 5: «Sessizce yün atkısını örmeye devam etti.»
   - Açıklama: Kartta Mimi'nin örgü yeteneği ya da yün atkı eşyası yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0162` birebir aynı, ardından `@onarim: b711c8bdaede6c7bef03c72130d2a22f0b361e8a`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0163
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fincan', fiil 'ayırmak', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: koşarken kardeşinin fincanına çarptı ve limonata döküldü | özür diledi ve kendi fincanını kardeşiyle paylaştı
@tohum: hello_kitty-0163
Parkta, ağacın gölgesinde iki fincan limonata duruyordu. Hello Kitty çimenlerde koşarken Mimi'nin fincanına çarptı. Fincan devrildi ve limonata çimenlere döküldü. Mimi boş fincanına baktı ve üzüldü. Hello Kitty hemen durdu ve kardeşinin yanına oturdu. Saygılı bir sesle ondan özür diledi. Sonra kendi fincanını eline aldı. Yarısını en iyi arkadaşına ayırdı ve onun fincanına koydu. Mimi fincanını iki eliyle tuttu ve gülümsedi. İkizler limonatalarını yudum yudum birlikte içti. Hello Kitty çok rahatladı, çünkü Mimi artık üzgün değildi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Saygılı bir sesle ondan"
   - Cümle 6: «Saygılı bir sesle ondan özür diledi.»
   - Açıklama: 'Saygılı bir ses' 3 yaşındaki çocuk için soyut bir ifade.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yarısını en iyi arkadaşına ayırdı"
   - Cümle 8: «Yarısını en iyi arkadaşına ayırdı ve onun fincanına koydu.»
   - Açıklama: Mimi kardeş olarak tanıtılmışken 'en iyi arkadaşı' denmesi kimin kastedildiğini belirsizleştiriyor.
   - Açıklama: Kardeş Mimi bir anda 'en iyi arkadaşı' diye anılıyor; kimin kastedildiği karışıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yarısını en iyi arkadaşına ayırdı"
   - Cümle 8: «Yarısını en iyi arkadaşına ayırdı ve onun fincanına koydu.»
   - Açıklama: Tohumdaki 'yeni arkadaşlar edinme' özelliği yalnız Mimi için bir ad olarak geçiyor, işe yarar biçimde kullanılmıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Yarısını en iyi arkadaşına ayırdı"
   - Cümle 8: «Yarısını en iyi arkadaşına ayırdı ve onun fincanına koydu.»
   - Açıklama: Mimi kardeşi ve ikizi olarak kuruluyor ama burada en iyi arkadaşı deniyor; limonatanın kime verildiği karışıyor.
   - Açıklama: Mimi kardeşi ve ikizi olarak anlatılırken burada en iyi arkadaşı deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0163` birebir aynı, ardından `@onarim: 3001d1b169062a3a3619eccf4a9873d5cb09b686`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0164
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'yelkenli', fiil 'düzelmek', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası yiyecek kutusunu evde unutmuştu | babasıyla yaptığı kurabiyeleri ona verdi
@tohum: hello_kitty-0164
@degisim: düzelmek -> doymak
Hello Kitty babasıyla ormandaki kamp yerindeydi. Hava açıktı ve babası acıkmıştı. Ama yiyecek kutusu çantada yoktu, babası onu evde unutmuştu. Babası başını kaşıdı ve güldü. Hello Kitty kendi küçük çantasını hatırladı. İçinde babasıyla birlikte yaptıkları kurabiyeler vardı. Kurabiyelerin hepsi küçük birer yelkenli şeklindeydi. "Buyur, babacığım, bunlar senin için," dedi Hello Kitty. Babası bir yelkenli aldı ve tadına baktı. "Çok lezzetli, kızım!" dedi babası. Babası birkaç kurabiye daha yedi ve doydu. İkisi kalan kurabiyeleri de paylaştı ve kamp yerinde mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kurabiyelerin hepsi küçük birer yelkenli şeklindeydi"
   - Cümle 7: «Kurabiyelerin hepsi küçük birer yelkenli şeklindeydi.»
   - Açıklama: Kurabiyelerin yelkenli şekli olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Babası bir yelkenli aldı"
   - Cümle 9: «Babası bir yelkenli aldı ve tadına baktı.»
   - Açıklama: Kurabiyeye 'yelkenli' denmesi kelimeyi yanlış anlamda kullanıyor, gerçek bir tekne alınmış gibi okunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0164` birebir aynı, `@degisim: düzelmek -> doymak` (tutuyorsan), ardından `@onarim: 677616e6094d5fc2bc6d27e57fd8b277ee3639e8`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0166 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0166
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'sandviç', fiil 'konmak', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: çimenler düz olmadığı için kurabiyeden duvarlar devrildi | sandviç kutusunun düz kapağını yere koydu
@tohum: hello_kitty-0166
@degisim: konmak -> kurmak
Evin yakınındaki parkta, ağaçların gölgesi serindi. Hello Kitty orada kurabiyelerden küçük bir ev kurmak istedi. Ama çimenler düz değildi ve kurabiyeden duvarlar hemen devrildi. Hello Kitty sepetindeki sandviç kutusuna baktı. Kutunun kapağı düz ve genişti. Hello Kitty sandviçini sepete koydu ve kapağı yere yerleştirdi. Sonra kıvrımlı kurabiyeleri onun üstüne tek tek dizdi. İki kurabiye duvar, bir kurabiye de çatı oldu. Bu kez duvarlar hiç yıkılmadı. Hello Kitty çok sevindi, çünkü küçük kurabiye evi sonunda sağlam duruyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kurabiyelerden küçük bir ev kurmak"
   - Cümle 2: «Hello Kitty orada kurabiyelerden küçük bir ev kurmak istedi.»
   - Açıklama: Karttaki özellik kurabiye yapmayı sevmek; burada kurabiye yapılmıyor, yapı malzemesi olarak kullanılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kurabiyelerden küçük bir ev kurmak istedi"
   - Cümle 2: «Hello Kitty orada kurabiyelerden küçük bir ev kurmak istedi.»
   - Açıklama: Tohumdaki özellik kurabiye yapmak; kurabiye yalnız yapı taşı olarak kullanılıyor, özellik sorunu çözmüyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra kıvrımlı kurabiyeleri"
   - Cümle 7: «Sonra kıvrımlı kurabiyeleri onun üstüne tek tek dizdi.»
   - Açıklama: 'Kıvrımlı' kelimesi 3 yaşındaki bir çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0166` birebir aynı, `@degisim: konmak -> kurmak` (tutuyorsan), ardından `@onarim: e49b40ba9a650ac7ef174b7e2283f0ddf0e736b0`, sonra gövde.
