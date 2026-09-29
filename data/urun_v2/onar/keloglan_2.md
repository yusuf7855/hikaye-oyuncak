# Editör görevi (onarım): Keloğlan, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar2.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0001
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'yiyecek', fiil 'basmak', sıfat 'dar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: rüzgar yiyecek kabını düşürdü ve kap kayboldu | sesi izledi ve kabı dar bir yerde buldu
@tohum: keloglan-0001
Rüzgar sert esiyordu. Keloğlan şatonun bahçesinde yiyecek kabını arıyordu. Kabı bankın kenarına koymuştu, ama rüzgar onu banktan düşürmüştü ve kap kaybolmuştu. Keloğlan çok acıkmıştı ve kabını bulmak istedi. Birden büyük kapının yanından ince bir ses geldi. Keloğlan yeni şeyler öğrenmeyi severdi ve bu sesi çok merak etti. Yumuşak otlara basarak kapıya doğru yürüdü. Kapının dibinde iki taşın arasında dar bir yer vardı. Yiyecek kabı orada sıkışmıştı. Rüzgar esince kap taşlara çarpıyordu. Ses buradan geliyordu! Keloğlan kabı dar yerden yavaşça çekip aldı. Sonra banka oturdu ve ekmeğini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar onu banktan düşürmüştü ve kap kaybolmuştu"
   - Cümle 3: «Kabı bankın kenarına koymuştu, ama rüzgar onu banktan düşürmüştü ve kap kaybolmuştu.»
   - Açıklama: Banktan düşen bir kabın kaybolup kapının dibindeki taşların arasına gitmesi akla yatkın değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ve kabını bulmak istedi"
   - Cümle 4: «Keloğlan çok acıkmıştı ve kabını bulmak istedi.»
   - Açıklama: Keloğlan'ın kabı aradığı 2. cümlede zaten söylenmişti; gereksiz tekrar.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan yeni şeyler öğrenmeyi severdi ve bu sesi çok merak etti"
   - Cümle 6: «Keloğlan yeni şeyler öğrenmeyi severdi ve bu sesi çok merak etti.»
   - Açıklama: Keloğlan kabını aramak için değil merakı yüzünden sese gidiyor, çözüm sebepsizce tesadüfle geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0001` birebir aynı, ardından `@onarim: 679a5484a24d50bff61bc455a850fc6d0ff6c50b`, sonra gövde.

### Hikâye 2: tohum keloglan-0004 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0004
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kemer', fiil 'getirmek', sıfat 'ıslak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kemer elinden kaydı ve ağacın dalına takıldı | uzun bir çubuk getirip kemeri daldan itti
@tohum: keloglan-0004
Bir sabah Keloğlan ormanda kemerini halka yapıp bir kütüğe atıyordu. Ama Keloğlan biraz sakardı ve bir atışta kemer elinden kaydı. Kemer havaya uçtu ve büyük bir ağacın dalına takıldı. Keloğlan zıpladı, ama eli dala yetişmedi. Kemer olmadan oyuna devam edemezdi. Keloğlan etrafına baktı ve düşündü. Sonra ağaçların altından uzun bir çubuk getirdi. Çubukla kemeri dalın üstünden yavaşça itti. Kemer ıslak yaprakların üstüne düştü. Keloğlan kemeri aldı ve yine halka yaptı. Halkayı kütüğe attı ve bu kez halka tam kütüğe geçti. Keloğlan çok sevindi, çünkü kemerini geri almış ve oyuna dönmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 2: «Ama Keloğlan biraz sakardı ve bir atışta kemer elinden kaydı.»
   - Açıklama: 'Sakar' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0004` birebir aynı, ardından `@onarim: 39bca83141f611019256019a86a6ab7b1a9897e6`, sonra gövde.

