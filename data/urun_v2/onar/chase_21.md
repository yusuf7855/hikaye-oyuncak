# Editör görevi (onarım): Chase, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0062 (deneme 5 -> 6)

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
Chase, Skye ile kulübelerinin önünde oturuyordu. İkisi bir takvimde kısa kuyruklu kuşların resmine bakıyordu. Birden kuşların sesi geldi, ama güneş çok parlaktı ve Skye bakamadı. "Kuşlar nerede, Chase? Hiçbirini göremiyorum," dedi Skye. Chase mavi şapkasını çıkardı ve Skye'ın başına taktı. Şapka Skye'ın gözlerini güneşten korudu. Skye şimdi kuşları rahatça gördü. "Bunlar takvimdeki kuşlar! Güle güle!" dedi Skye ve patisini salladı. Chase de sevinçle havladı. Sonra kuşlar yavaş yavaş uzaklaştı. Skye çok sevindi, çünkü kuşlar gitmeden onları görmüştü.
```

**Hakem bulguları (2):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "güneş çok parlaktı ve uçan kuşlar görünmedi"
   - Cümle 0 (plan satırı): «güneş çok parlaktı ve uçan kuşlar görünmedi | mavi şapkasını arkadaşının başına taktı»
   - Açıklama: Çoğul canlı kuşlar arka planda kalmıyor, sorunun ve sahnenin merkezinde yer alıp olaya katılıyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Sonra kuşlar yavaş yavaş uzaklaştı"
   - Cümle 12: «Sonra kuşlar yavaş yavaş uzaklaştı.»
   - Açıklama: Çoğul canlı kuşlar arka planda kalmıyor, sorunun ve olayın merkezine giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0062` birebir aynı, `@degisim: vedalaşmak -> sallamak` (tutuyorsan), ardından `@onarim: c730e4ca83ba8b7129c846fdeb46e97bd06905e4`, sonra gövde.

### Hikâye 2: tohum chase-0065 (deneme 4 -> 5)

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
@plan: arkadaşı uçak yapmak istedi ama kağıdı yoktu | kağıtları saydı, ikiye ayırdı ve yarısını ona verdi
@tohum: chase-0065
Chase kumsalda büyük bir zarf açtı. İçinde uçak yapmak için renkli kağıtlar vardı. Ryder de uçak yapmak istedi, ama onun kağıtları kulede kalmıştı. Chase kurallara uyardı: paylaşırken herkes eşit sayıda alırdı. Kağıtları tek tek saydı ve ikiye ayırdı. "Ryder, yarısı senin," dedi Chase. "Teşekkürler, Chase!" dedi Ryder. İkisi kağıtları katladı ve güzel uçaklar yaptı. Sonra onları havaya attılar. Uçaklar rüzgarla havalandı ve yumuşak kuma kondu. Chase ile Ryder uçaklarını tekrar tekrar uçurdu ve mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı: paylaşırken herkes eşit sayıda alırdı."
   - Cümle 4: «Chase kurallara uyardı: paylaşırken herkes eşit sayıda alırdı.»
   - Açıklama: 'Kural' ve 'eşit sayıda' soyut kavramlar 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "paylaşırken herkes eşit sayıda alırdı"
   - Cümle 4: «Chase kurallara uyardı: paylaşırken herkes eşit sayıda alırdı.»
   - Açıklama: 'Eşit sayıda' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0065` birebir aynı, ardından `@onarim: 38a15a0057c36e31d08898d4082725c5c7f49085`, sonra gövde.

### Hikâye 3: tohum chase-0070 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | -
@tohum: chase-0070
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'televizyon', fiil 'sevinmek', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | park | -
@plan: top kuyruğuna çarptı ve bankın altına yuvarlandı | şapkasını dişleriyle uzatıp topu kendine çekti
@tohum: chase-0070
@degisim: televizyon -> top
Parkta Chase simsiyah bir topla oynuyordu. Topu burnuyla havaya atıyor, sonra kuyruğuyla tutmaya çalışıyordu. Ama top bir kez kuyruğuna çarptı ve bankın altına yuvarlandı. Chase patisini uzattı, ama top biraz uzaktaydı. Bankın altı dardı ve Chase oraya giremedi. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı dişleriyle tuttu ve topun arkasına uzattı. Sonra şapkayı yavaşça geri çekti ve top bankın altından çıktı. Chase topu burnuyla havaya attı ve bu sefer ağzıyla yakaladı. Chase çok sevindi, çünkü topuyla yine oynayabiliyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sonra kuyruğuyla tutmaya çalışıyordu"
   - Cümle 2: «Topu burnuyla havaya atıyor, sonra kuyruğuyla tutmaya çalışıyordu.»
   - Açıklama: Kuyrukla top tutulmaz; fiil araca uymuyor.
   - Açıklama: Kuyrukla top tutulmaz; 'tutmak' fiili araca uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0070` birebir aynı, `@degisim: televizyon -> top` (tutuyorsan), ardından `@onarim: e32ee8d50e394ce4e615143f79faf0b969a9ed4f`, sonra gövde.

