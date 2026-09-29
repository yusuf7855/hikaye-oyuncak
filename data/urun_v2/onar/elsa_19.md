# Editör görevi (onarım): Elsa, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0036 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0036
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kapı', fiil 'değiştirmek', sıfat 'kabarık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: kızak kabarık bir kar yığınına girip takıldı | kızaktan indi ve yolu değiştirdi
@tohum: elsa-0036
@degisim: kapı -> kızak
Karlı ormanda Elsa ile Sven kızak oyunu oynuyordu. Sven önde koşuyor, Elsa da kızakta neşeyle şarkı söylüyordu. Ama kızak kabarık bir kar yığınına girdi ve durdu. Sven bütün gücüyle çekti ama kızak hiç kıpırdamadı. Sven çok yoruldu. Elsa hemen kızaktan indi. Kızak hafifledi ve Sven onu kolayca geri çekti. Elsa kraliçeydi ve bu ormanın yollarını iyi biliyordu. "Sven, yolu değiştirelim, şu yolda kar sert," dedi Elsa. Sven başını salladı ve kızağı o yola götürdü. Elsa yeniden kızağa oturdu. Bu yolda kızak kolayca kaydı. Elsa ile Sven ağaçların arasında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve bu ormanın yollarını iyi biliyordu"
   - Cümle 8: «Elsa kraliçeydi ve bu ormanın yollarını iyi biliyordu.»
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşini korumak; karttaki gibi kullanılmıyor, yol bilme özelliğe eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0036` birebir aynı, `@degisim: kapı -> kızak` (tutuyorsan), ardından `@onarim: 11d3c0955ac78436df70c3f90a60cff1de17c41b`, sonra gövde.

### Hikâye 2: tohum elsa-0037 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0037
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'fıstık', fiil 'sallamak', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: buz sarayının kapısından garip bir ses geldi | dışarı çıkıp baktı ve düşen fıstıkları gördü
@tohum: elsa-0037
Bir sabah Elsa dağda, buz sarayında oturuyordu. Birden kapıdan garip bir tık tık sesi geldi. Elsa kraliçeydi ve sarayını korumak için önce pencereden baktı. Kapının önünde kimse yoktu. Elsa kapıyı açtı ve dışarı çıktı. Karın üstünde küçük kahverengi fıstıklar vardı. Elsa başını kaldırdı ve kapının yanındaki büyük ağacı gördü. Rüzgar ağacın dallarını sallıyordu. Bir fıstık daldan düştü ve kapıya çarptı. Tık tık sesi yine geldi. Elsa güldü. Bu eğlenceli sesi düşen fıstıklar yapıyordu. Sonra Elsa fıstıkları topladı ve onlarla karda mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve sarayını korumak için önce pencereden baktı"
   - Cümle 3: «Elsa kraliçeydi ve sarayını korumak için önce pencereden baktı.»
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşini korumak; burada yalnız adı anılıyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve sarayını korumak"
   - Cümle 3: «Elsa kraliçeydi ve sarayını korumak için önce pencereden baktı.»
   - Açıklama: Kartın özellik alanı kız kardeşini korumak diyor; burada saray koruma olarak süs gibi kullanılıyor ve çözüme katkı vermiyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sarayını korumak için önce pencereden baktı"
   - Cümle 3: «Elsa kraliçeydi ve sarayını korumak için önce pencereden baktı.»
   - Açıklama: Sesin kaynağına ulaşmak pencereden bakma, dışarı çıkma, ağaca bakma ve fıstığın düşmesini bekleme gibi ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0037` birebir aynı, ardından `@onarim: 6c177e45fb99938a6a0036494b2a0673e9e16c6f`, sonra gövde.

