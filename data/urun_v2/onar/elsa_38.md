# Editör görevi (onarım): Elsa, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0133
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kapak', fiil 'keşfetmek', sıfat 'hafif'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kardan adamın kızağı yoktu ve kapak çok hafifti | kızağını paylaşıp onu öne oturttu
@tohum: elsa-0133
@degisim: keşfetmek -> bulmak
Elsa karlı ormanda kızağıyla kayıyordu. Olaf'ın ise hiç kızağı yoktu. Olaf yerde bir kutu kapağı buldu ve üstüne oturdu. Ama kapak çok hafifti ve kayarken döndü. Olaf karın içine yuvarlandı. Olaf güldü ama kızağa üzgün üzgün baktı. Elsa kızağını durdurdu. "Olaf, öne otur ve iki elinle sıkı tutun," dedi Kraliçe Elsa. Olaf hemen kraliçenin dediğini yaptı. Elsa da arkaya oturdu. Kızak ikisini ağaçların arasından yavaşça kaydırdı. "Bu çok eğlenceli, Elsa!" dedi Olaf. Elsa ile Olaf aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 8: «"Olaf, öne otur ve iki elinle sıkı tutun," dedi Kraliçe Elsa.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 8: «"Olaf, öne otur ve iki elinle sıkı tutun," dedi Kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak iki kez geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) çözüme katkı vermiyor; yalnız unvan olarak geçiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kızak ikisini ağaçların arasından yavaşça kaydırdı"
   - Cümle 11: «Kızak ikisini ağaçların arasından yavaşça kaydırdı.»
   - Açıklama: Kızak kendi başına kimseyi kaydırmaz; fiil öznesine uymuyor.
   - Açıklama: Kızak kimseyi kaydırmaz; fiil öznesine uymuyor, 'ikisi kızakla kaydı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0133` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 90dd1c9165ff952e068456df8d6aab7625be9144`, sonra gövde.

### Hikâye 2: tohum elsa-0134 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Anna
@tohum: elsa-0134
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çubuk', fiil 'parlatmak', sıfat 'akıllı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | Anna
@plan: tozlu camın üstüne eli uzanamadı | kardeşinden uzun bir çubuk istedi ve camı parlattı
@tohum: elsa-0134
Elsa sarayın büyük salonunda Anna ile karı izlemek istiyordu. Ama salonun penceresi çok tozluydu ve dışarısı iyi görünmüyordu. Elsa bir bezle camı silmeye başladı ama üstüne uzanamadı. Anna hemen bir sandalyeye çıkmak istedi. Kraliçe Elsa kardeşini korudu ve buna izin vermedi. Sonra Anna'dan köşedeki uzun çubuğu getirmesini istedi. Anna çubuğu getirdi. Akıllı kardeşi çubuğun ucuna bir bez de bağladı. Elsa çubuğu tuttu ve camın üstünü yavaş yavaş parlattı. Cam pırıl pırıl oldu. Dışarıdaki beyaz kar artık çok iyi görünüyordu. Elsa çok sevindi, çünkü kardeşiyle birlikte karı izleyebiliyordu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tozlu camın üstüne eli uzanamadı"
   - Cümle 0 (plan satırı): «tozlu camın üstüne eli uzanamadı | kardeşinden uzun bir çubuk istedi ve camı parlattı»
   - Açıklama: 'Camın üstüne' camın üst kısmı anlamında yanlış kullanılmış; 'camın üst kısmına' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "silmeye başladı ama üstüne uzanamadı"
   - Cümle 3: «Elsa bir bezle camı silmeye başladı ama üstüne uzanamadı.»
   - Açıklama: 'Üstüne uzanmak' üzerine yatmak anlamına da gelir; 'üst kısmına' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "camı silmeye başladı ama üstüne uzanamadı"
   - Cümle 3: «Elsa bir bezle camı silmeye başladı ama üstüne uzanamadı.»
   - Açıklama: 'Üstüne uzanamadı' camın üst kısmına ulaşamadığını doğru anlatmıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Akıllı kardeşi çubuğun ucuna"
   - Cümle 8: «Akıllı kardeşi çubuğun ucuna bir bez de bağladı.»
   - Açıklama: 'Kardeşi' Anna'yı mı Elsa'yı mı gösteriyor belli değil.
   - Açıklama: 'Kardeşi' zamiri Elsa'yı mı Anna'yı mı gösterdiği belli değil.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Akıllı kardeşi çubuğun ucuna bir bez de bağladı"
   - Cümle 8: «Akıllı kardeşi çubuğun ucuna bir bez de bağladı.»
   - Açıklama: Çözümün kilit adımını yan karakter Anna atıyor ve akıllılık ona veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0134` birebir aynı, ardından `@onarim: db599e94cd0501b8bf700dcae41b01e50eb30011`, sonra gövde.

### Hikâye 3: tohum elsa-0137 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0137
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çadır', fiil 'beklemek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: çadırın içi karışıktı ve kurabiye kutusu bulunamadı | eşyaları sıraya dizdirdi ve kutuyu buldu
@tohum: elsa-0137
Ormanda karlı ağaçların arasında Kristoff'un yeni çadırı vardı. Elsa ile Kristoff çadırın önünde küçük bir kutlama yapacaktı. Ama çadırın içi çok karışıktı ve Kristoff kurabiye kutusunu bulamadı. Kraliçe Elsa, Kristoff'a her şeyi dışarı çıkarmasını söyledi. Kristoff kraliçenin dediğini yaptı. Elsa da eşyaları karın üstüne bir sıraya dizdi. İplerin arasından küçük kurabiye kutusu çıktı. Kristoff eşyaları geri koydu ve Elsa onu bekledi. Sonra ikisi çadırın önüne oturdu ve kurabiye yedi. Yeni çadırı mutlu mutlu kutladılar. Kristoff bundan sonra Elsa'nın dediği gibi çadırını hep düzenli tuttu.
```

