# Editör görevi (onarım): Hello Kitty, onarım partisi 45

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar45.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar45.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0032 (deneme 4 -> 5)

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
@plan: ikisi de tek davulu aynı anda almak istedi | kardeşiyle sırayla davul çaldı
@tohum: hello_kitty-0032
@degisim: damla -> davul
Bir sabah Hello Kitty ile Mimi parkta elmalı turtayla piknik yapıyordu. Mimi yanında oyuncak bir davul getirmişti. İkisi de davulu aynı anda almak istedi, ama tek davul vardı. Davulu çekiştirdiler ve Mimi üzüldü. Hello Kitty durdu ve düşündü. "Sırayla çalalım mı? Bekleyen de turta yesin," dedi Hello Kitty. "Olur, ama önce sen çal," dedi Mimi. Hello Kitty davula vurdu ve gürültülü bir ses çıktı. Mimi de güldü ve turta yedi. Sonra Hello Kitty davulu Mimi'ye verdi ve "Sıra sende, Mimi," dedi. Mimi çalarken Hello Kitty turtadan bir dilim aldı. Sırayla oynayınca Hello Kitty ile Mimi çok eğlendi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mimi de güldü ve"
   - Cümle 10: «Mimi de güldü ve turta yedi.»
   - Açıklama: Daha önce kimse gülmediği için 'de' bağlacı yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0032` birebir aynı, `@degisim: damla -> davul` (tutuyorsan), ardından `@onarim: df05ca2a25b30c6b23ffb0ff46af9cbd98e4b9d5`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0101 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0101
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'güneş', fiil 'yazmak', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: kuru yapraklar yüzünden hiç elma göremedi | ağacın altındaki yaprakları itti ve elmaları buldu
@tohum: hello_kitty-0101
@degisim: yazmak -> saymak
Hello Kitty güneşli bir sabah ormandaki kamp yerindeydi. En sevdiği elmalı turta için sepetini elmayla doldurmak istiyordu. Ama hiçbir yerde elma göremedi, çünkü yerde bir sürü kuru yaprak vardı. Kamp yerinde büyük bir elma ağacı vardı. Ama dallarında hiç elma kalmamıştı. Hello Kitty elmaların yere düşmüş olabileceğini düşündü. Ağacın altına gitti ve yaprakları elleriyle yavaşça kenara itti. Altında kırmızı elmalar vardı! Hello Kitty onları tek tek saydı ve sepetine koydu. Tam beş tane vardı ve sepet doldu. Artık turta için elmalar hazırdı ve Hello Kitty sevinçli bir yüzle güldü.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty güneşli bir sabah ormandaki kamp yerindeydi"
   - Cümle 1: «Hello Kitty güneşli bir sabah ormandaki kamp yerindeydi.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda yalnız.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Altında kırmızı elmalar vardı!"
   - Cümle 8: «Altında kırmızı elmalar vardı!»
   - Açıklama: 'Altında' sözünün ağacı mı yaprakları mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0101` birebir aynı, `@degisim: yazmak -> saymak` (tutuyorsan), ardından `@onarim: bc938c96a56d0cbc77665ec04d258c62500ba579`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0102 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0102
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'taç', fiil 'çiğnemek', sıfat 'akıllı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: annesi hep baktığı için sürpriz gizli kalmıyordu | annesine elma verdi ve gizlice taç yaptı
@tohum: hello_kitty-0102
Bir sabah Hello Kitty ile annesi parkta piknik yapıyordu. Hello Kitty annesine sürpriz bir çiçek tacı yapmak istedi. Ama annesi hep ona bakıyordu ve sürpriz gizli kalmıyordu. Hello Kitty arkadaşlarıyla oynadığı bir oyunu hatırladı. "Anne, gözlerini kapat ve bu elmayı ye," dedi Hello Kitty. Annesi gözlerini kapattı ve elmayı çiğnedi. Hello Kitty yerdeki beyaz çiçekleri topladı. Çiçekleri birbirine bağladı ve bir taç yaptı. Tacı annesine taktı. "Şimdi gözlerini açabilirsin," dedi Hello Kitty. Annesi tacı görünce kızına sarıldı. "Sen çok akıllı bir kızsın," dedi annesi. Hello Kitty çok mutlu oldu, çünkü sürprizini gizli tutmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "arkadaşlarıyla oynadığı bir oyunu"
   - Cümle 4: «Hello Kitty arkadaşlarıyla oynadığı bir oyunu hatırladı.»
   - Açıklama: Tohumdaki 'yeni arkadaşlar edinmeyi sever' özelliği kullanılmıyor; arkadaşlar yalnız geçerken anılıyor ve sorunu çözen şey özellik değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0102` birebir aynı, ardından `@onarim: d3c412856d31b6eaaee7ba7c959051ada861ff76`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0106 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0106
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'fotoğraf', fiil 'toplamak', sıfat 'boş'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: rüzgar bir fotoğrafı uçurdu ve duvarda yer boş kaldı | sesi dinledi ve yatağın altında fotoğrafı buldu
@tohum: hello_kitty-0106
Hello Kitty ile Mimi odada fotoğrafları toplayıp duvara asıyordu. Açık pencereden rüzgar esti ve bir fotoğraf uçup kayboldu. Duvarda bir yer boş kaldı. Mimi çok üzüldü, çünkü o en sevdiği fotoğraftı. Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı. Odada durdu ve dikkatle dinledi. Yatağın yanından hışır hışır bir ses geliyordu. Hello Kitty yatağın altına eğilip baktı. Kayıp fotoğraf oradaydı ve rüzgar onu sallıyordu. "Buldum, Mimi, fotoğrafın burada!" dedi Hello Kitty. "Teşekkürler, Hello Kitty," dedi Mimi sevinçle. Hello Kitty fotoğrafı duvarda boş kalan yere astı. Sonra ikisi fotoğraflara bakıp mutlu mutlu güldü.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "arkadaşlarına da kardeşine de"
   - Cümle 5: «Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı.»
   - Açıklama: 'Kardeşine' ile kimin kastedildiği belli değil; Mimi ile aynı kişi mi olduğu anlaşılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı"
   - Cümle 5: «Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı.»
   - Açıklama: Tohumdaki özellik kartın özellikler alanındaki gibi işe yaramadan bir huy cümlesi olarak sayılıyor; sorun dinleyerek çözülüyor.
   - Açıklama: Özellik yalnız anlatıcı cümlesiyle sayılıyor, çözümde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı"
   - Cümle 5: «Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı.»
   - Açıklama: Bu cümle olaydan çıkmıyor ve fotoğrafı bulmakla hiçbir işlevi yok.
   - Açıklama: Bu cümle olay akışına bağlanmayan, işlevsiz bir özellik ayrıntısıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0106` birebir aynı, ardından `@onarim: 551ee04fd24e997b5f309470ca59c10531480891`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0109 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0109
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'waffle', fiil 'miyavlamak', sıfat 'kilitli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kardeşi kek kutusunu evde unuttu | kurabiyelerini ikiye ayırdı ve yarısını kardeşine verdi
@tohum: hello_kitty-0109
@degisim: waffle -> kek
Bir sabah Hello Kitty ile Mimi ormanda piknik yapıyordu. İkisi de çok acıkmıştı. Ama Mimi kek kutusunu evde unutmuştu. Mimi boş sepetine baktı ve üzgün üzgün başını eğdi. Hello Kitty evde yaptığı kurabiyeleri küçük bir kutuda getirmişti. Hello Kitty kilitli kutusunu açtı ve kurabiyeleri ikiye ayırdı. Yarısını hemen Mimi'ye verdi. Mimi kurabiyeyi ısırdı ve mutlu bir sesle miyavladı. İkisi yan yana oturup kurabiyeleri birlikte yedi. Hello Kitty çok sevindi, çünkü kardeşi artık aç değildi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hello Kitty kilitli kutusunu açtı"
   - Cümle 6: «Hello Kitty kilitli kutusunu açtı ve kurabiyeleri ikiye ayırdı.»
   - Açıklama: Kutu kilitli denip anahtarsız açılıyor; 'kilitli' kelimesi yanlış anlamda.
   - Açıklama: Kurabiye kutusunun 'kilitli' olması yersiz ve kelime bağlama uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty kilitli kutusunu açtı"
   - Cümle 6: «Hello Kitty kilitli kutusunu açtı ve kurabiyeleri ikiye ayırdı.»
   - Açıklama: Kutunun kilitli olması sebepsiz beliriyor ve hiçbir işe yaramıyor.
   - Açıklama: Kutunun kilitli olması sebepsiz bir ayrıntı; anahtar ya da işlevi hiç kurulmuyor.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "mutlu bir sesle miyavladı"
   - Cümle 8: «Mimi kurabiyeyi ısırdı ve mutlu bir sesle miyavladı.»
   - Açıklama: Kartın yanlar bölümünde Mimi konuşan bir karakterdir; dizideki gibi konuşmak yerine kedi gibi miyavlaması dünyasına yanlış bilgi katıyor.
   - Açıklama: Kartta Mimi konuşan bir karakterdir; dizide miyavlamaz, bu yanlış bilgi verir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0109` birebir aynı, `@degisim: waffle -> kek` (tutuyorsan), ardından `@onarim: fde162d47dc02a7e734c2ba38328d59151bdfcb6`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0113 (deneme 4 -> 5)

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
@plan: kuru otlar hemen kırıldı | ağaç gölgesinde yumuşak yeşil otlarla bileklik ördü
@tohum: hello_kitty-0113
Bir sabah Hello Kitty ormandaki kamp yerindeydi. Yeni arkadaşlara vermek için ilk kez otlardan bileklik yapmayı denedi. Ama yerdeki otlar kuru ve toz doluydu, hemen kırıldı. Hello Kitty kırık otlara baktı ve biraz düşündü. Sonra kamp yerindeki bir ağacın gölgesine geçti. Orada yumuşak ve yeşil otlar vardı. Hello Kitty birkaç yeşil otu nazikçe kopardı. Otları yavaş yavaş birbirine ördü. Yeşil otlar hiç kırılmadı. Sonunda küçük ve güzel bir bileklik oldu. Hello Kitty çok sevindi, çünkü artık yeni arkadaşlara verecek bir hediyesi vardı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerindeydi"
   - Cümle 1: «Bir sabah Hello Kitty ormandaki kamp yerindeydi.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormanda büyüksüz tek başına.
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda bir büyük olmadan yalnız.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Yeni arkadaşlara vermek için"
   - Cümle 2: «Yeni arkadaşlara vermek için ilk kez otlardan bileklik yapmayı denedi.»
   - Açıklama: İyelik eki eksik; 'yeni arkadaşlarına' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "otlar kuru ve toz doluydu"
   - Cümle 3: «Ama yerdeki otlar kuru ve toz doluydu, hemen kırıldı.»
   - Açıklama: Otlar için 'toz dolu' uygun değil; 'tozlu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0113` birebir aynı, ardından `@onarim: 342ea75006f7e92e007978343f00796ed09c28c6`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0116 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar kutuyu devirdi ve kurabiyeler yere döküldü | elindeki son kurabiyeyi ikiye kırıp annesiyle paylaştı
