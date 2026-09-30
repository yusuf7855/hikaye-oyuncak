# Editör görevi (onarım): Keloğlan, onarım partisi 53

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar53.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar53.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0200 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0200
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mayo', fiil 'taramak', sıfat 'yeşil'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: annenin yeşil tarağı uzun otların arasına düştü | annesinden yardım istedi ve tarağı taşın yanında buldu
@tohum: keloglan-0200
@degisim: mayo -> tarak
Tepede Keloğlan ile anası elma yiyordu. Anası saçını taradı ama yeşil tarağı elinden kaydı. Tarak uzun otların arasına düştü ve kayboldu. Keloğlan otlara baktı ama tarağı göremedi. "Anneciğim, bana yardım eder misin? Tarağı nerede gördün?" diye sordu Keloğlan. "Şu büyük taşın yanına bak, Keloğlan," dedi anası. Keloğlan taşın yanına gitti. Orada sakarlık etti ve elmasını elinden düşürdü. Elma otların arasında yuvarlandı ve bir şeye çarpıp durdu. Keloğlan otları iki eliyle açtı. Yeşil tarak elmanın hemen yanındaydı. Keloğlan tarağı anasına verdi. "Teşekkürler, anneciğim, işte tarağın!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Orada sakarlık etti"
   - Cümle 9: «Orada sakarlık etti ve elmasını elinden düşürdü.»
   - Açıklama: 'Sakarlık etti' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elmasını elinden düşürdü"
   - Cümle 9: «Orada sakarlık etti ve elmasını elinden düşürdü.»
   - Açıklama: Tarak, yuvarlanan elmanın tesadüfen ona çarpmasıyla bulunuyor; çözüm sebepsiz bir kazayla geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Orada sakarlık etti ve elmasını elinden düşürdü"
   - Cümle 9: «Orada sakarlık etti ve elmasını elinden düşürdü.»
   - Açıklama: Tarağı bulduran şey rastlantıyla yuvarlanan elma; çözüm sebepsiz bir kazayla geliyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elma otların arasında yuvarlandı ve bir şeye çarpıp durdu"
   - Cümle 10: «Elma otların arasında yuvarlandı ve bir şeye çarpıp durdu.»
   - Açıklama: Keloğlan taşın yanını aramıyor, tarak elmanın rastgele yuvarlanmasıyla bulunuyor; çözüm sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0200` birebir aynı, `@degisim: mayo -> tarak` (tutuyorsan), ardından `@onarim: 5ff5cb4485551043f6cd58dfb2a9fc31b575b2e1`, sonra gövde.

### Hikâye 2: tohum keloglan-0201 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0201
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'yağmur', fiil 'yırtılmak', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: uçurtma dala çarptı ve kağıdı yırtıldı | dededen yardım istedi ve yırtığı bantla kapattı
@tohum: keloglan-0201
Yağmur yeni dinmişti ve hızlı bir rüzgar esiyordu. Keloğlan ormanda kağıttan uçurtmasını uçuruyordu. Birden uçurtma büyük bir ağacın dalına çarptı. Kağıdı ortadan yırtıldı ve uçurtma yere düştü. Keloğlan yırtığı nasıl kapatacağını bilmiyordu. Ağaçların arasında Bilgecan Dede yürüyordu. Keloğlan uçurtmayı dedeye götürdü ve ondan yardım istedi. Bilgecan Dede cebinden bir bant çıkardı. Yırtığın bir ucuna bandı yapıştırdı ve Keloğlan'a gösterdi. Keloğlan dikkatle izledi ve hemen öğrendi. Sonra öbür ucuna bandı kendisi yapıştırdı. Kağıt yine sağlam oldu. Keloğlan uçurtmayı rüzgara bıraktı ve uçurtma yükseldi. Keloğlan ile Bilgecan Dede uçurtmayı sırayla mutlu mutlu uçurdu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağaçların arasında Bilgecan Dede yürüyordu"
   - Cümle 6: «Ağaçların arasında Bilgecan Dede yürüyordu.»
   - Açıklama: Dede tam gerektiği anda sebepsizce beliriyor ve cebinden bant çıkararak çözümü getiriyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Bilgecan Dede cebinden bir bant çıkardı"
   - Cümle 8: «Bilgecan Dede cebinden bir bant çıkardı.»
   - Açıklama: Yapışkan bant masal köyü dünyasına uymayan çağdaş bir eşya; kartın kapalı dünyasında böyle bir eşya yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0201` birebir aynı, ardından `@onarim: 12644bc556aca25f39cb4424e45038106294421d`, sonra gövde.

