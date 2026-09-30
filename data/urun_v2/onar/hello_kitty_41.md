# Editör görevi (onarım): Hello Kitty, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar41.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0139 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: resmin üstüne küçük sarı şeyler düşüyordu | çiçekleri üfledi ve güneşli bir yere oturdu
@tohum: hello_kitty-0139
Hello Kitty parkta bir ağacın gölgesinde oturuyordu. Yeni arkadaşlarına vermek için kağıda resim çiziyordu. Ama resmin üstüne küçük sarı şeyler düşüyordu. Hello Kitty bunların ne olduğunu çok merak etti. Bir tanesini eline aldı. O sarı şey çok hafif ve yumuşaktı. Sonra başını kaldırıp ağaca baktı. Dallarda limon sarısı küçük çiçekler vardı. Rüzgar esince çiçekler dallardan resmin üstüne düşüyordu. Hello Kitty çiçekleri resmin üstünden yavaşça üfledi. Sonra çimenlerde güneşli bir yere oturdu. Artık resmin üstüne hiç çiçek düşmedi. Hello Kitty resmini çizmeye mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına vermek için"
   - Cümle 2: «Yeni arkadaşlarına vermek için kağıda resim çiziyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Karttaki yeni arkadaş edinme özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0139` birebir aynı, ardından `@onarim: 2e246bb5243fe98e13c483bd462f46d998c6cdfd`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0140 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0140
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'süpürge', fiil 'yarışmak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: oyunda elmalı turta yapacaktı ama elması yoktu | kozalakları toplayıp taşın üstüne dizdi
@tohum: hello_kitty-0140
@degisim: yarışmak -> toplamak
Rüzgar ağaçların arasında yavaş yavaş esiyordu. Hello Kitty ormandaki kamp yerinde, çadırların yanında yemek oyunu oynuyordu. Oyunda sağlıklı bir elmalı turta yapacaktı, ama hiç elması yoktu. Hello Kitty etrafına baktı ve yerde yuvarlak kozalaklar gördü. Kozalaklar küçük elmalara benziyordu. Kuru bir dalı süpürge gibi kullandı ve kozalakları bir yere topladı. Sonra kozalakları düz bir taşın üstüne daire şeklinde dizdi. Taşın üstünde yuvarlak bir kozalak turtası oldu. Hello Kitty turtasına baktı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde, çadırların yanında yemek oyunu oynuyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormandaki kamp yerinde bir büyük olmadan yalnız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0140` birebir aynı, `@degisim: yarışmak -> toplamak` (tutuyorsan), ardından `@onarim: 2e20213f32962169edb76d5faa353e4489b37d9e`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0142 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0142
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'bant', fiil 'paylaşmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: koşarken kardeşinin uçurtmasına bastı ve yırttı | özür diledi ve kutunun bandıyla yırtık yeri yapıştırdı
@tohum: hello_kitty-0142
@degisim: düzenli -> yapışkan
Hello Kitty ile Mimi parkta uçurtma uçurmaya hazırlanıyordu. Çimenlerin üstünde, evde birlikte yaptıkları kurabiyelerin kutusu duruyordu. Hello Kitty koşarken Mimi'nin kağıt uçurtmasına bastı ve uçurtma yırtıldı. Mimi yırtık uçurtmaya baktı ve çok üzüldü. Hello Kitty hemen kardeşinin yanına oturdu ve ondan özür diledi. Sonra kurabiye kutusuna baktı. Kutunun kapağında yapışkan bir bant vardı. Hello Kitty bandı kapaktan yavaşça çekip aldı. Yırtık yeri bu bantla dikkatlice yapıştırdı. Rüzgar esince uçurtma yükseldi. Mimi sevindi ve Hello Kitty'ye sarıldı. Sonra ikisi kurabiyeleri paylaştı ve uçurtmayı mutlu mutlu uçurdu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "evde birlikte yaptıkları kurabiyelerin"
   - Cümle 2: «Çimenlerin üstünde, evde birlikte yaptıkları kurabiyelerin kutusu duruyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kurabiye bir büyükle yapılır, burada iki kardeşin büyük olmadan kurabiye yaptığı anlatılıyor.
   - Açıklama: Güvenli kullanım satırına göre kurabiye bir büyükle yapılır, burada iki kardeş büyük olmadan yapmış görünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0142` birebir aynı, `@degisim: düzenli -> yapışkan` (tutuyorsan), ardından `@onarim: 99d00d4ec61431bacdf09cb0926cddbc8418a01f`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0143 (deneme 3 -> 4)

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
Hello Kitty babasıyla parkta, ağacın gölgesinde piknik yapıyordu. Babası yanında uyuyordu ve örtüde elmalı turta vardı. Hello Kitty topla oynarken top babasının bardağını devirdi. Soğuk meyve suyu babasının eline döküldü. Babası gözlerini açtı ve ıslak eline baktı. Hello Kitty hemen yanına koştu. "Özür dilerim, babacığım, hiç dikkat etmedim," dedi Hello Kitty. Sonra meyve suyu şişesini aldı ve bardağı yeniden doldurdu. Babası bir yudum içti ve kızına sarıldı. Babası artık uyanıktı, bu yüzden turtayı birlikte yediler. İkisi pikniklerine mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Babası artık uyanıktı, bu yüzden turtayı birlikte yediler"
   - Cümle 10: «Babası artık uyanıktı, bu yüzden turtayı birlikte yediler.»
   - Açıklama: Tohum özelliği (en çok elmalı turtayı sevmek) yalnız dekor olarak geçiyor, sorunda ya da çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0143` birebir aynı, `@degisim: demet -> bardak` (tutuyorsan), ardından `@onarim: bd330823beea8f70456444849ad995da07eeb4fc`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0144 (deneme 3 -> 4)

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
Dışarıda sessizce kar yağıyordu. Hello Kitty mutfaktaki pencereden kara bakmak istedi. Ama mutfak çok sıcaktı ve camın üstü su damlalarıyla doluydu. Hello Kitty kurabiye yapmayı çok severdi ve yıldız kalıbını hemen getirdi. Plastik kalıp camı kırmazdı, güvenliydi. Hello Kitty kalıbı cama tuttu ve içini parmağıyla yavaşça ovdu. Camda yıldız şeklinde küçük, temiz bir yer açıldı. Hello Kitty yıldızın içinden dışarıya baktı. Beyaz kar taneleri yavaş yavaş yere düşüyordu. Hello Kitty karı görünce çok sevindi. Hello Kitty bundan sonra cam ıslanınca hep böyle bir yıldız açtı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty kurabiye yapmayı çok severdi ve yıldız kalıbını hemen getirdi"
   - Cümle 4: «Hello Kitty kurabiye yapmayı çok severdi ve yıldız kalıbını hemen getirdi.»
   - Açıklama: Kurabiye kalıbı buğuyu silmeye bir katkı sağlamadan sebepsizce çözüme getiriliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "camı kırmazdı, güvenliydi"
   - Cümle 5: «Plastik kalıp camı kırmazdı, güvenliydi.»
   - Açıklama: 'Güvenli' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Güvenli' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kalıbı cama tuttu"
   - Cümle 6: «Hello Kitty kalıbı cama tuttu ve içini parmağıyla yavaşça ovdu.»
   - Açıklama: Buğuyu silmek için parmak yeterken çözüm kalıp dolambacından geçiyor ve sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0144` birebir aynı, `@degisim: pul -> kalıp` (tutuyorsan), ardından `@onarim: ad16ec707440bfe339601d9d2bee1c45182201d0`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0148 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: tabaktaki yıldız kurabiye birden görünmüyordu | tostu kaldırıp altına yapışan kurabiyeyi buldu
@tohum: hello_kitty-0148
Ormandaki kamp yerinde Hello Kitty çadırın hemen önünde oturuyordu. Turuncu tabağında ballı bir tost ve yıldız şeklinde bir kurabiye vardı. Tostunu biraz yedi ve geri koydu, ama sonra kurabiyeyi göremedi. Hello Kitty kurabiyenin nereye gittiğini çok merak etti. Önce tabağın yanına ve otların arasına baktı. Kurabiye orada da yoktu. Sonra tostu eline aldı ve altına baktı. Tostun altından küçük bir yıldız ucu görünüyordu. Hello Kitty kurabiye yapmayı çok severdi ve kendi kurabiyesini hemen tanıdı. Bal, kurabiyeyi tostun altına yapıştırmıştı. Kurabiyeyi yavaşça çekip aldı. Hello Kitty çok sevindi, çünkü kurabiyesini bulmuştu.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tabaktaki yıldız kurabiye birden görünmüyordu"
   - Cümle 0 (plan satırı): «tabaktaki yıldız kurabiye birden görünmüyordu | tostu kaldırıp altına yapışan kurabiyeyi buldu»
   - Açıklama: Plan satırında 'yıldız kurabiye' tamlaması eksik ekli ('yıldız kurabiyesi' ya da 'yıldız şeklindeki kurabiye' olmalı) ve 'birden' sürekli olumsuz fiille uyumsuz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yıldız kurabiye birden görünmüyordu"
   - Cümle 0 (plan satırı): «tabaktaki yıldız kurabiye birden görünmüyordu | tostu kaldırıp altına yapışan kurabiyeyi buldu»
   - Açıklama: 'Birden' ile süreklilik bildiren 'görünmüyordu' uyuşmuyor ve tamlama 'yıldız kurabiyesi' olmalı.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ormandaki kamp yerinde Hello Kitty çadırın"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty çadırın hemen önünde oturuyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormandaki kamp yerinde bir büyük olmadan yalnız.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kendi kurabiyesini hemen tanıdı"
   - Cümle 9: «Hello Kitty kurabiye yapmayı çok severdi ve kendi kurabiyesini hemen tanıdı.»
   - Açıklama: Kurabiye zaten kendi tabağında olduğu için tanıma ayrıntısı işlevsiz ve olaya bir şey katmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kurabiye yapmayı çok severdi ve kendi kurabiyesini hemen tanıdı"
   - Cümle 9: «Hello Kitty kurabiye yapmayı çok severdi ve kendi kurabiyesini hemen tanıdı.»
   - Açıklama: Tabakta tek kurabiye varken onu tanıması hiçbir işe yaramayan, özelliği sokmak için eklenmiş işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0148` birebir aynı, ardından `@onarim: 929e44a8044ccaa81190d6e1a6d967819dde9b69`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0152 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Bir sabah orman bulutlu ve serindi. Hello Kitty kamp yerinde, çadırının yanında sarı kelebekler gördü. Ama oradaki çiçekler kuruydu ve kelebekler hep uzakta uçuyordu. Hello Kitty arkadaşlarına olduğu gibi kelebeklere de yardım etmek istedi. Çantasından su şişesini aldı ve suyu avucuna döktü. Sonra onu damla damla çiçeklerin üstüne serpti. Hello Kitty sessizce bekledi. Biraz sonra kelebekler ıslak çiçeklere kondu. Artık kelebekler Hello Kitty'nin çok yakınındaydı. Hello Kitty kelebekleri izleyerek çiçeklerin yanında mutlu mutlu oturdu.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde, çadırının yanında"
   - Cümle 2: «Hello Kitty kamp yerinde, çadırının yanında sarı kelebekler gördü.»
   - Açıklama: Güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmediğini söylüyor, Hello Kitty ormandaki kamp yerinde yetişkinsiz yalnız.
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylerken Hello Kitty ormanda büyük olmadan yalnız.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "oradaki çiçekler kuruydu ve kelebekler hep uzakta uçuyordu"
   - Cümle 3: «Ama oradaki çiçekler kuruydu ve kelebekler hep uzakta uçuyordu.»
   - Açıklama: Kelebeklerin uzakta uçması çocuğun önemseyeceği net bir sorun değil ve kuru çiçeklere birkaç damla serpmenin onları çekmesi zayıf bir sebep bağı.
   - Açıklama: Kuru çiçeklerin kelebekleri uzak tuttuğu ve birkaç damla suyla hemen yakına getirdiği sebebi akla pek yatkın değil.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "arkadaşlarına olduğu gibi kelebeklere"
   - Cümle 4: «Hello Kitty arkadaşlarına olduğu gibi kelebeklere de yardım etmek istedi.»
   - Açıklama: Yapı eksik ve bozuk; 'arkadaşlarına yaptığı gibi' olmalı.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "kelebekler ıslak çiçeklere kondu"
   - Cümle 8: «Biraz sonra kelebekler ıslak çiçeklere kondu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün parçası olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0152` birebir aynı, `@degisim: köpük -> su` (tutuyorsan), ardından `@onarim: 6061e45e04f8ebd75af59e93588b3a0694a9d635`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0153 (deneme 2 -> 3)

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
Hello Kitty babasıyla mutfakta elmalı turta yapıyordu. Bu kez turtanın üstüne fındık koymayı denedi. Ama yuvarlak fındıklar hamurun üstünden kaydı ve masaya düştü. "Babacığım, fındıklar durmuyor!" dedi Hello Kitty. Hello Kitty en sevdiği turtada fındıkların durmasını istedi. Fındıkları tek tek parmağıyla hamura hafifçe bastırdı. Artık hiçbiri kaymadı. Babası uzun hamur şeritlerini turtanın üstüne dizdi. "Çok güzel oldu, kızım!" dedi babası. Sonra babası turtayı fırına koydu. Biraz sonra mutfak elma ve fındık kokusuyla doldu. Hello Kitty çok sevindi, çünkü ilk fındıklı turtasını yapmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra babası turtayı fırına"
   - Cümle 10: «Sonra babası turtayı fırına koydu.»
   - Açıklama: 'Babası' art arda üç cümlede tekrarlanıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0153` birebir aynı, `@degisim: kaydetmek -> kaymak` (tutuyorsan), ardından `@onarim: 1d1f1bf53eb42d07f8faf337ef21b6d399b015b2`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0154 (deneme 2 -> 3)

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
Hello Kitty parkta top oynuyordu. Gökyüzü berrak ve maviydi. Ama top yükseğe zıpladı ve bir ağacın dalına takıldı. Hello Kitty zıpladı, ama topa ulaşamadı. Annesi yakında, ağacın gölgesinde üzüm yiyordu. Hello Kitty annesinin yanına gitti ve yardım istedi. Annesi kalktı ve uzun koluyla topu daldan aldı. Hello Kitty annesine sarıldı ve teşekkür etti. Sonra annesini de arkadaşları gibi oyuna çağırdı. İkisi birlikte top oynadı. Hello Kitty çok mutluydu, çünkü topu geri almıştı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Gökyüzü berrak ve maviydi"
   - Cümle 2: «Gökyüzü berrak ve maviydi.»
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "annesini de arkadaşları gibi oyuna çağırdı"
   - Cümle 9: «Sonra annesini de arkadaşları gibi oyuna çağırdı.»
   - Açıklama: Hikayede arkadaş yokken 'arkadaşları gibi' ifadesinin ne anlattığı belirsiz.
   - Açıklama: Sahnede olmayan arkadaşlarla yapılan karşılaştırma anlamsız ve kafa karıştırıcı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "annesini de arkadaşları gibi oyuna çağırdı"
   - Cümle 9: «Sonra annesini de arkadaşları gibi oyuna çağırdı.»
   - Açıklama: Tohumdaki arkadaş özelliği sorun çözüldükten sonra anılıyor, çözümde işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra annesini de arkadaşları gibi oyuna çağırdı"
   - Cümle 9: «Sonra annesini de arkadaşları gibi oyuna çağırdı.»
   - Açıklama: Karttaki yeni arkadaş edinme özelliği sorun çözüldükten sonra yalnız anılıyor, işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra annesini de arkadaşları gibi oyuna çağırdı"
   - Cümle 9: «Sonra annesini de arkadaşları gibi oyuna çağırdı.»
   - Açıklama: Hikayede hiç görünmeyen arkadaşlar sebepsizce anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0154` birebir aynı, ardından `@onarim: 9702d5024f94efbd915c8c22798d84aea0da515d`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: yukarıdan su damladı ve turta ıslandı | dallara bakıp suyun ıslak yapraklardan geldiğini buldu
@tohum: hello_kitty-0156
@degisim: hazırlıklı -> yumuşak
Bir sabah Hello Kitty babasıyla parkta piknik yapıyordu. İkisi ağacın gölgesinde oturuyordu ve önlerinde elmalı bir turta vardı. Birden yukarıdan su damladı ve Hello Kitty ile turta ıslandı. Ama gökyüzünde hiç bulut yoktu. Hello Kitty bu suyun nereden geldiğini çok merak etti. Başını kaldırdı ve ağacın dallarına baktı. Yapraklar sabahki yağmurdan ıslaktı. Rüzgar esince onlardan aşağı su dökülüyordu. "Baba, su ağaçtan geliyor!" dedi Hello Kitty. Hello Kitty en sevdiği turtayı hemen güneşli çimenlere taşıdı. Babası da sepeti getirdi ve içinden yumuşak bir havlu çıkardı. Hello Kitty havluyla güzelce kurulandı. Hello Kitty çok sevindi, çünkü suyun ağaçtan geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "suyun ıslak yapraklardan geldiğini buldu"
   - Cümle 0 (plan satırı): «yukarıdan su damladı ve turta ıslandı | dallara bakıp suyun ıslak yapraklardan geldiğini buldu»
   - Açıklama: Plan çözümü yalnız kaynağı bulmak olarak veriyor; gövdede asıl çözüm turtayı güneşli çimenlere taşımak.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "suyun nereden geldiğini çok merak etti"
   - Cümle 5: «Hello Kitty bu suyun nereden geldiğini çok merak etti.»
   - Açıklama: Tohumdaki özellik turta; çözümü merak getiriyor ve merak ikinci bir özellik olarak ekleniyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hello Kitty çok sevindi"
   - Cümle 13: «Hello Kitty çok sevindi, çünkü suyun ağaçtan geldiğini bulmuştu.»
   - Açıklama: Son dört cümlenin üçü gereksiz yere 'Hello Kitty' adıyla başlıyor ve 12. cümleden hemen sonra ad yeniden tekrarlanıyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "suyun ağaçtan geldiğini bulmuştu"
   - Cümle 13: «Hello Kitty çok sevindi, çünkü suyun ağaçtan geldiğini bulmuştu.»
   - Açıklama: Sorun turtanın ıslanmasıydı ama turta hiç kurutulmuyor ve son yalnız suyun kaynağını bulmaya dönüyor, asıl sorunun çözüldüğü görünmüyor.
   - Açıklama: Sorun turtanın ıslanmasıydı ama turtanın durumu çözülmeden son, yalnız suyun kaynağının bulunmasına seviniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0156` birebir aynı, `@degisim: hazırlıklı -> yumuşak` (tutuyorsan), ardından `@onarim: bc6542aea96b6a0b1cc988276ed6a11db3c5ec91`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0157 (deneme 2 -> 3)

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
@plan: suya zıpladı ve babasının pantolonu ıslandı | özür diledi ve babasını güneşe götürdü ve kurabiye verdi
@tohum: hello_kitty-0157
@degisim: zarif -> süslü
Parkta, çimenlerin arasında küçük bir su çukuru vardı. Hello Kitty koşarak geldi ve hızla çukura zıpladı. Su her yana sıçradı ve babasının pantolonu ıslandı. Babası elinde süslü bir paket tutuyordu. İçinde evde birlikte yaptıkları kurabiyeler vardı. Hello Kitty babasının pantolonuna baktı ve üzüldü. "Özür dilerim, babacığım," dedi Hello Kitty. Sonra babasının elinden tuttu ve onu güneşli bir yere götürdü. İkisi orada oturdu ve Hello Kitty paketi açtı. İçinden en güzel kurabiyeyi seçti ve babasına uzattı. Güneşte ıslak pantolon yavaş yavaş kurudu. Babası kurabiyeyi yedi ve kızına sarıldı. "Teşekkürler, Hello Kitty, bu kurabiye çok güzel olmuş!" dedi babası.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "babasını güneşe götürdü ve kurabiye verdi"
   - Cümle 0 (plan satırı): «suya zıpladı ve babasının pantolonu ıslandı | özür diledi ve babasını güneşe götürdü ve kurabiye verdi»
   - Açıklama: Plan satırında 've' art arda iki kez gereksiz tekrarlanıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "en güzel kurabiyeyi seçti ve babasına uzattı"
   - Cümle 10: «İçinden en güzel kurabiyeyi seçti ve babasına uzattı.»
   - Açıklama: Islak pantolon sorununa kurabiye vermek yönelmiyor; çözüm özür, güneş ve kurabiye olarak ikiden fazla adıma yayılıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İçinden en güzel kurabiyeyi seçti ve babasına uzattı"
   - Cümle 10: «İçinden en güzel kurabiyeyi seçti ve babasına uzattı.»
   - Açıklama: Islak pantolon sorununa kurabiye vermek yönelmiyor ve çözüm özür, güneşe götürme ve kurabiye olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0157` birebir aynı, `@degisim: zarif -> süslü` (tutuyorsan), ardından `@onarim: bdce41ffe116c915e4cf4df190f0f4c2316a8b84`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0160 (deneme 2 -> 3)

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
Hello Kitty annesiyle parkta, ağacın gölgesinde oturuyordu. Bugün annesinin doğum günüydü ve Hello Kitty ona sürpriz hazırlamak istedi. Ama annesi hemen yanındaydı ve her şeyi görecekti. "Anneciğim, gözlerini kapatıp yüze kadar sayar mısın?" diye sordu Hello Kitty. Annesi gülümsedi ve iki eliyle yüzünü kapattı. Hello Kitty sepetten büyük bir tabak çıkardı. Sepetteki kurabiyeleri tabağa kalp gibi dizdi. "Yüz!" dedi annesi ve ellerini indirdi. Tabakta kurabiyelerden kocaman bir kalp vardı. Annesi kızına sarıldı ve onu gıdıkladı. Hello Kitty neşeyle güldü. "Mutlu yıllar, anneciğim!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sepetteki kurabiyeleri tabağa kalp gibi dizdi"
   - Cümle 7: «Sepetteki kurabiyeleri tabağa kalp gibi dizdi.»
   - Açıklama: Karttaki özellik kurabiye yapmayı sevmek; hikayede kurabiye yapılmıyor, hazır kurabiyeler yalnız diziliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0160` birebir aynı, `@degisim: yardımsever -> mutlu` (tutuyorsan), ardından `@onarim: 17c73cd23caae390c482dd3b884b306ad9b8721f`, sonra gövde.
