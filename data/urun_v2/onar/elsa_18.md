# Editör görevi (onarım): Elsa, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0067 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ormanda garip bir tak tak sesi geldi | sese doğru yürüyüp sallanan tahtayı buldu
@tohum: elsa-0067
Elsa, Sven ile karlı ormanda yürüyordu. Birden ağaçların arasından tak tak diye bir ses geldi. Sven hemen durdu ve Elsa bu sesi çok merak etti. "Gel, Sven, sesin nereden geldiğine bakalım," dedi Elsa. Kraliçe Elsa önden yürüdü ve Sven onu izledi. Bir ağacın dalında eski bir tahta asılıydı. Tahtanın üstünde kırmızı bir ok vardı. Rüzgar esince tahta uçacak gibi sallanıyor ve ağaca vuruyordu. Ses bu tahtadan geliyordu. Kırmızı ok şatonun yolunu gösteriyordu. Elsa tahtayı daldan aldı ve karın içine sıkıca dikti. Elsa çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağaçların arasından tak tak diye bir ses geldi"
   - Cümle 2: «Birden ağaçların arasından tak tak diye bir ses geldi.»
   - Açıklama: Sorun yalnız merak edilen bir ses; çocuğun önemseyeceği gerçek bir sorun yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa önden yürüdü"
   - Cümle 5: «Kraliçe Elsa önden yürüdü ve Sven onu izledi.»
   - Açıklama: Zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa önden yürüdü"
   - Cümle 5: «Kraliçe Elsa önden yürüdü ve Sven onu izledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) sorunu çözmede kullanılmıyor, yalnız unvan olarak geçiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tahtanın üstünde kırmızı bir ok vardı"
   - Cümle 7: «Tahtanın üstünde kırmızı bir ok vardı.»
   - Açıklama: Şatonun yolunu gösteren kırmızı ok işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tahta uçacak gibi sallanıyor"
   - Cümle 8: «Rüzgar esince tahta uçacak gibi sallanıyor ve ağaca vuruyordu.»
   - Açıklama: 'Uçacak gibi' abartılı bir mecaz; tahta uçmaz.
   - Açıklama: 'Uçacak gibi' benzetmesi küçük çocuğa uygun olmayan bir mecaz.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kırmızı ok şatonun yolunu gösteriyordu"
   - Cümle 10: «Kırmızı ok şatonun yolunu gösteriyordu.»
   - Açıklama: Şatonun yolunu gösteren ok işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "karın içine sıkıca dikti"
   - Cümle 11: «Elsa tahtayı daldan aldı ve karın içine sıkıca dikti.»
   - Açıklama: Tahtanın neden karın içine dikildiği söylenmiyor ve olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0067` birebir aynı, ardından `@onarim: dd468fbc3111353684545bd71f5c8fe022bb2ff7`, sonra gövde.

### Hikâye 2: tohum elsa-0070 (deneme 1 -> 2)

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
@plan: sarayda nereden geldiği bilinmeyen bir ses vardı | sesin geldiği yere yürüyüp testiyi buldu
@tohum: elsa-0070
Dağın tepesindeki buz sarayında soğuk bir rüzgar esiyordu. Elsa sarayın içinde tatlı bir ses duydu. Ses uzun ve ince bir ıslık gibiydi. Elsa bu sesi çok merak etti. Kraliçe Elsa sesin geldiği yere doğru yürüdü. Sarayın balkonunda bir testi duruyordu. Elsa testiyi su doldurmak için oraya koymuştu. Rüzgar testinin boş ağzına esiyordu. Ses tam oradan çıkıyordu. Birden rüzgar dindi ve ses de durdu. Elsa testinin yanında biraz bekledi. Rüzgar yeniden esti ve testiden yine aynı ses geldi. Elsa çok sevindi, çünkü o güzel sesin testiden geldiğini bulmuştu.
```

