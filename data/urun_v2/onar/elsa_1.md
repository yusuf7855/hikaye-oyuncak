# Editör görevi (onarım): Elsa, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0001 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0001
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yağmur ya da kar günü
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çöp', fiil 'ekmek', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kar birden çok hızlı yağmaya başladı | kardeşini açık kapının altında korudu ve bahçeyi bitirdi
@tohum: elsa-0001
@degisim: çöp -> dal
Elsa ile Anna dağda, sarayın önünde kar bahçesi yapıyordu. Anna karın içine küçük dallar ekiyordu. Birden kar çok hızlı yağmaya başladı. "Elsa, saçlarım karla doldu!" dedi Anna. Kraliçe Elsa kardeşinin elini hemen tuttu. "Gel, Anna, kapının altında bekleyelim," dedi Elsa. İki kardeş sarayın açık kapısının altına koştu. Orada yan yana durup yağan karı izlediler. Biraz sonra kar yavaşladı. Elsa ile Anna bahçeye geri döndü. Anna kalan dalları da tek tek ekti. Elsa bahçenin çevresine küçük kar topları dizdi. "Elsa, bu en güzel kar bahçesi oldu!" dedi Anna.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "açık kapının altında korudu"
   - Cümle 0 (plan satırı): «kar birden çok hızlı yağmaya başladı | kardeşini açık kapının altında korudu ve bahçeyi bitirdi»
   - Açıklama: Kapının altında durulmaz; 'kapının önünde' ya da 'saçağın altında' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşinin elini"
   - Cümle 5: «Kraliçe Elsa kardeşinin elini hemen tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Anna, kapının altında bekleyelim"
   - Cümle 6: «"Gel, Anna, kapının altında bekleyelim," dedi Elsa.»
   - Açıklama: 'Kapının altında' çocuk için kelimenin tam anlamıyla kapının altı demek; 'kapının önünde' ya da 'kapının içinde' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "açık kapısının altına koştu"
   - Cümle 7: «İki kardeş sarayın açık kapısının altına koştu.»
   - Açıklama: Kapının altına koşulmaz; kelime yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0001` birebir aynı, `@degisim: çöp -> dal` (tutuyorsan), ardından `@onarim: f3fbb56a6683a420f1496273d0d51079f743e865`, sonra gövde.

### Hikâye 2: tohum elsa-0002 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0002
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çit', fiil 'dinlenmek', sıfat 'yaratıcı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: kardan evler düz olmayan yerde aşağı kaydı | evlerin önüne buzdan uzun bir çit yaptı
@tohum: elsa-0002
Hafif bir rüzgar esiyordu. Elsa ormanda kardan evler yapıp yaratıcı bir köy oyunu oynuyordu. Ama yer düz değildi ve küçük evler aşağı doğru kaydı. Elsa evleri tuttu ve yerlerine geri koydu. Evler bir kez daha kaydı. Elsa durdu ve biraz düşündü. Sonra elinden buz çıkardı ve evlerin önüne uzun bir çit yaptı. Çit evleri sıkıca tuttu. Artık hiçbir ev aşağı kaymadı. Elsa bir ağacın altına oturdu ve dinlendi. Sonra köyüne iki ev daha yaptı. Elsa oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "yaratıcı bir köy oyunu"
   - Cümle 2: «Elsa ormanda kardan evler yapıp yaratıcı bir köy oyunu oynuyordu.»
   - Açıklama: 'Yaratıcı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çit evleri sıkıca tuttu"
   - Cümle 8: «Çit evleri sıkıca tuttu.»
   - Açıklama: Çit bir şeyi elle tutar gibi tutamaz; fiil öznesine tam uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Elsa bir ağacın altına oturdu ve dinlendi"
   - Cümle 10: «Elsa bir ağacın altına oturdu ve dinlendi.»
   - Açıklama: Ağacın altında dinlenme olaydan çıkmıyor ve hiçbir işe yaramıyor.
   - Açıklama: Ağaç altında dinlenme olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0002` birebir aynı, ardından `@onarim: 750974c776fd47b9e8db2086f0c84d4fe130026a`, sonra gövde.

