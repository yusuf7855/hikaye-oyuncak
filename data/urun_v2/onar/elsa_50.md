# Editör görevi (onarım): Elsa, onarım partisi 50

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar50.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar50.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0176 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Sven
@tohum: elsa-0176
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'cetvel', fiil 'değmek', sıfat 'küçücük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Sven
@plan: geyiğin boynuzları alçak dallara takıldı | durmasını söyledi ve dalı kenara itti
@tohum: elsa-0176
@degisim: cetvel -> dal
Rüzgar hafifçe esiyordu. Elsa karlı ormanda Sven'i arıyordu. Sven iki dalın arasındaki küçücük yerden geçmek istemişti ama boynuzları takılmıştı. Sven başını çekti ama kurtulamadı. Dal her seferinde Sven'in başına değiyordu. Elsa kraliçeydi ve Sven'i korumak için hemen yanına koştu. "Sven, dur ve başını yavaşça aşağı indir," dedi Elsa. Sven hemen durdu ve başını indirdi. Elsa takılan dalı eliyle kenara itti. Sven'in boynuzları daldan kolayca çıktı. Sven sevinçle zıpladı ve Elsa'nın yanına geldi. "Aferin, Sven, beni çok güzel dinledin!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa karlı ormanda Sven'i arıyordu"
   - Cümle 2: «Elsa karlı ormanda Sven'i arıyordu.»
   - Açıklama: Arama kuruluyor ama Sven'in nasıl bulunduğu anlatılmadan olay takılmaya atlıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve Sven'i korumak"
   - Cümle 6: «Elsa kraliçeydi ve Sven'i korumak için hemen yanına koştu.»
   - Açıklama: Kartta özellik kız kardeşini korumak iken burada kraliçelik Sven'e uygulanıyor ve çözüme bir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0176` birebir aynı, `@degisim: cetvel -> dal` (tutuyorsan), ardından `@onarim: 47b751c4f98ae286449d864846e54004371e13f3`, sonra gövde.

