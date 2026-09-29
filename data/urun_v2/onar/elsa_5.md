# Editör görevi (onarım): Elsa, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0003 (deneme 5 -> 6)

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
@plan: rüzgar esti ve şemsiye yerde durmadı | şemsiyenin dibine buzdan sağlam bir ayak yaptı
@tohum: elsa-0003
Bir sabah Elsa ile Olaf kıyıda yaz oyunu oynuyordu. Olaf büyük bir şemsiyeyi yere dikti. Ama rüzgar esti ve şemsiye düştü. Olaf onu tekrar dikti, ama şemsiye yine devrildi. "Elsa, bu şemsiye hiç durmuyor!" dedi Olaf. Elsa eğildi ve şemsiyenin dibine buzdan sağlam bir ayak yaptı. Rüzgar bir kez daha esti, ama şemsiye bu kez kıpırdamadı. İkisi şemsiyenin altına oturdu ve yemek yedi. "Sıcak yaz günlerini çok severim!" dedi Olaf ve güldü. Elsa çok sevindi, çünkü şemsiyeleri artık rüzgarda hiç düşmüyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kıyıda yaz oyunu oynuyordu"
   - Cümle 1: «Bir sabah Elsa ile Olaf kıyıda yaz oyunu oynuyordu.»
   - Açıklama: 'Yaz oyunu oynamak' belirsiz ve doğal olmayan bir kullanım; ne oynandığı anlaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0003` birebir aynı, ardından `@onarim: cc17df43e988afb4a0897e4482c872601bad4902`, sonra gövde.

### Hikâye 2: tohum elsa-0006 (deneme 5 -> 6)

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
@degisim: toplanmak -> dinlemek
Soğuk bir sabah Elsa ile Sven dağda yürüyordu. Elsa'nın kolunda poğaça dolu bir sepet vardı. Birden yakından garip bir ses duyuldu. "Bu ses nereden geliyor, Sven?" diye sordu Elsa. Sven hemen sepete baktı. Ses yine geldi. Elsa durdu ve sesi dinledi. Sonra kulağını Sven'in karnına yaklaştırdı. "Sven, bu ses senin karnından geliyor!" dedi Elsa ve güldü. Sven çok acıkmıştı. Sven başını sepete soktu, ama büyük başı küçük sepete sığmadı. Elsa buzdan geniş bir tabak yaptı. İki poğaçayı tabağa koydu ve Sven onları hemen yedi. Sonra Elsa ile Sven yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "büyük başı küçük sepete sığmadı"
   - Cümle 11: «Sven başını sepete soktu, ama büyük başı küçük sepete sığmadı.»
   - Açıklama: Garip ses sorunu çözüldükten sonra başın sepete sığmaması ikinci bir sorun olarak ekleniyor.
   - Açıklama: Garip ses sorunu çözüldükten sonra başın sepete sığmaması diye ikinci bir sorun açılıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa buzdan geniş bir tabak yaptı"
   - Cümle 12: «Elsa buzdan geniş bir tabak yaptı.»
   - Açıklama: Çözüm sesi dinleme, kaynağı bulma, tabak yapma ve besleme olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0006` birebir aynı, `@degisim: toplanmak -> dinlemek` (tutuyorsan), ardından `@onarim: 4ce6b1e0be2b213f27d2523d8ed62819c29b2608`, sonra gövde.

