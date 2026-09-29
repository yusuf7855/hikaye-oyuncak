# Editör görevi (onarım): Pepee, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Pepee | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar7.txt --ad urun_v2`
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

## Kart: Pepee (kaynaklı, kapalı dünya)

- Ad: Pepee (okunuş: pepe; kesme eki okunuşa uyar)
- Kimlik: Pepee, mavi tulum ve mavi şapka giyen, dört yaşında meraklı bir oğlandır.
- Tür: oğlan
- Güvenli özellik kullanımı: Pepee yeni şeyleri bir büyüğün yanında dener; derin suya girmez, yüksek yere çıkmaz.
- Özellikler:
  - öğren: Yeni şeyler öğrenmeyi ve denemeyi sever. (örnek biçimler: öğrendi, öğrenmeyi)
  - kahvaltı: Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer. (örnek biçimler: kahvaltı, kahvaltıda)
  - dans: Oyun oynamayı ve dans etmeyi sever. (örnek biçimler: dans, dansı)
- Yerler:
  - orman: Ağaçlarla ve çiçeklerle dolu bir orman.
  - deniz: Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.
  - park: Salıncağı ve kaydırağı olan bir çocuk parkı.
  - ev: Pepee'nin ailesiyle yaşadığı ev.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Bebee: Pepee'nin küçük kız kardeşi; annesine hayrandır, Pepee ile oynamak için büyümek ister. Tür: kız; konuşur. Yüzey biçimleri: Bebee, kardeş, kardeşi
  - Şila: Pepee'nin kuzeni ve en yakın arkadaşı; çok güzel dans eder. Tür: kız; konuşur. Yüzey biçimleri: Şila, kuzen, kuzeni
  - Dedee: Pepee'nin dedesi; en az Pepee kadar hareketli bir oyun arkadaşı. Tür: dede; konuşur. Yüzey biçimleri: Dedee, dede, dedesi, dedeciğim
  - Nenee: Pepee'nin ninesi; komik ve eğlencelidir, yemek pişirmeyi sever. Tür: nine; konuşur. Yüzey biçimleri: Nenee, Ninee, nine, ninesi, nineciğim
  - Annee: Pepee'nin ve Bebee'nin annesi. Tür: anne; konuşur. Yüzey biçimleri: Annee, anne, annesi, anneciğim
- Dünya kuralları:
  - Bebee Pepee'nin küçük kız kardeşidir; Şila kuzenidir, kardeşi değildir.
  - Dizinin görünmeyen anlatıcısı hikayeye girmez; hikaye olayları kendisi anlatır.
- Yasak adlar: Şuşu, Şuşuu, Pisi, Zulu, Köpüş, Maymuş, Kaliş, Möcük, Zezee, Bibii, Kekee, Mimi, Mimii, Duduu, Tutuu, Ekee, Babaa, Zuku
- Yasak: Pepee'nin ve Bebee'nin konuşma zorluğu hikayeye konmaz; kimse konuşmasıyla alay etmez.
- Yasak: Dedee'nin uçan balonu hikayeye girmez (yükseklik).
- İzinli dünya kelimeleri: tulum, kahvaltı, pekmez, tahin, dans

## Onarılacak hikâyeler

