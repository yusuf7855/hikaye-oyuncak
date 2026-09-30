# Editör görevi (onarım): Chase, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0110 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0110
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kristal', fiil 'tamamlanmak', sıfat 'düşünceli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: arkadaşının kristali çimenlere düştü ve kayboldu | koşmadan yavaşça yürüdü ve kristali buldu
@tohum: chase-0110
@degisim: düşünceli -> üzgün
Chase kamp yerinde Marshall'ın yanına geldi. Marshall çadırın önünde taşlardan küçük bir kule yapıyordu. Ama kulenin en üstündeki kristal çimenlere düşmüş ve kaybolmuştu. Marshall üzgün üzgün yere bakıyordu. "Chase, kristal taşım hiçbir yerde yok," dedi Marshall. Kamp yerinde çimenlerde koşmak yasaktı ve Chase bu kuralı biliyordu. Chase koşmadı ve yavaş yavaş yürüdü. Böylece kristale hiç basmadı. Her yere dikkatle baktı. Sonunda kristali bir çiçeğin dibinde buldu. Chase kristali ağzıyla alıp Marshall'a verdi. Marshall kristali kulenin en üstüne koydu ve kule tamamlandı. Chase çok sevindi, çünkü arkadaşının kristalini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kulenin en üstündeki kristal çimenlere düşmüş ve kaybolmuştu"
   - Cümle 3: «Ama kulenin en üstündeki kristal çimenlere düşmüş ve kaybolmuştu.»
   - Açıklama: Kristalin neden düştüğü hiç söylenmiyor; sorunun sebebi yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bu kuralı biliyordu"
   - Cümle 6: «Kamp yerinde çimenlerde koşmak yasaktı ve Chase bu kuralı biliyordu.»
   - Açıklama: 'Kural' soyut bir kavram ve 3 yaşındaki çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0110` birebir aynı, `@degisim: düşünceli -> üzgün` (tutuyorsan), ardından `@onarim: ca4917f0fc60e0d27cc0604c10b55e6a34c802a5`, sonra gövde.

### Hikâye 2: tohum chase-0113 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0113
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'mücevher', fiil 'çıkarmak', sıfat 'koyu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: rüzgar arkadaşının mama kabını kumla doldurdu | şapkasını çıkarıp ters çevirdi ve kap yaptı
@tohum: chase-0113
@degisim: mücevher -> mama
Kulübelerin önünde rüzgar esiyordu. Chase ile Skye orada oynuyordu. Birden Skye acıktı ama rüzgar onun mama kabını kumla doldurmuştu. Mama torbası kulübenin yanındaydı ama başka kap yoktu. "Chase, mamamı neye koyacağım?" diye sordu Skye. Chase mavi şapkasını çıkardı ve ters çevirdi. Şapka küçük bir kap gibi oldu. Skye koyu kahverengi mamaları şapkanın içine koydu. Sonra mamaları hemen yedi ve kuyruğunu salladı. "Teşekkürler, Chase, karnım doydu!" dedi Skye. Chase bundan sonra rüzgar esince mama kaplarını kulübelerin içine koydu.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase mavi şapkasını çıkardı ve ters çevirdi"
   - Cümle 6: «Chase mavi şapkasını çıkardı ve ters çevirdi.»
   - Açıklama: Çözüm kaptaki kumu boşaltmak yerine sebebi atlayıp şapkayı kap yapıyor.
   - Açıklama: Sorun kabın kumla dolması ama kap boşaltılmıyor; çözüm sebebe doğrudan yönelmiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapka küçük bir kap gibi oldu"
   - Cümle 7: «Şapka küçük bir kap gibi oldu.»
   - Açıklama: Tohum özelliği mavi şapka takmaktır; şapkanın mama kabı yapılması karttaki özelliğin kullanımına uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0113` birebir aynı, `@degisim: mücevher -> mama` (tutuyorsan), ardından `@onarim: 8eefdf148d4f606ef3608f301b17e249737e4fc9`, sonra gövde.

