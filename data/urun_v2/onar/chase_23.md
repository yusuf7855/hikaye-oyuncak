# Editör görevi (onarım): Chase, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/chase_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/chase_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum chase-0065 (deneme 5 -> 6)

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
Chase kumsalda büyük bir zarf açtı. İçinde uçak yapmak için renkli kağıtlar vardı. Ryder de uçak yapmak istedi, ama onun kağıtları kulede kalmıştı. Bir kural vardı: herkes kağıtlarını arkadaşıyla paylaşırdı. Chase kağıtları tek tek saydı ve ikiye ayırdı. "Ryder, yarısı senin," dedi Chase. "Teşekkürler, Chase!" dedi Ryder. İkisi kağıtları katladı ve güzel uçaklar yaptı. Sonra onları havaya attılar. Uçaklar rüzgarla havalandı ve yumuşak kuma kondu. Chase ile Ryder uçaklarını tekrar tekrar uçurdu ve mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bir kural vardı: herkes"
   - Cümle 4: «Bir kural vardı: herkes kağıtlarını arkadaşıyla paylaşırdı.»
   - Açıklama: 'Kural' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0065` birebir aynı, ardından `@onarim: d4e0addd28fb341b1b522fa35e3b5c4c2f4ee988`, sonra gövde.

### Hikâye 2: tohum chase-0070 (deneme 5 -> 6)

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
@plan: top yere düştü ve bankın altına yuvarlandı | şapkasını dişleriyle uzatıp topu kendine çekti
@tohum: chase-0070
@degisim: televizyon -> top
Parkta Chase simsiyah bir topla oynuyordu. Topu burnuyla havaya atıyor, sonra ağzıyla yakalamaya çalışıyordu. Ama top bir kez yere düştü ve bankın altına yuvarlandı. Chase patisini uzattı, ama top biraz uzaktaydı. Bankın altı dardı ve Chase oraya giremedi. Chase biraz düşündü ve mavi şapkasını çıkardı. Şapkayı dişleriyle tuttu ve topun arkasına uzattı. Sonra şapkayı yavaşça geri çekti ve top bankın altından çıktı. Chase topu burnuyla havaya attı ve bu sefer ağzıyla yakaladı. Chase çok sevindi, çünkü topuyla yine oynayabiliyordu.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Topu burnuyla havaya atıyor"
   - Cümle 2: «Topu burnuyla havaya atıyor, sonra ağzıyla yakalamaya çalışıyordu.»
   - Açıklama: Anlatımda 'atıyor' şimdiki zamanda kalıyor; 'atıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0070` birebir aynı, `@degisim: televizyon -> top` (tutuyorsan), ardından `@onarim: c27754d83c5b18b30469885b1048bcc36ad89cc9`, sonra gövde.

