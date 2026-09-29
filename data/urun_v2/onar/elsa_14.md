# Editör görevi (onarım): Elsa, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0044 (deneme 3 -> 4)

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
Ormanda hafif bir rüzgar esiyordu. Kraliçe Elsa küçük bir yokuştan kızakla kayıyordu. Olaf da kaymak istedi ama onun kızağı yoktu. Olaf sabırsızdı, yokuşun dibinde yerinde zıplayıp bekliyordu. Kızak aşağıda, Olaf'ın hemen önünde durdu. "Gel, Olaf, bu kızak ikimize de yeter," dedi Elsa. İkisi kızağı yokuşun başına çekti. Elsa öne oturdu ve kızağın ipini iki eliyle tuttu. Olaf onun arkasına yerleşti ve ona sıkıca tutundu. Kızak yavaşça aşağı indi. Olaf kollarını açtı ve kahkahalarla güldü. "Birlikte çok daha eğlenceli!" dedi Olaf. Elsa ile Olaf mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa küçük bir yokuştan"
   - Cümle 2: «Kraliçe Elsa küçük bir yokuştan kızakla kayıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, paylaşma çözümünde işe yaramıyor (kart 'ozellikler').
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf sabırsızdı, yokuşun dibinde"
   - Cümle 4: «Olaf sabırsızdı, yokuşun dibinde yerinde zıplayıp bekliyordu.»
   - Açıklama: 'Sabırsız' soyut bir kişilik kelimesi ve karttaki özellik kelimesi değil; 3 yaşındaki çocuk için zor olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0044` birebir aynı, `@degisim: kayık -> kızak` (tutuyorsan), ardından `@onarim: 65c88ff207e78fdaeb38fcb1e54aaf6c982f130e`, sonra gövde.

### Hikâye 2: tohum elsa-0045 (deneme 3 -> 4)

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
@plan: yumuşak kardan yapılan kule yana devrildi | karı sıkıca bastırıp duvara yeni bir kule ekledi
@tohum: elsa-0045
@degisim: çekirdek -> duvar
Karlı dağda, buzdan sarayın yanında güneş parlıyordu. Kraliçe Elsa karla küçük bir kale yapıyordu. Ama kalenin uzun kulesi yumuşak kardandı ve birden yana devrildi. Elsa devrilen kuleye baktı ve biraz mutsuz oldu. Sonra yerden yeni kar aldı. Karı iki eliyle sıkıca bastırdı ve sert bir top yaptı. Bu sıkı kardan kalenin duvarına yeni bir kule ekledi. Elsa kuleye yavaşça dokundu. Yeni kule bu kez hiç devrilmedi ve duvarın üstünde dik durdu. Elsa kalesinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa karla küçük bir kale"
   - Cümle 2: «Kraliçe Elsa karla küçük bir kale yapıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa karla küçük"
   - Cümle 2: «Kraliçe Elsa karla küçük bir kale yapıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0045` birebir aynı, `@degisim: çekirdek -> duvar` (tutuyorsan), ardından `@onarim: 8abcb6a6c2aa390c77ee8d2046fe1f643fed27ff`, sonra gövde.