### Hikâye 2: tohum elsa-0178 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0178
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kavun', fiil 'yatırmak', sıfat 'aydınlık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: kavun yokuştan aşağı yuvarlandı ve kaçtı | buzdan alçak bir duvar yapıp kavunu durdurdu
@tohum: elsa-0178
Ormanda aydınlık bir sabahtı. Elsa ile Olaf karda piknik oyunu oynuyordu ve Olaf bir kavun getirmişti. Ama Olaf kavunu yokuşa bıraktı ve kavun aşağı yuvarlandı. "Kavunum kaçıyor!" diye bağırdı Olaf. Elsa hemen elini salladı. Yokuşun sonunda buzdan alçak bir duvar yaptı. Kavun duvara hafifçe çarptı ve durdu. Olaf koşup kavunu aldı ve güldü. "Teşekkürler, Elsa, piknik kurtuldu!" dedi Olaf. Sonra ikisi piknik oyununa mutlu mutlu devam etti. Olaf bundan sonra kavunu hep düz bir yere yatırdı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aşağı yuvarlandı ve kaçtı"
   - Cümle 0 (plan satırı): «kavun yokuştan aşağı yuvarlandı ve kaçtı | buzdan alçak bir duvar yapıp kavunu durdurdu»
   - Açıklama: Kavun kaçmaz; fiil öznesine uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yokuştan aşağı yuvarlandı ve kaçtı"
   - Cümle 0 (plan satırı): «kavun yokuştan aşağı yuvarlandı ve kaçtı | buzdan alçak bir duvar yapıp kavunu durdurdu»
   - Açıklama: Kavun kaçmaz; fiil cansız özneye uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa, piknik kurtuldu"
   - Cümle 9: «"Teşekkürler, Elsa, piknik kurtuldu!" dedi Olaf.»
   - Açıklama: 'Piknik kurtuldu' mecazlı bir ifade; küçük çocuğa uygun değil.
   - Açıklama: 'Piknik kurtuldu' mecazlı ve soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0178` birebir aynı, ardından `@onarim: b95e07653fe10afb54a83cace9592bc770e9a6cb`, sonra gövde.

### Hikâye 3: tohum elsa-0180 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0180
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: bir şey yapmak
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'mücevher', fiil 'kaybetmek', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: sarayı gösteren tahta kirliydi ve ok görünmüyordu | tahtayı temiz karla sildi ve ok yeniden göründü
@tohum: elsa-0180
Bir sabah Elsa karlı ormanda yürüyordu. Yolun başında sarayı gösteren eski bir tahta vardı. Ama tahta çok kirliydi ve üstündeki ok görünmüyordu. Böyle kalırsa ormana gelenler yolu kaybederdi. Elsa kraliçeydi ve onları korumak istedi. Temiz karla tahtayı iyice sildi. Ok yeniden göründü. Okun ucundaki küçük mavi mücevher de güneşte parladı. Elsa birkaç adım geri gitti ve tahtaya baktı. Ok ve mavi mücevher ağaçların arasından uzaktan görünüyordu. Elsa çok sevindi, çünkü artık herkes sarayı kolayca bulacaktı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ormana gelenler yolu kaybederdi"
   - Cümle 4: «Böyle kalırsa ormana gelenler yolu kaybederdi.»
   - Açıklama: 'Kalırsa' ile 'kaybederdi' zaman uyumsuz ve 'yolunu' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve onları korumak istedi"
   - Cümle 5: «Elsa kraliçeydi ve onları korumak istedi.»
   - Açıklama: Kartın özellikler alanında kraliçelik kız kardeşini korumak olarak tanımlı; burada ormana gelenleri korumaya genişletilip etiket olarak kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Okun ucundaki küçük mavi mücevher"
   - Cümle 8: «Okun ucundaki küçük mavi mücevher de güneşte parladı.»
   - Açıklama: Mücevher sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "küçük mavi mücevher de güneşte parladı"
   - Cümle 8: «Okun ucundaki küçük mavi mücevher de güneşte parladı.»
   - Açıklama: Mavi mücevher sebepsiz beliriyor ve sorunun çözümüne bir katkısı yok.
5. **C5** (K merceği) — Son güvenli ve sorun çözülmüş ('sıcaklık' aranmaz).
   - Alıntı: "artık herkes sarayı kolayca bulacaktı"
   - Cümle 11: «Elsa çok sevindi, çünkü artık herkes sarayı kolayca bulacaktı.»
   - Açıklama: Korkunç sesin kaynağı hiç açıklanmadan hikaye bitiyor, son tam güvenli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0180` birebir aynı, ardından `@onarim: 852c34995a685130a675f05cb510500828f20c59`, sonra gövde.

### Hikâye 4: tohum elsa-0181 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0181
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'iplik', fiil 'kokmak', sıfat 'komik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik havuçlara dönerken kızağın ipi ağaca sarıldı | ters yöne dönmesini söyledi ve ip çözüldü
@tohum: elsa-0181
@degisim: iplik -> ip
Bir sabah Elsa ile Sven dağda, buz sarayının önündeydi. Sven'in çektiği küçük kızakta güzel kokan havuçlar vardı. Sven havuçlara ulaşmak isterken ağacın etrafında döndü ve ip ağaca sarıldı. Şimdi Sven ne öne ne de arkaya gidebiliyordu. Sven başını salladı ve komik bir ses çıkardı. Elsa gülümsedi ve Sven'in önüne geçti. "Sven, dur ve ağacın etrafında ters yöne bir kez dön," dedi Elsa. Sven kraliçesini hemen dinledi ve ters yöne döndü. İp ağaçtan çözüldü ve kızak yeniden serbest kaldı. Elsa kızaktan bir havuç aldı ve Sven'e verdi. "Aferin, Sven, şimdi afiyetle ye!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçesini hemen dinledi"
   - Cümle 8: «Sven kraliçesini hemen dinledi ve ters yöne döndü.»
   - Açıklama: Kartın özellikler alanındaki kraliçelik (kız kardeşini korur) burada Sven'in itaat etmesi olarak kartta olmayan biçimde kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0181` birebir aynı, `@degisim: iplik -> ip` (tutuyorsan), ardından `@onarim: d12f9e77b2cb27813017d0cdba42123a161f4081`, sonra gövde.

