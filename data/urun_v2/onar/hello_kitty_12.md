# Editör görevi (onarım): Hello Kitty, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0030 (deneme 3 -> 4)

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
Hello Kitty ile annesi ormandaki kamp yerine doğru yürüyordu. Annesinin iki elinde de büyük çantalar vardı. Kolundaki sepet de kayıyordu, çünkü annesi onu tutamıyordu. Sepette, Hello Kitty'nin annesiyle yaptığı değişik şekilli kurabiyeler vardı. Hello Kitty onları severek yapmıştı ve düşmelerini hiç istemedi. "Anne, sepeti ben taşıyabilir miyim?" diye sordu Hello Kitty. "Tabii, ama iki elinle sıkıca tut," dedi annesi. Hello Kitty sepeti annesinin kolundan dikkatle aldı. Onu iki eliyle tuttu ve yavaş yavaş yürüdü. Kurabiyelerin hiçbiri yere düşmedi. "Çok yardımcı oldun, kızım," dedi annesi ve ona sarıldı. Hello Kitty bundan sonra annesinin elleri dolu olunca ona hemen yardım etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "düşmelerini hiç istemedi"
   - Cümle 5: «Hello Kitty onları severek yapmıştı ve düşmelerini hiç istemedi.»
   - Açıklama: Süren durum için 'istemiyordu' olmalı; 'yapmıştı' ile zaman uyumu bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0030` birebir aynı, `@degisim: koni -> sepet` (tutuyorsan), ardından `@onarim: 9076755d1410ffc59433fb127306514c7a249d1f`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0031
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: paylaşmak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'terazi', fiil 'tekrarlamak', sıfat 'kaygan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: iki kişiye yetecek kadar un yoktu | tek hamur yapıp babasıyla paylaştı
@tohum: hello_kitty-0031
@degisim: kaygan -> yuvarlak
Bir sabah Hello Kitty mutfakta kurabiye yapmak istedi. Babası da kendi kurabiyelerini yapmak için una uzandı. Ama torbada çok az un vardı. Babası unu teraziye koydu ve baktı. "Bu un yalnız bir kase hamura yeter," dedi babası. Hello Kitty biraz düşündü. "Baba, tek hamur yapalım ve paylaşalım," dedi Hello Kitty. Babası güldü ve onun sözünü sevinçle tekrarladı. İkisi hamuru birlikte yoğurdu. Hello Kitty küçük yıldızlar kesti, babası da yuvarlaklar yaptı. Sonra babası tepsiyi fırına koydu. Kurabiyeler pişince sıcak tepsiyi yine babası çıkardı. "Teşekkürler, Hello Kitty, paylaşınca ikimiz de kurabiye yaptık!" dedi babası.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onun sözünü sevinçle tekrarladı"
   - Cümle 8: «Babası güldü ve onun sözünü sevinçle tekrarladı.»
   - Açıklama: 'Onun' zamirinin kimi gösterdiği belli değil, çünkü son replik de babaya verilmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0031` birebir aynı, `@degisim: kaygan -> yuvarlak` (tutuyorsan), ardından `@onarim: 6c3405adc38b9adcafbc1436e559593bb539632d`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0033 (deneme 3 -> 4)

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
Hello Kitty pencerenin önünde oturmuş, gökyüzündeki aya bakıyordu. Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu. Ama çizdiği ay yuvarlak olmadı, çünkü eli hep kayıyordu. Hello Kitty resme baktı ve çok üzüldü. Annesi de odadaydı. "Anne, ay yuvarlak olmuyor, bana yardım eder misin?" diye sordu Hello Kitty. Annesi gülümsedi ve ona bir bardak verdi. "Bardağı kağıda koy ve çevresini çiz," dedi annesi. Hello Kitty bardağı kağıda koydu ve kalemle etrafından yavaşça çizdi. Kağıtta kocaman, yuvarlak bir ay vardı. Hello Kitty resmi annesine gösterdi ve ona sıcacık sarıldı. Hello Kitty bundan sonra bir şeyi yapamayınca annesinden yardım istedi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yeni arkadaşlarına bir ay resmi"
   - Cümle 2: «Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız amaç olarak anılıyor, çözüme katkısı yok ve sonda geri dönülmüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu"
   - Cümle 2: «Yeni arkadaşlarına bir ay resmi yapıp vermek istiyordu.»
   - Açıklama: Resmi yeni arkadaşlara verme amacı kuruluyor ama hiç kullanılmıyor; resim yalnız anneye gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0033` birebir aynı, ardından `@onarim: 2f249b11758f54191e2d2479377169d4825cb935`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0034 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | babası
@tohum: hello_kitty-0034
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'eşarp', fiil 'özlemek', sıfat 'buzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | babası
@plan: babası yanındaydı ve her şeyi görüyordu | babasının gözlerini eşarpla kapattı ve kurabiyeleri dizdi
@tohum: hello_kitty-0034
Ormanda ağaçların dalları buzluydu. Hello Kitty kamp yerinde babasına bir sürpriz hazırlamak istedi. Ama babası hemen yanında oturuyordu ve her şeyi görüyordu. "Kurabiyeleri çok özledim," dedi babası. Hello Kitty'nin çantasında kurabiyeler ve pembe bir eşarp vardı. "Baba, bu eşarpla gözlerini bağlayayım mı?" diye sordu Hello Kitty. Babası gülerek başını salladı. Hello Kitty eşarbı babasının gözlerine yavaşça bağladı. Sonra kurabiyeleri çantadan çıkarıp kütüğün üstüne dizdi. En sonunda eşarbı çözdü. Babası kurabiyeleri görünce çok şaşırdı. "Bu çok güzel bir sürpriz, kızım!" dedi babası. "Afiyet olsun, babacığım!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kurabiyeleri çantadan çıkarıp kütüğün üstüne dizdi"
   - Cümle 9: «Sonra kurabiyeleri çantadan çıkarıp kütüğün üstüne dizdi.»
   - Açıklama: Kartın özelliği kurabiye yapmayı sevmek; hikayede kurabiye yapılmıyor, hazır kurabiyeler yalnız diziliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0034` birebir aynı, ardından `@onarim: 586f32cca72dfd8105bbaf61c4a413ebe9cbc700`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0035
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'sebze', fiil 'karışmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: rüzgar tabağı devirdi ve sebzelerden yapılan yüz bozuldu | tabağı ağacın dibine koyup yüzü yeniden yaptı
@tohum: hello_kitty-0035
Parkta, ağaçların gölgesinde Hello Kitty piknik yapıyordu. Kağıt tabağına sebzelerle gülen bir yüz yapmıştı. Ama birden rüzgar esti ve hafif tabak çimenlere devrildi. Sebzeler birbirine karıştı ve yüz bozuldu. Hello Kitty bu yüzü yeni arkadaşları gibi sevmişti. Bu yüzden şimdi biraz mutsuzdu. Önce tabağı ağacın dibine, rüzgarın gelmediği yere koydu. Sonra sebzeleri tek tek topladı. İki havuç dilimi yüzün gözleri oldu. Bir domates dilimi de ağız oldu. İki salatalık parçasını da kulak diye yukarıya dizdi. Rüzgar yine esti ama tabak artık kıpırdamadı. Hello Kitty çok sevindi, çünkü tabaktaki yüz yeniden gülüyordu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yüzü yeni arkadaşları gibi sevmişti"
   - Cümle 5: «Hello Kitty bu yüzü yeni arkadaşları gibi sevmişti.»
   - Açıklama: Sebze yüzünü arkadaş gibi sevmek mecazlı ve anlaşılmaz bir benzetme.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu yüzü yeni arkadaşları gibi sevmişti"
   - Cümle 5: «Hello Kitty bu yüzü yeni arkadaşları gibi sevmişti.»
   - Açıklama: Yüzü arkadaş gibi sevmek soyut bir benzetme ve 'yüz/yüzden' karışıklığı 3 yaşındaki çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşları gibi sevmişti"
   - Cümle 5: «Hello Kitty bu yüzü yeni arkadaşları gibi sevmişti.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız benzetmede geçiyor, sorunun çözümünde işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yüzü yeni arkadaşları gibi sevmişti"
   - Cümle 5: «Hello Kitty bu yüzü yeni arkadaşları gibi sevmişti.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız benzetmede geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0035` birebir aynı, ardından `@onarim: 4f2bba3eb4c57cf4db8324ebd34cad204ba7f883`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0037
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'ip', fiil 'tartmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: ipler arkadaydı ve önlüğü bağlayamadı | önlüğü ters takıp ipleri önde bağladı
@tohum: hello_kitty-0037
Dışarıda soğuk bir rüzgar esiyordu. Hello Kitty mutfakta yemek oyunu oynamak istedi. Ama önlüğünü bağlayamadı, çünkü ipleri arkadaydı. Hello Kitty onları hiç göremiyordu. Biraz düşündü ve önlüğü ters taktı. Böylece ipler öne geldi ve onları güzelce bağladı. Sonra önlüğü belinde yavaşça döndürdü. Düğüm arkaya geçti. Oyunda en sevdiği elmalı turtayı hazırlayacaktı. Terazide üç kırmızı elmayı tarttı. Elmaları sonra büyük bir kaseye koydu. Hello Kitty çok mutluydu, çünkü önlüğünü tek başına bağlamıştı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ipler öne geldi ve onları güzelce bağladı"
   - Cümle 6: «Böylece ipler öne geldi ve onları güzelce bağladı.»
   - Açıklama: Özne 'ipler'den söylenmeden Hello Kitty'ye geçiyor; bağlayanın kim olduğu ve 'onları'nın gösterdiği belirsiz.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra önlüğü belinde yavaşça döndürdü"
   - Cümle 7: «Sonra önlüğü belinde yavaşça döndürdü.»
   - Açıklama: Çözüm ters takma, bağlama ve döndürme olarak üç adım sürüyor.
   - Açıklama: Çözüm ters takma, bağlama ve döndürme ile ikiden fazla adım sürüyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Oyunda en sevdiği elmalı turtayı hazırlayacaktı"
   - Cümle 9: «Oyunda en sevdiği elmalı turtayı hazırlayacaktı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre turta bir büyükle yapılır; Hello Kitty mutfakta tek başına turta hazırlıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Oyunda en sevdiği elmalı turtayı hazırlayacaktı"
   - Cümle 9: «Oyunda en sevdiği elmalı turtayı hazırlayacaktı.»
   - Açıklama: Turta özelliği sorun (önlük) ve çözümle ilgisiz, süs olarak ekleniyor.
   - Açıklama: Tohumdaki turta özelliği sorun çözüldükten sonra eklenmiş, işe yarar biçimde kullanılmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Terazide üç kırmızı elmayı tarttı"
   - Cümle 10: «Terazide üç kırmızı elmayı tarttı.»
   - Açıklama: Terazi ve elmalar önlük sorunuyla ilgisiz, işlevsiz ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0037` birebir aynı, ardından `@onarim: 5b2532b2b5e48caeb356a30ff3c8abc08a53c006`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0038 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0038
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'hediye', fiil 'yürümek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: eski sepetin sapı koptu ve annesi üzüldü | kurdelesini çıkarıp sapı sepete bağladı
@tohum: hello_kitty-0038
Parkta çimenlerin üstünde güneş parlıyordu. Hello Kitty annesiyle ağaçların gölgesine doğru yürüyordu. Annesinin elindeki piknik sepeti çok eskiydi ve sapı birden koptu. Bu sepet, annesinin çok sevdiği bir hediyeydi. Annesi sepete baktı ve üzüldü. Hello Kitty herkese iyi bir arkadaştı ve annesine hemen yardım etmek istedi. Kırmızı kurdelesini çıkardı. Sonra kurdeleyle sapı sepete sıkıca bağladı. Annesi sepeti yavaşça kaldırdı. Sap yerinde kaldı ve sepet düşmedi. Annesi gülümsedi ve kızına sarıldı. Sonra Hello Kitty ile annesi gölgede mutlu mutlu piknik yaptı.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hello Kitty herkese iyi bir arkadaştı"
   - Cümle 6: «Hello Kitty herkese iyi bir arkadaştı ve annesine hemen yardım etmek istedi.»
   - Açıklama: 'Arkadaş' yönelme eki almaz; 'herkesin iyi bir arkadaşıydı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0038` birebir aynı, ardından `@onarim: 19be9158a767b85b58ac767a5acef471e83f6738`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0039
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'meşe', fiil 'katmak', sıfat 'umutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: hafif sepet her atışta yere devriliyordu | kurabiye kutusunu sepetin dibine koydu
@tohum: hello_kitty-0039
@degisim: katmak -> atmak
Hello Kitty ile Mimi, bir kutu kurabiyeyle büyük meşe ağacının altına oturmuştu. İkisi küçük bir topu sepete atma oyunu oynuyordu. Ama sepet çok hafifti ve her atışta yere devriliyordu. Top çimenlere kaçtı ve Mimi güldü. "Sepet yine düştü, Hello Kitty!" dedi Mimi. Hello Kitty biraz düşündü. Sonra ağır kurabiye kutusunu sepetin dibine yerleştirdi. Mimi umutlu bir yüzle topu attı. Top içine düştü ve bu kez sepet hiç kıpırdamadı. "Oldu, Hello Kitty!" dedi Mimi sevinçle. İkisi sırayla atmaya devam etti. Hello Kitty bundan sonra hafif bir sepete hep ağır bir şey koydu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ağır kurabiye kutusunu sepetin dibine"
   - Cümle 7: «Sonra ağır kurabiye kutusunu sepetin dibine yerleştirdi.»
   - Açıklama: Tohum özelliği kurabiye yapmayı sevmek; kurabiye kutusu yalnız ağırlık eşyası olarak kullanılıyor, özellik karttaki gibi kullanılmıyor.
   - Açıklama: Kartın özelliği kurabiye yapmayı sevmek; burada kurabiye kutusu yalnız ağırlık olarak kullanılıyor.
   - Açıklama: Tohumdaki kurabiye yapma özelliği kullanılmıyor, kurabiye kutusu yalnız ağırlık olarak geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi umutlu bir yüzle"
   - Cümle 8: «Mimi umutlu bir yüzle topu attı.»
   - Açıklama: 'umutlu bir yüzle' soyut bir anlatım, 3 yaşındaki çocuk için zor.
   - Açıklama: 'Umutlu bir yüz' soyut bir anlatım; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0039` birebir aynı, `@degisim: katmak -> atmak` (tutuyorsan), ardından `@onarim: 5c44a5283f78c1f62558ae8585ae4288b1dd9c05`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0041 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | annesi
@tohum: hello_kitty-0041
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'şemsiye', fiil 'sallamak', sıfat 'yavaş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | annesi
@plan: yağmur başladı ve turta ıslanmak üzereydi | şemsiyeyi açıp turtayı kuru kuru annesine götürdü
@tohum: hello_kitty-0041
Bir sabah Hello Kitty kolunda bir şemsiyeyle parkta hediye oyunu oynuyordu. Ağacın altındaki annesine hediye diye en sevdiği elmalı turtayı götürecekti. Ama birden yağmur başladı ve turta ıslanmak üzereydi. Hello Kitty hemen şemsiyeyi açıp turtanın üstünde tuttu. Sonra yavaş adımlarla ağaca doğru yürüdü. Turtaya tek bir damla bile düşmedi. Ağacın altına varınca şemsiyeyi salladı. Damlalar çimenlere döküldü. "Hediyen geldi, anne!" dedi Hello Kitty. Annesi turtaya baktı ve gülümsedi. "Turta kuru kalmış, aferin sana," dedi annesi. "Gel, en sevdiğimiz turtayı birlikte yiyelim, anneciğim!" dedi Hello Kitty.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "turtayı kuru kuru annesine"
   - Cümle 0 (plan satırı): «yağmur başladı ve turta ıslanmak üzereydi | şemsiyeyi açıp turtayı kuru kuru annesine götürdü»
   - Açıklama: 'kuru kuru' ikilemesi 'kuru kalmış hâlde' anlamına gelmiyor; yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parkta hediye oyunu oynuyordu"
   - Cümle 1: «Bir sabah Hello Kitty kolunda bir şemsiyeyle parkta hediye oyunu oynuyordu.»
   - Açıklama: 'Hediye oyunu' anlamı belirsiz bir ifade; çocuk ne oynandığını anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0041` birebir aynı, ardından `@onarim: 39baaad4118596bff4457506ed74ad815867da06`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0042 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | Mimi
