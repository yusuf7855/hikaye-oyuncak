# Editör görevi (onarım): Chase, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0033 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0033
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: paylaşmak
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kaktüs', fiil 'sallamak', sıfat 'güneşli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: çocuğun kızağı kırılmıştı ve tek kızak vardı | kızağını çocukla paylaştı ve birlikte kaydılar
@tohum: chase-0033
@degisim: kaktüs -> kızak
Bir sabah karlı dağ çok güneşliydi. Chase ile Ryder kaymak için küçük bir tepeye çıktı. Ama yalnız Chase'in kızağı vardı, çünkü Ryder'ın kızağı kırılmıştı. Ryder üzgün üzgün Chase'e baktı. "Ryder, gel, bu kızak ikimizin!" dedi Chase. "İkimiz sığar mıyız?" diye sordu Ryder. Chase kuyruğunu salladı ve öne oturdu. Ryder de arkasına oturdu. Chase kuralı biliyordu: kayarken herkes sıkıca tutmalıydı. Chase kızağın ucunu, Ryder de iki kenarını tuttu. Kızak karın üstünde yavaşça aşağı indi. Sonra ikisi aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karlı dağ çok güneşliydi"
   - Cümle 1: «Bir sabah karlı dağ çok güneşliydi.»
   - Açıklama: 'Güneşli' sıfatı dağa değil havaya uyar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0033` birebir aynı, `@degisim: kaktüs -> kızak` (tutuyorsan), ardından `@onarim: f53cb2d1f2be47f1b425cef55144f223c4663075`, sonra gövde.

### Hikâye 2: tohum chase-0034 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0034
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'mürekkep', fiil 'çalışmak', sıfat 'dikkatli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: rüzgar esince kağıt hep havaya kalkıyordu | kağıdın köşelerine küçük taşlar koydu
@tohum: chase-0034
Ağaçlarda kuşlar ötüyordu. Chase parkta ilk kez mavi mürekkeple pati resmi yapmayı deniyordu. Ama rüzgar esince beyaz kağıt hep havaya kalkıyordu. Chase kuralı biliyordu: rüzgarlı günde kağıdın üstüne taş konurdu. Chase yerden küçük taşlar topladı. Taşları kağıdın dört köşesine koydu. Artık kağıt rüzgarda hiç kıpırdamadı. Chase patisini dikkatli bir şekilde mürekkebe batırdı. Sonra kağıda düz basmaya çalıştı. Kağıtta çok güzel bir pati izi çıktı. Chase çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kuralı biliyordu"
   - Cümle 4: «Chase kuralı biliyordu: rüzgarlı günde kağıdın üstüne taş konurdu.»
   - Açıklama: 'Kural' ve genel geçer 'konurdu' anlatımı soyut, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Kural' soyut bir kavram; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0034` birebir aynı, ardından `@onarim: ef8134b1ff573f869e8c679674855e602fbb763b`, sonra gövde.

