# Editör görevi (onarım): Elsa, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0120
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'askı', fiil 'şekillendirmek', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kızak kardeşinin kardan kalesine çarptı ve kale dağıldı | özür diledi ve kardeşiyle uzak bir yerde kale yaptı
@tohum: elsa-0120
@degisim: askı -> kızak
Elsa karlı dağda küçük bir tepeden kızakla kayıyordu. Anna ise tepenin altında kardan küçük bir kale şekillendirdi. Elsa önüne bakmadı ve kızak kaleye çarpıp onu dağıttı. "Kale yıkıldı!" dedi Anna üzgün bir sesle. Elsa hemen kızaktan indi ve kardeşinin yanına koştu. "Özür dilerim, Anna, dikkat etmedim," dedi Elsa. Kraliçe Elsa kardeşinin elini tuttu. Onu kızak yolundan uzak, düz bir yere götürdü. Yardımsever Elsa orada yeni kaleyi kardeşiyle birlikte yaptı. "Burada kale güvende, teşekkürler, Elsa!" dedi Anna. Sonra Elsa ile Anna el ele kızağa bindi ve mutlu mutlu kaydı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kardan küçük bir kale şekillendirdi"
   - Cümle 2: «Anna ise tepenin altında kardan küçük bir kale şekillendirdi.»
   - Açıklama: 'Şekillendirmek' 3 yaşındaki çocuğun bilmeyeceği bir kelime; 'yaptı' olmalı.
   - Açıklama: 'Şekillendirdi' 3 yaşındaki bir çocuk için zor bir kelime; 'yapıyordu' yeterli.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşinin elini"
   - Cümle 7: «Kraliçe Elsa kardeşinin elini tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yardımsever Elsa orada yeni"
   - Cümle 9: «Yardımsever Elsa orada yeni kaleyi kardeşiyle birlikte yaptı.»
   - Açıklama: Elsa bir kez daha sıfatla yeniden tanıtılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yardımsever Elsa orada yeni"
   - Cümle 9: «Yardımsever Elsa orada yeni kaleyi kardeşiyle birlikte yaptı.»
   - Açıklama: Tohumdaki kraliçe özelliğine ek olarak kartta olmayan yardımseverlik ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik kraliçe; yardımseverlik karta ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0120` birebir aynı, `@degisim: askı -> kızak` (tutuyorsan), ardından `@onarim: de4d04d1f30a3cd7e8a991769e7fd8889ee1be35`, sonra gövde.

### Hikâye 2: tohum elsa-0121 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0121
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'önlük', fiil 'aydınlatmak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: salon karanlıktı ve boyaların renkleri karışık görünüyordu | perdeleri açtı ve tacın ışıklarına bakıp boyaları seçti
@tohum: elsa-0121
Elsa önlüğünü giymiş, sarayın büyük salonunda resim yapıyordu. Resmine parlak renkler koymak istiyordu. Ama salon karanlıktı ve boyaların renkleri karışık görünüyordu. Elsa pencereye gitti ve kalın perdeleri açtı. Güneş içeri girdi ve salonu aydınlattı. Işık, kraliçe Elsa'nın tacına değdi. Tacın taşları parladı ve duvara renk renk ışıklar düştü. Elsa duvardaki kırmızı, sarı ve mavi ışıklara tek tek baktı. Sonra aynı renkteki boyaları buldu ve resmine sürdü. Resmi, duvardaki ışıklar gibi rengarenk oldu. Elsa resmini uzaktan izledi ve gülümsedi. Elsa çok sevindi, çünkü resmini tam istediği gibi yapmıştı.
```