**Hakem bulguları (8):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "içinde tatlı bir ses"
   - Cümle 2: «Elsa sarayın içinde tatlı bir ses duydu.»
   - Açıklama: 'tatlı ses' mecazdır; ses tatlı olmaz.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Ses uzun ve ince bir ıslık gibiydi.»
   - Açıklama: İlk 3 cümlede yalnız bir ses duyuluyor; bunun bir sorun olduğu ve merak edildiği ancak 4. cümlede söyleniyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa sesin geldiği"
   - Cümle 5: «Kraliçe Elsa sesin geldiği yere doğru yürüdü.»
   - Açıklama: Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
   - Açıklama: Önceden tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sesin geldiği yere"
   - Cümle 5: «Kraliçe Elsa sesin geldiği yere doğru yürüdü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sesin geldiği"
   - Cümle 5: «Kraliçe Elsa sesin geldiği yere doğru yürüdü.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa testiyi su doldurmak için"
   - Cümle 7: «Elsa testiyi su doldurmak için oraya koymuştu.»
   - Açıklama: Yapı bozuk; 'testiyi suyla doldurmak' ya da 'testiye su doldurmak' olmalı.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "testiyi su doldurmak için"
   - Cümle 7: «Elsa testiyi su doldurmak için oraya koymuştu.»
   - Açıklama: Doldurmak fiili bu yapıda uymuyor; 'testiye su doldurmak' ya da 'testiyi suyla doldurmak' olmalı.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa testiyi su doldurmak için oraya koymuştu"
   - Cümle 7: «Elsa testiyi su doldurmak için oraya koymuştu.»
   - Açıklama: Testinin balkona su doldurmak için konması akla yatkın bir sebep değil ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0070` birebir aynı, ardından `@onarim: f29bfa31c86e6cb5b82541b311e430cac7941d56`, sonra gövde.

### Hikâye 3: tohum elsa-0071 (deneme 1 -> 2)

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
Bir sabah Elsa dağda Kristoff'un yanına geldi. Kristoff buzdan bir ayçiçeği yapıyordu. Ama rüzgar esti ve çiçeğin ince bir yaprağı düşüp parça parça oldu. "Çiçeği bitiremedim," dedi Kristoff üzgün bir sesle. Kraliçe Elsa kızaktaki buz parçalarına baktı. İnce ve yaprağa benzeyen bir parça buldu. "Bu parça yaprak olabilir mi?" diye sordu Elsa. Elsa parçayı çiçeğin boş yerine dikkatle yerleştirdi. Parça tam oturdu ve ayçiçeği tamamlandı. Kristoff çiçeğe baktı ve kocaman gülümsedi. "Çok güzel oldu, Elsa!" dedi Kristoff. Sonra Elsa ile Kristoff ayçiçeğini buz sarayına mutlu mutlu götürdü.
```

**Hakem bulguları (7):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kristoff buzdan bir ayçiçeği yapıyordu"
   - Cümle 2: «Kristoff buzdan bir ayçiçeği yapıyordu.»
   - Açıklama: Kartın yanlar alanında Kristoff buz toplayıp satan adamdır; buzdan şekil yapma yeteneği kartta yok.
   - Açıklama: Kartın yanlar bölümünde Kristoff buz toplayıp satar; buzdan heykel yapma yeteneği kartta yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kızaktaki buz"
   - Cümle 5: «Kraliçe Elsa kızaktaki buz parçalarına baktı.»
   - Açıklama: Elsa önceden tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kızaktaki buz parçalarına baktı"
   - Cümle 5: «Kraliçe Elsa kızaktaki buz parçalarına baktı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, çözümde işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kraliçe Elsa kızaktaki buz parçalarına baktı"
   - Cümle 5: «Kraliçe Elsa kızaktaki buz parçalarına baktı.»
   - Açıklama: Kızak ve içindeki buz parçaları önceden kurulmadan çözümü getirmek için beliriyor.
   - Açıklama: Kızak ve içindeki buz parçaları daha önce kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Parça tam oturdu"
   - Cümle 9: «Parça tam oturdu ve ayçiçeği tamamlandı.»
   - Açıklama: 'Tam oturmak' mecazlı bir deyim; parça oturmaz.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Parça tam oturdu ve"
   - Cümle 9: «Parça tam oturdu ve ayçiçeği tamamlandı.»
   - Açıklama: 'Tam oturdu' mecazlı kullanım, parça oturmaz.
7. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "ayçiçeğini buz sarayına mutlu mutlu götürdü"
   - Cümle 12: «Sonra Elsa ile Kristoff ayçiçeğini buz sarayına mutlu mutlu götürdü.»
   - Açıklama: Hikaye dağda başlıyor ama son cümle sahneyi buz sarayına taşıyor.
   - Açıklama: Hikaye dağda başlıyor ama buz sarayına giden bir eylemle, başka bir yere taşınarak bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0071` birebir aynı, ardından `@onarim: 57af1a5aaeda4499f8cebabb2df6307140fe96ad`, sonra gövde.

### Hikâye 4: tohum elsa-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0072
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'bilezik', fiil 'kırılmak', sıfat 'çamurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: bilezik kırıldı ve çamurlu bir çukura düştü | kardeşinden yardım istedi ve bileziği buzla onardı
@tohum: elsa-0072
Elsa, kardeşi Anna ile dağda yürüyordu. Birden Elsa'nın bileziği kırıldı ve yere düştü. Bilezik yuvarlandı ve iki kayanın arasındaki çamurlu çukura girdi. Elsa elini uzattı ama çukur onun eline çok dardı. "Anna, senin elin daha küçük, bana yardım eder misin?" diye sordu Elsa. Anna elini çukura soktu ve bileziği çıkardı. Bilezik çamurluydu ama sağlamdı. Elsa bileziği temiz karla sildi. Sonra elinden küçük bir buz çıktı ve kırık yeri birleştirdi. Elsa bileziği yeniden koluna taktı. "Teşekkürler, Anna, bana çok yardım ettin!" dedi Elsa.
```

**Hakem bulguları (6):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "bilezik kırıldı ve çamurlu bir çukura düştü"
   - Cümle 0 (plan satırı): «bilezik kırıldı ve çamurlu bir çukura düştü | kardeşinden yardım istedi ve bileziği buzla onardı»
   - Açıklama: Bileziğin kırılması ve çukura düşmesi iki ayrı sorun.
   - Açıklama: Hikayede hem bileziğin kırılması hem çukura düşmesi olmak üzere iki sorun var.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden Elsa'nın bileziği kırıldı"
   - Cümle 2: «Birden Elsa'nın bileziği kırıldı ve yere düştü.»
   - Açıklama: Bileziğin neden kırıldığı söylenmiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Anna elini çukura soktu"
   - Cümle 6: «Anna elini çukura soktu ve bileziği çıkardı.»
   - Açıklama: Kayalar arasındaki dar çukura el sokmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Kayaların arasındaki dar çukura el sokmak çocuğun taklit edebileceği riskli bir davranış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bilezik çamurluydu ama sağlamdı"
   - Cümle 7: «Bilezik çamurluydu ama sağlamdı.»
   - Açıklama: Bilezik kırık olduğu için 'sağlam' kelimesi yanlış anlamda.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bilezik çamurluydu ama sağlamdı"
   - Cümle 7: «Bilezik çamurluydu ama sağlamdı.»
   - Açıklama: Kırıldığı söylenen bilezik sağlam deniyor, sonra kırık yeri onarılıyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa bileziği temiz karla sildi"
   - Cümle 8: «Elsa bileziği temiz karla sildi.»
   - Açıklama: Çözüm yardım isteme, çıkarma, silme ve onarma olarak ikiden çok adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0072` birebir aynı, ardından `@onarim: 07f40ea7519bf1473740a89624a6426372ce6d50`, sonra gövde.

### Hikâye 5: tohum elsa-0073 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ağaçtan pır pır diye garip bir ses geldi | kar topuyla dala takılan uçurtmayı indirdi
@tohum: elsa-0073
@degisim: saat -> uçurtma
Elsa ormanda Sven ile birlikte oynuyordu. Birden yukarıdan pır pır diye garip bir ses geldi. Elsa başını kaldırdı ve sesi çok merak etti. Sven de kulaklarını dikti ve bir ağaca baktı. Yüksek bir dalda sarı bir uçurtma takılı kalmıştı. Rüzgar esince uçurtma sallanıyor ve pır pır ses çıkarıyordu. "Sesi bulduk, Sven!" dedi Elsa. Elsa elini dala doğru uzattı. Elinden küçük bir buz topu çıktı ve dala çarptı. Uçurtma yavaşça yumuşak karın üstüne düştü. Sven koştu ve uçurtmayı ağzıyla Elsa'ya verdi. Uçurtma biraz ıslaktı ama hiç kırılmamıştı. Elsa çok sevindi, çünkü garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kar topuyla dala takılan uçurtmayı indirdi"
   - Cümle 0 (plan satırı): «ağaçtan pır pır diye garip bir ses geldi | kar topuyla dala takılan uçurtmayı indirdi»
   - Açıklama: Planda kar topu deniyor ama gövdede uçurtmayı buz topu indiriyor.
   - Açıklama: Gövdede Elsa kar topu değil buz topu atıyor ve asıl sorun olan ses uçurtmayı indirmeden önce çözülüyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "pır pır diye garip bir ses geldi"
   - Cümle 2: «Birden yukarıdan pır pır diye garip bir ses geldi.»
   - Açıklama: Garip bir ses yalnız merak konusu; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sven de kulaklarını dikti ve bir ağaca baktı"
   - Cümle 4: «Sven de kulaklarını dikti ve bir ağaca baktı.»
   - Açıklama: Sesin kaynağını Elsa değil Sven buluyor gibi görünüyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sesi bulduk, Sven!"
   - Cümle 7: «"Sesi bulduk, Sven!" dedi Elsa.»
   - Açıklama: Sesin kaynağı bulunduktan sonra uçurtmayı indirmek ikinci bir sorun olarak başlıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yumuşak karın üstüne düştü"
   - Cümle 10: «Uçurtma yavaşça yumuşak karın üstüne düştü.»
   - Açıklama: Ormanda kar olduğu hiç kurulmadan kar sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0073` birebir aynı, `@degisim: saat -> uçurtma` (tutuyorsan), ardından `@onarim: 02553d5a8fb868d039fd5639a5f7e505e1abfec9`, sonra gövde.

