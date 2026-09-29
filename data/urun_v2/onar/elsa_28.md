# Editör görevi (onarım): Elsa, onarım partisi 28

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar28.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar28.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0011 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0011
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kum', fiil 'koparmak', sıfat 'büyülü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: bayrak için dal gerekti ama dallar çok yüksekteydi | kardeşine buzdan küçük bir bayrak yaptı
@tohum: elsa-0011
@degisim: kum -> kar
Limanın kıyısında Elsa ile Anna kardan bir kale yapıyordu. Anna kalenin tepesine bir bayrak koymak istedi. Bir ağaçtan dal koparmak istedi, ama dallar çok yüksekteydi. "Elsa, dala ulaşamıyorum!" dedi Anna. "Bekle, Anna, sana bir bayrak yapayım," dedi Elsa. Elsa ellerini birleştirdi ve buzdan küçük bir bayrak yaptı. Bayrak güneşte pırıl pırıl parladı. Anna bayrağı dikkatle kalenin tepesine dikti. Kardan kale artık tamamdı. Elsa ile Anna kalelerine sevinçle baktı. "Teşekkürler, Elsa, bu büyülü bayrak kaleye çok yakıştı!" dedi Anna.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kardeşine buzdan küçük bir bayrak yaptı"
   - Cümle 0 (plan satırı): «bayrak için dal gerekti ama dallar çok yüksekteydi | kardeşine buzdan küçük bir bayrak yaptı»
   - Açıklama: Planda bayrağı Elsa yapıyor, gövdede ise Anna yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0011` birebir aynı, `@degisim: kum -> kar` (tutuyorsan), ardından `@onarim: 2b71618c62d3c14e7b396f4eb211f763a99d6c66`, sonra gövde.

### Hikâye 2: tohum elsa-0065 (deneme 5 -> 6)

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
@degisim: sergilemek -> göstermek
Elsa ile Anna dağın tepesindeki buz sarayının önündeydi. Anna yeni kızağını Elsa'ya gösteriyordu. Kızakla ilk kez kaymak istiyordu ama sarayın kapısından inen yol çok dikti. Anna aşağıya bakınca kızağını bıraktı. Elsa bir kraliçeydi ve kardeşini korumak istedi. Sarayın arkasında küçük bir tepe buldu. Tepenin altı düz ve genişti. "Anna, burada deneyelim," dedi Elsa. Anna küçük tepeye çıktı ve kızağa oturdu. Elsa kızağı arkadan tuttu ve hafifçe itti. Anna aşağı kaydı ve bir fidenin yanında yavaşça durdu. Sonra güldü ve hemen ayağa kalktı. "Teşekkürler, Elsa, kızakla kaymak çok güzelmiş!" dedi Anna.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir fidenin yanında"
   - Cümle 11: «Anna aşağı kaydı ve bir fidenin yanında yavaşça durdu.»
   - Açıklama: 'Fide' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir fidenin yanında yavaşça"
   - Cümle 11: «Anna aşağı kaydı ve bir fidenin yanında yavaşça durdu.»
   - Açıklama: 'Fide' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0065` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: 92a8eca2cb94383ad43cb289f9f6c458b1d7a6f4`, sonra gövde.

### Hikâye 3: tohum elsa-0066 (deneme 5 -> 6)

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
Bir sabah Elsa ile Sven karlı dağda yürüyordu. Elsa'nın filesinde Sven için küçük bir su kabı vardı. Sven çok susamıştı, ama yerdeki kar çok tozluydu. Kraliçe Elsa, Sven'i güneşli bir kayanın yanına götürdü. Kayanın üstündeki buz eriyordu ve su damla damla düşüyordu. Elsa fileden kabı çıkardı ve kayanın altına koydu. Kap yavaş yavaş temiz suyla doldu. Elsa kabı Sven'in önüne bıraktı. Sven suyu hızlıca içti ve sevinçle başını salladı. Sonra Elsa ile Sven dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa'nın filesinde Sven için"
   - Cümle 2: «Elsa'nın filesinde Sven için küçük bir su kabı vardı.»
   - Açıklama: 'File' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Sven'i güneşli bir kayanın"
   - Cümle 4: «Kraliçe Elsa, Sven'i güneşli bir kayanın yanına götürdü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Sven'i güneşli bir kayanın yanına götürdü"
   - Cümle 4: «Kraliçe Elsa, Sven'i güneşli bir kayanın yanına götürdü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0066` birebir aynı, ardından `@onarim: fd13987f5bb362f369ba37ad40374dfed154777d`, sonra gövde.

