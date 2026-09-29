# Editör görevi (onarım): Elsa, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar25.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0052 (deneme 5 -> 6)

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
@plan: önüne bakmadan koştu ve havuçları karda dağıttı | özür diledi ve havuçları buzdan bir kaseye topladı
@tohum: elsa-0052
@degisim: yağmurluk -> havuç
Karlı ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile enerjik Sven, karın üstüne dizili havuçların yanında koşup oynuyordu. Elsa önüne bakmadan koştu ve havuçları karın içine dağıttı. Sven karı kokladı ve üzgün bir ses çıkardı. "Özür dilerim, Sven, havuçlarını ben dağıttım," dedi Elsa. Sonra havuçlar için buzdan bir kase yaptı. İkisi havuçları toplamak için birlikte çalıştı. Sven burnuyla, Elsa da elleriyle onları tek tek buldu ve kaseye koydu. Elsa kaseyi Sven'in önüne bıraktı. Sven başını Elsa'ya sürttü ve bir havuç yedi. Elsa bundan sonra ormanda koşarken hep önüne baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa ile enerjik Sven"
   - Cümle 2: «Elsa ile enerjik Sven, karın üstüne dizili havuçların yanında koşup oynuyordu.»
   - Açıklama: 'Enerjik' 3 yaşındaki çocuğun bilmediği soyut, yabancı kökenli bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0052` birebir aynı, `@degisim: yağmurluk -> havuç` (tutuyorsan), ardından `@onarim: 1e08c404985ea6568d075cbd64a4a792b3a76780`, sonra gövde.

### Hikâye 2: tohum elsa-0053 (deneme 5 -> 6)

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
@plan: acele edince eldivenleri bir dolaba koydu ve unuttu | özür diledi ve dolapları tek tek açtı
@tohum: elsa-0053
@degisim: denemek -> açmak
Dışarıda kar sessizce yağıyordu. Elsa sarayın salonunu çabuk çabuk topluyordu. Acele edince Kristoff'un eldivenlerini bir dolaba koydu ve bunu unuttu. Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı. "Elsa, eldivenlerimi gördün mü?" diye sordu Kristoff. "Özür dilerim, Kristoff, onları ben bir dolaba koydum," dedi Elsa. Ama salonda çok dolap vardı ve Elsa hangisine koyduğunu bilmiyordu. Elsa sarayın kraliçesiydi ve her dolabı biliyordu. Dolapları tek tek açtı. Eldivenler kapının yanındaki küçük dolaptaydı! Elsa eldivenleri Kristoff'a verdi. "Teşekkürler, Elsa, hadi şimdi birlikte dışarıda oynayalım!" dedi Kristoff.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa sarayın kraliçesiydi ve her dolabı biliyordu"
   - Cümle 8: «Elsa sarayın kraliçesiydi ve her dolabı biliyordu.»
   - Açıklama: 'Biliyordu' bir önceki cümledeki 'bilmiyordu' ile çelişen bir anlamda kullanılmış ve ne demek istendiği belirsiz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa sarayın kraliçesiydi ve her dolabı biliyordu"
   - Cümle 8: «Elsa sarayın kraliçesiydi ve her dolabı biliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) karttaki gibi kullanılmıyor ve çözüme katkısı yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa sarayın kraliçesiydi ve her dolabı biliyordu"
   - Cümle 8: «Elsa sarayın kraliçesiydi ve her dolabı biliyordu.»
   - Açıklama: Kraliçe olup her dolabı bilmesi çözümde hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Her dolabı bilmesi hangisine koyduğunu bilmemesine hiçbir çıkış getirmiyor ve çözümde işlevsiz kalıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Elsa sarayın kraliçesiydi ve her dolabı biliyordu"
   - Cümle 8: «Elsa sarayın kraliçesiydi ve her dolabı biliyordu.»
   - Açıklama: Bir önceki cümlede Elsa eldivenleri hangi dolaba koyduğunu bilmiyor, burada her dolabı bildiği söyleniyor ve yine de dolapları tek tek açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0053` birebir aynı, `@degisim: denemek -> açmak` (tutuyorsan), ardından `@onarim: 9470100fe88201d3a2b24f6defa9e5338111aa47`, sonra gövde.

