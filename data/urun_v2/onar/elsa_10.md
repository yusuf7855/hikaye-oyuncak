# Editör görevi (onarım): Elsa, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0034 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0034
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kabak', fiil 'yakalamak', sıfat 'incecik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: rüzgar şapkayı uçurdu ve şapka yolda yuvarlandı | hemen koştu ve şapkayı ipinden yakaladı
@tohum: elsa-0034
@degisim: kabak -> şapka
Elsa limanda Kristoff ile yürüyordu. Kristoff iki eliyle büyük bir buz kalıbı taşıyordu. Birden güçlü bir rüzgar Kristoff'un şapkasını başından uçurdu. Şapka limanın taş yolunda yuvarlandı. "Şapkam gidiyor ama ellerim dolu!" dedi Kristoff. Elsa bir kraliçeydi ve arkadaşını üzgün görmek istemedi. Hemen koştu ve şapkayı incecik ipinden yakaladı. Sonra şapkayı Kristoff'un başına taktı ve ipini sıkıca bağladı. Artık şapka rüzgarda hiç uçmadı. "Teşekkürler, Elsa, çok hızlıydın!" dedi Kristoff. Elsa güldü. İkisi limanda yürümeye mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve arkadaşını üzgün görmek istemedi"
   - Cümle 6: «Elsa bir kraliçeydi ve arkadaşını üzgün görmek istemedi.»
   - Açıklama: Kraliçe özelliği karttaki gibi kız kardeşi korumak için değil süs olarak geçiyor; çözüm (koşup yakalamak) ona dayanmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve arkadaşını üzgün"
   - Cümle 6: «Elsa bir kraliçeydi ve arkadaşını üzgün görmek istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız anılıyor, sorunu çözmekte işe yaramıyor; çözüm sadece koşmak.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve arkadaşını üzgün görmek istemedi"
   - Cümle 6: «Elsa bir kraliçeydi ve arkadaşını üzgün görmek istemedi.»
   - Açıklama: Kraliçe olmak şapkayı yakalamakla ilgisiz, işlevsiz ve sebep gibi sunulan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0034` birebir aynı, `@degisim: kabak -> şapka` (tutuyorsan), ardından `@onarim: e0959cf9d3b7584958d6bb9600e949ad2850be85`, sonra gövde.

### Hikâye 2: tohum elsa-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0035
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'tomurcuk', fiil 'esnemek', sıfat 'yemyeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: top çok yükseğe gitti ve bir dala takıldı | buzdan uzun bir çubuk yapıp topu düşürdü
@tohum: elsa-0035
@degisim: tomurcuk -> top
Soğuk bir rüzgar esiyordu. Elsa dağda sarayının önüne çıktı ve uzun uzun esnedi. Sonra topunu havaya atıp tutmaya başladı. Ama top çok yükseğe gitti ve yemyeşil bir ağacın dalına takıldı. Elsa uzandı ama topa ulaşamadı. Elinden buz çıkardı ve uzun bir çubuk yaptı. Çubukla topa yavaşça dokundu. Top dalın üstünden kaydı ve yumuşak kara düştü. Elsa topu kardan aldı ve bu kez daha yavaş attı. Top yine tam eline geldi. Elsa çok sevindi, çünkü topunu kurtarmış ve oyununa dönmüştü.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "uzun uzun esnedi"
   - Cümle 2: «Elsa dağda sarayının önüne çıktı ve uzun uzun esnedi.»
   - Açıklama: Esneme olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Elsa'nın esnemesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Sonra topunu havaya atıp tutmaya başladı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak 4. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0035` birebir aynı, `@degisim: tomurcuk -> top` (tutuyorsan), ardından `@onarim: bbd76bc7e3e79e2235e2e3b8a033cf7d01a23a72`, sonra gövde.

