# Editör görevi (onarım): Chase, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0059
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bezelye', fiil 'ıslanmak', sıfat 'çiçekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: top kaydı ve havuzun ortasında kaldı | şapkasıyla suya vurdu ve topu kenara getirdi
@tohum: chase-0059
@degisim: bezelye -> top
Bir sabah Chase parkta topla komik bir oyun oynuyordu. Topu burnunun üstünde tutuyor ve çiçekli çimlerin arasında yürüyordu. Ama top birden kaydı ve fıskiyenin sığ havuzuna düştü. Top suyun ortasında kaldı ve Chase ona uzanamadı. Chase suya girmedi ve biraz düşündü. Sonra mavi şapkasını çıkardı ve onunla suya hafif hafif vurdu. Küçük dalgalar topu yavaş yavaş kenara itti. Chase topu sudan aldı. Ama Chase'in burnu da ıslanmıştı. Chase buna çok güldü. Chase bundan sonra topla oynarken havuzdan uzak durdu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "fıskiyenin sığ havuzuna düştü"
   - Cümle 3: «Ama top birden kaydı ve fıskiyenin sığ havuzuna düştü.»
   - Açıklama: 'sığ' kelimesini 3 yaşındaki çocuk bilmeyebilir.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Küçük dalgalar topu yavaş yavaş kenara itti"
   - Cümle 7: «Küçük dalgalar topu yavaş yavaş kenara itti.»
   - Açıklama: Kenardan suya vurmak dalgaları dışa doğru yayar, topu kenara değil uzağa iter; çözüm akla yatkın biçimde işlemiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama Chase'in burnu da ıslanmıştı"
   - Cümle 9: «Ama Chase'in burnu da ıslanmıştı.»
   - Açıklama: Chase suya hiç girmediği halde burnunun ıslanması sebepsiz beliriyor ve olaya hiçbir şey katmıyor.
   - Açıklama: Chase suya girmediği halde burnunun ıslanması sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0059` birebir aynı, `@degisim: bezelye -> top` (tutuyorsan), ardından `@onarim: c8f16bf8a5337ff5b414053b53b6ac86c3b85310`, sonra gövde.

### Hikâye 2: tohum chase-0062 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Skye
@tohum: chase-0062
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Skye
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'takvim', fiil 'vedalaşmak', sıfat 'kısa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | Skye
@plan: güneş çok parlaktı ve uçan kuşlar görünmedi | mavi şapkasını arkadaşının başına taktı
@tohum: chase-0062
@degisim: vedalaşmak -> sallamak
Chase, Skye ile evleri olan kulenin önünde oturuyordu. İkisi duvardaki takvime bakıyordu. Takvimde kısa kuyruklu kuşların resmi vardı. Birden gökyüzünde de böyle kuşlar göründü. Skye kuşlara güle güle demek istedi ama güneş çok parlaktı. "Kuşlar nerede, Chase? Hiçbirini göremiyorum," dedi Skye. Chase mavi şapkasını çıkardı ve arkadaşının başına taktı. Şapka onun gözlerini güneşten korudu. Skye şimdi kuşları rahatça gördü. "Güle güle, kuşlar!" dedi Skye ve patisini salladı. Chase de sevinçle havladı. Sonra kuşlar yavaş yavaş uzaklaştı. Skye çok sevindi, çünkü kuşlar gitmeden onları görmüştü.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İkisi duvardaki takvime bakıyordu"
   - Cümle 2: «İkisi duvardaki takvime bakıyordu.»
   - Açıklama: Kulenin önünde otururken duvardaki takvim sebepsiz beliriyor ve olayda işe yaramıyor.
   - Açıklama: Kulenin önünde oturan karakterlerin baktığı takvim ve üzerindeki kuş resmi olaya hiçbir katkı yapmıyor, kuşların belirmesi de tesadüfle geliyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Birden gökyüzünde de böyle kuşlar göründü"
   - Cümle 4: «Birden gökyüzünde de böyle kuşlar göründü.»
   - Açıklama: Kuşların göründüğü söyleniyor ama hemen ardından Skye hiçbirini göremediğini söylüyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 5: «Skye kuşlara güle güle demek istedi ama güneş çok parlaktı.»
   - Açıklama: Sorun (güneşten kuşların görülmemesi) ancak 5. cümlede söyleniyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şapka onun gözlerini güneşten korudu"
   - Cümle 9: «Şapka onun gözlerini güneşten korudu.»
   - Açıklama: 'Onun' zamirinin Chase'i mi Skye'ı mı gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0062` birebir aynı, `@degisim: vedalaşmak -> sallamak` (tutuyorsan), ardından `@onarim: 87d8dbb69b15206fe7194930f0cad43502f945fd`, sonra gövde.