### Hikâye 1: tohum pepee-0027 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0027
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'karpuz', fiil 'kırpmak', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: güneş çok parlaktı ve yumurta kaşıktan düştü | şapkasını öne çekip yumurtayı yavaşça taşıdı
@tohum: pepee-0027
@degisim: karpuz -> kaşık
Bir sabah Pepee ormanda eğlenceli bir oyun oynuyordu. Pişmiş bir yumurtayı kaşıkta taşıyıp büyük ağaca götürecekti. Ama güneş çok parlaktı, Pepee gözlerini kırptı ve yumurta düştü. Yumurta yumuşak otlara indi ve kırılmadı. Pepee onu aldı ve toprağını sildi. Sonra mavi şapkasını biraz öne çekti. Artık güneş gözüne gelmedi. Pepee yumurtayı kaşığa koydu ve yavaş yürüdü. Yumurta sallandı ama düşmedi. Pepee ağaca vardı ve güldü. Kahvaltıda en çok yumurtayı severdi. Bu yüzden kabuğunu soydu ve yumurtayı yedi. Pepee çok sevindi, çünkü yumurtayı sonunda ağaca getirmişti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yumurta yumuşak otlara indi"
   - Cümle 4: «Yumurta yumuşak otlara indi ve kırılmadı.»
   - Açıklama: Düşen yumurta için 'indi' fiili öznesine uygun değil; 'düştü' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kahvaltıda en çok yumurtayı severdi"
   - Cümle 11: «Kahvaltıda en çok yumurtayı severdi.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorun çözüldükten sonra süs olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kahvaltı özelliği sorunu çözmekte işe yaramıyor, çözümü şapka sağlıyor ve özellik sonradan eklenmiş bir bilgi olarak kalıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kahvaltıda en çok yumurtayı severdi"
   - Cümle 11: «Kahvaltıda en çok yumurtayı severdi.»
   - Açıklama: Kahvaltı sevgisi ve yumurtanın yenmesi olayla ilgisiz, özellikten sebepsizce eklenmiş bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden kabuğunu soydu ve yumurtayı yedi"
   - Cümle 12: «Bu yüzden kabuğunu soydu ve yumurtayı yedi.»
   - Açıklama: Oyunun hedefi yumurtayı ağaca taşımakken yumurtayı yemek işlevsiz, sonradan eklenmiş bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0027` birebir aynı, `@degisim: karpuz -> kaşık` (tutuyorsan), ardından `@onarim: c9a418f5f790d893ef598d88b7cefce2f771d4ae`, sonra gövde.

### Hikâye 2: tohum pepee-0028 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Nenee
@tohum: pepee-0028
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Nenee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'pizza', fiil 'yeşillenmek', sıfat 'basit'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Nenee
@plan: yapraktan pizzayı pişirecek bir fırın yoktu | ağaçtaki küçük deliği fırın yapıp pizzayı koydu
@tohum: pepee-0028
Rüzgar ağaçların arasında esiyordu. Pepee ile Nenee ormanda pizza oyunu oynuyordu. Yuvarlak bir yaprağı pizza yaptılar ama onu pişirecek bir fırın yoktu. Nenee pizzanın üstüne yeni yeşillenmiş otlar koydu. "Nine, fırını nerede buluruz?" diye sordu Pepee. "Fırın gibi bir yer ara, bu çok basit," dedi Nenee ve güldü. Pepee yeni şeyler denemeyi ve öğrenmeyi severdi. Kalın bir ağacın dibinde küçük bir delik buldu. Pizzayı dikkatle deliğe koydu. İkisi birlikte ona kadar saydı. Sonra Pepee pizzayı çıkardı ve ninesine uzattı. "Buyur, nineciğim, orman pizzası pişti!" dedi Pepee.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "deliği fırın yapıp pizzayı koydu"
   - Cümle 0 (plan satırı): «yapraktan pizzayı pişirecek bir fırın yoktu | ağaçtaki küçük deliği fırın yapıp pizzayı koydu»
   - Açıklama: Pizzanın nereye konduğu eksik; 'pizzayı içine koydu' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni yeşillenmiş otlar koydu"
   - Cümle 4: «Nenee pizzanın üstüne yeni yeşillenmiş otlar koydu.»
   - Açıklama: 'Yeni yeşillenmiş' 3 yaşındaki çocuk için ağır ve belirsiz bir ifade.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee yeni şeyler denemeyi ve öğrenmeyi severdi"
   - Cümle 7: «Pepee yeni şeyler denemeyi ve öğrenmeyi severdi.»
   - Açıklama: Özellik cümlesi olayın içine işlevsizce sokulmuş ve deliği bulmayı açıklamıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0028` birebir aynı, ardından `@onarim: 5036e6492635f2667f0fbf59b2ec0023825ffe40`, sonra gövde.

