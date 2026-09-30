# Editör görevi (onarım): Keloğlan, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0123
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bitki', fiil 'şaşırtmak', sıfat 'hevesli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: bahçede bir sürü bitki vardı ve naneyi tanımıyordu | kitaptaki resimden naneyi öğrenip bir demet topladı
@tohum: keloglan-0123
Şatonun bahçesinde hafif bir rüzgar esiyordu. Keloğlan, naneyi çok seven Bilgecan Dede'yi bir demet nane ile şaşırtmak istiyordu. Ama bahçede bir sürü yeşil bitki vardı ve Keloğlan naneyi tanımıyordu. Dede bankta oturmuş kitap okuyordu. Biraz sonra kitabı Keloğlan'a verdi ve yüksek kapılara doğru yürüdü. Keloğlan kitabın sayfalarını çevirdi ve bir nane resmi buldu. Resme bakıp nane yaprağını iyice öğrendi. Sonra hevesli adımlarla bahçede dolaştı. Aynı yaprakları duvarın dibinde buldu ve küçük bir demet topladı. Dede geri gelince Keloğlan demeti ona uzattı. Dede çok şaşırdı ve naneyi sevinçle kokladı. Keloğlan çok sevindi, çünkü naneyi tek başına bulmuştu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sonra kitabı Keloğlan'a verdi"
   - Cümle 5: «Biraz sonra kitabı Keloğlan'a verdi ve yüksek kapılara doğru yürüdü.»
   - Açıklama: Dede kitabı sebepsizce verip gidiyor ve çözüm tesadüfen eline geliyor.
   - Açıklama: Dede kitabı sebepsizce verip gidiyor ve kitapta tam aranan nane resmi çıkarak çözümü sebepsizce getiriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "nane yaprağını iyice öğrendi"
   - Cümle 7: «Resme bakıp nane yaprağını iyice öğrendi.»
   - Açıklama: Yaprak öğrenilmez; 'tanıdı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra hevesli adımlarla bahçede"
   - Cümle 8: «Sonra hevesli adımlarla bahçede dolaştı.»
   - Açıklama: 'Hevesli adımlarla' küçük çocuğa uygun olmayan mecazlı bir anlatım.
   - Açıklama: 'Hevesli adımlar' mecazlı ve küçük çocuk için zor bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0123` birebir aynı, ardından `@onarim: 79988daa107e284329826ad00d74ff2e3ef42d09`, sonra gövde.

### Hikâye 2: tohum keloglan-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0124
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fıstık', fiil 'tanışmak', sıfat 'dağınık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: rüzgar taşları yapraklarla örttü ve saklanan paket kayboldu | düşen fıstıkları görüp doğru taşı buldu
@tohum: keloglan-0124
@degisim: tanışmak -> saklamak
Rüzgar tepede hafif hafif esiyordu. Sakar Keloğlan, Balkız için taşın altına fıstık saklarken birkaçını düşürmüştü. Ama rüzgar taşları yapraklarla örttü ve Keloğlan doğru taşı bulamadı. "Keloğlan, neden buraya geldik?" diye sordu Balkız. "Sana bir şey göstereceğim, biraz bekle," dedi Keloğlan. Keloğlan yaprakların arasına dikkatle baktı. Birden yerde dağınık duran üç fıstık gördü. Üçü de düz bir taşın yanındaydı. Keloğlan taşı kaldırdı ve fıstık paketini buldu. "İşte, en sevdiğin fıstıklar!" dedi Keloğlan. Balkız paketi aldı ve sevinçle güldü. Keloğlan da çok sevindi, çünkü sürprizi Balkız'ı mutlu etmişti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar taşları yapraklarla örttü"
   - Cümle 3: «Ama rüzgar taşları yapraklarla örttü ve Keloğlan doğru taşı bulamadı.»
   - Açıklama: Hafif hafif esen rüzgarın taşları yapraklarla örtüp düşen fıstıkları açıkta bırakması akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0124` birebir aynı, `@degisim: tanışmak -> saklamak` (tutuyorsan), ardından `@onarim: b7ed608c706f4e0df38f4517e036c0b219937638`, sonra gövde.