### Hikâye 3: tohum chase-0064 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | -
@tohum: chase-0064
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'şemsiye', fiil 'yetiştirmek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | ev | -
@plan: yağmur geliyordu ve ince sapı olan çiçek kırılabilirdi | yağmuru kokladı ve saksıyı kulübesine taşıdı
@tohum: chase-0064
@degisim: şemsiye -> saksı
Bir sabah Chase kulübesinin önünde saksıda küçük bir çiçek yetiştiriyordu. Gökyüzü açıktı ama Chase burnuyla yağmurun kokusunu aldı. Çiçeğin sapı çok inceydi ve sert damlalar onu kırabilirdi. Chase saksıyı ağzıyla dikkatle tuttu ve kulübesine taşıdı. Saksıyı kapının yanına, kuru bir yere koydu. Biraz sonra yağmur başladı. Damlalar kulübenin üstünde tık tık ses çıkardı. Chase çiçeğin yanında sessiz sessiz bekledi. Yağmur dinince saksıyı yine dışarı çıkardı. Çiçek hiç kırılmamıştı ve dimdik duruyordu. Chase bundan sonra yağmurun kokusunu alınca çiçeğini hep içeri taşıdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase bundan sonra yağmurun kokusunu alınca"
   - Cümle 11: «Chase bundan sonra yağmurun kokusunu alınca çiçeğini hep içeri taşıdı.»
   - Açıklama: Tohumdaki koku özelliği çözümden sonra son cümlede ikinci kez tekrar ediliyor; özellik bir kez kullanılmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0064` birebir aynı, `@degisim: şemsiye -> saksı` (tutuyorsan), ardından `@onarim: 0e915a0748be9910a191de816c0a13cd724c83cc`, sonra gövde.

### Hikâye 4: tohum chase-0065 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0065
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'zarf', fiil 'havalanmak', sıfat 'büyük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: arkadaşı uçak yapmak istedi ama kağıdı yoktu | kağıtlarını ikiye ayırıp yarısını ona verdi
@tohum: chase-0065
Chase kumsalda büyük bir zarf açtı. İçinde uçak yapmak için renkli kağıtlar vardı. Ryder da uçak yapmak istedi, ama onun kağıtları kulede kalmıştı. Chase kağıtları ikiye ayırdı. "Ryder, yarısı senin," dedi Chase. "Teşekkürler, Chase!" dedi Ryder. İkisi kağıtları katladı ve güzel uçaklar yaptı. "Kural bu, uçakları denize değil, kuma doğru atalım," dedi Chase. Ryder başını salladı. Uçaklar rüzgarla havalandı ve yumuşak kuma kondu. Chase ile Ryder uçaklarını tekrar tekrar uçurup mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Ryder da uçak yapmak"
   - Cümle 3: «Ryder da uçak yapmak istedi, ama onun kağıtları kulede kalmıştı.»
   - Açıklama: 'Ryder' okunuşuna göre bağlaç 'de' olmalı: 'Ryder de'.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kural bu, uçakları denize değil, kuma doğru atalım"
   - Cümle 8: «"Kural bu, uçakları denize değil, kuma doğru atalım," dedi Chase.»
   - Açıklama: Kural sebepsizce ortaya çıkıyor; sorunla ya da önceki olaylarla bağı yok, yalnız özelliği göstermek için eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0065` birebir aynı, ardından `@onarim: 95d5c4b5184258930f26c0bd6cd41906ff3a970d`, sonra gövde.