### Hikâye 4: tohum chase-0071 (deneme 4 -> 5)

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
@plan: koşarken kardan köpeğe çarptı ve köpeğin başı düştü | özür diledi ve kardan başı yerine koydu
@tohum: chase-0071
@degisim: mermer -> kar
Bir sabah Rubble karlı dağda kardan özel bir köpek yapıyordu. Chase onu bekliyordu, ama çok sıkıldı ve karda koşmaya başladı. Koşarken kardan köpeğe çarptı ve köpeğin başı yere yuvarlandı. Rubble yerdeki başa baktı ve üzüldü. Chase kurallara uyardı ve bir şey bozulunca onu hemen düzeltirdi. Hemen Rubble'ın yanına gitti. "Özür dilerim, Rubble, beklerken sıkıldım ve koştum," dedi Chase. Sonra yuvarlanan başı itip geri getirdi. İkisi birlikte başı yerine koydu. Chase başın üstüne iki küçük kulak da yaptı. "Teşekkürler, Chase, köpeğimiz şimdi daha da güzel!" dedi Rubble.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kardan köpeğe çarptı ve köpeğin başı yere yuvarlandı"
   - Cümle 3: «Koşarken kardan köpeğe çarptı ve köpeğin başı yere yuvarlandı.»
   - Açıklama: Bir köpeğin başının yere yuvarlanması küçük çocuk için ürkütücü bir görüntü olabilir.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "köpeğin başı yere yuvarlandı"
   - Cümle 3: «Koşarken kardan köpeğe çarptı ve köpeğin başı yere yuvarlandı.»
   - Açıklama: Köpek biçimli figürün başının kopup yuvarlanması küçük çocuklar için ürkütücü olabilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uyardı"
   - Cümle 5: «Chase kurallara uyardı ve bir şey bozulunca onu hemen düzeltirdi.»
   - Açıklama: 'Kural' soyut bir kavramdır; 3 yaşındaki çocuk için uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Chase kurallara uyardı ve bir şey bozulunca onu hemen düzeltirdi"
   - Cümle 5: «Chase kurallara uyardı ve bir şey bozulunca onu hemen düzeltirdi.»
   - Açıklama: Tohumdaki kurallara uyma özelliği yalnız söyleniyor, çözüm özür dileyip düzeltmek; özellik işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0071` birebir aynı, `@degisim: mermer -> kar` (tutuyorsan), ardından `@onarim: c8fa2e5e14e3b0c5808ed87ac968f3c1e4d96d07`, sonra gövde.

### Hikâye 5: tohum chase-0072 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar topu götürdü ve iskelenin altından bir ses geldi | kokladı ve sesin topundan geldiğini buldu
@tohum: chase-0072
@degisim: plak -> top
Kumsalda sert bir rüzgar esiyordu. Rüzgar Chase'in kırmızı topunu uzağa yuvarladı. Chase topunu aradı ama hiçbir yerde bulamadı. Birden iskelenin altından tok tok diye bir ses geldi. Bu ses Chase'i çok şaşırttı. Orada çok direk vardı ve top görünmüyordu. Chase burnunu yere yaklaştırdı ve dikkatle kokladı. Orada kendi topunun kokusunu hemen tanıdı. Top, iskelenin direğine hafifçe çarpıyordu. Tok tok sesi buradan geliyordu. Chase topu patisiyle yavaşça dışarı çekti. Sonra neşeli bir sesle havladı. Chase çok sevindi, çünkü kaybolan topunu bulmuştu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "iskelenin altından bir ses geldi"
   - Cümle 0 (plan satırı): «rüzgar topu götürdü ve iskelenin altından bir ses geldi | kokladı ve sesin topundan geldiğini buldu»
   - Açıklama: Ses sorunun parçası değil, topun yerini gösteren bir ipucu; plan sorunu yanlış veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0072` birebir aynı, `@degisim: plak -> top` (tutuyorsan), ardından `@onarim: 4e20d0a8d2534181c910f866958c7173da7d7c46`, sonra gövde.

