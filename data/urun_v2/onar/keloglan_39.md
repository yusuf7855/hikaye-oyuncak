# Editör görevi (onarım): Keloğlan, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0109 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0109
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'saksı', fiil 'seçmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: cevizler saksının sert kenarına çarpıp dışarı düşüyordu | saksıyı yere yatırdı ve cevizleri yerden yuvarladı
@tohum: keloglan-0109
Keloğlan evde eğlenceli bir oyun oynuyordu. En büyük boş saksıyı seçti ve duvarın dibine koydu. Ama attığı cevizler saksının sert kenarına çarpıp dışarı düşüyordu. Keloğlan yere bir ip koymuştu ve cevizleri ipin arkasından atıyordu. Saksıya yaklaşmak çok kolaydı. Ama Keloğlan dürüst davrandı, ipin arkasında kaldı ve biraz düşündü. Sonra saksıyı yere yan yatırdı. Bu sefer cevizi atmadı, yerden yavaşça yuvarladı. Ceviz yerde ilerledi ve içeri girdi. Keloğlan öteki cevizleri de tek tek yuvarladı. Hepsi saksının içinde toplandı. Keloğlan çok sevindi, çünkü bütün cevizleri ipin arkasından saksıya sokmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Saksıya yaklaşmak çok kolaydı"
   - Cümle 5: «Saksıya yaklaşmak çok kolaydı.»
   - Açıklama: Hile yapma ayartısı sorunla bağsız bir yan konu olarak araya giriyor ve olayı ilerletmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0109` birebir aynı, ardından `@onarim: ba875cf95d811ca59458701da16656c62600fa95`, sonra gövde.

### Hikâye 2: tohum keloglan-0111 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0111
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kaşık', fiil 'hazırlanmak', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ormanda nereden geldiği bilinmeyen bir ses vardı | aramayı bırakmadı ve sesin kendi çantasından geldiğini buldu
@tohum: keloglan-0111
Hafif bir rüzgar esiyordu. Keloğlan çantasını alçak bir dala astı ve yemeğe hazırlandı. Birden yakından ince bir ses geldi. Keloğlan bu sesin nereden geldiğini çok merak etti. Büyük bir kayanın arkasına baktı ama hiçbir şey göremedi. Biraz mutsuz oldu. Ama dürüst ve azimli Keloğlan aramayı bırakmadı. Durdu ve sesi dikkatle dinledi. Sonunda sesin kendi çantasından geldiğini buldu. Rüzgar çantayı sallıyordu. İçindeki kaşık da bardağa çarpıp ses çıkarıyordu. Keloğlan güldü ve kaşığı çıkardı. Ses hemen kesildi. Keloğlan bundan sonra bir sesi merak edince onu bulana kadar aradı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama dürüst ve azimli Keloğlan"
   - Cümle 7: «Ama dürüst ve azimli Keloğlan aramayı bırakmadı.»
   - Açıklama: 'Dürüst ve azimli' soyut kelimeler; 'dürüst' olayla ilgisiz kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0111` birebir aynı, ardından `@onarim: f98203daf842abdaacebacc2a3d121b0ab5f1b75`, sonra gövde.