### Hikâye 3: tohum elsa-0046 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0046
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bayrak', fiil 'giyinmek', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: rüzgar gemideki ufak bayrağı duvarın arkasına uçurdu | salondan kendi bayrağını getirip kızağa bağladı
@tohum: elsa-0046
Rüzgar hafif hafif esiyordu. Elsa gemi oyunu için giyindi ve bahçedeki kızağa bindi. Kızak onun gemisiydi, ama rüzgar gemideki ufak bayrağı uçurdu. Bayrak duvarın arkasına düştü ve kayboldu. Bayrağı olmayan bir gemi yola çıkamazdı. Elsa duvara baktı, ama duvar çok yüksekti. Elsa biraz düşündü. O bu krallığın kraliçesiydi ve salonda kendi mavi bayrağı vardı. Elsa salona koştu ve mavi bayrağını getirdi. Onu kızağın önüne sıkıca bağladı. Rüzgar yine esti ve bayrak havada açıldı. Elsa gemisinde dik durdu ve uzaklara baktı. Elsa çok sevindi, çünkü gemisi artık yola çıkmaya hazırdı.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "bahçedeki kızağa bindi"
   - Cümle 2: «Elsa gemi oyunu için giyindi ve bahçedeki kızağa bindi.»
   - Açıklama: Şato tarifi büyük salonlar ve avlu diyor; bahçe tarifte yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kızak onun gemisiydi"
   - Cümle 3: «Kızak onun gemisiydi, ama rüzgar gemideki ufak bayrağı uçurdu.»
   - Açıklama: Kızağı gemi saymak mecazdır ve sonraki 'gemi' kelimeleri küçük çocuğun kafasını karıştırır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0046` birebir aynı, ardından `@onarim: 8a074f05196bb84b9daf21e2e792ea73093edc5c`, sonra gövde.

### Hikâye 4: tohum elsa-0047 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0047
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tarak', fiil 'gülümsemek', sıfat 'nazik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: tarak elinden kayıp derin karın içinde kayboldu | nazikçe yardım istedi ve geyiğin gösterdiği yeri kazdı
@tohum: elsa-0047
Karlı ormanda Kraliçe Elsa, Sven'in tüylerini tarıyordu. Birden tarak elinden kaydı ve kara düştü. Kar çok derindi ve tarak kayboldu. Elsa elleriyle aradı ama tarağı bulamadı. "Sven, tarağı bulmama yardım eder misin?" diye nazikçe sordu Elsa. Sven burnunu kara soktu ve kokladı. Bir yerde durdu ve ayağıyla karı gösterdi. Elsa orayı kazdı ve tarağı karın içinden çıkardı. Elsa gülümsedi ve Sven'in başını okşadı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Elsa çok sevindi, çünkü yardım isteyince tarağını bulmuştu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Karlı ormanda Kraliçe Elsa"
   - Cümle 1: «Karlı ormanda Kraliçe Elsa, Sven'in tüylerini tarıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor (kart 'ozellikler').
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, tarağı bulmada işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0047` birebir aynı, ardından `@onarim: 9b3c21c5752b0ce716ff22f2859199bdfae43ead`, sonra gövde.

### Hikâye 5: tohum elsa-0050 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0050
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sırayla oynamak
- yan: Anna
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'alet', fiil 'yıkanmak', sıfat 'şapkalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: iki kardeş tek kar aletini aynı anda istedi | sırayla kullanmayı önerdi ve pencereye buzdan cam yaptı
@tohum: elsa-0050
@degisim: yıkanmak -> beklemek
Ormanda Elsa ile şapkalı Anna kardan bir kale yapıyordu. Ama ellerinde tek bir kar aleti vardı. İkisi de aleti aynı anda istedi. "Önce ben kazacağım!" dedi Anna. Elsa biraz düşündü. "Sırayla kullanalım, Anna, önce sen başla," dedi Elsa. Anna aletle kaleye güzel bir kapı açtı. Elsa da sırasını bekledi. Biraz sonra Anna aleti Elsa'ya verdi. Elsa aletle kaleye küçük bir pencere açtı. Sonra elini salladı ve pencereye buzdan ince bir cam yaptı. "Kalemiz çok güzel oldu, Elsa!" dedi Anna. Elsa çok sevindi, çünkü sırayla oynayınca kaleyi birlikte bitirmişlerdi.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sırayla kullanmayı önerdi ve pencereye buzdan cam yaptı"
   - Cümle 0 (plan satırı): «iki kardeş tek kar aletini aynı anda istedi | sırayla kullanmayı önerdi ve pencereye buzdan cam yaptı»
   - Açıklama: Buzdan cam yapmak sorunun çözümünün parçası değil; plan çözümü yanlış söylüyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "pencereye buzdan cam yaptı"
   - Cümle 0 (plan satırı): «iki kardeş tek kar aletini aynı anda istedi | sırayla kullanmayı önerdi ve pencereye buzdan cam yaptı»
   - Açıklama: Buzdan cam yapmak sırayla kullanma sorununun çözümü değil, plan çözümü yanlış söylüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "pencereye buzdan ince bir cam yaptı"
   - Cümle 11: «Sonra elini salladı ve pencereye buzdan ince bir cam yaptı.»
   - Açıklama: Buzdan cam sorunla ilgisiz ve sıra sorunundan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0050` birebir aynı, `@degisim: yıkanmak -> beklemek` (tutuyorsan), ardından `@onarim: fd7ebd25a1139245ba5ff0e051eac0e02c207e0a`, sonra gövde.

### Hikâye 6: tohum elsa-0051 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0051
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yelken', fiil 'susmak', sıfat 'masmavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yelken rüzgara ters durduğu için kızak kaymadı | susup rüzgarı dinledi ve yelkeni rüzgara çevirdi
@tohum: elsa-0051
Bir sabah Kraliçe Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu. Kızağa uzun bir dal dikmiş ve pelerinini yelken yapmıştı. Ama kızak hiç kaymadı, çünkü yelken rüzgara ters duruyordu. Elsa sustu ve rüzgarı dikkatle dinledi. Rüzgar kızağın sağ yanından esiyordu. Elsa yelkeni rüzgara doğru çevirdi. Yelken birden şişti. Kızak düz karın üstünde yavaş yavaş kaymaya başladı. Elsa kızağın içinde oturdu ve güldü. Kızak masmavi gökyüzünün altında sarayın önünde bir tur attı. Elsa çok sevindi, çünkü yeni bir şeyi denemiş ve başarmıştı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa dağda"
   - Cümle 1: «Bir sabah Kraliçe Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor (kart 'ozellikler').
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa dağda, sarayının önünde yelkenli bir kızak deniyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir; kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa sustu ve rüzgarı"
   - Cümle 4: «Elsa sustu ve rüzgarı dikkatle dinledi.»
   - Açıklama: Elsa daha önce konuşmadığı için 'sustu' fiili bağlama uymuyor.
   - Açıklama: Elsa konuşmuyordu; 'sustu' fiili bağlama uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0051` birebir aynı, ardından `@onarim: 9d71cc5694985ce3c90e7a375bc62539d390a45d`, sonra gövde.