### Hikâye 3: tohum keloglan-0125 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0125
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'ayakkabı', fiil 'atlamak', sıfat 'zeki'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşeğin sırtındaki sepetin ipi bir çalıya takıldı | ipi çalının dallarından yavaş yavaş çözdü
@tohum: keloglan-0125
@degisim: ayakkabı -> çalı
Ormanda büyük ağaçların arasında dar bir yol vardı. Keloğlan ile zeki eşeği Karakaçan bu yoldan yürüyordu. Birden Karakaçan'ın sırtındaki sepetin ipi dikenli bir çalıya takıldı. Karakaçan ileri gidemedi. "İp çok karışmış, bu biraz uzun sürecek, Karakaçan," dedi dürüst Keloğlan. Karakaçan hiç kıpırdamadan bekledi. Keloğlan işini bırakmadı ve ipi dallardan yavaş yavaş çözdü. Sonunda ip çalıdan kurtuldu. Karakaçan sevinçle küçük bir kütüğün üstünden atladı. Sonra başını salladı ve Keloğlan'a sokuldu. Keloğlan bundan sonra dar yollarda sepetin ipine dikkat etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan işini bırakmadı"
   - Cümle 7: «Keloğlan işini bırakmadı ve ipi dallardan yavaş yavaş çözdü.»
   - Açıklama: 'İşini bırakmamak' deyimsel bir anlatım ve küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0125` birebir aynı, `@degisim: ayakkabı -> çalı` (tutuyorsan), ardından `@onarim: f7a99c2a3ce4f53d863ad53372894846bdb32c19`, sonra gövde.

### Hikâye 4: tohum keloglan-0126 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0126
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'bambu', fiil 'silmek', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kütük tozluydu ve halkalar iyi görünmüyordu | kütüğü suyla ıslatıp mendille sildi
@tohum: keloglan-0126
@degisim: bambu -> kütük
Keloğlan ile anası ormanda kesilmiş büyük bir kütüğün yanına geldi. Keloğlan kütüğün üstünde ince halkalar fark etti. Halkaları saymak istedi ama kütük tozluydu ve halkalar iyi görünmüyordu. Keloğlan tozu ıslatmak için su şişesini açtı. Biraz sakardı ve şişe elinden kaydı. Bütün su kütüğün üstüne döküldü ve tozu ıslattı. Keloğlan anasından bir mendil istedi. Anası ona yepyeni bir mendil verdi. Keloğlan ıslak kütüğü mendille sildi. Toz gitti ve bütün halkalar göründü. Keloğlan halkaları tek tek saydı ve tam yirmi halka buldu. Sonra ikisi ormanda başka kütükler aramaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Biraz sakardı ve şişe"
   - Cümle 5: «Biraz sakardı ve şişe elinden kaydı.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sakardı ve şişe elinden kaydı"
   - Cümle 5: «Biraz sakardı ve şişe elinden kaydı.»
   - Açıklama: Kütüğü ıslatma işini figürün eylemi değil sebepsiz bir kaza yapıyor.
   - Açıklama: Kütüğü ıslatma işini figür değil bir kaza yapıyor; çözüm tesadüfle geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0126` birebir aynı, `@degisim: bambu -> kütük` (tutuyorsan), ardından `@onarim: 07e46697741aa63a15f820682ed382b259e937a6`, sonra gövde.

