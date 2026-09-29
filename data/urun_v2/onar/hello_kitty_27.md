# Editör görevi (onarım): Hello Kitty, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0094 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0094
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'yağmur', fiil 'esmek', sıfat 'çekingen'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: koşarken kardeşinin kurabiyesini ıslak toprağa düşürdü | özür diledi ve ona kendi kurabiyesini verdi
@tohum: hello_kitty-0094
@degisim: çekingen -> sessiz
Ormanda serin bir rüzgar esiyordu. Yağmurdan sonra Hello Kitty ile Mimi kamp yerinde piknik yapıyordu. Hello Kitty bakmadan koştu ve Mimi'nin kurabiyesini ıslak toprağa düşürdü. Mimi sessiz kaldı ama çok üzüldü. Hello Kitty bunu gördü ve hemen durdu. "Özür dilerim, Mimi, bakmadan koştum," dedi Hello Kitty. Sonra sepetten evde yaptığı yıldız kurabiyeleri çıkardı. En büyüğünü Mimi'ye verdi. Mimi yavaşça gülümsedi ve kardeşine teşekkür etti. İkisi pikniklerine mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ile Mimi kamp yerinde piknik yapıyordu"
   - Cümle 2: «Yağmurdan sonra Hello Kitty ile Mimi kamp yerinde piknik yapıyordu.»
   - Açıklama: İki küçük kardeş ormandaki kamp yerinde bir büyük olmadan yalnız görünüyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
   - Açıklama: İki küçük kardeş ormanda hiçbir büyük olmadan yalnız görünüyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "evde yaptığı yıldız kurabiyeleri çıkardı"
   - Cümle 7: «Sonra sepetten evde yaptığı yıldız kurabiyeleri çıkardı.»
   - Açıklama: Belirli nesne belirtme eki almamış; 'yıldız kurabiyelerini çıkardı' olmalı.
   - Açıklama: Belirli nesne belirtme eki almalı: 'kurabiyelerini'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0094` birebir aynı, `@degisim: çekingen -> sessiz` (tutuyorsan), ardından `@onarim: 400aaa9ac3356b390785a72bc3ed831a35c23320`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0095 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0095
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mısır', fiil 'duymak', sıfat 'yumuşacık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: çadırın arkasından garip bir ses geldi | kurabiye kırıntılarını izleyip babasını buldu
@tohum: hello_kitty-0095
@degisim: mısır -> kutu
Çadırın arkasından kıtır kıtır bir ses geliyordu. Hello Kitty kamp yerinde bu sesi duydu ve çok merak etti. Ses, kurabiye yerken çıkan sese benziyordu. Hemen kurabiye kutusuna baktı. Kutu açıktı ve yerde küçük kırıntılar vardı. Bu kırıntılar babasıyla evde yaptığı yıldız kurabiyelerdendi. Hello Kitty kırıntıların peşinden çadırın arkasına yürüdü. Orada babası yumuşacık çimenlere oturmuştu. Ağzı kurabiyeyle doluydu. "Baba, bu ses senden mi geliyordu?" diye sordu Hello Kitty. "Evet, kurabiyelerin çok güzel, hepsi kıtır kıtır," dedi babası. Sonra en büyük kurabiyeyi Hello Kitty'ye uzattı. İkisi çadırın arkasında kurabiyeleri paylaştı ve mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çadırın arkasından garip bir ses geldi"
   - Cümle 0 (plan satırı): «çadırın arkasından garip bir ses geldi | kurabiye kırıntılarını izleyip babasını buldu»
   - Açıklama: Sorun yalnız babasının kurabiye yerken çıkardığı zararsız bir ses; çözülecek gerçek bir sorun yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Çadırın arkasından kıtır kıtır bir ses geliyordu"
   - Cümle 1: «Çadırın arkasından kıtır kıtır bir ses geliyordu.»
   - Açıklama: Sorun yalnız merak uyandıran bir ses; çocuğun önemseyeceği gerçek bir sorun ya da tehlike yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0095` birebir aynı, `@degisim: mısır -> kutu` (tutuyorsan), ardından `@onarim: f7c910074eb2d65cbaf2da6cb6016f172053ef8d`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0096 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0096
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kese', fiil 'öğrenmek', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: rüzgar esince kurabiye kulesi yıkıldı | büyük kurabiyeleri alta ve küçük olanları üste dizdi
@tohum: hello_kitty-0096
@degisim: kese -> torba
Ormandaki kamp yerinde Hello Kitty çadırın önünde gizli mutfak oyunu oynuyordu. Yanındaki torbada kurabiyeler vardı ve onlarla bir kütüğün üstünde kule yaptı. Ama rüzgar esti ve kule hemen yıkıldı. Hello Kitty kurabiyelere dikkatle baktı. Onları evde yapmıştı ve büyüklerin daha kalın olduğunu biliyordu. Küçük kurabiyeleri en alta koymuştu. Hello Kitty bu kez en büyük kurabiyeyi en alta koydu. Onun üstüne daha küçük kurabiyeleri sırayla dizdi. En küçük kurabiye en üste çıktı. Rüzgar yine esti ama kule bu kez yıkılmadı. Hello Kitty çok sevindi, çünkü sağlam bir kule yapmayı öğrenmişti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ormandaki kamp yerinde Hello Kitty çadırın önünde"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty çadırın önünde gizli mutfak oyunu oynuyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormandaki kamp yerinde büyüksüz tek başına.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gizli mutfak oyunu oynuyordu"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty çadırın önünde gizli mutfak oyunu oynuyordu.»
   - Açıklama: 'Gizli' kelimesi oyuna anlamca uymuyor; oyunda gizli bir şey yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "gizli mutfak oyunu oynuyordu"
   - Cümle 1: «Ormandaki kamp yerinde Hello Kitty çadırın önünde gizli mutfak oyunu oynuyordu.»
   - Açıklama: Oyunun gizli olması hiçbir işe yaramıyor ve bir daha geçmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0096` birebir aynı, `@degisim: kese -> torba` (tutuyorsan), ardından `@onarim: 287c4c3185ecccef1f284f9b0c3c6249b04e92b7`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0097 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0097
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'biftek', fiil 'düzeltmek', sıfat 'oynak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: çadırdan tık tık diye bir ses geldi | kardeşiyle sesi arayıp oynak direği düzeltti
@tohum: hello_kitty-0097
@degisim: biftek -> direk
Ormandaki kamp yerinde Hello Kitty ile Mimi çadırın önünde oturuyordu. Birden çadırdan tık tık diye bir ses geldi. Hello Kitty sesin nereden geldiğini çok merak etti. Kardeşinin elini tuttu. "Gel, Mimi, birlikte bakalım," dedi Hello Kitty. Mimi başını salladı ve onunla yürüdü. İkisi çadırın arkasına gitti. Orada çadırın direği oynaktı ve rüzgarda bir taşa vuruyordu. Hello Kitty direği toprağa sıkıca bastırdı ve düzeltti. Ses hemen kesildi. Hello Kitty çok sevindi, çünkü sesi en iyi arkadaşı Mimi ile bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en iyi arkadaşı Mimi ile"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü sesi en iyi arkadaşı Mimi ile bulmuştu.»
   - Açıklama: Mimi Hello Kitty'nin kardeşi olarak geçiyor, 'en iyi arkadaşı' denmesi kelimeyi yanlış anlamda kullanıyor.
   - Açıklama: Mimi kardeşi olarak geçiyor; 'en iyi arkadaşı' yanlış kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sesi en iyi arkadaşı Mimi ile bulmuştu"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü sesi en iyi arkadaşı Mimi ile bulmuştu.»
   - Açıklama: Tohum özelliği (yeni arkadaş edinme, herkese iyi davranma) yalnız etiket olarak anılıyor, sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en iyi arkadaşı Mimi ile"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü sesi en iyi arkadaşı Mimi ile bulmuştu.»
   - Açıklama: Tohumdaki 'arkadaş' özelliği çözümde kullanılmıyor, yalnız son cümlede etiket olarak geçiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sesi en iyi arkadaşı Mimi ile bulmuştu"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü sesi en iyi arkadaşı Mimi ile bulmuştu.»
   - Açıklama: Mimi önce kardeşi olarak anılıyor, sonda en iyi arkadaşı deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0097` birebir aynı, `@degisim: biftek -> direk` (tutuyorsan), ardından `@onarim: 13dfad71d81dc3b05246e60c1f00cd04fc2fa0b8`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0099 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0099
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'eldiven', fiil 'çekilmek', sıfat 'yeşil'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: eldiven büyük olduğu için top içinden düşüyordu | eldiveni çıkarıp topu elleriyle yakaladı
@tohum: hello_kitty-0099
Bir sabah Hello Kitty babasıyla parkta top yakalama oyunu oynuyordu. Babası ona büyük, yeşil bir eldiven vermişti. Ama eldiven çok büyüktü ve top her seferinde içinden düşüyordu. "Topu yakalarsan elmalı turtanın son dilimi senin," dedi babası. Sonra birkaç adım geri çekildi. Top yine eldivenden kaydı ve çimenlere yuvarlandı. Hello Kitty biraz düşündü. Sonra eldiveni çıkardı ve ellerini açtı. Babası topu yavaşça attı. Hello Kitty topu iki eliyle sıkıca yakaladı. Babası sevinçle ellerini çırptı ve ona turtayı verdi. Hello Kitty çok sevindi, çünkü sonunda topu yakalamıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "elmalı turtanın son dilimi senin"
   - Cümle 4: «"Topu yakalarsan elmalı turtanın son dilimi senin," dedi babası.»
   - Açıklama: Tohumdaki turta özelliği iki kez ödül olarak anılıyor ama çözümde işe yaramıyor.
   - Açıklama: Turta sevgisi sorunun çözümüne yaramıyor, yalnız ödül olarak ve iki kez anılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elmalı turtanın son dilimi senin"
   - Cümle 4: «"Topu yakalarsan elmalı turtanın son dilimi senin," dedi babası.»
   - Açıklama: Turta parkta sebepsiz beliriyor ve soruna bağlı olmayan bir ödül olarak getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0099` birebir aynı, ardından `@onarim: 32da63018f5e0396160a46216acaf23533561eff`, sonra gövde.