### Hikâye 5: tohum elsa-0183 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0183
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yıldız', fiil 'savrulmak', sıfat 'mor'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: ormanda garip bir ses ve karda delikler vardı | kardeşini durdurdu ve ağaca bakınca yemişleri gördü
@tohum: elsa-0183
Elsa, kardeşi Anna ile karlı ormanda yürüyordu. Birden yakından garip bir tık tık sesi geldi. Karda da yıldız gibi küçük delikler vardı. "Elsa, bu ses nereden geliyor?" diye sordu Anna. Anna sese doğru koşmak istedi. Kraliçe olan Elsa kardeşini korumak için onun elini tuttu. Deliklerin hep bir ağacın altında olduğunu gördü. "Anna, koşma, dur ve ağacın dallarına bak," dedi Elsa. Anna durdu ve başını kaldırdı. Rüzgar esince dallardan mor yemişler savruldu. Yemişler düşerken dallara çarptı ve aynı sesi çıkardı. Her yemiş karda bir delik açtı. "Sesi bu yemişler yapıyormuş!" dedi Anna. Elsa çok sevindi, çünkü sesin nereden geldiğini kardeşiyle bulmuştu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe olan Elsa kardeşini"
   - Cümle 6: «Kraliçe olan Elsa kardeşini korumak için onun elini tuttu.»
   - Açıklama: Elsa ilk cümlede tanıtılmışken 'Kraliçe olan Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe olan' diye yeniden tanıtılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dallardan mor yemişler savruldu"
   - Cümle 10: «Rüzgar esince dallardan mor yemişler savruldu.»
   - Açıklama: 'savruldu' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0183` birebir aynı, ardından `@onarim: ebb7727ed4bdf67dedfee21260e0ac6796e3a17a`, sonra gövde.

### Hikâye 6: tohum elsa-0185 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0185
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'içecek', fiil 'süzülmek', sıfat 'reçelli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: kuşları gösterirken arkadaşının bardağını devirdi | özür diledi ve kendi içeceğini onunla paylaştı
@tohum: elsa-0185
Limanda Kraliçe Elsa ile Kristoff yan yana oturuyordu. Önlerindeki taşta iki bardak içecek ve reçelli ekmek vardı. Elsa suyun üstünde süzülen kuşları gösterirken Kristoff'un bardağını devirdi. İçecek döküldü ve bardak boş kaldı. "Özür dilerim, Kristoff, dikkat etmedim," dedi Elsa. Elsa kendi bardağını aldı ve içeceğin yarısını Kristoff'a verdi. "Kristoff, al, bu yarısı senin," dedi Elsa. "Teşekkür ederim, Elsa," dedi Kristoff ve gülümsedi. Elsa ile Kristoff reçelli ekmeklerini yiyip kuşları mutlu mutlu izlediler.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Limanda Kraliçe Elsa ile Kristoff"
   - Cümle 1: «Limanda Kraliçe Elsa ile Kristoff yan yana oturuyordu.»
   - Açıklama: Tohumdaki kraliçe/koruma özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "al, bu yarısı senin"
   - Cümle 7: «"Kristoff, al, bu yarısı senin," dedi Elsa.»
   - Açıklama: 'bu yarısı' tamlaması bozuk; 'bu yarı senin' ya da 'yarısı senin' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0185` birebir aynı, ardından `@onarim: 4bb74589e073e1dbeb7022ba042c71b9474cb4b1`, sonra gövde.

