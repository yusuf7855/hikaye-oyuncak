# Editör görevi (onarım): Hello Kitty, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0081 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0081
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'kabuk', fiil 'birleşmek', sıfat 'üzgün'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: yaprak kurabiyeleri pişirecek bir fırın yoktu | iki kabuğu birbirine dayayıp oyun fırını yaptı
@tohum: hello_kitty-0081
Ormanda rüzgar yavaşça esiyordu. Hello Kitty ve ikizi Mimi kamp yerinde yemek oyunu oynuyordu. Yuvarlak yapraklardan kurabiyeler yapmışlardı ama onları pişirecek bir fırınları yoktu. "Fırın olmadan olmaz," dedi Mimi üzgün üzgün. Hello Kitty kurabiye yapmayı çok severdi ve hemen etrafına baktı. Yerde iki büyük ağaç kabuğu buldu. Kabukları yere dikti ve üstlerini birbirine dayadı. İki kabuk üstte birleşti ve küçük bir fırın oldu. "Yaprakları buraya koy, Mimi," dedi Hello Kitty. Mimi yaprak kurabiyeleri fırının içine dizdi. Sonra ikisi birlikte yavaşça ona kadar saydı. Mimi kurabiyeleri çıkardı ve güldü. "Teşekkürler, Hello Kitty, oyunumuz çok güzel oldu!" dedi Mimi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ikizi Mimi kamp yerinde yemek oyunu"
   - Cümle 2: «Hello Kitty ve ikizi Mimi kamp yerinde yemek oyunu oynuyordu.»
   - Açıklama: İki küçük kardeş ormandaki kamp yerinde büyük olmadan yalnız; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0081` birebir aynı, ardından `@onarim: afdc978b9c991fcb4bf32788c44b1e2d964dee8b`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0082 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | annesi
@tohum: hello_kitty-0082
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: bir şey yapmak
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'çekirdek', fiil 'süslemek', sıfat 'siyah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | annesi
@plan: kozalak arkadaşın gözleri yoktu | annesinden çekirdek isteyip gözleri yaptı
@tohum: hello_kitty-0082
Hello Kitty annesiyle ormandaki kamp yerindeydi. Yeni arkadaşları çok severdi ve büyük bir kozalaktan arkadaş yapmak istedi. Ama kozalağın gözleri yoktu ve yüzü boş görünüyordu. "Anne, gözler için ne kullanabilirim?" diye sordu Hello Kitty. Annesi çantadan iki siyah çekirdek çıkardı. "Bunları dene, kızım," dedi annesi. Hello Kitty çekirdekleri onun üstüne sıkıca yerleştirdi. Artık iki küçük siyah gözü vardı. Sonra başını yeşil bir yaprakla süsledi. Annesi kozalağa baktı ve gülümsedi. Hello Kitty çok sevindi, çünkü ormanda yeni bir kozalak arkadaşı olmuştu.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Yeni arkadaşları çok severdi"
   - Cümle 2: «Yeni arkadaşları çok severdi ve büyük bir kozalaktan arkadaş yapmak istedi.»
   - Açıklama: Belirtme eki eksik; 'arkadaşlarını' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çekirdekleri onun üstüne sıkıca"
   - Cümle 7: «Hello Kitty çekirdekleri onun üstüne sıkıca yerleştirdi.»
   - Açıklama: 'Onun' zamirinin kozalağı mı annesini mi gösterdiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hello Kitty çekirdekleri onun üstüne sıkıca yerleştirdi"
   - Cümle 7: «Hello Kitty çekirdekleri onun üstüne sıkıca yerleştirdi.»
   - Açıklama: Son anılan kişi anne olduğu için 'onun' zamirinin kozalağı gösterdiği belli değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra başını yeşil bir"
   - Cümle 9: «Sonra başını yeşil bir yaprakla süsledi.»
   - Açıklama: 'Başını' Hello Kitty'nin mi kozalağın mı başı olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0082` birebir aynı, ardından `@onarim: a7f8b378d712c13f7485c16e6e6170e0d6f6e418`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0083
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: sırayla oynamak
- yan: annesi
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'resim', fiil 'asmak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: masada tek bir kalem vardı | annesine sırayla çizmeyi önerdi
@tohum: hello_kitty-0083
Evde mutfaktan güzel bir elmalı turta kokusu geliyordu. Hello Kitty ve annesi turtayı beklerken birlikte resim yapmak istedi. Ama masada tek bir kalem vardı ve ikisi aynı anda çizemezdi. Hello Kitty biraz düşündü. "Anne, sırayla çizelim, önce sen başla," dedi Hello Kitty. Annesi kağıda büyük, yuvarlak bir turta çizdi. Sonra kalemi Hello Kitty'ye verdi. Hello Kitty turtanın üstüne küçük elmalar ekledi. Sıra yine annesine geçti ve o da bir tabak yaptı. Resim bitince Hello Kitty onu bantla mutfak duvarına astı. O sırada annesi fırından gerçek turtayı çıkardı. "Çok şanslıyım, anne, iki turtam oldu!" dedi Hello Kitty.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çok şanslıyım, anne"
   - Cümle 12: «"Çok şanslıyım, anne, iki turtam oldu!" dedi Hello Kitty.»
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0083` birebir aynı, ardından `@onarim: 98e26250b2d8183cbbbdee40b3c8b116a34aa490`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0084 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | -
@tohum: hello_kitty-0084
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'piyano', fiil 'gülüşmek', sıfat 'rengarenk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | -
@plan: piyanonun arasına küçük bir dal sıkışmıştı | piyanoyu ters çevirip salladı ve dalı düşürdü
@tohum: hello_kitty-0084
@degisim: gülüşmek -> gülmek
Ormanda rüzgar yavaşça esiyordu. Hello Kitty kamp yerinde kozalak arkadaşlarına rengarenk oyuncak piyanosunu çalıyordu. Ama piyano birden ses çıkarmadı, çünkü tuşlarının arasına küçük bir dal sıkışmıştı. Hello Kitty yeni arkadaşlarına güzel bir şarkı çalmak istiyordu. Piyanoyu yavaşça ters çevirdi ve biraz salladı. Küçük dal çimenlere düştü. Piyano yeniden ses verdi. Hello Kitty komik bir şarkı çaldı ve arkadaşlarının önünde zıpladı. Bir kozalak yuvarlandı ve piyanonun yanına geldi. Buna çok güldü. Hello Kitty çok mutluydu, çünkü piyanosu yeniden çalıyordu.
```

