# Editör görevi (onarım): Elsa, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar35.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0062 (deneme 4 -> 5)

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
Dağın tepesinde hafif bir rüzgar esiyordu. Elsa buzdan sarayının arkasında şekerli bir kurabiye yiyordu. Birden "çın, çın" diye bir çan sesi duydu. Ama dağda hiç çan yoktu, bu yüzden Elsa çok merak etti. Sesin geldiği yere, sarayın önüne yürüdü. Kapının üstünden ince buzlar sarkıyordu. Rüzgar esince buzlar birbirine çarpıyor ve çınlıyordu. Çan sesini bu buzlar yapıyordu! Elsa bu sesi çok beğendi. Elini salladı ve iki küçük buz çubuğu yaptı. Çubukları da kapının yanına astı. Artık kapıdan daha çok ses geliyordu. Elsa kapının önüne oturdu ve kurabiyesini yiyerek sesleri mutlu mutlu dinledi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kurabiyesini yiyerek sesleri mutlu mutlu dinledi"
   - Cümle 13: «Elsa kapının önüne oturdu ve kurabiyesini yiyerek sesleri mutlu mutlu dinledi.»
   - Açıklama: Kaybolan kurabiye sonda açıklamasız biçimde yeniden yeniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0062` birebir aynı, `@degisim: giydirmek -> asmak` (tutuyorsan), ardından `@onarim: 792c088fbf43bf12f1bd6971e9824ad90e043a3c`, sonra gövde.

### Hikâye 2: tohum elsa-0101 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0101
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'dolma', fiil 'yayılmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: rüzgarda kalenin ön duvarı sallandı | kardan adamdan yardım istedi ve duvara buz yaydı
@tohum: elsa-0101
@degisim: dolma -> duvar
Rüzgar karlı ağaçların arasında esiyordu. Elsa ormanda Olaf ile kardan büyük bir kale yapıyordu. Ama rüzgar her estiğinde kalenin ön duvarı sallanıyordu. Elsa duvarı elleriyle tutunca buz yapamıyordu. Bu yüzden Elsa, Olaf'tan yardım istedi. Olaf hemen duvarın yanına geldi ve onu sıkıca tuttu. Elsa ellerini duvara doğru açtı ve ince bir buz yaptı. Buz duvarın her yerine yavaşça yayıldı. Duvar sağlam oldu ve rüzgarda artık sallanmadı. Olaf kaleyi çok sevdi. Elsa, Olaf'a teşekkür etti ve ona sarıldı. Elsa cömert davrandı ve kaleyi Olaf'a hediye etti. İkisi kalenin içinde mutlu mutlu oyun oynadı.
```

**Hakem bulguları (2):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Elsa duvarı elleriyle tutunca buz yapamıyordu"
   - Cümle 4: «Elsa duvarı elleriyle tutunca buz yapamıyordu.»
   - Açıklama: Kartın özellikler alanında olmayan uydurma bir güç sınırı ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa cömert davrandı ve kaleyi Olaf'a hediye etti"
   - Cümle 12: «Elsa cömert davrandı ve kaleyi Olaf'a hediye etti.»
   - Açıklama: Birlikte yapılan kalenin sebepsizce hediye edilmesi olaydan çıkmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0101` birebir aynı, `@degisim: dolma -> duvar` (tutuyorsan), ardından `@onarim: 077d7883366ba2ba5d3bf17c13a585051ed6c638`, sonra gövde.

### Hikâye 3: tohum elsa-0104 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0104
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gözlük', fiil 'başlamak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: sert rüzgar küçük çiçeği çok sallıyordu | çiçeğin önüne eğilip onu elleriyle korudu
@tohum: elsa-0104
@degisim: gözlük -> yaprak
Rüzgar esmeye başladı. Elsa dağın tepesinde, buzdan sarayının önünde küçük, mavi bir çiçek gördü. Rüzgar çiçeği çok sallıyordu. Çiçek narindi, yani çok inceydi ve yaprakları kolayca kopabilirdi. Elsa bir kraliçeydi ve küçükleri hep korurdu. Hemen çiçeğin önüne eğildi. Sırtını rüzgara döndü ve iki elini çiçeğin çevresine koydu. Soğuk hava Elsa'ya çarptı ama çiçeğe gelmedi. Elsa orada durdu ve bir süre bekledi. Sonra rüzgar yavaşladı ve durdu. Elsa ellerini yavaşça çekti ve çiçeğe baktı. Mavi çiçek yine dik duruyordu ve yapraklarının hepsi yerindeydi. Elsa çok sevindi, çünkü çiçeği rüzgardan korumuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çiçek narindi, yani çok inceydi"
   - Cümle 4: «Çiçek narindi, yani çok inceydi ve yaprakları kolayca kopabilirdi.»
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmediği bir kelime; açıklansa da metinde kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0104` birebir aynı, `@degisim: gözlük -> yaprak` (tutuyorsan), ardından `@onarim: 3f2ee42c3d72670c3eb3015f5fae3a9ce41348a0`, sonra gövde.