### Hikâye 7: tohum elsa-0188 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0188
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'atkı', fiil 'sürmek', sıfat 'buzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: atkı yüksek ve buzlu bir dala takıldı | özür diledi ve buzdan bir çubukla atkıyı indirdi
@tohum: elsa-0188
@degisim: sürmek -> indirmek
Bir sabah Elsa ile Olaf karlı ormanda oynuyordu. Elsa şaka olsun diye Olaf'ın elindeki kırmızı atkıyı havaya attı. Ama atkı yüksek ve buzlu bir dala takıldı. "Atkı çok yüksekte kaldı!" dedi Olaf. "Özür dilerim, Olaf, bu şaka hiç iyi değildi," dedi Elsa. Sonra elinden çıkan buzla uzun bir çubuk yaptı. Çubukla atkıyı daldan yavaşça indirdi. Elsa atkıyı Olaf'a geri verdi. Olaf gülerek Elsa'ya sıkıca sarıldı. Elsa çok sevindi, çünkü arkadaşının atkısı yine elindeydi ve ikisi yeniden oynayabilirdi.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "arkadaşının atkısı yine elindeydi"
   - Cümle 10: «Elsa çok sevindi, çünkü arkadaşının atkısı yine elindeydi ve ikisi yeniden oynayabilirdi.»
   - Açıklama: 'elindeydi' zamirinin Elsa'nın mı Olaf'ın mı elini gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0188` birebir aynı, `@degisim: sürmek -> indirmek` (tutuyorsan), ardından `@onarim: 0844ca5524f8bf482073085b25c9440d4fc1669b`, sonra gövde.

### Hikâye 8: tohum elsa-0189 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0189
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'boncuk', fiil 'kirletmek', sıfat 'devasa'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: çamur kız kardeşinin boncuklarını kirletti | kardeşini sudan uzak tuttu ve boncuklarını paylaştı
@tohum: elsa-0189
@degisim: devasa -> büyük
Deniz kıyısında Elsa ile Anna boncuklarla kolye yapıyordu. Birden Anna'nın kutusu yere düştü. Yerdeki çamur bütün boncukları kirletti ve Anna'nın kolyesi yarım kaldı. Anna boncukları yıkamak için suya doğru koştu. Ama kıyıda su çok derindi. Kraliçe olan Elsa kardeşini korumak için hemen elini tuttu ve geri çekti. Anna durdu ve Elsa'nın yanına oturdu. Sonra Elsa kendi kutusunu açtı. Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi. Kutuda büyük, mavi bir boncuk da vardı. Elsa onu da kardeşine verdi. Anna mavi boncuğu kolyesinin ortasına taktı. Sonra Elsa ile Anna kolyelerini mutlu mutlu bitirdi.
```