**Hakem bulguları (8):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Işık, kraliçe Elsa'nın tacına"
   - Cümle 6: «Işık, kraliçe Elsa'nın tacına değdi.»
   - Açıklama: Addan önceki unvan büyük harfle yazılmalı ve özneden sonraki virgül gereksiz.
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kraliçe Elsa'nın tacına değdi"
   - Cümle 6: «Işık, kraliçe Elsa'nın tacına değdi.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
   - Açıklama: Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe Elsa'nın tacına değdi"
   - Cümle 6: «Işık, kraliçe Elsa'nın tacına değdi.»
   - Açıklama: Kraliçe özelliği karttaki gibi (kız kardeşini koruma) değil, kartta olmayan bir taç eşyası üzerinden kullanılıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Işık, kraliçe Elsa'nın tacına değdi"
   - Cümle 6: «Işık, kraliçe Elsa'nın tacına değdi.»
   - Açıklama: Perdeler açılınca sorun çözülmüşken çözüm taç ışıklarıyla gereksiz adımlara uzuyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Işık, kraliçe Elsa'nın tacına değdi"
   - Cümle 6: «Işık, kraliçe Elsa'nın tacına değdi.»
   - Açıklama: Salon aydınlanınca sorun çözülmüşken tacın ışıkları çözüme sebepsiz bir dolambaç ekliyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tacın taşları parladı ve duvara renk renk ışıklar düştü"
   - Cümle 7: «Tacın taşları parladı ve duvara renk renk ışıklar düştü.»
   - Açıklama: Taç ışıkları boyaları seçmek için gerekmiyor; işlevsiz ve sebepsiz bir ayrıntı.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa duvardaki kırmızı, sarı ve mavi ışıklara tek tek baktı"
   - Cümle 8: «Elsa duvardaki kırmızı, sarı ve mavi ışıklara tek tek baktı.»
   - Açıklama: Karanlık giderilince boyalar doğrudan görülebilirken çözüm duvardaki ışıklara bakmaya sapıyor ve iki adımı aşıyor.
8. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Resmi, duvardaki ışıklar"
   - Cümle 10: «Resmi, duvardaki ışıklar gibi rengarenk oldu.»
   - Açıklama: Özneden sonra gereksiz virgül kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0121` birebir aynı, ardından `@onarim: b9b361cfd12ae7dbd7634c0bbdc3dbffd994b73b`, sonra gövde.

### Hikâye 3: tohum elsa-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0122
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'koza', fiil 'biriktirmek', sıfat 'pahalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: salonda bilinmeyen bir tıkırtı vardı | tahtına oturup salona baktı ve sesi yapan kozayı buldu
@tohum: elsa-0122
@degisim: pahalı -> kuru
Büyük salonda ince bir tık tık sesi duyuluyordu. Elsa sesin nereden geldiğini çok merak etti. Önce perdeye, sonra halıya baktı, ama hiçbir şey bulamadı. Kraliçe Elsa bu kez tahtına oturdu, çünkü oradan bütün salon görünüyordu. Ses, pencerenin yanındaki küçük kutudan geliyordu. Elsa o kutuda kuru yapraklar biriktiriyordu. Elsa kutunun yanına gitti ve içine eğilip baktı. Yaprakların arasında boş, kahverengi bir koza vardı. Açık pencereden gelen rüzgar kozayı sallıyordu. Koza kutuya vurunca tık tık ses çıkıyordu. Elsa pencereyi kapattı ve ses hemen durdu. Sonra kozayı yaprakların üstüne koydu ve mutlu mutlu gülümsedi.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "tahtına oturup salona baktı ve sesi yapan kozayı buldu"
   - Cümle 0 (plan satırı): «salonda bilinmeyen bir tıkırtı vardı | tahtına oturup salona baktı ve sesi yapan kozayı buldu»
   - Açıklama: Gövdede sorun pencereyi kapatarak çözülüyor; plan bunu söylemiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa bu kez tahtına"
   - Cümle 4: «Kraliçe Elsa bu kez tahtına oturdu, çünkü oradan bütün salon görünüyordu.»
   - Açıklama: Elsa zaten tanıtılmışken ortada 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa bu kez"
   - Cümle 4: «Kraliçe Elsa bu kez tahtına oturdu, çünkü oradan bütün salon görünüyordu.»
   - Açıklama: Zaten tanınan Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kraliçe Elsa bu kez tahtına oturdu"
   - Cümle 4: «Kraliçe Elsa bu kez tahtına oturdu, çünkü oradan bütün salon görünüyordu.»
   - Açıklama: Bir sesin kaynağı tahta oturup bakarak bulunmaz; çözüm sebebe doğrudan yönelmiyor ve tahttan kutuya, pencereye uzanan adımlar ikiyi aşıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bu kez tahtına oturdu, çünkü oradan bütün salon görünüyordu"
   - Cümle 4: «Kraliçe Elsa bu kez tahtına oturdu, çünkü oradan bütün salon görünüyordu.»
   - Açıklama: Tahttan salonu görmek sesin kaynağını bulmayı açıklamıyor; çözüm sebepsizce geliyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "boş, kahverengi bir koza"
   - Cümle 8: «Yaprakların arasında boş, kahverengi bir koza vardı.»
   - Açıklama: 'Koza' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0122` birebir aynı, `@degisim: pahalı -> kuru` (tutuyorsan), ardından `@onarim: 6dd260c60cf0419d25d9375f85c4ddc8be9229db`, sonra gövde.