### Hikâye 4: tohum elsa-0105 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0105
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ipek', fiil 'karıştırmak', sıfat 'gri'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: rüzgar ipek kurdeleyi karıştırdı ve oyun durdu | kurdeleyi açıp oyunu sarayın büyük salonuna taşıdı
@tohum: elsa-0105
Sarayın önünde Elsa kurdele oyunu oynuyordu. Elinde uzun, gri bir ipek kurdele vardı. Elsa dönüyordu ve kurdele havada büyük daireler çiziyordu. Ama birden sert bir rüzgar esti ve kurdeleyi birbirine karıştırdı. Kurdele artık havada uçmuyordu. Elsa kurdeleyi yavaşça açtı ve düzeltti. Ama rüzgar dışarıda yine esiyordu. Elsa bu sarayın kraliçesiydi, bu yüzden en büyük salonun kapılarını açtı. Salonda hiç rüzgar yoktu. Elsa kurdeleyi yeniden havaya kaldırdı. Gri kurdele salonda rahatça döndü ve hiç karışmadı. Elsa kurdele oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oyunu sarayın büyük salonuna taşıdı"
   - Cümle 0 (plan satırı): «rüzgar ipek kurdeleyi karıştırdı ve oyun durdu | kurdeleyi açıp oyunu sarayın büyük salonuna taşıdı»
   - Açıklama: 'Oyunu taşımak' soyut ve mecazlı bir anlatım.
   - Açıklama: 'Oyunu taşımak' mecazlı bir anlatım.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elsa dönüyordu ve kurdele havada büyük daireler çiziyordu.»
   - Açıklama: Sorun ilk üç cümlede söylenmiyor, ancak dördüncü cümlede rüzgar kurdeleyi karıştırıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurdeleyi birbirine karıştırdı"
   - Cümle 4: «Ama birden sert bir rüzgar esti ve kurdeleyi birbirine karıştırdı.»
   - Açıklama: Tek bir kurdele 'birbirine karışmaz'; doğru fiil 'dolaştırdı' olmalı.
   - Açıklama: Tek kurdele için 'birbirine karıştırdı' uygun değil; 'kurdeleyi dolaştırdı' olmalı.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "sert bir rüzgar esti"
   - Cümle 4: «Ama birden sert bir rüzgar esti ve kurdeleyi birbirine karıştırdı.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede ortaya çıkıyor.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa kurdeleyi yavaşça açtı ve düzeltti"
   - Cümle 6: «Elsa kurdeleyi yavaşça açtı ve düzeltti.»
   - Açıklama: Karışan kurdele tek hamlede açılıyor; sorun önemsiz ve kendiliğinden bitiyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 8: «Elsa bu sarayın kraliçesiydi, bu yüzden en büyük salonun kapılarını açtı.»
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumakla tanımlı; burada yalnız herkesin yapabileceği bir kapı açmaya gerekçe olarak anılıyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0105` birebir aynı, ardından `@onarim: bdf182feab533720d8881588d3782929dd616dab`, sonra gövde.

### Hikâye 5: tohum elsa-0106 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0106
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'baston', fiil 'ayrılmak', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: arkadaşın bastonu yoktu ve ayakları kara batıyordu | bastonu sırayla kullanmak için kural koydu
@tohum: elsa-0106
@degisim: dürüst -> uzun
Bir sabah Elsa ile Kristoff karlı ormanda yürüyordu. Kar çok derindi ve Kristoff'un bastonu yoktu. Bu yüzden Kristoff'un ayakları her adımda kara batıyordu. Elsa'nın elinde ise uzun bir baston vardı. Elsa bunu gördü ve bastonunu Kristoff ile paylaşmak istedi. Elsa kraliçeydi ve kısa bir kural koydu. Her büyük ağaçta bastonu birbirlerine vereceklerdi. İkisi de kurala uydu ve bastonu sırayla kullandı. Böylece Kristoff da karda bastonla yürüyebildi. Ormanın sonunda ayrılırken Kristoff gülümsedi ve Elsa'ya teşekkür etti. Elsa bundan sonra bastonunu Kristoff ile hep paylaştı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kar çok derindi ve Kristoff'un bastonu yoktu"
   - Cümle 2: «Kar çok derindi ve Kristoff'un bastonu yoktu.»
   - Açıklama: Ayakların kara batmasının sebebi karın derinliği; bastonun olmaması ayakların batmasını açıklamıyor.
   - Açıklama: Bastonun olmaması ayakların kara batmasının akla yatkın sebebi değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bunu gördü"
   - Cümle 5: «Elsa bunu gördü ve bastonunu Kristoff ile paylaşmak istedi.»
   - Açıklama: 'bunu' zamiri bir önceki cümledeki Elsa'nın bastonunu mu Kristoff'un batan ayaklarını mı gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve kısa bir kural koydu"
   - Cümle 6: «Elsa kraliçeydi ve kısa bir kural koydu.»
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumaktır; kural koymak karttaki gibi bir kullanım değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İkisi de kurala uydu ve bastonu sırayla kullandı"
   - Cümle 8: «İkisi de kurala uydu ve bastonu sırayla kullandı.»
   - Açıklama: Bastonu sırayla kullanmak ayakların kara batmasını önlemiyor ve Kristoff yolun yarısında yine bastonsuz kalıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bastonu sırayla kullandı"
   - Cümle 8: «İkisi de kurala uydu ve bastonu sırayla kullandı.»
   - Açıklama: Bastonu sırayla kullanmak ayakların kara batmasını önlemiyor; çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0106` birebir aynı, `@degisim: dürüst -> uzun` (tutuyorsan), ardından `@onarim: 3384692501117e3e05b1a5de4208ab2cd59a06c3`, sonra gövde.