### Hikâye 5: tohum keloglan-0127 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0127
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'cetvel', fiil 'katmak', sıfat 'yaratıcı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ağaçtan garip bir tık tık sesi geldi | ağaca baktı ve dala takılan kaşığı buldu
@tohum: keloglan-0127
@degisim: cetvel -> kaşık
Rüzgar ormanda sert esiyordu. Keloğlan dallarla yaratıcı bir oyun oynuyordu ve küçük bir ev yapıyordu. Birden yakındaki bir ağaçtan garip bir "tık tık" sesi geldi. Keloğlan bu sesi çok merak etti ve ağaca yürüdü. Alçak bir dala tahta bir kaşık takılmıştı. Rüzgar kaşığı sallıyor ve ağaca çarpıyordu. Keloğlan kaşığı daldan çıkardı. Kaşık çok güzeldi ama onun değildi. Keloğlan dürüst bir çocuktu ve kaşığı kendine almadı. Sahibi kolayca görsün diye onu yolun kenarındaki büyük taşa koydu. Sonra küçük evine döndü ve ona bir dal daha kattı. Keloğlan çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yaratıcı bir oyun oynuyordu"
   - Cümle 2: «Keloğlan dallarla yaratıcı bir oyun oynuyordu ve küçük bir ev yapıyordu.»
   - Açıklama: 'Yaratıcı' soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dallarla yaratıcı bir oyun"
   - Cümle 2: «Keloğlan dallarla yaratıcı bir oyun oynuyordu ve küçük bir ev yapıyordu.»
   - Açıklama: 'Yaratıcı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yakındaki bir ağaçtan garip"
   - Cümle 3: «Birden yakındaki bir ağaçtan garip bir "tık tık" sesi geldi.»
   - Açıklama: Ağaçtan gelen zararsız bir ses gerçek bir sorun değil, çocuğun önemseyeceği bir güçlük yaratmıyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kaşık çok güzeldi ama onun değildi"
   - Cümle 8: «Kaşık çok güzeldi ama onun değildi.»
   - Açıklama: Ses sorunu çözüldükten sonra kaşığın sahibine ulaştırılması diye ikinci bir sorun açılıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kaşık çok güzeldi ama onun değildi"
   - Cümle 8: «Kaşık çok güzeldi ama onun değildi.»
   - Açıklama: Kaşığın sahibine bırakılması sorundan çıkmayan ek bir olay dizisi açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0127` birebir aynı, `@degisim: cetvel -> kaşık` (tutuyorsan), ardından `@onarim: d7c54403d8dcd3eed2cd12c8fdfcf09fb694ac07`, sonra gövde.

### Hikâye 6: tohum keloglan-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0128
- yer: dağ (Köyün yakınındaki tepe.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fındık', fiil 'sıkışmak', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: ahşap kutunun kapağı ıslanmış ve sıkışmıştı | kutuyu taşa hafif hafif vurdu ve kapak açıldı
@tohum: keloglan-0128
Tepede hava serin ve sessizdi. Keloğlan orada oturmuş güneşin doğmasını bekliyordu. Yanındaki ahşap kutu ıslanmıştı ve kapağı sıkışmıştı. Kutunun içinde Keloğlan'ın fındıkları vardı. Keloğlan kapağı çekti ama açamadı. Sonra kutuyu düz bir taşa hafif hafif vurdu. Kapak yavaşça açıldı. Ama Keloğlan biraz sakardı ve kutuyu çok eğdi. Birkaç fındık otların üstüne döküldü. Keloğlan güldü ve fındıkları tek tek topladı. Tam o sırada güneş tepenin arkasından doğdu. Keloğlan fındıklarını yiyerek güneşi mutlu mutlu seyretti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Yanındaki ahşap kutu ıslanmıştı"
   - Cümle 3: «Yanındaki ahşap kutu ıslanmıştı ve kapağı sıkışmıştı.»
   - Açıklama: Hava serin ve sessizken kutunun neden ıslandığı söylenmiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ama Keloğlan biraz sakardı ve kutuyu çok eğdi"
   - Cümle 8: «Ama Keloğlan biraz sakardı ve kutuyu çok eğdi.»
   - Açıklama: Tohumdaki sakarlık sorun çözüldükten sonra süs olarak geçiyor, işe yaramıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Birkaç fındık otların üstüne döküldü"
   - Cümle 9: «Birkaç fındık otların üstüne döküldü.»
   - Açıklama: Kapak sorunu çözüldükten sonra fındıkların dökülmesiyle ikinci bir sorun açılıyor.
   - Açıklama: Kapak sorunu çözüldükten sonra fındıkların dökülmesiyle ikinci bir sorun çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0128` birebir aynı, ardından `@onarim: 329e3de3f1ab75d82bb894aa14deaa7f778f1e52`, sonra gövde.

