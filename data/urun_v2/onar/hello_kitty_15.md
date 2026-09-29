# Editör görevi (onarım): Hello Kitty, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0037 (deneme 3 -> 4)

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
Dışarıda soğuk bir rüzgar esiyordu. Hello Kitty yemek oyununda en sevdiği elmalı turta için elma tartacaktı. Ama önlüğünü bağlayamadı, çünkü ipleri arkadaydı. Hello Kitty arkasındaki ipleri hiç göremiyordu. Hello Kitty biraz düşündü ve önlüğü ters taktı. Böylece iki ip de öne geldi. Hello Kitty iki ipi sıkıca bağladı. Sonra terazide üç kırmızı elmayı tarttı. Elmaları büyük bir kaseye tek tek koydu. Hello Kitty çok mutluydu, çünkü önlüğünü tek başına bağlamış ve oyuna başlamıştı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "önlüğü ters taktı"
   - Cümle 5: «Hello Kitty biraz düşündü ve önlüğü ters taktı.»
   - Açıklama: Önlüğü ters takınca önlük sırta gelir ve önü korumaz; çözüm önlüğün işini bozuyor.
   - Açıklama: Önlüğü ters takmak önü açıkta bıraktığı için çözüm önlüğün işlevini bozuyor ve sorunu gerçekten çözmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0037` birebir aynı, ardından `@onarim: 51b8e42d5438e62be3bdc3268a173435d56e8478`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0038 (deneme 3 -> 4)

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
Parkta çimenlerin üstünde güneş parlıyordu. Hello Kitty annesiyle ağaçların gölgesine doğru yürüyordu. Annesinin elindeki piknik sepeti çok eskiydi ve sapı birden koptu. Bu sepet, annesinin çok sevdiği bir hediyeydi. Annesi sepete baktı ve üzüldü. Hello Kitty herkesin iyi bir arkadaşıydı ve annesine hemen yardım etmek istedi. Kırmızı kurdelesini çıkardı. Sonra kurdeleyle sapı sepete sıkıca bağladı. Annesi sepeti yavaşça kaldırdı. Sap yerinde kaldı ve sepet düşmedi. Annesi gülümsedi ve kızına sarıldı. Sonra Hello Kitty ile annesi gölgede mutlu mutlu piknik yaptı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "herkesin iyi bir arkadaşıydı"
   - Cümle 6: «Hello Kitty herkesin iyi bir arkadaşıydı ve annesine hemen yardım etmek istedi.»
   - Açıklama: Soyut bir nitelendirme ve anneye yardımla uyuşmayan bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0038` birebir aynı, ardından `@onarim: bc642f5863d19ddf7a201ea052feca3a83c18e96`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0039 (deneme 3 -> 4)

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
Hello Kitty ile Mimi, bir kutu kurabiyeyle büyük meşe ağacının altına oturmuştu. İkisi küçük bir topu sepete atma oyunu oynuyordu. Ama sepet çok hafifti ve her atışta yere devriliyordu. Top çimenlere kaçtı ve Mimi güldü. "Sepet yine düştü, Hello Kitty!" dedi Mimi. Hello Kitty biraz düşündü. Sonra evde yaptığı kurabiyelerin ağır kutusunu sepetin dibine yerleştirdi. Mimi umutluydu ve topu sepete attı. Top içine düştü ve bu kez sepet hiç kıpırdamadı. "Oldu, Hello Kitty!" dedi Mimi sevinçle. İkisi sırayla atmaya devam etti. Hello Kitty bundan sonra hafif bir sepete hep ağır bir şey koydu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mimi umutluydu ve topu"
   - Cümle 8: «Mimi umutluydu ve topu sepete attı.»
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0039` birebir aynı, `@degisim: katmak -> atmak` (tutuyorsan), ardından `@onarim: e11c7922a6d3fed3171e9b1c990542aa67d66e5d`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0042 (deneme 3 -> 4)

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
Yağmur cama tık tık vuruyordu. Hello Kitty elmalı turta yemek için mutfağa koşuyordu. Ama yerdeki sarı kağıt zincire bastı ve zincir koptu. Zinciri yapan Mimi, kopan halkalara bakıp homurdandı. Hello Kitty hemen durdu ve ikizinin yanına oturdu. "Özür dilerim, Mimi, zincirini hemen düzelteyim," dedi Hello Kitty. Mimi ona yapıştırıcıyı uzattı. Hello Kitty kopan halkaları dikkatle birbirine yapıştırdı. Zincir yine uzun ve sağlam oldu. "Teşekkürler, şimdi daha da güzel," dedi Mimi. Sonra Hello Kitty en sevdiği elmalı turtayı ikiziyle paylaştı. Hello Kitty çok sevindi, çünkü ikizi yeniden gülüyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty elmalı turta yemek için mutfağa koşuyordu"
   - Cümle 2: «Hello Kitty elmalı turta yemek için mutfağa koşuyordu.»
   - Açıklama: Tohumdaki turta özelliği iki kez geçiyor ve sorunun çözümüne yaramıyor; özellik işe yarar biçimde bir kez kullanılmamış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "elmalı turta yemek için mutfağa koşuyordu"
   - Cümle 2: «Hello Kitty elmalı turta yemek için mutfağa koşuyordu.»
   - Açıklama: Tohumdaki turta özelliği iki kez ve sorunun çözümüne katkısız biçimde geçiyor, kartın özellikler alanındaki kullanım işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0042` birebir aynı, ardından `@onarim: d7e57edde0fdf4d9bd4c55e5fc95b2491ffaf0a6`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0044 (deneme 3 -> 4)

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
Ormanda, kamp yerinde Hello Kitty'nin annesi esnedi ve dinlenmek için uzandı. Hello Kitty yeni arkadaşlarından kalıpla sandviç yapmayı öğrenmişti. Annesine kalp sandviç yapacaktı ama ekmek çok kalındı ve kalıp kesemedi. Hello Kitty ekmeğe baktı ve düşündü. Sonra ekmeği yavaşça ikiye ayırdı. İnce parçaya kalıbı iki eliyle bastırdı. Bu kez güzel bir kalp çıktı. Hello Kitty üç kalp daha yaptı ve hepsini bir tabağa dizdi. "Anne, sana bir sürprizim var!" dedi Hello Kitty. Annesi tabağı görünce güldü. "Çok teşekkürler, kızım!" dedi annesi. Sonra ikisi kalp sandviçlerini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yeni arkadaşlarından kalıpla sandviç"
   - Cümle 2: «Hello Kitty yeni arkadaşlarından kalıpla sandviç yapmayı öğrenmişti.»
   - Açıklama: Tohumdaki arkadaş özelliği yalnız geçmişte anılıyor; sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni arkadaşlarından kalıpla sandviç yapmayı öğrenmişti"
   - Cümle 2: «Hello Kitty yeni arkadaşlarından kalıpla sandviç yapmayı öğrenmişti.»
   - Açıklama: Karttaki özellik yeni arkadaş edinmeyi sevmek; burada yalnız bir bilginin kaynağı olarak anılıyor ve karttaki gibi kullanılmıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Annesine kalp sandviç yapacaktı"
   - Cümle 3: «Annesine kalp sandviç yapacaktı ama ekmek çok kalındı ve kalıp kesemedi.»
   - Açıklama: Tamlama eki eksik; 'kalp sandviçi' ya da 'kalp şeklinde sandviç' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0044` birebir aynı, `@degisim: sakar -> ince` (tutuyorsan), ardından `@onarim: a49391cd956ec4894b3e3c32b83f0eed3c61dcec`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0045 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: ince sap büküldü ve hamurdan lale devrildi | kalın bir sap yapıp çiçeği tepsiye düz koydu
@tohum: hello_kitty-0045
@degisim: planlamak -> hatırlamak
Hello Kitty mutfakta oyun hamuruyla kurabiye oyunu oynuyordu. İlk kez lale gibi bir kurabiye yapmayı denedi. Ama lale ayakta durunca ince sap büküldü ve lale devrildi. Çiçek, yapraklar ve sap birbirine yapıştı ve karmakarışık oldu. Hello Kitty hamura baktı ve biraz düşündü. Kurabiyelerin tepside hep düz durduğunu hatırladı. Hamuru yeniden ayırdı. Bu kez kalın bir sapı tepsiye düz koydu. Yanına iki yaprak, en üste de kırmızı bir çiçek yerleştirdi. Lale tepside güzelce durdu ve hiç düşmedi. Hello Kitty bundan sonra ince bir sapı hep kalın yaptı.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "oyun hamuruyla kurabiye oyunu oynuyordu"
   - Cümle 1: «Hello Kitty mutfakta oyun hamuruyla kurabiye oyunu oynuyordu.»
   - Açıklama: Aynı cümlede 'oyun' kökü üç kez gereksizce tekrarlanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ince bir sapı hep kalın yaptı"
   - Cümle 11: «Hello Kitty bundan sonra ince bir sapı hep kalın yaptı.»
   - Açıklama: İnce bir sapı kalın yapmak çelişkili bir anlatım; 'sapı hep kalın yaptı' olmalı.
   - Açıklama: İnce bir sap kalın yapılamaz; cümle anlamca çelişkili.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ince bir sapı hep kalın yaptı"
   - Cümle 11: «Hello Kitty bundan sonra ince bir sapı hep kalın yaptı.»
   - Açıklama: Son cümle ince bir sapın kalın yapıldığını söyleyerek kendi içinde çelişiyor.
   - Açıklama: İnce bir sapı kalın yapmak kendi içinde çelişkili bir ders cümlesi; ayrıca asıl çözüm çiçeği düz koymaktı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0045` birebir aynı, `@degisim: planlamak -> hatırlamak` (tutuyorsan), ardından `@onarim: 0c25091ab88c629dc83f10a763bdcc55e4a6e3d7`, sonra gövde.

