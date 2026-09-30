# Editör görevi (onarım): Elsa, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0163 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0163
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'vanilya', fiil 'sabırsızlanmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: kapıyı kapadı ve kardan adamı dışarıda unuttu | özür diledi ve kapıya buzdan bir çan yaptı
@tohum: elsa-0163
@degisim: vanilya -> çan
Rüzgar dağın tepesinde sert esiyordu. Elsa buz sarayının büyük kapısını hemen kapadı. Ama Olaf daha dışarıdaydı ve Elsa ona bakmayı unutmuştu. Olaf kapalı kapıya vurdu, ama rüzgar çok gürültülüydü. Olaf kapının önünde sabırsızlanıyordu. Sonunda Elsa sesi duydu ve kapıyı açtı. "Özür dilerim, Olaf, seni dışarıda unuttum," dedi Elsa. "Tamam, ama bana sıkıca sarıl!" dedi Olaf. Elsa ona sıkıca sarıldı. Sonra Elsa elini salladı ve kapının yanına buzdan küçük bir çan yaptı. Olaf çanı çaldı ve çan güzel bir ses çıkardı. Elsa ile Olaf çok sevindi, çünkü Olaf artık gelince çanı çalabilecekti.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "özür diledi ve kapıya buzdan bir çan yaptı"
   - Cümle 0 (plan satırı): «kapıyı kapadı ve kardan adamı dışarıda unuttu | özür diledi ve kapıya buzdan bir çan yaptı»
   - Açıklama: Gövdede sorun kapının açılmasıyla çözülüyor; çan yalnız sonrası için bir önlem.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Olaf daha dışarıdaydı"
   - Cümle 3: «Ama Olaf daha dışarıdaydı ve Elsa ona bakmayı unutmuştu.»
   - Açıklama: 'Daha' burada 'hâlâ' anlamında yanlış kullanılmış; 'Olaf hâlâ dışarıdaydı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf kapının önünde sabırsızlanıyordu"
   - Cümle 5: «Olaf kapının önünde sabırsızlanıyordu.»
   - Açıklama: 'Sabırsızlanmak' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonunda Elsa sesi duydu ve kapıyı açtı"
   - Cümle 6: «Sonunda Elsa sesi duydu ve kapıyı açtı.»
   - Açıklama: Sorun Elsa'nın bir çabası olmadan, sesi kendiliğinden duymasıyla çözülüyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonunda Elsa sesi duydu ve kapıyı açtı"
   - Cümle 6: «Sonunda Elsa sesi duydu ve kapıyı açtı.»
   - Açıklama: Sorun Elsa'nın sebebe yönelen bir eylemiyle değil, sesi rastlantıyla duymasıyla çözülüyor.
   - Açıklama: Çözüm sebebe (Olaf'ı unutmak, gürültülü rüzgar) yönelmiyor; olay rastlantıyla çözülüyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonunda Elsa sesi duydu"
   - Cümle 6: «Sonunda Elsa sesi duydu ve kapıyı açtı.»
   - Açıklama: Rüzgar gürültüsü sesi bastırırken Elsa'nın sesi sonunda duyması çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0163` birebir aynı, `@degisim: vanilya -> çan` (tutuyorsan), ardından `@onarim: b1c6b4bdfa5f5404737b060f69bf51f1aa2bfabe`, sonra gövde.

### Hikâye 2: tohum elsa-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0164
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'dilim', fiil 'şişirmek', sıfat 'ince'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: limandan garip bir pat pat sesi geldi | geyiğe ipi çektirdi ve yelkeni direğe bağladı
@tohum: elsa-0164
@degisim: dilim -> yelken
Rüzgar limanda sert esiyordu. Birden Elsa teknelerin yanından garip bir "pat pat" sesi duydu. Elsa ile Sven bu sesi çok merak etti. İkisi sesin geldiği yere yavaşça yürüdü. Küçük bir teknenin ince yelkeni ipinden çözülmüştü. Rüzgar yelkeni şişirdi ve yelken direğe çarptı. Garip ses buradan geliyordu. Elsa yerdeki ipin ucunu aldı. "Sven, bu ipi ağzınla tut ve çek," dedi kraliçe Elsa. Sven ipi tuttu ve güçlü bir şekilde çekti. Yelken direğe doğru toplandı ve Elsa ipi sıkıca bağladı. Ses hemen kesildi. Elsa bundan sonra rüzgarlı günlerde teknelerin ipine baktı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "garip bir "pat pat" sesi duydu"
   - Cümle 2: «Birden Elsa teknelerin yanından garip bir "pat pat" sesi duydu.»
   - Açıklama: Sorun yalnız başkasının teknesinden gelen bir ses; çocuğun önemseyeceği bir kaybı ya da derdi yok.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa."
   - Cümle 9: «"Sven, bu ipi ağzınla tut ve çek," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 9: «"Sven, bu ipi ağzınla tut ve çek," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "günlerde teknelerin ipine baktı"
   - Cümle 13: «Elsa bundan sonra rüzgarlı günlerde teknelerin ipine baktı.»
   - Açıklama: Çoğul 'teknelerin' ile tekil 'ipine' uyumsuz; 'iplerine' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0164` birebir aynı, `@degisim: dilim -> yelken` (tutuyorsan), ardından `@onarim: 795e400e9f5cf4342138af1ca61d4b6ffd94fd75`, sonra gövde.

### Hikâye 3: tohum elsa-0165 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0165
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'teker', fiil 'ısınmak', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: arabanın tekeri bir taşa çarpıp çatladı | sarayın küçük arabasını paylaştı ve buzları taşıdılar
@tohum: elsa-0165
Bir sabah Kristoff limanda buz dolu arabasını çekiyordu. Elsa da oradaydı ve ona el salladı. Ama arabanın tekeri bir taşa çarptı ve çatladı. Araba yana yattı ve bir buz parçası yere düştü. Limanda sarayın küçük bir arabası duruyordu. Kraliçe Elsa bu arabayı hemen Kristoff ile paylaştı. Kristoff buzları yetenekli elleriyle yeni arabaya dizdi. Elsa da küçük buz parçalarını taşıdı. İkisi çalıştıkça ısındı ve yüzleri kızardı. Kristoff teşekkür için Elsa'ya en parlak buz parçasını verdi. Elsa o buzu güneşe tuttu ve güldü. Sonra Elsa ile Kristoff yeni arabayı mutlu mutlu birlikte çekti.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Limanda sarayın küçük bir arabası duruyordu"
   - Cümle 5: «Limanda sarayın küçük bir arabası duruyordu.»
   - Açıklama: Çözümü getiren saray arabası sebepsizce limanda hazır beliriyor.
   - Açıklama: Sarayın arabası limanda sebepsizce beliriyor ve çözümü hazır getiriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu arabayı hemen Kristoff ile paylaştı"
   - Cümle 6: «Kraliçe Elsa bu arabayı hemen Kristoff ile paylaştı.»
   - Açıklama: Elsa arabayı kendisi kullanmadığı için 'paylaştı' yanlış; 'verdi' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa bu arabayı"
   - Cümle 6: «Kraliçe Elsa bu arabayı hemen Kristoff ile paylaştı.»
   - Açıklama: Önceden tanıtılan Elsa unvanla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa bu arabayı"
   - Cümle 6: «Kraliçe Elsa bu arabayı hemen Kristoff ile paylaştı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor; yalnız unvan olarak geçiyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kristoff teşekkür için Elsa'ya"
   - Cümle 10: «Kristoff teşekkür için Elsa'ya en parlak buz parçasını verdi.»
   - Açıklama: 'Teşekkür için' eksik; 'teşekkür etmek için' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0165` birebir aynı, ardından `@onarim: 2eb0ff84c8d399b2ea58b87ad0a5d00b857521ab`, sonra gövde.

### Hikâye 4: tohum elsa-0166 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0166
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: bir şey yapmak
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'böğürtlen', fiil 'doğmak', sıfat 'konuşkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: sepetin altı yırtıldı ve böğürtlenler düştü | buzdan bir kase yaptı ve böğürtlenleri koydu
@tohum: elsa-0166
@degisim: konuşkan -> soğuk
Limanın kıyısında güneş yeni doğuyordu. Elsa böğürtlen dolu bir sepetle taşların üstüne oturdu. Ama sepetin altı birden yırtıldı. Böğürtlenler taşların arasına düşmeye başladı. Elsa yırtık yeri hemen bir eliyle tuttu. Sonra öbür elini salladı ve buzdan bir kase yaptı. Kase parlak ve soğuktu. Elsa böğürtlenleri tek tek kaseye koydu. Taşlara düşen böğürtlenleri de topladı. Böğürtlenler soğuk kasede taze kaldı. Elsa bir böğürtlen yedi ve denize baktı. Elsa çok sevindi, çünkü böğürtlenlerini kendi yaptığı kaseyle kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama sepetin altı birden yırtıldı"
   - Cümle 3: «Ama sepetin altı birden yırtıldı.»
   - Açıklama: Sepetin neden yırtıldığı söylenmiyor; sorunun sebebi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0166` birebir aynı, `@degisim: konuşkan -> soğuk` (tutuyorsan), ardından `@onarim: 00b1b07f6ea6daa046c722770920b790a68dcbdb`, sonra gövde.

### Hikâye 5: tohum elsa-0167 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0167
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tepsi', fiil 'çıkmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: ormanda garip bir su sesi geldi | sesi izleyip karı itti ve gizli suyu buldu
@tohum: elsa-0167
@degisim: tepsi -> su
Ormanda karlı ağaçların arasında her yer sessizdi. Elsa yürürken birden şırıl şırıl bir ses duydu. Ama hiçbir yerde su yoktu. Elsa bu sesi çok merak etti. Sesi izleyerek iki büyük ağacın arasına yürüdü. Ses burada daha güçlüydü. Elsa eğildi ve karı eliyle yavaşça kenara itti. Karın altından gizli, küçük bir su çıktı. Temiz su taşların arasından akıyordu. Kraliçe Elsa suyun iki yanına büyük taşlar dizdi. Böylece suyun yolu karla kapanmadı. Sonra Elsa suyun yanında oturdu ve sesini mutlu mutlu dinledi.
```

**Hakem bulguları (8):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama hiçbir yerde su yoktu"
   - Cümle 3: «Ama hiçbir yerde su yoktu.»
   - Açıklama: Sorun yalnız bir merak; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gizli, küçük bir su çıktı"
   - Cümle 8: «Karın altından gizli, küçük bir su çıktı.»
   - Açıklama: 'Küçük bir su' sayılabilir bir şey gibi kullanılmış; 'küçük bir dere' ya da 'akan su' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gizli, küçük bir su"
   - Cümle 8: «Karın altından gizli, küçük bir su çıktı.»
   - Açıklama: 'Küçük bir su' yanlış kelime; 'küçük bir dere' ya da 'su birikintisi' olmalı.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa suyun iki"
   - Cümle 10: «Kraliçe Elsa suyun iki yanına büyük taşlar dizdi.»
   - Açıklama: Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa suyun iki yanına"
   - Cümle 10: «Kraliçe Elsa suyun iki yanına büyük taşlar dizdi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa suyun iki"
   - Cümle 10: «Kraliçe Elsa suyun iki yanına büyük taşlar dizdi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; kartın özellik alanındaki gibi sorunu çözmekte kullanılmıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "suyun iki yanına büyük taşlar dizdi"
   - Cümle 10: «Kraliçe Elsa suyun iki yanına büyük taşlar dizdi.»
   - Açıklama: Suyun yolunun karla kapanması hiç sorun olarak kurulmadan yeni bir eylem ekleniyor.
   - Açıklama: Sorun su bulununca çözülmüş, taş dizme ve suyun karla kapanması sebepsiz eklenen işlevsiz bir ayrıntı.
8. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "oturdu ve sesini mutlu"
   - Cümle 12: «Sonra Elsa suyun yanında oturdu ve sesini mutlu mutlu dinledi.»
   - Açıklama: 'Sesini' zamirinin suyun mu Elsa'nın mı sesini gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0167` birebir aynı, `@degisim: tepsi -> su` (tutuyorsan), ardından `@onarim: 3f8a82a1b9db7070875778d4c67cf81dc1f77200`, sonra gövde.
