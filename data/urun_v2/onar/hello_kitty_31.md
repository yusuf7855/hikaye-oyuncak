# Editör görevi (onarım): Hello Kitty, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0098 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0098
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'çubuk', fiil 'gelmek', sıfat 'hızlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: koşarken masaya çarptı ve kurabiyeler döküldü | özür diledi ve annesiyle yeni kurabiye yaptı
@tohum: hello_kitty-0098
Yağmur cama tıp tıp vuruyordu. Hello Kitty mutfağa çok hızlı koşarak geldi. Masaya çarptı ve annesinin çubuk kurabiyeleri yere döküldü. Hepsi yerde kırılmıştı. Hello Kitty çok üzüldü. "Özür dilerim, anneciğim, yenilerini birlikte yapalım mı?" dedi Hello Kitty. Annesi gülümsedi ve başını salladı. Hello Kitty kaseye un, şeker ve yağ koydu. Hamuru iki eliyle güzelce yoğurdu. Sonra hamurdan ince uzun parçalar yuvarladı. Annesi tepsiyi fırına koydu. Biraz sonra mutfak tatlı bir kokuyla doldu. Annesi sıcak tepsiyi dikkatle çıkardı. "Teşekkürler, anne, bunlar ilkinden de güzel oldu!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kaseye un, şeker ve yağ koydu"
   - Cümle 8: «Hello Kitty kaseye un, şeker ve yağ koydu.»
   - Açıklama: Çözüm malzeme koyma, yoğurma, şekil verme, fırına koyma ve çıkarma gibi ikiden çok adım sürüyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bunlar ilkinden de güzel"
   - Cümle 14: «"Teşekkürler, anne, bunlar ilkinden de güzel oldu!" dedi Hello Kitty.»
   - Açıklama: Çoğul kurabiyeler için tekil 'ilkinden' uyumsuz; 'öncekilerden' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0098` birebir aynı, ardından `@onarim: f7704d14885bf28e3075c4bb1e7935bcc28a706d`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0100 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0100
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'yapıştırıcı', fiil 'tamamlanmak', sıfat 'harika'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: kutlama için sepette hiç tatlı yoktu | kağıt ve yapıştırıcıyla bir elmalı turta yaptı
@tohum: hello_kitty-0100
Bir sabah Hello Kitty ile Mimi ormandaki kamp yerinde oynuyordu. Mimi sarı kurdelesini ilk kez kendisi bağlamıştı. Hello Kitty buna küçük bir kutlama yapmak istedi. Ama sepette hiç tatlı yoktu. İçinde yalnız renkli kağıtlar ve bir yapıştırıcı vardı. Hello Kitty onlarla en sevdiği elmalı turtayı yapmaya başladı. Önce kahverengi bir kağıdı yuvarlak yırttı. Üstüne kırmızı kağıtlardan küçük elmalar yapıştırdı. Böylece turta tamamlandı. Hello Kitty onu Mimi'ye uzattı. "Bu turta senin için, Mimi!" dedi Hello Kitty. Mimi utangaç bir yüzle gülümsedi. "Bu harika bir sürpriz!" dedi Mimi. Hello Kitty bundan sonra küçük bir kutlama için hep kağıttan turta yaptı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ile Mimi ormandaki kamp yerinde"
   - Cümle 1: «Bir sabah Hello Kitty ile Mimi ormandaki kamp yerinde oynuyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; iki çocuk ormanda bir büyük olmadan yalnız.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama sepette hiç tatlı yoktu"
   - Cümle 4: «Ama sepette hiç tatlı yoktu.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede söyleniyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sepette hiç tatlı yoktu"
   - Cümle 4: «Ama sepette hiç tatlı yoktu.»
   - Açıklama: Sepette neden tatlı olmadığı söylenmiyor ve kağıt turta yenemeyeceği için tatlı eksikliği gerçekten giderilmiyor.
   - Açıklama: Sepette neden tatlı olmadığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0100` birebir aynı, ardından `@onarim: e67678e9fd564dd520001485013129521be57fd4`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0101 (deneme 1 -> 2)

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
@plan: kuru yapraklar yüzünden hiç elma göremedi | turtanın kokusunu tanıdı ve elmaları buldu
@tohum: hello_kitty-0101
@degisim: yazmak -> saymak
Hello Kitty ormandaki kamp yerinde elinde bir sepetle yürüyordu. Sepetini turta için elmayla doldurmak istiyordu. Ama hiçbir yerde elma göremedi, çünkü kuru yapraklar yeri örtmüştü. Güneş yerdeki yaprakları ısıttı ve havaya tatlı bir koku yayıldı. Hello Kitty en sevdiği elmalı turtanın kokusunu hemen tanıdı. Kokunun geldiği yere doğru yürüdü. Kamp yerinin yanındaki büyük bir ağacın dibine geldi. Yaprakları elleriyle yavaşça kenara itti. Altında kırmızı elmalar vardı! Hello Kitty onları tek tek saydı ve sepetine koydu. Tam beş tane vardı ve sepet doldu. Hello Kitty sevinçli bir yüzle sepetini kamp yerine taşıdı.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde elinde bir sepetle yürüyordu"
   - Cümle 1: «Hello Kitty ormandaki kamp yerinde elinde bir sepetle yürüyordu.»
   - Açıklama: Güvenli özellik kullanımı satırına göre kimse tek başına uzağa gitmez, ama Hello Kitty ormanda yanında bir büyük olmadan tek başına dolaşıyor.
   - Açıklama: Hello Kitty ormanda tek başına dolaşıp elma topluyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Güneş yerdeki yaprakları ısıttı"
   - Cümle 4: «Güneş yerdeki yaprakları ısıttı ve havaya tatlı bir koku yayıldı.»
   - Açıklama: Çözümü getiren koku güneşle sebepsizce ve tesadüfen ortaya çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Güneş yerdeki yaprakları ısıttı ve havaya tatlı bir koku yayıldı"
   - Cümle 4: «Güneş yerdeki yaprakları ısıttı ve havaya tatlı bir koku yayıldı.»
   - Açıklama: Çözümü getiren koku sebepsizce, güneşin tesadüfen yaprakları ısıtmasıyla geliyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elmalı turtanın kokusunu hemen"
   - Cümle 5: «Hello Kitty en sevdiği elmalı turtanın kokusunu hemen tanıdı.»
   - Açıklama: Ortada turta yok; yayılan koku elmanın kokusu, kelime yanlış anlamda kullanılmış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en sevdiği elmalı turtanın kokusunu"
   - Cümle 5: «Hello Kitty en sevdiği elmalı turtanın kokusunu hemen tanıdı.»
   - Açıklama: Ortada turta yok, yapraklardan gelen koku elma kokusudur; kelime yanlış anlamda.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty en sevdiği elmalı turtanın kokusunu hemen tanıdı"
   - Cümle 5: «Hello Kitty en sevdiği elmalı turtanın kokusunu hemen tanıdı.»
   - Açıklama: Karttaki özellik elmalı turtayı sevmek; yapraklar altındaki çiğ elmaların turta kokusu gibi tanınması özelliği karttaki gibi kullanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0101` birebir aynı, `@degisim: yazmak -> saymak` (tutuyorsan), ardından `@onarim: 16bef4c5c1ea33cbcff83dcf6a84c67fbae42f2a`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0102 (deneme 1 -> 2)

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
@plan: annesi hep baktığı için sürpriz gizli kalmıyordu | annesine elma verip gözlerini kapattırdı ve taç yaptı
@tohum: hello_kitty-0102
Bir sabah Hello Kitty ile annesi parkta piknik yapıyordu. Hello Kitty annesine sürpriz bir çiçek tacı yapmak istedi. Ama annesi hep ona bakıyordu ve sürpriz gizli kalmıyordu. Hello Kitty akıllı bir oyun düşündü. Arkadaşlarına hep yaptığı gibi en güzel elmayı annesine uzattı. "Anne, gözlerini kapat ve bu elmayı ye," dedi Hello Kitty. Annesi gözlerini kapattı ve elmayı yavaş yavaş çiğnedi. Hello Kitty ağacın altına düşmüş beyaz çiçekleri topladı. Saplarını birbirine bağladı ve küçük bir taç yaptı. Tacı annesinin başına koydu. "Şimdi gözlerini açabilirsin," dedi Hello Kitty. Annesi tacı görünce kızına sarıldı. Hello Kitty çok mutlu oldu, çünkü sürprizi başarmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hello Kitty akıllı bir oyun düşündü"
   - Cümle 4: «Hello Kitty akıllı bir oyun düşündü.»
   - Açıklama: 'Akıllı bir oyun' mecazlı ve soyut bir anlatım.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Arkadaşlarına hep yaptığı gibi"
   - Cümle 5: «Arkadaşlarına hep yaptığı gibi en güzel elmayı annesine uzattı.»
   - Açıklama: Tohumdaki arkadaş özelliği karttaki gibi kullanılmıyor, yalnız bir etiket olarak ekleniyor.
   - Açıklama: Tohumdaki arkadaş özelliği (yeni arkadaş edinmeyi sever) işe yarar biçimde kullanılmıyor, yalnız anılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arkadaşlarına hep yaptığı gibi"
   - Cümle 5: «Arkadaşlarına hep yaptığı gibi en güzel elmayı annesine uzattı.»
   - Açıklama: Arkadaşlarla ilgili bu ayrıntı olaya bağlanmıyor ve işlevsiz kalıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çünkü sürprizi başarmıştı"
   - Cümle 13: «Hello Kitty çok mutlu oldu, çünkü sürprizi başarmıştı.»
   - Açıklama: Sürpriz başarılmaz; 'sürprizi yapabilmişti' olmalı.
   - Açıklama: 'Sürprizi başarmak' yanlış bir eşdizimdir; 'sürprizi yapabilmişti' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0102` birebir aynı, ardından `@onarim: 161b390752e2764328ee6df8a7f85d55f02a9dcc`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0103 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0103
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'üniforma', fiil 'inanmak', sıfat 'geniş'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası çok iyi saklandı ve bulunamadı | kurabiyelerle seslendi ve babası çıktı
@tohum: hello_kitty-0103
@degisim: üniforma -> çalı
Hello Kitty parkta babasıyla saklambaç oynuyordu. Park çok genişti ve her yerde ağaçlar vardı. Bu kez arayan Hello Kitty'ydi, ama babası çok iyi saklanmıştı. Hello Kitty ağaçların arkasına baktı ama onu bulamadı. Sepette sabah babasıyla birlikte yaptığı kurabiyeler vardı. Hello Kitty sepeti açtı ve onları havaya kaldırdı. "Kim kurabiye ister?" diye seslendi Hello Kitty. Birden büyük bir çalı sallandı. Babası çalının arkasından gülerek çıktı. "Ben isterim, ben!" dedi babası. Hello Kitty babasının bu kadar yakında olduğuna inanamadı. İkisi çimenlere oturdu ve hepsini paylaştı. Hello Kitty bundan sonra saklambaçta babasını hep kurabiyeyle buldu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurabiyelerle seslendi ve babası"
   - Cümle 0 (plan satırı): «babası çok iyi saklandı ve bulunamadı | kurabiyelerle seslendi ve babası çıktı»
   - Açıklama: Kurabiyelerle seslenilmez; plan satırında araç eki fiile uymuyor.
   - Açıklama: Kurabiyelerle seslenilmez; 'kurabiyeleri gösterip seslendi' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepette sabah babasıyla birlikte yaptığı kurabiyeler vardı"
   - Cümle 5: «Sepette sabah babasıyla birlikte yaptığı kurabiyeler vardı.»
   - Açıklama: Kurabiye sepeti daha önce kurulmadan tam çözüm gerektiğinde beliriyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Sepet ve kurabiyeler önceden kurulmadan tam çözüm gerektiğinde beliriyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "oturdu ve hepsini paylaştı"
   - Cümle 12: «İkisi çimenlere oturdu ve hepsini paylaştı.»
   - Açıklama: 'hepsini' zamirinin kurabiyeleri gösterdiği, kurabiyeler çok önce geçtiği için belli değil.
   - Açıklama: 'hepsini' zamirinin kurabiyeleri gösterdiği uzak bağlamdan belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0103` birebir aynı, `@degisim: üniforma -> çalı` (tutuyorsan), ardından `@onarim: 4a26b3e66038906102cbed75b70d54c9c8feb81a`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0104
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'tutkal', fiil 'toplanmak', sıfat 'zeki'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası turtanın hangi kutuda olduğunu unuttu | kutuları tek tek kokladı ve turtayı buldu
@tohum: hello_kitty-0104
@degisim: toplanmak -> koklamak
Hello Kitty babasıyla parkta bir kutu oyunu oynuyordu. Babası turtayı üç kutudan birine koydu ve tutkalla yıldız yapıştırdı. Ama yıldız düştü ve babası doğru kutuyu unuttu. "Eyvah, hangi kutu?" dedi babası ve başını kaşıdı. Zeki Hello Kitty kutuları tek tek kokladı. İlk kutu peynir, ikinci kutu ekmek kokuyordu. Üçüncü kutu en sevdiği elmalı turta gibi kokuyordu! Hello Kitty kapağı açtı. "Buldum, baba, turta burada!" dedi Hello Kitty. Babası güldü ve ellerini çırptı. Hello Kitty çok sevindi, çünkü onu kokusundan bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama yıldız düştü ve babası doğru kutuyu unuttu"
   - Cümle 3: «Ama yıldız düştü ve babası doğru kutuyu unuttu.»
   - Açıklama: Tutkalla yapıştırılan yıldızın hemen düşmesi ve babanın az önce koyduğu kutuyu unutması akla yatkın bir sebep değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Zeki Hello Kitty kutuları"
   - Cümle 5: «Zeki Hello Kitty kutuları tek tek kokladı.»
   - Açıklama: Tohumdaki özellik turta; zekilik karttaki özelliklere eklenen ikinci bir özellik.
   - Açıklama: Tohumdaki özellik turta; zekilik karta ikinci bir özellik olarak ekleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en sevdiği elmalı turta gibi kokuyordu"
   - Cümle 7: «Üçüncü kutu en sevdiği elmalı turta gibi kokuyordu!»
   - Açıklama: Kutuda gerçekten turta var; 'gibi' yanlış anlamda kullanılmış.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çünkü onu kokusundan bulmuştu"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü onu kokusundan bulmuştu.»
   - Açıklama: 'onu' zamirinin turtayı gösterdiği belli değil; en yakın ad babası.
   - Açıklama: 'Onu' zamirinin turtayı mı babayı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0104` birebir aynı, `@degisim: toplanmak -> koklamak` (tutuyorsan), ardından `@onarim: dd92d773fe25e47c2f042581473b0f9077844a3a`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0105 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0105
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'erik', fiil 'örmek', sıfat 'sert'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: turtanın yanından tık tık diye bir ses geldi | kutuya baktı ve düşen erikleri buldu
@tohum: hello_kitty-0105
@degisim: örmek -> oturmak
Parkta tık tık diye garip bir ses geliyordu. Hello Kitty annesiyle bir ağacın gölgesinde oturuyordu. Hello Kitty bu sesin nereden geldiğini çok merak etti. Ses, en sevdiği elmalı turtanın yanından geliyordu. Hello Kitty hemen turtanın kutusuna baktı. Kapağın üstünde küçük yeşil bir erik vardı. Tam o sırada yukarıdan bir erik daha düştü. Kapağa çarptı ve tık diye ses çıkardı. "Anne, ses erik ağacından geliyor!" dedi Hello Kitty. Annesi düşen meyveyi eline aldı ve sıktı. "Bunlar çok sert, rüzgar onları düşürüyor," dedi annesi. Hello Kitty kutuyu başka bir ağacın gölgesine taşıdı. Sonra Hello Kitty ile annesi turtayı mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kutuya baktı ve düşen erikleri buldu"
   - Cümle 0 (plan satırı): «turtanın yanından tık tık diye bir ses geldi | kutuya baktı ve düşen erikleri buldu»
   - Açıklama: Plan çözümü yalnız erikleri bulmak olarak veriyor; gövdede kutunun başka ağaca taşınması atlanmış.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Hello Kitty kutuyu başka bir ağacın gölgesine taşıdı"
   - Cümle 12: «Hello Kitty kutuyu başka bir ağacın gölgesine taşıdı.»
   - Açıklama: Sesin gizemi çözüldükten sonra turtaya erik düşmesi ikinci bir sorun olarak ayrıca çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0105` birebir aynı, `@degisim: örmek -> oturmak` (tutuyorsan), ardından `@onarim: 026bbaa709c3420503581ddc8e25623b6506b859`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0106 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: masanın altından küçük bir ses geldi | baktı ve kardeşiyle dökülen fotoğrafları topladı
@tohum: hello_kitty-0106
Hello Kitty odasında resim yapıyordu. Birden masanın altından küçük bir ses geldi. Hello Kitty merakla eğildi ve masanın altına baktı. Orada Mimi oturuyordu ve elinde boş bir kutu vardı. Yere bir sürü fotoğraf dağılmıştı. "Kutu elimden düştü," dedi Mimi utangaç bir sesle. Hello Kitty hemen onun yanına oturdu. "Üzülme, Mimi, hepsini birlikte toplayalım," dedi Hello Kitty. İkisi fotoğrafları tek tek kutuya koydu. "Sen benim en iyi arkadaşımsın," dedi Mimi. Bir fotoğrafta kırmızı ve sarı kurdeleli iki kardeş gülüyordu. Sonra Hello Kitty ile Mimi o fotoğrafa bakıp mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kardeşiyle dökülen fotoğrafları topladı"
   - Cümle 0 (plan satırı): «masanın altından küçük bir ses geldi | baktı ve kardeşiyle dökülen fotoğrafları topladı»
   - Açıklama: Plan cümlesinde 'kardeşiyle' sıfat fiile bağlanıyor ve fotoğraflar kardeşiyle dökülmüş gibi okunuyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "masanın altından küçük bir ses geldi"
   - Cümle 2: «Birden masanın altından küçük bir ses geldi.»
   - Açıklama: Plandaki sorun bir ses; asıl sorun dökülen fotoğraflar.
   - Açıklama: Plandaki sorun bir ses; asıl sorun fotoğrafların yere dökülmesi.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Hello Kitty merakla eğildi ve masanın altına baktı.»
   - Açıklama: Fotoğrafların döküldüğü sorun ilk üç cümlede söylenmiyor, ancak beşinci cümlede ortaya çıkıyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yere bir sürü fotoğraf dağılmıştı"
   - Cümle 5: «Yere bir sürü fotoğraf dağılmıştı.»
   - Açıklama: Asıl sorun ancak beşinci cümlede ortaya çıkıyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kutu elimden düştü"
   - Cümle 6: «"Kutu elimden düştü," dedi Mimi utangaç bir sesle.»
   - Açıklama: Dökülen fotoğrafların toplanıp bitmesi önemsiz bir dağıttı-topladı sorunu.
   - Açıklama: Dökülen fotoğrafları toplamak önemsiz bir olay; toplandı, bitti.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0106` birebir aynı, ardından `@onarim: 9a4a9313546bbc2fbead288de7384d106e78d23b`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0107 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0107
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'kilit', fiil 'boyamak', sıfat 'temiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası anahtarı unuttu ve yemek kutusu açılmadı | en sevdiği turtayı ikiye bölüp babasıyla paylaştı
@tohum: hello_kitty-0107
Ağaçlarda kuşlar ötüyordu. Hello Kitty babasıyla parkta resim boyuyordu. Acıkınca babası yemek kutusunu aldı ama kilidin anahtarını evde unutmuştu. Babası üzgün üzgün kutuya baktı. Hello Kitty'nin çantasında en sevdiği elmalı turta vardı. Önce ikisi boyalı ellerini temiz bir bezle sildi. Sonra Hello Kitty turtayı ikiye böldü. Büyük parçayı babasına uzattı. "Buyur, babacığım, turta ikimize de yeter," dedi Hello Kitty. Babası bir ısırık aldı ve gülümsedi. "Çok teşekkürler, kızım, bu çok güzel!" dedi babası. "Paylaşınca turta daha da tatlı oldu, baba!" dedi Hello Kitty.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kilidin anahtarını evde unutmuştu"
   - Cümle 3: «Acıkınca babası yemek kutusunu aldı ama kilidin anahtarını evde unutmuştu.»
   - Açıklama: Anahtarla kilitlenen bir yemek kutusu akla yatkın bir sebep değil.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra Hello Kitty turtayı ikiye böldü"
   - Cümle 7: «Sonra Hello Kitty turtayı ikiye böldü.»
   - Açıklama: Sorunun sebebi unutulan anahtar ve kilitli kutu, ama çözüm kutuya hiç yönelmiyor ve kutu kilitli kalıyor.
   - Açıklama: Çözüm kutunun açılmaması sebebine yönelmiyor, sorunu atlayıp başka yiyecek paylaşıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Paylaşınca turta daha da tatlı oldu"
   - Cümle 12: «"Paylaşınca turta daha da tatlı oldu, baba!" dedi Hello Kitty.»
   - Açıklama: Paylaşınca turtanın tadının değişmesi mecaz bir anlatım.
   - Açıklama: Paylaşmak turtayı gerçekten tatlandırmaz; mecazlı anlatım küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0107` birebir aynı, ardından `@onarim: 085a36ff78ea2a375acde874826ee802912e1f4c`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0108
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kızartma', fiil 'eğmek', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: çamur kurabiyeler kalıp olmadığı için yamuk oluyordu | ince bir dalı eğdi ve yuvarlak bir kalıp yaptı
@tohum: hello_kitty-0108
@degisim: kızartma -> kalıp
Ormandaki kamp yerinde yumuşak bir çamur vardı. Hello Kitty orada mutfak oyunu oynuyordu ve çamurdan oyun kurabiyeleri yapıyordu. Ama yuvarlak bir kalıbı yoktu ve hepsi yamuk oluyordu. Hello Kitty evde kurabiye yaparken kullandığı kalıbı hatırladı. Yerden ince ve yumuşak bir dal aldı. Dalı yavaşça eğdi ve bir halka yaptı. Uçlarını uzun bir otla sıkıca bağladı. Böylece yeni bir kalıbı oldu. Onu çamura bastırdı ve yuvarlak bir kurabiye çıktı. Sonra aynı biçimde birkaç kurabiye daha yaptı. Hepsini büyük bir yaprağın üstüne güzelce dizdi. Hello Kitty mutfak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çamur kurabiyeler kalıp olmadığı"
   - Cümle 0 (plan satırı): «çamur kurabiyeler kalıp olmadığı için yamuk oluyordu | ince bir dalı eğdi ve yuvarlak bir kalıp yaptı»
   - Açıklama: Tamlama eki eksik; 'çamur kurabiyeleri' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty orada mutfak oyunu oynuyordu"
   - Cümle 2: «Hello Kitty orada mutfak oyunu oynuyordu ve çamurdan oyun kurabiyeleri yapıyordu.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde Hello Kitty ormandaki kamp yerinde bir büyük olmadan tek başına oynuyor.
   - Açıklama: Hello Kitty ormandaki kamp yerinde yanında hiçbir büyük olmadan tek başına oynuyor; güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmediğini söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0108` birebir aynı, `@degisim: kızartma -> kalıp` (tutuyorsan), ardından `@onarim: f491d309acede5aebe18584afc4f01a0908d2af4`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0109 (deneme 1 -> 2)

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
@plan: kardeşinin kutusunun kilidi sıkıştı ve açılmadı | kurabiyelerini ikiye ayırıp yarısını kardeşine verdi
@tohum: hello_kitty-0109
Bir sabah Hello Kitty ile Mimi ormanda piknik yapıyordu. İkisi de çok acıkmıştı. Ama Mimi'nin kilitli waffle kutusu açılmadı, çünkü kilidi sıkışmıştı. Mimi kutuyu iki eliyle çekti ama olmadı. Sonra üzüldü ve başını eğdi. Hello Kitty kendi sepetini açtı. İçinde evde yaptığı kurabiyeler vardı. Hello Kitty onları ikiye ayırdı ve yarısını Mimi'ye verdi. Mimi ilk ısırıkta mutlu mutlu miyavladı. İkisi yan yana oturup kurabiyeleri birlikte yedi. Hello Kitty çok sevindi, çünkü kardeşi artık aç değildi.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ile Mimi ormanda piknik"
   - Cümle 1: «Bir sabah Hello Kitty ile Mimi ormanda piknik yapıyordu.»
   - Açıklama: Güvenli kullanım satırına göre kimse büyüksüz uzağa gitmez; iki çocuk ormanda yalnız.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kilitli waffle kutusu"
   - Cümle 3: «Ama Mimi'nin kilitli waffle kutusu açılmadı, çünkü kilidi sıkışmıştı.»
   - Açıklama: 'Waffle' yabancı bir kelime ve 3 yaşındaki çocuk bilmeyebilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi'nin kilitli waffle kutusu"
   - Cümle 3: «Ama Mimi'nin kilitli waffle kutusu açılmadı, çünkü kilidi sıkışmıştı.»
   - Açıklama: 'waffle' yabancı ve 3 yaşındaki çocuğun bilmeyebileceği bir kelime.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty onları ikiye ayırdı ve yarısını Mimi'ye verdi"
   - Cümle 8: «Hello Kitty onları ikiye ayırdı ve yarısını Mimi'ye verdi.»
   - Açıklama: Çözüm sıkışan kilide yönelmiyor, sorunun sebebi olduğu gibi kalıyor.
   - Açıklama: Sorun sıkışan kilit ama çözüm kilide yönelmiyor, kutu hiç açılmıyor.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Mimi ilk ısırıkta mutlu mutlu miyavladı"
   - Cümle 9: «Mimi ilk ısırıkta mutlu mutlu miyavladı.»
   - Açıklama: Kartın dünyasında Mimi konuşan bir karakterdir; hayvan gibi miyavlaması diziyi izleyen çocuğa yanlış bilgi verir.
   - Açıklama: Kartta Mimi konuşan kız kardeş; miyavlayan hayvan gibi anlatılması diziye aykırı.
6. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hello Kitty çok sevindi, çünkü kardeşi artık aç değildi"
   - Cümle 11: «Hello Kitty çok sevindi, çünkü kardeşi artık aç değildi.»
   - Açıklama: Kilitli kutu hiç açılmıyor; kurulan sorun çözülmeden hikaye bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0109` birebir aynı, ardından `@onarim: 21c3877dffe94a8f3888d5eea7d3274a883a579f`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0110 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0110
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'çim', fiil 'dolaşmak', sıfat 'minik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: turta kutusunun kapağı çok sıkıydı | annesinden kapağı açmasını istedi
@tohum: hello_kitty-0110
Ormandaki kamp yerinde Hello Kitty çimlerde dolaşıyordu. Annesi ağacın altında örtünün üstüne bir kutu koymuştu. Kutuda en sevdiği elmalı turta vardı ama kapağı çok sıkıydı. Hello Kitty kapağı iki eliyle çekti ama açamadı. "Anne, bu kapağı açar mısın?" diye sordu Hello Kitty. "Tabii, bana sorman çok güzel," dedi annesi. Annesi kapağı hemen açtı. Hello Kitty tabakları örtünün üstüne dizdi. Annesi iki minik dilimi tabaklara koydu. Hello Kitty ile annesi ağacın gölgesinde turtalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iki minik dilimi tabaklara"
   - Cümle 9: «Annesi iki minik dilimi tabaklara koydu.»
   - Açıklama: Sayılı belirsiz nesne belirtme eki almaz; 'iki minik dilim' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0110` birebir aynı, ardından `@onarim: 422ff27e6fb712d0da2210a3fe7b5f6d2f8809e6`, sonra gövde.
