# Editör görevi (onarım): Elsa, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0058 (deneme 3 -> 4)

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
Bir sabah Kristoff karlı ormanda bir dala küçük bir zil astı. Kraliçe Elsa kar topuyla zili çalmayı ilk kez denedi. Ama kar çok kuruydu ve top zile varmadan havada dağıldı. "Kristoff, bana yardım eder misin?" diye sordu Elsa. "Bu kar çok kuru, Elsa, onu ellerinde yavaş yavaş yoğur," dedi Kristoff. Elsa karı iki eliyle sıkıca yoğurdu. Bu kez top sağlam oldu. Elsa topu dala doğru fırlattı. Top zile çarptı ve zil çın çın çaldı. Kristoff sevinçle ellerini çırptı. "Harika, Elsa, zili çaldın!" dedi Kristoff. Sonra ikisi sırayla zili çalarak mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kar topuyla"
   - Cümle 2: «Kraliçe Elsa kar topuyla zili çalmayı ilk kez denedi.»
   - Açıklama: Kraliçe özelliği yalnız unvan olarak geçiyor; sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0058` birebir aynı, ardından `@onarim: 7a0f22a458f532af9f597169be9e3b0d4c9938a9`, sonra gövde.

### Hikâye 2: tohum elsa-0059 (deneme 3 -> 4)

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
Bir sabah Elsa limanda kuru erikleri paketledi. Onları deniz kenarında yemek istiyordu. Kıyıdaki tahta yolda yürürken arkasından "tık, tık" diye bir ses geldi. Elsa bu sesi merak etti, çünkü paketi de hafiflemişti. Elsa durdu ve arkasına baktı. Yolda kuru erikler duruyordu. Paketin altında küçük bir delik vardı. Erikler bu delikten düşüyor ve tahtaya çarpınca ses çıkarıyordu. Elsa geri yürüdü ve yerdeki erikleri topladı. Ama paket delikti ve erikler yine düşecekti. Elsa elini salladı ve buzdan küçük bir kutu yaptı. Erikleri kutuya koydu ve kapağını kapattı. Artık hiçbir erik düşmedi. Elsa deniz kenarında bir taşa oturdu ve erikleri mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kıyıdaki tahta yolda yürürken arkasından "tık, tık" diye bir ses geldi.»
   - Açıklama: İlk üç cümlede yalnız bir ses duyuluyor; eriklerin delikten düştüğü sorunu ancak 6-8. cümlelerde ortaya çıkıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Elsa bu sesi merak etti, çünkü paketi de hafiflemişti"
   - Cümle 4: «Elsa bu sesi merak etti, çünkü paketi de hafiflemişti.»
   - Açıklama: Asıl sorun olan eriklerin düşmesi ilk üç cümlede açıkça söylenmiyor, ancak sonra anlaşılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0059` birebir aynı, ardından `@onarim: 1b5cf984d54f611b02f0e94482ea8aeba3a2c6b0`, sonra gövde.

