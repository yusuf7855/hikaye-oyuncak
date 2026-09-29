# Editör görevi (onarım): Chase, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0040 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0040
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'vanilya', fiil 'yayılmak', sıfat 'narin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: zıplarken kurabiyeleri düşürdü ve kırdı | özür dileyip parçaları beraber yemeyi istedi
@tohum: chase-0040
@degisim: narin -> ince
Bir sabah Chase karlı dağda sevinçle zıplıyordu. Rubble bir taşın üstüne vanilyalı kurabiyeler koymuştu. Chase zıplarken kuyruğu ince kurabiyeleri taştan düşürdü. Kurabiyeler kırıldı ve parçaları kara yayıldı. Rubble kırık kurabiyelere üzgün üzgün baktı. Chase kurallara uyardı ve hemen özür diledi. "Özür dilerim, Rubble, parçaları beraber yiyelim mi?" diye sordu Chase. Rubble bir parçayı ağzına attı ve güldü. İki arkadaş parçaları birlikte yedi. Chase çok sevindi, çünkü Rubble ona hiç kızmamıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kurallara uyardı ve hemen özür diledi"
   - Cümle 6: «Chase kurallara uyardı ve hemen özür diledi.»
   - Açıklama: Kurallara uymak özür dilemekle ilgisiz; ifade bu bağlamda yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 6: «Chase kurallara uyardı ve hemen özür diledi.»
   - Açıklama: 'Kurallara uymak' olaydan çıkmayan soyut bir kavram.
   - Açıklama: 'Kurallara uymak' soyut ve olaya bağlı olmayan bir kavram.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase kurallara uyardı ve hemen özür diledi"
   - Cümle 6: «Chase kurallara uyardı ve hemen özür diledi.»
   - Açıklama: Kurallara uyma özelliği özür dilemeyle ilgisiz, işlevsiz bir ayrıntı olarak araya sokulmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0040` birebir aynı, `@degisim: narin -> ince` (tutuyorsan), ardından `@onarim: db1a9f47d7441fcdb3acb81f9d02d90fbfa511dd`, sonra gövde.

### Hikâye 2: tohum chase-0041 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0041
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'patates', fiil 'köpürmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: kelebekler geldi ama önce kasesini yıkaması gerekti | kurallara uydu ve kasesini çabucak yıkadı
@tohum: chase-0041
Kulübelerin önünde güneş parlıyordu. Chase patates yemeğini yedi ve kulenin yanında rengarenk kelebekler gördü. Onları saymak istedi ama önce kasesini yıkaması gerekiyordu. Kural buydu ve Chase kurallara hep uyardı. Kaseye sabunlu su doldurdu ve su hemen köpürdü. Chase çabucak yıkadı ve onu yerine koydu. Her şey temiz ve düzenliydi. Sonra Chase başını kaldırıp kuleye baktı. Kelebekler yine oradaydı! Chase onları bir, iki, üç diye tek tek saydı. Chase çok sevindi, çünkü hem işini bitirmiş hem de kelebekleri görmüştü.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "önce kasesini yıkaması gerekiyordu"
   - Cümle 3: «Onları saymak istedi ama önce kasesini yıkaması gerekiyordu.»
   - Açıklama: Kase yıkamak kelebekleri saymadan önce yapılan sıradan bir iş; gerçek bir sorun kurulmuyor ve kelebekler zaten yerinde kalıyor.
   - Açıklama: Kase yıkamak gerçek bir sorun değil; kelebeklerin gideceğine dair bir tehlike de kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara hep uyardı"
   - Cümle 4: «Kural buydu ve Chase kurallara hep uyardı.»
   - Açıklama: 'Kurallara uymak' soyut bir kavram ve 'uyardı' belirsiz okunuyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Chase çabucak yıkadı ve onu yerine koydu"
   - Cümle 6: «Chase çabucak yıkadı ve onu yerine koydu.»
   - Açıklama: Nesne düşmüş; önceki cümlenin öznesi 'su' olduğu için 'onu' zamirinin kaseyi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0041` birebir aynı, ardından `@onarim: ad4d5306a1dc1f8869be4d83aa9b5a3bf2bc7910`, sonra gövde.

