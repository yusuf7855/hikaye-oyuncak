# Editör görevi (onarım): Elsa, onarım partisi 3

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar3.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar3.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0001 (deneme 3 -> 4)

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
@plan: rüzgar esti ve ağacın dalından ekmeğe kar döküldü | kardeşini açık kapıdan saraya aldı ve ekmeğini paylaştı
@tohum: elsa-0001
@degisim: çöp -> dal
Elsa ile Anna dağda, sarayın önündeki bir ağacın altında oturuyordu. Kar yavaş yavaş yağıyordu ve Anna ekmeğine şeker ekti. Birden rüzgar esti ve ağacın dalından ekmeğin üstüne kar döküldü. "Elsa, ekmek karla ıslandı!" dedi Anna. Ağacın dalları yine sallanıyordu. Kraliçe Elsa kardeşini korumak için hemen elinden tuttu. "Gel, Anna, içeride oturalım," dedi Elsa. İki kardeş sarayın açık kapısından içeri koştu. Elsa kendi ekmeğini ikiye böldü ve yarısını Anna'ya verdi. İkisi yan yana oturdu ve dışarıda yağan karı izledi. "Teşekkürler, Elsa, bu en güzel kar günü oldu!" dedi Anna.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Anna ekmeğine şeker ekti"
   - Cümle 2: «Kar yavaş yavaş yağıyordu ve Anna ekmeğine şeker ekti.»
   - Açıklama: Şeker ekme ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kar yavaş yavaş yağıyordu"
   - Cümle 2: «Kar yavaş yavaş yağıyordu ve Anna ekmeğine şeker ekti.»
   - Açıklama: Kar zaten ekmeğin üstüne yağarken daldan dökülen karın ekmeği ıslatması ayrı bir sorun gibi sunuluyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini korumak"
   - Cümle 6: «Kraliçe Elsa kardeşini korumak için hemen elinden tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Önceden tanıtılan Elsa unvanla ikinci kez tanıtılıyor.
   - Açıklama: Baştan tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "İki kardeş sarayın açık kapısından içeri koştu"
   - Cümle 8: «İki kardeş sarayın açık kapısından içeri koştu.»
   - Açıklama: Hikaye dağda ağacın altında başlıyor ama sarayın içinde bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0001` birebir aynı, `@degisim: çöp -> dal` (tutuyorsan), ardından `@onarim: fb8fd000ab4e0d068dae144408c908035888ee44`, sonra gövde.

### Hikâye 2: tohum elsa-0003 (deneme 3 -> 4)

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
Bir sabah Elsa ile Olaf kıyıda sıcak bir yaz günüymüş gibi oynuyordu. Olaf büyük bir şemsiyeyi karın içine dikti. Ama rüzgar esti ve şemsiye yere düştü. Olaf onu tekrar dikti, ama şemsiye yine devrildi. "Elsa, bu şemsiye hiç durmuyor!" dedi Olaf. Elsa eğildi ve şemsiyenin dibine buzdan sağlam bir ayak yaptı. Rüzgar bir kez daha esti, ama şemsiye bu kez kıpırdamadı. İkisi şemsiyenin altına oturdu. Olaf kardan iki küçük kek hazırladı ve birini Elsa'ya verdi. İkisi de kekleri yiyormuş gibi yaptı. "Bu kek çok lezzetli!" dedi Olaf ve güldü. Elsa çok sevindi, çünkü şemsiyeleri artık rüzgarda hiç düşmüyordu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şemsiyeyi karın içine dikti"
   - Cümle 2: «Olaf büyük bir şemsiyeyi karın içine dikti.»
   - Açıklama: Sıcak yaz oyunu oynanan deniz kıyısında kar sebepsiz beliriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Olaf kardan iki küçük kek hazırladı"
   - Cümle 9: «Olaf kardan iki küçük kek hazırladı ve birini Elsa'ya verdi.»
   - Açıklama: Kek oyunu sorundan ve çözümden çıkmayan, işlevsiz bir ek sahne.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0003` birebir aynı, ardından `@onarim: d30d05c20719c9f11ff6170cfec2f54f2c44d01e`, sonra gövde.