### Hikâye 3: tohum elsa-0007 (deneme 5 -> 6)

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
@plan: sert bir rüzgar mavi bağcığı uçurdu | rüzgarın estiği yöne yürüdü ve bağcığı çitin yanında buldu
@tohum: elsa-0007
@degisim: saygılı -> uzun
Bir sabah Elsa limanın kıyısında yürüyordu. Mavi bir bağcık uzun kraliçe pelerinini boynunda tutuyordu. Birden denizden sert bir rüzgar esti ve bağcığı uçurdu. Pelerin yere doğru kaymaya başladı. Elsa pelerinini bir eliyle tuttu ve düşündü. Rüzgar denizden karaya doğru esiyordu. Bu yönde, yolun kenarında bir çit vardı. Elsa hemen o çite doğru yürüdü. Çitin yanındaki otların arasına baktı ve bağcığı buldu. Sonra pelerinini yeniden sıkıca bağladı. Rüzgarın dağıttığı saçlarını da parmaklarıyla taradı. Elsa çok sevindi, çünkü kaybolan bağcığı kendi başına bulmuştu.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "uzun kraliçe pelerinini boynunda tutuyordu"
   - Cümle 2: «Mavi bir bağcık uzun kraliçe pelerinini boynunda tutuyordu.»
   - Açıklama: Cümlede Elsa geçmiyor; iyelik ve 'boynunda' kimi gösterdiği belirsiz, özne bağcık.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "uzun kraliçe pelerinini boynunda"
   - Cümle 2: «Mavi bir bağcık uzun kraliçe pelerinini boynunda tutuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohum özelliği kraliçelik yalnız pelerin sıfatı olarak geçiyor, kartındaki gibi işe yarar biçimde kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgarın dağıttığı saçlarını da parmaklarıyla taradı"
   - Cümle 11: «Rüzgarın dağıttığı saçlarını da parmaklarıyla taradı.»
   - Açıklama: Saç tarama olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "saçlarını da parmaklarıyla taradı"
   - Cümle 11: «Rüzgarın dağıttığı saçlarını da parmaklarıyla taradı.»
   - Açıklama: Saç tarama olayla ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0007` birebir aynı, `@degisim: saygılı -> uzun` (tutuyorsan), ardından `@onarim: d223d1d7153fd981c9305da6cc147c67c3de017f`, sonra gövde.

### Hikâye 4: tohum elsa-0010 (deneme 5 -> 6)

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
@degisim: faydalı -> kaygan
Limanda kayıklar yavaş yavaş sallanıyordu. Elsa ile Sven hafif karın altında kıyıda oturuyordu. Birden Sven'in havuç kovası kaygan kıyıda kaydı ve havuçlar denize düştü. Sven üzgün üzgün suya baktı, çünkü çok acıkmıştı. Elsa'nın sepetinde yalnız üç havuç vardı. "Gel, Sven, havuçlarımı seninle paylaşayım," dedi Elsa. Havuçlar yine düşmesin diye buzdan beşik şeklinde derin bir kase yaptı. Havuçların üstündeki karı silkti. İki havucu kaseye koydu ve Sven'in önüne itti. Sven havuçları hemen yedi. Elsa da kendi havucunu yedi. Elsa ile Sven kıyıda yan yana mutlu mutlu karı izledi.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kaygan kıyıda kaydı ve havuçlar denize düştü"
   - Cümle 3: «Birden Sven'in havuç kovası kaygan kıyıda kaydı ve havuçlar denize düştü.»
   - Açıklama: Kaygan ve suya düşülen kıyı kenarında oturmak çocuğun taklit edebileceği tehlikeli bir durum olarak sürdürülüyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "buzdan beşik şeklinde derin bir kase"
   - Cümle 7: «Havuçlar yine düşmesin diye buzdan beşik şeklinde derin bir kase yaptı.»
   - Açıklama: Kaseyi beşik şekline benzetmek kelimeyi yanlış anlamda kullanıyor ve çocuk için anlamsız bir tarif oluşturuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "buzdan beşik şeklinde derin"
   - Cümle 7: «Havuçlar yine düşmesin diye buzdan beşik şeklinde derin bir kase yaptı.»
   - Açıklama: 'Beşik şeklinde' benzetmesi 3 yaşındaki çocuk için soyut ve kaseye uymuyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "buzdan beşik şeklinde derin bir kase yaptı"
   - Cümle 7: «Havuçlar yine düşmesin diye buzdan beşik şeklinde derin bir kase yaptı.»
   - Açıklama: Çözüm paylaşmanın yanında kase yapma, kar silkme ve koyma gibi ikiden fazla adıma yayılıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Havuçların üstündeki karı silkti"
   - Cümle 8: «Havuçların üstündeki karı silkti.»
   - Açıklama: Kar silkme ve beşik şeklindeki kase olayda işe yaramayan ayrıntılar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0010` birebir aynı, `@degisim: faydalı -> kaygan` (tutuyorsan), ardından `@onarim: 8da5975c3c491626fe61b6c6f02017f1ac6ecc87`, sonra gövde.