### Hikâye 3: tohum keloglan-0005 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0005
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kumaş', fiil 'güzelleştirmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: böğürtlen suyu kumaşa döküldü ve leke oldu | yaprakları suya batırıp lekenin çevresine bastı
@tohum: keloglan-0005
Ormanda büyük bir ağacın altında Keloğlan ilk kez kumaşa resim yapmayı deniyordu. Tatlı böğürtlenlerin mor suyunu büyük bir yaprağa koymuştu. Ama Keloğlan biraz sakardı, yaprağı düşürdü ve su beyaz kumaşa döküldü. Kumaşın ortasında büyük, yuvarlak bir leke oldu. Keloğlan lekeye baktı ve düşündü. Sonra küçük yaprakları kalan mor suya batırdı. Onları lekenin çevresine tek tek bastı. Leke kocaman bir çiçeğin ortası oldu. Keloğlan çok sevindi, çünkü lekeli kumaşı mor bir çiçekle güzelleştirmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı, yaprağı"
   - Cümle 3: «Ama Keloğlan biraz sakardı, yaprağı düşürdü ve su beyaz kumaşa döküldü.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "küçük yaprakları kalan mor suya batırdı"
   - Cümle 6: «Sonra küçük yaprakları kalan mor suya batırdı.»
   - Açıklama: Mor su yaprağıyla birlikte kumaşa dökülmüştü; geriye su kalması çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0005` birebir aynı, ardından `@onarim: f5584c9cb1df79d05c7a4d2221b171d4ee3b04ac`, sonra gövde.

### Hikâye 4: tohum keloglan-0008 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0008
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'patates', fiil 'yakalamak', sıfat 'tedbirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: patatesi hızlı attı ve arkadaşının kulesini yıktı | özür diledi ve kuleyi yeniden yaptı
@tohum: keloglan-0008
@degisim: tedbirli -> dikkatli
Şatonun bahçesinde Keloğlan ile Balkız patates atıp yakalama oyunu oynuyordu. Balkız çimlerin kenarında küçük taşlardan bir kule yapmıştı. Keloğlan bakmadan patatesi çok hızlı attı ve patates kuleyi yıktı. Balkız yıkılan kuleye baktı ve çok üzüldü. Keloğlan dürüst bir çocuktu ve hatasını saklamadı. "Ben yıktım, Balkız, özür dilerim," dedi Keloğlan. Sonra taşları tek tek toplayıp kuleyi yeniden yaptı. "Teşekkürler, Keloğlan, kule yine çok güzel," dedi Balkız. Oyuna döndüler ve Keloğlan patatesi bu kez dikkatli ve yavaş attı. Balkız patatesi kolayca yakaladı. Keloğlan bundan sonra bir şey atmadan önce hep etrafına baktı.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür diledi ve kuleyi yeniden yaptı"
   - Cümle 0 (plan satırı): «patatesi hızlı attı ve arkadaşının kulesini yıktı | özür diledi ve kuleyi yeniden yaptı»
   - Açıklama: Plan kuleyi Keloğlan'ın yaptığını söylüyor ama gövdede kuleyi Balkız yapıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve hatasını saklamadı"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve hatasını saklamadı.»
   - Açıklama: 'Hatasını saklamak' soyut ve mecazlı bir anlatım; küçük çocuk için somut değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Teşekkürler, Keloğlan, kule yine çok güzel"
   - Cümle 8: «"Teşekkürler, Keloğlan, kule yine çok güzel," dedi Balkız.»
   - Açıklama: Kuleyi Balkız kendisi yeniden yaptığı halde Keloğlan'a kule için teşekkür ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0008` birebir aynı, `@degisim: tedbirli -> dikkatli` (tutuyorsan), ardından `@onarim: b2421669e4d734a9a7628915280d4f729cfa008f`, sonra gövde.