### Hikâye 7: tohum elsa-0052 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0052
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yağmurluk', fiil 'çalışmak', sıfat 'enerjik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: önüne bakmadan koştu ve havuçları karda dağıttı | özür diledi, havuçları bulup buzdan kaseye koydu
@tohum: elsa-0052
@degisim: yağmurluk -> havuç
Karlı ağaçların arasında hafif bir rüzgar esiyordu. Elsa ile enerjik Sven karda koşup oynuyordu. Elsa önüne bakmadan koştu ve Sven'in havuçlarını karın içine dağıttı. Sven burnuyla karı kokladı ve üzgün bir ses çıkardı. "Özür dilerim, Sven, havuçlarını ben dağıttım," dedi Elsa. Sonra ikisi havuçları bulmak için birlikte çalıştı. Sven burnuyla, Elsa da elleriyle havuçları tek tek buldu. Elsa elini salladı ve buzdan küçük bir kase yaptı. Havuçları kaseye koydu ve Sven'in önüne bıraktı. Sven başını Elsa'ya sürttü ve bir havuç yedi. Elsa bundan sonra ormanda koşarken hep önüne baktı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sven'in havuçlarını karın içine dağıttı"
   - Cümle 3: «Elsa önüne bakmadan koştu ve Sven'in havuçlarını karın içine dağıttı.»
   - Açıklama: Havuçlar daha önce hiç kurulmadan sebepsiz beliriyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa elini salladı ve buzdan küçük bir kase yaptı"
   - Cümle 8: «Elsa elini salladı ve buzdan küçük bir kase yaptı.»
   - Açıklama: Çözüm özür, arama ve buzdan kase yapma olarak iki adımı aşıyor; kase sorunun sebebine yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0052` birebir aynı, `@degisim: yağmurluk -> havuç` (tutuyorsan), ardından `@onarim: 6781bfe94fd8f979570c1d98cc738fc5ba923063`, sonra gövde.

### Hikâye 8: tohum elsa-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Kristoff
@tohum: elsa-0053
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'dolap', fiil 'denemek', sıfat 'çabuk'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | şato | Kristoff
@plan: acele edince eldivenleri bir dolaba koydu ve unuttu | özür diledi ve dolapları açıp eldivenleri buldu
@tohum: elsa-0053
Dışarıda kar sessizce yağıyordu. Elsa sarayın salonunu çabuk çabuk topluyordu. Acele edince Kristoff'un eldivenlerini bir dolaba koydu ve bunu unuttu. Kristoff dışarı çıkmak istedi, ama eldivenlerini bulamadı. "Elsa, eldivenlerimi gördün mü?" diye sordu Kristoff. "Özür dilerim, Kristoff, onları ben bir dolaba koydum," dedi Elsa. Ama salonda çok dolap vardı. Elsa bu sarayın kraliçesiydi ve salondaki dolapları iyi bilirdi. Önce büyük dolaba baktı, ama eldivenler orada yoktu. Sonra kapının yanındaki küçük dolabı açmayı denedi. Eldivenler oradaydı! Elsa eldivenleri Kristoff'a verdi. "Teşekkürler, Elsa, hadi şimdi birlikte dışarıda oynayalım!" dedi Kristoff.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 8: «Elsa bu sarayın kraliçesiydi ve salondaki dolapları iyi bilirdi.»
   - Açıklama: Kraliçe olmak dolapları bilmesinin gerekçesi yapılıyor ama Elsa yine yanlış dolaba bakıyor, özellik işe yaramıyor (kart 'ozellikler').
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve salondaki dolapları iyi bilirdi"
   - Cümle 8: «Elsa bu sarayın kraliçesiydi ve salondaki dolapları iyi bilirdi.»
   - Açıklama: Tohumdaki kraliçe özelliği anılıyor ama çözüme yaramıyor; Elsa dolapları yine deneyerek arıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve salondaki dolapları iyi bilirdi"
   - Cümle 8: «Elsa bu sarayın kraliçesiydi ve salondaki dolapları iyi bilirdi.»
   - Açıklama: Dolapları iyi bildiği işe yarayacakmış gibi kuruluyor ama Elsa yine de yanlış dolaba bakıyor, ayrıntı kullanılmıyor.
   - Açıklama: Dolapları iyi bildiği söylenen ayrıntı işe yaramıyor, Elsa yine önce yanlış dolaba bakıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük dolabı açmayı denedi"
   - Cümle 10: «Sonra kapının yanındaki küçük dolabı açmayı denedi.»
   - Açıklama: Dolabı açmayı denedi deniyor ama açtığı söylenmeden eldivenler bulunuyor; fiil yanlış seçilmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0053` birebir aynı, ardından `@onarim: 733734984d61d9146ba72fd0416e73a0e4934e16`, sonra gövde.