### Hikâye 3: tohum chase-0116 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Rubble
@tohum: chase-0116
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: paylaşmak
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'boya', fiil 'inanmak', sıfat 'sakar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | ev | Rubble
@plan: mama kabı boştu ve bisküvi kutusu kayboldu | kokusunu alıp kutuyu buldu ve paylaştı
@tohum: chase-0116
@degisim: sakar -> boş
Chase kulübesinin önünde Rubble ile oynuyordu. Birden Rubble acıktı ve mama kabına koştu. Kap boştu ve bisküvi kutusu da yerinde yoktu. Kulübeler boyanırken kutu başka bir yere konmuştu. Her yer boya kokuyordu ama Chase havayı dikkatle kokladı. Havada tatlı bir bisküvi kokusu da vardı. Chase burnuyla kulübelerin arkasını gösterdi. Rubble kutunun orada olduğuna inandı ve Chase ile oraya yürüdü. Kutu gerçekten bir kulübenin arkasındaydı. İçinde tek bir büyük bisküvi kalmıştı. Chase bisküviyi ikiye böldü ve yarısını Rubble'a verdi. İkisi bisküvilerini yedi ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Rubble kutunun orada olduğuna inandı"
   - Cümle 8: «Rubble kutunun orada olduğuna inandı ve Chase ile oraya yürüdü.»
   - Açıklama: 'Olduğuna inandı' soyut ve 3 yaşındaki çocuk için ağır bir anlatım.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "İçinde tek bir büyük bisküvi kalmıştı"
   - Cümle 10: «İçinde tek bir büyük bisküvi kalmıştı.»
   - Açıklama: Kutu bulunduktan sonra tek bisküvi kalması ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0116` birebir aynı, `@degisim: sakar -> boş` (tutuyorsan), ardından `@onarim: 9b692c7b63088952d8494e89951ad7ede99cb358`, sonra gövde.

### Hikâye 4: tohum chase-0119 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Marshall
@tohum: chase-0119
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'yüzük', fiil 'kirletmek', sıfat 'incecik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | ev | Marshall
@plan: rüzgar çilek kabını devirdi ve çilekler kayboldu | burnuyla çileklerin kokusunu alıp onları buldu
@tohum: chase-0119
@degisim: yüzük -> pasta
Kulübelerin önünde rüzgar esiyordu. Chase, Marshall için küçük bir pasta hazırlıyordu. Ama rüzgar çilek kabını devirdi ve çilekler her yere dağıldı. Chase etrafa baktı ama hiçbir çileği göremedi. Chase burnunu yere yaklaştırdı ve kokladı. Tatlı çilek kokusu bir kulübenin arkasından geliyordu. Chase oraya gitti ve bütün çilekleri buldu. Chase pastayı kirletmek istemedi ve çileklerin tozunu üfledi. Sonra çilekleri incecik pastanın üstüne dizdi. Tam o sırada Marshall geldi. "Sürpriz, Marshall, bu pasta senin için!" dedi Chase. "Çok güzel olmuş, teşekkürler, Chase!" dedi Marshall.
```

**Hakem bulguları (5):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çilekler her yere dağıldı"
   - Cümle 3: «Ama rüzgar çilek kabını devirdi ve çilekler her yere dağıldı.»
   - Açıklama: Çilekler her yere dağıldı deniyor ama sonra hepsi tek bir kulübenin arkasında bulunuyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase burnunu yere yaklaştırdı"
   - Cümle 5: «Chase burnunu yere yaklaştırdı ve kokladı.»
   - Açıklama: 'Chase' adı art arda cümlelerin başında gereksiz yere tekrarlanıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Chase oraya gitti ve bütün çilekleri buldu"
   - Cümle 7: «Chase oraya gitti ve bütün çilekleri buldu.»
   - Açıklama: Çilekler her yere dağıldı denirken hepsi tek bir kulübenin arkasında bulunuyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çileklerin tozunu üfledi"
   - Cümle 8: «Chase pastayı kirletmek istemedi ve çileklerin tozunu üfledi.»
   - Açıklama: Yere dağılan çilekler yıkanmadan yalnız üflenip yiyeceğe konuyor; taklit edilince sağlıksız bir davranış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çilekleri incecik pastanın üstüne"
   - Cümle 9: «Sonra çilekleri incecik pastanın üstüne dizdi.»
   - Açıklama: 'İncecik' sıfatı pastaya uymuyor ve yanlış yere konmuş.
   - Açıklama: 'İncecik' pasta için uygun ve anlaşılır bir sıfat değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0119` birebir aynı, `@degisim: yüzük -> pasta` (tutuyorsan), ardından `@onarim: fa0e4b80dfdbbd2f91a032b6ede6eefa5cf0a92c`, sonra gövde.

### Hikâye 5: tohum chase-0121 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0121
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'spagetti', fiil 'görünmek', sıfat 'ağır'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalgalar büyük kabuğu suyun altında bırakıyordu | suya girmedi, dalga gidince kabuğu hemen aldı
@tohum: chase-0121
@degisim: spagetti -> kabuk
Rüzgar esiyordu ve dalgalar kumsala geliyordu. Chase kumda büyük, parlak bir kabuk gördü ve onu almak istedi. Ama her dalga gelince kabuk suyun altında kalıyordu. Kumsalda suya girmek yasaktı ve Chase bu kuralı biliyordu. Chase suya girmedi ve kumun kuru yerinde bekledi. Dalga geri gidince kabuk yeniden göründü. Chase hemen kabuğun yanına gitti ve onu ağzıyla aldı. Yeni dalga gelmeden geri koştu. Kabuk biraz ağırdı ama Chase onu sıkıca tuttu. Chase kabuğa uzun uzun baktı ve çok sevindi. Chase bundan sonra kabuk alırken hep dalganın geri gitmesini bekledi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Yeni dalga gelmeden geri koştu"
   - Cümle 8: «Yeni dalga gelmeden geri koştu.»
   - Açıklama: Dalgalar arasında su kenarına koşup nesne kapmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Dalgalar arasında su kenarına koşup geri kaçmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0121` birebir aynı, `@degisim: spagetti -> kabuk` (tutuyorsan), ardından `@onarim: 7e0504023f324e254eeb4b8cc886419bea07731e`, sonra gövde.