### Hikâye 3: tohum elsa-0055 (deneme 5 -> 6)

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
Limanda hafif bir rüzgar esiyordu. Elsa kıyıda yürürken taşların arasında küçük bir yuva gördü. Yuvada üç küçük yumurta vardı, ama yuva yolun hemen yanındaydı. Yoldan geçen insanlar yumurtaları kırabilirdi. Elsa bir kraliçeydi ve yumurtaları korumak istedi. Yuvaya elini sürmedi. Kıyıdan düz taşlar topladı ve onları yuvanın önüne yan yana dizdi. Yuvanın önünde kısa ama sağlam bir duvar oldu. Elsa yuvaya bir kez daha baktı ve yumurtaları saydı. Elsa çok sevindi, çünkü üç yumurta da artık güvendeydi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve yumurtaları korumak istedi"
   - Cümle 5: «Elsa bir kraliçeydi ve yumurtaları korumak istedi.»
   - Açıklama: Özellikler alanındaki kraliçelik yalnız söyleniyor, çözümde (taş duvar) işe yarar biçimde kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve"
   - Cümle 5: «Elsa bir kraliçeydi ve yumurtaları korumak istedi.»
   - Açıklama: Elsa'nın kraliçe olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0055` birebir aynı, `@degisim: bölmek -> dizmek` (tutuyorsan), ardından `@onarim: 68a42f584d06163fe00f5625422e2d8f70576a4d`, sonra gövde.

### Hikâye 4: tohum elsa-0056 (deneme 5 -> 6)

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
Elsa buzdan sarayının önünde Sven ile oynuyordu. Sven sağlam bacaklarıyla karda yüksek yüksek zıplıyordu. Ama Elsa su içmek için saraya girdi ve Sven'e bakmayı unuttu. Sven karda yalnız kaldı ve başını öne eğdi. Elsa pencereden baktı ve Sven'in üzgün olduğunu gördü. Elsa bir kraliçeydi ve arkadaşını üzgün bırakmak istemedi. Hemen dışarı koştu, Sven'e sarıldı ve ondan özür diledi. Sonra karın üstüne oturdu ve Sven'i izledi. Sven yeniden zıpladı ve bu kez daha yükseğe çıktı. Elsa onu gülerek alkışladı. Sven de başını sevinçle Elsa'ya sürttü. Elsa çok sevindi, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve arkadaşını üzgün bırakmak istemedi"
   - Cümle 6: «Elsa bir kraliçeydi ve arkadaşını üzgün bırakmak istemedi.»
   - Açıklama: Kraliçe özelliği kartın özellik alanındaki (kız kardeşini korur) gibi değil, çözüme bağlanmayan bir etiket olarak kullanılıyor.
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor, yalnız etiket olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0056` birebir aynı, `@degisim: tartı -> pencere` (tutuyorsan), ardından `@onarim: a9ac55fcdce7372e63dddc903b0beb162e83abfe`, sonra gövde.

### Hikâye 5: tohum elsa-0057 (deneme 5 -> 6)

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
Dağın tepesinde Elsa, ışıltılı oyuncak trompetiyle bir ses oyunu oynuyordu. Trompeti her çaldığında, ses dağlardan geri geliyordu. Ama birden rüzgar esti ve trompetin içine kar doldu. Elsa yine üfledi, ama trompetten hiç ses çıkmadı. Dağlardan da hiç ses gelmedi. Elsa bu karlı dağın kraliçesiydi ve karın her yere girdiğini biliyordu. Trompetin içine baktı ve karı gördü. Trompeti ters çevirdi ve iki kez salladı. Bütün kar yere döküldü. Elsa bir kez daha üfledi ve trompet yüksek bir ses çıkardı. Ses dağlardan geri geldi ve Elsa güldü. Elsa bundan sonra rüzgar esince trompetinin ağzını eliyle kapattı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu karlı dağın kraliçesiydi"
   - Cümle 6: «Elsa bu karlı dağın kraliçesiydi ve karın her yere girdiğini biliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) çözümde işe yaramıyor, yalnız etiket olarak anılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu karlı dağın kraliçesiydi ve karın her yere girdiğini biliyordu"
   - Cümle 6: «Elsa bu karlı dağın kraliçesiydi ve karın her yere girdiğini biliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi (kız kardeşini korur) ve işe yarar biçimde kullanılmıyor.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Elsa bu karlı dağın kraliçesiydi"
   - Cümle 6: «Elsa bu karlı dağın kraliçesiydi ve karın her yere girdiğini biliyordu.»
   - Açıklama: Kartın kimlik cümlesine göre Elsa bir krallığın kraliçesidir, dağın kraliçesi değildir.
   - Açıklama: Kimlik cümlesine göre Elsa bir krallığın kraliçesidir, dağın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0057` birebir aynı, `@degisim: küçültmek -> sallamak` (tutuyorsan), ardından `@onarim: 9513b691887e9dd5ae51aba6287aed46b32c9644`, sonra gövde.