### Hikâye 7: tohum hello_kitty-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0046
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: babası
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'turşu', fiil 'soğumak', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: kavanozun kapağı çok sıkıydı | babasından yardım istedi ve kapak açıldı
@tohum: hello_kitty-0046
@degisim: soğumak -> paylaşmak
Hello Kitty babasıyla parkta, ağacın gölgesinde piknik yapıyordu. Örtünün üstünde çıtır patatesler ve bir kavanoz turşu vardı. Hello Kitty turşu almak istedi ama kavanozun kapağı çok sıkıydı. İki eliyle çevirdi ama kapak hiç dönmedi. "Baba, lütfen bu kapağı açar mısın?" diye sordu Hello Kitty. Babası kapağı bir kez çevirdi ve kavanoz hemen açıldı. "Teşekkürler, babacığım!" dedi Hello Kitty. Önce babasına bir turşu uzattı. "Sen çok iyi bir piknik arkadaşısın," dedi babası. Hello Kitty ile babası turşu ve patatesleri mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sen çok iyi bir piknik arkadaşısın"
   - Cümle 9: «"Sen çok iyi bir piknik arkadaşısın," dedi babası.»
   - Açıklama: Karttaki yeni arkadaş edinme özelliği kullanılmıyor; arkadaş kelimesi yalnız babanın övgüsünde geçiyor.
   - Açıklama: Tohumdaki arkadaş edinme özelliği Hello Kitty tarafından işe yarar biçimde kullanılmıyor; yalnız babanın repliğinde kelime olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0046` birebir aynı, `@degisim: soğumak -> paylaşmak` (tutuyorsan), ardından `@onarim: 3fdd33f537a84e54a0fea6b724990befd39e0830`, sonra gövde.

### Hikâye 8: tohum hello_kitty-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | -
@tohum: hello_kitty-0047
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'sepet', fiil 'tamamlamak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | -
@plan: dört tabak vardı ama sepette iki kurabiye kalmıştı | iki kurabiyeyi ikiye böldü ve dört parça yaptı
@tohum: hello_kitty-0047
Parkta çimenler yumuşacıktı. Hello Kitty ağacın gölgesinde oyuncaklarıyla piknik oyunu oynuyordu. Ama dört tabak vardı ve sepette yalnız iki elmalı kurabiye kalmıştı. Oyunda her tabağa kurabiye konacaktı. Tabakların önünde üç oyuncağı duruyordu. Dördüncü tabak Hello Kitty'nindi. Hello Kitty sepete baktı ve düşündü. Kurabiye yaparken hamuru hep küçük parçalara ayırırdı. Şimdi de iki kurabiyeyi ortadan ikiye böldü. Artık dört parça vardı. Her tabağa bir tane koydu. Böylece sofrayı tamamladı. Hello Kitty çok sevindi, çünkü her tabakta bir parça kurabiye vardı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ağacın gölgesinde oyuncaklarıyla piknik oyunu oynuyordu"
   - Cümle 2: «Hello Kitty ağacın gölgesinde oyuncaklarıyla piknik oyunu oynuyordu.»
   - Açıklama: Hello Kitty parkta yanında hiçbir büyük olmadan tek başına oynuyor; güvenli özellik kullanımı satırı kimsenin tek başına uzağa gitmemesini ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0047` birebir aynı, ardından `@onarim: b4172367ad7465a747b51450ffb2b218c9bd417a`, sonra gövde.