### Hikâye 5: tohum elsa-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0012
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'fiyonk', fiil 'okumak', sıfat 'çekingen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: kurdele hep açıldı çünkü fiyonk bağlamayı bilmiyordu | arkadaşından yardım istedi ve fiyonk bağlamayı öğrendi
@tohum: elsa-0012
@degisim: okumak -> bağlamak
Bir sabah Elsa sarayın önünde buzdan küçük bir çiçek yaptı. Çiçeğin sapına kırmızı bir fiyonk bağlamak istedi. Ama fiyonk bağlamayı bilmiyordu ve kurdele hep açıldı. Kristoff biraz ileride kızağını dolduruyordu. Elsa önce biraz çekingen davrandı. Sonra Kristoff'un yanına yürüdü. "Kristoff, bana fiyonk bağlamayı öğretir misin?" diye sordu Elsa. "Tabii, çok kolay," dedi Kristoff. Kristoff her adımı yavaşça gösterdi. Elsa da iki halka yaptı ve onları sıkıca bağladı. Bu kez kurdele hiç açılmadı. "Teşekkürler, Kristoff, fiyonk artık çok güzel!" dedi Elsa.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "buzdan küçük bir çiçek yaptı"
   - Cümle 1: «Bir sabah Elsa sarayın önünde buzdan küçük bir çiçek yaptı.»
   - Açıklama: Tohumdaki buz özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa sarayın önünde buzdan"
   - Cümle 1: «Bir sabah Elsa sarayın önünde buzdan küçük bir çiçek yaptı.»
   - Açıklama: Başlıktaki yer dağ ama hikaye sarayın önünde geçiyor ve dağ hiç anılmıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa önce biraz çekingen davrandı"
   - Cümle 5: «Elsa önce biraz çekingen davrandı.»
   - Açıklama: 'Çekingen davranmak' 3 yaşındaki çocuk için soyut bir kavram.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "biraz çekingen davrandı"
   - Cümle 5: «Elsa önce biraz çekingen davrandı.»
   - Açıklama: 'Çekingen davranmak' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0012` birebir aynı, `@degisim: okumak -> bağlamak` (tutuyorsan), ardından `@onarim: 067aef751e742c6af430d464ee4f81306f7def06`, sonra gövde.

### Hikâye 6: tohum elsa-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0013
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çekmece', fiil 'öpmek', sıfat 'parlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kızak küçüktü ve ikisi birden sığmadı | sırayla binip tepeden kaymayı önerdi
@tohum: elsa-0013
@degisim: çekmece -> kızak
Elsa ile Olaf karlı ormanda küçük bir tepenin başındaydı. Elsa elini salladı ve buzdan parlak bir kızak yaptı. Ama kızak çok küçüktü ve ikisi birden sığmadı. "Önce ben kaymak istiyorum!" dedi Olaf. Elsa biraz düşündü. "Sırayla binelim, önce sen kay, Olaf," dedi Elsa. Olaf kızağa bindi ve tepeden neşeyle kaydı. Aşağıda el çırptı ve kızağı geri getirdi. "Sıra sende, Elsa," dedi Olaf. Elsa da tepeden hızla kaydı ve güldü. İkisi sırayla tam beş kez kaydı. Sonunda Olaf sevinçle Elsa'nın yanağını öptü. Elsa bundan sonra kızağa hep Olaf ile sırayla bindi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama kızak çok küçüktü ve ikisi birden sığmadı"
   - Cümle 3: «Ama kızak çok küçüktü ve ikisi birden sığmadı.»
   - Açıklama: Kızağı Elsa istediği gibi buzdan yaptığı için küçük kalması akla yatkın bir sebep değil; daha büyüğünü yapabilirdi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0013` birebir aynı, `@degisim: çekmece -> kızak` (tutuyorsan), ardından `@onarim: 3eebc80483a0646d4f87d57492e9b0aae4cb54cc`, sonra gövde.

