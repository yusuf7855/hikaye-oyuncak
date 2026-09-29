# Editör görevi (onarım): Elsa, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Elsa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar17.txt --ad urun_v2`
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

## Kart: Elsa (kaynaklı, kapalı dünya)

- Ad: Elsa (okunuş: elsa; kesme eki okunuşa uyar)
- Kimlik: Elsa, buzu ve karı yönetebilen, bir krallığın genç kraliçesidir.
- Tür: kraliçe
- Güvenli özellik kullanımı: Buz ve kar gücü yalnız zararsız, güzel şeyler için kullanılır: kar yağdırır, buzdan şekil yapar. Hiçbir canlı donmaz, üşümez ya da incinmez; kimse buz tutmuş göl ya da deniz üstünde yürümez.
- Özellikler:
  - buz: Elinden buz ve kar çıkar; buzdan şekiller yapabilir. (örnek biçimler: buzdan, buzu)
  - kraliçe: Kraliçedir; kız kardeşini korur. (örnek biçimler: kraliçe)
- Yerler:
  - dağ: Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.
  - orman: Karlı ağaçlarla dolu orman.
  - deniz: Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.
  - şato: Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Anna: Elsa'nın cesur küçük kız kardeşi. Tür: prenses; konuşur. Yüzey biçimleri: Anna, kardeş, kardeşi
  - Olaf: Elsa'nın büyüsüyle canlanan neşeli kardan adam; sıcak sarılmaları ve yazı sever. Tür: kardan adam; konuşur. Yüzey biçimleri: Olaf, kardan adam
  - Kristoff: Buz toplayıp satan cesur dağ adamı; ren geyiği Sven'in arkadaşı. Tür: adam; konuşur. Yüzey biçimleri: Kristoff
  - Sven: Kristoff'un ren geyiği; kızağı çeker. Tür: ren geyiği; KONUŞMAZ. Yüzey biçimleri: Sven, ren geyiği, geyik
- Dünya kuralları:
  - Sven konuşmaz; sesle ve hareketle anlatır.
  - Anna Elsa'nın küçük kız kardeşidir; Elsa ablasıdır.
  - Olaf Elsa'nın büyüsüyle yapılmış kardan adamdır; hikayede erimez ya da parçalanmaz.
  - Elsa'nın gücü kimseyi dondurmaz ve incitmez.
- Yasak adlar: Hans, Weselton, Pabbie, Oaken, Marshmallow, Bruni, Arendelle
- Yasak: Anne babanın gemi yolculuğu, fırtına, troller, kurtlar ve kar canavarı hikayeye girmez.
- İzinli dünya kelimeleri: buz, kar, kraliçe, saray, kızak, fiyort, geyik

## Onarılacak hikâyeler

