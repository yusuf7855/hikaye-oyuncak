# Editör görevi (onarım): Hello Kitty, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar32.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0111 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0111
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'dolap', fiil 'yaklaştırmak', sıfat 'narin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: ağacın arkasından merak edilen bir ses geldi | kurabiyeyi ağaca yaklaştırdı ve sesi yapan babası çıktı
@tohum: hello_kitty-0111
@degisim: dolap -> sepet
Rüzgar esiyordu. Hello Kitty kamp yerinde sepetini açıyordu. Birden büyük bir ağacın arkasından tık tık diye bir ses geldi. Hello Kitty bu sesi çok merak etti. Babası da biraz önce o tarafa yürümüştü. Hello Kitty sepetten bir kurabiye aldı. Bu kurabiyeleri sabah babasıyla birlikte yapmıştı. Kurabiyeyi ağaca doğru yaklaştırdı. "Bu güzel kurabiyeyi kim ister?" diye sordu Hello Kitty. "Ben isterim!" dedi babası ve ağacın arkasından çıktı. Elinde narin bir dal vardı. "Seninle şaka yaptım, sesi bu dalla ben çıkardım," dedi babası. Hello Kitty kurabiyeyi babasına verdi ve ikisi de güldü. Hello Kitty çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (7):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden büyük bir ağacın arkasından"
   - Cümle 3: «Birden büyük bir ağacın arkasından tık tık diye bir ses geldi.»
   - Açıklama: Ormanda ağacın arkasından gelen bilinmeyen ses çocuk için tedirgin edici bir öğe.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tık tık diye bir ses"
   - Cümle 3: «Birden büyük bir ağacın arkasından tık tık diye bir ses geldi.»
   - Açıklama: Merak edilen bir ses gerçek bir sorun değil; ortada çözülmesi gereken bir güçlük yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kurabiyeleri sabah babasıyla birlikte"
   - Cümle 7: «Bu kurabiyeleri sabah babasıyla birlikte yapmıştı.»
   - Açıklama: Kurabiyelerin sabah yapıldığı ayrıntısı olayda hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu kurabiyeleri sabah babasıyla birlikte yapmıştı"
   - Cümle 7: «Bu kurabiyeleri sabah babasıyla birlikte yapmıştı.»
   - Açıklama: Kurabiyelerin sabah yapıldığı bilgisi olayda hiçbir işe yaramayan ayrıntı.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kurabiyeyi ağaca doğru yaklaştırdı"
   - Cümle 8: «Kurabiyeyi ağaca doğru yaklaştırdı.»
   - Açıklama: Kartın güvenli kullanım satırına aykırı olarak Hello Kitty tek başınayken bilinmeyen bir sesin kaynağına yiyecekle yaklaşıyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elinde narin bir dal"
   - Cümle 11: «Elinde narin bir dal vardı.»
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmediği bir kelime.
   - Açıklama: 'Narin' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kelimedir.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Seninle şaka yaptım, sesi"
   - Cümle 12: «"Seninle şaka yaptım, sesi bu dalla ben çıkardım," dedi babası.»
   - Açıklama: Doğru kullanım 'Sana şaka yaptım' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0111` birebir aynı, `@degisim: dolap -> sepet` (tutuyorsan), ardından `@onarim: e9e16bec8abf85b68b49230be75a626820fc1e07`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0112 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0112
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'tabure', fiil 'köpürmek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: rüzgar tabureye serilen örtüyü uçurdu | ağır turta tabağını örtünün ortasına koydu
@tohum: hello_kitty-0112
@degisim: sabırlı -> beyaz
Rüzgar ağaçların arasından hızlı hızlı esiyordu. Hello Kitty ormandaki kamp yerinde tabureyi sabunlu suyla yıkadı ve su köpürdü. Sonra tabureye beyaz bir örtü serdi, ama rüzgar örtüyü uçurdu. Hello Kitty örtüyü yerden aldı ve tekrar serdi. Rüzgar örtüyü bir kez daha havaya kaldırdı. Hello Kitty örtünün düzgün durmasını istiyordu. Birden sepetindeki elmalı turtayı düşündü. Turtanın tabağı büyük ve ağırdı. Hello Kitty turtanın tabağını örtünün tam ortasına koydu. Rüzgar yine esti ama örtü artık uçmadı. Hello Kitty bir dilim turta aldı ve mutlu mutlu yedi. Hello Kitty bundan sonra rüzgarlı günlerde örtünün üstüne ağır bir şey koydu.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde tabureyi"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde tabureyi sabunlu suyla yıkadı ve su köpürdü.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde Hello Kitty ormanda bir büyük olmadan tek başına bulunuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde tabureyi sabunlu suyla yıkadı ve su köpürdü.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda bir büyük olmadan yalnız.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tabureyi sabunlu suyla yıkadı ve su köpürdü"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde tabureyi sabunlu suyla yıkadı ve su köpürdü.»
   - Açıklama: Tabureyi yıkama ve köpüren su olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tabureyi sabunlu suyla yıkadı"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde tabureyi sabunlu suyla yıkadı ve su köpürdü.»
   - Açıklama: Tabureyi sabunlu suyla yıkama ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0112` birebir aynı, `@degisim: sabırlı -> beyaz` (tutuyorsan), ardından `@onarim: c8b498f36dcb3dd3e3c2cd616055f275458d8cd8`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0113 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0113
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'toz', fiil 'geçmek', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: kuru otlar örerken hemen kırıldı | gölgedeki yumuşak yeşil otlarla bileklik ördü
@tohum: hello_kitty-0113
Bir sabah Hello Kitty ormandaki kamp yerindeydi. İlk kez otlardan bir arkadaşlık bilekliği yapmayı denedi. Ama yoldaki otlar kuru ve tozluydu, hemen kırıldı. Hello Kitty kırık otlara baktı ve biraz düşündü. Sonra tozlu yoldan geçti ve ağaçların gölgesine gitti. Orada yumuşak ve yeşil otlar vardı. Hello Kitty birkaç yeşil otu nazikçe kopardı. Otları yavaş yavaş birbirine ördü. Yeşil otlar hiç kırılmadı. Sonunda küçük ve güzel bir bileklik oldu. Sonra bilekliğin üstündeki tozu üfledi. Hello Kitty çok sevindi, çünkü ilk bilekliğini kendisi yapmıştı.
```

**Hakem bulguları (8):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kuru otlar örerken hemen kırıldı"
   - Cümle 0 (plan satırı): «kuru otlar örerken hemen kırıldı | gölgedeki yumuşak yeşil otlarla bileklik ördü»
   - Açıklama: Otlar örmez; 'örülürken' olmalı, fiil yapısı özneye uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kuru otlar örerken hemen"
   - Cümle 0 (plan satırı): «kuru otlar örerken hemen kırıldı | gölgedeki yumuşak yeşil otlarla bileklik ördü»
   - Açıklama: Ören otlar değil Hello Kitty; '-ken' yan cümlesi yanlış özneye bağlanıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Hello Kitty ormandaki kamp yerindeydi"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerindeydi.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde Hello Kitty ormanda tek başına ve yol boyunca yürüyerek bulunuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir arkadaşlık bilekliği yapmayı"
   - Cümle 2: «İlk kez otlardan bir arkadaşlık bilekliği yapmayı denedi.»
   - Açıklama: 'Arkadaşlık' soyut bir kavram.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "otlardan bir arkadaşlık bilekliği"
   - Cümle 2: «İlk kez otlardan bir arkadaşlık bilekliği yapmayı denedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir kelime olarak geçiyor, arkadaş edinme sorunu çözmekte işe yaramıyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "otlardan bir arkadaşlık bilekliği yapmayı denedi"
   - Cümle 2: «İlk kez otlardan bir arkadaşlık bilekliği yapmayı denedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bilekliğin adında geçiyor ve çözümde işe yaramıyor.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra tozlu yoldan geçti ve ağaçların gölgesine gitti"
   - Cümle 5: «Sonra tozlu yoldan geçti ve ağaçların gölgesine gitti.»
   - Açıklama: Hello Kitty ormanda tek başına dolaşıyor; güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmediğini söylüyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bilekliğin üstündeki tozu üfledi"
   - Cümle 11: «Sonra bilekliğin üstündeki tozu üfledi.»
   - Açıklama: Gölgeden koparılan yumuşak yeşil otlarda toz yokken toz sebepsiz beliriyor ve işlevsiz.
   - Açıklama: Bileklik gölgedeki yumuşak yeşil otlardan örüldüğü halde üstünde sebepsiz toz beliriyor ve bu ayrıntı işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0113` birebir aynı, ardından `@onarim: 086a8e917792de6d54a8aee2afb0f5ce6cccc4f5`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0114 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0114
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'heykel', fiil 'rahatlatmak', sıfat 'tertemiz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: rüzgar tabağı devirdi ve kardeşinin turtası düştü | kendi turtasını ikiye bölüp yarısını kardeşine verdi
@tohum: hello_kitty-0114
@degisim: heykel -> tabak
Hello Kitty ile Mimi ormandaki kamp yerinde piknik yapıyordu. Birden rüzgar esti ve Mimi'nin kağıt tabağı devrildi. Mimi'nin elmalı turtası toprağa düştü. Mimi başını eğdi ve sessizce üzüldü. Hello Kitty kendi elmalı turtasına baktı. Sonra en sevdiği turtayı ikiye böldü. Yarısını tertemiz bir tabağa koydu. "Al, Mimi, bu yarısı senin," dedi Hello Kitty. Kardeşinin yardımı Mimi'yi hemen rahatlattı. "Teşekkür ederim, çok iyisin," dedi Mimi. İki kardeş turtalarını yedi ve pikniğe mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Mimi ormandaki kamp yerinde piknik"
   - Cümle 1: «Hello Kitty ile Mimi ormandaki kamp yerinde piknik yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse büyüksüz uzağa gitmez; iki çocuk ormanda yalnız.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kardeşinin yardımı Mimi'yi hemen rahatlattı"
   - Cümle 9: «Kardeşinin yardımı Mimi'yi hemen rahatlattı.»
   - Açıklama: 'Yardım' ve 'rahatlattı' soyut kavramlar; 3 yaşındaki çocuğa somut bir eylemle anlatılmalı.
   - Açıklama: Soyut 'yardım' öznesi ve 'rahatlattı' fiili 3 yaşındaki çocuk için soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0114` birebir aynı, `@degisim: heykel -> tabak` (tutuyorsan), ardından `@onarim: 840a0bd6d4e5a16d569085347e7e426ccbb76abc`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0115
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kask', fiil 'anlaşmak', sıfat 'kokulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: kask parktaki ağaçların birinin altında kayboldu | turta kokusunu izledi ve kaskını buldu
@tohum: hello_kitty-0115
@degisim: anlaşmak -> izlemek
Hello Kitty parkta kırmızı kaskını arıyordu. Bisiklet sürdükten sonra kaskı bir ağacın altına koymuştu. Ama parkta çok ağaç vardı ve hangi ağaç olduğunu bilmiyordu. Hello Kitty ağaçların altına tek tek baktı. Kask hiçbirinin altında yoktu. Birden rüzgarla çok güzel bir koku geldi. Hello Kitty bu kokuyu hemen tanıdı. Bu, en sevdiği elmalı turtanın kokusuydu. Turta sepeti de kaskın yanındaydı. Hello Kitty kokuyu izledi ve büyük bir ağaca yürüdü. Kokulu turta sepetinin yanında kırmızı kaskı duruyordu. Hello Kitty kaskını aldı ve başına taktı. Hello Kitty çok sevindi, çünkü kaskını bulmuştu.
```