**Hakem bulguları (7):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kristoff'un yeni çadırı vardı"
   - Cümle 1: «Ormanda karlı ağaçların arasında Kristoff'un yeni çadırı vardı.»
   - Açıklama: Kristoff'un çadırı kartın yanlar ve yerler bölümünde yok; kapalı dünyaya eklenmiş bir ev/eşya.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa, Kristoff'a her"
   - Cümle 4: «Kraliçe Elsa, Kristoff'a her şeyi dışarı çıkarmasını söyledi.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Kristoff'a her şeyi"
   - Cümle 4: «Kraliçe Elsa, Kristoff'a her şeyi dışarı çıkarmasını söyledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan ve emir olarak geçiyor; kartın özellik alanındaki kız kardeşini koruma biçiminde kullanılmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kristoff kraliçenin dediğini yaptı"
   - Cümle 5: «Kristoff kraliçenin dediğini yaptı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız emir veren unvan olarak kullanılıyor, karttaki gibi değil.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yeni çadırı mutlu mutlu kutladılar"
   - Cümle 10: «Yeni çadırı mutlu mutlu kutladılar.»
   - Açıklama: Çadır kutlanmaz; fiil nesnesine uymuyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa'nın dediği gibi çadırını"
   - Cümle 11: «Kristoff bundan sonra Elsa'nın dediği gibi çadırını hep düzenli tuttu.»
   - Açıklama: Elsa çadırı düzenli tutmayı hiç söylemedi; 'dediği gibi' yanlış kullanılmış.
7. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kristoff bundan sonra Elsa'nın dediği gibi çadırını hep düzenli tuttu"
   - Cümle 11: «Kristoff bundan sonra Elsa'nın dediği gibi çadırını hep düzenli tuttu.»
   - Açıklama: Elsa çadırı düzenli tutmayı hiç söylemedi, yalnız eşyaları dışarı çıkarmasını söyledi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0137` birebir aynı, ardından `@onarim: 53641ab2314ac2352c8e322c7c634feeec59ec31`, sonra gövde.

### Hikâye 4: tohum elsa-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Olaf
@tohum: elsa-0138
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'muz', fiil 'çağırmak', sıfat 'resimli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | Olaf
@plan: kar kitaba düştü ve muz resmi bozuldu | özür diledi ve buzdan bir muz yaptı
@tohum: elsa-0138
Sarayın büyük salonunda Elsa elinden kar taneleri çıkarıyordu. Olaf da yanında resimli bir kitaba bakıyordu. Elsa elini birden salladı ve kar, Olaf'ın kitabına düştü. Kitap ıslandı ve sayfadaki sarı muz resmi bozuldu. Olaf üzgün üzgün kitaba baktı. Elsa hemen Olaf'tan özür diledi. Sonra onu yanına çağırdı. Elsa elini yavaşça açtı ve buzdan bir muz yaptı. Bu muz, kitaptaki muza çok benziyordu. Olaf buzdan muzu eline aldı ve güldü. Sonra Elsa'ya sıkıca sarıldı. Elsa ile Olaf buzdan muzla salonda mutlu mutlu oynadı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kar, Olaf'ın kitabına düştü"
   - Cümle 3: «Elsa elini birden salladı ve kar, Olaf'ın kitabına düştü.»
   - Açıklama: Buz ve kar gücü hem sorunu yaratmak hem çözmek için iki kez kullanılıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra onu yanına çağırdı"
   - Cümle 7: «Sonra onu yanına çağırdı.»
   - Açıklama: Olaf zaten Elsa'nın yanındayken onu yanına çağırması çelişiyor.
   - Açıklama: Olaf zaten Elsa'nın yanında olduğu halde Elsa onu yanına çağırıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "buzdan bir muz yaptı"
   - Cümle 8: «Elsa elini yavaşça açtı ve buzdan bir muz yaptı.»
   - Açıklama: Bozulan kitap resmi düzeltilmiyor; buzdan muz sebebe değil telafiye yöneliyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa elini yavaşça açtı ve buzdan bir muz yaptı"
   - Cümle 8: «Elsa elini yavaşça açtı ve buzdan bir muz yaptı.»
   - Açıklama: Çözüm bozulan kitap resmine yönelmiyor; resim düzelmeden yerine başka bir oyuncak veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0138` birebir aynı, ardından `@onarim: 7b4cdd7bd4726668fc820e5d5840802a52094bf4`, sonra gövde.

### Hikâye 5: tohum elsa-0140 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0140
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'zincir', fiil 'koklamak', sıfat 'meraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: ince buz halkaları koptu ve zincir düştü | daha kalın halkalar yapıp zinciri yeniden taktı
@tohum: elsa-0140
@degisim: koklamak -> saymak
Meraklı martılar limanın üstünde ötüyordu. Elsa fiyort kıyısında buzdan uzun bir zincir yapıp havaya kaldırdı. Ama halkalar çok inceydi ve zincir ortadan koptu. Halkalar taşların üstüne düştü. Elsa buna çok güldü. Bu kez elinden daha kalın halkalar çıkardı. Halkaları bir, iki, üç diye saydı ve birbirine taktı. On halka olunca zinciri yavaşça havaya kaldırdı. Kalın zincir bu sefer sağlam kaldı. Zincir güneşte pırıl pırıl parladı. Elsa sevinçle zincire yeni halkalar ekledi ve oyununa devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yapıp zinciri yeniden taktı"
   - Cümle 0 (plan satırı): «ince buz halkaları koptu ve zincir düştü | daha kalın halkalar yapıp zinciri yeniden taktı»
   - Açıklama: Zincir bir yere takılmıyor, yeniden yapılıyor; 'taktı' fiili anlama uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa fiyort kıyısında buzdan"
   - Cümle 2: «Elsa fiyort kıyısında buzdan uzun bir zincir yapıp havaya kaldırdı.»
   - Açıklama: 'fiyort' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Fiyort' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa buna çok güldü"
   - Cümle 5: «Elsa buna çok güldü.»
   - Açıklama: Zincirin kopması Elsa'yı hiç üzmüyor; sorun önemsiz bir olay olarak kalıyor.
   - Açıklama: Figür kopan zincire gülüyor, bu da sorunun çocuğun önemseyeceği bir şey olmadığını gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0140` birebir aynı, `@degisim: koklamak -> saymak` (tutuyorsan), ardından `@onarim: 130c471a535a2884dd23470002ddcac7e5e831a9`, sonra gövde.

### Hikâye 6: tohum elsa-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0141
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'brokoli', fiil 'sokulmak', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: buzdan brokolinin ince sapı devrildi | kalın ve kısa yeni bir sap yaptı
@tohum: elsa-0141
@degisim: sokulmak -> gülmek
Bir sabah Elsa fiyort kıyısında heyecanlı bir oyun oynuyordu. Elinden buzdan kocaman bir brokoli yapıyordu. Ama brokolinin sapı çok inceydi ve brokoli devrildi. Brokoli taşların üstünde küçük bir ağaç gibi yatıyordu. Elsa buna baktı ve güldü. Sonra elini yavaşça oynattı. Bu kez kalın ve kısa bir sap yaptı. Sonra brokolinin başını dikkatle üstüne koydu. Elsa elini çekti ve bekledi. Brokoli hiç sallanmadı. Güneşte pırıl pırıl parladı. Elsa çok sevindi, çünkü buzdan brokoli artık dimdik duruyordu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "fiyort kıyısında heyecanlı"
   - Cümle 1: «Bir sabah Elsa fiyort kıyısında heyecanlı bir oyun oynuyordu.»
   - Açıklama: 'Fiyort' 3 yaşındaki bir çocuğun bilmediği bir kelime.
   - Açıklama: 'Fiyort' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elinden buzdan kocaman"
   - Cümle 2: «Elinden buzdan kocaman bir brokoli yapıyordu.»
   - Açıklama: Hal eki yanlış; 'Elleriyle' ya da 'Elleriyle buzdan' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elinden buzdan kocaman bir brokoli"
   - Cümle 2: «Elinden buzdan kocaman bir brokoli yapıyordu.»
   - Açıklama: 'Elinden buzdan' yapısı bozuk; 'Elinden çıkan buzla' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0141` birebir aynı, `@degisim: sokulmak -> gülmek` (tutuyorsan), ardından `@onarim: be921086677548e7bf0f9dcbcaa62fcb42ec49ec`, sonra gövde.