### Hikâye 3: tohum elsa-0036 (deneme 1 -> 2)

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
@plan: kızak kabarık bir kar yığınına girip takıldı | kızağı arkadan itip karı sert bir yola çevirdi
@tohum: elsa-0036
@degisim: kapı -> kızak
Karlı ormanda Elsa ile Sven kızak oyunu oynuyordu. Sven önde koşuyor, Elsa da arkada neşeyle şarkı söylüyordu. Ama kızak kabarık bir kar yığınına girdi ve durdu. Sven bütün gücüyle çekti ama kızak hiç kıpırdamadı. Sven'in burnu karla bembeyaz oldu. Elsa bu komik burna bakıp güldü ve yere indi. "Sven, yolu değiştirelim," dedi Elsa. Kraliçe Elsa kızağı arkadan itti ve karı sert bir yola çevirdi. Sven başını salladı ve kızağı bu kez kolayca çekti. Elsa yeniden yerine oturdu. Elsa ile Sven ağaçların arasında mutlu mutlu oyunlarına devam etti.
```

**Hakem bulguları (7):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sven'in burnu karla bembeyaz oldu"
   - Cümle 5: «Sven'in burnu karla bembeyaz oldu.»
   - Açıklama: Sven'in karlı burnu ve Elsa'nın gülmesi olay zincirinde hiçbir işe yaramayan ayrıntı.
2. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "bu komik burna bakıp güldü"
   - Cümle 6: «Elsa bu komik burna bakıp güldü ve yere indi.»
   - Açıklama: Elsa arkadaşının karla kaplanan burnuna gülüyor; örnek alınabilecek hafif bir alay var.
3. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Elsa bu komik burna bakıp güldü"
   - Cümle 6: «Elsa bu komik burna bakıp güldü ve yere indi.»
   - Açıklama: Elsa arkadaşının karlı burnuna gülüyor; çocuk için alay örneği olarak okunabilir.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karı sert bir yola çevirdi"
   - Cümle 8: «Kraliçe Elsa kızağı arkadan itti ve karı sert bir yola çevirdi.»
   - Açıklama: Kızağı itmek karı yola çevirmez; fiil anlamca uymuyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kızağı arkadan"
   - Cümle 8: «Kraliçe Elsa kızağı arkadan itti ve karı sert bir yola çevirdi.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Önceden tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' olarak yeniden tanıtılıyor.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kızağı arkadan itti"
   - Cümle 8: «Kraliçe Elsa kızağı arkadan itti ve karı sert bir yola çevirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, çözüme bir katkısı yok.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; kartın özellik satırındaki gibi işe yarar biçimde kullanılmıyor.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "kızağı arkadan itti ve karı sert bir yola çevirdi"
   - Cümle 8: «Kraliçe Elsa kızağı arkadan itti ve karı sert bir yola çevirdi.»
   - Açıklama: Kızağı arkadan itmenin kabarık karı nasıl sert bir yola çevirdiği anlaşılmıyor; çözüm sebebe akla yatkın biçimde yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0036` birebir aynı, `@degisim: kapı -> kızak` (tutuyorsan), ardından `@onarim: 03aaba32a35a1c9a8094013f7ef356cbf4d92954`, sonra gövde.