### Hikâye 3: tohum chase-0035 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0035
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kravat', fiil 'bindirmek', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | -
@plan: kamyon ağacın altındaydı ve boya ıslak kaldı | kamyonu güneşe itti ve kurumasını bekledi
@tohum: chase-0035
@degisim: pürüzsüz -> düz
Bir sabah Chase parkta düz bir kağıttan kravat yaptı. Kravatı maviye boyadı ve yanındaki oyuncak kamyona bindirdi. Ama kamyon ağacın altındaydı ve boya ıslak kaldı. Chase kravatı takıp parkta gezmek istiyordu. Chase kuralı biliyordu: ıslak boyaya dokunulmazdı. Kamyonu burnuyla itti ve kravatı güneşe taşıdı. Sonra kamyonun yanına oturdu ve bekledi. Güneş kravatı ısıttı ve boya kısa sürede kurudu. Chase patisiyle kravatın ucuna hafifçe dokundu. Boya artık patisine yapışmadı. Chase mavi kravatını taktı ve parkta mutlu mutlu gezdi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yanındaki oyuncak kamyona bindirdi"
   - Cümle 2: «Kravatı maviye boyadı ve yanındaki oyuncak kamyona bindirdi.»
   - Açıklama: 'Bindirmek' kravat gibi bir eşya için uygun değil; 'kamyona koydu' olmalı.
   - Açıklama: Kravat bir yolcu değildir; 'bindirmek' yerine 'koydu' ya da 'yükledi' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kamyon ağacın altındaydı ve boya ıslak kaldı"
   - Cümle 3: «Ama kamyon ağacın altındaydı ve boya ıslak kaldı.»
   - Açıklama: Boya yeni sürüldüğü için zaten ıslaktır; ağacın altında olmak sorunun akla yatkın bir sebebi değil ve sorun zorlama kalıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kuralı biliyordu: ıslak boyaya dokunulmazdı"
   - Cümle 5: «Chase kuralı biliyordu: ıslak boyaya dokunulmazdı.»
   - Açıklama: Tohumdaki kural özelliği sorunu çözmüyor; çözüm güneşte kurutmak, kural yalnız süs olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0035` birebir aynı, `@degisim: pürüzsüz -> düz` (tutuyorsan), ardından `@onarim: 178b9c341eaa51e8d47b17b7fd0182246714f95e`, sonra gövde.

### Hikâye 4: tohum chase-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Ryder
@tohum: chase-0042
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'tuz', fiil 'bitirmek', sıfat 'bomboş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Ryder
@plan: kardan köpeğin burnu için havuç yolda düşmüştü | burnuyla havucun kokusunu alıp karın altından çıkardı
@tohum: chase-0042
@degisim: tuz -> havuç
Karlı dağda serin bir rüzgar esiyordu. Chase ile Ryder ilk karı kutlamak için kardan köpek yapıyordu. Ama Ryder'ın çantası bomboştu, çünkü havuç yolda düşmüştü. "Burnu olmadan kardan köpeği bitiremeyiz," dedi Ryder. Chase burnunu kara yaklaştırdı ve havucun kokusunu aldı. Sonra az ileride karı patileriyle kazdı. Turuncu havuç karın altından çıktı! Chase onu ağzıyla alıp Ryder'a getirdi. Ryder havucu burun olarak kardan köpeğin yüzüne taktı. Kardan köpek artık bitmişti. İkisi yan yana durup güldü. "Teşekkürler, Chase, bu çok güzel bir kutlama oldu!" dedi Ryder.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ilk karı kutlamak için"
   - Cümle 2: «Chase ile Ryder ilk karı kutlamak için kardan köpek yapıyordu.»
   - Açıklama: 'İlk karı kutlamak' soyut bir anlatım; 3 yaşındaki çocuk için anlaşılır değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0042` birebir aynı, `@degisim: tuz -> havuç` (tutuyorsan), ardından `@onarim: 12013b0f5c177bcb0b01062acb6d76c6a775d293`, sonra gövde.