### Hikâye 7: tohum keloglan-0129 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0129
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kolye', fiil 'içmek', sıfat 'kokulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: dedenin kolyesini otların arasına düşürdü | özür diledi, otlara baktı ve kolyeyi buldu
@tohum: keloglan-0129
@degisim: içmek -> aramak
Rüzgar ormanda hafif hafif esiyordu. Bilgecan Dede, Keloğlan'a yeni yaptığı düdüklü bir kolyeyi gösterdi. Keloğlan biraz sakardı ve kolyeyi kokulu otların arasına düşürdü. Otlar çok sıktı ve kolye hiç görünmüyordu. "Özür dilerim, Dede, kolyeni düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan, onu bulabiliriz," dedi Dede. Keloğlan eğildi ve otları yavaşça aradı. Sonunda otların arasında küçük düdüğü gördü. Onu dikkatle aldı ve iki eliyle Dede'ye verdi. Dede düdüğü çaldı ve ormanda ince bir ses çıktı. "Teşekkürler, Keloğlan, kolyemi sen buldun!" dedi Bilgecan Dede.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve"
   - Cümle 3: «Keloğlan biraz sakardı ve kolyeyi kokulu otların arasına düşürdü.»
   - Açıklama: 'Sakar' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0129` birebir aynı, `@degisim: içmek -> aramak` (tutuyorsan), ardından `@onarim: 14570851f5ae30f51333ca7a731e4994a8a0db77`, sonra gövde.

### Hikâye 8: tohum keloglan-0130 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0130
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'perde', fiil 'gitmek', sıfat 'bomboş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: yağmur başladı ve kuru bir yer yoktu | düşen fındıkları izleyip ağaçta kuru bir delik buldu
@tohum: keloglan-0130
@degisim: perde -> sepet
Ormanda büyük ağaçların altında Keloğlan sepetine fındık topluyordu. Birden yağmur yağmaya başladı ve Keloğlan'ın başı ıslandı. Keloğlan yağmurdan saklanacak kuru bir yer aradı. Ama Keloğlan biraz sakardı ve acele ederken sepeti elinden düşürdü. Fındıklar yere döküldü ve kocaman bir ağaca doğru yuvarlandı. Keloğlan fındıkların peşinden gitti. Ağacın gövdesinde büyük bir delik vardı ve içi bomboştu. Keloğlan fındıkları topladı ve deliğin içine girip oturdu. Dışarıda yağmur yağmaya devam etti. Ama Keloğlan içeride hiç ıslanmadı. Biraz sonra yağmur dindi ve güneş çıktı. Keloğlan sepetini koluna taktı ve mutlu mutlu fındık toplamaya devam etti.
```

**Hakem bulguları (7):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "sepeti elinden düşürdü"
   - Cümle 4: «Ama Keloğlan biraz sakardı ve acele ederken sepeti elinden düşürdü.»
   - Açıklama: Yağmur sorununun yanına dökülen fındıklar diye ikinci bir sorun ekleniyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "acele ederken sepeti elinden düşürdü"
   - Cümle 4: «Ama Keloğlan biraz sakardı ve acele ederken sepeti elinden düşürdü.»
   - Açıklama: Kuru yeri Keloğlan bulmuyor, sepetin kazara düşmesiyle fındıklar onu deliğe götürüyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Fındıklar yere döküldü ve kocaman bir ağaca doğru yuvarlandı"
   - Cümle 5: «Fındıklar yere döküldü ve kocaman bir ağaca doğru yuvarlandı.»
   - Açıklama: Kuru yeri Keloğlan değil, rastlantıyla yuvarlanan fındıklar buluyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kocaman bir ağaca doğru yuvarlandı"
   - Cümle 5: «Fındıklar yere döküldü ve kocaman bir ağaca doğru yuvarlandı.»
   - Açıklama: Çözümü getiren delikli ağaç sebepsizce fındıkların yuvarlanmasıyla ortaya çıkıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan fındıkların peşinden gitti"
   - Cümle 6: «Keloğlan fındıkların peşinden gitti.»
   - Açıklama: Çözüm kuru yer aramaya yönelmiyor, fındıkların peşinden giderken tesadüfen geliyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağacın gövdesinde büyük bir delik vardı"
   - Cümle 7: «Ağacın gövdesinde büyük bir delik vardı ve içi bomboştu.»
   - Açıklama: Çözüm sakarlıkla gelen bir rastlantıyla sebepsizce ortaya çıkıyor.
7. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "deliğin içine girip oturdu"
   - Cümle 8: «Keloğlan fındıkları topladı ve deliğin içine girip oturdu.»
   - Açıklama: Yağmurda bilinmeyen bir ağaç kovuğunun içine girmek çocuğun taklit edebileceği riskli bir davranıştır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0130` birebir aynı, `@degisim: perde -> sepet` (tutuyorsan), ardından `@onarim: a1d65d096071874b9486eb6b091aa4fecbc84761`, sonra gövde.

### Hikâye 9: tohum keloglan-0131 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0131
- yer: dağ (Köyün yakınındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'avokado', fiil 'göndermek', sıfat 'minicik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: topu çok hızlı attı ve arkadaşı tutamadı | özür diledi ve topu yavaş atmayı öğrendi
@tohum: keloglan-0131
@degisim: avokado -> top
Bir sabah Keloğlan ile Balkız tepede top oynuyordu. Balkız minicik kırmızı bir top getirmişti. Keloğlan topu Balkız'a çok hızlı gönderiyordu ve Balkız hiç tutamıyordu. Top hep çimenlere yuvarlanıyordu. Balkız topu getirmekten yoruldu ve oturdu. "Özür dilerim, Balkız, topu çok hızlı attım," dedi Keloğlan. Balkız topu oturduğu yerden ona yavaşça ve aşağıdan attı. Keloğlan topu kolayca tuttu ve böyle atmayı öğrenmek istedi. Sonra topu o da yavaşça ve aşağıdan attı. Balkız bu kez topu hemen yakaladı. "Yakaladım, Keloğlan, şimdi oyun çok eğlenceli!" dedi Balkız.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Balkız topu oturduğu yerden ona yavaşça ve aşağıdan attı"
   - Cümle 7: «Balkız topu oturduğu yerden ona yavaşça ve aşağıdan attı.»
   - Açıklama: Yavaş atma çözümünü Keloğlan değil Balkız buluyor ve gösteriyor; Keloğlan yalnız onu taklit ediyor.
   - Açıklama: Doğru atış yolunu Balkız gösteriyor; Keloğlan çözümü kendisi bulmuyor, yalnız taklit ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0131` birebir aynı, `@degisim: avokado -> top` (tutuyorsan), ardından `@onarim: be8d4a537acc12828cd9b89224d2e250aaec3387`, sonra gövde.