### Hikâye 5: tohum chase-0067 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Skye
@tohum: chase-0067
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Skye
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'yün', fiil 'asmak', sıfat 'zarif'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Skye
@plan: koşarken yünden çiçeğe çarptı ve çiçek düştü | özür diledi ve çiçeği yerine astı
@tohum: chase-0067
Rüzgar esiyordu ve Chase parkta koşuyordu. Skye yünden zarif bir çiçek yapmış ve parkın çitine bağlamıştı. Chase koşarken dikkat etmedi, çiçeğe çarptı ve onu yere düşürdü. Skye yerdeki çiçeğe baktı ve üzüldü. Chase kurallara uyardı ve hata yapınca özür dilerdi. "Özür dilerim, Skye, çiçeğini düşürdüm," dedi Chase. Sonra çiçeği yerden aldı ve tozunu silkti. Chase onu dikkatle çite geri astı. "Teşekkürler, Chase, çiçeğim yine yerinde," dedi Skye. Sonra ikisi parkta kaydıraktan mutlu mutlu kaydı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "koşarken yünden çiçeğe çarptı"
   - Cümle 0 (plan satırı): «koşarken yünden çiçeğe çarptı ve çiçek düştü | özür diledi ve çiçeği yerine astı»
   - Açıklama: 'Yünden çiçeğe' tamlaması eksik; 'yünden yapılmış çiçeğe' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yünden zarif bir çiçek"
   - Cümle 2: «Skye yünden zarif bir çiçek yapmış ve parkın çitine bağlamıştı.»
   - Açıklama: 'Zarif' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 5: «Chase kurallara uyardı ve hata yapınca özür dilerdi.»
   - Açıklama: 'Kurallara uyardı' soyut bir karakter anlatımı, olaydan çıkan somut ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0067` birebir aynı, ardından `@onarim: 5875d8273dc6b3ad4c5c2061d812aa73dca5e42d`, sonra gövde.

### Hikâye 6: tohum chase-0069 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Marshall
@tohum: chase-0069
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Marshall
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'piyano', fiil 'kaybetmek', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Marshall
@plan: arkadaşının oyuncak piyanosunu bir yere bırakıp kaybetti | özür diledi ve kokuyu izleyip piyanoyu buldu
@tohum: chase-0069
@degisim: gizemli -> renkli
Parkta Chase, Marshall'ın renkli oyuncak piyanosuyla oynuyordu. Sonra kaydırağa koştu ve piyanoyu bir yere bıraktı. Ama nereye bıraktığını unuttu ve piyanoyu kaybetti. Marshall piyanosunu aradı ve çok üzüldü. Chase, Marshall'dan hemen özür diledi. Piyanoda Marshall'ın kokusu vardı. Chase burnuyla bu kokuyu izledi ve kum havuzuna gitti. Piyano orada, kumun içinde duruyordu. Chase onu kumdan çıkardı, silkti ve Marshall'a verdi. Marshall kuyruğunu salladı ve Chase'e sarıldı. Sonra ikisi piyanoyu sırayla çalıp mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Piyano orada, kumun içinde duruyordu"
   - Cümle 8: «Piyano orada, kumun içinde duruyordu.»
   - Açıklama: Chase piyanoyu kaydırağa giderken bırakmıştı; piyanonun kum havuzunda kumun içinde olmasının sebebi verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0069` birebir aynı, `@degisim: gizemli -> renkli` (tutuyorsan), ardından `@onarim: 6b877e4da0720603dbcafd727cd058a1d8fd6970`, sonra gövde.