### Hikâye 5: tohum chase-0044 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Skye
@tohum: chase-0044
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'sünger', fiil 'aydınlanmak', sıfat 'eğlenceli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Skye
@plan: çadırda resmin üstüne su damladı | lambayı yakıp ıslak süngeri buldu
@tohum: chase-0044
Chase, Skye ile çadırda eğlenceli resimler yapıyordu. Birden çadırın tepesinden tıp tıp diye bir ses geldi. Sonra Skye'ın resminin üstüne bir damla su düştü. "Bu su nereden geliyor?" diye sordu Skye. Ama çadırın tepesi karanlıktı ve orası görünmüyordu. Chase kuralı biliyordu: çadırda bir yere tırmanılmazdı. Chase lambayı yaktı ve çadır aydınlandı. Tepedeki ipte ıslak, sarı bir sünger vardı. Su damla damla ondan düşüyordu. "Bu benim, kurusun diye oraya koymuştum!" dedi Skye ve güldü. Chase onu ipten aldı ve dışarı çıkardı. Sonra ikisi resim yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kuralı biliyordu: çadırda bir yere tırmanılmazdı."
   - Cümle 6: «Chase kuralı biliyordu: çadırda bir yere tırmanılmazdı.»
   - Açıklama: Önceden anlatılmamış soyut bir 'kural' ve edilgen 'tırmanılmazdı' yapısı küçük çocuğa uygun değil.
   - Açıklama: Soyut 'kural' kavramı ve edilgen 'tırmanılmazdı' 3 yaşındaki çocuk için ağır.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Chase onu ipten aldı"
   - Cümle 11: «Chase onu ipten aldı ve dışarı çıkardı.»
   - Açıklama: Önceki cümlenin öznesi Skye olduğu için 'onu' zamirinin süngeri gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0044` birebir aynı, ardından `@onarim: 4ac1b1b2a0e9de3f3dd9e89a1d7d30b26c553507`, sonra gövde.

### Hikâye 6: tohum chase-0045 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0045
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Marshall
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'kolye', fiil 'şakımak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: rüzgar resmi çadırın üstüne attı | şapkasıyla arkadaşını çağırdı ve dalla resmi itti
@tohum: chase-0045
@degisim: şakımak -> ötmek
Bir sabah kamp yerinde kuşlar ötüyordu. Chase çadırın önünde kremalı bir kek yiyor ve kolye resmine bakıyordu. Birden rüzgar esti ve resim çadırın üstüne uçtu. Chase zıpladı ama oraya yetişemedi. Marshall uzakta, bir ağacın altında oturuyordu. Chase mavi şapkasını çıkardı ve havada salladı. Marshall onu gördü ve hemen koşarak geldi. Chase patisiyle çadırın üstünü gösterdi. Marshall ağacın altından uzun bir dal getirdi ve Chase'e verdi. Chase dalla resmi yavaşça itti. Resim kaydı ve aşağı düştü. Chase resmi yerden aldı. Chase kekinin yarısını Marshall'a verdi. Chase çok mutlu oldu, çünkü resmini geri almıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kolye resmine bakıyordu"
   - Cümle 2: «Chase çadırın önünde kremalı bir kek yiyor ve kolye resmine bakıyordu.»
   - Açıklama: 'Kolye resmi' anlamı belirsiz ve yerinde olmayan bir tamlama.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Chase mavi şapkasını çıkardı ve havada salladı"
   - Cümle 6: «Chase mavi şapkasını çıkardı ve havada salladı.»
   - Açıklama: Çözüm şapka sallamak, çatıyı göstermek, dal getirtmek ve itmek olarak ikiden fazla adıma yayılıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase resmi yerden aldı"
   - Cümle 12: «Chase resmi yerden aldı.»
   - Açıklama: Art arda cümlelerde 'Chase' adı gereksiz yere tekrarlanıyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase kekinin yarısını Marshall'a verdi"
   - Cümle 13: «Chase kekinin yarısını Marshall'a verdi.»
   - Açıklama: Art arda üç cümle 'Chase' ile başlıyor; gereksiz ad tekrarı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0045` birebir aynı, `@degisim: şakımak -> ötmek` (tutuyorsan), ardından `@onarim: 2680f711b0c954d2c0a630804a3c456b04d2f3df`, sonra gövde.