### Hikâye 6: tohum elsa-0110 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0110
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'toz', fiil 'gizlenmek', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: bir ağaçtan ağlamaya benzeyen bir ses geldi | daldaki deliğin önündeki karı itip sesi buldu
@tohum: elsa-0110
@degisim: gizlenmek -> kalmak
Ormanda ağaçların üstünde kar tozu parlıyordu. Elsa uykulu gözlerle karda yavaşça yürüyordu. Birden yakındaki bir ağaçtan ağlamaya benzeyen ince bir ses geldi. Elsa gözlerini kocaman açtı ve durdu. Elsa kraliçeydi ve ormanda kimsenin üzülmesini istemezdi. Bu yüzden sesin geldiği ağaca hemen yürüdü. Ağacın kalın bir dalında küçük bir delik vardı. Deliğin yarısı karın altında kalmıştı. Rüzgar esince ses oradan çıkıyordu. Elsa karı eliyle yavaşça itti. Rüzgar yine esti ve delikten bir ıslık sesi çıktı. Sesi yapan rüzgardı. Elsa çok sevindi, çünkü ormanda ağlayan kimse yoktu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karı itip sesi buldu"
   - Cümle 0 (plan satırı): «bir ağaçtan ağlamaya benzeyen bir ses geldi | daldaki deliğin önündeki karı itip sesi buldu»
   - Açıklama: Ses bulunmaz; 'sesin nereden geldiğini buldu' olmalı.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "ağlamaya benzeyen ince bir ses"
   - Cümle 3: «Birden yakındaki bir ağaçtan ağlamaya benzeyen ince bir ses geldi.»
   - Açıklama: Ormanda tek başına duyulan ağlama benzeri ses küçük çocuğu korkutabilir.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "ağaçtan ağlamaya benzeyen ince bir ses geldi"
   - Cümle 3: «Birden yakındaki bir ağaçtan ağlamaya benzeyen ince bir ses geldi.»
   - Açıklama: Ormanda tek başına yürürken ağaçtan gelen ağlama sesi 3-6 yaş için ürkütücü bir gizem öğesi olabilir.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa karı eliyle yavaşça itti"
   - Cümle 10: «Elsa karı eliyle yavaşça itti.»
   - Açıklama: Sesin kaynağı dokuzuncu cümlede zaten bulunmuşken karı itmek işlevsiz bir adım olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0110` birebir aynı, `@degisim: gizlenmek -> kalmak` (tutuyorsan), ardından `@onarim: 92c69f2f49956bae7ad90f593bcfbd5a0ab7a80f`, sonra gövde.

### Hikâye 7: tohum elsa-0111 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0111
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kadife', fiil 'bulmak', sıfat 'büyük'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: resim bitmeden arkadaşı erken geldi | kural koydu ve arkadaşı gözlerini kapattı
@tohum: elsa-0111
@degisim: kadife -> resim
Bir sabah Elsa limanda Olaf için bir sürpriz hazırlıyordu. Olaf yazı çok severdi, bu yüzden Elsa büyük bir güneş resmi yapıyordu. Ama resim bitmeden Olaf erken geldi. Olaf resmi şimdi görmemeliydi. "Elsa, ne yapıyorsun?" diye sordu Olaf. Elsa kraliçeydi ve hemen kısa bir kural koydu. "Gözlerini kapat, Olaf, biraz bekle!" dedi Elsa. Olaf gözlerini kapattı ve sessizce bekledi. Elsa bu sırada resmi çabucak tamamladı. Sonra resmi Olaf'ın önüne koydu. Olaf gözlerini açtı ve önünde sarı bir güneş buldu. "Yaz güneşi, en sevdiğim şey!" dedi Olaf. Olaf, Elsa'ya sıcacık sarıldı ve ikisi limanda mutlu mutlu güldü.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kural koydu ve arkadaşı"
   - Cümle 0 (plan satırı): «resim bitmeden arkadaşı erken geldi | kural koydu ve arkadaşı gözlerini kapattı»
   - Açıklama: 'Kural koymak' soyut bir kavram, küçük çocuğa uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hemen kısa bir kural koydu"
   - Cümle 6: «Elsa kraliçeydi ve hemen kısa bir kural koydu.»
   - Açıklama: Tek seferlik 'Gözlerini kapat' buyruğu kural değildir; kelime yanlış anlamda.
   - Açıklama: Elsa'nın söylediği bir kural değil bir istek; 'kural koymak' yanlış anlamda kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hemen kısa bir kural koydu"
   - Cümle 6: «Elsa kraliçeydi ve hemen kısa bir kural koydu.»
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumaktır; kural koymak karttaki gibi bir kullanım değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'ya sıcacık sarıldı"
   - Cümle 13: «Olaf, Elsa'ya sıcacık sarıldı ve ikisi limanda mutlu mutlu güldü.»
   - Açıklama: 'Sıcacık sarılmak' mecaz; üstelik kardan adam için kafa karıştırıcı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0111` birebir aynı, `@degisim: kadife -> resim` (tutuyorsan), ardından `@onarim: ad69e10155a33ff2ddcf637c2ad41348bf133e5c`, sonra gövde.