### Hikâye 6: tohum chase-0073 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | park | Ryder
@tohum: chase-0073
- yer: park (Kasabadaki çocuk oyun parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ryder
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'halat', fiil 'gelmek', sıfat 'farklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | park | Ryder
@plan: güneş yüzünden halatı göremedi ve ona takıldı | şapkasını gözlerinin üstüne indirdi ve on kez atladı
@tohum: chase-0073
@degisim: farklı -> geniş
Parkta kuşlar ötüyordu. Ryder halatı yerde döndürüyordu ve Chase üstünden atlıyordu. Chase on kez atlamak istiyordu, ama güneş gözlerine parlıyordu. Chase halatı göremedi ve halat ayağına takıldı. Chase çimlere yuvarlandı ve ikisi de güldü. "Güneş yüzünden halatı göremiyorum, Ryder," dedi Chase. Sonra mavi şapkasının geniş önünü gözlerinin üstüne indirdi. Artık halatı çok iyi görüyordu. "Hazırım, Ryder, halatı döndür!" dedi Chase. Halat ona doğru geldi ve Chase hemen atladı. Ryder yüksek sesle saydı ve Chase tam on kez atladı. İkisi halat oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "güneş gözlerine parlıyordu"
   - Cümle 3: «Chase on kez atlamak istiyordu, ama güneş gözlerine parlıyordu.»
   - Açıklama: 'Gözlerine parlamak' doğal değil; 'gözlerine vuruyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0073` birebir aynı, `@degisim: farklı -> geniş` (tutuyorsan), ardından `@onarim: 257fa597872e87409bbaac28b4aa2411a1890335`, sonra gövde.

### Hikâye 7: tohum chase-0075 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0075
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'bez', fiil 'dönmek', sıfat 'gri'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: güneş parladığı için sesin geldiği yeri göremedi | şapkasını gözlerinin üstüne indirdi ve dala takılan bezi buldu
@tohum: chase-0075
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken pat pat diye bir ses duydu. Chase sesin nereden geldiğini çok merak etti. Sesin geldiği yere baktı, ama güneş karda çok parlıyordu. Chase uzağı hiç göremedi. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi uzaktaki çam ağacını iyi görüyordu. Ağacın alçak bir dalında gri bir şey dönüyordu. Chase ağaca doğru yavaşça yürüdü. Bu, rüzgarın dala taktığı gri bir bezdi. Rüzgar esince bez dalın etrafında dönüyor ve ses çıkarıyordu. Chase bezi dişleriyle çekip daldan aldı. Ses hemen durdu. Chase bundan sonra güneşte şapkasını hep aşağı indirdi.
```

**Hakem bulguları (3):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "pat pat diye bir ses duydu"
   - Cümle 2: «Chase karda yürürken pat pat diye bir ses duydu.»
   - Açıklama: Hikayede hem sesin kaynağını bulma merakı hem de güneşin gözü alması ayrı sorunlar olarak yer alıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Chase sesin nereden geldiğini çok merak etti.»
   - Açıklama: İlk üç cümlede yalnız ses merakı var; asıl sorun olan güneşin parlaması ancak 4. cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "güneş karda çok parlıyordu"
   - Cümle 4: «Sesin geldiği yere baktı, ama güneş karda çok parlıyordu.»
   - Açıklama: Plandaki sorun olan güneşin gözü alması ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0075` birebir aynı, ardından `@onarim: 95594e7ea8a26d4a8b6714aac94cd8602b5706aa`, sonra gövde.

### Hikâye 8: tohum chase-0076 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0076
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'pelerin', fiil 'uyandırmak', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: yavaş yürüdü ve pelerin hiç kalkmadı | kurallara uydu ve sert kumda rüzgara doğru koştu
@tohum: chase-0076
@degisim: uyandırmak -> uçurmak
Bir sabah Chase kumsalda kıpkırmızı bir pelerin buldu. Pelerini ağzıyla tuttu ve rüzgarda uçurmayı ilk kez denedi. Ama Chase yavaş yürüdü ve pelerin hiç kalkmadı. Chase koşmak için düz bir yer aradı. Uzun iskele çok düzdü, ama orada koşmak yasaktı. Chase kurallara uydu ve iskeleye çıkmadı. Biraz ileride kum sert ve düzdü. Chase orada rüzgara doğru hızlı hızlı koştu. Pelerin arkasında havaya kalktı ve rüzgarda dalgalandı. Chase başını çevirip pelerine baktı ve kuyruğunu salladı. Sonra kumsalda mutlu mutlu koşmaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Uzun iskele çok düzdü, ama orada koşmak yasaktı"
   - Cümle 5: «Uzun iskele çok düzdü, ama orada koşmak yasaktı.»
   - Açıklama: İskele yalnız reddedilmek için kuruluyor ve olaya katkısı olmayan bir ara adım olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0076` birebir aynı, `@degisim: uyandırmak -> uçurmak` (tutuyorsan), ardından `@onarim: 56ea15e4798efe6034b643c3b3c6acb063ada9fc`, sonra gövde.

### Hikâye 9: tohum chase-0077 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | -
@tohum: chase-0077
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'yaprak', fiil 'ıslatmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | orman | -
@plan: çiçeğin toprağı kuruydu ve su taşıyacak kap yoktu | şapkasına su doldurdu ve çiçeğe götürdü
@tohum: chase-0077
Ormandaki kamp yerinde güneş parlıyordu. Chase çiçek sulama oyunu oynuyordu ve küçük bir çiçeği seçmişti. Ama çiçeğin toprağı kuruydu ve yaprakları aşağı eğilmişti. Kamp yerinin yanında küçük bir dere akıyordu. Ama Chase'in su taşıyacak bir kabı yoktu. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı derenin soğuk suyuna daldırdı ve doldurdu. Sonra şapkayı ağzıyla tuttu ve yavaş yavaş çiçeğe yürüdü. Chase suyu çiçeğin dibine döktü ve toprağı ıslattı. Biraz sonra çiçeğin yaprakları yukarı kalktı. Chase çok sevindi, çünkü küçük çiçek yine dik duruyordu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şapkayı derenin soğuk suyuna daldırdı"
   - Cümle 7: «Şapkayı derenin soğuk suyuna daldırdı ve doldurdu.»
   - Açıklama: Chase tek başına dere kenarına gidip suya uzanıyor; çocuk bunu taklit edebilir.
   - Açıklama: Tek başına dere kenarına gidip suya uzanmak çocuğun taklit edebileceği su kenarı davranışı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0077` birebir aynı, ardından `@onarim: 2598daef2774a891e08f6a56607d5e167be6794a`, sonra gövde.

### Hikâye 10: tohum chase-0078 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | Ryder
@tohum: chase-0078
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: paylaşmak
- yan: Ryder
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'çarşaf', fiil 'süpürmek', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | Ryder
@plan: rüzgar çarşafı kaldırdı ve bir elma kayboldu | burnuyla elmanın kokusunu alıp onu buldu
@tohum: chase-0078
@degisim: konuşkan -> kırmızı
Kumsalda serin bir rüzgar esiyordu. Ryder ile Chase büyük bir çarşafın üstünde iki kırmızı elmayla oturuyordu. Birden rüzgar çarşafın ucunu kaldırdı ve elmalardan biri kuma yuvarlandı ve kayboldu. Ryder her yere baktı, ama elmayı göremedi. Chase burnunu kuma yaklaştırdı ve elmanın kokusunu aldı. Sonra küçük bir kum tepesine doğru yürüdü. Elma tepenin arkasında, kumun içindeydi. Chase patisiyle kumu süpürdü ve elma göründü. Chase elmayı ağzıyla aldı ve Ryder'a getirdi. "Teşekkürler, Chase, bir elma sana, bir elma bana," dedi Ryder. İkisi çarşafta elmalarını mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elma tepenin arkasında, kumun içindeydi"
   - Cümle 7: «Elma tepenin arkasında, kumun içindeydi.»
   - Açıklama: Kuma yuvarlanan bir elmanın kaybolup bir tepenin arkasında kumun içine gömülmesi akla yatkın bir sebeple açıklanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0078` birebir aynı, `@degisim: konuşkan -> kırmızı` (tutuyorsan), ardından `@onarim: 56d03627111db5bf50c1bc03092d1930a06cd772`, sonra gövde.

### Hikâye 11: tohum chase-0080 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Rubble
@tohum: chase-0080
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'beşik', fiil 'yedirmek', sıfat 'plastik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Rubble
@plan: arkadaşı uzağa gitmişti ve onu göremedi | kurala uydu ve pastayı büyük ağacın yanına götürdü
@tohum: chase-0080
@degisim: beşik -> pasta
Bir sabah Chase karlı dağda Rubble için küçük bir pasta hazırladı. Pastayı plastik bir tabağa koydu. Ama Rubble karda uzağa gitmişti ve Chase onu göremedi. Bir kural vardı. Herkes yemeğini büyük ağacın yanında yerdi. Chase kurallara uydu ve tabağı ağacın yanına götürdü. Biraz sonra Rubble yemek için oraya geldi. "Rubble, bu pasta senin için!" dedi Chase. "Ne güzel bir sürpriz, Chase!" dedi Rubble. Chase pastadan küçük parçalar aldı ve Rubble'a yedirdi. Chase bundan sonra sürprizlerini hep büyük ağacın yanında hazırladı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rubble karda uzağa gitmişti"
   - Cümle 3: «Ama Rubble karda uzağa gitmişti ve Chase onu göremedi.»
   - Açıklama: Rubble'ın neden uzağa gittiği söylenmiyor, sorunun sebebi yok.
   - Açıklama: Rubble'ın neden uzağa gittiği söylenmiyor ve sorun belirsiz kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir kural vardı"
   - Cümle 4: «Bir kural vardı.»
   - Açıklama: Kural önceden kurulmadan tam çözüm gerektiğinde sebepsizce beliriyor ve çözümü getiriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Herkes yemeğini büyük ağacın yanında yerdi"
   - Cümle 5: «Herkes yemeğini büyük ağacın yanında yerdi.»
   - Açıklama: Kural çözümü getirmek için sebepsizce beliriyor; çözüm olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0080` birebir aynı, `@degisim: beşik -> pasta` (tutuyorsan), ardından `@onarim: b3a8d62952189fbcbde83b1320266c951e2bb7a1`, sonra gövde.

### Hikâye 12: tohum chase-0081 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0081
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'mama', fiil 'çoğalmak', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: rüzgar mama kabını uzağa yuvarladı | şapkasını gözlerinin üstüne indirdi ve parlayan kabı buldu
@tohum: chase-0081
@degisim: tekerlekli -> garip
Kumsalda sert bir rüzgar esiyordu. Chase mamasını yiyecekti, ama mama kabı yerinde yoktu. Rüzgar kabı uzağa götürmüştü ve biraz mama kuma dökülmüştü. Chase kumda küçük mama taneleri gördü. Tanelere bakarak yürüdü ve taneler çoğaldı. Uzakta, kumda garip bir şey parlıyordu. Chase mavi şapkasını gözlerinin üstüne indirdi. Şapkanın gölgesinde iyice baktı ve kendi mama kabını gördü. Mamanın çoğu kabın içindeydi. Chase kabı ağzıyla aldı ve yerine geri getirdi. Sonra mamasını yedi. Chase çok sevindi, çünkü kaybolan mamasını bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar kabı uzağa götürmüştü"
   - Cümle 3: «Rüzgar kabı uzağa götürmüştü ve biraz mama kuma dökülmüştü.»
   - Açıklama: Rüzgarın mama kabını uzağa götürüp mamanın çoğunun yine kabın içinde kalması akla yatkın değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Mamanın çoğu kabın içindeydi"
   - Cümle 9: «Mamanın çoğu kabın içindeydi.»
   - Açıklama: Rüzgar kabı kumsalda uzağa götürürken mamanın çoğunun kabın içinde kalması akla yatkın değil ve dökülen mamayla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0081` birebir aynı, `@degisim: tekerlekli -> garip` (tutuyorsan), ardından `@onarim: 171762ba3c1fac6f7057cafef8f96401f93df49e`, sonra gövde.
