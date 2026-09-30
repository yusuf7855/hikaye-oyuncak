# Editör görevi (onarım): Elsa, onarım partisi 58

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar58.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar58.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0228 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Anna
@tohum: elsa-0228
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: sırayla oynamak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kaya', fiil 'uyandırmak', sıfat 'bomboş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | Anna
@plan: ikisi de oyunda uyuyan olmak istemedi | sırayla oynamayı söyledi ve önce kendisi uyudu
@tohum: elsa-0228
@degisim: kaya -> yastık
Şatonun büyük salonu bomboştu. Elsa ile Anna orada uyku oyunu oynuyordu. Oyunda uyuyan gözlerini kapatıyor, öteki onu uyandırıyordu. Ama ikisi de uyuyan olmak istemedi. "Ben uyumam!" dedi Anna. "Ben de uyumam!" dedi Elsa. Sonra Elsa durdu ve düşündü. "Sırayla oynayalım, Anna. Önce ben uyurum, sonra sen," dedi kraliçe Elsa. Anna başını salladı. Elsa yastığa uzandı ve gözlerini kapattı. Anna onu yavaşça gıdıkladı. Elsa gülerek gözlerini açtı. Sonra sıra Anna'ya geldi. Anna yastığa uzandı ve Elsa onu gıdıkladı. İki kardeş salonda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ikisi de uyuyan olmak istemedi"
   - Cümle 4: «Ama ikisi de uyuyan olmak istemedi.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ikisi de uyuyan olmak istemedi"
   - Cümle 4: «Ama ikisi de uyuyan olmak istemedi.»
   - Açıklama: İkisinin neden uyuyan olmak istemediği hiç söylenmiyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 9: «Önce ben uyurum, sonra sen," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 9: «Önce ben uyurum, sonra sen," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, kardeşini koruma ya da krallık işi olarak kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0228` birebir aynı, `@degisim: kaya -> yastık` (tutuyorsan), ardından `@onarim: bfa35ba2eaa7f70ea0745d1182ff5eb46b2b7737`, sonra gövde.

### Hikâye 2: tohum elsa-0229 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0229
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'tebeşir', fiil 'getirmek', sıfat 'patlak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: top sivri bir buza çarptı ve delik açıldı | geyikten yardım isteyip deliği buzla kapattı
@tohum: elsa-0229
@degisim: tebeşir -> top
Rüzgar hafif hafif esiyordu. Elsa ile Sven karlı dağda büyük bir topla oynuyordu. Ama top sivri bir buza çarptı ve küçük bir delik açıldı. Sven patlak topu burnuyla Elsa'ya getirdi. Elsa topa her yerden baktı ama deliği bulamadı. Sonunda Sven'den yardım istedi. Sven burnunu topa yaklaştırdı ve yavaşça kokladı. Havanın çıktığı yerde durdu ve başını salladı. Elsa o yere elinden biraz buz çıkardı. Delik hemen kapandı. Elsa topa üfledi ve topu yeniden şişirdi. Top eskisi gibi zıpladı. Elsa ile Sven karda mutlu mutlu top oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o yere elinden biraz buz çıkardı"
   - Cümle 9: «Elsa o yere elinden biraz buz çıkardı.»
   - Açıklama: 'Bir yere buz çıkarmak' fiili yanlış kullanılmış; deliği buzla kapatmak anlatılmak istenmiş.
   - Açıklama: 'Yere buz çıkarmak' yanlış kullanım; buzu deliğe gönderip kapatmak anlatılmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa topa üfledi ve topu yeniden şişirdi"
   - Cümle 11: «Elsa topa üfledi ve topu yeniden şişirdi.»
   - Açıklama: Çözüm deliği bulmak, buzla kapatmak ve topu yeniden şişirmek olarak ikiden fazla adım sürüyor.
   - Açıklama: Çözüm deliği Sven'e buldurmak, buzla kapatmak ve topu yeniden şişirmek olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0229` birebir aynı, `@degisim: tebeşir -> top` (tutuyorsan), ardından `@onarim: 6db21517d3ed8769b9ecf120e00cd4e88d8bafe8`, sonra gövde.