### Hikâye 7: tohum elsa-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0143
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'örgü', fiil 'tamamlanmak', sıfat 'şirin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: kaydırak geyik için çok dardı | buzla kaydırağı daha geniş yapıp geyikle paylaştı
@tohum: elsa-0143
@degisim: örgü -> kaydırak
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa tepeden aşağı buzdan şirin bir kaydırak yapmıştı. Sven de kaymak istedi, ama kaydırak ona çok dardı. Sven kaydırağın başında üzgün üzgün bekledi. "Gel, Sven, bu kaydırağı paylaşalım," dedi Elsa. Elsa ellerini kaydırağın iki yanına uzattı. Elinden çıkan buz, kaydırağı daha geniş yaptı. Kaydırak tamamlanınca Sven sevinçle ayağını yere vurdu. Önce Elsa kaydı, sonra Sven dört ayağını açıp aşağı kaydı. Sven karın içine yuvarlandı ve burnundan neşeyle ses çıkardı. "Sıra yine sende, Sven!" dedi Elsa gülerek. Elsa çok mutluydu, çünkü kaydırağını Sven'le paylaşmıştı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "buzdan şirin bir kaydırak"
   - Cümle 2: «Elsa tepeden aşağı buzdan şirin bir kaydırak yapmıştı.»
   - Açıklama: Tohumdaki buz özelliği bir kez değil, kaydırağı yapmak ve genişletmek için iki kez kullanılıyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Elinden çıkan buz, kaydırağı"
   - Cümle 7: «Elinden çıkan buz, kaydırağı daha geniş yaptı.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elinden çıkan buz, kaydırağı daha geniş yaptı"
   - Cümle 7: «Elinden çıkan buz, kaydırağı daha geniş yaptı.»
   - Açıklama: Tohumdaki buz özelliği kaydırağı yapmak ve genişletmek için iki kez kullanılıyor; kart 'ozellikler' bir kez kullanım ister.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0143` birebir aynı, `@degisim: örgü -> kaydırak` (tutuyorsan), ardından `@onarim: 8d5aad1f2d140167c4a4b874879ff988c381e968`, sonra gövde.

### Hikâye 8: tohum elsa-0144 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0144
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'taş', fiil 'sıralamak', sıfat 'hareketli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: yolun kenarından garip bir ses geldi | sesin taşlardan geldiğini buldu ve suyun yanına taş sıraladı
@tohum: elsa-0144
Elsa karlı ormanda yürüyordu. Birden yolun kenarından garip bir ses geldi. Tık, tık, tık! Elsa bu sesi çok merak etti ve yavaşça yaklaştı. Karın altından ince bir su akıyordu. Su küçük taşları itiyordu ve taşlar birbirine çarpıyordu. Ses bu hareketli taşlardan geliyordu. Ama su karın altında kalmıştı ve hiç görünmüyordu. Elsa bu krallığın kraliçesiydi ve yoldan geçen herkesi korumak istedi. Suyun iki yanına büyük taşlar sıraladı. Artık herkes suyu görecek ve ayağını ıslatmayacaktı. Elsa bundan sonra garip bir ses duyunca hemen gidip baktı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yolun kenarından garip bir ses geldi"
   - Cümle 2: «Birden yolun kenarından garip bir ses geldi.»
   - Açıklama: Garip bir ses duymak çözülmesi gereken bir sorun değil; asıl çözülen sorunla ilgisiz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yolun kenarından garip bir ses geldi"
   - Cümle 2: «Birden yolun kenarından garip bir ses geldi.»
   - Açıklama: Garip bir ses duymak çocuğun önemseyeceği somut bir sorun değil ve sebebi sorun sayılmıyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama su karın altında kalmıştı ve hiç görünmüyordu"
   - Cümle 8: «Ama su karın altında kalmıştı ve hiç görünmüyordu.»
   - Açıklama: Garip ses sorunu çözülünce görünmeyen su gibi ikinci bir sorun ortaya çıkıyor.
   - Açıklama: Garip ses merakı çözüldükten sonra görünmeyen su diye ikinci bir sorun başlıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elsa bundan sonra garip bir ses duyunca hemen gidip baktı"
   - Cümle 12: «Elsa bundan sonra garip bir ses duyunca hemen gidip baktı.»
   - Açıklama: Garip bir ses duyunca hemen gidip bakmak çocuğun taklit edebileceği güvensiz bir davranış olarak örnek gösteriliyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra garip bir ses duyunca hemen gidip baktı"
   - Cümle 12: «Elsa bundan sonra garip bir ses duyunca hemen gidip baktı.»
   - Açıklama: Son cümle olaya bağlı sıcak bir kapanış vermiyor ve dersi taş sıralama çözümünden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0144` birebir aynı, ardından `@onarim: 6172f932acacb00d36798130f7d5a25807920b46`, sonra gövde.