### Hikâye 3: tohum elsa-0041 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0041
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gül', fiil 'tanımak', sıfat 'uyanık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: havucu tanımadı ve onu yokuştan aşağı attı | özür diledi ve saraydan yeni havuç getirdi
@tohum: elsa-0041
@degisim: gül -> havuç
Karlı dağda, buzdan sarayın kapısında Elsa karı temizliyordu. Sven'in sakladığı havuç karla kaplıydı ve Elsa onu tanımadı. Elsa havucu karla birlikte yokuştan aşağı attı. Biraz sonra Sven geldi. Sven artık uyanıktı ve havucunu yemek istiyordu. Ama havucunu karda bulamadı ve üzgün üzgün baktı. Elsa hatasını hemen anladı. "Özür dilerim, Sven, havucunu ben attım," dedi Elsa. Elsa kraliçeydi ve sarayında her zaman havuç vardı. Hemen içeri girdi ve Sven'e yeni, büyük bir havuç getirdi. Sven havucu yedi ve Elsa'ya burnunu sürttü. Sonra Elsa ile Sven karda mutlu mutlu koştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve Elsa onu tanımadı"
   - Cümle 2: «Sven'in sakladığı havuç karla kaplıydı ve Elsa onu tanımadı.»
   - Açıklama: Kar altındaki havuç için 'tanımadı' yanlış fiil; 'fark etmedi' olmalı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elsa havucu karla birlikte yokuştan aşağı attı.»
   - Açıklama: İlk üç cümlede havucun atıldığı anlatılıyor ama bunun bir sorun olduğu ancak 6. cümlede Sven havucu bulamayınca ortaya çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sven artık uyanıktı"
   - Cümle 5: «Sven artık uyanıktı ve havucunu yemek istiyordu.»
   - Açıklama: Sven'in uyuduğu hiç kurulmadan birden uyandığı söyleniyor.
   - Açıklama: Sven'in uyuduğu hiç kurulmadan uyanık olduğu söyleniyor; sebepsiz bir ayrıntı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve sarayında her zaman havuç vardı"
   - Cümle 9: «Elsa kraliçeydi ve sarayında her zaman havuç vardı.»
   - Açıklama: Kartın özellikler alanında kraliçelik kız kardeşini korumakla tanımlı; burada sarayda havuç bulunmasının gerekçesi olarak karttakinden farklı kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0041` birebir aynı, `@degisim: gül -> havuç` (tutuyorsan), ardından `@onarim: ebe076e10b1ee7bd3ccf1ca7325e41fff3100acf`, sonra gövde.

### Hikâye 4: tohum elsa-0044 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0044
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kayık', fiil 'durmak', sıfat 'sabırsız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: arkadaşı da kaymak istedi ama kızağı yoktu | büyük kızağını paylaşıp onu arkasına oturttu
@tohum: elsa-0044
@degisim: kayık -> kızak
Ormanda hafif bir rüzgar esiyordu. Elsa küçük bir yokuştan kızakla kayıyordu. Olaf da kaymak istedi ama onun kızağı yoktu. "Ben de kaymak istiyorum!" dedi Olaf sabırsız bir sesle. Kızak aşağıda, Olaf'ın hemen önünde durdu. Elsa'nın kızağı büyük bir kraliçe kızağıydı. "Gel, Olaf, bu kızak ikimize de yeter," dedi Elsa. İkisi kızağı yokuşun başına çekti. Elsa öne oturdu ve kızağın ipini iki eliyle tuttu. Olaf onun arkasına yerleşti ve ona sıkıca tutundu. Kızak yavaşça aşağı indi. Olaf kollarını açtı ve kahkahalarla güldü. "Birlikte çok daha eğlenceli!" dedi Olaf. Elsa ile Olaf mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "büyük bir kraliçe kızağıydı"
   - Cümle 6: «Elsa'nın kızağı büyük bir kraliçe kızağıydı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız kızağa sıfat olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşi korumak; karttaki gibi değil, yalnız kızağa sıfat olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0044` birebir aynı, `@degisim: kayık -> kızak` (tutuyorsan), ardından `@onarim: fdfbf434ee1b2bcc190cb1a4dd565610942cc9ee`, sonra gövde.