### Hikâye 9: tohum hello_kitty-0048 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | annesi
@tohum: hello_kitty-0048
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: arkadaş (Yeni arkadaşlar edinmeyi çok sever; herkese iyi davranır.)
- kelimeler: isim 'tuz', fiil 'dökmek', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | annesi
@plan: hamur çok suluydu ve yapışıyordu | hamura un ve tuz döktü ve yoğurdu
@tohum: hello_kitty-0048
Evde, kahverengi mutfak masasında Hello Kitty ile annesi tuz hamuru yapıyordu. Hello Kitty hamurdan komik bir kedi arkadaş yapmak istedi. Ama hamur çok suluydu ve ellerine yapışıyordu. "Anne, biraz un ve tuz alabilir miyim?" diye sordu Hello Kitty. Annesi unu ve tuzu ona uzattı. Hello Kitty hamura bir kaşık un ve biraz tuz döktü. Sonra hamuru güzelce yoğurdu. Hamur artık ellerine yapışmadı. Hello Kitty küçük bir kedi yaptı. Annesi kediyi görünce gülümsedi. Hello Kitty çok sevindi, çünkü hamur kedisi tam istediği gibi olmuştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "komik bir kedi arkadaş yapmak"
   - Cümle 2: «Hello Kitty hamurdan komik bir kedi arkadaş yapmak istedi.»
   - Açıklama: Karttaki özellik yeni arkadaş edinmek; hamurdan kedi yapmak bu özelliği işe yarar biçimde kullanmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "komik bir kedi arkadaş yapmak istedi"
   - Cümle 2: «Hello Kitty hamurdan komik bir kedi arkadaş yapmak istedi.»
   - Açıklama: Tohumdaki arkadaş edinme özelliği karttaki gibi kullanılmıyor, yalnız hamurdan kedi yapma isteğine ad olarak geçiyor ve sorunu çözmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0048` birebir aynı, ardından `@onarim: c03d34055d73d8151785d85eb2133544fe6f8b0b`, sonra gövde.

### Hikâye 10: tohum hello_kitty-0049 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | babası
@tohum: hello_kitty-0049
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: babası
- özellik: turta (En çok elmalı turtayı sever.)
- kelimeler: isim 'defter', fiil 'doyurmak', sıfat 'pembe'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | ev | babası
@plan: babası resmi anlamadı çünkü turtada elma yoktu | turtanın üstüne kırmızı elmalar çizip yeniden gösterdi
@tohum: hello_kitty-0049
Bir sabah Hello Kitty ile babası evde resim oyunu oynuyordu. Hello Kitty pembe defterine en sevdiği elmalı turtayı çizdi. Ama resimde hiç elma yoktu, bu yüzden babası resmin ne olduğunu anlamadı. "Bu bir şapka mı?" diye sordu babası. Bu komik cevap Hello Kitty'yi çok eğlendirdi. Hemen kırmızı bir kalem aldı. Turtanın üstüne üç küçük elma çizdi. Defteri babasına yeniden gösterdi. "Bu bir elmalı turta!" dedi babası sevinçle. Sonra resmi yiyormuş gibi yaptı ve karnını tuttu. "Bu resim beni çok doyurdu, kızım," dedi babası. Hello Kitty çok sevindi, çünkü babası çizdiği turtayı sonunda anlamıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu komik cevap Hello"
   - Cümle 5: «Bu komik cevap Hello Kitty'yi çok eğlendirdi.»
   - Açıklama: Babası soru sordu, cevap vermedi; 'cevap' yanlış anlamda kullanılmış.
   - Açıklama: Babası bir soru sordu, cevap vermedi; 'cevap' kelimesi yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0049` birebir aynı, ardından `@onarim: 0e217facb835ff05596398bca555d4968185ca6d`, sonra gövde.