### Hikâye 9: tohum elsa-0145 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0145
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'pirinç', fiil 'yazmak', sıfat 'bembeyaz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: kar yolu örttü ve saraya giden yol görünmedi | saraya giden yolu karın üstüne yazıp gösterdi
@tohum: elsa-0145
Bir sabah Elsa karlı ormanda Kristoff ile karşılaştı. Kristoff'un kızağında saray için büyük bir pirinç çuvalı vardı. Ama kar yolu örtmüştü ve her yer bembeyazdı. "Elsa, saraya hangi yoldan gideceğimi bilmiyorum," dedi Kristoff. Önlerinde iki yol vardı. Elsa bir dal aldı ve bir yolun başına büyük bir ok çizdi. Okun yanına da "saray" yazdı. "Kristoff, bu okun gösterdiği yoldan git," dedi Elsa. Kristoff kraliçenin sözünü dinledi ve kızağını o yola sürdü. Biraz sonra ağaçların arasından sarayın kuleleri göründü. "Buldum, teşekkürler!" diye bağırdı Kristoff. Elsa bundan sonra kar yağınca her yol başına bir ok çizdi.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Önlerinde iki yol vardı"
   - Cümle 5: «Önlerinde iki yol vardı.»
   - Açıklama: Kar yolu örtmüşken ve yol görünmüyorken önlerinde iki yolun görünmesi çelişiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kristoff kraliçenin sözünü dinledi"
   - Cümle 9: «Kristoff kraliçenin sözünü dinledi ve kızağını o yola sürdü.»
   - Açıklama: 'Kraliçe' daha önce tanıtılmadan Elsa'yı göstermek için kullanılıyor; kimi gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kristoff kraliçenin sözünü dinledi"
   - Cümle 9: «Kristoff kraliçenin sözünü dinledi ve kızağını o yola sürdü.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor; sorunu çizilen ok çözüyor.
   - Açıklama: Kartın özellikler alanındaki kraliçelik yalnız süs olarak anılıyor; sorunu ok çizmek çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0145` birebir aynı, ardından `@onarim: c0d3f94533792acbe37a94171bacaa9a2a2b0257`, sonra gövde.

### Hikâye 10: tohum elsa-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0147
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sırayla oynamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'düğme', fiil 'giymek', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: ikisi de eski paltoyu aynı anda giymek istedi | buzdan bir yıldız yaptı ve yıldızı sırayla verdi
@tohum: elsa-0147
Elsa ile Olaf dağda, buz sarayının önünde oynuyordu. Giyinme oyunu için eskimiş kırmızı bir palto getirmişlerdi. Ama ikisi de paltoyu aynı anda giymek istedi. Olaf bir kolu çekti, Elsa öbür kolu tuttu. Elsa biraz düşündü. Sonra elinden buz çıktı ve küçük bir buz yıldızı oldu. Yıldızı tutan paltoyu giyecekti. Elsa yıldızı önce Olaf'a verdi. Olaf paltoyu giydi ve büyük düğmeleri tek tek kapattı. Palto ona çok büyük geldi ve Olaf karda komik adımlarla yürüdü. Sonra Olaf yıldızı Elsa'ya uzattı. Elsa da paltoyu giydi ve iki kez döndü. Elsa çok mutlu oldu, çünkü sırayla oynadıkları için ikisi de eğlenmişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Olaf bir kolu çekti"
   - Cümle 4: «Olaf bir kolu çekti, Elsa öbür kolu tuttu.»
   - Açıklama: Tamlayan eksik; 'paltonun bir kolunu' olmalı, yoksa Olaf'ın kendi kolu sanılabilir.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü sırayla oynadıkları için"
   - Cümle 13: «Elsa çok mutlu oldu, çünkü sırayla oynadıkları için ikisi de eğlenmişti.»
   - Açıklama: 'Çünkü' ile '-dıkları için' birlikte kullanılmış; sebep iki kez bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0147` birebir aynı, ardından `@onarim: 38a8292de0ab90914646671e0018c781d3f4bcc7`, sonra gövde.