### Hikâye 5: tohum elsa-0045 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0045
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çekirdek', fiil 'eklemek', sıfat 'mutsuz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yumuşak kardan yapılan kule yana devrildi | karı sıkıca bastırıp duvara yeni bir kule ekledi
@tohum: elsa-0045
@degisim: çekirdek -> duvar
Karlı dağda, buzdan sarayın yanında güneş parlıyordu. Elsa karla küçük bir kale yapıyordu. Ama kalenin uzun kulesi yumuşak kardandı ve birden yana devrildi. Elsa devrilen kuleye baktı ve biraz mutsuz oldu. Sonra kraliçe sarayının sert buz kulelerine baktı. Elsa yerden yeni kar aldı. Karı iki eliyle sıkıca bastırdı ve sert bir top yaptı. Bu sıkı kardan kalenin duvarına yeni bir kule ekledi. Elsa kuleye yavaşça dokundu. Yeni kule bu kez hiç devrilmedi ve duvarın üstünde dik durdu. Elsa kalesinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra kraliçe sarayının sert buz kulelerine baktı"
   - Cümle 5: «Sonra kraliçe sarayının sert buz kulelerine baktı.»
   - Açıklama: Kraliçe özelliği yalnız anılıyor, sorunun çözümünde karttaki gibi işe yaramıyor.
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşi korumak; yalnız saraya sıfat olarak geçiyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0045` birebir aynı, `@degisim: çekirdek -> duvar` (tutuyorsan), ardından `@onarim: 14e884988150d7bcccf3407ea4cfa71efac59880`, sonra gövde.

### Hikâye 6: tohum elsa-0047 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0047
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tarak', fiil 'gülümsemek', sıfat 'nazik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: tarak elinden kayıp derin karın içinde kayboldu | nazikçe yardım istedi ve geyiğin gösterdiği yeri kazdı
@tohum: elsa-0047
Karlı ormanda Elsa, Sven'in tüylerini tarıyordu. Birden tarak elinden kaydı ve kara düştü. Kar çok derindi ve tarak kayboldu. Elsa elleriyle aradı ama tarağı bulamadı. Elsa nazik bir kraliçeydi ve Sven'e yavaşça döndü. "Sven, tarağı bulmama yardım eder misin?" diye sordu Elsa. Sven burnunu kara soktu ve kokladı. Bir yerde durdu ve ayağıyla karı gösterdi. Elsa orayı kazdı ve tarağı karın içinden çıkardı. Elsa gülümsedi ve Sven'in başını okşadı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Elsa çok sevindi, çünkü yardım isteyince tarağını bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa nazik bir kraliçeydi"
   - Cümle 5: «Elsa nazik bir kraliçeydi ve Sven'e yavaşça döndü.»
   - Açıklama: Kraliçe özelliği yalnız etiket olarak geçiyor ve yanına nazik huyu ekleniyor; çözümde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0047` birebir aynı, ardından `@onarim: c64a3c4ae3a9290dcfec61bd5daa133d6313a077`, sonra gövde.

### Hikâye 7: tohum elsa-0051 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0051
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yelken', fiil 'susmak', sıfat 'masmavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yelken rüzgara ters durduğu için kızak kaymadı | bayrağa bakıp yelkeni rüzgara çevirdi
@tohum: elsa-0051
@degisim: susmak -> bakmak
Bir sabah Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu. Kızağa uzun bir dal dikmiş ve kraliçe pelerinini yelken yapmıştı. Ama kızak hiç kaymadı, çünkü yelken rüzgara ters duruyordu. Sarayın tepesinde bir bayrak vardı. Elsa bayrağa baktı ve rüzgarın sağdan estiğini gördü. Sonra yelkeni rüzgara doğru çevirdi. Yelken birden şişti. Kızak düz karın üstünde yavaş yavaş kaymaya başladı. Elsa kızağın içinde oturdu ve güldü. Kızak masmavi gökyüzünün altında sarayın önünde bir tur attı. Elsa çok sevindi, çünkü yeni bir şeyi denemiş ve başarmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe pelerinini yelken yapmıştı"
   - Cümle 2: «Kızağa uzun bir dal dikmiş ve kraliçe pelerinini yelken yapmıştı.»
   - Açıklama: Kraliçe özelliği karttaki gibi (kraliçelik, kardeşini koruma) değil, sıradan bir pelerin olarak kullanılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sarayın önünde bir tur attı"
   - Cümle 10: «Kızak masmavi gökyüzünün altında sarayın önünde bir tur attı.»
   - Açıklama: 'Tur atmak' kalıp bir anlatım; 3 yaşındaki çocuk için 'döndü' gibi somut bir fiil olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0051` birebir aynı, `@degisim: susmak -> bakmak` (tutuyorsan), ardından `@onarim: 04a6228d067a997eb14800d5c928ce0cd6d409d7`, sonra gövde.

### Hikâye 8: tohum elsa-0052 (deneme 3 -> 4)

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
@plan: önüne bakmadan koştu ve havuçları karda dağıttı | özür diledi ve havuçları bulup buzdan kaseye koydu
@tohum: elsa-0052
@degisim: yağmurluk -> havuç
Karlı ağaçların arasında hafif bir rüzgar esiyordu. Elsa, Sven'in havuçlarını karın üstüne dizmişti. Elsa ile enerjik Sven havuçların yanında koşup oynuyordu. Elsa önüne bakmadan koştu ve havuçları karın içine dağıttı. Sven karı kokladı ve üzgün bir ses çıkardı. "Özür dilerim, Sven, havuçlarını ben dağıttım," dedi Elsa. Sonra ikisi havuçları bulmak için birlikte çalıştı. Sven burnuyla, Elsa da elleriyle onları tek tek buldu. Havuçlar yine kaybolmasın diye Elsa buzdan bir kase yaptı. Havuçları kaseye koydu ve Sven'in önüne bıraktı. Sven başını Elsa'ya sürttü ve bir havuç yedi. Elsa bundan sonra ormanda koşarken hep önüne baktı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elsa ile enerjik Sven havuçların yanında koşup oynuyordu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0052` birebir aynı, `@degisim: yağmurluk -> havuç` (tutuyorsan), ardından `@onarim: 3715fc01995dd1bae7c3689b92acf7f1aef589fa`, sonra gövde.