**Hakem bulguları (7):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Anna boncukları yıkamak için suya doğru koştu"
   - Cümle 4: «Anna boncukları yıkamak için suya doğru koştu.»
   - Açıklama: Derin suya doğru koşmak çocuğun taklit edebileceği tehlikeli bir davranış; deniz tarifi de kimsenin suya girmediğini söylüyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "boncukları yıkamak için suya doğru koştu"
   - Cümle 4: «Anna boncukları yıkamak için suya doğru koştu.»
   - Açıklama: Derin suya doğru koşmak, sonradan durdurulsa da taklit edilebilecek tehlikeli bir davranış.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Anna boncukları yıkamak için suya doğru koştu"
   - Cümle 4: «Anna boncukları yıkamak için suya doğru koştu.»
   - Açıklama: Kirlenen boncuklara ek olarak derin suya koşma tehlikesi ikinci bir sorun açıyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama kıyıda su çok derindi"
   - Cümle 5: «Ama kıyıda su çok derindi.»
   - Açıklama: Kirlenen boncukların yanında Anna'nın derin suya koşması ikinci bir sorun olarak ekleniyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe olan Elsa kardeşini"
   - Cümle 6: «Kraliçe olan Elsa kardeşini korumak için hemen elini tuttu ve geri çekti.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe olan Elsa' diye yeniden tanıtılıyor ve 'elini' zamirinin kimin elini gösterdiği belirsiz.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe olan Elsa kardeşini korumak için hemen elini tuttu"
   - Cümle 6: «Kraliçe olan Elsa kardeşini korumak için hemen elini tuttu ve geri çekti.»
   - Açıklama: Zaten tanıtılmış Elsa 'Kraliçe olan Elsa' diye yeniden tanıtılıyor ve 'elini' kimin eli olduğu belli değil.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi"
   - Cümle 9: «Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi.»
   - Açıklama: Çözüm çamurlu boncukları temizlemeye yönelmiyor, önce kardeşini sudan çekip sonra boncuk paylaşarak dolaylı ve çok adımlı ilerliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0189` birebir aynı, `@degisim: devasa -> büyük` (tutuyorsan), ardından `@onarim: c48f5eb030173e74ffb94723fae2930cfd5d425b`, sonra gövde.

### Hikâye 9: tohum elsa-0190 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0190
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kürek', fiil 'basmak', sıfat 'hevesli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: dağ soğuk olduğu için hiç çiçek açmıyordu | buzdan çiçekler yapıp karın içine dikti
@tohum: elsa-0190
@degisim: hevesli -> güzel
Karlı dağın tepesinde Elsa bahçe oyunu oynuyordu. Elsa sarayın önüne güzel bir bahçe yapmak istiyordu. Ama dağ çok soğuktu ve orada hiç çiçek açmıyordu. Elsa karlı yere bakıp biraz düşündü. Sonra elinden çıkan buzla parlak çiçekler yaptı. Çiçekleri dikmek için bir kürek aldı. Ayağıyla küreğe bastı ve karda küçük çukurlar açtı. Çiçekleri tek tek çukurlara dikti. Güneşte buz çiçekler ışıl ışıl parladı. Sarayın önünde bir çiçek bahçesi oldu. Elsa, soğuk dağda da kendi çiçeklerini yapabileceğini öğrendi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dağ soğuk olduğu için hiç çiçek açmıyordu"
   - Cümle 0 (plan satırı): «dağ soğuk olduğu için hiç çiçek açmıyordu | buzdan çiçekler yapıp karın içine dikti»
   - Açıklama: Dağ çiçek açmaz; yer eki eksik, 'dağda' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa bahçe oyunu oynuyordu"
   - Cümle 1: «Karlı dağın tepesinde Elsa bahçe oyunu oynuyordu.»
   - Açıklama: 'Bahçe oyunu' belirsiz ve anlamı açık olmayan bir ifade.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çiçekleri dikmek için bir kürek aldı"
   - Cümle 6: «Çiçekleri dikmek için bir kürek aldı.»
   - Açıklama: Kürek karlı dağda hiçbir yerden gelmeden sebepsizce beliriyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Güneşte buz çiçekler ışıl"
   - Cümle 9: «Güneşte buz çiçekler ışıl ışıl parladı.»
   - Açıklama: Tamlama eki eksik; 'buz çiçekleri' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0190` birebir aynı, `@degisim: hevesli -> güzel` (tutuyorsan), ardından `@onarim: c2cb630c9509ddfc99d5701d2a587e7d7057cbc5`, sonra gövde.