### Hikâye 3: tohum keloglan-0112 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0112
- yer: dağ (Köyün yakınındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çam', fiil 'fışkırmak', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: acele edip düğmeye sert bastı ve dedeyi ıslattı | özür diledi ve düğmeye yavaşça bastı
@tohum: keloglan-0112
@degisim: kırılgan -> yeni
Bir sabah Keloğlan ile Bilgecan Dede tepedeydi. Dede bir çam ağacını sulamak için yeni bir alet getirmişti. Keloğlan acele etti ve aletin düğmesine çok sert bastı. Su birden fışkırdı ve Dede'nin yüzünü ıslattı. "Özür dilerim, Bilgecan Dede, bu benim hatamdı," dedi Keloğlan. Dede gülümsedi ve yüzünü sildi. Keloğlan aleti kullanmayı öğrenmek istedi. "Bilgecan Dede, bana doğrusunu gösterir misin?" diye sordu Keloğlan. Bilgecan Dede düğmeye parmağıyla hafifçe dokundu. Keloğlan da tıpkı onun gibi yaptı. Bu kez su yavaşça ağacın dibine aktı. Keloğlan çok sevindi, çünkü Dede ona hiç kızmamıştı.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür diledi ve düğmeye yavaşça bastı"
   - Cümle 0 (plan satırı): «acele edip düğmeye sert bastı ve dedeyi ıslattı | özür diledi ve düğmeye yavaşça bastı»
   - Açıklama: Planda Keloğlan özür diliyor ama gövdede hiç özür dilemiyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Keloğlan çok sevindi, çünkü Dede ona hiç kızmamıştı"
   - Cümle 12: «Keloğlan çok sevindi, çünkü Dede ona hiç kızmamıştı.»
   - Açıklama: Son cümle aleti doğru kullanmayı öğrenme hedefine değil, geriye dönük başka bir konuya bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0112` birebir aynı, `@degisim: kırılgan -> yeni` (tutuyorsan), ardından `@onarim: fec2a7cfeb7ccd1a166841e7236722782423750b`, sonra gövde.

### Hikâye 4: tohum keloglan-0113 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0113
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'basamak', fiil 'hızlanmak', sıfat 'serin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: ağaçların arasından tık diye bir ses geldi | sesin geldiği ağaca gitti ve anasına sordu
@tohum: keloglan-0113
@degisim: basamak -> kozalak
Ormanda serin bir rüzgar esiyordu. Keloğlan anasıyla büyük ağaçların altında yürüyordu. Birden ileriden tık diye bir ses geldi. Keloğlan sesin ne olduğunu öğrenmek istedi. Keloğlan hızlandı ve sesin geldiği ağacın yanına gitti. Ağacın altında kahverengi, küçük şeyler vardı. Keloğlan yerden bir tane aldı ve anasına gösterdi. "Anneciğim, bu nedir?" diye sordu Keloğlan. "Bu bir kozalak, rüzgar esince dallardan düşüyor," dedi anası. O sırada bir kozalak daha tık diye yere düştü. Keloğlan çok sevindi, çünkü sesi yapan kozalakları bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden ileriden tık diye bir ses geldi"
   - Cümle 3: «Birden ileriden tık diye bir ses geldi.»
   - Açıklama: Ortada gerçek bir sorun yok; yalnız merak uyandıran bir ses var ve çözülecek bir dert kurulmuyor.
   - Açıklama: Ağaçtan gelen bir ses gerçek bir sorun değil, yalnız bir merak; çözülecek bir dert kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0113` birebir aynı, `@degisim: basamak -> kozalak` (tutuyorsan), ardından `@onarim: b44b41364db0b59d1606dbc447a635ca6dc85c83`, sonra gövde.

### Hikâye 5: tohum keloglan-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0114
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'taç', fiil 'serinletmek', sıfat 'bulutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: sıcaktan tacın çiçekleri aşağı eğildi | tacı soğuk suya koyup çiçekleri serinletti
@tohum: keloglan-0114
Hava bulutluydu ama çok sıcaktı. Keloğlan evde Balkız için çiçeklerden bir taç yapmıştı. Ama sıcaktan tacın çiçekleri aşağı eğildi. Tam o sırada Balkız kapıdan içeri girdi. "Ne saklıyorsun, Keloğlan?" diye sordu Balkız. Keloğlan dürüst davrandı ve tacı hemen gösterdi. "Senin için yaptım ama sıcakta bozuldu," dedi Keloğlan. "Bence çiçekler susamış," dedi Balkız. Keloğlan hemen bir kova soğuk su getirdi. Tacı suya koydu ve çiçekleri serinletti. Biraz sonra çiçekler yeniden yukarı kalktı. Keloğlan tacı Balkız'ın başına taktı. "Çok güzel bir taç, teşekkür ederim, Keloğlan!" dedi Balkız.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı ve tacı hemen gösterdi"
   - Cümle 6: «Keloğlan dürüst davrandı ve tacı hemen gösterdi.»
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız tacı göstermek için anılıyor ve sorunun çözümüne yaramıyor; çözümü Balkız'ın fikri ve su getiriyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bence çiçekler susamış"
   - Cümle 8: «"Bence çiçekler susamış," dedi Balkız.»
   - Açıklama: Çözüm fikrini yan karakter Balkız veriyor; Keloğlan yalnız uyguluyor.
   - Açıklama: Çözümün anahtar fikrini Keloğlan sormadan Balkız veriyor; figür yalnız uyguluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0114` birebir aynı, ardından `@onarim: 872b8144454c047b31b83f85e27992e9df732379`, sonra gövde.

### Hikâye 6: tohum keloglan-0115 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0115
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kıyafet', fiil 'güneşlenmek', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: resim için yeşil boya yoktu | lekeyi görüp sarı ile maviyi karıştırdı
@tohum: keloglan-0115
Tepede hafif bir rüzgar esiyordu. Keloğlan'ın eşeği Karakaçan otların üstünde güneşleniyordu. Keloğlan ilk kez resim yapıyordu, ama yeşil boyası yoktu. Elinde yalnız mavi ve sarı boya vardı. Keloğlan resimdeki otlar için ne yapacağını düşündü. Sakar Keloğlan birden sarı boyayı elinden düşürdü. Sarı boya mavi kıyafetine damladı ve orada yeşil bir leke oldu. Keloğlan bunu görünce sarı ve mavi boyayı fırçayla karıştırdı. Yeşil bir boya oldu ve Keloğlan güldü. Hemen resimdeki otları yeşile boyadı. Karakaçan resme bakıp başını salladı. Keloğlan bundan sonra yeşil boya için sarı ve maviyi karıştırdı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan birden sarı boyayı elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan birden sarı boyayı elinden düşürdü.»
   - Açıklama: Çözüm figürün düşünmesinden değil rastlantı bir kazadan geliyor.
   - Açıklama: Çözüm fikri sebepsiz bir kazayla, rastlantıyla geliyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Keloğlan bundan sonra yeşil boya için sarı ve maviyi karıştırdı"
   - Cümle 12: «Keloğlan bundan sonra yeşil boya için sarı ve maviyi karıştırdı.»
   - Açıklama: 'Bundan sonra' süreklilik bildirdiği için fiil '-ırdı' biçiminde olmalı; 'karıştırdı' uyumsuz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0115` birebir aynı, ardından `@onarim: 58d2b58d866bcbe997d8df366b13f6934187876e`, sonra gövde.

### Hikâye 7: tohum keloglan-0116 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0116
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kereviz', fiil 'küçültmek', sıfat 'ferah'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: anası acıkmıştı ve sert kereviz ikiye kırılmadı | kerevizi taşa vurdu ve ikiye ayırdı
@tohum: keloglan-0116
@degisim: ferah -> düz
Keloğlan anasıyla ormanda büyük ve düz bir taşa oturdu. Anası çok acıkmıştı, ama çantada yalnız bir kereviz vardı. Keloğlan onu anasıyla paylaşmak istedi, ama kereviz çok sertti. Kerevizi küçültmek için iki eliyle bükmeye çalıştı. Ama kereviz hiç kırılmadı. Sonra sakar Keloğlan kerevizi elinden düşürdü. Kereviz taşa çarptı ve ortası biraz çatladı. Keloğlan bunu görünce kerevizi bir kez daha taşa vurdu. Kereviz çat diye ikiye ayrıldı. "Anneciğim, bu parça senin, bu da benim," dedi Keloğlan. Anası parçasını aldı ve Keloğlan'ı öptü. İkisi kerevizi mutlu mutlu yedi. "Teşekkürler, Keloğlan, birlikte yemek çok güzel!" dedi anası.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ama kereviz çok sertti"
   - Cümle 3: «Keloğlan onu anasıyla paylaşmak istedi, ama kereviz çok sertti.»
   - Açıklama: Art arda cümlelerde 'ama' bağlacı ve 'anasıyla' gereksiz yere tekrarlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra sakar Keloğlan kerevizi elinden düşürdü"
   - Cümle 6: «Sonra sakar Keloğlan kerevizi elinden düşürdü.»
   - Açıklama: Çözüm Keloğlan'ın düşüncesinden değil rastlantı bir düşürmeden sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0116` birebir aynı, `@degisim: ferah -> düz` (tutuyorsan), ardından `@onarim: d0476ccc67e952e516a1c7a33210099313192423`, sonra gövde.

### Hikâye 8: tohum keloglan-0117 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0117
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'fide', fiil 'gerinmek', sıfat 'kısa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: fidan rüzgarda yana yatıyordu ve dallar kısaydı | ağaçların arasında uzun bir dal buldu ve fidanı bağladı
@tohum: keloglan-0117
@degisim: fide -> fidan
Bir sabah Keloğlan ile Balkız ormanda küçük bir fidan dikiyordu. Ama rüzgar esince ince fidan hep yana yatıyordu. Onu bir dala bağlamak gerekiyordu, ama yanlarındaki dallar çok kısaydı. "Keloğlan, uzun bir dal lazım," dedi Balkız. Keloğlan ayağa kalkıp gerindi ve ağaçların arasına baktı. Büyük bir ağacın dibinde uzun, kuru bir dal gördü. Sakar Keloğlan dalı getirirken düşürdü, ama dal yumuşak toprağa battı. Keloğlan güldü ve dalı toprağa biraz daha bastırdı. Balkız cebinden bir ip çıkardı ve Keloğlan fidanı dala bağladı. Rüzgar yine esti, ama fidan dik kaldı. "Teşekkürler, Keloğlan, sen çok iyi bir arkadaşsın!" dedi Balkız.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Keloğlan, uzun bir dal lazım"
   - Cümle 4: «"Keloğlan, uzun bir dal lazım," dedi Balkız.»
   - Açıklama: Çözüm fikrini figür değil yan karakter Balkız veriyor, ipi de o sağlıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dal yumuşak toprağa battı"
   - Cümle 7: «Sakar Keloğlan dalı getirirken düşürdü, ama dal yumuşak toprağa battı.»
   - Açıklama: Dalın toprağa saplanması bir kazayla sebepsizce çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0117` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: 8b9f893cf4ea326bee718b19608f58840eeb4b08`, sonra gövde.

### Hikâye 9: tohum keloglan-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0119
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'bulaşık', fiil 'zıplatmak', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: top kapının altından şatonun bahçesine kaçtı | izinsiz içeri girmedi ve topu uzun bir dalla çekti
@tohum: keloglan-0119
@degisim: bulaşık -> dal
Hafif bir rüzgar esiyordu. Keloğlan şatonun yüksek kapısının önünde küçük bir top zıplatıyordu. Top yere her değdiğinde Keloğlan bir kez dönüyordu. Ama top bir taşa çarptı ve kapının altından bahçeye kaçtı. Bahçe Keloğlan'ın değildi. Dürüst Keloğlan izinsiz içeri girmedi. Yerde uzun bir dal buldu. Dalı kapının altından uzattı ve topu yavaşça kendine çekti. Top yeniden elindeydi. Bu kez kapıdan uzakta, düz taşların üstünde oynadı. Top tam on kez zıpladı ve Keloğlan on kez döndü. Keloğlan çok sevindi, çünkü topunu geri almış ve oyununa devam etmişti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "top bir taşa çarptı ve kapının altından bahçeye kaçtı"
   - Cümle 4: «Ama top bir taşa çarptı ve kapının altından bahçeye kaçtı.»
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0119` birebir aynı, `@degisim: bulaşık -> dal` (tutuyorsan), ardından `@onarim: 65e792f230daffa59982786ca04294aeeff7b6d9`, sonra gövde.

### Hikâye 10: tohum keloglan-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0120
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'ip', fiil 'kırpmak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: uçurtma sallanıyor ve gürültülü bir ses geliyordu | uçurtmaya baktı ve fazla ipi kırptı
@tohum: keloglan-0120
Bir sabah Keloğlan ile Bilgecan Dede tepede uçurtma uçuruyordu. Birden yukarıdan gürültülü bir ses geldi. Uçurtma da rüzgarda çok sallanıyordu. "Dede, bu ses nereden geliyor?" diye sordu Keloğlan. "Sen ne düşünüyorsun?" diye sordu Dede. Keloğlan dürüst davrandı. "Bilmiyorum, Dede, ama bakacağım," dedi Keloğlan. Keloğlan uçurtmayı yavaşça indirdi ve her yerine dikkatle baktı. Uçurtmanın altında çok uzun bir ip parçası sallanıyordu. Rüzgar esince bu ip uçurtmaya çarpıp ses yapıyordu. Dede cebinden küçük bir makas çıkarıp Keloğlan'a verdi. Keloğlan ipin fazla ucunu makasla kırptı. Uçurtma bu kez sessizce yükseldi. Keloğlan çok sevindi, çünkü sesin nereden geldiğini kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Uçurtma da rüzgarda çok sallanıyordu"
   - Cümle 3: «Uçurtma da rüzgarda çok sallanıyordu.»
   - Açıklama: Sesin yanında ayrı bir sallanma sorunu açılıyor ve bu sorunun çözüldüğü söylenmiyor.
   - Açıklama: Sesin yanında ayrı bir sallanma sorunu açılıyor ve bu sorunun çözüldüğü hiç söylenmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ipin fazla ucunu makasla kırptı"
   - Cümle 12: «Keloğlan ipin fazla ucunu makasla kırptı.»
   - Açıklama: 'Kırptı' 3 yaşındaki çocuk için zor bir kelime; 'kesti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0120` birebir aynı, ardından `@onarim: c67ae2418829601cd17373f5e53c54ef52189316`, sonra gövde.

### Hikâye 11: tohum keloglan-0121 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0121
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'etiket', fiil 'dinlenmek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalaklar sert sepetten hep dışarı zıplıyordu | sepetin içine yumuşak yosun koydu
@tohum: keloglan-0121
@degisim: etiket -> kozalak
Keloğlan ormanda eğlenceli bir oyun oynuyordu. Kozalakları uzaktan sepetine atıyordu. Ama sepet çok sertti ve kozalaklar hep dışarı zıplıyordu. Keloğlan birkaç kez daha denedi ama olmadı. Sonra yoruldu ve bir kütüğün üstüne oturup dinlendi. Kütüğün dibinde yumuşak ve sulu yosunlar vardı. Keloğlan merak etti ve bir kozalağı yosunların üstüne attı. Kozalak hiç zıplamadı. Böylece yumuşak yerde kozalakların zıplamadığını öğrendi. Hemen sepetin dibine biraz yosun koydu. Sonra kozalakları yine attı. Bu kez hepsi sepette kaldı ve Keloğlan sevinçle el çırptı. Keloğlan bundan sonra oyunda hep sepete yosun koydu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşak ve sulu yosunlar"
   - Cümle 6: «Kütüğün dibinde yumuşak ve sulu yosunlar vardı.»
   - Açıklama: 'Sulu' yosun için yanlış kelime; 'ıslak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0121` birebir aynı, `@degisim: etiket -> kozalak` (tutuyorsan), ardından `@onarim: 419034477be41947e8fd17771c7ef8d45ba61527`, sonra gövde.

### Hikâye 12: tohum keloglan-0122 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0122
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yonca', fiil 'götürmek', sıfat 'sert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: rüzgar otları sallıyordu ve yaprakları saymak zordu | otları eliyle tuttu ve birer birer saydı
@tohum: keloglan-0122
Rüzgar ormanda sert esiyordu. Keloğlan ilk kez dört yapraklı bir yonca aramayı denedi. Ama rüzgar yüzünden otlar hep sallanıyordu ve yaprakları saymak zordu. Birden dört yapraklı gibi görünen bir yonca gördü. Önce eliyle tuttu ve yapraklarını saydı. Yaprakları üç taneydi. Keloğlan dürüst bir çocuktu ve bu yoncaya dört yapraklı demedi. O sırada bir şey gördü: elindeki ot hiç sallanmıyordu. Keloğlan otları birer birer eliyle tuttu ve yapraklara baktı. Sonunda gerçek bir dört yapraklı yonca buldu. Keloğlan onu eve götürmek için dikkatle cebine koydu ve sevinçle güldü.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 7: «Keloğlan dürüst bir çocuktu ve bu yoncaya dört yapraklı demedi.»
   - Açıklama: Tohumdaki dürüstlük özelliği kimseye karşı kullanılmıyor ve sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve bu yoncaya dört yapraklı demedi"
   - Cümle 7: «Keloğlan dürüst bir çocuktu ve bu yoncaya dört yapraklı demedi.»
   - Açıklama: Kimse yokken dürüstlük vurgusu olaya hizmet etmeyen işlevsiz bir ayrıntı.
   - Açıklama: Üç yapraklı yonca ve dürüstlük ayrıntısı sorunu ilerletmiyor; ayrıca otu zaten tutup saymışken sonradan tutunca sallanmadığını fark etmesi olay sırasını bozuyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "elindeki ot hiç sallanmıyordu"
   - Cümle 8: «O sırada bir şey gördü: elindeki ot hiç sallanmıyordu.»
   - Açıklama: Keloğlan otu zaten eliyle tutup saymıştı, aynı şeyi sonradan yeni bir buluş gibi fark ediyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0122` birebir aynı, ardından `@onarim: 943ab5c99a8ece9f1eba9a1bd300714770d5d833`, sonra gövde.