### Hikâye 7: tohum elsa-0014 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0014
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'ceviz', fiil 'asmak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: ağacın dallarında hiç ceviz yoktu | buzdan minicik cevizler yapıp dallara astı
@tohum: elsa-0014
Rüzgar dağın tepesinde hafifçe esiyordu. Elsa sarayın önünde bahçe oyunu oynuyordu. Ama ağacın dallarında hiç ceviz yoktu, çünkü karlı dağda ceviz olmazdı. Elsa boş dallara baktı ve biraz düşündü. Sonra elini açtı ve buzdan minicik cevizler yaptı. Cevizleri tek tek dallara astı. Birkaç adım geri gidip ağaca baktı. Dallarda şimdi parlak cevizler vardı. Rüzgar esince cevizler birbirine değdi ve hafif bir ses çıkardı. Elsa gülerek ellerini çırptı. Elsa çok mutlu oldu, çünkü ağacın dallarında artık ceviz vardı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağacın dallarında hiç ceviz yoktu"
   - Cümle 3: «Ama ağacın dallarında hiç ceviz yoktu, çünkü karlı dağda ceviz olmazdı.»
   - Açıklama: Bahçe oyunu oynayan Elsa için dalda ceviz olmaması neden önemli belli değil; sorun çocuğun önemseyeceği bir hedefe bağlanmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ağacın dallarında hiç ceviz yoktu"
   - Cümle 3: «Ama ağacın dallarında hiç ceviz yoktu, çünkü karlı dağda ceviz olmazdı.»
   - Açıklama: Elsa'nın neden cevize ihtiyaç duyduğu söylenmiyor; karlı dağda ceviz olmaması çocuğun önemseyeceği bir sorun olarak kurulmamış.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çünkü ağacın dallarında artık ceviz vardı"
   - Cümle 11: «Elsa çok mutlu oldu, çünkü ağacın dallarında artık ceviz vardı.»
   - Açıklama: Dallarda ceviz olduğu 8. cümlede söylendikten sonra gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0014` birebir aynı, ardından `@onarim: b6e8c32dbc899ecc80634087938de7aa1171c76e`, sonra gövde.

### Hikâye 8: tohum elsa-0015 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0015
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kazak', fiil 'girmek', sıfat 'sıcacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: tünel dardı ve iki kardeş sıkıştı | sırayla girmeyi önerdi ve ikisi sırayla geçti
@tohum: elsa-0015
Ormanda karlı ağaçların arasında Elsa buzdan kısa bir tünel yaptı. Elsa ile Anna aynı anda tünele girmek istedi. Ama tünel dardı ve iki kardeş kapıda sıkıştı. İkisi birbirine baktı ve güldü. "Sırayla girelim, önce sen geç, Anna," dedi Elsa. Anna tünele girdi ve öbür taraftan çıktı. Sıcacık kırmızı kazağı karla bembeyaz olmuştu. Anna kazağını silkti ve el salladı. "Sıra sende, Elsa!" dedi Anna. Elsa da tünelden geçti ve kardeşinin yanına çıktı. İkisi sırayla üç kez daha geçti. Elsa çok sevindi, çünkü sırayla girince ikisi de eğlenmişti.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "tünel dardı ve iki kardeş kapıda sıkıştı"
   - Cümle 3: «Ama tünel dardı ve iki kardeş kapıda sıkıştı.»
   - Açıklama: Dar bir kar/buz tüneline girip sıkışmak çocuğun taklit edebileceği tehlikeli bir davranış.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "iki kardeş kapıda sıkıştı"
   - Cümle 3: «Ama tünel dardı ve iki kardeş kapıda sıkıştı.»
   - Açıklama: Dar bir kar/buz tüneline girip sıkışmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Dar bir tünele girip sıkışmak çocuğun taklit edebileceği tehlikeli bir davranış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki kardeş kapıda sıkıştı"
   - Cümle 3: «Ama tünel dardı ve iki kardeş kapıda sıkıştı.»
   - Açıklama: Buzdan tünelin kapısı yok; 'tünelin girişinde' olmalı.
   - Açıklama: Buzdan tünelin kapısı yok; 'kapı' yanlış anlamda, 'girişte' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sıcacık kırmızı kazağı karla bembeyaz olmuştu"
   - Cümle 7: «Sıcacık kırmızı kazağı karla bembeyaz olmuştu.»
   - Açıklama: Anna'nın karlanan kazağı olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Kazağın beyazlaması sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0015` birebir aynı, ardından `@onarim: f8f720585725eb9df1016b5f25da05e40c38ea68`, sonra gövde.