### Hikâye 4: tohum elsa-0070 (deneme 5 -> 6)

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
@plan: sarayın bir yeri kırılıyor gibi bir ses duydu | balkona yürüdü ve sesi yapan şişeyi buldu
@tohum: elsa-0070
@degisim: testi -> şişe
Dağın tepesindeki buz sarayında soğuk bir rüzgar esiyordu. Elsa içeride ince bir ses duydu. Bir yerin kırıldığını sandı. Elsa iyi bir kraliçeydi ve sarayını korumak istedi. Hemen sesin geldiği yere yürüdü. Balkonda boş bir şişe duruyordu. Ama etrafta kırık bir şey yoktu. Rüzgar şişenin ağzına esiyordu ve ses oradan çıkıyordu. Birden rüzgar dindi ve ses de durdu. Elsa şişenin yanında biraz bekledi. Rüzgar yeniden esti ve şişeden yine aynı ses geldi. Elsa çok sevindi, çünkü saray kırılmamıştı ve bu tatlı ses şişeden geliyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu tatlı ses şişeden"
   - Cümle 12: «Elsa çok sevindi, çünkü saray kırılmamıştı ve bu tatlı ses şişeden geliyordu.»
   - Açıklama: Sese 'tatlı' demek mecazdır, küçük çocuk için uygun değil.
   - Açıklama: Ses için 'tatlı' mecazlı bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0070` birebir aynı, `@degisim: testi -> şişe` (tutuyorsan), ardından `@onarim: d40901b36c089a3494ae7333a0ae263ac7f8e2c9`, sonra gövde.

### Hikâye 5: tohum elsa-0071 (deneme 5 -> 6)

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
Bir sabah Elsa dağda Kristoff'un yanına geldi. Kristoff onun için kızağındaki buz parçalarıyla bir ayçiçeği yapıyordu. Ama rüzgar esti ve çiçeğin ince bir yaprağı düşüp kırıldı. "Çiçeği bitiremedim," dedi Kristoff üzgün bir sesle. Kraliçe Elsa, Kristoff'a yardım etmek istedi. Kızaktaki buz parçalarına baktı. İnce ve yaprağa benzeyen bir parça buldu. "Bu parça yaprak olabilir mi?" diye sordu Elsa. Elsa parçayı çiçeğin boş yerine dikkatle yerleştirdi. Parça boş yere tam sığdı ve ayçiçeği tamamlandı. "Çok güzel oldu, Elsa!" dedi Kristoff. Sonra Elsa ile Kristoff buzdan ayçiçeğinin yanında mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Kristoff'a yardım etmek istedi"
   - Cümle 5: «Kraliçe Elsa, Kristoff'a yardım etmek istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözüm kraliçelikle ilgili değil.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Parça boş yere tam"
   - Cümle 10: «Parça boş yere tam sığdı ve ayçiçeği tamamlandı.»
   - Açıklama: 'boş yere' deyim olarak 'nafile' anlamına geliyor; 'boş yere sığdı' yanlış anlaşılır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0071` birebir aynı, ardından `@onarim: 93ab96e656f82c509edd2a3a61c07510685bd103`, sonra gövde.