### Hikâye 7: tohum chase-0071 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0071
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'mermer', fiil 'sıkılmak', sıfat 'özel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: koşarken kardan köpeğe çarptı ve başı düştü | özür diledi ve başı yerine koydu
@tohum: chase-0071
@degisim: mermer -> kar
Bir sabah Rubble karlı dağda kardan özel bir köpek yapıyordu. Chase onu bekliyordu, ama çok sıkıldı ve karda koşmaya başladı. Koşarken çarptı ve kardan köpeğin başı yere yuvarlandı. Rubble başsız köpeğe baktı ve üzüldü. Chase hemen kurala uydu ve Rubble'ın yanına gitti. "Özür dilerim, Rubble, beklerken sıkıldım ve koştum," dedi Chase. Sonra yuvarlanan başı itip geri getirdi. İkisi birlikte başı yerine koydu. Chase başın üstüne iki küçük kulak da yaptı. "Teşekkürler, Chase, köpeğimiz şimdi daha da güzel!" dedi Rubble.
```

**Hakem bulguları (6):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "köpeğe çarptı ve başı düştü"
   - Cümle 0 (plan satırı): «koşarken kardan köpeğe çarptı ve başı düştü | özür diledi ve başı yerine koydu»
   - Açıklama: Plandaki 'başı' zamirinin Chase'i mi kardan köpeği mi gösterdiği belli değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Koşarken çarptı ve kardan"
   - Cümle 3: «Koşarken çarptı ve kardan köpeğin başı yere yuvarlandı.»
   - Açıklama: Çarptı fiilinin yönelme tümleci eksik; neye çarptığı söylenmiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Koşarken çarptı ve"
   - Cümle 3: «Koşarken çarptı ve kardan köpeğin başı yere yuvarlandı.»
   - Açıklama: 'Çarptı' fiilinin yönelme tümleci eksik; neye çarptığı söylenmiyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase hemen kurala uydu"
   - Cümle 5: «Chase hemen kurala uydu ve Rubble'ın yanına gitti.»
   - Açıklama: 'Kurala uymak' soyut ve hangi kural olduğu belli değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase hemen kurala uydu"
   - Cümle 5: «Chase hemen kurala uydu ve Rubble'ın yanına gitti.»
   - Açıklama: Hangi kurala uyulduğu belirsiz; tohumdaki kural özelliği işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kural özelliği hiçbir kural söylenmeden anılıyor ve çözüme işe yarar biçimde katkı vermiyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase hemen kurala uydu"
   - Cümle 5: «Chase hemen kurala uydu ve Rubble'ın yanına gitti.»
   - Açıklama: Hangi kurala uyulduğu hiç kurulmuyor; kural sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0071` birebir aynı, `@degisim: mermer -> kar` (tutuyorsan), ardından `@onarim: 34eacce58059db7f3771186c43ca2740623686dc`, sonra gövde.

### Hikâye 8: tohum chase-0072 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0072
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'plak', fiil 'şaşırtmak', sıfat 'neşeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: kumsalda nereden geldiği bilinmeyen tatlı bir koku vardı | burnuyla izledi ve iskelenin dibinde çiçekleri buldu
@tohum: chase-0072
@degisim: plak -> çiçek
Dalgalar kumsala yavaşça vuruyordu. Chase kumda yürürken tatlı bir koku aldı. Ama çevrede hiçbir şey göremedi. Chase merak etti. Burnunu havaya kaldırdı ve derin derin kokladı. Sonra burnunun gösterdiği yöne, iskelenin yanına yürüdü. Orada, iskelenin dibinde küçük sarı çiçekler açmıştı. Koku bu çiçeklerden geliyordu. Bu, Chase'i çok şaşırttı, çünkü kumsalda daha önce hiç çiçek görmemişti. Chase çiçeklerin yanına oturdu ve neşeli bir sesle havladı. Chase çok mutluydu, çünkü kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tatlı bir koku aldı"
   - Cümle 2: «Chase kumda yürürken tatlı bir koku aldı.»
   - Açıklama: Nereden geldiği bilinmeyen hoş bir koku gerçek bir sorun değil; çocuğun önemseyeceği bir dert kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "burnunun gösterdiği yöne"
   - Cümle 6: «Sonra burnunun gösterdiği yöne, iskelenin yanına yürüdü.»
   - Açıklama: Burun yön göstermez; mecazlı anlatım küçük çocuğa uygun değil.
   - Açıklama: Burnun yön göstermesi mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0072` birebir aynı, `@degisim: plak -> çiçek` (tutuyorsan), ardından `@onarim: ff214b3ab4e7a97df6298cc20bee580b4f811525`, sonra gövde.