### Hikâye 3: tohum elsa-0006 (deneme 3 -> 4)

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
@plan: dağda garip bir ses duyuldu | sesin aç geyikten geldiğini buldu ve onu doyurdu
@tohum: elsa-0006
Bir sabah Elsa ile Sven dağda yürüyordu. Elsa'nın kolunda poğaça dolu bir sepet vardı. Birden yakından garip bir ses duyuldu. "Bu ses nereden geliyor, Sven?" diye sordu Elsa. Sven hemen sepete baktı. Ses yine geldi ve bu kez çok yakındı. Elsa kulağını Sven'in karnına yaklaştırdı. "Sven, bu ses senin karnından geliyor!" dedi Elsa ve güldü. Sven çok acıkmıştı, ama başı derin sepete girmiyordu. Yerde de soğuk kar toplanmıştı. Elsa buzdan geniş bir tabak yaptı ve poğaçaları üstüne koydu. Sven iki poğaçayı hemen yedi. Sonra Elsa ile Sven yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (8):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve bu kez çok yakındı"
   - Cümle 6: «Ses yine geldi ve bu kez çok yakındı.»
   - Açıklama: 'bu kez' ilk sesin uzak olduğunu ima ediyor ama 3. cümlede ses zaten 'yakından' duyulmuştu.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "ama başı derin sepete girmiyordu"
   - Cümle 9: «Sven çok acıkmıştı, ama başı derin sepete girmiyordu.»
   - Açıklama: Garip ses sorunu çözüldükten sonra başın sepete girmemesi diye ikinci bir sorun ekleniyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "başı derin sepete girmiyordu"
   - Cümle 9: «Sven çok acıkmıştı, ama başı derin sepete girmiyordu.»
   - Açıklama: Garip ses sorunu çözüldükten sonra başın sepete girmemesi diye ikinci bir sorun ekleniyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yerde de soğuk kar toplanmıştı"
   - Cümle 10: «Yerde de soğuk kar toplanmıştı.»
   - Açıklama: 'de' bağlacının eklediği bir öge yok ve cümle öncekilere bağlanmıyor; anlamı belirsiz.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "soğuk kar toplanmıştı"
   - Cümle 10: «Yerde de soğuk kar toplanmıştı.»
   - Açıklama: Kar için 'toplanmak' doğal değil; 'birikmişti' olmalı.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "de soğuk kar toplanmıştı"
   - Cümle 10: «Yerde de soğuk kar toplanmıştı.»
   - Açıklama: Kar zaten soğuktur; 'soğuk' gereksiz tekrar.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yerde de soğuk kar toplanmıştı"
   - Cümle 10: «Yerde de soğuk kar toplanmıştı.»
   - Açıklama: Yerdeki kar işe yarayacakmış gibi kuruluyor ama hiç kullanılmıyor.
   - Açıklama: Yerdeki kar işe yarayacakmış gibi kuruluyor ama tabak Elsa'nın buzundan yapılıyor ve kar hiç kullanılmıyor.
8. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa buzdan geniş bir tabak yaptı"
   - Cümle 11: «Elsa buzdan geniş bir tabak yaptı ve poğaçaları üstüne koydu.»
   - Açıklama: Sven'i doyurmak için poğaçayı doğrudan vermek yerine dolambaçlı bir buz tabak çözümü kuruluyor.
   - Açıklama: Sven acıktığı için poğaçaları eliyle vermek yeterliyken buzdan tabak yapmak sebebe doğrudan yönelmeyen dolambaçlı bir çözüm.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0006` birebir aynı, ardından `@onarim: 603b62135e34613289f17b54a928ee94ce0259b1`, sonra gövde.

### Hikâye 4: tohum elsa-0007 (deneme 3 -> 4)

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
@plan: sert bir rüzgar mavi bağcığı uçurdu | rüzgarın estiği yöne yürüdü ve bağcığı çitte buldu
@tohum: elsa-0007
@degisim: saygılı -> uzun
Bir sabah Kraliçe Elsa limanın kıyısında yürüyordu. Mavi bir bağcık uzun pelerinini boynunda tutuyordu. Birden denizden sert bir rüzgar esti ve bağcığı uçurdu. Pelerin yere doğru kaymaya başladı. Elsa pelerinini iki eliyle tuttu ve düşündü. Rüzgar denizden karaya doğru esiyordu. Elsa da rüzgarın estiği yöne doğru yürüdü. Yolun kenarındaki çitte mavi bir şey sallanıyordu. Elsa bağcığı aldı ve pelerinini yeniden sıkıca bağladı. Sonra saçlarını da parmaklarıyla taradı. Elsa çok sevindi, çünkü kaybolan bağcığı kendi başına bulmuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa limanın"
   - Cümle 1: «Bir sabah Kraliçe Elsa limanın kıyısında yürüyordu.»
   - Açıklama: Tohumdaki özellik (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa limanın kıyısında yürüyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor ve kartın 'Kraliçedir; kız kardeşini korur.' özelliği kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra saçlarını da parmaklarıyla taradı"
   - Cümle 10: «Sonra saçlarını da parmaklarıyla taradı.»
   - Açıklama: Saç tarama olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Saç tarama olaydan çıkmıyor ve sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0007` birebir aynı, `@degisim: saygılı -> uzun` (tutuyorsan), ardından `@onarim: 0433dc8c01838bf4ab6f4566036a85bdbdeaa2cb`, sonra gövde.

### Hikâye 5: tohum elsa-0010 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kaygan kıyıda geyiğin havuçları denize düştü | havuçlarını paylaştı ve buzdan bir kaseye koydu
@tohum: elsa-0010
@degisim: beşik -> kayık
Limanda kayıklar yavaş yavaş sallanıyordu. Elsa ile Sven hafif karın altında kıyıda oturuyordu. Birden Sven'in havuç kovası kaygan kıyıda kaydı ve havuçlar denize düştü. Sven üzgün üzgün suya baktı, çünkü çok acıkmıştı. Elsa'nın sepetinde yalnız üç havuç vardı. "Gel, Sven, havuçlarımı seninle paylaşayım," dedi Elsa. Havuçlar yine düşmesin diye buzdan derin bir kase yaptı. İki havucu kaseye koydu ve Sven'in önüne itti. Sven havuçları hemen yedi. Buzdan kase çok faydalı oldu, çünkü hiçbir havuç kaymadı. Sonra Sven sevinçle sırtındaki karı silkti. Elsa da kendi havucunu yedi. Elsa ile Sven kıyıda yan yana mutlu mutlu karı izledi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Buzdan kase çok faydalı oldu"
   - Cümle 10: «Buzdan kase çok faydalı oldu, çünkü hiçbir havuç kaymadı.»
   - Açıklama: 'Faydalı' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.
   - Açıklama: 'Faydalı' soyut bir kelime, 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0010` birebir aynı, `@degisim: beşik -> kayık` (tutuyorsan), ardından `@onarim: 8a168763af8b90b15e1fd1585487f65d431fd165`, sonra gövde.