### Hikâye 9: tohum elsa-0017 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0017
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'sandalye', fiil 'hazırlamak', sıfat 'ahşap'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: yorgun arkadaşın oturacak kuru bir yeri yoktu | kendi ahşap sandalyesini ona verdi
@tohum: elsa-0017
Elsa limanda denizi seyrediyordu. Kristoff uzun süre kızağını yüklemişti ve çok yorgundu. Ama kıyıdaki taşlar ıslaktı ve oturacak kuru bir yer yoktu. Elsa'nın yanında kraliçe için konmuş ahşap bir sandalye duruyordu. "Kristoff, gel, bu sandalyeye sen otur," dedi Elsa. "Ama bu sandalye senin," dedi Kristoff. "Sen benden daha yorgunsun," dedi Elsa. Kristoff teşekkür etti ve sandalyeye oturdu. Elsa da sandalyenin yanında durdu. İkisi birlikte denizdeki küçük dalgalara baktı. Biraz sonra Kristoff dinlendi ve kalktı. Sonra Elsa ile Kristoff kızağı birlikte mutlu mutlu hazırladı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kraliçe için konmuş ahşap bir sandalye"
   - Cümle 4: «Elsa'nın yanında kraliçe için konmuş ahşap bir sandalye duruyordu.»
   - Açıklama: Sandalye tam gerektiği anda sebepsizce beliriyor ve çözümü hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0017` birebir aynı, ardından `@onarim: 4e588c5f12d37648408873356ffb2d9429b9de1f`, sonra gövde.

### Hikâye 10: tohum elsa-0019 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0019
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'şeftali', fiil 'değişmek', sıfat 'çilekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: arkadaşı geldi ama onun hiç yiyeceği yoktu | şeftaliyi ona verdi ve keki ikiye böldü
@tohum: elsa-0019
@degisim: değişmek -> paylaşmak
Bir sabah Elsa sarayın önünde sepetini açtı. Sepette bir şeftali ile çilekli bir kek vardı. O sırada Olaf geldi ama onun hiç yiyeceği yoktu. Olaf sepete baktı ve sessizce bekledi. Elsa, Olaf'ın yazı çok sevdiğini biliyordu. Şeftaliyi ona uzattı, çünkü şeftali yaz gibi kokuyordu. Sonra çilekli keki elleriyle ikiye böldü. Elsa elini salladı ve buzdan iki küçük tabak yaptı. Kekin yarısını Olaf'ın tabağına koydu. Olaf kocaman gülümsedi ve Elsa'ya sarıldı. İkisi yan yana oturdu ve keklerini mutlu mutlu yedi. Elsa bundan sonra yiyeceklerini hep Olaf ile paylaştı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bir sabah Elsa sarayın önünde sepetini açtı"
   - Cümle 1: «Bir sabah Elsa sarayın önünde sepetini açtı.»
   - Açıklama: Başlıktaki yer dağ ama hikaye sarayın önünde geçiyor ve dağ hiç kurulmuyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa sarayın önünde sepetini açtı"
   - Cümle 1: «Bir sabah Elsa sarayın önünde sepetini açtı.»
   - Açıklama: Başlıktaki yer dağ ama hikaye sarayın önünde geçiyor ve dağ hiç anılmıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çünkü şeftali yaz gibi kokuyordu"
   - Cümle 6: «Şeftaliyi ona uzattı, çünkü şeftali yaz gibi kokuyordu.»
   - Açıklama: 'Yaz gibi kokmak' soyut bir benzetme; 3 yaşındaki çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şeftali yaz gibi kokuyordu"
   - Cümle 6: «Şeftaliyi ona uzattı, çünkü şeftali yaz gibi kokuyordu.»
   - Açıklama: 'Yaz gibi kokmak' soyut bir benzetme, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0019` birebir aynı, `@degisim: değişmek -> paylaşmak` (tutuyorsan), ardından `@onarim: 70c9bc019328fc661885acf684095346cacd49ec`, sonra gövde.