### Hikâye 6: tohum elsa-0058 (deneme 5 -> 6)

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
Bir sabah Elsa, kraliçesi olduğu saraydan karlı ormana küçük bir zil getirdi. Kristoff zili bir dala astı. Elsa zili kar topuyla ilk kez çalmayı denedi ama kar çok kuruydu. Top zile varmadan havada dağıldı. "Kristoff, bana yardım eder misin?" diye sordu Elsa. "Bu kar çok kuru, Elsa, onu ellerinde yavaş yavaş yoğur," dedi Kristoff. Elsa karı iki eliyle sıkıca yoğurdu. Bu kez top sağlam oldu. Elsa topu dala doğru fırlattı. Top zile çarptı ve zil çın çın çaldı. Kristoff sevinçle ellerini çırptı. "Harika, Elsa, zili çaldın!" dedi Kristoff. Sonra ikisi sırayla zili çalarak mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kraliçesi olduğu saraydan"
   - Cümle 1: «Bir sabah Elsa, kraliçesi olduğu saraydan karlı ormana küçük bir zil getirdi.»
   - Açıklama: Kişi bir sarayın değil bir ülkenin kraliçesi olur; kelime yanlış yerde kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçesi olduğu saraydan karlı ormana"
   - Cümle 1: «Bir sabah Elsa, kraliçesi olduğu saraydan karlı ormana küçük bir zil getirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız süs olarak anılıyor, kartın özellik alanındaki gibi sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız etiket olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0058` birebir aynı, ardından `@onarim: 22293dddc34bfa9fc80c9b3464d5e695663c4b18`, sonra gövde.

### Hikâye 7: tohum elsa-0060 (deneme 5 -> 6)

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
@plan: kar yüzünden minik fidan yere eğilmişti | fidanı yavaşça silkti ve yanına sağlam bir dal dikti
@tohum: elsa-0060
@degisim: pilav -> fidan
Ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile Olaf karlı yolda yürüyordu. Elsa yolun kenarında minik bir fidan gördü; fidan karın altında yere eğilmişti. "Elsa, bu küçük ağaç kırılacak mı?" diye sordu Olaf. "Ona yardım edelim, Olaf," dedi Elsa. Elsa bir kraliçeydi ve fidanı korumak için yanına gitti. Önce fidanı eliyle yavaşça silkti ve kar yere düştü. Fidan biraz kalktı, ama yine yana eğik duruyordu. Sonra Elsa yerden sağlam bir dal aldı ve fidanın yanına dikti. Olaf fidanı tuttu ve Elsa onu dala yasladı. "Bak, Elsa, artık dik duruyor!" dedi Olaf. Elsa ile Olaf çok sevindi, çünkü minik fidanı kurtarmışlardı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve fidanı korumak"
   - Cümle 6: «Elsa bir kraliçeydi ve fidanı korumak için yanına gitti.»
   - Açıklama: Karttaki özellik kız kardeşini koruyan kraliçe olmak; burada kraliçelik yalnız söyleniyor ve fidanı kurtaran iş özellikle ilgisiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0060` birebir aynı, `@degisim: pilav -> fidan` (tutuyorsan), ardından `@onarim: 03d3b39dbe4f5e65e33bcad5413fcd0ea4eaca43`, sonra gövde.