### Hikâye 3: tohum chase-0044 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ağaçların arasından bilinmeyen bir ses geldi | kurallara uydu ve arkadaşıyla gidip süngeri buldu
@tohum: chase-0044
Chase, Skye ile kamp yerinde eğlenceli bir top oyunu oynuyordu. Birden ağaçların arasından tıp tıp diye bir ses geldi. Chase bu sesi çok merak etti. Ama Chase kurallara uyardı ve yalnız gitmedi. "Skye, benimle gelir misin?" diye sordu Chase. "Tabii," dedi Skye. İkisi sesin geldiği yere yürüdü. Güneş bulutların arasından çıktı ve orman aydınlandı. Alçak bir dalda sarı, ıslak bir sünger vardı. Ondan yere damla damla su düşüyordu. "Bu benim, sabah kurusun diye oraya koymuştum!" dedi Skye ve güldü. Chase süngeri daldan alıp Skye'a verdi. Sonra ikisi top oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağaçların arasından bilinmeyen bir ses geldi"
   - Cümle 0 (plan satırı): «ağaçların arasından bilinmeyen bir ses geldi | kurallara uydu ve arkadaşıyla gidip süngeri buldu»
   - Açıklama: Bir sesin gelmesi çocuğun önemseyeceği gerçek bir sorun değil; ıslak sünger bulunup bitiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İkisi sesin geldiği yere yürüdü"
   - Cümle 7: «İkisi sesin geldiği yere yürüdü.»
   - Açıklama: Ormanda bilinmeyen bir sesin peşinden bir yetişkine haber vermeden gidilmesi çocuk için taklit edilebilir riskli bir davranış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Güneş bulutların arasından çıktı ve orman aydınlandı"
   - Cümle 8: «Güneş bulutların arasından çıktı ve orman aydınlandı.»
   - Açıklama: Güneşin çıkması olaydan çıkmıyor ve hiçbir işe yaramıyor.
   - Açıklama: Güneşin çıkması olayda hiçbir işe yaramayan sebepsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0044` birebir aynı, ardından `@onarim: 6f270feda6926392180016473e59afbd9a2cdfe2`, sonra gövde.

### Hikâye 4: tohum chase-0045 (deneme 1 -> 2)

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
@plan: rüzgar mavi şapkayı çadırın üstüne attı | yetişemedi ve arkadaşından yardım istedi
@tohum: chase-0045
@degisim: kolye -> çadır
Bir sabah kamp yerinde kuşlar şakıyordu. Chase çadırın önünde kremalı bir kek yiyordu. Birden rüzgar esti ve mavi şapkası çadırın üstüne uçtu. Chase zıpladı ama oraya yetişemedi. Sonra Marshall'ın yanına koştu ve ondan yardım istedi. Marshall hemen geldi ve çadırın ipini hafifçe salladı. Çadır sallandı ve şapka kayıp aşağı düştü. Chase onu yerden aldı ve başına taktı. Sonra ikisi yan yana oturdu. Chase kekinin yarısını Marshall'a verdi. Chase çok mutlu oldu, çünkü şapkası yine başındaydı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "mavi şapkası çadırın üstüne uçtu"
   - Cümle 3: «Birden rüzgar esti ve mavi şapkası çadırın üstüne uçtu.»
   - Açıklama: Tohum özelliği şapka yalnız kaybolan nesne olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0045` birebir aynı, `@degisim: kolye -> çadır` (tutuyorsan), ardından `@onarim: 16c2f2df5161e2a07161c15eeacd97532852d04e`, sonra gövde.

### Hikâye 5: tohum chase-0047 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Ryder
@tohum: chase-0047
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: paylaşmak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'resim', fiil 'sergilemek', sıfat 'mutsuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Ryder
@plan: rüzgar üstünde taş olmayan resmi uçurdu | resmi kokusundan bulup kendi taşını paylaştı
@tohum: chase-0047
Kamp yerinde rüzgar hafif hafif esiyordu. Ryder ile Chase resimlerini büyük bir kütüğün üstünde sergiliyordu. Ama Ryder'ın resminin üstünde taş yoktu ve rüzgar onu uçurdu. Ryder mutsuz oldu. "Resmim nereye gitti?" diye sordu Ryder. Chase burnunu yere eğdi ve boya kokusunu aldı. Sonra bir çalının dibine gitti ve resmi buldu. Onu ağzıyla dikkatlice Ryder'a getirdi. Chase'in kendi resminin üstünde iki taş vardı. Taşlardan birini Ryder'ın resminin üstüne koydu. Şimdi iki resim de yan yana duruyordu. "Taşını benimle paylaştın, teşekkürler, Chase!" dedi Ryder.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir kütüğün üstünde sergiliyordu"
   - Cümle 2: «Ryder ile Chase resimlerini büyük bir kütüğün üstünde sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kütüğün üstünde sergiliyordu"
   - Cümle 2: «Ryder ile Chase resimlerini büyük bir kütüğün üstünde sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase burnunu yere eğdi"
   - Cümle 6: «Chase burnunu yere eğdi ve boya kokusunu aldı.»
   - Açıklama: Burun eğilmez; 'başını yere eğdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0047` birebir aynı, ardından `@onarim: 5c80effc1e0d3e5ce9f8181e65ddeb3d2afdb63d`, sonra gövde.