### Hikâye 6: tohum elsa-0074 (deneme 1 -> 2)

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
@plan: güneşli yerde kar erimişti ve yer ıslaktı | ağacın altında kuru ve yeşil bir yer buldu
@tohum: elsa-0074
Bir sabah Kraliçe Elsa ormana geldi. İlk kez ormanda tek başına piknik yapmayı deniyordu. Elinde bir yastık ve küçük bir sepet vardı. Ama güneşli açıklıkta kar erimişti ve yer çok ıslaktı. Elsa yastığını ıslak yere koyamadı. Elsa etrafına baktı ve büyük bir ağaç gördü. Ağacın altında hiç kar yoktu. Yer kuruydu ve yeşil otlarla kaplıydı. Elsa yastığını yumuşak otların üstüne koydu. Sonra sepetinden ekmek ve elma çıkardı. Elsa yastığına oturdu ve ilk pikniğini mutlu mutlu yaptı.
```

**Hakem bulguları (6):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa ormana geldi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kız kardeşini koruma biçiminde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa ormana geldi"
   - Cümle 1: «Bir sabah Kraliçe Elsa ormana geldi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, hikayede işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güneşli açıklıkta kar erimişti"
   - Cümle 4: «Ama güneşli açıklıkta kar erimişti ve yer çok ıslaktı.»
   - Açıklama: 'Açıklık' 3 yaşındaki çocuğun bilmediği bir kelime.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "güneşli açıklıkta kar erimişti"
   - Cümle 4: «Ama güneşli açıklıkta kar erimişti ve yer çok ıslaktı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ağacın altında hiç kar yoktu"
   - Cümle 7: «Ağacın altında hiç kar yoktu.»
   - Açıklama: Kar güneşte erimişken gölgedeki ağacın altının karsız ve kuru olması sebepsiz, çözümü kolayca getiriyor.
6. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Yer kuruydu ve yeşil otlarla kaplıydı"
   - Cümle 8: «Yer kuruydu ve yeşil otlarla kaplıydı.»
   - Açıklama: Kartın orman tarifi karlı ağaçlarla dolu orman diyor; kuru, yeşil otlu açıklık bu tarifle çelişiyor.
   - Açıklama: Kartın orman tarifi ve kararı yalnız karlı orman kullanımına izin veriyor; kuru yeşil otlu yer bu tarife aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0074` birebir aynı, ardından `@onarim: f396426d2529fe6abe27d707353cd39f439edeca`, sonra gövde.