### Hikâye 3: tohum elsa-0060 (deneme 3 -> 4)

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
Ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile Olaf karlı yolda yürüyordu. Elsa yolun kenarında minik bir fidan gördü; fidan karın altında yere eğilmişti. "Elsa, bu küçük ağaç kırılacak mı?" diye sordu Olaf. "Ona yardım edelim, Olaf," dedi Elsa. Elsa bir kraliçeydi ve minik fidanı korumak istedi. Önce fidanı eliyle yavaşça silkti ve kar yere düştü. Fidan biraz kalktı, ama yine yana eğik duruyordu. Sonra Elsa yerden sağlam bir dal aldı ve fidanın yanına dikti. Olaf fidanı tuttu ve Elsa onu dala yasladı. "Bak, Elsa, artık dik duruyor!" dedi Olaf. Elsa ile Olaf çok sevindi, çünkü minik fidanı kurtarmışlardı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve minik fidanı korumak istedi"
   - Cümle 6: «Elsa bir kraliçeydi ve minik fidanı korumak istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız etiket olarak anılıyor, çözüme hiçbir katkısı yok ve kartın 'kız kardeşini korur' tanımı fidana kaydırılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve"
   - Cümle 6: «Elsa bir kraliçeydi ve minik fidanı korumak istedi.»
   - Açıklama: Kraliçe olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0060` birebir aynı, `@degisim: pilav -> fidan` (tutuyorsan), ardından `@onarim: f3a28221d9f7a3ff04d21205cac188f96fb59b0c`, sonra gövde.

### Hikâye 4: tohum elsa-0062 (deneme 3 -> 4)

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
Dağın tepesinde hafif bir rüzgar esiyordu. Elsa buzdan sarayının önünde şekerli bir kurabiye yiyordu. Birden "çın, çın" diye bir çan sesi duydu. Ama dağda hiç çan yoktu, bu yüzden Elsa çok merak etti. Sesin geldiği yere doğru karda yürüdü. Sarayın kapısının üstünden ince buzlar sarkıyordu. Ama buzlar çok yüksekteydi ve Elsa onlara uzanamadı. Elsa elini salladı ve iki küçük buz çubuğu yaptı. Çubukları birbirine vurunca aynı ses çıktı. Çan sesini rüzgarda birbirine çarpan buzlar yapıyordu! Elsa iki buz çubuğunu da kapının yanına astı. Rüzgar esince çubuklar da çınladı. Elsa kapının önüne oturdu ve kurabiyesini yiyerek sesleri mutlu mutlu dinledi.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sesin geldiği yere doğru karda yürüdü"
   - Cümle 5: «Sesin geldiği yere doğru karda yürüdü.»
   - Açıklama: Elsa zaten sarayın önündeyken sesin kaynağına yürüyor ama kaynak aynı sarayın kapısında çıkıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa onlara uzanamadı"
   - Cümle 7: «Ama buzlar çok yüksekteydi ve Elsa onlara uzanamadı.»
   - Açıklama: Çözüm yürüme, uzanamama ve yeni buz çubukları yapıp deneme gibi dolambaçlı adımlarla ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0062` birebir aynı, `@degisim: giydirmek -> asmak` (tutuyorsan), ardından `@onarim: 2ab2fb35a55d3d15b7d3b9849f05f87e0b7e83f9`, sonra gövde.

### Hikâye 5: tohum elsa-0063 (deneme 2 -> 3)

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
@plan: kar çok yumuşaktı ve kızak kaymadı | tepeye buzdan uzun bir kaydırak yaptı
@tohum: elsa-0063
@degisim: basamak -> kaydırak
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa ve Olaf bu tepeden kızakla kaymak istiyordu. Ama kar çok yumuşaktı ve kızak karın içine battı. "Kızak hiç kaymıyor, Elsa," dedi Olaf. Elsa tepeye baktı ve biraz düşündü. Sonra elini tepeden aşağı doğru uzattı. Elinden ince bir buz çıktı ve tepeyi kapladı. Böylece tepede cam gibi şeffaf, uzun bir kaydırak oldu. Elsa aşağı yürüdü ve Olaf'ı bekledi. Olaf kızağa oturdu ve kaydıraktan yavaşça kaydı. Kızak aşağıda Elsa'ya yaklaştı ve durdu. "Harika bir kaydırak yaptın, Elsa!" dedi Olaf. İkisi sırayla kaymaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tepede cam gibi şeffaf, uzun bir kaydırak"
   - Cümle 8: «Böylece tepede cam gibi şeffaf, uzun bir kaydırak oldu.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki çocuk bilmez ve benzetme gereksiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "cam gibi şeffaf, uzun"
   - Cümle 8: «Böylece tepede cam gibi şeffaf, uzun bir kaydırak oldu.»
   - Açıklama: 'Şeffaf' kelimesini ve 'cam gibi' benzetmesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0063` birebir aynı, `@degisim: basamak -> kaydırak` (tutuyorsan), ardından `@onarim: c17bb32704906370ee22b18557f1ec4aae5d6e9b`, sonra gövde.

### Hikâye 6: tohum elsa-0065 (deneme 2 -> 3)

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
@degisim: fide -> kızak
Elsa ile Anna buz sarayının önündeydi. Anna yeni kızağını Elsa'ya sergiliyordu. Kızakla ilk kez kaymak istiyordu ama sarayın kapısından inen yol çok dikti. Anna aşağıya bakınca kızağını bıraktı. Kraliçe Elsa kardeşini korumak istedi. Sarayın arkasında küçük bir tepe buldu. Tepenin altı düz ve genişti. "Anna, burada deneyelim," dedi Elsa. Anna küçük tepeye çıktı ve kızağa oturdu. Elsa kızağı arkadan tuttu ve hafifçe itti. Anna aşağı kaydı ve düz yerde yavaşça durdu. Sonra güldü ve hemen ayağa kalktı. "Teşekkürler, Elsa, kızakla kaymak çok güzelmiş!" dedi Anna.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yeni kızağını Elsa'ya sergiliyordu"
   - Cümle 2: «Anna yeni kızağını Elsa'ya sergiliyordu.»
   - Açıklama: 'Sergilemek' burada yanlış anlamda ve çocuk için ağır; 'gösteriyordu' olmalı.
   - Açıklama: 'Sergilemek' burada yanlış; 'gösteriyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0065` birebir aynı, `@degisim: fide -> kızak` (tutuyorsan), ardından `@onarim: 33df60e0bf2da16789e038ee556caf3aa460719d`, sonra gövde.