@tohum: hello_kitty-0116
@degisim: muffin -> kek
Parkta ağaçların gölgesinde Hello Kitty ile annesi piknik yapıyordu. Evde birlikte yaptıkları kurabiyeler ve kekler bir kutudaydı. Hello Kitty kutudan bir kurabiye alırken rüzgar kutuyu devirdi. Kutu boşaldı ve kurabiyelerle kekler yere döküldü. Temkinli annesi hepsini hemen topladı. "Bunları yiyemeyiz," dedi annesi. Hello Kitty'nin aldığı kurabiye ise temiz kalmıştı. Hello Kitty o kurabiyeyi yavaşça ikiye kırdı. "Al, anneciğim, yarısı senin," dedi Hello Kitty. "Teşekkürler, tatlım," dedi annesi ve kurabiyeyi yedi. Hello Kitty çok mutlu oldu, çünkü son kurabiyeyi annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Hello Kitty kutudan bir kurabiye alırken rüzgar kutuyu devirdi"
   - Cümle 3: «Hello Kitty kutudan bir kurabiye alırken rüzgar kutuyu devirdi.»
   - Açıklama: Gölgede sakin bir piknikte rüzgarın kurabiye ve kek dolu kutuyu devirmesi hazırlanmamış ve zayıf bir sebep.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty o kurabiyeyi yavaşça ikiye kırdı"
   - Cümle 8: «Hello Kitty o kurabiyeyi yavaşça ikiye kırdı.»
   - Açıklama: Çözüm rüzgarla dökülen kurabiyeler sorununa yönelmiyor, yalnız kalan kurabiyeyi paylaşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0116` birebir aynı, `@degisim: muffin -> kek` (tutuyorsan), ardından `@onarim: 3d5b3f31480bd81ce867819186f55f179b2ddb75`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0117 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0117
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'su', fiil 'tatmak', sıfat 'konuşkan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: annesi çok susamıştı ama suyu bitmişti | kendi dolu şişesini annesine verdi
@tohum: hello_kitty-0117
@degisim: konuşkan -> dolu
Ormandaki kamp yerinde sıcak bir gündü. Hello Kitty ile annesi küçük bir yürüyüşten yeni dönmüştü. Annesi çok susamıştı, ama şişesi bomboştu. "Suyum bitti, kızım," dedi annesi. Hello Kitty'nin şişesi ise doluydu. Hello Kitty arkadaşlarına da annesine de hep iyi davranırdı. Şişesini hemen ona uzattı. "Al, anneciğim, bu su senin," dedi Hello Kitty. Annesi serin suyu içti ve gülümsedi. "Çok güzel, teşekkür ederim," dedi annesi. Hello Kitty de sudan biraz tattı. Sonra ikisi ağaçların gölgesinde oturup dinlendi. Hello Kitty çok sevindi, çünkü annesine yardım edebilmişti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty arkadaşlarına da annesine de hep iyi davranırdı"
   - Cümle 6: «Hello Kitty arkadaşlarına da annesine de hep iyi davranırdı.»
   - Açıklama: Tohumdaki özellik kartın özellikler alanındaki gibi olaya işlenmeden bir huy cümlesi olarak sayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0117` birebir aynı, `@degisim: konuşkan -> dolu` (tutuyorsan), ardından `@onarim: b22e998a88a48fae662e9b68570f2f9f28d897c2`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0118 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0118
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'yüzük', fiil 'inmek', sıfat 'heyecanlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: ikizinin büyük yüzüğü küçük bir yokuştan yuvarlandı | ikizinin elini tuttu, yokuştan indi ve yüzüğü buldu
@tohum: hello_kitty-0118
Ormandaki kamp yerinde Hello Kitty ile Mimi yaprak topluyordu. Mimi'nin parmağında büyük bir yüzük vardı. Birden yüzük parmağından kaydı ve küçük bir yokuştan aşağı yuvarlandı. Mimi çok üzüldü ama bir şey demedi. Hello Kitty arkadaşlarına da kardeşine de hep iyi davranırdı. Hemen Mimi'ye elini uzattı. "Gel, Mimi, birlikte arayalım," dedi Hello Kitty. İkisi el ele yokuştan yavaşça aşağı indi. Aşağıda bir sürü sarı yaprak vardı. Hello Kitty yaprakları tek tek kaldırdı. Sonunda bir yaprağın altında parlayan yüzüğü buldu. Mimi onu sevinçle aldı ve heyecanlı bir sesle teşekkür etti. Hello Kitty kardeşine yardım edince ikisi de çok mutlu oldu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi el ele yokuştan yavaşça aşağı indi"
   - Cümle 8: «İkisi el ele yokuştan yavaşça aşağı indi.»
   - Açıklama: İki küçük kardeş bir büyük olmadan ormanda yokuştan aşağı iniyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hello Kitty kardeşine yardım"
   - Cümle 13: «Hello Kitty kardeşine yardım edince ikisi de çok mutlu oldu.»
   - Açıklama: Mimi'nin Hello Kitty'nin kardeşi olduğu hiç söylenmediği için 'kardeşine' kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0118` birebir aynı, ardından `@onarim: a5232a8e72d711010925d77d45966a0ecabb9f8c`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0119 (deneme 4 -> 5)

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
Bir sabah Hello Kitty parkta yeni bir şey denemek istedi. İlk kez tebeşirle parkın yoluna resim çizecekti. Ama tebeşirler düşmesin diye kadife kesenin ipi sıkı bir düğümle bağlıydı. Hello Kitty ipi hızlı hızlı çekti. Düğüm daha da sıkıştı. Kese yeni arkadaşlarının hediyesiydi, bu yüzden Hello Kitty ipi koparmadı. Durdu ve düğüme dikkatle baktı. Sonra ipin ucunu buldu ve düğümü yavaşça açtı. Kese renkli tebeşirlerle doluydu. Hello Kitty yere büyük bir resim çizdi. Çizgiler çok güzel oldu. Hello Kitty bundan sonra düğümleri acele etmeden açtı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kadife kesenin ipi"
   - Cümle 3: «Ama tebeşirler düşmesin diye kadife kesenin ipi sıkı bir düğümle bağlıydı.»
   - Açıklama: 'Kadife' ve 'kese' 3 yaşındaki bir çocuğun bilmeyebileceği kelimeler.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kese yeni arkadaşlarının hediyesiydi"
   - Cümle 6: «Kese yeni arkadaşlarının hediyesiydi, bu yüzden Hello Kitty ipi koparmadı.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız keseyi hediye eden kişiler olarak anılıyor, karttaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0119` birebir aynı, ardından `@onarim: 9e6630964bd8e20fa58ad3614956957ca10ccbe5`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0121 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0121
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'menekşe', fiil 'giymek', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: koşarken kurabiye paketi cebinden düştü | kurabiyelerin kokusunu tanıdı ve paketi buldu
@tohum: hello_kitty-0121
@degisim: esnek -> mor
Hello Kitty yeleğini giymiş, parkta çimenlerin üstünde koşuyordu. Cebinde evde yapılan kurabiyelerden bir paket vardı. Ama koşarken paket cebinden düşmüştü. Hello Kitty paketin nereye düştüğünü çok merak etti. Çimenlerde geri yürüdü ve her yere baktı. Paketi göremedi, ama paketin üstü açıktı ve kurabiyeler güzel kokuyordu. Hello Kitty kurabiye yapmayı çok severdi ve bu kokuyu hemen tanıdı. Koku mor menekşelerin yanından geliyordu. Hello Kitty eğildi ve çiçeklere dikkatle baktı. Paket orada, yaprakların altında duruyordu. Hiçbir kurabiye kırılmamıştı. Hello Kitty bundan sonra cebinde kurabiye varken yavaş yürüdü.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Paketi göremedi, ama paketin üstü açıktı"
   - Cümle 6: «Paketi göremedi, ama paketin üstü açıktı ve kurabiyeler güzel kokuyordu.»
   - Açıklama: Hello Kitty paketi göremediği halde üstünün açık olduğunu biliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0121` birebir aynı, `@degisim: esnek -> mor` (tutuyorsan), ardından `@onarim: f74357a3676e7bd9a52e42ef0e3d108e2386660c`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0122 (deneme 4 -> 5)

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
Hello Kitty ile Mimi ormandaki kamp yerinde top oynuyordu. Topu şirin bir sepetin içine atıyorlardı. Ama bir tek top vardı ve ikisi de hep atmak istiyordu. Mimi utangaçtı, bir şey demedi ve oyundan ayrıldı. Bir ağacın altına oturdu ve topa baktı. Hello Kitty en iyi arkadaşı Mimi'yi üzmek istemedi. Mimi'nin yanına gitti ve topu ona verdi. "İlk sıra sende, Mimi, sonra ben atarım," dedi Hello Kitty. Mimi topu attı ve top sepete girdi. "Sıra sende, Hello Kitty!" dedi Mimi sevinçle. Hello Kitty de attı ve top sepete düştü. İki kardeş sırayla atış yapıp oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kardeşi oyundan ayrıldı"
   - Cümle 0 (plan satırı): «tek bir top vardı ve kardeşi oyundan ayrıldı | ilk sırayı kardeşine verdi ve sırayla oynadılar»
   - Açıklama: Plan kardeşten söz ediyor ama gövdede Mimi en iyi arkadaş olarak tanıtılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en iyi arkadaşı Mimi'yi"
   - Cümle 6: «Hello Kitty en iyi arkadaşı Mimi'yi üzmek istemedi.»
   - Açıklama: Mimi kardeş olarak geçiyor ama burada 'arkadaşı' deniyor; kelime kişiye uymuyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı Mimi'yi"
   - Cümle 6: «Hello Kitty en iyi arkadaşı Mimi'yi üzmek istemedi.»
   - Açıklama: Zaten tanıtılmış Mimi yeniden 'en iyi arkadaşı' diye tanıtılıyor, sonra ise 'iki kardeş' deniyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hello Kitty en iyi arkadaşı Mimi'yi"
   - Cümle 6: «Hello Kitty en iyi arkadaşı Mimi'yi üzmek istemedi.»
   - Açıklama: Mimi önce en iyi arkadaş olarak anılıyor, sonda ise ikisi kardeş deniyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İki kardeş sırayla atış"
   - Cümle 12: «İki kardeş sırayla atış yapıp oyunlarına mutlu mutlu devam etti.»
   - Açıklama: Mimi önce 'en iyi arkadaşı' diye tanıtıldı, sonunda 'iki kardeş' deniyor; kimi gösterdiği ve ilişki tutarsız.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İki kardeş sırayla atış yapıp"
   - Cümle 12: «İki kardeş sırayla atış yapıp oyunlarına mutlu mutlu devam etti.»
   - Açıklama: Arkadaş olarak tanıtılan Mimi ile Hello Kitty son cümlede kardeş oluyor.
   - Açıklama: Mimi önce Hello Kitty'nin en iyi arkadaşı diye tanıtılıyor, sonda ikisine kardeş deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0122` birebir aynı, `@degisim: pankek -> top` (tutuyorsan), ardından `@onarim: dd996cd803758c4ea4a880f72bd1b6defe494ce3`, sonra gövde.
