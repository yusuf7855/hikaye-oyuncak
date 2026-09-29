# Editör görevi (onarım): Hello Kitty, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar2.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kova çok hafifti ve top düşünce devrildi | kovanın içine taş koyup onu ağır yaptı
@tohum: hello_kitty-0001
@degisim: faydalı -> ağır
Parkta serin ve güneşli bir sabahtı. Hello Kitty ağaçların gölgesinde komik bir top oyunu oynuyordu. Topu uzaktan kırmızı kovaya atıyordu. Ama kova çok hafifti ve top içine düşünce kova devrildi. Top da çimenlerde uzağa yuvarlandı. Hello Kitty yeni arkadaşlar edinmeyi çok severdi. Bu oyunu onlara da göstermek istiyordu. Topun arkasından çimenlerde koşturdu ve onu geri getirdi. Sonra ağacın altından üç küçük taş topladı. Taşları kovanın içine koydu ve kova ağır oldu. Hello Kitty topu yine attı. Top kovaya düştü ve kova hiç devrilmedi. Hello Kitty sevinçle zıpladı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kova çok hafifti"
   - Cümle 4: «Ama kova çok hafifti ve top içine düşünce kova devrildi.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 6: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: 'Arkadaş edinmek' soyut bir ifade ve küçük çocuğa uygun değil.
   - Açıklama: 'Edinmek' 3 yaşındaki bir çocuğun bilmediği soyut bir kelimedir.
   - Açıklama: 'Arkadaş edinmek' soyut bir ifade ve 'edinmek' 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 6: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: Özellik karttaki cümleyle sayılıyor ve sorunun çözümünde hiç işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği karttaki cümle gibi sayılıyor ve sorunun çözümüne hiç katkı vermiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty yeni arkadaşlar edinmeyi çok severdi"
   - Cümle 6: «Hello Kitty yeni arkadaşlar edinmeyi çok severdi.»
   - Açıklama: Arkadaş edinme ve oyunu onlara gösterme isteği kuruluyor ama hikayede hiç kullanılmıyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bu oyunu onlara da göstermek istiyordu"
   - Cümle 7: «Bu oyunu onlara da göstermek istiyordu.»
   - Açıklama: 'Onlara' zamiri sahnede olmayan belirsiz arkadaşları gösteriyor; kimi kastettiği belli değil.
   - Açıklama: 'Onlara' zamiri sahnede olmayan, belirsiz arkadaşları gösteriyor; kimi kastettiği belli değil.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu oyunu onlara da göstermek istiyordu"
   - Cümle 7: «Bu oyunu onlara da göstermek istiyordu.»
   - Açıklama: Arkadaşlara oyunu gösterme isteği kuruluyor ama hikayede hiç arkadaş çıkmıyor ve bu ayrıntı işlevsiz kalıyor.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Topun arkasından çimenlerde koşturdu"
   - Cümle 8: «Topun arkasından çimenlerde koşturdu ve onu geri getirdi.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; yanında büyük olmayan Hello Kitty uzağa yuvarlanan topun ardından koşuyor.
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor; Hello Kitty parkta tek başına uzağa yuvarlanan topun peşinden koşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0001` birebir aynı, `@degisim: faydalı -> ağır` (tutuyorsan), ardından `@onarim: 1120b547b00bdd437f834d73fc7e3273460ddeb0`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0002 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kurdelenin düğümü sıkı değildi ve kurdele düştü | eğildiği dolabı hatırlayıp içini aradı
@tohum: hello_kitty-0002
@degisim: ilgilenmek -> aramak
Dışarıda hava güneşliydi ve kuşlar ötüyordu. Hello Kitty mutfakta oyun hamurundan kurabiye yapıyordu. Birden başına dokundu ama kırmızı kurdelesi orada yoktu. Kurdelenin düğümü sıkı değildi ve kurdele bir yere düşmüştü. Hello Kitty bu kurdeleyi çok seviyordu. Önce masanın altına baktı ama kurdele orada yoktu. Sonra biraz düşündü. Az önce hamur kalıbı almak için alt dolaba eğilmişti. Hello Kitty dolabı açtı ve içini dikkatle aradı. Kırmızı kurdele en altta duruyordu! Hello Kitty kurdeleyi aldı ve başına sıkı bir düğümle bağladı. Sonra işine döndü ve hamurdan kalp şekilli kurabiyeler yaptı. Hello Kitty kırmızı kurdelesiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "oyun hamurundan kurabiye yapıyordu"
   - Cümle 2: «Hello Kitty mutfakta oyun hamurundan kurabiye yapıyordu.»
   - Açıklama: Tohumdaki kurabiye özelliği yalnız arka plan etkinliği olarak geçiyor ve kurdele sorununun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hamurdan kalp şekilli kurabiyeler yaptı"
   - Cümle 12: «Sonra işine döndü ve hamurdan kalp şekilli kurabiyeler yaptı.»
   - Açıklama: Tohumdaki kurabiye özelliği iki kez geçiyor ve kurdele sorununun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0002` birebir aynı, `@degisim: ilgilenmek -> aramak` (tutuyorsan), ardından `@onarim: e080e0c13ee25b4b82986a420da5a9e5e46f4b22`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0005 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: eskimiş kalp kalıbı oyunun ortasında kırıldı | bardağın ağzını hamura bastırıp kurabiye kesti