### Hikâye 6: tohum chase-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0124
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'erik', fiil 'uzamak', sıfat 'tuzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: torba yırtıldı ve erikleri koyacak bir şey kalmadı | şapkasını tutması için arkadaşından yardım istedi
@tohum: chase-0124
Bir sabah Chase ile Skye parkta piknik yapıyordu. Yanlarında tuzlu bir simit ve bir torba erik vardı. Birden torba yırtıldı ve erikler uzamış otların arasına yuvarlandı. Erikleri koyacak başka bir torba yoktu. Chase hemen mavi şapkasını çıkardı ve ters çevirdi. "Skye, şapkamı tutar mısın?" diye sordu Chase. "Tabii," dedi Skye ve şapkayı sıkıca tuttu. Chase erikleri otların arasından ağzıyla tek tek şapkaya koydu. Sonunda bütün erikler şapkanın içindeydi. İkisi simidi ve erikleri keyifle paylaştı. Chase çok mutlu oldu, çünkü Skye'dan yardım istemiş ve erikleri toplamıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden torba yırtıldı ve erikler"
   - Cümle 3: «Birden torba yırtıldı ve erikler uzamış otların arasına yuvarlandı.»
   - Açıklama: Torbanın neden yırtıldığı hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0124` birebir aynı, ardından `@onarim: 47b2d3626f225a1ce7dafbd4eadc8877866ecbd5`, sonra gövde.

### Hikâye 7: tohum chase-0125 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Marshall
@tohum: chase-0125
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'eşarp', fiil 'dolaşmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Marshall
@plan: rüzgar şapkayı uçurdu ve şapka kayaların arasında kayboldu | arkadaşından yardım istedi ve arkadaşı mavi şapkayı gördü
@tohum: chase-0125
@degisim: eşarp -> kaya
Rüzgar esiyordu ve gökyüzü bulutlarla kapalıydı. Chase ile Marshall karlı dağda dolaşıyordu. Birden rüzgar Chase'in mavi şapkasını uçurdu. Şapka yolun yanındaki kayaların arasına düştü. Chase etrafa baktı ama şapkayı göremedi. "Marshall, şapkam mavi, onu karda arar mısın?" diye sordu Chase. İkisi yan yana yürüdü ve kayaların arasına baktı. Sonunda Marshall beyaz karın üstünde mavi bir şey gördü. "Chase, şapkan burada!" dedi Marshall. Chase şapkasını aldı ve yeniden taktı. İkisi neşeyle yürümeye devam etti. Chase bundan sonra bir şeyini bulamayınca hemen arkadaşından yardım istedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bulamayınca hemen arkadaşından yardım istedi"
   - Cümle 12: «Chase bundan sonra bir şeyini bulamayınca hemen arkadaşından yardım istedi.»
   - Açıklama: 'Bundan sonra' ile süreklilik anlatılırken 'isterdi' olmalı; kip uyumsuz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0125` birebir aynı, `@degisim: eşarp -> kaya` (tutuyorsan), ardından `@onarim: f361a706cf43b3912f197b4cfde39d17a9afa349`, sonra gövde.