### Hikâye 3: tohum keloglan-0202 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0202
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kazak', fiil 'büyütmek', sıfat 'yumuşacık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: ikisi de acıkmıştı ama tek sert elma vardı | elma düşüp ikiye ayrıldı ve paylaştılar
@tohum: keloglan-0202
@degisim: büyütmek -> bölmek
Serin bir rüzgar esiyordu. Keloğlan yumuşacık kazağıyla eşeğini ormanda gezdiriyordu. İkisi de çok acıkmıştı ama çantada tek bir elma vardı. Keloğlan elmayı eşeğiyle paylaşmak istedi. Ama sert elmayı elleriyle ikiye bölemedi. Eşek başını uzattı ve anırdı. Keloğlan elmayı ona göstermek için kaldırdı. Sakar Keloğlan elmayı yere düşürdü. Elma büyük bir taşa çarptı ve ikiye ayrıldı. "Bak, Karakaçan, şimdi iki parça elma var!" dedi Keloğlan. Parçaları kazağıyla temizledi ve büyük parçayı eşeğine verdi. Eşek elmasını yedi ve başını salladı. Keloğlan da küçük parçayı yedi ve güldü. Keloğlan bundan sonra yiyeceğini hep eşeğiyle paylaştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşacık kazağıyla eşeğini ormanda gezdiriyordu"
   - Cümle 2: «Keloğlan yumuşacık kazağıyla eşeğini ormanda gezdiriyordu.»
   - Açıklama: 'Kazağıyla' araç anlamı veriyor, eşeği kazakla gezdiriyor gibi okunuyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sakar Keloğlan elmayı yere düşürdü"
   - Cümle 8: «Sakar Keloğlan elmayı yere düşürdü.»
   - Açıklama: Elma Keloğlan'ın bilinçli bir çözümüyle değil, kazara düşüp taşa çarparak bölünüyor.
   - Açıklama: Sorunu Keloğlan bilerek çözmüyor, elma kazayla bölünüyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elma büyük bir taşa çarptı ve ikiye ayrıldı"
   - Cümle 9: «Elma büyük bir taşa çarptı ve ikiye ayrıldı.»
   - Açıklama: Çözüm sert elmayı bölme sorununa yönelmiyor; sorun rastlantıyla kendiliğinden çözülüyor.
   - Açıklama: Çözüm figürün sebebe yönelik bir eylemi değil, bir tesadüf.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elma büyük bir taşa çarptı ve ikiye ayrıldı"
   - Cümle 9: «Elma büyük bir taşa çarptı ve ikiye ayrıldı.»
   - Açıklama: Taş ve kaza çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0202` birebir aynı, `@degisim: büyütmek -> bölmek` (tutuyorsan), ardından `@onarim: 35dfd699fd4bacbb99d3ef9bc6ab52aefb9f1820`, sonra gövde.

### Hikâye 4: tohum keloglan-0203 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0203
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'buz', fiil 'yavaşlamak', sıfat 'temiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: rüzgar yüzünden eşek ıslığı duymadı | yeni ve yüksek bir ıslık çalmayı öğrendi
@tohum: keloglan-0203
Dışarıda buz gibi bir rüzgar esiyordu. Keloğlan evin bahçesinde eşeğiyle saklambaç oynuyordu. Keloğlan saklanıp ıslık çalınca eşek onu buluyordu. Bu kez büyük sepetin arkasına saklandı ve ıslık çaldı. Ama rüzgar çok gürültülüydü ve eşek ıslığı duymadı. Eşek bahçenin ortasında yavaşladı ve durdu. Keloğlan daha yüksek bir ıslık çalmayı öğrenmek istedi. Önce ellerini kovadaki temiz suyla yıkadı. Sonra iki parmağını ağzına koydu ve üfledi. İlk denemede ses çıkmadı ama sonra ıslık çok yüksek çıktı. Eşek sesi duydu ve hemen sepetin arkasına koştu. Karakaçan Keloğlan'ı buldu ve sevinçle anırdı. "Aferin, Karakaçan, yeni ıslığımı hemen duydun!" dedi Keloğlan.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dışarıda buz gibi bir rüzgar"
   - Cümle 1: «Dışarıda buz gibi bir rüzgar esiyordu.»
   - Açıklama: 'Buz gibi' bir benzetme/deyim, küçük çocuk için mecaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buz gibi bir rüzgar"
   - Cümle 1: «Dışarıda buz gibi bir rüzgar esiyordu.»
   - Açıklama: 'Buz gibi' benzetmeli bir deyimdir.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Keloğlan saklanıp ıslık çalınca eşek onu buluyordu.»
   - Açıklama: Sorun (eşeğin ıslığı duymaması) ancak 5. cümlede söyleniyor.
   - Açıklama: Sorun (eşeğin ıslığı duymaması) ilk üç cümlede değil ancak beşinci cümlede söyleniyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce ellerini kovadaki temiz suyla yıkadı"
   - Cümle 8: «Önce ellerini kovadaki temiz suyla yıkadı.»
   - Açıklama: Kova ve el yıkama sebepsiz beliriyor ve ıslığı öğrenmeye bir katkısı yok.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Karakaçan Keloğlan'ı buldu"
   - Cümle 12: «Karakaçan Keloğlan'ı buldu ve sevinçle anırdı.»
   - Açıklama: Eşeğin adı Karakaçan olduğu önceden söylenmeden birden kullanılıyor, kimin kastedildiği belli değil.
   - Açıklama: Karakaçan'ın eşek olduğu hiç söylenmeden adı birden kullanılıyor, kimi gösterdiği belli değil.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karakaçan Keloğlan'ı buldu"
   - Cümle 12: «Karakaçan Keloğlan'ı buldu ve sevinçle anırdı.»
   - Açıklama: Eşeğin adı hiç tanıtılmadan Karakaçan diye beliriyor ve okur yeni bir karakter sanabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0203` birebir aynı, ardından `@onarim: 53d0dbacff123fadfbc90e5de33db819a60574e3`, sonra gövde.