### Hikâye 7: tohum chase-0046 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Rubble
@tohum: chase-0046
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Rubble
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'şerit', fiil 'saymak', sıfat 'cesur'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | park | Rubble
@plan: rüzgar bitiş yerindeki şeridi uçurdu | burnuyla kokladı ve şeridi çalının dibinde buldu
@tohum: chase-0046
@degisim: cesur -> hızlı
Parkta hafif bir rüzgar esiyordu. Chase ile Rubble koşu yarışı için ağaçlara bir şerit bağlamıştı. Ama rüzgar birden güçlü esti ve şeridi çalılara uçurdu. "Şerit olmadan bitiş yeri olmaz," dedi Rubble. Chase burnuyla kokladı ve şeridi büyük bir çalının dibinde buldu. Onu dişleriyle alıp Rubble'a getirdi. İkisi şeridi bu kez sıkı sıkı bağladı. "Şimdi sen say, Rubble," dedi Chase. "Bir, iki, üç!" diye saydı Rubble. İki köpek hızlı hızlı koşup bitiş yerine vardı. Rubble güldü ve "Bu yarış çok eğlenceliydi, Chase!" dedi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase burnuyla kokladı ve şeridi"
   - Cümle 5: «Chase burnuyla kokladı ve şeridi büyük bir çalının dibinde buldu.»
   - Açıklama: Koklamak zaten burunla yapılır; 'burnuyla' gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0046` birebir aynı, `@degisim: cesur -> hızlı` (tutuyorsan), ardından `@onarim: d78c32c45e642fcbdb13ceee885cb7bcf772b22b`, sonra gövde.

### Hikâye 8: tohum chase-0050 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0050
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'keman', fiil 'silmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: arkadaşının kemanı çantadan düşüp kayboldu | çantayı kokladı ve kokuyla kemanı buldu
@tohum: chase-0050
@degisim: güvenli -> temiz
Chase kamp yerinde Ryder ile oynuyordu. Birden Ryder çantasına baktı ve üzüldü. "Chase, kemanım yok, çantadan düşmüş," dedi Ryder. Chase kemanın nerede olduğunu çok merak etti. Önce boş çantayı dikkatle kokladı. Sonra aynı kokuyu burnuyla yerde aradı. Bir çalının dibinde durdu. Keman orada, çamurun içinde duruyordu. "Ryder, kemanını buldum!" diye seslendi Chase. Ryder koşarak geldi ve kemanı aldı. Çamuru eliyle dikkatle sildi. Keman yine temiz oldu. "Teşekkürler, Chase, burnun çok iyi koku alıyor!" dedi Ryder. Sonra Ryder kemanı çaldı, Chase de mutlu mutlu dinledi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kemanım yok, çantadan düşmüş"
   - Cümle 3: «"Chase, kemanım yok, çantadan düşmüş," dedi Ryder.»
   - Açıklama: Kemanın çantadan neden düştüğü söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0050` birebir aynı, `@degisim: güvenli -> temiz` (tutuyorsan), ardından `@onarim: 7c4c9651501180096144eaaa870eec606865a357`, sonra gövde.