**Hakem bulguları (9):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "piyanonun arasına küçük bir dal"
   - Cümle 0 (plan satırı): «piyanonun arasına küçük bir dal sıkışmıştı | piyanoyu ters çevirip salladı ve dalı düşürdü»
   - Açıklama: Plan satırında 'piyanonun arasına' eksik tamlama; 'piyanonun tuşlarının arasına' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty kamp yerinde kozalak"
   - Cümle 2: «Hello Kitty kamp yerinde kozalak arkadaşlarına rengarenk oyuncak piyanosunu çalıyordu.»
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylüyor ama Hello Kitty ormandaki kamp yerinde bir büyük olmadan yalnız.
   - Açıklama: Hello Kitty ormandaki kamp yerinde büyük olmadan tek başına, güvenli kullanım satırındaki 'kimse tek başına uzağa gitmez' kuralına aykırı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kamp yerinde kozalak arkadaşlarına"
   - Cümle 2: «Hello Kitty kamp yerinde kozalak arkadaşlarına rengarenk oyuncak piyanosunu çalıyordu.»
   - Açıklama: Kozalakları arkadaş saymak kişileştirme ve mecazdır.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kozalak arkadaşlarına rengarenk oyuncak"
   - Cümle 2: «Hello Kitty kamp yerinde kozalak arkadaşlarına rengarenk oyuncak piyanosunu çalıyordu.»
   - Açıklama: Kozalakları arkadaş saymak mecaz ve 3 yaşındaki çocuk için anlaşılmaz.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kozalak arkadaşlarına rengarenk oyuncak piyanosunu"
   - Cümle 2: «Hello Kitty kamp yerinde kozalak arkadaşlarına rengarenk oyuncak piyanosunu çalıyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği kozalaklara yamanıyor ve sorunun çözümünde işe yaramıyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "piyano birden ses çıkarmadı"
   - Cümle 3: «Ama piyano birden ses çıkarmadı, çünkü tuşlarının arasına küçük bir dal sıkışmıştı.»
   - Açıklama: 'Birden' zarfı olumsuz 'ses çıkarmadı' fiiline uymuyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlarına güzel bir şarkı"
   - Cümle 4: «Hello Kitty yeni arkadaşlarına güzel bir şarkı çalmak istiyordu.»
   - Açıklama: Tohumdaki arkadaş özelliği kozalaklara yakıştırılıyor ve sorunun çözümünde işe yaramıyor, karttaki özelliğe uygun kullanılmamış.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir kozalak yuvarlandı ve piyanonun yanına geldi"
   - Cümle 9: «Bir kozalak yuvarlandı ve piyanonun yanına geldi.»
   - Açıklama: Yuvarlanan kozalak sorunla ya da çözümle bağı olmayan işlevsiz bir ayrıntı.
   - Açıklama: Kozalağın yuvarlanması sorun çözüldükten sonra gelen işlevsiz bir ayrıntı.
9. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Buna çok güldü"
   - Cümle 10: «Buna çok güldü.»
   - Açıklama: Son özne kozalak olduğu için kimin güldüğü belli değil.
   - Açıklama: Özne yok; gülenin Hello Kitty mi başkası mı olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0084` birebir aynı, `@degisim: gülüşmek -> gülmek` (tutuyorsan), ardından `@onarim: bf27d0fed7a5fb4a9f9c4407a3c9f7f7e7c5f181`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0085 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0085
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'sosis', fiil 'basmak', sıfat 'sessiz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: kalıp sandviçten geçmedi çünkü içindeki sosis kalındı | babasından sosisi kesmesini isteyip kalıbı ekmeğe bastı
@tohum: hello_kitty-0085
Parkta ağaçların gölgesi serin ve sessizdi. Hello Kitty babasıyla piknikte sosisli sandviçleri kurabiye kalıbıyla yıldız yapmak istedi. Ama kalıp sandviçten geçmedi, çünkü içindeki sosis çok kalındı. Hello Kitty kurabiye yapmayı çok severdi, bu yüzden kalıbı yanında getirmişti. "Baba, sosisi küçük parçalara keser misin?" diye sordu Hello Kitty. Babası sosisi çıkardı ve küçük parçalara ayırdı. Hello Kitty kalıbı yalnız ekmeğe bastı. Ekmek kolayca yıldız oldu. Sonra sosis parçalarını yıldızın üstüne dizdi. Babası bir ısırık aldı ve güldü. "Çok güzel olmuş, kızım, teşekkür ederim!" dedi babası.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gölgesi serin ve sessizdi"
   - Cümle 1: «Parkta ağaçların gölgesi serin ve sessizdi.»
   - Açıklama: Gölge sessiz olmaz; 'sessiz' sıfatı öznesine uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ağaçların gölgesi serin ve sessizdi"
   - Cümle 1: «Parkta ağaçların gölgesi serin ve sessizdi.»
   - Açıklama: Gölge sessiz olmaz; sıfat öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0085` birebir aynı, ardından `@onarim: c0d962d7219620a91d5c39b1f265b1cf48c2d0f9`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0086 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0086
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: bir şey yapmak
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'boncuk', fiil 'buluşmak', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: şeker boncuklar kuru kurabiyelere yapışmadı | kurabiyelere önce biraz bal sürdü
@tohum: hello_kitty-0086
@degisim: buluşmak -> yapışmak
Kuşlar ağaçlarda cıvıl cıvıl ötüyordu. Hello Kitty ve Mimi parkta saklı, gölge bir köşede kurabiye süslüyordu. Ama renkli şeker boncuklar yapışmadı, çünkü kurabiyeler çok kuruydu. "Boncuklar hep düşüyor," dedi Mimi. Hello Kitty kurabiye yapmayı çok severdi ve sepete baktı. Sepette ekmekler için getirdikleri bal vardı. "Önce biraz bal sürelim, Mimi," dedi Hello Kitty. Kaşıkla her kurabiyeye ince bir bal sürdü. Sonra renkli boncukları üstüne koydu. Boncuklar bala yapıştı ve hiç düşmedi. Mimi bir kurabiye aldı ve gülümsedi. "Teşekkürler, Hello Kitty, kurabiyeler çok güzel oldu!" dedi Mimi.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "parkta saklı, gölge bir köşede"
   - Cümle 2: «Hello Kitty ve Mimi parkta saklı, gölge bir köşede kurabiye süslüyordu.»
   - Açıklama: İki küçük kardeş büyük olmadan parkın saklı bir köşesinde kalıyor; güvenli kullanım satırındaki kimsenin tek başına uzağa gitmemesi kuralına aykırı, taklit edilince tehlikeli.
   - Açıklama: İki küçük kardeş büyük olmadan parkın saklı bir köşesinde yalnız; güvenli kullanım satırı kimsenin tek başına uzağa gitmemesini ister.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "saklı, gölge bir köşede"
   - Cümle 2: «Hello Kitty ve Mimi parkta saklı, gölge bir köşede kurabiye süslüyordu.»
   - Açıklama: 'Gölge bir köşe' yanlış; 'gölgeli bir köşe' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "parkta saklı, gölge bir köşede"
   - Cümle 2: «Hello Kitty ve Mimi parkta saklı, gölge bir köşede kurabiye süslüyordu.»
   - Açıklama: 'Gölge bir köşe' ek eksik; 'gölgeli bir köşe' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "her kurabiyeye ince bir bal sürdü"
   - Cümle 8: «Kaşıkla her kurabiyeye ince bir bal sürdü.»
   - Açıklama: Bal 'ince bir bal' diye sayılmaz; 'ince bir kat bal' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0086` birebir aynı, `@degisim: buluşmak -> yapışmak` (tutuyorsan), ardından `@onarim: dc93da68cbc61e2df2bcee8e0506bfeaef7c125f`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0087 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0087
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: paylaşmak
- yan: Mimi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'sakız', fiil 'barışmak', sıfat 'vanilyalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: sepette tek bir şişe süt kalmıştı ve ikisi tartıştı | sütü iki bardağa bölüp kardeşiyle paylaştı
@tohum: hello_kitty-0087
@degisim: sakız -> süt
Bir sabah Hello Kitty ve ikizi Mimi parkta piknik yapıyordu. Sepette tek bir şişe vanilyalı süt kalmıştı. İkisi de şişeyi istedi ve biraz tartıştılar. Hello Kitty herkese iyi davranırdı ve en iyi arkadaşı Mimi'yi üzmek istemedi. Sepetten iki bardak çıkardı. "Mimi, sütü paylaşalım, yarısı senin," dedi Hello Kitty. Sütü iki bardağa yavaşça döktü. Bir bardağı Mimi'ye uzattı. "Sen çok iyi bir kardeşsin," dedi Mimi. Hello Kitty ile Mimi hemen barıştı ve birbirine sarıldı. Sonra sütlerini içtiler ve oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en iyi arkadaşı Mimi'yi"
   - Cümle 4: «Hello Kitty herkese iyi davranırdı ve en iyi arkadaşı Mimi'yi üzmek istemedi.»
   - Açıklama: İkizi olarak tanıtılan Mimi ikinci kez en iyi arkadaşı olarak tanıtılıyor.
   - Açıklama: İkiz olarak tanıtılan Mimi bu kez en iyi arkadaş diye yeniden tanıtılıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "en iyi arkadaşı Mimi'yi üzmek istemedi"
   - Cümle 4: «Hello Kitty herkese iyi davranırdı ve en iyi arkadaşı Mimi'yi üzmek istemedi.»
   - Açıklama: Mimi önce ikiz kardeş olarak tanıtılıyor, sonra en iyi arkadaş deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0087` birebir aynı, `@degisim: sakız -> süt` (tutuyorsan), ardından `@onarim: fc8cfcfc5305f0bdbd4168c3d5ecf768f2ea6d24`, sonra gövde.