### Hikâye 5: tohum keloglan-0207 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0207
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'salıncak', fiil 'ovmak', sıfat 'sihirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: salıncağı kimse itmiyordu ve salıncak durdu | ayaklarıyla sallanmayı denedi ve öğrendi
@tohum: keloglan-0207
@degisim: sihirli -> parlak
Tepedeki büyük ağacın dalında bir salıncak vardı. Keloğlan salıncağa oturdu ve gemi oyunu oynadı. Salıncak onun gemisiydi ve gemi ileri gitmeliydi. Ama onu kimse itmiyordu ve salıncak hiç sallanmıyordu. Keloğlan tek başına sallanmayı bilmiyordu. Ellerindeki tozu ovdu ve ipleri sıkıca tuttu. Önce ayaklarını ileri uzattı, sonra geriye çekti. Salıncak biraz kıpırdadı. Keloğlan bunu birkaç kez denedi ve sallanmayı öğrendi. Gemi parlak güneşte ileri geri gitti. Keloğlan çok mutlu oldu, çünkü gemisi artık onun ayaklarıyla gidiyordu.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama onu kimse itmiyordu ve salıncak hiç sallanmıyordu.»
   - Açıklama: Salıncağı kimsenin itmemesi sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ellerindeki tozu ovdu"
   - Cümle 6: «Ellerindeki tozu ovdu ve ipleri sıkıca tuttu.»
   - Açıklama: Toz ovulmaz; 'ellerindeki tozu sildi' ya da 'ellerini ovdu' olmalı.
   - Açıklama: Toz ovulmaz; 'ellerini ovdu' ya da 'tozu silkti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0207` birebir aynı, `@degisim: sihirli -> parlak` (tutuyorsan), ardından `@onarim: b8e0cdad2b2fc9078c8296b99e85c6e895ee903d`, sonra gövde.

