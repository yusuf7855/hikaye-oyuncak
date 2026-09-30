# Editör görevi (onarım): Hello Kitty, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0161 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0161
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'baloncuk', fiil 'kirletmek', sıfat 'kırılgan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: rüzgar esti ve babasının baloncuk şişesi devrildi | kendi şişesini babasıyla paylaştı ve birlikte baloncuk yaptılar
@tohum: hello_kitty-0161
@degisim: kirletmek -> üflemek
Hello Kitty babasıyla parkta baloncuk makinesi oyunu oynuyordu. İkisi de en büyük baloncuğu yapmak istiyordu. Ama rüzgar esti ve babasının şişesi çimene devrildi. Şişedeki bütün baloncuk suyu toprağa aktı. "Eyvah, benim suyum bitti," dedi babası. Babası boş şişeye üzgün üzgün baktı. Hello Kitty hemen kendi şişesini babasına uzattı. "Sen benim oyun arkadaşımsın, baba, bunu birlikte kullanalım," dedi Hello Kitty. Babası gülümsedi ve çubuğu şişeye daldırdı. Hello Kitty çubuğu tuttu, babası da yavaşça üfledi. Kocaman ve kırılgan bir baloncuk ağaçlara doğru yükseldi. Babası sevinçle ellerini çırptı. Hello Kitty çok sevindi, çünkü en büyük baloncuğu babasıyla birlikte yapmıştı.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parkta baloncuk makinesi oyunu oynuyordu"
   - Cümle 1: «Hello Kitty babasıyla parkta baloncuk makinesi oyunu oynuyordu.»
   - Açıklama: Hikayede makine yok, şişe ve çubukla baloncuk yapılıyor; kelime yanlış anlamda.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parkta baloncuk makinesi oyunu"
   - Cümle 1: «Hello Kitty babasıyla parkta baloncuk makinesi oyunu oynuyordu.»
   - Açıklama: Hikayede makine yok, şişe ve çubukla baloncuk yapılıyor; kelime yanlış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "baloncuk makinesi oyunu oynuyordu"
   - Cümle 1: «Hello Kitty babasıyla parkta baloncuk makinesi oyunu oynuyordu.»
   - Açıklama: Baloncuk makinesi kuruluyor ama hikayede makine hiç yok, baloncuklar şişe ve çubukla yapılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sen benim oyun arkadaşımsın"
   - Cümle 8: «"Sen benim oyun arkadaşımsın, baba, bunu birlikte kullanalım," dedi Hello Kitty.»
   - Açıklama: Tohumdaki özellik yeni arkadaşlar edinmek iken 'arkadaş' kelimesi babaya zorla takılıyor; özellik kartta tarif edildiği gibi işe yarar biçimde kullanılmıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kocaman ve kırılgan bir baloncuk"
   - Cümle 11: «Kocaman ve kırılgan bir baloncuk ağaçlara doğru yükseldi.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kocaman ve kırılgan bir"
   - Cümle 11: «Kocaman ve kırılgan bir baloncuk ağaçlara doğru yükseldi.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0161` birebir aynı, `@degisim: kirletmek -> üflemek` (tutuyorsan), ardından `@onarim: 5fcde8e736112f557c554894402eb2bb44281c54`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0162 (deneme 2 -> 3)

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
@plan: kardeşi yemeğini evde unutmuştu ve acıkmıştı | turtayı ikiye böldü ve büyük parçayı kardeşine verdi
@tohum: hello_kitty-0162
@degisim: çekinmek -> utanmak
Rüzgar hafifçe esiyordu. Hello Kitty ile Mimi parkta, ağacın gölgesine geldi. Mimi kendi yemeğini evde unutmuştu ve karnı acıkmıştı. Ama utandı ve bir şey istemedi. Sessizce yün örtüyü çimenlere serdi. Hello Kitty kardeşinin sepete baktığını gördü. Hello Kitty sepetinden en sevdiği elmalı turtayı çıkardı. Turtayı ikiye böldü ve büyük parçayı Mimi'ye uzattı. "Sen çok çalışkansın, Mimi, biraz dinlen ve ye," dedi Hello Kitty. Mimi örtüye oturdu ve turtayı aldı. "Teşekkürler, Hello Kitty, bu turta çok güzel!" dedi Mimi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sen çok çalışkansın, Mimi"
   - Cümle 9: «"Sen çok çalışkansın, Mimi, biraz dinlen ve ye," dedi Hello Kitty.»
   - Açıklama: Mimi hiç çalışmadığı için 'çalışkan' kelimesi olaya uymuyor.
   - Açıklama: Mimi çalışmadığı için 'çalışkan' kelimesi bu bağlamda yanlış anlamda kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sen çok çalışkansın, Mimi, biraz dinlen"
   - Cümle 9: «"Sen çok çalışkansın, Mimi, biraz dinlen ve ye," dedi Hello Kitty.»
   - Açıklama: Mimi'nin çalıştığı hiçbir yerde anlatılmıyor; replik olaydan çıkmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sen çok çalışkansın, Mimi"
   - Cümle 9: «"Sen çok çalışkansın, Mimi, biraz dinlen ve ye," dedi Hello Kitty.»
   - Açıklama: Mimi hiç çalışmadı; övgü olaydan çıkmıyor ve sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0162` birebir aynı, `@degisim: çekinmek -> utanmak` (tutuyorsan), ardından `@onarim: 842ef942b03775c241806c90cb750abf76154b80`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0163 (deneme 2 -> 3)

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
@degisim: saygılı -> boş
Parkta, ağacın gölgesinde iki fincan limonata duruyordu. Hello Kitty çimenlerde koşarken Mimi'nin fincanına çarptı. Fincan devrildi ve limonata çimenlere döküldü. Mimi boş fincanına baktı ve üzüldü. Hello Kitty hemen durdu ve kardeşinin yanına oturdu. Ona sarıldı ve özür diledi. Sonra kendi fincanını eline aldı. Yarısını kardeşine ayırdı ve onun fincanına koydu. Mimi fincanını iki eliyle tuttu ve gülümsedi. İkizler limonatalarını yudum yudum birlikte içti. Hello Kitty rahatladı, çünkü kardeşi ve en iyi arkadaşı artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yarısını kardeşine ayırdı"
   - Cümle 8: «Yarısını kardeşine ayırdı ve onun fincanına koydu.»
   - Açıklama: 'Yarısını' neyin yarısı olduğu belli değil; limonata anılmıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kardeşi ve en iyi arkadaşı artık üzgün değildi"
   - Cümle 11: «Hello Kitty rahatladı, çünkü kardeşi ve en iyi arkadaşı artık üzgün değildi.»
   - Açıklama: 'Kardeşi ve en iyi arkadaşı' iki ayrı kişi gibi okunuyor; kimi gösterdiği belli değil.
   - Açıklama: 'Kardeşi ve en iyi arkadaşı' iki ayrı kişiyi gösteriyor gibi okunuyor; kimin kastedildiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0163` birebir aynı, `@degisim: saygılı -> boş` (tutuyorsan), ardından `@onarim: 9fc6350010d2bbb56e68a946ff82e83e4ad16c67`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0165 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0165
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kabak', fiil 'sektirmek', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: kutu çok hafifti ve top çarpınca devrildi | kutunun dibine ağır bir kabak koydu
@tohum: hello_kitty-0165
Bir sabah Hello Kitty evde arkadaşları için yeni bir oyun yapıyordu. Oyunda top yere sekip büyük bir kutunun içine düşecekti. Ama kutu çok hafifti ve top çarpınca hemen devrildi. Hello Kitty kutuyu kaldırdı ve biraz düşündü. Kutunun ağır olması için içine bir şey koymalıydı. Mutfaktaki sepette büyük, turuncu bir kabak vardı. Hello Kitty kabağı iki eliyle taşıdı ve kutunun dibine koydu. Sonra topu güçlü bir şekilde yere sektirdi. Top zıpladı ve kutunun içine düştü. Kutu bu kez hiç kıpırdamadı. Oyun artık arkadaşları için hazırdı. Hello Kitty bundan sonra hafif kutuların dibine hep ağır bir şey koydu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "evde arkadaşları için yeni bir oyun"
   - Cümle 1: «Bir sabah Hello Kitty evde arkadaşları için yeni bir oyun yapıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız amaç olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0165` birebir aynı, ardından `@onarim: 3f78adb8bca1b7517ebd38f5ef6e5ec9c557e3aa`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0167 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0167
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'flüt', fiil 'başlamak', sıfat 'meşgul'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: konsere başlamak istedi ama annesi örtüyle meşguldü | örtüyü annesiyle birlikte yaydı ve konsere başladı
@tohum: hello_kitty-0167
Bir sabah Hello Kitty annesiyle ormandaki kamp yerindeydi. Hello Kitty bu sabah flütüyle konser oyunu oynuyordu. Konsere başlamak istiyordu ama annesi çok meşguldü. Annesi büyük piknik örtüsünü tek başına yere yaymaya çalışıyordu. "Anne, benim konser arkadaşım olur musun?" diye sordu Hello Kitty. "Olurum ama önce bu işi bitirmem lazım," dedi annesi. Hello Kitty flütünü bıraktı ve örtünün öbür ucunu tuttu. İkisi örtüyü birlikte ağaçların altına yaydı. Annesi örtünün üstüne oturdu ve gülümsedi. Hello Kitty flütünü aldı ve neşeli bir şarkı çaldı. Annesi de şarkıya el çırparak katıldı. "Teşekkürler, anneciğim, en güzel konseri birlikte yaptık!" dedi Hello Kitty.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty bu sabah flütüyle"
   - Cümle 2: «Hello Kitty bu sabah flütüyle konser oyunu oynuyordu.»
   - Açıklama: İlk cümledeki 'Bir sabah' ve özne gereksiz yere yinelenmiş, anlatımda 'bu sabah' da yersiz.
   - Açıklama: İlk cümlede geçen 'sabah' ve 'Hello Kitty' hemen ardından gereksiz yere tekrarlanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama annesi çok meşguldü"
   - Cümle 3: «Konsere başlamak istiyordu ama annesi çok meşguldü.»
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "benim konser arkadaşım olur musun"
   - Cümle 5: «"Anne, benim konser arkadaşım olur musun?" diye sordu Hello Kitty.»
   - Açıklama: Tohumdaki özellik yeni arkadaş edinmeyi sevmek; burada yalnız annesine söylenen bir kelime olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "benim konser arkadaşım olur"
   - Cümle 5: «"Anne, benim konser arkadaşım olur musun?" diye sordu Hello Kitty.»
   - Açıklama: Tohumdaki özellik yeni arkadaşlar edinmek; annesini konser arkadaşı yapmak bu özelliği işe yarar biçimde kullanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0167` birebir aynı, ardından `@onarim: 23718f3b3af717be443e2a00f056340adf64a2a4`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0168 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0168
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'börek', fiil 'durdurmak', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: düşen elmalar çimenlerde çalılara doğru yuvarlandı | boş sepetini yere koyup elmaları durdurdu
@tohum: hello_kitty-0168
Parkta ferah bir sabah hafif bir rüzgar esiyordu. Hello Kitty bir elma ağacının gölgesinde böreğini yiyordu. Birden rüzgar dalları salladı ve yere kırmızı elmalar düştü. Elmalar çimenlerde yuvarlandı ve çalılara doğru gitti. Hello Kitty en sevdiği elmalı turtayı düşündü. Bu elmalar bir elmalı turta için çok güzeldi. Böreğini yanına koydu ve boş sepetini aldı. Elmaları durdurmak için sepeti çalıların önüne yatırdı. Elmalar birer birer sepetin içine girdi. Hello Kitty sepeti kaldırdı ve içine baktı. Sepette beş tane kırmızı elma vardı. Hello Kitty sepetin yanında böreğini mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (8):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Parkta ferah bir sabah"
   - Cümle 1: «Parkta ferah bir sabah hafif bir rüzgar esiyordu.»
   - Açıklama: 'Ferah' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Ferah' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden rüzgar dalları salladı ve yere kırmızı elmalar düştü.»
   - Açıklama: Elmaların çalılara yuvarlanması ve bunun neden sorun olduğu ilk üç cümlede söylenmiyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Elmalar çimenlerde yuvarlandı ve çalılara doğru gitti"
   - Cümle 4: «Elmalar çimenlerde yuvarlandı ve çalılara doğru gitti.»
   - Açıklama: Sorun ancak 4. cümlede, neden önemli olduğu 5-6. cümlelerde söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elmalar çimenlerde yuvarlandı ve çalılara doğru gitti"
   - Cümle 4: «Elmalar çimenlerde yuvarlandı ve çalılara doğru gitti.»
   - Açıklama: Elmaların çalılara yuvarlanması çocuğun önemseyeceği güçlü bir sorun değil; elmalar çalıdan da alınabilir.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu elmalar bir elmalı turta için çok güzeldi"
   - Cümle 6: «Bu elmalar bir elmalı turta için çok güzeldi.»
   - Açıklama: Bir önceki cümledeki elmalı turta düşüncesi gereksizce tekrarlanıyor.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu elmalar bir elmalı turta için"
   - Cümle 6: «Bu elmalar bir elmalı turta için çok güzeldi.»
   - Açıklama: 'Elmalı turta' art arda iki cümlede gereksiz yere tekrarlanıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Böreğini yanına koydu ve boş sepetini aldı"
   - Cümle 7: «Böreğini yanına koydu ve boş sepetini aldı.»
   - Açıklama: Daha önce kurulmamış boş sepet çözümü getirmek için sebepsizce beliriyor.
8. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "böreğini mutlu mutlu yemeye devam etti"
   - Cümle 12: «Hello Kitty sepetin yanında böreğini mutlu mutlu yemeye devam etti.»
   - Açıklama: Hedef elmalı turtaydı ama son cümle turtaya dönmüyor ve hikaye börek yemeye dönen durgun bir eylemle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0168` birebir aynı, ardından `@onarim: 8be51561ec27e1e37ebe716fa5e76b6841bfe0fd`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0169 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0169
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'brokoli', fiil 'kutlamak', sıfat 'çilekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: güneş çok parlaktı ve kağıda bakamadı | ağaçların gölgesine oturup bulutların resmini çizdi
@tohum: hello_kitty-0169
@degisim: kutlamak -> çizmek
Hello Kitty parkta çimenlere uzanmış, bulutlara bakıyordu. Bir bulut brokoliye, bir bulut da çilekli bir pastaya benziyordu. Hello Kitty arkadaşlarına göstermek için bu bulutları çizmek istedi. Ama güneş çok parlaktı ve beyaz kağıda hiç bakamadı. Hello Kitty etrafına baktı ve büyük bir ağaç gördü. Kağıdını ve boyalarını alıp ağacın gölgesine oturdu. Gölgede kağıt artık parlamıyordu. Hello Kitty önce yeşil boyayla brokoliye benzeyen bulutu çizdi. Sonra pembe boyayla pastaya benzeyen bulutu çizdi. Pastanın üstüne küçük kırmızı çilekler de ekledi. Resim bitince kağıdı iki eliyle tuttu ve baktı. Hello Kitty çok sevindi, çünkü bulutların resmi artık hazırdı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güneş çok parlaktı ve kağıda bakamadı"
   - Cümle 0 (plan satırı): «güneş çok parlaktı ve kağıda bakamadı | ağaçların gölgesine oturup bulutların resmini çizdi»
   - Açıklama: Plan satırında da özne uyumsuz; 'bakamadı' fiilinin öznesi güneş gibi okunuyor.
   - Açıklama: Plan satırında 'bakamadı' fiilinin öznesi güneş gibi okunuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarına göstermek için bu bulutları"
   - Cümle 3: «Hello Kitty arkadaşlarına göstermek için bu bulutları çizmek istedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş edinme ve herkese iyi davranma özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güneş çok parlaktı ve beyaz kağıda hiç bakamadı"
   - Cümle 4: «Ama güneş çok parlaktı ve beyaz kağıda hiç bakamadı.»
   - Açıklama: Bağlaçla birleşen iki yüklemin öznesi farklı ama ikinci özne yazılmamış; cümle 'güneş bakamadı' diye okunuyor.
   - Açıklama: İki yan cümle tek özneye bağlanmış; 'bakamadı' fiilinin öznesi güneş gibi okunuyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama güneş çok parlaktı"
   - Cümle 4: «Ama güneş çok parlaktı ve beyaz kağıda hiç bakamadı.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0169` birebir aynı, `@degisim: kutlamak -> çizmek` (tutuyorsan), ardından `@onarim: c311fb9d2ab5d52c7d11906c8db9f4dcbfb2c1cd`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0170
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fide', fiil 'uyanmak', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: top küçük bitkilerin arasına yuvarlandı | bitkilere dikkat ederek yürüdü ve topu aldı
@tohum: hello_kitty-0170
@degisim: uyanmak -> yürümek
Bir sabah Hello Kitty parkta topuyla yakalama oyunu oynuyordu. Arkadaşları gelmeden önce topu yakalamayı çalışıyordu. Ama top yere çarptı ve küçük bitkilerin arasına yuvarlandı. Her fide çok küçüktü ve kolay eğiliyordu. Hello Kitty bitkilerin arasında dar bir yol gördü. Parmaklarının ucunda bu yoldan yavaşça yürüdü. Topu iki bitkinin arasından dikkatle aldı. Sonra aynı yoldan geri döndü. Bitkilerin hepsi yine dimdik duruyordu. Çimenler top oyunu için mükemmel bir yerdi. Hello Kitty bundan sonra topuyla bitkilerden uzakta, çimenlerde oynadı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "topu yakalamayı çalışıyordu"
   - Cümle 2: «Arkadaşları gelmeden önce topu yakalamayı çalışıyordu.»
   - Açıklama: Ek hatası; 'yakalamaya çalışıyordu' ya da 'yakalama çalışması yapıyordu' olmalı.
   - Açıklama: Ek yanlış; 'topu yakalamaya çalışıyordu' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Arkadaşları gelmeden önce topu"
   - Cümle 2: «Arkadaşları gelmeden önce topu yakalamayı çalışıyordu.»
   - Açıklama: Tohumdaki arkadaşlık özelliği yalnız anılıyor, sorunun çözümünde (bitkilere dikkat etmek) hiç işe yaramıyor.
   - Açıklama: Karttaki 'yeni arkadaşlar edinmeyi sever' özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arkadaşları gelmeden önce topu yakalamayı çalışıyordu"
   - Cümle 2: «Arkadaşları gelmeden önce topu yakalamayı çalışıyordu.»
   - Açıklama: Gelecek arkadaşlar işe yarayacakmış gibi kuruluyor ama hikayede hiç kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arkadaşları gelmeden önce topu yakalamayı"
   - Cümle 2: «Arkadaşları gelmeden önce topu yakalamayı çalışıyordu.»
   - Açıklama: Gelecek arkadaşlar kurulup hikayede hiç kullanılmıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Her fide çok küçüktü"
   - Cümle 4: «Her fide çok küçüktü ve kolay eğiliyordu.»
   - Açıklama: 'Fide' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime ve bitkilere birden başka adla değiniliyor.
   - Açıklama: 'Fide' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0170` birebir aynı, `@degisim: uyanmak -> yürümek` (tutuyorsan), ardından `@onarim: cb8cf6d9c9316e3964e15989a4e14f2c4330bfe6`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0171 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0171
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'palmiye', fiil 'sallanmak', sıfat 'tozlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: tozlu ayakkabılarıyla temiz örtüye bastı | özür diledi ve turtanın en büyük dilimini verdi
@tohum: hello_kitty-0171
@degisim: palmiye -> salıncak
Rüzgar ağaçların arasında hafif hafif esiyordu. Hello Kitty ormandaki kamp yerinde salıncakta sallanıyordu. Annesi temiz bir örtünün ortasına elmalı turtayı koydu. Hello Kitty salıncaktan indi ve koşarak örtüye bastı. Tozlu ayakkabıları beyaz örtüyü kirletti. "Eyvah, örtü toz oldu," dedi annesi. Hello Kitty üzüldü ve ayakkabılarını çıkardı. "Özür dilerim, anneciğim," dedi Hello Kitty. Sonra örtünün tozunu elleriyle silkti. Annesi gülümsedi ve turtayı dilimledi. Hello Kitty en sevdiği turtanın en büyük dilimini annesine verdi. "Teşekkürler, tatlım, hadi birlikte yiyelim!" dedi annesi.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür diledi ve turtanın en büyük dilimini verdi"
   - Cümle 0 (plan satırı): «tozlu ayakkabılarıyla temiz örtüye bastı | özür diledi ve turtanın en büyük dilimini verdi»
   - Açıklama: Plan örtünün tozunu silkmeyi söylemiyor, sebebe yönelmeyen turta dilimini çözüm diye veriyor.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "kamp yerinde salıncakta sallanıyordu"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde salıncakta sallanıyordu.»
   - Açıklama: Kartın orman tarifi ağaçların arasındaki kamp yerinden söz ediyor; salıncak tarifte yok.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Annesi temiz bir örtünün ortasına elmalı turtayı koydu.»
   - Açıklama: Sorun ilk 3 cümlede söylenmiyor; örtüye basma ancak 4. ve 5. cümlede geliyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Tozlu ayakkabıları beyaz örtüyü kirletti"
   - Cümle 5: «Tozlu ayakkabıları beyaz örtüyü kirletti.»
   - Açıklama: Sorun ilk üç cümlede değil ancak beşinci cümlede ortaya çıkıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Eyvah, örtü toz oldu"
   - Cümle 6: «"Eyvah, örtü toz oldu," dedi annesi.»
   - Açıklama: 'Toz oldu' tozlandı anlamına gelmez; 'örtü tozlandı' ya da 'örtü kirlendi' olmalı.
   - Açıklama: 'Toz oldu' yanlış anlamda; örtü 'tozlandı' ya da 'kirlendi' olmalı.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty en sevdiği turtanın en büyük dilimini annesine verdi"
   - Cümle 11: «Hello Kitty en sevdiği turtanın en büyük dilimini annesine verdi.»
   - Açıklama: Çözüm özür, ayakkabı çıkarma, silkme ve dilim vermeyle ikiden fazla adım sürüyor ve dilim vermek kirli örtüye yönelmiyor.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "turtanın en büyük dilimini annesine verdi"
   - Cümle 11: «Hello Kitty en sevdiği turtanın en büyük dilimini annesine verdi.»
   - Açıklama: Turta dilimi vermek kirlenmiş örtü sorununa yönelmiyor ve çözüm ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0171` birebir aynı, `@degisim: palmiye -> salıncak` (tutuyorsan), ardından `@onarim: 0e22031d49468ed0b5ed3fefc58a6b424748dea6`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0172 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0172
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'halat', fiil 'gezinmek', sıfat 'zor'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: parkta bir ses duydu ve nereden geldiğini merak etti | ağaçların arasında gezindi ve sesi yapan salıncağı buldu
@tohum: hello_kitty-0172
Parkta rüzgarlı bir sabah Hello Kitty arkadaşlarını bekliyordu. Birden bir yerden tuhaf bir ses geldi. Hello Kitty sesin nereden geldiğini çok merak etti. Ağaçların arasında yavaş yavaş gezindi. Ağaçlar çok fazlaydı ve sesi bulmak zordu. Hello Kitty her ağacın yanında durdu ve dinledi. Ses en büyük ağaçtan geliyordu. Bu ağacın dalına kalın bir halat bağlıydı. Ucunda tahtadan bir salıncak vardı. Rüzgar salıncağı sallıyordu ve dal gıcırdıyordu. Hello Kitty sesi bulduğu için güldü. Salıncağa oturdu ve arkadaşları gelene kadar mutlu mutlu sallandı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarını bekliyordu"
   - Cümle 1: «Parkta rüzgarlı bir sabah Hello Kitty arkadaşlarını bekliyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Salıncağa oturdu ve arkadaşları"
   - Cümle 12: «Salıncağa oturdu ve arkadaşları gelene kadar mutlu mutlu sallandı.»
   - Açıklama: Tek başına, gıcırdayan bir dala bağlı salıncağa oturmak taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0172` birebir aynı, ardından `@onarim: abd961a42c8c90e7865cca3e8541e78b5a85f870`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0173
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yorgan', fiil 'yırtılmak', sıfat 'ilginç'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası elmalı turtayı nereye koyduğunu unuttu | kokusunu tanıdı ve turtanın kutusunu ağacın arkasında buldu
@tohum: hello_kitty-0173
Bir sabah Hello Kitty ile babası parkta bir yorganın üstünde oturuyordu. Babası sepete baktı ama elmalı turtayı bulamadı. Turtayı nereye koyduğunu unutmuştu. "Turta nerede, hiç bilmiyorum," dedi babası. Hello Kitty havayı kokladı ve ilginç, tatlı bir koku aldı. Bu, en sevdiği elmalı turtanın kokusuydu. Hello Kitty kokunun geldiği yere doğru yürüdü. Büyük bir ağacın arkasında bir kutu duruyordu. Kutunun kağıdı biraz yırtılmıştı ve koku oradan geliyordu. "Baba, turta burada!" diye seslendi Hello Kitty. "Onu serin kalsın diye gölgeye koydum," dedi babası. Hello Kitty kutuyu babasıyla birlikte yorganın üstüne taşıdı. Babası çok sevindi, çünkü Hello Kitty turtayı bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir yorganın üstünde oturuyordu"
   - Cümle 1: «Bir sabah Hello Kitty ile babası parkta bir yorganın üstünde oturuyordu.»
   - Açıklama: Yorgan yatakta örtünülen şeydir; parkta oturulan şey 'örtü' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parkta bir yorganın üstünde"
   - Cümle 1: «Bir sabah Hello Kitty ile babası parkta bir yorganın üstünde oturuyordu.»
   - Açıklama: Parkta oturulan örtü için 'yorgan' yanlış kelime; 'örtü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0173` birebir aynı, ardından `@onarim: 6a882d3482b1d8f48ab3faf21ff2df9480ba40be`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0174 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0174
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'sos', fiil 'saklanmak', sıfat 'uslu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: sos kavanozunun kapağı çok sıkıydı ve açılmadı | kardeşinden yardım istedi ve kapağı birlikte açtılar
@tohum: hello_kitty-0174
@degisim: saklanmak -> tutmak
Hello Kitty ile Mimi ormandaki kamp yerinde sandviç yapıyordu. Hello Kitty sandviçlere domates sosu koymak istedi. Ama sos kavanozunun kapağı çok sıkıydı ve açılmadı. Hello Kitty kapağı çevirdi ama kapak hiç dönmedi. Mimi örtünün üstünde uslu uslu oturmuş, bekliyordu. "Mimi, en iyi arkadaşım, bana yardım eder misin?" diye sordu Hello Kitty. "Tabii, kavanozu ben tutarım," dedi Mimi. Mimi kavanozu iki eliyle sıkıca tuttu. Hello Kitty de kapağı bütün gücüyle çevirdi. Kapak sonunda açıldı. Hello Kitty sandviçlere biraz sos sürdü ve birini Mimi'ye verdi. Hello Kitty çok sevindi, çünkü kardeşiyle kapağı birlikte açmıştı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Mimi, en iyi arkadaşım, bana"
   - Cümle 6: «"Mimi, en iyi arkadaşım, bana yardım eder misin?" diye sordu Hello Kitty.»
   - Açıklama: Tohum özelliği yeni arkadaşlar edinmek; yalnız bir hitap olarak geçiyor ve sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşım, bana yardım"
   - Cümle 6: «"Mimi, en iyi arkadaşım, bana yardım eder misin?" diye sordu Hello Kitty.»
   - Açıklama: Tohumdaki özellik yeni arkadaş edinmek ve herkese iyi davranmak; hikayede yalnız hitapta anılıyor, çözümde işe yaramıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Mimi, en iyi arkadaşım"
   - Cümle 6: «"Mimi, en iyi arkadaşım, bana yardım eder misin?" diye sordu Hello Kitty.»
   - Açıklama: Mimi burada en iyi arkadaş olarak anılıyor ama son cümlede ve planda kardeş olarak geçiyor.
   - Açıklama: Hello Kitty Mimi'ye en iyi arkadaşım diyor ama son cümlede Mimi kardeşi olarak anılıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çünkü kardeşiyle kapağı birlikte"
   - Cümle 12: «Hello Kitty çok sevindi, çünkü kardeşiyle kapağı birlikte açmıştı.»
   - Açıklama: Mimi gövdede 'en iyi arkadaşım' diye anılıyor, kardeş olarak tanıtılmadan 'kardeşiyle' denmesi kimi gösterdiğini belirsizleştiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0174` birebir aynı, `@degisim: saklanmak -> tutmak` (tutuyorsan), ardından `@onarim: bdd48163e8576ad923879a747a59968cd541d1e7`, sonra gövde.