### Hikâye 3: tohum elsa-0003 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0003
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'şemsiye', fiil 'yemek', sıfat 'sıcak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: rüzgar esti ve şemsiye karın içinde durmadı | şemsiyenin dibine buzdan sağlam bir ayak yaptı
@tohum: elsa-0003
Bir sabah Elsa ile Olaf kıyıda sıcak yaz günü oyunu oynuyordu. Olaf büyük bir şemsiyeyi karın içine dikti. Ama rüzgar esti ve şemsiye yere düştü. Olaf onu tekrar dikti, ama şemsiye yine devrildi. "Elsa, bu şemsiye hiç durmuyor!" dedi Olaf. Elsa eğildi ve şemsiyenin dibine buzdan sağlam bir ayak yaptı. Rüzgar bir kez daha esti, ama şemsiye bu kez kıpırdamadı. İkisi şemsiyenin altına oturdu. Olaf kardan iki küçük kek hazırladı ve birini Elsa'ya verdi. İkisi de kekleri yiyormuş gibi yaptı. "Bu kek çok lezzetli!" dedi Olaf ve güldü. Elsa çok sevindi, çünkü şemsiyeleri artık rüzgarda hiç düşmüyordu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Olaf büyük bir şemsiyeyi karın içine dikti"
   - Cümle 2: «Olaf büyük bir şemsiyeyi karın içine dikti.»
   - Açıklama: Sıcak yaz günü deniz kıyısında kar sebepsiz beliriyor, nereden geldiği söylenmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "şemsiyeyi karın içine dikti"
   - Cümle 2: «Olaf büyük bir şemsiyeyi karın içine dikti.»
   - Açıklama: Sıcak yaz gününde deniz kıyısında kar sebepsiz beliriyor; nereden geldiği söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0003` birebir aynı, ardından `@onarim: 98d9f8be7c96f1952a693b2dc2866c3c5e748539`, sonra gövde.

### Hikâye 4: tohum elsa-0004 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0004
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yelpaze', fiil 'söylemek', sıfat 'özel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: buz taşıyan dağ adamı çok terlemişti | buzdan bir yelpaze yapıp ona verdi
@tohum: elsa-0004
Bir sabah Elsa dağda, sarayının önünde yürüyordu. Kristoff orada kızağına ağır buz parçaları yüklüyordu. Uzun süre çalıştığı için çok terlemişti. Kristoff, Elsa'ya biraz serinlemek istediğini söyledi. Elsa ona yardım etmek istedi. Ellerini açtı ve buzdan ince bir yelpaze yaptı. "Bunu dene, Kristoff," dedi Elsa. Kristoff yelpazeyi yüzüne doğru salladı. Hemen serin bir rüzgar esti. "Bu çok özel bir yelpaze!" dedi Kristoff. Sonra yelpazeyi kızağın kenarına koydu ve işine döndü. Kalan parçaları da kızağa yükledi. Elsa çok sevindi, çünkü Kristoff artık rahatça çalışabiliyordu.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "buzdan bir yelpaze yapıp ona verdi"
   - Cümle 0 (plan satırı): «buz taşıyan dağ adamı çok terlemişti | buzdan bir yelpaze yapıp ona verdi»
   - Açıklama: Gövdede Elsa'nın buzdan yelpaze yaptığı hiç anlatılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Uzun süre çalıştığı için çok terlemişti"
   - Cümle 3: «Uzun süre çalıştığı için çok terlemişti.»
   - Açıklama: Terlemek küçük bir çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
   - Açıklama: Yan karakterin terlemesi 3-6 yaş çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "yelpazeyi kızağın kenarına koydu"
   - Cümle 11: «Sonra yelpazeyi kızağın kenarına koydu ve işine döndü.»
   - Açıklama: Çözüm olan yelpaze hemen kenara bırakılıyor ve serinleme etkisi sürmediği halde sorun çözülmüş sayılıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yelpazeyi kızağın kenarına koydu ve işine döndü"
   - Cümle 11: «Sonra yelpazeyi kızağın kenarına koydu ve işine döndü.»
   - Açıklama: Kristoff yelpazeyi bırakıp işe dönüyor ama son cümle yelpaze sayesinde artık rahatça çalışabildiğini söylüyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra yelpazeyi kızağın kenarına koydu ve işine döndü"
   - Cümle 11: «Sonra yelpazeyi kızağın kenarına koydu ve işine döndü.»
   - Açıklama: Kristoff yelpazeyi bir kenara bırakıp işe dönüyor ama son cümle serinleme sayesinde rahatça çalışabildiğini söylüyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra yelpazeyi kızağın kenarına koydu"
   - Cümle 11: «Sonra yelpazeyi kızağın kenarına koydu ve işine döndü.»
   - Açıklama: Kristoff yelpazeyi bırakıp işine dönüyor ama son cümle yelpaze sayesinde rahatça çalıştığını söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0004` birebir aynı, ardından `@onarim: a8e1dce9bbe5f66a18cfdb1dbd1f8bccf9e7076c`, sonra gövde.