### Hikâye 3: tohum chase-0073 (deneme 4 -> 5)

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
Parkta kuşlar ötüyordu. Ryder halatı yerde döndürüyordu ve Chase üstünden atlıyordu. Chase on kez atlamak istiyordu, ama güneş çok parlaktı. Chase halatı göremedi ve halat ayağına takıldı. Chase çimlere yuvarlandı ve ikisi de güldü. "Güneş yüzünden halatı göremiyorum, Ryder," dedi Chase. Sonra mavi şapkasının geniş önünü gözlerinin üstüne indirdi. Artık halatı çok iyi görüyordu. "Hazırım, Ryder, halatı döndür!" dedi Chase. Halat ona doğru geldi ve Chase hemen atladı. Ryder yüksek sesle saydı ve Chase tam on kez atladı. İkisi halat oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "halat ayağına takıldı"
   - Cümle 4: «Chase halatı göremedi ve halat ayağına takıldı.»
   - Açıklama: Chase halata takılıp çimlere yuvarlanıyor; düşme ve olası acı içeren bir an var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0073` birebir aynı, `@degisim: farklı -> geniş` (tutuyorsan), ardından `@onarim: 26c7c7915bea1ddd799f9ba135a2908f5b1c9024`, sonra gövde.

### Hikâye 4: tohum chase-0075 (deneme 4 -> 5)

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
@plan: güneş karda parladığı için sesin geldiği yeri göremedi | şapkasını gözlerinin üstüne indirdi ve dala takılan bezi buldu
@tohum: chase-0075
Karlı dağda soğuk bir rüzgar esiyordu. Chase karda yürürken pat pat diye bir ses duydu. Sesin geldiği yere baktı, ama güneş karda çok parlıyordu. Chase uzağı hiç göremedi. Chase mavi şapkasını gözlerinin üstüne indirdi. Şimdi uzaktaki çam ağacını iyi görüyordu. Ağacın alçak bir dalında gri bir şey dönüyordu. Chase ağaca doğru yavaşça yürüdü. Bu, rüzgarın dala taktığı gri bir bezdi. Rüzgar esince bez dalın etrafında dönüyor ve ses çıkarıyordu. Chase bezi dişleriyle çekip daldan aldı. Ses hemen durdu. Chase bundan sonra güneşte şapkasını hep aşağı indirdi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "pat pat diye bir ses duydu"
   - Cümle 2: «Chase karda yürürken pat pat diye bir ses duydu.»
   - Açıklama: Uzaktan gelen bir sesin kaynağını görememek çocuğun önemseyeceği bir sorun olarak kurulmuyor; sesin neden dert olduğu söylenmiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "rüzgarın dala taktığı"
   - Cümle 9: «Bu, rüzgarın dala taktığı gri bir bezdi.»
   - Açıklama: Rüzgar bir şeyi dala takmaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0075` birebir aynı, ardından `@onarim: f19046f41c5b3cc5016627197cbe805c16a3d241`, sonra gövde.

### Hikâye 5: tohum chase-0076 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Bir sabah Chase kumsalda kıpkırmızı bir pelerin buldu. Pelerini ağzıyla tuttu ve rüzgarda uçurmayı ilk kez denedi. Ama Chase yavaş yürüdü ve pelerin hiç kalkmadı. Chase koşmak için düz bir yer aradı. Chase kurallara uydu ve koşmadan önce etrafına baktı. Biraz ileride kum sert ve düzdü, orada kimse yoktu. Chase o sert kumda rüzgara doğru hızlı hızlı koştu. Pelerin arkasında havaya kalktı ve rüzgarda dalgalandı. Chase başını çevirip pelerine baktı ve kuyruğunu salladı. Sonra kumsalda mutlu mutlu koşmaya devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Chase yavaş yürüdü ve pelerin hiç kalkmadı"
   - Cümle 3: «Ama Chase yavaş yürüdü ve pelerin hiç kalkmadı.»
   - Açıklama: Sorun kendi uydurduğu önemsiz bir oyundan çıkıyor ve yalnız hızlı koşarak kendiliğinden bitiyor; çocuğun önemseyeceği gerçek bir sorun yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurallara uydu ve"
   - Cümle 5: «Chase kurallara uydu ve koşmadan önce etrafına baktı.»
   - Açıklama: 'Kurallara uydu' soyut bir ifade ve hangi kural olduğu somut değil.
   - Açıklama: Hangi kurallar olduğu belirsiz; 'kural' soyut bir kavram ve 3 yaşındaki çocuğa somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0076` birebir aynı, `@degisim: uyandırmak -> uçurmak` (tutuyorsan), ardından `@onarim: f33850dc90fedabf84e44d9bd0c600ae437ed1ee`, sonra gövde.

### Hikâye 6: tohum chase-0080 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: arkadaşı kar kazmak için uzağa gitmişti | kurala uydu ve pastayı büyük ağacın yanına götürdü
@tohum: chase-0080
@degisim: beşik -> pasta
Bir sabah Chase karlı dağda Rubble için küçük bir pasta hazırladı. Pastayı plastik bir tabağa koydu. Ama Rubble kar kazmak için uzağa gitmişti ve Chase onu göremedi. Chase biraz düşündü: herkes yemeğini büyük ağacın yanında yerdi. Chase kurala uydu ve tabağı ağacın yanına götürdü. Biraz sonra Rubble yemek için oraya geldi. "Rubble, bu pasta senin için!" dedi Chase. "Ne güzel bir sürpriz, Chase!" dedi Rubble. Chase pastadan küçük parçalar aldı ve Rubble'a yedirdi. Chase bundan sonra sürprizlerini hep büyük ağacın yanında hazırladı.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rubble kar kazmak için uzağa gitmişti"
   - Cümle 3: «Ama Rubble kar kazmak için uzağa gitmişti ve Chase onu göremedi.»
   - Açıklama: Arkadaşın biraz uzakta olması gerçek bir sorun değil; Chase'in neden beklemeyip bir çözüm araması gerektiği anlaşılmıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Chase biraz düşündü"
   - Cümle 4: «Chase biraz düşündü: herkes yemeğini büyük ağacın yanında yerdi.»
   - Açıklama: Chase art arda cümlelerde gereksiz yere adıyla tekrarlanıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "herkes yemeğini büyük ağacın yanında yerdi"
   - Cümle 4: «Chase biraz düşündü: herkes yemeğini büyük ağacın yanında yerdi.»
   - Açıklama: Kural daha önce kurulmadan tam çözüm gerektiğinde sebepsizce beliriyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurala uydu"
   - Cümle 5: «Chase kurala uydu ve tabağı ağacın yanına götürdü.»
   - Açıklama: 'Kurala uymak' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase kurala uydu ve"
   - Cümle 5: «Chase kurala uydu ve tabağı ağacın yanına götürdü.»
   - Açıklama: 'Kurala uymak' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
6. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Chase bundan sonra sürprizlerini hep büyük ağacın yanında hazırladı"
   - Cümle 10: «Chase bundan sonra sürprizlerini hep büyük ağacın yanında hazırladı.»
   - Açıklama: Son ders olaydan tam çıkmıyor; sorun buluşma yeriydi, sürprizi nerede hazırladığı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0080` birebir aynı, `@degisim: beşik -> pasta` (tutuyorsan), ardından `@onarim: 8f1876356fd6484eb22a2017de2e6fc380a86e47`, sonra gövde.