### Hikâye 7: tohum elsa-0066 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Bir sabah Elsa ile Sven karlı dağda yürüyordu. Elsa'nın kolundaki filede küçük bir kap vardı. Sven birden durdu ve dilini çıkardı, çünkü çok susamıştı. Ama dağda her yer kar ve buzdu. Elsa bir kraliçeydi ve Sven'e hemen yardım etmek istedi. Etrafına dikkatle baktı ve güneşli bir kayanın altında küçük damlalar gördü. Kayanın üstündeki buz eriyordu ve su damla damla düşüyordu. Elsa kabı fileden çıkardı ve kayanın altına koydu. Kap yavaş yavaş temiz suyla doldu. Elsa kabı Sven'in önüne bıraktı. Sven suyu hızlıca içti ve başını salladı. Sonra Elsa ile Sven dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama dağda her yer kar ve buzdu"
   - Cümle 4: «Ama dağda her yer kar ve buzdu.»
   - Açıklama: Kar ve buz zaten sudur; susayan geyiğin her yer kar olduğu için su bulamaması akla yatkın bir sorun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve Sven'e hemen yardım etmek istedi"
   - Cümle 5: «Elsa bir kraliçeydi ve Sven'e hemen yardım etmek istedi.»
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşi korumak; burada yalnız süs olarak anılıyor ve çözümde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve Sven'e hemen yardım etmek istedi"
   - Cümle 5: «Elsa bir kraliçeydi ve Sven'e hemen yardım etmek istedi.»
   - Açıklama: Kraliçe olması yardım isteğinin sebebi gibi sunuluyor ama olayla hiçbir bağı yok, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0066` birebir aynı, `@degisim: tozlu -> güneşli` (tutuyorsan), ardından `@onarim: 3795c6b7253e400cc020931838f35de6c551ea20`, sonra gövde.

### Hikâye 8: tohum elsa-0067 (deneme 2 -> 3)

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
Elsa, Sven'in çektiği kızakla karlı ormanda gidiyordu. Birden kızağın arkasından tak tak diye bir ses geldi. Sven bu sesi duyunca durdu ve yürümek istemedi. "Bekle, Sven, sese ben bakayım," dedi Elsa. Elsa kraliçeydi ve Sven'i korumak için kızaktan ilk o indi. Kızağın arkasında kırmızı bir tahta sallanıyordu. Tahta her sallanınca kızağa vuruyor ve ses çıkarıyordu. Elsa tahtayı iki eliyle yerine sıkıca bastırdı. Ses hemen durdu. Sven sevinçle kızağı yeniden çekmeye başladı. Elsa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kızaktan ilk o indi"
   - Cümle 5: «Elsa kraliçeydi ve Sven'i korumak için kızaktan ilk o indi.»
   - Açıklama: Kızakta başka binen olmadığı için 'ilk' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: Kızaktan inen tek kişi Elsa olduğu için 'ilk' kelimesi anlamca uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve Sven'i korumak için kızaktan ilk o indi"
   - Cümle 5: «Elsa kraliçeydi ve Sven'i korumak için kızaktan ilk o indi.»
   - Açıklama: Kartta kraliçe özelliği kız kardeşini korumaktır; burada Sven'i korumaya çevrilmiş ve çözüme katkısı yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve Sven'i korumak için kızaktan ilk o indi"
   - Cümle 5: «Elsa kraliçeydi ve Sven'i korumak için kızaktan ilk o indi.»
   - Açıklama: Kraliçelik ve Sven'i koruma ayrıntısı sebepsiz ekleniyor; tehlike olmayan bir sesten korunma olayda işe yaramıyor.
   - Açıklama: Ortada Sven'i tehdit eden bir şey yokken koruma gerekçesi zorla eklenmiş ve olaydan çıkmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0067` birebir aynı, `@degisim: uçmak -> sallanmak` (tutuyorsan), ardından `@onarim: a0e2ed17718ec969d502cf7afa26a128ba5e17c4`, sonra gövde.