### Hikâye 8: tohum chase-0136 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0136
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'basamak', fiil 'yıkamak', sıfat 'pembe'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalgalar basamakları yıkamıştı ve hepsi kaygandı | kaygan yere basmadı ve kurumasını bekledi
@tohum: chase-0136
Chase bir sabah erkenden kumsala geldi. Gökyüzünde pembe bulutlar vardı ve Chase onlara iskelenin üstünden bakmak istedi. Ama dalgalar basamakları yıkamıştı ve hepsi çok kaygandı. Bir kural vardı: kaygan yere basmak yoktu. Chase kumun üstüne oturdu ve bekledi. Biraz sonra rüzgar esti ve her yer kurudu. Chase basamakları yavaş yavaş çıktı ve iskelenin ortasına yürüdü. Orada durdu ve pembe bulutlara uzun uzun baktı. Chase çok mutluydu, çünkü bulutlara ilk kez iskelenin üstünden bakmıştı.
```

**Hakem bulguları (3):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Biraz sonra rüzgar esti ve her yer kurudu"
   - Cümle 6: «Biraz sonra rüzgar esti ve her yer kurudu.»
   - Açıklama: Kaygan basamakları Chase değil rüzgar çözüyor; Chase yalnız oturup bekliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "rüzgar esti ve her yer kurudu"
   - Cümle 6: «Biraz sonra rüzgar esti ve her yer kurudu.»
   - Açıklama: Dalgaların ıslattığı basamakların bir anda kuruması çözümü sebepsizce getiriyor.
   - Açıklama: Dalgaların ıslattığı basamakların bir rüzgarla hemen kuruması çözümü sebepsizce ve inandırıcı olmayan biçimde getiriyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "iskelenin ortasına yürüdü"
   - Cümle 7: «Chase basamakları yavaş yavaş çıktı ve iskelenin ortasına yürüdü.»
   - Açıklama: Chase sabah erkenden tek başına ıslak basamaklardan iskelenin ortasına yürüyor; çocuk taklit ederse derin su kenarında yalnız kalır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0136` birebir aynı, ardından `@onarim: 6a605d03b0a66f35a255fdf8e228046078dd2797`, sonra gövde.

### Hikâye 9: tohum chase-0138 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0138
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'koltuk', fiil 'saklamak', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: kütüklerin çoğu yağmurdan ıslanmıştı | kütükleri kokladı ve kuru bir kütük buldu
@tohum: chase-0138
@degisim: ilginç -> yüksek
Ormandaki kamp yerinde yağmur yeni durmuştu. Chase kendine kütükten bir koltuk yapmak istiyordu. Ama kütüklerin çoğu yağmurdan ıslanmıştı. Chase burnuyla kütükleri tek tek kokladı. Islak kütükler toprak gibi kokuyordu. Sonra büyük bir ağacın altında bir kütük buldu. Ağacın dalları onu yağmurdan saklamıştı. Bu kütük kuru odun kokuyordu. Kütüğün arkası yüksekti ve bir koltuğa benziyordu. Chase ağacın altındaki kuru yaprakları topladı. Yaprakları kütüğün üstüne yumuşak bir yatak gibi serdi. Sonra yeni koltuğuna rahatça oturdu. Chase çok mutluydu, çünkü kendi koltuğunu kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu yağmurdan saklamıştı"
   - Cümle 7: «Ağacın dalları onu yağmurdan saklamıştı.»
   - Açıklama: Dallar kütüğü saklamaz; 'korumuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0138` birebir aynı, `@degisim: ilginç -> yüksek` (tutuyorsan), ardından `@onarim: 9ac0701e137c01e009dd4777c5b0325485fa7551`, sonra gövde.