### Hikâye 6: tohum elsa-0073 (deneme 5 -> 6)

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
@plan: rüzgar eldiveni karın içine düşürdü ve eldiven görünmedi | sesin geldiği yeri buldu ve eldiveni buzdan kürekle çıkardı
@tohum: elsa-0073
@degisim: saat -> eldiven
Elsa, Sven ile karlı ormanda yürüyordu. Rüzgar esti ve Elsa'nın elindeki eldiveni karın içine düşürdü. Elsa yere baktı ama eldiveni göremedi. "Sven, eldivenimi bulmama yardım eder misin?" diye sordu Elsa. Sven başını salladı ve karı koklamaya başladı. Biraz sonra bir ağacın dibinden hışır hışır bir ses geldi. Elsa bu sesi merak etti ve ağaca doğru yürüdü. Orada eldivenin ucu karın içinden çıkmıştı ve rüzgarda sallanıyordu. Elsa buzdan küçük bir kürek yaptı. Küreği yavaşça kara soktu ve eldiveni çıkardı. Eldiven ıslaktı ama hiç yırtılmamıştı. Sven sevinçle kısa bir ses verdi. Elsa çok sevindi, çünkü eldivenini sesin geldiği yerde bulmuştu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "eldiveni buzdan kürekle çıkardı"
   - Cümle 0 (plan satırı): «rüzgar eldiveni karın içine düşürdü ve eldiven görünmedi | sesin geldiği yeri buldu ve eldiveni buzdan kürekle çıkardı»
   - Açıklama: 'Buzdan kürekle' belirsiz ve eksik kurulmuş; 'buzdan bir kürekle' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sven başını salladı ve karı koklamaya başladı"
   - Cümle 5: «Sven başını salladı ve karı koklamaya başladı.»
   - Açıklama: Sven'in koklaması işe yarayacakmış gibi kuruluyor ama kullanılmıyor; eldiveni sebepsizce beliren bir ses buldurur.
   - Açıklama: Sven'in koklaması işe yarayacakmış gibi kuruluyor ama eldiveni sebepsizce beliren bir ses buldurur.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sonra bir ağacın dibinden hışır hışır bir ses geldi"
   - Cümle 6: «Biraz sonra bir ağacın dibinden hışır hışır bir ses geldi.»
   - Açıklama: Çözümü getiren ses önceki olaydan çıkmıyor, rastlantıyla beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0073` birebir aynı, `@degisim: saat -> eldiven` (tutuyorsan), ardından `@onarim: 2f4d60aa4b54e21dd1bfc6047619eac926144927`, sonra gövde.

### Hikâye 7: tohum elsa-0074 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0074
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yastık', fiil 'erimek', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: güneşli yerde kar erimişti ve yer ıslaktı | sık dallı bir ağacın altında kuru bir yer buldu
@tohum: elsa-0074
Bir sabah Elsa ilk kez ormanda piknik yapmayı denedi. Elinde bir yastık ve küçük bir sepet vardı. Ama güneşli yerde kar erimişti ve yer çok ıslaktı. Elsa yastığını ıslak yere koyamadı. Elsa bu krallığın kraliçesiydi ve ormandaki ağaçları iyi tanıyordu. Hemen büyük, yeşil bir çam ağacına gitti. Ağacın sık dalları karı tutmuştu, bu yüzden altı kuruydu. Elsa yastığını ağacın altındaki kuru yere koydu. Sonra sepetinden ekmek ve elma çıkardı. Elsa yastığına oturdu ve ilk pikniğini mutlu mutlu yaptı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu krallığın kraliçesiydi ve ormandaki ağaçları iyi tanıyordu"
   - Cümle 5: «Elsa bu krallığın kraliçesiydi ve ormandaki ağaçları iyi tanıyordu.»
   - Açıklama: Kartın kraliçe özelliği (kız kardeşini korur) yerine ağaçları tanıma gerekçesi olarak zorlanarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0074` birebir aynı, ardından `@onarim: 70a360d5ec35b45ad52d9d58150feedec3dd9ff7`, sonra gövde.