### Hikâye 6: tohum chase-0048 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0048
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'gümüş', fiil 'boyamak', sıfat 'somurtkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: rüzgar uçurtmayı yüksek bir dala taktı | kurallara uydu, tırmanmadı ve arkadaşından yardım istedi
@tohum: chase-0048
Parkta güçlü bir rüzgar esiyordu. Chase gümüş rengine boyadığı uçurtmasını uçuruyordu. Birden rüzgar uçurtmayı yüksek bir ağacın dalına taktı. Chase somurtkan bir yüzle dala baktı. Chase kurallara uyardı ve ağaca tırmanmadı. Skye da parktaydı ve Chase ona koştu. "Skye, uçurtmam ağaca takıldı, bana yardım eder misin?" diye sordu Chase. "Tabii, hemen gelirim," dedi Skye. Skye helikopteriyle ağacın üstüne uçtu. Uçurtmanın ipini dikkatle çekti ve daldan kurtardı. Uçurtma yavaşça Chase'in önüne indi. Chase çok sevindi, çünkü uçurtmasını geri almıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase somurtkan bir yüzle"
   - Cümle 4: «Chase somurtkan bir yüzle dala baktı.»
   - Açıklama: 'Somurtkan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Somurtkan' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı ve"
   - Cümle 5: «Chase kurallara uyardı ve ağaca tırmanmadı.»
   - Açıklama: 'Kural' soyut bir kavram ve 'uyardı' kelimesi 'ikaz etti' diye de okunabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0048` birebir aynı, ardından `@onarim: 081042d6a785e52187c8c1fb16a1336845344adb`, sonra gövde.

### Hikâye 7: tohum chase-0049 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Marshall
@tohum: chase-0049
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'şapka', fiil 'üzülmek', sıfat 'sadık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Marshall
@plan: iki köpek aynı salıncağa binmek istedi | kurallara uydu ve sırayla binmeyi önerdi
@tohum: chase-0049
@degisim: şapka -> salıncak
Chase ile Marshall kamp yerinde salıncağa aynı anda koştu. Ama bir tane salıncak vardı ve ikisi de binmek istiyordu. Marshall üzüldü ve başını öne eğdi. Chase kurallara hep uyardı ve sırayla oynamayı biliyordu. "Önce sen bin, Marshall, sonra sıra bende," dedi Chase. Marshall sevindi ve salıncağa bindi. Chase onu yavaşça salladı ve ona kadar saydı. Sonra sıra Chase'e geldi ve Marshall onu salladı. İkisi de gülerek sallandı. "Teşekkürler, Chase, sen sadık bir arkadaşsın!" dedi Marshall.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "kamp yerinde salıncağa aynı anda"
   - Cümle 1: «Chase ile Marshall kamp yerinde salıncağa aynı anda koştu.»
   - Açıklama: Başlıktaki yer orman ama hikaye yalnız kamp yerinde geçiyor ve ormanı hiç kurmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sen sadık bir arkadaşsın"
   - Cümle 10: «"Teşekkürler, Chase, sen sadık bir arkadaşsın!" dedi Marshall.»
   - Açıklama: Sırayı paylaşmak sadakat değildir; kelime yanlış anlamda.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sen sadık bir arkadaşsın"
   - Cümle 10: «"Teşekkürler, Chase, sen sadık bir arkadaşsın!" dedi Marshall.»
   - Açıklama: 'Sadık' soyut bir kelime ve olayla ilgisi yok; figürün özelliği kurallara uymak.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Teşekkürler, Chase, sen sadık"
   - Cümle 10: «"Teşekkürler, Chase, sen sadık bir arkadaşsın!" dedi Marshall.»
   - Açıklama: İki ayrı cümle virgülle birleştirilmiş; noktalama yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0049` birebir aynı, `@degisim: şapka -> salıncak` (tutuyorsan), ardından `@onarim: 9f9f749539a7bc3eabfba58e6ad9ecf166d1795a`, sonra gövde.