@tohum: hello_kitty-0005
@degisim: yosun -> bardak
Bir sabah Hello Kitty ile Mimi mutfakta çay partisi oyunu oynuyordu. Parti için oyun hamurundan kurabiyeler yapacaklardı. Ama eskimiş kalp kalıbı Mimi'nin elinde ikiye kırıldı. "Şimdi kurabiyeleri nasıl keseceğiz?" dedi Mimi üzgün üzgün. Hello Kitty etrafa baktı ve masadaki boş bardağı aldı. Bardağın ağzını hamura yavaşça bastırdı. Bardak hamura değince yuvarlak bir kurabiye çıktı. "Şimdi sen dene, Mimi," dedi Hello Kitty. Mimi de bardakla bir kurabiye kesti ve gülümsedi. İki kardeş oyun tabaklarını kurabiyelerle doldurdu. "Teşekkürler, Hello Kitty, şimdi oyuna başlayalım!" dedi Mimi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İki kardeş oyun tabaklarını kurabiyelerle doldurdu"
   - Cümle 10: «İki kardeş oyun tabaklarını kurabiyelerle doldurdu.»
   - Açıklama: Tabak kaybolmuşken sonunda tabaklar hiçbir açıklama olmadan kurabiyelerle dolduruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0005` birebir aynı, `@degisim: yosun -> bardak` (tutuyorsan), ardından `@onarim: 17ef18cf4483044c795a9e3ab4092e280079fd75`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0008 (deneme 2 -> 3)

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
Bir sabah Hello Kitty parkta kukla oyunu oynamak istedi. İki ağacın arasına bir ip gerdi ve renkli bir perde astı. Ama ip sıkı değildi ve perde hemen çimenlere düştü. Hello Kitty ipi iki eliyle sıkıca çekti. Sonra ipin ucunu ağaca yeniden bağladı. Perdeyi tekrar astı ve bu kez perde düşmedi. Hello Kitty perdenin arkasına geçti ve kukla oyununa başladı. Oyunda Hello Kitty yeni arkadaşlar bulan bir kediyi oynadı. Hello Kitty çok sevindi, çünkü kukla oyunu sonunda başlamıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Oyunda Hello Kitty yeni arkadaşlar bulan bir kediyi oynadı"
   - Cümle 8: «Oyunda Hello Kitty yeni arkadaşlar bulan bir kediyi oynadı.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız oyun içinde süs olarak anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki arkadaş özelliği sona eklenmiş, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0008` birebir aynı, `@degisim: biberli -> renkli` (tutuyorsan), ardından `@onarim: 6274e2c63d0f68237da0b6c3a0857fbf63ad651b`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0009 (deneme 2 -> 3)

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
Ormandaki kamp yerinde hava serindi. Hello Kitty'nin babası çadırı kurmuştu ve çok yorulmuştu. Babası bir kütüğe oturmak istedi ama kütük sallandı, çünkü yer düz değildi. "Bu kütük hiç durmuyor, kızım!" dedi babası ve güldü. Hello Kitty etrafa baktı ve düz bir yer aradı. Ağaçların arasında düz bir yer buldu. "Baba, kütüğü buraya getirelim," dedi Hello Kitty. Babası kütüğü yavaşça oraya yuvarladı. Kütük artık hiç sallanmıyordu. Hello Kitty çadırın önündeki su testisini de getirdi, çünkü babası yorgundu. "Teşekkürler, kızım, sen çok iyi bir kamp arkadaşısın," dedi babası. Sonra ikisi kütükte yan yana oturup testiden mutlu mutlu su içti.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "düz bir yer buldu ve babasından yardım istedi"
   - Cümle 0 (plan satırı): «kütük sallanıyordu çünkü yer düz değildi | düz bir yer buldu ve babasından yardım istedi»
   - Açıklama: Plan düz yeri Hello Kitty'nin bulduğunu söylüyor ama gövdede yeri babası buluyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "su testisini de getirdi"
   - Cümle 10: «Hello Kitty çadırın önündeki su testisini de getirdi, çünkü babası yorgundu.»
   - Açıklama: 'Testi' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty çadırın önündeki su testisini de getirdi"
   - Cümle 10: «Hello Kitty çadırın önündeki su testisini de getirdi, çünkü babası yorgundu.»
   - Açıklama: Sorun çözüldükten sonra sorunla ilgisi olmayan su testisi olayı ekleniyor.
   - Açıklama: Su testisi önceden kurulmadan beliriyor ve sorunla ilgisi olmayan ikinci bir olay ekliyor.
   - Açıklama: Sorun çözüldükten sonra testi sebepsiz beliriyor ve kütük sorunuyla ilgisi olmayan ikinci bir olay ekleniyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çok iyi bir kamp arkadaşısın"
   - Cümle 11: «"Teşekkürler, kızım, sen çok iyi bir kamp arkadaşısın," dedi babası.»
   - Açıklama: Tohumdaki özellik yeni arkadaş edinmek; yalnız babanın sözünde etiket olarak geçiyor, çözümde işe yaramıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen çok iyi bir kamp arkadaşısın"
   - Cümle 11: «"Teşekkürler, kızım, sen çok iyi bir kamp arkadaşısın," dedi babası.»
   - Açıklama: Karttaki yeni arkadaş edinme özelliği kullanılmıyor; özellik yalnız babanın övgü sözünde kelime olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0009` birebir aynı, `@degisim: hareketli -> düz` (tutuyorsan), ardından `@onarim: 05ee68fab2a6d6a6071a6c723560b211aa70d058`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0011 (deneme 2 -> 3)

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
@degisim: çevik -> hızlı
Yağmur yeni dinmişti ve çimenler ıslaktı. Hello Kitty ile babası parkta piknik yapıyordu. Babasının meyvesi elinden kaydı, yuvarlandı ve çamura düştü. Hello Kitty hızlı hızlı koştu ama meyveye yetişemedi. "Meyvem çamurlu oldu, kızım!" dedi babası ve komik bir yüz yaptı. Sepette başka meyve yoktu. Hello Kitty kendi kutusunu açtı. Kutuda babasıyla yaptığı kurabiyeler vardı. Hello Kitty kurabiyelerin yarısını babasına verdi. "Buyur, babacığım, birlikte yiyelim," dedi Hello Kitty. Babası bir kurabiye yedi ve gülümsedi. "Çok lezzetli, teşekkürler, kızım," dedi babası. Hello Kitty paylaşınca babasının da çok sevindiğini gördü.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve komik bir yüz yaptı"
   - Cümle 5: «"Meyvem çamurlu oldu, kızım!" dedi babası ve komik bir yüz yaptı.»
   - Açıklama: 'Yüz yapmak' Türkçede doğal bir kullanım değil, İngilizceden çeviri gibi duruyor; 'komik bir surat yaptı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0011` birebir aynı, `@degisim: çevik -> hızlı` (tutuyorsan), ardından `@onarim: 7fdf0cdd9f6502b84b4a873774ab4af4c626e25f`, sonra gövde.
