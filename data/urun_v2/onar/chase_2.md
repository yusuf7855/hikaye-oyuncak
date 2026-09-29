# Editör görevi (onarım): Chase, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar2.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0002 (deneme 2 -> 3)

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
Chase kumsalda sarı bir uçurtma uçuruyordu. Birden güçlü bir rüzgar esti ve uçurtma iskeleye doğru gitti. Uçurtmanın ipi iskelenin kısa bir direğine dolandı. Uçurtma tahtaların üstüne indi ve orada kaldı. Chase hemen iskeleye koşmak istedi. Ama Chase kurallara uyan bir polis köpeğiydi. İskelede kimse koşmazdı. Chase yavaş yavaş yürüdü. İp direğe düğüm olmuştu. Chase düğümü dişleriyle dikkatle çözdü. Sonra uçurtmayı aldı ve düz kuma geri döndü. Biraz koştu ve uçurtma tekrar havaya yükseldi. Chase çok sevindi, çünkü sarı uçurtması yine gökyüzündeydi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyan bir polis köpeğiydi"
   - Cümle 6: «Ama Chase kurallara uyan bir polis köpeğiydi.»
   - Açıklama: 'Kurallara uyan' soyut bir kavram; küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0002` birebir aynı, `@degisim: pirinç -> uçurtma` (tutuyorsan), ardından `@onarim: 38bf1a0283f15143fc89024194d1912437ea4c2b`, sonra gövde.

### Hikâye 2: tohum chase-0003 (deneme 2 -> 3)

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
Bir sabah Chase kamp yerinde bahçe oyunu oynuyordu. Ağaçların arasında küçük sarı bir çiçek yetişiyordu. Ama güneş çok parlaktı ve çiçek solmaya başlamıştı. Chase çiçeği kurtarmak istedi. Küçük valizini açtı ve içinden kovasını aldı. Kamp çeşmesinden kovayla su getirdi. Çiçeğin toprağını yavaşça suladı. Sonra mavi şapkasını çıkardı ve yerdeki bir dala taktı. Dalı çiçeğin yanına dikti. Şapka çiçeğin üstüne küçük bir gölge yaptı. Biraz sonra çiçek yeniden dik durdu. Chase çok sevindi, çünkü bahçesindeki tek çiçeği kurtarmıştı.
```

**Hakem bulguları (8):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kamp yerinde bahçe oyunu oynuyordu"
   - Cümle 1: «Bir sabah Chase kamp yerinde bahçe oyunu oynuyordu.»
   - Açıklama: 'Bahçe oyunu' belirsiz ve kamp yerine uymayan bir kullanım.
   - Açıklama: 'Bahçe oyunu' belirsiz bir ifade ve kamp yeri bahçe değil; kelime doğru anlamda kullanılmamış.
2. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "kamp yerinde bahçe oyunu oynuyordu"
   - Cümle 1: «Bir sabah Chase kamp yerinde bahçe oyunu oynuyordu.»
   - Açıklama: Orman tarifi ağaçların arasındaki kamp yeri; hikaye yeri Chase'in bahçesi gibi anlatıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Küçük valizini açtı ve içinden kovasını aldı"
   - Cümle 5: «Küçük valizini açtı ve içinden kovasını aldı.»
   - Açıklama: Kartta Chase'in valizi ya da kovası gibi bir eşya yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Küçük valizini açtı ve içinden kovasını aldı"
   - Cümle 5: «Küçük valizini açtı ve içinden kovasını aldı.»
   - Açıklama: Valiz ve içindeki kova önceden kurulmadan, çözümü kolaylaştırmak için sebepsizce beliriyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bahçesindeki tek çiçeği kurtarmıştı"
   - Cümle 12: «Chase çok sevindi, çünkü bahçesindeki tek çiçeği kurtarmıştı.»
   - Açıklama: Çiçek kamp yerinde, ağaçların arasında; 'bahçesindeki' yanlış anlamda kullanılmış.
6. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bahçesindeki tek çiçeği kurtarmıştı"
   - Cümle 12: «Chase çok sevindi, çünkü bahçesindeki tek çiçeği kurtarmıştı.»
   - Açıklama: Kartta Chase'in bir bahçesi yok; kapalı dünyaya karttaki yerler dışında bir mülk ekleniyor.
   - Açıklama: Kartta Chase'in bir bahçesi yok; kapalı dünyaya ev/mülk ekleniyor.
7. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "bahçesindeki tek çiçeği kurtarmıştı"
   - Cümle 12: «Chase çok sevindi, çünkü bahçesindeki tek çiçeği kurtarmıştı.»
   - Açıklama: Orman tarifi ağaçların arasındaki kamp yeri; yer Chase'in bahçesi gibi anlatılıyor.
8. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bahçesindeki tek çiçeği kurtarmıştı"
   - Cümle 12: «Chase çok sevindi, çünkü bahçesindeki tek çiçeği kurtarmıştı.»
   - Açıklama: Çiçek ormanda ağaçların arasında yetişiyor, ama son cümlede Chase'in bahçesindeki çiçek diye anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0003` birebir aynı, `@degisim: sabunlu -> parlak` (tutuyorsan), ardından `@onarim: 5e33364e7899c95cc1093844b66cdd2f4a303731`, sonra gövde.

### Hikâye 3: tohum chase-0004 (deneme 2 -> 3)

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
Bir sabah Chase ile Rubble karlı dağda saklambaç oynuyordu. Chase büyük bir kar yığınının arkasına saklandı. Ama mavi şapkası yığının üstünden görünüyordu ve Rubble onu hemen buldu. "Şapkanı gördüm, Chase!" dedi Rubble ve güldü. Şapkasını yumuşak karın üstüne bastırdı. Kar şapkaya yapıştı ama şapka yalnız beyaz puantiyeli oldu. Mavi yerler yine görünüyordu. Chase şapkayı yine kara bastırdı. Bu kez şapka kar gibi bembeyaz oldu. Chase başka bir yığının arkasına saklandı. Rubble her yere baktı ama onu bulamadı. "Buradayım!" dedi Chase ve karın arkasından zıpladı. İkisi de çok sevindi, çünkü bu oyun çok eğlenceli olmuştu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şapkasını yumuşak karın üstüne bastırdı."
   - Cümle 5: «Şapkasını yumuşak karın üstüne bastırdı.»
   - Açıklama: Önceki cümlenin öznesi Rubble olduğundan şapkayı kimin bastırdığı ve 'Şapkasını' kimi gösterdiği belli değil.
   - Açıklama: Öznesiz cümlede son özne Rubble olduğu için şapkayı kimin bastırdığı belli değil; Chase olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şapka yalnız beyaz puantiyeli oldu"
   - Cümle 6: «Kar şapkaya yapıştı ama şapka yalnız beyaz puantiyeli oldu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase şapkayı yine kara bastırdı"
   - Cümle 8: «Chase şapkayı yine kara bastırdı.»
   - Açıklama: Çözüm ilk denemede işe yaramıyor ve bastırma, yeniden bastırma, yeniden saklanma diye ikiden fazla adıma uzuyor.
   - Açıklama: İlk bastırma işe yaramıyor ve çözüm bastırma, yeniden bastırma ve yeniden saklanma olarak iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0004` birebir aynı, `@degisim: kilit -> kar` (tutuyorsan), ardından `@onarim: e8a04e4bc825b61ec947e30863559521295ef35e`, sonra gövde.

### Hikâye 4: tohum chase-0005 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: yağmur başladı ve kum ıslandı | şemsiyenin altına gitti ve kuru kaldı
@tohum: chase-0005
@degisim: barışmak -> dinlemek
Chase kumsalda oturmuş, kırmızı bir elma yiyordu. Yakında büyük bir şemsiye vardı. Birden yağmur başladı ve kum çabucak ıslandı. Chase ıslak kumda oturmak istemedi. Chase kurallara uyan bir polis köpeğiydi. Yağmurda hep kuru bir yere giderdi. Elmasını ağzına aldı ve şemsiyenin altına koştu. Orada hiç yağmur yoktu. Damlalar şemsiyenin üstüne tık tık vuruyordu. Chase bu sesi dikkatle dinledi. Ses küçük bir davulun sesine benziyordu. Biraz sonra yağmur dindi ve güneş çıktı. Chase çok mutluydu, çünkü yağmurun sesini kuru bir yerde dinlemişti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yakında büyük bir şemsiye"
   - Cümle 2: «Yakında büyük bir şemsiye vardı.»
   - Açıklama: Cümle başındaki 'Yakında' çocuk için 'kısa süre sonra' anlamında okunur; 'Chase'in yanında' gibi açık bir yer bildirimi olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yakında büyük bir şemsiye vardı"
   - Cümle 2: «Yakında büyük bir şemsiye vardı.»
   - Açıklama: 'Yakında' çoğunlukla 'az sonra' anlamında okunur; yer için 'Chase'in yakınında' denmeliydi.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yağmur başladı ve kum çabucak ıslandı"
   - Cümle 3: «Birden yağmur başladı ve kum çabucak ıslandı.»
   - Açıklama: Kumun ıslanması çocuğun önemseyeceği bir sorun değil ve tek adımda kendiliğinden geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uyan bir polis köpeğiydi"
   - Cümle 5: «Chase kurallara uyan bir polis köpeğiydi.»
   - Açıklama: Kurallara uyma özelliği olaya bağlanmıyor; yağmurdan kaçmak bir kural değil, işlevsiz ayrıntı.
   - Açıklama: Kurallara uyma özelliği olaya bağlanmadan araya sokulmuş, yağmurdan kaçmakla bir kural ilişkisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0005` birebir aynı, `@degisim: barışmak -> dinlemek` (tutuyorsan), ardından `@onarim: de4eb4a0c966804796ef5510f5f0058ca019da29`, sonra gövde.