### Hikâye 8: tohum chase-0050 (deneme 1 -> 2)

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
@plan: kamp yerinde kimin olduğu bilinmeyen bir kutu vardı | kutuyu kokladı ve kokunun sahibini buldu
@tohum: chase-0050
Chase kamp yerinde bir kütüğün yanında siyah bir kutu gördü. Kutu çamurluydu ve kimin olduğu belli değildi. Chase kutunun kimin olduğunu çok merak etti. Burnunu yaklaştırdı ve kokladı. Bu, Ryder'ın kokusuydu! "Ryder, bu kutu senin mi?" diye seslendi Chase. Ryder koşarak geldi. "Evet, bu benim, burada unutmuşum!" dedi Ryder. Ryder çamuru bir bezle sildi ve kutuyu açtı. Keman içeride güvenli kalmıştı. Sonra Ryder keman çaldı ve Chase mutlu mutlu dinledi.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase kutunun kimin olduğunu çok merak etti"
   - Cümle 3: «Chase kutunun kimin olduğunu çok merak etti.»
   - Açıklama: Kutunun kimin olduğu bir önceki cümlede zaten söylendi; gereksiz tekrar.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kutunun kimin olduğunu çok merak etti"
   - Cümle 3: «Chase kutunun kimin olduğunu çok merak etti.»
   - Açıklama: Kutunun kimin olduğu bir önceki cümlede söylendi; aynı bilgi gereksiz yere tekrarlanıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keman içeride güvenli kalmıştı"
   - Cümle 10: «Keman içeride güvenli kalmıştı.»
   - Açıklama: 'Güvenli' yanlış anlamda; 'güvende kalmıştı' olmalı.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sonra Ryder keman çaldı"
   - Cümle 11: «Sonra Ryder keman çaldı ve Chase mutlu mutlu dinledi.»
   - Açıklama: Kartta Ryder'ın kemanı ya da keman çalma yeteneği yok (yanlar/ilişki alanı).
   - Açıklama: Kartın yanlar alanında Ryder'ın kemanı ya da keman çalma yeteneği yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0050` birebir aynı, ardından `@onarim: 7709b80d1c75bd10b88fe977fbab521fee18d8df`, sonra gövde.

### Hikâye 9: tohum chase-0051 (deneme 1 -> 2)

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
@plan: bazı kabukların içinde minik canlılar vardı | kurallara uydu ve yalnız boş kabukları topladı
@tohum: chase-0051
@degisim: kaydetmek -> yaymak
Kumsalda dalgalar yavaş yavaş geliyordu. Chase kumaş örtüsünü yaydı ve yakında renkli kabuklar gördü. Onları toplamak istedi ama bazı kabukların içinde minik canlılar vardı. Chase bir polis köpeğiydi ve kurallara hep uyardı. Kumsaldan canlı bir şey almak doğru değildi. Chase her kabuğa dikkatle baktı. İçinde canlı olanları suyun kenarına geri bıraktı. Boş kabukların üstünde yapışkan kum vardı. Chase kumu patisiyle temizledi. Sonra kabuklarla örtünün üstünde büyük bir yıldız yaptı. Chase yıldızına bakıp mutlu mutlu kuyruğunu salladı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yaydı ve yakında renkli kabuklar"
   - Cümle 2: «Chase kumaş örtüsünü yaydı ve yakında renkli kabuklar gördü.»
   - Açıklama: 'Yakında' burada 'yakınında' anlamında kullanılmış ama 'kısa süre sonra' anlamına da gelir; belirsiz.
   - Açıklama: 'Yakında' zaman anlamına gelir; yer için 'yakınında' ya da 'yakınlarda' denmeli.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Boş kabukların üstünde yapışkan kum"
   - Cümle 8: «Boş kabukların üstünde yapışkan kum vardı.»
   - Açıklama: Yapışkan kum ana sorundan ayrı ikinci bir sorun olarak ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Boş kabukların üstünde yapışkan kum vardı"
   - Cümle 8: «Boş kabukların üstünde yapışkan kum vardı.»
   - Açıklama: Yapışkan kum sebepsiz beliriyor ve olaya bir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0051` birebir aynı, `@degisim: kaydetmek -> yaymak` (tutuyorsan), ardından `@onarim: 6f6afe0846ec333b3f244fa74d47dd4407516542`, sonra gövde.