### Hikâye 10: tohum elsa-0191 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0191
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: bir şey yapmak
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yüzük', fiil 'korunmak', sıfat 'utangaç'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: dal çok kuru olduğu için büküldüğünde kırıldı | buzdan kalın bir yüzük yaptı
@tohum: elsa-0191
@degisim: utangaç -> parlak
Elsa karlı ormanda kendine bir yüzük yapmak istiyordu. Yerden ince bir dal aldı ve yavaşça büktü. Ama dal çok kuruydu ve çıt diye kırıldı. Elsa ikinci bir dal denedi, o da kırıldı. Elsa kırık dallara bakıp biraz düşündü. Sonra elinden çıkan buzla bir yüzük yaptı. Yüzük kalın buzdan olduğu için iyi korundu. Parlak yüzüğü parmağına taktı ve elini salladı. Yüzük hiç kırılmadı ve parmağında çok güzel durdu. Elsa bundan sonra yüzük yaparken kuru dal kullanmadı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "olduğu için iyi korundu"
   - Cümle 7: «Yüzük kalın buzdan olduğu için iyi korundu.»
   - Açıklama: 'Korundu' yanlış anlamda; yüzüğün sağlam olduğu anlatılmak isteniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yüzük kalın buzdan olduğu için iyi korundu"
   - Cümle 7: «Yüzük kalın buzdan olduğu için iyi korundu.»
   - Açıklama: Yüzüğün neyden korunduğu belirsiz; cümle olaydan çıkmıyor ve işlevsiz.
   - Açıklama: Yüzüğün neden ya da neyden korunduğu belirsiz; cümle olaydan çıkmıyor ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0191` birebir aynı, `@degisim: utangaç -> parlak` (tutuyorsan), ardından `@onarim: 9c8894b42d294aa2c967523c1344210678776e0c`, sonra gövde.

### Hikâye 11: tohum elsa-0192 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0192
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kurabiye', fiil 'tanışmak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: sürpriz hazır olmadan arkadaşı erken geldi | ona kapıda gözlerini kapatmasını söyledi
@tohum: elsa-0192
@degisim: tanışmak -> hazırlamak
Karlı dağın tepesindeki sarayda Kraliçe Elsa bir sürpriz hazırlıyordu. Kristoff için masaya kurabiyeler dizmek istiyordu. Ama Kristoff erken geldi ve kapıyı açtı. Masa daha hazır değildi. Elsa hemen elini kaldırdı. "Kristoff, kapıda dur ve gözlerini kapat," dedi Elsa. Kristoff durdu ve gözlerini sıkıca kapattı. Elsa kurabiyeleri hızla masaya dizdi. "Şimdi bakabilirsin, Kristoff," dedi Elsa. Kristoff baktı ve kurabiyeleri gördü. "Ne şanslıyım, bu çok güzel bir sürpriz!" dedi Kristoff. İkisi kurabiyeleri birlikte yedi ve güldü. Elsa bundan sonra sürprizlerini hep erkenden hazırladı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sarayda Kraliçe Elsa bir sürpriz"
   - Cümle 1: «Karlı dağın tepesindeki sarayda Kraliçe Elsa bir sürpriz hazırlıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa bir sürpriz hazırlıyordu"
   - Cümle 1: «Karlı dağın tepesindeki sarayda Kraliçe Elsa bir sürpriz hazırlıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "tepesindeki sarayda Kraliçe Elsa"
   - Cümle 1: «Karlı dağın tepesindeki sarayda Kraliçe Elsa bir sürpriz hazırlıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ne şanslıyım, bu çok"
   - Cümle 11: «"Ne şanslıyım, bu çok güzel bir sürpriz!" dedi Kristoff.»
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0192` birebir aynı, `@degisim: tanışmak -> hazırlamak` (tutuyorsan), ardından `@onarim: e8ee5a036417723e553c1dbcc282dadc870a28a1`, sonra gövde.

### Hikâye 12: tohum elsa-0193 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0193
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'limonata', fiil 'düşünmek', sıfat 'mavi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: mavi bardak kara düşüp çatladı | özür diledi ve buzdan yeni bir bardak yaptı
@tohum: elsa-0193
Karlı ormanda Elsa ile Olaf bir kütüğün üstünde oturuyordu. Olaf şişeden mavi bardağına limonata doldurmuştu. Elsa aceleyle kalktı, bardağa çarptı ve bardak kara düşüp çatladı. Olaf çatlak bardağa üzgün üzgün baktı. "Limonata içmek istiyordum!" dedi Olaf. Elsa biraz düşündü. "Özür dilerim, Olaf, hiç dikkat etmedim," dedi Elsa. Sonra elinden çıkan buzla yeni bir bardak yaptı. Olaf şişede kalan limonatayı yeni bardağa doldurdu. Limonata serin ve güzeldi. Olaf limonatayı içti ve Elsa'ya sıkıca sarıldı. Elsa çok sevindi, çünkü Olaf yine gülüyordu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bardak kara düşüp çatladı"
   - Cümle 3: «Elsa aceleyle kalktı, bardağa çarptı ve bardak kara düşüp çatladı.»
   - Açıklama: Yumuşak kara düşen bir bardağın çatlaması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0193` birebir aynı, ardından `@onarim: de0b78367df1bdc73d72c8be1ca5659528743290`, sonra gövde.