### Hikâye 11: tohum elsa-0148 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0148
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'zambak', fiil 'uçuşmak', sıfat 'şaşkın'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: ağır buzlar küçük bir fidanın üstüne konacaktı | buzları taşın yanına koymasını söyledi
@tohum: elsa-0148
@degisim: zambak -> fidan
Elsa dağda, havada uçuşan kar tanelerini izliyordu. Birden karın arasında küçük yeşil bir fidan fark etti. Ama Kristoff ağır buz parçalarını tam fidanın üstüne koymak üzereydi. "Dur, Kristoff!" dedi Elsa. Kristoff şaşkın bir yüzle durdu ve Elsa'ya baktı. "Kristoff, buzları şu büyük taşın yanına koy," dedi Elsa. Kristoff kraliçenin sözünü dinledi ve buzları taşın yanına taşıdı. Sonra eğildi ve fidana dikkatle baktı. "Karın içinde fidan mı büyüyor?" diye sordu Kristoff. Elsa gülümsedi ve fidanın üstündeki karı eliyle yavaşça açtı. Fidanın yaprakları güneşte parladı. "Teşekkürler, Kristoff, fidan artık güvende!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kristoff kraliçenin sözünü dinledi"
   - Cümle 7: «Kristoff kraliçenin sözünü dinledi ve buzları taşın yanına taşıdı.»
   - Açıklama: Elsa hiç kraliçe olarak anılmadan 'kraliçe' diye gösteriliyor; kimi kastettiği küçük çocuğa belli değil.
   - Açıklama: 'Kraliçe' daha önce tanıtılmadan Elsa'yı göstermek için kullanılıyor; kimi gösterdiği belli değil.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Fidanın yaprakları güneşte parladı"
   - Cümle 11: «Fidanın yaprakları güneşte parladı.»
   - Açıklama: Hikaye havada kar uçuşurken başlıyor ama birden güneş parlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0148` birebir aynı, `@degisim: zambak -> fidan` (tutuyorsan), ardından `@onarim: ca1baa2569b5c002c8150ff8f72b99eeac4415c7`, sonra gövde.

### Hikâye 12: tohum elsa-0149 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0149
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'maske', fiil 'karışmak', sıfat 'sakar'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: karda bir gözü eksik bir yüz şekli vardı | yüze göz ve taç çizip bir maske yaptı
@tohum: elsa-0149
@degisim: sakar -> kocaman
Elsa karlı ormanda tek başına yürüyordu. Birden karın üstünde garip bir şekil fark etti. Karda çizgiler birbirine karışmış ve kocaman bir yüz gibi olmuştu. Ama bu yüzün yalnız bir gözü vardı. Elsa bu yüzü güzel bir maskeye çevirmek istedi. Yerden ince bir dal aldı. Dalla karın üstüne ikinci bir göz çizdi. Sonra yüzün çevresine büyük bir daire çizdi. En üste de kendi tacına benzeyen bir kraliçe tacı çizdi. Karda artık kocaman bir kraliçe maskesi vardı. Elsa maskenin yanına eğildi ve güldü. Elsa ormanda yeni şekiller aramaya mutlu mutlu devam etti.
```