### Hikâye 4: tohum elsa-0123 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0123
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yağmur ya da kar günü
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'reçel', fiil 'serinlemek', sıfat 'sadık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: reçelli ekmeklerin üstüne kar düştü | kardeşini dalları sık bir ağacın altına çağırdı
@tohum: elsa-0123
@degisim: sadık -> kuru
Ormanda sessizce kar yağıyordu. Elsa ile Anna kartopu oynadıktan sonra bir kütüğe oturup serinledi. Anna çantasından reçelli iki ekmek çıkardı, ama ekmeklerin üstüne hemen kar düştü. "Ekmekler ıslanıyor, Elsa!" dedi Anna. Elsa etrafa baktı ve yakında dalları sık, büyük bir ağaç gördü. "Anna, ekmekleri al ve benimle o ağacın altına gel," dedi kraliçe Elsa. Anna onları tuttu ve Elsa'nın peşinden koştu. Ağacın kalın dalları karı tutuyordu ve altı kuruydu. Elsa ile Anna dalların altında yan yana oturdu. Çilek reçeli çok tatlıydı ve bu kez üstüne hiç kar düşmedi. "Teşekkürler, Elsa, burası kar günü için en güzel yer!" dedi Anna.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir kütüğe oturup serinledi"
   - Cümle 2: «Elsa ile Anna kartopu oynadıktan sonra bir kütüğe oturup serinledi.»
   - Açıklama: Kar yağarken ormanda 'serinledi' fiili duruma uygun değil.
   - Açıklama: Kar yağarken 'serinledi' anlamca uymuyor; 'dinlendi' olmalı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Anna, ekmekleri al ve benimle o ağacın altına gel," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0123` birebir aynı, `@degisim: sadık -> kuru` (tutuyorsan), ardından `@onarim: ed56163054b8b8a435d1aa8fb4612a52521dde78`, sonra gövde.