### Hikâye 9: tohum elsa-0053 (deneme 3 -> 4)

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
Dışarıda kar sessizce yağıyordu. Kraliçe Elsa sarayın salonunu çabuk çabuk topluyordu. Acele edince Kristoff'un eldivenlerini bir dolaba koydu. Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı. "Elsa, eldivenlerimi gördün mü?" diye sordu Kristoff. "Özür dilerim, Kristoff, onları ben bir dolaba koydum," dedi Elsa. Ama salonda çok dolap vardı ve Elsa hangisi olduğunu unutmuştu. Elsa dolapları tek tek açtı. Eldivenler kapının yanındaki küçük dolaptaydı! Elsa eldivenleri Kristoff'a verdi. "Teşekkürler, Elsa, hadi şimdi birlikte dışarıda oynayalım!" dedi Kristoff.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sarayın salonunu"
   - Cümle 2: «Kraliçe Elsa sarayın salonunu çabuk çabuk topluyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı"
   - Cümle 4: «Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede ortaya çıkıyor; unutma ise yedinci cümlede söyleniyor.
   - Açıklama: Eldivenlerin bulunamaması sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa hangisi olduğunu unutmuştu"
   - Cümle 7: «Ama salonda çok dolap vardı ve Elsa hangisi olduğunu unutmuştu.»
   - Açıklama: Yan cümle eksik kurulmuş; 'hangisine koyduğunu unutmuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0053` birebir aynı, `@degisim: denemek -> açmak` (tutuyorsan), ardından `@onarim: 421e007dae6d666066117655982443239a986348`, sonra gövde.