**Hakem bulguları (9):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "karın üstünde garip bir şekil"
   - Cümle 2: «Birden karın üstünde garip bir şekil fark etti.»
   - Açıklama: Ormanda tek başına karşılaşılan tek gözlü kocaman garip yüz küçük çocuk için ürkütücü olabilir.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Karda çizgiler birbirine karışmış ve kocaman bir yüz gibi olmuştu.»
   - Açıklama: Yüzün tek gözü olduğu ancak 4. cümlede söyleniyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Karda çizgiler birbirine karışmış"
   - Cümle 3: «Karda çizgiler birbirine karışmış ve kocaman bir yüz gibi olmuştu.»
   - Açıklama: Şeklin nasıl oluştuğu söylenmiyor ve tek gözlü bir kar şekli çocuğun önemseyeceği gerçek bir sorun değil.
4. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "yüzün yalnız bir gözü vardı"
   - Cümle 4: «Ama bu yüzün yalnız bir gözü vardı.»
   - Açıklama: Karda beliren garip, tek gözlü kocaman yüz küçük çocuk için ürkütücü olabilir.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama bu yüzün yalnız bir gözü vardı"
   - Cümle 4: «Ama bu yüzün yalnız bir gözü vardı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
6. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama bu yüzün yalnız bir gözü vardı"
   - Cümle 4: «Ama bu yüzün yalnız bir gözü vardı.»
   - Açıklama: Karda tek gözlü bir şekil görmek çocuğun önemseyeceği gerçek bir sorun değil.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu yüzü güzel bir maskeye çevirmek"
   - Cümle 5: «Elsa bu yüzü güzel bir maskeye çevirmek istedi.»
   - Açıklama: Kara çizilen yüz takılabilen bir maske değildir; kelime yanlış anlamda kullanılmış.
8. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir kraliçe tacı çizdi"
   - Cümle 9: «En üste de kendi tacına benzeyen bir kraliçe tacı çizdi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız çizilen taç olarak geçiyor, karttaki gibi kullanılmıyor.
9. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kendi tacına benzeyen bir kraliçe tacı"
   - Cümle 9: «En üste de kendi tacına benzeyen bir kraliçe tacı çizdi.»
   - Açıklama: Kartın özellikler alanındaki kraliçelik (kız kardeşini koruma) işe yarar biçimde kullanılmıyor, yalnız bir taç çizimine indirgeniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0149` birebir aynı, `@degisim: sakar -> kocaman` (tutuyorsan), ardından `@onarim: 4fafd093100c1c542d272360a3c098a50164f062`, sonra gövde.
