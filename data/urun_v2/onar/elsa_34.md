# Editör görevi (onarım): Elsa, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0101 (deneme 3 -> 4)

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
Rüzgar karlı ağaçların arasında esiyordu. Elsa ormanda Olaf ile kardan büyük bir kale yapıyordu. Ama rüzgar her estiğinde kalenin ön duvarı sallanıyordu. Elsa duvarı elleriyle tutunca buz yapamıyordu. Bu yüzden Elsa, Olaf'tan yardım istedi. Olaf hemen duvarın yanına geldi ve onu sıkıca tuttu. Elsa ellerini açtı ve duvara ince bir buz gönderdi. Buz duvarın her yerine yavaşça yayıldı. Duvar sağlam oldu ve rüzgarda artık sallanmadı. Olaf kaleyi çok sevdi. Elsa, cömert Olaf'a sıkıca sarıldı ve ona teşekkür etti. İkisi kalenin içinde mutlu mutlu oyun oynadı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "duvara ince bir buz gönderdi"
   - Cümle 7: «Elsa ellerini açtı ve duvara ince bir buz gönderdi.»
   - Açıklama: Buz 'gönderilmez'; fiil nesnesine uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa, cömert Olaf'a sıkıca sarıldı"
   - Cümle 11: «Elsa, cömert Olaf'a sıkıca sarıldı ve ona teşekkür etti.»
   - Açıklama: Olaf bir şey paylaşmadı, yardım etti; 'cömert' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0101` birebir aynı, `@degisim: dolma -> duvar` (tutuyorsan), ardından `@onarim: d674363442566ee04f9d7f2bd828c809db6b0223`, sonra gövde.

### Hikâye 2: tohum elsa-0104 (deneme 2 -> 3)

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
Rüzgar esmeye başladı. Elsa dağın tepesinde, buzdan sarayının önünde küçük, mavi bir çiçek gördü. Rüzgar çiçeği çok sallıyordu. Çiçek narindi ve yaprakları kolayca kopabilirdi. Elsa bir kraliçeydi ve küçükleri hep korurdu. Hemen çiçeğin önüne eğildi. Sırtını rüzgara döndü ve iki elini çiçeğin çevresine koydu. Soğuk hava Elsa'ya çarptı ama çiçeğe gelmedi. Elsa orada durdu ve bir süre bekledi. Sonra rüzgar yavaşladı ve durdu. Elsa ellerini yavaşça çekti ve çiçeğe baktı. Mavi çiçek yine dik duruyordu ve yapraklarının hepsi yerindeydi. Elsa çok sevindi, çünkü çiçeği rüzgardan korumuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Çiçek narindi ve yaprakları"
   - Cümle 4: «Çiçek narindi ve yaprakları kolayca kopabilirdi.»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Narin' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0104` birebir aynı, `@degisim: gözlük -> yaprak` (tutuyorsan), ardından `@onarim: 79a43d62064a2fd22a60482eb0e8806dd0de5011`, sonra gövde.

### Hikâye 3: tohum elsa-0106 (deneme 2 -> 3)

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
@plan: karda bastonu olmayan arkadaş geride kaldı | bastonu sırayla kullanmak için kural koydu
@tohum: elsa-0106
Bir sabah Elsa ile Kristoff karlı ormanda yürüyordu. Kar çok derindi ve Kristoff'un bastonu yoktu. Bu yüzden Kristoff yavaş ilerliyor ve geride kalıyordu. Elsa'nın elinde ise uzun bir baston vardı. Kristoff dürüst davrandı ve çok yorulduğunu söyledi. Bunu duyunca Elsa bastonunu onunla paylaşmak istedi. Elsa kraliçeydi ve kısa bir kural koydu. Her büyük ağaçta bastonu birbirlerine vereceklerdi. İkisi de kurala uydu ve bastonu sırayla kullandı. Böylece kimse çok yorulmadı. Hiç ayrılmadan yan yana ormanın içinden geçtiler. Kristoff gülümsedi ve Elsa'ya teşekkür etti. Elsa bundan sonra bastonunu Kristoff ile hep paylaştı.
```

**Hakem bulguları (3):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Kristoff yavaş ilerliyor ve geride kalıyordu"
   - Cümle 3: «Bu yüzden Kristoff yavaş ilerliyor ve geride kalıyordu.»
   - Açıklama: Kartın ilişki alanında cesur dağ adamı olan Kristoff'un karda geride kalıp yorulması diziyi bilen çocuğa yanlış gelir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kristoff dürüst davrandı ve"
   - Cümle 5: «Kristoff dürüst davrandı ve çok yorulduğunu söyledi.»
   - Açıklama: Yorulduğunu söylemek dürüstlük sayılmaz; 'dürüst' kelimesi yerinde kullanılmamış.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hiç ayrılmadan yan yana ormanın içinden geçtiler"
   - Cümle 11: «Hiç ayrılmadan yan yana ormanın içinden geçtiler.»
   - Açıklama: Bastonsuz kalan geride kalıyorsa sırayla paylaşınca da biri hep bastonsuz olduğu halde hiç ayrılmamaları çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0106` birebir aynı, ardından `@onarim: fc029ed8121d91819e95e4649686fda32aa44943`, sonra gövde.