### Hikâye 6: tohum keloglan-0208 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0208
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'armut', fiil 'yaratmak', sıfat 'yavaş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: sepet devrildi ve armutlar çalılara dağıldı | her çalının altına tek tek baktı ve hepsini buldu
@tohum: keloglan-0208
Kuşlar ötüyordu. Keloğlan ormanda kendine yeni bir oyun yaratmıştı. Oyunda orman onun bahçesiydi ve o, bir ağacın altından on armut toplamıştı. Sepeti taşırken sepet bir ağacın köküne çarptı ve devrildi. Armutlar yuvarlandı ve çalıların arasına dağıldı. Dürüst ve azimli Keloğlan oyunu bırakmadı ve aramaya başladı. Yavaş adımlarla her çalının altına tek tek baktı. Sekiz armut buldu ama iki tanesi yoktu. Keloğlan biraz yorulmuştu ama aramaya devam etti. Sonunda son iki armudu büyük bir taşın arkasında buldu. Sepet yine on armutla doldu. Keloğlan bahçe oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "her çalının altına tek tek baktı ve hepsini buldu"
   - Cümle 0 (plan satırı): «sepet devrildi ve armutlar çalılara dağıldı | her çalının altına tek tek baktı ve hepsini buldu»
   - Açıklama: Gövdede son iki armut çalının altında değil taşın arkasında bulunuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kendine yeni bir oyun yaratmıştı"
   - Cümle 2: «Keloğlan ormanda kendine yeni bir oyun yaratmıştı.»
   - Açıklama: 'Yaratmak' bu bağlamda uygun değil; 'uydurmuştu' ya da 'bulmuştu' olmalı.
   - Açıklama: 'Yaratmak' fiili çocuk oyunu için yanlış anlamda; 'uydurmuştu' ya da 'bulmuştu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oyunda orman onun bahçesiydi"
   - Cümle 3: «Oyunda orman onun bahçesiydi ve o, bir ağacın altından on armut toplamıştı.»
   - Açıklama: Ormanın oyunda bahçe sayılması soyut bir benzetme ve 3 yaşındaki çocuğa uygun değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Sepeti taşırken sepet bir ağacın köküne çarptı"
   - Cümle 4: «Sepeti taşırken sepet bir ağacın köküne çarptı ve devrildi.»
   - Açıklama: Zarf-fiilin öznesi Keloğlan, ana cümlenin öznesi sepet; özne uyumsuz ve 'sepet' gereksiz tekrarlanıyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Sepeti taşırken sepet bir ağacın köküne çarptı ve devrildi"
   - Cümle 4: «Sepeti taşırken sepet bir ağacın köküne çarptı ve devrildi.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede ortaya çıkıyor.
6. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Armutlar yuvarlandı ve çalıların arasına dağıldı"
   - Cümle 5: «Armutlar yuvarlandı ve çalıların arasına dağıldı.»
   - Açıklama: Dağılan armutları arayıp toplamak önemsiz bir 'dağıldı, topladı, bitti' olayı.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Dürüst ve azimli Keloğlan oyunu bırakmadı"
   - Cümle 6: «Dürüst ve azimli Keloğlan oyunu bırakmadı ve aramaya başladı.»
   - Açıklama: Özellik kartın cümlesi gibi sayılıyor; dürüstlük olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0208` birebir aynı, ardından `@onarim: fd0439df580b8d85c0eb7539dbeb9c76da124660`, sonra gövde.

### Hikâye 7: tohum keloglan-0209 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0209
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'file', fiil 'çiğnemek', sıfat 'renkli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: ikisi topu aynı anda almak istedi ve top düştü | arkadaşını izleyip öğrendi ve sırayla attılar
@tohum: keloglan-0209
@degisim: çiğnemek -> atmak
Şatonun bahçesinde hafif bir rüzgar esiyordu. Keloğlan ile Balkız ağaca asılı bir fileye renkli bir top atıyordu. İkisi de topu aynı anda almak istedi ve top yere düştü. Balkız topu hep fileye atıyordu ama Keloğlan atamıyordu. Keloğlan Balkız'ın topu nasıl attığını öğrenmek istedi. Bu yüzden topu Balkız'a verdi ve onu izledi. Balkız topu iki eliyle yavaşça attı ve top fileye girdi. Sonra sıra Keloğlan'a geldi. Keloğlan da onun gibi attı ve top yine fileye girdi. İkisi sırayla atmaya devam etti ve çok eğlendi. Keloğlan bundan sonra Balkız'la hep sırayla oynadı.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Balkız topu hep fileye atıyordu ama Keloğlan atamıyordu"
   - Cümle 4: «Balkız topu hep fileye atıyordu ama Keloğlan atamıyordu.»
   - Açıklama: Topu aynı anda alma sorununun yanına Keloğlan'ın topu atamaması diye ikinci bir sorun ekleniyor.
   - Açıklama: Topu aynı anda alma sorununun yanına Keloğlan'ın atamaması diye ikinci bir sorun ekleniyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan Balkız'ın topu nasıl attığını öğrenmek istedi"
   - Cümle 5: «Keloğlan Balkız'ın topu nasıl attığını öğrenmek istedi.»
   - Açıklama: Çözüm topu aynı anda almaya çalışma sebebine değil, atmayı öğrenmeye yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0209` birebir aynı, `@degisim: çiğnemek -> atmak` (tutuyorsan), ardından `@onarim: f023e8b385d0dcdca1ca5229f5c1d7f9f953e82d`, sonra gövde.