### Hikâye 11: tohum hello_kitty-0050 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | orman | Mimi
@tohum: hello_kitty-0050
- yer: orman (Kasabanın yakınındaki küçük orman; ağaçların arasında bir kamp yeri vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'şişe', fiil 'buruşturmak', sıfat 'küçücük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | orman | Mimi
@plan: rüzgar şişeyi devirdi ve kurabiyeler ıslandı | kapalı kutudaki kuru kurabiyeleri kardeşiyle paylaştı
@tohum: hello_kitty-0050
Ormanda hafif bir rüzgar esiyordu. Hello Kitty ile Mimi ormandaki kamp yerinde piknik yapıyordu. Birden rüzgar yerdeki şişeyi devirdi ve su Mimi'nin kurabiyelerine döküldü. Mimi ıslak kağıdı buruşturdu ve başını eğdi. Çok üzülmüştü ama utandığı için hiçbir şey demedi. Hello Kitty ikizinin yanına oturdu. Çantasından küçücük bir kutu çıkardı. Kutuda evde yaptığı kurabiyeler vardı. Kutunun kapağı sıkıydı, bu yüzden hepsi kuruydu. "Bunlar ikimize de yeter, Mimi," dedi Hello Kitty. Kurabiyelerin yarısını kardeşine verdi. "Çok teşekkür ederim," dedi Mimi sevinçle. Hello Kitty ile Mimi bundan sonra kurabiyeleri hep kapalı bir kutuda taşıdı.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ile Mimi ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ile Mimi ormandaki kamp yerinde piknik yapıyordu.»
   - Açıklama: Kartın güvenli kullanım satırına aykırı olarak iki küçük kardeş ormanda bir büyük olmadan yalnız.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ile Mimi ormandaki kamp yerinde piknik yapıyordu"
   - Cümle 2: «Hello Kitty ile Mimi ormandaki kamp yerinde piknik yapıyordu.»
   - Açıklama: İki küçük çocuk bir büyük olmadan ormanda piknik yapıyor; güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söyler.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgar yerdeki şişeyi devirdi"
   - Cümle 3: «Birden rüzgar yerdeki şişeyi devirdi ve su Mimi'nin kurabiyelerine döküldü.»
   - Açıklama: Hikaye rüzgarı hafif diye kuruyor; hafif rüzgarın şişeyi devirmesi akla yatkın değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mimi ıslak kağıdı buruşturdu"
   - Cümle 4: «Mimi ıslak kağıdı buruşturdu ve başını eğdi.»
   - Açıklama: Daha önce geçmeyen 'kağıt' belirli biçimde kullanılmış; hangi kağıt olduğu belli değil.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mimi ıslak kağıdı buruşturdu"
   - Cümle 4: «Mimi ıslak kağıdı buruşturdu ve başını eğdi.»
   - Açıklama: Kağıt daha önce kurulmadan sebepsizce beliriyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "utandığı için hiçbir şey demedi"
   - Cümle 5: «Çok üzülmüştü ama utandığı için hiçbir şey demedi.»
   - Açıklama: Mimi'nin utanması sebepsiz ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0050` birebir aynı, ardından `@onarim: 7240afae6f218cd00743ce02dad797a643c11e8c`, sonra gövde.

### Hikâye 12: tohum hello_kitty-0055 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | Mimi
@tohum: hello_kitty-0055
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Mimi
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'sabun', fiil 'susamak', sıfat 'sevimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hello Kitty | park | Mimi
@plan: küçük bir kedi sıcakta çok susamıştı | kurabiye kutusunun kapağına su döküp kediye verdi
@tohum: hello_kitty-0055
@degisim: sabun -> kutu
Hello Kitty ile Mimi parkta ağacın gölgesinde oturuyordu. Birden yanlarına sevimli küçük bir kedi geldi. Kedi yere oturdu ve soludu, çünkü sıcakta çok susamıştı. "Bu kedi su istiyor galiba," dedi Mimi yavaşça. Hello Kitty'nin yanında bir şişe su ve bir kurabiye kutusu vardı. Kutuda evde yaptığı kurabiyeler duruyordu. Hello Kitty kurabiyeleri bir peçeteye koydu. Sonra kutunun kapağına biraz su döktü. Kapağı yavaşça kedinin önüne bıraktı. Kedi hemen suyu içmeye başladı. Mimi sevinçle ellerini çırptı. Kedi suyu bitirince mutlu mutlu miyavladı. "Bak, Mimi, kedimiz artık mutlu!" dedi Hello Kitty.
```

**Hakem bulguları (6):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "yanlarına sevimli küçük bir kedi geldi"
   - Cümle 2: «Birden yanlarına sevimli küçük bir kedi geldi.»
   - Açıklama: Başlıktaki Yan alanında yalnız Mimi var; kedi kartın yanlar bölümünde yok.
   - Açıklama: Başlıktaki yan yalnız Mimi; küçük kedi kartın yanlar bölümünde yok.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "yanlarına sevimli küçük bir kedi geldi"
   - Cümle 2: «Birden yanlarına sevimli küçük bir kedi geldi.»
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları ve evcil hayvanlar kartta yok.
   - Açıklama: Kartın kararlarına göre hayvan arkadaşları kartta yok; kapalı dünyaya yeni bir hayvan karakter eklenmiş.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yere oturdu ve soludu"
   - Cümle 3: «Kedi yere oturdu ve soludu, çünkü sıcakta çok susamıştı.»
   - Açıklama: 'Soludu' tek başına 'nefes aldı' anlamına gelir; susamış kedinin hızlı hızlı soluması için 'soluyordu' ya da 'hızlı hızlı soludu' gerekirdi.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kedi yere oturdu ve soludu"
   - Cümle 3: «Kedi yere oturdu ve soludu, çünkü sıcakta çok susamıştı.»
   - Açıklama: 'Soludu' tek başına anlamı eksik bırakıyor; 'hızlı hızlı soludu' ya da 'soluk soluğa kaldı' olmalı.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty kurabiyeleri bir peçeteye koydu"
   - Cümle 7: «Hello Kitty kurabiyeleri bir peçeteye koydu.»
   - Açıklama: Tohumdaki kurabiye özelliği sorunu çözmüyor; çözümü kutunun kapağı ve su sağlıyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hello Kitty kurabiyeleri bir peçeteye koydu"
   - Cümle 7: «Hello Kitty kurabiyeleri bir peçeteye koydu.»
   - Açıklama: Kurabiyeleri peçeteye boşaltmak susuzluğa yönelmeyen fazladan bir adım; çözüm üç adıma uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0055` birebir aynı, `@degisim: sabun -> kutu` (tutuyorsan), ardından `@onarim: ef25de4e370daa58e4e52917c9208d430b0f7b5e`, sonra gövde.
