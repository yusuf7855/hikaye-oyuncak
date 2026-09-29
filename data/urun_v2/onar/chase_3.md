# Editör görevi (onarım): Chase, onarım partisi 3

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 4 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar3.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Chase | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar3.txt --ad urun_v2`
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

## Kart: Chase (kaynaklı, kapalı dünya)

- Ad: Chase (okunuş: çeys; kesme eki okunuşa uyar)
- Kimlik: Chase, bir kurtarma ekibinin polis köpeği olan bir çoban köpeği yavrusudur.
- Tür: köpek
- Güvenli özellik kullanımı: Chase kaybolanı bulur ve küçük sorunları çözer; kimseyi kovalamaz, yakalamaz ya da cezalandırmaz. Kimse yabancıyla bir yere gitmez. 'Tehlike' yerine 'bir sorun var' denir. Kediler ve tüyler yüzünden hapşırması hikayeye konmaz.
- Özellikler:
  - koku: Burnuyla koku alarak çözüm bulur. (örnek biçimler: koku, kokladı, kokusunu)
  - kural: Ekibin polis köpeğidir; kurallara uyar. (örnek biçimler: kural, kurallara)
  - şapka: Mavi bir şapka takar. (örnek biçimler: şapka, şapkası)
- Yerler:
  - dağ: Kasabanın yakınındaki karlı dağ.
  - deniz: Kasabanın kıyısı; kumsal ve iskele.
  - orman: Kasabanın yakınında, ağaçların arasındaki kamp yeri.
  - park: Kasabadaki çocuk oyun parkı.
  - ev: Ekibin yüksek kulesi ve köpeklerin kulübeleri.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Ryder: On yaşında bir çocuk; ekibin başıdır. Köpeklere bakar ve işe uygun köpeği o seçer. Tür: oğlan; konuşur. Yüzey biçimleri: Ryder
  - Marshall: Ekibin itfaiyeci köpeği; altı yaşında, benekli bir köpek. Biraz sakardır ama cesur ve yardımseverdir. Tür: köpek; konuşur. Yüzey biçimleri: Marshall
  - Skye: Helikopter kullanan pilot köpek; ekibin en küçüğü, küçük hayvanları çok sever. Tür: köpek; konuşur. Yüzey biçimleri: Skye
  - Rubble: İnşaat köpeği; güçlü, şakacıdır ve yemek yemeyi sever. Tür: köpek; konuşur. Yüzey biçimleri: Rubble
- Dünya kuralları:
  - Chase slogan söylemez; kimse kendi adıyla konuşmaz.
  - Ryder bir çocuktur, köpek değildir.
  - Görevler karışmaz: Chase polis, Marshall itfaiyeci, Skye pilot, Rubble inşaat köpeğidir.
- Yasak adlar: Rocky, Zuma, Everest, Tracker, Goodway, Chickaletta, Turbot, Humdinger, Robo-Dog, Jake, Liberty, Rex
- Yasak: Araçların kovalamacası, sirenle hız ve kötü karakterler hikayeye girmez.
- İzinli dünya kelimeleri: polis, koku, şapka, itfaiye, helikopter, kule, kulübe, iskele

## Onarılacak hikâyeler

### Hikâye 1: tohum chase-0002 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0002
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pirinç', fiil 'çözmek', sıfat 'düz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: uçurtmanın ipi iskelenin direğine dolandı | yavaşça yürüdü ve düğümü çözdü
@tohum: chase-0002
@degisim: pirinç -> uçurtma
Chase kumsalda sarı bir uçurtma uçuruyordu. Birden güçlü bir rüzgar esti ve uçurtma iskeleye doğru gitti. Uçurtmanın ipi iskelenin kısa bir direğine dolandı. Uçurtma tahtaların üstüne indi ve orada kaldı. Chase hemen iskeleye koşmak istedi. Ama iskelede koşmak kurallara uygun değildi. Chase yavaş yavaş yürüdü. İp direğe düğüm olmuştu. Chase düğümü dişleriyle dikkatle çözdü. Sonra uçurtmayı aldı ve düz kuma geri döndü. Biraz koştu ve uçurtma tekrar havaya yükseldi. Chase çok sevindi, çünkü sarı uçurtması yine gökyüzündeydi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iskelede koşmak kurallara uygun değildi"
   - Cümle 6: «Ama iskelede koşmak kurallara uygun değildi.»
   - Açıklama: 'Kurallara uygun değildi' soyut bir anlatım ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Kurallara uygun' soyut bir anlatım; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0002` birebir aynı, `@degisim: pirinç -> uçurtma` (tutuyorsan), ardından `@onarim: 23d87e33eeff9a4c59d7176ebd8c5ffe5fa9cfb4`, sonra gövde.