### Hikâye 8: tohum elsa-0065 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0065
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yeni bir şeyi denemek
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'fide', fiil 'sergilemek', sıfat 'düz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kız kardeşi ilk kez kaymak istiyordu ama yol dikti | ona küçük bir tepe buldu ve kızağı hafifçe itti
@tohum: elsa-0065
@degisim: fide -> fidan
Elsa ile Anna buz sarayının önündeydi. Anna yeni kızağını Elsa'ya sergiliyordu. Kızakla ilk kez kaymak istiyordu ama sarayın kapısından inen yol çok dikti. Anna aşağıya bakınca kızağını bıraktı. Elsa bir kraliçeydi ve kardeşini korumak istedi. Sarayın arkasında küçük bir tepe buldu. Tepenin altı düz ve genişti. "Anna, burada deneyelim," dedi Elsa. Anna küçük tepeye çıktı ve kızağa oturdu. Elsa kızağı arkadan tuttu ve hafifçe itti. Anna aşağı kaydı ve küçük bir çam fidanının yanında yavaşça durdu. Sonra güldü ve hemen ayağa kalktı. "Teşekkürler, Elsa, kızakla kaymak çok güzelmiş!" dedi Anna.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa ile Anna buz sarayının önündeydi"
   - Cümle 1: «Elsa ile Anna buz sarayının önündeydi.»
   - Açıklama: Başlıktaki yer dağ ama hikaye sarayın önünde başlıyor ve dağ hiç anılmıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Anna yeni kızağını Elsa'ya sergiliyordu"
   - Cümle 2: «Anna yeni kızağını Elsa'ya sergiliyordu.»
   - Açıklama: 'Sergilemek' bu bağlamda yanlış ve ağır bir kelime; 'gösteriyordu' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kızağını Elsa'ya sergiliyordu"
   - Cümle 2: «Anna yeni kızağını Elsa'ya sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmediği bir kelime ve burada yanlış; 'gösteriyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0065` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: 6f06c0408731a112cf9d6603642a4f6e5b38bc73`, sonra gövde.

### Hikâye 9: tohum elsa-0066 (deneme 4 -> 5)

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
@plan: geyik çok susadı ama yerdeki kar tozluydu | kayadan damlayan temiz suyu bir kapta topladı
@tohum: elsa-0066
Bir sabah Elsa ile Sven karlı dağda yürüyordu. Sven çok susamıştı, ama yerdeki kar çok tozluydu. Elsa'nın kolunda bir file vardı ve filede küçük bir kap duruyordu. Elsa buz sarayının kraliçesiydi ve bu dağı çok iyi biliyordu. Sven'i güneşli bir kayanın yanına götürdü. Kayanın üstündeki buz eriyordu ve su damla damla düşüyordu. Elsa fileden kabı çıkardı ve kayanın altına koydu. Kap yavaş yavaş temiz suyla doldu. Elsa kabı Sven'in önüne bıraktı. Sven suyu hızlıca içti ve sevinçle başını salladı. Sonra Elsa ile Sven dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "filede küçük bir kap duruyordu"
   - Cümle 3: «Elsa'nın kolunda bir file vardı ve filede küçük bir kap duruyordu.»
   - Açıklama: Çözümü sağlayan kap sorun söylenir söylenmez sebepsizce beliriyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa buz sarayının kraliçesiydi"
   - Cümle 4: «Elsa buz sarayının kraliçesiydi ve bu dağı çok iyi biliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız dağı bilmeye bağlanıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa buz sarayının kraliçesiydi ve bu dağı çok iyi biliyordu"
   - Cümle 4: «Elsa buz sarayının kraliçesiydi ve bu dağı çok iyi biliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız etiket olarak geçiyor.
4. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Elsa buz sarayının kraliçesiydi"
   - Cümle 4: «Elsa buz sarayının kraliçesiydi ve bu dağı çok iyi biliyordu.»
   - Açıklama: Kartın kimlik cümlesine göre Elsa bir krallığın kraliçesidir, buz sarayının kraliçesi değil.
   - Açıklama: Kimlik cümlesine göre Elsa bir krallığın kraliçesidir, buz sarayının değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0066` birebir aynı, ardından `@onarim: 7abf1120d9c8f97efc485a0acae1bbe52ffc8b4a`, sonra gövde.

### Hikâye 10: tohum elsa-0067 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0067
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tahta', fiil 'uçmak', sıfat 'kırmızı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: kızaktan gelen tak tak sesi yüzünden geyik durdu | sese baktı ve sallanan tahtayı yerine bastırdı
@tohum: elsa-0067
@degisim: uçmak -> sallanmak
Elsa, Sven'in çektiği kızakla karlı ormanda gidiyordu. Birden kızağın arkasından tak tak diye bir ses geldi. Sven bu sesi duyunca durdu ve yürümek istemedi. Elsa iyi bir kraliçeydi ve Sven'i korumak istedi. "Bekle, Sven, sese ben bakayım," dedi Elsa. Elsa kızaktan indi ve sesin geldiği yere baktı. Kızağın arkasında kırmızı bir tahta sallanıyordu. Tahta her sallanınca kızağa vuruyor ve ses çıkarıyordu. Elsa tahtayı iki eliyle yerine sıkıca bastırdı. Ses hemen durdu. Sven sevinçle kızağı yeniden çekmeye başladı. Elsa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve Sven'i korumak istedi"
   - Cümle 4: «Elsa iyi bir kraliçeydi ve Sven'i korumak istedi.»
   - Açıklama: Karttaki özellik kız kardeşini korumak; burada kraliçelik Sven'e aktarılıyor ve çözüm özellikle ilgisiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0067` birebir aynı, `@degisim: uçmak -> sallanmak` (tutuyorsan), ardından `@onarim: 2f76651c0939380db51ff40688852dc4aa613c6c`, sonra gövde.

### Hikâye 11: tohum elsa-0070 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0070
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'testi', fiil 'dinmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: sarayın bir yeri kırılıyor gibi bir ses duydu | balkona yürüdü ve sesi yapan testiyi buldu
@tohum: elsa-0070
@degisim: tatlı -> ince
Dağın tepesindeki buz sarayında soğuk bir rüzgar esiyordu. Elsa içeride ince bir ses duydu. Bir yerin kırıldığını sandı. Elsa iyi bir kraliçeydi ve sarayını korumak istedi. Hemen sesin geldiği yere yürüdü. Balkonda boş bir testi duruyordu. Ama etrafta kırık bir şey yoktu. Rüzgar testinin ağzına esiyordu ve ses oradan çıkıyordu. Birden rüzgar dindi ve ses de durdu. Elsa testinin yanında biraz bekledi. Rüzgar yeniden esti ve testiden yine aynı ses geldi. Elsa çok sevindi, çünkü saray kırılmamıştı ve ses testiden geliyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Balkonda boş bir testi duruyordu"
   - Cümle 6: «Balkonda boş bir testi duruyordu.»
   - Açıklama: 'Testi' 3 yaşındaki çocuğun bilmeyebileceği eski bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0070` birebir aynı, `@degisim: tatlı -> ince` (tutuyorsan), ardından `@onarim: 9b0bb3ccef3bf5e72e220b50f0d5d2dd5a3bfe0e`, sonra gövde.

### Hikâye 12: tohum elsa-0071 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0071
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: bir şey yapmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ayçiçeği', fiil 'tamamlamak', sıfat 'üzgün'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: rüzgar esti ve buzdan çiçeğin bir yaprağı kırıldı | kızakta yaprağa benzeyen bir buz parçası buldu
@tohum: elsa-0071
Bir sabah Elsa dağda Kristoff'un yanına geldi. Kristoff onun için kızağındaki buz parçalarıyla bir ayçiçeği yapıyordu. Ama rüzgar esti ve çiçeğin ince bir yaprağı düşüp kırıldı. "Çiçeği bitiremedim," dedi Kristoff üzgün bir sesle. Elsa iyi bir kraliçeydi ve Kristoff'a yardım etmek istedi. Kızaktaki buz parçalarına baktı. İnce ve yaprağa benzeyen bir parça buldu. "Bu parça yaprak olabilir mi?" diye sordu Elsa. Elsa parçayı çiçeğin boş yerine dikkatle yerleştirdi. Parça boş yere tam sığdı ve ayçiçeği tamamlandı. "Çok güzel oldu, Elsa!" dedi Kristoff. Sonra Elsa ile Kristoff buzdan ayçiçeğinin yanında mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa iyi bir kraliçeydi ve Kristoff'a yardım etmek istedi"
   - Cümle 5: «Elsa iyi bir kraliçeydi ve Kristoff'a yardım etmek istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) çözümde işe yaramıyor, yalnız etiket olarak anılıyor.
   - Açıklama: Özellikler alanındaki kraliçelik yalnız anılıyor, yaprak bulma çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0071` birebir aynı, ardından `@onarim: ef20c2dc4635d7239ed8eeda7c0a1558c32cbf35`, sonra gövde.