### Hikâye 11: tohum elsa-0020 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0020
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bileklik', fiil 'ulaşmak', sıfat 'yepyeni'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik kaygan yolda havuç sepetine ulaşamadı | kendi pelerinini yola serdi ve geyik geçti
@tohum: elsa-0020
@degisim: bileklik -> havuç
Rüzgar dağda hafifçe esiyordu. Elsa sarayın kapısına Sven için bir sepet havuç koymuştu. Ama kapıya giden yol çok kaygandı ve Sven sepete ulaşamadı. Sven her adımda kaydı ve geri çekildi. "Üzülme, Sven, sana yardım edeceğim," dedi Elsa. Kraliçe Elsa yepyeni pelerinini omzundan çıkardı. Pelerini kaygan yolun üstüne uzun uzun serdi. Sven pelerinin üstüne bastı ve bu kez hiç kaymadı. Yavaş yavaş yürüdü ve kapıya ulaştı. Sepetteki havuçları görünce sevinçle başını salladı. Elsa pelerinini yerden topladı. Sven havuçlarını mutlu mutlu yedi ve Elsa da sevinçle güldü.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa sarayın kapısına Sven için bir sepet havuç koymuştu"
   - Cümle 2: «Elsa sarayın kapısına Sven için bir sepet havuç koymuştu.»
   - Açıklama: Elsa sepeti Sven'e kendisi götürebilecekken sorun zorlama bir sebebe dayanıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa yepyeni pelerinini"
   - Cümle 6: «Kraliçe Elsa yepyeni pelerinini omzundan çıkardı.»
   - Açıklama: Zaten tanınan Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Önceden tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa yepyeni pelerinini"
   - Cümle 6: «Kraliçe Elsa yepyeni pelerinini omzundan çıkardı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak anılıyor.
   - Açıklama: Tohum özelliği kraliçelik yalnız unvan olarak anılıyor, kartındaki gibi çözümde işe yaramıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yolun üstüne uzun uzun serdi"
   - Cümle 7: «Pelerini kaygan yolun üstüne uzun uzun serdi.»
   - Açıklama: 'Uzun uzun' uzun süre demektir; pelerini boylu boyunca sermek için yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0020` birebir aynı, `@degisim: bileklik -> havuç` (tutuyorsan), ardından `@onarim: 1d164cb2167d2d77a137abe8b54cbad89b1652da`, sonra gövde.

### Hikâye 12: tohum elsa-0021 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0021
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'hediye', fiil 'güzelleşmek', sıfat 'beyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: limanda kıyıdan tık tık diye bir ses geldi | kardeşinin önünde yürüdü ve sesi yapan kabuğu buldu
@tohum: elsa-0021
Rüzgar esiyordu ve limanın kıyısından tık tık diye bir ses geliyordu. Elsa ile Anna bu sesi çok merak etti. Sesin nereden geldiğini bulmak istediler. "Önce ben bakayım, Anna," dedi Elsa. Elsa bir kraliçe olarak kardeşinin önünde yürüdü. İkisi büyük bir taşın arkasına baktı. Orada beyaz bir kabuk rüzgarla sallanıyor ve taşa çarpıyordu. "Ses buradan geliyormuş!" dedi Anna. Anna kabuğu yerden kaldırdı ve üstündeki kumu sildi. Kabuk temizlenince daha da güzelleşti. "Bu sana hediye, Elsa," dedi Anna. Elsa kabuğu aldı ve kardeşine sarıldı. Elsa çok sevindi, çünkü sesin nereden geldiğini kardeşiyle birlikte bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "limanın kıyısından tık tık diye bir ses geliyordu"
   - Cümle 1: «Rüzgar esiyordu ve limanın kıyısından tık tık diye bir ses geliyordu.»
   - Açıklama: Sorun yalnız bir ses; çözülmesi gereken gerçek bir sorun ve sebebi baştan kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa bir kraliçe olarak"
   - Cümle 5: «Elsa bir kraliçe olarak kardeşinin önünde yürüdü.»
   - Açıklama: 'Bir kraliçe olarak' rol ve sorumluluk gibi soyut bir anlam taşıyor, 3 yaşındaki çocuğa uygun değil.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: ""Ses buradan geliyormuş!" dedi Anna"
   - Cümle 8: «"Ses buradan geliyormuş!" dedi Anna.»
   - Açıklama: Sesin kaynağını ikisi birlikte buluyor ve kabuğu Anna alıyor; çözüm Elsa'ya ait değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0021` birebir aynı, ardından `@onarim: daaa175fb9401e863ea7253bdcf68265189f177d`, sonra gövde.