### Hikâye 1: tohum elsa-0052 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0052
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yağmurluk', fiil 'çalışmak', sıfat 'enerjik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: önüne bakmadan koştu ve havuçları karda dağıttı | özür diledi ve havuçları bulup kaseye geri koydu
@tohum: elsa-0052
@degisim: yağmurluk -> havuç
Karlı ağaçların arasında hafif bir rüzgar esiyordu. Elsa buzdan bir kase yapmış ve içine Sven'in havuçlarını koymuştu. Elsa ile enerjik Sven kasenin yanında koşup oynuyordu. Elsa önüne bakmadan koştu, kaseyi devirdi ve havuçları karın içine dağıttı. Sven karı kokladı ve üzgün bir ses çıkardı. "Özür dilerim, Sven, havuçlarını ben dağıttım," dedi Elsa. Sonra ikisi havuçları bulmak için birlikte çalıştı. Sven burnuyla, Elsa da elleriyle havuçları tek tek buldu. Elsa havuçları kaseye geri koydu ve Sven'in önüne bıraktı. Sven başını Elsa'ya sürttü ve bir havuç yedi. Elsa bundan sonra ormanda koşarken hep önüne baktı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa buzdan bir kase yapmış"
   - Cümle 2: «Elsa buzdan bir kase yapmış ve içine Sven'in havuçlarını koymuştu.»
   - Açıklama: Buz özelliği sorunun çözümünde işe yaramıyor, yalnız başta dekor olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0052` birebir aynı, `@degisim: yağmurluk -> havuç` (tutuyorsan), ardından `@onarim: 468a19da50893a231a47e365e7cf80e2bcd525e1`, sonra gövde.

### Hikâye 2: tohum elsa-0053 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Kristoff
@tohum: elsa-0053
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'dolap', fiil 'denemek', sıfat 'çabuk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | şato | Kristoff
@plan: acele edince eldivenleri bir dolaba koydu ve unuttu | özür diledi ve kapının yanındaki dolabı açtı
@tohum: elsa-0053
@degisim: denemek -> açmak
Dışarıda kar sessizce yağıyordu. Elsa sarayın salonunu çabuk çabuk topluyordu. Acele edince Kristoff'un eldivenlerini bir dolaba koydu ve bunu unuttu. Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı. "Elsa, eldivenlerimi gördün mü?" diye sordu Kristoff. "Özür dilerim, Kristoff, onları ben bir dolaba koydum," dedi Elsa. Ama salonda çok dolap vardı. Elsa bu sarayın kraliçesiydi ve eşyaların yerini bilirdi. Eldivenler hep kapının yanındaki küçük dolapta dururdu. Elsa o dolabı hemen açtı. Eldivenler oradaydı! Elsa eldivenleri Kristoff'a verdi. "Teşekkürler, Elsa, hadi şimdi birlikte dışarıda oynayalım!" dedi Kristoff.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kristoff'un eldivenlerini bir dolaba koydu ve bunu unuttu"
   - Cümle 3: «Acele edince Kristoff'un eldivenlerini bir dolaba koydu ve bunu unuttu.»
   - Açıklama: Elsa eldivenleri koyduğu yeri unuttuğu söyleniyor ama sonra yerlerini hep bildiği anlatılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve eşyaların yerini bilirdi"
   - Cümle 8: «Elsa bu sarayın kraliçesiydi ve eşyaların yerini bilirdi.»
   - Açıklama: Çözüm, sorunu kuran unutmayla çelişen ve önceden kurulmamış bir bilgiyle sebepsizce geliyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve eşyaların yerini bilirdi"
   - Cümle 8: «Elsa bu sarayın kraliçesiydi ve eşyaların yerini bilirdi.»
   - Açıklama: Elsa eldivenleri nereye koyduğunu unuttu deniyor ama sonra eşyaların yerini bildiği için hemen buluyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Eldivenler hep kapının yanındaki küçük dolapta dururdu"
   - Cümle 9: «Eldivenler hep kapının yanındaki küçük dolapta dururdu.»
   - Açıklama: Çözüm figürün bir eyleminden değil, sebepsizce eklenen bir bilgiden geliyor ve sorunu anlamsız kılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0053` birebir aynı, `@degisim: denemek -> açmak` (tutuyorsan), ardından `@onarim: ad394dac350c9ccd2a6be1dafb51630442e37aa8`, sonra gövde.