### Hikâye 5: tohum elsa-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0124
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gardırop', fiil 'serinletmek', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: kızağın ipi bir çalıya takıldı ve karıştı | ipi dalların arasından tek tek çözdü
@tohum: elsa-0124
@degisim: gardırop -> ip
Rüzgar ağaçların arasında hafifçe esiyordu. Elsa ormanda küçük bir tepeden kızakla kayıyor, her seferinde gülerek kara yuvarlanıyordu. Ama kızağın ipi bir çalıya takıldı ve karmakarışık oldu. Elsa kızağı çekti, ama kızak yerinden oynamadı. Kraliçe Elsa çekmeyi bıraktı ve çalının yanına eğildi. İpi dalların arasından tek tek çözdü. Sonunda ip düzeldi ve kızak çalıdan kurtuldu. Elsa kızağını tepeye çekti ve bir kez daha kaydı. Rüzgar Elsa'nın sıcak yüzünü güzelce serinletti. Bu kez ip hiçbir yere takılmadı. Elsa tepenin altında yüksek sesle güldü. Sonra kızakla kaymaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa çekmeyi bıraktı"
   - Cümle 5: «Kraliçe Elsa çekmeyi bıraktı ve çalının yanına eğildi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği işe yarar biçimde kullanılmıyor; yalnız unvan olarak geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar Elsa'nın sıcak yüzünü güzelce serinletti"
   - Cümle 9: «Rüzgar Elsa'nın sıcak yüzünü güzelce serinletti.»
   - Açıklama: Rüzgarın yüzü serinletmesi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa tepenin altında yüksek"
   - Cümle 11: «Elsa tepenin altında yüksek sesle güldü.»
   - Açıklama: Tepenin 'altında' yanlış anlamda; 'tepenin eteğinde/aşağısında' olmalı.
   - Açıklama: 'Tepenin altında' tepenin içi/altı anlamına gelir; 'tepenin eteğinde' ya da 'aşağıda' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0124` birebir aynı, `@degisim: gardırop -> ip` (tutuyorsan), ardından `@onarim: e091d76099d40a702d730bdca5ecadb27b839b6d`, sonra gövde.

### Hikâye 6: tohum elsa-0125 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Olaf
@tohum: elsa-0125
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'masa', fiil 'yapışmak', sıfat 'taze'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | Olaf
@plan: kardan adamın eli bal kasesine yapıştı | ona elini yavaşça çevirmesini söyledi ve elini sildi
@tohum: elsa-0125
Bir sabah Elsa sarayda kahvaltı yapıyordu, Olaf da masada oturuyordu. Olaf, Elsa'nın taze ekmeğine bal sürmek istedi. Ama ince eli bal kasesinin kenarına yapıştı. "Elsa, elim kaseye yapıştı!" dedi Olaf. Olaf elini hızlı hızlı salladı ve kase de onunla sallandı. "Olaf, dur ve elini yavaşça çevir," dedi kraliçe Elsa. Olaf onun sözünü dinledi ve elini yavaşça çevirdi. Eli kolayca kurtuldu. Elsa bir bezle Olaf'ın elindeki balı sildi. Sonra kendi ekmeğine biraz bal sürdü. Olaf, Elsa'ya sıkıca sarıldı. Olaf çok sevindi, çünkü Elsa ona yardım etmişti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yavaşça çevirmesini söyledi ve elini sildi"
   - Cümle 0 (plan satırı): «kardan adamın eli bal kasesine yapıştı | ona elini yavaşça çevirmesini söyledi ve elini sildi»
   - Açıklama: Plandaki ikinci 'elini' kimin elini gösterdiği belli değil; Elsa kendi elini siliyor gibi okunuyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Olaf, dur ve elini yavaşça çevir," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Ada bağlı unvan büyük harfle yazılır: 'Kraliçe Elsa'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Olaf, dur ve elini yavaşça çevir," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği işe yarar biçimde kullanılmıyor; yalnız unvan olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0125` birebir aynı, ardından `@onarim: b0c04ccae1802c53ff257a732f0b71a20fad0fd6`, sonra gövde.

### Hikâye 7: tohum elsa-0126 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0126
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kırıntı', fiil 'yeşillenmek', sıfat 'düzgün'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: sürpriz hazırlamak istedi ama geyik hep yanındaydı | geyiğe kayanın arkasında beklemesini söyledi ve elmaları dizdi
@tohum: elsa-0126
@degisim: yeşillenmek -> dizmek
Bir sabah Elsa karlı dağda Sven ile yürüyordu. Çantasında Sven için beş kırmızı elma vardı. Elsa ona bir sürpriz yapmak istedi, ama geyik hep burnunu çantaya sokuyordu. "Sven, şu kayanın arkasına git ve orada bekle," dedi kraliçe Elsa. Sven başını salladı ve kayanın arkasına geçti. Elsa düz bir taşın üstündeki karı temizledi. Elmaları taşın üstüne yan yana düzgün dizdi. Sonra Sven'i yanına çağırdı. Sven koşarak geldi ve elmaları görünce sevinçle zıpladı. Bütün elmaları yedi ve karda yalnız küçük kırıntılar kaldı. Sven başını Elsa'nın koluna sürttü. "Bu sürpriz senin için, sevgili Sven!" dedi Elsa.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ama geyik hep burnunu"
   - Cümle 3: «Elsa ona bir sürpriz yapmak istedi, ama geyik hep burnunu çantaya sokuyordu.»
   - Açıklama: Sven daha önce geyik olarak tanıtılmadığı için 'geyik' kimi gösterdiği belirsiz.
   - Açıklama: Sven'in geyik olduğu söylenmeden 'geyik' deniyor; kimi gösterdiği belli değil.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 4: «"Sven, şu kayanın arkasına git ve orada bekle," dedi kraliçe Elsa.»
   - Açıklama: Ada bağlı unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 4: «"Sven, şu kayanın arkasına git ve orada bekle," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Kraliçe özelliği yalnız etiket olarak geçiyor, kartın 'kız kardeşini korur' özelliği işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0126` birebir aynı, `@degisim: yeşillenmek -> dizmek` (tutuyorsan), ardından `@onarim: 087d7e8992b115557ae7a223660aebac01da168e`, sonra gövde.

### Hikâye 8: tohum elsa-0127 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0127
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kart', fiil 'eğmek', sıfat 'yumuşak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: kalın kar küçük bir fidanı yere doğru eğmişti | buzdan bir direk yaptı ve fidan ona dayandı
@tohum: elsa-0127
@degisim: kart -> direk
Ormanda Elsa ile Kristoff karla kaplı bir yolda yürüyordu. Elsa yolun kenarında küçük bir fidan gördü. Üstündeki kalın kar, fidanı yere doğru eğmişti. "Bu fidan böyle kırılabilir," dedi Elsa. Kristoff dalları yavaşça silkti ve yumuşak kar yere düştü. Ama fidan yine yerden kalkmadı. Elsa elini salladı ve buzdan ince bir direk yaptı. Direği fidanın yanına, toprağa dikti. Kristoff fidanı yavaşça kaldırdı ve direğe dayadı. Fidan artık dik duruyordu. "Şimdi rahatça büyüyebilir," dedi Kristoff. Elsa bundan sonra kar yağınca yol kenarındaki küçük ağaçlara dikkatle baktı.
```