### Hikâye 8: tohum elsa-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Kristoff
@tohum: elsa-0114
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'satranç', fiil 'ıslanmak', sıfat 'gururlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | şato | Kristoff
@plan: yağmur başladı ve satranç taşları ıslandı | elinden çıkan buzla masanın üstüne bir çatı yaptı
@tohum: elsa-0114
Dışarıda hafif bir yağmur yağmaya başladı. Elsa ile Kristoff sarayın önünde satranç oynuyordu. Yağmur damlaları satranç tahtasına düştü ve taşlar ıslandı. "Böyle oynayamayız, Elsa!" dedi Kristoff. Elsa gökyüzüne baktı ve ellerini kaldırdı. Elinden buz çıktı ve masanın üstünde buzdan bir çatı oldu. Yağmur artık çatıya vuruyordu ve taşlar kuru kaldı. Elsa buzdan çatıya gururlu bir yüzle baktı. Kristoff güldü ve beyaz taşını ileri itti. "Şimdi sıra sende, Elsa," dedi Kristoff. Elsa da siyah taşını oynattı. İkisi çatının altında oyuna devam etti. "Teşekkürler, Elsa, buzdan çatı oyunumuzu kurtardı!" dedi Kristoff.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "taşlar kuru kaldı"
   - Cümle 7: «Yağmur artık çatıya vuruyordu ve taşlar kuru kaldı.»
   - Açıklama: Taşlar üçüncü cümlede ıslanmışken burada kuru kaldığı söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzdan çatıya gururlu bir yüzle baktı"
   - Cümle 8: «Elsa buzdan çatıya gururlu bir yüzle baktı.»
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzdan çatı oyunumuzu kurtardı"
   - Cümle 13: «"Teşekkürler, Elsa, buzdan çatı oyunumuzu kurtardı!" dedi Kristoff.»
   - Açıklama: 'Oyunu kurtarmak' mecazdır; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Oyunu kurtarmak' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0114` birebir aynı, ardından `@onarim: 98aae99d9efb06af6eaecec0790c8f165f0931ea`, sonra gövde.