### Hikâye 3: tohum elsa-0055 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0055
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yumurta', fiil 'bölmek', sıfat 'kısa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: küçük yuva insanların geçtiği yolun hemen yanındaydı | taşları yuvanın önüne dizdi ve kısa bir duvar yaptı
@tohum: elsa-0055
@degisim: bölmek -> dizmek
Limanda hafif bir rüzgar esiyordu. Elsa kıyıda yürürken taşların arasında küçük bir yuva gördü. Yuvada üç küçük yumurta vardı, ama yuva yolun hemen yanındaydı. Yoldan geçen insanlar yumurtaları kırabilirdi. Elsa yuvaya elini sürmedi. Kraliçe Elsa yumurtaları korumak istedi. Kıyıdan düz taşlar topladı ve onları yuvanın önüne yan yana dizdi. Yuvanın önünde kısa ama sağlam bir duvar oldu. Elsa yuvaya bir kez daha baktı ve yumurtaları saydı. Elsa çok sevindi, çünkü üç yumurta da artık güvendeydi.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa yumurtaları korumak"
   - Cümle 6: «Kraliçe Elsa yumurtaları korumak istedi.»
   - Açıklama: Önceden tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla ikinci kez tanıtılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0055` birebir aynı, `@degisim: bölmek -> dizmek` (tutuyorsan), ardından `@onarim: e018ebdc03fa291d24dfd78f619986158573be0e`, sonra gövde.

### Hikâye 4: tohum elsa-0056 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0056
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tartı', fiil 'alkışlamak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: zıplamayı izlemeyi unuttu ve arkadaşını dışarıda bıraktı | dışarı koşup özür diledi ve zıplamayı alkışladı
@tohum: elsa-0056
@degisim: tartı -> pencere
Elsa buzdan sarayının önünde Sven ile oynuyordu. Sven sağlam bacaklarıyla karda yüksek yüksek zıplıyordu. Ama Elsa su içmek için saraya girdi ve Sven'e bakmayı unuttu. Sven karda yalnız kaldı ve başını öne eğdi. Elsa pencereden baktı ve Sven'in üzgün olduğunu gördü. Hemen dışarı koştu. Elsa bir kraliçeydi, ama Sven'e sarıldı ve ondan özür diledi. Sonra karın üstüne oturdu ve yalnız Sven'e baktı. Sven yeniden zıpladı ve bu kez daha yükseğe çıktı. Elsa onu gülerek alkışladı. Sven de başını sevinçle Elsa'ya sürttü. Elsa çok sevindi, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa bir kraliçeydi, ama Sven'e sarıldı"
   - Cümle 7: «Elsa bir kraliçeydi, ama Sven'e sarıldı ve ondan özür diledi.»
   - Açıklama: 'ama' bağlacı karşıtlık olmayan iki yargıyı bağlıyor; bağlaç yanlış anlamda.
   - Açıklama: 'ama' bağlacı yanlış anlamda; kraliçe olmakla sarılmak arasında karşıtlık yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi, ama Sven'e sarıldı"
   - Cümle 7: «Elsa bir kraliçeydi, ama Sven'e sarıldı ve ondan özür diledi.»
   - Açıklama: Tohumdaki kraliçe özelliği özür dilemede işe yaramıyor, yalnız anılıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız etiket olarak anılıyor, işe yarar biçimde kullanılmıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yalnız Sven'e baktı"
   - Cümle 8: «Sonra karın üstüne oturdu ve yalnız Sven'e baktı.»
   - Açıklama: 'yalnız' hem 'sadece' hem 'tek başına' okunabiliyor; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0056` birebir aynı, `@degisim: tartı -> pencere` (tutuyorsan), ardından `@onarim: ec069713ef6cc719601a0bd7abaacd0742446307`, sonra gövde.