### Hikâye 10: tohum elsa-0055 (deneme 3 -> 4)

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
Limanda hafif bir rüzgar esiyordu. Elsa kıyıda yürürken taşların arasında küçük bir yuva gördü. Yuvada üç küçük yumurta vardı, ama yuva yolun hemen yanındaydı. Yoldan geçen insanlar yumurtaları kırabilirdi. Elsa yuvaya elini sürmedi. O bir kraliçeydi ve yumurtaları korumak istedi. Kıyıdan düz taşlar topladı ve onları yuvanın önüne yan yana dizdi. Yuvanın önünde kısa ama sağlam bir duvar oldu. Elsa yuvaya bir kez daha baktı ve yumurtaları saydı. Elsa çok sevindi, çünkü üç yumurta da artık güvendeydi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "O bir kraliçeydi ve"
   - Cümle 6: «O bir kraliçeydi ve yumurtaları korumak istedi.»
   - Açıklama: Kraliçe özelliği yalnız etiket olarak söyleniyor; duvarı yapmak kraliçe olmayı gerektirmiyor, özellik işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "O bir kraliçeydi ve yumurtaları korumak istedi"
   - Cümle 6: «O bir kraliçeydi ve yumurtaları korumak istedi.»
   - Açıklama: Kartın özellikler alanında kraliçelik kız kardeşini korumak olarak tanımlı; burada yumurtaları korumaya genelleştiriliyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0055` birebir aynı, `@degisim: bölmek -> dizmek` (tutuyorsan), ardından `@onarim: 7ea009917210217aa74162b73bc718422b85d128`, sonra gövde.

### Hikâye 11: tohum elsa-0056 (deneme 3 -> 4)

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
Elsa buzdan sarayının önünde Sven ile oynuyordu. Sven sağlam bacaklarıyla karda yüksek yüksek zıplıyordu. Ama Elsa su içmek için saraya girdi ve Sven'e bakmayı unuttu. Sven karda yalnız kaldı ve başını öne eğdi. Elsa pencereden baktı ve Sven'in üzgün olduğunu gördü. Hemen dışarı koştu. Elsa bir kraliçeydi ve hatasını hemen düzeltmek istedi. Sven'e sarıldı ve ondan özür diledi. Sonra karın üstüne oturdu ve Sven'i izledi. Sven yeniden zıpladı ve bu kez daha yükseğe çıktı. Elsa onu gülerek alkışladı. Sven de başını sevinçle Elsa'ya sürttü. Elsa çok sevindi, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hatasını hemen düzeltmek istedi"
   - Cümle 7: «Elsa bir kraliçeydi ve hatasını hemen düzeltmek istedi.»
   - Açıklama: 'Hatasını düzeltmek' soyut bir ifade; 3 yaşındaki çocuk için somut değil.
   - Açıklama: 'Hatasını düzeltmek' küçük çocuk için soyut bir ifade.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve hatasını"
   - Cümle 7: «Elsa bir kraliçeydi ve hatasını hemen düzeltmek istedi.»
   - Açıklama: Kraliçe özelliği yalnız etiket olarak geçiyor; özür dilemek kraliçe olmaya bağlı değil.
   - Açıklama: Kartın özellik alanındaki kraliçelik ve kız kardeşi koruma yerine hatayı düzeltme gerekçesi olarak süs gibi kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve hatasını hemen düzeltmek istedi"
   - Cümle 7: «Elsa bir kraliçeydi ve hatasını hemen düzeltmek istedi.»
   - Açıklama: Kraliçe olmak hatayı düzeltme isteğine sebep değil; özellik olay akışına zorla sokulmuş.
   - Açıklama: Kraliçe olmak hatayı düzeltme isteğine sebep olarak bağlanıyor ama olayla hiçbir mantıksal ilişkisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0056` birebir aynı, `@degisim: tartı -> pencere` (tutuyorsan), ardından `@onarim: e424bafc159da818dc90dd407946fcfd5ec008e5`, sonra gövde.

### Hikâye 12: tohum elsa-0057 (deneme 3 -> 4)

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
Dağın tepesinde Kraliçe Elsa, ışıltılı oyuncak trompetiyle bir ses oyunu oynuyordu. Trompeti her çaldığında, ses dağlardan geri geliyordu. Ama birden rüzgar esti ve trompetin içine kar doldu. Elsa yine üfledi, ama trompetten hiç ses çıkmadı. Dağlardan da hiç ses gelmedi. Elsa trompetin içine baktı ve karı gördü. Trompeti ters çevirdi ve iki kez salladı. Bütün kar yere döküldü. Elsa bir kez daha üfledi ve trompet yüksek bir ses çıkardı. Ses dağlardan geri geldi ve Elsa güldü. Elsa bundan sonra rüzgar esince trompetinin ağzını eliyle kapattı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Dağın tepesinde Kraliçe Elsa"
   - Cümle 1: «Dağın tepesinde Kraliçe Elsa, ışıltılı oyuncak trompetiyle bir ses oyunu oynuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) sorunun çözümünde işe yaramıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0057` birebir aynı, `@degisim: küçültmek -> sallamak` (tutuyorsan), ardından `@onarim: 9d98ed7d6177aa6aa0705db915815dbd986a8fd4`, sonra gövde.