### Hikâye 9: tohum elsa-0115 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0115
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'filiz', fiil 'dolmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: elma derin karın içine battı | buzdan geniş bir tabak yapıp elmaları içine koydu
@tohum: elsa-0115
@degisim: filiz -> elma
Bir sabah Elsa dağda Sven ile dinleniyordu. Elsa'nın puantiyeli sepeti kırmızı elmalarla dolmuştu. Elsa ilk elmayı Sven için karın üstüne koydu ama elma kara battı. Sven burnunu kara soktu ve elmayı aradı. Elsa elmaları Sven ile paylaşmak istiyordu. "Bekle, Sven, sana bir tabak yapayım," dedi Elsa. Elsa elini salladı ve buzdan geniş bir tabak yaptı. Tabağı karın üstüne bıraktı ve elmaların yarısını içine yerleştirdi. Sven başını salladı ve elmaları çıtır çıtır yedi. Sonra Elsa ile Sven karlı dağda yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'nın puantiyeli sepeti"
   - Cümle 2: «Elsa'nın puantiyeli sepeti kırmızı elmalarla dolmuştu.»
   - Açıklama: 'Puantiyeli' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sven burnunu kara soktu ve elmayı aradı"
   - Cümle 4: «Sven burnunu kara soktu ve elmayı aradı.»
   - Açıklama: Kara batan elmanın aranması kuruluyor ama elma hiç bulunmuyor ve olay yarım kalıyor.
   - Açıklama: Kara batan elma aranıyor ama bulunup bulunmadığı hiç söylenmiyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yürüyüşlerine mutlu mutlu devam etti"
   - Cümle 10: «Sonra Elsa ile Sven karlı dağda yürüyüşlerine mutlu mutlu devam etti.»
   - Açıklama: Hikayenin başında dinleniyorlardı, yürümüyorlardı; yürüyüşe devam etmeleri çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0115` birebir aynı, `@degisim: filiz -> elma` (tutuyorsan), ardından `@onarim: d2263c48c8f1ee078f4389c517a9a4bc0ff19ccb`, sonra gövde.

### Hikâye 10: tohum elsa-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0116
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'davul', fiil 'kurutmak', sıfat 'rahat'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: bir dalga davulu ıslattı ve davul ses vermedi | elinden çıkan buzla yeni bir davul yaptı
@tohum: elsa-0116
Limanda hafif bir rüzgar esiyordu. Elsa orada Olaf için bir davul çalmak istiyordu. Ama bir dalga kıyıdaki davulu ıslattı ve davul ses vermedi. Olaf uzakta gemilere bakıyordu ve hiçbir şey görmedi. Elsa davulu kurutmak istedi, ama bu çok uzun sürecekti. Elsa ellerini açtı ve elinden buz çıktı. Buzdan parlak, yeni bir davul yaptı. Davula vurunca güzel bir ses çıktı. Sonra Elsa Olaf'ı yanına çağırdı. Olaf gelip bir taşın üstüne rahatça oturdu. Elsa buzdan davulu çaldı. Olaf neşeyle zıpladı ve güldü. Olaf çok sevindi, çünkü bu sürpriz onun içindi.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bu sürpriz onun içindi"
   - Cümle 13: «Olaf çok sevindi, çünkü bu sürpriz onun içindi.»
   - Açıklama: Hikayede daha önce sürpriz diye bir şey anılmadığı için 'bu sürpriz' neyi gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0116` birebir aynı, ardından `@onarim: ce1e02da2a683ae6d68f309a60c6ec3f4891a661`, sonra gövde.