**Hakem bulguları (3):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kristoff dalları yavaşça silkti"
   - Cümle 5: «Kristoff dalları yavaşça silkti ve yumuşak kar yere düştü.»
   - Açıklama: Sorunun sebebi olan karı yan karakter Kristoff temizliyor ve fidanı da o kaldırıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa elini salladı ve buzdan ince bir direk yaptı"
   - Cümle 7: «Elsa elini salladı ve buzdan ince bir direk yaptı.»
   - Açıklama: Figürün çözümü sebep olan kara değil, sonradan direk kurmaya yöneliyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa bundan sonra kar yağınca yol kenarındaki küçük ağaçlara dikkatle baktı"
   - Cümle 12: «Elsa bundan sonra kar yağınca yol kenarındaki küçük ağaçlara dikkatle baktı.»
   - Açıklama: 'Bundan sonra' ile süren alışkanlık anlatılıyor, fiil 'bakardı' ya da 'bakmaya başladı' olmalı.
   - Açıklama: Tekrarlanan davranış için geniş zamanlı geçmiş gerekir; 'bakardı' ya da 'bakmaya başladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0127` birebir aynı, `@degisim: kart -> direk` (tutuyorsan), ardından `@onarim: e6fd3f19deee70f316f4863b5541334475070b9f`, sonra gövde.

### Hikâye 9: tohum elsa-0128 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0128
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yaprak', fiil 'yankılanmak', sıfat 'keyifli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: yüksek sesle bağırınca geyik şaşırdı ve ağacın arkasına kaçtı | özür diledi ve onu yavaşça yanına çağırdı
@tohum: elsa-0128
Elsa ormanda Sven ile keyifli bir yürüyüş yapıyordu. Sven karın altındaki yaprakları bulup yiyordu. Elsa, sesinin yankılanmasını duymak için birden çok yüksek bağırdı. Ses ağaçların arasında yankılandı. Sven şaşırdı ve bir ağacın arkasına kaçtı. Elsa hatasını anladı ve ağaca doğru yürüdü. "Özür dilerim, Sven, çok yüksek bağırdım," dedi Elsa. Sven başını ağacın arkasından yavaşça çıkardı. Elsa bir avuç yaprak topladı ve ona uzattı. "Gel, Sven, yemeğine burada devam et," dedi kraliçe Elsa. Sven yavaşça yanına geldi ve yaprakları yedi. Sonra burnunu Elsa'nın eline sürttü. Elsa çok sevindi, çünkü Sven onu affetmişti.
```

**Hakem bulguları (8):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sesinin yankılanmasını duymak"
   - Cümle 3: «Elsa, sesinin yankılanmasını duymak için birden çok yüksek bağırdı.»
   - Açıklama: 'Yankılanmak' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sesinin yankılanmasını duymak için"
   - Cümle 3: «Elsa, sesinin yankılanmasını duymak için birden çok yüksek bağırdı.»
   - Açıklama: 'Yankılanma' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elsa, sesinin yankılanmasını duymak için birden çok yüksek bağırdı.»
   - Açıklama: Sven'in kaçması sorunu ancak 5. cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Sven şaşırdı ve bir ağacın arkasına kaçtı"
   - Cümle 5: «Sven şaşırdı ve bir ağacın arkasına kaçtı.»
   - Açıklama: Sorun, Sven'in kaçması, ancak beşinci cümlede söyleniyor.
5. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 10: «"Gel, Sven, yemeğine burada devam et," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Unvan addan önce geldiğinde büyük harfle yazılır: 'Kraliçe Elsa'.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 10: «"Gel, Sven, yemeğine burada devam et," dedi kraliçe Elsa.»
   - Açıklama: Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 10: «"Gel, Sven, yemeğine burada devam et," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi sorunun çözümünde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sven onu affetmişti"
   - Cümle 13: «Elsa çok sevindi, çünkü Sven onu affetmişti.»
   - Açıklama: 'Affetmek' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0128` birebir aynı, ardından `@onarim: 254e60f2fabf5729b79802d64956deaf03280eef`, sonra gövde.