### Hikâye 2: tohum chase-0003 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0003
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'valiz', fiil 'yetişmek', sıfat 'sabunlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: güneş çok parlaktı ve küçük çiçek solmaya başladı | çiçeği suladı ve şapkasıyla ona gölge yaptı
@tohum: chase-0003
@degisim: sabunlu -> parlak
Bir sabah Chase kamp yerinde çiçek sulama oyunu oynuyordu. Yanında küçük bir valiz vardı. Ağaçların arasında yetişen küçük sarı çiçek parlak güneşte solmaya başlamıştı. Chase çiçeği kurtarmak istedi. Valizi açtı ve içinden bir kova aldı. Kovayla çeşmeden su getirdi. Çiçeğin toprağını yavaşça suladı. Sonra mavi şapkasını çıkardı ve yerdeki bir dala taktı. Dalı çiçeğin yanına dikti. Şapka çiçeğin üstüne küçük bir gölge yaptı. Biraz sonra çiçek yeniden dik durdu. Chase çok sevindi, çünkü sarı çiçeği kurtarmıştı.
```

**Hakem bulguları (6):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çiçek sulama oyunu oynuyordu"
   - Cümle 1: «Bir sabah Chase kamp yerinde çiçek sulama oyunu oynuyordu.»
   - Açıklama: Chase çiçek sulama oyunu oynarken yanında su yok ve çiçek susuzluktan soluyor, bu durum birbiriyle çelişiyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Yanında küçük bir valiz vardı"
   - Cümle 2: «Yanında küçük bir valiz vardı.»
   - Açıklama: Kartta Chase'e ait bir valiz eşyası yok; kapalı dünyaya kartta olmayan bir eşya ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanında küçük bir valiz vardı"
   - Cümle 2: «Yanında küçük bir valiz vardı.»
   - Açıklama: Valiz ve içindeki kova çözümü sebepsizce getirmek için beliriyor.
   - Açıklama: Ormanda valiz ve içindeki kova yalnız çözümü getirmek için sebepsizce beliriyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Valizi açtı ve içinden bir kova aldı"
   - Cümle 5: «Valizi açtı ve içinden bir kova aldı.»
   - Açıklama: Çözüm kova alma, su getirme, sulama, şapkayı dala takma ve dalı dikme gibi ikiden çok adım sürüyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kovayla çeşmeden su getirdi"
   - Cümle 6: «Kovayla çeşmeden su getirdi.»
   - Açıklama: Ormanda çeşme hiç kurulmadan sebepsizce beliriyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra mavi şapkasını çıkardı ve yerdeki bir dala taktı"
   - Cümle 8: «Sonra mavi şapkasını çıkardı ve yerdeki bir dala taktı.»
   - Açıklama: Çözüm sulama ve gölge yapma olarak iki ayrı işe ve valiz açma, su getirme, dal dikme gibi ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0003` birebir aynı, `@degisim: sabunlu -> parlak` (tutuyorsan), ardından `@onarim: ec19318d1e0054d9c79ee84267c5dd164aef4b0d`, sonra gövde.