### Hikâye 9: tohum elsa-0069 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0069
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'pedal', fiil 'katmak', sıfat 'yorgun'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: arkadaşı yazı seviyordu ama dağda çiçek yoktu | o uyurken buzdan çiçekler ve bir güneş yaptı
@tohum: elsa-0069
@degisim: pedal -> çiçek
Dağın tepesinde hafif bir rüzgar esiyordu. Elsa ile Olaf buz sarayının önünde oturuyordu. Olaf yazı çok seviyordu ama karlı dağda hiç çiçek yoktu. Dağa yürüyerek çıkmıştı ve çok yorgundu. Biraz sonra karın üstünde uyudu. Elsa ona bir sürpriz hazırlamak istedi. Ellerini salladı ve Olaf'ın yanına buzdan çiçekler yaptı. Çiçeklerin ortasına parlak bir güneş de kattı. Olaf gözlerini açınca çiçekleri gördü. "Elsa, burada yaz var!" dedi Olaf. "Bunları senin için yaptım, Olaf," dedi Elsa. Sonra Elsa ile Olaf çiçeklerin arasında mutlu mutlu dans etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dağa yürüyerek çıkmıştı ve çok yorgundu"
   - Cümle 4: «Dağa yürüyerek çıkmıştı ve çok yorgundu.»
   - Açıklama: Öznesiz cümlede dağa çıkıp yorulanın ve sonra uyuyanın Elsa mı Olaf mı olduğu belli değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parlak bir güneş de kattı"
   - Cümle 8: «Çiçeklerin ortasına parlak bir güneş de kattı.»
   - Açıklama: 'Katmak' fiili burada uygun değil; güneşi 'yaptı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0069` birebir aynı, `@degisim: pedal -> çiçek` (tutuyorsan), ardından `@onarim: 2fed90e745541ecc025c792acd0675e10ac40a9e`, sonra gövde.