### Hikâye 8: tohum elsa-0078 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0078
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'sünger', fiil 'yakalanmak', sıfat 'sihirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: karda her yerde ayak izi vardı ve saklanan bulunamadı | kar yağdırıp eski izleri kapattı ve yeni izleri buldu
@tohum: elsa-0078
@degisim: sünger -> kaya
Elsa ile Kristoff dağda saklambaç oynuyordu. Kristoff kayaların arkasına saklanmıştı. Ama karda her yerde eski ayak izleri vardı ve Elsa onu bulamadı. Elsa biraz düşündü ve ellerini gökyüzüne kaldırdı. Ellerinden buz taneleri ve sihirli bir kar yağdı. Yeni kar bütün eski izleri kapattı. "Kristoff, şimdi yeniden saklan!" dedi Elsa. Kristoff kayanın arkasından çıktı ve başka bir kayanın arkasına koştu. Bu kez karda yalnız onun yeni ayak izleri vardı. Elsa izlerin peşinden gitti ve Kristoff'u buldu. "Tamam, yakalandım!" dedi Kristoff gülerek. Elsa çok sevindi, çünkü saklanan Kristoff'u sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kristoff, şimdi yeniden saklan!"
   - Cümle 7: «"Kristoff, şimdi yeniden saklan!" dedi Elsa.»
   - Açıklama: Çözüm saklanan Kristoff'u bulmuyor, oyunu yeniden başlatıp üç adımda sonuca varıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kristoff kayanın arkasından çıktı ve başka bir kayanın arkasına koştu"
   - Cümle 8: «Kristoff kayanın arkasından çıktı ve başka bir kayanın arkasına koştu.»
   - Açıklama: Kristoff Elsa'nın gözü önünde saklanıyor, bu yüzden izleri takip ederek bulmak çözümü anlamsız kılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0078` birebir aynı, `@degisim: sünger -> kaya` (tutuyorsan), ardından `@onarim: ec4d86a2f70b17f2170e148a95e10b126417c0c6`, sonra gövde.

### Hikâye 9: tohum elsa-0080 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0080
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kutu', fiil 'sevmek', sıfat 'biberli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik acıkmıştı ve kutudaki ekmekler biberliydi | kutudaki havuçları ona verdi
@tohum: elsa-0080
Elsa elinde bir yemek kutusuyla sarayından çıktı. Kapının önünde Sven burnuyla karı karıştırıyordu. Karın altında hiç ot yoktu ve Sven çok acıkmıştı. Elsa kraliçeydi ve kutusuna saraydan iki havuç da koymuştu. Hemen kutusunu açtı. Kutunun içinde üstte biberli ekmekler, altta havuçlar vardı. Sven bir ekmeği kokladı ve başını çevirdi. "Biberli ekmeği sevmiyorsun, değil mi?" diye sordu Elsa. Sven başını iki yana salladı. Elsa ekmekleri kaldırdı ve iki havucu aldı. Havuçları hemen Sven'e uzattı. Sven onları yedi ve sevinçle zıpladı. "Afiyet olsun, Sven, bunlar senin için!" dedi Elsa gülerek.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kutudaki ekmekler biberliydi"
   - Cümle 0 (plan satırı): «geyik acıkmıştı ve kutudaki ekmekler biberliydi | kutudaki havuçları ona verdi»
   - Açıklama: Gövdede sorun karın altında ot olmadığı için Sven'in acıkması; biberli ekmek sorunun sebebi değil, sonradan çıkan bir ayrıntı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve kutusuna saraydan iki havuç"
   - Cümle 4: «Elsa kraliçeydi ve kutusuna saraydan iki havuç da koymuştu.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümle nedensel bağ kurmadan süs olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve kutusuna saraydan iki havuç da koymuştu"
   - Cümle 4: «Elsa kraliçeydi ve kutusuna saraydan iki havuç da koymuştu.»
   - Açıklama: Kraliçelik işlevsiz bir ayrıntı ve havuçlar çözümü sebepsizce hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0080` birebir aynı, ardından `@onarim: f567317f72803849d76d750995e8236235eea575`, sonra gövde.

### Hikâye 10: tohum elsa-0084 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0084
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'eşarp', fiil 'yaratmak', sıfat 'temiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: rüzgar kardan arkadaşın başını yere düşürdü | başı yerine koyup boynuna eşarp bağladı
@tohum: elsa-0084
@degisim: yaratmak -> yapmak
Rüzgar karlı ağaçların arasında çok sert esiyordu. Elsa ile Olaf ormanda kardan küçük bir arkadaş yapıyordu. Ama rüzgar kardan arkadaşın başını yere düşürdü. "Arkadaşımın başı düştü, Elsa!" dedi Olaf üzgün üzgün. Elsa bir kraliçeydi ve boynunda uzun, temiz bir eşarp vardı. Hemen Olaf'ın yanına eğildi. Başı yerine koydu ve karı iki eliyle bastırdı. Sonra eşarbını boynundan çıkardı. Eşarbı yeni arkadaşın boynuna sıkıca bağladı. Rüzgar yine esti ama baş artık düşmedi. "Yaşasın, yeni arkadaşım hazır!" dedi Olaf. Elsa ile Olaf yeni arkadaşın yanında mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Arkadaşımın başı düştü, Elsa!"
   - Cümle 4: «"Arkadaşımın başı düştü, Elsa!" dedi Olaf üzgün üzgün.»
   - Açıklama: Arkadaş diye anılan kardan figürün başının düşmesi küçük çocuk için ürkütücü bir imge.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0084` birebir aynı, `@degisim: yaratmak -> yapmak` (tutuyorsan), ardından `@onarim: 4d903462595f3b69929b7c1bf76c15ff05cf53a6`, sonra gövde.