### Hikâye 3: tohum elsa-0230 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0230
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'boru', fiil 'çözülmek', sıfat 'bol'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: sarayda tıp tıp diye bir ses geldi | kar yağdırdı ve sesin yerini buldu
@tohum: elsa-0230
@degisim: boru -> damla
Elsa dağın tepesindeki buz sarayında yürüyordu. Birden "tıp tıp" diye bir ses duydu. Elsa sesin nereden geldiğini merak etti. Salonun her yerine baktı ama bir şey göremedi. Sonra elini kaldırdı ve bol bol ince kar yağdırdı. Kar salonun yerini kapladı. Bir yerde karın üstünde küçük delikler açıldı. Elsa hemen yukarı baktı. Tavandaki bir buz parçası güneşte çözülüyordu. Damlalar tek tek yere düşüyordu. Elsa sesi bulduğu için güldü. Elsa bundan sonra güneşin vurduğu yere buz parçası yapmadı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden "tıp tıp" diye bir ses duydu"
   - Cümle 2: «Birden "tıp tıp" diye bir ses duydu.»
   - Açıklama: Tıp tıp sesi çocuğun önemseyeceği bir sorun değil; hiçbir şey tehlikede değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buz parçası güneşte çözülüyordu"
   - Cümle 9: «Tavandaki bir buz parçası güneşte çözülüyordu.»
   - Açıklama: 'Çözülmek' küçük çocuğun bu anlamda bilmeyeceği bir kelime; 'eriyordu' olmalı.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Damlalar tek tek yere düşüyordu"
   - Cümle 10: «Damlalar tek tek yere düşüyordu.»
   - Açıklama: Damlama durdurulmuyor; ses kaynağı bulunsa da sorun giderilmiş görünmüyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "güneşin vurduğu yere buz parçası yapmadı"
   - Cümle 12: «Elsa bundan sonra güneşin vurduğu yere buz parçası yapmadı.»
   - Açıklama: Damlama durdurulmadan hikaye bitiyor ve ders, hikayede hiç geçmeyen bir eyleme (Elsa'nın buz parçası yapmasına) dayanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0230` birebir aynı, `@degisim: boru -> damla` (tutuyorsan), ardından `@onarim: 155ebf1fddd74ec1a98281bea45e7176f2b04d68`, sonra gövde.

### Hikâye 4: tohum elsa-0231 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0231
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kanepe', fiil 'konmak', sıfat 'ilginç'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: ormanda çın çın diye bir ses geldi | ayrı ayrı aramayı söyledi ve sesi buldu
@tohum: elsa-0231
@degisim: kanepe -> dal
Rüzgar ormanda hızlı esiyordu. Elsa ile Kristoff karlı ağaçların arasında yürüyordu. Birden "çın çın" diye ilginç bir ses duydular. "Bu ses de ne?" diye sordu Kristoff. Kristoff sağa sola koştu ama bulamadı. "Kristoff, sen şu ağaçlara bak, ben de bunlara," dedi kraliçe Elsa. Kristoff hemen öteki ağaçlara gitti. Elsa büyük bir ağacın yanında durdu. Bir dalın üstüne iki buz parçası konmuştu. Rüzgar esince parçalar birbirine çarpıyordu. Kristoff koşarak geldi ve güldü. "Bu buzları ben bıraktım, unutmuşum!" dedi Kristoff. "Ne güzel bir ses, Kristoff, birlikte dinleyelim!" dedi Elsa.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "diye ilginç bir ses duydular"
   - Cümle 3: «Birden "çın çın" diye ilginç bir ses duydular.»
   - Açıklama: Sorun yalnız bir merak; çocuğun önemseyeceği bir sorun ve akla yatkın bir sebep kurulmuyor.
   - Açıklama: Ormanda bir ses duyulması çocuğun önemseyeceği gerçek bir sorun değil, yalnız bir merak olayı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Kristoff, sen şu ağaçlara bak, ben de bunlara," dedi kraliçe Elsa.»
   - Açıklama: Ada bağlı unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Kristoff, sen şu ağaçlara bak, ben de bunlara," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; çözüm ayrı aramak, özellik işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, çözümde işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu buzları ben bıraktım"
   - Cümle 12: «"Bu buzları ben bıraktım, unutmuşum!" dedi Kristoff.»
   - Açıklama: Buzları Kristoff'un bırakıp unuttuğu sonradan sebepsizce ortaya çıkıyor ve önceki sorusuyla uyuşmuyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu buzları ben bıraktım, unutmuşum!"
   - Cümle 12: «"Bu buzları ben bıraktım, unutmuşum!" dedi Kristoff.»
   - Açıklama: Buzların dala Kristoff tarafından konup unutulduğu sonradan sebepsizce ortaya atılıyor ve Kristoff'un sesi hiç tanımaması bununla uyuşmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0231` birebir aynı, `@degisim: kanepe -> dal` (tutuyorsan), ardından `@onarim: 4ded8a9c04e2642c9d5ba047689e9b1a35c97b14`, sonra gövde.

### Hikâye 5: tohum elsa-0232 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0232
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'havuç', fiil 'saklamak', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: kardan kalenin tepesi için bayrak yoktu | kraliçe olduğu için bayrakların saklandığı dolabı bildi
@tohum: elsa-0232
@degisim: havuç -> bayrak
Şatonun önüne bol kar yağıyordu. Elsa elleriyle geniş bir kardan kale yaptı. Ama kalenin tepesine koyacak bir bayrak yoktu. Elsa kaleye baktı ve biraz üzüldü. Elsa bu şatonun kraliçesiydi ve her köşesini biliyordu. Bayrakların büyük salondaki dolapta saklandığını hatırladı. Hemen salona koştu ve dolabı açtı. Dolaptan küçük, mavi bir bayrak aldı. Sonra kalesine geri döndü. Bayrağı kalenin tepesine dikkatle taktı. Elsa çok sevindi, çünkü kardan kalesinin artık bir bayrağı vardı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bayrakların saklandığı dolabı bildi"
   - Cümle 0 (plan satırı): «kardan kalenin tepesi için bayrak yoktu | kraliçe olduğu için bayrakların saklandığı dolabı bildi»
   - Açıklama: 'bildi' burada 'biliyordu' anlamında yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0232` birebir aynı, `@degisim: havuç -> bayrak` (tutuyorsan), ardından `@onarim: 6411ba09f609093fa10c8c21cb5d4ea424b7065d`, sonra gövde.

### Hikâye 6: tohum elsa-0233 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0233
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kolye', fiil 'şaşırmak', sıfat 'limonlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: ilk kolye çok ağır oldu ve takılamadı | küçük taneler yapıp hafif bir kolye yaptı
@tohum: elsa-0233
@degisim: limonlu -> hafif
Bir sabah Elsa karlı ormanda yürüyordu. Elsa ilk kez buzdan bir kolye yapmayı denemek istedi. Ama ilk kolyenin taneleri çok büyüktü ve kolye çok ağır oldu. Kolyeyi boynuna takamadı ve biraz düşündü. Sonra elinden küçük küçük buz taneleri çıkardı. Taneleri ince bir buz ipine dizdi. Yeni kolye çok hafif oldu. Elsa onu boynuna rahatça taktı. Taneler güneşte parlıyordu. Elsa kolyenin bu kadar güzel olmasına çok şaşırdı. Elsa bundan sonra yeni bir şeyi denerken önce küçük parçalarla başladı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "küçük taneler yapıp hafif bir kolye yaptı"
   - Cümle 0 (plan satırı): «ilk kolye çok ağır oldu ve takılamadı | küçük taneler yapıp hafif bir kolye yaptı»
   - Açıklama: Plan satırında 'yapıp ... yaptı' fiili gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0233` birebir aynı, `@degisim: limonlu -> hafif` (tutuyorsan), ardından `@onarim: e12de2c8c851e6311f369bc8c293ad62def1c982`, sonra gövde.

### Hikâye 7: tohum elsa-0234 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0234
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'marul', fiil 'hatırlamak', sıfat 'sevimli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: dağda garip bir ses geldi | gözleri kapatıp dinlemeyi söyledi ve sesi buldu
@tohum: elsa-0234
Rüzgar dağda serin serin esiyordu. Elsa ile Kristoff buz sarayının önünde oturuyordu. Birden garip bir ses duydular. Kristoff kayaların arkasına baktı ama bir şey yoktu. "Kristoff, gözlerini kapat ve sesi dinle," dedi kraliçe Elsa. Kristoff gözlerini kapattı. Ses yine geldi, hem de Kristoff'un karnından! Kristoff çok güldü. "Bu ses benim karnım, çok açım!" dedi Kristoff. Sonra çantasındaki ekmekle marulu hatırladı. Hepsini ikiye böldü ve yarısını Elsa'ya verdi. "Teşekkürler, Kristoff, karnın ne sevimli bir ses çıkarıyor!" dedi Elsa.
```

**Hakem bulguları (5):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 5: «"Kristoff, gözlerini kapat ve sesi dinle," dedi kraliçe Elsa.»
   - Açıklama: Addan önceki unvan büyük harfle yazılır: 'Kraliçe Elsa'.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 5: «"Kristoff, gözlerini kapat ve sesi dinle," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellikler alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses yine geldi, hem de Kristoff'un karnından!"
   - Cümle 7: «Ses yine geldi, hem de Kristoff'un karnından!»
   - Açıklama: Kristoff'un kendi karnının sesini garip bir dağ sesi sanması akla yatkın değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bu ses benim karnım"
   - Cümle 9: «"Bu ses benim karnım, çok açım!" dedi Kristoff.»
   - Açıklama: Ses karın olamaz; 'karnımın sesi' olmalı.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Bu ses benim karnım, çok açım"
   - Cümle 9: «"Bu ses benim karnım, çok açım!" dedi Kristoff.»
   - Açıklama: Ses sorunu çözülünce Kristoff'un açlığı ikinci bir sorun olarak ortaya çıkıyor ve ekmekle ayrıca çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0234` birebir aynı, ardından `@onarim: 12e93625e7cdb3ccb44eb6797f3f59d05902f538`, sonra gövde.