### Hikâye 11: tohum elsa-0117 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0117
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'silgi', fiil 'dolaşmak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: dolabın altında gri ve küçük bir şey vardı | buzdan uzun bir çubukla onu dışarı çekti
@tohum: elsa-0117
Sarayın büyük salonunda Elsa dolaşıyordu. Birden dolabın altında gri, küçük bir şey gördü. Elsa bunun ne olduğunu çok merak etti. Ama dolabın altı çok dardı ve kolu sığmadı. Elsa biraz düşündü. Sonra elini açtı ve elinden buz çıktı. Buzdan ince, uzun bir çubuk yaptı. Elsa çubukla o şeyi yavaşça dışarı çekti. Bu, işaretli küçük bir silgiydi. Üstünde mavi bir kar tanesi vardı. Elsa onu hemen tanıdı, çünkü kaybolan kendi silgisiydi. Elsa onu alıp masaya oturdu ve mutlu mutlu resim yaptı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "dolabın altında gri, küçük bir şey gördü"
   - Cümle 2: «Birden dolabın altında gri, küçük bir şey gördü.»
   - Açıklama: Sorun yalnızca belirsiz bir merak; sebebi söylenmiyor ve çocuğun önemseyeceği bir kayıp baştan kurulmuyor.
   - Açıklama: Sorunun sebebi (silginin nasıl kaybolup dolabın altına girdiği) hiç söylenmiyor ve sorun yalnız meraktan ibaret kalıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elsa bunun ne olduğunu çok merak etti.»
   - Açıklama: İlk üç cümlede yalnız bir merak var; asıl sorun olan ulaşamama 4. cümlede, kayıp silgi ise ancak sonda ortaya çıkıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu, işaretli küçük bir silgiydi"
   - Cümle 9: «Bu, işaretli küçük bir silgiydi.»
   - Açıklama: 'İşaretli' belirsiz ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0117` birebir aynı, ardından `@onarim: 3b3b2e766da206eff35c8ad316dc6574a193b1f8`, sonra gövde.

### Hikâye 12: tohum elsa-0118 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0118
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: kaybolan eşya
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'minder', fiil 'fırlatmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: rüzgar minderi fırlattı ve minder karda kayboldu | geyiğe kar yığınını gösterdi ve geyik minderi buldu
@tohum: elsa-0118
Dağda sert bir rüzgar esiyordu. Elsa buzdan sarayın önünde Sven ile oturuyordu. Birden rüzgar Elsa'nın yanındaki mavi minderi havaya fırlattı. Minder uçtu, karların içine düştü ve kayboldu. Elsa rüzgarın estiği yöne baktı ve küçük bir kar yığını gördü. "Sven, şu kar yığınına git ve orada ara!" dedi Kraliçe Elsa. Sven hemen koştu ve burnuyla kazdı. Sonra minderi ağzıyla kardan çıkardı. Minder sırılsıklamdı, ama bozulmamıştı. Sven minderi Elsa'nın önüne bıraktı. "Aferin, Sven, çok akıllısın!" dedi Elsa. Elsa çok sevindi, çünkü Sven onun sözünü dinlemiş ve minderi bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 6: «"Sven, şu kar yığınına git ve orada ara!" dedi Kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak süs gibi geçiyor, karttaki özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir, kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0118` birebir aynı, ardından `@onarim: 56d748f6e01bb0b9a7cb2e758e6835046711b337`, sonra gövde.