### Hikâye 3: tohum pepee-0029 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Annee
@tohum: pepee-0029
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: kaybolan eşya
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'gazete', fiil 'yorulmak', sıfat 'kirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Annee
@plan: şapka koltukta görünmüyordu | annesini dinleyip koltukta gazetenin altına baktı
@tohum: pepee-0029
@degisim: kirli -> mavi
Evde Pepee mavi şapkasını arıyordu. Şapkayı az önce koltuğa koymuştu ama şimdi orada göremiyordu. Mutfağa ve odasına da baktı, ama şapka hiçbir yerde yoktu. Sonunda Pepee yoruldu ve masada oturan annesinin yanına gitti. "Anne, şapkam kayboldu," dedi Pepee. "Şapkayı nereye koydun? Oraya bir daha iyice bak," dedi Annee. Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi. Koltuğa geri döndü. Koltukta annesinin gazetesi duruyordu. Pepee gazeteyi kaldırdı ve şapkasını altında buldu. Şapkayı hemen başına taktı. "Teşekkürler, anneciğim, şapkamı buldum!" dedi Pepee.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "severdi ve bunu hemen denedi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi.»
   - Açıklama: 'Bunu' zamirinin neyi gösterdiği ve neyin denendiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bunu hemen denedi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi.»
   - Açıklama: 'Bunu' zamirinin öğrenmeyi mi annenin önerisini mi gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi.»
   - Açıklama: Tohumdaki öğrenme özelliği kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor; koltuğa yeniden bakmak yeni bir şey öğrenmek değil.
   - Açıklama: Öğrenme özelliği karttaki gibi yeni bir şey öğrenmek için değil, annesinin tekrar bak öğüdüne zorlama bir etiket olarak kullanılmış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi"
   - Cümle 8: «Pepee yeni şeyler öğrenmeyi severdi ve bunu hemen denedi.»
   - Açıklama: Özellik cümlesi olaya bağlanmadan zorla sokuluyor ve işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0029` birebir aynı, `@degisim: kirli -> mavi` (tutuyorsan), ardından `@onarim: 5338d0ef6121607f764a139c119f810935acf11d`, sonra gövde.

### Hikâye 4: tohum pepee-0030 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0030
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Şila
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'mıknatıs', fiil 'kıpırdamak', sıfat 'kibar'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: dalga kumdan pastanın bir yanını yıktı | pastayı suyun uzağında yeniden yaptı
@tohum: pepee-0030
@degisim: mıknatıs -> kabuk
Bir sabah Pepee ile Şila kumsalda oynuyordu. O gün Şila'nın doğum günüydü ve Pepee ona kumdan pasta yapıyordu. Ama pasta suya yakındı ve bir dalga pastanın yanını yıktı. Şila arkasını dönmüş, kıpırdamadan duruyordu. "Biraz daha bekler misin, Şila?" diye sordu Pepee kibar bir sesle. "Tabii, Pepee," dedi Şila. Pepee dalgaların yalnız ıslak kuma geldiğini öğrendi. Pastayı daha yukarıda yeniden yaptı. Üstüne küçük deniz kabukları dizdi. Bu kez hiçbir dalga pastaya gelmedi. "Şimdi dönebilirsin, Şila!" dedi Pepee. Şila pastayı görünce sevinçle zıpladı. Pepee ile Şila pastanın yanında el ele mutlu mutlu döndü.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pepee dalgaların yalnız ıslak kuma geldiğini öğrendi"
   - Cümle 7: «Pepee dalgaların yalnız ıslak kuma geldiğini öğrendi.»
   - Açıklama: Pepee'nin bunu nasıl öğrendiği söylenmiyor; çözümü getiren bilgi sebepsiz beliriyor.
   - Açıklama: Pepee'nin bunu nasıl öğrendiği söylenmiyor; çözümü getiren bilgi sebepsizce beliriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "el ele mutlu mutlu döndü"
   - Cümle 13: «Pepee ile Şila pastanın yanında el ele mutlu mutlu döndü.»
   - Açıklama: 'Döndü' fiilinin anlamı belirsiz; nereye döndükleri ya da neden döndükleri belli değil.
   - Açıklama: 'Döndü' burada anlamı belirsiz ve yanlış; eve dönmek mi kendi etrafında dönmek mi belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0030` birebir aynı, `@degisim: mıknatıs -> kabuk` (tutuyorsan), ardından `@onarim: d53d59c0f88992df1bb4d0d369dfe99501d35697`, sonra gövde.

### Hikâye 5: tohum pepee-0031 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0031
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: paylaşmak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'boru', fiil 'ıslanmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: ağacın altındaki kuru yer küçüktü ve annesi ıslanıyordu | ağaca yaslanıp dans ederek annesini kuru yere çekti
@tohum: pepee-0031
@degisim: boru -> ağaç
Yağmur yapraklara hafifçe vuruyordu. Pepee ile Annee ormanda büyük bir ağacın altına koştu. Ama ağacın altındaki kuru yer küçüktü ve Annee'nin omzu ıslanıyordu. Pepee annesine yer açmak istedi. Hemen ağaca iyice yaslandı. Sonra annesinin elini tuttu ve dans ederek onu yanına çekti. Annee dönerek kuru yere geldi ve güldü. Şimdi ikisi de yaprakların altında kuruydu. Annee Pepee'nin başını okşadı ve huzurlu bir yüzle gülümsedi. Yağmur bir süre daha yağdı, sonra durdu. Pepee çok mutluydu, çünkü kuru yerini annesiyle paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "huzurlu bir yüzle gülümsedi"
   - Cümle 9: «Annee Pepee'nin başını okşadı ve huzurlu bir yüzle gülümsedi.»
   - Açıklama: 'Huzurlu' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Huzurlu bir yüz' soyut bir ifade; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0031` birebir aynı, `@degisim: boru -> ağaç` (tutuyorsan), ardından `@onarim: 5a1fe057dac3b34a401b7d818d52ecce18c55fd8`, sonra gövde.
