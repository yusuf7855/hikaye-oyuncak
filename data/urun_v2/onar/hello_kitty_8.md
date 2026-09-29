# Editör görevi (onarım): Hello Kitty, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0026 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0026
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kayık', fiil 'birikmek', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: suda yüzdürecek bir kayığı yoktu | boş kurabiye kutusunu kapatıp suya koydu
@tohum: hello_kitty-0026
Bir sabah Hello Kitty parkta biriken yağmur suyunda yüzen bir yaprak gördü. O da bu sığ suda bir kayık yüzdürmek istedi. Ama yanında hiç kayık yoktu, çünkü parka sadece kurabiye kutusunu getirmişti. Hello Kitty kutuya baktı ve düşündü. Kurabiyeler bitmişti ve kutu boştu. Kutu hafifti ve kapağı sıkıca kapanıyordu. Hello Kitty kapağı kapattı ve kutuyu yavaşça suyun üstüne koydu. Kutu batmadı ve küçük bir kayık gibi durdu. Rüzgar esince kutu suyun öbür ucuna kadar gitti. Hello Kitty suyun kenarından yürüdü ve kutuyu geri aldı. Hello Kitty çok memnundu, çünkü kutusu gerçek bir kayık olmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu sığ suda bir"
   - Cümle 2: «O da bu sığ suda bir kayık yüzdürmek istedi.»
   - Açıklama: 'Sığ' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "parka sadece kurabiye kutusunu getirmişti"
   - Cümle 3: «Ama yanında hiç kayık yoktu, çünkü parka sadece kurabiye kutusunu getirmişti.»
   - Açıklama: Karttaki özellik kurabiye yapmayı sevmek, hikayede yalnız boş kutu kullanılıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kutusu gerçek bir kayık olmuştu"
   - Cümle 11: «Hello Kitty çok memnundu, çünkü kutusu gerçek bir kayık olmuştu.»
   - Açıklama: Kutu gerçek bir kayık olmadı, kayık gibi yüzdü; 'gerçek' yanlış anlamda kullanılmış.
   - Açıklama: Kutu gerçek bir kayık olmaz; 'gerçek' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0026` birebir aynı, ardından `@onarim: 2ea346d7e1f4298fafe846e85aecb9973b77d87d`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0028 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: ağacın altından garip bir ses geldi | sessizce bekledi ve kavuna düşen kozalağı gördü
@tohum: hello_kitty-0028
Bir sabah Hello Kitty ormandaki kamp yerinde oturuyordu ve biraz sıkılmıştı. Birden büyük bir ağacın altından garip bir ses geldi: tok, tok. Hello Kitty bu sesi çok merak etti. Ağaca doğru birkaç adım yürüdü ve baktı. Ağacın altında piknik sepeti duruyordu. Sepette kocaman bir kavun ve en sevdiği elmalı turta vardı. Hello Kitty sessizce bekledi. Sonra ağaçtan bir kozalak düştü ve kavuna çarptı: tok! Sesi yapan, düşen kozalaklardı. Hello Kitty değerli turtasını korumak için sepeti hemen açık bir yere çekti. Hello Kitty çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ormandaki kamp yerinde oturuyordu"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerinde oturuyordu ve biraz sıkılmıştı.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde Hello Kitty ormanda yanında büyük olmadan tek başına kalıyor ve garip sese doğru yürüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağacın altında piknik sepeti duruyordu"
   - Cümle 5: «Ağacın altında piknik sepeti duruyordu.»
   - Açıklama: Piknik sepeti kimin olduğu ve neden orada olduğu söylenmeden sebepsizce beliriyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty değerli turtasını"
   - Cümle 10: «Hello Kitty değerli turtasını korumak için sepeti hemen açık bir yere çekti.»
   - Açıklama: 'Değerli' turta için yanlış anlamda ve çocuğa uygun olmayan bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "değerli turtasını korumak için"
   - Cümle 10: «Hello Kitty değerli turtasını korumak için sepeti hemen açık bir yere çekti.»
   - Açıklama: 'Değerli' soyut bir kelime ve 3 yaşındaki çocuğun bilmeyeceği bir kullanım.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty değerli turtasını korumak için"
   - Cümle 10: «Hello Kitty değerli turtasını korumak için sepeti hemen açık bir yere çekti.»
   - Açıklama: Tohumdaki turta özelliği iki kez anılıyor ve sorunun (sesin kaynağı) çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0028` birebir aynı, ardından `@onarim: e35c6a731df422113546e1e94803ecceaaed9353`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0029 (deneme 1 -> 2)

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
Hello Kitty ile Mimi mutfakta sıcak çorbalarını içiyordu. Dışarısı çok rüzgarlıydı. Birden kapı rüzgarla açıldı ve içeri soğuk hava doldu. Hello Kitty kaşığını bıraktı ve kapıya gitti. Kapıyı itti, ama rüzgar çok güçlüydü ve kapı kapanmadı. "Mimi, bana yardım eder misin?" diye sordu Hello Kitty. Mimi hemen masadan kalktı ve kardeşinin yanına koştu. İkisi "Bir, iki, üç!" diye saydı ve kapıyı birlikte itti. Kapı yavaşça kapandı. Mutfak yine sıcacık oldu. İkisi masaya döndü ve çorbalarını bitirdi. "Teşekkürler, Mimi, sen benim en iyi arkadaşımsın!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen benim en iyi arkadaşımsın"
   - Cümle 12: «"Teşekkürler, Mimi, sen benim en iyi arkadaşımsın!" dedi Hello Kitty.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği yalnız son replikte anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Karttaki arkadaş edinme özelliği yalnız sondaki bir sözde anılıyor, sorunun çözümünde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0029` birebir aynı, ardından `@onarim: bfb4041a3061e28f9d4416d11d6103b394e2c1f8`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0030 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0030
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'koni', fiil 'taşımak', sıfat 'değişik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesinin elleri doluydu ve sepet kayıyordu | sepeti annesinden alıp iki eliyle taşıdı
@tohum: hello_kitty-0030
@degisim: koni -> sepet
Hello Kitty ile annesi ormandaki kamp yerine doğru yürüyordu. Annesinin iki elinde de büyük çantalar vardı. Kolundaki sepet de kayıyordu, çünkü annesi onu tutamıyordu. Sepette, Hello Kitty'nin annesiyle yaptığı değişik şekilli kurabiyeler vardı. "Anne, sepeti ben taşıyabilir miyim?" diye sordu Hello Kitty. "Tabii, ama iki elinle sıkıca tut," dedi annesi. Hello Kitty sepeti annesinin kolundan dikkatle aldı. Onu iki eliyle tuttu ve yavaş yavaş yürüdü. Kurabiyelerin hiçbiri yere düşmedi. Kamp yerine gelince sepeti bir ağacın altına koydu. "Çok yardımcı oldun, kızım," dedi annesi ve ona sarıldı. Hello Kitty bundan sonra annesinin elleri dolu olunca ona hemen yardım etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "annesiyle yaptığı değişik şekilli kurabiyeler"
   - Cümle 4: «Sepette, Hello Kitty'nin annesiyle yaptığı değişik şekilli kurabiyeler vardı.»
   - Açıklama: Tohumdaki kurabiye yapma özelliği yalnız sepetin içeriği olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0030` birebir aynı, `@degisim: koni -> sepet` (tutuyorsan), ardından `@onarim: 36ab645278b2f9bd7f90e7739e76f0d8b7f0ff3f`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0032 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0032
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sırayla oynamak
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'damla', fiil 'almak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: ikisi de davula aynı anda vurdu | kardeşiyle sırayla davul çaldı
@tohum: hello_kitty-0032
@degisim: damla -> davul
Bir sabah Hello Kitty ile Mimi parkta ağacın gölgesinde piknik yapıyordu. Mimi yanında oyuncak bir davul getirmişti. İkisi de aynı anda davula vurdu ve çok gürültülü bir ses çıktı. Hello Kitty durdu ve biraz düşündü. "Sırayla çalalım mı, Mimi?" diye sordu Hello Kitty. "Olur, ama önce sen çal," dedi Mimi. Hello Kitty davula beş kez vurdu. Sonra davulu Mimi'ye verdi ve "Sıra sende, Mimi," dedi. Mimi çalarken Hello Kitty en sevdiği elmalı turtadan bir dilim aldı. Şimdi davulun sesi güzel ve neşeliydi. Hello Kitty bundan sonra tek oyuncak olunca hep sırayla oynadı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği elmalı turtadan bir dilim aldı"
   - Cümle 9: «Mimi çalarken Hello Kitty en sevdiği elmalı turtadan bir dilim aldı.»
   - Açıklama: Tohumdaki turta özelliği sorunla ilgisiz bir ek olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Kartın özellikler alanındaki elmalı turta sevgisi davul sorununun çözümünde işe yaramıyor, yalnız araya ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty en sevdiği elmalı turtadan bir dilim aldı"
   - Cümle 9: «Mimi çalarken Hello Kitty en sevdiği elmalı turtadan bir dilim aldı.»
   - Açıklama: Turta sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği elmalı turtadan bir dilim aldı"
   - Cümle 9: «Mimi çalarken Hello Kitty en sevdiği elmalı turtadan bir dilim aldı.»
   - Açıklama: Turta sebepsiz beliriyor ve olayda hiçbir işlev görmüyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra tek oyuncak olunca"
   - Cümle 11: «Hello Kitty bundan sonra tek oyuncak olunca hep sırayla oynadı.»
   - Açıklama: 'tek oyuncak olunca' öznesi belirsiz ve bozuk; Hello Kitty oyuncak olmuş gibi okunuyor, 'tek bir oyuncak olunca' gibi kurulmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0032` birebir aynı, `@degisim: damla -> davul` (tutuyorsan), ardından `@onarim: fff4e2c07bf5ab0b9a88336d98f13c4672b8d6c8`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0033 (deneme 1 -> 2)

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
Hello Kitty pencerenin önünde oturmuş, gökyüzündeki aya bakıyordu. Bir ay resmi yapıp yeni arkadaşına vermek istiyordu. Ama çizdiği ay yuvarlak olmadı, çünkü eli hep kayıyordu. Hello Kitty resme baktı ve çok üzüldü. Annesi de odadaydı. "Anne, ay yuvarlak olmuyor, bana yardım eder misin?" diye sordu Hello Kitty. Annesi gülümsedi ve ona bir bardak verdi. "Bardağı kağıda koy ve çevresini çiz," dedi annesi. Hello Kitty bardağı kağıda koydu ve kalemle etrafından yavaşça çizdi. Kağıtta kocaman bir ay oldu. Sevinçle annesine sıcacık sarıldı. Hello Kitty bundan sonra bir şeyi yapamayınca annesinden yardım istedi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşına vermek istiyordu"
   - Cümle 2: «Bir ay resmi yapıp yeni arkadaşına vermek istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Bir ay resmi yapıp yeni arkadaşına vermek istiyordu"
   - Cümle 2: «Bir ay resmi yapıp yeni arkadaşına vermek istiyordu.»
   - Açıklama: Resmi yeni arkadaşa verme hedefi kuruluyor ama hikaye bu hedefe hiç dönmeden bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0033` birebir aynı, ardından `@onarim: e7b99de39dabecff55f55c3f695f0879631f63ca`, sonra gövde.