### Hikâye 4: tohum elsa-0110 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: karlı bir daldan ince bir ses geliyordu | daldaki karı itip altındaki zili buldu
@tohum: elsa-0110
@degisim: gizlenmek -> kalmak
Ormanda ağaçların üstünde kar tozu parlıyordu. Elsa uykuluydu ve sarayına dönmek istiyordu. Ama rüzgar esince yakındaki bir daldan ince bir ses geldi. Elsa sesi merak etti ve durdu. Dala baktı ama hiçbir şey göremedi. Dalın üstünde kalın bir kar vardı. Elsa kraliçeydi ve yolu göstermek için ağaçlara ziller asmıştı. Bu yüzden sesin bir zilden gelebileceğini düşündü. Elsa dalın üstündeki karı eliyle yavaşça itti. Küçük bir zil karın altında kalmıştı. Rüzgar yine esti ve zil bu kez daha yüksek sesle çaldı. Elsa çok sevindi, çünkü sesi yapan zili bulmuştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa uykuluydu ve sarayına dönmek istiyordu"
   - Cümle 2: «Elsa uykuluydu ve sarayına dönmek istiyordu.»
   - Açıklama: Uykululuk ve saraya dönme isteği kuruluyor ama hikayede hiç kullanılmıyor.
   - Açıklama: Elsa'nın uykulu olması ve saraya dönmek istemesi kuruluyor ama hikayede hiç kullanılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakındaki bir daldan ince bir ses geldi"
   - Cümle 3: «Ama rüzgar esince yakındaki bir daldan ince bir ses geldi.»
   - Açıklama: Bir sesin nereden geldiğini merak etmek gerçek bir sorun değil, çocuğun önemseyeceği bir güçlük kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "daldan ince bir ses geldi"
   - Cümle 3: «Ama rüzgar esince yakındaki bir daldan ince bir ses geldi.»
   - Açıklama: Daldan gelen bir ses gerçek bir sorun değil; çocuğun önemseyeceği bir güçlük kurulmuyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve yolu göstermek için ağaçlara ziller asmıştı"
   - Cümle 7: «Elsa kraliçeydi ve yolu göstermek için ağaçlara ziller asmıştı.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi (kız kardeşini koruyan kraliçe) kullanılmıyor ve çözüme bir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0110` birebir aynı, `@degisim: gizlenmek -> kalmak` (tutuyorsan), ardından `@onarim: 21e401928aacede8c293e6313436d719656da37f`, sonra gövde.

### Hikâye 5: tohum elsa-0111 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar hediye kutusunun kurdelesini uçurdu | rüzgarın estiği yöne yürüyüp kurdeleyi buldu
@tohum: elsa-0111
Bir sabah Elsa limanda Olaf için büyük bir hediye kutusu hazırlıyordu. Ama rüzgar esti ve kutunun kadife kurdelesi uçtu. Elsa bu limanın kraliçesiydi ve her yerini iyi bilirdi. Kurdeleyi bulmak için rüzgarın estiği yöne yürüdü. Kurdele limandaki kısa bir direğe takılmıştı. Elsa kurdeleyi aldı ve kutuya sıkıca bağladı. Tam o sırada Olaf limana geldi. "Olaf, bu hediye senin için!" dedi Elsa. Olaf kutuyu açtı ve içinde sarı bir güneş resmi gördü. "Yaz güneşi, en sevdiğim şey!" dedi Olaf. Olaf Elsa'ya sıcacık sarıldı ve ikisi limanda mutlu mutlu güldü.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kutunun kadife kurdelesi uçtu"
   - Cümle 2: «Ama rüzgar esti ve kutunun kadife kurdelesi uçtu.»
   - Açıklama: 'Kadife' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
   - Açıklama: 'Kadife' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kutunun kadife kurdelesi uçtu"
   - Cümle 2: «Ama rüzgar esti ve kutunun kadife kurdelesi uçtu.»
   - Açıklama: Kurdele uçuyor, Elsa yürüyüp hemen buluyor; sorun önemsiz ve kendiliğinden çözülen bir olay.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve kutunun kadife kurdelesi uçtu"
   - Cümle 2: «Ama rüzgar esti ve kutunun kadife kurdelesi uçtu.»
   - Açıklama: Rüzgarın kurdeleyi uçurması, yürüyüp bulunup bitiveren önemsiz bir olay; 'rüzgar dağıttı, topladı, bitti' kalıbına çok yakın.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu limanın kraliçesiydi"
   - Cümle 3: «Elsa bu limanın kraliçesiydi ve her yerini iyi bilirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği süs olarak anılıyor, çözüm rüzgarın yönüne yürümekle geliyor ve kartın 'kız kardeşini korur' özelliğine uygun işe yaramıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu limanın kraliçesiydi ve her yerini iyi bilirdi"
   - Cümle 3: «Elsa bu limanın kraliçesiydi ve her yerini iyi bilirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor; kurdele yalnız rüzgarın yönüne yürüyerek bulunuyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu limanın kraliçesiydi ve her yerini iyi bilirdi"
   - Cümle 3: «Elsa bu limanın kraliçesiydi ve her yerini iyi bilirdi.»
   - Açıklama: Limanı iyi bilmesi kurdeleyi bulmada hiçbir işe yaramıyor; işlevsiz ayrıntı.
   - Açıklama: Elsa'nın limanı iyi bilmesi işe yarayacakmış gibi kuruluyor ama çözümde kullanılmıyor; Elsa yalnız rüzgarın yönüne yürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0111` birebir aynı, ardından `@onarim: b20434648e99806f05a185da9a029d5c145c22a6`, sonra gövde.