### Hikâye 5: tohum chase-0008 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0008
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: kaybolan eşya
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kakao', fiil 'kurmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: rüzgar esti ve bardak kayboldu | bardağın durduğu yere gidip kumdaki izin peşinden gitti
@tohum: chase-0008
@degisim: kakao -> süt
Kumsalda rüzgarlı bir gündü. Chase ile Marshall kuma büyük bir şemsiye kurdu. Yanlarında bir şişe süt ve iki bardak vardı. Birden rüzgar esti ve Marshall'ın bardağı şemsiyenin yanından yuvarlandı. "Bardağım nerede?" diye sordu Marshall. "Polis kuralı: önce bardağın durduğu yere bakarız," dedi Chase. Chase şemsiyenin yanına gitti ve kumda ince bir iz gördü. İz iskeleye doğru gidiyordu. Chase o yöne yürüdü. Bardak iskelenin yanında, bir kum yığınının arkasındaydı! Chase bardağı Marshall'a getirdi. Marshall iki bardağa da süt koydu. Sonra ikisi şemsiyenin altında oturdu ve sütlerini mutlu mutlu içti.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "durduğu yere gidip kumdaki izin peşinden gitti"
   - Cümle 0 (plan satırı): «rüzgar esti ve bardak kayboldu | bardağın durduğu yere gidip kumdaki izin peşinden gitti»
   - Açıklama: Plan satırında 'gidip' ve 'gitti' aynı cümlede gereksiz tekrar ediliyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yere gidip kumdaki izin peşinden gitti"
   - Cümle 0 (plan satırı): «rüzgar esti ve bardak kayboldu | bardağın durduğu yere gidip kumdaki izin peşinden gitti»
   - Açıklama: Plan satırında 'gidip' ve 'gitti' aynı cümlede gereksiz tekrar ediliyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden rüzgar esti"
   - Cümle 4: «Birden rüzgar esti ve Marshall'ın bardağı şemsiyenin yanından yuvarlandı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bardağı şemsiyenin yanından yuvarlandı"
   - Cümle 4: «Birden rüzgar esti ve Marshall'ın bardağı şemsiyenin yanından yuvarlandı.»
   - Açıklama: Rüzgarın bardağı yuvarlayıp bulununca bitmesi önemsiz, 'dağıttı, topladı, bitti' türü bir sorun.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Polis kuralı: önce bardağın"
   - Cümle 6: «"Polis kuralı: önce bardağın durduğu yere bakarız," dedi Chase.»
   - Açıklama: 'Polis kuralı' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0008` birebir aynı, `@degisim: kakao -> süt` (tutuyorsan), ardından `@onarim: 8116ee7a30eedfd7096f807d559d17dff59c365c`, sonra gövde.

### Hikâye 6: tohum chase-0010 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Marshall
@tohum: chase-0010
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'başörtüsü', fiil 'aramak', sıfat 'işaretli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Marshall
@plan: koşarken arkadaşının kalesini yıktı | özür dileyip kaleyi birlikte yeniden yaptı
@tohum: chase-0010
@degisim: başörtüsü -> top
Kumsalda Chase topuyla oynuyordu. Marshall da kumdan bir kale yapmıştı. Kalenin kapısı iki beyaz taşla işaretliydi. Chase topunun peşinden koşarken kaleyi görmedi ve ona çarptı. Kalenin tepesi yıkıldı ve beyaz taşlar kuma dağıldı. Marshall üzgün üzgün kaleye baktı. "Özür dilerim, Marshall," dedi Chase. Chase dağılan taşları kumda aradı ve mavi şapkasına topladı. İkisi kaleyi yeniden yaptı ve taşları kapıya dizdi. "Kale yine çok güzel oldu, teşekkürler, Chase!" dedi Marshall. İkisi kaleden biraz uzakta mutlu mutlu top oynadı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iki beyaz taşla işaretliydi"
   - Cümle 3: «Kalenin kapısı iki beyaz taşla işaretliydi.»
   - Açıklama: 'İşaretliydi' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kalenin kapısı iki beyaz taşla işaretliydi.»
   - Açıklama: Kalenin yıkılması ancak 4. cümlede söyleniyor; ilk üç cümle yalnız durumu kuruyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase dağılan taşları kumda aradı ve mavi şapkasına topladı"
   - Cümle 8: «Chase dağılan taşları kumda aradı ve mavi şapkasına topladı.»
   - Açıklama: Çözüm özür dileme, taşları arayıp toplama ve kaleyi yeniden yapma olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0010` birebir aynı, `@degisim: başörtüsü -> top` (tutuyorsan), ardından `@onarim: 70aa0adfa56ef202086e5c7a10754c66a1dd8695`, sonra gövde.