### Hikâye 11: tohum elsa-0085 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0085
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ekmek', fiil 'dilemek', sıfat 'siyah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: kurabiye torbası kaygan karda kayıp aşağıdaki kara düştü | geyikten yardım diledi ve geyik torbayı getirdi
@tohum: elsa-0085
@degisim: ekmek -> kurabiye
Karlı dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Kraliçe Elsa, Sven için siyah bir torbada kurabiye getirmişti. Ama torba kaygan karda kaydı ve biraz aşağıdaki karın içine düştü. Elsa oraya gidemedi, çünkü ayakları yumuşak karda batıyordu. Elsa, Sven'den yardım diledi. "Sven, torbayı bana getirir misin?" diye sordu Elsa. Sven uzun bacaklarıyla karda kolayca yürüdü. Siyah torbayı beyaz karda hemen gördü. Torbayı dişleriyle tuttu ve yukarı çıktı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Sven sevinçle başını salladı. Sonra ikisi sarayın önünde oturdu ve kurabiyeleri mutlu mutlu paylaştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Sven için"
   - Cümle 2: «Kraliçe Elsa, Sven için siyah bir torbada kurabiye getirmişti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Elsa, Sven'den yardım diledi."
   - Cümle 5: «Elsa, Sven'den yardım diledi.»
   - Açıklama: Yardım isteği önce anlatılıyor, hemen ardından replikle yeniden veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0085` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: 17d65a06b0e0d5624decd9363614eba32b4b0b7d`, sonra gövde.

### Hikâye 12: tohum elsa-0087 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0087
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kese', fiil 'kullanmak', sıfat 'berrak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: soğukta ip donup sıkı bir düğüm oldu | düğümü açmak için arkadaşından yardım istedi
@tohum: elsa-0087
@degisim: berrak -> mavi
Elsa, Kristoff ile karlı dağda yürüyordu. Kraliçe Elsa kurabiye yemek için küçük bir keseyi açmak istedi. Ama soğukta ipi donmuş ve sıkı bir düğüm olmuştu. Elsa düğümü tek başına açamadı. "Kristoff, bu düğümü açabilir misin?" diye sordu Elsa. Kristoff keseyi aldı ve güçlü parmaklarını kullandı. Önce düğümü avucunda biraz ısıttı. Sonra ipi yavaşça çekti ve düğüm açıldı. "İşte kurabiyeler, Elsa!" dedi Kristoff. Elsa kurabiyeleri ikiye böldü ve yarısını Kristoff'a verdi. İkisi mavi gökyüzünün altında kurabiyelerini yedi. Elsa çok mutlu oldu, çünkü yardım isteyince düğüm hemen açılmıştı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kurabiye yemek"
   - Cümle 2: «Kraliçe Elsa kurabiye yemek için küçük bir keseyi açmak istedi.»
   - Açıklama: Önceki cümlede tanıtılan Elsa unvanıyla ikinci kez tanıtılıyor.
   - Açıklama: Elsa ilk cümlede tanıtıldıktan sonra 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kurabiye yemek"
   - Cümle 2: «Kraliçe Elsa kurabiye yemek için küçük bir keseyi açmak istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, düğümü Kristoff açıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "soğukta ipi donmuş ve sıkı bir düğüm olmuştu"
   - Cümle 3: «Ama soğukta ipi donmuş ve sıkı bir düğüm olmuştu.»
   - Açıklama: Donmak ipi düğüm yapmaz; sorunun sebebi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0087` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: c6c8018d25bdb8eadd1ff2a611c340750b81ca2b`, sonra gövde.