### Hikâye 4: tohum elsa-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0042
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kaymak', fiil 'gülüşmek', sıfat 'benekli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kızakla kayan kardeş yumuşak bir kar yığınına gömüldü | kardeşinin elinden tuttu ve onu kardan çekti
@tohum: elsa-0042
Bir sabah Elsa ile Anna dağda, küçük bir tepenin başındaydı. İkisi de kızakla aşağı kaymak istiyordu. Anna önce kaydı ama yumuşak bir kar yığınına gömüldü. Kardan yalnız onun benekli şapkası görünüyordu. "Elsa, çıkamıyorum!" dedi Anna neşeyle. Kraliçe Elsa kız kardeşini hep korurdu ve hemen yanına koştu. Kardeşinin elinden tuttu ve onu yavaşça dışarı çekti. Anna'nın yüzü kardan bembeyaz olmuştu. İki kardeş birbirine baktı ve gülüştü. "Teşekkürler, Elsa, şimdi bir kez daha kayalım!" dedi Anna.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yumuşak bir kar yığınına gömüldü"
   - Cümle 3: «Anna önce kaydı ama yumuşak bir kar yığınına gömüldü.»
   - Açıklama: Çocuğun kar yığınına tamamen gömülmesi taklit edilince tehlikeli bir durum olarak olağan gösteriliyor.
   - Açıklama: Kar yığınına gömülmek taklit edilince boğulma tehlikesi taşıyan bir durum.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedi Anna neşeyle"
   - Cümle 5: «"Elsa, çıkamıyorum!" dedi Anna neşeyle.»
   - Açıklama: Karda gömülüp çıkamayan Anna'nın 'neşeyle' konuşması duruma uygun değil.
   - Açıklama: Kardan çıkamayan Anna'nın yardım isterken 'neşeyle' konuşması kelimeyi duruma uygunsuz kılıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "dedi Anna neşeyle"
   - Cümle 5: «"Elsa, çıkamıyorum!" dedi Anna neşeyle.»
   - Açıklama: Anna kara gömülüp çıkamadığını söylerken neşeli olması sorunla çelişiyor.
   - Açıklama: Anna kardan çıkamadığını söylerken neşeli görünüyor; bu, sorunun ciddiyetiyle çelişiyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kız kardeşini hep korurdu"
   - Cümle 6: «Kraliçe Elsa kız kardeşini hep korurdu ve hemen yanına koştu.»
   - Açıklama: Zaten tanıtılmış Elsa 'Kraliçe Elsa' olarak yeniden tanıtılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0042` birebir aynı, ardından `@onarim: f1790e2b78ab41e16569bff8330c764755143917`, sonra gövde.

### Hikâye 5: tohum elsa-0044 (deneme 1 -> 2)

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
@plan: arkadaşı da kaymak istedi ama kızağı yoktu | kızağı paylaşıp onu arkasına oturttu
@tohum: elsa-0044
@degisim: kayık -> kızak
Ormanda hafif bir rüzgar esiyordu. Elsa küçük, açık bir yokuştan kızakla kayıyordu. Olaf da kaymak istedi ama onun kızağı yoktu. Olaf sabırsızdı ve yokuşun altında zıplayarak bekliyordu. Kızak aşağıda, Olaf'ın hemen önünde durdu. "Gel, Olaf, bu kızak ikimize de yeter," dedi Elsa. İkisi kızağı yokuşun başına çekti. Kraliçe Elsa öne oturdu ve Olaf onun arkasına yerleşti. Kızak yavaşça aşağı indi. Olaf kollarını açtı ve kahkahalarla güldü. "Birlikte çok daha eğlenceli!" dedi Olaf. Elsa ile Olaf mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yokuşun altında zıplayarak bekliyordu"
   - Cümle 4: «Olaf sabırsızdı ve yokuşun altında zıplayarak bekliyordu.»
   - Açıklama: Yokuşun 'altı' yanlış; 'yokuşun dibinde' olmalı.
   - Açıklama: 'Altında' yanlış; 'yokuşun dibinde' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa öne oturdu"
   - Cümle 8: «Kraliçe Elsa öne oturdu ve Olaf onun arkasına yerleşti.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa öne oturdu"
   - Cümle 8: «Kraliçe Elsa öne oturdu ve Olaf onun arkasına yerleşti.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0044` birebir aynı, `@degisim: kayık -> kızak` (tutuyorsan), ardından `@onarim: e0f756cbac765e1b5814a5dab7ac853d48246da7`, sonra gövde.

### Hikâye 6: tohum elsa-0045 (deneme 1 -> 2)

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
@plan: yumuşak kardan yapılan kule yana devrildi | karı sıkıca bastırıp kuleyi sağlam yaptı
@tohum: elsa-0045
Karlı dağda, buzdan sarayın yanında güneş parlıyordu. Elsa karla uzun kuleli, küçük bir kale yapıyordu. Ama kulenin karı çok yumuşaktı ve kule birden yana devrildi. Elsa biraz mutsuz oldu. Sonra karı iki eliyle sıkıca bastırdı ve kuleyi daha sağlam yaptı. Elsa'nın cebinde bir avuç ayçiçeği çekirdeği vardı. Kraliçe Elsa çekirdekleri tek tek kalenin duvarlarına ekledi. Kale şimdi benekli bir kurabiyeye benziyordu. Elsa buna bakıp güldü. Rüzgar esti ama kule bu kez dik durdu. Elsa kalesinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa'nın cebinde bir avuç ayçiçeği çekirdeği vardı"
   - Cümle 6: «Elsa'nın cebinde bir avuç ayçiçeği çekirdeği vardı.»
   - Açıklama: Çekirdekler sebepsiz beliriyor ve sorunun çözümüne hiçbir katkı yapmıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa çekirdekleri tek"
   - Cümle 7: «Kraliçe Elsa çekirdekleri tek tek kalenin duvarlarına ekledi.»
   - Açıklama: Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Elsa bu cümlede birden unvanla yeniden adlandırılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa çekirdekleri tek tek"
   - Cümle 7: «Kraliçe Elsa çekirdekleri tek tek kalenin duvarlarına ekledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve kartın 'kız kardeşini korur' özelliğine uygun işe yarar biçimde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa çekirdekleri tek tek kalenin duvarlarına ekledi"
   - Cümle 7: «Kraliçe Elsa çekirdekleri tek tek kalenin duvarlarına ekledi.»
   - Açıklama: Tohum özelliği kraliçelik ve kız kardeşi korumak; özellik sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0045` birebir aynı, ardından `@onarim: 6ee9d78742676a0f3d6e267098c3b4201fdd2799`, sonra gövde.