### Hikâye 5: tohum elsa-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0057
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'trompet', fiil 'küçültmek', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: rüzgar esti ve trompetin içine kar doldu | trompeti ters çevirip salladı ve karı döktü
@tohum: elsa-0057
@degisim: küçültmek -> sallamak
Dağın tepesinde Elsa, ışıltılı trompetiyle bir ses oyunu oynuyordu. Trompeti her çaldığında, ses dağlardan geri geliyordu. Ama birden rüzgar esti ve trompetin içine kar doldu. Elsa yine üfledi, ama trompetten hiç ses çıkmadı. Dağlardan da hiç ses gelmedi. Elsa trompetin içine baktı ve karı gördü. Elsa bir kraliçeydi ve saraydaki bütün müzik aletlerini iyi tanırdı. Trompeti ters çevirdi ve iki kez salladı. Bütün kar yere döküldü. Elsa bir kez daha üfledi ve trompet yüksek bir ses çıkardı. Ses dağlardan geri geldi ve Elsa güldü. Elsa bundan sonra rüzgar esince trompetinin ağzını eliyle kapattı.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ışıltılı trompetiyle bir ses"
   - Cümle 1: «Dağın tepesinde Elsa, ışıltılı trompetiyle bir ses oyunu oynuyordu.»
   - Açıklama: Kartta Elsa'nın trompeti ya da müzik aleti çalma işi yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve saraydaki bütün müzik aletlerini iyi tanırdı"
   - Cümle 7: «Elsa bir kraliçeydi ve saraydaki bütün müzik aletlerini iyi tanırdı.»
   - Açıklama: Kraliçe özelliği karttaki kız kardeşini koruma biçiminde değil, kartta olmayan bir bilgiyle kullanılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "saraydaki bütün müzik aletlerini iyi tanırdı"
   - Cümle 7: «Elsa bir kraliçeydi ve saraydaki bütün müzik aletlerini iyi tanırdı.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi (kız kardeşini korur) değil, kartta olmayan bir bilgi olarak kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve saraydaki bütün müzik aletlerini iyi tanırdı"
   - Cümle 7: «Elsa bir kraliçeydi ve saraydaki bütün müzik aletlerini iyi tanırdı.»
   - Açıklama: Kraliçelik ve müzik aletlerini tanıma ayrıntısı çözüme bir şey katmıyor, işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0057` birebir aynı, `@degisim: küçültmek -> sallamak` (tutuyorsan), ardından `@onarim: 50056e1bb5df1d8ce0dec350f49f5fae77601ebe`, sonra gövde.

### Hikâye 6: tohum elsa-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0058
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yeni bir şeyi denemek
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'zil', fiil 'yoğurmak', sıfat 'yavaş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: kar çok kuru olduğu için kar topu dağıldı | yardım istedi ve karı iyice yoğurdu
@tohum: elsa-0058
Bir sabah Kristoff karlı ormanda bir dala küçük bir zil astı. Elsa kar topuyla zili çalmayı ilk kez denedi. Ama kar çok kuruydu ve top zile varmadan havada dağıldı. Elsa bir kraliçeydi ve böyle bir oyunu hiç oynamamıştı. "Kristoff, bana yardım eder misin?" diye sordu Elsa. "Karı ellerinde yavaş yavaş yoğur, Elsa," dedi Kristoff. Elsa karı iki eliyle sıkıca yoğurdu. Bu kez top sağlam oldu. Elsa topu dala doğru fırlattı. Top zile çarptı ve zil çın çın çaldı. Kristoff sevinçle ellerini çırptı. "Harika, Elsa, zili çaldın!" dedi Kristoff. Sonra ikisi sırayla zili çalarak mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve böyle bir oyunu hiç oynamamıştı"
   - Cümle 4: «Elsa bir kraliçeydi ve böyle bir oyunu hiç oynamamıştı.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor, yalnız anılıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız etiket olarak geçiyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "böyle bir oyunu hiç oynamamıştı"
   - Cümle 4: «Elsa bir kraliçeydi ve böyle bir oyunu hiç oynamamıştı.»
   - Açıklama: Kartta karı yönetebilen Elsa'nın kar topu yapmayı bilmemesi dizideki kimliğiyle çelişiyor.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Karı ellerinde yavaş yavaş yoğur, Elsa"
   - Cümle 6: «"Karı ellerinde yavaş yavaş yoğur, Elsa," dedi Kristoff.»
   - Açıklama: Kartın kimlik cümlesine göre karı yönetebilen Elsa'nın kar topu yapmayı bilmemesi diziyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0058` birebir aynı, ardından `@onarim: 8c000d7d77c9054236118efae953e6a5be8d658e`, sonra gövde.