@tohum: hello_kitty-0042
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mimi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'zincir', fiil 'homurdanmak', sıfat 'sarı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | Mimi
@plan: koşarken ikizinin kağıt zincirini kopardı | özür dileyip kopan halkaları yapıştırdı
@tohum: hello_kitty-0042
Yağmur cama tık tık vuruyordu. Hello Kitty elmalı turta yemek için mutfağa koşuyordu. Ama yerdeki sarı kağıt zincire bastı ve zincir koptu. Zinciri yapan Mimi, kopan halkalara bakıp homurdandı. Hello Kitty hemen durdu ve ikizinin yanına oturdu. "Özür dilerim, Mimi, zincirini hemen düzelteyim," dedi Hello Kitty. Mimi ona yapıştırıcıyı uzattı. Hello Kitty kopan halkaları dikkatle birbirine yapıştırdı. Zincir yine uzun ve sağlam oldu. "Teşekkürler, şimdi daha da güzel," dedi Mimi. Hello Kitty çok sevindi, çünkü ikizi yeniden gülüyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "elmalı turta yemek için"
   - Cümle 2: «Hello Kitty elmalı turta yemek için mutfağa koşuyordu.»
   - Açıklama: Tohumdaki turta özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elmalı turta yemek için mutfağa koşuyordu"
   - Cümle 2: «Hello Kitty elmalı turta yemek için mutfağa koşuyordu.»
   - Açıklama: Turta yeme hedefi amaç gibi kuruluyor ama hikayede bir daha hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0042` birebir aynı, ardından `@onarim: a04b9019d94cc535e21593d1e805a9f142fa1bce`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0044
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'kalıp', fiil 'esnemek', sıfat 'sakar'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: ekmek çok kalındı ve kalıp ekmeği kesemedi | ekmeği ikiye ayırıp ince parçaya kalıbı bastırdı
@tohum: hello_kitty-0044
@degisim: sakar -> ince
Ormanda, kamp yerinde Hello Kitty'nin annesi esnedi ve dinlenmek için uzandı. Hello Kitty herkese iyi bir arkadaştı ve annesini sevindirmek istedi. Kalp biçiminde sandviç yapacaktı ama ekmek çok kalındı ve kalıp ekmeği kesemedi. Hello Kitty ekmeğe baktı ve düşündü. Sonra ekmeği yavaşça ikiye ayırdı. İnce parçaya kalıbı iki eliyle bastırdı. Bu kez güzel bir kalp çıktı. Hello Kitty üç kalp daha yaptı ve hepsini bir tabağa dizdi. "Anne, sana bir sürprizim var!" dedi Hello Kitty. Annesi tabağı görünce güldü. "Çok teşekkürler, kızım!" dedi annesi. Sonra ikisi kalp sandviçlerini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty herkese iyi bir arkadaştı"
   - Cümle 2: «Hello Kitty herkese iyi bir arkadaştı ve annesini sevindirmek istedi.»
   - Açıklama: Arkadaş özelliği sayılıyor ama çözümde işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "herkese iyi bir arkadaştı"
   - Cümle 2: «Hello Kitty herkese iyi bir arkadaştı ve annesini sevindirmek istedi.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız söylenip geçiliyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty herkese iyi bir arkadaştı"
   - Cümle 2: «Hello Kitty herkese iyi bir arkadaştı ve annesini sevindirmek istedi.»
   - Açıklama: Bu özellik cümlesi olaya bağlanmıyor ve hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0044` birebir aynı, `@degisim: sakar -> ince` (tutuyorsan), ardından `@onarim: 71951b424757792ccf3d7639f4421cd0b999624c`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0045 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0045
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'lale', fiil 'planlamak', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: kutudaki kurabiyeler karmakarışık olmuştu | önce işini planladı ve kurabiyeleri sıraya ayırdı
@tohum: hello_kitty-0045
Hello Kitty mutfakta ilk kez yeni bir şey denemek istedi. Kurabiyelerle bir tabağa lale resmi yapacaktı. Ama kutu sallanmıştı ve içindeki kurabiyeler karmakarışık olmuştu. Yuvarlak, uzun ve yaprak gibi kurabiyeler iç içe duruyordu. Hello Kitty hemen başlamadı ve önce işini planladı. Kurabiyeleri üç sıraya ayırdı. Yuvarlak kurabiyeler çiçek olacaktı. Uzun olanlar sap, yaprak gibi olanlar da yaprak olacaktı. Sonra hepsini tabağa tek tek dizdi. Tabakta güzel bir lale oldu. Resme bakıp gülümsedi. Hello Kitty bundan sonra yeni bir işe başlamadan önce hep onu planladı.
```

**Hakem bulguları (6):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ilk kez yeni bir şey"
   - Cümle 1: «Hello Kitty mutfakta ilk kez yeni bir şey denemek istedi.»
   - Açıklama: 'İlk kez' ile 'yeni' aynı şeyi söylüyor; gereksiz tekrar.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kurabiyelerle bir tabağa lale resmi yapacaktı"
   - Cümle 2: «Kurabiyelerle bir tabağa lale resmi yapacaktı.»
   - Açıklama: Karttaki özellik kurabiye yapmak; burada hazır kurabiyeler yalnız diziliyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kutu sallanmıştı ve içindeki kurabiyeler karmakarışık olmuştu"
   - Cümle 3: «Ama kutu sallanmıştı ve içindeki kurabiyeler karmakarışık olmuştu.»
   - Açıklama: Sorun önemsiz ve sebebi zayıf; karışan kurabiyeleri ayırmak basitçe toplayıp bitirmek gibi.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "içindeki kurabiyeler karmakarışık olmuştu"
   - Cümle 3: «Ama kutu sallanmıştı ve içindeki kurabiyeler karmakarışık olmuştu.»
   - Açıklama: Kurabiyelerin karışması işi engellemeyen önemsiz bir sorun; ayırıp dizmekle kendiliğinden bitiyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "önce işini planladı"
   - Cümle 5: «Hello Kitty hemen başlamadı ve önce işini planladı.»
   - Açıklama: 'Planlamak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "hep onu planladı"
   - Cümle 12: «Hello Kitty bundan sonra yeni bir işe başlamadan önce hep onu planladı.»
   - Açıklama: 'Onu' zamirinin neyi gösterdiği belirsiz; belirsiz 'yeni bir iş' zamirle karşılanamaz, 'işini planladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0045` birebir aynı, ardından `@onarim: 07f6c8c793a4255098b588098523e1e879b122a5`, sonra gövde.
