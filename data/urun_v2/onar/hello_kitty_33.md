# Editör görevi (onarım): Hello Kitty, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hello_kitty_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hello_kitty_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum hello_kitty-0140 (deneme 1 -> 2)

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
@plan: oyunda elmalı turta yapacaktı ama elması yoktu | kozalakları toplayıp turta gibi dizdi
@tohum: hello_kitty-0140
@degisim: yarışmak -> toplamak
Rüzgar ağaçların arasında yavaş yavaş esiyordu. Hello Kitty ormandaki kamp yerinde yemek yapma oyunu oynuyordu. Oyunda sağlıklı bir elmalı turta yapmak istiyordu ama hiç elması yoktu. Hello Kitty etrafına baktı ve yerde yuvarlak kozalaklar gördü. Kozalakları tek tek topladı. Sonra kuru bir dalı süpürge gibi kullandı. Düz bir taşın üstündeki toprağı süpürdü. Kozalakları taşın üstüne, gerçek bir turtadaki elmalar gibi daire şeklinde dizdi. Kenarlarına da sarı yapraklar koydu. Hayali turta çok güzel oldu. Hello Kitty turtasına baktı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hello Kitty ormandaki kamp yerinde"
   - Cümle 2: «Hello Kitty ormandaki kamp yerinde yemek yapma oyunu oynuyordu.»
   - Açıklama: Güvenli kullanım satırı kimsenin tek başına uzağa gitmediğini söylerken Hello Kitty ormanda büyüksüz, tek başına.
   - Açıklama: Güvenli kullanım satırına göre kimse tek başına uzağa gitmez; Hello Kitty ormanda yalnız.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oyunda sağlıklı bir elmalı turta"
   - Cümle 3: «Oyunda sağlıklı bir elmalı turta yapmak istiyordu ama hiç elması yoktu.»
   - Açıklama: 'Sağlıklı' soyut bir kavram ve oyun turtası için anlamsız.
   - Açıklama: 'Sağlıklı' soyut bir nitelik ve oyun turtası için anlamsız.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kuru bir dalı süpürge gibi kullandı"
   - Cümle 6: «Sonra kuru bir dalı süpürge gibi kullandı.»
   - Açıklama: Çözüm toplama, süpürme, dizme ve yaprak koyma ile iki adımı aşıyor.
   - Açıklama: Çözüm toplama, süpürme, dizme ve süsleme ile 2 adımdan uzun sürüyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayali turta çok güzel oldu"
   - Cümle 10: «Hayali turta çok güzel oldu.»
   - Açıklama: 'Hayali' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0140` birebir aynı, `@degisim: yarışmak -> toplamak` (tutuyorsan), ardından `@onarim: a2481c8ff831f931d1072d28ae43b761f9595e05`, sonra gövde.

### Hikâye 2: tohum hello_kitty-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | ev | -
@tohum: hello_kitty-0141
- yer: ev (Ailenin birlikte yaşadığı ev; kurabiye yapılan bir mutfağı vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'mont', fiil 'incelemek', sıfat 'çikolatalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hello Kitty | ev | -
@plan: oyun hamuru çok kuruydu ve kurabiyeler kırılıyordu | hamura biraz su koydu ve yoğurdu
@tohum: hello_kitty-0141
@degisim: mont -> su
Evin mutfağında Hello Kitty oyun hamuruyla oynuyordu. Kahverengi hamurdan çikolatalı kurabiyeler yapacaktı. Ama hamur çok kuruydu ve her kurabiye kırılıyordu. Hello Kitty hamuru dikkatle inceledi. Gerçek kurabiye yaparken de kuru hamura biraz su koyardı. Bir kaşık suyu hamura yavaşça damlattı. Sonra hamuru uzun uzun yoğurdu. Hamur yumuşadı ve artık kırılmadı. Hello Kitty hamurdan yuvarlak kurabiyeler yaptı. Her kurabiyeye komik bir yüz çizdi. Bir tanesinin burnu çok büyük oldu ve Hello Kitty güldü. Sonra kurabiyeleri tabağa dizdi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşadı ve artık kırılmadı"
   - Cümle 8: «Hamur yumuşadı ve artık kırılmadı.»
   - Açıklama: Kırılan hamur değil kurabiyelerdi; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0141` birebir aynı, `@degisim: mont -> su` (tutuyorsan), ardından `@onarim: c9b0f15716618f294770474aacdbe0bd00394e41`, sonra gövde.