### Hikâye 9: tohum chase-0051 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0051
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'kumaş', fiil 'kaydetmek', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: bazı kabukların içinde minik canlılar vardı | canlıları bırakıp yalnız boş kabukları topladı
@tohum: chase-0051
@degisim: kaydetmek -> yaymak
Kumsalda dalgalar yavaş yavaş geliyordu. Chase kumaş örtüsünü yaydı ve hemen yanında renkli kabuklar gördü. Onları toplamak istedi ama bazı kabukların içinde minik canlılar vardı. Chase kurallara uyan bir polis köpeğiydi ve canlıları toplamadı. Chase her kabuğun içine dikkatle baktı. İçinde canlı olanları suyun kenarına yavaşça geri bıraktı. Boş kabukları ıslak, yapışkan kumdan tek tek çıkardı. Sonra kabuklarla örtünün üstünde büyük bir yıldız yaptı. Chase yıldızına bakıp mutlu mutlu kuyruğunu salladı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "içinde minik canlılar vardı"
   - Cümle 3: «Onları toplamak istedi ama bazı kabukların içinde minik canlılar vardı.»
   - Açıklama: 'Canlılar' soyut bir ad; 3 yaşındaki çocuk 'minik hayvanlar' der.
   - Açıklama: 'Canlılar' soyut bir üst kavram, 3 yaşındaki çocuk için somut hayvan adı gerekir.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "bazı kabukların içinde minik canlılar vardı"
   - Cümle 3: «Onları toplamak istedi ama bazı kabukların içinde minik canlılar vardı.»
   - Açıklama: Çoğul minik canlılar arka planda kalmıyor, sorunun ve olayın parçası oluyor.
   - Açıklama: Çoğul canlılar arka planda kalmıyor, sorunun merkezine girerek olaya katılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uyan bir polis köpeğiydi ve canlıları toplamadı"
   - Cümle 4: «Chase kurallara uyan bir polis köpeğiydi ve canlıları toplamadı.»
   - Açıklama: Sonuç kabuklara bakmadan önce söyleniyor ve canlıların varlığı bakılmadan biliniyor; olaylar sırayla birbirinden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0051` birebir aynı, `@degisim: kaydetmek -> yaymak` (tutuyorsan), ardından `@onarim: 4c04a2dd3ccd33969f5d829f7da126f812707a17`, sonra gövde.

### Hikâye 10: tohum chase-0053 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0053
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Skye
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'zincir', fiil 'kucaklamak', sıfat 'sabırlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: rüzgar esti ve kardan köpeğin havuç burnu karda kayboldu | karı kokladı ve havucu bulup yerine taktı
@tohum: chase-0053
Karlı dağda hava güneşliydi. Chase, Skye için kardan bir köpek ve kağıttan bir zincir yapmıştı. Ama rüzgar esti ve kardan köpeğin havuç burnu karın içine düştü. Skye biraz ileride gözlerini kapatmış, sabırlı bir şekilde bekliyordu. Chase burnunu karın üstüne eğdi ve dikkatle kokladı. Havucu küçük bir çukurun içinde buldu. Onu çıkardı ve eski yerine taktı. "Şimdi gözlerini açabilirsin," dedi Chase. Skye gözlerini açtı ve kardan köpeği gördü. "Bu benim için mi?" diye sordu Skye. Chase gülümsedi ve zinciri Skye'ın boynuna taktı. Skye, Chase'i sıkıca kucakladı. Chase çok sevindi, çünkü Skye sürprizi çok beğenmişti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kardan köpeğin havuç burnu karın içine düştü"
   - Cümle 3: «Ama rüzgar esti ve kardan köpeğin havuç burnu karın içine düştü.»
   - Açıklama: Havucun düşüp hemen yerine takılması önemsiz, hemen biten bir olay.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve kardan köpeğin havuç burnu karın içine düştü"
   - Cümle 3: «Ama rüzgar esti ve kardan köpeğin havuç burnu karın içine düştü.»
   - Açıklama: Havucun hemen yanına düşüp kokuyla bir anda bulunması önemsiz, gerilimsiz bir sorun.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "zinciri Skye'ın boynuna taktı"
   - Cümle 11: «Chase gülümsedi ve zinciri Skye'ın boynuna taktı.»
   - Açıklama: Birinin boynuna zincir takmak çocuğun taklit edebileceği riskli bir davranış olabilir.
   - Açıklama: Birinin boynuna zincir takmak çocuğun taklit edebileceği boğulma riski taşıyan bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0053` birebir aynı, ardından `@onarim: 5f75f82ddea272c5644bbf5f272f39b1194d0556`, sonra gövde.