### Hikâye 9: tohum elsa-0054 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0054
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: kaybolan eşya
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kupa', fiil 'çoğalmak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: yağan kar çoğaldı ve kupanın üstünü kapattı | buzdan bir kürek yapıp karı kenara itti
@tohum: elsa-0054
Elsa karlı ormanda kırmızı kupasına kozalak topluyordu. Kupayı bir ağacın dibine bıraktı ve yeni kozalaklar aramaya gitti. Bu sırada yağan kar çoğaldı ve kupanın üstünü tamamen kapattı. Elsa geri döndü, ama kupasını göremedi. Her yer bembeyazdı. Elsa ağaçların diplerine tek tek baktı. Bir ağacın dibinde karın içinden kırmızı bir şey görünüyordu. Elsa elini salladı ve buzdan küçük bir kürek yaptı. Kürekle karı yavaşça kenara itti. Kırmızı kupa karın altından çıktı. Elsa kupanın içine baktı ve kozalakların hepsini gördü. Elsa çok memnundu, çünkü kupasını ve kozalaklarını bulmuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kupanın üstünü tamamen kapattı"
   - Cümle 3: «Bu sırada yağan kar çoğaldı ve kupanın üstünü tamamen kapattı.»
   - Açıklama: Kar kupayı tamamen kapattı deniyor ama sonra karın içinden kupanın kırmızısı görünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0054` birebir aynı, ardından `@onarim: ce450da3a3d30e4b0d93ad872063f08ee8a79856`, sonra gövde.

### Hikâye 10: tohum elsa-0055 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0055
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yumurta', fiil 'bölmek', sıfat 'kısa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: küçük yuva insanların geçtiği yolun hemen yanındaydı | taşları yuvanın önüne dizdi ve kısa bir duvar yaptı
@tohum: elsa-0055
@degisim: bölmek -> dizmek
Limanda hafif bir rüzgar esiyordu. Elsa kıyıda yürürken taşların arasında küçük bir yuva gördü. Yuvada üç küçük yumurta vardı, ama yuva yolun hemen yanındaydı. Yoldan geçen insanlar yumurtaları kırabilirdi. Elsa yuvaya elini sürmedi. Elsa bu krallığın kraliçesiydi ve küçük canlıları korurdu. Kıyıdan düz taşlar topladı ve onları yuvanın önüne yan yana dizdi. Yuvanın önünde kısa ama sağlam bir duvar oldu. Elsa yuvaya bir kez daha baktı ve yumurtaları saydı. Elsa çok sevindi, çünkü üç yumurta da artık güvendeydi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük canlıları korurdu"
   - Cümle 6: «Elsa bu krallığın kraliçesiydi ve küçük canlıları korurdu.»
   - Açıklama: 'Canlı' soyut bir kavram ve 3 yaşındaki çocuk için uygun değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bu krallığın kraliçesiydi"
   - Cümle 6: «Elsa bu krallığın kraliçesiydi ve küçük canlıları korurdu.»
   - Açıklama: 'Bu krallık' daha önce anılmadığı için neyi gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçesiydi ve küçük canlıları korurdu"
   - Cümle 6: «Elsa bu krallığın kraliçesiydi ve küçük canlıları korurdu.»
   - Açıklama: Kartın özellik alanı kraliçenin kız kardeşini koruduğunu söylüyor; özellik küçük canlıları korumaya kaydırılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0055` birebir aynı, `@degisim: bölmek -> dizmek` (tutuyorsan), ardından `@onarim: d07521f123c0fa70a4e1446f260642eb8d94ab20`, sonra gövde.