### Hikâye 3: tohum hello_kitty-0142 (deneme 1 -> 2)

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
@plan: koşarken kardeşinin uçurtmasına bastı ve yırttı | özür diledi ve yırtık yeri bantla yapıştırdı
@tohum: hello_kitty-0142
Hello Kitty ile Mimi parkta uçurtma uçurmaya hazırlanıyordu. Hello Kitty koşarken Mimi'nin kağıt uçurtmasına bastı ve uçurtma yırtıldı. Mimi yırtık uçurtmaya baktı ve çok üzüldü. Hello Kitty hemen kardeşinin yanına oturdu ve ondan özür diledi. Mimi'nin çantası her zaman çok düzenliydi. Mimi çantasından bir bant çıkardı ve Hello Kitty'ye verdi. Hello Kitty yırtık yeri bantla dikkatlice yapıştırdı. Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı. Mimi kurabiyesini yedi ve gülümsedi. Rüzgar esince uçurtma yükseldi. Hello Kitty ile Mimi uçurtmayı mutlu mutlu uçurdu.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra kendi yaptığı kurabiyeleri"
   - Cümle 8: «Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Tohumdaki kurabiye özelliği sorun bantla çözüldükten sonra ekleniyor, işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı"
   - Cümle 8: «Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Tohumdaki kurabiye özelliği sorunun çözümünde işe yaramıyor, sona eklenmiş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kendi yaptığı kurabiyeleri Mimi ile paylaştı"
   - Cümle 8: «Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Kurabiyeler sebepsiz beliriyor ve uçurtma sorunuyla hiçbir ilgisi yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı"
   - Cümle 8: «Sonra kendi yaptığı kurabiyeleri Mimi ile paylaştı.»
   - Açıklama: Kurabiyeler sebepsiz beliriyor ve uçurtma sorununda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0142` birebir aynı, ardından `@onarim: 511ccd69c061eb606f137c7741310c1bc2553257`, sonra gövde.

### Hikâye 4: tohum hello_kitty-0143 (deneme 1 -> 2)

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
Hello Kitty babasıyla parkta, ağacın gölgesinde piknik yapıyordu. Babası yarı uyanık, örtünün üstünde uzanıyordu. Hello Kitty topla oynarken top babasının bardağına çarptı ve meyve suyu döküldü. "Eyvah, meyve suyum örtüye döküldü!" dedi babası. Hello Kitty babasının yanına koştu. "Özür dilerim, babacığım, hiç dikkat etmedim," dedi Hello Kitty. Şişeyi aldı ve bardağı yeniden doldurdu. Sonra en sevdiği elmalı turtadan kendi dilimini babasına verdi. "Bu dilim de senin olsun," dedi Hello Kitty. Babası turtayı yedi ve kızına sarıldı. İkisi pikniklerine mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babası yarı uyanık, örtünün üstünde uzanıyordu"
   - Cümle 2: «Babası yarı uyanık, örtünün üstünde uzanıyordu.»
   - Açıklama: Babanın yarı uyanık olması hiçbir işe yaramayan bir ayrıntı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "en sevdiği elmalı turtadan kendi dilimini"
   - Cümle 8: «Sonra en sevdiği elmalı turtadan kendi dilimini babasına verdi.»
   - Açıklama: Bardak doldurulduktan sonra turta vermek çözüme fazladan bir adım ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0143` birebir aynı, `@degisim: demet -> bardak` (tutuyorsan), ardından `@onarim: f859bc902f3b1b90469c538aad0d239a6899e13d`, sonra gövde.