### Hikâye 7: tohum elsa-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0059
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'erik', fiil 'paketlemek', sıfat 'kuru'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: yürürken bir ses geldi ve paket hafifledi | delikten düşen erikleri buldu ve buzdan kutuya koydu
@tohum: elsa-0059
Bir sabah Elsa kuru erikleri paketledi ve limana götürdü. Kıyıdaki tahta yolda yürürken arkasından "tık, tık" diye bir ses geldi. Elsa bu sesi merak etti, çünkü paketi de hafiflemişti. Elsa durdu ve arkasına baktı. Tahta yolun üstünde kuru erikler duruyordu. Paketin altında küçük bir delik vardı. Erikler bu delikten düşüyor ve tahtaya çarpınca ses çıkarıyordu. Elsa geri yürüdü ve yerdeki erikleri topladı. Ama paket delikti ve erikler yine düşecekti. Elsa elini salladı ve buzdan küçük bir kutu yaptı. Erikleri kutuya koydu ve kapağını kapattı. Artık hiçbir erik düşmedi. Elsa kıyıda bir taşa oturdu ve erikleri mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "paketledi ve limana götürdü"
   - Cümle 1: «Bir sabah Elsa kuru erikleri paketledi ve limana götürdü.»
   - Açıklama: Eriklerin limana götürülme amacı kuruluyor ama hiç kullanılmıyor, Elsa sonunda erikleri kendisi yiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa kuru erikleri paketledi ve limana götürdü"
   - Cümle 1: «Bir sabah Elsa kuru erikleri paketledi ve limana götürdü.»
   - Açıklama: Hikaye erikleri paketlediği başka bir yerde başlayıp limana taşınıyor; tek sahne kuralı çiğneniyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bir sabah Elsa kuru erikleri paketledi"
   - Cümle 1: «Bir sabah Elsa kuru erikleri paketledi ve limana götürdü.»
   - Açıklama: Hikaye erikleri paketlediği başka bir yerde başlayıp limana taşınıyor; tek sahne kuralı belirsizleşiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0059` birebir aynı, ardından `@onarim: 5ab069707b294327e887a03f91ebf4e1f241fdb2`, sonra gövde.

### Hikâye 8: tohum elsa-0060 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0060
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'pilav', fiil 'dikmek', sıfat 'minik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kar yüzünden minik fidan yere eğilmişti | fidanın karını silkti ve yanına sağlam bir dal dikti
@tohum: elsa-0060
@degisim: pilav -> fidan
Ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile Olaf karlı yolda yürüyordu. Elsa yolun kenarında minik bir fidan gördü; fidan karın altında yere eğilmişti. "Elsa, bu küçük ağaç kırılacak mı?" diye sordu Olaf. "Ona yardım edelim, Olaf," dedi Elsa. Elsa bir kraliçeydi ve ormandaki ağaçları da korurdu. Önce fidanın üstündeki karı eliyle yavaşça silkti. Fidan biraz kalktı, ama yine yana eğik duruyordu. Sonra Elsa yerden sağlam bir dal aldı ve fidanın yanına dikti. Olaf fidanı tuttu ve Elsa onu dala yasladı. "Bak, Elsa, artık dik duruyor!" dedi Olaf. Elsa ile Olaf çok sevindi, çünkü minik fidanı kurtarmışlardı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fidanın karını silkti"
   - Cümle 0 (plan satırı): «kar yüzünden minik fidan yere eğilmişti | fidanın karını silkti ve yanına sağlam bir dal dikti»
   - Açıklama: Planda da 'karını silkti' yanlış; 'fidanı silkeledi' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve ormandaki ağaçları da korurdu"
   - Cümle 6: «Elsa bir kraliçeydi ve ormandaki ağaçları da korurdu.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşini korumaktır; burada yalnız söylenmiş, sorunun çözümünde işe yaramıyor.
   - Açıklama: Karttaki özellik kız kardeşini korumak; ağaçları korumak karttakinden farklı bir kullanım.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karı eliyle yavaşça silkti"
   - Cümle 7: «Önce fidanın üstündeki karı eliyle yavaşça silkti.»
   - Açıklama: Kar silkilmez, fidan silkelenir; fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0060` birebir aynı, `@degisim: pilav -> fidan` (tutuyorsan), ardından `@onarim: e0a6eef2cf79afd741e227a81dbe4f6889d405a8`, sonra gövde.