### Hikâye 10: tohum keloglan-0133 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0133
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tartı', fiil 'gülmek', sıfat 'oynak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: yeni tartı taşların üstünde sallanıyordu | tartıyı düz bir yere koydu
@tohum: keloglan-0133
Rüzgar büyük ağaçların arasında hafifçe esiyordu. Keloğlan ormanda Bilgecan Dede'nin yeni yaptığı tartıyı gördü. Ama tartı taşların üstünde oynak duruyor ve hep sallanıyordu. Dede cevizleri köyün çocukları için iki torbaya eşit koymak istiyordu. "Dede, bu tartı neden sallanıyor?" diye sordu Keloğlan. "Tartı yalnız düz bir yerde iyi çalışır," dedi Bilgecan Dede. Keloğlan bunu hemen öğrendi ve etrafına baktı. Tartıyı taşlardan aldı ve düz bir yere koydu. Tartı artık hiç sallanmadı. Dede cevizleri tarttı ve iki torba tam eşit oldu. Keloğlan ile Dede birlikte güldü ve torbaları mutlu mutlu bağladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iki torbaya eşit koymak"
   - Cümle 4: «Dede cevizleri köyün çocukları için iki torbaya eşit koymak istiyordu.»
   - Açıklama: 'Eşit' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan bunu hemen öğrendi"
   - Cümle 7: «Keloğlan bunu hemen öğrendi ve etrafına baktı.»
   - Açıklama: Bir cümleyi duymak için 'öğrendi' demek bu bağlamda uygun değil.
   - Açıklama: 'Öğrendi' burada anlamca uygun değil; 'anladı' olmalı ve soyut kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0133` birebir aynı, ardından `@onarim: 21524e778fe87fde9f43c696abf009682ba54854`, sonra gövde.

### Hikâye 11: tohum keloglan-0134 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0134
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'fidan', fiil 'görüşmek', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar deliğin önündeki fidana çarpıyordu | yüksekten atmayı öğrendi ve kozalağı deliğe attı
@tohum: keloglan-0134
@degisim: görüşmek -> fırlatmak
Keloğlan ormanda komik bir kozalak oyunu oynuyordu. Kozalakları büyük bir ağacın dibindeki deliğe atmaya çalışıyordu. Ama deliğin önünde küçük bir fidan vardı ve kozalaklar hep ona çarpıyordu. Keloğlan kibar bir çocuktu ve fidanın dallarını kırmak istemedi. Durdu ve kozalağı fidanın üstünden atmayı öğrenmek istedi. Bu kez kozalağı yukarı doğru, yüksekten fırlattı. Kozalak fidanın üstünden geçti ama delikten uzağa düştü. Keloğlan ikinci kozalağı biraz daha yavaş fırlattı. Bu kez kozalak tam deliğin içine girdi! Keloğlan sevinçle güldü ve ellerini çırptı. Sonra oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan kibar bir çocuktu"
   - Cümle 4: «Keloğlan kibar bir çocuktu ve fidanın dallarını kırmak istemedi.»
   - Açıklama: 'Kibar' fidanın dallarını kırmamak için yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan kibar bir çocuktu"
   - Cümle 4: «Keloğlan kibar bir çocuktu ve fidanın dallarını kırmak istemedi.»
   - Açıklama: Tohumdaki özellik öğrenmek; kibarlık karttaki özellikler alanında olmayan ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik öğrenmeyi sevmek; kartın özellikler alanında olmayan kibarlık ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0134` birebir aynı, `@degisim: görüşmek -> fırlatmak` (tutuyorsan), ardından `@onarim: 958c480b4298953884976220615eefc65f403b14`, sonra gövde.

### Hikâye 12: tohum keloglan-0135 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0135
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kabak', fiil 'ışıldamak', sıfat 'yalnız'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: sürpriz için yıkanacak kabak çok ağırdı | kabağı yerde iterek kovaya götürdü
@tohum: keloglan-0135
Bir sabah Keloğlan anasına bir sürpriz hazırlamak istedi. Anası dışarıdaydı ve biraz sonra kabak tatlısı yapacaktı. Keloğlan büyük kabağı yıkamak istedi, ama kabak çok ağırdı. Onu yalnız başına kucağına alıp su dolu kovanın yanına taşıyamadı. Keloğlan kabağı yan yatırdı ve eliyle hafifçe itti. Kabak top gibi kolayca yuvarlandı. Keloğlan böylece ağır bir şeyi kaldırmadan götürmeyi öğrendi. Kabağı böyle kovanın yanına kadar getirdi ve bezle yıkadı. Temiz kabak kovanın yanında ışıldadı. Az sonra anası içeri girdi ve kabağı gördü. Anası çok sevindi, çünkü Keloğlan kabağı onun için hazırlamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Temiz kabak kovanın yanında ışıldadı"
   - Cümle 9: «Temiz kabak kovanın yanında ışıldadı.»
   - Açıklama: Kabak ışıldamaz; fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kabak kovanın yanında ışıldadı"
   - Cümle 9: «Temiz kabak kovanın yanında ışıldadı.»
   - Açıklama: 'Işıldamak' küçük çocuğun bilmeyeceği edebi bir kelime ve kabağa pek uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0135` birebir aynı, ardından `@onarim: 3cdef6a11bc2c7896aecddd09d91c94d1af11477`, sonra gövde.