### Hikâye 5: tohum hello_kitty-0144 (deneme 1 -> 2)

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
@plan: camın üstü su damlalarıyla doluydu ve kar görünmüyordu | camı eliyle ovdu ve kar tanelerini gördü
@tohum: hello_kitty-0144
@degisim: pul -> kalıp
Dışarıda sessizce kar yağıyordu. Hello Kitty mutfaktaki pencereden kara bakmak istedi. Ama mutfak çok sıcaktı ve camın üstü su damlalarıyla doluydu. Hello Kitty eliyle camı yavaşça ovdu. Camda küçük, temiz bir yer açıldı. Hello Kitty dışarıda yıldız gibi kar taneleri gördü. Bu kar taneleri onun yıldız kurabiyelerine çok benziyordu. Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi. Kalıbı camın ıslak yerine bastırdı. Camda küçük bir yıldız çıktı. Sıcak mutfak karı izlemek için güvenli bir yerdi. Hello Kitty bundan sonra kar yağınca camı ovdu ve karı içeriden izledi.
```

**Hakem bulguları (8):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu kar taneleri onun yıldız kurabiyelerine"
   - Cümle 7: «Bu kar taneleri onun yıldız kurabiyelerine çok benziyordu.»
   - Açıklama: Kar tanelerinin yıldıza benzediği bir önceki cümlede söylenmişken yeniden tekrarlanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yıldız şeklindeki kurabiye kalıbını getirdi"
   - Cümle 8: «Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi.»
   - Açıklama: Tohumdaki kurabiye özelliği sorunun çözümüne katkı vermeden süs olarak kullanılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi"
   - Cümle 8: «Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi.»
   - Açıklama: Tohumdaki kurabiye özelliği sorunun çözümünde işe yaramıyor; sorun camı ovmakla çözülmüş.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yıldız şeklindeki kurabiye kalıbını getirdi"
   - Cümle 8: «Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi.»
   - Açıklama: Sorun çözüldükten sonra kalıp sebepsizce getiriliyor ve olaya işlev katmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi"
   - Cümle 8: «Hello Kitty yıldız şeklindeki kurabiye kalıbını getirdi.»
   - Açıklama: Sorun çözüldükten sonra gelen kurabiye kalıbı olaya bağlanmayan işlevsiz bir ayrıntı.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sıcak mutfak karı izlemek için güvenli bir yerdi"
   - Cümle 11: «Sıcak mutfak karı izlemek için güvenli bir yerdi.»
   - Açıklama: 'Güvenli bir yer' soyut ve olaya bağlanmayan bir değerlendirme, küçük çocuğa uygun değil.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karı izlemek için güvenli bir yerdi"
   - Cümle 11: «Sıcak mutfak karı izlemek için güvenli bir yerdi.»
   - Açıklama: 'Güvenli' soyut bir kavram ve olaydan çıkan somut bir ders değil.
8. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra kar yağınca camı ovdu"
   - Cümle 12: «Hello Kitty bundan sonra kar yağınca camı ovdu ve karı içeriden izledi.»
   - Açıklama: 'Bundan sonra' ile süreklilik anlatılırken tek seferlik 'ovdu' kullanılmış; 'ovardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0144` birebir aynı, `@degisim: pul -> kalıp` (tutuyorsan), ardından `@onarim: 7e2babbbcc9490659ec0ea9c8444e7fbfa2d2e25`, sonra gövde.

### Hikâye 6: tohum hello_kitty-0146 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hello Kitty | park | babası
@tohum: hello_kitty-0146
- yer: park (Evin yakınındaki büyük park; çimenler, çiçekler ve piknik yapılan ağaçların gölgesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babası
- özellik: kurabiye (Kurabiye yapmayı çok sever.)
- kelimeler: isim 'pilav', fiil 'alkışlamak', sıfat 'peynirli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hello Kitty | park | babası
@plan: babası pilavı evde unuttu ve çok acıktı | çantasındaki kurabiyeleri babasına verdi
@tohum: hello_kitty-0146
Rüzgar parkta hafifçe esiyordu. Hello Kitty babasıyla ağacın gölgesinde piknik yapıyordu. Ama babası pilavı evde unutmuştu. "Eyvah, pilavı mutfakta bıraktım," dedi babası. Babası çok acıkmıştı. Hello Kitty kendi çantasını açtı. İçinde sabah birlikte yaptıkları peynirli kurabiyeler vardı. "Baba, kurabiyelerimizi de unuttun mu?" diye sordu Hello Kitty. Babası kurabiyeleri görünce güldü ve kızını alkışladı. "Kurabiyeler çok güzel olmuş," dedi babası. İkisi kurabiyeleri paylaşıp yedi. Hello Kitty çok sevindi, çünkü babası artık aç değildi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurabiyelerimizi de unuttun mu?"
   - Cümle 8: «"Baba, kurabiyelerimizi de unuttun mu?" diye sordu Hello Kitty.»
   - Açıklama: Kurabiyeler Hello Kitty'nin elindeyken 'unuttun mu' sorusu anlamca yerinde değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Baba, kurabiyelerimizi de unuttun mu?"
   - Cümle 8: «"Baba, kurabiyelerimizi de unuttun mu?" diye sordu Hello Kitty.»
   - Açıklama: Kurabiyeler Hello Kitty'nin çantasında dururken babasına onları da unutup unutmadığını sorması çelişkili.
   - Açıklama: Kurabiyeler Hello Kitty'nin kendi çantasında dururken babasına onları da unutup unutmadığını sorması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hello_kitty-0146` birebir aynı, ardından `@onarim: f77c04e488e005184dbf90152bef00cec9d6ab84`, sonra gövde.