**Hakem bulguları (5):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Bisiklet sürdükten sonra kaskı"
   - Cümle 2: «Bisiklet sürdükten sonra kaskı bir ağacın altına koymuştu.»
   - Açıklama: Bisiklet ve kask kartta yok ve tohum_yasak_kategoriler içindeki cagdas_arac kategorisine giriyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Bisiklet sürdükten sonra"
   - Cümle 2: «Bisiklet sürdükten sonra kaskı bir ağacın altına koymuştu.»
   - Açıklama: Bisiklet ve kask kartta olmayan eşyalar; kartın tohum yasak kategorileri çağdaş aracı dışlıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kask hiçbirinin altında yoktu"
   - Cümle 5: «Kask hiçbirinin altında yoktu.»
   - Açıklama: Kask hiçbir ağacın altında yok deniyor ama sonra büyük bir ağacın altında bulunuyor.
   - Açıklama: Bütün ağaçların altına bakılıp kask bulunamıyor ama sonra bir ağacın altında çıkıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Turta sepeti de kaskın yanındaydı"
   - Cümle 9: «Turta sepeti de kaskın yanındaydı.»
   - Açıklama: Turta sepeti sebepsiz beliriyor ve çözümü kendiliğinden getiriyor.
   - Açıklama: Turta sepeti önceden kurulmadan sebepsizce beliriyor ve çözümü getiriyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Kokulu turta sepetinin yanında kırmızı kaskı duruyordu"
   - Cümle 11: «Kokulu turta sepetinin yanında kırmızı kaskı duruyordu.»
   - Açıklama: Sepetin kaskın yanında olduğu 9. cümlede zaten söylenmişti; bilgi tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0115` birebir aynı, `@degisim: anlaşmak -> izlemek` (tutuyorsan), ardından `@onarim: 7032c23e29daf210a078438c5e7e6484c1d3a909`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0116
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'muffin', fiil 'boşalmak', sıfat 'temkinli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: rüzgar kutuyu devirdi ve kurabiyeler çimene döküldü | elindeki son kurabiyeyi ikiye bölüp annesiyle paylaştı
@tohum: hello_kitty-0116
@degisim: muffin -> kutu
Parkta ağaçların gölgesinde bir piknik örtüsü vardı. Hello Kitty ile annesi evde birlikte yaptıkları kurabiyeleri getirmişti. Ama rüzgar örtüyü kaldırdı ve kurabiye kutusu devrildi. Kutu boşaldı ve kurabiyeler yere döküldü. Bir tek kurabiye Hello Kitty'nin elinde kalmıştı. "Yere düşen kurabiyeleri yiyemeyiz," dedi annesi ve onları topladı. Annesi daha hiç kurabiye yememişti. Hello Kitty temkinli davrandı ve son kurabiyeyi yavaşça ikiye kırdı. "Al, anneciğim, bu yarısı senin," dedi Hello Kitty. "Teşekkürler, tatlım," dedi annesi ve kurabiyeyi yedi. Hello Kitty çok mutlu oldu, çünkü son kurabiyeyi annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hello Kitty temkinli davrandı"
   - Cümle 8: «Hello Kitty temkinli davrandı ve son kurabiyeyi yavaşça ikiye kırdı.»
   - Açıklama: 'Temkinli davranmak' soyut bir ifade, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty temkinli davrandı"
   - Cümle 8: «Hello Kitty temkinli davrandı ve son kurabiyeyi yavaşça ikiye kırdı.»
   - Açıklama: Tohumdaki özellik kurabiye; temkinlilik karttaki özelliklere ikinci bir huy olarak ekleniyor.
   - Açıklama: Tohumdaki özellik kurabiye; temkinlilik karttaki özelliklerde olmayan ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0116` birebir aynı, `@degisim: muffin -> kutu` (tutuyorsan), ardından `@onarim: b31b5e606fb9986fe751c9987a0303283101319e`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0119 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0119
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kadife', fiil 'açmak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: tebeşir kesesi sıkı bir düğümle bağlıydı | düğüme dikkatle baktı ve yavaşça açtı
@tohum: hello_kitty-0119
Bir sabah Hello Kitty parkta yeni bir şey denemek istedi. İlk kez tebeşirle parkın yoluna resim çizecekti. Ama kadife kese sıkı bir düğümle bağlıydı. Hello Kitty ipi hızlı hızlı çekti. Düğüm daha da sıkıştı. Hello Kitty durdu ve düğüme dikkatle baktı. Sonra ipin ucunu buldu ve düğümü yavaşça açtı. Kese renkli tebeşirlerle doluydu. Hello Kitty yere büyük bir güneş çizdi. Güneşin altına el ele tutuşan arkadaşlar çizdi. Resim çok güzel oldu. Hello Kitty bundan sonra düğümleri acele etmeden açtı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "el ele tutuşan arkadaşlar çizdi"
   - Cümle 10: «Güneşin altına el ele tutuşan arkadaşlar çizdi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız bir resimde anılıyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Güneşin altına el ele tutuşan arkadaşlar çizdi"
   - Cümle 10: «Güneşin altına el ele tutuşan arkadaşlar çizdi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız resimde anılıyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0119` birebir aynı, ardından `@onarim: eef913a1b26396794907d1f70afe521b491e2265`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0122
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: sırayla oynamak
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'pankek', fiil 'ayrılmak', sıfat 'şirin'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: tek bir top vardı ve kardeşi oyundan ayrıldı | ilk sırayı kardeşine verdi ve sırayla oynadılar
@tohum: hello_kitty-0122
@degisim: pankek -> top
Hello Kitty ile Mimi ormandaki kamp yerinde top oynuyordu. Topu şirin bir sepetin içine atıyorlardı. Ama bir tek top vardı ve ikisi de hep atmak istiyordu. Mimi utangaçtı, bir şey demedi ve oyundan ayrıldı. Bir ağacın altına oturdu ve topa baktı. Hello Kitty en iyi arkadaşının yanına gitti. Topu Mimi'nin eline verdi. "İlk sıra sende, Mimi, sonra ben atarım," dedi Hello Kitty. Mimi topu attı ve top sepete girdi. "Sıra sende, Hello Kitty!" dedi Mimi sevinçle. Hello Kitty de attı ve top sepetin içine düştü. İki kardeş sırayla atış yapıp oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en iyi arkadaşının yanına"
   - Cümle 6: «Hello Kitty en iyi arkadaşının yanına gitti.»
   - Açıklama: Mimi kardeşi olduğu halde 'en iyi arkadaşı' deniyor, sonra 'İki kardeş' deniyor; kelime seçimi tutarsız.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşının yanına gitti"
   - Cümle 6: «Hello Kitty en iyi arkadaşının yanına gitti.»
   - Açıklama: Kardeş olan Mimi burada 'en iyi arkadaşı' diye anılıyor, sonra 'İki kardeş' deniyor; gönderim tutarsız.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hello Kitty en iyi arkadaşının yanına gitti"
   - Cümle 6: «Hello Kitty en iyi arkadaşının yanına gitti.»
   - Açıklama: Mimi burada en iyi arkadaş diye anılıyor ama sonda ve planda kardeş olarak geçiyor.
   - Açıklama: Mimi önce en iyi arkadaş, sonunda kardeş olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0122` birebir aynı, `@degisim: pankek -> top` (tutuyorsan), ardından `@onarim: 8869a6ba66b882a4cba25554c42ec5cc5db4decb`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0135 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0135
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'bambu', fiil 'atlamak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: rüzgar çok gürültülü olduğu için geri gelen sesi duyamadı | rüzgarın durmasını bekledi ve yeniden seslendi
@tohum: hello_kitty-0135
@degisim: bambu -> rüzgar
Rüzgar ormanda hızlı hızlı esiyordu. Hello Kitty ile annesi kamp yerinde oturuyordu. Hello Kitty ağaçlara seslendi ama geri gelen sesi duyamadı. "Anne, sesim neden geri gelmedi?" diye sordu Hello Kitty. "Rüzgar çok gürültülü, o yüzden duyamadın," dedi annesi. Hello Kitty sabırsızdı ve yerinde iki kez atladı. Sonra annesinin yanına oturdu ve rüzgarın durmasını bekledi. Biraz sonra orman sessiz oldu. Hello Kitty ayağa kalktı. "Benimle arkadaş olur musun?" diye seslendi Hello Kitty. Uzaktan "Olur musun?" diye bir ses geri geldi. Annesi güldü ve kızına sarıldı. Hello Kitty çok sevindi, çünkü sesinin geri geldiğini sonunda duymuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hello Kitty sabırsızdı ve"
   - Cümle 6: «Hello Kitty sabırsızdı ve yerinde iki kez atladı.»
   - Açıklama: 'Sabırsız' soyut bir özellik kelimesi, 3 yaşındaki çocuk için somut bir davranışla anlatılmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty sabırsızdı ve yerinde"
   - Cümle 6: «Hello Kitty sabırsızdı ve yerinde iki kez atladı.»
   - Açıklama: Tohumdaki özellik arkadaş; sabırsızlık ikinci bir huy olarak ekleniyor ve arkadaş özelliği çözümde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty sabırsızdı"
   - Cümle 6: «Hello Kitty sabırsızdı ve yerinde iki kez atladı.»
   - Açıklama: Karttaki özelliklerde olmayan sabırsızlık ikinci bir huy olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0135` birebir aynı, `@degisim: bambu -> rüzgar` (tutuyorsan), ardından `@onarim: 334608edc67ada086f50aadd0a7d99813d6323d8`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0136 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0136
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çit', fiil 'saklamak', sıfat 'güzel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babasının sandviçi çimenlere düştü ve kirlendi | kendi sandviçini babasıyla paylaştı
@tohum: hello_kitty-0136
@degisim: çit -> çimen
Parkta ağaçların gölgesi çok güzeldi. Hello Kitty ile babası orada piknik yapıyordu. Babası sandviçini yerken sandviç elinden kaydı ve çimenlere düştü. "Eyvah, sandviçim kirlendi," dedi babası. Hello Kitty hemen çantasını açtı. Kendi sandviçini orada saklıyordu. Sandviçini ikiye böldü ve büyük parçayı babasına uzattı. "Al babacığım, bunu seninle paylaşmak istiyorum," dedi Hello Kitty. "Sen çok iyi bir arkadaşsın," dedi babası ve kızına teşekkür etti. İkisi yan yana oturup sandviçlerini yedi. Babası komik bir yüz yaptı ve Hello Kitty çok güldü. Sonra ikisi pikniklerine mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Al babacığım, bunu seninle"
   - Cümle 8: «"Al babacığım, bunu seninle paylaşmak istiyorum," dedi Hello Kitty.»
   - Açıklama: Hitaptan önce virgül eksik: 'Al, babacığım'.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Al babacığım, bunu"
   - Cümle 8: «"Al babacığım, bunu seninle paylaşmak istiyorum," dedi Hello Kitty.»
   - Açıklama: Hitaptan önce virgül eksik: 'Al, babacığım' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: ""Sen çok iyi bir arkadaşsın," dedi babası"
   - Cümle 9: «"Sen çok iyi bir arkadaşsın," dedi babası ve kızına teşekkür etti.»
   - Açıklama: Baba kızına 'arkadaş' diyor; kelime bu ilişkiye uygun değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sen çok iyi bir arkadaşsın"
   - Cümle 9: «"Sen çok iyi bir arkadaşsın," dedi babası ve kızına teşekkür etti.»
   - Açıklama: Baba kızına 'arkadaş' diyor; kelime konuşulan kişiye uygun değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: ""Sen çok iyi bir arkadaşsın," dedi babası"
   - Cümle 9: «"Sen çok iyi bir arkadaşsın," dedi babası ve kızına teşekkür etti.»
   - Açıklama: Karttaki özellik yeni arkadaş edinmek; hikayede yeni arkadaş edinilmiyor, kelime yalnız övgü olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0136` birebir aynı, `@degisim: çit -> çimen` (tutuyorsan), ardından `@onarim: 77cffc79eba06c4100c50f8ebd668c811914e2d3`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0137 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0137
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çamaşır', fiil 'şakalaşmak', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: koşarken kardeşinin çamaşırlarını yere düşürdü | özür diledi ve çamaşırları kardeşiyle yeniden katladı
@tohum: hello_kitty-0137
Dışarıda yağmur yağıyordu. Hello Kitty ile Mimi evde şakalaşıyordu. Hello Kitty koşarken Mimi'nin katladığı çamaşırlara çarptı ve hepsi yere düştü. Mimi yerdeki çamaşırlara baktı ve çok üzüldü. Hello Kitty hemen durdu. Kardeşinin yanına gitti ve ondan özür diledi. Sonra en iyi arkadaşına sıkıca sarıldı. Hello Kitty yumuşak havluları yerden tek tek topladı. Mimi de ona yardım etti. İkisi birlikte bütün çamaşırları yeniden katladı ve sepete koydu. Mimi gülümsedi ve Hello Kitty'nin elini tuttu. Hello Kitty bundan sonra evde koşarken etrafına dikkat etti.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra en iyi arkadaşına sıkıca sarıldı"
   - Cümle 7: «Sonra en iyi arkadaşına sıkıca sarıldı.»
   - Açıklama: Kardeş olarak anılan Mimi birden 'en iyi arkadaşı' diye anılıyor, yeni biri tanıtılıyormuş gibi kimin kastedildiği belirsizleşiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşına sıkıca"
   - Cümle 7: «Sonra en iyi arkadaşına sıkıca sarıldı.»
   - Açıklama: Kardeşi Mimi bir de 'en iyi arkadaşı' diye anılıyor; kime sarıldığı belirsiz ve kişi yeniden tanıtılmış gibi.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra en iyi arkadaşına sıkıca sarıldı"
   - Cümle 7: «Sonra en iyi arkadaşına sıkıca sarıldı.»
   - Açıklama: Kardeşi Mimi'den söz edilirken birden 'en iyi arkadaş' beliriyor ve kime sarıldığı belirsizleşiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra en iyi arkadaşına sıkıca sarıldı"
   - Cümle 7: «Sonra en iyi arkadaşına sıkıca sarıldı.»
   - Açıklama: Mimi bir cümle önce kardeş olarak anılıyor, sonra en iyi arkadaş deniyor; kimlik çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0137` birebir aynı, ardından `@onarim: e4c7aa34b3f014c31b94dbae756724875821567a`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0139 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0139
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'limon', fiil 'üflemek', sıfat 'hafif'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: çalıların arasından garip bir ses geldi | çalıya bakıp sıkışan balonu çıkardı
@tohum: hello_kitty-0139
Hello Kitty evin yanındaki parkta çiçeklere bakıyordu. Birden çalıların arasından garip bir ses geldi. Hello Kitty bu sesin nereden geldiğini çok merak etti. Çalıya yavaşça yaklaştı ve dallara baktı. Dalların arasında limon sarısı bir balon sıkışmıştı. Rüzgar esince hafif balon dallara sürtünüyor ve ses çıkarıyordu. Hello Kitty dalları dikkatle açtı ve balonu çıkardı. Balonun üstündeki küçük yaprakları üfledi. Sonra balonun ipini parkın girişindeki banka bağladı. Böylece balonu arayan arkadaşlar onu kolayca bulabilecekti. Hello Kitty çiçeklere bakmaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden çalıların arasından garip bir ses geldi"
   - Cümle 2: «Birden çalıların arasından garip bir ses geldi.»
   - Açıklama: Garip bir ses çocuğun önemseyeceği gerçek bir sorun değil, yalnız bir merak konusu.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Çalıya yavaşça yaklaştı ve dallara baktı"
   - Cümle 4: «Çalıya yavaşça yaklaştı ve dallara baktı.»
   - Açıklama: Parkta yalnız olan çocuk figür çalıdan gelen bilinmeyen garip sese yaklaşıyor; taklit edilince güvensiz bir davranış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Balonun üstündeki küçük yaprakları üfledi"
   - Cümle 8: «Balonun üstündeki küçük yaprakları üfledi.»
   - Açıklama: Yaprakları üfleme olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "balonu arayan arkadaşlar onu kolayca bulabilecekti"
   - Cümle 10: «Böylece balonu arayan arkadaşlar onu kolayca bulabilecekti.»
   - Açıklama: Tohumdaki özellik yeni arkadaş edinmek; hikayede arkadaş edinilmiyor, özellik yalnız varsayımsal arka plan arkadaşlara değinerek geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0139` birebir aynı, ardından `@onarim: f750a4ecefe83de30a0c9d0edee160708e935827`, sonra gövde.