### Hikâye 6: tohum elsa-0115 (deneme 2 -> 3)

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
@degisim: puantiyeli -> kırmızı
Bir sabah Elsa dağda Sven ile dinleniyordu. Sven karda yeşil filiz arıyordu. Ama karın altında hiç filiz yoktu. Elsa'nın sepeti kırmızı elmalarla dolmuştu. Elsa elmaları Sven ile paylaşmak istedi. İlk elmayı karın üstüne koydu ama elma derin kara battı. Sven burnunu kara soktu ve elmayı aradı. "Bekle, Sven, sana bir tabak yapayım," dedi Elsa. Elsa elini salladı ve buzdan geniş bir tabak yaptı. Tabağı karın üstüne koydu ve elmaların yarısını içine koydu. Sven başını salladı ve elmaları çıtır çıtır yedi. Sonra ikisi karlı dağda yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karda yeşil filiz arıyordu"
   - Cümle 2: «Sven karda yeşil filiz arıyordu.»
   - Açıklama: 'Filiz' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Ama karın altında hiç filiz yoktu.»
   - Açıklama: Elmanın kara batması sorunu ancak 6. cümlede söyleniyor; ilk üç cümle başka bir konuyu anlatıyor.
   - Açıklama: İlk üç cümle filiz bulunamamasını anlatıyor; plandaki elmanın kara batması sorunu ancak 6. cümlede geliyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama karın altında hiç filiz yoktu"
   - Cümle 3: «Ama karın altında hiç filiz yoktu.»
   - Açıklama: Filiz bulamama ve elmanın kara batması olmak üzere iki ayrı sorun var.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "elma derin kara battı"
   - Cümle 6: «İlk elmayı karın üstüne koydu ama elma derin kara battı.»
   - Açıklama: Sven'in yiyecek filiz bulamaması ve elmanın kara batması iki ayrı sorun olarak veriliyor.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Tabağı karın üstüne koydu ve elmaların yarısını içine koydu"
   - Cümle 10: «Tabağı karın üstüne koydu ve elmaların yarısını içine koydu.»
   - Açıklama: Aynı cümlede 'koydu' fiili gereksiz yere iki kez tekrarlanıyor.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "elmaların yarısını içine koydu"
   - Cümle 10: «Tabağı karın üstüne koydu ve elmaların yarısını içine koydu.»
   - Açıklama: Aynı cümlede 'koydu' fiili gereksiz yere iki kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0115` birebir aynı, `@degisim: puantiyeli -> kırmızı` (tutuyorsan), ardından `@onarim: 37f3282eab4d03268f638659f953dc09b9225bc4`, sonra gövde.