### Hikâye 11: tohum elsa-0056 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0056
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tartı', fiil 'alkışlamak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: zıplamayı izlemeyi unuttu ve arkadaşını dışarıda bıraktı | dışarı koşup özür diledi ve zıplamayı alkışladı
@tohum: elsa-0056
@degisim: tartı -> pencere
Elsa buzdan sarayının önünde Sven ile oynuyordu. Sven sağlam bacaklarıyla karda yüksek yüksek zıplıyordu. Ama Elsa ona bakmayı unuttu ve Sven'i dışarıda bırakıp saraya girdi. Sven karda yalnız kaldı ve başını öne eğdi. Elsa pencereden baktı ve Sven'in üzgün olduğunu gördü. Hemen dışarı koştu. Kraliçe Elsa, Sven'in önünde eğildi ve ondan özür diledi. Sonra karın üstüne oturdu ve yalnız Sven'e baktı. Sven yeniden zıpladı ve bu kez daha yükseğe çıktı. Elsa onu gülerek alkışladı. Sven de başını sevinçle Elsa'ya sürttü. Elsa çok sevindi, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Elsa ona bakmayı unuttu"
   - Cümle 3: «Ama Elsa ona bakmayı unuttu ve Sven'i dışarıda bırakıp saraya girdi.»
   - Açıklama: Elsa'nın Sven'i unutup saraya girmesinin sebebi söylenmiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Sven'in önünde eğildi"
   - Cümle 7: «Kraliçe Elsa, Sven'in önünde eğildi ve ondan özür diledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir; kız kardeşini korur) yalnız süs unvan olarak geçiyor, olayda işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0056` birebir aynı, `@degisim: tartı -> pencere` (tutuyorsan), ardından `@onarim: c3dadb0f9384f25491c01020a72bc4ff1958b61a`, sonra gövde.

### Hikâye 12: tohum elsa-0057 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0057
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'trompet', fiil 'küçültmek', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: rüzgar esti ve trompetin içine kar doldu | trompeti ters çevirip salladı ve karı döktü
@tohum: elsa-0057
@degisim: küçültmek -> sallamak
Dağın tepesinde Kraliçe Elsa, ışıltılı trompetiyle bir ses oyunu oynuyordu. Trompeti her çaldığında, ses dağlardan geri geliyordu. Ama birden rüzgar esti ve trompetin içine kar doldu. Elsa yine üfledi, ama trompetten hiç ses çıkmadı. Dağlardan da hiç ses gelmedi. Elsa trompetin içine baktı ve karı gördü. Trompeti ters çevirdi ve iki kez salladı. Bütün kar yere döküldü. Elsa bir kez daha üfledi ve trompet yüksek bir ses çıkardı. Ses dağlardan geri geldi ve Elsa güldü. Elsa bundan sonra rüzgar esince trompetinin ağzını eliyle kapattı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Dağın tepesinde Kraliçe Elsa"
   - Cümle 1: «Dağın tepesinde Kraliçe Elsa, ışıltılı trompetiyle bir ses oyunu oynuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, hikayede hiçbir işe yaramıyor (kart 'ozellikler').
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, trompet sorununun çözümünde hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0057` birebir aynı, `@degisim: küçültmek -> sallamak` (tutuyorsan), ardından `@onarim: 818a0c02e33fe9304e422b5c36561a1e1cc21eb6`, sonra gövde.