### Hikâye 10: tohum elsa-0129 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0129
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'tablo', fiil 'inmek', sıfat 'eksik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: ağacın tepesinde yıldız eksikti ve eli yetişmiyordu | buzdan bir yıldız yapıp arkadaşından yardım istedi
@tohum: elsa-0129
@degisim: tablo -> yıldız
Ormanda Elsa büyük bir ağacı süslüyordu, Kristoff da yakında kızakla kayıyordu. Dallarda renkli kurdeleler vardı, ama tepede bir yıldız eksikti. Elsa'nın eli en üstteki dala yetişemiyordu. Elsa elini salladı ve buzdan parlak bir yıldız yaptı. "Kristoff, bu yıldızı tepeye koyar mısın?" diye seslendi Elsa. Kristoff kızaktan indi ve hemen yanına geldi. "Tabii, Elsa, hemen koyarım," dedi Kristoff. Kristoff parmaklarının ucuna kalktı ve yıldızı en üstteki dala taktı. Güneş yıldıza vurdu ve bütün ağaç parladı. Elsa ile Kristoff süslü ağacın önünde mutlu mutlu el çırptı.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "tepede bir yıldız eksikti"
   - Cümle 2: «Dallarda renkli kurdeleler vardı, ama tepede bir yıldız eksikti.»
   - Açıklama: Hikayede iki ayrı sorun var: yıldız eksik ve Elsa'nın eli tepeye yetişmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0129` birebir aynı, `@degisim: tablo -> yıldız` (tutuyorsan), ardından `@onarim: 6df2745119da5671cb1c964e204b0d4e3ac6d34f`, sonra gövde.

### Hikâye 11: tohum elsa-0130 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0130
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'vazo', fiil 'katılmak', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: sarayın önünde garip bir ıslık sesi vardı | buzdan kıvrımlı bir parça yapıp rüzgara tuttu
@tohum: elsa-0130
@degisim: vazo -> kapı
Dağda hafif bir rüzgar esiyordu. Elsa buzdan sarayının önünde ince bir ıslık sesi duydu. Sesin nereden geldiğini çok merak etti. Önce kayaların arkasına baktı, ama orada hiçbir şey yoktu. Elsa elinden küçük, kıvrımlı bir buz parçası yaptı ve rüzgara tuttu. Parçanın içinden hava geçince aynı ıslık sesi çıktı. Elsa sarayın kapısına baktı. Kapının üstünde de kıvrımlı buzlar asılıydı. Ses, bu buzlardan geliyordu. Elsa gülümsedi ve kendisi de ıslık çalıp sese katıldı. Elsa bundan sonra rüzgarlı günlerde kapının önünde bu ıslığı keyifle dinledi.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ince bir ıslık sesi duydu"
   - Cümle 2: «Elsa buzdan sarayının önünde ince bir ıslık sesi duydu.»
   - Açıklama: Zararsız bir ıslık sesi çocuğun önemseyeceği gerçek bir sorun değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sesin nereden geldiğini çok merak etti"
   - Cümle 3: «Sesin nereden geldiğini çok merak etti.»
   - Açıklama: Garip bir ıslık sesi gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir şey kaybedilmiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa elinden küçük, kıvrımlı bir buz parçası yaptı"
   - Cümle 5: «Elsa elinden küçük, kıvrımlı bir buz parçası yaptı ve rüzgara tuttu.»
   - Açıklama: 'elinden ... yaptı' ek kullanımı hatalı; 'eliyle' ya da 'elinden ... çıkardı' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa elinden küçük, kıvrımlı bir buz parçası yaptı"
   - Cümle 5: «Elsa elinden küçük, kıvrımlı bir buz parçası yaptı ve rüzgara tuttu.»
   - Açıklama: Elsa'nın neden kıvrımlı bir buz parçası yapıp rüzgara tuttuğu hiçbir öncekinden çıkmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa elinden küçük, kıvrımlı bir buz parçası yaptı ve rüzgara tuttu"
   - Cümle 5: «Elsa elinden küçük, kıvrımlı bir buz parçası yaptı ve rüzgara tuttu.»
   - Açıklama: Elsa'nın neden kıvrımlı bir buz parçası yaptığı önceki olaydan çıkmıyor; çözümü sebepsizce getiriyor.
6. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Ses, bu buzlardan geliyordu"
   - Cümle 9: «Ses, bu buzlardan geliyordu.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.
   - Açıklama: Özneden sonra gereksiz virgül kullanılmış.
7. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa bundan sonra rüzgarlı günlerde"
   - Cümle 11: «Elsa bundan sonra rüzgarlı günlerde kapının önünde bu ıslığı keyifle dinledi.»
   - Açıklama: Son cümle ders değil, sonraki günlere uzanan bir alışkanlık anlatıyor; tek zaman kuralı çiğneniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0130` birebir aynı, `@degisim: vazo -> kapı` (tutuyorsan), ardından `@onarim: 0e7313217732dd666f874675d54d8ccf38c86e72`, sonra gövde.

### Hikâye 12: tohum elsa-0131 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0131
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tabak', fiil 'kapanmak', sıfat 'uzak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: kraliçe içeri koştu ve kapı kardeşinin önünde kapandı | özür diledi ve tabağı alıp kapıyı açık tuttu
@tohum: elsa-0131
Dağın tepesinde Elsa ile Anna buzdan saraya yürüyordu. Anna iki eliyle kurabiye dolu bir tabak taşıyordu. Elsa ise koşup içeri girdi ve buzdan kapı arkasından kapandı. Anna daha uzaktaydı ve elleri tabakla doluydu. "Elsa, kapıyı açamıyorum!" diye seslendi Anna. Elsa hatasını anladı ve kapıyı hemen açtı. "Özür dilerim, Anna, seni beklemem gerekirdi," dedi Elsa. Sonra kraliçe Elsa kardeşinin elinden tabağı aldı. Kapıyı açık tuttu ve Anna içeri girdi. "Önemli değil, Elsa," dedi Anna ve gülümsedi. İki kardeş kurabiyeleri birlikte yedi. Elsa çok sevindi, çünkü Anna onu hemen affetmişti.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa hatasını anladı"
   - Cümle 6: «Elsa hatasını anladı ve kapıyı hemen açtı.»
   - Açıklama: 'Hata' ve 'hatasını anlamak' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Sonra kraliçe Elsa kardeşinin"
   - Cümle 8: «Sonra kraliçe Elsa kardeşinin elinden tabağı aldı.»
   - Açıklama: Unvan addan önce geldiğinde büyük harfle yazılır: 'Kraliçe Elsa'.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra kraliçe Elsa kardeşinin"
   - Cümle 8: «Sonra kraliçe Elsa kardeşinin elinden tabağı aldı.»
   - Açıklama: Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kraliçe Elsa kardeşinin elinden tabağı aldı"
   - Cümle 8: «Sonra kraliçe Elsa kardeşinin elinden tabağı aldı.»
   - Açıklama: Kapı 6. cümlede açılınca sorun çözülmüş, ardından özür, tabağı alma ve kapıyı tutma ile çözüm ikiden fazla adıma yayılıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anna onu hemen affetmişti"
   - Cümle 12: «Elsa çok sevindi, çünkü Anna onu hemen affetmişti.»
   - Açıklama: 'Affetmek' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.
   - Açıklama: 'Affetmek' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0131` birebir aynı, ardından `@onarim: b2e7033c860638c6b690564ddf0aed7d42fc20cf`, sonra gövde.