### Hikâye 9: tohum elsa-0062 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0062
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çan', fiil 'giydirmek', sıfat 'şekerli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: dağda hiç çan yokken bir çan sesi duydu | sesin rüzgarda çarpan buzlardan geldiğini buldu
@tohum: elsa-0062
@degisim: giydirmek -> asmak
Dağın tepesinde, buzdan sarayın önünde rüzgar esiyordu. Elsa birden "çın, çın" diye bir çan sesi duydu. Ama dağda hiç çan yoktu, bu yüzden Elsa çok merak etti. Sesin geldiği yere doğru karda yürüdü. Sarayın kapısının üstünden ince buzlar sarkıyordu. Ama buzlar çok yüksekteydi ve Elsa onlara uzanamadı. Elsa elini salladı ve iki küçük buz çubuğu yaptı. Çubukları birbirine vurunca aynı ses çıktı. Çan sesini rüzgarda birbirine çarpan buzlar yapıyordu! Elsa iki buz çubuğunu da kapının yanına astı. Rüzgar esince hepsi birlikte çınladı. Elsa kapıda şekerli bir kurabiye yedi ve sesleri mutlu mutlu dinledi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "hepsi birlikte çınladı"
   - Cümle 11: «Rüzgar esince hepsi birlikte çınladı.»
   - Açıklama: İki çubuk asıldığı halde 'hepsi' zamirinin neyi gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kapıda şekerli bir kurabiye yedi"
   - Cümle 12: «Elsa kapıda şekerli bir kurabiye yedi ve sesleri mutlu mutlu dinledi.»
   - Açıklama: Kurabiye sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Kurabiye sebepsiz beliriyor ve olayla bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0062` birebir aynı, `@degisim: giydirmek -> asmak` (tutuyorsan), ardından `@onarim: c5936e15bde356553ff9b751a1c212aec5d69a40`, sonra gövde.

### Hikâye 10: tohum elsa-0063 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0063
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: bir şey yapmak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'basamak', fiil 'yaklaşmak', sıfat 'şeffaf'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kar çok yumuşaktı ve kızak kaymadı | tepeye buzdan şeffaf bir kaydırak yaptı
@tohum: elsa-0063
@degisim: basamak -> kaydırak
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa ve Olaf bu tepeden kızakla kaymak istiyordu. Ama kar çok yumuşaktı ve kızak karın içine battı. "Kızak hiç kaymıyor, Elsa," dedi Olaf. Elsa tepeye baktı ve biraz düşündü. Sonra elini tepeden aşağı doğru uzattı. Elinden ince bir buz çıktı ve tepeyi kapladı. Böylece tepede şeffaf, uzun bir kaydırak oldu. Elsa aşağı yürüdü ve Olaf'ı bekledi. Olaf kızağa oturdu ve kaydıraktan yavaşça kaydı. Kızak aşağıda Elsa'ya yaklaştı ve durdu. "Harika bir kaydırak yaptın, Elsa!" dedi Olaf. İkisi sırayla kaymaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzdan şeffaf bir kaydırak"
   - Cümle 0 (plan satırı): «kar çok yumuşaktı ve kızak kaymadı | tepeye buzdan şeffaf bir kaydırak yaptı»
   - Açıklama: Plan satırında da 3 yaşındaki çocuğun bilmediği 'şeffaf' kelimesi var.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tepede şeffaf, uzun bir kaydırak"
   - Cümle 8: «Böylece tepede şeffaf, uzun bir kaydırak oldu.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Şeffaf' 3 yaşındaki bir çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0063` birebir aynı, `@degisim: basamak -> kaydırak` (tutuyorsan), ardından `@onarim: 335d4ac2efcdae75ca096bb80c40dea282137a31`, sonra gövde.