### Hikâye 7: tohum chase-0081 (deneme 4 -> 5)

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
Kumsalda sert bir rüzgar esiyordu. Chase mamasını yiyecekti, ama mama kabı yerinde yoktu. Rüzgar hafif kabı uzağa götürmüştü ve mama yol boyunca dökülmüştü. Chase kumda küçük mama taneleri gördü. Tanelere bakarak yürüdü ve taneler çoğaldı. Uzakta garip bir şey parlıyordu. Chase mavi şapkasını gözlerinin üstüne indirdi. Şapkanın gölgesinde iyice baktı ve kendi mama kabını gördü. Kabın dibinde biraz mama kalmıştı. Chase kabı ağzıyla aldı ve yerine geri getirdi. Sonra kalanını yedi. Chase çok sevindi, çünkü kaybolan kabını bulmuştu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Tanelere bakarak yürüdü ve taneler çoğaldı"
   - Cümle 5: «Tanelere bakarak yürüdü ve taneler çoğaldı.»
   - Açıklama: Çözüm önce mama izini takip etmek, sonra şapkayı indirip bakmak gibi iki ayrı yoldan ve ikiden fazla adımda ilerliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0081` birebir aynı, `@degisim: tekerlekli -> garip` (tutuyorsan), ardından `@onarim: 04029f596d10e3e8ee92dd4361ce3d16e49d65ef`, sonra gövde.

### Hikâye 8: tohum chase-0086 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | Marshall
@tohum: chase-0086
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: sırayla oynamak
- yan: Marshall
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'raf', fiil 'dikmek', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Chase | dağ | Marshall
@plan: tek top vardı ve ikisi de ilk atmak istedi | kurallara uydu ve sırayı önce arkadaşına verdi
@tohum: chase-0086
@degisim: raf -> top
Chase ile Marshall karlı dağda bir top oyunu kuruyordu. Chase kara uzun bir dal dikti ve ikisi topu bu dala atacaktı. Ama tek bir top vardı ve ikisi de onu ilk atmak istedi. Oyunun bir kuralı vardı. Herkes topu sırayla atardı. "Önce sen at, Marshall," dedi Chase. "Teşekkürler, Chase, sonra sıra sende," dedi Marshall. Marshall attı ve top dala değdi. Çalışkan Marshall topu koşarak geri getirdi. Sonra Chase topu attı ve dalı vurdu. Chase ile Marshall çok sevindi, çünkü oyunları yine eğlenceliydi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kara uzun bir dal dikti"
   - Cümle 2: «Chase kara uzun bir dal dikti ve ikisi topu bu dala atacaktı.»
   - Açıklama: 'kara' burada 'siyah' olarak okunuyor; 'karın içine' gibi açık bir ifade gerekir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Chase kara uzun bir dal"
   - Cümle 2: «Chase kara uzun bir dal dikti ve ikisi topu bu dala atacaktı.»
   - Açıklama: 'kara' burada 'kara renkli' diye de okunuyor; 'karın içine' anlamı belirsiz kalıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oyunun bir kuralı vardı."
   - Cümle 4: «Oyunun bir kuralı vardı.»
   - Açıklama: 'kural' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Kural' soyut bir kavram; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0086` birebir aynı, `@degisim: raf -> top` (tutuyorsan), ardından `@onarim: 4eb0c1262ae4fa79421af193b552038530745534`, sonra gövde.