### Hikâye 10: tohum chase-0143 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0143
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'bardak', fiil 'doldurmak', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: koşunca bardaktaki su döküldü | bardağı yeniden doldurup yavaş yürümeyi söyledi
@tohum: chase-0143
@degisim: utangaç -> üzgün
Kulübelerin önünde Chase ile Skye küçük bir çiçeğe su taşıyordu. Ama Skye koştuğu için bardaktaki su hep dökülüyordu. "Çiçeğe hiç su kalmıyor," dedi Skye üzgün bir sesle. Chase bardağı musluktan yeniden doldurdu ve Skye'a verdi. "Skye, kural şu: su taşırken yavaş yürü," dedi Chase. Skye bardağı dikkatle tuttu ve yavaş yavaş yürüdü. Chase de onun yanında yürüdü. Bardaktaki su hiç dökülmedi. Skye suyu çiçeğe döktü. Skye bundan sonra su taşırken hiç koşmadı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "su taşırken yavaş yürü"
   - Cümle 5: «"Skye, kural şu: su taşırken yavaş yürü," dedi Chase.»
   - Açıklama: Özellikler alanında Chase kurallara uyar; burada kendisi Skye'a kural koyup uyguluyor, özellik karttaki gibi kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0143` birebir aynı, `@degisim: utangaç -> üzgün` (tutuyorsan), ardından `@onarim: b3544eb15abfa3f173574f3d01e9cdc1a76034f9`, sonra gövde.

### Hikâye 11: tohum chase-0150 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0150
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'testi', fiil 'büyümek', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: çiçeklere su götürmek istedi ama kaygan testi kaydı | testiyi ters şapkanın içine koyup taşıdı
@tohum: chase-0150
Parkta hava sisliydi. Chase çiçeklere bakma oyunu oynuyordu ve suyla dolu bir testi taşımak istiyordu. Ama testi ıslak ve kaygandı, Chase onu ağzıyla tutamıyordu. Parktaki küçük çiçeklerin toprağı çok kuruydu. Chase çiçekler büyüsün diye onlara su götürmek istiyordu. Chase biraz düşündü. Sonra mavi şapkasını çıkardı ve yere ters koydu. Testiyi burnuyla şapkanın içine itti. Şapkanın kenarını ağzıyla tuttu ve dikkatle yürüdü. Testi bu kez hiç kaymadı. Chase çiçeklerin yanına varınca testiyi yavaşça eğdi. Su aktı ve toprak ıslandı. Chase bundan sonra kaygan şeyleri hep böyle taşıdı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çiçeklere bakma oyunu oynuyordu"
   - Cümle 2: «Chase çiçeklere bakma oyunu oynuyordu ve suyla dolu bir testi taşımak istiyordu.»
   - Açıklama: Çiçeklere bakmak (sulamak) bir oyun değil; 'bakma' kelimesi hem 'görmek' hem 'ilgilenmek' anlamına gelerek yanlış ve belirsiz kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0150` birebir aynı, ardından `@onarim: 7db53b3feb75548c7b40ca76f853f37158d9469e`, sonra gövde.

### Hikâye 12: tohum chase-0156 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0156
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Rubble
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'sakız', fiil 'tekrarlamak', sıfat 'uyanık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: ikisi aynı anda attı ve kozalaklar havada çarpıştı | sırayla atmayı önerdi ve kozalaklar şapkaya girdi
@tohum: chase-0156
@degisim: sakız -> kozalak
Chase ile Rubble sabah erkenden uyanıktı ve kamp yerine oynamaya geldi. İkisi kozalakları, Chase'in kütüğe koyduğu mavi şapkaya atıyordu. Ama hep aynı anda atıyorlardı ve kozalaklar havada birbirine çarpıyordu. "Hiçbiri şapkaya girmedi!" dedi Rubble. Chase biraz düşündü. "Sırayla atalım, önce sen, Rubble," dedi Chase. Rubble attı ve kozalak şapkanın içine düştü. Sonra Chase attı ve onun kozalağı da içeri girdi. İkisi oyunu sırayla birkaç kez tekrarladı. Az sonra şapka doldu. "Kamp yerinde sırayla oynamak çok eğlenceli, Chase!" dedi Rubble.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sabah erkenden uyanıktı"
   - Cümle 1: «Chase ile Rubble sabah erkenden uyanıktı ve kamp yerine oynamaya geldi.»
   - Açıklama: 'Erkenden' zarfı durum bildiren 'uyanıktı' ile uyuşmuyor; 'erkenden uyanmıştı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kozalaklar havada birbirine çarpıyordu"
   - Cümle 3: «Ama hep aynı anda atıyorlardı ve kozalaklar havada birbirine çarpıyordu.»
   - Açıklama: Aynı anda atılan kozalakların her seferinde havada çarpışıp hiçbirinin girmemesi akla yatkın değil.
   - Açıklama: Aynı anda atılan kozalakların hep havada çarpışması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0156` birebir aynı, `@degisim: sakız -> kozalak` (tutuyorsan), ardından `@onarim: db8c9149f7b32652869397637fb5c44953a7343c`, sonra gövde.