### Hikâye 5: tohum elsa-0005 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0005
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'fıçı', fiil 'hoşlanmak', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: ince dal çok esnekti ve hemen eğildi | buzdan sağlam bir kaşık yapıp çorbayı karıştırdı
@tohum: elsa-0005
Bir sabah Elsa dağda, sarayının önünde yemek yapma oyunu oynuyordu. Boş bir fıçıyı karla doldurdu ve kar çorbası yaptı. Ama çorbayı karıştırmak için kaşığı yoktu. Elsa yerden ince bir dal aldı. Dal çok esnekti ve karın içinde hemen eğildi. Elsa biraz düşündü. Sonra buzdan uzun, sağlam bir kaşık yaptı. Bu kaşıkla çorba güzelce karıştı. Elsa çorbanın tadına bakıyormuş gibi yaptı ve güldü. Bu yemek oyunundan çok hoşlandı. Elsa çok sevindi, çünkü kar çorbası sonunda hazırdı.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ince dal çok esnekti ve hemen eğildi"
   - Cümle 0 (plan satırı): «ince dal çok esnekti ve hemen eğildi | buzdan sağlam bir kaşık yapıp çorbayı karıştırdı»
   - Açıklama: Hikayenin sorunu çorbayı karıştıracak kaşığın olmaması; esnek dal yalnızca başarısız bir deneme.
   - Açıklama: Hikayenin asıl sorunu çorbayı karıştıracak kaşığın olmaması; plan yalnız ara bir denemeyi sorun diye yazıyor.
   - Açıklama: Gövdedeki asıl sorun kaşık olmaması; esnek dal yalnız başarısız bir deneme, plan sorunu yanlış söylüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Dal çok esnekti ve"
   - Cümle 5: «Dal çok esnekti ve karın içinde hemen eğildi.»
   - Açıklama: 'esnek' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Dal çok esnekti"
   - Cümle 5: «Dal çok esnekti ve karın içinde hemen eğildi.»
   - Açıklama: 'Esnek' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kavram.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu kaşıkla çorba güzelce karıştı"
   - Cümle 8: «Bu kaşıkla çorba güzelce karıştı.»
   - Açıklama: 'karıştı' burada yanlış anlamda; çorba kendiliğinden karışmaz, 'karıştırıldı' ya da 'Elsa çorbayı karıştırdı' olmalı.
   - Açıklama: Çorba kendi kendine karışmaz; 'karıştırdı' ya da 'karıştırıldı' olmalı.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Bu yemek oyunundan çok hoşlandı."
   - Cümle 10: «Bu yemek oyunundan çok hoşlandı.»
   - Açıklama: Hemen ardından gelen 'Elsa çok sevindi' ile aynı duyguyu gereksiz yere tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0005` birebir aynı, ardından `@onarim: dfee0c4173d114f140bc60ac487dfdfea8d0a085`, sonra gövde.

### Hikâye 6: tohum elsa-0006 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0006
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'poğaça', fiil 'toplanmak', sıfat 'soğuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: dağda garip bir ses duyuldu | sesi aradı ve geyiğin aç karnını buldu
@tohum: elsa-0006
Bir sabah Elsa ile Sven dağda yürüyordu. Elsa'nın kolunda poğaça dolu bir sepet vardı. Birden yakından garip bir ses duyuldu. "Bu ses nereden geliyor, Sven?" diye sordu Elsa. Sven de şaşırdı ve etrafına baktı. Elsa büyük bir kayanın arkasını kontrol etti. Orada yalnız soğuk kar toplanmıştı. Ses yine geldi ve bu kez çok yakındı. Elsa kulağını Sven'in karnına yaklaştırdı. "Sven, bu ses senin karnından geliyor!" dedi Elsa ve güldü. Elsa buzdan küçük bir masa yaptı ve poğaçaları üstüne dizdi. Sven iki poğaçayı hemen yedi. Elsa da bir poğaça yedi. Sonra Elsa ile Sven yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (7):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geyiğin aç karnını buldu"
   - Cümle 0 (plan satırı): «dağda garip bir ses duyuldu | sesi aradı ve geyiğin aç karnını buldu»
   - Açıklama: Aç karın bulunacak bir şey değil; fiil nesnesine uymuyor.
   - Açıklama: Sesin kaynağı bulunur, 'aç karın' bulunmaz; fiil nesnesine uymuyor.
   - Açıklama: Bir karın 'bulunmaz'; sesin geyiğin aç karnından geldiğini buldu denmeliydi.
   - Açıklama: Aç karın bulunacak bir nesne değil; 'bulmak' fiili nesnesine uymuyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "geyiğin aç karnını buldu"
   - Cümle 0 (plan satırı): «dağda garip bir ses duyuldu | sesi aradı ve geyiğin aç karnını buldu»
   - Açıklama: Gövdede Sven'in aç olduğu ya da sesin karnından geldiği hiç söylenmiyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yakından garip bir ses duyuldu"
   - Cümle 3: «Birden yakından garip bir ses duyuldu.»
   - Açıklama: Sesin sebebi (Sven'in aç karnı) gövdede hiç açıkça söylenmiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sven de şaşırdı ve etrafına baktı"
   - Cümle 5: «Sven de şaşırdı ve etrafına baktı.»
   - Açıklama: Ses Sven'in kendi karnından geldiği halde Sven şaşırıp sesi etrafta arıyor.
   - Açıklama: Ses Sven'in kendi karnından geldiği halde Sven sesin nereden geldiğine şaşırıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa büyük bir kayanın arkasını kontrol etti"
   - Cümle 6: «Elsa büyük bir kayanın arkasını kontrol etti.»
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor; boşa giden arama adımıyla ikiden fazla adım sürüyor.
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor; boşa arama, dinleme, masa kurma ve besleme ile ikiden fazla adım sürüyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Elsa buzdan küçük bir masa yaptı"
   - Cümle 11: «Elsa buzdan küçük bir masa yaptı ve poğaçaları üstüne dizdi.»
   - Açıklama: Buz masa olayda hiçbir işe yaramıyor, poğaçalar sepetten de yenebilirdi.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "yürüyüşlerine mutlu mutlu devam etti"
   - Cümle 14: «Sonra Elsa ile Sven yürüyüşlerine mutlu mutlu devam etti.»
   - Açıklama: Sesin ne olduğu hiç söylenmediği için okur çözümü merak ederek kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0006` birebir aynı, ardından `@onarim: c047b0aef7a2d81e77887953440e52d722751d7c`, sonra gövde.