### Hikâye 9: tohum chase-0088 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | dağ | -
@tohum: chase-0088
- yer: dağ (Kasabanın yakınındaki karlı dağ.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şapka (Mavi bir şapka takar.)
- kelimeler: isim 'sürahi', fiil 'kokmak', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | dağ | -
@plan: kar taneleri sıcak sütün içine düşüyordu | mavi şapkasını sürahiye kapak gibi koydu
@tohum: chase-0088
Dağda büyük kar taneleri yağıyordu. Chase'in yanında sıcacık süt dolu bir sürahi vardı. Ama kar taneleri açık sürahiye, sütün içine düşüyordu. Kar yüzünden süt soğumaya başlamıştı. Sürahinin bir kapağı da yoktu. Chase mavi şapkasını çıkardı. Şapkayı sürahiye kapak gibi koydu. Kar taneleri artık şapkanın üstüne düşüyordu. Biraz sonra şapkayı kaldırdı ve yeniden taktı. Sütün içinde hiç kar yoktu ve süt güzel kokuyordu. Chase sütünü yavaş yavaş içti ve karı mutlu mutlu seyretti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sütün içinde hiç kar yoktu"
   - Cümle 10: «Sütün içinde hiç kar yoktu ve süt güzel kokuyordu.»
   - Açıklama: Kar önceden sütün içine düşmüştü ve şapka kalkınca kar yağmaya devam ederken sütte hiç kar olmaması çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0088` birebir aynı, ardından `@onarim: d097bdf68b0582814b2bd9950fe5a6fb3417eef8`, sonra gövde.

### Hikâye 10: tohum chase-0091 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | orman | Rubble
@tohum: chase-0091
- yer: orman (Kasabanın yakınında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Rubble
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'delik', fiil 'tanımak', sıfat 'umutlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Chase | orman | Rubble
@plan: top dar bir deliğe düştü ve patisi yetişemedi | kurallara uydu ve arkadaşından yardım istedi
@tohum: chase-0091
@degisim: umutlu -> dar
Chase kamp yerinde kırmızı topuyla oynuyordu. Top yuvarlandı ve bir ağacın yanındaki dar bir deliğe düştü. Chase patisini uzattı ama topa yetişemedi. Chase bir kuralı biliyordu: Bir iş zor olunca yardım istenirdi. Chase bu kurala uydu ve bir arkadaşını aradı. Ağaçların arasından bir kürek sesi geliyordu. Chase bu sesi hemen tanıdı. "Rubble, topum deliğe düştü, yardım eder misin?" diye sordu Chase. "Tabii, Chase," dedi Rubble. Rubble küreğiyle deliği biraz büyüttü. Chase deliğin yanında bekledi. Sonra patisini uzattı ve topunu çıkardı. "Teşekkürler, Rubble, iyi ki sana seslendim!" dedi Chase.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bir iş zor olunca yardım istenirdi"
   - Cümle 4: «Chase bir kuralı biliyordu: Bir iş zor olunca yardım istenirdi.»
   - Açıklama: Olaydan çıkmayan, edilgen ve genel bir kural cümlesi 3 yaşındaki çocuk için soyut.
   - Açıklama: Genel kural cümlesi soyut ve edilgen; olaydan çıkan somut bir ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0091` birebir aynı, `@degisim: umutlu -> dar` (tutuyorsan), ardından `@onarim: d5a17d6aae58121b5b5a901b41cc40f7f329d737`, sonra gövde.

### Hikâye 11: tohum chase-0092 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | deniz | -
@tohum: chase-0092
- yer: deniz (Kasabanın kıyısı; kumsal ve iskele.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: koku (Burnuyla koku alarak çözüm bulur.)
- kelimeler: isim 'balkabağı', fiil 'birleşmek', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | deniz | -
@plan: dalga kovayı yuvarladı ve topun yerini bulamadı | kumu kokladı ve topun yerini bulup kazdı
@tohum: chase-0092
@degisim: balkabağı -> kova
Chase kumsalda eğlenceli bir oyun oynuyordu. Benekli topunu kuma gömdü ve yanına kırmızı kovasını koydu. Ama küçük bir dalga kovayı uzağa yuvarladı ve Chase topun yerini bulamadı. Chase önce iki yeri yan yana kazdı. İki çukur birleşti ama top orada da yoktu. Chase kumlu kulaklarını salladı ve güldü. Sonra burnunu kuma yaklaştırdı ve dikkatle kokladı. Topunun kokusu biraz uzaktan geliyordu. Chase oraya koştu ve patileriyle kumu açtı. Benekli top kumun içinden çıktı. Chase topu yeniden gömdü ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dalga kovayı yuvarladı ve topun yerini bulamadı"
   - Cümle 0 (plan satırı): «dalga kovayı yuvarladı ve topun yerini bulamadı | kumu kokladı ve topun yerini bulup kazdı»
   - Açıklama: Plan satırında 'bulamadı' fiilinin öznesi dalga oluyor; özne uyumu bozuk.
   - Açıklama: Ortak özne 'dalga' olduğundan topun yerini dalga bulamamış gibi okunuyor; ikinci yüklemin öznesi eksik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0092` birebir aynı, `@degisim: balkabağı -> kova` (tutuyorsan), ardından `@onarim: 7f7cef6bc6c4673549f5111957dea286e5bc12eb`, sonra gövde.

### Hikâye 12: tohum chase-0093 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Chase | ev | Ryder
@tohum: chase-0093
- yer: ev (Ekibin yüksek kulesi ve köpeklerin kulübeleri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ryder
- özellik: kural (Ekibin polis köpeğidir; kurallara uyar.)
- kelimeler: isim 'tomurcuk', fiil 'yaslanmak', sıfat 'dalgalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Chase | ev | Ryder
@plan: çizginin ortası ayakkabıyla silindi | kurallara uydu ve yeni bir çizgi çizdi
@tohum: chase-0093
@degisim: tomurcuk -> tebeşir
Chase ile Ryder kulübelerin önünde çizgi oyunu oynuyordu. Ryder yere tebeşirle uzun, dalgalı bir çizgi çizmişti. Ama Ryder yürürken ayakkabısıyla çizginin ortasını sildi. "Sıra sende, Chase," dedi Ryder ve kulübeye yaslandı. Oyunda çizginin dışına basmak yoktu. Chase bu kurala uydu ve silinen yere basmadı. Chase tebeşiri patisiyle tuttu ve ortaya yeni bir çizgi çizdi. Ryder çizgiye baktı ve sevindi. "Çok güzel olmuş, hadi yürü," dedi Ryder. Chase çizginin üstünde yavaş yavaş yürüdü. Sonra Chase ile Ryder oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Chase bu kurala uydu"
   - Cümle 6: «Chase bu kurala uydu ve silinen yere basmadı.»
   - Açıklama: 'Kurala uymak' soyut bir kavram; 3 yaşındaki çocuk için somut değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Chase bu kurala uydu ve silinen yere basmadı"
   - Cümle 6: «Chase bu kurala uydu ve silinen yere basmadı.»
   - Açıklama: Kural ayrıntısı çözüme bir şey katmıyor ve silinen yere basmamak çizginin dışına basmama kuralıyla bağlanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: chase-0093` birebir aynı, `@degisim: tomurcuk -> tebeşir` (tutuyorsan), ardından `@onarim: 8a5483cc7aeef5f21db8bae19c1b670fd792e544`, sonra gövde.