### Hikâye 11: tohum elsa-0064 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0064
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'karton', fiil 'taşımak', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: yer ıslaktı ve kutuyu yere koyamadı | buzdan pürüzsüz bir masa yapıp kutuyu koydu
@tohum: elsa-0064
Limanda hava soğuktu. Elsa, Kristoff'a sürpriz için kartondan bir kutu taşıyordu. Kutuyu Kristoff'un kızağının yanına bırakmak istedi, ama yer çok ıslaktı. Kristoff ise ileride büyük buz parçalarını topluyordu. Elsa elini yere doğru uzattı. Elinden buz çıktı ve küçük, pürüzsüz bir masa oldu. Elsa kutuyu masanın üstüne koydu ve Kristoff'a el salladı. Kristoff koşarak geldi ve kutuyu gördü. Kutuyu açtı ve içinde yeni bir şapka buldu. Kristoff şapkayı hemen taktı ve kocaman gülümsedi. Sonra Elsa ile Kristoff kıyıda mutlu mutlu yürüdü.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kristoff'a sürpriz için kartondan"
   - Cümle 2: «Elsa, Kristoff'a sürpriz için kartondan bir kutu taşıyordu.»
   - Açıklama: 'Sürpriz için' eksik bir yapı; 'sürpriz yapmak için' olmalı.
   - Açıklama: 'Sürpriz için' eksik yapı; 'sürpriz yapmak için' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama yer çok ıslaktı"
   - Cümle 3: «Kutuyu Kristoff'un kızağının yanına bırakmak istedi, ama yer çok ıslaktı.»
   - Açıklama: Kutuyu yere koyamamak zayıf bir sorun; Elsa kutuyu elinde tutup Kristoff'a verebilirdi.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, pürüzsüz bir masa"
   - Cümle 6: «Elinden buz çıktı ve küçük, pürüzsüz bir masa oldu.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0064` birebir aynı, ardından `@onarim: 1aed4f5055df6bf4bd7a7b19b620092f60842014`, sonra gövde.

### Hikâye 12: tohum elsa-0066 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0066
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'file', fiil 'susamak', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik çok susadı ama her yer kardı | kayadan damlayan suyu bir kapta topladı
@tohum: elsa-0066
@degisim: tozlu -> güneşli
Bir sabah Elsa ile Sven karlı dağda yürüyordu. Sven birden durdu ve dilini çıkardı. Çok susamıştı, ama dağda her yer kar ve buzdu. Elsa etrafına dikkatle baktı. Güneşli bir kayanın altında küçük damlalar fark etti. Kayanın üstündeki buz eriyordu ve su damla damla düşüyordu. Elsa kolundaki fileden küçük bir kap çıkardı. Kabı damlaların altına koydu ve bekledi. Kap yavaş yavaş temiz suyla doldu. Kraliçe Elsa kabı kendi eliyle Sven'in önüne koydu. Sven suyu hızlıca içti ve başını salladı. Sonra Elsa ile Sven dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kolundaki fileden küçük bir kap çıkardı"
   - Cümle 7: «Elsa kolundaki fileden küçük bir kap çıkardı.»
   - Açıklama: Kolundaki file ve kap önceden kurulmadan tam gerektiği anda sebepsizce beliriyor.
   - Açıklama: File ve kap daha önce hiç anılmadan beliriyor ve çözümü sebepsizce getiriyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kabı kendi eliyle Sven'in"
   - Cümle 10: «Kraliçe Elsa kabı kendi eliyle Sven'in önüne koydu.»
   - Açıklama: 'Kendi eliyle' gereksiz bir ekleme.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kabı kendi"
   - Cümle 10: «Kraliçe Elsa kabı kendi eliyle Sven'in önüne koydu.»
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Elsa hikayenin ortasında 'Kraliçe Elsa' olarak yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kabı kendi eliyle"
   - Cümle 10: «Kraliçe Elsa kabı kendi eliyle Sven'in önüne koydu.»
   - Açıklama: Tohumdaki kraliçe özelliği suyu toplamada işe yaramıyor, yalnız unvan olarak anılıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kabı kendi"
   - Cümle 10: «Kraliçe Elsa kabı kendi eliyle Sven'in önüne koydu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0066` birebir aynı, `@degisim: tozlu -> güneşli` (tutuyorsan), ardından `@onarim: 3aec34a6270fdc307af1daf65f541622e4d53b85`, sonra gövde.