### Hikâye 7: tohum elsa-0007 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0007
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bağcık', fiil 'taramak', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: rüzgar esti ve mavi bağcığı uçup gitti | limanı gözleriyle taradı ve bağcığı buldu
@tohum: elsa-0007
@degisim: saygılı -> uzun
Bir sabah Elsa limanın kıyısında yürüyordu. Birden sert bir rüzgar esti. Elsa'nın mavi bağcığı çözüldü ve uçup gitti. Uzun kraliçe pelerini yere doğru kaymaya başladı. Elsa pelerini iki eliyle tuttu. Durdu ve limanı gözleriyle taradı. Bağcığı yolda göremedi. Taşların arasında da bir şey yoktu. Sonra yolun kenarındaki bir direğe baktı. Mavi bağcığı direğin dibinde gördü. Elsa direğe yürüdü ve bağcığı yavaşça aldı. Pelerinini yeniden sıkıca bağladı. Elsa çok sevindi, çünkü kaybolan bağcığı kendi başına bulmuştu.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "limanı gözleriyle taradı ve bağcığı buldu"
   - Cümle 0 (plan satırı): «rüzgar esti ve mavi bağcığı uçup gitti | limanı gözleriyle taradı ve bağcığı buldu»
   - Açıklama: Plan satırında da aynı mecazlı 'gözleriyle taramak' kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Uzun kraliçe pelerini yere"
   - Cümle 4: «Uzun kraliçe pelerini yere doğru kaymaya başladı.»
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız pelerin sıfatı olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik (kraliçedir, kız kardeşini korur) yalnız pelerin sıfatı olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız pelerin sıfatı olarak geçiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "limanı gözleriyle taradı"
   - Cümle 6: «Durdu ve limanı gözleriyle taradı.»
   - Açıklama: 'gözleriyle taramak' 3 yaşındaki çocuğa uygun olmayan mecazlı bir anlatım.
   - Açıklama: 'Gözleriyle taramak' mecazlı anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Gözleriyle taramak' mecazlı bir anlatım ve küçük çocuk için anlaşılmaz.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Durdu ve limanı gözleriyle taradı"
   - Cümle 6: «Durdu ve limanı gözleriyle taradı.»
   - Açıklama: Arama yol, taşlar ve direk olmak üzere ikiden fazla adım sürüyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bağcığı yolda göremedi"
   - Cümle 7: «Bağcığı yolda göremedi.»
   - Açıklama: Arama yol, taşlar ve direk olmak üzere ikiden fazla adım sürüyor.
   - Açıklama: Arama yol, taşlar ve direk olmak üzere üç adıma yayılıyor; çözüm en çok 2 adımı aşıyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Taşların arasında da bir şey yoktu"
   - Cümle 8: «Taşların arasında da bir şey yoktu.»
   - Açıklama: Arama yol, taşlar ve direk olmak üzere birden çok denemeye uzuyor, çözüm 2 adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0007` birebir aynı, `@degisim: saygılı -> uzun` (tutuyorsan), ardından `@onarim: e62fb3a703c49b270a8afa02c3f8b2b755373af8`, sonra gövde.

### Hikâye 8: tohum elsa-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0008
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'küp', fiil 'dökülmek', sıfat 'meşgul'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: dağda tıkır tıkır garip bir ses geldi | dökülen küpleri gördü ve deliği buzla kapattı
@tohum: elsa-0008
Bir sabah Elsa dağda, sarayının yanında yürüyordu. Birden yukarıdan tıkır tıkır garip bir ses geldi. Elsa çok merak etti ve o yöne doğru yürüdü. Orada Kristoff kızağına buz küpleri yüklüyordu. Kristoff çok meşguldü ve arkasına hiç bakmıyordu. Kızağın arkasında küçük bir delik vardı. Küpler bu delikten tek tek yere dökülüyordu. Küpler taşlara düşünce tıkır tıkır ses çıkarıyordu. Garip ses buradan geliyordu. Elsa hemen ellerini deliğe tuttu ve deliği ince bir buzla kapattı. Artık hiçbir küp dökülmedi. Kristoff arkasına dönünce yerdeki küpleri topladı ve Elsa'ya teşekkür etti. Elsa çok sevindi, çünkü hem sesi bulmuş hem de Kristoff'a yardım etmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Kristoff çok meşguldü"
   - Cümle 5: «Kristoff çok meşguldü ve arkasına hiç bakmıyordu.»
   - Açıklama: 'Meşgul' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Kristoff çok meşguldü ve"
   - Cümle 5: «Kristoff çok meşguldü ve arkasına hiç bakmıyordu.»
   - Açıklama: 'Meşgul' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Küpler bu delikten tek tek yere dökülüyordu"
   - Cümle 7: «Küpler bu delikten tek tek yere dökülüyordu.»
   - Açıklama: Garip ses sorunu Kristoff'un kızağından dökülen küpler sorununa dönüşüyor; iki ayrı sorun var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0008` birebir aynı, ardından `@onarim: 704e11f6e50186b1e5a67ad8df01ba1908d54bb7`, sonra gövde.