### Hikâye 5: tohum keloglan-0009 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0009
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'trompet', fiil 'eğilmek', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: bardakta su yoktu ve çiçekler yana eğildi | bardağa su doldurdu ve çiçekler doğruldu
@tohum: keloglan-0009
@degisim: trompet -> çiçek
Keloğlan anasına bir sürpriz hazırlıyordu. Sabah topladığı sarı çiçekler masada bir bardakta duruyordu. Ama bardakta su yoktu ve çiçekler yana eğilmişti. Keloğlan hemen testiden bardağa su doldurdu. Az sonra çiçekler yavaş yavaş doğruldu. Tam o sırada anası açık kapıdan içeri girdi. "Keloğlan, orada ne saklıyorsun?" diye sordu anası. Keloğlan dürüst bir çocuktu ve hiçbir şeyi saklamadı. "Sana bir sürpriz hazırladım, anneciğim, bu çiçekler senin için!" dedi Keloğlan. Anası çiçekleri kokladı ve Keloğlan'a sıkıca sarıldı. Keloğlan çok sevindi, çünkü sürprizi anasını mutlu etmişti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Keloğlan hemen testiden bardağa su doldurdu"
   - Cümle 4: «Keloğlan hemen testiden bardağa su doldurdu.»
   - Açıklama: Sorun önemsiz ve tek hamlede hemen bitiyor; hikayenin geri kalanı sorunla ilgisiz sürprize geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve hiçbir şeyi saklamadı"
   - Cümle 8: «Keloğlan dürüst bir çocuktu ve hiçbir şeyi saklamadı.»
   - Açıklama: Tohumdaki dürüstlük özelliği plandaki sorunun (susuz çiçekler) çözümünde iş görmüyor, yalnız süs olarak anılıyor.
   - Açıklama: Tohumdaki dürüstlük özelliği sorunun (susuz çiçekler) çözümünde işe yaramıyor, yalnız sonradan anılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve hiçbir şeyi saklamadı"
   - Cümle 8: «Keloğlan dürüst bir çocuktu ve hiçbir şeyi saklamadı.»
   - Açıklama: Dürüstlük cümlesi olaya bir şey katmıyor ve sürpriz hazırlama fikriyle çelişir biçimde araya sokulmuş.
   - Açıklama: Sorun 5. cümlede çözülmüşken saklama sorusu ve dürüstlük ayrıntısı olaydan çıkmıyor ve sürpriz kurgusuyla işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0009` birebir aynı, `@degisim: trompet -> çiçek` (tutuyorsan), ardından `@onarim: e3e449969633d94e9b095ea28a0b7570e3e23f1a`, sonra gövde.

### Hikâye 6: tohum keloglan-0010 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0010
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'odun', fiil 'süpürmek', sıfat 'kırık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: kozalak büyük bir yaprak yığınına girdi ve kayboldu | eşeğin kuyruğuna bakıp dallarla yaprakları süpürdü
@tohum: keloglan-0010
@degisim: odun -> yaprak
Bir sabah Keloğlan ile eşeği Karakaçan ormanda kozalak oyunu oynuyordu. Keloğlan kozalağı ayağıyla Karakaçan'a doğru itti. Ama kozalak büyük bir yaprak yığınına girdi ve kayboldu. Yığın çok büyüktü. Keloğlan yeni şeyler öğrenmeyi severdi ve Karakaçan'a baktı. Karakaçan kuyruğunu sallıyor, yaprakları bir yana itiyordu. Keloğlan kırık dalları topladı ve kuyruk gibi bir süpürge yaptı. Onunla yaprakları sağa sola süpürdü. Az sonra kozalak göründü. "Buldum, Karakaçan!" dedi Keloğlan. Karakaçan başını salladı. Keloğlan çok sevindi, çünkü kozalağı bulmuştu ve oyun yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kozalak büyük bir yaprak yığınına girdi ve kayboldu"
   - Cümle 3: «Ama kozalak büyük bir yaprak yığınına girdi ve kayboldu.»
   - Açıklama: Kozalakla dolu bir ormanda tek bir kozalağın kaybolması önemsiz bir sorun; yerden başka bir kozalak almak yeterdi.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "öğrenmeyi severdi ve Karakaçan'a baktı"
   - Cümle 5: «Keloğlan yeni şeyler öğrenmeyi severdi ve Karakaçan'a baktı.»
   - Açıklama: Kalıcı bir özellik bildiren '-ardı' yan cümlesi ilgisiz bir eylemle 've' ile bağlanmış, cümle bozuk kurulmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0010` birebir aynı, `@degisim: odun -> yaprak` (tutuyorsan), ardından `@onarim: 33d6ea74e8ad6eda8f3e168f55a5f3860d95cb49`, sonra gövde.

### Hikâye 7: tohum keloglan-0011 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0011
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tarak', fiil 'yeşillenmek', sıfat 'nazik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: dedenin tarağı yolda cebinden düştü | aramayı bırakmadı ve tarağı bulup dedeye verdi
@tohum: keloglan-0011
Keloğlan ormanda Bilgecan Dede ile yürüyordu. Büyük ağaçlar yeni yeşillenmişti. Birden Dede durdu, çünkü tahta tarağı cebinden düşmüştü. "Keloğlan, tarağı birlikte arayalım mı?" diye sordu Bilgecan Dede. Keloğlan yerdeki yeşil otlara baktı, ama tarak görünmüyordu. Keloğlan aramayı bırakmadı. Yolda biraz geri yürüdü ve her yere baktı. Büyük bir ağacın dibinde tarağı buldu. Keloğlan dürüst bir çocuktu ve tarağı hemen sahibine götürdü. "Teşekkür ederim, Keloğlan, ne nazik bir çocuksun," dedi Bilgecan Dede. Dede tarağı cebine koydu ve gülümsedi. Sonra Keloğlan ile Bilgecan Dede ormanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tahta tarağı cebinden düşmüştü"
   - Cümle 3: «Birden Dede durdu, çünkü tahta tarağı cebinden düşmüştü.»
   - Açıklama: Tarağın neden düştüğü söylenmiyor ve kaybolan tarak sorunu zayıf kalıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 9: «Keloğlan dürüst bir çocuktu ve tarağı hemen sahibine götürdü.»
   - Açıklama: Tohumdaki dürüstlük özelliği, sahibinin birlikte aramasını istediği tarağı ona vermekle gösteriliyor; dürüstlük gerektiren bir seçim olmadığından özellik işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve tarağı hemen sahibine götürdü"
   - Cümle 9: «Keloğlan dürüst bir çocuktu ve tarağı hemen sahibine götürdü.»
   - Açıklama: Tarak sahibiyle birlikte aranırken dürüstlük işe yarar biçimde kullanılmıyor; özellik zaten 'aramayı bırakmadı' ile bir kez kullanılmışken ikinci kez anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0011` birebir aynı, ardından `@onarim: 3f08e3b0902d6d44246b4d469ebe3b0014ecd177`, sonra gövde.