### Hikâye 10: tohum elsa-0070 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: sarayda nereden geldiği bilinmeyen bir ses vardı | sesin geldiği yere yürüyüp testiyi buldu
@tohum: elsa-0070
@degisim: tatlı -> ince
Dağın tepesindeki buz sarayında soğuk bir rüzgar esiyordu. Elsa sarayın içinde ince bir ses duydu. Elsa bu sesi daha önce hiç duymamıştı ve çok merak etti. Ses uzun bir ıslık gibiydi. Elsa sarayın kraliçesiydi ve bütün odalarını iyi bilirdi. Hemen sesin geldiği yere doğru yürüdü. Sarayın balkonunda boş bir testi duruyordu. Rüzgar testinin ağzına esiyordu. Ses tam oradan çıkıyordu. Birden rüzgar dindi ve ses de durdu. Elsa testinin yanında biraz bekledi. Rüzgar yeniden esti ve testiden yine aynı ses geldi. Elsa çok sevindi, çünkü o güzel sesin testiden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa bu sesi daha önce hiç duymamıştı ve çok merak etti"
   - Cümle 3: «Elsa bu sesi daha önce hiç duymamıştı ve çok merak etti.»
   - Açıklama: Ses zararsız ve güzel bir ses; ortada çocuğun önemseyeceği gerçek bir sorun yok, yalnız merak var.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa sarayın kraliçesiydi ve bütün odalarını iyi bilirdi"
   - Cümle 5: «Elsa sarayın kraliçesiydi ve bütün odalarını iyi bilirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki 'kız kardeşini korur' anlamıyla değil, odaları bilmek gibi işe yaramayan bir süs olarak kullanılıyor.
   - Açıklama: Kartın özellikler alanında kraliçelik kız kardeşini korumakla tanımlı; burada odaları bilmenin gerekçesi olarak karttakinden farklı kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa sarayın kraliçesiydi ve bütün odalarını iyi bilirdi"
   - Cümle 5: «Elsa sarayın kraliçesiydi ve bütün odalarını iyi bilirdi.»
   - Açıklama: Odaları iyi bilmesi işe yarayacakmış gibi kuruluyor ama çözümde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0070` birebir aynı, `@degisim: tatlı -> ince` (tutuyorsan), ardından `@onarim: 4197d274a6a55d3f8cb154259beac9a4c470ca61`, sonra gövde.

### Hikâye 11: tohum elsa-0071 (deneme 2 -> 3)

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
Bir sabah Elsa dağda Kristoff'un yanına geldi. Kristoff, kraliçesi için kızağındaki buz parçalarıyla bir ayçiçeği diziyordu. Ama rüzgar esti ve çiçeğin ince bir yaprağı düşüp kırıldı. "Çiçeği bitiremedim," dedi Kristoff üzgün bir sesle. Elsa kızaktaki buz parçalarına baktı. İnce ve yaprağa benzeyen bir parça buldu. "Bu parça yaprak olabilir mi?" diye sordu Elsa. Elsa parçayı çiçeğin boş yerine dikkatle yerleştirdi. Parça boş yere tam sığdı ve ayçiçeği tamamlandı. Kristoff çiçeğe baktı ve kocaman gülümsedi. "Çok güzel oldu, Elsa!" dedi Kristoff. Sonra Elsa ile Kristoff buzdan ayçiçeğinin yanında mutlu mutlu güldü.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "buz parçalarıyla bir ayçiçeği diziyordu"
   - Cümle 2: «Kristoff, kraliçesi için kızağındaki buz parçalarıyla bir ayçiçeği diziyordu.»
   - Açıklama: 'Dizmek' parçalar için kullanılır, ayçiçeği dizilmez; 'ayçiçeği yapıyordu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir ayçiçeği diziyordu"
   - Cümle 2: «Kristoff, kraliçesi için kızağındaki buz parçalarıyla bir ayçiçeği diziyordu.»
   - Açıklama: Ayçiçeği dizilmez, parçalar dizilir; fiil nesnesine uymuyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kristoff, kraliçesi için"
   - Cümle 2: «Kristoff, kraliçesi için kızağındaki buz parçalarıyla bir ayçiçeği diziyordu.»
   - Açıklama: 'Kraliçesi' kimi gösteriyor belli değil; Elsa olduğu söylenmiyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kristoff, kraliçesi için kızağındaki"
   - Cümle 2: «Kristoff, kraliçesi için kızağındaki buz parçalarıyla bir ayçiçeği diziyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçesi için kızağındaki buz"
   - Cümle 2: «Kristoff, kraliçesi için kızağındaki buz parçalarıyla bir ayçiçeği diziyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız bir sıfat olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0071` birebir aynı, ardından `@onarim: 9a2373bf0c17eaece36ed4765145575df0df7821`, sonra gövde.

### Hikâye 12: tohum elsa-0073 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0073
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'saat', fiil 'vermek', sıfat 'ıslak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: küçük saat karların içine düştü ve görünmedi | karların altındaki sesi izledi ve saati buzdan kürekle çıkardı
@tohum: elsa-0073
Elsa, Sven ile karlı ormanda yürüyordu. Elsa küçük saatine bakarken saat elinden kaydı ve karların içine düştü. Elsa karların üstüne baktı ama saati göremedi. "Sven, saatim karların içinde kayboldu," dedi Elsa. O sırada karların altından tık tık diye bir ses geldi. Sven hemen durdu ve hiç ses çıkarmadı. Elsa bu sesi merak etti ve başını yere doğru eğdi. Ses bir ağacın dibinden geliyordu. "Bu benim saatimin sesi, Sven!" dedi Elsa. Elsa buzdan küçük bir kürek yaptı. Küreği yavaşça karlara soktu ve saati çıkardı. Saat ıslaktı ama yine tık tık ses veriyordu. Elsa çok sevindi, çünkü saatini sesinden bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karların altındaki sesi izledi"
   - Cümle 0 (plan satırı): «küçük saat karların içine düştü ve görünmedi | karların altındaki sesi izledi ve saati buzdan kürekle çıkardı»
   - Açıklama: 'İzlemek' çocuk için 'bakmak' anlamındadır; sese uymuyor, 'sesin geldiği yere gitti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0073` birebir aynı, ardından `@onarim: 470db9936f062bf62c889c6472317d536749c8af`, sonra gövde.