### Hikâye 9: tohum elsa-0009 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0009
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'küpe', fiil 'karşılaşmak', sıfat 'harika'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: neşeli dostu da küpe takmak istedi | bir küpe verdi ve onu dala astı
@tohum: elsa-0009
Bir sabah Elsa ormanda yürürken Olaf'la karşılaştı. Elsa'nın kulaklarında, buzdan yaptığı iki küçük küpe vardı. "Ne harika küpeler, Elsa, ben de takmak isterdim!" dedi Olaf. Elsa hemen bir küpe çıkardı ve Olaf'a uzattı. "Bir küpe senin, bir küpe benim olsun," dedi Elsa. Ama Olaf'ın hiç kulağı yoktu! Olaf şaşkın şaşkın Elsa'ya baktı. Elsa biraz düşündü. Sonra küpeyi Olaf'ın kafasındaki küçük dala astı. Küpe dalda sallandı ve güneşte parladı. Olaf sevinçle zıpladı ve Elsa'ya sıkıca sarıldı. Elsa ile Olaf çok sevindi, çünkü artık ikisi de küpe takıyordu.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "neşeli dostu da küpe takmak istedi"
   - Cümle 0 (plan satırı): «neşeli dostu da küpe takmak istedi | bir küpe verdi ve onu dala astı»
   - Açıklama: Plan, çözülen asıl sorunu (Olaf'ın kulağı olmadığı için küpe takamaması) söylemiyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Elsa'nın kulaklarında, buzdan yaptığı"
   - Cümle 2: «Elsa'nın kulaklarında, buzdan yaptığı iki küçük küpe vardı.»
   - Açıklama: Yer tamlayıcısından sonra gereksiz virgül kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "buzdan yaptığı iki küçük küpe"
   - Cümle 2: «Elsa'nın kulaklarında, buzdan yaptığı iki küçük küpe vardı.»
   - Açıklama: Tohumdaki buz özelliği sorunun çözümünde işe yarar biçimde kullanılmıyor; sorun küpeyi dala asarak çözülüyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Olaf'ın hiç kulağı yoktu"
   - Cümle 6: «Ama Olaf'ın hiç kulağı yoktu!»
   - Açıklama: Asıl sorun olan Olaf'ın kulağının olmaması ilk 3 cümlede değil 6. cümlede ortaya çıkıyor.
   - Açıklama: Asıl engel olan Olaf'ın kulağının olmaması ilk 3 cümlede değil ancak 6. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0009` birebir aynı, ardından `@onarim: efe63510c7e8ceb6619c227d1afffaf2cb60c18b`, sonra gövde.

### Hikâye 10: tohum elsa-0010 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0010
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'beşik', fiil 'silkmek', sıfat 'faydalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: tek bir havuç vardı ve geyik çok acıkmıştı | havucu paylaştı ve yarısını buzdan tabağa koydu
@tohum: elsa-0010
@degisim: beşik -> havuç
Limanda hafif hafif kar yağıyordu. Elsa ile Sven iskelenin yanında dinleniyordu. Elsa'nın elinde tek bir havuç vardı, ama Sven de çok acıkmıştı. "Bu havucu paylaşalım, Sven," dedi Elsa. Sonra havucu ikiye böldü. Ama yer ıslak ve çamurluydu. Elsa buzdan küçük bir tabak yaptı. Havucun bir yarısını tabağın üstüne koydu. Havuç temiz kaldı ve bu tabak çok faydalı oldu. Sven havucunu hemen yedi. Sevinçle üstündeki karı silkti. Elsa da kendi yarısını yedi ve güldü. Elsa ile Sven limanda yan yana dinlenmeye mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama Sven de çok acıkmıştı"
   - Cümle 3: «Elsa'nın elinde tek bir havuç vardı, ama Sven de çok acıkmıştı.»
   - Açıklama: 'de' Elsa'nın da aç olduğunu ima ediyor ama bu söylenmemiş; 'ama' ile birlikte bağlaç anlamca yanlış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa'nın elinde tek bir havuç vardı"
   - Cümle 3: «Elsa'nın elinde tek bir havuç vardı, ama Sven de çok acıkmıştı.»
   - Açıklama: Tek havucun olması gerçek bir sorun kurmuyor; ikiye bölmekle hemen ve zahmetsizce çözülüyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama yer ıslak ve çamurluydu"
   - Cümle 6: «Ama yer ıslak ve çamurluydu.»
   - Açıklama: Havuç sorunu çözüldükten sonra ıslak yer ikinci bir sorun olarak ekleniyor.
   - Açıklama: Havuç paylaşımı çözüldükten sonra çamurlu yer ikinci bir sorun olarak geliyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "bu tabak çok faydalı oldu"
   - Cümle 9: «Havuç temiz kaldı ve bu tabak çok faydalı oldu.»
   - Açıklama: 'Faydalı' soyut bir kelime; 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Faydalı' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0010` birebir aynı, `@degisim: beşik -> havuç` (tutuyorsan), ardından `@onarim: a951c356834ace25ef6372a157c5adc7ce3d1995`, sonra gövde.

### Hikâye 11: tohum elsa-0011 (deneme 1 -> 2)

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
Deniz kıyısında Elsa ile Anna kumdan bir kale yapıyordu. Anna kalenin tepesine bir bayrak koymak istedi. Bir ağaçtan dal koparmaya çalıştı, ama eli yetmedi. "Elsa, dallar çok yüksek!" dedi Anna. "Bekle, Anna, sana bir bayrak yapayım," dedi Elsa. Elsa ellerini birleştirdi ve buzdan küçük bir bayrak yaptı. Bayrak güneşte pırıl pırıl parladı. Anna bayrağı dikkatle kalenin tepesine dikti. Kumdan kale artık tamamdı. Elsa ile Anna kalelerine sevinçle baktı. "Teşekkürler, Elsa, bu büyülü bayrak kaleye çok yakıştı!" dedi Anna.
```

**Hakem bulguları (3):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Elsa ile Anna kumdan bir kale yapıyordu"
   - Cümle 1: «Deniz kıyısında Elsa ile Anna kumdan bir kale yapıyordu.»
   - Açıklama: Kartın deniz tarifi krallığın önündeki fiyort kıyısı ve limanı diyor; kumsalda kumdan kale yapılan bir sahil bu tarifte yok.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama eli yetmedi"
   - Cümle 3: «Bir ağaçtan dal koparmaya çalıştı, ama eli yetmedi.»
   - Açıklama: 'Eli yetmedi' yanlış ve deyimsi bir kullanım; 'eli yetişmedi' ya da 'eli uzanmadı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "ama eli yetmedi"
   - Cümle 3: «Bir ağaçtan dal koparmaya çalıştı, ama eli yetmedi.»
   - Açıklama: 'Eli yetmedi' deyimsel bir kullanım; 'eli yetişmedi' ya da 'boyu yetmedi' daha somut olur.
   - Açıklama: 'Eli yetmedi' deyimsel bir kullanım; 'uzanamadı' gibi somut bir ifade gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0011` birebir aynı, ardından `@onarim: 352c0775fe2a09c3799af83e1a9ffd3533f27a08`, sonra gövde.