### Hikâye 11: tohum chase-0056 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0056
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'alet', fiil 'yakalamak', sıfat 'renkli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: uçurtmanın ipi koptu ve uçurtma kumsala uçtu | şapkasını gözlerine indirdi ve uçurtmayı buldu
@tohum: chase-0056
@degisim: yakalamak -> dönmek
Kumsalda güçlü bir rüzgar esiyordu. Chase iskelenin yanında renkli uçurtmasını uçuruyordu. Birden ipi koptu ve uçurtma kumsala uçtu. Chase uçurtmasını aradı ama bulamadı. Sonra kumsaldan garip bir ses duydu. Chase bu sesi çok merak etti. Ama güneş çok parlaktı ve Chase kumsalı iyi göremedi. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi her yeri rahatça gördü. Uçurtma bir taşa takılmıştı ve rüzgarda ses çıkarıyordu. Garip sesi yapan alet onun uçurtmasıydı. Chase uçurtmasını ağzıyla aldı ve iskeleye geri döndü. Chase çok sevindi, çünkü kaybolan uçurtmasını bulmuştu.
```

**Hakem bulguları (5):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sonra kumsaldan garip bir ses duydu"
   - Cümle 5: «Sonra kumsaldan garip bir ses duydu.»
   - Açıklama: Kayıp uçurtmanın yanına ayrı bir gizemli ses sorunu ve sonra güneş parlaklığı sorunu ekleniyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama güneş çok parlaktı ve Chase kumsalı iyi göremedi"
   - Cümle 7: «Ama güneş çok parlaktı ve Chase kumsalı iyi göremedi.»
   - Açıklama: Kopan ip ve kaybolan uçurtma sorununa ikinci bir sorun olarak güneşin göz kamaştırması ekleniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ama güneş çok parlaktı ve Chase kumsalı iyi göremedi"
   - Cümle 7: «Ama güneş çok parlaktı ve Chase kumsalı iyi göremedi.»
   - Açıklama: Çözüm ipin kopmasına değil sonradan eklenen güneş parlaklığına yöneliyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Garip sesi yapan alet onun uçurtmasıydı"
   - Cümle 11: «Garip sesi yapan alet onun uçurtmasıydı.»
   - Açıklama: Uçurtma alet değildir; kelime yanlış anlamda kullanılmış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Garip sesi yapan alet"
   - Cümle 11: «Garip sesi yapan alet onun uçurtmasıydı.»
   - Açıklama: Uçurtma bir alet değil; kelime yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0056` birebir aynı, `@degisim: yakalamak -> dönmek` (tutuyorsan), ardından `@onarim: eb96ef8b51ea2f7621d146d4ad3e2d2a42720002`, sonra gövde.

### Hikâye 12: tohum chase-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Skye
@tohum: chase-0057
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'peçete', fiil 'ulaşmak', sıfat 'faydalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Skye
@plan: kar taneleri yere düşünce karın içinde kayboluyordu | şapkasını çıkarıp karın altına tuttu
@tohum: chase-0057
@degisim: peçete -> yıldız
Karlı dağda yavaş yavaş kar yağıyordu. Chase ile Skye yıldıza benzeyen küçük kar tanelerini fark etti. Ama taneler yere ulaşınca beyaz karın içinde kayboluyordu. "Chase, bir tanesine yakından bakmak istiyorum," dedi Skye. Chase biraz düşündü. Sonra mavi şapkasını çıkardı ve gökyüzüne doğru tuttu. Birkaç tane şapkanın üstüne kondu. Beyaz taneler orada kaybolmadı ve kolayca göründü. Skye yaklaştı ve altı köşeli minik bir yıldız gördü. Sevinçle kuyruğunu salladı. "Şapkan çok faydalı oldu, Chase, teşekkürler!" dedi Skye.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkasını çıkarıp karın altına tuttu"
   - Cümle 0 (plan satırı): «kar taneleri yere düşünce karın içinde kayboluyordu | şapkasını çıkarıp karın altına tuttu»
   - Açıklama: 'Karın altına' yanlış anlamda; gövdede şapka yağan karın altına değil gökyüzüne doğru tutuluyor ve 'karın' belirsiz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Birkaç tane şapkanın üstüne kondu"
   - Cümle 7: «Birkaç tane şapkanın üstüne kondu.»
   - Açıklama: 'Birkaç tane' miktar belirteci gibi okunuyor, cümle 'birkaç şapkanın üstüne' anlamına kayıyor; 'Birkaç kar tanesi şapkanın üstüne kondu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şapkan çok faydalı oldu"
   - Cümle 11: «"Şapkan çok faydalı oldu, Chase, teşekkürler!" dedi Skye.»
   - Açıklama: 'Faydalı' soyut bir kelime; 3 yaşındaki çocuk için 'işe yaradı' gibi somut bir ifade gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0057` birebir aynı, `@degisim: peçete -> yıldız` (tutuyorsan), ardından `@onarim: 3f3b95dab7873a09f9dfcbb824c11a8d0a4dbb42`, sonra gövde.