### Hikâye 8: tohum keloglan-0211 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0211
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yoğurt', fiil 'tasarlamak', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: yediği yoğurt çok ekşiydi | kuru üzümler yoğurdun içine döküldü ve yoğurt tatlı oldu
@tohum: keloglan-0211
@degisim: tasarlamak -> yapmak
Ormanda sıcacık bir öğle vaktiydi. Keloğlan büyük bir ağacın altında bir kase yoğurt yiyordu. Ama yoğurt çok ekşiydi ve Keloğlan yüzünü buruşturdu. Çantasında bir avuç kuru üzüm de vardı. Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü. Bütün üzümler yoğurdun içine döküldü. Keloğlan önce şaşırdı. Sonra yeni bir şey denemek istedi ve yoğurtla üzümleri karıştırdı. Bir kaşık aldı ve tadına baktı. Yoğurt artık tatlı ve çok lezzetliydi. Böylece kendine üzümlü bir yoğurt yaptı. Kaşık kaşık bütün kaseyi bitirdi. Keloğlan çok sevindi, çünkü yeni ve güzel bir tat bulmuştu.
```

**Hakem bulguları (6):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çantasında bir avuç kuru üzüm de vardı"
   - Cümle 4: «Çantasında bir avuç kuru üzüm de vardı.»
   - Açıklama: Üzüm tam gerektiği anda sebepsizce beliriyor ve çözümü kendiliğinden getiriyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çantayı açarken onu kasenin üstüne"
   - Cümle 5: «Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü.»
   - Açıklama: 'Onu' zamirinin çantayı mı üzümleri mi gösterdiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çantayı açarken onu kasenin üstüne düşürdü"
   - Cümle 5: «Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü.»
   - Açıklama: 'onu' zamirinin çantayı mı üzümleri mi gösterdiği belli değil.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü"
   - Cümle 5: «Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü.»
   - Açıklama: Sorunu Keloğlan bilerek çözmüyor; üzümler kazayla dökülüyor.
   - Açıklama: Yoğurdu tatlandıran çözüm figürün kararıyla değil, kazara düşürmeyle geliyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü"
   - Cümle 5: «Sakar Keloğlan çantayı açarken onu kasenin üstüne düşürdü.»
   - Açıklama: Çözüm ekşiliğe yönelen bir eylem değil, rastlantı bir kaza.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yeni bir şey denemek istedi"
   - Cümle 8: «Sonra yeni bir şey denemek istedi ve yoğurtla üzümleri karıştırdı.»
   - Açıklama: Tohumdaki özellik sakarlık; yeni şey deneme merakı ikinci bir kart özelliği olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0211` birebir aynı, `@degisim: tasarlamak -> yapmak` (tutuyorsan), ardından `@onarim: 2822ea48d3cbdfe959c782d008855314890a81a7`, sonra gövde.

### Hikâye 9: tohum keloglan-0212 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0212
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'üzüm', fiil 'yerleştirmek', sıfat 'ılık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: düz tabaktaki üzümler yuvarlanıyor ve düşüyordu | üzümlerin kasede durduğunu öğrendi ve kaseye koydu
@tohum: keloglan-0212
Ilık bir rüzgar pencereden içeri esiyordu. Keloğlan evde sofra kurma oyunu oynuyordu. Oyunda masaya güzel bir üzüm tabağı koymak istiyordu. Ama tabak düzdü ve üzümler hep yuvarlanıyordu. Birçoğu yere düşüyordu. Keloğlan bunun nedenini öğrenmek istedi. Bir üzümü düz tabağa, bir üzümü de derin bir kaseye koydu. Tabaktaki üzüm yuvarlandı ama kasenin içindeki üzüm yerinde durdu. Keloğlan böylece yuvarlak üzümlerin derin kapta durduğunu öğrendi. Bütün üzümleri tek tek kaseye yerleştirdi. Bu kez hiçbir üzüm düşmedi. Sonra kaseyi masanın ortasına koydu. Keloğlan çok sevindi, çünkü oyunda güzel bir üzüm kasesi hazırlamıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bunun nedenini öğrenmek istedi"
   - Cümle 6: «Keloğlan bunun nedenini öğrenmek istedi.»
   - Açıklama: 'Neden' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0212` birebir aynı, ardından `@onarim: 46ff094e3958dfcbbd553427d058c2e1db572654`, sonra gövde.