### Hikâye 3: tohum chase-0004 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0004
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kilit', fiil 'yapışmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: saklandı ama mavi şapkası görünüyordu | şapkasını karla bembeyaz yaptı ve yeniden saklandı
@tohum: chase-0004
@degisim: kilit -> kar
Bir sabah Chase ile Rubble karlı dağda saklambaç oynuyordu. Chase büyük bir kar yığınının arkasına saklandı. Ama mavi şapkası yığının üstünden görünüyordu ve Rubble onu hemen buldu. "Şapkanı gördüm, Chase!" dedi Rubble ve güldü. Chase şapkasını yumuşak karın içine iyice bastırdı. Kar önce şapkaya küçük noktalar gibi yapıştı ve şapka puantiyeli oldu. Sonra noktalar büyüdü ve şapka kar gibi bembeyaz oldu. Chase başka bir yığının arkasına saklandı. Rubble her yere baktı ama onu bulamadı. "Buradayım!" dedi Chase ve karın arkasından zıpladı. İkisi de çok sevindi, çünkü bu oyun çok eğlenceli olmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve şapka puantiyeli oldu"
   - Cümle 6: «Kar önce şapkaya küçük noktalar gibi yapıştı ve şapka puantiyeli oldu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bildiği bir kelime değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kar önce şapkaya küçük noktalar gibi yapıştı ve şapka puantiyeli oldu"
   - Cümle 6: «Kar önce şapkaya küçük noktalar gibi yapıştı ve şapka puantiyeli oldu.»
   - Açıklama: Tek bir bastırmadan sonra noktaların kendiliğinden büyüyüp şapkayı beyazlatması sebepsiz ve işlevsiz bir ara ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra noktalar büyüdü ve şapka kar gibi bembeyaz oldu"
   - Cümle 7: «Sonra noktalar büyüdü ve şapka kar gibi bembeyaz oldu.»
   - Açıklama: Kar noktaları hiçbir sebep olmadan kendi kendine büyüyor ve puantiyeli ara aşama olayda işe yaramayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0004` birebir aynı, `@degisim: kilit -> kar` (tutuyorsan), ardından `@onarim: 295ffced1b85304a5014a91cd249527333443e9d`, sonra gövde.

### Hikâye 4: tohum chase-0005 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0005
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'elma', fiil 'barışmak', sıfat 'ıslak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: elma kuma düştü ve her yeri kum oldu | elmayı yağmurun altında yıkadı
@tohum: chase-0005
@degisim: barışmak -> yıkamak
Chase yağmurlu bir sabah kumsalda kırmızı bir elma yiyordu. Birden elma ağzından düştü ve ıslak kumda yuvarlandı. Elmanın her yerine kum yapıştı. Chase elmayı hemen yemek istedi. Ama Chase kurallara uyardı ve kumlu elmayı yıkamadan yemedi. Elmayı dişleriyle tuttu ve başını yağmura doğru kaldırdı. Damlalar elmanın üstüne tık tık düştü. Kum yavaş yavaş aktı ve elma tertemiz oldu. Chase kırmızı elmasını mutlu mutlu yedi. Chase çok sevindi, çünkü yağmur elmasını onun için yıkamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama Chase kurallara uyardı"
   - Cümle 5: «Ama Chase kurallara uyardı ve kumlu elmayı yıkamadan yemedi.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve 'uyardı' kelimesi 'ikaz etti' anlamıyla da karışabilir.
   - Açıklama: 'Kurallara uyardı' soyut bir alışkanlık anlatımı ve 'uyardı' küçük çocukça 'uyarmak' olarak okunabilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yağmur elmasını onun için yıkamıştı"
   - Cümle 10: «Chase çok sevindi, çünkü yağmur elmasını onun için yıkamıştı.»
   - Açıklama: Yağmura bilinçli bir iş yükleyen kişileştirme 3 yaşındaki çocuğa uygun olmayan bir mecaz.
   - Açıklama: Yağmur Chase için bilerek iş yapan biri gibi anlatılıyor; kişileştirme mecazı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0005` birebir aynı, `@degisim: barışmak -> yıkamak` (tutuyorsan), ardından `@onarim: 700989d62594ea950ce92c134d413919263ae309`, sonra gövde.
